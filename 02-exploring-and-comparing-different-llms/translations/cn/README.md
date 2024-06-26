# 第二章 : 探索和比较不同的 LLMs

[![Exploring and comparing different LLMs](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _点击该图片看本章导学视频_

在上一章中，我们了解了生成式人工智能如何改变技术格局、LLMs 工作原理，以及企业（例如“Our startup”）如何将它们应用到自己的应用场景中并得到发展！ 在本章中，我们将比较和对比不同类型的大型语言模型以了解它们的优缺点。

我们初创公司技术旅程的下一步是 LLMs 的前景并了解哪些适合我们的案例

## 本章概述

本章内容包括：

- 当前落地的不同类型的 LLMs 。
- 在 Azure 中测试、迭代和不同模型使用场景的比较
- 如何部署 LLMs 。

## 学习目标

完成本章学习后，您将会学习到：

- 为您的应用场景选择合适的模型。
- 了解如何测试、迭代和提高模型的性能。
- 了解企业如何部署模型。

## 认识不同的 LLMs

大型语言模型 (LLM) 可以根据其架构、训练数据和用例进行多种分类。 了解这些差异将有助于“Our startup”根据场景选择正确的模型，并了解如何测试、迭代和提高性能。

LLM 模型有许多不同类型，您选择的模型取决于您的用途、您的数据、您准备支付的费用等等。

根据您是否打算使用模型进行文本、音频、视频、图像生成等，您可能会选择不同类型的模型。

- **音频和语音识别**。 为此，Whisper 模型是一个不错的选择，因为它们是通常用于语音识别。 它经过不同音频数据的训练，可以执行多语言语音识别。 例如，您可以使用所有的模型，从价格便宜但功能强大的模型（如 Curry）到更昂贵拥有高性能的达芬奇（Davinci）模型。 详细了解 [ Whisper 类型模型](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst)。

- **图像生成**。 对于图像生成，DALL-E 和 Midjourney 是两个最佳的选择。 DALL-E 由 Azure OpenAI 提供。 [在此处阅读有关 DALL-E 的更多信息](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) 以及本课程的第九章。

- **文本生成**。 大多数模型都经过文本生成训练，您有从 GPT-3.5 到 GPT-4 的多种选择。 它们的成本各不同，其中 GPT-4 是最昂贵的。 值得研究一下 [Azure OpenAI Playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst)，以评估哪些模型在功能和成本方面适合你的实际需求。

选择模型意味着您能获得一些基本功能，但这可能还不够。 通常，您有公司特定的数据，您需要以某种方式告诉 LLMs。 关于如何解决这个问题，有几种不同的选择，接下来的部分将详细介绍。

### 认识基础模型与 LLMs

“基础模型”是[由斯坦福大学研究人员创造](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)，定义为遵循某些标准的人工智能模型，例如：

- **他们使用无监督学习或自监督学习进行训练**，这意味着他们接受未标记的多模式数据的训练，并且他们的训练过程不需要人工注释或数据标记。
- **它们是非常大的模型**，基于经过数十亿参数训练的深度神经网络。
- **它们通常旨在作为其他模型的“基础”**，这意味着它们可以用作构建其他模型的起点，可以通过微调方式来完成。

![基础模型与 LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

图片来源：[基础模型和大语言模型基本指南| 巴巴尔·M·巴蒂 (Babar M Bhatti) | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

为了进一步阐明这种区别，我们以 ChatGPT 为例。 为了构建 ChatGPT 的第一个版本，名为 GPT-3.5 的模型作为基础模型。 这意味着 OpenAI 使用一些特定于聊天的数据来创建 GPT-3.5 的调整版本，专门用于在对话场景（例如聊天机器人）中让其有更好的表现。

![基础模型](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

图片来源：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 认识开源模型与专有模型

对 LLM 进行分类的另一种方法是它们是开源的还是专有的。

开源模型是向公众开放并且任何人都可以使用的模型。 它们通常由创建它们的公司或研究团体提供。 这些模型可以针对 LLMs 的各种用例进行检查、修改和定制。 然而，它们并不总是针对生产用途进行优化，并且可能不如专有模型具备高性能。 此外，开源模型的资金可能有限，并且它们可能无法长期维护或可能无法根据最新研究进行更新。 流行的开源模型的例子包括 [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)、[Bloom](https://sapling.ai/llm/bloom) 和 [ LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst)。

专有模型是公司拥有的模型，不向公众提供。 这些模型通常针对生产用途进行了优化。 但是，不允许针对特定的使用场景进行检查、修改或定制它们。 另外，它们并不总是免费提供，可能需要订阅或付费才能使用。 此外，用户无法控制用于训练模型的数据，这意味着他们应该委托模型所有者确保对数据隐私和负责任地使用人工智能的承诺。 流行的专有模型的例子包括 [OpenAI 模型](https://platform.openai.com/docs/models/overview)、[Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) 或 [Claude 2](https://www.anthropic.com/index/claude-2)。

### 认识嵌入式，图像生成，文本或代码生成

LLMs 还可以根据其产生的输出进行分类。

嵌入是一组可以将文本转换为数字形式的模型，称为嵌入，它是输入文本的数字表示。 嵌入使机器更容易理解单词或句子之间的关系，并且可以用作其他模型的输入，例如分类模型或对数值数据具有更好性能的聚类模型。 嵌入模型通常用于迁移学习，其中为有大量数据的代理任务构建模型，然后将模型权重（嵌入）重新用于其他下游任务。 此类别的一个示例是 [OpenAI 嵌入](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)。

![嵌入](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

图像生成模型主要是用来生成图像。 这些模型通常用于图像编辑、图像合成和图像翻译。 图像生成模型通常在大型图像数据集上进行训练，例如 [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)，并且可用于生成新图像或编辑现有图像 修复、超分辨率和着色技术。 如 [DALL-E-3](https://openai.com/dall-e-3) 和 [StableDiffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst)。

![Image generation](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

文本或代码生成模型主要是生成文本或代码。 这些模型通常用于文本摘要、翻译和问答。 文本生成模型通常在大型文本数据集上进行训练，例如 [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html)，并且可用于生成新文本或回答问题。 代码生成模型，例如 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)，通常在大型代码数据集（如 GitHub）上进行训练，可用于生成新代码或修复现有代码中的错误。

![Text and code generation](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### 了解编码-解码器与独立解码器

为了讨论 LLMs 的不同类型的架构，让我们来打个比方。

想象一下，您的经理给您一个为学生编写测验题目的任务。 您有两个同事； 一名负责监督内容的创建，另一名负责审查内容。

内容创建者就像一个独立解码器的模型，他们可以查看主题并查看您已经写的内容，然后他可以基于这些内容来编写课程。 他们非常擅长撰写引人入胜且内容丰富的内容，但不太擅长理解主题和学习目标。 独立解码器模型如 GPT 系列模型，例如 GPT-3。

审阅者就像一个独立编码器的模型，他们查看编写的课程和答案，注意它们之间的关系并通过上下文进行理解，但他们不擅于生成内容。独立编码器模型的一个例子是 BERT。

想象一下，我们也可以有人可以创建和审查测验，这是一个编码器-解码器模型如 BART 和 T5

### 理解服务与模型

现在，我们来谈谈服务和模型之间的区别。 服务是云服务提供商提供的产品，通常是模型、数据和其他组件的结合。 模型是服务的核心组件，通常是基础模型，例如各种 LLM。

服务通常针对生产环境进行了优化，并且通常比模型让用户通过图形界面使用。 但服务并不总是免费提供的，可能需要订阅或付费才能使用，以换取服务所有者的设备和相关资源，优化费用并轻松扩展。 服务的一个例子是 [Azure OpenAI 服务](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst)，它提供按需付费计划，意味着用户根据服务用量付费。此外，Azure OpenAI Service 在模型功能上还提供企业级安全性和负责任的 AI 框架。

模型是带有参数、权重等的神经网络。 允许公司在本地运营需要购买设备、构建并购买许可证或使用开源模型。 像 LLaMA 这样的模型使用就需要额外的算力运行

## 如何使用不同的模型进行测试和迭代从而了解 Azure 上的运行性能

一旦我们的团队探索了当前的 LLMs 前景并为他们的场景确定了一些好的候选模型后，下一步就是根据他们的数据和工作负载行测试。 这是一个迭代过程，通过实验和量化来完成。
我们在前面的段落中提到的大多数模型（OpenAI 模型、Llama2 等开源模型和 Hugging Face transformers）都可以在 [Azure 机器学习工作室](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst) 中的目录中找到 [基础模型](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) 。

[Azure 机器学习](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst) 是一项云服务，专为数据科学家和机器学习工程师设计，用于管理整个机器学习生命周期（训练、测试、部署和 MLOps 相关的工作）在一个平台上。 机器学习工作室为此服务提供图形用户界面，使用户能够：

- 在目录中查找感兴趣的基础模型，按任务、许可证或名称进行过滤。 还可以导入尚未包含在目录中的新模型。
- 查看模型名片(包括详细描述和代码示例,并通过提供示例提示来测试结果),使用示例推理小部件对其进行测试。

![Model card](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- 使用特定工作负载和输入中提供的特定数据集的评估指标来评估模型性能。

![Model evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- 利用 Azure 机器学习的实验和跟踪功能，根据自定义训练数据微调模型，以提高特定工作负载中的模型性能。

![Model fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- 将原始预训练模型或微调版本模型部署到远程实时推理或批处理端点，以使应用程序能够直接使用。

![Model deployment](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## 提升 LLM 的输出结果准确度

我们与 “Our startup” 团队一起探索了不同类型的 LLMs 和云平台（Azure 机器学习），使我们能够比较不同的模型，根据测试数据对其进行评估，提高性能并将其部署在推理端点上。

但是他们什么时候应该考虑微调模型而不是使用预先训练的模型呢？ 是否有其他方法可以提高模型在特定工作负载上的性能？

企业可以使用多种方法从 LLMs 获得所需的结果，您可以选择具有不同训练程度的不同类型的模型

在生产中部署 LLMs ，具有不同程度的复杂性、成本和质量。 以下是一些不同的方法：

- **根据上下文的提示工程**。 这个想法是在提示时提供足够的背景信息，以确保获得所需的结果。

- **检索增强生成，RAG**。 例如，您的数据可能存在于向量数据库或 Web 端点中，为了确保在提示时包含此数据或其子集，您可以获取相关数据并对用户进行提示。

- **微调模型**。 在这里，您根据自己的数据进一步训练模型，这使得模型更加准确并且能够响应您的需求，但可能成本高昂。

![LLMs deployment](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

图片来源: [企业部署 LLM 的四种方式| Fiddler AI 博客](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 通过上下文的提示工程

预先训练的 LLMs 在广义自然语言任务上表现得非常好，甚至可以用简短的提示来调用它们，比如要完成的句子或问题——即所谓的“零样本”学习。

然而，用户越能通过详细的请求和示例（上下文）来构建他们的查询，就会得到最准确、最接近用户期望的答案。 在这种情况下，如果提示仅包含一个示例，我们讨论“单样本”学习；如果提示包含多个示例，我们讨论“少样本学习”。

根据上下文进行快速工程设计是最具成本效益的启动方法。

### 检索增强生成 (RAG)

LLMs 有一个限制，即他们只能使用训练期间使用过的数据来生成答案。 这意味着他们对训练过程后发生的事情一无所知，并且无法访问非公开信息（例如公司数据）。
这可以通过 RAG 来克服，RAG 是一种考虑提示长度限制的技术，以文档块的形式使用外部数据来增强提示。 矢量数据库工具（例如 [Azure 向量搜索](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)）支持此功能，可检索有用的信息来自各种预定义数据源的块并将它们添加到提示上下文中。

当企业没有足够的数据、足够的时间或资源来微调 LLMs，但仍希望提高特定工作负载的性能并减少幻觉的风险（即对现实的神秘化或有害的风险）时，此技术非常有用

### 微调模型

微调是一个利用迁移学习使模型“适应”下游任务或解决特定问题的过程。 与少样本学习和 RAG 不同，它会生成一个新模型，并更新权重和偏差。 它需要一组训练示例，其中包含单个输入（提示）及其关联的输出（完成）。

如果出现以下情况，这将是首选方法：

- **使用微调模型**。 企业希望使用经过微调能力较差的模型（例如嵌入模型）而不是高性能模型，从而获得更具成本效益和快速的解决方案。

- **考虑延迟**。 延迟对于特定用例很重要，因此不可能使用很长的提示，或者应该从模型中学习的示例数量不符合提示长度限制。

- **保持最新状态**。 企业拥有大量高质量的数据和真实标签，以及随着时间的推移保持这些数据最新所需的资源。

### 训练垂直行业模型

从头开始培训 LLMs 无疑是最困难、最复杂的方法，需要大量数据、熟练资源和适当的计算能力。 仅在企业具有特定领域的用例和大量以特定领域为中心的数据的情况下才应考虑此选项。

## 知识检查

提升 LLMs 输出效率最好的方法是什么？

1. 根据背景提示进行工程设计
2. RAG
3. 模型微调

A：3，如果您有时间和资源以及高质量的数据，微调是保持最新状态的更好选择。 然而，如果您正在寻求改进，但又缺乏时间，那么值得首先考虑 RAG。

## 🚀 知识拓展

详细了解如何为您的业务 [使用 RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)。

## 继续您的学习旅程

想要了解更多关于不同的生成人工智能概念吗？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关本章的其他重要资源。

前往第三章，我们将了解如何[负责任地使用生成式 AI 进行应用构建](../../../03-using-generative-ai-responsibly/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)！
