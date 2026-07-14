# Tvorba AI aplikácií s nízkym kódom

[![Tvorba AI aplikácií s nízkym kódom](../../../translated_images/sk/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

## Úvod

Keďže sme sa naučili, ako vytvárať aplikácie generujúce obrázky, porozprávajme sa o nízkom kóde. Generatívna AI sa dá použiť v rôznych oblastiach vrátane nízkeho kódu, ale čo je nízky kód a ako do neho môžeme pridať AI?

Vývoj aplikácií a riešení sa stal jednoduchším pre tradičných vývojárov i neprogramátorov vďaka použitiu platforiem na vývoj s nízkym kódom (Low Code Development Platforms). Tieto platformy umožňujú vytvárať aplikácie a riešenia s minimom alebo žiadnym kódom. To sa dosahuje poskytovaním vizuálneho vývojového prostredia, kde môžete aplikácie a riešenia stavať pomocou ťahania a pustenia komponentov. Umožňuje to rýchlejšiu výstavbu aplikácií a riešení a s menším množstvom zdrojov. V tejto lekcii sa podrobne pozrieme na to, ako používať nízky kód a ako ho vylepšiť AI pomocou Power Platform.

Power Platform poskytuje organizáciám možnosť umožniť svojim tímom budovať vlastné riešenia prostredníctvom intuitívneho prostredia s nízkym alebo žiadnym kódom. Toto prostredie zjednodušuje proces vytvárania riešení. S Power Platform môžete riešenia vytvoriť za dni alebo týždne namiesto mesiacov či rokov. Power Platform pozostáva z piatich kľúčových produktov: Power Apps, Power Automate, Power BI, Power Pages a Copilot Studio.

Táto lekcia pokrýva:

- Úvod do generatívnej AI v Power Platform
- Úvod do Copilota a ako ho používať
- Použitie generatívnej AI na tvorbu aplikácií a tokov v Power Platform
- Pochopenie AI modelov v Power Platform s AI Builder
- Tvorba inteligentných agentov s Microsoft Copilot Studio

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Pochopiť, ako Copilot funguje v Power Platform.

- Vytvoriť aplikáciu na sledovanie študentských zadaní pre našu vzdelávaciu startup spoločnosť.

- Vytvoriť tok na spracovanie faktúr, ktorý používa AI na extrakciu informácií z faktúr.

- Aplikovať najlepšie praktiky pri používaní GPT AI modelu na tvorbu textu.

- Pochopiť, čo je Microsoft Copilot Studio a ako s ním vytvárať inteligentných agentov.

Nástroje a technológie, ktoré v tejto lekcii použijete, sú:

- **Power Apps** pre aplikáciu na sledovanie študentských zadaní, ktorá poskytuje vývojové prostredie s nízkym kódom na tvorbu aplikácií na sledovanie, správu a interakciu s dátami.

- **Dataverse** na ukladanie dát pre aplikáciu na sledovanie študentských zadaní, kde Dataverse poskytuje dátovú platformu s nízkym kódom na ukladanie dát aplikácie.

- **Power Automate** pre tok spracovania faktúr, kde budete mať prostredie s nízkym kódom na vytváranie pracovných tokov na automatizáciu procesu spracovania faktúr.

- **AI Builder** pre AI model spracovania faktúr, kde využijete predpripravené AI modely na spracovanie faktúr pre náš startup.

## Generatívna AI v Power Platform

Vylepšovanie vývoja s nízkym kódom a aplikácií generatívnou AI je kľúčovou oblasťou zamerania Power Platform. Cieľom je umožniť každému tvoriť AI-poháňané aplikácie, stránky, dashboardy a automatizovať procesy pomocou AI, _bez potreby znalostí dátovej vedy_. Tento cieľ sa dosahuje integráciou generatívnej AI do vývojového prostredia s nízkym kódom v Power Platform v podobe Copilota a AI Buildera.

### Ako to funguje?

Copilot je AI asistent, ktorý vám umožňuje vytvárať riešenia Power Platform opisom požiadaviek v sérii konverzačných krokov v prirodzenom jazyku. Môžete napríklad povedať asistentovi, aké polia vaša aplikácia bude používať, a on vytvorí aplikáciu aj základný dátový model, alebo môžete zadať, ako nastaviť tok v Power Automate.

Môžete používať funkcie Copilota ako súčasť obrazoviek vašej aplikácie, aby používatelia mohli získavať poznatky prostredníctvom konverzačných interakcií.

AI Builder je schopnosť AI s nízkym kódom dostupná v Power Platform, ktorá vám umožňuje používať AI modely na automatizáciu procesov a predikciu výsledkov. S AI Builderom môžete AI priniesť do svojich aplikácií a tokov, ktoré sa pripájajú k vašim dátam v Dataverse alebo v rôznych cloudových dátových zdrojoch, ako sú SharePoint, OneDrive alebo Azure.

Copilot je dostupný vo všetkých produktoch Power Platformu: Power Apps, Power Automate, Power BI, Power Pages a Copilot Studio (predtým Power Virtual Agents). AI Builder je dostupný v Power Apps a Power Automate. V tejto lekcii sa zameriame, ako používať Copilot a AI Builder v Power Apps a Power Automate na vytvorenie riešenia pre náš vzdelávací startup.

### Copilot v Power Apps

Power Apps je súčasťou Power Platform a poskytuje prostredie na vývoj aplikácií s nízkym kódom na sledovanie, správu a prácu s dátami. Je to sada služieb na vývoj aplikácií s škálovateľnou dátovou platformou a možnosťou pripojenia ku cloudovým službám a on-premises dátam. Power Apps umožňuje vytvárať aplikácie, ktoré bežia v prehliadači, na tabletoch a telefónoch a môžu sa zdieľať s kolegami. Power Apps uľahčuje používateľom vstup do vývoja aplikácií jednoduchým rozhraním, takže každý obchodný používateľ alebo profesionálny vývojár môže vytvárať vlastné aplikácie. Vývoj aplikácií je tiež vylepšený generatívnou AI prostredníctvom Copilota.

Funkcia AI asistenta Copilota v Power Apps vám umožňuje opísať, aký druh aplikácie potrebujete a aké informácie má vaša aplikácia sledovať, zbierať alebo zobrazovať. Copilot potom vygeneruje responzívnu Canvas aplikáciu na základe vášho opisu. Aplikáciu môžete ďalej prispôsobiť podľa svojich potrieb. AI Copilot tiež vygeneruje a navrhne tabuľku v Dataverse s poliami, ktoré potrebujete na uloženie údajov, ktoré chcete sledovať, spolu s ukážkovými dátami. V tejto lekcii sa neskôr pozrieme, čo je Dataverse a ako ho môžete používať v Power Apps. Tabuľku potom môžete prispôsobiť podľa svojich potrieb pomocou funkcie AI asistenta Copilota cez konverzačné kroky. Táto funkcia je priamo dostupná na domovskej obrazovke Power Apps.

### Copilot v Power Automate

Power Automate je súčasťou Power Platform a umožňuje používateľom vytvárať automatizované pracovné toky medzi aplikáciami a službami. Pomáha automatizovať opakujúce sa podnikateľské procesy, ako je komunikácia, zber dát a schvaľovanie rozhodnutí. Jeho jednoduché rozhranie umožňuje používateľom s rôznou technickou úrovňou (od začiatočníkov po skúsených vývojárov) automatizovať pracovné úlohy. Vývoj pracovných tokov je tiež vylepšený generatívnou AI cez Copilot.

Funkcia AI asistenta Copilota v Power Automate vám umožňuje opísať, aký druh toku potrebujete a aké akcie chcete, aby váš tok vykonával. Copilot potom na základe vášho opisu vygeneruje tok. Tok môžete ďalej prispôsobiť podľa svojich potrieb. AI Copilot tiež navrhne akcie potrebné na vykonanie úlohy, ktorú chcete automatizovať. V tejto lekcii sa neskôr pozrieme, čo sú to toky a ako ich môžete používať v Power Automate. Následne môžete akcie upravovať podľa svojich potrieb pomocou AI asistenta Copilota prostredníctvom konverzačných krokov. Táto funkcia je priamo dostupná na domovskej obrazovke Power Automate.

## Tvorba inteligentných agentov s Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (predtým Power Virtual Agents) je členom Power Platform s nízkym kódom na tvorbu **AI agentov** — konverzačných kopilotov, ktorí môžu odpovedať na otázky, vykonávať akcie a automatizovať úlohy za vašich používateľov. Rovnako ako zvyšok Power Platform, tieto agenti sa vytvárajú vo vizuálnom, prednostne prirodzeným jazykom orientovanom prostredí: popíšete, čo chcete, aby agent robil, a Copilot Studio pomáha zostaviť jeho inštrukcie, znalosti a akcie.

Pre náš vzdelávací startup by ste mohli vytvoriť agenta, ktorý odpovedá na otázky študentov o kurzoch, kontroluje termíny zadaní a dokonca posiela e-maily lektorovi — to všetko bez písania kódu.

Tu sú niektoré z najnovších schopností, ktoré robia Copilot Studio silným:

- **Generatívne odpovede z vašich znalostí**. Namiesto ručného písania každej konverzácie môžete pripojiť **zdroje znalostí** — verejné webové stránky, SharePoint, OneDrive, Dataverse, nahrané súbory alebo podnikové dáta cez konektory — a agent generuje podložené odpovede z týchto zdrojov.

- **Generatívna orchestrácia**. Namiesto spoléhaniu sa na pevné spúšťacie frázy agent používa AI na pochopenie požiadavky a dynamicky rozhodne, ktoré znalosti, témy a akcie skombinovať na jej splnenie, vrátane reťazenia viacerých krokov dohromady.

- **Akcie a konektory**. Agenti môžu *vykonávať* úlohy, nielen chatovať. Môžete agentovi prideliť akcie podporené 1 500+ predpripravenými konektormi Power Platform, tokmi Power Automate, vlastnými REST API, promptmi alebo servermi **Model Context Protocol (MCP)**.

- **Autonómni agenti**. Agenti nie sú limitovaní odpovedaním v chatovacom okne. Môžete vytvoriť **autonómnych agentov**, ktorí sú spustením udalostí — napríklad nové e-maily, nový záznam v Dataverse alebo nahratie súboru — a potom v pozadí vykonávajú úlohu.

- **Multiagentná orchestrácia**. Agenti môžu volať iných agentov. Agent v Copilot Studio môže predávať úlohy iným agentom alebo byť nimi rozšírený, vrátane agentov publikovaných do Microsoft 365 Copilot a agentov vytvorených v Microsoft Foundry.

- **Voľba modelu**. Okrem vstavaných modelov môžete priniesť modely z katalógu modelov Microsoft Foundry a prispôsobiť spôsob, akým váš agent uvažuje a odpovedá.

- **Publikovanie kdekoľvek**. Akonáhle je agent vytvorený, môže byť publikovaný do viacerých kanálov — Microsoft Teams, Microsoft 365 Copilot, webové stránky alebo vlastné aplikácie a ďalšie — so zabezpečením, autentifikáciou a analýzou riadenou cez administrátorské prostredie Power Platform.

Môžete začať tvoriť svoj prvý agent na [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) a dozvedieť sa viac v [dokumentácii Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Zadanie: Správa študentských zadaní a faktúr pre náš startup pomocou Copilota

Náš startup poskytuje online kurzy študentom. Startup rýchlo rástol a teraz má problém držať krok s dopytom po svojich kurzoch. Najali si vás ako vývojára Power Platform, aby ste im pomohli vytvoriť riešenie s nízkym kódom na správu študentských zadaní a faktúr. Ich riešenie by malo pomôcť sledovať a spravovať študentské zadania cez aplikáciu a automatizovať proces spracovania faktúr cez workflow. Požiadali vás, aby ste použili generatívnu AI na vývoj riešenia.

Ak začínate používať Copilot, môžete použiť [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), aby ste sa zoznámili s promptami. Táto knižnica obsahuje zoznam promptov, ktoré môžete použiť na tvorbu aplikácií a tokov s Copilotom. Prompty z knižnice vám tiež pomôžu predstaviť si, ako opísať svoje požiadavky Copilotovi.

### Vytvorte aplikáciu na sledovanie študentských zadaní pre náš startup

Učitelia v našom startupe mali problémy so sledovaním študentských zadaní. Používali tabuľkový kalkulátor na sledovanie zadaní, ale to sa stalo náročným na správu, keď počet študentov vzrástol. Požiadali vás, aby ste vytvorili aplikáciu, ktorá im pomôže sledovať a spravovať študentské zadania. Aplikácia by mala umožniť pridávať nové zadania, zobrazovať zadania, aktualizovať zadania a mazať zadania. Mala by tiež umožniť učiteľom a študentom zobraziť zadania, ktoré už boli ohodnotené, a tie, ktoré ešte nie.

Aplikáciu vytvoríte pomocou Copilota v Power Apps podľa nasledujúcich krokov:

1. Prejdite na domovskú obrazovku [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Pomocou textového poľa na domovskej obrazovke opíšte aplikáciu, ktorú chcete vytvoriť. Napríklad **_Chcem vytvoriť aplikáciu na sledovanie a správu študentských zadaní_**. Kliknite na tlačidlo **Odoslať**, aby ste prompt poslali AI Copilotovi.

![Popíšte aplikáciu, ktorú chcete vytvoriť](../../../translated_images/sk/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot navrhne tabuľku v Dataverse s poliami potrebnými na uloženie údajov, ktoré chcete sledovať, a niektoré ukážkové dáta. Tabuľku potom môžete prispôsobiť podľa svojich potrieb pomocou funkcie AI asistenta Copilot cez konverzačné kroky.

   > **Dôležité**: Dataverse je základná dátová platforma Power Platform. Je to platforma s nízkym kódom na ukladanie dát aplikácie. Je to plne spravovaná služba, ktorá bezpečne ukladá dáta v Microsoft Cloude a je sprístupnená vo vašom prostredí Power Platform. Obsahuje vstavané funkcie riadenia dát, ako je klasifikácia dát, sledovanie pôvodu dát, detailné riadenie prístupu a ďalšie. Viac o Dataverse sa dozviete [tu](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Navrhované polia vo vašej novej tabuľke](../../../translated_images/sk/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Učitelia chcú posielať e-maily študentom, ktorí odovzdali svoje zadania, aby ich informovali o stave ich zadaní. Môžete použiť Copilot na pridanie nového poľa do tabuľky na uloženie emailu študenta. Napríklad môžete použiť prompt: **_Chcem pridať stĺpec na uloženie emailu študenta_**. Kliknite na tlačidlo **Odoslať**, aby ste prompt poslali AI Copilotovi.

![Pridanie nového poľa](../../../translated_images/sk/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot vygeneruje nové pole a vy ho potom môžete prispôsobiť podľa svojich potrieb.


1. Keď dokončíte tabuľku, kliknite na tlačidlo **Vytvoriť aplikáciu** na vytvorenie aplikácie.

1. AI Copilot vygeneruje responzívnu aplikáciu Canvas na základe vášho popisu. Potom môžete aplikáciu prispôsobiť podľa svojich potrieb.

1. Pre učiteľov, ktorí chcú posielať e-maily študentom, môžete použiť Copilot na pridanie novej obrazovky do aplikácie. Napríklad môžete použiť nasledujúci príkaz na pridanie novej obrazovky do aplikácie: **_Chcem pridať obrazovku na odosielanie e-mailov študentom_**. Kliknite na tlačidlo **Odoslať** na odoslanie príkazu do AI Copilota.

![Pridanie novej obrazovky pomocou inštrukcie v príkaze](../../../translated_images/sk/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot vygeneruje novú obrazovku, ktorú potom môžete prispôsobiť podľa svojich potrieb.

1. Keď dokončíte aplikáciu, kliknite na tlačidlo **Uložiť** na uloženie aplikácie.

1. Ak chcete zdieľať aplikáciu s učiteľmi, kliknite na tlačidlo **Zdieľať** a potom znovu kliknite na tlačidlo **Zdieľať**. Aplikáciu môžete zdieľať s učiteľmi zadaním ich e-mailových adries.

> **Vaša domáca úloha**: Aplikácia, ktorú ste práve vytvorili, je dobrý začiatok, ale dá sa vylepšiť. Pomocou e-mailovej funkcie môžu učitelia posielať e-maily študentom iba manuálne tým, že musia zadávať ich e-maily. Môžete použiť Copilota na vytvorenie automatizácie, ktorá umožní učiteľom posielať e-maily študentom automaticky, keď odovzdajú svoje úlohy? Vaša nápoveda je, že s správnym príkazom môžete použiť Copilota v Power Automate na vytvorenie tohto.

### Vytvorte tabuľku informácií o faktúrach pre náš startup

Finančný tím nášho startupu sa snažil udržať prehľad o faktúrach. Používali tabuľku, aby sledovali faktúry, ale stalo sa to ťažko spravovateľným, keďže sa počet faktúr zvýšil. Požiadali vás, aby ste vytvorili tabuľku, ktorá im pomôže ukladať, sledovať a spravovať informácie o prijatých faktúrach. Tabuľka by mala slúžiť na vytvorenie automatizácie, ktorá vyťaží všetky informácie z faktúr a uloží ich do tabuľky. Tabuľka by tiež mala finančnému tímu umožniť zobraziť faktúry, ktoré boli zaplatené, a tie, ktoré neboli zaplatené.

Power Platform má základnú dátovú platformu nazývanú Dataverse, ktorá umožňuje ukladať dáta pre vaše aplikácie a riešenia. Dataverse poskytuje nízkonákladovú dátovú platformu na ukladanie dát aplikácie. Je to plne spravovaná služba, ktorá bezpečne ukladá dáta v Microsoft Cloud a je sprístupnená vo vašom prostredí Power Platform. Obsahuje vstavané funkcie správy dát, ako sú klasifikácia dát, sledovanie pôvodu dát, podrobná kontrola prístupu a ďalšie. Viac sa môžete dozvedieť [o Dataverse tu](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Prečo by sme mali používať Dataverse pre náš startup? Štandardné a vlastné tabuľky v Dataverse poskytujú bezpečnú a cloudovú možnosť ukladania vašich dát. Tabuľky umožňujú ukladať rôzne typy dát, podobne ako by ste mohli používať viacero pracovných listov v jednom Excel súbore. Tabuľky môžete použiť na ukladanie dát špecifických pre vašu organizáciu alebo obchodné potreby. Niektoré z výhod, ktoré náš startup z používania Dataverse získa, zahŕňajú, ale nie sú obmedzené na:

- **Jednoduché spravovanie**: Metadata aj dáta sa ukladajú v cloude, takže sa nemusíte starať o detaily, ako sú uložené alebo spravované. Môžete sa sústrediť na tvorbu vašich aplikácií a riešení.

- **Bezpečné**: Dataverse poskytuje bezpečné cloudové úložisko pre vaše dáta. Môžete kontrolovať, kto má prístup k dátam vo vašich tabuľkách a ako k nim môže pristupovať pomocou zabezpečenia založeného na rolách.

- **Bohaté metadáta**: Typy dát a vzťahy sa používajú priamo v Power Apps.

- **Logika a validácia**: Môžete použiť obchodné pravidlá, vypočítané polia a validačné pravidlá na vynútenie obchodnej logiky a udržanie presnosti dát.

Teraz, keď viete, čo je Dataverse a prečo ho používať, pozrime sa, ako môžete použiť Copilota na vytvorenie tabuľky v Dataverse, ktorá splní požiadavky nášho finančného tímu.

> **Poznámka** : Túto tabuľku použijete v nasledujúcej časti na vytvorenie automatizácie, ktorá vyťaží všetky informácie z faktúr a uloží ich do tabuľky.

Na vytvorenie tabuľky v Dataverse pomocou Copilota postupujte podľa nasledovných krokov:

1. Prejdite na [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) domovskú obrazovku.

2. Na ľavom navigačnom paneli vyberte **Tabuľky** a potom kliknite na **Opísať novú tabuľku**.

![Vyberte novú tabuľku](../../../translated_images/sk/describe-new-table.0792373eb757281e.webp)

1. Na obrazovke **Opísať novú tabuľku** použite textové pole na popis tabuľky, ktorú chcete vytvoriť. Napríklad, **_Chcem vytvoriť tabuľku na ukladanie informácií o faktúrach_**. Kliknite na tlačidlo **Odoslať** na odoslanie príkazu do AI Copilota.

![Opísať tabuľku](../../../translated_images/sk/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot navrhne tabuľku Dataverse s poľami, ktoré potrebujete na uloženie dát, ktoré chcete sledovať, a so vzorovými dátami. Potom môžete tabuľku upraviť podľa svojich potrieb pomocou asistenta AI Copilot v konverzačných krokoch.

![Navrhnutá tabuľka Dataverse](../../../translated_images/sk/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finančný tím chce poslať e-mail dodávateľovi, aby ich informoval o aktuálnom stave ich faktúry. Môžete použiť Copilota na pridanie nového poľa do tabuľky na uloženie e-mailu dodávateľa. Napríklad môžete použiť tento príkaz na pridanie nového poľa: **_Chcem pridať stĺpec na uloženie e-mailu dodávateľa_**. Kliknite na tlačidlo **Odoslať** na odoslanie príkazu do AI Copilota.

1. AI Copilot vygeneruje nové pole, ktoré potom môžete prispôsobiť svojim potrebám.

1. Keď dokončíte tabuľku, kliknite na tlačidlo **Vytvoriť** na vytvorenie tabuľky.

## AI modely v Power Platform pomocou AI Builder

AI Builder je nízkonákladová AI funkcia dostupná v Power Platform, ktorá umožňuje použiť AI modely na automatizáciu procesov a predpovedanie výsledkov. Pomocou AI Builder môžete priniesť AI do vašich aplikácií a tokov, ktoré sa pripájajú k vašim dátam v Dataverse alebo v rôznych cloudových dátových zdrojoch, ako sú SharePoint, OneDrive alebo Azure.

## Predpripravené AI modely vs vlastné AI modely

AI Builder poskytuje dva typy AI modelov: predpripravené AI modely a vlastné AI modely. Predpripravené AI modely sú pripravené na použitie, sú trénované spoločnosťou Microsoft a dostupné v Power Platform. Pomáhajú vám pridať inteligenciu do vašich aplikácií a tokov bez potreby zhromažďovať dáta, následne tvoriť, trénovať a publikovať vlastné modely. Môžete použiť tieto modely na automatizáciu procesov a predpovedanie výsledkov.

Niektoré z predpripravených AI modelov dostupných v Power Platform zahŕňajú:

- **Extrahovanie kľúčových fráz**: Tento model získava kľúčové frázy z textu.
- **Detekcia jazyka**: Tento model zisťuje jazyk textu.
- **Analýza sentimentu**: Tento model zisťuje pozitívny, negatívny, neutrálny alebo zmiešaný sentiment v texte.
- **Čítačka vizitiek**: Tento model získava informácie z vizitiek.
- **Rozpoznávanie textu**: Tento model extrahuje text z obrázkov.
- **Detekcia objektov**: Tento model zisťuje a extrahuje objekty z obrázkov.
- **Spracovanie dokumentov**: Tento model získava informácie z formulárov.
- **Spracovanie faktúr**: Tento model získava informácie z faktúr.

S vlastnými AI modelmi môžete do AI Builder priniesť vlastný model, aby mohol fungovať ako akýkoľvek vlastný model AI Builder, čo vám umožňuje trénovať model s vlastnými dátami. Tieto modely môžete použiť na automatizáciu procesov a predpovedanie výsledkov v Power Apps aj Power Automate. Pri používaní vlastného modelu platia určité obmedzenia. Viac o týchto [obmedzeniach](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![modely AI Builder](../../../translated_images/sk/ai-builder-models.8069423b84cfc47f.webp)

## Úloha č. 2 - Vytvorte tok spracovania faktúr pre náš startup

Finančný tím mal problémy so spracovaním faktúr. Používali tabuľku na sledovanie faktúr, ale stalo sa to ťažko spravovateľným, keďže sa počet faktúr zvýšil. Požiadali vás o vytvorenie pracovného toku, ktorý im pomôže spracovávať faktúry pomocou AI. Pracovný tok by mal umožniť vyťažiť informácie z faktúr a uložiť ich do tabuľky Dataverse. Pracovný tok by im tiež mal umožniť odoslať e-mail finančnému tímu s vyťaženými informáciami.

Teraz, keď viete, čo je AI Builder a prečo ho používať, pozrime sa, ako môžete použiť AI model Spracovanie faktúr, ktorý sme prebrali skôr, na vytvorenie pracovného toku, ktorý pomôže finančnému tímu spracovávať faktúry.

Na vytvorenie pracovného toku, ktorý pomôže finančnému tímu spracovávať faktúry pomocou AI modelu Spracovanie faktúr v AI Builder, postupujte podľa krokov nižšie:

1. Prejdite na [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) domovskú obrazovku.

2. Použite textové pole na domovskej obrazovke na opísanie pracovného toku, ktorý chcete vytvoriť. Napríklad, **_Spracovať faktúru, keď dorazí do mojej schránky_**. Kliknite na tlačidlo **Odoslať** na odoslanie príkazu do AI Copilota.

   ![Copilot power automate](../../../translated_images/sk/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot navrhne akcie, ktoré potrebujete na vykonanie úlohy, ktorú chcete automatizovať. Môžete kliknúť na tlačidlo **Ďalej** pre postupovanie ďalšími krokmi.

4. V ďalšom kroku vás Power Automate vyzve na nastavenie pripojení potrebných pre tok. Keď skončíte, kliknite na tlačidlo **Vytvoriť tok** na vytvorenie toku.

5. AI Copilot vygeneruje tok, ktorý potom môžete prispôsobiť podľa svojich potrieb.

6. Aktualizujte spúšťač toku a nastavte **Zložku** na zložku, kde budú faktúry uložené. Napríklad môžete nastaviť zložku na **Doručená pošta**. Kliknite na **Zobraziť rozšírené možnosti** a nastavte **Iba s prílohami** na **Áno**. To zabezpečí, že tok bude bežať iba, keď príde e-mail s prílohou do tejto zložky.

7. Odstráňte nasledujúce akcie z toku: **HTML na text**, **Zložiť**, **Zložiť 2**, **Zložiť 3** a **Zložiť 4**, pretože ich nebudete používať.

8. Odstráňte akciu **Podmienka** z toku, pretože ju nebudete používať. Malo by to vyzerať ako na nasledujúcom obrázku:

   ![power automate, odstrániť akcie](../../../translated_images/sk/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Kliknite na tlačidlo **Pridať akciu** a vyhľadajte **Dataverse**. Vyberte akciu **Pridať nový riadok**.

10. V akcii **Extrahovať informácie z faktúr** aktualizujte **Súbor faktúry** tak, aby smeroval na **Obsah prílohy** z e-mailu. To zabezpečí, že tok vyťaží informácie z prílohy faktúry.

11. Vyberte tabuľku, ktorú ste vytvorili skôr. Napríklad vyberte tabuľku **Informácie o faktúre**. Vyberte dynamický obsah z predchádzajúcej akcie na vyplnenie nasledujúcich polí:

    - ID
    - Suma
    - Dátum
    - Názov
    - Stav - nastavte **Stav** na **Čaká sa**.
    - E-mail dodávateľa - použite dynamický obsah **Od** z udalosti **Keď dorazí nový e-mail**.

    ![power automate pridať riadok](../../../translated_images/sk/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Keď dokončíte tok, kliknite na tlačidlo **Uložiť** na uloženie toku. Potom môžete tok otestovať odoslaním e-mailu s faktúrou do zložky, ktorú ste nastavili v spúšťači.

> **Vaša domáca úloha**: Tok, ktorý ste práve vytvorili, je dobrým začiatkom, teraz musíte premýšľať, ako vytvoriť automatizáciu, ktorá umožní nášmu finančnému tímu poslať e-mail dodávateľovi a informovať ich o aktuálnom stave ich faktúry. Vaša nápoveda: tok musí bežať, keď sa zmení stav faktúry.

## Použitie AI modelu na generovanie textu v Power Automate

AI model Create Text with GPT v AI Builder umožňuje generovať text na základe príkazu a je poháňaný službou Microsoft Azure OpenAI Service. Vďaka tejto funkcii môžete začleniť technológiu GPT (Generative Pre-Trained Transformer) do vašich aplikácií a tokov na vytváranie rôznych automatizovaných tokov a prehľadných aplikácií.

GPT modely prešli rozsiahlym trénovaním na veľkom množstve dát, čo im umožňuje produkovať text, ktorý veľmi pripomína ľudský jazyk pri zadaní príkazu. Keď sa integrujú do automatizácie pracovných tokov, AI modely ako GPT možno využiť na zefektívnenie a automatizáciu širokej škály úloh.

Napríklad môžete vytvoriť toky na automatické generovanie textu pre rôzne použitia, ako sú návrhy e-mailov, popisy produktov a ďalšie. Model môžete tiež použiť na generovanie textu pre rôzne aplikácie, ako sú chatboti a aplikácie zákazníckej podpory, ktoré umožňujú agentom zákazníckej podpory efektívne a účinne reagovať na požiadavky zákazníkov.

![vytvoriť príkaz](../../../translated_images/sk/create-prompt-gpt.69d429300c2e870a.webp)


Ak sa chcete naučiť, ako používať tento AI model v Power Automate, prejdite si modul [Pridanie inteligencie pomocou AI Builder a GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Skvelá práca! Pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zvyšovali svoje vedomosti o Generatívnej AI!

Chcete si prispôsobiť Copilot a získať z neho viac? Preskúmajte [Úžasný Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — kolekciu príspevkov od komunitných členov obsahujúcu inštrukcie, agentov, zručnosti a konfigurácie, ktoré vám pomôžu čo najlepšie využiť GitHub Copilot.

Prejdite do Lekcie 11, kde si ukážeme, ako [integrovať Generatívnu AI s volaním funkcií](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->