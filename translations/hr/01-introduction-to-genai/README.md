<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:40:30+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "hr"
}
-->
# Uvod u Generativnu AI i Velike Jezične Modele

_(Kliknite na sliku iznad za pregled videozapisa ove lekcije)_

Generativna AI je umjetna inteligencija sposobna generirati tekst, slike i druge vrste sadržaja. Ono što je čini fantastičnom tehnologijom je to što demokratizira AI; svatko je može koristiti uz jednostavan tekstualni upit, rečenicu napisanu prirodnim jezikom. Nema potrebe za učenjem jezika poput Jave ili SQL-a da biste postigli nešto vrijedno, sve što trebate je koristiti svoj jezik, navesti što želite i AI model će vam ponuditi prijedlog. Primjene i utjecaj ovoga su ogromni, možete pisati ili razumjeti izvještaje, pisati aplikacije i mnogo više, sve u nekoliko sekundi.

U ovom kurikulumu istražit ćemo kako naš startup koristi generativnu AI za otključavanje novih scenarija u svijetu obrazovanja i kako se nosimo s neizbježnim izazovima povezanim sa socijalnim implikacijama njegove primjene i ograničenjima tehnologije.

## Uvod

Ova lekcija će pokriti:

- Uvod u poslovni scenarij: našu startup ideju i misiju.
- Generativnu AI i kako smo došli do trenutnog tehnološkog okruženja.
- Unutarnji rad velikog jezičnog modela.
- Glavne sposobnosti i praktični slučajevi upotrebe Velikih Jezičnih Modela.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete:

- Što je generativna AI i kako rade Veliki Jezični Modeli.
- Kako možete koristiti velike jezične modele za različite slučajeve upotrebe, s fokusom na obrazovne scenarije.

## Scenarij: naš obrazovni startup

Generativna Umjetna Inteligencija (AI) predstavlja vrhunac AI tehnologije, pomičući granice onoga što se nekada smatralo nemogućim. Generativni AI modeli imaju nekoliko sposobnosti i primjena, ali za ovaj kurikulum istražit ćemo kako revolucionišu obrazovanje putem izmišljenog startupa. Nazvat ćemo ovaj startup _naš startup_. Naš startup djeluje u obrazovnom domenu s ambicioznim misijskim ciljem

> _poboljšanja pristupačnosti u učenju, na globalnoj razini, osiguravajući ravnopravan pristup obrazovanju i pružajući personalizirane iskustva učenja svakom učeniku, prema njihovim potrebama_.

Naš startup tim je svjestan da nećemo moći postići ovaj cilj bez korištenja jednog od najmoćnijih alata modernog doba – Velikih Jezičnih Modela (LLM).

Očekuje se da će generativna AI revolucionirati način na koji danas učimo i podučavamo, s učenicima koji imaju na raspolaganju virtualne učitelje 24 sata dnevno koji pružaju velike količine informacija i primjera, a učitelji mogu koristiti inovativne alate za procjenu svojih učenika i davanje povratnih informacija.

Za početak, definirajmo neke osnovne pojmove i terminologiju koju ćemo koristiti kroz kurikulum.

## Kako smo dobili Generativnu AI?

Unatoč izvanrednom _hypeu_ stvorenom nedavno najavom generativnih AI modela, ova tehnologija se razvija desetljećima, s prvim istraživačkim naporima koji datiraju iz 60-ih godina. Sada smo na točki kada AI ima ljudske kognitivne sposobnosti, poput razgovora, kao što pokazuje, na primjer, [OpenAI ChatGPT](https://openai.com/chatgpt) ili [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), koji također koristi GPT model za Bing razgovore pretraživanja weba.

Vratimo se malo unatrag, prvi prototipi AI sastojali su se od tipkanih chatbotova, koji su se oslanjali na bazu znanja izvučenu iz grupe stručnjaka i predstavljenu u računalu. Odgovori u bazi znanja bili su aktivirani ključnim riječima koje se pojavljuju u ulaznom tekstu.
Međutim, ubrzo je postalo jasno da takav pristup, koristeći tipkane chatbotove, nije dobro skalirao.

### Statistički pristup AI: Strojno učenje

Prekretnica je stigla tijekom 90-ih, s primjenom statističkog pristupa analizi teksta. To je dovelo do razvoja novih algoritama – poznatih kao strojno učenje – sposobnih za učenje obrazaca iz podataka bez eksplicitnog programiranja. Ovaj pristup omogućuje strojevima simuliranje ljudskog razumijevanja jezika: statistički model se trenira na parovima tekst-oznaka, omogućujući modelu klasifikaciju nepoznatog ulaznog teksta s unaprijed definiranim oznakom koja predstavlja namjeru poruke.

### Neuronske mreže i moderni virtualni asistenti

Posljednjih godina, tehnološka evolucija hardvera, sposobnog za rukovanje većim količinama podataka i složenijim proračunima, potaknula je istraživanja u AI, dovodeći do razvoja naprednih algoritama strojnog učenja poznatih kao neuronske mreže ili algoritmi dubokog učenja.

Neuronske mreže (i posebno Rekurentne Neuronske Mreže – RNN) značajno su poboljšale obradu prirodnog jezika, omogućujući reprezentaciju značenja teksta na značajniji način, vrednujući kontekst riječi u rečenici.

Ovo je tehnologija koja je pokretala virtualne asistente rođene u prvom desetljeću novog stoljeća, vrlo sposobne u interpretaciji ljudskog jezika, identifikaciji potrebe i izvršavanju radnje kako bi je zadovoljila – poput odgovaranja unaprijed definiranim skriptama ili korištenja usluge treće strane.

### Današnje generativne AI

Tako smo došli do današnje generativne AI, koja se može promatrati kao podskup dubokog učenja.

Nakon desetljeća istraživanja na polju AI, nova arhitektura modela – nazvana _Transformer_ – prevladala je ograničenja RNN-a, sposobna primiti mnogo duže sekvence teksta kao ulaz. Transformeri se temelje na mehanizmu pažnje, omogućujući modelu da daje različite težine ulazima koje prima, 'posvećujući više pažnje' tamo gdje je koncentrirana najrelevantnija informacija, bez obzira na njihov redoslijed u sekvenci teksta.

Većina nedavnih generativnih AI modela – također poznatih kao Veliki Jezični Modeli (LLM), budući da rade s tekstualnim ulazima i izlazima – doista se temelje na ovoj arhitekturi. Ono što je zanimljivo kod ovih modela – treniranih na ogromnoj količini nepovezanih podataka iz različitih izvora poput knjiga, članaka i web stranica – je to što se mogu prilagoditi širokom spektru zadataka i generirati gramatički ispravan tekst s prividom kreativnosti. Dakle, ne samo da su nevjerojatno poboljšali sposobnost stroja da 'razumije' ulazni tekst, već su omogućili njihovu sposobnost generiranja originalnog odgovora na ljudskom jeziku.

## Kako rade veliki jezični modeli?

U sljedećem poglavlju istražit ćemo različite vrste generativnih AI modela, ali za sada pogledajmo kako rade veliki jezični modeli, s fokusom na OpenAI GPT (Generativni Pre-trenirani Transformer) modele.

- **Tokenizer, tekst u brojeve**: Veliki Jezični Modeli primaju tekst kao ulaz i generiraju tekst kao izlaz. Međutim, budući da su statistički modeli, mnogo bolje rade s brojevima nego s tekstualnim sekvencama. Zato se svaki ulaz u model obrađuje pomoću tokenizatora prije nego što ga koristi osnovni model. Token je dio teksta – koji se sastoji od varijabilnog broja znakova, pa je glavna zadaća tokenizatora podijeliti ulaz u niz tokena. Zatim se svaki token mapira s indeksom tokena, koji je cjelobrojno kodiranje izvornog dijela teksta.

- **Predviđanje izlaznih tokena**: S obzirom na n tokena kao ulaz (s maksimalnim n koji varira od jednog modela do drugog), model je sposoban predvidjeti jedan token kao izlaz. Ovaj token se zatim uključuje u ulaz sljedeće iteracije, u obrascu proširujućeg prozora, omogućujući bolje korisničko iskustvo dobivanja jedne (ili više) rečenice kao odgovora. To objašnjava zašto, ako ste ikada igrali s ChatGPT-om, možda ste primijetili da ponekad izgleda kao da se zaustavlja usred rečenice.

- **Proces odabira, distribucija vjerojatnosti**: Izlazni token bira model prema svojoj vjerojatnosti pojavljivanja nakon trenutne sekvence teksta. To je zato što model predviđa distribuciju vjerojatnosti svih mogućih 'sljedećih tokena', izračunatu na temelju svog treninga. Međutim, nije uvijek token s najvećom vjerojatnošću odabran iz rezultirajuće distribucije. Stupanj slučajnosti dodaje se ovom izboru, na način da model djeluje na nedeterministički način - ne dobivamo potpuno isti izlaz za isti ulaz. Ovaj stupanj slučajnosti dodaje se kako bi se simulirao proces kreativnog razmišljanja i može se podesiti pomoću parametra modela nazvanog temperatura.

## Kako naš startup može iskoristiti Velike Jezične Modele?

Sada kada imamo bolje razumijevanje unutarnjeg rada velikog jezičnog modela, pogledajmo neke praktične primjere najčešćih zadataka koje oni mogu obavljati prilično dobro, s obzirom na naš poslovni scenarij.
Rekli smo da je glavna sposobnost Velikog Jezičnog Modela _generiranje teksta od nule, počevši od tekstualnog ulaza, napisanog prirodnim jezikom_.

Ali kakav tekstualni ulaz i izlaz?
Ulaz velikog jezičnog modela poznat je kao upit, dok je izlaz poznat kao dovršenje, pojam koji se odnosi na mehanizam modela za generiranje sljedećeg tokena za dovršavanje trenutnog ulaza. Uronit ćemo duboko u ono što je upit i kako ga dizajnirati na način da izvučemo najviše iz našeg modela. Ali za sada, recimo samo da upit može uključivati:

- **Instrukciju** koja specificira vrstu izlaza koju očekujemo od modela. Ova instrukcija ponekad može sadržavati neke primjere ili dodatne podatke.

  1. Sažetak članka, knjige, recenzija proizvoda i više, uz izvlačenje uvida iz nestrukturiranih podataka.
  
  2. Kreativno osmišljavanje i dizajn članka, eseja, zadatka ili više.

- **Pitanje**, postavljeno u obliku razgovora s agentom.

- Dio **teksta za dovršavanje**, koji implicitno predstavlja zahtjev za pomoć pri pisanju.

- Dio **koda** zajedno sa zahtjevom za objašnjenje i dokumentiranje ili komentar koji traži generiranje dijela koda koji obavlja određeni zadatak.

Gore navedeni primjeri su prilično jednostavni i nisu namijenjeni da budu iscrpna demonstracija sposobnosti Velikih Jezičnih Modela. Oni su namijenjeni pokazivanju potencijala korištenja generativne AI, posebno ali ne ograničavajući se na obrazovne kontekste.

Također, izlaz generativnog AI modela nije savršen i ponekad kreativnost modela može djelovati protiv njega, rezultirajući izlazom koji je kombinacija riječi koje ljudski korisnik može protumačiti kao mistifikaciju stvarnosti ili može biti uvredljiv. Generativna AI nije inteligentna - barem u sveobuhvatnijoj definiciji inteligencije, uključujući kritičko i kreativno razmišljanje ili emocionalnu inteligenciju; nije deterministička i nije pouzdana, budući da se izmišljotine, poput pogrešnih referenci, sadržaja i izjava, mogu kombinirati s točnim informacijama i predstaviti na uvjerljiv i samouvjeren način. U sljedećim lekcijama bavit ćemo se svim ovim ograničenjima i vidjeti što možemo učiniti da ih ublažimo.

## Zadatak

Vaš zadatak je da pročitate više o [generativnoj AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i pokušate identificirati područje u kojem biste danas dodali generativnu AI, a da je trenutno nema. Kako bi se utjecaj razlikovao od obavljanja na "stari način", možete li učiniti nešto što prije niste mogli, ili ste brži? Napišite sažetak od 300 riječi o tome kako bi izgledao vaš startup iz snova u području AI i uključite naslove poput "Problem", "Kako bih koristio AI", "Utjecaj" i opcionalno poslovni plan.

Ako ste izvršili ovaj zadatak, možda ste čak spremni prijaviti se u Microsoftov inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) gdje nudimo kredite za Azure, OpenAI, mentorstvo i mnogo više, provjerite!

## Provjera znanja

Što je točno o velikim jezičnim modelima?

1. Dobivate potpuno isti odgovor svaki put.
1. Radi stvari savršeno, izvrsno dodaje brojeve, proizvodi radni kod itd.
1. Odgovor može varirati unatoč korištenju istog upita. Također je izvrstan za pružanje prvog nacrta nečega, bilo da je tekst ili kod. Ali trebate poboljšati rezultate.

A: 3, LLM je nedeterministički, odgovor varira, međutim, možete kontrolirati njegovu varijancu putem postavke temperature. Također ne biste trebali očekivati da radi stvari savršeno, tu je da obavi teži dio posla za vas, što često znači da dobivate dobar prvi pokušaj nečega što trebate postupno poboljšati.

## Odličan posao! Nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili povećavati svoje znanje o Generativnoj AI!

Prijeđite na Lekciju 2 gdje ćemo istražiti kako [istražiti i usporediti različite vrste LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Odricanje odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.