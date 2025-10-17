<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T18:58:56+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "sv"
}
-->
# Bygga sökapplikationer

[![Introduktion till Generativ AI och Stora Språkmodeller](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.sv.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Klicka på bilden ovan för att se videon för denna lektion_

Det finns mer att utforska med LLMs än bara chatbotar och textgenerering. Det är också möjligt att bygga sökapplikationer med hjälp av Embeddings. Embeddings är numeriska representationer av data, även kända som vektorer, och kan användas för semantisk sökning av data.

I denna lektion ska du bygga en sökapplikation för vår utbildningsstartup. Vår startup är en ideell organisation som erbjuder gratis utbildning till studenter i utvecklingsländer. Startupen har ett stort antal YouTube-videor som studenter kan använda för att lära sig om AI. Startupen vill bygga en sökapplikation som gör det möjligt för studenter att söka efter en YouTube-video genom att skriva en fråga.

Till exempel kan en student skriva in 'Vad är Jupyter Notebooks?' eller 'Vad är Azure ML' och sökapplikationen kommer att returnera en lista med YouTube-videor som är relevanta för frågan, och ännu bättre, sökapplikationen kommer att returnera en länk till den plats i videon där svaret på frågan finns.

## Introduktion

I denna lektion kommer vi att täcka:

- Semantisk vs nyckelordssökning.
- Vad är Text Embeddings.
- Skapa ett Text Embeddings Index.
- Söka i ett Text Embeddings Index.

## Lärandemål

Efter att ha avslutat denna lektion kommer du att kunna:

- Förstå skillnaden mellan semantisk och nyckelordssökning.
- Förklara vad Text Embeddings är.
- Skapa en applikation med Embeddings för att söka efter data.

## Varför bygga en sökapplikation?

Att skapa en sökapplikation hjälper dig att förstå hur man använder Embeddings för att söka efter data. Du kommer också att lära dig hur man bygger en sökapplikation som kan användas av studenter för att snabbt hitta information.

Lektionens Embedding Index innehåller transkriptioner från YouTube-videor på Microsofts [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube-kanal. AI Show är en YouTube-kanal som lär dig om AI och maskininlärning. Embedding Index innehåller Embeddings för varje YouTube-transkription fram till oktober 2023. Du kommer att använda Embedding Index för att bygga en sökapplikation för vår startup. Sökapplikationen returnerar en länk till den plats i videon där svaret på frågan finns. Detta är ett utmärkt sätt för studenter att snabbt hitta den information de behöver.

Följande är ett exempel på en semantisk fråga för frågan 'kan du använda rstudio med azure ml?'. Kolla in YouTube-URL:en, du kommer att se att URL:en innehåller en tidsstämpel som tar dig till den plats i videon där svaret på frågan finns.

![Semantisk fråga för frågan "kan du använda rstudio med Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.sv.png)

## Vad är semantisk sökning?

Nu kanske du undrar, vad är semantisk sökning? Semantisk sökning är en sökteknik som använder semantiken, eller betydelsen, av orden i en fråga för att returnera relevanta resultat.

Här är ett exempel på semantisk sökning. Låt oss säga att du letar efter att köpa en bil, du kanske söker efter 'min drömbil', semantisk sökning förstår att du inte `drömmer` om en bil, utan snarare letar efter att köpa din `ideala` bil. Semantisk sökning förstår din avsikt och returnerar relevanta resultat. Alternativet är `nyckelordssökning` som bokstavligen skulle söka efter drömmar om bilar och ofta returnera irrelevanta resultat.

## Vad är Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) är en teknik för textrepresentation som används inom [naturlig språkbehandling](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings är semantiska numeriska representationer av text. Embeddings används för att representera data på ett sätt som är lätt för en maskin att förstå. Det finns många modeller för att skapa text embeddings, och i denna lektion kommer vi att fokusera på att generera embeddings med OpenAI Embedding Model.

Här är ett exempel, föreställ dig att följande text finns i en transkription från ett avsnitt på AI Show YouTube-kanalen:

```text
Today we are going to learn about Azure Machine Learning.
```

Vi skickar texten till OpenAI Embedding API och det skulle returnera följande embedding bestående av 1536 siffror, även kallad en vektor. Varje siffra i vektorn representerar en annan aspekt av texten. För korthetens skull är här de första 10 siffrorna i vektorn.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Hur skapas Embedding Index?

Embedding Index för denna lektion skapades med en serie Python-skript. Du hittar skripten tillsammans med instruktioner i [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) i mappen 'scripts' för denna lektion. Du behöver inte köra dessa skript för att slutföra denna lektion eftersom Embedding Index tillhandahålls för dig.

Skripten utför följande operationer:

1. Transkriptionen för varje YouTube-video i [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) spellistan laddas ner.
2. Med hjälp av [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) görs ett försök att extrahera talarens namn från de första 3 minuterna av YouTube-transkriptionen. Talarens namn för varje video lagras i Embedding Index som heter `embedding_index_3m.json`.
3. Transkriptionstexten delas sedan upp i **3-minuters textsegment**. Segmentet inkluderar cirka 20 ord som överlappar från nästa segment för att säkerställa att Embedding för segmentet inte avbryts och för att ge bättre sökkontext.
4. Varje textsegment skickas sedan till OpenAI Chat API för att sammanfatta texten till 60 ord. Sammanfattningen lagras också i Embedding Index `embedding_index_3m.json`.
5. Slutligen skickas segmenttexten till OpenAI Embedding API. Embedding API returnerar en vektor med 1536 siffror som representerar den semantiska betydelsen av segmentet. Segmentet tillsammans med OpenAI Embedding-vektorn lagras i Embedding Index `embedding_index_3m.json`.

### Vektordatabaser

För enkelhetens skull i lektionen lagras Embedding Index i en JSON-fil som heter `embedding_index_3m.json` och laddas in i en Pandas DataFrame. Men i produktion skulle Embedding Index lagras i en vektordatabas som [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), för att nämna några.

## Förstå kosinuslikhet

Vi har lärt oss om text embeddings, nästa steg är att lära oss hur man använder text embeddings för att söka efter data och särskilt hitta de mest liknande embeddings till en given fråga med hjälp av kosinuslikhet.

### Vad är kosinuslikhet?

Kosinuslikhet är ett mått på likhet mellan två vektorer, du kommer också att höra detta refereras till som `närmaste grann-sökning`. För att utföra en kosinuslikhetssökning behöver du _vektorisera_ för _fråge_text med hjälp av OpenAI Embedding API. Sedan beräknar du _kosinuslikheten_ mellan frågevektorn och varje vektor i Embedding Index. Kom ihåg att Embedding Index har en vektor för varje YouTube-transkriptionstextsegment. Slutligen sorterar du resultaten efter kosinuslikhet och textsegmenten med högst kosinuslikhet är de mest liknande frågan.

Ur ett matematiskt perspektiv mäter kosinuslikhet kosinus för vinkeln mellan två vektorer projicerade i ett multidimensionellt utrymme. Denna mätning är fördelaktig, eftersom om två dokument är långt ifrån varandra enligt euklidiskt avstånd på grund av storlek, kan de fortfarande ha en mindre vinkel mellan sig och därmed högre kosinuslikhet. För mer information om kosinuslikhetsekvationer, se [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Bygga din första sökapplikation

Nästa steg är att lära oss hur man bygger en sökapplikation med Embeddings. Sökapplikationen gör det möjligt för studenter att söka efter en video genom att skriva en fråga. Sökapplikationen returnerar en lista med videor som är relevanta för frågan. Sökapplikationen returnerar också en länk till den plats i videon där svaret på frågan finns.

Denna lösning byggdes och testades på Windows 11, macOS och Ubuntu 22.04 med Python 3.10 eller senare. Du kan ladda ner Python från [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Uppgift - bygga en sökapplikation för att möjliggöra för studenter

Vi introducerade vår startup i början av denna lektion. Nu är det dags att möjliggöra för studenterna att bygga en sökapplikation för sina bedömningar.

I denna uppgift kommer du att skapa Azure OpenAI Services som kommer att användas för att bygga sökapplikationen. Du kommer att skapa följande Azure OpenAI Services. Du behöver ett Azure-abonnemang för att slutföra denna uppgift.

### Starta Azure Cloud Shell

1. Logga in på [Azure-portalen](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Välj Cloud Shell-ikonen i det övre högra hörnet av Azure-portalen.
3. Välj **Bash** som miljötyp.

#### Skapa en resursgrupp

> För dessa instruktioner använder vi resursgruppen med namnet "semantic-video-search" i East US.
> Du kan ändra namnet på resursgruppen, men när du ändrar platsen för resurserna,
> kontrollera [modellens tillgänglighetstabell](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Skapa en Azure OpenAI Service-resurs

Från Azure Cloud Shell, kör följande kommando för att skapa en Azure OpenAI Service-resurs.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Hämta endpoint och nycklar för användning i denna applikation

Från Azure Cloud Shell, kör följande kommandon för att hämta endpoint och nycklar för Azure OpenAI Service-resursen.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Distribuera OpenAI Embedding-modellen

Från Azure Cloud Shell, kör följande kommando för att distribuera OpenAI Embedding-modellen.

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

## Lösning

Öppna [lösningsnotebooken](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) i GitHub Codespaces och följ instruktionerna i Jupyter Notebook.

När du kör notebooken kommer du att bli ombedd att ange en fråga. Inmatningsrutan kommer att se ut så här:

![Inmatningsruta för användaren att ange en fråga](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.sv.png)

## Bra jobbat! Fortsätt din inlärning

Efter att ha avslutat denna lektion, kolla in vår [Generativ AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

Gå vidare till Lektion 9 där vi kommer att titta på hur man [bygger applikationer för bildgenerering](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.