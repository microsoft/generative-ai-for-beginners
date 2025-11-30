<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-17T21:43:11+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "cs"
}
-->
# Základy návrhu promptů

[![Základy návrhu promptů](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.cs.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul se zabývá základními koncepty a technikami pro vytváření efektivních promptů v generativních AI modelech. Způsob, jakým napíšete svůj prompt pro LLM, má také význam. Pečlivě vytvořený prompt může přinést kvalitnější odpovědi. Ale co přesně znamenají pojmy jako _prompt_ a _návrh promptů_? A jak mohu zlepšit _vstupní prompt_, který posílám LLM? To jsou otázky, na které se pokusíme odpovědět v této kapitole a v následující.

_Generativní AI_ je schopná vytvářet nový obsah (např. text, obrázky, zvuk, kód atd.) na základě požadavků uživatele. Toho dosahuje pomocí _velkých jazykových modelů_ (Large Language Models) jako je série GPT ("Generative Pre-trained Transformer") od OpenAI, které jsou trénovány na přirozeném jazyce a kódu.

Uživatelé nyní mohou s těmito modely komunikovat pomocí známých paradigmat, jako je chat, aniž by potřebovali technické znalosti nebo školení. Modely jsou _založené na prompty_ - uživatelé posílají textový vstup (prompt) a dostávají zpět odpověď od AI (výstup). Poté mohou "chatovat s AI" iterativně, v konverzacích na více úrovních, a upravovat svůj prompt, dokud odpověď neodpovídá jejich očekáváním.

"Prompty" se nyní stávají primárním _programovacím rozhraním_ pro aplikace generativní AI, které modelům říkají, co mají dělat, a ovlivňují kvalitu vrácených odpovědí. "Návrh promptů" je rychle se rozvíjející oblast studia, která se zaměřuje na _návrh a optimalizaci_ promptů, aby poskytovaly konzistentní a kvalitní odpovědi ve velkém měřítku.

## Cíle učení

V této lekci se naučíme, co je návrh promptů, proč je důležitý a jak můžeme vytvářet efektivnější prompty pro daný model a cíle aplikace. Porozumíme základním konceptům a osvědčeným postupům pro návrh promptů - a dozvíme se o interaktivním prostředí "sandbox" v Jupyter Notebooks, kde můžeme tyto koncepty aplikovat na skutečné příklady.

Na konci této lekce budeme schopni:

1. Vysvětlit, co je návrh promptů a proč je důležitý.
2. Popsat komponenty promptu a jak se používají.
3. Naučit se osvědčené postupy a techniky pro návrh promptů.
4. Aplikovat naučené techniky na skutečné příklady pomocí OpenAI endpointu.

## Klíčové pojmy

Návrh promptů: Praxe navrhování a zdokonalování vstupů, které vedou AI modely k produkci požadovaných výstupů.
Tokenizace: Proces převodu textu na menší jednotky, nazývané tokeny, které model dokáže pochopit a zpracovat.
LLM laděné na instrukce: Velké jazykové modely (LLM), které byly doladěny pomocí specifických instrukcí za účelem zlepšení přesnosti a relevance jejich odpovědí.

## Sandbox pro učení

Návrh promptů je v současnosti spíše umění než věda. Nejlepší způsob, jak si v něm zlepšit intuici, je _více cvičit_ a přijmout přístup pokus-omyl, který kombinuje odborné znalosti v dané oblasti aplikace s doporučenými technikami a optimalizacemi specifickými pro model.

Jupyter Notebook, který doprovází tuto lekci, poskytuje prostředí _sandbox_, kde si můžete vyzkoušet, co jste se naučili - buď průběžně, nebo jako součást závěrečné výzvy kódování. K provedení cvičení budete potřebovat:

1. **Klíč API Azure OpenAI** - koncový bod služby pro nasazený LLM.
2. **Python Runtime** - prostředí, ve kterém lze Notebook spustit.
3. **Lokální proměnné prostředí** - _dokončete kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) nyní, abyste byli připraveni_.

Notebook obsahuje _startovací_ cvičení - ale doporučujeme přidat vlastní sekce _Markdown_ (popis) a _Code_ (požadavky na prompt), abyste si mohli vyzkoušet více příkladů nebo nápadů - a rozvíjet svou intuici pro návrh promptů.

## Ilustrovaný průvodce

Chcete získat celkový přehled o tom, co tato lekce pokrývá, než se do ní ponoříte? Podívejte se na tento ilustrovaný průvodce, který vám poskytne přehled hlavních témat a klíčových poznatků, o kterých byste měli přemýšlet v každé z nich. Plán lekce vás provede od pochopení základních konceptů a výzev k jejich řešení pomocí relevantních technik návrhu promptů a osvědčených postupů. Upozorňujeme, že sekce "Pokročilé techniky" v tomto průvodci odkazuje na obsah pokrytý v _další_ kapitole tohoto kurzu.

![Ilustrovaný průvodce návrhem promptů](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.cs.png)

## Naše startupová mise

Nyní si povíme, jak _toto téma_ souvisí s naší startupovou misí [přinést inovace AI do vzdělávání](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvářet aplikace poháněné AI pro _personalizované vzdělávání_ - takže se zamysleme nad tím, jak různí uživatelé naší aplikace mohou "navrhovat" prompty:

- **Administrátoři** mohou požádat AI, aby _analyzovala data z učebních osnov a identifikovala mezery v pokrytí_. AI může výsledky shrnout nebo je vizualizovat pomocí kódu.
- **Učitelé** mohou požádat AI, aby _vytvořila plán lekce pro cílovou skupinu a téma_. AI může vytvořit personalizovaný plán ve specifickém formátu.
- **Studenti** mohou požádat AI, aby je _doučovala v obtížném předmětu_. AI může studenty vést lekcemi, nápovědou a příklady přizpůsobenými jejich úrovni.

To je jen špička ledovce. Podívejte se na [Prompty pro vzdělávání](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otevřenou knihovnu promptů vytvořenou odborníky na vzdělávání - abyste získali širší představu o možnostech! _Vyzkoušejte některé z těchto promptů v sandboxu nebo v OpenAI Playground a podívejte se, co se stane!_

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrývat základní koncept #1.
Posilujte koncept pomocí příkladů a odkazů.

KONCEPT #1:
Návrh promptů.
Definujte ho a vysvětlete, proč je potřeba.
-->

## Co je návrh promptů?

Tuto lekci jsme začali definicí **návrhu promptů** jako procesu _navrhování a optimalizace_ textových vstupů (promptů) za účelem dosažení konzistentních a kvalitních odpovědí (výstupů) pro daný cíl aplikace a model. Můžeme si to představit jako dvoustupňový proces:

- _navrhování_ počátečního promptu pro daný model a cíl
- _zdokonalování_ promptu iterativně za účelem zlepšení kvality odpovědi

Tento proces je nutně založen na pokusech a omylech, které vyžadují intuici uživatele a úsilí k dosažení optimálních výsledků. Proč je tedy důležitý? Abychom na tuto otázku odpověděli, musíme nejprve pochopit tři koncepty:

- _Tokenizace_ = jak model "vidí" prompt
- _Základní LLM_ = jak základní model "zpracovává" prompt
- _LLM laděné na instrukce_ = jak model nyní vidí "úkoly"

### Tokenizace

LLM vidí prompty jako _sekvenci tokenů_, kde různé modely (nebo verze modelu) mohou tokenizovat stejný prompt různými způsoby. Protože LLM jsou trénovány na tokenech (a ne na surovém textu), způsob, jakým jsou prompty tokenizovány, má přímý dopad na kvalitu generované odpovědi.

Chcete-li získat intuici o tom, jak tokenizace funguje, vyzkoušejte nástroje jako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) uvedený níže. Zkopírujte svůj prompt - a podívejte se, jak se převádí na tokeny, věnujte pozornost tomu, jak jsou zpracovávány znaky mezer a interpunkce. Upozorňujeme, že tento příklad ukazuje starší LLM (GPT-3) - takže při použití novějšího modelu může být výsledek odlišný.

![Tokenizace](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.cs.png)

### Koncept: Základní modely

Jakmile je prompt tokenizován, hlavní funkcí ["Základního LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (nebo základního modelu) je předpovědět token v této sekvenci. Protože LLM jsou trénovány na obrovských textových datových sadách, mají dobrý přehled o statistických vztazích mezi tokeny a mohou tuto předpověď provést s určitou jistotou. Upozorňujeme, že nerozumí _významu_ slov v promptu nebo tokenu; vidí pouze vzor, který mohou "dokončit" svou další předpovědí. Mohou pokračovat v předpovídání sekvence, dokud je uživatel nezasáhne nebo dokud nenastane nějaká předem stanovená podmínka.

Chcete vidět, jak funguje dokončování na základě promptů? Zadejte výše uvedený prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) v Azure OpenAI Studio s výchozím nastavením. Systém je nakonfigurován tak, aby prompty považoval za požadavky na informace - takže byste měli vidět výstup, který odpovídá tomuto kontextu.

Ale co když uživatel chtěl vidět něco konkrétního, co splňuje nějaká kritéria nebo cíl úkolu? Zde přicházejí na scénu _LLM laděné na instrukce_.

![Dokončování chatu základního LLM](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.cs.png)

### Koncept: LLM laděné na instrukce

[LLM laděné na instrukce](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začíná základním modelem a doladí ho pomocí příkladů nebo párů vstup/výstup (např. vícenásobné "zprávy"), které mohou obsahovat jasné instrukce - a odpověď od AI se snaží tyto instrukce dodržet.

Používá techniky jako Reinforcement Learning with Human Feedback (RLHF), které mohou model naučit _dodržovat instrukce_ a _učit se z zpětné vazby_, aby produkoval odpovědi, které jsou lépe přizpůsobené praktickým aplikacím a více relevantní pro cíle uživatele.

Vyzkoušejme to - vraťte se k výše uvedenému promptu, ale nyní změňte _systémovou zprávu_, aby poskytla následující instrukci jako kontext:

> _Shrňte obsah, který vám byl poskytnut, pro žáka druhé třídy. Udržte výsledek na jeden odstavec s 3-5 odrážkami._

Vidíte, jak je výsledek nyní přizpůsoben požadovanému cíli a formátu? Učitel může nyní tuto odpověď přímo použít ve svých prezentacích pro danou třídu.

![Dokončování chatu LLM laděného na instrukce](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.cs.png)

## Proč potřebujeme návrh promptů?

Nyní, když víme, jak jsou prompty zpracovávány LLM, pojďme si povědět o _důvodech_, proč potřebujeme návrh promptů. Odpověď spočívá v tom, že současné LLM představují řadu výzev, které činí _spolehlivé a konzistentní výstupy_ obtížnějšími bez úsilí věnovaného konstrukci a optimalizaci promptů. Například:

1. **Odpovědi modelu jsou stochastické.** _Stejný prompt_ pravděpodobně přinese různé odpovědi s různými modely nebo verzemi modelů. A může dokonce přinést různé výsledky se _stejným modelem_ v různých časech. _Techniky návrhu promptů nám mohou pomoci minimalizovat tyto variace poskytováním lepších mantinelů_.

1. **Modely mohou vytvářet smyšlené odpovědi.** Modely jsou předtrénovány na _velkých, ale konečných_ datových sadách, což znamená, že nemají znalosti o konceptech mimo tento rozsah tréninku. Výsledkem je, že mohou produkovat výstupy, které jsou nepřesné, smyšlené nebo přímo protichůdné známým faktům. _Techniky návrhu promptů pomáhají uživatelům identifikovat a zmírnit takové smyšlenky, např. požádáním AI o citace nebo odůvodnění_.

1. **Schopnosti modelů se liší.** Novější modely nebo generace modelů budou mít bohatší schopnosti, ale také přinesou jedinečné zvláštnosti a kompromisy v nákladech a složitosti. _Návrh promptů nám může pomoci vyvinout osvědčené postupy a pracovní postupy, které abstrahují rozdíly a přizpůsobují se požadavkům specifickým pro modely škálovatelným a bezproblémovým způsobem_.

Podívejme se na to v praxi v OpenAI nebo Azure OpenAI Playground:

- Použijte stejný prompt s různými nasazeními LLM (např. OpenAI, Azure OpenAI, Hugging Face) - viděli jste rozdíly?
- Použijte stejný prompt opakovaně se _stejným_ nasazením LLM (např. Azure OpenAI Playground) - jak se tyto variace lišily?

### Příklad smyšlenek

V tomto kurzu používáme termín **"smyšlenka"** k označení jevu, kdy LLM někdy generují fakticky nesprávné informace kvůli omezením ve svém tréninku nebo jiným omezením. Možná jste o tom také slyšeli pod pojmem _"halucinace"_ v populárních článcích nebo výzkumných pracích. Nicméně důrazně doporučujeme používat termín _"smyšlenka"_, abychom náhodou neantropomorfizovali chování tím, že bychom přisuzovali lidskou vlastnost výsledku řízenému strojem. To také posiluje [zásady odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hlediska terminologie, odstraňuje termíny, které mohou být v některých kontextech považovány za urážlivé nebo neinkluzivní.

Chcete získat představu o tom,
Webové vyhledávání mi ukázalo, že existují fiktivní příběhy (např. televizní seriály nebo knihy) o válkách na Marsu – ale žádné z roku 2076. Zdravý rozum nám také říká, že rok 2076 je _v budoucnosti_ a tudíž nemůže být spojen s reálnou událostí.

Co se tedy stane, když tento dotaz zadáme různým poskytovatelům LLM?

> **Odpověď 1**: OpenAI Playground (GPT-35)

![Odpověď 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.cs.png)

> **Odpověď 2**: Azure OpenAI Playground (GPT-35)

![Odpověď 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.cs.png)

> **Odpověď 3**: Hugging Face Chat Playground (LLama-2)

![Odpověď 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.cs.png)

Jak se dalo očekávat, každý model (nebo verze modelu) generuje mírně odlišné odpovědi díky stochastickému chování a rozdílům ve schopnostech modelu. Například jeden model cílí na publikum osmého ročníku, zatímco druhý předpokládá středoškolské studenty. Ale všechny tři modely vytvořily odpovědi, které by mohly přesvědčit neinformovaného uživatele, že událost byla skutečná.

Techniky návrhu dotazů, jako je _metaprompting_ a _konfigurace teploty_, mohou do určité míry snížit výskyt smyšlených odpovědí modelu. Nové _architektury_ návrhu dotazů také bezproblémově začleňují nové nástroje a techniky do toku dotazů, aby zmírnily nebo snížily některé z těchto efektů.

## Případová studie: GitHub Copilot

Tuto sekci zakončíme tím, že si uděláme představu o tom, jak se návrh dotazů používá v reálných řešeních, a podíváme se na jednu případovou studii: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš „AI programátorský partner“ – převádí textové dotazy na návrhy kódu a je integrován do vašeho vývojového prostředí (např. Visual Studio Code) pro bezproblémový uživatelský zážitek. Jak je zdokumentováno v sérii níže uvedených blogů, nejranější verze byla založena na modelu OpenAI Codex – přičemž inženýři rychle zjistili potřebu model doladit a vyvinout lepší techniky návrhu dotazů, aby se zlepšila kvalita kódu. V červenci [představili vylepšený AI model, který jde nad rámec Codexu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pro ještě rychlejší návrhy.

Přečtěte si příspěvky v pořadí, abyste sledovali jejich cestu učení.

- **Květen 2023** | [GitHub Copilot se zlepšuje v porozumění vašemu kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Květen 2023** | [Uvnitř GitHubu: Práce s LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Červen 2023** | [Jak psát lepší dotazy pro GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Červenec 2023** | [.. GitHub Copilot jde nad rámec Codexu s vylepšeným AI modelem](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Červenec 2023** | [Průvodce vývojáře návrhem dotazů a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Září 2023** | [Jak vytvořit podnikovou aplikaci LLM: Lekce z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Můžete také procházet jejich [blog o inženýrství](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pro další příspěvky, jako je [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), který ukazuje, jak jsou tyto modely a techniky _aplikovány_ pro pohon reálných aplikací.

---

## Konstrukce dotazů

Viděli jsme, proč je návrh dotazů důležitý – nyní pochopíme, jak jsou dotazy _konstruovány_, abychom mohli vyhodnotit různé techniky pro efektivnější návrh dotazů.

### Základní dotaz

Začněme základním dotazem: textový vstup zaslaný modelu bez dalšího kontextu. Zde je příklad – když pošleme první slova americké národní hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžitě _dokončí_ odpověď dalšími řádky, což ilustruje základní predikční chování.

| Dotaz (Vstup)     | Dokončení (Výstup)                                                                                                                        |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdá se, že začínáte text „The Star-Spangled Banner“, národní hymny Spojených států. Celý text je ... |

### Komplexní dotaz

Nyní přidáme kontext a instrukce k základnímu dotazu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje vytvořit komplexní dotaz jako kolekci _zpráv_ s:

- Páry vstup/výstup odrážející _uživatelský_ vstup a _odpověď asistenta_.
- Systémovou zprávou nastavující kontext pro chování nebo osobnost asistenta.

Požadavek má nyní podobu níže, kde _tokenizace_ efektivně zachycuje relevantní informace z kontextu a konverzace. Změna systémového kontextu může mít stejně velký dopad na kvalitu dokončení jako poskytnuté uživatelské vstupy.

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

### Instrukční dotaz

V předchozích příkladech byl uživatelský dotaz jednoduchým textovým dotazem, který lze interpretovat jako žádost o informace. U _instrukčních_ dotazů můžeme tento text použít k podrobnějšímu specifikování úkolu, čímž poskytneme AI lepší vodítko. Zde je příklad:

| Dotaz (Vstup)                                                                                                                                                                                                                         | Dokončení (Výstup)                                                                                                        | Typ instrukce      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Napište popis občanské války                                                                                                                                                                     | _vrácen jednoduchý odstavec_                                                                                              | Jednoduchý         |
| Napište popis občanské války. Uveďte klíčová data a události a popište jejich význam                                                                                                             | _vrácen odstavec následovaný seznamem klíčových dat událostí s popisy_                                                    | Komplexní          |
| Napište popis občanské války v 1 odstavci. Uveďte 3 odrážky s klíčovými daty a jejich významem. Uveďte další 3 odrážky s klíčovými historickými postavami a jejich příspěvky. Výstup vraťte jako soubor JSON | _vráceny podrobnější informace v textovém poli, formátované jako JSON, které můžete zkopírovat do souboru a ověřit podle potřeby_ | Komplexní. Formátovaný. |

## Primární obsah

V předchozích příkladech byl dotaz stále poměrně otevřený, což umožnilo LLM rozhodnout, která část jeho předem naučené databáze je relevantní. S návrhovým vzorem _primárního obsahu_ je vstupní text rozdělen na dvě části:

- instrukci (akci)
- relevantní obsah (který ovlivňuje akci)

Zde je příklad, kde je instrukcí „shrňte to ve 2 větách“.

| Dotaz (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončení (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je pátá planeta od Slunce a největší v naší Sluneční soustavě. Je to plynný obr s hmotností tisíciny hmotnosti Slunce, ale dva a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je znám starověkým civilizacím již před zaznamenanou historií. Je pojmenován po římském bohu Jupiterovi.[19] Při pohledu ze Země může být Jupiter dostatečně jasný, aby jeho odražené světlo vrhalo viditelné stíny,[20] a je průměrně třetím nejjasnějším přírodním objektem na noční obloze po Měsíci a Venuši. <br/> **Shrňte to ve 2 krátkých větách** | Jupiter, pátá planeta od Slunce, je největší ve Sluneční soustavě a je známá jako jeden z nejjasnějších objektů na noční obloze. Pojmenovaný po římském bohu Jupiterovi, je plynným obrem s hmotností dva a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. |

Segment primárního obsahu lze použít různými způsoby k efektivnějšímu řízení instrukcí:

- **Příklady** – místo toho, abychom modelu explicitně říkali, co má dělat, poskytneme mu příklady požadovaného výstupu a necháme ho odvodit vzor.
- **Vodítka** – následujeme instrukci „vodítkem“, které připraví model na relevantnější odpovědi.
- **Šablony** – jedná se o opakovatelné „recepty“ pro dotazy s proměnnými (místy), které lze přizpůsobit daty pro konkrétní případy použití.

Pojďme si tyto techniky prozkoumat v praxi.

### Použití příkladů

Toto je přístup, kdy použijete primární obsah k „nakrmení modelu“ několika příklady požadovaného výstupu pro danou instrukci a necháte ho odvodit vzor pro požadovaný výstup. Na základě počtu poskytnutých příkladů můžeme mít zero-shot prompting, one-shot prompting, few-shot prompting atd.

Dotaz nyní sestává ze tří komponent:

- Popis úkolu
- Několik příkladů požadovaného výstupu
- Začátek nového příkladu (který se stává implicitním popisem úkolu)

| Typ učení | Dotaz (Vstup)                                                                                                                                        | Dokončení (Výstup)         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot | "The Sun is Shining". Přeložte do španělštiny                                                                                                         | "El Sol está brillando".    |
| One-shot  | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot  | Hráč oběhl mety => Baseball <br/> Hráč zahrál eso => Tenis <br/> Hráč zahrál šestku => Kriket <br/> Hráč provedl smeč =>                              | Basketbal                   |
|           |                                                                                                                                                       |                             |

Všimněte si, jak jsme museli poskytnout explicitní instrukci („Přeložte do španělštiny“) v zero-shot prompting, ale v one-shot prompting se odvodí. Příklad few-shot ukazuje, jak přidání více příkladů umožňuje modelům dělat přesnější závěry bez dalších instrukcí.

### Vodítka v dotazech

Další technikou pro použití primárního obsahu je poskytnutí _vodítek_ místo příkladů. V tomto případě dáváme modelu „nápovědu“ správným směrem tím, že ho _nastartujeme_ úryvkem, který odráží požadovaný formát odpovědi. Model pak „vezme vodítko“ a pokračuje v tomto duchu.

| Počet vodítek | Dotaz (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončení (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0             | Jupiter je pátá planeta od Slunce a největší v naší Sluneční soustavě. Je to plynný obr s hmotností tisíciny hmotnosti Slunce, ale dva a půlkrát větší než všechny ostatní planety Sluneční soustavy dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je znám starověkým civilizacím již před zaznamenanou historií. <br/>**Shrňte to**                                       | Jupiter je největší planeta v naší Sluneční soustavě a pátá od Slunce. Je to plynný obr s hmotností 1/1000 Slunce, ale je těžší než všechny ostatní planety dohromady. Starověké civilizace znají Jupiter již dlouho a je snadno viditelný na noční obloze. |
| 1              | Jupiter je pátá planeta od Slunce a největší v naší Sluneční soustavě. Je to plynný obr s hmotností tisíciny hmotnosti Slunce, ale dva a půlkrát větší než všechny ostatní planety dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je známý již od dob starověkých civilizací, ještě před zaznamenanou historií. <br/>**Shrňte to** <br/> Co jsme se naučili je, že Jupiter | je pátá planeta od Slunce a největší v naší Sluneční soustavě. Je to plynný obr s hmotností tisíciny hmotnosti Slunce, ale dva a půlkrát větší než všechny ostatní planety dohromady. Je snadno viditelný pouhým okem a je známý již od starověku.                        |
| 2              | Jupiter je pátá planeta od Slunce a největší v naší Sluneční soustavě. Je to plynný obr s hmotností tisíciny hmotnosti Slunce, ale dva a půlkrát větší než všechny ostatní planety dohromady. Jupiter je jedním z nejjasnějších objektů viditelných pouhým okem na noční obloze a je známý již od dob starověkých civilizací, ještě před zaznamenanou historií. <br/>**Shrňte to** <br/> Top 3 fakta, která jsme se naučili:         | 1. Jupiter je pátá planeta od Slunce a největší v naší Sluneční soustavě. <br/> 2. Je to plynný obr s hmotností tisíciny hmotnosti Slunce...<br/> 3. Jupiter je viditelný pouhým okem již od starověku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablony pro zadání

Šablona pro zadání je _předem definovaný recept na zadání_, který lze uložit a znovu použít podle potřeby, aby bylo možné dosáhnout konzistentnějších uživatelských zkušeností ve velkém měřítku. V nejjednodušší formě je to jednoduše sbírka příkladů zadání jako [tento od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), která poskytuje interaktivní komponenty zadání (zprávy uživatele a systému) a formát požadavku řízený API - pro podporu opětovného použití.

V jeho složitější formě, jako [tento příklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), obsahuje _zástupné symboly_, které lze nahradit daty z různých zdrojů (uživatelský vstup, kontext systému, externí datové zdroje atd.) pro dynamické generování zadání. To nám umožňuje vytvořit knihovnu opakovaně použitelných zadání, která lze použít k programovému dosažení konzistentních uživatelských zkušeností ve velkém měřítku.

Nakonec skutečná hodnota šablon spočívá ve schopnosti vytvářet a publikovat _knihovny zadání_ pro vertikální aplikační domény - kde je šablona zadání nyní _optimalizována_ tak, aby odrážela kontext nebo příklady specifické pro aplikaci, které činí odpovědi relevantnějšími a přesnějšími pro cílové uživatelské publikum. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvělým příkladem tohoto přístupu, který kurátoruje knihovnu zadání pro vzdělávací doménu s důrazem na klíčové cíle, jako je plánování lekcí, návrh učebních osnov, doučování studentů atd.

## Podpůrný obsah

Pokud uvažujeme o konstrukci zadání jako o kombinaci instrukce (úkolu) a cíle (primárního obsahu), pak _sekundární obsah_ je jako další kontext, který poskytujeme, aby **ovlivnil výstup nějakým způsobem**. Mohou to být parametry ladění, pokyny k formátování, taxonomie témat atd., které mohou modelu pomoci _přizpůsobit_ jeho odpověď tak, aby vyhovovala požadovaným uživatelským cílům nebo očekáváním.

Například: Vzhledem k katalogu kurzů s rozsáhlými metadaty (název, popis, úroveň, metadata, instruktor atd.) o všech dostupných kurzech v učebních osnovách:

- můžeme definovat instrukci "shrňte katalog kurzů pro podzim 2023"
- můžeme použít primární obsah k poskytnutí několika příkladů požadovaného výstupu
- můžeme použít sekundární obsah k identifikaci 5 nejdůležitějších "tagů".

Nyní může model poskytnout shrnutí ve formátu ukázaném několika příklady - ale pokud má výsledek více tagů, může upřednostnit 5 tagů identifikovaných v sekundárním obsahu.

---

<!--
ŠABLONA LEKCE:
Tato jednotka by měla pokrývat základní koncept #1.
Posilněte koncept pomocí příkladů a odkazů.

KONCEPT #3:
Techniky pro tvorbu zadání.
Jaké jsou základní techniky pro tvorbu zadání?
Ilustrujte je pomocí cvičení.
-->

## Nejlepší postupy pro tvorbu zadání

Nyní, když víme, jak mohou být zadání _konstruována_, můžeme začít přemýšlet o tom, jak je _navrhnout_, aby odrážela nejlepší postupy. Můžeme o tom přemýšlet ve dvou částech - mít správný _přístup_ a aplikovat správné _techniky_.

### Přístup k tvorbě zadání

Tvorba zadání je proces pokusů a omylů, takže mějte na paměti tři široké vodítka:

1. **Porozumění doméně je důležité.** Přesnost a relevance odpovědí závisí na _doméně_, ve které aplikace nebo uživatel působí. Použijte svou intuici a odborné znalosti v dané doméně k **dalšímu přizpůsobení technik**. Například definujte _osobnosti specifické pro doménu_ ve svých systémových zadáních nebo použijte _šablony specifické pro doménu_ ve svých uživatelských zadáních. Poskytněte sekundární obsah, který odráží kontexty specifické pro doménu, nebo použijte _vodítka a příklady specifické pro doménu_, aby model směřoval k známým vzorcům použití.

2. **Porozumění modelu je důležité.** Víme, že modely jsou stochastické povahy. Ale implementace modelů se mohou také lišit z hlediska datových sad, které používají (předem naučené znalosti), schopností, které poskytují (např. prostřednictvím API nebo SDK), a typu obsahu, pro který jsou optimalizovány (např. kód vs. obrázky vs. text). Pochopte silné stránky a omezení modelu, který používáte, a použijte tyto znalosti k _prioritizaci úkolů_ nebo vytvoření _přizpůsobených šablon_, které jsou optimalizovány pro schopnosti modelu.

3. **Iterace a validace jsou důležité.** Modely se rychle vyvíjejí, stejně jako techniky pro tvorbu zadání. Jako odborník na danou doménu můžete mít jiný kontext nebo kritéria pro _vaši_ konkrétní aplikaci, která nemusí platit pro širší komunitu. Použijte nástroje a techniky pro tvorbu zadání k "nastartování" konstrukce zadání, poté iterujte a validujte výsledky pomocí své vlastní intuice a odborných znalostí v dané doméně. Zaznamenejte své poznatky a vytvořte **databázi znalostí** (např. knihovny zadání), která může být použita jako nový základ pro ostatní, pro rychlejší iterace v budoucnu.

## Nejlepší postupy

Nyní se podívejme na běžné nejlepší postupy doporučené odborníky z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Proč                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnoťte nejnovější modely.       | Nové generace modelů pravděpodobně mají lepší funkce a kvalitu - ale mohou také přinést vyšší náklady. Vyhodnoťte jejich dopad, poté se rozhodněte o migraci.                                                                                |
| Oddělte instrukce a kontext.   | Zkontrolujte, zda váš model/provident definuje _oddělovače_ pro jasnější rozlišení instrukcí, primárního a sekundárního obsahu. To může modelům pomoci přesněji přiřadit váhy tokenům.                                                         |
| Buďte konkrétní a jasní.             | Poskytněte více detailů o požadovaném kontextu, výsledku, délce, formátu, stylu atd. To zlepší jak kvalitu, tak konzistenci odpovědí. Zaznamenejte recepty do opakovaně použitelných šablon.                                                          |
| Buďte popisní, používejte příklady.      | Modely mohou lépe reagovat na přístup "ukaž a vysvětli". Začněte s přístupem `zero-shot`, kde mu dáte instrukci (ale žádné příklady), poté zkuste `few-shot` jako vylepšení, poskytnutím několika příkladů požadovaného výstupu. Používejte analogie. |
| Používejte vodítka pro zahájení odpovědí. | Nasměrujte model k požadovanému výsledku tím, že mu poskytnete několik úvodních slov nebo frází, které může použít jako výchozí bod pro odpověď.                                                                                                               |
| Zdůrazněte důležité.                       | Někdy je potřeba modelu zopakovat instrukce. Poskytněte instrukce před a po primárním obsahu, použijte instrukci a vodítko atd. Iterujte a validujte, co funguje.                                                         |
| Pořadí je důležité.                     | Pořadí, ve kterém modelu prezentujete informace, může ovlivnit výstup, dokonce i v učebních příkladech, díky efektu nedávnosti. Vyzkoušejte různé možnosti, abyste zjistili, co funguje nejlépe.                                                               |
| Dejte modelu "únik".           | Poskytněte modelu _záložní_ odpověď, kterou může poskytnout, pokud z nějakého důvodu nemůže úkol dokončit. To může snížit pravděpodobnost, že model vygeneruje nesprávné nebo smyšlené odpovědi.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Stejně jako u jakéhokoli nejlepšího postupu, pamatujte, že _vaše zkušenosti se mohou lišit_ v závislosti na modelu, úkolu a doméně. Použijte je jako výchozí bod a iterujte, abyste zjistili, co funguje nejlépe pro vás. Neustále přehodnocujte svůj proces tvorby zadání, jakmile budou k dispozici nové modely a nástroje, s důrazem na škálovatelnost procesu a kvalitu odpovědí.

<!--
ŠABLONA LEKCE:
Tato jednotka by měla obsahovat výzvu k řešení kódu, pokud je to možné.

VÝZVA:
Odkaz na Jupyter Notebook pouze s komentáři kódu v instrukcích (sekce kódu jsou prázdné).

ŘEŠENÍ:
Odkaz na kopii tohoto Notebooku s vyplněnými a spuštěnými zadáními, ukazující, jak by mohl vypadat jeden příklad.
-->

## Zadání

Gratulujeme! Dostali jste se na konec lekce! Je čas otestovat některé z těchto konceptů a technik na skutečných příkladech!

Pro naše zadání budeme používat Jupyter Notebook s cvičeními, která můžete interaktivně dokončit. Notebook můžete také rozšířit o vlastní buňky Markdown a kódu, abyste mohli sami prozkoumat nápady a techniky.

### Začněte tím, že si forknete repozitář, poté

- (Doporučeno) Spusťte GitHub Codespaces
- (Alternativně) Klonujte repozitář na své lokální zařízení a použijte ho s Docker Desktop
- (Alternativně) Otevřete Notebook ve svém preferovaném prostředí pro běh Notebooků.

### Dále nakonfigurujte své proměnné prostředí

- Zkopírujte soubor `.env.copy` v kořenovém adresáři repozitáře do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Vraťte se do sekce [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), abyste se dozvěděli jak.

### Dále otevřete Jupyter Notebook

- Vyberte runtime kernel. Pokud používáte možnosti 1 nebo 2, jednoduše vyberte výchozí kernel Python 3.10.x poskytovaný vývojářským kontejnerem.

Nyní jste připraveni spustit cvičení. Všimněte si, že zde nejsou žádné _správné nebo špatné_ odpovědi - jde jen o zkoumání možností metodou pokusů a omylů a budování intuice pro to, co funguje pro daný model a aplikační doménu.

_Z tohoto důvodu v této lekci nejsou žádné segmenty řešení kódu. Místo toho bude Notebook obsahovat buňky Markdown s názvem "Moje řešení:", které ukazují jeden příklad výstupu pro referenci._

 <!--
ŠABLONA LEKCE:
Uzavřete sekci shrnutím a zdroji pro samostatné učení.
-->

## Kontrola znalostí

Které z následujících zadání je dobré podle rozumných nejlepších postupů?

1. Ukaž mi obrázek červeného auta
2. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90 zaparkovaného u útesu při západu slunce
3. Ukaž mi obrázek červeného auta značky Volvo a modelu XC90

Odpověď: 2, je to nejlepší zadání, protože poskytuje detaily o "čem" a jde do specifik (ne jen jakékoliv auto, ale konkrétní značka a model) a také popisuje celkové prostředí. 3 je další nejlepší, protože také obsahuje hodně popisu.

## 🚀 Výzva

Zkuste využít techniku "vodítka" s tímto zadáním: Doplňte větu "Ukaž mi obrázek červeného auta značky Volvo a ". Co vám model odpoví a jak byste to vylepšili?

## Skvělá práce! Pokračujte v učení

Chcete se dozvědět více o různých konceptech tvorby zadání? Navštivte [stránku pro další učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde najdete další skvělé zdroje na toto téma.

Přejděte na lekci 5, kde se podíváme na [pokročilé techniky tvorby zadání](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.