# Generiranje s podrškom dohvaćanja (RAG) i vektorske baze podataka

[![Generiranje s podrškom dohvaćanja (RAG) i vektorske baze podataka](../../../translated_images/hr/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

U lekciji o pretraživanju ukratko smo naučili kako integrirati vlastite podatke u velike jezične modele (LLM). U ovoj lekciji ćemo detaljnije istražiti koncepte povezivanja vaših podataka u aplikaciji LLM, mehaniku procesa i metode za pohranu podataka, uključujući i ugnježđene prikaze i tekst.

> **Video uskoro**

## Uvod

U ovoj lekciji ćemo obraditi sljedeće:

- Uvod u RAG, što je i zašto se koristi u umjetnoj inteligenciji (AI).

- Razumijevanje što su vektorske baze podataka i kako stvoriti jednu za našu aplikaciju.

- Praktični primjer kako integrirati RAG u aplikaciju.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Objasniti značaj RAG-a u dohvaćanju i obradi podataka.

- Postaviti RAG aplikaciju i povezati LLM s vašim podacima

- Učinkovito integrirati RAG i vektorske baze podataka u LLM aplikacije.

## Naš scenarij: obogaćivanje naših LLM-ova vlastitim podacima

Za ovu lekciju želimo dodati vlastite bilješke u startup za obrazovanje, što chatbotu omogućuje da dobije više informacija o različitim predmetima. Koristeći bilješke koje imamo, učenici će moći bolje učiti i razumjeti različite teme, što će olakšati ponavljanje za njihove ispite. Za stvaranje našeg scenarija koristit ćemo:

- `Azure OpenAI:` LLM koji ćemo koristiti za izradu našeg chatbota

- `AI for beginners' lesson on Neural Networks`: to će biti podaci na kojima povezujemo naš LLM

- `Azure AI Search` i `Azure Cosmos DB:` vektorska baza podataka za pohranu naših podataka i izradu indeksa za pretraživanje

Korisnici će moći stvarati praktične kvizove i kartice za ponavljanje iz svojih bilješki te sažimati te bilješke u sažete pregledne tekstove. Za početak, pogledajmo što je RAG i kako funkcionira:

## Generiranje s podrškom dohvaćanja (RAG)

Chatbot pokretan LLM-om obrađuje upite korisnika kako bi generirao odgovore. Dizajniran je za interakciju i angažman s korisnicima o širokom spektru tema. Međutim, njegovi su odgovori ograničeni na kontekst koji mu je dan i na osnovne podatke za trening. Na primjer, datum prekida znanja GPT-4 modela je rujan 2021., što znači da nema znanje o događajima koji su se dogodili nakon tog razdoblja. Dodatno, podaci korišteni za treniranje LLM-a isključuju povjerljive informacije poput osobnih bilješki ili priručnika proizvoda tvrtke.

### Kako RAG (Generiranje s podrškom dohvaćanja) funkcionira

![crtež koji prikazuje kako RAG funkcionira](../../../translated_images/hr/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Pretpostavimo da želite implementirati chatbota koji stvara kvizove iz vaših bilješki; tada će vam trebati veza s bazom znanja. Tu RAG dolazi kao rješenje. RAG-ovi rade na sljedeći način:

- **Baza znanja:** Prije dohvaćanja, ti dokumenti moraju biti uneseni i unaprijed obrađeni, obično se velike dokumente razlaže u manje dijelove, pretvaraju u tekstualne ugnježđene prikaze i pohranjuju u bazu podataka.

- **Upit korisnika:** korisnik postavlja pitanje

- **Dohvaćanje:** Kad korisnik postavi pitanje, model ugnježđivanja dohvaća relevantne informacije iz naše baze znanja kako bi pružio više konteksta koji će biti uključen u upit.

- **Proširena generacija:** LLM poboljšava svoj odgovor na temelju dohvaćenih podataka. To omogućuje da generirani odgovor nije samo baziran na unaprijed treniranim podacima, već i na relevantnim informacijama iz dodanog konteksta. Dohvaćeni podaci služe za proširenje odgovora LLM-a. LLM tada vraća odgovor na korisnikovo pitanje.

![Dijagram koji prikazuje RAG arhitekturu](../../../translated_images/hr/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG kombinira dohvaćanje s generiranjem: upit se pretvara u vektor, uspoređuje s indeksom dokumenata kako bi se pronašli relevantni tekstualni dijelovi i ti se dijelovi koriste kao kontekst LLM-u koji generira odgovor. Dohvaćatelj i generator mogu koristiti različite modele; RAG ne zahtijeva enkoder-dekoder transformator.

Dva pristupa pri implementaciji RAG-a prema predloženom radu: [Retrieval-Augmented Generation for Knowledge intensive NLP (softver za obradu prirodnog jezika) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) su:

- **_RAG-Sequence_** koristi dohvaćene dokumente za predviđanje najboljeg mogućeg odgovora na korisnički upit

- **RAG-Token** koristi dokumente za generiranje sljedećeg tokena, potom ih dohvaća kako bi odgovorio na korisnikov upit

### Zašto koristiti RAG? 

- **Bogatsvo informacija:** osigurava da su tekstualni odgovori ažurni i aktualni. Time poboljšava izvedbu na specifičnim zadacima pristupom internoj bazi znanja.

- Smanjuje izmišljanje podataka koristeći **provjerljive podatke** u bazi znanja za pružanje konteksta korisničkim upitima.

- **Isplativo je** jer su ekonomičniji u odnosu na fino podešavanje velikog jezičnog modela (LLM)

## Kreiranje baze znanja

Naša aplikacija temelji se na našim osobnim podacima, tj. lekciji o neuronskim mrežama iz kurikuluma AI za početnike.

### Vektorske baze podataka

Vektorska baza podataka, za razliku od tradicionalnih baza podataka, je specijalizirana baza podataka dizajnirana za pohranu, upravljanje i pretraživanje ugrađenih vektora. Pohranjuje numeričke reprezentacije dokumenata. Razbijanjem podataka u numeričke ugradnje (embeddings) olakšava se našem AI sustavu razumijevanje i obrada podataka.

Budući da LLM-ovi imaju ograničenje na broj ulaznih tokena, dokumente razdvajamo u dijelove prije ugradnje. Kad korisnik postavi pitanje, ugrađivanja koja su najsličnija upitu identificiraju relevantne dijelove teksta koji se vraćaju s promptom. Razdvajanje na dijelove također smanjuje broj tokena proslijeđenih LLM-u i time može smanjiti troškove.

Neke popularne vektorske baze podataka uključuju Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Model Azure Cosmos DB možete kreirati pomoću Azure CLI naredbom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od teksta do ugradnji

Prije nego što pohranimo naše podatke, morat ćemo ih pretvoriti u vektorske ugradnje prije pohrane u bazu podataka. Ako radite s velikim dokumentima ili dugim tekstovima, možete ih razbiti na osnovu očekivanih upita. Razdvajanje može biti na razini rečenice ili odlomka. Kako razdvajanje izvlači značenja iz riječi oko sebe, možete dodati neki dodatni kontekst dijelu, na primjer, dodavanjem naslova dokumenta ili uključivanjem teksta prije ili poslije dijela. Podatke možete razdvojiti na sljedeći način:

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

Nakon razdvajanja, možemo ugraditi naš tekst koristeći različite modele za ugradnju. Neki modeli koje možete koristiti uključuju: word2vec, ada-002 od OpenAI, Azure Computer Vision i mnoge druge. Odabir modela ovisit će o jezicima koje koristite, vrsti sadržaja koji se kodira (tekst/slike/zvuk), veličini ulaza koji može kodirati i duljini izlaza ugradnje.

Primjer ugrađenog teksta korištenjem OpenAI-evog `text-embedding-ada-002` modela je:
![ugrađivanje riječi cat](../../../translated_images/hr/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Dohvaćanje i vektorsko pretraživanje

Kada korisnik postavi pitanje, sustav za dohvaćanje ga pretvara u vektor koristeći enkoder upita, zatim pretražuje indeks dokumenata za relevantne vektore povezane s unosom. Kad završi, pretvara i ulazni vektor i vektore iz dokumenata u tekst i prosljeđuje ih kroz LLM.

### Dohvaćanje

Dohvaćanje se događa kada sustav pokušava brzo pronaći dokumente iz indeksa koji zadovoljavaju kriterije pretraživanja. Cilj dohvaćanja jest dobiti dokumente koji će se koristiti za pružanje konteksta i utemeljenje LLM-a na vašim podacima.

Postoji nekoliko načina za izvršavanje pretraživanja unutar naše baze podataka, kao što su:

- **Pretraživanje po ključnim riječima** - koristi se za pretraživanje teksta

- **Vektorsko pretraživanje** - pretvara dokumente iz teksta u vektorske reprezentacije koristeći modele ugnježđivanja, dopuštajući **semantičko pretraživanje** koje se temelji na značenju riječi. Dohvaćanje će se izvršiti pretraživanjem dokumenata čije su vektorske reprezentacije najbliže korisničkom pitanju.

- **Hibridno** - kombinacija pretraživanja po ključnim riječima i vektorskog pretraživanja.

Izazov kod dohvaćanja nastaje kada u bazi podataka nema sličnog odgovora na upit, tada sustav vraća najbolje informacije koje može pronaći, no možete koristiti taktike poput postavljanja maksimalne udaljenosti za relevantnost ili koristiti hibridno pretraživanje koje spaja ključne riječi i vektorsko pretraživanje. U ovoj lekciji koristit ćemo hibridno pretraživanje, kombinaciju vektorskog i pretraživanja po ključnim riječima. Podatke ćemo pohraniti u dataframe s stupcima koji sadrže dijelove kao i ugnježđenja.

### Vektorska sličnost

Dohvaćanje će pretraživati bazu znanja za ugnježđenja koja su blizu jedan drugome — najbliži susjedi — jer predstavljaju slične tekstove. U ovom scenariju, kad korisnik pošalje upit, on se prvo ugnježđuje, a zatim se podudara sa sličnim ugnježđenjima. Najčešća mjera koja se koristi za usporedbu vektorske sličnosti je kosinusna sličnost, koja se temelji na kutu između dva vektora.

Druge metrike koje možemo koristiti za mjerenje sličnosti uključuju Euklidsku udaljenost, koja je prava linija između krajeva vektora, te skalarni produkt, koji mjeri zbroj proizvoda odgovarajućih elemenata u dva vektora.

### Indeks pretraživanja

Kod dohvaćanja ćemo trebati izgraditi indeks pretraživanja za naš bazu znanja prije nego što izvršimo pretraživanje. Indeks će pohraniti naša ugnježđenja i može brzo dohvatiti najsličnije dijelove čak i u velikoj bazi podataka. Indeks možemo kreirati lokalno pomoću:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno rangiranje

Nakon što ste upitali bazu podataka, možda ćete trebati sortirati rezultate od najrelevantnijih. LLM za ponovno rangiranje koristi strojno učenje kako bi poboljšao relevantnost rezultata pretraživanja tako da ih sortira od najrelevantnijih. Koristeći Azure AI Search, ponovno rangiranje se vrši automatski pomoću semantičkog rangera. Primjer kako ponovno rangiranje funkcionira koristeći najbliže susjede:

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

## Sve skupa

Posljednji korak je dodati naš LLM u cijeli proces kako bismo mogli dobivati odgovore utemeljene na našim podacima. To možemo implementirati na sljedeći način:

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

### Metrike evaluacije

- Kvaliteta pruženih odgovora osiguravajući da zvuče prirodno, tečno i kao od čovjeka

- Utemeljenost podataka: procjena je li odgovor došao iz priloženih dokumenata

- Relevantnost: procjena odgovara li odgovor i je li povezan s postavljenim pitanjem

- Tečnost - procjena gramatičkog smisla odgovora

## Primjene RAG-a (Retrieval Augmented Generation) i vektorskih baza podataka

Postoji mnogo različitih primjena gdje RAG može poboljšati vašu aplikaciju, kao što su:

- Pitanja i odgovori: utemeljiti podatke vaše tvrtke na chat koji zaposlenici mogu koristiti za postavljanje pitanja.

- Sustavi preporuka: gdje možete izraditi sustav koji pronalazi najsličnije vrijednosti npr. filmove, restorane i mnoge druge.

- Usluge chatbota: možete spremiti povijest razgovora i personalizirati razgovor na temelju korisničkih podataka.

- Pretraživanje slika na temelju vektorskih ugrađivanja, korisno za prepoznavanje slika i otkrivanje anomalija.

## Sažetak

Pokrili smo osnovna područja RAG-a od dodavanja naših podataka u aplikaciju, korisničkog upita i izlaza. Za pojednostavljenje stvaranja RAG-a, možete koristiti okvire poput Semantic Kernel, LangChain ili AutoGen.

## Zadatak

Za nastavak učenja o Retrieval Augmented Generation (RAG) možete izgraditi:

- Izradite front-end za aplikaciju koristeći okvir po vašem izboru

- Koristite okvir, bilo LangChain ili Semantic Kernel, i ponovno izradite vašu aplikaciju.

Čestitamo na dovršetku lekcije 👏.

## Učenje ovdje ne prestaje, nastavite Putovanje

Nakon dovršetka ove lekcije, pogledajte našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->