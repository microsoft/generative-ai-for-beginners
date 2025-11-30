<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T22:29:57+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "en"
}
-->
# Building a Search Applications

[![Introduction to Generative AI and Large Language Models](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.en.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Click the image above to watch the video for this lesson_

Large Language Models (LLMs) are not just for chatbots and text generation. They can also be used to create search applications using Embeddings. Embeddings are numerical representations of data, also known as vectors, and are useful for semantic data search.

In this lesson, you will build a search application for our education startup. This startup is a non-profit organization that provides free education to students in developing countries. It has a large collection of YouTube videos that students can use to learn about AI. The goal is to create a search application that allows students to find a specific YouTube video by typing a question.

For instance, a student might ask, "What are Jupyter Notebooks?" or "What is Azure ML?" The search application will then return a list of relevant YouTube videos and, even better, provide a link to the exact point in the video where the answer to the question can be found.

## Introduction

In this lesson, we will cover:

- Semantic vs Keyword search.
- What Text Embeddings are.
- How to create a Text Embeddings Index.
- How to search a Text Embeddings Index.

## Learning Goals

By the end of this lesson, you will be able to:

- Differentiate between semantic and keyword search.
- Understand what Text Embeddings are.
- Build an application using Embeddings to search for data.

## Why build a search application?

Building a search application will help you learn how to use Embeddings for data search. Additionally, you will gain the skills to create a search tool that enables students to quickly find the information they need.

This lesson includes an Embedding Index of YouTube transcripts from the Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube channel. The AI Show is a channel dedicated to teaching AI and machine learning concepts. The Embedding Index contains Embeddings for each YouTube transcript up to October 2023. You will use this Embedding Index to develop a search application for our startup. The application will provide links to the exact points in the videos where answers to students' questions are located. This will help students access the information they need more efficiently.

Below is an example of a semantic query for the question "Can you use RStudio with Azure ML?" Notice the YouTube URL includes a timestamp that directs you to the specific part of the video where the answer is found.

![Semantic query for the question "can you use rstudio with Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.en.png)

## What is semantic search?

You might be wondering, what exactly is semantic search? Semantic search is a technique that uses the meaning of words in a query to provide relevant results.

For example, if you're looking to buy a car, you might search for "my dream car." Semantic search understands that you're not literally dreaming about a car but are looking for your ideal car. It interprets your intent and provides relevant results. In contrast, a keyword search would focus on the literal words "dream" and "car," often returning irrelevant results.

## What are Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) are a method of representing text in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). They are semantic numerical representations of text that make data easier for machines to understand. There are various models for creating text embeddings, but in this lesson, we will focus on generating embeddings using the OpenAI Embedding Model.

For example, consider the following text from a transcript of an episode on the AI Show YouTube channel:

```text
Today we are going to learn about Azure Machine Learning.
```

When this text is passed to the OpenAI Embedding API, it returns an embedding consisting of 1536 numbers, also known as a vector. Each number in the vector represents a different aspect of the text. For brevity, here are the first 10 numbers in the vector:

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```


## How is the Embedding index created?

The Embedding Index for this lesson was created using a series of Python scripts. You can find these scripts and instructions in the [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) file located in the 'scripts' folder for this lesson. You don't need to run these scripts to complete the lesson, as the Embedding Index is already provided.

The scripts perform the following tasks:

1. Download the transcript for each YouTube video in the [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) playlist.
2. Use [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) to extract the speaker's name from the first 3 minutes of the transcript. The speaker's name for each video is stored in the Embedding Index named `embedding_index_3m.json`.
3. Divide the transcript text into **3-minute segments**. Each segment includes about 20 overlapping words from the next segment to ensure the Embedding is not cut off and provides better search context.
4. Pass each text segment to the OpenAI Chat API to summarize the text into 60 words. The summary is stored in the Embedding Index `embedding_index_3m.json`.
5. Finally, pass the segment text to the OpenAI Embedding API. The API returns a vector of 1536 numbers representing the semantic meaning of the segment. The segment and its corresponding vector are stored in the Embedding Index `embedding_index_3m.json`.

### Vector Databases

For simplicity, the Embedding Index is stored in a JSON file named `embedding_index_3m.json` and loaded into a Pandas DataFrame. However, in a production environment, the Embedding Index would typically be stored in a vector database such as [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), or [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst).

## Understanding cosine similarity

Now that we've learned about text embeddings, the next step is to understand how to use them to search for data, specifically by finding the most similar embeddings to a given query using cosine similarity.

### What is cosine similarity?

Cosine similarity measures the similarity between two vectors, often referred to as `nearest neighbor search`. To perform a cosine similarity search, you first need to _vectorize_ the _query_ text using the OpenAI Embedding API. Then, calculate the _cosine similarity_ between the query vector and each vector in the Embedding Index. Remember, the Embedding Index contains a vector for each YouTube transcript text segment. Finally, sort the results by cosine similarity, and the text segments with the highest similarity are the most relevant to the query.

Mathematically, cosine similarity measures the cosine of the angle between two vectors in a multidimensional space. This is useful because even if two documents are far apart in terms of Euclidean distance due to size, they might still have a smaller angle between them, resulting in higher cosine similarity. For more details on cosine similarity equations, see [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Building your first search application

Next, we will learn how to create a search application using Embeddings. This application will allow students to search for videos by typing a question. It will return a list of videos relevant to the question and provide links to the exact points in the videos where the answers are located.

This solution has been tested on Windows 11, macOS, and Ubuntu 22.04 using Python 3.10 or later. You can download Python from [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Assignment - building a search application to help students

At the beginning of this lesson, we introduced our startup. Now it's time to help students build a search application for their assessments.

In this assignment, you will create the Azure OpenAI Services required to build the search application. You will set up the following Azure OpenAI Services. An Azure subscription is necessary to complete this assignment.

### Start the Azure Cloud Shell

1. Sign in to the [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Click the Cloud Shell icon in the upper-right corner of the Azure portal.
3. Select **Bash** as the environment type.

#### Create a resource group

> For these instructions, we're using the resource group named "semantic-video-search" in East US.
> You can change the name of the resource group, but when changing the location for the resources,
> check the [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Create an Azure OpenAI Service resource

Run the following command in the Azure Cloud Shell to create an Azure OpenAI Service resource.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Get the endpoint and keys for usage in this application

Run the following commands in the Azure Cloud Shell to retrieve the endpoint and keys for the Azure OpenAI Service resource.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Deploy the OpenAI Embedding model

Run the following command in the Azure Cloud Shell to deploy the OpenAI Embedding model.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Solution

Open the [solution notebook](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) in GitHub Codespaces and follow the instructions in the Jupyter Notebook.

When you run the notebook, you'll be prompted to enter a query. The input box will look like this:

![Input box for the user to input a query](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.en.png)

## Great Work! Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to further enhance your knowledge of Generative AI!

Move on to Lesson 9, where we will explore how to [build image generation applications](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.