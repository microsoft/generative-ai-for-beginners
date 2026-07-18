[![Open Source Models](../../../translated_images/da/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduktion

AI-agenter repræsenterer en spændende udvikling inden for Generativ AI, som gør det muligt for store sprogmodeller (LLM'er) at udvikle sig fra assistenter til agenter, der er i stand til at udføre handlinger. AI-agent-rammeværker gør det muligt for udviklere at skabe applikationer, der giver LLM'er adgang til værktøjer og tilstandsstyring. Disse rammeværker forbedrer også synligheden, så brugere og udviklere kan overvåge de handlinger, som LLM'erne planlægger, hvilket forbedrer oplevelsesstyringen.

Lektionen vil dække følgende områder:

- Forstå hvad en AI-agent er - Hvad er en AI-agent præcist?
- Udforske fem forskellige AI-agent-rammeværker - Hvad gør dem unikke?
- Anvende disse AI-agenter til forskellige anvendelsestilfælde - Hvornår bør vi bruge AI-agenter?

## Læringsmål

Efter at have taget denne lektion vil du kunne:

- Forklare, hvad AI-agenter er, og hvordan de kan bruges.
- Have forståelse for forskellene mellem nogle af de populære AI-agent-rammeværker, og hvordan de adskiller sig.
- Forstå, hvordan AI-agenter fungerer for at kunne bygge applikationer med dem.

## Hvad er AI-agenter?

AI-agenter er et meget spændende område inden for Generativ AI. Med denne spænding følger nogle gange en forvirring om termer og deres anvendelse. For at holde det enkelt og inkluderende for de fleste af de værktøjer, der henvises til som AI-agenter, vil vi bruge denne definition:

AI-agenter giver store sprogmodeller (LLM'er) mulighed for at udføre opgaver ved at give dem adgang til en **tilstand** og **værktøjer**.

![Agent Model](../../../translated_images/da/what-agent.21f2893bdfd01e6a.webp)

Lad os definere disse termer:

**Store sprogmodeller** - Disse er de modeller, der omtales gennem dette kursus såsom GPT-5, GPT-4o og Llama 3.3 osv.

**Tilstand** - Dette henviser til den kontekst, som LLM'en arbejder i. LLM'en bruger konteksten fra sine tidligere handlinger samt den aktuelle kontekst, som styrer dens beslutningstagning for efterfølgende handlinger. AI-agent-rammeværker gør det lettere for udviklere at vedligeholde denne kontekst.

**Værktøjer** - For at fuldføre den opgave, som brugeren har anmodet om, og som LLM'en har planlagt, har LLM'en brug for adgang til værktøjer. Nogle eksempler på værktøjer kan være en database, et API, en ekstern applikation eller endda en anden LLM!

Disse definitioner vil forhåbentlig give dig et godt fundament fremadrettet, når vi ser på, hvordan de implementeres. Lad os udforske et par forskellige AI-agent-rammeværker:

## LangChain Agenter

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) er en implementering af de definitioner, vi gav ovenfor.

For at håndtere **tilstanden** bruger den en indbygget funktion kaldet `AgentExecutor`. Denne modtager den definerede `agent` og de `værktøjer`, der er tilgængelige for den.

`Agent Executor` gemmer også chathistorikken for at give konteksten for samtalen.

![Langchain Agents](../../../translated_images/da/langchain-agents.edcc55b5d5c43716.webp)

LangChain tilbyder en [katalog af værktøjer](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), som kan importeres til din applikation, og som LLM'en kan få adgang til. Disse er lavet af fællesskabet og LangChain-teamet.

Du kan derefter definere disse værktøjer og sende dem til `Agent Executor`.

Synlighed er et andet vigtigt aspekt, når man taler om AI-agenter. Det er vigtigt for applikationsudviklere at forstå, hvilket værktøj LLM'en bruger, og hvorfor. Til det har teamet hos LangChain udviklet LangSmith.

## AutoGen

Det næste AI-agent-rammeværk, vi vil diskutere, er [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGens hovedfokus er samtaler. Agenter er både **samtalebare** og **tilpasselige**.

**Samtalebare -** LLM'er kan starte og fortsætte en samtale med en anden LLM for at fuldføre en opgave. Dette gøres ved at skabe `AssistantAgents` og give dem en specifik systembesked.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Tilpasselige** - Agenter kan defineres ikke kun som LLM'er, men også som en bruger eller et værktøj. Som udvikler kan du definere en `UserProxyAgent`, som er ansvarlig for at interagere med brugeren for feedback i at fuldføre en opgave. Denne feedback kan enten fortsætte udførelsen af opgaven eller stoppe den.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tilstand og værktøjer

For at ændre og styre tilstand genererer en assisterende Agent Python-kode for at fuldføre opgaven.

Her er et eksempel på processen:

![AutoGen](../../../translated_images/da/autogen.dee9a25a45fde584.webp)

#### LLM defineret med en systembesked

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Denne systembesked leder denne specifikke LLM til, hvilke funktioner der er relevante for dens opgave. Husk, med AutoGen kan du have flere definerede AssistantAgents med forskellige systembeskeder.

#### Samtale initieres af bruger

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Denne besked fra user_proxy (mennesket) vil starte processen for agenten til at udforske de mulige funktioner, som den bør udføre.

#### Funktion udføres

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Når den indledende chat er behandlet, sender agenten det foreslåede værktøj, der skal kaldes. I dette tilfælde er det en funktion kaldet `get_weather`. Afhængigt af din konfiguration kan denne funktion automatisk blive udført og læst af agenten eller blive udført baseret på brugerinput.

Du kan finde en liste over [AutoGen-eksempelkoder](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) for yderligere at udforske, hvordan man kommer i gang med at bygge.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) er Microsofts open source SDK til at bygge AI-agenter og multi-agent systemer i både **Python** og **.NET**. Det samler styrkerne fra to tidligere Microsoft projekter — virksomhedsfunktionerne af **Semantic Kernel** og multi-agent orkestreringen af **AutoGen** — i ét enkelt, understøttet rammeværk. Hvis du starter et nyt agentprojekt i dag, er dette den anbefalede efterfølger til AutoGen.

Rammeværket skalerer fra en enkelt **chat-agent** helt op til komplekse **multi-agent arbejdsgange**, og det integreres direkte med Microsoft Foundry, Azure OpenAI og OpenAI. Det tilbyder også indbygget observerbarhed gennem OpenTelemetry, så du præcist kan spore, hvad dine agenter foretager sig.

### Tilstand og værktøjer

**Tilstand** - Rammeværket håndterer samtalekonteksten for dig gennem **tråde**. En agent holder styr på beskedhistorikken (brugeranmodninger, værktøjskald og deres resultater), så hvert trin bygger videre på de tidligere. Tråde kan også gemmes, så en samtale kan pauses og genoptages senere.

**Værktøjer** - Du giver en agent værktøjer ved at sende almindelige Python-funktioner. Typeannoterede parametre bliver automatisk omdannet til et skema, så modellen ved, hvordan og hvornår den skal kalde dem (funktionkald). Rammeværket understøtter også Model Context Protocol (MCP) servere og hostede værktøjer såsom en kodefortolker.

Her er et eksempel på en enkelt agent med et brugerdefineret værktøj:

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

For at forbinde til Azure OpenAI i Microsoft Foundry i stedet sender du dit endpoint og dine legitimationsoplysninger til klienten:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent arbejdsgange

Hvor rammeværket virkelig skiller sig ud, er orkestreringen af flere agenter sammen. For eksempel kan du køre agenter efter hinanden (hver videregiver sin kontekst til den næste) eller sprede til flere agenter parallelt og samle deres resultater:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Kør agenter i rækkefølge og send samtalekontexten videre i kæden
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Spred opgaven til agenter parallelt, og saml derefter deres svar sammen
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

For at installere rammeværket og komme i gang:

```bash
pip install agent-framework-core
# Valgfrie integrationer
pip install agent-framework-openai       # OpenAI og Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kan undersøge mere i [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) og den [officielle dokumentation](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Det næste agent-rammeværk, vi vil udforske, er [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Det er kendt som en "kode-først" agent, fordi den i stedet for kun at arbejde med `strings`, kan arbejde med DataFrames i Python. Dette bliver ekstremt nyttigt til dataanalyser og genereringsopgaver. Det kan være ting som at skabe grafer og diagrammer eller generere tilfældige tal.

### Tilstand og værktøjer

For at styre samtalens tilstand bruger TaskWeaver konceptet `Planner`. `Planner` er en LLM, som tager brugernes anmodning og kortlægger de opgaver, der skal udføres for at opfylde denne anmodning.

For at fuldføre opgaverne eksponeres `Planner` for en samling af værktøjer kaldet `Plugins`. Dette kan være Python-klasser eller en generel kodefortolker. Disse plugins er gemt som embeddings, så LLM kan søge bedre efter det korrekte plugin.

![Taskweaver](../../../translated_images/da/taskweaver.da8559999267715a.webp)

Her er et eksempel på et plugin til at håndtere anomalidetektion:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden bliver verificeret, inden den køres. En anden funktion til at styre konteksten i Taskweaver er `experience`. Experience tillader, at konteksten af en samtale gemmes på længere sigt i en YAML-fil. Dette kan konfigureres, så LLM forbedres over tid på visse opgaver, forudsat at den eksponeres for tidligere samtaler.

## JARVIS

Det sidste agent-rammeværk, vi vil udforske, er [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Det, der gør JARVIS unikt, er, at den bruger en LLM til at styre `tilstanden` af samtalen, og at `værktøjerne` er andre AI-modeller. Hver af AI-modellerne er specialiserede modeller, der udfører bestemte opgaver såsom objektgenkendelse, transskription eller billedbeskrivelse.

![JARVIS](../../../translated_images/da/jarvis.762ddbadbd1a3a33.webp)

LLM'en, som er en generel formålsmodel, modtager anmodningen fra brugeren og identificerer den specifikke opgave og eventuelle argumenter/data, der er nødvendige for at fuldføre opgaven.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM'en formaterer derefter anmodningen på en måde, som den specialiserede AI-model kan fortolke, såsom JSON. Når AI-modellen har returneret sin forudsigelse baseret på opgaven, modtager LLM svaret.

Hvis der kræves flere modeller for at fuldføre opgaven, vil den også fortolke svarene fra disse modeller, før den sætter dem sammen for at generere svaret til brugeren.

Eksemplet nedenfor viser, hvordan dette ville fungere, når en bruger anmoder om en beskrivelse og optælling af objekter i et billede:

## Opgave

For at fortsætte din læring om AI-agenter kan du bygge med Microsoft Agent Framework:

- En applikation, der simulerer et forretningsmøde med forskellige afdelinger i en uddannelsesopstart.
- Opret systembeskeder, der guider LLM'erne i at forstå forskellige personaer og prioriteter, og gør det muligt for brugeren at præsentere en ny produktidé.
- LLM'en skal derefter generere opfølgende spørgsmål fra hver afdeling for at raffinere og forbedre præsentationen og produktideen.

## Læringen stopper ikke her, fortsæt rejsen

Efter at have gennemført denne lektion kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->