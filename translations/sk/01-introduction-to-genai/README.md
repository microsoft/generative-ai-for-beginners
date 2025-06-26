<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:05:34+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sk"
}
-->
# Úvod do generatívnej AI a veľkých jazykových modelov

_(Kliknite na obrázok vyššie a pozrite si video tejto lekcie)_

Generatívna AI je umelá inteligencia schopná generovať text, obrázky a iné typy obsahu. Čo z nej robí fantastickú technológiu, je to, že demokratizuje AI, každý ju môže používať s takým jednoduchým vstupom ako je textový prompt, veta napísaná v prirodzenom jazyku. Nie je potrebné sa naučiť jazyk ako Java alebo SQL, aby ste dosiahli niečo hodnotné, stačí použiť svoj jazyk, uviesť, čo chcete, a AI model vám poskytne návrh. Aplikácie a dopad tohto sú obrovské, môžete písať alebo rozumieť správam, písať aplikácie a oveľa viac, a to všetko za pár sekúnd.

V tomto kurikule preskúmame, ako náš startup využíva generatívnu AI na odomknutie nových scenárov vo svete vzdelávania a ako riešime nevyhnutné výzvy spojené so sociálnymi dôsledkami jej aplikácie a technologickými obmedzeniami.

## Úvod

Táto lekcia pokryje:

- Úvod do obchodného scenára: náš startupový nápad a poslanie.
- Generatívna AI a ako sme sa dostali na súčasnú technologickú krajinu.
- Vnútorné fungovanie veľkého jazykového modelu.
- Hlavné schopnosti a praktické použitia veľkých jazykových modelov.

## Ciele učenia

Po dokončení tejto lekcie budete rozumieť:

- Čo je generatívna AI a ako fungujú veľké jazykové modely.
- Ako môžete využiť veľké jazykové modely na rôzne použitia, so zameraním na vzdelávacie scenáre.

## Scenár: náš vzdelávací startup

Generatívna umelá inteligencia (AI) predstavuje vrchol AI technológie, posúva hranice toho, čo sa kedysi považovalo za nemožné. Generatívne AI modely majú niekoľko schopností a aplikácií, ale pre toto kurikulum preskúmame, ako revolučne mení vzdelávanie prostredníctvom fiktívneho startupu. Budeme sa odvolávať na tento startup ako _náš startup_. Náš startup pracuje v oblasti vzdelávania s ambicióznym vyhlásením misie

> _zlepšovať dostupnosť vzdelávania na globálnej úrovni, zabezpečiť rovný prístup k vzdelaniu a poskytovať personalizované vzdelávacie skúsenosti každému študentovi podľa jeho potrieb_.

Náš startupový tím si je vedomý, že tento cieľ nedosiahneme bez využitia jedného z najvýkonnejších nástrojov modernej doby – veľkých jazykových modelov (LLMs).

Generatívna AI sa očakáva, že revolučne zmení spôsob, akým sa dnes učíme a učíme, pričom študenti budú mať k dispozícii virtuálnych učiteľov 24 hodín denne, ktorí poskytujú obrovské množstvo informácií a príkladov, a učitelia budú schopní využívať inovatívne nástroje na hodnotenie svojich študentov a poskytovanie spätnej väzby.

Aby sme začali, definujme niektoré základné koncepty a terminológiu, ktorú budeme používať v celom kurikule.

## Ako sme získali generatívnu AI?

Napriek mimoriadnemu _hype_, ktorý bol nedávno vytvorený oznámením generatívnych AI modelov, táto technológia sa vyvíja už desaťročia, pričom prvé výskumné úsilie siaha až do 60. rokov. Teraz sme na bode, kde AI má ľudské kognitívne schopnosti, ako je konverzácia, ako ukazuje napríklad [OpenAI ChatGPT](https://openai.com/chatgpt) alebo [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), ktorý tiež používa GPT model na webové vyhľadávanie Bing konverzácií.

Trochu sa vraciame späť, prvé prototypy AI pozostávali z písacích chatbotov, spoliehajúc sa na znalostnú bázu extrahovanú zo skupiny expertov a reprezentovanú do počítača. Odpovede v znalostnej báze boli aktivované kľúčovými slovami, ktoré sa objavili vo vstupnom texte.
Avšak čoskoro sa ukázalo, že takýto prístup, používajúci písacie chatboty, sa neškáloval dobre.

### Štatistický prístup k AI: strojové učenie

Prelom nastal počas 90. rokov s aplikáciou štatistického prístupu k analýze textu. To viedlo k vývoju nových algoritmov – známych ako strojové učenie – schopných učiť sa vzory z dát bez explicitného programovania. Tento prístup umožňuje strojom simulovať porozumenie ľudského jazyka: štatistický model je trénovaný na párovaní text-etiketa, čo umožňuje modelu klasifikovať neznámy vstupný text s preddefinovanou etiketou reprezentujúcou zámer správy.

### Neurónové siete a moderní virtuálni asistenti

V posledných rokoch technologická evolúcia hardvéru, schopného spracovávať väčšie množstvo dát a zložitejšie výpočty, povzbudila výskum v oblasti AI, čo viedlo k vývoju pokročilých algoritmov strojového učenia známych ako neurónové siete alebo algoritmy hlbokého učenia.

Neurónové siete (a najmä rekurentné neurónové siete – RNNs) výrazne zlepšili spracovanie prirodzeného jazyka, umožňujúc reprezentáciu významu textu zmysluplnejším spôsobom, hodnotiac kontext slova vo vete.

Toto je technológia, ktorá poháňala virtuálnych asistentov, narodených v prvom desaťročí nového storočia, veľmi zručných v interpretácii ľudského jazyka, identifikácii potreby a vykonávaní akcie na jej uspokojenie – ako je odpovedanie s preddefinovaným skriptom alebo spotrebovanie služby tretej strany.

### Súčasnosť, Generatívna AI

Takto sme sa dostali k dnešnej generatívnej AI, ktorá môže byť vnímaná ako podmnožina hlbokého učenia.

Po desaťročiach výskumu v oblasti AI nová architektúra modelov – nazvaná _Transformer_ – prekonala limity RNNs, schopná prijímať oveľa dlhšie sekvencie textu ako vstup. Transformery sú založené na mechanizme pozornosti, umožňujúc modelu dávať rôzne váhy vstupom, ktoré prijíma, „venovať väčšiu pozornosť“ tam, kde je sústredená najrelevantnejšia informácia, bez ohľadu na ich poradie v textovej sekvencii.

Väčšina nedávnych generatívnych AI modelov – známych tiež ako veľké jazykové modely (LLMs), pretože pracujú s textovými vstupmi a výstupmi – je skutočne založená na tejto architektúre. Čo je zaujímavé na týchto modeloch – trénovaných na obrovskom množstve neoznačených dát z rôznych zdrojov ako knihy, články a webové stránky – je to, že môžu byť prispôsobené na širokú škálu úloh a generovať gramaticky správny text s náznakom kreativity. Takže nielenže neuveriteľne zlepšili schopnosť stroja „rozumieť“ vstupnému textu, ale umožnili ich schopnosť generovať originálnu odpoveď v ľudskom jazyku.

## Ako fungujú veľké jazykové modely?

V nasledujúcej kapitole preskúmame rôzne typy generatívnych AI modelov, ale zatiaľ sa pozrime na to, ako fungujú veľké jazykové modely, so zameraním na modely OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, text na čísla**: Veľké jazykové modely prijímajú text ako vstup a generujú text ako výstup. Avšak, ako štatistické modely, pracujú oveľa lepšie s číslami než s textovými sekvenciami. Preto je každý vstup do modelu spracovaný tokenizerom, predtým než je použitý jadrovým modelom. Token je kúsok textu – pozostávajúci z variabilného počtu znakov, takže hlavná úloha tokenizeru je rozdelenie vstupu do poľa tokenov. Potom je každý token mapovaný na token index, čo je celočíselné kódovanie pôvodného textového kúsku.

- **Predikcia výstupných tokenov**: Daných n tokenov ako vstup (s maximálnym n, ktoré sa líši od jedného modelu k druhému), model je schopný predikovať jeden token ako výstup. Tento token je potom začlenený do vstupu ďalšej iterácie, v rozširujúcom sa okne, umožňujúc lepšiu užívateľskú skúsenosť získať jednu (alebo viacero) viet ako odpoveď. To vysvetľuje, prečo, ak ste sa niekedy hrali s ChatGPT, mohli ste si všimnúť, že niekedy to vyzerá, že sa zastaví uprostred vety.

- **Proces výberu, rozdelenie pravdepodobnosti**: Výstupný token je vybraný modelom podľa jeho pravdepodobnosti výskytu po aktuálnej textovej sekvencii. To je preto, že model predikuje rozdelenie pravdepodobnosti nad všetkými možnými „nasledujúcimi tokenmi“, vypočítané na základe jeho tréningu. Avšak nie vždy je token s najvyššou pravdepodobnosťou vybraný z výsledného rozdelenia. Do tejto voľby je pridaný stupeň náhodnosti, spôsobom, že model sa správa nedeterministickým spôsobom - nedostávame presne ten istý výstup pre ten istý vstup. Tento stupeň náhodnosti je pridaný na simuláciu procesu kreatívneho myslenia a môže byť nastavený pomocou parametra modelu nazývaného teplota.

## Ako môže náš startup využiť veľké jazykové modely?

Teraz, keď máme lepšie pochopenie vnútorného fungovania veľkého jazykového modelu, pozrime sa na niektoré praktické príklady najbežnejších úloh, ktoré môžu vykonávať veľmi dobre, s pohľadom na náš obchodný scenár.
Povedali sme, že hlavná schopnosť veľkého jazykového modelu je _generovať text od začiatku, začínajúc od textového vstupu, napísaného v prirodzenom jazyku_.

Ale aký druh textového vstupu a výstupu?
Vstup veľkého jazykového modelu je známy ako prompt, zatiaľ čo výstup je známy ako dokončenie, termín, ktorý sa vzťahuje na mechanizmus modelu generovania ďalšieho tokenu na dokončenie aktuálneho vstupu. Ponoríme sa hlboko do toho, čo je prompt a ako ho navrhnúť tak, aby sme z nášho modelu získali maximum. Ale zatiaľ len povedzme, že prompt môže obsahovať:

- **Inštrukciu** špecifikujúcu typ výstupu, ktorý očakávame od modelu. Táto inštrukcia niekedy môže obsahovať niekoľko príkladov alebo nejaké ďalšie údaje.

  1. Zhrnutie článku, knihy, recenzií produktov a viac, spolu s extrakciou poznatkov z nestrukturovaných dát.
    
  2. Kreatívna ideácia a návrh článku, eseje, zadania alebo viac.
      
- **Otázku**, položenú vo forme konverzácie s agentom.

- Kus **textu na dokončenie**, čo implicitne je žiadosť o pomoc pri písaní.

- Kus **kódu** spolu s požiadavkou na vysvetlenie a dokumentáciu, alebo komentár žiadajúci generovať kus kódu vykonávajúci konkrétnu úlohu.

Vyššie uvedené príklady sú pomerne jednoduché a nie sú určené na to, aby boli vyčerpávajúcou demonštráciou schopností veľkých jazykových modelov. Majú za cieľ ukázať potenciál používania generatívnej AI, najmä ale nie výlučne vo vzdelávacích kontextoch.

Výstup generatívneho AI modelu tiež nie je dokonalý a niekedy môže kreatívnosť modelu pracovať proti nemu, výsledkom čoho je výstup, ktorý je kombináciou slov, ktoré ľudský užívateľ môže interpretovať ako mystifikáciu reality, alebo môže byť urážlivý. Generatívna AI nie je inteligentná - aspoň v komplexnejšej definícii inteligencie, zahŕňajúcej kritické a kreatívne uvažovanie alebo emocionálnu inteligenciu; nie je deterministická a nie je dôveryhodná, pretože fabrikácie, ako nesprávne odkazy, obsah a tvrdenia, môžu byť kombinované so správnymi informáciami a prezentované presvedčivým a sebaistým spôsobom. V nasledujúcich lekciách sa budeme zaoberať všetkými týmito obmedzeniami a uvidíme, čo môžeme urobiť na ich zmiernenie.

## Zadanie

Vašou úlohou je prečítať si viac o [generatívnej AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) a pokúsiť sa identifikovať oblasť, kde by ste dnes pridali generatívnu AI, ktorá ju nemá. Ako by bol dopad odlišný od robenia vecí „starým spôsobom“, môžete urobiť niečo, čo ste nemohli predtým, alebo ste rýchlejší? Napíšte 300-slovný súhrn o tom, ako by vyzeral váš vysnívaný AI startup a zahrňte nadpisy ako „Problém“, „Ako by som použil AI“, „Dopad“ a voliteľne podnikateľský plán.

Ak ste túto úlohu splnili, môžete byť pripravení podať žiadosť do inkubátora Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) ponúkame kredity pre Azure, OpenAI, mentoring a oveľa viac, pozrite si to!

## Kontrola znalostí

Čo je pravda o veľkých jazykových modeloch?

1. Dostanete presne rovnakú odpoveď každýkrát.
1. Robí veci dokonale, skvelé v sčítavaní čísel, produkuje funkčný kód atď.
1. Odpoveď sa môže líšiť napriek použitiu rovnakého promptu. Je tiež skvelý na poskytnutie prvého návrhu niečoho, či už textu alebo kódu. Ale musíte vylepšiť výsledky.

A: 3, LLM je nedeterministický, odpoveď sa líši, avšak môžete kontrolovať jeho variabilitu pomocou nastavenia teploty. Nemali by ste tiež očakávať, že veci robí dokonale, je tu na to, aby za vás urobil ťažkú prácu, čo často znamená, že dostanete dobrý prvý pokus o niečo, čo musíte postupne zlepšovať.

## Skvelá práca! Pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v zvyšovaní vašich znalostí o generatívnej AI!

Prejdite na lekciu 2, kde sa pozrieme na to, ako [preskúmať a porovnať rôzne typy LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.