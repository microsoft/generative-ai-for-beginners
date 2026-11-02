# Generiranje z dopolnitvijo iskanja (RAG) in vektorske baze podatkov  

[![Generiranje z dopolnitvijo iskanja (RAG) in vektorske baze podatkov](../../../translated_images/sl/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)  

V lekciji o aplikacijah iskanja smo na kratko spoznali, kako vključiti lastne podatke v velike jezikovne modele (LLM). V tej lekciji bomo podrobneje raziskali koncepte utemeljitve podatkov v vaši aplikaciji LLM, mehaniko procesa in metode shranjevanja podatkov, vključno z vdelavami in besedilom.  

> **Video prihaja kmalu**  

## Uvod  

V tej lekciji bomo pokrili naslednje:  

- Uvod v RAG, kaj je in zakaj se uporablja v AI (umetna inteligenca).  

- Razumevanje, kaj so vektorske baze podatkov in ustvarjanje takšne baze za našo aplikacijo.  

- Praktičen primer, kako integrirati RAG v aplikacijo.  

## Cilji učenja  

Po zaključku te lekcije boste lahko:  

- Pojasnili pomen RAG pri pridobivanju in obdelavi podatkov.  

- Nastavili aplikacijo RAG in utemeljili LLM z vašimi podatki  

- Učinkovito integrirali RAG in vektorske baze podatkov v aplikacijah LLM.  

## Naš scenarij: izboljšanje naših LLM z lastnimi podatki  

Za to lekcijo želimo dodati naše lastne zapiske v izobraževalno zagonsko podjetje, ki omogoča klepetalnemu robotu, da pridobi več informacij o različnih predmetih. Z uporabo zapiskov, ki jih imamo, bodo se učenci lažje učili in razumeli različne teme, kar bo olajšalo pripravo na izpite. Za ustvarjanje našega scenarija bomo uporabili:  

- `Azure OpenAI:` LLM, ki ga bomo uporabili za ustvarjanje našega klepetalnega robota  

- `AI for beginners' lesson on Neural Networks`: to bodo podatki, na katerih bomo utemeljili naš LLM  

- `Azure AI Search` in `Azure Cosmos DB:` vektorsko bazo podatkov za shranjevanje podatkov in ustvarjanje iskalnega indeksa  

Uporabniki bodo lahko ustvarjali vadbene kvize in kartice za ponavljanje iz svojih zapiskov ter povzemali te zapiske v jedrnate preglednice. Za začetek si oglejmo, kaj je RAG in kako deluje:  

## Generiranje z dopolnitvijo iskanja (RAG)  

Klepetalni robot, poganjan z LLM, obdeluje uporabniške pozive za ustvarjanje odgovorov. Namenjen je interakciji in sodelovanju z uporabniki o širokem spektru tem. Vendar so njegovi odgovori omejeni na podani kontekst in na osnovne učne podatke. Na primer, mejni datum znanja GPT-4 je september 2021, kar pomeni, da nima znanja o dogodkih, ki so se zgodili po tem obdobju. Poleg tega podatki, uporabljeni za učenje LLM, izključujejo zaupne informacije, kot so osebni zapiski ali priročniki podjetja za izdelke.  

### Kako delujejo RAG (Generiranje z dopolnitvijo iskanja)  

![risba, ki prikazuje, kako delujejo RAG](../../../translated_images/sl/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)  

Predpostavimo, da želite zagotoviti klepetalnega robota, ki ustvarja kvize iz vaših zapiskov; potrebovali boste povezavo z bazo znanja. Tukaj pride prav RAG. RAG deluje tako:  

- **Baza znanja:** Pred pridobivanjem je treba dokumente uvoziti in predobdelati, običajno s tem, da se veliki dokumenti razdelijo na manjše dele, pretvorijo v vdelavo besedila in shranijo v bazo podatkov.  

- **Uporabniška poizvedba:** uporabnik postavi vprašanje  

- **Iskanje:** Ko uporabnik postavi vprašanje, model vdelave pridobi relevantne informacije iz naše baze znanja, da zagotovi več konteksta, ki bo vključen v poziv.  

- **Generiranje z dopolnitvijo:** LLM izboljša svoj odgovor na podlagi pridobljenih podatkov. To omogoča, da je odgovor, ki ga ustvari, ne le na podlagi vnaprej treniranih podatkov, ampak tudi relevantne informacije iz dodanega konteksta. Pridobljeni podatki se uporabijo za dopolnitev odgovorov LLM. LLM nato vrne odgovor na uporabnikovo vprašanje.  

![diagram, ki prikazuje arhitekturo RAG](../../../translated_images/sl/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)  

RAG združuje iskalnik z generatorjem: poizvedba se pretvori v vektor, se ujema z dokumentnim indeksom za iskanje relevantnih kosov besedila, ti deli so dani kot kontekst LLM, ki generira odgovor. Iskalnik in generator lahko uporabljata različne modele; RAG ne zahteva transformatorja tipa encoder-decoder.  

Dva pristopa pri implementaciji RAG po predlaganem članku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sta:

- **_RAG-Sequence_** uporablja pridobljene dokumente za napoved najbolj možnega odgovora na uporabniško vprašanje

- **RAG-Token** uporablja dokumente za generiranje naslednjega tokena, nato jih pridobi za odgovor na uporabnikovo vprašanje

### Zakaj bi uporabljali RAG? 

- **Bogastvo informacij:** zagotavlja, da so besedilni odgovori ažurni in tekoči. S tem izboljša delovanje na specifičnih nalogah s dostopom do notranje baze znanja.

- Zmanjšuje izmišljanje z uporabo **preverljivih podatkov** v bazi znanja za zagotavljanje konteksta uporabniškim poizvedbam.

- Je **stroškovno učinkovit** saj je cenejši od fino nastavljanja velikega jezikovnega modela (LLM)

## Ustvarjanje baze znanja

Naša aplikacija temelji na naših osebnih podatkih, tj. lekciji o nevronskih mrežah iz učnega načrta AI za začetnike.

### Vektorske baze podatkov

Vektorska baza podatkov, v nasprotju s tradicionalnimi bazami, je specializirana baza za shranjevanje, upravljanje in iskanje vključenih vektorjev. Shranjuje številčne reprezentacije dokumentov. Razbijanje podatkov v številčne vgradnje olajša razumevanje in obdelavo podatkov našemu AI sistemu.

Ker imajo veliki jezikovni modeli omejitev glede števila vhodnih tokenov, dokumente razdelimo na kose, preden jih vgradimo. Ko uporabnik postavi vprašanje, vgradnje, najbolj podobne poizvedbi, identificirajo ustrezne besedilne kose, ki se vrnejo s pozivom. Razbijanje na kose tudi zmanjša število tokenov, poslanih LLM, in zato lahko zniža stroške.

Nekatere priljubljene vektorske baze so Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant in DeepLake. Model Azure Cosmos DB lahko ustvarite z uporabo Azure CLI z naslednjim ukazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od besedila do vgradnje

Preden shranimo naše podatke, jih moramo pretvoriti v vektorske vgradnje, preden jih shranimo v bazo. Če delate z velikimi dokumenti ali dolgimi besedili, jih lahko razdelite na kose glede na pričakovane poizvedbe. Razbijanje lahko poteka na ravni stavkov ali odstavkov. Ker razbijanje izhaja iz pomenov okoli besed, lahko k toku dodate še drug kontekst, na primer z dodajanjem naslova dokumenta ali vključitvijo besedila pred ali za kos. Podatke lahko razdelite kot sledi:

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

Ko so kosi pripravljeni, lahko besedilo vgradimo z različnimi modeli vgradnje. Nekateri modeli, ki jih lahko uporabite, vključujejo: word2vec, ada-002 by OpenAI, Azure Computer Vision in še več. Izbira modela je odvisna od jezikov, ki jih uporabljate, vrste vsebine, ki jo kodira (besedilo/slike/zvok), velikosti vhoda in dolžine izhoda vgradnje.

Primer vgrajenega besedila z modelom OpenAI `text-embedding-ada-002`:
![vgradnja besede cat](../../../translated_images/sl/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pridobivanje in vektorsko iskanje

Ko uporabnik postavi vprašanje, ga pridobitelj pretvori v vektor s kodirnikom poizvedbe, nato pa išče v našem iskalniku dokumentov ustrezne vektorje, povezane z vhodom. Ko konča, pretvori tako vhodni kot dokumentne vektorje nazaj v besedilo in ju posreduje LLM.

### Pridobivanje

Pridobivanje poteka, ko sistem hitro poskuša najti dokumente v indeksu, ki ustrezajo iskalnim merilom. Cilj pridobitelja je pridobiti dokumente, ki se uporabijo za zagotovitev konteksta in utemeljitev LLM na vaših podatkih.

Obstaja več načinov iskanja v naši bazi, kot so:

- **Iskanje po ključnih besedah** - uporablja se za besedilna iskanja

- **Vektorsko iskanje** - pretvori dokumente iz besedila v vektorske reprezentacije z modeli vgradnje, kar omogoča **semantično iskanje** po pomenu besed. Pridobivanje poteka z iskanjem dokumentov, katerih vektorske reprezentacije so najbližje uporabnikovemu vprašanju.

- **Hibridno** - kombinacija iskanja po ključnih besedah in vektorskega iskanja.

Težava pri pridobivanju nastopi, ko baza nima podobnega odgovora poizvedbi, sistem bo takrat vrnil najboljše informacije, ki jih lahko dobi, lahko pa uporabite taktike, kot so nastavitev največje razdalje za relevantnost ali hibridno iskanje, ki združuje ključno besedo in vektorsko iskanje. V tej lekciji bomo uporabili hibridno iskanje, kombinacijo vektorskega in iskanja po ključnih besedah. Podatke bomo shranili v podatkovni okvir s stolpci, ki vsebujejo kose in vgradnje.

### Vektorska podobnost

Pridobitelj bo iskal v bazi znanja vgradnje, ki so blizu skupaj — najbližji sosedje — saj predstavljajo podobna besedila. V tem primeru, ko uporabnik pošlje poizvedbo, se ta najprej vgradi in nato ujame z podobnimi vgradnjami. Najpogosteje uporabljena mera za primerjavo vektorske podobnosti je kosinusna podobnost, ki temelji na kotu med dvema vektorjema.

Druge metrike, ki jih lahko uporabimo za merjenje podobnosti, vključujejo evklidsko razdaljo, ki je najkrajša linija med končnima točkama vektorjev, in skalarni produkt, ki meri vsoto produktov ustreznih elementov v dveh vektorjih.

### Iskalni indeks

Pri pridobivanju moramo pred iskanjem ustvariti iskalni indeks za našo bazo znanja. Indeks bo shranil naše vgradnje in lahko hitro pridobi najbolj podobne kose, tudi v veliki bazi. Indeks lahko ustvarimo lokalno z:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno razvrščanje

Ko ste poizvedbo poslali v bazo, boste morda morali rezultate razvrstiti od najbolj relevantnih. Ponovno razvrščanje LLM uporablja strojno učenje za izboljšanje relevantnosti rezultatov iskanja z njihovo razvrstitvijo od najbolj relevantnih. Z uporabo Azure AI Search se ponovno razvrščanje samodejno izvaja z uporabo semantičnega preurednika. Primer, kako deluje ponovno razvrščanje z najbližjimi sosedi:

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

## Vse skupaj

Zadnji korak je vključitev našega LLM, da dobimo odgovore, ki temeljijo na naših podatkih. Implementiramo ga lahko takole:

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

## Ocenjevanje naše aplikacije

### Merila ocenjevanja

- Kakovost podanih odgovorov, ki zagotavljajo, da zvenijo naravno, tekoče in kot človeški

- Utemeljenost podatkov: ocenjevanje, ali je odgovor prišel iz podanih dokumentov

- Relevantnost: ocena, ali odgovor ustreza in je povezan z zastavljenim vprašanjem

- Tekočnost - ali je odgovor slovnično smiseln

## Primeri uporabe RAG (Retrieval Augmented Generation) in vektorskih podatkovnih baz

Obstaja veliko različnih primerov uporabe, kjer lahko RAG izboljša vašo aplikacijo, kot so:

- Vprašanja in odgovori: utemeljitev podatkov vašega podjetja v klepetu, ki ga lahko zaposleni uporabljajo za postavljanje vprašanj.

- Priporočilni sistemi: kjer lahko ustvarite sistem, ki ujema najprimernejše vrednosti npr. filme, restavracije in še več.

- Storitve chatbotov: lahko shranite zgodovino pogovorov in personalizirate klepet na podlagi uporabniških podatkov.

- Iskanje slik na podlagi vektorskih vgradnje, uporabno pri prepoznavanju slik in odkrivanju anomalij.

## Povzetek

Obravnavali smo osnovna področja RAG od dodajanja naših podatkov v aplikacijo, uporabniške poizvedbe in izhod. Za poenostavitev ustvarjanja RAG lahko uporabite ogrodja, kot so Semantic Kernel, LangChain ali AutoGen.

## Naloga

Za nadaljevanje učenja o Retrieval Augmented Generation (RAG) lahko zgradite:

- Ustvarite frontend aplikacije z ogrodjem po vaši izbiri

- Uporabite ogrodje, bodisi LangChain ali Semantic Kernel, in ponovno ustvarite svojo aplikacijo.

Čestitke za dokončanje lekcije 👏.

## Učenje se tukaj ne konča, nadaljujte potovanje

Po končani lekciji si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nadaljevanje nadgrajevanja vašega znanja o Generativni AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->