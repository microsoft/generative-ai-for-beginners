# 检索增强生成 (RAG) 与向量数据库

在之前的搜索应用课程中，我们简单探讨了如何将个人数据融入到大型语言模型（LLM）中。本节课将更深入地讲述如何在LLM应用中实现数据基础化，包括数据处理的机制和方法，以及如何存储包括嵌入和文本在内的数据。

> **视频教程即将上线**

## 引言

本课程内容包括：

- RAG简介，探讨其在人工智能中的应用及其重要性。
- 了解向量数据库并创建一个用于应用的实例。
- 通过实践示例展示如何在应用程序中集成RAG。

## 学习目标

课程完成后，您将能够：

- 阐述RAG在数据检索和处理中的重要作用。
- 配置RAG应用，并将数据与LLM结合。
- 在LLM应用中有效地整合RAG和向量数据库。

## 场景设定：用个人数据增强LLM

本课程旨在通过加入个人笔记来增强教育初创公司的LLM，让聊天机器人能够获取更多关于不同学科的信息。利用这些笔记，学习者可以更好地学习理解不同的主题，从而更轻松地为考试做准备。我们的场景包括：

- `Azure Open AI:` 我们选用的LLM，用于创建聊天机器人。
- `AI初学者的神经网络课程`：这是我们将基础化到LLM的数据。
- `Azure AI Search` 和 `Azure Cosmos DB:` 用于存储数据并创建搜索索引的向量数据库。

用户可以利用这些笔记创建练习测验、复习卡片，并将其概括为简洁的总结。在开始之前，让我们先了解RAG及其工作原理：

## 检索增强生成 (RAG)

LLM驱动的聊天机器人通过处理用户的提示来生成回答。它旨在与用户就广泛的话题进行互动。然而，它的回答仅限于所提供的上下文和其基础训练数据。例如，GPT-4的知识截止日期是2021年9月，这意味着它缺少在此之后发生事件的知识。此外，用于训练LLM的数据不包括个人笔记或公司产品手册等机密信息。

### RAG如何工作

如果您想部署一个能从笔记创建测验的聊天机器人，您需要连接到知识库。这正是RAG发挥作用的地方。RAG的工作流程如下：

- **知识库：** 在检索之前，需要将这些文档摄入并预处理，通常是将大型文档拆分为更小的块，将它们转换成文本嵌入，并存储在数据库中。
- **用户查询：** 用户提问。
- **检索：** 当用户提出问题时，嵌入模型从知识库中检索相关信息，为提示提供更多上下文。
- **增强生成：** LLM根据检索到的数据增强其回答，使得生成的回答不仅基于预先训练的数据，还包括从添加的上下文中获得的相关信息。检索到的数据用于增强LLM的回答，LLM随后向用户提供问题的答案。

### 为什么使用RAG？

- **信息丰富：** 确保文本回答是最新和相关的，因此通过访问内部知识库，提高了特定领域任务的性能。
- 通过利用知识库中的**可验证数据**来减少错误信息，为用户查询提供上下文。
- **成本效益：** 与微调LLM相比，它们更加经济。

## 创建知识库

我们的应用是基于我们个人的数据，即AI初学者课程中的神经网络课程。

### 向量数据库

向量数据库与传统数据库不同，它是专门设计来存储、管理和搜索嵌入向量的。它存储文档的数值表示形式。将数据分解为数值嵌入，使AI系统更容易理解和处理数据。

我们将嵌入存储在向量数据库中，因为LLM对作为输入接受的标记数量有限制。由于不能将整个嵌入传递给LLM，我们需要将它们分解成块，当用户提问时，最相似的嵌入将与提示一起返回。分块还有助于减少通过LLM传递的标记数量的成本。

一些流行的向量数据库包括Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Quadrants和DeepLake。您可以使用以下命令通过Azure CLI创建Azure Cosmos DB模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 从文本到嵌入

在存储数据之前，我们需要将其转换为向量嵌入。如果您处理的是大型文档或长文本，可以根据预期的查询进行分块。分块可以在句子级别或段落级别进行。由于分块从周围的词汇中提取含义，您可以向块中添加额外的上下文，例如，通过添加文档标题或包含块前后的文本。您可以按以下方式进行分块：

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) > max_length and len(' '.join(current_chunk)) < min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # 如果最后一个块没有达到最小长度，无论如何都要添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```
一旦完成分块，我们就可以使用不同的嵌入模型来嵌入我们的文本。您可以使用的一些模型包括word2vec、OpenAI的ada-002、Azure Computer Vision等。选择使用哪个模型将取决于您使用的语言、编码的内容类型（文本/图像/音频）、它可以编码的输入大小以及嵌入输出的长度。

使用OpenAI的`text-embedding-ada-002`模型嵌入文本的示例是：![嵌入单词cat的示例](images/cat.png?WT.mc_id=academic-105485-koreyst)

## 检索和向量搜索

当用户提问时，检索器使用查询编码器将其转换为向量，然后在我们的文档搜索索引中搜索与输入相关的文档中的相关向量。完成后，它将输入向量和文档向量转换为文本，并将其传递给LLM。

### 检索

检索是系统尝试快速找到索引中满足搜索条件的文档的过程。检索器的目标是获取将用于提供上下文并将LLM基础化在您的数据上的文档。

在我们的数据库中执行搜索的几种方式包括：

- **关键字搜索** - 用于文本搜索。
- 
- **语义搜索** - 使用单词的语义含义进行搜索。
- 
- **向量搜索** - 使用嵌入模型将文档从文本转换为向量表示。检索通过查询与用户问题最接近的文档向量表示来完成。
- 
- **混合搜索** - 关键字和向量搜索的结合。

检索的一个挑战是，当数据库中没有与查询类似的响应时，系统将返回它们能找到的最佳信息。然而，您可以使用策略，如设置相关性的最大距离或使用结合了关键字和向量搜索的混合搜索。在本课中，我们将使用混合搜索，即关键字和向量搜索的结合。我们将数据存储到一个包含块和嵌入的数据帧中。

### 向量相似度

检索器通过知识数据库搜索嵌入彼此接近的向量，即最近的邻居，因为它们是相似的文本。在用户提出查询的情况下，首先对其进行嵌入，然后与相似的嵌入匹配。用于找出不同向量有多相似的常用测量是余弦相似度，它基于两个向量之间的角度。

我们可以使用其他方法来测量相似度，包括欧几里得距离，这是向量端点之间的直线距离，以及点积，它测量两个向量对应元素的乘积之和。

### 搜索索引

在进行检索时，我们需要先为知识库构建一个搜索索引。索引存储我们的嵌入，并能在大型数据库中快速检索最相似的块。我们可以使用以下代码在本地创建我们的索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].tolist()

# 创建搜索索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 查询索引，可以使用kneighbors方法
distances, indices = nbrs.kneighbors(embeddings)
```
### 重新排序

查询数据库后，可能需要按照相关性从高到低对结果进行排序。重新排序的LLM使用机器学习来提高搜索结果的相关性，通过从最相关的排序。使用Azure AI Search，重新排序会自动使用语义重新排序器为您完成。使用最近邻居重新排序的示例：

```python
# 查找最相似的文档
distances, indices = nbrs.kneighbors([query_vector])

# 打印最相似的文档
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"DataFrame中未找到索引 {index}")
```
## 整合所有元素

最后一步是将我们的LLM融入进来，以便能够得到基于我们数据的响应。我们可以按以下方式实现：

```python
user_input = "什么是感知？"

def chatbot(user_input):
    # 将问题转换为查询向量
    query_vector = create_embeddings(user_input)

    # 查找最相似的文档
    distances, indices = nbrs.kneighbors([query_vector])

    # 将文档添加到查询中以提供上下文
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 组合历史记录和用户输入
    history.append(user_input)

    # 创建消息对象
    messages=[
        {"role": "system", "content": "你是一个帮助解答AI问题的AI助手。"},
        {"role": "user", "content": history[-1]}
    ]

    # 使用聊天完成生成回应
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

- 确保提供的回应质量自然、流畅且类似人类。

- 数据的基础性：评估回应是否来源于提供的文档。

- 相关性：评估回应与提出的问题是否匹配且相关。

- 语法正确性：评估回应在语法上是否通顺。

## 使用RAG(Retervival Augmented Generation)和向量数据库的用例

RAG和向量数据库的应用场景广泛，包括：

- 问答系统：将公司数据基础化到一个聊天系统中，员工可以用来提问。
- 推荐系统：创建一个系统，匹配最相似的项，如电影、餐馆等。
- 聊天机器人服务：可以存储聊天历史，并基于用户数据个性化对话。
- 基于向量嵌入的图像搜索，适用于图像识别和异常检测。

## 总结

我们详细介绍了RAG的基本概念，从添加我们的数据到应用、用户查询和输出。为简化RAG的创建，可以使用如Semanti Kernel、Langchain或Autogen等框架。

## 作业

为了深入学习检索增强生成（RAG），您可以：

- 使用您选择的框架为应用构建前端。
- 利用LangChain或Semantic Kernel等框架，重新创建您的应用。

恭喜您完成了本课 👏。

## 学习之旅未结束，继续前行

完成本课程后，继续探索我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，以进一步提升您的生成式AI知识！
