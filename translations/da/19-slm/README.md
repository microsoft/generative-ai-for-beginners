# Introduktion til Små Sprogmodeller for Generativ AI for Begyndere
Generativ AI er et fascinerende område inden for kunstig intelligens, som fokuserer på at skabe systemer, der er i stand til at generere nyt indhold. Dette indhold kan spænde fra tekst og billeder til musik og endda komplette virtuelle miljøer. En af de mest spændende anvendelser af generativ AI er inden for sprogmodeller.

## Hvad er Små Sprogmodeller?

En Lille Sprogmodel (LSM) repræsenterer en nedskaleret variant af en stor sprogmodel (LSM), som udnytter mange af de arkitektoniske principper og teknikker fra store sprogmodeller, samtidig med at den udviser et betydeligt reduceret beregningsmæssigt fodaftryk.

LSM'er er en undergruppe af sprogmodeller designet til at generere menneskelignende tekst. I modsætning til deres større modstykker, såsom GPT-4, er LSM'er mere kompakte og effektive, hvilket gør dem ideelle til anvendelser, hvor beregningsressourcer er begrænsede. På trods af deres mindre størrelse kan de stadig udføre en række opgaver. Typisk konstrueres LSM'er ved at komprimere eller destillere store sprogmodeller med det formål at bevare en væsentlig del af den oprindelige models funktionalitet og sproglige kapaciteter. Denne reduktion i modelstørrelse mindsker den samlede kompleksitet, hvilket gør LSM'er mere effektive både med hensyn til hukommelsesforbrug og beregningskrav. På trods af disse optimeringer kan LSM'er stadig udføre en bred vifte af opgaver inden for naturlig sprogbehandling (NLP):

- Tekstgenerering: At skabe sammenhængende og kontekstuelt relevante sætninger eller afsnit.
- Tekstfuldførelse: At forudsige og fuldføre sætninger baseret på en given prompt.
- Oversættelse: At konvertere tekst fra ét sprog til et andet.
- Opsummering: At kondensere lange tekststykker til kortere, mere fordøjelige resuméer.

Selvom der kan være nogle kompromiser i ydeevne eller forståelsesdybde sammenlignet med deres større modstykker.

## Hvordan Fungerer Små Sprogmodeller?
LSM'er trænes på enorme mængder tekstdata. Under træningen lærer de mønstre og strukturer i sproget, hvilket gør dem i stand til at generere tekst, der både er grammatisk korrekt og kontekstuelt passende. Træningsprocessen involverer:

- Dataindsamling: Indsamling af store datasæt med tekst fra forskellige kilder.
- Forbehandling: Rensning og organisering af dataene for at gøre dem egnede til træning.
- Træning: Brug af maskinlæringsalgoritmer til at lære modellen at forstå og generere tekst.
- Finjustering: Justering af modellen for at forbedre dens ydeevne på specifikke opgaver.

Udviklingen af LSM'er understøttes af det stigende behov for modeller, der kan implementeres i ressourcebegrænsede miljøer såsom mobile enheder eller edge computing-platforme, hvor fuldskala store sprogmodeller kan være upraktiske på grund af deres store ressourcebehov. Ved at fokusere på effektivitet balancerer LSM'er ydeevne med tilgængelighed og muliggør bredere anvendelse på tværs af forskellige domæner.

![slm](../../../translated_images/da/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Læringsmål

I denne lektion håber vi at introducere kendskabet til LSM og kombinere det med Microsoft Phi-3 for at lære forskellige scenarier inden for tekstindhold, vision og MoE.

Ved slutningen af denne lektion bør du kunne besvare følgende spørgsmål:

- Hvad er LSM?
- Hvad er forskellen mellem LSM og LLM?
- Hvad er Microsoft Phi-3/3.5-familien?
- Hvordan kører man inferens med Microsoft Phi-3/3.5-familien?

Klar? Lad os komme i gang.

## Forskellene mellem Store Sprogmodeller (LLMs) og Små Sprogmodeller (SLMs)

Både LLM'er og LSM'er er bygget på grundlæggende principper fra probabilistisk maskinlæring og følger lignende tilgange i deres arkitektoniske design, træningsmetoder, data-genereringsprocesser og modelvurderingsteknikker. Dog adskiller flere nøglefaktorer disse to typer modeller.

## Anvendelser af Små Sprogmodeller

LSM'er har et bredt anvendelsesområde, herunder:

- Chatbots: Tilbyde kundesupport og engagere sig med brugere på en konverserende måde.
- Indholdsskabelse: Assistere skribenter ved at generere idéer eller endda udarbejde hele artikler.
- Uddannelse: Hjælpe studerende med skriveopgaver eller læring af nye sprog.
- Tilgængelighed: Skabe værktøjer for personer med handicaps, såsom tekst-til-tale-systemer.

**Størrelse**
  
En primær forskel mellem LLM'er og LSM'er ligger i modellernes skala. LLM'er, såsom ChatGPT (GPT-4), kan omfatte anslået 1,76 billioner parametre, mens open source LSM'er som Mistral 7B er designet med betydeligt færre parametre—omtrent 7 milliarder. Denne forskel skyldes primært variationer i modelarkitektur og træningsprocesser. For eksempel anvender ChatGPT en selvopmærksomhedsmekanisme inden for en encoder-decoder struktur, mens Mistral 7B bruger sliding window attention, hvilket muliggør mere effektiv træning inden for en ren decoder-model. Denne arkitektoniske variation har dybtgående konsekvenser for modellernes kompleksitet og ydeevne.

**Forståelse**

LSM'er er typisk optimeret til ydeevne inden for specifikke domæner, hvilket gør dem højt specialiserede, men potentielt begrænsede i deres evne til at tilbyde bred kontekstuel forståelse på tværs af mange vidensfelter. Til gengæld sigter LLM'er mod at simulere menneskelignende intelligens på et mere omfattende niveau. Trænet på enorme, forskellige datasæt er LLM'er designet til at klare sig godt inden for en række domæner og tilbyder større alsidighed og tilpasningsevne. Derfor er LLM'er mere velegnede til et bredere udsnit af efterfølgende opgaver som naturlig sprogbehandling og programmering.

**Beregning**

Træning og deployment af LLM'er er ressourceintensive processer, som ofte kræver betydelig beregningsinfrastruktur, herunder store GPU-klynger. For eksempel kan træning af en model som ChatGPT fra bunden kræve tusindvis af GPU'er over længere perioder. Til sammenligning er LSM'er, med deres mindre antal parametre, mere tilgængelige mht. beregningsressourcer. Modeller som Mistral 7B kan trænes og køres på lokale maskiner med moderate GPU-muligheder, selvom træningen stadig kræver flere timer på tværs af flere GPU'er.

**Bias**

Bias er et kendt problem i LLM'er, primært på grund af træningsdataenes natur. Disse modeller anvender ofte rå, åbent tilgængelige data fra internettet, som kan underrepræsentere eller fejlagtigt repræsentere visse grupper, introducere fejlagtig mærkning eller afspejle sproglige biaser påvirket af dialekter, geografiske variationer og grammatiske regler. Derudover kan kompleksiteten i LLM-arkitekturer utilsigtet forværre bias, som kan gå ubemærket hen uden omhyggelig finjustering. På den anden side er LSM'er, som trænes på mere begrænsede, domænespecifikke datasæt, indbygget mindre udsatte for sådanne bias, selvom de ikke er immune.

**Inferens**

Den reducerede størrelse af LSM'er giver dem en betydelig fordel i inferenshastighed, hvilket gør dem i stand til effektivt at generere output på lokal hardware uden behov for omfattende parallel behandling. Til gengæld kræver LLM'er, på grund af deres størrelse og kompleksitet, ofte betydelige parallele beregningsressourcer for at opnå acceptable inferenstider. Tilstedeværelsen af flere samtidige brugere forsinker yderligere LLM'ers svartider, især når de implementeres i stor skala.

Sammenfattende, selvom både LLM'er og LSM'er deler en grundlæggende base i maskinlæring, adskiller de sig markant i forhold til modelstørrelse, ressourcekrav, kontekstuel forståelse, sårbarhed over for bias og inferenshastighed. Disse forskelle afspejler deres respektive egnethed til forskellige anvendelsestilfælde, hvor LLM'er er mere alsidige men ressourcekrævende, og LSM'er tilbyder mere domænespecifik effektivitet med reducerede beregningskrav.

***Bemærk: I denne lektion vil vi introducere LSM med Microsoft Phi-3 / 3.5 som eksempel.***

## Introduktion til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien henvender sig primært til tekst-, vision- og Agent (MoE)-anvendelsesscenarier:

### Phi-3 / 3.5 Instruct

Primært til tekstgenerering, chatfuldførelse og indholdsoplysningsekstraktion osv.

**Phi-3-mini**

Den 3,8 milliarder parametre store sprogmodel findes på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modeller overgår betydeligt sprogmodeller af samme og større størrelser på nøglebenchmarks (se benchmark-tal nedenfor, højere tal er bedre). Phi-3-mini overgår modeller dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inklusive GPT-3.5.

**Phi-3-small & medium**

Med kun 7 milliarder parametre slår Phi-3-small GPT-3.5T på en række benchmarks inden for sprog, ræsonnement, kodning og matematik.

Phi-3-medium med 14 milliarder parametre fortsætter denne tendens og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan betragte det som en opgradering af Phi-3-mini. Selvom antallet af parametre forbliver uændret, forbedres evnen til at understøtte flere sprog (understøtter 20+ sprog: Arabisk, Kinesisk, Tjekkisk, Dansk, Hollandsk, Engelsk, Finsk, Fransk, Tysk, Hebraisk, Ungarsk, Italiensk, Japansk, Koreansk, Norsk, Polsk, Portugisisk, Russisk, Spansk, Svensk, Thai, Tyrkisk, Ukrainsk) og der tilføjes stærkere understøttelse af lange kontekster.

Phi-3.5-mini med 3,8 milliarder parametre overgår sprogmodeller af samme størrelse og er på niveau med modeller dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan tænke på Instruct-modellen af Phi-3/3.5 som Phis evne til at forstå, og Vision er det, der giver Phi øjne til at forstå verden.


**Phi-3-Vision**

Phi-3-vision, med kun 4,2 milliarder parametre, fortsætter denne tendens og overgår større modeller såsom Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle ræsonnementopgaver, OCR samt tabel- og diagramforståelsesopgaver.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en opgradering af Phi-3-Vision, der tilføjer understøttelse for flere billeder. Du kan tænke på det som en forbedring af vision; ikke alene kan du se billeder, men også videoer.

Phi-3.5-vision overgår større modeller såsom Claude-3.5 Sonnet og Gemini 1.5 Flash på tværs af OCR, tabel- og diagramforståelsesopgaver og er på niveau med generel visuel viden og ræsonnementopgaver. Understøtter multi-frame input, dvs. ræsonnerer over flere inputbilleder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** muliggør, at modeller kan fortrænes med langt mindre beregningskraft, hvilket betyder, at du dramatisk kan skalere op model- eller datasætstørrelsen med samme beregningsbudget som en tæt model. Især bør en MoE-model opnå samme kvalitet som sin tætte modpart meget hurtigere under fortræning.

Phi-3.5-MoE består af 16x3,8 milliarder ekspertmoduler. Phi-3.5-MoE med kun 6,6 milliarder aktive parametre opnår et lignende niveau af ræsonnement, sprogforståelse og matematik som langt større modeller.

Vi kan anvende Phi-3/3.5-familie-modellen baseret på forskellige scenarier. I modsætning til LLM kan du implementere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheder.


## Sådan bruger du Phi-3/3.5-familiemodeller

Vi håber at bruge Phi-3/3.5 i forskellige scenarier. Næste vil vi bruge Phi-3/3.5 baseret på forskellige scenarier.

![phi3](../../../translated_images/da/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via Cloud APIs

**Microsoft Foundry-modeller**

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatning.

> **Bemærk:** Hele Phi-3/3.5-familien (Instruct, Vision og MoE-varianter) blev udfaset fra Microsoft Foundry Models-kataloget den 2025-08-30. Brug `Phi-4` (Instruct) eller `Phi-4-mini-instruct` der i stedet — Phi-3/3.5-eksemplerne nedenfor virker stadig via Hugging Face, Ollama, ONNX Runtime og NVIDIA NIM.

Microsoft Foundry Models tilbyder nu Phi-4-efterfølgerne. Brug `Phi-4` eller `Phi-4-mini-instruct` i stedet for de udfasede Phi-3/3.5-modeller, når du følger eksempler på cloud API'er.

- Demo: Sammenligning af effekterne af Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/da/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/da/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Hvis du vil bruge vision (multimodale) modeller i skyen, brug da den nu tilgængelige `Phi-4-multimodal-instruct` gennem Microsoft Foundry i stedet for de udfasede Phi-3/3.5 Vision-modeller; til tekstopgaver brug `Phi-4` eller `Phi-4-mini-instruct`. Phi-3.5 MoE-modellen er blevet udfaset fra Microsoft Foundry, så brug de andre muligheder beskrevet i denne lektion (for eksempel Hugging Face), hvis du vil eksperimentere med den. Hvis du er interesseret, kan du læse Phi Cookbook for at lære, hvordan du kalder Phi-modeller gennem Microsoft Foundry [Klik på dette link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ud over det skybaserede Microsoft Foundry Models-katalog kan du også bruge [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) til at foretage relaterede kald. Du kan besøge NVIDIA NIM for at udføre API-kald for Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sæt accelererede inferensmikrotjenester designet til at hjælpe udviklere med at implementere AI-modeller effektivt på tværs af forskellige miljøer, herunder skyer, datacentre og arbejdsstationer.

Her er nogle nøglefunktioner ved NVIDIA NIM:

- **Nem implementering:** NIM muliggør implementering af AI-modeller med en enkelt kommando, hvilket gør det enkelt at integrere i eksisterende arbejdsgange.
- **Optimeret ydeevne:** Det udnytter NVIDIA’s for- optimerede inferensmotorer, såsom TensorRT og TensorRT-LLM, for at sikre lav ventetid og høj gennemstrømning.
- **Skalerbarhed:** NIM understøtter autoskalering på Kubernetes, hvilket gør det i stand til effektivt at håndtere varierende arbejdsbelastninger.
- **Sikkerhed og kontrol:** Organisationer kan bevare kontrollen over deres data og applikationer ved selv at hoste NIM-mikrotjenester på deres egen administrerede infrastruktur.
- **Standard-API'er:** NIM tilbyder branchestandard-API'er, hvilket gør det let at bygge og integrere AI-applikationer som chatbots, AI-assistenter og mere.

NIM er en del af NVIDIA AI Enterprise, som har til formål at forenkle implementeringen og operationaliseringen af AI-modeller og sikre, at de kører effektivt på NVIDIA GPU'er.

- Demo: Brug af NVIDIA NIM til at kalde Phi-3.5-Vision-API [[Klik på dette link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kørsel af Phi-3/3.5 lokalt
Inferens i relation til Phi-3 eller enhver sprogmodel som GPT-3 henviser til processen med at generere svar eller forudsigelser baseret på den input, den modtager. Når du giver en prompt eller et spørgsmål til Phi-3, bruger den sit trænede neurale netværk til at udlede det mest sandsynlige og relevante svar ved at analysere mønstre og relationer i de data, den er trænet på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftfuldt bibliotek designet til naturlig sprogbehandling (NLP) og andre maskinlæringsopgaver. Her er nogle nøglepunkter om det:

1. **Fortrænede modeller**: Det giver tusindvis af fortrænede modeller, der kan bruges til forskellige opgaver såsom tekstklassificering, navngiven entitetsgenkendelse, spørgsmålssvar, opsummering, oversættelse og tekstgenerering.

2. **Framework-interoperabilitet**: Biblioteket understøtter flere dybdelæringsframeworks, herunder PyTorch, TensorFlow og JAX. Det gør det muligt at træne en model i ét framework og bruge den i et andet.

3. **Multimodale muligheder**: Ud over NLP understøtter Hugging Face Transformers også opgaver inden for computervision (fx billedklassificering, objektdetektion) og lydbehandling (fx talegenkendelse, lydklassificering).

4. **Brugervenlighed**: Biblioteket tilbyder API'er og værktøjer til nemt at downloade og finjustere modeller, hvilket gør det tilgængeligt for både begyndere og eksperter.

5. **Fællesskab og ressourcer**: Hugging Face har et levende fællesskab og omfattende dokumentation, tutorials og guider til at hjælpe brugere i gang og få mest muligt ud af biblioteket.
[officiel dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest almindeligt anvendte metode, men den kræver også GPU-acceleration. Scenarier såsom Vision og MoE kræver mange beregninger, som vil være meget langsomme på CPU, hvis de ikke er kvantificerede.


- Demo: Brug af Transformer til at kalde Phi-3.5-Instruct [Klik på dette link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-Vision [Klik på dette link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-MoE [Klik på dette link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en platform designet til at gøre det lettere at køre store sprogmodeller (LLM'er) lokalt på din maskine. Den understøtter forskellige modeller som Llama 3.1, Phi 3, Mistral og Gemma 2 blandt andre. Platformen forenkler processen ved at samle modelvægte, konfiguration og data i en enkelt pakke, hvilket gør det mere tilgængeligt for brugere at tilpasse og skabe deres egne modeller. Ollama er tilgængelig til macOS, Linux og Windows. Det er et fantastisk værktøj, hvis du ønsker at eksperimentere med eller implementere LLM'er uden at være afhængig af cloud-tjenester. Ollama er den mest direkte måde, du skal blot køre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, on-device runtime til at køre modeller som Phi fuldstændigt på din egen hardware - ingen Azure-abonnement, API-nøgle eller netværksforbindelse kræves. Den vælger automatisk den bedste tilgængelige udførelsesudbyder (NPU, GPU eller CPU) og tilbyder en OpenAI-kompatibel endpoint, så eksisterende `openai`/Azure AI Inference SDK kode kan pege på den med minimale ændringer. Se [Foundry Local dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en tværplatforms accelerator til inferens og træning af maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftfuldt værktøj, der hjælper dig med at køre generative AI-modeller effektivt på tværs af forskellige platforme.

## Hvad er ONNX Runtime?
ONNX Runtime er et open source-projekt, der muliggør højtydende inferens af maskinlæringsmodeller. Det understøtter modeller i Open Neural Network Exchange (ONNX)-formatet, som er en standard til repræsentation af maskinlæringsmodeller. ONNX Runtime inferens kan muliggøre hurtigere kundeoplevelser og lavere omkostninger, og understøtter modeller fra dybdelæringsframeworks såsom PyTorch og TensorFlow/Keras samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost osv. ONNX Runtime er kompatibel med forskellige hardware, drivere og operativsystemer og leverer optimal ydeevne ved at udnytte hardwareacceleratorer, hvor det er relevant, sammen med grafoptimeringer og transformationer.

## Hvad er Generativ AI?
Generativ AI refererer til AI-systemer, der kan generere nyt indhold, såsom tekst, billeder eller musik, baseret på de data, de er trænet på. Eksempler inkluderer sprogmodeller som GPT-3 og billedgenereringsmodeller såsom Stable Diffusion. ONNX Runtime for GenAI-biblioteket leverer den generative AI-loop for ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, søgning og sampling, samt KV-cache-håndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI udvider funktionerne i ONNX Runtime til at understøtte generative AI-modeller. Her er nogle nøglefunktioner:

- **Bred platformunderstøttelse:** Det fungerer på forskellige platforme, herunder Windows, Linux, macOS, Android og iOS.
- **Modelunderstøttelse:** Det understøtter mange populære generative AI-modeller, såsom LLaMA, GPT-Neo, BLOOM og flere.
- **Ydeevneoptimering:** Det inkluderer optimeringer til forskellige hardwareacceleratorer som NVIDIA GPU'er, AMD GPU'er og mere2.
- **Brugervenlighed:** Det tilbyder API'er til nem integration i applikationer, så du kan generere tekst, billeder og andet indhold med minimal kode.
- Brugere kan kalde en høj-niveau generate()-metode, eller køre hver iteration af modellen i en løkke, generere ét token ad gangen og eventuelt opdatere genereringsparametre inde i løkken.
- ONNX runtime har også understøttelse for greedy/beam search og TopP, TopK sampling til at generere tokensekvenser samt indbygget logitsbehandling såsom gentagelsesstraffe. Du kan også nemt tilføje brugerdefineret scoring.

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

Ud over ONNX Runtime, Ollama og Foundry Local reference metoder, kan vi også færdiggøre referencen af kvantitative modeller baseret på modelreferencemetoder leveret af forskellige producenter. Såsom Apple MLX framework med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også finde mere indhold i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mere

Vi har lært det grundlæggende om Phi-3/3.5-familien, men for at lære mere om SLM har vi brug for mere viden. Du kan finde svarene i Phi-3 Cookbook. Hvis du vil vide mere, bedes du besøge [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->