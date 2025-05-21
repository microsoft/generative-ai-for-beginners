<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T22:07:34+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "hr"
}
-->
# Dizajniranje UX-a za AI aplikacije

> _(Kliknite na sliku iznad za pregledavanje videozapisa ove lekcije)_

Korisničko iskustvo vrlo je važan aspekt izgradnje aplikacija. Korisnici trebaju biti u mogućnosti koristiti vašu aplikaciju na učinkovit način kako bi obavljali zadatke. Biti učinkovit je jedno, ali također trebate dizajnirati aplikacije tako da ih svi mogu koristiti, kako bi bile _pristupačne_. Ovo poglavlje će se fokusirati na ovo područje kako biste, nadamo se, na kraju dizajnirali aplikaciju koju ljudi mogu i žele koristiti.

## Uvod

Korisničko iskustvo je način na koji korisnik interaktivno koristi određeni proizvod ili uslugu, bilo da se radi o sustavu, alatu ili dizajnu. Kada razvijaju AI aplikacije, programeri ne samo da se fokusiraju na osiguravanje učinkovitog korisničkog iskustva, već i etičkog. U ovoj lekciji pokrivamo kako izgraditi aplikacije umjetne inteligencije (AI) koje odgovaraju potrebama korisnika.

Lekcija će pokriti sljedeća područja:

- Uvod u korisničko iskustvo i razumijevanje potreba korisnika
- Dizajniranje AI aplikacija za povjerenje i transparentnost
- Dizajniranje AI aplikacija za suradnju i povratne informacije

## Ciljevi učenja

Nakon ove lekcije, moći ćete:

- Razumjeti kako izgraditi AI aplikacije koje zadovoljavaju potrebe korisnika.
- Dizajnirati AI aplikacije koje promiču povjerenje i suradnju.

### Preduvjet

Odvojite malo vremena i pročitajte više o [korisničkom iskustvu i dizajnerskom razmišljanju.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Uvod u korisničko iskustvo i razumijevanje potreba korisnika

U našem fiktivnom startupu za obrazovanje imamo dva primarna korisnika, učitelje i učenike. Svaki od tih korisnika ima jedinstvene potrebe. Dizajn usmjeren na korisnika daje prioritet korisniku osiguravajući da su proizvodi relevantni i korisni za one kojima su namijenjeni.

Aplikacija bi trebala biti **korisna, pouzdana, pristupačna i ugodna** kako bi pružila dobro korisničko iskustvo.

### Upotrebljivost

Biti koristan znači da aplikacija ima funkcionalnost koja odgovara njezinoj namjeni, kao što je automatizacija procesa ocjenjivanja ili generiranje kartica za ponavljanje. Aplikacija koja automatizira proces ocjenjivanja trebala bi biti sposobna točno i učinkovito dodijeliti ocjene učenicima na temelju unaprijed definiranih kriterija. Slično tome, aplikacija koja generira kartice za ponavljanje trebala bi biti sposobna stvoriti relevantna i raznolika pitanja na temelju svojih podataka.

### Pouzdanost

Biti pouzdan znači da aplikacija može dosljedno i bez grešaka obavljati svoj zadatak. Međutim, AI, baš kao i ljudi, nije savršen i može biti sklon greškama. Aplikacije mogu naići na pogreške ili neočekivane situacije koje zahtijevaju ljudsku intervenciju ili ispravak. Kako se nosite s greškama? U posljednjem dijelu ove lekcije, pokrit ćemo kako su AI sustavi i aplikacije dizajnirani za suradnju i povratne informacije.

### Pristupačnost

Biti pristupačan znači proširiti korisničko iskustvo na korisnike s različitim sposobnostima, uključujući one s invaliditetom, osiguravajući da nitko nije isključen. Slijedeći smjernice i principe pristupačnosti, AI rješenja postaju inkluzivnija, upotrebljivija i korisnija za sve korisnike.

### Ugodnost

Biti ugodan znači da je aplikacija ugodna za korištenje. Privlačno korisničko iskustvo može imati pozitivan utjecaj na korisnika, potičući ga da se vrati aplikaciji i povećavajući prihod poslovanja.

Ne svaki izazov može se riješiti AI-om. AI dolazi kako bi unaprijedio vaše korisničko iskustvo, bilo da se radi o automatizaciji ručnih zadataka ili personalizaciji korisničkih iskustava.

## Dizajniranje AI aplikacija za povjerenje i transparentnost

Izgradnja povjerenja je ključna kada se dizajniraju AI aplikacije. Povjerenje osigurava da korisnik ima povjerenja da će aplikacija obaviti posao, dosljedno isporučivati rezultate i da su rezultati ono što korisnik treba. Rizik u ovom području je nepovjerenje i preveliko povjerenje. Nepovjerenje se javlja kada korisnik ima malo ili nimalo povjerenja u AI sustav, što dovodi do odbacivanja vaše aplikacije. Preveliko povjerenje se događa kada korisnik precijeni sposobnost AI sustava, što dovodi do toga da korisnici previše vjeruju AI sustavu. Na primjer, automatizirani sustav ocjenjivanja u slučaju prevelikog povjerenja mogao bi dovesti do toga da učitelj ne provjeri neka od radova kako bi osigurao da sustav ocjenjivanja dobro funkcionira. To bi moglo rezultirati nepravednim ili netočnim ocjenama za učenike ili propuštenim prilikama za povratne informacije i poboljšanje.

Dva načina da se osigura da je povjerenje stavljeno u središte dizajna su objašnjivost i kontrola.

### Objašnjivost

Kada AI pomaže u donošenju odluka, kao što je prenošenje znanja budućim generacijama, ključno je da učitelji i roditelji razumiju kako se donose AI odluke. Ovo je objašnjivost - razumijevanje kako AI aplikacije donose odluke. Dizajniranje za objašnjivost uključuje dodavanje detalja o primjerima što AI aplikacija može učiniti. Na primjer, umjesto "Započnite s AI učiteljem", sustav može koristiti: "Sažmite svoje bilješke za lakše ponavljanje koristeći AI."

Drugi primjer je kako AI koristi korisničke i osobne podatke. Na primjer, korisnik s personom učenika može imati ograničenja temeljena na njihovoj personi. AI možda neće moći otkriti odgovore na pitanja, ali može pomoći korisniku da razmisli o tome kako može riješiti problem.

Jedan posljednji ključni dio objašnjivosti je pojednostavljenje objašnjenja. Učenici i učitelji možda nisu stručnjaci za AI, stoga objašnjenja o tome što aplikacija može ili ne može učiniti trebaju biti pojednostavljena i lako razumljiva.

### Kontrola

Generativni AI stvara suradnju između AI-a i korisnika, gdje, na primjer, korisnik može modificirati upite za različite rezultate. Osim toga, kada se generira izlaz, korisnici bi trebali moći modificirati rezultate, dajući im osjećaj kontrole. Na primjer, kada koristite Bing, možete prilagoditi svoj upit na temelju formata, tona i duljine. Osim toga, možete dodati promjene svom izlazu i modificirati ga kako je prikazano dolje:

Još jedna značajka u Bingu koja omogućuje korisniku da ima kontrolu nad aplikacijom je mogućnost uključivanja i isključivanja podataka koje AI koristi. Za školsku aplikaciju, učenik možda želi koristiti svoje bilješke kao i učiteljeve resurse kao materijal za ponavljanje.

> Kada dizajnirate AI aplikacije, namjera je ključna u osiguravanju da korisnici ne postavljaju nerealna očekivanja o sposobnostima AI-a. Jedan način da to učinite je stvaranje trenja između upita i rezultata. Podsjećajući korisnika da je ovo AI, a ne drugi čovjek.

## Dizajniranje AI aplikacija za suradnju i povratne informacije

Kao što je ranije spomenuto, generativni AI stvara suradnju između korisnika i AI-a. Većina angažmana je s korisnikom koji unosi upit, a AI generira izlaz. Što ako je izlaz netočan? Kako aplikacija rješava pogreške ako se pojave? Da li AI okrivljuje korisnika ili odvoji vrijeme da objasni pogrešku?

AI aplikacije trebaju biti izgrađene kako bi primale i davale povratne informacije. Ovo ne samo da pomaže AI sustavu da se poboljša, već i gradi povjerenje s korisnicima. Povratna petlja trebala bi biti uključena u dizajn, primjer može biti jednostavan palac gore ili dolje na izlazu.

Drugi način za rješavanje ovog problema je jasno komuniciranje sposobnosti i ograničenja sustava. Kada korisnik napravi pogrešku tražeći nešto izvan AI sposobnosti, trebalo bi postojati način za rješavanje ovog problema, kao što je prikazano dolje.

Sistemske pogreške su česte kod aplikacija gdje korisnik možda treba pomoć s informacijama izvan opsega AI-a ili aplikacija može imati ograničenje koliko pitanja/predmeta korisnik može generirati sažetke. Na primjer, AI aplikacija obučena s podacima o ograničenim predmetima, na primjer, povijest i matematika, možda neće moći rješavati pitanja o geografiji. Da bi se to ublažilo, AI sustav može dati odgovor poput: "Žao nam je, naš proizvod je obučen s podacima o sljedećim predmetima....., ne mogu odgovoriti na pitanje koje ste postavili."

AI aplikacije nisu savršene, stoga su sklone pogreškama. Kada dizajnirate svoje aplikacije, trebali biste osigurati prostor za povratne informacije od korisnika i rješavanje pogrešaka na način koji je jednostavan i lako objašnjiv.

## Zadaci

Uzmi bilo koju AI aplikaciju koju si dosad izgradio, razmisli o implementaciji sljedećih koraka u svojoj aplikaciji:

- **Ugodnost:** Razmisli kako možeš učiniti svoju aplikaciju ugodnijom. Dodaješ li objašnjenja posvuda? Potičeš li korisnika na istraživanje? Kako formuliraš svoje poruke o pogreškama?

- **Upotrebljivost:** Izgradnja web aplikacije. Osiguraj da je tvoja aplikacija navigabilna i mišem i tipkovnicom.

- **Povjerenje i transparentnost:** Ne vjeruj AI-u potpuno i njegovom izlazu, razmisli kako bi dodao čovjeka u proces kako bi provjerio izlaz. Također, razmisli i implementiraj druge načine za postizanje povjerenja i transparentnosti.

- **Kontrola:** Daj korisniku kontrolu nad podacima koje pruža aplikaciji. Implementiraj način na koji korisnik može uključiti i isključiti prikupljanje podataka u AI aplikaciji.

## Nastavi svoje učenje!

Nakon završetka ove lekcije, pogledaj našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako bi nastavio unapređivati svoje znanje o generativnoj AI!

Idi na Lekciju 13, gdje ćemo pogledati kako [osigurati AI aplikacije](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.