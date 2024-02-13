# Retrieval Augmented Generation (RAG) and Vector Databases

![chapter image](./images/)

In the search applications lesson, we learnt briefly how you can integrate your own data into Large Language Models (LLMs). In this lesson, we will delve further into the concepts of grounding your data in your LLM application, the mechanics of the process and the methods for storing data, including both embeddings and text.

> **Video Coming Soon**

## Introduction

In this lesson we will cover the following:

- An introduction to RAG, what it is and why it is used in AI (artificial intelligence).

- Understanding what vector databases are and creating one for our application.

- A practical example on how to integrate RAG into an application.

## Learning Goals

After completing this lesson, you will be able to:

- Explain the significance of RAG in data retrieval and processing.

- Setup RAG application and ground your data to an LLM

- Effective integration of RAG and Vector Databases in LLM Applications.

## Our Scenario: enhancing our LLMs with our own data

For this lesson, we want to add our own notes into the education startup, which allows the chatbot to get more information on the different subjects. Using the notes that we have, learners will be able to study better and understand the different topics, making it easier to revise for their examinations. To create our scenario, we will use:

- `Azure Open AI:` the LLM we will use to create our chatbot

- `AI for beginners' lesson on Neural Networks`: this will be the data we ground our LLM on

- `Azure AI Search` and `Azure Cosmos DB:` vector database to store our data and create a search index

Users will be able to create practice quizzes from their notes, revision flash cards and summarize it to concise overviews. To get started, let us look at what is RAG and how works:

## Retrieval Augmented Generation (RAG)

An LLM powered chatbot processes user prompts to generate responses. It is designed to be interactive and engages with users on a wide array of topics. However, its responses are limited to the context provided and its foundational training data. For instance, GPT-4 knowledge cut off is September 2021, meaning, it lacks knowledge of events that have occurred after this period. In addition, the data used to train LLMs excludes confidential information such as personal notes or a company's product manual.

### How RAGs (Retrieval Augmented Generation) work

![drawing showing how RAGs work](images/how-rag-works.png)

Suppose you want to deploy a chatbot that creates quizzes from your notes, you will require a connection to the knowledge base. This is where RAG comes to the rescue. RAGs operate as follows:

- **Knowledge base:** Before retrieval, these documents need to be ingested and preprocessed, typically breaking down large documents into smaller chunks, transforming them to text embedding and storing them in a database.

- **User Query:** the user asks a question

- **Retrieval:** When a user asks a question, the embedding model retrieves relevant information from our knowledge base to provide more context that will be incorporated into the prompt.

- **Augmented Generation:** the LLM enhances its response based on the data retrieved. It allows the response generated to be not only based on pre-trained data but also relevant information from the added context. The retrieved data is used to augment the LLM's responses. The LLM then returns an answer to the user's question.

![drawing showing how RAGs architecture](images/encoder-decode.png)

The architecture for RAGs is implemented using transformers consisting of two parts: an encoder and a decoder. For example, when a user asks a question, the input text 'encoded' into vectors capturing the meaning of words and the vectors are 'decoded' into our document index and generates new text based on the user query. The LLM uses both an encoder-decoder model to generate the output.

Two approaches when implementing RAG according to the proposed paper: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf) are:

- ***RAG-Sequence*** using retrieved documents to predict the best possible answer to a user query

- **RAG-Token** using documents to generate the next token, then retrieve them to answer the user's query

### Why would you use RAGs? 

- **Information richness:** ensures text responses are up to date and current. It, therefore, enhances performance on domain specific tasks by accessing the internal knowledge base.

- Reduces fabrication by utilizing **verifiable data** in the knowledge base to provide context to the user queries.

- It is **cost effective** as they are more economical compared to fine-tuning an LLM

## Creating a knowledge base

Our application is based on our personal data i.e., the Neural Network lesson on AI For Beginners curriculum.

### Vector Databases

A vector database, unlike traditional databases, is a specialized database designed to store, manage and search embedded vectors. It stores numerical representations of documents. Breaking down data to numerical embeddings makes it easier for our AI system to understand and process the data.

We store our embeddings in vector databases as LLMs have a limit of the number of tokens they accept as input. As you cannot pass the entire embeddings to an LLM, we will need to break them down into chunks and when a user asks a question, the embeddings most like the question will be returned together with the prompt. Chunking also reduces costs on  the number of tokens passed through an LLM.

Some popular vector databases include Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN,, Quadrants and DeepLake. You can create an Azure Cosmos DB model using azd as follows:

### From text to embeddings

Before we store our data, we will need to convert it to vector embeddings before it is stored in the database. If you are working with large documents or long texts, you can chunk them based on queries you expect. Chunking can be done at sentence level, or at a paragraph level. As chunking derives meanings from the words around them, you can add some other context to a chunk, for example, by adding the document title or including some text before or after the chunk.

Once chunked, we can then embed our text using different embedding models. Some models you can use include: word2vec, ada-002 by OpenAI, Azure Computer Vision and many more. Selecting a model to use will depend on the languages you're using, the type of content encoded (text/images/audio), the size of input it can encode and length of the embedding output.

An example of embedded text is:

## Retrieval and Vector Search

When a user asks a question, the retriever transforms it into a vector using the query encoder, it then searches the through our document search index for relevant vectors in the document that are related to the input. Once done, it converts both the input vector and document vectors into text and passes it through the LLM.

### Retrieval

Retrieval happens when the system tries to quickly find the documents from the index that satisfy the search criteria. The goal of the retriever is to get documents that will be used to provide context and ground the LLM on your data.

There are several ways to perform search within our database such as:

- *Keyword* search - used for text searches

- *Semantic* search - uses the semantic meaning of words

- *Vector* search - converts documents from text to vector representations using embedding models. Retrieval will be done by querying the documents whose vector representations are closest to the user question.

- *Hybrid* - a combination of both keyword and vector search.

A challenge with retrieval comes in when there is no similar response to the query in the database, the system will then return the best information they can get, however, you can use tactics like set up the maximum distance for relevance or use hybrid search that combines both keywords and vector search. In this lesson we will use hybrid search, a combination of both vector and keyword search.

### Vector Similarity

The retriever will search through the knowledge database for embeddings that are close together, the closest neighbour, as they are texts that are similar. In the scenario a user asks a query, it is first embedded then matched with similar embeddings. The common measurement that is used to find how similar different vectors are is cosine similarity which is based on the angle between two vectors.

> cosine similarity formula

We can measure similarity using other alternatives we can use are Euclidean distance which is the straight line between vector endpoints and dot product which measures the sum of the products of corresponding elements of two vectors.

### Search index

When doing retrieval, we will need to build a search index for our knowledge base before we perform search. An index will store our embeddings and can quickly retrieve the most similar chunks even in a large database. We can create our index locally using:

> Code to create a search index to be added

### Re-ranking

Once you have queried the database, you might need to sort the results from the most relevant. A reranking LLM utilizes Machine Learning to improve the relevance of search results by ordering them from the most relevant. Using Azure AI Search, reranking is done automatically for you using a semantic reranker. An example of how reranking works:

> semantic reranker

## Bringing it all together

The last step is adding our LLM into the mix to be able to get responses that are grounded on our data. We can implement it as follows:

> code

## Evaluating our application

### Evaluation Metrics

- Quality of responses supplied ensuring it sounds natural, fluent and human-like

- Groundedness of the data: evaluating whether the response that came from supplied docs

- Relevance: evaluating the response matches and is related to the question asked

- Fluency - whether the response makes sense grammatically

## Use Cases for using RAG and vector databases

There are many different use cases where function calls can improve your app like:

- Question and Answering: grounding your company data to a chat that can be used by employees to ask questions.

- Recommendation Systems: where you can create a sysytem that matches the most similar values e.g. movies, restaurants and many more.

- Chatbot services: you can store chat history and personalize the conversation based on the user data.

- Image search based on vector embeddings, useful when doing image recognition and anomaly detection.

## Summary

We have covered the fundamental areas of RAG from adding our data to the application, the user query and output. To simplify creation of RAG, you can use frameworks such as Semanti Kernel, Langchain or Autogen.

## Resources

- [Azure AI Search: Outperforming vector search with hybrid retrieval and ranking capabilities - Microsoft Community Hub](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167)

- [Get started with the Python enterprise chat sample using RAG - Python on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/python/get-started-app-chat-template?tabs=github-codespaces)

- [Generative AI for Beginners (microsoft.github.io)](https://microsoft.github.io/generative-ai-for-beginners/#/08-building-search-applications/README?wt.mc_id=academic-105485-koreyst) - how to build a search application

- [Quickly build and deploy OpenAI apps on Azure, infused with your own data (youtube.com)](https://www.youtube.com/watch?v=j8i-OM5kwiY) - Using Azure CLI to initialize, architect and deploy your applications.

- [Mastering RAG: How To Architect An Enterprise RAG System - Galileo (rungalileo.io)](https://www.rungalileo.io/blog/mastering-rag-how-to-architect-an-enterprise-rag-system) - non-Azure approach

- [Build A Production RAG with Azure AI and Prompt Flow (nitya.github.io)](https://nitya.github.io/contoso-chat/) - building with promptflow 

## Assignment

To continue your learning of Retrieval Augmented Generation (RAG) you can build:

- Build a front-end for the application using the framework of your choice

- Utilize a framework, either LangChain or Semantic Kernel, and recreate your application.

Congratulations for completing the lesson 👏.

## Learning does not stop here, continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](<https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst>) to continue leveling up your Generative AI knowledge!

Head over to Lesson 18 where we will look at how xxx](../xxxx?WT.mc_id=academic-105485-koreyst)!