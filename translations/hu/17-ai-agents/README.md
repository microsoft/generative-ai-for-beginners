[![Nyílt Forráskódú Modellek](../../../translated_images/hu/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Bevezetés

Az AI Ügynökök izgalmas fejlesztést jelentenek a Generatív AI területén, lehetővé téve, hogy a Nagy Nyelvi Modellek (LLM-ek) asszisztensekből olyan ügynökökké fejlődjenek, amelyek képesek cselekedetek végrehajtására. Az AI Ügynök keretrendszerek lehetővé teszik a fejlesztők számára olyan alkalmazások létrehozását, amelyek hozzáférést biztosítanak az LLM-eknek eszközökhöz és állapotkezeléshez. Ezek a keretrendszerek növelik a láthatóságot is, lehetővé téve a felhasználók és fejlesztők számára, hogy figyelemmel kísérjék az LLM-ek által tervezett cselekvéseket, ezáltal javítva a felhasználói élmény kezelését.

A tananyag a következő területeket fogja lefedni:

- Az AI Ügynök fogalmának megértése - Mi is pontosan az AI Ügynök?
- Öt különböző AI Ügynök Keretrendszer felfedezése - Mi teszi őket egyedivé?
- Ezeknek az AI Ügynököknek az alkalmazása különböző esetekben - Mikor érdemes AI Ügynököket használni?

## Tanulási célok

A tananyag elvégzése után képes leszel:

- Elmagyarázni, mik azok az AI Ügynökök és hogyan használhatók.
- Megérteni a különbségeket népszerű AI Ügynök Keretrendszerek között, és azok eltéréseit.
- Megérteni, hogyan működnek az AI Ügynökök az alkalmazások építéséhez.

## Mik azok az AI Ügynökök?

Az AI Ügynökök nagyon izgalmas területet képviselnek a Generatív AI világában. Ez az izgalom néha a fogalmak és alkalmazásuk összezavarodásával járhat. Annak érdekében, hogy egyszerű és minden, AI Ügynököt említő eszközt magába foglaló definíciót használjunk, a következőt fogjuk alkalmazni:

Az AI Ügynökök lehetővé teszik a Nagy Nyelvi Modellek (LLM-ek) számára, hogy feladatokat hajtsanak végre azáltal, hogy hozzáférést kapnak egy **állapothoz** és **eszközökhöz**.

![Agent Model](../../../translated_images/hu/what-agent.21f2893bdfd01e6a.webp)

Határozzuk meg ezeket a fogalmakat:

**Nagy Nyelvi Modellek** - Ezek a tanfolyam során említett modellek, mint például a GPT-3.5, GPT-4, Llama-2, stb.

**Állapot** - Ez utal arra a kontextusra, amiben az LLM dolgozik. Az LLM a korábbi cselekvések és az aktuális kontextus alapján alakítja döntéshozatalát a következő lépésekhez. Az AI Ügynök Keretrendszerek megkönnyítik a fejlesztők számára ennek a kontextusnak a fenntartását.

**Eszközök** - Ahhoz, hogy az LLM végrehajtsa a felhasználó által kért és általa tervezett feladatot, hozzáférnie kell eszközökhöz. Például egy adatbázis, egy API, egy külső alkalmazás vagy akár egy másik LLM is lehet eszköz!

Ezek a meghatározások remélhetőleg jó alapot adnak a továbblépéshez, miközben megnézzük az implementációikat. Vizsgáljunk meg néhány különböző AI Ügynök keretrendszert:

## LangChain Ügynökök

A [LangChain Ügynökök](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) megvalósítják a fentiekben bemutatott definíciókat.

Az **állapot** kezelésére beépített funkciót használ, amely az `AgentExecutor` nevet viseli. Ez fogadja a definiált `agent`-et és a rendelkezésre álló `tools`-okat.

Az `Agent Executor` eltárolja a chat előzményeit is, hogy megadja a beszélgetés kontextusát.

![Langchain Agents](../../../translated_images/hu/langchain-agents.edcc55b5d5c43716.webp)

A LangChain egy [eszköztárat](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) kínál, amelyet importálni lehet az alkalmazásodba, és amelyhez az LLM hozzáférhet. Ezeket a közösség és a LangChain csapata hozta létre.

Ezután definiálhatod ezeket az eszközöket, és átadhatod őket az `Agent Executor`-nek.

A láthatóság szintén fontos szempont AI Ügynökök esetén. Fontos, hogy az alkalmazás fejlesztői megértsék, melyik eszközt használja az LLM és miért. Erre a LangChain csapata fejlesztette ki a LangSmith-et.

## AutoGen

A következő, amit megvizsgálunk az AI Ügynök keretrendszerek között az [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Az AutoGen fő fókusza a párbeszéd. Az ügynökök egyszerre **beszélgetőképesek** és **testreszabhatóak**.

**Beszélgetőképes -** Az LLM-ek képesek egy másik LLM-mel beszélgetést kezdeni és folytatni egy feladat elvégzéséhez. Ezt `AssistantAgents` létrehozásával és egy specifikus rendszerüzenet megadásával érik el.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Testreszabható** - Az ügynökök nemcsak LLM-ként, hanem felhasználóként vagy eszközként is meghatározhatók. Fejlesztőként definiálhatsz egy `UserProxyAgent`-et, amely felelős a felhasználói visszajelzés kezeléséért a feladat végrehajtásában. Ez a visszajelzés vagy folytathatja a feladat végrehajtását, vagy megállíthatja azt.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Állapot és Eszközök

Az állapot változtatásához és kezeléséhez egy asszisztens Ügynök Python kódot generál a feladat elvégzéséhez.

Íme egy példa a folyamatról:

![AutoGen](../../../translated_images/hu/autogen.dee9a25a45fde584.webp)

#### LLM rendszerüzenettel definiálva

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ez a rendszerüzenet irányítja az adott LLM-et, hogy mely funkciók relevánsak a számára. Ne feledd, AutoGen-nel több különböző AssistantAgent is definiálható eltérő rendszerüzenetekkel.

#### A beszélgetést a felhasználó indítja

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ez az üzenet a user_proxy (ember) részéről indítja el az Ügynök folyamatát, hogy feltérképezze, mely funkciókat kell végrehajtania.

#### A funkció végrehajtásra kerül

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Miután az első beszélgetés feldolgozásra került, az Ügynök elküldi a javasolt eszközt, amelyet hívni kell. Ebben az esetben ez egy `get_weather` nevű funkció. Konfigurációtól függően ez a funkció automatikusan végrehajtásra kerülhet az Ügynök által, vagy a felhasználó bemenetétől függően.

További [AutoGen kód példákat](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) találsz, amikkel mélyebben megismerheted a fejlesztést.

## Microsoft Agent Framework

A [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) a Microsoft nyílt forráskódú SDK-ja AI Ügynökök és többügynökös rendszerek építéséhez **Python** és **.NET** környezetben. Egyesíti két korábbi Microsoft projekt – a **Semantic Kernel** vállalati funkcióit és az **AutoGen** többügynökös koordinációját – egyetlen, támogatott keretrendszerben. Ha ma kezdesz új ügynök projektet, ez az ajánlott utódja az AutoGennek.

A keretrendszer skálázható egyetlen **beszélgető ügynöktől** egészen a komplex **többügynökös munkafolyamatokig**, és közvetlenül integrálódik a Microsoft Foundry-val, az Azure OpenAI-val és az OpenAI-val. Beépített megfigyelhetőséget biztosít az OpenTelemetry-n keresztül, hogy pontosan nyomon kövesd, mit csinálnak az ügynökeid.

### Állapot és Eszközök

**Állapot** - A keretrendszer kezeli a beszélgetési kontextust helyetted **szálak** (threads) segítségével. Egy ügynök követi az üzenettörténetet (felhasználói kérések, eszközhívások és azok eredményei), így minden lépés az előzőkre épül. A szálak elmenthetők is, lehetővé téve a beszélgetés felfüggesztését és későbbi folytatását.

**Eszközök** - Egy ügynöknek egyszerű Python függvényeket adhatsz eszközként. A típusannotációval ellátott paraméterek automatikusan sémává alakulnak, így a modell tudja, hogyan és mikor hívja meg azokat (funkcióhívás). A keretrendszer támogatja a Model Context Protocol (MCP) szervereket és a hosztolt eszközöket, például a kódfordítót.

Íme egy példa egy egyedi eszközzel rendelkező egyszeri ügynökre:

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

Az Azure OpenAI-hoz való csatlakozáshoz a Microsoft Foundry-ban add át az endpointodat és a hitelesítő adatokat a kliensnek:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Többügynökös munkafolyamatok

A keretrendszer igazi erőssége az, hogy több ügynököt képes összehangolni. Például az ügynököket egymás után futtathatod úgy, hogy mindegyik továbbadja a kontextusát a következőnek, vagy párhuzamosan több ügynökhöz is lehet szétosztani a feladatokat, majd összegezni az eredményeket:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Ügynökök futtatása sorban, a beszélgetési kontextus átadása a láncon keresztül
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Párhuzamosan elosztás az ügynökök között, majd azok válaszainak összesítése
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

A keretrendszer telepítéséhez és a kezdéshez:

```bash
pip install agent-framework-core
# Opcionális integrációk
pip install agent-framework-openai       # OpenAI és Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Többet fedezhetsz fel a [Microsoft Agent Framework tárházban](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) és a [hivatalos dokumentációban](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

A következő ügynök keretrendszer, amit megnézünk, a [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ezt úgy ismerik, mint "kód-először" ügynököt, mert nem csak `stringekkel` dolgozik, hanem Python DataFrame-ekkel is. Ez nagyon hasznos adat elemzéshez és generálási feladatokhoz. Például grafikonok és diagramok készítéséhez, vagy véletlenszámok generálásához.

### Állapot és Eszközök

A beszélgetés állapotának kezelésére a TaskWeaver a `Planner` koncepciót használja. A `Planner` egy LLM, amely megkapja a felhasználók kérését, és felvázolja a teljesítendő feladatokat.

A feladatok elvégzéséhez a `Planner` hozzáfér az úgynevezett `Plugins` gyűjteményhez. Ezek lehetnek Python osztályok vagy általános kódfordítók. Ezek a pluginok beágyazva vannak tárolva, hogy az LLM jobban tudjon keresni a megfelelő plugint.

![Taskweaver](../../../translated_images/hu/taskweaver.da8559999267715a.webp)

Íme egy példa egy anomália detektáló pluginra:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

A kód végrehajtás előtt hitelesítésre kerül. Egy másik funkció a Taskweaver-ben a kontextus kezelésére az `experience`. Az experience lehetővé teszi, hogy egy beszélgetés kontextusa hosszú távon tárolódjon YAML fájlban. Ez konfigurálható úgy, hogy az LLM idővel javuljon bizonyos feladatokon, mivel korábbi beszélgetésekhez van kitéve.

## JARVIS

Az utolsó ügynök keretrendszer, amit megvizsgálunk, a [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ami különlegessé teszi JARVIS-t, hogy egy LLM kezeli a beszélgetés `állapotát`, míg a `tools` más AI modellek. Ezek az AI modellek specializált modellek, amelyek bizonyos feladatokat végeznek el, mint például objektumfelismerés, átirat készítés vagy képaláírás generálás.

![JARVIS](../../../translated_images/hu/jarvis.762ddbadbd1a3a33.webp)

Az LLM, mint általános célú modell, megkapja a felhasználó kérését, és azonosítja a specifikus feladatot és azokat az argumentumokat/adatokat, amelyek szükségesek a feladat elvégzéséhez.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Az LLM ezután olyan formátumba rendezi a kérést, amit a specializált AI modell értelmezni tud, például JSON-ként. Miután az AI modell visszaküldi az előrejelzését a feladat alapján, az LLM megkapja a választ.

Ha több modellre van szükség a feladat befejezéséhez, az LLM értelmezi az ezekről érkezett válaszokat, mielőtt összefogja őket a felhasználó válaszának generálásához.

Az alábbi példa bemutatja, hogyan működik ez, amikor a felhasználó egy kép objektumainak leírását és számát kéri:

## Feladat

Az AI Ügynökök tanulmányozásának folytatásához az alábbiakat építheted meg a Microsoft Agent Framework-kel:

- Egy alkalmazás, amely egy üzleti megbeszélést szimulál egy oktatási startup különböző osztályaival.
- Rendszerüzenetek létrehozása, amelyek irányítják az LLM-eket abban, hogy megértsék a különböző személyiségeket és prioritásokat, és lehetővé teszik a felhasználónak, hogy új termékötletet mutasson be.
- Az LLM-nek ezt követően kérdéseket kell generálnia az egyes osztályoktól, hogy finomítsa és javítsa az ötletet és a terméket.

## A tanulás itt nem áll meg, folytasd az utad

A tananyag elvégzése után nézd meg a [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd Generatív AI tudásodat!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->