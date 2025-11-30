<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T19:21:11+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "no"
}
-->
# Utforsking og sammenligning av ulike LLM-er

[![Utforsking og sammenligning av ulike LLM-er](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.no.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikk på bildet over for å se videoen til denne leksjonen_

I forrige leksjon så vi hvordan generativ AI endrer teknologilandskapet, hvordan store språkmodeller (LLM-er) fungerer, og hvordan en bedrift – som vår oppstart – kan bruke dem til sine formål og vokse! I dette kapittelet skal vi sammenligne og kontrastere ulike typer store språkmodeller (LLM-er) for å forstå deres fordeler og ulemper.

Neste steg i vår oppstartsreise er å utforske det nåværende landskapet av LLM-er og forstå hvilke som passer for vårt brukstilfelle.

## Introduksjon

Denne leksjonen vil dekke:

- Ulike typer LLM-er i dagens landskap.
- Testing, iterering og sammenligning av ulike modeller for ditt brukstilfelle i Azure.
- Hvordan distribuere en LLM.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Velge riktig modell for ditt brukstilfelle.
- Forstå hvordan du tester, itererer og forbedrer ytelsen til modellen din.
- Vite hvordan bedrifter distribuerer modeller.

## Forstå ulike typer LLM-er

LLM-er kan kategoriseres på flere måter basert på deres arkitektur, treningsdata og brukstilfelle. Å forstå disse forskjellene vil hjelpe vår oppstart med å velge riktig modell for scenarioet, samt forstå hvordan man tester, itererer og forbedrer ytelsen.

Det finnes mange forskjellige typer LLM-modeller, og valget av modell avhenger av hva du ønsker å bruke dem til, dataene dine, hvor mye du er villig til å betale, og mer.

Avhengig av om du ønsker å bruke modellene til tekst, lyd, video, bildegenerering og så videre, kan du velge en annen type modell.

- **Lyd- og talegjenkjenning**. For dette formålet er Whisper-typen modeller et godt valg, da de er allsidige og rettet mot talegjenkjenning. De er trent på variert lyd og kan utføre flerspråklig talegjenkjenning. Lær mer om [Whisper-typen modeller her](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Bildegenerering**. For bildegenerering er DALL-E og Midjourney to svært kjente valg. DALL-E tilbys av Azure OpenAI. [Les mer om DALL-E her](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) og også i kapittel 9 av dette pensumet.

- **Tekstgenerering**. De fleste modeller er trent på tekstgenerering, og du har et stort utvalg av alternativer fra GPT-3.5 til GPT-4. De har ulike kostnader, der GPT-4 er den dyreste. Det er verdt å se på [Azure OpenAI-lekeplassen](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) for å evaluere hvilke modeller som best passer dine behov når det gjelder kapasitet og kostnad.

- **Multimodalitet**. Hvis du ønsker å håndtere flere typer data i input og output, kan du vurdere modeller som [gpt-4 turbo med visjon eller gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) – de nyeste utgivelsene av OpenAI-modeller – som er i stand til å kombinere naturlig språkbehandling med visuell forståelse, og muliggjør interaksjoner gjennom multimodale grensesnitt.

Å velge en modell gir deg noen grunnleggende funksjoner, men det er kanskje ikke nok. Ofte har du bedriftsspesifikke data som du på en eller annen måte må informere LLM-en om. Det finnes flere ulike tilnærminger til dette, mer om det i de kommende seksjonene.

### Grunnmodeller versus LLM-er

Begrepet Grunnmodell ble [skapt av forskere ved Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) og definert som en AI-modell som oppfyller visse kriterier, som:

- **De er trent ved bruk av usupervisert læring eller selv-supervisert læring**, noe som betyr at de er trent på umerkede multimodale data og ikke krever menneskelig annotering eller merking av data for treningsprosessen.
- **De er svært store modeller**, basert på svært dype nevrale nettverk trent på milliarder av parametere.
- **De er vanligvis ment å tjene som et ‘grunnlag’ for andre modeller**, noe som betyr at de kan brukes som et utgangspunkt for å bygge andre modeller, som kan gjøres ved finjustering.

![Grunnmodeller versus LLM-er](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.no.png)

Bildekilde: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

For å tydeliggjøre dette skillet, la oss ta ChatGPT som et eksempel. For å bygge den første versjonen av ChatGPT, fungerte en modell kalt GPT-3.5 som grunnmodellen. Dette betyr at OpenAI brukte noen chat-spesifikke data for å lage en finjustert versjon av GPT-3.5 som var spesialisert på å prestere godt i samtalescenarier, som chatboter.

![Grunnmodell](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.no.png)

Bildekilde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Åpen kildekode versus proprietære modeller

En annen måte å kategorisere LLM-er på er om de er åpen kildekode eller proprietære.

Modeller med åpen kildekode er modeller som gjøres tilgjengelige for offentligheten og kan brukes av hvem som helst. De gjøres ofte tilgjengelige av selskapet som opprettet dem, eller av forskningsmiljøet. Disse modellene kan inspiseres, modifiseres og tilpasses for ulike brukstilfeller i LLM-er. De er imidlertid ikke alltid optimalisert for produksjonsbruk og kan være mindre ytelsesdyktige enn proprietære modeller. I tillegg kan finansiering for modeller med åpen kildekode være begrenset, og de kan ikke vedlikeholdes på lang sikt eller oppdateres med den nyeste forskningen. Eksempler på populære modeller med åpen kildekode inkluderer [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) og [LLaMA](https://llama.meta.com).

Proprietære modeller er modeller som eies av et selskap og ikke gjøres tilgjengelige for offentligheten. Disse modellene er ofte optimalisert for produksjonsbruk. De kan imidlertid ikke inspiseres, modifiseres eller tilpasses for ulike brukstilfeller. I tillegg er de ikke alltid gratis tilgjengelige og kan kreve abonnement eller betaling for bruk. Brukere har heller ikke kontroll over dataene som brukes til å trene modellen, noe som betyr at de må stole på at modelleieren sikrer forpliktelse til databeskyttelse og ansvarlig bruk av AI. Eksempler på populære proprietære modeller inkluderer [OpenAI-modeller](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) eller [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Innebygging versus bildegenerering versus tekst- og kodegenerering

LLM-er kan også kategoriseres etter outputen de genererer.

Innebygginger er et sett med modeller som kan konvertere tekst til en numerisk form, kalt innebygging, som er en numerisk representasjon av input-teksten. Innebygginger gjør det enklere for maskiner å forstå forholdet mellom ord eller setninger og kan brukes som input av andre modeller, som klassifiseringsmodeller eller klyngemodeller som har bedre ytelse på numeriske data. Innebyggingsmodeller brukes ofte til overføringslæring, der en modell bygges for en surrogatoppgave som det finnes rikelig med data for, og deretter gjenbrukes modellvektene (innebyggingene) for andre oppgaver. Et eksempel på denne kategorien er [OpenAI innebygginger](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Innebygging](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.no.png)

Bildegenereringsmodeller er modeller som genererer bilder. Disse modellene brukes ofte til bildebehandling, bildesyntese og bildetransformasjon. Bildegenereringsmodeller trenes ofte på store datasett av bilder, som [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), og kan brukes til å generere nye bilder eller redigere eksisterende bilder med teknikker som inpainting, superoppløsning og fargelegging. Eksempler inkluderer [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) og [Stable Diffusion-modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Bildegenerering](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.no.png)

Tekst- og kodegenereringsmodeller er modeller som genererer tekst eller kode. Disse modellene brukes ofte til tekstsammendrag, oversettelse og spørsmål-svar. Tekstgenereringsmodeller trenes ofte på store datasett av tekst, som [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), og kan brukes til å generere ny tekst eller svare på spørsmål. Kodegenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), trenes ofte på store datasett av kode, som GitHub, og kan brukes til å generere ny kode eller fikse feil i eksisterende kode.

![Tekst- og kodegenerering](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.no.png)

### Encoder-Decoder versus kun Decoder

For å snakke om de ulike typene arkitekturer for LLM-er, la oss bruke en analogi.

Tenk deg at sjefen din ga deg en oppgave med å lage en quiz for studentene. Du har to kolleger; én som har ansvar for å lage innholdet og en annen som har ansvar for å gjennomgå det.

Innholdsskaperen er som en modell som kun er en Decoder, de kan se på emnet og det du allerede har skrevet, og deretter skrive et kurs basert på det. De er veldig gode til å skrive engasjerende og informativt innhold, men de er ikke veldig gode til å forstå emnet og læringsmålene. Noen eksempler på Decoder-modeller er GPT-familien, som GPT-3.

Gjennomleseren er som en modell som kun er en Encoder, de ser på kurset som er skrevet og svarene, legger merke til forholdet mellom dem og forstår konteksten, men de er ikke gode til å generere innhold. Et eksempel på en Encoder-modell ville være BERT.

Tenk deg at vi også kan ha noen som både kan lage og gjennomgå quizen, dette er en Encoder-Decoder-modell. Noen eksempler ville være BART og T5.

### Tjeneste versus Modell

La oss nå snakke om forskjellen mellom en tjeneste og en modell. En tjeneste er et produkt som tilbys av en skyleverandør, og er ofte en kombinasjon av modeller, data og andre komponenter. En modell er kjernen i en tjeneste, og er ofte en grunnmodell, som en LLM.

Tjenester er ofte optimalisert for produksjonsbruk og er ofte enklere å bruke enn modeller, via et grafisk brukergrensesnitt. Tjenester er imidlertid ikke alltid gratis tilgjengelige og kan kreve abonnement eller betaling for bruk, i bytte mot å utnytte tjenesteeierens utstyr og ressurser, optimalisere utgifter og skalere enkelt. Et eksempel på en tjeneste er [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som tilbyr en betalingsplan basert på bruk, noe som betyr at brukere belastes proporsjonalt med hvor mye de bruker tjenesten. I tillegg tilbyr Azure OpenAI Service sikkerhet på bedriftsnivå og et ansvarlig AI-rammeverk på toppen av modellens funksjoner.

Modeller er bare det nevrale nettverket, med parametere, vekter og andre komponenter. Dette gjør det mulig for selskaper å kjøre dem lokalt, men de må kjøpe utstyr, bygge en struktur for skalering og kjøpe en lisens eller bruke en modell med åpen kildekode. En modell som LLaMA er tilgjengelig for bruk, men krever datakraft for å kjøre modellen.

## Hvordan teste og iterere med ulike modeller for å forstå ytelse i Azure

Når teamet vårt har utforsket det nåværende LLM-landskapet og identifisert noen gode kandidater for sine scenarier, er neste steg å teste dem på deres data og arbeidsbelastning. Dette er en iterativ prosess, utført gjennom eksperimenter og målinger.
De fleste av modellene vi nevnte i tidligere avsnitt (OpenAI-modeller, åpen kildekode-modeller som Llama2 og Hugging Face-transformers) er tilgjengelige i [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) i [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) er en skyplattform designet for utviklere som ønsker å bygge generative AI-applikasjoner og administrere hele utviklingssyklusen – fra eksperimentering til evaluering – ved å kombinere alle Azure AI-tjenester i ett enkelt knutepunkt med et brukervennlig grensesnitt. Modellkatalogen i Azure AI Studio gjør det mulig for brukeren å:

- Finne Foundation-modellen av interesse i katalogen – enten proprietær eller åpen kildekode – ved å filtrere etter oppgave, lisens eller navn. For å forbedre søkbarheten er modellene organisert i samlinger, som Azure OpenAI-samlingen, Hugging Face-samlingen og mer.

![Model catalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.no.png)

- Gå gjennom modellkortet, som inkluderer en detaljert beskrivelse av tiltenkt bruk og treningsdata, kodeeksempler og evalueringsresultater fra det interne evalueringsbiblioteket.

![Model card](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.no.png)

- Sammenligne benchmarks på tvers av modeller og datasett tilgjengelig i bransjen for å vurdere hvilken som passer best til forretningsscenariet, via [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelet.

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.no.png)

- Finjustere modellen på egendefinerte treningsdata for å forbedre modellens ytelse i en spesifikk arbeidsbelastning, ved å utnytte eksperimenterings- og sporingsfunksjonene i Azure AI Studio.

![Model fine-tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.no.png)

- Distribuere den originale forhåndstrente modellen eller den finjusterte versjonen til en ekstern sanntidsinference – administrert databehandling – eller serverløs API-endepunkt – [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) – for å gjøre det mulig for applikasjoner å bruke den.

![Model deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.no.png)

> [!NOTE]
> Ikke alle modeller i katalogen er for øyeblikket tilgjengelige for finjustering og/eller pay-as-you-go-distribusjon. Sjekk modellkortet for detaljer om modellens funksjoner og begrensninger.

## Forbedring av LLM-resultater

Vi har utforsket med vårt oppstartsteam ulike typer LLM-er og en skyplattform (Azure Machine Learning) som gjør det mulig for oss å sammenligne forskjellige modeller, evaluere dem på testdata, forbedre ytelsen og distribuere dem på inference-endepunkter.

Men når bør de vurdere å finjustere en modell i stedet for å bruke en forhåndstrent? Finnes det andre tilnærminger for å forbedre modellens ytelse på spesifikke arbeidsbelastninger?

Det finnes flere tilnærminger en bedrift kan bruke for å oppnå de resultatene de trenger fra en LLM. Du kan velge forskjellige typer modeller med ulike grader av trening når du distribuerer en LLM i produksjon, med forskjellige nivåer av kompleksitet, kostnad og kvalitet. Her er noen forskjellige tilnærminger:

- **Prompt engineering med kontekst**. Ideen er å gi nok kontekst når du gir en prompt for å sikre at du får de svarene du trenger.

- **Retrieval Augmented Generation, RAG**. Dataene dine kan for eksempel finnes i en database eller et web-endepunkt. For å sikre at disse dataene, eller en del av dem, inkluderes ved prompting, kan du hente relevante data og gjøre dem til en del av brukerens prompt.

- **Finjustert modell**. Her trener du modellen videre på dine egne data, noe som gjør modellen mer presis og responsiv til dine behov, men det kan være kostbart.

![LLMs deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.no.png)

Bildekilde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontekst

Forhåndstrente LLM-er fungerer veldig godt på generelle oppgaver innen naturlig språk, selv ved å kalle dem med en kort prompt, som en setning som skal fullføres eller et spørsmål – det såkalte "zero-shot"-læring.

Jo mer brukeren kan ramme inn forespørselen sin med en detaljert forespørsel og eksempler – konteksten – desto mer nøyaktig og nærmere brukerens forventninger vil svaret være. I dette tilfellet snakker vi om "one-shot"-læring hvis prompten inneholder bare ett eksempel, og "few-shot"-læring hvis den inneholder flere eksempler. Prompt engineering med kontekst er den mest kostnadseffektive tilnærmingen å starte med.

### Retrieval Augmented Generation (RAG)

LLM-er har begrensningen at de kun kan bruke dataene som ble brukt under treningen for å generere et svar. Dette betyr at de ikke vet noe om hendelser som skjedde etter treningsprosessen, og de kan ikke få tilgang til ikke-offentlig informasjon (som bedriftsdata).
Dette kan overvinnes gjennom RAG, en teknikk som utvider prompten med eksterne data i form av dokumentbiter, med tanke på begrensninger i promptlengde. Dette støttes av verktøy for vektordatabaser (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) som henter nyttige biter fra ulike forhåndsdefinerte datakilder og legger dem til promptens kontekst.

Denne teknikken er svært nyttig når en bedrift ikke har nok data, nok tid eller ressurser til å finjustere en LLM, men likevel ønsker å forbedre ytelsen på en spesifikk arbeidsbelastning og redusere risikoen for fabrikasjoner, det vil si forvrengning av virkeligheten eller skadelig innhold.

### Finjustert modell

Finjustering er en prosess som utnytter overføringslæring for å "tilpasse" modellen til en nedstrømsoppgave eller for å løse et spesifikt problem. I motsetning til few-shot-læring og RAG resulterer det i en ny modell som genereres, med oppdaterte vekter og skjevheter. Det krever et sett med treningseksempler som består av en enkelt input (prompten) og dens tilhørende output (fullføringen).
Dette vil være den foretrukne tilnærmingen hvis:

- **Bruk av finjusterte modeller**. En bedrift ønsker å bruke finjusterte mindre kapable modeller (som embedding-modeller) i stedet for høyytelsesmodeller, noe som resulterer i en mer kostnadseffektiv og rask løsning.

- **Vurdering av latens**. Latens er viktig for en spesifikk brukstilfelle, så det er ikke mulig å bruke veldig lange promter eller antallet eksempler som modellen skal lære av, passer ikke med promptens lengdebegrensning.

- **Holde seg oppdatert**. En bedrift har mye data av høy kvalitet og sannhetsdata, samt ressursene som kreves for å holde disse dataene oppdatert over tid.

### Trenet modell

Å trene en LLM fra bunnen av er uten tvil den mest krevende og komplekse tilnærmingen å ta i bruk, og krever enorme mengder data, dyktige ressurser og passende datakraft. Dette alternativet bør kun vurderes i et scenario der en bedrift har en domenespesifikk brukstilfelle og en stor mengde domenesentriske data.

## Kunnskapssjekk

Hva kan være en god tilnærming for å forbedre LLM-fullføringsresultater?

1. Prompt engineering med kontekst
1. RAG
1. Finjustert modell

A:3, hvis du har tid og ressurser og data av høy kvalitet, er finjustering det bedre alternativet for å holde seg oppdatert. Men hvis du ser på å forbedre ting og mangler tid, er det verdt å vurdere RAG først.

## 🚀 Utfordring

Les mer om hvordan du kan [bruke RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) for din bedrift.

## Flott arbeid, fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å øke kunnskapen din om Generative AI!

Gå videre til Leksjon 3 hvor vi skal se på hvordan man [bygger med Generative AI på en ansvarlig måte](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.