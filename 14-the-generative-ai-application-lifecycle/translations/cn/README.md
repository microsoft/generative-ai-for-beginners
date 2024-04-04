# 生成式AI应用生命周期

在所有AI应用的开发中，一个核心问题是如何保持AI特性的持续相关性。鉴于AI技术的快速进步，为了确保你的应用能够持续提供相关、可靠且强大的性能，你需要不断地监控、评估并优化它。这正是生成式AI生命周期发挥作用的地方。

生成式AI生命周期提供了一个框架，指引你穿越开发、部署和维护生成式AI应用的各个阶段。它帮助你明确目标、衡量性能、识别挑战，并实施解决方案。此外，它还支持你确保应用遵循特定领域及其利益相关者的伦理和法律标准。遵循生成式AI生命周期，可以保证你的应用持续创造价值，满足用户需求。

## 引言

在本章中，你将学到：

- 从MLOps到LLMOps的范式转变
- LLM生命周期
- 生命周期工具
- 生命周期量化与评估

## 从MLOps到LLMOps的范式转变

大型语言模型(LLMs)作为人工智能工具箱中的新成员，它们在分析和生成任务中表现出强大的能力。然而，这种能力也给我们如何高效地管理AI和传统机器学习任务带来了挑战。

这要求我们采用新的范式来适应这一变化，以正确的激励措施引导其发展。我们可以将传统的AI应用称为“ML应用”，将基于最新技术和技术的新型AI应用称为“GenAI应用”或简称“AI应用”。这种分类方式从多个方面改变了我们的讨论框架，如下比较所示。

![LLMOps vs. MLOps comparison](../../images/01-llmops-shift.png?WT.mc_id=academic-105485-koreys)

注意，在LLMOps中，我们更加关注应用开发者，并将集成作为关键点，采用“模型即服务”，并围绕以下几个关键指标进行思考：

- 质量：响应的质量
- 危害：负责任的AI
- 诚信：响应的合理性（是否有意义？是否正确？）
- 成本：解决方案的预算
- 延迟：令牌响应的平均时间

## LLM生命周期

首先，让我们通过下图了解生命周期及其变化。

![LLMOps infographic](../../images/02-llmops.png?WT.mc_id=academic-105485-koreys)

可以看出，这与MLOps的传统生命周期有所不同。LLMs引入了许多新的需求，如提示工程、质量改进技术（微调、RAG、元提示）、负责任AI的不同评估和责任，以及新的评估指标（质量、危害、诚信、成本和延迟）。

例如，看看我们如何进行构思。利用提示工程与不同LLMs进行实验，探索各种可能性，测试假设是否成立。

注意，这不是一个线性过程，而是一个集成的循环过程，迭代且具有一个总体周期。

我们应该如何探索这些步骤？让我们深入了解如何构建一个生命周期。

![LLMOps Workflow](../../images/03-llm-stage-flows.png?WT.mc_id=academic-105485-koreys)

这个过程可能看起来复杂，让我们先关注三个主要步骤：

1. 构思/探索：在这里，我们可以根据业务需求进行探索。原型设计，创建[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，并测试其是否足够有效来验证我们的假设。
2. 构建/增强：现在开始评估更大的数据集并实施技术，如微调和RAG，以检验我们的解决方案的稳健性。如果不符合要求，重新实施、添加新的流程步骤或重组数据可能会有所帮助。经过流程和规模测试后，如果一切顺利并满足我们的指标，就准备进入下一个阶段。
3. 运营化：集成监控和警报系统到我们的系统，部署和应用程序集成。

然后，我们有管理的整体周期，重点关注安全、合规和治理。

恭喜，现在你的AI应用已经准备就绪，可以投入使用了。想要动手体验，可以尝试[Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

那么，我们可以使用哪些工具呢？

## 生命周期工具

Microsoft提供的[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)和[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，简化了生命周期的实施，让你的应用快速上线。

通过[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)，你可以利用[AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)。AI Studio是一个网页门户，让你可以探索模型、示例和工具，管理资源，进行UI开发流程，以及提供SDK/CLI选项进行代码优先开发。

![Azure AI possibilities](../../images/04-azure-ai-platform.png?WT.mc_id=academic-105485-koreys)
Azure AI让你可以使用多种资源，管理你的操作、服务、项目、向量搜索和数据库需求。

![LLMOps with Azure AI](../../images/05-llm-azure-ai-prompt.png?WT.mc_id=academic-105485-koreys)

从概念证明(POC)到大规模应用，利用PromptFlow进行构建：

- 从VS Code设计和构建应用，使用视觉和功能工具。
- 轻松测试和微调你的应用，以实现高质量AI。
- 使用Azure AI Studio进行集成和迭代，通过云推送和部署实现快速集成。

![LLMOps with PromptFlow](../../images/06-llm-promptflow.png?WT.mc_id=academic-105485-koreys)

## 继续学习！

通过[Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)深入学习我们如何将这些概念应用于实际应用开发，并查看Cloud Advocacy如何在演示中加入这些概念。想要获取更多内容，不妨观看我们的[Ignite breakout session!](https://www.youtube.com/watch?v=DdOylyrTOWg)

接下来，通过第15课，了解[检索增强生成和向量数据库](#)如何影响生成式AI，使应用更加吸引用户！
