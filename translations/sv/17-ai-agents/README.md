[![Open Source Models](../../../translated_images/sv/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduktion

AI-agenter representerar en spännande utveckling inom Generativ AI, som möjliggör för stora språkmodeller (LLMs) att utvecklas från assistenter till agenter som kan vidta åtgärder. AI-agentramverk gör det möjligt för utvecklare att skapa applikationer som ger LLMs tillgång till verktyg och tillståndshantering. Dessa ramverk förbättrar också synligheten, vilket gör det möjligt för användare och utvecklare att övervaka de åtgärder som LLMs planerar, och därigenom förbättra hanteringen av användarupplevelsen.

Lektionen kommer att täcka följande områden:

- Förstå vad en AI-agent är - Vad är egentligen en AI-agent?
- Utforska fem olika AI-agentramverk - Vad gör dem unika?
- Tillämpa dessa AI-agenter på olika användningsfall - När ska vi använda AI-agenter?

## Lärandemål

Efter att ha genomgått denna lektion kommer du att kunna:

- Förklara vad AI-agenter är och hur de kan användas.
- Ha en förståelse för skillnaderna mellan några av de populära AI-agentramverken, och hur de skiljer sig åt.
- Förstå hur AI-agenter fungerar för att kunna bygga applikationer med dem.

## Vad är AI-agenter?

AI-agenter är ett mycket spännande område inom Generativ AI. Med denna spänning kommer ibland en förvirring kring termer och deras tillämpning. För att hålla det enkelt och inkluderande för de flesta verktyg som refererar till AI-agenter, kommer vi att använda denna definition:

AI-agenter låter stora språkmodeller (LLMs) utföra uppgifter genom att ge dem tillgång till ett **tillstånd** och **verktyg**.

![Agent Model](../../../translated_images/sv/what-agent.21f2893bdfd01e6a.webp)

Låt oss definiera dessa termer:

**Stora språkmodeller** - Dessa är de modeller som nämnts genom hela denna kurs som GPT-5, GPT-4o och Llama 3.3, osv.

**Tillstånd** - Detta refererar till context som LLM arbetar i. LLM använder kontexten från sina tidigare åtgärder och den aktuella kontexten, som styr dess beslutsfattande för efterföljande åtgärder. AI-agentramverk gör det enklare för utvecklare att upprätthålla denna kontext.

**Verktyg** - För att slutföra uppgiften som användaren har begärt och som LLM har planerat, behöver LLM tillgång till verktyg. Några exempel på verktyg kan vara en databas, ett API, en extern applikation eller till och med en annan LLM!

Dessa definitioner kommer förhoppningsvis att ge dig en bra grund för framtiden när vi tittar på hur de implementeras. Låt oss utforska några olika AI-agentramverk:

## LangChain-agenter

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) är en implementering av de definitioner vi gav ovan.

För att hantera **tillstånd** används en inbyggd funktion som kallas `AgentExecutor`. Den accepterar den definierade `agent` och de `verktyg` som är tillgängliga för den.

`Agent Executor` lagrar också chathistoriken för att tillhandahålla kontext i chatten.

![Langchain Agents](../../../translated_images/sv/langchain-agents.edcc55b5d5c43716.webp)

LangChain erbjuder en [katalog med verktyg](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) som kan importeras till din applikation där LLM kan få tillgång till dem. Dessa är skapade av gemenskapen och LangChain-teamet.

Du kan sedan definiera dessa verktyg och skicka dem till `Agent Executor`.

Synlighet är en annan viktig aspekt när man pratar om AI-agenter. Det är viktigt för applikationsutvecklare att förstå vilket verktyg LLM använder och varför. För detta har teamet på LangChain utvecklat LangSmith.

## AutoGen

Det nästa AI-agentramverk vi kommer att diskutera är [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Huvudfokus för AutoGen är konversationer. Agenter är både **konverserbara** och **anpassningsbara**.

**Konverserbara -** LLMs kan starta och fortsätta en konversation med en annan LLM för att slutföra en uppgift. Detta görs genom att skapa `AssistantAgents` och ge dem ett specifikt systemmeddelande.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Anpassningsbara** - Agenter kan definieras inte bara som LLMs utan också som en användare eller ett verktyg. Som utvecklare kan du definiera en `UserProxyAgent` som är ansvarig för att interagera med användaren för feedback vid slutförande av en uppgift. Denna feedback kan antingen fortsätta utförandet av uppgiften eller stoppa det.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tillstånd och verktyg

För att ändra och hantera tillstånd genererar en assistentagent Python-kod för att slutföra uppgiften.

Här är ett exempel på processen:

![AutoGen](../../../translated_images/sv/autogen.dee9a25a45fde584.webp)

#### LLM definierad med ett systemmeddelande

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Detta systemmeddelande styr denna specifika LLM vilka funktioner som är relevanta för dess uppgift. Kom ihåg, med AutoGen kan du ha flera definierade AssistantAgents med olika systemmeddelanden.

#### Chatten initieras av användaren

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Detta meddelande från user_proxy (människa) är vad som startar processen för agenten att utforska möjliga funktioner som den bör utföra.

#### Funktion utförs

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

När den första chatten har bearbetats kommer agenten att skicka det föreslagna verktyget att anropas. I detta fall är det en funktion som kallas `get_weather`. Beroende på din konfiguration kan denna funktion automatiskt utföras och läsas av agenten eller utföras baserat på användarens input.

Du kan hitta en lista över [AutoGen kodexempel](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) för att utforska hur du kan komma igång med att bygga.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) är Microsofts open source SDK för att bygga AI-agenter och multi-agent system i både **Python** och **.NET**. Det förenar styrkorna från två tidigare Microsoft-projekt – företagsfunktionerna i **Semantic Kernel** och multi-agent orkestrering av **AutoGen** – till ett enda, stödformat ramverk. Om du startar ett nytt agentprojekt idag är detta den rekommenderade efterträdaren till AutoGen.

Ramverket skalar från en enskild **chattagent** hela vägen till komplexa **multi-agentarbetsflöden**, och det integreras direkt med Microsoft Foundry, Azure OpenAI och OpenAI. Det erbjuder också inbyggd observerbarhet via OpenTelemetry så att du kan spåra exakt vad dina agenter gör.

### Tillstånd och verktyg

**Tillstånd** - Ramverket hanterar samtalskontexten åt dig genom **trådar**. En agent håller koll på meddelandehistoriken (användarförfrågningar, verktygsanrop och deras resultat), så varje tur bygger på de tidigare. Trådar kan också sparas, vilket gör det möjligt att pausa och återuppta en konversation senare.

**Verktyg** - Du ger en agent verktyg genom att skicka vanliga Python-funktioner. Typannoterade parametrar omvandlas automatiskt till ett schema, så att modellen vet hur och när den ska anropa dem (funktionsanrop). Ramverket stöder också Model Context Protocol (MCP) servrar och hostade verktyg som en kodtolk.

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

För att istället ansluta till Azure OpenAI i Microsoft Foundry, skicka din endpoint och dina autentiseringsuppgifter till klienten:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-agentarbetsflöden

Där ramverket verkligen utmärker sig är i orkestrering av flera agenter tillsammans. Till exempel kan du köra agenter efter varandra (varje agent skickar sin kontext till nästa) eller fördela till flera agenter parallellt och aggregera deras resultat:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Kör agenter i följd och för samtalskontexten vidare längs kedjan
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sprid ut till agenter parallellt och sammanställ sedan deras svar
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

För att installera ramverket och komma igång:

```bash
pip install agent-framework-core
# Valfria integrationer
pip install agent-framework-openai       # OpenAI och Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kan utforska mer i [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) och i den [officiella dokumentationen](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Nästa agentramverk vi ska utforska är [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Det är känt som ett "code-first" agent eftersom det istället för att arbeta strikt med `strängar` kan arbeta med DataFrames i Python. Detta blir extremt användbart för dataanalys och genereringsuppgifter. Detta kan vara saker som att skapa grafer och diagram eller generera slumptal.

### Tillstånd och verktyg

För att hantera tillståndet i konversationen använder TaskWeaver konceptet `Planner`. `Planner` är en LLM som tar användarens förfrågan och kartlägger de uppgifter som behöver utföras för att uppfylla denna förfrågan.

För att slutföra uppgifterna exponeras `Planner` för en samling verktyg som kallas `Plugins`. Detta kan vara Python-klasser eller en generell kodtolk. Dessa plugins lagras som embeddings så att LLM kan söka bättre efter rätt plugin.

![Taskweaver](../../../translated_images/sv/taskweaver.da8559999267715a.webp)

Här är ett exempel på en plugin för att hantera avvikelsedetektering:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koden verifieras innan den körs. En annan funktion för att hantera kontext i Taskweaver är `experience`. Experience tillåter att kontexten för en konversation sparas över lång tid i en YAML-fil. Detta kan konfigureras så att LLM förbättras över tid i vissa uppgifter eftersom den exponeras för tidigare konversationer.

## JARVIS

Det sista agentramverket vi ska utforska är [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Det som gör JARVIS unikt är att det använder en LLM för att hantera `tillståndet` i konversationen och `verktygen` är andra AI-modeller. Varje AI-modell är specialiserad på att utföra vissa uppgifter som objektdetektering, transkription eller bildbeskrivning.

![JARVIS](../../../translated_images/sv/jarvis.762ddbadbd1a3a33.webp)

LLM:n, som är en allmänt använd modell, tar emot begäran från användaren och identifierar den specifika uppgiften och eventuella argument/data som behövs för att slutföra uppgiften.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM:n formaterar sedan begäran på ett sätt som den specialiserade AI-modellen kan tolka, till exempel JSON. När AI-modellen har återvänt sin prediktion baserad på uppgiften, får LLM svaret.

Om flera modeller krävs för att slutföra uppgiften kommer den också att tolka svaren från dessa modeller innan den sammanställer dem för att generera svaret till användaren.

Exemplet nedan visar hur detta skulle fungera när en användare begär en beskrivning och räkning av objekt i en bild:

## Uppgift

För att fortsätta din lärande om AI-agenter kan du bygga med Microsoft Agent Framework:

- En applikation som simulerar ett affärsmöte med olika avdelningar i en utbildningsstartup.
- Skapa systemmeddelanden som vägledar LLMs att förstå olika personer och prioriteringar, och gör det möjligt för användaren att presentera en ny produktidé.
- LLM bör sedan generera följdfrågor från varje avdelning för att förfina och förbättra pitch och produktidé.

## Lärandet stannar inte här, fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap inom Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->