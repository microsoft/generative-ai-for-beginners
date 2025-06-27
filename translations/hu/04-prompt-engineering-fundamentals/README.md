<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:18:51+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hu"
}
-->
# A Prompt Engineering Alapjai

## Bevezetés
Ez a modul a generatív AI modellek hatékony promptjainak létrehozásához szükséges alapvető fogalmakat és technikákat tárgyalja. Fontos, hogyan írjuk meg a promptot egy LLM-nek. Egy gondosan megfogalmazott prompt jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint a _prompt_ és a _prompt engineering_? És hogyan javíthatom a prompt _inputot_, amit az LLM-nek küldök? Ezek azok a kérdések, amelyeket ebben a fejezetben és a következőben megpróbálunk megválaszolni.

A _Generatív AI_ képes új tartalmakat (például szöveget, képeket, hangot, kódot stb.) létrehozni a felhasználói kérésekre válaszul. Ezt _Nagy Nyelvi Modellek_ (LLM-ek) segítségével éri el, mint például az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyet természetes nyelv és kód használatára képeztek ki.

A felhasználók most már ismerős paradigmák, például chat segítségével léphetnek kapcsolatba ezekkel a modellekkel, anélkül hogy technikai szakértelemre vagy képzésre lenne szükségük. A modellek _prompt-alapúak_ - a felhasználók szöveges inputot (promptot) küldenek, és visszakapják az AI választ (completion). Ezután "chatelhetnek az AI-val" iteratív módon, többfordulós beszélgetésekben, finomítva a promptot, amíg a válasz megfelel az elvárásaiknak.

A "promptok" most a generatív AI alkalmazások elsődleges _programozási interfészévé_ válnak, amelyek megmondják a modelleknek, mit kell tenniük, és befolyásolják a visszakapott válaszok minőségét. A "Prompt Engineering" egy gyorsan növekvő tanulmányi terület, amely a promptok _tervezésére és optimalizálására_ összpontosít, hogy következetes és minőségi válaszokat nyújtson nagy léptékben.

## Tanulási Célok

Ebben a leckében megtanuljuk, mi az a Prompt Engineering, miért fontos, és hogyan készíthetünk hatékonyabb promptokat egy adott modell és alkalmazási cél érdekében. Megértjük a prompt engineering alapfogalmait és legjobb gyakorlatait - és megismerkedünk egy interaktív Jupyter Notebooks "sandbox" környezettel, ahol láthatjuk, hogyan alkalmazzák ezeket a fogalmakat valós példákra.

A lecke végére képesek leszünk:

1. Elmagyarázni, mi a prompt engineering és miért fontos.
2. Leírni a prompt összetevőit és hogyan használják őket.
3. Megtanulni a prompt engineering legjobb gyakorlatait és technikáit.
4. Alkalmazni a tanult technikákat valós példákra, egy OpenAI végpont használatával.

## Kulcsfogalmak

Prompt Engineering: Az AI modellek irányítására szolgáló bemenetek tervezésének és finomításának gyakorlata a kívánt kimenetek előállítása érdekében.
Tokenizálás: A szöveg kisebb egységekre, úgynevezett tokenekre való átalakításának folyamata, amelyeket a modell megért és feldolgoz.
Instruction-Tuned LLM-ek: Nagy Nyelvi Modellek (LLM-ek), amelyeket konkrét utasításokkal finomhangoltak, hogy javítsák válaszaik pontosságát és relevanciáját.

## Tanulási Sandbox

A prompt engineering jelenleg inkább művészet, mint tudomány. A legjobb módja annak, hogy javítsuk az intuíciót, ha _gyakorolunk többet_, és egy próbálkozás-hibázás megközelítést alkalmazunk, amely ötvözi az alkalmazási terület szakértelmét az ajánlott technikákkal és modell-specifikus optimalizációkkal.

A lecke mellékelt Jupyter Notebookja egy _sandbox_ környezetet biztosít, ahol kipróbálhatjuk, amit tanulunk - menet közben vagy a kód kihívás részeként a végén. Az feladatok végrehajtásához szükség lesz:

1. **Egy Azure OpenAI API kulcs** - a telepített LLM szolgáltatási végpontja.
2. **Egy Python futtatási környezet** - amelyben a Notebook futtatható.
3. **Helyi környezeti változók** - _teljesítse most a [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) lépéseket, hogy készen álljon_.

A notebook _kezdő_ gyakorlatokkal érkezik - de bátorítjuk, hogy adjon hozzá saját _Markdown_ (leírás) és _Code_ (prompt kérések) szakaszokat, hogy kipróbáljon több példát vagy ötletet - és építse intuícióját a prompt tervezéshez.

## Illusztrált Útmutató

Szeretné látni, hogy milyen nagy kép van ebben a leckében, mielőtt belemerülne? Nézze meg ezt az illusztrált útmutatót, amely áttekintést nyújt a főbb témákról és a kulcsfontosságú tanulságokról, amelyeket minden egyes szakaszban érdemes átgondolni. A lecke útvonalterve elvezet a főbb fogalmak és kihívások megértésétől azok kezeléséig releváns prompt engineering technikákkal és legjobb gyakorlatokkal. Ne feledje, hogy az "Advanced Techniques" szakasz ebben az útmutatóban a következő fejezet tartalmára utal.

## A Startupunk

Most beszéljünk arról, hogyan kapcsolódik _ez a téma_ a startup küldetésünkhöz, hogy [AI innovációt hozzunk az oktatásba](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). AI-alapú alkalmazásokat szeretnénk építeni a _személyre szabott tanulás_ érdekében - így gondolkodjunk el azon, hogy alkalmazásunk különböző felhasználói hogyan "tervezhetik" a promptokat:

- **Adminisztrátorok** kérhetik az AI-t, hogy _elemezze a tantervi adatokat a lefedettségi hiányosságok azonosítása érdekében_. Az AI összefoglalhatja az eredményeket vagy vizualizálhatja őket kóddal.
- **Oktatók** kérhetik az AI-t, hogy _készítsen egy óratervet egy célközönség és téma számára_. Az AI személyre szabott tervet készíthet egy megadott formátumban.
- **Diákok** kérhetik az AI-t, hogy _tutorálja őket egy nehéz témában_. Az AI most már irányíthatja a diákokat órákkal, tippekkel és példákkal az ő szintjüknek megfelelően.

Ez csak a jéghegy csúcsa. Nézze meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - egy nyílt forráskódú prompt könyvtárat, amelyet oktatási szakértők kuráltak - hogy szélesebb képet kapjon a lehetőségekről! _Próbáljon ki néhányat ezek közül a promptok közül a sandboxban vagy az OpenAI Playgroundban, hogy lássa, mi történik!_

## Mi az a Prompt Engineering?

Ezt a leckét úgy kezdtük, hogy a **Prompt Engineering**-et a szöveges bemenetek (promptok) _tervezési és optimalizálási_ folyamataként definiáltuk, hogy következetes és minőségi válaszokat (completions) nyújtsanak egy adott alkalmazási cél és modell esetében. Ezt egy kétlépéses folyamatként képzelhetjük el:

- _tervezni_ az első promptot egy adott modellhez és célhoz
- _finomítani_ a promptot iteratívan a válasz minőségének javítása érdekében

Ez szükségszerűen egy próbálkozás-hibázás folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmények eléréséhez. Miért fontos ez? A válaszhoz először három fogalmat kell megértenünk:

- _Tokenizálás_ = hogyan látja a modell a promptot
- _Alap LLM-ek_ = hogyan dolgozza fel az alapmodell a promptot
- _Instruction-Tuned LLM-ek_ = hogyan láthatja a modell a "feladatokat"

### Tokenizálás

Egy LLM promptokat _tokenek sorozataként_ lát, ahol különböző modellek (vagy egy modell verziói) különböző módon tokenizálhatják ugyanazt a promptot. Mivel az LLM-ek tokeneken (és nem nyers szövegen) vannak kiképezve, a promptok tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Hogy intuíciót szerezzünk a tokenizálás működéséről, próbáljunk ki olyan eszközöket, mint az alábbi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Másolja be a promptját - és nézze meg, hogyan alakul át tokenekké, figyelje meg, hogyan kezelik a szóköz karaktereket és írásjeleket. Ne feledje, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat - így ha ezt egy újabb modellel próbálja, más eredményt hozhat.

### Fogalom: Alapmodellek

Miután egy prompt tokenizálódott, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Alapmodell) elsődleges funkciója, hogy megjósolja a tokeneket abban a sorozatban. Mivel az LLM-ek hatalmas szöveges adathalmazokon vannak kiképezve, jó érzékük van a tokenek közötti statisztikai kapcsolatokhoz, és némi magabiztossággal tudják megtenni ezt a jóslatot. Ne feledje, hogy nem értik a szavak _jelentését_ a promptban vagy tokenben; csak egy mintát látnak, amit "befejezhetnek" a következő jóslatukkal. Folytathatják a sorozat jóslását, amíg a felhasználó közbe nem avatkozik vagy valamilyen előre meghatározott feltétel nem szünteti meg.

Szeretné látni, hogyan működik a prompt-alapú befejezés? Írja be a fenti promptot az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) alapértelmezett beállításokkal. A rendszer úgy van konfigurálva, hogy a promptokat információkérésként kezelje - így látnia kell egy befejezést, amely kielégíti ezt a kontextust.

De mi van akkor, ha a felhasználó valami konkrétat szeretne látni, ami megfelel bizonyos kritériumoknak vagy feladat célkitűzésnek? Itt jönnek képbe az _instruction-tuned_ LLM-ek.

### Fogalom: Instruction Tuned LLM-ek

Egy [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezdődik, és példákkal vagy input/output párokkal (például többfordulós "üzenetekkel") finomhangolja, amelyek egyértelmű utasításokat tartalmazhatnak - és az AI válasz kísérletet tesz ezen utasítás követésére.

Ez olyan technikákat használ, mint a Reinforcement Learning with Human Feedback (RLHF), amelyek képesek kiképezni a modellt, hogy _kövesse az utasításokat_ és _tanuljon a visszajelzésekből_, így olyan válaszokat hoz létre, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és relevánsabbak a felhasználói célkitűzésekhez.

Próbáljuk ki - térjünk vissza a fenti prompthoz, de most változtassuk meg a _rendszerüzenetet_, hogy az alábbi utasítást adja meg kontextusként:

> _Foglalja össze a kapott tartalmat egy másodikos tanuló számára. Tartsa az eredményt egy bekezdésben, 3-5 ponttal._

Látja, hogy az eredmény most a kívánt célt és formát tükrözi? Egy oktató most közvetlenül használhatja ezt a választ az óráinak diáiban.

## Miért van szükségünk Prompt Engineeringre?

Most, hogy tudjuk, hogyan dolgozzák fel a promptokat az LLM-ek, beszéljünk arról, hogy _miért_ van szükségünk prompt engineeringre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek miatt _megbízható és következetes befejezések_ nehezebben érhetők el, ha nem fektetünk erőfeszítést a prompt megalkotásába és optimalizálásába. Például:

1. **A modell válaszai sztochasztikusak.** Az _ugyanaz a prompt_ valószínűleg különböző válaszokat fog eredményezni különböző modellekkel vagy modell verziókkal. És még az _ugyanazon modell_ is különböző időpontokban eltérő eredményeket hozhat. _A prompt engineering technikák segíthetnek minimalizálni ezeket a variációkat jobb korlátok biztosításával_.

1. **A modellek hamis válaszokat generálhatnak.** A modellek _nagy, de véges_ adathalmazokkal vannak előre kiképezve, ami azt jelenti, hogy nem rendelkeznek tudással a képzési hatókörön kívüli fogalmakról. Ennek eredményeként olyan befejezéseket hozhatnak létre, amelyek pontatlanok, képzeletbeliak vagy közvetlenül ellentmondanak a jól ismert tényeknek. _A prompt engineering technikák segítenek a felhasználóknak az ilyen hamisítások azonosításában és enyhítésében, például az AI-tól való idézetek vagy érvelés kérése révén_.

1. **A modellek képességei eltérőek lesznek.** Az újabb modellek vagy modell generációk gazdagabb képességekkel rendelkeznek, de egyedi furcsaságokat és kompromisszumokat is hoznak a költségek és a komplexitás terén. _A prompt engineering segíthet a legjobb gyakorlatok és munkafolyamatok kifejlesztésében, amelyek elvonják a különbségeket, és alkalmazkodnak a modell-specifikus követelményekhez skálázható, zökkenőmentes módon_.

Lássuk ezt a gyakorlatban az OpenAI vagy Azure OpenAI Playgroundban:

- Használja ugyanazt a promptot különböző LLM telepítésekkel (például OpenAI, Azure OpenAI, Hugging Face) - látta a variációkat?
- Használja ugyanazt a promptot többször az _ugyanazon_ LLM telepítéssel (például Azure OpenAI playground) - hogyan különböztek ezek a variációk?

### Hamisítások Példa

Ebben a kurzusban a **"hamisítás"** kifejezést használjuk arra a jelenségre, amikor az LLM-ek néha tényszerűen helytelen információkat generálnak a képzésük korlátai vagy más korlátok miatt. Lehet, hogy ezt _"hallucinációknak"_ nevezték népszerű cikkekben vagy kutatási tanulmányokban. Azonban erősen ajánljuk a _"hamisítás"_ kifejezés használatát, hogy ne antropomorfizáljuk a viselkedést azáltal, hogy emberi tulajdonságot tulajdonítunk egy gépi eredménynek. Ez szintén megerősíti a [Responsible AI irányelveket](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminológiai szemp
Végül a sablonok igazi értéke abban rejlik, hogy képesek _prompt könyvtárakat_ létrehozni és publikálni vertikális alkalmazási területek számára - ahol a prompt sablon most már _optimalizált_, hogy tükrözze az alkalmazás-specifikus kontextust vagy példákat, amelyek a válaszokat relevánsabbá és pontosabbá teszik a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repozitórium remek példa erre a megközelítésre, amely egy könyvtárat kurál az oktatási területre vonatkozóan, hangsúlyozva a kulcsfontosságú célokat, mint a tantervezés, tantervfejlesztés, diákok oktatása stb.

## Támogató Tartalom

Ha a prompt szerkesztést úgy tekintjük, mint amelynek van egy utasítása (feladat) és egy célja (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan további kontextus, amelyet azért biztosítunk, hogy **valamilyen módon befolyásoljuk a kimenetet**. Lehetnek ezek hangolási paraméterek, formázási utasítások, téma taxonómiák stb., amelyek segíthetnek a modellnek _személyre szabni_ a válaszát, hogy megfeleljen a kívánt felhasználói céloknak vagy elvárásoknak.

Például: Adott egy kurzuskatalógus kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető kurzusról a tantervben:

- megadhatunk egy utasítást a "kurzuskatalógus összefoglalására a 2023-as őszi szemeszterre"
- használhatjuk az elsődleges tartalmat néhány példa biztosítására a kívánt kimenetre
- használhatjuk a másodlagos tartalmat az érdeklődésre számot tartó 5 legfontosabb "címke" azonosítására.

Most a modell biztosíthat egy összefoglalót a néhány példa által mutatott formátumban - de ha egy eredmény több címkével rendelkezik, prioritást adhat az 5, másodlagos tartalomban azonosított címkének.

---

<!--
LECKE SABLON:
Ez az egység az alapvető koncepció #1-et kell, hogy lefedje.
Erősítse meg a koncepciót példákkal és hivatkozásokkal.

KONCEPCIÓ #3:
Prompt Műszaki Technikák.
Melyek az alapvető technikák a prompt műszaki tervezéshez?
Illusztrálja néhány gyakorlattal.
-->

## Promptolási Legjobb Gyakorlatok

Most, hogy tudjuk, hogyan lehet a promtokat _felépíteni_, elkezdhetünk gondolkodni azon, hogyan _tervezzük_ meg őket a legjobb gyakorlatok tükrözése érdekében. Két részre oszthatjuk ezt - a megfelelő _gondolkodásmód_ és a megfelelő _technikák_ alkalmazása.

### Prompt Műszaki Gondolkodásmód

A prompt műszaki tervezés egy próbálkozás és hibázás folyamat, ezért tartson szem előtt három széles irányadó tényezőt:

1. **A terület megértése számít.** A válasz pontossága és relevanciája annak a _területnek_ a függvénye, amelyben az alkalmazás vagy felhasználó működik. Alkalmazza intuícióját és területi szakértelmét a **technikák testreszabására**. Például határozza meg a _területspecifikus személyiségeket_ a rendszer promtjaiban, vagy használjon _területspecifikus sablonokat_ a felhasználói promtokban. Biztosítson másodlagos tartalmat, amely tükrözi a területspecifikus kontextusokat, vagy használjon _területspecifikus jeleket és példákat_, hogy a modellt a megszokott használati minták felé terelje.

2. **A modell megértése számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk is eltérhetnek az általuk használt képzési adathalmaz (előre betanított tudás), az általuk biztosított képességek (például API vagy SDK révén) és az optimalizált tartalom típusa (például kód vs. képek vs. szöveg) tekintetében. Értse meg az Ön által használt modell erősségeit és korlátait, és használja ezt a tudást a _feladatok prioritizálására_ vagy _testreszabott sablonok_ építésére, amelyek optimalizáltak a modell képességeihez.

3. **Iteráció és validálás számít.** A modellek gyorsan fejlődnek, és így a prompt műszaki technikák is. Mint területi szakértő, lehet, hogy más kontextusa vagy kritériumai vannak az _Ön_ konkrét alkalmazásának, amelyek nem vonatkoznak a szélesebb közösségre. Használja a prompt műszaki eszközöket és technikákat a prompt szerkesztés "beindításához", majd iterálja és validálja az eredményeket saját intuíciója és területi szakértelme alapján. Rögzítse meglátásait, és hozzon létre egy **tudásbázist** (például prompt könyvtárakat), amelyet mások új alapként használhatnak a gyorsabb iterációkhoz a jövőben.

## Legjobb Gyakorlatok

Most nézzük meg a közös legjobb gyakorlatokat, amelyeket az [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és az [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakemberei ajánlanak.

| Mi                                | Miért                                                                                                                                                                                                                                               |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Értékelje a legújabb modelleket.  | Az új modellgenerációk valószínűleg javított funkciókkal és minőséggel rendelkeznek - de magasabb költségekkel is járhatnak. Értékelje őket a hatásuk alapján, majd hozzon döntéseket a migrációról.                                                 |
| Válassza külön az utasításokat és a kontextust | Ellenőrizze, hogy a modell/szolgáltató definiál-e _határolókat_ az utasítások, elsődleges és másodlagos tartalom egyértelműbb megkülönböztetésére. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                                      |
| Legyen specifikus és világos      | Adjon több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és konzisztenciáját. Rögzítse a recepteket újrafelhasználható sablonokban.                                       |
| Legyen leíró, használjon példákat | A modellek jobban reagálhatnak a "mutasd és mondd" megközelítésre. Kezdje egy `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` értékekkel. Térjen vissza a [Tanulási Homokozó szakaszhoz](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), hogy megtanulja hogyan.

### Ezután nyissa meg a Jupyter Notebookot

- Válassza ki a futási kernelt. Ha az 1. vagy 2. opciót használja, egyszerűen válassza a fejlesztői konténer által biztosított alapértelmezett Python 3.10.x kernelt.

Minden készen áll a gyakorlatok futtatására. Vegye figyelembe, hogy itt nincsenek _jó és rossz_ válaszok - csak a lehetőségek próbálgatása próbálkozás és hibázás útján, és intuíció építése arról, hogy mi működik egy adott modell és alkalmazási terület esetében.

_Ezért ebben a leckében nincsenek Kód Megoldás szegmensek. Ehelyett a Notebooknak lesznek Markdown cellái "Az én megoldásom:" címmel, amelyek egy példakimenetet mutatnak referenciaként._

<!--
LECKE SABLON:
Zárja le a szakaszt egy összefoglalóval és az önálló tanuláshoz szükséges forrásokkal.
-->

## Tudásellenőrzés

Melyik a következő közül egy jó prompt, amely megfelel néhány ésszerű legjobb gyakorlatnak?

1. Mutass nekem egy piros autót
2. Mutass nekem egy piros Volvo XC90 típusú autót, amely egy szikla mellett parkol, miközben a nap lemegy
3. Mutass nekem egy piros Volvo XC90 típusú autót

A: 2, ez a legjobb prompt, mivel részleteket ad "miről" van szó, és specifikus részletekbe megy (nem csak bármilyen autó, hanem egy konkrét márka és típus), és az általános környezetet is leírja. A 3 a következő legjobb, mivel szintén sok leírást tartalmaz.

## 🚀 Kihívás

Nézze meg, hogy tudja-e használni a "jel" technikát a következő prompttal: Egészítse ki a mondatot "Mutass nekem egy piros Volvo márkájú autót és ". Mit válaszol, és hogyan javítaná?

## Nagyszerű Munka! Folytassa a Tanulást

Szeretne többet megtudni a különböző Prompt Műszaki koncepciókról? Látogasson el a [folytatott tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy más nagyszerű forrásokat találjon ebben a témában.

Lépjen tovább az 5. leckére, ahol megnézzük a [haladó promptolási technikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével lett lefordítva. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.