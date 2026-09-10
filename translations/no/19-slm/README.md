# Introduksjon til små språkmodeller for generativ AI for nybegynnere
Generativ AI er et fascinerende felt innen kunstig intelligens som fokuserer på å skape systemer som er i stand til å generere nytt innhold. Dette innholdet kan variere fra tekst og bilder til musikk og til og med hele virtuelle miljøer. En av de mest spennende anvendelsene av generativ AI er innenfor språkteknologi.

## Hva er små språkmodeller?

En liten språkmodell (SLM) representerer en nedskalert variant av en stor språkmodell (LLM), som benytter mange av de arkitektoniske prinsippene og teknikkene til LLM-er, samtidig som den har et betydelig redusert beregningsmessig fotavtrykk.

SLM-er er en undergruppe av språkmodeller designet for å generere menneskelignende tekst. I motsetning til sine større motstykker, som GPT-4, er SLM-er mer kompakte og effektive, noe som gjør dem ideelle for applikasjoner hvor databehandlingsressurser er begrensede. Til tross for sin mindre størrelse kan de fortsatt utføre en rekke oppgaver. Vanligvis konstrueres SLM-er ved å komprimere eller destillere LLM-er, med mål om å beholde en betydelig del av den opprinnelige modellens funksjonalitet og språklige evner. Denne reduksjonen i modellstørrelse reduserer den totale kompleksiteten, noe som gjør SLM-er mer effektive både når det gjelder minnebruk og beregningskrav. Til tross for disse optimaliseringene kan SLM-er fortsatt utføre et bredt spekter av oppgaver innen naturlig språkbehandling (NLP):

- Tekstgenerering: Lage sammenhengende og kontekstuelt relevante setninger eller avsnitt.
- Tekstfullføring: Forutsi og fullføre setninger basert på en gitt ledetekst.
- Oversettelse: Konvertere tekst fra ett språk til et annet.
- Oppsummering: Forkorte lange tekststykker til kortere, mer lettfordøyelige sammendrag.

Selv om det innebærer noen avveininger i ytelse eller dybde i forståelsen sammenlignet med deres større motstykker.

## Hvordan fungerer små språkmodeller?
SLM-er trenes på store mengder tekstdata. Under treningen lærer de mønstre og strukturer i språket, noe som gjør dem i stand til å generere tekst som både er grammatisk korrekt og kontekstuelt passende. Treningsprosessen innebærer:

- Datainnsamling: Samle store datasett med tekst fra ulike kilder.
- Forbehandling: Rensing og organisering av dataene for å gjøre dem egnet for trening.
- Trening: Bruke maskinlæringsalgoritmer for å lære modellen å forstå og generere tekst.
- Finjustering: Justere modellen for å forbedre ytelsen på spesifikke oppgaver.

Utviklingen av SLM-er samsvarer med det økende behovet for modeller som kan implementeres i miljøer med begrensede ressurser, som mobile enheter eller edge computing-plattformer, hvor fullskala LLM-er kan være upraktiske på grunn av deres tunge ressurskrav. Ved å fokusere på effektivitet balanserer SLM-er ytelse med tilgjengelighet, noe som muliggjør bredere anvendelse på tvers av ulike domener.

![slm](../../../translated_images/no/slm.4058842744d0444a.webp)

## Læringsmål

I denne leksjonen håper vi å introdusere kunnskap om SLM og kombinere det med Microsoft Phi-3 for å lære ulike scenarier innen tekstinnhold, visjon og MoE.

Ved slutten av denne leksjonen bør du kunne svare på følgende spørsmål:

- Hva er SLM?
- Hva er forskjellen mellom SLM og LLM?
- Hva er Microsoft Phi-3/3.5-familien?
- Hvordan kjøre inferens med Microsoft Phi-3/3.5-familien?

Klar? La oss begynne.

## Forskjellene mellom store språkmodeller (LLMs) og små språkmodeller (SLMs)

Både LLM-er og SLM-er bygger på grunnleggende prinsipper for probabilistisk maskinlæring, og følger lignende tilnærminger i deres arkitektoniske design, treningsmetodologier, datagenereringsprosesser og modellvurderingsteknikker. Imidlertid skiller flere nøkkelfaktorer disse to modelltypene.

## Anvendelser av små språkmodeller

SLM-er har et bredt spekter av bruksområder, inkludert:

- Chatbots: Gi kundeservice og engasjere brukere i en samtalebasert måte.
- Innholdsproduksjon: Bistå forfattere ved å generere idéer eller til og med skrive hele artikler.
- Utdanning: Hjelpe studenter med skriveoppgaver eller å lære nye språk.
- Tilgjengelighet: Lage verktøy for personer med funksjonsnedsettelser, som tekst-til-tale-systemer.

**Størrelse**
  
En hovedforskjell mellom LLM-er og SLM-er ligger i modellens skala. LLM-er, som ChatGPT (GPT-4), kan bestå av anslagsvis 1,76 billioner parametere, mens åpne SLM-er som Mistral 7B er designet med betydelig færre parametere — omtrent 7 milliarder. Denne ulikheten skyldes hovedsakelig forskjeller i modellarkitektur og treningsprosesser. For eksempel benytter ChatGPT en selvoppmerksomhetsmekanisme innenfor en encoder-decoder-rammeverk, mens Mistral 7B bruker sliding window attention, noe som muliggjør mer effektiv trening innenfor en decoder-only modell. Denne arkitektoniske variasjonen har store konsekvenser for modellens kompleksitet og ytelse.

**Forståelse**

SLM-er er vanligvis optimalisert for ytelse innen spesifikke domener, noe som gjør dem høyt spesialiserte, men potensielt begrenset i evnen til å gi bred kontekstuell forståelse på tvers av flere kunnskapsområder. I kontrast prøver LLM-er å simulere menneskelignende intelligens på et mer omfattende nivå. Trent på store, mangfoldige datasett er LLM-er designet for å prestere godt på tvers av ulike domener, og tilbyr større allsidighet og tilpasningsevne. Derfor er LLM-er mer egnet for et bredere spekter av nedstrømsoppgaver, som naturlig språkbehandling og programmering.

**Beregning**

Trening og distribusjon av LLM-er er ressurskrevende prosesser, som ofte krever betydelig datainfrastruktur, inkludert storskala GPU-klynger. For eksempel kan det å trene en modell som ChatGPT fra bunnen av kreve tusenvis av GPU-er over lang tid. I motsetning til dette er SLM-er, med sitt mindre antall parametere, mer tilgjengelige når det gjelder beregningsressurser. Modeller som Mistral 7B kan trenes og kjøres på lokale maskiner utstyrt med moderate GPU-kapasiteter, selv om treningen fortsatt krever flere timer over flere GPU-er.

**Skjevhet**

Skjevhet er et kjent problem i LLM-er, hovedsakelig på grunn av typen treningsdata. Disse modellene er ofte avhengige av rå, åpent tilgjengelige data fra Internett, som kan underrepresentere eller feilsitere visse grupper, introdusere feilaktig merking, eller reflektere språklige skjevheter påvirket av dialekt, geografiske variasjoner og grammatikkregler. I tillegg kan kompleksiteten i LLM-arkitekturer utilsiktet forsterke skjevheter, som kan gå ubemerket uten nøye finjustering. På den annen side, fordi SLM-er trenes på mer begrensede, domenespesifikke datasett, er de i utgangspunktet mindre utsatt for slike skjevheter, selv om de ikke er immune.

**Inferens**

Den reduserte størrelsen på SLM-er gir dem en betydelig fordel når det gjelder inferenshastighet, noe som gjør dem i stand til å generere resultater effektivt på lokal maskinvare uten behov for omfattende parallell behandling. I kontrast krever LLM-er, på grunn av deres størrelse og kompleksitet, ofte betydelige parallelle beregningsressurser for å oppnå akseptable inferenstider. Tilstedeværelsen av flere samtidige brukere bremser også LLM-ers responstider, spesielt når de implementeres i stor skala.

Oppsummert, selv om både LLM-er og SLM-er deler et grunnleggende grunnlag i maskinlæring, skiller de seg betydelig når det gjelder modellstørrelse, ressursbehov, kontekstuell forståelse, sårbarhet for skjevhet og inferenshastighet. Disse forskjellene reflekterer deres respektive egnethet for ulike bruksområder, hvor LLM-er er mer allsidige men ressurskrevende, og SLM-er tilbyr mer domensespesifikk effektivitet med reduserte beregningsbehov.

***Merk: I denne leksjonen vil vi introdusere SLM ved bruk av Microsoft Phi-3 / 3.5 som eksempel.***

## Introduksjon til Phi-3 / Phi-3.5-familien

Phi-3 / 3.5-familien retter seg hovedsakelig mot tekst-, syns- og Agent (MoE)-applikasjonsscenarier:

### Phi-3 / 3.5 Instruct

Hovedsakelig for tekstgenerering, chattefullføring og innholdsutvinning, osv.

**Phi-3-mini**

Den 3,8 milliarder store språkmodellen er tilgjengelig på Microsoft Foundry, Hugging Face og Ollama. Phi-3-modeller presterer betydelig bedre enn språkmodeller av lik eller større størrelse på viktige benchmarks (se benchmark-tall nedenfor, høyere tall er bedre). Phi-3-mini presterer bedre enn modeller med dobbelt så mange parametere, mens Phi-3-small og Phi-3-medium overgår større modeller, inkludert GPT-3.5.

**Phi-3-small & medium**

Med bare 7 milliarder parametere slår Phi-3-small GPT-3.5T på en rekke språk-, resonnement-, koding- og matematiske benchmarks.

Phi-3-medium med 14 milliarder parametere fortsetter denne trenden og overgår Gemini 1.0 Pro.

**Phi-3.5-mini**

Vi kan se på den som en oppgradering av Phi-3-mini. Mens parameterantallet forblir uendret, forbedrer den evnen til å støtte flere språk (støtter 20+ språk: arabisk, kinesisk, tsjekkisk, dansk, nederlandsk, engelsk, finsk, fransk, tysk, hebraisk, ungarsk, italiensk, japansk, koreansk, norsk, polsk, portugisisk, russisk, spansk, svensk, thai, tyrkisk, ukrainsk) og gir sterkere støtte for lang kontekst.

Phi-3.5-mini med 3,8 milliarder parametere overgår språkmodeller av samme størrelse og står på linje med modeller med dobbelt så mange parametere.

### Phi-3 / 3.5 Vision

Vi kan tenke på Instruct-modellen til Phi-3/3.5 som Phis evne til å forstå, og Vision er det som gir Phi øyne for å forstå verden.


**Phi-3-Vision**

Phi-3-vision, med bare 4,2 milliarder parametere, fortsetter denne trenden og overgår større modeller som Claude-3 Haiku og Gemini 1.0 Pro V på generelle visuelle resonnementoppgaver, OCR, og bord- og diagramforståelse.


**Phi-3.5-Vision**

Phi-3.5-Vision er også en oppgradering av Phi-3-Vision, og tilfører støtte for flere bilder. Du kan tenke på det som en forbedring i syn, ikke bare kan du se bilder, men også videoer.

Phi-3.5-vision overgår større modeller som Claude-3.5 Sonnet og Gemini 1.5 Flash innen OCR-, bord- og diagramforståelse og er på nivå med generelle visuelle kunnskapsresonnementoppgaver. Støtter multi-frame input, det vil si utfører resonnement på flere inngangsbilder.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** gjør det mulig å forhåndstrene modeller med langt mindre beregning, noe som betyr at du kan skalere opp modell- eller datasettstørrelsen dramatisk med samme beregningsbudsjett som en tett modell. Spesielt skal en MoE-modell oppnå samme kvalitet som sin tette motpart mye raskere under forhåndstrening.

Phi-3.5-MoE består av 16x3,8 milliarder ekspertmoduler. Phi-3.5-MoE med bare 6,6 milliarder aktive parametere oppnår et lignende nivå av resonnement, språkforståelse og matematikk som mye større modeller.

Vi kan bruke Phi-3/3.5-familie-modellen basert på ulike scenarier. I motsetning til LLM kan du distribuere Phi-3/3.5-mini eller Phi-3/3.5-Vision på kant-enheter.


## Hvordan bruke Phi-3/3.5-familie modeller

Vi ønsker å bruke Phi-3/3.5 i ulike scenarier. Neste vil vi bruke Phi-3/3.5 basert på forskjellige scenarier.

![phi3](../../../translated_images/no/phi3.655208c3186ae381.webp)

### Inferens via sky-API-er

**Microsoft Foundry Models**

> **Merk:** GitHub Models fases ut ved slutten av juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) er den direkte erstatningen.

Microsoft Foundry Models er den mest direkte måten. Du kan raskt få tilgang til Phi-3/3.5-Instruct-modellen gjennom Foundry-modellkatalogen. Kombinert med Azure AI Inference SDK / OpenAI SDK kan du få tilgang til API-et gjennom kode for å fullføre Phi-3/3.5-Instruct-kall. Du kan også teste ulike effekter gjennom Playground.

- Demo: Sammenligning av effektene av Phi-3-mini og Phi-3.5-mini i kinesiske scenarioer

![phi3](../../../translated_images/no/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/no/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Eller hvis vi ønsker å bruke visjons- og MoE-modellene, kan du bruke Microsoft Foundry til å fullføre kallet. Hvis du er interessert, kan du lese Phi-3 Cookbook for å lære hvordan du kaller Phi-3/3.5 Instruct, Vision, MoE gjennom Microsoft Foundry [Klikk på denne lenken](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

I tillegg til den skybaserte Microsoft Foundry Models-katalogen, kan du også bruke [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) for å fullføre relaterte kall. Du kan besøke NVIDIA NIM for å fullføre API-kall til Phi-3/3.5-familien. NVIDIA NIM (NVIDIA Inference Microservices) er et sett akselererte inferens-mikrotjenester designet for å hjelpe utviklere med å distribuere AI-modeller effektivt på tvers av ulike miljøer, inkludert sky, datasentre og arbeidsstasjoner.

Her er noen nøkkelfunksjoner ved NVIDIA NIM:

- **Enkel distribusjon:** NIM tillater distribusjon av AI-modeller med én kommando, noe som gjør det enkelt å integrere i eksisterende arbeidsflyter.

- **Optimalisert ytelse:** Den bruker NVIDIAs forhåndsoptimaliserte inferensemotorer, slik som TensorRT og TensorRT-LLM, for å sikre lav ventetid og høy gjennomstrømning.
- **Skalerbarhet:** NIM støtter autoskalering på Kubernetes, noe som gjør at den effektivt kan håndtere varierende arbeidsmengder.
- **Sikkerhet og kontroll:** Organisasjoner kan opprettholde kontroll over sine data og applikasjoner ved å selvhoste NIM-mikrotjenester på egen administrert infrastruktur.
- **Standard API-er:** NIM tilbyr bransjestandard API-er, som gjør det enkelt å bygge og integrere AI-applikasjoner som chatbots, AI-assistenter og mer.

NIM er en del av NVIDIA AI Enterprise, som har som mål å forenkle distribusjon og operasjonalisering av AI-modeller, og sørge for at de kjøres effektivt på NVIDIA GPUer.

- Demo: Bruke NVIDIA NIM til å kalle Phi-3.5-Vision-API [[Klikk på denne lenken](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kjøre Phi-3/3.5 Lokalt
Inference i forhold til Phi-3, eller en hvilken som helst språkmodell som GPT-3, refererer til prosessen med å generere svar eller prediksjoner basert på input den mottar. Når du gir en prompt eller spørsmål til Phi-3, bruker den sitt trente nevrale nettverk til å inferere det mest sannsynlige og relevante svaret ved å analysere mønstre og relasjoner i dataene den ble trent på.

**Hugging Face Transformer**
Hugging Face Transformers er et kraftig bibliotek designet for naturlig språkbehandling (NLP) og andre maskinlæringsoppgaver. Her er noen hovedpunkter om det:

1. **Fortrente modeller**: Det tilbyr tusenvis av fortrente modeller som kan brukes til forskjellige oppgaver som tekstklassifisering, navngitt entitetsgjenkjenning, spørsmål og svar, oppsummering, oversettelse og tekstgenerering.

2. **Rammeverksinteroperabilitet:** Biblioteket støtter flere dype læringsrammeverk, inkludert PyTorch, TensorFlow og JAX. Dette lar deg trene en modell i ett rammeverk og bruke den i et annet.

3. **Multimodale muligheter:** I tillegg til NLP støtter Hugging Face Transformers også oppgaver innen datavisjon (f.eks. bildeklassifisering, objektdeteksjon) og lydbehandling (f.eks. talegjenkjenning, lydklassifisering).

4. **Brukervennlighet:** Biblioteket tilbyr API-er og verktøy for enkel nedlasting og finjustering av modeller, noe som gjør det tilgjengelig både for nybegynnere og eksperter.

5. **Fellesskap og ressurser:** Hugging Face har et levende fellesskap og omfattende dokumentasjon, veiledninger og guider for å hjelpe brukere å komme i gang og få mest mulig ut av biblioteket.
[offisiell dokumentasjon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) eller deres [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dette er den mest brukte metoden, men det krever også GPU-akselerasjon. Tross alt krever scenarier som Vision og MoE mye beregning, noe som vil gå veldig sakte på CPU hvis de ikke er kvantiserte.


- Demo: Bruke Transformer til å kalle Phi-3.5-Instruct [Klikk på denne lenken](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer til å kalle Phi-3.5-Vision [Klikk på denne lenken](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Bruke Transformer til å kalle Phi-3.5-MoE [Klikk på denne lenken](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) er en plattform laget for å gjøre det enklere å kjøre store språkmodeller (LLMs) lokalt på maskinen din. Den støtter ulike modeller som Llama 3.1, Phi 3, Mistral og Gemma 2, blant andre. Plattformen forenkler prosessen ved å pakke modellvekter, konfigurasjon og data i en enkelt pakke, noe som gjør det mer tilgjengelig for brukere å tilpasse og lage sine egne modeller. Ollama er tilgjengelig for macOS, Linux og Windows. Det er et flott verktøy hvis du ønsker å eksperimentere med eller distribuere LLM-er uten å være avhengig av skyløsninger. Ollama er den mest direkte metoden, du trenger bare å kjøre følgende kommando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) er Microsofts offline, lokale kjøretidsmiljø for å kjøre modeller som Phi helt på din egen maskinvare - ingen Azure-abonnement, API-nøkkel eller nettverkstilkobling nødvendig. Den velger automatisk den beste tilgjengelige utførelsesleverandøren (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, slik at eksisterende `openai`/Azure AI Inference SDK-kode kan peke på det med minimale endringer. Se [Foundry Local dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) er en tverrplattform for akselerert inferens og trening av maskinlæring. ONNX Runtime for Generative AI (GENAI) er et kraftig verktøy som hjelper deg å kjøre generative AI-modeller effektivt på tvers av ulike plattformer. 

## Hva er ONNX Runtime?
ONNX Runtime er et åpen kildekode-prosjekt som muliggjør høyytelses inferens av maskinlæringsmodeller. Det støtter modeller i Open Neural Network Exchange (ONNX)-formatet, som er en standard for representasjon av maskinlæringsmodeller. ONNX Runtime-inferens kan muliggjøre raskere kundeopplevelser og lavere kostnader, og støtter modeller fra dype læringsrammeverk som PyTorch og TensorFlow/Keras, i tillegg til klassiske maskinlæringsbiblioteker som scikit-learn, LightGBM, XGBoost osv. ONNX Runtime er kompatibelt med ulik maskinvare, drivere og operativsystemer, og gir optimal ytelse ved å utnytte maskinvareakseleratorer der det er aktuelt, sammen med grafoptimaliseringer og transformasjoner.

## Hva er Generativ AI?
Generativ AI refererer til AI-systemer som kan generere nytt innhold, som tekst, bilder eller musikk, basert på dataene de er trent på. Eksempler inkluderer språkmodeller som GPT-3 og bilde-genereringsmodeller som Stable Diffusion. ONNX Runtime for GenAI-biblioteket gir den generative AI-løkken for ONNX-modeller, inkludert inferens med ONNX Runtime, logits-prosessering, søk og sampling, samt KV cache-håndtering.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI utvider funksjonene til ONNX Runtime for å støtte generative AI-modeller. Her er noen nøkkelfunksjoner:

- **Bred plattformstøtte:** Den fungerer på ulike plattformer, inkludert Windows, Linux, macOS, Android og iOS.
- **Modellstøtte:** Den støtter mange populære generative AI-modeller, som LLaMA, GPT-Neo, BLOOM og flere.
- **Ytelsesoptimalisering:** Den inkluderer optimaliseringer for ulike maskinvareakseleratorer som NVIDIA GPU-er, AMD GPU-er og flere.
- **Enkel å bruke:** Den tilbyr API-er for enkel integrering i applikasjoner, slik at du kan generere tekst, bilder og annet innhold med minimal kode.
- Brukere kan kalle en høy-nivå generate()-metode, eller kjøre hver iterasjon av modellen i en løkke, generere én token om gangen, og eventuelt oppdatere genereringsparametere inne i løkken.
- ONNX runtime støtter også greedy/beam search og TopP, TopK sampling for å generere tokensekvenser og innebygd logits-prosessering som repetisjonsstraffer. Det er også enkelt å legge til egendefinert poengsetting.

## Komme i gang
For å komme i gang med ONNX Runtime for GENAI kan du følge disse trinnene:

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
### Demo: Bruke ONNX Runtime GenAI til å kalle Phi-3.5-Vision


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

I tillegg til ONNX Runtime, Ollama og Foundry Local referansemetoder, kan vi også fullføre referansen av kvantitative modeller basert på modellreferansemetoder levert av ulike produsenter. Som Apple MLX-rammeverket med Apple Metal, Qualcomm QNN med NPU, Intel OpenVINO med CPU/GPU, osv. Du kan også finne mer innhold i [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mer

Vi har lært det grunnleggende om Phi-3/3.5-familien, men for å lære mer om SLM trenger vi mer kunnskap. Du kan finne svar i Phi-3 Cookbook. Hvis du ønsker å lære mer, vennligst besøk [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->