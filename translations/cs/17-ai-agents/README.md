[![Open Source Models](../../../translated_images/cs/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Úvod

AI agenti představují vzrušující vývoj v generativní umělé inteligenci, který umožňuje velkým jazykovým modelům (LLM) vyvinout se z asistentů na agenty schopné vykonávat akce. Rámce AI agentů umožňují vývojářům vytvářet aplikace, které dávají LLM přístup k nástrojům a správě stavu. Tyto rámce také zlepšují viditelnost, což uživatelům a vývojářům umožňuje sledovat akce plánované LLM, čímž se zlepšuje správa zkušeností.

Tato lekce pokryje následující oblasti:

- Porozumění tomu, co je AI agent - Co přesně je AI agent?
- Prozkoumání pěti různých rámců AI agentů - Čím jsou jedinečné?
- Aplikace těchto AI agentů na různé případy použití - Kdy bychom měli používat AI agenty?

## Cíle učení

Po absolvování této lekce budete schopni:

- Vysvětlit, co jsou AI agenti a jak je lze používat.
- Mít přehled o rozdílech mezi některými oblíbenými rámci AI agentů a jak se liší.
- Chápat, jak AI agenti fungují, abyste s nimi mohli vytvářet aplikace.

## Co jsou AI agenti?

AI agenti jsou velmi vzrušující oblastí ve světě generativní AI. S tímto nadšením ale někdy přichází i zmatení ohledně pojmů a jejich použití. Abychom to zjednodušili a zahrnuli většinu nástrojů, které se vztahují k AI agentům, použijeme tuto definici:

AI agenti umožňují velkým jazykovým modelům (LLM) vykonávat úkoly tím, že jim dávají přístup ke **stavu** a **nástrojům**.

![Agent Model](../../../translated_images/cs/what-agent.21f2893bdfd01e6a.webp)

Pojďme si vysvětlit tyto pojmy:

**Velké jazykové modely** – Jsou to modely zmíněné v tomto kurzu, jako je GPT-3.5, GPT-4, Llama-2 a další.

**Stav** – Toto odkazuje na kontext, ve kterém LLM pracuje. LLM využívá kontext svých minulých akcí a aktuálního kontextu k řízení rozhodování o následujících akcích. Rámce AI agentů umožňují vývojářům snadněji spravovat tento kontext.

**Nástroje** – Aby LLM dokončil úkol, který uživatel požaduje a který LLM naplánoval, potřebuje přístup k nástrojům. Některé příklady nástrojů jsou databáze, API, externí aplikace nebo dokonce jiný LLM!

Tyto definice by vám měly poskytnout dobrý základ, když se podíváme na to, jak jsou implementovány. Prozkoumejme několik různých rámců AI agentů:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) je implementací výše uvedených definic.

Ke správě **stavu** používá vestavěnou funkci nazvanou `AgentExecutor`. Ta přijímá definovaného `agenta` a `nástroje`, které má k dispozici.

`Agent Executor` také ukládá historii chatu, aby poskytl kontext konverzace.

![Langchain Agents](../../../translated_images/cs/langchain-agents.edcc55b5d5c43716.webp)

LangChain nabízí [katalog nástrojů](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), které lze importovat do vaší aplikace a ke kterým může LLM získat přístup. Tyto nástroje vytváří komunita a tým LangChain.

Poté můžete tyto nástroje definovat a předat je `Agent Executoru`.

Viditelnost je dalším důležitým aspektem při mluvení o AI agentech. Je důležité, aby vývojáři aplikací rozuměli, který nástroj LLM používá a proč. K tomu tým LangChain vyvinul LangSmith.

## AutoGen

Dalším rámcem AI agentů, o kterém budeme hovořit, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hlavním zaměřením AutoGen jsou konverzace. Agenti jsou zároveň **konverzační** a **přizpůsobitelní**.

**Konverzační –** LLM může zahájit a pokračovat v konverzaci s jiným LLM, aby dokončil úkol. To se děje vytvořením `AssistantAgents` a přiřazením specifické systémové zprávy.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Přizpůsobitelní** – Agent může být definován nejen jako LLM, ale také jako uživatel nebo nástroj. Jako vývojář můžete definovat `UserProxyAgent`, který je zodpovědný za interakci s uživatelem ohledně zpětné vazby při plnění úkolu. Tato zpětná vazba může buď pokračovat ve vykonávání úkolu, nebo ho zastavit.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stav a nástroje

Ke změně a správě stavu pomocný agent generuje Python kód k dokončení úkolu.

Zde je příklad tohoto procesu:

![AutoGen](../../../translated_images/cs/autogen.dee9a25a45fde584.webp)

#### LLM definovaný systémovou zprávou

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Tato systémová zpráva směruje specifický LLM, které funkce jsou pro jeho úkol relevantní. Pamatujte, že v AutoGen můžete mít více definovaných AssistantAgents s různými systémovými zprávami.

#### Chat je zahájen uživatelem

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tato zpráva od user_proxy (člověk) zahájí proces, kdy Agent prozkoumává možné funkce, které by měl vykonat.

#### Funkce je vykonána

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Jakmile je počáteční chat zpracován, Agent navrhne nástroj k volání. V tomto případě je to funkce `get_weather`. Podle vaší konfigurace může být tato funkce automaticky vykonána a její výsledek načten Agentem, nebo může být provedena na základě vstupu uživatele.

Najdete zde seznam [ukázek kódu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), které vám pomohou dále prozkoumat, jak začít s vývojem.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je open-source SDK od Microsoftu pro tvorbu AI agentů a multiagentních systémů v **Pythonu** a **.NET**. Spojuje silné stránky dvou předchozích projektů Microsoftu — podnikové funkce **Semantic Kernel** a víceagentní orchestraci **AutoGen** — do jednoho podporovaného rámce. Pokud dnes začínáte nový projekt s agenty, toto je doporučený nástupce AutoGen.

Rámec škáluje od jediného **chat agenta** až po komplexní **multiagentní workflow** a integruje se přímo s Microsoft Foundry, Azure OpenAI a OpenAI. Poskytuje také vestavěnou sledovatelnost přes OpenTelemetry, abyste mohli přesně sledovat, co vaši agenti dělají.

### Stav a nástroje

**Stav** – Rámec spravuje kontext konverzace za vás pomocí **vláken**. Agent si uchovává historii zpráv (uživatelské požadavky, volání nástrojů a jejich výsledky), takže každý krok navazuje na předešlé. Vláken lze také uložit, což umožňuje pozastavení a obnovení konverzace.

**Nástroje** – Agentovi poskytujete nástroje předáním běžných Python funkcí. Parametry s anotacemi typů jsou automaticky převedeny do schématu, aby model věděl, jak a kdy je volat (volání funkce). Rámec také podporuje Model Context Protocol (MCP) servery a hostované nástroje, jako je interpret kódu.

Zde je příklad jednoho agenta s vlastním nástrojem:

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

Pro připojení k Azure OpenAI v Microsoft Foundry místo toho předejte svůj endpoint a přihlašovací údaje klientovi:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Víceagentní workflow

Rámec opravdu vyniká v orchestraci několika agentů dohromady. Například můžete spouštět agenty jeden po druhém (každý předá svůj kontext dalšímu) nebo rozvětvit paralelně na několik agentů a agregovat jejich výsledky:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Spusťte agenty za sebou, přičemž předávejte kontext konverzace po řetězci
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Roztáhněte na agenty paralelně, poté agregujte jejich odpovědi
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Pro instalaci rámce a začátek:

```bash
pip install agent-framework-core
# Volitelné integrace
pip install agent-framework-openai       # OpenAI a Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Více informace najdete v [repositáři Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) a v [oficiální dokumentaci](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Dalším rámcem agentů, který prozkoumáme, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Je známý jako "code-first" agent, protože místo práce výhradně s `řetězci` může pracovat s DataFrames v Pythonu. To je extrémně užitečné pro úkoly analýzy dat a generování. Mohou to být například tvorba grafů a diagramů nebo generování náhodných čísel.

### Stav a nástroje

Pro správu stavu konverzace používá TaskWeaver koncept `Planner`. `Planner` je LLM, který přijímá požadavek od uživatele a plánuje úkoly potřebné k jeho splnění.

K dokončení úkolů je `Planner` vystaven kolekci nástrojů nazvaných `Plugins`. Mohou to být Python třídy nebo obecný interpret kódu. Tyto pluginy jsou uloženy jako embeddings, aby LLM mohl lépe vyhledávat správný plugin.

![Taskweaver](../../../translated_images/cs/taskweaver.da8559999267715a.webp)

Zde je příklad pluginu pro detekci anomálií:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kód je ověřen před spuštěním. Další funkcí pro správu kontextu v Taskweaver je `experience`. Experience umožňuje ukládat kontext konverzace dlouhodobě do YAML souboru. Toto lze nakonfigurovat tak, aby se LLM časem zlepšoval na určitých úkolech, pokud je vystaven předchozím konverzacím.

## JARVIS

Posledním rámcem agentů, který prozkoumáme, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Co dělá JARVIS jedinečným, je to, že používá LLM k řízení `stavu` konverzace a `nástroje` jsou jiné AI modely. Každý AI model je specializovaný model, který vykonává určité úkoly, jako je detekce objektů, přepis nebo titulkování obrázků.

![JARVIS](../../../translated_images/cs/jarvis.762ddbadbd1a3a33.webp)

LLM, jako model univerzálního použití, přijímá požadavek od uživatele a identifikuje specifický úkol a jakékoliv argumenty/data potřebná k jeho dokončení.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM pak formátuje požadavek způsobem, který specializovaný AI model umí interpretovat, například jako JSON. Jakmile AI model vrátí svůj predikční výstup na základě úkolu, LLM obdrží odpověď.

Pokud je k dokončení úkolu potřeba více modelů, interpretuje také odpovědi těchto modelů, než je spojí a vytvoří odpověď pro uživatele.

Příklad níže ukazuje, jak by to fungovalo, když uživatel požaduje popis a počet objektů na obrázku:

## Zadání

Chcete-li pokračovat ve svém studiu AI agentů, můžete stavět s Microsoft Agent Framework:

- Aplikaci, která simuluje obchodní schůzku různých oddělení vzdělávacího startupu.
- Vytvořte systémové zprávy, které vedou LLM k pochopení různých osobností a priorit, a umožněte uživateli prezentovat nový nápad na produkt.
- Následně by měl LLM generovat doplňující otázky od každého oddělení pro zpřesnění a zlepšení prezentace a nápadu na produkt.

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce si prohlédněte naši [kolekci učení generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde můžete dále rozšiřovat své znalosti o generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->