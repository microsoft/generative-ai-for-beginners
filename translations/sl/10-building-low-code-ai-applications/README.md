# Gradnja nizkokodnih AI aplikacij

[![Gradnja nizkokodnih AI aplikacij](../../../translated_images/sl/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Kliknite zgornjo sliko, da si ogledate video te lekcije)_

## Uvod

Zdaj, ko smo se naučili, kako zgraditi aplikacije za ustvarjanje slik, pa se pogovorimo o nizkodu. Generativna AI se lahko uporablja za različna področja, vključno z nizkodom, vendar kaj je nizkod in kako mu lahko dodamo AI?

Gradnja aplikacij in rešitev je postala lažja tako za tradicionalne razvijalce kot tudi za ne-razvijalce z uporabo platform za razvijanje nizkodnih programov. Platforme za nizkodno razvoj omogočajo, da gradite aplikacije in rešitve z malo ali nič kode. To dosežejo z zagotavljanjem vizualnega razvojnega okolja, ki omogoča povleci in spusti komponente za gradnjo aplikacij in rešitev. To omogoča hitrejšo gradnjo aplikacij in rešitev z manj resursov. V tej lekciji se poglobimo v to, kako uporabljati nizkod in kako izboljšati nizkodni razvoj z AI z uporabo Power Platform.

Power Platform organizacijam ponuja priložnost, da okrepi svoje ekipe, da same gradijo svoje rešitve preko intuitivnega nizkodnega ali nekodnega okolja. To okolje pomaga poenostaviti proces gradnje rešitev. Z Power Platform lahko rešitve zgradite v dneh ali tednih namesto v mesecih ali letih. Power Platform sestavlja pet ključnih produktov: Power Apps, Power Automate, Power BI, Power Pages in Copilot Studio.

Ta lekcija zajema:

- Uvod v generativno AI v Power Platform
- Uvod v Copilot in kako ga uporabljati
- Uporabo generativne AI za gradnjo aplikacij in tokov v Power Platform
- Razumevanje AI modelov v Power Platform z AI Builder
- Gradnjo inteligentnih agentov z Microsoft Copilot Studio

## Cilji učenja

Na koncu te lekcije boste lahko:

- Razumeli, kako Copilot deluje v Power Platform.

- Zgradili aplikacijo za sledenje študentskih nalog za naše izobraževalno zagonsko podjetje.

- Zgradili tok za procesiranje računov, ki uporablja AI za izvleček informacij iz računov.

- Uporabili najboljše prakse pri uporabi AI modela Ustvari besedilo z GPT.

- Razumeli, kaj je Microsoft Copilot Studio in kako graditi inteligentne agente z njim.

Orodja in tehnologije, ki jih boste uporabili v tej lekciji, so:

- **Power Apps**, za aplikacijo za sledenje študentskih nalog, ki ponuja nizkodno razvojno okolje za gradnjo aplikacij za sledenje, upravljanje in interakcijo s podatki.

- **Dataverse**, za shranjevanje podatkov aplikacije za sledenje študentskih nalog, kjer Dataverse zagotavlja nizkodno podatkovno platformo za shranjevanje podatkov aplikacije.

- **Power Automate**, za tok procesiranja računov, kjer boste imeli nizkodno razvojno okolje za gradnjo delovnih tokov za avtomatizacijo procesa procesiranja računov.

- **AI Builder**, za AI model procesiranja računov, kjer boste uporabili pripravljene AI modele za procesiranje računov za naše zagonsko podjetje.

## Generativna AI v Power Platform

Izboljšanje nizkodnega razvoja in aplikacij z generativno AI je ključno področje fokusa za Power Platform. Cilj je omogočiti vsem gradnjo AI-podprtih aplikacij, spletnih strani, nadzornih plošč in avtomatizacijo procesov z AI, _brez potrebe po znanju podatkovne znanosti_. Ta cilj je dosežen z integracijo generativne AI v nizkodno razvojno izkušnjo v Power Platform v obliki Copilota in AI Builderja.

### Kako to deluje?

Copilot je AI pomočnik, ki vam omogoča gradnjo rešitev v Power Platform z opisovanjem vaših zahtev v vrsti pogovornih korakov z uporabo naravnega jezika. Na primer, lahko svojemu AI pomočniku naročite, naj navede, katera polja bo vaša aplikacija uporabila, in ustvari tako aplikacijo kot osnovni podatkovni model, ali pa lahko določite, kako nastaviti tok v Power Automate.

Funkcionalnosti, ki jih poganja Copilot, lahko uporabite kot funkcijo na zaslonih vaše aplikacije, da omogočite uporabnikom odkrivanje vpogledov skozi pogovorne interakcije.

AI Builder je nizkodna AI zmogljivost v Power Platform, ki vam omogoča uporabo AI modelov za pomoč pri avtomatizaciji procesov in napovedovanju izidov. Z AI Builderjem lahko prinesete AI v svoje aplikacije in tokove, ki se povezujejo z vašimi podatki v Dataverse ali v različnih oblačnih virov podatkov, kot so SharePoint, OneDrive ali Azure.

Copilot je na voljo v vseh produktih Power Platform: Power Apps, Power Automate, Power BI, Power Pages in Copilot Studio (prej Power Virtual Agents). AI Builder je na voljo v Power Apps in Power Automate. V tej lekciji se bomo osredotočili na uporabo Copilota in AI Builderja v Power Apps in Power Automate za gradnjo rešitve za naše izobraževalno zagonsko podjetje.

### Copilot v Power Apps

Kot del Power Platform, Power Apps ponuja nizkodno razvojno okolje za gradnjo aplikacij za sledenje, upravljanje in interakcijo s podatki. Je komplet storitev za razvoj aplikacij s prilagodljivo podatkovno platformo in možnostjo povezovanja z oblačnimi storitvami in lokalnimi podatki. Power Apps vam omogoča gradnjo aplikacij, ki delujejo v brskalnikih, tablicah in telefonih, ter jih je možno deliti s sodelavci. Power Apps uporabnikom olajša razvoj aplikacij z enostavnim vmesnikom, da lahko vsak poslovni uporabnik ali izkušen razvijalec gradi prilagojene aplikacije. Izkušnja razvoja aplikacij je prav tako izboljšana z generativno AI preko Copilota.

Funkcija AI pomočnika copilot v Power Apps vam omogoča, da opišete, kakšno aplikacijo potrebujete in katere informacije naj vaša aplikacija sledi, zbira ali prikazuje. Copilot nato ustvari odzivno aplikacijo Canvas, ki temelji na vašem opisu. Nato lahko prilagodite aplikacijo, da izpolnjuje vaše potrebe. AI Copilot prav tako ustvari in predlaga Dataverse tabelo s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite spremljati, in nekaj vzorčnih podatkov. Kasneje v tej lekciji si bomo ogledali, kaj je Dataverse in kako ga lahko uporabite v Power Apps. Nato lahko tabelo prilagodite svojim potrebam z uporabo funkcije AI Copilot pomočnika preko pogovornih korakov. Ta funkcija je enostavno dostopna s domačega zaslona Power Apps.

### Copilot v Power Automate

Kot del Power Platform, Power Automate uporabnikom omogoča ustvarjanje avtomatiziranih delovnih tokov med aplikacijami in storitvami. Pomaga avtomatizirati ponavljajoče se poslovne procese, kot so komunikacija, zbiranje podatkov in odobritve odločitev. Njegov preprost vmesnik omogoča uporabnikom z vsemi tehničnimi zmožnostmi (od začetnikov do izkušenih razvijalcev) avtomatizirati delovne naloge. Izkušnja razvoja delovnih tokov je prav tako izboljšana z generativno AI preko Copilota.

Funkcija AI pomočnika copilot v Power Automate vam omogoča, da opišete, kakšen tok potrebujete in katere akcije želite, da vaš tok izvede. Copilot nato ustvari tok na podlagi vašega opisa. Nato lahko tok prilagodite, da izpolnjuje vaše potrebe. AI Copilot prav tako ustvari in predlaga akcije, ki jih potrebujete za izvedbo naloge, ki jo želite avtomatizirati. Kasneje v tej lekciji si bomo ogledali, kaj so tokovi in kako jih lahko uporabljate v Power Automate. Nato lahko prilagodite akcije svojim potrebam z uporabo funkcije AI Copilot pomočnika preko pogovornih korakov. Ta funkcija je enostavno dostopna s domačega zaslona Power Automate.

## Gradnja inteligentnih agentov z Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (prej Power Virtual Agents) je nizkodni član Power Platform za gradnjo **AI agentov** — pogovornih copilotov, ki lahko odgovarjajo na vprašanja, izvajajo akcije in avtomatizirajo naloge v imenu vaših uporabnikov. Tako kot ostali del Power Platform, te agente gradite v vizualni izkušnji, usmerjeni na naravni jezik: opišete, kaj želite, da agent naredi, in Copilot Studio pomaga strukturirati njegove navodila, znanje in dejanja.

Za naše izobraževalno zagonsko podjetje lahko zgradite agenta, ki odgovarja na vprašanja študentov o tečajih, preverja roke za naloge in celo pošilja elektronska sporočila inštruktorju — vse to brez pisanja kode.

Tukaj je nekaj najnovejših zmogljivosti, ki naredijo Copilot Studio zmogljiv:

- **Generativni odgovori iz vašega znanja**. Namesto ročnega oblikovanja vsakega pogovora lahko povežete **vire znanja** — javne spletne strani, SharePoint, OneDrive, Dataverse, naložene datoteke ali podatke podjetja prek konektorjev — in agent generira utemeljene odgovore iz njih.

- **Generativna orkestracija**. Namesto da bi se zanašal na rigidne sprožilne fraze, agent uporablja AI, da razume zahtevo in dinamično odloči, kateri viri znanja, teme in dejanja se kombinirajo za izpolnitev zahteve, vključno z zaporednim povezovanjem več korakov.

- **Dejanja in konektorji**. Agenti lahko *delajo* stvari, ne samo klepetajo. Agentu lahko dodelite dejanja, podprta z več kot 1.500 pripravljenimi konektorji Power Platform, delovnimi tokovi Power Automate, lastnimi REST API-ji, pozivi ali strežniki **Model Context Protocol (MCP)**.

- **Avtonomni agenti**. Agentom ni omejeno odgovarjanje v klepetalnem oknu. Lahko zgradite **avtonomne agente**, ki se sprožijo ob dogodkih — kot je novo elektronsko sporočilo, nov zapis v Dataverse ali naložena datoteka — in nato delujejo v ozadju za dokončanje naloge.

- **Orkestracija več agentov**. Agenti lahko kličejo druge agente. Agent Copilot Studio lahko preda nalogo drugim agentom ali pa ga razširijo drugi agenti, tudi agenti, objavljeni v Microsoft 365 Copilot in agenti, zgrajeni v Microsoft Foundry.

- **Izbor modela**. Poleg vgrajenih modelov lahko prinesete modele iz kataloga modelov Microsoft Foundry, da prilagodite, kako vaš agent sklepa in odgovarja.

- **Objava kjerkoli**. Ko je agent zgrajen, ga lahko objavite na več kanalih — Microsoft Teams, Microsoft 365 Copilot, spletna stran ali lastna aplikacija in več — z upravljanjem varnosti, avtentikacije in analitike preko upravljavske izkušnje Power Platform.

Svoj prvi agent lahko začnete graditi na [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) in se naučite več v [dokumentaciji Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Naloga: Upravljanje študentskih nalog in računov za naše zagonsko podjetje z uporabo Copilota

Naše zagonsko podjetje ponuja spletne tečaje študentom. Podjetje hitro raste in zdaj težko dohaja povpraševanje po svojih tečajih. Najeli so vas kot razvijalca Power Platform, da jim pomagate zgraditi nizkodno rešitev za upravljanje šolskih nalog in računov. Njihova rešitev naj jim omogoči sledenje in upravljanje študentskih nalog preko aplikacije ter avtomatizacijo procesa obdelave računov preko delovnega toka. Prosili so vas, da pri razvoju rešitve uporabite generativno AI.

Ko začnete uporabljati Copilot, lahko uporabite [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) za začetek s pozivi. Ta knjižnica vsebuje seznam pozivov, ki jih lahko uporabite za gradnjo aplikacij in tokov s Copilotom. Prav tako lahko s temi pozivi dobite idejo, kako opisati svoje zahteve Copilotu.

### Zgradite aplikacijo za sledenje študentskih nalog za naše zagonsko podjetje

Izobraževalci v našem zagonskem podjetju so imeli težave z vodenjem evidence študentskih nalog. Uporabljali so preglednico za sledenje nalogam, vendar je to postalo težavno za upravljanje, saj se je število študentov povečalo. Prosili so vas, da zgradite aplikacijo, ki jim bo pomagala slediti in upravljati študentske naloge. Aplikacija naj omogoča dodajanje novih nalog, ogled nalog, posodabljanje nalog in brisanje nalog. Prav tako naj omogoča izobraževalcem in študentom ogled nalog, ki so ocenjene, in tistih, ki niso ocenjene.

Aplikacijo boste zgradili z uporabo Copilota v Power Apps po naslednjih korakih:

1. Pojdite na domači zaslon [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Uporabite besedilno polje na domačem zaslonu za opis aplikacije, ki jo želite zgraditi. Na primer, **_Hočem zgraditi aplikacijo za sledenje in upravljanje študentskih nalog_**. Kliknite gumb **Pošlji**, da pošljete poziv AI Copilotu.

![Opišite aplikacijo, ki jo želite zgraditi](../../../translated_images/sl/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot bo predlagal Dataverse tabelo s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite spremljati, in nekaj vzorčnih podatkov. Nato lahko prilagodite tabelo, da izpolnjuje vaše potrebe z uporabo funkcije AI Copilot pomočnika preko pogovornih korakov.

   > **Pomembno**: Dataverse je osnovna podatkovna platforma za Power Platform. Je nizkodna podatkovna platforma za shranjevanje podatkov aplikacije. Je popolnoma upravljana storitev, ki varno shranjuje podatke v Microsoftovem oblaku in je zagotovljena znotraj vašega Power Platform okolja. Ponuja vgrajene zmogljivosti upravljanja podatkov, kot so klasifikacija podatkov, izvor podatkov, finozrnat nadzor dostopa in še več. Več o Dataverse lahko izveste [tukaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Predlagana polja v vaši novi tabeli](../../../translated_images/sl/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Izobraževalci želijo pošiljati elektronske pošte študentom, ki so predali svoje naloge, da jih obveščajo o napredku njihovih nalog. Uporabite lahko Copilot, da dodate novo polje v tabelo za shranjevanje elektronskih naslovov študentov. Na primer, uporabite naslednji poziv za dodajanje novega polja v tabelo: **_Hočem dodati stolpec za shranjevanje elektronskega naslova študenta_**. Kliknite gumb **Pošlji**, da pošljete poziv AI Copilotu.

![Dodajanje novega polja](../../../translated_images/sl/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot bo ustvaril novo polje, ki ga lahko nato prilagodite, da izpolnjuje vaše potrebe.


1. Ko končate s tabelo, kliknite na gumb **Ustvari aplikacijo** za ustvarjanje aplikacije.

1. AI Copilot bo ustvaril odzivno Canvas aplikacijo na podlagi vašega opisa. Nato lahko prilagodite aplikacijo po svojih potrebah.

1. Za izobraževalce, da pošiljajo e-pošto študentom, lahko uporabite Copilot, da dodate nov zaslon aplikaciji. Na primer, lahko uporabite naslednje navodilo, da dodate nov zaslon aplikaciji: **_Želim dodati zaslon za pošiljanje e-pošte študentom_**. Kliknite na gumb **Pošlji**, da pošljete navodilo AI Copilotu.

![Adding a new screen via a prompt instruction](../../../translated_images/sl/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot bo ustvaril nov zaslon, ki ga nato lahko prilagodite svojim potrebam.

1. Ko končate z aplikacijo, kliknite gumb **Shrani**, da shranite aplikacijo.

1. Da delite aplikacijo z izobraževalci, kliknite gumb **Deli** in nato ponovno kliknite gumb **Deli**. Nato lahko aplikacijo delite z izobraževalci tako, da vnesete njihove e-poštne naslove.

> **Vaša domača naloga**: Aplikacija, ki ste jo pravkar ustvarili, je dober začetek, vendar jo je mogoče izboljšati. Z funkcijo e-pošte lahko izobraževalci pošiljajo e-pošto študentom le ročno, tako da vnesejo njihove e-poštne naslove. Ali lahko uporabite Copilot za izdelavo avtomatizacije, ki bo izobraževalcem omogočila samodejno pošiljanje e-pošte študentom, ko ti oddajo svoje naloge? Namig: z ustreznim navodilom lahko uporabite Copilot v Power Automate za izdelavo tega.

### Ustvarite tabelo informacij o računih za naš startup

Finančna ekipa našega startupa ima težave s sledenjem računov. Uporabljali so preglednico za pregled računov, vendar je s povečanjem števila računov postalo težko upravljati z njimi. Prosili so vas, da ustvarite tabelo, ki jim bo pomagala shranjevati, slediti in upravljati podatke o prejetih računih. Tabela naj se uporablja za izdelavo avtomatizacije, ki bo iz vseh podatkov o računih izvlekla informacije in jih shranila v tabelo. Tabela naj tudi omogoča finančni ekipi ogled plačanih in neplačanih računov.

Power Platform ima osnovno podatkovno platformo imenovano Dataverse, ki omogoča shranjevanje podatkov za vaše aplikacije in rešitve. Dataverse ponuja nizkoodno podatkovno platformo za shranjevanje podatkov aplikacije. Gre za popolnoma upravljano storitev, ki varno shranjuje podatke v Microsoftovi oblaku in je zagotovljena znotraj vašega Power Platform okolja. Vsebuje vgrajene zmogljivosti upravljanja podatkov, kot so klasifikacija podatkov, sledljivost podatkov, podrobna kontrola dostopa in več. Več o Dataverse si lahko preberete [tukaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Zakaj bi morali za naš startup uporabljati Dataverse? Standardne in prilagojene tabele v Dataverse nudijo varno in oblačno opcijo za shranjevanje vaših podatkov. Tabele omogočajo shranjevanje različnih tipov podatkov, podobno kot uporabljate več listov v eni Excelovi delovni knjižici. Tabele lahko uporabljate za shranjevanje podatkov, ki so specifični za vašo organizacijo ali poslovne potrebe. Nekatere prednosti, ki jih bo naš startup pridobil z uporabo Dataverse, vključujejo med drugim:

- **Enostavno upravljanje**: Tako metapodatki kot podatki so shranjeni v oblaku, zato se vam ni treba ukvarjati s podrobnostmi o tem, kako so shranjeni ali upravljani. Lahko se osredotočite na izgradnjo svojih aplikacij in rešitev.

- **Varnost**: Dataverse nudi varno in oblačno opcijo za shranjevanje vaših podatkov. Lahko nadzorujete, kdo ima dostop do podatkov v vaših tabelah in kako do njih dostopa, s pomočjo varnosti, ki temelji na vlogah.

- **Bogati metapodatki**: Tipi podatkov in odnosi se uporabljajo neposredno znotraj Power Apps

- **Logika in validacija**: Uporabite lahko poslovna pravila, izračunana polja in pravila za validacijo za uveljavljanje poslovne logike in ohranjanje natančnosti podatkov.

Sedaj ko veste, kaj je Dataverse in zakaj ga uporabiti, poglejmo, kako lahko uporabite Copilot za ustvarjanje tabele v Dataverse, ki bo ustrezala zahtevam naše finančne ekipe.

> **Opomba**: To tabelo boste uporabili v naslednjem razdelku za izdelavo avtomatizacije, ki bo izvlekla vse podatke o računih in jih shranila v tabelo.

Za ustvarjanje tabele v Dataverse s pomočjo Copilot sledite spodnjim korakom:

1. Pojdite na domačo stran [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na levi navigacijski vrstici izberite **Tabele** in nato kliknite na **Opisi novo tabelo**.

![Select new table](../../../translated_images/sl/describe-new-table.0792373eb757281e.webp)

1. Na zaslonu **Opisi novo tabelo** uporabite besedilno polje za opis tabele, ki jo želite ustvariti. Na primer: **_Želim ustvariti tabelo za shranjevanje informacij o računih_**. Kliknite gumb **Pošlji**, da pošljete navodilo AI Copilotu.

![Describe the table](../../../translated_images/sl/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot bo predlagal Dataverse tabelo s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite slediti, in nekaj vzorčnih podatkov. Nato lahko prilagodite tabelo svojim potrebam s pomočjo asistenta AI Copilot preko pogovornih korakov.

![Suggested Dataverse table](../../../translated_images/sl/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finančna ekipa želi poslati e-pošto dobavitelju, da ga obvesti o trenutnem statusu njihovega računa. Uporabite Copilot, da dodate novo polje v tabelo za shranjevanje e-poštnega naslova dobavitelja. Na primer, lahko uporabite naslednje navodilo: **_Želim dodati stolpec za shranjevanje e-poštnega naslova dobavitelja_**. Kliknite gumb **Pošlji**, da pošljete navodilo AI Copilotu.

1. AI Copilot bo ustvaril novo polje, ki ga nato lahko prilagodite svojim potrebam.

1. Ko končate s tabelo, kliknite gumb **Ustvari**, da ustvarite tabelo.

## AI modeli v Power Platform z AI Builder

AI Builder je nizkoodna AI zmogljivost v Power Platform, ki vam omogoča uporabo AI modelov za avtomatizacijo procesov in napovedovanje izidov. Z AI Builder lahko v svoje aplikacije in tokove povežete umetno inteligenco, ki se povezuje z vašimi podatki v Dataverse ali v različnih podatkovnih virih v oblaku, kot so SharePoint, OneDrive ali Azure.

## Vnaprej zgrajeni AI modeli vs. Prilagojeni AI modeli

AI Builder nudi dve vrsti AI modelov: vnaprej zgrajene AI modele in prilagojene AI modele. Vnaprej zgrajeni AI modeli so že pripravljeni za uporabo in jih je usposobil Microsoft ter so na voljo v Power Platform. Pomagajo vam dodati inteligenco v vaše aplikacije in tokove brez potrebe po zbiranju podatkov ter gradnji, usposabljanju in objavi lastnih modelov. Te modele lahko uporabite za avtomatizacijo procesov in napovedovanje izidov.

Nekateri od vnaprej zgrajenih AI modelov, ki so na voljo v Power Platform, vključujejo:

- **Izvleček ključnih fraz**: Ta model izvleče ključne fraze iz besedila.
- **Prepoznavanje jezika**: Ta model prepozna jezik besedila.
- **Analiza sentimenta**: Ta model zazna pozitiven, negativen, nevtralen ali mešan sentiment v besedilu.
- **Branje vizitk**: Ta model izvleče informacije iz vizitk.
- **Prepoznavanje besedila**: Ta model izvleče besedilo iz slik.
- **Detekcija predmetov**: Ta model zazna in izvleče predmete iz slik.
- **Obdelava dokumentov**: Ta model izvleče informacije iz obrazcev.
- **Obdelava računov**: Ta model izvleče informacije iz računov.

S prilagojenimi AI modeli lahko v AI Builder pripeljete svoj model, da deluje kot kateri koli prilagojeni AI model, kar vam omogoča usposabljanje z vašimi lastnimi podatki. Te modele lahko uporabite za avtomatizacijo procesov in napovedovanje izidov tako v Power Apps kot Power Automate. Pri uporabi lastnega modela veljajo omejitve. Več o teh [omejitvah](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst) preberite tukaj.

![AI builder models](../../../translated_images/sl/ai-builder-models.8069423b84cfc47f.webp)

## Domača naloga #2 - Ustvari tok za obdelavo računov za naš startup

Finančna ekipa ima težave z obdelavo računov. Uporabljali so preglednico za sledenje računom, vendar je s povečanjem števila postalo težko upravljati. Prosili so vas, da ustvarite potek dela, ki jim bo pomagal obdelati račune z uporabo umetne inteligence. Potek dela naj jim omogoča izvlečenje informacij iz računov in shranjevanje teh podatkov v Dataverse tabelo. Prav tako naj jim omogoča pošiljanje e-pošte finančni ekipi z izvlečenimi informacijami.

Sedaj ko veste, kaj je AI Builder in zakaj ga uporabiti, poglejmo, kako lahko uporabite AI model za obdelavo računov v AI Builder, ki smo ga prej omenili, za izdelavo poteka dela, ki bo finančni ekipi pomagal obdelati račune.

Za izdelavo poteka dela, ki bo finančni ekipi pomagal obdelati račune z uporabo AI modela za obdelavo računov v AI Builder, sledite spodnjim korakom:

1. Pojdite na domačo stran [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Uporabite besedilno polje na domači strani, da opišete potek dela, ki ga želite izdelati. Na primer: **_Obdelaj račun, ko prispe v moj poštni predal_**. Kliknite gumb **Pošlji**, da pošljete navodilo AI Copilotu.

   ![Copilot power automate](../../../translated_images/sl/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot bo predlagal dejanja, ki jih morate izvesti za opravljanje naloge, ki jo želite avtomatizirati. Kliknete lahko gumb **Naprej**, da nadaljujete z naslednjimi koraki.

4. V naslednjem koraku vas bo Power Automate pozval, da nastavite povezave, ki so potrebne za tok. Ko končate, kliknite gumb **Ustvari tok**, da ustvarite tok.

5. AI Copilot bo ustvaril tok, ki ga nato lahko prilagodite svojim potrebam.

6. Posodobite sprožilec toka in nastavite **Mapa** na mapo, v katero bodo računi shranjeni. Na primer, nastavite mapo na **Prejeto**. Kliknite na **Pokaži napredne možnosti** in **Samo z prilogami** nastavite na **Da**. To bo zagotovilo, da se tok izvede samo, ko prejmete e-pošto s prilogo v določeni mapi.

7. Odstranite naslednja dejanja iz toka: **HTML v besedilo**, **Sestavi**, **Sestavi 2**, **Sestavi 3** in **Sestavi 4**, ker jih ne boste uporabljali.

8. Odstranite dejanje **Pogoj** iz toka, ker ga ne boste uporabljali. Izgledati mora podobno kot na spodnjem posnetku zaslona:

   ![power automate, remove actions](../../../translated_images/sl/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Kliknite gumb **Dodaj dejanje** in poiščite **Dataverse**. Izberite dejanje **Dodaj novo vrstico**.

10. Na dejanju **Izvleci informacije iz računov** posodobite **Datoteko računa** tako, da kaže na **Vsebino priloge** iz e-pošte. To bo zagotovilo, da tok izvleče informacije iz priloge računa.

11. Izberite tabelo, ki ste jo prej ustvarili. Na primer, izberite tabelo **Informacije o računu**. Izberite dinamične vsebine iz prejšnjega dejanja, da napolnite naslednja polja:

    - ID
    - Znesek
    - Datum
    - Ime
    - Status - Nastavite **Status** na **V teku**.
    - E-pošta dobavitelja - Uporabite dinamično vsebino **Od** iz sprožilca **Ko prispe nova e-pošta**.

    ![power automate add row](../../../translated_images/sl/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Ko končate s tokom, kliknite gumb **Shrani**, da shranite tok. Nato lahko preizkusite tok tako, da pošljete e-pošto z računom v mapo, ki ste jo določili v sprožilcu.

> **Vaša domača naloga**: Tok, ki ste ga pravkar izdelali, je dober začetek, zdaj pa razmislite, kako ustvariti avtomatizacijo, ki bo finančni ekipi omogočila pošiljanje e-pošte dobavitelju, da jih obvesti o trenutnem statusu njihovega računa. Namig: tok mora teči, ko se status računa spremeni.

## Uporabite AI model za generiranje besedila v Power Automate

AI Model Create Text with GPT v AI Builder omogoča generiranje besedila na podlagi navodila in temelji na Microsoft Azure OpenAI storitvi. S to zmogljivostjo lahko v svoje aplikacije in tokove vključite GPT (Generative Pre-Trained Transformer) tehnologijo za izdelavo različnih avtomatiziranih tokov in poučnih aplikacij.

GPT modeli so bili obsežno usposobljeni na velikih količinah podatkov, kar jim omogoča ustvarjanje besedila, ki zelo spominja na človeški jezik, ko dobijo navodilo. Ko jih vključite v avtomatizacijo delovnega toka, lahko AI modeli, kot je GPT, poenostavijo in avtomatizirajo širok spekter opravil.

Na primer, lahko ustvarite tokove za samodejno generiranje besedila za različne namene, kot so osnutki e-poštnih sporočil, opisi izdelkov in več. Model lahko uporabite tudi za generiranje besedila v različnih aplikacijah, kot so chatbot-i in aplikacije za podporo strankam, ki omogočajo agentom učinkovito in uspešno odzivanje na povpraševanja strank.

![create a prompt](../../../translated_images/sl/create-prompt-gpt.69d429300c2e870a.webp)


Če se želite naučiti, kako uporabljati ta AI model v Power Automate, si oglejte modul [Dodajte inteligenco z AI Builder in GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Odlično delo! Nadaljujte z učenjem

Ko končate ta pouk, si oglejte našo [Zbirko za učenje generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo vašega znanja o generativni umetni inteligenci!

Želite po meri prilagoditi in izkoristiti še več iz Copilota? Raziskujte [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — skupnostno prispevano zbirko navodil, agentov, veščin in konfiguracij, ki vam pomagajo kar najbolje izkoristiti GitHub Copilot.

Pojdite na Lekcijo 11, kjer bomo pogledali, kako [integrirati generativno umetno inteligenco s klicanjem funkcij](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->