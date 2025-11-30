<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T19:20:47+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "no"
}
-->
# Retrieval Augmented Generation (RAG) og Vektordatabaser

[![Retrieval Augmented Generation (RAG) og Vektordatabaser](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.no.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

I leksjonen om søkeapplikasjoner lærte vi kort hvordan du kan integrere dine egne data i store språkmodeller (LLMs). I denne leksjonen skal vi gå dypere inn i konseptene rundt å forankre dine data i LLM-applikasjoner, mekanismene bak prosessen og metodene for lagring av data, inkludert både embeddings og tekst.

> **Video kommer snart**

## Introduksjon

I denne leksjonen skal vi dekke følgende:

- En introduksjon til RAG, hva det er og hvorfor det brukes i kunstig intelligens (AI).

- Forstå hva vektordatabaser er og opprette en for vår applikasjon.

- Et praktisk eksempel på hvordan man integrerer RAG i en applikasjon.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Forklare betydningen av RAG i datainnhenting og behandling.

- Sette opp en RAG-applikasjon og forankre dine data til en LLM.

- Effektiv integrering av RAG og vektordatabaser i LLM-applikasjoner.

## Vårt scenario: forbedre våre LLM-er med egne data

I denne leksjonen ønsker vi å legge til våre egne notater i utdanningsstart-upen, som lar chatboten få mer informasjon om de ulike emnene. Ved å bruke notatene vi har, vil lærende kunne studere bedre og forstå de ulike temaene, noe som gjør det enklere å forberede seg til eksamen. For å lage vårt scenario, vil vi bruke:

- `Azure OpenAI:` LLM-en vi skal bruke for å lage vår chatbot.

- `AI for nybegynnere-leksjon om nevrale nettverk:` dette vil være dataene vi forankrer vår LLM på.

- `Azure AI Search` og `Azure Cosmos DB:` vektordatabase for å lagre våre data og opprette et søkeindeks.

Brukere vil kunne lage øvingsquizer fra sine notater, repetisjonskort og oppsummere dem til konsise oversikter. For å komme i gang, la oss se på hva RAG er og hvordan det fungerer:

## Retrieval Augmented Generation (RAG)

En LLM-drevet chatbot behandler brukerforespørsler for å generere svar. Den er designet for å være interaktiv og engasjerer seg med brukere om et bredt spekter av temaer. Imidlertid er dens svar begrenset til konteksten som er gitt og dens grunnleggende treningsdata. For eksempel har GPT-4 en kunnskapsgrense fra september 2021, noe som betyr at den mangler kunnskap om hendelser som har skjedd etter denne perioden. I tillegg utelukker dataene som brukes til å trene LLM-er konfidensiell informasjon som personlige notater eller en bedrifts produktmanual.

### Hvordan RAGs (Retrieval Augmented Generation) fungerer

![tegning som viser hvordan RAGs fungerer](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.no.png)

Anta at du ønsker å distribuere en chatbot som lager quizer fra dine notater, da vil du trenge en tilkobling til kunnskapsbasen. Her kommer RAG til unnsetning. RAGs fungerer som følger:

- **Kunnskapsbase:** Før innhenting må disse dokumentene behandles og forberedes, vanligvis ved å dele opp store dokumenter i mindre deler, transformere dem til tekstembeddings og lagre dem i en database.

- **Brukerforespørsel:** brukeren stiller et spørsmål.

- **Innhenting:** Når en bruker stiller et spørsmål, henter embedding-modellen relevant informasjon fra vår kunnskapsbase for å gi mer kontekst som vil bli innlemmet i forespørselen.

- **Forsterket generering:** LLM-en forbedrer sitt svar basert på de innhentede dataene. Dette gjør at det genererte svaret ikke bare er basert på forhåndstrente data, men også relevant informasjon fra den ekstra konteksten. De innhentede dataene brukes til å forsterke LLM-ens svar. LLM-en returnerer deretter et svar på brukerens spørsmål.

![tegning som viser RAGs arkitektur](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.no.png)

Arkitekturen for RAGs implementeres ved hjelp av transformatorer som består av to deler: en encoder og en decoder. For eksempel, når en bruker stiller et spørsmål, blir input-teksten 'kodet' til vektorer som fanger meningen med ordene, og vektorene blir 'dekodet' inn i vårt dokumentindeks og genererer ny tekst basert på brukerforespørselen. LLM-en bruker både en encoder-decoder-modell for å generere output.

To tilnærminger ved implementering av RAG ifølge den foreslåtte artikkelen: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) er:

- **_RAG-Sequence_** bruker innhentede dokumenter for å forutsi det beste mulige svaret på en brukerforespørsel.

- **RAG-Token** bruker dokumenter for å generere neste token, deretter henter dem for å svare på brukerens forespørsel.

### Hvorfor bruke RAGs?

- **Informasjonsrikdom:** sikrer at tekstsvar er oppdaterte og aktuelle. Det forbedrer derfor ytelsen på domene-spesifikke oppgaver ved å få tilgang til den interne kunnskapsbasen.

- Reduserer fabrikasjon ved å bruke **verifiserbare data** i kunnskapsbasen for å gi kontekst til brukerforespørsler.

- Det er **kostnadseffektivt** da de er mer økonomiske sammenlignet med finjustering av en LLM.

## Opprette en kunnskapsbase

Vår applikasjon er basert på våre personlige data, dvs. leksjonen om nevrale nettverk fra AI For Beginners-kurset.

### Vektordatabaser

En vektordatabase, i motsetning til tradisjonelle databaser, er en spesialisert database designet for å lagre, administrere og søke i embedded vektorer. Den lagrer numeriske representasjoner av dokumenter. Å bryte ned data til numeriske embeddings gjør det enklere for vårt AI-system å forstå og behandle dataene.

Vi lagrer våre embeddings i vektordatabaser da LLM-er har en grense for antall tokens de aksepterer som input. Siden du ikke kan sende hele embeddings til en LLM, må vi dele dem opp i mindre deler, og når en bruker stiller et spørsmål, vil embeddings som ligner mest på spørsmålet bli returnert sammen med forespørselen. Oppdeling reduserer også kostnadene for antall tokens som sendes gjennom en LLM.

Noen populære vektordatabaser inkluderer Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant og DeepLake. Du kan opprette en Azure Cosmos DB-modell ved hjelp av Azure CLI med følgende kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Fra tekst til embeddings

Før vi lagrer våre data, må vi konvertere dem til vektor-embeddings før de lagres i databasen. Hvis du arbeider med store dokumenter eller lange tekster, kan du dele dem opp basert på forespørsler du forventer. Oppdeling kan gjøres på setningsnivå eller avsnittsnivå. Siden oppdeling henter mening fra ordene rundt dem, kan du legge til litt annen kontekst til en del, for eksempel ved å legge til dokumenttittelen eller inkludere litt tekst før eller etter delen. Du kan dele opp dataene som følger:

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

Når de er delt opp, kan vi deretter embedde teksten vår ved hjelp av forskjellige embedding-modeller. Noen modeller du kan bruke inkluderer: word2vec, ada-002 fra OpenAI, Azure Computer Vision og mange flere. Valg av modell avhenger av språkene du bruker, typen innhold som kodes (tekst/bilder/lyd), størrelsen på input den kan kode og lengden på embedding-output.

Et eksempel på embedded tekst ved bruk av OpenAIs `text-embedding-ada-002`-modell er:
![en embedding av ordet katt](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.no.png)

## Innhenting og vektorsøk

Når en bruker stiller et spørsmål, transformerer innhenteren det til en vektor ved hjelp av forespørselskoderen, og søker deretter gjennom vårt dokumentindeks for relevante vektorer i dokumentet som er relatert til input. Når dette er gjort, konverterer den både input-vektoren og dokumentvektorene til tekst og sender det gjennom LLM-en.

### Innhenting

Innhenting skjer når systemet prøver å raskt finne dokumentene fra indeksen som tilfredsstiller søkekriteriene. Målet med innhenteren er å få dokumenter som vil bli brukt til å gi kontekst og forankre LLM-en på dine data.

Det finnes flere måter å utføre søk i vår database, som:

- **Nøkkelordssøk** - brukes for tekstsøk.

- **Semantisk søk** - bruker den semantiske betydningen av ord.

- **Vektorsøk** - konverterer dokumenter fra tekst til vektorrepresentasjoner ved hjelp av embedding-modeller. Innhenting vil bli gjort ved å søke etter dokumenter hvis vektorrepresentasjoner er nærmest brukerens spørsmål.

- **Hybrid** - en kombinasjon av både nøkkelord og vektorsøk.

En utfordring med innhenting oppstår når det ikke finnes et lignende svar på forespørselen i databasen. Systemet vil da returnere den beste informasjonen de kan finne. Du kan imidlertid bruke taktikker som å sette opp maksimal avstand for relevans eller bruke hybrid søk som kombinerer både nøkkelord og vektorsøk. I denne leksjonen vil vi bruke hybrid søk, en kombinasjon av både vektor- og nøkkelordssøk. Vi vil lagre våre data i en dataframe med kolonner som inneholder delene samt embeddings.

### Vektorsimilaritet

Innhenteren vil søke gjennom kunnskapsdatabasen etter embeddings som er nær hverandre, den nærmeste naboen, da de er tekster som er like. I scenarioet der en bruker stiller en forespørsel, blir den først embeddet og deretter matchet med lignende embeddings. Den vanlige målingen som brukes for å finne hvor like forskjellige vektorer er, er cosinus-similaritet, som er basert på vinkelen mellom to vektorer.

Vi kan måle similaritet ved hjelp av andre alternativer som Euklidisk avstand, som er den rette linjen mellom vektorendepunkter, og prikkprodukt, som måler summen av produktene av tilsvarende elementer i to vektorer.

### Søkeindeks

Når vi utfører innhenting, må vi bygge en søkeindeks for vår kunnskapsbase før vi utfører søk. En indeks vil lagre våre embeddings og kan raskt hente de mest lignende delene selv i en stor database. Vi kan opprette vår indeks lokalt ved hjelp av:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

Når du har spurt databasen, kan det være nødvendig å sortere resultatene fra de mest relevante. En re-ranking LLM bruker maskinlæring for å forbedre relevansen av søkeresultater ved å ordne dem fra de mest relevante. Ved bruk av Azure AI Search, blir re-ranking gjort automatisk for deg ved hjelp av en semantisk re-ranker. Et eksempel på hvordan re-ranking fungerer ved bruk av nærmeste naboer:

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

## Sette alt sammen

Det siste steget er å legge til vår LLM i miksen for å kunne få svar som er forankret i våre data. Vi kan implementere det som følger:

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

## Evaluering av vår applikasjon

### Evalueringsmetoder

- Kvaliteten på de leverte svarene, og sikre at de høres naturlige, flytende og menneskelige ut.

- Forankring av data: evaluere om svaret kom fra de leverte dokumentene.

- Relevans: evaluere om svaret samsvarer med og er relatert til det stilte spørsmålet.

- Flyt - om svaret gir mening grammatisk.

## Bruksområder for RAG (Retrieval Augmented Generation) og vektordatabaser

Det finnes mange ulike bruksområder der funksjonskall kan forbedre din app, som:

- Spørsmål og svar: forankre dine bedriftsdata til en chat som kan brukes av ansatte til å stille spørsmål.

- Anbefalingssystemer: der du kan lage et system som matcher de mest lignende verdiene, f.eks. filmer, restauranter og mye mer.

- Chatbot-tjenester: du kan lagre chathistorikk og tilpasse samtalen basert på brukerdata.

- Bildesøk basert på vektor-embeddings, nyttig ved bildegjenkjenning og avviksdeteksjon.

## Oppsummering

Vi har dekket de grunnleggende områdene av RAG fra å legge til våre data i applikasjonen, brukerforespørselen og output. For å forenkle opprettelsen av RAG, kan du bruke rammeverk som Semantic Kernel, Langchain eller Autogen.

## Oppgave

For å fortsette din læring om Retrieval Augmented Generation (RAG) kan du bygge:

- Lag en front-end for applikasjonen ved hjelp av rammeverket du ønsker.

- Bruk et rammeverk, enten LangChain eller Semantic Kernel, og gjenskap applikasjonen din.

Gratulerer med å ha fullført leksjonen 👏.

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om generativ AI!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.