[![Open Source Models](../../../translated_images/my/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## နိဒါန်း

AI Agents သည် Generative AI အတွက် စိတ်လှုပ်ရှားဖွယ်ဖြစ်ပြီး၊ Large Language Models (LLMs) ကို အကူအညီပေးသူမှ တက်ကြွလှုပ်ရှားခွင့်ရှိသည့် သက်ဆိုင်သူအဖြစ် ဖွံ့ဖြိုးတိုးတက်စေပါသည်။ AI Agent Framework များသည် developer များအနေဖြင့် LLMs များကို tool များနှင့် state စီမံခန့်ခွဲမှု အလွယ်တကူ အသုံးပြုနိုင်စေရန် အက်ပ်လီကေးရှင်းများ ဖန်တီးနိုင်စေသည်။ ထို့အပြင် user နှင့် developer များအား LLMs မှ ကြိုတင်အစီအစဉ်ရေးဆွဲထားသော လှုပ်ရှားမှုများကို ကြည့်ရှု စစ်ဆေးနိုင်သော ဝါရင့်နေရာလုံခြုံမှုကို တိုးတက်စေပြီး အသုံးပြုမှုကို မျှတစွာ စီမံခန့်ခွဲနိုင်စေပါသည်။

ဒီသင်ခန်းစာတွင် အောက်ပါအချက်များကို ဖတ်ရှု လေ့လာသွားမှာ ဖြစ်ပါတယ်။

- AI Agent ဆိုတာ ဘာလဲဆိုတာ နားလည်ခြင်း - AI Agent ဆိုတာ မည်သည်နည်း?
- AI Agent Framework ပေါင်း ၅ မျိုးကို ရှင်းလင်းခြင်း - ၎င်းတို့သည် ဘာကြောင့်ထူးခြားသနည်း?
- AI Agents များကို အသုံးပြုနိုင်သော ကိစ္စများတွင် လျှောက်ထားခြင်း - ဘယ်အချိန်တွင် AI Agents များကို အသုံးပြုသင့်သနည်း?

## သင်ယူစရာ ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက် သင်သည်:

- AI Agents ဆိုတာ ဘာလဲ၊ ဘယ်လိုအသုံးပြုနိုင်လဲ ဆိုတာကိုရှင်းပြနိုင်ပါမည်။
- လူကြိုက်များသော AI Agent Framework များအနက် တချို့၏ကွာခြားချက်များနားလည်နိုင်မည်။
- AI Agents များသည် ဘယ်လိုလုပ်ဆောင်ကြသည်ကို နားလည်သဘောပေါက်၍ လျှောက်လွှာများ ဖန်တီးနိုင်မည်။

## AI Agents ဆိုတာ မည်သည်နည်း?

AI Agents သည် Generative AI အတွင်း အလွန်စိတ်လှုပ်ရှားဖွယ် အရာဖြစ်သည်။ သိုသော် စကားလုံးအသုံးအနှုန်းနှင့် ဤ တီထွင်မှုများ၏ အသုံးချမှုအပေါ် အချိန်အခါအားဖြင့် မပေါက်ကြားမှုတွေရှိတတ်သည်။ AI Agents ဟုအမည်ပေးသော အသုံးအနှုန်းများကို ရိုးရှင်းပြီး အများအားလုံးပါဝင်သော စကားသတ်မှတ်ချက်တစ်ခုကို အသုံးပြုသွားမည်ဖြစ်သည်။

AI Agents သည် Large Language Models (LLMs) များကို **state** နှင့် **tools** များ အသုံးပြု၍ လုပ်ဆောင်နိုင်စေပါသည်။

![Agent Model](../../../translated_images/my/what-agent.21f2893bdfd01e6a.webp)

အောက်ပါ စကားလုံးများကို သတ်မှတ်ကြရအောင်။

**Large Language Models** - ဒီသင်ခန်းစာတွင် အကြောင်းပြုသော မော်ဒယ်များမှာ GPT-5, GPT-4o နှင့် Llama 3.3 စသဖြင့် ဖြစ်ပါသည်။

**State** -  မည်သည့် context သို့ LLM သည် လုပ်ဆောင်နေသည်ကို ရည်ညွှန်းသည်။ LLM သည် ၎င်း၏ ယခင် လှုပ်ရှားမှုများနှင့် လက်ရှိ context ကို အသုံးပြု၍ နောက်ထပ် လုပ်ဆောင်ချက်များအတွက် ဆုံးဖြတ်မှု လမ်းပြသည်။ AI Agent Framework များသည် developer များအတွက် ထို context ကို ပိုမိုလွယ်ကူစွာ စီမံခန့်ခွဲနိုင်ရန် အထောက်အကူပြုပါသည်။

**Tools** - user ၏ တောင်းဆိုမှုနှင့် LLM ၏ စီစဉ်ထားသော အလုပ်အကိုင်များကို ပြည့်မှီအောင် ဖော်ဆောင်ရန် လိုအပ်သော tools များကို ရယူရမည်။ ဥပမာ တချို့မှာ ဒေတာဘေ့စ်၊ API၊ ပြင်ပအက်ပ်လီကေးရှင်း သို့မဟုတ် အခြား LLM တစ်ခုဖြစ်နိုင်သည်။

အဆိုပါစကားသတ်မှတ်ချက်များသည် နောက်တည့်နေ့တွင် ၎င်းတို့ ဘယ်လို အကောင်အထည်ဖော်ကြောင်း စူးစမ်းရှာဖွရာတွင် များစွာ အခြေခံအချက်များ ပေးနိုင်မည်ဟု မျှော်လင့်ပါတယ်။ AI Agent Framework များအနည်းငယ်ကို စူးစမ်းကြည့်ရအောင် -

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) သည် အထက်ဖော်ပြပါသတ်မှတ်ချက်များကို တက်ရောက်ပုံဖော်ပြချက်တစ်ခုဖြစ်သည်။

**state** ကို စီမံရန်အတွက် `AgentExecutor` ဟုခေါ်သော built-in function ကို အသုံးပြုသည်။ ၎င်းသည် သတ်မှတ်ထားသော `agent` နှင့် ရနိုင်သော `tools` များကို လက်ခံသည်။

`Agent Executor` သည် chat မှတ်တမ်းအကြောင်းအရာကိုလည်းသိမ်းဆည်းထားပြီး၊ chat context ကို ပံ့ပိုးပေးသည်။

![Langchain Agents](../../../translated_images/my/langchain-agents.edcc55b5d5c43716.webp)

LangChain သည် LLM အား access ရစေရန် သင့်အက်ပ်လီကေးရှင်းထဲသို့ ထည့်သွင်းနိုင်သော [tool များ का ကတ်တလော့](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ကို ပေးသည်။ ၎င်းထုတ်လုပ်မှုများကို အဖွဲ့အစည်းနှင့် LangChain အဖွဲ့တို ့မှ ဖန်တီးထားသည်။

ထို tools များကို သတ်မှတ်ပြီး `Agent Executor` ထံ ပို့ပါ။

AI Agents အကြောင်း စကားပြောရာတွင် Visibility သည် အရေးပါတဲ့အချက်တစ်ခုဖြစ်ပြီး၊ application developer များအနေဖြင့် LLM ဘယ် tool ကို အသုံးပြုနေသည်ကို နားလည်ရန် အရေးကြီးပါသည်။ ထို့ကြောင့် LangChain အဖွဲ့သည် LangSmith ကို ဖန်တီးထားသည်။

## AutoGen

နောက်တစ်ခု မိတ်ဆက်မည့် AI Agent framework သည် [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst) ဖြစ်သည်။ AutoGen ၏ အဓိကအာရုံစိုက်ချက်မှာ စကားပြောခြင်းဖြစ်သည်။ Agents များသည် **စကားပြောနိုင်**ပြီး **စိတ်ကြိုက်ပြင်ဆင်နိုင်**ပါသည်။

**စကားပြောနိုင်ခြင်း -** LLM များသည် တစ်ခုချင်း LLM နှင့် စကားပြော၍ လုပ်ရမည့် အလုပ်ကို ပြီးဆုံးစေနိုင်သည်။ ၎င်းသည် `AssistantAgents` များ ဖန်တီးပြီး အထူးပြု system message ကို ပေးခြင်းဖြင့် ဖြစ်သည်။

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**စိတ်ကြိုက်ပြင်ဆင်နိုင်ခြင်း** - Agents များကို LLM များအဖြစ်သာမက user သို့မဟုတ် tool အဖြစ် မည်သည့် developer မှ မဆို ရေးဆွဲနိုင်သည်။ developer များအနေနှင့် တာဝန်ယူသော `UserProxyAgent` ကို သတ်မှတ်နိုင်ပြီး၊ ၎င်းသည် user မှ တုံ့ပြန်ချက်ရယူ၍ task ပြီးစီးမှုအတွက် အကြံပြုရန် အတွက် ဖြစ်သည်။ ဒီ feedback သည် task လုပ်ငန်း ဆက်လက်ဆောင်ရွက်ခြင်း သို့မဟုတ် ရပ်နားခြင်း တို့ဖြစ်နိုင်သည်။

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### State နှင့် Tools

state ကို ပြောင်းလဲ စီမံရန်အတွက် assistant Agent သည် Python code တစ်ခု ဖန်တီးပြီး အလုပ် ပြီးဆုံးပါသည်။

ဒီလုပ်ငန်းစဉ်၏ ဥပမာဖြစ်သည် -

![AutoGen](../../../translated_images/my/autogen.dee9a25a45fde584.webp)

#### LLM ကို System Message ဖြင့် သတ်မှတ်ခြင်း

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

ဒီ system message သည် ထို LLM သတ်မှတ်ထားသော လုပ်ငန်းများအတွက် ဘာ function များ သင့်လျော်ကြောင်းညွှန်ပြသည်။ AutoGen ဖြင့် သင်သည် แตกต่างသော မတူညီသော system messages များရသော AssistantAgents များ များစွာ သတ်မှတ်နိုင်သည်။

#### အသုံးပြုသူမှ စကားပြောခြင်း စတင်ခြင်း

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

user_proxy (လူ့မက်ဆေ့ခ်ျ) မှ ဒီမက်ဆေ့ခ်ျသည် Agent စတင် လုပ်ဆောင်ရန် လုပ်ငန်းစဉ်ကို စတင်ခြင်းဖြစ်သည်။

#### Function ကို အကောင်အထည်ဖော်ခြင်း

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

စတင်သော chat ကို ပြုလုပ်ပြီးနောက် Agent သည် ခေါ်ဆိုရန်အတွက် အကြံပြု tool ကို ရိုက်ချက်ပေးပါသည်။ ဤအမှုအတွက် သည်သည် `get_weather` ဟုခေါ်သော function တစ်ခုဖြစ်သည်။ သင်၏ configuration အပေါ်မူတည်၍ ၎င်း function ကို Agent မှ မလိုလားဘဲ အလိုအလျောက် တင်နိုင်သလို၊ user input ဖြင့် ရုပ်သိမ်းပါလိမ့်မည်။

[AutoGen code နမူနာများ](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) ကို ဘယ်လိုတည်ဆောက်မလဲဆိုတာ အကောင်းဆုံးလေ့လာနိုင်ပါသည်။

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) သည် Microsoft ၏ AI Agent များနှင့် multi-agent systems များကို **Python** နှင့် **.NET** တို့ဖြင့် တည်ဆောက်နိုင်သော open-source SDK ဖြစ်သည်။ ၎င်းသည် Microsoft ၏ ယခင် project များဖြစ်သော **Semantic Kernel** ၏ စီးပွားရေးလုပ်ငန်း features များနှင့် **AutoGen** ၏ multi-agent ထိန်းချုပ်မှုတို့ကို ပေါင်းစည်းထားသည်။ ယနေ့တွင် agent project အသစ် စတင်ရန် AutoGen ၏ နောက်လမ်းကြောင်းအဖြစ် အကြံပြုသည်။

၎င်း framework သည် တစ်ခုတည်းသော **chat agent** မှ စ၍ ခက်ခဲတော်တဲ့ **multi-agent workflow** များအထိ အလွယ်တကူ တိုးတက်နိုင်ပြီး Microsoft Foundry, Azure OpenAI, နှင့် OpenAI တို့နှင့် တိုက်ရိုက် ပေါင်းစပ်ထားသည်။ OpenTelemetry ဖြင့် ဆောင်ရွက်မှု အတိအကျ ပြန်ကြည့်သိရှိနိုင်မှုကိုလည်း ပံ့ပိုးသည်။

### State နှင့် Tools

**State** - framework သည် **threads** အားဖြင့် စကားပြော context ကို စီမံသည်။ agent များသည် မက်ဆေ့ခ်ျမှတ်တမ်း (user တောင်းဆိုချက်များ၊ tool ခေါ်ဆိုချက်၊ နှင့် ၎င်းတို့ရလဒ်များ) ကို ထိန်းသိမ်းထားပြီး turn တစ်ခုပြီး turn နောက်က ဆက်ခံသည်။ Threads များကို ထိန်းသိမ်းပြီး စကားပြောမှုကို ပိတ်ထား၍ ပြန်စတင်နိုင်သည်။

**Tools** - Python function များကို တိုက်ရိုက် agent များသို့ ပေးပို့သည်။ Type-annotated parameter များကို schema ဖန်တီး စက်တင်ဖြစ်သဖြင့် မော်ဒယ်သည် ဘယ်အချိန်နှင့် ဘယ်လိုခေါ်လို့ရမည်ကို သိပါသည် (function calling)။ framework သည် Model Context Protocol (MCP) server များနှင့် hosted tool များ (အနုပညာကုဒ် interpreter ကိုပါ) အား ပံ့ပိုးပေးသည်။

ဒီမှာ လုပ်ငန်း တစ်ခုနှင့် custom tool တစ်ခု ပါဝင်သော agent ဥပမာရှိသည်။

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

Microsoft Foundry ၏ Azure OpenAI နှင့် ဆက်သွယ်ရန် client သို့ endpoint နှင့် credentials ပေးပို့ပါ။

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

ဒီ framework ၏ ထူးခြားမှုမှာ 여러 agent များကို တစ်ပြိုင်နက် တွဲညှိခြင်းဖြစ်သည်။ ဥပမာ agent များကို တစ်ချိန်တည်းတွင် တစ်ခုချင်းလှည့်လုပ်ခြင်း( တစ်ခု၏ context ကို နောက်တစ်ခုသို့ ပို့ခြင်း) သို့မဟုတ် agent များစွာ parallel တင်လုပ်ပြီး ၎င်းတို့ရလဒ်များ ကို စုစည်းခြင်းဖြစ်သည်။

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# ကိုယ်စားလှယ်များကို တန်းလိုက် အပ်နှံပြီး၊ စကားပြော ဆက်စပ်မှုကို ဆက်လက် ပေးပို့သည်
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# ကိုယ်စားလှယ်များကို တပြိုင်နက် အဖြန်ထုတ်ပြီး၊ ၎င်းတို့၏ တုံ့ပြန်ချက်များကို စုပေါင်းသည်
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Framework ကို install ပြီး စတင်လိုက်ပါ -

```bash
pip install agent-framework-core
# ရွေးချယ်စရာပေါင်းစည်းမှုများ
pip install agent-framework-openai       # OpenAI နှင့် Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

[Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) နှင့် [တရားဝင်စာရွက်စာတမ်း](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) တွင် ပိုမိုလေ့လာနိုင်သည်။

## Taskweaver

နောက်တစ်ခု အကြောင်းဖေါ်ပြမည့် agent framework သည် [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst) ဖြစ်သည်။ ၎င်းကို "code-first" agent ဟု ခေါ်ကြပြီး `strings` ဖြင့်သာ မဟုတ် DataFrames များဖြင့် Python အတွင်း လုပ်ဆောင်နိုင်သည်။ ဒါက data analysis နှင့် ကြိုတင်ထုတ်လုပ်မှုလုပ်ငန်းများတွင် အလွန်အသုံးဝင်သည်။ ဥပမာ လက်တွေ့ သို့မဟုတ် ဖန်တီးတာသည် graphs နှင့် charts တည်ဆောက်ခြင်း သို့မဟုတ် ကျပ်တည်းဟုတွင် random number များ ဖန်တီးခြင်းဖြစ်နိုင်သည်။

### State နှင့် Tools

စကားပြောမှု State ကို စီမံရန် TaskWeaver သည် `Planner` အယူအဆကို သုံးသည်။ `Planner` သည် LLM တစ်ခုဖြစ်ပြီး user မှ တောင်းဆိုမှုကို ဖမ်းယူထားပြီး ပြီးစီးရမည့် task များကို ရှာဖွေ စီမံသည်။

task များကို ပြီးဆုံးရန် `Planner` သည် `Plugins` ဟုခေါ်သော tool များစုစည်းမှုအတွက်ဖွင့်ပေးသည်။ ၎င်းသည် Python classes သို့မဟုတ် ဝေါဟာရ interpreter များဖြစ်နိုင်သည်။ Plugins များကို embeddings အဖြစ်သိမ်းဆည်းထားပြီး LLM သည် မှန်ကန်သော plugin ကို အလွယ်တကူ ရှာဖွေနိုင်ပါသည်။

![Taskweaver](../../../translated_images/my/taskweaver.da8559999267715a.webp)

အောက်ပါမှာ anomaly detection ကို ကိုင်တွယ်သည့် plugin ၏ ဥပမာဖြစ်သည် -

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

ကုဒ်သည် တည်ဆောက်ခြင်းမတိုင်မှီ စစ်ဆေးသည်။ Taskweaver ထဲတွင် context စီမံရန်နောက်ထပ် function တစ်ခုမှာ `experience` ဖြစ်သည်။ Experience သည် စကားပြော context ကို YAML ဖိုင်တစ်ခုတွင် ကြာရှည်သိမ်းထားခြင်းဖြစ်သည်။ ၎င်းကို configure ပြုလုပ်၍ LLM သည် ယှဉ်တွဲစကားပြောမှုများကို ပုသိပ်လေ့လာ၍ အချိန်အတောအတွင်း တိုးတက်မြှင့်တင်နိုင်သည်။

## JARVIS

နောက်ဆုံး agent framework သည် [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst) ဖြစ်သည်။ JARVIS ၏ထူးခြားချက်မှာ LLM သည် စကားပြော **state** ကို စီမံခြင်း ဖြစ်ပြီး `tools` များမှာ အခြား AI မော်ဒယ်များ ဖြစ်သည်။ AI မော်ဒယ်တိုင်းမှာ သတ်မှတ်ထားသော အလုပ်များကို လုပ်ဆောင်သော အထူးပြု မော်ဒယ်များဖြစ်သည်၊ ဥပမာ object detection, transcription သို့မဟုတ် image captioning ပါ။

![JARVIS](../../../translated_images/my/jarvis.762ddbadbd1a3a33.webp)

LLM သည် ပုံမှန်ဒီဇိုင်းမော်ဒယ်ဆိုပြီး user မှ တောင်းဆိုမှုကို လက်ခံကာ သတ်မှတ်ထားသော task နှင့် အကျိုးဝါး/ဒေတာများကို ခွဲခြားထားသည်။

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM သည် request ကို specialized AI မော်ဒယ် အား သိမ်းထားသော ပုံစံဖြစ် JSON အနေဖြင့် ပြောင်းလဲလုပ်ဆောင်ပါသည်။ AI မော်ဒယ်အနေဖြင့် အလုပ်ဆောင်ပြီး ရလဒ် များကလည်း LLM သို့ ပြန်သွားသည်။

အလုပ်ပြီးစီးရန် မော်ဒယ်များစွာ ခေါ်ရန်လိုလျှင် ဤ model များမှရရှိသော ဖြေကြောင်းများကို စုစည်းညှိနှိုင်းကာ user တွင် တုံ့ပြန်ချက် ထုတ်ပေးသည်။

အောက်ပါ ဥပမာတွင် user တစ်ဦးမှ ဓာတ်ပုံရှိ objects များ၏ ဖော်ပြချက်နှင့် အရေအတွက် တောင်းဆိုသည့် နည်းလမ်းကို ဖော်ပြသည်။

## လုပ်ငန်းတာဝန်

AI Agents ကို ဆက်လက်လေ့လာရန် Microsoft Agent Framework ဖြင့် အောက်ပါအတိုင်း အက်ပ် တစ်ခု တည်ဆောက်ပါ -

- ပညာရေး စတိတ်တစ်ခု၏ ကွဲပြားသော ဌာနများနှင့် စီးပွားရေး အစည်းအဝေးကို နမူနာပြုကြည့်ရန်။
- LLM များကို မတူညီသော persona များနှင့် ဦးစားပေးချက်များ ဆိုင်ရာ ဒီဇိုင်း system message များ ဖန်တီးပြီး အသုံးပြုသူအား ထုတ်ကုန်အကြံပြု မှတ်ချက် တင်နိုင်စေပါ။
- ထို့နောက် 各ဌာနမှ follow-up မေးခွန်းများကို ရှာဖွေရန် ဖန်တီးသင့်ပါသည်၊ ဒါမှ pitch နှင့် ထုတ်ကုန်အကြံစာတို့ တိုးတက်မြှင့်တင်နိုင်မည်။

## သင်ယူမှု သက်တမ်း မရပ်နား၊ ခရီးလမ်းဆက်လက် နှင့်အတူဖြတ်သန်းပါ

ဒီသင်ခန်းစာပြီးသည်နှင့် [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) တွင် သင့် Generative AI ကျွမ်းကျင်မှုများ အဆင့်မြင့်စေနိုင်ပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->