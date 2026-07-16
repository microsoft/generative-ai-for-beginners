# Generatív mesterséges intelligencia által vezérelt csevegőalkalmazások építése

[![Generatív mesterséges intelligencia által vezérelt csevegőalkalmazások építése](../../../translated_images/hu/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

Most, hogy láttuk, hogyan építhetünk szövegalkotó alkalmazásokat, nézzük meg a csevegőalkalmazásokat.

A csevegőalkalmazások beépültek mindennapjainkba, nem csak alkalmi beszélgetések eszközeként. A vevőszolgálat, technikai támogatás és még kifinomult tanácsadó rendszerek elengedhetetlen részei. Valószínű, hogy nemrégiben egy csevegőalkalmazástól kaptál segítséget. Ahogy egyre fejlettebb technológiákat, például generatív mesterséges intelligenciát integrálunk ezekbe a platformokba, nő a komplexitás, és vele együtt a kihívások is.

Néhány kérdés, amelyre meg kell találnunk a választ:

- **Az alkalmazás építése**. Hogyan építsük meg hatékonyan és integráljuk zökkenőmentesen ezeket a mesterséges intelligenciával működő alkalmazásokat specifikus esetekhez?
- **Figyelés**. Az alkalmazás telepítése után hogyan monitorozhatjuk és biztosíthatjuk, hogy az alkalmazások a legmagasabb minőségi szinten működnek, mind funkcionalitás, mind a [felelősségteljes AI hat alapelve](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) betartása szempontjából?

Ahogy az automatizáció és a zökkenőmentes ember-gép interakciók korszaka előrehalad, elengedhetetlen megérteni, hogyan alakítja át a generatív AI a csevegőalkalmazások hatókörét, mélységét és alkalmazkodóképességét. Ez a lecke megvizsgálja az olyan architekturális szempontokat, amelyek támogatják ezeket az összetett rendszereket, bemutatja a domain-specifikus feladatokra való finomhangolás módszertanát, valamint értékeli a felelős AI bevezetéshez szükséges mutatókat és megfontolásokat.

## Bevezetés

Ez a lecke lefedi:

- Technikai megközelítéseket a csevegőalkalmazások hatékony építéséhez és integrálásához.
- Hogyan alkalmazzunk testreszabást és finomhangolást az alkalmazásokhoz.
- Stratégiákat és megfontolásokat a csevegőalkalmazások hatékony figyeléséhez.

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni a megfontolandó szempontokat a csevegőalkalmazások meglévő rendszerekbe való beépítéséhez.
- Testreszabni a csevegőalkalmazásokat speciális felhasználási esetekre.
- Azonosítani a kulcsfontosságú mutatókat és megfontolásokat az AI-alapú csevegőalkalmazások minőségének hatékony monitorozásához és fenntartásához.
- Biztosítani, hogy a csevegőalkalmazások felelősségteljesen használják az AI-t.

## Generatív AI integrálása csevegőalkalmazásokba

A generatív AI-val való fejlesztés nem csupán az alkalmazások okosabbá tételéről szól; az architektúra, a teljesítmény és a felhasználói felület optimalizálása is lényeges egy minőségi felhasználói élmény biztosításához. Ez magában foglalja az architekturális alapok, API integrációk és felhasználói felület megfontolásait. Ez a részletes útmutatót nyújt a bonyolult területek átvizsgálásához, akár meglévő rendszerekhez csatlakoztatod őket, akár önálló platformokat építesz.

Ennek a szakasznak a végére meglesz az a tudásod, amely ahhoz szükséges, hogy hatékonyan építs és illessz be csevegőalkalmazásokat.

### Chatbot vagy csevegőalkalmazás?

Mielőtt belekezdenénk a csevegőalkalmazások építésébe, hasonlítsuk össze a 'chatbotokat' és az 'AI-vezérelt csevegőalkalmazásokat', melyek különböző feladatokat és funkciókat látnak el. A chatbot fő célja bizonyos beszélgetési feladatok automatizálása, mint például a gyakran ismételt kérdésekre adott válaszok vagy csomagkövetés. Tipikusan szabályalapú logika vagy összetett AI algoritmusok irányítják. Ezzel szemben az AI-vezérelt csevegőalkalmazás sokkal tágabb környezet, amely különféle digitális kommunikációs formákat támogat, például szöveges, hang- és videócsevegést emberi felhasználók között. Meghatározó jellemzője egy generatív AI modell integrálása, amely árnyalt, emberihez hasonló beszélgetéseket szimulál, válaszokat generálva változatos bemenetek és kontextuális jelek alapján. Egy generatív AI-val működő csevegőalkalmazás képes nyílt témájú beszélgetésekre, alkalmazkodik a változó beszélgetési kontextusokhoz, és kreatív vagy összetett dialógusokat is előállíthat.

Az alábbi táblázat a legfőbb különbségeket és hasonlóságokat foglalja össze, hogy megértsük egyedi szerepüket a digitális kommunikációban.

| Chatbot                               | Generatív AI-val vezérelt csevegőalkalmazás                        |
| ------------------------------------- | -------------------------------------- |
| Feladatorientált és szabályalapú      | Kontextusérzékeny                                                 |
| Gyakran nagyobb rendszerekbe integrálva | Egy vagy több chatbotot is kiszolgálhat                           |
| Csak programozott funkciókra korlátozódik | Generatív AI modelleket is alkalmaz                               |
| Specializált és strukturált interakciók | Nyílt témájú beszélgetésekre képes                               |

### Előre elkészített funkciók kihasználása SDK-kkal és API-kkal

Csevegőalkalmazás építésekor jó kiindulópont felmérni, mi áll már rendelkezésre. SDK-k és API-k használata előnyös stratégia több okból is. A jól dokumentált SDK-k és API-k beillesztésével alkalmazásunkat hosszú távú sikerre pozícionáljuk, kezelve a skálázási és karbantartási szempontokat.

- **Gyorsítja a fejlesztési folyamatot és csökkenti a terheket**: Az előre megépített funkciókra támaszkodás helyett, hogy drágán saját magad építenéd fel őket, az alkalmazásod más fontosabb aspektusaira koncentrálhatsz, például az üzleti logikára.
- **Jobb teljesítmény**: Amikor a funkcionalitást nulláról építed, előbb-utóbb felmerül a kérdés: "Hogyan skálázódik? Képes ez az alkalmazás kezelni a hirtelen felhasználói hullámot?" A jól karbantartott SDK-k és API-k gyakran beépített megoldásokat kínálnak ezen kihívásokra.
- **Könnyebb karbantartás**: A frissítések és fejlesztések kezelése egyszerűbb, mivel a legtöbb API és SDK esetében elegendő egy könyvtár frissítése az új verzió megjelenésekor.
- **Hozzáférés élvonalbeli technológiákhoz**: Finomhangolt, nagy adathalmazokon tanított modellek használatával az alkalmazás természetes nyelvi képességeket szerez.

Egy SDK vagy API funkcionalitásának eléréséhez általában engedély szükséges, amit egyedi kulcs vagy hitelesítő token biztosít. Az OpenAI Python könyvtár segítségével mutatjuk be ezt a folyamatot. Ön is kipróbálhatja a következő [OpenAI jegyzetfüzetben](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) vagy az [Azure OpenAI Services jegyzetfüzetben](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) ehhez a leckéhez.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

A fenti példa a GPT-4o mini modellt használja a Responses API-val a prompt befejezésére, de észreveendő, hogy az API kulcsot előzetesen be kell állítani. Hibát kapnál, ha nem állítanád be a kulcsot.

## Felhasználói élmény (UX)

Általános UX elvek érvényesek a csevegőalkalmazásokra, de itt néhány további megfontolás is fontos lesz a gépi tanulási komponensek miatt.

- **Mechanizmus az egyértelműtlenség kezelésére**: A generatív AI modellek néha kétértelmű válaszokat adnak. Egy olyan funkció, amely engedi a felhasználónak tisztázást kérni, hasznos lehet ilyen esetekben.
- **Kontextus megőrzés**: A fejlett generatív AI modellek képesek megjegyezni a beszélgetés kontextusát, ami lényeges lehet a felhasználói élményhez. Ha a felhasználók kézben tarthatják és kezelhetik a kontextust, az javítja az élményt, ám magában hordozza a kockázatot, hogy érzékeny információk tárolódnak. Fontos megfontolni a tárolás időtartamát, például visszatartási szabályzat bevezetésével, így kiegyensúlyozva a kontextus szükségességét a magánélettel.
- **Személyre szabás**: Az AI modellek tanulási és alkalmazkodási képessége személyre szabott élményt nyújt. A felhasználói profilokkal történő testreszabás nemcsak azt a benyomást kelti, hogy a felhasználót megértik, hanem segíti a specifikus válaszok megtalálását, hatékonyabbá és kielégítőbbé téve az interakciót.

Egy ilyen személyre szabás példája az OpenAI ChatGPT "Egyéni utasítások" beállítása. Ez lehetőséget ad arra, hogy magadról olyan információkat adj meg, amelyek fontos kontextusok lehetnek a promptjaid számára. Íme egy példa egy egyéni utasításra.

![Egyéni utasítások beállítása a ChatGPT-ben](../../../translated_images/hu/custom-instructions.b96f59aa69356fcf.webp)

Ez a "profil" arra ösztönzi a ChatGPT-t, hogy egy tananyagtervet készítsen a láncolt listákról. Észrevehető, hogy a ChatGPT figyelembe veszi a felhasználó tapasztalata alapján a mélyebb tananyagot.

![Prompt a ChatGPT-ben láncolt listák témájú tananyagtervhez](../../../translated_images/hu/lesson-plan-prompt.cc47c488cf1343df.webp)

### A Microsoft nagy nyelvi modellekhez készült Rendszerüzenet-keretrendszere

[A Microsoft útmutatót nyújtott](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) hatékony rendszerüzenetek írásához LLM-ekből történő válaszgeneráláshoz, négy területre bontva:

1. A modell célközönségének, képességeinek és korlátainak meghatározása.
2. A modell kimeneti formátumának definiálása.
3. Konkrét példák biztosítása, amelyek bemutatják a modell kívánt viselkedését.
4. További viselkedési védőintézkedések biztosítása.

### Akadálymentesség

Függetlenül attól, hogy a felhasználó látási, hallási, mozgásbeli vagy kognitív sérüléssel él-e, egy jól megtervezett csevegőalkalmazásnak mindenki számára használhatónak kell lennie. Az alábbi lista konkrét funkciókat sorol fel, amelyek különféle felhasználói korlátozásokhoz segítik elő az akadálymentességet.

- **Látássérülteknek szánt funkciók**: Magas kontrasztú témák és méretezhető szöveg, képernyőolvasó kompatibilitás.
- **Hallássérülteknek szánt funkciók**: Szöveg-beszéd és beszéd-szöveg funkciók, vizuális jelzések hangértesítésekhez.
- **Mozgáskorlátozottaknak szánt funkciók**: Billentyűzetes navigáció támogatása, hangalapú parancsok.
- **Kognitív sérüléssel élőknek szánt funkciók**: Egyszerűsített nyelvi opciók.

## Testreszabás és finomhangolás domén-specifikus nyelvi modellekhez

Képzelj el egy csevegőalkalmazást, amely érti a céged zsargonját és előre látja a felhasználói bázis gyakori kérdéseit. Több megközelítést érdemes megemlíteni:

- **DSL modellek használata**. A DSL a domain specifikus nyelvet jelenti. Használhatsz úgynevezett DSL modellt, amely egy adott doménre lett betanítva, hogy megértse annak fogalmait és helyzeteit.
- **Finomhangolás alkalmazása**. A finomhangolás a modelled további, specifikus adatokkal való tanítása.

## Testreszabás: DSL használata

A domén-specifikus nyelvi modellek (DSL modellek) használata növelheti a felhasználói elköteleződést, mivel specializált, kontextusban releváns interakciókat biztosítanak. Ez egy olyan modell, amely egy adott terület, iparág vagy téma szövegének megértésére és generálására lett betanítva vagy finomhangolva. A DSL modell használatának lehetőségei változatosak: lehet saját modellet nulláról tanítani, vagy előre létezőket használni SDK-kon és API-kon keresztül. Egy másik lehetőség a finomhangolás, amely egy meglévő, előre betanított modellt igazít egy adott doménhez.

## Testreszabás: finomhangolás alkalmazása

A finomhangolás gyakran merül fel, amikor egy előre betanított modell nem teljesít elég jól egy szakosodott doménben vagy adott feladatban.

Például az orvosi kérdések komplexek és nagy kontextust igényelnek. Amikor egy orvos diagnosztizál, ezt különböző tényezők, például életmód vagy meglévő állapotok figyelembevételével teszi, és olykor aktuális orvosi szaklapokra is támaszkodik diagnózisának alátámasztásához. Ilyen árnyalt helyzetekben egy általános célú AI csevegőalkalmazás nem lehet megbízható forrás.

### Példa: orvosi alkalmazás

Képzelj el olyan csevegőalkalmazást, amely támogatja az orvosi szakembereket gyors hivatkozásokkal kezelési irányelvekre, gyógyszerkölcsönhatásokra vagy legfrissebb kutatási eredményekre vonatkozóan.

Egy általános célú modell alkalmas lehet alap orvosi kérdések megválaszolására vagy általános tanácsadásra, de nehézségekbe ütközhet az alábbiakban:

- **Nagyon specifikus vagy összetett esetek**. Például egy neurológus megkérdezheti az alkalmazást: „Mik a jelenlegi legjobb gyakorlatok a gyógyszerrezisztens epilepszia kezelésére gyermekkorú betegeknél?”
- **Friss fejlesztések hiánya**. Egy általános célú modell nem biztos, hogy képes a neurológia és farmakológia legfrissebb eredményeit is figyelembe vevő választ adni.

Ilyen esetben a modell finomhangolása egy szakosodott orvosi adattal jelentősen javíthatja e bonyolult orvosi kérdések pontosabb és megbízhatóbb kezelését. Ehhez hozzáférés kell egy nagy és releváns adatkészlethez, amely képviseli a domén-specifikus kihívásokat és kérdéseket.

## Magas minőségű AI-alapú csevegési élmény megfontolásai

Ez a szakasz a „magas minőségű” csevegőalkalmazások kritériumait vázolja, beleértve a használható mérőszámok rögzítését és a felelősségteljes AI technológia alkalmazásához szükséges keretrendszer betartását.

### Kulcsfontosságú mutatók

Az alkalmazás magas teljesítményének fenntartásához elengedhetetlen a kulcsfontosságú mérőszámok és megfontolások nyomon követése. Ezek az értékelések nemcsak az alkalmazás funkcionalitását biztosítják, hanem felmérik az AI modell és a felhasználói élmény minőségét is. Az alábbi lista alapvető, AI és UX mutatókat tartalmaz, amelyekre érdemes figyelni.

| Mutató                       | Meghatározás                                                                                                             | Fejlesztői szempontok                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Üzemidő**                  | Az az időtartam, amíg az alkalmazás működőképes és a felhasználók számára elérhető.                                         | Hogyan minimalizálod a leállásokat?                                      |
| **Válaszidő**                | Az az idő, amely alatt az alkalmazás reagál a felhasználó lekérdezésére.                                                    | Hogyan optimalizálod a lekérdezések feldolgozását a válaszidő javítása érdekében? |
| **Pontosság**                | Az igaz pozitív előrejelzések aránya az összes pozitív előrejelzéshez viszonyítva.                                         | Hogyan validálod a modell pontosságát?                                   |
| **Visszahívás (Érzékenység)** | Az igaz pozitív előrejelzések aránya a tényleges pozitív esetekhez viszonyítva.                                             | Hogyan méred és javítod a visszahívást?                                 |
| **F1 pontszám**              | A pontosság és visszahívás harmonikus átlaga, amely egyensúlyt teremt e két mutató között.                                  | Mi a célzott F1 pontszámod? Hogyan egyensúlyozod a pontosságot és visszahívást? |
| **Perplexitás**              | A mérőszám azt mutatja, mennyire egyezik a modell által jósolt valószínűségi eloszlás az adat valós eloszlásával.             | Hogyan minimalizálod a perplexitást?                                    |
| **Felhasználói elégedettségi mutatók** | A felhasználók véleményét méri az alkalmazásról, gyakran felmérésekkel gyűjtve.                                             | Milyen gyakran gyűjtesz visszajelzést? Hogyan alkalmazod a tapasztalatokat? |
| **Hibaarány**                | A modell által elkövetett hibák aránya a megértésben vagy a kimenetben.                                                     | Milyen stratégiáid vannak a hibaarány csökkentésére?                      |
| **Újraoktatási ciklusok**     | A modell frissítésének gyakorisága új adatok és ismeretek beépítésére.                                                      | Milyen gyakran képezed újra a modellt? Mi indít újraoktatási ciklust?     |

| **Anomália észlelés**         | Szerszámok és technikák a szokványostól eltérő, váratlan mintázatok azonosítására.                        | Hogyan fogsz reagálni az anomáliákra?                                        |

### Felelős MI-gyakorlatok bevezetése csevegőalkalmazásokban

A Microsoft Felelős MI-hez való hozzáállása hat elvet azonosított, amelyeknek irányítaniuk kell az MI fejlesztését és használatát. Az alábbiakban láthatók az elvek, azok meghatározása, valamint amit egy csevegőfejlesztőnek fontolóra kell vennie, és hogy miért kell ezt komolyan vennie.

| Elvek                  | A Microsoft meghatározása                             | Csevegőfejlesztői szempontok                                             | Miért fontos                                                                      |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Méltányosság           | Az MI rendszereknek méltányosan kell bánniuk minden emberrel. | Biztosítsd, hogy a csevegőalkalmazás ne diszkrimináljon a felhasználói adatok alapján. | A felhasználói bizalom és befogadás megteremtése; jogi következmények elkerülése. |
| Megbízhatóság és Biztonság | Az MI rendszereknek megbízhatóan és biztonságosan kell működniük. | Tesztelések és biztonsági mechanizmusok bevezetése a hibák és kockázatok minimalizálására. | Felhasználói elégedettség garantálása és potenciális károk megelőzése.             |
| Adatvédelem és Biztonság | Az MI rendszereknek biztonságosnak kell lenniük, és tiszteletben kell tartaniuk a magánszférát. | Erős titkosítás és adatvédelmi intézkedések alkalmazása.                 | Érzékeny felhasználói adatok védelme és adatvédelmi jogszabályoknak való megfelelés. |
| Befogadás              | Az MI rendszereknek mindenkiben erőt kell adniuk és be kell vonniuk az embereket. | Olyan UI/UX tervezése, amely hozzáférhető és könnyen használható különböző felhasználók számára. | Szélesebb közönség hatékony alkalmazáshasználatának biztosítása.                   |
| Átláthatóság           | Az MI rendszerek érthetőek kell legyenek.             | Világos dokumentáció és magyarázatok biztosítása az MI válaszairól.    | A felhasználók jobban megbíznak a rendszerben, ha értik, hogyan hozza döntéseit.   |
| Felelősség             | Az embereknek felelősséget kell vállalniuk az MI rendszerekért. | Világos folyamat kialakítása az MI döntések auditálására és fejlesztésére. | Folyamatos fejlesztés és hibák esetén helyesbítő intézkedések lehetősége.          |

## Feladat

Lásd a [feladatot](../../../07-building-chat-applications/python). Átvezet egy sor gyakorlaton az első csevegési promptod futtatásától a szöveg osztályozásán és összefoglalásán át sok minden másig. Érdemes megjegyezni, hogy a feladatok különböző programozási nyelveken is elérhetők!

## Nagyszerű munka! Folytasd az utazást

A lecke elvégzése után nézd meg [a Generatív MI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszthesd generatív MI tudásod!

Lépj át a 8. leckére, hogy megtudd, hogyan kezdhetsz el [keresőalkalmazásokat építeni](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->