[![Open Source Models](../../../translated_images/sk/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Úvod

AI Agenti predstavujú vzrušujúci vývoj v oblasti generatívnej AI, ktorý umožňuje veľkým jazykovým modelom (LLM) premeniť sa zo asistentov na agentov schopných vykonávať akcie. Frameworky AI Agentov umožňujú vývojárom vytvárať aplikácie, ktoré dávajú LLM prístup k nástrojom a správe stavu. Tieto frameworky tiež zlepšujú viditeľnosť, čo umožňuje používateľom a vývojárom sledovať akcie plánované LLM, čím sa zlepšuje správa používateľského zážitku.

V tejto lekcii sa budeme venovať nasledujúcim oblastiam:

- Pochopenie, čo je AI Agent - Čo presne je AI Agent?
- Preskúmanie piatich rôznych frameworkov AI Agentov - Čo ich robí jedinečnými?
- Aplikácia týchto AI Agentov pre rôzne prípady použitia - Kedy by sme mali používať AI Agentov?

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Vysvetliť, čo sú AI Agenti a ako sa dajú použiť.
- Mať prehľad o rozdieloch medzi niektorými populárnymi frameworkami AI Agentov a v čom sa líšia.
- Pochopiť, ako AI Agenti fungujú, aby ste mohli vytvárať aplikácie s ich použitím.

## Čo sú AI Agenti?

AI Agenti predstavujú veľmi vzrušujúcu oblasť vo svete generatívnej AI. S týmto nadšením však niekedy prichádza zmätok v pojmoch a ich aplikáciách. Aby sme to udržali jednoduché a zahrnuli väčšinu nástrojov, ktoré sa označujú ako AI Agenti, použijeme túto definíciu:

AI Agenti umožňujú veľkým jazykovým modelom (LLM) vykonávať úlohy tým, že im dávajú prístup ku **stavu** a **nástrojom**.

![Agent Model](../../../translated_images/sk/what-agent.21f2893bdfd01e6a.webp)

Definujme si tieto pojmy:

**Veľké jazykové modely** - Sú to modely, na ktoré sa v tomto kurze odkazujeme ako napríklad GPT-5, GPT-4o, a Llama 3.3 a podobne.

**Stav** - Toto odkazuje na kontext, v ktorom LLM pracuje. LLM využíva kontext svojich predchádzajúcich akcií a aktuálny kontext, ktorý riadi jeho rozhodovanie o nasledujúcich krokoch. Frameworky AI Agentov umožňujú vývojárom jednoduchšie udržiavať tento kontext.

**Nástroje** - Na splnenie úlohy, ktorú používateľ požaduje a ktorú LLM plánuje, potrebuje LLM prístup k nástrojom. Medzi príklady nástrojov patria databáza, API, externá aplikácia alebo dokonca ďalší LLM!

Tieto definície by vám mali poskytnúť dobrý základ pri ďalšom štúdiu ich implementácie. Poďme preskúmať niekoľko rôznych frameworkov AI Agentov:

## LangChain Agenti

[LangChain Agenti](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) sú implementáciou vyššie uvedených definícií.

Na správu **stavu** používa vstavanú funkciu nazvanú `AgentExecutor`. Tá prijíma definovaného `agenta` a dostupné `nástroje`.

`Agent Executor` tiež ukladá históriu chatu, aby poskytol kontext konverzácie.

![Langchain Agents](../../../translated_images/sk/langchain-agents.edcc55b5d5c43716.webp)

LangChain ponúka [katalóg nástrojov](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), ktoré je možné importovať do vašej aplikácie a ku ktorým môže LLM získať prístup. Sú vytvorené komunitou a tímom LangChain.

Tieto nástroje potom môžete definovať a odovzdať `Agent Executoru`.

Viditeľnosť je ďalším dôležitým aspektom, keď hovoríme o AI Agentoch. Pre vývojárov aplikácií je dôležité vedieť, ktorý nástroj LLM používa a prečo. Pre tento účel tím LangChain vyvinul LangSmith.

## AutoGen

Ďalší framework AI Agentov, ktorý preberieme, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hlavným zameraním AutoGen sú konverzácie. Agenti sú **konverzační** a **prispôsobiteľní**.

**Konverzační -** LLM môžu začať a pokračovať v konverzácii s iným LLM, aby splnili úlohu. Toto sa dosahuje vytváraním `AssistantAgents` a pridelením konkrétnej systémovej správy.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prispôsobiteľní** - Agenti môžu byť definovaní nielen ako LLM, ale aj ako používateľ alebo nástroj. Ako vývojár môžete definovať `UserProxyAgent`, ktorý zodpovedá za interakciu s používateľom pre spätnú väzbu pri plnení úlohy. Táto spätná väzba môže buď pokračovať vo vykonávaní úlohy, alebo ju zastaviť.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stav a nástroje

Na zmenu a správu stavu asistent Agenta generuje Python kód na vykonanie úlohy.

Tu je príklad tohto procesu:

![AutoGen](../../../translated_images/sk/autogen.dee9a25a45fde584.webp)

#### LLM definovaný systémovou správou

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Táto systémová správa smeruje konkrétny LLM, ktoré funkcie sú relevantné pre jeho úlohu. Pamätajte, že s AutoGen môžete mať viacero definovaných AssistantAgents s rôznymi systémovými správami.

#### Konverzácia je iniciovaná používateľom

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Táto správa od user_proxy (človeka) spustí proces Agenta, aby preskúmal možné funkcie, ktoré by mal vykonať.

#### Funkcia je vykonaná

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po spracovaní počiatočného chatu Agent navrhne nástroj na zavolanie. V tomto prípade je to funkcia s názvom `get_weather`. Podľa konfigurácie môže byť táto funkcia automaticky vykonávaná a čítaná Agentom, alebo môže byť vykonaná na základe vstupu používateľa.

Nájdete tu zoznam [príkladov kódu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), ktoré vám pomôžu lepšie pochopiť začiatky vývoja.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je open-source SDK od Microsoftu na vytváranie AI Agentov a multiagentových systémov v **Python** a **.NET**. Spája silné stránky dvoch predchádzajúcich projektov Microsoftu — podnikové funkcie **Semantic Kernel** a multiagentnú orchestráciu **AutoGen** — do jedného podporovaného frameworku. Ak dnes začínate nový projekt agentov, je to odporúčaný nástupca AutoGen.

Framework sa škáluje od jedného **chat agenta** až po komplexné **multiagentové pracovné postupy** a integruje sa priamo s Microsoft Foundry, Azure OpenAI a OpenAI. Tiež poskytuje vstavanú pozorovateľnosť cez OpenTelemetry, aby ste mohli sledovať presne, čo vaši agenti robia.

### Stav a nástroje

**Stav** - Framework spravuje kontext konverzácie za vás prostredníctvom **vlákien**. Agent udržiava históriu správ (požiadavky používateľa, volania nástrojov a ich výsledky), takže každý krok nadväzuje na predchádzajúce. Vlákna možno tiež ukladať, čo umožňuje konverzáciu pozastaviť a neskôr obnoviť.

**Nástroje** - Agentovi poskytujete nástroje zaslaním obyčajných Python funkcií. Typované parametre sa automaticky premietnu do schémy, takže model vie, ako a kedy ich volať (volanie funkcie). Framework tiež podporuje servery Model Context Protocol (MCP) a hostené nástroje, ako je interpret kódu.

Tu je príklad jedného agenta s vlastným nástrojom:

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

Na pripojenie k Azure OpenAI v Microsoft Foundry namiesto toho predajte endpoint a poverenia klientovi:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multiagentové pracovné postupy

Framework sa naozaj vyníma orchestráciou viacerých agentov dohromady. Napríklad môžete spúšťať agentov jeden po druhom (každý odovzdáva svoj kontext ďalšiemu) alebo rozvetviť na niekoľko agentov paralelne a agregovať ich výsledky:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Spustiť agentov v sekvencii, pričom sa konverzačný kontext prenáša pozdĺž reťazca
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Rozvetviť na agentov paralelne a potom zhrnúť ich odpovede
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Na inštaláciu frameworku a začiatok práce:

```bash
pip install agent-framework-core
# Voliteľné integrácie
pip install agent-framework-openai       # OpenAI a Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Viac informácií nájdete v [Microsoft Agent Framework repozitári](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) a [oficiálnej dokumentácii](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Ďalší framework agentov, ktorý preskúmame, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Je známy ako "code-first" agent, pretože namiesto práce výlučne so `stringami` môže pracovať s DataFrame v Pythone. To je mimoriadne užitočné pre úlohy analýzy a generovania dát, ako napríklad vytváranie grafov a diagramov alebo generovanie náhodných čísel.

### Stav a nástroje

Na správu kontextu konverzácie TaskWeaver používa koncept `Planner`. `Planner` je LLM, ktorý prijíma požiadavku od používateľov a mapuje úlohy, ktoré je potrebné vykonať na splnenie tejto požiadavky.

Na dokončenie týchto úloh je `Planner` vystavený kolekcii nástrojov nazývaných `Plugins`. Môžu to byť Python triedy alebo všeobecný interpret kódu. Tieto pluginy sú uložené ako embeddingy, aby LLM mohol lepšie vyhľadávať správny plugin.

![Taskweaver](../../../translated_images/sk/taskweaver.da8559999267715a.webp)

Tu je príklad pluginu na detekciu anomálií:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kód sa overuje pred vykonaním. Ďalšou funkciou na správu kontextu v Taskweaver je `experience`. Experience umožňuje kontext konverzácie uchovávať dlhodobo v YAML súbore. Toto sa dá nakonfigurovať tak, aby sa LLM časom zlepšoval v určitých úlohách na základe predchádzajúcich konverzácií.

## JARVIS

Posledným frameworkom agentov, ktorý preskúmame, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Čo robí JARVIS jedinečným je, že používa LLM na správu `stavu` konverzácie a `nástrojmi` sú iné AI modely. Každý z AI modelov je špecializovaný model, ktorý vykonáva konkrétne úlohy, ako je detekcia objektov, prepis alebo popis obrázkov.

![JARVIS](../../../translated_images/sk/jarvis.762ddbadbd1a3a33.webp)

LLM, ako všeobecný model, prijíma požiadavku od používateľa a identifikuje konkrétnu úlohu a akékoľvek argumenty/dáta potrebné na jej splnenie.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM potom formátuje požiadavku tak, aby ju špecializovaný AI model vedel interpretovať, napríklad v JSON formáte. Keď AI model vráti predikciu na základe úlohy, LLM prijme odpoveď.

Ak je potrebných niekoľko modelov na dokončenie úlohy, interpretuje aj odpovede z týchto modelov, skombinuje ich a následne vygeneruje odpoveď používateľovi.

Príklad nižšie ukazuje, ako by to fungovalo, keď používateľ požaduje popis a počet objektov na obrázku:

## Zadanie

Pre pokračovanie vo vašom učení o AI Agentoch môžete vytvoriť aplikáciu s Microsoft Agent Framework:

- Aplikácia, ktorá simuluje biznis stretnutie medzi rôznymi oddeleniami vzdelávacieho startupu.
- Vytvorte systémové správy, ktoré nasmerujú LLM, aby pochopili rôzne persony a priority, a umožnite používateľovi predstaviť nový produktový nápad.
- LLM by mal následne generovať doplňujúce otázky od každého oddelenia na spresnenie a zlepšenie prezentácie a produktového nápadu.

## Učenie sa tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si prezrite našu [kolekciu za učenie o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zvyšovali svoje vedomosti o generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->