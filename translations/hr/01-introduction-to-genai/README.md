<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:08:52+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "hr"
}
-->
# Uvod u Generativnu AI i Velike Jezične Modele

_(Kliknite na sliku iznad za prikaz videa ove lekcije)_

Generativna AI je umjetna inteligencija sposobna generirati tekst, slike i druge vrste sadržaja. Ono što je čini fantastičnom tehnologijom je to što demokratizira AI, svatko je može koristiti s jednostavnim tekstualnim promptom, rečenicom napisanom na prirodnom jeziku. Nema potrebe da učite jezik poput Jave ili SQL-a kako biste postigli nešto vrijedno, sve što trebate je koristiti svoj jezik, iznijeti što želite i AI model će dati prijedlog. Primjene i utjecaj ovoga su ogromni, možete pisati ili razumjeti izvještaje, pisati aplikacije i još mnogo toga, sve u nekoliko sekundi.

U ovom kurikulumu istražit ćemo kako naš startup koristi generativnu AI za otključavanje novih scenarija u svijetu obrazovanja i kako se nosimo s neizbježnim izazovima povezanim s društvenim implikacijama njezine primjene i tehnološkim ograničenjima.

## Uvod

Ova lekcija će pokriti:

- Uvod u poslovni scenarij: naša startup ideja i misija.
- Generativna AI i kako smo došli do trenutnog tehnološkog pejzaža.
- Unutarnji rad velikog jezičnog modela.
- Glavne sposobnosti i praktični slučajevi uporabe Velikih Jezičnih Modela.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete:

- Što je generativna AI i kako rade Veliki Jezični Modeli.
- Kako možete iskoristiti velike jezične modele za različite slučajeve uporabe, s naglaskom na obrazovne scenarije.

## Scenarij: naš obrazovni startup

Generativna umjetna inteligencija (AI) predstavlja vrhunac AI tehnologije, pomičući granice onoga što se nekad smatralo nemogućim. Generativni AI modeli imaju nekoliko sposobnosti i primjena, ali za ovaj kurikulum istražit ćemo kako revolucionira obrazovanje kroz fiktivni startup. Ovaj startup ćemo nazvati _naš startup_. Naš startup djeluje u obrazovnom području s ambicioznom misijom

> _poboljšanja pristupačnosti u učenju, na globalnoj razini, osiguravajući ravnopravan pristup obrazovanju i pružajući personalizirana iskustva učenja svakom učeniku, prema njihovim potrebama_.

Naš startup tim je svjestan da nećemo moći postići ovaj cilj bez korištenja jednog od najmoćnijih alata modernog doba – Velikih Jezičnih Modela (LLMs).

Očekuje se da će generativna AI revolucionirati način na koji danas učimo i poučavamo, s učenicima koji imaju na raspolaganju virtualne učitelje 24 sata dnevno koji pružaju velike količine informacija i primjera, i učiteljima koji mogu koristiti inovativne alate za procjenu svojih učenika i davanje povratnih informacija.

Za početak, definirajmo neke osnovne pojmove i terminologiju koju ćemo koristiti kroz cijeli kurikulum.

## Kako smo dobili Generativnu AI?

Unatoč izvanrednom _hypeu_ stvorenom nedavno najavom generativnih AI modela, ova tehnologija se razvija desetljećima, s prvim istraživačkim naporima koji datiraju iz 60-ih. Sada smo na točki gdje AI ima ljudske kognitivne sposobnosti, poput razgovora, što pokazuju na primjer [OpenAI ChatGPT](https://openai.com/chatgpt) ili [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), koji također koristi GPT model za pretraživanje weba u Bing razgovorima.

Vraćajući se malo unatrag, prvi prototipovi AI sastojali su se od chatbota na pisaćem stroju, oslanjajući se na bazu znanja izvučenu iz grupe stručnjaka i predstavljenu u računalu. Odgovori u bazi znanja bili su pokrenuti ključnim riječima koje se pojavljuju u ulaznom tekstu.
Međutim, ubrzo je postalo jasno da takav pristup, koristeći chatbote na pisaćem stroju, nije dobro skalirao.

### Statistički pristup AI: Strojno učenje

Prekretnica je stigla tijekom 90-ih, s primjenom statističkog pristupa analizi teksta. To je dovelo do razvoja novih algoritama – poznatih kao strojno učenje – sposobnih učiti obrasce iz podataka bez eksplicitnog programiranja. Ovaj pristup omogućava strojevima da simuliraju razumijevanje ljudskog jezika: statistički model je treniran na parovima tekst-oznaka, omogućujući modelu da klasificira nepoznati ulazni tekst s unaprijed definiranom oznakom koja predstavlja namjeru poruke.

### Neuronske mreže i moderni virtualni asistenti

U posljednjih nekoliko godina, tehnološka evolucija hardvera, sposobnog za obradu većih količina podataka i složenijih izračuna, potaknula je istraživanja u AI, što je dovelo do razvoja naprednih algoritama strojnog učenja poznatih kao neuronske mreže ili algoritmi dubokog učenja.

Neuronske mreže (i posebno Rekurentne Neuronske Mreže – RNNs) značajno su poboljšale obradu prirodnog jezika, omogućujući prikazivanje značenja teksta na značajniji način, vrednujući kontekst riječi u rečenici.

Ovo je tehnologija koja je pokretala virtualne asistente rođene u prvom desetljeću novog stoljeća, vrlo vješte u tumačenju ljudskog jezika, identificiranju potrebe i izvršavanju radnje kako bi je zadovoljile – poput odgovaranja unaprijed definiranim skriptom ili korištenja usluge treće strane.

### Današnje vrijeme, Generativna AI

Tako smo došli do Generativne AI danas, koja se može promatrati kao podskup dubokog učenja.

Nakon desetljeća istraživanja u AI polju, nova arhitektura modela – nazvana _Transformer_ – nadmašila je ograničenja RNN-ova, budući da je sposobna primiti puno duže sekvence teksta kao ulaz. Transformeri se temelje na mehanizmu pažnje, omogućujući modelu da daje različite težine ulazima koje prima, ‘posvećujući više pažnje’ tamo gdje je koncentrirana najrelevantnija informacija, bez obzira na njihov redoslijed u tekstualnoj sekvenci.

Većina nedavnih generativnih AI modela – također poznatih kao Veliki Jezični Modeli (LLMs), budući da rade s tekstualnim ulazima i izlazima – doista se temelji na ovoj arhitekturi. Ono što je zanimljivo kod ovih modela – treniranih na ogromnoj količini neoznačenih podataka iz različitih izvora poput knjiga, članaka i web stranica – jest da se mogu prilagoditi širokom spektru zadataka i generirati gramatički ispravan tekst s naznakom kreativnosti. Dakle, ne samo da su nevjerojatno poboljšali sposobnost stroja da ‘razumije’ ulazni tekst, već su omogućili i njihovu sposobnost generiranja originalnog odgovora na ljudskom jeziku.

## Kako rade veliki jezični modeli?

U sljedećem poglavlju istražit ćemo različite vrste generativnih AI modela, ali za sada pogledajmo kako rade veliki jezični modeli, s naglaskom na OpenAI GPT (Generativni Predtrenirani Transformer) modele.

- **Tokenizer, tekst u brojeve**: Veliki Jezični Modeli primaju tekst kao ulaz i generiraju tekst kao izlaz. Međutim, budući da su statistički modeli, bolje rade s brojevima nego s tekstualnim sekvencama. Zato se svaki ulaz u model obrađuje pomoću tokenizera prije nego što ga koristi osnovni model. Token je dio teksta – koji se sastoji od varijabilnog broja znakova, tako da je glavna zadaća tokenizera razdvajanje ulaza na niz tokena. Zatim se svaki token mapira s indeksom tokena, što je cjelobrojno kodiranje izvornog dijela teksta.

- **Predviđanje izlaznih tokena**: S obzirom na n tokena kao ulaz (s maksimalnim n koji varira od jednog modela do drugog), model može predvidjeti jedan token kao izlaz. Taj se token zatim uključuje u ulaz sljedeće iteracije, u obrascu proširenja prozora, omogućujući bolji korisnički doživljaj dobivanja jedne (ili više) rečenica kao odgovora. To objašnjava zašto, ako ste se ikad igrali s ChatGPT-om, možda ste primijetili da ponekad izgleda kao da staje usred rečenice.

- **Proces odabira, distribucija vjerojatnosti**: Izlazni token odabire model prema njegovoj vjerojatnosti pojavljivanja nakon trenutne tekstualne sekvence. To je zato što model predviđa distribuciju vjerojatnosti za sve moguće ‘sljedeće tokene’, izračunatu na temelju njegovog treninga. Međutim, ne bira se uvijek token s najvišom vjerojatnošću iz rezultirajuće distribucije. Stupanj slučajnosti dodaje se ovom izboru, na način da model djeluje na nedeterministički način - ne dobivamo isti izlaz za isti ulaz. Ovaj stupanj slučajnosti dodaje se kako bi se simulirao proces kreativnog razmišljanja i može se prilagoditi pomoću parametra modela nazvanog temperatura.

## Kako naš startup može iskoristiti Velike Jezične Modele?

Sada kada bolje razumijemo unutarnji rad velikog jezičnog modela, pogledajmo nekoliko praktičnih primjera najčešćih zadataka koje mogu prilično dobro obaviti, s pogledom na naš poslovni scenarij.
Rekli smo da je glavna sposobnost Velikog Jezičnog Modela _generiranje teksta od nule, počevši od tekstualnog ulaza, napisanog na prirodnom jeziku_.

Ali kakav tekstualni ulaz i izlaz?
Ulaz velikog jezičnog modela poznat je kao prompt, dok je izlaz poznat kao completion, pojam koji se odnosi na mehanizam modela generiranja sljedećeg tokena za dovršavanje trenutnog ulaza. Istražit ćemo duboko što je prompt i kako ga dizajnirati na način da izvučemo najviše iz našeg modela. Ali za sada, recimo da prompt može uključivati:

- **Instrukciju** koja specificira vrstu izlaza koju očekujemo od modela. Ova instrukcija ponekad može sadržavati neke primjere ili dodatne podatke.

  1. Sažimanje članka, knjige, recenzija proizvoda i više, uz izvlačenje uvida iz nestrukturiranih podataka.
  
  2. Kreativno osmišljavanje i dizajn članka, eseja, zadatka ili više.

- **Pitanje**, postavljeno u obliku razgovora s agentom.

- Dio **teksta za dovršavanje**, što implicitno znači traženje pomoći pri pisanju.

- Dio **koda** zajedno sa zahtjevom za objašnjenje i dokumentiranje, ili komentar tražeći generiranje dijela koda koji obavlja određeni zadatak.

Gore navedeni primjeri su prilično jednostavni i nisu namijenjeni kao iscrpna demonstracija sposobnosti Velikih Jezičnih Modela. Oni su namijenjeni pokazivanju potencijala korištenja generativne AI, posebno ali ne ograničavajući se na obrazovne kontekste.

Također, izlaz generativnog AI modela nije savršen i ponekad kreativnost modela može djelovati protiv njega, rezultirajući izlazom koji je kombinacija riječi koje ljudski korisnik može protumačiti kao mistifikaciju stvarnosti, ili može biti uvredljiv. Generativna AI nije inteligentna - barem u sveobuhvatnijoj definiciji inteligencije, uključujući kritičko i kreativno razmišljanje ili emocionalnu inteligenciju; nije deterministička i nije pouzdana, budući da se izmišljotine, poput pogrešnih referenci, sadržaja i izjava, mogu kombinirati s točnim informacijama i predstaviti na uvjerljiv i samopouzdan način. U sljedećim lekcijama bavit ćemo se svim ovim ograničenjima i vidjeti što možemo učiniti da ih ublažimo.

## Zadatak

Vaš zadatak je pročitati više o [generativnoj AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i pokušati identificirati područje gdje biste danas dodali generativnu AI koja ga nema. Kako bi utjecaj bio drugačiji od toga da se radi na "stari način", možete li učiniti nešto što prije niste mogli, ili ste brži? Napišite sažetak od 300 riječi o tome kako bi izgledao vaš AI startup iz snova i uključite naslove poput "Problem", "Kako bih koristio AI", "Utjecaj" i opcionalno poslovni plan.

Ako ste izvršili ovaj zadatak, možda ste čak spremni prijaviti se u Microsoftov inkubator, [Microsoft za Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) nudimo kredite za Azure, OpenAI, mentorstvo i još mnogo toga, provjerite!

## Provjera znanja

Što je istina o velikim jezičnim modelima?

1. Dobivate isti odgovor svaki put.
1. Radi stvari savršeno, odlično zbraja brojeve, proizvodi radni kod itd.
1. Odgovor može varirati unatoč korištenju istog prompta. Također je odlično za davanje prvog nacrta nečega, bilo da je to tekst ili kod. Ali trebate poboljšati rezultate.

A: 3, LLM je nedeterministički, odgovor varira, međutim, možete kontrolirati njegovu varijancu putem postavke temperature. Također ne biste trebali očekivati da radi stvari savršeno, tu je da obavi težak posao za vas, što često znači da dobivate dobar prvi pokušaj nečega što trebate postupno poboljšavati.

## Odličan posao! Nastavite putovanje

Nakon završetka ove lekcije, provjerite našu [kolekciju za učenje o Generativnoj AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

Idite na Lekciju 2 gdje ćemo pogledati kako [istraživati i uspoređivati različite vrste LLM-ova](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI prevoditeljske usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.