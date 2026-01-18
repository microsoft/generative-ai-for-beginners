<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:04:45+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sv"
}
-->
# Retrieval Augmented Generation (RAG) och vektordatabaser

[![Retrieval Augmented Generation (RAG) och Vektordatabaser](../../../../../translated_images/sv/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

I lektionen om sökapplikationer lärde vi oss kort hur man integrerar egna data i Large Language Models (LLMs). I denna lektion ska vi fördjupa oss i koncepten för att förankra dina data i din LLM-applikation, hur processen fungerar och metoder för att lagra data, inklusive både embeddings och text.

> **Video kommer snart**

## Introduktion

I denna lektion kommer vi ta upp följande:

- En introduktion till RAG, vad det är och varför det används inom AI (artificiell intelligens).

- Förstå vad vektordatabaser är och skapa en för vår applikation.

- Ett praktiskt exempel på hur man integrerar RAG i en applikation.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Förklara betydelsen av RAG vid datahämtning och bearbetning.

- Sätta upp en RAG-applikation och förankra dina data till en LLM.

- Effektiv integration av RAG och vektordatabaser i LLM-applikationer.

## Vårt scenario: förbättra våra LLMs med våra egna data

I denna lektion vill vi lägga till våra egna anteckningar i utbildningsstartuppen, vilket gör det möjligt för chatbotten att få mer information om de olika ämnena. Genom att använda de anteckningar vi har, kan eleverna studera bättre och förstå de olika ämnena, vilket gör det enklare att repetera inför sina examinationer. För att skapa vårt scenario använder vi:

- `Azure OpenAI:` den LLM vi ska använda för att skapa vår chatbot

- `AI for beginners' lesson on Neural Networks:` detta kommer att vara datan vi förankrar vår LLM på

- `Azure AI Search` och `Azure Cosmos DB:` vektordatabas för att lagra våra data och skapa en sökindex

Användare kommer att kunna skapa övningsquiz från sina anteckningar, repetitionsflashkort och sammanfatta dessa till kortfattade översikter. För att komma igång, låt oss titta på vad RAG är och hur det fungerar:

## Retrieval Augmented Generation (RAG)

En LLM-driven chatbot bearbetar användarfrågor för att generera svar. Den är designad för att vara interaktiv och engagerar sig med användare inom många olika ämnen. Men dess svar begränsas till det sammanhang som ges och dess grundläggande träningsdata. Till exempel har GPT-4 kunskapsstopp i september 2021, vilket innebär att den saknar kunskap om händelser som inträffat efter detta datum. Dessutom inkluderar träningsdatan för LLMs inte konfidentiell information som personliga anteckningar eller ett företags produktmanual.

### Hur RAGs (Retrieval Augmented Generation) fungerar

![ritning som visar hur RAGs fungerar](../../../../../translated_images/sv/how-rag-works.f5d0ff63942bd3a6.webp)

Anta att du vill implementera en chatbot som skapar quiz från dina anteckningar, då behöver du en koppling till kunskapsbasen. Det är här RAG kommer in. RAGs fungerar enligt följande:

- **Kunskapsbas:** Innan hämtning måste dessa dokument läsas in och förbehandlas, vanligtvis genom att bryta ner stora dokument i mindre delar, omvandla dem till textembeddingar och lagra dem i en databas.

- **Användarfråga:** användaren ställer en fråga

- **Hämtning:** När användaren ställer en fråga hämtar embeddingmodellen relevant information från vår kunskapsbas för att ge mer kontext som inkluderas i prompten.

- **Augmented Generation:** LLM förbättrar sitt svar baserat på den hämtade datan. Detta tillåter det genererade svaret att inte bara baseras på förtränad data utan också på relevant information från den tillagda kontexten. Den hämtade datan används för att förstärka LLM:s svar. LLM returnerar därefter ett svar på användarens fråga.

![ritning som visar hur RAGs arkitektur fungerar](../../../../../translated_images/sv/encoder-decode.f2658c25d0eadee2.webp)

Arkitekturen för RAGs implementeras med transformers bestående av två delar: en encoder och en decoder. Till exempel, när en användare ställer en fråga, "kodas" inmatningstexten till vektorer som fångar ordens betydelse och vektorerna "avkodas" mot vårt dokumentindex och genererar ny text baserad på användarens fråga. LLM använder både en encoder-decoder-modell för att generera output.

Två tillvägagångssätt vid implementering av RAG enligt det föreslagna dokumentet: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) är:

- **_RAG-Sequence_** använder hämtade dokument för att förutsäga bästa möjliga svar på en användarfråga

- **RAG-Token** använder dokument för att generera nästa token, sedan hämtas de för att svara på användarens fråga

### Varför skulle du använda RAGs?

- **Informationsrikedom:** säkerställer att textsvar är uppdaterade och aktuella. Detta förbättrar prestandan på domänspecifika uppgifter genom att komma åt den interna kunskapsbasen.

- Minskar fabricering genom att använda **verifierbar data** i kunskapsbasen för att ge kontext till användarfrågor.

- Det är **kostnadseffektivt** eftersom det är mer ekonomiskt jämfört med finjustering av en LLM.

## Skapa en kunskapsbas

Vår applikation baseras på våra personliga data, det vill säga lektionen om neurala nätverk i AI For Beginners-kursen.

### Vektordatabaser

En vektordatabas är, till skillnad från traditionella databaser, en specialiserad databas designad för att lagra, hantera och söka inbäddade vektorer. Den lagrar numeriska representationer av dokument. Att bryta ner data till numeriska embeddingar gör det enklare för vårt AI-system att förstå och bearbeta datan.

Vi lagrar våra embeddingar i vektordatabaser eftersom LLMs har en gräns för hur många tokens de accepterar som input. Eftersom man inte kan skicka hela embeddingarna till en LLM, behöver vi dela upp dem i bitar och när en användare ställer en fråga kommer embeddingarna som är mest relevanta för frågan att returneras tillsammans med prompten. Uppdelning minskar också kostnaderna för antalet tokens som skickas genom en LLM.

Några populära vektordatabaser är Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant och DeepLake. Du kan skapa en Azure Cosmos DB-modell med Azure CLI med följande kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Från text till embeddingar

Innan vi lagrar vår data måste vi konvertera den till vektor-embeddingar innan de lagras i databasen. Om du arbetar med stora dokument eller långa texter kan du dela upp dem baserat på förväntade frågor. Uppdelning kan göras på meningsnivå eller på styckesnivå. Eftersom uppdelning hämtar betydelser från orden runt omkring kan du lägga till viss ytterligare kontext till en bit, till exempel genom att lägga till dokumentets titel eller inkludera viss text före eller efter biten. Du kan dela upp datan enligt följande:

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

    # Om den sista biten inte nådde minimilängden, lägg till den ändå
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

När den väl är uppdelad kan vi sedan bädda in vår text med olika embeddingmodeller. Några modeller du kan använda inkluderar: word2vec, ada-002 från OpenAI, Azure Computer Vision och många fler. Valet av modell beror på vilka språk du använder, typen av innehåll som kodas (text/bilder/ljud), storleken på input den kan koda och längden på embeddingoutput.

Ett exempel på inbäddad text med OpenAIs `text-embedding-ada-002` modell är:
![en embedding av ordet katt](../../../../../translated_images/sv/cat.74cbd7946bc9ca38.webp)

## Hämtning och vektorsökning

När en användare ställer en fråga omvandlar retrievern den till en vektor med query-encodern och söker sedan igenom vårt dokumentindex efter relevanta vektorer i dokumentet som relaterar till inmatningen. När detta är gjort konverteras både inmatningsvektorn och dokumentvektorer till text och skickas genom LLM.

### Hämtning

Hämtning sker när systemet försöker snabbt hitta dokument i indexet som uppfyller sökkriterierna. Målet för retrievern är att få fram dokument som kan användas för att ge kontext och förankra LLM i dina data.

Det finns flera sätt att utföra sökningar i vår databas, såsom:

- **Nyckelordssökning** – används för textsökningar

- **Vektorsökning** – konverterar dokument från text till vektorrepresentationer med hjälp av embeddingmodeller, vilket möjliggör en **semantisk sökning** baserad på ordens betydelse. Hämtning sker genom att fråga de dokument vars vektorrepresentationer är närmast användarens fråga.

- **Hybrid** – en kombination av både nyckelords- och vektorsökning.

En utmaning med hämtning uppstår när det inte finns något liknande svar i databasen; systemet returnerar då den bästa information det kan finna, men du kan använda taktiker som att ställa in maximal relevansavstånd eller använda hybrid-sökning som kombinerar både nyckelord och vektorsökning. I denna lektion använder vi hybrid-sökning, en kombination av både vektor- och nyckelordssökning. Vi kommer att lagra vår data i en dataframe med kolumner som innehåller bitarna samt embeddingarna.

### Vektorsimilaritet

Retrievern söker igenom kunskapsdatabasen efter embeddingar som ligger nära varandra, närmaste granne, eftersom det handlar om texter som är liknande. I scenariot där en användare ställer en fråga, bäddas frågan först in och matchas sedan med liknande embeddingar. Det vanliga måttet som används för att hitta hur lika olika vektorer är är cosinuslikhet, vilket baseras på vinkeln mellan två vektorer.

Vi kan mäta likhet med andra alternativ som vi kan använda, till exempel Euklidiskt avstånd, vilket är den raka linjen mellan vektorändpunkter, och prdotprodukt som mäter summan av produkterna för motsvarande element i två vektorer.

### Sökindex

När vi hämtar behöver vi bygga ett sökindex för vår kunskapsbas innan vi utför sökningen. Ett index lagrar våra embeddingar och kan snabbt hämta de mest lika bitarna även i en stor databas. Vi kan skapa vårt index lokalt med:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Skapa sökindexet
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# För att fråga indexet kan du använda kneighbors-metoden
distances, indices = nbrs.kneighbors(embeddings)
```

### Omrankning

När du har frågat i databasen kan du behöva sortera resultaten från mest relevanta till minst relevanta. En omrankande LLM använder maskininlärning för att förbättra relevansen av sökresultaten genom att ordna dem från mest relevanta. Med Azure AI Search görs omrankning automatiskt med en semantisk omrankare. Ett exempel på hur omrankning fungerar med närmaste grannar:

```python
# Hitta de mest liknande dokumenten
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Skriv ut de mest liknande dokumenten
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Att förena allt detta

Det sista steget är att lägga till vår LLM i mixen för att kunna få svar som är förankrade i vår data. Vi kan implementera det enligt följande:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Konvertera frågan till en förfrågningsvektor
    query_vector = create_embeddings(user_input)

    # Hitta de mest liknande dokumenten
    distances, indices = nbrs.kneighbors([query_vector])

    # lägg till dokument till förfrågan för att ge kontext
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # kombinera historiken och användarens input
    history.append(user_input)

    # skapa ett meddelandeobjekt
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # använd chattkomplettering för att generera ett svar
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Utvärdera vår applikation

### Utvärderingsmått

- Kvaliteten på svaren, att de låter naturliga, flytande och människolika

- Förankring av datan: utvärdering om svaret kom från de tillhandahållna dokumenten

- Relevans: utvärdering att svaret matchar och är relaterat till ställd fråga

- Flyt – om svaret är grammatiskt korrekt och begripligt

## Användningsområden för RAG (Retrieval Augmented Generation) och vektordatabaser

Det finns många olika användningsområden där funktionsanrop kan förbättra din app såsom:

- Frågor och svar: förankra din företagsdata till en chatt som kan användas av anställda för att ställa frågor.

- Rekommendationssystem: där du kan skapa ett system som matchar de mest lika värdena, t.ex. filmer, restauranger och mycket mer.

- Chattbottjänster: du kan lagra chattloggen och personanpassa konversationen baserat på användardata.

- Bildsökning baserad på vektorembeddingar, användbart vid bildigenkänning och felavvikelsedetektering.

## Sammanfattning

Vi har täckt grundläggande områden för RAG från att lägga till vår data till applikationen, användarfrågan och utdata. För att förenkla skapandet av RAG kan du använda ramverk som Semantic Kernel, Langchain eller Autogen.

## Uppgift

För att fortsätta din lärande om Retrieval Augmented Generation (RAG) kan du bygga:

- Skapa ett front-end för applikationen med valfritt ramverk

- Använd ett ramverk, antingen LangChain eller Semantic Kernel, och återbygg din applikation.

Grattis till att ha slutfört lektionen 👏.

## Lärandet slutar inte här, fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja din kunskap inom Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->