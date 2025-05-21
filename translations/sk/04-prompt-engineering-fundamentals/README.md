<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:15:46+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sk"
}
-->
# Základy tvorby promptov

## Úvod
Tento modul sa zaoberá základnými konceptmi a technikami pre tvorbu efektívnych promptov v generatívnych AI modeloch. Spôsob, akým píšete svoj prompt pre LLM, je tiež dôležitý. Starostlivo vytvorený prompt môže dosiahnuť lepšiu kvalitu odpovede. Ale čo presne znamenajú pojmy ako _prompt_ a _tvorba promptov_? A ako zlepším prompt _input_, ktorý posielam LLM? Toto sú otázky, na ktoré sa pokúsime odpovedať v tejto kapitole a v nasledujúcej.

_Generatívna AI_ je schopná vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) ako odpoveď na požiadavky používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ ako je séria GPT ("Generative Pre-trained Transformer") od OpenAI, ktoré sú trénované na používanie prirodzeného jazyka a kódu.

Používatelia môžu teraz interagovať s týmito modelmi pomocou známych paradigmat ako chat, bez potreby technickej odbornosti alebo školenia. Modely sú _založené na prompty_ - používatelia posielajú textový vstup (prompt) a dostávajú späť odpoveď AI (kompletné). Potom môžu "chatovať s AI" iteratívne, v rozhovoroch na viac úrovniach, zdokonaľovať svoj prompt, až kým odpoveď nesplní ich očakávania.

"Prompty" sa teraz stávajú primárnym _programovacím rozhraním_ pre generatívne AI aplikácie, hovoria modelom, čo majú robiť a ovplyvňujú kvalitu vrátených odpovedí. "Tvorba promptov" je rýchlo rastúce pole štúdia, ktoré sa zameriava na _návrh a optimalizáciu_ promptov na dodanie konzistentných a kvalitných odpovedí v rozsahu.

## Ciele učenia

V tejto lekcii sa dozvieme, čo je tvorba promptov, prečo je dôležitá a ako môžeme vytvárať efektívnejšie prompty pre daný model a cieľ aplikácie. Pochopíme základné koncepty a osvedčené postupy pre tvorbu promptov - a naučíme sa o interaktívnom prostredí "sandbox" v Jupyter Notebookoch, kde môžeme tieto koncepty aplikovať na reálnych príkladoch.

Na konci tejto lekcie budeme schopní:

1. Vysvetliť, čo je tvorba promptov a prečo je dôležitá.
2. Opísať komponenty promptu a ako sa používajú.
3. Naučiť sa osvedčené postupy a techniky pre tvorbu promptov.
4. Aplikovať naučené techniky na reálne príklady, pomocou OpenAI endpointu.

## Kľúčové pojmy

Tvorba promptov: Prax navrhovania a zdokonaľovania vstupov na usmernenie AI modelov k produkcii požadovaných výstupov.
Tokenizácia: Proces konvertovania textu na menšie jednotky, nazývané tokeny, ktoré model môže pochopiť a spracovať.
Inštrukciou vyladené LLMs: Veľké jazykové modely (LLMs), ktoré boli doladené s konkrétnymi inštrukciami na zlepšenie presnosti a relevantnosti ich odpovedí.

## Sandbox pre učenie

Tvorba promptov je momentálne viac umenie ako veda. Najlepší spôsob, ako zlepšiť našu intuíciu pre ňu, je _viac praxe_ a prijatie prístupu pokus-omyl, ktorý kombinuje odborné znalosti v aplikačnej oblasti s odporúčanými technikami a optimalizáciami špecifickými pre model.

Jupyter Notebook, ktorý sprevádza túto lekciu, poskytuje _sandbox_ prostredie, kde si môžete vyskúšať, čo sa naučíte - či už počas štúdia, alebo ako súčasť kódovej výzvy na konci. Na vykonanie cvičení budete potrebovať:

1. **Azure OpenAI API kľúč** - služobný endpoint pre nasadený LLM.
2. **Python Runtime** - v ktorom môže byť Notebook spustený.
3. **Lokálne env. premenné** - _dokončite kroky [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), aby ste boli pripravení_.

Notebook obsahuje _úvodné_ cvičenia - ale ste povzbudzovaní, aby ste pridali svoje vlastné _Markdown_ (popis) a _Code_ (prompt požiadavky) sekcie, aby ste si vyskúšali viac príkladov alebo nápadov - a vybudovali si intuíciu pre návrh promptov.

## Ilustrovaný sprievodca

Chcete získať celkový obraz o tom, čo táto lekcia pokrýva predtým, než sa do nej ponoríte? Pozrite si tento ilustrovaný sprievodca, ktorý vám poskytne predstavu o hlavných témach, ktoré sú pokryté, a kľúčových poznatkoch, nad ktorými by ste mali premýšľať v každej z nich. Plán lekcie vás prevedie od pochopenia základných konceptov a výziev až po ich riešenie s relevantnými technikami tvorby promptov a osvedčenými postupmi. Upozorňujeme, že sekcia "Pokročilé techniky" v tomto sprievodcovi sa odkazuje na obsah pokrytý v _nasledujúcej_ kapitole tohto kurikula.

## Naša startupová firma

Teraz sa poďme porozprávať o tom, ako _táto téma_ súvisí s našou startupovou misiou [priniesť AI inovácie do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme budovať aplikácie poháňané AI pre _personalizované učenie_ - tak sa zamyslime nad tým, ako rôzni používatelia našej aplikácie môžu "navrhovať" prompty:

- **Administrátori** môžu požiadať AI, aby _analyzovala údaje o učebných osnovách na identifikáciu medzier v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať pomocou kódu.
- **Učitelia** môžu požiadať AI, aby _vytvorila plán lekcie pre cieľovú skupinu a tému_. AI môže zostaviť personalizovaný plán v špecifikovanom formáte.
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI teraz môže viesť študentov s lekciami, nápovedami a príkladmi prispôsobenými ich úrovni.

To je len špička ľadovca. Pozrite sa na [Prompty pre vzdelávanie](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otvorenú knižnicu promptov kurátorsky spravovanú odborníkmi na vzdelávanie - aby ste získali širší prehľad o možnostiach! _Skúste spustiť niektoré z týchto promptov v sandboxe alebo pomocou OpenAI Playground a uvidíte, čo sa stane!_

## Čo je tvorba promptov?

Začali sme túto lekciu definovaním **tvorby promptov** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) na dodanie konzistentných a kvalitných odpovedí (kompletácií) pre daný aplikačný cieľ a model. Môžeme to považovať za dvojkrokový proces:

- _navrhovanie_ počiatočného promptu pre daný model a cieľ
- _zdokonaľovanie_ promptu iteratívne na zlepšenie kvality odpovede

Toto je nevyhnutne proces pokus-omyl, ktorý vyžaduje užívateľskú intuíciu a úsilie na dosiahnutie optimálnych výsledkov. Prečo je to teda dôležité? Na zodpovedanie tejto otázky musíme najprv pochopiť tri koncepty:

- _Tokenizácia_ = ako model "vidí" prompt
- _Základné LLMs_ = ako základný model "spracováva" prompt
- _Inštrukciou vyladené LLMs_ = ako model teraz môže vidieť "úlohy"

### Tokenizácia

LLM vidí prompty ako _sekvenciu tokenov_, kde rôzne modely (alebo verzie modelu) môžu tokenizovať ten istý prompt rôznymi spôsobmi. Keďže LLMs sú trénované na tokenoch (a nie na surovom texte), spôsob, akým sa prompty tokenizujú, má priamy vplyv na kvalitu generovanej odpovede.

Aby ste získali intuíciu o tom, ako tokenizácia funguje, skúste nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Skopírujte svoj prompt - a sledujte, ako sa prevádza na tokeny, pričom si všímajte, ako sú spracované znaky medzier a interpunkčné znamienka. Upozorňujeme, že tento príklad ukazuje starší LLM (GPT-3) - takže pokus s novším modelom môže priniesť iný výsledok.

### Koncept: Základné modely

Keď je prompt tokenizovaný, primárnou funkciou ["Základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo základného modelu) je predpovedať token v tejto sekvencii. Keďže LLMs sú trénované na obrovských textových datasetoch, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a môžu túto predpoveď urobiť s určitou dôverou. Upozorňujeme, že nerozumejú _významu_ slov v prompty alebo tokenu; vidia len vzor, ktorý môžu "dokončiť" svojou ďalšou predpoveďou. Môžu pokračovať v predpovedaní sekvencie, kým nie sú ukončené zásahom používateľa alebo nejakou prednastavenou podmienkou.

Chcete vidieť, ako funguje dokončenie založené na prompty? Zadajte vyššie uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s predvolenými nastaveniami. Systém je nakonfigurovaný tak, aby považoval prompty za požiadavky na informácie - takže by ste mali vidieť dokončenie, ktoré spĺňa tento kontext.

Ale čo ak by používateľ chcel vidieť niečo konkrétne, čo splňuje nejaké kritériá alebo cieľ úlohy? Tu prichádzajú na scénu _inštrukciou vyladené_ LLMs.

### Koncept: Inštrukciou vyladené LLMs

[Inštrukciou vyladený LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začína so základným modelom a doladí ho pomocou príkladov alebo párov vstup/výstup (napr. viacotáčkových "správ"), ktoré môžu obsahovať jasné inštrukcie - a odpoveď od AI sa snaží dodržať túto inštrukciu.

Toto využíva techniky ako Posilňovacie učenie s ľudskou spätnou väzbou (RLHF), ktoré môžu model naučiť _nasledovať inštrukcie_ a _učiť sa zo spätnej väzby_, aby produkoval odpovede, ktoré sú lepšie prispôsobené praktickým aplikáciám a viac relevantné pre ciele používateľov.

Skúsme to - znovu navštívte vyššie uvedený prompt, ale teraz zmeňte _systémovú správu_, aby poskytovala nasledujúcu inštrukciu ako kontext:

> _Zhrňte obsah, ktorý vám bol poskytnutý, pre druháka. Udržujte výsledok na jeden odsek s 3-5 bodmi._

Vidíte, ako je výsledok teraz naladený tak, aby odrážal požadovaný cieľ a formát? Učiteľ teraz môže priamo použiť túto odpoveď vo svojich slidoch pre túto triedu.

## Prečo potrebujeme tvorbu promptov?

Teraz, keď vieme, ako sú prompty spracovávané LLMs, poďme hovoriť o _prečo_ potrebujeme tvorbu promptov. Odpoveď spočíva v tom, že súčasné LLMs predstavujú niekoľko výziev, ktoré robia _spoľahlivé a konzistentné dokončenia_ náročnejšie na dosiahnutie bez vynaloženia úsilia na konštrukciu a optimalizáciu promptov. Napríklad:

1. **Odpovede modelu sú stochastické.** _Rovnaký prompt_ pravdepodobne vyprodukuje rôzne odpovede s rôznymi modelmi alebo verziami modelu. A môže dokonca produkovať rôzne výsledky s _tým istým modelom_ v rôznych časoch. _Techniky tvorby promptov nám môžu pomôcť minimalizovať tieto variácie poskytnutím lepších bezpečnostných opatrení_.

2. **Modely môžu fabrikovať odpovede.** Modely sú predtrénované s _veľkými, ale konečnými_ datasetmi, čo znamená, že nemajú znalosti o konceptoch mimo tohto tréningového rozsahu. Výsledkom je, že môžu produkovať dokončenia, ktoré sú nepresné, imaginárne alebo priamo protirečia známym faktom. _Techniky tvorby promptov pomáhajú používateľom identifikovať a zmierniť takéto fabrikácie, napríklad žiadaním AI o citácie alebo odôvodnenie_.

3. **Schopnosti modelov sa budú líšiť.** Novšie modely alebo generácie modelov budú mať bohatšie schopnosti, ale tiež prinesú jedinečné zvláštnosti a kompromisy v nákladoch a zložitosti. _Tvorba promptov nám môže pomôcť vyvinúť osvedčené postupy a pracovné postupy, ktoré abstrahujú rozdiely a prispôsobujú sa požiadavkám špecifickým pre modely v škálovateľných, bezproblémových spôsoboch_.

Pozrime sa na to v akcii v OpenAI alebo Azure OpenAI Playground:

- Použite rovnaký prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) - videli ste variácie?
- Použite rovnaký prompt opakovane s _tým istým_ nasadením LLM (napr. Azure OpenAI Playground) - ako sa tieto variácie líšili?

### Príklad fabrikácií

V tomto kurze používame termín **"fabrikácia"** na označenie javu, keď LLMs niekedy generujú fakticky nesprávne informácie kvôli obmedzeniam v ich tréningu alebo iným obmedzeniam. Možno ste tiež počuli, že sa to v populárnych článkoch alebo výskumných prácach označuje ako _"halucinácie"_. Avšak dôrazne odporúčame používať termín _"fabrikácia"_, aby sme náhodou nepripisovali ľudskú vlastnosť strojovo riadenému výsledku. To tiež posilňuje [smernice pre zodpovednú AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z hľadiska terminológie, odstránením výrazov, ktoré môžu byť v niektorých kontextoch považované za urážlivé alebo nevhodné.

Chcete získať predstavu o tom, ako fabrikácie fungujú? Premyslite si prompt, ktorý inštruuje AI, aby generovala obsah pre neexistujúcu tému (aby ste sa uistili, že sa nenachádza v tréningovom datasete). Napríklad - skúsil som tento prompt:

> **Prompt:** vytvorte plán lekcie o Marsovskej vojne z roku 2076.

Webový vyhľadávač mi ukázal, že existovali fiktívne účty (napr. televízne seriály alebo knihy) o Marsovských vojnách - ale žiadne v roku 2076. Zdravý rozum nám tiež h
Skutočná hodnota šablón spočíva v schopnosti vytvárať a publikovať _knižnice promptov_ pre vertikálne aplikačné domény - kde je šablóna promptu teraz _optimalizovaná_ tak, aby odrážala kontext špecifický pre aplikáciu alebo príklady, ktoré robia odpovede relevantnejšie a presnejšie pre cieľovú skupinu používateľov. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, ktorý zhromažďuje knižnicu promptov pre oblasť vzdelávania s dôrazom na kľúčové ciele, ako je plánovanie lekcií, navrhovanie učebných osnov, doučovanie študentov atď.

## Podporný obsah

Ak premýšľame o konštrukcii promptov ako o inštrukcii (úlohe) a cieli (primárnom obsahu), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytujeme na **ovplyvnenie výstupu určitým spôsobom**. Môže to byť ladenie parametrov, formátovacie pokyny, taxonómie tém atď., ktoré môžu modelu pomôcť _prispôsobiť_ jeho odpoveď tak, aby vyhovovala požadovaným cieľom alebo očakávaniam používateľa.

Napríklad: Daný katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, metadátové značky, inštruktor atď.) o všetkých dostupných kurzoch v učebných osnovách:

- môžeme definovať inštrukciu "zhrň katalóg kurzov pre jeseň 2023"
- môžeme použiť primárny obsah na poskytnutie niekoľkých príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu top 5 "značiek" záujmu.

Teraz môže model poskytnúť zhrnutie vo formáte ukázanom niekoľkými príkladmi - ale ak má výsledok viacero značiek, môže uprednostniť 5 značiek identifikovaných v sekundárnom obsahu.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #1.
Posilniť koncept príkladmi a odkazmi.

KONCEPT #3:
Techniky návrhu promptov.
Aké sú niektoré základné techniky návrhu promptov?
Ilustrujte to niekoľkými cvičeniami.
-->

## Najlepšie praktiky pre prompty

Teraz, keď vieme, ako sa prompty môžu _konštruovať_, môžeme začať premýšľať o tom, ako ich _navrhnúť_ tak, aby odrážali najlepšie praktiky. Môžeme o tom premýšľať v dvoch častiach - mať správny _mentálny postoj_ a aplikovať správne _techniky_.

### Mentálny postoj návrhu promptov

Návrh promptov je proces pokusov a omylov, preto majte na pamäti tri široké usmerňujúce faktory:

1. **Porozumenie domény je dôležité.** Presnosť a relevantnosť odpovede je funkcia _domény_, v ktorej tá aplikácia alebo používateľ pôsobí. Použite svoju intuíciu a odborné znalosti domény na **prispôsobenie techník** ďalej. Napríklad, definujte _osobnosti špecifické pre doménu_ vo svojich systémových promptoch alebo použite _šablóny špecifické pre doménu_ vo svojich užívateľských promptoch. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo použite _náznaky a príklady špecifické pre doménu_ na usmernenie modelu k známym vzorom použitia.

2. **Porozumenie modelu je dôležité.** Vieme, že modely sú stochastické povahy. Ale implementácie modelov sa môžu tiež líšiť z hľadiska dátovej sady, ktorú používajú (predtrénované znalosti), schopností, ktoré poskytujú (napr. prostredníctvom API alebo SDK) a typu obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné stránky a obmedzenia modelu, ktorý používate, a použite tieto znalosti na _prioritizáciu úloh_ alebo vytvorenie _prispôsobených šablón_, ktoré sú optimalizované pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako ako techniky návrhu promptov. Ako odborník na doménu môžete mať iný kontext alebo kritériá pre _vašu_ konkrétnu aplikáciu, ktoré nemusia platiť pre širšiu komunitu. Použite nástroje a techniky návrhu promptov na "rýchly štart" konštrukcie promptov, potom iterujte a validujte výsledky pomocou svojej vlastnej intuície a odborných znalostí domény. Zaznamenajte svoje poznatky a vytvorte **znalostnú základňu** (napr. knižnice promptov), ktoré môžu byť použité ako nový základ ostatnými, pre rýchlejšie iterácie v budúcnosti.

## Najlepšie praktiky

Pozrime sa teraz na bežné najlepšie praktiky, ktoré odporúčajú odborníci z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Čo                                | Prečo                                                                                                                                                                                                                                               |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vyhodnoťte najnovšie modely.      | Nové generácie modelov pravdepodobne majú vylepšené funkcie a kvalitu - ale môžu tiež spôsobiť vyššie náklady. Vyhodnoťte ich vplyv a potom urobte rozhodnutia o migrácii.                                                                           |
| Oddelte inštrukcie a kontext      | Skontrolujte, či váš model/poskytovateľ definuje _oddeľovače_, ktoré jasnejšie rozlišujú inštrukcie, primárny a sekundárny obsah. To môže pomôcť modelom presnejšie priradiť váhy k tokenom.                                                            |
| Buďte konkrétny a jasný           | Poskytnite viac podrobností o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu a konzistentnosť odpovedí. Zachyťte recepty v opakovane použiteľných šablónach.                                                           |
| Buďte popisný, používajte príklady| Modely môžu lepšie reagovať na prístup "ukáž a povedz". Začnite s `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` hodnotami. Vráťte sa do sekcie [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby ste sa naučili ako.

### Ďalej otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x poskytovaný dev kontajnerom.

Ste pripravení spustiť cvičenia. Všimnite si, že tu nie sú _správne a nesprávne_ odpovede - len skúmanie možností pokusom a omylom a budovanie intuície pre to, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú žiadne segmenty riešenia kódu. Namiesto toho bude Notebook obsahovať bunky Markdown s názvom "Moje riešenie:", ktoré ukazujú jeden príklad výstupu na referenciu._

 <!--
ŠABLÓNA LEKCIE:
Uzavrite sekciu zhrnutím a zdrojmi pre samostatné učenie.
-->

## Kontrola znalostí

Ktorý z nasledujúcich je dobrý prompt podľa niektorých rozumných najlepších praktík?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného pri útesu so západom slnka
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

A: 2, je to najlepší prompt, pretože poskytuje podrobnosti o "čo" a ide do špecifík (nielen akékoľvek auto, ale konkrétnu značku a model) a tiež opisuje celkové prostredie. 3 je ďalší najlepší, pretože tiež obsahuje veľa popisov.

## 🚀 Výzva

Skúste využiť techniku "náznak" s promptom: Dokončite vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Čo odpovie, a ako by ste to vylepšili?

## Skvelá práca! Pokračujte vo svojom učení

Chcete sa dozvedieť viac o rôznych konceptoch návrhu promptov? Prejdite na [stránku pokračujúceho učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje na túto tému.

Prejdite na Lekciu 5, kde sa pozrieme na [pokročilé techniky promptov](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny preklad človekom. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.