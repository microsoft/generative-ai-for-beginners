# Udforskning og sammenligning af forskellige LLM'er

[![Udforskning og sammenligning af forskellige LLM'er](../../../translated_images/da/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klik på billedet ovenfor for at se videoen af denne lektion_

Med den tidligere lektion har vi set, hvordan Generativ AI ændrer teknologilandskabet, hvordan store sprogmodeller (LLM'er) fungerer, og hvordan en virksomhed - som vores startup - kan anvende dem til deres brugssager og vokse! I dette kapitel vil vi sammenligne og kontrastere forskellige typer af store sprogmodeller (LLM'er) for at forstå deres fordele og ulemper.

Næste skridt i vores startups rejse er at udforske det nuværende landskab af LLM'er og forstå, hvilke der er egnede til vores brugssag.

## Introduktion

Denne lektion vil omfatte:

- Forskellige typer af LLM'er i det nuværende landskab.
- Test, iteration og sammenligning af forskellige modeller til din brugssag i Azure.
- Hvordan man implementerer en LLM.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Vælge den rigtige model til din brugssag.
- Forstå hvordan man tester, itererer og forbedrer modellens ydeevne.
- Vide, hvordan virksomheder implementerer modeller.

## Forstå forskellige typer af LLM'er

LLM'er kan kategoriseres på flere måder baseret på deres arkitektur, træningsdata og brugssag. At forstå disse forskelle vil hjælpe vores startup med at vælge den rette model til scenariet og forstå, hvordan man tester, itererer og forbedrer ydeevnen.

Der findes mange forskellige typer LLM-modeller; dit valg afhænger af, hvad du ønsker at bruge dem til, dine data, hvor meget du er villig til at betale og mere.

Afhængigt af om du vil bruge modellerne til tekst, lyd, video, billedgenerering osv., kan du vælge en anden type model.

- **Lyd- og talegenkendelse**. Whisper-lignende modeller er stadig nyttige som generelle talegenkendelsesmodeller, men produktionsvalg inkluderer nu også nyere tale-til-tekst modeller såsom `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` og diariseringsvarianter. Vurder sprogunderstøttelse, diariseringsmuligheder, realtidssupport, latenstid og omkostninger for dit scenarie. Læs mere i [OpenAI tale-til-tekst dokumentationen](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Billedgenerering**. DALL-E og Midjourney er velkendte billedgenereringsmuligheder, men de nuværende OpenAI billed-API'er centrerer sig om GPT billedmodeller som `gpt-image-2`, mens Stable Diffusion, Imagen, Flux og andre modelfamilier også er almindelige valg. Sammenlign promptoverholdelse, redigeringsstøtte, stilkontrol, sikkerhedskrav og licensering. Læs mere i [OpenAI billedgenereringsguide](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) og kapitel 9 i dette pensum.

- **Tekstgenerering**. Tekstmodeller spænder nu over frontlinjemodeller, ræsonnementmodeller, mindre lav-latens modeller og open-weight modeller. Nuværende eksempler inkluderer OpenAI GPT-5.x modeller, Anthropic Claude 4.x modeller, Google Gemini 3.x modeller, Meta Llama 4 modeller og Mistral modeller. Vælg ikke kun ud fra udgivelsesdato eller pris; sammenlign opgavekvalitet, latenstid, kontekstvindue, brug af værktøjer, sikkerhedsadfærd, regional tilgængelighed og samlede omkostninger. [Microsoft Foundry modelkatalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) er et godt sted at sammenligne modeller tilgængelige på Azure.

- **Multimodalitet**. Mange nuværende modeller kan håndtere mere end tekst. Nogle accepterer billede-, lyd- eller videoinput; nogle kan kalde værktøjer; og specialiserede modeller kan generere billeder, lyd eller video. For eksempel understøtter nuværende OpenAI-modeller tekst og billede-input, Gemini-modeller kan afhængigt af variant understøtte tekst, kode, billede, lyd og video-input, og Llama 4 Scout og Maverick er open-weight nativt multimodale modeller. Tjek altid hver modelkort for understøttede input- og outputmodaliteter, før du bygger et workflow omkring den.

At vælge en model betyder, at du får nogle grundlæggende funktioner, som måske ikke er nok. Ofte har man virksomheds-specifikke data, som man på en eller anden måde skal gøre LLM'en opmærksom på. Der findes forskellige måder at håndtere dette på, mere om det i de kommende afsnit.

### Foundation Models versus LLM'er

Begrebet Foundation Model blev [uddybet af Stanford-forskere](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) og defineret som en AI-model, der følger nogle kriterier, såsom:

- **De trænes ved hjælp af usuperviseret læring eller selv-superviseret læring**, hvilket betyder, at de trænes på unlabeled multimodale data og ikke kræver menneskelig annotering eller mærkning af data til træningsprocessen.
- **De er meget store modeller**, baseret på meget dybe neurale netværk trænet på milliarder af parametre.
- **De er normalt beregnet til at tjene som en ‘foundation’ for andre modeller**, hvilket betyder, at de kan bruges som udgangspunkt for at bygge andre modeller ovenpå, hvilket kan ske ved finjustering.

![Foundation Models versus LLMs](../../../translated_images/da/FoundationModel.e4859dbb7a825c94.webp)

Billedkilde: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

For yderligere at tydeliggøre denne sondring, lad os tage ChatGPT som et historisk eksempel. Tidlige versioner af ChatGPT brugte GPT-3.5 som foundation model. OpenAI brugte derefter chat-specifikke data og justeringsteknikker til at skabe en finjusteret version, der præsterede bedre i samtalescenarier såsom chatbots. Moderne AI-tjenester ruter ofte mellem flere modelvarianter, så tjenestens navn og den underliggende modelnavn er ikke altid det samme.

![Foundation Model](../../../translated_images/da/Multimodal.2c389c6439e0fc51.webp)

Billedkilde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus Proprietære modeller

En anden måde at kategorisere LLM'er på er, om de er open-weight, open-source eller proprietære.

Open-source og open-weight modeller gør modelartefakter tilgængelige for inspektion, download eller tilpasning, men deres licenser adskiller sig. Nogle er fuldt open source, mens andre er open-weight modeller med brugsbegrænsninger. De kan være nyttige, når en virksomhed har behov for større kontrol over implementering, datalokation, omkostninger eller tilpasning. Men hold skal stadig gennemgå licensvilkår, serveromkostninger, vedligeholdelse, sikkerhedsopdateringer og evalueringskvalitet, før de bruger dem i produktion. Eksempler inkluderer [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), nogle [Mistral modeller](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) og mange modeller hostet på [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietære modeller ejes og hostes af en udbyder. Disse modeller er ofte optimeret til managed produktionsbrug og kan tilbyde stærk support, sikkerhedssystemer, værktøjsintegration og skalerbarhed. Dog kan kunder normalt ikke inspicere eller ændre modelvægtene, og de skal gennemgå udbydervilkår for privatliv, datalagring, overholdelse og acceptabel brug. Eksempler inkluderer [OpenAI modeller](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) og [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus billedgenerering versus tekst- og kodegenerering

LLM'er kan også kategoriseres efter outputtypen, de genererer.

Embeddings er en række modeller, der kan konvertere tekst til en numerisk form kaldet embedding, som er en numerisk repræsentation af indtastningsteksten. Embeddings gør det lettere for maskiner at forstå relationerne mellem ord eller sætninger og kan bruges som input til andre modeller, såsom klassifikationsmodeller eller klyngeanalyser, der har bedre ydeevne på numeriske data. Embedding-modeller bruges ofte til transfer learning, hvor en model bygges til en surrogatopgave, hvor der findes masser af data, og derefter genbruges modelvægtene (embeddings) til andre efterfølgende opgaver. Et eksempel på denne kategori er [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/da/Embedding.c3708fe988ccf760.webp)

Billedgenereringsmodeller er modeller, der genererer billeder. Disse modeller bruges ofte til billedredigering, billedsyntese og billedtransformation. Billedgenereringsmodeller trænes ofte på store datasæt med billeder, såsom [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), og kan bruges til at generere nye billeder eller til at redigere eksisterende billeder med teknikker som inpainting, super-opløsning og kolorering. Eksempler inkluderer [GPT Image modeller](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) og Imagen modeller.

![Image generation](../../../translated_images/da/Image.349c080266a763fd.webp)

Tekst- og kodegenereringsmodeller er modeller, der genererer tekst eller kode. Disse modeller bruges ofte til tekstopsummering, oversættelse og besvarelse af spørgsmål. Tekstgenereringsmodeller trænes ofte på store datasæt med tekst, såsom [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst) og kan bruges til at generere ny tekst eller besvare spørgsmål. Kodegenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), trænes ofte på store datasæt med kode, såsom GitHub, og kan bruges til at generere ny kode eller rette fejl i eksisterende kode.

![Text and code generation](../../../translated_images/da/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus kun Decoder

For at tale om de forskellige typer arkitekturer for LLM'er, lad os bruge en analogi.

Forestil dig, at din chef gav dig en opgave med at skrive en quiz til eleverne. Du har to kollegaer; en der skaber indholdet og en anden, der gennemgår det.

Indholdsskaberen er som en decoder-only-model: de kan se på emnet, se, hvad du allerede har skrevet, og derefter fortsætte med at generere indhold baseret på denne kontekst. De er meget gode til at skrive engagerende og informativt indhold, men er ikke altid det bedste valg, når opgaven kun er at klassificere, hente eller kode information. Eksempler på decoder-only modelfamilier inkluderer GPT og Llama modeller.

Gennemgiveren er som en encoder-only-model: de kigger på det skrevne kursus og svarene, bemærker forholdet mellem dem og forstår konteksten, men er ikke gode til at generere indhold. Et eksempel på en encoder-only-model er BERT.

Forestil dig, at vi også kan have en, der både kan skabe og gennemgå quizzen, dette er en encoder-decoder-model. Nogle eksempler ville være BART og T5.

### Service versus Model

Lad os nu tale om forskellen mellem en service og en model. En service er et produkt, der tilbydes af en cloud-tjenesteudbyder og er ofte en kombination af modeller, data og andre komponenter. En model er kernekomponenten i en service og er ofte en foundation model, som en LLM.

Services er ofte optimeret til produktionsbrug og er ofte lettere at bruge end modeller via en grafisk brugerflade. Services er dog ikke altid gratis tilgængelige og kan kræve abonnement eller betaling for brug til gengæld for at udnytte service-ejerens udstyr og ressourcer, optimere udgifter og nem skalering. Et eksempel på en service er [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), som tilbyder en pay-as-you-go-skala, hvilket betyder, at brugere bliver opkrævet i forhold til, hvor meget de bruger tjenesten. Azure OpenAI Service tilbyder også virksomheds-graded sikkerhed og et ansvarligt AI-rammeværk ovenpå modellernes kapabiliteter.

Modeller er de neurale netværksartefakter: parametre, vægte, arkitektur, tokenizer og understøttende konfiguration. At køre en model lokalt eller i et privat miljø kræver passende hardware, serverinfrastruktur, overvågning og enten en kompatibel open-source/open-weight licens eller en kommerciel licens. Open-weight modeller såsom Llama 4 eller Mistral modeller kan hostes selv, men de kræver stadig regnekraft og operationel ekspertise.

## Hvordan man tester og itererer med forskellige modeller for at forstå ydeevnen på Azure


Når vores team har udforsket det nuværende LLM-landskab og identificeret nogle gode kandidater til deres scenarier, er det næste skridt at teste dem på deres data og deres arbejdsbyrde. Dette er en iterativ proces, udført gennem eksperimenter og målinger.
De fleste af de modeller, vi nævnte i tidligere afsnit (OpenAI-modeller, open-weight modeller som Llama 4 og Mistral, og Hugging Face-modeller) er tilgængelige i [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), tidligere Azure AI Studio/Azure AI Foundry, er en ensartet Azure-platform til opbygning af AI-apps og agenter. Den hjælper udviklere med at styre livscyklussen fra eksperimentering og evaluering til implementering, overvågning og styring. Modelkataloget i Microsoft Foundry giver brugeren mulighed for at:

- Finde den fundamentale model af interesse i kataloget, inklusive modeller solgt af Azure og modeller fra partnere og fællesskabsudbydere. Brugere kan filtrere efter opgave, udbyder, licens, implementeringsmulighed eller navn.

![Model catalog](../../../translated_images/da/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Gennemgå modelkortet, inklusive en detaljeret beskrivelse af tiltænkt brug og træningsdata, kodeeksempler og evalueringsresultater fra det interne evalueringsbibliotek.

![Model card](../../../translated_images/da/ModelCard.598051692c6e400d.webp)

- Sammenligne benchmarks på tværs af modeller og datasæt tilgængelige i industrien for at vurdere, hvilken der opfylder forretningsscenariet, gennem [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelet.

![Model benchmarks](../../../translated_images/da/ModelBenchmarks.254cb20fbd06c03a.webp)

- Finjustere understøttede modeller på tilpassede træningsdata for at forbedre modelpræstation i en specifik arbejdsbyrde ved at udnytte eksperimenterings- og sporingsfunktionerne i Microsoft Foundry.

![Model fine-tuning](../../../translated_images/da/FineTuning.aac48f07142e36fd.webp)

- Implementere den oprindelige fortrænede model eller den finjusterede version til en fjern realtidsinference-endpoint ved hjælp af styrede compute- eller serverløse implementeringsmuligheder for at gøre det muligt for applikationer at bruge den.

![Model deployment](../../../translated_images/da/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Ikke alle modeller i kataloget er i øjeblikket tilgængelige til finjustering og/eller pay-as-you-go-implementering. Tjek modelkortet for detaljer om modellens kapaciteter og begrænsninger.

## Forbedring af LLM-resultater

Vi har udforsket med vores startup-team forskellige typer af LLM’er og en cloud-platform (Microsoft Foundry), der gør os i stand til at sammenligne forskellige modeller, evaluere dem på testdata, forbedre præstation og implementere dem på inference-endpoints.

Men hvornår skal de overveje at finjustere en model fremfor at bruge en fortrænet? Er der andre tilgange til at forbedre modelpræstation på specifikke arbejdsbyrder?

Der er flere tilgange, en virksomhed kan bruge for at opnå de resultater, de har brug for fra en LLM. Du kan vælge forskellige typer modeller med forskellige grader af træning, når du implementerer en LLM i produktion, med forskellige niveauer af kompleksitet, omkostninger og kvalitet. Her er nogle forskellige tilgange:

- **Prompt engineering med kontekst**. Ideen er at give nok kontekst, når du forespørger, for at sikre, at du får de svar, du har brug for.

- **Retrieval Augmented Generation, RAG**. Dine data kan for eksempel eksistere i en database eller et web-endpoint. For at sikre, at disse data – eller en delmængde heraf – inkluderes på tidspunktet for forespørgslen, kan du hente de relevante data og gøre dem til en del af brugerens prompt.

- **Finjusteret model**. Her træner du modellen yderligere på dine egne data, hvilket leder til, at modellen bliver mere præcis og responsiv over for dine behov, men det kan være omkostningstungt.

![LLMs deployment](../../../translated_images/da/Deploy.18b2d27412ec8c02.webp)

Billedkilde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontekst

Fortrænede LLM’er fungerer meget godt på generaliserede opgaver inden for naturligt sprog, selv ved at kalde dem med en kort prompt, som for eksempel en sætning, der skal fuldføres, eller et spørgsmål – det såkaldte “zero-shot” læring.

Men jo mere brugeren kan indramme deres forespørgsel med en detaljeret anmodning og eksempler – Konteksten – desto mere nøjagtigt og tæt på brugerens forventninger vil svaret være. I dette tilfælde taler vi om “one-shot” læring, hvis prompten kun indeholder ét eksempel, og “few shot learning”, hvis den indeholder flere eksempler.
Prompt engineering med kontekst er den mest omkostningseffektive tilgang at starte med.

### Retrieval Augmented Generation (RAG)

LLM’er har den begrænsning, at de kun kan bruge de data, der er brugt under deres træning, til at generere et svar. Det betyder, at de ikke ved noget om fakta, der er sket efter deres træningsproces, og at de ikke kan tilgå ikke-offentlig information (som virksomhedsdata).
Dette kan overvindes med RAG, en teknik som forbedrer prompten med eksterne data i form af dokumentstykker, under hensyntagen til promptens længdebegrænsninger. Dette understøttes af vektordatabasesystemer (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), der henter de relevante stykker fra forskellige foruddefinerede datakilder og tilføjer dem til promptens kontekst.

Denne teknik er meget nyttig, når en virksomhed ikke har nok data, tid eller ressourcer til at finjustere en LLM, men alligevel ønsker at forbedre præstation på en specifik arbejdsbyrde og reducere risikoen for hallucinerede, forældede eller uunderstøttede svar.

### Finjusteret model

Finjustering er en proces, der udnytter transfer learning til at ‘tilpasse’ modellen til en nedstrømsopgave eller til at løse et specifikt problem. I modsætning til few-shot læring og RAG resulterer det i, at der genereres en ny model med opdaterede vægte og bias. Det kræver et sæt træningseksempler bestående af en enkelt input (prompten) og dets tilknyttede output (fuldførelsen).
Dette ville være den foretrukne tilgang, hvis:

- **Brug af mindre opgavespecifikke modeller**. En virksomhed ønsker at finjustere en mindre model til en snæver opgave fremfor gentagne gange at forespørge en større frontier-model, hvilket resulterer i en mere omkostningseffektiv og hurtigere løsning.

- **Overveje latenstid**. Latenstid er vigtig for en bestemt brugssag, så det ikke er muligt at bruge meget lange prompts, eller antallet af eksempler, der skal læres fra modellen, passer ikke med promptens længdebegrænsning.

- **Tilpasse stabil adfærd**. En virksomhed har mange høj-kvalitets eksempler og ønsker, at modellen konsekvent følger en opgavestruktur, outputformat, tone eller domænespecifik stil. Hvis hovedproblemet er friske fakta eller privat viden, der ændrer sig ofte, bør man bruge RAG i stedet for udelukkende at stole på finjustering.

### Trænet model

Træning af en LLM fra bunden er uden tvivl den sværeste og mest komplekse tilgang at tage, hvilket kræver massive mængder data, dygtige ressourcer og passende computerkraft. Denne mulighed bør kun overvejes i scenarier, hvor en virksomhed har en domænespecifik brugssag og en stor mængde domænecentrerede data.

## Videnstjek

Hvad kunne være en god tilgang til at forbedre LLM-fuldførelsesresultater?

1. Prompt engineering med kontekst
1. RAG
1. Finjusteret model

A: Alle tre kan hjælpe. Start med prompt engineering og kontekst for hurtige forbedringer, og brug RAG, når modellen har brug for aktuelle fakta eller private virksomhedsdata. Vælg finjustering, når du har nok høj-kvalitets eksempler og har brug for, at modellen konsekvent følger en opgave, format, tone eller domænemønster.

## 🚀 Udfordring

Læs mere om, hvordan du kan [bruge RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) i din virksomhed.

## Godt arbejde, fortsæt din læring

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for fortsat at styrke din viden om Generativ AI!

Gå videre til lektion 3, hvor vi vil se på, hvordan man [bygger med Generativ AI Ansvarligt](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->