<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:04:11+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "zh"
}
-->
# 检索增强生成 (RAG) 和向量数据库

[![检索增强生成 (RAG) 和向量数据库](../../../../../translated_images/zh-CN/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜索应用课程中，我们简要学习了如何将自己的数据整合到大型语言模型（LLM）中。在本课程中，我们将深入探讨在LLM应用中绑定数据的概念、该过程的机制以及存储数据的方法，包括向量嵌入和文本。

> **视频即将发布**

## 介绍

本课程将涵盖以下内容：

- 对RAG的介绍，RAG是什么以及为何在AI（人工智能）中使用它。

- 理解什么是向量数据库以及为我们的应用创建一个。

- 如何将RAG集成到应用中的实用示例。

## 学习目标

完成本课程后，您将能够：

- 解释RAG在数据检索和处理中的重要性。

- 设置RAG应用并将您的数据绑定到LLM。

- 在LLM应用中有效集成RAG和向量数据库。

## 我们的场景：用自己的数据增强我们的LLM

本课程中，我们希望将自己的笔记添加到教育初创项目中，使聊天机器人能够获取更多不同学科的信息。利用我们的笔记，学习者能够更好地学习和理解不同的话题，从而更轻松地为考试复习。为了创建我们的场景，我们将使用：

- `Azure OpenAI:` 我们用来创建聊天机器人的大型语言模型

- `AI for beginners' lesson on Neural Networks`：这将是我们用来绑定LLM的数据

- `Azure AI Search` 和 `Azure Cosmos DB:` 用于存储数据和创建搜索索引的向量数据库

用户将能够从笔记中创建练习测验、复习闪卡，并将其总结为简明概述。开始之前，让我们了解什么是RAG及其工作原理：

## 检索增强生成 (RAG)

一个由LLM驱动的聊天机器人处理用户提示以生成响应。它被设计为交互式，能够与用户就各种主题进行交流。然而，它的回答受到所提供上下文和基础训练数据的限制。例如，GPT-4的知识截止时间为2021年9月，这意味着它不了解此日期之后发生的事件。此外，训练LLM使用的数据不包括诸如个人笔记或公司产品手册等机密信息。

### RAG（检索增强生成）如何工作

![说明RAG工作方式的图](../../../../../translated_images/zh-CN/how-rag-works.f5d0ff63942bd3a6.webp)

假设您想部署一个能从您的笔记中创建测验的聊天机器人，您将需要连接到知识库。这时RAG就派上用场了。RAG的运作流程如下：

- **知识库：** 在检索之前，这些文档需要被导入和预处理，通常是将大型文档拆解成更小的块，将它们转换为文本嵌入并存储在数据库中。

- **用户查询：** 用户提出问题。

- **检索：** 当用户提问时，嵌入模型从我们的知识库中检索相关信息，提供更多上下文，该上下文将被纳入提示中。

- **增强生成：** LLM根据检索到的数据增强其回答。这使得生成的答复不仅基于预训练数据，还包括来自附加上下文的相关信息。检索到的数据用于扩展LLM的响应。随后LLM返回用户问题的答案。

![显示RAG架构的图](../../../../../translated_images/zh-CN/encoder-decode.f2658c25d0eadee2.webp)

RAG的架构采用transformers实现，由编码器和解码器两部分组成。例如，当用户提出问题时，输入文本被“编码”为捕捉单词含义的向量，这些向量被“解码”到我们的文档索引，并基于用户查询生成新文本。LLM使用编码器-解码器模型来生成输出。

根据论文[Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，实现RAG有两种方法：

- **_RAG-Sequence_** 使用检索到的文档预测用户查询的最佳答案

- **RAG-Token** 使用文档生成下一个token，再检索它们以回答用户查询

### 为什么要使用RAG？

- **信息丰富性：** 确保文本响应是最新和当前的。因此通过访问内部知识库提高特定领域任务的性能。

- 降低虚构生成，通过使用知识库中的**可验证数据**为用户查询提供上下文。

- 成本效益高，相较于微调LLM，它们更加经济实惠。

## 创建知识库

我们的应用基于我们的个人数据，即“AI初学者课程”中的神经网络课程。

### 向量数据库

向量数据库与传统数据库不同，是一种专门设计用来存储、管理和搜索嵌入向量的数据库。它存储文档的数值表示。将数据拆解为数值嵌入，使我们的AI系统更容易理解和处理数据。

我们将嵌入存储在向量数据库中，因为LLM对输入符号数有限制。由于无法将整个嵌入传递给LLM，我们需要将其拆分成多个块，当用户提问时，最相关的嵌入将与提示一起返回。分块还减少了通过LLM传递的令牌数量，从而降低成本。

一些流行的向量数据库包括Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant和DeepLake。您可以使用Azure CLI通过以下命令创建Azure Cosmos DB模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```


### 从文本到嵌入

在存储数据之前，我们需要将其转换为向量嵌入。若处理大型文档或长文本，可以按预期查询进行分块。分块可以在句子层面，也可以在段落层面进行。由于分块从周围单词中提取含义，可以为分块添加其他上下文，例如文档标题或包含分块之前或之后的一些文本。数据分块示例：

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

    # 如果最后一个块未达到最小长度，仍然添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```


分块完成后，我们可以使用不同的嵌入模型对文本进行嵌入。一些可用模型包括word2vec、OpenAI的ada-002、Azure计算机视觉等。选择模型取决于您使用的语言、编码内容的类型（文本/图像/音频）、输入大小限制和嵌入输出长度。

以下是使用OpenAI的`text-embedding-ada-002`模型嵌入的“cat”一词示例：
![单词 cat 的嵌入图](../../../../../translated_images/zh-CN/cat.74cbd7946bc9ca38.webp)

## 检索和向量搜索

当用户提问时，检索器使用查询编码器将提问转为向量，然后在文档搜索索引中搜索与输入相关的向量。一旦完成，它将输入向量和文档向量转换为文本并传递给LLM。

### 检索

检索是系统试图快速从索引中找到满足搜索条件文档的过程。检索器的目标是获取用于提供上下文并将LLM基于您的数据进行绑定的文档。

数据库检索的几种方式包括：

- **关键词搜索** — 用于文本搜索

- **向量搜索** — 使用嵌入模型将文档从文本转换为向量表示，允许基于单词含义的**语义搜索**。通过查询与用户问题向量最接近的文档向量来检索。

- **混合搜索** — 关键词搜索和向量搜索的组合。

检索的挑战在于，当数据库中不存在与查询相似的响应时，系统将返回最佳可用信息。不过，您可以使用设定最大相关距离或使用结合关键词和向量搜索的混合搜索等策略。本课程中我们将使用混合搜索，将数据存储到包含分块和嵌入的DataFrame中。

### 向量相似度

检索器会在知识库中搜索彼此接近的嵌入，即最近邻，因为这些文本相似。用户提问时，查询首先被嵌入，然后与相似嵌入匹配。常用的相似度度量是余弦相似度，它基于两个向量之间的角度。

我们也可以用其他方式衡量相似度，比如欧氏距离（向量端点间的直线距离）和点积（对应元素乘积之和）。

### 搜索索引

执行检索前，我们需要为知识库构建搜索索引。索引存储我们的嵌入，即使在大型数据库中也能快速检索最相似的分块。我们可以本地创建索引，示例如下：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 创建搜索索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 要查询索引，可以使用kneighbors方法
distances, indices = nbrs.kneighbors(embeddings)
```


### 重新排序

查询数据库后，您可能需要将结果按相关性排序。重新排序LLM利用机器学习技术，通过将结果按相关性从高到低排序来提升搜索结果的准确度。使用Azure AI Search，语义重新排序器会自动为您完成此工作。以下是基于最近邻的重新排序示例：

```python
# 查找最相似的文档
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 打印最相似的文档
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```


## 综合应用

最后一步是将我们的LLM整合进来，以便生成基于我们数据的响应。实现示例：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 将问题转换为查询向量
    query_vector = create_embeddings(user_input)

    # 查找最相似的文档
    distances, indices = nbrs.kneighbors([query_vector])

    # 将文档添加到查询中以提供上下文
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 合并历史记录和用户输入
    history.append(user_input)

    # 创建消息对象
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用聊天补全生成回复
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

- 回答质量：确保回答自然、流畅且类似人类语言。

- 数据绑定度：评估回答是否来源于提供的文档。

- 相关性：评估回答是否与提问匹配且相关。

- 流畅性：回答在语法上的合理性。

## 使用RAG（检索增强生成）和向量数据库的用例

函数调用能提升应用的多个场景，如：

- 问答系统：将公司数据绑定到聊天机器人，员工可用其提问。

- 推荐系统：创建匹配最相似值（如电影、餐厅等）的系统。

- 聊天机器人服务：存储聊天历史，并基于用户数据个性化对话。

- 基于向量嵌入的图像搜索，适合做图像识别和异常检测。

## 总结

我们涵盖了RAG的基本内容，从添加数据到应用、用户查询及输出。为了简化RAG的创建，您可以使用框架如Semantic Kernel、Langchain或Autogen。

## 作业

继续学习检索增强生成（RAG），您可以：

- 使用您选择的框架为应用构建前端。

- 使用LangChain或Semantic Kernel框架，重新创建您的应用。

恭喜您完成本课程 👏。

## 学习不会止步于此，继续前行

完成本课程后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持续提升您的生成式AI知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始语言版本的文档应视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->