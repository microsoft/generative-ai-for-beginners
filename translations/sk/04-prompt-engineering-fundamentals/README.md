<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T10:17:20+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sk"
}
-->
# Základy tvorby promptov

[![Základy tvorby promptov](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.sk.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Úvod
Táto kapitola pokrýva základné koncepty a techniky na vytváranie efektívnych promptov pre generatívne AI modely. Spôsob, akým napíšete svoj prompt pre LLM, je dôležitý. Starostlivo vytvorený prompt môže priniesť kvalitnejšiu odpoveď. Ale čo presne znamenajú pojmy ako _prompt_ a _tvorba promptov_? A ako môžem zlepšiť _vstupný prompt_, ktorý posielam LLM? Na tieto otázky sa pokúsime odpovedať v tejto a nasledujúcej kapitole.

_Generatívna AI_ dokáže vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) na základe požiadaviek používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ (Large Language Models, LLM), ako je séria GPT ("Generative Pre-trained Transformer") od OpenAI, ktoré sú trénované na používanie prirodzeného jazyka a kódu.

Používatelia môžu teraz s týmito modelmi komunikovať prostredníctvom známych rozhraní, ako je chat, bez potreby technických znalostí alebo školení. Modely sú _založené na promptoch_ – používatelia posielajú textový vstup (prompt) a dostávajú odpoveď od AI (completion). Následne môžu "chatovať s AI" iteratívne, v rámci viackolových konverzácií, a upravovať prompt, kým odpoveď nezodpovedá ich očakávaniam.

"Prompty" sa tak stávajú primárnym _programovacím rozhraním_ pre generatívne AI aplikácie, ktoré modelom hovoria, čo majú robiť, a ovplyvňujú kvalitu vrátených odpovedí. "Tvorba promptov" je rýchlo rastúca oblasť štúdia, ktorá sa zameriava na _návrh a optimalizáciu_ promptov s cieľom dosiahnuť konzistentné a kvalitné odpovede vo veľkom rozsahu.

## Ciele učenia

V tejto lekcii sa naučíme, čo je tvorba promptov, prečo je dôležitá a ako môžeme vytvárať efektívnejšie prompty pre konkrétny model a cieľ aplikácie. Pochopíme základné koncepty a osvedčené postupy pre tvorbu promptov – a zoznámime sa s interaktívnym prostredím "sandbox" v Jupyter Notebookoch, kde si tieto koncepty môžeme vyskúšať na reálnych príkladoch.

Na konci tejto lekcie budeme schopní:

1. Vysvetliť, čo je tvorba promptov a prečo je dôležitá.
2. Opísať komponenty promptu a ich použitie.
3. Naučiť sa osvedčené postupy a techniky pre tvorbu promptov.
4. Aplikovať naučené techniky na reálne príklady pomocou OpenAI endpointu.

## Kľúčové pojmy

Tvorba promptov: Prax navrhovania a zdokonaľovania vstupov na usmernenie AI modelov k produkcii požadovaných výstupov.  
Tokenizácia: Proces konverzie textu na menšie jednotky, nazývané tokeny, ktoré model dokáže pochopiť a spracovať.  
LLM doladené na inštrukcie: Veľké jazykové modely (LLM), ktoré boli doladené pomocou špecifických inštrukcií na zlepšenie presnosti a relevantnosti odpovedí.

## Sandbox na učenie

Tvorba promptov je momentálne viac umenie ako veda. Najlepší spôsob, ako si zlepšiť intuíciu, je _viac cvičiť_ a prijať prístup pokus-omyl, ktorý kombinuje odborné znalosti z danej oblasti s odporúčanými technikami a optimalizáciami špecifickými pre model.

Jupyter Notebook, ktorý sprevádza túto lekciu, poskytuje prostredie _sandbox_, kde si môžete vyskúšať, čo sa naučíte – buď priebežne, alebo ako súčasť výzvy na konci. Na vykonanie cvičení budete potrebovať:

1. **Azure OpenAI API kľúč** – endpoint služby pre nasadený LLM.  
2. **Python runtime** – prostredie, v ktorom sa môže Notebook spustiť.  
3. **Lokálne environmentálne premenné** – _dokončite kroky [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), aby ste boli pripravení_.  

Notebook obsahuje _úvodné_ cvičenia – ale odporúčame vám pridať si vlastné sekcie _Markdown_ (popis) a _Code_ (požiadavky promptov), aby ste si mohli vyskúšať viac príkladov alebo nápadov – a budovať si intuíciu pre návrh promptov.

## Ilustrovaný sprievodca

Chcete si urobiť predstavu o tom, čo táto lekcia pokrýva, ešte predtým, než sa do nej ponoríte? Pozrite si tento ilustrovaný sprievodca, ktorý vám poskytne prehľad hlavných tém a kľúčových poznatkov, na ktoré by ste mali myslieť pri každej z nich. Plán lekcie vás prevedie od pochopenia základných konceptov a výziev až po ich riešenie pomocou relevantných techník a osvedčených postupov pre tvorbu promptov. Upozorňujeme, že sekcia "Pokročilé techniky" v tomto sprievodcovi odkazuje na obsah pokrytý v _nasledujúcej_ kapitole tohto kurzu.

![Ilustrovaný sprievodca tvorbou promptov](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.sk.png)

## Naša startupová misia

Teraz sa pozrime, ako _táto téma_ súvisí s našou startupovou misiou [priniesť AI inovácie do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať AI aplikácie pre _personalizované vzdelávanie_ – takže sa zamyslime nad tým, ako rôzni používatelia našej aplikácie môžu "navrhovať" prompty:

- **Administrátori** môžu požiadať AI, aby _analyzovala údaje o učebných osnovách a identifikovala medzery v pokrytí_. AI môže zhrnúť výsledky alebo ich vizualizovať pomocou kódu.  
- **Učitelia** môžu požiadať AI, aby _vytvorila plán hodiny pre cieľové publikum a tému_. AI môže vytvoriť personalizovaný plán v špecifikovanom formáte.  
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI môže teraz študentov viesť lekciami, nápovedami a príkladmi prispôsobenými ich úrovni.  

A to je len špička ľadovca. Pozrite si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – open-source knižnicu promptov, ktorú zostavili odborníci na vzdelávanie – aby ste získali širší prehľad o možnostiach! _Vyskúšajte spustiť niektoré z týchto promptov v sandboxe alebo v OpenAI Playground a uvidíte, čo sa stane!_

## Čo je tvorba promptov?

Túto lekciu sme začali definovaním **tvorby promptov** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) na dosiahnutie konzistentných a kvalitných odpovedí (completions) pre konkrétny cieľ aplikácie a model. Môžeme to chápať ako dvojkrokový proces:

- _navrhnutie_ počiatočného promptu pre konkrétny model a cieľ  
- _zdokonaľovanie_ promptu iteratívne na zlepšenie kvality odpovede  

Tento proces je nevyhnutne založený na pokusoch a omyloch, pričom vyžaduje intuíciu a úsilie používateľa na dosiahnutie optimálnych výsledkov. Prečo je to však dôležité? Na zodpovedanie tejto otázky musíme najprv pochopiť tri koncepty:

- _Tokenizácia_ = ako model "vidí" prompt  
- _Základné LLM_ = ako základný model "spracováva" prompt  
- _LLM doladené na inštrukcie_ = ako model teraz dokáže "vidieť úlohy"  

### Tokenizácia

LLM vidí prompty ako _sekvenciu tokenov_, pričom rôzne modely (alebo verzie modelu) môžu tokenizovať ten istý prompt rôznymi spôsobmi. Keďže LLM sú trénované na tokenoch (a nie na surovom texte), spôsob, akým sa prompty tokenizujú, má priamy vplyv na kvalitu generovanej odpovede.

Aby ste získali intuíciu o tom, ako tokenizácia funguje, vyskúšajte nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) uvedený nižšie. Skopírujte svoj prompt – a pozrite sa, ako sa konvertuje na tokeny, pričom si všímajte, ako sa spracovávajú medzery a interpunkčné znaky. Upozorňujeme, že tento príklad ukazuje starší LLM (GPT-3) – takže pri použití novšieho modelu môže byť výsledok odlišný.

![Tokenizácia](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.sk.png)

### Koncept: Základné modely

Keď je prompt tokenizovaný, primárnou funkciou ["Základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo základného modelu) je predpovedať ďalší token v tejto sekvencii. Keďže LLM sú trénované na obrovských textových datasetoch, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a dokážu túto predpoveď urobiť s určitou mierou istoty. Upozorňujeme, že nerozumejú _významu_ slov v promptoch alebo tokenoch; vidia len vzor, ktorý môžu "doplniť" svojou ďalšou predpoveďou. Môžu pokračovať v predpovedaní sekvencie, kým ich nezastaví zásah používateľa alebo nejaká prednastavená podmienka.

Chcete vidieť, ako funguje dopĺňanie na základe promptov? Zadajte vyššie uvedený prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) v Azure OpenAI Studio s predvolenými nastaveniami. Systém je nakonfigurovaný tak, aby prompty považoval za požiadavky na informácie – takže by ste mali vidieť odpoveď, ktorá vyhovuje tomuto kontextu.

Ale čo ak by používateľ chcel vidieť niečo konkrétne, čo spĺňa určité kritériá alebo cieľ úlohy? Tu prichádzajú na rad _LLM doladené na inštrukcie_.

![Základné LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.sk.png)

### Koncept: LLM doladené na inštrukcie

[LLM doladené na inštrukcie](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) začínajú základným modelom a doladia ho pomocou príkladov alebo párov vstup/výstup (napr. viackolové "správy"), ktoré môžu obsahovať jasné inštrukcie – a odpoveď AI sa pokúša tieto inštrukcie dodržať.

Používajú sa techniky ako Reinforcement Learning with Human Feedback (RLHF), ktoré dokážu model naučiť _nasledovať inštrukcie_ a _učiť sa z spätnej väzby_, aby produkoval odpovede, ktoré sú lepšie prispôsobené praktickým aplikáciám a relevantnejšie pre ciele používateľa.

Vyskúšajme si to – vráťte sa k vyššie uvedenému promptu, ale teraz zmeňte _systémovú správu_, aby poskytla nasledujúcu inštrukciu ako kontext:

> _Zhrňte obsah, ktorý vám bol poskytnutý, pre druháka. Výsledok udržte na jednom odseku s 3-5 odrážkami._

Vidíte, ako je výsledok teraz prispôsobený požadovanému cieľu a formátu? Učiteľ môže teraz priamo použiť túto odpoveď vo svojich prezentáciách pre danú triedu.

![LLM doladené na inštrukcie Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.sk.png)

## Prečo potrebujeme tvorbu promptov?

Teraz, keď vieme, ako LLM spracovávajú prompty, poďme sa porozprávať o _tom, prečo_ potrebujeme tvorbu promptov. Odpoveď spočíva v tom, že súčasné LLM predstavujú množstvo výziev, ktoré robia _spoľahlivé a konzistentné odpovede_ náročnejšími na dosiahnutie bez vynaloženia úsilia na konštrukciu a optimalizáciu promptov. Napríklad:

1. **Odpovede modelu sú stochastické.** _Ten istý prompt_ pravdepodobne vyprodukuje rôzne odpovede s rôznymi modelmi alebo verziami modelov. A môže dokonca vyprodukovať rôzne výsledky s _tým istým modelom_ v rôznych časoch. _Techniky tvorby promptov nám môžu pomôcť minimalizovať tieto variácie poskytnutím lepších mantinelov_.  

1. **Modely môžu vymýšľať odpovede.** Modely sú predtrénované na _veľkých, ale konečných_ datasetoch, čo znamená, že im chýbajú znalosti o konceptoch mimo tohto tréningového rozsahu. Výsledkom je, že môžu produkovať odpovede, ktoré sú nepresné, vymyslené alebo priamo protirečia známym faktom. _Techniky tvorby promptov pomáhajú používateľom identifikovať a zmierniť takéto výmysly, napr. požiadaním AI o citácie alebo zdôvodnenie_.  

1. **Schopnosti modelov sa líšia.** Novšie modely alebo generácie modelov budú mať bohatšie schopnosti, ale prinesú aj jedinečné zvláštnosti a kompromisy v nákladoch a zložitosti. _Tvorba promptov nám môže pomôcť vyvinúť osvedčené postupy a pracovné postupy, ktoré abstrahujú rozdiely a prispôsobujú sa požiadavkám špecifickým pre modely škálovateľným a bezproblémovým spôsobom_.  

Pozrime sa na to v praxi v OpenAI alebo Azure OpenAI Playground:

- Použite ten istý prompt s rôznymi nasadeniami LLM (napr. OpenAI, Azure OpenAI, Hugging Face) – videli ste rozdiely?  
- Použite ten istý prompt opakovane s _tým istým_ nasadením LLM (napr. Azure OpenAI Playground) – ako sa tieto variácie líšili?  

### Príklad vymýšľania

V tomto kurze používame termín **"vymýšľanie"** na označenie javu, keď LLM niekedy generujú fakticky nesprávne informácie kvôli obmedzeniam ich tréningu alebo iným faktorom. Možno ste sa s týmto javom stretli aj pod pojmom _"halucinácie"_ v populárnych článkoch alebo výskumných prácach. Odporúčame však používať termín _"vymýšľanie"_, aby sme náhodou nepripisovali ľudskú vlastnosť strojom. Tento prístup tiež podporuje [zásady zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105
Webové vyhľadávanie mi ukázalo, že existujú fiktívne príbehy (napr. televízne seriály alebo knihy) o vojnách na Marse – ale žiadne z roku 2076. Zdravý rozum nám tiež hovorí, že rok 2076 je _v budúcnosti_ a preto nemôže byť spojený so skutočnou udalosťou.

Čo sa však stane, keď tento podnet použijeme s rôznymi poskytovateľmi LLM?

> **Odpoveď 1**: OpenAI Playground (GPT-35)

![Odpoveď 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.sk.png)

> **Odpoveď 2**: Azure OpenAI Playground (GPT-35)

![Odpoveď 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.sk.png)

> **Odpoveď 3**: Hugging Face Chat Playground (LLama-2)

![Odpoveď 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.sk.png)

Ako sa dalo očakávať, každý model (alebo verzia modelu) generuje mierne odlišné odpovede vďaka stochastickému správaniu a rozdielom vo schopnostiach modelov. Napríklad jeden model sa zameriava na publikum ôsmeho ročníka, zatiaľ čo druhý predpokladá študentov strednej školy. Ale všetky tri modely vytvorili odpovede, ktoré by mohli presvedčiť neinformovaného používateľa, že udalosť bola skutočná.

Techniky navrhovania podnetov, ako je _metaprompting_ a _konfigurácia teploty_, môžu do určitej miery znížiť výmysly modelov. Nové architektúry navrhovania podnetov tiež bezproblémovo začleňujú nové nástroje a techniky do toku podnetov, aby zmiernili alebo znížili niektoré z týchto efektov.

## Prípadová štúdia: GitHub Copilot

Túto sekciu zakončíme tým, že si priblížime, ako sa navrhovanie podnetov používa v reálnych riešeniach, a to na príklade jednej prípadovej štúdie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš „AI pár programátor“ – konvertuje textové podnety na návrhy kódu a je integrovaný do vášho vývojového prostredia (napr. Visual Studio Code) pre bezproblémový používateľský zážitok. Ako je zdokumentované v sérii blogov nižšie, najskoršia verzia bola založená na modeli OpenAI Codex – pričom inžinieri rýchlo zistili potrebu doladiť model a vyvinúť lepšie techniky navrhovania podnetov na zlepšenie kvality kódu. V júli [predstavili vylepšený AI model, ktorý presahuje Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) pre ešte rýchlejšie návrhy.

Prečítajte si príspevky v poradí, aby ste sledovali ich cestu učenia.

- **Máj 2023** | [GitHub Copilot sa zlepšuje v porozumení vášho kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Máj 2023** | [V zákulisí GitHubu: Práca s LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jún 2023** | [Ako písať lepšie podnety pre GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Júl 2023** | [.. GitHub Copilot presahuje Codex s vylepšeným AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Júl 2023** | [Sprievodca vývojára k navrhovaniu podnetov a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Ako vytvoriť podnikový LLM aplikáciu: Lekcie z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Môžete si tiež prezrieť ich [technický blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pre ďalšie príspevky, ako je [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ktorý ukazuje, ako sa tieto modely a techniky _používajú_ na poháňanie aplikácií v reálnom svete.

---

## Konštrukcia podnetov

Videli sme, prečo je navrhovanie podnetov dôležité – teraz pochopme, ako sa podnety _konštruujú_, aby sme mohli vyhodnotiť rôzne techniky na efektívnejší návrh podnetov.

### Základný podnet

Začnime základným podnetom: textový vstup odoslaný modelu bez ďalšieho kontextu. Tu je príklad – keď pošleme prvé slová americkej národnej hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžite _dokončí_ odpoveď ďalšími riadkami, čím ilustruje základné prediktívne správanie.

| Podnet (Vstup)     | Dokončenie (Výstup)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Zdá sa, že začínate text piesne „The Star-Spangled Banner“, národnej hymny Spojených štátov. Celý text je ...                              |

### Komplexný podnet

Teraz pridajme kontext a pokyny k základnému podnetu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje konštruovať komplexný podnet ako kolekciu _správ_ s:

- Pármi vstup/výstup, ktoré odrážajú _používateľský_ vstup a _odpoveď asistenta_.
- Systémovou správou, ktorá nastavuje kontext pre správanie alebo osobnosť asistenta.

Požiadavka má teraz formu uvedenú nižšie, kde _tokenizácia_ efektívne zachytáva relevantné informácie z kontextu a konverzácie. Zmena systémového kontextu môže byť rovnako významná pre kvalitu dokončení ako poskytnuté používateľské vstupy.

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


### Inštrukčný podnet

V predchádzajúcich príkladoch bol používateľský podnet jednoduchým textovým dotazom, ktorý možno interpretovať ako žiadosť o informácie. Pri _inštrukčných_ podnetoch môžeme tento text použiť na špecifikáciu úlohy podrobnejšie, čím poskytneme AI lepšie usmernenie. Tu je príklad:

| Podnet (Vstup)                                                                                                                                                                                                                         | Dokončenie (Výstup)                                                                                                        | Typ inštrukcie      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napíšte opis občianskej vojny                                                                                                                                                                                                          | _vrátený jednoduchý odsek_                                                                                                | Jednoduchý          |
| Napíšte opis občianskej vojny. Uveďte kľúčové dátumy a udalosti a opíšte ich význam                                                                                                                                                     | _vrátený odsek nasledovaný zoznamom kľúčových dátumov udalostí s popismi_                                                  | Komplexný           |
| Napíšte opis občianskej vojny v 1 odseku. Uveďte 3 odrážky s kľúčovými dátumami a ich významom. Uveďte ďalšie 3 odrážky s kľúčovými historickými osobnosťami a ich príspevkami. Výstup vráťte ako JSON súbor.                              | _vrátené rozsiahlejšie detaily v textovom poli, formátované ako JSON, ktorý môžete skopírovať do súboru a overiť podľa potreby_ | Komplexný. Formátovaný. |

## Primárny obsah

V predchádzajúcich príkladoch bol podnet stále pomerne otvorený, čo umožnilo LLM rozhodnúť, ktorá časť jeho predtrénovaného datasetu je relevantná. Pri dizajnovom vzore _primárneho obsahu_ je vstupný text rozdelený na dve časti:

- inštrukciu (akciu)
- relevantný obsah (ktorý ovplyvňuje akciu)

Tu je príklad, kde inštrukcia je „zhrňte to v 2 vetách“.

| Podnet (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Dokončenie (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od nepamäti. Je pomenovaný po rímskom bohu Jupiterovi.[19] Pri pohľade zo Zeme môže byť Jupiter dostatočne jasný na to, aby jeho odrazené svetlo vrhalo viditeľné tiene,[20] a je v priemere tretím najjasnejším prirodzeným objektom na nočnej oblohe po Mesiaci a Venuši. <br/> **Zhrňte to v 2 krátkych vetách** | Jupiter, piata planéta od Slnka, je najväčšia v Slnečnej sústave a je známa ako jeden z najjasnejších objektov na nočnej oblohe. Pomenovaný po rímskom bohu Jupiterovi, je to plynný obor s hmotnosťou dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. |

Segment primárneho obsahu môže byť použitý rôznymi spôsobmi na efektívnejšie usmernenie inštrukcií:

- **Príklady** – namiesto toho, aby sme modelu explicitne povedali, čo má robiť, poskytneme mu príklady požadovaného výstupu a necháme ho odvodiť vzor.
- **Náznaky** – nasledujte inštrukciu „náznakom“, ktorý modelu poskytne podnet na relevantnejšie odpovede.
- **Šablóny** – opakovateľné „recepty“ pre podnety s premennými (miestami), ktoré môžu byť prispôsobené údajmi pre konkrétne použitia.

Preskúmajme tieto techniky v praxi.

### Používanie príkladov

Toto je prístup, kde použijete primárny obsah na „nakŕmenie modelu“ niekoľkými príkladmi požadovaného výstupu pre danú inštrukciu a necháte ho odvodiť vzor pre požadovaný výstup. Na základe počtu poskytnutých príkladov môžeme mať podnety bez príkladov, s jedným príkladom, s niekoľkými príkladmi atď.

Podnet teraz pozostáva z troch komponentov:

- Popis úlohy
- Niekoľko príkladov požadovaného výstupu
- Začiatok nového príkladu (ktorý sa stáva implicitným popisom úlohy)

| Typ učenia | Podnet (Vstup)                                                                                                                                        | Dokončenie (Výstup)         |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Bez príkladov | „The Sun is Shining“. Preložte do španielčiny                                                                                                       | „El Sol está brillando“.    |
| Jeden príklad | „The Sun is Shining“ => „El Sol está brillando“. <br> „It's a Cold and Windy Day“ =>                                                                | „Es un día frío y ventoso“. |
| Niekoľko príkladov | Hráč bežal po métach => Baseball <br/> Hráč zahral eso => Tenis <br/> Hráč zahral šestku => Kriket <br/> Hráč skóroval slam-dunk =>             | Basketbal                   |

Všimnite si, ako sme museli poskytnúť explicitnú inštrukciu („Preložte do španielčiny“) pri podnete bez príkladov, ale táto inštrukcia sa odvádza v príklade s jedným príkladom. Príklad s niekoľkými príkladmi ukazuje, ako pridanie viacerých príkladov umožňuje modelom robiť presnejšie odvodenia bez ďalších inštrukcií.

### Náznaky podnetov

Ďalšou technikou používania primárneho obsahu je poskytovanie _náznakov_ namiesto príkladov. V tomto prípade dávame modelu „nápovedu“ správnym smerom tým, že ho _naštartujeme_ úryvkom, ktorý odráža požadovaný formát odpovede. Model potom „nasleduje náznak“ a pokračuje v rovnakom duchu.

| Počet náznakov | Podnet (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dokončenie (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od nepamäti. <br/>**Zhrňte to**                                       | Jupiter je najväčšia planéta v našej Slnečnej sústave a piata od Slnka. Je to plynný obor s hmotnosťou 1/1000 hmotnosti Slnka, ale je ťažší ako všetky ostatné planéty dokopy. Staroveké civilizácie poznali Jupiter už dávno a je ľahko viditeľný na nočnej oblohe. |
| 1              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty v Slnečnej sústave dokopy. Jupiter je jeden z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od nepamäti. <br/>**Zhrňte to** <br/> Zistili sme, že Jupiter | je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty dokopy. Je ľahko viditeľný voľným okom a je známy už od staroveku.                        |
| 2              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty v Slnečnej sústave dokopy. Jupiter je jeden z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už od nepamäti. <br/>**Zhrňte to** <br/> Top 3 fakty, ktoré sme sa dozvedeli:         | 1. Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. <br/> 2. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka...<br/> 3. Jupiter je viditeľný voľným okom už od staroveku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablóny pre výzvy

Šablóna výzvy je _preddefinovaný recept na výzvu_, ktorý je možné uložiť a opakovane používať podľa potreby, aby sa dosiahla konzistentnejšia používateľská skúsenosť vo veľkom rozsahu. V najjednoduchšej forme je to jednoducho zbierka príkladov výziev, ako je [tento od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), ktorý poskytuje interaktívne komponenty výzvy (správy používateľa a systému) a formát požiadavky riadený API - na podporu opakovaného použitia.

V zložitejšej forme, ako je [tento príklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), obsahuje _zástupné symboly_, ktoré je možné nahradiť údajmi z rôznych zdrojov (vstup používateľa, kontext systému, externé zdroje údajov atď.) na dynamické generovanie výzvy. To nám umožňuje vytvoriť knižnicu opakovane použiteľných výziev, ktoré sa dajú použiť na programatické dosiahnutie konzistentných používateľských skúseností vo veľkom rozsahu.

Nakoniec, skutočná hodnota šablón spočíva v schopnosti vytvárať a publikovať _knižnice výziev_ pre vertikálne aplikačné domény - kde je šablóna výzvy teraz _optimalizovaná_ tak, aby odrážala aplikačne špecifický kontext alebo príklady, ktoré robia odpovede relevantnejšími a presnejšími pre cieľovú skupinu používateľov. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, ktorý kurátorsky zhromažďuje knižnicu výziev pre vzdelávaciu oblasť s dôrazom na kľúčové ciele, ako je plánovanie lekcií, návrh učebných osnov, doučovanie študentov atď.

## Podporný obsah

Ak uvažujeme o konštrukcii výzvy ako o úlohe (inštrukcii) a cieli (primárny obsah), potom _sekundárny obsah_ je ako dodatočný kontext, ktorý poskytujeme na **ovplyvnenie výstupu určitým spôsobom**. Môže to byť ladenie parametrov, pokyny na formátovanie, taxonómie tém atď., ktoré môžu modelu pomôcť _prispôsobiť_ jeho odpoveď tak, aby vyhovovala požadovaným cieľom alebo očakávaniam používateľa.

Napríklad: Ak máme katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, značky metadát, inštruktor atď.) o všetkých dostupných kurzoch v učebných osnovách:

- môžeme definovať inštrukciu na "zhrnutie katalógu kurzov na jeseň 2023"
- môžeme použiť primárny obsah na poskytnutie niekoľkých príkladov požadovaného výstupu
- môžeme použiť sekundárny obsah na identifikáciu top 5 "značiek" záujmu.

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

## Najlepšie praktiky pri výzvach

Teraz, keď vieme, ako môžu byť výzvy _konštruované_, môžeme začať uvažovať o tom, ako ich _navrhnúť_, aby odrážali najlepšie praktiky. Môžeme na to myslieť v dvoch častiach - mať správny _prístup_ a aplikovať správne _techniky_.

### Prístup k inžinierstvu výziev

Inžinierstvo výziev je proces pokusov a omylov, takže majte na pamäti tri široké usmerňujúce faktory:

1. **Porozumenie domény je dôležité.** Presnosť a relevantnosť odpovede je funkciou _domény_, v ktorej aplikácia alebo používateľ operuje. Použite svoju intuíciu a odborné znalosti v danej oblasti na **ďalšie prispôsobenie techník**. Napríklad definujte _osobnosti špecifické pre doménu_ vo svojich systémových výzvach alebo použite _šablóny špecifické pre doménu_ vo svojich používateľských výzvach. Poskytnite sekundárny obsah, ktorý odráža kontexty špecifické pre doménu, alebo použite _narážky a príklady špecifické pre doménu_, aby ste model nasmerovali na známe vzory používania.

2. **Porozumenie modelu je dôležité.** Vieme, že modely sú stochastické. Implementácie modelov sa však môžu líšiť z hľadiska použitého tréningového datasetu (predtrénované znalosti), poskytovaných schopností (napr. prostredníctvom API alebo SDK) a typu obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné stránky a obmedzenia modelu, ktorý používate, a použite tieto znalosti na _prioritizáciu úloh_ alebo vytvorenie _prispôsobených šablón_, ktoré sú optimalizované pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako ako techniky inžinierstva výziev. Ako odborník v danej oblasti môžete mať iný kontext alebo kritériá pre _vašu_ konkrétnu aplikáciu, ktoré sa nemusia vzťahovať na širšiu komunitu. Použite nástroje a techniky inžinierstva výziev na "štartovanie" konštrukcie výzvy, potom iterujte a validujte výsledky pomocou vlastnej intuície a odborných znalostí v danej oblasti. Zaznamenajte svoje poznatky a vytvorte **databázu znalostí** (napr. knižnice výziev), ktoré môžu byť použité ako nový základ pre ostatných na rýchlejšie iterácie v budúcnosti.

## Najlepšie praktiky

Pozrime sa teraz na bežné najlepšie praktiky, ktoré odporúčajú odborníci z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Čo                               | Prečo                                                                                                                                                                                                                                               |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vyhodnoťte najnovšie modely.     | Nové generácie modelov pravdepodobne majú vylepšené funkcie a kvalitu - ale môžu tiež priniesť vyššie náklady. Vyhodnoťte ich vplyv a potom urobte rozhodnutia o migrácii.                                                                            |
| Oddelte inštrukcie a kontext.    | Skontrolujte, či váš model/poskytovateľ definuje _oddiely_, ktoré jasnejšie odlišujú inštrukcie, primárny a sekundárny obsah. To môže modelom pomôcť presnejšie priradiť váhy k tokenom.                                                                |
| Buďte konkrétni a jasní.         | Poskytnite viac podrobností o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. To zlepší kvalitu aj konzistentnosť odpovedí. Zachyťte recepty v opakovane použiteľných šablónach.                                                           |
| Buďte popisní, používajte príklady. | Modely môžu lepšie reagovať na prístup "ukáž a povedz". Začnite s prístupom `zero-shot`, kde mu dáte inštrukciu (ale žiadne príklady), potom skúste `few-shot` ako vylepšenie, poskytnutím niekoľkých príkladov požadovaného výstupu. Používajte analógie. |
| Používajte narážky na začatie odpovedí. | Nasmerujte model na požadovaný výsledok tým, že mu poskytnete niekoľko úvodných slov alebo fráz, ktoré môže použiť ako východiskový bod pre odpoveď.                                                                                               |
| Zdvojnásobte.                    | Niekedy môže byť potrebné modelu zopakovať inštrukcie. Poskytnite inštrukcie pred a po primárnom obsahu, použite inštrukciu a narážku atď. Iterujte a validujte, aby ste zistili, čo funguje.                                                        |
| Poradie je dôležité.             | Poradie, v ktorom modelu prezentujete informácie, môže ovplyvniť výstup, dokonca aj v učebných príkladoch, vďaka zaujatosti posledných informácií. Skúšajte rôzne možnosti, aby ste zistili, čo funguje najlepšie.                                   |
| Dajte modelu "únikovú cestu".    | Poskytnite modelu _alternatívnu odpoveď_, ktorú môže poskytnúť, ak z akéhokoľvek dôvodu nemôže úlohu dokončiť. To môže znížiť šance, že modely generujú nesprávne alebo vymyslené odpovede.                                                           |
|                                 |                                                                                                                                                                                                                                                     |

Ako pri každej najlepšej praxi, pamätajte, že _vaše výsledky sa môžu líšiť_ v závislosti od modelu, úlohy a domény. Použite ich ako východiskový bod a iterujte, aby ste zistili, čo funguje najlepšie pre vás. Neustále prehodnocujte svoj proces inžinierstva výziev, keď sa objavia nové modely a nástroje, so zameraním na škálovateľnosť procesu a kvalitu odpovedí.

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala poskytnúť výzvu na kód, ak je to možné.

VÝZVA:
Odkaz na Jupyter Notebook s iba komentármi kódu v inštrukciách (sekcie kódu sú prázdne).

RIEŠENIE:
Odkaz na kópiu toho Notebooku s vyplnenými a spustenými výzvami, ukazujúci, čo by mohol byť jeden príklad.
-->

## Zadanie

Gratulujeme! Dostali ste sa na koniec lekcie! Je čas vyskúšať niektoré z týchto konceptov a techník na reálnych príkladoch!

Pre naše zadanie budeme používať Jupyter Notebook s cvičeniami, ktoré môžete interaktívne dokončiť. Notebook môžete tiež rozšíriť o vlastné bunky Markdown a Code, aby ste mohli sami preskúmať nápady a techniky.

### Na začiatok, forkujte repozitár, potom

- (Odporúčané) Spustite GitHub Codespaces
- (Alternatívne) Klonujte repozitár na svoje lokálne zariadenie a použite ho s Docker Desktop
- (Alternatívne) Otvorte Notebook vo svojom preferovanom prostredí pre Notebooky.

### Ďalej, nakonfigurujte svoje environmentálne premenné

- Skopírujte súbor `.env.copy` v koreňovom adresári repozitára na `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Vráťte sa do sekcie [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby ste sa dozvedeli viac.

### Ďalej, otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x poskytovaný vývojovým kontajnerom.

Ste pripravení spustiť cvičenia. Upozorňujeme, že tu neexistujú _správne a nesprávne_ odpovede - ide len o skúmanie možností metódou pokusov a omylov a budovanie intuície o tom, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú segmenty Code Solution. Namiesto toho bude Notebook obsahovať bunky Markdown s názvom "My Solution:", ktoré ukazujú jeden príklad výstupu na referenciu._

 <!--
ŠABLÓNA LEKCIE:
Zhrňte sekciu a poskytnite zdroje na samostatné učenie.
-->

## Kontrola znalostí

Ktorá z nasledujúcich výziev je dobrá výzva podľa niektorých rozumných najlepších praktík?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90 zaparkovaného pri útesu so zapadajúcim slnkom
3. Ukáž mi obrázok červeného auta značky Volvo a modelu XC90

Odpoveď: 2, je to najlepšia výzva, pretože poskytuje detaily o "čom" a ide do špecifík (nielen akékoľvek auto, ale konkrétnu značku a model) a tiež opisuje celkové prostredie. 3 je ďalšia najlepšia, pretože tiež obsahuje veľa popisu.

## 🚀 Výzva

Skúste využiť techniku "narážky" s výzvou: Dokončite vetu "Ukáž mi obrázok červeného auta značky Volvo a ". Čo odpovie, a ako by ste to vylepšili?

## Skvelá práca! Pokračujte vo svojom učení

Chcete sa dozvedieť viac o rôznych konceptoch inžinierstva výziev? Prejdite na [stránku pokračujúceho učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje na túto tému.

Prejdite na Lekciu 5, kde sa pozrieme na [pokročilé techniky výziev](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.