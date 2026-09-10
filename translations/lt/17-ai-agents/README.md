[![Atviro kodo modeliai](../../../translated_images/lt/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Įvadas

Dirbtinio intelekto agentai yra įdomi generatyvaus DI pažanga, leidžianti dideliems kalbos modeliams (LLM) evoliucionuoti iš asistentų į agentus, galinčius imtis veiksmų. Dirbtinio intelekto agentų sistemos leidžia kūrėjams kurti programas, suteikiančias LLM prieigą prie įrankių ir būsenos valdymą. Šios sistemos taip pat pagerina matomumą, leidžiančią vartotojams ir kūrėjams stebėti LLM numatomus veiksmus, taip gerinant patirties valdymą.

Pamoka apims šias sritis:

- Suprasti, kas yra dirbtinio intelekto agentas – kas tiksliai yra DI agentas?
- Išnagrinėti penkias skirtingas DI agentų sistemas – kuo jos unikalios?
- Taikyti šiuos DI agentus įvairiems naudojimo atvejams – kada verta naudoti DI agentus?

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Paaiškinti, kas yra DI agentai ir kaip juos galima naudoti.
- Suprasti skirtumus tarp populiarių DI agentų sistemų ir kuo jos skiriasi.
- Suprasti, kaip veikia DI agentai, kad galėtumėte kurti programas naudodami juos.

## Kas yra DI agentai?

DI agentai yra labai įdomi sritis generatyvaus DI pasaulyje. Su šiuo susidomėjimu kartais kyla ir terminų bei jų taikymo painiava. Norėdami supaprastinti ir apimti daugumą įrankių, vadinamų DI agentais, naudosime šią apibrėžtį:

DI agentai leidžia dideliems kalbos modeliams (LLM) atlikti užduotis, suteikdami jiems prieigą prie **būsenos** ir **įrankių**.

![Agentų modelis](../../../translated_images/lt/what-agent.21f2893bdfd01e6a.webp)

Apibrėžkime šiuos terminus:

**Dideli kalbos modeliai** – šie modeliai aptariami viso kurso metu, pavyzdžiui, GPT-5, GPT-4o ir Llama 3.3 ir kt.

**Būsena** – tai kontekstas, kuriame LLM dirba. LLM naudoja savo ankstesnių veiksmų ir dabartinį kontekstą, kuris nukreipia sprendimų priėmimą dėl tolesnių veiksmų. DI agentų sistemos leidžia kūrėjams lengviau palaikyti šį kontekstą.

**Įrankiai** – norint įvykdyti vartotojo užklausą ir LLM suplanuotus veiksmus, LLM reikia prieigos prie įrankių. Kai kurie pavyzdžiai: duomenų bazė, API, išorinė programa arba net kitas LLM!

Šie apibrėžimai, tikimės, suteiks gerą pagrindą, kai žvelgsime, kaip jie įgyvendinami. Pažvelkime į keletą skirtingų DI agentų sistemų:

## LangChain agentai

[LangChain agentai](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) įgyvendina aukščiau pateiktus apibrėžimus.

Būdama būsenos valdymo dalimi, ji naudoja integruotą funkciją `AgentExecutor`. Ji priima apibrėžtą `agent` ir prieinamus `tools`.

`AgentExecutor` taip pat saugo pokalbio istoriją, kad pateiktų pokalbio kontekstą.

![LangChain agentai](../../../translated_images/lt/langchain-agents.edcc55b5d5c43716.webp)

LangChain siūlo [įrankių katalogą](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), kurį galite importuoti į savo programą, kad LLM galėtų prie jų prisijungti. Šiuos įrankius kuria bendruomenė ir LangChain komanda.

Tuomet galite apibrėžti šiuos įrankius ir perduoti juos `AgentExecutor`.

Matomumas yra dar vienas svarbus aspektas kalbant apie DI agentus. Svarbu programų kūrėjams suprasti, kokį įrankį LLM naudoja ir kodėl. Tam LangChain komanda sukūrė LangSmith.

## AutoGen

Kita DI agentų sistema, apie kurią kalbėsime, yra [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Pagrindinis AutoGen dėmesys – pokalbiai. Agentai yra tiek **pokalbiai draugiški**, tiek **pritaikomi**.

**Pokalbiai draugiški** – LLM gali pradėti ir tęsti pokalbį su kitu LLM, kad įvykdytų užduotį. Tai daroma kuriant `AssistantAgents` su konkrečiomis sistemos žinutėmis.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Pritaikomi** – Agentai gali būti apibrėžti ne tik kaip LLM, bet ir kaip vartotojas ar įrankis. Kaip kūrėjas, galite apibrėžti `UserProxyAgent`, kuris atsakingas už vartotojo sąveiką ir atsiliepimus vykdant užduotį. Šie atsiliepimai gali tęsti arba nutraukti užduoties vykdymą.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Būsena ir įrankiai

Būsenos keitimui ir valdymui pagalbinis agentas generuoja Python kodą užduoties atlikimui.

Štai pavyzdys, kaip vyksta procesas:

![AutoGen](../../../translated_images/lt/autogen.dee9a25a45fde584.webp)

#### LLM apibrėžtas sistemos žinute

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ši sistema nukreipia konkretų LLM, kokios funkcijos yra svarbios jo užduočiai. Atminkite, su AutoGen galite turėti kelis apibrėžtus AssistantAgents su skirtingomis sistemos žinutėmis.

#### Pokalbis pradėtas vartotojo

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ši žinutė iš user_proxy (žmogaus) paleidžia agento procesą tirti galimas funkcijas, kurias reikia vykdyti.

#### Funkcija vykdoma

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po pradinio pokalbio apdorojimo agentas pasiūlo įrankį iškviesti. Šiuo atveju – tai funkcija `get_weather`. Priklausomai nuo konfigūracijos, ši funkcija gali būti automatiškai vykdoma ir skaitoma agento arba vykdoma pagal vartotojo įvestį.

[AutoGen kodo pavyzdžių](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) galite rasti sąrašą, kuris padės gilintis, kaip pradėti kurti.

## Microsoft agentų sistema

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) yra Microsoft atvirojo kodo SDK DI agentų ir daugiagentinių sistemų kūrimui tiek **Python**, tiek **.NET** aplinkoje. Ji sujungia dviejų ankstesnių Microsoft projektų privalumus – įmonės ypatybes iš **Semantic Kernel** ir daugiagentinės orkestracijos iš **AutoGen** – į vieną, palaikomą sistemą. Jei šiandien pradedate naują agentų projektą, rekomenduojama naudoti šią AutoGen tęsinį.

Sistema gali apimti vieną **pokalbių agentą** iki sudėtingų **daugiagentinių procesų** ir tiesiogiai integruojasi su Microsoft Foundry, Azure OpenAI bei OpenAI. Ji taip pat suteikia integruotą stebėseną per OpenTelemetry, todėl galite tiksliai sekti, ką daro jūsų agentai.

### Būsena ir įrankiai

**Būsena** – sistema valdo pokalbio kontekstą per **gijas** (threads). Agentas seka žinučių istoriją (vartotojo užklausas, įrankių kvietimus ir rezultatus), todėl kiekvienas raundas remiasi ankstesniais. Gijas galima išsaugoti, leidžiant sustabdyti ir vėliau tęsti pokalbį.

**Įrankiai** – įrankius agentui suteikiate perduodami paprastas Python funkcijas. Tipais pažymėti parametrai automatiškai paverčiami schema, tad modelis žino, kaip ir kada jas iškviesti (funkcijų iškvietimas). Sistema taip pat palaiko Model Context Protocol (MCP) serverius ir talpinamus įrankius, pvz., kodo interpretuotoją.

Štai pavyzdys apie vieną agentą su pritaikytu įrankiu:

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

Norint vietoj to prisijungti prie Azure OpenAI Microsoft Foundry, perduokite savo galinį tašką ir prisijungimo duomenis klientui:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Daugiagentiniai procesai

Išskirtinumas yra kelių agentų koordinavimas kartu. Pavyzdžiui, galite paleisti agentus vieną po kito (kiekvienas perduoda savo kontekstą kitam), arba paleisti kelis agentus lygiagrečiai ir sujungti jų rezultatus:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Paleiskite agentus paeiliui, perduodami pokalbio kontekstą per grandinę
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Plėskite agentus lygiagrečiai, tada sujunkite jų atsakymus
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Norėdami įdiegti sistemą ir pradėti darbą:

```bash
pip install agent-framework-core
# Neprivalomos integracijos
pip install agent-framework-openai       # OpenAI ir Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Daugiau galite sužinoti [Microsoft Agent Framework saugykloje](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ir [oficialioje dokumentacijoje](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kita agentų sistema, kurią išnagrinėsime, yra [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ji žinoma kaip "kodu pirmiausia" agentas, nes vietoj darbo vien su `eilutėmis` gali dirbti su Python DataFrame’ais. Tai ypač naudinga atliekant duomenų analizės ir generavimo užduotis, pavyzdžiui, kuriant grafikus ir diagramas arba generuojant atsitiktinius skaičius.

### Būsena ir įrankiai

Būsena valdoma per `Planner` – tai LLM, kuris gauna vartotojų užklausą ir suplanuoja užduotis, kurias reikia atlikti, kad būtų įvykdyta ši užklausa.

Atlikimui `Planner` yra suteikta prieiga prie įrankių rinkinio pavadinimu `Plugins`. Tai gali būti Python klasės ar bendras kodo interpretuotojas. Šie įskiepiai saugomi kaip embeddingai, kad LLM galėtų lengviau surasti tinkamą įskiepį.

![Taskweaver](../../../translated_images/lt/taskweaver.da8559999267715a.webp)

Štai pavyzdys, kaip įskiepis tvarko anomalijų aptikimą:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kodo patikrinimas atliekamas prieš vykdymą. Kitas būdas valdyti kontekstą Taskweaver yra `experience`. Ši patirtis leidžia pokalbio kontekstą saugoti ilgalaikiame YAML faile. Tai galima konfigūruoti taip, kad LLM laikui bėgant pagerėtų tam tikrose užduotyse, mat jį veiktų ankstesni pokalbiai.

## JARVIS

Paskutinė agentų sistema, kurią apžvelgsime, yra [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVIS unikalumas ta, kad jis naudoja LLM valdyti pokalbio `būseną`, o `įrankiai` yra kiti DI modeliai. Kiekvienas šių DI modelių yra specializuotas atlikti tam tikras užduotis, tokias kaip objektų aptikimas, transkripcija ar vaizdo anotavimas.

![JARVIS](../../../translated_images/lt/jarvis.762ddbadbd1a3a33.webp)

LLM, kaip bendros paskirties modelis, gauna užklausą iš vartotojo ir identifikuoja specifinę užduotį bei reikiamus argumentus/duomenis užduočiai atlikti.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM tada formatuoja užklausą taip, kad specializuotas DI modelis galėtų ją interpretuoti, pavyzdžiui, JSON formatu. Kai DI modelis pateikia prognozę pagal užduotį, LLM gauna atsakymą.

Jei užduočiai atlikti reikia kelių modelių, jis taip pat interpretuoja jų atsakymus prieš sujungdamas juos į atsakymą vartotojui.

Toliau pateiktas pavyzdys rodo, kaip tai veiktų, kai vartotojas užklausia apibūdinimo ir objektų skaičiaus nuotraukoje:

## Užduotis

Norėdami tęsti mokymą apie DI agentus, galite kurti su Microsoft Agent Framework:

- Programą, simuliuojančią verslo susitikimą su skirtingais švietimo pradedančios įmonės skyriais.
- Sukurkite sistemos žinutes, kurios nukreiptų LLM suprasti skirtingas personas ir prioritetus bei leistų vartotojui pristatyti naują produkto idėją.
- LLM turėtų sukurti klausimus iš kiekvieno skyriaus, kad patikslintų ir pagerintų pristatymą bei produkto idėją.

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, apsilankykite mūsų [Generatyvaus DI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gerintumėte savo žinias apie generatyvų DI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->