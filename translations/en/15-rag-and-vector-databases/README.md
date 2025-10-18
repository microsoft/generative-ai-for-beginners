<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T22:31:33+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "en"
}
-->
# Retrieval Augmented Generation (RAG) and Vector Databases

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.en.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

In the search applications lesson, we briefly explored how to integrate your own data into Large Language Models (LLMs). In this lesson, we will dive deeper into the concepts of grounding your data in your LLM application, the mechanics of the process, and the methods for storing data, including embeddings and text.

> **Video Coming Soon**

## Introduction

In this lesson, we will cover the following:

- An introduction to RAG: what it is and why it is used in artificial intelligence (AI).

- Understanding what vector databases are and creating one for our application.

- A practical example of how to integrate RAG into an application.

## Learning Goals

After completing this lesson, you will be able to:

- Explain the importance of RAG in data retrieval and processing.

- Set up a RAG application and ground your data to an LLM.

- Effectively integrate RAG and vector databases into LLM applications.

## Our Scenario: Enhancing our LLMs with our own data

For this lesson, we aim to incorporate our own notes into an education startup, enabling the chatbot to provide more information on various subjects. By using these notes, learners will be able to study more effectively, understand different topics better, and prepare for their exams more easily. To create our scenario, we will use:

- `Azure OpenAI:` the LLM we will use to build our chatbot.

- `AI for Beginners' lesson on Neural Networks:` this will serve as the data we ground our LLM on.

- `Azure AI Search` and `Azure Cosmos DB:` a vector database to store our data and create a search index.

Users will be able to create practice quizzes from their notes, revision flashcards, and concise summaries. To get started, let’s explore what RAG is and how it works:

## Retrieval Augmented Generation (RAG)

An LLM-powered chatbot processes user prompts to generate responses. It is designed to be interactive and engage users on a wide range of topics. However, its responses are limited to the context provided and its foundational training data. For example, GPT-4's knowledge cutoff is September 2021, meaning it lacks information about events that occurred after that date. Additionally, the data used to train LLMs excludes confidential information such as personal notes or a company's product manual.

### How RAGs (Retrieval Augmented Generation) Work

![drawing showing how RAGs work](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.en.png)

Suppose you want to deploy a chatbot that creates quizzes from your notes. You will need a connection to the knowledge base. This is where RAG comes into play. RAGs work as follows:

- **Knowledge base:** Before retrieval, documents need to be ingested and preprocessed, typically by breaking down large documents into smaller chunks, transforming them into text embeddings, and storing them in a database.

- **User Query:** The user asks a question.

- **Retrieval:** When a user asks a question, the embedding model retrieves relevant information from the knowledge base to provide more context, which is then incorporated into the prompt.

- **Augmented Generation:** The LLM enhances its response based on the retrieved data. This allows the generated response to be based not only on pre-trained data but also on relevant information from the added context. The retrieved data is used to augment the LLM's responses, and the LLM then returns an answer to the user's question.

![drawing showing how RAGs architecture](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.en.png)

The architecture for RAGs is implemented using transformers consisting of two parts: an encoder and a decoder. For example, when a user asks a question, the input text is 'encoded' into vectors that capture the meaning of words, and the vectors are 'decoded' into our document index to generate new text based on the user query. The LLM uses both an encoder-decoder model to generate the output.

Two approaches for implementing RAG, as proposed in the paper [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst), are:

- **_RAG-Sequence_**: Using retrieved documents to predict the best possible answer to a user query.

- **RAG-Token**: Using documents to generate the next token, then retrieving them to answer the user's query.

### Why Use RAGs?

- **Information richness:** Ensures text responses are up-to-date and current. This enhances performance on domain-specific tasks by accessing the internal knowledge base.

- Reduces fabrication by utilizing **verifiable data** in the knowledge base to provide context to user queries.

- It is **cost-effective** as it is more economical compared to fine-tuning an LLM.

## Creating a Knowledge Base

Our application is based on our personal data, specifically the Neural Network lesson from the AI For Beginners curriculum.

### Vector Databases

A vector database, unlike traditional databases, is a specialized database designed to store, manage, and search embedded vectors. It stores numerical representations of documents. Breaking down data into numerical embeddings makes it easier for our AI system to understand and process the data.

We store our embeddings in vector databases because LLMs have a limit on the number of tokens they accept as input. Since you cannot pass all embeddings to an LLM, we need to break them down into chunks. When a user asks a question, the embeddings most similar to the question will be returned along with the prompt. Chunking also reduces costs associated with the number of tokens passed through an LLM.

Some popular vector databases include Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant, and DeepLake. You can create an Azure Cosmos DB model using Azure CLI with the following command:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### From Text to Embeddings

Before storing our data, we need to convert it into vector embeddings. If you are working with large documents or long texts, you can chunk them based on the queries you expect. Chunking can be done at the sentence level or paragraph level. Since chunking derives meaning from the surrounding words, you can add additional context to a chunk, such as the document title or some text before or after the chunk. You can chunk the data as follows:

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

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Once chunked, we can embed our text using different embedding models. Some models you can use include: word2vec, ada-002 by OpenAI, Azure Computer Vision, and many more. The choice of model depends on the languages you're using, the type of content being encoded (text/images/audio), the size of input it can encode, and the length of the embedding output.

An example of embedded text using OpenAI's `text-embedding-ada-002` model is:
![an embedding of the word cat](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.en.png)

## Retrieval and Vector Search

When a user asks a question, the retriever transforms it into a vector using the query encoder. It then searches through our document search index for relevant vectors in the document that are related to the input. Once done, it converts both the input vector and document vectors into text and passes them through the LLM.

### Retrieval

Retrieval occurs when the system quickly finds documents from the index that meet the search criteria. The goal of the retriever is to get documents that will provide context and ground the LLM on your data.

There are several ways to perform searches within our database, such as:

- **Keyword search**: Used for text searches.

- **Semantic search**: Uses the semantic meaning of words.

- **Vector search**: Converts documents from text to vector representations using embedding models. Retrieval is done by querying the documents whose vector representations are closest to the user question.

- **Hybrid**: A combination of both keyword and vector search.

A challenge with retrieval arises when there is no similar response to the query in the database. In such cases, the system will return the best information it can find. However, you can use strategies like setting a maximum distance for relevance or using hybrid search, which combines both keyword and vector search. In this lesson, we will use hybrid search, combining vector and keyword search. We will store our data in a dataframe with columns containing the chunks as well as embeddings.

### Vector Similarity

The retriever searches through the knowledge database for embeddings that are close together, the nearest neighbors, as they are texts that are similar. When a user asks a query, it is first embedded and then matched with similar embeddings. A common measurement used to determine how similar different vectors are is cosine similarity, which is based on the angle between two vectors.

Other alternatives for measuring similarity include Euclidean distance, which calculates the straight line between vector endpoints, and dot product, which measures the sum of the products of corresponding elements of two vectors.

### Search Index

When performing retrieval, we need to build a search index for our knowledge base before conducting the search. An index stores our embeddings and can quickly retrieve the most similar chunks, even in a large database. We can create our index locally using:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

After querying the database, you may need to sort the results by relevance. A re-ranking LLM uses machine learning to improve the relevance of search results by ordering them from most to least relevant. Using Azure AI Search, re-ranking is done automatically with a semantic re-ranker. An example of how re-ranking works using nearest neighbors:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Bringing It All Together

The final step is integrating our LLM to generate responses grounded in our data. We can implement it as follows:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Evaluating Our Application

### Evaluation Metrics

- Quality of responses: Ensuring they sound natural, fluent, and human-like.

- Groundedness of the data: Evaluating whether the response is based on the supplied documents.

- Relevance: Assessing whether the response matches and relates to the question asked.

- Fluency: Ensuring the response is grammatically correct and makes sense.

## Use Cases for RAG (Retrieval Augmented Generation) and Vector Databases

There are many use cases where function calls can enhance your application, such as:

- Question and Answering: Grounding your company data to a chatbot that employees can use to ask questions.

- Recommendation Systems: Creating systems that match the most similar values, such as movies, restaurants, and more.

- Chatbot Services: Storing chat history and personalizing conversations based on user data.

- Image Search: Using vector embeddings for image recognition and anomaly detection.

## Summary

We have covered the fundamental aspects of RAG, from adding our data to the application, to the user query and output. To simplify the creation of RAG, you can use frameworks such as Semantic Kernel, LangChain, or Autogen.

## Assignment

To continue your learning about Retrieval Augmented Generation (RAG), you can:

- Build a front-end for the application using the framework of your choice.

- Use a framework, either LangChain or Semantic Kernel, to recreate your application.

Congratulations on completing the lesson 👏.

## Learning Does Not Stop Here, Continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue enhancing your knowledge of Generative AI!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.