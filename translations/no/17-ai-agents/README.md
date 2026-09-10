[![Open Source Models](../../../translated_images/no/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduksjon

AI-agenter representerer en spennende utvikling innen generativ AI, som gjør det mulig for store språkmodeller (LLMs) å utvikle seg fra assistenter til agenter som kan utføre handlinger. AI-agent-rammeverk gjør det mulig for utviklere å lage applikasjoner som gir LLMs tilgang til verktøy og tilstandsbehandling. Disse rammeverkene forbedrer også synlighet, slik at brukere og utviklere kan overvåke handlingene LLMene planlegger, og dermed forbedre opplevelsesstyringen.

Leksjonen vil dekke følgende områder:

- Forstå hva en AI-agent er - Hva er egentlig en AI-agent?
- Utforske fem ulike AI-agent-rammeverk - Hva gjør dem unike?
- Bruke disse AI-agentene på forskjellige bruksområder - Når bør vi bruke AI-agenter?

## Læringsmål

Etter å ha tatt denne leksjonen vil du kunne:

- Forklare hva AI-agenter er og hvordan de kan brukes.
- Ha en forståelse av forskjellene mellom noen av de populære AI-agent-rammeverkene, og hvordan de skiller seg.
- Forstå hvordan AI-agenter fungerer for å kunne bygge applikasjoner med dem.

## Hva er AI-agenter?

AI-agenter er et svært spennende område innen generativ AI. Med denne begeistringen følger også noe forvirring rundt begreper og deres anvendelse. For å holde det enkelt og inkluderende for de fleste verktøy som refererer til AI-agenter, vil vi bruke denne definisjonen:

AI-agenter gjør det mulig for store språkmodeller (LLMs) å utføre oppgaver ved å gi dem tilgang til en **tilstand** og **verktøy**.

![Agent Model](../../../translated_images/no/what-agent.21f2893bdfd01e6a.webp)

La oss definere disse begrepene:

**Store språkmodeller** - Dette er modellene som blir referert til gjennom hele kurset, som GPT-5, GPT-4o og Llama 3.3, osv.

**Tilstand** - Dette viser til konteksten LLM-en arbeider i. LLM-en bruker konteksten fra sine tidligere handlinger og den nåværende konteksten, noe som styrer beslutningsprosessen for påfølgende handlinger. AI-agent-rammeverk gjør det enklere for utviklere å opprettholde denne konteksten.

**Verktøy** - For å fullføre oppgaven brukeren har bedt om og som LLM-en har planlagt, trenger LLM-en tilgang til verktøy. Noen eksempler på verktøy kan være en database, en API, en ekstern applikasjon eller til og med en annen LLM!

Disse definisjonene vil forhåpentligvis gi deg et godt grunnlag fremover når vi ser på hvordan de blir implementert. La oss utforske noen forskjellige AI-agent-rammeverk:

## LangChain-agenter

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) er en implementasjon av definisjonene vi ga ovenfor.

For å håndtere **tilstand** bruker den en innebygd funksjon kalt `AgentExecutor`. Denne tar imot den definerte `agent` og de `verktøyene` som er tilgjengelige for den.

`AgentExecutor` lagrer også chathistorikken for å gi konteksten for samtalen.

![Langchain Agents](../../../translated_images/no/langchain-agents.edcc55b5d5c43716.webp)

LangChain tilbyr en [verktøykatalog](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) som kan importeres til applikasjonen din og som LLM kan få tilgang til. Disse er laget av fellesskapet og LangChain-teamet.

Du kan så definere disse verktøyene og sende dem til `AgentExecutor`.

Synlighet er et annet viktig aspekt når man snakker om AI-agenter. Det er viktig for applikasjonsutviklere å forstå hvilket verktøy LLM-en bruker og hvorfor. For dette har teamet hos LangChain utviklet LangSmith.

## AutoGen

Det neste AI-agent-rammeverket vi skal diskutere er [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hovedfokuset til AutoGen er samtaler. Agenter er både **samtalevennlige** og **tilpassbare**.

**Samtalevennlig -** LLM-er kan starte og fortsette en samtale med en annen LLM for å fullføre en oppgave. Dette gjøres ved å lage `AssistantAgents` og gi dem en spesifikk systemmelding.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Tilpassbar** - Agenter kan defineres ikke bare som LLM-er, men også som en bruker eller et verktøy. Som utvikler kan du definere en `UserProxyAgent` som har ansvar for å samhandle med brukeren for tilbakemelding i fullføringen av en oppgave. Denne tilbakemeldingen kan enten fortsette utførelsen av oppgaven eller stoppe den.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tilstand og verktøy

For å endre og håndtere tilstand genererer en assistentagent Python-kode for å fullføre oppgaven.

Her er et eksempel på prosessen:

![AutoGen](../../../translated_images/no/autogen.dee9a25a45fde584.webp)

#### LLM definert med en systemmelding

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Denne systemmeldingen styrer denne spesifikke LLM-en til hvilke funksjoner som er relevante for oppgaven. Husk at med AutoGen kan du ha flere definerte AssistantAgents med forskjellige systemmeldinger.

#### Chat startes av bruker

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Denne meldingen fra user_proxy (menneske) er det som starter prosessen hvor agenten utforsker mulige funksjoner som den skal utføre.

#### Funksjon utføres

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Når den innledende chatten er behandlet, vil agenten sende verktøyforslaget for å kalles. I dette tilfellet er det en funksjon kalt `get_weather`. Avhengig av konfigurasjonen din kan denne funksjonen automatisk utføres og leses av agenten, eller den kan utføres basert på brukerinput.

Du kan finne en liste over [AutoGen-kodeeksempler](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) for å utforske videre hvordan du kan komme i gang med å bygge.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) er Microsofts open-source SDK for å bygge AI-agenter og multi-agent-systemer i både **Python** og **.NET**. Det samler styrkene til to tidligere Microsoft-prosjekter — bedriftsfunksjonene i **Semantic Kernel** og multi-agent-orchestreringen i **AutoGen** — i ett enkelt, støttet rammeverk. Dersom du starter et nytt agentprosjekt i dag, er dette den anbefalte etterfølgeren til AutoGen.

Rammeverket skalerer fra en enkelt **chat-agent** til komplekse **multi-agent-arbeidsflyter**, og det integreres direkte med Microsoft Foundry, Azure OpenAI og OpenAI. Det tilbyr også innebygd observasjon gjennom OpenTelemetry slik at du kan spore nøyaktig hva agentene dine gjør.

### Tilstand og verktøy

**Tilstand** - Rammeverket håndterer samtalekontekst for deg gjennom **threads** (tråder). En agent holder styr på meldingshistorikken (brukerforespørsler, verktøykall og resultatene deres), slik at hver runde bygger på de forrige. Tråder kan også vedvare, slik at en samtale kan pauses og gjenopptas senere.

**Verktøy** - Du gir en agent verktøy ved å sende vanlige Python-funksjoner. Typeannoterte parametere blir automatisk omgjort til et skjema, slik at modellen vet hvordan og når den skal kalle dem (funksjonskalling). Rammeverket støtter også Model Context Protocol (MCP)-servere og hostede verktøy som en kodeinterpreter.

Her er et eksempel på en enkelt agent med et tilpasset verktøy:

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

For å koble til Azure OpenAI i Microsoft Foundry i stedet, sender du inn endepunkt og legitimasjon til klienten:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent-arbeidsflyter

Der rammeverket virkelig skiller seg ut, er i samsvar med flere agenter sammen. For eksempel kan du kjøre agenter etter hverandre (hver overfører sin kontekst til den neste) eller spre til flere agenter parallelt og samle inn resultatene deres:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Kjør agenter i rekkefølge, og send samtalekonteksten videre langs kjeden
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Spre til agenter parallelt, og samle deretter inn svarene deres
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

For å installere rammeverket og komme i gang:

```bash
pip install agent-framework-core
# Valgfrie integrasjoner
pip install agent-framework-openai       # OpenAI og Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kan utforske mer i [Microsoft Agent Framework-repositoriet](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) og i [den offisielle dokumentasjonen](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Det neste agent-rammeverket vi skal utforske er [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Det er kjent som en "kode-først"-agent fordi det, i stedet for å jobbe strikt med `strenger`, kan arbeide med DataFrames i Python. Dette blir ekstremt nyttig for dataanalyse og genereringsoppgaver. Det kan være ting som å lage grafer og diagrammer eller generere tilfeldige tall.

### Tilstand og verktøy

For å håndtere samtalens tilstand, bruker TaskWeaver konseptet `Planner`. `Planner` er en LLM som tar forespørselen fra brukerne og kartlegger oppgavene som må fullføres for å oppfylle denne forespørselen.

For å fullføre oppgavene er `Planner` eksponert for samlingen av verktøy kalt `Plugins`. Dette kan være Python-klasser eller en generell kodeinterpreter. Disse plugins lagres som embedder slik at LLM-en bedre kan søke etter riktig plugin.

![Taskweaver](../../../translated_images/no/taskweaver.da8559999267715a.webp)

Her er et eksempel på en plugin for å håndtere anomali-deteksjon:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden blir verifisert før utføring. En annen funksjon for å administrere kontekst i Taskweaver er `experience`. Experience lar en samtalekontekst bli lagret over tid i en YAML-fil. Dette kan konfigureres slik at LLM-en forbedres over tid på visse oppgaver gitt at den eksponeres for tidligere samtaler.

## JARVIS

Det siste agent-rammeverket vi skal utforske er [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Det som gjør JARVIS unikt, er at det bruker en LLM for å administrere `tilstanden` i samtalen, og `verktøyene` er andre AI-modeller. Hver av AI-modellene er spesialiserte modeller som utfører bestemte oppgaver som objektdeteksjon, transkripsjon eller bildeteksting.

![JARVIS](../../../translated_images/no/jarvis.762ddbadbd1a3a33.webp)

LLM-en, som en allsidig modell, mottar forespørselen fra brukeren og identifiserer den spesifikke oppgaven og eventuelle argumenter/data som trengs for å fullføre oppgaven.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM-en formaterer deretter forespørselen på en måte som den spesialiserte AI-modellen kan tolke, som JSON. Når AI-modellen har returnert sin prediksjon basert på oppgaven, mottar LLM-en svaret.

Hvis flere modeller kreves for å fullføre oppgaven, vil den også tolke svarene fra disse modellene før den setter dem sammen til svaret til brukeren.

Eksempelet nedenfor viser hvordan dette vil fungere når en bruker ber om en beskrivelse og telling av objektene i et bilde:

## Oppgave

For å fortsette læringen din om AI-agenter kan du bygge med Microsoft Agent Framework:

- En applikasjon som simulerer et forretningsmøte med forskjellige avdelinger i en utdanningsstartup.
- Lag systemmeldinger som guider LLM-er i å forstå forskjellige personas og prioriteringer, og som gjør det mulig for brukeren å presentere en ny produktidé.
- LLM-en skal deretter generere oppfølgingsspørsmål fra hver avdeling for å forbedre og videreutvikle presentasjonen og produktideen.

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen kan du sjekke ut vår [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å styrke din kunnskap om generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->