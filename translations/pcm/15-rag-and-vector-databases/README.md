<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T19:44:10+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "pcm"
}
-->
# Retrieval Augmented Generation (RAG) and Vector Databases

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../../../translated_images/pcm/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

For di search applications lesson, we learn small how to integrate your own data inside Large Language Models (LLMs). For dis lesson, we go talk more about how to ground your data for your LLM application, how di process dey work and di methods to store data, including both embeddings and text.

> **Video Coming Soon**

## Introduction

For dis lesson, we go cover these tins:

- Intro to RAG, wetin e be and why dem dey use am for AI (artificial intelligence).

- Understand wetin vector databases be and how to create one for our application.

- One practical example how to integrate RAG inside one application.

## Learning Goals

After you finish dis lesson, you go sabi:

- Explain di importance of RAG for data retrieval and processing.

- Setup RAG application and ground your data to LLM

- How to integrate RAG and Vector Databases well well for LLM Applications.

## Our Scenario: how we go take improve our LLMs with our own data

For dis lesson, we wan add our own notes for education startup, weh go make chatbot fit get more information about different subjects dem. If we use di notes we get, learners go fit study better and understand different topics, e go make e easy to revise for their exams. To create our scenario, we go use:

- `Azure OpenAI:` na di LLM wey we go take create our chatbot

- `AI for beginners' lesson on Neural Networks`: na dis one be di data wey we go ground our LLM on top

- `Azure AI Search` and `Azure Cosmos DB:` na vector database wey go store our data and create search index

Users go fit create practice quizzes from their notes, get revision flash cards and summarize am into short overview dem. To start, make we check wetin RAG be and how e dey work:

## Retrieval Augmented Generation (RAG)

LLM powered chatbot dey process user prompts to generate answers. E join dey interactive and e dey talk with users on many kind topics. But di answers wey e dey give fit only reach as far as di context e get and di training data wey e base on. For example, GPT-4 knowledge cutoff na September 2021, mean say, e no sabi anything wey happen after dat time. Plus, di data wey dem use train LLM no include any confidential tins like personal notes or company product manual.

### How RAGs (Retrieval Augmented Generation) dey work

![drawing showing how RAGs work](../../../../../translated_images/pcm/how-rag-works.f5d0ff63942bd3a6.webp)

Make we suppose you want deploy one chatbot wey dey create quizzes from your notes, you go need connection to di knowledge base. Na here RAG go help. RAGs dey operate like dis:

- **Knowledge base:** Before retrieval, dem need take put these documents inside and preprocess am, usually dem go break big documents into smaller chunks, convert dem to text embedding and store for database.

- **User Query:** di user go ask question

- **Retrieval:** When user ask question, di embedding model go find correct info from our knowledge base to give extra context wey go join for di prompt.

- **Augmented Generation:** di LLM go improve im answer based on di data wey dem retrieve. E go make di answer no only dey based on pre-trained data but also di info from di added context. Di data wey dem pull go add to how LLM dey answer. LLM go then return answer give di user.

![drawing showing how RAGs architecture](../../../../../translated_images/pcm/encoder-decode.f2658c25d0eadee2.webp)

Di architecture for RAGs dey use transformers wey get two parts: encoder and decoder. For example, if user ask question, di input text 'encrypted' into vectors wey get di meaning of words then di vectors dey 'decoded' into our document index and e go generate new text based on di user query. Di LLM dey use encoder-decoder model to generate output.

Two ways to implement RAG according to di paper [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) be:

- **_RAG-Sequence_** wey use retrieved documents to guess di best answer to the user's question

- **RAG-Token** wey use documents to generate di next token, then retrieve them to answer di user's question

### Why you go use RAGs? 

- **Info rich:** e make sure say text answers dey up to date and current. E improve performance on domain specific tasks by taking info from inside the knowledge base.

- E reduce fake info by using **verifiable data** inside di knowledge base for context to user question.

- E cost less as e dey more cheap than to fine-tune LLM

## How to create knowledge base

Our application dey based on our personal data i.e., di Neural Network lesson for AI For Beginners curriculum.

### Vector Databases

Vector database, no be like normal databases, na special database wey dem design to store, manage and search embedded vectors. E store numerical representation of documents. Breaking down data to numerical embeddings make e easy for our AI system to understand and process data.

We dey store our embeddings inside vector databases as LLMs get limit on how many tokens dem fit accept as input. As you no fit pass all the embeddings to LLM, we go need cut dem into chunks and when user ask question, di embeddings wey match di question most go dey returned with di prompt. Chunking still dey reduce cost on how many tokens dem pass inside LLM.

Some vector databases wey popular include Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant and DeepLake. You fit create Azure Cosmos DB model using Azure CLI with dis command:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### From text to embeddings

Before we fit store our data, we go need change am to vector embeddings before e enter database. If your documents big or long, you fit break dem based on di questions you expect. You fit chunk am for sentence level or paragraph level. Because chunking dey take meaning from words wey dey around am, you fit add some other context to di chunk, like by adding di document title or put some text before or after di chunk. You fit chunk data like dis:

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

    # If di last chunk neva reach di minimum length, still add am anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

After you chunk am, you fit embed your text using different embedding models. Some models wey you fit use be: word2vec, ada-002 by OpenAI, Azure Computer Vision and plenty more. How you go select model depend on di languages you dey use, di content type encoded (text/images/audio), how big di input fit be and how long the embedding output be.

Example of embedded text using OpenAI's `text-embedding-ada-002` model be:
![an embedding of the word cat](../../../../../translated_images/pcm/cat.74cbd7946bc9ca38.webp)

## Retrieval and Vector Search

When user ask question, di retriever go turn am to vector using di query encoder, e go search our document search index for relevant vectors wey relate to di input. After dat, e go change both di input vector and document vectors to text and pass am through LLM.

### Retrieval

Retrieval na when system try find documents from index wey satisfy di search request sharp sharp. Di goal of di retriever be to find documents wey dem go use provide context and ground di LLM on your data.

There dey different ways to search inside our database like:

- **Keyword search** - to search text

- **Vector search** - to convert documents from text to vector using embedding models, e dey allow **semantic search** wey dey based on meaning of words. Retrieval go happen by querying documents wey their vector representations dey closest to user question.

- **Hybrid** - na mix of keyword and vector search.

One challenge with retrieval be say if no response wey resemble di query dey database, system go give best info wey e fit find, but you fit use methods like set max distance for relevance or use hybrid search wey combine keyword and vector search. For dis lesson, we go use hybrid search, mix of vector and keyword search. We go store data inside dataframe with columns wey get chunks and embeddings.

### Vector Similarity

Retriever go search inside knowledge database for embeddings wey close to each other, closest neighbour, as dem be texts wey get similarity. If user ask question, e go embed am then match am with similar embeddings. Di normal way wey dem dey take measure how vectors similar na cosine similarity, wey base on angle between two vectors.

Other ways to measure similarity na Euclidean distance, na straight line between vector endpoints, and dot product wey dey measure sum of products of corresponding elements of two vectors.

### Search index

When you dey do retrieval, you go need build search index for your knowledge base before search. Index go store embeddings and fit quickly return similar chunks even if database big. You fit create index locally using:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Make di search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query di index, yu fit use di kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

After you don query di database, you fit want arrange di results from di best relevant ones. Reranking LLM dey use Machine Learning to improve search result relevance by putting dem in order from most relevant. Using Azure AI Search, reranking dey automatic using semantic reranker. Example how reranking dey work with nearest neighbours:

```python
# Find di most kain documents wey resemble
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print di most kain documents wey resemble
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## How to put everything together

Last step na add our LLM join so e fit give answers wey dey ground on our data. We fit do am like dis:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Change di question come query vector
    query_vector = create_embeddings(user_input)

    # Find di most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query make e get context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # join di history and di user input
    history.append(user_input)

    # create one message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use chat completion make e generate answer
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## How to evaluate our application

### Evaluation Metrics

- Quality of responses: make sure answer sound natural, fluent and human-like

- Groundedness of data: check if answer dey based on docs wey you supply

- Relevance: check if answer match and relate to question wey dem ask

- Fluency - check if answer dey grammatically correct

## Use Cases for RAG (Retrieval Augmented Generation) and vector databases

Plenty use cases dey where function calls fit improve your app like:

- Question and Answering: ground your company data to chat wey employees fit use ask questions.

- Recommendation Systems: you fit create system wey match most similar tins like movies, restaurants and others.

- Chatbot services: you fit store chat history and personalize conversation based on user data.

- Image search based on vector embeddings, help for image recognition and anomaly detection.

## Summary

We don cover di main parts of RAG from how we take add our data to application, user query and output. To simplify RAG creation, you fit use frameworks like Semanti Kernel, Langchain or Autogen.

## Assignment

To continue learning Retrieval Augmented Generation (RAG), you fit build:

- Build front-end for the application using any framework you like

- Use framework like LangChain or Semantic Kernel, and remake your application.

Congrats for finishing di lesson 👏.

## Learning no stop here, continue di Journey

After you finish dis lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to dey improve your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) wey dem use translate am. Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or wrong tori. Di original document wey e dey for e original language na di correct one wey you suppose trust. If na serious info, e better make person wey sabi do human translation help. We no go responsible for any misunderstanding or wrong meaning wey fit show because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->