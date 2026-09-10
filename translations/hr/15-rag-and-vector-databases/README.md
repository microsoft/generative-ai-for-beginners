# Generiranje potpomognuto dohvatom (RAG) i vektorske baze podataka

[![Generiranje potpomognuto dohvatom (RAG) i vektorske baze podataka](../../../translated_images/hr/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

U lekciji o aplikacijama za pretraživanje ukratko smo naučili kako integrirati vlastite podatke u velike jezične modele (LLM). U ovoj lekciji ćemo detaljnije proučiti koncept pridruživanja vaših podataka vašoj LLM aplikaciji, mehaniku procesa i metode za pohranu podataka, uključujući kako ugradnje tako i tekst.

> **Video uskoro**

## Uvod

U ovoj lekciji pokriti ćemo sljedeće:

- Uvod u RAG, što je i zašto se koristi u AI (umjetnoj inteligenciji).

- Razumijevanje što su vektorske baze podataka i kako stvoriti jednu za našu aplikaciju.

- Praktični primjer kako integrirati RAG u aplikaciju.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Objasniti važnost RAG u dohvaćanju i obradi podataka.

- Postaviti RAG aplikaciju i pridružiti svoje podatke LLM-u

- Učinkovito integrirati RAG i vektorske baze podataka u LLM aplikacije.

## Naš scenarij: unapređenje naših LLM-ova našim vlastitim podacima

Za ovu lekciju želimo dodati vlastite bilješke u edukacijski startup, što omogućuje chatbotu da dobije više informacija o različitim predmetima. Koristeći bilješke koje imamo, učenici će moći bolje proučavati i razumjeti različite teme, čime će im biti lakše pripremiti se za ispite. Za izradu našeg scenarija koristit ćemo:

- `Azure OpenAI:` LLM koji ćemo koristiti za izradu našeg chatbota

- `Lekcija AI za početnike o neuronskim mrežama`: to će biti podaci na kojima temeljimo naš LLM

- `Azure AI Search` i `Azure Cosmos DB:` vektorska baza podataka za pohranu naših podataka i stvaranje indeksa pretraživanja

Korisnici će moći izrađivati kvizove za vježbu iz svojih bilješki, kartice za ponavljanje i sažimati ih u sažete preglede. Za početak, pogledajmo što je RAG i kako radi:

## Generiranje potpomognuto dohvatom (RAG)

Chatbot pokretan LLM-om obrađuje korisničke upite kako bi generirao odgovore. Dizajniran je da bude interaktivan i komunicira s korisnicima o širokom spektru tema. Međutim, njegovi odgovori ograničeni su na kontekst koji mu je dan i na temeljne podatke korištene u treniranju. Na primjer, GPT-4 ima ograničenje znanja do rujna 2021., što znači da nema znanja o događajima nakon tog razdoblja. Osim toga, podaci korišteni za treniranje LLM-ova isključuju povjerljive informacije kao što su osobne bilješke ili korisnički priručnici tvrtke.

### Kako RAG-ovi (Generiranje potpomognuto dohvatom) rade

![crtež koji prikazuje kako rade RAG-ovi](../../../translated_images/hr/how-rag-works.f5d0ff63942bd3a6.webp)

Pretpostavimo da želite implementirati chatbota koji stvara kvizove iz vaših bilješki, trebat će vam veza s bazom znanja. Tu RAG dolazi kao rješenje. RAG-ovi funkcioniraju kako slijedi:

- **Baza znanja:** Prije dohvaćanja, ovi se dokumenti trebaju unijeti i prethodno obraditi, obično razbijanjem velikih dokumenata na manje dijelove, pretvaranjem u tekstualne ugradnje i pohranom u bazu podataka.

- **Korisnički upit:** korisnik postavlja pitanje

- **Dohvaćanje:** Kad korisnik postavi pitanje, model ugradnje dohvaća relevantne informacije iz naše baze znanja kako bi pružio više konteksta koji će biti uključen u upit.

- **Potpomognuto generiranje:** LLM unapređuje svoj odgovor na temelju dohvaćenih podataka. To omogućuje da generirani odgovor ne bude samo na temelju prethodno obučenih podataka, već i na temelju relevantnih informacija iz dodanog konteksta. Dohvaćeni podaci koriste se za poboljšanje odgovora LLM-a. LLM zatim vraća odgovor na pitanje korisnika.

![crtež koji prikazuje arhitekturu RAG-ova](../../../translated_images/hr/encoder-decode.f2658c25d0eadee2.webp)

Arhitektura RAG-ova implementirana je pomoću transformera koji se sastoje od dva dijela: enkodera i dekodera. Na primjer, kad korisnik postavi pitanje, ulazni tekst se 'enkodira' u vektore koji hvataju značenje riječi, a vektori se 'dekodiraju' u naš indeks dokumenata i generiraju novi tekst na temelju korisničkog upita. LLM koristi model enkodera-dekodera za generiranje izlaza.

Prema predloženom radu: [Generiranje potpomognuto dohvatom za zadatke intenzivnog NLP-a (obrada prirodnog jezika)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst), postoje dva pristupa implementaciji RAG-a:

- **_RAG-Sequence_** koristi dohvaćene dokumente za predviđanje najboljeg mogućeg odgovora na korisnički upit

- **RAG-Token** koristi dokumente za generiranje sljedećeg tokena, a zatim ih dohvaća za odgovor na korisnički upit

### Zašto koristiti RAG?

- **Bogatstvo informacija:** osigurava da su tekstualni odgovori ažurni i aktualni. Time se poboljšava izvedba u zadacima specifičnim za određeno područje pristupanjem internoj bazi znanja.

- Smanjuje izmišljotine korištenjem **provjerivih podataka** u bazi znanja kao konteksta za korisničke upite.

- **Isplativo** je jer je ekonomičnije od podešavanja LLM-a (fine-tuning).

## Izrada baze znanja

Naša aplikacija bazira se na našim osobnim podacima, odnosno lekciji o neuronskim mrežama iz kurikuluma AI za početnike.

### Vektorske baze podataka

Vektorska baza podataka, za razliku od tradicionalnih baza, je specijalizirana baza podataka dizajnirana za spremanje, upravljanje i pretraživanje ugniježđenih vektora. Sprema numeričke prikaze dokumenata. Razbijanje podataka na numeričke ugradnje olakšava našem AI sustavu razumijevanje i obradu podataka.

Pohranjujemo naše ugradnje u vektorske baze jer LLM-ovi imaju limit na broj tokena koje prihvaćaju kao ulaz. Kako ne možete proslijediti cjelokupne ugradnje LLM-u, morat ćemo ih razbiti u dijelove i kad korisnik postavi pitanje, vraćaju se ugradnje koje najviše odgovaraju pitanju zajedno s upitom. Razbijanje također smanjuje troškove broja tokena proslijeđenih kroz LLM.

Neke popularne vektorske baze uključuju Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Možete stvoriti Azure Cosmos DB model korištenjem Azure CLI s slijedećom naredbom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od teksta do ugradnji

Prije pohrane podataka, potrebno ih je pretvoriti u vektorske ugradnje. Ako radite s velikim dokumentima ili dugim tekstovima, možete ih dijeliti u segmente temeljem očekivanih upita. Dijeljenje može biti na razini rečenice ili odlomka. Kako dijelovi izvode značenje iz okoline riječi, možete dodati drugi kontekst dijelu, na primjer, dodavanjem naslova dokumenta ili uključivanjem teksta prije ili poslije dijela. Podatke možete dijeliti na sljedeći način:

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

    # Ako zadnji komad nije dosegao minimalnu duljinu, dodajte ga ionako
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Nakon što su podijeljeni, možemo tekst ugrađivati pomoću različitih modela ugradnje. Neki modeli koje možete koristiti uključuju: word2vec, ada-002 od OpenAI-a, Azure Computer Vision i mnoge druge. Odabir modela ovisi o jezicima koje koristite, tipu sadržaja koji se kodira (tekst/slike/zvuk), veličini ulaza koju može kodirati i duljini izlaza ugradnje.

Primjer ugradnje teksta korištenjem OpenAI `text-embedding-ada-002` modela:
![ugradnja riječi mačka](../../../translated_images/hr/cat.74cbd7946bc9ca38.webp)

## Dohvaćanje i vektorsko pretraživanje

Kad korisnik postavi pitanje, dohvaćalac ga pretvara u vektor koristeći enkoder upita, zatim pretražuje naš indeks dokumenata za relevantne vektore u dokumentu povezane s ulazom. Nakon toga pretvara oba, ulazni vektor i vektore dokumenata, natrag u tekst i prosljeđuje ih kroz LLM.

### Dohvaćanje

Dohvaćanje se događa kad sustav nastoji brzo pronaći dokumente iz indeksa koji zadovoljavaju kriterije pretraživanja. Cilj dohvaćalca je dobiti dokumente koji će se koristiti kao kontekst i temelj LLM-a na vašim podacima.

Postoje različiti načini za pretraživanje u našoj bazi podataka, kao što su:

- **Pretraživanje ključnim riječima** - koristi se za tekstualno pretraživanje

- **Vektorsko pretraživanje** - pretvara dokumente iz teksta u vektorske prikaze pomoću modela ugradnje, dopuštajući **semantičko pretraživanje** na temelju značenja riječi. Dohvaćanje se vrši upitivanjem dokumenata čiji su vektorski prikazi najbliži korisničkom pitanju.

- **Hibridno** - kombinacija pretraživanja ključnim riječima i vektorskog pretraživanja.

Izazov kod dohvaćanja nastaje kada u bazi nema sličnog odgovora na upit; sustav tada vraća najbolju dostupnu informaciju, no možete koristiti tehnike poput postavljanja maksimalne udaljenosti za relevantnost ili koristiti hibridno pretraživanje koje kombinira ključne riječi i vektorsko pretraživanje. U ovoj lekciji koristit ćemo hibridno pretraživanje, kombinaciju vektorskog i pretraživanja ključnim riječima. Naše podatke pohranit ćemo u datafrejm s stupcima koji sadrže dijelove i ugradnje.

### Vektorska sličnost

Dohvaćalac će pretraživati bazu znanja za ugradnje koje su blizu jedna drugoj, najsličnijeg susjeda, jer su tekstovi slični. U scenariju kada korisnik postavi upit, on se prvo ugradi, zatim usporedi sličnim ugradnjama. Uobičajena mjera koja se koristi za utvrđivanje koliko su različiti vektori slični jest kosinusna sličnost koja se temelji na kutu između dva vektora.

Možemo mjeriti sličnost i drugim metodama poput Euklidske udaljenosti, što je najkraća linija između krajeva vektora, te skalarne produkcije koja mjeri zbroj proizvoda odgovarajućih elemenata dvaju vektora.

### Indeks pretraživanja

Prije dohvaćanja, potrebno je izgraditi indeks pretraživanja za bazu znanja. Indeks će pohraniti naše ugradnje i može brzo dohvatiti najsličnije dijelove čak i u velikoj bazi podataka. Indeks možemo stvoriti lokalno koristeći:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Stvori indeks pretraživanja
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Za upit indeksa, možete koristiti metodu kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno rangiranje

Kad ste upitom dohvatili podatke, možda ćete ih htjeti sakupiti od najrelevantnijih. LLM za re-rangiranje koristi strojno učenje za poboljšanje relevantnosti rezultata pretraživanja tako da ih poretka od najrelevantnijih. Korištenjem Azure AI Search, re-rangiranje se automatski izvršava koristeći semantički re-ranker. Primjer kako re-rangiranje radi koristeći najbliže susjede:

```python
# Pronađite najsličnije dokumente
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Ispišite najsličnije dokumente
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

Posljednji korak je dodavanje našeg LLM-a kako bi mogli dobiti odgovore koji su utemeljeni na našim podacima. To možemo implementirati na sljedeći način:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Pretvori pitanje u vektor upita
    query_vector = create_embeddings(user_input)

    # Pronađi najsličnije dokumente
    distances, indices = nbrs.kneighbors([query_vector])

    # dodaj dokumente upitu kako bi pružio kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # kombiniraj povijest i korisnički unos
    history.append(user_input)

    # kreiraj objekt poruke
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # koristi Responses API za generiranje odgovora
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

- Kvaliteta danih odgovora, osiguravajući da zvuče prirodno, tečno i ljudski

- Utemeljenost podataka: evaluacija je li odgovor došao iz priloženih dokumenata

- Relevantnost: evaluacija je li odgovor povezan i odgovara na postavljeno pitanje

- Tečnost - je li odgovor gramatički smislen

## Primjeri upotrebe RAG-a (Generiranje potpomognuto dohvatom) i vektorskih baza podataka

Postoje mnogi slučajevi upotrebe gdje funkcijski pozivi mogu unaprijediti vašu aplikaciju, kao što su:

- Pitanja i odgovori: pridruživanje podataka vaše tvrtke chatu koji koriste zaposlenici za postavljanje pitanja.

- Sustavi preporuke: gdje možete izraditi sustav koji pronalazi najbliže podudarne vrijednosti, npr. filmove, restorane i još mnogo toga.

- Chatbot usluge: možete pohraniti povijest razgovora i personalizirati konverzaciju na osnovu korisničkih podataka.

- Pretraživanje slika temeljeno na vektorskim ugradnjama, korisno pri prepoznavanju slika i otkrivanju anomalija.

## Sažetak

Pokrili smo osnovna područja RAG-a od dodavanja naših podataka u aplikaciju, korisničkog upita do izlaza. Za pojednostavljenje izrade RAG-a možete koristiti frameworke poput Semanti Kernel, Langchain ili Autogen.

## Zadatak

Za nastavak učenja o Generiranju potpomognutom dohvatom (RAG) možete izraditi:

- Izraditi sučelje za aplikaciju koristeći framework po vlastitom izboru

- Iskoristiti neki od frameworka, bilo LangChain ili Semantic Kernel, i ponovno kreirati svoju aplikaciju.

Čestitamo na završetku lekcije 👏.

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju Generativnog AI učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnom AI-u!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->