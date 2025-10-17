<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T19:18:29+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "no"
}
-->
# Bygge søkeapplikasjoner

[![Introduksjon til Generativ AI og Store Språkmodeller](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.no.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Klikk på bildet ovenfor for å se videoen til denne leksjonen_

LLM-er handler om mer enn bare chatbots og tekstgenerering. Det er også mulig å bygge søkeapplikasjoner ved hjelp av Embeddings. Embeddings er numeriske representasjoner av data, også kjent som vektorer, og kan brukes til semantisk søk etter data.

I denne leksjonen skal du bygge en søkeapplikasjon for vår utdanningsstartup. Vår startup er en ideell organisasjon som tilbyr gratis utdanning til studenter i utviklingsland. Startuppen har et stort antall YouTube-videoer som studenter kan bruke for å lære om AI. Startuppen ønsker å bygge en søkeapplikasjon som lar studenter søke etter en YouTube-video ved å skrive inn et spørsmål.

For eksempel kan en student skrive inn 'Hva er Jupyter Notebooks?' eller 'Hva er Azure ML', og søkeapplikasjonen vil returnere en liste over YouTube-videoer som er relevante for spørsmålet. Enda bedre, søkeapplikasjonen vil returnere en lenke til stedet i videoen hvor svaret på spørsmålet finnes.

## Introduksjon

I denne leksjonen vil vi dekke:

- Semantisk vs nøkkelordssøk.
- Hva er tekstembeddings.
- Opprette en tekstembedding-indeks.
- Søke i en tekstembedding-indeks.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Skille mellom semantisk og nøkkelordssøk.
- Forklare hva tekstembeddings er.
- Lage en applikasjon som bruker embeddings for å søke etter data.

## Hvorfor bygge en søkeapplikasjon?

Å lage en søkeapplikasjon vil hjelpe deg å forstå hvordan du bruker embeddings for å søke etter data. Du vil også lære hvordan du bygger en søkeapplikasjon som kan brukes av studenter for å finne informasjon raskt.

Leksjonen inkluderer en embedding-indeks av YouTube-transkriptene for Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube-kanalen. AI Show er en YouTube-kanal som lærer deg om AI og maskinlæring. Embedding-indeksen inneholder embeddings for hvert av YouTube-transkriptene frem til oktober 2023. Du vil bruke embedding-indeksen for å bygge en søkeapplikasjon for vår startup. Søkeapplikasjonen returnerer en lenke til stedet i videoen hvor svaret på spørsmålet finnes. Dette er en flott måte for studenter å finne informasjonen de trenger raskt.

Følgende er et eksempel på et semantisk søk for spørsmålet 'kan du bruke rstudio med azure ml?'. Sjekk ut YouTube-URL-en, du vil se at URL-en inneholder et tidsstempel som tar deg til stedet i videoen hvor svaret på spørsmålet finnes.

![Semantisk søk for spørsmålet "kan du bruke rstudio med Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.no.png)

## Hva er semantisk søk?

Nå lurer du kanskje på, hva er semantisk søk? Semantisk søk er en søketeknikk som bruker semantikken, eller betydningen, av ordene i en forespørsel for å returnere relevante resultater.

Her er et eksempel på et semantisk søk. La oss si at du ønsker å kjøpe en bil, du kan søke etter 'min drømmebil'. Semantisk søk forstår at du ikke `drømmer` om en bil, men heller ser etter din `ideelle` bil. Semantisk søk forstår intensjonen din og returnerer relevante resultater. Alternativet er `nøkkelordssøk`, som bokstavelig talt ville søkt etter drømmer om biler og ofte returnert irrelevante resultater.

## Hva er tekstembeddings?

[Tekstembeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) er en teknikk for tekstrepresentasjon som brukes i [naturlig språkbehandling](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Tekstembeddings er semantiske numeriske representasjoner av tekst. Embeddings brukes til å representere data på en måte som er lett for en maskin å forstå. Det finnes mange modeller for å lage tekstembeddings, i denne leksjonen vil vi fokusere på å generere embeddings ved hjelp av OpenAI Embedding Model.

Her er et eksempel: Tenk deg at følgende tekst er i et transkript fra en av episodene på AI Show YouTube-kanalen:

```text
Today we are going to learn about Azure Machine Learning.
```

Vi sender teksten til OpenAI Embedding API, og den returnerer følgende embedding som består av 1536 tall, også kjent som en vektor. Hvert tall i vektoren representerer et annet aspekt av teksten. For korthetens skyld er her de første 10 tallene i vektoren.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Hvordan opprettes embedding-indeksen?

Embedding-indeksen for denne leksjonen ble opprettet med en serie Python-skript. Du finner skriptene sammen med instruksjoner i [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) i 'scripts'-mappen for denne leksjonen. Du trenger ikke å kjøre disse skriptene for å fullføre denne leksjonen, da embedding-indeksen er gitt til deg.

Skriptene utfører følgende operasjoner:

1. Transkriptet for hver YouTube-video i [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1)-spillelisten lastes ned.
2. Ved hjelp av [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) forsøkes det å hente ut navnet på foredragsholderen fra de første 3 minuttene av YouTube-transkriptet. Navnet på foredragsholderen for hver video lagres i embedding-indeksen kalt `embedding_index_3m.json`.
3. Transkriptteksten deles deretter opp i **3-minutters tekstsegmenter**. Segmentet inkluderer omtrent 20 ord som overlapper fra neste segment for å sikre at embedding for segmentet ikke blir avbrutt og for å gi bedre søkekontekst.
4. Hvert tekstsegment sendes deretter til OpenAI Chat API for å oppsummere teksten til 60 ord. Sammendraget lagres også i embedding-indeksen `embedding_index_3m.json`.
5. Til slutt sendes segmentteksten til OpenAI Embedding API. Embedding API returnerer en vektor med 1536 tall som representerer den semantiske betydningen av segmentet. Segmentet sammen med OpenAI Embedding-vektoren lagres i embedding-indeksen `embedding_index_3m.json`.

### Vektordatabaser

For enkelhetens skyld i leksjonen lagres embedding-indeksen i en JSON-fil kalt `embedding_index_3m.json` og lastes inn i en Pandas DataFrame. Men i produksjon ville embedding-indeksen bli lagret i en vektordatabase som [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), for å nevne noen.

## Forstå kosinuslikhet

Vi har lært om tekstembeddings, neste steg er å lære hvordan man bruker tekstembeddings for å søke etter data, og spesielt finne de mest like embeddings til en gitt forespørsel ved hjelp av kosinuslikhet.

### Hva er kosinuslikhet?

Kosinuslikhet er et mål på likhet mellom to vektorer, du vil også høre dette referert til som `nærmeste nabo-søk`. For å utføre et kosinuslikhetssøk må du _vektorisere_ for _forespørselstekst_ ved hjelp av OpenAI Embedding API. Deretter beregner du _kosinuslikheten_ mellom forespørselsvektoren og hver vektor i embedding-indeksen. Husk at embedding-indeksen har en vektor for hvert YouTube-transkripttekstsegment. Til slutt sorterer du resultatene etter kosinuslikhet, og tekstsegmentene med høyest kosinuslikhet er de mest like forespørselen.

Fra et matematisk perspektiv måler kosinuslikhet kosinus til vinkelen mellom to vektorer projisert i et flerdimensjonalt rom. Denne målingen er nyttig, fordi hvis to dokumenter er langt fra hverandre i euklidisk avstand på grunn av størrelse, kan de fortsatt ha en mindre vinkel mellom seg og derfor høyere kosinuslikhet. For mer informasjon om kosinuslikhetsligninger, se [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Bygge din første søkeapplikasjon

Neste steg er å lære hvordan man bygger en søkeapplikasjon ved hjelp av embeddings. Søkeapplikasjonen vil la studenter søke etter en video ved å skrive inn et spørsmål. Søkeapplikasjonen vil returnere en liste over videoer som er relevante for spørsmålet. Søkeapplikasjonen vil også returnere en lenke til stedet i videoen hvor svaret på spørsmålet finnes.

Denne løsningen ble bygget og testet på Windows 11, macOS og Ubuntu 22.04 ved bruk av Python 3.10 eller nyere. Du kan laste ned Python fra [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Oppgave - bygge en søkeapplikasjon for å hjelpe studenter

Vi introduserte vår startup i begynnelsen av denne leksjonen. Nå er det på tide å hjelpe studentene med å bygge en søkeapplikasjon for deres vurderinger.

I denne oppgaven vil du opprette Azure OpenAI Services som vil bli brukt til å bygge søkeapplikasjonen. Du vil opprette følgende Azure OpenAI Services. Du trenger et Azure-abonnement for å fullføre denne oppgaven.

### Start Azure Cloud Shell

1. Logg inn på [Azure-portalen](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Velg Cloud Shell-ikonet øverst til høyre i Azure-portalen.
3. Velg **Bash** som miljøtype.

#### Opprett en ressursgruppe

> For disse instruksjonene bruker vi ressursgruppen kalt "semantic-video-search" i East US.
> Du kan endre navnet på ressursgruppen, men når du endrer plasseringen for ressursene,
> sjekk [modelltilgjengelighetstabellen](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Opprett en Azure OpenAI Service-ressurs

Fra Azure Cloud Shell, kjør følgende kommando for å opprette en Azure OpenAI Service-ressurs.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Hent endepunkt og nøkler for bruk i denne applikasjonen

Fra Azure Cloud Shell, kjør følgende kommandoer for å hente endepunkt og nøkler for Azure OpenAI Service-ressursen.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Distribuer OpenAI Embedding-modellen

Fra Azure Cloud Shell, kjør følgende kommando for å distribuere OpenAI Embedding-modellen.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Løsning

Åpne [løsningsnotatboken](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) i GitHub Codespaces og følg instruksjonene i Jupyter Notebook.

Når du kjører notatboken, vil du bli bedt om å skrive inn en forespørsel. Inndataboksen vil se slik ut:

![Inndataboks for brukeren til å skrive inn en forespørsel](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.no.png)

## Flott arbeid! Fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generativ AI læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå videre til leksjon 9 hvor vi skal se på hvordan man [bygger applikasjoner for bildegenerering](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.