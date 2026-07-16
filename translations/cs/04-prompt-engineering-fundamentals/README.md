# Základy návrhu promptů

[![Základy návrhu promptů](../../../translated_images/cs/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrývá základní koncepty a techniky pro vytváření efektivních promptů v generativních AI modelech. Na způsob, jakým napíšete svůj prompt pro LLM, také záleží. Pečlivě vytvořený prompt může dosáhnout lepší kvality odpovědi. Ale co přesně znamenají pojmy jako _prompt_ a _navrhování promptů_? A jak mohu zlepšit vstupní _prompt_, který posílám do LLM? Na tyto otázky se pokusíme odpovědět v této kapitole a následující.

_Generativní AI_ je schopná vytvářet nový obsah (např. text, obrázky, zvuk, kód atd.) na základě uživatelských požadavků. Toho dosahuje pomocí _Velkých jazykových modelů_ jako je série GPT od OpenAI („Generative Pre-trained Transformer“), které jsou trénovány pro práci s přirozeným jazykem a kódem.

Uživatelé nyní mohou s těmito modely komunikovat pomocí známých paradigmů, například chatu, bez nutnosti technických znalostí či školení. Modely jsou založeny na _promptech_ – uživatelé posílají textový vstup (prompt) a získávají zpět odpověď AI (completion). Mohou pak s AI iterativně „chatovat“ ve vícestupňových konverzacích, vylepšovat své prompt až do chvíle, kdy odpověď odpovídá jejich očekáváním.

„Prompty“ se tak stávají primárním _programovacím rozhraním_ pro generativní AI aplikace, říkají modelům, co mají dělat, a ovlivňují kvalitu vrácených odpovědí. „Návrh promptů“ je rychle rostoucí oblast studia, která se zaměřuje na _navrhování a optimalizaci_ promptů za účelem dodání konzistentních a kvalitních odpovědí ve velkém rozsahu.

## Cíle učení

V této lekci se naučíme, co je návrh promptů, proč je důležitý a jak můžeme vytvořit efektivnější prompty pro daný model a cílový účel aplikace. Pochopíme základní koncepty a osvědčené postupy pro návrh promptů – a naučíme se o interaktivním "sandbox" prostředí Jupyter Notebooků, kde uvidíme tyto koncepty aplikované na reálných příkladech.

Na konci této lekce budeme schopni:

1. Vysvětlit, co je návrh promptů a proč je důležitý.
2. Popsat komponenty promptu a jejich použití.
3. Naučit se osvědčené postupy a techniky návrhu promptů.
4. Aplikovat naučené techniky na reálných příkladech pomocí OpenAI endpointu.

## Klíčové pojmy

Návrh promptů: Praxe navrhování a zdokonalování vstupů, které vedou AI modely k produkci požadovaných výstupů.
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model dokáže pochopit a zpracovat.
Instruction-Tuned LLMs: Velké jazykové modely (LLM), které byly doladěny pomocí specifických instrukcí pro zlepšení přesnosti a relevance odpovědí.

## Sandbox pro učení

Návrh promptů je zatím více umění než věda. Nejlepší způsob, jak si k němu vytvořit intuici, je _více procvičovat_ a přijmout přístup pokusu a omylu, který kombinuje odbornost v dané oblasti s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook k této lekci poskytuje _sandbox_ prostředí, kde můžete vyzkoušet to, co se naučíte – průběžně nebo jako součást kódového cvičení na konci. Pro spuštění cvičení budete potřebovat:

1. **Azure OpenAI API klíč** – služební endpoint pro nasazený LLM.
2. **Python Runtime** – ve kterém lze notebook spustit.
3. **Lokální proměnné prostředí** – _dokončete nyní kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) pro přípravu_.

Notebook obsahuje _startovací_ cvičení – ale doporučujeme přidávat své vlastní sekce _Markdown_ (popis) a _Code_ (požadavky promptu), abyste mohli vyzkoušet další příklady či nápady a rozvíjet intuici pro navrhování promptů.

## Ilustrovaný průvodce

Chcete získat celkový přehled o tom, co tato lekce pokrývá, než se do ní pustíte? Podívejte se na tento ilustrovaný průvodce, který vám přiblíží hlavní témata a klíčové poznatky, o kterých budete přemýšlet v každé části. Plán lekce vás provede od pochopení základních konceptů a výzev až po jejich řešení pomocí relevantních technik a osvědčených postupů návrhu promptů. Sekce „Pokročilé techniky“ v tomto průvodci odkazuje na obsah pokrytý v _následující_ kapitole tohoto kurzu.

![Ilustrovaný průvodce návrhem promptů](../../../translated_images/cs/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naše startupová mise

Nyní si povíme, jak se _toto téma_ vztahuje k naší mise startupu [přinést AI inovaci do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vyvíjet AI-poháněné aplikace zaměřené na _personalizované učení_ – přemýšlejme tedy o tom, jak by různí uživatelé naší aplikace mohli „navrhovat“ prompty:

- **Administrátoři** by mohli požádat AI o _analýzu dat učebních plánů pro identifikaci mezer v obsahu_. AI může výsledky shrnout nebo je vizualizovat pomocí kódu.
- **Vyučující** by mohli požádat AI o _vytvoření plánu lekce pro cílové publikum a téma_. AI může sestavit personalizovaný plán ve specifikovaném formátu.
- **Studenti** by mohli požádat AI, aby je _doučovala obtížným předmětem_. AI může nyní studenty vést lekcemi, nápovědou a příklady přizpůsobenými jejich úrovni.

To je jen vrchol ledovce. Podívejte se na [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – otevřenou knihovnu promptů sestavenou odborníky na vzdělávání – abyste získali širší představu o možnostech! _Vyzkoušejte spustit některé z těchto promptů v sandboxu nebo na OpenAI Playground a uvidíte, co se stane!_

<!--
ŠABLONA LEKCE:
Tento modul by měl pokrýt základní koncept #1.
Posílit koncept příklady a odkazy.

KONCEPT #1:
Návrh promptů.
Definujte a vysvětlete, proč je potřeba.
-->

## Co je to návrh promptů?

Lekci jsme zahájili definicí **Návrhu promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů) za účelem doručení konzistentních a kvalitních odpovědí (completionů) pro daný účel aplikace a model. Můžeme si to představit jako dvoufázový proces:

- _navrhnout_ počáteční prompt pro daný model a cíl
- _zdokonalovat_ prompt iterativně pro zlepšení kvality odpovědi

Je to nezbytně proces pokusu a omylu, který vyžaduje uživatelskou intuici a úsilí pro dosažení optimálních výsledků. Proč je tedy důležitý? Abychom na tuto otázku odpověděli, musíme nejdříve pochopit tři koncepty:

- _Tokenizace_ = jak model „vidí“ prompt
- _Základní LLM_ = jak základní model „zpracovává“ prompt
- _Instruction-Tuned LLM_ = jak model nyní může vidět „úkoly“

### Tokenizace

LLM vidí prompty jako _sekvenci tokenů_, přičemž různé modely (nebo verze modelu) mohou stejný prompt tokenizovat různými způsoby. Protože LLM jsou trénovány na toky tokenů (a ne na surový text), způsob, jakým se prompty tokenizují, má přímý dopad na kvalitu vygenerované odpovědi.

Pro intuici, jak funguje tokenizace, vyzkoušejte nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) uvedený níže. Zkopírujte svůj prompt a sledujte, jak je převeden na tokeny, věnujte pozornost tomu, jak jsou zpracovány mezery a interpunkční znaménka. Poznámka: tento příklad ukazuje starší LLM (GPT-3), proto může vyzkoušení s novějším modelem přinést odlišný výsledek.

![Tokenizace](../../../translated_images/cs/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Základní modely

Jakmile je prompt tokenizován, primární funkcí ["Základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (neboli Základního modelu) je předpovídat token v dané sekvenci. Protože LLM jsou trénovány na rozsáhlých textových datasetů, mají dobrý přehled o statistických vztazích mezi tokeny a mohou s určitou jistotou předpovídat další token. Neporozumí však _významu_ slov v promptu nebo tokenu; vidí pouze vzor, který mohou „dokončit“ dalším odhadem. Mohou pokračovat v předpovídání posloupnosti, dokud je uživatel nepřeruší nebo dokud není splněna nějaká předem stanovená podmínka.

Chcete vidět, jak funguje doplňování založené na promptu? Zadejte výše uvedený prompt do [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) s výchozím nastavením. Systém je nastaven tak, aby považoval prompty za žádosti o informace – takže byste měli vidět doplnění, které odpovídá tomuto kontextu.

Co když ale uživatel chce vidět něco konkrétního, co splňuje určitá kritéria nebo cíl úkolu? Tady přicházejí do hry _instruction-tuned_ LLM.

![Doplňování chatu základního LLM](../../../translated_images/cs/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction Tuned LLM

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začíná se základním modelem a doladí ho na základě příkladů nebo vstupně-výstupních párů (např. vícestupňových „zpráv“), které obsahují jasné instrukce – a odpověď AI se snaží těmto instrukcím vyhovět.

Používá techniky jako Posilované učení s lidskou zpětnou vazbou (RLHF), které mohou model naučit _řídit se instrukcemi_ a _učit se ze zpětné vazby_, aby produkoval odpovědi lépe přizpůsobené praktickým aplikacím a uživatelským cílům.

Zkuste to – vraťte se k výše uvedenému promptu, ale nyní změňte _systémovou zprávu_ tak, aby poskytla následující instrukci jako kontext:

> _Shrňte poskytnutý obsah pro žáka druhé třídy. Výsledek udržte v jednom odstavci s 3-5 odrážkami._

Vidíte, jak je výsledek nyní laděn tak, aby odrážel požadovaný cíl a formát? Vyučující může tuto odpověď přímo použít ve svých prezentacích pro danou třídu.

![Doplňování chatu instruction-tuned LLM](../../../translated_images/cs/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Proč potřebujeme návrh promptů?

Nyní, když víme, jak LLM zpracovávají prompty, pojďme si říct, _proč_ je třeba návrh promptů. Odpověď spočívá v tom, že současné LLM představují řadu výzev, které ztěžují dosažení _spolehlivých a konzistentních odpovědí_ bez úsilí věnovaného konstrukci a optimalizaci promptu. Například:

1. **Odpovědi modelu jsou náhodné.** _Stejný prompt_ pravděpodobně poskytne odlišné odpovědi u různých modelů nebo verzí modelů. A může produkovat i různé výsledky u _tohoto samého modelu_ v různých časech. _Techniky návrhu promptů nám pomáhají tyto rozdíly minimalizovat tím, že poskytnou lepší vodítka_.

1. **Modely mohou smyšlet odpovědi.** Modely jsou předtrénované na _velkých, ale konečných_ datech, což znamená, že nemají znalosti o pojmech mimo tento rozsah tréninku. Výsledkem mohou být odpovědi, které jsou nepřesné, smyšlené nebo přímo v rozporu s ověřenými fakty. _Techniky návrhu promptů uživatelům pomáhají tyto smyšlenky identifikovat a omezit, např. požadováním citací nebo zdůvodnění od AI_.

1. **Schopnosti modelů se liší.** Novější modely nebo generace modelů mají bohatší schopnosti, ale také přinášejí specifické zvláštnosti a kompromisy v nákladech a složitosti. _Návrh promptů nám může pomoci vyvinout osvědčené postupy a pracovní postupy, které abstrahují rozdíly a přizpůsobují se požadavkům konkrétního modelu škálovatelným a hladkým způsobem_.

Pojďme si to vyzkoušet v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) – viděli jste odlišnosti?
- Použijte stejný prompt opakovaně s _tím samým_ nasazením LLM (např. Azure OpenAI playground) – jak se tyto variace lišily?

### Příklad smyšlení (fabrications)

V tomto kurzu používáme výraz **„fabrication“** k označení jevu, kdy LLM někdy generují fakticky nesprávné informace kvůli omezením ve svém tréninku nebo jiným podmínkám. Můžete to také znát pod názvem _„halucinace“_ z populárních článků nebo vědeckých prací. Nicméně důrazně doporučujeme používat termín _„fabrication“_, abychom se vyhnuli antropomorfizaci chování a nepřisuzovali strojovému výsledku lidskou vlastnost. Tento přístup také posiluje [zásady odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hlediska terminologie tím, že odstraňuje termíny, které mohou být v některých kontextech považovány za urážlivé nebo výlučné.

Chcete porozumět tomu, jak fungují fabrications? Představte si prompt, který instruuje AI generovat obsah pro neexistující téma (aby bylo zaručeno, že se nenachází v tréninkové sadě). Například – zkusil jsem tento prompt:

> **Prompt:** vytvoř plán lekce o Marťanské válce roku 2076.

Webové vyhledávání mi ukázalo, že existují fiktivní popisy (např. televizní seriály nebo knihy) o marťanských válkách – ale žádné z roku 2076. Zdravý rozum také říká, že rok 2076 je _v budoucnosti_ a tudíž nemůže být spojován se skutečnou událostí.


Co se tedy stane, když tento prompt spustíme u různých poskytovatelů LLM?

> **Odpověď 1**: OpenAI Playground (GPT-35)

![Odpověď 1](../../../translated_images/cs/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpověď 2**: Azure OpenAI Playground (GPT-35)

![Odpověď 2](../../../translated_images/cs/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpověď 3**: : Hugging Face Chat Playground (LLama-2)

![Odpověď 3](../../../translated_images/cs/04-fabrication-huggingchat.faf82a0a51278956.webp)

Jak se dalo očekávat, každý model (nebo verze modelu) produkuje mírně odlišné odpovědi díky stochastickému chování a odlišnostem v kapacitě modelu. Například jeden model cílí na publikum 8. třídy, zatímco druhý předpokládá studenta střední školy. Ale všechny tři modely vygenerovaly odpovědi, které by mohly přesvědčit neinformovaného uživatele, že událost byla skutečná.

Techniky prompt engineeringu jako _metaprompting_ a _nastavení teploty_ mohou do určité míry snížit falešné informace generované modelem. Nové _architektury_ prompt engineeringu také bezproblémově integrují nové nástroje a techniky do toku promptu, aby tyto efekty snížily nebo zmírnily.

## Případová studie: GitHub Copilot

Uzavřeme tuto část získáním představy o tom, jak se prompt engineering používá v reálných řešeních na příkladu jedné případové studie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš "AI pár programátora" - převádí textové prompty na dokončení kódu a je integrován do vašeho vývojového prostředí (např. Visual Studio Code) pro bezproblémový uživatelský zážitek. Jak je zdokumentováno v sérii blogů níže, nejstarší verze byla založena na modelu OpenAI Codex - přičemž inženýři rychle pochopili potřebu doladit model a vyvinout lepší techniky prompt engineeringu, aby zlepšili kvalitu kódu. V červenci představili [vylepšený AI model, který jde nad rámec Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pro ještě rychlejší návrhy.

Čtěte příspěvky v pořadí, abyste sledovali jejich učební cestu.

- **Květen 2023** | [GitHub Copilot se stále lépe učí rozumět vašemu kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Květen 2023** | [Uvnitř GitHubu: Práce s LLM za GitHub Copilotem](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Červen 2023** | [Jak napsat lepší prompty pro GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Červenec 2023** | [.. GitHub Copilot jde nad rámec Codex s vylepšeným AI modelem](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Červenec 2023** | [Průvodce vývojáře prompt engineeringem a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Září 2023** | [Jak postavit enterprise LLM aplikaci: Lekce z GitHub Copilota](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Můžete také procházet jejich [enginneering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pro více příspěvků jako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), který ukazuje, jak jsou tyto modely a techniky _aplikovány_ pro řízení reálných aplikací.

---

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrýt základní koncept č. 2.
Posílit koncept na příkladech a referencích.

KONCEPT č. 2:
Návrh promptu.
Ilustrováno na příkladech.
-->

## Konstrukce promptu

Viděli jsme, proč je prompt engineering důležitý - nyní porozumíme tomu, jak se prompty _konstruují_, abychom mohli vyhodnotit různé techniky pro efektivnější návrh promptu.

### Základní prompt

Začněme se základním promptem: textovým vstupem poslaným modelu bez jiného kontextu. Zde je příklad - když pošleme první několik slov americké národní hymny OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžitě _dokončí_ odpověď dalšími několika řádky, čímž ilustruje základní predikční chování.

| Prompt (Vstup)        | Dokončení (Výstup)                                                                                                                       |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see    | Zdá se, že začínáte text "The Star-Spangled Banner," národní hymnu Spojených států. Celý text je ...                                      |

### Komplexní prompt

Nyní přidejme kontext a instrukce k tomu základnímu promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje konstruovat komplexní prompt jako kolekci _zpráv_ s:

- Páry vstup/výstup odrážející _uživatelský_ vstup a _asistentovu_ odpověď.
- Systémovou zprávou nastavující kontext chování nebo osobnosti asistenta.

Žádost má nyní níže uvedenou formu, kde _tokenizace_ efektivně zachycuje relevantní informace z kontextu a konverzace. Změna systémového kontextu může mít stejně významný dopad na kvalitu dokončení jako poskytnuté uživatelské vstupy.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukční prompt

V předchozích příkladech uživatelský prompt byl jednoduchý textový dotaz, který lze interpretovat jako žádost o informaci. U _instrukčních_ promptů můžeme použít tento text k podrobnějšímu specifikování úkolu a poskytnout AI jasnější směr. Zde je příklad:

| Prompt (Vstup)                                                                                                                                                                                                                          | Dokončení (Výstup)                                                                                                       | Typ instrukce      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------ | :----------------- |
| Napiš popis občanské války                                                                                                                                                                                                              | _vrátil jednoduchý odstavec_                                                                                             | Jednoduchý         |
| Napiš popis občanské války. Uveď klíčová data a události a popiš jejich význam                                                                                                                                                         | _vrátil odstavec následovaný seznamem klíčových dat událostí s popisy_                                                  | Komplexní          |
| Napiš popis občanské války v 1 odstavci. Uveď 3 odrážky s klíčovými daty a jejich významem. Uveď 3 další odrážky s klíčovými historickými postavami a jejich přínosy. Výstup vrať jako JSON soubor                                     | _vrací rozsáhlejší detail v textovém bloku, formátovaný jako JSON, který můžete zkopírovat a uložit do souboru a případně ověřit_ | Komplexní. Formátovaný. |

## Primární obsah

Ve výše uvedených příkladech byl prompt stále poměrně otevřený, což umožňovalo LLM rozhodnout se, která část jeho předtrénovaného datasetu je relevantní. S návrhovým vzorem _primární obsah_ je vstupní text rozdělen do dvou částí:

- instrukce (akce)
- relevantní obsah (který ovlivňuje akci)

Zde je příklad, kde je instrukce „shrň to ve 2 větách“.

| Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Dokončení (Výstup)                                                                                                                                                                                                                                                               |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je pátou planetou od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu Slunce, ale dvakrát a půl vyšší než všech ostatních planet v Sluneční soustavě dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a známý byl starověkým civilizacím před zaznamenanou historií. Je pojmenován po římském bohu Jupiterovi.[19] Když je pozorován ze Země, může být Jupiter dostatečně jasný, aby jeho odražené světlo vrhalo viditelné stíny,[20] a je průměrně třetím nejjasnějším přírodním objektem na noční obloze po Měsíci a Venuši. <br/> **Shrň to ve 2 krátkých větách** | Jupiter, pátá planeta od Slunce, je největší v Sluneční soustavě a je známý jako jeden z nejjasnějších objektů na noční obloze. Pojmenován po římském bohu Jupiterovi, je to plynný obr s hmotností dvakrát a půl vyšší než všech ostatních planet v Sluneční soustavě dohromady. |

Segment primárního obsahu může být použit různými způsoby pro efektivnější instrukce:

- **Příklady** - místo explicitního instrukce modelu, co má dělat, mu dejte příklady a nechte jej odvodit vzor.
- **Pokyny** - následujte instrukci „pokynem“, který napomáhá dokončení a vede model k relevantnějším odpovědím.
- **Šablony** - jsou to opakující se „recepty“ promptů s místy (proměnnými), které lze přizpůsobit daty pro konkrétní případy použití.

Pojďme se na to podívat v praxi.

### Použití příkladů

Toto je přístup, kdy využijete primární obsah k „nakrmení modelu“ několika příklady požadovaného výstupu pro danou instrukci a necháte model odvodit vzor požadovaného výstupu. Na základě počtu poskytnutých příkladů může jít o zero-shot prompting, one-shot prompting, few-shot prompting atd.

Prompt nyní sestává ze tří komponent:

- Popis úkolu
- Několik příkladů požadovaného výstupu
- Začátek nového příkladu (který se stává implicitním popisem úkolu)

| Typ učení  | Prompt (Vstup)                                                                                                                              | Dokončení (Výstup)        |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------ |
| Zero-shot  | "The Sun is Shining". Přelož do španělštiny                                                                                              | "El Sol está brillando".  |
| One-shot   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                     | "Es un día frío y ventoso". |
| Few-shot   | Hráč oběhl mety => Baseball <br/> Hráč zahrál eso => Tenis <br/> Hráč zahrál šestku => Kriket <br/> Hráč dal smeč =>                   | Basketbal                 |
|            |                                                                                                                                            |                           |

Všimněte si, že jsme museli poskytnout explicitní instrukci („Přelož do španělštiny“) v zero-shot promptingu, ale ve one-shot příkladu je již odvozená. Few-shot příklad ukazuje, jak přidáním více příkladů modely mohou činit přesnější závěry bez dalších instrukcí.

### Pokyny (Cues) pro prompt

Další technika použití primárního obsahu je poskytování _pokynů_ místo příkladů. V tomto případě modelu dáme najevo směr _zahájením_ útržku, který odráží požadovaný formát odpovědi. Model pak „vezme pokyn“ a pokračuje v tomto duchu.

| Počet pokynů | Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dokončení (Výstup)                                                                                                                                                                                                                                                                                     |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0            | Jupiter je pátou planetou od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu Slunce, ale dvakrát a půl vyšší než všech ostatních planet v Sluneční soustavě dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a známý byl starověkým civilizacím před zaznamenanou historií. <br/>**Shrň to**                                          | Jupiter je největší planeta naší Sluneční soustavy a pátá od Slunce. Je to plynný obr s hmotností 1/1000 hmotnosti Slunce, ale je těžší než všechny ostatní planety dohromady. Starověké civilizace o Jupiteru věděly dlouhou dobu, a je snadno viditelný na noční obloze. |
| 1            | Jupiter je pátou planetou od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu Slunce, ale dvakrát a půl vyšší než všech ostatních planet v Sluneční soustavě dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a známý byl starověkým civilizacím před zaznamenanou historií. <br/>**Shrň to** <br/> Co jsme se dozvěděli je, že Jupiter | je pátou planetou od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností tisícinu Slunce, ale dvakrát a půl vyšší než všech ostatních planet dohromady. Je snadno viditelný pouhým okem a známý je od starověku.                       |

| 2              | Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. Je to plynný obr s hmotností jedna tisícina hmotnosti Slunce, ale dvě a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je známý starověkým civilizacím již před zaznamenáním historie. <br/>**Shrnutí** <br/> Top 3 fakta, která jsme se naučili:         | 1. Jupiter je pátá planeta od Slunce a největší v Sluneční soustavě. <br/> 2. Je to plynný obr s hmotností jedna tisícina hmotnosti Slunce...<br/> 3. Jupiter je viditelný pouhým okem již od starověku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablony promptů

Šablona promptu je _předem definovaný recept na prompt_, který může být uložen a znovu použit podle potřeby pro dosažení konzistentnějších uživatelských zkušeností ve větším měřítku. V nejjednodušší podobě je to jednoduše sbírka příkladů promptů jako [tento od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), která poskytuje jak interaktivní komponenty promptu (zprávy uživatele a systému), tak formát požadavku řízený API - pro podporu opětovného použití.

V komplikovanější podobě jako [tento příklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) obsahuje _zástupné symboly_, které mohou být nahrazeny daty z různých zdrojů (uživatelský vstup, kontext systému, externí zdroje dat atd.) pro dynamické generování promptu. To nám umožňuje vytvořit knihovnu opakovaně použitelných promptů, které lze _programově_ používat pro konzistentní uživatelské zkušenosti ve velkém měřítku.

Skutečná hodnota šablon spočívá v možnosti vytvářet a publikovat _knihovny promptů_ pro vertikální aplikace - kde je šablona promptu _optimalizována_ tak, aby odrážela kontext nebo příklady specifické pro danou aplikaci, které zvyšují relevanci a přesnost odpovědí pro cílové uživatele. Repozitář [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, kurátoruje knihovnu promptů pro vzdělávací oblast s důrazem na klíčové cíle jako plánování lekcí, návrh osnov, doučování studentů atd.

## Podpůrný obsah

Pokud uvažujeme konstrukci promptu jako zadání úkolu (instrukce) a cílového obsahu (primární obsah), pak _sekundární obsah_ je něco jako dodatečný kontext, který poskytujeme k **ovlivnění výstupu určitým způsobem**. Může to být ladící parametry, instrukce formátování, taxonomie témat atd., které mohou pomoci modelu _přizpůsobit_ svou odpověď tak, aby vyhovovala požadovaným uživatelským cílům či očekáváním.

Například: Máme katalog kurzů s rozsáhlými metadaty (název, popis, úroveň, štítky metadat, instruktor atd.) všech dostupných kurzů v osnově:

- můžeme definovat instrukci „shrň katalog kurzů pro podzim 2023“
- můžeme použít primární obsah pro poskytnutí několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci 5 nejdůležitějších „štítků“ zájmu

Nyní může model poskytnout shrnutí ve formátu, který ukazují příklady - ale pokud má výsledek více štítků, může upřednostnit právě těch 5 identifikovaných v sekundárním obsahu.

---

<!--
VZOR LEKCE:
Tato jednotka by měla pokrýt hlavní koncept č. 1.
Posilte koncept příklady a odkazy.

KONCEPT Č. 3:
Techniky návrhu promptu.
Jaké jsou základní techniky návrhu promptu?
Ilustrujte je na cvičeních.
-->

## Nejlepší praktiky promptování

Teď, když víme, jak lze prompty _konstruktivně sestavovat_, můžeme začít přemýšlet o tom, jak je _navrhnout_ tak, aby odrážely nejlepší praktiky. Můžeme o tom přemýšlet ve dvou částech - mít správný _přístup_ a aplikovat správné _techniky_.

### Přístup pro návrh promptů

Návrh promptů je proces metodou pokusu a omylu, takže mějte na paměti tři široké vodítka:

1. **Porozumění doméně je důležité.** Přesnost a relevance odpovědi závisí na _doméně_, ve které aplikace nebo uživatel pracuje. Použijte svou intuici a expertní znalosti domény k **dále přizpůsobení technik**. Například definujte _osobnosti specifické pro doménu_ ve svých systémových promptech, nebo použijte _šablony specifické pro doménu_ ve svých uživatelských promptech. Poskytněte sekundární obsah, který odráží kontext specifický pro doménu, nebo použijte _náznaky a příklady specifické pro doménu_ k vedení modelu k známým vzorcům použití.

2. **Porozumění modelu je důležité.** Víme, že modely jsou ze své podstaty stochastické. Ale implementace modelu se mohou lišit v závislosti na tréninkové sadě dat (předtrénované znalosti), schopnostech, které poskytují (např. přes API nebo SDK) a typu obsahu, pro který jsou optimalizovány (např. kód vs. obrázky vs. text). Pochopte silné a slabé stránky modelu, který používáte, a použijte tyto znalosti k _upřednostnění úkolů_ nebo vytvoření _customizovaných šablon_, které jsou optimalizované podle schopností modelu.

3. **Iterace & validace je důležitá.** Modely se rychle vyvíjejí a stejně tak techniky návrhu promptů. Jako expert v dané oblasti můžete mít další kontext nebo kritéria pro _vaši_ specifickou aplikaci, která nemusí platit pro širší komunitu. Použijte nástroje a techniky návrhu promptů k „rychlému startu“ konstrukce promptu, poté iterujte a validujte výsledky pomocí vlastní intuice a odborných znalostí. Zaznamenávejte své poznatky a vytvářejte **vědomostní bázi** (např. knihovny promptů), kterou mohou ostatní použít jako nový základ pro rychlejší iterace v budoucnu.

## Nejlepší praktiky

Teď se podívejme na běžné nejlepší praktiky doporučované znalci z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                              | Proč                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hodnoťte nejnovější modely.       | Nové generace modelů pravděpodobně obsahují vylepšené funkce a kvalitu - ale zároveň mohou znamenat vyšší náklady. Hodnoťte je z hlediska dopadu a pak se rozhodněte k migraci.                                                                              |
| Oddělte instrukce a kontext   | Zjistěte, zda váš model/providr definuje _oddělovače_, které jasněji rozlišují instrukce, primární a sekundární obsah. To může modelům pomoci přesněji vážit tokeny.                                                        |
| Buďte specifičtí a jasní             | Poskytněte více detailů o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší kvalitu i konzistenci odpovědí. Zaznamenávejte recepty v opakovaně použitelných šablonách.                                                          |
| Buďte popisní, využívejte příklady      | Modely mohou lépe reagovat na přístup „ukázat a říct“. Začněte s `zero-shot` přístupem, kdy dáte instrukci (bez příkladů), poté zkuste `few-shot` jako zpřesnění, poskytující několik příkladů požadovaného výstupu. Použijte analogie. |
| Použijte náznaky k nastartování dokončení | Nasměrujte model k požadovanému výsledku tím, že mu dáte několik úvodních slov nebo frází, které může použít jako výchozí bod pro odpověď.                                                                                                               |
| Opakujte                         | Někdy je potřeba model opakovat. Dej mu instrukce před a po primárním obsahu, použij instrukci a náznak atd. Iterujte a validujte, abyste zjistili, co funguje.                                                                                                                         |
| Pořadí má význam                 | Pořadí, v jakém modelu předkládáte informace, může ovlivnit výstup, dokonce i u učebních příkladů kvůli efektu čerstvosti (recency bias). Vyzkoušejte různé možnosti, abyste zjistili, co funguje nejlépe.                                                               |
| Dopřejte modelu “únik”          | Dejte modelu _záložní_ odpověď, kterou může poskytnout, pokud nemůže úkol z nějakého důvodu dokončit. To může snížit šanci, že model vygeneruje falešné nebo smyšlené odpovědi.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Stejně jako u každé nejlepší praxe mějte na paměti, že _výsledky se mohou lišit_ podle modelu, úkolu a domény. Používejte je jako výchozí bod a iterujte, abyste zjistili, co funguje nejlépe pro vás. Neustále převalujte proces návrhu promptů, jakmile jsou dostupné nové modely a nástroje, se zaměřením na škálovatelnost procesu a kvalitu výstupu.

<!--
VZOR LEKCE:
Tato jednotka by měla poskytnout kódový úkol, pokud je to relevantní

ÚKOL:
Odkaz na Jupyter Notebook, kde jsou instrukce pouze v komentářích kódu (sekce s kódem jsou prázdné).

ŘEŠENÍ:
Odkaz na kopii toho Notebooks se vyplněnými prompty a spuštěnou ukázkou výsledku.
-->

## Zadání úkolu

Gratulujeme! Dostali jste se na konec lekce! Je čas otestovat některé z těchto konceptů a technik na reálných příkladech!

Pro náš úkol budeme používat Jupyter Notebook s cvičeními, která můžete dělat interaktivně. Můžete také rozšířit Notebook o vlastní buňky Markdown a kódu, abyste si průzkum a techniky vyzkoušeli sami.

### Pro začátek forkněte repozitář, poté

- (Doporučeno) Spusťte GitHub Codespaces
- (Alternativně) Klonujte repozitář do svého lokálního zařízení a použijte ho s Docker Desktop
- (Alternativně) Otevřete Notebook ve svém preferovaném prostředí pro Notebooky.

### Dále nastavte své environmentální proměnné

- Zkopírujte soubor `.env.copy` v kořenovém adresáři repozitáře na `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Poté se vraťte do [sekce Learning Sandbox](#sandbox-pro-učení) a naučte se jak na to.

### Dále otevřete Jupyter Notebook

- Vyberte runtime kernel. Pokud používáte možnost 1 nebo 2, jednoduše zvolte výchozí kernel Python 3.10.x poskytovaný vývojovým kontejnerem.

Jste připraveni spustit cvičení. Všimněte si, že zde nejsou žádné _správné a špatné_ odpovědi - jen průzkum možností metodou pokus-omyl a budování intuice, co funguje pro daný model a doménu aplikace.

_Z tohoto důvodu nejsou v této lekci sekce s Kódovým řešením. Místo toho budou v Notebooku buňky Markdown s názvem "Moje řešení:", které ukážou jeden příklad výsledku pro referenci._

 <!--
VZOR LEKCE:
Osaďte sekci shrnutím a zdroji pro samostatné učení.
-->

## Kontrola znalostí

Který z následujících promptů odpovídá rozumným nejlepším praktikám?

1. Ukáž mi obrázek červeného auta
2. Ukáž mi obrázek červeného auta značky Volvo a modelu XC90 zaparkovaného u útesu při západu slunce
3. Ukáž mi obrázek červeného auta značky Volvo a modelu XC90

A: 2 je nejlepší prompt, protože poskytuje detaily o „čem“ a jde do specifik (ne jen jakékoliv auto, ale konkrétní značka a model) a také popisuje celkové prostředí. 3 je druhý nejlepší, protože také obsahuje hodně popisu.

## 🚀 Výzva

Zkuste využít techniku „náznak“ s promptem: Dokonči větu „Ukáž mi obrázek červeného auta značky Volvo a “. Jak na to odpoví a jak byste to zlepšili?

## Skvělá práce! Pokračujte ve svém učení

Chcete se dozvědět více o různých pojmech Prompt Engineering? Přejděte na [stránku s dalším učením](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a najděte další skvělé zdroje na toto téma.

Přejděte do Lekce 5, kde se podíváme na [pokročilé techniky promptování](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->