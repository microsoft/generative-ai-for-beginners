# 探索和比较不同的 LLMs

[![探索和比较不同的 LLMs](../../../translated_images/02-lesson-banner.png?WT.96d85175e46909d65f6895923ed5f3ad0ae5e874792ccad49542fcfe8ebd12dd.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _点击上方图片观看本课视频_

在上一课中，我们了解到生成式 AI 如何改变技术格局，大型语言模型（LLMs）如何运作，以及像我们这样的初创企业如何将其应用于用例并实现增长！在本章中，我们将比较和对比不同类型的大型语言模型（LLMs），以了解它们的优缺点。

我们初创公司的下一步是探索当前的 LLMs 格局，并了解哪些适合我们的用例。

## 介绍

本课将涵盖：

- 当前格局中的不同类型的 LLMs。
- 在 Azure 中测试、迭代和比较不同的模型以满足您的用例。
- 如何部署 LLM。

## 学习目标

完成本课后，您将能够：

- 为您的用例选择合适的模型。
- 理解如何测试、迭代和提高模型性能。
- 知道企业如何部署模型。

## 理解不同类型的 LLMs

LLMs 可以根据其架构、训练数据和用例进行多种分类。理解这些差异将帮助我们的初创公司为场景选择合适的模型，并了解如何测试、迭代和提高性能。

LLM 模型有许多不同类型，您选择的模型取决于您的用途、数据、预算等。

根据您是否希望使用模型进行文本、音频、视频、图像生成等，您可能会选择不同类型的模型。

- **音频和语音识别**。对于此目的，Whisper 类型的模型是一个不错的选择，因为它们是通用的，旨在进行语音识别。它们经过多样化音频的训练，能够执行多语言语音识别。了解更多关于 [Whisper 类型模型的信息](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst)。

- **图像生成**。对于图像生成，DALL-E 和 Midjourney 是两个非常知名的选择。DALL-E 由 Azure OpenAI 提供。[阅读更多关于 DALL-E 的信息](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst)，也可以在本课程的第 9 章中找到相关内容。

- **文本生成**。大多数模型都经过文本生成的训练，您可以从 GPT-3.5 到 GPT-4 中选择多种选项。它们的成本不同，其中 GPT-4 是最昂贵的。值得在 [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) 中查看，以评估哪个模型在能力和成本方面最适合您的需求。

- **多模态**。如果您希望处理多种类型的输入和输出数据，您可能需要考虑 [gpt-4 turbo with vision 或 gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) 等模型——这是 OpenAI 模型的最新版本，能够将自然语言处理与视觉理解结合起来，实现通过多模态界面进行交互。

选择一个模型意味着您获得了一些基本功能，但这可能还不够。通常您有公司特定的数据，您需要以某种方式告知 LLM。对此有几种不同的方法，在接下来的章节中会详细介绍。

### 基础模型与 LLMs

基础模型这一术语由 [斯坦福研究人员提出](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)，定义为符合某些标准的 AI 模型，例如：

- **它们使用无监督学习或自监督学习进行训练**，这意味着它们是在未标记的多模态数据上进行训练的，不需要人工注释或数据标记。
- **它们是非常大的模型**，基于非常深的神经网络，训练了数十亿个参数。
- **它们通常旨在作为其他模型的“基础”**，这意味着可以在其基础上构建其他模型，这可以通过微调来完成。

![基础模型与 LLMs](../../../translated_images/FoundationModel.png?WT.9690c2a9f6be278baf730a5b26ea901ac6d6ede04cad555ef2b59d774ba557eb.zh.mc_id=academic-105485-koreyst)

图片来源：[基础模型和大型语言模型的基本指南 | 作者：Babar M Bhatti | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

为了进一步阐明这种区别，让我们以 ChatGPT 为例。要构建 ChatGPT 的第一个版本，使用了名为 GPT-3.5 的模型作为基础模型。这意味着 OpenAI 使用了一些特定于聊天的数据，创建了一个经过调整的 GPT-3.5 版本，专注于在对话场景中表现良好，例如聊天机器人。

![基础模型](../../../translated_images/Multimodal.png?WT.29151b07403f77b38d7dc2a3069f4c171198d59c9df6bdfccd4326c209db4432.zh.mc_id=academic-105485-koreyst)

图片来源：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 开源模型与专有模型

另一种对 LLMs 的分类方式是它们是开源的还是专有的。

开源模型是公开可用的，任何人都可以使用。它们通常由创建它们的公司或研究社区提供。这些模型可以被检查、修改和定制用于 LLMs 的各种用例。然而，它们并不总是为生产用途优化的，可能不如专有模型那样高效。此外，开源模型的资金可能有限，可能不会长期维护或更新为最新的研究。流行的开源模型示例包括 [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst)、[Bloom](https://huggingface.co/bigscience/bloom) 和 [LLaMA](https://llama.meta.com)。

专有模型是由公司拥有的，不向公众开放。这些模型通常为生产用途进行了优化。然而，它们不允许被检查、修改或定制用于不同的用例。此外，它们并不总是免费提供的，可能需要订阅或付费使用。此外，用户无法控制用于训练模型的数据，这意味着他们应信任模型所有者，以确保对数据隐私和 AI 负责任使用的承诺。流行的专有模型示例包括 [OpenAI 模型](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst)、[Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) 或 [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst)。

### 嵌入与图像生成与文本和代码生成

LLMs 还可以根据它们生成的输出进行分类。

嵌入是一组可以将文本转换为数值形式的模型，称为嵌入，即输入文本的数值表示。嵌入使机器更容易理解单词或句子之间的关系，并可以作为其他模型的输入，例如在数值数据上表现更好的分类模型或聚类模型。嵌入模型通常用于迁移学习，其中为数据丰富的替代任务构建模型，然后将模型权重（嵌入）重新用于其他下游任务。此类别的示例是 [OpenAI 嵌入](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)。

![嵌入](../../../translated_images/Embedding.png?WT.15a2282d046c6d94a54f553fa9e7f19e3ef0e65f9eb05f4d476a5d28b2dead18.zh.mc_id=academic-105485-koreyst)

图像生成模型是生成图像的模型。这些模型通常用于图像编辑、图像合成和图像翻译。图像生成模型通常在大型图像数据集上进行训练，例如 [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)，可以用于生成新图像或使用修补、超分辨率和上色技术编辑现有图像。示例包括 [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) 和 [Stable Diffusion 模型](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst)。

![图像生成](../../../translated_images/Image.png?WT.6a1995ff7d9be5a713e6aaee5f1625f31620756937c283e292ef5ffe1e30ed11.zh.mc_id=academic-105485-koreyst)

文本和代码生成模型是生成文本或代码的模型。这些模型通常用于文本摘要、翻译和问答。文本生成模型通常在大型文本数据集上进行训练，例如 [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)，可以用于生成新文本或回答问题。代码生成模型，如 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)，通常在大型代码数据集上进行训练，例如 GitHub，可以用于生成新代码或修复现有代码中的错误。

![文本和代码生成](../../../translated_images/Text.png?WT.b55b7b9b96faac1d758fb555436c56c5a323a55743b75e70198160caca3fb73c.zh.mc_id=academic-105485-koreyst)

### 编码器-解码器与仅解码器

为了讨论 LLMs 的不同架构类型，我们使用一个类比。

想象一下，您的经理给您一个任务，为学生编写一个测验。您有两个同事；一个负责创建内容，另一个负责审核。

内容创建者就像一个仅解码器模型，他们可以查看主题，看到您已经写了什么，然后根据这些内容编写课程。他们在编写引人入胜和信息丰富的内容方面非常出色，但在理解主题和学习目标方面不太擅长。仅解码器模型的例子有 GPT 系列模型，如 GPT-3。

审核者就像一个仅编码器模型，他们查看编写的课程和答案，注意它们之间的关系并理解上下文，但不擅长生成内容。仅编码器模型的例子是 BERT。

想象一下，我们也可以有一个既能创建又能审核测验的人，这就是编码器-解码器模型。例子有 BART 和 T5。

### 服务与模型

现在，让我们讨论服务与模型的区别。服务是由云服务提供商提供的产品，通常是模型、数据和其他组件的组合。模型是服务的核心组件，通常是基础模型，例如 LLM。

服务通常为生产用途进行了优化，通常比模型更容易使用，通过图形用户界面。然而，服务并不总是免费提供的，可能需要订阅或付费使用，以换取利用服务所有者的设备和资源，优化开支并轻松扩展。服务的一个例子是 [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst)，提供按使用量付费的计划，这意味着用户根据使用服务的多少按比例收费。此外，Azure OpenAI Service 在模型功能的基础上提供企业级安全和负责任的 AI 框架。

模型仅是神经网络，包含参数、权重等。允许公司本地运行，但需要购买设备、构建结构以扩展并购买许可证或使用开源模型。像 LLaMA 这样的模型可以使用，但需要计算能力来运行模型。

## 如何在 Azure 上测试和迭代不同的模型以了解性能

一旦我们的团队探索了当前的 LLMs 格局并确定了一些适合他们场景的候选者，下一步就是在他们的数据和工作负载上测试它们。这是一个通过实验和测量完成的迭代过程。
我们在前面段落中提到的大多数模型（OpenAI 模型、开源模型如 Llama2 和 Hugging Face transformers）都可以在 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) 的 [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) 中找到。

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) 是一个云平台，专为开发人员构建生成式 AI 应用程序并管理整个开发生命周期而设计——从实验到评估——通过将所有 Azure AI 服务组合到一个单一的中心，并提供一个方便的 GUI。Azure AI Studio 中的 Model Catalog 使用户能够：

- 在目录中找到感兴趣的基础模型——无论是专有的还是开源的，通过任务、许可证或名称进行筛选。为了提高搜索性，模型被组织成集合，如 Azure OpenAI 集合、Hugging Face 集合等。

![模型目录](../../../translated_images/AzureAIStudioModelCatalog.png?WT.cd7b78fc6a7b010869adb0defabce1ea5fbe62131aa7f59e54a083be8d789d24.zh.mc_id=academic-105485-koreyst)

- 查看模型卡，包括预期用途和训练数据的详细描述、代码示例和内部评估库的评估结果。

![模型卡](../../../translated_images/ModelCard.png?WT.cd385d3d0228f86cef5987e3074be75f377a95ba505d6805f7c6965dc5972693.zh.mc_id=academic-105485-koreyst)
- 通过[模型基准测试](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)面板，比较行业内可用的模型和数据集的基准测试，以评估哪个符合业务场景。

![模型基准测试](../../../translated_images/ModelBenchmarks.png?WT.634f688bb2a74b3c90a9212ecfb9b99045405b2414be3d17429cfea319c06f61.zh.mc_id=academic-105485-koreyst)

- 在自定义训练数据上微调模型，以利用Azure AI Studio的实验和跟踪功能，提高模型在特定工作负载下的性能。

![模型微调](../../../translated_images/FineTuning.png?WT.523a6ab7580c924e42e8478d072fb670f879033779b8ab5a6abb155d2fc63d5a.zh.mc_id=academic-105485-koreyst)

- 将原始预训练模型或微调版本部署到远程实时推理 - 管理计算 - 或无服务器API端点 - [按需付费](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - 以便应用程序可以使用它。

![模型部署](../../../translated_images/ModelDeploy.png?WT.a765ca6b7a396eb5d2fd346f8a211542f6fe578e2218bbe16f9fcdb5ca8f3661.zh.mc_id=academic-105485-koreyst)

> [!NOTE]
> 目录中的所有模型目前并不都支持微调和/或按需付费部署。请查看模型卡以了解模型的能力和限制。

## 改善LLM结果

我们与初创团队一起探索了不同类型的LLM和云平台（Azure Machine Learning），使我们能够比较不同的模型，在测试数据上评估它们，提高性能并将其部署在推理端点上。

但何时应该考虑微调模型而不是使用预训练模型呢？还有其他方法可以提高模型在特定工作负载上的性能吗？

企业可以采用多种方法从LLM中获得所需结果。您可以选择不同类型的模型，在生产环境中部署LLM时具有不同的训练程度、复杂性、成本和质量。以下是一些不同的方法：

- **带上下文的提示工程**。这个想法是当您提示时提供足够的上下文，以确保您得到所需的响应。

- **检索增强生成，RAG**。例如，您的数据可能存在于数据库或网络端点中，为确保在提示时包含这些数据或其子集，您可以获取相关数据并将其作为用户提示的一部分。

- **微调模型**。在这里，您在自己的数据上进一步训练模型，使模型更加精确和响应您的需求，但可能成本较高。

![LLM部署](../../../translated_images/Deploy.png?WT.0eeb36a208bf2bf97ea1058e54c74e13f5c810679cd7f3600cb2084b98d737be.zh.mc_id=academic-105485-koreyst)

图片来源：[企业部署LLM的四种方式 | Fiddler AI博客](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 带上下文的提示工程

预训练的LLM在通用自然语言任务上表现非常好，即使通过一个简短的提示（如需要完成的句子或问题）调用它们——所谓的“零样本”学习。

然而，用户能越详细地构建他们的查询，包括详细的请求和示例——上下文，答案就越准确，越接近用户的期望。在这种情况下，如果提示只包含一个示例，我们称之为“一次样本”学习，如果包含多个示例，则称为“少样本学习”。带上下文的提示工程是启动的最具成本效益的方法。

### 检索增强生成（RAG）

LLM有一个限制，即它们只能使用在训练过程中使用过的数据来生成答案。这意味着它们对训练过程之后发生的事实一无所知，也无法访问非公开信息（如公司数据）。
通过RAG可以克服这一问题，这是一种通过外部数据块增强提示的技术，考虑到提示长度限制。这由向量数据库工具（如[Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)）支持，从各种预定义数据源中检索有用的数据块并将其添加到提示上下文中。

当企业没有足够的数据、时间或资源来微调LLM，但仍希望在特定工作负载上提高性能并降低虚构风险（即现实的神秘化或有害内容）时，这项技术非常有帮助。

### 微调模型

微调是一种利用迁移学习将模型“适应”下游任务或解决特定问题的过程。与少样本学习和RAG不同，它生成一个新的模型，具有更新的权重和偏差。它需要一组训练示例，包括单个输入（提示）及其相关的输出（完成）。
如果出现以下情况，这将是首选的方法：

- **使用微调模型**。企业希望使用微调的能力较弱的模型（如嵌入模型）而不是高性能模型，从而实现更具成本效益和快速的解决方案。

- **考虑延迟**。延迟对于特定用例很重要，因此不可能使用非常长的提示或示例数量不符合提示长度限制。

- **保持更新**。企业拥有大量高质量数据和真实标签，并且有资源随时间保持这些数据的更新。

### 训练模型

从头开始训练LLM无疑是最困难和最复杂的方法，要求大量数据、熟练资源和适当的计算能力。只有在企业有领域特定的用例和大量领域中心数据的情况下才应考虑此选项。

## 知识检查

提高LLM完成结果的好方法是什么？

1. 带上下文的提示工程
1. RAG
1. 微调模型

A:3，如果您有时间、资源和高质量的数据，微调是保持更新的更好选择。然而，如果您希望改善事情并且时间不足，值得首先考虑RAG。

## 🚀 挑战

阅读更多关于如何[使用RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)为您的业务服务的信息。

## 做得很好，继续学习

完成本课后，查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

前往第3课，我们将学习如何[负责任地构建生成式AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：  
本文件是使用基于机器的AI翻译服务翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文件的本国语言版本视为权威来源。对于关键信息，建议进行专业的人类翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担责任。