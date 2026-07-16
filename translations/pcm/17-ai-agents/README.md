[![Open Source Models](../../../translated_images/pcm/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduction

AI Agents na one kain beta development for Generative AI, wey dey enable Large Language Models (LLMs) to change from assistants come be agents wey fit take actions. AI Agent frameworks dey help developers make applications wey fit give LLMs access to tools and state management. These frameworks still dey improve how people fit see wetin LLMs plan to do, make users and developers fit monitor am well, so e go beta the experience wey dem get.

Dis lesson go cover dis kain tins:

- Understand wetin AI Agent be - Wetin AI Agent really mean?
- Check five different AI Agent Frameworks - Wetin make dem special?
- How to use these AI Agents for different case dem - Wen person suppose use AI Agents?

## Learning goals

After you don take dis lesson, you go fit:

- Explain wetin AI Agents be and how person fit use dem.
- Understand the difference between some popular AI Agent Frameworks, and how dem different.
- Understand how AI Agents dey work to fit build applications with dem.

## Wetin be AI Agents?

AI Agents na very exciting area for Generative AI world. But sometimes e dey cause small confusion about the terms and how dem dey use am. To make am simple and cover most tools wey dey call themselves AI Agents, we go use this definition:

AI Agents dey allow Large Language Models (LLMs) to do work by giving dem access to **state** and **tools**.

![Agent Model](../../../translated_images/pcm/what-agent.21f2893bdfd01e6a.webp)

Make we define these tins:

**Large Language Models** - Na these models we dey talk about for this course like GPT-5, GPT-4o, and Llama 3.3, and others.

**State** - Na the context wey LLM dey work inside. LLM dey use the past actions and the current context to decide wetin e go do next. AI Agent Frameworks dey help developers manage this context well-well.

**Tools** - To fit complete the work wey user ask and LLM plan to do, LLM need access to tools. Some examples of tools na database, API, external application, or even another LLM!

These definitions go help you understand well as we dey see how dem dey implement am. Make we look some different AI Agent frameworks:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) na the way dem take implement the definitions we talk before.

To manage the **state**, e dey use one built-in function wey dem call `AgentExecutor`. E dey accept the `agent` wey dem define and the `tools` wey e fit use.

`Agent Executor` still dey keep chat history so e fit provide the chat context.

![Langchain Agents](../../../translated_images/pcm/langchain-agents.edcc55b5d5c43716.webp)

LangChain get one [catalog of tools](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) wey you fit import for your application so the LLM fit use am. Na community and LangChain team be the makers of these tools.

You fit define these tools and give am to `Agent Executor`.

Visibility na beta part when we dey talk about AI Agents. E important make application developer dem understand which tool LLM dey use and why e dey use am. For that one, LangChain team make LangSmith.

## AutoGen

The next AI Agent framework we go talk about na [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). The main matter for AutoGen na conversations. Agents fit both **talk** and **customize** well.

**Conversable -** LLM fit start and continue talk with another LLM to complete task. This one dey happen by creating `AssistantAgents` and dem dey give dem special system message.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Customizable** - Agents no be only LLM, dem fit be user or tools too. As developer, you fit define `UserProxyAgent` wey go dey interact with user to get feedback for task completion. This feedback fit make task continue or stop.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### State and Tools

To change and manage state, assistant Agent dey generate Python code to complete the work.

Example for how e dey work:

![AutoGen](../../../translated_images/pcm/autogen.dee9a25a45fde584.webp)

#### LLM Define with System Message

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Dis system message dey guide dis specific LLM on which functions e suppose use for im work. Remember say for AutoGen, you fit get many different AssistantAgents with different system messages.

#### Chat Start from User

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Dis message from user_proxy (Human) na im go start the process for Agent to check the possible functions wey e fit execute.

#### Function Execute

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

After the first chat don process, Agent go send suggestion to call tool. For this case, na function `get_weather`. Depending on how you configure am, this function fit auto run and the Agent fit read am or e fit run based on user input.

You fit find list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to learn more and start building.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) na Microsoft's open-source SDK to build AI Agents and multi-agent systems for both **Python** and **.NET**. E join two Microsoft projects together — enterprise features of **Semantic Kernel** and multi-agent orchestration of **AutoGen** — into one framework wey dem dey support well. If you dey start new agent project now, na this one dem recommend pass AutoGen.

The framework fit handle from one **chat agent** reach **complex multi-agent workflows**, e dey connect directly with Microsoft Foundry, Azure OpenAI, and OpenAI. E get built-in observability with OpenTelemetry so you fit trace exactly wetin your agents dey do.

### State and Tools

**State** - Framework dey manage conversation context for you through **threads**. Agent dey keep message history (user requests, tool calls, and results), so each turn dey build on top previous ones. Threads fit still dey saved, so conversation fit pause and continue later.

**Tools** - You fit give agent tools by passing simple Python functions. Type-annotated parameters go automatically change to schema, so model go sabi how and when to call dem (function calling). Framework still support Model Context Protocol (MCP) servers and hosted tools like code interpreter.

Example of one single agent with custom tool:

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

To connect to Azure OpenAI for Microsoft Foundry, just pass your endpoint and credentials to client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent workflows

The way framework show beta pass na when e dey orchestrate many agents together. For example, you fit run agents one after another (each one pass context give the next) or run many agents for same time and combine their results:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Make agents run one after di oda, carry di conversation context go along di chain
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Spread agents to run for same time, den gather dem responses together
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

To install the framework and start:

```bash
pip install agent-framework-core
# Optional integrations
pip install agent-framework-openai       # OpenAI and Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

You fit learn more for [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) and [official documentation](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

The next agent framework we go check na [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Dem dey call am "code-first" agent because e no just work with `strings`; e fit also work with DataFrames for Python. This one dey very useful for data analysis and generating tasks like making graphs and charts or create random numbers.

### State and Tools

To manage conversation state, TaskWeaver dey use concept wey dem call `Planner`. `Planner` na LLM wey take user request and plan the tasks wey need to finish to complete the request.

To finish the tasks, `Planner` dey get access to collection of tools wey dem call `Plugins`. These fit be Python classes or general code interpreter. These plugins dey stored as embeddings so LLM fit find correct plugin well.

![Taskweaver](../../../translated_images/pcm/taskweaver.da8559999267715a.webp)

Example of one plugin wey fit do anomaly detection:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Code go check well before e run. Another beta feature for managing context for Taskweaver na `experience`. Experience dey allow make conversation context save for long term inside YAML file. You fit configure am so the LLM go improve over time on some tasks if e dey see past conversation.

## JARVIS

Last agent framework we go look na [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Wetin make JARVIS special na say e use LLM to manage the `state` of conversation and the `tools` na other AI models. Each AI model na specialized model wey fit do certain task like object detection, transcription or image captioning.

![JARVIS](../../../translated_images/pcm/jarvis.762ddbadbd1a3a33.webp)

The LLM, wey be general purpose model, go receive request from user and identify the particular task and any arguments/data wey needed to complete the task.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Then the LLM go format the request the way specialized AI model fit understand, like JSON. After AI model don return its prediction based on task, LLM go receive the response.

If many models need to work to finish the task, LLM go also interpret response from all those models before e join dem to generate answer for user.

Example below show how e go work when user ask for description and count of objects for picture:

## Assignment

To continue your learning about AI Agents, you fit build with Microsoft Agent Framework:

- One application wey go simulate business meeting with different departments for education startup.
- Create system messages wey go guide LLMs to understand different personas and priorities, and make user fit pitch new product idea.
- Then make LLM generate follow-up questions from each department to refine and improve the pitch and product idea.

## Learning no stop here, continue di Journey

After you finish this lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to upgrade your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->