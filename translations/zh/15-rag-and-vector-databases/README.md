# 检索增强生成 (RAG) 和向量数据库

[![检索增强生成 (RAG) 和向量数据库](../../../translated_images/15-lesson-banner.png?WT.ae1ec4b596c9c2b74121dd24c30143380d4789a9ef381276dbbc9fd5d7abc3d5.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

在搜索应用课程中，我们简要学习了如何将自己的数据集成到大型语言模型 (LLM) 中。在本课中，我们将深入探讨如何在 LLM 应用中根植数据的概念、过程的机制以及存储数据的方法，包括嵌入和文本。

> **视频即将上线**

## 介绍

在本课中，我们将涵盖以下内容：

- RAG 的介绍，它是什么以及为什么在人工智能中使用它。

- 理解什么是向量数据库，并为我们的应用创建一个。

- 如何将 RAG 集成到应用中的实际示例。

## 学习目标

完成本课后，您将能够：

- 解释 RAG 在数据检索和处理中的重要性。

- 设置 RAG 应用并将您的数据植根于 LLM。

- 在 LLM 应用中有效集成 RAG 和向量数据库。

## 我们的场景：用我们自己的数据增强我们的 LLM

在本课中，我们希望将自己的笔记添加到教育初创公司中，这样聊天机器人就可以获取有关不同主题的更多信息。利用我们拥有的笔记，学习者将能够更好地学习和理解不同的主题，使他们更容易为考试复习。为了创建我们的场景，我们将使用：

- `Azure OpenAI:` 我们将用于创建聊天机器人的 LLM

- `AI for beginners' lesson on Neural Networks`：这将是我们植根于 LLM 的数据

- `Azure AI Search` 和 `Azure Cosmos DB:` 向量数据库来存储我们的数据并创建搜索索引

用户将能够从他们的笔记中创建练习测验、复习闪卡，并将其总结为简洁的概述。让我们开始了解什么是 RAG 以及它如何工作：

## 检索增强生成 (RAG)

一个由 LLM 驱动的聊天机器人处理用户提示以生成响应。它旨在与用户互动，并在广泛的主题上进行交流。然而，其响应仅限于所提供的上下文及其基础训练数据。例如，GPT-4 的知识截止日期是 2021 年 9 月，这意味着它不了解此后发生的事件。此外，用于训练 LLM 的数据不包括个人笔记或公司的产品手册等机密信息。

### RAGs (检索增强生成) 的工作原理

![展示 RAGs 工作原理的图示](../../../translated_images/how-rag-works.png?WT.fde75879826c169b53e16dc0d0d6691172c75b314400f380d40a9f31244eba0e.zh.mc_id=academic-105485-koreyst)

假设您想部署一个从您的笔记中创建测验的聊天机器人，您将需要连接到知识库。这就是 RAG 的用武之地。RAG 的操作如下：

- **知识库：** 在检索之前，这些文档需要被摄取和预处理，通常将大型文档分解为较小的块，将其转换为文本嵌入并存储在数据库中。

- **用户查询：** 用户提出问题

- **检索：** 当用户提出问题时，嵌入模型从我们的知识库中检索相关信息，以提供将被整合到提示中的更多上下文。

- **增强生成：** LLM 基于检索到的数据增强其响应。它允许生成的响应不仅基于预训练数据，还包括来自添加上下文的相关信息。检索到的数据用于增强 LLM 的响应。然后 LLM 返回用户问题的答案。

![展示 RAGs 架构的图示](../../../translated_images/encoder-decode.png?WT.80c3c9669a10e85d1f7e9dc7f7f0d416a71e16d2f8a6da93267e55cbfbddbf9f.zh.mc_id=academic-105485-koreyst)

RAG 的架构使用由两个部分组成的变压器实现：编码器和解码器。例如，当用户提出问题时，输入文本被“编码”为捕捉词义的向量，然后向量被“解码”到我们的文档索引中，并根据用户查询生成新文本。LLM 使用编码器-解码器模型生成输出。

根据提议的论文 [检索增强生成用于知识密集型 NLP（自然语言处理软件）任务](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，实现 RAG 的两种方法是：

- **_RAG-Sequence_** 使用检索到的文档来预测用户查询的最佳答案

- **RAG-Token** 使用文档生成下一个标记，然后检索它们以回答用户的查询

### 为什么要使用 RAGs？

- **信息丰富性：** 确保文本响应是最新的。因此，通过访问内部知识库，提升特定领域任务的性能。

- 通过利用知识库中的**可验证数据**来减少虚构内容，为用户查询提供上下文。

- 它是**成本效益高的**，因为与微调 LLM 相比，它们更经济。

## 创建知识库

我们的应用基于我们的个人数据，即 AI 初学者课程中的神经网络课程。

### 向量数据库

与传统数据库不同，向量数据库是一种专门设计用于存储、管理和搜索嵌入向量的数据库。它存储文档的数值表示。将数据分解为数值嵌入，使我们的 AI 系统更容易理解和处理数据。

我们将嵌入存储在向量数据库中，因为 LLM 对其接受的输入标记数量有一个限制。由于无法将整个嵌入传递给 LLM，我们需要将其分解为块，当用户提出问题时，最接近问题的嵌入将与提示一起返回。分块还可以减少通过 LLM 的标记数量，从而降低成本。

一些流行的向量数据库包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以使用 Azure CLI 使用以下命令创建 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 从文本到嵌入

在存储数据之前，我们需要将其转换为向量嵌入，然后再存储到数据库中。如果您正在处理大型文档或长文本，可以根据预期的查询对其进行分块。分块可以在句子级别或段落级别进行。由于分块从其周围的词中获取含义，您可以为分块添加一些其他上下文，例如，通过添加文档标题或在分块前后包含一些文本。您可以按以下方式分块数据：

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

分块后，我们可以使用不同的嵌入模型嵌入我们的文本。您可以使用的一些模型包括：word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。选择要使用的模型将取决于您使用的语言、编码的内容类型（文本/图像/音频）、它可以编码的输入大小以及嵌入输出的长度。

使用 OpenAI 的 `text-embedding-ada-002` 模型嵌入文本的示例如下：
![“cat”一词的嵌入](../../../translated_images/cat.png?WT.6f67a41409b2174c6f543273f4a9f8c38b227112a12831da3070e52f13e03818.zh.mc_id=academic-105485-koreyst)

## 检索和向量搜索

当用户提出问题时，检索器使用查询编码器将其转换为向量，然后在我们的文档搜索索引中搜索与输入相关的向量。一旦完成，它将输入向量和文档向量都转换为文本，并通过 LLM 传递。

### 检索

检索发生在系统尝试快速从索引中找到满足搜索条件的文档时。检索器的目标是获取将用于提供上下文并在您的数据上植根于 LLM 的文档。

在我们的数据库中执行搜索的方法有多种，例如：

- **关键词搜索** - 用于文本搜索

- **语义搜索** - 使用词义

- **向量搜索** - 使用嵌入模型将文档从文本转换为向量表示。检索将通过查询与用户问题最接近的文档来完成。

- **混合搜索** - 关键词和向量搜索的结合。

检索的一个挑战是当数据库中没有与查询类似的响应时，系统将返回他们能找到的最佳信息，不过，您可以使用一些策略，例如设置相关性的最大距离或使用结合关键词和向量搜索的混合搜索。在本课中，我们将使用混合搜索，即向量和关键词搜索的结合。我们将数据存储到包含块和嵌入的列的数据框中。

### 向量相似性

检索器将在知识数据库中搜索彼此靠近的嵌入，即最近邻，因为它们是相似的文本。在用户提出查询的情况下，首先将其嵌入，然后与相似的嵌入匹配。用于测量不同向量相似性的常见度量是余弦相似性，它基于两个向量之间的角度。

我们可以使用其他替代方法来测量相似性，例如欧几里得距离，它是向量端点之间的直线距离，以及点积，它测量两个向量的对应元素的乘积之和。

### 搜索索引

在进行检索时，我们需要在执行搜索之前为我们的知识库构建一个搜索索引。索引将存储我们的嵌入，并可以在大型数据库中快速检索最相似的块。我们可以使用以下方法在本地创建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 重排序

查询数据库后，您可能需要对结果进行排序，以使其从最相关的结果开始。重排序 LLM 利用机器学习通过将搜索结果按相关性排序来提高其相关性。使用 Azure AI 搜索，重排序会自动为您完成，使用语义重排序器。使用最近邻的重排序示例如下：

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

## 将所有内容整合在一起

最后一步是将我们的 LLM 添加到组合中，以便能够获得基于我们数据的响应。我们可以按以下方式实现：

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

## 评估我们的应用

### 评估指标

- 提供的响应质量，确保其听起来自然、流畅和人性化

- 数据的植根性：评估响应是否来自提供的文档

- 相关性：评估响应是否与所提问题匹配并相关

- 流利度：评估响应在语法上是否合理

## 使用 RAG（检索增强生成）和向量数据库的用例

在许多不同的用例中，函数调用可以改善您的应用，例如：

- 问答：将公司数据植根于员工可以用来提问的聊天中。

- 推荐系统：您可以创建一个系统，匹配最相似的值，例如电影、餐馆等。

- 聊天机器人服务：您可以存储聊天记录，并根据用户数据个性化对话。

- 基于向量嵌入的图像搜索，在进行图像识别和异常检测时非常有用。

## 总结

我们已经涵盖了 RAG 的基础领域，从将数据添加到应用、用户查询和输出。为了简化 RAG 的创建，您可以使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作业

为了继续学习检索增强生成 (RAG)，您可以构建：

- 使用您选择的框架为应用构建前端

- 利用 LangChain 或 Semantic Kernel 框架，重建您的应用。

恭喜您完成本课 👏。

## 学习不止于此，继续旅程

完成本课后，请查看我们的 [生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

**免责声明**：  
本文档使用机器翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担责任。