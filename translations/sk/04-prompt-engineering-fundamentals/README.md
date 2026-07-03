# Základy navrhovania promptov

[![Základy navrhovania promptov](../../../translated_images/sk/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrýva základné koncepty a techniky pre tvorbu efektívnych promptov v generatívnych AI modeloch. Spôsob, akým zadáte prompt do veľkého jazykového modelu (LLM), je tiež dôležitý. Premyslený prompt môže priniesť lepšiu kvalitu odpovede. Ale čo presne znamenajú pojmy ako _prompt_ a _navrhovanie promptov_? A ako zlepšiť _vstup_ promptu, ktorý posielam do LLM? Na tieto otázky sa pokúsime odpovedať v tejto kapitole a nasledujúcej.

_Generatívna AI_ je schopná vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) v reakcii na požiadavky používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ ako séria GPT od OpenAI ("Generative Pre-trained Transformer"), ktoré sú trénované na prácu s prirodzeným jazykom a kódom.

Používatelia teraz môžu interagovať s týmito modelmi pomocou známych spôsobov, ako je chat, bez potreby technických znalostí alebo školení. Modely sú _postavené na prompte_ - používatelia posielajú textový vstup (prompt) a dostávajú odpoveď AI (dokončenie). Môžu potom "rozprávať sa s AI" iteratívne v viackolových konverzáciách a dolaďovať svoj prompt, až kým odpoveď nevyhovuje ich očakávaniam.

"Prompty" sa teraz stávajú primárnym _programovacím rozhraním_ pre generatívne AI aplikácie, ktoré hovoria modelom, čo majú robiť, a ovplyvňujú kvalitu vrátených odpovedí. "Navrhovanie promptov" je rýchlo rastúca disciplína, ktorá sa zameriava na _návrh a optimalizáciu_ promptov pre dosiahnutie konzistentných a kvalitných odpovedí vo veľkom rozsahu.

## Ciele vzdelávania

V tejto lekcii sa naučíme, čo je navrhovanie promptov, prečo je dôležité a ako môžeme vytvárať efektívnejšie prompty pre daný model a cieľ aplikácie. Pochopíme základné koncepty a najlepšie postupy pre navrhovanie promptov - a naučíme sa o interaktívnom prostredí Jupyter Notebook sandbox, kde si tieto koncepty môžeme vyskúšať na reálnych príkladoch.

Na konci tejto lekcie budeme schopní:

1. Vysvetliť, čo je navrhovanie promptov a prečo je dôležité.
2. Popísať komponenty promptu a ich využitie.
3. Naučiť sa najlepšie postupy a techniky navrhovania promptov.
4. Aplikovať naučené techniky na reálne príklady s použitím OpenAI endpointu.

## Kľúčové pojmy

Navrhovanie promptov: Praktika navrhovania a dolaďovania vstupov na usmernenie AI modelov k požadovaným výstupom.  
Tokenizácia: Proces rozdelenia textu na menšie jednotky, nazývané tokeny, ktoré model dokáže spracovať.  
Instruction-Tuned LLMs: Veľké jazykové modely (LLM), ktoré boli doladené s konkrétnymi inštrukciami pre zlepšenie presnosti a relevantnosti odpovedí.

## Výučbový sandbox

Navrhovanie promptov je dnes skôr umenie ako veda. Najlepší spôsob, ako zlepšiť svoju intuíciu, je _viac praxe_ a používanie metódy pokus-omyl, ktorá spája odborné znalosti v danej oblasti s odporúčanými technikami a optimalizáciami špecifickými pre modely.

Jupyter Notebook k tejto lekcii poskytuje _sandbox_ prostredie, kde si môžete vyskúšať, čo sa naučíte – priebežne alebo ako súčasť záverečného cvičenia. Na spustenie úloh budete potrebovať:

1. **Azure OpenAI API kľúč** – koncový bod služby pre nasadený LLM.  
2. **Python runtime** – prostredie, v ktorom sa notebook spustí.  
3. **Lokálne premenné prostredia** – _splňte kroky v [SETUPE](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) na pripravenie_.

Notebook obsahuje _štartovacie_ cvičenia – ale ste povzbudzovaní, aby ste pridávali vlastné _Markdown_ (popisy) a _Code_ (žiadosti promptov) sekcie, aby ste mohli vyskúšať viac príkladov alebo nápadov – a rozvíjať intuície pri návrhu promptov.

## Ilustrovaný sprievodca

Chcete najskôr získať celkový obraz toho, čo táto lekcia pokrýva? Pozrite sa na tento ilustrovaný sprievodca, ktorý vám poskytne prehľad o hlavných témach a kľúčových bodov na zamyslenie v každej z nich. Plán lekcie vás povedie od pochopenia základných konceptov a výziev až po ich riešenie pomocou príslušných techník navrhovania promptov a najlepších postupov. Sekcia "Pokročilé techniky" v tomto sprievodcovi sa vzťahuje na obsah nasledujúcej kapitoly tohto kurzu.

![Ilustrovaný sprievodca navrhovaním promptov](../../../translated_images/sk/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naša startupová misia

Teraz sa porozprávajme o tom, ako sa _táto téma_ spája s misiou nášho startupu prinášať [inovácie AI do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať AI poháňané aplikácie pre _personalizované učenie_ – tak poďme premýšľať, ako môžu rôzni používatelia našej aplikácie "navrhovať" prompty:

- **Administrátori** môžu požiadať AI o _analýzu údajov o učebných osnovách za účelom identifikácie medzier v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať pomocou kódu.  
- **Pedagógovia** môžu požiadať AI o _vytvorenie plánu hodiny pre cieľovú skupinu a tému_. AI dokáže vytvoriť personalizovaný plán v požadovanom formáte.  
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI teraz môže študentov viesť lekciami, nápovedami a príkladmi prispôsobenými ich úrovni.

To je len špička ľadovca. Prezrite si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – open-source knižnicu promptov spravovanú odborníkmi na vzdelávanie – aby ste získali širší prehľad o možnostiach! _Vyskúšajte spustiť niektoré z týchto promptov v sandboxe alebo v OpenAI Playground a uvidíte, čo sa stane!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Čo je navrhovanie promptov?

Lekciu sme začali definíciou **navrhovania promptov** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) s cieľom zabezpečiť konzistentné a kvalitné odpovede (dokončenia) pre daný cieľ aplikácie a model. Môžeme si to predstaviť ako dvojetapový proces:

- _navrhnutie_ počiatočného promptu pre daný model a cieľ  
- _iteratívne dolaďovanie_ promptu pre zlepšenie kvality odpovede

Je to nevyhnutne proces pokus-omyl, ktorý vyžaduje intuíciu používateľa a úsilie na dosiahnutie optimálnych výsledkov. Prečo je to teda také dôležité? Na túto otázku odpovieme po pochopení troch konceptov:

- _Tokenizácia_ = ako model "vidí" prompt  
- _Základné LLM_ = ako základný model "spracováva" prompt  
- _Instruction-Tuned LLM_ = ako model teraz chápe "úlohy"

### Tokenizácia

LLM vidí prompty ako _sekvenciu tokenov_, pričom rôzne modely (alebo verzie modelu) môžu ten istý prompt tokenizovať rôznymi spôsobmi. Keďže LLM sú trénované na tokenoch (nie na surovom texte), spôsob tokenizácie promptov má priamy vplyv na kvalitu generovanej odpovede.

Pre lepšiu intuíciu, ako tokenizácia funguje, vyskúšajte nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) uvedený nižšie. Skopírujte svoj prompt a pozrite sa, ako sa prevedie na tokeny, venujte pozornosť tomu, ako sú spracované medzery a interpunkčné znaky. Upozorňujeme, že tento príklad zobrazuje starší LLM (GPT-3), takže vyskúšanie s novším modelom môže priniesť iný výsledok.

![Tokenizácia](../../../translated_images/sk/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Základné modely

Po tokenizácii promptu je primárnou funkciou ["základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo základného modelu) predpoveď ďalšieho tokenu v sekvencii. Keďže LLM sú trénované na masívnych textových dátach, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a dokážu túto predpoveď vykonať s určitým stupňom istoty. Treba poznamenať, že ony nerozumejú _významu_ slov v prompte alebo tokenoch; vidia totiž vzor, ktorý môžu "dokončiť" ďalšou predpoveďou. Môžu pokračovať v predpovedaní sekvencie, kým nie sú zastavené používateľom alebo nejakou predom stanovenou podmienkou.

Chcete vidieť, ako funguje dokončenie založené na prompte? Zadajte vyššie uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s predvolenými nastaveniami. Systém je nastavený tak, aby považoval prompt za požiadavku na informácie – tým pádom uvidíte dokončenie, ktoré tomuto kontextu vyhovuje.

Ale čo ak by používateľ chcel vidieť niečo konkrétne, čo spĺňa nejaké kritériá alebo úlohu? Tu prichádzajú do hry _instruction-tuned_ LLM.

![Dokončenie chatu základným LLM](../../../translated_images/sk/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction-Tuned LLM

[Instruction-tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začína so základným modelom a doladí ho pomocou príkladov alebo párov vstup/výstup (napr. viackolové "správy"), ktoré môžu obsahovať jasné inštrukcie - a odpoveď AI sa ich snaží plniť.

Používa techniky ako Reinforcement Learning with Human Feedback (RLHF), ktoré model naučia _dodržiavať inštrukcie_ a _učiť sa z spätnej väzby_, aby poskytoval odpovede vhodnejšie pre praktické použitia a relevantnejšie k cieľom používateľa.

Skúsme to – vráťte sa k predchádzajúcemu promptu, ale teraz zmeňte _systémovú správu_ tak, aby obsahovala túto inštrukciu ako kontext:

> _Zhrň obsah, ktorý dostaneš, pre druháka. Výsledok maj v jednom odstavci s 3-5 bodmi._

Vidíte, ako výsledok teraz ladí s požadovaným cieľom a formátom? Pedagóg môže túto odpoveď priamo použiť vo svojich prezentáciách pre danú triedu.

![Dokončenie chatu instruction-tuned LLM](../../../translated_images/sk/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Prečo potrebujeme navrhovanie promptov?

Teraz, keď vieme, ako LLM spracovávajú prompty, poďme sa pozrieť, _prečo_ potrebujeme navrhovanie promptov. Odpoveď spočíva v tom, že aktuálne LLM predstavujú niekoľko výziev, ktoré sťažia dosahovanie _spoľahlivých a konzistentných dokončení_ bez snahy o správnu konštrukciu a optimalizáciu promptu. Napríklad:

1. **Výstupy modelov sú stochastické.** _Ten istý prompt_ pravdepodobne vyprodukuje rôzne odpovede s rôznymi modelmi alebo ich verziami. A dokonca môže byť výsledok rôzny so _stejným modelom_ pri rôznych spusteniach. _Techniky navrhovania promptov nám pomáhajú tieto variácie minimalizovať poskytnutím lepších mantinelov_.

1. **Modely môžu vymýšľať odpovede.** Modely sú predtrénované na _veľkých, ale konečných_ datasúboroch, čo znamená, že môžu postrádať znalosti o konceptoch mimo rozsahu tréningu. Výsledkom môžu byť nepresné, fiktívne alebo priamo protirečiace fakty odpovede. _Techniky navrhovania promptov pomáhajú používateľom identifikovať a zmierniť takéto vymýšľanie, napríklad požiadavkou na citácie alebo zdôvodnenia_.

1. **Schopnosti modelov sa líšia.** Novšie modely alebo ich generácie budú mať bohatšie schopnosti, no tiež prinášajú špecifické zvláštnosti a kompenzácie v nákladoch a zložitosti. _Navrhovanie promptov nám umožňuje rozvíjať najlepšie praktiky a pracovné postupy, ktoré abstrahujú rozdiely a prispôsobujú sa špecifickým požiadavkám modelu v škálovateľných a plynulých spôsoboch_.

Pozrime sa na to v praxi v OpenAI alebo Azure OpenAI Playground:

- Použite ten istý prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) – videli ste variácie?  
- Použite ten istý prompt viackrát so _stejným_ LLM nasadením (napr. Azure OpenAI Playground) – ako sa líšili odpovede?

### Príklad vymýšľania

V tomto kurze používame výraz **"vymýšľanie"** na označenie javu, keď LLM niekedy generujú fakticky nesprávne informácie z dôvodu obmedzení v ich tréningu alebo iných okolností. Toto ste možno počuli ako _"halucinácie"_ v populárnych článkoch alebo výskumných prácach. Odporúčame však používať výraz _"vymýšľanie"_, aby sme sa vyhli náhodnému priraďovaniu ľudských vlastností k strojom poháňaným výsledkom. Toto tiež posilňuje [zásady zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hľadiska terminológie, vynechávajúc výrazy, ktoré môžu byť v niektorých kontextoch považované za urážlivé alebo nevhodné.

Chcete získať predstavu o tom, ako funguje vymýšľanie? Predstavte si prompt, ktorý AI prikazuje generovať obsah na neexistujúcu tému (aby ste sa uistili, že sa táto téma nenachádza v trénovacom dátovom sete). Napríklad – vyskúšal som tento prompt:

> **Prompt:** Vytvor plán hodiny o Martianskej vojne v roku 2076.
Webové vyhľadávanie mi ukázalo, že existovali fiktívne príbehy (napr. televízne seriály alebo knihy) o marťanských vojnách – ale žiadne z roku 2076. Zdravý rozum tiež hovorí, že rok 2076 je _v budúcnosti_ a teda nemôže byť spojený so skutočnou udalosťou.

Tak čo sa stane, keď tento prompt spustíme s rôznymi poskytovateľmi LLM?

> **Odpoveď 1**: OpenAI Playground (GPT-35)

![Odpoveď 1](../../../translated_images/sk/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpoveď 2**: Azure OpenAI Playground (GPT-35)

![Odpoveď 2](../../../translated_images/sk/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpoveď 3**: : Hugging Face Chat Playground (LLama-2)

![Odpoveď 3](../../../translated_images/sk/04-fabrication-huggingchat.faf82a0a51278956.webp)

Ako sa dalo očakávať, každý model (alebo verzia modelu) generuje mierne odlišné odpovede vďaka stochastickému správaniu a rôznym schopnostiam modelu. Napríklad jeden model cieli na publikum ôsmej triedy, zatiaľ čo iný predpokladá študenta strednej školy. Ale všetky tri modely vytvorili odpovede, ktoré by mohli presvedčiť neinformovaného používateľa, že daná udalosť bola skutočná.

Techniky promptového inžinierstva ako _metaprompting_ a _nastavenie teploty_ môžu do určitej miery znížiť fabulácie modelov. Nové _architektúry_ promptového inžinierstva tiež bezproblémovo integrujú nové nástroje a techniky do toku promptov, aby zmiernili alebo znížili niektoré z týchto efektov.

## Prípadová štúdia: GitHub Copilot

Uzavrieme túto časť pohľadom na to, ako sa promptové inžinierstvo využíva v reálnych riešeniach, a to prostredníctvom jednej prípadovej štúdie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš "AI parťák programátora" – premení textové promptové vstupy na dokončenia kódu a je integrovaný vo vašom vývojovom prostredí (napr. Visual Studio Code) pre bezproblémový používateľský zážitok. Ako je zdokumentované v sérii blogov nižšie, najskoršia verzia bola založená na OpenAI Codex modeli – pričom inžinieri rýchlo pochopili potrebu doladiť model a vyvinúť lepšie techniky promptového inžinierstva na zlepšenie kvality kódu. V júli predstavili [vylepšený AI model, ktorý presahuje Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pre ešte rýchlejšie návrhy.

Prečítajte si príspevky v poradí, aby ste nasledovali ich učenie.

- **Máj 2023** | [GitHub Copilot sa lepšie učí rozumieť vášmu kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Máj 2023** | [Inside GitHub: Práca s LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jún 2023** | [Ako písať lepšie prompty pre GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Júl 2023** | [.. GitHub Copilot ide nad rámec Codex s vylepšeným AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Júl 2023** | [Sprievodca vývojára promptovým inžinierstvom a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Ako vybudovať podnikový LLM app: Lekcie z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Môžete tiež prezerať ich [inžiniersky blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pre viac príspevkov ako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ktorý ukazuje, ako sa tieto modely a techniky _aplikujú_ na reálne projekty.

---

## Konštrukcia promptu

Videli sme, prečo je promptové inžinierstvo dôležité – teraz pochopme, ako sa prompt _konštruuje_, aby sme mohli vyhodnocovať rôzne techniky na efektívnejší návrh promptov.

### Základný prompt

Začnime so základným promptom: textovým vstupom zaslaným modelu bez ďalšieho kontextu. Tu je príklad – keď odošleme prvé slová národnej hymny USA na OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), model okamžite _doplní_ odpoveď ďalšími riadkami, ilustrujúc základné predikčné správanie.

| Prompt (Vstup)      | Dokončenie (Výstup)                                                                                                                         |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdá sa, že začínate text piesne "The Star-Spangled Banner," národnej hymny Spojených štátov. Celý text piesne je ... |

### Komplexný prompt

Teraz pridajme kontext a inštrukcie k základnému promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) umožňuje konštruovať komplexný prompt ako zbierku _správ_ s:

- páry vstup/výstup znázorňujúcimi vstup používateľa a odpoveď asistenta.
- systémovou správou nastavujúcou kontext správania alebo osobnosti asistenta.

Požiadavka je teraz v nasledovnej forme, kde _tokenizácia_ efektívne zachytáva relevantné informácie z kontextu a rozhovoru. Zmena systémového kontextu môže mať rovnaký dopad na kvalitu dokončení ako vstupy používateľa.

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

### Inštrukčný prompt

V príkladoch vyššie bol prompt používateľa jednoduchý textový dopyt, ktorý sa môže interpretovať ako požiadavka na informácie. Pri _inštrukčných_ promptoch môžeme tento text použiť na podrobnejšie špecifikovanie úlohy a poskytnúť AI lepšie usmernenie. Tu je príklad:

| Prompt (Vstup)                                                                                                                                                                                                                         | Dokončenie (Výstup)                                                                                                        | Typ inštrukcie     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napíš popis Občianskej vojny                                                                                                                                                                                                            | _vrátil jednoduchý odstavec_                                                                                              | Jednoduché          |
| Napíš popis Občianskej vojny. Uveď kľúčové dátumy a udalosti a popíš ich význam                                                                                                                                                         | _vrátil odstavec nasledovaný zoznamom kľúčových dátumov udalostí s popisom_                                               | Komplexné           |
| Napíš popis Občianskej vojny v jednom odstavci. Uveď 3 odrážky s kľúčovými dátumami a ich významom. Uveď 3 ďalšie odrážky so známymi historickými osobnosťami a ich prínosmi. Výstup vráť vo formáte JSON | _vracia rozsiahlejší text v textovom okne, naformátovaný ako JSON, ktorý možno podľa potreby kopírovať do súboru a overiť_ | Komplexné. Formátované. |

## Primárny obsah

V príkladoch vyššie bol prompt stále pomerne otvorený, čo necháva LLM rozhodnúť, ktorá časť jeho predtrénovanej dátovej množiny je relevantná. Pri dizajnovom vzore _primárny obsah_ je vstupný text rozdelený na dve časti:

- inštrukcia (akcia)
- relevantný obsah (ktorý ovplyvňuje akciu)

Tu je príklad, kde inštrukcia je "zhrň toto v 2 vetách".

| Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončenie (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou jedna tisícina hmotnosti Slnka, ale dvojnásobne väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jeden z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. Je pomenovaný po rímskom bohovi Jupiterovi.[19] Keď ho pozorujeme zo Zeme, môže byť jasný natoľko, že jeho odrazené svetlo vrhá viditeľné tiene,[20] a v priemere je tretím najsvetlejším prírodným objektom na nočnej oblohe po Mesiaci a Venuši. <br/> **Zhrň toto do 2 krátkych viet** | Jupiter, piata planéta od Slnka, je najväčšia v Slnečnej sústave a je známa ako jeden z najsvetlejších objektov na nočnej oblohe. Pomenovaná po rímskom bohovi Jupiterovi, je to plynný obor s hmotnosťou dvojnásobnou ako všetky ostatné planéty Slnečnej sústavy dokopy. |

Segment primárneho obsahu možno využiť rôznymi spôsobmi na podporu efektívnejších inštrukcií:

- **Príklady** – namiesto explicitného povedania modelu, čo má robiť, mu dajte príklady a nech nechá na ňom, aby odvodenie vzoru.
- **Náznaky** – pridajte ku inštrukcii "náznak", ktorý nasmeruje dokončenie, čím model navediete k relevantnejším odpovediam.
- **Šablóny** – opakovateľné "recepty" na prompty s zástupnými znakmi (premennými), ktoré možno prispôsobiť dátami pre konkrétne prípady použitia.

Pozrime sa na to v praxi.

### Použitie príkladov

Toto je prístup, kde použijete primárny obsah na "napájanie modelu" príkladmi požadovaného výstupu pre danú inštrukciu, a necháte model odvodiť vzor požadovaného výstupu. Na základe počtu poskytnutých príkladov rozlišujeme zero-shot prompting, one-shot prompting, few-shot prompting a pod.

Prompt sa teraz skladá z troch častí:

- popis úlohy
- niekoľko príkladov požadovaného výstupu
- začiatok nového príkladu (čo sa stáva implicitným popisom úlohy)

| Typ učenia    | Prompt (Vstup)                                                                                                                                        | Dokončenie (Výstup)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Prelož do španielčiny                                                                                                          | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Hráč prebehol základne => Baseball <br/> Hráč získal esáčko => Tenis <br/> Hráč zaznamenal šesť => Kriket <br/> Hráč dal slam-dunk => | Basketbal                  |
|               |                                                                                                                                                       |                             |

Všimnite si, že pri zero-shot prompting museli sme explicitne uviesť inštrukciu ("Prelož do španielčiny"), ale tá sa odvádza v one-shot prompting príklade. Few-shot príklad ukazuje, že pridaním viacerých príkladov môžu modely robiť presnejšie závery bez ďalších inštrukcií.

### Náznaky promptu

Ďalšou technikou použitia primárneho obsahu je poskytovať _náznaky_ namiesto príkladov. V tomto prípade modelu dodáme podnet správnym smerom _začiatkom_ textu, ktorý odráža požadovaný formát odpovede. Model potom "zachytí náznak" a pokračuje v danom štýle.

| Počet náznakov | Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončenie (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou jedna tisícina hmotnosti Slnka, ale dvojnásobne väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jeden z najjasnejších objektov viditeľných voľným okom na nočnej oblohe, a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrň toto**                                       | Jupiter je najväčšia planéta v našej Slnečnej sústave a piata od Slnka. Je to plynný obor s hmotnosťou 1/1000 hmotnosti Slnka, ale ťažší ako všetky ostatné planéty dokopy. Staroveké civilizácie poznali Jupiter už dávno a je ľahko viditeľný na nočnej oblohe.                           |
| 1              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou približne tisícinu hmotnosti Slnka, no s hmotnosťou dvoch a pol násobku všetkých ostatných planét v Slnečnej sústave dokopy. Jupiter je jeden z najjasnejších objektov, ktoré sú voľným okom viditeľné na nočnej oblohe, a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrnutie** <br/> Čo sme sa naučili je, že Jupiter | je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou približne tisícinu hmotnosti Slnka, no dvojnásobne väčšou ako všetky ostatné planéty dokopy. Je ľahko viditeľný voľným okom a je známy od dávnych čias.                       |
| 2              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou približne tisícinu hmotnosti Slnka, no s hmotnosťou dvoch a pol násobku všetkých ostatných planét v Slnečnej sústave dokopy. Jupiter je jeden z najjasnejších objektov, ktoré sú voľným okom viditeľné na nočnej oblohe, a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrnutie** <br/> Top 3 fakty, ktoré sme sa naučili:         | 1. Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. <br/> 2. Je to plynný obor s hmotnosťou približne tisícinu hmotnosti Slnka...<br/> 3. Jupiter je voľným okom viditeľný od dávnych čias ...                                                                                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablóny výziev

Šablóna výzvy je _preddefinovaný recept na výzvu_, ktorý možno uložiť a znova použiť podľa potreby, aby sa zabezpečila konzistentnejšia používateľská skúsenosť vo veľkom rozsahu. V jeho najjednoduchšej forme je to zbierka príkladov výziev ako [tento od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), poskytujúca interaktívne komponenty výzvy (správy používateľa a systému) a formát požiadavky riadenej API – na podporu opätovného použitia.

V zložitejšej forme ako [tento príklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) obsahuje _zástupné symboly_, ktoré je možné nahradiť údajmi z rôznych zdrojov (vstup používateľa, systémový kontext, externé zdroje dát atď.), čím sa výzva generuje dynamicky. To nám umožňuje vytvoriť knižnicu opakovane použiteľných výziev, ktoré možno používateľsky programovo ovládať vo veľkom rozsahu.

Nakoniec, skutočná hodnota šablón spočíva v schopnosti vytvárať a publikovať _knižnice výziev_ pre vertikálne oblasti aplikácií – kde je šablóna výzvy optimalizovaná tak, aby odrážala kontext alebo príklady špecifické pre aplikácie, ktoré robia odpovede relevantnejšími a presnejšími pre cieľovú používateľskú skupinu. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je vynikajúcim príkladom tohto prístupu, zhromažďujúc knižnicu výziev pre oblasť vzdelávania so zameraním na kľúčové ciele ako plánovanie lekcií, návrh učebných osnov, doučovanie študentov atď.

## Podporný obsah

Ak uvažujeme o konštrukcii výzvy ako o inštrukcii (úlohe) a cieli (primárny obsah), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytneme, aby sme **nejako ovplyvnili výstup**. Môžu to byť ladené parametre, inštrukcie pre formátovanie, taxonómie tém atď., ktoré môžu pomôcť modelu _prispôsobiť_ odpoveď tak, aby vyhovovala požadovaným používateľským cieľom alebo očakávaniam.

Napríklad: Máme katalog kurzov s rozsiahlymi metaúdajmi (názov, popis, úroveň, značky metaúdajov, lektor atď.) o všetkých dostupných kurzoch v učebnom pláne:

- môžeme definovať inštrukciu „zhodnoť katalóg kurzov na jeseň 2023“
- môžeme použiť primárny obsah, aby sme poskytli niekoľko príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu 5 najdôležitejších „tagov“.

Teraz model môže poskytnúť zhrnutie v formáte ukázanom na niekoľkých príkladoch – ale ak výsledok obsahuje viacero tagov, môže uprednostniť 5 tagov identifikovaných v sekundárnom obsahu.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #1.
Posilnite koncept príkladmi a referenciami.

KONCEPT #3:
Techniky tvorby výziev.
Aké sú základné techniky tvorby výziev?
Ilustrujte to niekoľkými cvičeniami.
-->

## Najlepšie postupy pri tvorbe výziev

Keď už vieme, ako môžu byť výzvy _konštruované_, môžeme začať uvažovať, ako ich _navrhnúť_, aby odrážali najlepšie postupy. Môžeme to vnímať v dvoch častiach – mať správny _postoj_ a aplikovať správne _techniky_.

### Postoj pri tvorbe výziev

Tvorba výziev je proces metódou pokus-omyl, preto majte na pamäti tri široké vodidlá:

1. **Dôležité je porozumenie domény.** Presnosť a relevantnosť odpovedí závisí od _domeny_, v ktorej aplikácia alebo používateľ pôsobí. Uplatnite svoju intuíciu a odbornosť v danej doméne, aby ste **ďalej prispôsobili techniky**. Napríklad definujte _osobnosti špecifické pre doménu_ v systémových výzvach alebo použite _šablóny špecifické pre doménu_ v používateľských výzvach. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo použite _náznaky a príklady špecifické pre doménu_, aby ste model nasmerovali k známych vzorom použitia.

2. **Dôležité je porozumenie modelu.** Vieme, že modely sú stochastické povahy. Ale implementácie modelov sa môžu líšiť čo do použitého tréningového datasetu (predtrénované znalosti), schopností, ktoré poskytujú (napr. cez API alebo SDK) a typu obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné a slabé stránky modelu, ktorý používate, a použite tieto poznatky na _prioritizáciu úloh_ alebo na vytváranie _prispôsobených šablón_ optimalizovaných pre schopnosti modelu.

3. **Dôležitá je iterácia a validácia.** Modely sa rýchlo vyvíjajú, rovnako ako techniky tvorby výziev. Ako odborník na doménu možno máte ďalší kontext alebo kritériá pre _vašu_ špecifickú aplikáciu, ktoré nemusia platiť pre širšiu komunitu. Použite nástroje a techniky tvorby výziev na „rýchly štart“ konštrukcie výzvy, potom iterujte a validačné výsledky pomocou vlastnej intuície a odbornosti v doméne. Zaznamenávajte si svoje poznatky a vytvorte **znalostnú bázu** (napr. knižnice výziev), ktorá môže slúžiť ako nová východisková úroveň pre ostatných, pre rýchlejší vývoj v budúcnosti.

## Najlepšie postupy

Teraz sa pozrime na bežné najlepšie postupy, ktoré odporúčajú [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) odborníci.

| Čo                                | Prečo                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnocujte najnovšie modely.    | Nové generácie modelov pravdepodobne prinášajú vylepšené vlastnosti a kvalitu – ale môžu tiež znamenať vyššie náklady. Otestujte ich vplyv a potom urobte rozhodnutie o migrácii.                                                                  |
| Oddeľte inštrukcie a kontext      | Skontrolujte, či váš model alebo poskytovateľ definuje _oddeľovače_ na jasnejšie rozlíšenie inštrukcií, primárneho a sekundárneho obsahu. Pomáha to modelom presnejšie priraďovať váhy tokenom.                                                    |
| Buďte špecifickí a jasní          | Poskytnite viac detailov o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu aj konzistenciu odpovedí. Zachyťte recepty v opakovane použiteľných šablónach.                                                             |
| Buďte popisní, používajte príklady | Modely často lepšie reagujú na prístup „ukáž a povedz“. Začnite s `zero-shot` prístupom, kde dáte inštrukciu (bez príkladov), potom skúste `few-shot` na doladenie, pri ktorom pridávate niekoľko príkladov požadovaného výstupu. Používajte analógie.  |
| Používajte náznaky na naštartovanie doplnení | Nabádajte model k požadovanému výsledku tým, že mu dáte niekoľko úvodných slov alebo fráz, ktoré môže použiť ako východiskový bod pre odpoveď.                                                                                                      |
| Opakujte                          | Niekedy je potrebné sa modelu opakovať. Dajte inštrukcie pred a po primárnom obsahu, použite inštrukciu a náznak, atď. Iterujte a overujte, čo funguje najlepšie.                                                                               |
| Poradie je dôležité              | Poradie, v akom modelu prezentujete informácie, môže ovplyvniť výstup, aj v učebných príkladoch, vďaka efektu recencie. Vyskúšajte rôzne varianty, aby ste zistili, čo funguje najlepšie.                                                          |
| Dajte modelu možnosť „vypadnúť“   | Poskytnite modelu _náhradnú_ odpoveď pre prípad, že by nemohol úlohu dokončiť z akéhokoľvek dôvodu. Znižuje to pravdepodobnosť generovania nesprávnych alebo vymyslených odpovedí.                                                                |
|                                   |                                                                                                                                                                                                                                                  |

Ako pri každom najlepšom postupe, pamätajte, že _vaša skúsenosť sa môže líšiť_ podľa modelu, úlohy a domény. Použite ich ako východiskový bod a iterujte, aby ste zistili, čo vám najviac vyhovuje. Neustále prehodnocujte svoj proces tvorby výziev, keď sa objavia nové modely a nástroje, s dôrazom na škálovateľnosť procesu a kvalitu odpovedí.

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala obsahovať výzvu na kódovanie, ak je to vhodné.

VÝZVA:
Odkaz na Jupyter Notebook s iba komentármi v inštrukciách (sekcie kódu sú prázdne).

RIEŠENIE:
Odkaz na kópiu tohto Notebooku s vyplnenými a spustenými výzvami, ktorý ukazuje jeden príklad výstupu.
-->

## Zadanie

Gratulujeme! Dopracovali ste sa na koniec lekcie! Je čas vyskúšať niektoré z týchto konceptov a techník na reálnych príkladoch!

Pre naše zadanie použijeme Jupyter Notebook s cvičeniami, ktoré môžete interaktívne dopĺňať. Notebook si môžete tiež rozšíriť vlastným Markdownom a kódovými bunkami, aby ste si sami preskúmali nápady a techniky.

### Na začiatok, forkni repozitár, potom

- (Odporúčané) Spustite GitHub Codespaces
- (Alternatívne) Naklonujte repozitár do svojho lokálneho zariadenia a používajte ho cez Docker Desktop
- (Alternatívne) Otvorte Notebook v preferovanom runtime prostredí Notebooku.

### Potom nakonfigurujte svoje premenné prostredia

- Skopírujte súbor `.env.copy` v koreňovom adresári repozitára do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Potom sa vráťte do sekcie [Learning Sandbox](#výučbový-sandbox), aby ste sa dozvedeli viac.

### Nakoniec otvorte Jupyter Notebook

- Vyberte runtime jadro. Ak používate možnosť 1 alebo 2, jednoducho vyberte predvolené jadro Python 3.10.x, ktoré poskytuje vývojové prostredie kontajnera.

Ste pripravení spustiť cvičenia. Upozorňujeme, že tu neexistujú _správne a nesprávne_ odpovede – len skúmanie možností metódou pokus-omyl a budovanie intuície, čo funguje pre daný model a doménu aplikácie.

_Preto v tejto lekcii nie sú sekcie s riešeniami kódu. Namiesto toho bude Notebook obsahovať Markdown bunky s názvom „Moje riešenie:“, ktoré ukážu jeden príklad výstupu ako referenciu._

 <!--
ŠABLÓNA LEKCIE:
Zhrňte sekciu a poskytnite zdroje na samostatné učenie.
-->

## Overenie poznatkov

Ktorá z nasledujúcich výziev je dobrá a dodržiava rozumné najlepšie postupy?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného na útesu pri západe slnka
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

Odpoveď: 2, je to najlepšia výzva, pretože poskytuje podrobnosti o „čo“ a ide do špecifík (nie len akékoľvek auto, ale konkrétna značka a model) a tiež popisuje celkové prostredie. 3 je na druhom mieste, lebo tiež obsahuje veľa popisu.

## 🚀 Výzva

Skúste využiť „náznak“ techniku s výzvou: Dokonči vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Čo vám odpovie a ako by ste to zlepšili?

## Skvelá práca! Pokračujte vo svojom učení

Chcete sa dozvedieť viac o rôznych konceptoch tvorby výziev? Prejdite na [pokračovaciu stránku učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie výborné zdroje o tejto téme.

Prejdite do Lekcie 5, kde sa pozrieme na [pokročilé techniky tvorby výziev](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->