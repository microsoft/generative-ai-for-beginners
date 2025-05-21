<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:44:44+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sr"
}
-->
# Generacija uz podršku pretraživanja (RAG) i vektorske baze podataka

U lekciji o aplikacijama za pretragu, ukratko smo naučili kako da integrišemo vaše sopstvene podatke u velike jezičke modele (LLM). U ovoj lekciji, detaljnije ćemo istražiti koncepte utemeljenja vaših podataka u vašoj LLM aplikaciji, mehanizme procesa i metode za skladištenje podataka, uključujući i ugradnje i tekst.

## Uvod

U ovoj lekciji pokrićemo sledeće:

- Uvod u RAG, šta je to i zašto se koristi u veštačkoj inteligenciji (AI).

- Razumevanje šta su vektorske baze podataka i kreiranje jedne za našu aplikaciju.

- Praktičan primer kako integrisati RAG u aplikaciju.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete da:

- Objasnite značaj RAG-a u preuzimanju i obradi podataka.

- Postavite RAG aplikaciju i utemeljite vaše podatke na LLM-u

- Efikasna integracija RAG-a i vektorskih baza podataka u LLM aplikacijama.

## Naš scenario: unapređenje naših LLM-ova sa našim sopstvenim podacima

Za ovu lekciju, želimo da dodamo naše sopstvene beleške u edukativni startap, koji omogućava chatbotu da dobije više informacija o različitim temama. Koristeći beleške koje imamo, učenici će moći bolje da uče i razumeju različite teme, olakšavajući im pripremu za ispite. Da bismo kreirali naš scenario, koristićemo:

- `Azure OpenAI:` LLM koji ćemo koristiti da kreiramo naš chatbot

- `AI for beginners' lesson on Neural Networks`: ovo će biti podaci na kojima ćemo utemeljiti naš LLM

- `Azure AI Search` i `Azure Cosmos DB:` vektorsku bazu podataka za skladištenje naših podataka i kreiranje indeksa pretrage

Korisnici će moći da kreiraju kvizove za vežbanje iz svojih beleški, kartice za reviziju i sažmu ih u koncizne preglede. Da bismo počeli, pogledajmo šta je RAG i kako funkcioniše:

## Generacija uz podršku pretraživanja (RAG)

Chatbot pokretan LLM-om obrađuje korisničke zahteve da generiše odgovore. Dizajniran je da bude interaktivan i angažuje se sa korisnicima na širokom spektru tema. Međutim, njegovi odgovori su ograničeni kontekstom koji mu je dat i njegovim osnovnim podacima za obuku. Na primer, GPT-4 prekid znanja je septembar 2021, što znači da mu nedostaje znanje o događajima koji su se dogodili nakon ovog perioda. Osim toga, podaci korišćeni za obuku LLM-ova isključuju poverljive informacije kao što su lične beleške ili priručnik za proizvode kompanije.

### Kako RAG-ovi (Generacija uz podršku pretraživanja) funkcionišu

Pretpostavimo da želite da postavite chatbot koji kreira kvizove iz vaših beleški, biće vam potrebna veza sa bazom znanja. Tu dolazi RAG. RAG-ovi funkcionišu na sledeći način:

- **Baza znanja:** Pre preuzimanja, ovi dokumenti moraju biti uneti i prethodno obrađeni, obično razbijajući velike dokumente u manje delove, pretvarajući ih u tekstualne ugradnje i skladišteći ih u bazi podataka.

- **Korisnički upit:** korisnik postavlja pitanje

- **Preuzimanje:** Kada korisnik postavi pitanje, model za ugradnju preuzima relevantne informacije iz naše baze znanja da pruži više konteksta koji će biti uključen u zahtev.

- **Generacija uz podršku:** LLM poboljšava svoj odgovor na osnovu preuzetih podataka. Omogućava da generisani odgovor bude ne samo zasnovan na prethodno obučenim podacima već i na relevantnim informacijama iz dodatog konteksta. Preuzeti podaci se koriste za poboljšanje odgovora LLM-a. LLM zatim vraća odgovor na korisničko pitanje.

Arhitektura za RAG-ove se implementira korišćenjem transformatora koji se sastoje iz dva dela: kodera i dekodera. Na primer, kada korisnik postavi pitanje, ulazni tekst se 'kodira' u vektore koji hvataju značenje reči, a vektori se 'dekodiraju' u naš indeks dokumenata i generišu novi tekst na osnovu korisničkog upita. LLM koristi model kodera-dekodera da generiše izlaz.

Dva pristupa pri implementaciji RAG-a prema predloženom radu: [Generacija uz podršku pretraživanja za zadatke NLP-a (softver za obradu prirodnog jezika) koji intenzivno koriste znanje](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) su:

- **_RAG-Sekvenca_** koristeći preuzete dokumente da predvidi najbolji mogući odgovor na korisnički upit

- **RAG-Tok** koristeći dokumente da generiše sledeći tok, zatim ih preuzme da odgovori na korisnički upit

### Zašto biste koristili RAG-ove? 

- **Bogatsvo informacija:** osigurava da tekstualni odgovori budu ažurirani i aktuelni. Stoga poboljšava performanse na zadacima specifičnim za domen pristupom unutrašnjoj bazi znanja.

- Smanjuje fabrikaciju korišćenjem **proverljivih podataka** u bazi znanja da pruži kontekst korisničkim upitima.

- **Ekonomičan je** jer su ekonomičniji u poređenju sa finim podešavanjem LLM-a.

## Kreiranje baze znanja

Naša aplikacija se zasniva na našim ličnim podacima tj. lekciji o neuronskim mrežama u kurikulumu AI za početnike.

### Vektorske baze podataka

Vektorska baza podataka, za razliku od tradicionalnih baza podataka, je specijalizovana baza podataka dizajnirana da skladišti, upravlja i pretražuje ugrađene vektore. Skladišti numeričke reprezentacije dokumenata. Razbijanje podataka na numeričke ugradnje olakšava našem AI sistemu da razume i obradi podatke.

Skladištimo naše ugradnje u vektorskim bazama podataka jer LLM-ovi imaju ograničenje broja tokena koje prihvataju kao ulaz. Kako ne možete proslediti sve ugradnje LLM-u, moraćemo da ih razbijemo na delove i kada korisnik postavi pitanje, ugradnje koje su najbliže pitanju će biti vraćene zajedno sa zahtevom. Razbijanje takođe smanjuje troškove broja tokena koji se prosleđuju kroz LLM.

Neke popularne vektorske baze podataka uključuju Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Možete kreirati model Azure Cosmos DB koristeći Azure CLI sa sledećom komandom:

### Od teksta do ugradnji

Pre nego što skladištimo naše podatke, moramo ih pretvoriti u vektorske ugradnje pre nego što budu skladišteni u bazi podataka. Ako radite sa velikim dokumentima ili dugim tekstovima, možete ih razbiti na osnovu upita koje očekujete. Razbijanje se može uraditi na nivou rečenice ili na nivou paragrafa. Kako razbijanje izvodi značenja iz reči oko njih, možete dodati neki drugi kontekst delu, na primer, dodavanjem naslova dokumenta ili uključivanjem nekog teksta pre ili posle dela. Možete razbiti podatke na sledeći način:

Jednom kada su razbijeni, možemo zatim ugraditi naš tekst koristeći različite modele za ugradnju. Neki modeli koje možete koristiti uključuju: word2vec, ada-002 od OpenAI, Azure Computer Vision i mnoge druge. Odabir modela za korišćenje zavisiće od jezika koje koristite, tipa sadržaja koji se kodira (tekst/slike/audio), veličine ulaza koji može kodirati i dužine izlaza ugradnje.

Primer ugrađenog teksta koristeći OpenAI-ov model `text-embedding-ada-002` je:

## Preuzimanje i vektorska pretraga

Kada korisnik postavi pitanje, preuzimač ga transformiše u vektor koristeći kodera upita, zatim pretražuje kroz naš indeks pretrage dokumenata za relevantne vektore u dokumentu koji su povezani sa ulazom. Kada završi, konvertuje i ulazni vektor i vektore dokumenata u tekst i prosleđuje ih kroz LLM.

### Preuzimanje

Preuzimanje se dešava kada sistem pokušava brzo da pronađe dokumente iz indeksa koji zadovoljavaju kriterijume pretrage. Cilj preuzimača je da dobije dokumente koji će se koristiti za pružanje konteksta i utemeljenje LLM-a na vašim podacima.

Postoji nekoliko načina za obavljanje pretrage unutar naše baze podataka kao što su:

- **Pretraga po ključnim rečima** - koristi se za tekstualne pretrage

- **Semantička pretraga** - koristi semantičko značenje reči

- **Vektorska pretraga** - konvertuje dokumente iz teksta u vektorske reprezentacije koristeći modele za ugradnju. Preuzimanje će se obaviti upitom dokumenata čije su vektorske reprezentacije najbliže korisničkom pitanju.

- **Hibridna** - kombinacija pretrage po ključnim rečima i vektorske pretrage.

Izazov sa preuzimanjem dolazi kada nema sličnog odgovora na upit u bazi podataka, sistem će tada vratiti najbolje informacije koje može dobiti, međutim, možete koristiti taktike kao što je postavljanje maksimalne udaljenosti za relevantnost ili korišćenje hibridne pretrage koja kombinuje i ključne reči i vektorsku pretragu. U ovoj lekciji ćemo koristiti hibridnu pretragu, kombinaciju vektorske i pretrage po ključnim rečima. Skladištićemo naše podatke u okvir podataka sa kolonama koje sadrže delove kao i ugradnje.

### Vektorska sličnost

Preuzimač će pretraživati kroz bazu znanja za ugradnje koje su blizu jedna drugoj, najbliži sused, jer su to tekstovi koji su slični. U slučaju da korisnik postavi upit, prvo se ugrađuje, zatim se poklapa sa sličnim ugradnjama. Zajednička mera koja se koristi da se utvrdi koliko su slični različiti vektori je kosinusna sličnost koja se zasniva na uglu između dva vektora.

Možemo meriti sličnost koristeći druge alternative koje možemo koristiti su Euklidska udaljenost koja je prava linija između krajnjih tačaka vektora i skalarni proizvod koji meri zbir proizvoda odgovarajućih elemenata dva vektora.

### Indeks pretrage

Kada radimo preuzimanje, moraćemo da izgradimo indeks pretrage za našu bazu znanja pre nego što obavimo pretragu. Indeks će skladištiti naše ugradnje i može brzo preuzeti najsličnije delove čak i u velikoj bazi podataka. Možemo kreirati naš indeks lokalno koristeći:

### Ponovno rangiranje

Kada ste upitali bazu podataka, možda ćete morati da sortirate rezultate od najrelevantnijih. LLM za ponovno rangiranje koristi mašinsko učenje da poboljša relevantnost rezultata pretrage tako što ih poređa od najrelevantnijih. Koristeći Azure AI pretragu, ponovno rangiranje se automatski obavlja za vas koristeći semantičko ponovno rangiranje. Primer kako ponovno rangiranje funkcioniše koristeći najbliže susede:

## Sve zajedno

Poslednji korak je dodavanje našeg LLM-a u kombinaciju da bismo mogli da dobijemo odgovore koji su utemeljeni na našim podacima. Možemo ga implementirati na sledeći način:

## Evaluacija naše aplikacije

### Metodologija evaluacije

- Kvalitet odgovora koji se isporučuju osiguravajući da zvuče prirodno, tečno i kao ljudski

- Utemeljenost podataka: evaluacija da li je odgovor došao iz dostavljenih dokumenata

- Relevantnost: evaluacija da li odgovor odgovara i da li je povezan sa postavljenim pitanjem

- Tečnost - da li odgovor ima smisla gramatički

## Upotrebe za korišćenje RAG-a (Generacija uz podršku pretraživanja) i vektorskih baza podataka

Postoji mnogo različitih upotreba gde pozivi funkcija mogu poboljšati vašu aplikaciju kao što su:

- Postavljanje pitanja i odgovaranje: utemeljenje podataka vaše kompanije na chat koji zaposleni mogu koristiti za postavljanje pitanja.

- Sistemi preporuka: gde možete kreirati sistem koji poklapa najsličnije vrednosti npr. filmove, restorane i mnoge druge.

- Usluge chatbota: možete skladištiti istoriju chatova i personalizovati razgovor na osnovu korisničkih podataka.

- Pretraga slika zasnovana na vektorskim ugradnjama, korisna kada radite prepoznavanje slika i otkrivanje anomalija.

## Rezime

Pokrićemo osnovne oblasti RAG-a od dodavanja naših podataka u aplikaciju, korisničkog upita i izlaza. Da biste pojednostavili kreiranje RAG-a, možete koristiti okvire kao što su Semanti Kernel, Langchain ili Autogen.

## Zadaci

Da nastavite vaše učenje Generacije uz podršku pretraživanja (RAG) možete izgraditi:

- Izgradite front-end za aplikaciju koristeći okvir po vašem izboru

- Iskoristite okvir, bilo LangChain ili Semantic Kernel, i ponovo kreirajte vašu aplikaciju.

Čestitamo na završetku lekcije 👏.

## Učenje ne prestaje ovde, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite sa unapređenjem vašeg znanja o generativnoj AI!

**Одрекување од одговорност**:  
Овој документ е преведен користејќи услуга за AI превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудиме за точност, ве молиме имајте предвид дека автоматските преводи може да содржат грешки или неточности. Оригиналниот документ на неговиот изворен јазик треба да се смета за авторитетен извор. За критични информации, се препорачува професионален човечки превод. Не сме одговорни за никакви недоразбирања или погрешни толкувања кои произлегуваат од користењето на овој превод.