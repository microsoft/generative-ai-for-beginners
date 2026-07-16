[![Atviro kodo modeliai](../../../translated_images/lt/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Įvadas

DI agentai žymi įdomią pažangą generuojančioje DI srityje, leidžiančią didelių kalbų modeliams (LLM) evoliucionuoti iš asistentų į agentus, galinčius imtis veiksmų. DI agentų karkasai leidžia kūrėjams kurti programas, suteikiančias LLM prieigą prie įrankių ir būsenos valdymo. Šie karkasai taip pat didina matomumą, leidžiantį vartotojams ir kūrėjams stebėti LLM planuojamus veiksmus, tokiu būdu gerinant patirties valdymą.

Pamoka apims šias sritis:

- Supratimą, kas yra DI agentas – kas iš tikrųjų yra DI agentas?
- Penkių skirtingų DI agentų karkasų tyrimą – kuo jie unikalūs?
- DI agentų taikymą skirtingais atvejais – kada reikėtų naudoti DI agentus?

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Paaiškinti, kas yra DI agentai ir kaip juos galima naudoti.
- Suprasti skirtumus tarp populiariausių DI agentų karkasų ir kuo jie skiriasi.
- Suprasti, kaip veikia DI agentai, kad galėtumėte kurti taikomąsias programas su jais.

## Kas yra DI agentai?

DI agentai yra labai įdomi sritis generuojančioje DI pasaulyje. Su šiuo susidomėjimu kartais kyla terminų ir jų taikymo painiava. Norėdami supaprastinti ir apimti daugumą įrankių, kurie vadina save DI agentais, naudosime šią apibrėžtį:

DI agentai leidžia dideliems kalbų modeliams (LLM) atlikti užduotis suteikiant jiems prieigą prie **būsenos** ir **įrankių**.

![Agentų modelis](../../../translated_images/lt/what-agent.21f2893bdfd01e6a.webp)

Apibrėžkime šiuos terminus:

**Dideli kalbų modeliai** – tai modeliai, apie kuriuos kalbama šiame kurse, kaip GPT-3.5, GPT-4, Llama-2 ir kt.

**Būsena** – tai kontekstas, kuriame LLM dirba. LLM naudoja savo ankstesnių veiksmų ir esamą kontekstą vadovaudamasis sprendimams dėl tolesnių veiksmų. DI agentų karkasai leidžia kūrėjams lengviau palaikyti šį kontekstą.

**Įrankiai** – norint įvykdyti vartotojo pateiktą ir LLM suplanuotą užduotį, LLM reikia prieigos prie įrankių. Tai gali būti duomenų bazė, API, išorinė programa ar net kitas LLM!

Tikimės, kad šie apibrėžimai suteiks jums gerą pagrindą tolimesniame įrankių tvarkyme. Pažvelkime į keletą skirtingų DI agentų karkasų:

## LangChain agentai

[LangChain agentai](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) yra aukščiau pateiktų apibrėžimų įgyvendinimas.

Norint valdyti **būseną**, naudojama įmontuota funkcija `AgentExecutor`. Ji priima apibrėžtą `agent` ir prieinamus `įrankius`.

`AgentExecutor` taip pat saugo pokalbio istoriją, kad suteiktų kontekstą pokalbiui.

![Langchain agentai](../../../translated_images/lt/langchain-agents.edcc55b5d5c43716.webp)

LangChain siūlo [įrankių katalogą](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), kuris gali būti importuotas į jūsų programą ir prie jo gali prieiti LLM. Juos kuria bendruomenė ir LangChain komanda.

Jūs galite apibrėžti šiuos įrankius ir perduoti juos `AgentExecutor`.

Matomumas yra dar vienas svarbus aspektas, kalbant apie DI agentus. Svarbu, kad programų kūrėjai suprastų, kurį įrankį LLM naudoja ir kodėl. Tam LangChain komanda sukūrė LangSmith.

## AutoGen

Kitas DI agentų karkasas, apie kurį kalbėsime, yra [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGen pagrindinis dėmesys skiriamas pokalbiams. Agentai yra tiek **pokalbių galintys**, tiek **pritaikomi**.

**Pokalbių galintys –** LLM gali pradėti ir tęsti pokalbį su kitu LLM, kad įvykdytų užduotį. Tai įgyvendinama kuriant `AssistantAgents` ir suteikiant jiems specifinį sistemos pranešimą.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Pritaikomi** – agentus galima apibrėžti ne tik kaip LLM, bet ir kaip vartotoją ar įrankį. Kūrėjas gali apibrėžti `UserProxyAgent`, kuris yra atsakingas už vartotojo sąveiką siekiant gauti atsiliepimų užduoties vykdymui. Šie atsiliepimai gali tęsti arba nutraukti užduoties vykdymą.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Būsena ir įrankiai

Būsenos keitimui ir valdymui, pagalbinis agentas generuoja Python kodą užduočiai įvykdyti.

Štai proceso pavyzdys:

![AutoGen](../../../translated_images/lt/autogen.dee9a25a45fde584.webp)

#### LLM apibrėžtas su sistemos pranešimu

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Šis sistemos pranešimas nurodo šiam konkrečiam LLM, kurios funkcijos yra svarbios jo užduočiai. Atminkite, kad AutoGen galite turėti kelis apibrėžtus AssistantAgents su skirtingais sistemos pranešimais.

#### Pokalbis inicijuojamas vartotojo

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Šis pranešimas iš user_proxy (žmogaus) pradės agento procesą tirti galimas funkcijas, kurias reikia įvykdyti.

#### Vykdoma funkcija

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kai pradinė pokalbio dalis apdorojama, agentas siunčia siūlomą įrankį paleisti. Šiuo atveju tai funkcija `get_weather`. Priklausomai nuo jūsų konfigūracijos, ši funkcija gali būti automatiškai vykdoma ir perskaitoma agento arba paleidžiama pagal vartotojo įvestį.

Galite rasti [AutoGen kodo pavyzdžių](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), kad plačiau susipažintumėte, kaip pradėti kurti.

## Microsoft agentų karkasas

[Microsoft agentų karkasas](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) yra „Microsoft“ atviro kodo SDK, skirtas kurti DI agentams ir daugiagentinėms sistemoms tiek **Python**, tiek **.NET** aplinkose. Jis sujungia dviejų ankstesnių Microsoft projektų stiprybes — įmonių funkcionalumą iš **Semantic Kernel** ir daugiagentų derinimą iš **AutoGen** — į vieną palaikomą karkasą. Jei šiandien pradedate naują agentų projektą, tai yra rekomenduojamas AutoGen įpėdinis.

Šis karkasas pritaikomas nuo vieno **pokalbių agento** iki sudėtingų **daugiagentinių darbo procesų**, ir jis tiesiogiai integruojasi su Microsoft Foundry, Azure OpenAI ir OpenAI. Jis taip pat suteikia integruotą stebėjimo galią per OpenTelemetry, kad galėtumėte tiksliai sekti, ką jūsų agentai veikia.

### Būsena ir įrankiai

**Būsena** – karkasas valdo pokalbio kontekstą už jus per **gijas**. Agentas saugo žinučių istoriją (vartotojų užklausas, įrankių kvietimus ir jų rezultatus), taigi kiekvienas žingsnis kaupia informaciją iš ankstesnių. Gijos taip pat gali būti išsaugotos, leidžiant pokalbį sustabdyti ir vėliau tęsti.

**Įrankiai** – suteikiate agentui įrankius, perduodami paprastas Python funkcijas. Parametrai su tipų anotacijomis automatiškai paverčiami į schemą, todėl modelis žino, kaip ir kada jas kvieti (funkcijų kvietimas). Karkasas taip pat palaiko Model Context Protocol (MCP) serverius ir įrankius, tokius kaip kodo interpretatorius.

Štai pavyzdys, kaip atrodo vienas agentas su pritaikytu įrankiu:

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

Norėdami vietoj to prisijungti prie Azure OpenAI Microsoft Foundry, perduokite savo galinį tašką ir kredencialus klientui:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Daugiagentiniai darbo procesai

Šis karkasas ypač išsiskiria derinant kelis agentus kartu. Pavyzdžiui, galite paleisti agentus vieną po kito (kiekvienas perduodantis kitam savo kontekstą) arba skirstyti užduotis keliems agentams paraleliai ir sujungti jų rezultatus:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Vykdykite agentus sekos tvarka, perduodami pokalbio kontekstą per grandinę
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Paskirstykite agentams lygiagrečiai, tada sujunkite jų atsakymus
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Norėdami įdiegti karkasą ir pradėti darbą:

```bash
pip install agent-framework-core
# Pasirenkamos integracijos
pip install agent-framework-openai       # OpenAI ir Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Daugiau sužinoti galite [Microsoft Agent Framework saugykloje](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ir [oficialioje dokumentacijoje](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kitas agentų karkasas, kurį apžvelgsime, yra [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Jis žinomas kaip „kodo pirmas“ agentas, nes vietoje darbo tik su `strings` gali dirbti su DataFrame struktūromis Python kalboje. Tai itin naudinga duomenų analizės ir generavimo užduotims. Tai gali būti pvz., grafų ir diagramų kūrimas arba atsitiktinių skaičių generavimas.

### Būsena ir įrankiai

Valdyti pokalbio būseną TaskWeaver naudoja koncepciją `Planner`. `Planner` yra LLM, kuris ima vartotojo užklausą ir išdėsto užduotis, kurias reikia įvykdyti tam užsakymui įgyvendinti.

Siekiant įvykdyti užduotis, `Planner` turi prieigą prie įrankių rinkinio, vadinamo `Plugins`. Tai gali būti Python klasės ar bendras kodo interpretatorius. Šie papildiniai saugomi kaip įterpiniai (embeddings), kad LLM galėtų geriau ieškoti tinkamo papildinio.

![Taskweaver](../../../translated_images/lt/taskweaver.da8559999267715a.webp)

Štai pavyzdys papildinio anomalijų aptikimui:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kodas patikrinamas prieš vykdymą. Kita būsenos valdymo Taskweaver ypatybė yra `experience`. Patirtis leidžia pokalbio kontekstą saugoti ilgalaikėje YAML byloje. Tai galima konfigūruoti taip, kad LLM gerėtų laikui bėgant tam tikrose užduotyse, gavęs prieigą prie ankstesnių pokalbių.

## JARVIS

Paskutinis agentų karkasas, kurį apžvelgsime, yra [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVIS unikalumas yra tas, kad jis naudoja LLM pokalbio `būsenos` valdymui, o `įrankiais` yra kiti DI modeliai. Kiekvienas DI modelis yra specializuotas modelis, atliekantis tam tikras užduotis, pvz., objektų atpažinimą, transkripciją ar vaizdo aprašymus.

![JARVIS](../../../translated_images/lt/jarvis.762ddbadbd1a3a33.webp)

LLM, būdamas bendros paskirties modeliu, gauna vartotojo užklausą ir identifikuoja konkrečią užduotį bei visus argumentus/duomenis, reikalingus užduočiai įvykdyti.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM tuomet formatuoja užklausą taip, kad specializuotas DI modelis galėtų ją interpretuoti, pavyzdžiui, JSON formatu. Kai DI modelis pateikia prognozę pagal užduotį, LLM gauna atsakymą.

Jei užduočiai įvykdyti reikia kelių modelių, LLM taip pat interpretuoja jų atsakymus prieš sujungdamas juos į bendrą atsakymą vartotojui.

Žemiau pateiktas pavyzdys parodo, kaip tai veikia, kai vartotojas prašo aprašymo ir objektų skaičiaus nuotraukoje:

## Užduotis

Toliau gilindamiesi į DI agentus galite kurti su Microsoft agentų karkasu:

- Programą, kuri simuliuoja verslo susitikimą su įvairiais švietimo startuolio skyriais.
- Kurkite sistemos pranešimus, kurie padeda LLM suprasti skirtingas personas ir prioritetus, bei leidžia vartotojui pristatyti naują produkto idėją.
- Tada LLM turėtų sugeneruoti tolimesnius klausimus iš kiekvieno skyriaus idėjos patobulinimui ir pristatymo gerinimui.

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką peržiūrėkite mūsų [Generuojančios DI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau keltumėte savo generuojančios DI žinias į aukštesnį lygį!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->