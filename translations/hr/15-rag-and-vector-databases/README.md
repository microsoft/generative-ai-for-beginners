# Generacija obogaćena pretraživanjem (RAG) i vektorske baze podataka

[![Generacija obogaćena pretraživanjem (RAG) i vektorske baze podataka](../../../translated_images/hr/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

U lekciji o aplikacijama za pretraživanje, ukratko smo naučili kako integrirati vlastite podatke u Velike jezične modele (LLM-ove). U ovoj lekciji ćemo dublje zaroniti u koncepte ukorjenjivanja vaših podataka u vašu LLM aplikaciju, mehaniku procesa i metode za spremanje podataka, uključujući i ugradnje i tekst.

> **Video uskoro**

## Uvod

U ovoj lekciji ćemo obraditi sljedeće:

- Uvod u RAG, što je to i zašto se koristi u AI (umjetnoj inteligenciji).

- Razumijevanje što su vektorske baze podataka i kako stvoriti jednu za našu aplikaciju.

- Praktični primjer kako integrirati RAG u aplikaciju.

## Ciljevi učenja

Nakon završetka ove lekcije bit ćete sposobni:

- Objasniti važnost RAG-a u dohvaćanju i obradi podataka.

- Postaviti RAG aplikaciju i ukorijeniti LLM s vašim podacima.

- Učinkovito integrirati RAG i vektorske baze podataka u LLM aplikacije.

## Naš scenarij: unapređivanje naših LLM-ova s vlastitim podacima

Za ovu lekciju želimo dodati vlastite bilješke u edukacijsku startup aplikaciju, koja omogućuje chatbotu da dobije više informacija o različitim predmetima. Koristeći bilješke koje imamo, učenici će moći bolje učiti i razumjeti različite teme, što će olakšati ponavljanje za ispite. Za izradu našeg scenarija koristit ćemo:

- `Azure OpenAI:` LLM koji ćemo koristiti za stvaranje našeg chatbota

- `AI for beginners' lesson on Neural Networks`: to će biti podaci na kojima ukorjenjujemo naš LLM

- `Azure AI Search` i `Azure Cosmos DB:` vektorska baza podataka za pohranu naših podataka i izradu indeksa pretraživanja

Korisnici će moći kreirati vježbe za praksu i kartice za ponavljanje iz svojih bilješki te sažeti te bilješke u sažete preglede. Za početak, pogledajmo što je RAG i kako funkcionira:

## Generacija obogaćena pretraživanjem (RAG)

LLM-pokretan chatbot obrađuje upite korisnika da bi generirao odgovore. Dizajniran je da bude interaktivan i komunicira s korisnicima o širokom spektru tema. Međutim, njegovi su odgovori ograničeni na kontekst dan i njegove temeljne podatke za treniranje. Na primjer, GPT-4 ima granicu znanja do rujna 2021., što znači da nema znanje o događajima koji su se dogodili nakon tog razdoblja. Osim toga, podaci korišteni za treniranje LLM-ova isključuju povjerljive informacije poput osobnih bilješki ili priručnika za proizvode tvrtke.

### Kako rade RAG-ovi (Generacija obogaćena pretraživanjem)

![crtež koji prikazuje kako RAG-ovi funkcioniraju](../../../translated_images/hr/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Pretpostavimo da želite implementirati chatbota koji stvara kvizove iz vaših bilješki, trebat će vam veza s bazom znanja. Tu RAG dolazi kao pomoć. RAG-ovi rade na sljedeći način:

- **Baza znanja:** Prije dohvaćanja, ti dokumenti trebaju biti uneseni i unaprijed obrađeni, obično razbijajući velike dokumente na manje dijelove, pretvarajući ih u tekstualne ugradnje i spremajući ih u bazu podataka.

- **Upit korisnika:** korisnik postavlja pitanje

- **Dohvaćanje:** Kada korisnik postavi pitanje, model ugradnje dohvaća relevantne informacije iz naše baze znanja kako bi pružio više konteksta koji će biti uključen u upit.

- **Obogaćena generacija:** LLM poboljšava svoj odgovor temeljem dohvaćenih podataka. To omogućuje da odgovor koji se generira nije samo temeljen na prethodno treniranim podacima, već i na relevantnim informacijama iz dodanog konteksta. Dohvaćeni se podaci koriste za obogaćivanje LLM-ovih odgovora. LLM zatim vraća odgovor na korisnikovo pitanje.

![Dijagram koji prikazuje RAG arhitekturu](../../../translated_images/hr/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG kombinira dohvaćanje s generiranjem: upit se pretvara u vektor, uspoređuje s indeksom dokumenata kako bi pronašao relevantne dijelove teksta, a ti se dijelovi daju kao kontekst LLM-u, koji generira odgovor. Dohvaćanje i generiranje mogu koristiti različite modele; RAG ne zahtijeva enkoder-dekoder transformator.

Dva pristupa pri implementaciji RAG-a prema predloženom radu: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) su:

- **_RAG-Sequence_** korištenje dohvaćenih dokumenata za predviđanje najboljeg mogućeg odgovora na korisnički upit

- **RAG-Token** korištenje dokumenata za generiranje sljedećeg tokena, zatim njihovo dohvaćanje za odgovor na korisnički upit

### Zašto biste koristili RAG? 

- **Bogatsvo informacija:** osigurava da odgovori u tekstu budu ažurirani i trenutni. Time se poboljšava izvedba na zadacima specifičnim za područje pristupom internom bazi znanja.

- Smanjuje izmišljanje činjenica korištenjem **provjerljivih podataka** u bazi znanja kako bi se korisničkim upitima pružio kontekst.

- **Isplativo je** jer je ekonomičnije u usporedbi s fino podešavanjem velikog jezičnog modela (LLM)

## Izrada baze znanja

Naša aplikacija temelji se na našim osobnim podacima, tj. lekciji o neuronskim mrežama iz kurikuluma AI za početnike.

### Vektorske baze podataka

Vektorska baza podataka, za razliku od tradicionalnih baza podataka, specijalizirana je baza podataka dizajnirana za pohranu, upravljanje i pretraživanje ugrađenih vektora. Pohranjuje numeričke reprezentacije dokumenata. Razlaganje podataka na numeričke ugradnje olakšava našem AI sustavu razumijevanje i obradu podataka.

Budući da LLM-ovi imaju ograničenje na broj ulaznih tokena, dijelimo dokumente na dijelove prije njihova ugrađivanja. Kada korisnik postavi pitanje, ugradnje najbliže upitu identificiraju relevantne dijelove teksta koji se vraćaju s upitom. Dijeljenje na dijelove također smanjuje broj tokena poslanih LLM-u i time može smanjiti troškove.

Neke popularne vektorske baze podataka uključuju Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Možete stvoriti model Azure Cosmos DB koristeći Azure CLI s sljedećom naredbom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od teksta do ugradnji

Prije nego što pohranimo naše podatke, morat ćemo ih pretvoriti u vektorske ugradnje prije nego što ih pohranimo u bazu podataka. Ako radite s velikim dokumentima ili dugim tekstovima, možete ih dijeliti na dijelove temeljem upita koje očekujete. Dijeljenje može biti na razini rečenice ili na razini paragrafa. Kako dijeljenje crpi značenje iz riječi oko njih, možete dodati dodatni kontekst dijelu, na primjer dodavanjem naslova dokumenta ili uključivanjem nekog teksta prije ili poslije dijela. Podatke možete dijeliti na sljedeći način:

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

Nakon dijeljenja, tada možemo ugraditi naš tekst koristeći različite modele za ugradnju. Neki modeli koje možete koristiti uključuju: word2vec, ada-002 tvrtke OpenAI, Azure Computer Vision i mnoge druge. Odabir modela ovisit će o jezicima koje koristite, vrsti sadržaja koji se kodira (tekst/slike/audio), veličini ulaza koji može kodirati i duljini izlaza ugradnje.

Primjer ugradnje teksta koristeći OpenAI model `text-embedding-ada-002` je:
![ugradnja riječi cat](../../../translated_images/hr/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Dohvaćanje i vektorsko pretraživanje

Kada korisnik postavi pitanje, dohvaćatelj ga pretvara u vektor korištenjem kodera upita, zatim pretražuje indeks dokumenata za relevantne vektore u dokumentu povezane s unosom. Kad završi, pretvara i ulazni vektor i vektore dokumenata u tekst i prosljeđuje ih LLM-u.

### Dohvaćanje

Dohvaćanje se događa kada sustav pokušava brzo pronaći dokumente iz indeksa koji zadovoljavaju kriterije pretraživanja. Cilj dohvaćatelja je dobiti dokumente koji će se koristiti za pružanje konteksta i ucjeljivanje LLM-a na vaše podatke.

Postoji nekoliko načina za izvođenje pretraživanja unutar naše baze podataka, kao što su:

- **Pretraživanje po ključnim riječima** - koristi se za tekstualna pretraživanja

- **Vektorsko pretraživanje** - pretvara dokumente iz teksta u vektorske reprezentacije koristeći modele za ugradnju, omogućujući **semantičko pretraživanje** koristeći značenje riječi. Dohvaćanje se izvodi upitivanjem dokumenata čije su vektorske reprezentacije najbliže korisničkom pitanju.

- **Hibridno** - kombinacija pretraživanja po ključnim riječima i vektorskog pretraživanja.

Izazov kod dohvaćanja nastaje ako nema sličnog odgovora na upit u bazi podataka, sustav će tada vratiti najbolje moguće informacije, no možete koristiti taktike poput postavljanja maksimalne udaljenosti za relevantnost ili koristiti hibridno pretraživanje koje kombinira i pretraživanje po ključnim riječima i vektorsko pretraživanje. U ovoj lekciji koristit ćemo hibridno pretraživanje, kombinaciju vektorskog i pretraživanja po ključnim riječima. Naše podatke ćemo pohraniti u dataframe s stupcima koji sadrže dijelove i ugradnje.

### Sličnost vektora

Dohvaćatelj će pretraživati bazu znanja za ugradnje koje su bliske - najbliži susjedi - jer predstavljaju slične tekstove. U ovom scenariju, kad korisnik pošalje upit, on se najprije ugradi, a zatim podudara sa sličnim ugradnjama. Najčešća mjera koja se koristi za usporedbu sličnosti vektora je kosinusna sličnost, koja se temelji na kutu između dva vektora.

Druge metrike koje možemo koristiti za mjerenje sličnosti uključuju Euklidsku udaljenost, koja je ravna linija između krajnjih točaka vektora, i skalarni produkt, koji mjeri zbroj proizvoda odgovarajućih elemenata u dva vektora.

### Indeks pretraživanja

Prilikom dohvaćanja, morat ćemo izgraditi indeks pretraživanja za našu bazu znanja prije nego što izvršimo pretraživanje. Indeks će pohraniti naše ugradnje i može brzo dohvatiti najsličnije dijelove čak i u velikoj bazi podataka. Indeks možemo kreirati lokalno koristeći:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno rangiranje

Nakon što upitate bazu podataka, možda ćete htjeti poredati rezultate od najrelevantnijih. Re-rangiranje LLM koristi strojno učenje za poboljšanje relevantnosti rezultata pretraživanja njihovim razvrstavanjem od najrelevantnijih. Koristeći Azure AI Search, ponovno rangiranje se automatski izvodi uz pomoć semantičkog re-rankera. Primjer kako ponovno rangiranje funkcionira uz najbliže susjede:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Spajanje svega

Posljednji korak je dodavanje našeg LLM-a u cijelu sliku kako bismo mogli dobiti odgovore koji su utemeljeni na našim podacima. Možemo ga implementirati na sljedeći način:

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
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use the Responses API to generate a response
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Evaluacija naše aplikacije

### Mjerne vrijednosti evaluacije

- Kvaliteta dostavljenih odgovora osiguravajući da zvuče prirodno, tečno i nalik na ljudski govor

- Utemeljenost podataka: procjena je li odgovor došao iz dostavljenih dokumenata

- Relevantnost: procjena poklapanja i povezanosti odgovora s postavljenim pitanjem

- Tečnost - procjena je li odgovor gramatički smislen

## Primjene korištenja RAG-a (Retrieval Augmented Generation) i vektorskih baza podataka

Postoji mnogo različitih primjena gdje RAG može poboljšati vašu aplikaciju, kao što su:

- Pitanja i odgovori: utemeljenje podataka vaše tvrtke u chat koji zaposlenici mogu koristiti za postavljanje pitanja.

- Sustavi preporuka: gdje možete stvoriti sustav koji pronalazi najsličnije vrijednosti npr. filmove, restorane i mnoge druge.

- Chatbot usluge: možete pohraniti povijest razgovora i personalizirati konverzaciju na temelju podataka korisnika.

- Pretraživanje slika temeljeno na vektorskim ugradnjama, korisno pri prepoznavanju slika i otkrivanju anomalija.

## Sažetak

Pokrili smo osnovna područja RAG-a od dodavanja naših podataka u aplikaciju, korisničkog upita do izlaza. Kako bi pojednostavili izradu RAG-a, možete koristiti okvire kao što su Semantic Kernel, LangChain ili AutoGen.

## Zadatak

Za nastavak učenja Retrieval Augmented Generation (RAG), možete izgraditi:

- Izraditi front-end aplikacije koristeći okvir po vašem izboru

- Iskoristiti okvir, bilo LangChain ili Semantic Kernel, i ponovno stvoriti svoju aplikaciju.

Čestitamo na dovršetku lekcije 👏.

## Učenje ovdje ne prestaje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili podizati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->