[![Open Source Models](../../../translated_images/sw/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Utangulizi

Wakala wa AI wanaonyesha maendeleo ya kusisimua katika AI ya Kizazi, kuwezesha Modeli Kubwa za Lugha (LLMs) kukua kutoka kuwa wasaidizi hadi kuwa mawakala wenye uwezo wa kuchukua hatua. Mifumo ya Wakala wa AI inawawezesha waendelezaji kuunda programu zinazowapa LLMs ufikiaji wa zana na usimamizi wa hali. Mifumo hii pia huboresha uwazi, ikiruhusu watumiaji na waendelezaji kufuatilia hatua zilizopangwa na LLMs, hivyo kuboresha usimamizi wa uzoefu.

Somo hili litashughulikia maeneo yafuatayo:

- Kuelewa ni nini hasa Wakala wa AI - Wakala wa AI ni nini hasa?
- Kuchunguza mifumo mitano tofauti ya Wakala wa AI - Nini kinawafanya wawe wa kipekee?
- Kutumia Wakala hawa wa AI katika matumizi tofauti - Tutatumiwa lini Wakala wa AI?

## Malengo ya Kujifunza

Baada ya kuchukua somo hili, utaweza:

- Eleza ni wakala wa AI ni nini na jinsi wanavyoweza kutumiwa.
- Kuwa na uelewa wa tofauti kati ya mifumo maarufu ya Wakala wa AI, na jinsi zinavyotofautiana.
- Kuelewa jinsi wakala wa AI wanavyofanya kazi ili kujenga programu pamoja nao.

## Wakala wa AI ni Nani?

Wakala wa AI ni eneo la kusisimua sana katika dunia ya AI ya Kizazi. Pamoja na msisimko huu mara nyingine hutokea mkanganyiko wa maneno na matumizi yao. Ili kuweka mambo rahisi na jumuishi kwa zana nyingi zinazorejelea Wakala wa AI, tutatumia ufafanuzi huu:

Wakala wa AI huruhusu Modeli Kubwa za Lugha (LLMs) kutekeleza majukumu kwa kuwapa ufikiaji wa **hali** na **zana**.

![Agent Model](../../../translated_images/sw/what-agent.21f2893bdfd01e6a.webp)

Hebu tueleze maneno haya:

**Modeli Kubwa za Lugha** - Hizi ni modeli zinazozungumziwa katika kozi hii kama GPT-5, GPT-4o, na Llama 3.3, nk.

**Hali** - Hii inarejelea muktadha ambao LLM inafanya kazi ndani yake. LLM hutumia muktadha wa hatua zake za zamani na muktadha wa sasa, ikiongoza maamuzi yake kwa hatua zinazofuata. Mifumo ya Wakala wa AI huruhusu waendelezaji kudumisha muktadha huu kwa urahisi zaidi.

**Zana** - Ili kukamilisha kazi ambayo mtumiaji aliomba na LLM imepanga, LLM inahitaji ufikiaji wa zana. Mifano ya zana inaweza kuwa hifadhidata, API, programu ya nje au hata LLM nyingine!

Ufafanuzi huu una matumaini utakupa msingi mzuri uendelezaji tunapokuwa tunachunguza jinsi zinavyotekelezwa. Hebu tuchunguze mifumo kadhaa tofauti ya wakala wa AI:

## Wakala wa LangChain

[Wakala wa LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ni utekelezaji wa ufafanuzi tuliopewa hapo juu.

Kusimamia **hali** , inatumia kazi iliyojengwa ndani iitwayo `AgentExecutor`. Hii inakubali `agent` iliyobainishwa na `tools` zinazopatikana kwake.

`Agent Executor` pia huhifadhi historia ya mazungumzo kutoa muktadha wa mazungumzo.

![Langchain Agents](../../../translated_images/sw/langchain-agents.edcc55b5d5c43716.webp)

LangChain inatoa [katalogi ya zana](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) zinazoweza kuingizwa kwenye programu yako ambapo LLM inaweza kupata ufikiaji. Hizi hutengenezwa na jamii na timu ya LangChain.

Kisha unaweza kufafanua zana hizi na kuzipitisha kwa `Agent Executor`.

Uwazi ni kipengele kingine muhimu unapotamka kuhusu Wakala wa AI. Ni muhimu kwa waendelezaji wa programu kuelewa ni zana gani LLM inazitumia na kwa nini.. Kwa hiyo, timu ya LangChain wameunda LangSmith.

## AutoGen

Mfumo mwingine wa wakala wa AI tutaozungumzia ni [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Lengo kuu la AutoGen ni mazungumzo. Wakala ni **wanaoweza kuzungumza** na **wanaoweza kubadilishwa**.

**Wanaoweza kuzungumza -** LLM zinaweza kuanzisha na kuendeleza mazungumzo na LLM nyingine ili kukamilisha kazi. Hii hufanyika kwa kuunda `AssistantAgents` na kuwapa ujumbe maalum wa mfumo.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Wanaoweza kubadilishwa** - Wakala wanaweza kufafanuliwa si tu kama LLM bali pia kuwa mtumiaji au zana. Kama msanidi, unaweza kufafanua `UserProxyAgent` anayehusika na kuingiliana na mtumiaji kwa maoni katika kukamilisha kazi. Maoni haya yanaweza kuendelea au kusimamisha utekelezaji wa kazi.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Hali na Zana

Kubadilisha na kusimamia hali, Msaidizi wa Wakala hutengeneza msimbo wa Python kukamilisha kazi.

Huu ni mfano wa mchakato:

![AutoGen](../../../translated_images/sw/autogen.dee9a25a45fde584.webp)

#### LLM Imefafanuliwa kwa Ujumbe wa Mfumo

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ujumbe huu wa mfumo unaelekeza LLM hii maalum ni kazi gani zinazohitajika kwa ajili ya jukumu lake. Kumbuka, na AutoGen unaweza kuwa na AssistantAgents wengi wenye ujumbe mbalimbali wa mfumo.

#### Mazungumzo Huanza na Mtumiaji

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ujumbe huu kutoka kwa user_proxy (Binadamu) ndio utaanza mchakato wa Wakala kuchunguza kazi zinazowezekana za kutekeleza.

#### Kazi Inafanywa

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Mara baada ya mazungumzo ya mwanzo kusindikwa, Wakala atatuma zana iliyopendekezwa kuita. Katika kesi hii, ni kazi iitwayo `get_weather`. Kulingana na usanidi wako, kazi hii inaweza kutekelezwa moja kwa moja na kusomwa na Wakala au kufanywa kulingana na maoni ya mtumiaji.

Unaweza kupata orodha ya [mifano ya msimbo ya AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) kuchunguza zaidi jinsi ya kuanza kujenga.

## Mfumo wa Wakala wa Microsoft

[Mfumo wa Wakala wa Microsoft](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ni SDK ya chanzo wazi ya Microsoft kwa kujenga Wakala wa AI na mifumo ya mawakala wengi katika **Python** na **.NET**. Inaleta pamoja nguvu za miradi miwili ya awali ya Microsoft — vipengele vya biashara vya **Semantic Kernel** na usimamizi wa mawakala wengi wa **AutoGen** — katika mfumo mmoja unaounga mkono. Ikiwa unaanza mradi mpya wa wakala leo, huu ndio mrithi anayependekezwa wa AutoGen.

Mfumo huu unaweza kupanuka kutoka kwa **wakala mmoja wa mazungumzo** hadi **mchakato wa mawakala wengi tata**, na unaunganisha moja kwa moja na Microsoft Foundry, Azure OpenAI, na OpenAI. Pia hutoa ufuatiliaji uliojengewa ndani kupitia OpenTelemetry ili uweze kufuatilia hasa kile mawakala wako wanachofanya.

### Hali na Zana

**Hali** - Mfumo husimamia muktadha wa mazungumzo kwako kupitia **nyuzi**. Wakala hubaini historia ya ujumbe (maombi ya mtumiaji, simu za zana, na matokeo yake), hivyo kila zamu hujenga juu ya zile zilizopita. Nyuzi pia zinaweza kuhifadhiwa, kuruhusu mazungumzo kusimamishwa na kuendelea baadaye.

**Zana** - Unampa wakala zana kwa kupitisha kazi za kawaida za Python. Vigezo vilivyo na aina hubadilishwa moja kwa moja kuwa kielelezo, hivyo modeli inajua jinsi na lini kuvaita (atingozi ya kazi). Mfumo pia unaunga mkono seva za Model Context Protocol (MCP) na zana zilizo hifadhiwa kama mtafsiri wa msimbo.

Huu ni mfano wa wakala mmoja mwenye zana maalum:

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

Kuungana na Azure OpenAI katika Microsoft Foundry badala yake, pita huduma zako na kredenshali kwa mteja:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Mchakato wa mawakala wengi

Sehemu ambapo mfumo huu unajitokeza zaidi ni kusimamia mawakala kadhaa pamoja. Kwa mfano, unaweza kuendesha mawakala mmoja baada ya mwingine (kila mmoja akipitisha muktadha wake kwa mwingine) au kupeleka kwa mawakala wengi sambamba na kujumlisha matokeo yao:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Endesha maajenti kwa mfululizo, ukipitisha muktadha wa mazungumzo kwa mlolongo
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sambaza kwa maajenti kwa wakati mmoja, kisha Kusanya majibu yao
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Ili kusakinisha mfumo na kuanza:

```bash
pip install agent-framework-core
# Mchanganyiko ya hiari
pip install agent-framework-openai       # OpenAI na Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Unaweza kuchunguza zaidi katika [hifadhidata ya Mfumo wa Wakala wa Microsoft](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) na [nyaraka rasmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Mfumo mwingine wa wakala tutaochunguza ni [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Unajulikana kama wakala "wa kwanza msimbo" kwa sababu badala ya kufanya kazi kwa kutumia `mifugo` tu, unaweza kufanya kazi na DataFrames katika Python. Hii inakuwa muhimu sana kwa kazi za uchambuzi wa data na uzalishaji. Hii inaweza kuwa vitu kama kuunda michoro na chati au kuzalisha nambari za bahati nasibu.

### Hali na Zana

Kusimamia hali ya mazungumzo, TaskWeaver hutumia dhana ya `Planner`. `Planner` ni LLM inayopokea maombi kutoka kwa watumiaji na kupanga majukumu yanayohitajika kukamilishwa ili kutimiza ombi hilo.

Kumalizia majukumu `Planner` inafahamishwa na mkusanyiko wa zana unaoitwa `Plugins`. Hizi zinaweza kuwa madarasa ya Python au mtafsiri wa msimbo wa jumla. Plugins hizi huhifadhiwa kama embeddings ili LLM iweze kutafuta plugin sahihi kwa urahisi zaidi.

![Taskweaver](../../../translated_images/sw/taskweaver.da8559999267715a.webp)

Huu ni mfano wa plugin ya kushughulikia utambuzi wa kasoro:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Msimbo unathibitishwa kabla ya utekelezaji. Kipengele kingine cha kusimamia muktadha katika Taskweaver ni `experience`. Uzoefu huruhusu muktadha wa mazungumzo kuhifadhiwa kwa muda mrefu katika faili la YAML. Hii inaweza kusanidiwa ili LLM iboreze kwa muda katika kazi fulani kwa kuwa imefahamishwa na mazungumzo ya awali.

## JARVIS

Mfumo wa wakala wa mwisho tutaochunguza ni [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Kinachomfanya JARVIS kuwa wa kipekee ni kwamba hutumia LLM kusimamia `hali` ya mazungumzo na `zanafanya kazi` ni modeli nyingine za AI. Kila moja ya modeli hizo za AI ni maalumu zinazofanya kazi fulani kama utambuzi wa vitu, uandishi wa maandishi au kutoa maelezo ya picha.

![JARVIS](../../../translated_images/sw/jarvis.762ddbadbd1a3a33.webp)

LLM, ikiwa ni modeli ya matumizi ya jumla, hupokea ombi kutoka kwa mtumiaji na kutambua kazi maalum na hoja/data zinazohitajika kukamilisha kazi.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kisha huweka ombi katika muundo unaoweza kufasiriwa na modeli maalumu ya AI, kama JSON. Mara modeli ya AI inaporodhesha utabiri wake kulingana na kazi, LLM hupokea jibu.

Ikiwa modeli nyingi zinahitajika kukamilisha kazi, pia itatafsiri jibu kutoka kwa modeli hizo kabla ya kuziunganisha pamoja kutoa jibu kwa mtumiaji.

Mfano hapa chini unaonyesha jinsi hii ingefanya kazi wakati mtumiaji anapotaka maelezo na hesabu ya vitu katika picha:

## Kazi ya Nyumbani

Kuendelea na kujifunza kwako kwa Wakala wa AI unaweza kujenga kwa Microsoft Agent Framework:

- Programu inayosimulia mkutano wa biashara na idara tofauti za kuanzisha elimu.
- Unda ujumbe wa mfumo unaoelekeza LLM kuelewa wahusika na vipaumbele tofauti, na kumruhusu mtumiaji kupendekeza wazo jipya la bidhaa.
- LLM inapaswa kisha kuunda maswali ya kufuatilia kutoka kila idara kuboresha na kusahihisha pendekezo na wazo la bidhaa

## Kujifunza hakukomi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kuendelea kuongeza maarifa yako ya AI ya Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->