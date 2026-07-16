# Retrieval Augmented Generation (RAG) and Vector Databases

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../translated_images/pcm/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

For di search applications lekshan, we bin tok small how to put your own data inside Large Language Models (LLMs). For dis lekshan, we go dig more inside di tori of how to ground your data for your LLM app, how di whole process dey work and di ways wey you fit store data, including both embeddings and text.

> **Video Go Soon Come**

## Introduction

For dis lekshan, we go talk about dis tins:

- Wetin RAG be, how e dey work and why dem dey use am for AI (artificial intelligence).

- Understand wetin vector databases be and how to create one for our app.

- Practical example for how to combine RAG inside app.

## Learning Goals

After you finish dis lekshan, you go fit:

- Talk wetin make RAG important for data retrieval and processing.

- Setup RAG application and ground your data inside one LLM

- How to properly combine RAG and Vector Databases for LLM Apps.

## Our Scenario: how we go take enhance our LLMs with our own data

For dis lekshan, we want put our own notes inside the education startup, wey go make the chatbot get more info about different subjects dem. Using di notes we get, learners go fit study well well and understand different topics, e go make am easy to revise for their exam. For create our scenario, we go use:

- `Azure OpenAI:` na di LLM we go use for create our chatbot

- `AI for beginners' lekshan on Neural Networks`: na dis data we go ground our LLM on top

- `Azure AI Search` and `Azure Cosmos DB:` na vector database we go use to store our data and create search index

Users go fit create practice quizzes from their notes, make revision flash cards and summarize am into small small crispy overviews. To start, mek we look wetin RAG be and how e dey work:

## Retrieval Augmented Generation (RAG)

One LLM powered chatbot dey process user prompts to create responses. E design to dey interactive and e dey yan with users on plenty different topics. But na di context wey e get dey limit e responses and wetin e learn from training. For example, GPT-4 knowledge cutoff na September 2021, so e no sabi wetin happen after that date. Plus, di data wey dem use train LLMs no include private info like personal notes or company's product manual.

### How RAGs (Retrieval Augmented Generation) dey work

![drawing showing how RAGs work](../../../translated_images/pcm/how-rag-works.f5d0ff63942bd3a6.webp)

Imagine say you wan deploy chatbot wey dey create quizzes from your notes, you go need make e connect with knowledge base. Na here RAG go help. RAGs dey work like dis:

- **Knowledge base:** Before retrieval, you gots make sure say di documents don enter and dem don preprocess am, usually e mean to break big documents into small small parts, convert dem to text embedding and save for database.

- **User Query:** user come ask question

- **Retrieval:** When user ask question, di embedding model go find better info from knowledge base to give more context wey Dey go join the prompt.

- **Augmented Generation:** LLM go improve e answer based on di data wey e retrieve. E no go only use pre-trained data but also di new info wey e add from di extra context. Di retrieved data dey use boost di LLM responses. LLM go then return answer back to user.

![drawing showing how RAGs architecture](../../../translated_images/pcm/encoder-decode.f2658c25d0eadee2.webp)

RAGs architecture dey based on transformers wey get two part: encoder and decoder. For example, if user ask question, di input text dey 'encode' into vectors wey capture word meaning, and di vectors dey 'decode' enter our document index and e dey generate new text wey base on user query. LLM dey use both encoder-decoder model to make output.

Two ways to implement RAG based on di paper: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) be:

- **_RAG-Sequence_** dey use retrieved documents to predict di best answer for user query

- **RAG-Token** dey use documents to generate next token, then retrieve am to answer user query

### Why you go use RAGs? 

- **Information richness:** dey make sure say di text answers dey up to date and correct. E dey make performance better for specific task by tapping the internal knowledge base.

- E dey reduce lie by using **verifiable data** inside knowledge base to give context for user questions.

- E dey **cost effective** because e cheap pass to fine-tune one LLM

## How to create knowledge base

Our app na based on our own personal data, dat one be di Neural Network lekshan for AI For Beginners curriculum.

### Vector Databases

Vector database no be like traditional database, na special database wey dem design to store, manage and search embedded vectors. E store numerical forms of documents. To break data into numerical embeddings go make am easier for our AI system to understand and process di data.

We dey store our embeddings for vector databases because LLMs get limit on how many tokens dem fit take for input. You no fit pass all di embeddings for one LLM, so we gots break am into chunks and when user ask question, di embeddings wey match di question go return with di prompt. Chunking go also reduce cost on tokens wey LLM go handle.

Some popular vector databases na Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant and DeepLake. You fit create Azure Cosmos DB model using Azure CLI with dis command:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### From text to embeddings

Before we save our data, we gots change am to vector embeddings first before e enter database. If you dey work with big documents or long texts, you fit break dem based on wetin question you expect. You fit break am for sentence level or paragraph level. Because chunking dey find meanings from words around am, you fit add extra context to chunk like document title or add some text before or after di chunk. You fit chunk data like dis:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If di last chunk no reach di minimum length, add am anyhow
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

After chunking, we fit then embed our text using different embedding models. Some models you fit use be: word2vec, ada-002 by OpenAI, Azure Computer Vision and plenty others. Which model you go pick depend on di languages wey you dey use, di kind content wey you encode (text/images/audio), di size of input e fit handle and di length of embedding output.

Example of embedded text using OpenAI's `text-embedding-ada-002` model na:
![an embedding of the word cat](../../../translated_images/pcm/cat.74cbd7946bc9ca38.webp)

## Retrieval and Vector Search

When user ask question, the retriever go turn am to vector using query encoder, e go then search through our document search index for relevant vectors wey relate to di input. After, e go convert both di input vector and document vectors back to text and pass am through LLM.

### Retrieval

Retrieval na when system try find documents wey match wetin search say quickly. Di aim of retriever na to get documents dem wey dem go use provide context and ground LLM for your data.

Several ways dey to do search inside our database, like:

- **Keyword search** - wey dem dey use for text search

- **Vector search** - e dey convert documents from text to vector using embedding models, e go let you do **semantic search** based on meaning of words. Retrieval na by to ask documents wey their vector representations dey closest to user question.

- **Hybrid** - combination of both keyword and vector search.

Main wahala with retrieval be say if no similar answer dey database for question, system go try bring best info wey e fit get, but you fit set maximum distance for relevance or use hybrid search wey combine keyword and vector search. For dis lekshan, we go use hybrid search, wey be mix of vector and keyword search. We go store our data inside dataframe with columns wey get chunks and embeddings.

### Vector Similarity

Retriever go search through knowledge database for embeddings wey close one another, di closest neighbour, because dem be texts wey similar. For scenario wey user ask question, e go first embed am then match with similar embeddings. Common way to measure similarity na cosine similarity wey take angle between two vectors.

We fit also use other ways to measure similarity like Euclidean distance wey na straight line between vector endpoints and dot product wey measure sum of products of corresponding elements of two vectors.

### Search index

Before retrieval, we gots build search index for knowledge base. Index go store embeddings and go fit quick find most similar chunks even if database big. We fit create index locally using:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Make di search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To find inside di index, you fit use di kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

After you don query the database, you fit need sort results from most relevant. Reranking LLM dey use Machine Learning to improve relevance of search results by arranging from most relevant. For Azure AI Search, reranking dey do automatically for you using semantic reranker. Example of how reranking dey work using nearest neighbours:

```python
# Find di most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print di most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Bringing am all together

Last step na to add our LLM inside the mix to fit get answer wey base for our data. We fit implement am like dis:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Change di question to one query vector
    query_vector = create_embeddings(user_input)

    # Find di documents wey dey most like am
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to di query to give context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # join di history and di user input together
    history.append(user_input)

    # make one message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use di Responses API to make response
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Evaluating our application

### Evaluation Metrics

- Quality of responses wey make am sound natural, fluent and human-like

- Groundedness of data: check if response come from supplied docs

- Relevance: check if response match and relate to question wey dem ask

- Fluency - check if response make sense grammatically

## Use Cases for using RAG (Retrieval Augmented Generation) and vector databases

Plenty different use cases dey where function calls fit improve your app like:

- Question and Answering: ground your company data to chat wey employees fit use ask questions.

- Recommendation Systems: create system wey go match closest similar values like movies, restaurants and plenty more.

- Chatbot services: store chat history and personalize conversation based on user data.

- Image search based on vector embeddings, useful for image recognition and anomaly detection.

## Summary

We don cover main areas of RAG from adding our data to app, user query and output. To make RAG creation easy, you fit use frameworks like Semanti Kernel, Langchain or Autogen.

## Assignment

To continue your learning for Retrieval Augmented Generation (RAG) you fit build:

- Build front-end for your app using framework wey you like

- Use framework like LangChain or Semantic Kernel, and recreate your app.

Congrats for finishing di lekshan 👏.

## Learning no stop for here, continue di Journey

After you finish dis lekshan, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->