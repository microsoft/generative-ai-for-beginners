# Introduksjon til små språkmodeller for generativ AI for nybegynnere
Generativ AI er et fascinerende felt innen kunstig intelligens som fokuserer på å skape systemer som kan generere nytt innhold. Dette innholdet kan variere fra tekst og bilder til musikk og til og med hele virtuelle miljøer. En av de mest spennende bruksområdene for generativ AI er innen området språkmodeller.

## Hva er små språkmodeller?

En liten språkmodell (SLM) er en nedskalert variant av en stor språkmodell (LLM), som bruker mange av de arkitektoniske prinsippene og teknikkene fra LLM-er, samtidig som den har et betydelig redusert beregningsavtrykk.

SLM-er er en undergruppe av språkmodeller designet for å generere menneskelignende tekst. I motsetning til deres større motstykker, som GPT-4, er SLM-er mer kompakte og effektive, noe som gjør dem ideelle for applikasjoner der beregningsressurser er begrensede. Til tross for den mindre størrelsen kan de fortsatt utføre en rekke oppgaver. Vanligvis bygges SLM-er ved å komprimere eller destillere LLM-er, med mål om å beholde en vesentlig del av den originale modellens funksjonalitet og språklige evner. Denne reduksjonen i modellstørrelse reduserer den generelle kompleksiteten, noe som gjør SLM-er mer effektive både når det gjelder minnebruk og beregningsbehov. Til tross for disse optimaliseringene kan SLM-er fortsatt utføre et bredt spekter av oppgaver innen naturlig språkbehandling (NLP):

- Tekstgenerering: Lage koherente og kontekstuelt relevante setninger eller avsnitt.
- Tekstfullføring: Forutsi og fullføre setninger basert på en gitt prompt.
- Oversettelse: Konvertere tekst fra ett språk til et annet.
- Oppsummering: Kondensering av lange tekster til kortere, mer lettfordøyelige sammendrag.

Selv om det kan innebære noen kompromisser i ytelse eller dybde av forståelse sammenlignet med deres større motstykker.

## Hvordan fungerer små språkmodeller?
SLM-er trenes på store mengder tekstdata. Under treningen lærer de mønstrene og strukturene i språket, noe som gjør dem i stand til å generere tekst som både er grammatisk korrekt og kontekstuelt passende. Treningsprosessen involverer:

- Datainnsamling: Samle store tekstdatasett fra ulike kilder.
- Forbehandling: Rengjøre og organisere dataene slik at de blir egnet for trening.
- Trening: Bruke maskinlæringsalgoritmer for å lære modellen å forstå og generere tekst.
- Finjustering: Justere modellen for å forbedre ytelsen på spesifikke oppgaver.

Utviklingen av SLM-er samsvarer med det økende behovet for modeller som kan distribueres i ressursbegrensede miljøer, som mobile enheter eller edge computing-plattformer, hvor fullskala LLM-er kan være upraktiske på grunn av deres store ressursbehov. Ved å fokusere på effektivitet balanserer SLM-er ytelse med tilgjengelighet, noe som muliggjør bredere anvendelse på tvers av ulike domener.

![slm](../../../translated_images/no/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Læringsmål

I denne leksjonen håper vi å introdusere kunnskapen om SLM og kombinere den med Microsoft Phi-3 for å lære ulike scenarier innen tekstinnhold, visjon og MoE.

Ved slutten av denne leksjonen bør du kunne svare på følgende spørsmål:

- Hva er SLM?
- Hva er forskjellen mellom SLM og LLM?
- Hva er Microsoft Phi-3/3.5-familien?
- Hvordan kjøre inferens med Microsoft Phi-3/3.5-familien?

Klar? La oss komme i gang.

## Forskjellene mellom store språkmodeller (LLM) og små språkmodeller (SLM)

Både LLM-er og SLM-er er bygget på grunnleggende prinsipper innen probabilistisk maskinlæring, og følger lignende tilnærminger i sin arkitektoniske utforming, treningsmetodikk, datagenereringsprosesser og modelevalueringsmetoder. Imidlertid skiller flere nøkkelfaktorer disse to typene modeller.

## Bruksområder for små språkmodeller

SLM-er har et bredt spekter av bruksområder, inkludert:

- Chatboter: Gi kundestøtte og engasjere brukere i en samtalebasert interaksjon.
- Innholdsskaping: Assistere forfattere ved å generere ideer eller til og med utarbeide hele artikler.
- Utdanning: Hjelpe studenter med skriveoppgaver eller å lære nye språk.
- Tilgjengelighet: Lage verktøy for personer med funksjonshemminger, som tekst-til-tale systemer.

**Størrelse**
  
En hovedforskjell mellom LLM-er og SLM-er ligger i modellens skala. LLM-er, som ChatGPT (GPT-4), kan bestå av anslagsvis 1,76 billioner parametere, mens åpne SLM-er som Mistral 7B er designet med betydelig færre parametere — omtrent 7 milliarder. Denne forskjellen skyldes hovedsakelig ulikheter i arkitektur og treningsprosesser. For eksempel benytter ChatGPT en selvoppmerksomhetsmekanisme innenfor en encoder-decoder-ramme, mens Mistral 7B bruker glidende vindu-oppmerksomhet, som muliggjør mer effektiv trening innen en ren decoder-modell. Denne arkitektoniske variasjonen har store implikasjoner for modellens kompleksitet og ytelse.

**Forståelse**

SLM-er er vanligvis optimalisert for ytelse innen spesifikke domener, noe som gjør dem svært spesialiserte, men potensielt begrenset i evnen til å gi bred kontekstuell forståelse på tvers av flere kunnskapsfelt. I kontrast søker LLM-er å simulere menneskelig intelligens på et mer omfattende nivå. Trenet på store, mangfoldige datasett, er LLM-er designet for å prestere godt på tvers av mange domener, og tilbyr større allsidighet og tilpasningsevne. Følgelig er LLM-er mer egnet for et bredere utvalg av videre oppgaver, som naturlig språkbehandling og programmering.

**Beregning**

Trening og utrulling av LLM-er er ressurskrevende prosesser, som ofte krever betydelig beregningsinfrastruktur, inkludert storstilte GPU-klynger. For eksempel kan trening av en modell som ChatGPT fra bunnen av kreve tusenvis av GPU-er over lange perioder. I kontrast er SLM-er, med sine mindre parametertall, mer tilgjengelige når det gjelder beregningsressurser. Modeller som Mistral 7B kan trenes og kjøres på lokale maskiner utstyrt med moderate GPU-kapasiteter, selv om trening fortsatt krever flere timer på tvers av flere GPU-er.

**Bias**

Bias er et kjent problem i LLM-er, hovedsakelig på grunn av naturen til treningsdataene. Disse modellene baserer seg ofte på rå, åpent tilgjengelige data fra internett, som kan underrepresentere eller feilrepresentere visse grupper, introdusere feilaktig merking, eller gjenspeile språklige skjevheter påvirket av dialekter, geografiske variasjoner og grammatikkregler. I tillegg kan kompleksiteten i LLM-arkitekturene utilsiktet forsterke bias, som kan gå ubemerket hen uten nøye finjustering. På den annen side, trenes SLM-er på mer begrensede, domenespesifikke datasett, og er derfor iboende mindre utsatt for slike skjevheter, selv om de ikke er immune.

**Inferens**

Den reduserte størrelsen på SLM-er gir dem en betydelig fordel i form av inferenshastighet, noe som tillater rask generering av utdata på lokal maskinvare uten behov for omfattende parallellbehandling. I kontrast krever LLM-er, på grunn av sin størrelse og kompleksitet, ofte betydelige parallellberegningsressurser for å oppnå akseptable inferenstider. Tilstedeværelsen av flere samtidige brukere øker ytterligere LLM-ers responstid, spesielt ved storskala utrulling.

Oppsummert, selv om både LLM-er og SLM-er deler en grunnleggende basis i maskinlæring, skiller de seg betydelig hva gjelder modellstørrelse, ressursbehov, kontekstuell forståelse, utsatthet for bias og inferenshastighet. Disse forskjellene gjenspeiler deres respektive egnethet for ulike bruksområder, der LLM-er er mer allsidige, men ressurskrevende, mens SLM-er tilbyr mer domene-spesifikk effektivitet med redusert beregningsbehov.

***Merk: I denne leksjonen vil vi introdusere SLM ved hjelp av Microsoft Phi-3 / 3.5 som eksempel.***

## Introduksjon til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien retter seg hovedsakelig mot tekst-, visjons- og agent (MoE) applikasjonsscenarier:

### Phi-3 / 3.5 Instruct

Hovedsakelig for tekstgenerering, chatfullføring og innholdsinformasjonsekstraksjon osv.

**Phi-3-mini**

Språkmodellen på 3,8 milliarder parametere er tilgjengelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modellene presterer betydelig bedre enn språkmodeller av lik eller større størrelse på viktige benchmarks (se benchmark-tall nedenfor, høyere tall er bedre). Phi-3-mini presterer bedre enn modeller dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inkludert GPT-3.5.

**Phi-3-small & medium**

Med bare 7 milliarder parametere slår Phi-3-small GPT-3.5T på en rekke språk-, resonnement-, koding- og matematikkbenchmarks.

Phi-3-medium med 14 milliarder parametere fortsetter denne trenden og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan tenke på den som en oppgradering av Phi-3-mini. Selv om parameterne forblir uendret, forbedrer den evnen til å støtte flere språk (støtter 20+ språk: arabisk, kinesisk, tsjekkisk, dansk, nederlandsk, engelsk, finsk, fransk, tysk, hebraisk, ungarsk, italiensk, japansk, koreansk, norsk, polsk, portugisisk, russisk, spansk, svensk, thai, tyrkisk, ukrainsk) og tilfører sterkere støtte for lang kontekst.

Phi-3.5-mini med 3,8 milliarder parametere overgår språkmodeller av samme størrelse og er på nivå med modeller dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan tenke på Instruct-modellen til Phi-3/3.5 som Phis evne til å forstå, og Vision er det som gir Phi øyne til å forstå verden.


**Phi-3-Vision**

Phi-3-vision, med kun 4,2 milliarder parametere, fortsetter denne trenden og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle resonnementoppgaver, OCR, samt bord- og diagramforståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en oppgradering av Phi-3-Vision, som legger til støtte for flere bilder. Du kan se på det som en forbedring innen visjon; ikke bare kan du se bilder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash på OCR, bord- og diagramforståelsesoppgaver, og er på nivå med dem på generelle visuelle kunnskapsresonnementoppgaver. Støtter multi-frame input, altså evnen til å gjøre resonnement på flere input-bilder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gjør det mulig å trene modeller med langt mindre beregning, som betyr at du dramatisk kan skalere opp modell- eller datasettstørrelsen med samme beregningsbudsjett som en tett modell. Spesielt bør en MoE-modell oppnå samme kvalitet som sin tette motpart mye raskere under fortrening.

Phi-3.5-MoE består av 16x3,8 milliarder ekspertmoduler. Phi-3.5-MoE med bare 6,6 milliarder aktive parametere oppnår et lignende nivå av resonnement, språkforståelse og matematikk som mye større modeller.

Vi kan bruke Phi-3/3.5-familien basert på forskjellige scenarier. I motsetning til LLM, kan du distribuere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheter.


## Hvordan bruke Phi-3/3.5-familie-modeller

Vi håper å bruke Phi-3/3.5 i forskjellige scenarier. Neste steg er å bruke Phi-3/3.5 basert på ulike scenarier.

![phi3](../../../translated_images/no/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens via sky-APIer

**Microsoft Foundry Modeller**

> **Merk:** GitHub Models avvikles ved slutten av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatningen.

Microsoft Foundry Models er den mest direkte måten. Du kan raskt få tilgang til Phi-3/3.5-Instruct-modellen gjennom Foundry-modellkatalogen. Kombinert med Azure AI Inference SDK / OpenAI SDK kan du tilgå API'et via kode for å fullføre Phi-3/3.5-Instruct-kall. Du kan også teste ulike effekter gjennom Playground.

- Demo: Sammenligning av effektene til Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/no/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/no/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Eller hvis vi vil bruke visjons- og MoE-modeller, kan du bruke Microsoft Foundry for å fullføre kallet. Hvis du er interessert, kan du lese Phi-3 Cookbook for å lære hvordan du kaller Phi-3/3.5 Instruct, Vision, MoE gjennom Microsoft Foundry [Klikk denne lenken](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

I tillegg til den skybaserte Microsoft Foundry Models-katalogen kan du også bruke [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) for å fullføre relevante kall. Du kan besøke NVIDIA NIM for å fullføre API-kallene til Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er en samling akselererte inferenstjenester designet for å hjelpe utviklere med å distribuere AI-modeller effektivt på tvers av ulike miljøer, inkludert skyer, datasentre og arbeidsstasjoner.

Her er noen viktige funksjoner ved NVIDIA NIM:

- **Enkel distribusjon:** NIM tillater distribusjon av AI-modeller med en enkelt kommando, noe som gjør det enkelt å integrere i eksisterende arbeidsflyter.
- **Optimalisert ytelse:** Det utnytter NVIDIA sine forhåndsoptimaliserte inferensmotorer, som TensorRT og TensorRT-LLM, for å sikre lav ventetid og høy gjennomstrømning.
- **Skalerbarhet:** NIM støtter automatisk skalering på Kubernetes, noe som gjør det i stand til å håndtere varierende arbeidsmengder effektivt.
- **Sikkerhet og kontroll:** Organisasjoner kan opprettholde kontroll over sine data og applikasjoner ved å selv-hoste NIM-mikrotjenester på egen administrert infrastruktur.
- **Standard API-er:** NIM tilbyr bransjestandard API-er, noe som gjør det enkelt å bygge og integrere AI-applikasjoner som chatbots, AI-assistenter og mer.

NIM er en del av NVIDIA AI Enterprise, som har som mål å forenkle distribusjon og operationalisering av AI-modeller, og sikre at de kjører effektivt på NVIDIA GPU-er.

- Demo: Bruke NVIDIA NIM for å kalle Phi-3.5-Vision-API [[Klikk på denne lenken](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kjøre Phi-3/3.5 lokalt
Inference i forhold til Phi-3, eller enhver språkmodell som GPT-3, refererer til prosessen med å generere svar eller prediksjoner basert på input den mottar. Når du gir et prompt eller spørsmål til Phi-3, bruker den sitt trente nevrale nettverk for å inferere det mest sannsynlige og relevante svaret ved å analysere mønstre og relasjoner i dataene den ble trent på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftig bibliotek designet for naturlig språkprosessering (NLP) og andre maskinlæringsoppgaver. Her er noen nøkkelpunkter om det:

1. **Fortrente modeller**: Det tilbyr tusenvis av fortrente modeller som kan brukes til ulike oppgaver som tekstklassifisering, navngitt entity-gjenkjenning, spørsmål-og-svar, oppsummering, oversettelse og tekstgenerering.

2. **Rammeverksinteroperabilitet**: Biblioteket støtter flere dyplæringsrammeverk, inkludert PyTorch, TensorFlow og JAX. Dette gjør at du kan trene en modell i ett rammeverk og bruke den i et annet.

3. **Multimodale egenskaper**: I tillegg til NLP støtter Hugging Face Transformers også oppgaver innen datavisjon (f.eks. bildeklassifisering, objektdeteksjon) og lydbehandling (f.eks. talegjenkjenning, lydklassifisering).

4. **Brukervennlighet**: Biblioteket tilbyr API-er og verktøy for enkelt å laste ned og finjustere modeller, noe som gjør det tilgjengelig for både nybegynnere og eksperter.

5. **Fellesskap og ressurser**: Hugging Face har et levende fellesskap og omfattende dokumentasjon, opplæringsprogrammer og veiledninger for å hjelpe brukere komme i gang og utnytte biblioteket best mulig.
[offisiell dokumentasjon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repositorium](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest brukte metoden, men den krever også GPU-akselerasjon. Scenarioer som Vision og MoE krever mye beregninger, som vil være veldig tregt på CPU hvis modellene ikke er kvantiserte.


- Demo: Bruke Transformer for å kalle Phi-3.5-Instruct [Klikk på denne lenken](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-Vision [Klikk på denne lenken](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-MoE [Klikk på denne lenken](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en plattform designet for å gjøre det enklere å kjøre store språkmodeller (LLMs) lokalt på maskinen din. Den støtter flere modeller som Llama 3.1, Phi 3, Mistral og Gemma 2, blant andre. Plattformen forenkler prosessen ved å samle modellvekter, konfigurasjon og data i en enkelt pakke, noe som gjør det mer tilgjengelig for brukere å tilpasse og lage egne modeller. Ollama er tilgjengelig for macOS, Linux og Windows. Det er et flott verktøy hvis du ønsker å eksperimentere med eller distribuere LLM-er uten å være avhengig av skytjenester. Ollama er den mest direkte måten, du trenger bare å kjøre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, på-enheten runtime for å kjøre modeller som Phi helt på ditt eget maskinvare - ingen Azure-abonnement, API-nøkkel eller nettverkstilkobling kreves. Den velger automatisk den beste tilgjengelige kjøreleverandøren (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, slik at eksisterende `openai`/Azure AI Inference SDK-kode kan peke på det med minimale endringer. Se [Foundry Local dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en plattformuavhengig akselerator for inferens og trening av maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftig verktøy som hjelper deg med å kjøre generative AI-modeller effektivt på tvers av ulike plattformer.

## Hva er ONNX Runtime?
ONNX Runtime er et åpen kildekode prosjekt som muliggjør høyytelses-inferens av maskinlæringsmodeller. Det støtter modeller i Open Neural Network Exchange (ONNX)-format, som er en standard for representasjon av maskinlæringsmodeller. ONNX Runtime-inferens kan muliggjøre raskere kundeopplevelser og lavere kostnader, og støtter modeller fra dyplæringsrammeverk som PyTorch og TensorFlow/Keras, samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost, osv. ONNX Runtime er kompatibel med ulike maskinvare, drivere og operativsystemer, og gir optimal ytelse ved å utnytte maskinvareakseleratorer der det er mulig, sammen med grafoptimaliseringer og transformasjoner.

## Hva er Generativ AI?
Generativ AI refererer til AI-systemer som kan generere nytt innhold, som tekst, bilder eller musikk, basert på dataene de er trent på. Eksempler inkluderer språkmodeller som GPT-3 og bildegenereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket gir den generative AI-løkken for ONNX-modeller, inkludert inferens med ONNX Runtime, logits-behandling, søk og sampling, samt KV cache-administrasjon.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI utvider kapasitetene til ONNX Runtime for å støtte generative AI-modeller. Her er noen nøkkelfunksjoner:

- **Bred plattformstøtte:** Den fungerer på ulike plattformer, inkludert Windows, Linux, macOS, Android og iOS.
- **Modellstøtte:** Den støtter mange populære generative AI-modeller, som LLaMA, GPT-Neo, BLOOM og flere.
- **Ytelsesoptimalisering:** Den inkluderer optimaliseringer for ulike maskinvareakseleratorer som NVIDIA GPU-er, AMD GPU-er og mer2.
- **Brukervennlighet:** Den tilbyr API-er for enkel integrasjon i applikasjoner, som lar deg generere tekst, bilder og annet innhold med minimal kode.
- Brukere kan kalle en høynivå generate()-metode, eller kjøre hver iterasjon av modellen i en løkke, generere ett token om gangen, og eventuelt oppdatere generasjonsparametere inne i løkken.
- ONNX runtime har også støtte for greedy/beam-søk og TopP, TopK sampling for å generere token-sekvenser og innebygd logits-behandling som repeteringsstraff. Du kan også enkelt legge til egen scoring.

## Komme i gang
For å komme i gang med ONNX Runtime for GENAI, kan du følge disse stegene:

### Installer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installer Generative AI Extensions:
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

I tillegg til ONNX Runtime, Ollama og Foundry Local referansemetoder, kan vi også fullføre referansen for kvantitative modeller basert på modellreferansemetodene som tilbys av forskjellige produsenter. Som Apple MLX-rammeverket med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU osv. Du kan også få mer innhold fra [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lært det grunnleggende om Phi-3/3.5-familien, men for å lære mer om SLM trenger vi mer kunnskap. Du kan finne svarene i Phi-3 Cookbook. Hvis du vil lære mer, vennligst besøk [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->