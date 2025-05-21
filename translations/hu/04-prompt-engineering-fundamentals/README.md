<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:10:29+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hu"
}
-->
# Prompt Engineering Alapok

## Bevezetés
Ez a modul alapvető fogalmakat és technikákat ismertet, amelyek hatékony promptok létrehozásához szükségesek a generatív AI modellekben. Az is számít, hogyan írjuk meg a promptot egy LLM-nek. Egy gondosan megfogalmazott prompt jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint a _prompt_ és a _prompt mérnökség_? És hogyan tudom javítani a prompt _bemenetet_, amit az LLM-nek küldök? Ezekre a kérdésekre próbálunk válaszokat adni ebben a fejezetben és a következőben.

A _Generatív AI_ képes új tartalmat létrehozni (például szöveget, képeket, hangot, kódot stb.) a felhasználói kérésekre reagálva. Ezt _Nagy Nyelvi Modellek_ (LLM) segítségével éri el, mint az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyeket természetes nyelv és kód használatára képeztek ki.

A felhasználók mostantól ismerős paradigmák, például chat segítségével léphetnek kapcsolatba ezekkel a modellekkel, anélkül, hogy technikai szakértelemre vagy képzésre lenne szükségük. A modellek _prompt-alapúak_ - a felhasználók szöveges bemenetet (promptot) küldenek, és visszakapják az AI választ (kiegészítést). Ezután iteratív módon "beszélgethetnek az AI-val" többfordulós beszélgetésekben, finomítva a promptot, amíg a válasz megfelel az elvárásaiknak.

A "promptok" most a generatív AI alkalmazások elsődleges _programozási interfészévé_ válnak, amelyek megmondják a modelleknek, mit kell tenniük, és befolyásolják a visszakapott válaszok minőségét. A "Prompt Mérnökség" egy gyorsan növekvő tanulmányi terület, amely a promptok _tervezésére és optimalizálására_ összpontosít, hogy konzisztens és minőségi válaszokat nyújtson nagy léptékben.

## Tanulási Célok

Ebben a leckében megtanuljuk, mi az a Prompt Mérnökség, miért fontos, és hogyan készíthetünk hatékonyabb promptokat egy adott modellhez és alkalmazási célhoz. Megértjük a prompt mérnökség alapfogalmait és legjobb gyakorlatait - és megismerkedünk egy interaktív Jupyter Notebooks "sandbox" környezettel, ahol ezek a fogalmak valós példákra alkalmazhatók.

A lecke végére képesek leszünk:

1. Elmagyarázni, mi a prompt mérnökség és miért fontos.
2. Leírni a promptok összetevőit és azok használatát.
3. Megtanulni a prompt mérnökség legjobb gyakorlatait és technikáit.
4. Alkalmazni a megtanult technikákat valós példákra, egy OpenAI végpont használatával.

## Kulcsfogalmak

Prompt Mérnökség: A gyakorlat, amely a bemenetek tervezésére és finomítására irányul, hogy az AI modelleket a kívánt kimenetek előállítására irányítsa.
Tokenizálás: Az a folyamat, amely a szöveget kisebb egységekké, úgynevezett tokenekké alakítja, amelyeket a modell megérthet és feldolgozhat.
Instrukcióra Hangolt LLM-ek: Nagy Nyelvi Modellek (LLM-ek), amelyeket speciális utasításokkal finomítottak a válaszok pontosságának és relevanciájának javítása érdekében.

## Tanulási Sandbox

A prompt mérnökség jelenleg inkább művészet, mint tudomány. A legjobb módja annak, hogy javítsuk a vele kapcsolatos intuícióinkat, ha _többet gyakorlunk_, és egy próbálgatásos megközelítést alkalmazunk, amely ötvözi az alkalmazási terület szakértelmét az ajánlott technikákkal és modell-specifikus optimalizálásokkal.

A leckéhez tartozó Jupyter Notebook egy _sandbox_ környezetet biztosít, ahol kipróbálhatod, amit tanulsz - menet közben vagy a végén lévő kód kihívás részeként. Az gyakorlatok végrehajtásához szükséged lesz:

1. **Egy Azure OpenAI API kulcsra** - a telepített LLM szolgáltatási végpontja.
2. **Egy Python futtatási környezetre** - amelyben a Notebook futtatható.
3. **Helyi környezeti változókra** - _fejezd be a [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) lépéseket most, hogy készen állj_.

A notebook _kezdő_ gyakorlatokat tartalmaz - de bátorítunk, hogy adj hozzá saját _Markdown_ (leírás) és _Code_ (prompt kérések) szekciókat, hogy kipróbálj több példát vagy ötletet - és építsd az intuíciódat a prompt tervezéséhez.

## Illusztrált Útmutató

Szeretnéd megkapni a nagy képet arról, hogy mit tartalmaz ez a lecke, mielőtt belemerülnél? Nézd meg ezt az illusztrált útmutatót, amely megadja a főbb témákat és a kulcsfontosságú tanulságokat, amelyeket érdemes átgondolni mindegyikben. A lecke útvonala elvezet az alapfogalmak és kihívások megértésétől azok megoldásáig a releváns prompt mérnökségi technikákkal és legjobb gyakorlatokkal. Ne feledd, hogy az útmutató "Haladó Technikák" szekciója a következő fejezet tartalmára utal ebben a tananyagban.

## Startupunk

Most beszéljünk arról, hogyan kapcsolódik _ez a téma_ a startup küldetésünkhöz, amelynek célja az [AI innováció eljuttatása az oktatásba](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). AI-alapú, _személyre szabott tanulási_ alkalmazásokat szeretnénk építeni - így gondoljuk át, hogyan "tervezhetnek" különböző felhasználók promptokat az alkalmazásunkban:

- **Adminisztrátorok** kérhetik az AI-t, hogy _elemezze a tantervi adatokat a lefedettségi hiányosságok azonosítása érdekében_. Az AI összefoglalhatja az eredményeket vagy vizualizálhatja őket kóddal.
- **Oktatók** kérhetik az AI-t, hogy _készítsen egy tantervet egy célközönség és téma számára_. Az AI megépítheti a személyre szabott tervet egy meghatározott formátumban.
- **Diákok** kérhetik az AI-t, hogy _tanítsa őket egy nehéz tárgyban_. Az AI most már vezethet diákokat leckékkel, tippekkel és példákkal az ő szintjükre szabva.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - egy nyílt forráskódú prompt könyvtárat, amelyet oktatási szakértők készítettek - hogy szélesebb képet kapj a lehetőségekről! _Próbálj ki néhányat ezek közül a promptok közül a sandboxban vagy az OpenAI Playgroundban, hogy lássad, mi történik!_

## Mi az a Prompt Mérnökség?

A leckét azzal kezdtük, hogy a **Prompt Mérnökséget** a szöveges bemenetek (promptok) _tervezési és optimalizálási_ folyamataként definiáltuk, hogy konzisztens és minőségi válaszokat (kiegészítéseket) nyújtson egy adott alkalmazási cél és modell számára. Ezt egy 2-lépéses folyamatként gondolhatjuk el:

- a kezdeti prompt _tervezése_ egy adott modellhez és célhoz
- a prompt _finomítása_ iteratívan a válasz minőségének javítása érdekében

Ez szükségszerűen egy próbálgatásos folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmények eléréséhez. Miért fontos ez? Ahhoz, hogy válaszoljunk erre a kérdésre, először három fogalmat kell megértenünk:

- _Tokenizálás_ = hogyan "látja" a modell a promptot
- _Alap LLM-ek_ = hogyan "dolgozza fel" az alapmodell a promptot
- _Instrukcióra Hangolt LLM-ek_ = hogyan látja a modell most a "feladatokat"

### Tokenizálás

Egy LLM a promptokat egy _tokenek sorozataként_ látja, ahol különböző modellek (vagy egy modell verziói) különböző módon tokenizálhatják ugyanazt a promptot. Mivel az LLM-ek tokeneken vannak kiképezve (és nem nyers szövegen), a promptok tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Ahhoz, hogy megértsük, hogyan működik a tokenizálás, próbálj ki olyan eszközöket, mint az alábbi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Másold be a promptodat - és nézd meg, hogyan alakul át tokenekké, figyelve arra, hogyan kezelik a szóköz karaktereket és írásjeleket. Ne feledd, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat - így ha ezt egy újabb modellel próbálod, más eredményt kaphatsz.

### Fogalom: Alapmodellek

Miután egy prompt tokenizálódik, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Alapmodell) elsődleges funkciója az, hogy megjósolja a tokeneket abban a sorozatban. Mivel az LLM-ek hatalmas szöveges adathalmazokon vannak kiképezve, jól érzik a tokenek közötti statisztikai kapcsolatokat, és bizonyos bizalommal tudják megtenni ezt a jóslást. Ne feledd, hogy nem értik a prompt vagy token _jelentését_; csak egy mintát látnak, amit a következő jóslatukkal "kiegészíthetnek". Folytathatják a sorozat előrejelzését, amíg a felhasználó közbe nem avatkozik, vagy valamilyen előre megállapított feltétel nem áll fenn.

Szeretnéd látni, hogyan működik a prompt-alapú kiegészítés? Írd be a fenti promptot az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) alapértelmezett beállításaival. A rendszer úgy van konfigurálva, hogy a promptokat információkérésekként kezelje - így látnod kell egy kiegészítést, amely kielégíti ezt a kontextust.

De mi van, ha a felhasználó valami konkrét dolgot szeretne látni, amely megfelel valamilyen kritériumnak vagy feladat célkitűzésnek? Itt jönnek képbe az _instrukcióra hangolt_ LLM-ek.

### Fogalom: Instrukcióra Hangolt LLM-ek

Az [Instrukcióra Hangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezdődik, és finomítja példákkal vagy bemenet/kimenet párokkal (például többfordulós "üzenetekkel"), amelyek egyértelmű utasításokat tartalmazhatnak - és az AI válasza megpróbálja követni azt az utasítást.

Ez olyan technikákat használ, mint az emberi visszajelzéssel történő megerősítéses tanulás (RLHF), amely képezheti a modellt az _utasítások követésére_ és _visszajelzésekből való tanulásra_, hogy olyan válaszokat generáljon, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és relevánsabbak a felhasználói célokhoz.

Próbáljuk ki - térj vissza a fenti prompthoz, de most változtasd meg a _rendszerüzenetet_, hogy a következő utasítást adja meg kontextusként:

> _Összefoglalás a megadott tartalomról egy másodikos diáknak. Tartsa a végeredményt egy bekezdésben, 3-5 felsorolásjellel._

Látod, hogy az eredmény most a kívánt cél és formátum tükrözésére van hangolva? Egy oktató most közvetlenül használhatja ezt a választ a diákjai számára készített diáiban.

## Miért van szükségünk Prompt Mérnökségre?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek a promptokat, beszéljünk arról, _miért_ van szükségünk prompt mérnökségre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek miatt _megbízható és konzisztens kiegészítések_ elérése nehezebb, ha nem fektetünk erőfeszítést a prompt megalkotásába és optimalizálásába. Például:

1. **A modell válaszai sztochasztikusak.** Ugyanaz a prompt valószínűleg különböző válaszokat produkál különböző modellekkel vagy modell verziókkal. És még ugyanaz a modell is eltérő eredményeket produkálhat különböző időpontokban. _A prompt mérnökségi technikák segíthetnek minimalizálni ezeket a variációkat jobb korlátok biztosításával_.

1. **A modellek fabrikálhatnak válaszokat.** A modellek _nagy, de véges_ adathalmazokkal vannak előkészítve, ami azt jelenti, hogy hiányzik a tudásuk a képzés hatókörén kívüli fogalmakról. Ennek eredményeként olyan kiegészítéseket generálhatnak, amelyek pontatlanok, képzeletbeli vagy közvetlenül ellentmondanak a tényeknek. _A prompt mérnökségi technikák segíthetnek a felhasználóknak az ilyen fabrikációk azonosításában és enyhítésében, például az AI-tól való idézések vagy érvelés kérésével_.

1. **A modellek képességei eltérhetnek.** Az újabb modellek vagy modell generációk gazdagabb képességekkel rendelkeznek, de egyedi furcsaságokat és kompromisszumokat is hoznak a költségek és a komplexitás terén. _A prompt mérnökség segíthet kidolgozni a legjobb gyakorlatokat és munkafolyamatokat, amelyek elvonják a különbségeket és alkalmazkodnak a modell-specifikus követelményekhez, skálázható, zökkenőmentes módon_.

Nézzük meg ezt akcióban az OpenAI vagy Azure OpenAI Playgroundban:

- Használd ugyanazt a promptot különböző LLM telepítésekkel (például OpenAI, Azure OpenAI, Hugging Face) - láttad a variációkat?
- Használd ugyanazt a promptot ismételten ugyanazzal az LLM telepítéssel (például Azure OpenAI playground) - hogyan különböztek ezek a variációk?

### Fabrikációk Példa

Ebben a kurzusban a **"fabrikáció"** kifejezést használjuk arra a jelenségre, amikor az LLM-ek néha tényszerűen helytelen információkat generálnak a képzésük korlátai vagy más korlátozások miatt. Lehet, hogy hallottál már erről _"hallucinációk"_ néven népszerű cikkekben vagy kutatási tanulmányokban. Azonban erősen ajánljuk a _"fabrikáció"_ kife
Végül a sablonok valódi értéke abban rejlik, hogy képesek létrehozni és közzétenni _prompt könyvtárakat_ vertikális alkalmazási területek számára - ahol a prompt sablon most _optimalizált_ az alkalmazás-specifikus kontextus vagy példák tükrözésére, amelyek a válaszokat relevánsabbá és pontosabbá teszik a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adattár nagyszerű példája ennek a megközelítésnek, egy könyvtárat gyűjt össze az oktatási terület promptjaival, hangsúlyozva a kulcsfontosságú célokat, mint például óratervezés, tanterv kialakítás, diákok korrepetálása stb.

## Támogató tartalom

Ha a prompt felépítését úgy tekintjük, mint aminek van egy utasítása (feladat) és egy célja (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan további kontextus, amit azért adunk meg, hogy **valamilyen módon befolyásoljuk a kimenetet**. Lehetnek finomhangolási paraméterek, formázási utasítások, témakategóriák stb., amelyek segíthetnek a modellnek _testreszabni_ a válaszát, hogy megfeleljen a kívánt felhasználói céloknak vagy elvárásoknak.

Például: Adott egy kurzuskatalógus kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető kurzusról a tantervben:

- meghatározhatunk egy utasítást a "kurzuskatalógus összefoglalására 2023 őszére"
- az elsődleges tartalommal néhány példát adhatunk a kívánt kimenetre
- a másodlagos tartalommal azonosíthatjuk az 5 legfontosabb érdekes "címkét".

Most a modell képes összefoglalót adni a néhány példa által bemutatott formátumban - de ha egy eredménynek több címkéje van, akkor a másodlagos tartalomban azonosított 5 címkét helyezheti előtérbe.

---

<!--
LECKE SABLON:
Ez az egység a #1 alapfogalmat kell, hogy lefedje.
Erősítse meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #3:
Prompt mérnöki technikák.
Melyek a prompt mérnöki alaptechnikák?
Mutassa be néhány gyakorlattal.
-->

## Prompt legjobb gyakorlatok

Most, hogy tudjuk, hogyan lehet a promptokat _felépíteni_, elkezdhetünk gondolkodni azon, hogyan _tervezzük_ meg őket a legjobb gyakorlatok tükrözésére. Ezt két részre oszthatjuk - a megfelelő _hozzáállás_ és a megfelelő _technikák_ alkalmazása.

### Prompt mérnöki hozzáállás

A prompt mérnöki munka egy próbálkozás és hibázás folyamat, ezért tartsa szem előtt a három széles irányító tényezőt:

1. **A terület megértése számít.** A válasz pontossága és relevanciája annak a _területnek_ a függvénye, amelyben az alkalmazás vagy a felhasználó működik. Alkalmazza intuícióját és területi szakértelmét a **technikák testreszabására**. Például, határozzon meg _terület-specifikus személyiségeket_ a rendszer promptjaiban, vagy használjon _terület-specifikus sablonokat_ a felhasználói promptokban. Nyújtson másodlagos tartalmat, amely tükrözi a terület-specifikus kontextusokat, vagy használjon _terület-specifikus utalásokat és példákat_, hogy a modellt ismerős használati minták felé irányítsa.

2. **A modell megértése számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk is változhatnak a használt képzési adatkészlet (előre tanult tudás), az általuk biztosított képességek (például API vagy SDK által) és az optimalizált tartalom típusa (például kód vs. képek vs. szöveg) tekintetében. Értsd meg a használt modell erősségeit és korlátait, és használd ezt a tudást a _feladatok prioritizálására_ vagy _testreszabott sablonok_ létrehozására, amelyek optimalizáltak a modell képességeihez.

3. **Iteráció és validáció számít.** A modellek gyorsan fejlődnek, és így a prompt mérnöki technikák is. Mint területi szakértő, lehet, hogy van más kontextus vagy kritérium a _te_ specifikus alkalmazásodhoz, ami nem vonatkozik a szélesebb közösségre. Használj prompt mérnöki eszközöket és technikákat a prompt felépítés "beindítására", majd iterálj és validáld az eredményeket saját intuícióddal és területi szakértelmeddel. Rögzítsd meglátásaidat, és hozz létre egy **tudásbázist** (például prompt könyvtárakat), amelyet mások új alapként használhatnak a jövőbeli gyorsabb iterációkhoz.

## Legjobb gyakorlatok

Most nézzük meg a közös legjobb gyakorlatokat, amelyeket az [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és az [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) gyakorlói ajánlanak.

| Mi                                 | Miért                                                                                                                                                                                                                                                |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Értékelje a legújabb modelleket.   | Az új modellgenerációk valószínűleg javított funkciókkal és minőséggel rendelkeznek - de magasabb költségekkel is járhatnak. Értékelje őket a hatásuk alapján, majd hozza meg a migrációs döntéseket.                                                  |
| Válassza szét az utasításokat és a kontextust | Ellenőrizze, hogy a modell/szolgáltató definiál-e _határolókat_, amelyek világosabban megkülönböztetik az utasításokat, az elsődleges és másodlagos tartalmat. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                             |
| Legyen konkrét és világos          | Adjon több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és következetességét. Rögzítse a recepteket újrafelhasználható sablonokban.                                         |
| Legyen leíró, használjon példákat  | A modellek jobban reagálhatnak a "mutasd és mesélj" megközelítésre. Kezdje a `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` értékekkel. Térjen vissza a [Learning Sandbox szekcióhoz](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), hogy megtanulja hogyan.

### Következő lépésként nyissa meg a Jupyter Notebookot

- Válassza ki a futtatási kernelt. Ha az 1-es vagy 2-es opciót használja, egyszerűen válassza a dev konténer által biztosított alapértelmezett Python 3.10.x kernelt.

Most készen áll az edzések futtatására. Ne feledje, hogy itt nincsenek _jó és rossz_ válaszok - csak a lehetőségek felfedezése próbálkozás és hibázás útján, és intuíció építése arra, hogy mi működik egy adott modell és alkalmazási terület esetén.

_Ezért nincsenek Kód Megoldás szegmensek ebben a leckében. Ehelyett a Notebookban lesznek Markdown cellák "Saját Megoldás:" címmel, amelyek egy példa kimenetet mutatnak referenciaként._

 <!--
LECKE SABLON:
Zárja le a szekciót összefoglalóval és önálló tanulási forrásokkal.
-->

## Tudás ellenőrzés

Melyik az alábbiak közül egy jó prompt, amely követ néhány ésszerű legjobb gyakorlatot?

1. Mutass egy képet piros autóról
2. Mutass egy képet piros autóról, Volvo márkájú és XC90 modellű, egy szikla mellett parkolva, naplementével
3. Mutass egy képet piros autóról, Volvo márkájú és XC90 modellű

A: 2, ez a legjobb prompt, mivel részleteket ad arról, hogy "mi", és konkrétumokba megy (nem csak bármilyen autó, hanem egy konkrét márka és modell), és leírja az általános környezetet is. A 3 a következő legjobb, mivel szintén sok leírást tartalmaz.

## 🚀 Kihívás

Nézze meg, hogy tudja-e használni az "utalás" technikát a prompttal: Fejezze be a mondatot "Mutass egy képet piros autóról, Volvo márkájú és ". Mit válaszol, és hogyan javítaná?

## Nagyszerű munka! Folytassa a tanulást

Szeretne többet megtudni a különböző Prompt mérnöki koncepciókról? Menjen a [folytatott tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy további nagyszerű forrásokat találjon a témában.

Menjen át az 5. leckére, ahol [fejlett prompt technikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) fogunk megvizsgálni!

**Jogi nyilatkozat**:  
Ezt a dokumentumot a [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatással fordították le. Bár igyekszünk a pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítás ajánlott. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.