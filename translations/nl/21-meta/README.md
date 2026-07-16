# Bouwen met de Meta Familie Modellen 

## Introductie 

Deze les behandelt: 

- Het verkennen van de twee belangrijkste Meta familiemodellen - Llama 3.1 en Llama 3.2 
- Begrijpen van de gebruiksscenario's voor elk model 
- Voorbeeldcode om de unieke kenmerken van elk model te tonen 


## De Meta Familie van Modellen 

In deze les verkennen we 2 modellen uit de Meta familie of "Llama Herd" - Llama 3.1 en Llama 3.2.

Deze modellen zijn er in verschillende varianten en zijn beschikbaar in de [Microsoft Foundry Models catalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Notitie:** GitHub Models wordt uitgefaseerd eind juli 2026. Hier zijn meer details over het gebruik van [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) om te prototypen met AI-modellen.

Modelvarianten: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Opmerking: Llama 3 is ook beschikbaar in Microsoft Foundry Models maar zal niet behandeld worden in deze les*

## Llama 3.1 

Met 405 miljard parameters valt Llama 3.1 in de categorie open source LLM. 

Het model is een upgrade ten opzichte van de eerdere release Llama 3 door te bieden: 

- Groter contextvenster - 128k tokens versus 8k tokens 
- Groter max aantal output tokens - 4096 versus 2048 
- Betere meertalige ondersteuning - dankzij toename in training tokens 

Deze maken het mogelijk voor Llama 3.1 om meer complexe use cases aan te pakken bij het bouwen van GenAI-toepassingen, waaronder: 
- Native Function Calling - de mogelijkheid om externe tools en functies buiten de LLM-workflow aan te roepen
- Betere RAG-prestaties - dankzij het grotere contextvenster 
- Synthese van data - de mogelijkheid om effectieve data te creëren voor taken zoals fine-tuning 

### Native Function Calling 

Llama 3.1 is fijn afgestemd om effectiever te zijn in het maken van functie- of toolaanroepen. Het heeft ook twee ingebouwde tools die het model kan identificeren als nodig om te gebruiken op basis van de prompt van de gebruiker. Deze tools zijn: 

- **Brave Search** - Kan worden gebruikt om up-to-date informatie te verkrijgen zoals het weer door een webzoekopdracht uit te voeren 
- **Wolfram Alpha** - Kan worden gebruikt voor complexere wiskundige berekeningen zodat je geen eigen functies hoeft te schrijven. 

Je kunt ook je eigen aangepaste tools maken die de LLM kan aanroepen. 

In het onderstaande codevoorbeeld: 

- Definiëren we de beschikbare tools (brave_search, wolfram_alpha) in de systeem prompt. 
- Versturen we een gebruikersprompt die vraagt naar het weer in een bepaalde stad. 
- Zal de LLM reageren met een toolaanroep naar de Brave Search-tool die er zo uit zal zien `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Opmerking: Dit voorbeeld maakt alleen de toolaanroep, als je de resultaten wilt krijgen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Verkrijg deze van de "Overzicht" pagina van je Microsoft Foundry-project
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

Ondanks dat het een LLM is, is een beperking van Llama 3.1 het ontbreken van multimodaliteit. Dat wil zeggen, het onvermogen om verschillende soorten input te gebruiken zoals afbeeldingen als prompts en daarop te antwoorden. Deze mogelijkheid is een van de belangrijkste kenmerken van Llama 3.2. Deze kenmerken omvatten ook: 

- Multimodaliteit - heeft de mogelijkheid om zowel tekst- als afbeeldingsprompts te evalueren 
- Kleine tot middelgrote varianten (11B en 90B) - dit biedt flexibele inzetopties, 
- Alleen-tekst varianten (1B en 3B) - hiermee kan het model op edge / mobiele apparaten worden ingezet en biedt het lage latency 

De multimodale ondersteuning vertegenwoordigt een grote stap in de wereld van open source modellen. Het onderstaande codevoorbeeld neemt zowel een afbeelding als tekstprompt om een analyse van de afbeelding te krijgen van Llama 3.2 90B. 


### Multimodale Ondersteuning met Llama 3.2

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

## Leren stopt hier niet, ga verder op de reis

Na het voltooien van deze les, bekijk onze [Generatieve AI Leercollectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder te vergroten!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->