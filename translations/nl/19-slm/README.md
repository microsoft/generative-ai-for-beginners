# Introductie tot Kleine Taalmodellen voor Generatieve AI voor Beginners
Generatieve AI is een fascinerend gebied binnen kunstmatige intelligentie dat zich richt op het creëren van systemen die in staat zijn nieuwe content te genereren. Deze content kan variëren van tekst en afbeeldingen tot muziek en zelfs complete virtuele omgevingen. Een van de meest opwindende toepassingen van generatieve AI is op het gebied van taalmodellen.

## Wat zijn Kleine Taalmodellen?

Een Klein Taalmodel (SLM) is een verkleinde variant van een groot taalmodel (LLM), waarbij veel van dezelfde architectonische principes en technieken van LLM's worden gebruikt, maar met een aanzienlijk verminderde computationele voetafdruk.

SLM's zijn een subset van taalmodellen die zijn ontworpen om mensachtige tekst te genereren. In tegenstelling tot hun grotere tegenhangers, zoals GPT-4, zijn SLM's compacter en efficiënter, wat ze ideaal maakt voor toepassingen waar computationele middelen beperkt zijn. Ondanks hun kleinere omvang kunnen ze nog steeds verschillende taken uitvoeren. Typisch worden SLM's geconstrueerd door LLM's te comprimeren of te distilleren, met als doel een aanzienlijk deel van de functionaliteit en linguïstische capaciteiten van het oorspronkelijke model te behouden. Deze reductie in modelgrootte vermindert de algehele complexiteit, waardoor SLM's efficiënter zijn qua geheugengebruik en computationele vereisten. Ondanks deze optimalisaties kunnen SLM's nog steeds een breed scala aan taken in natuurlijke taalverwerking (NLP) uitvoeren:

- Tekstgeneratie: Het creëren van samenhangende en contextueel relevante zinnen of paragrafen.
- Tekstvoltooiing: Het voorspellen en afmaken van zinnen op basis van een gegeven prompt.
- Vertaling: Het omzetten van tekst van de ene taal naar de andere.
- Samenvatting: Het inkorten van lange stukken tekst tot kortere, beter verteerbare samenvattingen.

Hoewel dit gepaard gaat met enkele concessies in prestaties of diepgang van begrip vergeleken met hun grotere tegenhangers.

## Hoe Werken Kleine Taalmodellen?
SLM's worden getraind op enorme hoeveelheden tekstgegevens. Tijdens het trainen leren ze de patronen en structuren van taal, waardoor ze tekst kunnen genereren die zowel grammaticaal correct als contextueel passend is. Het trainingsproces omvat:

- Gegevensverzameling: Het verzamelen van grote datasets met tekst uit diverse bronnen.
- Voorbewerking: Het schoonmaken en organiseren van de data om deze geschikt te maken voor training.
- Training: Het gebruiken van machine learning-algoritmen om het model te leren tekst te begrijpen en genereren.
- Fijnregelen: Het aanpassen van het model om de prestaties op specifieke taken te verbeteren.

De ontwikkeling van SLM's sluit aan bij de groeiende behoefte aan modellen die kunnen worden ingezet in omgevingen met beperkte middelen, zoals mobiele apparaten of edge computing-platforms, waar volledige LLM's onpraktisch zijn vanwege hun hoge resourceverbruik. Door te focussen op efficiëntie balanceren SLM's prestaties met toegankelijkheid, wat bredere toepassing in diverse domeinen mogelijk maakt.

![slm](../../../translated_images/nl/slm.4058842744d0444a.webp)

## Leerdoelen

In deze les hopen we kennis over SLM te introduceren en dit te combineren met Microsoft Phi-3 om verschillende scenario's in tekstcontent, visie en MoE te leren.

Aan het einde van deze les zou je de volgende vragen moeten kunnen beantwoorden:

- Wat is SLM?
- Wat is het verschil tussen SLM en LLM?
- Wat is de Microsoft Phi-3/3.5 Familie?
- Hoe voer je inferentie uit met de Microsoft Phi-3/3.5 Familie?

Klaar? Laten we beginnen.

## De Verschillen tussen Grote Taalmodellen (LLM's) en Kleine Taalmodellen (SLM's)

Zowel LLM's als SLM's zijn gebaseerd op fundamentele principes van probabilistische machine learning, met vergelijkbare benaderingen in architectonisch ontwerp, trainingsmethodologieën, datageneratieprocessen en modelevaluatietechnieken. Desalniettemin onderscheiden verschillende belangrijke factoren deze twee typen modellen.

## Toepassingen van Kleine Taalmodellen

SLM's hebben een breed scala aan toepassingen, waaronder:

- Chatbots: Het bieden van klantenservice en interactie met gebruikers via conversaties.
- Contentcreatie: Het assisteren van schrijvers door ideeën te genereren of zelfs hele artikelen te schrijven.
- Onderwijs: Het helpen van studenten bij schrijfopdrachten of het leren van nieuwe talen.
- Toegankelijkheid: Het creëren van hulpmiddelen voor mensen met een beperking, zoals tekst-naar-spraak systemen.

**Grootte**
  
Een belangrijke onderscheiding tussen LLM's en SLM's ligt in de schaal van de modellen. LLM's, zoals ChatGPT (GPT-4), kunnen ongeveer 1,76 biljoen parameters bevatten, terwijl open-source SLM's zoals Mistral 7B ontworpen zijn met aanzienlijk minder parameters—ongeveer 7 miljard. Dit verschil is voornamelijk terug te voeren op verschillen in modelarchitectuur en trainingsprocessen. Bijvoorbeeld, ChatGPT gebruikt een zelf-attentiemechanisme binnen een encoder-decoder framework, terwijl Mistral 7B gebruikmaakt van sliding window attention, wat efficiëntere training binnen een decoder-only model mogelijk maakt. Deze architecturale variatie heeft grote gevolgen voor de complexiteit en prestaties van deze modellen.

**Begrip**

SLM's zijn meestal geoptimaliseerd voor prestaties binnen specifieke domeinen, wat ze zeer gespecialiseerd maakt maar mogelijk beperkt in hun vermogen tot breed contextueel begrip over meerdere kennisgebieden. LLM's daarentegen streven ernaar menselijke intelligentie op een meer omvattend niveau te simuleren. Getraind op enorme, diverse datasets, zijn LLM's ontworpen om goed te presteren in diverse domeinen, met grotere veelzijdigheid en aanpasbaarheid. Daardoor zijn LLM's geschikter voor een breder scala aan downstream-taken, zoals natuurlijke taalverwerking en programmeren.

**Computatie**

Het trainen en inzetten van LLM's zijn resource-intensieve processen die vaak aanzienlijke computationele infrastructuur vereisen, waaronder grootschalige GPU-clusters. Het trainen van een model zoals ChatGPT vanaf nul kan duizenden GPU's over langdurige periodes vereisen. Daarentegen zijn SLM's, met hun kleinere aantal parameters, toegankelijker qua computationele middelen. Modellen zoals Mistral 7B kunnen getraind en uitgevoerd worden op lokale machines met matige GPU-capaciteiten, hoewel de training nog steeds meerdere uren op meerdere GPU's vergt.

**Bias**

Bias is een bekend probleem in LLM's, hoofdzakelijk vanwege de aard van de trainingsdata. Deze modellen vertrouwen vaak op ruwe, openbaar beschikbare internetdata, die bepaalde groepen kunnen ondervertegenwoordigen of verkeerd kunnen weergeven, foutieve labeling kunnen introduceren, of taalkundige vooroordelen kunnen reflecteren beïnvloed door dialecten, geografische variaties en grammaticale regels. Bovendien kan de complexiteit van LLM-architecturen bias onopgemerkt versterken zonder zorgvuldige fijnafstemming. Aan de andere kant zijn SLM's, die getraind worden op meer beperkte, domeinspecifieke datasets, van nature minder vatbaar voor dergelijke biases, hoewel ze er niet immuun voor zijn.

**Inferentie**

De kleinere omvang van SLM's biedt een aanzienlijk voordeel in inferentiesnelheid, waardoor ze outputs efficiënt kunnen genereren op lokale hardware zonder noodzaak voor uitgebreide parallelle verwerking. LLM's vereisen vanwege hun grootte en complexiteit vaak aanzienlijke parallelle computationele middelen om acceptabele inferentietijden te bereiken. Het gelijktijdig gebruik door meerdere gebruikers vertraagt daarnaast de reactietijden van LLM's, vooral bij grootschalige inzet.

Samengevat, hoewel zowel LLM's als SLM's een gemeenschappelijke basis in machine learning delen, verschillen ze aanzienlijk in modelgrootte, resourcevereisten, contextueel begrip, vatbaarheid voor bias en inferentiesnelheid. Deze verschillen weerspiegelen hun respectievelijke geschiktheid voor verschillende toepassingen, waarbij LLM's veelzijdiger maar resource-intensiever zijn, en SLM's domeinspecifieke efficiëntie bieden met lagere computationele eisen.

***Opmerking: In deze les introduceren we SLM aan de hand van Microsoft Phi-3 / 3.5 als voorbeeld.***

## Introductie Phi-3 / Phi-3.5 Familie

De Phi-3 / 3.5 Familie richt zich voornamelijk op tekst-, visie- en Agent (MoE) toepassingsscenario's:

### Phi-3 / 3.5 Instruct

Voornamelijk voor tekstgeneratie, chatvoltooiing, en informatiewinning uit content, etc.

**Phi-3-mini**

Het 3,8 miljard parameters tellende taalmodel is beschikbaar op Microsoft Foundry, Hugging Face en Ollama. Phi-3-modellen presteren significant beter dan taalmodellen van gelijke en grotere omvang op belangrijke benchmarks (zie benchmarkcijfers hieronder, hogere cijfers zijn beter). Phi-3-mini overtreft modellen die twee keer zo groot zijn, terwijl Phi-3-small en Phi-3-medium grotere modellen, waaronder GPT-3.5, overtreffen.

**Phi-3-small & medium**

Met slechts 7 miljard parameters verslaat Phi-3-small GPT-3.5T op diverse benchmarks voor taal, redeneren, coderen en wiskunde.

Phi-3-medium met 14 miljard parameters zet deze trend voort en presteert beter dan Gemini 1.0 Pro.

**Phi-3.5-mini**

We kunnen dit zien als een upgrade van Phi-3-mini. Hoewel het aantal parameters ongewijzigd blijft, verbetert het de ondersteuning voor meerdere talen (ondersteunt meer dan 20 talen: Arabisch, Chinees, Tsjechisch, Deens, Nederlands, Engels, Fins, Frans, Duits, Hebreeuws, Hongaars, Italiaans, Japans, Koreaans, Noors, Pools, Portugees, Russisch, Spaans, Zweeds, Thais, Turks, Oekraïens) en voegt sterkere ondersteuning toe voor lange contexten.

Phi-3.5-mini met 3,8 miljard parameters presteert beter dan taalmodellen van dezelfde omvang en is gelijkwaardig aan modellen van twee keer die grootte.

### Phi-3 / 3.5 Visie

We kunnen het Instruct-model van Phi-3/3.5 zien als Phis vermogen om te begrijpen, en Visie geeft Phi ogen om de wereld te begrijpen.


**Phi-3-Visie**

Phi-3-Visie, met slechts 4,2 miljard parameters, zet deze trend voort en presteert beter dan grotere modellen zoals Claude-3 Haiku en Gemini 1.0 Pro V op algemene visuele redeneertaken, OCR, en begripsopdrachten met tabellen en diagrammen.


**Phi-3.5-Visie**

Phi-3.5-Visie is ook een upgrade van Phi-3-Visie, met ondersteuning voor meerdere afbeeldingen. Je kunt het zien als een verbetering in visie, niet alleen kun je plaatjes zien, maar ook video’s.

Phi-3.5-Visie presteert beter dan grotere modellen zoals Claude-3.5 Sonnet en Gemini 1.5 Flash op OCR-, tabel- en grafiekbegripstaken en is gelijkwaardig op algemene visuele kennisredentietaken. Ondersteunt multi-frame input, oftewel redeneren over meerdere invoerafbeeldingen.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** maakt het mogelijk modellen te pretrainen met veel minder compute, wat betekent dat je het model of de dataset met hetzelfde computebudget dramatisch kunt opschalen vergeleken met een dense model. Een MoE-model zou in het bijzonder tijdens pretraining dezelfde kwaliteit moeten bereiken als zijn dense tegenhanger, maar veel sneller.

Phi-3.5-MoE bestaat uit 16x3,8 miljard expertenmodules. Phi-3.5-MoE met slechts 6,6 miljard actieve parameters bereikt een vergelijkbaar niveau van redeneren, taalbegrip en wiskunde als veel grotere modellen.

We kunnen het Phi-3/3.5-familie model gebruiken op basis van verschillende scenario's. In tegenstelling tot LLM kun je Phi-3/3.5-mini of Phi-3/3.5-Visie inzetten op edge-apparaten.


## Hoe Phi-3/3.5 Familie modellen te gebruiken

We hopen Phi-3/3.5 in verschillende scenario’s te gebruiken. Vervolgens zullen we Phi-3/3.5 toepassen op basis van verschillende scenario’s.

![phi3](../../../translated_images/nl/phi3.655208c3186ae381.webp)

### Inferentie via cloud-API's

**Microsoft Foundry-modellen**

> **Opmerking:** GitHub Models wordt eind juli 2026 uitgefaseerd. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) is de directe vervanging.

Microsoft Foundry Models is de meest directe manier. Je kunt snel toegang krijgen tot het Phi-3/3.5-Instruct model via de Foundry modelcatalogus. In combinatie met de Azure AI Inference SDK / OpenAI SDK kun je via code de API benaderen om een Phi-3/3.5-Instruct oproep te voltooien. Je kunt ook verschillende effecten testen in de Playground.

- Demo: Vergelijking van de effecten van Phi-3-mini en Phi-3.5-mini in Chinese scenario's

![phi3](../../../translated_images/nl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/nl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Of als we de visie- en MoE-modellen willen gebruiken, kun je Microsoft Foundry gebruiken om de oproep te voltooien. Mocht je geïnteresseerd zijn, dan kun je de Phi-3 Cookbook lezen om te leren hoe je Phi-3/3.5 Instruct, Visie, MoE aanroept via Microsoft Foundry [Klik op deze link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Naast de cloudgebaseerde Microsoft Foundry Models-catalogus kun je ook [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) gebruiken om gerelateerde oproepen te voltooien. Je kunt NVIDIA NIM bezoeken om de API-oproepen van de Phi-3/3.5 Familie te voltooien. NVIDIA NIM (NVIDIA Inference Microservices) is een set geoptimaliseerde inferentiemicroservices die ontwikkelaars helpt AI-modellen efficiënt te implementeren in verschillende omgevingen, waaronder clouds, datacenters en werkstations.

Hier zijn enkele belangrijke kenmerken van NVIDIA NIM:

- **Eenvoud van implementatie:** NIM maakt het mogelijk AI-modellen met één commando uit te rollen, wat integratie in bestaande workflows eenvoudig maakt.

- **Geoptimaliseerde prestaties:** Het maakt gebruik van NVIDIA’s vooraf geoptimaliseerde inferentie-engines, zoals TensorRT en TensorRT-LLM, om lage latency en hoge doorvoer te garanderen.
- **Schaalbaarheid:** NIM ondersteunt autoscaling op Kubernetes, waardoor het effectief met wisselende werklasten om kan gaan.
- **Beveiliging en controle:** Organisaties kunnen controle behouden over hun gegevens en applicaties door NIM-microservices zelf te hosten op hun eigen beheerde infrastructuur.
- **Standaard-API's:** NIM biedt industriestandaard API's, wat het gemakkelijk maakt om AI-toepassingen zoals chatbots, AI-assistenten en meer te bouwen en te integreren.

NIM maakt deel uit van NVIDIA AI Enterprise, dat tot doel heeft het inzetten en operationaliseren van AI-modellen te vereenvoudigen, zodat deze efficiënt draaien op NVIDIA GPU's.

- Demo: Het gebruik van NVIDIA NIM om Phi-3.5-Vision-API aan te roepen  [[Klik op deze link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaal uitvoeren
Inferentie met betrekking tot Phi-3, of een taalmodel zoals GPT-3, verwijst naar het proces van het genereren van antwoorden of voorspellingen op basis van de ingevoerde gegevens. Wanneer je een prompt of vraag aan Phi-3 geeft, gebruikt het zijn getrainde neuraal netwerk om de meest waarschijnlijke en relevante reactie af te leiden door patronen en relaties te analyseren in de data waarop het getraind is.

**Hugging Face Transformer**
Hugging Face Transformers is een krachtige bibliotheek ontworpen voor natuurlijke taalverwerking (NLP) en andere machine learning taken. Hier zijn enkele belangrijke punten over deze bibliotheek:

1. **Voorgetrainde modellen**: Het biedt duizenden voorgetrainde modellen die gebruikt kunnen worden voor diverse taken zoals tekstclassificatie, benoemde entiteitsherkenning, vraagbeantwoording, samenvatten, vertaling en tekstgeneratie.

2. **Framework-interoperabiliteit**: De bibliotheek ondersteunt meerdere diepe-leerframeworks, waaronder PyTorch, TensorFlow en JAX. Dit maakt het mogelijk een model in één framework te trainen en in een ander te gebruiken.

3. **Multimodale mogelijkheden**: Naast NLP ondersteunt Hugging Face Transformers ook taken in computer vision (zoals beeldclassificatie, objectdetectie) en audioprocessing (zoals spraakherkenning, audioclassificatie).

4. **Gebruiksgemak**: De bibliotheek biedt API's en tools om eenvoudig modellen te downloaden en fijn af te stemmen, waardoor het toegankelijk is voor zowel beginners als experts.

5. **Community en bronnen**: Hugging Face heeft een levendige community en uitgebreide documentatie, tutorials en handleidingen om gebruikers te helpen aan de slag te gaan en het meeste uit de bibliotheek te halen.
[officiële documentatie](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) of hun [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dit is de meest gebruikte methode, maar het vereist ook GPU-versnelling. Scenario's zoals Vision en MoE vereisen immers veel berekeningen, die op CPU zeer traag zullen zijn als ze niet gequantiseerd zijn.


- Demo: Gebruik van Transformer om Phi-3.5-Instruct aan te roepen [Klik op deze link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-Vision aan te roepen [Klik op deze link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-MoE aan te roepen [Klik op deze link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) is een platform ontworpen om het gemakkelijker te maken om grote taalmodellen (LLM's) lokaal op je machine te draaien. Het ondersteunt verschillende modellen zoals Llama 3.1, Phi 3, Mistral, en Gemma 2, onder andere. Het platform vereenvoudigt het proces door modelgewichten, configuratie en data in één pakket te bundelen, waardoor het toegankelijker wordt voor gebruikers om hun eigen modellen aan te passen en te creëren. Ollama is beschikbaar voor macOS, Linux en Windows. Het is een uitstekend hulpmiddel als je wilt experimenteren met of LLM's wilt inzetten zonder afhankelijk te zijn van clouddiensten. Ollama is de meest directe manier, je hoeft alleen het volgende commando uit te voeren.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) is Microsofts offline, on-device runtime voor het draaien van modellen zoals Phi volledig op je eigen hardware – geen Azure-abonnement, API-sleutel, of netwerkverbinding nodig. Het kiest automatisch de beste beschikbare uitvoeringstool (NPU, GPU, of CPU) en biedt een OpenAI-compatibele endpoint, zodat bestaande `openai`/Azure AI Inference SDK-code er met minimale aanpassingen op kan wijzen. Zie de [Foundry Local documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om aan de slag te gaan.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) is een platformonafhankelijke inferentie- en trainingsversneller voor machine learning. ONNX Runtime voor Generatieve AI (GENAI) is een krachtig hulpmiddel dat je helpt generatieve AI-modellen efficiënt te draaien op diverse platforms.

## Wat is ONNX Runtime?
ONNX Runtime is een open-source project dat hoge prestaties bij inferentie van machine learning modellen mogelijk maakt. Het ondersteunt modellen in het Open Neural Network Exchange (ONNX) formaat, een standaard voor het representeren van machine learning modellen. ONNX Runtime inferentie kan snellere klantbelevingen en lagere kosten mogelijk maken, door ondersteuning van modellen uit diepe-leerframeworks zoals PyTorch en TensorFlow/Keras, evenals klassieke machine learning bibliotheken zoals scikit-learn, LightGBM, XGBoost, enzovoort. ONNX Runtime is compatibel met diverse hardware, drivers en besturingssystemen en biedt optimale prestaties door het benutten van hardwareversnellers waar mogelijk, naast graafoptimalisaties en transformaties.

## Wat is Generatieve AI?
Generatieve AI verwijst naar AI-systemen die nieuwe inhoud kunnen genereren, zoals tekst, afbeeldingen of muziek, gebaseerd op de data waarop ze getraind zijn. Voorbeelden zijn taalmodellen zoals GPT-3 en beeldgeneratiemodellen zoals Stable Diffusion. De ONNX Runtime voor GenAI bibliotheek levert de generatieve AI-lus voor ONNX-modellen, inclusief inferentie met ONNX Runtime, logitsverwerking, zoek- en samplingalgoritmen, en beheer van KV-cache.

## ONNX Runtime voor GENAI
ONNX Runtime voor GENAI breidt de mogelijkheden van ONNX Runtime uit om generatieve AI-modellen te ondersteunen. Hier zijn enkele belangrijke kenmerken:

- **Breed platformondersteuning:** Het werkt op verschillende platforms, waaronder Windows, Linux, macOS, Android en iOS.
- **Modelondersteuning:** Het ondersteunt veel populaire generatieve AI-modellen, zoals LLaMA, GPT-Neo, BLOOM en meer.
- **Prestatieoptimalisatie:** Het bevat optimalisaties voor verschillende hardwareversnellers zoals NVIDIA GPU's, AMD GPU's, en meer2.
- **Gebruiksgemak:** Het biedt API's voor eenvoudige integratie in applicaties, waarmee je met minimale code tekst, afbeeldingen en andere inhoud kunt genereren.
- Gebruikers kunnen een high-level generate()-methode aanroepen, of elke iteratie van het model in een lus uitvoeren, waarbij telkens één token wordt gegenereerd en optioneel generatieparameters worden bijgewerkt binnen de lus.
- ONNX Runtime ondersteunt ook greedy/beam search en TopP, TopK sampling om tokenreeksen te genereren en ingebouwde logitsverwerking zoals repetitie-straf. Je kunt ook eenvoudig aangepaste scoringsfuncties toevoegen.

## Aan de slag
Om te starten met ONNX Runtime voor GENAI, kun je de volgende stappen volgen:

### Installeer ONNX Runtime:
```Python
pip install onnxruntime
```
### Installeer de Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Draai een model: Hier is een eenvoudig voorbeeld in Python:
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
### Demo: Gebruik van ONNX Runtime GenAI om Phi-3.5-Vision aan te roepen


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

Naast ONNX Runtime, Ollama en Foundry Local referentiemethoden kunnen we ook de referentie van kwantitatieve modellen voltooien op basis van de modelleringsreferentiemethoden die door verschillende fabrikanten worden aangeboden. Zoals het Apple MLX-framework met Apple Metal, Qualcomm QNN met NPU, Intel OpenVINO met CPU/GPU, enzovoort. Je kunt ook meer inhoud vinden in de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Meer

We hebben de basis van Phi-3/3.5 familie geleerd, maar om meer over SLM te leren hebben we meer kennis nodig. Je kunt de antwoorden vinden in de Phi-3 Cookbook. Als je meer wilt leren, bezoek dan alsjeblieft de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->