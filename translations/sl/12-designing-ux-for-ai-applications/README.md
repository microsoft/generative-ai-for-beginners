<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:36:01+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "sl"
}
-->
# Oblikovanje uporabniške izkušnje za aplikacije z umetno inteligenco

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

Uporabniška izkušnja je zelo pomemben vidik pri gradnji aplikacij. Uporabniki morajo vašo aplikacijo uporabljati učinkovito za izvajanje nalog. Biti učinkovit je ena stvar, vendar morate aplikacije oblikovati tudi tako, da jih lahko uporabljajo vsi, da so _dostopne_. Ta poglavje se bo osredotočilo na to področje, da boste na koncu oblikovali aplikacijo, ki jo ljudje lahko in želijo uporabljati.

## Uvod

Uporabniška izkušnja je način, kako uporabnik interagira z določenim izdelkom ali storitvijo, naj bo to sistem, orodje ali dizajn. Pri razvoju aplikacij z umetno inteligenco se razvijalci ne osredotočajo le na zagotavljanje učinkovite uporabniške izkušnje, temveč tudi etične. V tej lekciji bomo pokrili, kako zgraditi aplikacije z umetno inteligenco, ki zadovoljujejo potrebe uporabnikov.

Lekcija bo pokrila naslednja področja:

- Uvod v uporabniško izkušnjo in razumevanje potreb uporabnikov
- Oblikovanje aplikacij z umetno inteligenco za zaupanje in preglednost
- Oblikovanje aplikacij z umetno inteligenco za sodelovanje in povratne informacije

## Cilji učenja

Po tej lekciji boste sposobni:

- Razumeti, kako zgraditi aplikacije z umetno inteligenco, ki izpolnjujejo potrebe uporabnikov.
- Oblikovati aplikacije z umetno inteligenco, ki spodbujajo zaupanje in sodelovanje.

### Predpogoji

Vzemite si čas in preberite več o [uporabniški izkušnji in oblikovalskem razmišljanju.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Uvod v uporabniško izkušnjo in razumevanje potreb uporabnikov

V našem namišljenem startupu za izobraževanje imamo dva glavna uporabnika, učitelje in študente. Vsak od teh dveh uporabnikov ima edinstvene potrebe. Na uporabnika osredotočeno oblikovanje daje prednost uporabniku, s čimer zagotavlja, da so izdelki pomembni in koristni za tiste, za katere so namenjeni.

Aplikacija naj bo **uporabna, zanesljiva, dostopna in prijetna**, da zagotovi dobro uporabniško izkušnjo.

### Uporabnost

Biti uporaben pomeni, da ima aplikacija funkcionalnost, ki ustreza njenemu namenu, na primer avtomatizacija procesa ocenjevanja ali ustvarjanje učnih kartic za ponavljanje. Aplikacija, ki avtomatizira proces ocenjevanja, bi morala biti sposobna natančno in učinkovito dodeljevati ocene na podlagi vnaprej določenih kriterijev. Podobno bi morala aplikacija, ki ustvarja učne kartice, biti sposobna ustvariti relevantna in raznolika vprašanja na podlagi svojih podatkov.

### Zanesljivost

Biti zanesljiv pomeni, da aplikacija lahko dosledno in brez napak opravlja svojo nalogo. Vendar pa AI, tako kot ljudje, ni popolna in je lahko nagnjena k napakam. Aplikacije se lahko srečajo z napakami ali nepričakovanimi situacijami, ki zahtevajo človeško posredovanje ali popravek. Kako se spopadate z napakami? V zadnjem delu te lekcije bomo pokrili, kako so sistemi in aplikacije z umetno inteligenco zasnovani za sodelovanje in povratne informacije.

### Dostopnost

Biti dostopen pomeni razširiti uporabniško izkušnjo na uporabnike z različnimi sposobnostmi, vključno z invalidi, ter zagotoviti, da nihče ni izključen. Z upoštevanjem smernic in načel dostopnosti postanejo rešitve z umetno inteligenco bolj vključujoče, uporabne in koristne za vse uporabnike.

### Prijetnost

Biti prijeten pomeni, da je aplikacija užitna za uporabo. Privlačna uporabniška izkušnja lahko pozitivno vpliva na uporabnika, ga spodbuja k vrnitvi k aplikaciji in povečuje prihodke podjetja.

Ne vsak izziv je mogoče rešiti z umetno inteligenco. AI pride na pomoč pri izboljšanju uporabniške izkušnje, bodisi z avtomatizacijo ročnih nalog ali personalizacijo uporabniških izkušenj.

## Oblikovanje aplikacij z umetno inteligenco za zaupanje in preglednost

Gradnja zaupanja je ključna pri oblikovanju aplikacij z umetno inteligenco. Zaupanje zagotavlja, da je uporabnik prepričan, da bo aplikacija opravila delo, dosledno zagotavljala rezultate in da so rezultati tisto, kar uporabnik potrebuje. Tveganje na tem področju je nezaupanje in prekomerno zaupanje. Nezaupanje se pojavi, ko uporabnik nima ali ima malo zaupanja v sistem z umetno inteligenco, kar vodi do tega, da uporabnik zavrne vašo aplikacijo. Prekomerno zaupanje se pojavi, ko uporabnik preceni sposobnosti sistema z umetno inteligenco, kar vodi do tega, da uporabniki preveč zaupajo sistemu z umetno inteligenco. Na primer, avtomatiziran sistem ocenjevanja v primeru prekomernega zaupanja lahko privede do tega, da učitelj ne preveri nekaterih nalog, da bi zagotovil, da sistem ocenjevanja deluje dobro. To bi lahko privedlo do nepravičnih ali netočnih ocen za študente ali zamujenih priložnosti za povratne informacije in izboljšanje.

Dva načina za zagotovitev, da je zaupanje postavljeno v središče oblikovanja, sta razložljivost in nadzor.

### Razložljivost

Ko AI pomaga pri sprejemanju odločitev, kot je prenašanje znanja na prihodnje generacije, je ključno, da učitelji in starši razumejo, kako so sprejete odločitve z umetno inteligenco. To je razložljivost - razumevanje, kako aplikacije z umetno inteligenco sprejemajo odločitve. Oblikovanje za razložljivost vključuje dodajanje podrobnosti o primerih, kaj lahko aplikacija z umetno inteligenco naredi. Na primer, namesto "Začnite z AI učiteljem", lahko sistem uporabi: "Povzemite svoje zapiske za lažje ponavljanje z uporabo AI."

Drug primer je, kako AI uporablja uporabniške in osebne podatke. Na primer, uporabnik z osebnostjo študenta ima lahko omejitve na podlagi svoje osebnosti. AI morda ne bo mogla razkriti odgovorov na vprašanja, lahko pa uporabnika vodi, kako razmišljati o reševanju problema.

Zadnji ključni del razložljivosti je poenostavitev razlag. Študenti in učitelji morda niso strokovnjaki za umetno inteligenco, zato morajo biti razlage, kaj aplikacija lahko ali ne more storiti, poenostavljene in enostavne za razumevanje.

### Nadzor

Generativna umetna inteligenca ustvarja sodelovanje med umetno inteligenco in uporabnikom, kjer lahko uporabnik na primer spremeni pozive za različne rezultate. Poleg tega, ko je rezultat ustvarjen, bi morali uporabniki imeti možnost, da spremenijo rezultate, kar jim daje občutek nadzora. Na primer, ko uporabljate Bing, lahko prilagodite svoj poziv glede na format, ton in dolžino. Poleg tega lahko dodate spremembe svojemu izhodu in spremenite izhod.

Druga funkcija v Bingu, ki uporabniku omogoča nadzor nad aplikacijo, je možnost, da se prijavi in odjavi iz podatkov, ki jih uporablja umetna inteligenca. Za šolsko aplikacijo bi študent morda želel uporabiti svoje zapiske in učiteljeve vire kot gradivo za ponavljanje.

> Pri oblikovanju aplikacij z umetno inteligenco je namernost ključna za zagotavljanje, da uporabniki ne postavljajo nerealnih pričakovanj glede njenih sposobnosti. Eden od načinov za to je ustvarjanje trenja med pozivi in rezultati. Opominjanje uporabnika, da je to umetna inteligenca in ne sočlovek.

## Oblikovanje aplikacij z umetno inteligenco za sodelovanje in povratne informacije

Kot je bilo prej omenjeno, generativna umetna inteligenca ustvarja sodelovanje med uporabnikom in umetno inteligenco. Večina interakcij je z uporabnikom, ki vnese poziv, in umetno inteligenco, ki generira izhod. Kaj pa, če je izhod napačen? Kako aplikacija obravnava napake, če se pojavijo? Ali umetna inteligenca krivi uporabnika ali si vzame čas za razlago napake?

Aplikacije z umetno inteligenco bi morale biti zgrajene tako, da prejemajo in dajejo povratne informacije. To ne pomaga le izboljšati sistem umetne inteligence, ampak tudi gradi zaupanje pri uporabnikih. Povratna zanka bi morala biti vključena v oblikovanje, primer je lahko preprosto všeč ali ne všeč na izhodu.

Drug način za obravnavanje tega je jasna komunikacija sposobnosti in omejitev sistema. Ko uporabnik naredi napako pri zahtevi nečesa, kar presega zmožnosti umetne inteligence, bi moral obstajati način za obravnavanje tega.

Sistemske napake so pogoste pri aplikacijah, kjer uporabnik morda potrebuje pomoč z informacijami zunaj obsega umetne inteligence ali aplikacija morda omejuje, koliko vprašanj/predmetov lahko uporabnik generira povzetke. Na primer, aplikacija z umetno inteligenco, usposobljena z omejenimi predmeti, na primer Zgodovina in Matematika, morda ne bo mogla obravnavati vprašanj o Geografiji. Da bi to omilili, lahko sistem umetne inteligence poda odgovor, kot je: "Oprostite, naš izdelek je bil usposobljen z podatki o naslednjih predmetih....., ne morem odgovoriti na vprašanje, ki ste ga postavili."

Aplikacije z umetno inteligenco niso popolne, zato so nagnjene k napakam. Pri oblikovanju svojih aplikacij bi morali zagotoviti, da ustvarite prostor za povratne informacije uporabnikov in obravnavanje napak na način, ki je preprost in lahko razumljiv.

## Naloga

Vzemite katero koli aplikacijo z umetno inteligenco, ki ste jo do sedaj zgradili, in razmislite o implementaciji spodnjih korakov v vaši aplikaciji:

- **Prijetnost:** Razmislite, kako lahko naredite svojo aplikacijo bolj prijetno. Ali povsod dodajate razlage? Ali spodbujate uporabnika k raziskovanju? Kako oblikujete svoja sporočila o napakah?

- **Uporabnost:** Gradnja spletne aplikacije. Poskrbite, da bo vaša aplikacija navigabilna tako z miško kot s tipkovnico.

- **Zaupanje in preglednost:** Ne zaupajte umetni inteligenci popolnoma in njenemu izhodu, razmislite, kako bi vključili človeka v proces za preverjanje izhoda. Prav tako razmislite in implementirajte druge načine za doseganje zaupanja in preglednosti.

- **Nadzor:** Dajte uporabniku nadzor nad podatki, ki jih zagotovi aplikaciji. Implementirajte način, kako se lahko uporabnik prijavi in odjavi iz zbiranja podatkov v aplikaciji z umetno inteligenco.

## Nadaljujte z učenjem!

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

Pojdite na lekcijo 13, kjer bomo pogledali, kako [zavarovati aplikacije z umetno inteligenco](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno prevajanje s strani človeka. Ne odgovarjamo za kakršne koli nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.