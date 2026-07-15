[![Open Source Models](../../../translated_images/sv/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduktion

AI-agenter representerar en spännande utveckling inom Generativ AI och möjliggör för stora språkmodeller (LLMs) att utvecklas från assistenter till agenter som kan utföra handlingar. AI-agentramverk gör det möjligt för utvecklare att skapa applikationer som ger LLM tillgång till verktyg och tillståndshantering. Dessa ramverk förbättrar också synligheten, vilket gör att användare och utvecklare kan övervaka handlingarna som LLM planerar och därigenom förbättra upplevelsehanteringen.

Lektionen kommer att täcka följande områden:

- Att förstå vad en AI-agent är - Vad är en AI-agent egentligen?
- Utforska fem olika AI-agentramverk - Vad gör dem unika?
- Tillämpa dessa AI-agenter i olika användningsfall - När bör vi använda AI-agenter?

## Lärandemål

Efter denna lektion kommer du att kunna:

- Förklara vad AI-agenter är och hur de kan användas.
- Ha en förståelse för skillnaderna mellan några av de populära AI-agentramverken och hur de skiljer sig åt.
- Förstå hur AI-agenter fungerar för att kunna bygga applikationer med dem.

## Vad är AI-agenter?

AI-agenter är ett mycket spännande område inom Generativ AI. Denna spänning medför ibland förvirring kring termer och deras tillämpning. För att hålla det enkelt och inkluderande för de flesta verktygen som refererar till AI-agenter, kommer vi att använda denna definition:

AI-agenter gör det möjligt för stora språkmodeller (LLMs) att utföra uppgifter genom att ge dem tillgång till ett **tillstånd** och **verktyg**.

![Agent Model](../../../translated_images/sv/what-agent.21f2893bdfd01e6a.webp)

Låt oss definiera dessa termer:

**Stora språkmodeller** - Dessa är modellerna som refereras till i hela kursen, såsom GPT-3.5, GPT-4, Llama-2, etc.

**Tillstånd** - Detta refererar till kontexten som LLM arbetar i. LLM använder kontexten från tidigare handlingar och den aktuella kontexten för att styra sitt beslutsfattande för efterföljande handlingar. AI-agentramverk gör det enklare för utvecklare att upprätthålla denna kontext.

**Verktyg** - För att slutföra den uppgift som användaren har begärt och som LLM har planerat behöver LLM tillgång till verktyg. Några exempel på verktyg kan vara en databas, ett API, en extern applikation eller till och med en annan LLM!

Dessa definitioner förhoppningsvis ger dig en bra grund när vi nu tittar på hur de implementeras. Låt oss utforska några olika AI-agentramverk:

## LangChain-agenter

[LangChain-agenter](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) är en implementation av de definitioner vi gav ovan.

För att hantera **tillståndet** använder den en inbyggd funktion som kallas `AgentExecutor`. Den tar emot den definierade `agenten` och de `verktyg` som finns tillgängliga för den.

`Agent Executor` lagrar även chattens historik för att ge kontext till chatten.

![Langchain Agents](../../../translated_images/sv/langchain-agents.edcc55b5d5c43716.webp)

LangChain erbjuder en [katalog med verktyg](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) som kan importeras till din applikation och som LLM kan få tillgång till. Dessa är skapade av communityn och LangChain-teamet.

Du kan sedan definiera dessa verktyg och skicka dem till `Agent Executor`.

Synlighet är en annan viktig aspekt när man talar om AI-agenter. Det är viktigt för applikationsutvecklare att förstå vilket verktyg LLM använder och varför. För detta har teamet på LangChain utvecklat LangSmith.

## AutoGen

Det nästa AI-agentramverket vi ska diskutera är [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGen har fokus på konversationer. Agenter är både **konverserbara** och **anpassningsbara**.

**Konverserbara** - LLM kan starta och fortsätta en konversation med en annan LLM för att slutföra en uppgift. Detta görs genom att skapa `AssistantAgents` och ge dem ett specifikt systemmeddelande.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Anpassningsbara** - Agenter kan definieras inte bara som LLM utan även som en användare eller verktyg. Som utvecklare kan du definiera en `UserProxyAgent` som är ansvarig för att interagera med användaren för feedback i att slutföra en uppgift. Denna feedback kan antingen fortsätta uppgiftens utförande eller stoppa det.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tillstånd och Verktyg

För att ändra och hantera tillstånd genererar en assistentagent Python-kod för att slutföra uppgiften.

Här är ett exempel på processen:

![AutoGen](../../../translated_images/sv/autogen.dee9a25a45fde584.webp)

#### LLM definierad med ett systemmeddelande

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Detta systemmeddelande styr denna specifika LLM till vilka funktioner som är relevanta för dess uppgift. Kom ihåg att med AutoGen kan du ha flera definierade AssistantAgents med olika systemmeddelanden.

#### Chatten initieras av användaren

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Detta meddelande från user_proxy (människa) är det som startar processen för agenten att utforska vilka funktioner som bör utföras.

#### Funktion utförs

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

När den initiala chatten har hanterats kommer agenten att skicka det föreslagna verktyget att anropas. I detta fall är det en funktion som heter `get_weather`. Beroende på din konfiguration kan denna funktion automatiskt exekveras och läsas av agenten eller köras baserat på användarens input.

Du kan hitta en lista med [AutoGen kodexempel](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) för att utforska hur du kommer igång med att bygga.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) är Microsofts open source SDK för att bygga AI-agenter och multi-agent-system i både **Python** och **.NET**. Det samlar styrkorna från två tidigare Microsoft-projekt — företagsfunktionerna i **Semantic Kernel** och multi-agent-organiseringen i **AutoGen** — i ett enda, supporterat ramverk. Om du startar ett nytt agentprojekt idag, är detta den rekommenderade efterföljaren till AutoGen.

Ramverket skalar från en enda **chattagent** ända upp till komplexa **multi-agentflöden**, och det integreras direkt med Microsoft Foundry, Azure OpenAI och OpenAI. Det erbjuder också inbyggd observerbarhet genom OpenTelemetry så att du kan spåra exakt vad dina agenter gör.

### Tillstånd och Verktyg

**Tillstånd** - Ramverket hanterar konversationskontext åt dig genom **trådar**. En agent håller reda på meddelandehistoriken (användarförfrågningar, verktygsanrop och deras resultat), så varje steg bygger vidare på de tidigare. Trådar kan också sparas så att en konversation kan pausas och återupptas senare.

**Verktyg** - Du ger en agent verktyg genom att skicka in vanliga Python-funktioner. Typannoterade parametrar omvandlas automatiskt till ett schema, så modellen vet hur och när de ska anropas (funktionsanrop). Ramverket stödjer även Model Context Protocol (MCP) servrar och hostade verktyg såsom en kodtolk.

Här är ett exempel på en enskild agent med ett anpassat verktyg:

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

För att istället ansluta till Azure OpenAI i Microsoft Foundry, skicka in din endpoint och dina autentiseringsuppgifter till klienten:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agentflöden

Där ramverket verkligen utmärker sig är i att orkestrera flera agenter tillsammans. Till exempel kan du köra agenter efter varandra (var och en skickar vidare sin kontext till nästa) eller parallellt till flera agenter och sedan aggregera deras resultat:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Kör agenter i sekvens, och för vidare konversationskontexten längs kedjan
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sprid ut till agenter parallellt, och samla sedan in deras svar
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

För att installera ramverket och komma igång:

```bash
pip install agent-framework-core
# Valfria integrationer
pip install agent-framework-openai       # OpenAI och Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kan utforska mer i [Microsoft Agent Frameworks repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) och den [officiella dokumentationen](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Nästa agentramverk vi ska utforska är [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Det är känt som ett "code-first" agent eftersom det istället för att arbeta strikt med `strings`, kan arbeta med DataFrames i Python. Detta blir extremt användbart för dataanalys och genereringsuppgifter. Det kan vara saker som att skapa grafer och diagram eller generera slumpmässiga nummer.

### Tillstånd och Verktyg

För att hantera samtalets tillstånd använder TaskWeaver konceptet `Planner`. `Planner` är en LLM som tar användarnas förfrågan och kartlägger de uppgifter som behöver slutföras för att uppfylla denna förfrågan.

För att utföra uppgifterna exponeras `Planner` för en samling verktyg kallade `Plugins`. Dessa kan vara Python-klasser eller en generell kodtolk. Dessa plugins lagras som inbäddningar (embeddings) så att LLM kan bättre söka efter rätt plugin.

![Taskweaver](../../../translated_images/sv/taskweaver.da8559999267715a.webp)

Här är ett exempel på ett plugin för att hantera anomaliupptäckt:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden verifieras innan exekvering. En annan funktion för att hantera kontext i Taskweaver är `experience`. Experience tillåter att kontexten av en konversation lagras långsiktigt i en YAML-fil. Detta kan konfigureras så att LLM förbättras över tid på vissa uppgifter under förutsättning att det exponeras för tidigare konversationer.

## JARVIS

Det sista agentramverket vi ska utforska är [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Det som gör JARVIS unikt är att det använder en LLM för att hantera konversationens `tillstånd` och att `verktygen` är andra AI-modeller. Varje AI-modell är specialiserad för att utföra vissa uppgifter som objektigenkänning, transkription eller bildbeskrivning.

![JARVIS](../../../translated_images/sv/jarvis.762ddbadbd1a3a33.webp)

LLM, som är en allmän modell, tar emot förfrågan från användaren och identifierar den specifika uppgiften och eventuella argument/data som behövs för att slutföra uppgiften.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM formaterar sedan förfrågan på ett sätt som den specialiserade AI-modellen kan tolka, till exempel JSON. När AI-modellen har returnerat sin prediktion baserat på uppgiften, får LLM svaret.

Om flera modeller krävs för att slutföra uppgiften kommer den också att tolka svaren från dessa modeller innan de sammanställs för att generera svaret till användaren.

Exemplet nedan visar hur detta skulle fungera när en användare begär en beskrivning och räkning av objekten i en bild:

## Uppgift

För att fortsätta lära dig om AI-agenter kan du bygga med Microsoft Agent Framework:

- En applikation som simulerar ett affärsmöte med olika avdelningar i en utbildningsstartup.
- Skapa systemmeddelanden som vägleder LLM att förstå olika personligheter och prioriteringar, och möjliggör för användaren att presentera en ny produktidé.
- LLM ska sedan generera följdfrågor från varje avdelning för att förfina och förbättra presentationen och produktidén.

## Lärandet tar inte slut här, fortsätt resan

Efter denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta fördjupa dina kunskaper inom Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->