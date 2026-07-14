# Introductie tot Kleine Taalmodellen voor Generatieve AI voor Beginners
Generatieve AI is een fascinerend gebied binnen kunstmatige intelligentie dat zich richt op het creëren van systemen die in staat zijn nieuwe content te genereren. Deze content kan variëren van tekst en beelden tot muziek en zelfs volledige virtuele omgevingen. Een van de meest opwindende toepassingen van generatieve AI is op het gebied van taalmodellen.

## Wat Zijn Kleine Taalmodellen?

Een Klein Taalmodel (SLM) vertegenwoordigt een verkleinde variant van een groot taalmodel (LLM), waarbij veel van de architectonische principes en technieken van LLM's worden gebruikt, terwijl het een aanzienlijk verminderde rekenkundige voetafdruk heeft.

SLM's zijn een subset van taalmodellen die ontworpen zijn om mensachtige tekst te genereren. In tegenstelling tot hun grotere tegenhangers, zoals GPT-4, zijn SLM's compacter en efficiënter, waardoor ze ideaal zijn voor toepassingen waarbij rekenkundige middelen beperkt zijn. Ondanks hun kleinere omvang kunnen ze nog steeds een verscheidenheid aan taken uitvoeren. Meestal worden SLM's geconstrueerd door LLM's te comprimeren of distilleren, met als doel een aanzienlijk deel van de oorspronkelijke functionaliteit en linguïstische capaciteiten te behouden. Deze verkleining van het model vermindert de algehele complexiteit, waardoor SLM's efficiënter zijn in termen van zowel geheugengebruik als rekenkundige vereisten. Ondanks deze optimalisaties kunnen SLM's nog steeds een breed scala aan natuurlijke taalverwerking (NLP) taken uitvoeren:

- Tekstgeneratie: Het creëren van coherente en contextueel relevante zinnen of paragrafen.
- Tekstvoltooiing: Het voorspellen en voltooien van zinnen op basis van een gegeven prompt.
- Vertaling: Het omzetten van tekst van de ene taal naar de andere.
- Samenvatting: Het inkorten van lange teksten tot kortere, beter verteerbare samenvattingen.

Weliswaar met enige concessies in prestaties of diepte van begrip vergeleken met hun grotere tegenhangers.

## Hoe Werken Kleine Taalmodellen?
SLM's worden getraind op enorme hoeveelheden tekstdata. Tijdens het trainen leren ze de patronen en structuren van taal, waardoor ze tekst kunnen genereren die zowel grammaticaal correct als contextueel passend is. Het trainingsproces omvat:

- Gegevensverzameling: Het verzamelen van grote datasets van tekst uit diverse bronnen.
- Voorbewerking: Het opschonen en organiseren van de data om het geschikt te maken voor training.
- Training: Het gebruiken van machine learning-algoritmen om het model te leren hoe het tekst moet begrijpen en genereren.
- Fijn-afstemming: Het afstellen van het model om de prestaties op specifieke taken te verbeteren.

De ontwikkeling van SLM's stemt overeen met de toenemende behoefte aan modellen die kunnen worden ingezet in omgevingen met beperkte middelen, zoals mobiele apparaten of edge computing platforms, waar volledige LLM's onpraktisch kunnen zijn vanwege hun zware middelengebruik. Door te focussen op efficiëntie balanceren SLM's prestaties met toegankelijkheid en maken ze bredere toepassingen mogelijk in diverse domeinen.

![slm](../../../translated_images/nl/slm.4058842744d0444a.webp)

## Leerdoelen

In deze les hopen we kennis van SLM te introduceren en dit te combineren met Microsoft Phi-3 om verschillende scenario's te leren in tekstcontent, visie en MoE.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is SLM?
- Wat is het verschil tussen SLM en LLM?
- Wat is de Microsoft Phi-3/3.5 Familie?
- Hoe voer je inferentie uit met de Microsoft Phi-3/3.5 Familie?

Klaar? Laten we beginnen.

## De Onderscheidingen tussen Grote Taalmodellen (LLM's) en Kleine Taalmodellen (SLM's)

Zowel LLM's als SLM's zijn gebouwd op basisprincipes van probabilistische machine learning, en volgen vergelijkbare benaderingen in hun architectonisch ontwerp, trainingsmethodologieën, data-generatieprocessen en modelevaluatietechnieken. Echter, enkele belangrijke factoren onderscheiden deze twee soorten modellen.

## Toepassingen van Kleine Taalmodellen

SLM's hebben een breed scala aan toepassingen, waaronder:

- Chatbots: Het bieden van klantenondersteuning en het aangaan van gesprekken met gebruikers.
- Contentcreatie: Het assisteren van schrijvers door ideeën te genereren of zelfs hele artikelen te schrijven.
- Onderwijs: Het helpen van studenten met schrijfopdrachten of het leren van nieuwe talen.
- Toegankelijkheid: Het creëren van hulpmiddelen voor mensen met een beperking, zoals tekst-naar-spraak systemen.

**Grootte**
  
Een belangrijk onderscheid tussen LLM's en SLM's ligt in de schaal van de modellen. LLM's, zoals ChatGPT (GPT-4), kunnen ongeveer 1,76 biljoen parameters omvatten, terwijl open-source SLM's zoals Mistral 7B aanzienlijk minder parameters bevatten — ongeveer 7 miljard. Dit verschil komt voornamelijk door variaties in modelarchitectuur en trainingsprocessen. Bijvoorbeeld, ChatGPT gebruikt een self-attention mechanisme binnen een encoder-decoder architectuur, terwijl Mistral 7B gebruikmaakt van sliding window attention, wat efficiëntere training mogelijk maakt binnen een decoder-only model. Deze architecturale verschillen hebben een grote impact op de complexiteit en prestaties van deze modellen.

**Begrip**

SLM's zijn meestal geoptimaliseerd voor prestaties binnen specifieke domeinen, waardoor ze zeer gespecialiseerd zijn maar mogelijk beperkt in hun vermogen om brede contextuele kennis over meerdere kennisgebieden te bieden. LLM's daarentegen streven ernaar menselijke intelligentie op een bredere schaal na te bootsen. Getraind op grote, diverse datasets zijn LLM's ontworpen om goed te presteren in verschillende domeinen, wat grotere veelzijdigheid en aanpassingsvermogen biedt. Hierdoor zijn LLM's geschikter voor een breder scala aan downstream-taken, zoals natuurlijke taalverwerking en programmeren.

**Rekenen**

Het trainen en inzetten van LLM's zijn middelenintensieve processen, vaak vereisend aanzienlijke rekeninfrastructuur, waaronder grootschalige GPU-clusters. Bijvoorbeeld, het trainen van een model zoals ChatGPT vanaf nul kan duizenden GPU's vereisen over lange periodes. SLM's daarentegen, vanwege hun kleinere aantal parameters, zijn toegankelijker qua rekenkracht. Modellen zoals Mistral 7B kunnen getraind en uitgevoerd worden op lokale machines met matige GPU-capaciteiten, hoewel training nog steeds enkele uren en meerdere GPU's kan vereisen.

**Vooringenomenheid**

Vooringenomenheid is een bekend probleem bij LLM's, hoofdzakelijk vanwege de aard van de trainingsdata. Deze modellen vertrouwen vaak op ruwe, vrij beschikbare data van internet, die bepaalde groepen ondervertegenwoordigen of verkeerd weergeven, foutieve labels bevatten, of taalkundige biases weerspiegelen beïnvloed door dialect, geografische variaties en grammaticale regels. Bovendien kan de complexiteit van LLM-architecturen onbedoeld vooringenomenheid versterken, wat zonder zorgvuldige fijn-afstemming ongezien kan blijven. SLM's, getraind op meer beperkte, domeinspecifieke datasets, zijn van nature minder vatbaar voor dergelijke biases, hoewel ze er niet helemaal immuun voor zijn.

**Inferentie**

De kleinere omvang van SLM's geeft ze een aanzienlijk voordeel qua inferentiesnelheid, waardoor ze efficiënt output kunnen genereren op lokale hardware zonder uitgebreide parallelle verwerking. LLM's daarentegen vereisen vanwege hun grootte en complexiteit vaak aanzienlijke parallelle rekenmiddelen om acceptabele inferentietijden te behalen. Het gelijktijdig gebruik door meerdere gebruikers vertraagt ook de responstijden van LLM's, vooral bij grootschalige inzet.

Samenvattend, hoewel zowel LLM's als SLM's een gemeenschappelijke basis in machine learning delen, verschillen ze aanzienlijk in modelgrootte, middelenvereisten, contextueel begrip, gevoeligheid voor vooringenomenheid en inferentiesnelheid. Deze verschillen weerspiegelen hun respectieve geschiktheid voor diverse toepassingen, waarbij LLM's veelzijdiger maar middelenintensief zijn, en SLM's efficiënter zijn binnen specifieke domeinen met verminderde rekenkundige eisen.

***Opmerking: In deze les zullen we SLM introduceren aan de hand van Microsoft Phi-3 / 3.5 als voorbeeld.***

## Introductie Tot Phi-3 / Phi-3.5 Familie

Phi-3 / 3.5 familie richt zich hoofdzakelijk op tekst-, visie- en Agent (MoE) toepassingen:

### Phi-3 / 3.5 Instruct

Voornamelijk voor tekstgeneratie, chatvoltooiing en contentinformatie-extractie, enzovoort.

**Phi-3-mini**

Het 3.8 miljard parameters model is beschikbaar op Microsoft Foundry, Hugging Face en Ollama. Phi-3 modellen presteren significant beter dan taalmodellen van gelijke en grotere grootte op belangrijke benchmarks (zie onderstaande benchmarkcijfers, hogere cijfers zijn beter). Phi-3-mini presteert beter dan modellen die twee keer zo groot zijn, terwijl Phi-3-small en Phi-3-medium grotere modellen, inclusief GPT-3.5, overtreffen.

**Phi-3-small & medium**

Met slechts 7 miljard parameters verslaat Phi-3-small GPT-3.5T op diverse benchmarks op het gebied van taal, redenering, codering en wiskunde.

Phi-3-medium met 14 miljard parameters zet deze trend voort en presteert beter dan Gemini 1.0 Pro.

**Phi-3.5-mini**

We kunnen het zien als een upgrade van Phi-3-mini. Hoewel het aantal parameters gelijk blijft, verbetert het de ondersteuning voor meerdere talen (ondersteuning voor meer dan 20 talen: Arabisch, Chinees, Tsjechisch, Deens, Nederlands, Engels, Fins, Frans, Duits, Hebreeuws, Hongaars, Italiaans, Japans, Koreaans, Noors, Pools, Portugees, Russisch, Spaans, Zweeds, Thais, Turks, Oekraïens) en voegt het sterkere ondersteuning toe voor lange context.

Phi-3.5-mini met 3.8 miljard parameters overtreft taalmodellen van dezelfde grootte en is vergelijkbaar met modellen die twee keer zo groot zijn.

### Phi-3 / 3.5 Visie

We kunnen het instructiemodel van Phi-3/3.5 zien als Phi's vermogen om te begrijpen, en Visie is wat Phi ogen geeft om de wereld te begrijpen.


**Phi-3-Visie**

Phi-3-Visie, met slechts 4.2 miljard parameters, zet deze trend voort en presteert beter dan grotere modellen zoals Claude-3 Haiku en Gemini 1.0 Pro V op algemene visuele redeneertaken, OCR, en taken rond tabellen en diagrammen begrijpen.


**Phi-3.5-Visie**

Phi-3.5-Visie is ook een upgrade van Phi-3-Visie, waarbij ondersteuning voor meerdere beelden wordt toegevoegd. Je kunt het zien als een verbetering in visie: niet alleen kan je foto's zien, maar ook video's.

Phi-3.5-Visie presteert beter dan grotere modellen zoals Claude-3.5 Sonnet en Gemini 1.5 Flash op OCR-, tabel- en grafiekbegripstaken en is gelijkwaardig in algemene visuele kennis redeneertaken. Het ondersteunt multi-frame input, d.w.z. redeneren over meerdere inputbeelden.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** stelt modellen in staat om met veel minder rekencapaciteit getraind te worden, wat betekent dat je het model of de dataset dramatisch kunt opschalen met hetzelfde rekenbudget als een dicht model. Met name zou een MoE model tijdens de pretraining dezelfde kwaliteit als zijn dichte tegenhanger veel sneller moeten bereiken.

Phi-3.5-MoE omvat 16x3.8 miljard expertmodules. Phi-3.5-MoE met slechts 6.6 miljard actieve parameters bereikt een vergelijkbaar niveau van redeneren, taalbegrip en wiskunde als veel grotere modellen.

We kunnen het Phi-3/3.5 familie model gebruiken op basis van verschillende scenario's. In tegenstelling tot LLM's kun je Phi-3/3.5-mini of Phi-3/3.5-Visie op edge-apparaten implementeren.


## Hoe gebruik je Phi-3/3.5 Familie modellen

We hopen Phi-3/3.5 in verschillende scenario's te gebruiken. Vervolgens zullen we Phi-3/3.5 gebruiken op basis van verschillende scenario's.

![phi3](../../../translated_images/nl/phi3.655208c3186ae381.webp)

### Inferentie via Cloud API's

**Microsoft Foundry Modellen**

> **Opmerking:** GitHub Models wordt uitgefaseerd eind juli 2026. [Microsoft Foundry Modellen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) is de directe vervanging.

Microsoft Foundry Modellen is de meest directe manier. Je kunt snel toegang krijgen tot het Phi-3/3.5-Instruct model via de Foundry modelcatalogus. Gecombineerd met de Azure AI Inference SDK / OpenAI SDK kun je via code de API benaderen om de Phi-3/3.5-Instruct aanroep te voltooien. Je kunt ook verschillende effecten testen via de Playground.

- Demo: Vergelijking van de effecten van Phi-3-mini en Phi-3.5-mini in Chinese scenario’s

![phi3](../../../translated_images/nl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/nl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Of als je de visie- en MoE-modellen wilt gebruiken, kun je Microsoft Foundry gebruiken om de aanroep te voltooien. Als je geïnteresseerd bent, kun je de Phi-3 Cookbook lezen om te leren hoe je Phi-3/3.5 Instruct, Visie, MoE via Microsoft Foundry aanroept [Klik op deze link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Naast de cloudgebaseerde Microsoft Foundry Models catalogus kun je ook [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) gebruiken om gerelateerde aanroepen te voltooien. Je kunt NVIDIA NIM bezoeken om de API-aanroepen van de Phi-3/3.5 Familie af te handelen. NVIDIA NIM (NVIDIA Inference Microservices) is een set van versnelde inferentiemicroservices ontworpen om ontwikkelaars te helpen AI-modellen efficiënt te implementeren in diverse omgevingen, inclusief clouds, datacenters en werkstations.

Hier zijn enkele kernfuncties van NVIDIA NIM:

- **Eenvoud van Implementatie:** NIM maakt het mogelijk AI-modellen met één commando uit te rollen, wat integratie in bestaande workflows eenvoudig maakt.

- **Geoptimaliseerde prestaties:** Het maakt gebruik van NVIDIA’s vooraf geoptimaliseerde inference engines, zoals TensorRT en TensorRT-LLM, om lage latency en hoge doorvoer te garanderen.
- **Schaalbaarheid:** NIM ondersteunt autoscaling op Kubernetes, waardoor het effectief kan omgaan met wisselende werklasten.
- **Beveiliging en controle:** Organisaties kunnen controle behouden over hun data en applicaties door NIM-microservices zelf te hosten op hun eigen beheerde infrastructuur.
- **Standaard API’s:** NIM biedt API’s volgens industriestandaard, waardoor het eenvoudig is om AI-toepassingen zoals chatbots, AI-assistenten en meer te bouwen en integreren.

NIM maakt deel uit van NVIDIA AI Enterprise, dat erop gericht is het eenvoudig te maken AI-modellen te implementeren en te operationaliseren, zodat ze efficiënt draaien op NVIDIA GPU’s.

- Demo: NVIDIA NIM gebruiken om Phi-3.5-Vision-API aan te roepen [[Klik op deze link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaal draaien
Inference in relatie tot Phi-3, of een taalmodel zoals GPT-3, verwijst naar het proces van het genereren van antwoorden of voorspellingen op basis van de input die het ontvangt. Wanneer je een prompt of vraag aan Phi-3 geeft, gebruikt het zijn getrainde neurale netwerk om de meest waarschijnlijke en relevante respons af te leiden door patronen en relaties in de data waarop het is getraind te analyseren.

**Hugging Face Transformer**
Hugging Face Transformers is een krachtige bibliotheek ontworpen voor natural language processing (NLP) en andere machine learning taken. Hier zijn enkele belangrijke punten erover:

1. **Voorgetrainde modellen**: Het biedt duizenden voorgetrainde modellen die gebruikt kunnen worden voor diverse taken zoals tekstclassificatie, named entity recognition, vraagbeantwoording, samenvatting, vertaling en tekstgeneratie.

2. **Framework interoperabiliteit**: De bibliotheek ondersteunt meerdere deep learning frameworks, waaronder PyTorch, TensorFlow en JAX. Dit maakt het mogelijk een model in het ene framework te trainen en in een ander te gebruiken.

3. **Multimodale mogelijkheden**: Naast NLP ondersteunt Hugging Face Transformers ook taken in computer vision (bijv. beeldclassificatie, objectdetectie) en audioprocessing (bijv. spraakherkenning, audioclassificatie).

4. **Gebruiksgemak**: De bibliotheek biedt API’s en tools om modellen eenvoudig te downloaden en fijn af te stemmen, waardoor het toegankelijk is voor zowel beginners als experts.

5. **Community en bronnen**: Hugging Face heeft een levendige community en uitgebreide documentatie, tutorials en handleidingen om gebruikers te helpen snel aan de slag te gaan en optimaal gebruik te maken van de bibliotheek.
[officiële documentatie](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) of hun [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dit is de meest gebruikte methode, maar vereist ook GPU-versnelling. Scenario’s zoals Vision en MoE vereisen immers veel berekeningen, die heel traag zouden zijn op CPU als ze niet gequantiseerd zijn.


- Demo: Transformer gebruiken om Phi-3.5-Instruct aan te roepen [Klik op deze link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer gebruiken om Phi-3.5-Vision aan te roepen [Klik op deze link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer gebruiken om Phi-3.5-MoE aan te roepen [Klik op deze link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) is een platform dat het makkelijker maakt grote taalmodellen (LLM’s) lokaal op je machine te draaien. Het ondersteunt verschillende modellen zoals Llama 3.1, Phi 3, Mistral en Gemma 2, onder andere. Het platform vereenvoudigt het proces door modelgewichten, configuratie en data samen te bundelen in één pakket, waardoor het toegankelijker wordt voor gebruikers om hun eigen modellen aan te passen en te creëren. Ollama is beschikbaar voor macOS, Linux en Windows. Het is een geweldig hulpmiddel als je wilt experimenteren met of LLM’s wilt implementeren zonder te vertrouwen op cloudservices. Ollama is de meest directe weg, je hoeft alleen het volgende commando uit te voeren.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) is Microsoft’s offline, on-device runtime voor het draaien van modellen zoals Phi volledig op je eigen hardware - geen Azure-abonnement, API-sleutel of netwerkverbinding nodig. Het kiest automatisch de beste beschikbare uitvoeringprovider (NPU, GPU of CPU) en biedt een OpenAI-compatibele endpoint, zodat bestaande `openai`/Azure AI Inference SDK-code er met minimale wijzigingen naar kan verwijzen. Raadpleeg de [Foundry Local documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om te beginnen.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Of gebruik de SDK direct in Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime voor GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) is een cross-platform inference- en trainingsversneller voor machine learning. ONNX Runtime voor Generative AI (GENAI) is een krachtig hulpmiddel dat je helpt generatieve AI-modellen efficiënt te draaien op verschillende platformen.

## Wat is ONNX Runtime?
ONNX Runtime is een open-source project dat high-performance inference van machine learning modellen mogelijk maakt. Het ondersteunt modellen in het Open Neural Network Exchange (ONNX) formaat, een standaard voor het representeren van machine learning modellen. ONNX Runtime inference kan snellere klantbelevingen en lagere kosten mogelijk maken, met ondersteuning voor modellen uit deep learning frameworks zoals PyTorch en TensorFlow/Keras en klassieke machine learning bibliotheken zoals scikit-learn, LightGBM, XGBoost, enzovoort. ONNX Runtime is compatibel met verschillende hardware, drivers en besturingssystemen, en biedt optimale prestaties door waar mogelijk hardwareversnellers te benutten naast grafiekoptimalisaties en transformaties.

## Wat is Generative AI?
Generative AI verwijst naar AI-systemen die nieuwe content kunnen genereren, zoals tekst, afbeeldingen of muziek, op basis van de data waarop ze zijn getraind. Voorbeelden zijn taalmodellen zoals GPT-3 en beeldgeneratiemodellen zoals Stable Diffusion. De ONNX Runtime voor GenAI bibliotheek biedt de generatieve AI-loop voor ONNX modellen, inclusief inference met ONNX Runtime, logitsverwerking, zoek- en steekproefmethoden, en KV-cachebeheer.

## ONNX Runtime voor GENAI
ONNX Runtime voor GENAI breidt de mogelijkheden van ONNX Runtime uit om generatieve AI-modellen te ondersteunen. Hier zijn enkele belangrijke kenmerken:

- **Breed platformondersteuning:** Het werkt op verschillende platformen, waaronder Windows, Linux, macOS, Android en iOS.
- **Modelondersteuning:** Het ondersteunt veel populaire generatieve AI-modellen, zoals LLaMA, GPT-Neo, BLOOM en meer.
- **Prestatieoptimalisatie:** Het bevat optimalisaties voor verschillende hardwareversnellers zoals NVIDIA GPU’s, AMD GPU’s, en meer2.
- **Gebruiksgemak:** Het biedt API’s voor eenvoudige integratie in applicaties, waarmee je tekst, afbeeldingen en andere content kunt genereren met minimale code.
- Gebruikers kunnen een high level generate() methode aanroepen, of elke iteratie van het model in een lus uitvoeren, waarbij telkens één token wordt gegenereerd en optioneel generatieparameters binnen de lus worden aangepast.
- ONNX runtime ondersteunt ook greedy/beam search en TopP, TopK sampling om tokenreeksen te genereren en ingebouwde logitsverwerking zoals straf op herhaling. Je kunt ook eenvoudig eigen scoremethoden toevoegen.

## Aan de slag
Om aan de slag te gaan met ONNX Runtime voor GENAI kun je deze stappen volgen:

### Installeer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installeer de generatieve AI-extensies:
```Python
pip install onnxruntime-genai
```

### Draai een model: Hier is een simpel voorbeeld in Python:
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
### Demo: ONNX Runtime GenAI gebruiken om Phi-3.5-Vision aan te roepen


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


**Overige**

Naast ONNX Runtime, Ollama en Foundry Local referentiemethoden kunnen we ook kwantitatieve modellering afronden op basis van modelreferentiemethoden die door verschillende fabrikanten worden geleverd. Zoals Apple MLX framework met Apple Metal, Qualcomm QNN met NPU, Intel OpenVINO met CPU/GPU, enzovoort. Je kunt ook meer inhoud vinden in de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Meer

We hebben de basis van de Phi-3/3.5 familie geleerd, maar om meer te leren over SLM hebben we meer kennis nodig. Je kunt de antwoorden vinden in de Phi-3 Cookbook. Als je meer wilt leren, bezoek dan de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->