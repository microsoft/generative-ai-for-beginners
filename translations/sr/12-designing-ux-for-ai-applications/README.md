<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T22:07:04+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "sr"
}
-->
# Dizajniranje UX za AI aplikacije

Korisničko iskustvo je veoma važan aspekt izgradnje aplikacija. Korisnici moraju biti u stanju da koriste vašu aplikaciju na efikasan način kako bi obavili zadatke. Efikasnost je jedna stvar, ali takođe morate dizajnirati aplikacije tako da ih svi mogu koristiti, da budu _pristupačne_. Ovaj deo će se fokusirati na to područje kako biste na kraju dizajnirali aplikaciju koju ljudi mogu i žele da koriste.

## Uvod

Korisničko iskustvo je način na koji korisnik interaguje sa i koristi određeni proizvod ili uslugu, bilo da je to sistem, alat ili dizajn. Kada razvijaju AI aplikacije, programeri ne samo da se fokusiraju na to da korisničko iskustvo bude efektivno, već i etično. U ovoj lekciji pokrivamo kako izgraditi aplikacije veštačke inteligencije (AI) koje zadovoljavaju potrebe korisnika.

Lekcija će pokriti sledeće oblasti:

- Uvod u korisničko iskustvo i razumevanje potreba korisnika
- Dizajniranje AI aplikacija za poverenje i transparentnost
- Dizajniranje AI aplikacija za saradnju i povratne informacije

## Ciljevi učenja

Nakon ove lekcije, moći ćete:

- Razumeti kako izgraditi AI aplikacije koje zadovoljavaju potrebe korisnika.
- Dizajnirati AI aplikacije koje promovišu poverenje i saradnju.

### Preduslov

Odvojite vreme i pročitajte više o [korisničkom iskustvu i dizajnerskom razmišljanju.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Uvod u korisničko iskustvo i razumevanje potreba korisnika

U našem fiktivnom obrazovnom startapu imamo dva primarna korisnika, nastavnike i učenike. Svaki od dva korisnika ima jedinstvene potrebe. Dizajn orijentisan na korisnika prioritizuje korisnika, osiguravajući da su proizvodi relevantni i korisni za one kojima su namenjeni.

Aplikacija treba da bude **korisna, pouzdana, pristupačna i prijatna** da bi pružila dobro korisničko iskustvo.

### Upotrebljivost

Biti koristan znači da aplikacija ima funkcionalnost koja odgovara njenoj nameni, kao što je automatizacija procesa ocenjivanja ili generisanje kartica za ponavljanje gradiva. Aplikacija koja automatizuje proces ocenjivanja treba da može tačno i efikasno da dodeli ocene učenicima na osnovu unapred definisanih kriterijuma. Slično tome, aplikacija koja generiše kartice za ponavljanje treba da može da kreira relevantna i raznolika pitanja na osnovu svojih podataka.

### Pouzdanost

Biti pouzdan znači da aplikacija može dosledno i bez grešaka obavljati svoj zadatak. Međutim, AI kao i ljudi nije savršen i može biti sklon greškama. Aplikacije mogu naići na greške ili neočekivane situacije koje zahtevaju ljudsku intervenciju ili korekciju. Kako se nositi sa greškama? U poslednjem delu ove lekcije, pokrićemo kako su AI sistemi i aplikacije dizajnirani za saradnju i povratne informacije.

### Pristupačnost

Biti pristupačan znači proširiti korisničko iskustvo na korisnike sa različitim sposobnostima, uključujući one sa invaliditetom, osiguravajući da niko nije izostavljen. Prateći smernice i principe pristupačnosti, AI rešenja postaju inkluzivnija, upotrebljivija i korisnija za sve korisnike.

### Prijatnost

Biti prijatan znači da je aplikacija užitak za korišćenje. Privlačno korisničko iskustvo može imati pozitivan uticaj na korisnika, podstičući ga da se vrati aplikaciji i povećavajući poslovne prihode.

Nije svaki izazov moguće rešiti sa AI. AI dolazi da unapredi vaše korisničko iskustvo, bilo da se radi o automatizaciji manuelnih zadataka ili personalizaciji korisničkih iskustava.

## Dizajniranje AI aplikacija za poverenje i transparentnost

Izgradnja poverenja je ključna kada se dizajniraju AI aplikacije. Poverenje osigurava da korisnik bude siguran da će aplikacija obaviti posao, dosledno isporučiti rezultate i da su rezultati ono što korisnik treba. Rizik u ovoj oblasti je nepoverenje i preterano poverenje. Nepoverenje se javlja kada korisnik ima malo ili nimalo poverenja u AI sistem, što dovodi do odbacivanja vaše aplikacije. Preterano poverenje se javlja kada korisnik preceni sposobnosti AI sistema, što dovodi do toga da korisnici previše veruju AI sistemu. Na primer, automatizovani sistem ocenjivanja u slučaju preteranog poverenja može dovesti do toga da nastavnik ne pregleda neke radove kako bi se osiguralo da sistem ocenjivanja dobro funkcioniše. To bi moglo rezultirati nefer ili netačnim ocenama za učenike, ili propuštenim prilikama za povratne informacije i poboljšanje.

Dva načina da se osigura da poverenje bude u centru dizajna su objašnjivost i kontrola.

### Objašnjivost

Kada AI pomaže u donošenju odluka kao što je prenošenje znanja budućim generacijama, važno je da nastavnici i roditelji razumeju kako AI donosi odluke. To je objašnjivost - razumevanje kako AI aplikacije donose odluke. Dizajniranje za objašnjivost uključuje dodavanje detalja o primerima šta AI aplikacija može da uradi. Na primer, umesto "Započnite sa AI nastavnikom", sistem može koristiti: "Sumirajte svoje beleške za lakše ponavljanje koristeći AI."

Još jedan primer je kako AI koristi korisničke i lične podatke. Na primer, korisnik sa personom učenika može imati ograničenja na osnovu svoje persone. AI možda neće moći da otkrije odgovore na pitanja, ali može pomoći korisniku da razmisli o tome kako može rešiti problem.

Jedan poslednji ključni deo objašnjivosti je pojednostavljivanje objašnjenja. Učenici i nastavnici možda nisu stručnjaci za AI, stoga objašnjenja o tome šta aplikacija može ili ne može da uradi treba da budu pojednostavljena i laka za razumevanje.

### Kontrola

Generativna AI stvara saradnju između AI i korisnika, gde na primer korisnik može modifikovati upite za različite rezultate. Dodatno, kada se generiše izlaz, korisnici treba da mogu da modifikuju rezultate dajući im osećaj kontrole. Na primer, kada koristite Bing, možete prilagoditi svoj upit na osnovu formata, tona i dužine. Dodatno, možete dodati promene svom izlazu i modifikovati izlaz kao što je prikazano ispod:

Još jedna karakteristika u Bing-u koja omogućava korisniku da ima kontrolu nad aplikacijom je sposobnost da se uključi ili isključi iz podataka koje AI koristi. Za školsku aplikaciju, učenik možda želi da koristi svoje beleške kao i resurse nastavnika kao materijal za ponavljanje.

> Kada dizajnirate AI aplikacije, namera je ključna u osiguravanju da korisnici ne preterano veruju postavljajući nerealna očekivanja o njenim sposobnostima. Jedan način da se to postigne je stvaranje trenja između upita i rezultata. Podsećajući korisnika da je ovo AI, a ne drugi čovek.

## Dizajniranje AI aplikacija za saradnju i povratne informacije

Kao što je ranije pomenuto, generativna AI stvara saradnju između korisnika i AI. Većina interakcija je sa korisnikom koji unosi upit, a AI generiše izlaz. Šta ako je izlaz netačan? Kako aplikacija postupa sa greškama ako se pojave? Da li AI krivi korisnika ili uzima vreme da objasni grešku?

AI aplikacije treba da budu izgrađene da primaju i daju povratne informacije. To ne samo da pomaže AI sistemu da se poboljša, već i gradi poverenje sa korisnicima. Povratna petlja treba da bude uključena u dizajn, primer može biti jednostavan palac gore ili dole na izlazu.

Još jedan način da se to postigne je jasno komuniciranje sposobnosti i ograničenja sistema. Kada korisnik napravi grešku tražeći nešto van AI sposobnosti, treba da postoji način da se to reši, kao što je prikazano ispod.

Sistemske greške su česte kod aplikacija gde korisnik možda treba pomoć sa informacijama van opsega AI ili aplikacija može imati ograničenje koliko pitanja/predmeta korisnik može generisati sažetke. Na primer, AI aplikacija obučena sa podacima o ograničenim predmetima kao što su Istorija i Matematika možda neće moći da se nosi sa pitanjima o Geografiji. Da bi se to ublažilo, AI sistem može dati odgovor kao: "Žao nam je, naš proizvod je obučavan sa podacima u sledećim predmetima....., ne mogu da odgovorim na pitanje koje ste postavili."

AI aplikacije nisu savršene, stoga su sklone greškama. Kada dizajnirate svoje aplikacije, treba da osigurate da stvorite prostor za povratne informacije od korisnika i rukovanje greškama na način koji je jednostavan i lako objašnjiv.

## Zadatak

Uzmite bilo koju AI aplikaciju koju ste do sada izgradili, razmislite o implementaciji sledećih koraka u svojoj aplikaciji:

- **Prijatnost:** Razmislite kako možete učiniti svoju aplikaciju prijatnijom. Da li dodajete objašnjenja svuda? Da li podstičete korisnika da istražuje? Kako formulirate svoje poruke o greškama?

- **Upotrebljivost:** Izgradnja web aplikacije. Uverite se da je vaša aplikacija navigabilna i mišem i tastaturom.

- **Poverenje i transparentnost:** Nemojte potpuno verovati AI i njenom izlazu, razmislite kako biste dodali čoveka u proces da verifikuje izlaz. Takođe, razmislite i implementirajte druge načine za postizanje poverenja i transparentnosti.

- **Kontrola:** Dajte korisniku kontrolu nad podacima koje pruža aplikaciji. Implementirajte način da korisnik može da se uključi ili isključi iz prikupljanja podataka u AI aplikaciji.

## Nastavite sa učenjem!

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili da unapređujete svoje znanje o generativnoj AI!

Pređite na Lekciju 13, gde ćemo pogledati kako [osigurati AI aplikacije](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI услуге превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неразумевања или погрешна тумачења која произилазе из коришћења овог превода.