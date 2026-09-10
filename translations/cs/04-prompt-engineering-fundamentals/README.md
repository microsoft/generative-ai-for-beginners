# Základy inženýrství promptů

[![Základy inženýrství promptů](../../../translated_images/cs/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrývá základní pojmy a techniky pro vytváření efektivních promptů v generativních AI modelech. Záleží také na tom, jak napíšete svůj prompt pro LLM. Pečlivě vytvořený prompt může dosáhnout lepší kvality odpovědi. Co však přesně znamenají pojmy jako _prompt_ a _inženýrství promptů_? A jak mohu zlepšit promptový _vstup_, který posílám do LLM? Na tyto otázky se pokusíme odpovědět v této kapitole a následující.

_Generativní AI_ je schopna vytvářet nový obsah (např. text, obrázky, zvuk, kód atd.) v reakci na uživatelské požadavky. Dosahuje toho pomocí _velkých jazykových modelů_ jako je série GPT od OpenAI („Generative Pre-trained Transformer“), které jsou trénovány k používání přirozeného jazyka a kódu.

Uživatelé nyní mohou komunikovat s těmito modely pomocí známých paradigmat, jako je chat, bez nutnosti technických znalostí či školení. Modely jsou založené na _promptech_ – uživatelé pošlou textový vstup (prompt) a obdrží odpověď AI (kompletaci). Následně mohou s AI „chatovat“ iterativně, v několika kolech konverzace, zdokonalovat svůj prompt až dokud odpověď nebude vyhovovat jejich očekáváním.

„Prompty“ se nyní stávají primárním _programovacím rozhraním_ pro aplikace generativní AI, říkají modelům, co mají dělat, a ovlivňují kvalitu vrácených odpovědí. „Inženýrství promptů“ je rychle rostoucí oblast studia, která se zaměřuje na _navrhování a optimalizaci_ promptů, aby dodávaly konzistentní a kvalitní odpovědi ve velkém měřítku.

## Cíle učení

V této lekci se naučíme, co je inženýrství promptů, proč je důležité a jak vytvářet efektivnější prompty pro daný model a cíl aplikace. Pochopíme základní koncepty a osvědčené postupy inženýrství promptů – a seznámíme se s interaktivním prostředím Jupyter Notebook, kde uvidíme tyto koncepty aplikované na reálných příkladech.

Na konci lekce budeme schopni:

1. Vysvětlit, co je inženýrství promptů a proč je důležité.
2. Popsat komponenty promptu a jak se používají.
3. Naučit se osvědčené postupy a techniky inženýrství promptů.
4. Aplikovat naučené techniky na reálných příkladech za použití OpenAI endpointu.

## Klíčové pojmy

Inženýrství promptů: Praxe navrhování a zdokonalování vstupů, aby AI modely generovaly požadované výstupy.
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model umí rozumět a zpracovat.
Instruction-Tuned LLMs: Velké jazykové modely (LLM), které byly doladěny specifickými instrukcemi pro zlepšení přesnosti a relevance odpovědí.

## Učební prostředí

Inženýrství promptů je zatím spíše umění než věda. Nejlepší cestou, jak zlepšit intuici, je _více praxe_ a přístup pokus-omyl, který kombinuje znalosti oboru s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook k této lekci poskytuje _sandbox_ prostředí, kde si můžete vyzkoušet, co jste se naučili – průběžně nebo jako součást úkolu na konci. Pro provádění cvičení potřebujete:

1. **Klíč Azure OpenAI API** – servisní endpoint pro nasazený LLM.
2. **Python runtime** – ve kterém lze Notebook spustit.
3. **Lokální proměnné prostředí** – _dokončete nyní kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), abyste se připravili_.

Notebook obsahuje _startovací_ cvičení, ale jste vyzváni, abyste přidali vlastní sekce s _Markdown_ (popisy) a _Kódem_ (promptové požadavky), vyzkoušeli tak více příkladů nebo nápadů a budovali intuici pro návrh promptů.

## Ilustrovaný průvodce

Chcete získat přehled o tom, co lekce pokrývá, než začnete? Podívejte se na tento ilustrovaný průvodce, který vám ukáže hlavní témata a klíčové postřehy, nad kterými se můžete zamyslet. Plán lekce vás provede od pochopení základních konceptů a výzev k jejich řešení pomocí relevantních technik inženýrství promptů a osvědčených postupů. Sekce „Pokročilé techniky“ v tomto průvodci odkazuje na obsah pokrytý v _následující_ kapitole tohoto kurzu.

![Ilustrovaný průvodce inženýrstvím promptů](../../../translated_images/cs/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naše startupová mise

Nyní si povíme, jak _toto téma_ souvisí s naší startupovou misí [přinést inovace AI do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvářet AI-řízené aplikace pro _personalizované učení_ – tak přemýšlejme, jak by různí uživatelé naší aplikace mohli „navrhovat“ prompty:

- **Administrátoři** mohou požádat AI o _analýzu dat kurikula za účelem identifikace mezer v obsahovém pokrytí_. AI může výsledky shrnout nebo je vizualizovat pomocí kódu.
- **Pedagogové** mohou požádat AI o _vytvoření plánu lekce pro konkrétní cílovou skupinu a téma_. AI může vytvořit personalizovaný plán ve specifikovaném formátu.
- **Studenti** mohou požádat AI, aby je _doučovala v obtížném předmětu_. AI může nyní studenty vést lekcemi, nápovědami a příklady přizpůsobenými jejich úrovni.

To je jen špička ledovce. Podívejte se na [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – open-source knihovnu promptů sestavenou odborníky na vzdělávání – pro širší představu o možnostech! _Zkuste některé z těchto promptů v sandboxu nebo v OpenAI Playground a uvidíte, co se stane!_

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrýt základní koncept #1.
Posílit koncept příklady a odkazy.

KONCEPT #1:
Inženýrství promptů.
Definujte a vysvětlete, proč je potřeba.
-->

## Co je inženýrství promptů?

Tuto lekci jsme začali definicí **inženýrství promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů), aby poskytly konzistentní a kvalitní odpovědi (kompletace) pro daný cíl aplikace a model. Můžeme to chápat jako dvoufázový proces:

- _navrhování_ počátečního promptu pro daný model a cíl
- _iterativní zdokonalování_ promptu k lepší kvalitě odpovědi

Je to nutně proces pokusů a omylů, který vyžaduje uživatelskou intuici a úsilí k dosažení optimálních výsledků. Proč je tedy důležitý? Odpověď vyžaduje pochopení tří konceptů:

- _Tokenizace_ = jak model „vidí“ prompt
- _Základní LLM_ = jak základní model „zpracovává“ prompt
- _Instruction-Tuned LLM_ = jak model nyní může vidět „úkoly“

### Tokenizace

LLM vidí prompty jako _sekvenci tokenů_, přičemž různé modely (nebo verze modelu) mohou stejný prompt tokenizovat různými způsoby. Protože LLM jsou trénovány na tokenech (a ne na surovém textu), způsob tokenizace promptů výrazně ovlivňuje kvalitu generované odpovědi.

Pro získání intuice o fungování tokenizace vyzkoušejte nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), ukázaný níže. Zkopírujte do něj svůj prompt a sledujte, jak je převeden na tokeny, věnujte pozornost tomu, jak se zpracovávají znaky mezer a interpunkce. Vezměte na vědomí, že tento příklad ukazuje starší LLM (GPT-3) – vyzkoušení s novějším modelem může přinést odlišný výsledek.

![Tokenizace](../../../translated_images/cs/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Základní modely (Foundation Models)

Jakmile je prompt tokenizován, hlavní funkcí ["Základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (nebo Foundation modelu) je předpovědět další token v sekvenci. Protože LLM jsou trénovány na obrovských textových datech, mají dobré povědomí o statistických vztazích mezi tokeny a dokážou tuto předpověď učinit s určitou důvěrou. Neznají _význam_ slov v promptu nebo tokenu; pouze vidí vzorec, který mohou „dokončit“ příští předpovědí. Mohou pokračovat v předpovídání sekvence, dokud uživatel nepřeruší nebo není splněna předem stanovená podmínka.

Chcete vidět, jak funguje kompletace na základě promptu? Zadejte výše uvedený prompt do [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) s výchozím nastavením. Systém je nastaven pro zpracování promptů jako požadavky na informace – takže byste měli vidět odpověď, která tomuto kontextu odpovídá.

Ale co když uživatel chce vidět něco konkrétního, co splňuje nějaká kritéria nebo cíl úkolu? Právě sem vstupují do hry _instruction-tuned_ LLM.

![Kompletace chatu Základním modelem LLM](../../../translated_images/cs/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction Tuned LLM

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) vychází ze základního modelu a dále jej optimalizuje pomocí příkladů nebo vstupně-výstupních párů (např. vícekrokových „zpráv“), které mohou obsahovat jasné instrukce – a odpověď AI se snaží těmto instrukcím vyhovět.

Toto využívá techniky jako Reinforcement Learning s lidskou zpětnou vazbou (RLHF), které dokážou naučit model _řídit se instrukcemi_ a _učit se z feedbacku_, takže produkuje odpovědi lépe vhodné pro praktické aplikace a relevantnější pro uživatelské cíle.

Vyzkoušejme to – vraťte se k předchozímu promptu, ale nyní změňte _systemovou zprávu_ tak, aby obsahovala následující instrukci jako kontext:

> _Shrň poskytnutý obsah pro žáka druhé třídy. Výsledek udrž na jeden odstavec se 3-5 odrážkami._

Vidíte, že výsledek je nyní laděný tak, aby odrážel požadovaný cíl a formát? Pedagog může tuto odpověď přímo použít do svých slidů pro hodinu.

![Kompletace chatu Instruction Tuned LLM](../../../translated_images/cs/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Proč potřebujeme inženýrství promptů?

Nyní, když víme, jak LLM zpracovávají prompty, pojďme si říct, _proč_ potřebujeme inženýrství promptů. Odpověď spočívá v tom, že současné LLM představují řadu výzev, které činí _spolehlivé a konzistentní odpovědi_ obtížnější bez námahy při konstrukci a optimalizaci promptů. Například:

1. **Odpovědi modelu jsou stochastické.** _Stejný prompt_ pravděpodobně vyprodukuje různé odpovědi s různými modely nebo verzemi modelu. A může dokonce produkovat různorodé výsledky i se _stejným modelem_ v různých časech. _Techniky inženýrství promptů nám mohou pomoci minimalizovat tyto variace tím, že nastaví lepší ochranné mantinely_.

1. **Modely mohou vymýšlet odpovědi.** Modely jsou předtrénovány na _velkých ale konečných_ datasetech, což znamená, že nemají znalosti o pojmech mimo rozsah tohoto tréninku. Výsledkem je, že mohou produkovat odpovědi, které jsou nepřesné, smyšlené nebo přímo v rozporu s ověřenými fakty. _Techniky inženýrství promptů pomáhají uživatelům tato vyjádření identifikovat a zmírnit, např. požadavkem na citace nebo zdůvodnění_.

1. **Schopnosti modelů se budou lišit.** Novější modely nebo generace modelů budou mít bohatší schopnosti, ale také specifické zvláštnosti a kompromisy v nákladech a složitosti. _Inženýrství promptů nám může pomoci vytvořit osvědčené postupy a pracovní postupy, které skryjí rozdíly a adaptují se na specifické požadavky modelů škálovatelným a plynulým způsobem_.

Podívejme se na to v praxi v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) – všimli jste si rozdílů?
- Použijte stejný prompt opakovaně se _stejným_ nasazením LLM (např. Azure OpenAI playground) – jak se tyto rozdíly lišily?

### Příklad vymýšlení (fabricace)

V tomto kurzu používáme termín **„fabricace“** k označení fenoménu, kdy LLM někdy generují fakticky nesprávné informace kvůli omezením ve svém tréninku nebo jiným podmínkám. Možná jste slyšeli tento jev nazývat _„halucinace“_ v populárních článcích nebo výzkumných pracích. Důrazně však doporučujeme používat termín _„fabricace“_, aby nedocházelo k antropomorfizaci chování přisuzováním lidské vlastnosti strojovému výsledku. Tím také podporujeme [zásady odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hlediska terminologie, vyhýbáme se výrazům, které mohou být v některých kontextech považovány za urážlivé nebo nevhodné.

Chcete pochopit, jak fabricace fungují? Představte si prompt, který instruuje AI vytvořit obsah pro neexistující téma (aby se zajistilo, že není v tréninkovém datasetu). Například – vyzkoušel jsem tento prompt:

> **Prompt:** vytvoř plán lekce o Marsovské válce roku 2076.

Webové vyhledávání mi ukázalo, že existují fiktivní příběhy (např. televizní seriály nebo knihy) o marsovských válkách – ale žádné z roku 2076. Zdravý rozum nám také říká, že rok 2076 je _v budoucnosti_ a tudíž nemůže být spojen s reálnou událostí.


Co se tedy stane, když spustíme tento prompt u různých poskytovatelů LLM?

> **Odpověď 1**: OpenAI Playground (GPT-35)

![Odpověď 1](../../../translated_images/cs/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpověď 2**: Azure OpenAI Playground (GPT-35)

![Odpověď 2](../../../translated_images/cs/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpověď 3**: : Hugging Face Chat Playground (LLama-2)

![Odpověď 3](../../../translated_images/cs/04-fabrication-huggingchat.faf82a0a51278956.webp)

Jak se dalo očekávat, každý model (nebo verze modelu) produkuje mírně odlišné odpovědi díky stochastickému chování a rozdílům ve schopnostech modelu. Například jeden model cílí na publikum na úrovni osmé třídy, zatímco jiný předpokládá středoškolského studenta. Všechny tři modely však vytvořily odpovědi, které by mohly přesvědčit neinformovaného uživatele, že událost byla skutečná.

Techniky prompt engineeringu, jako jsou _metaprompting_ a _nastavení teploty_, mohou do jisté míry snížit fabrication modelu. Nové _architektury_ prompt engineeringu také bezproblémově začleňují nové nástroje a techniky do promptu, aby zmírnily nebo snížily některé z těchto efektů.

## Případová studie: GitHub Copilot

Uzavřeme tuto sekci tím, že si uděláme představu o tom, jak se prompt engineering využívá v reálných řešeních, a podíváme se na jednu případovou studii: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš "AI pár programátor" - převádí textové prompt do dokončení kódu a je integrován do vašeho vývojového prostředí (například Visual Studio Code) pro bezproblémový uživatelský zážitek. Jak je zdokumentováno v sérii blogů níže, nejranější verze byla založena na modelu OpenAI Codex - a inženýři rychle pochopili potřebu doladění modelu a vývoje lepších technik prompt engineeringu, aby zlepšili kvalitu kódu. V červenci představili [vylepšený AI model, který jde nad rámec Codexu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pro ještě rychlejší návrhy.

Přečtěte si příspěvky v pořadí, abyste sledovali jejich vývojovou cestu.

- **květen 2023** | [GitHub Copilot se zlepšuje v porozumění vašeho kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **květen 2023** | [Uvnitř GitHubu: Práce s LLM za GitHub Copilotem](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **červen 2023** | [Jak psát lepší prompty pro GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **červenec 2023** | [.. GitHub Copilot jde nad rámec Codexu s vylepšeným AI modelem](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **červenec 2023** | [Průvodce vývojáře prompt engineeringem a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **září 2023** | [Jak vytvořit podnikatelskou LLM aplikaci: Lekce od GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Můžete také procházet jejich [Inženýrský blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pro další příspěvky jako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), který ukazuje, jak jsou tyto modely a techniky _používány_ k řízení reálných aplikací.

---

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrýt základní koncept č. 2.
Posilte koncept příklady a odkazy.

KONCEPT #2:
Návrh promptu.
Ilustrováno příklady.
-->

## Konstrukce promptu

Viděli jsme, proč je prompt engineering důležitý – nyní pochopíme, jak jsou prompt konstruovány, abychom mohli hodnotit různé techniky pro efektivnější návrh promptu.

### Základní prompt

Začneme se základním promptem: textovým vstupem poslaným modelu bez dalšího kontextu. Zde je příklad – když pošleme prvních pár slov americké národní hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ihned dokončí odpověď několika dalšími řádky, což ilustruje základní predikční chování.

| Prompt (Vstup)         | Dokončení (Výstup)                                                                                                                        |
| :-----------------   | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see    | Zdá se, že začínáte zpívat text "The Star-Spangled Banner", národní hymny Spojených států. Celý text je ...                             |

### Komplexní prompt

Nyní přidáme ke základnímu promptu kontext a instrukce. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje konstruovat komplexní prompt jako kolekci _zpráv_ obsahujících:

- Páry vstupů/výstupů reflektující _uživatelský_ vstup a _asistentovu_ odpověď.
- Systémová zpráva nastavující kontext chování nebo osobnosti asistenta.

Požadavek má nyní níže uvedenou podobu, kde _tokenizace_ účinně zachycuje relevantní informace z kontextu a konverzace. Změna systémového kontextu může mít stejně výrazný dopad na kvalitu dokončení jako poskytované uživatelské vstupy.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukční prompt

Ve výše uvedených příkladech byl uživatelský prompt jednoduchý textový dotaz, který lze interpretovat jako žádost o informace. S _instrukčními_ promptami můžeme tento text použít k podrobnějšímu specifikování úkolu a tak poskytnout AI lepší vedení. Zde je příklad:

| Prompt (Vstup)                                                                                                                                                                                                                           | Dokončení (Výstup)                                                                                               | Typ instrukce      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napiš popis občanské války                                                                                                                                                                                                              | _vrátil jednoduchý odstavec_                                                                                      | Jednoduchý          |
| Napiš popis občanské války. Uveď klíčová data a události a popiš jejich význam.                                                                                                                                                         | _vrátil odstavec následovaný seznamem klíčových dat událostí s popisy_                                             | Komplexní           |
| Napiš popis občanské války v 1 odstavci. Uveď 3 odrážky s klíčovými daty a jejich významem. Uveď 3 další odrážky s klíčovými historickými postavami a jejich přínosem. Výstup vrať jako JSON soubor | _vrací podrobnější informace v textovém poli, formátované jako JSON, které můžete zkopírovat a vložit do souboru a případně ověřit_ | Komplexní. Formátované. |

## Primární obsah

Ve výše uvedených příkladech byl prompt stále docela otevřený, což umožňovalo LLM rozhodnout, která část jeho předtrénovaného datasetu je relevantní. Se vzorem návrhu _primárního obsahu_ je vstupní text rozdělen na dvě části:

- instrukce (akce)
- relevantní obsah (který ovlivňuje akci)

Zde je příklad, kde instrukce je "shrň to ve 2 větách".

| Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Dokončení (Výstup)                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je pátou planetou od Slunce a největší v sluneční soustavě. Je to plynný obr s hmotností tisící části Slunce, ale dva a půlkrát větší než hmotnost všech ostatních planet sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je znám od dávných civilizací ještě před zaznamenanou historií. Je pojmenován po římském bohu Jupiterovi.[19] Při pohledu ze Země může být Jupiter dostatečně jasný, aby jeho odražené světlo vrhalo viditelné stíny,[20] a je v průměru třetím nejjasnějším přírodním objektem na noční obloze po Měsíci a Venuši. <br/> **Shrinkni to do 2 krátkých vět** | Jupiter, pátá planeta od Slunce, je největší v sluneční soustavě a je známý jako jeden z nejjasnějších objektů na noční obloze. Pojmenovaný po římském bohu Jupiterovi, je to plynný obr, jehož hmotnost je dva a půlkrát větší než všech ostatních planet v sluneční soustavě dohromady. |

Segment primárního obsahu může být použit různými způsoby k efektivnějšímu řízení pokynů:

- **Příklady** - místo explicitního sdělení modelu, co má dělat, mu dejte příklady, co dělat, a nechte ho vzorec odvodit.
- **Návodné signály** - následujte instrukci "návodným signálem", který spustí dokončení a nasměruje model k relevantnějším odpovědím.
- **Šablony** - to jsou opakovatelné „recepty“ na prompty s proměnnými (placeholdry), které lze přizpůsobit daty pro konkrétní použití.

Pojďme si je vyzkoušet v praxi.

### Použití příkladů

Tento přístup používá primární obsah k "nakrmení modelu" několika příklady požadovaného výstupu pro danou instrukci a nechá ho vzorec odvodit. Podle počtu příkladů poskytovaných můžeme mít zero-shot prompting, one-shot prompting, few-shot prompting apod.

Prompt nyní obsahuje tři komponenty:

- Popis úkolu
- Několik příkladů požadovaného výstupu
- Začátek nového příkladu (který se stává implicitním popisem úkolu)

| Typ učení   | Prompt (Vstup)                                                                                                                                      | Dokončení (Výstup)       |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------ |
| Zero-shot  | "The Sun is Shining". Přelož do španělštiny                                                                                                        | "El Sol está brillando".  |
| One-shot   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                               | "Es un día frío y ventoso". |
| Few-shot   | Hráč běžel po metách => Baseball <br/> Hráč zahrál eso => Tenis <br/> Hráč zahrál šestku => Kriket <br/> Hráč dal smeč =>                          | Basketbal                |
|             |                                                                                                                                                   |                           |

Všimněte si, že u zero-shot promptingu jsme museli poskytnout explicitní instrukci („Přelož do španělštiny“), ale při one-shot promptingu je to odvozeno z příkladu. Příklad few-shot ukazuje, jak přidání více příkladů umožňuje modelům dělat přesnější odhady bez nutnosti dalších instrukcí.

### Návodné signály promptu

Další technikou použití primárního obsahu je poskytování _návodných signálů_ místo příkladů. V tomto případě dáváme modelu jemný podnět správným směrem _začátkem_ útržku, který odráží požadovaný formát odpovědi. Model pak „vezme návladní signál“ a pokračuje v daném duchu.

| Počet návladních signálů | Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                        | Dokončení (Výstup)                                                                                                                                                                                                                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                        | Jupiter je pátou planetou od Slunce a největší v sluneční soustavě. Je to plynný obr s hmotností tisící části Slunce, ale dva a půlkrát větší než hmotnost všech ostatních planet sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je znám od dávných civilizací ještě před zaznamenanou historií. <br/>**Shrň to**                 | Jupiter je největší planeta naší sluneční soustavy a pátá od Slunce. Je to plynný obr s hmotností 1/1000 Slunce, ale těžší než všechny ostatní planety dohromady. Dávné civilizace znaly Jupiter dlouho a je snadno viditelný na noční obloze.                      |
| 1                        | Jupiter je pátou planetou od Slunce a největší v sluneční soustavě. Je to plynný obr s hmotností tisící části Slunce, ale dva a půlkrát větší než hmotnost všech ostatních planet sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je znám od dávných civilizací ještě před zaznamenanou historií. <br/>**Shrň to** <br/> Co jsme se dozvěděli je, že Jupiter | je pátou planetou od Slunce a největší v sluneční soustavě. Je to plynný obr s hmotností tisící části Slunce, ale dva a půlkrát větší než hmotnost všech ostatních planet dohromady. Je snadno viditelný pouhým okem a je znám od starověku.                        |

| 2              | Jupiter je pátá planeta od Slunce a největší v sluneční soustavě. Je to plynný obr s hmotností jedna tisícina Slunce, ale dvakrát a půl větší než všechny ostatní planety sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je známý starověkým civilizacím již před zaznamenanou historií. <br/>**Shrňte toto** <br/> Tři nejdůležitější fakta, která jsme se naučili:         | 1. Jupiter je pátá planeta od Slunce a největší v sluneční soustavě. <br/> 2. Je to plynný obr s hmotností jedna tisícina Slunce...<br/> 3. Jupiter je pouhým okem viditelný už od starověku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablony promptů

Šablona promptu je _předem definovaný recept na prompt_, který může být uložen a znovu použit podle potřeby, aby se zajistila konzistentnější uživatelská zkušenost ve velkém měřítku. V nejjednodušší podobě je to kolekce příkladů promptů jako [tento od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), která poskytuje jak interaktivní komponenty promptů (uživatelské a systémové zprávy), tak formát požadavku řízený API - pro podporu opakovaného použití.

Ve složitější podobě jako [tento příklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) obsahuje _zástupné symboly_, které mohou být nahrazeny daty z různých zdrojů (uživatelský vstup, systémový kontext, externí datové zdroje atd.) pro dynamické generování promptu. To nám umožňuje vytvářet knihovnu znovu použitelných promptů, které lze použít k programovému řízení konzistentních uživatelských zážitků ve velkém měřítku.

Nakonec skutečná hodnota šablon spočívá v možnosti vytvářet a zveřejňovat _knihovny promptů_ pro vertikální aplikační oblasti - kde je šablona promptu nyní _optimalizována_ tak, aby odrážela kontext specifický pro aplikaci nebo příklady, které dělají odpovědi relevantnější a přesnější pro cílové uživatelské publikum. Repozitář [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, který kurátoruje knihovnu promptů pro oblast vzdělávání se zaměřením na klíčové cíle jako plánování lekcí, návrh osnov, doučování studentů atd.

## Podpůrný obsah

Pokud uvažujeme o konstrukci promptu jako o instrukci (úkolu) a cíli (primárním obsahu), pak _sekundární obsah_ je jako dodatečný kontext, který poskytujeme k **ovlivnění výstupu způsobem**. Může to být ladicí parametry, instrukce pro formátování, taxonomie témat atd., které mohou pomoci modelu _přizpůsobit_ jeho odpověď tak, aby vyhovovala požadovaným uživatelským cílům nebo očekáváním.

Například: Máme katalog kurzů s rozsáhlými metadaty (název, popis, úroveň, tagy metadat, lektor atd.) o všech dostupných kurzech v osnově:

- můžeme definovat instrukci „shrň katalog kurzů pro podzim 2023“
- můžeme použít primární obsah k poskytnutí několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci 5 nejdůležitějších „tagů“

Nyní může model poskytnout shrnutí ve formátu ukázaném v několika příkladech - ale pokud má výsledek více tagů, může upřednostnit těchto 5 tagů uvedených v sekundárním obsahu.

---

<!--
ŠABLONA LEKCE:
Tento blok by měl pokrýt základní koncept #1.
Upevněte koncept příklady a odkazy.

KONCEPT #3:
Techniky prompt engineeringu.
Jaké jsou základní techniky prompt engineeringu?
Ilustrujte to několika cvičeními.
-->

## Nejlepší postupy při promptování

Nyní, když víme, jak mohou být prompty _konstruovány_, můžeme začít přemýšlet o tom, jak je _navrhovat_ tak, aby odrážely nejlepší praxe. Můžeme to rozdělit na dvě části - mít správný _přístup_ a aplikovat správné _techniky_.

### Přístup k prompt engineeringu

Prompt engineering je proces pokus-omyl, proto si mějte na paměti tři široké vodítka:

1. **Porozumění doméně je důležité.** Přesnost a relevance odpovědi závisí na _doméně_, ve které daná aplikace nebo uživatel operuje. Použijte svou intuici a odbornost v dané oblasti k dalšímu **přizpůsobení technik**. Například definujte _osobnosti specifické pro doménu_ ve svých systémových promptech nebo použijte _šablony specifické pro doménu_ ve svých uživatelských promptech. Poskytněte sekundární obsah, který odráží kontext specifický pro doménu, nebo použijte _výzvy a příklady specifické pro doménu_, abyste nasměrovali model k známým vzorcům použití.

2. **Porozumění modelu je důležité.** Víme, že modely jsou ze své podstaty stochastické. Ale implementace modelů se mohou lišit podle použitého tréninkového datasetu (předtrénované znalosti), možností, které poskytují (např. přes API nebo SDK) a typu obsahu, pro který jsou optimalizovány (např. kód versus obrázky versus text). Pochopte silné stránky a omezení modelu, který používáte, a použijte tyto znalosti k _prioritizaci úkolů_ nebo vytváření _vlastních šablon_ optimalizovaných pro schopnosti modelu.

3. **Iterace a validace jsou důležité.** Modely se rychle vyvíjejí, stejně tak techniky prompt engineeringu. Jako odborník na doménu můžete mít další kontext nebo kritéria pro _vaši_ konkrétní aplikaci, které nemusí platit pro širší komunitu. Používejte nástroje a techniky prompt engineeringu k „rychlému spuštění“ konstrukce promptů, pak výsledky iterujte a validujte pomocí vlastní intuice a odbornosti v doméně. Zaznamenávejte své poznatky a vytvářejte **databázi znalostí** (např. knihovny promptů), která může být použita jako nová základna ostatními pro rychlejší iterace v budoucnu.

## Nejlepší postupy

Podívejme se nyní na běžné nejlepší postupy doporučované praktiky [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                              | Proč                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnocujte nejnovější modely.       | Nové generace modelů pravděpodobně přinesou vylepšené funkce a kvalitu - mohou však také znamenat vyšší náklady. Vyhodnoťte jejich dopad a poté se rozhodněte o migraci.                                                                                |
| Oddělujte instrukce a kontext   | Zkontrolujte, zda váš model / poskytovatel definuje _oddělovače_ pro jasnější rozlišení instrukcí, primárního a sekundárního obsahu. To pomáhá modelům přesněji přiřazovat váhy tokenům.                                                         |
| Buďte specifický a jasný             | Poskytněte více podrobností o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší jak kvalitu, tak konzistenci odpovědí. Zachyťte recepty v znovu použitelných šablonách.                                                          |
| Buďte popisní, používejte příklady      | Modely mohou lépe reagovat na přístup „ukázat a říct“. Začněte `zero-shot` přístupem, kdy jim dáte instrukci (ale žádné příklady), pak zkusíte `few-shot` jako vylepšení, kde poskytnete několik příkladů požadovaného výstupu. Použijte analogie. |
| Používejte výzvy k nastartování dokončení | Nasměrujte model k požadovanému výsledku tím, že mu dáte několik úvodních slov nebo frází, které může použít jako výchozí bod pro odpověď.                                                                                                               |
| Zdvojnásobte to                       | Někdy je potřeba modelu instrukci zopakovat. Dejte pokyny před i po primárním obsahu, použijte instrukci a výzvu, atd. Iterujte a validujte, co funguje.                                                         |
| Pořadí má význam                     | Pořadí, ve kterém modelu předkládáte informace, může ovlivnit výsledky, dokonce i u učebních příkladů, díky novějším informacím v paměti. Zkoušejte různé možnosti, co funguje nejlépe.                                                               |
| Dejte modelu „únik“           | Dejte modelu _náhradní_ odpověď, kterou může poskytnout, pokud nemůže z jakéhokoli důvodu úkol dokončit. To snižuje pravděpodobnost generování falešných nebo vymyšlených odpovědí.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Jako u jakékoli nejlepší praktiky nezapomeňte, že _vlastní zkušenosti se mohou lišit_ podle modelu, úkolu a domény. Používejte tyto tipy jako výchozí bod a iterujte, abyste zjistili, co je pro vás nejlepší. Neustále přehodnocujte svůj proces prompt engineeringu, jakmile jsou k dispozici nové modely a nástroje, se zaměřením na škálovatelnost procesu a kvalitu odpovědí.

<!--
ŠABLONA LEKCE:
Tento blok by měl obsahovat úkol s kódem, pokud je relevantní

ÚKOL:
Odkaz na Jupyter Notebook, který obsahuje pouze komentáře kódu v instrukcích (sekce kódu jsou prázdné).

ŘEŠENÍ:
Odkaz na kopii tohoto notebooku s vyplněnými prompti, spuštěnou ukázkou jednoho příkladu.
-->

## Zadání

Gratulujeme! Dostali jste se na konec lekce! Je čas otestovat některé z těchto konceptů a technik na reálných příkladech!

Pro naše zadání budeme používat Jupyter Notebook s cvičeními, která můžete dokončit interaktivně. Notebook můžete také rozšířit vlastními Markdown a kódovými buňkami pro vlastní zkoumání nápadů a technik.

### Pro začátek, forkni repo, pak

- (Doporučeno) Spusťte GitHub Codespaces
- (Alternativně) Naklonujte repo do svého lokálního zařízení a použijte ho s Docker Desktopem
- (Alternativně) Otevřete notebook ve svém preferovaném prostředí pro běh notebooků.

### Dále nastavte své proměnné prostředí

- Zkopírujte soubor `.env.copy` v kořenovém adresáři repozitáře do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Poté se vraťte do [sekce Learning Sandbox](#učební-prostředí) a naučte se, jak na to.

### Dále otevřete Jupyter Notebook

- Vyberte runtime kernel. Pokud používáte možnosti 1 nebo 2, jednoduše vyberte výchozí Python 3.10.x kernel poskytovaný vývojovým kontejnerem.

Jste připraveni spustit cvičení. Poznámka, že neexistují _správné a nesprávné_ odpovědi - jde pouze o průzkum pomocí pokus-omyl a budování intuice, co funguje pro daný model a aplikační doménu.

_Z tohoto důvodu v této lekci nebudou sekce s řešením kódu. Místo toho bude notebook obsahovat Markdown buňky s nadpisem „Moje řešení:“, které ukáží jeden příklad výstupu pro referenci._

 <!--
ŠABLONA LEKCE:
Uzavřete sekci shrnutím a zdroji pro samostatné učení.
-->

## Kontrola znalostí

Který z následujících promptů je dobrý podle rozumných nejlepších praktik?

1. Ukázat mi obrázek červeného auta
2. Ukázat mi obrázek červeného auta značky Volvo a model XC90 zaparkovaného u útesu při západu slunce
3. Ukázat mi obrázek červeného auta značky Volvo a model XC90

A: 2, je to nejlepší prompt, protože poskytuje podrobnosti o „co“ a jde do specifik (ne jen jakékoliv auto, ale konkrétní značka a model) a také popisuje celkové prostředí. 3 je druhý nejlepší, protože také obsahuje hodně popisu.

## 🚀 Výzva

Zkuste využít techniku „výzvy“ s promptem: Dokončete větu „Ukázat mi obrázek červeného auta značky Volvo a “. Co odpoví a jak byste to vylepšili?

## Skvělá práce! Pokračujte ve vzdělávání

Chcete se dozvědět více o různých konceptech prompt engineeringu? Přejděte na [stránku pokračujícího učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a najděte další skvělé zdroje na toto téma.

Přejděte na Lekci 5, kde se podíváme na [pokročilé techniky promptování](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->