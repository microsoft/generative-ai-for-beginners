<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:34:39+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "sv"
}
-->
# Retrieval Augmented Generation (RAG) och vektordatabaser

I lektionen om sökapplikationer lärde vi oss kortfattat hur man integrerar din egen data i stora språkmodeller (LLMs). I denna lektion kommer vi att fördjupa oss i koncepten att förankra din data i din LLM-applikation, processens mekanik och metoder för att lagra data, inklusive både inbäddningar och text.

> **Video Kommer Snart**

## Introduktion

I denna lektion kommer vi att täcka följande:

- En introduktion till RAG, vad det är och varför det används inom AI (artificiell intelligens).

- Förstå vad vektordatabaser är och skapa en för vår applikation.

- Ett praktiskt exempel på hur man integrerar RAG i en applikation.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Förklara betydelsen av RAG vid datahämtning och bearbetning.

- Ställa in RAG-applikationen och förankra din data till en LLM

- Effektiv integration av RAG och vektordatabaser i LLM-applikationer.

## Vårt scenario: förbättra våra LLM:er med vår egen data

För denna lektion vill vi lägga till våra egna anteckningar i utbildningsstarten, vilket gör att chatboten kan få mer information om de olika ämnena. Genom att använda de anteckningar vi har kommer eleverna att kunna studera bättre och förstå de olika ämnena, vilket gör det lättare att repetera inför sina prov. För att skapa vårt scenario kommer vi att använda:

- `Azure OpenAI:` den LLM vi kommer att använda för att skapa vår chatbot

- `AI for beginners' lesson on Neural Networks`: detta kommer att vara den data vi förankrar vår LLM på

- `Azure AI Search` och `Azure Cosmos DB:` vektordatabas för att lagra vår data och skapa ett sökindex

Användare kommer att kunna skapa övningsquiz från sina anteckningar, repetitionskort och sammanfatta dem till kortfattade översikter. För att komma igång, låt oss titta på vad RAG är och hur det fungerar:

## Retrieval Augmented Generation (RAG)

En LLM-driven chatbot bearbetar användarens uppmaningar för att generera svar. Den är designad för att vara interaktiv och engagerar sig med användare inom ett brett spektrum av ämnen. Men dess svar är begränsade till den kontext som ges och dess grundläggande träningsdata. Till exempel, GPT-4:s kunskapsavgränsning är september 2021, vilket betyder att den saknar kunskap om händelser som inträffat efter denna period. Dessutom utesluter datan som används för att träna LLM:er konfidentiell information såsom personliga anteckningar eller en företags produktmanual.

### Hur RAGs (Retrieval Augmented Generation) fungerar

Anta att du vill distribuera en chatbot som skapar quiz från dina anteckningar, du kommer att behöva en anslutning till kunskapsbasen. Det är här RAG kommer till undsättning. RAGs fungerar på följande sätt:

- **Kunskapsbas:** Innan hämtning behöver dessa dokument matas in och förbehandlas, vanligtvis genom att bryta ner stora dokument i mindre delar, omvandla dem till textinbäddning och lagra dem i en databas.

- **Användarfråga:** användaren ställer en fråga

- **Hämtning:** När en användare ställer en fråga hämtar inbäddningsmodellen relevant information från vår kunskapsbas för att ge mer kontext som kommer att införlivas i uppmaningen.

- **Förstärkt generering:** LLM förbättrar sitt svar baserat på den hämtade datan. Det gör att det genererade svaret inte bara baseras på förtränad data utan också på relevant information från den tillagda kontexten. Den hämtade datan används för att förstärka LLM:s svar. LLM returnerar sedan ett svar på användarens fråga.

Arkitekturen för RAGs implementeras med hjälp av transformatorer bestående av två delar: en kodare och en avkodare. Till exempel, när en användare ställer en fråga, 'kodas' inputtexten till vektorer som fångar ordens betydelse och vektorerna 'avkodas' till vårt dokumentindex och genererar ny text baserat på användarens fråga. LLM använder både en kodare-avkodare-modell för att generera output.

Två tillvägagångssätt när man implementerar RAG enligt det föreslagna dokumentet: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) är:

- **_RAG-Sequence_** använder hämtade dokument för att förutsäga det bästa möjliga svaret på en användarfråga

- **RAG-Token** använder dokument för att generera nästa token, sedan hämta dem för att svara på användarens fråga

### Varför skulle du använda RAGs?

- **Informationsrikedom:** säkerställer att textresponsen är uppdaterad och aktuell. Det förbättrar därför prestandan på domänspecifika uppgifter genom att få tillgång till den interna kunskapsbasen.

- Minskar fabricering genom att använda **verifierbar data** i kunskapsbasen för att ge kontext till användarfrågorna.

- Det är **kostnadseffektivt** eftersom de är mer ekonomiska jämfört med att finjustera en LLM.

## Skapa en kunskapsbas

Vår applikation baseras på vår personliga data, dvs. lektionen om neurala nätverk i AI för nybörjare-kursen.

### Vektordatabaser

En vektordatabas, till skillnad från traditionella databaser, är en specialiserad databas designad för att lagra, hantera och söka inbäddade vektorer. Den lagrar numeriska representationer av dokument. Att bryta ner data till numeriska inbäddningar gör det lättare för vårt AI-system att förstå och bearbeta datan.

Vi lagrar våra inbäddningar i vektordatabaser eftersom LLM:er har en gräns för antalet tokens de accepterar som input. Eftersom du inte kan skicka hela inbäddningarna till en LLM, behöver vi bryta ner dem i delar och när en användare ställer en fråga, kommer de inbäddningar som mest liknar frågan att returneras tillsammans med uppmaningen. Att dela upp minskar också kostnaderna för antalet tokens som skickas genom en LLM.

Några populära vektordatabaser inkluderar Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant och DeepLake. Du kan skapa en Azure Cosmos DB-modell med Azure CLI med följande kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Från text till inbäddningar

Innan vi lagrar vår data, behöver vi konvertera den till vektor-inbäddningar innan den lagras i databasen. Om du arbetar med stora dokument eller långa texter, kan du dela upp dem baserat på de frågor du förväntar dig. Uppdelning kan göras på meningsnivå eller på styckenivå. Eftersom uppdelning hämtar betydelser från orden runt dem, kan du lägga till annan kontext till en del, till exempel genom att lägga till dokumenttiteln eller inkludera lite text före eller efter delen. Du kan dela upp datan enligt följande:

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

När den väl är uppdelad, kan vi sedan bädda in vår text med hjälp av olika inbäddningsmodeller. Några modeller du kan använda inkluderar: word2vec, ada-002 av OpenAI, Azure Computer Vision och många fler. Valet av modell beror på vilka språk du använder, typen av innehåll som kodas (text/bilder/ljud), storleken på inputen den kan koda och längden på inbäddningsoutputen.

Ett exempel på inbäddad text med hjälp av OpenAI:s `text-embedding-ada-002`-modell är:

## Hämtning och vektorsökning

När en användare ställer en fråga, omvandlar hämtaren den till en vektor med hjälp av frågekodaren, den söker sedan genom vårt dokumentsökindex efter relevanta vektorer i dokumentet som är relaterade till inputen. När det är klart, omvandlar den både inputvektorn och dokumentvektorerna till text och skickar det genom LLM.

### Hämtning

Hämtning sker när systemet försöker snabbt hitta dokumenten från indexet som uppfyller sökkriterierna. Målet för hämtaren är att få dokument som kommer att användas för att ge kontext och förankra LLM på din data.

Det finns flera sätt att utföra sökning inom vår databas som:

- **Nyckelordssökning** - används för textsökningar

- **Semantisk sökning** - använder den semantiska betydelsen av ord

- **Vektorsökning** - omvandlar dokument från text till vektorrepresentationer med hjälp av inbäddningsmodeller. Hämtning kommer att göras genom att fråga dokumenten vars vektorrepresentationer är närmast användarfrågan.

- **Hybrid** - en kombination av både nyckelord och vektorsökning.

En utmaning med hämtning kommer när det inte finns något liknande svar på frågan i databasen, systemet kommer då att returnera den bästa informationen de kan få, men du kan använda taktiker som att ställa in det maximala avståndet för relevans eller använda hybrid sökning som kombinerar både nyckelord och vektorsökning. I denna lektion kommer vi att använda hybrid sökning, en kombination av både vektor- och nyckelordssökning. Vi kommer att lagra vår data i en dataram med kolumner som innehåller delarna samt inbäddningarna.

### Vektorsimilaritet

Hämtaren kommer att söka genom kunskapsdatabasen efter inbäddningar som är nära varandra, den närmaste grannen, eftersom de är texter som är liknande. I scenariot där en användare ställer en fråga, är den först inbäddad och sedan matchad med liknande inbäddningar. Den vanliga mätningen som används för att hitta hur liknande olika vektorer är är cosinuslikhet som baseras på vinkeln mellan två vektorer.

Vi kan mäta likhet med andra alternativ vi kan använda är Euklidiskt avstånd som är den raka linjen mellan vektorändpunkter och punktprodukt som mäter summan av produkterna av motsvarande element i två vektorer.

### Sökindex

När vi gör hämtning, behöver vi bygga ett sökindex för vår kunskapsbas innan vi utför sökning. Ett index kommer att lagra våra inbäddningar och kan snabbt hämta de mest liknande delarna även i en stor databas. Vi kan skapa vårt index lokalt med:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Omrankning

När du har frågat databasen, kanske du behöver sortera resultaten från de mest relevanta. En omranknings-LLM utnyttjar maskininlärning för att förbättra relevansen av sökresultat genom att ordna dem från de mest relevanta. Med hjälp av Azure AI Search görs omrankning automatiskt för dig med hjälp av en semantisk omrankare. Ett exempel på hur omrankning fungerar med närmaste grannar:

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

## Sammanföra allt

Det sista steget är att lägga till vår LLM i mixen för att kunna få svar som är förankrade i vår data. Vi kan implementera det enligt följande:

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

### Utvärderingsmetoder

- Kvalitet på de svar som ges, säkerställ att det låter naturligt, flytande och mänskligt

- Förankring av datan: utvärdera om svaret kom från de angivna dokumenten

- Relevans: utvärdera om svaret matchar och är relaterat till frågan som ställts

- Flyt - om svaret är grammatiskt korrekt

## Användningsfall för att använda RAG (Retrieval Augmented Generation) och vektordatabaser

Det finns många olika användningsfall där funktionsanrop kan förbättra din app som:

- Fråga och svar: förankra din företagsdata till en chatt som kan användas av anställda för att ställa frågor.

- Rekommendationssystem: där du kan skapa ett system som matchar de mest liknande värdena, t.ex. filmer, restauranger och många fler.

- Chatbottjänster: du kan lagra chattens historia och anpassa konversationen baserat på användardatan.

- Bildsökning baserat på vektor-inbäddningar, användbart vid bildigenkänning och anomalidetektering.

## Sammanfattning

Vi har täckt de grundläggande områdena av RAG från att lägga till vår data till applikationen, användarfrågan och utdata. För att förenkla skapandet av RAG, kan du använda ramverk som Semantic Kernel, Langchain eller Autogen.

## Uppgift

För att fortsätta din inlärning av Retrieval Augmented Generation (RAG) kan du bygga:

- Bygg en front-end för applikationen med hjälp av det ramverk du väljer

- Använd ett ramverk, antingen LangChain eller Semantic Kernel, och återskapa din applikation.

Grattis till att ha slutfört lektionen 👏.

## Lärandet slutar inte här, fortsätt resan

Efter att ha slutfört denna lektion, kolla in vår [Generativ AI-inlärningssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap inom generativ AI!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.