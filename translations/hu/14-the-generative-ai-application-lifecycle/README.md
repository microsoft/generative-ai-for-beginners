[![Funkcióhívással való integráció](../../../translated_images/hu/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# A Generatív MI alkalmazás életciklusa

Egy fontos kérdés minden MI alkalmazás esetében az MI funkciók relevanciája, mivel az MI gyorsan fejlődő terület. Annak érdekében, hogy az alkalmazásod releváns, megbízható és robusztus maradjon, folyamatosan figyelnie, értékelnie és fejlesztenie kell azt. Itt lép be a generatív MI életciklusa.

A generatív MI életciklusa egy keretrendszer, amely végigvezet a generatív MI alkalmazás fejlesztésének, telepítésének és karbantartásának szakaszain. Segít meghatározni céljaidat, mérni a teljesítményedet, azonosítani a kihívásaidat, és megvalósítani a megoldásaidat. Továbbá segít az alkalmazásod összhangba hozni az adott terület és az érintettek etikai és jogi szabályaival. A generatív MI életciklus követésével biztosíthatod, hogy alkalmazásod mindig értéket nyújtson és elégedetté tegye a felhasználóidat.

## Bevezetés

Ebben a fejezetben:

- Megérted az MLOps-ról az LLMOps-ra való paradigmaváltást
- Az LLM életciklusa
- Eszközök az életciklus kezeléséhez
- Életciklus metrikák és értékelés

## Megérteni az MLOps-ról az LLMOps-ra való paradigmaváltást

Az LLM-ek új eszközök a mesterséges intelligencia arzenáljában, hihetetlenül erősek az elemző és generáló feladatokban, azonban ez az erő következményekkel jár az MI és a klasszikus gépi tanulás feladatainak egyszerűsítésében.

Ezért egy új paradigma szükséges, hogy dinamikusan, a megfelelő ösztönzőkkel igazítsuk ezt az eszközt. A régebbi MI alkalmazásokat "ML alkalmazásokként", az újabbakat pedig "GenAI alkalmazásokként" vagy egyszerűen "MI alkalmazásokként" kategorizálhatjuk, tükrözve az adott időszakban alkalmazott fő technológiákat és technikákat. Ez a megközelítés több szempontból is módosítja a narratívánkat, lásd az alábbi összehasonlítást.

![LLMOps vs. MLOps összehasonlítás](../../../translated_images/hu/01-llmops-shift.29bc933cb3bb0080.webp)

Vegyük észre, hogy az LLMOps inkább az alkalmazásfejlesztőkre összpontosít, az integrációkat kulcspontként használva, a "Modellek mint szolgáltatások" szemléletet alkalmazva, és a következő metrikákra koncentrálva.

- Minőség: Válasz minősége
- Kár: Felelős MI
- Őszinteség: Válasz megalapozottsága (Értelmes? Helyes?)
- Költség: Megoldás költségvetése
- Válaszidő: Átlagos idő tokenválaszra

## Az LLM életciklusa

Először is, az életciklus megértéséhez és a módosításokhoz nézzük meg a következő infografikát.

![LLMOps infografika](../../../translated_images/hu/02-llmops.70a942ead05a7645.webp)

Ahogy észreveheted, ez eltér a megszokott MLOps életciklusoktól. Az LLM-ek számos új követelményt támasztanak, mint a promptolás, különböző minőségjavító technikák (finomhangolás, RAG, meta-promptok), eltérő értékelés és felelősség a felelős MI kapcsán, valamint új értékelési metrikák (minőség, kár, őszinteség, költség és válaszidő).

Például nézd meg, hogyan alkotunk ötleteket. Prompt mérnökséget használunk, hogy különböző LLM-ekkel kísérletezzünk, és felfedezzük a lehetőségeket, tesztelve, hogy a hipotézisünk helyes lehet-e.

Jegyezd meg, hogy ez nem lineáris, hanem integrált ciklusokból áll, ismétlődő és egy átfogó ciklussal.

Hogyan fedezhetjük fel ezeket a lépéseket? Nézzük meg részletesen, hogyan építhetünk életciklust.

![LLMOps munkafolyamat](../../../translated_images/hu/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Ez talán kissé bonyolultnak tűnhet, fókuszáljunk először a három nagy lépésre.

1. Ötletelés/Felfedezés: Felfedezés, itt üzleti igényeink szerint kutathatunk. Prototípus készítés, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) létrehozása és tesztelése, hogy elég hatékony-e a hipotézisünkhöz.
1. Építés/Bővítés: Megvalósítás, ekkor elkezdjük értékelni a nagyobb adatkészleteket, megvalósítunk technikákat, mint a finomhangolás és a RAG, hogy ellenőrizzük megoldásunk robusztusságát. Ha nem működik, újra megvalósíthatjuk, további lépéseket adhatunk a folyamatunkhoz vagy átszervezhetjük az adatokat. A folyamatunk és a skálázás tesztelése után, ha működik és az értékelő metrikák megfelelőek, készen áll a következő lépésre.
1. Üzembe helyezés: Integráció, most hozzáadjuk a monitorozási és riasztási rendszereket a rendszerünkhöz, telepítjük és integráljuk az alkalmazásba.

Ezután jön az átfogó menedzsment ciklus, amely a biztonságra, megfelelőségre és irányításra fókuszál.

Gratulálunk, most már készen áll az MI alkalmazásod az éles működésre. Gyakorlati tapasztalathoz nézd meg a [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) bemutatót.

Most pedig, milyen eszközöket használhatunk?

## Életciklus eszközök

Az eszközökhöz a Microsoft az [Azure AI Platformot](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) és a [PromptFlow-t](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) kínálja, amelyek megkönnyítik és egyben egyszerűvé teszik az életciklus megvalósítását.

Az [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) lehetővé teszi a [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) használatát. A Microsoft Foundry (korábban Azure AI Studio) egy webes portál, amely modellek, minták és eszközök felfedezését, erőforrások kezelését, UI fejlesztési folyamatokat és SDK/CLI opciókat kínál kód alapú fejlesztéshez.

![Azure AI lehetőségek](../../../translated_images/hu/04-azure-ai-platform.80203baf03a12fa8.webp)

Az Azure AI lehetővé teszi több erőforrás használatát az üzemeltetésedhez, szolgáltatásokhoz, projektekhez, vektor kereséshez és adatbázis igényekhez.

![LLMOps az Azure AI-val](../../../translated_images/hu/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Készíts proof-of-concepttől (POC) a nagyszabású alkalmazásokig a PromptFlow-val:

- Alkalmazások tervezése és fejlesztése VS Code-ból vizuális és funkcionális eszközökkel
- Alkalmazások tesztelése és finomhangolása a minőségi MI érdekében, egyszerűen.
- Használd a Microsoft Foundry-t a felhővel való integrációra és iterációra, gyors integráció érdekében tolás és telepítés.

![LLMOps a PromptFlow-val](../../../translated_images/hu/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Szuper! Folytasd a tanulást!

Nagyszerű, most tanulj meg többet arról, hogyan épül fel egy alkalmazás, hogy alkalmazd a koncepciókat a [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) segítségével, ahol a Cloud Advocacy bemutatja ezeket a koncepciókat demonstráció során. Több tartalomért nézd meg az [Ignite breakout sessionünket!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Most pedig nézd meg a 15. leckét, hogy megértsd, hogyan befolyásolják a [Retrieval Augmented Generation és a Vektor Adatbázisok](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) a generatív MI-t, és hogy még érdekesebb alkalmazásokat készíthess!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->