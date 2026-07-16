[![开源模型](../../../translated_images/zh-CN/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介绍

AI代理是生成式AI中的一个令人兴奋的发展，使大型语言模型（LLMs）从助手演变为能够采取行动的代理。AI代理框架使开发人员能够创建让LLM访问工具和状态管理的应用程序。这些框架还增强了可见性，允许用户和开发者监控LLM计划的动作，从而提升体验管理。

本课程将涵盖以下内容：

- 了解什么是AI代理——AI代理到底是什么？
- 探索五种不同的AI代理框架——它们各有什么独特之处？
- 将这些AI代理应用到不同的用例——何时应该使用AI代理？

## 学习目标

完成本课程后，你将能够：

- 解释什么是AI代理以及它们如何被使用。
- 理解一些流行的AI代理框架之间的差异，以及它们是如何不同的。
- 理解AI代理的工作原理，以便用它们构建应用程序。

## 什么是AI代理？

AI代理是生成式AI领域一个非常令人兴奋的部分。随着兴奋而来的，往往也会带来术语和应用的困惑。为了简化并涵盖大多数被称为AI代理的工具，我们将使用如下定义：

AI代理允许大型语言模型（LLMs）通过赋予它们<strong>状态</strong>和<strong>工具</strong>来执行任务。

![代理模型](../../../translated_images/zh-CN/what-agent.21f2893bdfd01e6a.webp)

让我们定义这些术语：

<strong>大型语言模型</strong> - 这些是在本课程中提到的模型，如GPT-3.5、GPT-4、Llama-2等。

<strong>状态</strong> - 指的是LLM工作的上下文。LLM利用其过去的行为和当前上下文，指导其后续行动的决策。AI代理框架帮助开发者更易于维护这种上下文。

<strong>工具</strong> - 为了完成用户请求且LLM计划的任务，LLM需要使用工具。一些工具的例子可以是数据库、API、外部应用程序甚至另一个LLM！

这些定义希望能为你后续理解它们的实现打下良好基础。接下来，让我们探索几个不同的AI代理框架：

## LangChain代理

[LangChain代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)是我们上面定义的实现。

为了管理<strong>状态</strong>，它使用一个内置功能叫做`AgentExecutor`。它接受定义好的`agent`和可用的`tools`。

`AgentExecutor`还会存储聊天历史，提供聊天的上下文。

![Langchain代理](../../../translated_images/zh-CN/langchain-agents.edcc55b5d5c43716.webp)

LangChain提供了一个[工具目录](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以导入到你的应用中，LLM可以使用这些工具。这些工具由社区和LangChain团队制作。

你可以定义这些工具并传递给`AgentExecutor`。

在谈论AI代理时，可见性是另一个重要方面。应用开发者需要了解LLM使用了哪个工具及原因。为此，LangChain团队开发了LangSmith。

## AutoGen

接下来讨论的AI代理框架是[AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen的主要关注点是对话。代理既<strong>可对话</strong>又<strong>可定制</strong>。

<strong>可对话</strong> - LLM可以启动并持续与另一个LLM对话以完成任务。这是通过创建`AssistantAgents`并给它们一个特定的系统消息实现的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可定制</strong> - 代理不仅可以定义为LLM，还可以是用户或工具。作为开发者，你可以定义一个`UserProxyAgent`，负责与用户交流反馈以完成任务。此反馈可以继续执行任务或终止任务。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状态和工具

为了更改和管理状态，助手代理生成Python代码以完成任务。

下面是该过程的示例：

![AutoGen](../../../translated_images/zh-CN/autogen.dee9a25a45fde584.webp)

#### 用系统消息定义LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

该系统消息指示特定LLM哪些功能与其任务相关。记住，使用AutoGen你可以定义多个带有不同系统消息的AssistantAgents。

#### 聊天由用户发起

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

用户代理（Human）的消息将启动代理探查其应执行的可能功能的过程。

#### 功能执行

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

初始聊天处理完成后，代理会发送建议调用的工具。在此示例中，调用了一个名为`get_weather`的函数。根据配置，函数可自动执行并由代理读取，也可根据用户输入执行。

你可以查阅[AutoGen代码示例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，进一步探索如何开始构建。

## Microsoft代理框架

[Microsoft代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)是微软的开源SDK，用于构建AI代理和多代理系统，支持<strong>Python</strong>和<strong>.NET</strong>。它结合了微软两个早期项目的优势——企业功能的<strong>Semantic Kernel</strong>和多代理编排的<strong>AutoGen</strong>——合为一个支持的框架。如果你今天要开始一个新的代理项目，这是推荐的AutoGen继任者。

该框架可扩展，从单一的<strong>聊天代理</strong>到复杂的<strong>多代理工作流</strong>，并且直接集成微软Foundry、Azure OpenAI和OpenAI。它还通过OpenTelemetry提供内置的可观察性，让你能准确跟踪代理的行为。

### 状态和工具

<strong>状态</strong> - 框架通过<strong>线程</strong>管理对话上下文。代理跟踪消息历史（用户请求、工具调用及其结果），每轮构建在上一轮基础上。线程也可以持久化，允许对话暂停后继续。

<strong>工具</strong> - 你通过传递简单的Python函数给代理。带类型注释的参数会自动转换为一个schema，这样模型就知道如何及何时调用这些函数（函数调用）。框架还支持Model Context Protocol (MCP)服务器和代码解释器等托管工具。

这是一个带自定义工具的单代理示例：

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

若要连接Microsoft Foundry中的Azure OpenAI，请将你的端点和凭据传给客户端：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 多代理工作流

该框架真正出彩的是编排多个代理。例如，你可以一个接一个地运行代理（每个将其上下文传递给下一个），或并行运行多个代理并聚合它们的结果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按顺序运行代理，将对话上下文沿链传递
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 并行分发给多个代理，然后汇总它们的响应
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安装框架并开始使用：

```bash
pip install agent-framework-core
# 可选集成
pip install agent-framework-openai       # OpenAI 和 Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

你可以在[Microsoft代理框架仓库](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)和[官方文档](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)中了解更多。

## Taskweaver

下一个探索的代理框架是[Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)。它被称为“代码优先”的代理，因为它不仅使用`字符串`，还能处理Python中的DataFrames。这对数据分析和生成任务非常有用，比如创建图表或生成随机数。

### 状态和工具

为了管理对话状态，TaskWeaver使用了`Planner`概念。`Planner`是一个LLM，接收用户请求，规划完成该请求需要执行的任务。

为完成任务，`Planner`可以使用名为`Plugins`的工具集合。这些插件可以是Python类或通用代码解释器。这些插件以嵌入的形式存储，帮助LLM更好地搜寻正确的插件。

![Taskweaver](../../../translated_images/zh-CN/taskweaver.da8559999267715a.webp)

这是一个处理异常检测的插件示例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

代码在执行前会被验证。Taskweaver中管理上下文的另一特性是`experience`。Experience允许会话上下文在YAML文件中长期存储。配置后，LLM可以通过接触先前对话逐步改进某些任务的表现。

## JARVIS

最后一个代理框架是[JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS的独特之处在于，它使用LLM管理对话`状态`，而`工具`是其他AI模型。每个AI模型都是专门的模型，用于执行特定任务，如目标检测、转录或图像描述。

![JARVIS](../../../translated_images/zh-CN/jarvis.762ddbadbd1a3a33.webp)

通用模型LLM接收用户请求，确定具体任务及完成任务所需的参数/数据。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM将请求格式化为专门AI模型可理解的形式，如JSON。AI模型返回预测后，LLM接收回应。

如任务需要多个模型，它还会解释这些模型的响应，然后汇总生成回复给用户。

以下示例展示用户请求图片中对象的描述和计数时的工作流程：

## 任务

继续学习AI代理，尝试使用Microsoft代理框架构建：

- 一个模拟教育初创公司不同部门商务会议的应用。
- 创建系统消息，引导LLM理解不同角色和优先级，使用户能够推介新产品想法。
- 之后LLM应生成来自各部门的后续问题，以完善和改进推介及产品想法。

## 学习远未结束，继续前行

完成本课后，可查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持续提升你的生成式AI知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->