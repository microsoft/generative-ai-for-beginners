[![Open Source Models](../../../translated_images/hu/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Bevezetés

Az AI ügynökök izgalmas fejlődést jelentenek a generatív MI területén, lehetővé téve, hogy a nagy nyelvi modellek (LLM-ek) asszisztensekből cselekvőképes ügynökökké fejlődjenek. Az AI ügynök keretrendszerek fejlesztők számára lehetőséget adnak olyan alkalmazások létrehozására, amelyek hozzáférést biztosítanak az LLM-eknek az eszközökhöz és állapotkezeléshez. Ezek a keretrendszerek növelik az átláthatóságot is, lehetővé téve a felhasználók és fejlesztők számára, hogy nyomon kövessék az LLM-ek által tervezett cselekvéseket, ezáltal javítva a felhasználói élmény menedzsmentjét.

Az óra az alábbi témákat fogja lefedni:

- Az AI ügynökök megértése - Mi is az pontosan az AI ügynök?
- Öt különböző AI ügynök keretrendszer felfedezése - Mi teszi őket egyedivé?
- Ezeknek az AI ügynököknek a különböző felhasználási esetekhez való alkalmazása - Mikor érdemes AI ügynököket használni?

## Tanulási célok

A lecke elvégzése után képes leszel:

- Elmagyarázni, mik azok az AI ügynökök és hogyan használhatók.
- Érteni néhány népszerű AI ügynök keretrendszer közötti különbségeket és eltéréseket.
- Megérteni az AI ügynökök működését, hogy képes legyél alkalmazásokat fejleszteni velük.

## Mik azok az AI ügynökök?

Az AI ügynökök egy nagyon izgalmas területet képviselnek a generatív MI világában. Az izgalom gyakran a kifejezések és alkalmazások zavarával jár együtt. Az egyszerűség kedvéért és a legtöbb AI ügynökre utaló eszköz bevonásával a következő definíciót használjuk:

Az AI ügynökök lehetővé teszik, hogy a nagy nyelvi modellek (LLM-ek) feladatokat hajtsanak végre azáltal, hogy hozzáférést kapnak egy **állapothoz** és **eszközökhöz**.

![Agent Model](../../../translated_images/hu/what-agent.21f2893bdfd01e6a.webp)

Meghatározzuk ezeket a fogalmakat:

**Nagy nyelvi modellek** - Ezek a kurzus egészében említett modellek, például GPT-5, GPT-4o, és Llama 3.3 stb.

**Állapot** - Ez a kontextust jelenti, amelyben az LLM dolgozik. Az LLM a múltbéli cselekvések és a jelenlegi kontextus alapján irányítja döntéshozatalát a további cselekvésekhez. Az AI ügynök keretrendszerek megkönnyítik a fejlesztők számára ennek a kontextusnak a fenntartását.

**Eszközök** - Ahhoz, hogy az LLM a felhasználó kérését és az általa megtervezett feladatot elvégezze, hozzáférésre van szüksége eszközökhöz. Néhány példa lehet adatbázis, API, külső alkalmazás vagy akár egy másik LLM!

Ezek a definíciók remélhetőleg jó alapot adnak a továbblépéshez, miközben megvizsgáljuk gyakorlati megvalósításukat. Nézzünk meg néhány különböző AI ügynök keretrendszert:

## LangChain Ügynökök

A [LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) megvalósítja a fent megadott definíciókat.

Az **állapot** kezelésére egy beépített funkciót használ, az `AgentExecutor`-t. Ez elfogadja a definiált `agent`-et és az elérhető `tools`-okat.

Az `Agent Executor` tárolja a csevegés előzményeit is, hogy biztosítsa a kontextust.

![Langchain Agents](../../../translated_images/hu/langchain-agents.edcc55b5d5c43716.webp)

A LangChain egy [eszköztár katalogust](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) kínál, amely importálható és hozzáférhető az LLM számára az alkalmazásodban. Ezeket a közösség és a LangChain csapata készíti.

Ezután definiálhatod ezeket az eszközöket és átadhatod az `Agent Executor`-nak.

Az láthatóság is fontos az AI ügynököknél. Fontos, hogy a fejlesztők megértsék, melyik eszközt használja az LLM és miért. Ehhez a LangChain csapata kifejlesztette a LangSmith-et.

## AutoGen

A következő AI ügynök keretrendszer az [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Az AutoGen fő fókusza a beszélgetésekre irányul. Az ügynökök **beszélgetnek** és **testreszabhatók**.

**Beszélgethető -** Az LLM-ek képesek beszélgetést kezdeni és folytatni egy másik LLM-mel a feladat teljesítéséhez. Ezt úgy érik el, hogy `AssistantAgents`-et hoznak létre és specifikus rendszerüzenetet adnak nekik.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Testreszabható** - Az ügynökök nem csak LLM-ként definiálhatók, hanem felhasználóként vagy eszközként is. Fejlesztőként definiálhatsz `UserProxyAgent`-et, amely a felhasználóval való interakcióért felelős a visszajelzésért a feladat végrehajtásához. Ez a visszajelzés folytathatja vagy leállíthatja a feladat végrehajtását.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Állapot és eszközök

Az állapot megváltoztatására és kezelésére az asszisztens ügynök Python kódot generál a feladat elvégzéséhez.

Íme egy példa a folyamatról:

![AutoGen](../../../translated_images/hu/autogen.dee9a25a45fde584.webp)

#### LLM meghatározása egy rendszerüzenettel

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ez a rendszerüzenet irányítja ezt a konkrét LLM-et, hogy mely funkciók relevánsak a feladatára. Ne feledd, az AutoGen-nél több definiált AssistantAgent is lehet különböző rendszerüzenetekkel.

#### A csevegést a felhasználó indítja

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ez a felhasználói_proxi (Ember) üzenet indítja el az ügynök folyamatát, hogy feltérképezze a végrehajtandó funkciókat.

#### A funkció végrehajtása

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Miután az első csevegést feldolgozták, az ügynök ajánl egy hívandó eszközt, jelen esetben egy `get_weather` nevű függvényt. Beállítástól függően ez a függvény automatikusan végrehajtható és az ügynök által olvasható, vagy felhasználói beviteltől függően fut le.

Megtalálható egy lista [AutoGen kódmintákról](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), hogy bővebben megismerhesd az építés kezdetét.

## Microsoft Agent Framework

A [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) a Microsoft nyílt forráskódú SDK-ja AI ügynökök és többügynökös rendszerek építésére **Python**-ban és **.NET**-ben. Egyesíti a korábbi Microsoft projektek erősségeit — az **Semantic Kernel** vállalati funkcióit és az **AutoGen** többügynökös összehangolását — egyetlen, támogatott keretrendszerbe. Ha ma kezdesz új ügynök projektbe, ez az ajánlott utódja az AutoGennek.

A keretrendszer skálázható az egyetlen **csevegőügynöktől** a bonyolult **többügynökös munkafolyamatokig**, és közvetlenül integrálható a Microsoft Foundry-val, Azure OpenAI-val és OpenAI-val. Beépített megfigyelhetőséget is nyújt OpenTelemetry-n keresztül, így pontosan nyomon követheted, mit csinálnak az ügynökeid.

### Állapot és eszközök

**Állapot** - A keretrendszer a beszélgetés kontextusát **szálakon** kezeli. Egy ügynök nyomon követi az üzenettörténetet (felhasználói kérések, eszköz hívások és azok eredményei), így minden forduló az előzőkre épül. A szálak el is menthetők, így egy beszélgetés szüneteltethető és később folytatható.

**Eszközök** - Eszközökkel látod el az ügynököt, ha sima Python függvényeket adsz át. A típus annotált paraméterek automatikusan sémává alakulnak, így a modell tudja, mikor és hogyan hívja meg őket (függvényhívás). A keretrendszer támogatja Model Context Protocol (MCP) szervereket és hosztolt eszközöket, mint például a kódértelmezőt.

Íme egy példa egy egyedi eszközzel rendelkező egyetlen ügynökre:

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

Az Azure OpenAI-hoz való csatlakozáshoz Microsoft Foundry-ban az alábbi módon add át a végpontot és hitelesítő adatokat az ügyfélnek:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Többügynökös munkafolyamatok

A keretrendszer igazán akkor tűnik ki, amikor több ügynök összehangolását végzi. Például futtathatod őket egymás után (mindegyik átadja a kontextusát a következőnek), vagy párhuzamosan több ügynökre terjesztheted ki és összesítheted az eredményeket:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Futtassa az ügynököket egymás után, továbbítva a beszélgetési kontextust a láncon keresztül
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Párhuzamosan terjessze ki az ügynökökre, majd egyesítse a válaszaikat
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

A keretrendszer telepítéséhez és az induláshoz:

```bash
pip install agent-framework-core
# Opcionális integrációk
pip install agent-framework-openai       # OpenAI és Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

További információkat találhatsz a [Microsoft Agent Framework tárolóban](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) és a [hivatalos dokumentációban](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

A következő ügynök keretrendszer, amit megvizsgálunk, a [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ezt „code-first” ügynökként ismerik, mert nem csak `string`-ekkel dolgozik, hanem Python DataFrame-kkel is. Ez rendkívül hasznos adat elemzés és generálási feladatoknál, például grafikonok és diagramok készítésénél vagy véletlenszám generálásnál.

### Állapot és eszközök

A beszélgetés állapotának kezelésére a TaskWeaver a `Planner` fogalmát használja. A `Planner` egy LLM, amely megkapja a felhasználók kérését és feltérképezi az elvégzendő feladatokat a kérés teljesítéséhez.

A feladatok elvégzéséhez a `Planner` rendelkezik egy `Plugins` nevű eszközkészlettel. Ezek lehetnek Python osztályok vagy általános kódértelmezők. Ezeket a pluginokat beágyazott formában tárolják, hogy az LLM jobban tudja keresni a megfelelő plugint.

![Taskweaver](../../../translated_images/hu/taskweaver.da8559999267715a.webp)

Íme egy példa egy anomália detektálást kezelő pluginra:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

A kód végrehajtás előtt ellenőrzésre kerül. Egy másik kontextuskezelési funkció a Taskweavernél az `experience`. Az experience lehetővé teszi, hogy a beszélgetés kontextusa hosszú távon egy YAML fájlban tárolódjon. Ez konfigurálható úgy, hogy az LLM idővel javuljon bizonyos feladatokon, ha korábbi beszélgetésekhez hozzáfér.

## JARVIS

Az utolsó ügynök keretrendszer, amit megvizsgálunk, a [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ami egyedivé teszi a JARVIS-t, hogy egy LLM kezeli a beszélgetés `állapotát`, míg a `tools` más AI modellek. Minden AI modell specializált feladatokat végez, mint például objektumfelismerés, átírás vagy kép leírás.

![JARVIS](../../../translated_images/hu/jarvis.762ddbadbd1a3a33.webp)

Az LLM, mint általános célú modell, megkapja a felhasználói kérést, azonosítja a konkrét feladatot és a szükséges argumentumokat/adatokat a feladat elvégzéséhez.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Az LLM ezt követően olyan formátumba rendezi a kérést, amelyet a specializált AI modell értelmezni tud, például JSON. Miután az AI modell visszaadja előrejelzését a feladat alapján, az LLM megkapja a választ.

Ha több modell szükséges a feladat végrehajtásához, az LLM értelmezi a modellek válaszait is, mielőtt összevonja őket a végső válasz generálásához a felhasználónak.

Az alábbi példa azt mutatja, hogyan működik ez, amikor a felhasználó képleírást és számlálást kér az objektumokról:

## Feladat

Az AI ügynökök tanulásának folytatásához építhetsz Microsoft Agent Frameworkkel:

- Egy alkalmazást, amely egy oktatási startup különböző részlegeinek üzleti találkozóját szimulálja.
- Rendszerüzeneteket készíteni, amelyek irányítják az LLM-eket különböző személyiségek és prioritások megértésére, és lehetővé teszik a felhasználónak egy új termék ötlet bemutatását.
- Az LLM-nek utólagos kérdéseket kell generálnia minden részlegtől az ötlet és a termék bemutató finomítására és javítására.

## A tanulás itt nem ér véget, folytasd az utazást

A lecke elvégzése után nézd meg a [Generatív MI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív MI ismereteidet!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->