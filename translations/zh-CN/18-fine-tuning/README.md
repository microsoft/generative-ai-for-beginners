[![开源模型](../../../translated_images/zh-CN/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微调您的大语言模型

使用大语言模型构建生成式 AI 应用程序带来了新的挑战。一个关键问题是确保模型针对给定用户请求生成的内容的响应质量（准确性和相关性）。在之前的课程中，我们讨论了如提示工程和检索增强生成等技术，这些技术试图通过_修改现有模型的提示输入_来解决此问题。

在今天的课程中，我们将讨论第三种技术，<strong>微调</strong>，它尝试通过_使用额外数据重新训练模型本身_来应对这一挑战。让我们深入了解细节。

## 学习目标

本课程介绍预训练语言模型微调的概念，探讨该方法的优势和挑战，并提供关于何时及如何使用微调来提升生成式 AI 模型性能的指导。

在本课程结束时，您应该能够回答以下问题：

- 什么是语言模型的微调？
- 微调何时有用，为什么有用？
- 我如何微调预训练模型？
- 微调有哪些局限性？

准备好了吗？我们开始吧。

## 图解指南

想先了解我们将要覆盖的大致内容吗？看看这份图解指南，描述了本课程的学习旅程 —— 从学习微调的核心概念和动机，到理解微调过程及执行微调任务的最佳实践。这是一个极具吸引力的探索主题，别忘了查看[资源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)页面，获取更多支持自主学习的链接！

![微调语言模型的图解指南](../../../translated_images/zh-CN/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什么是语言模型的微调？

根据定义，大型语言模型是在大量来自互联网等多样化来源的文本上进行_预训练_的。正如我们在之前的课程中学到的，我们需要像_提示工程_和_检索增强生成_这样的技术来提升模型对用户问题（“提示”）的响应质量。

一种流行的提示工程技术是向模型提供更多关于期望响应内容的指导，或通过提供_指令_（显式指导），或_给出几个示例_（隐式指导）。这被称为_少样本学习_，但它有两个限制：

- 模型的标记数量限制会限制您能给出的示例数量，并限制效果。
- 模型的标记成本会使每个提示添加示例变得昂贵，从而限制灵活性。

微调是机器学习系统中的一种常见做法，我们取一个预训练模型，并用新的数据重新训练它，以提高其在特定任务上的性能。在语言模型的背景下，我们可以用_针对特定任务或应用领域精心挑选的示例集_微调预训练模型，创建一个<strong>定制模型</strong>，这可能更加准确且与该特定任务或领域相关。微调的一个附加好处是，它还能减少少样本学习所需的示例数量 —— 减少标记使用和相关成本。

## 何时以及为何要微调模型？

在_此处_讨论微调时，我们指的是<strong>监督</strong>微调，其通过添加原始训练数据集中没有的新数据来重新训练模型。这不同于在原始数据上但调整超参数的无监督微调方法。

关键点是，微调是一项高级技术，需要一定的专业知识以获得期望的结果。如果操作不当，可能不会带来预期的改进，甚至可能降低模型在您目标领域的表现。

因此，在了解“如何”微调语言模型之前，您需要知道“为什么”要走这条路，以及“何时”开始微调。首先要问自己这些问题：

- <strong>用例</strong>：您微调的_用例_是什么？您想改进当前预训练模型的哪个方面？
- <strong>替代方案</strong>：您是否尝试过_其他技术_来实现预期结果？用它们创建基线进行比较。
  - 提示工程：尝试少样本提示技术，使用相关提示响应示例。评估响应质量。
  - 检索增强生成：尝试通过搜索您的数据来检索查询结果并增强提示。评估响应质量。
- <strong>成本</strong>：您是否确定了微调的成本？
  - 可调性 - 该预训练模型是否支持微调？
  - 努力 - 准备训练数据、评估与优化模型所需的工作量。
  - 计算资源 - 运行微调作业及部署微调模型所需资源。
  - 数据 - 访问到足够质量的示例以影响微调效果。
- <strong>收益</strong>：您是否确认了微调的收益？
  - 质量 - 微调模型是否优于基线模型？
  - 成本 - 是否通过简化提示减少了标记使用？
  - 可扩展性 - 是否可将基础模型用于新领域？

通过回答这些问题，您应该能够决定微调是否适合您的用例。理想情况下，只有当收益大于成本时，方法才有效。一旦决定继续，就该考虑_如何_微调预训练模型了。

想了解更多关于决策过程的见解吗？观看 [微调还是不微调](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 如何微调预训练模型？

要微调预训练模型，您需要：

- 一个待微调的预训练模型
- 一个用于微调的数据集
- 一个可运行微调作业的训练环境
- 一个可部署微调模型的托管环境

## 微调实操

> **注意：** `gpt-35-turbo` / `gpt-3.5-turbo`，在下述某些教程中提及，现已停用用于推理和微调。如果您今天开始新的微调作业，请以当前支持的模型为目标——例如 `gpt-4o-mini` 或 `gpt-4.1-mini`。请参阅[微调模型列表](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)了解当前可微调模型。尽管如此，这些教程中的概念和步骤仍然适用。

以下资源提供了分步教程，引导您使用精选数据集和选定模型完成真实示例。要完成这些教程，您需要拥有特定提供商的账号，并可访问相关模型和数据集。

| 提供商       | 教程                                                                                                                                                                         | 描述                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微调聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                       | 学习如何微调 `gpt-35-turbo` 用于特定领域（“食谱助手”），包括准备训练数据、运行微调作业，并使用微调模型进行推理。                                                                                                                                                                                                                                                                               |
| Azure OpenAI | [GPT 3.5 Turbo 微调教程](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)         | 学习如何在 **Azure** 上微调 `gpt-35-turbo-0613` 模型，包括创建和上传训练数据、运行微调作业，部署和使用新模型。                                                                                                                                                                                                                                                                           |
| Hugging Face | [使用 Hugging Face 微调大语言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                         | 本博客介绍如何使用开源 LLM（例如 `CodeLlama 7B`）及 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 库和 [Transformer 强化学习 (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) 及 Hugging Face 上的开放 [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) 进行微调。 |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                               |
| 🤗 AutoTrain | [使用 AutoTrain 微调大语言模型](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                       | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 开发的 Python 库，支持多种任务的微调，包括 LLM 微调。AutoTrain 是无代码解决方案，微调可在您自己的云端、Hugging Face Spaces 或本地完成。它支持基于网页的 GUI，CLI 以及通过 yaml 配置文件的训练。                                                                                                        |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                               |
| 🦥 Unsloth | [使用 Unsloth 微调大语言模型](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                           | Unsloth 是一个支持 LLM 微调和强化学习（RL）的开源框架。Unsloth 通过现成的 [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) 简化本地训练、评估和部署。它还支持文本转语音（TTS）、BERT 及多模态模型。要开始，请阅读他们的分步[微调 LLM 指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                         |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                               |
## 作业

请选择上述教程之一进行实践。_我们可能会在此仓库的 Jupyter 笔记本中复制这些教程的某个版本供参考。请直接使用原始来源以获取最新版本_。

## 干得好！继续学习。

完成本课程后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

恭喜！！您已完成本课程 v2 系列的最终课！不要停止学习和构建。**请查看[资源](RESOURCES.md?WT.mc_id=academic-105485-koreyst)页面，获取针对本主题的更多建议列表。

我们的 v1 系列课程也已经更新，包含更多作业和概念。花点时间刷新您的知识吧 — 并且请[分享您的问题和反馈](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，帮助我们为社区改进这些课程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->