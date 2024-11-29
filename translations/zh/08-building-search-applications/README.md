# 构建搜索应用程序

[![生成式 AI 和大语言模型简介](../../../translated_images/08-lesson-banner.png?WT.38007baa37b3809836fefd9caf72cba7434d1d1e82074d170c2b066e3c7aa2d0.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _点击上面的图片查看本课视频_

大语言模型不仅限于聊天机器人和文本生成。还可以使用嵌入来构建搜索应用程序。嵌入是数据的数值表示，也称为向量，可以用于数据的语义搜索。

在本课中，您将为我们的教育初创公司构建一个搜索应用程序。我们的初创公司是一家非营利组织，为发展中国家的学生提供免费教育。我们的初创公司拥有大量的 YouTube 视频，学生可以用来学习 AI。我们的初创公司希望构建一个搜索应用程序，允许学生通过输入问题来搜索 YouTube 视频。

例如，学生可能会输入“什么是 Jupyter Notebooks？”或“什么是 Azure ML”，搜索应用程序将返回与问题相关的 YouTube 视频列表，更好的是，搜索应用程序将返回视频中问题答案所在位置的链接。

## 介绍

在本课中，我们将涵盖：

- 语义搜索与关键词搜索。
- 什么是文本嵌入。
- 创建文本嵌入索引。
- 搜索文本嵌入索引。

## 学习目标

完成本课后，您将能够：

- 区分语义搜索和关键词搜索。
- 解释什么是文本嵌入。
- 使用嵌入创建用于数据搜索的应用程序。

## 为什么要构建搜索应用程序？

创建搜索应用程序将帮助您了解如何使用嵌入来搜索数据。您还将学习如何构建一个可以让学生快速找到信息的搜索应用程序。

本课包括 Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube 频道的 YouTube 转录的嵌入索引。AI Show 是一个教授 AI 和机器学习的 YouTube 频道。嵌入索引包含截至 2023 年 10 月的每个 YouTube 转录的嵌入。您将使用嵌入索引为我们的初创公司构建一个搜索应用程序。搜索应用程序返回视频中问题答案所在位置的链接。这是一种让学生快速找到所需信息的好方法。

以下是问题“你能用 rstudio 与 azure ml 吗？”的语义查询示例。查看 YouTube URL，您会看到 URL 包含一个时间戳，带您到视频中问题答案所在的位置。

![问题“你能用 rstudio 与 Azure ML 吗？”的语义查询](../../../translated_images/query-results.png?WT.c2bcab091b108e899efca56b2cd996ea8f95145c049888f52ef7495a2b7df665.zh.mc_id=academic-105485-koreyst)

## 什么是语义搜索？

现在您可能会想，什么是语义搜索？语义搜索是一种使用查询中单词的语义或意义来返回相关结果的搜索技术。

以下是一个语义搜索的示例。假设您正在寻找购买汽车，您可能会搜索“我的梦想车”，语义搜索理解您不是`dreaming`一辆车，而是您正在寻找购买您的`ideal`车。语义搜索理解您的意图并返回相关结果。相反的是`keyword search`，它将字面上搜索关于汽车的梦想，并且经常返回不相关的结果。

## 什么是文本嵌入？

[文本嵌入](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst)是一种用于[自然语言处理](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst)的文本表示技术。文本嵌入是文本的语义数值表示。嵌入用于以机器易于理解的方式表示数据。有许多用于构建文本嵌入的模型，在本课中，我们将重点介绍使用 OpenAI 嵌入模型生成嵌入。

这是一个示例，假设以下文本是 AI Show YouTube 频道某一集的转录：

```text
Today we are going to learn about Azure Machine Learning.
```

我们将文本传递给 OpenAI 嵌入 API，它将返回一个由 1536 个数字组成的嵌入，也就是一个向量。向量中的每个数字代表文本的不同方面。为简洁起见，这里是向量的前 10 个数字。

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## 嵌入索引是如何创建的？

本课的嵌入索引是通过一系列 Python 脚本创建的。您可以在本课的“scripts”文件夹中的 [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) 中找到脚本和说明。您不需要运行这些脚本来完成本课，因为嵌入索引已经为您提供。

脚本执行以下操作：

1. 下载 [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) 播放列表中每个 YouTube 视频的转录。
2. 使用 [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst)，尝试从 YouTube 转录的前 3 分钟中提取演讲者姓名。每个视频的演讲者姓名存储在名为 `embedding_index_3m.json` 的嵌入索引中。
3. 然后将转录文本分块为**3 分钟文本段**。段包括从下一个段重叠的约 20 个单词，以确保段的嵌入不被截断并提供更好的搜索上下文。
4. 然后将每个文本段传递给 OpenAI Chat API，将文本总结为 60 个单词。摘要也存储在嵌入索引 `embedding_index_3m.json` 中。
5. 最后，将段文本传递给 OpenAI 嵌入 API。嵌入 API 返回一个由 1536 个数字组成的向量，代表段的语义意义。段以及 OpenAI 嵌入向量存储在嵌入索引 `embedding_index_3m.json` 中。

### 向量数据库

为简化课程，嵌入索引存储在名为 `embedding_index_3m.json` 的 JSON 文件中，并加载到 Pandas DataFrame 中。然而，在生产环境中，嵌入索引将存储在向量数据库中，如 [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst)、[Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst)、[Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst)、[Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) 等。

## 理解余弦相似性

我们已经了解了文本嵌入，下一步是学习如何使用文本嵌入来搜索数据，特别是使用余弦相似性查找与给定查询最相似的嵌入。

### 什么是余弦相似性？

余弦相似性是两个向量之间相似性的度量，您也会听到它被称为`nearest neighbor search`。要执行余弦相似性搜索，您需要使用 OpenAI 嵌入 API 为 _query_ 文本进行_向量化_。然后计算查询向量与嵌入索引中每个向量之间的_余弦相似性_。记住，嵌入索引为每个 YouTube 转录文本段提供一个向量。最后，根据余弦相似性对结果进行排序，余弦相似性最高的文本段与查询最相似。

从数学角度来看，余弦相似性测量两个向量在多维空间中投影的角度的余弦。这个测量很有用，因为如果两个文档因为大小而在欧几里得距离上相距很远，它们之间的角度可能仍然较小，因此具有较高的余弦相似性。有关余弦相似性方程的更多信息，请参见[余弦相似性](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)。

## 构建您的第一个搜索应用程序

接下来，我们将学习如何使用嵌入构建搜索应用程序。搜索应用程序将允许学生通过输入问题来搜索视频。搜索应用程序将返回与问题相关的视频列表。搜索应用程序还将返回视频中问题答案所在位置的链接。

此解决方案在 Windows 11、macOS 和 Ubuntu 22.04 上使用 Python 3.10 或更高版本构建和测试。您可以从 [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 下载 Python。

## 作业 - 构建搜索应用程序，帮助学生

我们在本课开始时介绍了我们的初创公司。现在是时候让学生能够为他们的评估构建一个搜索应用程序了。

在此作业中，您将创建用于构建搜索应用程序的 Azure OpenAI 服务。您将创建以下 Azure OpenAI 服务。您需要一个 Azure 订阅才能完成此作业。

### 启动 Azure 云 Shell

1. 登录 [Azure 门户](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)。
2. 选择 Azure 门户右上角的云 Shell 图标。
3. 选择 **Bash** 作为环境类型。

#### 创建资源组

> 对于这些说明，我们使用位于美国东部的名为 "semantic-video-search" 的资源组。
> 您可以更改资源组的名称，但在更改资源的位置时，
> 请查看[模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```shell
az group create --name semantic-video-search --location eastus
```

#### 创建 Azure OpenAI 服务资源

从 Azure 云 Shell，运行以下命令以创建 Azure OpenAI 服务资源。

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### 获取用于此应用程序的端点和密钥

从 Azure 云 Shell，运行以下命令以获取 Azure OpenAI 服务资源的端点和密钥。

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### 部署 OpenAI 嵌入模型

从 Azure 云 Shell，运行以下命令以部署 OpenAI 嵌入模型。

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

## 解决方案

在 GitHub Codespaces 中打开[解决方案笔记本](../../../08-building-search-applications/python/aoai-solution.ipynb)并按照 Jupyter Notebook 中的说明进行操作。

当您运行笔记本时，系统会提示您输入查询。输入框看起来像这样：

![用户输入查询的输入框](../../../translated_images/notebook-search.png?WT.2910e3d34815aab8d713050521ac5fcb2436defe66fed016f56b95867eb12fbd.zh.mc_id=academic-105485-koreyst)

## 做得好！继续学习

完成本课后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

前往第 9 课，我们将学习如何[构建图像生成应用程序](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：  
本文档使用机器翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用此翻译而产生的任何误解或误读不承担责任。