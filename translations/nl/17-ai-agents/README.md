[![Open Source Models](../../../translated_images/nl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introductie

AI Agents vertegenwoordigen een spannende ontwikkeling in Generatieve AI, waarmee Grote Taalmodellen (LLM's) zich kunnen ontwikkelen van assistenten tot agenten die in staat zijn acties te ondernemen. AI Agent-frameworks stellen ontwikkelaars in staat om applicaties te creëren die LLM's toegang geven tot tools en statusbeheer. Deze frameworks verbeteren ook de zichtbaarheid, waardoor gebruikers en ontwikkelaars de acties die door LLM's gepland worden kunnen volgen en zo de ervaringsmanagement verbeteren.

De les behandelt de volgende gebieden:

- Begrijpen wat een AI Agent is - Wat is precies een AI Agent?
- Verkennen van vijf verschillende AI Agent Frameworks - Wat maakt ze uniek?
- Toepassen van deze AI Agents op verschillende gebruikssituaties - Wanneer moeten we AI Agents gebruiken?

## Leerdoelen

Na deze les kun je:

- Uitleggen wat AI Agents zijn en hoe ze gebruikt kunnen worden.
- Inzicht hebben in de verschillen tussen enkele populaire AI Agent Frameworks, en hoe ze verschillen.
- Begrijpen hoe AI Agents functioneren om applicaties met hen te bouwen.

## Wat Zijn AI Agents?

AI Agents zijn een heel spannend vakgebied in de wereld van Generatieve AI. Met deze opwinding gaat soms ook verwarring over termen en hun toepassing gepaard. Om het eenvoudig te houden en de meeste tools die naar AI Agents verwijzen te omvatten, gebruiken we de volgende definitie:

AI Agents stellen Grote Taalmodellen (LLM's) in staat taken uit te voeren door ze toegang te geven tot een **status** en **tools**.

![Agent Model](../../../translated_images/nl/what-agent.21f2893bdfd01e6a.webp)

Laten we deze termen definiëren:

**Grote Taalmodellen** - Dit zijn de modellen die in deze cursus worden genoemd zoals GPT-3.5, GPT-4, Llama-2, enzovoort.

**Status** - Dit verwijst naar de context waarin de LLM werkt. De LLM gebruikt de context van zijn eerdere acties en de huidige context, die de besluitvorming voor volgende acties stuurt. AI Agent Frameworks maken het voor ontwikkelaars gemakkelijker om deze context te behouden.

**Tools** - Om de taak te voltooien die de gebruiker heeft gevraagd en die de LLM heeft gepland, heeft de LLM toegang nodig tot tools. Enkele voorbeelden van tools kunnen een database, een API, een externe applicatie of zelfs een andere LLM zijn!

Deze definities geven hopelijk een goede basis om verder te gaan terwijl we kijken hoe ze worden geïmplementeerd. Laten we een paar verschillende AI Agent-frameworks verkennen:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) is een implementatie van de hierboven gegeven definities.

Om de **status** te beheren, gebruikt het een ingebouwde functie genaamd `AgentExecutor`. Deze accepteert de gedefinieerde `agent` en de `tools` die beschikbaar zijn.

De `Agent Executor` slaat ook de chatgeschiedenis op om de context van de chat te bieden.

![Langchain Agents](../../../translated_images/nl/langchain-agents.edcc55b5d5c43716.webp)

LangChain biedt een [catalogus van tools](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) die kunnen worden geïmporteerd in je applicatie waar de LLM toegang toe kan krijgen. Deze worden gemaakt door de community en door het LangChain-team.

Je kunt vervolgens deze tools definiëren en doorgeven aan de `Agent Executor`.

Zichtbaarheid is een ander belangrijk aspect bij het praten over AI Agents. Het is belangrijk voor applicatieontwikkelaars om te begrijpen welke tool de LLM gebruikt en waarom. Hiervoor heeft het team van LangChain LangSmith ontwikkeld.

## AutoGen

Het volgende AI Agent-framework dat we bespreken is [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). De hoofdfocus van AutoGen is conversaties. Agenten zijn zowel **conversatiegericht** als **aanpasbaar**.

**Conversatiegericht -** LLM's kunnen een gesprek beginnen en voortzetten met een andere LLM om een taak te voltooien. Dit wordt gedaan door `AssistantAgents` te creëren en een specifiek systeembericht te geven.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Aanpasbaar** - Agenten kunnen niet alleen worden gedefinieerd als LLM's maar ook als een gebruiker of een tool. Als ontwikkelaar kun je een `UserProxyAgent` definiëren die verantwoordelijk is voor de interactie met de gebruiker voor feedback bij het voltooien van een taak. Deze feedback kan de uitvoering van de taak voortzetten of stoppen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Status en Tools

Om status te wijzigen en te beheren genereert een assistent Agent Python-code om de taak te voltooien.

Hier is een voorbeeld van het proces:

![AutoGen](../../../translated_images/nl/autogen.dee9a25a45fde584.webp)

#### LLM Gedefinieerd met een Systeembericht

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Dit systeembericht leidt deze specifieke LLM naar welke functies relevant zijn voor zijn taak. Onthoud dat je met AutoGen meerdere gedefinieerde AssistantAgents met verschillende systeemberichten kunt hebben.

#### Chat wordt geïnitieerd door gebruiker

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Dit bericht van de user_proxy (mens) is wat het proces van de Agent start om de mogelijke functies te verkennen die het zou moeten uitvoeren.

#### Functie wordt uitgevoerd

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Zodra de initiële chat is verwerkt, zal de Agent de voorgestelde tool sturen om op te roepen. In dit geval is dat een functie genaamd `get_weather`. Afhankelijk van je configuratie kan deze functie automatisch uitgevoerd en gelezen worden door de Agent of kan hij worden uitgevoerd op basis van gebruikersinput.

Je kunt een lijst vinden van [AutoGen codevoorbeelden](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) om verder te verkennen hoe je kunt beginnen met bouwen.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) is Microsoft's open-source SDK voor het bouwen van AI Agents en multi-agent systemen in zowel **Python** als **.NET**. Het brengt de krachten van twee eerdere Microsoft-projecten samen — de enterprise functies van **Semantic Kernel** en de multi-agent orkestratie van **AutoGen** — in één enkel, ondersteund framework. Als je vandaag een nieuw agent project start, is dit de aanbevolen opvolger van AutoGen.

Het framework schaalt van een enkele **chatagent** tot complexe **multi-agent workflows**, en integreert direct met Microsoft Foundry, Azure OpenAI en OpenAI. Het biedt ook ingebouwde observatie via OpenTelemetry zodat je precies kunt volgen wat je agents doen.

### Status en Tools

**Status** - Het framework beheert de context van het gesprek voor je via **threads**. Een agent houdt de berichtgeschiedenis bij (gebruikersverzoeken, tool-aanroepen en de resultaten daarvan), zodat elke beurt voortbouwt op de vorige. Threads kunnen ook worden opgeslagen, waardoor een gesprek gepauzeerd en later hervat kan worden.

**Tools** - Je geeft een agent tools door gewone Python-functies door te geven. Type-geannoteerde parameters worden automatisch omgezet in een schema, zodat het model weet hoe en wanneer het ze moet aanroepen (functie-aanroep). Het framework ondersteunt ook Model Context Protocol (MCP) servers en gehoste tools zoals een code-interpreter.

Hier is een voorbeeld van een enkele agent met een aangepaste tool:

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

Om in plaats daarvan verbinding te maken met Azure OpenAI in Microsoft Foundry, geef je je endpoint en referenties door aan de client:

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

Waar het framework echt uitblinkt is bij het orkestreren van meerdere agents samen. Zo kun je agents na elkaar laten draaien (elke agent geeft zijn context door aan de volgende) of parallel meerdere agents laten draaien en hun resultaten samenvoegen:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Voer agenten achtereenvolgens uit, waarbij de gesprekscontext langs de keten wordt doorgegeven
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Verdeel naar agenten parallel, en verzamel vervolgens hun reacties
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Om het framework te installeren en aan de slag te gaan:

```bash
pip install agent-framework-core
# Optionele integraties
pip install agent-framework-openai       # OpenAI en Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Je kunt meer ontdekken in de [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) en de [officiële documentatie](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Het volgende agent-framework dat we gaan verkennen is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Het staat bekend als een "code-first" agent omdat het in plaats van strikt met `strings` te werken, ook met DataFrames in Python kan werken. Dit wordt extreem nuttig voor data-analyse en generatietaken. Dit kunnen dingen zijn zoals het maken van grafieken en diagrammen of het genereren van willekeurige getallen.

### Status en Tools

Om de status van het gesprek te beheren gebruikt TaskWeaver het concept van een `Planner`. De `Planner` is een LLM die het verzoek van de gebruikers neemt en de taken uitzet die voltooid moeten worden om dit verzoek te vervullen.

Om de taken te voltooien heeft de `Planner` toegang tot een verzameling tools genaamd `Plugins`. Dit kunnen Python klassen zijn of een algemene code-interpreter. Deze plugins worden opgeslagen als embeddings zodat de LLM beter kan zoeken naar de juiste plugin.

![Taskweaver](../../../translated_images/nl/taskweaver.da8559999267715a.webp)

Hier is een voorbeeld van een plugin om anomaliedetectie te verwerken:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

De code wordt geverifieerd voordat deze wordt uitgevoerd. Een andere functie om context te beheren in Taskweaver is `experience`. Experience maakt het mogelijk om de context van een gesprek langdurig op te slaan in een YAML-bestand. Dit kan zo worden ingesteld dat de LLM na verloop van tijd verbetert op bepaalde taken als het wordt blootgesteld aan eerdere gesprekken.

## JARVIS

Het laatste agent-framework dat we gaan verkennen is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Wat JARVIS uniek maakt, is dat het een LLM gebruikt om de `status` van het gesprek te beheren en de `tools` andere AI-modellen zijn. Elk van de AI-modellen zijn gespecialiseerde modellen die bepaalde taken uitvoeren, zoals objectdetectie, transcriptie of beeldbijschriften.

![JARVIS](../../../translated_images/nl/jarvis.762ddbadbd1a3a33.webp)

De LLM, als een algemeen model, ontvangt het verzoek van de gebruiker en identificeert de specifieke taak en eventuele argumenten/gegevens die nodig zijn om de taak te voltooien.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

De LLM formatteert vervolgens het verzoek op een manier die het gespecialiseerde AI-model kan interpreteren, zoals JSON. Zodra het AI-model zijn voorspelling heeft teruggegeven op basis van de taak, ontvangt de LLM het antwoord.

Als meerdere modellen nodig zijn om de taak te voltooien, zal het ook de antwoorden van die modellen interpreteren voordat het ze samenbrengt om het antwoord aan de gebruiker te genereren.

Het onderstaande voorbeeld laat zien hoe dit zou werken wanneer een gebruiker een beschrijving en telling van de objecten in een afbeelding vraagt:

## Opdracht

Om je leerproces van AI Agents voort te zetten, kun je bouwen met Microsoft Agent Framework:

- Een applicatie die een zakelijke vergadering simuleert met verschillende afdelingen van een educatieve startup.
- Maak systeemberichten die LLM's begeleiden in het begrijpen van verschillende persona's en prioriteiten, en waarmee de gebruiker een nieuw productidee kan pitchen.
- De LLM moet dan vervolgvraagstukken genereren van elke afdeling om de pitch en het productidee te verfijnen en te verbeteren.

## Het leren stopt hier niet, ga door met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te vergroten!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->