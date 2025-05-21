<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:31:15+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "cs"
}
-->
# Úvod do Generativní AI a Velkých jazykových modelů

_(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Generativní AI je umělá inteligence schopná generovat text, obrázky a další typy obsahu. Co z ní dělá fantastickou technologii, je to, že demokratizuje AI; kdokoli ji může použít s pouhým textovým zadáním, větou napsanou v přirozeném jazyce. Nemusíte se učit jazyk jako Java nebo SQL, abyste dosáhli něčeho hodnotného, stačí použít svůj jazyk, říct, co chcete, a AI model vám navrhne řešení. Aplikace a dopady této technologie jsou obrovské, můžete psát nebo rozumět zprávám, psát aplikace a mnohem více, a to vše během několika sekund.

V tomto kurikulu prozkoumáme, jak náš startup využívá generativní AI k odemykání nových scénářů ve světě vzdělávání a jak řešíme nevyhnutelné výzvy spojené se sociálními dopady její aplikace a technologickými omezeními.

## Úvod

Tato lekce pokryje:

- Úvod do obchodního scénáře: naše startupová myšlenka a mise.
- Generativní AI a jak jsme se dostali k současné technologické krajině.
- Vnitřní fungování velkého jazykového modelu.
- Hlavní schopnosti a praktické případy použití Velkých jazykových modelů.

## Cíle učení

Po dokončení této lekce budete rozumět:

- Co je generativní AI a jak fungují Velké jazykové modely.
- Jak můžete využít velké jazykové modely pro různé případy použití, se zaměřením na vzdělávací scénáře.

## Scénář: náš vzdělávací startup

Generativní umělá inteligence (AI) představuje vrchol AI technologie, posouvající hranice toho, co bylo kdysi považováno za nemožné. Generativní AI modely mají několik schopností a aplikací, ale pro toto kurikulum prozkoumáme, jak revolucionalizují vzdělávání prostřednictvím fiktivního startupu. Budeme na tento startup odkazovat jako na _náš startup_. Náš startup pracuje v oblasti vzdělávání s ambiciózním prohlášením mise

> _zlepšit přístupnost ve vzdělávání na globální úrovni, zajistit rovný přístup ke vzdělání a poskytovat personalizované vzdělávací zážitky každému studentovi podle jeho potřeb_.

Tým našeho startupu si je vědom, že tohoto cíle nedosáhneme bez využití jednoho z nejmocnějších nástrojů moderní doby – Velkých jazykových modelů (LLMs).

Generativní AI se očekává, že zrevolucionalizuje způsob, jakým se dnes učíme a učíme, s tím, že studenti budou mít k dispozici virtuální učitele 24 hodin denně, kteří poskytují obrovské množství informací a příkladů, a učitelé budou moci využívat inovativní nástroje k hodnocení svých studentů a poskytování zpětné vazby.

Na začátek si definujme některé základní pojmy a terminologii, které budeme používat v průběhu kurikula.

## Jak jsme se dostali ke Generativní AI?

Navzdory mimořádnému _hype_ vytvořenému nedávno oznámením generativních AI modelů, tato technologie je ve vývoji již desítky let, přičemž první výzkumné úsilí sahá až do 60. let. Nyní jsme na bodě, kdy AI má lidské kognitivní schopnosti, jako je konverzace, jak ukazují například [OpenAI ChatGPT](https://openai.com/chatgpt) nebo [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), který také používá GPT model pro vyhledávání Bing konverzací.

Když se trochu vrátíme zpět, první prototypy AI sestávaly z psacích chatbotů, spoléhajících na znalostní bázi extrahovanou ze skupiny odborníků a reprezentovanou v počítači. Odpovědi ve znalostní bázi byly spouštěny klíčovými slovy, která se objevovala ve vstupním textu. Brzy se však ukázalo, že takový přístup, využívající psací chatboty, se dobře neškáluje.

### Statistický přístup k AI: Strojové učení

Zlom nastal v 90. letech s aplikací statistického přístupu k analýze textu. To vedlo k vývoji nových algoritmů – známých jako strojové učení – schopných učit se vzory z dat, aniž by byly explicitně naprogramovány. Tento přístup umožňuje strojům simulovat lidské porozumění jazyku: statistický model je trénován na párech text-štítek, což umožňuje modelu klasifikovat neznámý vstupní text s předdefinovaným štítkem reprezentujícím úmysl zprávy.

### Neuronové sítě a moderní virtuální asistenti

V posledních letech technologický vývoj hardwaru, schopného zpracovávat větší množství dat a složitější výpočty, podpořil výzkum v oblasti AI, což vedlo k vývoji pokročilých algoritmů strojového učení známých jako neuronové sítě nebo algoritmy hlubokého učení.

Neuronové sítě (a zejména Recurrent Neural Networks – RNNs) významně zlepšily zpracování přirozeného jazyka, umožňující reprezentaci významu textu smysluplnějším způsobem, oceňujícím kontext slova ve větě.

To je technologie, která poháněla virtuální asistenty zrozené v první dekádě nového století, velmi zdatné v interpretaci lidského jazyka, identifikaci potřeby a provádění akce k jejímu uspokojení – jako je odpověď s předdefinovaným skriptem nebo využití služby třetí strany.

### Současnost, Generativní AI

Tak jsme se dostali k dnešní Generativní AI, kterou lze považovat za podmnožinu hlubokého učení.

Po desetiletích výzkumu v oblasti AI nová architektura modelu – nazývaná _Transformer_ – překonala limity RNNs, schopna přijmout mnohem delší sekvence textu jako vstup. Transformery jsou založeny na mechanismu pozornosti, umožňujícím modelu dávat různé váhy vstupům, které přijímá, „věnovat více pozornosti“ tam, kde je soustředěna nejrelevantnější informace, bez ohledu na jejich pořadí v textové sekvenci.

Většina nedávných generativních AI modelů – také známých jako Velké jazykové modely (LLMs), protože pracují s textovými vstupy a výstupy – je skutečně založena na této architektuře. Co je na těchto modelech zajímavé – trénovaných na obrovském množství neoznačených dat z různých zdrojů, jako jsou knihy, články a webové stránky – je, že je lze přizpůsobit široké škále úkolů a generovat gramaticky správný text s nádechem kreativity. Takže nejen že neuvěřitelně zvýšily schopnost stroje „porozumět“ vstupnímu textu, ale umožnily jejich schopnost generovat originální odpověď v lidském jazyce.

## Jak fungují velké jazykové modely?

V další kapitole prozkoumáme různé typy generativních AI modelů, ale nyní se podívejme na to, jak fungují velké jazykové modely, se zaměřením na modely OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, text na čísla**: Velké jazykové modely přijímají text jako vstup a generují text jako výstup. Nicméně, jako statistické modely, pracují mnohem lépe s čísly než s textovými sekvencemi. Proto je každý vstup do modelu zpracován tokenizerem, než je použit jádrem modelu. Token je kus textu – skládající se z proměnlivého počtu znaků, takže hlavním úkolem tokenizeru je rozdělit vstup na pole tokenů. Poté je každý token mapován s tokenovým indexem, což je celočíselné kódování původního textového kusu.

- **Předpovídání výstupních tokenů**: Daných n tokenů jako vstup (s maximem n se liší od jednoho modelu k druhému), model je schopen předpovědět jeden token jako výstup. Tento token je pak začleněn do vstupu další iterace, v rozšiřujícím se okně, což umožňuje lepší uživatelský zážitek z získání jedné (nebo více) vět jako odpovědi. To vysvětluje, proč, pokud jste někdy hráli s ChatGPT, mohli jste si všimnout, že někdy to vypadá, jako by se zastavil uprostřed věty.

- **Proces výběru, rozdělení pravděpodobnosti**: Výstupní token je vybrán modelem podle jeho pravděpodobnosti výskytu po aktuální textové sekvenci. To je proto, že model předpovídá rozdělení pravděpodobnosti nad všemi možnými „následujícími tokeny“, vypočítané na základě jeho tréninku. Nicméně, ne vždy je vybrán token s nejvyšší pravděpodobností z výsledného rozdělení. Do této volby je přidán stupeň náhodnosti, takovým způsobem, že model jedná v nedeterministickém módu – nedostáváme stejný výstup pro stejný vstup. Tento stupeň náhodnosti je přidán k simulaci procesu kreativního myšlení a lze jej ladit pomocí modelového parametru nazývaného teplota.

## Jak může náš startup využít Velké jazykové modely?

Nyní, když máme lepší pochopení vnitřního fungování velkého jazykového modelu, podívejme se na některé praktické příklady nejběžnějších úkolů, které mohou vykonávat docela dobře, s ohledem na náš obchodní scénář. Řekli jsme, že hlavní schopnost Velkého jazykového modelu je _generovat text od nuly, počínaje textovým vstupem, napsaným v přirozeném jazyce_.

Ale jaký druh textového vstupu a výstupu?
Vstup velkého jazykového modelu je znám jako prompt, zatímco výstup je znám jako dokončení, termín, který se vztahuje k mechanismu modelu generujícího další token k dokončení aktuálního vstupu. Ponoříme se hlouběji do toho, co je prompt a jak jej navrhnout tak, abychom z modelu získali maximum. Ale prozatím řekněme, že prompt může zahrnovat:

- **Instrukci** specifikující typ výstupu, který od modelu očekáváme. Tato instrukce někdy může zahrnovat některé příklady nebo nějaká dodatečná data.

  1. Shrnutí článku, knihy, recenzí produktů a dalších, spolu s extrakcí poznatků z nestrukturovaných dat.

  2. Kreativní nápady a návrh článku, eseje, úkolu nebo dalších.

- **Otázku**, položenou ve formě konverzace s agentem.

- Kus **textu k dokončení**, což implicitně je žádost o pomoc při psaní.

- Kus **kódu** spolu s žádostí o vysvětlení a dokumentaci, nebo komentář žádající o generování kódu provádějícího konkrétní úkol.

Výše uvedené příklady jsou poměrně jednoduché a nejsou zamýšleny jako vyčerpávající ukázka schopností Velkých jazykových modelů. Mají ukázat potenciál použití generativní AI, zejména ale nejen ve vzdělávacích kontextech.

Také výstup generativního AI modelu není dokonalý a někdy kreativita modelu může působit proti němu, což vede k výstupu, který je kombinací slov, kterou může lidský uživatel interpretovat jako mystifikaci reality, nebo může být urážlivý. Generativní AI není inteligentní – alespoň ve více komplexní definici inteligence, zahrnující kritické a kreativní myšlení nebo emoční inteligenci; není deterministická a není důvěryhodná, protože vymyšleniny, jako jsou nesprávné odkazy, obsah a tvrzení, mohou být kombinovány se správnými informacemi a prezentovány přesvědčivým a sebevědomým způsobem. V následujících lekcích se budeme zabývat všemi těmito omezeními a uvidíme, co můžeme udělat, abychom je zmírnili.

## Úkol

Vaším úkolem je více se seznámit s [generativní AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) a pokusit se identifikovat oblast, kde byste dnes přidali generativní AI, která ji nemá. Jak by byl dopad jiný oproti tomu, kdybyste to dělali „starým způsobem“, můžete udělat něco, co jste předtím nemohli, nebo jste rychlejší? Napište 300slovné shrnutí toho, jak by váš vysněný AI startup vypadal a zahrňte nadpisy jako "Problém", "Jak bych použil AI", "Dopad" a případně obchodní plán.

Pokud jste tento úkol splnili, možná jste dokonce připraveni přihlásit se do inkubátoru Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), kde nabízíme kredity jak pro Azure, OpenAI, mentoring a mnohem více, podívejte se na to!

## Kontrola znalostí

Co je pravda o velkých jazykových modelech?

1. Dostanete stejnou odpověď pokaždé.
1. Dělá věci perfektně, skvělé v sčítání čísel, produkci fungujícího kódu atd.
1. Odpověď se může lišit navzdory použití stejného promptu. Je také skvělý pro poskytnutí prvního návrhu něčeho, ať už je to text nebo kód. Ale musíte zlepšit výsledky.

Odpověď: 3, LLM je nedeterministický, odpověď se liší, nicméně můžete kontrolovat její variabilitu pomocí nastavení teploty. Také byste neměli očekávat, že bude dělat věci perfektně, je tu proto, aby za vás udělal těžkou práci, což často znamená, že dostanete dobrý první pokus o něco, co musíte postupně vylepšit.

## Skvělá práce! Pokračujte v cestě

Po dokončení této lekce se podívejte na naši [sbírku učení o Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v zvyšování svých znalostí o Generativní AI!

Přejděte k Lekci 2, kde se podíváme na to, jak [prozkoumat a porovnat různé typy LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Prohlášení:**
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.