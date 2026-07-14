[![Open Source Models](../../../translated_images/pcm/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introdukshon

AI Agents na one kain beta tins wey don dey for Generative AI, wey dey make Large Language Models (LLMs) move from just assistant dem go become agent wey fit do tins. AI Agent frameworks dey help developers build apps wey dey give LLMs chance to use tools and manage how tins dey go. Dem frameworks sef dey make e clear say, so users and developers fit dey watch wetin LLMs plan to do and make experience better.

Dis lesson go cover dis kind tins:

- Make una sabi wetin AI Agent mean - Wetin be AI Agent exactly?
- Look different AI Agent Frameworks dem five - Wetin make dem different?
- How to use AI Agents for different kain work - When we suppose use AI Agents?

## Learning goals

After you finish dis lesson, you go fit:

- Talk wetin AI Agents be and how dem fit take work.
- Get sense about the differences wey dey for some popular AI Agent Frameworks, and how dem dey different.
- Understand how AI Agents dey work so you fit build apps with dem.

## Wetin be AI Agents?

AI Agents na one beta field for the world of Generative AI. With this kain beta thing dey come sometimes confusion about terms and how e dey work. To make am easy and cover majority of the tools wey dey call themselves AI Agents, we go use dis definition:

AI Agents dey allow Large Language Models (LLMs) to do work by giving dem access to **state** and **tools**.

![Agent Model](../../../translated_images/pcm/what-agent.21f2893bdfd01e6a.webp)

Make we explain dis terms:

**Large Language Models** - Na dis one be di models wey we dey talk about throughout this course like GPT-3.5, GPT-4, Llama-2, and others.

**State** - Na the context wey di LLM dey work inside. Di LLM dey use wetin e don do before and wetin dey happen now to guide how e go take decide di next tins for action. AI Agent Frameworks dey help developers manage dis context well well.

**Tools** - To finish di work wey user request and wey LLM plan, di LLM need access to tools. Examples na database, API, external app or even another LLM!

Dis definitions go help you get beta understanding as we go look how dem dey put am to work. Make we check small different AI Agent frameworks:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) na di way wey dem implement di tins wey we define above.

To manage di **state** , e dey use one built-in function wey dem call `AgentExecutor`. E dey accept di `agent` wey define and di `tools` wey e fit use.

Di `Agent Executor` sef dey save di chat history to fit show di context of di chat.

![Langchain Agents](../../../translated_images/pcm/langchain-agents.edcc55b5d5c43716.webp)

LangChain get [catalog of tools](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) wey you fit put inside your app make di LLM get access to. Dem tools na community and LangChain team make.

You fit define dis tools and pass am go `Agent Executor`.

Visibility na important one when we dey talk AI Agents. E important for app developers to sabi which tool LLM dey use and why.. So for dat, LangChain team develop LangSmith.

## AutoGen

The next AI Agent framework we go talk about na [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGen main focus na conversations. Agents fit **talk** and fit **customize**.

**Conversable -** LLMs fit start and continue talk with another LLM to finish task. Dem dey create `AssistantAgents` and give dem special system messages.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Customizable** - Agents no be only LLMs, dem fit be user or tool tu. As developer, you fit define `UserProxyAgent` wey go dey interact with user for feedback to finish task. Dis feedback fit make task continue or stop.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### State and Tools

To manage state, assistant Agent dey create Python code to finish di task.

Dis na example of how e dey waka:

![AutoGen](../../../translated_images/pcm/autogen.dee9a25a45fde584.webp)

#### LLM Define with System Message

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Dis system message dey guide dis LLM which functions e go focus for task. Remember, AutoGen fit get multiple defined AssistantAgents wey get different system messages.

#### Chat Start from User

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Dis message from user_proxy (Human) na wetin go start Agent process to check which functions e suppose execute.

#### Function dey Execute

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

After initial chat finish processing, Agent go send suggested tool to call. For dis case na function wey dem call `get_weather`. Based on your config, dis function fit automatically run or Agent fit run am based on user talk.

You fit find list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to sabi more how to start to build.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) na open-source SDK from Microsoft wey dem use to build AI Agents and multi-agent systems for both **Python** and **.NET**. E join strength from two previous Microsoft projects — enterprise features of **Semantic Kernel** and multi-agent orchestration of **AutoGen** — into one framework wey Microsoft support. If you dey start new agent project now, dis na di best choice after AutoGen.

Di framework fit handle from single **chat agent** reach complex **multi-agent workflows**, and e fit integrate well well with Microsoft Foundry, Azure OpenAI, and OpenAI. E dey also get built-in observability through OpenTelemetry so you fit trace exactly wetin your agents dey do.

### State and Tools

**State** - Di framework dey manage conversation context for you through **threads**. Agent dey keep record of message history (user requests, tool calls, and results), so each turn dey build on top previous one. Threads fit save make conversation fit pause and continue later.

**Tools** - You dey give agent tools by passing plain Python functions. If parameters get type annotation e go automatically become schema so model go sabi how and when to call am (function calling). Framework also support Model Context Protocol (MCP) servers and hosted tools like code interpreter.

Here be example of single agent with custom tool:

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

To connect to Azure OpenAI for Microsoft Foundry instead, just pass your endpoint and credentials to client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent workflows

Di framework sabi well well to dey manage several agents together. For example, you fit run agents one after another (each one dey pass im context to the next) or run many agents side by side then combine results:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Make agents run one after the oda, carry di conversation gist go along di chain
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Scatter to agents for parallel, den put all dia answers together
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

To install di framework and start:

```bash
pip install agent-framework-core
# Optional integrations
pip install agent-framework-openai       # OpenAI and Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

You fit explore more for [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) and [official documentation](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Next agent framework we go check na [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). People dey call am "code-first" agent because e no dey work only with `strings`, e fit work with DataFrames for Python. Dis one beta well for data analysis and generation work. E fit be like to make graphs and charts or generate random numbers.

### State and Tools

To manage conversation state, TaskWeaver dey use `Planner`. Na LLM wey dey take request from users and plan out the tasks wey e suppose finish.

To finish tasks, `Planner` fit use tools wey dem dey call `Plugins`. Dis fit be Python classes or code interpreter. Dem plugins dey save as embeddings so LLM fit find correct plugin easy.

![Taskweaver](../../../translated_images/pcm/taskweaver.da8559999267715a.webp)

Dis na example of plugin wey dey handle anomaly detection:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Di code go check before e run am. Another thing to manage context for Taskweaver na `experience`. Experience go allow context of conversation to dey saved well for long time inside YAML file. You fit configure am make LLM improve on some tasks over time as e dey see old conversations.

## JARVIS

Last agent framework we go check na [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Wetin make JARVIS special be say e dey use LLM to manage `state` of conversation and di `tools` na other AI models. Each AI model specialize for certain task like object detection, transcription or image captioning.

![JARVIS](../../../translated_images/pcm/jarvis.762ddbadbd1a3a33.webp)

Di LLM, wey be general purpose model, na im dey receive request from user and identify the task and any data or arguments wey e need to finish am.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Di LLM go format di request so di specialized AI model go fit understand am, like JSON. After AI model don give answer based on task, LLM go receive di response.

If many models dey needed to finish the task, e go also interpret responses from those models before e come put am together to give answer to user.

Example below show how e dey work when user request description and count of objects wey dey photo:

## Assignment

To continue your AI Agents learning, you fit build with Microsoft Agent Framework:

- App wey go simulate business meeting with different departments for education startup.
- Create system messages to guide LLMs make dem sabi different personas and wahala dem get, and make user fit pitch new product idea.
- LLM go generate follow-up questions from each department to improve and make pitch and product idea beta

## Learning no stop here, continue your Journey

After you don finish dis lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to keep leveling up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->