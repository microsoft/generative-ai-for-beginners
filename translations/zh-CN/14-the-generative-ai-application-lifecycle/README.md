[![与函数调用集成](../../../translated_images/zh-CN/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 应用生命周期

对所有 AI 应用来说，一个重要问题是 AI 功能的相关性。由于 AI 是一个快速发展的领域，为确保您的应用保持相关、可靠且健壮，您需要持续监控、评估和改进它。这正是生成式 AI 生命周期的作用所在。

生成式 AI 生命周期是一个指导您开发、部署和维护生成式 AI 应用各阶段的框架。它帮助您定义目标、衡量性能、识别挑战并实施解决方案。它还帮助您使应用符合所在领域和利益相关者的伦理与法律标准。遵循生成式 AI 生命周期，您可以确保应用始终提供价值并满足用户需求。

## 介绍

在本章中，您将：

- 理解从 MLOps 到 LLMOps 的范式转变
- LLM 生命周期
- 生命周期工具
- 生命周期计量和评估

## 理解从 MLOps 到 LLMOps 的范式转变

LLM 是人工智能工具库中的新工具，它们在分析和生成任务中极具威力，然而这种强大也影响了我们简化 AI 与传统机器学习任务的方式。

因此，我们需要新的范式来以动态且正确的激励方式适应这款工具。我们可以将旧的 AI 应用归类为“ML 应用”，而较新的 AI 应用则为“生成式 AI 应用”或简称“AI 应用”，反映技术和方法的主流变迁。这在多个方面改变了我们的叙事，看看以下对比。

![LLMOps 与 MLOps 对比](../../../translated_images/zh-CN/01-llmops-shift.29bc933cb3bb0080.webp)

注意在 LLMOps 中，我们更关注应用开发者，把集成作为关键点，采用“模型即服务”，并关注以下指标：

- 质量：响应质量
- 伤害：负责任的 AI
- 诚实性：响应的依据（是否有理？是否正确？）
- 成本：解决方案预算
- 延迟：平均生成单个令牌的时间

## LLM 生命周期

首先，为了理解生命周期及其变化，请看下方信息图。

![LLMOps 信息图](../../../translated_images/zh-CN/02-llmops.70a942ead05a7645.webp)

如您所见，这与传统的 MLOps 生命周期不同。LLM 拥有许多新需求，如提示工程、提升质量的不同技术（微调、RAG、元提示）、负责任 AI 的不同评估和责任，最后是新的评价指标（质量、伤害、诚实性、成本与延迟）。

例如，看我们如何进行构思。利用提示工程对各种 LLM 进行实验，探索可能性，以测试其假设是否正确。

注意这不是线性流程，而是集成循环、迭代的并包含宏观循环。

我们如何探索这些步骤？让我们深入细节，看看如何构建生命周期。

![LLMOps 工作流程](../../../translated_images/zh-CN/03-llm-stage-flows.3a1e1c401235a6cf.webp)

这看起来有点复杂，先聚焦于三个主要步骤。

1. 构思/探索：探索阶段，根据业务需求探索。进行原型设计，创建一个 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 并测试是否足够高效以验证假设。
1. 构建/增强：实施阶段，现在开始评估更大数据集，实施微调和RAG等技术，检查解决方案的鲁棒性。如果不理想，重新实施，添加新步骤或重组数据可能会有所帮助。测试流程和规模后，指标达标即可进入下一步。
1. 运营化：集成阶段，添加监控和警报系统，部署并集成到我们的应用中。

还有贯穿的管理循环，关注安全、合规和治理。

恭喜，您的 AI 应用准备就绪并可投入运营。想亲身体验一下，请查看 [Contoso 聊天演示](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)。

现在，我们可以使用哪些工具？

## 生命周期工具

在工具方面，微软提供了 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，让您的生命周期实施变得简单便捷。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 支持使用 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)。Microsoft Foundry（前身为 Azure AI Studio）是一个网页门户，允许您探索模型、示例和工具，管理资源，并使用 UI 开发流程以及 SDK/CLI 选项进行代码优先开发。

![Azure AI 可能性](../../../translated_images/zh-CN/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI 允许您利用多种资源，管理您的运营、服务、项目、向量搜索和数据库需求。

![使用 Azure AI 的 LLMOps](../../../translated_images/zh-CN/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

从概念验证（POC）到大规模应用，使用 PromptFlow 构建：

- 在 VS Code 中设计和构建应用，结合视觉和功能工具
- 轻松测试和微调应用，确保 AI 质量
- 使用 Microsoft Foundry 与云端集成迭代，快速推送和部署集成

![使用 PromptFlow 的 LLMOps](../../../translated_images/zh-CN/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 太棒了！继续学习吧！

很棒，现在了解如何构建应用以使用这些概念，参见 [Contoso Chat 应用](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，查看云推广如何在演示中加入这些概念。更多内容，请查看我们的 [Ignite 突破会议！
](https://www.youtube.com/watch?v=DdOylyrTOWg)

接下来，查看第 15 课，了解 [检索增强生成和向量数据库](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影响生成式 AI 并打造更具吸引力的应用！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->