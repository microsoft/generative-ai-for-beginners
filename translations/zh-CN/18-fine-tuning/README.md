[![开源模型](../../../translated_images/zh-CN/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微调您的大语言模型

使用大型语言模型构建生成式 AI 应用面临新的挑战。一个关键问题是确保模型针对特定用户请求生成内容时的响应质量（准确性和相关性）。在之前的课程中，我们讨论了诸如提示工程和检索增强生成等技术，这些技术试图通过_修改输入提示_来解决这一问题。

本节课中，我们将讨论第三种技术，<strong>微调</strong>，该技术试图通过_使用额外数据重新训练模型本身_来解决这一挑战。让我们深入了解细节。

## 学习目标

本课程介绍了预训练语言模型微调的概念，探讨了该方法的优势和挑战，并提供了关于何时以及如何使用微调来提升生成式 AI 模型性能的指导。

课程结束后，您应该能够回答以下问题：

- 什么是语言模型的微调？
- 何时以及为何使用微调？
- 如何微调预训练模型？
- 微调有哪些局限？

准备好了吗？让我们开始吧。

## 图解指南

想要先了解我们将要涵盖的主要内容吗？请查看这份图解指南，它描述了本课的学习旅程——从学习微调的核心概念和动机，到理解执行微调任务的流程和最佳实践。这是一个非常有趣的探索主题，别忘了查看[资源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)页面，获取更多支持您自学旅程的链接！

![语言模型微调图解指南](../../../translated_images/zh-CN/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什么是语言模型的微调？

大型语言模型被定义为基于来自互联网等多样来源的大量文本进行_预训练_。如我们之前课程所学，我们需要类似_提示工程_和_检索增强生成_的技术来提升模型对用户提问（“提示”）的响应质量。

一种流行的提示工程技术是通过提供_指令_（明确指导）或_几个示例_（隐式指导）来给模型更多关于预期响应的引导。这被称为_少样本学习_，但它有两个限制：

- 模型的令牌限制可能限制你能给出的示例数量，从而限制效果。
- 令牌成本可能使得在每个提示中添加示例费用昂贵，限制灵活性。

微调是机器学习系统中的常用实践，我们从预训练模型开始，使用新数据重新训练它，以提升其在特定任务上的表现。在语言模型的背景下，我们可以用_为特定任务或应用领域精选的一组示例_对预训练模型进行微调，以创建一个更适合该领域或任务、更准确相关的<strong>定制模型</strong>。微调的一个副作用是它还可以减少少样本学习所需的示例数，从而降低令牌使用和相关成本。

## 何时以及为何应微调模型？

在_这里_讨论的微调，指的是<strong>监督学习</strong>中的微调，即通过<strong>添加新的数据</strong>来重新训练模型，而这些数据不包含在原始训练集内。这不同于无监督微调方法，无监督微调是在原始数据上，使用不同超参数重新训练模型。

关键要记的是，微调是一项高级技术，需要一定专业知识才能达到预期效果。错误操作可能不会带来预期的改进，甚至可能降低模型在目标领域的性能。

因此，在学习“如何”微调语言模型之前，您需要明确“为何”选择这条路径，以及“何时”开始微调流程。先问自己以下问题：

- <strong>用例</strong>：您的微调_用例_是什么？您想提升预训练模型的哪些方面？
- <strong>替代方案</strong>：您是否尝试过_其他技术_来达到预期效果？使用它们创建基线进行比较。
  - 提示工程：尝试像用相关提示响应示例进行少样本提示这样的技术。评估响应质量。
  - 检索增强生成：尝试通过搜索数据检索结果增强提示。评估响应质量。
- <strong>成本</strong>：您是否评估过微调所需成本？
  - 可调性——所用预训练模型是否支持微调？
  - 工作量——训练数据准备，模型评估与优化工作。
  - 计算资源——微调作业运行及微调后模型部署所需资源。
  - 数据——用于微调的足够高质量示例的获取。
- <strong>收益</strong>：您是否确认过微调的收益？
  - 质量——微调模型是否超过基线模型表现？
  - 成本——是否简化提示从而减少令牌使用？
  - 可扩展性——能否将基础模型用在新的领域？

回答这些问题后，您应该能判断微调是否适合您的用例。理想情况下，只有当利益大于成本时，才可采用该方法。一旦决定继续，就需要考虑_如何_微调预训练模型。

想了解更多决策过程的见解？请观看[是否微调？](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 我们如何微调预训练模型？

微调预训练模型需要准备：

- 一个待微调的预训练模型
- 一套用于微调的数据集
- 一个运行微调作业的训练环境
- 一个部署微调模型的托管环境

## 在 Microsoft Foundry 上微调

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 是您在 Azure 上微调、部署和管理定制模型的地方（它整合了原先的 Azure OpenAI Studio 和 Azure AI Studio）。开始作业前，了解 Foundry 所提供的选项以及平台的最佳实践是有帮助的。Foundry 底层使用<strong>LoRA（低秩适配）</strong>来高效地微调模型，这使得训练比重新训练每个权重更快且成本更低。

### 步骤 1：选择训练技术

Foundry 支持三种微调技术。**从监督微调（SFT）开始**，它涵盖了最广泛的场景。

| 技术 | 作用 | 何时使用 |
| --- | --- | --- |
| **监督微调 (SFT)** | 通过输入/输出示例对训练，使模型学会生成期望的响应。 | 多数任务的默认选择：领域专精，任务性能，风格与语气，指令遵循，语言适应。 |
| **直接偏好优化 (DPO)** | 通过学习_偏好与非偏好_响应对以使输出与人类偏好一致。 | 当有比较反馈时，用于提升响应质量、安全性和一致性。 |
| **强化微调 (RFT)** | 使用_评分系统_的奖励信号，通过强化学习优化复杂行为。 | 客观性强、推理密集的领域（数学、化学、物理）且答案明确对错。需要较高的机器学习专业技能。 |

### 步骤 2：选择训练级别

Foundry 允许您选择训练运行的方式和地点：

- <strong>标准</strong> - 在您资源所在区域训练，确保数据驻留。当数据必须留在特定区域时使用。
- <strong>全球</strong> - 利用非所属区域的容量，队列更便宜更快（数据和权重复制到训练区）。数据驻留无要求时的良好默认选项。
- <strong>开发者</strong> - 这是最低成本选项，使用闲置容量，无延迟/SLA保证（作业可能被抢占后恢复）。适合实验。

### 步骤 3：选择基础模型

支持微调的模型包括 OpenAI 的 `gpt-4o-mini`、`gpt-4o`、`gpt-4.1`、`gpt-4.1-mini` 和 `gpt-4.1-nano`（SFT；4o/4.1 系列也支持 DPO），推理模型 `o4-mini` 和 `gpt-5`（RFT），以及开源模型如 `Ministral-3B`、`Qwen-32B`、`Llama-3.3-70B-Instruct` 和 `gpt-oss-20b`（Foundry 资源上的 SFT）。请务必查看当前[微调模型列表](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)了解支持的方法、区域和可用性。

> Foundry 提供两种模式：<strong>无服务器</strong>（按消费计费，无需管理 GPU 配额，支持 OpenAI 及精选模型）和<strong>托管计算</strong>（通过 Azure 机器学习带自有虚拟机，支持最广泛的模型）。大多数用户应先尝试无服务器模式。

### Foundry 最佳实践

- **先建立基线。** 在微调之前，先用提示工程和 RAG 测量基础模型表现，以证明增益。
- **从小规模开始，再扩大。** 先用 50-100 个高质量示例验证方法，之后扩展到 500+ 以用于生产。质量优于数量，剔除低质量示例。
- **正确格式化数据。** 训练和验证文件须为 JSONL，UTF-8 **带 BOM**，大小不超过 512 MB，使用聊天完成功能消息格式。一定要包含验证文件，以监测过拟合。
- **推理时保留训练用系统提示。** 调用模型时使用与训练时相同的系统消息。
- **评估检查点 —— 不要盲目部署最后一个。** Foundry 会保存最近三个训练周期作为可部署检查点；根据 `train_loss` / `valid_loss` 和令牌准确度选取泛化能力最好的版本。
- **比较微调模型与基线时同时测量令牌成本和质量。**
- **持续微调迭代。** 可以在已微调模型上用新数据继续微调（对 OpenAI 模型支持）。
- **注意托管成本。** 部署的定制模型按小时计费，闲置部署 15 天后自动移除——清理不需要的部署。

完成[用微调自定义模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst)的全流程演练，准备好尝试其他技术时，可以查看 [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) 和 [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) 指南。

## 微调实战

以下资源提供逐步教程，带您使用精选数据集在当前支持的模型上完成示例。要执行这些教程，您需要在对应提供商处拥有账户，并能访问相关模型和数据集。

| 提供商       | 教程                                                                                                                                                                         | 描述                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微调聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                        | 了解如何为特定领域（“食谱助手”）微调 OpenAI 最近的聊天模型，包括准备训练数据、运行微调作业以及使用微调模型进行推理。                                                                                                                                                                                                                                                                                                   |
| Microsoft Foundry | [使用微调定制模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)        | 了解如何在 Microsoft Foundry 中微调当前支持的模型，如 `gpt-4.1-mini` **在 Azure 上**：准备与上传训练及验证数据，运行微调作业，然后部署并使用新模型。                                                                                                                                                                                                                                                                           |

| Hugging Face | [使用 Hugging Face 微调 LLM](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | 本博客文章将向您演示如何使用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 库和 [Transformer 强化学习（TRL）](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) 对 _开源 LLM_（例如 `CodeLlama 7B`）进行微调，使用 Hugging Face 上的开放[数据集](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst)。 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [使用 AutoTrain 微调 LLM](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 开发的 Python 库，支持多种任务的微调，包括 LLM 微调。AutoTrain 是一个无需编码的解决方案，微调可以在您自己的云端、Hugging Face Spaces 或本地完成。它支持基于网页的 GUI、命令行界面（CLI）以及通过 yaml 配置文件进行训练。                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [使用 Unsloth 微调 LLM](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth 是一个开源框架，支持 LLM 微调和强化学习（RL）。Unsloth 通过现成的[笔记本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)简化了本地训练、评估和部署。它还支持文本转语音（TTS）、BERT 和多模态模型。要开始使用，请阅读他们的逐步[微调 LLM 指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## 作业

选择上述教程之一并完成学习。_我们可能会在本仓库中的 Jupyter 笔记本中复现这些教程的版本，仅供参考。请直接使用原始来源以获取最新版本_。

## 干得好！继续学习吧。

完成本课后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持续提升您的生成式 AI 知识！

祝贺您！！您已完成本课程 v2 系列的最后一课！不要停止学习和构建。**查看[资源](RESOURCES.md?WT.mc_id=academic-105485-koreyst)页面，获取更多本主题的建议列表。

我们的 v1 系列课程也已更新，增加了更多作业和概念。请花点时间复习您的知识——并请[分享您的问题和反馈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，帮助我们为社区改进这些课程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->