[![Open Source Models](../../../translated_images/cs/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Úvod

AI agenti představují vzrušující vývoj v oblasti generativní AI, který umožňuje velkým jazykovým modelům (LLM) vyvinout se z asistentů na agenty schopné podnikat akce. Rámce AI agentů umožňují vývojářům vytvářet aplikace, které dávají LLM přístup k nástrojům a správě stavu. Tyto rámce také zlepšují přehlednost, což uživatelům i vývojářům umožňuje sledovat akce plánované LLM, čímž se zlepšuje správa zkušeností.

Lekce pokryje následující oblasti:

- Porozumění tomu, co je AI Agent – Co přesně je AI Agent?
- Prozkoumání pěti různých rámců AI agentů – Čím jsou jedinečné?
- Aplikace těchto AI agentů na různé případů užití – Kdy bychom měli AI Agenty používat?

## Cíle učení

Po absolvování této lekce budete schopni:

- Vysvětlit, co jsou AI agenti a jak mohou být použiti.
- Mít porozumění rozdílům mezi některými populárními rámci AI agentů a jak se liší.
- Rozumět tomu, jak AI agenti fungují, abyste mohli s nimi vytvářet aplikace.

## Co jsou AI agenti?

AI agenti jsou velmi vzrušující oblastí ve světě generativní AI. S tímto vzrušením však někdy přichází zmatek ohledně pojmů a jejich aplikace. Pro zjednodušení a zahrnutí většiny nástrojů, které označují AI agenty, použijeme toto definici:

AI agenti umožňují velkým jazykovým modelům (LLM) vykonávat úkoly tím, že jim poskytují přístup ke **stavu** a **nástrojům**.

![Agent Model](../../../translated_images/cs/what-agent.21f2893bdfd01e6a.webp)

Definujme si tyto pojmy:

**Velké jazykové modely** – To jsou modely zmiňované v tomto kurzu, jako jsou GPT-5, GPT-4o, a Llama 3.3 atd.

**Stav** – To se vztahuje na kontext, ve kterém LLM pracuje. LLM využívá kontext svých minulých akcí a aktuálního kontextu, který usměrňuje jeho rozhodování pro následné akce. Rámce AI agentů umožňují vývojářům tento kontext snadněji udržovat.

**Nástroje** – K dokončení úkolu, který uživatel požadoval a který LLM naplánoval, potřebuje LLM přístup k nástrojům. Příklady nástrojů mohou být databáze, API, externí aplikace nebo dokonce jiný LLM!

Tyto definice vám doufejme poskytnou dobré základy, když se podíváme na jejich implementaci. Pojďme prozkoumat několik různých rámců AI agentů:

## LangChain Agent

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) jsou implementací výše uvedených definic.

Pro správu **stavu** používá vestavěnou funkci nazvanou `AgentExecutor`. Ta přijímá definovaného `agenta` a dostupné `nástroje`.

`AgentExecutor` také uchovává historii chatu, aby poskytoval kontext rozhovoru.

![Langchain Agents](../../../translated_images/cs/langchain-agents.edcc55b5d5c43716.webp)

LangChain nabízí [katalog nástrojů](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), které lze importovat do vaší aplikace a ke kterým může LLM získat přístup. Tyto nástroje vytváří komunita a tým LangChain.

Tyto nástroje pak můžete definovat a předat `AgentExecutor`.

Přehlednost je dalším důležitým aspektem při mluvení o AI agentech. Je důležité, aby vývojáři aplikací rozuměli, který nástroj LLM používá a proč. Pro to tým LangChain vyvinul LangSmith.

## AutoGen

Další rámec AI agentů, který budeme diskutovat, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hlavním zaměřením AutoGenu jsou konverzace. Agent je jak **konverzační**, tak **přizpůsobitelný**.

**Konverzační -** LLM mohou zahájit a pokračovat v rozhovoru s jiným LLM za účelem dokončení úkolu. To se dělá vytvořením `AssistantAgents` a udělením specifické systémové zprávy.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Přizpůsobitelný** - Agenti mohou být definováni nejen jako LLM, ale také jako uživatel nebo nástroj. Jako vývojář můžete definovat `UserProxyAgent`, který je zodpovědný za interakci s uživatelem za účelem získání zpětné vazby pro dokončení úkolu. Tato zpětná vazba může buď pokračovat ve vykonávání úkolu, nebo jej zastavit.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stav a nástroje

Pro změnu a správu stavu generuje asistent Agent Python kód k dokončení úkolu.

Zde je příklad průběhu:

![AutoGen](../../../translated_images/cs/autogen.dee9a25a45fde584.webp)

#### LLM definovaný systémovou zprávou

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Tato systémová zpráva nasměruje tento konkrétní LLM, které funkce jsou relevantní pro jeho úkol. Pamatujte, že v AutoGenu můžete mít několik definovaných AssistantAgents s různými systémovými zprávami.

#### Rozhovor zahájen uživatelem

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tato zpráva od user_proxy (člověka) zahájí proces agenta k prozkoumání možných funkcí, které by měl vykonat.

#### Funkce je vykonána

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po zpracování počátečního rozhovoru agent odešle návrh nástroje ke volání. V tomto případě je to funkce nazvaná `get_weather`. Podle vaší konfigurace může být tato funkce automaticky vykonána a přečtena agentem, nebo může být vykonána na základě vstupu uživatele.

Můžete najít seznam [AutoGen kódových příkladů](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), které vám pomohou dále prozkoumat, jak začít vývoj.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je otevřený SDK Microsoftu pro vytváření AI agentů a systémů s více agenty v **Pythonu** a **.NET**. Spojuje sílu dvou předchozích projektů Microsoftu — podnikové funkce **Semantic Kernel** a orchestraci více agentů **AutoGen** — do jednoho podporovaného rámce. Pokud dnes začínáte nový projekt agenta, toto je doporučený nástupce AutoGenu.

Rámec se škáluje od jednoho **chat agenta** až po složité **pracovní postupy s více agenty** a integruje se přímo s Microsoft Foundry, Azure OpenAI a OpenAI. Také poskytuje vestavěnou pozorovatelnost přes OpenTelemetry, takže můžete přesně sledovat, co vaši agenti dělají.

### Stav a nástroje

**Stav** – Rámec spravuje kontext konverzace za vás pomocí **vláken**. Agent sleduje historii zpráv (uživatelské požadavky, volání nástrojů a jejich výsledky), takže každý krok vychází z těch předchozích. Vlákna mohou být také uložena, což umožňuje pauzu a pozdější pokračování konverzace.

**Nástroje** – Agentovi předáváte nástroje pomocí obyčejných Python funkcí. Parametry s typovou anotací jsou automaticky převedeny na schéma, takže model ví, jak je kdy volat (volání funkcí). Rámec také podporuje servery Model Context Protocol (MCP) a hostované nástroje, jako je interpretr kódu.

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

Pro připojení k Azure OpenAI v Microsoft Foundry místo toho předáte svou koncovou adresu a přihlašovací údaje klientovi:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Pracovní postupy s více agenty

Rámec opravdu vyniká v orchestraci více agentů dohromady. Například můžete spouštět agenty jeden po druhém (každý předává svůj kontext dalšímu) nebo paralelně více agentů a sjednocovat jejich výsledky:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Spuštění agentů v sekvenci, přenášení kontextu konverzace podél řetězce
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Rozptýlení agentů paralelně, následné shromáždění jejich odpovědí
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Pro instalaci rámce a začátek práce:

```bash
pip install agent-framework-core
# Volitelné integrace
pip install agent-framework-openai       # OpenAI a Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Můžete dále prozkoumat v [Microsoft Agent Framework repozitáři](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) a [oficiální dokumentaci](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Dalším rámcem agentů, který prozkoumáme, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Je známý jako „code-first“ agent, protože místo práce čistě se `stringy` může pracovat s DataFrames v Pythonu. To je velmi užitečné pro úlohy analýzy a generování dat. Mohou to být například vytváření grafů a diagramů nebo generování náhodných čísel.

### Stav a nástroje

Pro správu stavu konverzace TaskWeaver používá koncept `Planner`. `Planner` je LLM, který přijímá požadavek od uživatele a mapuje úkoly, které je potřeba dokončit k jeho splnění.

K dokončení úkolů je `Planner` vystaven kolekci nástrojů nazývaných `Plugins`. Může jít o Python třídy nebo obecný interpretr kódu. Tyto pluginy jsou uloženy jako embeddingy, aby LLM mohl lépe vyhledat správný plugin.

![Taskweaver](../../../translated_images/cs/taskweaver.da8559999267715a.webp)

Zde je příklad pluginu pro detekci anomálií:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kód je před vykonáním ověřen. Další funkcí pro správu kontextu v Taskweaver je `experience`. Experience umožňuje kontext konverzace ukládat dlouhodobě v YAML souboru. To může být nastaveno tak, aby se LLM časem zlepšoval v určitých úkolech, protože je vystaven předchozím konverzacím.

## JARVIS

Poslední rámec agentů, který prozkoumáme, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Co dělá JARVIS unikátním je, že používá LLM ke správě `stavu` konverzace a `nástroje` jsou jiné AI modely. Každý z AI modelů je specializovaný model, který provádí určité úkoly, jako je detekce objektů, přepis nebo popis obrázku.

![JARVIS](../../../translated_images/cs/jarvis.762ddbadbd1a3a33.webp)

LLM, jako model s obecným účelem, přijímá požadavek od uživatele a identifikuje konkrétní úkol a případné argumenty/data potřebná k jeho dokončení.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM poté formátuje požadavek způsobem, který specializovaný AI model může interpretovat, například JSON. Jakmile AI model vrátí svůj odhad založený na úkolu, LLM obdrží odpověď.

Pokud je k dokončení úkolu potřeba více modelů, LLM také interpretuje odpovědi od těchto modelů dříve, než je sjednotí a vygeneruje odpověď uživateli.

Níže uvedený příklad ukazuje, jak by to fungovalo, když uživatel požaduje popis a počet objektů na obrázku:

## Úkol

Abychom pokračovali ve vašem učení AI agentů, můžete stavět s Microsoft Agent Framework:

- Aplikaci, která simuluje obchodní poradu různých oddělení vzdělávacího startupu.
- Vytvořit systémové zprávy, které vedou LLM k pochopení různých person a priorit a umožňují uživateli představit nový produkt.
- LLM by měl poté generovat doplňující otázky z každého oddělení, aby vylepšil a zdokonalil představení i produkt.

## Učení zde nekončí, pokračujte na cestě dál

Po dokončení této lekce si prohlédněte naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále zvyšovali své znalosti v generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->