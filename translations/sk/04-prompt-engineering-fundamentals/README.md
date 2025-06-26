<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:24:38+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sk"
}
-->
# Základy návrhu promptov

## Úvod

Tento modul pokrýva základné koncepty a techniky na vytváranie efektívnych promptov v generatívnych AI modeloch. Spôsob, akým píšete svoj prompt pre LLM, tiež záleží. Dôkladne vytvorený prompt môže dosiahnuť lepšiu kvalitu odpovede. Ale čo presne znamenajú pojmy ako _prompt_ a _návrh promptov_? A ako zlepšiť vstupný prompt, ktorý posielam LLM? Toto sú otázky, na ktoré sa pokúsime odpovedať v tejto a nasledujúcej kapitole.

_Generatívna AI_ je schopná vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) ako odpoveď na požiadavky používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ ako séria GPT ("Generative Pre-trained Transformer") od OpenAI, ktoré sú trénované na používanie prirodzeného jazyka a kódu.

Používatelia môžu teraz interagovať s týmito modelmi pomocou známych paradigiem ako chat, bez potreby technickej odbornosti alebo školenia. Modely sú _založené na promtoch_ - používatelia posielajú textový vstup (prompt) a dostávajú späť odpoveď AI (dokončenie). Potom môžu "chatovať s AI" iteratívne, v mnohých kolách rozhovorov, vylepšujúc svoj prompt, kým odpoveď nezodpovedá ich očakávaniam.

"Prompty" sa teraz stávajú primárnym _programovacím rozhraním_ pre generatívne AI aplikácie, ktoré hovoria modelom, čo majú robiť a ovplyvňujú kvalitu vrátených odpovedí. "Návrh promptov" je rýchlo rastúca oblasť štúdia, ktorá sa zameriava na _návrh a optimalizáciu_ promptov na dosiahnutie konzistentných a kvalitných odpovedí v širokom meradle.

## Ciele učenia

V tejto lekcii sa dozvieme, čo je návrh promptov, prečo je dôležitý a ako môžeme vytvoriť efektívnejšie prompty pre daný model a cieľ aplikácie. Pochopíme základné koncepty a najlepšie postupy pre návrh promptov - a dozvieme sa o interaktívnom prostredí Jupyter Notebooks "sandbox", kde môžeme tieto koncepty aplikovať na skutočné príklady.

Na konci tejto lekcie budeme schopní:

1. Vysvetliť, čo je návrh promptov a prečo je dôležitý.
2. Opísať komponenty promptu a ako sa používajú.
3. Naučiť sa najlepšie postupy a techniky pre návrh promptov.
4. Aplikovať naučené techniky na skutočné príklady pomocou OpenAI endpointu.

## Kľúčové pojmy

Návrh promptov: Prax navrhovania a dolaďovania vstupov na usmernenie AI modelov k produkcii požadovaných výstupov.  
Tokenizácia: Proces konverzie textu na menšie jednotky, nazývané tokeny, ktoré model dokáže pochopiť a spracovať.  
LLM vyladené inštrukciami: Veľké jazykové modely (LLM), ktoré boli vyladené s konkrétnymi inštrukciami na zlepšenie presnosti a relevantnosti ich odpovedí.

## Učebný sandbox

Návrh promptov je momentálne viac umenie než veda. Najlepší spôsob, ako zlepšiť našu intuíciu, je _viac cvičiť_ a prijať prístup pokus-omyl, ktorý kombinuje odborné znalosti z aplikačnej oblasti s odporúčanými technikami a optimalizáciami špecifickými pre model.

Jupyter Notebook sprevádzajúci túto lekciu poskytuje _sandbox_ prostredie, kde si môžete vyskúšať, čo sa naučíte - ako pokračujete alebo ako súčasť výzvy na konci kódu. Na vykonanie cvičení budete potrebovať:

1. **Kľúč Azure OpenAI API** - služobný endpoint pre nasadený LLM.
2. **Python Runtime** - v ktorom môže byť Notebook vykonaný.
3. **Lokálne premenné prostredia** - _dokončite kroky [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), aby ste boli pripravení_.

Notebook prichádza so _začiatočnými_ cvičeniami - ale ste povzbudzovaní pridať svoje vlastné _Markdown_ (popis) a _Code_ (požiadavky promptov) sekcie, aby ste si vyskúšali viac príkladov alebo nápadov - a budovali svoju intuíciu pre návrh promptov.

## Ilustrovaný sprievodca

Chcete získať celkový obraz o tom, čo táto lekcia pokrýva, predtým než sa ponoríte? Pozrite si tento ilustrovaný sprievodca, ktorý vám poskytne predstavu o hlavných témach pokrytých a kľúčových poznatkoch, na ktoré by ste mali myslieť v každom z nich. Cestovná mapa lekcie vás zavedie od pochopenia základných konceptov a výziev až po ich riešenie s relevantnými technikami návrhu promptov a najlepšími postupmi. Upozorňujeme, že sekcia "Pokročilé techniky" v tomto sprievodcovi odkazuje na obsah pokrytý v _nasledujúcej_ kapitole tohto kurikula.

## Naša startupová spoločnosť

Teraz sa porozprávajme o tom, ako _táto téma_ súvisí s našou misiou startupu [priniesť AI inovácie do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať AI aplikácie poháňané personalizovaným učením - takže sa zamyslime nad tým, ako by rôzni používatelia našej aplikácie mohli "navrhovať" prompty:

- **Administrátori** by mohli požiadať AI, aby _analyzovala údaje o učebných osnovách na identifikáciu medzier v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať pomocou kódu.
- **Učitelia** by mohli požiadať AI, aby _vytvorila plán hodiny pre cieľové publikum a tému_. AI môže vytvoriť personalizovaný plán v špecifikovanom formáte.
- **Študenti** by mohli požiadať AI, aby ich _doučovala v náročnom predmete_. AI môže teraz študentov viesť pomocou lekcií, rád a príkladov prispôsobených ich úrovni.

To je len špička ľadovca. Pozrite si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otvorenú knižnicu promptov kurátorovanú odborníkmi na vzdelávanie - aby ste získali širší obraz o možnostiach! _Skúste spustiť niektoré z týchto promptov v sandboxe alebo pomocou OpenAI Playground a uvidíte, čo sa stane!_

## Čo je návrh promptov?

Začali sme túto lekciu definovaním **návrhu promptov** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) na dosiahnutie konzistentných a kvalitných odpovedí (dokončení) pre daný cieľ aplikácie a model. Môžeme to považovať za dvojkrokový proces:

- _navrhovanie_ počiatočného promptu pre daný model a cieľ
- _dolaďovanie_ promptu iteratívne na zlepšenie kvality odpovede

Toto je nevyhnutne proces pokus-omyl, ktorý vyžaduje intuíciu a úsilie používateľa na dosiahnutie optimálnych výsledkov. Tak prečo je to dôležité? Aby sme odpovedali na túto otázku, najprv musíme pochopiť tri koncepty:

- _Tokenizácia_ = ako model "vidí" prompt
- _Základné LLM_ = ako základný model "spracováva" prompt
- _LLM vyladené inštrukciami_ = ako model teraz vidí "úlohy"

### Tokenizácia

LLM vidí prompty ako _sekvenciu tokenov_, kde rôzne modely (alebo verzie modelu) môžu tokenizovať ten istý prompt rôznymi spôsobmi. Keďže LLM sú trénované na tokenoch (a nie na surovom texte), spôsob, akým sa prompty tokenizujú, má priamy vplyv na kvalitu generovanej odpovede.

Aby sme získali intuíciu o tom, ako tokenizácia funguje, vyskúšajte nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zobrazené nižšie. Skopírujte svoj prompt - a pozrite sa, ako sa to konvertuje na tokeny, pričom venujte pozornosť tomu, ako sa manipulujú znaky medzery a interpunkčné znamienka. Upozorňujeme, že tento príklad ukazuje starší LLM (GPT-3) - takže skúšanie tohto s novším modelom môže priniesť iný výsledok.

### Koncept: Základné modely

Keď je prompt tokenizovaný, primárna funkcia ["Základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo Základného modelu) je predpovedať token v tejto sekvencii. Keďže LLM sú trénované na masívnych textových datasetoch, majú dobrý pocit zo štatistických vzťahov medzi tokenmi a môžu túto predpoveď urobiť s určitým presvedčením. Upozorňujeme, že nerozumejú _významu_ slov v prompte alebo tokene; vidia len vzor, ktorý môžu "dokončiť" svojou ďalšou predpoveďou. Môžu pokračovať v predpovedaní sekvencie, kým nie sú ukončené zásahom používateľa alebo nejakou prednastavenou podmienkou.

Chcete vidieť, ako funguje dokončovanie na základe promptov? Zadajte vyššie uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s predvolenými nastaveniami. Systém je nakonfigurovaný tak, aby zaobchádzal s promptmi ako s požiadavkami na informácie - takže by ste mali vidieť dokončenie, ktoré uspokojí tento kontext.

Ale čo ak používateľ chcel vidieť niečo konkrétne, čo splní nejaké kritériá alebo cieľ úlohy? Tu prichádzajú do hry _LLM vyladené inštrukciami_.

### Koncept: LLM vyladené inštrukciami

[LLM vyladené inštrukciami](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začína základným modelom a jemne ho doladí pomocou príkladov alebo párov vstup/výstup (napr. viacotáčkové "správy"), ktoré môžu obsahovať jasné inštrukcie - a odpoveď AI sa snaží túto inštrukciu dodržať.

Toto využíva techniky ako Reinforcement Learning with Human Feedback (RLHF), ktoré môžu model trénovať na _sledovanie inštrukcií_ a _učenie sa z spätnej väzby_, aby produkoval odpovede, ktoré sú lepšie prispôsobené praktickým aplikáciám a relevantnejšie pre ciele používateľov.

Skúsme to - prejdite na vyššie uvedený prompt, ale teraz zmeňte _systémovú správu_, aby poskytla nasledujúcu inštrukciu ako kontext:

> _Zhrňte obsah, ktorý vám bol poskytnutý, pre žiaka druhej triedy. Udržte výsledok na jeden odsek s 3-5 bodmi._

Vidíte, ako je výsledok teraz naladený tak, aby odrážal požadovaný cieľ a formát? Učiteľ teraz môže túto odpoveď priamo použiť vo svojich prezentáciách pre tú triedu.

## Prečo potrebujeme návrh promptov?

Teraz, keď vieme, ako sú prompty spracovávané LLM, poďme sa porozprávať o tom, _prečo_ potrebujeme návrh promptov. Odpoveď spočíva v tom, že súčasné LLM predstavujú množstvo výziev, ktoré robia _spoľahlivé a konzistentné dokončenia_ náročnejšie dosiahnuť bez vynaloženia úsilia na konštrukciu a optimalizáciu promptov. Napríklad:

1. **Odpovede modelu sú stochastické.** _Ten istý prompt_ pravdepodobne vyprodukuje rôzne odpovede s rôznymi modelmi alebo verziami modelov. A môže dokonca produkovať rôzne výsledky s _tým istým modelom_ v rôznych časoch. _Techniky návrhu promptov nám môžu pomôcť minimalizovať tieto variácie poskytnutím lepších mantinelov_.

2. **Modely môžu fabrikovať odpovede.** Modely sú predtrénované na _veľkých, ale konečných_ datasetoch, čo znamená, že nemajú znalosti o konceptoch mimo tohto tréningového rozsahu. Výsledkom je, že môžu produkovať dokončenia, ktoré sú nepresné, imaginárne alebo priamo protirečia známym faktom. _Techniky návrhu promptov pomáhajú používateľom identifikovať a zmierniť takéto fabrikácie, napr. tým, že požiadajú AI o citácie alebo odôvodnenie_.

3. **Schopnosti modelov sa budú líšiť.** Novšie modely alebo generácie modelov budú mať bohatšie schopnosti, ale tiež prinášajú jedinečné zvláštnosti a kompromisy v nákladoch a zložitosti. _Návrh promptov nám môže pomôcť vyvinúť najlepšie postupy a pracovné postupy, ktoré abstrahujú rozdiely a prispôsobujú sa špecifickým požiadavkám modelov škálovateľným a bezproblémovým spôsobom_.

Pozrime sa na to v akcii v OpenAI alebo Azure OpenAI Playground:

- Použite ten istý prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) - videli ste variácie?
- Použite ten istý prompt opakovane s _tým istým_ nasadením LLM (napr. Azure OpenAI playground) - ako sa tieto variácie líšili?

### Príklad fabrikácií

V tomto kurze používame termín **"fabrikácia"** na označenie fenoménu, keď LLM niekedy generujú fakticky nesprávne informácie kvôli obmedzeniam vo svojom tréningu alebo iným obmedzeniam. Možno ste o tom tiež počuli ako o _"halucináciách"_ v populárnych článkoch alebo výskumných prácach. Avšak, dôrazne odporúčame používať _"fabrikácia"_ ako termín, aby sme náhodou nepripisovali ľudskú vlastnosť strojovo riadenému výsledku. Toto tiež posilňuje [smernice zodpovedného AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z terminologického hľadiska, odstraňujúc termíny, ktoré môžu byť považované za urážlivé alebo neinkluzívne v niektorých kontextoch.

Chcete získať predstavu o tom, ako fabrikácie fungujú? Premyslite si prompt, ktorý inštruuje AI, aby generovala obsah pre neexistujúcu tému (aby sa uistilo, že sa nenachádza v tréningovom datasete). Napríklad - skúsil som tento prompt:

> **Prompt:** generovať plán hodiny o Marťanskej vojne z roku 2076.

Webový vyhľadávač mi ukázal, že existovali fiktívne účty (napr. televízne seriály alebo knihy) o Marťanských vojnách - ale žiadne v roku 2076. Zdravý rozum nám tiež hovorí, že rok 2076 je _v bud
Nakoniec skutočná hodnota šablón spočíva v schopnosti vytvárať a publikovať _knižnice promptov_ pre vertikálne aplikačné domény - kde je šablóna promptu teraz _optimalizovaná_ tak, aby odrážala kontext alebo príklady špecifické pre aplikáciu, ktoré robia odpovede relevantnejšie a presnejšie pre cieľovú používateľskú skupinu. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, ktorý zhromažďuje knižnicu promptov pre oblasť vzdelávania s dôrazom na kľúčové ciele ako plánovanie hodín, návrh osnov, doučovanie študentov atď.

## Podporný obsah

Ak uvažujeme o konštrukcii promptov ako o inštrukcii (úloha) a cieli (primárny obsah), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytujeme na **ovplyvnenie výstupu určitým spôsobom**. Môže to byť ladenie parametrov, pokyny na formátovanie, taxonómie tém atď., ktoré môžu pomôcť modelu _prispôsobiť_ svoju odpoveď tak, aby vyhovovala požadovaným cieľom alebo očakávaniam používateľa.

Napríklad: Máme katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, značky metadát, inštruktor atď.) pre všetky dostupné kurzy v učebnom pláne:

- môžeme definovať inštrukciu na "zhrnutie katalógu kurzov pre jeseň 2023"
- môžeme použiť primárny obsah na poskytnutie niekoľkých príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu top 5 "značiek" záujmu.

Teraz môže model poskytnúť zhrnutie vo formáte, ktorý ukazujú niekoľko príkladov - ale ak má výsledok viacero značiek, môže uprednostniť 5 značiek identifikovaných v sekundárnom obsahu.

---

## Najlepšie praktiky promptovania

Teraz, keď vieme, ako môžu byť prompty _konštruované_, môžeme začať premýšľať o tom, ako ich _navrhnúť_ tak, aby odrážali najlepšie praktiky. Môžeme o tom premýšľať v dvoch častiach - mať správny _postoj_ a uplatňovať správne _techniky_.

### Postoj k promptovému inžinierstvu

Promptové inžinierstvo je proces pokusov a omylov, preto majte na pamäti tri široké usmerňujúce faktory:

1. **Porozumenie doméne je dôležité.** Presnosť a relevantnosť odpovedí je funkciou _domény_, v ktorej aplikácia alebo používateľ funguje. Uplatnite svoju intuíciu a odborné znalosti domény na **ďalšie prispôsobenie techník**. Napríklad, definujte _doménovo-špecifické osobnosti_ vo svojich systémových promptoch, alebo používajte _doménovo-špecifické šablóny_ vo svojich používateľských promptoch. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo používajte _doménovo-špecifické nápovedy a príklady_ na vedenie modelu smerom k známym vzorom používania.

2. **Porozumenie modelu je dôležité.** Vieme, že modely sú stochastické. Ale implementácie modelov sa môžu tiež líšiť z hľadiska tréningovej dátovej sady, ktorú používajú (predtrénované vedomosti), schopností, ktoré poskytujú (napr. cez API alebo SDK) a typu obsahu, pre ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné stránky a obmedzenia modelu, ktorý používate, a použite tieto znalosti na _prioritizáciu úloh_ alebo vytvorenie _prispôsobených šablón_, ktoré sú optimalizované pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako ako techniky promptového inžinierstva. Ako odborník na doménu môžete mať iný kontext alebo kritériá _vašej_ konkrétnej aplikácie, ktoré nemusia platiť pre širšiu komunitu. Použite nástroje a techniky promptového inžinierstva na "rýchly začiatok" konštrukcie promptov, potom iterujte a validujte výsledky pomocou vlastnej intuície a odborných znalostí domény. Zaznamenajte svoje poznatky a vytvorte **znalostnú základňu** (napr. knižnice promptov), ktorú môžu iní použiť ako nový základ pre rýchlejšie iterácie v budúcnosti.

## Najlepšie praktiky

Pozrime sa teraz na bežné najlepšie praktiky, ktoré odporúčajú odborníci [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Čo                                | Prečo                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnocujte najnovšie modely.    | Nové generácie modelov pravdepodobne majú vylepšené funkcie a kvalitu - ale môžu tiež spôsobiť vyššie náklady. Vyhodnoťte ich vplyv a potom urobte rozhodnutia o migrácii.                                                                         |
| Oddelte inštrukcie a kontext      | Skontrolujte, či váš model/poskytovateľ definuje _delimitery_ na jasnejšie rozlíšenie inštrukcií, primárneho a sekundárneho obsahu. To môže pomôcť modelom presnejšie priradiť váhy k tokenom.                                                      |
| Buďte konkrétny a jasný           | Poskytnite viac podrobností o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu aj konzistenciu odpovedí. Zachyťte recepty v opakovane použiteľných šablónach.                                                         |
| Buďte opisný, používajte príklady | Modely môžu lepšie reagovať na prístup "ukáž a povedz". Začnite s `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` hodnoty. Vráťte sa k [sekcii Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby ste sa dozvedeli viac.

### Ďalej otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x poskytovaný vývojovým kontajnerom.

Ste pripravení na spustenie cvičení. Všimnite si, že tu nie sú _správne a nesprávne_ odpovede - len skúmanie možností metódou pokusov a omylov a budovanie intuície pre to, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú segmenty riešenia kódu. Namiesto toho bude mať Notebook bunky Markdown s názvom "Moje riešenie:", ktoré ukazujú jeden príklad výstupu pre referenciu._

## Kontrola vedomostí

Ktorý z nasledujúcich promptov je dobrý podľa niektorých rozumných najlepších praktík?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného pri útesu so západom slnka
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

A: 2, je to najlepší prompt, pretože poskytuje detaily o "čom" a ide do špecifík (nielen akékoľvek auto, ale konkrétna značka a model) a tiež popisuje celkové prostredie. 3 je ďalší najlepší, pretože tiež obsahuje veľa popisu.

## 🚀 Výzva

Zistite, či dokážete využiť techniku "nápovedy" s promptom: Dokončite vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Ako na to model odpovie a ako by ste to zlepšili?

## Skvelá práca! Pokračujte vo svojom vzdelávaní

Chcete sa dozvedieť viac o rôznych konceptoch promptového inžinierstva? Prejdite na [stránku pokračujúceho vzdelávania](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje na túto tému.

Prejdite na Lekciu 5, kde sa pozrieme na [pokročilé techniky promptovania](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.