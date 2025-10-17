<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-17T22:00:31+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sk"
}
-->
# Základy tvorby promptov

[![Základy tvorby promptov](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.sk.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Úvod
Tento modul pokrýva základné koncepty a techniky na vytváranie efektívnych promptov pre generatívne AI modely. Spôsob, akým napíšete svoj prompt pre LLM, je dôležitý. Dôkladne vytvorený prompt môže priniesť kvalitnejšiu odpoveď. Ale čo presne znamenajú pojmy ako _prompt_ a _tvorba promptov_? A ako môžem zlepšiť _vstupný prompt_, ktorý posielam LLM? Na tieto otázky sa pokúsime odpovedať v tejto kapitole a v nasledujúcej.

_Generatívna AI_ dokáže vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) na základe požiadaviek používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ ako séria GPT ("Generative Pre-trained Transformer") od OpenAI, ktoré sú trénované na používanie prirodzeného jazyka a kódu.

Používatelia teraz môžu interagovať s týmito modelmi pomocou známych paradigmatov, ako je chat, bez potreby technických znalostí alebo školenia. Modely sú _založené na promptoch_ - používatelia posielajú textový vstup (prompt) a dostávajú odpoveď AI (výstup). Následne môžu "chatovať s AI" iteratívne, v konverzáciách na viacero kôl, upravovať svoj prompt, až kým odpoveď nezodpovedá ich očakávaniam.

"Prompty" sa teraz stávajú primárnym _programovacím rozhraním_ pre aplikácie generatívnej AI, ktoré modelom hovoria, čo majú robiť, a ovplyvňujú kvalitu vrátených odpovedí. "Tvorba promptov" je rýchlo rastúca oblasť štúdia, ktorá sa zameriava na _návrh a optimalizáciu_ promptov na dosiahnutie konzistentných a kvalitných odpovedí vo veľkom rozsahu.

## Ciele učenia

V tejto lekcii sa naučíme, čo je tvorba promptov, prečo je dôležitá a ako môžeme vytvárať efektívnejšie prompty pre konkrétny model a cieľ aplikácie. Pochopíme základné koncepty a osvedčené postupy pre tvorbu promptov - a dozvieme sa o interaktívnom prostredí "sandbox" v Jupyter Notebookoch, kde môžeme tieto koncepty aplikovať na reálne príklady.

Na konci tejto lekcie budeme schopní:

1. Vysvetliť, čo je tvorba promptov a prečo je dôležitá.
2. Opísať komponenty promptu a ich využitie.
3. Naučiť sa osvedčené postupy a techniky tvorby promptov.
4. Aplikovať naučené techniky na reálne príklady pomocou OpenAI endpointu.

## Kľúčové pojmy

Tvorba promptov: Prax navrhovania a zdokonaľovania vstupov na usmernenie AI modelov k produkcii požadovaných výstupov.  
Tokenizácia: Proces konverzie textu na menšie jednotky, nazývané tokeny, ktoré model dokáže pochopiť a spracovať.  
LLM upravené na inštrukcie: Veľké jazykové modely (LLM), ktoré boli jemne doladené konkrétnymi inštrukciami na zlepšenie presnosti a relevantnosti ich odpovedí.

## Sandbox na učenie

Tvorba promptov je momentálne viac umenie než veda. Najlepší spôsob, ako si zlepšiť intuíciu v tejto oblasti, je _viac praktizovať_ a prijať prístup pokus-omyl, ktorý kombinuje odborné znalosti z aplikačnej oblasti s odporúčanými technikami a optimalizáciami špecifickými pre model.

Jupyter Notebook, ktorý sprevádza túto lekciu, poskytuje prostredie _sandbox_, kde si môžete vyskúšať, čo ste sa naučili - priebežne alebo ako súčasť kódovej výzvy na konci. Na vykonanie cvičení budete potrebovať:

1. **API kľúč Azure OpenAI** - endpoint služby pre nasadený LLM.  
2. **Python runtime** - prostredie, v ktorom je možné spustiť Notebook.  
3. **Lokálne environmentálne premenné** - _dokončite kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) teraz, aby ste boli pripravení_.

Notebook obsahuje _úvodné_ cvičenia - ale odporúčame vám pridať vlastné sekcie _Markdown_ (popis) a _Code_ (požiadavky na prompt), aby ste si vyskúšali viac príkladov alebo nápadov - a vybudovali si intuíciu pre návrh promptov.

## Ilustrovaný sprievodca

Chcete získať celkový obraz o tom, čo táto lekcia pokrýva, predtým než sa do nej pustíte? Pozrite si tento ilustrovaný sprievodca, ktorý vám poskytne prehľad hlavných tém a kľúčových poznatkov, o ktorých by ste mali premýšľať v každej z nich. Cestovná mapa lekcie vás prevedie od pochopenia základných konceptov a výziev k ich riešeniu pomocou relevantných techník a osvedčených postupov tvorby promptov. Upozorňujeme, že sekcia "Pokročilé techniky" v tomto sprievodcovi sa týka obsahu pokrytého v _nasledujúcej_ kapitole tejto učebnej osnovy.

![Ilustrovaný sprievodca tvorbou promptov](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.sk.png)

## Naša startupová misia

Teraz sa pozrime, ako _táto téma_ súvisí s našou startupovou misiou [priniesť inováciu AI do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať aplikácie poháňané AI pre _personalizované vzdelávanie_ - takže sa zamyslime nad tým, ako by rôzni používatelia našej aplikácie mohli "navrhovať" prompty:

- **Administrátori** môžu požiadať AI, aby _analyzovala údaje o učebných osnovách na identifikáciu medzier v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať pomocou kódu.  
- **Učitelia** môžu požiadať AI, aby _vytvorila plán lekcie pre cieľovú skupinu a tému_. AI môže vytvoriť personalizovaný plán v špecifikovanom formáte.  
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI môže študentov viesť lekciami, tipmi a príkladmi prispôsobenými ich úrovni.  

To je len špička ľadovca. Pozrite si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - knižnicu promptov s otvoreným zdrojovým kódom, ktorú zostavili odborníci na vzdelávanie - aby ste získali širší prehľad o možnostiach! _Vyskúšajte spustiť niektoré z týchto promptov v sandboxe alebo pomocou OpenAI Playground a uvidíte, čo sa stane!_

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #1.
Posilnite koncept pomocou príkladov a referencií.

KONCEPT #1:
Tvorba promptov.
Definujte ho a vysvetlite, prečo je potrebný.
-->

## Čo je tvorba promptov?

Túto lekciu sme začali definovaním **tvorby promptov** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) na dosiahnutie konzistentných a kvalitných odpovedí (výstupov) pre konkrétny cieľ aplikácie a model. Môžeme si to predstaviť ako dvojkrokový proces:

- _navrhovanie_ počiatočného promptu pre konkrétny model a cieľ  
- _zdokonaľovanie_ promptu iteratívne na zlepšenie kvality odpovede  

Toto je nevyhnutne proces pokus-omyl, ktorý vyžaduje intuíciu a úsilie používateľa na dosiahnutie optimálnych výsledkov. Prečo je to teda dôležité? Na zodpovedanie tejto otázky musíme najprv pochopiť tri koncepty:

- _Tokenizácia_ = ako model "vidí" prompt  
- _Základné LLM_ = ako základný model "spracováva" prompt  
- _LLM upravené na inštrukcie_ = ako model dokáže "vidieť úlohy"  

### Tokenizácia

LLM vidí prompty ako _sekvenciu tokenov_, pričom rôzne modely (alebo verzie modelu) môžu tokenizovať ten istý prompt rôznymi spôsobmi. Keďže LLM sú trénované na tokenoch (a nie na surovom texte), spôsob, akým sa prompty tokenizujú, má priamy vplyv na kvalitu generovanej odpovede.

Aby ste získali intuíciu o tom, ako funguje tokenizácia, vyskúšajte nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) uvedený nižšie. Skopírujte svoj prompt - a pozrite sa, ako sa konvertuje na tokeny, pričom venujte pozornosť tomu, ako sa spracovávajú medzery a interpunkčné znamienka. Upozorňujeme, že tento príklad ukazuje starší LLM (GPT-3) - takže skúšanie tohto s novším modelom môže priniesť iný výsledok.

![Tokenizácia](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.sk.png)

### Koncept: Základné modely

Keď je prompt tokenizovaný, primárnou funkciou ["Základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo základného modelu) je predpovedať token v tejto sekvencii. Keďže LLM sú trénované na obrovských textových dátach, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a dokážu túto predpoveď urobiť s určitou istotou. Upozorňujeme, že nerozumejú _významu_ slov v promptoch alebo tokenoch; vidia len vzor, ktorý môžu "doplniť" svojou ďalšou predpoveďou. Môžu pokračovať v predpovedaní sekvencie, kým ich nezastaví zásah používateľa alebo nejaká prednastavená podmienka.

Chcete vidieť, ako funguje dokončovanie na základe promptov? Zadajte vyššie uvedený prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) v Azure OpenAI Studio s predvolenými nastaveniami. Systém je nakonfigurovaný tak, aby prompty považoval za požiadavky na informácie - takže by ste mali vidieť výstup, ktorý uspokojí tento kontext.

Ale čo ak používateľ chcel vidieť niečo konkrétne, čo spĺňa určité kritériá alebo cieľ úlohy? Tu prichádzajú na scénu _LLM upravené na inštrukcie_.

![Základné LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.sk.png)

### Koncept: LLM upravené na inštrukcie

[LLM upravené na inštrukcie](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začínajú základným modelom a jemne ho dolaďujú pomocou príkladov alebo párov vstup/výstup (napr. viacnásobné "správy"), ktoré môžu obsahovať jasné inštrukcie - a odpoveď AI sa pokúša tieto inštrukcie dodržať.

Používajú sa techniky ako posilňovacie učenie s ľudskou spätnou väzbou (RLHF), ktoré môžu model trénovať na _dodržiavanie inštrukcií_ a _učenie sa zo spätnej väzby_, aby produkoval odpovede, ktoré sú lepšie prispôsobené praktickým aplikáciám a relevantnejšie pre ciele používateľa.

Vyskúšajme si to - vráťte sa k vyššie uvedenému promptu, ale teraz zmeňte _systémovú správu_, aby poskytovala nasledujúcu inštrukciu ako kontext:

> _Zhrňte obsah, ktorý vám bol poskytnutý, pre druháka. Výsledok udržte na jednom odseku s 3-5 bodmi._

Pozrite sa, ako je výsledok teraz prispôsobený tak, aby odrážal požadovaný cieľ a formát? Učiteľ môže teraz priamo použiť túto odpoveď vo svojich prezentáciách pre danú triedu.

![LLM upravené na inštrukcie - Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.sk.png)

## Prečo potrebujeme tvorbu promptov?

Teraz, keď vieme, ako LLM spracovávajú prompty, poďme sa porozprávať o _tom, prečo_ potrebujeme tvorbu promptov. Odpoveď spočíva v tom, že súčasné LLM predstavujú množstvo výziev, ktoré robia _spoľahlivé a konzistentné výstupy_ náročnejšími na dosiahnutie bez vynaloženia úsilia na konštrukciu a optimalizáciu promptov. Napríklad:

1. **Odpovede modelu sú stochastické.** _Ten istý prompt_ pravdepodobne vyprodukuje rôzne odpovede s rôznymi modelmi alebo verziami modelu. A môže dokonca produkovať rôzne výsledky s _tým istým modelom_ v rôznych časoch. _Techniky tvorby promptov nám môžu pomôcť minimalizovať tieto variácie poskytnutím lepších mantinelov_.

1. **Modely môžu vytvárať falošné odpovede.** Modely sú predtrénované na _veľkých, ale konečných_ datasetoch, čo znamená, že nemajú znalosti o konceptoch mimo rozsahu toho tréningu. Výsledkom je, že môžu produkovať výstupy, ktoré sú nepresné, vymyslené alebo priamo protirečia známym faktom. _Techniky tvorby promptov pomáhajú používateľom identifikovať a zmierniť takéto výmysly, napr. požiadaním AI o citácie alebo zdôvodnenie_.

1. **Schopnosti modelov sa líšia.** Novšie modely alebo generácie modelov budú mať bohatšie schopnosti, ale tiež prinášajú jedinečné zvláštnosti a kompromisy v nákladoch a zložitosti. _Tvorba promptov nám môže pomôcť vyvinúť osvedčené postupy a pracovné postupy, ktoré abstrahujú rozdiely a prispôsobujú sa špecifickým požiadavkám modelu škálovateľným a bezproblémovým spôsobom_.

Pozrime sa na to v praxi v OpenAI alebo Azure OpenAI Playground:

- Použite ten istý prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) - videli ste variácie?  
- Použite ten istý prompt opakovane s _tým istým_ nasadením LLM (napr. Azure OpenAI Playground) - ako sa tieto variácie líšili?  

### Príklad vymyslených odpovedí

V tomto kurze používame termín **"vymyslenie"** na označenie fenoménu, keď LLM niekedy generujú fakticky nesprávne informácie kvôli obmedzeniam vo svojom tréningu alebo iným faktorom. Možno ste sa s týmto javom stretli aj pod pojmom _"hal
Webové vyhľadávanie mi ukázalo, že existujú fiktívne príbehy (napr. televízne seriály alebo knihy) o vojnách na Marse – ale žiadne z roku 2076. Zdravý rozum nám tiež hovorí, že rok 2076 je _v budúcnosti_ a preto nemôže byť spojený so skutočnou udalosťou.

Čo sa však stane, keď tento príkaz spustíme s rôznymi poskytovateľmi LLM?

> **Odpoveď 1**: OpenAI Playground (GPT-35)

![Odpoveď 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.sk.png)

> **Odpoveď 2**: Azure OpenAI Playground (GPT-35)

![Odpoveď 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.sk.png)

> **Odpoveď 3**: Hugging Face Chat Playground (LLama-2)

![Odpoveď 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.sk.png)

Ako sa očakávalo, každý model (alebo verzia modelu) generuje mierne odlišné odpovede vďaka stochastickému správaniu a rozdielom v schopnostiach modelov. Napríklad jeden model sa zameriava na publikum ôsmeho ročníka, zatiaľ čo druhý predpokladá študentov strednej školy. Ale všetky tri modely generovali odpovede, ktoré by mohli presvedčiť neinformovaného používateľa, že udalosť bola skutočná.

Techniky navrhovania príkazov, ako _metaprompting_ a _konfigurácia teploty_, môžu do určitej miery znížiť výskyt výmyslov modelov. Nové architektúry navrhovania príkazov tiež bezproblémovo začleňujú nové nástroje a techniky do toku príkazov, aby zmiernili alebo znížili niektoré z týchto efektov.

## Prípadová štúdia: GitHub Copilot

Túto sekciu zakončíme tým, že si ukážeme, ako sa navrhovanie príkazov používa v reálnych riešeniach, na príklade jednej prípadovej štúdie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš "AI programátorský partner" – konvertuje textové príkazy na návrhy kódu a je integrovaný do vášho vývojového prostredia (napr. Visual Studio Code) pre bezproblémový používateľský zážitok. Ako je zdokumentované v sérii blogov nižšie, najskoršia verzia bola založená na modeli OpenAI Codex – pričom inžinieri rýchlo zistili potrebu doladiť model a vyvinúť lepšie techniky navrhovania príkazov, aby sa zlepšila kvalita kódu. V júli [predstavili vylepšený AI model, ktorý presahuje Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pre ešte rýchlejšie návrhy.

Prečítajte si príspevky v poradí, aby ste sledovali ich cestu učenia.

- **Máj 2023** | [GitHub Copilot sa zlepšuje v porozumení vášho kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Máj 2023** | [V zákulisí GitHubu: Práca s LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jún 2023** | [Ako písať lepšie príkazy pre GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Júl 2023** | [.. GitHub Copilot presahuje Codex s vylepšeným AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Júl 2023** | [Sprievodca vývojára k navrhovaniu príkazov a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Ako vytvoriť podnikový LLM aplikáciu: Lekcie z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Môžete si tiež prezrieť ich [blog o inžinierstve](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pre ďalšie príspevky, ako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ktorý ukazuje, ako sa tieto modely a techniky _používajú_ na poháňanie aplikácií v reálnom svete.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #2.
Posilnite koncept pomocou príkladov a odkazov.

KONCEPT #2:
Navrhovanie príkazov.
Ilustrované príkladmi.
-->

## Konštrukcia príkazov

Videli sme, prečo je navrhovanie príkazov dôležité – teraz pochopíme, ako sa príkazy _konštruujú_, aby sme mohli vyhodnotiť rôzne techniky pre efektívnejší návrh príkazov.

### Základný príkaz

Začnime základným príkazom: textový vstup odoslaný modelu bez ďalšieho kontextu. Tu je príklad – keď pošleme prvé slová americkej národnej hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžite _dokončí_ odpoveď ďalšími riadkami, čo ilustruje základné prediktívne správanie.

| Príkaz (Vstup)     | Dokončenie (Výstup)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdá sa, že začínate text piesne "The Star-Spangled Banner", národnej hymny Spojených štátov. Celý text je ... |

### Komplexný príkaz

Teraz pridajme kontext a pokyny k základnému príkazu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje konštruovať komplexný príkaz ako kolekciu _správ_ s:

- Pármi vstup/výstup, ktoré odrážajú _používateľský_ vstup a _odpoveď asistenta_.
- Systémovou správou, ktorá nastavuje kontext pre správanie alebo osobnosť asistenta.

Požiadavka je teraz vo forme nižšie, kde _tokenizácia_ efektívne zachytáva relevantné informácie z kontextu a konverzácie. Zmena systémového kontextu môže mať rovnako veľký vplyv na kvalitu dokončení ako poskytnuté používateľské vstupy.

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

### Príkaz s pokynmi

V predchádzajúcich príkladoch bol používateľský príkaz jednoduchým textovým dotazom, ktorý možno interpretovať ako žiadosť o informácie. Pri príkazoch s _pokynmi_ môžeme tento text použiť na podrobnejšie špecifikovanie úlohy, čím poskytneme AI lepšie usmernenie. Tu je príklad:

| Príkaz (Vstup)                                                                                                                                                                                                                         | Dokončenie (Výstup)                                                                                                        | Typ pokynov        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napíšte opis občianskej vojny                                                                                                                                                                                                          | _vrátený jednoduchý odsek_                                                                                                 | Jednoduchý          |
| Napíšte opis občianskej vojny. Uveďte kľúčové dátumy a udalosti a opíšte ich význam                                                                                                                                                     | _vrátený odsek nasledovaný zoznamom kľúčových dátumov udalostí s popismi_                                                  | Komplexný           |
| Napíšte opis občianskej vojny v 1 odseku. Uveďte 3 odrážky s kľúčovými dátumami a ich významom. Uveďte ďalšie 3 odrážky s kľúčovými historickými osobnosťami a ich prínosmi. Výstup vráťte ako JSON súbor.                                | _vrátené rozsiahlejšie detaily v textovom poli, formátované ako JSON, ktorý môžete skopírovať do súboru a overiť podľa potreby_ | Komplexný. Formátovaný. |

## Primárny obsah

V predchádzajúcich príkladoch bol príkaz stále pomerne otvorený, čo umožnilo LLM rozhodnúť, ktorá časť jeho predtrénovanej databázy je relevantná. S dizajnovým vzorom _primárneho obsahu_ je vstupný text rozdelený na dve časti:

- pokyn (akcia)
- relevantný obsah (ktorý ovplyvňuje akciu)

Tu je príklad, kde pokyn je "zhrňte to v 2 vetách".

| Príkaz (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončenie (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. Je pomenovaný po rímskom bohu Jupiterovi.[19] Pri pohľade zo Zeme môže byť Jupiter dostatočne jasný na to, aby jeho odrazené svetlo vrhalo viditeľné tiene,[20] a je priemerne tretím najjasnejším prírodným objektom na nočnej oblohe po Mesiaci a Venuši. <br/> **Zhrňte to v 2 krátkych vetách** | Jupiter, piata planéta od Slnka, je najväčšia v Slnečnej sústave a je známa ako jeden z najjasnejších objektov na nočnej oblohe. Pomenovaný po rímskom bohu Jupiterovi, je plynným obrom s hmotnosťou dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. |

Segment primárneho obsahu môže byť použitý rôznymi spôsobmi na efektívnejšie usmernenie pokynov:

- **Príklady** – namiesto toho, aby sme modelu explicitne povedali, čo má robiť, poskytneme mu príklady požadovaného výstupu a necháme ho odvodiť vzor.
- **Náznaky** – nasledujte pokyn s "náznakom", ktorý modelu poskytne smerovanie k relevantnejším odpovediam.
- **Šablóny** – opakovateľné 'recepty' pre príkazy s premennými (miestami), ktoré môžu byť prispôsobené údajmi pre konkrétne použitia.

Poďme si tieto techniky ukázať v praxi.

### Používanie príkladov

Toto je prístup, kde použijete primárny obsah na "nakŕmenie modelu" niekoľkými príkladmi požadovaného výstupu pre daný pokyn a necháte ho odvodiť vzor pre požadovaný výstup. Na základe počtu poskytnutých príkladov môžeme mať zero-shot prompting, one-shot prompting, few-shot prompting atď.

Príkaz teraz pozostáva z troch komponentov:

- Popis úlohy
- Niekoľko príkladov požadovaného výstupu
- Začiatok nového príkladu (ktorý sa stáva implicitným popisom úlohy)

| Typ učenia | Príkaz (Vstup)                                                                                                                                        | Dokončenie (Výstup)         |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot  | "The Sun is Shining". Preložte do španielčiny                                                                                                         | "El Sol está brillando".    |
| One-shot   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot   | Hráč bežal po métach => Baseball <br/> Hráč zahral eso => Tenis <br/> Hráč zahral šestku => Kriket <br/> Hráč skóroval slam-dunk =>                   | Basketbal                   |
|            |                                                                                                                                                       |                             |

Všimnite si, ako sme museli poskytnúť explicitný pokyn ("Preložte do španielčiny") pri zero-shot promptingu, ale v one-shot promptingu sa to odvádza. Few-shot príklad ukazuje, ako pridanie viacerých príkladov umožňuje modelom robiť presnejšie odvodenia bez ďalších pokynov.

### Náznaky príkazov

Ďalšou technikou pre použitie primárneho obsahu je poskytnutie _náznakov_ namiesto príkladov. V tomto prípade dávame modelu podnet správnym smerom tým, že _začneme_ odpoveď úryvkom, ktorý odráža požadovaný formát odpovede. Model potom "nasleduje náznak" a pokračuje v rovnakom duchu.

| Počet náznakov | Príkaz (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončenie (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred zaznamenanou históriou. <br/>**Zhrňte to**                                       | Jupiter je najväčšia planéta v našej Slnečnej sústave a piata od Slnka. Je to plynný obor s hmotnosťou 1/1000 hmotnosti Slnka, ale je ťažší ako všetky ostatné planéty dokopy. Staroveké civilizácie poznali Jupiter už dávno a je ľahko viditeľný na nočnej oblohe. |
| 1              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a polkrát väčšou ako všetky ostatné planéty v Slnečnej sústave dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od čias pred zaznamenanou históriou. <br/>**Zhrňte to** <br/> Čo sme sa naučili je, že Jupiter | je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a polkrát väčšou ako všetky ostatné planéty dokopy. Je ľahko viditeľný voľným okom a je známy už od staroveku.                        |
| 2              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a polkrát väčšou ako všetky ostatné planéty v Slnečnej sústave dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od čias pred zaznamenanou históriou. <br/>**Zhrňte to** <br/> Top 3 fakty, ktoré sme sa naučili:         | 1. Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. <br/> 2. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka...<br/> 3. Jupiter je viditeľný voľným okom už od staroveku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablóny pre výzvy

Šablóna výzvy je _vopred definovaný recept na výzvu_, ktorý je možné uložiť a opakovane používať podľa potreby, aby sa zabezpečila konzistentnejšia používateľská skúsenosť vo veľkom rozsahu. V najjednoduchšej forme je to jednoducho zbierka príkladov výziev ako [tento od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), ktorý poskytuje interaktívne komponenty výzvy (správy používateľa a systému) a formát požiadavky riadený API - na podporu opakovanej použiteľnosti.

V jeho zložitejšej forme, ako [tento príklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), obsahuje _zástupné symboly_, ktoré je možné nahradiť údajmi z rôznych zdrojov (vstup používateľa, kontext systému, externé zdroje údajov atď.) na dynamické generovanie výzvy. To nám umožňuje vytvoriť knižnicu opakovane použiteľných výziev, ktoré sa dajú použiť na programatické zabezpečenie konzistentnej používateľskej skúsenosti vo veľkom rozsahu.

Nakoniec, skutočná hodnota šablón spočíva v schopnosti vytvárať a publikovať _knižnice výziev_ pre vertikálne aplikačné domény - kde je šablóna výzvy teraz _optimalizovaná_ tak, aby odrážala kontext alebo príklady špecifické pre aplikáciu, ktoré robia odpovede relevantnejšími a presnejšími pre cieľovú skupinu používateľov. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, ktorý kurátorsky zhromažďuje knižnicu výziev pre vzdelávaciu oblasť s dôrazom na kľúčové ciele, ako je plánovanie lekcií, návrh učebných osnov, doučovanie študentov atď.

## Podporný obsah

Ak uvažujeme o konštrukcii výzvy ako o inštrukcii (úlohe) a cieli (primárny obsah), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytujeme na **ovplyvnenie výstupu určitým spôsobom**. Môže to byť ladenie parametrov, pokyny na formátovanie, taxonómie tém atď., ktoré môžu modelu pomôcť _prispôsobiť_ jeho odpoveď tak, aby vyhovovala požadovaným cieľom alebo očakávaniam používateľa.

Napríklad: Ak máme katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, značky metadát, inštruktor atď.) o všetkých dostupných kurzoch v učebných osnovách:

- môžeme definovať inštrukciu na "zhrnutie katalógu kurzov na jeseň 2023"
- môžeme použiť primárny obsah na poskytnutie niekoľkých príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu 5 najdôležitejších "značiek" záujmu.

Teraz môže model poskytnúť zhrnutie vo formáte ukázanom v niekoľkých príkladoch - ale ak má výsledok viacero značiek, môže uprednostniť 5 značiek identifikovaných v sekundárnom obsahu.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #1.
Posilnite koncept pomocou príkladov a odkazov.

KONCEPT #3:
Techniky inžinierstva výziev.
Aké sú základné techniky inžinierstva výziev?
Ilustrujte to pomocou cvičení.
-->

## Najlepšie postupy pri výzvach

Teraz, keď vieme, ako môžu byť výzvy _konštruované_, môžeme začať premýšľať o tom, ako ich _navrhnúť_, aby odrážali najlepšie postupy. Môžeme o tom uvažovať v dvoch častiach - mať správny _prístup_ a aplikovať správne _techniky_.

### Prístup k inžinierstvu výziev

Inžinierstvo výziev je proces pokusov a omylov, preto majte na pamäti tri široké usmerňujúce faktory:

1. **Porozumenie doméne je dôležité.** Presnosť a relevantnosť odpovede je funkciou _domény_, v ktorej tá aplikácia alebo používateľ pôsobí. Použite svoju intuíciu a odborné znalosti v doméne na **prispôsobenie techník**. Napríklad definujte _osobnosti špecifické pre doménu_ vo svojich systémových výzvach alebo použite _šablóny špecifické pre doménu_ vo svojich používateľských výzvach. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo použite _narážky a príklady špecifické pre doménu_, aby ste model nasmerovali na známe vzory používania.

2. **Porozumenie modelu je dôležité.** Vieme, že modely sú stochastické. Ale implementácie modelov sa môžu líšiť aj z hľadiska datasetu, ktorý používajú (predtrénované znalosti), schopností, ktoré poskytujú (napr. prostredníctvom API alebo SDK), a typu obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné stránky a obmedzenia modelu, ktorý používate, a použite tieto znalosti na _prioritizáciu úloh_ alebo vytvorenie _prispôsobených šablón_, ktoré sú optimalizované pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako ako techniky inžinierstva výziev. Ako odborník na doménu môžete mať iný kontext alebo kritériá pre _vašu_ konkrétnu aplikáciu, ktoré sa nemusia vzťahovať na širšiu komunitu. Použite nástroje a techniky inžinierstva výziev na "rýchly štart" konštrukcie výziev, potom iterujte a validujte výsledky pomocou vlastnej intuície a odborných znalostí v doméne. Zaznamenajte svoje poznatky a vytvorte **databázu znalostí** (napr. knižnice výziev), ktoré môžu byť použité ako nový základ pre ostatných na rýchlejšie iterácie v budúcnosti.

## Najlepšie postupy

Pozrime sa teraz na bežné najlepšie postupy, ktoré odporúčajú odborníci z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Čo                               | Prečo                                                                                                                                                                                                                                               |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vyhodnoťte najnovšie modely.     | Nové generácie modelov pravdepodobne majú vylepšené funkcie a kvalitu - ale môžu tiež priniesť vyššie náklady. Vyhodnoťte ich vplyv a potom urobte rozhodnutia o migrácii.                                                                            |
| Oddelenie inštrukcií a kontextu  | Skontrolujte, či váš model/poskytovateľ definuje _oddiely_ na jasnejšie rozlíšenie inštrukcií, primárneho a sekundárneho obsahu. To môže modelom pomôcť presnejšie priradiť váhy k tokenom.                                                         |
| Buďte konkrétny a jasný          | Poskytnite viac podrobností o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu aj konzistenciu odpovedí. Zaznamenajte recepty do opakovane použiteľných šablón.                                                          |
| Buďte popisný, používajte príklady | Modely môžu lepšie reagovať na prístup "ukáž a povedz". Začnite s prístupom `zero-shot`, kde mu dáte inštrukciu (ale žiadne príklady), potom skúste `few-shot` ako vylepšenie, poskytnutím niekoľkých príkladov požadovaného výstupu. Používajte analógie. |
| Používajte narážky na začatie odpovedí | Nasmerujte model k požadovanému výsledku tým, že mu poskytnete niekoľko úvodných slov alebo fráz, ktoré môže použiť ako východiskový bod pre odpoveď.                                                                                               |
| Zdvojnásobte                     | Niekedy je potrebné modelu zopakovať inštrukcie. Dajte inštrukcie pred a po primárnom obsahu, použite inštrukciu a narážku atď. Iterujte a validujte, aby ste zistili, čo funguje.                                                                  |
| Poradie je dôležité              | Poradie, v ktorom modelu prezentujete informácie, môže ovplyvniť výstup, dokonca aj v učebných príkladoch, vďaka zaujatosti posledných informácií. Skúšajte rôzne možnosti, aby ste zistili, čo funguje najlepšie.                                   |
| Dajte modelu "únikovú cestu"     | Poskytnite modelu _záložnú_ odpoveď, ktorú môže poskytnúť, ak z akéhokoľvek dôvodu nemôže úlohu dokončiť. To môže znížiť šance, že modely generujú nesprávne alebo vymyslené odpovede.                                                             |
|                                 |                                                                                                                                                                                                                                                   |

Ako pri každom najlepšom postupe, pamätajte, že _vaše výsledky sa môžu líšiť_ v závislosti od modelu, úlohy a domény. Použite ich ako východiskový bod a iterujte, aby ste zistili, čo funguje najlepšie pre vás. Neustále prehodnocujte svoj proces inžinierstva výziev, keď sa objavia nové modely a nástroje, so zameraním na škálovateľnosť procesu a kvalitu odpovedí.

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala poskytnúť výzvu na kód, ak je to možné.

VÝZVA:
Odkaz na Jupyter Notebook s iba komentármi kódu v inštrukciách (sekcie kódu sú prázdne).

RIEŠENIE:
Odkaz na kópiu toho Notebooku s vyplnenými a spustenými výzvami, ukazujúc, čo by mohol byť jeden príklad.
-->

## Zadanie

Gratulujeme! Dostali ste sa na koniec lekcie! Je čas otestovať niektoré z týchto konceptov a techník na skutočných príkladoch!

Pre naše zadanie budeme používať Jupyter Notebook s cvičeniami, ktoré môžete interaktívne dokončiť. Notebook môžete tiež rozšíriť o vlastné bunky Markdown a Code, aby ste mohli preskúmať vlastné nápady a techniky.

### Na začiatok, forkujte repozitár, potom

- (Odporúčané) Spustite GitHub Codespaces
- (Alternatívne) Klonujte repozitár na svoje lokálne zariadenie a použite ho s Docker Desktop
- (Alternatívne) Otvorte Notebook vo svojom preferovanom prostredí pre Notebooky.

### Ďalej, nakonfigurujte svoje environmentálne premenné

- Skopírujte súbor `.env.copy` v koreňovom adresári repozitára na `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Vráťte sa do sekcie [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby ste sa dozvedeli viac.

### Ďalej, otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x poskytovaný vývojovým kontajnerom.

Ste pripravení spustiť cvičenia. Upozorňujeme, že tu neexistujú _správne a nesprávne_ odpovede - ide len o skúmanie možností metódou pokusov a omylov a budovanie intuície pre to, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú segmenty s riešením kódu. Namiesto toho bude Notebook obsahovať bunky Markdown s názvom "Moje riešenie:", ktoré ukazujú jeden príklad výstupu na referenciu._

 <!--
ŠABLÓNA LEKCIE:
Zhrňte sekciu a poskytnite zdroje na samostatné štúdium.
-->

## Kontrola znalostí

Ktorá z nasledujúcich výziev je dobrá výzva podľa rozumných najlepších postupov?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného pri útesu so zapadajúcim slnkom
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

Odpoveď: 2, je to najlepšia výzva, pretože poskytuje detaily o "čom" a ide do špecifík (nie len akékoľvek auto, ale konkrétna značka a model) a tiež opisuje celkové prostredie. 3 je ďalšia najlepšia, pretože tiež obsahuje veľa popisu.

## 🚀 Výzva

Skúste využiť techniku "narážky" s výzvou: Dokončite vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Čo vám odpovie a ako by ste to vylepšili?

## Skvelá práca! Pokračujte vo svojom vzdelávaní

Chcete sa dozvedieť viac o rôznych konceptoch inžinierstva výziev? Navštívte [stránku ďalšieho vzdelávania](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje na túto tému.

Prejdite na Lekciu 5, kde sa pozrieme na [pokročilé techniky výziev](../05-advanced-prompts/README.md?WT.mc_id=academic-

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.