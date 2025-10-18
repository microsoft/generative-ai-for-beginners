<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-18T01:41:41+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sl"
}
-->
# Pridobivanje z dodatno generacijo (RAG) in vektorske baze podatkov

[![Pridobivanje z dodatno generacijo (RAG) in vektorske baze podatkov](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.sl.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

V lekciji o aplikacijah za iskanje smo na kratko spoznali, kako vključiti lastne podatke v velike jezikovne modele (LLM). V tej lekciji se bomo podrobneje posvetili konceptom utemeljevanja vaših podatkov v aplikaciji LLM, mehaniki procesa in metodam za shranjevanje podatkov, vključno z vektorskimi predstavitvami in besedilom.

> **Video prihaja kmalu**

## Uvod

V tej lekciji bomo obravnavali naslednje:

- Uvod v RAG, kaj je in zakaj se uporablja v umetni inteligenci (AI).

- Razumevanje, kaj so vektorske baze podatkov, in ustvarjanje ene za našo aplikacijo.

- Praktičen primer, kako vključiti RAG v aplikacijo.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Razložili pomen RAG pri pridobivanju in obdelavi podatkov.

- Nastavili aplikacijo RAG in utemeljili svoje podatke v LLM.

- Učinkovito vključili RAG in vektorske baze podatkov v aplikacije LLM.

## Naš scenarij: izboljšanje naših LLM-jev z lastnimi podatki

V tej lekciji želimo dodati lastne zapiske v izobraževalni startup, ki chatbotu omogočajo pridobivanje več informacij o različnih temah. Z uporabo naših zapiskov bodo učenci lahko bolje študirali in razumeli različne teme, kar jim bo olajšalo pripravo na izpite. Za ustvarjanje našega scenarija bomo uporabili:

- `Azure OpenAI:` LLM, ki ga bomo uporabili za ustvarjanje našega chatbota

- `Lekcija za začetnike o nevronskih mrežah:` to bodo podatki, na katerih bomo utemeljili naš LLM

- `Azure AI Search` in `Azure Cosmos DB:` vektorska baza podatkov za shranjevanje naših podatkov in ustvarjanje iskalnega indeksa

Uporabniki bodo lahko ustvarili vadbene kvize iz svojih zapiskov, kartice za ponavljanje in jih povzemali v jedrnate preglede. Za začetek si poglejmo, kaj je RAG in kako deluje:

## Pridobivanje z dodatno generacijo (RAG)

Chatbot, ki ga poganja LLM, obdeluje uporabniške zahteve za generiranje odgovorov. Zasnovan je tako, da je interaktiven in se ukvarja z uporabniki na širokem spektru tem. Vendar pa so njegovi odgovori omejeni na kontekst, ki ga zagotavljajo osnovni podatki za usposabljanje. Na primer, GPT-4 ima omejitev znanja do septembra 2021, kar pomeni, da mu primanjkuje znanja o dogodkih, ki so se zgodili po tem obdobju. Poleg tega podatki, uporabljeni za usposabljanje LLM-jev, izključujejo zaupne informacije, kot so osebni zapiski ali priročnik za izdelke podjetja.

### Kako delujejo RAG (Pridobivanje z dodatno generacijo)

![diagram, ki prikazuje, kako delujejo RAG](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.sl.png)

Recimo, da želite namestiti chatbot, ki ustvarja kvize iz vaših zapiskov, potrebovali boste povezavo z bazo znanja. Tukaj pride RAG na pomoč. RAG deluje na naslednji način:

- **Baza znanja:** Pred pridobivanjem je treba te dokumente uvoziti in predhodno obdelati, običajno z razdelitvijo velikih dokumentov na manjše dele, pretvorbo v vektorske predstavitve in shranjevanje v bazo podatkov.

- **Uporabniška zahteva:** Uporabnik postavi vprašanje.

- **Pridobivanje:** Ko uporabnik postavi vprašanje, model za vektorsko predstavitev pridobi ustrezne informacije iz naše baze znanja, da zagotovi več konteksta, ki bo vključen v zahtevo.

- **Dodatna generacija:** LLM izboljša svoj odgovor na podlagi pridobljenih podatkov. To omogoča, da je generiran odgovor ne le temelječ na predhodno usposobljenih podatkih, temveč tudi na ustreznih informacijah iz dodanega konteksta. Pridobljeni podatki se uporabljajo za izboljšanje odgovorov LLM. LLM nato vrne odgovor na uporabnikovo vprašanje.

![diagram, ki prikazuje arhitekturo RAG](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.sl.png)

Arhitektura RAG je implementirana z uporabo transformatorjev, ki sestojijo iz dveh delov: kodirnika in dekodirnika. Na primer, ko uporabnik postavi vprašanje, se vhodno besedilo 'kodira' v vektorje, ki zajemajo pomen besed, in vektorji se 'dekodirajo' v naš indeks dokumentov ter generirajo novo besedilo na podlagi uporabniške zahteve. LLM uporablja tako kodirni-dekodirni model za generiranje izhoda.

Dva pristopa pri implementaciji RAG, kot je predlagano v članku: [Pridobivanje z dodatno generacijo za naloge NLP (obdelava naravnega jezika)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst), sta:

- **_RAG-Sequence_** uporaba pridobljenih dokumentov za napovedovanje najboljšega možnega odgovora na uporabniško zahtevo

- **RAG-Token** uporaba dokumentov za generiranje naslednjega tokena, nato pa njihovo pridobivanje za odgovor na uporabniško zahtevo

### Zakaj bi uporabljali RAG? 

- **Bogastvo informacij:** zagotavlja, da so besedilni odgovori posodobljeni in aktualni. Zato izboljšuje zmogljivost pri nalogah, specifičnih za določeno področje, z dostopom do notranje baze znanja.

- Zmanjšuje izmišljanje z uporabo **preverljivih podatkov** v bazi znanja za zagotavljanje konteksta uporabniškim zahtevam.

- Je **stroškovno učinkovit**, saj je bolj ekonomičen v primerjavi z dodatnim usposabljanjem LLM.

## Ustvarjanje baze znanja

Naša aplikacija temelji na naših osebnih podatkih, tj. lekciji o nevronskih mrežah iz učnega načrta AI za začetnike.

### Vektorske baze podatkov

Vektorska baza podatkov, za razliko od tradicionalnih baz podatkov, je specializirana baza podatkov, zasnovana za shranjevanje, upravljanje in iskanje vektorskih predstavitev. Shranjuje numerične predstavitve dokumentov. Razčlenitev podatkov na numerične vektorske predstavitve olajša razumevanje in obdelavo podatkov našemu AI sistemu.

Vektorske predstavitve shranjujemo v vektorskih bazah podatkov, saj imajo LLM-ji omejitev števila tokenov, ki jih sprejmejo kot vhod. Ker ne morete posredovati celotnih vektorskih predstavitev LLM-ju, jih bomo morali razdeliti na dele, in ko uporabnik postavi vprašanje, se vrnejo vektorske predstavitve, ki so najbolj podobne vprašanju, skupaj z zahtevo. Razdelitev na dele tudi zmanjša stroške glede števila tokenov, ki jih posredujemo LLM-ju.

Nekatere priljubljene vektorske baze podatkov vključujejo Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant in DeepLake. Model Azure Cosmos DB lahko ustvarite z uporabo Azure CLI z naslednjim ukazom:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od besedila do vektorskih predstavitev

Preden shranimo naše podatke, jih moramo pretvoriti v vektorske predstavitve, preden jih shranimo v bazo podatkov. Če delate z velikimi dokumenti ali dolgimi besedili, jih lahko razdelite glede na zahteve, ki jih pričakujete. Razdelitev lahko izvedete na ravni stavka ali odstavka. Ker razdelitev izhaja iz pomenov besed okoli njih, lahko dodate nekaj drugega konteksta k delu, na primer z dodajanjem naslova dokumenta ali vključitvijo besedila pred ali po delu. Podatke lahko razdelite na naslednji način:

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

Ko so podatki razdeljeni, jih lahko nato kodiramo z različnimi modeli za vektorske predstavitve. Nekateri modeli, ki jih lahko uporabite, vključujejo: word2vec, ada-002 od OpenAI, Azure Computer Vision in mnoge druge. Izbira modela bo odvisna od jezikov, ki jih uporabljate, vrste kodirane vsebine (besedilo/slike/zvok), velikosti vhodnih podatkov, ki jih lahko kodira, in dolžine izhoda vektorske predstavitve.

Primer kodiranega besedila z uporabo modela OpenAI `text-embedding-ada-002` je:
![vektorska predstavitev besede mačka](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.sl.png)

## Pridobivanje in vektorsko iskanje

Ko uporabnik postavi vprašanje, iskalnik to pretvori v vektor z uporabo kodirnika za zahteve, nato pa išče po našem iskalnem indeksu dokumentov za ustrezne vektorje v dokumentu, ki so povezani z vhodom. Ko je to opravljeno, pretvori tako vhodni vektor kot vektorje dokumentov v besedilo in jih posreduje LLM-ju.

### Pridobivanje

Pridobivanje se zgodi, ko sistem poskuša hitro najti dokumente iz indeksa, ki ustrezajo iskalnim kriterijem. Cilj iskalnika je pridobiti dokumente, ki bodo uporabljeni za zagotavljanje konteksta in utemeljitev LLM-ja na vaših podatkih.

Obstaja več načinov za iskanje znotraj naše baze podatkov, kot so:

- **Iskanje po ključnih besedah** - uporablja se za iskanje besedila.

- **Semantično iskanje** - uporablja semantični pomen besed.

- **Vektorsko iskanje** - pretvori dokumente iz besedila v vektorske predstavitve z uporabo modelov za kodiranje. Pridobivanje se izvede z iskanjem dokumentov, katerih vektorske predstavitve so najbližje uporabniškemu vprašanju.

- **Hibridno** - kombinacija iskanja po ključnih besedah in vektorskega iskanja.

Izziv pri pridobivanju nastane, ko v bazi podatkov ni podobnega odgovora na zahtevo, sistem pa nato vrne najboljše informacije, ki jih lahko najde. Vendar pa lahko uporabite taktike, kot so nastavitev največje razdalje za ustreznost ali uporaba hibridnega iskanja, ki združuje iskanje po ključnih besedah in vektorsko iskanje. V tej lekciji bomo uporabili hibridno iskanje, kombinacijo vektorskega in iskanja po ključnih besedah. Naše podatke bomo shranili v podatkovni okvir s stolpci, ki vsebujejo dele besedila in vektorske predstavitve.

### Vektorska podobnost

Iskalnik bo iskal po bazi znanja za vektorske predstavitve, ki so si med seboj blizu, najbližji sosed, saj so to besedila, ki so si podobna. V scenariju, ko uporabnik postavi zahtevo, se ta najprej kodira, nato pa se ujema s podobnimi vektorskimi predstavitvami. Pogosta metoda za merjenje podobnosti med različnimi vektorji je kosinusna podobnost, ki temelji na kotu med dvema vektorjema.

Za merjenje podobnosti lahko uporabimo tudi druge alternative, kot so Evklidska razdalja, ki je ravna črta med končnimi točkami vektorjev, in skalarni produkt, ki meri vsoto produktov ustreznih elementov dveh vektorjev.

### Iskalni indeks

Pri pridobivanju bomo morali zgraditi iskalni indeks za našo bazo znanja, preden izvedemo iskanje. Indeks bo shranil naše vektorske predstavitve in lahko hitro pridobil najbolj podobne dele, tudi v veliki bazi podatkov. Naš indeks lahko lokalno ustvarimo z:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponovno razvrščanje

Ko ste poizvedovali po bazi podatkov, boste morda morali rezultate razvrstiti po ustreznosti. LLM za ponovno razvrščanje uporablja strojno učenje za izboljšanje ustreznosti rezultatov iskanja z razvrščanjem od najbolj ustreznih. Z uporabo Azure AI Search se ponovno razvrščanje samodejno izvede za vas z uporabo semantičnega razvrščevalnika. Primer, kako deluje ponovno razvrščanje z uporabo najbližjih sosedov:

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

Zadnji korak je dodajanje našega LLM v mešanico, da bi lahko dobili odgovore, ki temeljijo na naših podatkih. To lahko implementiramo na naslednji način:

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

### Merila vrednotenja

- Kakovost podanih odgovorov, ki zagotavlja, da zvenijo naravno, tekoče in človeško.

- Utemeljenost podatkov: ocenjevanje, ali je odgovor prišel iz podanih dokumentov.

- Ustreznost: ocenjevanje, ali se odgovor ujema in je povezan z zastavljenim vprašanjem.

- Tekočnost - ali je odgovor slovnično smiseln.

## Primeri uporabe RAG (Pridobivanje z dodatno generacijo) in vektorskih baz podatkov

Obstaja veliko različnih primerov uporabe, kjer lahko klici funkcij izboljšajo vašo aplikacijo, kot so:

- Vprašanja in odgovori: utemeljitev podatkov vašega podjetja v klepetu, ki ga lahko zaposleni uporabljajo za postavljanje vprašanj.

- Sistemi priporočil: kjer lahko ustvarite sistem, ki ujema najbolj podobne vrednosti, npr. filme, restavracije in še veliko več.

- Storitev chatbotov: lahko shranite zgodovino klepeta in prilagodite pogovor na podlagi uporabniških podatkov.

- Iskanje slik na podlagi vektorskih predstavitev, uporabno pri prepoznavanju slik in zaznavanju anomalij.

## Povzetek

Pokazali smo temeljna področja RAG od dodajanja naših podatkov v aplikacijo, uporabniške zahteve in izhoda. Za poenostavitev ustvarjanja RAG lahko uporabite ogrodja, kot so Semantic Kernel, Langchain ali Autogen.

## Naloga

Za nadaljevanje učenja o Pridobivanju z dodatno generacijo (RAG) lahko ustvarite:

- Ustvarite uporabniški vmesnik za aplikacijo z uporabo izbranega ogrodja.

- Uporabite ogrodje, bodisi LangChain ali Semantic Kernel, in ponovno ustvarite svojo aplikacijo.

Čestitke za zaključek lekcije 👏.

## Učenje se tukaj ne konča, nadaljujte pot

Po zaključku te lekcije si oglejte našo [Zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.