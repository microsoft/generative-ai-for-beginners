# Alacsony kódú AI alkalmazások építése  

[![Alacsony kódú AI alkalmazások építése](../../../translated_images/hu/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)  

> _(Kattints a fenti képre a leckevideó megtekintéséhez)_  

## Bevezetés  

Most, hogy megtanultuk, hogyan építsünk képgeneráló alkalmazásokat, beszéljünk az alacsony kódról. A generatív AI számos különböző területen használható, beleértve az alacsony kódot is, de mi is az az alacsony kód, és hogyan adhatunk AI-t hozzá?  

Alkalmazások és megoldások építése könnyebbé vált a hagyományos fejlesztők és fejlesztők nélküli felhasználók számára is az Alacsony Kódú Fejlesztési Platformok használatával. Az Alacsony Kódú Fejlesztési Platformok lehetővé teszik, hogy kevés vagy egyáltalán ne kelljen kódolni az alkalmazások és megoldások létrehozásához. Ez egy vizuális fejlesztési környezet biztosításával valósul meg, amely lehetővé teszi az összetevők húzását és eldobását az alkalmazások és megoldások építéséhez. Ez gyorsabb és kevesebb erőforrást igénylő alkalmazás- és megoldásépítést tesz lehetővé. Ebben a leckében mélyebben megvizsgáljuk, hogyan használjuk az Alacsony Kódot, és hogyan fejleszthetjük az alacsony kódú fejlesztést AI segítségével a Power Platformon.  

A Power Platform lehetőséget biztosít a szervezetek számára, hogy felhatalmazzák csapataikat saját megoldásaik építésére egy intuitív, alacsony kódú vagy kód nélküli környezetben. Ez a környezet leegyszerűsíti a megoldások építésének folyamatát. A Power Platformmal a megoldások napok vagy hetek alatt építhetők meg hónapok vagy évek helyett. A Power Platform öt kulcsfontosságú termékből áll: Power Apps, Power Automate, Power BI, Power Pages és Copilot Studio.  

Ez a lecke lefedi:  

- Bevezetés a generatív AI-be a Power Platformon  
- Bevezetés a Copilotba és annak használatába  
- Generatív AI használata alkalmazások és folyamatok építéséhez a Power Platformban  
- Az AI modellek megértése a Power Platformon az AI Builder segítségével  
- Intelligens ügynökök építése a Microsoft Copilot Studioval  

## Tanulási célok  

A lecke végére képes leszel:  

- Megérteni, hogyan működik a Copilot a Power Platformban.  

- Egy diákfeladat-követő alkalmazás építése az oktatási startupunk számára.  

- Egy számlafeldolgozó folyamat létrehozása, amely AI segítségével kinyeri az információkat a számlákból.  

- A legjobb gyakorlatok alkalmazása a "Szöveg létrehozása GPT-vel" AI modell használata közben.  

- Megérteni, mi a Microsoft Copilot Studio, és hogyan lehet intelligens ügynököket építeni vele.  

Az eszközök és technológiák, amelyeket ebben a leckében fogsz használni:  

- **Power Apps**, a diákfeladat-követő alkalmazáshoz, amely egy alacsony kódú fejlesztési környezet, amellyel alkalmazásokat lehet építeni adatok nyomon követésére, kezelésére és kölcsönhatásának biztosítására.  

- **Dataverse**, amely az adatokat tárolja a diákfeladat-követő alkalmazáshoz, ahol a Dataverse egy alacsony kódú adatplatform, amely az alkalmazás adatainak tárolására szolgál.  

- **Power Automate**, a számlafeldolgozó folyamathoz, ahol egy alacsony kódú fejlesztési környezetet kapsz munkafolyamatok építéséhez, hogy automatizáld a számlafeldolgozás folyamatát.  

- **AI Builder**, a számlafeldolgozó AI modellhez, ahol előre elkészített AI modelleket használsz a startupunk számláinak feldolgozására.  

## Generatív AI a Power Platformban  

Az alacsony kódú fejlesztés és alkalmazás fejlesztése generatív AI segítségével kulcsfontosságú fókuszterület a Power Platform számára. A cél, hogy bárki építhessen AI-alapú alkalmazásokat, webhelyeket, irányítópultokat és automatizálhassa a folyamatokat AI használatával, _anélkül, hogy adattudományi szakértelemre lenne szüksége_. Ezt a célt a generatív AI integrálásával érjük el az alacsony kódú fejlesztési élménybe a Power Platformon, Copilot és AI Builder formájában.  

### Hogyan működik ez?  

A Copilot egy AI asszisztens, amely lehetővé teszi, hogy Power Platform megoldásokat építs leíró módon, természetes nyelven folytatott párbeszédes lépések során. Például megadhatod az AI asszisztensednek, hogy milyen mezőket használjon az alkalmazásod, és az elkészíti mind az alkalmazást, mind az alapul szolgáló adatmodellt, vagy megadhatod, hogyan állíts be egy folyamatot a Power Automate-ben.  

Copilot alapú funkciókat is használhatsz az alkalmazásod képernyőin, hogy a felhasználók párbeszédes interakciókon keresztül mélyebb betekintéseket nyerhessenek.  

Az AI Builder egy alacsony kódú AI képesség a Power Platformban, amely lehetővé teszi AI Modellek használatát a folyamatok automatizálásához és eredmények előrejelzéséhez. Az AI Builder segítségével AI-t vihetsz az alkalmazásaidba és folyamataidba, amelyek kapcsolódnak az adataidhoz a Dataverse-ban vagy különböző felhőadat-forrásokban, például SharePoint, OneDrive vagy Azure esetén.  

A Copilot elérhető a Power Platform összes termékében: Power Apps, Power Automate, Power BI, Power Pages és Copilot Studio (korábban Power Virtual Agents). Az AI Builder elérhető a Power Apps-ben és Power Automate-ban. Ebben a leckében a Copilot és az AI Builder használatára fókuszálunk a Power Apps-ben és Power Automate-ban, hogy megoldást építsünk az oktatási startupunk számára.  

### Copilot a Power Apps-ben  

A Power Platform részeként a Power Apps egy alacsony kódú fejlesztési környezet, amely alkalmazások építését teszi lehetővé az adatok nyomon követésére, kezelésére és kölcsönhatására. Ez egy alkalmazásfejlesztési szolgáltatásokból álló csomag, amely méretezhető adatplatformot és felhőszolgáltatásokhoz, illetve helyszíni adatokhoz való csatlakozási lehetőséget biztosít. A Power Apps segítségével böngészőkön, táblagépeken és telefonokon futtatható alkalmazásokat építhetsz, amelyeket megoszthatsz munkatársaiddal is. A Power Apps egyszerű felületével segíti a felhasználókat az alkalmazásfejlesztésbe való bevezetésben, így minden üzleti felhasználó vagy profi fejlesztő építhet egyéni alkalmazásokat. Az alkalmazásfejlesztést a generatív AI is támogatja a Copilot révén.  

A Power Apps-ben a Copilot AI asszisztens lehetővé teszi, hogy leírd, milyen alkalmazásra van szükséged és milyen információkat szeretnél az alkalmazásban nyomon követni, gyűjteni vagy megjeleníteni. A Copilot a leírásod alapján egy reszponzív vászon (Canvas) alkalmazást hoz létre. Ezt az alkalmazást később testre szabhatod az igényeid szerint. Az AI Copilot emellett generál és javasol egy Dataverse táblát a szükséges mezőkkel az általad követni kívánt adatok tárolására, valamint néhány mintaadatot. Ebben a leckében később részletesen megnézzük, mi az a Dataverse és hogyan használhatod a Power Apps-ben. Ezután a táblát is testre szabhatod a Copilot asszisztens funkció segítségével, párbeszédes lépéseken keresztül. Ez a funkció könnyen elérhető a Power Apps kezdőképernyőjén.  

### Copilot a Power Automate-ban  

A Power Platform részeként a Power Automate lehetővé teszi a felhasználók számára, hogy automatizált munkafolyamatokat hozzanak létre alkalmazások és szolgáltatások között. Segít automatizálni ismétlődő üzleti folyamatokat, például kommunikációt, adatgyűjtést és jóváhagyási döntéseket. Egyszerű felületének köszönhetően a technikai tudásszinttől függetlenül (kezdőktől a tapasztalt fejlesztőkig) mindenki automatizálhat munkafolyamatokat. A munkafolyamat-fejlesztési élményt generatív AI is gazdagítja a Copilot használatával.  

A Power Automate-ban a Copilot AI asszisztens lehetővé teszi, hogy leírd, milyen típusú folyamatot szeretnél, és milyen műveleteket kívánsz végrehajtani. A Copilot a leírás alapján létrehoz egy folyamatot, amelyet aztán testre szabhatsz az igényeid szerint. Az AI Copilot emellett generál és javasolja a szükséges műveleteket a feladat automatizálásához. Ebben a leckében később megnézzük, mik azok a folyamatok és hogyan használhatók a Power Automate-ban. A műveleteket aztán a Copilot asszisztens funkcióval, párbeszédes lépéseken keresztül testre szabhatod. Ez a funkció könnyen elérhető a Power Automate kezdőképernyőjén.  

## Intelligens ügynökök építése a Microsoft Copilot Studioval  

A [Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (korábban Power Virtual Agents) a Power Platform alacsony kódú tagja az **AI ügynökök** építéséhez – párbeszédes copilotok, amelyek kérdésekre válaszolnak, műveleteket hajtanak végre és automatizálják a felhasználók nevében a feladatokat. Akárcsak a Power Platform többi része, ezeket az ügynököket vizuális, természetes nyelvre alapozó élményben építed: leírod, hogy mit szeretnél, hogy az ügynök tegyen, és a Copilot Studio segít az instrukciók, tudás és műveletek felépítésében.  

Az oktatási startupunk számára építhetsz például egy olyan ügynököt, amely válaszol a hallgatók kérdéseire a kurzusokról, ellenőrzi a beadási határidőket, sőt emailt küld az oktatónak – mindezt kód írása nélkül.  

Íme néhány a Copilot Studio legújabb képességei közül, amelyek hatékonnyá teszik:  

- **Generatív válaszok a tudásodból**. Ahelyett, hogy minden beszélgetést kézzel írnál meg, összekapcsolhatsz **tudásforrásokat** – nyilvános weboldalakat, SharePointot, OneDrive-ot, Dataverse-t, feltöltött fájlokat, vagy vállalati adatokat kapcsolókon keresztül – és az ügynök ezekből alapozott válaszokat generál.  

- **Generatív összehangolás**. A merev indító kulcsszavak helyett az ügynök AI segítségével érti meg a kérést, és dinamikusan dönt arról, hogy mely tudás, témák és műveletek együttesével teljesítse azt, beleértve több lépés láncolását is.  

- **Műveletek és kapcsolók**. Az ügynökök nem csak chatelnek, hanem *tesznek* is. Megadhatsz az ügynöknek műveleteket több mint 1500 előre elkészített Power Platform kapcsolón, Power Automate folyamatokon, egyedi REST API-kon, utasításokon vagy **Model Context Protocol (MCP)** szervereken keresztül.  

- **Autonóm ügynökök**. Az ügynökök nem csak chat ablakban válaszolnak. Létrehozhatsz **autonóm ügynököket**, amelyek események – például új email, új rekord a Dataverse-ben vagy fájl feltöltése – hatására lépnek működésbe, majd háttérben végrehajtanak egy feladatot.  

- **Több ügynök összehangolása**. Az ügynökök egymást is hívhatják. Egy Copilot Studio ügynök átadhatja a vezérlést vagy bővíthető más ügynökökkel, beleértve a Microsoft 365 Copilotban publikált és a Microsoft Foundry-ban épített ügynököket is.  

- **Modell választás**. Az alapértelmezett modelleken túl behozhatsz modelleket a Microsoft Foundry modell katalógusból, hogy személyre szabhasd az ügynök gondolkodását és válaszait.  

- **Publikálás bárhol**. Az elkészült ügynök több csatornára is publikálható – Microsoft Teams, Microsoft 365 Copilot, weboldal vagy egyéni alkalmazás és még sok más – biztonság, hitelesítés és analitika kezelése a Power Platform adminisztrációs élményén keresztül történik.  

Első ügynöködet a [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) oldalon kezdheted el építeni, és többet tanulhatsz a [Microsoft Copilot Studio dokumentációjából](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).  

## Feladat: Diákfeladatok és számlák kezelése startupunk számára, Copilot használatával  

A startupunk online kurzusokat biztosít a hallgatók számára. A startup gyorsan nőtt, és most nehéz lépést tartani a kurzus iránti kereslettel. Felkértek Power Platform fejlesztőnek, hogy segíts nekik egy alacsony kódú megoldás építésében a diákfeladatok és számlák kezelésére. A megoldásnak lehetővé kell tennie a diákfeladatok nyomon követését és kezelését egy alkalmazáson keresztül, illetve az automatizált számlafeldolgozást egy munkafolyamat segítségével. Kérték, hogy Generatív AI használatával fejleszd a megoldást.  

Ha elkezded a Copilot használatát, a [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) segítségével kezdhetsz el a promptokkal dolgozni. Ez a könyvtár lista formájában tartalmaz utasításokat, amelyeket alkalmazások és folyamatok építéséhez használhatsz a Copilot-ban. A könyvtári utasítások segítségével ötleteket kaphatsz, hogyan írd le követelményeidet a Copilot számára.  

### Diákfeladat-követő alkalmazás építése startupunk számára  

Az oktatók startupunkban nehezen tartották nyilván a diákfeladatokat. Egy táblázatkezelőt használtak a feladatok követésére, de ez egyre nehezebben kezelhető lett, ahogy nőtt a diákok száma. Megkértek, hogy építs egy alkalmazást, amely segít nyomon követni és kezelni a diákfeladatokat. Az alkalmazás lehetővé teszi új feladatok hozzáadását, megtekintését, frissítését és törlését. Az alkalmazásnak azt is lehetővé kell tennie az oktatók és diákok számára, hogy megtekintsék a már értékelt és még nem értékelt feladatokat.  

Az alkalmazást a következő lépéseken keresztül építjük meg a Power Apps Copilot segítségével:  

1. Navigálj a [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) kezdőképernyőjére.  

1. Használd a szövegterületet a kezdőképernyőn, hogy leírd az általad építeni kívánt alkalmazást. Például: **_Egy alkalmazást szeretnék építeni a diákfeladatok nyomon követésére és kezelésére_**. Kattints a **Küldés** gombra, hogy elküldd az utasítást az AI Copilotnak.  

![Írd le az építeni kívánt alkalmazást](../../../translated_images/hu/copilot-chat-prompt-powerapps.84250f341d060830.webp)  

1. Az AI Copilot javasol egy Dataverse táblát a szükséges mezőkkel az általad követni kívánt adatok tárolásához, és néhány mintaadatot. A táblát a Copilot asszisztens funkció páros párbeszédes lépései segítségével testre szabhatod.  

   > **Fontos**: A Dataverse a Power Platform alapul szolgáló adatplatformja. Ez egy alacsony kódú adatplatform az alkalmazás adatainak tárolására. Teljes körűen kezelt szolgáltatás, amely biztonságosan tárolja az adatokat a Microsoft felhőjében, és a Power Platform környezeteden belül van elhelyezve. Beépített adatirányítási képességekkel rendelkezik, mint az adat osztályozása, adat nyomon követése, finomhangolt hozzáférés-vezérlés és még sok más. További információt a Dataverse-ről [itt](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko) találsz.  

   ![Javasolt mezők az új tábládban](../../../translated_images/hu/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)  

1. Az oktatók szeretnének e-mailt küldeni azoknak a diákoknak, akik leadták a feladataikat, hogy tájékoztassák őket a feladat előrehaladásáról. A Copilot segítségével új mezőt adhatsz a táblához a diák e-mail címének tárolására. Például használhatod a következő utasítást az új mező hozzáadásához: **_Szeretnék egy oszlopot hozzáadni a diák e-mail címének tárolásához_**. Kattints a **Küldés** gombra, hogy elküldd az utasítást az AI Copilotnak.  

![Új mező hozzáadása](../../../translated_images/hu/copilot-new-column.35e15ff21acaf274.webp)  

1. Az AI Copilot létrehoz egy új mezőt, amelyet aztán igényeid szerint testre szabhatsz.  


1. Miután befejezte a táblázatot, kattintson a **Create app** gombra az alkalmazás létrehozásához.

1. Az AI Copilot a leírása alapján létrehoz egy reszponzív Canvas alkalmazást. Ezután testreszabhatja az alkalmazást az igényeinek megfelelően.

1. Az oktatók számára, hogy e-maileket küldjenek a diákoknak, használhatja a Copilotot egy új képernyő hozzáadására az alkalmazáshoz. Például a következő utasítást adhatja meg egy új képernyő hozzáadásához az alkalmazáshoz: **_Szeretnék egy képernyőt hozzáadni, ahol e-maileket küldhetek a diákoknak_**. Kattintson a **Send** gombra az utasítás elküldéséhez az AI Copilotnak.

![Adding a new screen via a prompt instruction](../../../translated_images/hu/copilot-new-screen.2e0bef7132a17392.webp)

1. Az AI Copilot létrehoz egy új képernyőt, amit aztán testreszabhat az igényeinek megfelelően.

1. Miután befejezte az alkalmazást, kattintson a **Save** gombra az alkalmazás mentéséhez.

1. Az oktatókkal való megosztáshoz kattintson a **Share** gombra, majd ismét a **Share** gombra. Ezután megoszthatja az alkalmazást az oktatókkal, ha megadja az e-mail címeiket.

> **Házi feladatod**: Az éppen elkészített alkalmazás jó kezdés, de tovább fejleszthető. Az e-mail funkcióval az oktatók manuálisan tudnak csak e-maileket küldeni a diákoknak, be kell gépelniük az e-mail címeket. Tudsz használni a Copilotot arra, hogy létrehozz egy automatizálást, amely lehetővé teszi az oktatók számára, hogy automatikusan küldjenek e-maileket a diákoknak, amikor leadják a beadandóikat? A tipp: a megfelelő utasítással a Copilotot a Power Automate-ban használhatod ehhez.

### Számlainformációs tábla létrehozása a startupunk számára

A startup pénzügyi csapata nehezen tartja nyilván a számlákat. Egy táblázatot használnak a számlák követésére, de ez egyre nehezebben kezelhető a számlák számának növekedésével. Megkértek, hogy hozzon létre egy táblázatot, amely segíti őket a beérkezett számlák adatainak tárolásában, követésében és kezelésében. A táblázatot automatizálás létrehozására kell használni, amely kinyeri az összes számlainformációt és tárolja azt a táblázatban. A táblázatnak azt is lehetővé kell tennie, hogy a pénzügyi csapat megtekinthesse a kifizetett és a még ki nem fizetett számlákat.

A Power Platform alatt egy adatformátum platform, a Dataverse áll, amely lehetővé teszi az alkalmazások és megoldások adatainak tárolását. A Dataverse egy alacsony-kódolású adatplatform az alkalmazás adatainak tárolására. Egy teljesen felügyelt szolgáltatás, amely biztonságosan tárolja az adatokat a Microsoft Cloudban, és a Power Platform környezetében kerül beállításra. Beépített adatkezelési funkciókat kínál, mint például az adat-osztályozás, adatvonal, finomhangolt hozzáférés-szabályozás és sok más. További információt talál [a Dataverse-ről itt](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Miért használjuk a Dataverse-t a startupunknál? A Dataverse standard és egyedi táblái biztonságos, felhőalapú tárolási lehetőséget kínálnak az adataink számára. A táblák lehetővé teszik különböző adatfajták tárolását, hasonlóan ahhoz, mint amikor több munkalapot használ egy Excel munkafüzetben. A táblák segítenek az adott szervezet vagy üzleti igények szerinti adatok tárolásában. Néhány előny, amit a startupunk nyer a Dataverse használatával, többek között:

- **Könnyen kezelhető**: Mind a metaadatok, mind az adatok a felhőben tárolódnak, így nem kell aggódnia azok tárolási vagy kezelési részletei miatt. Az alkalmazások és megoldások építésére koncentrálhat.

- **Biztonságos**: A Dataverse egy biztonságos, felhőalapú tárolási lehetőséget kínál az adataidnak. Szabályozhatod, hogy ki férhet hozzá a táblákban lévő adatokhoz, és hogyan férnek hozzá, szerepalapú biztonságot használva.

- **Gazdag metaadatok**: Az adattípusok és kapcsolatok közvetlenül használhatók a Power Apps-en belül.

- **Logika és érvényesítés**: Üzleti szabályokat, számított mezőket és érvényesítési szabályokat használhat az üzleti logika érvényesítésére és az adatok pontosságának fenntartására.

Most, hogy tudja, mi az a Dataverse és miért érdemes használni, nézzük meg, hogyan használhatja a Copilotot egy Dataverse tábla létrehozásához, amely megfelel a pénzügyi csapat igényeinek.

> **Megjegyzés**: A táblát a következő részben fogja használni arra, hogy automatizálást építsen, amely kinyeri az összes számlainformációt és tárolja azokat a táblázatban.

Egy Dataverse tábla létrehozásához a Copilot segítségével, kövesse az alábbi lépéseket:

1. Lépjen a [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) kezdőképernyőjére.

2. A bal oldali navigációs sávon válassza ki a **Tables** lehetőséget, majd kattintson a **Describe the new Table** gombra.

![Select new table](../../../translated_images/hu/describe-new-table.0792373eb757281e.webp)

1. A **Describe the new Table** képernyőn használja a szövegmezőt, hogy leírja, milyen táblát szeretne létrehozni. Például: **_Szeretnék egy táblát létrehozni a számlainformációk tárolására_**. Kattintson a **Send** gombra az utasítás elküldéséhez az AI Copilotnak.

![Describe the table](../../../translated_images/hu/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. Az AI Copilot javasolni fog egy Dataverse táblát a szükséges mezőkkel az adatok tárolásához és egy mintapéldányt. Ezután testreszabhatja a táblát az igényeinek megfelelően az AI Copilot asszisztens funkcióját használva, párbeszédes lépésekben.

![Suggested Dataverse table](../../../translated_images/hu/copilot-dataverse-table.b3bc936091324d9d.webp)

1. A pénzügyi csapat szeretne egy e-mailt küldeni a beszállítónak, hogy tájékoztassa a számla aktuális állapotáról. A Copilot segítségével hozzáadhat egy új mezőt a táblához a beszállító e-mail címének tárolására. Például a következő utasítással adhat új oszlopot a táblához: **_Szeretnék egy oszlopot hozzáadni a beszállító e-mail címének tárolására_**. Kattintson a **Send** gombra az utasítás elküldéséhez az AI Copilotnak.

1. Az AI Copilot létrehoz egy új mezőt, amelyet aztán testreszabhat az igényeinek megfelelően.

1. Miután befejezte a táblázatot, kattintson a **Create** gombra a tábla létrehozásához.

## AI modellek a Power Platformon AI Builderrel

Az AI Builder egy alacsony-kódolású AI képesség a Power Platformban, amely lehetővé teszi, hogy AI modelleket használjon folyamatok automatizálására és eredmények előrejelzésére. Az AI Builderrel AI-t hozhat be az alkalmazásaiba és folyamaiba, amelyek csatlakoznak az adataihoz a Dataverse-ben vagy más felhőalapú adatforrásokban, például SharePointban, OneDrive-ban vagy Azure-ban.

## Előre elkészített AI modellek vs egyedi AI modellek

Az AI Builder két típust kínál: előre elkészített AI modellek és egyéni AI modellek. Az előre elkészített AI modelleket a Microsoft képezi ki, és készen állnak a használatra a Power Platformban. Ezek segítenek intelligenciát adni az alkalmazásokhoz és a folyamatokhoz anélkül, hogy adatot kellene gyűjteni és saját modellt kellene építeni, tanítani és közzétenni. Ezeket a modelleket használhatja folyamatok automatizálására és eredmények előrejelzésére.

Néhány előre elkészített AI modell a Power Platformban:

- **Kulcsszó kinyerés**: Ez a modell kulcsszavakat emel ki a szövegből.
- **Nyelvfelismerés**: Ez a modell felismeri a szöveg nyelvét.
- **Hangulatelemzés**: Ez a modell pozitív, negatív, semleges vagy vegyes hangulatot ismer fel a szövegben.
- **Névjegykártya beolvasó**: Ez a modell információkat nyer ki névjegykártyákból.
- **Szövegfelismerés**: Ez a modell szöveget emel ki képekből.
- **Objektumfelismerés**: Ez a modell tárgyakat ismer fel és emel ki képekből.
- **Dokumentumfeldolgozás**: Ez a modell űrlapokból nyer ki információkat.
- **Számlafeldolgozás**: Ez a modell számlákból nyer ki információkat.

Egyéni AI modellekkel saját modellt hozhat be az AI Builderbe, amely úgy működik, mint bármely egyéni modell az AI Builderben, és lehetővé teszi a modell az adatokkal való tanítását. Ezeket a modelleket használhatja folyamatok automatizálására és eredmények előrejelzésére mind Power Apps-ben, mind Power Automate-ban. A saját modell használatakor bizonyos korlátok vonatkoznak. További információért olvassa el a [korlátozásokat](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/hu/ai-builder-models.8069423b84cfc47f.webp)

## 2. feladat – Számlafeldolgozási folyamat létrehozása a startupunk számára

A pénzügyi csapat nehezen tudja feldolgozni a számlákat. Egy táblázatot használnak a követésükre, de ez egyre kezelhetetlenebb lett a számlák számának növekedésével. Kérték, hogy hozzon létre egy munkafolyamatot, amely segít nekik a számlák feldolgozásában AI segítségével. A munkafolyamatnak képesnek kell lennie a számlákból információ kinyerésére és ezek tárolására egy Dataverse táblában. A munkafolyamatnak azt is lehetővé kell tennie, hogy e-mailt küldjenek a pénzügyi csapatnak a kinyert információkkal.

Most, hogy tudja, mi az az AI Builder és miért érdemes használni, nézzük meg, hogyan használhatja az előzőleg megismert Számlafeldolgozó AI modellt az AI Builderben egy munkafolyamat létrehozására, amely segíti a pénzügyi csapatot a számlák feldolgozásában.

Ahhoz, hogy egy munkafolyamatot hozzon létre, amely segíti a pénzügyi csapatot a számlák feldolgozásában a Számlafeldolgozó AI modell használatával az AI Builderben, kövesse az alábbi lépéseket:

1. Lépjen a [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) kezdőképernyőjére.

2. Használja a szövegmezőt a kezdőképernyőn a munkafolyamat leírásához. Például: **_Számla feldolgozása, amikor megérkezik a postafiókomba_**. Kattintson a **Send** gombra az utasítás elküldéséhez az AI Copilotnak.

   ![Copilot power automate](../../../translated_images/hu/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. Az AI Copilot javaslatot tesz a szükséges műveletekre a feladat automatizálásához. Kattintson a **Next** gombra a további lépések megtekintéséhez.

4. A következő lépésben a Power Automate felszólítja a munkafolyamat kapcsolatok beállítására. Miután elkészült, kattintson a **Create flow** gombra a munkafolyamat létrehozásához.

5. Az AI Copilot létrehoz egy munkafolyamatot, amelyet aztán testreszabhat az igényeinek megfelelően.

6. Frissítse a munkafolyamat triggerét, és állítsa be a **Folder** mezőt arra a mappára, ahol a számlákat tárolni fogják. Például állítsa be az **Inbox** mappára. Kattintson a **Show advanced options** gombra, és állítsa be az **Only with Attachments** opciót **Yes** értékre. Ez biztosítja, hogy a folyamat csak akkor fusson, amikor a mappába egy csatolt fájlokat tartalmazó e-mail érkezik.

7. Távolítsa el az alábbi műveleteket a munkafolyamatból: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** és **Compose 4**, mivel ezekre nem lesz szükség.

8. Távolítsa el a **Condition** műveletet is, mert ezt sem fogja használni. Így kell kinéznie:

   ![power automate, remove actions](../../../translated_images/hu/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Kattintson az **Add an action** gombra, keressen rá a **Dataverse**-re, és válassza az **Add a new row** műveletet.

10. Az **Extract Information from invoices** műveletnél állítsa be a **Invoice File**-t úgy, hogy az az e-mail csatolmány tartalmára (**Attachment Content**) mutasson. Ez biztosítja, hogy a folyamat a számla csatolmányából kinyerje az információkat.

11. Válassza ki az előbb létrehozott **Table**-t. Például választhatja a **Invoice Information** táblát. Válassza ki az előző művelet dinamikus tartalmát az alábbi mezők feltöltéséhez:

    - ID
    - Amount
    - Date
    - Name
    - Status - Állítsa a **Status** mezőt **Pending**-re.
    - Supplier Email - Használja a **From** dinamikus tartalmat a **When a new email arrives** triggerből.

    ![power automate add row](../../../translated_images/hu/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Miután elkészült a munkafolyamattal, kattintson a **Save** gombra a mentéshez. Ezután kipróbálhatja a munkafolyamatot, ha egy számlát tartalmazó e-mailt küld a triggerben megadott mappába.

> **Házi feladatod**: Az éppen elkészített munkafolyamat jó kezdés, most gondolkodjon el, hogyan készíthet olyan automatizálást, amely lehetővé teszi a pénzügyi csapatnak, hogy e-mailt küldjenek a beszállítónak tájékoztatásul a számla aktuális állapotáról. Tipp: a munkafolyamatnak akkor kell futnia, amikor a számla állapota megváltozik.

## Szöveg generálás AI modell használata a Power Automate-ban

Az AI Builderben a Create Text with GPT AI modell lehetővé teszi, hogy prompt alapján szöveget generáljon, és a Microsoft Azure OpenAI Service működteti. Ezzel a képességgel GPT (Generative Pre-Trained Transformer) technológiát építhet be az alkalmazásaiba és munkafolyamataiba, hogy különféle automatizált munkafolyamatokat és ügyes alkalmazásokat hozzon létre.

A GPT modelleket hatalmas adatmennyiségen képezik, ami lehetővé teszi, hogy prompt alapján nagyon hasonló, emberi nyelvet imitáló szöveget állítsanak elő. A munkafolyamat-automatizálással integrálva az ilyen AI modelleket kihasználhatják sokféle feladat egyszerűsítésére és automatizálására.

Például olyan munkafolyamatokat építhet, amelyek automatikusan generálnak szöveget sokféle esetre, mint például e-mail tervezetek, termékleírások és még sok más. A modellt különféle alkalmazásokban is használhatja, például chatbotokban vagy ügyfélszolgálati alkalmazásokban, amelyek lehetővé teszik az ügyfélszolgálati munkatársak számára, hogy hatékonyan és gyorsan válaszoljanak az ügyfelek kérdéseire.

![create a prompt](../../../translated_images/hu/create-prompt-gpt.69d429300c2e870a.webp)


Ha meg szeretné tanulni, hogyan használja ezt a MI modellt a Power Automatében, tekintse át a [Add intelligence with AI Builder and GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) modult.

## Nagyszerű munka! Folytassa a tanulást

A lecke elvégzése után nézze meg a [Generatív MI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív MI ismereteit!

Szeretné személyre szabni és többet kihozni a Copilotból? Fedezze fel az [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) gyűjteményt — egy közösség által összeállított utasításokat, ügynököket, képességeket és konfigurációkat tartalmazó csomagot, amely segít a GitHub Copilot maximális kihasználásában.

Lépjen tovább a 11. leckébe, ahol megnézzük, hogyan lehet [integrálni a generatív MI-t a Function Calling segítségével](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->