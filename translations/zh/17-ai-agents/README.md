[![开源模型](../../../translated_images/17-lesson-banner.png?WT.d223296926e27d95f6b5a748e3f77ab9a1b669d4f9aebe608f926cbb44ea08a8.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## 介绍

AI代理代表了生成式AI中的一个激动人心的发展，使大型语言模型（LLM）从助手进化为能够采取行动的代理。AI代理框架使开发人员能够创建应用程序，让LLM访问工具和状态管理。这些框架还增强了可视性，使用户和开发人员能够监控LLM计划的动作，从而改善体验管理。

本课将涵盖以下领域：

- 理解AI代理是什么 - AI代理到底是什么？
- 探索四种不同的AI代理框架 - 它们有什么独特之处？
- 将这些AI代理应用于不同的用例 - 什么时候应该使用AI代理？

## 学习目标

完成本课后，你将能够：

- 解释什么是AI代理以及如何使用它们。
- 理解一些流行的AI代理框架之间的区别，以及它们的不同之处。
- 理解AI代理的工作原理，以便用它们构建应用程序。

## 什么是AI代理？

AI代理在生成式AI的世界中是一个非常令人兴奋的领域。伴随着这种兴奋，有时也会出现术语和其应用的混淆。为了简单并涵盖大多数涉及AI代理的工具，我们将使用以下定义：

AI代理通过为大型语言模型（LLM）提供访问**状态**和**工具**的权限来执行任务。

![代理模型](../../../translated_images/what-agent.png?WT.96b2eb171bd613cd0652fb5a2c1f488c80fde8d3405db76d780603041a415cb3.zh.mc_id=academic-105485-koreyst)

让我们定义这些术语：

**大型语言模型** - 这些是本课程中提到的模型，如GPT-3.5、GPT-4、Llama-2等。

**状态** - 这指的是LLM工作的上下文。LLM利用其过去动作的上下文和当前上下文，引导其后续动作的决策。AI代理框架使开发人员更容易维护这种上下文。

**工具** - 为了完成用户请求的任务以及LLM计划的任务，LLM需要访问工具。一些工具的例子可以是数据库、API、外部应用程序，甚至是另一个LLM！

希望这些定义能为你提供一个良好的基础，因为我们将探讨它们是如何实现的。让我们来看看几个不同的AI代理框架：

## LangChain代理

[LangChain代理](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst)是我们提供的定义的一个实现。

为了管理**状态**，它使用一个内置函数`AgentExecutor`。这接受已定义的`agent`和可用的`tools`。

`Agent Executor`还存储了聊天记录，以提供聊天的上下文。

![Langchain代理](../../../translated_images/langchain-agents.png?WT.311575a86262a6e33490477b281688373d96e3392dbfe3094965470531a9f111.zh.mc_id=academic-105485-koreyst)

LangChain提供了一个[工具目录](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst)，可以导入到你的应用程序中，LLM可以访问这些工具。这些工具由社区和LangChain团队制作。

然后你可以定义这些工具并将它们传递给`Agent Executor`。

可视性是讨论AI代理时的另一个重要方面。应用程序开发人员了解LLM正在使用哪个工具以及原因非常重要。为此，LangChain团队开发了LangSmith。

## AutoGen

接下来我们将讨论的AI代理框架是[AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst)。AutoGen的主要关注点是对话。代理既可以**对话**也可以**定制**。

**对话 -** LLM可以启动并继续与另一个LLM的对话以完成任务。这是通过创建`AssistantAgents`并给它们一个特定的系统消息来完成的。

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**定制** - 代理不仅可以定义为LLM，还可以是用户或工具。作为开发人员，你可以定义一个`UserProxyAgent`，负责与用户交互以获得完成任务的反馈。此反馈可以继续执行任务或停止它。

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### 状态和工具

为了更改和管理状态，助手代理生成Python代码以完成任务。

这是一个过程示例：

![AutoGen](../../../translated_images/autogen.png?WT.45c9474fbd6109577f4363559f022554e796000ea2d677b80021b00e6ca0d869.zh.mc_id=academic-105485-koreyst)

#### 用系统消息定义的LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

这个系统消息指引特定的LLM完成任务所需的相关功能。记住，使用AutoGen，你可以定义多个具有不同系统消息的AssistantAgents。

#### 用户启动聊天

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

来自user_proxy（人类）的这条消息将启动代理探索应该执行的可能功能的过程。

#### 执行功能

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

一旦初始聊天被处理，代理将发送建议调用的工具。在这种情况下，它是一个名为`get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`的功能。这可以是Python类或通用代码解释器。这些插件存储为嵌入，以便LLM可以更好地搜索正确的插件。

![Taskweaver](../../../translated_images/taskweaver.png?WT.c5d336793941a5af0d2489ad6d88a03f09557bd5ca68a954f1ddaa3d9f1ecc3b.zh.mc_id=academic-105485-koreyst)

这是一个处理异常检测的插件示例：

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

在执行之前会验证代码。Taskweaver中管理上下文的另一个功能是`experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state`对话和`tools`是其他AI模型。每个AI模型都是专门的模型，执行特定任务，如对象检测、转录或图像描述。

![JARVIS](../../../translated_images/jarvis.png?WT.f12468c52a0c4848aeed51606a0e53a36eb38c65cc6c821597ea4dcaad03d1a3.zh.mc_id=academic-105485-koreyst)

LLM作为通用模型，接收用户的请求，并识别完成任务所需的特定任务和任何参数/数据。

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

然后LLM以专用AI模型可以解释的方式格式化请求，例如JSON。一旦AI模型根据任务返回其预测，LLM接收响应。

如果需要多个模型来完成任务，它还将解释这些模型的响应，然后将它们结合起来生成对用户的响应。

下面的示例显示了当用户请求图像中对象的描述和计数时，这将如何工作：

## 作业

为了继续学习AI代理，你可以使用AutoGen构建：

- 一个模拟教育初创公司不同部门的商务会议的应用程序。
- 创建系统消息，引导LLM理解不同的角色和优先级，并使用户能够推销新的产品理念。
- 然后，LLM应该生成每个部门的后续问题，以完善和改进推销和产品理念。

## 学习不止于此，继续旅程

完成本课后，请查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式AI知识！

**免责声明**：
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文件的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们概不负责。