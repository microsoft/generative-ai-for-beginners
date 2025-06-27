<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-06-26T00:19:27+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "da"
}
-->
[![Open Source Models](../../../translated_images/17-lesson-banner.a5b918fb0920e4e6d8d391a100f5cb1d5929f4c2752c937d40392905dec82592.da.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Introduktion

AI-agenter repræsenterer en spændende udvikling inden for Generativ AI, der gør det muligt for store sprogmodeller (LLMs) at udvikle sig fra assistenter til agenter, der kan udføre handlinger. AI-agentrammer gør det muligt for udviklere at skabe applikationer, der giver LLMs adgang til værktøjer og tilstandsstyring. Disse rammer forbedrer også synligheden, så brugere og udviklere kan overvåge de handlinger, som LLMs planlægger, hvilket forbedrer oplevelsesstyringen.

Lektionen vil dække følgende områder:

- Forståelse af, hvad en AI-agent er - Hvad er en AI-agent præcist?
- Udforskning af fire forskellige AI-agentrammer - Hvad gør dem unikke?
- Anvendelse af disse AI-agenter til forskellige brugsscenarier - Hvornår skal vi bruge AI-agenter?

## Læringsmål

Efter at have gennemgået denne lektion vil du kunne:

- Forklare, hvad AI-agenter er, og hvordan de kan bruges.
- Have en forståelse af forskellene mellem nogle af de populære AI-agentrammer, og hvordan de adskiller sig.
- Forstå, hvordan AI-agenter fungerer for at kunne bygge applikationer med dem.

## Hvad er AI-agenter?

AI-agenter er et meget spændende felt inden for Generativ AI. Med denne spænding følger nogle gange en forvirring af termer og deres anvendelse. For at holde tingene enkle og inkluderende for de fleste af de værktøjer, der refererer til AI-agenter, vil vi bruge denne definition:

AI-agenter giver store sprogmodeller (LLMs) mulighed for at udføre opgaver ved at give dem adgang til en **tilstand** og **værktøjer**.

![Agent Model](../../../translated_images/what-agent.21f2893bdfd01e6a7fd09b0416c2b15594d97f44bbb2ab5a1ff8bf643d2fcb3d.da.png)

Lad os definere disse termer:

**Store sprogmodeller** - Dette er de modeller, der omtales gennem hele dette kursus, såsom GPT-3.5, GPT-4, Llama-2 osv.

**Tilstand** - Dette refererer til den kontekst, som LLM arbejder i. LLM bruger konteksten af sine tidligere handlinger og den aktuelle kontekst til at guide sin beslutningstagning for efterfølgende handlinger. AI-agentrammer gør det lettere for udviklere at opretholde denne kontekst.

**Værktøjer** - For at fuldføre den opgave, som brugeren har anmodet om, og som LLM har planlagt, har LLM brug for adgang til værktøjer. Nogle eksempler på værktøjer kan være en database, en API, en ekstern applikation eller endda en anden LLM!

Disse definitioner vil forhåbentlig give dig et godt grundlag, når vi ser på, hvordan de implementeres. Lad os udforske et par forskellige AI-agentrammer:

## LangChain-agenter

[LangChain-agenter](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) er en implementering af de definitioner, vi gav ovenfor.

For at administrere **tilstanden** bruger den en indbygget funktion kaldet `AgentExecutor`. Denne accepterer den definerede `agent` og de `tools`, der er tilgængelige for den.

`Agent Executor` gemmer også chat-historikken for at give konteksten af chatten.

![Langchain Agents](../../../translated_images/langchain-agents.edcc55b5d5c437169a2037211284154561183c58bcec6d4ac2f8a79046fac9af.da.png)

LangChain tilbyder et [katalog af værktøjer](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), der kan importeres i din applikation, hvor LLM kan få adgang til dem. Disse er lavet af fællesskabet og af LangChain-teamet.

Du kan derefter definere disse værktøjer og videregive dem til `Agent Executor`.

Synlighed er en anden vigtig aspekt, når man taler om AI-agenter. Det er vigtigt for applikationsudviklere at forstå, hvilket værktøj LLM bruger og hvorfor. For det har teamet hos LangChain udviklet LangSmith.

## AutoGen

Den næste AI-agentramme, vi vil diskutere, er [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hovedfokus for AutoGen er samtaler. Agenter er både **samtaleorienterede** og **tilpasselige**.

**Samtaleorienterede -** LLMs kan starte og fortsætte en samtale med en anden LLM for at fuldføre en opgave. Dette gøres ved at oprette `AssistantAgents` og give dem en specifik systemmeddelelse.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Tilpasselige** - Agenter kan defineres ikke kun som LLMs, men også som en bruger eller et værktøj. Som udvikler kan du definere en `UserProxyAgent`, der er ansvarlig for at interagere med brugeren for feedback i forbindelse med fuldførelsen af en opgave. Denne feedback kan enten fortsætte udførelsen af opgaven eller stoppe den.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tilstand og værktøjer

For at ændre og administrere tilstanden genererer en assistentagent Python-kode for at fuldføre opgaven.

Her er et eksempel på processen:

![AutoGen](../../../translated_images/autogen.dee9a25a45fde584fedd84b812a6e31de5a6464687cdb66bb4f2cb7521391856.da.png)

#### LLM defineret med en systemmeddelelse

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Denne systemmeddelelse styrer denne specifikke LLM til, hvilke funktioner der er relevante for dens opgave. Husk, med AutoGen kan du have flere definerede AssistantAgents med forskellige systemmeddelelser.

#### Chat initieres af bruger

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Denne meddelelse fra user_proxy (Menneske) er det, der vil starte processen for agenten til at udforske de mulige funktioner, som den skal udføre.

#### Funktion udføres

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Når den indledende chat er behandlet, vil agenten sende det foreslåede værktøj til at kalde. I dette tilfælde er det en funktion kaldet `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Dette kan være Python-klasser eller en generel kodefortolker. Disse plugins gemmes som embeddings, så LLM kan bedre søge efter det korrekte plugin.

![Taskweaver](../../../translated_images/taskweaver.da8559999267715a95b7677cf9b7d7dd8420aee6f3c484ced1833f081988dcd5.da.png)

Her er et eksempel på et plugin til at håndtere anomali-detektion:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden verificeres, før den udføres. En anden funktion til at administrere kontekst i Taskweaver er `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` af samtalen og `tools` er andre AI-modeller. Hver af AI-modellerne er specialiserede modeller, der udfører visse opgaver såsom objektgenkendelse, transskription eller billedbeskrivelse.

![JARVIS](../../../translated_images/jarvis.762ddbadbd1a3a3364d4ca3db1a7a9c0d2180060c0f8da6f7bd5b5ea2a115aa7.da.png)

LLM, der er en generel formålsmodel, modtager forespørgslen fra brugeren og identificerer den specifikke opgave og eventuelle argumenter/data, der er nødvendige for at fuldføre opgaven.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM formaterer derefter forespørgslen på en måde, som den specialiserede AI-model kan fortolke, såsom JSON. Når AI-modellen har returneret sin forudsigelse baseret på opgaven, modtager LLM svaret.

Hvis flere modeller er nødvendige for at fuldføre opgaven, vil den også fortolke svaret fra disse modeller, før de bringes sammen for at generere svaret til brugeren.

Eksemplet nedenfor viser, hvordan dette ville fungere, når en bruger anmoder om en beskrivelse og antal af objekterne i et billede:

## Opgave

For at fortsætte din læring om AI-agenter kan du bygge med AutoGen:

- En applikation, der simulerer et forretningsmøde med forskellige afdelinger i en uddannelsesstartup.
- Opret systemmeddelelser, der guider LLMs i at forstå forskellige personligheder og prioriteter, og gør det muligt for brugeren at præsentere en ny produktidé.
- LLM skal derefter generere opfølgende spørgsmål fra hver afdeling for at forfine og forbedre præsentationen og produktidéen.

## Læringen stopper ikke her, fortsæt rejsen

Efter at have gennemført denne lektion, tjek vores [Generativ AI Læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.