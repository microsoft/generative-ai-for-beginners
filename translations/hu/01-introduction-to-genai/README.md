<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:30:24+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "hu"
}
-->
# Bevezetés a generatív mesterséges intelligenciába és a nagy nyelvi modellekbe

_(Kattints a fenti képre az óra videójának megtekintéséhez)_

A generatív mesterséges intelligencia olyan mesterséges intelligencia, amely képes szövegeket, képeket és más típusú tartalmakat generálni. Az teszi fantasztikus technológiává, hogy demokratizálja az AI-t, bárki használhatja, akár csak egy szöveges utasítással, egy természetes nyelven írt mondattal. Nem kell megtanulnod olyan nyelveket, mint a Java vagy az SQL, hogy valami érdemlegeset érj el, csak használnod kell a saját nyelvedet, megfogalmaznod, mit szeretnél, és az AI modell javaslatot tesz. Ennek alkalmazási lehetőségei és hatásai óriásiak, jelentéseket írhatsz vagy érthetsz meg, alkalmazásokat írhatsz, és még sok minden mást, mindezt másodpercek alatt.

Ebben a tantervben azt vizsgáljuk meg, hogyan használja startupunk a generatív mesterséges intelligenciát az oktatási világ új forgatókönyveinek megnyitására, és hogyan kezeljük az alkalmazás társadalmi hatásaival és a technológiai korlátokkal járó elkerülhetetlen kihívásokat.

## Bevezetés

Ez az óra a következőket fogja lefedni:

- Bevezetés az üzleti forgatókönyvbe: startup ötletünk és küldetésünk.
- Generatív mesterséges intelligencia és hogyan jutottunk el a jelenlegi technológiai környezethez.
- Nagy nyelvi modellek belső működése.
- Nagy nyelvi modellek fő képességei és gyakorlati alkalmazási esetei.

## Tanulási célok

Az óra befejezése után megérted:

- Mi a generatív mesterséges intelligencia és hogyan működnek a nagy nyelvi modellek.
- Hogyan lehet kihasználni a nagy nyelvi modelleket különböző alkalmazási esetekre, különös tekintettel az oktatási forgatókönyvekre.

## Forgatókönyv: oktatási startupunk

A generatív mesterséges intelligencia (AI) az AI technológia csúcsa, és a lehetetlennek hitt határokat feszegeti. A generatív AI modelleknek számos képessége és alkalmazási lehetősége van, de ebben a tantervben azt vizsgáljuk meg, hogyan forradalmasítja az oktatást egy fiktív startupon keresztül. Ezt a startupot _saját startupunknak_ nevezzük. Startupunk az oktatási területen dolgozik, ambiciózus küldetési nyilatkozattal

> _a tanulás hozzáférhetőségének javítása globális szinten, az oktatáshoz való egyenlő hozzáférés biztosítása és személyre szabott tanulási élmények nyújtása minden tanulónak, az igényeiknek megfelelően_.

Startupunk csapata tisztában van vele, hogy ezt a célt nem tudjuk elérni anélkül, hogy ne használnánk a modern idők egyik legerősebb eszközét – a nagy nyelvi modelleket (LLM-eket).

A generatív mesterséges intelligencia várhatóan forradalmasítja a mai tanulási és tanítási módszereket, a diákok rendelkezésére állnak virtuális tanárok, akik napi 24 órában hatalmas mennyiségű információt és példát szolgáltatnak, a tanárok pedig innovatív eszközöket használhatnak diákjaik értékelésére és visszajelzés adására.

Ahhoz, hogy elkezdjük, definiáljuk néhány alapvető fogalmat és terminológiát, amelyeket a tanterv során használni fogunk.

## Hogyan jutottunk el a generatív mesterséges intelligenciához?

Annak ellenére, hogy a generatív AI modellek bejelentése által keltett rendkívüli _hype_, ez a technológia évtizedek óta készül, az első kutatási erőfeszítések az 1960-as évekre nyúlnak vissza. Most eljutottunk arra a pontra, ahol az AI rendelkezik emberi kognitív képességekkel, mint például a beszélgetés, ahogy azt például az [OpenAI ChatGPT](https://openai.com/chatgpt) vagy a [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) mutatja, amely szintén GPT modellt használ a Bing kereső beszélgetéseihez.

Egy kicsit visszatekintve, az AI legelső prototípusai gépírásos chatbotokból álltak, amelyek egy szakértői csoportból kinyert tudásbázisra támaszkodtak, és ezt számítógépre ábrázolták. A tudásbázisban lévő válaszokat kulcsszavak váltották ki, amelyek megjelentek a bemeneti szövegben.
Azonban hamar világossá vált, hogy egy ilyen megközelítés, gépírásos chatbotok használatával, nem méretezhető jól.

### Statisztikai megközelítés az AI-hoz: Gépi tanulás

A fordulópont az 1990-es években érkezett el, a statisztikai megközelítés alkalmazásával a szövegelemzésre. Ez új algoritmusok – gépi tanulásként ismert – kifejlesztéséhez vezetett, amelyek képesek mintákat tanulni az adatokból anélkül, hogy kifejezetten programozva lennének. Ez a megközelítés lehetővé teszi a gépek számára, hogy szimulálják az emberi nyelv megértését: egy statisztikai modellt szöveg-címke párokon képeznek ki, lehetővé téve a modell számára, hogy az ismeretlen bemeneti szöveget egy előre meghatározott címkével osztályozza, amely a üzenet szándékát képviseli.

### Neurális hálózatok és modern virtuális asszisztensek

Az elmúlt években a hardver technológiai fejlődése, amely képes nagyobb mennyiségű adatot és bonyolultabb számításokat kezelni, ösztönözte az AI kutatását, ami fejlett gépi tanulási algoritmusok, úgynevezett neurális hálózatok vagy mély tanulási algoritmusok kifejlesztéséhez vezetett.

A neurális hálózatok (és különösen a visszatérő neurális hálózatok – RNN-ek) jelentősen javították a természetes nyelv feldolgozását, lehetővé téve a szöveg jelentésének értelmesebb módon történő ábrázolását, értékelve a szó kontextusát egy mondatban.

Ez a technológia táplálta a virtuális asszisztenseket, amelyek az új évszázad első évtizedében születtek, nagyon ügyesek az emberi nyelv értelmezésében, az igény azonosításában és egy cselekvés végrehajtásában annak kielégítésére – mint például egy előre meghatározott szkript válaszadása vagy egy harmadik fél szolgáltatásának fogyasztása.

### Jelenkor, generatív mesterséges intelligencia

Így jutottunk el a generatív mesterséges intelligenciához ma, amely a mély tanulás egyik alcsoportjaként tekinthető.

Évtizedes kutatások után az AI területén egy új modell architektúra – _Transformer_ néven – leküzdötte az RNN-ek korlátait, képes sokkal hosszabb szövegszekvenciákat fogadni bemenetként. A transformerek az attention mechanizmuson alapulnak, lehetővé téve a modell számára, hogy különböző súlyokat adjon a kapott bemeneteknek, „nagyobb figyelmet” fordítva oda, ahol a legrelevánsabb információ koncentrálódik, függetlenül azok sorrendjétől a szövegszekvenciában.

A legújabb generatív AI modellek többsége – más néven nagy nyelvi modellek (LLM-ek), mivel szöveges bemenetekkel és kimenetekkel dolgoznak – valójában ezen az architektúrán alapul. Ami érdekes ezekben a modellekben – amelyek hatalmas mennyiségű címkézetlen adaton lettek képezve különböző forrásokból, mint például könyvek, cikkek és weboldalak – az, hogy sokféle feladathoz adaptálhatók és grammatikailag helyes szöveget generálhatnak, ami kreativitás látszatát kelti. Tehát nemcsak hogy hihetetlenül növelték a gép képességét a bemeneti szöveg „megértésére”, hanem lehetővé tették a képességüket, hogy eredeti választ generáljanak emberi nyelven.

## Hogyan működnek a nagy nyelvi modellek?

A következő fejezetben különböző típusú generatív AI modelleket fogunk felfedezni, de most nézzük meg, hogyan működnek a nagy nyelvi modellek, különös tekintettel az OpenAI GPT (Generative Pre-trained Transformer) modellekre.

- **Tokenizáló, szöveg számmá alakítása**: A nagy nyelvi modellek szöveget kapnak bemenetként és szöveget generálnak kimenetként. Azonban, mivel statisztikai modellek, sokkal jobban működnek számokkal, mint szövegszekvenciákkal. Ezért minden bemenet a modellhez egy tokenizálón keresztül kerül feldolgozásra, mielőtt a fő modell használná. A token egy szövegrész – változó számú karakterből áll, így a tokenizáló fő feladata a bemenet felosztása egy token tömbre. Ezután minden token egy token indexhez van rendelve, ami az eredeti szövegrész egész számú kódolása.

- **Kimeneti tokenek előrejelzése**: Adott n token bemenetként (a maximális n modellről modellre változik), a modell képes egy token előrejelzésére kimenetként. Ez a token aztán bekerül a következő iteráció bemenetébe, egy bővülő ablak mintázatban, lehetővé téve a jobb felhasználói élményt, hogy egy (vagy több) mondatot kapjunk válaszként. Ez megmagyarázza, hogy ha valaha játszottál a ChatGPT-vel, észrevehetted, hogy néha úgy tűnik, mintha megállna egy mondat közepén.

- **Kiválasztási folyamat, valószínűségi eloszlás**: A kimeneti tokent a modell választja ki annak valószínűsége alapján, hogy előfordul a jelenlegi szövegszekvencia után. Ennek oka, hogy a modell egy valószínűségi eloszlást jósol az összes lehetséges „következő token” fölött, amelyet a képzés alapján számítanak ki. Azonban nem mindig a legmagasabb valószínűségű token kerül kiválasztásra az eredmény eloszlásából. Egy fokú véletlenszerűség adódik hozzá ehhez a választáshoz, úgy, hogy a modell nem-determinista módon működik - nem kapjuk meg ugyanazt a kimenetet ugyanazon bemenetre. Ez a véletlenszerűség fokozata hozzáadódik a kreatív gondolkodás folyamatának szimulálásához, és egy modell paraméter, az úgynevezett hőmérséklet segítségével állítható.

## Hogyan tudja startupunk kihasználni a nagy nyelvi modelleket?

Most, hogy jobban megértjük a nagy nyelvi modell belső működését, nézzünk néhány gyakorlati példát a leggyakoribb feladatokra, amelyeket jól tudnak elvégezni, tekintettel üzleti forgatókönyvünkre.
Azt mondtuk, hogy a nagy nyelvi modell fő képessége _szöveg generálása a semmiből, kiindulva egy szöveges bemenetből, amely természetes nyelven van megírva_.

De milyen típusú szöveges bemenet és kimenet?
A nagy nyelvi modell bemenete promptként ismert, míg a kimenet teljesítésként, amely a modell mechanizmusára utal, amely a következő tokent generálja a jelenlegi bemenet befejezéséhez. Mélyen bele fogunk merülni abba, hogy mi a prompt és hogyan lehet úgy tervezni, hogy a legtöbbet hozzuk ki modellünkből. De egyelőre csak annyit mondjunk, hogy egy prompt tartalmazhat:

- Egy **utasítást**, amely meghatározza, milyen típusú kimenetet várunk a modelltől. Ez az utasítás néha tartalmazhat példákat vagy további adatokat.

  1. Cikk, könyv, termékértékelések és még sok más összefoglalása, valamint betekintések kinyerése strukturálatlan adatokból.
    
  2. Kreatív ötletelés és tervezés cikk, esszé, feladat vagy más írásához.
      
- Egy **kérdést**, amelyet egy ügynökkel folytatott beszélgetés formájában tesznek fel.

- Egy **szövegrész befejezése**, amely implicit módon írási segítségkérés.

- Egy **kódrészlet** együtt a magyarázat és dokumentálás kérésével, vagy egy megjegyzés, amely arra kéri, hogy generáljon egy kódrészletet, amely egy adott feladatot hajt végre.

A fenti példák meglehetősen egyszerűek, és nem céljuk, hogy kimerítően bemutassák a nagy nyelvi modellek képességeit. Arra szolgálnak, hogy megmutassák a generatív mesterséges intelligencia használatának potenciálját, különösen, de nem kizárólag oktatási kontextusban.

Továbbá, a generatív AI modell kimenete nem tökéletes, és néha a modell kreativitása ellen dolgozhat, ami olyan kimenetet eredményez, amely a szavak kombinációja, amelyet az emberi felhasználó a valóság eltorzításának vagy sértőnek értelmezhet. A generatív mesterséges intelligencia nem intelligens - legalábbis a intelligencia átfogóbb meghatározásában, amely magában foglalja a kritikus és kreatív érvelést vagy érzelmi intelligenciát; nem determinisztikus, és nem megbízható, mivel hamisítások, például hibás hivatkozások, tartalom és állítások kombinálódhatnak helyes információval, és meggyőző és magabiztos módon bemutathatók. A következő órákban foglalkozni fogunk ezekkel a korlátokkal, és megnézzük, mit tehetünk azok enyhítésére.

## Feladat

A feladatod, hogy olvass többet a [generatív AI-ról](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst), és próbálj meg azonosítani egy területet, ahol ma hozzáadnád a generatív AI-t, ahol még nincs. Hogyan lenne más a hatás a "régi módon" való megvalósításhoz képest, tudsz-e valamit csinálni, amit korábban nem tudtál, vagy gyorsabb vagy-e? Írj egy 300 szavas összefoglalót arról, hogy milyen lenne álmaid AI startupja, és tartalmazz olyan fejléceket, mint "Probléma", "Hogyan használnám az AI-t", "Hatás" és opcionálisan egy üzleti tervet.

Ha elvégezted ezt a feladatot, akár készen állhatsz jelentkezni a Microsoft inkubátorába, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), ahol krediteket kínálunk az Azure-ra, az OpenAI-re, mentorálásra és még sok másra, nézd meg!

## Tudásellenőrzés

Mi igaz a nagy nyelvi modellekre?

1. Minden alkalommal pontosan ugyanazt a választ kapod.
2. Tökéletesen csinálja a dolgokat, nagyszerű a számok összeadásában, működő kódot produkál stb.
3. A válasz változhat annak ellenére, hogy ugyanazt a promptot használjuk. Nagyszerű első vázlatot ad

**Felelősség kizárása**:  
Ez a dokumentum AI fordítószolgáltatással, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.