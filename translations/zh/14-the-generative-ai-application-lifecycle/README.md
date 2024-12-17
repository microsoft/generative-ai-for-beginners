[![Integrating with function calling](../../../translated_images/14-lesson-banner.png?WT.833a8de2ff3806528caaf839db4385f00ff7c9f92ccdd38d886f4d662fc72f2a.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# 生成式 AI 应用程序生命周期

对于所有 AI 应用程序而言，一个重要的问题是 AI 特性的相关性。由于 AI 是一个快速发展的领域，为了确保您的应用程序保持相关性、可靠性和稳健性，您需要不断地监控、评估和改进。这就是生成式 AI 生命周期的用武之地。

生成式 AI 生命周期是一个框架，指导您完成开发、部署和维护生成式 AI 应用程序的各个阶段。它帮助您定义目标、衡量性能、识别挑战并实施解决方案。它还帮助您将应用程序与您所在领域和利益相关者的伦理和法律标准对齐。通过遵循生成式 AI 生命周期，您可以确保您的应用程序始终提供价值并满足用户需求。

## 介绍

在本章中，您将：

- 理解从 MLOps 到 LLMOps 的范式转变
- 了解 LLM 生命周期
- 生命周期工具
- 生命周期度量和评估

## 理解从 MLOps 到 LLMOps 的范式转变

LLM 是人工智能武器库中的一种新工具，它在应用程序的分析和生成任务中非常强大，但这种力量对我们如何简化 AI 和经典机器学习任务产生了一些影响。

因此，我们需要一个新的范式来动态地适应这一工具，并提供正确的激励。我们可以将旧的 AI 应用程序分类为“ML 应用程序”，而将新的 AI 应用程序分类为“GenAI 应用程序”或简单的“AI 应用程序”，以反映当时使用的主流技术和技术。这在多个方面改变了我们的叙述，请看下面的比较。

![LLMOps vs. MLOps comparison](../../../translated_images/01-llmops-shift.png?WT.38bc3eca81f659d83b17070d0a766bc3a9f13284b92c307e296915db4e683fcf.zh.mc_id=academic-105485-koreys)

注意，在 LLMOps 中，我们更关注应用程序开发者，将集成作为关键点，使用“模型即服务”并考虑以下指标。

- 质量：响应质量
- 危害：负责任的 AI
- 诚实：响应的合理性（有意义吗？它正确吗？）
- 成本：解决方案预算
- 延迟：平均令牌响应时间

## LLM 生命周期

首先，为了理解生命周期和修改，让我们注意下一个信息图。

![LLMOps infographic](../../../translated_images/02-llmops.png?WT.32553adc9de4d89bb1d6a2f1f99d985457158a3be863e8e5dddc5e3dd074558a.zh.mc_id=academic-105485-koreys)

如您所见，这与 MLOps 的常规生命周期不同。LLM 有许多新的要求，如提示、不同的技术以提高质量（微调、RAG、元提示）、负责任 AI 的不同评估和责任，最后是新的评估指标（质量、危害、诚实、成本和延迟）。

例如，看看我们是如何构思的。使用提示工程来实验各种 LLM，以探索可能性并测试他们的假设是否正确。

注意，这不是线性的，而是集成的循环，迭代的，并且有一个全面的循环。

我们如何探索这些步骤？让我们详细了解如何构建一个生命周期。

![LLMOps Workflow](../../../translated_images/03-llm-stage-flows.png?WT.118920c8fd638f0879fe06c5e6eb9d91536e8b9c6bc56808ebed8706812f5391.zh.mc_id=academic-105485-koreys)

这可能看起来有点复杂，让我们先关注三个大步骤。

1. 构思/探索：探索，在这里我们可以根据业务需求进行探索。制作原型，创建一个 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 并测试它是否足够高效以验证我们的假设。
2. 构建/增强：实现，现在，我们开始评估更大的数据集，实施技术，如微调和 RAG，以检查解决方案的稳健性。如果不够，可以重新实施，添加新步骤到我们的流程或重组数据。测试我们的流程和规模后，如果有效并检查我们的指标，就可以进入下一步。
3. 运作：集成，现在将监控和警报系统添加到我们的系统中，部署和应用程序集成到我们的应用程序中。

然后，我们有一个专注于安全、合规和治理的全面管理循环。

恭喜，现在您的 AI 应用程序已准备好运行。要获得实践经验，请查看 [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

现在，我们可以使用哪些工具？

## 生命周期工具

对于工具，Microsoft 提供了 [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，以便于实施和准备启动您的周期。

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 允许您使用 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)。AI Studio 是一个网络门户，允许您探索模型、示例和工具。管理您的资源、UI 开发流程和 SDK/CLI 选项以进行代码优先开发。

![Azure AI possibilities](../../../translated_images/04-azure-ai-platform.png?WT.a39053c2efd7670298a79282658a9f5bf903dec5c1938b1a08cf45f1284e6ac0.zh.mc_id=academic-105485-koreys)

Azure AI 允许您使用多种资源，管理您的操作、服务、项目、向量搜索和数据库需求。

![LLMOps with Azure AI](../../../translated_images/05-llm-azure-ai-prompt.png?WT.9189130ce4f2e7c8667fc7c83c6b89236ce5c6361150f47104c27c105f04b487.zh.mc_id=academic-105485-koreys)

从概念验证（POC）到大型应用程序，使用 PromptFlow 构建：

- 从 VS Code 设计和构建应用程序，使用视觉和功能工具
- 轻松测试和微调您的应用程序以获得高质量 AI
- 使用 Azure AI Studio 与云集成和迭代，快速集成进行推送和部署

![LLMOps with PromptFlow](../../../translated_images/06-llm-promptflow.png?WT.e479dfedaa5f6ef7d36a11edbff74ac5579c3121ba0be0ee32eb5fc3eb17bd77.zh.mc_id=academic-105485-koreys)

## 太棒了！继续学习！

太棒了，现在了解更多关于我们如何构建应用程序以使用这些概念的内容，请查看 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，了解云倡导如何在演示中添加这些概念。有关更多内容，请查看我们的 [Ignite 分组会议！](https://www.youtube.com/watch?v=DdOylyrTOWg)

现在，查看第 15 课，了解 [检索增强生成和向量数据库](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影响生成式 AI 并制作更具吸引力的应用程序！

**免责声明**：  
本文件是使用基于机器的AI翻译服务翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议进行专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。