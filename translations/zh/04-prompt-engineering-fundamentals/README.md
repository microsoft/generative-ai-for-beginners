<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:47:11+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "zh"
}
-->
# 提示工程基础

## 介绍

本模块涵盖了为生成式AI模型创建有效提示的基本概念和技术。编写提示的方式对大型语言模型（LLM）也很重要。精心设计的提示可以获得更高质量的响应。那么，像 _提示_ 和 _提示工程_ 这样的术语究竟是什么意思？我该如何改进发送给LLM的提示 _输入_ 呢？这些是我们将在本章和下一章中试图回答的问题。

_生成式AI_ 能够根据用户请求创建新内容（例如，文本、图像、音频、代码等）。它使用类似于OpenAI的GPT（"生成预训练变换器"）系列的大型语言模型，通过自然语言和代码进行训练。

用户现在可以使用聊天等熟悉的方式与这些模型进行交互，而无需任何技术专长或培训。这些模型是 _基于提示_ 的——用户发送文本输入（提示）并获得AI响应（完成）。他们可以在多轮对话中迭代地与AI聊天，逐步调整提示，直到响应符合他们的期望。

“提示”现在成为生成式AI应用程序的主要 _编程接口_，告诉模型要做什么，并影响返回响应的质量。“提示工程”是一个快速发展的研究领域，专注于提示的 _设计和优化_，以大规模提供一致和高质量的响应。

## 学习目标

在本课中，我们将学习什么是提示工程、它的重要性，以及如何为特定模型和应用目标制作更有效的提示。我们将了解提示工程的核心概念和最佳实践——并了解一个交互式Jupyter Notebooks "沙盒" 环境，在那里我们可以看到这些概念应用于实际示例。

到本课结束时，我们将能够：

1. 解释什么是提示工程及其重要性。
2. 描述提示的组成部分及其使用方式。
3. 学习提示工程的最佳实践和技术。
4. 将所学技术应用于实际示例，使用OpenAI端点。

## 关键术语

提示工程：设计和优化输入以指导AI模型生成期望输出的实践。
标记化：将文本转换为模型可以理解和处理的小单位（称为标记）的过程。
指令调优的LLM：经过特定指令微调以提高响应准确性和相关性的大型语言模型（LLM）。

## 学习沙盒

提示工程目前更像是一门艺术而非科学。提高直觉的最佳方法是 _多加练习_，并采用结合应用领域专业知识与推荐技术和模型特定优化的试错方法。

本课附带的Jupyter Notebook提供了一个 _沙盒_ 环境，您可以在其中尝试所学内容——无论是随时进行还是作为最后代码挑战的一部分。要执行练习，您将需要：

1. **一个Azure OpenAI API密钥** - 部署LLM的服务端点。
2. **一个Python运行时** - 在其中可以执行Notebook。
3. **本地环境变量** - _现在完成[设置](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst)步骤以做好准备_。

该Notebook附带 _入门_ 练习——但鼓励您添加自己的 _Markdown_（描述）和 _代码_（提示请求）部分，以尝试更多示例或想法——并建立对提示设计的直觉。

## 图解指南

想在深入学习之前了解本课涵盖的内容吗？查看这个图解指南，它可以让您了解涵盖的主要主题以及每个主题需要考虑的关键要点。课程路线图将带您从理解核心概念和挑战到使用相关提示工程技术和最佳实践解决这些问题。请注意，本指南中的“高级技术”部分指的是本课程下一章中涵盖的内容。

## 我们的创业公司

现在，让我们谈谈 _这个主题_ 如何与我们创业使命相关，即[将AI创新带入教育](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)。我们希望构建AI驱动的 _个性化学习_ 应用程序——所以让我们思考一下我们应用程序的不同用户如何“设计”提示：

- **管理员**可能会要求AI _分析课程数据以识别覆盖中的差距_。AI可以总结结果或用代码可视化它们。
- **教育者**可能会要求AI _为目标受众和主题生成课程计划_。AI可以以指定格式构建个性化计划。
- **学生**可能会要求AI _辅导他们解决困难科目_。AI现在可以根据他们的水平为学生提供量身定制的课程、提示和示例。

这只是冰山一角。查看[教育提示](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)——一个由教育专家策划的开源提示库——以获得更广泛的可能性！_尝试在沙盒中运行其中一些提示或使用OpenAI Playground看看会发生什么！_

## 什么是提示工程？

我们从定义**提示工程**开始本课，即为给定应用目标和模型 _设计和优化_ 文本输入（提示）以提供一致和高质量响应（完成）的过程。我们可以将其视为一个两步过程：

- 为给定模型和目标 _设计_ 初始提示
- 迭代地 _优化_ 提示以提高响应质量

这必然是一个需要用户直觉和努力才能获得最佳结果的试错过程。那么为什么它很重要？要回答这个问题，我们首先需要了解三个概念：

- _标记化_ = 模型如何“看到”提示
- _基础LLM_ = 基础模型如何“处理”提示
- _指令调优的LLM_ = 模型如何现在可以看到“任务”

### 标记化

LLM将提示视为 _标记序列_，不同模型（或模型版本）可以以不同方式标记相同提示。由于LLM是基于标记（而不是原始文本）进行训练的，因此提示的标记化方式直接影响生成响应的质量。

要了解标记化的工作原理，请尝试使用下面显示的[OpenAI标记化工具](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)。复制您的提示——看看它是如何转换为标记的，注意空白字符和标点符号的处理方式。请注意，此示例显示的是较旧的LLM（GPT-3）——因此尝试使用较新的模型可能会产生不同的结果。

### 概念：基础模型

一旦提示被标记化，["基础LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)（或基础模型）的主要功能就是预测序列中的标记。由于LLM在大量文本数据集上进行了训练，它们对标记之间的统计关系有很好的了解，并可以有信心地进行预测。请注意，它们并不理解提示或标记中的单词 _含义_；它们只是看到一个可以通过下一个预测“完成”的模式。它们可以继续预测序列，直到被用户干预或某个预设条件终止。

想看看基于提示的完成是如何工作的？将上述提示输入Azure OpenAI Studio的[_聊天游乐场_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)并使用默认设置。系统被配置为将提示视为信息请求——因此您应该看到一个满足此上下文的完成。

但如果用户想要看到符合某些标准或任务目标的特定内容怎么办？这就是 _指令调优_ 的LLM的用武之地。

### 概念：指令调优的LLM

一个[指令调优的LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)从基础模型开始，并通过示例或输入/输出对（例如，多轮“消息”）进行微调，这些对可以包含明确的指令——AI尝试遵循这些指令的响应。

这使用了诸如人类反馈强化学习（RLHF）等技术，可以训练模型 _遵循指令_ 并 _从反馈中学习_，以便生成更适合实际应用并更符合用户目标的响应。

让我们试试看——重新审视上面的提示，但现在更改 _系统消息_，提供以下指令作为上下文：

> _将您提供的内容总结为二年级学生。将结果保持在一段中，包含3-5个要点。_

看看结果如何现在被调优以反映期望的目标和格式？教育者现在可以直接在他们的幻灯片中使用此响应。

## 为什么我们需要提示工程？

现在我们知道LLM如何处理提示，让我们来谈谈 _为什么_ 我们需要提示工程。答案在于当前的LLM存在许多挑战，使得在不投入提示构建和优化的情况下实现 _可靠和一致的完成_ 更具挑战性。例如：

1. **模型响应是随机的。** _相同的提示_ 可能会在不同的模型或模型版本上产生不同的响应。甚至在 _相同模型_ 上的不同时间也可能产生不同的结果。_提示工程技术可以帮助我们通过提供更好的防护措施来最大限度地减少这些变化_。

2. **模型可能会捏造响应。** 模型是用 _大但有限_ 的数据集进行预训练的，这意味着它们缺乏关于超出训练范围的概念的知识。因此，它们可能会生成不准确、虚构或直接与已知事实相矛盾的完成。_提示工程技术帮助用户识别和减轻这些捏造，例如，通过要求AI提供引用或推理_。

3. **模型能力会有所不同。** 较新的模型或模型代将具有更丰富的功能，但也带来了成本和复杂性方面的独特怪癖和权衡。_提示工程可以帮助我们开发最佳实践和工作流程，以抽象掉差异并以可扩展、无缝的方式适应模型特定要求_。

让我们在OpenAI或Azure OpenAI Playground中看到这一点：

- 使用不同的LLM部署（例如，OpenAI、Azure OpenAI、Hugging Face）使用相同的提示——您是否看到了变化？
- 在 _相同_ 的LLM部署（例如，Azure OpenAI playground）上重复使用相同的提示——这些变化有何不同？

### 捏造示例

在本课程中，我们使用术语 **“捏造”** 来指代LLM由于训练限制或其他限制有时生成事实不正确的信息的现象。您可能也在流行文章或研究论文中听到过称为 _“幻觉”_ 的说法。然而，我们强烈建议使用 _“捏造”_ 作为术语，以免通过将人类特征归因于机器驱动的结果而无意中将行为拟人化。这也从术语角度加强了[负责任AI指南](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)，去除了可能在某些情况下被认为具有攻击性或非包容性的术语。

想了解捏造是如何工作的吗？想一个提示，指示AI为一个不存在的主题生成内容（以确保它不在训练数据集中）。例如——我尝试了这个提示：

> **提示：** 为2076年的火星战争生成一个课程计划。

网络搜索显示有关于火星战争的虚构账户（例如，电视连续剧或书籍）——但没有在2076年。常识也告诉我们2076年是 _未来_，因此不能与真实事件相关联。

那么，当我们使用不同的LLM提供商运行此提示时会发生什么？

> **响应1**：OpenAI Playground（GPT-35）

> **响应2**：Azure OpenAI Playground（GPT-35）

> **响应3**：Hugging Face Chat Playground（LLama-2）

正如预期的那样，由于随机行为和模型能力的变化，每个模型（或模型版本）产生略有不同的响应。例如，一个模型针对8年级观众，而另一个假设高中学生。但所有三个模型都生成了可能让不知情的用户相信事件是真实的响应

提示工程技术如 _元提示_ 和 _温度配置_ 可以在一定程度上减少模型捏造。新的提示工程 _架构_ 也无缝地将新工具和技术融入提示流中，以减轻或减少其中一些影响。

## 案例研究：GitHub Copilot

让我们通过一个案例研究来了解提示工程在实际解决方案中的应用： [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)。

GitHub Copilot是您的“AI对编程伙伴”——它将文本提示转换为代码完成，并集成到您的开发环境中（例如，Visual Studio Code），提供无缝的用户体验。如下面系列博客中所述，最早的版本基于OpenAI Codex模型——工程师很快意识到需要微调模型并开发更好的提示工程技术，以提高代码质量。在7月，他们推出了[超越Codex的改进AI模型，以提供更快速的建议](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)。

按顺序阅读这些帖子，以了解他们的学习历程。

- **2023年5月** | [GitHub Copilot正在更好地理解您的代码](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023年5月** | [在GitHub内部：与GitHub Copilot背后的LLM合作](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年6月** | [如何为GitHub Copilot编写更好的提示](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)。
- **2023年7月** | [.. GitHub Copilot超越Codex的改进AI模型](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023年7月** | [开发者指南：提示工程和LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023年9月** | [如何构建企业级LLM应用程序：GitHub Copilot的经验教训](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

您还可以浏览他们的[工程博客](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)，了解更多类似[这个](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)的帖子，展示这些模型和技术如何 _应用_ 于推动现实世界的应用。

## 提示构建

我们已经了解了提示工程的重要性——现在让我们了解提示是如何 _构建_ 的，以便我们可以评估不同的技术以设计更有效的提示。

### 基本提示

让我们从基本提示开始：没有其他上下文的文本输入发送到模型。以下是一个示例——当我们将美国国歌的前几句话发送到OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)时，它立即 _完成_ 了响应，显示了基本的预测行为。

| 提示（输入） | 完成（输出） |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | 听起来您正在开始“星条旗永不落”的歌词，美国国歌。完整歌词是... |

### 复杂提示

现在让我们为该基本提示添加上下文和指令。[聊天完成API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst)允许我们将复杂提示构建为 _消息_ 的集合，其中：

- 输入/输出对反映 _用户_ 输入和 _助手_ 响应。
- 系统消息设置助手行为或个性的上下文。

请求现在采用以下形式，其中 _标记化_ 有效地捕获上下文和对话中的相关信息。现在，更改系统上下文可以对完成的质量产生与提供的用户输入同样重要的影响。

### 指令提示

在上述示例中，用户提示是一个简单的文本查询，可以被解释为信息请求。使用 _指令_ 提示，我们可以使用该文本更详细地指定任务，为AI提供更好的指导。以下是一个示例：

| 提示（输入） | 完成（输出） | 指令类型 |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| 写一篇关于内战的描述 | _返回一个简单的段落_ | 简单 |
| 写一篇关于内战的描述。提供关键日期和事件并描述其重要性 | _返回一个段落，随后是关键事件日期列表和描述_ | 复杂 |
| 写一篇关于内战的描述，限
模板的真正价值在于能够为垂直应用领域创建和发布_提示库_——此时的提示模板已被_优化_，以反映特定应用的上下文或示例，使响应对目标用户群体更加相关和准确。[Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 仓库就是这种方法的一个很好例子，专注于课程计划、课程设计、学生辅导等关键目标，策划了一个教育领域的提示库。

## 支持内容

如果我们将提示构建视为包含指令（任务）和目标（主要内容），那么_次要内容_就像我们提供的额外上下文，用于**以某种方式影响输出**。它可以是调优参数、格式说明、主题分类等，帮助模型_定制_其响应以符合用户的目标或期望。

例如：给定一个课程目录，包含所有课程的丰富元数据（名称、描述、级别、元数据标签、教师等）：

- 我们可以定义一个指令来“总结2023年秋季的课程目录”
- 我们可以使用主要内容提供几个期望输出的示例
- 我们可以使用次要内容来识别最感兴趣的5个“标签”。

现在，模型可以按照几个示例展示的格式提供摘要——但如果结果有多个标签，它可以优先考虑次要内容中识别的5个标签。

---

<!--
课程模板：
这个单元应涵盖核心概念#1。
通过示例和参考来强化概念。

概念#3：
提示工程技术。
提示工程有哪些基本技术？
通过一些练习来说明。
-->

## 提示最佳实践

现在我们知道如何_构建_提示，我们可以开始思考如何_设计_它们以反映最佳实践。我们可以从两个方面考虑——拥有正确的_心态_和应用正确的_技术_。

### 提示工程心态

提示工程是一个试错过程，因此请牢记三个广泛的指导因素：

1. **领域理解很重要。** 响应的准确性和相关性是应用或用户操作的_领域_的函数。运用你的直觉和领域专业知识来进一步**定制技术**。例如，在系统提示中定义_领域特定的个性_，或在用户提示中使用_领域特定的模板_。提供反映领域特定上下文的次要内容，或使用_领域特定的提示和示例_来引导模型走向熟悉的使用模式。

2. **模型理解很重要。** 我们知道模型本质上是随机的。但模型实现也可能因其使用的训练数据集（预训练知识）、它们提供的功能（例如，通过API或SDK）以及它们优化的内容类型（例如，代码 vs. 图片 vs. 文本）而有所不同。了解你使用的模型的优点和限制，并利用这些知识来_优先化任务_或构建_定制模板_，以优化模型的能力。

3. **迭代与验证很重要。** 模型正在迅速发展，提示工程的技术也是如此。作为领域专家，你可能有其他上下文或标准适用于_你的_特定应用，而不适用于更广泛的社区。使用提示工程工具和技术来“快速启动”提示构建，然后利用你的直觉和领域专业知识进行迭代和验证结果。记录你的见解并创建一个**知识库**（例如，提示库），供其他人使用，作为未来更快迭代的新基线。

## 最佳实践

现在让我们看看[OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)和[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)从业者推荐的常见最佳实践。

| 内容                              | 原因                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 评估最新模型。                   | 新一代模型可能具有改进的功能和质量——但也可能产生更高的成本。评估它们的影响，然后做出迁移决策。                                                                                                                                                |
| 分离指令和上下文                 | 检查你的模型/提供者是否定义了_分隔符_以更清楚地区分指令、主要和次要内容。这可以帮助模型更准确地分配权重给标记。                                                                                                                         |
| 具体且清晰                       | 提供更多关于期望上下文、结果、长度、格式、风格等的细节。这将提高响应的质量和一致性。将配方捕获到可重用的模板中。                                                                                                                          |
| 描述性，使用示例                 | 模型可能对“展示和讲解”方法响应更好。开始使用`zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT`值。回到[学习沙盒部分](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)了解如何。

### 接下来，打开 Jupyter Notebook

- 选择运行时内核。如果使用选项1或2，只需选择开发容器提供的默认 Python 3.10.x 内核。

你已经准备好进行练习。请注意，这里没有_正确与错误_的答案——只是通过试错探索选项，并为给定模型和应用领域建立直觉。

_因此，本课中没有代码解决方案部分。相反，Notebook将有标题为“我的解决方案”的Markdown单元格，显示一个示例输出供参考。_

 <!--
课程模板：
用总结和自学资源来结束部分。
-->

## 知识检查

以下哪个是遵循合理最佳实践的良好提示？

1. 给我看一辆红色汽车的图片
2. 给我看一辆红色汽车的图片，品牌为沃尔沃，型号为XC90，停在悬崖边，夕阳西下
3. 给我看一辆红色汽车的图片，品牌为沃尔沃，型号为XC90

A: 2，它是最好的提示，因为它提供了“什么”的细节并深入到具体（不仅仅是任何汽车，而是特定品牌和型号），还描述了整体环境。3是次优，因为它也包含了很多描述。

## 🚀 挑战

看看你能否利用“提示”技术完成提示：“完成句子‘给我看一辆红色汽车的图片，品牌为沃尔沃和’”。它会如何响应，你会如何改进？

## 出色的工作！继续学习

想了解更多不同的提示工程概念？访问[继续学习页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以找到其他关于此主题的优秀资源。

前往第5课，我们将探讨[高级提示技术](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。