<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T19:13:18+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "da"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.da.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering af din LLM

At bruge store sprogmodeller til at bygge generative AI-applikationer medfører nye udfordringer. En vigtig problemstilling er at sikre kvaliteten af de svar (nøjagtighed og relevans), som modellen genererer til en given brugerforespørgsel. I tidligere lektioner har vi diskuteret teknikker som prompt engineering og retrieval-augmented generation, der forsøger at løse problemet ved _at ændre prompt-input_ til den eksisterende model.

I dagens lektion diskuterer vi en tredje teknik, **finjustering**, som forsøger at tackle udfordringen ved _at genuddanne selve modellen_ med yderligere data. Lad os dykke ned i detaljerne.

## Læringsmål

Denne lektion introducerer konceptet finjustering af fortrænede sprogmodeller, udforsker fordelene og udfordringerne ved denne tilgang og giver vejledning om, hvornår og hvordan man kan bruge finjustering til at forbedre ydeevnen af dine generative AI-modeller.

Ved slutningen af denne lektion bør du kunne besvare følgende spørgsmål:

- Hvad er finjustering af sprogmodeller?
- Hvornår og hvorfor er finjustering nyttigt?
- Hvordan kan jeg finjustere en fortrænet model?
- Hvad er begrænsningerne ved finjustering?

Klar? Lad os komme i gang.

## Illustreret guide

Vil du have det store overblik over, hvad vi dækker, før vi dykker ned? Tjek denne illustrerede guide, der beskriver læringsrejsen for denne lektion - fra at lære de grundlæggende begreber og motivationen for finjustering til at forstå processen og bedste praksis for at udføre finjusteringsopgaven. Dette er et fascinerende emne at udforske, så glem ikke at tjekke [Ressourcer](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) siden for yderligere links til at støtte din selvstyrede læringsrejse!

![Illustreret guide til finjustering af sprogmodeller](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.da.png)

## Hvad er finjustering af sprogmodeller?

Per definition er store sprogmodeller _fortrænede_ på store mængder tekst hentet fra forskellige kilder, herunder internettet. Som vi har lært i tidligere lektioner, har vi brug for teknikker som _prompt engineering_ og _retrieval-augmented generation_ for at forbedre kvaliteten af modellens svar på brugerens spørgsmål ("prompts").

En populær prompt-engineering teknik involverer at give modellen mere vejledning om, hvad der forventes i svaret, enten ved at give _instruktioner_ (eksplicit vejledning) eller _give den nogle eksempler_ (implicit vejledning). Dette kaldes _few-shot learning_, men det har to begrænsninger:

- Modellens token-grænser kan begrænse antallet af eksempler, du kan give, og begrænse effektiviteten.
- Modellens token-omkostninger kan gøre det dyrt at tilføje eksempler til hver prompt og begrænse fleksibiliteten.

Finjustering er en almindelig praksis i maskinlæringssystemer, hvor vi tager en fortrænet model og genuddanner den med nye data for at forbedre dens ydeevne på en specifik opgave. I konteksten af sprogmodeller kan vi finjustere den fortrænede model _med et kurateret sæt eksempler til en given opgave eller applikationsdomæne_ for at skabe en **tilpasset model**, der kan være mere præcis og relevant for den specifikke opgave eller det specifikke domæne. En sidegevinst ved finjustering er, at det også kan reducere antallet af eksempler, der er nødvendige for few-shot learning - hvilket reducerer tokenforbrug og relaterede omkostninger.

## Hvornår og hvorfor bør vi finjustere modeller?

I _denne_ kontekst, når vi taler om finjustering, refererer vi til **superviseret** finjustering, hvor genuddannelsen sker ved **at tilføje nye data**, der ikke var en del af det oprindelige træningsdatasæt. Dette er anderledes end en usuperviseret finjusteringsmetode, hvor modellen genuddannes på det oprindelige data, men med forskellige hyperparametre.

Det vigtigste at huske er, at finjustering er en avanceret teknik, der kræver et vist niveau af ekspertise for at opnå de ønskede resultater. Hvis det gøres forkert, kan det muligvis ikke give de forventede forbedringer og kan endda forringe modellens ydeevne for dit målrettede domæne.

Så før du lærer "hvordan" man finjusterer sprogmodeller, skal du vide "hvorfor" du bør tage denne vej, og "hvornår" du skal starte processen med finjustering. Start med at stille dig selv disse spørgsmål:

- **Brugsscenarie**: Hvad er dit _brugsscenarie_ for finjustering? Hvilket aspekt af den nuværende fortrænede model ønsker du at forbedre?
- **Alternativer**: Har du prøvet _andre teknikker_ for at opnå de ønskede resultater? Brug dem til at skabe en baseline for sammenligning.
  - Prompt engineering: Prøv teknikker som few-shot prompting med eksempler på relevante prompt-svar. Evaluer kvaliteten af svarene.
  - Retrieval Augmented Generation: Prøv at udvide prompts med forespørgselsresultater hentet ved at søge i dine data. Evaluer kvaliteten af svarene.
- **Omkostninger**: Har du identificeret omkostningerne ved finjustering?
  - Justerbarhed - er den fortrænede model tilgængelig for finjustering?
  - Indsats - for at forberede træningsdata, evaluere og forfine modellen.
  - Beregning - for at køre finjusteringsjobs og implementere den finjusterede model.
  - Data - adgang til tilstrækkelige kvalitets-eksempler for finjusteringspåvirkning.
- **Fordele**: Har du bekræftet fordelene ved finjustering?
  - Kvalitet - overgik den finjusterede model baseline?
  - Omkostninger - reducerer det tokenforbrug ved at forenkle prompts?
  - Udvidelsesmuligheder - kan du genbruge basismodellen til nye domæner?

Ved at besvare disse spørgsmål bør du kunne afgøre, om finjustering er den rigtige tilgang for dit brugsscenarie. Ideelt set er tilgangen kun gyldig, hvis fordelene opvejer omkostningerne. Når du beslutter dig for at fortsætte, er det tid til at tænke over _hvordan_ du kan finjustere den fortrænede model.

Vil du have flere indsigter i beslutningsprocessen? Se [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hvordan kan vi finjustere en fortrænet model?

For at finjustere en fortrænet model skal du have:

- en fortrænet model til finjustering
- et datasæt til brug for finjustering
- et træningsmiljø til at køre finjusteringsjobbet
- et hostingmiljø til at implementere den finjusterede model

## Finjustering i praksis

Følgende ressourcer giver trin-for-trin vejledninger til at guide dig gennem et reelt eksempel ved hjælp af en udvalgt model med et kurateret datasæt. For at arbejde gennem disse vejledninger skal du have en konto hos den specifikke udbyder samt adgang til den relevante model og datasæt.

| Udbyder      | Vejledning                                                                                                                                                                    | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lær at finjustere en `gpt-35-turbo` til et specifikt domæne ("opskriftassistent") ved at forberede træningsdata, køre finjusteringsjobbet og bruge den finjusterede model til inferens.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Lær at finjustere en `gpt-35-turbo-0613` model **på Azure** ved at tage skridt til at oprette og uploade træningsdata, køre finjusteringsjobbet. Implementer og brug den nye model.                                                                                                                                                                                                                                                 |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Denne blogpost guider dig gennem finjustering af en _åben LLM_ (fx `CodeLlama 7B`) ved hjælp af [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) med åbne [datasæt](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) er et Python-bibliotek udviklet af Hugging Face, der muliggør finjustering for mange forskellige opgaver, herunder LLM finjustering. AutoTrain er en no-code løsning, og finjustering kan udføres i din egen cloud, på Hugging Face Spaces eller lokalt. Det understøtter både en webbaseret GUI, CLI og træning via yaml-konfigurationsfiler.                                                       |
|              |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Opgave

Vælg en af vejledningerne ovenfor og gennemgå dem. _Vi kan muligvis replikere en version af disse vejledninger i Jupyter Notebooks i dette repo kun til reference. Brug venligst de originale kilder direkte for at få de nyeste versioner_.

## Godt arbejde! Fortsæt din læring.

Efter at have afsluttet denne lektion, tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generative AI!

Tillykke!! Du har afsluttet den sidste lektion fra v2-serien for dette kursus! Stop ikke med at lære og bygge. \*\*Tjek [RESSOURCER](RESOURCES.md?WT.mc_id=academic-105485-koreyst) siden for en liste over yderligere forslag til netop dette emne.

Vores v1-serie af lektioner er også blevet opdateret med flere opgaver og begreber. Så tag et øjeblik til at genopfriske din viden - og venligst [del dine spørgsmål og feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) for at hjælpe os med at forbedre disse lektioner for fællesskabet.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.