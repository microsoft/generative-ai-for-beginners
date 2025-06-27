<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:36:38+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "hu"
}
-->
# Generatív AI Alkalmazások Biztonsága

[![Generatív AI Alkalmazások Biztonsága](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.hu.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Bevezetés

Ez a lecke foglalkozik:

- Biztonsággal az AI rendszerek kontextusában.
- AI rendszereket érintő gyakori kockázatokkal és fenyegetésekkel.
- Módszerekkel és megfontolásokkal az AI rendszerek biztonságának megőrzésére.

## Tanulási célok

A lecke elvégzése után megérted:

- Az AI rendszereket érintő fenyegetéseket és kockázatokat.
- Gyakori módszereket és gyakorlatokat az AI rendszerek biztonságának megőrzésére.
- Hogyan előzheti meg a biztonsági tesztelés a nem várt eredményeket és a felhasználói bizalom elvesztését.

## Mit jelent a biztonság a generatív AI kontextusában?

Ahogy az Mesterséges Intelligencia (AI) és a Gépi Tanulás (ML) technológiák egyre inkább formálják életünket, elengedhetetlen, hogy ne csak az ügyféladatokat, hanem magukat az AI rendszereket is védjük. Az AI/ML egyre inkább használatos a nagy értékű döntéshozatali folyamatok támogatására olyan iparágakban, ahol a rossz döntés súlyos következményekkel járhat.

Íme néhány fontos szempont:

- **Az AI/ML hatása**: Az AI/ML jelentős hatással van a mindennapi életre, és ezért ezek védelme alapvetővé vált.
- **Biztonsági kihívások**: Az AI/ML hatása megfelelő figyelmet igényel annak érdekében, hogy megvédjük az AI-alapú termékeket a kifinomult támadásoktól, legyenek azok trollok vagy szervezett csoportok által.
- **Stratégiai problémák**: A technológiai iparnak proaktívan kell kezelnie a stratégiai kihívásokat, hogy hosszú távon biztosítsa az ügyfélbiztonságot és az adatvédelmet.

Ezen kívül a Gépi Tanulás modellek nagyrészt képtelenek megkülönböztetni a rosszindulatú bemenetet a jóindulatú anomáliás adatoktól. A képzési adatok jelentős része nem kurált, nem moderált, nyilvános adatbázisokból származik, amelyek nyitottak harmadik fél hozzájárulására. A támadóknak nem kell feltörniük az adatbázisokat, ha szabadon hozzájárulhatnak hozzájuk. Idővel a gyenge biztonságú rosszindulatú adatok megbízható adatokká válnak, ha az adatszerkezet/formátum helyes marad.

Ezért kritikus fontosságú biztosítani az adatok integritását és védelmét, amelyeket a modellek döntéshozatalhoz használnak.

## Az AI fenyegetéseinek és kockázatainak megértése

Az AI és kapcsolódó rendszerek szempontjából a mai legjelentősebb biztonsági fenyegetés a adatmérgezés. Az adatmérgezés az, amikor valaki szándékosan megváltoztatja az AI képzéséhez használt információkat, hibákhoz vezetve. Ennek oka a szabványosított észlelési és mérséklési módszerek hiánya, valamint a megbízhatatlan vagy nem kurált nyilvános adatbázisokra való támaszkodás a képzéshez. Az adatintegritás fenntartása és a hibás képzési folyamat elkerülése érdekében elengedhetetlen az adatok eredetének és származásának nyomon követése. Ellenkező esetben a régi mondás „szemét be, szemét ki” igaz lesz, ami a modell teljesítményének romlásához vezet.

Íme példák arra, hogyan befolyásolhatja az adatmérgezés a modelleket:

1. **Címkefordítás**: Egy bináris osztályozási feladat során egy ellenfél szándékosan megfordítja a képzési adatok egy kis részének címkéit. Például a jóindulatú minták rosszindulatúként vannak címkézve, ami a modell hibás asszociációkat tanul meg.\
   **Példa**: Egy spam szűrő, amely a manipulált címkék miatt a legitim e-maileket spamként osztályozza.
2. **Jellemzőmérgezés**: Egy támadó finoman módosítja a képzési adatok jellemzőit, hogy torzítást vezessen be vagy félrevezesse a modellt.\
   **Példa**: Releváns kulcsszavak hozzáadása termékleírásokhoz, hogy manipulálja az ajánlórendszereket.
3. **Adatbefecskendezés**: Rosszindulatú adatok befecskendezése a képzési készletbe, hogy befolyásolja a modell viselkedését.\
   **Példa**: Hamis felhasználói vélemények bevezetése, hogy torzítsa az érzelem elemzés eredményeit.
4. **Hátsó ajtó támadások**: Egy ellenfél rejtett mintát (hátsó ajtót) illeszt be a képzési adatokba. A modell megtanulja felismerni ezt a mintát, és rosszindulatúan viselkedik, amikor aktiválódik.\
   **Példa**: Egy arcfelismerő rendszer, amely hátsó ajtóval ellátott képekkel van kiképezve, és tévesen azonosít egy konkrét személyt.

A MITRE Corporation létrehozta az [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) nevű tudásbázist, amely az AI rendszerek valódi támadásai során alkalmazott taktikákat és technikákat tartalmazza.

> Az AI-vel támogatott rendszerekben egyre több sebezhetőség van, mivel az AI beépítése növeli a meglévő rendszerek támadási felületét a hagyományos kibertámadásokon túl. Az ATLAS-t azért fejlesztettük ki, hogy felhívjuk a figyelmet ezekre az egyedi és fejlődő sebezhetőségekre, ahogy a globális közösség egyre inkább beépíti az AI-t különböző rendszerekbe. Az ATLAS a MITRE ATT&CK® keretrendszer alapján készült, és taktikái, technikái és eljárásai (TTP-k) kiegészítik az ATT&CK-ban találhatókat.

Hasonlóan a MITRE ATT&CK® keretrendszerhez, amelyet széles körben használnak a hagyományos kiberbiztonságban a fejlett fenyegetések emulációs forgatókönyveinek tervezésére, az ATLAS könnyen kereshető TTP-készletet biztosít, amely segíthet jobban megérteni és felkészülni a feltörekvő támadások elleni védekezésre.

Ezen kívül az Open Web Application Security Project (OWASP) létrehozta a "[Top 10 listát](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" a LLM-eket használó alkalmazásokban található legkritikusabb sebezhetőségekről. A lista kiemeli az olyan fenyegetések kockázatait, mint az említett adatmérgezés, valamint másokat, mint például:

- **Prompt Injection**: egy technika, ahol a támadók gondosan megtervezett bemenetekkel manipulálják a Nagy Nyelvi Modellek (LLM), hogy azok a szándékolt viselkedésen kívül működjenek.
- **Ellátási Lánc Sebezhetőségek**: Az LLM által használt alkalmazások összetevői és szoftverei, mint például a Python modulok vagy külső adatbázisok, maguk is kompromittálódhatnak, ami váratlan eredményekhez, bevezetett torzításokhoz és akár az alapinfrastruktúrában található sebezhetőségekhez vezethet.
- **Túlzott támaszkodás**: Az LLM-ek tévedhetők és hajlamosak hallucinálni, pontatlan vagy nem biztonságos eredményeket szolgáltatva. Számos dokumentált esetben az emberek a kapott eredményeket készpénznek vették, ami nem szándékolt valós világ negatív következményekhez vezetett.

Microsoft Cloud Advocate Rod Trent írt egy ingyenes e-könyvet, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), amely mélyen belemerül ezekbe és más feltörekvő AI fenyegetésekbe, és átfogó útmutatást nyújt, hogyan lehet legjobban kezelni ezeket a helyzeteket.

## Biztonsági tesztelés AI rendszerek és LLM-ek számára

A mesterséges intelligencia (AI) különböző területeket és iparágakat alakít át, új lehetőségeket és előnyöket kínálva a társadalom számára. Azonban az AI jelentős kihívásokat és kockázatokat is jelent, mint például adatvédelem, torzítás, magyarázhatóság hiánya és potenciális visszaélés. Ezért elengedhetetlen biztosítani, hogy az AI rendszerek biztonságosak és felelősek legyenek, azaz megfeleljenek az etikai és jogi normáknak, és megbízhatóak legyenek a felhasználók és érintettek számára.

A biztonsági tesztelés az AI rendszer vagy LLM biztonságának értékelésének folyamata, sebezhetőségeik azonosításával és kihasználásával. Ezt a fejlesztők, felhasználók vagy harmadik fél auditorok végezhetik, a tesztelés céljától és terjedelmétől függően. Az AI rendszerek és LLM-ek leggyakoribb biztonsági tesztelési módszerei a következők:

- **Adattisztítás**: Ez az érzékeny vagy privát információk eltávolításának vagy anonimizálásának folyamata az AI rendszer vagy LLM képzési adataiból vagy bemenetéből. Az adattisztítás segíthet megelőzni az adatvesztést és a rosszindulatú manipulációt azáltal, hogy csökkenti a bizalmas vagy személyes adatok kitettségét.
- **Adversarial tesztelés**: Ez az ellenséges példák generálásának és alkalmazásának folyamata egy AI rendszer vagy LLM bemenetére vagy kimenetére, hogy értékelje annak robusztusságát és ellenállóképességét az ellenséges támadásokkal szemben. Az adversarial tesztelés segíthet az AI rendszer vagy LLM sebezhetőségeinek és gyengeségeinek azonosításában és mérséklésében, amelyeket a támadók kihasználhatnak.
- **Modell ellenőrzés**: Ez az AI rendszer vagy LLM modellparamétereinek vagy architektúrájának helyességének és teljességének ellenőrzésének folyamata. A modell ellenőrzés segíthet a modell lopásának észlelésében és megelőzésében azáltal, hogy biztosítja, hogy a modell védett és hitelesített.
- **Kimeneti validáció**: Ez az AI rendszer vagy LLM kimenetének minőségének és megbízhatóságának validálásának folyamata. A kimeneti validáció segíthet a rosszindulatú manipuláció észlelésében és kijavításában azáltal, hogy biztosítja, hogy a kimenet következetes és pontos.

Az OpenAI, az AI rendszerek vezetője, egy sor _biztonsági értékelést_ állított fel a piros csapat hálózati kezdeményezés részeként, amelynek célja az AI rendszerek kimenetének tesztelése, az AI biztonságának hozzájárulása érdekében.

> Az értékelések egyszerű kérdés-válasz tesztektől összetettebb szimulációkig terjedhetnek. Konkrét példaként íme néhány értékelés, amelyeket az OpenAI fejlesztett ki az AI viselkedésének különböző szempontokból történő értékelésére:

#### Meggyőzés

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer másik AI rendszert rávenni arra, hogy kimondjon egy titkos szót?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer másik AI rendszert meggyőzni, hogy adományozzon pénzt?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer befolyásolni másik AI rendszer politikai javaslat támogatását?

#### Steganográfia (rejtett üzenetek)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer titkos üzeneteket átadni anélkül, hogy egy másik AI rendszer elkapná?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer üzeneteket tömöríteni és visszafejteni, hogy lehetővé tegye a titkos üzenetek elrejtését?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Mennyire tud egy AI rendszer koordinálni egy másik AI rendszerrel, közvetlen kommunikáció nélkül?

### AI Biztonság

Fontos, hogy megvédjük az AI rendszereket a rosszindulatú támadásoktól, visszaélésektől vagy nem szándékolt következményektől. Ez magában foglalja a biztonság, megbízhatóság és az AI rendszerek megbízhatóságának biztosítását, például:

- Az AI modellek képzésére és futtatására használt adatok és algoritmusok védelme
- Az AI rendszerek jogosulatlan hozzáférésének, manipulációjának vagy szabotálásának megelőzése
- Az AI rendszerekben található torzítások, diszkriminációk vagy etikai kérdések észlelése és mérséklése
- Az AI döntések és cselekvések elszámoltathatóságának, átláthatóságának és magyarázhatóságának biztosítása
- Az AI rendszerek céljainak és értékeinek összehangolása az emberek és a társadalom céljaival és értékeivel

Az AI biztonság fontos az AI rendszerek és adatok integritásának, elérhetőségének és bizalmasságának biztosítása érdekében. Az AI biztonságának néhány kihívása és lehetősége:

- Lehetőség: Az AI beépítése a kiberbiztonsági stratégiákba, mivel kulcsszerepet játszhat a fenyegetések azonosításában és a válaszidők javításában. Az AI segíthet automatizálni és kiegészíteni a kibertámadások, például adathalászat, rosszindulatú szoftverek vagy zsarolóvírusok észlelését és mérséklését.
- Kihívás: Az AI-t a támadók is használhatják kifinomult támadások indítására, például hamis vagy félrevezető tartalom generálására, felhasználók megszemélyesítésére vagy az AI rendszerek sebezhetőségeinek kihasználására. Ezért az AI fejlesztőknek egyedi felelősségük van olyan rendszerek tervezésében, amelyek robusztusak és ellenállóak a visszaélésekkel sz

**Felelősségi nyilatkozat**:  
Ezt a dokumentumot AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget semmilyen félreértésért vagy félremagyarázásért, amely e fordítás használatából ered.