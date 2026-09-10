# Generatív AI-vel működő csevegőalkalmazások építése

[![Generatív AI-vel működő csevegőalkalmazások építése](../../../translated_images/hu/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(A fenti képre kattintva megtekintheti az óra videóját)_

Most, hogy láttuk, hogyan építhetünk szöveggeneráló alkalmazásokat, nézzük meg a csevegőalkalmazásokat.

A csevegőalkalmazások beépültek a mindennapi életünkbe, nem csupán alkalmi kommunikáció eszközei. Fontos részei az ügyfélszolgálatnak, műszaki támogatásnak, sőt, kifinomult tanácsadó rendszereknek is. Valószínűleg nemrégiben egy csevegőalkalmazástól kaptál segítséget. Ahogy egyre fejlettebb technológiákat, például generatív AI-t integrálunk ezekbe a platformokba, nő a komplexitás és a kihívások száma is.

Néhány kérdés, amire választ kell adnunk:

- **Az alkalmazás építése**. Hogyan építsük hatékonyan és zökkenőmentesen ezeket az AI-alapú alkalmazásokat specifikus felhasználási esetekhez?
- **Felügyelet**. A telepítés után hogyan tudjuk figyelemmel kísérni és biztosítani, hogy az alkalmazások a legmagasabb minőségi szinten működjenek, mind a funkcionális, mind a felelős AI hat alapelvének betartása szempontjából? [six principles of responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)

Ahogy egyre inkább az automatizáció és az ember-gép interakciók zökkenőmentes kora felé haladunk, alapvető fontosságú megérteni, hogy a generatív AI hogyan alakítja át a csevegőalkalmazások hatókörét, mélységét és alkalmazkodóképességét. Ez az óra megvizsgálja azokat a szerkezeti aspektusokat, amelyek támogatják ezeket az összetett rendszereket, bemutatja a domain-specifikus finomhangolás módszereit, és értékeli azokat a mérőszámokat és szempontokat, amelyek a felelős AI alkalmazáshoz szükségesek.

## Bevezetés

Ez az óra a következőket fedi le:

- Technikák a csevegőalkalmazások hatékony építéséhez és integrálásához.
- Hogyan alkalmazzuk a testreszabást és finomhangolást az alkalmazásoknál.
- Stratégiák és szempontok a csevegőalkalmazások hatékony felügyeletéhez.

## Tanulási célok

Az óra végére képes leszel:

- Leírni a csevegőalkalmazások építésének és meglévő rendszerekbe való integrálásának szempontjait.
- Testreszabni a csevegőalkalmazásokat specifikus felhasználási esetekhez.
- Azonosítani a kulcsfontosságú mérőszámokat és szempontokat az AI-alapú csevegőalkalmazások minőségének hatékony felügyeletéhez és fenntartásához.
- Biztosítani, hogy a csevegőalkalmazások felelősen használják az AI-t.

## Generatív AI integrálása csevegőalkalmazásokba

A generatív AI-val történő emelése a csevegőalkalmazásoknak nem csupán azt jelenti, hogy okosabbá tesszük őket; az architektúra, a teljesítmény és a felhasználói felület optimalizálásáról is szól, hogy minőségi felhasználói élményt nyújtsunk. Ez magában foglalja az architekturális alapok, az API integrációk és a felhasználói felületi szempontok vizsgálatát. Ez a rész átfogó iránymutatást kínál ezeknek az összetett területeknek a kezeléséhez, akár meglévő rendszerekbe csatlakoztatod, akár önálló platformként építed őket.

Ennek a szakasznak a végére képes leszel hatékonyan felépíteni és integrálni csevegőalkalmazásokat.

### Chatbot vagy csevegőalkalmazás?

Mielőtt belevágnánk a csevegőalkalmazások építésébe, hasonlítsuk össze a 'chatbotokat' és az 'AI-alapú csevegőalkalmazásokat', amelyek különböző szerepeket és funkciókat töltenek be. Egy chatbot fő célja, hogy automatizáljon specifikus beszélgetési feladatokat, mint például a gyakran ismételt kérdések megválaszolása vagy egy csomag nyomon követése. Általában szabályalapú logika vagy összetett AI algoritmusok alapján működik. Ezzel szemben az AI-alapú csevegőalkalmazás egy jóval tágabb környezet, amely különféle digitális kommunikációs formákat támogat, mint szöveges, hang- és videócsevegés emberi felhasználók között. Fő jellemzője egy generatív AI modell integrálása, amely árnyalt, emberi jellegű beszélgetéseket szimulál, válaszokat generálva sokféle bemenet és kontextuális jel alapján. Egy generatív AI-val működő csevegőalkalmazás képes nyílt témájú beszélgetésekre, alkalmazkodik a folyamatosan változó beszélgetési kontextushoz, sőt kreatív vagy összetett párbeszédeket is előállít.

Az alábbi táblázat vázolja a fő különbségeket és hasonlóságokat, hogy segítsen megérteni egyedi szerepüket a digitális kommunikációban.

| Chatbot                               | Generatív AI-vel működő csevegőalkalmazás |
| ------------------------------------- | ---------------------------------------- |
| Feladatra fókuszált és szabályalapú   | Kontextusérzékeny                        |
| Gyakran integrált nagyobb rendszerekbe | Egy vagy több chatbot otthont adhat       |
| Csak előre programozott funkciókra korlátozódik | Generatív AI modelleket használ            |
| Specializált és struktúrált interakciók | Képes nyílt témájú beszélgetésekre         |

### Előre elkészített funkciók kihasználása SDK-kkal és API-kkal

Egy csevegőalkalmazás építésénél az első nagyszerű lépés az elérhető lehetőségek felmérése. SDK-k és API-k használata csevegőalkalmazások építéséhez előnyös stratégia számos okból. A jól dokumentált SDK-k és API-k integrálásával stratégiailag pozícionálod az alkalmazásodat a hosszú távú siker érdekében, megoldva a skálázhatóság és a karbantartás kérdéseit.

- **Gyorsítja a fejlesztési folyamatot és csökkenti a terheket**: Az előre elkészített funkciókra támaszkodva a drága saját fejlesztési folyamat helyett más, fontosabb alkalmazásrészekre koncentrálhatsz, például az üzleti logikára.
- **Jobb teljesítmény**: Ha saját magad építed a funkciókat, előbb-utóbb felteszed magadnak a kérdést: "Hogyan skálázódik? Képes ez az alkalmazás hirtelen nagy felhasználószámot kezelni?" A jól karbantartott SDK-k és API-k gyakran beépített megoldásokat kínálnak ezekre a problémákra.
- **Könnyebb karbantartás**: A frissítések és fejlesztések egyszerűbben kezelhetők, mivel a legtöbb API és SDK esetében csak egy könyvtár frissítése szükséges, amikor új verzió jelenik meg.
- **Hozzáférés a legkorszerűbb technológiához**: Olyan modellek használata, amelyeket finomhangoltak és kiterjedt adatkészleteken tanítottak, természetes nyelvi képességekkel ruházza fel az alkalmazást.

Az SDK vagy API funkcióinak elérése általában a szolgáltatások használatára vonatkozó engedély megszerzését jelenti, ami gyakran egyedi kulcs vagy hitelesítő token használatán keresztül történik. Az OpenAI Python könyvtár segítségével vizsgáljuk meg, hogyan néz ez ki. Az alábbi [OpenAI jegyzetfüzetben](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) vagy az [Azure OpenAI Szolgáltatások jegyzetfüzetben](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) is kipróbálhatod ezt az órán.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

A fenti példa a GPT-5 mini modellt használja a Responses API-val a prompt kitöltéséhez, de vedd észre, hogy az API kulcsot előtte állítjuk be. Hibaüzenetet kapnál, ha nem állítanád be a kulcsot.

## Felhasználói élmény (UX)

Általános UX elvek érvényesek a csevegőalkalmazásokra, de íme néhány további szempont, amelyek különösen fontossá válnak a gépi tanulási összetevők miatt.

- **Ambiguitás kezelési mechanizmus**: A generatív AI modellek időnként kétértelmű válaszokat adnak. Egy olyan funkció, amely lehetővé teszi a felhasználók számára a tisztázás kérést, hasznos lehet, ha ilyen problémába ütköznek.
- **Kontextus megőrzése**: A fejlett generatív AI modellek képesek emlékezni a beszélgetés kontextusára, ami szükséges lehet a felhasználói élményhez. Ha a felhasználók irányíthatják és kezelhetik a kontextust, az javítja az élményt, de növeli az érzékeny adatok megőrzésének kockázatát. Érdemes megfontolni, meddig tároljuk ezeket az adatokat, például egy megőrzési szabályzat bevezetésével, amely kiegyensúlyozza a kontextus szükségességét a magánszféra védelmével.
- **Személyre szabás**: Az AI modellek tanulási és alkalmazkodási képessége révén személyre szabott élményt kínálnak a felhasználónak. A felhasználói profilokhoz hasonló funkciókon keresztül testre szabott élmény nemcsak azt a benyomást kelti, hogy a felhasználót megértik, hanem segíti is specifikus válaszok megtalálását, hatékonyabbá és kielégítőbbé téve a beszélgetést.

Egy ilyen személyre szabásra példa az OpenAI ChatGPT „Egyéni utasítások” beállítása. Megadhatod magadról azokat az információkat, amelyek fontos kontextust szolgáltathatnak a promptjaidhoz. Íme egy példa egy egyéni utasításra.

![Egyéni utasítások beállítása a ChatGPT-ben](../../../translated_images/hu/custom-instructions.b96f59aa69356fcf.webp)

Ez a „profil” arra készteti a ChatGPT-t, hogy egy oktatási tervet készítsen a láncolt listákról. Vegyük észre, hogy a ChatGPT figyelembe veszi, hogy a felhasználó tapasztalata alapján mélyebb oktatási tervet szeretne.

![Prompt a ChatGPT-ben egy láncolt listákról szóló oktatási tervhez](../../../translated_images/hu/lesson-plan-prompt.cc47c488cf1343df.webp)

### A Microsoft rendszerüzenet keretrendszere nagy nyelvi modellekhez

[A Microsoft útmutatást nyújtott](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) hatékony rendszerüzenetek írásához, amikor LLM-ekből generálnak válaszokat, 4 területre bontva:

1. A modell célcsoportjának, képességeinek és korlátainak meghatározása.
2. A modell kimeneti formátumának definiálása.
3. Konkrét példák biztosítása, amelyek bemutatják a modell szándékolt viselkedését.
4. További viselkedési szabályok megadása.

### Akadálymentesség

Legyen a felhasználó vizuális, hallási, mozgás- vagy kognitív fogyatékossággal élő, egy jól megtervezett csevegőalkalmazásnak mindenkinek használhatónak kell lennie. Az alábbi lista konkrét funkciókat bont le, amelyek célja a hozzáférhetőség javítása különféle fogyatékosságok esetén.

- **Vizuális fogyatékosság esetére**: Magas kontrasztú témák és átméretezhető szöveg, képernyőolvasó kompatibilitás.
- **Hallási fogyatékosság esetére**: Szöveg-beszéd és beszéd-szöveg funkciók, vizuális jelek audio értesítésekhez.
- **Mozgáskorlátozottság esetére**: Billentyűzetes navigáció támogatása, hangvezérlés.
- **Kognitív fogyatékosság esetére**: Egyszerűsített nyelvi opciók.

## Testreszabás és finomhangolás domain-specifikus nyelvi modellekhez

Képzelj el egy csevegőalkalmazást, amely érti a céged zsargonját, és előre látja a felhasználói bázis gyakori kérdéseit. Néhány megközelítés érdemes megemlíteni:

- **DSL modellek kihasználása**. A DSL domain-specifikus nyelvet jelent. Használhatsz úgynevezett DSL modellt, amely egy adott területen tanult, hogy megértse annak fogalmait és helyzeteit.
- **Finomhangolás alkalmazása**. A finomhangolás a modell további, specifikus adatokkal való tanítása.

## Testreszabás: DSL használata

A domain-specifikus nyelvi modellek (DSL modellek) használata növelheti a felhasználók elkötelezettségét, mivel specializált, kontextuálisan releváns interakciókat biztosítanak. Olyan modellről van szó, amelyet kifejezetten egy adott szakterület, iparág vagy téma megértésére és szöveg generálására képztek vagy finomhangoltak. A DSL modell használati lehetőségei változóak: lehet nulláról képezni, vagy előre létezőket használni SDK-kon és API-kon keresztül. Egy másik lehetőség a finomhangolás, amely során egy meglévő előre kiképzett modellt adaptálnak egy adott területre.

## Testreszabás: finomhangolás alkalmazása

A finomhangolást általában akkor veszik fontolóra, ha egy előre kiképzett modell nem elég jó egy specializált területen vagy adott feladatban.

Például az orvosi kérdések összetettek és sok kontextust igényelnek. Amikor egy orvos diagnózist állít fel, azt különböző tényezők, mint az életmód vagy meglévő betegségek alapján teszi, és esetleg a legfrissebb orvosi szakfolyóiratokkal igazolja. Ilyen finom helyzetekben egy általános AI csevegőalkalmazás nem lehet megbízható forrás.

### Például: egy orvosi alkalmazás

Képzelj el egy csevegőalkalmazást, amely orvosi szakembereknek nyújt gyors hivatkozási pontokat a kezelési irányelvekhez, gyógyszer-kölcsönhatásokhoz vagy legfrissebb kutatási eredményekhez.

Egy általános modell elegendő lehet alapvető orvosi kérdések megválaszolásához vagy általános tanácsadásra, de nehézségekbe ütközhet az alábbi helyzetekben:

- **Nagyon specifikus vagy összetett esetek**. Például egy neurológus megkérdezheti az alkalmazást: „Mik a jelenlegi legjobb gyakorlatok a gyógyszerrezisztens epilepszia kezelésére gyerekeknél?”
- **Hiányoznak a legújabb fejlesztések**. Egy általános modell nehezebben adhat naprakész választ, amely magában foglalja a legutóbbi neurológiai és farmakológiai előrelépéseket.

Ilyen esetekben a modell finomhangolása egy speciális orvosi adattal jelentősen javíthatja a kérdések pontosabb és megbízhatóbb kezelését. Ehhez nagy és releváns adatgyűjtemény szükséges, amely a domain-specifikus kihívásokat és kérdéseket reprezentálja, amelyeket meg kell oldani.

## Szempontok a magas minőségű AI-alapú csevegőélményhez

Ez a rész leírja a „magas minőségű” csevegőalkalmazások kritériumait, amelyek között szerepelnek az intézkedhető mérőszámok rögzítése és egy olyan keretrendszer követése, amely felelősen használja az AI technológiát.

### Kulcsfontosságú mérőszámok

Ahhoz, hogy egy alkalmazás megbízhatóan magas teljesítményt nyújtson, elengedhetetlen a kulcsfontosságú mérőszámok és szempontok nyomon követése. Ezek a mérések nemcsak az alkalmazás működését biztosítják, hanem értékelik az AI modell és a felhasználói élmény minőségét is. Az alábbiakban felsorolunk alap-, AI- és felhasználói élményhez kapcsolódó mérőszámokat, amelyeket érdemes figyelembe venni.

| Mérőszám                      | Meghatározás                                                                                                              | Szempontok a csevegőfejlesztő számára                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Rendelkezésre állás (Uptime)** | Az idő, ameddig az alkalmazás működőképes és elérhető a felhasználók számára.                                               | Hogyan minimalizálod a leállásokat?                              |
| **Válaszidő**                 | Az az idő, amely alatt az alkalmazás válaszol a felhasználó lekérdezésére.                                                   | Hogyan optimalizálod a lekérdezések feldolgozását a gyorsabb válaszhoz? |
| **Precizitás (Precision)**    | A valódi pozitív találatok aránya az összes pozitív találathoz viszonyítva.                                                | Hogyan validálod a modell precizitását?                          |
| **Visszahívás (Recall, érzékenység)** | A valódi pozitív találatok aránya a tényleges pozitív esetekhez képest.                                                    | Hogyan méred és javítod a visszahívást?                          |
| **F1 pontszám**               | A precizitás és visszahívás harmonikus átlaga, amely kiegyensúlyozza a kettő közötti kompromisszumot.                        | Mi a célzott F1 pontszámod? Hogyan egyensúlyozod a precizitást és a visszahívást? |
| **Zavaró tényező (Perplexity)** | Azt méri, mennyire illeszkedik a modell által jósolt valószínűségi eloszlás az adatok tényleges eloszlásához.                     | Hogyan minimalizálod a perplexity-t?                             |
| **Felhasználói elégedettségi mérőszámok** | A felhasználó észlelését méri az alkalmazásról. Gyakran felmérésekből származik.                                              | Milyen gyakran gyűjtesz visszajelzést? Hogyan alkalmazkodsz ehhez? |
| **Hibaarány**                | A modell hibáinak aránya az értelmezés vagy a kimenet során.                                                                 | Milyen stratégiáid vannak a hibaarány csökkentésére?             |
| **Újraképzési ciklusok**     | Milyen gyakran frissítik a modellt új adatok és ismeretek integrálására.                                                     | Milyen gyakran újraképezed a modellt? Mi indítja el az újraképzési ciklust? |

| **Anomália-észlelés**         | Olyan eszközök és technikák, amelyek szokatlan mintákat azonosítanak, amelyek nem felelnek meg a várható viselkedésnek.                        | Hogyan reagálsz az anomáliákra?                                        |

### Felelős MI-gyakorlatok megvalósítása csevegőalkalmazásokban

A Microsoft felelős MI-hez való megközelítése hat olyan elvet határozott meg, amelyeknek irányítaniuk kell az MI fejlesztését és használatát. Az alábbiakban az elveket, meghatározásukat, valamint azokat a szempontokat találja, amelyeket egy csevegő fejlesztőnek figyelembe kell vennie, és hogy miért fontos komolyan venni azokat.

| Elvek             | A Microsoft meghatározása                                | Szempontok csevegő fejlesztők számára                                      | Miért fontos                                                                       |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Méltányosság               | Az MI rendszereknek minden embert méltányosan kell kezelniük.            | Biztosítsa, hogy a csevegőalkalmazás ne diszkrimináljon a felhasználói adatok alapján.  | A felhasználók közötti bizalom és befogadás kiépítéséhez; jogi következmények elkerülése érdekében.                |
| Megbízhatóság és biztonság | Az MI rendszereknek megbízhatóan és biztonságosan kell működniük.        | Vezessen be tesztelést és védelmi mechanizmusokat a hibák és kockázatok minimalizálására.         | Biztosítja a felhasználói elégedettséget és megelőzi az esetleges károkat.                                 |
| Adatvédelem és biztonság   | Az MI rendszereknek biztonságosnak kell lenniük és tiszteletben kell tartaniuk a magánéletet.      | Erős titkosítást és adatvédelmi intézkedéseket kell bevezetni.              | Az érzékeny felhasználói adatok védelméhez és az adatvédelmi törvények betartásához.                         |
| Befogadás          | Az MI rendszereknek mindenkit fel kell hatalmazniuk, és bevonniuk az embereket. | Olyan UI/UX tervezése, amely hozzáférhető és könnyen használható különféle közönségek számára. | Biztosítja, hogy szélesebb felhasználói kör hatékonyan használhassa az alkalmazást.                   |
| Átláthatóság           | Az MI rendszereknek érthetőknek kell lenniük.                  | Biztosítson világos dokumentációt és indoklást az MI válaszokhoz.            | A felhasználók nagyobb valószínűséggel bíznak egy rendszerben, ha megértik, hogyan születnek a döntések. |
| Felelősségvállalás         | Az embereknek vállalniuk kell a felelősséget az MI rendszerekért.          | Hozzon létre egyértelmű folyamatot az MI döntések auditálására és fejlesztésére.     | Lehetővé teszi a folyamatos fejlesztést és a javító intézkedéseket hiba esetén.               |

## Feladat

Nézze meg a [feladatot](../../../07-building-chat-applications/python). Ez végigvezeti Önt egy sor gyakorlaton, az első csevegési parancsok futtatásától a szövegek osztályozásán és összefoglalásán át még sok másig. Vegye észre, hogy a feladatok különböző programozási nyelveken is elérhetők!

## Remek munka! Folytassa az utazást

A lecke befejezése után tekintse meg a [Generatív MI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív MI-ismereteit!

Lépjen tovább a 8. leckére, hogy megnézze, hogyan kezdhet el [keresőalkalmazásokat építeni](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->