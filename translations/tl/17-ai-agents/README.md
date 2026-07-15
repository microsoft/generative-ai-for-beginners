[![Open Source Models](../../../translated_images/tl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Panimula

Ang mga AI Agents ay kumakatawan sa isang kapanapanabik na pag-unlad sa Generative AI, na nagpapahintulot sa Large Language Models (LLMs) na umunlad mula sa pagiging mga katulong patungo sa mga agent na may kakayahang gumawa ng mga aksyon. Pinapayagan ng mga AI Agent framework ang mga developer na lumikha ng mga aplikasyon na nagbibigay sa mga LLM ng access sa mga tools at pamamahala ng estado. Pinapalakas din ng mga framework na ito ang kakayahang makita, na nagpapahintulot sa mga gumagamit at developer na subaybayan ang mga aksyon na plano ng mga LLM, kaya't pinapabuti ang pamamahala ng karanasan.

Sasaklawin ng aralin ang mga sumusunod na larangan:

- Pag-unawa kung ano ang AI Agent - Ano nga ba talaga ang AI Agent?
- Pagsasaliksik ng limang iba't ibang AI Agent Frameworks - Ano ang nagpapakilala sa kanila?
- Paglalapat ng mga AI Agent sa iba't ibang mga kaso ng paggamit - Kailan dapat gumamit ng AI Agents?

## Mga layunin sa pag-aaral

Pagkatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang mga AI Agents at paano sila maaaring gamitin.
- Maunawaan ang pagkakaiba sa pagitan ng ilang mga kilalang AI Agent Frameworks, at kung paano sila nagkakaiba.
- Maunawaan kung paano gumagana ang mga AI Agents upang makabuo ng mga aplikasyon gamit ang mga ito.

## Ano ang mga AI Agents?

Ang mga AI Agents ay isang napaka-kapanapanabik na larangan sa mundo ng Generative AI. Kasabay ng kasiyahang ito ay ang minsang kalituhan sa mga termino at ang kanilang aplikasyon. Upang gawing simple at inklusibo para sa karamihan ng mga tool na tumutukoy sa AI Agents, gagamitin natin ang depinisyong ito:

Pinapayagan ng mga AI Agents ang Large Language Models (LLMs) na magsagawa ng mga gawain sa pamamagitan ng pagbibigay sa kanila ng access sa **estado** at **tools**.

![Agent Model](../../../translated_images/tl/what-agent.21f2893bdfd01e6a.webp)

Tukuyin natin ang mga terminong ito:

**Large Language Models** - Ito ang mga modelong tinutukoy sa buong kurso na ito tulad ng GPT-3.5, GPT-4, Llama-2, atbp.

**Estado** - Tumutukoy ito sa kontextong pinagtratrabahuhan ng LLM. Ginagamit ng LLM ang kontexto ng mga nagdaang aksyon at kasalukuyang kontexto para gabayan ang paggawa ng desisyon sa mga susunod na aksyon. Pinapayagan ng AI Agent Frameworks ang mga developer na mas madaling mapanatili ang kontexto.

**Tools** - Upang makumpleto ang gawain na hiniling ng gumagamit at pinlanong gawin ng LLM, kailangan ng LLM ng access sa mga tools. Ilan sa mga halimbawa ng tools ay maaaring isang database, API, panlabas na aplikasyon, o kahit isa pang LLM!

Inaasahan namin na ang mga depinisyon na ito ay magbibigay sa iyo ng matibay na pundasyon habang tinitingnan natin kung paano ito ipinatupad. Tingnan natin ang ilang iba't ibang AI Agent frameworks:

## LangChain Agents

Ang [LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ay isang pagpapatupad ng mga depinisyong ibinigay namin sa itaas.

Upang pamahalaan ang **estado**, gumagamit ito ng built-in na function na tinatawag na `AgentExecutor`. Tumatanggap ito ng tinukoy na `agent` at mga `tools` na magagamit dito.

Itinatago rin ng `Agent Executor` ang kasaysayan ng chat upang magbigay ng kontexto ng pag-uusap.

![Langchain Agents](../../../translated_images/tl/langchain-agents.edcc55b5d5c43716.webp)

Nagbibigay ang LangChain ng [catalog ng mga tools](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) na maaaring i-import sa iyong aplikasyon kung saan makakakuha ng access ang LLM. Ginawa ito ng komunidad at ng koponan ng LangChain.

Maaari mong tukuyin ang mga tools na ito at ipasa ang mga ito sa `Agent Executor`.

Ang kakayahang makita ay isa pang mahalagang aspekto kapag pinag-uusapan ang AI Agents. Mahalaga para sa mga developer ng aplikasyon na maunawaan kung aling tool ang ginagamit ng LLM at bakit.. Para doon, binuo ng koponan sa LangChain ang LangSmith.

## AutoGen

Ang susunod na AI Agent framework na tatalakayin natin ay [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Ang pangunahing pokus ng AutoGen ay mga pag-uusap. Ang mga agents ay parehong **conversable** at **customizable**.

**Conversable -** Maaaring magsimula at magpatuloy ng pag-uusap ang mga LLM sa isa pang LLM upang makumpleto ang isang gawain. Ginagawa ito sa pamamagitan ng paglikha ng `AssistantAgents` at pagbibigay sa kanila ng isang partikular na system message.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Customizable** - Maaaring tukuyin ang mga Agents hindi lamang bilang mga LLM kundi bilang isang gumagamit o tool. Bilang isang developer, maaari kang magtukoy ng `UserProxyAgent` na responsable sa pakikipag-interact sa gumagamit para sa feedback sa pagkumpleto ng isang gawain. Ang feedback na ito ay maaaring ipagpatuloy ang pagpapatupad ng gawain o itigil ito.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado at Tools

Upang baguhin at pamahalaan ang estado, nag-ge-generate ang isang assistant Agent ng Python code upang makumpleto ang gawain.

Narito ang isang halimbawa ng proseso:

![AutoGen](../../../translated_images/tl/autogen.dee9a25a45fde584.webp)

#### LLM na Tinutukoy ng System Message

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Itinatalaga ng system message na ito ang partikular na LLM sa mga function na mahalaga para sa kanyang gawain. Tandaan, sa AutoGen maaari kang magkaroon ng maraming tinukoy na AssistantAgents na may iba't ibang system messages.

#### Inumpisahan ng User ang Chat

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ang mensaheng ito mula sa user_proxy (Tao) ang magsisimula sa proseso ng Agent na suriin ang mga posibleng function na dapat nitong isagawa.

#### Isinagawa ang Function

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kapag naiproseso na ang paunang chat, ipapadala ng Agent ang iminungkahing tool na tatawagin. Sa kasong ito, ito ay isang function na tinatawag na `get_weather`. Depende sa iyong configuration, maaaring awtomatikong isagawa at basahin ng Agent ang function na ito o maaaring isagawa batay sa input ng gumagamit.

Maaari kang makakita ng listahan ng [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para mas mapag-aralan kung paano magsimula sa paggawa.

## Microsoft Agent Framework

Ang [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ay open-source SDK ng Microsoft para sa paggawa ng AI Agents at mga multi-agent na sistema sa parehong **Python** at **.NET**. Pinagsasama nito ang lakas ng dalawang naunang proyekto ng Microsoft — ang enterprise features ng **Semantic Kernel** at ang multi-agent orchestration ng **AutoGen** — sa isang suportadong framework. Kung magsisimula ka ng bagong project ng agent ngayon, ito ang inirerekomendang kapalit ng AutoGen.

Ang framework ay nag-scale mula sa isang **chat agent** hanggang sa kumplikadong **multi-agent workflows**, at nag-iintegrate nang direkta sa Microsoft Foundry, Azure OpenAI, at OpenAI. Nagbibigay din ito ng built-in observability sa pamamagitan ng OpenTelemetry upang masubaybayan mo nang eksakto kung ano ang ginagawa ng iyong mga agents.

### Estado at Tools

**Estado** - Pinamamahalaan ng framework ang konteksto ng pag-uusap para sa iyo sa pamamagitan ng **threads**. Sinusubaybayan ng isang agent ang kasaysayan ng mensahe (mga kahilingan ng gumagamit, pagtawag sa tool, at ang kanilang mga resulta), kaya bawat pagikot ay nagtutuluy-tuloy sa mga naunang pagikot. Maaari ring mapanatili ang threads, na nagpapahintulot na ma-pause at maipagpatuloy ang pag-uusap sa ibang pagkakataon.

**Tools** - Bibigyan mo ang isang agent ng tools sa pamamagitan ng pagpapasa ng simpleng Python functions. Ang type-annotated na mga parameter ay awtomatikong ginagawang schema, kaya alam ng model kung paano at kailan tawagin ang mga ito (function calling). Sinusuportahan din ng framework ang Model Context Protocol (MCP) servers at mga hosted tools tulad ng code interpreter.

Narito ang isang halimbawa ng isang agent na may custom na tool:

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

Upang kumonekta sa Azure OpenAI sa Microsoft Foundry, ipasa ang iyong endpoint at mga kredensyal sa client:

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

Saan talagang namumukod-tangi ang framework ay sa pag-oorganisa ng maraming agents nang sabay-sabay. Halimbawa, maaari mong patakbuhin ang mga agents isa-isa (bawat isa ay ipinapasa ang kanyang kontexto sa susunod) o sabay-sabay sa parallel ang ilang agents at pagsamahin ang kanilang mga resulta:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Patakbuhin ang mga ahente nang sunud-sunod, ipinapasa ang konteksto ng pag-uusap sa kahabaan ng kadena
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Ipamahagi sa mga ahente nang sabay-sabay, pagkatapos ay pagsamahin ang kanilang mga sagot
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Upang i-install ang framework at magsimula:

```bash
pip install agent-framework-core
# Opsyonal na mga integrasyon
pip install agent-framework-openai       # OpenAI at Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Maaari kang mag-explore pa sa [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) at ang [opisyal na dokumentasyon](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Ang susunod na agent framework na susuriin natin ay [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Kilala ito bilang "code-first" agent dahil sa halip na magtrabaho lang sa `strings`, maaari itong magtrabaho gamit ang DataFrames sa Python. Ito ay napaka-kapaki-pakinabang para sa mga task sa pag-aanalisa at pagbuo ng data. Maaaring ito ay mga bagay tulad ng paggawa ng mga graph at chart o pagbuo ng mga random na numero.

### Estado at Tools

Upang pamahalaan ang estado ng pag-uusap, ginagamit ng TaskWeaver ang konsepto ng `Planner`. Ang `Planner` ay isang LLM na kumukuha ng kahilingan mula sa mga gumagamit at nagmamapa ng mga gawain na kailangang matapos upang matupad ang kahilingang ito.

Upang matapos ang mga gawain, ang `Planner` ay inilalantad sa koleksyon ng mga tool na tinatawag na `Plugins`. Ito ay maaaring mga Python classes o isang pangkalahatang code interpreter. Ang mga plugins na ito ay iniimbak bilang embeddings upang mas mahusay na mahanap ng LLM ang tamang plugin.

![Taskweaver](../../../translated_images/tl/taskweaver.da8559999267715a.webp)

Narito ang isang halimbawa ng plugin para sa paghawak ng anomaly detection:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Pinapatunayan ang code bago ito isagawa. Isa pang tampok para sa pamamahala ng kontexto sa Taskweaver ay ang `experience`. Pinapayagan ng experience ang kontexto ng pag-uusap na maimbak sa mahabang panahon sa isang YAML file. Maaari itong i-configure upang mapabuti ang LLM sa paglipas ng panahon sa ilang mga gawain dahil naipapakita ito sa mga naunang pag-uusap.

## JARVIS

Ang huling agent framework na susuriin natin ay ang [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ang nagtatangi sa JARVIS ay ginagamit nito ang isang LLM upang pamahalaan ang `estado` ng pag-uusap at ang `tools` ay mga ibang AI model. Ang bawat AI model ay espesyalisadong modelo na nagsasagawa ng tiyak na mga gawain tulad ng object detection, transcription o image captioning.

![JARVIS](../../../translated_images/tl/jarvis.762ddbadbd1a3a33.webp)

Tumatanggap ang LLM, bilang isang general purpose model, ng kahilingan mula sa gumagamit at tinutukoy ang partikular na gawain at anumang mga argumento/data na kailangan upang makumpleto ang gawain.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Nagsa-format ang LLM ng kahilingan sa paraan na maiintindihan ng espesyalisadong AI model, tulad ng JSON. Kapag naibalik na ng AI model ang hula nito batay sa gawain, tinatanggap ng LLM ang tugon.

Kung kinakailangang gamitin ang maraming modelo upang makumpleto ang gawain, iinterpreta rin nito ang mga tugon mula sa mga modelong iyon bago pagsamahin ang mga ito upang gumawa ng sagot para sa gumagamit.

Ipinapakita ng halimbawa sa ibaba kung paano ito gagana kapag ang gumagamit ay humiling ng paglalarawan at bilang ng mga bagay sa isang larawan:

## Pagsasanay

Upang ipagpatuloy ang iyong pag-aaral sa AI Agents, maaari kang gumawa gamit ang Microsoft Agent Framework:

- Isang aplikasyon na nagsasagawa ng isang pagpupulong ng negosyo kasama ang iba't ibang departamento ng isang education startup.
- Lumikha ng mga system message na gumagabay sa mga LLM upang maunawaan ang iba't ibang persona at prayoridad, at pahintulutan ang gumagamit na mag-pitch ng bagong ideya ng produkto.
- Pagkatapos ay dapat mag-generate ang LLM ng mga follow-up na tanong mula sa bawat departamento upang pinuhin at pagbutihin ang pitch at ang ideya ng produkto

## Hindi dito nagtatapos ang pagkatuto, ipagpatuloy ang Paglalakbay

Pagkatapos tapusin ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-angat ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->