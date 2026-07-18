[![Open Source Models](../../../translated_images/no/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Finjustering av din LLM

Bruk av store språkmodeller for å bygge generative AI-applikasjoner kommer med nye utfordringer. Et nøkkelspørsmål er å sikre svarenes kvalitet (nøyaktighet og relevans) i innhold som modellen genererer for en gitt brukerforespørsel. I tidligere leksjoner diskuterte vi teknikker som prompt engineering og henteutvidet generering som prøver å løse problemet ved å _endre prompt-innputten_ til den eksisterende modellen.

I dagens leksjon diskuterer vi en tredje teknikk, **finjustering**, som prøver å ta tak i utfordringen ved å _ettertrene selve modellen_ med ekstra data. La oss dykke inn i detaljene.

## Læringsmål

Denne leksjonen introduserer konseptet finjustering for forhåndstrente språkmodeller, utforsker fordelene og utfordringene ved denne tilnærmingen, og gir veiledning om når og hvordan du kan bruke finjustering for å forbedre ytelsen til dine generative AI-modeller.

Ved slutten av denne leksjonen skal du kunne svare på følgende spørsmål:

- Hva er finjustering for språkmodeller?
- Når, og hvorfor, er finjustering nyttig?
- Hvordan kan jeg finjustere en forhåndstrent modell?
- Hva er begrensningene ved finjustering?

Klar? La oss sette i gang.

## Illustrert guide

Vil du få oversikten over hva vi skal dekke før vi begynner? Sjekk ut denne illustrerte guiden som beskriver læringsreisen for denne leksjonen - fra å lære de grunnleggende konseptene og motivasjonen for finjustering, til å forstå prosessen og beste praksis for å gjennomføre finjusteringsoppgaven. Dette er et spennende tema å utforske, så ikke glem å sjekke [Ressurser](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) siden for flere lenker som støtter din selvstyrte læringsreise!

![Illustrert guide til finjustering av språkmodeller](../../../translated_images/no/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Hva er finjustering for språkmodeller?

Per definisjon er store språkmodeller _forhåndstrent_ på store mengder tekst hentet fra ulike kilder, inkludert internett. Som vi har lært i tidligere leksjoner, trenger vi teknikker som _prompt engineering_ og _henteutvidet generering_ for å forbedre modellens svar på brukerens spørsmål ("prompter").

En populær prompt-engineering teknikk innebærer å gi modellen mer veiledning om hva som forventes i svaret enten ved å gi _instruksjoner_ (eksplicit veiledning) eller _gi den noen eksempler_ (implisitt veiledning). Dette kalles for _few-shot learning_, men det har to begrensninger:

- Modellens token-grenser kan begrense antall eksempler du kan gi, og begrense effektiviteten.
- Kostnader knyttet til modellens tokens kan gjøre det dyrt å legge til eksempler i hver prompt, og begrense fleksibiliteten.

Finjustering er en vanlig praksis i maskinlæringssystemer hvor vi tar en forhåndstrent modell og trener den på nytt med nye data for å forbedre ytelsen på en spesifikk oppgave. I sammenheng med språkmodeller kan vi finjustere den forhåndstrente modellen _med et kuratert sett av eksempler for en bestemt oppgave eller bruksområde_ for å lage en **tilpasset modell** som kan være mer nøyaktig og relevant for nettopp den oppgaven eller domenet. En bieffekt av finjustering er at det også kan redusere antallet nødvendige eksempler for few-shot learning - noe som reduserer token-bruk og relaterte kostnader.

## Når og hvorfor bør vi finjustere modeller?

I _denne_ konteksten, når vi snakker om finjustering, refererer vi til **veiledet** finjustering hvor opplæringen gjøres ved å **legge til nye data** som ikke var en del av det opprinnelige treningsdatasettet. Dette er forskjellig fra en ikke-veiledet finjusteringsmetode hvor modellen trenes på nytt på originaldata, men med forskjellige hyperparametere.

Det viktigste å huske er at finjustering er en avansert teknikk som krever et visst nivå av ekspertise for å oppnå ønskede resultater. Gjøres det feil, kan det hende den ikke gir forventede forbedringer, og kan til og med forringe modellens ytelse for ditt målrettede domene.

Så, før du lærer "hvordan" du finjusterer språkmodeller, må du vite "hvorfor" du bør velge denne veien, og "når" du skal starte finjusteringsprosessen. Begynn med å stille deg selv disse spørsmålene:

- **Bruksområde**: Hva er ditt _bruksområde_ for finjustering? Hvilke aspekter ved den nåværende forhåndstrente modellen ønsker du å forbedre?
- **Alternativer**: Har du prøvd _andre teknikker_ for å oppnå ønskede resultater? Bruk dem til å lage en referanse for sammenligning.
  - Prompt engineering: Prøv teknikker som few-shot prompting med eksempler på relevante svar. Evaluer kvaliteten på svarene.
  - Henteutvidet generering: Prøv å utvide prompter med resultater hentet ved søk i dine data. Evaluer kvaliteten på svarene.
- **Kostnader**: Har du identifisert kostnadene for finjustering?
  - Justerbarhet - er den forhåndstrente modellen tilgjengelig for finjustering?
  - Innsats - for forberedelse av treningsdata, evaluering og raffinering av modellen.
  - Beregningsressurser - for å kjøre finjusteringsjobber og distribuere den finjusterte modellen.
  - Data - tilgang til tilstrekkelig kvalitetseksempler for finjusteringens effekt.
- **Fordeler**: Har du bekreftet fordelene ved finjustering?
  - Kvalitet - overgikk den finjusterte modellen baseline?
  - Kostnad - reduserer den token-bruken ved å forenkle prompter?
  - Utvidbarhet - kan du gjenbruke basismodellen for nye domener?

Ved å besvare disse spørsmålene bør du kunne avgjøre om finjustering er riktig tilnærming for ditt bruksområde. Ideelt sett er tilnærmingen gyldig bare hvis fordelene oppveier kostnadene. Når du bestemmer deg for å gå videre, er det på tide å tenke på _hvordan_ du kan finjustere den forhåndstrente modellen.

Vil du ha flere innsikter i beslutningsprosessen? Se [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hvordan kan vi finjustere en forhåndstrent modell?

For å finjustere en forhåndstrent modell, trenger du:

- en forhåndstrent modell å finjustere
- et datasett til bruk for finjustering
- et treningsmiljø for å kjøre finjusteringsjobben
- et hostingmiljø for å distribuere den finjusterte modellen

## Finjustering på Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) er hvor du i dag finjusterer, distribuerer og administrerer tilpassede modeller på Azure (det samler det som tidligere var Azure OpenAI Studio og Azure AI Studio). Før du starter en jobb, er det nyttig å forstå valgmulighetene Foundry gir deg - og beste praksis plattformen anbefaler. Under panseret bruker Foundry **LoRA (low-rank adaptation)** for å finjustere modeller effektivt, noe som gjør treningen raskere og mer rimelig enn å trene hver vekt på nytt.

### Trinn 1: Velg en treningsteknikk

Foundry støtter tre finjusteringsteknikker. **Start med SFT** - det dekker det bredeste spekteret av scenarioer.

| Teknikk | Hva den gjør | Når den skal brukes |
| --- | --- | --- |
| **Veiledet finjustering (SFT)** | Trener på inn- og ut-eksempelpar slik at modellen lærer å produsere de svarene du ønsker. | Standard for de fleste oppgaver: domene-spesialisering, oppgaveytelse, stil og tone, instruksjonsfølging og språktilpasning. |
| **Direkte preferanseoptimalisering (DPO)** | Lærer fra _foretrukne vs. ikke-foretrukne_ svarpar for å tilpasse utdata til menneskelige preferanser. | Forbedring av svar kvalitet, sikkerhet og samsvar når du har sammenlignende tilbakemeldinger. |
| **Forsterkningsfinjustering (RFT)** | Bruker belønningssignaler fra _vurderere_ for å optimalisere komplekse atferder med forsterkningslæring. | Objektive, resonnementstunge domener (matematikk, kjemi, fysikk) med klare riktige/gale svar. Krever mer ML-kompetanse. |

### Trinn 2: Velg et treningsnivå

Foundry lar deg velge hvordan og hvor treningen kjører:

- **Standard** - trener i ressursens region og garanterer datalokalitet. Bruk dette når data må oppbevares i en spesifikk region.
- **Global** - billigere og raskere å sette i kø ved å bruke kapasitet utenfor din region (data og vekter kopieres til treningsregionen). En god standard når datalokalitet ikke er et krav.
- **Utvikler** - laveste kostnad, bruker ledig kapasitet uten garantert lav ventetid/SLA (jobber kan avbrytes og gjenopptas). Ideell for eksperimentering.

### Trinn 3: Velg en basismodell

Finjusterbare modeller inkluderer OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` og `gpt-4.1-nano` (SFT; 4o/4.1-familien støtter også DPO), resonnementmodellene `o4-mini` og `gpt-5` (RFT), pluss åpen kildekode-modeller som `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, og `gpt-oss-20b` (SFT på Foundry-ressurser). Sjekk alltid den nåværende [listen over finjusteringsmodeller](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) for støttede metoder, regioner, og tilgjengelighet.

> Foundry tilbyr to modaliteter: **serverløs** (forbruksbasert prising, ingen GPU-kvote å administrere, OpenAI og utvalgte modeller) og **administrert compute** (ta med egne VMer via Azure Machine Learning for bredest modellutvalg). De fleste bør starte med serverløs.

### Foundrys beste praksis

- **Start med baseline.** Mål basismodellen med prompt engineering og RAG _før_ du finjusterer, slik at du kan dokumentere gevinsten.
- **Begynn smått, så skaler.** Start med 50-100 høy-kvalitets eksempler for å validere tilnærmingen, så øk til 500+ for produksjon. Kvalitet trumfer kvantitet - stryk lav-kvalitets eksempler.
- **Formater data riktig.** Trenings- og valideringsfiler må være JSONL, UTF-8 **med BOM**, under 512 MB, og bruke chat-kompletterings meldingsformatet. Inkluder alltid en valideringsfil slik at du kan følge med på overtilpasning.
- **Behold systemprompten under inferens.** Bruk samme systemmelding når du kaller modellen som under treningen.
- **Evaluer sjekkpunkter - distribuer ikke blindt det siste.** Foundry beholder de siste tre epokene som deployerbare sjekkpunkter; velg det som generaliserer best ved å følge med på `train_loss` / `valid_loss` og token-nøyaktighet.
- **Mål token-kostnad sammen med kvalitet** når du sammenligner den finjusterte modellen med baseline.
- **Iterer med kontinuerlig finjustering.** Du kan finjustere en allerede finjustert modell på ny data (støttet for OpenAI-modeller).
- **Vær oppmerksom på hosting-kostnader.** En distribuert tilpasset modell faktureres per time, og en inaktiv distribusjon fjernes etter 15 dager - rydd opp det du ikke trenger.

Følg gjennom hele veiledningen i [Tilpass en modell med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), og se veiledningene for [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) og [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) når du er klar for de andre teknikkene.

## Finjustering i praksis

Følgende ressurser gir trinnvise veiledninger som leder deg gjennom et reelt eksempel på en støttet modell med et kuratert datasett. For å jobbe med dem trenger du en konto hos den aktuelle leverandøren, samt tilgang til den relevante modellen og datasettene.

| Leverandør   | Veiledning                                                                                                                                                                    | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hvordan finjustere chatmodeller](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)           | Lær å finjustere en nyere OpenAI chatmodell for et spesifikt domene ("oppskriftsassistent") ved å forberede treningsdata, kjøre finjusteringsjobben, og bruke den finjusterte modellen til inferens.                                                                                                                                                                                                                                 |
| Microsoft Foundry | [Tilpass en modell med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                        | Lær å finjustere en for øyeblikket støttet modell som `gpt-4.1-mini` **på Azure** med Microsoft Foundry: forbered og last opp trenings- og valideringsdata, kjør finjusteringsjobben, og distribuer og bruk den nye modellen.                                                                                                                                                                                                                 |

| Hugging Face | [Finjustering av LLM-er med Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dette blogginnlegget tar deg gjennom finjustering av en _åpen LLM_ (f.eks: `CodeLlama 7B`) ved bruk av [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) biblioteket & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) med åpne [datasett](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) på Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Finjustering av LLM-er med AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (eller AutoTrain Advanced) er et python-bibliotek utviklet av Hugging Face som lar deg finjustere for mange forskjellige oppgaver, inkludert finjustering av LLM-er. AutoTrain er en kodefri løsning, og finjustering kan gjøres i din egen sky, på Hugging Face Spaces eller lokalt. Den støtter både en nettbasert GUI, CLI og trening via yaml-konfigurasjonsfiler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Finjustering av LLM-er med Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth er et åpen kildekode-rammeverk som støtter finjustering av LLM og forsterkende læring (RL). Unsloth effektiviserer lokal trening, evaluering og distribusjon med ferdiglagde [notatbøker](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Den støtter også tekst-til-tale (TTS), BERT og multimodale modeller. For å komme i gang, les deres trinn-for-trinn [Finjustering av LLM-er Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Oppgave

Velg en av opplæringene over og gå gjennom dem. _Vi kan komme til å replikere en versjon av disse opplæringene i Jupyter Notebooks i dette repoet kun som referanse. Vennligst bruk de originale kildene direkte for å få de nyeste versjonene_.

## Flott jobba! Fortsett læringen din.

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å øke kunnskapen din om Generative AI!

Gratulerer!! Du har fullført den siste leksjonen i v2-serien for dette kurset! Ikke slutt å lære og bygge. \*\*Sjekk ut [RESSURSENE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) for en liste over flere forslag for akkurat dette temaet.

Vår v1-serie med leksjoner er også oppdatert med flere oppgaver og konsepter. Så ta et minutt for å friske opp kunnskapen din - og vær så snill å [del dine spørsmål og tilbakemeldinger](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) for å hjelpe oss med å forbedre disse leksjonene for fellesskapet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->