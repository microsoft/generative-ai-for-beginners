<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T16:37:19+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "hu"
}
-->
[![Integrálás függvényhívással](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.hu.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# A generatív MI alkalmazás életciklusa

Minden MI alkalmazás számára fontos kérdés az MI funkciók relevanciája, mivel az MI gyorsan fejlődő terület, hogy az alkalmazásod releváns, megbízható és robusztus maradjon, folyamatosan figyelni, értékelni és fejleszteni kell. Ebben segít a generatív MI életciklus.

A generatív MI életciklus egy keretrendszer, amely végigvezet a generatív MI alkalmazás fejlesztésének, bevezetésének és karbantartásának szakaszain. Segít meghatározni a céljaidat, mérni a teljesítményedet, azonosítani a kihívásaidat és megvalósítani a megoldásaidat. Emellett segít az alkalmazásod összehangolásában az adott terület és az érintettek etikai és jogi normáival. A generatív MI életciklus követésével biztosíthatod, hogy az alkalmazásod mindig értéket nyújtson és elégedetté tegye a felhasználókat.

## Bevezetés

Ebben a fejezetben:

- Megérted az MLOps-ról az LLMOps-ra való paradigmaváltást
- Az LLM életciklusát
- Az életciklus eszközeit
- Az életciklus metrikázását és értékelését

## Megérteni az MLOps-ról az LLMOps-ra való paradigmaváltást

Az LLM-ek új eszközök a mesterséges intelligencia arzenáljában, rendkívül erősek elemzési és generálási feladatokban az alkalmazások számára, azonban ez az erő bizonyos következményekkel jár az MI és a klasszikus gépi tanulási feladatok egyszerűsítésében.

Ehhez új paradigmára van szükség, hogy ezt az eszközt dinamikusan, a megfelelő ösztönzőkkel alkalmazzuk. A régebbi MI alkalmazásokat "ML alkalmazásoknak", az újabbakat pedig "GenAI alkalmazásoknak" vagy egyszerűen "MI alkalmazásoknak" nevezhetjük, tükrözve az adott időszak fő technológiáit és technikáit. Ez többféleképpen is megváltoztatja a narratívánkat, nézd meg az alábbi összehasonlítást.

![LLMOps vs. MLOps összehasonlítás](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.hu.png)

Figyeld meg, hogy az LLMOps esetén inkább az alkalmazásfejlesztőkre fókuszálunk, az integrációkat kulcspontként használva, "Modellek mint szolgáltatás" megközelítéssel, és a következő metrikákra gondolunk.

- Minőség: Válasz minősége
- Káros hatás: Felelős MI
- Őszinteség: Válasz megalapozottsága (Értelmes? Helyes?)
- Költség: Megoldás költségvetése
- Késleltetés: Átlagos válaszidő tokenenként

## Az LLM életciklusa

Először, hogy megértsük az életciklust és a módosításokat, nézzük meg a következő infografikát.

![LLMOps infografika](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.hu.png)

Ahogy láthatod, ez eltér a megszokott MLOps életciklusoktól. Az LLM-eknek sok új követelménye van, mint a promptolás, különböző technikák a minőség javítására (finomhangolás, RAG, meta-promptok), különböző értékelési és felelősségi szempontok a felelős MI-vel kapcsolatban, végül új értékelési metrikák (minőség, káros hatás, őszinteség, költség és késleltetés).

Például nézd meg, hogyan ötletelünk. Prompt mérnökséget használva különböző LLM-ekkel kísérletezünk, hogy felfedezzük a lehetőségeket és teszteljük, hogy a hipotézisük helyes lehet-e.

Figyeld meg, hogy ez nem lineáris, hanem integrált hurkokból áll, iteratív és egy átfogó ciklussal.

Hogyan fedezhetnénk fel ezeket a lépéseket? Nézzük meg részletesen, hogyan építhetünk életciklust.

![LLMOps munkafolyamat](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.hu.png)

Ez talán bonyolultnak tűnik, fókuszáljunk először a három nagy lépésre.

1. Ötletelés/Felfedezés: Felfedezés, itt az üzleti igényeink szerint fedezhetünk fel. Prototípus készítése, egy [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) létrehozása és tesztelése, hogy elég hatékony-e a hipotézisünkhöz.
1. Építés/Kibővítés: Megvalósítás, most elkezdjük nagyobb adathalmazokon értékelni, technikákat alkalmazni, mint a finomhangolás és RAG, hogy ellenőrizzük a megoldásunk robusztusságát. Ha nem működik, újraimplementálás, új lépések hozzáadása a folyamatba vagy az adatok átszervezése segíthet. Miután teszteltük a folyamatot és a skálát, ha működik és megfelel a metrikáknak, készen áll a következő lépésre.
1. Üzemeltetés: Integráció, most hozzáadjuk a monitorozó és riasztó rendszereket a rendszerhez, bevezetjük és integráljuk az alkalmazásba.

Ezután van egy átfogó menedzsment ciklus, amely a biztonságra, megfelelőségre és irányításra fókuszál.

Gratulálunk, most már készen áll az MI alkalmazásod az üzemeltetésre. Gyakorlati tapasztalatért nézd meg a [Contoso Chat Demo-t.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Most, milyen eszközöket használhatunk?

## Életciklus eszközök

Eszközök tekintetében a Microsoft az [Azure AI Platformot](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) és a [PromptFlow-t](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) kínálja, amelyek megkönnyítik és egyszerűvé teszik az életciklus megvalósítását.

Az [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) lehetővé teszi az [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys) használatát. Az AI Studio egy webes portál, amely lehetővé teszi modellek, minták és eszközök felfedezését. Erőforrásaid kezelését, UI fejlesztési folyamatokat és SDK/CLI opciókat kínál kód-első fejlesztéshez.

![Azure AI lehetőségek](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.hu.png)

Az Azure AI lehetővé teszi több erőforrás használatát, hogy kezeld az üzemeltetést, szolgáltatásokat, projekteket, vektoros keresést és adatbázis igényeket.

![LLMOps Azure AI-val](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.hu.png)

Építs, a Proof-of-Concepttől (POC) a nagyszabású alkalmazásokig a PromptFlow-val:

- Tervezd és építsd az alkalmazásokat VS Code-ból, vizuális és funkcionális eszközökkel
- Teszteld és finomhangold az alkalmazásokat minőségi MI-hez, könnyedén.
- Használd az Azure AI Studiot az integrációhoz és iterációhoz a felhővel, gyors integráció érdekében nyomd és telepítsd.

![LLMOps PromptFlow-val](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.hu.png)

## Remek! Folytasd a tanulást!

Csodás, most tanulj meg többet arról, hogyan strukturálunk egy alkalmazást, hogy használd a fogalmakat a [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) segítségével, hogy lásd, hogyan alkalmazza a Cloud Advocacy ezeket a fogalmakat a bemutatókban. További tartalmakért nézd meg az [Ignite szekciót!](https://www.youtube.com/watch?v=DdOylyrTOWg)

Most nézd meg a 15. leckét, hogy megértsd, hogyan hat a [Retrieval Augmented Generation és a vektoros adatbázisok](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) a generatív MI-re, és hogyan teheted az alkalmazásokat még vonzóbbá!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->