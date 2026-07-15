[![Open Source Models](../../../translated_images/my/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## မိတ်ဆက်ခြင်း

AI Agents တွေဟာ Generative AI ကဏ္ဍမှာ ရွှေ့ပြောင်းတိုးတက်မှုစိတ်လှုပ်ရှားဖွယ်ရာအမျိုးအစားဖြစ်ပြီး၊ Large Language Models (LLMs) ကို အကူအညီပေးသူများမှ အသက်သွင်းနိုင်သော agent များအဖြစ် ဖွံ့ဖြိုးတိုးတက်စေပါသည်။ AI Agent ဖွဲ့စည်းမှုက developers များကို LLM များအတွက် tools နှင့် state စီမံခန့်ခွဲမှုများကို အသုံးပြုနိုင်စေရန် အက်ပလီကေးရှင်းများ ဖန်တီးနိုင်စေပါသည်။ ထို့အပြင် user များနှင့် developer များအား LLM များမှ စီစဉ်ထားသော လုပ်ဆောင်ချက်များကို လေ့လာကြည့်ရှုနိုင်ဖို့ မြင်သာမှုတိုးမြှင့်ပေးခြင်းမွ ်ဖြစ်သည်၊ ဒါဟာ အတွေ့အကြုံ စီမံခန့်ခွဲမှုကို တိုးကောင်းစေပါသည်။

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို ပညာပို့မှာဖြစ်ပါတယ်။

- AI Agent ဆိုတာ ဘာလဲ၊ AI Agent အကြောင်း နားလည်ခြင်း။
- AI Agent Frameworks ငါးမျိုးကို စူးစမ်းလေ့လာခြင်း၊ ထူးခြားချက်များ။
- AI Agent များကို အသုံးပြုသင့်သည့် နေရာများ၊ မည်သည့်အခါ အသုံးပြုသင့်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် သင်သည်:

- AI Agent များကို ရှင်းပြနိုင်ပြီး သူတို့အသုံးပြုမှုကို နားလည်နိုင်ပါလိမ့်မည်။
- လူကြိုက်များသော AI Agent Frameworks များရဲ့ ကွာခြားချက်များနှင့် မတူကွဲပြားမှုများကို နားလည်နိုင်ပါလိမ့်မည်။
- AI Agent များက မည်သို့လုပ်ဆောင်ကြောင်းနားလည်ပြီး အက်ပလီကေးရှင်းများ ဆောက်ရန် အသုံးပြုနိုင်ပါလိမ့်မည်။

## AI Agent များ ဆိုတာဘာလဲ?

AI Agent များဟာ Generative AI ကမ္ဘာကြီးအတွင်း စိတ်လှုပ်ရှားဖွယ် ကဏ္ဍတစ်ခုဖြစ်ပါတယ်။ ဒီစိတ်လှုပ်ရှားမှုကြောင့် အချိန်တစ်ချို့ စကားလုံးများနှင့် သုတေသနများမှာ ရှုပ်ထွေးမှုရှိနိုင်ပါတယ်။ AI Agent ကို ပြောဆိုရာမှာ ထည့်သွင်းစဉ်းစားသူအများစုအတွက် ရိုးရှင်းပြီး အပြင်အဆင်များကို ထည့်သွင်းစဉ်းစားရန် ဒီအဓိပ္ပါယ်ကို သုံးမှာဖြစ်ပါတယ်။

AI Agent များက Large Language Models (LLMs) ကို **state** နှင့် **tools** သုံးစွဲခွင့်ပေးခြင်းဖြင့် တစ်စိတ်တစ်ပိုင်းအလုပ်များ ပြုလုပ်နိုင်စေပါသည်။

![Agent Model](../../../translated_images/my/what-agent.21f2893bdfd01e6a.webp)

ဒီစကားလုံးများကို အဓိပ္ပါယ်ပေးလိုက်မယ်။

**Large Language Models** - ဒီဟာတွေက ဒီသင်ခန်းစာမှာ ဖော်ပြထားတဲ့ GPT-3.5, GPT-4, Llama-2 စတာတွေပါ။

**State** - ဒါဟာ LLM များ လုပ်ဆောင်နေသည့် အခြေအနေဖြစ်ပါတယ်။ LLM က မကြာသေးမီလုပ်ဆောင်ချက်များနဲ့ လက်ရှိလုပ်ဆောင်နေသော အခြေအနေကို အသုံးပြုပြီး နောက်လှည့်လုပ်ဆောင်ချက်များ ဆုံးဖြတ်တတ်ပါသည်။ AI Agent Frameworks တွေက ဒီအခြေအနေကို ထိန်းသိမ်းရာမှာ developer များကို အဆင်ပြေလွယ်ကူစေပါသည်။

**Tools** - အသုံးပြုသူတောင်းဆိုထားပြီး LLM က စီစဉ်ထားတဲ့ လုပ်ငန်းကို ပြီးမြောက်စေရန် Tools တွေလိုအပ်ပါတယ်။ Tools များအနေနဲ့ database တစ်ခု၊ API တစ်ခု၊ ပြင်ပအက်ပလီကေးရှင်းတစ်ခု သို့မဟုတ် တခြား LLM တစ်ခုဖြစ်နိုင်ပါတယ်။

ဒီအဓိပ္ပါယ်တွေက မကြာခဏ ဆက်လက်ကြည့်ရှုတွေ့ကြုံနေမယ့် AI Agent များ တည်ဆောက်ပုံနဲ့တဲ့အခါ ကောင်းမွန်အခြေခံတည်ဆောက်မှု ပေးစေနိုင်ပါလိမ့်မယ်။ အခု အနည်းငယ်ကွဲပြားတဲ့ AI Agent framework များကို စူးစမ်းကြည့်ကြမယ်။

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) က ကျွန်တော်တို့ ယခင်အဓိပ္ပါယ်ပေးထားတဲ့ အကြောင်းအရာတွေအပေါ် တည်ဆောက်ထားတာပါ။

**state** ကို စီမံရန် `AgentExecutor` လို့ခေါ်တဲ့ built-in function တစ်ခုကို အသုံးပြုပါတယ်။ ဒါက သတ်မှတ်ထားတဲ့ `agent` နဲ့ ရနိုင်တဲ့ `tools` တွေကို လက်ခံပါတယ်။

`Agent Executor` က chat သမိုင်းဇယားကိုလည်း သိမ်းဆည်းထားပြီး chat context ကို ပံ့ပိုးပေးပါတယ်။

![Langchain Agents](../../../translated_images/my/langchain-agents.edcc55b5d5c43716.webp)

LangChain မှာ [တင့်တယ်တဲ့ tools စုစည်းမှု](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ရှိပြီး ကိုယ့်အက်ပလီကေးရှင်းထဲသို့ import လုပ်နိုင်ပြီး LLM က access ရစေပါတယ်။ ဒီ tools တွေကို ပြုလုပ်သူများနဲ့ LangChain အဖွဲ့က ဖန်တီးထားသော tools များဖြစ်ပါသည်။

ထို့နောက် ဒီ tools တွေကို သတ်မှတ်ပြီး `Agent Executor` ကို ပေးပို့နိုင်ပါသည်။

AI Agents တွေကို ဆိုတဲ့အခါ မြင်သာမှုက အရေးကြီးတဲ့ အရာတစ်ခုဖြစ်ပါတယ်။ Application developer များအနေနဲ့ LLM ဘယ် tool ကို ဘာကြောင့် အသုံးပြုနေသည်ကို နားလည်ရပါမယ်။ အဲဒီအတွက် LangChain အဖွဲ့က LangSmith ကို ဖန်တီးထားပါတယ်။

## AutoGen

နောက်တစ်ခု ဆွေးနွေးမည့် AI Agent framework ကတော့ [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst) ပါ။ AutoGen ရဲ့ အဓိက ဦးတည်ချက်က စကားပြောခြင်းဖြစ်ပါတယ်။ Agents များဟာ **စကားပြောနိုင်ပြီး** ပုံစံပြင်နိုင်ပါတယ်။

**စကားပြောနိုင်ခြင်း** - LLM များက တစ်ခြား LLM နဲ့ စကားပြောစတင်နိုင်ပြီး တစ်ဆက်တည်း ဆက်လက်ပြောဆိုနိုင်ပါတယ်၊ လုပ်ငန်းကို ပြီးမြောက်စေရန်ဖြစ်သည်။ ဒါကို `AssistantAgents` ကို ဖန်တီးထားပြီး စနစ်စာသား (system message) သတ်မှတ်ပေးခြင်းဖြင့် ပြုလုပ်ပါတယ်။

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**စိတ်ကြိုက်ပြင်နိုင်ခြင်း** - Agent များကို LLM အဖြစ်တင်မက User သို့မဟုတ် Tool အဖြစ်လည်း သတ်မှတ်နိုင်ပါတယ်။ Developer အနေနဲ့ `UserProxyAgent` ကို သတ်မှတ်နိုင်ပြီး၊ ဒီ Agent က user နဲ့ feedback ဖြင့် ဆက်ဆံရေးထားပြီး လုပ်ငန်းစတင်ဆောင်ရွက်မှုကို ဆက်လက်လုပ်ဆောင်သည်ဟုတ်၊ ရပ်ဆိုင်းသည်ဟုတ် ဆုံးဖြတ်ပေးနိုင်ပါတယ်။

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### State နှင့် Tools

စတိတ်ပြောင်းလဲမှုနဲ့ စီမံခန့်ခွဲမှုအတွက် assistant Agent က Python code ကို ထုတ်လုပ်ပြီး လုပ်ငန်းကို ပြီးမြောက်စေပါသည်။

ဒီကိစ္စကို ဥပမာအားဖြင့် ပြပါမယ်။

![AutoGen](../../../translated_images/my/autogen.dee9a25a45fde584.webp)

#### စနစ်စာသားဖြင့် သတ်မှတ်ထားသော LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

ဒီစနစ်စာသားက LLM အထူးသတ်မှတ် လုပ်ငန်းဆောင်တာတွေအတွက် စနစ်ကို ဦးတည်ညွှန်ပြသည်။ AutoGen ကိုသုံး၍ အသားတင်ထားသော AssistantAgents များစွာဖြင့် စနစ်စာသားတွေကွဲပြားစွာ အသုံးပြုနိုင်သည်။

#### User ကနေ စတင်သော စကားပြောခြင်း

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

User_proxy (လူ) ထံမှ စကားလုံး အဲဒါကြောင့် Agent က လုပ်ဆောင်ရမယ့် function တွေကို ရှာဖွေလေ့လာဖို့ စတင်သည်။

#### Function တစ်ခုကို လုပ်ဆောင်ခြင်း

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

ပထမဆုံး စကားပြောချက် ပြီးမြောက်ပြီးနောက် Agent က သတ်မှတ်ထားသော tool ကို အကြံပြုကြောင်း ပို့ပါမည်၊ ဒီေနရာမှာ `get_weather` ဆိုတဲ့ function ဖြစ်ပါတယ်။ သင့်စနစ်ပုံစံအရ ဒီ function ကို အလိုအလျောက် လုပ်ဆောင်နိုင်ကာ Agent ကဖတ်ရှုမှုရရှိတတ်သည်၊ မဟုတ်လျှင် user input မူတည်ပြီး လုပ်ဆောင်ပေးရပါမည်။

ပိုမိုလေ့လာရန်အတွက် [AutoGen code နမူနာများ](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုနိုင်ပါသည်။

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) သည် Microsoft ၏ အခမဲ့ SDK ဖြစ်ပြီး AI Agents နှင့် multi-agent စနစ်များကို **Python** နှင့် **.NET** နှစ်မျိုးစလုံးဖြင့် တည်ဆောက်နိုင်မည့် framework ဖြစ်သည်။ ဒီ framework သည် Microsoft ၏ နောက်ဆုံးပေါ် project နှစ်ခုဖြစ်သည့် **Semantic Kernel** ၏ စီးပွားရေးဆိုင်ရာ အင်္ဂါရပ်များနှင့် **AutoGen** ၏ multi-agent စနစ်ကို ပေါင်းစပ်ထားပြီး single framework တစ်ခုအဖြစ် ကျင်းပထားသည်။ AutoGen ၏ အဆက်သတင်းအဖြစ် အခုမှ စတင်တဲ့ Agent project များအတွက် ဒီ framework ကို အကြံပြုပါသည်။

ဒီ framework က single **chat agent** မှစ၍ ရှုပ်ထွေးသော **multi-agent workflow** အထိ ဖြန့်ချိသည်။ Microsoft Foundry, Azure OpenAI နှင့် OpenAI တို့နှင့် တိုက်ရိုက်ပေါင်းစည်းထားသည်။ OpenTelemetry မှတဆင့် Built-in observability ကို ပေးပြီး agents များ၏ လုပ်ဆောင်ချက်များကို အတိအကျနားလည်နိုင်စေသည်။

### State နှင့် Tools

**State** - Framework က အသုံးပြုသူနှင့် စကားဝိုင်း context ကို **threads** မှတဆင့် စီမံသည်။ Agent က စကားပြောသမိုင်း (အသုံးပြုသူတောင်းဆိုမှုများ၊ tool ခေါ်ဆိုမှုများ၊ ဆာလီလ်) အား ထိန်းသိမ်းထားပြီး turns တစ်ခုချင်းစီမှာ ယခင် turns များကို အခြေခံသည်။ Threads များကို တိုက်ရိုက် သိုလှောင်ထားပြီး စကားဝိုင်း ပြန်စဖွင့်ရန် ခွင့်ပြုသည်။

**Tools** - Agent သို့ Tools များကို အခြေခံ Python function များဖြင့် ပေးနိုင်ပါသည်။ Type-annotated parameters များကို schema အဖြစ် အလိုအလျော့ ပြောင်းလဲပြီး model သည် ဘယ်လိုနဲ့ ဘယ်အချိန်ခေါ်ဆိုမလဲ သိရှိစေသည်။ Framework က Model Context Protocol (MCP) servers နှင့် hosted tools များ (code interpreter အသေးစိတ်) ကိုလည်း ထောက်ပံ့သည်။

ဒီမှာ custom tool ပါတဲ့ single agent ရဲ့ ဥပမာတစ်ခုရှိသည်။

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

Microsoft Foundry မှ Azure OpenAI ကို ချိတ်ဆက်ရန် အစား၊ endpoint နှင့် credentials များကို client သို့ ပေးပို့ပါ။

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

Framework ဟာ အတဲ့အရာမှာအခြား agent တွေကို တစ်ခုချင်းစီ နောက်တစ်ခုဆက်ပြီး လုပ်ကိုင်ခိုင်းတာ (context များ လွှဲပြောင်းခြင်း) သို့မဟုတ် agent များစွာကို တပြိုင်နက် မျှဝေပေးပြီး သူတို့ရဲ့ ရလဒ်များကို စုစည်းပြည့်စုံစေခြင်း အတွက် အထူးကောင်းမွန်သည်။

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# နောက်ဆက်လက်အသွားအလာအဖြစ် ကိုယ်စားလှယ်များကို လည်ပတ်ပါ၊ စကားပြောဆိုမှု အကြောင်းအရာကို ချိတ်ဆက်ပါ။
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# ကိုယ်စားလှယ်များကို တပြိုင်နက်စီ ဖြန့်ချိပြီး၊ ၎င်းတို့၏ တုံ့ပြန်ချက်များကို စုစည်းပါ။
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Framework ကိုထည့်သွင်းပြီး စတင်အသုံးပြုရန်--

```bash
pip install agent-framework-core
# ရွေးချယ်စရာ ပေါင်းစည်းမှုများ
pip install agent-framework-openai       # OpenAI နှင့် Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

[Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) နှင့် [တရားဝင်စာတမ်းများ](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) များကို ပိုမိုလေ့လာနိုင်သည်။

## Taskweaver

နောက်တစ်ခု စူးစမ်းမည့် agent framework ကတော့ [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) ဖြစ်ပြီး “code-first” agent လို့ လူသိများသည်။ `strings` အသုံးပြုမှု အစား Python DataFrames တွေနဲ့အလုပ်လုပ်နိုင်ပါတယ်။ ဒါက data analysis နဲ့ generation လုပ်ငန်းအတွက် အထူးအသုံးဝင်ပြီး ဂရပ်နဲ့ဇယားဖန်တီးခြင်း သို့မဟုတ် စံတော်ချိန်နံပါတ်တွေထုတ်ယူခြင်း စတာတွေလုပ်ဖို့ အသုံးဝင်ပါတယ်။

### State နှင့် Tools

စကားပြောအခြေအနေကို စီမံရန် TaskWeaver က `Planner` ဆိုတဲ့အယူအဆကိုသုံးတယ်။ `Planner` ဆိုတာဟာ အသုံးပြုသူတောင်းဆိုချက်တွေကို လက်ခံပြီး လုပ်ငန်းလိုအပ်ချက်တွေကို အစီအစဉ်ပြုစုတဲ့ LLM ပါ။

လုပ်ငန်းများကို ပြီးမြောက်စေရန် `Planner` ကို `Plugins` ဆိုတဲ့ tool စုဆောင်းမှုပေးတယ်။ ဒါတွေဟာ Python class များ သို့မဟုတ် စက် code ရှင်းလင်းစနစ်တွေ ဖြစ်နိုင်သည်။ ဒီ plugins တွေကို embedding အဖြစ် သိမ်းဆည်းထားတာကြောင့် LLM က درست plugin ရှာဖွေရာမှာ တိုးတက်ကောင်းမွန်ပြီး ရှာဖွေတတ်စေသည်။

![Taskweaver](../../../translated_images/my/taskweaver.da8559999267715a.webp)

Anomaly detection ကို ကိုင်တွယ်ရန် plugin ဥပမာတစ်ခုရှိသည်။

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

ကုဒ်ကို 실행하기မပြုလုပ်ခင် စစ်ဆေးပါသည်။ Taskweaver မှာ context ကို စီမံရန် `experience` ဆိုတဲ့ feature တစ်ခုရှိသည်။ Experience က YAML ဖိုင်ထဲမှာ စကားပြော context ကို ကြာရှည်သိမ်းဆည်းနိုင်ပြီး LLM က ဒီအရည်အချင်းကို အချိန်ကြာလာတာနဲ့ တိုးတက်လာစေသည်။

## JARVIS

နောက်ဆုံး agent framework ကတော့ [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) ဖြစ်ပြီး JARVIS ၏ ထူးခြားချက်က စကားပြောအခြေအနေ (`state`) ကို စီမံရန် LLM ကို အသုံးပြုခြင်းနှင့် `tools` အဖြစ် အခြား AI မော်ဒယ်များကို အသုံးပြုခြင်း ဖြစ်သည်။ AI မော်ဒယ်တိုင်းသည် အထူးပြုလုပ်ချက်များ လုပ်ဆောင်သော အထူးပြု မော်ဒယ်များဖြစ်ပြီး အရာဝတ္ထု မှတ်တမ်းတင်ခြင်း၊ အသံစာတမ်းပြုခြင်း သို့မဟုတ် ပုံလေး ဆွဲခြင်း စသည်တို့ဖြစ်သည်။

![JARVIS](../../../translated_images/my/jarvis.762ddbadbd1a3a33.webp)

အထူးပန်းတိုင် မော်ဒယ်များကို အသုံးပြုရန် LLM ဟာ အသုံးပြုသူ၏ တောင်းဆိုမှုကို လက်ခံပြီး အထူးပြု လုပ်ငန်းနဲ့ လိုအပ်သောဒေတာ/အချက်အလက်များကို ထုတ်ဖော်သိမြင်သည်။

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM က ထိုတောင်းဆိုမှုကို အထူးပန်းတိုင်မော်ဒယ် က နားလည်နိုင်ဖို့ JSON သို့နှင့် ပြောင်းထားသည်။ AI မော်ဒယ်က လုပ်ငန်းအောက်တွင်ခံယူချက် ပြန်ပေးလာပါက LLM က အဲဒီဖြေကြားချက်ကို လက်ခံပါသည်။

လုပ်ငန်း ပြီးမြောက်ဖို့ မော်ဒယ်များစွာလိုအပ်ပါက ဒီ model တွေရဲ့ ဖြေကြားချက်များအား စုစည်းပြီး အသုံးပြုသူလာတဲ့ ဖြေကြားချက် ထုတ်ဖော်ရန် ပြင်ဆင်သည်။

ဥပမာအောက်မှာ အသုံးပြုသူက ပုံထဲမှာ အရာဝတ္ထုများ၏ ဖော်ပြချက်နှင့် အရေအတွက်ကို တောင်းဆိုတဲ့ အခါ ဒီလိုပုံစံဖြင့် ဆောင်ရွက်မည်ကို မြင်ရပါမည်။

## လုပ်ငန်းစီမံကိန်း

AI Agents သင်ယူမှုကို ဆက်လက်တိုးတက်ရန် Microsoft Agent Framework ဖြင့် အောက်ပါအတိုင်း application တစ်ခု တည်ဆောက်ပါ။

- ပညာရေး စတားတပ်တစ်ခု၏ ကဏ္ဍများအကြား စီးပွားရေး ဆွေးနွေးပွဲကို အတုလုပ်ထားသော အက်ပလီကေးရှင်း။
- LLM များကို မတူသောပုဂ္ဂိုလ်များနှင့် ဦးစားပေးချက်များ နားလည်စေရန် စနစ်စာသားများ ဖန်တီးပြီး အသုံးပြုသူကို ထုတ်ကုန်အသစ် ဝင်ငွေ ဆွေးနွေးခွင့် ပေးပါ။
- LLM က အဆိုပြုထားသော ထုတ်ကုန်အကြံပြုမှုကို တိုင်းတာ ရှေးရွေးကောက်ချက်များဖန်တီးရန် ဝန်ကြီးဌာန တစ်ခုစီထံမှ တုံ့ပြန်မေးခွန်းများ ထုတ်လုပ်ပါ။

## သင်ယူခြင်း ဒီမှာ မရပ်ပါနဲ့၊ ခရီးစဉ်ကို ဆက်လက်ပါ

ဒီသင်ခန်းစာပြီးလျှင် ကျွန်ုပ်တို့ရဲ့ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပြီး Generative AI ဗဟုသုတကို ဆက်လက်မြှင့်တင်နိုင်ပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->