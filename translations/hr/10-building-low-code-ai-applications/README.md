# Izrada AI aplikacija s malim kodom

[![Izrada AI aplikacija s malim kodom](../../../translated_images/hr/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Kliknite na gornju sliku za prikaz video lekcije)_

## Uvod

Sada kad smo naučili kako izgraditi aplikacije za generiranje slika, razgovarajmo o low code (malom kodu). Generativni AI može se koristiti u raznim područjima, uključujući low code, ali što je low code i kako mu možemo dodati AI?

Izgradnja aplikacija i rješenja postala je lakša za tradicionalne programere i neprogramere korištenjem platformi za razvoj s malim kodom. Platforme za razvoj s malim kodom omogućuju izradu aplikacija i rješenja s malo ili bez koda. To se postiže pružanjem vizualnog razvojno okruženja koje vam omogućuje povlačenje i ispuštanje komponenti za izradu aplikacija i rješenja. To vam omogućuje da brže i s manje resursa gradite aplikacije i rješenja. U ovoj lekciji detaljno ćemo istražiti kako koristiti low code i kako unaprijediti razvoj s malim kodom pomoću AI koristeći Power Platform.

Power Platform pruža organizacijama priliku da osnaže svoje timove da sami grade svoja rješenja putem intuitivnog okruženja s malim ili bez koda. Ovo okruženje pojednostavljuje proces izrade rješenja. Uz Power Platform, rješenja se mogu izraditi u danima ili tjednima umjesto mjesecima ili godinama. Power Platform se sastoji od pet ključnih proizvoda: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio.

Ova lekcija obuhvaća:

- Uvod u generativni AI u Power Platformi
- Uvod u Copilot i kako ga koristiti
- Korištenje generativnog AI za izgradnju aplikacija i tijekova u Power Platformi
- Razumijevanje AI modela u Power Platformi s AI Builderom
- Izrada inteligentnih agenata s Microsoft Copilot Studiom

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Razumjeti kako Copilot funkcionira u Power Platformi.

- Izraditi aplikaciju za praćenje studentskih zadataka za naš obrazovni startup.

- Izraditi tijek za obradu računa koji koristi AI za izdvajanje informacija iz računa.

- Primijeniti najbolje prakse pri korištenju Create Text s GPT AI modelom.

- Razumjeti što je Microsoft Copilot Studio i kako izraditi inteligentne agente s njim.

Alati i tehnologije koje ćete koristiti u ovoj lekciji su:

- **Power Apps**, za aplikaciju za praćenje studentskih zadataka, koja pruža razvojno okruženje s malim kodom za izgradnju aplikacija za praćenje, upravljanje i interakciju s podacima.

- **Dataverse**, za pohranu podataka za aplikaciju za praćenje studentskih zadataka, gdje Dataverse pruža platformu s malim kodom za pohranu podataka aplikacije.

- **Power Automate**, za tijek obrade računa gdje ćete imati razvojno okruženje s malim kodom za izradu tijekova rada za automatizaciju procesa obrade računa.

- **AI Builder**, za AI model obrade računa gdje ćete koristiti prethodno izrađene AI modele za obradu računa za naš startup.

## Generativni AI u Power Platformi

Unapređenje razvoja s malim kodom i aplikacija generativnim AI-jem ključni je fokus Power Platforme. Cilj je omogućiti svima kreiranje AI-pokretanih aplikacija, stranica, nadzornih ploča i automatizaciju procesa pomoću AI, _bez potrebe za stručnjacima za podatkovnu znanost_. Taj se cilj ostvaruje integracijom generativnog AI-ja u razvojno iskustvo s malim kodom u Power Platformi kroz Copilot i AI Builder.

### Kako to funkcionira?

Copilot je AI asistent koji vam omogućuje izgradnju rješenja u Power Platformi tako da opisujete svoje zahtjeve kroz niz konverzacijskih koraka koristeći prirodni jezik. Možete, na primjer, zatražiti da vaš AI asistent navede koje će polja vaša aplikacija koristiti, a on će kreirati i aplikaciju i osnovni podatkovni model ili možete specificirati kako postaviti tijek rada u Power Automate.

Možete koristiti funkcionalnosti vođene copilotom kao značajku u vašim zaslonima aplikacije kako biste korisnicima omogućili otkrivanje uvida putem konverzacijskih interakcija.

AI Builder je AI mogućnost s malim kodom dostupna u Power Platformi koja vam omogućuje korištenje AI modela za automatizaciju procesa i predviđanje ishoda. S AI Builderom možete donijeti AI u svoje aplikacije i tijekove koji se povezuju s vašim podacima u Dataverseu ili u raznim cloud izvorima podataka, poput SharePointa, OneDrivea ili Azurea.

Copilot je dostupan u svim proizvodima Power Platforme: Power Apps, Power Automate, Power BI, Power Pages i Copilot Studio (nekada Power Virtual Agents). AI Builder je dostupan u Power Apps i Power Automate. U ovoj lekciji fokusirat ćemo se na korištenje Copilota i AI Buildera u Power Apps i Power Automate za izgradnju rješenja za naš obrazovni startup.

### Copilot u Power Apps

Kao dio Power Platforme, Power Apps pruža razvojno okruženje s malim kodom za izgradnju aplikacija za praćenje, upravljanje i interakciju s podacima. To je skup usluga za razvoj aplikacija s skalabilnom platformom podataka i mogućnošću povezivanja na cloud usluge i lokalne podatke. Power Apps omogućava izradu aplikacija koje rade na preglednicima, tabletima i telefonima te se mogu dijeliti s kolegama. Power Apps olakšava korisnicima ulazak u razvoj aplikacija jednostavnim sučeljem, tako da svaki poslovni korisnik ili profesionalni programer može izraditi prilagođene aplikacije. Iskustvo razvoja aplikacije dodatno je unaprijeđeno generativnim AI-jem kroz Copilot.

Značajka AI asistenta copilota u Power Apps omogućuje vam opisivanje vrste aplikacije koja vam treba i koje informacije želite da vaša aplikacija prati, prikuplja ili prikazuje. Copilot zatim generira responzivnu Canvas aplikaciju na temelju vašeg opisa. Aplikaciju zatim možete prilagoditi svojim potrebama. AI Copilot također generira i predlaže Dataverse tablicu s poljima koja trebate za pohranu podataka koje želite pratiti te neke uzorke podataka. U ovoj ćemo lekciji kasnije pogledati što je Dataverse i kako ga možete koristiti u Power Apps. Zatim možete prilagoditi tablicu svojim potrebama koristeći AI Copilot pomoćnika kroz konverzacijske korake. Ova značajka dostupna je odmah s početnog zaslona Power Apps.

### Copilot u Power Automate

Kao dio Power Platforme, Power Automate omogućuje korisnicima stvaranje automatiziranih tijekova rada između aplikacija i usluga. Pomaže automatizirati ponovljive poslovne procese kao što su komunikacija, prikupljanje podataka i odobrenja odluka. Njegovo jednostavno sučelje omogućuje korisnicima svih tehničkih razina (od početnika do iskusnih programera) automatizaciju radnih zadataka. Iskustvo razvoja tijekova rada dodatno je poboljšano generativnim AI-jem kroz Copilot.

Značajka AI asistenta copilota u Power Automate omogućuje vam opisivanje vrste tijeka rada koja vam treba i koje radnje želite da vaš tijek obavi. Copilot zatim generira tijek rada na temelju vašeg opisa. Možete prilagoditi tijek svom potrebama. AI Copilot također generira i predlaže radnje potrebne za zadatak koji želite automatizirati. U ovoj lekciji kasnije ćemo pogledati što su tijekovi rada i kako ih koristiti u Power Automate. Zatim možete prilagoditi radnje koristeći AI Copilot pomoćnika kroz konverzacijske korake. Ova značajka dostupna je odmah s početnog zaslona Power Automate.

## Izgradnja inteligentnih agenata s Microsoft Copilot Studiom

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (nekada Power Virtual Agents) je low-code član Power Platforme za izradu **AI agenata** — razgovornih copilota koji mogu odgovarati na pitanja, poduzimati radnje i automatizirati zadatke u ime vaših korisnika. Kao i ostatak Power Platforme, ove agente gradite u vizualnom iskustvu usmjerenom na prirodni jezik: opisujete što želite da agent radi, a Copilot Studio pomaže u strukturiranju uputa, znanja i radnji.

Za naš obrazovni startup mogli biste izraditi agenta koji odgovara na studentska pitanja o tečajevima, provjerava rokove zadataka, pa čak šalje e-poštu instruktoru — sve bez pisanja koda.

Evo nekih od najnovijih mogućnosti koje čine Copilot Studio moćnim:

- **Generativni odgovori iz vašeg znanja**. Umjesto ručnog sastavljanja svake konverzacije, možete povezati **izvore znanja** — javne web stranice, SharePoint, OneDrive, Dataverse, učitane datoteke ili korporativne podatke putem konektora — i agent generira utemeljene odgovore iz njih.

- **Generativna orkestracija**. Umjesto oslanjanja na rigidne okidačke fraze, agent koristi AI da razumije zahtjev i dinamički odluči koje kombinacije znanja, tema i radnji upotrijebiti za ispunjenje, uključujući povezivanje nekoliko koraka.

- **Radnje i konektori**. Agenti mogu *činjenje*, ne samo chat. Možete agentu dati radnje potpomognute s više od 1.500 unaprijed izrađenih konektora Power Platforme, tijekova rada Power Automate, prilagođenih REST API-ja, promptova ili **Model Context Protocol (MCP)** servera.

- **Autonomni agenti**. Agenti nisu ograničeni na odgovaranje u chat prozoru. Možete izraditi **autonomne agente** koji se aktiviraju događajima — poput nove e-pošte, novog zapisa u Dataverseu ili učitavanja datoteke — te zatim djeluju u pozadini za dovršetak zadatka.

- **Orkestracija više agenata**. Agenti mogu pozvati druge agente. Copilot Studio agent može predati upravljanje ili se proširiti drugim agentima, uključujući agente objavljene u Microsoft 365 Copilotu i agente izrađene u Microsoft Foundryju.

- **Izbor modela**. Osim ugrađenih modela, možete donijeti modele iz Microsoft Foundry kataloga modela kako biste prilagodili način na koji vaš agent rezonira i odgovara.

- **Objavljivanje bilo gdje**. Kad je agent izrađen, može se objaviti na više kanala — Microsoft Teams, Microsoft 365 Copilot, web stranici ili prilagođenoj aplikaciji i više — s upravljanjem sigurnošću, autentifikacijom i analizom putem administrativnog iskustva Power Platforme.

Svoj prvi agent možete početi graditi na [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) i saznati više u [Microsoft Copilot Studio dokumentaciji](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Zadatak: Upravljajte studentskim zadacima i računima za naš startup koristeći Copilot

Naš startup pruža online tečajeve studentima. Startup je brzo rastao i sada se bori s održavanjem tempa potražnje za svojim tečajevima. Startup je zaposlio vas kao Power Platform programera da im pomognete izraditi rješenje s malim kodom za upravljanje studentskim zadacima i računima. Njihovo rješenje trebalo bi im pomoći pratiti i upravljati studentskim zadacima preko aplikacije te automatizirati proces obrade računa putem tijeka rada. Zatraženo je da koristite generativni AI za razvoj rješenja.

Kada započinjete s korištenjem Copilota, možete koristiti [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) za početak s promptovima. Ova biblioteka sadrži popis promptova koje možete koristiti za izgradnju aplikacija i tijekova s Copilotom. Također možete koristiti promptove u biblioteci za ideju kako opisati vaše zahtjeve Copilotu.

### Izradite aplikaciju za praćenje studentskih zadataka za naš startup

Obrazovni djelatnici u našem startupu teško prate studentske zadatke. Koristili su proračunsku tablicu za praćenje zadataka, ali to je postalo teško upravljati jer je broj studenata porastao. Zamolili su vas da izradite aplikaciju koja će im pomoći pratiti i upravljati studentskim zadacima. Aplikacija bi im trebala omogućiti dodavanje novih zadataka, pregled zadataka, ažuriranje zadataka i brisanje zadataka. Također bi omogućila nastavnicima i studentima da vide zadatke koji su ocijenjeni i one koji nisu ocijenjeni.

Aplikaciju ćete izraditi koristeći Copilot u Power Apps slijedeći korake u nastavku:

1. Idite na [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) početni zaslon.

1. Koristite tekstni prostor na početnom zaslonu za opis aplikacije koju želite izraditi. Na primjer, **_Želim izraditi aplikaciju za praćenje i upravljanje studentskim zadacima_**. Kliknite na gumb **Pošalji** za slanje prompta AI Copilotu.

![Opišite aplikaciju koju želite izraditi](../../../translated_images/hr/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot će predložiti Dataverse tablicu s poljima koja trebate za pohranu podataka koje želite pratiti i nekim uzorcima podataka. Zatim tablicu možete prilagoditi svojim potrebama koristeći AI Copilot pomoćnika kroz konverzacijske korake.

   > **Važno**: Dataverse je temeljna podatkovna platforma za Power Platformu. To je platforma s malim kodom za pohranu podataka aplikacije. To je potpuno upravljana usluga koja sigurno pohranjuje podatke u Microsoft Cloudu i postavljena je unutar vašeg Power Platform okruženja. Dolazi s ugrađenim mogućnostima upravljanja podacima, poput klasifikacije podataka, podrijetla podataka, finog upravljanja pristupom i još mnogo toga. Više o Dataverseu možete saznati [ovdje](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Predložena polja u vašoj novoj tablici](../../../translated_images/hr/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Nastavnici žele slati e-poštu studentima koji su predali zadatke kako bi ih obavještavali o napretku njihovih zadataka. Možete koristiti Copilot za dodavanje novog polja u tablicu za pohranu e-pošte studenta. Na primjer, možete upotrijebiti sljedeći prompt za dodavanje novog polja u tablicu: **_Želim dodati stupac za pohranu e-pošte studenta_**. Kliknite na gumb **Pošalji** za slanje prompta AI Copilotu.

![Dodavanje novog polja](../../../translated_images/hr/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot će generirati novo polje i zatim ga možete prilagoditi svojim potrebama.


1. Nakon što završite s tablicom, kliknite na gumb **Create app** za kreiranje aplikacije.

1. AI Copilot će generirati responzivnu Canvas aplikaciju na temelju vašeg opisa. Zatim možete prilagoditi aplikaciju prema svojim potrebama.

1. Za nastavnike koji žele slati e-poštu studentima, možete koristiti Copilot za dodavanje novog zaslona u aplikaciju. Na primjer, možete upotrijebiti sljedeći upit za dodavanje novog zaslona u aplikaciju: **_Želim dodati zaslon za slanje e-pošte studentima_**. Kliknite na gumb **Send** za slanje upita AI Copilotu.

![Adding a new screen via a prompt instruction](../../../translated_images/hr/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot će generirati novi zaslon, a zatim možete prilagoditi zaslon prema svojim potrebama.

1. Kad završite s aplikacijom, kliknite na gumb **Save** za spremanje aplikacije.

1. Da biste podijelili aplikaciju s nastavnicima, kliknite na gumb **Share**, a zatim ponovno kliknite na gumb **Share**. Zatim možete podijeliti aplikaciju s nastavnicima unosom njihovih adresa e-pošte.

> **Vaš domaći zadatak**: Aplikacija koju ste upravo izgradili dobar je početak, ali može se poboljšati. S funkcijom e-pošte, nastavnici mogu slati e-poštu studentima samo ručno, unosom njihovih adresa e-pošte. Možete li upotrijebiti Copilot za izradu automatizacije koja će omogućiti nastavnicima da automatski šalju e-poštu studentima kada predaju svoje zadatke? Vaš savjet je da uz pravi upit možete koristiti Copilot u Power Automate za to.

### Izgradite tablicu informacija o računima za naš startup

Financijski tim našeg startupa ima poteškoće s praćenjem računa. Koristili su tablicu za praćenje računa, ali to je postalo teško za upravljanje kako se povećao broj računa. Zamolili su vas da izgradite tablicu koja će im pomoći pohraniti, pratiti i upravljati informacijama o obrađenim računima. Tablica bi trebala biti korištena za izradu automatizacije koja će izvući sve informacije o računima i pohraniti ih u tablicu. Tablica bi također trebala omogućiti financijskom timu da vidi račune koji su plaćeni i one koji nisu.

Power Platform ima osnovnu podatkovnu platformu zvanu Dataverse koja omogućuje pohranu podataka za vaše aplikacije i rješenja. Dataverse pruža low-code podatkovnu platformu za pohranu podataka aplikacije. To je potpuno upravljana usluga koja sigurno pohranjuje podatke u Microsoft Cloud i dostupna je unutar vašeg Power Platform okruženja. Dolazi s ugrađenim funkcijama upravljanja podacima, kao što su klasifikacija podataka, porijeklo podataka, kontrola pristupa s detaljima, i više. Više o Dataverseu možete saznati [ovdje](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Zašto bismo trebali koristiti Dataverse za naš startup? Standardne i prilagođene tablice unutar Dataversea pružaju sigurnu i cloud baziranu opciju pohrane za vaše podatke. Tablice vam omogućuju pohranu različitih tipova podataka, slično kao što možete koristiti više radnih listova u jednoj Excel radnoj knjizi. Možete koristiti tablice za pohranu podataka specifičnih za vašu organizaciju ili poslovne potrebe. Neke od prednosti koje naš startup dobiva korištenjem Dataversea uključuju, ali nisu ograničene na:

- **Lako za upravljanje**: Metapodaci i podaci pohranjuju se u oblaku, tako da se ne morate brinuti o tome kako su pohranjeni ili upravljani. Možete se fokusirati na izradu svojih aplikacija i rješenja.

- **Sigurno**: Dataverse pruža sigurnu i cloud baziranu opciju pohrane za vaše podatke. Možete kontrolirati tko ima pristup podacima u vašim tablicama i kako do njih pristupa koristeći sigurnost baziranu na ulogama.

- **Bogati metapodaci**: Tipovi podataka i odnosi se koriste izravno unutar Power Apps.

- **Logika i validacija**: Možete koristiti poslovna pravila, izračunate polja i pravila validacije za provođenje poslovne logike i održavanje točnosti podataka.

Sada kada znate što je Dataverse i zašto ga koristiti, pogledajmo kako možete koristiti Copilot za kreiranje tablice u Dataverseu koja će zadovoljiti zahtjeve našeg financijskog tima.

> **Napomena** : Ovu tablicu ćete koristiti u sljedećem dijelu za izradu automatizacije koja će izvući sve informacije o računima i pohraniti ih u tablicu.

Da biste kreirali tablicu u Dataverseu koristeći Copilot, slijedite sljedeće korake:

1. Idite na [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) početni zaslon.

2. Na lijevoj navigacijskoj traci odaberite **Tables**, a zatim kliknite na **Describe the new Table**.

![Select new table](../../../translated_images/hr/describe-new-table.0792373eb757281e.webp)

1. Na zaslonu **Describe the new Table** koristite tekstualno područje za opis tablice koju želite stvoriti. Na primjer, **_Želim stvoriti tablicu za pohranu informacija o računima_**. Kliknite na gumb **Send** za slanje upita AI Copilotu.

![Describe the table](../../../translated_images/hr/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot će predložiti Dataverse tablicu s poljima koja vam trebaju za pohranu podataka koje želite pratiti te neke uzorke podataka. Zatim možete prilagoditi tablicu pomoću AI Copilota kroz razgovorne korake.

![Suggested Dataverse table](../../../translated_images/hr/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Financijski tim želi poslati e-poštu dobavljaču kako bi ga obavijestio o trenutnom statusu njihovog računa. Možete koristiti Copilot za dodavanje novog polja u tablicu za pohranu e-pošte dobavljača. Na primjer, možete upotrijebiti sljedeći upit za dodavanje novog polja u tablicu: **_Želim dodati stupac za pohranu e-pošte dobavljača_**. Kliknite na gumb **Send** za slanje upita AI Copilotu.

1. AI Copilot će generirati novo polje, a zatim ga možete prilagoditi prema svojim potrebama.

1. Kada završite s tablicom, kliknite na gumb **Create** za kreiranje tablice.

## AI modeli u Power Platformu s AI Builderom

AI Builder je low-code AI mogućnost dostupna u Power Platformu koja vam omogućuje korištenje AI modela za automatizaciju procesa i predviđanje ishoda. Uz AI Builder možete integrirati AI u svoje aplikacije i tokove rada koji su povezani s vašim podacima u Dataverseu ili u raznim cloud izvorima podataka, poput SharePointa, OneDrivea ili Azure-a.

## Preddefinirani AI modeli vs Prilagođeni AI modeli

AI Builder nudi dvije vrste AI modela: Preddefinirane AI modele i Prilagođene AI modele. Preddefinirani AI modeli su spremni za upotrebu, trenirani od strane Microsofta i dostupni u Power Platformu. Oni vam pomažu dodati inteligenciju vašim aplikacijama i tokovima bez potrebe za prikupljanjem podataka te izgradnjom, treniranjem i objavom vlastitih modela. Možete koristiti ove modele za automatizaciju procesa i predviđanje ishoda.

Neki od preddefiniranih AI modela dostupnih u Power Platformu uključuju:

- **Izdvajanje ključnih fraza**: Ovaj model izvlači ključne fraze iz teksta.
- **Detekcija jezika**: Ovaj model prepoznaje jezik teksta.
- **Analiza sentimenta**: Ovaj model prepoznaje pozitivan, negativan, neutralan ili miješani sentiment u tekstu.
- **Čitač posjetnica**: Ovaj model izvlači informacije s posjetnica.
- **Prepoznavanje teksta**: Ovaj model izvlači tekst iz slika.
- **Detekcija objekata**: Ovaj model prepoznaje i izvlači predmete sa slika.
- **Obrada dokumenata**: Ovaj model izvlači informacije iz obrazaca.
- **Obrada računa**: Ovaj model izvlači informacije iz računa.

Uz Prilagođene AI modele možete unijeti vlastiti model u AI Builder kako bi funkcionirao poput bilo kojeg prilagođenog AI Builder modela, omogućujući vam treniranje modela pomoću vlastitih podataka. Te modele možete koristiti za automatizaciju procesa i predviđanje ishoda u Power Apps i Power Automate. Kad koristite vlastiti model, vrijede određena ograničenja. Više pročitajte na [ovim ograničenjima](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/hr/ai-builder-models.8069423b84cfc47f.webp)

## Zadatak #2 - Izgradite tok za obradu računa za naš startup

Financijski tim ima poteškoće s obradom računa. Koristili su tablicu za praćenje računa, ali to je postalo teško za upravljanje kako se povećao broj računa. Zamolili su vas da izgradite tok rada koji će im pomoći u obradi računa pomoću AI. Tok rada trebao bi im omogućiti izvlačenje informacija iz računa i pohranu tih informacija u Dataverse tablicu. Također, tok rada bi trebao omogućiti slanje e-pošte financijskom timu s izdvojenim informacijama.

Sada kada znate što je AI Builder i zašto ga koristiti, pogledajmo kako možete koristiti AI model za obradu računa u AI Builderu, koji smo ranije spomenuli, za izradu toka rada koji će pomoći financijskom timu u obradi računa.

Da biste izgradili tok rada koji će pomoći financijskom timu u obradi računa koristeći AI model za obradu računa u AI Builderu, slijedite sljedeće korake:

1. Idite na početni zaslon [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Koristite tekstualno područje na početnom zaslonu za opis toka rada koji želite izgraditi. Na primjer, **_Obraditi račun kad stigne u moju pristiglu poštu_**. Kliknite na gumb **Send** za slanje upita AI Copilotu.

   ![Copilot power automate](../../../translated_images/hr/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot će predložiti radnje potrebne za automatizaciju zadatka koji želite. Možete kliknuti na gumb **Next** za prolazak kroz sljedeće korake.

4. U sljedećem koraku, Power Automate će vas tražiti da postavite konekcije potrebne za tok. Kada završite, kliknite na gumb **Create flow** za kreiranje toka.

5. AI Copilot će generirati tok, a zatim možete prilagoditi tok kako vam odgovara.

6. Ažurirajte trigger toka i postavite **Folder** na mapu u kojoj će se pohranjivati računi. Na primjer, možete postaviti mapu na **Inbox**. Kliknite na **Show advanced options** i postavite **Only with Attachments** na **Yes**. Ovo će osigurati da tok radi samo kad je u mapi primljena e-pošta s privitkom.

7. Uklonite sljedeće radnje iz toka: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** i **Compose 4** jer ih nećete koristiti.

8. Uklonite radnju **Condition** iz toka jer je nećete koristiti. Trebalo bi izgledati kao na sljedećem screenshotu:

   ![power automate, remove actions](../../../translated_images/hr/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Kliknite na gumb **Add an action** i potražite **Dataverse**. Odaberite radnju **Add a new row**.

10. U radnji **Extract Information from invoices**, ažurirajte **Invoice File** na **Attachment Content** iz e-pošte. Ovo će osigurati da tok izvlači informacije iz privitka računa.

11. Odaberite **Table** koju ste ranije kreirali. Na primjer, možete odabrati tablicu **Invoice Information**. Odaberite dinamički sadržaj iz prethodne radnje za popunjavanje sljedećih polja:

    - ID
    - Iznos
    - Datum
    - Ime
    - Status - Postavite **Status** na **Pending**.
    - E-pošta dobavljača - Koristite dinamički sadržaj **From** iz triggera **When a new email arrives**.

    ![power automate add row](../../../translated_images/hr/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Kad završite s tokom, kliknite na gumb **Save** za spremanje toka. Zatim možete testirati tok slanjem e-pošte s računom u mapu koju ste naveli u triggeru.

> **Vaš domaći zadatak**: Tok koji ste upravo izgradili je dobar početak, sada trebate razmisliti kako napraviti automatizaciju koja će omogućiti našem financijskom timu da pošalje e-poštu dobavljaču kako bi ga obavijestio o trenutnom statusu njihovog računa. Vaš savjet: tok mora raditi kada se status računa promijeni.

## Koristite AI model za generiranje teksta u Power Automate

AI model Create Text with GPT u AI Builderu omogućuje vam generiranje teksta na temelju upita i koristi Microsoft Azure OpenAI servis. Uz ovu mogućnost, u svoje aplikacije i tokove rada možete integrirati GPT (Generative Pre-Trained Transformer) tehnologiju za izgradnju različitih automatiziranih tokova i korisnih aplikacija.

GPT modeli prolaze kroz opsežno treniranje na velikim količinama podataka, što im omogućuje generiranje teksta koji je vrlo sličan ljudskom jeziku kada im se da upit. Kad se integriraju s automatizacijom tokova rada, AI modeli poput GPT mogu se koristiti za pojednostavljenje i automatizaciju mnogih zadataka.

Na primjer, možete izgraditi tokove koji automatski generiraju tekst za razne slučajeve upotrebe, kao što su: nacrti e-pošte, opisi proizvoda i slično. Također možete koristiti model za generiranje teksta u različitim aplikacijama, poput chatbotova i aplikacija za korisničku podršku koje omogućuju agentima za podršku učinkovito i brzo odgovaranje na upite korisnika.

![create a prompt](../../../translated_images/hr/create-prompt-gpt.69d429300c2e870a.webp)


Da naučite kako koristiti ovaj AI model u Power Automate, provedite se kroz modul [Dodavanje inteligencije s AI Builder i GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Sjajan posao! Nastavite sa učenjem

Nakon što završite ovu lekciju, pogledajte našu [Generativnu AI zbirku za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili nadograđivati svoje znanje o Generativnoj AI!

Želite li prilagoditi i izvući više iz Copilota? Istražite [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — zbirku uputa, agenata, vještina i konfiguracija koju doprinosi zajednica, kako biste maksimalno iskoristili GitHub Copilot.

Krenite na Lekciju 11 gdje ćemo pogledati kako [integrirati Generativnu AI s Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->