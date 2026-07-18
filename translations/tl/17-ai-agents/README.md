[![Open Source Models](../../../translated_images/tl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Panimula

Ang AI Agents ay isang kapana-panabik na pag-unlad sa Generative AI, na nagpapahintulot sa Large Language Models (LLMs) na umunlad mula sa pagiging mga assistant tungo sa mga agent na may kakayahang kumilos. Pinapayagan ng mga AI Agent framework ang mga developer na lumikha ng mga aplikasyon na nagbibigay ng access sa LLMs sa mga tool at pamamahala ng estado. Pinapataas din ng mga framework na ito ang kakayahang makita, na nagpapahintulot sa mga gumagamit at developer na subaybayan ang mga planong aksyon ng LLMs, kaya't pinapabuti ang pamamahala ng karanasan.

Tatalakayin ng aralin ang mga sumusunod na aspeto:

- Pag-unawa kung ano ang AI Agent - Ano nga ba ang AI Agent?
- Pag-explore ng limang iba't ibang AI Agent Framework - Ano ang nagpapa-iba sa kanila?
- Paglalapat ng mga AI Agent sa iba't ibang gamit - Kailan dapat gamitin ang AI Agents?

## Mga Layunin sa Pagkatuto

Pagkatapos gawin ang araling ito, magagawa mong:

- Ipaliwanag kung ano ang AI Agents at kung paano ito maaaring gamitin.
- Magkaroon ng pag-unawa sa pagkakaiba ng ilang mga sikat na AI Agent Frameworks, at kung paano sila nagkakaiba.
- Maunawaan kung paano gumagana ang AI Agents upang makabuo ng mga aplikasyon gamit ang mga ito.

## Ano ang AI Agents?

Ang AI Agents ay isang napakapanabik na larangan sa mundo ng Generative AI. Kasabay ng kasabikan na ito ay ang minsang pagkalito tungkol sa mga termino at kanilang aplikasyon. Upang gawing simple at inklusibo sa karamihan ng mga tool na nagtutukoy sa AI Agents, gagamitin natin ang sumusunod na kahulugan:

Pinapayagan ng AI Agents ang Large Language Models (LLMs) na gumanap ng mga gawain sa pamamagitan ng pagbibigay sa kanila ng access sa isang **estado** at **mga tool**.

![Agent Model](../../../translated_images/tl/what-agent.21f2893bdfd01e6a.webp)

Tukuyin natin ang mga terminong ito:

**Large Language Models** - Ito ang mga modelo na tinutukoy sa buong kurso na ito tulad ng GPT-5, GPT-4o, at Llama 3.3, atbp.

**Estado** - Ito ay tumutukoy sa konteksto kung saan nagtatrabaho ang LLM. Ginagamit ng LLM ang konteksto ng mga nakaraang aksyon at kasalukuyang konteksto nito bilang gabay sa paggawa ng desisyon para sa mga susunod na aksyon. Pinapayagan ng AI Agent Frameworks ang mga developer na mas madaling mapanatili ang kontekstong ito.

**Mga Tool** - Upang makatapos ng gawain na hiniling ng gumagamit at pinaplano ng LLM, kailangan ng LLM ng access sa mga tool. Ilan sa mga halimbawa ng tool ay isang database, isang API, isang external na aplikasyon, o kahit isang ibang LLM!

Inaasahan namin na ang mga depinisyong ito ay makakapagbigay sa iyo ng magandang pundasyon habang tinitingnan natin kung paano ito ipinatutupad. Tingnan natin ang ilang iba't ibang AI Agent framework:

## LangChain Agents

Ang [LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ay isang implementasyon ng mga depinisyon na ibinigay natin sa itaas.

Upang pamahalaan ang **estado**, ginagamit nito ang built-in na function na tinatawag na `AgentExecutor`. Tumatanggap ito ng tinukoy na `agent` at ng `tools` na available dito.

Iniimbak din ng `Agent Executor` ang kasaysayan ng chat upang makapagbigay ng konteksto ng usapan.

![Langchain Agents](../../../translated_images/tl/langchain-agents.edcc55b5d5c43716.webp)

Nag-aalok ang LangChain ng isang [katalogo ng mga tool](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) na maaaring i-import sa iyong aplikasyon upang magkaroon ng access ang LLM. Ang mga ito ay ginawa ng komunidad at ng LangChain team.

Maaari mong tukuyin ang mga tool na ito at ipasa ang mga ito sa `Agent Executor`.

Mahalaga rin ang visibility kapag pinag-uusapan ang AI Agents. Mahalaga para sa mga developer ng aplikasyon na maunawaan kung aling tool ang ginagamit ng LLM at bakit. Kaya naman, binuo ng koponan ng LangChain ang LangSmith.

## AutoGen

Ang susunod na AI Agent framework na tatalakayin natin ay ang [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Ang pangunahing pokus ng AutoGen ay mga pag-uusap. Ang mga agent ay parehong **kakayahang makipag-usap** at **napapasadyang**.

**Kakayahang Makipag-usap -** Maaaring magsimula at magpatuloy ng pag-uusap ang mga LLM sa ibang LLM upang matapos ang isang gawain. Ginagawa ito sa pamamagitan ng paglikha ng `AssistantAgents` at pagbibigay sa kanila ng partikular na mensahe ng sistema.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Napapasadyang** - Maaaring tukuyin ang mga agent hindi lamang bilang mga LLM kundi bilang isang user o isang tool. Bilang isang developer, maaari kang magtakda ng `UserProxyAgent` na responsable sa pakikipag-ugnayan sa gumagamit para sa feedback sa pagtapos ng isang gawain. Ang feedback na ito ay maaaring magpatuloy sa pagpapatupad ng gawain o itigil ito.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado at Mga Tool

Upang baguhin at pamahalaan ang estado, ang isang assistant Agent ay gumagawa ng Python code upang matapos ang gawain.

Narito ang isang halimbawa ng proseso:

![AutoGen](../../../translated_images/tl/autogen.dee9a25a45fde584.webp)

#### LLM na Tinukoy na may Mensahe ng Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Nakatuon ang mensaheng ito ng sistema sa partikular na LLM kung aling mga function ang may kaugnayan sa kanyang gawain. Tandaan, sa AutoGen maaari kang magkaroon ng maraming tinukoy na AssistantAgents na may iba't ibang mensahe ng sistema.

#### Sinimulan ang Chat ng User

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ang mensahe mula sa user_proxy (Tao) na ito ang magsisimula sa proseso ng Agent upang alamin ang mga posibleng function na dapat nitong isagawa.

#### Naitakda ang Function

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kapag naproseso na ang unang chat, magpapadala ang Agent ng mungkahing tool na tawagin. Sa kasong ito, ito ay isang function na tinatawag na `get_weather`. Depende sa iyong pagsasaayos, ang function na ito ay maaaring awtomatikong isagawa at basahin ng Agent o isagawa batay sa input ng user.

Maaari mong makita ang listahan ng [mga halimbawa ng code ng AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) upang higit pang matuklasan kung paano magsimula sa paggawa.

## Microsoft Agent Framework

Ang [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ay ang open-source SDK ng Microsoft para sa paggawa ng AI Agents at multi-agent systems sa **Python** at **.NET**. Pinagsasama nito ang lakas ng dalawang mas naunang proyekto ng Microsoft — ang mga enterprise feature ng **Semantic Kernel** at ang multi-agent orchestration ng **AutoGen** — sa isang suportadong framework. Kung nagsisimula ka ng bagong proyekto ng agent ngayon, ito ang inirerekomendang kapalit ng AutoGen.

Ang framework ay nag-scale mula sa isang **chat agent** hanggang sa masalimuot na **multi-agent workflows**, at direktang nag-iintegrate sa Microsoft Foundry, Azure OpenAI, at OpenAI. Nagbibigay din ito ng built-in na obserbabilidad sa pamamagitan ng OpenTelemetry upang masubaybayan mo ng eksakto ang ginagawa ng iyong mga agent.

### Estado at Mga Tool

**Estado** - Pinamamahalaan ng framework ang konteksto ng pag-uusap para sa iyo sa pamamagitan ng **threads**. Ang isang agent ay nagtatala ng kasaysayan ng mga mensahe (mga kahilingan ng user, mga tawag sa tool, at mga resulta nito), kaya ang bawat turn ay nagtatayo sa mga naunang turn. Maaaring ma-persist ang mga threads, na nagpapahintulot na pahintuin at ipagpatuloy ang pag-uusap sa ibang oras.

**Mga Tool** - Binibigyan mo ng tool ang isang agent sa pamamagitan ng pagpasa ng mga plain Python functions. Ang mga parameter na may type-annotation ay awtomatikong ginagawa bilang schema, kaya alam ng modelo kung kailan at paano tatawagin ang mga ito (function calling). Sinusuportahan din ng framework ang Model Context Protocol (MCP) servers at mga hosted tool tulad ng code interpreter.

Narito ang isang halimbawa ng isang single agent na may custom na tool:

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

Upang kumonekta sa Azure OpenAI sa Microsoft Foundry, ipasa ang iyong endpoint at credentials sa client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Mga Multi-agent Workflow

Ang tampok kung saan tunay na namumukod-tangi ang framework ay ang pag-orchestrate ng maraming agent nang sabay. Halimbawa, maaari mong patakbuhin ang mga agent nang isa-isa (bawat isa ay ipinapasa ang kanyang konteksto sa susunod) o mag-fan out sa maraming agent nang sabay at pagsamahin ang kanilang mga resulta:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Patakbuhin ang mga ahente nang sunud-sunod, ipinapasa ang konteksto ng usapan sa kahabaan ng kadena
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Magpadala sa mga ahente nang sabay-sabay, pagkatapos ay pagsamahin ang kanilang mga sagot
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Upang mai-install ang framework at makapagsimula:

```bash
pip install agent-framework-core
# Opsyonal na mga integrasyon
pip install agent-framework-openai       # OpenAI at Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Maaari mong tuklasin pa sa [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) at ang [opisyal na dokumentasyon](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Ang susunod na agent framework na susuriin natin ay ang [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Kilala ito bilang "code-first" agent dahil sa halip na direktang gumamit ng `strings`, maaari nitong gamitin ang DataFrames sa Python. Napaka-kapaki-pakinabang nito para sa mga gawaing pagsusuri at paggawa ng datos. Maaaring ito ay paggawa ng mga graph at charts o pagbuo ng mga random na numero.

### Estado at Mga Tool

Upang pamahalaan ang estado ng pag-uusap, gumagamit ang TaskWeaver ng konsepto ng `Planner`. Ang `Planner` ay isang LLM na tumatanggap ng kahilingan mula sa mga gumagamit at nagmamapa ng mga gawain na kailangang matapos upang matupad ang kahilingang ito.

Upang matapos ang mga gawain, ipinapakilala ng `Planner` ang koleksyon ng mga tool na tinatawag na `Plugins`. Maaaring ito ay mga Python classes o pangkalahatang code interpreter. Ang mga plugins na ito ay iniimbak bilang embeddings upang mas madaling mahanap ng LLM ang tamang plugin.

![Taskweaver](../../../translated_images/tl/taskweaver.da8559999267715a.webp)

Narito ang isang halimbawa ng plugin para sa paghawak ng anomaly detection:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Sinusuri muna ang code bago ito ipatupad. Isa pang tampok para pamahalaan ang konteksto sa Taskweaver ay ang `experience`. Pinapayagan ng experience na ang konteksto ng isang pag-uusap ay maiimbak pang matagal sa isang YAML file. Maaaring i-configure ito upang mapahusay ng LLM ang kakayahan nito sa mga partikular na gawain sa pagdaan ng panahon kapag naipakilala ito sa mga naunang pag-uusap.

## JARVIS

Ang huling agent framework na tatalakayin natin ay ang [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ang nagpapa-iba sa JARVIS ay ginagamit nito ang isang LLM upang pamahalaan ang `estado` ng pag-uusap at ang mga `tool` ay iba pang mga AI model. Ang bawat isa sa mga AI model na ito ay mga espesyalistang modelo na gumagawa ng mga partikular na gawain tulad ng object detection, transcription, o image captioning.

![JARVIS](../../../translated_images/tl/jarvis.762ddbadbd1a3a33.webp)

Ang LLM, bilang isang general purpose na modelo, ay tumatanggap ng kahilingan mula sa gumagamit at tinutukoy ang partikular na gawain at anumang argumento/data na kailangan upang matapos ang gawain.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Inaayos ng LLM ang kahilingan sa paraang maiintindihan ng espesyalistang AI model, tulad ng JSON. Kapag naibalik ng AI model ang kanyang hula base sa gawain, tinatanggap ito ng LLM.

Kung maraming modelo ang kailangan para matapos ang gawain, iinterpreta rin nito ang mga tugon mula sa mga modelong iyon bago pagsamahin ang mga ito upang makabuo ng tugon para sa gumagamit.

Ipinapakita ng halimbawa sa ibaba kung paano ito gagana kapag ang isang gumagamit ay humiling ng paglalarawan at bilang ng mga bagay sa isang larawan:

## Takdang Aralin

Upang ipagpatuloy ang pag-aaral mo tungkol sa AI Agents, maaari kang gumawa gamit ang Microsoft Agent Framework:

- Isang aplikasyon na nagsasagawa ng simulasyon ng pagpupulong sa negosyo kasama ang iba't ibang departamento ng edukasyong startup.
- Gumawa ng mga system message na gagabay sa LLMs upang maunawaan ang iba't ibang persona at prayoridad, at payagan ang user na mag-mungkahi ng bagong ideya ng produkto.
- Dapat gumawa ang LLM ng mga follow-up na tanong mula sa bawat departamento upang pinuhin at pagandahin ang pitch at ang ideya ng produkto.

## Hindi dito nagtatapos ang Pagkatuto, Ipagpatuloy ang Paglalakbay

Pagkatapos tapusin ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->