# 提示工程基础

[![提示工程基础](../../../translated_images/04-lesson-banner.png?WT.d904d510033d5f0283f2caff5f735050f929dd196a1fc25fefa18433347fe463.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## 介绍
本模块涵盖了在生成式AI模型中创建有效提示的基本概念和技术。你如何向LLM编写提示也很重要。精心设计的提示可以获得更高质量的响应。但是，像 _prompt_ 和 _prompt engineering_ 这样的术语到底是什么意思？我如何改进发送给LLM的提示 _input_？这些是我们将在本章和下一章中尝试回答的问题。

_生成式AI_ 能够根据用户请求创建新的内容（例如文本、图像、音频、代码等）。它使用像OpenAI的GPT（"Generative Pre-trained Transformer"）系列这样的 _大型语言模型_ 来实现这些功能，这些模型经过自然语言和代码的训练。

用户现在可以使用熟悉的聊天模式与这些模型进行交互，而无需任何技术专长或培训。这些模型是基于 _提示_ 的 - 用户发送一个文本输入（提示）并获得AI响应（完成）。然后他们可以在多轮对话中与AI进行迭代聊天，优化他们的提示，直到响应符合他们的预期。

“提示”现在成为生成式AI应用的主要 _编程接口_，告诉模型要做什么并影响返回响应的质量。“提示工程”是一个快速发展的研究领域，专注于提示的 _设计和优化_，以大规模提供一致和高质量的响应。

## 学习目标

在本课中，我们将学习什么是提示工程，为什么它很重要，以及如何为给定的模型和应用目标制作更有效的提示。我们将理解提示工程的核心概念和最佳实践，并了解一个互动的Jupyter Notebooks“沙盒”环境，在这里我们可以看到这些概念应用于实际例子。

到本课结束时，我们将能够：

1. 解释什么是提示工程以及为什么它很重要。
2. 描述提示的组成部分及其使用方式。
3. 学习提示工程的最佳实践和技术。
4. 使用OpenAI端点将学到的技术应用于实际示例。

## 关键术语

提示工程：设计和优化输入以引导AI模型生成所需输出的实践。
分词：将文本转换为模型可以理解和处理的更小单位（称为tokens）的过程。
指令调优LLM：经过特定指令微调的大型语言模型（LLM），以提高其响应的准确性和相关性。

## 学习沙盒

提示工程目前更像是一门艺术而不是科学。提高我们直觉的最佳方法是 _多练习_ 并采用试错方法，将应用领域专业知识与推荐技术和模型特定优化相结合。

本课附带的Jupyter Notebook提供了一个 _沙盒_ 环境，您可以在这里尝试学习内容 - 无论是在学习过程中还是在最后的代码挑战中。要执行这些练习，您将需要：

1. **Azure OpenAI API 密钥** - 部署LLM的服务端点。
2. **Python 运行时** - 用于执行Notebook。
3. **本地环境变量** - _完成[SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst)步骤以做好准备_。

Notebook附带 _入门_ 练习 - 但鼓励您添加自己的 _Markdown_（描述）和 _代码_（提示请求）部分，以尝试更多示例或想法 - 并建立您对提示设计的直觉。

## 插图指南

想在深入学习之前了解本课涵盖的内容吗？查看这个插图指南，它为您提供了每个主题的主要内容和关键要点的概述。课程路线图将带您从理解核心概念和挑战开始，使用相关的提示工程技术和最佳实践来解决这些问题。请注意，本指南中的“高级技术”部分涉及本课程下一章的内容。

![提示工程插图指南](../../../translated_images/04-prompt-engineering-sketchnote.png?WT.a936f69bc33c7a783015f6747ea56d0f0071349644cd9031f9b8d20a3eec8696.zh.mc_id=academic-105485-koreyst)

## 我们的创业公司

现在，让我们讨论一下 _这个主题_ 如何与我们的创业使命相关，即[将AI创新带入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)。我们希望构建AI驱动的 _个性化学习_ 应用程序 - 因此，让我们思考一下我们应用程序的不同用户如何“设计”提示：

- **管理员** 可能会要求AI _分析课程数据以识别覆盖中的差距_。AI可以总结结果或使用代码进行可视化。
- **教育者** 可能会要求AI _为目标受众和主题生成课程计划_。AI可以以指定格式构建个性化计划。
- **学生** 可能会要求AI _在困难科目上辅导他们_。AI现在可以为学生提供量身定制的课程、提示和示例。

这只是冰山一角。查看[教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - 由教育专家策划的开源提示库 - 以获得更广泛的可能性！_尝试在沙盒中运行这些提示或使用OpenAI Playground查看会发生什么！_

<!--
课程模板：
本单元应涵盖核心概念#1。
用示例和参考资料加强概念。

概念#1：
提示工程。
定义并解释为什么需要它。
-->

## 什么是提示工程？

我们从定义**提示工程**开始本课，将其描述为 _设计和优化_ 文本输入（提示）的过程，以为给定的应用目标和模型提供一致和高质量的响应（完成）。我们可以将其视为一个两步过程：

- 为给定的模型和目标 _设计_ 初始提示
- 迭代 _优化_ 提示以提高响应质量

这必然是一个需要用户直觉和努力以获得最佳结果的试错过程。那么为什么它很重要呢？要回答这个问题，我们首先需要理解三个概念：

- _分词_ = 模型如何“看待”提示
- _基础LLM_ = 基础模型如何“处理”提示
- _指令调优LLM_ = 模型现在如何看到“任务”

### 分词

LLM将提示视为 _token序列_，不同的模型（或模型版本）可以以不同的方式对同一提示进行分词。由于LLM是基于tokens训练的（而不是原始文本），因此提示的分词方式会直接影响生成响应的质量。

要了解分词如何工作，可以尝试像[OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)这样的工具。复制您的提示 - 看看它如何被转换为tokens，注意空白字符和标点符号的处理方式。请注意，此示例显示的是旧版LLM（GPT-3） - 使用新模型可能会产生不同的结果。

![分词](../../../translated_images/04-tokenizer-example.png?WT.f5399316da400747ffe3af9c95e61dc1a85508d57378da23a77538270c4cabf1.zh.mc_id=academic-105485-koreyst)

### 概念：基础模型

一旦提示被分词，["基础LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)（或基础模型）的主要功能就是预测该序列中的token。由于LLM是在大量文本数据集上训练的，它们对tokens之间的统计关系有很好的理解，并且可以有信心地进行预测。请注意，它们并不理解提示或token中的单词的 _意义_；它们只是看到一个可以通过下一个预测“完成”的模式。它们可以继续预测序列，直到用户干预或某个预先设定的条件终止。

想看看基于提示的完成如何工作？将上述提示输入Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)并使用默认设置。系统配置为将提示视为信息请求 - 因此您应该看到一个满足此上下文的完成。

但是如果用户希望看到符合某些标准或任务目标的特定内容怎么办？这就是 _指令调优_ LLM的作用。

![基础LLM聊天完成](../../../translated_images/04-playground-chat-base.png?WT.7645a03d7989b1c410f2e9e6b503d18e4624f82d9cbf108dac999b8c8988f0ad.zh.mc_id=academic-105485-koreyst)

### 概念：指令调优LLM

[指令调优LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)从基础模型开始，并通过包含明确指令的示例或输入/输出对（例如，多轮“消息”）对其进行微调 - AI的响应尝试遵循该指令。

这使用了诸如带有人类反馈的强化学习（RLHF）等技术，可以训练模型 _遵循指令_ 和 _从反馈中学习_，以便其生成更适合实际应用并更符合用户目标的响应。

让我们试试 - 重新审视上面的提示，但现在更改 _系统消息_ 提供以下指令作为上下文：

> _将您提供的内容总结给二年级学生。将结果保持在一个段落中，包含3-5个要点。_

看看结果现在如何调整以反映所需的目标和格式？教育者现在可以直接在他们的幻灯片中使用此响应为该课程。

![指令调优LLM聊天完成](../../../translated_images/04-playground-chat-instructions.png?WT.d9c80b15e90815a83ce665bf4418e70205d30318a5a5bcf407b2c92769743593.zh.mc_id=academic-105485-koreyst)

## 为什么我们需要提示工程？

既然我们知道提示是如何被LLM处理的，那么让我们讨论一下 _为什么_ 我们需要提示工程。答案在于当前的LLM存在一些挑战，使得 _可靠和一致的完成_ 更难以实现，而不在提示构建和优化上投入精力。例如：

1. **模型响应是随机的。** _相同的提示_ 可能会在不同的模型或模型版本上产生不同的响应。即使在 _相同的模型_ 上，不同时间也可能产生不同的结果。_提示工程技术可以通过提供更好的护栏来帮助我们最小化这些变化_。

1. **模型可能会编造响应。** 模型是通过 _大但有限_ 的数据集预训练的，这意味着它们缺乏关于超出训练范围的概念的知识。因此，它们可能会生成不准确、虚构或直接与已知事实相矛盾的完成。_提示工程技术可以帮助用户识别和减轻此类编造，例如，通过要求AI提供引用或推理_。

1. **模型能力会有所不同。** 新的模型或模型代可能具有更丰富的能力，但也带来了成本和复杂性方面的独特特性和权衡。_提示工程可以帮助我们开发最佳实践和工作流程，以抽象出差异并适应模型特定的需求，以可扩展、无缝的方式_。

让我们在OpenAI或Azure OpenAI Playground中看到这些在行动中：

- 使用相同的提示与不同的LLM部署（例如，OpenAI，Azure OpenAI，Hugging Face） - 你看到变化了吗？
- 使用相同的提示在 _相同的_ LLM部署中重复使用（例如，Azure OpenAI playground） - 这些变化有何不同？

### 编造示例

在本课程中，我们使用术语**“编造”**来指代由于训练限制或其他约束，LLM有时会生成不正确信息的现象。您可能还在流行文章或研究论文中听说过这种现象被称为 _“幻觉”_。然而，我们强烈建议使用 _“编造”_ 作为术语，以避免将人类特质错误地归因于机器驱动的结果。这也从术语角度加强了[负责任AI指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除了在某些情况下可能被认为具有冒犯性或不包容性的术语。

想了解编造如何工作吗？想一个提示，指示AI为不存在的主题生成内容（以确保它不在训练数据集中）。例如 - 我尝试了这个提示：

> **提示：** 为2076年的火星战争生成课程计划。

网络搜索显示存在关于火星战争的虚构叙述（例如，电视系列或书籍） - 但没有关于2076年的。常识也告诉我们，2076年是 _未来_，因此不能与真实事件相关联。

那么，当我们与不同的LLM提供商运行此提示时会发生什么？

> **响应1**：OpenAI Playground (GPT-35)

![响应1](../../../translated_images/04-fabrication-oai.png?WT.08cc3e01259a6b46725a800e67de50c37b7fdd6b1f932f027881cbe32f80bcf1.zh.mc_id=academic-105485-koreyst)

> **响应2**：Azure OpenAI Playground (GPT-35)

![响应2](../../../translated_images/04-fabrication-aoai.png?WT.81e0d286a351c87c804aaca6e5f8251a6deed5105d11bca035f8cead8c52d299.zh.mc_id=academic-105485-koreyst)

> **响应3**：Hugging Face Chat Playground (LLama-2)

![响应3](../../../translated_images/04-fabrication-huggingchat.png?WT.992b3a675cc7ed0dbe53e308b93df8165048fb7c4516e6bb00611d05c92e8fd5.zh.mc_id=academic-105485-koreyst)

正如预期的那样，由于随机行为和模型能力的变化，每个模型（或模型版本）产生了略有不同的响应。例如，一个模型针对8年级受众，而另一个假定是高中生。但所有三个模型都生成了可能会让不知情用户相信事件是真实的响应。

提示工程技术如 _元提示_ 和 _温度配置_ 可以在一定程度上减少模型编造。新的提示工程 _架构_ 还将新工具和技术无缝集成到提示流中，以减轻或减少其中的一些效果。

## 案例研究：GitHub Copilot

让我们通过查看一个案例研究来结束这一部分： [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot是您的“AI配对程序员” - 它将文本提示转换为代码完成，并集成到您的开发环境中（例如，Visual Studio Code），以提供无缝的用户体验。如以下系列博客中所述，最早的版本基于OpenAI Codex模型 - 工程师们很快意识到需要微调模型并开发更好的提示工程技术，以提高代码质量。在7月，他们[推出了一个改进的AI模型，超越了Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，以提供更快的建议。

按顺序阅读这些文章，跟随他们的学习之旅。

- **2023年5月** | [GitHub Copilot在理解您的代码方面越来越好](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub内部：与GitHub Copilot背后的LLM合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年6月** | [如何为GitHub Copilot编写更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年7月** | [.. GitHub Copilot超越Codex，推出改进的AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [开发者的提示工程和LLM指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何构建企业级LLM应用：来自GitHub Copilot的经验](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

您还可以浏览他们的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)以获取更多类似[这篇文章](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)的帖子，展示这些模型和技术如何用于推动现实世界的应用。

---

<!--
课程模板：
本单元应涵盖核心概念#2。
用示例和参考资料加强概念。

概念#2：
提示设计。
用示例说明。
-->

## 提示构建

我们已经了解了为什么提示工程很重要 - 现在让我们了解提示是如何 _构建_ 的，以便我们可以评估不同的技术以实现更有效的提示设计。

### 基本提示

让我们从基本提示开始：发送给模型的文本输入，没有其他上下文。这里有一个例子 - 当我们将美国国歌的前几句话发送到OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)时，它立即 _完成_ 响应，显示基本的预测行为。

| 提示（输入）     | 完成（输出）                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| 哦说你能看到吗 |
最终，模板的真正价值在于能够为垂直应用领域创建和发布_提示库_——在这里，提示模板经过_优化_以反映特定应用的上下文或示例，使响应对目标用户群体更相关和准确。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 仓库就是这种方法的一个很好的例子，它为教育领域策划了一个提示库，重点放在课程计划、课程设计、学生辅导等关键目标上。

## 支持内容

如果我们将提示构建视为具有指令（任务）和目标（主要内容），那么_次要内容_就像是我们提供的额外上下文，以某种方式**影响输出**。这可能是调整参数、格式化指令、主题分类等，帮助模型_定制_其响应以适应所需的用户目标或期望。

例如：给定一个课程目录，其中包含所有课程的广泛元数据（名称、描述、级别、元数据标签、讲师等）：

- 我们可以定义一个指令来“总结 2023 年秋季的课程目录”
- 我们可以使用主要内容提供一些所需输出的示例
- 我们可以使用次要内容来识别感兴趣的前 5 个“标签”。

现在，模型可以以几个示例所示的格式提供摘要——但如果结果有多个标签，它可以优先考虑次要内容中识别的 5 个标签。

---

<!--
课程模板：
本单元应涵盖核心概念#1。
通过示例和参考资料加强概念。

概念#3：
提示工程技术。
提示工程的一些基本技术是什么？
用一些练习来说明。
-->

## 提示最佳实践

现在我们知道如何_构建_提示，我们可以开始思考如何_设计_它们以反映最佳实践。我们可以将其分为两部分——拥有正确的_心态_和应用正确的_技术_。

### 提示工程心态

提示工程是一个试错过程，因此请牢记三个广泛的指导因素：

1. **领域理解很重要。** 响应的准确性和相关性取决于应用程序或用户所处的_领域_。运用你的直觉和领域专业知识来进一步**定制技术**。例如，在系统提示中定义_领域特定的个性_，或在用户提示中使用_领域特定的模板_。提供反映领域特定上下文的次要内容，或使用_领域特定的提示和示例_来引导模型朝着熟悉的使用模式发展。

2. **模型理解很重要。** 我们知道模型本质上是随机的。但是，模型实现可能会因其使用的训练数据集（预训练知识）、它们提供的功能（例如，通过 API 或 SDK）以及它们针对的内容类型（例如代码、图像、文本）而有所不同。了解你所使用模型的优缺点，并利用这些知识来_优先排序任务_或构建_定制模板_，以优化模型的功能。

3. **迭代和验证很重要。** 模型正在快速发展，提示工程技术也是如此。作为领域专家，你可能有其他上下文或标准适用于_你的_特定应用，而不适用于更广泛的社区。使用提示工程工具和技术来“快速启动”提示构建，然后使用你的直觉和领域专业知识迭代和验证结果。记录你的见解并创建一个**知识库**（例如，提示库），以便其他人可以在未来更快地迭代。

## 最佳实践

现在让我们看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) 和 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) 从业者推荐的常见最佳实践。

| 内容                             | 原因                                                                                                                                                                                                                                               |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 评估最新模型。                   | 新一代模型可能具有改进的功能和质量——但也可能会产生更高的成本。评估它们的影响，然后做出迁移决策。                                                                                                                                                |
| 分开指令和上下文                 | 检查你的模型/提供者是否定义了_分隔符_以更清楚地区分指令、主要和次要内容。这可以帮助模型更准确地分配权重给令牌。                                                                                                                         |
| 具体且清晰                       | 提供更多关于所需上下文、结果、长度、格式、风格等的细节。这将提高响应的质量和一致性。将方案捕捉到可重用的模板中。                                                                                                                          |
| 描述性，使用示例                 | 模型可能更好地响应“展示和讲述”的方法。以 `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` 值开始。返回到 [学习沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) 学习如何操作。

### 接下来，打开 Jupyter Notebook

- 选择运行时内核。如果使用选项 1 或 2，只需选择开发容器提供的默认 Python 3.10.x 内核。

你已经准备好运行练习了。请注意，这里没有_对错_的答案——只是通过试错探索选项，并为给定模型和应用领域建立直觉。

_因此，本课中没有代码解决方案部分。相反，Notebook 将有名为“我的解决方案”的 Markdown 单元格，显示一个参考输出示例。_

 <!--
课程模板：
用总结和自学资源包裹章节。
-->

## 知识检查

以下哪项是遵循合理最佳实践的良好提示？

1. 给我看一辆红色汽车的图片
2. 给我看一辆红色沃尔沃 XC90 型号汽车停在悬崖边，夕阳西下的图片
3. 给我看一辆红色沃尔沃 XC90 型号汽车的图片

A: 2，这是最好的提示，因为它提供了“什么”的细节并且进入了具体（不仅仅是任何汽车，而是一个特定的品牌和型号），同时也描述了整体环境。3 是次佳，因为它也包含了很多描述。

## 🚀 挑战

看看你能否利用“提示”技术来完成以下提示：“给我看一辆红色沃尔沃汽车的图片，并且 ”。它如何响应，以及你将如何改进它？

## 出色的工作！继续你的学习

想了解更多关于不同提示工程概念的信息吗？请访问[继续学习页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以找到关于此主题的其他优秀资源。

前往第 5 课，我们将探讨[高级提示技术](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：  
本文件是使用机器翻译服务翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担责任。