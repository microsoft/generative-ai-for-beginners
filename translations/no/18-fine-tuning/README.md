[![Open Source Models](../../../translated_images/no/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering av din LLM

Å bruke store språkmodeller for å bygge generative AI-applikasjoner kommer med nye utfordringer. En viktig problemstilling er å sikre responsernes kvalitet (nøyaktighet og relevans) i innhold generert av modellen for en gitt brukerforespørsel. I tidligere leksjoner har vi diskutert teknikker som prompt engineering og retrieval-augmented generation som prøver å løse problemet ved å _endre prompt-innspillingen_ til den eksisterende modellen.

I dagens leksjon diskuterer vi en tredje teknikk, **finjustering**, som prøver å løse utfordringen ved å _videreutdanne modellen selv_ med tillegg av data. La oss dykke ned i detaljene.

## Læringsmål

Denne leksjonen introduserer konseptet finjustering for forhåndstrente språkmodeller, utforsker fordelene og utfordringene med denne tilnærmingen, og gir veiledning om når og hvordan man kan bruke finjustering for å forbedre ytelsen til dine generative AI-modeller.

Etter denne leksjonen skal du kunne svare på følgende spørsmål:

- Hva er finjustering for språkmodeller?
- Når, og hvorfor, er finjustering nyttig?
- Hvordan kan jeg finjustere en forhåndstrent modell?
- Hva er begrensningene med finjustering?

Klar? La oss komme i gang.

## Illustrert guide

Ønsker du å få en oversikt over hva vi skal dekke før vi dykker inn? Sjekk ut denne illustrerte guiden som beskriver læringsreisen for denne leksjonen – fra å lære kjernebegrepene og motivasjonen for finjustering, til å forstå prosessen og beste praksis for å utføre finjusteringsoppgaven. Dette er et fascinerende tema å utforske, så ikke glem å sjekke ut [Ressurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) siden for flere lenker som støtter din selvstyrte læringsreise!

![Illustrert guide til finjustering av språkmodeller](../../../translated_images/no/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Hva er finjustering for språkmodeller?

Etter definisjon er store språkmodeller _forhåndstrent_ på store mengder tekst fra mange forskjellige kilder, inkludert internett. Som vi har lært i tidligere leksjoner, trenger vi teknikker som _prompt engineering_ og _retrieval-augmented generation_ for å forbedre kvaliteten på modellens svar på brukerens spørsmål ("prompter").

En populær teknikk innen prompt engineering innebærer å gi modellen mer veiledning om hva som forventes i svaret, enten ved å gi _instruksjoner_ (eksplisitt veiledning) eller _gi noen få eksempler_ (implisitt veiledning). Dette kalles _few-shot learning_, men det har to begrensninger:

- Modellens token-grenser kan begrense antallet eksempler du kan gi, og redusere effektiviteten.
- Modellens token-kostnader kan gjøre det dyrt å legge til eksempler i hver prompt, og begrense fleksibiliteten.

Finjustering er en vanlig praksis i maskinlæringssystemer hvor man tar en forhåndstrent modell og videreutdanner den med nye data for å forbedre ytelsen på en spesifikk oppgave. I sammenheng med språkmodeller kan vi finjustere den forhåndstrente modellen _med et kuratert sett av eksempler for en gitt oppgave eller applikasjonsområde_ for å lage en **tilpasset modell** som kan være mer nøyaktig og relevant for akkurat den oppgaven eller domenet. En tilleggseffekt av finjustering er at det også kan redusere antallet eksempler som trengs for few-shot learning – og dermed redusere token-bruken og relaterte kostnader.

## Når og hvorfor bør vi finjustere modeller?

I _denne_ sammenhengen, når vi snakker om finjustering, refererer vi til **overvåket** finjustering der videreutdanningen gjøres ved å **legge til nye data** som ikke var en del av det opprinnelige treningsdatasettet. Dette er forskjellig fra en ikke-overvåket finjustering der modellen trenes på nytt på det opprinnelige datasettet, men med andre hyperparametere.

Det viktigste å huske er at finjustering er en avansert teknikk som krever et visst nivå av ekspertise for å oppnå ønskede resultater. Dersom det gjøres feil, kan det hende man ikke får de forventede forbedringene, og det kan til og med forringe modellens ytelse for det målrettede domenet.

Så, før du lærer "hvordan" du skal finjustere språkmodeller, må du vite "hvorfor" du bør velge denne metoden, og "når" du skal starte prosessen med finjustering. Start med å stille deg disse spørsmålene:

- **Bruksområde**: Hva er ditt _brukstilfelle_ for finjustering? Hvilket aspekt av den nåværende forhåndstrente modellen ønsker du å forbedre?
- **Alternativer**: Har du prøvd _andre teknikker_ for å oppnå ønskede resultater? Bruk dem til å lage en referanse for sammenligning.
  - Prompt engineering: Prøv teknikker som few-shot prompting med eksempler på relevante prompt-svar. Evaluer kvaliteten på svarene.
  - Retrieval Augmented Generation: Prøv å berike prompter med søkeresultater hentet fra dine data. Evaluer kvaliteten på svarene.
- **Kostnader**: Har du identifisert kostnadene for finjustering?
  - Mulighet for tuning – er den forhåndstrente modellen tilgjengelig for finjustering?
  - Innsats – for å forberede treningsdata, evaluere og forbedre modellen.
  - Beregningsressurser – for å kjøre finjusteringsjobber og distribuere finjustert modell.
  - Data – tilgang til tilstrekkelig kvalitetsdata for finjusteringens effekt.
- **Fordeler**: Har du bekreftet fordelene ved finjustering?
  - Kvalitet – overgikk den finjusterte modellen referansemodellen?
  - Kostnader – reduserer den token-bruk ved å forenkle prompter?
  - Utvidbarhet – kan du viderebruke grunnmodellen for nye domener?

Ved å svare på disse spørsmålene bør du kunne avgjøre om finjustering er riktig tilnærming for ditt brukstilfelle. Ideelt sett er metoden gyldig kun dersom fordelene oppveier kostnadene. Når du har bestemt deg for å gå videre, er det på tide å tenke på _hvordan_ du kan finjustere den forhåndstrente modellen.

Ønsker du å få flere innsikter i beslutningsprosessen? Se [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hvordan kan vi finjustere en forhåndstrent modell?

For å finjustere en forhåndstrent modell, trenger du:

- en forhåndstrent modell å finjustere
- et datasett å bruke for finjustering
- et treningsmiljø for å kjøre finjusteringsjobben
- et hosting-miljø for å distribuere den finjusterte modellen

## Finjustering i praksis

> **Merk:** `gpt-35-turbo` / `gpt-3.5-turbo`, som refereres til i noen av tutorialene nedenfor, er pensjonert for både inferens og finjustering. Hvis du starter en ny finjusteringsjobb i dag, bør du sikte deg inn på en modell som for øyeblikket støttes – for eksempel `gpt-4o-mini` eller `gpt-4.1-mini`. Se [Listen over modeller for finjustering](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) for nåværende sett av finjusterbare modeller. Konseptene og trinnene i disse tutorialene gjelder fortsatt.

Følgende ressurser gir steg-for-steg veiledninger for å gå gjennom et ekte eksempel der en valgt modell brukes med et kuratert datasett. For å jobbe med disse tutorialene trenger du en konto hos den spesifikke leverandøren, samt tilgang til relevant modell og datasett.

| Leverandør     | Tutorial                                                                                                                                                                       | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hvordan finjustere chattmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lær å finjustere en `gpt-35-turbo` for et spesifikt domene ("oppskriftassistent") ved å forberede treningsdata, kjøre finjusteringsjobben og bruke den finjusterte modellen til inferens.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo finjusteringsøkt](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Lær å finjustere en `gpt-35-turbo-0613` modell **på Azure** ved å følge steg for å lage og laste opp treningsdata, kjøre finjusteringsjobben, distribuere og bruke den nye modellen.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Finjustere LLMs med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dette blogginnlegget guider deg gjennom finjustering av en _åpen LLM_ (f.eks. `CodeLlama 7B`) ved å bruke [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket og [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med åpne [datasett](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finjustering av LLMs med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) er et python-bibliotek utviklet av Hugging Face som tillater finjustering for mange forskjellige oppgaver inkludert finjustering av LLMs. AutoTrain er en løsning uten behov for koding og finjustering kan gjøres i din egen sky, på Hugging Face Spaces eller lokalt. Den støtter både et webbasert GUI, CLI og trening via yaml-konfigurasjonsfiler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finjustering av LLMs med Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth er en åpen kildekode-rammeverk som støtter finjustering av LLM og forsterkende læring (RL). Unsloth forenkler lokal trening, evaluering og distribusjon med klare [notatbøker](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Den støtter også tekst-til-tale (TTS), BERT og multimodale modeller. For å komme i gang, les deres steg-for-steg [Finjustering LLMs guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Oppgave

Velg en av tutorialene ovenfor og gjennomfør den. _Vi kan gjenskape en versjon av disse tutorialene i Jupyter Notebooks i dette repoet kun for referanse. Vennligst bruk de originale kildene direkte for å få de nyeste versjonene_.

## Flott arbeid! Fortsett læringen din.

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å bygge på kunnskapen din om Generativ AI!

Gratulerer!! Du har fullført den siste leksjonen i v2-serien for dette kurset! Ikke slutte å lære og bygge. \*\*Sjekk ut [RESSURSER](RESOURCES.md?WT.mc_id=academic-105485-koreyst)-siden for en liste over flere forslag bare for dette temaet.

Vår v1-serie av leksjoner har også blitt oppdatert med flere oppgaver og konsepter. Så bruk et minutt på å friske opp kunnskapen din - og vær så snill å [del dine spørsmål og tilbakemeldinger](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) for å hjelpe oss med å forbedre disse leksjonene for fellesskapet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->