<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:03:41+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "hu"
}
-->
# Bevezetés a Generatív Mesterséges Intelligenciába és a Nagy Nyelvi Modellekbe

_(Kattints a fenti képre, hogy megnézd a leckéhez tartozó videót)_

A generatív mesterséges intelligencia olyan mesterséges intelligencia, amely képes szövegeket, képeket és más típusú tartalmakat generálni. Az teszi fantasztikus technológiává, hogy demokratizálja a mesterséges intelligenciát, bárki használhatja mindössze egy szöveges parancs, egy természetes nyelven írt mondat segítségével. Nem szükséges olyan nyelveket megtanulnod, mint a Java vagy SQL, hogy valami értékeset hozz létre, elég csak a saját nyelvedet használnod, megfogalmaznod, mit szeretnél, és az AI modell javaslatot tesz. Ennek alkalmazási területei és hatása óriási, másodpercek alatt írhatsz vagy érthetsz meg jelentéseket, alkalmazásokat és még sok mást.

Ebben a tananyagban megvizsgáljuk, hogyan használja fel startupunk a generatív mesterséges intelligenciát, hogy új szcenáriókat nyisson meg az oktatás világában, és hogyan kezeljük a társadalmi hatásokból adódó elkerülhetetlen kihívásokat és a technológiai korlátokat.

## Bevezetés

Ez a lecke a következőket fedi le:

- Bevezetés az üzleti szcenárióba: startup ötletünk és küldetésünk.
- Generatív mesterséges intelligencia és hogyan jutottunk el a jelenlegi technológiai környezethez.
- Nagy nyelvi modell belső működése.
- Nagy Nyelvi Modellek fő képességei és gyakorlati felhasználási esetei.

## Tanulási célok

A lecke befejezése után meg fogod érteni:

- Mi a generatív mesterséges intelligencia és hogyan működnek a Nagy Nyelvi Modellek.
- Hogyan használhatod ki a nagy nyelvi modelleket különböző felhasználási esetekre, különös tekintettel az oktatási szcenáriókra.

## Szcenárió: oktatási startupunk

A Generatív Mesterséges Intelligencia (AI) az AI technológia csúcspontját képviseli, kitolva a határokat, amelyeket korábban lehetetlennek gondoltak. A generatív AI modellek számos képességgel és alkalmazással rendelkeznek, de ebben a tananyagban azt fogjuk megvizsgálni, hogyan forradalmasítja az oktatást egy fiktív startupon keresztül. Ezt a startupot _a mi startupunknak_ fogjuk nevezni. Startupunk az oktatás területén működik azzal az ambiciózus küldetésnyilatkozattal, hogy

> _javítsa a tanulás elérhetőségét globális szinten, biztosítva az oktatáshoz való egyenlő hozzáférést és személyre szabott tanulási élményeket nyújtson minden tanulónak, az igényeik szerint_.

Startupunk csapata tisztában van azzal, hogy ezt a célt nem tudjuk elérni az egyik legmodernebb eszköz - a Nagy Nyelvi Modellek (LLM-ek) - kihasználása nélkül.

A generatív mesterséges intelligencia várhatóan forradalmasítja a mai tanulási és tanítási módszereket, a diákok 24 órás virtuális tanárok rendelkezésére állnak, akik hatalmas mennyiségű információt és példát nyújtanak, a tanárok pedig innovatív eszközöket használhatnak a diákjaik értékelésére és visszajelzés adására.

Kezdetnek határozzunk meg néhány alapfogalmat és terminológiát, amelyeket a tananyag során használni fogunk.

## Hogyan jutottunk el a Generatív Mesterséges Intelligenciához?

A generatív AI modellek bejelentése által keltett rendkívüli _hype_ ellenére ez a technológia évtizedek óta készül, az első kutatási erőfeszítések az 1960-as évekig nyúlnak vissza. Most egy olyan ponton vagyunk, ahol az AI emberi kognitív képességekkel rendelkezik, mint például a beszélgetés, ahogy azt például az [OpenAI ChatGPT](https://openai.com/chatgpt) vagy a [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) is mutatja, amely szintén GPT modellt használ a Bing kereső beszélgetéseihez.

Visszalépve egy kicsit, az AI legelső prototípusai írógépes chatbotokból álltak, amelyek egy szakértői csoportból kivont tudásbázisra támaszkodtak és számítógépen reprezentálták azokat. A tudásbázisban lévő válaszokat a bemeneti szövegben megjelenő kulcsszavak váltották ki. Azonban hamar világossá vált, hogy egy ilyen megközelítés, írógépes chatbotok használatával, nem skálázható jól.

### Statisztikai megközelítés az AI-hoz: Gépi tanulás

Egy fordulópont érkezett el az 1990-es években, amikor egy statisztikai megközelítést alkalmaztak a szövegelemzésre. Ez új algoritmusok kifejlesztéséhez vezetett - amelyek gépi tanulás néven ismertek -, amelyek képesek mintákat tanulni az adatokból anélkül, hogy explicit módon programoznák őket. Ez a megközelítés lehetővé teszi a gépek számára az emberi nyelv megértésének szimulálását: egy statisztikai modellt szöveg-címke párosításokon képeznek ki, lehetővé téve a modell számára, hogy egy ismeretlen bemeneti szöveget osztályozzon egy előre meghatározott címkével, amely a üzenet szándékát képviseli.

### Neurális hálózatok és modern virtuális asszisztensek

Az utóbbi években a hardver technológiai fejlődése, amely képes nagyobb adatmennyiségek és bonyolultabb számítások kezelésére, ösztönözte az AI kutatást, ami a fejlett gépi tanulási algoritmusok, az úgynevezett neurális hálózatok vagy mélytanulási algoritmusok kifejlesztéséhez vezetett.

A neurális hálózatok (különösen a Recurrent Neural Networks - RNN-ek) jelentősen javították a természetes nyelvfeldolgozást, lehetővé téve a szöveg jelentésének értelmesebb módon történő reprezentálását, értékelve egy szó kontextusát egy mondatban.

Ez az a technológia, amely az új évszázad első évtizedében született virtuális asszisztenseket hajtotta, amelyek nagyon jártasak voltak az emberi nyelv értelmezésében, az igény felismerésében és egy cselekvés végrehajtásában annak kielégítésére - mint például egy előre meghatározott szkripttel való válaszadás vagy egy harmadik fél szolgáltatásának felhasználása.

### Napjainkban, Generatív AI

Így jutottunk el a Generatív AI-hoz, amely a mélytanulás egy részhalmazának tekinthető.

Évtizedek AI kutatása után egy új modellarchitektúra - amelyet _Transformer_-nek hívnak - leküzdötte az RNN-ek korlátait, képes sokkal hosszabb szövegsorozatokat bevinni. A Transformerek az figyelmi mechanizmuson alapulnak, lehetővé téve a modell számára, hogy különböző súlyokat adjon a bemeneteinek, 'nagyobb figyelmet' fordítva arra, ahol a legrelevánsabb információk összpontosulnak, függetlenül a szövegsorozat sorrendjétől.

A legtöbb újabb generatív AI modell - más néven Nagy Nyelvi Modellek (LLM-ek), mivel szöveges bemenetekkel és kimenetekkel dolgoznak - valóban ezen az architektúrán alapul. Ami érdekes ezekben a modellekben - amelyeket hatalmas mennyiségű, címkézetlen adatokkal képeztek ki, különböző forrásokból, mint könyvek, cikkek és weboldalak - az az, hogy sokféle feladathoz adaptálhatók, és nyelvtanilag helyes szöveget generálnak, amely kreativitás látszatát kelti. Tehát nemcsak, hogy hihetetlenül növelték a gép képességét a bemeneti szöveg 'megértésére', hanem lehetővé tették a képességüket, hogy eredeti választ generáljanak emberi nyelven.

## Hogyan működnek a nagy nyelvi modellek?

A következő fejezetben különböző generatív AI modelleket fogunk felfedezni, de most nézzük meg, hogyan működnek a nagy nyelvi modellek, különös tekintettel az OpenAI GPT (Generative Pre-trained Transformer) modellekre.

- **Tokenizáló, szöveg számmá alakítása**: A Nagy Nyelvi Modellek szöveget kapnak bemenetként és szöveget generálnak kimenetként. Azonban, mivel statisztikai modellek, sokkal jobban működnek számokkal, mint szövegsorozatokkal. Ezért minden bemenetet egy tokenizáló dolgoz fel, mielőtt a magmodell használná. Egy token egy szövegrész - amely változó számú karakterből áll, így a tokenizáló fő feladata a bemenet darabolása tokenek tömbjévé. Ezután minden tokenhez hozzárendelnek egy token indexet, amely az eredeti szövegrész egész számú kódolása.

- **Kimeneti tokenek előrejelzése**: Adott n token bemenetként (a maximális n modellről modellre változik), a modell képes egy tokent előrejelezni kimenetként. Ezt a tokent ezután a következő iteráció bemenetébe építik be, egy bővülő ablak mintázatban, lehetővé téve a felhasználói élmény javítását azzal, hogy egy (vagy több) mondatot kapunk válaszként. Ez magyarázza, miért, ha valaha játszottál a ChatGPT-vel, észrevehetted, hogy néha úgy tűnik, mintha a mondat közepén megállna.

- **Kiválasztási folyamat, valószínűségi eloszlás**: A kimeneti tokent a modell választja ki az alapján, hogy mekkora valószínűséggel fordul elő a jelenlegi szövegsorozat után. Ez azért van, mert a modell egy valószínűségi eloszlást jósol az összes lehetséges 'következő token' felett, amelyet a képzése alapján számítanak ki. Azonban nem mindig választják ki a legmagasabb valószínűségű tokent az eredő eloszlásból. Egy fokú véletlenszerűséget adnak ehhez a választáshoz, úgy, hogy a modell nem determinisztikus módon viselkedik - nem kapjuk meg pontosan ugyanazt a kimenetet ugyanazon bemenet esetén. Ez a véletlenszerűségi fokozat a kreatív gondolkodási folyamat szimulálására szolgál, és egy modellparaméter, az úgynevezett hőmérséklet segítségével hangolható.

## Hogyan hasznosíthatja startupunk a Nagy Nyelvi Modelleket?

Most, hogy jobban megértettük a nagy nyelvi modellek belső működését, nézzük meg a leggyakoribb feladatok gyakorlati példáit, amelyeket elég jól el tudnak végezni, szem előtt tartva üzleti szcenáriónkat. Azt mondtuk, hogy a Nagy Nyelvi Modellek fő képessége a _szöveg generálása a semmiből, egy természetes nyelven írt szöveges bemenet alapján_.

De milyen típusú szöveges bemenet és kimenet?
A nagy nyelvi modell bemenetét promptnak nevezik, míg a kimenetet completionsnak nevezik, amely a modell mechanizmusára utal, amely a következő tokent generálja a jelenlegi bemenet kiegészítésére. Mélyebben bele fogunk merülni abba, hogy mi is az a prompt, és hogyan tervezhetjük meg úgy, hogy a legtöbbet hozzuk ki modellünkből. De egyelőre mondjuk azt, hogy egy prompt tartalmazhat:

- Egy **utasítást**, amely meghatározza, milyen típusú kimenetet várunk a modelltől. Ez az utasítás néha tartalmazhat példákat vagy további adatokat.

  1. Cikk, könyv, termékértékelések és egyéb összefoglalása, valamint betekintések kinyerése strukturálatlan adatokból.
    
  2. Kreatív ötletelés és tervezés egy cikk, esszé, feladat vagy egyéb területen.
      
- Egy **kérdést**, amelyet egy ügynökkel folytatott beszélgetés formájában teszünk fel.
  
- Egy **szövegrészletet a kiegészítéshez**, amely implicit módon írási segítséget kér.
  
- Egy **kódrészletet** együtt azzal a kéréssel, hogy magyarázza el és dokumentálja azt, vagy egy megjegyzést, amely egy adott feladatot végrehajtó kódrészlet generálását kéri.

A fenti példák meglehetősen egyszerűek, és nem céljuk a Nagy Nyelvi Modellek képességeinek kimerítő bemutatása. Azért vannak, hogy megmutassák a generatív AI használatának potenciálját, különösen, de nem kizárólagosan oktatási kontextusban.

Emellett a generatív AI modell kimenete nem tökéletes, és néha a modell kreativitása ellene dolgozhat, ami olyan kimenetet eredményezhet, amely a szavak kombinációja, amelyet az emberi felhasználó a valóság eltorzításaként értelmezhet, vagy amely sértő lehet. A generatív AI nem intelligens - legalábbis az intelligencia átfogóbb meghatározásában, beleértve a kritikai és kreatív gondolkodást vagy az érzelmi intelligenciát; nem determinisztikus, és nem megbízható, mivel kitalációk, mint hibás hivatkozások, tartalom és állítások, helyes információkkal kombinálva lehetnek, és meggyőző és magabiztos módon mutathatók be. A következő leckékben foglalkozunk ezekkel a korlátokkal, és megnézzük, mit tehetünk azok enyhítésére.

## Feladat

A feladatod, hogy olvass többet a [generatív AI-ról](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst), és próbálj meg azonosítani egy területet, ahol ma generatív AI-t adnál hozzá, ahol még nincs. Hogyan lenne más a hatás, mint a "régi módon" csinálva, tudsz-e valamit, amit korábban nem tudtál, vagy gyorsabb vagy? Írj egy 300 szavas összefoglalót arról, hogy nézne ki álmaid AI startupja, és tartalmazz fejléceket, mint "Probléma", "Hogyan használnám az AI-t", "Hatás" és opcionálisan egy üzleti tervet.

Ha elvégezted ezt a feladatot, talán már készen is állsz arra, hogy jelentkezz a Microsoft inkubátorába, a [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) programba, amely krediteket kínál mind az Azure, mind az OpenAI, mentorálás és még sok más területen, nézd meg!

## Tudásellenőrzés

Mi igaz a nagy nyelvi modellekre?

1. Minden alkalommal pontosan ugyanazt a választ kapod.
2. Mindent tökéletesen csinál, kiváló a számok hozzáadásában, működő kódot készít stb.
3. A válasz változhat annak ellenére, hogy ugyanazt a promptot használod. Kiválóan ad egy első vázlatot valamiről, legyen az szöveg vagy kód. De javítanod kell az eredményeken.

A: 3, egy

**Felelősség kizárása**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.