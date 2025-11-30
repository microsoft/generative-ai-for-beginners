<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T21:25:18+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "hu"
}
-->
# Generatív AI alkalmazások biztonságának megőrzése

[![Generatív AI alkalmazások biztonságának megőrzése](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.hu.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Bevezetés

Ebben a leckében szó lesz:

- A biztonságról az AI rendszerek kontextusában.
- Az AI rendszereket érintő gyakori kockázatokról és fenyegetésekről.
- Az AI rendszerek biztonságának megőrzésére szolgáló módszerekről és szempontokról.

## Tanulási célok

A lecke elvégzése után megérted:

- Az AI rendszereket érintő fenyegetéseket és kockázatokat.
- Az AI rendszerek biztonságának megőrzésére szolgáló gyakori módszereket és gyakorlatokat.
- Hogyan előzheted meg a nem várt eredményeket és a felhasználói bizalom csökkenését biztonsági tesztelés alkalmazásával.

## Mit jelent a biztonság a generatív AI kontextusában?

Ahogy a mesterséges intelligencia (AI) és a gépi tanulás (ML) technológiái egyre inkább formálják életünket, elengedhetetlen, hogy ne csak az ügyféladatokat, hanem magukat az AI rendszereket is megvédjük. Az AI/ML egyre gyakrabban támogatja a nagy értékű döntéshozatali folyamatokat olyan iparágakban, ahol a rossz döntések súlyos következményekkel járhatnak.

Íme néhány kulcsfontosságú szempont:

- **AI/ML hatása**: Az AI/ML jelentős hatással van a mindennapi életre, ezért elengedhetetlen ezek védelme.
- **Biztonsági kihívások**: Az AI/ML hatása megfelelő figyelmet igényel, hogy megvédjük az AI-alapú termékeket a kifinomult támadásoktól, legyenek azok trollok vagy szervezett csoportok által végrehajtottak.
- **Stratégiai problémák**: A technológiai iparnak proaktívan kell kezelnie a stratégiai kihívásokat, hogy hosszú távon biztosítsa az ügyfelek biztonságát és az adatok védelmét.

Ezenkívül a gépi tanulási modellek nagyrészt képtelenek megkülönböztetni a rosszindulatú bemenetet a jóindulatú, szokatlan adatoktól. Az edzéshez használt adatok jelentős része nem ellenőrzött, moderálatlan, nyilvános adatbázisokból származik, amelyekhez harmadik felek is hozzájárulhatnak. A támadóknak nem kell feltörniük az adatbázisokat, ha szabadon hozzájárulhatnak hozzájuk. Idővel az alacsony megbízhatóságú rosszindulatú adatok magas megbízhatóságú, megbízható adatokká válhatnak, ha az adatszerkezet/formátum helyes marad.

Ezért kritikus fontosságú biztosítani a modellek döntéseihez használt adattárolók integritását és védelmét.

## Az AI fenyegetéseinek és kockázatainak megértése

Az AI és a kapcsolódó rendszerek tekintetében az adatmérgezés ma a legjelentősebb biztonsági fenyegetés. Az adatmérgezés akkor következik be, amikor valaki szándékosan megváltoztatja az AI edzéséhez használt információkat, hibás működést okozva. Ez a szabványosított észlelési és enyhítési módszerek hiánya, valamint a nem megbízható vagy nem ellenőrzött nyilvános adatbázisokra való támaszkodás miatt történik. Az adatintegritás fenntartása és a hibás edzési folyamat megelőzése érdekében elengedhetetlen az adatok eredetének és származásának nyomon követése. Ellenkező esetben az „amit beviszel, azt kapod” régi mondás igaz marad, ami a modell teljesítményének romlásához vezet.

Íme néhány példa arra, hogyan befolyásolhatja az adatmérgezés a modelleket:

1. **Címke megfordítása**: Egy bináris osztályozási feladatban egy támadó szándékosan megfordítja az edzési adatok egy kis részének címkéit. Például a jóindulatú mintákat rosszindulatúként címkézik, ami miatt a modell helytelen társításokat tanul.\
   **Példa**: Egy spam szűrő, amely manipulált címkék miatt tévesen osztályozza a legitim e-maileket spamként.
2. **Jellemző mérgezés**: Egy támadó finoman módosítja az edzési adatok jellemzőit, hogy elfogultságot vezessen be vagy félrevezesse a modellt.\
   **Példa**: Jelentéktelen kulcsszavak hozzáadása termékleírásokhoz, hogy manipulálják az ajánlórendszereket.
3. **Adat injekció**: Rosszindulatú adatok bejuttatása az edzési készletbe, hogy befolyásolják a modell viselkedését.\
   **Példa**: Hamis felhasználói vélemények bevezetése, hogy torzítsák az érzelemelemzés eredményeit.
4. **Hátsó ajtós támadások**: Egy támadó rejtett mintát (hátsó ajtót) helyez el az edzési adatokban. A modell megtanulja felismerni ezt a mintát, és rosszindulatúan viselkedik, amikor aktiválják.\
   **Példa**: Egy arcfelismerő rendszer, amely hátsó ajtós képekkel edzett, és egy adott személyt tévesen azonosít.

A MITRE Corporation létrehozta az [ATLAS-t (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), amely egy tudásbázis az AI rendszerek elleni valós támadások során alkalmazott taktikákról és technikákról.

> Az AI-alapú rendszerekben egyre több sebezhetőség jelenik meg, mivel az AI beépítése növeli a meglévő rendszerek támadási felületét a hagyományos kibertámadásokon túl. Az ATLAS-t azért fejlesztettük ki, hogy felhívjuk a figyelmet ezekre az egyedi és folyamatosan fejlődő sebezhetőségekre, mivel a globális közösség egyre inkább beépíti az AI-t különböző rendszerekbe. Az ATLAS a MITRE ATT&CK® keretrendszer mintájára készült, és taktikái, technikái, valamint eljárásai (TTP-k) kiegészítik az ATT&CK-ban találhatókat.

Hasonlóan a MITRE ATT&CK® keretrendszerhez, amelyet széles körben használnak a hagyományos kiberbiztonságban fejlett fenyegetés-emulációs forgatókönyvek tervezésére, az ATLAS könnyen kereshető TTP-ket kínál, amelyek segítenek jobban megérteni és felkészülni a feltörekvő támadások elleni védekezésre.

Ezenkívül az Open Web Application Security Project (OWASP) létrehozott egy "[Top 10 listát](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" a LLM-eket használó alkalmazásokban található legkritikusabb sebezhetőségekről. A lista kiemeli az olyan fenyegetések kockázatait, mint az említett adatmérgezés, valamint másokat, például:

- **Prompt Injection**: egy technika, amelyben a támadók gondosan megfogalmazott bemenetekkel manipulálják a Nagy Nyelvi Modelleket (LLM), hogy azok a szándékolt viselkedésen kívül működjenek.
- **Ellátási lánc sebezhetőségek**: Az LLM-eket használó alkalmazások összetevői és szoftverei, például Python modulok vagy külső adatbázisok, maguk is kompromittálódhatnak, ami váratlan eredményeket, bevezetett elfogultságokat és akár az alapvető infrastruktúrában lévő sebezhetőségeket is okozhat.
- **Túlzott támaszkodás**: Az LLM-ek hibásak lehetnek, és hajlamosak „hallucinálni”, pontatlan vagy nem biztonságos eredményeket adva. Számos dokumentált esetben az emberek az eredményeket készpénznek vették, ami nem szándékolt negatív következményekhez vezetett a való világban.

A Microsoft Cloud Advocate Rod Trent írt egy ingyenes e-könyvet, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), amely mélyen belemerül ezekbe és más feltörekvő AI fenyegetésekbe, és átfogó útmutatást nyújt arról, hogyan lehet a legjobban kezelni ezeket a helyzeteket.

## Biztonsági tesztelés AI rendszerek és LLM-ek számára

A mesterséges intelligencia (AI) számos területet és iparágat átalakít, új lehetőségeket és előnyöket kínálva a társadalom számára. Azonban az AI jelentős kihívásokat és kockázatokat is jelent, mint például az adatvédelem, az elfogultság, a magyarázhatóság hiánya és a potenciális visszaélés. Ezért elengedhetetlen, hogy az AI rendszerek biztonságosak és felelősségteljesek legyenek, azaz megfeleljenek az etikai és jogi normáknak, és megbízhatóak legyenek a felhasználók és érintettek számára.

A biztonsági tesztelés az AI rendszer vagy LLM biztonságának értékelésének folyamata, amely során azonosítják és kihasználják azok sebezhetőségeit. Ezt a fejlesztők, felhasználók vagy harmadik fél által megbízott auditorok végezhetik, a tesztelés céljától és terjedelmétől függően. Az AI rendszerek és LLM-ek leggyakoribb biztonsági tesztelési módszerei a következők:

- **Adattisztítás**: Ez az érzékeny vagy személyes információk eltávolításának vagy anonimizálásának folyamata az AI rendszer vagy LLM edzési adataiból vagy bemenetéből. Az adattisztítás segíthet megelőzni az adatvesztést és a rosszindulatú manipulációt azáltal, hogy csökkenti a bizalmas vagy személyes adatok kitettségét.
- **Adverzárius tesztelés**: Ez az adverzárius példák generálásának és alkalmazásának folyamata az AI rendszer vagy LLM bemenetére vagy kimenetére, hogy értékeljék annak robusztusságát és ellenállóképességét az adverzárius támadásokkal szemben. Az adverzárius tesztelés segíthet az AI rendszer vagy LLM sebezhetőségeinek és gyengeségeinek azonosításában és enyhítésében, amelyeket a támadók kihasználhatnak.
- **Modell ellenőrzés**: Ez az AI rendszer vagy LLM modellparamétereinek vagy architektúrájának helyességének és teljességének ellenőrzési folyamata. A modell ellenőrzés segíthet a modell lopásának észlelésében és megelőzésében azáltal, hogy biztosítja a modell védelmét és hitelesítését.
- **Kimenet ellenőrzés**: Ez az AI rendszer vagy LLM kimenetének minőségének és megbízhatóságának ellenőrzési folyamata. A kimenet ellenőrzés segíthet a rosszindulatú manipuláció észlelésében és kijavításában azáltal, hogy biztosítja a kimenet következetességét és pontosságát.

Az OpenAI, az AI rendszerek egyik vezetője, egy sor _biztonsági értékelést_ állított fel a red teaming hálózati kezdeményezés részeként, amelynek célja az AI rendszerek kimenetének tesztelése, hogy hozzájáruljon az AI biztonságához.

> Az értékelések egyszerű kérdezz-felelek tesztektől összetettebb szimulációkig terjedhetnek. Konkrét példaként itt vannak az OpenAI által kidolgozott mintavizsgálatok, amelyek az AI viselkedését több szempontból értékelik:

#### Meggyőzés

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer rávenni egy másik AI rendszert, hogy kimondjon egy titkos szót?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer meggyőzni egy másik AI rendszert, hogy pénzt adományozzon?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer befolyásolni egy másik AI rendszer támogatását egy politikai javaslat iránt?

#### Steganográfia (rejtett üzenetküldés)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer titkos üzeneteket átadni anélkül, hogy egy másik AI rendszer észrevenné?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer üzeneteket tömöríteni és visszafejteni, hogy lehetővé tegye titkos üzenetek rejtését?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Mennyire jól tud egy AI rendszer koordinálni egy másik AI rendszerrel közvetlen kommunikáció nélkül?

### AI Biztonság

Elengedhetetlen, hogy megvédjük az AI rendszereket a rosszindulatú támadásoktól, visszaélésektől vagy nem szándékolt következményektől. Ez magában foglalja az AI rendszerek biztonságának, megbízhatóságának és hitelességének biztosítását, például:

- Az AI modellek edzéséhez és futtatásához használt adatok és algoritmusok védelme
- Az AI rendszerek jogosulatlan hozzáférésének, manipulációjának vagy szabotázsának megelőzése
- Az AI rendszerekben lévő elfogultság, diszkrimináció vagy etikai problémák észlelése és enyhítése
- Az AI döntések és cselekvések elszámoltathatóságának, átláthatóságának és magyarázhatóságának biztosítása
- Az AI rendszerek céljainak és értékeinek összehangolása az emberek és a társadalom céljaival és értékeivel

Az AI biztonság fontos az AI rendszerek és adatok integritásának, elérhetőségének és titkosságának biztosítása érdekében. Az AI biztonságának kihívásai és lehetőségei közé tartozik:

- Lehetőség: Az AI beépítése a kiberbiztonsági stratégiákba, mivel kulcsszerepet játszhat a fenyegetések azonosításában és a válaszidők javításában. Az AI segíthet automatizálni és kiegészíteni a kibertámadások, például adathalászat, rosszindulatú programok vagy zsarolóprogramok észlelését és enyhítését.
- Kihívás: Az AI-t az ellenfelek is használhatják kifinomult támadások indítására, például hamis vagy félrevezető tartalom generálására
A valós fenyegetések szimulálása ma már standard gyakorlatnak számít az ellenállóképes mesterséges intelligencia rendszerek építésében, amely során hasonló eszközöket, taktikákat és eljárásokat alkalmaznak a rendszerek kockázatainak azonosítására és a védők reakcióinak tesztelésére.

> Az AI red teaming gyakorlata kibővült, és már nemcsak a biztonsági sebezhetőségek feltárását foglalja magában, hanem más rendszerhibák vizsgálatát is, például potenciálisan káros tartalmak generálását. Az AI rendszerek új kockázatokkal járnak, és a red teaming kulcsfontosságú ezeknek az új kockázatoknak a megértésében, mint például a prompt injection és a megalapozatlan tartalmak előállítása. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Útmutató és források a red teaminghez](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.hu.png)]()

Az alábbiakban bemutatjuk azokat a kulcsfontosságú felismeréseket, amelyek formálták a Microsoft AI Red Team programját.

1. **Az AI Red Teaming kiterjesztett hatóköre:**
   Az AI red teaming most már magában foglalja mind a biztonsági, mind a Felelős AI (RAI) eredményeket. Hagyományosan a red teaming a biztonsági aspektusokra összpontosított, a modellt vektorként kezelve (pl. az alapmodell ellopása). Az AI rendszerek azonban új biztonsági sebezhetőségeket vezetnek be (pl. prompt injection, mérgezés), amelyek különös figyelmet igényelnek. A biztonságon túl az AI red teaming a méltányossági kérdéseket (pl. sztereotipizálás) és a káros tartalmakat (pl. erőszak dicsőítése) is vizsgálja. Ezeknek a problémáknak a korai azonosítása lehetővé teszi a védelmi beruházások prioritásának meghatározását.
2. **Rosszindulatú és jóindulatú hibák:**
   Az AI red teaming a hibákat mind rosszindulatú, mind jóindulatú szempontból vizsgálja. Például, amikor a Bing új verzióját teszteljük, nemcsak azt vizsgáljuk, hogyan tudják rosszindulatú támadók aláásni a rendszert, hanem azt is, hogyan találkozhatnak hétköznapi felhasználók problémás vagy káros tartalommal. A hagyományos biztonsági red teaming főként rosszindulatú szereplőkre összpontosít, míg az AI red teaming szélesebb körű személyiségeket és potenciális hibákat vesz figyelembe.
3. **Az AI rendszerek dinamikus természete:**
   Az AI alkalmazások folyamatosan fejlődnek. A nagy nyelvi modell alkalmazások esetében a fejlesztők alkalmazkodnak a változó követelményekhez. A folyamatos red teaming biztosítja az állandó éberséget és az alkalmazkodást az újonnan felmerülő kockázatokhoz.

Az AI red teaming nem mindenre kiterjedő megoldás, és kiegészítő mozgásként kell tekinteni más kontrollok mellett, mint például a [szerepkör-alapú hozzáférés-vezérlés (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) és átfogó adatkezelési megoldások. Célja, hogy kiegészítse egy olyan biztonsági stratégiát, amely a biztonságos és felelős AI megoldások alkalmazására összpontosít, figyelembe véve a magánélet és a biztonság szempontjait, miközben törekszik minimalizálni az elfogultságokat, káros tartalmakat és félretájékoztatást, amelyek alááshatják a felhasználói bizalmat.

Íme néhány további olvasnivaló, amely segíthet jobban megérteni, hogyan segíthet a red teaming az AI rendszerek kockázatainak azonosításában és enyhítésében:

- [Red teaming tervezése nagy nyelvi modellek (LLM-ek) és alkalmazásaik számára](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Mi az OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Kulcsfontosságú gyakorlat a biztonságosabb és felelősebb AI megoldások építéséhez](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), egy tudásbázis a mesterséges intelligencia rendszerek elleni valós támadások során alkalmazott taktikákról és technikákról.

## Tudásellenőrzés

Mi lehet egy jó megközelítés az adatintegritás fenntartására és a visszaélések megelőzésére?

1. Erős szerepkör-alapú kontrollok alkalmazása az adathozzáférés és adatkezelés terén  
1. Az adatok címkézésének megvalósítása és auditálása az adatok félreértelmezésének vagy visszaélésének megelőzése érdekében  
1. Biztosítsa, hogy AI infrastruktúrája támogatja a tartalomszűrést  

A:1, Bár mindhárom nagyszerű ajánlás, azzal, hogy biztosítja a megfelelő adathozzáférési jogosultságok kiosztását a felhasználóknak, nagyban hozzájárulhat az LLM-ek által használt adatok manipulációjának és félreértelmezésének megelőzéséhez.

## 🚀 Kihívás

Olvasson többet arról, hogyan [kormányozhatja és védheti az érzékeny információkat](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) az AI korában.

## Nagyszerű munka, folytassa a tanulást

A lecke befejezése után tekintse meg [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI ismereteit!

Lépjen tovább a 14. leckére, ahol [a Generatív AI alkalmazás életciklusát](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst) fogjuk megvizsgálni!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.