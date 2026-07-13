# Retrieval Augmented Generation (RAG) og vektordatabaser

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../translated_images/no/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

I leksjonen om søkeapplikasjoner lærte vi kort hvordan du integrerer egne data i store språkmodeller (LLMs). I denne leksjonen vil vi gå nærmere inn på konseptene rundt å forankre data i din LLM-applikasjon, mekanismene i prosessen og metodene for lagring av data, inkludert både innebygde representasjoner og tekst.

> **Video kommer snart**

## Introduksjon

I denne leksjonen vil vi dekke følgende:

- En introduksjon til RAG, hva det er og hvorfor det brukes i KI (kunstig intelligens).

- Forstå hva vektordatabaser er og opprette en for vår applikasjon.

- Et praktisk eksempel på hvordan integrere RAG i en applikasjon.

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Forklare betydningen av RAG innen datahenting og prosessering.

- Sette opp en RAG-applikasjon og forankre dine data til en LLM

- Effektiv integrering av RAG og vektordatabaser i LLM-applikasjoner.

## Vårt scenario: forbedring av våre LLM-er med egne data

For denne leksjonen ønsker vi å legge til egne notater i utdanningsoppstarten, noe som gjør at chatboten kan få mer informasjon om ulike fag. Ved å bruke notatene vi har, vil elever kunne studere bedre og forstå de forskjellige temaene, noe som gjør det enklere å repetere til eksamen. For å lage vårt scenario vil vi bruke:

- `Azure OpenAI:` LLM-en vi vil bruke for å lage chatboten vår

- `AI for beginners' lesson on Neural Networks`: dette vil være dataene vi forankrer vår LLM på

- `Azure AI Search` og `Azure Cosmos DB:` vektordatabasen for å lagre våre data og opprette en søkeindeks

Brukere vil kunne opprette øvings-quizzer fra sine notater, repetisjonskort og oppsummere til konsise oversikter. For å komme i gang, la oss se på hva RAG er og hvordan det fungerer:

## Retrieval Augmented Generation (RAG)

En LLM-drevet chatbot prosesserer brukerforespørsler for å generere svar. Den er designet for å være interaktiv og engasjerer brukere på en rekke emner. Imidlertid er svarene begrenset til konteksten som tilbys og dens grunnleggende treningsdata. For eksempel er GPT-4s kunnskapsavskjæring september 2021, noe som betyr at den mangler kunnskap om hendelser som har skjedd etter denne perioden. I tillegg ekskluderer treningsdataene for LLM-er konfidensiell informasjon som personlige notater eller en bedrifts produktmanual.

### Hvordan RAGs (Retrieval Augmented Generation) fungerer

![tegning som viser hvordan RAGs fungerer](../../../translated_images/no/how-rag-works.f5d0ff63942bd3a6.webp)

Anta at du ønsker å distribuere en chatbot som lager quizzer fra dine notater, da trenger du en tilkobling til kunnskapsbasen. Det er her RAG kommer til unnsetning. RAGs opererer slik:

- **Kunnskapsbase:** Før henting må dokumentene inntas og forklares, vanligvis ved å dele opp store dokumenter i mindre biter, konvertere dem til tekst-embedding og lagre dem i en database.

- **Brukerspørsmål:** brukeren stiller et spørsmål

- **Henting:** Når en bruker stiller et spørsmål, henter innebyggingsmodellen relevant informasjon fra vår kunnskapsbase for å gi mer kontekst som legges inn i prompten.

- **Forsterket generering:** LLM-en forbedrer svaret basert på hentede data. Det tillater at svaret ikke bare baserer seg på forhåndstrent data, men også relevant informasjon fra tilleggs-konteksten. De hentede dataene brukes til å forsterke LLM-ens svar. Deretter returnerer LLM et svar på brukerens spørsmål.

![tegning som viser hvordan RAGs arkitektur fungerer](../../../translated_images/no/encoder-decode.f2658c25d0eadee2.webp)

Arkitekturen for RAGs implementeres ved hjelp av transformere bestående av to deler: en kodekoder og en dekoder. For eksempel, når en bruker stiller et spørsmål, kodes inntekst til vektorer som fanger betydningen av ord, og vektorene dekodes i vårt dokumentindeks og genererer ny tekst basert på brukerens spørsmål. LLM bruker både en koder-dekoder modell for å generere utdata.

To tilnærminger når man implementerer RAG i henhold til den foreslåtte artikkelen: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) er:

- **_RAG-Sequence_** bruker hentede dokumenter for å forutsi det beste mulige svaret på et brukerspørsmål

- **RAG-Token** bruker dokumenter til å generere neste token, og henter dem deretter for å svare på brukerens spørsmål

### Hvorfor bruke RAGs? 

- **Informasjonsrikdom:** sikrer at tekstsvar er oppdaterte og aktuelle. Det forbedrer derfor ytelsen på domene-spesifikke oppgaver ved å få tilgang til intern kunnskapsbase.

- Reduserer fabrikasjon ved å benytte **verifiserbar data** i kunnskapsbasen for å gi kontekst til brukerspørsmål.

- Det er **kostnadseffektivt** da det er mer økonomisk sammenlignet med finjustering av en LLM

## Opprette en kunnskapsbase

Applikasjonen vår er basert på våre personlige data, dvs. Neural Network-leksjonen i AI For Beginners pensum.

### Vektordatabaser

En vektordatabasen er, i motsetning til tradisjonelle databaser, en spesialisert database designet for å lagre, håndtere og søke i innebygde vektorer. Den lagrer numeriske representasjoner av dokumenter. Å bryte ned data til numeriske embeddings gjør det enklere for AI-systemet vårt å forstå og bearbeide dataene.

Vi lagrer våre embeddings i vektordatabaser fordi LLM-er har en grense for hvor mange tokens de aksepterer som input. Siden du ikke kan sende hele embeddingene til en LLM, må vi dele dem opp i biter, og når en bruker stiller et spørsmål, vil de embeddingene som mest ligner spørsmålet bli returnert sammen med prompten. Oppdeling reduserer også kostnader knyttet til antall tokens sendt gjennom en LLM.

Noen populære vektordatabaser inkluderer Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant og DeepLake. Du kan opprette en Azure Cosmos DB-modell ved å bruke Azure CLI med følgende kommando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Fra tekst til embeddings

Før vi lagrer dataene våre, må vi konvertere dem til vektor-embeddings før de lagres i databasen. Dersom du arbeider med store dokumenter eller lange tekster, kan du dele dem opp basert på forespørsler du forventer. Oppdeling kan gjøres på setningsnivå eller avsnittsnivå. Siden oppdeling utleder mening fra ordene rundt dem, kan du legge til annen kontekst i et avsnitt, for eksempel ved å legge til dokumenttittel eller inkludere tekst før eller etter avsnittet. Du kan dele opp dataene som følger:

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

    # Hvis den siste delen ikke nådde minimum lengde, legg den til likevel
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Når dataene er delt opp, kan vi så embedde teksten med forskjellige embedding-modeller. Noen modeller du kan bruke inkluderer: word2vec, ada-002 av OpenAI, Azure Computer Vision og mange flere. Valg av modell avhenger av språkene du bruker, typen innhold som kodes (tekst/bilder/lyd), størrelsen på inndata den kan kode og lengden på embedded output.

Et eksempel på embedded tekst ved bruk av OpenAIs `text-embedding-ada-002` modell er:
![embedding av ordet katt](../../../translated_images/no/cat.74cbd7946bc9ca38.webp)

## Henting og vektorsøk

Når en bruker stiller et spørsmål, omformer henteren det til en vektor ved bruk av spørringskoderen. Den søker deretter gjennom vårt dokumentsøkeindeks etter relevante vektorer i dokumentet som er relatert til inndataen. Når det er gjort, konverteres både inndatavektor og dokumentvektorer til tekst og sendes gjennom LLM.

### Henting

Henting skjer når systemet prøver å raskt finne dokumentene i indeksen som oppfyller søkekriteriene. Målet til henteren er å hente dokumenter som kan brukes til å gi kontekst og forankre LLM i dine data.

Det finnes flere måter å utføre søk i databasen vår på, som:

- **Nøkkelordsøk** - brukt for tekstsøk

- **Vektorsøk** - konverterer dokumenter fra tekst til vektorreprensentasjoner ved bruk av embedding-modeller, noe som tillater et **semantisk søk** ved bruk av ords mening. Henting utføres ved å spørre de dokumentene hvis vektorreprensentasjoner er nærmest brukerens spørsmål.

- **Hybrid** - en kombinasjon av både nøkkelord- og vektorsøk.

En utfordring med henting oppstår når det ikke finnes noe lignende svar på forespørselen i databasen; systemet vil da returnere den beste informasjonen det kan finne. Du kan imidlertid bruke taktikker som å sette maksimal avstand for relevans eller bruke hybridsøk, som kombinerer både nøkkelord- og vektorsøk. I denne leksjonen vil vi bruke hybridsøk, en kombinasjon av både vektor- og nøkkelordssøk. Vi lagrer dataene våre i en dataframe med kolonner som inneholder biter samt embeddings.

### Vektorsimilartet

Henteren søker gjennom kunnskapsdatabasen etter embeddings som er nær hverandre, den nærmeste nabo, siden de er tekster som er like. I scenariet stiller en bruker et spørsmål, som først embeddes og deretter matches med lignende embeddings. Den vanlige målingen som brukes for å finne hvor like forskjellige vektorer er, er cosinuslikhet basert på vinkelen mellom to vektorer.

Vi kan måle likhet ved bruk av andre alternativer som du kan bruke er Euklidisk avstand, som er den rette linjen mellom vektorendepunktene, og prikkprodukt som måler summen av produktene av tilsvarende elementer i to vektorer.

### Søkeindeks

Når vi gjør henting, må vi bygge en søkeindeks for kunnskapsbasen vår før vi utfører søk. En indeks lagrer embeddingene våre og kan raskt hente de mest lignende bitene selv i en stor database. Vi kan opprette indeksen vår lokalt ved bruk av:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Opprett søkeindeksen
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# For å søke i indeksen kan du bruke kneighbors-metoden
distances, indices = nbrs.kneighbors(embeddings)
```

### Omrangering

Når du har spurt databasen, kan det være behov for å sortere resultatene fra de mest relevante. En omrangering LLM benytter maskinlæring for å forbedre relevansen av søkeresultater ved å ordne dem fra mest relevant. Ved bruk av Azure AI Search skjer omrangering automatisk med en semantisk omrangering. Et eksempel på hvordan omrangering fungerer ved bruk av nærmeste naboer:

```python
# Finn de mest lignende dokumentene
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Skriv ut de mest lignende dokumentene
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Å sette det hele sammen

Det siste steget er å legge til vår LLM i prosessen for å kunne få svar som er forankret i våre data. Vi kan implementere det som følger:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Konverter spørsmålet til en spørringsvektor
    query_vector = create_embeddings(user_input)

    # Finn de mest lignende dokumentene
    distances, indices = nbrs.kneighbors([query_vector])

    # legg til dokumenter til spørringen for å gi kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # kombiner historikken og brukerinnputten
    history.append(user_input)

    # opprett et melding-objekt
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # bruk Responses API for å generere et svar
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

## Evaluering av applikasjonen vår

### Evalueringsmetrikker

- Kvalitet på de leverte svarene, som sikrer at de høres naturlige, flytende og menneskelige ut

- Forankring av data: evaluere om svaret kom fra de oppgitte dokumentene

- Relevans: evaluere om svaret stemmer overens og er relatert til det stilte spørsmålet

- Flyt: hvorvidt svaret gir grammatisk mening

## Bruksområder for RAG (Retrieval Augmented Generation) og vektordatabaser

Det finnes mange ulike bruksområder hvor funksjonskall kan forbedre appen din, slik som:

- Spørsmål og svar: forankre firmaets data til en chat som kan brukes av ansatte til å stille spørsmål.

- Anbefalingssystemer: der du kan lage et system som matcher de mest lignende verdiene, f.eks. filmer, restauranter og mye mer.

- Chatbot-tjenester: du kan lagre chattehistorikk og personliggjøre samtalen basert på brukerdata.

- Bildesøk basert på vektor-embeddings, nyttig ved bilde- og anomalideteksjon.

## Oppsummering

Vi har dekket grunnleggende områder rundt RAG fra å legge til våre data i applikasjonen, brukerforespørsel og output. For å forenkle opprettelsen av RAG kan du bruke rammeverk som Semantic Kernel, Langchain eller Autogen.

## Oppgave

For å fortsette din læring om Retrieval Augmented Generation (RAG) kan du bygge:

- Lag et front-end for applikasjonen ved å bruke rammeverket du foretrekker

- Bruk et rammeverk, enten LangChain eller Semantic Kernel, og gjenskap applikasjonen din.

Gratulerer med å ha fullført leksjonen 👏.

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å styrke din kunnskap om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->