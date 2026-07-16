# Retrieval Augmented Generation (RAG) och vektordatabaser

[![Retrieval Augmented Generation (RAG) och vektordatabaser](../../../translated_images/sv/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

I lektionen om sökapplikationer lärde vi oss kortfattat hur du integrerar din egen data i stora språkmodeller (LLM). I denna lektion kommer vi att fördjupa oss i koncepten för att förankra din data i din LLM-applikation, processen bakom och metoder för att lagra data, inklusive både inbäddningar och text.

> **Video kommer snart**

## Introduktion

I denna lektion kommer vi att täcka följande:

- En introduktion till RAG, vad det är och varför det används inom AI (artificiell intelligens).

- Förstå vad vektordatabaser är och skapa en för vår applikation.

- Ett praktiskt exempel på hur man integrerar RAG i en applikation.

## Lärandemål

Efter att ha genomfört denna lektion kommer du att kunna:

- Förklara vikten av RAG vid datahämtning och bearbetning.

- Ställa in en RAG-applikation och förankra din data till en LLM

- Effektiv integration av RAG och vektordatabaser i LLM-applikationer.

## Vårt scenario: förbättra våra LLM:er med vår egen data

För denna lektion vill vi lägga till våra egna anteckningar i utbildningsstartupen, vilket låter chatboten få mer information om olika ämnen. Med hjälp av anteckningarna vi har kommer eleverna kunna studera bättre och förstå olika ämnen, vilket gör det lättare att repetera inför prov. För att skapa vårt scenario kommer vi att använda:

- `Azure OpenAI:` den LLM vi kommer använda för att skapa vår chatbot

- `AI for beginners' lesson on Neural Networks`: detta kommer vara datan vi förankrar vår LLM på

- `Azure AI Search` och `Azure Cosmos DB:` vektordatabas för att lagra vår data och skapa ett sökindex

Användare kommer kunna skapa övningsquiz från sina anteckningar, repetitionsflashkort och sammanfatta till korta översikter. För att komma igång, låt oss titta på vad RAG är och hur det fungerar:

## Retrieval Augmented Generation (RAG)

En LLM-drivna chatbot bearbetar användarfrågor för att generera svar. Den är designad för att vara interaktiv och engagerar sig med användare inom många olika ämnen. Dock är dess svar begränsade till den kontext som tillhandahålls och den grundläggande träningsdatan. Till exempel har GPT-4 kunskapsgränsen september 2021, vilket betyder att den saknar kunskap om händelser som inträffat efter detta datum. Dessutom exkluderar den data som används för att träna LLM:er konfidentiell information såsom personliga anteckningar eller ett företags produktmanual.

### Hur RAG (Retrieval Augmented Generation) fungerar

![ritning som visar hur RAG fungerar](../../../translated_images/sv/how-rag-works.f5d0ff63942bd3a6.webp)

Antag att du vill driftsätta en chatbot som skapar quiz från dina anteckningar, du behöver en koppling till kunskapsbasen. Här kommer RAG till undsättning. RAG fungerar på följande sätt:

- **Kunskapsbas:** Innan hämtning måste dessa dokument bearbetas och förbehandlas, vanligtvis genom att dela upp stora dokument i mindre delar, omvandla dem till textinbäddningar och lagra dem i en databas.

- **Användarfråga:** användaren ställer en fråga

- **Hämtning:** När användaren ställer en fråga hämtar inbäddningsmodellen relevant information från vår kunskapsbas för att ge mer kontext som inkluderas i prompten.

- **Förstärkt generering:** LLM förbättrar sitt svar baserat på den hämtade datan. Detta tillåter att genererat svar inte bara baseras på förtränad data utan även relevant information från den tillagda kontexten. Den hämtade datan används för att förstärka LLM:s svar. LLM returnerar sedan ett svar på användarens fråga.

![ritning som visar RAG-arkitekturen](../../../translated_images/sv/encoder-decode.f2658c25d0eadee2.webp)

Arkitekturen för RAG implementeras med hjälp av transformatorer bestående av två delar: en kodare och en avkodare. Till exempel, när en användare ställer en fråga, "kodas" ingångstexten till vektorer som fångar ordens betydelse och vektorerna "avkodas" i vårt dokumentindex och genererar ny text baserat på användarens fråga. LLM använder en kodare-avkodare-modell för att generera utdata.

Två tillvägagångssätt vid implementation av RAG enligt den föreslagna artikeln: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) är:

- **_RAG-Sequencen_** använder hämtade dokument för att förutsäga det bästa möjliga svaret på en användarfråga

- **RAG-Token** använder dokument för att generera nästa token, och hämtar dem därefter för att svara på användarens fråga

### Varför använda RAG? 

- **Informationsrikedom:** säkerställer att textsvar är uppdaterade och aktuella. Förbättrar därför prestandan i domänspecifika uppgifter genom att ha tillgång till den interna kunskapsbasen.

- Minskar fabricering genom att använda **verifierbar data** i kunskapsbasen för att ge kontext till användarfrågor.

- Det är **kostnadseffektivt** eftersom det är mer ekonomiskt jämfört med finjustering av en LLM.

## Skapa en kunskapsbas

Vår applikation baseras på vår personliga data, dvs. lektionen om neurala nätverk i AI för nybörjare-kursen.

### Vektordatabaser

En vektordatabas, till skillnad från traditionella databaser, är en specialiserad databas designad för att lagra, hantera och söka inbäddade vektorer. Den lagrar numeriska representationer av dokument. Att dela upp data till numeriska inbäddningar gör det enklare för vårt AI-system att förstå och bearbeta datan.

Vi lagrar våra inbäddningar i vektordatabaser eftersom LLM har en gräns för antal token de accepterar som input. Eftersom du inte kan skicka hela inbäddningarna till en LLM, behöver vi dela upp dem i delar, och när en användare ställer en fråga, returneras de inbäddningar som mest liknar frågan tillsammans med prompten. Uppdelning minskar även kostnaderna för antalet token som skickas genom en LLM.

Några populära vektordatabaser inkluderar Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant och DeepLake. Du kan skapa en Azure Cosmos DB-modell med Azure CLI med följande kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Från text till inbäddningar

Innan vi lagrar vår data behöver vi konvertera den till vektorinbäddningar innan den lagras i databasen. Om du arbetar med stora dokument eller långa texter kan du dela upp dem baserat på förväntade frågor. Uppdelning kan göras på meningsnivå eller på styckesnivå. Eftersom uppdelning härleder betydelser från orden runt omkring, kan du lägga till ytterligare kontext till en del, till exempel genom att lägga till dokumentets titel eller inkludera lite text före eller efter delen. Du kan dela upp datan enligt följande:

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

    # Om sista biten inte nådde miniminängden, lägg till den ändå
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

När datan är uppdelad kan vi sedan bädda in vår text med olika inbäddningsmodeller. Några modeller du kan använda inkluderar: word2vec, ada-002 från OpenAI, Azure Computer Vision med flera. Val av modell beror på vilka språk du använder, vilken typ av innehåll som kodas (text/bilder/ljud), storleken på ingången det kan koda och längden på inbäddningsutdata.

Ett exempel på inbäddad text med OpenAI:s `text-embedding-ada-002`-modell är:
![en inbäddning av ordet katt](../../../translated_images/sv/cat.74cbd7946bc9ca38.webp)

## Hämtning och vektorsökning

När en användare ställer en fråga omvandlar hämtaren den till en vektor med hjälp av frågekodaren, därefter söker den igenom vårt dokumentindex efter relevanta vektorer i dokumenten som är relaterade till ingången. När detta är gjort omvandlas både ingångsvektorn och dokumentvektorerna till text och skickas till LLM.

### Hämtning

Hämtning sker när systemet försöker snabbt hitta dokument i indexet som uppfyller sökkriterierna. Målet med hämtaren är att få dokument att använda för att ge kontext och förankra LLM på din data.

Det finns flera sätt att söka inom vår databas, till exempel:

- **Nyckelordssökning** - används vid textsökning

- **Vektorsökning** - omvandlar dokument från text till vektorrepresentationer med hjälp av inbäddningsmodeller, vilket möjliggör en **semantisk sökning** baserad på ordens betydelse. Hämtning sker genom att fråga dokument vars vektorrepresentationer är närmast användarens fråga.

- **Hybrid** - en kombination av både nyckelords- och vektorsökning.

En utmaning med hämtning uppstår när det inte finns något liknande svar på frågan i databasen, systemet returnerar då den bästa information de kan, men du kan använda taktiker som att ställa in maximal avstånd för relevans eller använda hybrid sökning som kombinerar både nyckelord och vektorsökning. I den här lektionen använder vi hybrid sökning, en kombination av vektor- och nyckelordssökning. Vi lagrar vår data i en dataframer med kolumner som innehåller både delar och inbäddningar.

### Vektorsimilaritet

Hämtaren söker igenom kunskapsdatabasen efter inbäddningar som ligger nära varandra, närmaste grannen, eftersom de är texter som är liknande. I scenariot där en användare ställer en fråga, bäddas den först in och matchas sedan med liknande inbäddningar. Vanligt mått som används för att mäta hur lika olika vektorer är är cosinuslikhet, som baseras på vinkeln mellan två vektorer.

Vi kan mäta likhet med andra alternativ, till exempel Euklidiskt avstånd som är den raka linjen mellan vektorändpunkterna och skalärprodukt som mäter summan av produkterna av motsvarande element i två vektorer.

### Sökindex

När vi gör hämtning måste vi bygga ett sökindex för vår kunskapsbas innan vi utför sökning. Ett index lagrar våra inbäddningar och kan snabbt hämta de mest liknande delarna även i en stor databas. Vi kan skapa vårt index lokalt med:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Skapa sökindexet
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# För att söka i indexet kan du använda metoden kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Omdirigering av rankning

När du har frågat databasen kan det vara nödvändigt att sortera resultaten från mest relevanta. En omrankande LLM använder maskininlärning för att förbättra relevansen av sökresultat genom att ordna dem från mest relevanta. Med Azure AI Search görs omrankning automatiskt med en semantisk omrankare. Ett exempel på hur omrankning fungerar med närmaste grannar:

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

## Att föra ihop allt

Det sista steget är att lägga till vår LLM i mixen för att kunna få svar som är förankrade i vår data. Vi kan implementera det på följande sätt:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Konvertera frågan till en frågevektor
    query_vector = create_embeddings(user_input)

    # Hitta de mest liknande dokumenten
    distances, indices = nbrs.kneighbors([query_vector])

    # lägg till dokument till frågan för att ge kontext
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # kombinera historiken och användarens indata
    history.append(user_input)

    # skapa ett meddelandeobjekt
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # använd Responses API för att generera ett svar
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Utvärdera vår applikation

### Utvärderingsmått

- Kvalitet på svaren: säkerställa att det låter naturligt, flytande och mänskligt

- Förankring i data: utvärdera om svaret kommer från de angivna dokumenten

- Relevans: utvärdera om svaret matchar och är relaterat till ställd fråga

- Flytande språk - om svaret är grammatiskt korrekt

## Användningsfall för RAG (Retrieval Augmented Generation) och vektordatabaser

Det finns många olika användningsfall där funktionsanrop kan förbättra din app, såsom:

- Frågor och svar: förankra företagets data till en chatt som kan användas av anställda för att ställa frågor.

- Rekommendationssystem: där du kan skapa ett system som matchar de mest lika värdena, till exempel filmer, restauranger med mera.

- Chattbottjänster: du kan spara chattlogg och personifiera konversationen baserat på användardata.

- Bildsökning baserat på vektorinbäddningar, användbart vid bildigenkänning och avvikelsedetektering.

## Sammanfattning

Vi har täckt grundläggande områden av RAG från tillägg av vår data till applikationen, användarfråga och utdata. För att förenkla skapandet av RAG kan du använda ramverk som Semantic Kernel, Langchain eller Autogen.

## Uppgift

För att fortsätta din inlärning av Retrieval Augmented Generation (RAG) kan du bygga:

- Skapa ett frontend för applikationen med valfritt ramverk

- Använd ett ramverk, antingen LangChain eller Semantic Kernel, och återskapa din applikation.

Grattis till att du slutfört lektionen 👏.

## Lärandet slutar inte här, fortsätt resan

Efter att ha avslutat denna lektion, kika in i vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->