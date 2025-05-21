<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:05:39+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "hu"
}
-->
# Generatív AI Alkalmazások Biztonságának Megőrzése

[![Generatív AI Alkalmazások Biztonságának Megőrzése](../../../translated_images/13-lesson-banner.c21a3a479f9ff14ad1f7c9b02bfe0d9a549b43497588334356f91073466a1283.hu.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Bevezetés

Ez a lecke az alábbi témákat tárgyalja:

- Biztonság az AI rendszerek kontextusában.
- Az AI rendszerekre leselkedő gyakori kockázatok és fenyegetések.
- Módszerek és szempontok az AI rendszerek biztonságának megőrzésére.

## Tanulási célok

A lecke elvégzése után megérted:

- Az AI rendszerekre leselkedő fenyegetéseket és kockázatokat.
- Az AI rendszerek biztonságának megőrzésére szolgáló általános módszereket és gyakorlatokat.
- Hogyan akadályozhatja meg a biztonsági tesztelés végrehajtása a váratlan eredményeket és a felhasználói bizalom csökkenését.

## Mit jelent a biztonság a generatív AI kontextusában?

Ahogy a Mesterséges Intelligencia (AI) és a Gépi Tanulás (ML) technológiák egyre inkább formálják életünket, nemcsak az ügyféladatok védelme, hanem az AI rendszerek védelme is létfontosságúvá válik. Az AI/ML egyre inkább használatos a magas értékű döntéshozatali folyamatok támogatására olyan iparágakban, ahol a rossz döntés súlyos következményekkel járhat.

Íme néhány fontos szempont:

- **AI/ML hatása**: Az AI/ML jelentős hatással van a mindennapi életre, ezért megóvásuk elengedhetetlenné vált.
- **Biztonsági kihívások**: Az AI/ML hatása megfelelő figyelmet igényel annak érdekében, hogy megvédjük az AI-alapú termékeket a kifinomult támadásoktól, legyenek azok trollok vagy szervezett csoportok.
- **Stratégiai problémák**: A tech iparnak proaktívan kell foglalkoznia a stratégiai kihívásokkal a hosszú távú ügyfélbiztonság és adatbiztonság érdekében.

Továbbá a Gépi Tanulási modellek nagyrészt képtelenek megkülönböztetni a rosszindulatú bemenetet a jóindulatú anomáliás adatoktól. A képzési adatok jelentős része nem kurált, nem moderált, nyilvános adatbázisokból származik, amelyek nyitottak harmadik fél hozzájárulására. A támadóknak nem kell feltörniük az adatbázisokat, ha szabadon hozzájárulhatnak hozzájuk. Idővel a kis megbízhatóságú rosszindulatú adatok magas megbízhatóságú megbízható adatokká válnak, ha az adatstruktúra/formázás helyes marad.

Ezért kritikus fontosságú a modellek döntéseihez használt adattárak integritásának és védelmének biztosítása.

## Az AI fenyegetéseinek és kockázatainak megértése

Az AI és kapcsolódó rendszerek tekintetében az adatmérgezés ma a legjelentősebb biztonsági fenyegetés. Az adatmérgezés akkor következik be, amikor valaki szándékosan megváltoztatja az AI képzésére használt információkat, hibákat okozva ezzel. Ez a szabványosított észlelési és mérséklési módszerek hiánya miatt van, valamint amiatt, hogy a képzéshez megbízhatatlan vagy nem kurált nyilvános adatbázisokra támaszkodunk. Az adatok integritásának megőrzése és a hibás képzési folyamat megelőzése érdekében fontos nyomon követni az adatok eredetét és származását. Ellenkező esetben az a régi mondás, hogy „szemetet be, szemetet ki”, igaz lesz, ami a modell teljesítményének romlásához vezet.

Az alábbiakban példák láthatók arra, hogyan befolyásolhatja az adatmérgezés a modelleket:

1. **Címkefordítás**: Egy bináris osztályozási feladatban egy ellenfél szándékosan megfordítja a képzési adatok egy kis részhalmazának címkéit. Például a jóindulatú mintákat rosszindulatúként címkézik, ami a modell számára helytelen társításokat tanít.\
   **Példa**: Egy spam szűrő, amely a manipulált címkék miatt jogos e-maileket spamként azonosít.
2. **Jellemzőmérgezés**: Egy támadó finoman módosítja a képzési adatok jellemzőit, hogy torzítást vezessen be vagy félrevezesse a modellt.\
   **Példa**: Releváns kulcsszavak hozzáadása termékleírásokhoz, hogy manipulálják az ajánlórendszereket.
3. **Adatinjekció**: Rosszindulatú adatok bejuttatása a képzési készletbe a modell viselkedésének befolyásolása érdekében.\
   **Példa**: Hamis felhasználói értékelések bevezetése, hogy elferdítsék a hangulatelemzési eredményeket.
4. **Hátsóajtós támadások**: Egy ellenfél rejtett mintát (hátsóajtót) helyez el a képzési adatokban. A modell megtanulja felismerni ezt a mintát, és rosszindulatúan viselkedik, ha aktiválják.\
   **Példa**: Egy arcfelismerő rendszer, amely hátsóajtós képekkel lett betanítva, és egy konkrét személyt hibásan azonosít.

A MITRE Corporation létrehozta az [ATLAS-t (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), amely egy tudásbázis a valós támadások során alkalmazott taktikákról és technikákról az AI rendszerek ellen.

> Az AI-alapú rendszerekben egyre több sebezhetőség van, mivel az AI beépítése növeli a meglévő rendszerek támadási felületét a hagyományos kibertámadásokon túl. Az ATLAS-t azért fejlesztettük ki, hogy felhívjuk a figyelmet ezekre az egyedi és fejlődő sebezhetőségekre, mivel a globális közösség egyre inkább beépíti az AI-t különféle rendszerekbe. Az ATLAS a MITRE ATT&CK® keretrendszer alapján készült, és taktikái, technikái, valamint eljárásai kiegészítik az ATT&CK-ban találhatóakat.

Hasonlóan a MITRE ATT&CK® keretrendszerhez, amelyet széles körben használnak a hagyományos kiberbiztonságban az előrehaladott fenyegetési emulációs forgatókönyvek tervezésére, az ATLAS könnyen kereshető TTP-készletet biztosít, amely segít jobban megérteni és felkészülni a felmerülő támadások elleni védekezésre.

Ezenkívül az Open Web Application Security Project (OWASP) létrehozott egy "[Top 10 listát](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" a LLM-eket használó alkalmazásokban található legkritikusabb sebezhetőségekről. A lista kiemeli az olyan fenyegetések kockázatait, mint a már említett adatmérgezés, valamint másokat, mint például:

- **Prompt Injection**: egy technika, ahol a támadók egy Nagy Nyelvi Modellt (LLM) manipulálnak gondosan megtervezett bemenetekkel, hogy az a szándékolt viselkedésén kívül működjön.
- **Ellátási lánc sebezhetőségek**: Az LLM által használt alkalmazásokat alkotó összetevők és szoftverek, mint például a Python modulok vagy külső adatbázisok, maguk is kompromittálhatók, ami váratlan eredményekhez, bevezetett torzításokhoz és akár sebezhetőségekhez vezethet az alapul szolgáló infrastruktúrában.
- **Túlzott függőség**: Az LLM-ek hibázhatnak és hajlamosak fantáziálni, pontatlan vagy veszélyes eredményeket adva. Számos dokumentált esetben az emberek az eredményeket készpénznek vették, ami nem szándékolt valós világban negatív következményekhez vezetett.

A Microsoft Cloud Advocate Rod Trent írt egy ingyenes ebookot, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), amely mélyrehatóan foglalkozik ezekkel és más felmerülő AI fenyegetésekkel, és átfogó útmutatást nyújt arra, hogyan lehet a legjobban kezelni ezeket a helyzeteket.

## Biztonsági Tesztelés AI Rendszerek és LLM-ek Számára

A mesterséges intelligencia (AI) különböző területeket és iparágakat alakít át, új lehetőségeket és előnyöket kínálva a társadalom számára. Azonban az AI jelentős kihívásokat és kockázatokat is jelent, mint például az adatvédelem, a torzítás, a magyarázhatóság hiánya és a potenciális visszaélések. Ezért elengedhetetlen, hogy az AI rendszerek biztonságosak és felelősségteljesek legyenek, vagyis megfeleljenek az etikai és jogi normáknak, és a felhasználók és az érdekelt felek megbízhassanak bennük.

A biztonsági tesztelés az AI rendszer vagy LLM biztonságának értékelési folyamata, amely során azonosítják és kihasználják a sebezhetőségeiket. Ezt a fejlesztők, felhasználók vagy harmadik fél auditorok végezhetik, a tesztelés céljától és terjedelmétől függően. Az AI rendszerek és LLM-ek számára leggyakrabban használt biztonsági tesztelési módszerek közé tartoznak:

- **Adattisztítás**: Ez az AI rendszer vagy LLM képzési adataiból vagy bemenetéből származó érzékeny vagy privát információk eltávolításának vagy anonimizálásának folyamata. Az adattisztítás segíthet megakadályozni az adatszivárgást és a rosszindulatú manipulációt azáltal, hogy csökkenti a bizalmas vagy személyes adatok kitettségét.
- **Ellenséges tesztelés**: Ez az AI rendszer vagy LLM bemenetére vagy kimenetére ellenséges példák generálásának és alkalmazásának folyamata, hogy értékeljék a robusztusságát és ellenállását az ellenséges támadásokkal szemben. Az ellenséges tesztelés segíthet az AI rendszer vagy LLM sebezhetőségeinek és gyengeségeinek azonosításában és mérséklésében, amelyeket a támadók kihasználhatnak.
- **Modell-ellenőrzés**: Ez az AI rendszer vagy LLM modellparamétereinek vagy architektúrájának helyességének és teljességének ellenőrzési folyamata. A modell-ellenőrzés segíthet a modell lopásának észlelésében és megelőzésében azáltal, hogy biztosítja, hogy a modell védett és hitelesített.
- **Kimeneti validálás**: Ez az AI rendszer vagy LLM kimenetének minőségének és megbízhatóságának validálási folyamata. A kimeneti validálás segíthet a rosszindulatú manipuláció észlelésében és javításában azáltal, hogy biztosítja, hogy a kimenet konzisztens és pontos.

Az OpenAI, az AI rendszerek vezetője, biztonsági értékeléseket állított fel a piros csapat hálózati kezdeményezés részeként, amelynek célja az AI rendszerek kimenetének tesztelése az AI biztonságának előmozdítása érdekében.

> Az értékelések egyszerű kérdés-válasz tesztektől bonyolultabb szimulációkig terjedhetnek. Konkrét példaként, az alábbiakban az OpenAI által kifejlesztett mintavételek láthatók, amelyek az AI viselkedésének különböző szempontokból történő értékelésére szolgálnak:

#### Meggyőzés

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer egy másik AI rendszert becsapni, hogy kimondjon egy titkos szót?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer egy másik AI rendszert rávenni, hogy pénzt adományozzon?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer egy másik AI rendszer politikai javaslat támogatására befolyásolni?

#### Szteganográfia (rejtett üzenetek)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer titkos üzeneteket átadni anélkül, hogy egy másik AI rendszer észrevenné?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer üzeneteket tömöríteni és kitömöríteni, hogy lehetővé tegye titkos üzenetek elrejtését?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer más AI rendszerrel koordinálni közvetlen kommunikáció nélkül?

### AI Biztonság

Elengedhetetlen, hogy megvédjük az AI rendszereket a rosszindulatú támadásoktól, visszaélésektől vagy nem szándékolt következményektől. Ez magában foglalja az AI rendszerek biztonságának, megbízhatóságának és hitelességének biztosítását, például:

- Az AI modellek képzésére és futtatására használt adatok és algoritmusok biztosítása
- Az AI rendszerekhez való jogosulatlan hozzáférés, manipuláció vagy szabotázs megakadályozása
- Az AI rendszerekben megjelenő torzítások, diszkrimináció vagy etikai problémák észlelése és mérséklése
- Az AI döntések és cselekvések elszámoltathatóságának, átláthatóságának és magyarázhatóságának biztosítása
- Az AI rendszerek céljainak és értékeinek az emberek és a társadalom céljaival való összehangolása

Az AI biztonság fontos az AI rendszerek és adatok integritásának, elérhetőségének és bizalmasságának biztosítása érdekében. Az AI biztonságának néhány kihívása és lehetősége:

- Lehetőség: Az AI beépítése a kiberbiztonsági stratégiákba, mivel az AI kulcsszerepet játszhat a fenyegetések azonosításában és a válaszidők javításában. Az AI segíthet a kibertámadások, például az adathalászat, a rosszindulatú szoftverek vagy a zsarolóprogramok észlelésének és mérséklésének automatizálásában és kiegészítésében.
- Kihívás: Az AI-t az ellenfelek is felhasználhatják kifinomult támadások indítására, például hamis vagy félrevezető tartalom generálására, felhasználók megszemélyesítésére vagy az

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.