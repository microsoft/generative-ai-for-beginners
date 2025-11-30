<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T23:22:46+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "zh"
}
-->
# 检索增强生成 (RAG) 和向量数据库

[![检索增强生成 (RAG) 和向量数据库](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.zh.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜索应用课程中，我们简要学习了如何将自己的数据集成到大型语言模型 (LLMs) 中。在本课程中，我们将进一步探讨如何在 LLM 应用中将数据进行基础化处理的概念、过程机制以及存储数据的方法，包括嵌入和文本。

> **视频即将上线**

## 介绍

在本课程中，我们将涵盖以下内容：

- RAG 的介绍，它是什么以及为什么在人工智能 (AI) 中使用它。

- 理解什么是向量数据库，并为我们的应用创建一个。

- 一个关于如何将 RAG 集成到应用中的实际示例。

## 学习目标

完成本课程后，您将能够：

- 解释 RAG 在数据检索和处理中的重要性。

- 设置 RAG 应用并将您的数据基础化到 LLM。

- 在 LLM 应用中有效集成 RAG 和向量数据库。

## 我们的场景：用自己的数据增强 LLM

在本课程中，我们希望将自己的笔记添加到教育初创公司中，使聊天机器人能够获取更多关于不同主题的信息。通过使用我们的笔记，学习者将能够更好地学习和理解不同的主题，从而更轻松地为考试复习。为了创建我们的场景，我们将使用：

- `Azure OpenAI:` 我们将用来创建聊天机器人的 LLM

- `AI 初学者课程中的神经网络章节`: 我们将用来基础化 LLM 的数据

- `Azure AI Search` 和 `Azure Cosmos DB:` 用于存储数据并创建搜索索引的向量数据库

用户将能够从笔记中创建练习测验、复习闪卡，并将其总结为简洁的概述。让我们开始了解什么是 RAG 以及它如何工作：

## 检索增强生成 (RAG)

一个由 LLM 驱动的聊天机器人处理用户提示以生成响应。它旨在与用户进行互动，并涵盖广泛的主题。然而，它的响应仅限于提供的上下文及其基础训练数据。例如，GPT-4 的知识截止日期是 2021 年 9 月，这意味着它无法了解此后发生的事件。此外，用于训练 LLM 的数据不包括机密信息，例如个人笔记或公司的产品手册。

### RAG（检索增强生成）如何工作

![展示 RAG 工作原理的图示](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.zh.png)

假设您想部署一个从笔记中创建测验的聊天机器人，您需要一个连接到知识库的方式。这时 RAG 就派上用场了。RAG 的工作方式如下：

- **知识库:** 在检索之前，这些文档需要被摄取和预处理，通常将大型文档分解为较小的块，将其转换为文本嵌入并存储在数据库中。

- **用户查询:** 用户提出问题。

- **检索:** 当用户提出问题时，嵌入模型从我们的知识库中检索相关信息，以提供更多上下文并将其纳入提示中。

- **增强生成:** LLM 基于检索到的数据增强其响应。这使得生成的响应不仅基于预训练数据，还基于添加的上下文中的相关信息。检索到的数据用于增强 LLM 的响应。然后 LLM 返回用户问题的答案。

![展示 RAG 架构的图示](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.zh.png)

RAG 的架构通过使用包含两个部分的 Transformer 实现：编码器和解码器。例如，当用户提出问题时，输入文本被“编码”为捕捉单词含义的向量，这些向量被“解码”到我们的文档索引中，并根据用户查询生成新文本。LLM 使用编码器-解码器模型生成输出。

根据论文 [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) 提出的两种实现 RAG 的方法是：

- **_RAG-Sequence_** 使用检索到的文档预测用户查询的最佳答案。

- **RAG-Token** 使用文档生成下一个 token，然后检索它们以回答用户的查询。

### 为什么使用 RAG？

- **信息丰富性:** 确保文本响应是最新的和当前的。因此，通过访问内部知识库提高了特定领域任务的性能。

- 通过利用知识库中的 **可验证数据** 来减少虚假信息，为用户查询提供上下文。

- **成本效益高:** 与微调 LLM 相比，它更经济。

## 创建知识库

我们的应用基于个人数据，即 AI 初学者课程中的神经网络章节。

### 向量数据库

与传统数据库不同，向量数据库是一种专门设计用于存储、管理和搜索嵌入向量的数据库。它存储文档的数值表示。将数据分解为数值嵌入使我们的 AI 系统更容易理解和处理数据。

我们将嵌入存储在向量数据库中，因为 LLM 对接受为输入的 token 数量有限制。由于无法将整个嵌入传递给 LLM，我们需要将其分解为块，当用户提出问题时，与问题最相似的嵌入将与提示一起返回。分块还可以减少通过 LLM 传递的 token 数量，从而降低成本。

一些流行的向量数据库包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以使用以下命令通过 Azure CLI 创建 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 从文本到嵌入

在存储数据之前，我们需要将其转换为向量嵌入，然后存储到数据库中。如果您正在处理大型文档或长文本，可以根据预期的查询对其进行分块。分块可以在句子级别或段落级别进行。由于分块从周围的单词中提取含义，您可以为分块添加一些其他上下文，例如添加文档标题或在分块前后包含一些文本。可以按以下方式分块数据：

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

分块后，我们可以使用不同的嵌入模型嵌入我们的文本。您可以使用的一些模型包括：word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。选择使用的模型将取决于您使用的语言、编码的内容类型（文本/图像/音频）、它可以编码的输入大小以及嵌入输出的长度。

使用 OpenAI 的 `text-embedding-ada-002` 模型嵌入文本的示例如下：
![“cat”一词的嵌入示例](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.zh.png)

## 检索和向量搜索

当用户提出问题时，检索器使用查询编码器将其转换为向量，然后在我们的文档搜索索引中搜索与输入相关的文档的相关向量。完成后，它将输入向量和文档向量都转换为文本，并通过 LLM 传递。

### 检索

检索发生在系统尝试快速从索引中找到满足搜索条件的文档时。检索器的目标是获取将用于提供上下文并将 LLM 基础化到您的数据上的文档。

在我们的数据库中有几种执行搜索的方法，例如：

- **关键词搜索** - 用于文本搜索。

- **语义搜索** - 使用单词的语义含义。

- **向量搜索** - 使用嵌入模型将文档从文本转换为向量表示。检索通过查询与用户问题最接近的文档向量来完成。

- **混合搜索** - 结合关键词搜索和向量搜索。

检索的一个挑战是，当数据库中没有与查询类似的响应时，系统将返回它能找到的最佳信息。然而，您可以使用一些策略，例如设置相关性的最大距离或使用结合关键词和向量搜索的混合搜索。在本课程中，我们将使用混合搜索，即关键词搜索和向量搜索的结合。我们将数据存储到一个数据框中，其中包含分块和嵌入的列。

### 向量相似度

检索器将在知识数据库中搜索彼此接近的嵌入，即最近邻，因为它们是相似的文本。在用户提出查询的情况下，查询首先被嵌入，然后与相似的嵌入进行匹配。用于衡量不同向量相似度的常见方法是余弦相似度，它基于两个向量之间的角度。

我们可以使用其他替代方法来测量相似度，例如欧几里得距离（向量端点之间的直线距离）和点积（测量两个向量对应元素的乘积之和）。

### 搜索索引

在进行检索时，我们需要为知识库构建一个搜索索引，然后才能执行搜索。索引将存储我们的嵌入，即使在大型数据库中也能快速检索最相似的分块。我们可以使用以下方法在本地创建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 重排序

查询数据库后，您可能需要对结果进行排序以显示最相关的内容。重排序 LLM 利用机器学习通过从最相关的结果开始排序来提高搜索结果的相关性。使用 Azure AI Search，重排序会自动为您完成，使用语义重排序器。以下是使用最近邻重排序的示例：

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

## 整合所有内容

最后一步是将我们的 LLM 添加到流程中，以便能够生成基于我们数据的响应。我们可以按以下方式实现：

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

- 提供的响应质量，确保其听起来自然、流畅且像人类。

- 数据的基础性：评估响应是否来自提供的文档。

- 相关性：评估响应是否与所提问题匹配并相关。

- 流畅性：评估响应在语法上是否合理。

## 使用 RAG（检索增强生成）和向量数据库的应用场景

使用函数调用可以改进您的应用的许多不同场景，例如：

- 问答系统：将公司数据基础化到聊天中，供员工提问。

- 推荐系统：创建一个匹配最相似值的系统，例如电影、餐厅等。

- 聊天机器人服务：可以存储聊天记录并根据用户数据个性化对话。

- 基于向量嵌入的图像搜索，在图像识别和异常检测中非常有用。

## 总结

我们已经涵盖了 RAG 的基本领域，包括将数据添加到应用、用户查询和输出。为了简化 RAG 的创建，您可以使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作业

为了继续学习检索增强生成 (RAG)，您可以：

- 使用您选择的框架为应用构建前端。

- 使用框架（LangChain 或 Semantic Kernel）重新创建您的应用。

恭喜您完成了本课程 👏。

## 学习不会止步于此，继续您的学习之旅

完成本课程后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。