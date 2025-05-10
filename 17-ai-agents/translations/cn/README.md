[![开放源码模型](../../images/17-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## 简介

AI 智能体代表了生成式AI的一个令人兴奋的发展，使大型语言模型（LLMs）从助手演变为能够采取行动的智能体。AI 智能体框架使开发者能够建立应用程序，让LLMs能够访问工具和状态管理。这些框架还增强了可见性，使用户和开发者能够监控LLMs计划的行动，从而改善体验管理。

这节课将涵盖以下领域:

- 理解什么是 AI Agent - AI Agent 到底是什么？
- 探索四种不同的 AI Agent 框架 - 它们有什么独特之处？
- 将这些 AI Agent 应用于不同的使用案例 - 我们应该何时使用 AI Agent？

## 学习目标

完成这节课后，你将能够：

- 解释什么是 AI 智能体以及它们如何使用。
- 了解一些流行的 AI 智能体框架之间的差异，以及它们的不同之处。
- 了解 AI 智能体如何运作，以便使用它们构建应用程序。

## 什么是 AI 智能体？

AI 智能体是一个在生成式AI世界中非常令人兴奋的领域。随着这种兴奋，有时会出现术语和其应用的混淆。为了保持简单并包含大多数提到AI 智能体的工具，我们将使用这一定义:

AI Agents 允许大型语言模型（LLMs）通过提供**状态**和**工具**来执行任务。

![智能体模型](../../images/what-agent.png?WT.mc_id=academic-105485-koreyst)

让我们定义这些术语:

**大型语言模型** - 这些是本课程中提到的模型，例如 GPT-3.5、GPT-4、Llama-2 等。

**状态** - 这指的是LLM正在工作的上下文。LLM使用其过去行动的上下文和当前上下文，指导其后续行动的决策。AI 智能体框架允许开发人员更容易地维护此上下文。

**工具** - 为了完成用户请求的任务以及 LLM 所规划的任务，LLM 需要访问工具。一些工具的例子可以是数据库、API、外部应用程序甚至是另一个 LLM！

这些定义希望能在我们了解它们如何实现时，为你打下良好的基础。让我们来探索几个不同的 AI Agent 框架:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是我们上述定义的实现。

要管理**状态**，它使用一个名为 `AgentExecutor` 的内置函数。这个函数接受定义的 `agent` 和可用的 `tools`。

`Agent Executor` 也存储聊天记录以提供聊天的上下文。

![Langchain Agents](../../images/langchain-agents.png?WT.mc_id=academic-105485-koreyst)

LangChain 提供一个[工具目录](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以导入到您的应用程序中，LLM 可以访问这些工具。这些工具由社区和 LangChain 团队制作。

然后你可以定义这些工具并将它们传递给 `Agent Executor`。

可见性是讨论 AI 智能体时另一个重要方面。应用程序开发人员需要了解 LLM 使用的是哪种工具以及为什么。为此，LangChain 团队开发了 LangSmith。

## AutoGen

下一个我们将讨论的 AI Agent 框架是 [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen 的主要焦点是对话。Agents 既是**可对话的**也是**可定制的**。

**Conversable -** LLMs 可以启动并继续与另一个 LLM 的对话以完成任务。这是通过建立 `AssistantAgents` 并给予它们特定的系统消息来完成的。

```python
autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) 
pm = autogen.AssistantAgent( 
    name="Product_manager", 
    system_message="Creative in software product ideas.",
    llm_config=llm_config, 
)
```

**可自订** - Agent 不仅可以定义为 LLMs，也可以是用户或工具。作为开发者，你可以定义一个 `UserProxyAgent`，负责与用户互动以获取完成任务的反馈。这些反馈可以继续执行任务或停止它。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状态和工具

为了改变和管理状态，助手智能体生成 Python 代码来完成任务。

这里是一个过程的示例:

![AutoGen](../../images/autogen.png?WT.mc_id=academic-105485-koreyst)

#### 定义 LLM 的系统消息

```python
system_message="对于天气相关的任务，只使用提供给你的函数。任务完成后回复 TERMINATE。"
```

此系统信息指导此特定 LLM 哪些函数与其任务相关。请记住，使用 AutoGen 时，您可以有多个具有不同系统信息的 AssistantAgents。

#### 聊天由用户发起

```python
user_proxy.initiate_chat( chatbot, message="我计划下周去纽约旅行，你能帮我选择穿什么吗？", )
```

此消息来自 user_proxy (人类) 是启动智能体探索应执行的可能函数的过程。

#### 函数被执行

```bash
聊天机器人 (to user_proxy):

***** 建议的工具调用: get_weather ***** 参数: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> 执行函数 get_weather... user_proxy (to 聊天机器人): ***** 调用函数 "get_weather" 的回应 ***** 112.22727272727272 EUR ****************************************************************

```

一旦初始聊天处理完成，智能体将发送建议的工具来调用。在这种情况下，它是一个名为 `get_weather` 的函数。根据您的配置，这个函数可以由智能体自动执行和读取，或者可以根据用户输入来执行。

你可以找到[AutoGen 代码示例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)来进一步探索如何开始构建。

## Taskweaver

接下来我们将探讨的智能体框架是 [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被称为「代码优先」智能体，因为它不仅仅是严格地与 `strings` 一起工作，它还可以与 Python 中的 DataFrames 一起工作。这对于资料分析和生成任务变得非常有用。这可以是建立图表或生成随机数等事情。

### 状态和工具

为了管理对话的状态，TaskWeaver 使用了 `Planner` 的概念。`Planner` 是一个 LLM，它接收用户的请求并规划出需要完成的任务，以满足这些请求。

为了完成任务，`Planner` 会接触到称为 `Plugins` 的工具集合。这可以是 Python 类别或一般的代码解释器。这些插件被储存为嵌入，以便 LLM 能够更好地搜索正确的插件。

![Taskweaver](../../images/taskweaver.png?WT.mc_id=academic-105485-koreyst)

这里是一个处理异常检测的插件示例:

```python
class AnomalyDetectionPlugin(Plugin): 
    def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

代码在执行前会被验证。Taskweaver 中管理上下文的另一个功能是 `experience`。Experience 允许将对话的上下文长期存储在 YAML 文件中。这可以配置，使得 LLM 随着时间的推移在某些任务上有所改进，前提是它接触到先前的对话。

## JARVIS

最后我们将探讨的智能体框架是 [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst)。JARVIS 的独特之处在于它使用 LLM 来管理对话的 `state`，而 `tools` 是其他 AI 模型。每个 AI 模型都是专门的模型，执行某些任务，例如物体检测、转录或图像标注。

![JARVIS](../../images/jarvis.png?WT.mc_id=academic-105485-koreyst)

LLM 作为一个通用模型，接收来自用户的请求并识别特定任务及完成任务所需的任何参数/资料。

```python
[{"task": "物体-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM 然后以专门的 AI 模型能够解释的方式格式化请求，例如 JSON。一旦 AI 模型根据任务返回其预测，LLM 便会接收回应。

如果需要多个模型来完成任务，它还会解释这些模型的回应，然后将它们整合起来生成对用户的回应。

范例如下显示当用户请求描述和计算图片中的物体时，这将如何运作:

## 作业

为了继续学习可以使用 AutoGen 构建的 AI 智能体:

- 一个模拟教育初创公司不同部门商务会议的应用程序。
- 建立系统信息，引导LLM理解不同角色和优先事项，并使用户能够提出新的产品创意。
- 然后，LLM应从每个部门生成后续问题，以完善和改进提案和产品创意。

## 学习不止于此，继续旅程

完成本课程后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以继续提升您的生成式 AI 知识！


