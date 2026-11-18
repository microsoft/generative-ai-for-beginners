# Retrieval Augmented Generation (RAG) en Vector Databases

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../translated_images/nl/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

In de les over zoektoepassingen hebben we kort geleerd hoe je je eigen data kunt integreren in Large Language Models (LLM's). In deze les gaan we dieper in op de concepten van het verankeren van je data in je LLM-applicatie, de werking van het proces en de methoden voor het opslaan van data, inclusief zowel embeddings als tekst.

> **Video binnenkort beschikbaar**

## Introductie

In deze les behandelen we het volgende:

- Een introductie tot RAG, wat het is en waarom het wordt gebruikt in AI (kunstmatige intelligentie).

- Begrijpen wat vector databases zijn en er een aanmaken voor onze applicatie.

- Een praktisch voorbeeld over hoe je RAG in een applicatie integreert.

## Leerdoelen

Na het voltooien van deze les ben je in staat om:

- Het belang van RAG in dataretrieval en verwerking uit te leggen.

- Een RAG-applicatie op te zetten en een LLM te verankeren met je data

- RAG en vector databases effectief te integreren in LLM-toepassingen.

## Onze situatie: het verbeteren van onze LLM's met onze eigen data

Voor deze les willen we onze eigen aantekeningen toevoegen aan de educatieve startup, zodat de chatbot meer informatie krijgt over de verschillende onderwerpen. Met behulp van de aantekeningen kunnen leerlingen beter studeren en de verschillende onderwerpen begrijpen, waardoor het makkelijker wordt om voor hun examens te leren. Om onze situatie te creëren, gebruiken we:

- `Azure OpenAI:` de LLM die we zullen gebruiken om onze chatbot te maken

- `AI for beginners' lesson on Neural Networks`: dit wordt de data waarop we onze LLM verankeren

- `Azure AI Search` en `Azure Cosmos DB:` vector database om onze data op te slaan en een zoekindex te maken

Gebruikers kunnen oefenquizzen en revisie-flashcards maken van hun aantekeningen en deze aantekeningen samenvatten in beknopte overzichten. Laten we om te beginnen kijken wat RAG is en hoe het werkt:

## Retrieval Augmented Generation (RAG)

Een LLM-aangedreven chatbot verwerkt gebruikersprompts om reacties te genereren. Het is ontworpen om interactief te zijn en gaat in gesprek met gebruikers over een breed scala van onderwerpen. Echter, de reacties zijn beperkt tot de geleverde context en de onderliggende trainingsdata. Bijvoorbeeld, GPT-4's kennis loopt tot september 2021, wat betekent dat het geen kennis heeft van gebeurtenissen die daarna plaatsvonden. Daarnaast sluiten de data die voor het trainen van LLM's wordt gebruikt vertrouwelijke informatie uit, zoals persoonlijke aantekeningen of een bedieningshandleiding van een bedrijf.

### Hoe RAGs (Retrieval Augmented Generation) werken

![tekening die toont hoe RAGs werken](../../../translated_images/nl/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Stel dat je een chatbot wilt inzetten die quizzen maakt van je aantekeningen, dan is er een verbinding met de kennisbasis nodig. Hier komt RAG van pas. RAGs werken als volgt:

- **Kennisbasis:** Voordat er gezocht kan worden, moeten deze documenten worden ingeladen en voorbewerkt, meestal door grote documenten op te splitsen in kleinere stukken, ze om te zetten naar tekst-embeddings en op te slaan in een database.

- **Gebruikersvraag:** de gebruiker stelt een vraag

- **Opvraging:** Wanneer een gebruiker een vraag stelt, haalt het embeddingmodel relevante informatie op uit onze kennisbasis om meer context te bieden die in de prompt wordt verwerkt.

- **Uitgebreide generatie:** de LLM verbetert zijn antwoord op basis van de opgehaalde data. Dit maakt het mogelijk dat het antwoord niet alleen gebaseerd is op vooraf getrainde data, maar ook op relevante informatie uit de toegevoegde context. De opgehaalde data wordt gebruikt om de antwoorden van de LLM uit te breiden. De LLM geeft vervolgens een antwoord op de vraag van de gebruiker.

![Diagram dat de RAG-architectuur toont](../../../translated_images/nl/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG combineert een retriever met een generator: de vraag wordt omgezet in een vector, vergeleken met de documentindex om relevante tekststukken te vinden, en die stukken worden als context aan een LLM aangeboden, welke het antwoord genereert. De retriever en generator kunnen verschillende modellen gebruiken; RAG vereist geen encoder-decoder transformer.

Twee benaderingen bij het implementeren van RAG volgens het voorgestelde artikel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) zijn:

- **_RAG-Sequence_** waarbij opgehaalde documenten worden gebruikt om het best mogelijke antwoord op een gebruikersvraag te voorspellen

- **RAG-Token** waarbij documenten worden gebruikt om de volgende token te genereren, en deze daarna te gebruiken om de vraag van de gebruiker te beantwoorden

### Waarom zou je RAGs gebruiken?

- **Informatierijkdom:** zorgt ervoor dat tekstuele antwoorden up-to-date en actueel zijn. Het verbetert daarom de prestaties bij domeinspecifieke taken door toegang te bieden tot de interne kennisbasis.

- Vermindert verzinsels door gebruik te maken van **verifieerbare data** in de kennisbasis om context te bieden bij gebruikersvragen.

- Het is **kosteneffectief**, omdat het goedkoper is dan het fijn afstemmen van een LLM

## Een kennisbasis aanmaken

Onze applicatie is gebaseerd op onze persoonlijke data, namelijk de Neural Network les uit het AI voor Beginners-curriculum.

### Vector Databases

Een vector database is, in tegenstelling tot traditionele databases, een gespecialiseerde database die is ontworpen om ingesloten vectoren op te slaan, beheren en zoeken. Het slaat numerieke representaties van documenten op. Door data op te splitsen in numerieke embeddings wordt het makkelijker voor ons AI-systeem om de data te begrijpen en te verwerken.

Omdat LLM's een limiet hebben voor het aantal invoertokens, splitsen we documenten op in stukken voordat we ze embedden. Wanneer een gebruiker een vraag stelt, identificeren de embeddings die het meest lijken op de query de relevante tekststukken, die samen met de prompt worden teruggegeven. Door op te splitsen verminderen we ook het aantal tokens dat aan de LLM wordt doorgegeven en kunnen zo kosten worden bespaard.

Enkele populaire vector databases zijn Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant en DeepLake. Je kunt een Azure Cosmos DB-model maken met de Azure CLI met het volgende commando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Van tekst naar embeddings

Voordat we onze data opslaan, moeten we ze eerst omzetten naar vector embeddings. Als je met grote documenten of lange teksten werkt, kun je ze opdelen op basis van verwachte vragen. Het opdelen kan op zinsniveau of op alinea niveau. Omdat segmentatie betekenis haalt uit de woorden eromheen, kun je extra context toevoegen aan een segment, bijvoorbeeld door de documenttitel toe te voegen of wat tekst vóór of na het segment. Je kunt de data als volgt opdelen:

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

Eenmaal opgedeeld kunnen we onze tekst embedden met verschillende embeddingmodellen. Enkele modellen die je kunt gebruiken zijn: word2vec, ada-002 van OpenAI, Azure Computer Vision en vele anderen. De keuze voor een model hangt af van de gebruikte talen, het type gecodeerde inhoud (tekst/afbeeldingen/audio), de grootte van de input die het kan coderen en de lengte van de embedding output.

Een voorbeeld van een embedded tekst met het OpenAI-model `text-embedding-ada-002` is:
![een embedding van het woord kat](../../../translated_images/nl/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Opvraging en Vectorzoektocht

Wanneer een gebruiker een vraag stelt, zet de retriever deze om in een vector met behulp van de query-encoder, en zoekt vervolgens in onze documentzoekindex naar relevante vectoren in het document die gerelateerd zijn aan de invoer. Daarna zet het zowel de invoervector als de documentvectoren om in tekst en voert deze door de LLM.

### Opvraging

Opvraging gebeurt wanneer het systeem probeert snel documenten uit de index te vinden die voldoen aan de zoekcriteria. Het doel van de retriever is om documenten te vinden die gebruikt worden om context te bieden en de LLM te verankeren in jouw data.

Er zijn verschillende manieren om te zoeken binnen onze database, zoals:

- **Zoeken op trefwoord** - gebruikt voor tekstzoekopdrachten

- **Vectorzoektocht** - zet documenten om van tekst naar vectorrepresentaties met behulp van embeddingmodellen, wat een **semantische zoekopdracht** mogelijk maakt op basis van de betekenis van woorden. Opvraging gebeurt door te zoeken naar documenten waarvan de vectorrepresentaties het dichtst bij de gebruikersvraag liggen.

- **Hybride** - een combinatie van zowel trefwoord- als vectorzoektocht.

Een uitdaging bij opvraging ontstaat wanneer er geen vergelijkbaar antwoord op de query in de database staat, dan geeft het systeem de best mogelijke informatie terug. Je kunt tactieken toepassen zoals het instellen van de maximale afstand voor relevantie of een hybride zoekopdracht die zowel trefwoord- als vectorzoektocht combineert. In deze les gebruiken we hybride zoekopdracht, een combinatie van vector- en trefwoordzoeken. We slaan onze data op in een dataframe met kolommen die de stukken en de embeddings bevatten.

### Vectorovereenkomst

De retriever zoekt in de kennisdatabase naar embeddings die dicht bij elkaar liggen—de dichtstbijzijnde buren—omdat deze teksten vertegenwoordigen die vergelijkbaar zijn. In dit scenario wordt bij het indienen van een query eerst een embedding gemaakt die vervolgens wordt gematcht met gelijksoortige embeddings. De meest gebruikte maatstaf om vectorovereenkomst te meten is cosinusafstand, die gebaseerd is op de hoek tussen twee vectoren.

Andere metrics die we kunnen gebruiken om overeenkomst te meten zijn Euclidische afstand, de rechte lijn tussen vector-eindpunten, en het dotproduct, dat de som meet van de producten van overeenkomstige elementen in twee vectoren.

### Zoekindex

Bij het uitvoeren van opvraging moeten we eerst een zoekindex voor onze kennisbasis bouwen. Een index slaat onze embeddings op en kan snel de meest vergelijkbare stukken terugvinden, zelfs in een grote database. We kunnen onze index lokaal maken met:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Herordenen

Nadat je de database hebt bevraagd, moet je mogelijk de resultaten sorteren van meest relevant naar minder relevant. Een herordende LLM maakt gebruik van Machine Learning om de relevantie van zoekresultaten te verbeteren door ze te ordenen van meest relevant. Met Azure AI Search wordt herordening automatisch voor je gedaan met een semantische herordener. Een voorbeeld van hoe herordenen werkt met de dichtstbijzijnde buren:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Alles samenbrengen

De laatste stap is het toevoegen van onze LLM zodat we antwoorden kunnen krijgen die gebaseerd zijn op onze data. We kunnen het als volgt implementeren:

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

## Onze applicatie evalueren

### Evaluatiematen

- Kwaliteit van de geleverde antwoorden, zodat het natuurlijk, vloeiend en menselijk klinkt

- Verankering van de data: evalueren of het antwoord afkomstig is van de aangeleverde documenten

- Relevantie: evalueren of het antwoord overeenkomt en gerelateerd is aan de gestelde vraag

- Vloeiendheid - of het antwoord grammaticaal klopt

## Gebruikssituaties voor het gebruik van RAG (Retrieval Augmented Generation) en vector databases

Er zijn veel verschillende gebruikssituaties waarin RAG je app kan verbeteren, zoals:

- Vraag en Antwoord: je bedrijfsdata koppelen aan een chat die door werknemers kan worden gebruikt om vragen te stellen.

- Aanbevelingssystemen: waarbij je een systeem kunt maken dat de meest vergelijkbare waarden matcht, bijvoorbeeld films, restaurants en nog veel meer.

- Chatbotdiensten: je kunt chatgeschiedenis opslaan en het gesprek personaliseren aan de hand van gebruikersdata.

- Afbeelding zoeken op basis van vector embeddings, nuttig bij beeldherkenning en het detecteren van afwijkingen.

## Samenvatting

We hebben de fundamentele gebieden van RAG behandeld: het toevoegen van onze data aan de applicatie, de gebruikersvraag en de output. Om de creatie van RAG te vereenvoudigen, kun je frameworks gebruiken zoals Semantic Kernel, LangChain of AutoGen.

## Opdracht

Om je kennis van Retrieval Augmented Generation (RAG) verder uit te breiden, kun je bouwen aan:

- Bouw een front-end voor de applicatie met het framework van jouw keuze

- Gebruik een framework, LangChain of Semantic Kernel, en bouw je applicatie opnieuw.

Gefeliciteerd met het afronden van de les 👏.

## Leren stopt hier niet, ga door op je leerreis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te verdiepen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->