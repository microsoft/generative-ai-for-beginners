<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:21:35+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "cs"
}
-->
# Základy návrhu promptů

## Úvod
Tento modul se zabývá základními koncepty a technikami pro vytváření efektivních promptů v generativních AI modelech. Záleží také na tom, jakým způsobem napíšete svůj prompt pro LLM. Pečlivě vytvořený prompt může dosáhnout lepší kvality odpovědi. Ale co přesně znamenají pojmy jako _prompt_ a _návrh promptů_? A jak mohu zlepšit prompt _vstup_, který posílám LLM? To jsou otázky, na které se pokusíme odpovědět v této kapitole a v následující.

_Generativní AI_ je schopna vytvářet nový obsah (např. text, obrázky, zvuk, kód atd.) jako odpověď na požadavky uživatelů. Dosahuje toho pomocí _Velkých jazykových modelů_ jako je série GPT ("Generative Pre-trained Transformer") od OpenAI, které jsou vyškoleny na používání přirozeného jazyka a kódu.

Uživatelé nyní mohou interagovat s těmito modely pomocí známých paradigmat, jako je chat, aniž by potřebovali jakékoliv technické znalosti nebo školení. Modely jsou _založeny na prompty_ - uživatelé posílají textový vstup (prompt) a dostávají zpět odpověď AI (dokončení). Mohou pak "chatovat s AI" iterativně, v rozhovorech na více tahů, a zdokonalovat svůj prompt, dokud odpověď nesplňuje jejich očekávání.

"Prompty" se nyní stávají primárním _programovacím rozhraním_ pro generativní AI aplikace, které říkají modelům, co dělat, a ovlivňují kvalitu vrácených odpovědí. "Návrh promptů" je rychle rostoucí obor, který se zaměřuje na _návrh a optimalizaci_ promptů, aby poskytovaly konzistentní a kvalitní odpovědi v rozsahu.

## Cíle učení

V této lekci se naučíme, co je návrh promptů, proč je důležitý a jak můžeme vytvářet efektivnější prompty pro daný model a aplikační cíl. Porozumíme základním konceptům a osvědčeným postupům pro návrh promptů - a dozvíme se o interaktivním prostředí "sandbox" Jupyter Notebooks, kde můžeme vidět tyto koncepty aplikované na skutečné příklady.

Na konci této lekce budeme schopni:

1. Vysvětlit, co je návrh promptů a proč je důležitý.
2. Popsat komponenty promptu a jak se používají.
3. Naučit se osvědčené postupy a techniky pro návrh promptů.
4. Aplikovat naučené techniky na skutečné příklady pomocí OpenAI endpointu.

## Klíčové pojmy

Návrh promptů: Praxe navrhování a zdokonalování vstupů k vedení AI modelů k produkci požadovaných výstupů.
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model může pochopit a zpracovat.
LLM doladěné instrukcemi: Velké jazykové modely (LLMs), které byly doladěny pomocí specifických instrukcí pro zlepšení jejich přesnosti a relevance odpovědí.

## Sandbox pro učení

Návrh promptů je aktuálně spíše umění než věda. Nejlepší způsob, jak zlepšit naši intuici pro něj, je _více cvičit_ a přijmout přístup pokus-omyl, který kombinuje odborné znalosti aplikačního doménu s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook, který doprovází tuto lekci, poskytuje _sandbox_ prostředí, kde si můžete vyzkoušet, co se naučíte - buď průběžně, nebo jako součást výzvy kódování na konci. K provedení cvičení budete potřebovat:

1. **Azure OpenAI API klíč** - servisní endpoint pro nasazený LLM.
2. **Python Runtime** - ve kterém lze Notebook spustit.
3. **Lokální proměnné prostředí** - _dokončete kroky [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) nyní, abyste byli připraveni_.

Notebook přichází se _startovními_ cvičeními - ale jste povzbuzováni k přidání vlastních _Markdown_ (popis) a _Code_ (požadavky promptů) sekcí, abyste si vyzkoušeli více příkladů nebo nápadů - a budovali svou intuici pro návrh promptů.

## Ilustrovaný průvodce

Chcete získat celkový obraz toho, co tato lekce pokrývá, než se do ní ponoříte? Podívejte se na tento ilustrovaný průvodce, který vám dává smysl hlavních témat pokrytých a klíčových poznatků, o kterých byste měli přemýšlet v každém z nich. Plán lekce vás vede od porozumění základním konceptům a výzvám k jejich řešení pomocí relevantních technik návrhu promptů a osvědčených postupů. Všimněte si, že sekce "Pokročilé techniky" v tomto průvodci odkazuje na obsah pokrytý v _další_ kapitole tohoto kurikula.

## Naše startupová mise

Nyní si povíme, jak _toto téma_ souvisí s naší startupovou misí [přinést AI inovace do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme budovat AI poháněné aplikace pro _personalizované učení_ - takže si pojďme přemýšlet o tom, jak různí uživatelé naší aplikace mohou "navrhovat" prompty:

- **Administrátoři** mohou požádat AI, aby _analyzovala data kurikula a identifikovala mezery v pokrytí_. AI může shrnout výsledky nebo je vizualizovat pomocí kódu.
- **Učitelé** mohou požádat AI, aby _vytvořila plán lekce pro cílové publikum a téma_. AI může vytvořit personalizovaný plán ve specifikovaném formátu.
- **Studenti** mohou požádat AI, aby je _doučovala v obtížném předmětu_. AI může nyní vést studenty s lekcemi, nápovědami a příklady přizpůsobenými jejich úrovni.

To je jen špička ledovce. Podívejte se na [Prompty pro vzdělávání](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otevřenou knihovnu promptů kurátorovanou odborníky na vzdělávání - abyste získali širší smysl možností! _Zkuste spustit některé z těchto promptů v sandboxu nebo použijte OpenAI Playground, abyste viděli, co se stane!_

## Co je návrh promptů?

Začali jsme tuto lekci definováním **návrhu promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů) pro poskytování konzistentních a kvalitních odpovědí (dokončení) pro daný aplikační cíl a model. Můžeme si to představit jako dvoustupňový proces:

- _navrhování_ počátečního promptu pro daný model a cíl
- _zdokonalování_ promptu iterativně pro zlepšení kvality odpovědi

To je nutně proces pokus-omyl, který vyžaduje intuici uživatele a úsilí k dosažení optimálních výsledků. Proč je to tedy důležité? Abychom na tuto otázku odpověděli, musíme nejprve porozumět třem konceptům:

- _Tokenizace_ = jak model "vidí" prompt
- _Základní LLMs_ = jak základní model "zpracovává" prompt
- _LLM doladěné instrukcemi_ = jak model nyní vidí "úkoly"

### Tokenizace

LLM vidí prompty jako _sekvenci tokenů_, kde různé modely (nebo verze modelu) mohou tokenizovat stejný prompt různými způsoby. Protože LLMs jsou vyškoleny na tokenech (a ne na surovém textu), způsob, jakým jsou prompty tokenizovány, má přímý dopad na kvalitu generované odpovědi.

Abychom získali intuici, jak tokenizace funguje, vyzkoušejte nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zobrazený níže. Zkopírujte svůj prompt - a podívejte se, jak se převádí na tokeny, věnujte pozornost tomu, jak jsou zpracovávány bílé znaky a interpunkční znaménka. Všimněte si, že tento příklad ukazuje starší LLM (GPT-3) - takže zkoušení tohoto s novějším modelem může přinést jiný výsledek.

### Koncept: Základní modely

Jakmile je prompt tokenizován, primární funkcí ["Základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (nebo Základního modelu) je předpovědět token v této sekvenci. Protože LLMs jsou vyškoleny na obrovských textových datech, mají dobrý smysl pro statistické vztahy mezi tokeny a mohou tuto předpověď udělat s určitou jistotou. Všimněte si, že nerozumí _významu_ slov v promptu nebo tokenu; vidí pouze vzor, který mohou "dokončit" svou další předpovědí. Mohou pokračovat v předpovídání sekvence, dokud není ukončena uživatelským zásahem nebo nějakou předem stanovenou podmínkou.

Chcete vidět, jak funguje dokončení založené na promptu? Zadejte výše uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s výchozím nastavením. Systém je konfigurován tak, aby zacházel s prompty jako s požadavky na informace - takže byste měli vidět dokončení, které uspokojí tento kontext.

Ale co když uživatel chtěl vidět něco konkrétního, co splňuje nějaká kritéria nebo cíle úkolu? Zde přicházejí na scénu _LLM doladěné instrukcemi_.

### Koncept: LLM doladěné instrukcemi

[LLM doladěné instrukcemi](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začíná s základním modelem a doladí ho pomocí příkladů nebo párů vstup/výstup (např. více tahových "zpráv"), které mohou obsahovat jasné instrukce - a odpověď od AI se pokusí tuto instrukci následovat.

To používá techniky jako Posilování učení s lidskou zpětnou vazbou (RLHF), které mohou vyškolit model, aby _následoval instrukce_ a _učil se ze zpětné vazby_, takže produkuje odpovědi, které jsou lépe přizpůsobeny praktickým aplikacím a více relevantní pro cíle uživatelů.

Zkusme to - vraťte se k výše uvedenému promptu, ale nyní změňte _systémovou zprávu_ tak, aby poskytovala následující instrukci jako kontext:

> _Shrňte obsah, který vám byl poskytnut, pro druháka. Udržujte výsledek na jeden odstavec s 3-5 odrážkami._

Vidíte, jak je výsledek nyní doladěn tak, aby odrážel požadovaný cíl a formát? Učitel může nyní přímo použít tuto odpověď ve svých slidech pro tuto třídu.

## Proč potřebujeme návrh promptů?

Nyní, když víme, jak jsou prompty zpracovávány LLMs, pojďme si povědět, _proč_ potřebujeme návrh promptů. Odpověď spočívá v tom, že současné LLMs představují řadu výzev, které činí _spolehlivé a konzistentní dokončení_ obtížnější dosáhnout bez vynaložení úsilí na konstrukci a optimalizaci promptů. Například:

1. **Odpovědi modelů jsou stochastické.** _Stejný prompt_ pravděpodobně přinese různé odpovědi s různými modely nebo verzemi modelů. A může dokonce produkovat různé výsledky se _stejným modelem_ v různých časech. _Techniky návrhu promptů nám mohou pomoci minimalizovat tyto variace poskytnutím lepších mantinelů_.

1. **Modely mohou vyrábět odpovědi.** Modely jsou předem vyškoleny na _velkých, ale konečných_ datových souborech, což znamená, že jim chybí znalosti o konceptech mimo tento tréninkový rozsah. V důsledku toho mohou produkovat dokončení, která jsou nepřesná, imaginární nebo přímo protikladná známým faktům. _Techniky návrhu promptů pomáhají uživatelům identifikovat a zmírňovat takové výroby např. požádáním AI o citace nebo logiku_.

1. **Schopnosti modelů se budou lišit.** Novější modely nebo generace modelů budou mít bohatší schopnosti, ale také přinesou jedinečné zvláštnosti a kompromisy v nákladech a složitosti. _Návrh promptů nám může pomoci vyvinout osvědčené postupy a pracovní postupy, které abstrahují rozdíly a přizpůsobují se požadavkům specifickým pro modely škálovatelným a bezproblémovým způsobem_.

Podívejme se na to v akci v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) - viděli jste variace?
- Použijte stejný prompt opakovaně se _stejným_ nasazením LLM (např. Azure OpenAI Playground) - jak se tyto variace lišily?

### Příklad výroby

V tomto kurzu používáme termín **"výroba"** k označení fenoménu, kdy LLMs někdy generují fakticky nesprávné informace kvůli omezením v jejich školení nebo jiným omezením. Možná jste také slyšeli, že se to nazývá _"halucinace"_ v populárních článcích nebo výzkumných pracích. Nicméně, důrazně doporučujeme používat termín _"výroba"_, abychom náhodou neantropomorfizovali chování přisuzováním lidské vlastnosti k výsledku řízenému strojem. To také posiluje [pokyny pro zodpovědnou AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z terminologického hlediska, odstraňováním termínů, které mohou být v některých kontextech považovány za urážlivé nebo neinkluzivní.

Chcete získat smysl, jak fungují výroby? Přemýšlejte o promptu, který instruuje AI, aby generovala obsah pro neexistující téma (aby bylo zajištěno, že není nalezeno v tréninkovém datovém souboru). Například - zkusil jsem tento prompt:

> **Prompt:** vytvořte plán lekce o Martianské válce z roku 2076.

Webový vyhledávač mi ukázal, že existovaly fiktivní účty (např. televizní seriály nebo knihy) o Martianských válkách - ale žádné v roce 2076. Zdravý rozum nám také říká, že rok 2076 je _v budoucnosti_ a tudíž nemůže být spojen s reálnou událostí.

Takže co se stane, když spustíme tento prompt s různými poskytovateli LLM?

Jak se očekávalo, každý model (nebo verze modelu) produkuje mírně odlišné odpovědi díky stochastickému chování a variacím schopností modelu. Například jeden model cílí na publikum 8. třídy, zatímco druhý předpok
Skutečná hodnota šablon spočívá ve schopnosti vytvářet a publikovat _knihovny promptů_ pro vertikální aplikační domény - kde je šablona promptu nyní _optimalizována_ tak, aby odrážela kontext nebo příklady specifické pro aplikaci, které činí odpovědi relevantnějšími a přesnějšími pro cílovou uživatelskou skupinu. Repozitář [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, když kurátoruje knihovnu promptů pro oblast vzdělávání s důrazem na klíčové cíle, jako je plánování lekcí, návrh osnov, doučování studentů atd.

## Podpůrný obsah

Pokud uvažujeme o konstrukci promptů jako o úkolu (instrukce) a cíli (primární obsah), pak _sekundární obsah_ je jako dodatečný kontext, který poskytujeme, abychom **nějakým způsobem ovlivnili výstup**. Mohou to být parametry ladění, instrukce formátování, taxonomie témat atd., které mohou pomoci modelu _přizpůsobit_ svou odpověď tak, aby vyhovovala požadovaným uživatelským cílům nebo očekáváním.

Například: Máme katalog kurzů s rozsáhlými metadaty (název, popis, úroveň, metadata, instruktor atd.) o všech dostupných kurzech v osnovách:

- můžeme definovat instrukci "shrňte katalog kurzů pro podzim 2023"
- můžeme použít primární obsah k poskytnutí několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci 5 nejdůležitějších "štítků" zájmu.

Nyní může model poskytnout shrnutí ve formátu ukázaném v několika příkladech - ale pokud má výsledek více štítků, může upřednostnit 5 štítků identifikovaných v sekundárním obsahu.

---

## Nejlepší postupy pro vytváření promptů

Nyní, když víme, jak mohou být prompty _konstruovány_, můžeme začít přemýšlet o tom, jak je _navrhnout_ tak, aby odrážely nejlepší postupy. Můžeme o tom přemýšlet ve dvou částech - mít správné _myšlení_ a aplikovat správné _techniky_.

### Myšlení pro vytváření promptů

Vytváření promptů je proces pokusů a omylů, proto mějte na paměti tři široké vodítka:

1. **Porozumění doméně je důležité.** Přesnost a relevance odpovědí je funkcí _domény_, ve které daná aplikace nebo uživatel operuje. Použijte svou intuici a odborné znalosti domény k dalšímu **přizpůsobení technik**. Například definujte _osobnosti specifické pro doménu_ ve svých systémových promptech nebo použijte _šablony specifické pro doménu_ ve svých uživatelských promptech. Poskytněte sekundární obsah, který odráží kontexty specifické pro doménu, nebo použijte _podněty a příklady specifické pro doménu_, abyste model vedli k známým vzorům použití.

2. **Porozumění modelu je důležité.** Víme, že modely jsou svou povahou stochastické. Ale implementace modelů se mohou také lišit z hlediska tréninkového datasetu, který používají (předem naučené znalosti), schopností, které poskytují (např. prostřednictvím API nebo SDK), a typu obsahu, pro který jsou optimalizovány (např. kód vs. obrázky vs. text). Pochopte silné a slabé stránky modelu, který používáte, a použijte tyto znalosti k _prioritizaci úkolů_ nebo vytváření _přizpůsobených šablon_, které jsou optimalizovány pro schopnosti modelu.

3. **Iterace a validace jsou důležité.** Modely se rychle vyvíjejí, stejně jako techniky pro vytváření promptů. Jako odborník na doménu můžete mít další kontext nebo kritéria pro _vaši_ specifickou aplikaci, která nemusí platit pro širší komunitu. Použijte nástroje a techniky pro vytváření promptů k "nastartování" konstrukce promptů, poté iterujte a validujte výsledky pomocí své vlastní intuice a odborných znalostí domény. Zaznamenejte své poznatky a vytvořte **bázi znalostí** (např. knihovny promptů), kterou mohou ostatní použít jako nový základ pro rychlejší iterace v budoucnu.

## Nejlepší postupy

Nyní se podívejme na běžné nejlepší postupy, které doporučují praktici [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                                | Proč                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hodnoťte nejnovější modely.       | Nové generace modelů pravděpodobně mají vylepšené funkce a kvalitu - ale mohou také znamenat vyšší náklady. Zhodnoťte je z hlediska dopadu a poté proveďte rozhodnutí o migraci.                                                                  |
| Oddělte instrukce a kontext       | Zkontrolujte, zda váš model/poskytovatel definuje _oddělovače_ pro jasnější rozlišení instrukcí, primárního a sekundárního obsahu. To může modelům pomoci přiřadit váhy přesněji k tokenům.                                                       |
| Buďte konkrétní a jasní           | Poskytněte více podrobností o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší jak kvalitu, tak konzistenci odpovědí. Zachyťte recepty v opakovaně použitelných šablonách.                                                      |
| Buďte popisní, používejte příklady | Modely mohou lépe reagovat na přístup "ukázat a říci". Začněte s `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` hodnoty. Vraťte se k [sekci Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), abyste se dozvěděli více.

### Dále otevřete Jupyter Notebook

- Vyberte runtime kernel. Pokud používáte možnosti 1 nebo 2, jednoduše vyberte výchozí kernel Python 3.10.x poskytovaný dev kontejnerem.

Jste připraveni spustit cvičení. Všimněte si, že zde nejsou žádné _správné a špatné_ odpovědi - jen zkoumání možností metodou pokusů a omylů a budování intuice pro to, co funguje pro daný model a aplikační doménu.

_Z tohoto důvodu v této lekci nejsou žádné segmenty řešení kódu. Místo toho bude Notebook obsahovat buňky Markdown s názvem "My Solution:", které ukazují jeden příklad výstupu pro referenci._

## Kontrola znalostí

Který z následujících promptů je dobrý podle některých rozumných nejlepších postupů?

1. Ukaž mi obrázek červeného auta
2. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90 zaparkovaného u útesu při západu slunce
3. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90

A: 2, je to nejlepší prompt, protože poskytuje podrobnosti o "čem" a jde do specifik (nejen jakékoliv auto, ale konkrétní značka a model) a také popisuje celkové prostředí. 3 je další nejlepší, protože také obsahuje hodně popisu.

## 🚀 Výzva

Zkuste využít techniku "podnětu" s promptem: Dokončete větu "Ukaž mi obrázek červeného auta značky Volvo a ". Jak na to odpovídá a jak byste to vylepšili?

## Skvělá práce! Pokračujte ve svém učení

Chcete se dozvědět více o různých konceptech vytváření promptů? Přejděte na [stránku pro pokračující učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a najděte další skvělé zdroje na toto téma.

Přejděte na lekci 5, kde se podíváme na [pokročilé techniky vytváření promptů](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.