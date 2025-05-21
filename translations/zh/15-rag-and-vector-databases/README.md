<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:04:21+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "zh"
}
-->
# 检索增强生成 (RAG) 和向量数据库

在搜索应用课程中，我们简要学习了如何将自己的数据集成到大型语言模型 (LLMs) 中。在本课中，我们将深入探讨如何在LLM应用中锚定数据、这一过程的机制以及存储数据的方法，包括嵌入和文本。

> **视频即将推出**

## 简介

在本课中，我们将涵盖以下内容：

- 介绍RAG，它是什么以及为什么在人工智能 (AI) 中使用。

- 理解什么是向量数据库，并为我们的应用创建一个。

- 一个关于如何将RAG集成到应用中的实际例子。

## 学习目标

完成本课后，您将能够：

- 解释RAG在数据检索和处理中的重要性。

- 设置RAG应用，并将您的数据锚定到LLM中。

- 在LLM应用中有效集成RAG和向量数据库。

## 我们的场景：用我们自己的数据增强我们的LLM

在本课中，我们希望将自己的笔记添加到教育初创企业中，这使得聊天机器人能够获取更多关于不同主题的信息。通过我们拥有的笔记，学习者将能够更好地学习和理解不同的主题，从而更容易为他们的考试复习。为了创建我们的场景，我们将使用：

- `Azure OpenAI:` 我们将用来创建聊天机器人的LLM

- `AI for beginners' lesson on Neural Networks`：这将是我们锚定LLM的数据

- `Azure AI Search` 和 `Azure Cosmos DB:` 向量数据库用于存储我们的数据并创建搜索索引

用户将能够从他们的笔记中创建练习测验、复习闪卡并将其总结为简洁的概述。要开始，让我们看看什么是RAG以及它如何工作：

## 检索增强生成 (RAG)

一个由LLM驱动的聊天机器人处理用户提示以生成响应。它旨在是互动的，并在广泛的主题上与用户互动。然而，其响应仅限于所提供的上下文及其基础训练数据。例如，GPT-4的知识截止日期是2021年9月，这意味着它缺乏在此之后发生事件的知识。此外，用于训练LLM的数据不包括机密信息，如个人笔记或公司的产品手册。

### RAGs (检索增强生成) 如何工作

假设您想部署一个从笔记中创建测验的聊天机器人，您将需要与知识库的连接。这就是RAG发挥作用的地方。RAGs的操作如下：

- **知识库：** 在检索之前，这些文档需要被摄取和预处理，通常将大文档分解为较小的块，将它们转换为文本嵌入并存储在数据库中。

- **用户查询：** 用户提出问题

- **检索：** 当用户提出问题时，嵌入模型从我们的知识库中检索相关信息，以提供更多上下文，这些上下文将被纳入提示中。

- **增强生成：** LLM基于检索到的数据增强其响应。它允许生成的响应不仅基于预训练数据，还基于所添加上下文中的相关信息。检索到的数据用于增强LLM的响应。然后，LLM向用户的问题返回答案。

RAGs的架构是通过由两个部分组成的transformers实现的：编码器和解码器。例如，当用户提出问题时，输入文本被“编码”成向量，捕捉单词的意义，然后向量被“解码”到我们的文档索引中，并根据用户查询生成新文本。LLM使用编码器-解码器模型生成输出。

根据所提出的论文：[用于知识密集型NLP（自然语言处理软件）任务的检索增强生成](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) ，实现RAG的两种方法是：

- **_RAG-Sequence_** 使用检索到的文档来预测用户查询的最佳答案

- **RAG-Token** 使用文档生成下一个标记，然后检索它们以回答用户的查询

### 为什么使用RAG？

- **信息丰富性：** 确保文本响应是最新的。因此，通过访问内部知识库，它提高了在特定领域任务上的表现。

- 通过利用知识库中的**可验证数据**来减少虚构，为用户查询提供上下文。

- 它是**成本效益高的**，因为它们比微调LLM更经济。

## 创建知识库

我们的应用基于我们的个人数据，即AI初学者课程中的神经网络课程。

### 向量数据库

向量数据库，与传统数据库不同，是一种专门设计用于存储、管理和搜索嵌入向量的数据库。它存储文档的数值表示。将数据分解为数值嵌入使我们的AI系统更容易理解和处理数据。

我们将嵌入存储在向量数据库中，因为LLM对接受的输入令牌数量有限制。由于不能将整个嵌入传递给LLM，我们需要将它们分解成块，当用户提出问题时，与问题最相似的嵌入将与提示一起返回。分块也降低了通过LLM传递的令牌数量的成本。

一些流行的向量数据库包括Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant和DeepLake。您可以使用Azure CLI通过以下命令创建Azure Cosmos DB模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 从文本到嵌入

在我们存储数据之前，我们需要将其转换为向量嵌入，然后存储在数据库中。如果您正在处理大文档或长文本，可以根据预期的查询对它们进行分块。分块可以在句子级别或段落级别进行。由于分块从周围的单词中获取意义，您可以向分块添加其他上下文，例如，通过添加文档标题或在分块之前或之后包含一些文本。您可以按以下方式分块数据：

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

分块后，我们可以使用不同的嵌入模型嵌入我们的文本。您可以使用的一些模型包括：word2vec，OpenAI的ada-002，Azure Computer Vision等等。选择要使用的模型将取决于您使用的语言、编码内容的类型（文本/图像/音频）、它可以编码的输入大小以及嵌入输出的长度。

使用OpenAI的`text-embedding-ada-002`模型嵌入文本的一个例子是：

## 检索和向量搜索

当用户提出问题时，检索器使用查询编码器将其转换为向量，然后在我们的文档搜索索引中搜索与输入相关的相关向量。完成后，它将输入向量和文档向量都转换为文本并通过LLM传递。

### 检索

检索发生在系统尝试快速从索引中找到满足搜索标准的文档时。检索器的目标是获取将用于提供上下文并将LLM锚定在您的数据上的文档。

在我们的数据库中执行搜索有几种方法，例如：

- **关键词搜索** - 用于文本搜索

- **语义搜索** - 使用单词的语义意义

- **向量搜索** - 使用嵌入模型将文档从文本转换为向量表示。检索将通过查询与用户问题最接近的文档来完成。

- **混合** - 结合关键词和向量搜索。

检索的一个挑战是当数据库中没有与查询相似的响应时，系统将返回他们能获得的最佳信息，然而，您可以使用策略，例如设置相关性的最大距离或使用结合关键词和向量搜索的混合搜索。在本课中，我们将使用混合搜索，结合向量和关键词搜索。我们将数据存储到一个包含块和嵌入的列的数据框中。

### 向量相似性

检索器将在知识数据库中搜索彼此接近的嵌入，最接近的邻居，因为它们是相似的文本。在用户提出查询的情况下，它首先被嵌入，然后与相似的嵌入匹配。用于查找不同向量之间相似性的常用测量是余弦相似性，它基于两个向量之间的角度。

我们可以使用其他替代方法测量相似性，例如欧几里得距离，它是向量端点之间的直线，以及点积，它测量两个向量对应元素的乘积之和。

### 搜索索引

在进行检索时，我们需要为我们的知识库构建一个搜索索引，然后才能执行搜索。索引将存储我们的嵌入，并且即使在大型数据库中也能快速检索到最相似的块。我们可以使用以下方法在本地创建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 重新排序

一旦您查询了数据库，您可能需要从最相关的结果中进行排序。重新排序LLM利用机器学习通过从最相关的排序来提高搜索结果的相关性。使用Azure AI搜索，重新排序会自动为您完成，使用语义重新排序器。使用最近邻居的重新排序工作示例如下：

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

## 将一切结合在一起

最后一步是将我们的LLM加入其中，以便能够获得基于我们数据的响应。我们可以按如下方式实现：

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

- 提供的响应质量，确保其听起来自然、流利且人性化

- 数据的锚定性：评估响应是否来自提供的文档

- 相关性：评估响应是否与所问问题匹配并相关

- 流利度 - 响应在语法上是否合理

## 使用RAG（检索增强生成）和向量数据库的用例

有许多不同的用例可以通过函数调用来改善您的应用程序，例如：

- 问答：将您的公司数据锚定到员工可以用来提问的聊天中。

- 推荐系统：您可以创建一个系统来匹配最相似的值，例如电影、餐馆等等。

- 聊天机器人服务：您可以存储聊天历史记录并根据用户数据个性化对话。

- 基于向量嵌入的图像搜索，在进行图像识别和异常检测时非常有用。

## 总结

我们已经涵盖了RAG的基本领域，从将我们的数据添加到应用程序、用户查询和输出。为了简化RAG的创建，您可以使用诸如Semanti Kernel、Langchain或Autogen等框架。

## 作业

为了继续学习检索增强生成 (RAG)，您可以构建：

- 使用您选择的框架构建应用程序的前端

- 使用框架，无论是LangChain还是Semantic Kernel，并重新创建您的应用程序。

恭喜您完成了本课 👏。

## 学习不会止步于此，继续前进

完成本课后，请查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

**免责声明**：
本文档已使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。应将原始文档的本国语言版本视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。