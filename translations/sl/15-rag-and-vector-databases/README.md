# Pridobivanje z izboljšanim generiranjem (RAG) in vektorske baze podatkov

[![Pridobivanje z izboljšanim generiranjem (RAG) in vektorske baze podatkov](../../../translated_images/sl/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekciji o aplikacijah iskanja smo na kratko spoznali, kako integrirati lastne podatke v velike jezikovne modele (LLM). V tej lekciji bomo bolj podrobno raziskali pojme utemeljitve vaših podatkov v aplikaciji LLM, mehaniko procesa in metode za shranjevanje podatkov, vključno tako z vdelavami kot besedilom.

> **Video prihaja kmalu**

## Uvod

V tej lekciji bomo pokrili naslednje:

- Uvod v RAG, kaj je in zakaj se uporablja v AI (umetna inteligenca).

- Razumevanje, kaj so vektorske baze podatkov in kako ustvariti eno za našo aplikacijo.

- Praktičen primer, kako integrirati RAG v aplikacijo.

## Cilji učenja

Po končani tej lekciji boste lahko:

- Pojasnili pomen RAG pri iskanju in obdelavi podatkov.

- Nastavili aplikacijo RAG in utemeljili podatke na LLM

- Učinkovita integracija RAG in vektorskih baz podatkov v LLM aplikacije.

## Naš scenarij: nadgradnja naših LLM s lastnimi podatki

Za to lekcijo želimo dodati svoje lastne zapiske v izobraževalno zagonsko podjetje, kar omogoča klepetalnemu botu pridobivanje več informacij o različnih predmetih. Z uporabo zapiskov, ki jih imamo, bodo uporabniki lahko bolje študirali in razumeli različne teme, kar bo olajšalo pripravo na izpite. Za ustvarjanje našega scenarija bomo uporabili:

- `Azure OpenAI:` LLM, ki ga bomo uporabili za ustvarjanje našega klepetalnega bota

- `Lekcija AI za začetnike o nevronskih mrežah`: to bo podlaga naših podatkov za LLM

- `Azure AI Search` in `Azure Cosmos DB:` vektorska baza podatkov za shranjevanje naših podatkov in ustvarjanje iskalnega indeksa

Uporabniki bodo lahko ustvarjali vaje iz svojih zapiskov, kartice za ponavljanje in povzemali vsebine v jedrnate preglede. Za začetek poglejmo, kaj je RAG in kako deluje:

## Pridobivanje z izboljšanim generiranjem (RAG)

Klepetalni bot, ki temelji na velikem jezikovnem modelu, obdeluje uporabniške pozive za generiranje odgovorov. Namenjen je interakciji in sodelovanju z uporabniki o različnih temah. Vendar so njegovi odgovori omejeni na kontekst, ki mu je na voljo, in njegovo osnovno učna podatkov. Na primer, znanje GPT-4 je omejeno do septembra 2021, kar pomeni, da nima znanja o dogodkih po tem obdobju. Poleg tega podatki, uporabljeni za usposabljanje LLM, izključujejo zaupne informacije, kot so osebni zapiski ali uporabniški priročniki podjetja.

### Kako delujejo RAG (Pridobivanje z izboljšanim generiranjem)

![risba prikazuje, kako delujejo RAG](../../../translated_images/sl/how-rag-works.f5d0ff63942bd3a6.webp)

Predpostavimo, da želite uporabiti klepetalnega bota, ki ustvarja kvize iz vaših zapiskov; potrebovali boste povezavo do baze znanja. Tukaj pride do izraza RAG. RAG deluje tako:

- **Baza znanja:** Pred pridobivanjem morajo biti ti dokumenti uvoženi in predobdelani, običajno z razdelitvijo velikih dokumentov na manjše dele, pretvorbo v vdelave besedila in shranjevanjem v bazo podatkov.

- **Uporabniški poizvedba:** uporabnik zastavi vprašanje

- **Pridobivanje:** Ko uporabnik zastavi vprašanje, model vdelave pridobi ustrezne informacije iz baze znanja, da zagotovi več konteksta, ki se vključi v poziv.

- **Izboljšano generiranje:** LLM izboljša svoj odgovor na podlagi pridobljenih podatkov. To omogoča, da je odgovor, ki ga generira, ne le na podlagi predtrenirane podatkov, ampak tudi relevantnih informacij iz dodanega konteksta. Pridobljeni podatki se uporabijo za izboljšanje odgovorov LLM. LLM nato vrne odgovor na uporabnikovo vprašanje.

![risba prikazuje arhitekturo RAG](../../../translated_images/sl/encoder-decode.f2658c25d0eadee2.webp)

Arhitektura RAG je izvedena z uporabo transformatorjev, ki so sestavljeni iz dveh delov: kodirnika in dekodirnika. Na primer, ko uporabnik zastavi vprašanje, se vhodno besedilo 'kodira' v vektorje, ki zajamejo pomen besed, nato pa se vektorji 'dekodirajo' v indeks dokumentov in generirajo nov tekst na podlagi uporabniške poizvedbe. LLM uporablja model kodirnik-dekodirnik za generiranje izhoda.

Obstajata dva pristopa pri implementaciji RAG po predlaganem članku: [Retrieval-Augmented Generation for Knowledge intensive NLP (naravoslovna obdelava jezika)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst):

- **_RAG-Sequence_** uporablja pridobljene dokumente za napovedovanje najboljšega možnega odgovora na uporabniško poizvedbo

- **RAG-Token** uporablja dokumente za generiranje naslednjega tokena, nato jih pridobi za odgovor na uporabnikovo poizvedbo

### Zakaj bi uporabljali RAG? 

- **Bogastvo informacij:** zagotavlja, da so tekstovni odgovori ažurni in aktualni. S tem izboljša delovanje pri specifičnih domenah z dostopom do notranje baze znanja.

- Zmanjša izmišljanje s tem, da uporablja **preverljive podatke** v bazi znanja za zagotavljanje konteksta uporabniškim poizvedbam.

- Je **stroškovno učinkovito**, saj je bolj ekonomično kot natančno prilagajanje LLM

## Ustvarjanje baze znanja

Naša aplikacija temelji na naših osebnih podatkih, tj. lekciji o nevronskih mrežah v kurikulumu AI za začetnike.

### Vektorske baze podatkov

Vektorska baza podatkov, v nasprotju s tradicionalnimi bazami podatkov, je specializirana baza, zasnovana za shranjevanje, upravljanje in iskanje vdelanih vektorjev. Shranjuje numerične predstavitve dokumentov. Razbijanje podatkov na numerične vdelave omogoča našemu sistemu AI lažje razumevanje in obdelavo podatkov.

Shranjujemo svoje vdelave v vektorskih bazah podatkov, ker imajo LLM omejitev števila tokenov, ki jih sprejmejo kot vhod. Ker ni mogoče poslati celotnih vdelav LLM, jih moramo razdeliti na dele, ko uporabnik zastavi vprašanje, bodo vrnjene vdelave, ki so najbolj podobne vprašanju, skupaj s pozivom. Razbijanje tudi znižuje stroške glede števila tokenov, ki se pošljejo skozi LLM.

Nekatere priljubljene vektorske baze podatkov vključujejo Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant in DeepLake. Model Azure Cosmos DB lahko ustvarite z uporabo Azure CLI z naslednjim ukazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od besedila do vdelav

Preden shranimo podatke, jih moramo pretvoriti v vektorske vdelave, preden jih shranimo v bazo podatkov. Če delate z velikimi dokumenti ali dolgimi besedili, jih lahko razdelite glede na pričakovane poizvedbe. Razdelitev se lahko opravi na ravni stavkov ali odstavkov. Ker razdeljevanje izvleče pomen iz besed okoli njih, lahko k delu dodate še nekaj drugega konteksta, na primer naslov dokumenta ali vključite nekaj besedila pred ali za delom. Podatke lahko razdelite tako:

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

    # Če zadnji kos ni dosegel minimalne dolžine, ga vseeno dodajte
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Ko so podatki razdeljeni, jih lahko vdelate z različnimi modeli vdelav. Nekateri modeli, ki jih lahko uporabite, vključujejo: word2vec, ada-002 od OpenAI, Azure Computer Vision in še več. Izbira modela je odvisna od jezikov, ki jih uporabljate, vrste vsebine, ki se kodira (besedilo/slike/zvok), velikosti vhodnih podatkov in dolžine izhoda vdelave.

Primer vdelanega besedila z modelom OpenAI `text-embedding-ada-002` je:
![vdelava besede mačka](../../../translated_images/sl/cat.74cbd7946bc9ca38.webp)

## Pridobivanje in vektorsko iskanje

Ko uporabnik zastavi vprašanje, ga pridobitelj pretvori v vektor z uporabo kodirnika poizvedbe, nato pa išče po iskalnem indeksu dokumentov za relevantne vektorje v dokumentih, ki so povezani z vhodom. Ko je to opravljeno, pretvori tako vhodni kot vektorske vektorje v tekst in jih posreduje LLM.

### Pridobivanje

Pridobivanje se zgodi, ko sistem poskuša hitro najti dokumente v indeksu, ki ustrezajo iskalnim kriterijem. Cilj pridobitelja je pridobiti dokumente, ki bodo uporabljeni za zagotavljanje konteksta in utemeljitev LLM na vaših podatkih.

Obstajajo različni načini za izvedbo iskanja znotraj naše baze podatkov, na primer:

- **Iskanje po ključnih besedah** – uporablja se za besedilno iskanje

- **Vektorsko iskanje** – pretvori dokumente iz besedila v vektorske predstavitve z uporabo modelov vdelav, kar omogoča **semantično iskanje** glede na pomen besed. Pridobivanje se izvaja z iskanjem dokumentov, katerih vektorske predstavitve so najbližje uporabnikovemu vprašanju.

- **Hibridno** – kombinacija iskanja po ključnih besedah in vektorskega iskanja.

Izziv pri pridobivanju nastopi, če v bazi ni podobnega odgovora na poizvedbo; sistem bo nato vrnil najboljšo informacijо, ki jo lahko najde. Lahko pa uporabite taktike, kot je nastavitev največje razdalje za relevantnost ali uporabite hibridno iskanje, ki združuje oboje – iskanje po ključnih besedah in vektorsko iskanje. V tej lekciji bomo uporabili hibridno iskanje, kombinacijo obeh načinov iskanja. Podatke bomo shranili v podatkovni okvir z stolpci, ki vsebujejo dele besedila in tudi vdelave.

### Vektorska podobnost

Pridobitelj bo iskal po bazi znanja vdelave, ki so med seboj blizu, najbližji sosed, saj so to podobni teksti. V scenariju, ko uporabnik postavi vprašanje, se najprej doda vdelavo in nato primerja s podobnimi vdelavami. Pogosta mera podobnosti, ki se uporablja za ugotavljanje, kako so različni vektorji podobni, je kosinusna podobnost, ki temelji na kotu med dvema vektorjema.

Podobnost lahko merimo tudi z drugimi alternativami, kot sta evklidska razdalja, ki je neposredna črta med končnima točkama vektorjev, in skalarni produkt, ki meri vsoto produktov ustreznih elementov dveh vektorjev.

### Iskalni indeks

Pri izvajanju pridobivanja bomo morali pred iskanjem sestaviti iskalni indeks za našo bazo znanja. Indeks bo shranil naše vdelave in lahko hitro pridobil najbolj podobne dele tudi v veliki bazi podatkov. Indeks lahko ustvarimo lokalno z uporabo:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Ustvari iskalni indeks
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Za poizvedovanje po indeksu lahko uporabite metodo kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno razvrščanje

Ko ste poizvedovali bazo podatkov, boste morda morali rezultate razvrstiti od najbolj relevantnih. Model za ponovno razvrščanje, ki uporablja strojno učenje, izboljšuje relevantnost rezultatov iskanja tako, da jih ureja od najbolj relevantnih. Z uporabo Azure AI Search se ponovno razvrščanje samodejno izvede z uporabo semantičnega razvrščevalnika. Primer, kako deluje ponovno razvrščanje z iskanjem najbližjih sosedov:

```python
# Poišči najbolj podobne dokumente
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Izpiši najbolj podobne dokumente
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Vse skupaj združimo

Zadnji korak je dodati naš LLM v proces, da bomo lahko dobili odgovore, ki temeljijo na naših podatkih. Izvedemo ga lahko tako:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Pretvori vprašanje v vektor poizvedbe
    query_vector = create_embeddings(user_input)

    # Najdi najbolj podobne dokumente
    distances, indices = nbrs.kneighbors([query_vector])

    # dodaj dokumente k poizvedbi, da zagotoviš kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # združi zgodovino in uporabniški vnos
    history.append(user_input)

    # ustvari objekt sporočila
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # uporabi Responses API za generiranje odgovora
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Ocena naše aplikacije

### Merila ocenjevanja

- Kakovost dobavljenih odgovorov, ki zagotavlja, da so naravni, tekoči in podobni človeškemu govoru

- Utemeljenost podatkov: ocenjevanje, ali je odgovor izhajal iz posredovanih dokumentov

- Relevantnost: ocenjevanje, če odgovor ustreza in je povezan z zastavljenim vprašanjem

- Tekočnost - ali je odgovor slovnično smiseln

## Primeri uporabe RAG (Pridobivanje z izboljšanim generiranjem) in vektorskih baz podatkov

Obstaja veliko primerov uporabe, kjer lahko klici funkcij izboljšajo vašo aplikacijo, kot so:

- Vprašanja in odgovori: utemeljitev podatkov podjetja za klepet, ki ga lahko zaposleni uporabljajo za postavljanje vprašanj.

- Sistemi priporočil: kjer lahko ustvarite sistem, ki ustreza najsličnejšim vrednostim, npr. filmi, restavracije in še več.

- Klepetalni servisi: lahko shranjujete zgodovino pogovorov in personalizirate pogovor glede na uporabnikove podatke.

- Iskanje slik na podlagi vektorskih vdelav, uporabno pri prepoznavanju slik in odkrivanju anomalij.

## Povzetek

Pokrili smo temeljna področja RAG od dodajanja podatkov v aplikacijo, uporabniške poizvedbe in izhoda. Za poenostavitev ustvarjanja RAG lahko uporabite ogrodja, kot so Semanti Kernel, Langchain ali Autogen.

## Naloga

Za nadaljevanje učenja o Pridobivanju z izboljšanim generiranjem (RAG) lahko ustvarite:

- Ustvarite sprednji del aplikacije z ogrodjem po vaši izbiri

- Uporabite ogrodje, bodisi LangChain ali Semantic Kernel, in ponovno ustvarite vašo aplikacijo.

Čestitamo za dokončano lekcijo 👏.

## Učenje se tukaj ne ustavi, nadaljujte pot

Po končani tej lekciji si oglejte našo [Zbirko Generativnega AI učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadgradite svoje znanje o Generativnem AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->