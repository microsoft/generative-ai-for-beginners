<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:32:04+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sk"
}
-->
# Úvod do generatívnej AI a veľkých jazykových modelov

_(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

Generatívna AI je umelá inteligencia schopná generovať text, obrázky a iné typy obsahu. Čo z nej robí fantastickú technológiu, je to, že demokratizuje AI, každý ju môže používať s minimálnym úsilím – stačí textový podnet, veta napísaná v prirodzenom jazyku. Nemusíte sa učiť jazyk ako Java alebo SQL, aby ste dosiahli niečo hodnotné, stačí použiť svoj jazyk, povedať, čo chcete, a AI model vám poskytne návrh. Aplikácie a dopady sú obrovské, môžete písať alebo rozumieť správam, písať aplikácie a oveľa viac, všetko v priebehu sekúnd.

V tomto učebnom pláne preskúmame, ako naša startup firma využíva generatívnu AI na odomknutie nových scenárov vo svete vzdelávania a ako sa zaoberáme nevyhnutnými výzvami spojenými so sociálnymi dopadmi jej aplikácie a technologickými obmedzeniami.

## Úvod

Táto lekcia pokryje:

- Úvod do obchodného scenára: naša startupová idea a misia.
- Generatívna AI a ako sme sa dostali k súčasnej technologickej krajine.
- Vnútorné fungovanie veľkého jazykového modelu.
- Hlavné schopnosti a praktické prípady použitia veľkých jazykových modelov.

## Ciele učenia

Po dokončení tejto lekcie budete rozumieť:

- Čo je generatívna AI a ako fungujú veľké jazykové modely.
- Ako môžete využiť veľké jazykové modely pre rôzne prípady použitia, so zameraním na scenáre vzdelávania.

## Scenár: náš vzdelávací startup

Generatívna umelá inteligencia (AI) predstavuje vrchol AI technológie, posúvajúc hranice toho, čo sa kedysi považovalo za nemožné. Generatívne AI modely majú niekoľko schopností a aplikácií, ale pre tento učebný plán preskúmame, ako revolucionalizuje vzdelávanie prostredníctvom fiktívneho startupu. Budeme odkazovať na tento startup ako _náš startup_. Náš startup pracuje v oblasti vzdelávania s ambicióznou misiou

> _zlepšiť prístupnosť učenia na globálnej úrovni, zabezpečiť rovnaký prístup k vzdelaniu a poskytovať personalizované vzdelávacie skúsenosti každému študentovi podľa jeho potrieb_.

Tím nášho startupu si je vedomý, že nedokážeme dosiahnuť tento cieľ bez využitia jedného z najvýkonnejších nástrojov modernej doby – veľkých jazykových modelov (LLMs).

Generatívna AI sa očakáva, že revolucionalizuje spôsob, akým sa dnes učíme a učíme, pričom študenti majú k dispozícii virtuálnych učiteľov 24 hodín denne, ktorí poskytujú obrovské množstvo informácií a príkladov, a učitelia sú schopní využiť inovatívne nástroje na hodnotenie svojich študentov a poskytovanie spätnej väzby.

Aby sme začali, definujme niektoré základné koncepty a terminológiu, ktorú budeme používať v celom učebnom pláne.

## Ako sme získali generatívnu AI?

Napriek mimoriadnemu _hypeu_ vytvorenému nedávno oznámením generatívnych AI modelov, táto technológia sa vyvíja už desaťročia, pričom prvé výskumné úsilie siaha až do 60. rokov. Teraz sme na bode, keď AI má ľudské kognitívne schopnosti, ako je konverzácia, čo je viditeľné napríklad pri [OpenAI ChatGPT](https://openai.com/chatgpt) alebo [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), ktorý tiež používa GPT model pre webové vyhľadávanie Bing konverzácií.

Ak sa trochu vrátime späť, prvé prototypy AI pozostávali z písaných chatbotov, ktoré sa spoliehali na znalostnú základňu extrahovanú z skupiny odborníkov a reprezentovanú v počítači. Odpovede v znalostnej základni boli aktivované kľúčovými slovami, ktoré sa objavili vo vstupnom texte.
Čoskoro sa však ukázalo, že takýto prístup, využívajúci písané chatboty, sa dobre neškáluje.

### Štatistický prístup k AI: strojové učenie

Zlom nastal počas 90. rokov, s aplikáciou štatistického prístupu k analýze textu. To viedlo k vývoju nových algoritmov – známych ako strojové učenie – schopných učiť sa vzory z údajov bez explicitného programovania. Tento prístup umožňuje strojom simulovať porozumenie ľudského jazyka: štatistický model je trénovaný na párovaní textu a štítkov, čo umožňuje modelu klasifikovať neznámy vstupný text s preddefinovaným štítkom predstavujúcim úmysel správy.

### Neurónové siete a moderní virtuálni asistenti

V posledných rokoch technologický vývoj hardvéru, schopného spracovať väčšie množstvo údajov a zložitejšie výpočty, podporil výskum v oblasti AI, čo viedlo k vývoju pokročilých algoritmov strojového učenia známych ako neurónové siete alebo algoritmy hlbokého učenia.

Neurónové siete (a najmä Rekurentné neurónové siete – RNNs) výrazne zlepšili spracovanie prirodzeného jazyka, umožňujúc reprezentáciu významu textu spôsobom, ktorý lepšie hodnotí kontext slova vo vete.

Toto je technológia, ktorá poháňala virtuálnych asistentov, ktorí sa narodili v prvom desaťročí nového storočia, veľmi zdatných v interpretácii ľudského jazyka, identifikácii potreby a vykonávaní akcie na jej uspokojenie – ako odpovedanie s preddefinovaným skriptom alebo využívanie služby tretej strany.

### Súčasnosť, generatívna AI

Tak sme sa dostali k dnešnej generatívnej AI, ktorá môže byť videná ako podmnožina hlbokého učenia.

Po desaťročiach výskumu v oblasti AI, nová architektúra modelu – nazvaná _Transformer_ – prekonala limity RNNs, schopná prijímať oveľa dlhšie sekvencie textu ako vstup. Transformery sú založené na mechanizme pozornosti, ktorý umožňuje modelu dávať rôzne váhy vstupom, ktoré dostáva, „venovať väčšiu pozornosť“ tam, kde sú sústredené najrelevantnejšie informácie, bez ohľadu na ich poradie v sekvencii textu.

Väčšina nedávnych generatívnych AI modelov – tiež známych ako Veľké jazykové modely (LLMs), pretože pracujú s textovými vstupmi a výstupmi – je skutočne založená na tejto architektúre. Čo je zaujímavé na týchto modeloch – trénovaných na obrovskom množstve neoznačených údajov z rôznych zdrojov ako knihy, články a webové stránky – je to, že môžu byť prispôsobené na širokú škálu úloh a generovať gramaticky správny text s náznakom kreativity. Takže nielenže neuveriteľne zlepšili schopnosť stroja „rozumieť“ vstupnému textu, ale umožnili jeho schopnosť generovať originálnu odpoveď v ľudskom jazyku.

## Ako fungujú veľké jazykové modely?

V ďalšej kapitole preskúmame rôzne typy generatívnych AI modelov, ale teraz sa pozrime na to, ako fungujú veľké jazykové modely, so zameraním na OpenAI GPT (Generative Pre-trained Transformer) modely.

- **Tokenizer, text na čísla**: Veľké jazykové modely prijímajú text ako vstup a generujú text ako výstup. Avšak, keďže sú to štatistické modely, pracujú oveľa lepšie s číslami ako s textovými sekvenciami. Preto je každý vstup do modelu spracovaný tokenizerom, predtým ako je použitý jadrovým modelom. Token je kus textu – pozostávajúci z variabilného počtu znakov, takže hlavnou úlohou tokenizeru je rozdelenie vstupu na pole tokenov. Potom je každý token mapovaný s indexom tokenu, ktorý je celým číselným kódovaním pôvodného textového kusu.

- **Predikcia výstupných tokenov**: Pri zadaní n tokenov ako vstupu (s maximálnym n sa líši od modelu k modelu), model je schopný predpovedať jeden token ako výstup. Tento token je potom zahrnutý do vstupu ďalšej iterácie, v rozširujúcom sa okne, čo umožňuje lepší používateľský zážitok získania jednej (alebo viacerých) vety ako odpovede. To vysvetľuje, prečo, ak ste sa niekedy hrali s ChatGPT, možno ste si všimli, že niekedy to vyzerá, že sa zastaví uprostred vety.

- **Proces výberu, distribúcia pravdepodobnosti**: Výstupný token je vybraný modelom podľa jeho pravdepodobnosti výskytu po aktuálnej textovej sekvencii. To je preto, že model predpovedá distribúciu pravdepodobnosti nad všetkými možnými „nasledujúcimi tokenmi“, vypočítanú na základe jeho tréningu. Avšak, nie vždy je token s najvyššou pravdepodobnosťou vybraný z výslednej distribúcie. Do tejto voľby je pridaný stupeň náhodnosti, spôsobom, že model koná v nedeterministickom režime - nedostaneme presne rovnaký výstup pre rovnaký vstup. Tento stupeň náhodnosti je pridaný na simuláciu procesu kreatívneho myslenia a môže byť upravený pomocou parametra modelu nazvaného teplota.

## Ako môže náš startup využiť veľké jazykové modely?

Teraz, keď máme lepšie pochopenie vnútorného fungovania veľkého jazykového modelu, pozrime sa na niektoré praktické príklady najbežnejších úloh, ktoré dokážu vykonávať veľmi dobre, so zameraním na náš obchodný scenár.
Povedali sme, že hlavnou schopnosťou veľkého jazykového modelu je _generovanie textu od začiatku, počnúc textovým vstupom, napísaným v prirodzenom jazyku_.

Ale aký druh textového vstupu a výstupu?
Vstup veľkého jazykového modelu je známy ako prompt, zatiaľ čo výstup je známy ako completion, termín, ktorý sa odkazuje na mechanizmus modelu generovania nasledujúceho tokenu na dokončenie aktuálneho vstupu. Budeme sa hlboko ponoriť do toho, čo je prompt a ako ho navrhnúť spôsobom, aby sme z nášho modelu vyťažili maximum. Ale teraz, povedzme si len, že prompt môže zahŕňať:

- **Inštrukciu** špecifikujúcu typ výstupu, ktorý očakávame od modelu. Táto inštrukcia môže niekedy obsahovať niekoľko príkladov alebo niektoré dodatočné údaje.

  1. Zhrnutie článku, knihy, recenzií produktov a ďalších, spolu s extrakciou poznatkov z nestruktúrovaných údajov.

  2. Kreatívne navrhovanie a dizajn článku, eseje, zadania alebo viac.

- **Otázku**, položenú formou konverzácie s agentom.

- Kus **textu na dokončenie**, ktorý implicitne žiada o pomoc pri písaní.

- Kus **kódu** spolu s požiadavkou na vysvetlenie a dokumentáciu, alebo komentár žiadajúci o generovanie kúsku kódu vykonávajúceho konkrétnu úlohu.

Vyššie uvedené príklady sú pomerne jednoduché a nie sú určené ako vyčerpávajúca demonštrácia schopností veľkých jazykových modelov. Sú určené na ukázanie potenciálu používania generatívnej AI, najmä ale nie výlučne v kontexte vzdelávania.

Tiež, výstup generatívneho AI modelu nie je dokonalý a niekedy kreativita modelu môže pracovať proti nemu, čo má za následok výstup, ktorý je kombináciou slov, ktoré ľudský používateľ môže interpretovať ako mystifikáciu reality, alebo môže byť urážlivý. Generatívna AI nie je inteligentná - aspoň v komplexnejšej definícii inteligencie, zahŕňajúcej kritické a kreatívne uvažovanie alebo emocionálnu inteligenciu; nie je deterministická a nie je dôveryhodná, pretože fikcie, ako nesprávne odkazy, obsah a tvrdenia, môžu byť kombinované so správnymi informáciami a prezentované presvedčivým a sebavedomým spôsobom. V nasledujúcich lekciách sa budeme zaoberať všetkými týmito obmedzeniami a uvidíme, čo môžeme urobiť, aby sme ich zmiernili.

## Úloha

Vašou úlohou je prečítať si viac o [generatívnej AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) a pokúsiť sa identifikovať oblasť, kde by ste dnes pridali generatívnu AI, ktorá ju nemá. Ako by bol dopad odlišný od vykonania to "starým spôsobom", môžete urobiť niečo, čo ste predtým nemohli, alebo ste rýchlejší? Napíšte 300 slovný súhrn o tom, ako by vyzeral váš vysnívaný AI startup a zahrňte nadpisy ako "Problém", "Ako by som použil AI", "Dopad" a prípadne obchodný plán.

Ak ste túto úlohu vykonali, možno budete pripravení prihlásiť sa do inkubátora Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) ponúkame kredity pre Azure, OpenAI, mentoring a oveľa viac, pozrite sa na to!

## Kontrola znalostí

Čo je pravda o veľkých jazykových modeloch?

1. Dostanete presne rovnakú odpoveď zakaždým.
1. Robí veci dokonale, skvelé v sčítavaní čísel, produkuje funkčný kód atď.
1. Odpoveď sa môže líšiť napriek použitiu rovnakého promptu. Je tiež skvelý na poskytnutie prvého návrhu niečoho, či už textu alebo kódu. Ale musíte zlepšiť výsledky.

A: 3, LLM je nedeterministický, odpoveď sa líši, avšak môžete kontrolovať jej variabilitu pomocou nastavenia teploty. Tiež by ste nemali očakávať, že robí veci dokonale, je tu na to, aby robil ťažkú prácu za vás, čo často znamená, že dostanete dobrý prvý pokus o niečo, čo musíte postupne zlepšovať.

## Skvelá práca! Pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [Generatívnu AI vzdelávaciu kolekciu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zvyšovaní svojich znalostí o generatívnej AI!

Prejdite na Lekciu 2, kde sa pozrieme na to, ako [preskúmať a porovnať rôzne typy LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.