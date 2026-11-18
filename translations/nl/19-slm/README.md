# Inleiding tot Kleine Taalmodellen voor Generatieve AI voor Beginners
Generatieve AI is een fascinerend gebied binnen kunstmatige intelligentie dat zich richt op het creëren van systemen die nieuwe content kunnen genereren. Deze content kan variëren van tekst en afbeeldingen tot muziek en zelfs volledige virtuele omgevingen. Een van de spannendste toepassingen van generatieve AI is op het gebied van taalmodellen.

## Wat zijn Kleine Taalmodellen?

Een Klein Taalmodel (KTM) is een verkleinde variant van een groot taalmodel (GTM), waarbij veel van de architectonische principes en technieken van GTM's worden gebruikt, maar met een aanzienlijk verminderde berekeningsbelasting.

KTM's zijn een subset van taalmodellen die zijn ontworpen om mensachtige tekst te genereren. In tegenstelling tot hun grotere tegenhangers, zoals GPT-4, zijn KTM's compacter en efficiënter, waardoor ze ideaal zijn voor toepassingen waarbij rekenmiddelen beperkt zijn. Ondanks hun kleinere formaat kunnen ze nog steeds diverse taken uitvoeren. Meestal worden KTM's opgebouwd door het comprimeren of destilleren van GTM's, met als doel een substantieel deel van de functionaliteit en linguïstische capaciteiten van het originele model te behouden. Deze verkleining van het model vermindert de algehele complexiteit, waardoor KTM's efficiënter zijn wat betreft zowel geheugengebruik als rekenvereisten. Ondanks deze optimalisaties kunnen KTM's nog steeds een breed scala aan natuurlijke taalverwerking (NLP) taken uitvoeren:

- Tekstgeneratie: Het creëren van coherente en contextueel relevante zinnen of paragrafen.
- Tekstvoltooiing: Het voorspellen en aanvullen van zinnen op basis van een gegeven prompt.
- Vertaling: Het omzetten van tekst van de ene taal naar de andere.
- Samenvatting: Het inkorten van lange teksten tot kortere, beter verteerbare samenvattingen.

Weliswaar met enkele compromissen in prestaties of diepgang van begrip vergeleken met hun grotere tegenhangers.

## Hoe Werken Kleine Taalmodellen?
KTM's worden getraind op enorme hoeveelheden tekstdata. Tijdens het trainen leren ze patronen en structuren van taal, waardoor ze in staat zijn tekst te genereren die grammaticaal correct en contextueel passend is. Het trainingsproces omvat:

- Dataverzameling: Het verzamelen van grote datasets met tekst uit diverse bronnen.
- Voorbewerking: Het schoonmaken en organiseren van de data om deze geschikt te maken voor training.
- Training: Het gebruiken van machine learning-algoritmes om het model te leren tekst te begrijpen en te genereren.
- Fijn afstellen: Het aanpassen van het model om de prestaties op specifieke taken te verbeteren.

De ontwikkeling van KTM's sluit aan bij de toenemende behoefte aan modellen die kunnen worden ingezet in omgevingen met beperkte middelen, zoals mobiele apparaten of edge computing platforms, waar full-scale GTM's onpraktisch kunnen zijn vanwege hun zware eisen aan resources. Door te focussen op efficiëntie balanceren KTM's prestaties met toegankelijkheid, waardoor ze breder toepasbaar zijn in verschillende domeinen.

![slm](../../../translated_images/nl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Leerdoelen

In deze les hopen we kennis over KTM te introduceren en deze te combineren met Microsoft Phi-3 om verschillende scenario's te leren in tekstinhoud, visie en MoE.

Aan het einde van deze les moet je de volgende vragen kunnen beantwoorden:

- Wat is een KTM?
- Wat is het verschil tussen KTM en GTM?
- Wat is de Microsoft Phi-3/3.5 familie?
- Hoe voer je inferentie uit met de Microsoft Phi-3/3.5 familie?

Klaar? Laten we aan de slag gaan.

## De Onderscheidingen tussen Grote Taalmodellen (GTM's) en Kleine Taalmodellen (KTM's)

Zowel GTM's als KTM's zijn gebouwd op fundamentele principes van probabilistische machine learning, waarbij vergelijkbare benaderingen worden gevolgd in hun architectonisch ontwerp, trainingsmethodologieën, data generaties en modellen evaluatietechnieken. Toch onderscheiden een aantal sleutelverschillen deze twee typen modellen.

## Toepassingen van Kleine Taalmodellen

KTM's hebben een breed scala aan toepassingen, waaronder:

- Chatbots: Het bieden van klantenservice en het voeren van gesprekken met gebruikers.
- Contentcreatie: Het assisteren van schrijvers door ideeën te genereren of zelfs gehele artikelen te schrijven.
- Onderwijs: Het helpen van studenten bij schrijfopdrachten of het leren van nieuwe talen.
- Toegankelijkheid: Het creëren van hulpmiddelen voor personen met beperkingen, zoals tekst-naar-spraak systemen.

**Grootte**
  
Een primaire onderscheid tussen GTM's en KTM's ligt in de schaal van de modellen. GTM's, zoals ChatGPT (GPT-4), kunnen naar schatting 1,76 biljoen parameters bevatten, terwijl open-source KTM's zoals Mistral 7B zijn ontworpen met aanzienlijk minder parameters—ongeveer 7 miljard. Dit verschil is voornamelijk te wijten aan verschillen in modelarchitectuur en trainingsprocessen. Bijvoorbeeld, ChatGPT gebruikt een self-attention mechanisme binnen een encoder-decoder framework, terwijl Mistral 7B sliding window attention gebruikt, wat efficiënter trainen mogelijk maakt binnen een decodermodel. Deze architectonische variatie heeft grote gevolgen voor de complexiteit en prestaties van deze modellen.

**Begrip**

KTM's zijn doorgaans geoptimaliseerd voor prestaties binnen specifieke domeinen, waardoor ze zeer gespecialiseerd maar mogelijk beperkt zijn in hun vermogen om brede contextuele kennis uit meerdere vakgebieden te bieden. GTM's daarentegen streven ernaar menselijke intelligentie op een uitgebreider niveau na te bootsen. Getraind op enorme, diverse datasets, zijn GTM's ontworpen om goed te presteren in diverse domeinen, wat grotere veelzijdigheid en aanpasbaarheid biedt. Daardoor zijn GTM's geschikter voor een breder scala aan downstreamtaken zoals natuurlijke taalverwerking en programmeren.

**Rekenen**

Het trainen en inzetten van GTM's zijn resource-intensieve processen, die vaak aanzienlijke rekeninfrastructuur vereisen, inclusief grootschalige GPU-clusters. Bijvoorbeeld, het trainen van een model als ChatGPT vanaf nul kan duizenden GPU's over langere periodes nodig hebben. KTM's met hun kleinere parameteraantallen zijn in termen van benodigde rekenkracht toegankelijker. Modellen zoals Mistral 7B kunnen getraind en uitgevoerd worden op lokale machines met matige GPU-mogelijkheden, hoewel het trainen nog steeds enkele uren op meerdere GPU's vraagt.

**Bias**

Bias is een bekend probleem bij GTM's, voornamelijk vanwege de aard van de trainingsdata. Deze modellen vertrouwen vaak op ruwe, open beschikbare data van het internet, die bepaalde groepen ondervertegenwoordigen of verkeerd voorstellen, onjuiste labeling kunnen introduceren, of linguïstische bias vertonen beïnvloed door dialect, geografische variaties en grammaticale regels. Bovendien kan de complexiteit van GTM-architecturen bias onbedoeld versterken, wat onopgemerkt kan blijven zonder zorgvuldige fijn afstemming. KTM's, die worden getraind op meer beperkte, domeinspecifieke datasets, zijn van nature minder vatbaar voor dergelijke biases, hoewel ze er niet helemaal immuun voor zijn.

**Inferentie**

De kleinere omvang van KTM's geeft hen een aanzienlijk voordeel qua inferentiesnelheid, waardoor ze efficiënt output kunnen genereren op lokale hardware zonder behoefte aan uitgebreide parallelle verwerking. GTM's daarentegen vereisen door hun grootte en complexiteit vaak aanzienlijke parallelle rekenbronnen om acceptabele inferentietijden te bereiken. De aanwezigheid van meerdere gelijktijdige gebruikers vertraagt bovendien de reactietijden van GTM's, vooral bij grootschalige inzet.

Samengevat: hoewel zowel GTM's als KTM's een fundamentele basis delen in machine learning, verschillen ze aanzienlijk qua modelgrootte, resource-eisen, contextueel begrip, vatbaarheid voor bias en inferentiesnelheid. Deze verschillen weerspiegelen hun respectieve geschiktheid voor verschillende use cases, waarbij GTM's veelzijdiger maar resource-intensief zijn, en KTM's meer domeinspecifieke efficiëntie bieden met verminderde rekenvereisten.

***Opmerking: In deze les introduceren we KTM aan de hand van Microsoft Phi-3 / 3.5 als voorbeeld.***

## Introductie van Phi-3 / Phi-3.5 Familie

De Phi-3 / 3.5 Familie richt zich voornamelijk op tekst-, visie- en Agent (MoE) toepassingsscenario's:

### Phi-3 / 3.5 Instruct

Voornamelijk voor tekstgeneratie, chatvoltooiing en contentinformatie-extractie, enzovoort.

**Phi-3-mini**

Het 3,8 miljard parameters tellende taalmodel is beschikbaar op Microsoft Foundry, Hugging Face en Ollama. Phi-3 modellen presteren significant beter dan taalmodellen van gelijke en grotere omvang op belangrijke benchmarks (zie benchmarkcijfers hieronder, hogere cijfers zijn beter). Phi-3-mini presteert beter dan modellen met twee keer zoveel parameters, terwijl Phi-3-small en Phi-3-medium grotere modellen, inclusief GPT-3.5, overtreffen.

**Phi-3-small & medium**

Met slechts 7 miljard parameters verslaat Phi-3-small GPT-3.5T op verschillende benchmarks voor taal, redeneren, coderen en wiskunde.

De Phi-3-medium met 14 miljard parameters zet deze lijn voort en presteert beter dan Gemini 1.0 Pro.

**Phi-3.5-mini**

We kunnen dit zien als een upgrade van Phi-3-mini. Hoewel het aantal parameters ongewijzigd blijft, verbetert het de ondersteuning voor meerdere talen (ondersteunt 20+ talen: Arabisch, Chinees, Tsjechisch, Deens, Nederlands, Engels, Fins, Frans, Duits, Hebreeuws, Hongaars, Italiaans, Japans, Koreaans, Noors, Pools, Portugees, Russisch, Spaans, Zweeds, Thai, Turks, Oekraïens) en voegt het sterkere ondersteuning voor lange context toe.

Phi-3.5-mini met 3,8 miljard parameters overtreft taalmodellen van dezelfde grootte en staat op gelijke voet met modellen die twee keer zo groot zijn.

### Phi-3 / 3.5 Vision

We kunnen het Instruct-model van Phi-3/3.5 zien als Phi's vermogen om te begrijpen, en Vision is wat Phi ogen geeft om de wereld te begrijpen.


**Phi-3-Vision**

Phi-3-vision, met slechts 4,2 miljard parameters, zet deze trend voort en presteert beter dan grotere modellen zoals Claude-3 Haiku en Gemini 1.0 Pro V op algemene visuele redeneertaken, OCR en het begrijpen van tabellen en diagrammen.


**Phi-3.5-Vision**

Phi-3.5-Vision is ook een upgrade van Phi-3-Vision, met toevoeging van ondersteuning voor meerdere afbeeldingen. Je kunt het zien als een verbetering in visie, waarbij je niet alleen plaatjes kunt zien, maar ook video's.

Phi-3.5-vision presteert beter dan grotere modellen zoals Claude-3.5 Sonnet en Gemini 1.5 Flash bij OCR, het begrijpen van tabellen en grafieken en is gelijkwaardig op algemene visuele kennis- en redeneertaken. Ondersteunt multi-frame input, d.w.z. redeneert over meerdere invoerafbeeldingen.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** maakt het mogelijk modellen te pretrainen met veel minder rekenkracht, wat betekent dat je het model- of datasetformaat dramatisch kunt opschalen met hetzelfde computercapaciteitsbudget als een dicht model. Met name zou een MoE-model tijdens pretraining dezelfde kwaliteit als zijn dichte tegenhanger veel sneller moeten bereiken.

Phi-3.5-MoE bestaat uit 16x3,8 miljard expertmodules. Phi-3.5-MoE met slechts 6,6 miljard actieve parameters behaalt een vergelijkbaar niveau van redeneren, taalbegrip en wiskunde als veel grotere modellen.

We kunnen het Phi-3/3.5 Familie model gebruiken op basis van verschillende scenario's. In tegenstelling tot GTM kun je Phi-3/3.5-mini of Phi-3/3.5-Vision op edge-apparaten implementeren.


## Hoe Gebruik je Phi-3/3.5 Familie modellen

We hopen Phi-3/3.5 in verschillende scenario's te gebruiken. Vervolgens zullen we Phi-3/3.5 gebruiken gebaseerd op verschillende scenario's.

![phi3](../../../translated_images/nl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferentie via Cloud-API's

**Microsoft Foundry Modellen**

> **Opmerking:** GitHub Models wordt aan het eind van juli 2026 uitgefaseerd. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) is de directe vervanger.

> **Opmerking:** De gehele Phi-3/3.5 familie (Instruct, Vision en MoE varianten) is uit het Microsoft Foundry Models catalogus gehaald op 2025-08-30. Gebruik daar in plaats daarvan `Phi-4` (Instruct) of `Phi-4-mini-instruct` — de hieronder genoemde Phi-3/3.5 voorbeelden werken nog via Hugging Face, Ollama, ONNX Runtime en NVIDIA NIM.

Microsoft Foundry Models biedt nu de Phi-4 opvolgers aan. Gebruik `Phi-4` of `Phi-4-mini-instruct` in plaats van de uitgefaseerde Phi-3/3.5 modellen wanneer je de voorbeelden met cloud-API volgt.

- Demo: Vergelijking van de effecten van Phi-3-mini en Phi-3.5-mini in Chinese scenario's

![phi3](../../../translated_images/nl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/nl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Als je visiemodellen (multimodaal) in de cloud wilt gebruiken, gebruik dan de momenteel beschikbare `Phi-4-multimodal-instruct` via Microsoft Foundry in plaats van de uitgefaseerde Phi-3/3.5 Vision modellen; voor taaktaken gebruik `Phi-4` of `Phi-4-mini-instruct`. Het Phi-3.5 MoE model is uit Microsoft Foundry gehaald, dus gebruik de andere opties die in deze les worden beschreven (bijvoorbeeld Hugging Face) als je ermee wilt experimenteren. Als je geïnteresseerd bent, kun je de Phi Cookbook lezen om te leren hoe je Phi-modellen aanroept via Microsoft Foundry [Klik op deze link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Naast de cloud-gebaseerde Microsoft Foundry Models catalogus kun je ook [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) gebruiken om gerelateerde oproepen te voltooien. Je kunt NVIDIA NIM bezoeken om de API-aanroepen van de Phi-3/3.5 Familie te voltooien. NVIDIA NIM (NVIDIA Inference Microservices) is een set van versnelde inferentie microservices ontworpen om ontwikkelaars te helpen AI-modellen efficiënt te implementeren in diverse omgevingen, waaronder clouds, datacenters en werkstations.

Hier zijn enkele belangrijke kenmerken van NVIDIA NIM:

- **Gemakkelijk inzetten:** NIM maakt het mogelijk om AI-modellen met één commando in te zetten, waardoor het eenvoudig te integreren is in bestaande workflows.
- **Geoptimaliseerde prestaties:** Het maakt gebruik van NVIDIA’s voorgeoptimaliseerde inference-engines, zoals TensorRT en TensorRT-LLM, om lage latentie en hoge doorvoer te garanderen.
- **Schaalbaarheid:** NIM ondersteunt autoscaling op Kubernetes, waardoor het effectief met wisselende werklasten kan omgaan.
- **Veiligheid en controle:** Organisaties kunnen controle houden over hun data en applicaties door NIM-microservices zelf te hosten op hun eigen beheerde infrastructuur.
- **Standaard API’s:** NIM biedt industriestandaard API’s, waardoor het eenvoudig is AI-toepassingen zoals chatbots, AI-assistenten en meer te bouwen en te integreren.

NIM maakt deel uit van NVIDIA AI Enterprise, dat erop gericht is het inzetten en operationeel maken van AI-modellen te vereenvoudigen, zodat deze efficiënt op NVIDIA GPU’s draaien.

- Demo: Gebruik van NVIDIA NIM om Phi-3.5-Vision-API aan te roepen [[Klik op deze link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaal draaien
Inference met betrekking tot Phi-3, of elk taalmodel zoals GPT-3, verwijst naar het proces van het genereren van antwoorden of voorspellingen op basis van de input die het ontvangt. Wanneer je een prompt of vraag aan Phi-3 geeft, gebruikt het zijn getrainde neuraal netwerk om het meest waarschijnlijke en relevante antwoord af te leiden door patronen en relaties in de data waarop het is getraind te analyseren.

**Hugging Face Transformer**
Hugging Face Transformers is een krachtige bibliotheek, ontworpen voor natuurlijke taalverwerking (NLP) en andere machine learning taken. Hier enkele belangrijke punten:

1. **Voorgetrainde Modellen**: Het biedt duizenden voorgetrainde modellen die gebruikt kunnen worden voor diverse taken zoals tekstclassificatie, named entity recognition, vraagbeantwoording, samenvattingen, vertaling en tekstgeneratie.

2. **Framework Interoperabiliteit**: De bibliotheek ondersteunt meerdere deep learning frameworks, waaronder PyTorch, TensorFlow, en JAX. Dit maakt het mogelijk een model in het ene framework te trainen en in een ander te gebruiken.

3. **Multimodale mogelijkheden**: Naast NLP ondersteunt Hugging Face Transformers ook taken in computer vision (bijv. beeldclassificatie, objectdetectie) en audioprocessing (bijv. spraakherkenning, audioclassificatie).

4. **Gebruiksgemak**: De bibliotheek biedt API’s en tools om modellen eenvoudig te downloaden en fijn af te stemmen, wat het toegankelijk maakt voor zowel beginners als experts.

5. **Community en bronnen**: Hugging Face heeft een levendige community en uitgebreide documentatie, tutorials en handleidingen om gebruikers op weg te helpen en het meeste uit de bibliotheek te halen.
[officiële documentatie](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) of hun [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dit is de meest gebruikte methode, maar het vereist ook GPU-versnelling. Scenario’s zoals Vision en MoE vergen immers veel berekeningen, wat op CPU erg traag zal zijn als ze niet gequantiseerd zijn.


- Demo: Gebruik van Transformer om Phi-3.5-Instruct aan te roepen [Klik op deze link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-Vision aan te roepen [Klik op deze link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Gebruik van Transformer om Phi-3.5-MoE aan te roepen [Klik op deze link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) is een platform dat het gemakkelijker maakt grote taalmodellen (LLM’s) lokaal op je machine te draaien. Het ondersteunt diverse modellen zoals Llama 3.1, Phi 3, Mistral en Gemma 2, onder andere. Het platform vereenvoudigt het proces door gewichten van modellen, configuratie en data in één pakket te bundelen, waardoor het toegankelijker wordt voor gebruikers om zelf modellen aan te passen en te maken. Ollama is beschikbaar voor macOS, Linux en Windows. Het is een uitstekend hulpmiddel als je wilt experimenteren met of LLM’s deployen zonder afhankelijk te zijn van clouddiensten. Ollama is de meest directe manier, je hoeft alleen het volgende commando uit te voeren.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) is Microsoft’s offline runtime op het apparaat zelf om modellen zoals Phi volledig op je eigen hardware te draaien - zonder Azure-abonnement, API-sleutel of netwerkverbinding. Het kiest automatisch de beste beschikbare uitvoeringprovider (NPU, GPU, of CPU) en biedt een OpenAI-compatibele endpoint, zodat bestaande `openai`/Azure AI Inference SDK code er met minimale aanpassingen gebruik van kan maken. Zie de [Foundry Local documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om te beginnen.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) is een platformonafhankelijke versneller voor het uitvoeren en trainen van machine learning. ONNX Runtime voor Generative AI (GENAI) is een krachtig hulpmiddel dat je helpt generatieve AI-modellen efficiënt uit te voeren op verschillende platforms.

## Wat is ONNX Runtime?
ONNX Runtime is een open source project dat high-performance inference van machine learning modellen mogelijk maakt. Het ondersteunt modellen in het Open Neural Network Exchange (ONNX) formaat, een standaard voor het representeren van machine learning modellen. ONNX Runtime inference kan snellere gebruikerservaringen en lagere kosten mogelijk maken, door modellen te ondersteunen van deep learning frameworks zoals PyTorch en TensorFlow/Keras, evenals klassieke machine learning bibliotheken zoals scikit-learn, LightGBM, XGBoost, enz. ONNX Runtime is compatibel met verschillende hardware, drivers en besturingssystemen, en levert optimale prestaties door indien mogelijk hardwareversnellers te benutten naast grafoptimalisaties en transformaties.

## Wat is Generatieve AI?
Generatieve AI verwijst naar AI systemen die nieuwe content kunnen genereren, zoals tekst, afbeeldingen of muziek, gebaseerd op de data waarop ze getraind zijn. Voorbeelden zijn taalmodellen zoals GPT-3 en beeldgeneratiemodellen zoals Stable Diffusion. De ONNX Runtime voor GenAI bibliotheek biedt de generatieve AI-lus voor ONNX modellen, inclusief inference met ONNX Runtime, logitsverwerking, zoeken en sampling, en KV-cachebeheer.

## ONNX Runtime voor GENAI
ONNX Runtime voor GENAI breidt de mogelijkheden van ONNX Runtime uit om generatieve AI-modellen te ondersteunen. Hier enkele belangrijke kenmerken:

- **Breed platformondersteuning:** Het werkt op diverse platforms, waaronder Windows, Linux, macOS, Android en iOS.
- **Modelondersteuning:** Het ondersteunt vele populaire generatieve AI-modellen, zoals LLaMA, GPT-Neo, BLOOM en meer.
- **Prestatieoptimalisatie:** Het bevat optimalisaties voor diverse hardwareversnellers zoals NVIDIA GPU’s, AMD GPU’s, en meer2.
- **Gebruiksgemak:** Het biedt API’s voor eenvoudige integratie in applicaties, waardoor je met minimale code tekst, afbeeldingen en andere content kunt genereren.
- Gebruikers kunnen een hoge-niveau generate()-methode aanroepen, of elke iteratie van het model in een lus draaien, waarbij telkens één token wordt gegenereerd, en optioneel generatieparameters binnen de lus worden aangepast.
- ONNX runtime ondersteunt ook greedy/beam search en TopP, TopK sampling om tokenreeksen te genereren en ingebouwde logitsverwerking zoals herhalingsstraffen. Je kunt ook eenvoudig aangepaste scoring toevoegen.

## Aan de slag
Om aan de slag te gaan met ONNX Runtime voor GENAI, kun je de volgende stappen volgen:

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
### Demo: Gebruik ONNX Runtime GenAI om Phi-3.5-Vision aan te roepen


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

Naast ONNX Runtime, Ollama en Foundry Local referentiemethoden, kunnen we ook de referentie van kwantitatieve modellen aanvullen op basis van de modelreferentiemethoden die door verschillende fabrikanten worden aangeboden. Zoals het Apple MLX-framework met Apple Metal, Qualcomm QNN met NPU, Intel OpenVINO met CPU/GPU, enz. Je kunt ook meer inhoud vinden in de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Meer

We hebben de basis geleerd van de Phi-3/3.5 familie, maar om meer over SLM te leren hebben we meer kennis nodig. Je kunt de antwoorden vinden in de Phi-3 Cookbook. Als je meer wilt leren, bezoek dan de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->