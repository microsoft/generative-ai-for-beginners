<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T19:11:16+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "da"
}
-->
# Udforskning og sammenligning af forskellige LLM'er

[![Udforskning og sammenligning af forskellige LLM'er](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.da.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klik på billedet ovenfor for at se videoen til denne lektion_

I den forrige lektion har vi set, hvordan Generativ AI ændrer teknologilandskabet, hvordan store sprogmodeller (LLM'er) fungerer, og hvordan en virksomhed - som vores startup - kan anvende dem til deres brugsscenarier og vokse! I dette kapitel vil vi sammenligne og kontrastere forskellige typer af store sprogmodeller (LLM'er) for at forstå deres fordele og ulemper.

Det næste skridt i vores startups rejse er at udforske det nuværende landskab af LLM'er og forstå, hvilke der er egnede til vores brugsscenarie.

## Introduktion

Denne lektion vil dække:

- Forskellige typer af LLM'er i det nuværende landskab.
- Testning, iteration og sammenligning af forskellige modeller til dit brugsscenarie i Azure.
- Hvordan man implementerer en LLM.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Vælge den rette model til dit brugsscenarie.
- Forstå, hvordan man tester, itererer og forbedrer modellens ydeevne.
- Vide, hvordan virksomheder implementerer modeller.

## Forstå forskellige typer af LLM'er

LLM'er kan kategoriseres på flere måder baseret på deres arkitektur, træningsdata og brugsscenarier. At forstå disse forskelle vil hjælpe vores startup med at vælge den rette model til scenariet og forstå, hvordan man tester, itererer og forbedrer ydeevnen.

Der findes mange forskellige typer af LLM-modeller, og dit valg af model afhænger af, hvad du ønsker at bruge dem til, dine data, hvor meget du er villig til at betale og mere.

Afhængigt af om du ønsker at bruge modellerne til tekst, lyd, video, billedgenerering osv., kan du vælge en anden type model.

- **Lyd- og talegenkendelse**. Til dette formål er Whisper-typen modeller et godt valg, da de er alsidige og rettet mod talegenkendelse. De er trænet på mangfoldig lyd og kan udføre flersproget talegenkendelse. Læs mere om [Whisper-typen modeller her](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Billedgenerering**. Til billedgenerering er DALL-E og Midjourney to meget kendte valg. DALL-E tilbydes af Azure OpenAI. [Læs mere om DALL-E her](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) og også i kapitel 9 af dette pensum.

- **Tekstgenerering**. De fleste modeller er trænet til tekstgenerering, og du har et stort udvalg fra GPT-3.5 til GPT-4. De kommer med forskellige omkostninger, hvor GPT-4 er den dyreste. Det er værd at undersøge [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) for at evaluere, hvilke modeller der bedst passer til dine behov med hensyn til kapacitet og omkostninger.

- **Multimodalitet**. Hvis du ønsker at håndtere flere typer data i input og output, kan du overveje modeller som [gpt-4 turbo med vision eller gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - de nyeste udgivelser af OpenAI-modeller - som er i stand til at kombinere naturlig sprogbehandling med visuel forståelse, hvilket muliggør interaktioner gennem multimodale grænseflader.

At vælge en model betyder, at du får nogle grundlæggende kapaciteter, som dog måske ikke er tilstrækkelige. Ofte har du virksomhedsspecifikke data, som du på en eller anden måde skal informere LLM'en om. Der er flere forskellige måder at gribe dette an på, mere om det i de kommende afsnit.

### Grundlæggende modeller versus LLM'er

Begrebet Grundlæggende Model blev [skabt af Stanford-forskere](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) og defineret som en AI-model, der opfylder nogle kriterier, såsom:

- **De er trænet ved hjælp af usuperviseret læring eller selv-superviseret læring**, hvilket betyder, at de er trænet på ulabelerede multimodale data og ikke kræver menneskelig annotering eller labeling af data til deres træningsproces.
- **De er meget store modeller**, baseret på meget dybe neurale netværk trænet på milliarder af parametre.
- **De er normalt beregnet til at fungere som en 'grundlæggelse' for andre modeller**, hvilket betyder, at de kan bruges som udgangspunkt for andre modeller, der kan bygges ovenpå, hvilket kan gøres ved finjustering.

![Grundlæggende modeller versus LLM'er](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.da.png)

Billedkilde: [Essential Guide to Foundation Models and Large Language Models | af Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

For yderligere at afklare denne forskel, lad os tage ChatGPT som et eksempel. For at bygge den første version af ChatGPT blev en model kaldet GPT-3.5 brugt som grundlæggende model. Det betyder, at OpenAI brugte nogle chat-specifikke data til at skabe en finjusteret version af GPT-3.5, der var specialiseret i at præstere godt i samtalescenarier, såsom chatbots.

![Grundlæggende model](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.da.png)

Billedkilde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open Source versus Proprietære modeller

En anden måde at kategorisere LLM'er på er, om de er open source eller proprietære.

Open source-modeller er modeller, der er gjort tilgængelige for offentligheden og kan bruges af alle. De bliver ofte gjort tilgængelige af virksomheden, der skabte dem, eller af forskningssamfundet. Disse modeller kan inspiceres, modificeres og tilpasses til forskellige brugsscenarier i LLM'er. Dog er de ikke altid optimeret til produktionsbrug og kan være mindre effektive end proprietære modeller. Derudover kan finansiering til open source-modeller være begrænset, og de kan muligvis ikke vedligeholdes på lang sigt eller opdateres med den nyeste forskning. Eksempler på populære open source-modeller inkluderer [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) og [LLaMA](https://llama.meta.com).

Proprietære modeller er modeller, der ejes af en virksomhed og ikke er gjort tilgængelige for offentligheden. Disse modeller er ofte optimeret til produktionsbrug. Dog kan de ikke inspiceres, modificeres eller tilpasses til forskellige brugsscenarier. Derudover er de ikke altid gratis tilgængelige og kan kræve et abonnement eller betaling for at bruge. Brugere har heller ikke kontrol over de data, der bruges til at træne modellen, hvilket betyder, at de skal stole på, at modelens ejer sikrer databeskyttelse og ansvarlig brug af AI. Eksempler på populære proprietære modeller inkluderer [OpenAI-modeller](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) eller [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus Billedgenerering versus Tekst- og kodegenerering

LLM'er kan også kategoriseres efter det output, de genererer.

Embeddings er en række modeller, der kan konvertere tekst til en numerisk form, kaldet embedding, som er en numerisk repræsentation af inputteksten. Embeddings gør det lettere for maskiner at forstå forholdet mellem ord eller sætninger og kan bruges som input af andre modeller, såsom klassifikationsmodeller eller klyngemodeller, der har bedre ydeevne på numeriske data. Embedding-modeller bruges ofte til transfer learning, hvor en model bygges til en surrogatopgave, som der er rigeligt med data til, og derefter genbruges modelvægtene (embeddings) til andre opgaver. Et eksempel på denne kategori er [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.da.png)

Billedgenereringsmodeller er modeller, der genererer billeder. Disse modeller bruges ofte til billedredigering, billedsyntese og billedoversættelse. Billedgenereringsmodeller trænes ofte på store datasæt af billeder, såsom [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), og kan bruges til at generere nye billeder eller til at redigere eksisterende billeder med teknikker som inpainting, superopløsning og farvelægning. Eksempler inkluderer [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) og [Stable Diffusion-modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Billedgenerering](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.da.png)

Tekst- og kodegenereringsmodeller er modeller, der genererer tekst eller kode. Disse modeller bruges ofte til tekstopsummering, oversættelse og besvarelse af spørgsmål. Tekstgenereringsmodeller trænes ofte på store datasæt af tekst, såsom [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), og kan bruges til at generere ny tekst eller til at besvare spørgsmål. Kodegenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), trænes ofte på store datasæt af kode, såsom GitHub, og kan bruges til at generere ny kode eller til at rette fejl i eksisterende kode.

![Tekst- og kodegenerering](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.da.png)

### Encoder-Decoder versus Kun Decoder

For at tale om de forskellige typer af LLM-arkitekturer, lad os bruge en analogi.

Forestil dig, at din leder giver dig en opgave med at lave en quiz til eleverne. Du har to kolleger; den ene står for at skabe indholdet, og den anden står for at gennemgå det.

Indholdsskaberens rolle kan sammenlignes med en model, der kun er en Decoder. De kan se på emnet og det, du allerede har skrevet, og derefter skrive et kursus baseret på det. De er meget gode til at skrive engagerende og informativt indhold, men de er ikke så gode til at forstå emnet og læringsmålene. Nogle eksempler på Decoder-modeller er GPT-familien, såsom GPT-3.

Anmelderen kan sammenlignes med en model, der kun er en Encoder. De ser på det skrevne kursus og svarene, bemærker forholdet mellem dem og forstår konteksten, men de er ikke gode til at generere indhold. Et eksempel på en Encoder-model ville være BERT.

Forestil dig, at vi også kunne have en person, der både kunne skabe og gennemgå quizzen, dette er en Encoder-Decoder-model. Nogle eksempler ville være BART og T5.

### Tjeneste versus Model

Lad os nu tale om forskellen mellem en tjeneste og en model. En tjeneste er et produkt, der tilbydes af en Cloud Service Provider og ofte er en kombination af modeller, data og andre komponenter. En model er den centrale komponent i en tjeneste og er ofte en grundlæggende model, såsom en LLM.

Tjenester er ofte optimeret til produktionsbrug og er ofte lettere at bruge end modeller via en grafisk brugergrænseflade. Dog er tjenester ikke altid gratis tilgængelige og kan kræve et abonnement eller betaling for at bruge, i bytte for at udnytte tjenesteudbyderens udstyr og ressourcer, optimere omkostninger og skalere nemt. Et eksempel på en tjeneste er [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som tilbyder en pay-as-you-go prisplan, hvilket betyder, at brugere bliver opkrævet proportionalt med, hvor meget de bruger tjenesten. Derudover tilbyder Azure OpenAI Service sikkerhed på virksomhedsniveau og en ansvarlig AI-ramme oven på modellernes kapaciteter.

Modeller er blot det neurale netværk med parametre, vægte og andre elementer. Dette giver virksomheder mulighed for at køre lokalt, men kræver, at de køber udstyr, opbygger en struktur til skalering og køber en licens eller bruger en open source-model. En model som LLaMA er tilgængelig til brug, men kræver computerkraft for at køre modellen.

## Hvordan man tester og itererer med forskellige modeller for at forstå ydeevne på Azure

Når vores team har udforsket det nuværende LLM-landskab og identificeret nogle gode kandidater til deres scenarier, er det næste skridt at teste dem på deres data og arbejdsbyrde. Dette er en iterativ proces, der udføres gennem eksperimenter og målinger.
De fleste af de modeller, vi nævnte i de tidligere afsnit (OpenAI-modeller, open source-modeller som Llama2 og Hugging Face transformers), er tilgængelige i [Modelkataloget](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) i [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) er en cloud-platform designet til udviklere, der ønsker at bygge generative AI-applikationer og administrere hele udviklingsprocessen - fra eksperimentering til evaluering - ved at kombinere alle Azure AI-tjenester i én samlet hub med en brugervenlig grænseflade. Modelkataloget i Azure AI Studio giver brugeren mulighed for at:

- Finde den ønskede Foundation Model i kataloget - enten proprietær eller open source - ved at filtrere efter opgave, licens eller navn. For at forbedre søgbarheden er modellerne organiseret i samlinger, såsom Azure OpenAI-samlingen, Hugging Face-samlingen og flere.

![Modelkatalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.da.png)

- Gennemgå modelkortet, som inkluderer en detaljeret beskrivelse af den tilsigtede anvendelse og træningsdata, kodeeksempler og evalueringsresultater fra det interne evalueringsbibliotek.

![Modelkort](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.da.png)

- Sammenligne benchmarks på tværs af modeller og datasæt, der er tilgængelige i branchen, for at vurdere, hvilken der bedst opfylder forretningsscenariet, via [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelet.

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.da.png)

- Finjustere modellen på brugerdefinerede træningsdata for at forbedre modellens ydeevne i en specifik arbejdsopgave ved at udnytte eksperimenterings- og sporingsfunktionerne i Azure AI Studio.

![Model finjustering](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.da.png)

- Implementere den originale fortrænede model eller den finjusterede version til fjern realtidsinference - administreret beregning - eller serverløs API-endepunkt - [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - for at gøre det muligt for applikationer at bruge den.

![Model implementering](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.da.png)

> [!NOTE]
> Ikke alle modeller i kataloget er i øjeblikket tilgængelige for finjustering og/eller pay-as-you-go implementering. Tjek modelkortet for detaljer om modellens kapaciteter og begrænsninger.

## Forbedring af LLM-resultater

Vi har sammen med vores startup-team udforsket forskellige typer LLM'er og en cloud-platform (Azure Machine Learning), der gør det muligt for os at sammenligne forskellige modeller, evaluere dem på testdata, forbedre ydeevnen og implementere dem på inference-endepunkter.

Men hvornår bør man overveje at finjustere en model frem for at bruge en fortrænet? Er der andre metoder til at forbedre modellens ydeevne på specifikke arbejdsopgaver?

Der er flere tilgange, en virksomhed kan bruge for at opnå de ønskede resultater fra en LLM. Du kan vælge forskellige typer modeller med forskellige grader af træning, når du implementerer en LLM i produktion, med forskellige niveauer af kompleksitet, omkostninger og kvalitet. Her er nogle forskellige tilgange:

- **Prompt engineering med kontekst**. Ideen er at give nok kontekst, når du prompt'er, for at sikre, at du får de svar, du har brug for.

- **Retrieval Augmented Generation, RAG**. Hvis dine data f.eks. findes i en database eller et web-endepunkt, kan du hente relevante data og inkludere dem i brugerens prompt for at sikre, at disse data eller en delmængde af dem bliver en del af prompten.

- **Finjusteret model**. Her træner du modellen yderligere på dine egne data, hvilket gør modellen mere præcis og responsiv i forhold til dine behov, men det kan være dyrt.

![LLMs implementering](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.da.png)

Billedkilde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontekst

Fortrænede LLM'er fungerer meget godt på generelle naturlige sprogopgaver, selv når de kaldes med en kort prompt, som en sætning der skal fuldføres eller et spørgsmål – det såkaldte "zero-shot" læring.

Jo mere brugeren kan rammesætte deres forespørgsel med en detaljeret anmodning og eksempler – konteksten – desto mere præcist og tættere på brugerens forventninger vil svaret være. I dette tilfælde taler vi om "one-shot" læring, hvis prompten kun indeholder ét eksempel, og "few-shot" læring, hvis den indeholder flere eksempler. Prompt engineering med kontekst er den mest omkostningseffektive tilgang til at komme i gang.

### Retrieval Augmented Generation (RAG)

LLM'er har den begrænsning, at de kun kan bruge de data, der er blevet brugt under deres træning, til at generere et svar. Det betyder, at de ikke ved noget om fakta, der er sket efter deres træningsproces, og de kan ikke få adgang til ikke-offentlige oplysninger (som virksomhedsdata).
Dette kan overvindes gennem RAG, en teknik der udvider prompten med eksterne data i form af dokumentstykker, under hensyntagen til promptens længdebegrænsninger. Dette understøttes af vektordatabaseværktøjer (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), der henter de relevante stykker fra forskellige foruddefinerede datakilder og tilføjer dem til promptens kontekst.

Denne teknik er meget nyttig, når en virksomhed ikke har nok data, tid eller ressourcer til at finjustere en LLM, men stadig ønsker at forbedre ydeevnen på en specifik arbejdsopgave og reducere risikoen for fejlinformation, dvs. forvrængning af virkeligheden eller skadeligt indhold.

### Finjusteret model

Finjustering er en proces, der udnytter transfer learning til at 'tilpasse' modellen til en downstream-opgave eller til at løse et specifikt problem. I modsætning til few-shot læring og RAG resulterer det i en ny model med opdaterede vægte og bias. Det kræver et sæt træningseksempler bestående af en enkelt input (prompten) og dens tilknyttede output (fuldførelsen).
Dette ville være den foretrukne tilgang, hvis:

- **Brug af finjusterede modeller**. En virksomhed ønsker at bruge finjusterede mindre kapable modeller (som embedding-modeller) frem for højtydende modeller, hvilket resulterer i en mere omkostningseffektiv og hurtig løsning.

- **Overvejer latenstid**. Latenstid er vigtig for en specifik brugssag, så det er ikke muligt at bruge meget lange prompts, eller antallet af eksempler, som modellen skal lære fra, passer ikke med promptens længdebegrænsning.

- **Holder sig opdateret**. En virksomhed har mange høj-kvalitets data og sandhedsmærkater samt de ressourcer, der kræves for at vedligeholde disse data opdateret over tid.

### Trænet model

At træne en LLM fra bunden er uden tvivl den mest udfordrende og komplekse tilgang, der kræver enorme mængder data, dygtige ressourcer og passende beregningskraft. Denne mulighed bør kun overvejes i et scenarie, hvor en virksomhed har en domænespecifik brugssag og en stor mængde domænecentriske data.

## Videnstjek

Hvad kunne være en god tilgang til at forbedre LLM-fuldførelsesresultater?

1. Prompt engineering med kontekst  
1. RAG  
1. Finjusteret model  

A:3, hvis du har tid og ressourcer samt høj-kvalitets data, er finjustering den bedre mulighed for at holde sig opdateret. Men hvis du ønsker at forbedre tingene og mangler tid, er det værd at overveje RAG først.

## 🚀 Udfordring

Læs mere om, hvordan du kan [bruge RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) til din virksomhed.

## Godt arbejde, fortsæt din læring

Efter at have afsluttet denne lektion, kan du tjekke vores [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generative AI!

Gå videre til Lektion 3, hvor vi vil se på, hvordan man [bygger med Generative AI ansvarligt](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.