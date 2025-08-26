<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcbaaae026cb50fee071e690685b5843",
  "translation_date": "2025-08-26T19:07:43+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "sk"
}
-->
# Základy Prompt Engineeringu

[![Prompt Engineering Fundamentals](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.sk.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Úvod
Tento modul sa venuje základným pojmom a technikám na vytváranie efektívnych promptov pre generatívne AI modely. Záleží aj na tom, ako svoj prompt pre LLM napíšete. Dobre premyslený prompt môže viesť k lepšej kvalite odpovede. Ale čo presne znamenajú pojmy ako _prompt_ a _prompt engineering_? A ako môžem zlepšiť _vstupný prompt_, ktorý posielam LLM? Na tieto otázky sa pokúsime odpovedať v tejto a nasledujúcej kapitole.

_Generatívna AI_ dokáže vytvárať nový obsah (napr. text, obrázky, zvuk, kód atď.) na základe požiadaviek používateľa. Dosahuje to pomocou _veľkých jazykových modelov_ ako je séria GPT ("Generative Pre-trained Transformer") od OpenAI, ktoré sú trénované na prácu s prirodzeným jazykom a kódom.

Používatelia môžu s týmito modelmi komunikovať cez známe rozhrania ako chat, bez potreby technických znalostí či školení. Modely sú _prompt-based_ – používateľ pošle textový vstup (prompt) a dostane AI odpoveď (completion). Môže potom s AI viesť iteratívny "rozhovor", v niekoľkých krokoch prompt upravovať, kým odpoveď nezodpovedá jeho očakávaniam.

"Prompt" sa tak stáva hlavným _programovacím rozhraním_ pre generatívne AI aplikácie, určuje, čo má model robiť a ovplyvňuje kvalitu odpovedí. "Prompt Engineering" je rýchlo rastúca oblasť, ktorá sa zameriava na _návrh a optimalizáciu_ promptov, aby boli odpovede konzistentné a kvalitné vo veľkom rozsahu.

## Ciele lekcie

V tejto lekcii sa naučíme, čo je Prompt Engineering, prečo je dôležitý a ako môžeme vytvárať efektívnejšie prompty pre konkrétny model a cieľ aplikácie. Pochopíme základné pojmy a odporúčané postupy pre prompt engineering – a zoznámime sa s interaktívnym prostredím Jupyter Notebooks "sandbox", kde si tieto koncepty vyskúšame na reálnych príkladoch.

Na konci tejto lekcie budeme vedieť:

1. Vysvetliť, čo je prompt engineering a prečo je dôležitý.
2. Opísať z čoho sa skladá prompt a ako sa jednotlivé časti používajú.
3. Naučiť sa najlepšie postupy a techniky pre prompt engineering.
4. Aplikovať naučené techniky na reálnych príkladoch pomocou OpenAI endpointu.

## Kľúčové pojmy

Prompt Engineering: Prax navrhovania a vylepšovania vstupov, ktoré vedú AI modely k požadovaným výstupom.
Tokenizácia: Proces rozdelenia textu na menšie jednotky, tzv. tokeny, ktoré model dokáže spracovať a pochopiť.
Instruction-Tuned LLMs: Veľké jazykové modely (LLM), ktoré boli doladené špecifickými inštrukciami na zlepšenie presnosti a relevantnosti odpovedí.

## Učebný sandbox

Prompt engineering je zatiaľ skôr umenie než veda. Najlepší spôsob, ako si naň vybudovať cit, je _veľa trénovať_ a skúšať metódu pokus-omyl, ktorá kombinuje znalosti z danej oblasti s odporúčanými technikami a optimalizáciami pre konkrétny model.

Jupyter Notebook, ktorý túto lekciu sprevádza, poskytuje _sandbox_ prostredie, kde si môžete všetko vyskúšať – priebežne alebo v rámci záverečnej úlohy. Na spustenie cvičení budete potrebovať:

1. **Azure OpenAI API kľúč** – endpoint služby s nasadeným LLM.
2. **Python runtime** – prostredie, v ktorom notebook spustíte.
3. **Lokálne environmentálne premenné** – _dokončite teraz kroky v [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), aby ste boli pripravení_.

Notebook obsahuje _úvodné_ cvičenia – ale odporúčame vám pridať si vlastné sekcie _Markdown_ (popis) a _Code_ (prompt požiadavky), aby ste si vyskúšali ďalšie príklady alebo nápady – a vybudovali si cit pre návrh promptov.

## Ilustrovaný sprievodca

Chcete si najprv urobiť prehľad, čo táto lekcia pokrýva? Pozrite si tento ilustrovaný sprievodca, ktorý vám ukáže hlavné témy a kľúčové poznatky, na ktoré sa v každej z nich zamerať. Cesta lekciou vás prevedie od pochopenia základných pojmov a výziev až po ich riešenie pomocou relevantných techník a odporúčaných postupov prompt engineeringu. Upozorňujeme, že sekcia "Pokročilé techniky" v tomto sprievodcovi odkazuje na obsah, ktorý bude pokrytý v _nasledujúcej_ kapitole tohto kurzu.

![Ilustrovaný sprievodca Prompt Engineeringom](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.sk.png)

## Náš startup

Poďme sa teraz pozrieť, ako _táto téma_ súvisí s naším startupovým cieľom [priniesť AI inovácie do vzdelávania](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chceme vytvárať AI aplikácie pre _personalizované vzdelávanie_ – zamyslime sa teda, ako by rôzni používatelia našej aplikácie mohli "navrhovať" prompty:

- **Administrátori** môžu požiadať AI, aby _analyzovala dáta o učebných osnovách a identifikovala medzery v pokrytí_. AI môže výsledky zhrnúť alebo vizualizovať pomocou kódu.
- **Učitelia** môžu požiadať AI, aby _vytvorila plán hodiny pre konkrétnu cieľovú skupinu a tému_. AI pripraví personalizovaný plán v požadovanom formáte.
- **Študenti** môžu požiadať AI, aby ich _doučovala v náročnom predmete_. AI ich môže viesť lekciami, tipmi a príkladmi prispôsobenými ich úrovni.

To je len špička ľadovca. Pozrite si [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – open-source knižnicu promptov zostavenú odborníkmi na vzdelávanie – a získajte širší prehľad o možnostiach! _Vyskúšajte niektoré z týchto promptov v sandboxe alebo v OpenAI Playground a sledujte, čo sa stane!_

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný pojem #1.
Podporte pojem príkladmi a odkazmi.

POJEM #1:
Prompt Engineering.
Definujte ho a vysvetlite, prečo je potrebný.
-->

## Čo je Prompt Engineering?

Túto lekciu sme začali definovaním **Prompt Engineeringu** ako procesu _navrhovania a optimalizácie_ textových vstupov (promptov) s cieľom dosiahnuť konzistentné a kvalitné odpovede (completions) pre konkrétny cieľ aplikácie a model. Môžeme si to predstaviť ako dvojkrokový proces:

- _navrhnutie_ počiatočného promptu pre daný model a cieľ
- _postupné vylepšovanie_ promptu, aby sa zlepšila kvalita odpovede

Je to nevyhnutne proces pokus-omyl, ktorý vyžaduje intuíciu a úsilie používateľa na dosiahnutie optimálnych výsledkov. Prečo je to dôležité? Aby sme na to odpovedali, musíme najprv pochopiť tri pojmy:

- _Tokenizácia_ = ako model "vidí" prompt
- _Základné LLM_ = ako základný model "spracováva" prompt
- _Instruction-Tuned LLMs_ = ako model dokáže vnímať "úlohy"

### Tokenizácia

LLM vníma prompty ako _sekvenciu tokenov_, pričom rôzne modely (alebo ich verzie) môžu ten istý prompt tokenizovať rôzne. Keďže LLM sú trénované na tokenoch (nie na surovom texte), spôsob tokenizácie promptu priamo ovplyvňuje kvalitu vygenerovanej odpovede.

Aby ste získali predstavu, ako tokenizácia funguje, vyskúšajte nástroje ako [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) zobrazený nižšie. Skopírujte svoj prompt – a sledujte, ako sa rozdelí na tokeny, pričom si všímajte, ako sa spracúvajú medzery a interpunkcia. Upozorňujeme, že tento príklad ukazuje starší LLM (GPT-3) – pri novšom modeli môžu byť výsledky iné.

![Tokenizácia](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.sk.png)

### Pojem: Základné modely

Keď je prompt tokenizovaný, hlavnou úlohou ["základného LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (alebo Foundation modelu) je predpovedať ďalší token v sekvencii. Keďže LLM sú trénované na obrovských textových datasetoch, majú dobrý prehľad o štatistických vzťahoch medzi tokenmi a dokážu túto predikciu urobiť s určitou istotou. Neznamená to však, že rozumejú _významu_ slov v promptoch alebo tokenoch; vnímajú len vzory, ktoré dokážu "doplniť" ďalšou predikciou. Môžu pokračovať v predikcii sekvencie, kým ich nezastaví používateľ alebo nejaká vopred stanovená podmienka.

Chcete vidieť, ako funguje prompt-based completion? Zadajte vyššie uvedený prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) s predvolenými nastaveniami. Systém je nastavený tak, aby prompty vnímal ako žiadosti o informácie – mali by ste teda dostať odpoveď, ktorá zodpovedá tomuto kontextu.

Čo ak však používateľ chce niečo konkrétne, čo spĺňa určité kritériá alebo cieľ úlohy? Tu prichádzajú na rad _instruction-tuned_ LLM.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.sk.png)

### Pojem: Instruction Tuned LLMs

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) vychádza zo základného modelu a dolaďuje sa pomocou príkladov alebo párov vstup/výstup (napr. viacotáčkové "správy"), ktoré môžu obsahovať jasné inštrukcie – a AI sa snaží tieto inštrukcie splniť.

Používajú sa na to techniky ako Reinforcement Learning with Human Feedback (RLHF), ktoré model trénujú _nasledovať inštrukcie_ a _učiť sa zo spätnej väzby_, aby odpovede boli vhodnejšie pre praktické použitie a relevantnejšie pre ciele používateľa.

Vyskúšajme si to – použite vyššie uvedený prompt, ale teraz zmeňte _system message_ a zadajte nasledujúcu inštrukciu ako kontext:

> _Zhrň obsah, ktorý dostaneš, pre druháka na základnej škole. Výsledok nech je jeden odsek s 3-5 odrážkami._

Vidíte, ako je výsledok teraz prispôsobený požadovanému cieľu a formátu? Učiteľ môže túto odpoveď priamo použiť vo svojich slidoch pre danú triedu.

![Instruction Tuned LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.sk.png)

## Prečo potrebujeme Prompt Engineering?

Keď už vieme, ako LLM spracúvajú prompty, poďme sa pozrieť _prečo_ prompt engineering potrebujeme. Odpoveď spočíva v tom, že súčasné LLM prinášajú viacero výziev, ktoré sťažujú dosiahnutie _spoľahlivých a konzistentných odpovedí_ bez toho, aby sme venovali úsilie návrhu a optimalizácii promptov. Napríklad:

1. **Odpovede modelu sú stochastické.** _Ten istý prompt_ pravdepodobne vyprodukuje rôzne odpovede pri rôznych modeloch alebo verziách modelu. A dokonca aj pri _tom istom modeli_ v rôznych časoch môžu byť výsledky odlišné. _Techniky prompt engineeringu nám môžu pomôcť tieto rozdiely minimalizovať lepším nastavením promptov._

1. **Modely môžu vymýšľať odpovede.** Modely sú predtrénované na _veľkých, ale konečných_ datasetoch, takže im chýbajú znalosti o témach mimo tohto rozsahu. Výsledkom môžu byť odpovede, ktoré sú nepresné, vymyslené alebo priamo protirečia známym faktom. _Prompt engineering techniky pomáhajú používateľom takéto výmysly odhaliť a zmierniť, napríklad žiadosťou o citácie alebo vysvetlenie._

1. **Schopnosti modelov sa líšia.** Novšie modely alebo generácie modelov majú bohatšie možnosti, ale prinášajú aj špecifické zvláštnosti a kompromisy v cene a zložitosti. _Prompt engineering nám umožňuje vytvárať odporúčané postupy a workflowy, ktoré abstrahujú rozdiely a prispôsobujú sa špecifikám modelov škálovateľným a plynulým spôsobom._

Vyskúšajte si to v OpenAI alebo Azure OpenAI Playground:

- Použite ten istý prompt s rôznymi LLM nasadeniami (napr. OpenAI, Azure OpenAI, Hugging Face) – všimli ste si rozdiely?
- Použite ten istý prompt opakovane s _tým istým_ LLM nasadením (napr. Azure OpenAI playground) – ako sa líšili tieto odpovede?

### Príklad fabrikácie

V tomto kurze používame pojem **"fabrikácia"** na označenie javu, keď LLM niekedy generujú fakticky nesprávne informácie v dôsledku obmedzení v trénovaní alebo iných faktorov. Možno ste sa s tým stretli aj pod pojmom _"halucinácie"_ v populárnych článkoch alebo vedeckých prácach. Odporúčame však používať pojem _"fabrikácia"_, aby sme nepripisovali stroju ľudské vlastnosti. Zároveň to podporuje [zásady zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aj z hľadiska terminológie, keďže niektoré výrazy môžu byť v určitých kontextoch považované za nevhodné alebo vylučujúce.

Chcete vidieť, ako fabrikácie fungujú? Skúste prompt, ktorý AI inštruuje vygenerovať obsah na neexistujúcu tému (aby ste mali istotu, že sa v trénovacom datasete nenachádza). Napríklad – ja som vyskúšal tento prompt:
> **Výzva:** vytvorte plán hodiny o Marťanskej vojne v roku 2076.

# Plán hodiny: Marťanská vojna v roku 2076

## Ciele hodiny
- Študenti pochopia hlavné príčiny a dôsledky Marťanskej vojny v roku 2076.
- Študenti budú schopní identifikovať kľúčové postavy, udalosti a technológie spojené s konfliktom.
- Študenti budú diskutovať o vplyve vojny na vzťahy medzi Zemou a Marsom.

## Úvod (10 minút)
- Stručné predstavenie Marťanskej vojny v roku 2076.
- Diskusia: Prečo by mohlo dôjsť ku konfliktu medzi Marsom a Zemou?
- Otázka pre triedu: Aké faktory by mohli viesť k vojne medzi dvoma planétami?

## Hlavná časť (30 minút)

### 1. Príčiny vojny
- Politické napätie medzi kolóniami na Marse a vládou na Zemi.
- Súťaž o zdroje, technológie a nezávislosť.
- Vývoj nových zbraní a obranných systémov.

### 2. Priebeh konfliktu
- Hlavné bitky: Bitka o Olympus Mons, obliehanie kolónie New Horizon.
- Kľúčové postavy: generál Li Wei, prezidentka Marsu Sofia Torres.
- Použitie pokročilých technológií: robotické jednotky, orbitálne zbrane.

### 3. Dôsledky vojny
- Straty na životoch a materiálne škody.
- Zmena politickej mapy: vznik nezávislého Marťanského štátu.
- Dlhodobý vplyv na obchod, diplomaciu a vedecký výskum.

## Aktivita (15 minút)
- Rozdeľte študentov do skupín.
- Každá skupina vytvorí krátku prezentáciu o jednej z hlavných udalostí vojny.
- Prezentácie pred triedou, diskusia o rôznych pohľadoch na konflikt.

## Záver (5 minút)
- Zhrnutie hlavných bodov hodiny.
- Otvorená diskusia: Mohla sa vojna zabrániť? Aké ponaučenia si môžeme vziať do budúcnosti?
- Domáca úloha: Napíšte krátku esej o tom, ako by ste riešili napätie medzi Marsom a Zemou.

## Materiály
- Mapy Marsu a kolónií
- Prehľad kľúčových postáv a technológií
- Chronológia udalostí Marťanskej vojny v roku 2076

## Poznámky pre učiteľa
- Povzbudzujte študentov, aby premýšľali kriticky o príčinách a dôsledkoch vojny.
- Pripomínajte, že ide o fiktívny konflikt, ale témy sú relevantné aj pre skutočné medzinárodné vzťahy.
Webové vyhľadávanie mi ukázalo, že existujú fiktívne diela (napr. televízne seriály alebo knihy) o vojnách na Marse – ale žiadne z roku 2076. Zdravý rozum nám tiež hovorí, že rok 2076 je _v budúcnosti_ a teda nemôže byť spojený so skutočnou udalosťou.

Čo sa teda stane, keď tento prompt zadáme rôznym poskytovateľom LLM?

> **Odpoveď 1**: OpenAI Playground (GPT-35)

![Odpoveď 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.sk.png)

> **Odpoveď 2**: Azure OpenAI Playground (GPT-35)

![Odpoveď 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.sk.png)

> **Odpoveď 3**: Hugging Face Chat Playground (LLama-2)

![Odpoveď 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.sk.png)

Ako sa dalo čakať, každý model (alebo verzia modelu) generuje mierne odlišné odpovede vďaka stochastickému správaniu a rozdielom vo schopnostiach modelov. Napríklad jeden model cieli na žiakov 8. ročníka, zatiaľ čo iný predpokladá stredoškoláka. Všetky tri modely však vytvorili odpovede, ktoré by mohli neinformovaného používateľa presvedčiť, že udalosť bola skutočná.

Techniky prompt engineeringu ako _metaprompting_ a _nastavenie teploty_ môžu do určitej miery znížiť výskyt vymyslených odpovedí modelu. Nové _architektúry_ prompt engineeringu tiež plynulo začleňujú nové nástroje a techniky do promptov, aby zmiernili alebo znížili niektoré z týchto efektov.

## Prípadová štúdia: GitHub Copilot

Túto časť uzavrieme pohľadom na to, ako sa prompt engineering využíva v reálnych riešeniach na príklade jednej prípadovej štúdie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot je váš „AI párový programátor“ – prevádza textové prompty na doplnenia kódu a je integrovaný priamo do vášho vývojového prostredia (napr. Visual Studio Code) pre plynulý používateľský zážitok. Ako je zdokumentované v sérii blogov nižšie, najskoršia verzia bola založená na modeli OpenAI Codex – inžinieri však rýchlo zistili potrebu model doladiť a vyvinúť lepšie techniky prompt engineeringu na zlepšenie kvality kódu. V júli [predstavili vylepšený AI model, ktorý ide nad rámec Codexu](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) a ponúka ešte rýchlejšie návrhy.

Prečítajte si príspevky v poradí, aby ste sledovali ich cestu učenia.

- **Máj 2023** | [GitHub Copilot je čoraz lepší v porozumení vášho kódu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Máj 2023** | [Inside GitHub: Práca s LLM za GitHub Copilotom](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jún 2023** | [Ako písať lepšie prompty pre GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Júl 2023** | [.. GitHub Copilot ide nad rámec Codexu s vylepšeným AI modelom](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Júl 2023** | [Sprievodca vývojára prompt engineeringom a LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Ako postaviť podnikový LLM app: Lekcie z GitHub Copilota](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Môžete si tiež prezrieť ich [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) pre ďalšie príspevky ako [tento](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), ktorý ukazuje, ako sa tieto modely a techniky _používajú_ pri vývoji reálnych aplikácií.

---

## Konštrukcia promptov

Videli sme, prečo je prompt engineering dôležitý – teraz si vysvetlíme, ako sa prompty _vytvárajú_, aby sme mohli posúdiť rôzne techniky pre efektívnejší návrh promptov.

### Základný prompt

Začnime základným promptom: textový vstup, ktorý sa pošle modelu bez ďalšieho kontextu. Tu je príklad – keď pošleme prvé slová americkej štátnej hymny do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), okamžite _dokončí_ odpoveď ďalšími riadkami, čo ilustruje základné predikčné správanie.

| Prompt (Vstup)     | Doplnenie (Výstup)                                                                                                                        |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Vyzerá to, že začínate text hymny „The Star-Spangled Banner“, štátnej hymny Spojených štátov. Celý text je ... |

### Komplexný prompt

Teraz pridajme k základnému promptu kontext a inštrukcie. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nám umožňuje vytvoriť komplexný prompt ako kolekciu _správ_ s:

- dvojicami vstup/výstup, ktoré odrážajú _používateľský_ vstup a _odpoveď asistenta_
- systémovou správou, ktorá nastavuje kontext pre správanie alebo osobnosť asistenta

Požiadavka má teraz tvar nižšie, kde _tokenizácia_ efektívne zachytáva relevantné informácie z kontextu a konverzácie. Zmena systémového kontextu môže mať na kvalitu odpovedí rovnako veľký vplyv ako samotné používateľské vstupy.

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

V predchádzajúcich príkladoch bol prompt jednoduchý textový dopyt, ktorý sa dá chápať ako žiadosť o informáciu. Pri _inštrukčných_ promptoch môžeme tento text použiť na podrobnejšie zadanie úlohy a poskytnúť AI lepšie usmernenie. Tu je príklad:

| Prompt (Vstup)                                                                                                                                                                                                                         | Doplnenie (Výstup)                                                                                                        | Typ inštrukcie      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :------------------ |
| Napíš opis občianskej vojny                                                                                                                                                                     | _vrátil jednoduchý odsek_                                                                                                 | Jednoduchý          |
| Napíš opis občianskej vojny. Uveď kľúčové dátumy a udalosti a popíš ich význam                                                                                                                  | _vrátil odsek a zoznam kľúčových dátumov s popismi_                                                                       | Komplexný           |
| Napíš opis občianskej vojny v 1 odseku. Uveď 3 odrážky s kľúčovými dátumami a ich významom. Uveď ďalšie 3 odrážky s kľúčovými historickými osobnosťami a ich prínosom. Výstup vráť ako JSON súbor | _vrátil rozsiahlejšie detaily v textovom poli, naformátované ako JSON, ktorý môžete skopírovať do súboru a validovať_      | Komplexný. Formátovaný. |

## Primárny obsah

V predchádzajúcich príkladoch bol prompt stále pomerne otvorený a nechával na LLM, aby rozhodlo, ktorá časť jeho predtrénovaného datasetu je relevantná. Pri návrhovom vzore _primárny obsah_ je vstup rozdelený na dve časti:

- inštrukcia (akcia)
- relevantný obsah (ktorý ovplyvňuje akciu)

Tu je príklad, kde inštrukcia znie „zhrň toto v 2 vetách“.

| Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Doplnenie (Výstup)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisícinu hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred začiatkom písanej histórie. Je pomenovaný po rímskom bohovi Jupiterovi.[19] Pri pohľade zo Zeme môže byť Jupiter dostatočne jasný na to, aby jeho odrazené svetlo vrhalo viditeľné tiene,[20] a v priemere je tretím najjasnejším prirodzeným objektom na nočnej oblohe po Mesiaci a Venuši. <br/> **Zhrň toto v 2 krátkych vetách** | Jupiter, piata planéta od Slnka, je najväčšia v Slnečnej sústave a patrí medzi najjasnejšie objekty na nočnej oblohe. Je pomenovaný po rímskom bohovi Jupiterovi a je to plynný obor, ktorého hmotnosť je dva a pol krát väčšia ako všetky ostatné planéty dokopy. |

Segment primárneho obsahu sa dá využiť rôznymi spôsobmi na efektívnejšie zadávanie inštrukcií:

- **Príklady** – namiesto explicitnej inštrukcie modelu, čo má robiť, mu dáte príklady požadovaného výstupu a necháte ho odvodiť vzor.
- **Nápovedy** – za inštrukciu pridáte „nápovedu“, ktorá navnadí doplnenie a nasmeruje model k relevantnejšej odpovedi.
- **Šablóny** – opakovateľné „recepty“ na prompty s premennými, ktoré môžete prispôsobiť konkrétnym dátam a prípadom použitia.

Poďme si to ukázať v praxi.

### Použitie príkladov

Tento prístup spočíva v tom, že modelu „naservírujete“ v primárnom obsahu niekoľko príkladov požadovaného výstupu pre danú inštrukciu a necháte ho odvodiť vzor požadovaného výstupu. Podľa počtu poskytnutých príkladov rozlišujeme zero-shot prompting, one-shot prompting, few-shot prompting atď.

Prompt teraz pozostáva z troch častí:

- Popis úlohy
- Niekoľko príkladov požadovaného výstupu
- Začiatok nového príkladu (ktorý sa stáva implicitným popisom úlohy)

| Typ učenia | Prompt (Vstup)                                                                                                                                        | Doplnenie (Výstup)         |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- |
| Zero-shot  | "The Sun is Shining". Prelož do španielčiny                                                                                                          | "El Sol está brillando".   |
| One-shot   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso".|
| Few-shot   | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                 |
|            |                                                                                                                                                       |                            |

Všimnite si, že pri zero-shot promptingu sme museli poskytnúť explicitnú inštrukciu („Prelož do španielčiny“), ale pri one-shot promptingu sa už inštrukcia odvodí z príkladu. Few-shot príklad ukazuje, že pridaním ďalších príkladov dokážu modely presnejšie odvodiť vzor aj bez ďalších inštrukcií.

### Nápovedy v promptoch

Ďalšou technikou využitia primárneho obsahu je poskytnúť _nápovedy_ namiesto príkladov. V tomto prípade modelu jemne naznačíte požadovaný formát odpovede tým, že _začnete_ odpoveď krátkym úryvkom v požadovanom štýle. Model potom „chytí nápovedu“ a pokračuje v rovnakom duchu.

| Počet nápoved | Prompt (Vstup)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Doplnenie (Výstup)                                                                                                                                                                                                                                                                                       |
| :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0             | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisícinu hmotnosti Slnka, ale dva a pol krát väčšou ako všetky ostatné planéty Slnečnej sústavy dokopy. Jupiter je jedným z najjasnejších objektov viditeľných voľným okom na nočnej oblohe a je známy starovekým civilizáciám už pred začiatkom písanej histórie.

**Zhrňte to**                                       | Jupiter je najväčšia planéta v našej Slnečnej sústave a piata od Slnka. Je to plynný obor s hmotnosťou 1/1000 hmotnosti Slnka, ale je ťažšia ako všetky ostatné planéty dokopy. Staroveké civilizácie poznali Jupiter už dávno a je ľahko viditeľný na nočnej oblohe. |
| 1              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát ťažšia ako všetky ostatné planéty dokopy. Jupiter patrí medzi najjasnejšie objekty viditeľné voľným okom na nočnej oblohe a je známy už od čias pred písanou históriou. <br/>**Zhrňte to** <br/> Čo sme sa dozvedeli je, že Jupiter | je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát ťažšia ako všetky ostatné planéty dokopy. Je ľahko viditeľná voľným okom a známa už od staroveku.                        |
| 2              | Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka, ale dva a pol krát ťažšia ako všetky ostatné planéty dokopy. Jupiter patrí medzi najjasnejšie objekty viditeľné voľným okom na nočnej oblohe a je známy už od čias pred písanou históriou. <br/>**Zhrňte to** <br/> Top 3 fakty, ktoré sme sa dozvedeli:         | 1. Jupiter je piata planéta od Slnka a najväčšia v Slnečnej sústave. <br/> 2. Je to plynný obor s hmotnosťou tisíciny hmotnosti Slnka...<br/> 3. Jupiter je viditeľný voľným okom už od staroveku ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Šablóny promptov

Šablóna promptu je _preddefinovaný recept na prompt_, ktorý sa dá uložiť a opakovane používať podľa potreby, aby sa dosiahla konzistentnejšia používateľská skúsenosť vo väčšom rozsahu. V najjednoduchšej podobe je to zbierka príkladov promptov ako [tento od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), ktorý poskytuje interaktívne komponenty promptu (správy používateľa a systému) aj formát požiadavky pre API - na podporu opakovaného použitia.

V zložitejšej podobe, ako [tento príklad od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), obsahuje _zástupné znaky_, ktoré sa dajú nahradiť údajmi z rôznych zdrojov (vstup používateľa, systémový kontext, externé zdroje údajov atď.) na dynamické generovanie promptu. To nám umožňuje vytvárať knižnicu opakovane použiteľných promptov, ktoré sa dajú programovo využívať vo veľkom rozsahu.

Skutočná hodnota šablón spočíva v možnosti vytvárať a publikovať _knižnice promptov_ pre konkrétne aplikačné oblasti – kde je šablóna promptu _optimalizovaná_ tak, aby odrážala špecifický kontext aplikácie alebo príklady, ktoré robia odpovede relevantnejšími a presnejšími pre cieľovú skupinu používateľov. Repozitár [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) je skvelým príkladom tohto prístupu, kde sa kurátorsky zhromažďuje knižnica promptov pre vzdelávací sektor s dôrazom na kľúčové ciele ako plánovanie lekcií, tvorba učebných osnov, doučovanie študentov a pod.

## Podporný obsah

Ak si predstavíme tvorbu promptu ako zadanie úlohy (inštrukcie) a cieľ (primárny obsah), potom _sekundárny obsah_ je dodatočný kontext, ktorý poskytujeme, aby sme **nejakým spôsobom ovplyvnili výstup**. Môže ísť o parametre ladenia, pokyny na formátovanie, tematické taxonómie atď., ktoré pomáhajú modelu _prispôsobiť_ odpoveď požadovaným cieľom alebo očakávaniam používateľa.

Napríklad: Ak máme katalóg kurzov s rozsiahlymi metadátami (názov, popis, úroveň, značky, lektor atď.) o všetkých dostupných kurzoch v učebných osnovách:

- môžeme zadať inštrukciu „zhrň katalóg kurzov na jeseň 2023“
- ako primárny obsah môžeme poskytnúť niekoľko príkladov požadovaného výstupu
- sekundárny obsah môžeme použiť na identifikáciu top 5 „značiek“, ktoré nás zaujímajú

Model potom poskytne zhrnutie vo formáte podľa príkladov – ale ak má výsledok viacero značiek, uprednostní tých 5 identifikovaných v sekundárnom obsahu.

---

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala pokrývať základný koncept #1.
Posilnite koncept príkladmi a odkazmi.

KONCEPT #3:
Techniky prompt engineeringu.
Aké sú základné techniky prompt engineeringu?
Ukážte to na cvičeniach.
-->

## Najlepšie postupy pri promptovaní

Keď už vieme, ako sa dajú prompty _vytvárať_, môžeme začať premýšľať nad tým, ako ich _navrhovať_ podľa najlepších postupov. Môžeme to rozdeliť na dve časti – správne _nastavenie mysle_ a použitie správnych _techník_.

### Nastavenie mysle pri prompt engineeringu

Prompt engineering je proces pokusov a omylov, preto majte na pamäti tri hlavné faktory:

1. **Porozumenie doméne je dôležité.** Presnosť a relevantnosť odpovede závisí od _domény_, v ktorej aplikácia alebo používateľ pôsobí. Využite svoju intuíciu a odborné znalosti na **prispôsobenie techník**. Napríklad definujte _doménovo špecifické osobnosti_ vo vašich systémových promptoch, alebo použite _doménovo špecifické šablóny_ vo vašich používateľských promptoch. Poskytnite sekundárny obsah, ktorý odráža kontext domény, alebo použite _doménovo špecifické nápovedy a príklady_, aby ste model nasmerovali k známym vzorom použitia.

2. **Porozumenie modelu je dôležité.** Vieme, že modely sú zo svojej podstaty stochastické. Ale implementácie modelov sa môžu líšiť v použitých trénovacích dátach (predtrénované znalosti), v poskytovaných možnostiach (napr. cez API alebo SDK) a v type obsahu, na ktorý sú optimalizované (napr. kód vs. obrázky vs. text). Pochopte silné a slabé stránky modelu, ktorý používate, a využite tieto znalosti na _prioritizáciu úloh_ alebo tvorbu _prispôsobených šablón_ optimalizovaných pre schopnosti modelu.

3. **Iterácia a validácia sú dôležité.** Modely sa rýchlo vyvíjajú, rovnako aj techniky prompt engineeringu. Ako odborník na doménu môžete mať ďalší kontext alebo kritériá pre _vašu_ konkrétnu aplikáciu, ktoré nemusia platiť pre širšiu komunitu. Využite nástroje a techniky prompt engineeringu na „rozbehnutie“ tvorby promptov, potom iterujte a validujte výsledky podľa vlastnej intuície a odbornosti. Zaznamenajte svoje poznatky a vytvorte **znalostnú databázu** (napr. knižnice promptov), ktorú môžu ostatní použiť ako nový základ pre rýchlejšie iterácie v budúcnosti.

## Najlepšie postupy

Pozrime sa teraz na bežné odporúčané postupy od odborníkov z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) a [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Čo                              | Prečo                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Vyhodnoťte najnovšie modely.       | Nové generácie modelov pravdepodobne ponúkajú lepšie funkcie a kvalitu – ale môžu byť aj drahšie. Vyhodnoťte ich vplyv a potom sa rozhodnite, či migrovať.                                                                                |
| Oddelte inštrukcie a kontext   | Skontrolujte, či váš model/poskytovateľ definuje _oddeľovače_ na jasnejšie rozlíšenie inštrukcií, primárneho a sekundárneho obsahu. To môže modelu pomôcť presnejšie priradiť váhy tokenom.                                                         |
| Buďte konkrétni a jasní             | Uveďte viac detailov o požadovanom kontexte, výsledku, dĺžke, formáte, štýle atď. Zlepšíte tým kvalitu aj konzistentnosť odpovedí. Ukladajte postupy do opakovane použiteľných šablón.                                                          |
| Buďte opisní, používajte príklady      | Modely často lepšie reagujú na prístup „ukáž a vysvetli“. Začnite s `zero-shot` prístupom, kde zadáte len inštrukciu (bez príkladov), potom skúste `few-shot` ako vylepšenie, kde poskytnete niekoľko príkladov požadovaného výstupu. Používajte analógie. |
| Používajte nápovedy na rozbehnutie odpovede | Nasmerujte model k požadovanému výsledku tým, že mu dáte úvodné slová alebo frázy, ktoré môže použiť ako východiskový bod odpovede.                                                                                                               |
| Opakujte pokyny                       | Niekedy je potrebné modelu zopakovať pokyny. Dajte inštrukcie pred aj po primárnom obsahu, použite inštrukciu aj nápovedu atď. Iterujte a validujte, čo funguje.                                                         |
| Záleží na poradí                     | Poradie, v akom modelu prezentujete informácie, môže ovplyvniť výstup, dokonca aj v príkladoch učenia, kvôli efektu posledných informácií. Skúšajte rôzne možnosti, aby ste zistili, čo je najlepšie.                                                               |
| Dajte modelu „únikovú cestu“           | Dajte modelu _alternatívnu_ odpoveď, ktorú môže použiť, ak z nejakého dôvodu nemôže úlohu splniť. Tým znížite riziko, že model vygeneruje nepravdivé alebo vymyslené odpovede.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Ako pri každom odporúčanom postupe, _vaše výsledky sa môžu líšiť_ podľa modelu, úlohy a domény. Použite ich ako východiskový bod a iterujte, aby ste našli, čo vám najviac vyhovuje. Neustále prehodnocujte svoj proces prompt engineeringu, keď sa objavujú nové modely a nástroje, so zameraním na škálovateľnosť procesu a kvalitu odpovedí.

<!--
ŠABLÓNA LEKCIE:
Táto jednotka by mala obsahovať kódovú výzvu, ak je to vhodné

VÝZVA:
Odkaz na Jupyter Notebook, kde sú v inštrukciách len komentáre (sekcie s kódom sú prázdne).

RIEŠENIE:
Odkaz na kópiu toho Notebooku s vyplnenými promptmi a spustenými, kde je ukázaný jeden príklad.
-->

## Zadanie

Gratulujeme! Dostali ste sa na koniec lekcie! Teraz je čas vyskúšať niektoré z týchto konceptov a techník na reálnych príkladoch!

Na zadanie použijeme Jupyter Notebook s cvičeniami, ktoré môžete interaktívne vypracovať. Notebook si môžete rozšíriť o vlastné Markdown a kódové bunky, aby ste mohli skúmať vlastné nápady a techniky.

### Začnite tak, že si forkujete repozitár, potom

- (Odporúčané) Spustite GitHub Codespaces
- (Alternatívne) Naklonujte repozitár do svojho zariadenia a použite ho s Docker Desktop
- (Alternatívne) Otvorte Notebook vo svojom obľúbenom prostredí pre Notebooky.

### Ďalej nastavte svoje environmentálne premenné

- Skopírujte súbor `.env.copy` z koreňa repozitára do `.env` a vyplňte hodnoty `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` a `AZURE_OPENAI_DEPLOYMENT`. Vráťte sa do sekcie [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), kde sa dozviete viac.

### Potom otvorte Jupyter Notebook

- Vyberte runtime kernel. Ak používate možnosti 1 alebo 2, jednoducho vyberte predvolený kernel Python 3.10.x, ktorý poskytuje vývojársky kontajner.

Ste pripravení spustiť cvičenia. Upozorňujeme, že tu nie sú _správne alebo nesprávne_ odpovede – ide o skúšanie možností metódou pokus-omyl a budovanie intuície, čo funguje pre daný model a aplikačnú doménu.

_Z tohto dôvodu v tejto lekcii nie sú segmenty s riešením kódu. Namiesto toho bude v Notebooku Markdown bunka s názvom „Moje riešenie:“, kde je ukázaný jeden príklad výstupu na referenciu._

 <!--
ŠABLÓNA LEKCIE:
Uzavrite sekciu zhrnutím a zdrojmi na samoštúdium.
-->

## Kontrola znalostí

Ktorý z nasledujúcich promptov je dobrý a spĺňa rozumné najlepšie postupy?

1. Ukáž mi obrázok červeného auta
2. Ukáž mi obrázok červeného auta značky Volvo, model XC90, zaparkovaného pri útesoch so zapadajúcim slnkom
3. Ukáž mi obrázok červeného auta značky Volvo, model XC90

A: 2, je najlepší prompt, pretože obsahuje detaily o „čo“ a ide do špecifík (nie len akékoľvek auto, ale konkrétna značka a model) a tiež opisuje celkové prostredie. 3 je druhý najlepší, lebo obsahuje veľa popisu.

## 🚀 Výzva

Skúste využiť techniku „nápovedy“ s promptom: Dokonči vetu „Ukáž mi obrázok červeného auta značky Volvo a “. Čo vám model odpovie a ako by ste to vylepšili?

## Skvelá práca! Pokračujte v učení

Chcete sa dozvedieť viac o rôznych konceptoch Prompt Engineeringu? Navštívte [stránku na pokračovanie v učení](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde nájdete ďalšie skvelé zdroje k tejto téme.

Pokračujte na Lekciu 5, kde sa pozrieme na [pokročilé techniky promptovania](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vyhlásenie o vylúčení zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho natívnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.