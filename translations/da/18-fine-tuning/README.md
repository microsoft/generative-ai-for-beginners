[![Open Source Modeller](../../../translated_images/da/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering af din LLM

Brugen af store sprogmodeller til at bygge generative AI-applikationer medfører nye udfordringer. Et nøgleproblem er at sikre svarenes kvalitet (nøjagtighed og relevans) i det indhold, modellen genererer for en given brugerforespørgsel. I tidligere lektioner har vi diskuteret teknikker som prompt engineering og retrieval-augmented generation, der forsøger at løse problemet ved _at ændre promptinputtet_ til den eksisterende model.

I dagens lektion diskuterer vi en tredje teknik, **finjustering**, som forsøger at tackle udfordringen ved _at genuddanne selve modellen_ med yderligere data. Lad os dykke ned i detaljerne.

## Læringsmål

Denne lektion introducerer konceptet finjustering for fortrænede sprogmodeller, udforsker fordelene og udfordringerne ved denne tilgang, og giver vejledning i, hvornår og hvordan man bruger finjustering til at forbedre ydelsen af dine generative AI-modeller.

Når du er færdig med denne lektion, skulle du kunne besvare følgende spørgsmål:

- Hvad er finjustering for sprogmodeller?
- Hvornår og hvorfor er finjustering nyttigt?
- Hvordan kan jeg finjustere en fortrænet model?
- Hvad er begrænsningerne ved finjustering?

Klar? Lad os komme i gang.

## Illustreret guide

Vil du have et overblik over, hvad vi vil dække, inden vi går i dybden? Se denne illustrerede guide, som beskriver læringsrejsen for denne lektion – fra at lære kernekoncepter og motivationen for finjustering, til at forstå processen og bedste praksis for at udføre finjusteringsopgaven. Dette er et fascinerende emne at udforske, så glem ikke at tjekke [Ressourcer](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)-siden for yderligere links, der kan støtte din selvstyrede læringsrejse!

![Illustreret Guide til Finjustering af Sprogmodeller](../../../translated_images/da/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Hvad er finjustering for sprogmodeller?

Per definition er store sprogmodeller _fortrænet_ på store mængder tekst hentet fra forskellige kilder inklusiv internettet. Som vi har lært i tidligere lektioner, har vi brug for teknikker som _prompt engineering_ og _retrieval-augmented generation_ for at forbedre kvaliteten af modellens svar på brugerens spørgsmål ("prompter").

En populær prompt-engineering teknik involverer at give modellen mere vejledning i, hvad der forventes i svaret, enten ved at give _instruktioner_ (eksplicit vejledning) eller _give den nogle få eksempler_ (implicit vejledning). Dette kaldes _few-shot learning_, men det har to begrænsninger:

- Modellens token-grænser kan begrænse antallet af eksempler, du kan give, og begrænse effektiviteten.
- Modellens token-omkostninger kan gøre det dyrt at tilføje eksempler til hver prompt og begrænse fleksibiliteten.

Finjustering er en almindelig praksis i maskinlæringssystemer, hvor vi tager en fortrænet model og genuddanner den med nye data for at forbedre dens ydelse på en specifik opgave. I konteksten af sprogmodeller kan vi finjustere den fortrænede model _med et kurateret sæt eksempler for en given opgave eller anvendelsesdomæne_ for at skabe en **tilpasset model**, der kan være mere nøjagtig og relevant for netop denne opgave eller domæne. En sidegevinst ved finjustering er, at det også kan reducere antallet af eksempler, der er nødvendige for few-shot learning – hvilket reducerer tokenforbruget og relaterede omkostninger.

## Hvornår og hvorfor skal vi finjustere modeller?

I _denne_ kontekst, når vi taler om finjustering, henviser vi til **superviseret** finjustering, hvor genuddannelsen udføres ved at **tilføje nye data**, som ikke var en del af det oprindelige træningsdatasæt. Dette er forskelligt fra en unsuperviseret finjusteringstilgang, hvor modellen genuddannes på de oprindelige data, men med forskellige hyperparametre.

Det vigtigste at huske er, at finjustering er en avanceret teknik, der kræver et vist niveau af ekspertise for at opnå de ønskede resultater. Hvis det gøres forkert, kan det ikke levere de forventede forbedringer og kan endda forringe modellens ydelse for dit målrettede domæne.

Så før du lærer "hvordan" man finjusterer sprogmodeller, skal du vide "hvorfor" du bør vælge denne vej og "hvornår" du skal starte finjusteringsprocessen. Start med at stille dig selv disse spørgsmål:

- **Brugssag**: Hvad er din _brugssag_ for finjustering? Hvilket aspekt af den nuværende fortrænede model vil du forbedre?
- **Alternativer**: Har du prøvet _andre teknikker_ for at opnå de ønskede resultater? Brug dem til at skabe en baseline for sammenligning.
  - Prompt engineering: Prøv teknikker som few-shot prompting med eksempler på relevante prompt-svar. Evaluer svarenes kvalitet.
  - Retrieval Augmented Generation: Prøv at forøge prompter med forespørgselsresultater, hentet ved at søge i dine data. Evaluer svarenes kvalitet.
- **Omkostninger**: Har du identificeret omkostningerne ved finjustering?
  - Tilpasningsevne - er den fortrænede model tilgængelig for finjustering?
  - Arbejdsindsats - til forberedelse af træningsdata, evaluering og forfining af modellen.
  - Beregning - til at køre finjusteringsopgaver og implementere finjusteret model.
  - Data - adgang til et tilstrækkeligt kvalitetsudvalg af eksempler til finjustering.
- **Fordele**: Har du bekræftet fordelene ved finjustering?
  - Kvalitet - overgik den finjusterede model baselinen?
  - Omkostning - reducerer det tokenforbruget ved at forenkle prompter?
  - Udvidelsesmuligheder - kan du genbruge basismodellen til nye domæner?

Ved at besvare disse spørgsmål bør du kunne afgøre, om finjustering er den rigtige tilgang for din brugssag. Ideelt set er tilgangen kun gyldig, hvis fordelene opvejer omkostningerne. Når du beslutter dig for at fortsætte, er det tid til at tænke over _hvordan_ du kan finjustere den fortrænede model.

Vil du have flere indsigter om beslutningsprocessen? Se [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hvordan kan vi finjustere en fortrænet model?

For at finjustere en fortrænet model skal du have:

- en fortrænet model til finjustering
- et datasæt til brug ved finjustering
- et træningsmiljø til at køre finjusteringsopgaven
- et hostingmiljø til at implementere den finjusterede model

## Finjustering i praksis

> **Note:** `gpt-35-turbo` / `gpt-3.5-turbo`, som refereres til i nogle af nedenstående vejledninger, er udfaset både til inferens og finjustering. Hvis du starter en ny finjusteringsopgave i dag, så ret dig mod en aktuelt understøttet model i stedet – for eksempel `gpt-4o-mini` eller `gpt-4.1-mini`. Se listen over [Finjusterbare modeller](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) for det aktuelle sæt af modeller, der kan finjusteres. Koncepterne og trinene i disse tutorials gælder stadig.

Følgende ressourcer indeholder trin-for-trin vejledninger til at guide dig gennem et reelt eksempel med en udvalgt model og et kurateret datasæt. For at arbejde med disse vejledninger skal du have en konto hos den specifikke udbyder samt adgang til den relevante model og datasæt.

| Udbyder     | Tutorial                                                                                                                                                                       | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lær at finjustere en `gpt-35-turbo` for et specifikt domæne ("recipe assistant") ved at forberede træningsdata, køre finjusteringsjobbet og bruge den finjusterede model til inferens.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Lær at finjustere en `gpt-35-turbo-0613` model **på Azure** ved at tage skridt til at oprette og uploade træningsdata, køre finjusteringsjobbet. Implementer og brug den nye model.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Denne blogpost guider dig i finjustering af en _åben LLM_ (fx `CodeLlama 7B`) ved brug af [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket og [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med åbne [datasæt](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) er et python-bibliotek udviklet af Hugging Face, som tillader finjustering for mange forskellige opgaver, inklusiv LLM finjustering. AutoTrain er en no-code løsning, og finjustering kan udføres i din egen cloud, på Hugging Face Spaces eller lokalt. Det understøtter både en web-baseret GUI, CLI samt træning via yaml-konfigurationsfiler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth er et open-source framework, der understøtter LLM finjustering og reinforcement learning (RL). Unsloth strømliner lokal træning, evaluering og implementering med klar-til-brug [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Det understøtter også text-to-speech (TTS), BERT og multimodale modeller. For at komme i gang, læs deres trin-for-trin [Finjustering af LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Opgave

Vælg en af ovenstående tutorials og gennemgå den. _Vi kan eventuelt gengive en version af disse tutorials i Jupyter Notebooks i dette repo kun til reference. Brug venligst de originale kilder direkte for at få de nyeste versioner_.

## Godt arbejde! Fortsæt din læring.

Når du har gennemført denne lektion, så tjek vores [Generative AI Learning kollektion](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din Generative AI-viden!

Tillykke!! Du har gennemført den afsluttende lektion i v2-serien for dette kursus! Stop ikke med at lære og bygge videre. \*\*Tjek [RESSOURCER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) siden for en liste over yderligere forslag til netop dette emne.

Vores v1-serie af lektioner er også blevet opdateret med flere opgaver og koncepter. Så brug et øjeblik på at genopfriske din viden – og del venligst [dine spørgsmål og feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) for at hjælpe os med at forbedre disse lektioner for fællesskabet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->