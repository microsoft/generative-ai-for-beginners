# Utforske og sammenligne forskjellige LLM-er

[![Utforske og sammenligne forskjellige LLM-er](../../../translated_images/no/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikk på bildet over for å se video av denne leksjonen_

Med forrige leksjon har vi sett hvordan Generativ AI forandrer teknologi-landskapet, hvordan store språkmodeller (LLM-er) fungerer og hvordan en bedrift - som vår oppstart - kan bruke dem i sine bruksområder og vokse! I dette kapitlet ser vi på å sammenligne og kontrastere ulike typer store språkmodeller (LLM-er) for å forstå deres fordeler og ulemper.

Neste steg i oppstartens reise er å utforske dagens landskap av LLM-er og forstå hvilke som passer til vårt brukstilfelle.

## Introduksjon

Denne leksjonen vil dekke:

- Ulike typer LLM-er i dagens landskap.
- Testing, iterasjon og sammenligning av ulike modeller for ditt brukstilfelle i Azure.
- Hvordan distribuere en LLM.

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Velge riktig modell for ditt brukstilfelle.
- Forstå hvordan du tester, itererer og forbedrer ytelsen til modellen din.
- Vite hvordan bedrifter distribuerer modeller.

## Forstå ulike typer LLM-er

LLM-er kan kategoriseres på flere måter basert på arkitektur, treningsdata og brukstilfelle. Å forstå disse forskjellene vil hjelpe vår oppstart med å velge riktig modell for scenariet, og forstå hvordan man tester, itererer og forbedrer ytelsen.

Det finnes mange forskjellige typer LLM-modeller; valget av modell avhenger av hva du har som mål å bruke dem til, dine data, hvor mye du er villig til å betale og mer.

Avhengig av om du ønsker å bruke modellene til tekst, lyd, video, bildegenerering osv., kan du velge en annen type modell.

- **Lyd- og talegjenkjenning**. Whisper-stil modeller er fortsatt nyttige allmenn-talegjenkjenningsmodeller, men valg for produksjon inkluderer nå også nyere tale-til-tekst modeller som `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` og diariseringsvarianter. Vurder språkdekning, diariseringsstøtte, sanntidsstøtte, latenstid og kostnad for ditt scenario. Les mer i [OpenAI tale-til-tekst dokumentasjon](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Bildefremstilling**. DALL-E og Midjourney er velkjente alternativer for bildeopprettelse, men nåværende OpenAI bilde-APIer sentrerer rundt GPT Image-modeller som `gpt-image-2`, mens Stable Diffusion, Imagen, Flux og andre modellfamilier også er vanlige valg. Sammenlign prompt-overholdelse, redigeringsstøtte, stilkontroll, sikkerhetskrav og lisensiering. Les mer i [OpenAI bildegenereringsguide](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) og kapittel 9 i dette læreplanen.

- **Tekstgenerering**. Tekstmodeller spenner nå fra toppmodeller, resonneringsmodeller, mindre lav-latenstid modeller, og åpne vekt-modeller. Nåværende eksempler inkluderer OpenAI GPT-5.x modeller, Anthropic Claude 4.x modeller, Google Gemini 3.x modeller, Meta Llama 4 modeller og Mistral modeller. Ikke velg kun basert på utgivelsesdato eller pris; sammenlign oppgavekvalitet, latenstid, kontekstvindu, verktøybruk, sikkerhetsatferd, regional tilgjengelighet og totale kostnader. [Microsoft Foundry modellkatalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) er et godt sted å sammenligne modeller tilgjengelig på Azure.

- **Multimodalitet**. Mange nåværende modeller kan prosessere mer enn tekst. Noen aksepterer bilde-, lyd- eller videoinndata; noen kan kalle verktøy; og spesialiserte modeller kan generere bilder, lyd eller video. For eksempel, nåværende OpenAI-modeller støtter tekst- og bildeinput, Gemini-modeller kan støtte tekst, kode, bilde, lyd og video, avhengig av variant, og Llama 4 Scout og Maverick er åpne vekt nativt multimodale modeller. Sjekk alltid hver modellkort for støttede inndata- og utdata-modaliteter før du bygger en arbeidsflyt rundt den.

Å velge en modell betyr at du får noen grunnleggende kapasitet, som kanskje ikke er nok. Ofte har du bedrifts-spesifikke data som du på en eller annen måte må informere LLM-en om. Det finnes noen ulike valg for hvordan man kan nærme seg det, mer om dette i de kommende seksjonene.

### Foundation-modeller versus LLM-er

Begrepet Foundation Model ble [myntet av Stanford-forskere](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) og definert som en AI-modell som følger noen kriterier, slik som:

- **De trenes ved hjelp av usupervised eller selvsupervisert læring**, som betyr at de trenes på umerkede multimodale data, og de krever ikke menneskelig annotering eller merking av data for treningsprosessen.
- **De er svært store modeller**, basert på veldig dype nevrale nettverk trent på milliarder av parametere.
- **De er normalt ment å tjene som en 'grunnmur' for andre modeller**, noe som betyr at de kan brukes som et utgangspunkt for at andre modeller bygges på toppen av, som kan gjøres ved finjustering.

![Foundation Models versus LLMs](../../../translated_images/no/FoundationModel.e4859dbb7a825c94.webp)

Bildekilde: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

For å klargjøre skillelinjen ytterligere, la oss ta ChatGPT som et historisk eksempel. Tidlige versjoner av ChatGPT brukte GPT-3.5 som en foundation-modell. OpenAI brukte deretter chatt-spesifikke data og tilpasningsteknikker for å lage en justert versjon som presterte bedre i samtalescenarier, slik som chatbots. Moderne AI-tjenester ruter ofte mellom flere modellvarianter, så tjenestenavnet og den underliggende modellens navn er ikke alltid det samme.

![Foundation Model](../../../translated_images/no/Multimodal.2c389c6439e0fc51.webp)

Bildekilde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Åpne-vekt/åpen-kilde versus proprietære modeller

En annen måte å kategorisere LLM-er på er om de er åpne-vekt, åpen-kilde, eller proprietære.

Åpen-kilde og åpne-vekt modeller gjør modellartefakter tilgjengelige for inspeksjon, nedlasting eller tilpasning, men lisensene deres varierer. Noen er fullstendig åpen kildekode, mens andre er åpne-vekt modeller med bruksbegrensninger. De kan være nyttige når en bedrift trenger mer kontroll over distribusjon, datalokalisering, kostnader eller tilpasning. Likevel må team fortsatt gå gjennom lisensbetingelser, serveringskostnader, vedlikehold, sikkerhetsoppdateringer og evalueringskvalitet før bruk i produksjon. Eksempler inkluderer [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), noen [Mistral-modeller](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) og mange modeller hostet på [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietære modeller eies og hostes av en tilbyder. Disse modellene er ofte optimalisert for administrert produksjonsbruk og kan tilby sterk støtte, sikkerhetssystemer, verktøyintegrasjon og skalerbarhet. Likevel kan kunder vanligvis ikke inspisere eller endre modellvektene, og må gjennomgå tilbyderens vilkår for personvern, oppbevaring, samsvar og akseptabel bruk. Eksempler inkluderer [OpenAI-modeller](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), og [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus bildegenerering versus tekst- og kodegenerering

LLM-er kan også kategoriseres etter hvilken type output de genererer.

Embeddings er en gruppe modeller som kan konvertere tekst til en numerisk form, kalt embedding, som er en numerisk representasjon av inngangsteksten. Embeddings gjør det enklere for maskiner å forstå relasjonene mellom ord eller setninger og kan brukes som input for andre modeller, slik som klassifiseringsmodeller eller klyngemodeller som har bedre ytelse på numeriske data. Embedding-modeller brukes ofte for transfer learning, der en modell bygges for en surrogatoppgave med rikelig data, og deretter gjenbrukes modellvektene (embeddingene) for andre nedstrømsoppgaver. Et eksempel på denne kategorien er [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/no/Embedding.c3708fe988ccf760.webp)

Bildegenereringsmodeller er modeller som genererer bilder. Disse modellene brukes ofte til bildebehandling, bildesyntese og bildeoversettelse. Bildgenereringsmodeller trenes ofte på store datasett av bilder, slik som [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), og kan brukes til å generere nye bilder eller redigere eksisterende bilder med teknikker som inpainting, superoppløsning og fargelegging. Eksempler inkluderer [GPT Image-modeller](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion-modeller](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) og Imagen-modeller.

![Image generation](../../../translated_images/no/Image.349c080266a763fd.webp)

Tekst- og kodegenereringsmodeller er modeller som genererer tekst eller kode. Disse modellene brukes ofte til tekstoppsummering, oversettelse og spørsmål-svar. Tekstgenereringsmodeller trenes ofte på store tekstdatasett, slik som [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), og kan brukes til å generere ny tekst eller svare på spørsmål. Kodegenereringsmodeller, som [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), trenes ofte på store kode-datasett, slik som GitHub, og kan brukes til å generere ny kode eller rette feil i eksisterende kode.

![Text and code generation](../../../translated_images/no/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Kun dekoder

For å snakke om ulike arkitekturtyper av LLM-er, la oss bruke en analogi.

Forestill deg sjefen din ga deg en oppgave om å skrive en quiz til studentene. Du har to kollegaer; en som lager innholdet, og en annen som gjennomgår det.

Innholdsskaperen er som en kun dekoder-modell: de kan se på temaet, se hva du allerede har skrevet, og fortsette å generere innhold basert på denne konteksten. De er veldig gode til å skrive engasjerende og informativt innhold, men ikke alltid best egnet når oppgaven bare er å klassifisere, hente eller kode informasjon. Eksempler på kun dekoder modellfamilier er GPT og Llama-modeller.

Gjennomgangspersonen er som en kun encoder-modell, de ser på den skrevne materialet og svarene, legger merke til forholdet mellom dem og forstår kontekst, men er ikke gode til å generere innhold. Et eksempel på kun encoder-modell er BERT.

Tenk at vi kan ha noen som både kunne lage og gjennomgå quizzen, dette er en encoder-decoder modell. Noen eksempler er BART og T5.

### Tjeneste versus Modell

Nå, la oss snakke om forskjellen på en tjeneste og en modell. En tjeneste er et produkt som tilbys av en sky-leverandør, og er ofte en kombinasjon av modeller, data og andre komponenter. En modell er kjernen i en tjeneste, og er ofte en grunnmur-modell, slik som en LLM.

Tjenester er ofte optimalisert for produksjonsbruk og er ofte enklere å bruke enn modeller, via en grafisk brukergrensesnitt. Likevel er tjenester ikke alltid gratis tilgjengelige, og kan kreve abonnement eller betaling for bruk, til gjengjeld for å benytte tjenesteeierens utstyr og ressurser, optimalisere kostnader og skalere enkelt. Et eksempel på en tjeneste er [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), som tilbyr en betalingsmodell basert på forbruk, noe som betyr at brukere betaler proporsjonalt med tjenestebruk. Azure OpenAI Service tilbyr også bedriftsgradert sikkerhet og en ansvarlig AI-rammeverk på toppen av modellens kapasiteter.

Modeller er nevrale nettverk-artefakter: parametere, vekter, arkitektur, tokenizer og støttende konfigurasjon. Å kjøre en modell lokalt eller i et privat miljø krever egnet maskinvare, serverinfrastruktur, overvåking, og enten en kompatibel åpen-kilde/åpen-vekt lisens eller en kommersiell lisens. Åpne-vekt modeller som Llama 4 eller Mistral-modeller kan hostes selv, men krever fortsatt regnekraft og operasjonell kompetanse.

## Hvordan teste og iterere med ulike modeller for å forstå ytelse på Azure


Når teamet vårt har utforsket det nåværende landskapet for LLM-er og identifisert noen gode kandidater for deres scenarier, er neste steg å teste dem på deres data og arbeidsbelastning. Dette er en iterativ prosess, utført gjennom eksperimenter og målinger.
De fleste av modellene vi nevnte i tidligere avsnitt (OpenAI-modeller, åpne vektsmodeller som Llama 4 og Mistral, og Hugging Face-modeller) er tilgjengelige i [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), tidligere Azure AI Studio/Azure AI Foundry, er en sammenslått Azure-plattform for å bygge AI-apper og agenter. Den hjelper utviklere med å håndtere livssyklusen fra eksperimentering og evaluering til distribusjon, overvåking og styring. Modellkatalogen i Microsoft Foundry gjør det mulig for brukeren å:

- Finne grunnlagsmodellen av interesse i katalogen, inkludert modeller solgt av Azure og modeller fra partnere og fellesskapsleverandører. Brukere kan filtrere på oppgave, leverandør, lisens, distribusjonsalternativ eller navn.

![Model catalog](../../../translated_images/no/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Gå gjennom modellkortet, inkludert en detaljert beskrivelse av tiltenkt bruk og treningsdata, kodeeksempler og evalueringsresultater på det interne evalueringsbiblioteket.

![Model card](../../../translated_images/no/ModelCard.598051692c6e400d.webp)

- Sammenligne referansetester på tvers av modeller og datasett tilgjengelig i bransjen for å vurdere hvilken som oppfyller forretningsscenariet, gjennom [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)-panelet.

![Model benchmarks](../../../translated_images/no/ModelBenchmarks.254cb20fbd06c03a.webp)

- Finjustere støttede modeller på egendata for å forbedre modellens ytelse i en spesifikk arbeidsbelastning, ved å utnytte eksperimenterings- og sporingsmulighetene til Microsoft Foundry.

![Model fine-tuning](../../../translated_images/no/FineTuning.aac48f07142e36fd.webp)

- Distribuere den opprinnelige forhåndstrente modellen eller den finjusterte versjonen til et eksternt sanntidsinferenzendepunkt, ved bruk av administrerte databehandlings- eller serverløse distribusjonsalternativer, for å gjøre det mulig for applikasjoner å konsumere den.

![Model deployment](../../../translated_images/no/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Ikke alle modellene i katalogen er for øyeblikket tilgjengelige for finjustering og/eller betaling etter bruk-distribusjon. Sjekk modellkortet for detaljer om modellens kapasiteter og begrensninger.

## Forbedring av LLM-resultater

Vi har sammen med vårt oppstartsteam utforsket ulike typer LLM-er og en skyplattform (Microsoft Foundry) som gjør det mulig å sammenligne ulike modeller, evaluere dem på testdata, forbedre ytelsen og distribuere dem på inferensendepunkter.

Men når bør de vurdere å finjustere en modell i stedet for å bruke en forhåndstrent en? Finnes det andre tilnærminger for å forbedre modellens ytelse på spesifikke arbeidsbelastninger?

Det finnes flere tilnærminger en bedrift kan bruke for å få de resultatene de trenger fra en LLM. Du kan velge forskjellige typer modeller med ulike grader av trening når du distribuerer en LLM i produksjon, med forskjellige nivåer av kompleksitet, kostnad og kvalitet. Her er noen forskjellige tilnærminger:

- **Prompt engineering med kontekst**. Ideen er å gi nok kontekst når du gir instruksjoner for å sikre at du får svarene du trenger.

- **Retrieval Augmented Generation, RAG**. Dine data kan for eksempel eksistere i en database eller et webelement; for å sikre at disse dataene, eller et delsett av dem, inkluderes ved tidspunkt for prompten, kan du hente relevante data og gjøre dem til en del av brukerens prompt.

- **Finjustert modell**. Her har du trent modellen videre på egne data, noe som gjør modellen mer presis og responsiv til dine behov, men det kan være kostbart.

![LLMs deployment](../../../translated_images/no/Deploy.18b2d27412ec8c02.webp)

Bildets kilde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering med Kontekst

Forhåndstrente LLM-er fungerer veldig godt på generaliserte oppgaver innen naturlig språk, selv ved å kalle dem med en kort prompt, som en setning som skal fullføres eller et spørsmål – den såkalte «zero-shot» læringen.

Jo mer brukeren kan ramme inn forespørselen med en detaljert anmodning og eksempler – konteksten – desto mer nøyaktig og nær brukerens forventninger vil svaret være. I dette tilfellet snakker vi om «one-shot» læring hvis prompten inneholder bare ett eksempel og «few-shot» læring hvis den inneholder flere eksempler.
Prompt engineering med kontekst er den mest kostnadseffektive tilnærmingen å starte med.

### Retrieval Augmented Generation (RAG)

LLM-er har den begrensningen at de kun kan bruke data som har blitt brukt under treningen for å generere et svar. Dette betyr at de ikke vet noe om faktiske hendelser som skjedde etter treningsprosessen, og de kan ikke få tilgang til ikke-offentlig informasjon (som bedriftsdata).
Dette kan overvinnes gjennom RAG, en teknikk som utvider prompten med eksterne data i form av dokumentbiter, med tanke på promptens lengdebegrensninger. Dette støttes av verktøy for vektordatabaser (som [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) som henter nyttige biter fra forskjellige forhåndsdefinerte datakilder og legger dem til som en del av prompt-konteksten.

Denne teknikken er svært nyttig når en bedrift ikke har nok data, tid eller ressurser til å finjustere en LLM, men likevel ønsker å forbedre ytelsen på en spesifikk arbeidsbelastning og redusere risikoen for hallusinerte, utdaterte eller ubegrunnede svar.

### Finjustert modell

Finjustering er en prosess som utnytter transferlæring for å ‘tilpasse’ modellen til en påfølgende oppgave eller løse et spesifikt problem. I motsetning til few-shot læring og RAG, resulterer denne i at en ny modell genereres, med oppdaterte vekter og biaser. Den krever et sett med trenings-eksempler bestående av en enkelt inngang (prompten) og tilhørende utgang (fullføringen).
Dette vil være den foretrukne tilnærmingen hvis:

- **Bruk av mindre oppgavespesifikke modeller**. En bedrift ønsker å finjustere en mindre modell for en smal oppgave i stedet for gjentatte ganger å gi prompt til en større grenseløs modell, noe som resulterer i en mer kostnadseffektiv og raskere løsning.

- **Vurdering av latenstid**. Latenstid er viktig for en spesifikk bruksområde, så det er ikke mulig å bruke veldig lange prompts, eller antall eksempler som modellen skal lære fra, passer ikke innenfor promptens lengdebegrensning.

- **Tilpasning av stabil oppførsel**. En bedrift har mange høykvalitets eksempler og ønsker at modellen konsekvent følger en oppgave, utdataformat, tone eller domene-spesifikk stil. Hvis hovedproblemet er ferske fakta eller privat kunnskap som endres ofte, bør man heller bruke RAG enn å stole på finjustering alene.

### Trenet modell

Å trene en LLM fra bunnen av er uten tvil den vanskeligste og mest komplekse tilnærmingen å ta i bruk, som krever enorme mengder data, dyktige ressurser og passende datakraft. Dette alternativet bør bare vurderes i et scenario hvor en bedrift har et domenespesifikt bruksområde og store mengder domene-sentrerte data.

## Kunnskapssjekk

Hva kan være en god tilnærming for å forbedre LLM fullføringsresultater?

1. Prompt engineering med kontekst
1. RAG
1. Finjustert modell

A: Alle tre kan hjelpe. Start med prompt engineering og kontekst for raske forbedringer, og bruk RAG når modellen trenger oppdaterte fakta eller privat bedriftsdata. Velg finjustering når du har nok høykvalitets eksempler og trenger at modellen konsekvent følger en oppgave, format, tone eller domenemønster.

## 🚀 Utfordring

Les mer om hvordan du kan [bruke RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) i din virksomhet.

## Flott jobba, fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve kunnskapen din om Generative AI!

Gå videre til Leksjon 3 hvor vi vil se på hvordan man kan [bygge med Generative AI Ansvarlig](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->