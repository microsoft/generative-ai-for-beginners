# Bouwen met de Meta Familietmodellen 

## Introductie 

Deze les behandelt: 

- Verkenning van de twee belangrijkste Meta familietmodellen - Llama 3.1 en Llama 3.2 
- Begrip van de gebruikssituaties en scenario's voor elk model 
- Voorbeeldcode om de unieke kenmerken van elk model te laten zien 


## De Meta Familie van Modellen 

In deze les verkennen we 2 modellen uit de Meta familie of "Llama Herd" - Llama 3.1 en Llama 3.2.

Deze modellen zijn beschikbaar in verschillende varianten en zijn beschikbaar in de [Microsoft Foundry Models catalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Opmerking:** GitHub Models wordt beëindigd eind juli 2026. Hier vindt u meer details over het gebruik van [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) om prototypes te maken met AI-modellen.

Modelvarianten: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Opmerking: Llama 3 is ook beschikbaar in Microsoft Foundry Models maar wordt niet behandeld in deze les*

## Llama 3.1 

Met 405 miljard parameters valt Llama 3.1 in de categorie open source LLM. 

Het model is een upgrade van de eerdere release Llama 3 door te bieden: 

- Groter contextvenster - 128k tokens vs 8k tokens 
- Grotere maximale output tokens - 4096 vs 2048 
- Betere meertalige ondersteuning - dankzij een toename in trainings-tokens 

Deze maken Llama 3.1 in staat om complexere gebruikssituaties aan te kunnen bij het bouwen van GenAI-toepassingen, waaronder: 
- Native Function Calling - het vermogen om externe tools en functies buiten de LLM-workflow aan te roepen
- Betere RAG-prestaties - dankzij het grotere contextvenster 
- Synthese van gegevens - het vermogen om effectieve data te creëren voor taken zoals fijn-tuning 

### Native Function Calling 

Llama 3.1 is fijn afgestemd om effectiever te zijn in het uitvoeren van functie- of tool-aanroepen. Het heeft ook twee ingebouwde tools die het model kan herkennen als nodig op basis van de prompt van de gebruiker. Deze tools zijn: 

- **Brave Search** - kan worden gebruikt om up-to-date informatie te krijgen zoals het weer door een websearch uit te voeren 
- **Wolfram Alpha** - kan worden gebruikt voor complexere wiskundige berekeningen, zodat je geen eigen functies hoeft te schrijven. 

Je kunt ook je eigen aangepaste tools maken die door de LLM kunnen worden aangeroepen. 

In het onderstaande codevoorbeeld: 

- Definiëren we de beschikbare tools (brave_search, wolfram_alpha) in de systeem-prompt. 
- Sturen we een gebruikersprompt die vraagt naar het weer in een bepaalde stad. 
- Zal de LLM reageren met een tool-aanroep naar de Brave Search tool die er zo uitziet `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Opmerking: Dit voorbeeld voert alleen de tool-aanroep uit, als je de resultaten wilt krijgen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Haal deze op van de "Overzicht" pagina van je Microsoft Foundry-project
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

Ondanks dat het een LLM is, is een beperking van Llama 3.1 het gebrek aan multimodaliteit. Dat wil zeggen, het onvermogen om verschillende soorten invoer zoals afbeeldingen als prompts te gebruiken en hierop te reageren. Dit vermogen is één van de belangrijkste kenmerken van Llama 3.2. Deze kenmerken omvatten ook: 

- Multimodaliteit - het vermogen om zowel tekst- als afbeeldingsprompts te evalueren 
- Kleine tot middelgrote variaties (11B en 90B) - dit biedt flexibele implementatie-opties, 
- Alleen tekst variaties (1B en 3B) - dit stelt het model in staat om op edge / mobiele apparaten te worden ingezet en biedt lage latentie 

De multimodale ondersteuning vertegenwoordigt een grote stap in de wereld van open source modellen. Het onderstaande codevoorbeeld neemt zowel een afbeelding als tekstprompt om een analyse van de afbeelding te krijgen van Llama 3.2 90B. 


### Multimodale ondersteuning met Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Haal deze op van de "Overzicht"-pagina van je Microsoft Foundry-project
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Leren stopt hier niet, ga door met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je Generative AI kennis verder te verhogen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->