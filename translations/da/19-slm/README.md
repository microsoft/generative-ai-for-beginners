# Introduktion til små sprogmodeller for generativ AI for begyndere
Generativ AI er et fascinerende område inden for kunstig intelligens, der fokuserer på at skabe systemer, der er i stand til at generere nyt indhold. Dette indhold kan spænde fra tekst og billeder til musik og endda hele virtuelle miljøer. En af de mest spændende anvendelser af generativ AI er inden for sprogmodeller.

## Hvad er små sprogmodeller?

En lille sprogmodel (SLM) repræsenterer en nedskaleret variant af en stor sprogmodel (LLM), der udnytter mange af de arkitektoniske principper og teknikker fra LLM'er, samtidig med at den har et betydeligt reduceret beregningsmæssigt fodaftryk.

SLM'er er en undergruppe af sprogmodeller designet til at generere menneskelignende tekst. I modsætning til deres større modstykker, såsom GPT-4, er SLM'er mere kompakte og effektive, hvilket gør dem ideelle til anvendelser, hvor beregningsressourcer er begrænsede. På trods af deres mindre størrelse kan de stadig udføre forskellige opgaver. Typisk konstrueres SLM'er ved at komprimere eller destillere LLM'er med det formål at bevare en væsentlig del af den oprindelige models funktionalitet og sproglige evner. Denne reduktion i modelstørrelse mindsker kompleksiteten som helhed, hvilket gør SLM'er mere effektive med hensyn til både hukommelsesforbrug og beregningskrav. På trods af disse optimeringer kan SLM'er stadig udføre en bred vifte af naturligt sprogbehandlingsopgaver (NLP):

- Tekstgenerering: Skabe sammenhængende og kontekstuelt relevante sætninger eller afsnit.
- Tekstfuldførelse: Forudsige og fuldføre sætninger baseret på en given prompt.
- Oversættelse: Konvertere tekst fra et sprog til et andet.
- Opsummering: Forkorte lange tekststykker til kortere, mere letfordøjelige resuméer.

Dog med visse kompromiser i ydeevne eller dybde af forståelse sammenlignet med deres større modstykker.

## Hvordan fungerer små sprogmodeller?
SLM'er trænes på enorme mængder tekstdata. Under træningen lærer de sprogets mønstre og strukturer, hvilket gør dem i stand til at generere tekst, der både er grammatisk korrekt og kontekstuelt passende. Træningsprocessen involverer:

- Datainsamling: Indsamling af store datasæt af tekst fra forskellige kilder.
- Forbehandling: Rensning og organisering af dataene for at gøre dem egnede til træning.
- Træning: Brug af maskinlæringsalgoritmer til at lære modellen at forstå og generere tekst.
- Finjustering: Justering af modellen for at forbedre dens ydeevne på specifikke opgaver.

Udviklingen af SLM'er er i tråd med det stigende behov for modeller, der kan implementeres i ressourcestærk begrænsede miljøer, såsom mobile enheder eller edge computing-platforme, hvor fuldskala LLM'er kan være upraktiske på grund af deres store ressourceforbrug. Ved at fokusere på effektivitet balancerer SLM'er ydeevne med tilgængelighed, hvilket muliggør bredere anvendelse på tværs af forskellige domæner.

![slm](../../../translated_images/da/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Læringsmål

I denne lektion håber vi at introducere viden om SLM og kombinere det med Microsoft Phi-3 for at lære om forskellige scenarier inden for tekstindhold, vision og MoE.

Ved slutningen af denne lektion bør du kunne besvare følgende spørgsmål:

- Hvad er SLM?
- Hvad er forskellen mellem SLM og LLM?
- Hvad er Microsoft Phi-3/3.5-familien?
- Hvordan kører man inferens med Microsoft Phi-3/3.5-familien?

Klar? Lad os komme i gang.

## Forskellene mellem store sprogmodeller (LLM'er) og små sprogmodeller (SLM'er)

Både LLM'er og SLM'er bygger på grundlæggende principper for probabilistisk maskinlæring og følger lignende tilgange i deres arkitektoniske design, træningsmetoder, data-genereringsprocesser og modelvurderingsteknikker. Dog adskiller flere nøglefaktorer disse to typer modeller.

## Anvendelser af små sprogmodeller

SLM'er har et bredt anvendelsesområde, herunder:

- Chatbots: Yde kundesupport og engagere brugere i samtalebaserede interaktioner.
- Indholdsskabelse: Assistere skribenter ved at generere idéer eller endda udforme hele artikler.
- Uddannelse: Hjælpe elever med skriveopgaver eller at lære nye sprog.
- Tilgængelighed: Skabe værktøjer til personer med handicap, såsom tekst-til-tale-systemer.

**Størrelse**
  
En væsentlig forskel mellem LLM'er og SLM'er ligger i modellernes skala. LLM'er, såsom ChatGPT (GPT-4), kan have anslået 1,76 billioner parametre, mens open source SLM'er som Mistral 7B er designet med betydeligt færre parametre — cirka 7 milliarder. Denne forskel skyldes primært forskelle i modelarkitektur og træningsprocesser. For eksempel anvender ChatGPT en selvopmærksomhedsmekanisme inden for en encoder-decoder ramme, mens Mistral 7B bruger glidende vindues-opmærksomhed, hvilket muliggør mere effektiv træning inden for en decoder-only model. Denne arkitektoniske variation har dybtgående konsekvenser for modellernes kompleksitet og ydeevne.

**Forståelse**

SLM'er optimeres typisk til ydeevne inden for specifikke domæner, hvilket gør dem meget specialiserede, men potentielt begrænsede i deres evne til at give bred kontekstuel forståelse på tværs af flere vidensområder. Til gengæld sigter LLM'er efter at simulere menneskelig intelligens på et mere omfattende niveau. Trænet på store og forskelligartede datasæt er LLM'er designet til at præstere godt på tværs af en række domæner og tilbyder større alsidighed og tilpasningsevne. Derfor er LLM'er mere egnede til en bredere vifte af nedstrømsopgaver, såsom naturlig sprogbehandling og programmering.

**Beregning**

Træning og implementering af LLM'er er ressourcekrævende processer, som ofte kræver betydelig beregningsinfrastruktur, herunder storskala GPU-klynger. For eksempel kan træningen af en model som ChatGPT fra bunden nødvendiggøre tusindvis af GPU'er over længere perioder. Til sammenligning er SLM'er, med deres mindre parameterantal, mere tilgængelige med hensyn til beregningsressourcer. Modeller som Mistral 7B kan trænes og køres på lokale maskiner med moderat GPU-kapacitet, selvom træning stadig kræver flere timers kørsel på tværs af flere GPU'er.

**Bias**

Bias er et kendt problem i LLM'er, primært på grund af træningsdataenes natur. Disse modeller er ofte afhængige af rå, offentligt tilgængelige data fra internettet, som kan underrepræsentere eller fejlagtigt repræsentere visse grupper, indføre fejlbehæftet mærkning eller afspejle sproglige forudindtagetheder påvirket af dialekt, geografiske variationer og grammatiske regler. Derudover kan kompleksiteten i LLM-arkitekturer utilsigtet forværre bias, som kan gå ubemærket hen uden omhyggelig finjustering. Til gengæld, fordi SLM'er trænes på mere begrænsede, domænespecifikke datasæt, er de mindre modtagelige over for sådanne biases, selvom de ikke er immune.

**Inferens**

Den reducerede størrelse af SLM'er giver dem en betydelig fordel med hensyn til inferenshastighed, hvilket gør dem i stand til effektivt at generere output på lokal hardware uden behov for omfattende parallel behandling. I modsætning hertil kræver LLM'er på grund af deres størrelse og kompleksitet ofte betydelige parallelle beregningsressourcer for at opnå acceptable inferenstider. Tilstedeværelsen af flere samtidige brugere sænker yderligere LLM'ers svartider, især når de deployeres i stor skala.

Sammenfattende, mens både LLM'er og SLM'er deler en grundlæggende maskinlæringsbasis, adskiller de sig væsentligt med hensyn til modelstørrelse, ressourcekrav, kontekstuel forståelse, modtagelighed for bias og inferenshastighed. Disse forskelle afspejler deres respektive egnethed til forskellige anvendelsestilfælde, hvor LLM'er er mere alsidige men ressourcetunge, og SLM'er tilbyder mere domænespecifik effektivitet med reducerede beregningskrav.

***Bemærk: I denne lektion vil vi introducere SLM ved hjælp af Microsoft Phi-3 / 3.5 som eksempel.***

## Introduktion til Phi-3 / Phi-3.5 familien

Phi-3 / 3.5 familien henvender sig primært til tekst-, vision- og Agent (MoE) applikationsscenarier:

### Phi-3 / 3.5 Instruct

Primært til tekstgenerering, chatfuldførelse og udtrækning af indholdsoplysninger osv.

**Phi-3-mini**

3.8B sprogmodellen er tilgængelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3 modeller præsterer markant bedre end sprogmodeller af tilsvarende og større størrelser på nøglebenchmarks (se benchmarktal nedenfor, højere tal er bedre). Phi-3-mini overgår modeller, der er dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, herunder GPT-3.5.

**Phi-3-small & medium**

Med kun 7B parametre slår Phi-3-small GPT-3.5T på en række sprog-, ræsonnerings-, kodnings- og matematikbenchmarks.

Phi-3-medium med 14B parametre fortsætter denne tendens og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan betragte den som en opgradering af Phi-3-mini. Selvom antallet af parametre forbliver uændret, forbedrer den evnen til at understøtte flere sprog (understøtter 20+ sprog: Arabisk, Kinesisk, Tjekkisk, Dansk, Hollandsk, Engelsk, Finsk, Fransk, Tysk, Hebraisk, Ungarsk, Italiensk, Japansk, Koreansk, Norsk, Polsk, Portugisisk, Russisk, Spansk, Svensk, Thai, Tyrkisk, Ukrainsk) og tilføjer stærkere understøttelse af lange kontekster.

Phi-3.5-mini med 3.8B parametre overgår sprogmodeller af samme størrelse og matcher modeller dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan betragte Instruct-modellen fra Phi-3/3.5 som Phis evne til at forstå, og Vision er det, der giver Phi øjne til at forstå verden.


**Phi-3-Vision**

Phi-3-vision, med kun 4.2B parametre, fortsætter denne tendens og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V i generelle visuelle ræsonneringsopgaver, OCR samt tabel- og diagramforståelsesopgaver.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en opgradering af Phi-3-Vision, der tilføjer understøttelse for flere billeder. Du kan betragte det som en forbedring i vision, hvor du ikke kun kan se billeder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash inden for OCR, tabel- og diagramforståelsesopgaver og matcher på generelle visuelle vidensræsonneringsopgaver. Understøtter multi-frame input, dvs. ræsonnering på flere inputbilleder


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gør det muligt for modeller at blive fortrænet med langt mindre beregning, hvilket betyder, at man dramatisk kan skalere modellen eller datasætets størrelse med samme beregningsbudget som en tæt model. Især bør en MoE-model nå samme kvalitet som dens tætte modstykke meget hurtigere under fortræning.

Phi-3.5-MoE består af 16x3.8B ekspertmoduler. Phi-3.5-MoE med kun 6.6B aktive parametre opnår et lignende niveau af ræsonnering, sprogforståelse og matematik som langt større modeller.

Vi kan bruge Phi-3/3.5 familie modellen baseret på forskellige scenarier. I modsætning til LLM kan du implementere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheder.


## Hvordan bruger man Phi-3/3.5 familie modeller

Vi håber at bruge Phi-3/3.5 i forskellige scenarier. Næste vil vi bruge Phi-3/3.5 baseret på forskellige scenarier.

![phi3](../../../translated_images/da/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via cloud-API'er

**Microsoft Foundry-modeller**

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatning.

> **Bemærk:** Hele Phi-3/3.5 familien (Instruct, Vision og MoE varianter) blev udfaset fra Microsoft Foundry Models-kataloget den 2025-08-30. Brug `Phi-4` (Instruct) eller `Phi-4-mini-instruct` der i stedet — Phi-3/3.5 eksemplerne nedenfor fungerer stadig via Hugging Face, Ollama, ONNX Runtime og NVIDIA NIM.

Microsoft Foundry Models tilbyder nu efterfølgerne Phi-4. Brug `Phi-4` eller `Phi-4-mini-instruct` i stedet for de udfasede Phi-3/3.5 modeller, når du følger eksemplerne på cloud API.

- Demo: Sammenligning af effekterne af Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/da/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/da/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Hvis du ønsker at bruge vision (multimodale) modeller i skyen, brug den nu tilgængelige `Phi-4-multimodal-instruct` via Microsoft Foundry i stedet for de udfasede Phi-3/3.5 Vision modeller; til tekstopgaver brug `Phi-4` eller `Phi-4-mini-instruct`. Phi-3.5 MoE modellen er udfaset fra Microsoft Foundry, så brug de andre muligheder beskrevet i denne lektion (for eksempel Hugging Face) hvis du ønsker at eksperimentere med den. Hvis du er interesseret, kan du læse Phi Cookbook for at lære, hvordan du kalder Phi-modeller via Microsoft Foundry [Klik på dette link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Ud over Microsoft Foundry Models-kataloget, som er skybaseret, kan du også bruge [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) til at gennemføre relaterede kald. Du kan besøge NVIDIA NIM for at færdiggøre API-kald til Phi-3/3.5 familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sæt accelererede inferens-mikrotjenester designet til at hjælpe udviklere med effektivt at implementere AI-modeller på tværs af forskellige miljøer, herunder skyer, datacentre og arbejdsstationer.

Her er nogle nøglefunktioner ved NVIDIA NIM:

- **Nem implementering:** NIM tillader implementering af AI-modeller med en enkelt kommando, hvilket gør det let at integrere i eksisterende arbejdsprocesser.
- **Optimeret ydeevne:** Det udnytter NVIDIAs forudoptimerede inferensmotorer såsom TensorRT og TensorRT-LLM for at sikre lav latenstid og høj gennemløb.
- **Skalerbarhed:** NIM understøtter autoskalering på Kubernetes, hvilket gør det muligt effektivt at håndtere varierende arbejdsbelastninger.
- **Sikkerhed og kontrol:** Organisationer kan bevare kontrol over deres data og applikationer ved selv at hoste NIM-mikrotjenester på deres egen administrerede infrastruktur.
- **Standard API'er:** NIM tilbyder branche-standard API'er, hvilket gør det nemt at bygge og integrere AI-applikationer som chatbots, AI-assistenter og mere.

NIM er en del af NVIDIA AI Enterprise, som har til formål at forenkle implementeringen og driften af AI-modeller og sikre, at de kører effektivt på NVIDIA GPU’er.

- Demo: Brug af NVIDIA NIM til at kalde Phi-3.5-Vision-API [[Klik på dette link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kørsel af Phi-3/3.5 Lokalt
Inferens i relation til Phi-3, eller en hvilken som helst sprogmodel som GPT-3, refererer til processen med at generere svar eller forudsigelser baseret på den input, den modtager. Når du giver en prompt eller et spørgsmål til Phi-3, bruger den sit trænede neurale netværk til at udlede det mest sandsynlige og relevante svar ved at analysere mønstre og relationer i de data, den er trænet på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftfuldt bibliotek designet til naturlig sprogbehandling (NLP) og andre maskinlæringsopgaver. Her er nogle nøglepunkter om det:

1. **Foruddannede modeller**: Det tilbyder tusindvis af foruddannede modeller, der kan bruges til forskellige opgaver såsom tekstklassificering, navngiven entitetsgenkendelse, spørgsmålssvar, opsummering, oversættelse og tekstgenerering.

2. **Framework-interoperabilitet**: Biblioteket understøtter flere dybdelæringsframeworks, herunder PyTorch, TensorFlow og JAX. Dette gør det muligt at træne en model i ét framework og bruge den i et andet.

3. **Multimodale kapaciteter**: Ud over NLP understøtter Hugging Face Transformers også opgaver inden for computer vision (f.eks. billedklassificering, objektgenkendelse) og lydbehandling (f.eks. talegenkendelse, lydklassificering).

4. **Nem at bruge**: Biblioteket tilbyder API'er og værktøjer til nemt at downloade og finjustere modeller, hvilket gør det tilgængeligt for både begyndere og eksperter.

5. **Fællesskab og ressourcer**: Hugging Face har et livligt fællesskab og omfattende dokumentation, tutorials og vejledninger til at hjælpe brugere i gang og få mest muligt ud af biblioteket.
[officiel dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest anvendte metode, men den kræver også GPU-acceleration. Scenarier som Vision og MoE kræver nemlig mange beregninger, som vil være meget langsomme på CPU, hvis de ikke er kvantiserede.


- Demo: Brug af Transformer til at kalde Phi-3.5-Instruct [Klik på dette link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-Vision [Klik på dette link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Brug af Transformer til at kalde Phi-3.5-MoE [Klik på dette link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en platform designet til at gøre det lettere at køre store sprogmodeller (LLMs) lokalt på din maskine. Den understøtter forskellige modeller som Llama 3.1, Phi 3, Mistral og Gemma 2 blandt andre. Platformen forenkler processen ved at samle modelvægte, konfiguration og data i en enkelt pakke, hvilket gør det nemmere for brugere at tilpasse og skabe deres egne modeller. Ollama er tilgængelig for macOS, Linux og Windows. Det er et fremragende værktøj, hvis du ønsker at eksperimentere med eller implementere LLM'er uden at være afhængig af cloud-tjenester. Ollama er den mest direkte metode, du skal blot udføre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, lokale runtime til at køre modeller som Phi helt på din egen hardware - ingen Azure-abonnement, API-nøgle eller netværksforbindelse nødvendig. Det vælger automatisk den bedste tilgængelige eksekveringsudbyder (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endpoint, så eksisterende `openai`/Azure AI Inference SDK-kode kan pege på det med minimale ændringer. Se [Foundry Local dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en platformuafhængig accelerator til inferens og træning af maskinlæringsmodeller. ONNX Runtime for Generative AI (GENAI) er et kraftfuldt værktøj, der hjælper dig med effektivt at køre generative AI-modeller på tværs af forskellige platforme. 

## Hvad er ONNX Runtime?
ONNX Runtime er et open source-projekt, der muliggør højtydende inferens af maskinlæringsmodeller. Det understøtter modeller i Open Neural Network Exchange (ONNX) formatet, som er en standard for repræsentation af maskinlæringsmodeller. ONNX Runtime-inferens kan muliggøre hurtigere kundeoplevelser og lavere omkostninger, og understøtter modeller fra dybdelæringsframeworks som PyTorch og TensorFlow/Keras samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost, osv. ONNX Runtime er kompatibel med forskellig hardware, drivere og operativsystemer, og leverer optimal ydeevne ved at udnytte hardwareacceleration hvor muligt sammen med optimeringer og transformationer af grafen.

## Hvad er Generativ AI?
Generativ AI refererer til AI-systemer, der kan generere nyt indhold, såsom tekst, billeder eller musik, baseret på de data, de er trænet på. Eksempler inkluderer sprogmodeller som GPT-3 og billedgenereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket leverer loopet for generativ AI til ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, søgning og sampling, samt KV cache-styring.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI udvider ONNX Runtimes kapaciteter til at understøtte generative AI-modeller. Her er nogle nøglefunktioner:

- **Bred platformsunderstøttelse:** Det virker på forskellige platforme, herunder Windows, Linux, macOS, Android og iOS.
- **Modelunderstøttelse:** Det understøtter mange populære generative AI-modeller, såsom LLaMA, GPT-Neo, BLOOM og flere.
- **Performanceoptimering:** Det inkluderer optimeringer til forskellige hardwareacceleratorer som NVIDIA GPU'er, AMD GPU'er med mere.
- **Nem at bruge:** Det tilbyder API'er til nem integration i applikationer, som tillader dig at generere tekst, billeder og andet indhold med minimal kode.
- Brugere kan kalde en høj-niveau generate() metode eller køre hver iteration af modellen i en løkke, generere et token ad gangen og eventuelt opdatere genereringsparametre inde i løkken.
- ONNX runtime har også understøttelse for greedy/beam search og TopP, TopK sampling til at generere token-sekvenser samt indbygget logitsbehandling som gentagelsesstraffe. Du kan også nemt tilføje brugerdefineret scoring.

## Kom i gang
For at komme i gang med ONNX Runtime for GENAI, kan du følge disse trin:

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
### Demo: Brug af ONNX Runtime GenAI til at kalde Phi-3.5-Vision


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

Ud over ONNX Runtime, Ollama og Foundry Local referencemetoderne, kan vi også fuldføre referencen for kvantitative modeller baseret på model referencemetoder leveret af forskellige producenter. Som Apple MLX framework med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også finde mere indhold i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mere

Vi har lært det grundlæggende om Phi-3/3.5-familien, men for at lære mere om SLM har vi brug for mere viden. Du kan finde svarene i Phi-3 Cookbook. Hvis du vil lære mere, så besøg venligst [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->