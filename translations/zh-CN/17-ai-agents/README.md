[![开源模型](../../../translated_images/zh-CN/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## 介绍

AI代理是生成式AI中的一个令人兴奋的发展，使大型语言模型（LLM）能够从助手进化为能够采取行动的代理。AI代理框架使开发者能够创建让LLM访问工具和状态管理的应用程序。这些框架还增强了可见性，使用户和开发者能够监控LLM计划的动作，从而改善体验管理。

本课程将涵盖以下内容：

- 理解什么是AI代理——AI代理到底是什么？
- 探索五种不同的AI代理框架——它们的独特之处是什么？
- 将这些AI代理应用于不同的用例——我们什么时候应该使用AI代理？

## 学习目标

完成本课后，您将能够：

- 解释什么是AI代理以及它们如何被使用。
- 了解一些流行AI代理框架之间的差异及其不同之处。
- 理解AI代理如何工作，从而构建相关应用。

## 什么是AI代理？

AI代理是生成式AI领域一个非常令人兴奋的方向。随之而来的是一些术语和应用上的混淆。为了简单且包容大多数被称为AI代理的工具，我们将采用以下定义：

AI代理允许大型语言模型（LLM）通过访问<strong>状态</strong>和<strong>工具</strong>来执行任务。

![Agent Model](../../../translated_images/zh-CN/what-agent.21f2893bdfd01e6a.webp)

我们来定义这些术语：

<strong>大型语言模型</strong>——指本课程中提及的模型，如GPT-5、GPT-4o和Llama 3.3等。

<strong>状态</strong>——指LLM所工作的上下文。LLM利用其过去动作和当前的上下文，指导其后续动作的决策。AI代理框架让开发者更容易维护这个上下文。

<strong>工具</strong>——完成用户请求且由LLM规划的任务时，LLM需要访问工具。工具的例子包括数据库、API、外部应用甚至其他LLM！

这些定义希望能为您今后了解它们如何实现打下良好基础。我们一起来探索几种不同的AI代理框架：

## LangChain代理

[LangChain代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) 是我们上述定义的具体实现。

为了管理<strong>状态</strong>，它使用一个内置函数`AgentExecutor`，可接受定义好的`agent`和可用的`tools`。

`Agent Executor`还存储聊天历史，以提供聊天上下文。

![Langchain Agents](../../../translated_images/zh-CN/langchain-agents.edcc55b5d5c43716.webp)

LangChain提供了一个[工具目录](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可导入到应用中供LLM访问。这些工具由社区和LangChain团队制作。

您可以定义这些工具并将它们传递给`Agent Executor`。

可见性是在谈论AI代理时的另一个重要方面。应用开发者需要了解LLM正在使用哪个工具及其原因。对此，LangChain团队开发了LangSmith。

## AutoGen

下一个我们要讨论的AI代理框架是[AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen的主要关注点是对话。代理既是<strong>可对话的</strong>，也是<strong>可定制的</strong>。

**可对话的——** LLM能够与另一个LLM发起并持续对话，以完成任务。这是通过创建`AssistantAgents`并给予它们特定的系统消息完成的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

<strong>可定制的</strong>——代理不仅可以定义为LLM，还可以是用户或工具。作为开发者，您可以定义一个`UserProxyAgent`，负责与用户互动以获取完成任务的反馈。该反馈可以继续执行任务或停止任务。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状态与工具

为了更改和管理状态，助理代理生成Python代码来完成任务。

下面是该流程的一个示例：

![AutoGen](../../../translated_images/zh-CN/autogen.dee9a25a45fde584.webp)

#### 带有系统消息的LLM定义

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

该系统消息指示此特定LLM哪些功能与其任务相关。需要记住的是，在AutoGen中，您可以定义多个拥有不同系统消息的AssistantAgents。

#### 由用户发起聊天

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

用户代理（Human）发出的这条消息将启动代理探索应执行的可能功能的过程。

#### 执行功能

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

一旦处理了初始聊天，代理将发送建议调用的工具。在本例中，这是一个名为`get_weather`的函数。根据您的配置，该函数可以被自动执行和读取，也可以基于用户输入执行。

您可以在这里找到[AutoGen代码示例](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst)，进一步了解如何开始构建。

## Microsoft代理框架

[Microsoft代理框架](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) 是微软开源的用于构建AI代理和多代理系统的SDK，支持<strong>Python</strong>和<strong>.NET</strong>。它融合了微软之前两个项目的优势——企业级功能的<strong>Semantic Kernel</strong>和多代理编排的<strong>AutoGen</strong>——整合成一个支持的框架。如果您今天开始一个新的代理项目，这是AutoGen的推荐后续方案。

该框架可扩展至单个<strong>聊天代理</strong>，也支持复杂的<strong>多代理工作流</strong>，并且可直接与Microsoft Foundry、Azure OpenAI和OpenAI集成。它还通过OpenTelemetry提供内置可观测性，让您可以精确追踪代理的行为。

### 状态与工具

<strong>状态</strong>——框架通过<strong>线程</strong>管理对话上下文。代理跟踪消息历史（用户请求、工具调用及其结果），每轮对话基于前一轮建立。线程可持久化，允许对话暂停和恢复。

<strong>工具</strong>——您通过传递普通Python函数给代理设置工具。带类型注释的参数会自动转换为模式(schema)，模型能知道如何及何时调用它们（函数调用）。框架也支持模型上下文协议(MCP)服务器和托管工具，如代码解释器。

下面是一个带自定义工具的单代理示例：

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

若要改为连接Microsoft Foundry的Azure OpenAI，需要将端点和凭证传给客户端：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### 多代理工作流

该框架真正出彩之处在于编排多个代理协同工作。例如，您可以让代理一个接一个运行（每个代理传递上下文给下一个），或并行启动多个代理并聚合其结果：

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# 按顺序运行代理，在链中传递对话上下文
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# 并行分发给代理，然后汇总它们的响应
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

安装框架并开始使用：

```bash
pip install agent-framework-core
# 可选集成
pip install agent-framework-openai       # OpenAI 和 Azure OpenAI
pip install agent-framework-foundry      # 微软 Foundry
```

您可以在[Microsoft代理框架仓库](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst)和[官方文档](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst)中了解更多。

## Taskweaver

接下来我们将探讨[Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst)代理框架。其被称为“代码优先”代理，因为它不仅仅严格处理`字符串`，还能处理Python中的DataFrame。这在数据分析和生成任务中非常有用，比如制作图表和图形或生成随机数。

### 状态与工具

TaskWeaver通过`Planner`管理对话状态。`Planner`是一个LLM，它接收用户请求并制定完成请求所需任务的计划。

为了完成任务，`Planner`可以访问称为`Plugins`的工具集。这些可以是Python类或通用代码解释器。插件以嵌入形式存储，便于LLM更好地检索合适插件。

![Taskweaver](../../../translated_images/zh-CN/taskweaver.da8559999267715a.webp)

下面是一个处理异常检测的插件示例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

代码在执行前会被验证。Taskweaver中管理上下文的另一个功能是`experience`。Experience允许将对话上下文长时间存储在YAML文件中。这样可以配置，让LLM随着暴露于先前对话在特定任务上不断进步。

## JARVIS

我们要探讨的最后一个代理框架是[JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst)。JARVIS的独特之处在于使用LLM管理对话的`状态`，而`工具`则是其他AI模型。每个AI模型都是专门执行某些任务的模型，比如对象检测、转录或图像标题生成。

![JARVIS](../../../translated_images/zh-CN/jarvis.762ddbadbd1a3a33.webp)

作为通用模型的LLM接收用户请求，并识别具体任务及完成任务所需的任何参数/数据。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM随后以专门AI模型能理解的格式（如JSON）组织请求。一旦AI模型基于任务返回预测结果，LLM接收响应。

如果完成任务需要多个模型，LLM还会解析这些模型的响应，再将它们综合生成对用户的回复。

下面的示例展示了当用户请求描述和计数图片中对象时的工作流程：

## 任务

为继续学习AI代理，您可以使用Microsoft代理框架构建：

- 一个模拟教育创业公司不同部门业务会议的应用。
- 创建系统消息，指导LLM理解不同角色和优先事项，并允许用户推介新产品想法。
- LLM随后应从各部门生成后续问题以完善和改进推介及产品想法。

## 学习不会止步于此，继续你的旅程

完成本课后，欢迎浏览我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->