# Retrieval Augmented Generation (RAG) en Vector Databases

[![Retrieval Augmented Generation (RAG) en Vector Databases](../../../translated_images/nl/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

In de les over zoekapplicaties hebben we kort geleerd hoe je je eigen gegevens kunt integreren in Large Language Models (LLM's). In deze les gaan we dieper in op de concepten van het funderen van je gegevens in je LLM-toepassing, de werking van het proces en de methoden voor het opslaan van gegevens, inclusief zowel embeddings als tekst.

> **Video binnenkort beschikbaar**

## Introductie

In deze les behandelen we het volgende:

- Een introductie tot RAG, wat het is en waarom het wordt gebruikt in AI (kunstmatige intelligentie).

- Inzicht in wat vectordatabases zijn en het creëren van een database voor onze toepassing.

- Een praktisch voorbeeld hoe je RAG in een applicatie integreert.

## Leerdoelen

Na het voltooien van deze les kun je:

- De betekenis van RAG uitleggen bij het ophalen en verwerken van gegevens.

- Een RAG-toepassing opzetten en je gegevens funderen aan een LLM.

- Effectieve integratie van RAG en Vector Databases in LLM-toepassingen.

## Ons scenario: het verbeteren van onze LLM's met onze eigen gegevens

Voor deze les willen we onze eigen notities toevoegen aan de educatieve startup, zodat de chatbot meer informatie krijgt over de verschillende onderwerpen. Met behulp van de notities kunnen leerlingen beter studeren en de verschillende onderwerpen begrijpen, waardoor het eenvoudiger wordt om voor hun examens te leren. Voor ons scenario gebruiken we:

- `Azure OpenAI:` de LLM die we gebruiken om onze chatbot te creëren

- `AI for beginners' les over Neurale Netwerken`: dit wordt de data waarop we onze LLM funderen

- `Azure AI Search` en `Azure Cosmos DB:` vectordatabase om onze data op te slaan en een zoekindex te creëren

Gebruikers kunnen oefenquizzen maken van hun notities, revisiefiches en die samenvatten tot beknopte overzichten. Om te beginnen bekijken we wat RAG is en hoe het werkt:

## Retrieval Augmented Generation (RAG)

Een door een LLM aangedreven chatbot verwerkt gebruikersprompts om antwoorden te genereren. Het is ontworpen om interactief te zijn en communiceert met gebruikers over diverse onderwerpen. De antwoorden zijn echter beperkt tot de context die gegeven is en de fundamentele trainingsdata. Bijvoorbeeld, de kennis van GPT-4 stopt bij september 2021, wat betekent dat het geen kennis heeft van gebeurtenissen die daarna hebben plaatsgevonden. Daarnaast omvatten de gegevens die gebruikt worden om LLM's te trainen geen vertrouwelijke informatie zoals persoonlijke notities of een producthandleiding van een bedrijf.

### Hoe RAG's (Retrieval Augmented Generation) werken

![tekening die laat zien hoe RAG's werken](../../../translated_images/nl/how-rag-works.f5d0ff63942bd3a6.webp)

Stel dat je een chatbot wilt inzetten die quizzen maakt van je notities, dan heb je een verbinding nodig met de kennisbank. Dit is waar RAG te hulp komt. RAG's werken als volgt:

- **Kennisbank:** Voordat er gezocht kan worden, moeten deze documenten worden ingelezen en voorbewerkt, meestal door grote documenten op te splitsen in kleinere stukken, die omgezet worden in tekstembeddings en opgeslagen in een database.

- **Gebruikersvraag:** de gebruiker stelt een vraag

- **Ophalen:** Wanneer een gebruiker een vraag stelt, haalt het embeddingmodel relevante informatie uit onze kennisbank om meer context te bieden die in de prompt wordt verwerkt.

- **Aangevulde generatie:** de LLM verbetert zijn antwoord op basis van de opgehaalde data. Dit maakt het mogelijk dat het antwoord niet alleen gebaseerd is op voorgetrainde data, maar ook op relevante informatie uit de toegevoegde context. De opgehaalde data wordt gebruikt om de antwoorden van de LLM aan te vullen. Daarna geeft de LLM een antwoord op de vraag van de gebruiker.

![diagram die de architectuur van RAG's toont](../../../translated_images/nl/encoder-decode.f2658c25d0eadee2.webp)

De architectuur voor RAG's wordt geïmplementeerd met transformers die bestaan uit twee delen: een encoder en een decoder. Wanneer een gebruiker een vraag stelt, wordt de invoertekst 'geëncodeerd' in vectoren die de betekenis van woorden vastleggen, en worden die vectoren 'gedecodeerd' in onze documentindex en wordt er nieuwe tekst gegenereerd op basis van de gebruikersvraag. De LLM gebruikt een encoder-decoder model om de output te genereren.

Twee benaderingen bij het implementeren van RAG volgens het voorgestelde artikel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) zijn:

- **_RAG-Sequence_** waarbij opgehaalde documenten worden gebruikt om het best mogelijke antwoord op een gebruikersvraag te voorspellen

- **RAG-Token** waarbij documenten worden gebruikt om het volgende token te genereren, en dan worden opgehaald om de gebruikersvraag te beantwoorden

### Waarom zou je RAG gebruiken? 

- **Informatierijkdom:** zorgt ervoor dat tekstuele antwoorden actueel en up-to-date zijn. Het verbetert dus de prestaties op domeinspecifieke taken door toegang tot de interne kennisbank te bieden.

- Vermindert verzinsels door gebruik te maken van **verifieerbare data** in de kennisbank om context te bieden voor de gebruikersvragen.

- Het is **kosteneffectief** omdat het goedkoper is in vergelijking met het bijschaven van een LLM.

## Een kennisbank creëren

Onze toepassing is gebaseerd op onze persoonlijke data, bijvoorbeeld de les Neurale Netwerken uit het AI For Beginners-curriculum.

### Vector Databases

Een vectordatabase is, in tegenstelling tot traditionele databases, een gespecialiseerde database ontworpen om embedded vectoren op te slaan, beheren en doorzoeken. Het slaat numerieke representaties van documenten op. Door data om te zetten naar numerieke embeddings kan ons AI-systeem de data beter begrijpen en verwerken.

We slaan onze embeddings op in vectordatabases omdat LLM's een limiet hebben van het aantal tokens dat ze als invoer accepteren. Omdat je niet de gehele embedding aan een LLM kunt doorgeven, zullen we ze moeten opsplitsen in stukken en wanneer een gebruiker een vraag stelt, worden de embeddings die het meest op de vraag lijken teruggegeven samen met de prompt. Deze opsplitsing verlaagt ook de kosten voor het aantal tokens dat door een LLM wordt verwerkt.

Enkele populaire vectordatabases zijn Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant en DeepLake. Je kunt een Azure Cosmos DB-model maken met Azure CLI met de volgende opdracht:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Van tekst naar embeddings

Voordat we onze data opslaan, moeten we deze omzetten naar vector embeddings. Als je met grote documenten of lange teksten werkt, kun je ze opdelen in stukken op basis van verwachte vragen. Opsplitsen kan op zinsniveau of op alinea niveau. Omdat een stuk de betekenis afleidt uit de woorden rondom, kun je wat extra context aan een stuk toevoegen, bijvoorbeeld door de titel van het document toe te voegen of wat tekst vóór of na het stuk mee te nemen. Je kunt de data als volgt opsplitsen:

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

    # Als het laatste stuk de minimale lengte niet bereikte, voeg het dan toch toe
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Als we de stukken hebben, kunnen we onze tekst embedden met verschillende embeddingmodellen. Enkele modellen die je kunt gebruiken zijn: word2vec, ada-002 van OpenAI, Azure Computer Vision en nog veel meer. Het kiezen van een model hangt af van de talen die je gebruikt, het type inhoud dat wordt gecodeerd (tekst/afbeeldingen/audio), de grootte van de invoer die het kan coderen en de lengte van de embedding-output.

Een voorbeeld van embedded tekst met behulp van het `text-embedding-ada-002` model van OpenAI is:
![een embedding van het woord kat](../../../translated_images/nl/cat.74cbd7946bc9ca38.webp)

## Ophalen en Vectorzoektocht

Wanneer een gebruiker een vraag stelt, zet de retriever deze om in een vector met de query-encoder, daarna zoekt het voor relevante vectoren in onze documentzoekindex die gerelateerd zijn aan de invoer. Als dat gebeurd is, zet het zowel de invoervector als de documentvectoren om naar tekst en stuurt dit door naar de LLM.

### Ophalen

Ophalen gebeurt wanneer het systeem snel de documenten zoekt in de index die voldoen aan de zoekcriteria. Het doel van de retriever is documenten te vinden die context bieden en de LLM funderen op jouw data.

Er zijn verschillende manieren om te zoeken in onze database, zoals:

- **Zoeken op trefwoord** - gebruikt voor tekstzoekopdrachten

- **Vectorzoektocht** - zet documenten om van tekst naar vectorrepresentaties met embeddingmodellen, wat een **semantische zoekopdracht** mogelijk maakt op basis van de betekenis van woorden. Ophalen gebeurt door te zoeken naar documenten waarvan de vectorrepresentaties het dichtst bij de gebruikersvraag liggen.

- **Hybride** - een combinatie van trefwoord- en vectorzoektocht.

Een uitdaging bij ophalen ontstaat wanneer er geen vergelijkbaar antwoord op de vraag in de database is. Het systeem zal dan de best mogelijke informatie teruggeven, maar je kunt tactieken inzetten zoals het instellen van een maximale afstand voor relevantie of het gebruik van hybride zoekopdrachten die zowel trefwoorden als vectoren combineren. In deze les gebruiken we hybride zoekopdrachten, een combinatie van vector- en trefwoordzoekopdrachten. We slaan onze data op in een dataframe met kolommen die de stukken en embeddings bevatten.

### Vectorvergelijking

De retriever zoekt in de kennisdatabase naar embeddings die dicht bij elkaar liggen, de dichtstbijzijnde buren, omdat dit teksten zijn die vergelijkbaar zijn. In het scenario waarin een gebruiker een vraag stelt, wordt deze eerst omgezet in een embedding en dan gematcht met vergelijkbare embeddings. De gebruikelijke maatstaf om te bepalen hoe vergelijkbaar verschillende vectoren zijn, is cosine similarity die gebaseerd is op de hoek tussen twee vectoren.

We kunnen gelijkenis ook meten met andere methoden zoals Euclidische afstand, wat de rechte lijn is tussen vector-eindpunten, en dotproduct, dat de som van de producten van overeenkomende elementen van twee vectoren meet.

### Zoekindex

Bij ophalen moeten we een zoekindex voor onze kennisbank bouwen vóór we de zoekopdracht uitvoeren. Een index slaat onze embeddings op en kan snel de meest vergelijkbare stukken terughalen, ook in een grote database. We kunnen onze index lokaal creëren met:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Maak de zoekindex aan
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Om de index te doorzoeken, kunt u de kneighbors-methode gebruiken
distances, indices = nbrs.kneighbors(embeddings)
```

### Herordenen

Nadat je de database hebt gequeryd, wil je mogelijk de resultaten sorteren op relevantie. Een herordende LLM gebruikt Machine Learning om de relevantie van zoekresultaten te verbeteren door ze te rangschikken van meest relevant. Met Azure AI Search wordt het herordenen automatisch voor je gedaan met een semantische herorderaar. Een voorbeeld van hoe herordenen werkt met de dichtstbijzijnde buren:

```python
# Zoek de meest vergelijkbare documenten
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Druk de meest vergelijkbare documenten af
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Alles samenbrengen

De laatste stap is onze LLM toevoegen aan het geheel om antwoorden te krijgen die gefundeerd zijn op onze data. Dit kunnen we als volgt implementeren:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Zet de vraag om in een queryvector
    query_vector = create_embeddings(user_input)

    # Vind de meest vergelijkbare documenten
    distances, indices = nbrs.kneighbors([query_vector])

    # voeg documenten toe aan de query om context te bieden
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combineer de geschiedenis en de gebruikersinvoer
    history.append(user_input)

    # maak een berichtobject aan
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # gebruik de Responses API om een reactie te genereren
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Onze toepassing evalueren

### Evaluatiecriteria

- Kwaliteit van gegeven antwoorden, waarbij wordt verzekerd dat het natuurlijk, vloeiend en menselijk klinkt

- Fundering van de data: evalueren of het antwoord afkomstig is van de geleverde documenten

- Relevantie: beoordelen of het antwoord overeenkomt met en gerelateerd is aan de gestelde vraag

- Vloeiendheid - of het antwoord grammaticaal logisch is

## Toepassingen van RAG (Retrieval Augmented Generation) en vectordatabases

Er zijn vele gebruikssituaties waarin functieaanroepen je app kunnen verbeteren, zoals:

- Vraag en Antwoord: je bedrijfsdata funderen aan een chat die door medewerkers kan worden gebruikt om vragen te stellen.

- Aanbevelingssystemen: waarmee je een systeem kunt creëren dat de meest vergelijkbare waarden matcht, bijvoorbeeld films, restaurants en meer.

- Chatbotdiensten: je kunt chatgeschiedenis opslaan en het gesprek personaliseren op basis van gebruikersdata.

- Beeldzoeken op basis van vectorembeddings, nuttig bij beeldherkenning en detectie van afwijkingen.

## Samenvatting

We hebben de fundamentele gebieden van RAG behandeld, van het toevoegen van onze data aan de applicatie, de gebruikersvraag tot de output. Om het creëren van RAG te vereenvoudigen, kun je frameworks gebruiken zoals Semanti Kernel, Langchain of Autogen.

## Opdracht

Om je kennis over Retrieval Augmented Generation (RAG) voort te zetten, kun je bouwen aan:

- Een front-end voor de applicatie met het framework van jouw keuze

- Gebruik maken van een framework, zoals LangChain of Semantic Kernel, en je applicatie recreëren.

Gefeliciteerd met het afronden van de les 👏.

## Het leren stopt hier niet, zet je reis voort

Na het voltooien van deze les, bekijk onze [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generative AI verder te verdiepen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->