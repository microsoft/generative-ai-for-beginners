<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T13:18:21+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "zh"
}
-->
[![与函数调用集成](../../../translated_images/zh/14-lesson-banner.066d74a31727ac12.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 应用生命周期

对于所有 AI 应用来说，一个重要的问题是 AI 功能的相关性。由于 AI 是一个快速发展的领域，为了确保您的应用保持相关性、可靠性和稳健性，您需要持续监控、评估和改进它。这就是生成式 AI 生命周期的作用所在。

生成式 AI 生命周期是一个指导您开发、部署和维护生成式 AI 应用的框架。它帮助您定义目标、衡量性能、识别挑战并实施解决方案。它还帮助您使应用符合您领域和利益相关者的伦理和法律标准。通过遵循生成式 AI 生命周期，您可以确保您的应用始终提供价值并满足用户需求。

## 介绍

在本章中，您将：

- 理解从 MLOps 到 LLMOps 的范式转变
- 了解 LLM 生命周期
- 生命周期工具
- 生命周期指标化和评估

## 理解从 MLOps 到 LLMOps 的范式转变

LLM 是人工智能工具库中的新工具，它们在应用的分析和生成任务中非常强大，但这种强大也对我们如何简化 AI 和传统机器学习任务带来了一些影响。

因此，我们需要一个新的范式，以动态且具有正确激励的方式适应这一工具。我们可以将较早的 AI 应用归类为“ML 应用”，而较新的 AI 应用则称为“生成式 AI 应用”或简称“AI 应用”，反映当时主流的技术和方法。这在多个方面改变了我们的叙述，看看下面的对比。

![LLMOps 与 MLOps 对比](../../../translated_images/zh/01-llmops-shift.29bc933cb3bb0080.png)

请注意，在 LLMOps 中，我们更关注应用开发者，使用集成作为关键点，采用“模型即服务”，并考虑以下指标：

- 质量：响应质量
- 伤害：负责任的 AI
- 诚实：响应的依据（合理吗？正确吗？）
- 成本：解决方案预算
- 延迟：平均令牌响应时间

## LLM 生命周期

首先，为了理解生命周期及其变化，请注意下图。

![LLMOps 信息图](../../../translated_images/zh/02-llmops.70a942ead05a7645.png)

如您所见，这与传统的 MLOps 生命周期不同。LLM 有许多新需求，如提示工程、提升质量的不同技术（微调、RAG、元提示）、负责任 AI 的不同评估和责任，最后是新的评估指标（质量、伤害、诚实、成本和延迟）。

例如，看看我们的构思过程。使用提示工程来尝试各种 LLM，探索可能性，测试假设是否正确。

请注意，这不是线性的，而是集成的循环，迭代且有一个总体循环。

我们如何探索这些步骤？让我们详细了解如何构建生命周期。

![LLMOps 工作流程](../../../translated_images/zh/03-llm-stage-flows.3a1e1c401235a6cf.png)

这看起来可能有点复杂，先关注三个大步骤。

1. 构思/探索：探索阶段，根据业务需求进行探索。原型设计，创建一个 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 并测试其对假设的有效性。
1. 构建/增强：实施阶段，现在开始评估更大数据集，实施技术，如微调和 RAG，检查解决方案的稳健性。如果不行，重新实现，添加新步骤或重构数据可能有帮助。测试流程和规模后，若效果良好并检查指标，准备进入下一步。
1. 运营化：集成阶段，现在为系统添加监控和警报系统，部署并集成到应用中。

然后，有一个管理的总体循环，关注安全、合规和治理。

恭喜，现在您的 AI 应用已准备好并投入运营。想要动手体验，请查看 [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)。

那么，我们可以使用哪些工具呢？

## 生命周期工具

在工具方面，微软提供了 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，使您的生命周期易于实现并快速启动。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 允许您使用 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)。AI Studio 是一个网页门户，允许您探索模型、示例和工具。管理资源、UI 开发流程以及用于代码优先开发的 SDK/CLI 选项。

![Azure AI 可能性](../../../translated_images/zh/04-azure-ai-platform.80203baf03a12fa8.png)

Azure AI 允许您使用多种资源，管理您的运营、服务、项目、向量搜索和数据库需求。

![使用 Azure AI 的 LLMOps](../../../translated_images/zh/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.png)

使用 PromptFlow，从概念验证（POC）到大规模应用构建：

- 从 VS Code 设计和构建应用，使用可视化和功能工具
- 轻松测试和微调您的应用，实现高质量 AI
- 使用 Azure AI Studio 集成和迭代云端，快速推送和部署

![使用 PromptFlow 的 LLMOps](../../../translated_images/zh/06-llm-promptflow.a183eba07a3a7fdf.png)

## 太棒了！继续学习吧！

非常好，现在了解更多关于如何构建应用以使用这些概念，查看 [Contoso Chat 应用](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，了解云倡导团队如何在演示中应用这些概念。更多内容，请查看我们的 [Ignite 分会场！](https://www.youtube.com/watch?v=DdOylyrTOWg)

接下来，查看第 15 课，了解 [检索增强生成和向量数据库](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影响生成式 AI，并打造更具吸引力的应用！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->