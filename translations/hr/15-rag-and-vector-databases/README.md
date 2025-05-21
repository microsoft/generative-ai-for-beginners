<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:45:25+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "hr"
}
-->
# Generiranje uz pomoć pretraživanja (RAG) i vektorske baze podataka

U lekciji o aplikacijama za pretraživanje, ukratko smo naučili kako integrirati vlastite podatke u velike jezične modele (LLM). U ovoj lekciji ćemo detaljnije istražiti koncepte uzemljenja vaših podataka u vašoj LLM aplikaciji, mehaniku procesa i metode za pohranu podataka, uključujući i ugrađene i tekstualne podatke.

## Uvod

U ovoj lekciji obradit ćemo sljedeće:

- Uvod u RAG, što je to i zašto se koristi u AI (umjetnoj inteligenciji).

- Razumijevanje što su vektorske baze podataka i stvaranje jedne za našu aplikaciju.

- Praktični primjer kako integrirati RAG u aplikaciju.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Objasniti značaj RAG-a u pretraživanju i obradi podataka.

- Postaviti RAG aplikaciju i uzemljiti svoje podatke na LLM.

- Učinkovita integracija RAG-a i vektorskih baza podataka u LLM aplikacije.

## Naš scenarij: poboljšanje naših LLM-a s vlastitim podacima

Za ovu lekciju želimo dodati vlastite bilješke u edukativni startup, koji omogućuje chatbotu da dobije više informacija o različitim predmetima. Koristeći bilješke koje imamo, učenici će moći bolje učiti i razumjeti različite teme, što će im olakšati pripremu za ispite. Da bismo kreirali naš scenarij, koristit ćemo:

- `Azure OpenAI:` LLM koji ćemo koristiti za kreiranje našeg chatbota

- `AI for beginners' lesson on Neural Networks`: ovo će biti podaci na koje uzemljujemo naš LLM

- `Azure AI Search` i `Azure Cosmos DB:` vektorska baza podataka za pohranu naših podataka i kreiranje indeksa pretraživanja

Korisnici će moći kreirati vježbovne kvizove iz svojih bilješki, kartice za ponavljanje i sažeti ih u koncizne preglede. Da bismo započeli, pogledajmo što je RAG i kako funkcionira:

## Generiranje uz pomoć pretraživanja (RAG)

Chatbot pokretan LLM-om obrađuje korisničke upite kako bi generirao odgovore. Dizajniran je da bude interaktivan i komunicira s korisnicima o širokom rasponu tema. Međutim, njegovi odgovori su ograničeni na kontekst koji je pružen i osnovne podatke za treniranje. Na primjer, GPT-4 ima prekid znanja u rujnu 2021., što znači da nema znanja o događajima koji su se dogodili nakon tog razdoblja. Osim toga, podaci korišteni za treniranje LLM-ova isključuju povjerljive informacije kao što su osobne bilješke ili priručnik za proizvode tvrtke.

### Kako RAG-ovi (Generiranje uz pomoć pretraživanja) rade

Pretpostavimo da želite implementirati chatbot koji kreira kvizove iz vaših bilješki, trebat će vam veza s bazom znanja. Tu RAG dolazi u pomoć. RAG-ovi djeluju na sljedeći način:

- **Baza znanja:** Prije pretraživanja, ovi dokumenti moraju biti uneseni i prethodno obrađeni, obično razbijajući velike dokumente u manje dijelove, transformirajući ih u tekstualne ugradnje i pohranjujući ih u bazu podataka.

- **Upit korisnika:** korisnik postavlja pitanje

- **Pretraživanje:** Kada korisnik postavi pitanje, model ugradnje pretražuje relevantne informacije iz naše baze znanja kako bi pružio više konteksta koji će biti uključen u upit.

- **Generiranje uz pomoć pretraživanja:** LLM poboljšava svoj odgovor na temelju pretraženih podataka. Omogućuje da generirani odgovor bude ne samo temeljen na prethodno treniranim podacima već i relevantnim informacijama iz dodanog konteksta. Pretraženi podaci koriste se za poboljšanje odgovora LLM-a. LLM tada vraća odgovor na korisničko pitanje.

Arhitektura za RAG-ove se implementira pomoću transformatora koji se sastoje od dva dijela: kodera i dekodera. Na primjer, kada korisnik postavi pitanje, ulazni tekst se 'kodira' u vektore koji hvataju značenje riječi, a vektori se 'dekodiraju' u naš indeks dokumenata i generiraju novi tekst temeljen na korisničkom upitu. LLM koristi model kodera-dekodera za generiranje izlaza.

Dva pristupa pri implementaciji RAG-a prema predloženom radu: [Generiranje uz pomoć pretraživanja za zadatke intenzivne obrade znanja u NLP-u (softver za obradu prirodnog jezika)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) su:

- **_RAG-Sequence_** koristeći pretražene dokumente za predviđanje najboljeg mogućeg odgovora na korisnički upit

- **RAG-Token** koristeći dokumente za generiranje sljedećeg tokena, zatim ih pretražuje kako bi odgovorio na korisnički upit

### Zašto biste koristili RAG-ove?

- **Bogatstvo informacija:** osigurava da tekstualni odgovori budu ažurirani i aktualni. Stoga poboljšava izvedbu na zadacima specifičnim za domenu pristupajući unutarnjoj bazi znanja.

- Smanjuje izmišljanje koristeći **provjerljive podatke** u bazi znanja kako bi pružio kontekst korisničkim upitima.

- **Isplativo je** jer su ekonomičniji u usporedbi s finim podešavanjem LLM-a.

## Stvaranje baze znanja

Naša aplikacija temelji se na našim osobnim podacima tj. lekciji o neuronskim mrežama u kurikulumu AI za početnike.

### Vektorske baze podataka

Vektorska baza podataka, za razliku od tradicionalnih baza podataka, je specijalizirana baza podataka dizajnirana za pohranu, upravljanje i pretraživanje ugrađenih vektora. Pohranjuje numeričke reprezentacije dokumenata. Razbijanje podataka na numeričke ugradnje olakšava našem AI sustavu razumijevanje i obradu podataka.

Pohranjujemo naše ugradnje u vektorske baze podataka jer LLM-ovi imaju ograničenje broja tokena koje prihvaćaju kao ulaz. Kako ne možete prenijeti cijele ugradnje u LLM, morat ćemo ih razbiti na dijelove i kada korisnik postavi pitanje, ugradnje koje su najviše slične pitanju bit će vraćene zajedno s upitom. Razbijanje također smanjuje troškove broja tokena koji prolaze kroz LLM.

Neke popularne vektorske baze podataka uključuju Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Možete kreirati model Azure Cosmos DB pomoću Azure CLI s sljedećom naredbom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od teksta do ugradnji

Prije nego pohranimo naše podatke, morat ćemo ih pretvoriti u vektorske ugradnje prije nego što ih pohranimo u bazu podataka. Ako radite s velikim dokumentima ili dugim tekstovima, možete ih razbiti na temelju upita koje očekujete. Razbijanje se može obaviti na razini rečenice ili na razini paragrafa. Kako razbijanje izvodi značenja iz riječi oko njih, možete dodati neki drugi kontekst dijelu, na primjer, dodavanjem naslova dokumenta ili uključivanjem nekog teksta prije ili poslije dijela. Možete razbiti podatke na sljedeći način:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Jednom kada su razbijeni, možemo zatim ugraditi naš tekst koristeći različite modele ugradnje. Neki modeli koje možete koristiti uključuju: word2vec, ada-002 od OpenAI, Azure Computer Vision i mnoge druge. Odabir modela koji ćete koristiti ovisit će o jezicima koje koristite, vrsti sadržaja koji se kodira (tekst/slike/audio), veličini ulaza koji može kodirati i duljini izlaza ugradnje.

Primjer ugrađenog teksta koristeći OpenAI-jev model `text-embedding-ada-002` je:

## Pretraživanje i vektorsko pretraživanje

Kada korisnik postavi pitanje, retriver ga transformira u vektor koristeći kodera upita, zatim pretražuje kroz naš indeks pretraživanja dokumenata za relevantne vektore u dokumentu koji su povezani s ulazom. Kada je gotovo, pretvara i ulazni vektor i vektore dokumenata u tekst i prosljeđuje ga kroz LLM.

### Pretraživanje

Pretraživanje se događa kada sustav pokušava brzo pronaći dokumente iz indeksa koji zadovoljavaju kriterije pretraživanja. Cilj retrivera je dobiti dokumente koji će se koristiti za pružanje konteksta i uzemljenje LLM-a na vašim podacima.

Postoji nekoliko načina za izvođenje pretraživanja unutar naše baze podataka kao što su:

- **Pretraživanje po ključnim riječima** - koristi se za tekstualna pretraživanja

- **Semantičko pretraživanje** - koristi semantičko značenje riječi

- **Vektorsko pretraživanje** - pretvara dokumente iz teksta u vektorske reprezentacije koristeći modele ugradnje. Pretraživanje će se obaviti upitom dokumenta čije su vektorske reprezentacije najbliže korisničkom pitanju.

- **Hibridno** - kombinacija pretraživanja po ključnim riječima i vektorskog pretraživanja.

Izazov s pretraživanjem dolazi kada nema sličnog odgovora na upit u bazi podataka, sustav će tada vratiti najbolje informacije koje mogu dobiti, međutim, možete koristiti taktike kao što su postavljanje maksimalne udaljenosti za relevantnost ili korištenje hibridnog pretraživanja koje kombinira i ključne riječi i vektorsko pretraživanje. U ovoj lekciji ćemo koristiti hibridno pretraživanje, kombinaciju vektorskog i pretraživanja po ključnim riječima. Pohranit ćemo naše podatke u dataframe s stupcima koji sadrže dijelove kao i ugradnje.

### Vektorska sličnost

Retriver će pretraživati kroz bazu znanja za ugradnje koje su blizu jedna drugoj, najbliži susjed, jer su tekstovi slični. U scenariju kada korisnik postavi upit, prvo se ugrađuje, zatim se podudara sa sličnim ugradnjama. Uobičajeno mjerenje koje se koristi za pronalaženje koliko su različiti vektori slični je kosinusna sličnost koja se temelji na kutu između dvaju vektora.

Možemo mjeriti sličnost koristeći druge alternative koje možemo koristiti su euklidska udaljenost koja je ravna linija između krajnjih točaka vektora i skalarni produkt koji mjeri zbroj proizvoda odgovarajućih elemenata dvaju vektora.

### Indeks pretraživanja

Kada radimo pretraživanje, trebat ćemo izgraditi indeks pretraživanja za našu bazu znanja prije nego što obavimo pretraživanje. Indeks će pohraniti naše ugradnje i može brzo pretražiti najviše slične dijelove čak i u velikoj bazi podataka. Možemo kreirati naš indeks lokalno koristeći:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno rangiranje

Nakon što ste upitali bazu podataka, možda ćete trebati sortirati rezultate od najrelevantnijih. LLM za ponovno rangiranje koristi strojno učenje za poboljšanje relevantnosti rezultata pretraživanja rangiranjem od najrelevantnijih. Koristeći Azure AI Search, ponovno rangiranje se automatski obavlja za vas koristeći semantički ponovni rangir. Primjer kako ponovno rangiranje radi koristeći najbliže susjede:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Sve zajedno

Posljednji korak je dodavanje našeg LLM-a u mješavinu kako bismo mogli dobiti odgovore koji su uzemljeni na našim podacima. Možemo ga implementirati na sljedeći način:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Evaluacija naše aplikacije

### Evaluacijske metrike

- Kvaliteta dostavljenih odgovora osiguravajući da zvuči prirodno, tečno i ljudski

- Uzemljenost podataka: procjena je li odgovor došao iz dostavljenih dokumenata

- Relevantnost: procjena odgovora koji se podudara i odnosi se na postavljeno pitanje

- Tečnost - je li odgovor gramatički smislen

## Primjeri upotrebe za korištenje RAG-a (Generiranje uz pomoć pretraživanja) i vektorskih baza podataka

Postoji mnogo različitih primjera upotrebe gdje pozivi funkcija mogu poboljšati vašu aplikaciju kao što su:

- Postavljanje pitanja i odgovora: uzemljenje vaših podataka tvrtke na chat koji zaposlenici mogu koristiti za postavljanje pitanja.

- Sustavi preporuka: gdje možete kreirati sustav koji podudara najsličnije vrijednosti npr. filmove, restorane i mnoge druge.

- Usluge chatbota: možete pohraniti povijest chata i personalizirati razgovor na temelju korisničkih podataka.

- Pretraživanje slika temeljeno na vektorskim ugradnjama, korisno kada radite prepoznavanje slika i detekciju anomalija.

## Sažetak

Obradili smo temeljna područja RAG-a od dodavanja naših podataka u aplikaciju, korisničkog upita i izlaza. Da biste pojednostavili kreiranje RAG-a, možete koristiti okvire kao što su Semanti Kernel, Langchain ili Autogen.

## Zadatak

Da biste nastavili s učenjem Generiranja uz pomoć pretraživanja (RAG) možete izgraditi:

- Izgradite front-end za aplikaciju koristeći okvir po vašem izboru

- Iskoristite okvir, bilo LangChain ili Semanti Kernel, i rekreirajte svoju aplikaciju.

Čestitamo na završetku lekcije 👏.

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj AI!

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo ka točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.