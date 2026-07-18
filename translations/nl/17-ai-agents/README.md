[![Open Source Models](../../../translated_images/nl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introductie

AI Agents vertegenwoordigen een opwindende ontwikkeling in Generatieve AI, waarbij Grote Taalmodellen (LLM's) kunnen evolueren van assistenten naar agenten die tot actie in staat zijn. AI Agent-frameworks stellen ontwikkelaars in staat om applicaties te creëren die LLM's toegang geven tot tools en state management. Deze frameworks verbeteren ook de zichtbaarheid, waardoor gebruikers en ontwikkelaars de geplande acties van LLM's kunnen volgen, wat de ervaring verbetert.

De les zal de volgende gebieden behandelen:

- Begrijpen wat een AI Agent is - Wat is precies een AI Agent?
- Vijf verschillende AI Agent-frameworks verkennen - Wat maakt ze uniek?
- Deze AI Agents toepassen op verschillende use cases - Wanneer moeten we AI Agents gebruiken?

## Leerdoelen

Na het volgen van deze les zul je in staat zijn om:

- Uitleggen wat AI Agents zijn en hoe ze gebruikt kunnen worden.
- Inzicht hebben in de verschillen tussen enkele populaire AI Agent-frameworks en hoe ze verschillen.
- Begrijpen hoe AI Agents functioneren om er toepassingen mee te bouwen.

## Wat zijn AI Agents?

AI Agents zijn een zeer spannend gebied binnen de wereld van Generatieve AI. Met deze opwinding komt soms ook verwarring over termen en toepassing. Om het simpel te houden en de meeste tools die naar AI Agents verwijzen te omvatten, gebruiken we deze definitie:

AI Agents stellen Grote Taalmodellen (LLM's) in staat om taken uit te voeren door hen toegang te geven tot een **state** en **tools**.

![Agent Model](../../../translated_images/nl/what-agent.21f2893bdfd01e6a.webp)

Laten we deze termen definiëren:

**Grote Taalmodellen** - Dit zijn de modellen waar in deze cursus naar wordt verwezen zoals GPT-5, GPT-4o, en Llama 3.3, etc.

**State** - Dit verwijst naar de context waarin de LLM werkt. De LLM gebruikt de context van zijn eerdere acties en de huidige context om zijn besluitvorming voor volgende acties te sturen. AI Agent-frameworks maken het voor ontwikkelaars gemakkelijker om deze context te behouden.

**Tools** - Om de taak die de gebruiker heeft gevraagd en die de LLM heeft gepland te voltooien, heeft de LLM toegang nodig tot tools. Voorbeelden van tools kunnen een database, een API, een externe applicatie of zelfs een andere LLM zijn!

Deze definities zullen je hopelijk een goede basis geven terwijl we bekijken hoe ze worden geïmplementeerd. Laten we een paar verschillende AI Agent-frameworks verkennen:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) is een implementatie van de definities die we hierboven gaven.

Om de **state** te beheren, gebruikt het een ingebouwde functie genaamd `AgentExecutor`. Deze accepteert de gedefinieerde `agent` en de beschikbare `tools`.

De `AgentExecutor` slaat ook de chatgeschiedenis op om de context van de chat te bieden.

![Langchain Agents](../../../translated_images/nl/langchain-agents.edcc55b5d5c43716.webp)

LangChain biedt een [catalogus van tools](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) die geïmporteerd kunnen worden in je applicatie waartoe de LLM toegang kan krijgen. Deze zijn gemaakt door de community en door het LangChain-team.

Je kunt deze tools vervolgens definiëren en doorgeven aan de `AgentExecutor`.

Zichtbaarheid is een ander belangrijk aspect bij het praten over AI Agents. Het is belangrijk voor applicatie-ontwikkelaars om te begrijpen welke tool de LLM gebruikt en waarom. Hiervoor heeft het team van LangChain LangSmith ontwikkeld.

## AutoGen

Het volgende AI Agent-framework dat we bespreken is [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). De belangrijkste focus van AutoGen ligt op conversaties. Agents zijn zowel **conversabel** als **aanpasbaar**.

**Conversabel -** LLM's kunnen een gesprek starten en voortzetten met een andere LLM om een taak te voltooien. Dit wordt gedaan door `AssistantAgents` te maken en ze een specifieke systeemboodschap te geven.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Aanpasbaar** - Agents kunnen niet alleen als LLM's worden gedefinieerd, maar ook als gebruiker of tool. Als ontwikkelaar kun je een `UserProxyAgent` definiëren die verantwoordelijk is voor de interactie met de gebruiker voor feedback bij het voltooien van een taak. Deze feedback kan de uitvoering van de taak voortzetten of stoppen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### State en Tools

Om de state te veranderen en beheren genereert een Assistant Agent Python-code om de taak te voltooien.

Hier is een voorbeeld van het proces:

![AutoGen](../../../translated_images/nl/autogen.dee9a25a45fde584.webp)

#### LLM Gedefinieerd met een Systeemboodschap

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Deze systeemboodschap geeft aan welke functies relevant zijn voor de taak van deze specifieke LLM. Onthoud dat je met AutoGen meerdere gedefinieerde AssistantAgents kunt hebben met verschillende systeemboodschappen.

#### Chat wordt gestart door Gebruiker

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Dit bericht van de user_proxy (Mens) is wat het proces van de Agent zal starten om de mogelijke functies die hij moet uitvoeren te onderzoeken.

#### Functie wordt uitgevoerd

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Zodra de initiële chat is verwerkt, zal de Agent de voorgestelde tool aanroepen. In dit geval is het een functie genaamd `get_weather`. Afhankelijk van jouw configuratie kan deze functie automatisch worden uitgevoerd en door de Agent worden uitgelezen, of kunnen ze worden uitgevoerd op basis van gebruikersinvoer.

Je kunt een lijst met [AutoGen codevoorbeelden](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) vinden om verder te verkennen hoe je kunt beginnen met bouwen.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) is Microsoft's open-source SDK voor het bouwen van AI Agents en multi-agent systemen in zowel **Python** als **.NET**. Het brengt de kracht van twee eerdere Microsoft-projecten samen — de enterprise features van **Semantic Kernel** en de multi-agent orkestratie van **AutoGen** — in één enkel, ondersteund framework. Als je vandaag een nieuw agent-project start, is dit de aanbevolen opvolger van AutoGen.

Het framework schaalt van een enkele **chat agent** tot complexe **multi-agent workflows**, en integreert direct met Microsoft Foundry, Azure OpenAI en OpenAI. Het biedt ook ingebouwde observability via OpenTelemetry zodat je precies kunt volgen wat je agenten doen.

### State en Tools

**State** - Het framework beheert de gesprekcontext voor jou via **threads**. Een agent houdt de berichtgeschiedenis bij (gebruikersverzoeken, toolaanroepen en hun resultaten), zodat elke beurt voortbouwt op de vorige. Threads kunnen ook worden opgeslagen, waardoor een gesprek gepauzeerd en later hervat kan worden.

**Tools** - Je geeft een agent tools door gewone Python-functies door te geven. Type-geannoteerde parameters worden automatisch omgezet in een schema, zodat het model weet hoe en wanneer het ze moet aanroepen (function calling). Het framework ondersteunt ook Model Context Protocol (MCP) servers en gehoste tools zoals een code-interpreter.

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

Om in plaats daarvan verbinding te maken met Azure OpenAI in Microsoft Foundry, geef je je endpoint en credentials door aan de client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agent workflows

Waar het framework echt uitblinkt, is het orkestreren van meerdere agenten samen. Bijvoorbeeld, je kunt agenten na elkaar laten draaien (ieder geeft zijn context door aan de volgende) of parallel meerdere agenten aanroepen en hun resultaten samenvoegen:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Voer agenten achtereenvolgens uit en geef de gesprekscontext door in de keten
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Spreid uit naar agenten parallel en verzamel daarna hun reacties bijeen
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

Het volgende agent-framework dat we gaan verkennen is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Het staat bekend als een "code-first" agent omdat het in plaats van strikt met `strings` te werken, ook kan werken met DataFrames in Python. Dit wordt extreem nuttig voor data-analyse en generatietaken. Dit kan onder meer het maken van grafieken en diagrammen of het genereren van willekeurige getallen zijn.

### State en Tools

Om de state van het gesprek te beheren gebruikt TaskWeaver het concept van een `Planner`. De `Planner` is een LLM die het verzoek van de gebruikers neemt en de taken in kaart brengt die voltooid moeten worden om aan het verzoek te voldoen.

Om de taken te voltooien wordt de `Planner` blootgesteld aan een verzameling tools genaamd `Plugins`. Dit kunnen Python-klassen zijn of een algemene code-interpreter. Deze plugins worden opgeslagen als embeddings zodat de LLM beter kan zoeken naar de juiste plugin.

![Taskweaver](../../../translated_images/nl/taskweaver.da8559999267715a.webp)

Hier is een voorbeeld van een plugin voor anomaliedetectie:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

De code wordt gecontroleerd voor uitvoering. Een andere functie om context te beheren in Taskweaver is `experience`. Experience maakt het mogelijk om de context van een gesprek op de lange termijn op te slaan in een YAML-bestand. Dit kan zo worden geconfigureerd dat de LLM verbetert in bepaalde taken naarmate het wordt blootgesteld aan eerdere gesprekken.

## JARVIS

Het laatste agent-framework dat we verkennen is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Wat JARVIS uniek maakt, is dat het een LLM gebruikt om de `state` van het gesprek te beheren en de `tools` andere AI-modellen zijn. Elk van de AI-modellen zijn gespecialiseerde modellen die bepaalde taken uitvoeren zoals objectdetectie, transcriptie of afbeeldingsonderschriften maken.

![JARVIS](../../../translated_images/nl/jarvis.762ddbadbd1a3a33.webp)

De LLM, als een algemeen doeleinde model, ontvangt het verzoek van de gebruiker en identificeert de specifieke taak en eventuele argumenten/gegevens die nodig zijn om de taak te voltooien.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

De LLM formatteert dan het verzoek op een manier dat het gespecialiseerde AI-model kan interpreteren, zoals JSON. Zodra het AI-model zijn voorspelling heeft teruggestuurd gebaseerd op de taak, ontvangt de LLM de respons.

Als meerdere modellen nodig zijn om de taak te voltooien, zal het ook de respons van die modellen interpreteren voordat ze worden samengevoegd om de respons aan de gebruiker te genereren.

Het onderstaande voorbeeld laat zien hoe dit werkt wanneer een gebruiker een beschrijving en telling van de objecten op een afbeelding vraagt:

## Opdracht

Om je leerproces over AI Agents voort te zetten kun je bouwen met Microsoft Agent Framework:

- Een applicatie die een zakelijke vergadering simuleert met verschillende afdelingen van een onderwijsstartup.
- Maak systeemboodschappen die LLM's begeleiden bij het begrijpen van verschillende persona's en prioriteiten, en stelt de gebruiker in staat een nieuw productidee te presenteren.
- De LLM moet vervolgens vervolgvragen genereren van elke afdeling om de pitch en het productidee te verfijnen en te verbeteren.

## Leren stopt hier niet, zet de Reis voort

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te vergroten!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->