<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T19:34:43+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "sl"
}
-->
# Gradnja AI aplikacij z malo kode

## Uvod

Zdaj, ko smo se naučili graditi aplikacije za generiranje slik, se pogovorimo o malo kodi. Generativna umetna inteligenca se lahko uporablja na različnih področjih, vključno z malo kode, ampak kaj je malo koda in kako lahko vanjo vključimo AI?

Izdelava aplikacij in rešitev je postala lažja za tradicionalne razvijalce in tiste, ki niso razvijalci, z uporabo platform za razvoj z malo kode. Platforme za razvoj z malo kode vam omogočajo gradnjo aplikacij in rešitev z malo ali brez kode. To se doseže z zagotavljanjem vizualnega razvojnega okolja, ki vam omogoča, da povlečete in spustite komponente za gradnjo aplikacij in rešitev. To vam omogoča hitrejšo gradnjo aplikacij in rešitev z manj sredstvi. V tej lekciji se bomo poglobili v to, kako uporabljati malo kodo in kako izboljšati razvoj z malo kode z AI z uporabo Power Platforme.

Power Platform organizacijam omogoča, da opolnomočijo svoje ekipe, da same gradijo rešitve v intuitivnem okolju z malo ali brez kode. To okolje poenostavi proces gradnje rešitev. S Power Platform se lahko rešitve gradijo v dneh ali tednih namesto mesecev ali let. Power Platform sestavlja pet ključnih izdelkov: Power Apps, Power Automate, Power BI, Power Pages in Copilot Studio.

Ta lekcija pokriva:

- Uvod v generativno AI v Power Platformi
- Uvod v Copilot in kako ga uporabljati
- Uporaba generativne AI za gradnjo aplikacij in tokov v Power Platformi
- Razumevanje AI modelov v Power Platformi z AI Builderjem

## Cilji učenja

Do konca te lekcije boste lahko:

- Razumeli, kako deluje Copilot v Power Platformi.

- Zgradili aplikacijo za sledenje nalog študentov za naš izobraževalni startup.

- Zgradili tok za obdelavo računov, ki uporablja AI za izvlečenje informacij iz računov.

- Uporabili najboljše prakse pri uporabi modela GPT AI za ustvarjanje besedila.

Orodja in tehnologije, ki jih boste uporabili v tej lekciji, so:

- **Power Apps**, za aplikacijo za sledenje nalog študentov, ki zagotavlja razvojno okolje z malo kode za gradnjo aplikacij za sledenje, upravljanje in interakcijo s podatki.

- **Dataverse**, za shranjevanje podatkov za aplikacijo za sledenje nalog študentov, kjer bo Dataverse zagotovil platformo z malo kode za shranjevanje podatkov aplikacije.

- **Power Automate**, za tok obdelave računov, kjer boste imeli razvojno okolje z malo kode za gradnjo delovnih tokov za avtomatizacijo procesa obdelave računov.

- **AI Builder**, za AI model obdelave računov, kjer boste uporabili vnaprej zgrajene AI modele za obdelavo računov za naš startup.

## Generativna AI v Power Platformi

Izboljšanje razvoja z malo kode in aplikacij z generativno AI je ključno področje za Power Platform. Cilj je omogočiti vsakomur gradnjo aplikacij, spletnih mest, nadzornih plošč in avtomatizacijo procesov z AI, _brez potrebe po strokovnem znanju na področju podatkovne znanosti_. Ta cilj se doseže z integracijo generativne AI v izkušnjo razvoja z malo kode v Power Platformi v obliki Copilot in AI Builder.

### Kako to deluje?

Copilot je AI pomočnik, ki vam omogoča gradnjo rešitev v Power Platformi z opisovanjem vaših zahtev v nizu pogovornih korakov z uporabo naravnega jezika. Na primer, lahko svojemu AI pomočniku naročite, katere polja bo vaša aplikacija uporabljala, in ta bo ustvaril tako aplikacijo kot tudi osnovni podatkovni model ali pa lahko določite, kako nastaviti tok v Power Automate.

Funkcionalnosti, ki jih poganja Copilot, lahko uporabite kot funkcijo v zaslonih vaše aplikacije, da omogočite uporabnikom odkrivanje vpogledov skozi pogovorne interakcije.

AI Builder je zmožnost AI z malo kode, ki je na voljo v Power Platformi, in vam omogoča uporabo AI modelov za pomoč pri avtomatizaciji procesov in napovedovanju rezultatov. Z AI Builder lahko prinesete AI v vaše aplikacije in tokove, ki se povezujejo z vašimi podatki v Dataverse ali v različnih virih podatkov v oblaku, kot so SharePoint, OneDrive ali Azure.

Copilot je na voljo v vseh izdelkih Power Platform: Power Apps, Power Automate, Power BI, Power Pages in Power Virtual Agents. AI Builder je na voljo v Power Apps in Power Automate. V tej lekciji se bomo osredotočili na to, kako uporabiti Copilot in AI Builder v Power Apps in Power Automate za gradnjo rešitve za naš izobraževalni startup.

### Copilot v Power Apps

Kot del Power Platforme, Power Apps zagotavlja razvojno okolje z malo kode za gradnjo aplikacij za sledenje, upravljanje in interakcijo s podatki. Gre za zbirko storitev za razvoj aplikacij z razširljivo podatkovno platformo in zmožnostjo povezovanja s storitvami v oblaku in podatki v lokalnem okolju. Power Apps vam omogoča gradnjo aplikacij, ki delujejo v brskalnikih, tablicah in telefonih ter jih lahko delite s sodelavci. Power Apps uporabnike uvede v razvoj aplikacij z enostavnim vmesnikom, tako da lahko vsak poslovni uporabnik ali profesionalni razvijalec gradi prilagojene aplikacije. Izkušnja razvoja aplikacij je prav tako izboljšana z generativno AI preko Copilot.

Funkcija AI pomočnika Copilot v Power Apps vam omogoča opisati, kakšno aplikacijo potrebujete in katere informacije želite, da vaša aplikacija sledi, zbira ali prikazuje. Copilot nato generira odzivno Canvas aplikacijo na podlagi vašega opisa. Aplikacijo lahko nato prilagodite svojim potrebam. AI Copilot prav tako generira in predlaga tabelo Dataverse s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite slediti, in nekaj vzorčnih podatkov. V tej lekciji bomo kasneje pogledali, kaj je Dataverse in kako ga lahko uporabite v Power Apps. Nato lahko prilagodite tabelo svojim potrebam z uporabo funkcije AI Copilot pomočnika skozi pogovorne korake. Ta funkcija je na voljo z domačega zaslona Power Apps.

### Copilot v Power Automate

Kot del Power Platforme, Power Automate uporabnikom omogoča ustvarjanje avtomatiziranih delovnih tokov med aplikacijami in storitvami. Pomaga avtomatizirati ponavljajoče se poslovne procese, kot so komunikacija, zbiranje podatkov in odobritve odločitev. Njegov enostaven vmesnik omogoča uporabnikom z različnimi tehničnimi kompetencami (od začetnikov do izkušenih razvijalcev) avtomatizacijo delovnih nalog. Izkušnja razvoja delovnih tokov je prav tako izboljšana z generativno AI preko Copilot.

Funkcija AI pomočnika Copilot v Power Automate vam omogoča opisati, kakšen tok potrebujete in katere akcije želite, da vaš tok izvaja. Copilot nato generira tok na podlagi vašega opisa. Tok lahko nato prilagodite svojim potrebam. AI Copilot prav tako generira in predlaga akcije, ki jih potrebujete za izvedbo naloge, ki jo želite avtomatizirati. Kasneje v tej lekciji bomo pogledali, kaj so tokovi in kako jih lahko uporabite v Power Automate. Nato lahko prilagodite akcije svojim potrebam z uporabo funkcije AI Copilot pomočnika skozi pogovorne korake. Ta funkcija je na voljo z domačega zaslona Power Automate.

## Naloga: Upravljanje študentskih nalog in računov za naš startup, z uporabo Copilot

Naš startup ponuja spletne tečaje za študente. Startup je hitro rasel in zdaj se trudi slediti povpraševanju po svojih tečajih. Startup vas je zaposlil kot razvijalca Power Platform, da jim pomagate zgraditi rešitev z malo kode, ki jim bo pomagala upravljati študentske naloge in račune. Njihova rešitev bi morala omogočiti sledenje in upravljanje študentskih nalog preko aplikacije ter avtomatizirati proces obdelave računov preko delovnega toka. Prosili so vas, da uporabite generativno AI za razvoj rešitve.

Ko začnete uporabljati Copilot, lahko uporabite [Knjižnico pozivov Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) za začetek z pozivi. Ta knjižnica vsebuje seznam pozivov, ki jih lahko uporabite za gradnjo aplikacij in tokov z Copilot. Pozive v knjižnici lahko uporabite tudi za ideje, kako opisati vaše zahteve Copilot.

### Zgradite aplikacijo za sledenje nalog študentov za naš startup

Izobraževalci v našem startupu so se trudili slediti študentskim nalogam. Uporabljali so preglednico za sledenje nalogam, vendar je to postalo težko upravljati, ko se je število študentov povečalo. Prosili so vas, da zgradite aplikacijo, ki jim bo pomagala slediti in upravljati študentske naloge. Aplikacija bi jim morala omogočiti dodajanje novih nalog, ogled nalog, posodabljanje nalog in brisanje nalog. Aplikacija bi morala tudi omogočiti izobraževalcem in študentom ogled nalog, ki so bile ocenjene in tistih, ki niso bile ocenjene.

Aplikacijo boste zgradili z uporabo Copilot v Power Apps po naslednjih korakih:

1. Pomaknite se na domači zaslon [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Uporabite besedilno polje na domačem zaslonu, da opišete aplikacijo, ki jo želite zgraditi. Na primer, **_Želim zgraditi aplikacijo za sledenje in upravljanje študentskih nalog_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilot.

1. AI Copilot bo predlagal tabelo Dataverse s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite slediti, in nekaj vzorčnih podatkov. Nato lahko prilagodite tabelo svojim potrebam z uporabo funkcije AI Copilot pomočnika skozi pogovorne korake.

1. Izobraževalci želijo poslati e-pošto študentom, ki so oddali svoje naloge, da jih obvestijo o napredku njihovih nalog. Copilot lahko uporabite za dodajanje novega polja v tabelo za shranjevanje e-pošte študentov. Na primer, lahko uporabite naslednji poziv za dodajanje novega polja v tabelo: **_Želim dodati stolpec za shranjevanje e-pošte študentov_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilot.

1. AI Copilot bo generiral novo polje, ki ga lahko nato prilagodite svojim potrebam.

1. Ko končate s tabelo, kliknite na gumb **Ustvari aplikacijo**, da ustvarite aplikacijo.

1. AI Copilot bo generiral odzivno Canvas aplikacijo na podlagi vašega opisa. Aplikacijo lahko nato prilagodite svojim potrebam.

1. Da bi izobraževalci poslali e-pošto študentom, lahko uporabite Copilot za dodajanje novega zaslona v aplikacijo. Na primer, lahko uporabite naslednji poziv za dodajanje novega zaslona v aplikacijo: **_Želim dodati zaslon za pošiljanje e-pošte študentom_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilot.

1. AI Copilot bo generiral nov zaslon, ki ga lahko nato prilagodite svojim potrebam.

1. Ko končate z aplikacijo, kliknite na gumb **Shrani**, da shranite aplikacijo.

1. Da delite aplikacijo z izobraževalci, kliknite na gumb **Deli** in nato ponovno kliknite na gumb **Deli**. Nato lahko delite aplikacijo z izobraževalci z vnosom njihovih e-poštnih naslovov.

### Zgradite tabelo informacij o računih za naš startup

Finančna ekipa našega startupa se je trudila slediti računom. Uporabljali so preglednico za sledenje računom, vendar je to postalo težko upravljati, ko se je število računov povečalo. Prosili so vas, da zgradite tabelo, ki jim bo pomagala shranjevati, slediti in upravljati informacije o prejetih računih. Tabela bi morala biti uporabljena za gradnjo avtomatizacije, ki bo izvlekla vse informacije o računih in jih shranila v tabelo. Tabela bi morala tudi omogočiti finančni ekipi ogled računov, ki so bili plačani, in tistih, ki niso bili plačani.

Power Platform ima osnovno podatkovno platformo, imenovano Dataverse, ki vam omogoča shranjevanje podatkov za vaše aplikacije in rešitve. Dataverse zagotavlja platformo z malo kode za shranjevanje podatkov aplikacije. Gre za popolnoma upravljano storitev, ki varno shranjuje podatke v Microsoftovem oblaku in je dodeljena znotraj vašega okolja Power Platform. Ima vgrajene zmožnosti upravljanja podatkov, kot so klasifikacija podatkov, izvor podatkov, natančen nadzor dostopa in več. Več o Dataverse lahko preberete [tukaj](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Zakaj bi uporabili Dataverse za naš startup? Standardne in prilagojene tabele znotraj Dataverse zagotavljajo varno in na oblaku osnovano možnost shranjevanja za vaše podatke. Tabele vam omogočajo shranjevanje različnih vrst podatkov, podobno kot bi uporabili več delovnih listov v enem Excelovem delovnem zvezku. Tabele lahko uporabite za shranjevanje podatkov, ki so specifični za vaše organizacijske ali poslovne potrebe. Nekatere koristi, ki jih bo naš startup imel od uporabe Dataverse, vključujejo, vendar niso omejene na:

- **Enostavno upravljanje**: Tako metapodatki kot podatki so shranjeni v oblaku, zato vam ni treba skrbeti za podrobnosti, kako so shranjeni ali upravljani. Lahko se osredotočite na gradnjo vaših aplikacij in rešitev.

- **Varno**: Dataverse zagotavlja varno in na oblaku osnovano možnost shranjevanja za vaše podatke. Lahko nadzorujete, kdo ima dostop do podatkov v vaših tabelah in kako jih lahko dostopa z uporabo varnosti na podlagi vlog.

- **Bogati metapodatki**: Vrste podatkov in odnosi se uporabljajo neposredno znotraj Power Apps.

- **Logika in validacija**: Uporabite lahko poslovna pravila, izračunana polja in pravila validacije za uveljavljanje poslovne logike in ohranjanje natančnosti podatkov.

Zdaj, ko veste, kaj je Dataverse in zakaj bi ga morali uporabiti, si poglejmo, kako lahko uporabite Copilot za ustvarjanje tabele v Dataverse, da izpolnite zahteve naše finančne ekipe.

> **Opomba**: To tabelo boste uporabili v naslednjem razdelku za gradnjo avtomatizacije, ki bo izvlekla vse informacije o računih in jih shranila v tabelo.  
Za ustvarjanje tabele v Dataverse z uporabo Copilot sledite spodnjim korakom: 1. Pomaknite se na domači zaslon [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst). 2. Na levi navigacijski vrstici izberite **Tabele** in nato kliknite na **Opisi nove tabele**. 1. Na zaslonu **Opisi nove tabele** uporabite besedilno polje za opis tabele, ki jo želite ustvariti. Na primer, **_Želim ustvariti tabelo za shranjevanje informacij o računih_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilot. 1. AI Copilot bo predlagal tabelo Dataverse s polji, ki jih potrebujete za shranjevanje podatkov, ki jih želite slediti, in nekaj vzorčnih podatkov. Nato lahko prilagodite tabelo svojim potrebam z uporabo funkcije AI Copilot pomočnika skozi pogovorne korake. 1. Finančna ekipa želi poslati e-pošto dobavitelju, da jih obvesti o trenutnem stanju njihovega računa. Copilot lahko uporabite za dodajanje novega polja v tabelo za shranjevanje e-pošte dobavitelja. Na primer, lahko uporabite naslednji poziv za dodajanje novega polja v tabelo: **_Želim dodati stolpec za shranjevanje e-pošte dobavitelja_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilot. 1. AI Copilot bo generiral novo polje, ki ga lahko nato prilagodite svojim potrebam. 1. Ko konč
- **Analiza sentimenta**: Ta model zazna pozitivna, negativna, nevtralna ali mešana čustva v besedilu. 
- **Branje poslovnih vizitk**: Ta model izlušči informacije iz poslovnih vizitk. 
- **Prepoznavanje besedila**: Ta model izlušči besedilo iz slik. 
- **Zaznavanje objektov**: Ta model zazna in izlušči objekte iz slik. 
- **Obdelava dokumentov**: Ta model izlušči informacije iz obrazcev. 
- **Obdelava računov**: Ta model izlušči informacije iz računov. 

S prilagojenimi modeli AI lahko v AI Builder vključite svoj model, da deluje kot kateri koli prilagojen model AI Builder, kar vam omogoča, da model usposobite z lastnimi podatki. Te modele lahko uporabite za avtomatizacijo procesov in napovedovanje rezultatov tako v Power Apps kot v Power Automate. Pri uporabi lastnega modela veljajo omejitve. Več o teh omejitvah si preberite [tukaj](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

## Naloga #2 - Zgradite tok obdelave računov za naš startup

Finančna ekipa ima težave pri obdelavi računov. Za sledenje računom so uporabljali preglednico, vendar je to postalo težko obvladljivo, saj se je število računov povečalo. Prosili so vas, da zgradite delovni tok, ki jim bo pomagal obdelovati račune z uporabo AI. Delovni tok naj omogoči, da izluščijo informacije iz računov in shranijo informacije v tabelo Dataverse. Prav tako naj jim omogoči, da pošljejo e-pošto finančni ekipi z izluščenimi informacijami. 

Zdaj, ko veste, kaj je AI Builder in zakaj bi ga morali uporabljati, poglejmo, kako lahko uporabite model AI za obdelavo računov v AI Builderju, ki smo ga obravnavali prej, da zgradite delovni tok, ki bo finančni ekipi pomagal obdelovati račune. Da zgradite delovni tok, ki bo finančni ekipi pomagal obdelovati račune z uporabo modela AI za obdelavo računov v AI Builderju, sledite spodnjim korakom:

1. Pomaknite se na domačo stran [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Uporabite besedilno polje na domači strani, da opišete delovni tok, ki ga želite zgraditi. Na primer, **_Obdelaj račun, ko prispe v mojo pošto_**. Kliknite na gumb **Pošlji**, da pošljete poziv AI Copilotu.
3. AI Copilot vam bo predlagal dejanja, ki jih morate izvesti, da avtomatizirate nalogo, ki jo želite. Kliknite na gumb **Naprej**, da nadaljujete na naslednje korake.
4. V naslednjem koraku vas bo Power Automate pozval, da nastavite povezave, potrebne za tok. Ko končate, kliknite na gumb **Ustvari tok**, da ustvarite tok.
5. AI Copilot bo ustvaril tok in ga lahko nato prilagodite svojim potrebam.
6. Posodobite sprožilec toka in nastavite **Mapo** na mapo, kjer bodo shranjeni računi. Na primer, lahko nastavite mapo na **Prejeto**. Kliknite na **Prikaži napredne možnosti** in nastavite **Samo z priponkami** na **Da**. To bo zagotovilo, da se tok zažene le, ko je v mapi prejet e-poštni naslov s priponko.
7. Odstranite naslednja dejanja iz toka: **HTML v besedilo**, **Sestavi**, **Sestavi 2**, **Sestavi 3** in **Sestavi 4**, ker jih ne boste uporabljali.
8. Odstranite dejanje **Pogoj** iz toka, ker ga ne boste uporabljali. Videti naj bo kot na naslednjem posnetku zaslona:
9. Kliknite na gumb **Dodaj dejanje** in poiščite **Dataverse**. Izberite dejanje **Dodaj novo vrstico**.
10. Na dejanje **Izlušči informacije iz računov** posodobite **Datoteko računa**, da kaže na **Vsebino priponke** iz e-pošte. To bo zagotovilo, da tok izlušči informacije iz priponke računa.
11. Izberite **Tabelo**, ki ste jo ustvarili prej. Na primer, lahko izberete tabelo **Informacije o računu**. Izberite dinamično vsebino iz prejšnjega dejanja, da izpolnite naslednja polja:
    - ID
    - Znesek
    - Datum
    - Ime
    - Status
    - Nastavite **Status** na **V obdelavi**.
    - E-pošta dobavitelja
    - Uporabite dinamično vsebino **Od** iz sprožilca **Ko prispe nov e-poštni naslov**.
12. Ko končate s tokom, kliknite na gumb **Shrani**, da shranite tok. Nato lahko testirate tok tako, da pošljete e-poštni naslov z računom v mapo, ki ste jo določili v sprožilcu.

> **Vaša domača naloga**: Tok, ki ste ga pravkar zgradili, je dober začetek, zdaj morate razmisliti, kako lahko zgradite avtomatizacijo, ki bo naši finančni ekipi omogočila, da pošlje e-pošto dobavitelju, da ga obvesti o trenutnem statusu njegovega računa. Vaš namig: tok se mora zagnati, ko se status računa spremeni.

## Uporaba modela AI za generiranje besedila v Power Automate

Model AI za ustvarjanje besedila z GPT v AI Builderju vam omogoča generiranje besedila na podlagi poziva in ga poganja Microsoft Azure OpenAI Service. S to zmožnostjo lahko vključite tehnologijo GPT (Generative Pre-Trained Transformer) v svoje aplikacije in tokove, da zgradite različne avtomatizirane tokove in pronicljive aplikacije.

Modeli GPT so deležni obsežnega usposabljanja na velikih količinah podatkov, kar jim omogoča, da proizvajajo besedilo, ki tesno spominja na človeški jezik, ko so jim podani pozivi. Ko so integrirani z avtomatizacijo delovnih tokov, se lahko modeli AI, kot je GPT, izkoristijo za poenostavitev in avtomatizacijo širokega spektra nalog.

Na primer, lahko zgradite tokove za samodejno generiranje besedila za različne primere uporabe, kot so: osnutki e-poštnih sporočil, opisi izdelkov in še več. Model lahko uporabite tudi za generiranje besedila za različne aplikacije, kot so klepetalni roboti in aplikacije za podporo strankam, ki omogočajo agentom za podporo strankam, da učinkovito in učinkovito odgovarjajo na poizvedbe strank.

Če želite izvedeti, kako uporabljati ta model AI v Power Automate, preglejte modul [Dodajte inteligenco z AI Builderjem in GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo zbirko [Učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni AI!

Pomaknite se na lekcijo 11, kjer bomo pogledali, kako [integrirati generativno AI z klicanjem funkcij](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Medtem ko si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.