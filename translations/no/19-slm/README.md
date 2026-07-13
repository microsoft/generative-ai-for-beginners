# Introduksjon til Små Språkmodeller for Generativ AI for Nybegynnere
Generativ AI er et fascinerende felt innen kunstig intelligens som fokuserer på å skape systemer som kan generere nytt innhold. Dette innholdet kan variere fra tekst og bilder til musikk og til og med hele virtuelle miljøer. En av de mest spennende anvendelsene av generativ AI er innen språkteknologier.

## Hva er Små Språkmodeller?

En Små Språkmodell (SLM) representerer en nedskalert variant av en stor språkmodell (LLM), som utnytter mange av de arkitektoniske prinsippene og teknikkene fra LLM-er, samtidig som den viser et betydelig redusert beregningsavtrykk.

SLM-er er en undergruppe av språkmodeller designet for å generere menneskelignende tekst. I motsetning til sine større motparter, som GPT-4, er SLM-er mer kompakte og effektive, noe som gjør dem ideelle for applikasjoner hvor beregningsressursene er begrenset. Til tross for deres mindre størrelse, kan de fortsatt utføre en rekke oppgaver. Vanligvis bygges SLM-er ved å komprimere eller destillere LLM-er, med mål om å beholde en betydelig del av den opprinnelige modellens funksjonalitet og språklige evner. Denne reduksjonen i modellstørrelse minsker den totale kompleksiteten, noe som gjør SLM-er mer effektive både når det gjelder minnebruk og beregningsbehov. Til tross for disse optimaliseringene, kan SLM-er fortsatt utføre et bredt spekter av oppgaver innen naturlig språkbehandling (NLP):

- Tekstgenerering: Lage sammenhengende og kontekstuelt relevante setninger eller avsnitt.
- Tekstfullføring: Forutsi og fullføre setninger basert på et gitt startpunkt.
- Oversettelse: Oversette tekst fra ett språk til et annet.
- Oppsummering: Komprimere lange tekster til kortere, mer fordøyelige sammendrag.

Dog med noen kompromisser i ytelse eller dybde i forståelsen sammenlignet med sine større motparter.

## Hvordan Fungerer Små Språkmodeller?
SLM-er trenes på store mengder tekstdata. Under treningen lærer de mønstre og strukturer i språket, noe som gjør dem i stand til å generere tekst som både er grammatisk korrekt og kontekstuelt passende. Treningsprosessen involverer:

- Datainnsamling: Samle store datasett med tekst fra ulike kilder.
- Forbehandling: Renske og organisere dataene for å gjøre dem egnet for trening.
- Trening: Bruke maskinlæringsalgoritmer for å lære modellen å forstå og generere tekst.
- Finjustering: Justere modellen for å forbedre ytelsen på spesifikke oppgaver.

Utviklingen av SLM-er samsvarer med det økende behovet for modeller som kan distribueres i ressursbegrensede miljøer, som mobile enheter eller edge computing-plattformer, hvor fullskala LLM-er kan være upraktiske på grunn av høye ressurskrav. Ved å fokusere på effektivitet balanserer SLM-er ytelse med tilgjengelighet, noe som muliggjør bredere anvendelse på tvers av ulike domener.

![slm](../../../translated_images/no/slm.4058842744d0444a.webp)

## Læringsmål

I denne leksjonen håper vi å introdusere kunnskapen om SLM og kombinere den med Microsoft Phi-3 for å lære ulike scenarier innen tekstinnhold, visjon og MoE.

Ved slutten av denne leksjonen skal du kunne svare på følgende spørsmål:

- Hva er SLM?
- Hva er forskjellen mellom SLM og LLM?
- Hva er Microsoft Phi-3/3.5-familien?
- Hvordan kjøre inferens med Microsoft Phi-3/3.5-familien?

Klar? La oss komme i gang.

## Forskjellene mellom Store Språkmodeller (LLMs) og Små Språkmodeller (SLMs)

Både LLM-er og SLM-er er basert på grunnleggende prinsipper innen probabilistisk maskinlæring, og følger lignende tilnærminger i sin arkitektoniske utforming, treningsmetodikker, datagenereringsprosesser og modellvurderingsteknikker. Flere nøkkelfaktorer skiller likevel disse to modelltypene.

## Anvendelser av Små Språkmodeller

SLM-er har et bredt spekter av bruksområder, inkludert:

- Chatbots: Gi kundesupport og engasjere brukere i en samtalemåte.
- Innholdsskaping: Assistere forfattere ved å generere ideer eller til og med utforme hele artikler.
- Utdanning: Hjelpe studenter med skriveoppgaver eller å lære nye språk.
- Tilgjengelighet: Lage verktøy for personer med funksjonshemminger, som tekst-til-tale-systemer.

**Størrelse**
  
En hovedforskjell mellom LLM-er og SLM-er ligger i modellens skala. LLM-er, som ChatGPT (GPT-4), kan omfatte anslagsvis 1,76 billioner parametere, mens åpne SLM-er som Mistral 7B er designet med betydelig færre parametere—omtrent 7 milliarder. Denne forskjellen skyldes hovedsakelig ulikheter i modellarkitektur og treningsprosesser. For eksempel benytter ChatGPT en selvoppmerksomhetsmekanisme innenfor et encoder-decoder-rammeverk, mens Mistral 7B bruker sliding window attention, som muliggjør mer effektiv trening innen en kun decoder-basert modell. Denne arkitektoniske variasjonen har dype implikasjoner for modellens kompleksitet og ytelse.

**Forståelse**

SLM-er er typisk optimalisert for ytelse innen spesifikke domener, noe som gjør dem høyt spesialiserte, men potensielt begrensede i deres evne til å gi bred kontekstuell forståelse på tvers av flere kunnskapsfelt. I kontrast søker LLM-er å simulere menneskelignende intelligens på et mer omfattende nivå. Trenede på store, varierte datasett, er LLM-er designet for å fungere bra på tvers av ulike domener, og tilbyr større allsidighet og tilpasningsevne. Derfor egner LLM-er seg bedre for et bredere spekter av etterfølgende oppgaver, som naturlig språkbehandling og programmering.

**Beregning**

Treningen og implementeringen av LLM-er krever store ressurser, ofte betydelig datainfrastruktur, inkludert store GPU-klynger. For eksempel kan trening av en modell som ChatGPT fra bunnen av kreve tusenvis av GPU-er over lengre perioder. I kontrast er SLM-er, med sine færre parametere, mer tilgjengelige når det gjelder beregningsressurser. Modeller som Mistral 7B kan trenes og kjøres på lokale maskiner med moderate GPU-kapasiteter, selv om trening fremdeles kan kreve flere timer på tvers av flere GPU-er.

**Skjevhet**

Skjevhet er et kjent problem i LLM-er, hovedsakelig på grunn av treningsdataenes natur. Disse modellene baserer seg ofte på rå, fritt tilgjengelig data fra internett, som kan underrepresentere eller feilrepresentere visse grupper, introdusere feilaktig merking eller reflektere språklige skjevheter påvirket av dialekter, geografiske variasjoner og grammatikkregler. I tillegg kan kompleksiteten i LLM-arkitekturer utilsiktet forsterke skjevheter, som kanskje ikke oppdages uten nøye finjustering. På den annen side, siden SLM-er trenes på mer avgrensede, domene-spesifikke datasett, er de iboende mindre utsatt for slike skjevheter, men er ikke immune mot dem.

**Inferens**

Den reduserte størrelsen på SLM-er gir dem en betydelig fordel når det gjelder inferenshastighet, noe som gjør at de kan generere utdata effektivt på lokal maskinvare uten behov for omfattende parallellbehandling. I kontrast krever LLM-er, på grunn av størrelse og kompleksitet, ofte betydelige parallelle beregningsressurser for å oppnå akseptable inferenstider. Tilstedeværelsen av flere samtidige brukere senker også responstidene for LLM-er, spesielt ved storskala distribusjon.

Oppsummert, selv om både LLM-er og SLM-er deler en grunnleggende basis i maskinlæring, skiller de seg betydelig når det gjelder modellstørrelse, ressursbehov, kontekstuell forståelse, mottakelighet for skjevhet og inferenshastighet. Disse forskjellene reflekterer deres egnethet for ulike bruksområder, der LLM-er er mer allsidige, men ressurskrevende, mens SLM-er tilbyr mer domene-spesifikk effektivitet med redusert beregningsbehov.

***Merk: I denne leksjonen vil vi introdusere SLM ved bruk av Microsoft Phi-3 / 3.5 som eksempel.***

## Introduksjon til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien retter seg hovedsakelig mot tekst-, visjons- og Agent (MoE) applikasjonsscenarier:

### Phi-3 / 3.5 Instruct

Hovedsakelig for tekstgenerering, fullføring av chat og innholdsinformasjonsekstraksjon, osv.

**Phi-3-mini**

3,8B språkmodellen er tilgjengelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modellene presterer betydelig bedre enn språkmodeller med lik eller større størrelse på viktige benchmark-tester (se benchmark-tall under, høyere tall er bedre). Phi-3-mini overgår modeller dobbelt så store, mens Phi-3-small og Phi-3-medium overgår større modeller, inkludert GPT-3.5.

**Phi-3-small & medium**

Med bare 7B parametere slår Phi-3-small GPT-3.5T på en rekke språk-, resonnerings-, koding- og matematikk-benchmark-tester.

Phi-3-medium med 14B parametere fortsetter denne trenden og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan se på den som en oppgradering av Phi-3-mini. Selv om parametertallet forblir uendret, forbedrer den evnen til å støtte flere språk (støtter 20+ språk: Arabisk, Kinesisk, Tsjekkisk, Dansk, Nederlandsk, Engelsk, Finsk, Fransk, Tysk, Hebraisk, Ungarsk, Italiensk, Japansk, Koreansk, Norsk, Polsk, Portugisisk, Russisk, Spansk, Svensk, Thai, Tyrkisk, Ukrainsk) og legger til sterkere støtte for lang kontekst.

Phi-3.5-mini med 3,8B parametere overgår språkmodeller av samme størrelse og er på nivå med modeller dobbelt så store.

### Phi-3 / 3.5 Vision

Vi kan tenke på Instruct-modellen til Phi-3/3.5 som Phis evne til å forstå, og Vision er det som gir Phi øyne til å forstå verden.


**Phi-3-Vision**

Phi-3-vision, med bare 4,2B parametere, fortsetter denne trenden og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle resonneringsoppgaver, OCR-oppgaver og tabell- og diagramforståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en oppgradering av Phi-3-Vision, som legger til støtte for flere bilder. Du kan tenke på det som en forbedring i syn, ikke bare kan du se bilder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash på OCR-, tabell- og diagramforståelse, og er på nivå med generelle oppgaver innen visuell kunnskapsresonnering. Støtter multi-frame input, det vil si resonnering på flere inndata-bilder


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gjør det mulig for modeller å forhåndstrenes med mye mindre datakraft, noe som betyr at du drastisk kan skalere opp modell- eller datasettstørrelsen med samme beregningsbudsjett som en tett modell. Spesielt bør en MoE-modell oppnå samme kvalitet som sin tette motpart mye raskere under forhåndstreningen.

Phi-3.5-MoE består av 16x3,8B ekspertmoduler. Phi-3.5-MoE med bare 6,6B aktive parametere oppnår liknende nivåer av resonnering, språkforståelse og matematikk som mye større modeller.

Vi kan bruke Phi-3/3.5-familien basert på ulike scenarier. I motsetning til LLM kan du distribuere Phi-3/3.5-mini eller Phi-3/3.5-Vision på edge-enheter.


## Hvordan bruke Phi-3/3.5-familie modeller

Vi håper å bruke Phi-3/3.5 i forskjellige scenarier. Neste skal vi bruke Phi-3/3.5 basert på ulike scenarier.

![phi3](../../../translated_images/no/phi3.655208c3186ae381.webp)

### Inferens via Cloud API-er

**Microsoft Foundry Models**

> **Merk:** GitHub Models avvikles ved slutten av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er direkte erstatning.

Microsoft Foundry Models er den mest direkte måten. Du kan raskt få tilgang til Phi-3/3.5-Instruct-modellen gjennom Foundry modellkatalogen. Kombinert med Azure AI Inference SDK / OpenAI SDK, kan du få tilgang til API-en via kode for å fullføre Phi-3/3.5-Instruct-kall. Du kan også teste ulike effekter via Playground.

- Demo: Sammenligning av effektene til Phi-3-mini og Phi-3.5-mini i kinesiske scenarier

![phi3](../../../translated_images/no/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/no/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Eller hvis vi vil bruke visjons- og MoE-modeller, kan du bruke Microsoft Foundry for å fullføre kallet. Hvis du er interessert, kan du lese Phi-3 Cookbook for å lære hvordan du ringer Phi-3/3.5 Instruct, Vision, MoE via Microsoft Foundry [Klikk denne linken](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

I tillegg til den skybaserte Microsoft Foundry Models-katalogen, kan du også bruke [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) for å fullføre relaterte kall. Du kan besøke NVIDIA NIM for å utføre API-kall til Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sett akselererte inferenstjenester designet for å hjelpe utviklere med å distribuere AI-modeller effektivt på tvers av ulike miljøer, inkludert skyer, datasentre og arbeidsstasjoner.

Her er noen viktige funksjoner ved NVIDIA NIM:

- **Enkel Distribusjon:** NIM tillater distribusjon av AI-modeller med en enkelt kommando, noe som gjør det enkelt å integrere i eksisterende arbeidsflyter.

- **Optimalisert ytelse:** Den utnytter NVIDIAs forhåndsoptimaliserte inferensmotorer, som TensorRT og TensorRT-LLM, for å sikre lav ventetid og høy gjennomstrømning.
- **Skalerbarhet:** NIM støtter autoskalering på Kubernetes, noe som gjør at den effektivt kan håndtere varierende arbeidsmengder.
- **Sikkerhet og kontroll:** Organisasjoner kan opprettholde kontroll over sine data og applikasjoner ved å kjøre NIM mikrotjenester selv på egen administrert infrastruktur.
- **Standardiserte APIer:** NIM tilbyr bransjestandard APIer, noe som gjør det enkelt å bygge og integrere AI-applikasjoner som chatboter, AI-assistenter og mer.

NIM er en del av NVIDIA AI Enterprise, som har som mål å forenkle implementeringen og driften av AI-modeller, og sikre at de kjører effektivt på NVIDIA GPUer.

- Demo: Bruke NVIDIA NIM for å kalle Phi-3.5-Vision-API [[Klikk på denne lenken](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kjøre Phi-3/3.5 lokalt
Inferens i forhold til Phi-3, eller en hvilken som helst språkmodell som GPT-3, refererer til prosessen med å generere svar eller prediksjoner basert på input den mottar. Når du gir en prompt eller et spørsmål til Phi-3, bruker den sitt trente nevrale nettverk til å slutte seg til det mest sannsynlige og relevante svaret ved å analysere mønstre og relasjoner i dataene den ble trent på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftig bibliotek designet for naturlig språkprosessering (NLP) og andre maskinlæringsoppgaver. Her er noen viktige punkter om det:

1. **Fortrente modeller**: Det tilbyr tusenvis av forhåndstrente modeller som kan brukes til ulike oppgaver som tekstklassifisering, navngitt enhetsgjenkjenning, spørsmål-svar, oppsummering, oversettelse og tekstgenerering.

2. **Rammeverksinteroperabilitet**: Biblioteket støtter flere dype læringsrammeverk, inkludert PyTorch, TensorFlow og JAX. Dette lar deg trene en modell i ett rammeverk og bruke den i et annet.

3. **Multimodale evner**: I tillegg til NLP støtter Hugging Face Transformers også oppgaver innen datavisjon (f.eks. bildeklassifisering, objektgjenkjenning) og lydbehandling (f.eks. talegjenkjenning, lydklassifisering).

4. **Brukervennlighet**: Biblioteket tilbyr APIer og verktøy for å enkelt laste ned og finjustere modeller, noe som gjør det tilgjengelig for både nybegynnere og eksperter.

5. **Fellesskap og ressurser**: Hugging Face har et levende fellesskap og omfattende dokumentasjon, guider og veiledninger for å hjelpe brukere med å komme i gang og få mest mulig ut av biblioteket.
[offisiell dokumentasjon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repositorium](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest brukte metoden, men den krever også GPU-akselerasjon. Scenarioer som Vision og MoE krever tross alt mange beregninger, noe som blir veldig tregt på CPU hvis de ikke er kvantisert.


- Demo: Bruke Transformer for å kalle Phi-3.5-Instruct [Klikk på denne lenken](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-Vision [Klikk på denne lenken](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer for å kalle Phi-3.5-MoE [Klikk på denne lenken](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en plattform designet for å gjøre det enklere å kjøre store språkmodeller (LLMs) lokalt på din maskin. Den støtter ulike modeller som Llama 3.1, Phi 3, Mistral, og Gemma 2, blant andre. Plattformen forenkler prosessen ved å pakke modellvekter, konfigurasjon og data i en enkelt pakke, noe som gjør det mer tilgjengelig for brukere å tilpasse og lage sine egne modeller. Ollama er tilgjengelig for macOS, Linux og Windows. Det er et flott verktøy hvis du ønsker å eksperimentere med eller distribuere LLMer uten å være avhengig av skytjenester. Ollama er den mest direkte veien, du trenger bare å kjøre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, lokale kjøreomgivelse for å kjøre modeller som Phi helt på din egen maskinvare – ingen Azure-abonnement, API-nøkkel eller nettverkstilkobling nødvendig. Den velger automatisk den beste tilgjengelige kjøreleverandøren (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, slik at eksisterende `openai`/Azure AI Inference SDK-kode kan peke til det med minimale endringer. Se [Foundry Local-dokumentasjonen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Eller bruk SDK direkte i Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en kryssplattform for akselerasjon av inferens og trening for maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftig verktøy som hjelper deg å kjøre generative AI-modeller effektivt på tvers av ulike plattformer.

## Hva er ONNX Runtime?
ONNX Runtime er et open source-prosjekt som muliggjør høyytelses inferens av maskinlæringsmodeller. Det støtter modeller i Open Neural Network Exchange (ONNX)-formatet, som er en standard for representasjon av maskinlæringsmodeller. ONNX Runtime-inferens kan muliggjøre raskere kundeopplevelser og lavere kostnader, og støtter modeller fra dype læringsrammeverk som PyTorch og TensorFlow/Keras, samt klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost med flere. ONNX Runtime er kompatibel med ulik maskinvare, drivere og operativsystemer, og gir optimal ytelse ved å utnytte maskinvareakseleratorer der det er mulig, sammen med grafoptimaliseringer og transformasjoner.

## Hva er Generativ AI?
Generativ AI refererer til AI-systemer som kan generere nytt innhold, som tekst, bilder eller musikk, basert på dataene de er trent på. Eksempler inkluderer språkmodeller som GPT-3 og bildegenereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket tilbyr den generative AI-syklusen for ONNX-modeller, inkludert inferens med ONNX Runtime, logitsbehandling, søk og sampling, samt KV-cache-håndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI utvider funksjonaliteten til ONNX Runtime for å støtte generative AI-modeller. Her er noen nøkkelfunksjoner:

- **Bred plattformstøtte:** Den fungerer på ulike plattformer, inkludert Windows, Linux, macOS, Android og iOS.
- **Modellstøtte:** Den støtter mange populære generative AI-modeller, som LLaMA, GPT-Neo, BLOOM, og flere.
- **Ytelsesoptimalisering:** Den inkluderer optimaliseringer for ulike maskinvareakseleratorer som NVIDIA GPUer, AMD GPUer, og flere2.
- **Brukervennlighet:** Den tilbyr APIer for enkel integrasjon i applikasjoner, slik at du kan generere tekst, bilder og annet innhold med minimal kode.
- Brukere kan kalle en høynivå generate()-metode, eller kjøre hver iterasjon av modellen i en løkke, generere ett token om gangen, og eventuelt oppdatere generasjonsparametere inne i løkken.
- ONNX Runtime har også støtte for greedy/beam search og TopP, TopK sampling for å generere tokensekvenser og innebygd logitsbehandling som repeteringsstraffer. Du kan også enkelt legge til egen poenggiving.

## Komme i gang
For å komme i gang med ONNX Runtime for GENAI, kan du følge disse trinnene:

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

I tillegg til ONNX Runtime, Ollama og Foundry Local referansemetoder, kan vi også fullføre referansen til kvantitative modeller basert på modellreferansemetoder levert av ulike leverandører. For eksempel Apple MLX-rammeverk med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU, osv. Du kan også finne mer innhold i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lært det grunnleggende om Phi-3/3.5-familien, men for å lære mer om SLM trenger vi mer kunnskap. Du kan finne svarene i Phi-3 Cookbook. Hvis du vil lære mer, besøk gjerne [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->