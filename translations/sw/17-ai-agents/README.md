[![Open Source Models](../../../translated_images/sw/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Utangulizi

Wakala wa AI wanawakilisha maendeleo ya kusisimua katika AI ya Kizazi, ikiwawezesha Mifano Mikubwa ya Lugha (LLMs) kuibuka kutoka kwa wasaidizi kuwa mawakala wenye uwezo wa kuchukua hatua. Mifumo ya Wakala wa AI inawawezesha watengenezaji kuunda programu zinazowapa LLMs ufikiaji wa zana na usimamizi wa hali. Mifumo hii pia huongeza uonekano, ikiruhusu watumiaji na watengenezaji kufuatilia hatua zinazopangwa na LLMs, hivyo kuboresha usimamizi wa uzoefu.

Somo hili litashughulikia maeneo yafuatayo:

- Kuelewa ni Wakala wa AI gani - Ni nini hasa Wakala wa AI?
- Kuchunguza mifumo mitano tofauti ya Wakala wa AI - Nini kinaifanya kuwa za kipekee?
- Kutumia Wakala hawa wa AI katika matumizi tofauti - Lini tunapaswa kutumia Wakala wa AI?

## Malengo ya Kujifunza

Baada ya kuchukua somo hili, utaweza:

- Eleza ni Wakala wa AI gani na jinsi wanavyoweza kutumiwa.
- Kuwa na uelewa wa tofauti kati ya baadhi ya mifumo maarufu ya Wakala wa AI, na jinsi zinavyotofautiana.
- Elewa jinsi Wakala wa AI wanavyofanya kazi ili kuunda programu kwa kutumia wao.

## Ni Wakala wa AI Gani?

Wakala wa AI ni eneo lenye kusisimua sana katika dunia ya AI ya Kizazi. Pamoja na msisimko huu kuna wakati hutokea mkanganyiko wa maneno na matumizi yao. Ili kuweka mambo kuwa rahisi na kujumuisha zana nyingi zinazotaja Wakala wa AI, tutatumia ufasiri huu:

Wakala wa AI huwapa Mifano Mikubwa ya Lugha (LLMs) uwezo wa kutekeleza kazi kwa kuwapa ufikiaji wa **hali** na **zana**.

![Agent Model](../../../translated_images/sw/what-agent.21f2893bdfd01e6a.webp)

Tukafafanue maneno haya:

**Mifano Mikubwa ya Lugha** - Hawa ni mifano inayotajwa katika kozi hii kama GPT-3.5, GPT-4, Llama-2, n.k.

**Hali** - Inahusu muktadha ambamo LLM inafanya kazi. LLM hutumia muktadha wa hatua zake za awali na muktadha wa sasa, kuongoza uamuzi wake kwa hatua zinazofuata. Mifumo ya Wakala wa AI huwasaidia watengenezaji kudumisha muktadha huu kwa urahisi zaidi.

**Zana** - Ili kukamilisha kazi ambayo mtumiaji ameomba na ambayo LLM imeipanga, LLM inahitaji ufikiaji wa zana. Mifano ya zana inaweza kuwa hifadhidata, API, programu ya nje au hata LLM nyingine!

Tafsiri hizi zinatarajiwa kukupa msingi mzuri unaoelekea mbele tunapochunguza jinsi zinavyotekelezwa. Tuchunguze mifumo michache tofauti ya Wakala wa AI:

## Wakala wa LangChain

[Wakala wa LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ni utekelezaji wa taswira tulizotoa hapo juu.

Kusimamia **hali**, inatumia kazi iliyojengwa ndani iitwayo `AgentExecutor`. Hii inakubali `agent` iliyotangazwa pamoja na `tools` zinazopatikana kwake.

`Agent Executor` pia huhifadhi historia ya mazungumzo kutoa muktadha wa mazungumzo.

![Langchain Agents](../../../translated_images/sw/langchain-agents.edcc55b5d5c43716.webp)

LangChain hutoa [katalogi ya zana](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) ambazo zinaweza kuingizwa katika programu yako ambapo LLM inaweza kupata ufikiaji. Hizi hutengenezwa na jamii na timu ya LangChain.

Kisha unaweza kufafanua zana hizi na kuzitumia kwa `Agent Executor`.

Uonekano ni jambo lingine muhimu tunapoongea kuhusu Wakala wa AI. Ni muhimu kwa watengenezaji wa programu kuelewa ni zana gani LLM inazitumia na kwa nini. Kwa hili, timu ya LangChain imeunda LangSmith.

## AutoGen

Mfumo mwingine wa Wakala wa AI tutakaojadili ni [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Lengo kuu la AutoGen ni mazungumzo. Wakala ni **yanaweza kuzungumza** na **yanaweza kubadilishwa**.

**Yanaweza kuzungumza -** LLM inaweza kuanzisha na kuendelea na mazungumzo na LLM nyingine ili kukamilisha kazi. Hii hufanyika kwa kuunda `AssistantAgents` na kuwapa ujumbe maalum wa mfumo.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Yanaweza kubadilishwa** - Wakala wanaweza kufafanuliwa si kama LLM tu bali kuwa mtumiaji au zana. Kama mtengenezaji, unaweza kufafanua `UserProxyAgent` anayehusika na kuingiliana na mtumiaji kwa maoni katika kumaliza kazi. Maoni haya yanaweza kuendelea au kusitisha utekelezaji wa kazi.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Hali na Zana

Kubadilisha na kusimamia hali, Msaidizi Wakala hutengeneza msimbo wa Python kumaliza kazi.

Hapa ni mfano wa mchakato:

![AutoGen](../../../translated_images/sw/autogen.dee9a25a45fde584.webp)

#### LLM Imefafanuliwa kwa Ujumbe wa Mfumo

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ujumbe huu wa mfumo unaelekeza LLM hii maalum ni kazi zipi zinazohusiana. Kumbuka, kwa AutoGen unaweza kuwa na AssistantAgents wengi waliotangazwa na ujumbe tofauti wa mfumo.

#### Mazungumzo Yaanza na Mtumiaji

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ujumbe huu kutoka kwa mtumiaji_proxy (Binaadamu) ndicho kitakachosababisha mchakato wa Wakala kuchunguza kazi zinazoweza kutekelezwa.

#### Kazi Inatekelezwa

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Mara mazungumzo ya awali yatakapopatiwa, Wakala atatuma zana iliyopendekezwa kuitwa. Katika kesi hii, ni kazi iitwayo `get_weather`. Kulingana na usanidi wako, kazi hii inaweza kutekelezwa moja kwa moja na kusomwa na Wakala au kufanyika kwa kuzingatia maoni ya mtumiaji.

Unaweza kupata orodha ya [mifano ya kanuni za AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) ili kuchunguza zaidi jinsi ya kuanza kujenga.

## Mfumo wa Wakala wa Microsoft

[Mfumo wa Wakala wa Microsoft](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ni SDK ya chanzo huria ya Microsoft ya kujenga Wakala wa AI na mifumo ya mawakala wengi kwa **Python** na **.NET**. Inachanganya nguvu za miradi miwili ya awali ya Microsoft — sifa za biashara za **Semantic Kernel** na usimamizi wa mawakala wengi wa **AutoGen** — katika mfumo mmoja unaounga mkono. Ikiwa unaanza mradi mpya wa wakala leo, huu ndio mrithi anayependekezwa wa AutoGen.

Mfumo huu unakua kutoka kwa **wakala wa mazungumzo** mmoja hadi **mipangilio ya kazi ya mawakala wengi** tata, na unajumuika moja kwa moja na Microsoft Foundry, Azure OpenAI, na OpenAI. Pia hutoa uonekano wa ndani kupitia OpenTelemetry ili uweze kufuatilia hasa wanachofanya mawakala wako.

### Hali na Zana

**Hali** - Mfumo unasimamia muktadha wa mazungumzo kwako kupitia **nyuzi**. Wakala hufuata historia ya ujumbe (maombi ya mtumiaji, simu za zana, na matokeo yao), hivyo kila mzunguko unajengwa juu ya wa awali. Nyuzi zinaweza pia kuhifadhiwa, kuruhusu mazungumzo kupumzishwa na kuendelea baadaye.

**Zana** - Unampa wakala zana kwa kumpitisha kazi za kawaida za Python. Vigezo vilivyotajwa aina hubadilishwa moja kwa moja kuwa kielelezo, hivyo mfano unajua jinsi na lini kuvita (kupiga simu ya kazi). Mfumo pia unaunga mkono seva za Protocol ya Muktadha wa Mfano (MCP) na zana zilizo hifadhiwa kama kimsingi cha msimbo.

Hapa ni mfano wa wakala mmoja akiwa na zana maalum:

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

Kuunganishwa na Azure OpenAI katika Microsoft Foundry badala yake, pitisha anwani yako na nyaraka kwa mteja:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Mipangilio ya kazi ya mawakala wengi

Mahali ambapo mfumo unaonekana kweli ni kupanga mawakala kadhaa pamoja. Kwa mfano, unaweza kuendesha mawakala mmoja baada ya mwingine (kila mmoja akipitisha muktadha wake kwa mwingine) au kueneza kwa mawakala wengi kwa wakati mmoja na kuchanganya matokeo yao:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Endesha mawakala mfululizo, ukipitisha muktadha wa mazungumzo mnyoroni
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Fanya mawakala kufanya kazi sambamba, kisha kusanya majibu yao pamoja
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Ili kusakinisha mfumo na kuanza:

```bash
pip install agent-framework-core
# Mwingiliano wa hiari
pip install agent-framework-openai       # OpenAI na Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Unaweza kuchunguza zaidi katika [hazina ya Mfumo wa Wakala wa Microsoft](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) na [nyaraka rasmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Mfumo mwingine wa wakala tutakaochunguza ni [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Unajulikana kama wakala "msimbo kwanza" kwa sababu badala ya kufanya kazi kwa mujibu wa `strings`, unaweza kufanya kazi na DataFrames katika Python. Hii huwa muhimu sana kwa kazi za uchambuzi wa data na kizazi. Hii inaweza kuwa kama kutengeneza grafs na chati au kuzalisha nambari nasibu.

### Hali na Zana

Kusimamia hali ya mazungumzo, TaskWeaver hutumia dhana ya `Planner`. `Planner` ni LLM inayochukua ombi kutoka kwa watumiaji na kupanga kazi zinazopaswa kukamilishwa kutimiza ombi hili.

Ili kukamilisha kazi, `Planner` huwa na ufikiaji wa makusanyo ya zana zinazotajwa `Plugins`. Hizi zinaweza kuwa madarasa ya Python au kimsingi cha msimbo kwa ujumla. Plugins hizi huhifadhiwa kama embeddings ili LLM iweze kutafuta plugin sahihi vyema.

![Taskweaver](../../../translated_images/sw/taskweaver.da8559999267715a.webp)

Hapa ni mfano wa plugin inayoshughulikia utambuzi wa kasoro:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Msimbo unathibitishwa kabla ya kutekelezwa. Kipengele kingine cha kusimamia muktadha katika Taskweaver ni `experience`. Uzoefu huruhusu muktadha wa mazungumzo kuhifadhiwa kwa muda mrefu katika faili la YAML. Hii inaweza kusanidiwa hivyo LLM inaendelea kuboresha kwa muda katika kazi fulani kwa kuwa imeshughulikiwa na mazungumzo ya awali.

## JARVIS

Mfumo wa mwisho wa wakala tutakaochunguza ni [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Kinachofanya JARVIS kipekee ni kwamba hutumia LLM kusimamia `hali` ya mazungumzo na `zana` ni mifano mingine ya AI. Kila mfano wa AI ni mfano maalum unaotekeleza kazi fulani kama utambuzi wa vitu, uandishi wa maneno, au maelezo ya picha.

![JARVIS](../../../translated_images/sw/jarvis.762ddbadbd1a3a33.webp)

LLM, kuwa mfano wa matumizi ya jumla, hupokea ombi kutoka kwa mtumiaji na kutambua kazi maalum na hoja/data inayohitajika kukamilisha kazi.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kisha huandaa ombi kwa namna ambayo mfano maalum wa AI unaweza kuelewa, kama JSON. Mara mfano wa AI utakaporejelea utabiri wake kulingana na kazi, LLM hupokea jibu.

Ikiwa mifano mingi inahitajika kukamilisha kazi, pia itatafsiri jibu kutoka kwa mifano hiyo kabla ya kuziweka pamoja kutoa jibu kwa mtumiaji.

Mfano hapa chini unaonyesha jinsi hii ingeweza kufanya kazi wakati mtumiaji anamuomba maelezo na hesabu ya vitu katika picha:

## Kazi ya Nyumba

Kuendeleza kujifunza kwako kuhusu Wakala wa AI unaweza kujenga na Mfumo wa Wakala wa Microsoft:

- Programu inayofanikisha mkutano wa biashara na idara tofauti za kuanzisha elimu.
- Unda ujumbe za mfumo zinazowaongoza LLM kuelewa tabia tofauti na kipaumbele, na kuruhusu mtumiaji kuwasilisha wazo jipya la bidhaa.
- LLM kisha inapaswa kuzalisha maswali ya ufuatiliaji kutoka kila idara ili kuboresha na kuimarisha wazo la bidhaa na uwasilishaji.

## Kujifunza hakuishi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia [mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuinua ujuzi wako wa AI ya Kizazi!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->