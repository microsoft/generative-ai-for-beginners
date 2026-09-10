[![Open Source Models](../../../translated_images/da/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering af dit LLM

Brug af store sprogmodeller til at bygge generative AI-applikationer kommer med nye udfordringer. Et nøglespørgsmål er at sikre svarenes kvalitet (nøjagtighed og relevans) i det indhold, modellen genererer for en given brugerforespørgsel. I tidligere lektioner har vi diskuteret teknikker som prompt engineering og retrieval-augmented generation, som forsøger at løse problemet ved at _ændre promptinputtet_ til den eksisterende model.

I dagens lektion diskuterer vi en tredje teknik, **finjustering**, som prøver at imødegå udfordringen ved _at genuddanne selve modellen_ med yderligere data. Lad os dykke ned i detaljerne.

## Læringsmål

Denne lektion introducerer begrebet finjustering for fortrænede sprogmodeller, udforsker fordelene og udfordringerne ved denne tilgang og giver vejledning i, hvornår og hvordan du kan bruge finjustering til at forbedre ydeevnen af dine generative AI-modeller.

Ved lektionens slutning bør du kunne besvare følgende spørgsmål:

- Hvad er finjustering for sprogmodeller?
- Hvornår og hvorfor er finjustering nyttig?
- Hvordan kan jeg finjustere en fortrænet model?
- Hvad er begrænsningerne ved finjustering?

Klar? Lad os komme i gang.

## Illustreret guide

Vil du have det store overblik over, hvad vi vil gennemgå, inden vi dykker ned? Se denne illustrerede guide, der beskriver læringsrejsen for denne lektion – fra at lære kernebegreberne og motivationen for finjustering til at forstå processen og bedste praksis for udførelse af finjusteringsopgaven. Dette er et fascinerende emne at udforske, så glem ikke at tjekke siden [Ressourcer](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) for yderligere links til at støtte din selvstyrede læringsrejse!

![Illustreret guide til finjustering af sprogmodeller](../../../translated_images/da/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Hvad er finjustering for sprogmodeller?

Ifølge definitionen er store sprogmodeller _fortrænet_ på store mængder tekst hentet fra forskellige kilder, inklusive internettet. Som vi har lært i tidligere lektioner, har vi brug for teknikker som _prompt engineering_ og _retrieval-augmented generation_ for at forbedre kvaliteten af modellens svar på brugerens spørgsmål ("prompter").

En populær prompt-engineering-teknik indebærer at give modellen mere vejledning om, hvad der forventes i svaret, enten ved at give _instruktioner_ (eksplicit vejledning) eller _give nogle eksempler_ (implicit vejledning). Dette kaldes _few-shot learning_, men det har to begrænsninger:

- Modellens token-grænser kan begrænse antallet af eksempler, du kan give, og dermed begrænse effektiviteten.
- Omkostningerne ved modeltokens kan gøre det dyrt at tilføje eksempler til hver prompt og begrænse fleksibilitet.

Finjustering er en almindelig praksis i maskinlæringssystemer, hvor vi tager en fortrænet model og genuddanner den med nye data for at forbedre dens ydeevne på en specifik opgave. I sammenhæng med sprogmodeller kan vi finjustere den fortrænede model _med et kurateret sæt eksempler for en given opgave eller applikationsdomæne_ for at skabe en **tilpasset model**, der kan være mere præcis og relevant for den specifikke opgave eller domæne. En sidegevinst ved finjustering er, at det også kan reducere antallet af eksempler, der kræves for few-shot learning – hvilket mindsker tokenforbrug og relaterede omkostninger.

## Hvornår og hvorfor skal vi finjustere modeller?

I _denne_ sammenhæng, når vi taler om finjustering, refererer vi til **overvåget** finjustering, hvor genuddannelsen sker ved at **tilføje nye data**, som ikke var en del af det oprindelige træningsdatasæt. Dette adskiller sig fra en ikke-overvåget finjusteringsmetode, hvor modellen genuddannes på de oprindelige data, men med forskellige hyperparametre.

Det vigtigste at huske er, at finjustering er en avanceret teknik, der kræver et vist ekspertiseniveau for at opnå de ønskede resultater. Hvis det gøres forkert, kan det undlade at give de forventede forbedringer og endda forringe modellens ydeevne for dit målrettede domæne.

Så inden du lærer "hvordan" man finjusterer sprogmodeller, skal du vide "hvorfor" du bør vælge denne vej og "hvornår" du skal starte processen med finjustering. Start med at stille dig selv disse spørgsmål:

- **Brugssag**: Hvad er din _brugssag_ for finjustering? Hvilket aspekt af den nuværende fortrænede model ønsker du at forbedre?
- **Alternativer**: Har du prøvet _andre teknikker_ for at opnå de ønskede resultater? Brug dem til at skabe en baseline for sammenligning.
  - Prompt engineering: Prøv teknikker som few-shot prompting med eksempler på relevante prompt-svar. Evaluer kvaliteten af svarene.
  - Retrieval Augmented Generation: Prøv at forstærke prompter med søgeresultater hentet fra dine data. Evaluer kvaliteten af svarene.
- **Omkostninger**: Har du identificeret omkostningerne ved finjustering?
  - Justerbarhed - er den fortrænede model tilgængelig for finjustering?
  - Arbejdsindsats - for at forberede træningsdata, evaluere og forfine modellen.
  - Beregning - for at køre finjusteringsjobs og implementere den finjusterede model.
  - Data - adgang til tilstrækkeligt kvalitetsmateriale til finjusteringens effekt.
- **Fordele**: Har du bekræftet fordelene ved finjustering?
  - Kvalitet - overgik den finjusterede model baseline?
  - Omkostninger - reducerer den tokenforbrug ved at forenkle prompter?
  - Udvidelsesmuligheder - kan du genbruge basismodellen til nye domæner?

Ved at besvare disse spørgsmål bør du kunne afgøre, om finjustering er den rigtige tilgang for din brugssag. Ideelt set er tilgangen kun gyldig, hvis fordelene opvejer omkostningerne. Når du beslutter dig for at fortsætte, er det tid til at tænke over _hvordan_ du kan finjustere den fortrænede model.

Vil du have flere indsigter i beslutningsprocessen? Se [At finjustere eller ikke finjustere](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hvordan kan vi finjustere en fortrænet model?

For at finjustere en fortrænet model skal du have:

- en fortrænet model til at finjustere
- et datasæt til brug for finjustering
- et træningsmiljø til at køre finjusteringsjobbet
- et hostingmiljø til at implementere den finjusterede model

## Finjustering på Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) er stedet, hvor du i dag finjusterer, implementerer og administrerer tilpassede modeller på Azure (det samler, hvad der tidligere var Azure OpenAI Studio og Azure AI Studio). Inden du starter et job, hjælper det at forstå de valgmuligheder, Foundry giver dig – samt de bedste praksisser platformen anbefaler. Under motorhjelmen bruger Foundry **LoRA (low-rank adaptation)** til at finjustere modeller effektivt, hvilket holder træningen hurtigere og mere overkommelig end at genuddanne hver vægt.

### Trin 1: Vælg en træningsteknik

Foundry understøtter tre finjusteringsteknikker. **Start med SFT** – det dækker det bredeste spektrum af scenarier.

| Teknik | Hvad den gør | Hvornår den skal bruges |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Træner på input/output eksempelpar, så modellen lærer at producere de ønskede svar. | Standard for de fleste opgaver: domænespecialisering, opgavepræstation, stil og tone, instruktionefterlevelse og sprogtilpasning. |
| **Direct Preference Optimization (DPO)** | Lærer fra _foretrukne vs. ikke-foretrukne_ svarpar for at tilpasse output til menneskelige præferencer. | Forbedring af responskvalitet, sikkerhed og tilpasning, når du har sammenlignende feedback. |
| **Reinforcement Fine-Tuning (RFT)** | Bruger belønningssignaler fra _bedømmere_ til at optimere komplekse adfærdsmønstre med forstærkningslæring. | Objektive, ræsonneringstunge domæner (matematik, kemi, fysik) med klare rigtige/forkerte svar. Kræver mere ML-ekspertise. |

### Trin 2: Vælg en træningskategori

Foundry lader dig vælge, hvordan og hvor træningen kører:

- **Standard** – træner i din ressources region og garanterer dataresidens. Brug det når data skal blive i en specifik region.
- **Global** – billigere og hurtigere at sætte i kø ved at bruge kapacitet uden for din region (data og vægte kopieres til træningsregionen). En god standardløsning, når dataresidens ikke er et krav.
- **Developer** – laveste omkostning, bruger ledig kapacitet uden latens-/SLA-garantier (job kan afbrydes og genoptages). Ideel til eksperimenter.

### Trin 3: Vælg en basismodel

Finjusterbare modeller omfatter OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` og `gpt-4.1-nano` (SFT; 4o/4.1-familien understøtter også DPO), ræsonneringsmodellerne `o4-mini` og `gpt-5` (RFT), plus open source-modeller som `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` og `gpt-oss-20b` (SFT på Foundry-ressourcer). Tjek altid den aktuelle [Liste over finjusteringsmodeller](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) for understøttede metoder, regioner og tilgængelighed.

> Foundry tilbyder to modaliteter: **serverless** (forbrugsbaseret prissætning, ingen GPU-kvoter at administrere, OpenAI og udvalgte modeller) og **managed compute** (bring-your-own VMs via Azure Machine Learning for det bredeste modeludvalg). De fleste bør starte med serverless.

### Foundry bedste praksisser

- **Baseline først.** Mål basismodellen med prompt engineering og RAG _før_ du finjusterer, så du kan bevise gevinst.
- **Start småt, og skaler derfra.** Begynd med 50-100 høj-kvalitets eksempler for at validere tilgangen, og udvid så til 500+ til produktion. Kvalitet slår kvantitet – fjern lavkvalitetseksempler.
- **Formatér data korrekt.** Trænings- og valideringsfiler skal være JSONL, UTF-8 **med en BOM**, under 512 MB, og bruge chat-completions beskedformatet. Inkluder altid en valideringsfil for at kunne overvåge overtilpasning.
- **Behold træningssystemprompten ved inferens.** Brug samme systembesked når du kalder modellen, som du brugte under træningen.
- **Evaluer checkpoints – deploy ikke blindt den sidste.** Foundry beholder de sidste tre epoker som deployerbare checkpoints; vælg den, der generaliserer bedst ved at overvåge `train_loss` / `valid_loss` og token-nøjagtighed.
- **Mål tokenomkostninger samtidig med kvalitet** når du sammenligner den finjusterede model med baseline.
- **Iterer med kontinuerlig finjustering.** Du kan finjustere en allerede finjusteret model på nye data (understøttes for OpenAI-modeller).
- **Pas på hosting-omkostninger.** En implementeret tilpasset model faktureres per time, og et inaktivt deployment fjernes efter 15 dage – ryd op i hvad du ikke har brug for.

Gennemgå den komplette gennemgang i [Tilpas en model med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), og se vejledningerne for [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) og [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) når du er klar til de andre teknikker.

## Finjustering i praksis

Følgende ressourcer tilbyder trin-for-trin vejledninger, der guider dig gennem et reelt eksempel på en aktuelt understøttet model med et kurateret datasæt. For at arbejde med dem, har du brug for en konto hos den specifikke udbyder samt adgang til den relevante model og datasæt.

| Udbyder     | Vejledning                                                                                                                                                                 | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hvordan man finjusterer chatmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)    | Lær at finjustere en nyere OpenAI chatmodel til et specifikt domæne ("opskriftassistent") ved at forberede træningsdata, køre finjusteringsjobbet og bruge den finjusterede model til inferens.                                                                                                                                                                                                                            |
| Microsoft Foundry | [Tilpas en model med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                           | Lær at finjustere en aktuelt understøttet model som `gpt-4.1-mini` **på Azure** med Microsoft Foundry: forbered og upload trænings- og valideringsdata, kør finjusteringsjobbet, og implementer derefter den nye model.                                                                                                                                                                                                     |

| Hugging Face | [Finjustering af LLM'er med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dette blogindlæg vejleder dig i finjustering af en _åben LLM_ (f.eks.: `CodeLlama 7B`) ved hjælp af [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst)-biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med åbne [datasæt](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finjustering af LLM'er med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) er et Python-bibliotek udviklet af Hugging Face, som muliggør finjustering til mange forskellige opgaver, inklusive LLM-finjustering. AutoTrain er en no-code løsning, og finjustering kan udføres i din egen cloud, på Hugging Face Spaces eller lokalt. Det understøtter både en webbaseret GUI, CLI og træning via yaml-konfigurationsfiler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finjustering af LLM'er med Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth er et open-source-rammeværk, der understøtter LLM-finjustering og forstærkningslæring (RL). Unsloth gør lokal træning, evaluering og implementering nemmere med færdige [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Det understøtter også tekst-til-tale (TTS), BERT og multimodale modeller. For at komme i gang, læs deres trin-for-trin [Finjustering af LLM'er Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Opgave

Vælg en af ovenstående vejledninger og gennemgå den. _Vi kan måske genskabe en version af disse vejledninger i Jupyter Notebooks i dette repo som reference. Brug venligst de originale kilder direkte for at få de nyeste versioner_.

## Godt arbejde! Fortsæt din læring.

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at forbedre din viden om Generativ AI!

Tillykke!! Du har gennemført den sidste lektion fra v2-serien for dette kursus! Stop ikke med at lære og bygge videre. \*\*Tjek [RESSOURCERNE](RESOURCES.md?WT.mc_id=academic-105485-koreyst)-siden for en liste over yderligere forslag netop til dette emne.

Vores v1-serie af lektioner er også blevet opdateret med flere opgaver og koncepter. Så tag et øjeblik til at friske din viden op – og del gerne [dine spørgsmål og feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) for at hjælpe os med at forbedre disse lektioner for fællesskabet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->