<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:46:50+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sl"
}
-->
# Povečana generacija pridobivanja (RAG) in vektorske baze podatkov

V lekciji o iskalnih aplikacijah smo na kratko spoznali, kako vključiti svoje podatke v velike jezikovne modele (LLM). V tej lekciji se bomo poglobili v koncepte utemeljitve vaših podatkov v vaši aplikaciji LLM, mehaniko procesa in metode za shranjevanje podatkov, vključno z vektorskimi predstavitvami in besedilom.

> **Video prihaja kmalu**

## Uvod

V tej lekciji bomo obravnavali naslednje:

- Uvod v RAG, kaj je to in zakaj se uporablja v umetni inteligenci (AI).

- Razumevanje, kaj so vektorske baze podatkov, in ustvarjanje ene za našo aplikacijo.

- Praktičen primer, kako integrirati RAG v aplikacijo.

## Cilji učenja

Po končani lekciji boste lahko:

- Razložili pomen RAG pri pridobivanju in obdelavi podatkov.

- Nastavili aplikacijo RAG in utemeljili svoje podatke na LLM.

- Učinkovita integracija RAG in vektorskih baz podatkov v aplikacije LLM.

## Naš scenarij: izboljšanje naših LLM-ov z lastnimi podatki

Za to lekcijo želimo dodati lastne zapiske v izobraževalni startup, kar omogoča klepetalnemu botu pridobivanje več informacij o različnih predmetih. Z uporabo zapiskov, ki jih imamo, bodo učenci lahko bolje študirali in razumeli različne teme, kar bo olajšalo pripravo na izpite. Za ustvarjanje našega scenarija bomo uporabili:

- `Azure OpenAI:` LLM, ki ga bomo uporabili za ustvarjanje našega klepetalnega bota

- `AI for beginners' lesson on Neural Networks`: to bodo podatki, na katerih bomo utemeljili naš LLM

- `Azure AI Search` in `Azure Cosmos DB:` vektorska baza podatkov za shranjevanje naših podatkov in ustvarjanje iskalnega indeksa

Uporabniki bodo lahko ustvarjali vadbene kvize iz svojih zapiskov, kartice za ponavljanje in jih povzemali v jedrnate preglede. Začnimo z razumevanjem, kaj je RAG in kako deluje:

## Povečana generacija pridobivanja (RAG)

Klepetalni bot, ki ga poganja LLM, obdeluje uporabniške pozive za ustvarjanje odgovorov. Namenjen je interaktivnosti in vključuje uporabnike v širok spekter tem. Vendar so njegovi odgovori omejeni na zagotovljeni kontekst in osnovne podatke o usposabljanju. Na primer, GPT-4 ima omejitev znanja do septembra 2021, kar pomeni, da mu manjka znanje o dogodkih, ki so se zgodili po tem obdobju. Poleg tega podatki, uporabljeni za usposabljanje LLM-ov, izključujejo zaupne informacije, kot so osebni zapiski ali priročnik za izdelke podjetja.

### Kako delujejo RAG-i (Povečana generacija pridobivanja)

Predpostavimo, da želite uvesti klepetalni bot, ki ustvarja kvize iz vaših zapiskov, potrebovali boste povezavo z bazo znanja. Tukaj pride na pomoč RAG. RAG-i delujejo na naslednji način:

- **Baza znanja:** Pred pridobivanjem je treba te dokumente vnesti in predhodno obdelati, običajno razdeliti velike dokumente na manjše dele, jih pretvoriti v vektorske predstavitve besedila in jih shraniti v bazo podatkov.

- **Uporabniško vprašanje:** uporabnik postavi vprašanje

- **Pridobivanje:** Ko uporabnik postavi vprašanje, model vektorske predstavitve pridobi ustrezne informacije iz naše baze znanja, da zagotovi več konteksta, ki bo vključen v poziv.

- **Povečana generacija:** LLM izboljša svoj odgovor na podlagi pridobljenih podatkov. Omogoča, da je ustvarjeni odgovor ne le na podlagi predhodno usposobljenih podatkov, temveč tudi na podlagi ustreznih informacij iz dodanega konteksta. Pridobljeni podatki se uporabljajo za povečanje odgovorov LLM-a. LLM nato vrne odgovor na uporabnikovo vprašanje.

Arhitektura za RAG-e je implementirana z uporabo transformatorjev, ki sestojijo iz dveh delov: kodirnika in dekodirnika. Na primer, ko uporabnik postavi vprašanje, se vhodno besedilo 'kodira' v vektorje, ki zajemajo pomen besed, in vektorji se 'dekodirajo' v naš dokumentni indeks ter generirajo novo besedilo na podlagi uporabniškega vprašanja. LLM uporablja model kodirnik-dekodirnik za generiranje izhoda.

Dva pristopa pri implementaciji RAG-a po predlaganem članku: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sta:

- **_RAG-Sequence_** uporablja pridobljene dokumente za napovedovanje najboljšega možnega odgovora na uporabniško vprašanje

- **RAG-Token** uporablja dokumente za generiranje naslednjega znaka, nato jih pridobi za odgovor na uporabniško vprašanje

### Zakaj bi uporabljali RAG-e?

- **Bogastvo informacij:** zagotavlja, da so besedilni odgovori ažurni in aktualni. Zato izboljšuje zmogljivost pri nalogah, specifičnih za določeno področje, z dostopom do notranje baze znanja.

- Zmanjšuje izdelavo z uporabo **preverljivih podatkov** v bazi znanja za zagotavljanje konteksta uporabniškim vprašanjem.

- Je **stroškovno učinkovit**, saj so bolj ekonomični v primerjavi z fino nastavitvijo LLM-a.

## Ustvarjanje baze znanja

Naša aplikacija temelji na naših osebnih podatkih, tj. lekciji o nevronskih mrežah v učnem načrtu AI za začetnike.

### Vektorske baze podatkov

Vektorska baza podatkov, za razliko od tradicionalnih baz podatkov, je specializirana baza podatkov, zasnovana za shranjevanje, upravljanje in iskanje vektorskih predstavitev. Shranjuje številčne predstavitve dokumentov. Razdelitev podatkov na številčne vektorske predstavitve olajša našemu AI sistemu razumevanje in obdelavo podatkov.

Naše vektorske predstavitve shranjujemo v vektorskih bazah podatkov, saj imajo LLM-ji omejitev števila znakov, ki jih sprejmejo kot vhod. Ker ne morete posredovati celotnih vektorskih predstavitev LLM-u, jih bomo morali razdeliti na dele, in ko uporabnik postavi vprašanje, bodo vrnjene vektorske predstavitve, ki so najbolj podobne vprašanju, skupaj s pozivom. Razdelitev na dele tudi zmanjšuje stroške glede na število znakov, ki se posredujejo skozi LLM.

Nekatere priljubljene vektorske baze podatkov vključujejo Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant in DeepLake. Model Azure Cosmos DB lahko ustvarite z uporabo Azure CLI z naslednjim ukazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od besedila do vektorskih predstavitev

Preden shranimo naše podatke, jih bomo morali pretvoriti v vektorske predstavitve, preden jih shranimo v bazo podatkov. Če delate z velikimi dokumenti ali dolgimi besedili, jih lahko razdelite na podlagi pričakovanih vprašanj. Razdelitev lahko izvedete na ravni stavka ali odstavka. Ker razdelitev pridobiva pomene iz besed okoli njih, lahko dodate še nekaj konteksta k delu, na primer z dodajanjem naslova dokumenta ali vključitvijo besedila pred ali po delu. Podatke lahko razdelite na naslednji način:

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

Ko so razdeljeni, lahko nato vstavimo naše besedilo z uporabo različnih modelov vektorskih predstavitev. Nekateri modeli, ki jih lahko uporabite, vključujejo: word2vec, ada-002 s strani OpenAI, Azure Computer Vision in še več. Izbira modela bo odvisna od jezikov, ki jih uporabljate, vrste kodirane vsebine (besedilo/slike/zvok), velikosti vnosa, ki ga lahko kodira, in dolžine izhoda vektorske predstavitve.

Primer vstavljenega besedila z uporabo modela OpenAI `text-embedding-ada-002` je:
![vektorska predstavitev besede mačka](../../../translated_images/cat.3db013cbca4fd5d90438ea7b312ad0364f7686cf79931ab15cd5922151aea53e.sl.png)

## Pridobivanje in vektorsko iskanje

Ko uporabnik postavi vprašanje, ga retriver pretvori v vektor z uporabo kodirnika poizvedb, nato pa išče po našem indeksu iskanja dokumentov za ustrezne vektorje v dokumentu, ki so povezani z vhodom. Ko je to storjeno, pretvori tako vhodni vektor kot dokumentne vektorje v besedilo in jih posreduje skozi LLM.

### Pridobivanje

Pridobivanje se zgodi, ko sistem poskuša hitro najti dokumente iz indeksa, ki izpolnjujejo iskalna merila. Cilj retriverja je pridobiti dokumente, ki bodo uporabljeni za zagotavljanje konteksta in utemeljitev LLM-a na vaših podatkih.

Obstaja več načinov za iskanje znotraj naše baze podatkov, kot so:

- **Iskanje po ključnih besedah** - uporablja se za iskanje besedila

- **Semantično iskanje** - uporablja semantični pomen besed

- **Vektorsko iskanje** - pretvarja dokumente iz besedila v vektorske predstavitve z uporabo modelov vektorskih predstavitev. Pridobivanje bo izvedeno z iskanjem dokumentov, katerih vektorske predstavitve so najbližje uporabniškemu vprašanju.

- **Hibridno** - kombinacija iskanja po ključnih besedah in vektorskega iskanja.

Izziv pri pridobivanju se pojavi, ko v bazi podatkov ni podobnega odgovora na poizvedbo, sistem pa bo nato vrnil najboljše informacije, ki jih lahko dobi, vendar lahko uporabite taktike, kot so nastavitev največje razdalje za ustreznost ali uporaba hibridnega iskanja, ki združuje tako iskanje po ključnih besedah kot vektorsko iskanje. V tej lekciji bomo uporabili hibridno iskanje, kombinacijo vektorskega in iskanja po ključnih besedah. Naše podatke bomo shranili v podatkovni okvir s stolpci, ki vsebujejo dele in vektorske predstavitve.

### Vektorska podobnost

Retriver bo iskal po bazi znanja za vektorske predstavitve, ki so blizu skupaj, najbližji sosed, saj so to besedila, ki so podobna. V scenariju, ko uporabnik postavi poizvedbo, se ta najprej vstavi, nato pa se ujema s podobnimi vektorskimi predstavitvami. Običajna meritev, ki se uporablja za ugotavljanje, kako podobni so različni vektorji, je kosinusna podobnost, ki temelji na kotu med dvema vektorjema.

Podobnost lahko merimo z drugimi alternativami, ki jih lahko uporabimo, so Evklidska razdalja, ki je ravna črta med končnimi točkami vektorjev, in skalarni produkt, ki meri vsoto produktov ustreznih elementov dveh vektorjev.

### Iskalni indeks

Ko izvajamo pridobivanje, bomo morali zgraditi iskalni indeks za našo bazo znanja, preden izvedemo iskanje. Indeks bo shranil naše vektorske predstavitve in lahko hitro pridobil najbolj podobne dele tudi v veliki bazi podatkov. Naš indeks lahko ustvarimo lokalno z uporabo:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno rangiranje

Ko ste poizvedovali po bazi podatkov, boste morda morali rezultate razvrstiti od najbolj relevantnih. Ponovno rangiranje LLM uporablja strojno učenje za izboljšanje ustreznosti iskalnih rezultatov z njihovim urejanjem od najbolj relevantnih. Z uporabo Azure AI Search je ponovno rangiranje samodejno izvedeno za vas z uporabo semantičnega ponovnega rangiranja. Primer, kako ponovno rangiranje deluje z uporabo najbližjih sosedov:

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

Zadnji korak je dodajanje našega LLM-a v mešanico, da lahko dobimo odgovore, ki so utemeljeni na naših podatkih. To lahko implementiramo na naslednji način:

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

## Vrednotenje naše aplikacije

### Evalvacijske metrike

- Kakovost dobavljenih odgovorov, ki zagotavlja, da zvenijo naravno, tekoče in človeško.

- Utemeljenost podatkov: vrednotenje, ali je odgovor prišel iz dobavljenih dokumentov.

- Ustreznost: vrednotenje, ali odgovor ustreza in je povezan z zastavljenim vprašanjem.

- Tekočnost - ali odgovor smiselno zveni slovnično.

## Primeri uporabe RAG (Povečana generacija pridobivanja) in vektorskih baz podatkov

Obstaja veliko različnih primerov uporabe, kjer lahko klici funkcij izboljšajo vašo aplikacijo, kot so:

- Vprašanja in odgovori: utemeljevanje podatkov vašega podjetja v klepetu, ki ga lahko uporabljajo zaposleni za postavljanje vprašanj.

- Sistemi priporočil: kjer lahko ustvarite sistem, ki ujema najbolj podobne vrednosti, npr. filme, restavracije in še več.

- Storitve klepetalnih botov: lahko shranite zgodovino klepeta in prilagodite pogovor na podlagi uporabniških podatkov.

- Iskanje slik na podlagi vektorskih predstavitev, uporabno pri prepoznavanju slik in odkrivanju anomalij.

## Povzetek

Pokazali smo osnovna področja RAG, od dodajanja naših podatkov v aplikacijo, uporabniške poizvedbe in izhoda. Za poenostavitev ustvarjanja RAG lahko uporabite ogrodja, kot so Semanti Kernel, Langchain ali Autogen.

## Naloga

Za nadaljevanje učenja o Povečani generaciji pridobivanja (RAG) lahko zgradite:

- Zgradite sprednji del aplikacije z uporabo ogrodja po vaši izbiri.

- Uporabite ogrodje, bodisi LangChain ali Semanti Kernel, in ponovno ustvarite svojo aplikacijo.

Čestitamo za dokončanje lekcije 👏.

## Učenje se tukaj ne konča, nadaljujte potovanje

Po končani lekciji si oglejte našo [Generativno AI učno zbirko](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni AI!

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.