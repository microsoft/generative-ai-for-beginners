# Introduksjon til små språkmodeller for generativ AI for nybegynnere
Generativ AI er et fascinerende felt innen kunstig intelligens som fokuserer på å skape systemer som kan generere nytt innhold. Dette innholdet kan variere fra tekst og bilder til musikk og til og med hele virtuelle miljøer. En av de mest spennende anvendelsene av generativ AI er innenfor området språkmodeller.

## Hva er små språkmodeller?

En liten språkmodell (SLM) representerer en nedskalert variant av en stor språkmodell (LLM), som benytter mange av arkitekturelle prinsipper og teknikker fra LLM-er, samtidig som den har et betydelig redusert beregningsavtrykk.

SLM-er er en undergruppe av språkmodeller designet for å generere menneskelignende tekst. I motsetning til deres større motparter, som GPT-4, er SLM-er mer kompakte og effektive, noe som gjør dem ideelle for applikasjoner der beregningsressursene er begrenset. Til tross for sin mindre størrelse, kan de fortsatt utføre en rekke oppgaver. Vanligvis bygges SLM-er ved å komprimere eller destillere LLM-er, med mål om å bevare en betydelig del av den opprinnelige modellens funksjonalitet og språklige evner. Denne reduksjonen i modellstørrelse reduserer den totale kompleksiteten, noe som gjør SLM-er mer effektive både med hensyn til minnebruk og beregningskrav. Til tross for disse optimaliseringene kan SLM-er fortsatt utføre et bredt spekter av oppgaver innen naturlig språkbehandling (NLP):

- Tekstgenerering: Lage sammenhengende og kontekstuelt relevante setninger eller avsnitt.
- Tekstfullføring: Forutsi og fullføre setninger basert på en gitt prompt.
- Oversettelse: Konvertere tekst fra ett språk til et annet.
- Oppsummering: Komprimere lange tekster til kortere, mer fordøyelige oppsummeringer.

Selv om det kan være noen kompromisser i ytelse eller dybde av forståelse sammenlignet med deres større motparter.

## Hvordan fungerer små språkmodeller?
SLM-er trenes på store mengder tekstdata. Under treningen lærer de mønstre og strukturer i språket, noe som gjør dem i stand til å generere tekst som både er grammatisk korrekt og kontekstuelt passende. Treningsprosessen innebærer:

- Datainnsamling: Samle store datasett med tekst fra ulike kilder.
- Forbehandling: Rense og organisere dataene for å gjøre dem egnet for trening.
- Trening: Bruke maskinlæringsalgoritmer for å lære modellen hvordan den skal forstå og generere tekst.
- Finjustering: Justere modellen for å forbedre ytelsen på spesifikke oppgaver.

Utviklingen av SLM-er samsvarer med det økende behovet for modeller som kan distribueres i ressursbegrensede miljøer, som mobile enheter eller edge computing-plattformer, der fullskala LLM-er kan være upraktiske på grunn av deres store ressursbehov. Ved å fokusere på effektivitet balanserer SLM-er ytelse med tilgjengelighet, noe som muliggjør bredere anvendelse på tvers av ulike domener.

![slm](../../../translated_images/no/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Læringsmål

I denne leksjonen håper vi å introdusere kunnskap om SLM og kombinere den med Microsoft Phi-3 for å lære ulike scenarier innen tekstinnhold, visjon og MoE.

Etter denne leksjonen skal du kunne svare på følgende spørsmål:

- Hva er SLM?
- Hva er forskjellen mellom SLM og LLM?
- Hva er Microsoft Phi-3/3.5-familien?
- Hvordan kjøre inferens med Microsoft Phi-3/3.5-familien?

Klar? La oss komme i gang.

## Forskjellene mellom store språkmodeller (LLM) og små språkmodeller (SLM)

Både LLM-er og SLM-er er bygget på grunnleggende prinsipper for sannsynlighetsbasert maskinlæring, med lignende tilnærminger i arkitekturdesign, treningsmetoder, datagenereringsprosesser og modellvurderingsteknikker. Likevel skiller flere viktige faktorer disse to modelltypene.

## Anvendelser av små språkmodeller

SLM-er har et bredt spekter av anvendelser, inkludert:

- Chatbots: Gi kundestøtte og engasjere brukere i samtalebasert interaksjon.
- Innholdsproduksjon: Hjelpe forfattere med å generere ideer eller til og med utforme hele artikler.
- Utdanning: Hjelpe studenter med skriveoppgaver eller læring av nye språk.
- Tilgjengelighet: Lage verktøy for personer med funksjonshemminger, som tekst-til-tale-systemer.

**Størrelse**
 
En hovedforskjell mellom LLM-er og SLM-er ligger i modellens størrelse. LLM-er, som ChatGPT (GPT-4), kan bestå av anslagsvis 1,76 billioner parametere, mens open source SLM-er som Mistral 7B er designet med betydelig færre parametere — omtrent 7 milliarder. Denne forskjellen skyldes hovedsakelig forskjeller i modellarkitektur og treningsprosesser. For eksempel bruker ChatGPT en selvoppmerksomhetsmekanisme innenfor en encoder-decoder-ramme, mens Mistral 7B benytter sliding window attention, noe som muliggjør mer effektiv trening i en decoder-only modell. Denne arkitekturelle variasjonen har dype implikasjoner for kompleksiteten og ytelsen til modellene.

**Forståelse**

SLM-er er vanligvis optimalisert for ytelse innen spesifikke domener, noe som gjør dem svært spesialiserte, men potensielt begrenset i evnen til å gi bred kontekstuell forståelse på tvers av flere kunnskapsfelt. I motsetning til dette har LLM-er som mål å simulere menneskelignende intelligens på et mer omfattende nivå. Trenet på store, mangfoldige datasett, er LLM-er designet for å prestere godt på tvers av en rekke domener, og tilbyr større allsidighet og tilpasningsevne. Følgelig egner LLM-er seg bedre for et bredt spekter av etterfølgende oppgaver, som naturlig språkbehandling og programmering.

**Beregning**

Trening og utrulling av LLM-er er ressurskrevende prosesser, som ofte krever betydelig beregningsinfrastruktur, inkludert store GPU-klynger. For eksempel kan trening av en modell som ChatGPT fra bunnen av kreve tusenvis av GPU-er over lang tid. I kontrast er SLM-er, med sitt mindre antall parametere, mer tilgjengelige med hensyn til beregningsressurser. Modeller som Mistral 7B kan trenes og kjøre på lokale maskiner utstyrt med moderate GPU-kapasiteter, selv om treningen fortsatt krever flere timer på tvers av flere GPU-er.

**Skjevhet**

Skjevhet er et kjent problem i LLM-er, hovedsakelig på grunn av arten av treningsdataene. Disse modellene baserer seg ofte på rådata fra internett som er åpent tilgjengelig, og som kan underrepresentere eller feile å representere visse grupper, introdusere feilaktig merking, eller reflektere språklige skjevheter påvirket av dialekter, geografiske variasjoner og grammatiske regler. I tillegg kan kompleksiteten i LLM-arkitekturer utilsiktet forsterke skjevhet, noe som kan gå ubemerket uten nøye finjustering. På den annen side, siden SLM-er trenes på mer begrensede, domene-spesifikke datasett, er de iboende mindre utsatt for slike skjevheter, selv om de ikke er immune mot dem.

**Inferens**

Den reduserte størrelsen på SLM-er gir dem en betydelig fordel når det gjelder inferenshastighet, slik at de kan generere resultater effektivt på lokal maskinvare uten behov for omfattende parallell prosessering. I motsetning krever LLM-er, på grunn av deres størrelse og kompleksitet, ofte betydelige parallelle beregningsressurser for å oppnå akseptable inferenstider. Tilstedeværelsen av mange samtidige brukere senker også LLM-ers responstider, spesielt når de distribueres i stor skala.

Oppsummert, selv om både LLM-er og SLM-er deler en grunnleggende basis i maskinlæring, skiller de seg betydelig med hensyn til modellstørrelse, ressurskrav, kontekstuell forståelse, utsatthet for skjevhet og inferenshastighet. Disse forskjellene reflekterer deres respektive egnethet for ulike bruksområder, hvor LLM-er er mer allsidige, men ressurskrevende, mens SLM-er tilbyr mer domene-spesifikk effektivitet med reduserte beregningsbehov.

***Merk: I denne leksjonen vil vi introdusere SLM ved å bruke Microsoft Phi-3 / 3.5 som eksempel.***

## Introduksjon til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien retter seg hovedsakelig mot tekst-, visjons- og agentapplikasjonsscenarier (MoE):

### Phi-3 / 3.5 Instruct

Hovedsakelig for tekstgenerering, chat-fulføring og innholdsinformasjonsekstraksjon, osv.

**Phi-3-mini**

Den 3,8 milliarder parametermodellen er tilgjengelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modellene overgår betydelig språkmodeller av lik eller større størrelse på viktige benchmarks (se benchmarks nedenfor, høyere tall er bedre). Phi-3-mini overgår modeller som er dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inkludert GPT-3.5.

**Phi-3-small & medium**

Med bare 7 milliarder parametere slår Phi-3-small GPT-3.5T på en rekke språk-, resonnerings-, kode- og matematikkbenchmarks.

Phi-3-medium med 14 milliarder parametere fortsetter denne trenden og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan se på den som en oppgradering av Phi-3-mini. Selv om parameterne forblir uendret, forbedrer den evnen til å støtte flere språk (støtter 20+ språk: arabisk, kinesisk, tsjekkisk, dansk, nederlandsk, engelsk, finsk, fransk, tysk, hebraisk, ungarsk, italiensk, japansk, koreansk, norsk, polsk, portugisisk, russisk, spansk, svensk, thai, tyrkisk, ukrainsk) og legger til sterkere støtte for lang kontekst.

Phi-3.5-mini med 3,8 milliarder parametere overgår språkmodeller av samme størrelse og er på nivå med modeller som er dobbelt så store.

### Phi-3 / 3.5 Visjon

Vi kan se på Instruct-modellen til Phi-3/3.5 som Phis evne til å forstå, og Visjon er det som gir Phi øyne til å forstå verden.


**Phi-3-Visjon**

Phi-3-vision, med bare 4,2 milliarder parametere, fortsetter denne trenden og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle resonneringsoppgaver, OCR, og oppgaver med tabell- og diagramforståelse.


**Phi-3.5-Visjon**

Phi-3.5-Visjon er også en oppgradering av Phi-3-Visjon, som legger til støtte for flere bilder. Du kan se på det som en forbedring i visjon, ikke bare kan du se bilder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash på tvers av OCR-, tabell- og diagramforståelsesoppgaver og er på nivå med generelle visuelle kunnskapsresonneringsoppgaver. Støtter flerbildeinngang, dvs. kan utføre resonnering på flere inngangsbilder


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gjør det mulig for modeller å forhåndstrenes med langt mindre datakraft, noe som betyr at du dramatisk kan skalere opp modell- eller datasettstørrelsen med samme datakraftbudsjett som en tett modell. Spesielt bør en MoE-modell oppnå samme kvalitet som sin tette motpart mye raskere under forhåndstreningen.

Phi-3.5-MoE består av 16x3,8B ekspertmoduler. Phi-3.5-MoE med bare 6,6 milliarder aktive parametere oppnår et lignende nivå av resonnering, språkforståelse og matematikk som mye større modeller.

Vi kan bruke Phi-3/3.5-familien av modeller basert på forskjellige scenarier. I motsetning til LLM kan du distribuere Phi-3/3.5-mini eller Phi-3/3.5-Visjon på edge-enheter.


## Hvordan bruke Phi-3/3.5-familie modeller

Vi ønsker å bruke Phi-3/3.5 i forskjellige scenarier. Neste skal vi bruke Phi-3/3.5 basert på ulike scenarier.

![phi3](../../../translated_images/no/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via sky-APIer

**Microsoft Foundry-modeller**

> **Merk:** GitHub Models utfases ved slutten av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatningen.

> **Merk:** Hele Phi-3/3.5-familien (Instruct, Vision og MoE-varianter) ble tatt ut av katalogen til Microsoft Foundry Models 30.08.2025. Bruk `Phi-4` (Instruct) eller `Phi-4-mini-instruct` der i stedet — Phi-3/3.5-eksemplene nedenfor fungerer fortsatt via Hugging Face, Ollama, ONNX Runtime, og NVIDIA NIM.

Microsoft Foundry Models tilbyr nå etterfølgerne Phi-4. Bruk `Phi-4` eller `Phi-4-mini-instruct` i stedet for de avviklede Phi-3/3.5-modellene når du følger sky-API-eksemplene.

- Demo: Sammenligning av effektene av Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/no/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/no/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Hvis du ønsker å bruke visjons(modale) modeller i skyen, bruk de tilgjengelige `Phi-4-multimodal-instruct` gjennom Microsoft Foundry i stedet for de avviklede Phi-3/3.5-Visjonsmodellene; for tekstoppgaver bruk `Phi-4` eller `Phi-4-mini-instruct`. Phi-3.5 MoE-modellen er avviklet fra Microsoft Foundry, så bruk de andre alternativene beskrevet i denne leksjonen (for eksempel Hugging Face) hvis du ønsker å eksperimentere med den. Hvis du er interessert, kan du lese Phi Cookbook for å lære hvordan du kaller Phi-modeller gjennom Microsoft Foundry [Klikk denne lenken](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

I tillegg til skybaserte Microsoft Foundry Models-katalogen kan du også bruke [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) for å fullføre relaterte kall. Du kan besøke NVIDIA NIM for å utføre API-kall for Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sett akselererte inferens-mikrotjenester designet for å hjelpe utviklere med å distribuere AI-modeller effektivt på tvers av ulike miljøer, inkludert skyer, datasentre og arbeidsstasjoner.

Her er noen nøkkelfunksjoner ved NVIDIA NIM:

- **Enkel distribusjon:** NIM tillater distribusjon av AI-modeller med en enkelt kommando, noe som gjør det enkelt å integrere i eksisterende arbeidsflyter.
- **Optimalisert ytelse:** Den utnytter NVIDIAs forhåndsoptimaliserte inferensmotorer, som TensorRT og TensorRT-LLM, for å sikre lav ventetid og høy gjennomstrømning.
- **Skalerbarhet:** NIM støtter autoskalering på Kubernetes, noe som gjør det mulig å håndtere varierende arbeidsmengder effektivt.
- **Sikkerhet og kontroll:** Organisasjoner kan beholde kontroll over sine data og applikasjoner ved å selvhoste NIM-mikrotjenester på egen administrert infrastruktur.
- **Standard API-er:** NIM tilbyr bransjestandard API-er, noe som gjør det enkelt å bygge og integrere AI-applikasjoner som chatboter, AI-assistenter og mer.

NIM er en del av NVIDIA AI Enterprise, som har som mål å forenkle distribusjon og drift av AI-modeller, og sikrer at de kjører effektivt på NVIDIA GPUer.

- Demo: Bruke NVIDIA NIM for å kalle Phi-3.5-Vision-API [[Klikk på denne lenken](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kjøre Phi-3/3.5 lokalt
Inferens i forhold til Phi-3, eller enhver språkmodell som GPT-3, refererer til prosessen med å generere svar eller prediksjoner basert på den inputen den mottar. Når du gir en prompt eller spørsmål til Phi-3, bruker den det trente nevrale nettverket for å slutte seg til det mest sannsynlige og relevante svaret ved å analysere mønstre og relasjoner i dataene den ble trent på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftfullt bibliotek designet for naturlig språkbehandling (NLP) og andre maskinlæringsoppgaver. Her er noen viktige punkter om det:

1. **Fortrente modeller**: Den tilbyr tusenvis av forhåndstrente modeller som kan brukes til forskjellige oppgaver som tekstklassifisering, navngitt entity-gjenkjenning, spørsmål og svar, oppsummering, oversettelse og tekstgenerering.

2. **Rammeverkskompatibilitet**: Biblioteket støtter flere dype læringsrammeverk, inkludert PyTorch, TensorFlow og JAX. Dette lar deg trene en modell i ett rammeverk og bruke den i et annet.

3. **Multimodale evner**: I tillegg til NLP støtter Hugging Face Transformers også oppgaver innen datamaskinsyn (f.eks. bildeklassifisering, objektgjenkjenning) og lydprosessering (f.eks. talegjenkjenning, lydklassifisering).

4. **Brukervennlighet**: Biblioteket tilbyr APIer og verktøy for enkel nedlasting og finjustering av modeller, noe som gjør det tilgjengelig både for nybegynnere og eksperter.

5. **Fellesskap og ressurser**: Hugging Face har et levende fellesskap og omfattende dokumentasjon, veiledninger og guider for å hjelpe brukere i gang og få mest mulig ut av biblioteket.
[offisiell dokumentasjon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest brukte metoden, men den krever også GPU-akselerasjon. Scenarioer som Vision og MoE krever mye beregning, noe som vil være svært tregt på CPU dersom det ikke er kvantifisert.


- Demo: Bruke Transformer for å kalle Phi-3.5-Instruct [Klikk på denne lenken](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-Vision [Klikk på denne lenken](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-MoE [Klikk på denne lenken](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en plattform designet for å gjøre det enklere å kjøre store språkmodeller (LLM-er) lokalt på maskinen din. Den støtter ulike modeller som Llama 3.1, Phi 3, Mistral, og Gemma 2, blant andre. Plattformen forenkler prosessen ved å samle modellvekter, konfigurasjon og data i én pakke, noe som gjør det mer tilgjengelig for brukere å tilpasse og lage sine egne modeller. Ollama er tilgjengelig for macOS, Linux og Windows. Det er et flott verktøy hvis du ønsker å eksperimentere med eller distribuere LLM-er uten å være avhengig av skytjenester. Ollama er den mest direkte måten, du trenger bare å kjøre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, på-enheten runtime for å kjøre modeller som Phi helt på egen maskinvare - ingen Azure-abonnement, API-nøkkel eller nettverkstilkobling kreves. Den velger automatisk den beste tilgjengelige utførelsesleverandøren (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, så eksisterende `openai`/Azure AI Inferens SDK-kode kan peke på det med minimale endringer. Se [Foundry Local-dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Eller bruk SDK-en direkte i Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en tverrplattform inferens- og treningsakselerator for maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftfullt verktøy som hjelper deg å kjøre generative AI-modeller effektivt på ulike plattformer.

## Hva er ONNX Runtime?
ONNX Runtime er et open source-prosjekt som muliggjør høyytelses inferens av maskinlæringsmodeller. Det støtter modeller i Open Neural Network Exchange (ONNX)-format, som er en standard for representasjon av maskinlæringsmodeller. ONNX Runtime inferens kan muliggjøre raskere kundeopplevelser og lavere kostnader, og støtter modeller fra dype læringsrammeverk som PyTorch og TensorFlow/Keras samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost, osv. ONNX Runtime er kompatibel med ulike maskinvare, drivere og operativsystemer, og gir optimal ytelse ved å utnytte maskinvareakseleratorer der det er mulig sammen med graf optimaliseringer og transformasjoner.

## Hva er generativ AI?
Generativ AI refererer til AI-systemer som kan generere nytt innhold, som tekst, bilder eller musikk, basert på dataene de er trent på. Eksempler inkluderer språkmodeller som GPT-3 og bilde-generasjonsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket gir den generative AI løkken for ONNX-modeller, inkludert inferens med ONNX Runtime, logitsbehandling, søk og sampling, samt KV-cachehåndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI utvider mulighetene til ONNX Runtime for å støtte generative AI-modeller. Her er noen hovedfunksjoner:

- **Bred plattformstøtte:** Den fungerer på ulike plattformer, inkludert Windows, Linux, macOS, Android og iOS.
- **Modellstøtte:** Den støtter mange populære generative AI-modeller, som LLaMA, GPT-Neo, BLOOM, og flere.
- **Ytelsesoptimalisering:** Den inkluderer optimaliseringer for forskjellige maskinvareakseleratorer som NVIDIA GPUer, AMD GPUer og mer2.
- **Brukervennlighet:** Den tilbyr API-er for enkel integrering i applikasjoner, slik at du kan generere tekst, bilder og annet innhold med minimal kode.
- Brukere kan kalle en høy-nivå generate()-metode, eller kjøre hver iterasjon av modellen i en løkke, generere ett token om gangen, og eventuelt oppdatere generasjonsparametere innad i løkken.
- ONNX runtime har også støtte for greedy/beam search og TopP, TopK sampling for å generere token-sekvenser og innebygd logitsbehandling som repeterende straffer. Du kan også enkelt legge til egendefinert poenggiving.

## Komme i gang
For å komme i gang med ONNX Runtime for GENAI kan du følge disse trinnene:

### Installer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installer utvidelsene for Generativ AI:
```Python
pip install onnxruntime-genai
```

### Kjør en modell: Her er et enkelt eksempel i Python:
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
### Demo: Bruke ONNX Runtime GenAI for å kalle Phi-3.5-Vision


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

I tillegg til referansemetodene ONNX Runtime, Ollama og Foundry Local kan vi også fullføre referansen til kvantitative modeller basert på modellreferansemetoder levert av ulike produsenter. For eksempel Apple MLX-rammeverk med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også få mer innhold fra [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lært det grunnleggende om Phi-3/3.5-familien, men for å lære mer om SLM trenger vi mer kunnskap. Du kan finne svarene i Phi-3 Cookbook. Hvis du ønsker å lære mer, vennligst besøk [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->