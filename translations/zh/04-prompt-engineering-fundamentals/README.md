<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T11:58:18+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "zh"
}
-->
# 提示工程基础

## 简介

本模块涵盖了在生成式 AI 模型中创建有效提示的基本概念和技术。编写提示给大型语言模型（LLM）的方式也很重要。精心设计的提示可以获得更高质量的响应。那么，像 _prompt_ 和 _prompt engineering_ 这样的术语究竟是什么意思呢？我如何改进发送给 LLM 的提示 _输入_？这些是我们将在本章及下一章中尝试回答的问题。

_生成式 AI_ 能够根据用户请求创建新的内容（例如文本、图像、音频、代码等）。它通过使用像 OpenAI 的 GPT 系列（"Generative Pre-trained Transformer"）这样的 _大型语言模型_ 来实现，这些模型经过训练可以使用自然语言和代码。

用户现在可以使用熟悉的范式（如聊天）与这些模型进行交互，而无需任何技术专长或培训。模型是基于 _提示_ 的——用户发送文本输入（提示）并获得 AI 的响应（完成）。他们可以在多轮对话中迭代地“与 AI 聊天”，不断完善他们的提示，直到响应符合他们的期望。

“提示”现在成为生成式 AI 应用程序的主要 _编程接口_，告诉模型该做什么，并影响返回响应的质量。“提示工程”是一个快速发展的研究领域，专注于提示的 _设计和优化_，以大规模地提供一致和高质量的响应。

## 学习目标

在本课中，我们将学习什么是提示工程、为什么它很重要，以及如何为给定模型和应用目标制作更有效的提示。我们将了解提示工程的核心概念和最佳实践——并了解一个交互式 Jupyter Notebooks “沙盒”环境，在那里我们可以看到这些概念应用于真实示例。

到本课结束时，我们将能够：

1. 解释什么是提示工程以及它的重要性。
2. 描述提示的组成部分及其使用方式。
3. 学习提示工程的最佳实践和技术。
4. 将学到的技术应用于真实示例，使用 OpenAI 端点。

## 关键术语

提示工程：设计和优化输入以引导 AI 模型生成期望输出的实践。
分词：将文本转换为模型可以理解和处理的更小单位（称为令牌）的过程。
指令调优 LLMs：通过特定指令进行微调以提高响应准确性和相关性的模型。

## 学习沙盒

提示工程目前更多是一门艺术而非科学。提高我们对其直觉的最佳方法是 _多加练习_，并采用一种结合应用领域专长与推荐技术和特定模型优化的试错方法。

本课附带的 Jupyter Notebook 提供了一个 _沙盒_ 环境，您可以在学习过程中或在代码挑战的结尾尝试所学内容。要执行练习，您需要：

1. **Azure OpenAI API 密钥** - 部署的 LLM 的服务端点。
2. **Python 运行时** - 执行 Notebook。
3. **本地环境变量** - _现在完成 [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) 步骤以准备好_。

Notebook 附带 _入门_ 练习 - 但鼓励您添加自己的 _Markdown_（描述）和 _Code_（提示请求）部分，以尝试更多示例或想法 - 并建立您对提示设计的直觉。

## 插图指南

想在深入学习之前了解本课涵盖的内容的大致情况吗？查看此插图指南，它让您了解所涵盖的主要主题以及每个主题中需要思考的关键要点。课程路线图将引导您从理解核心概念和挑战开始，通过相关的提示工程技术和最佳实践来解决这些问题。请注意，本指南中的“高级技术”部分涉及本课程的 _下一_ 章内容。

## 我们的创业公司

现在，让我们讨论一下 _这个主题_ 如何与我们将 AI 创新带入教育的创业使命相关。我们希望构建 AI 驱动的 _个性化学习_ 应用程序 - 因此让我们考虑一下我们应用程序的不同用户如何“设计”提示：

- **管理员** 可能会要求 AI _分析课程数据以识别覆盖范围的差距_。AI 可以总结结果或用代码将其可视化。
- **教育工作者** 可能会要求 AI _为目标受众和主题生成课程计划_。AI 可以以指定格式构建个性化计划。
- **学生** 可能会要求 AI _在困难的科目上辅导他们_。AI 现在可以根据他们的水平为学生提供课程、提示和示例。

这只是冰山一角。查看 [教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - 由教育专家策划的开源提示库 - 以获得更广泛的可能性！_尝试在沙盒中运行这些提示或使用 OpenAI Playground 看看会发生什么！_

## 什么是提示工程？

我们从定义 **提示工程** 作为 _设计和优化_ 文本输入（提示）的过程开始，以便为给定的应用目标和模型提供一致和高质量的响应（完成）。我们可以将其视为一个两步过程：

- 为给定模型和目标 _设计_ 初始提示
- 迭代 _改进_ 提示以提高响应质量

这是一个必然的试错过程，需要用户的直觉和努力以获得最佳结果。那么为什么它很重要？要回答这个问题，我们首先需要了解三个概念：

- _分词_ = 模型如何“看到”提示
- _基础 LLMs_ = 基础模型如何“处理”提示
- _指令调优 LLMs_ = 模型如何现在可以看到“任务”

### 分词

LLM 将提示视为 _令牌序列_，不同的模型（或模型版本）可以以不同的方式对同一提示进行分词。由于 LLMs 是在令牌上训练的（而不是在原始文本上），因此提示的分词方式对生成响应的质量有直接影响。

要了解分词的工作原理，请尝试使用 [OpenAI 分词器](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) 等工具。复制您的提示 - 看看它如何转换为令牌，注意空白字符和标点符号的处理方式。请注意，此示例显示的是旧版本的 LLM（GPT-3） - 因此尝试使用较新模型可能会产生不同的结果。

### 概念：基础模型

一旦提示被分词，“基础 LLM” 的主要功能是预测该序列中的令牌。由于 LLMs 是在大量文本数据集上训练的，它们对令牌之间的统计关系有很好的理解，并且可以有信心地进行预测。请注意，它们并不理解提示或令牌中的单词的 _含义_；它们只看到一个可以通过下一个预测“完成”的模式。它们可以继续预测序列，直到用户干预或某些预先设定的条件终止。

想看看基于提示的完成是如何工作的？将上面的提示输入 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) 中，使用默认设置。系统配置为将提示视为信息请求 - 因此您应该看到满足此上下文的完成。

但如果用户希望看到满足某些标准或任务目标的特定内容呢？这就是 _指令调优_ LLMs 的作用。

### 概念：指令调优 LLMs

[指令调优 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) 从基础模型开始，并通过包含明确指令的示例或输入/输出对（例如，多轮“消息”）对其进行微调 - AI 的响应尝试遵循该指令。

这使用了人类反馈的强化学习（RLHF）等技术，可以训练模型 _遵循指令_ 并 _从反馈中学习_，以便生成更适合实际应用并更符合用户目标的响应。

让我们试试 - 重新审视上面的提示，但现在更改 _系统消息_，提供以下指令作为上下文：

> _将您提供的内容总结为二年级学生。结果保持在一个段落内，包含3-5个要点。_

看看结果现在如何调整以反映期望的目标和格式？教育工作者现在可以直接在他们的幻灯片中使用此响应。

## 为什么我们需要提示工程？

现在我们知道 LLMs 如何处理提示，让我们来谈谈 _为什么_ 我们需要提示工程。答案在于当前的 LLMs 存在一些挑战，这使得在不对提示构建和优化投入努力的情况下，实现 _可靠和一致的完成_ 更具挑战性。例如：

1. **模型响应是随机的。** _相同的提示_ 可能会在不同的模型或模型版本中产生不同的响应。甚至可能在 _相同的模型_ 上产生不同的结果。_提示工程技术可以通过提供更好的护栏来帮助我们最小化这些变化_。

2. **模型可能会编造响应。** 模型是通过 _大但有限_ 的数据集进行预训练的，这意味着它们缺乏关于超出训练范围的概念的知识。因此，它们可能会生成不准确、虚构或直接与已知事实相矛盾的完成。_提示工程技术帮助用户识别和减轻这些虚构内容，例如，要求 AI 提供引用或推理_。

3. **模型能力会有所不同。** 较新的模型或模型代将具有更丰富的功能，但也带来成本和复杂性方面的独特怪癖和权衡。_提示工程可以帮助我们开发最佳实践和工作流，以抽象掉差异并以可扩展、无缝的方式适应特定模型的要求_。

让我们在 OpenAI 或 Azure OpenAI Playground 中看看这一点：

- 在不同的 LLM 部署（例如，OpenAI、Azure OpenAI、Hugging Face）中使用相同的提示 - 您看到变化了吗？
- 使用 _相同_ 的 LLM 部署（例如，Azure OpenAI Playground）反复使用相同的提示 - 这些变化有何不同？

### 虚构示例

在本课程中，我们使用术语 **“虚构”** 来引用 LLMs 有时会由于训练或其他限制而生成事实不正确的信息的现象。您可能还在流行文章或研究论文中听说过这被称为 _“幻觉”_。然而，我们强烈建议使用 _“虚构”_ 作为术语，以免通过将人类特征归因于机器驱动的结果而无意中将行为拟人化。这也从术语角度强化了 [负责任的 AI 指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，消除在某些情况下可能被认为是冒犯或不包容的术语。

想了解虚构是如何工作的？想一个提示，指示 AI 为一个不存在的主题生成内容（以确保它不在训练数据集中）。例如 - 我尝试了这个提示：

> **提示：** 生成关于 2076 年火星战争的课程计划。

网络搜索显示有关于火星战争的虚构作品（例如，电视连续剧或书籍） - 但没有 2076 年的。常识也告诉我们，2076 年是 _未来_，因此不能与真实事件相关联。

那么，当我们在不同的 LLM 提供商中运行此提示时会发生什么？

> **响应 1**：OpenAI Playground (GPT-35)

> **响应 2**：Azure OpenAI Playground (GPT-35)

> **响应 3**：Hugging Face Chat Playground (LLama-2)

如预期的那样，由于随机行为和模型能力的差异，每个模型（或模型版本）产生略有不同的响应。例如，一个模型针对八年级学生，而另一个假设是高中生。但所有三个模型都生成了可能会让不知情用户相信事件是真实的响应。

提示工程技术如 _元提示_ 和 _温度配置_ 可以在某种程度上减少模型虚构。新的提示工程 _架构_ 也将新的工具和技术无缝集成到提示流程中，以减轻或减少其中的一些影响。

## 案例研究：GitHub Copilot

让我们通过查看一个案例研究来了解提示工程在现实世界解决方案中的应用：[GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot 是您的“AI 配对程序员” - 它将文本提示转换为代码完成，并集成到您的开发环境（例如，Visual Studio Code）中，以提供无缝的用户体验。正如以下系列博客中所记录的，最早的版本基于 OpenAI Codex 模型 - 工程师很快意识到需要对模型进行微调并开发更好的提示工程技术，以提高代码质量。在 7 月，他们 [推出了一种改进的 AI 模型，不仅仅是 Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)，以获得更快的建议。

按顺序阅读帖子，以了解他们的学习历程。

- **2023年5月** | [GitHub Copilot 正在变得更好地理解您的代码](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [GitHub 内部：与 GitHub Copilot 背后的 LLMs 合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年6月** | [如何为 GitHub Copilot 编写更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年7月** | [.. GitHub Copilot 通过改进的 AI 模型超越 Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [开发人员的提示工程和 LLMs 指南](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何构建企业级 LLM 应用程序：GitHub Copilot 的经验教训](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

您还可以浏览他们的 [工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)，了解更多类似 [这个](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) 的帖子，展示这些模型和技术如何 _应用_ 于推动现实世界的应用程序。

## 提示构建

我们已经了解了为什么提示工程很重要 - 现在让我们了解提示是如何 _构建_ 的，以便我们可以评估不同的技术以设计更有效的提示。

### 基本提示

让我们从基本提示开始：发送给模型的文本输入，没有其他上下文。这里有一个例子 - 当我们将美国国歌的前几句话发送到 OpenAI [完成 API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) 时，它会立即用接下来的几行 _完成_ 响应，说明了基本的预测行为。

### 复杂提示

现在让我们在基本提示中添加上下文和指令。使用 [聊天完成 API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst)，我们可以将复杂提示构建为 _消息_ 集合，其中包括：

- 反映 _用户_ 输入和 _助手_ 响应的输入/输出对。
- 设置助手行为或个性上下文的系统消息。

请求现在如下所示，其中 _分词_ 有效地捕获了上下文和对话中的相关信息。现在，更改系统上下文对完成质量的影响可能与提供的用户输入一样大。

### 指令提示

在上面的示例中，用户提示是一个简单的文本查询，可以解释为信息请求。使用 _指令_ 提示，我们可以使用文本更详细地指定任务，为 AI 提供更好的指导。以下是一个示例：

| 提示（输入）                                                                                                                                                                                                                         | 完成（输出）                                                                                                        | 指令类型    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| 写一段关于内战的描述                                                                                                                                                                                                   | _返回一个简单的段落_                                                                                              | 简单              |
| 写一段关于内战的描述。提供关键日期和事件并描述其重要性                                                                                                                                     | _返回一个段落，后面是关键事件日期及描述的列表_                                             | 复杂             |
| 写一段关于内战的描述，限制在1个段落内。提供3个要点，包含关键日期及其重要性。再提供3个要点，包含关键历史人物及其贡献
模板的真正价值在于能够为垂直应用领域创建和发布_提示库_——在这里，提示模板经过_优化_以反映特定应用的上下文或示例，从而使响应对目标用户群体更相关和准确。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 仓库就是这种方法的一个很好的例子，它为教育领域策划了一个提示库，重点放在课程规划、课程设计、学生辅导等关键目标上。

## 支持内容

如果我们将提示构建视为具有指令（任务）和目标（主要内容），那么_次要内容_就像是我们提供的额外上下文，以某种方式**影响输出**。它可以是调优参数、格式化指令、主题分类等，可以帮助模型_定制_其响应以符合所需的用户目标或期望。

例如：给定一个课程目录，其中包含关于课程的丰富元数据（名称、描述、级别、元数据标签、讲师等）：

- 我们可以定义一个指令来“总结2023年秋季课程目录”
- 我们可以使用主要内容提供一些期望输出的示例
- 我们可以使用次要内容来识别感兴趣的前5个“标签”。

现在，模型可以按照少数示例中展示的格式提供总结——但如果结果有多个标签，它可以优先考虑次要内容中识别的5个标签。

---

<!--
课程模板：
本单元应涵盖核心概念#1。
用示例和参考资料强化这一概念。

概念#3：
提示工程技术。
提示工程有哪些基本技术？
通过一些练习来说明。
-->

## 提示的最佳实践

现在我们知道如何_构建_提示，我们可以开始考虑如何_设计_它们以反映最佳实践。我们可以将其分为两个部分——拥有正确的_心态_和应用正确的_技术_。

### 提示工程心态

提示工程是一个反复试验的过程，因此请牢记三个广泛的指导因素：

1. **领域理解很重要。** 响应的准确性和相关性取决于应用或用户所处的_领域_。运用你的直觉和领域专业知识来**进一步定制技术**。例如，在系统提示中定义_领域特定的人格_，或在用户提示中使用_领域特定的模板_。提供反映领域特定上下文的次要内容，或使用_领域特定的线索和示例_来引导模型朝着熟悉的使用模式。

2. **模型理解很重要。** 我们知道模型本质上是随机的。但模型的实现也可能因其使用的训练数据集（预训练知识）、所提供的能力（例如，通过API或SDK）以及优化的内容类型（例如，代码与图像与文本）而异。了解你所使用模型的优势和局限性，并利用这些知识来_优先处理任务_或构建_定制模板_，以优化模型的能力。

3. **迭代和验证很重要。** 模型正在快速发展，提示工程的技术也是如此。作为领域专家，你可能有其他上下文或标准适用于_你的_特定应用，而不适用于更广泛的社区。使用提示工程工具和技术来“快速启动”提示构建，然后使用你的直觉和领域专业知识迭代并验证结果。记录你的见解并创建一个**知识库**（例如，提示库），以便其他人可以用作新基准，从而在未来更快地迭代。

## 最佳实践

现在让我们看看 [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) 和 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) 从业者推荐的常见最佳实践。

| 内容                               | 原因                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 评估最新模型。                   | 新一代模型可能具有改进的功能和质量——但也可能带来更高的成本。评估它们的影响，然后做出迁移决策。                                                                                                                                                |
| 分开指令和上下文                  | 检查你的模型/提供商是否定义了_分隔符_以更清楚地区分指令、主要和次要内容。这可以帮助模型更准确地分配权重给标记。                                                                                                                         |
| 具体且清晰                        | 提供有关期望的上下文、结果、长度、格式、风格等的更多细节。这将提高响应的质量和一致性。将配方捕获在可重用的模板中。                                                                                                                          |
| 具有描述性，使用示例              | 模型可能对“展示与讲解”方法反应更好。开始时使用 `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` 值。返回到[学习沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)以了解如何操作。

### 接下来，打开 Jupyter Notebook

- 选择运行时内核。如果使用选项1或2，只需选择开发容器提供的默认 Python 3.10.x 内核。

你已经准备好运行练习。请注意，这里没有_对错_之分——只是通过反复试验探索选项并建立直觉，了解哪个适用于给定的模型和应用领域。

_因此，本课程中没有代码解决方案部分。相反，Notebook 将有标题为“我的解决方案：”的 Markdown 单元格，显示一个示例输出以供参考。_

 <!--
课程模板：
用总结和自学资源来结束本节。
-->

## 知识检查

以下哪个是遵循合理最佳实践的良好提示？

1. 给我看一辆红色汽车的图片
2. 给我看一辆红色沃尔沃XC90车型的汽车，停在悬崖边，太阳正在落下
3. 给我看一辆红色沃尔沃XC90车型的汽车

A: 2，它是最好的提示，因为它提供了“什么”的细节，并深入到具体（不仅仅是任何汽车，而是特定的品牌和型号），并且还描述了整体环境。3是次佳，因为它也包含了很多描述。

## 🚀 挑战

看看你是否可以利用“线索”技术来完成提示：“完成句子‘给我看一辆红色沃尔沃车型的汽车，并’。”它会如何响应，你会如何改进它？

## 干得好！继续你的学习

想了解更多不同的提示工程概念吗？访问[继续学习页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，寻找有关此主题的其他优秀资源。

前往第5课，我们将学习[高级提示技术](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：
本文档是使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译的。尽管我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。