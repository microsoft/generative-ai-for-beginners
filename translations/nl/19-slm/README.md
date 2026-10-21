# Inleiding tot Kleine Taalmodellen voor Generatieve AI voor Beginners
Generatieve AI is een fascinerend gebied van kunstmatige intelligentie dat zich richt op het creëren van systemen die in staat zijn nieuwe inhoud te genereren. Deze inhoud kan variëren van tekst en afbeeldingen tot muziek en zelfs complete virtuele omgevingen. Een van de meest spannende toepassingen van generatieve AI is op het gebied van taalmodellen.

## Wat zijn Kleine Taalmodellen?

Een Klein Taalmodel (SLM) is een verkleinde variant van een groot taalmodel (LLM), die veel van de architecturale principes en technieken van LLM's gebruikt, maar met een aanzienlijk kleinere computationele voetafdruk.

SLM’s zijn een subset van taalmodellen die ontworpen zijn om mensachtige tekst te genereren. In tegenstelling tot hun grotere tegenhangers, zoals GPT-4, zijn SLM’s compacter en efficiënter, waardoor ze ideaal zijn voor toepassingen waar beperkte computationele middelen beschikbaar zijn. Ondanks hun kleinere formaat kunnen ze nog steeds een verscheidenheid aan taken uitvoeren. Meestal worden SLM’s geconstrueerd door LLM’s te comprimeren of te distilleren, met als doel een aanzienlijk deel van de oorspronkelijke functionaliteit en taalkundige capaciteiten te behouden. Deze reductie in modelgrootte vermindert de algehele complexiteit, waardoor SLM’s efficiënter zijn in zowel geheugenverbruik als computationele vereisten. Ondanks deze optimalisaties kunnen SLM’s nog steeds een breed scala aan taken op het gebied van natuurlijke taalverwerking (NLP) uitvoeren:

- Tekstgeneratie: Creëren van coherente en contextueel relevante zinnen of alinea’s.
- Tekstvoltooiing: Voorspellen en vervolledigen van zinnen op basis van een gegeven prompt.
- Vertaling: Omzetten van tekst van de ene taal naar de andere.
- Samenvatting: Het condenseren van lange stukken tekst tot kortere, beter verteerbare samenvattingen.

Hoewel dit gepaard gaat met enkele concessies in prestaties of diepgang van begrip vergeleken met hun grotere tegenhangers.

## Hoe Werken Kleine Taalmodellen?
SLM’s worden getraind op enorme hoeveelheden tekstgegevens. Tijdens het trainen leren ze de patronen en structuren van taal, waardoor ze tekst kunnen genereren die zowel grammaticaal correct als contextueel passend is. Het trainingsproces omvat:

- Gegevensverzameling: Het verzamelen van grote datasets van tekst uit diverse bronnen.
- Voorbewerking: Het opschonen en organiseren van de data om deze geschikt te maken voor training.
- Training: Het gebruiken van machine learning-algoritmen om het model te leren tekst te begrijpen en genereren.
- Fijn-afstemming: Het aanpassen van het model om de prestaties op specifieke taken te verbeteren.

De ontwikkeling van SLM’s sluit aan bij de groeiende behoefte aan modellen die ingezet kunnen worden in omgevingen met beperkte middelen, zoals mobiele apparaten of edge computing-platforms, waar volledige LLM’s onpraktisch kunnen zijn vanwege hun hoge resourcegebruik. Door zich te richten op efficiëntie, balanceren SLM’s prestaties met toegankelijkheid, waardoor ze breder toepasbaar zijn in verschillende domeinen.

![slm](../../../translated_images/nl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Leerdoelen

In deze les hopen we kennis over SLM te introduceren en dit te combineren met Microsoft Phi-3 om verschillende scenario’s te leren in tekstinhoud, visie en MoE.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is een SLM?
- Wat is het verschil tussen SLM en LLM?
- Wat is de Microsoft Phi-3/3.5 Familie?
- Hoe voer je inferentie uit met de Microsoft Phi-3/3.5 Familie?

Klaar? Laten we beginnen.

## De Onderscheidingen tussen Grote Taalmodellen (LLM's) en Kleine Taalmodellen (SLM's)

Zowel LLM's als SLM's zijn gebouwd op fundamentele principes van probabilistisch machine learning, en volgen vergelijkbare benaderingen in hun architectonisch ontwerp, trainingsmethodologieën, data-generatieprocessen en modelevaluatietechnieken. Er zijn echter enkele belangrijke verschillen die deze twee typen modellen onderscheiden.

## Toepassingen van Kleine Taalmodellen

SLM's hebben een breed scala aan toepassingen, waaronder:

- Chatbots: Het bieden van klantenservice en het voeren van gesprekken met gebruikers.
- Inhoudcreatie: Schrijvers ondersteunen door ideeën te genereren of zelfs volledige artikelen op te stellen.
- Onderwijs: Studenten helpen bij schrijfopdrachten of het leren van nieuwe talen.
- Toegankelijkheid: Tools creëren voor mensen met beperkingen, zoals tekst-naar-spraak systemen.

**Grootte**
  
Een belangrijk verschil tussen LLM’s en SLM’s ligt in de schaal van de modellen. LLM’s, zoals ChatGPT (GPT-4), kunnen een geschatte 1,76 biljoen parameters bevatten, terwijl open source SLM’s zoals Mistral 7B zijn ontworpen met aanzienlijk minder parameters — ongeveer 7 miljard. Dit verschil is voornamelijk te wijten aan verschillen in modelarchitectuur en trainingsprocessen. Bijvoorbeeld, ChatGPT gebruikt een zelf-aandachtsmechanisme binnen een encoder-decoder framework, terwijl Mistral 7B sliding window attention gebruikt, wat efficiënter trainen binnen een decoder-only model mogelijk maakt. Deze architecturale variatie heeft diepgaande gevolgen voor de complexiteit en prestaties van deze modellen.

**Begrip**

SLM’s zijn typisch geoptimaliseerd voor prestaties binnen specifieke domeinen, waardoor ze zeer gespecialiseerd maar mogelijk beperkt zijn in hun vermogen tot breed contextueel begrip over meerdere kennisgebieden heen. Daarentegen streven LLM’s ernaar menselijke intelligentie op een meer omvattend niveau na te bootsen. Getraind op enorme, diverse datasets, zijn LLM’s ontworpen om goed te presteren in een verscheidenheid aan domeinen, waardoor ze groter aanpassingsvermogen en veelzijdigheid bieden. Daarom zijn LLM’s geschikt voor een breder scala aan downstream-taken, zoals natuurlijke taalverwerking en programmeren.

**Rekenkracht**

Het trainen en inzetten van LLM’s is resource-intensief en vereist vaak aanzienlijke computationele infrastructuur, waaronder grootschalige GPU clusters. Bijvoorbeeld, het trainen van een model als ChatGPT vanaf nul kan duizenden GPU’s over lange periodes vereisen. Daarentegen zijn SLM’s, met hun kleinere aantal parameters, toegankelijker wat betreft benodigde computationele middelen. Modellen zoals Mistral 7B kunnen getraind en uitgevoerd worden op lokale machines met matige GPU-capaciteiten, hoewel training toch enkele uren over meerdere GPU’s vergt.

**Bias**

Bias is een bekend probleem in LLM’s, voornamelijk veroorzaakt door de aard van de trainingsdata. Deze modellen vertrouwen vaak op ruwe, openbaar beschikbare data van het internet, die bepaalde groepen mogelijk onder- of verkeerd representeren, foutieve labeling introduceren, of taalkundige biases bevatten beïnvloed door dialecten, geografische variaties en grammaticale regels. Daarnaast kan de complexiteit van LLM-architecturen onbedoeld bias versterken, wat onopgemerkt kan blijven zonder zorgvuldige fijn-afstemming. Daarentegen zijn SLM’s, getraind op meer beperkte, domeinspecifieke datasets, van nature minder vatbaar voor dergelijke biases, hoewel ze er niet immuun voor zijn.

**Inferentie**

De kleinere omvang van SLM’s biedt een aanzienlijk voordeel in inferentiesnelheid, waardoor ze efficiënt output kunnen genereren op lokale hardware zonder noodzaak van uitgebreide parallelle verwerking. LLM’s daarentegen vereisen vanwege hun grootte en complexiteit vaak grote parallelle computationele bronnen om aanvaardbare inferentietijden te behalen. Het gelijktijdig gebruik door meerdere gebruikers vertraagt bovendien de responstijden van LLM’s, vooral bij grootschalige inzet.

Samenvattend, hoewel zowel LLM’s als SLM’s een fundamentele basis hebben in machine learning, verschillen ze aanzienlijk in modelgrootte, resourcevereisten, contextueel begrip, gevoeligheid voor bias en inferentiesnelheid. Deze verschillen weerspiegelen hun respectieve geschiktheid voor verschillende toepassingen, waarbij LLM’s veelzijdiger maar resource-intensief zijn, en SLM’s meer domeinspecifieke efficiëntie bieden met lagere computationele eisen.

***Let op: In deze les introduceren we SLM aan de hand van Microsoft Phi-3 / 3.5 als voorbeeld.***

## Introductie van Phi-3 / Phi-3.5 Familie

Phi-3 / 3.5 Familie richt zich voornamelijk op tekst-, visie- en Agent (MoE) toepassingsscenario’s:

### Phi-3 / 3.5 Instruct

Hoofdzakelijk voor tekstgeneratie, chatvoltooiing en extraheren van inhoudsinformatie, enzovoort.

**Phi-3-mini**

Het 3,8 miljard parameters tellende taalmodel is beschikbaar op Microsoft Foundry, Hugging Face en Ollama. Phi-3 modellen presteren aanzienlijk beter dan taalmodellen met gelijke en grotere omvang op belangrijke benchmarks (zie benchmarkcijfers hieronder, hogere cijfers zijn beter). Phi-3-mini presteert beter dan modellen met een dubbele grootte, terwijl Phi-3-small en Phi-3-medium betere prestaties leveren dan grotere modellen, inclusief GPT-3.5.

**Phi-3-small & medium**

Met slechts 7 miljard parameters verslaat Phi-3-small GPT-3.5T op diverse benchmarks voor taal, redeneren, programmeren en wiskunde.

De Phi-3-medium met 14 miljard parameters zet deze trend voort en overtreft de Gemini 1.0 Pro.

**Phi-3.5-mini**

We kunnen het zien als een upgrade van Phi-3-mini. Terwijl het aantal parameters gelijk blijft, verbetert het de ondersteuning voor meerdere talen (ondersteunt meer dan 20 talen: Arabisch, Chinees, Tsjechisch, Deens, Nederlands, Engels, Fins, Frans, Duits, Hebreeuws, Hongaars, Italiaans, Japans, Koreaans, Noors, Pools, Portugees, Russisch, Spaans, Zweeds, Thai, Turks, Oekraïens) en voegt het sterkere ondersteuning toe voor lange contexten.

Phi-3.5-mini met 3,8 miljard parameters presteert beter dan taalmodellen van dezelfde grootte en is gelijkwaardig aan modellen met het dubbele aantal parameters.

### Phi-3 / 3.5 Vision

We kunnen het Instruct-model van Phi-3/3.5 zien als Phi’s vermogen om te begrijpen, en Vision is wat Phi ogen geeft om de wereld te begrijpen.


**Phi-3-Vision**

Phi-3-vision, met slechts 4,2 miljard parameters, zet deze trend voort en overtreft grotere modellen zoals Claude-3 Haiku en Gemini 1.0 Pro V op algemene visuele redeneertaken, OCR, en het begrijpen van tabellen en diagrammen.


**Phi-3.5-Vision**

Phi-3.5-Vision is ook een upgrade van Phi-3-Vision en voegt ondersteuning toe voor meerdere afbeeldingen. Je kunt het zien als een verbetering in visie: niet alleen kunnen er afbeeldingen worden gezien, maar ook video’s.

Phi-3.5-vision presteert beter dan grotere modellen zoals Claude-3.5 Sonnet en Gemini 1.5 Flash op OCR, het begrijpen van tabellen en grafieken, en is gelijkwaardig in algemene visuele kennisredeneringstaken. Ondersteunt multi-frame input, d.w.z. redeneren op meerdere invoerafbeeldingen.


### Phi-3.5-MoE

***Mixture of Experts(MoE)*** maakt het mogelijk om modellen te pretrainen met veel minder rekenkracht, wat betekent dat je het model- of datasetformaat dramatisch kunt opschalen met hetzelfde compute-budget als een dense model. Met name een MoE-model zou dezelfde kwaliteit als zijn dense tegenhanger veel sneller moeten bereiken tijdens pretraining.

Phi-3.5-MoE bestaat uit 16x3.8B expertmodules. Phi-3.5-MoE met slechts 6,6 miljard actieve parameters behaalt een vergelijkbaar niveau van redeneren, taalbegrip en rekenen als veel grotere modellen.

We kunnen het Phi-3/3.5 Familielmodel gebruiken op basis van verschillende scenario’s. In tegenstelling tot LLM’s kun je Phi-3/3.5-mini of Phi-3/3.5-Vision implementeren op edge-apparaten.


## Hoe gebruik je Phi-3/3.5 Familielmodellen

We hopen Phi-3/3.5 in verschillende scenario’s te gebruiken. Vervolgens zullen we Phi-3/3.5 in verschillende scenario’s toepassen.

![phi3](../../../translated_images/nl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferentie via Cloud APIs

**Microsoft Foundry Modellen**

> **Let op:** GitHub Modellen worden beëindigd eind juli 2026. [Microsoft Foundry Modellen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) zijn de directe vervanging.

Microsoft Foundry Modellen is de meest directe manier. Je kunt snel toegang krijgen tot het Phi-3/3.5-Instruct-model via de Foundry modelcatalogus. In combinatie met de Azure AI Inference SDK / OpenAI SDK kun je via code de API aanroepen om de Phi-3/3.5-Instruct oproep te voltooien. Je kunt ook verschillende effecten testen via de Playground.

- Demo: Vergelijking van de effecten van Phi-3-mini en Phi-3.5-mini in Chinese scenario's

![phi3](../../../translated_images/nl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/nl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Of als je de visie- en MoE-modellen wilt gebruiken, kun je Microsoft Foundry gebruiken om de oproep te voltooien. Als je geïnteresseerd bent, kun je de Phi-3 Cookbook lezen om te leren hoe je Phi-3/3.5 Instruct, Vision, MoE oproept via Microsoft Foundry [Klik op deze link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Naast de cloud-gebaseerde Microsoft Foundry Modellencatalogus kun je ook [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) gebruiken om gerelateerde oproepen uit te voeren. Je kunt NVIDIA NIM bezoeken om API-oproepen van de Phi-3/3.5 Familie te voltooien. NVIDIA NIM (NVIDIA Inference Microservices) is een set van versnelde inferentie-microservices die ontwikkelaars helpen AI-modellen efficiënt te implementeren in verschillende omgevingen, waaronder clouds, datacenters en werkstations.

Hier zijn enkele belangrijke functies van NVIDIA NIM:

- **Eenvoud van Implementatie:** NIM maakt het mogelijk AI-modellen met één commando uit te rollen, waardoor integratie in bestaande workflows eenvoudig is.
- **Geoptimaliseerde Prestaties:** Het maakt gebruik van NVIDIA’s voorgeoptimaliseerde inferentiemotoren, zoals TensorRT en TensorRT-LLM, om lage latentie en hoge doorvoer te garanderen.
- **Schaalbaarheid:** NIM ondersteunt autoscaling op Kubernetes, waardoor het effectief kan omgaan met variërende workloads.
- **Beveiliging en Controle:** Organisaties kunnen de controle over hun data en applicaties behouden door NIM-microservices zelf te hosten op hun eigen beheerde infrastructuur.
- **Standaard API's:** NIM biedt branche-standaard API's, waardoor het eenvoudig is om AI-toepassingen zoals chatbots, AI-assistenten en meer te bouwen en te integreren.

NIM maakt deel uit van NVIDIA AI Enterprise, dat tot doel heeft de inzet en operationalisatie van AI-modellen te vereenvoudigen, zodat deze efficiënt draaien op NVIDIA GPU's.

- Demo: Gebruik van NVIDIA NIM om Phi-3.5-Vision-API aan te roepen [[Klik op deze link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaal draaien
Inferentie met betrekking tot Phi-3, of een taalmodel zoals GPT-3, verwijst naar het proces van het genereren van antwoorden of voorspellingen op basis van de ontvangen input. Wanneer je een prompt of vraag aan Phi-3 geeft, gebruikt het zijn getrainde neuraal netwerk om het meest waarschijnlijke en relevante antwoord af te leiden door patronen en relaties in de trainingsdata te analyseren.

**Hugging Face Transformer**
Hugging Face Transformers is een krachtige bibliotheek ontworpen voor natuurlijke taalverwerking (NLP) en andere machine learning taken. Hier zijn enkele belangrijke punten:

1. **Voorgetrainde modellen**: Het biedt duizenden voorgetrainde modellen die gebruikt kunnen worden voor diverse taken zoals tekstclassificatie, named entity recognition, vraag en antwoord, samenvatting, vertaling en tekstgeneratie.

2. **Framework interoperabiliteit**: De bibliotheek ondersteunt meerdere deep learning frameworks, waaronder PyTorch, TensorFlow en JAX. Dit stelt je in staat een model in het ene framework te trainen en in een ander te gebruiken.

3. **Multimodale mogelijkheden**: Naast NLP ondersteunt Hugging Face Transformers ook taken in computer vision (bijv. beeldclassificatie, objectdetectie) en audioverwerking (bijv. spraakherkenning, audioclassificatie).

4. **Gebruiksgemak**: De bibliotheek biedt API's en tools om gemakkelijk modellen te downloaden en fijn af te stemmen, waardoor het toegankelijk is voor zowel beginners als experts.

5. **Community en bronnen**: Hugging Face heeft een levendige community en uitgebreide documentatie, tutorials en handleidingen om gebruikers op weg te helpen en het meeste uit de bibliotheek te halen.
[officiële documentatie](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) of hun [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dit is de meest gebruikte methode, maar vereist ook GPU-versnelling. Scenario's zoals Vision en MoE vereisen immers veel rekencapaciteit, wat erg traag zal zijn op CPU als ze niet gequantiseerd zijn.


- Demo: Gebruik van Transformer om Phi-3.5-Instruct aan te roepen [Klik op deze link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-Vision aan te roepen [Klik op deze link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-MoE aan te roepen [Klik op deze link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) is een platform dat het eenvoudiger maakt om grote taalmodellen (LLM's) lokaal op je machine te draaien. Het ondersteunt verschillende modellen zoals Llama 3.1, Phi 3, Mistral en Gemma 2, onder andere. Het platform vereenvoudigt het proces door modelgewichten, configuratie en data in één pakket samen te bundelen, waardoor het toegankelijker wordt voor gebruikers om hun eigen modellen aan te passen en te creëren. Ollama is beschikbaar voor macOS, Linux en Windows. Het is een geweldig hulpmiddel als je wilt experimenteren met of LLM's wilt inzetten zonder afhankelijk te zijn van cloudservices. Ollama is de meest directe manier, je hoeft alleen het volgende commando uit te voeren.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) is Microsoft's offline uitvoering op het apparaat zelf om modellen zoals Phi volledig op je eigen hardware te draaien - geen Azure-abonnement, API-sleutel of netwerkverbinding nodig. Het kiest automatisch de beste beschikbare uitvoeringsprovider (NPU, GPU of CPU) en biedt een OpenAI-compatibele endpoint, zodat bestaande `openai`/Azure AI Inference SDK code er met minimale aanpassingen naartoe kan wijzen. Zie de [Foundry Local documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om aan de slag te gaan.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) is een platformonafhankelijke accelerator voor inferentie en training van machine learning modellen. ONNX Runtime voor Generatieve AI (GENAI) is een krachtig hulpmiddel dat je helpt generatieve AI-modellen efficiënt op diverse platforms uit te voeren.

## Wat is ONNX Runtime?
ONNX Runtime is een open source project dat high-performance inferentie van machine learning modellen mogelijk maakt. Het ondersteunt modellen in het Open Neural Network Exchange (ONNX) formaat, een standaard voor het representeren van machine learning modellen. ONNX Runtime inferentie kan snellere klantervaringen en lagere kosten mogelijk maken, en ondersteunt modellen van deep learning frameworks zoals PyTorch en TensorFlow/Keras evenals klassieke machine learning bibliotheken zoals scikit-learn, LightGBM, XGBoost, enz. ONNX Runtime is compatibel met verschillende hardware, drivers en besturingssystemen, en biedt optimale prestaties door gebruik te maken van hardwareversnellers waar mogelijk samen met grafiekoptimalisaties en -transformaties.

## Wat is Generatieve AI?
Generatieve AI verwijst naar AI-systemen die nieuwe content kunnen genereren, zoals tekst, afbeeldingen of muziek, gebaseerd op de data waarop ze getraind zijn. Voorbeelden zijn taalmodellen zoals GPT-3 en beeldgeneratiemodellen zoals Stable Diffusion. De ONNX Runtime voor GenAI bibliotheek biedt de generatieve AI-cyclus voor ONNX modellen, inclusief inferentie met ONNX Runtime, logits verwerking, zoeken en sampling, en KV cachebeheer.

## ONNX Runtime voor GENAI
ONNX Runtime voor GENAI breidt de mogelijkheden van ONNX Runtime uit om generatieve AI modellen te ondersteunen. Hier zijn enkele belangrijke kenmerken:

- **Brede platformondersteuning:** Het werkt op diverse platforms, waaronder Windows, Linux, macOS, Android en iOS.
- **Modelondersteuning:** Het ondersteunt vele populaire generatieve AI modellen, zoals LLaMA, GPT-Neo, BLOOM en meer.
- **Prestatie-optimalisatie:** Het bevat optimalisaties voor verschillende hardwareversnellers zoals NVIDIA GPU's, AMD GPU's, en meer2.
- **Gebruiksgemak:** Het biedt API's voor eenvoudige integratie in applicaties, waarmee je tekst, afbeeldingen en andere content kunt genereren met minimale code.
- Gebruikers kunnen een hoge-niveau generate() methode aanroepen, of elke iteratie van het model in een lus uitvoeren, waarbij telkens één token wordt gegenereerd en optioneel generatieparameters binnen de lus worden bijgewerkt.
- ONNX runtime ondersteunt ook greedy/beam search en TopP, TopK sampling voor het genereren van tokenreeks en ingebouwde logits verwerking zoals repetitie-penalty's. Je kunt ook eenvoudig aangepaste scorings toevoegen.

## Aan de slag
Om aan de slag te gaan met ONNX Runtime voor GENAI kun je de volgende stappen volgen:

### Installeer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installeer de Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Voer een model uit: Hier is een eenvoudig voorbeeld in Python:
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
### Demo:Gebruik ONNX Runtime GenAI om Phi-3.5-Vision aan te roepen


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


**Overigen**

Naast de referentiemethoden van ONNX Runtime, Ollama en Foundry Local kunnen we ook de referentie van kwantitatieve modellen aanvullen gebaseerd op modelreferentiemethoden geleverd door verschillende fabrikanten. Zoals Apple MLX framework met Apple Metal, Qualcomm QNN met NPU, Intel OpenVINO met CPU/GPU, enzovoort. Je kunt ook meer inhoud vinden in de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Meer

We hebben de basis van de Phi-3/3.5-familie geleerd, maar om meer te weten te komen over SLM hebben we meer kennis nodig. Je kunt de antwoorden vinden in de Phi-3 Cookbook. Wil je meer leren, bezoek dan de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->