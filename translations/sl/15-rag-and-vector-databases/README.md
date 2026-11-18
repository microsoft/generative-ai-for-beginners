# Pridobivanje z izboljšano generacijo (RAG) in vektorske baze podatkov

[![Pridobivanje z izboljšano generacijo (RAG) in vektorske baze podatkov](../../../translated_images/sl/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekciji o iskalnih aplikacijah smo na kratko spoznali, kako integrirati svoje podatke v modele velikih jezikov (LLM). V tej lekciji bomo podrobneje obravnavali koncepte utemeljitve vaših podatkov v aplikaciji LLM, mehanizme procesa in metode za shranjevanje podatkov, vključno z vgradnjami in besedilom.

> **Video kmalu na voljo**

## Uvod

V tej lekciji bomo obravnavali naslednje:

- Uvod v RAG, kaj je in zakaj se uporablja v umetni inteligenci (AI).

- Razumevanje, kaj so vektorske baze podatkov in ustvarjanje take za našo aplikacijo.

- Praktičen primer, kako integrirati RAG v aplikacijo.

## Cilji učenja

Po zaključku te lekcije boste znali:

- Pojasniti pomen RAG pri iskanju in obdelavi podatkov.

- Nastaviti aplikacijo RAG in utemeljiti LLM s svojimi podatki.

- Učinkovito integrirati RAG in vektorske baze podatkov v aplikacije LLM.

## Naš scenarij: izboljševanje naših LLM z lastnimi podatki

Za to lekcijo želimo dodati svoje zapiske v izobraževalni startup, ki omogoča klepetalnemu botu pridobivanje več informacij o različnih predmetih. Z uporabo teh zapiskov bodo učenci lahko bolje študirali in razumeli različne teme, kar jim bo olajšalo pripravo na izpite. Za ustvarjanje našega scenarija bomo uporabili:

- `Azure OpenAI:` LLM, ki ga bomo uporabili za ustvarjanje našega klepetalnega bota

- `AI for beginners' lesson on Neural Networks`: to bodo podatki, na katerih bomo utemeljili naš LLM

- `Azure AI Search` in `Azure Cosmos DB:` vektorsko bazo podatkov za shranjevanje naših podatkov in ustvarjanje iskalnega indeksa

Uporabniki bodo lahko ustvarjali vaja vprašanja in kartice za ponavljanje iz svojih zapiskov ter povzeli te zapiske v jedrnate preglednice. Za začetek si poglejmo, kaj je RAG in kako deluje:

## Pridobivanje z izboljšano generacijo (RAG)

LLM-poganjani klepetalni bot obdeluje uporabniške pozive za ustvarjanje odgovorov. Namenjen je interakciji in sodelovanju z uporabniki o širokem naboru tem. Njegovi odgovori pa so omejeni na podani kontekst in njegove izhodiščne učne podatke. Na primer, znanje GPT-4 je omejeno do septembra 2021, kar pomeni, da nima znanja o dogodkih po tem obdobju. Poleg tega podatki, uporabljeni za usposabljanje LLM, izključujejo zaupne informacije, kot so osebni zapiski ali priročnik za izdelek podjetja.

### Kako delujejo RAG (pridobivanje z izboljšano generacijo)

![risba, ki prikazuje, kako delujejo RAG](../../../translated_images/sl/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Predpostavimo, da želite zagnati klepetalnega bota, ki ustvarja kvize iz vaših zapiskov — potrebovali boste povezavo do baze znanja. Tu pride do izraza RAG. RAG deluje tako:

- **Baza znanja:** Pred pridobivanjem je treba te dokumente vnesti in predprocesirati, običajno z razbijanjem velikih dokumentov na manjše dele, pretvorbo v vdelave besedila ter shranjevanje v bazo podatkov.

- **Uporabniški poizvedba:** uporabnik postavi vprašanje

- **Pridobivanje:** Ko uporabnik postavi vprašanje, model vdelave poišče ustrezne informacije v naši bazi znanja, da zagotovi več konteksta, ki se bo vključil v poziv.

- **Izboljšana generacija:** LLM izboljša svoj odgovor na podlagi pridobljenih podatkov. To omogoča, da je odgovor generiran ne le na podlagi vnaprej usposobljenih podatkov, temveč tudi relevantnih informacij iz dodanega konteksta. Pridobljeni podatki se uporabijo za izboljšanje LLM odzivov. LLM nato vrne odgovor na uporabnikovo vprašanje.

![Diagram, ki prikazuje arhitekturo RAG](../../../translated_images/sl/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG združuje iskalnik z generatorjem: poizvedba se pretvori v vektor, ta se poišče v indeksu dokumentov za najdbo ustreznih besedilnih kosov, ki se nato zagotovijo kot kontekst LLM, ki ustvari odgovor. Iskalnik in generator lahko uporabljata različne modele; RAG ne zahteva transformatorja kodirnik-dekodirnik.

Dva pristopa pri implementaciji RAG po predlaganem članku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sta:

- **_RAG-Sequence_** uporaba pridobljenih dokumentov za napovedovanje najboljše možne odgovora na uporabniško vprašanje

- **RAG-Token** uporaba dokumentov za generiranje naslednjega tokena, nato njihovo pridobivanje za odgovor na uporabniško vprašanje

### Zakaj uporabljati RAG? 

- **Bogastvo informacij:** zagotavlja, da so besedilni odgovori ažurni in aktualni. S tem izboljšuje uspešnost pri nalogah, specifičnih za določeno področje, z dostopom do notranje baze znanja.

- Zmanjšuje izmišljanje z uporabo **verificiranih podatkov** v bazi znanja, da nudi kontekst uporabniškim vprašanjem.

- Je **stroškovno učinkovit** saj je bolj ekonomičen v primerjavi s finim prilagajanjem LLM.

## Ustvarjanje baze znanja

Naša aplikacija temelji na naših osebnih podatkih, tj. lekciji o Nevronskih mrežah iz učnega načrta AI za začetnike.

### Vektorske baze podatkov

Vektorska baza podatkov, za razliko od tradicionalnih baz, je specializirana baza podatkov, ki je namenjena shranjevanju, upravljanju in iskanju vgrajenih vektorjev. Shrani številčne predstavitve dokumentov. Razbitje podatkov na številčne vgradnje omogoča našemu AI sistemu lažje razumevanje in obdelavo podatkov.

Ker imajo LLM omejitve glede števila vhodnih tokenov, dokumente razdelimo na kose pred vgradnjo. Ko uporabnik postavi vprašanje, vgradnje, ki so najbolj podobne poizvedbi, identificirajo relevantne tekstovne dele, ki se vrnejo z pozivom. Razdeljevanje tudi zmanjšuje število tokenov, ki se posredujejo LLM, s čimer lahko zniža stroške.

Nekaj priljubljenih vektorskih baz vključuje Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant in DeepLake. Model Azure Cosmos DB lahko ustvarite z ukazom Azure CLI:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od besedila do vgradnje

Preden shranimo naše podatke, jih moramo pretvoriti v vektorske vgradnje, preden jih shranimo v bazo. Če delate z velikimi dokumenti ali dolgimi teksti, jih lahko razdelite glede na pričakovane poizvedbe. Razdeljevanje lahko opravite na ravni stavkov ali odstavkov. Ker razdeljevanje izhaja iz pomenov okoliških besed, lahko v kos dodate tudi drugi kontekst, na primer naslov dokumenta ali nekaj besedila pred ali za kosom. Podatke lahko razdelite na naslednji način:

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

Ko so podatki razdeljeni, jih lahko vgradimo z uporabo različnih modelov za vgradnjo. Nekateri modeli, ki jih lahko uporabite, vključujejo: word2vec, ada-002 od OpenAI, Azure Computer Vision in še mnoge druge. Izbira modela je odvisna od jezikov, ki jih uporabljate, vrste kodirane vsebine (besedilo/slike/zvok), velikosti vhoda, ki ga lahko model kodira, ter dolžine vgradnje.

Primer vgrajenega besedila z modelom `text-embedding-ada-002` iz OpenAI je:
![embedding besede mačka](../../../translated_images/sl/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pridobivanje in vektorsko iskanje

Ko uporabnik postavi vprašanje, pridobiteljski modul to vprašanje pretvori v vektor z uporabo kodirnika poizvedb, nato poišče po indeksu dokumentov za relevantne vektorje, povezane z vhodom. Ko konča, pretvori vhodni in dokumentne vektorje nazaj v besedilo in jih posreduje LLM.

### Pridobivanje

Pridobivanje se zgodi, ko sistem poskuša hitro najti dokumente v indeksu, ki ustrezajo iskalnim kriterijem. Namen pridobitelja je pridobiti dokumente, ki se uporabijo kot kontekst in dajo LLM trdno podlago na vaših podatkih.

Iskanje v naši bazi lahko izvedemo na več načinov, kot so:

- **Iskanje po ključnih besedah** - za tekstovno iskanje

- **Vektorsko iskanje** - pretvori dokumente iz besedila v vektorske predstavitve z uporabo modelov za vgradnjo, kar omogoča **semantično iskanje** z uporabo pomena besed. Pridobivanje poteka z poizvedbo dokumentov, katerih vektorske predstavitve so najbližje uporabnikovemu vprašanju.

- **Hibridno** - kombinacija iskanja po ključnih besedah in vektorskega iskanja.

Težava pri pridobivanju nastane, kadar v bazi ni podobnega odgovora na poizvedbo, sistem bo vrnil najboljše informacije, ki jih lahko dobi, vendar lahko uporabite taktike, kot je nastavitev največje dopustne razdalje za relevantnost ali uporabo hibridnega iskanja, ki združuje ključno besedo in vektorsko iskanje. V tej lekciji bomo uporabili hibridno iskanje, kombinacijo vektorskega in iskanja po ključnih besedah. Podatke bomo shranili v dataframe s stolpci, ki vsebujejo kose in vgradnje.

### Vektorska podobnost

Pridobitelj bo iskal po bazi znanja vgradnje, ki so si blizu – najbližji sosedje – ker predstavljajo besedila, ki so podobna. V tem scenariju, ko uporabnik odda vprašanje, se najprej vgradi in nato primerja s podobnimi vgradnjami. Najpogosteje uporabljena mera za primerjavo vektorskih podobnosti je kosinusna podobnost, ki temelji na kotu med dvema vektorjema.

Druge metrike za merjenje podobnosti vključujejo evklidsko razdaljo, ki je najkrajša črta med končnima točkama vektorjev, in skalarni produkt, ki meri vsoto produktov ustreznih elementov v dveh vektorjih.

### Iskalni indeks

Pri pridobivanju bomo morali pred iskanjem ustvariti iskalni indeks za našo bazo znanja. Indeks bo shranjeval naše vgradnje in bo lahko hitro pridobil najbolj podobne kose tudi v veliki bazi podatkov. Indeks lahko ustvarimo lokalno z uporabo:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno razvrščanje

Ko poizvedujete bazo, boste morda morali rezultate razvrstiti od najbolj relevantnih. Re-rangirajoči LLM uporablja strojno učenje za izboljšanje relevantnosti iskalnih rezultatov z njihovim urejanjem od najbolj relevantnega navzdol. Z uporabo Azure AI Search se ponovno razvrščanje samodejno izvede z uporabo semantičnega razvrščevalnika. Primer delovanja ponovnega razvrščanja z najbližjimi sosedi:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Združevanje vsega skupaj

Zadnji korak je dodajanje našega LLM, da dobimo odgovore, ki temeljijo na naših podatkih. Implementacijo lahko izvedemo tako:

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

## Evalvacija naše aplikacije

### Merila za evalvacijo

- Kakovost podanih odgovorov, ki zagotavljajo, da izgledajo naravno, tekoče in človeško

- Temelji na podatkih: ocenjevanje, ali je odgovor prišel iz podanih dokumentov

- Relevantnost: ocenjevanje, ali odgovor ustreza in je povezan z zastavljenim vprašanjem

- Tekočnost - ali je odgovor slovnično smiseln

## Primeri uporabe RAG (Retrieval Augmented Generation) in vektorskih baz podatkov

Obstaja veliko različnih primerov uporabe, kjer lahko RAG izboljša vašo aplikacijo, na primer:

- Vpraša in odgovor: povežite podatke vašega podjetja v klepet, ki ga lahko uporabljajo zaposleni za postavljanje vprašanj.

- Sistemi priporočil: lahko ustvarite sistem, ki primerja najbolj podobne vrednosti, npr. filme, restavracije in še več.

- Storitve chatbotov: lahko shranjujete zgodovino pogovorov in personalizirate pogovor glede na uporabniške podatke.

- Iskanje slik na podlagi vektorskih vgradnj, uporabno pri prepoznavanju slik in odkrivanju anomalij.

## Povzetek

Pokrili smo osnovna področja RAG od dodajanja podatkov v aplikacijo, uporabniške poizvedbe do izhoda. Za poenostavitev ustvarjanja RAG lahko uporabite ogrodja, kot so Semantic Kernel, LangChain ali AutoGen.

## Naloga

Da nadaljujete z učenjem Retrieval Augmented Generation (RAG), lahko ustvarite:

- Front-end za aplikacijo z uporabo ogrodja po vaši izbiri

- Uporabite ogrodje, bodisi LangChain ali Semantic Kernel, in ponovno ustvarite vašo aplikacijo.

Čestitke ob zaključku lekcije 👏.

## Učenje se tukaj ne konča, nadaljujte pot

Po končani lekciji si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nadaljnje poglabljanje znanja o generativni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->