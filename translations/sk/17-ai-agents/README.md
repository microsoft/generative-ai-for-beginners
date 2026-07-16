[![Open Source Models](../../../translated_images/sk/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Úvod

AI Agent predstavujú vzrušujúci vývoj v oblasti Generatívnej AI, ktorý umožňuje veľkým jazykovým modelom (LLM) vyvinúť sa z asistentov na agentov schopných konať. Frameworky AI Agentov umožňujú vývojárom vytvárať aplikácie, ktoré dávajú LLM prístup k nástrojom a správe stavu. Tieto frameworky tiež zlepšujú viditeľnosť, čím umožňujú používateľom a vývojárom sledovať akcie plánované LLM, a tým zlepšujú správu skúseností.

V tejto lekcii sa budeme venovať týmto oblastiam:

- Pochopenie, čo je AI Agent - Čo presne je AI Agent?
- Preskúmanie piatich rôznych frameworkov AI Agentov - Čo ich robí jedinečnými?
- Použitie týchto AI Agentov na rôzne prípady použitia - Kedy by sme mali používať AI Agentov?

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Vysvetliť, čo sú AI Agenti a ako ich možno použiť.
- Mať prehľad o rozdieloch medzi niektorými populárnymi frameworkmi AI Agentov a ako sa líšia.
- Pochopiť, ako AI Agenti fungujú, aby ste s nimi mohli budovať aplikácie.

## Čo sú AI Agenti?

AI Agenti sú veľmi vzrušujúca oblasť vo svete Generatívnej AI. S týmto nadšením sú niekedy spojené aj zmätky v pojmoch a ich použití. Aby sme to udržali jednoduché a zahrnuli väčšinu nástrojov, ktoré sa označujú ako AI Agenti, použijeme túto definíciu:

AI Agenti umožňujú veľkým jazykovým modelom (LLM) vykonávať úlohy tým, že im dávajú prístup k **stavu** a **nástrojom**.

![Agent Model](../../../translated_images/sk/what-agent.21f2893bdfd01e6a.webp)

Definujme si tieto pojmy:

**Veľké jazykové modely** - Sú to modely, na ktoré sa odkazuje v tomto kurze, ako GPT-3.5, GPT-4, Llama-2 a podobne.

**Stav** - To sa vzťahuje na kontext, v ktorom LLM pracuje. LLM využíva kontext svojich predchádzajúcich akcií a aktuálny kontext, ktorý riadi jeho rozhodovanie pre nasledujúce akcie. Frameworky AI Agentov umožňujú vývojárom ľahšie udržiavať tento kontext.

**Nástroje** - Na dokončenie úlohy, ktorú používateľ požaduje a ktorú LLM naplánoval, potrebuje LLM prístup k nástrojom. Príkladmi nástrojov môžu byť databáza, API, externá aplikácia alebo dokonca iný LLM!

Tieto definície vám dúfajme poskytnú dobrý základ do budúcna, keď si pozrieme, ako sú implementované. Preskúmajme niekoľko rôznych frameworkov AI Agentov:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) je implementáciou definícií, ktoré sme poskytli vyššie.

Na správu **stavu** používa vstavanú funkciu nazvanú `AgentExecutor`. Táto prijíma definovaný `agent` a dostupné `tools`.

`AgentExecutor` tiež ukladá históriu chatu na poskytovanie kontextu rozhovoru.

![Langchain Agents](../../../translated_images/sk/langchain-agents.edcc55b5d5c43716.webp)

LangChain ponúka [katalóg nástrojov](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), ktoré môžu byť importované do vašej aplikácie, ku ktorým môže LLM získať prístup. Tieto sú vytvorené komunitou a tímom LangChain.

Potom môžete tieto nástroje definovať a odovzdať ich do `AgentExecutor`.

Viditeľnosť je ďalším dôležitým aspektom pri rozprávaní o AI Agento. Je dôležité, aby vývojári aplikácií rozumeli, ktorý nástroj LLM používa a prečo. Preto tím v LangChain vyvinul LangSmith.

## AutoGen

Ďalším frameworkom AI Agentov, o ktorom budeme hovoriť, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Hlavným zameraním AutoGen sú konverzácie. Agenti sú zároveň **konverzační** a **prispôsobiteľní**.

**Konverzační -** LLM môžu začať a pokračovať v rozhovore s iným LLM na dokončenie úlohy. Toto sa robí vytváraním `AssistantAgents` a poskytovaním konkrétnej systémovej správy.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prispôsobiteľní** - Agenti môžu byť definovaní nielen ako LLM, ale aj ako používateľ alebo nástroj. Ako vývojár môžete definovať `UserProxyAgent`, ktorý je zodpovedný za interakciu s používateľom pre spätnú väzbu pri vykonávaní úlohy. Táto spätná väzba môže buď pokračovať v vykonávaní úlohy alebo ju zastaviť.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stav a nástroje

Na zmenu a správu stavu asistent Agent generuje Python kód na dokončenie úlohy.

Tu je príklad procesu:

![AutoGen](../../../translated_images/sk/autogen.dee9a25a45fde584.webp)

#### LLM definované systémovou správou

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Táto systémová správa usmerňuje konkrétny LLM, ktoré funkcie sú relevantné pre jeho úlohu. Pamätajte, že pri AutoGen môžete mať viacero definovaných AssistantAgents s rôznymi systémovými správami.

#### Chat začína používateľ

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Táto správa od user_proxy (človeka) je to, čo spustí proces agenta preskúmať možné funkcie, ktoré by mal vykonať.

#### Funkcia je vykonaná

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po spracovaní počiatočného chatu agent navrhne nástroj na volanie. V tomto prípade je to funkcia s názvom `get_weather`. V závislosti od vašej konfigurácie môže byť táto funkcia automaticky vykonaná a prečítaná agentom alebo môže byť vykonaná na základe vstupu používateľa.

Môžete nájsť zoznam [AutoGen ukážok kódu](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) na ďalšie preskúmanie, ako začať s vývojom.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je open-source SDK Microsoftu na vytváranie AI Agentov a systémov s viacerými agentmi v jazykoch **Python** a **.NET**. Spojuje silné stránky dvoch skorších Microsoft projektov — podnikové funkcie **Semantic Kernel** a orchestráciu viacerých agentov **AutoGen** — do jedného, podporovaného frameworku. Ak dnes začínate nový agentový projekt, toto je odporúčaný následník AutoGen.

Framework škáluje od jedného **chat agenta** až po komplexné **pracovné procesy s viacerými agentmi** a integruje sa priamo s Microsoft Foundry, Azure OpenAI a OpenAI. Tiež poskytuje vstavanú pozorovateľnosť cez OpenTelemetry, aby ste mohli presne sledovať, čo vaši agenti robia.

### Stav a nástroje

**Stav** - Framework spravuje kontext rozhovoru za vás cez **vlákna**. Agent udržiava históriu správ (požiadavky používateľa, volania nástrojov a ich výsledky), takže každý krok nadväzuje na predchádzajúce. Vlákna môžu byť taktiež perzistentné, čo umožňuje rozhovor pozastaviť a neskôr pokračovať.

**Nástroje** - Agentovi poskytujete nástroje odovzdaním obyčajných Python funkcií. Parametre s typovou anotáciou sa automaticky premenia na schému, takže model vie, ako a kedy ich volať (volanie funkcií). Framework tiež podporuje Model Context Protocol (MCP) servery a hosťované nástroje, ako je interpretr kódu.

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

Ak sa chcete pripojiť k Azure OpenAI v Microsoft Foundry, namiesto toho odovzdajte svoj koncový bod a poverenia klientovi:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Pracovné procesy s viacerými agentmi

Framework vyniká najmä pri orchestrácii viacerých agentov spoločne. Napríklad môžete spúšťať agentov jeden za druhým (každý odovzdáva svoj kontext nasledujúcemu) alebo paralelne rozvetviť na niekoľko agentov a agregovať ich výsledky:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Spustite agentov postupne, pričom kontext konverzácie sa odovzdáva pozdĺž reťazca
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Rozvetvite na agentov paralelne a potom zhromaždite ich odpovede
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Na inštaláciu frameworku a začatie práce:

```bash
pip install agent-framework-core
# Voliteľné integrácie
pip install agent-framework-openai       # OpenAI a Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Môžete preskúmať viac v [Microsoft Agent Framework repozitári](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) a [oficiálnej dokumentácii](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Ďalší framework agentov, ktorý preskúmame, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Je známy ako "code-first" agent, pretože namiesto práce striktne so `stringami` môže pracovať s DataFrames v Pythone. Toto je mimoriadne užitočné pre úlohy analýzy dát a generácie. Môžu to byť napríklad tvorba grafov a diagramov alebo generovanie náhodných čísel.

### Stav a nástroje

Na správu stavu rozhovoru TaskWeaver používa koncept `Planner`. `Planner` je LLM, ktorý prevezme požiadavku používateľov a naplánuje úlohy, ktoré je potrebné vykonať na splnenie tejto požiadavky.

Na dokončenie úloh je `Planner` vystavený zbierke nástrojov nazývaných `Plugins`. Môžu to byť Python triedy alebo všeobecný interpreter kódu. Tieto pluginy sú uložené ako embeddings, aby LLM mohol lepšie vyhľadávať správny plugin.

![Taskweaver](../../../translated_images/sk/taskweaver.da8559999267715a.webp)

Tu je príklad pluginu na spracovanie detekcie anomálií:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kód je overený pred vykonaním. Ďalšou vlastnosťou na správu kontextu v Taskweaver je `experience`. Experience umožňuje uchovávať kontext rozhovoru dlhodobo v YAML súbore. Môže byť nakonfigurovaná tak, aby sa LLM v priebehu času zlepšoval v určitých úlohách, keďže je vystavený predchádzajúcim rozhovorom.

## JARVIS

Posledným frameworkom agentov, ktorý preskúmame, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Čo robí JARVIS jedinečným, je to, že používa LLM na správu `stavu` rozhovoru a `nástroje` sú iné AI modely. Každý z AI modelov je špecializovaný model, ktorý vykonáva určité úlohy, ako detekcia objektov, prepis alebo tvorba popisov obrázkov.

![JARVIS](../../../translated_images/sk/jarvis.762ddbadbd1a3a33.webp)

LLM, ako všeobecný model, prijíma požiadavku od používateľa a identifikuje konkrétnu úlohu a akékoľvek argumenty/dáta potrebné na dokončenie úlohy.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM potom formátuje požiadavku spôsobom, ktorý môže špecializovaný AI model interpretovať, napríklad ako JSON. Keď AI model vráti svoju predikciu na základe úlohy, LLM prijme odpoveď.

Ak je na dokončenie úlohy potrebných viacero modelov, LLM tiež interpretuje odpoveď z týchto modelov pred tým, než ich spojí na vytvorenie odpovede používateľovi.

Príklad nižšie ukazuje, ako by toto fungovalo, keď používateľ požaduje popis a počet objektov na obrázku:

## Zadanie

Na pokračovanie vo svojom učení o AI Agento môžete vytvoriť s Microsoft Agent Framework:

- Aplikáciu, ktorá simuluje obchodné stretnutie rôznych oddelení startupu v oblasti vzdelávania.
- Vytvoriť systémové správy, ktoré vedú LLM k pochopeniu rôznych osobností a priorít a umožňujú používateľovi predložiť nápad na nový produkt.
- LLM by potom mal generovať otázky na doplnenie z každého oddelenia na zdokonalenie a vylepšenie návrhu a produktu.

## Učenie tu nekončí, pokračujte na ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia o Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v zvyšovaní svojich znalostí o Generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->