[![Åpne Kildekode Modeller](../../../translated_images/no/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduksjon

AI-agenter representerer en spennende utvikling innen Generativ AI, som gjør det mulig for store språkmodeller (LLMs) å utvikle seg fra assistenter til agenter som er i stand til å utføre handlinger. AI-agent-rammeverk gjør det mulig for utviklere å lage applikasjoner som gir LLM-er tilgang til verktøy og tilstandsadministrasjon. Disse rammeverkene forbedrer også synligheten, slik at brukere og utviklere kan overvåke handlingene som LLM-ene planlegger, og dermed forbedre opplevelsesstyringen.

Leksjonen vil dekke følgende områder:

- Forstå hva en AI-agent er - Hva er egentlig en AI-agent?
- Utforske fem forskjellige AI-agent-rammeverk - Hva gjør dem unike?
- Anvende disse AI-agentene til ulike brukstilfeller - Når bør vi bruke AI-agenter?

## Læringsmål

Etter å ha tatt denne leksjonen vil du være i stand til å:

- Forklare hva AI-agenter er og hvordan de kan brukes.
- Ha en forståelse av forskjellene mellom noen av de populære AI-agent-rammeverkene, og hvordan de skiller seg.
- Forstå hvordan AI-agenter fungerer for å kunne bygge applikasjoner med dem.

## Hva er AI-agenter?

AI-agenter er et veldig spennende felt innen Generativ AI. Med denne spenningen kommer noen ganger en forvirring rundt begreper og anvendelser. For å holde det enkelt og inkluderende for de fleste verktøyene som refererer til AI-agenter, skal vi bruke denne definisjonen:

AI-agenter lar store språkmodeller (LLMs) utføre oppgaver ved å gi dem tilgang til en **tilstand** og **verktøy**.

![Agentmodell](../../../translated_images/no/what-agent.21f2893bdfd01e6a.webp)

La oss definere disse begrepene:

**Store språkmodeller** - Dette er modellene som omtales gjennom hele dette kurset, som GPT-3.5, GPT-4, Llama-2 osv.

**Tilstand** - Dette refererer til konteksten som LLM-en jobber i. LLM-en bruker konteksten fra sine tidligere handlinger og nåværende kontekst for å styre beslutningstakingen for påfølgende handlinger. AI-agent-rammeverk gjør det lettere for utviklere å opprettholde denne konteksten.

**Verktøy** - For å fullføre oppgaven som brukeren har bedt om og som LLM-en har planlagt, trenger LLM-en tilgang til verktøy. Noen eksempler på verktøy kan være en database, et API, en ekstern applikasjon eller til og med en annen LLM!

Disse definisjonene vil forhåpentligvis gi deg et godt grunnlag videre når vi ser på hvordan de implementeres. La oss utforske noen forskjellige AI-agent-rammeverk:

## LangChain-agenter

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) er en implementering av definisjonene vi ga ovenfor.

For å administrere **tilstanden**, bruker den en innebygd funksjon kalt `AgentExecutor`. Denne tar inn den definerte `agent` og de `verktøyene` som er tilgjengelige for den.

`AgentExecutor` lagrer også chatthistorikken for å gi konteksten for chatten.

![Langchain Agents](../../../translated_images/no/langchain-agents.edcc55b5d5c43716.webp)

LangChain tilbyr en [katalog av verktøy](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) som kan importeres inn i applikasjonen din, slik at LLM-en kan få tilgang til dem. Disse er laget av fellesskapet og LangChain-teamet.

Du kan så definere disse verktøyene og sende dem til `AgentExecutor`.

Synlighet er et annet viktig aspekt når man snakker om AI-agenter. Det er viktig for applikasjonsutviklere å forstå hvilket verktøy LLM-en bruker og hvorfor. For dette har teamet hos LangChain utviklet LangSmith.

## AutoGen

Det neste AI-agent-rammeverket vi skal diskutere er [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hovedfokuset til AutoGen er samtaler. Agenter er både **samtalebare** og **tilpassbare**.

**Samtalebare -** LLM-er kan starte og fortsette en samtale med en annen LLM for å fullføre en oppgave. Dette gjøres ved å lage `AssistantAgents` og gi dem en spesifikk systemmelding.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Tilpassbare** - Agenter kan defineres ikke bare som LLM-er, men også som en bruker eller et verktøy. Som utvikler kan du definere en `UserProxyAgent` som er ansvarlig for å samhandle med brukeren for tilbakemelding ved fullføring av en oppgave. Denne tilbakemeldingen kan enten fortsette utførelsen av oppgaven eller stoppe den.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tilstand og Verktøy

For å endre og administrere tilstanden genererer en assistent-agent Python-kode for å fullføre oppgaven.

Her er et eksempel på prosessen:

![AutoGen](../../../translated_images/no/autogen.dee9a25a45fde584.webp)

#### LLM definert med en systemmelding

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Denne systemmeldingen styrer denne spesifikke LLM-en til hvilke funksjoner som er relevante for oppgaven. Husk at med AutoGen kan du ha flere definerte AssistantAgents med forskjellige systemmeldinger.

#### Chat initieres av bruker

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Denne meldingen fra user_proxy (menneske) er det som starter prosessen for at agenten utforsker mulige funksjoner den bør utføre.

#### Funksjon utføres

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Når den innledende chatten er behandlet, sender agenten det foreslåtte verktøyet som skal kalles. I dette tilfellet er det en funksjon kalt `get_weather`. Avhengig av konfigurasjonen kan denne funksjonen automatisk utføres og leses av agenten, eller utføres basert på brukerinput.

Du kan finne en liste over [AutoGen-kodeeksempler](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) for å utforske nærmere hvordan du kommer i gang med bygging.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) er Microsofts åpen kildekode SDK for å bygge AI-agenter og multi-agent systemer i både **Python** og **.NET**. Det samler styrkene til to tidligere Microsoft-prosjekter — bedriftsfunksjonene til **Semantic Kernel** og multi-agent orkestrering av **AutoGen** — i et enkelt, støttet rammeverk. Hvis du starter et nytt agentprosjekt i dag, er dette den anbefalte etterfølgeren til AutoGen.

Rammeverket skalerer fra en enkelt **chat-agent** til komplekse **multi-agent arbeidsflyter**, og det integreres direkte med Microsoft Foundry, Azure OpenAI og OpenAI. Det tilbyr også innebygd observabilitet gjennom OpenTelemetry slik at du kan spore nøyaktig hva agentene dine gjør.

### Tilstand og Verktøy

**Tilstand** - Rammeverket håndterer samtalekontekst for deg gjennom **threads** (tråder). En agent holder oversikt over meldingshistorikken (brukerforespørsler, verktøysanrop og deres resultater), slik at hvert steg bygger på de foregående. Tråder kan også vedvare, slik at en samtale kan pause og gjenopptas senere.

**Verktøy** - Du gir en agent verktøy ved å sende vanlige Python-funksjoner. Typeannoterte parametere blir automatisk gjort om til et skjema, slik at modellen vet hvordan og når den skal kalle dem (funksjonskall). Rammeverket støtter også Model Context Protocol (MCP) servere og hostede verktøy som en kode-tolker.

Her er et eksempel på en enkelt agent med et spesialtilpasset verktøy:

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

For å koble til Azure OpenAI i Microsoft Foundry i stedet, send endepunktet og legitimasjonen din til klienten:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent arbeidsflyter

Der rammeverket virkelig utmerker seg, er ved orkestrering av flere agenter sammen. For eksempel kan du kjøre agenter etter hverandre (hver overfører sin kontekst til den neste) eller spre til flere agenter parallelt og aggregere deres resultater:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Kjør agenter i rekkefølge, og send samtalekonteksten videre langs kjeden
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Kjør agenter parallelt, og samle deretter svarene deres
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

For å installere rammeverket og komme i gang:

```bash
pip install agent-framework-core
# Valgfrie integrasjoner
pip install agent-framework-openai       # OpenAI og Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kan utforske mer i [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) og den [offisielle dokumentasjonen](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Det neste agent-rammeverket vi skal utforske er [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Det er kjent som en "kode-først" agent fordi den i stedet for å jobbe strengt med `strings`, kan jobbe med DataFrames i Python. Dette blir ekstremt nyttig for dataanalyse og generering. Dette kan være ting som å lage grafer og diagrammer eller generere tilfeldige tall.

### Tilstand og Verktøy

For å administrere samtalens tilstand bruker TaskWeaver konseptet `Planner`. `Planner` er en LLM som tar imot forespørselen fra brukerne og kartlegger oppgavene som må utføres for å oppfylle denne forespørselen.

For å fullføre oppgavene får `Planner` tilgang til en samling verktøy kalt `Plugins`. Dette kan være Python-klasser eller en generell kode-tolker. Disse pluginene lagres som embeddings slik at LLM-en kan søke mer effektivt etter riktig plugin.

![Taskweaver](../../../translated_images/no/taskweaver.da8559999267715a.webp)

Her er et eksempel på en plugin for å håndtere anomali-detektering:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden blir verifisert før utførelse. En annen funksjon for å administrere kontekst i Taskweaver er `experience`. Erfaring tillater at konteksten av en samtale lagres over tid i en YAML-fil. Dette kan konfigureres slik at LLM-en forbedres over tid på visse oppgaver ved at den får tilgang til tidligere samtaler.

## JARVIS

Det siste agent-rammeverket vi skal utforske er [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Det som gjør JARVIS unikt er at den bruker en LLM for å administrere `tilstanden` i samtalen, og at `verktøyene` er andre AI-modeller. Hver av AI-modellene er spesialiserte modeller som utfører bestemte oppgaver som objektgjenkjenning, transkripsjon eller bildekaptiering.

![JARVIS](../../../translated_images/no/jarvis.762ddbadbd1a3a33.webp)

LLM-en, som er en generell modell, mottar forespørselen fra brukeren og identifiserer den spesifikke oppgaven og eventuelle argumenter/data som trengs for å fullføre oppgaven.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM-en formaterer deretter forespørselen på en måte som den spesialiserte AI-modellen kan tolke, for eksempel JSON. Når AI-modellen har returnert sin prediksjon basert på oppgaven, mottar LLM-en svaret.

Hvis flere modeller kreves for å fullføre oppgaven, vil den også tolke responsen fra disse modellene før den samler dem for å generere svaret til brukeren.

Eksempelet nedenfor viser hvordan dette vil fungere når en bruker ber om en beskrivelse og telling av objektene i et bilde:

## Oppgave

For å fortsette læringen din om AI-agenter kan du bygge med Microsoft Agent Framework:

- En applikasjon som simulerer et forretningsmøte med forskjellige avdelinger i en utdanningsoppstart.
- Lag systemmeldinger som veileder LLM-ene i å forstå forskjellige personaer og prioriteringer, og gjør det mulig for brukeren å presentere en ny produktidé.
- LLM-en bør deretter generere oppfølgingsspørsmål fra hver avdeling for å forbedre og utvikle presentasjonen og produktideen.

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å øke din kunnskap om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->