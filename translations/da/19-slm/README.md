# Introduktion til Små Sprogmodeller for Generativ AI for Begyndere
Generativ AI er et fascinerende område inden for kunstig intelligens, der fokuserer på at skabe systemer, der er i stand til at generere nyt indhold. Dette indhold kan spænde fra tekst og billeder til musik og endda hele virtuelle miljøer. En af de mest spændende anvendelser af generativ AI er inden for sproglige modeller.

## Hvad er Små Sprogmodeller?

En Små Sprogmodel (SLM) repræsenterer en nedskaleret variant af en stor sprogmodel (LLM), der udnytter mange af de arkitektoniske principper og teknikker fra LLM'er, samtidig med at den udviser et betydeligt reduceret beregningsmæssigt aftryk.

SLM'er er en undergruppe af sprogmodeller designet til at generere menneskelignende tekst. I modsætning til deres større modstykker, såsom GPT-4, er SLM'er mere kompakte og effektive, hvilket gør dem ideelle til applikationer, hvor computational ressourcer er begrænsede. På trods af deres mindre størrelse kan de stadig udføre en række opgaver. Typisk konstrueres SLM'er ved at komprimere eller destillere LLM'er og sigter mod at bevare en betydelig del af den oprindelige modelfunktionalitet og sproglige kapaciteter. Denne reduktion i modelstørrelse mindsker den samlede kompleksitet, hvilket gør SLM'er mere effektive med hensyn til både hukommelsesbrug og beregningskrav. På trods af disse optimeringer kan SLM'er stadig udføre en bred vifte af opgaver inden for naturlig sprogbehandling (NLP):

- Tekstgenerering: Skabelse af sammenhængende og kontekstuelt relevante sætninger eller afsnit.
- Tekstkomplettering: Forudsigelse og færdiggørelse af sætninger baseret på en given prompt.
- Oversættelse: Konvertering af tekst fra et sprog til et andet.
- Opsummering: Forkortelse af lange tekststykker til kortere, mere fordøjelige resuméer.

Dog med nogle kompromiser i ydeevne eller dybde af forståelse sammenlignet med deres større modstykker.

## Hvordan Fungerer Små Sprogmodeller?
SLM'er trænes på enorme mængder tekstdata. Under træningen lærer de sprogets mønstre og strukturer, hvilket gør dem i stand til at generere tekst, der både er grammatisk korrekt og kontekstuelt passende. Træningsprocessen involverer:

- Dataindsamling: Samling af store datasæt af tekst fra forskellige kilder.
- Forbehandling: Rensning og organisering af dataene for at gøre dem egnede til træning.
- Træning: Brug af maskinlæringsalgoritmer til at lære modellen at forstå og generere tekst.
- Finjustering: Justering af modellen for at forbedre dens ydeevne på specifikke opgaver.

Udviklingen af SLM'er stemmer overens med det voksende behov for modeller, der kan implementeres i ressourcestærke miljøer, såsom mobile enheder eller edge computing-platforme, hvor fuldskala LLM'er kan være upraktiske på grund af deres store ressourcekrav. Ved at fokusere på effektivitet balancerer SLM'er ydeevne med tilgængelighed, hvilket muliggør bredere anvendelse på tværs af forskellige domæner.

![slm](../../../translated_images/da/slm.4058842744d0444a.webp)

## Læringsmål

I denne lektion håber vi at introducere viden om SLM og kombinere det med Microsoft Phi-3 for at lære forskellige scenarier inden for tekstindhold, vision og MoE.

Ved slutningen af denne lektion skal du kunne besvare følgende spørgsmål:

- Hvad er SLM?
- Hvad er forskellen mellem SLM og LLM?
- Hvad er Microsoft Phi-3/3.5-familien?
- Hvordan kører man inference med Microsoft Phi-3/3.5-familien?

Klar? Lad os komme i gang.

## Forskellene mellem Store Sprogmodeller (LLM'er) og Små Sprogmodeller (SLM'er)

Både LLM'er og SLM'er er baseret på grundlæggende principper inden for probabilistisk maskinlæring og følger lignende tilgange i deres arkitektoniske design, træningsmetoder, datagenereringsprocesser og modelvurderingsteknikker. Dog adskiller flere nøglefaktorer disse to typer modeller.

## Anvendelser af Små Sprogmodeller

SLM'er har en bred vifte af anvendelser, herunder:

- Chatbots: Yde kundesupport og engagere sig med brugere på en samtalemæssig måde.
- Indholdsskabelse: Hjælpe forfattere ved at generere ideer eller endda udarbejde hele artikler.
- Uddannelse: Hjælpe studerende med skriveopgaver eller lære nye sprog.
- Tilgængelighed: Skabe værktøjer til personer med handicap, såsom tekst-til-tale-systemer.

**Størrelse**
  
En primær forskel mellem LLM'er og SLM'er ligger i modellernes skala. LLM'er, såsom ChatGPT (GPT-4), kan bestå af anslået 1,76 billioner parametre, mens open source SLM'er som Mistral 7B er designet med betydeligt færre parametre—omtrent 7 milliarder. Denne forskel skyldes primært forskelle i modelarkitektur og træningsprocesser. For eksempel anvender ChatGPT en selv-opmærksomhedsmekanisme inden for en encoder-decoder-ramme, hvorimod Mistral 7B bruger sliding window attention, hvilket muliggør mere effektiv træning inden for en kun-decoder-model. Denne arkitektoniske variation har store konsekvenser for modellernes kompleksitet og ydeevne.

**Forståelse**

SLM'er er typisk optimeret til ydeevne inden for specifikke domæner, hvilket gør dem meget specialiserede, men potentielt begrænsede i deres evne til at give bred kontekstuel forståelse på tværs af flere vidensfelter. Til gengæld sigter LLM'er mod at simulere menneskelignende intelligens på et mere omfattende niveau. Trænet på enorme, diverse datasæt er LLM'er designet til at klare sig godt på tværs af forskellige domæner, hvilket giver større alsidighed og tilpasningsevne. Derfor er LLM'er mere velegnede til et bredere udvalg af nedstrømsopgaver såsom naturlig sprogbehandling og programmering.

**Beregning**

Træning og implementering af LLM'er er ressourcekrævende processer, der ofte kræver betydelig beregningsinfrastruktur, herunder store GPU-klynger. For eksempel kan det at træne en model som ChatGPT fra bunden kræve tusindvis af GPU'er over længere perioder. Derimod er SLM'er, med deres mindre antal parametre, mere tilgængelige med hensyn til beregningsressourcer. Modeller som Mistral 7B kan trænes og køre på lokale maskiner udstyret med moderate GPU-kapaciteter, selvom træning stadig kræver flere timers arbejde på tværs af flere GPU'er.

**Bias**

Bias er et kendt problem i LLM'er, primært på grund af træningsdataenes natur. Disse modeller er ofte afhængige af rå, offentligt tilgængelige data fra internettet, som kan underrepræsentere eller fejlagtigt repræsentere visse grupper, indføre fejlagtig mærkning eller afspejle sproglige bias påvirket af dialekt, geografiske variationer og grammatisk regler. Derudover kan kompleksiteten af LLM-arkitekturer utilsigtet forværre bias, som kan forblive uopdaget uden omhyggelig finjustering. På den anden side er SLM'er, som trænes på mere afgrænsede, domænespecifikke datasæt, naturligt mindre modtagelige for sådanne biases, selvom de ikke er immune over for dem.

**Inference**

Den reducerede størrelse af SLM'er giver dem en betydelig fordel i forhold til inferenshastighed, hvilket gør det muligt for dem effektivt at generere output på lokal hardware uden behov for omfattende parallel behandling. Til sammenligning kræver LLM'er på grund af deres størrelse og kompleksitet ofte betydelige parallelle beregningsressourcer for at opnå acceptable inferenstider. Tilstedeværelsen af flere samtidige brugere nedkøler yderligere LLM'ers svartider, især når de implementeres i stor skala.

Samlet set, mens både LLM'er og SLM'er deler en grundlæggende basis i maskinlæring, adskiller de sig væsentligt i forhold til modelstørrelse, ressourcekrav, kontekstuel forståelse, modtagelighed for bias og inferenshastighed. Disse forskelle afspejler deres respektive egnethed til forskellige anvendelsestilfælde, hvor LLM'er er mere alsidige men ressourcekrævende, og SLM'er tilbyder mere domænespecifik effektivitet med reducerede beregningsmæssige krav.

***Bemærk: I denne lektion vil vi introducere SLM ved hjælp af Microsoft Phi-3 / 3.5 som eksempel.***

## Introduktion til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien henvender sig primært til tekst-, vision- og Agent (MoE)-anvendelsesscenarier:

### Phi-3 / 3.5 Instruct

Primært til tekstgenerering, chatkomplettering og indholdsudtrækning m.m.

**Phi-3-mini**

Den 3,8B sprogmodel er tilgængelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3 modeller overgår betydeligt sprogmodeller af lige eller større størrelse på nøglebenchmarks (se benchmarktallene nedenfor, højere tal er bedre). Phi-3-mini overgår modeller, der er dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med blot 7B parametre slår Phi-3-small GPT-3.5T på en række benchmarks inden for sprog, ræsonnement, kodning og matematik.

Phi-3-medium med 14B parametre fortsætter denne tendens og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan tænke på det som en opgradering af Phi-3-mini. Mens antallet af parametre forbliver uændret, forbedres evnen til at understøtte flere sprog (understøtter 20+ sprog: Arabisk, Kinesisk, Tjekkisk, Dansk, Hollandsk, Engelsk, Finsk, Fransk, Tysk, Hebraisk, Ungarsk, Italiensk, Japansk, Koreansk, Norsk, Polsk, Portugisisk, Russisk, Spansk, Svensk, Thai, Tyrkisk, Ukrainsk) ​​og tilføjer stærkere understøttelse af langt kontekst.

Phi-3.5-mini med 3,8B parametre overgår sprogmodeller af samme størrelse og er på niveau med modeller, der er dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan tænke på Instruct-modellen i Phi-3/3.5 som Phis evne til at forstå, og Vision er det, der giver Phi øjne til at forstå verden.


**Phi-3-Vision**

Phi-3-vision, med kun 4,2B parametre, fortsætter denne tendens og overgår større modeller såsom Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle ræsonnementopgaver, OCR samt tabel- og diagramforståelsesopgaver.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en opgradering af Phi-3-Vision, der tilføjer understøttelse af flere billeder. Du kan tænke på det som en forbedring af vision, hvor du ikke kun kan se billeder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash på OCR-, tabel- og diagramforståelsesopgaver og er på niveau med generelle visuelle vidensræsonnementopgaver. Understøtter multi-frame input, dvs. udføre ræsonnement på flere inputbilleder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gør det muligt for modeller at blive fortrænet med langt mindre beregning, hvilket betyder, at du dramatisk kan skalere op modellen eller datasætstørrelsen med samme beregningsbudget som en dens model. Specifikt bør en MoE-model opnå samme kvalitet som sin tætte modpart meget hurtigere under fortræningen.

Phi-3.5-MoE består af 16x3,8B ekspertmoduler. Phi-3.5-MoE med kun 6,6B aktive parametre opnår et lignende niveau af ræsonnement, sprogforståelse og matematik som meget større modeller.

Vi kan bruge Phi-3/3.5-familie-modellen baseret på forskellige scenarier. I modsætning til LLM kan du implementere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheder.


## Sådan bruger du Phi-3/3.5-familie-modeller

Vi håber at bruge Phi-3/3.5 i forskellige scenarier. Næste vil vi anvende Phi-3/3.5 baseret på forskellige scenarier.

![phi3](../../../translated_images/da/phi3.655208c3186ae381.webp)

### Inferens via Cloud APIs

**Microsoft Foundry Modeller**

> **Bemærk:** GitHub Modeller udfases ved udgangen af juli 2026. [Microsoft Foundry Modeller](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatning.

Microsoft Foundry Modeller er den mest direkte måde. Du kan hurtigt få adgang til Phi-3/3.5-Instruct modellen gennem Foundry modelkataloget. Kombineret med Azure AI Inference SDK / OpenAI SDK kan du via kode tilgå API'en for at fuldføre Phi-3/3.5-Instruct kaldet. Du kan også teste forskellige effekter gennem Playground.

- Demo: Sammenligning af effekterne af Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/da/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/da/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Eller hvis vi ønsker at bruge vision og MoE modeller, kan du bruge Microsoft Foundry til at fuldføre kaldet. Hvis du er interesseret, kan du læse Phi-3 Cookbook for at lære, hvordan man kalder Phi-3/3.5 Instruct, Vision og MoE gennem Microsoft Foundry [Klik på dette link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ud over det cloud-baserede Microsoft Foundry Modelkatalog kan du også bruge [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) til at fuldføre relaterede kald. Du kan besøge NVIDIA NIM for at fuldføre API-kald fra Phi-3/3.5 familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sæt accelererede inferens-mikrotjenester designet til at hjælpe udviklere med effektivt at implementere AI-modeller på tværs af forskellige miljøer, inklusive skyer, datacentre og arbejdsstationer.

Her er nogle nøglefunktioner ved NVIDIA NIM:

- **Nem implementering:** NIM tillader implementering af AI-modeller med en enkelt kommando, hvilket gør det nemt at integrere i eksisterende arbejdsflows.

- **Optimeret ydeevne:** Den udnytter NVIDIAs forudoptimerede inferensmotorer, såsom TensorRT og TensorRT-LLM, for at sikre lav latenstid og høj gennemstrømning.
- **Skalerbarhed:** NIM understøtter autoskalering på Kubernetes, hvilket gør det muligt at håndtere varierende arbejdsbelastninger effektivt.
- **Sikkerhed og kontrol:** Organisationer kan bevare kontrollen over deres data og applikationer ved at selvhoste NIM-mikrotjenester på deres egen administrerede infrastruktur.
- **Standard-API'er:** NIM leverer branche-standardiserede API'er, hvilket gør det nemt at bygge og integrere AI-applikationer som chatbots, AI-assistenter og mere.

NIM er en del af NVIDIA AI Enterprise, som har til formål at forenkle implementering og drift af AI-modeller og sikre, at de kører effektivt på NVIDIA GPU'er.

- Demo: Brug af NVIDIA NIM til at kalde Phi-3.5-Vision-API [[Klik på dette link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kørsel af Phi-3/3.5 lokalt
Inferens i relation til Phi-3, eller ethvert sprogsmodel som GPT-3, henviser til processen med at generere svar eller forudsigelser baseret på den input, den modtager. Når du giver en prompt eller et spørgsmål til Phi-3, bruger den sit trænede neurale netværk til at udlede det mest sandsynlige og relevante svar ved at analysere mønstre og relationer i de data, den er trænet på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftfuldt bibliotek designet til naturlig sprogbehandling (NLP) og andre maskinlæringsopgaver. Her er nogle nøglepunkter om det:

1. **Foruddannede modeller:** Det tilbyder tusindvis af foruddannede modeller, der kan bruges til forskellige opgaver som tekstklassificering, navngiven entitetsgenkendelse, spørgsmålssvar, opsummering, oversættelse og tekstgenerering.

2. **Framework-interoperabilitet:** Biblioteket understøtter flere dybe læringsframeworks, inklusive PyTorch, TensorFlow og JAX. Dette gør det muligt at træne en model i ét framework og bruge den i et andet.

3. **Multimodale kapaciteter:** Ud over NLP understøtter Hugging Face Transformers også opgaver inden for computervision (f.eks. billedklassificering, objektgenkendelse) og lydbehandling (f.eks. talegenkendelse, lydklassificering).

4. **Brugervenlighed:** Biblioteket tilbyder API'er og værktøjer til nemt at downloade og finjustere modeller, hvilket gør det tilgængeligt for både begyndere og eksperter.

5. **Fællesskab og ressourcer:** Hugging Face har et engageret fællesskab og omfattende dokumentation, tutorials og vejledninger, som hjælper brugere med at komme i gang og få mest muligt ud af biblioteket.
[officiel dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest almindeligt anvendte metode, men den kræver også GPU-acceleration. Scenarier som Vision og MoE kræver mange beregninger, hvilket vil være meget langsomt på CPU, hvis de ikke er kvantificeret.


- Demo: Brug af Transformer til at kalde Phi-3.5-Instruct [Klik på dette link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-Vision [Klik på dette link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-MoE [Klik på dette link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en platform designet til at gøre det lettere at køre store sprogmodeller (LLM) lokalt på din maskine. Den understøtter forskellige modeller som Llama 3.1, Phi 3, Mistral og Gemma 2 blandt andre. Platformen forenkler processen ved at samle modelvægte, konfiguration og data i en enkelt pakke, hvilket gør det mere tilgængeligt for brugere at tilpasse og skabe deres egne modeller. Ollama er tilgængelig for macOS, Linux og Windows. Det er et fremragende værktøj, hvis du ønsker at eksperimentere med eller udrulle LLM'er uden at skulle stole på cloud-tjenester. Ollama er den mest direkte måde, du skal blot udføre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, på-enheden runtime til at køre modeller som Phi helt på dit eget hardware – ingen Azure-abonnement, API-nøgle eller netværksforbindelse kræves. Den vælger automatisk den bedste tilgængelige eksekveringsudbyder (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, så eksisterende `openai`/Azure AI Inference SDK-kode kan pege på det med minimale ændringer. Se [Foundry Local dokumentationen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Eller brug SDK’en direkte i Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en platformuafhængig accelerator til inferens og træning af maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftfuldt værktøj, der hjælper dig med at køre generative AI-modeller effektivt på tværs af forskellige platforme.

## Hvad er ONNX Runtime?
ONNX Runtime er et open source-projekt, der muliggør højtydende inferens af maskinlæringsmodeller. Det understøtter modeller i Open Neural Network Exchange (ONNX)-formatet, som er en standard til repræsentation af maskinlæringsmodeller. ONNX Runtime inferens kan muliggøre hurtigere kundeoplevelser og lavere omkostninger ved at understøtte modeller fra dybdelæringsframeworks som PyTorch og TensorFlow/Keras samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost osv. ONNX Runtime er kompatibel med forskelligt hardware, drivere og operativsystemer og giver optimal ydeevne ved at udnytte hardwareacceleratorer, hvor det er relevant, sammen med grafoptimeringer og transformeringer.

## Hvad er Generativ AI?
Generativ AI refererer til AI-systemer, der kan generere nyt indhold, som tekst, billeder eller musik, baseret på de data, de er trænet på. Eksempler inkluderer sprogmodeller som GPT-3 og billedgenereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket leverer den generative AI-loop for ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, søgning og sampling samt KV-cachehåndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI udvider funktionerne i ONNX Runtime til at understøtte generative AI-modeller. Her er nogle nøglefunktioner:

- **Bred platformunderstøttelse:** Det fungerer på forskellige platforme, herunder Windows, Linux, macOS, Android og iOS.
- **Modelunderstøttelse:** Det understøtter mange populære generative AI-modeller, såsom LLaMA, GPT-Neo, BLOOM og flere.
- **Ydelsesoptimering:** Det inkluderer optimeringer til forskellige hardwareacceleratorer som NVIDIA GPU'er, AMD GPU'er og flere.
- **Brugervenlighed:** Det tilbyder API’er til nem integration i applikationer, så du kan generere tekst, billeder og andet indhold med minimal kode.
- Brugere kan kalde en højniveau generate()-metode eller køre hver iteration af modellen i en løkke, generere et token ad gangen og valgfrit opdatere genereringsparametre inde i løkken.
- ONNX Runtime understøtter også greedy/beam search og TopP, TopK sampling til generering af tokensekvenser samt indbygget logitsbehandling som repetitionsstraffe. Du kan også nemt tilføje tilpasset scoring.

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

Ud over ONNX Runtime, Ollama og Foundry Local reference-metoder kan vi også fuldføre referencen for kvantitative modeller baseret på modelreference-metoder leveret af forskellige producenter. Som Apple MLX framework med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også finde mere indhold i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mere

Vi har lært det grundlæggende om Phi-3/3.5-familien, men for at lære mere om SLM har vi brug for mere viden. Du kan finde svarene i Phi-3 Cookbook. Hvis du vil lære mere, besøg venligst [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->