<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T19:53:40+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "nl"
}
-->
# Retrieval Augmented Generation (RAG) en Vector Databases

[![Retrieval Augmented Generation (RAG) en Vector Databases](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.nl.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

In de les over zoektoepassingen hebben we kort geleerd hoe je je eigen data kunt integreren in Large Language Models (LLMs). In deze les gaan we dieper in op de concepten van het verankeren van je data in je LLM-toepassing, de werking van het proces en de methoden voor het opslaan van data, inclusief zowel embeddings als tekst.

> **Video binnenkort beschikbaar**

## Introductie

In deze les behandelen we het volgende:

- Een introductie tot RAG, wat het is en waarom het wordt gebruikt in AI (kunstmatige intelligentie).

- Begrijpen wat vector databases zijn en er een maken voor onze toepassing.

- Een praktisch voorbeeld van hoe je RAG kunt integreren in een toepassing.

## Leerdoelen

Na het voltooien van deze les kun je:

- Uitleggen waarom RAG belangrijk is voor data-opvraging en -verwerking.

- Een RAG-toepassing instellen en je data verankeren aan een LLM.

- RAG en Vector Databases effectief integreren in LLM-toepassingen.

## Ons scenario: onze LLMs verbeteren met onze eigen data

Voor deze les willen we onze eigen notities toevoegen aan de educatieve startup, zodat de chatbot meer informatie kan geven over verschillende onderwerpen. Met behulp van de notities kunnen leerlingen beter studeren en de verschillende onderwerpen begrijpen, wat het makkelijker maakt om zich voor te bereiden op examens. Om ons scenario te creëren, gebruiken we:

- `Azure OpenAI:` de LLM die we gebruiken om onze chatbot te maken.

- `AI voor beginners-les over neurale netwerken:` dit is de data waarop we onze LLM verankeren.

- `Azure AI Search` en `Azure Cosmos DB:` vector database om onze data op te slaan en een zoekindex te maken.

Gebruikers kunnen oefenquizzen maken van hun notities, samenvattingskaartjes en deze samenvatten tot beknopte overzichten. Om te beginnen, laten we eens kijken wat RAG is en hoe het werkt:

## Retrieval Augmented Generation (RAG)

Een door LLM aangedreven chatbot verwerkt gebruikersvragen om antwoorden te genereren. Het is ontworpen om interactief te zijn en met gebruikers te communiceren over een breed scala aan onderwerpen. De antwoorden zijn echter beperkt tot de context die wordt geboden en de basis trainingsdata. Bijvoorbeeld, de kennis van GPT-4 stopt in september 2021, wat betekent dat het geen kennis heeft van gebeurtenissen die daarna hebben plaatsgevonden. Bovendien bevat de data die wordt gebruikt om LLMs te trainen geen vertrouwelijke informatie zoals persoonlijke notities of een producthandleiding van een bedrijf.

### Hoe RAGs (Retrieval Augmented Generation) werken

![tekening die laat zien hoe RAGs werken](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.nl.png)

Stel dat je een chatbot wilt inzetten die quizzen maakt van je notities, dan heb je een verbinding met de kennisbank nodig. Hier komt RAG van pas. RAGs werken als volgt:

- **Kennisbank:** Voordat data wordt opgehaald, moeten deze documenten worden ingelezen en voorbewerkt, meestal door grote documenten op te splitsen in kleinere stukken, ze om te zetten in tekstembeddings en ze op te slaan in een database.

- **Gebruikersvraag:** de gebruiker stelt een vraag.

- **Opvraging:** Wanneer een gebruiker een vraag stelt, haalt het embeddingmodel relevante informatie uit onze kennisbank om meer context te bieden die in de prompt wordt opgenomen.

- **Augmented Generation:** de LLM verbetert zijn antwoord op basis van de opgehaalde data. Dit zorgt ervoor dat het gegenereerde antwoord niet alleen gebaseerd is op vooraf getrainde data, maar ook op relevante informatie uit de toegevoegde context. De opgehaalde data wordt gebruikt om de antwoorden van de LLM te verrijken. De LLM geeft vervolgens een antwoord op de vraag van de gebruiker.

![tekening die de architectuur van RAGs toont](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.nl.png)

De architectuur van RAGs wordt geïmplementeerd met behulp van transformers die bestaan uit twee delen: een encoder en een decoder. Bijvoorbeeld, wanneer een gebruiker een vraag stelt, wordt de invoertekst 'gecodeerd' in vectoren die de betekenis van woorden vastleggen, en worden de vectoren 'gedecodeerd' in onze documentindex en genereert nieuwe tekst op basis van de gebruikersvraag. De LLM gebruikt zowel een encoder-decoder model om de output te genereren.

Twee benaderingen bij het implementeren van RAG volgens het voorgestelde artikel: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) zijn:

- **_RAG-Sequence_** gebruikt opgehaalde documenten om het best mogelijke antwoord op een gebruikersvraag te voorspellen.

- **RAG-Token** gebruikt documenten om de volgende token te genereren en haalt ze vervolgens op om de vraag van de gebruiker te beantwoorden.

### Waarom zou je RAGs gebruiken?

- **Informatierijkdom:** zorgt ervoor dat tekstantwoorden actueel en up-to-date zijn. Het verbetert dus de prestaties bij domeinspecifieke taken door toegang te krijgen tot de interne kennisbank.

- Vermindert verzinsels door gebruik te maken van **verifieerbare data** in de kennisbank om context te bieden bij gebruikersvragen.

- Het is **kosteneffectief** omdat ze economischer zijn in vergelijking met het fijn afstemmen van een LLM.

## Een kennisbank maken

Onze toepassing is gebaseerd op onze persoonlijke data, namelijk de les over neurale netwerken uit het AI For Beginners-curriculum.

### Vector Databases

Een vector database, in tegenstelling tot traditionele databases, is een gespecialiseerde database ontworpen om embedded vectoren op te slaan, beheren en doorzoeken. Het slaat numerieke representaties van documenten op. Het opsplitsen van data in numerieke embeddings maakt het makkelijker voor ons AI-systeem om de data te begrijpen en te verwerken.

We slaan onze embeddings op in vector databases omdat LLMs een limiet hebben aan het aantal tokens dat ze als input accepteren. Omdat je niet alle embeddings aan een LLM kunt doorgeven, moeten we ze opsplitsen in stukken en wanneer een gebruiker een vraag stelt, worden de embeddings die het meest lijken op de vraag samen met de prompt teruggegeven. Het opsplitsen vermindert ook de kosten van het aantal tokens dat door een LLM wordt verwerkt.

Enkele populaire vector databases zijn Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant en DeepLake. Je kunt een Azure Cosmos DB-model maken met Azure CLI met het volgende commando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Van tekst naar embeddings

Voordat we onze data opslaan, moeten we deze omzetten in vector embeddings voordat deze in de database wordt opgeslagen. Als je werkt met grote documenten of lange teksten, kun je ze opsplitsen op basis van de vragen die je verwacht. Opsplitsen kan op zinsniveau of op alinea-niveau. Omdat opsplitsen betekenissen afleidt uit de woorden eromheen, kun je wat extra context toevoegen aan een stuk, bijvoorbeeld door de documenttitel toe te voegen of wat tekst voor of na het stuk op te nemen. Je kunt de data als volgt opsplitsen:

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

Zodra de data is opgesplitst, kunnen we deze embedden met verschillende embeddingmodellen. Enkele modellen die je kunt gebruiken zijn: word2vec, ada-002 van OpenAI, Azure Computer Vision en nog veel meer. Het kiezen van een model hangt af van de talen die je gebruikt, het type inhoud dat wordt gecodeerd (tekst/afbeeldingen/audio), de grootte van de input die het kan coderen en de lengte van de embedding-output.

Een voorbeeld van embedded tekst met behulp van OpenAI's `text-embedding-ada-002` model is:
![een embedding van het woord kat](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.nl.png)

## Opvraging en Vector Search

Wanneer een gebruiker een vraag stelt, zet de retriever deze om in een vector met behulp van de query encoder, waarna deze door onze documentzoekindex zoekt naar relevante vectoren in het document die gerelateerd zijn aan de input. Zodra dit is gedaan, zet het zowel de inputvector als de documentvectoren om in tekst en geeft het door aan de LLM.

### Opvraging

Opvraging vindt plaats wanneer het systeem probeert snel de documenten uit de index te vinden die voldoen aan de zoekcriteria. Het doel van de retriever is om documenten te verkrijgen die zullen worden gebruikt om context te bieden en de LLM te verankeren op je data.

Er zijn verschillende manieren om zoekopdrachten uit te voeren binnen onze database, zoals:

- **Zoeken op trefwoord** - gebruikt voor tekstzoekopdrachten.

- **Semantisch zoeken** - gebruikt de semantische betekenis van woorden.

- **Vector zoeken** - zet documenten om van tekst naar vectorrepresentaties met behulp van embeddingmodellen. Opvraging wordt uitgevoerd door de documenten te zoeken waarvan de vectorrepresentaties het dichtst bij de gebruikersvraag liggen.

- **Hybride** - een combinatie van zowel trefwoord- als vector zoeken.

Een uitdaging bij opvraging ontstaat wanneer er geen vergelijkbaar antwoord op de vraag in de database is, het systeem zal dan de beste informatie teruggeven die ze kunnen vinden. Je kunt echter tactieken gebruiken zoals het instellen van de maximale afstand voor relevantie of hybride zoeken dat zowel trefwoorden als vector zoeken combineert. In deze les gebruiken we hybride zoeken, een combinatie van zowel vector- als trefwoord zoeken. We slaan onze data op in een dataframe met kolommen die de stukken en embeddings bevatten.

### Vector Similarity

De retriever zoekt door de kennisdatabase naar embeddings die dicht bij elkaar liggen, de dichtstbijzijnde buur, omdat dit teksten zijn die vergelijkbaar zijn. In het scenario waarin een gebruiker een vraag stelt, wordt deze eerst embedded en vervolgens gekoppeld aan vergelijkbare embeddings. De meest gebruikte maatstaf om te bepalen hoe vergelijkbaar verschillende vectoren zijn, is cosine similarity, gebaseerd op de hoek tussen twee vectoren.

We kunnen vergelijkbaarheid meten met andere alternatieven zoals Euclidische afstand, wat de rechte lijn tussen vector eindpunten is, en dot product, wat de som van de producten van overeenkomstige elementen van twee vectoren meet.

### Zoekindex

Bij het uitvoeren van opvraging moeten we een zoekindex bouwen voor onze kennisbank voordat we zoeken uitvoeren. Een index slaat onze embeddings op en kan snel de meest vergelijkbare stukken ophalen, zelfs in een grote database. We kunnen onze index lokaal maken met:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Herordenen

Nadat je de database hebt doorzocht, moet je mogelijk de resultaten sorteren van meest relevant naar minder relevant. Een herordening LLM maakt gebruik van Machine Learning om de relevantie van zoekresultaten te verbeteren door ze te ordenen van meest relevant. Met Azure AI Search wordt herordening automatisch voor je uitgevoerd met behulp van een semantische herordener. Een voorbeeld van hoe herordening werkt met behulp van dichtstbijzijnde buren:

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

## Alles samenbrengen

De laatste stap is het toevoegen van onze LLM om antwoorden te kunnen krijgen die gebaseerd zijn op onze data. We kunnen dit implementeren als volgt:

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

## Evaluatie van onze toepassing

### Evaluatiemetrics

- Kwaliteit van de gegeven antwoorden, waarbij wordt gekeken of ze natuurlijk, vloeiend en menselijk klinken.

- Verankering van de data: evalueren of het antwoord afkomstig is van de aangeleverde documenten.

- Relevantie: evalueren of het antwoord overeenkomt met en gerelateerd is aan de gestelde vraag.

- Vlotheid - of het antwoord grammaticaal logisch is.

## Toepassingen van RAG (Retrieval Augmented Generation) en vector databases

Er zijn veel verschillende toepassingen waarbij functieaanroepen je app kunnen verbeteren, zoals:

- Vraag en antwoord: je bedrijfsdata verankeren aan een chat die door medewerkers kan worden gebruikt om vragen te stellen.

- Aanbevelingssystemen: waarbij je een systeem kunt maken dat de meest vergelijkbare waarden matcht, zoals films, restaurants en meer.

- Chatbotdiensten: je kunt chatgeschiedenis opslaan en het gesprek personaliseren op basis van gebruikersdata.

- Afbeeldingszoekopdrachten op basis van vector embeddings, handig bij beeldherkenning en het detecteren van afwijkingen.

## Samenvatting

We hebben de fundamentele gebieden van RAG behandeld, van het toevoegen van onze data aan de toepassing, de gebruikersvraag en de output. Om het maken van RAG te vereenvoudigen, kun je frameworks zoals Semantic Kernel, Langchain of Autogen gebruiken.

## Opdracht

Om je kennis over Retrieval Augmented Generation (RAG) verder te ontwikkelen, kun je:

- Een front-end bouwen voor de toepassing met behulp van een framework naar keuze.

- Een framework gebruiken, zoals LangChain of Semantic Kernel, en je toepassing opnieuw maken.

Gefeliciteerd met het voltooien van de les 👏.

## Het leren stopt hier niet, ga verder met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generative AI verder uit te breiden!

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.