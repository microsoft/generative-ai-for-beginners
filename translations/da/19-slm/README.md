# Introduktion til Små Sprogmodeller for Generativ AI for Begyndere
Generativ AI er et fascinerende område inden for kunstig intelligens, der fokuserer på at skabe systemer, som er i stand til at generere nyt indhold. Dette indhold kan spænde fra tekst og billeder til musik og endda komplette virtuelle miljøer. En af de mest spændende anvendelser af generativ AI er inden for sprogmodeller.

## Hvad er Små Sprogmodeller?

En Lille Sprogmodel (SLM) er en nedskaleret udgave af en stor sprogmodel (LLM), som anvender mange af de arkitektoniske principper og teknikker fra LLM'er, men med et betydeligt reduceret beregningsaftryk.

SLM'er er en undergruppe af sprogmodeller designet til at generere menneskelignende tekst. I modsætning til deres større modstykker, som GPT-4, er SLM'er mere kompakte og effektive, hvilket gør dem ideelle til anvendelser, hvor computressourcer er begrænsede. På trods af deres mindre størrelse kan de stadig udføre en række opgaver. Typisk konstrueres SLM'er ved at komprimere eller destillere LLM'er med det formål at bevare en væsentlig del af den oprindelige models funktionalitet og sproglige evner. Denne reduktion i modelstørrelse mindsker den samlede kompleksitet og gør SLM'er mere effektive både med hensyn til hukommelsesforbrug og beregningsbehov. På trods af disse optimeringer kan SLM'er stadig udføre en bred vifte af opgaver inden for naturlig sprogbehandling (NLP):

- Tekstgenerering: At skabe sammenhængende og kontekstuelt relevante sætninger eller afsnit.
- Tekstkomplettering: At forudsige og fuldføre sætninger baseret på et givet prompt.
- Oversættelse: At omdanne tekst fra et sprog til et andet.
- Opsummering: At kondensere lange tekststykker til kortere og mere fordøjelige resuméer.

Dog med nogle kompromiser i ydelse eller dybden af forståelsen sammenlignet med deres større modstykker.

## Hvordan Fungerer Små Sprogmodeller?
SLM'er trænes på store mængder tekstdata. Under træningen lærer de sprogets mønstre og strukturer, hvilket gør dem i stand til at generere tekst, der både er grammatisk korrekt og kontekstuelt passende. Træningsprocessen involverer:

- Dataindsamling: Indsamling af store datasæt af tekst fra forskellige kilder.
- Forbehandling: Rensning og organisering af dataene for at gøre dem egnede til træning.
- Træning: Brug af maskinlæringsalgoritmer til at lære modellen at forstå og generere tekst.
- Finjustering: Justering af modellen for at forbedre dens præstation på specifikke opgaver.

Udviklingen af SLM'er svarer til den stigende efterspørgsel efter modeller, der kan implementeres i ressourcebegrænsede miljøer, såsom mobile enheder eller edge computing-platforme, hvor fuldskala LLM'er kan være upraktiske på grund af deres store ressourcetræk. Ved at fokusere på effektivitet balancerer SLM'er ydelse med tilgængelighed, hvilket muliggør bredere anvendelse på tværs af forskellige domæner.

![slm](../../../translated_images/da/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Læringsmål

I denne lektion håber vi at introducere viden om SLM og kombinere den med Microsoft Phi-3 for at lære om forskellige scenarier inden for tekstindhold, vision og MoE.

Ved slutningen af denne lektion bør du kunne besvare følgende spørgsmål:

- Hvad er SLM?
- Hvad er forskellen mellem SLM og LLM?
- Hvad er Microsoft Phi-3/3.5-familien?
- Hvordan kører man inferens med Microsoft Phi-3/3.5-familien?

Klar? Lad os komme i gang.

## Forskellene mellem Store Sprogmodeller (LLMs) og Små Sprogmodeller (SLMs)

Både LLM'er og SLM'er bygger på grundlæggende principper fra probabilistisk maskinlæring og følger lignende tilgange i deres arkitektoniske design, træningsmetoder, data-genereringsprocesser og modelvurderingsteknikker. Dog er flere centrale faktorer med til at differentiere disse to typer modeller.

## Anvendelser af Små Sprogmodeller

SLM'er har et bredt anvendelsesområde, herunder:

- Chatbots: Til kundesupport og brugerinteraktion i en konverserende stil.
- Indholdsskabelse: Assistere forfattere ved at generere idéer eller endda udkast til hele artikler.
- Uddannelse: Hjælpe elever med skriveopgaver eller at lære nye sprog.
- Tilgængelighed: Skabe værktøjer til personer med handicap, såsom tekst-til-tale systemer.

**Størrelse**
  
En primær forskel mellem LLM'er og SLM'er ligger i modellernes skala. LLM'er, såsom ChatGPT (GPT-4), kan omfatte estimeret 1,76 billioner parametre, mens open source SLM'er som Mistral 7B er designet med betydeligt færre parametre—omkring 7 milliarder. Denne forskel skyldes primært forskelle i modelarkitektur og træningsprocesser. For eksempel anvender ChatGPT en selv-opmærksomhedsmekanisme inden for en encoder-decoder-ramme, mens Mistral 7B bruger glidende vinduesopmærksomhed, som muliggør mere effektiv træning i en decodermodel. Denne arkitektoniske variation har dybtgående konsekvenser for modellernes kompleksitet og ydelse.

**Forståelse**

SLM'er er typisk optimeret til ydeevne inden for specifikke domæner, hvilket gør dem meget specialiserede, men potentielt begrænsede i deres evne til at give bred kontekstforståelse på tværs af flere vidensfelter. I kontrast tilstræber LLM'er at simulere menneskelig intelligens på et mere omfattende niveau. Trænet på store, varierede datasæt er LLM'er designet til at klare sig godt på tværs af en række domæner og tilbyder større alsidighed og tilpasningsevne. Derfor er LLM'er mere velegnede til et bredere spektrum af efterfølgende opgaver, såsom naturlig sprogbehandling og programmering.

**Beregning**

Træning og implementering af LLM'er er ressourcekrævende processer, ofte med behov for betydelig beregningsinfrastruktur, herunder store GPU-klynger. For eksempel kan træning af en model som ChatGPT fra bunden kræve tusindvis af GPU'er over længere perioder. I modsætning hertil er SLM'er, med deres mindre antal parametre, mere tilgængelige i forhold til computressourcer. Modeller som Mistral 7B kan trænes og køres på lokale maskiner udstyret med moderate GPU-kapaciteter, selvom træning stadig kræver flere timer på tværs af flere GPU'er.

**Bias**

Bias er et kendt problem i LLM'er, primært på grund af træningsdataenes karakter. Disse modeller baserer sig ofte på rå, frit tilgængelige internetdata, som kan underrepresentere eller fejlagtigt fremstille visse grupper, introducere fejlagtig mærkning eller afspejle sproglige bias påvirket af dialekt, geografiske variationer og grammatiske regler. Derudover kan kompleksiteten i LLM-arkitekturer utilsigtet forværre bias, som måske går ubemærket hen uden omhyggelig finjustering. På den anden side, da SLM'er trænes på mere begrænsede, domænespecifikke datasæt, er de naturligt mindre modtagelige over for sådanne biases, selvom de ikke er immune.

**Inferens**

Den reducerede størrelse af SLM'er giver dem en betydelig fordel med hensyn til inferenshastighed, hvilket gør dem i stand til effektivt at generere output på lokal hardware uden behov for omfattende parallel behandling. LLM'er kræver derimod på grund af deres størrelse og kompleksitet ofte betydelige parallelle beregningsressourcer for at opnå acceptable inferenstider. Flere samtidige brugere kan desuden sænke LLM'ers svartider, især ved implementering i stor skala.

Sammenfattende, mens både LLM'er og SLM'er deler et fælles grundlag i maskinlæring, adskiller de sig markant med hensyn til modelstørrelse, ressourcebehov, kontekstuel forståelse, modtagelighed for bias og inferenshastighed. Disse forskelle afspejler deres respektive egnethed for forskellige anvendelser, hvor LLM'er er mere alsidige, men ressourcekrævende, mens SLM'er tilbyder domænespecifik effektivitet med reduceret beregningsbehov.

***Bemærk: I denne lektion vil vi introducere SLM ved brug af Microsoft Phi-3 / 3.5 som eksempel.***

## Introduktion til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien fokuserer primært på tekst, vision og Agent (MoE)-anvendelsesscenarier:

### Phi-3 / 3.5 Instruct

Hovedsageligt til tekstgenerering, chatkomplettering og udtrækning af indholdsinformation osv.

**Phi-3-mini**

Den 3,8 mia. parametre store sprogmodel er tilgængelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modeller overgår betydeligt sprogmodeller af samme og større størrelser på nøglebenchmarks (se benchmarktal nedenfor; højere tal er bedre). Phi-3-mini overgår modeller, der er dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med blot 7 mia. parametre slår Phi-3-small GPT-3.5T på en række benchmarks for sprog, ræsonnering, kodning og matematik.

Phi-3-medium med 14 mia. parametre fortsætter denne trend og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan betragte den som en opgradering af Phi-3-mini. Selvom antallet af parametre er uændret, forbedrer den evnen til at understøtte flere sprog (understøtter 20+ sprog: arabisk, kinesisk, tjekkisk, dansk, hollandsk, engelsk, finsk, fransk, tysk, hebraisk, ungarsk, italiensk, japansk, koreansk, norsk, polsk, portugisisk, russisk, spansk, svensk, thai, tyrkisk, ukrainsk) og tilføjer stærkere støtte til lange kontekster.

Phi-3.5-mini med 3,8 mia. parametre overgår sprogmodeller af samme størrelse og er på niveau med modeller, der er dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan tænke på Instruct-modellen af Phi-3/3.5 som Phis evne til at forstå, og Vision er, hvad der giver Phi øjne til at forstå verden.


**Phi-3-Vision**

Phi-3-vision med kun 4,2 mia. parametre fortsætter denne tendens og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle ræsonnementopgaver, OCR samt tabel- og diagramforståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en opgradering af Phi-3-Vision, der tilføjer understøttelse af flere billeder. Du kan tænke på det som en forbedring i synssansen: ikke kun kan du se billeder, men også videoer.

Phi-3.5-vision overgår større modeller såsom Claude-3.5 Sonnet og Gemini 1.5 Flash inden for OCR, tabel- og diagramforståelsesopgaver og er på niveau på generelle opgaver med visuel viden og ræsonnering. Understøtter input med flere frames, dvs. ræsonnering på flere indgangsbilleder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** muliggør, at modeller kan foruddannes med langt mindre beregningskraft, hvilket betyder, at man dramatisk kan skalere model- eller datasætstørrelsen med samme beregningsbudget som en tæt model. Især bør en MoE-model opnå samme kvalitet som sin tætte modpart meget hurtigere under foruddannelse.

Phi-3.5-MoE består af 16x3,8 mia. ekspertmoduler. Phi-3.5-MoE med kun 6,6 mia. aktive parametre opnår et tilsvarende niveau af ræsonnering, sprogforståelse og matematik som meget større modeller.

Vi kan bruge Phi-3/3.5-familie-modellen baseret på forskellige scenarier. I modsætning til LLM kan du implementere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheder.


## Sådan bruger du Phi-3/3.5-familiemodeller

Vi håber at kunne bruge Phi-3/3.5 i forskellige scenarier. Næste trin vil være at bruge Phi-3/3.5 baseret på forskellige scenarier.

![phi3](../../../translated_images/da/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via Cloud APIs

**Microsoft Foundry-modeller**

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatning.

Microsoft Foundry Models er den mest direkte måde. Du kan hurtigt få adgang til Phi-3/3.5-Instruct-modellen gennem Foundry-modelkataloget. Sammen med Azure AI Inference SDK / OpenAI SDK kan du tilgå API'en via kode for at udføre Phi-3/3.5-Instruct-opkald. Du kan også teste forskellige effekter gennem Playground.

- Demo: Sammenligning af effekterne af Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/da/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/da/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Eller hvis vi ønsker at bruge vision- og MoE-modellerne, kan du bruge Microsoft Foundry til at gennemføre opkaldet. Hvis du er interesseret, kan du læse Phi-3 Cookbook for at lære, hvordan man kalder Phi-3/3.5 Instruct, Vision, MoE gennem Microsoft Foundry [Klik på dette link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ud over det cloud-baserede Microsoft Foundry Models-katalog kan du også bruge [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) til at udføre relaterede opkald. Du kan besøge NVIDIA NIM for at gennemføre API-opkald for Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sæt accelererede inferens-mikrotjenester designet til at hjælpe udviklere med effektivt at implementere AI-modeller på tværs af forskellige miljøer, herunder cloud, datacentre og arbejdsstationer.

Her er nogle nøglefunktioner ved NVIDIA NIM:

- **Nem implementering:** NIM tillader implementering af AI-modeller med en enkelt kommando, hvilket gør det let at integrere i eksisterende arbejdsgange.
- **Optimeret ydeevne:** Det udnytter NVIDIA’s for-optimere inferensmotorer, såsom TensorRT og TensorRT-LLM, for at sikre lav latenstid og høj gennemstrømning.
- **Skalerbarhed:** NIM understøtter autoskalering på Kubernetes, hvilket gør det i stand til effektivt at håndtere varierende arbejdsbelastninger.
- **Sikkerhed og kontrol:** Organisationer kan bevare kontrollen over deres data og applikationer ved selv at hoste NIM-mikrotjenester på deres egen styrede infrastruktur.
- **Standard-API'er:** NIM leverer branchestandard-API'er, hvilket gør det nemt at opbygge og integrere AI-applikationer som chatbots, AI-assistenter og mere.

NIM er en del af NVIDIA AI Enterprise, som har til formål at forenkle implementering og drift af AI-modeller, så de kører effektivt på NVIDIA GPU'er.

- Demo: Brug af NVIDIA NIM til at kalde Phi-3.5-Vision-API  [[Klik på dette link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kørsel af Phi-3/3.5 Lokalt
Inference i forhold til Phi-3, eller enhver sprogmodel som GPT-3, refererer til processen med at generere svar eller forudsigelser baseret på den input, den modtager. Når du giver et prompt eller spørgsmål til Phi-3, bruger den sit trænede neurale netværk til at slutte sig til det mest sandsynlige og relevante svar ved at analysere mønstre og relationer i de data, den er trænet på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftfuldt bibliotek designet til naturlig sprogbehandling (NLP) og andre maskinlæringsopgaver. Her er nogle nøglepunkter om det:

1. **Foruddannede modeller**: Det tilbyder tusindvis af foruddannede modeller, der kan bruges til forskellige opgaver som tekstklassifikation, navngiven entitetsgenkendelse, spørgsmål og svar, opsummering, oversættelse og tekstgenerering.

2. **Framework-interoperabilitet**: Biblioteket understøtter flere dybdelæringsrammer, herunder PyTorch, TensorFlow og JAX. Dette giver dig mulighed for at træne en model i én ramme og bruge den i en anden.

3. **Multimodale kapaciteter**: Ud over NLP understøtter Hugging Face Transformers også opgaver inden for computer vision (f.eks. billedklassifikation, objektdetektion) og lydbehandling (f.eks. talegenkendelse, lydklassifikation).

4. **Brugervenlighed**: Biblioteket tilbyder API'er og værktøjer til nemt at downloade og finjustere modeller, hvilket gør det tilgængeligt for både begyndere og eksperter.

5. **Fællesskab og ressourcer**: Hugging Face har et levende fællesskab og omfattende dokumentation, tutorials og vejledninger til at hjælpe brugere i gang og få mest muligt ud af biblioteket.
[officiel dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest almindeligt anvendte metode, men den kræver også GPU-acceleration. Scenarier såsom Vision og MoE kræver trods alt mange beregninger, som vil være meget langsomme på CPU, hvis de ikke er kvantificerede.


- Demo: Brug af Transformer til at kalde Phi-3.5-Instruct [Klik på dette link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-Vision [Klik på dette link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-MoE [Klik på dette link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en platform designet til at gøre det lettere at køre store sprogmodeller (LLM'er) lokalt på din maskine. Den understøtter forskellige modeller som Llama 3.1, Phi 3, Mistral og Gemma 2 blandt andre. Platformen forenkler processen ved at samle modelvægte, konfiguration og data i én pakke, hvilket gør det mere tilgængeligt for brugere at tilpasse og skabe egne modeller. Ollama er tilgængelig for macOS, Linux og Windows. Det er et fantastisk værktøj, hvis du ønsker at eksperimentere med eller implementere LLM'er uden at være afhængig af cloud-tjenester. Ollama er den mest direkte måde, du skal blot udføre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline on-device runtime til at køre modeller som Phi fuldstændigt på din egen hardware - ingen Azure-abonnement, API-nøgle eller netværksforbindelse nødvendig. Den vælger automatisk den bedste eksekveringsudbyder tilgængelig (NPU, GPU eller CPU) og eksponerer en OpenAI-kompatibel endpoint, så eksisterende `openai`/Azure AI Inference SDK-kode kan pege på den med minimale ændringer. Se [Foundry Local dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Eller brug SDK'en direkte i Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en platformuafhængig inferens- og træningsaccelerator til maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftfuldt værktøj, der hjælper dig med at køre generative AI-modeller effektivt på tværs af forskellige platforme.

## Hvad er ONNX Runtime?
ONNX Runtime er et open source-projekt, der muliggør højtydende inferens af maskinlæringsmodeller. Den understøtter modeller i Open Neural Network Exchange (ONNX)-format, som er en standard for repræsentation af maskinlæringsmodeller. ONNX Runtime inferens kan give hurtigere kundeoplevelser og lavere omkostninger ved at understøtte modeller fra dybdelæringsframeworks som PyTorch og TensorFlow/Keras samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost osv. ONNX Runtime er kompatibel med forskellig hardware, drivere og operativsystemer, og leverer optimal ydeevne ved at udnytte hardwareacceleratorer, hvor det er relevant, sammen med grafoptimeringer og transformationer.

## Hvad er Generativ AI?
Generativ AI refererer til AI-systemer, der kan generere nyt indhold, såsom tekst, billeder eller musik, baseret på de data, de er trænet på. Eksempler inkluderer sprogmodeller som GPT-3 og billedgenereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket leverer den generative AI-løkke for ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, søgning og sampling samt KV-cache-håndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI udvider funktionerne i ONNX Runtime til at understøtte generative AI-modeller. Her er nogle nøglefunktioner:

- **Bred platformunderstøttelse:** Den fungerer på forskellige platforme, herunder Windows, Linux, macOS, Android og iOS.
- **Modelunderstøttelse:** Den understøtter mange populære generative AI-modeller, som LLaMA, GPT-Neo, BLOOM og flere.
- **Ydelsesoptimering:** Den inkluderer optimeringer til forskellige hardwareacceleratorer som NVIDIA GPU'er, AMD GPU'er og mere2.
- **Brugervenlighed:** Den tilbyder API'er til nem integration i applikationer, hvilket gør det muligt at generere tekst, billeder og andet indhold med minimal kode
- Brugere kan kalde en højniveau generate()-metode eller køre hver iteration af modellen i en løkke, generere ét token ad gangen og valgfrit opdatere genereringsparametre inde i løkken.
- ONNX runtime har også støtte for greedy/beam-søgning og TopP, TopK sampling for at generere tokensekvenser og indbygget logitsbehandling som repetitionsstraffe. Du kan også nemt tilføje egen scoring.

## Kom godt i gang
For at komme i gang med ONNX Runtime for GENAI kan du følge disse trin:

### Installer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installer Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Kør en model: Her er et simpelt eksempel i Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Brug ONNX Runtime GenAI til at kalde Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Andre**

Ud over ONNX Runtime, Ollama og Foundry Local reference-metoder kan vi også fuldføre referencen for kvantitative modeller baseret på modelreferencemetoder leveret af forskellige producenter. Som Apple MLX framework med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også få mere indhold fra [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mere

Vi har lært det grundlæggende om Phi-3/3.5-familien, men for at lære mere om SLM har vi brug for mere viden. Du kan finde svarene i Phi-3 Cookbook. Hvis du vil lære mere, besøg venligst [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->