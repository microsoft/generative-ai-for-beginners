# Základy návrhu promptov

[![Základy návrhu promptov](../../../translated_images/sk/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrýva základné koncepty a techniky pre tvorbu efektívnych promptov v generatívnych AI modeloch. Spôsob, akým napíšete prompt pre LLM, tiež záleží. Starostlivo vytvorený prompt môže dosiahnuť lepšiu kvalitu odpovede. Ale čo presne znamenajú pojmy ako _prompt_ a _prompt engineering_? A ako zlepšiť _vstup_ promptu, ktorý posielam LLM? Na tieto otázky sa pokúsime odpovedať v tejto kapite a ďalšej.

_Generatívna AI_ je schopná vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) ako odpoveď na požiadavky používateľa. Dosahuje to pomocou _Veľkých jazykových modelov_ (Large Language Models), ako je séria GPT od OpenAI ("Generative Pre-trained Transformer"), ktoré sú trénované na prácu s prirodzeným jazykom a kódom.

Používatelia teraz môžu komunikovať s týmito modelmi pomocou známych spôsobov ako chat bez potreby technických znalostí alebo školenia. Modely sú _promptové_ - používatelia posielajú textový vstup (prompt) a dostávajú späť AI odpoveď (dokončenie). Následne môžu "chatovať s AI" opakovane v niekoľkonásobných výmenách, dolaďovať prompt, kým odpoveď nesplní ich očakávania.

"Prompty" sa tak stávajú primárnym _programovacím rozhraním_ pre generatívne AI aplikácie, ktoré modelom hovoria, čo majú robiť a ovplyvňujú kvalitu vrátených odpovedí. "Prompt Engineering" je rýchlo rastúca oblasť štúdia, ktorá sa zameriava na _navrhovanie a optimalizáciu_ promptov pre dosiahnutie konzistentných a kvalitných odpovedí vo veľkom rozsahu.

## Ciele učenia

V tejto lekcii sa naučíme, čo je Prompt Engineering, prečo je dôležitý a ako môžeme vytvárať efektívnejšie prompty pre daný model a cieľ aplikácie. Pochopíme základné koncepty a osvedčené postupy pri návrhu promptov - a zoznámime sa s interaktívnym prostredím Jupyter Notebooks "pieskovisko", kde môžeme vidieť tieto koncepty na reálnych príkladoch.

Na konci lekcie budeme schopní:

1. Vysvetliť, čo je prompt engineering a prečo je dôležitý.
2. Opísať jednotlivé komponenty promptu a ich použitie.
3. Naučiť sa najlepšie praktiky a techniky pre prompt engineering.
4. Použiť naučené techniky na reálne príklady pomocou OpenAI endpointu.

## Kľúčové pojmy

Prompt Engineering: Prax navrhovania a doladenia vstupov na usmernenie AI modelov k produkcii požadovaných výstupov.
Tokenizácia: Proces prevedenia textu na menšie jednotky, nazývané tokeny, ktoré model dokáže spracovať a pochopiť.
Instruction-Tuned LLMs: Veľké jazykové modely (LLM), ktoré boli doladené na základe špecifických inštrukcií pre zlepšenie presnosti a relevantnosti odpovedí.

## Sandbox na učenie sa

Prompt engineering je v súčasnosti viac umením ako vedou. Najlepší spôsob, ako zlepšiť našu intuíciu, je _viac praxe_ a adopcia prístupu pokus-omyl, ktorý kombinuje odborné znalosti z oblasti aplikácií s odporúčanými technikami a modelovo-špecifickými optimalizáciami.

K tomuto kurzu patrí Jupyter Notebook, ktorý poskytuje _pieskoviskové_ prostredie, kde môžete skúšať to, čo sa naučíte - priebežne alebo ako súčasť kódovej výzvy na konci. Na spustenie cvičení budete potrebovať:

1. **Kľúč API Azure OpenAI** - služobný endpoint pre nasadený LLM.
2. **Python Runtime** - v ktorom sa notebook spustí.
3. **Lokálne premenné prostredia** - _dokončite teraz kroky v [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), aby ste boli pripravení_.

Notebook obsahuje _štartovacie_ cvičenia - no odporúča sa pridávať vlastné sekcie s _Markdown_ (popisom) a _Kódom_ (prompt požiadavky) na skúšanie ďalších príkladov alebo nápadov a budovanie intuície pre návrh promptov.

## Ilustrovaný sprievodca

Chcete získať celkový prehľad o tom, čo táto lekcia pokrýva skôr, než sa pustíte do detailov? Pozrite si tento ilustrovaný sprievodca, ktorý vám poskytne prehľad hlavných tém a kľúčových bodov na zamyslenie pre každú. Plán lekcie vás prevedie od pochopenia základných konceptov a výziev až po riešenie pomocou relevantných techník a osvedčených postupov prompt engineeringu. Upozorňujeme, že časť "Pokročilé techniky" v tomto sprievodcovi odkazuje na obsah pokrytý v _nasledujúcej_ kapitole tohto kurikula.

![Ilustrovaný sprievodca návrhom promptov](../../../translated_images/sk/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Naša startupová misia

Teraz si povedzme, ako sa _táto téma_ týka našej startupovej misie prinášať [inovácie AI do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať AI-poháňané aplikácie pre _personalizované učenie_ - premýšľajme teda o tom, ako môžu rôzni používatelia našej aplikácie "navrhovať" prompty:

- **Administrátori** môžu požiadať AI o _analýzu dát učebných osnov s cieľom identifikovať medzery v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať s kódom.
- **Učitelia** môžu požiadať AI, aby _generovala plán hodiny pre cieľové publikum a tému_. AI môže zostaviť personalizovaný plán v zadanom formáte.
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI môže teraz viesť študentov prostredníctvom lekcií, nápovedy a príkladov prispôsobených ich úrovni.

To je len špička ľadovca. Pozrite sa na [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - open-source knižnicu promptov zostavenú odborníkmi na vzdelávanie - pre širší prehľad možností! _Vyskúšajte spustiť niektoré z týchto promptov v pieskovisku alebo v OpenAI Playground, aby ste videli výsledky!_

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept č. 1.
Konzistentne posilnite koncept príkladmi a odkazmi.

KONCEPT č. 1:
Prompt Engineering.
Definujte a vysvetlite, prečo je potrebný.
-->

## Čo je Prompt Engineering?

Lekciu sme začali definíciou **Prompt Engineering** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov), aby priniesli konzistentné a kvalitné odpovede (dokončenia) pre daný cieľ aplikácie a modelu. Môžeme to vnímať ako dvojstupňový proces:

- _navrhnúť_ počiatočný prompt pre daný model a cieľ
- _dolaďovať_ prompt iteratívne pre zlepšenie kvality odpovede

Ide o skúšobný proces, ktorý si vyžaduje užívateľskú intuíciu a úsilie na dosiahnutie optimálnych výsledkov. Prečo je to teda dôležité? Najprv musíme pochopiť tri koncepty:

- _Tokenizácia_ = ako model "vidí" prompt
- _Základné LLM_ = ako základný model spracováva prompt
- _Instruction-Tuned LLMs_ = ako model teraz chápe "úlohy"

### Tokenizácia

LLM vidí prompt ako _sekvenciu tokenov_, kde rôzne modely (alebo verzie modelu) môžu rovnaký prompt tokenizovať rôznymi spôsobmi. Keďže LLM sú trénované na tokenoch (a nie na surovom texte), spôsob tokenizácie promptov priamo ovplyvňuje kvalitu generovanej odpovede.

Na získanie intuície o tokenizácii skúste nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), viditeľný nižšie. Skopírujte svoj prompt a pozrite sa, ako je konvertovaný na tokeny, venujte pozornosť, ako sa spracovávajú medzery a interpunkčné znamienka. Tento príklad ukazuje starší model LLM (GPT-3) - pokus s novším modelom môže priniesť iný výsledok.

![Tokenizácia](../../../translated_images/sk/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncept: Základné modely (Foundation Models)

Po tokenizácii promptu je primárnou úlohou ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo základného modelu) predpovedať ďalší token v sekvencii. Pretože LLM sú trénované na obrovských dátových množinách textu, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a môžu túto predpoveď urobiť s istotou. Nechápu však _význam_ slov v texte alebo tokenoch; vidia len vzor, ktorý môžu "dopĺňať" ďalšou predpoveďou. Pokračujú v predpovedaní sekvencie, kým nie sú zastavení zásahom používateľa alebo nejakou prednastavenou podmienkou.

Chcete vidieť, ako funguje dopĺňanie na základe promptu? Zadajte vyššie uvedený prompt do [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) s predvolenými nastaveniami. Systém má nastavenie tak, aby prijímal prompty ako požiadavky na informácie - takže by ste mali vidieť doplnenie uspokojujúce tento kontext.

Ale čo ak chce používateľ vidieť niečo konkrétne, čo spĺňa nejaké kritériá alebo cieľ úlohy? Tu prichádzajú do hry _Instruction-Tuned_ LLM.

![Dopĺňanie chat s Base LLM](../../../translated_images/sk/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncept: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) vychádza zo základného modelu a doladí ho na základe príkladov alebo párov vstup/výstup (napr. viackolové "správy"), ktoré môžu obsahovať jasné inštrukcie - a AI sa snaží na túto inštrukciu reagovať.

Používa techniky ako Reinforcement Learning s ľudskou spätnou väzbou (RLHF), ktoré model naučia _dodržiavať pokyny_ a _učiť sa zo spätnej väzby_, aby produkoval odpovede lepšie prispôsobené praktickým aplikáciám a viac relevantné pre používateľské ciele.

Skúsme to - vráťte sa k vyššie uvedenému promptu, ale teraz zmeňte _systémovú správu_ tak, aby kontext zahŕňal nasledujúcu inštrukciu:

> _Zhrňte poskytnutý obsah pre druháka základnej školy. Výsledok nech je v jednom odstavci s 3-5 odrážkami._

Vidíte, že výsledok je teraz nastavený na požadovaný cieľ a formát? Učiteľ môže túto odpoveď priamo použiť na svojich prezentáciách pre hodinu.

![Dopĺňanie chat s Instruction Tuned LLM](../../../translated_images/sk/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Prečo potrebujeme Prompt Engineering?

Teraz, keď vieme, ako modely spracovávajú prompty, poďme sa pozrieť na _dôvod_, prečo potrebujeme prompt engineering. Odpoveď spočíva v tom, že súčasné LLM predstavujú niekoľko výziev, ktoré robia _spoľahlivé a konzistentné dokončenia_ náročnejšie, ak sa nevenujeme starostlivému návrhu a optimalizácii promptu. Napríklad:

1. **Odpovede modelu sú náhodné.** _Rovnaký prompt_ môže pravdepodobne generovať rozdielne odpovede v rôznych modeloch alebo verziách modelov. Môže dokonca produkovať rozdielne výsledky s _tým istým modelom_ v rôznych časoch. _Techniky prompt engineeringu nám pomáhajú minimalizovať tieto variácie zabezpečením lepších ochranných mechanizmov_.

1. **Modely môžu vyrábať nepravdivé odpovede.** Modely sú predtrénované na _veľkých ale konečných_ dátových množinách, takže nemajú znalosti o konceptoch mimo rozsah ich školenia. Výsledkom môžu byť odpovede, ktoré sú nepresné, vymyslené alebo priamo protichodné známym faktom. _Techniky prompt engineeringu pomáhajú používateľom tieto fabricácie identifikovať a zmierniť napríklad tým, že žiadajú AI o citácie alebo zdôvodnenie_.

1. **Schopnosti modelov sa líšia.** Novšie modely alebo generácie modelov majú bohatšie schopnosti, ale prinášajú aj unikátne zvláštnosti a kompromisy v nákladoch a zložitosti. _Prompt engineering môže pomôcť vyvinúť najlepšie postupy a workflow, ktoré abstraktne odstraňujú rozdiely a prispôsobujú sa modelovo-špecifickým požiadavkám škálovateľným a plynulým spôsobom_.

Poďme si to ukázať v praxi v OpenAI alebo Azure OpenAI Playground:

- Použite rovnaký prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) - videli ste rozdiely?
- Použite rovnaký prompt opakovane s _tým istým_ nasadením LLM (napr. Azure OpenAI playground) - ako sú tieto rozdiely rôzne?

### Príklad fabricácií

V tomto kurze používame pojem **"fabricácia"** na označenie javu, keď LLM niekedy generujú fakticky nesprávne informácie kvôli obmedzeniam ich školenia alebo iným faktorom. Možno ste tiež počuli výraz _"halucinácie"_ v populárnych článkoch alebo vedeckých prácach. Avšak dôrazne odporúčame používať pojem _"fabricácia"_, aby sme náhodou neosobnili správanie modelu tým, že by sme mu prisudzovali ľudskú vlastnosť. To tiež podporuje [zásady zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hľadiska terminológie, odstránením termínov, ktoré môžu byť v niektorých kontextoch považované za nevhodné alebo neinkluzívne.

Chcete si predstaviť, ako fabricácie fungujú? Premýšľajte o promte, ktorý požiada AI, aby generovala obsah o neexistujúcej téme (aby sa zabezpečilo, že sa v dátovej sade školenia nenachádza). Napríklad - vyskúšal som tento prompt:

> **Prompt:** vygeneruj plán hodiny o Marťanskej vojne v roku 2076.

Vyhľadávanie na webe mi ukázalo, že existujú fiktívne príbehy (napr. televízne seriály alebo knihy) o Marťanských vojnách - ale žiadne o roku 2076. Spoločný rozum nám tiež hovorí, že rok 2076 je _v budúcnosti_ a teda nemôže byť spojený so skutočnou udalosťou.


Čo sa teda stane, keď spustíme tento prompt u rôznych poskytovateľov LLM?

> **Odpoveď 1**: OpenAI Playground (GPT-35)

![Odpoveď 1](../../../translated_images/sk/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpoveď 2**: Azure OpenAI Playground (GPT-35)

![Odpoveď 2](../../../translated_images/sk/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpoveď 3**: : Hugging Face Chat Playground (LLama-2)

![Odpoveď 3](../../../translated_images/sk/04-fabrication-huggingchat.faf82a0a51278956.webp)

Ako sa očakávalo, každý model (alebo verzia modelu) produkuje mierne odlišné odpovede vďaka stochastickému správaniu a variáciám schopností modelu. Napríklad jeden model cieli na publikom 8. triedy, zatiaľ čo druhý predpokladá študenta strednej školy. Ale všetky tri modely vygenerovali odpovede, ktoré by mohli presvedčiť neinformovaného používateľa, že udalosť je skutočná.

Techniky návrhu promptov ako _metaprompting_ a _nastavenie teploty_ môžu do istej miery znížiť vymyslené informácie modelom. Nové architektúry promptov taktiež bezproblémovo integrujú nové nástroje a techniky do priebehu promptu, aby zmiernili alebo znížili niektoré z týchto efektov.

## Prípadová štúdia: GitHub Copilot

Ukončime túto sekciu tým, že sa pozrieme, ako sa návrh promptov využíva v reálnych riešeniach na príklade jednej prípadovej štúdie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš "AI programovací parťák" - prevádza textové prompty na dokončenia kódu a je integrovaný do vývojového prostredia (napr. Visual Studio Code) pre plynulý používateľský zážitok. Ako je zdokumentované v sérii blogov nižšie, najskoršia verzia bola založená na modeli OpenAI Codex - inžinieri však rýchlo pochopili potrebu doladiť model a vyvinúť lepšie techniky návrhu promptov, aby zlepšili kvalitu kódu. V júli predstavili [vylepšený AI model, ktorý presahuje Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pre ešte rýchlejšie návrhy.

Prečítajte si príspevky v poradí, aby ste sledovali ich učenie.

- **Máj 2023** | [GitHub Copilot sa lepšie učí rozumieť vášmu kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Máj 2023** | [Vnútri GitHub: Práca s LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jún 2023** | [Ako písať lepšie prompty pre GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Júl 2023** | [.. GitHub Copilot presahuje Codex s vylepšeným AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Júl 2023** | [Sprievodca vývojára návrhom promptov a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Ako postaviť enterprise LLM aplikáciu: Lekcie z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Môžete si tiež prezrieť ich [Inžiniersky blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pre ďalšie články ako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ktorý ukazuje, ako sa tieto modely a techniky _aplikujú_ na poháňanie reálnych aplikácií.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokryť jadrový koncept #2.
Posilniť koncept príkladmi a odkazmi.

KONCEPT #2:
Návrh promptu.
Ilustrované príkladmi.
-->

## Konštrukcia promptu

Videli sme, prečo je návrh promptov dôležitý - teraz pochopme, ako sa prompty _konštruujú_, aby sme mohli vyhodnotiť rôzne techniky pre efektívnejší návrh promptov.

### Základný prompt

Začnime so základným promptom: textovým vstupom zaslaným modelu bez ďalšieho kontextu. Tu je príklad - keď pošleme prvé slová národnej hymny USA do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), model okamžite _dokončí_ odpoveď ďalšími riadkami, čo ilustruje základné predikčné správanie.

| Prompt (Vstup)     | Dokončenie (Výstup)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Znie to, akoby ste začínali so slovami piesne "The Star-Spangled Banner," národnej hymny Spojených štátov. Celý text je ...              |

### Zložitý prompt

Teraz pridajme kontext a inštrukcie k základnému promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje konštruovať zložité prompty ako zbierku _správ_ obsahujúcich:

- Pár vstup/výstup odrážajúcich _vstup používateľa_ a _odpoveď asistenta_.
- Systémovú správu nastavujúcu kontext pre správanie alebo osobnosť asistenta.

Žiadosť má teraz formu nižšie, kde _tokenizácia_ efektívne zachytáva relevantné informácie z kontextu a konverzácie. Zmena systémového kontextu môže mať rovnaký dopad na kvalitu dokončení ako vstupy používateľa.

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

### Inštrukčný prompt

V predchádzajúcich príkladoch bol prompt jednoduchý textový dopyt, ktorý sa dá interpretovať ako žiadosť o informáciu. Pri _inštrukčných_ promptoch môžeme tento text použiť na konkrétnejšie špecifikovanie úlohy, čím AI poskytujeme lepšie usmernenia. Tu je príklad:

| Prompt (Vstup)                                                                                                                                                                                                                         | Dokončenie (Výstup)                                                                                                        | Typ inštrukcie    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napíš opis Občianskej vojny                                                                                                                                                                                                           | _vrátil jednoduchý odsek_                                                                                                  | Jednoduchý         |
| Napíš opis Občianskej vojny. Uveď kľúčové dátumy a udalosti a popíš ich význam                                                                                                                                                        | _vrátil odsek nasledovaný zoznamom kľúčových dátumov a popisov udalostí_                                                   | Zložitý            |
| Napíš opis Občianskej vojny v 1 odseku. Uveď 3 bodové body s kľúčovými dátumami a ich významom. Uveď ďalšie 3 bodové body s dôležitými historickými osobnosťami a ich príspevkami. Výstup vráť ako JSON súbor                             | _vracia podrobnejšie informácie v textovom okne formátované ako JSON, ktoré je možné skopírovať do súboru a podľa potreby overiť_ | Zložitý. Formátovaný. |

## Primárny obsah

V predchádzajúcich príkladoch bol prompt stále pomerne otvorený, čo modelu umožňovalo rozhodnúť, ktorá časť jeho predtrénovaného datasetu je relevantná. Pri návrhovom vzore _primárny obsah_ je vstupný text rozdelený na dve časti:

- inštrukciu (akciu)
- relevantný obsah (ktorý ovplyvňuje akciu)

Tu je príklad, kde inštrukcia je "zhrň toto v 2 vetách".

| Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončenie (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynného obra s hmotnosťou tisícinu hmotnosti Slnka, ale dvojnásobnou a pol hmotnosťou všetkých ostatných planét Slnečnej sústavy dohromady. Jupiter je jedným z najsvetlejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. Je pomenovaný podľa rímskeho boha Jupitera.[19] Keď ho pozorujeme zo Zeme, Jupiter môže byť dosť jasný na to, že jeho odrazené svetlo vrhá viditeľné tiene,[20] a je v priemere tretím najsvetlejším prírodným objektom na nočnej oblohe po Mesiaci a Venuši. <br/> **Zhrň toto v 2 krátkych vetách** | Jupiter, piata planéta od Slnka, je najväčšia v Slnečnej sústave a je známy tým, že je jedným z najsvetlejších objektov na nočnej oblohe. Pomenovaný po rímskom bohovi Jupiterovi, je to plynný obor, ktorého hmotnosť je dvojnásobná a pol hmotnosti všetkých ostatných planét Slnečnej sústavy dohromady. |

Segment primárneho obsahu možno použiť rôznymi spôsobmi na efektívnejšie inštrukcie:

- **Príklady** - namiesto explicitnej inštrukcie povedať modelu, čo má robiť, dajte mu príklady, čo má robiť, a nechajte ho odvodiť vzor.
- **Náznaky** - nasledujte inštrukciu „náznakom“, ktorý navádza dokončenie a usmerňuje model k relevantnejším odpovediam.
- **Šablóny** - sú to opakovateľné „recepty“ promptov s zástupnými znakmi (premennými), ktoré možno prispôsobiť údajmi pre konkrétne použitia.

Poďme si ich ukázať v praxi.

### Použitie príkladov

Toto je prístup, kde používate primárny obsah na „nakŕmenie modelu“ príkladmi žiadaného výstupu pre danú inštrukciu a necháte ho odvodiť vzor žiadaného výstupu. Na základe počtu poskytnutých príkladov môžeme mať zero-shot prompting, one-shot prompting, few-shot prompting atď.

Prompt teraz pozostáva z troch častí:

- Popis úlohy
- Niekoľko príkladov žiadaného výstupu
- Začiatok nového príkladu (čo sa stáva implicitným popisom úlohy)

| Typ učenia | Prompt (Vstup)                                                                                                                                        | Dokončenie (Výstup)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Prelož do španielčiny                                                                                                         | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Hráč bežal po bodoch => Baseball <br/> Hráč zasiahol eso => Tenis <br/> Hráč zasiahol šesťku => Kriket <br/> Hráč urobil smeč =>                     | Basketbal                  |
|               |                                                                                                                                                       |                             |

Všimnite si, ako sme museli poskytnúť explicitnú inštrukciu ("Prelož do španielčiny") pri zero-shot promptingu, ale tá sa odvádza v príklade one-shot promptingu. Príklad few-shot ukazuje, ako pridanie viacerých príkladov umožňuje modelom robiť presnejšie dedukcie bez ďalších inštrukcií.

### Náznaky promptu

Ďalšou technikou použitia primárneho obsahu je poskytnutie _náznakov_ namiesto príkladov. V tomto prípade dávame modelu jemný podnet správnym smerom tým, že ho _začíname_ úryvkom, ktorý odráža žiadaný formát odpovede. Model potom „berie náznak“ a pokračuje v tomto smere.

| Počet náznakov | Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončenie (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynného obra s hmotnosťou tisícinu hmotnosti Slnka, ale dvojnásobnou a pol hmotnosťou všetkých ostatných planét Slnečnej sústavy dohromady. Jupiter je jedným z najsvetlejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrň toto**                                       | Jupiter je najväčšia planéta v našej Slnečnej sústave a piata od Slnka. Je to plynného obra s hmotnosťou 1/1000 hmotnosti Slnka, ale ťažší než všetky ostatné planéty dohromady. Staroveké civilizácie poznali Jupitera už dávno a je ľahko viditeľný na nočnej oblohe. |
| 1              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynného obra s hmotnosťou tisícinu hmotnosti Slnka, ale dvojnásobnou a pol hmotnosťou všetkých ostatných planét Slnečnej sústavy dohromady. Jupiter je jedným z najsvetlejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrň toto** <br/> Čo sme sa dozvedeli, je, že Jupiter | je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynného obra s hmotnosťou tisícinu hmotnosti Slnka, ale dvojnásobnou a pol hmotnosťou všetkých ostatných planét dohromady. Je ľahko viditeľný voľným okom a je známy už od staroveku.                           |

| 2              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou jedna tisícina hmotnosti Slnka, ale dvojnásobnou a pol hmotnosti všetkých ostatných planét Slnečnej sústavy spolu. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrnutie** <br/> Top 3 fakty, ktoré sme sa naučili:         | 1. Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. <br/> 2. Je to plynný obor s hmotnosťou jedna tisícina hmotnosti Slnka...<br/> 3. Jupiter je viditeľný voľným okom od staroveku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablóny výziev

Šablóna výzvy je _preddefinovaný recept na výzvu_, ktorý môže byť uložený a znovu použitý podľa potreby na zabezpečenie konzistentnejších používateľských skúseností vo veľkom rozsahu. V jeho najjednoduchšej forme je to jednoducho zbierka príkladov výziev ako [tento od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), ktorý poskytuje interaktívne komponenty výzvy (správy používateľa a systému) aj formát požiadavky ovládanej API - na podporu opätovného použitia.

V zložitejšej forme, ako [tento príklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), obsahuje _zástupné symboly_, ktoré môžu byť nahradené údajmi z rôznych zdrojov (vstup používateľa, kontext systému, externé dátové zdroje atď.), aby sa výzva generovala dynamicky. To nám umožňuje vytvoriť knižnicu znovupoužiteľných výziev, ktoré môžu programovo riadiť konzistentné používateľské skúsenosti vo veľkom rozsahu.

Skutočná hodnota šablón však spočíva v možnosti vytvárať a publikovať _knižnice výziev_ pre vertikálne aplikačné domény - kde je šablóna výzvy _optimalizovaná_ tak, aby odrážala kontext aplikácie alebo príklady, ktoré robia odpovede relevantnejšie a presnejšie pre cieľové užívateľské publikum. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, ktorý kurátorsky zhromažďuje knižnicu výziev pre vzdelávaciu oblasť so zameraním na kľúčové ciele, ako je plánovanie lekcií, návrh kurikula, doučovanie študentov a pod.

## Podporný obsah

Ak o konštrukcii výzvy uvažujeme ako o inštrukcii (úlohe) a cieľovom obsahu (primárnom obsahu), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytujeme na **ovplyvnenie výstupu nejakým spôsobom**. Môžu to byť ladieace parametre, pokyny na formátovanie, kategórie tém a pod., ktoré môžu pomôcť modelu _prispôsobiť_ svoju odpoveď tak, aby vyhovovala požadovaným používateľským cieľom alebo očakávaniam.

Napríklad: Ak máme katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, metadátové značky, lektor atď.) o všetkých dostupných kurzoch v učebnom pláne:

- môžeme definovať inštrukciu "zhrnúť katalóg kurzov na jeseň 2023"
- môžeme použiť primárny obsah na poskytnutie niekoľkých príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu top 5 "štítkov" záujmu.

Teraz môže model poskytnúť zhrnutie vo formáte podľa zopár príkladov - ale ak výsledok má viacero štítkov, môže uprednostniť 5 štítkov určených v sekundárnom obsahu.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokryť základný koncept č.1.
Posilnite koncept príkladmi a odkazmi.

KONCEPT č.3:
Techniky promptového inžinierstva.
Aké sú niektoré základné techniky promptového inžinierstva?
Ilustrujte to niekoľkými cvičeniami.
-->

## Najlepšie praktiky promptovania

Teraz, keď vieme, ako možno výzvy _konštruovať_, môžeme začať premýšľať, ako ich _navrhovať_, aby odrážali najlepšie praktiky. Môžeme to uvažovať v dvoch častiach - mať správny _postoj_ a aplikovať správne _techniky_.

### Postoj k promptovému inžinierstvu

Promptové inžinierstvo je proces metódy pokusu a omylu, takže majte na pamäti tri hlavné vodítka:

1. **Znalosť domény je dôležitá.** Presnosť a relevantnosť odpovede závisí od _domeny_, v ktorej aplikácia alebo používateľ pôsobí. Aplikujte svoju intuíciu a odborné znalosti domény na ďalšie **prispôsobenie techník**. Napríklad definujte _doménovo špecifické osobnosti_ vo svojich systémových výzvach alebo použite _doménovo špecifické šablóny_ v používateľských výzvach. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo použite _doménovo špecifické náznaky a príklady_ na nasmerovanie modelu k známym vzorom použitia.

2. **Znalosť modelu je dôležitá.** Vieme, že modely sú z povahy stochastické. Ale implementácie modelov sa môžu líšiť v závislosti od použitého tréningového datasetu (predtrénované znalosti), schopností, ktoré poskytujú (napr. cez API alebo SDK) a typu obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné stránky a obmedzenia modelu, ktorý používate, a využite tieto vedomosti na _prioritizáciu úloh_ alebo vytváranie _prispôsobených šablón_ optimalizovaných pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako aj techniky promptového inžinierstva. Ako odborník na doménu môžete mať ďalší kontext alebo kritériá špecifické pre _vašu_ aplikáciu, ktoré nemusia platiť pre širšiu komunitu. Používajte nástroje a techniky promptového inžinierstva na "rýchly štart" konštrukcie výzvy, potom iterujte a validujte výsledky pomocou vlastnej intuície a odborných znalostí. Zaznamenávajte svoje poznatky a vytvárajte **znalostnú databázu** (napr. knižnice výziev), ktorú môžu ostatní použiť ako nový základ pre rýchlejšie iterácie v budúcnosti.

## Najlepšie praktiky

Teraz sa pozrieme na bežné najlepšie praktiky odporúčané [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) odborníkmi.

| Čo                               | Prečo                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnocujte najnovšie modely.  | Nové generácie modelov pravdepodobne ponúkajú zlepšené funkcie a kvalitu - ale môžu tiež priniesť vyššie náklady. Vyhodnoťte ich podľa dopadu a potom sa rozhodnite o migrácii.                                                                        |
| Oddelte inštrukcie a kontext     | Skontrolujte, či váš model/poskytovateľ definuje _oddeľovače_ na jasnejšie rozlíšenie inštrukcií, primárneho a sekundárneho obsahu. To môže modelom pomôcť presnejšie prideľovať váhy tokenom.                                                         |
| Buďte konkrétni a jasní           | Poskytnite viac detailov o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu i konzistentnosť odpovedí. Zachyťte recepty v znovupoužiteľných šablónach.                                                                     |
| Buďte popisní, používajte príklady | Modely môžu lepšie reagovať na prístup "ukáž a povedz". Začnite s `zero-shot` prístupom, kde dávate inštrukciu (bez príkladov) a potom skúste `few-shot` ako vylepšenie, poskytujúc niekoľko príkladov požadovaného výstupu. Používajte analógie.           |
| Používajte náznaky na naštartovanie dokončení | Postrčte model k želanému výsledku tým, že mu dáte niekoľko úvodných slov alebo fráz, ktoré môže použiť ako východiskový bod pre odpoveď.                                                                                                             |
| Zdvojte úsilie                  | Niekedy môže byť potrebné model opakovať. Dajte inštrukcie pred a po primárnom obsahu, používajte inštrukciu aj náznak, atď. Iterujte a validujte, aby ste videli, čo funguje.                                                                         |
| Poradie je dôležité             | Poradie, v akom prezentujete informácie modelu, môže ovplyvniť výstup, dokonca aj v príkladoch učenia, vďaka tendencii uprednostňovať novšie informácie. Skúšajte rôzne možnosti, aby ste zistili, čo najlepšie funguje.                                   |
| Dajte modelu "výstupnú bránu"    | Dajte modelu odpoveď _náhradného dokončenia_, ktorú môže poskytnúť, ak nemôže úlohu z nejakého dôvodu dokončiť. To môže znížiť riziko generovania nepravdivých alebo vymyslených odpovedí.                                                             |
|                                   |                                                                                                                                                                                                                                                   |

Ako pri každej najlepšej praxi, nezabudnite, že _váš výsledek sa môže líšiť_ v závislosti od modelu, úlohy a domény. Používajte ich ako východiskový bod a iterujte, kým nenájdete, čo najlepšie funguje pre vás. Neustále prehodnocujte svoj proces promptového inžinierstva, keď sa objavia nové modely a nástroje, so zameraním na škálovateľnosť procesu a kvalitu odpovedí.

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala obsahovať programátorskú výzvu, ak je to vhodné

VÝZVA:
Odkaz na Jupyter Notebook, kde sú v inštrukciách iba komentáre ku kódu (sekcie kódu sú prázdne).

RIEŠENIE:
Odkaz na kópiu tohto Noteboku s vyplnenými výzvami a spusteným kódom, ktorý ukazuje jeden príklad riešenia.
-->

## Zadanie

Blahoželáme! Dopracovali ste sa na koniec lekcie! Je čas otestovať niektoré z týchto konceptov a techník na skutočných príkladoch!

Pre naše zadanie použijeme Jupyter Notebook s cvičeniami, ktoré môžete interaktívne dokončiť. Notebook si môžete tiež rozšíriť o vlastné Markdown a kódové bunky, aby ste skúmali nápady a techniky samostatne.

### Na začiatok, vytvorte si fork repozitára, potom

- (Odporúčané) Spustite GitHub Codespaces
- (Alternatívne) Naklonujte repozitár do lokálneho zariadenia a používajte ho s Docker Desktop
- (Alternatívne) Otvorte Notebook vo vašom preferovanom prostredí pre Notebooky.

### Ďalej nakonfigurujte svoje environmentálne premenné

- Skopírujte súbor `.env.copy` v koreňovom priečinku repozitára do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Potom sa vráťte do sekcie [Learning Sandbox](#sandbox-na-učenie-sa), kde sa naučíte ako na to.

### Ďalej otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x, ktorý poskytuje vývojárske prostredie.

Ste pripravení spustiť cvičenia. Upozorňujeme, že tu neexistujú _správne alebo nesprávne_ odpovede - len skúmanie možností metódou pokusu a omylu a budovanie intuície o tom, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú segmenty s riešeniami kódu. Namiesto toho bude Notebook obsahovať markdown bunky s názvom "Moje riešenie:", ktoré ukážu jeden príkladový výstup ako referenciu._

 <!--
ŠABLÓNA LEKCIE:
Zabaľte sekciu s kontrolou poznatkov a zdrojmi pre samoštúdium.
-->

## Kontrola poznatkov

Ktorý z nasledujúcich príkladov je dobrá výzva, ktorá nasleduje rozumné najlepšie praktiky?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného pri útesu pri západe slnka
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

Odpoveď: 2, je to najlepšia výzva, pretože poskytuje detaily o "čo" a ide do špecifík (nie len akékoľvek auto, ale konkrétnu značku a model) a tiež popisuje celkové prostredie. 3 je ďalšia najlepšia, pretože obsahuje veľa popisov.

## 🚀 Výzva

Skúste využiť techniku "náznaku" s výzvou: Dokončete vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Čo vám model odpovie a ako by ste to vylepšili?

## Skvelá práca! Pokračujte v učení

Chcete sa naučiť viac o rôznych konceptoch promptového inžinierstva? Prejdite na [pokračovaciu stránku učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje na túto tému.

Presuňte sa na Lekciu 5, kde sa pozrieme na [pokročilé techniky promptovania](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->