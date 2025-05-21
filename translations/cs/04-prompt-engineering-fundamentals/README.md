<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:13:18+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "cs"
}
-->
# Základy inženýrství promptů

## Úvod
Tento modul se zabývá základními koncepty a technikami pro vytváření efektivních promptů v generativních AI modelech. Záleží na tom, jak napíšete svůj prompt do LLM. Pečlivě vytvořený prompt může dosáhnout lepší kvality odpovědi. Ale co přesně znamenají pojmy jako _prompt_ a _inženýrství promptů_? A jak mohu zlepšit _vstup_ promptu, který posílám do LLM? To jsou otázky, na které se pokusíme odpovědět v této kapitole a v té následující.

_Generativní AI_ je schopna vytvářet nový obsah (např. text, obrázky, audio, kód atd.) jako reakci na požadavky uživatelů. Dosahuje toho pomocí _velkých jazykových modelů_ jako je série GPT ("Generative Pre-trained Transformer") od OpenAI, které jsou trénovány pro použití přirozeného jazyka a kódu.

Uživatelé nyní mohou interagovat s těmito modely pomocí známých paradigmat, jako je chat, aniž by potřebovali technické znalosti nebo školení. Modely jsou _založené na prompty_ - uživatelé posílají textový vstup (prompt) a získávají zpět odpověď AI (dokončení). Mohou poté "chatovat s AI" iterativně, v konverzacích s více otočkami, zdokonalovat svůj prompt, dokud odpověď neodpovídá jejich očekáváním.

"Prompty" se nyní stávají hlavním _programovacím rozhraním_ pro generativní AI aplikace, říkají modelům, co mají dělat, a ovlivňují kvalitu vrácených odpovědí. "Inženýrství promptů" je rychle rostoucí oblast studia, která se zaměřuje na _návrh a optimalizaci_ promptů pro dosažení konzistentních a kvalitních odpovědí v měřítku.

## Cíle učení

V této lekci se dozvíme, co je inženýrství promptů, proč je důležité, a jak můžeme vytvářet efektivnější prompty pro daný model a cíl aplikace. Porozumíme základním konceptům a osvědčeným postupům pro inženýrství promptů - a dozvíme se o interaktivním prostředí "sandboxu" Jupyter Notebooks, kde můžeme vidět tyto koncepty aplikované na skutečné příklady.

Na konci této lekce budeme schopni:

1. Vysvětlit, co je inženýrství promptů a proč je důležité.
2. Popsat komponenty promptu a jak jsou použity.
3. Naučit se osvědčené postupy a techniky pro inženýrství promptů.
4. Aplikovat naučené techniky na skutečné příklady, pomocí OpenAI endpointu.

## Klíčové pojmy

Inženýrství promptů: Praktika navrhování a zdokonalování vstupů k vedení AI modelů k produkci požadovaných výstupů.
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model může pochopit a zpracovat.
LLM laděné instrukcemi: Velké jazykové modely (LLM), které byly jemně doladěny specifickými instrukcemi pro zlepšení jejich přesnosti a relevance odpovědí.

## Sandbox pro učení

Inženýrství promptů je aktuálně spíše umění než věda. Nejlepší způsob, jak zlepšit naši intuici pro něj, je _více cvičit_ a přijmout přístup pokus-omyl, který kombinuje odborné znalosti v oblasti aplikace s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook doprovázející tuto lekci poskytuje _sandbox_ prostředí, kde si můžete vyzkoušet, co se učíte - jak jdete, nebo jako součást výzvy kódování na konci. K provedení cvičení budete potřebovat:

1. **Azure OpenAI API klíč** - služební endpoint pro nasazený LLM.
2. **Python Runtime** - ve kterém může být Notebook spuštěn.
3. **Lokální proměnné prostředí** - _dokončete kroky [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) nyní, abyste byli připraveni_.

Notebook přichází s _počátečními_ cvičeními - ale doporučuje se přidat vlastní _Markdown_ (popis) a _Code_ (žádosti o prompty) sekce, abyste si vyzkoušeli více příkladů nebo nápadů - a budovali svou intuici pro návrh promptů.

## Ilustrovaný průvodce

Chcete získat celkový obrázek o tom, co tato lekce pokrývá, než se ponoříte? Podívejte se na tento ilustrovaný průvodce, který vám dá pocit z hlavních témat pokrytých a klíčových závěrů, které byste měli mít na paměti u každého z nich. Plán lekce vás vede od pochopení základních konceptů a výzev k jejich řešení pomocí relevantních technik inženýrství promptů a osvědčených postupů. Všimněte si, že sekce "Pokročilé techniky" v tomto průvodci odkazuje na obsah pokrytý v _další_ kapitole tohoto kurikula.

## Naše startupová mise

Nyní si povíme, jak _toto téma_ souvisí s naší startupovou misí [přinést AI inovaci do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme budovat AI-poháněné aplikace pro _personalizované učení_ - takže přemýšlejme o tom, jak různí uživatelé naší aplikace mohou "navrhnout" prompty:

- **Administrátoři** mohou požádat AI o _analýzu dat kurikula k identifikaci mezer v pokrytí_. AI může shrnout výsledky nebo je vizualizovat pomocí kódu.
- **Učitelé** mohou požádat AI o _vytvoření plánu lekce pro cílové publikum a téma_. AI může sestavit personalizovaný plán ve specifikovaném formátu.
- **Studenti** mohou požádat AI o _doučování v obtížném předmětu_. AI nyní může vést studenty s lekcemi, nápovědou a příklady přizpůsobenými jejich úrovni.

To je jen špička ledovce. Podívejte se na [Prompty pro vzdělávání](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - knihovnu otevřených promptů kurátorovanou odborníky na vzdělávání - abyste získali širší přehled o možnostech! _Zkuste spustit některé z těchto promptů v sandboxu nebo použít OpenAI Playground a uvidíte, co se stane!_

## Co je inženýrství promptů?

Tuto lekci jsme zahájili definicí **inženýrství promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů) k dosažení konzistentních a kvalitních odpovědí (dokončení) pro daný cíl aplikace a model. Můžeme to považovat za dvoustupňový proces:

- _navrhování_ počátečního promptu pro daný model a cíl
- _zdokonalování_ promptu iterativně k zlepšení kvality odpovědi

To je nutně proces pokus-omyl, který vyžaduje intuici uživatele a úsilí k dosažení optimálních výsledků. Tak proč je to důležité? Abychom na tuto otázku odpověděli, musíme nejprve pochopit tři koncepty:

- _Tokenizace_ = jak model "vidí" prompt
- _Základní LLMs_ = jak základní model "zpracovává" prompt
- _LLMs laděné instrukcemi_ = jak model nyní může vidět "úkoly"

### Tokenizace

LLM vidí prompty jako _sekvenci tokenů_, kde různé modely (nebo verze modelu) mohou tokenizovat stejný prompt různými způsoby. Protože LLMs jsou trénovány na tokenech (a ne na surovém textu), způsob, jakým jsou prompty tokenizovány, má přímý dopad na kvalitu generované odpovědi.

Chcete-li získat intuici, jak tokenizace funguje, zkuste nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) ukázané níže. Zkopírujte svůj prompt - a podívejte se, jak se převádí na tokeny, věnujte pozornost tomu, jak jsou zpracovány znaky bílé mezery a interpunkční znaménka. Všimněte si, že tento příklad ukazuje starší LLM (GPT-3) - takže zkoušení s novějším modelem může produkovat jiný výsledek.

### Koncept: Základní modely

Jakmile je prompt tokenizován, primární funkcí ["Základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (nebo základního modelu) je předpovědět token v této sekvenci. Protože LLMs jsou trénovány na masivních textových datových sadách, mají dobrý smysl pro statistické vztahy mezi tokeny a mohou tuto předpověď provést s jistou mírou důvěry. Všimněte si, že nerozumí _významu_ slov v promptu nebo tokenu; jen vidí vzor, který mohou "dokončit" svou další předpovědí. Mohou pokračovat v předpovídání sekvence, dokud nejsou zastaveni uživatelským zásahem nebo nějakou předem stanovenou podmínkou.

Chcete vidět, jak funguje dokončení založené na promptu? Zadejte výše uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s výchozím nastavením. Systém je konfigurován tak, aby prompty považoval za žádosti o informace - takže byste měli vidět dokončení, které uspokojí tento kontext.

Ale co když uživatel chtěl vidět něco specifického, co splňuje nějaká kritéria nebo cíle úkolu? Zde přicházejí na scénu _LLMs laděné instrukcemi_.

### Koncept: LLMs laděné instrukcemi

[LLM laděný instrukcemi](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začíná základním modelem a jemně ho doladí příklady nebo páry vstup/výstup (např. víceotáčkové "zprávy"), které mohou obsahovat jasné instrukce - a odpověď AI se pokouší tuto instrukci dodržet.

To využívá techniky jako Reinforcement Learning with Human Feedback (RLHF), které mohou trénovat model na _dodržování instrukcí_ a _učení se z feedbacku_, aby produkoval odpovědi, které jsou lépe přizpůsobené praktickým aplikacím a více relevantní pro cíle uživatele.

Zkusme to - znovu se podívejte na výše uvedený prompt, ale nyní změňte _systémovou zprávu_, aby poskytovala následující instrukci jako kontext:

> _Shrňte obsah, který vám byl poskytnut, pro druháka. Udržujte výsledek na jeden odstavec s 3-5 odrážkami._

Vidíte, jak je výsledek nyní naladěn, aby odrážel požadovaný cíl a formát? Učitel nyní může tuto odpověď přímo použít ve svých slidech pro tuto třídu.

## Proč potřebujeme inženýrství promptů?

Nyní, když víme, jak jsou prompty zpracovávány LLMs, pojďme si povědět o _proč_ potřebujeme inženýrství promptů. Odpověď spočívá v tom, že současné LLMs představují řadu výzev, které činí _spolehlivé a konzistentní dokončení_ obtížnějším dosáhnout bez úsilí o konstrukci a optimalizaci promptů. Například:

1. **Odpovědi modelu jsou stochastické.** _Stejný prompt_ pravděpodobně produkuje různé odpovědi s různými modely nebo verzemi modelu. A může dokonce produkovat různé výsledky se _stejným modelem_ v různých časech. _Techniky inženýrství promptů nám mohou pomoci minimalizovat tyto variace poskytováním lepších ochranných opatření_.

1. **Modely mohou vytvářet odpovědi.** Modely jsou předtrénovány s _velkými, ale konečnými_ datovými sadami, což znamená, že jim chybí znalosti o konceptech mimo tento tréninkový rozsah. V důsledku toho mohou produkovat dokončení, která jsou nepřesná, imaginární nebo přímo odporující známým faktům. _Techniky inženýrství promptů pomáhají uživatelům identifikovat a zmírnit takové výroby např. požadováním AI o citace nebo odůvodnění_.

1. **Schopnosti modelů se budou lišit.** Novější modely nebo generace modelů budou mít bohatší schopnosti, ale také přinesou jedinečné zvláštnosti a kompromisy v nákladech a složitosti. _Inženýrství promptů nám může pomoci vyvinout osvědčené postupy a pracovní postupy, které abstrahují rozdíly a přizpůsobují se požadavkům specifickým pro model způsobem, který je škálovatelný a bezproblémový_.

Pojďme to vidět v akci v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) - viděli jste ty variace?
- Použijte stejný prompt opakovaně se _stejným_ nasazením LLM (např. Azure OpenAI playground) - jak se tyto variace lišily?

### Příklad výroby

V tomto kurzu používáme termín **"výroba"** k označení fenoménu, kdy LLMs někdy generují fakticky nesprávné informace kvůli omezením ve svém tréninku nebo jiným omezením. Možná jste také slyšeli o tom, že se to označuje jako _"halucinace"_ v populárních článcích nebo výzkumných pracích. Nicméně důrazně doporučujeme používat _"výroba"_ jako termín, abychom náhodně neantropomorfizovali chování tím, že připisujeme lidský rys výsledku řízenému strojem. To také posiluje [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hlediska terminologie, odstraněním termínů, které mohou být také považovány za urážlivé nebo neinkluzivní v některých kontextech.

Chcete získat představu o tom, jak výroby fungují? Pomyslete na prompt, který instruuje AI generovat obsah pro neexistující téma (aby bylo zajištěno, že se nenachází v tréninkové datové sadě). Například - zkusil jsem tento prompt:

> **Prompt:** vytvořte plán lekce o Martianské válce roku 2076.

Webové vyhledávání mi ukázalo, že existovaly fiktivní účty (např. televizní seriály nebo knihy) o Martianských válkách - ale žádné v roce 2076. Zdravý rozum nám také říká, že 2076 je _v budoucnosti_ a tudíž nemůže být spojeno se skutečnou událostí.

Co se tedy stane, když tento prompt spustíme s různými poskytovateli LLM?

> **Odpověď 1**: OpenAI Playground (GPT-35)

> **Odpověď 2**: Azure OpenAI Playground (GPT-35)

> **Odpověď 3**: Hugging Face Chat Playground (LLama-2)

Jak se očekávalo, každý model (nebo verze modelu) produkuje mírně odlišné odpovědi díky stochastickému chování a variacím schopností modelu. Například
Nakonec skutečná hodnota šablon spočívá ve schopnosti vytvářet a publikovat _knihovny promptů_ pro vertikální aplikační domény - kde je šablona promptu nyní _optimalizována_ tak, aby odrážela kontext specifický pro aplikaci nebo příklady, které činí odpovědi relevantnějšími a přesnějšími pro cílovou skupinu uživatelů. Repozitář [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, který sestavuje knihovnu promptů pro vzdělávací doménu s důrazem na klíčové cíle jako plánování lekcí, návrh osnov, doučování studentů atd.

## Podpůrný obsah

Pokud považujeme konstrukci promptu za úkol a cílový obsah, pak _sekundární obsah_ je jako další kontext, který poskytujeme, abychom **nějakým způsobem ovlivnili výstup**. Mohou to být ladicí parametry, pokyny pro formátování, taxonomie témat atd., které mohou pomoci modelu _přizpůsobit_ jeho odpověď tak, aby vyhovovala požadovaným uživatelským cílům nebo očekáváním.

Například: Máme katalog kurzů s rozsáhlými metadaty (název, popis, úroveň, metadata tagy, instruktor atd.) pro všechny dostupné kurzy v osnovách:

- můžeme definovat instrukci pro "souhrn katalogu kurzů na podzim 2023"
- můžeme použít hlavní obsah k poskytnutí několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci 5 nejzajímavějších "tagů".

Nyní může model poskytnout souhrn ve formátu ukázaném několika příklady - ale pokud má výsledek více tagů, může upřednostnit 5 tagů identifikovaných v sekundárním obsahu.

---

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrývat hlavní koncept č. 1.
Posílit koncept pomocí příkladů a referencí.

KONCEPT č. 3:
Techniky návrhu promptů.
Jaké jsou některé základní techniky pro návrh promptů?
Ukázat je pomocí cvičení.
-->

## Nejlepší praktiky pro návrh promptů

Nyní, když víme, jak lze prompty _konstruovat_, můžeme začít přemýšlet o tom, jak je _navrhnout_ tak, aby odrážely nejlepší praktiky. Můžeme o tom přemýšlet ve dvou částech - mít správný _přístup_ a aplikovat správné _techniky_.

### Přístup k návrhu promptů

Návrh promptů je proces pokusů a omylů, proto mějte na paměti tři široké vodicí faktory:

1. **Porozumění doméně je důležité.** Přesnost a relevance odpovědí je funkcí _domény_, ve které daná aplikace nebo uživatel působí. Použijte svou intuici a odborné znalosti domény k **dalšímu přizpůsobení technik**. Například definujte _doménově specifické osobnosti_ ve svých systémových promptech nebo použijte _doménově specifické šablony_ ve svých uživatelských promptech. Poskytněte sekundární obsah, který odráží kontexty specifické pro doménu, nebo použijte _doménově specifické nápovědy a příklady_, které povedou model k známým vzorcům použití.

2. **Porozumění modelu je důležité.** Víme, že modely jsou stochastické povahy. Ale implementace modelů se mohou lišit také z hlediska datové sady, kterou používají (předem naučené znalosti), schopností, které poskytují (např. prostřednictvím API nebo SDK) a typu obsahu, pro který jsou optimalizovány (např. kód vs. obrázky vs. text). Pochopte silné stránky a omezení modelu, který používáte, a využijte tyto znalosti k _upřednostnění úkolů_ nebo k vytvoření _přizpůsobených šablon_, které jsou optimalizovány pro schopnosti modelu.

3. **Iterace a validace jsou důležité.** Modely se rychle vyvíjejí, stejně jako techniky pro návrh promptů. Jako odborník na danou doménu můžete mít další kontext nebo kritéria pro _vaši_ konkrétní aplikaci, která nemusí platit pro širší komunitu. Použijte nástroje a techniky pro návrh promptů k "nastartování" konstrukce promptů, poté iterujte a validujte výsledky pomocí své vlastní intuice a odborných znalostí domény. Zaznamenejte své poznatky a vytvořte **databázi znalostí** (např. knihovny promptů), která může být použita jako nový základ pro ostatní, aby mohli rychleji iterovat v budoucnu.

## Nejlepší praktiky

Nyní se podívejme na běžné nejlepší praktiky, které doporučují [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a odborníci z [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                                | Proč                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hodnoťte nejnovější modely.       | Nové generace modelů pravděpodobně budou mít vylepšené funkce a kvalitu - ale mohou také mít vyšší náklady. Hodnoťte jejich dopad, pak se rozhodněte pro migraci.                                                                                 |
| Oddělte instrukce a kontext       | Zkontrolujte, zda váš model/poskytovatel definuje _oddělovače_, které jasněji rozlišují instrukce, primární a sekundární obsah. To může pomoci modelům přiřadit váhy přesněji k tokenům.                                                          |
| Buďte konkrétní a jasní           | Poskytněte více podrobností o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší kvalitu a konzistenci odpovědí. Zaznamenejte recepty v opakovaně použitelných šablonách.                                                      |
| Buďte popisní, používejte příklady| Modely mohou lépe reagovat na přístup "ukaž a řekni". Začněte s hodnotami `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT`. Vraťte se k [Learning Sandbox sekci](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), abyste se naučili jak.

### Dále otevřete Jupyter Notebook

- Vyberte jádro runtime. Pokud používáte možnosti 1 nebo 2, jednoduše vyberte výchozí jádro Python 3.10.x poskytované vývojovým kontejnerem.

Jste připraveni spustit cvičení. Všimněte si, že zde nejsou žádné _správné a špatné_ odpovědi - pouze zkoumání možností pomocí pokusů a omylů a budování intuice pro to, co funguje pro daný model a aplikační doménu.

_Z tohoto důvodu v této lekci nejsou žádné segmenty řešení kódu. Místo toho bude Notebook obsahovat buňky Markdown nazvané "Moje řešení:", které ukazují jeden příklad výstupu pro referenci._

 <!--
ŠABLONA LEKCE:
Uzavřete sekci souhrnem a zdroji pro samostatné učení.
-->

## Kontrola znalostí

Který z následujících je dobrý prompt podle některých rozumných nejlepších praktik?

1. Ukaž mi obrázek červeného auta
2. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90 zaparkovaného u útesu se zapadajícím sluncem
3. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90

A: 2, je to nejlepší prompt, protože poskytuje podrobnosti o "čem" a jde do specifik (ne jen nějaké auto, ale konkrétní značka a model) a také popisuje celkové prostředí. 3 je další nejlepší, protože také obsahuje mnoho popisů.

## 🚀 Výzva

Zkuste využít techniku "nápovědy" s promptem: Dokončete větu "Ukaž mi obrázek červeného auta značky Volvo a ". Co odpovídá, a jak byste to zlepšili?

## Skvělá práce! Pokračujte ve svém učení

Chcete se dozvědět více o různých konceptech návrhu promptů? Přejděte na [stránku pokračujícího učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a najděte další skvělé zdroje na toto téma.

Přejděte na Lekci 5, kde se podíváme na [pokročilé techniky promptování](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument ve svém rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.