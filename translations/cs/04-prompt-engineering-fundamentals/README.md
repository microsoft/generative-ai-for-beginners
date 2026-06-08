# Základy návrhu promptů

[![Základy návrhu promptů](../../../translated_images/cs/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrývá základní koncepty a techniky vytváření efektivních promptů v generativních AI modelech. Způsob, jakým napíšete svůj prompt pro LLM, také hraje roli. Pečlivě sestavený prompt může dosáhnout lepší kvality odpovědi. Ale co přesně znamenají pojmy jako _prompt_ a _návrh promptů_? A jak zlepšit prompt _vstup_, který posílám do LLM? To jsou otázky, na které se pokusíme odpovědět v této kapitole a v té následující.

_Generativní AI_ je schopná vytvářet nový obsah (např. text, obrázky, zvuk, kód atd.) v reakci na uživatelské požadavky. Dosahuje toho prostřednictvím _velkých jazykových modelů_ jako je série OpenAI GPT („Generative Pre-trained Transformer“), které jsou trénovány na práci s přirozeným jazykem a kódem.

Uživatelé nyní mohou s těmito modely komunikovat pomocí známých paradigmat, jako je chat, bez nutnosti technických znalostí nebo školení. Modely jsou _postaveny na promptech_ – uživatelé posílají textový vstup (prompt) a dostávají odpověď AI (completion). Mohou pak iterativně „chatovat s AI“ v několika krocích, upravovat prompt, dokud odpověď nesplní jejich očekávání.

„Prompty“ se nyní stávají hlavním _programovacím rozhraním_ pro aplikace generativní AI, říkají modelům, co mají dělat, a ovlivňují kvalitu vrácených odpovědí. „Návrh promptů“ je rychle rostoucí oblast studia zaměřená na _navrhování a optimalizaci_ promptů tak, aby poskytovaly konzistentní a kvalitní odpovědi ve velkém měřítku.

## Výukové cíle

V této lekci se naučíme, co je návrh promptů, proč je důležitý a jak můžeme vytvořit efektivnější prompty pro daný model a cíl aplikace. Pochopíme základní koncepty a osvědčené postupy návrhu promptů – a seznámíme se s interaktivním prostředím Jupyter Notebook „sandbox“, ve kterém můžeme tyto koncepty aplikovat na reálných příkladech.

Na konci této lekce budeme umět:

1. Vysvětlit, co je návrh promptů a proč je důležitý.
2. Popsat složky promptu a jak se používají.
3. Naučit se osvědčené postupy a techniky návrhu promptů.
4. Aplikovat naučené techniky na reálné příklady pomocí OpenAI endpointu.

## Klíčové pojmy

Návrh promptů: Praktika navrhování a zdokonalování vstupů za účelem nasměrování AI modelů k produkci požadovaných výstupů.  
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model může chápat a zpracovávat.  
Instruction-Tuned LLMs: Velké jazykové modely (LLM), které byly doladěny pomocí specifických instrukcí ke zvýšení přesnosti a relevance jejich odpovědí.

## Výukový sandbox

Návrh promptů je zatím spíše umění než věda. Nejlepší způsob, jak zlepšit svoji intuici, je _praktikovat více_ a přijmout přístup pokus-omyl, který kombinuje odborné znalosti v dané oblasti s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook přiložený k této lekci poskytuje _sandbox_ prostředí, kde můžete zkoušet, co se naučíte – jak postupně, tak i jako součást kódovací výzvy na konci. K provedení cvičení budete potřebovat:

1. **Azure OpenAI API klíč** – službu s endpointem pro nasazený LLM.  
2. **Python runtime** – ve kterém lze Notebook spustit.  
3. **Místní prostředí proměnných** – _dokončete nyní kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), abyste se připravili_.

Notebook obsahuje _startovací_ cvičení – ale jste povzbuzováni přidávat vlastní _Markdown_ (popisky) a _Code_ (promptové dotazy), abyste vyzkoušeli více příkladů nebo nápadů a budovali si intuici pro návrh promptů.

## Ilustrovaný průvodce

Chcete získat celkový přehled o tom, co tato lekce pokrývá ještě před tím, než do ní ponoříte? Podívejte se na tento ilustrovaný průvodce, který vám poskytne představu o hlavních tématech a klíčových myšlenkách, nad kterými můžete přemýšlet. Plán lekce vás provede od pochopení základních konceptů a výzev až po jejich řešení pomocí relevantních technik návrhu promptů a osvědčených postupů. Upozorňujeme, že sekce „Pokročilé techniky“ v tomto průvodci odkazuje na obsah pokrytý v _následující_ kapitole tohoto kurzu.

![Ilustrovaný průvodce návrhem promptů](../../../translated_images/cs/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naše startup

Nyní si povíme, jak _toto téma_ souvisí s misí našeho startupu [přinést AI inovace do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vyvíjet AI aplikace zaměřené na _personalizované učení_ – pojďme tedy přemýšlet o tom, jak by různí uživatelé naší aplikace mohli „navrhovat“ prompty:

- **Administrátoři** mohou požádat AI o _analýzu dat učebních plánů za účelem identifikace mezer ve výuce_. AI může shrnout výsledky nebo je vizualizovat kódem.  
- **Učitelé** mohou požádat AI o _generování plánu lekce pro cílové publikum a téma_. AI může vytvořit personalizovaný plán ve specifikovaném formátu.  
- **Studenti** mohou požádat AI o _doučování v obtížném předmětu_. AI je nyní může vést s lekcemi, nápovědou a příklady přizpůsobenými jejich úrovni.

To je jen špička ledovce. Mrkněte na [Prompty pro vzdělávání](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – otevřenou knihovnu promptů, kterou spravují odborníci na vzdělávání – abyste získali širší představu o možnostech! _Vyzkoušejte spuštění některých z těchto promptů v sandboxu nebo v OpenAI Playground a uvidíte, co se stane!_

<!--
LESSON TEMPLATE:
Tato jednotka by měla pokrýt základní koncept #1.
Podpořte koncept příklady a odkazy.

KONCEPT #1:
Návrh promptů.
Definujte to a vysvětlete, proč je to potřeba.
-->

## Co je návrh promptů?

Lekci jsme začali definicí **Návrhu promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů) pro dosažení konzistentních a kvalitních odpovědí (completion) pro daný cíl aplikace a model. Můžeme si to představit jako dvoukrokový proces:

- _navrhování_ počátečního promptu pro daný model a cíl  
- _zdokonalování_ promptu iterativně za účelem zlepšení kvality odpovědi

Jedná se nutně o proces založený na pokusu a omylu vyžadující uživatelskou intuici a úsilí k dosažení optimálních výsledků. Proč je to tedy důležité? Abychom na to odpověděli, musíme nejprve pochopit tři koncepty:

- _tokenizace_ = jak model „vidí“ prompt  
- _základní LLM_ = jak základní model „zpracovává“ prompt  
- _instruction-tuned LLM_ = jak model nyní dokáže vidět „úkoly“

### Tokenizace

LLM vidí prompt jako _sekvenci tokenů_, kde různé modely (nebo verze modelu) mohou tentýž prompt tokenizovat různými způsoby. Jelikož LLM jsou trénovány na tokenech (a ne na surovém textu), způsob tokenizace promptů přímo ovlivňuje kvalitu generované odpovědi.

Chcete-li získat představu o tom, jak tokenizace funguje, vyzkoušejte nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zobrazený níže. Zkopírujte svůj prompt a uvidíte, jak je převeden na tokeny, sledujte, jak jsou zpracovány mezery a interpunkční znaménka. Všimněte si, že tento příklad ukazuje starší LLM (GPT-3) – u novějších modelů může výsledek vypadat jinak.

![Tokenizace](../../../translated_images/cs/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Základní modely

Jakmile je prompt tokenizován, hlavní funkcí ["základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (nebo základního modelu) je predikovat další token v sekvenci. Protože LLM jsou trénovány na obrovských textových datech, mají dobrou představu o statistických vztazích mezi tokeny a mohou tuto predikci učinit s nějakou mírou jistoty. Všimněte si, že nerozumí _významu_ slov v promptu nebo tokenu; vidí pouze vzor, který mohou „dokončit“ svým dalším předpovězeným tokenem. Mohou v predikci pokračovat, dokud uživatel nezastaví proces nebo nedojde k nějaké předem dané podmínce.

Chcete vidět, jak funguje doplňování založené na promptu? Zadejte výše uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s výchozím nastavením. Systém je nastaven tak, aby bral prompty jako požadavky na informace – takže byste měli vidět doplnění, které odpovídá tomuto kontextu.

Co ale když uživatel chce vidět něco specifického, co splňuje nějaká kritéria nebo cíl úkolu? Právě zde přicházejí na scénu _instruction-tuned_ LLM.

![Doplňování základního LLM chatu](../../../translated_images/cs/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction Tuned LLM

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) vychází ze základního modelu a doladí jej pomocí příkladů nebo vstupně-výstupních párů (např. vícekrokové „zprávy“), které mohou obsahovat jasné instrukce – a odpověď AI se snaží těmto instrukcím vyhovět.

Používá techniky jako je posilované učení s lidskou zpětnou vazbou (RLHF), které trénují model, aby _následoval instrukce_ a _učil se ze zpětné vazby_, takže vytváří odpovědi lépe přizpůsobené praktickým aplikacím a relevantnější uživatelským cílům.

Vyzkoušejme to – vraťte se k výše uvedenému promptu, ale nyní změňte _systémovou zprávu_, aby poskytla následující instrukci jako kontext:

> _Shrňte obsah, který vám je poskytnut, pro žáka druhé třídy. Výsledek udržte v jednom odstavci s 3-5 odrážkami._

Vidíte, jak je výsledek nyní laděn tak, aby odrážel požadovaný cíl a formát? Učitel může tuto odpověď přímo použít ve své prezentaci na danou hodinu.

![Doplňování instruction tuned LLM chatu](../../../translated_images/cs/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Proč potřebujeme návrh promptů?

Nyní, když víme, jak jsou prompt zpracovány LLM, pojďme si povědět, _proč_ návrh promptů potřebujeme. Odpověď spočívá v tom, že současné LLM představují řadu výzev, které ztěžují dosažení _spolehlivých a konzistentních doplnění_ bez vynaložení úsilí na konstrukci a optimalizaci promptů. Například:

1. **Odpovědi modelu jsou stochastické.** _Stejný prompt_ pravděpodobně vyprodukuje různé odpovědi u různých modelů nebo jejich verzí. A může dokonce dát jiné výsledky při opakovaném použití _tohoto samého modelu_. _Techniky návrhu promptů nám mohou pomoci minimalizovat tyto odchylky tím, že poskytneme lepší kontrolní mechanismy_.

1. **Modely mohou vyrábět odpovědi.** Modely jsou předtrénovány na _velkých, ale omezených_ datech, tudíž nemají znalosti o konceptech mimo rozsah tréninku. Výsledkem může být produkce odpovědí, které jsou nepřesné, smyšlené nebo přímo v rozporu s fakty. _Techniky návrhu promptů pomáhají uživatelům odhalit a zmírnit takové smyšlenky, například žádáním AI o citace nebo odůvodnění_.

1. **Schopnosti modelů se liší.** Novější modely nebo generace modelů mají širší schopnosti, ale zároveň přinášejí specifické zvláštnosti a kompromisy v nákladech a složitosti. _Návrh promptů nám může pomoci vyvinout osvědčené postupy a pracovní toky, které abstraktně překrývají rozdíly a přizpůsobují se požadavkům specifickým pro modely v škálovatelných a plynulých způsobech_.

Podívejme se na to v praxi v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) – viděli jste rozdíly?  
- Použijte stejný prompt opakovaně u _tohoto samého_ nasazení LLM (např. Azure OpenAI playground) – jak se tyto rozdíly projevily?

### Příklad smyšlenek

V tomto kurzu používáme termín **„smyšlenka“** k označení jevu, kdy LLM občas generují fakticky nesprávné informace kvůli omezením ve svém tréninku nebo jiným omezením. Toto jste možná slyšeli označovat jako _„halucinace“_ v populárních článcích či výzkumných pracích. Nicméně důrazně doporučujeme používat termín _„smyšlenka“_, aby nedocházelo k antropomorfizaci chování přisuzováním lidské vlastnosti výsledku strojového zpracování. Tím také posilujeme [zásady odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hlediska terminologie, odstraněním termínů, které mohou být v některých kontextech považovány za urážlivé nebo neinkluzivní.

Chcete si udělat představu, jak smyšlenky fungují? Představte si prompt, který instruuje AI generovat obsah k neexistujícímu tématu (aby bylo jisté, že se v tréninkových datech nenachází). Například – vyzkoušel jsem tento prompt:

> **Prompt:** vytvoř plán lekce o marsovské válce roku 2076.
Webové vyhledávání mi ukázalo, že existovaly fiktivní příběhy (např. televizní seriály nebo knihy) o martianských válkách – ale žádné z roku 2076. Zdravý rozum nám také říká, že rok 2076 je _v budoucnosti_ a proto nemůže být spojován s reálnou událostí.

Co se tedy stane, když spustíme tento prompt u různých poskytovatelů LLM?

> **Odpověď 1**: OpenAI Playground (GPT-35)

![Odpověď 1](../../../translated_images/cs/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpověď 2**: Azure OpenAI Playground (GPT-35)

![Odpověď 2](../../../translated_images/cs/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpověď 3**: : Hugging Face Chat Playground (LLama-2)

![Odpověď 3](../../../translated_images/cs/04-fabrication-huggingchat.faf82a0a51278956.webp)

Jak se dalo očekávat, každý model (nebo verze modelu) generuje mírně odlišné odpovědi díky stochastickému chování a rozdílům ve schopnostech modelu. Například jeden model cílí na osmou třídu, zatímco druhý předpokládá středoškolského studenta. Ale všechny tři modely vytvořily odpovědi, které by mohly neinformovaného uživatele přesvědčit, že událost byla skutečná.

Techniky prompt engineeringu, jako je _metaprompting_ a _konfigurace teploty_, mohou do určité míry snižovat tvorbu nepravdivých informací modelem. Nové _architektury_ prompt engineeringu také bezproblémově začleňují nové nástroje a techniky do toku promptu, aby zmírnily nebo snížily některé z těchto efektů.

## Případová studie: GitHub Copilot

Zakončeme tuto sekci tím, že si uděláme představu, jak se prompt engineering používá v reálných řešeních, a podíváme se na jednu případovou studii: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš „AI parťák programátor“ – převádí textové podněty do dokončení kódu a je integrovaný do vašeho vývojového prostředí (např. Visual Studio Code) pro hladký uživatelský zážitek. Jak je zdokumentováno v sérii níže uvedených blogů, nejranější verze byla založena na modelu OpenAI Codex – inženýři však brzy pochopili potřebu doladit model a vyvinout lepší techniky prompt engineeringu, aby zlepšili kvalitu kódu. V červenci představili [vylepšený AI model, který jde dále než Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pro ještě rychlejší návrhy.

Čtěte příspěvky v pořadí, abyste sledovali jejich učební cestu.

- **Květen 2023** | [GitHub Copilot se zlepšuje v porozumění vašemu kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Květen 2023** | [Uvnitř GitHubu: Práce s LLM za GitHub Copilotem](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Červen 2023** | [Jak psát lepší prompty pro GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Červenec 2023** | [.. GitHub Copilot jde za Codex s vylepšeným AI modelem](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Červenec 2023** | [Průvodce vývojáře prompt engineeringem a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Září 2023** | [Jak postavit enterprise LLM aplikaci: Lekce z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Můžete také procházet jejich [inženýrský blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pro další příspěvky jako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), který ukazuje, jak jsou tyto modely a techniky _aplikovány_ pro pohánění reálných aplikací.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Konstrukce promptu

Viděli jsme, proč je prompt engineering důležitý – teď si pojďme vysvětlit, jak jsou prompty _konstruovány_, abychom mohli vyhodnotit různé techniky pro efektivnější návrh promptů.

### Základní prompt

Začněme se základním promptem: textovým vstupem zaslaným do modelu bez dalšího kontextu. Zde je příklad – když pošleme prvních pár slov americké národní hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžitě _doplní_ odpověď několika dalšími řádky, což ilustruje základní predikční chování.

| Prompt (vstup)        | Dokončení (výstup)                                                                                                      |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see    | Zdá se, že začínáte text písně „The Star-Spangled Banner“, národní hymny Spojených států. Celý text je ...               |

### Složitý prompt

Nyní přidejme kontext a instrukce k tomu základnímu promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje sestavit složitý prompt jako kolekci _zpráv_ s:

- páry vstup/výstup odrážejícími _uživatelský_ vstup a _asistentovu_ odpověď.
- systémovou zprávou nastavující kontext chování nebo osobnosti asistenta.

Žádost nyní vypadá následovně, přičemž _tokenizace_ efektivně zachycuje relevantní informace z kontextu a konverzace. Změna systémového kontextu může mít stejně významný dopad na kvalitu dokončení jako samotné uživatelské vstupy.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukční prompt

V předchozích příkladech byl uživatelský prompt jednoduchý textový dotaz, který lze interpretovat jako žádost o informace. U _instrukčních_ promptů můžeme pomocí textu specifikovat úlohu podrobněji a poskytnout lepší návod AI. Zde je příklad:

| Prompt (vstup)                                                                                                                                                                | Dokončení (výstup)                                                                                                    | Typ instrukce      |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Napiš popis občanské války                                                                                                                                                    | _vrátil jednoduchý odstavec_                                                                                          | Jednoduchý         |
| Napiš popis občanské války. Uveď klíčová data a události a popiš jejich význam                                                                                                | _vrátil odstavec následovaný seznamem klíčových dat událostí s popisy_                                                | Složitý            |
| Napiš popis občanské války v 1 odstavci. Uveď 3 odrážky s klíčovými daty a jejich významem. Uveď 3 další odrážky s hlavními historickými osobnostmi a jejich přínosy. Výstup vrátíš jako JSON soubor | _vrací podrobnější údaje v textovém poli, formátované jako JSON, které lze zkopírovat a uložit do souboru a případně validovat_ | Složitý. Formátovaný.|

## Primární obsah

V předchozích příkladech byl prompt stále poměrně otevřený, což umožňovalo LLM vybrat relevantní část svého předtrénovaného datasetu. U vzoru _primárního obsahu_ je vstupní text rozdělen na dvě části:

- instrukci (akci)
- relevantní obsah (který ovlivňuje akci)

Zde je příklad, kde instrukce zní „shrň toto ve 2 větách“.

| Prompt (vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Dokončení (výstup)                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obřík s hmotností tisíckrát menší než Slunce, ale dvě a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a byl znám starověkým civilizacím již před zaznamenanou historií. Je pojmenován po římském bohu Jupiterovi.[19] Při pohledu ze Země může být Jupiter dostatečně jasný, že jeho odražené světlo vrhá viditelné stíny,[20] a je v průměru třetím nejjasnějším přírodním objektem na noční obloze po Měsíci a Venuši. <br/> **Shrň toto ve 2 krátkých větách** | Jupiter, pátá planeta od Slunce, je největší v Sluneční soustavě a je známý jako jeden z nejjasnějších objektů na noční obloze. Pojmenován po římském bohu Jupiterovi, je to plynný obřík, jehož hmotnost je dvě a půlkrát větší než všech ostatních planet Sluneční soustavy dohromady. |

Segment primárního obsahu lze využít různými způsoby k efektivnějším instrukcím:

- **Příklady** – místo explicitního zadání modelu pomocí instrukce mu dejte příklady, co dělat, a nechte ho odvodit vzor.
- **Nápovědy** – za instrukcí následuje „nápověda“, která připraví dokončení a nasměruje model k relevantnějším odpovědím.
- **Šablony** – to jsou opakovatelné „recepty“ na prompty s místy pro vložení hodnot (proměnné), které lze přizpůsobit daty pro konkrétní použití.

Pojďme si to ukázat v praxi.

### Použití příkladů

Toto je přístup, kdy využíváte primární obsah k „nakrmení modelu“ příklady požadovaného výstupu pro danou instrukci a necháte ho odvodit vzor požadovaného výstupu. Podle počtu uvedených příkladů rozlišujeme zero-shot prompting, one-shot prompting, few-shot prompting atd.

Prompt nyní obsahuje tři komponenty:

- Popis úkolu
- Několik příkladů požadovaného výstupu
- Začátek nového příkladu (který se stává implicitním popisem úkolu)

| Typ učení   | Prompt (vstup)                                                                 |

| Výstup dokončení                   |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Přelož do španělštiny                                                                                                          | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Všimněte si, že u zero-shot promptingu bylo třeba explicitně zadat instrukci („Přelož do španělštiny“), zatímco u one-shot promptingu se instrukce vyvozuje z příkladu. Few-shot příklad ukazuje, jak přidání více příkladů umožňuje modelům přesnější odvození bez nutnosti dalších instrukcí.

### Nápovědy k promptu

Další technikou pro využití primárního obsahu je poskytovat _nápovědy_ místo příkladů. V tomto případě model navedeme správným směrem tím, že _začneme_ kusem textu, který odráží požadovaný formát odpovědi. Model pak „vezme nápovědu“ a pokračuje ve stejném stylu.

| Počet nápověd | Prompt (vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončení (výstup)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obřík s hmotností tisíckrát menší než Slunce, ale dvě a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a byl znám starověkým civilizacím již před zaznamenanou historií. <br/>**Shrň toto**                                       | Jupiter je největší planeta v naší Sluneční soustavě a pátá od Slunce. Je to plynný obřík s hmotností 1/1000 Slunce, ale je hmotnější než všechny ostatní planety dohromady. Starověké civilizace o Jupiteru věděly velmi dlouho a je snadno viditelný na noční obloze. |
| 1              | Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu hmotnosti Slunce, ale dvojnásobek a půl hmotnosti všech ostatních planet Sluneční soustavy dohromady. Jupiter je jedním z nejsvětlejších objektů viditelných pouhým okem na noční obloze a je známý starověkým civilizacím již před zaznamenanou historií. <br/>**Shrňte toto** <br/> Co jsme se naučili, je že Jupiter | je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu hmotnosti Slunce, ale dvojnásobek a půl hmotnosti všech ostatních planet dohromady. Je snadno viditelný pouhým okem a je známý od starověku.                        |
| 2              | Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu hmotnosti Slunce, ale dvojnásobek a půl hmotnosti všech ostatních planet Sluneční soustavy dohromady. Jupiter je jedním z nejsvětlejších objektů viditelných pouhým okem na noční obloze a je známý starověkým civilizacím již před zaznamenanou historií. <br/>**Shrňte toto** <br/> Tři nejdůležitější fakta, která jsme se naučili:         | 1. Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. <br/> 2. Je to plynný obr s hmotností tisícinu hmotnosti Slunce...<br/> 3. Jupiter je viditelný pouhým okem již od starověku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablony promptů

Šablona promptu je _předdefinovaný recept na prompt_, který může být uložen a znovu použit podle potřeby k dosažení konzistentnějších uživatelských zkušeností v měřítku. V jeho nejjednodušší podobě je to jednoduše kolekce příkladů promptů jako [tento od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), která poskytuje jak interaktivní komponenty promptu (zprávy uživatele a systému), tak formát požadavku řízený API – pro podporu opakovaného použití.

V jeho složitější podobě jako [tento příklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) obsahuje _zástupné symboly_, které mohou být nahrazeny daty z různých zdrojů (uživatelský vstup, systémový kontext, externí datové zdroje apod.) k dynamickému generování promptu. To nám umožňuje vytvořit knihovnu opakovaně použitelných promptů, které lze použít k řízení konzistentních uživatelských zkušeností **programově** ve velkém měřítku.

Konečně skutečná hodnota šablon spočívá ve schopnosti vytvářet a publikovat _knihovny promptů_ pro vertikální aplikační domény – kde je šablona promptu nyní _optimalizována_ tak, aby reflektovala specifický kontext aplikace nebo příklady, které činí odpovědi relevantnějšími a přesnějšími pro cílové uživatele. Repozitář [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, který shromažďuje knihovnu promptů pro oblast vzdělávání se zaměřením na klíčové cíle jako plánování lekcí, návrh učebních osnov, doučování studentů atd.

## Podpůrný obsah

Když přemýšlíme o konstrukci promtu jako o instrukci (úkolu) a cíli (primárním obsahu), pak _sekundární obsah_ je jako dodatečný kontext, který poskytujeme k **ovlivnění výstupu nějakým způsobem**. Může to být ladicí parametry, instrukce k formátování, tematické taxonomie atd., které mohou pomoci modelu _přizpůsobit_ svou odpověď tak, aby vyhovovala požadovaným uživatelským cílům nebo očekáváním.

Například: Máme katalog kurzů s rozsáhlými metadaty (název, popis, úroveň, štítky metadat, instruktor apod.) o všech dostupných kurzech v učebním plánu:

- můžeme definovat instrukci „shrni katalog kurzů pro podzim 2023“
- můžeme použít primární obsah k uvedení několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci top 5 „štítků“ zájmu.

Model pak může podat shrnutí ve formátu, jaký ukazují tyto příklady – ale pokud výsledek obsahuje více štítků, může upřednostnit 5 identifikovaných ve sekundárním obsahu.

---

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrýt základní pojem č. 1.
Podpořte pochopení příklady a odkazy.

POJEM Č. 3:
Techniky inženýrství promptů.
Jaké jsou základní techniky inženýrství promptů?
Ilustrujte cvičeními.
-->

## Nejlepší postupy v promptování

Nyní, když víme, jak lze prompty _konstrukčně_ vytvořit, můžeme začít přemýšlet o tom, jak je _navrhnout_ tak, aby odrážely nejlepší postupy. Můžeme o tom uvažovat ve dvou částech – mít správný _přístup_ a aplikovat správné _techniky_.

### Přístup k inženýrství promptů

Inženýrství promptů je proces pokus-omyl, proto mějte na paměti tři obecné vodící faktory:

1. **Porozumění doméně má význam.** Přesnost a relevance odpovědi závisí na _doméně_, ve které daná aplikace nebo uživatel pracuje. Aplikujte svou intuici a odborné znalosti v doméně k **další úpravě technik**. Například definujte _specifické osobnosti domény_ ve vašich systémových promptech, nebo použijte _šablony specifické pro doménu_ ve vašich uživatelských promptech. Poskytněte sekundární obsah odrážející doménově specifické kontexty, nebo použijte _doménově specifické vodítka a příklady_, které povedou model k známým vzorcům použití.

2. **Porozumění modelu má význam.** Víme, že modely jsou svým charakterem stochastické. Ale implementace modelů se také mohou lišit, pokud jde o tréninková data (předtrénované znalosti), schopnosti (např. přes API nebo SDK) a typ obsahu, pro který jsou optimalizovány (např. kód vs. obrázky vs. text). Pochopte silné a slabé stránky modelu, který používáte, a využijte této znalosti k _prioritizaci úkolů_ nebo k vytvoření _přizpůsobených šablon_ optimalizovaných pro schopnosti modelu.

3. **Iterace a validace mají význam.** Modely se rychle vyvíjejí, stejně jako techniky pro inženýrství promptů. Jako odborník v oblasti můžete mít další kontext nebo kritéria pro _vaši_ konkrétní aplikaci, která nemusí platit pro širší komunitu. Používejte nástroje a techniky inženýrství promptů k „rychlému rozběhu“ konstrukce promptů, pak iterujte a validujte výsledky podle vlastní intuice a odbornosti. Zaznamenávejte své poznatky a vytvářejte **základnu znalostí** (např. knihovny promptů), kterou mohou použít i ostatní jako novou výchozí úroveň pro rychlejší iterace v budoucnu.

## Nejlepší praktiky

Podívejme se nyní na běžné nejlepší postupy doporučené odborníky z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                              | Proč                                                                                                                                                                                                                                               |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyzkoušejte nejnovější modely.  | Nové generace modelů pravděpodobně nabízejí vylepšené funkce a kvalitu – ale mohou také znamenat vyšší náklady. Otestujte je pro dopad, pak rozhodujte o migraci.                                                                                   |
| Oddělte instrukce a kontext     | Zjistěte, zda váš model/poskytovatel definuje _oddělovače_ pro jasnější rozlišení instrukcí, primárního a sekundárního obsahu. To může modelům pomoci přesněji vážit tokeny.                                                                        |
| Buďte specifičtí a jasní         | Poskytněte více detailů o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší kvalitu i konzistenci odpovědí. Zachyťte recepty do opakovaně použitelných šablon.                                                                   |
| Buďte popisní, používejte příklady | Modely mohou lépe reagovat na přístup „ukaž a pověz“. Začněte s přístupem `zero-shot`, kdy dáte instrukci (ale bez příkladů), pak zkuste `few-shot` jako zpřesnění s několika příklady požadovaného výstupu. Používejte analogie.                         |
| Používejte vodítka pro zahájení completions | Navádějte model k požadovanému výsledku tím, že mu dáte několik úvodních slov nebo frází, které může použít jako výchozí bod pro odpověď.                                                                                             |
| Zdvojnásobte úsilí               | Někdy je nutné model opakovat. Dejte instrukce před a po primárním obsahu, použijte instrukci a vodítko atd. Iterujte a ověřujte, co funguje.                                                                                                       |
| Pořadí má význam                 | Pořadí, ve kterém předkládáte informace modelu, může ovlivnit výstup, i v učebních příkladech, díky efektu „novosti“. Vyzkoušejte různé možnosti a zjistěte, co funguje nejlépe.                                                                     |
| Dejte modelu „východisko“        | Dejte modelu záložní odpověď, kterou může použít, pokud z nějakého důvodu úkol nezvládne dokončit. To může snížit riziko, že model vytvoří falešné nebo vymyšlené odpovědi.                                                                       |
|                                |                                                                                                                                                                                                                                                   |

Jako u jakékoli nejlepší praxe mějte na paměti, že _váš dojezd se může lišit_ v závislosti na modelu, úkolu a doméně. Použijte tyto rady jako výchozí bod a iterujte, dokud nenajdete to nejlepší pro vás. Pravidelně přehodnocujte svůj proces inženýrství promptů s nástupem nových modelů a nástrojů, se zaměřením na škálovatelnost procesu a kvalitu odpovědí.

<!--
ŠABLONA LEKCE:
Tato jednotka by měla poskytnout programovací výzvu, pokud to platí.

VÝZVA:
Odkaz na Jupyter Notebook, který obsahuje pouze komentáře kódu v instrukcích (sekce kódu jsou prázdné).

ŘEŠENÍ:
Odkaz na kopii toho Notebooku s vyplněnými promptami a spuštěnou ukázkou jednoho příkladu.
-->

## Zadání

Gratulujeme! Došli jste na konec lekce! Je čas otestovat některé z těchto pojmů a technik na reálných příkladech!

Pro náš úkol budeme používat Jupyter Notebook s cvičeními, která můžete interaktivně dokončit. Můžete také rozšířit Notebook o vlastní Markdown a kódové buňky a objevovat nápady a techniky sami.

### Pro začátek forkni repo, pak

- (Doporučeno) Spusťte GitHub Codespaces
- (Alternativně) Klonujte repo na svůj lokální počítač a používejte s Docker Desktop
- (Alternativně) Otevřete Notebook ve vašem preferovaném prostředí pro Notebooky.

### Dále nastavte své environmentální proměnné

- Zkopírujte soubor `.env.copy` v kořenovém adresáři repa do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Vraťte se do [sekce Learning Sandbox](#výukový-sandbox) pro návod.

### Dále otevřete Jupyter Notebook

- Vyberte kernel runtime. Pokud používáte první nebo druhou možnost, jednoduše vyberte výchozí Python 3.10.x kernel poskytovaný dev kontejnerem.

Jste připraveni spustit cvičení. Všimněte si, že zde nejsou žádné _správné a nesprávné_ odpovědi – jde o objevování možností pomocí pokus-omyl a budování intuice, co funguje pro daný model a aplikační doménu.

_Právě z toho důvodu neobsahuje tato lekce segmenty s řešením kódu. Místo toho bude Notebook obsahovat Markdown buňky nazvané „Moje řešení:“, které ukážou jeden příklad výstupu pro referenci._

 <!--
ŠABLONA LEKCE:
Zabalte sekci shrnutím a zdroji pro samostatné učení.
-->

## Kontrola znalostí

Který z následujících promptů je dobrý podle rozumných nejlepších praktik?

1. Ukáž mi obrázek červeného auta
2. Ukáž mi obrázek červeného auta značky Volvo a modelu XC90 zaparkovaného u útesu při západu slunce
3. Ukáž mi obrázek červeného auta značky Volvo a modelu XC90

Odpověď: 2, je to nejlepší prompt, protože poskytuje detaily o „čem“ a jde do podrobností (nejen jakékoli auto, ale specifická značka a model) a dále popisuje celkové okolí. 3 je druhý nejlepší, protože také obsahuje hodně popisu.

## 🚀 Výzva

Vyzkoušejte, jestli můžete využít techniku „vodítka“ s promptem: Dokonči větu „Ukáž mi obrázek červeného auta značky Volvo a “. Co odpoví a jak byste to zlepšili?

## Skvělá práce! Pokračujte ve svém učení

Chcete-li se dozvědět více o různých konceptech inženýrství promptů, přejděte na [pokračující stránku učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde najdete další skvělé zdroje k tomuto tématu.

Přesuňte se do Lekce 5, kde se podíváme na [pokročilé techniky promptování](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->