<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T19:01:05+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sv"
}
-->
# Retrieval Augmented Generation (RAG) och Vektordatabaser

[![Retrieval Augmented Generation (RAG) och Vektordatabaser](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.sv.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

I lektionen om sökapplikationer lärde vi oss kort hur man integrerar egen data i stora språkmodeller (LLMs). I denna lektion kommer vi att fördjupa oss i koncepten kring att grunda din data i din LLM-applikation, mekaniken bakom processen och metoder för att lagra data, inklusive både embeddings och text.

> **Video kommer snart**

## Introduktion

I denna lektion kommer vi att täcka följande:

- En introduktion till RAG, vad det är och varför det används inom AI (artificiell intelligens).

- Förstå vad vektordatabaser är och skapa en för vår applikation.

- Ett praktiskt exempel på hur man integrerar RAG i en applikation.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att kunna:

- Förklara betydelsen av RAG för datahämtning och bearbetning.

- Ställa in en RAG-applikation och grunda din data till en LLM.

- Effektiv integration av RAG och vektordatabaser i LLM-applikationer.

## Vårt scenario: förbättra våra LLMs med vår egen data

För denna lektion vill vi lägga till våra egna anteckningar i utbildningsstartupen, vilket gör att chatboten kan få mer information om olika ämnen. Genom att använda de anteckningar vi har kommer eleverna att kunna studera bättre och förstå de olika ämnena, vilket gör det enklare att repetera inför sina prov. För att skapa vårt scenario kommer vi att använda:

- `Azure OpenAI:` LLM som vi kommer att använda för att skapa vår chatbot.

- `AI för nybörjare-lektion om neurala nätverk:` detta kommer att vara den data vi grundar vår LLM på.

- `Azure AI Search` och `Azure Cosmos DB:` vektordatabas för att lagra vår data och skapa ett sökindex.

Användare kommer att kunna skapa övningsquiz från sina anteckningar, repetitionskort och sammanfatta dem till kortfattade översikter. För att komma igång, låt oss titta på vad RAG är och hur det fungerar:

## Retrieval Augmented Generation (RAG)

En LLM-driven chatbot bearbetar användarens frågor för att generera svar. Den är designad för att vara interaktiv och engagerar sig med användare inom en mängd olika ämnen. Men dess svar är begränsade till det sammanhang som tillhandahålls och dess grundläggande träningsdata. Till exempel har GPT-4 en kunskapsgräns från september 2021, vilket innebär att den saknar kunskap om händelser som inträffat efter denna period. Dessutom utesluter den data som används för att träna LLMs konfidentiell information såsom personliga anteckningar eller en företags produktmanual.

### Hur RAGs (Retrieval Augmented Generation) fungerar

![ritning som visar hur RAGs fungerar](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.sv.png)

Anta att du vill distribuera en chatbot som skapar quiz från dina anteckningar, då behöver du en anslutning till kunskapsbasen. Det är här RAG kommer till undsättning. RAGs fungerar enligt följande:

- **Kunskapsbas:** Innan hämtning måste dessa dokument importeras och förbehandlas, vanligtvis genom att bryta ner stora dokument i mindre delar, omvandla dem till textembeddings och lagra dem i en databas.

- **Användarfråga:** användaren ställer en fråga.

- **Hämtning:** När en användare ställer en fråga hämtar embeddingmodellen relevant information från vår kunskapsbas för att ge mer sammanhang som kommer att införlivas i frågan.

- **Förbättrad generering:** LLM förbättrar sitt svar baserat på den data som hämtats. Det gör att det genererade svaret inte bara baseras på förtränad data utan också relevant information från det tillagda sammanhanget. Den hämtade datan används för att förbättra LLM:s svar. LLM returnerar sedan ett svar på användarens fråga.

![ritning som visar RAGs arkitektur](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.sv.png)

Arkitekturen för RAGs implementeras med hjälp av transformatorer som består av två delar: en encoder och en decoder. Till exempel, när en användare ställer en fråga, kodas inputtexten till vektorer som fångar innebörden av orden och vektorerna avkodas till vårt dokumentindex och genererar ny text baserat på användarens fråga. LLM använder både en encoder-decoder-modell för att generera output.

Två tillvägagångssätt vid implementering av RAG enligt det föreslagna dokumentet: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) är:

- **_RAG-Sequence_** använder hämtade dokument för att förutsäga det bästa möjliga svaret på en användarfråga.

- **RAG-Token** använder dokument för att generera nästa token och hämtar dem sedan för att svara på användarens fråga.

### Varför använda RAGs?

- **Informationsrikedom:** säkerställer att textresponsen är aktuell och uppdaterad. Det förbättrar därför prestandan på domänspecifika uppgifter genom att få tillgång till den interna kunskapsbasen.

- Minskar fabricering genom att använda **verifierbar data** i kunskapsbasen för att ge sammanhang till användarfrågor.

- Det är **kostnadseffektivt** eftersom de är mer ekonomiska jämfört med att finjustera en LLM.

## Skapa en kunskapsbas

Vår applikation är baserad på vår personliga data, dvs. lektionen om neurala nätverk från AI för nybörjare-kursen.

### Vektordatabaser

En vektordatabas, till skillnad från traditionella databaser, är en specialiserad databas designad för att lagra, hantera och söka inbäddade vektorer. Den lagrar numeriska representationer av dokument. Att bryta ner data till numeriska embeddings gör det enklare för vårt AI-system att förstå och bearbeta datan.

Vi lagrar våra embeddings i vektordatabaser eftersom LLMs har en gräns för antalet tokens de accepterar som input. Eftersom du inte kan skicka hela embeddings till en LLM, måste vi dela upp dem i mindre delar och när en användare ställer en fråga kommer de embeddings som är mest lik frågan att returneras tillsammans med frågan. Att dela upp data i mindre delar minskar också kostnaderna för antalet tokens som skickas genom en LLM.

Några populära vektordatabaser inkluderar Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant och DeepLake. Du kan skapa en Azure Cosmos DB-modell med Azure CLI med följande kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Från text till embeddings

Innan vi lagrar vår data måste vi konvertera den till vektorembeddings innan den lagras i databasen. Om du arbetar med stora dokument eller långa texter kan du dela upp dem baserat på de frågor du förväntar dig. Uppdelning kan göras på meningsnivå eller på styckenivå. Eftersom uppdelning härleder betydelser från orden runt dem kan du lägga till annat sammanhang till en del, till exempel genom att lägga till dokumenttiteln eller inkludera viss text före eller efter delen. Du kan dela upp datan enligt följande:

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

När den är uppdelad kan vi sedan bädda in vår text med olika embeddingmodeller. Några modeller du kan använda inkluderar: word2vec, ada-002 av OpenAI, Azure Computer Vision och många fler. Valet av modell beror på vilka språk du använder, vilken typ av innehåll som kodas (text/bilder/ljud), storleken på input den kan koda och längden på embeddingoutputen.

Ett exempel på inbäddad text med OpenAI:s `text-embedding-ada-002`-modell är:
![en embedding av ordet katt](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.sv.png)

## Hämtning och vektorsökning

När en användare ställer en fråga omvandlar hämtaren den till en vektor med hjälp av frågekodaren, och söker sedan igenom vårt dokumentsökindex efter relevanta vektorer i dokumentet som är relaterade till input. När detta är gjort konverterar den både inputvektorn och dokumentvektorerna till text och skickar dem genom LLM.

### Hämtning

Hämtning sker när systemet försöker snabbt hitta dokument från indexet som uppfyller sökkriterierna. Målet med hämtaren är att få dokument som kommer att användas för att ge sammanhang och grunda LLM på din data.

Det finns flera sätt att utföra sökningar inom vår databas, såsom:

- **Nyckelordssökning** - används för textsökningar.

- **Semantisk sökning** - använder den semantiska betydelsen av ord.

- **Vektorsökning** - konverterar dokument från text till vektorrepresentationer med hjälp av embeddingmodeller. Hämtning görs genom att fråga dokument vars vektorrepresentationer är närmast användarens fråga.

- **Hybrid** - en kombination av både nyckelordssökning och vektorsökning.

En utmaning med hämtning uppstår när det inte finns något liknande svar på frågan i databasen, systemet kommer då att returnera den bästa informationen de kan hitta. Du kan dock använda taktiker som att ställa in det maximala avståndet för relevans eller använda hybridsökning som kombinerar både nyckelord och vektorsökning. I denna lektion kommer vi att använda hybridsökning, en kombination av både vektor- och nyckelordssökning. Vi kommer att lagra vår data i en dataframe med kolumner som innehåller delarna samt embeddings.

### Vektorsimilaritet

Hämtaren kommer att söka igenom kunskapsdatabasen efter embeddings som ligger nära varandra, den närmaste grannen, eftersom de är texter som är liknande. I scenariot där en användare ställer en fråga, bäddas den först in och matchas sedan med liknande embeddings. Det vanliga måttet som används för att hitta hur lika olika vektorer är, är cosinuslikhet som baseras på vinkeln mellan två vektorer.

Vi kan mäta likhet med andra alternativ som Euclidean-avstånd, vilket är den raka linjen mellan vektorändpunkter, och skalärprodukt som mäter summan av produkterna av motsvarande element i två vektorer.

### Sökindex

När vi gör hämtning måste vi bygga ett sökindex för vår kunskapsbas innan vi utför sökningen. Ett index lagrar våra embeddings och kan snabbt hämta de mest liknande delarna även i en stor databas. Vi kan skapa vårt index lokalt med:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Omrankning

När du har frågat databasen kan du behöva sortera resultaten från de mest relevanta. En omranknings-LLM använder maskininlärning för att förbättra relevansen av sökresultaten genom att ordna dem från de mest relevanta. Med Azure AI Search görs omrankning automatiskt för dig med en semantisk omrankare. Ett exempel på hur omrankning fungerar med närmaste grannar:

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

## Sätta ihop allt

Det sista steget är att lägga till vår LLM i mixen för att kunna få svar som är grundade på vår data. Vi kan implementera det enligt följande:

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

## Utvärdera vår applikation

### Utvärderingsmått

- Kvaliteten på de svar som ges, säkerställa att de låter naturliga, flytande och mänskliga.

- Grundning av data: utvärdera om svaret kom från tillhandahållna dokument.

- Relevans: utvärdera om svaret matchar och är relaterat till den fråga som ställdes.

- Flyt: om svaret är grammatiskt korrekt.

## Användningsområden för RAG (Retrieval Augmented Generation) och vektordatabaser

Det finns många olika användningsområden där funktionsanrop kan förbättra din app, såsom:

- Frågor och svar: grunda din företagsdata till en chatt som kan användas av anställda för att ställa frågor.

- Rekommendationssystem: där du kan skapa ett system som matchar de mest liknande värdena, t.ex. filmer, restauranger och mycket mer.

- Chatbot-tjänster: du kan lagra chattloggar och anpassa konversationen baserat på användardata.

- Bildsökning baserat på vektorembeddings, användbart vid bildigenkänning och avvikelsedetektering.

## Sammanfattning

Vi har täckt de grundläggande områdena för RAG från att lägga till vår data i applikationen, användarfrågan och output. För att förenkla skapandet av RAG kan du använda ramverk som Semantic Kernel, Langchain eller Autogen.

## Uppgift

För att fortsätta din inlärning om Retrieval Augmented Generation (RAG) kan du bygga:

- Bygg en front-end för applikationen med det ramverk du föredrar.

- Använd ett ramverk, antingen LangChain eller Semantic Kernel, och återskapa din applikation.

Grattis till att ha avslutat lektionen 👏.

## Lärandet slutar inte här, fortsätt resan

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.