<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:11:17+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "nl"
}
-->
# Bouwen met de Meta Family Modellen

## Introductie

Deze les behandelt:

- Verkenning van de twee belangrijkste Meta family modellen - Llama 3.1 en Llama 3.2  
- Inzicht in de gebruikssituaties en scenario’s voor elk model  
- Codevoorbeeld om de unieke kenmerken van elk model te laten zien  

## De Meta Family van Modellen

In deze les verkennen we 2 modellen uit de Meta family of "Llama Herd" - Llama 3.1 en Llama 3.2

Deze modellen zijn beschikbaar in verschillende varianten en te vinden op de GitHub Model marketplace. Hier vind je meer informatie over het gebruik van GitHub Models om te [prototypen met AI-modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelvarianten:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Opmerking: Llama 3 is ook beschikbaar op GitHub Models, maar wordt niet behandeld in deze les*

## Llama 3.1

Met 405 miljard parameters valt Llama 3.1 in de categorie open source LLM.

Dit model is een upgrade van de eerdere release Llama 3 en biedt:

- Groter contextvenster - 128k tokens versus 8k tokens  
- Groter maximaal aantal output tokens - 4096 versus 2048  
- Betere meertalige ondersteuning - dankzij een toename in trainingsdata  

Hierdoor kan Llama 3.1 complexere use-cases aan bij het bouwen van GenAI-toepassingen, waaronder:  
- Native Function Calling - de mogelijkheid om externe tools en functies buiten de LLM workflow aan te roepen  
- Betere RAG-prestaties - dankzij het grotere contextvenster  
- Genereren van synthetische data - de mogelijkheid om effectieve data te creëren voor taken zoals fine-tuning  

### Native Function Calling

Llama 3.1 is fijn afgestemd om effectiever te zijn in het aanroepen van functies of tools. Het heeft ook twee ingebouwde tools die het model kan herkennen en gebruiken op basis van de prompt van de gebruiker. Deze tools zijn:

- **Brave Search** - Kan gebruikt worden om actuele informatie op te zoeken, zoals het weer, door een webzoekopdracht uit te voeren  
- **Wolfram Alpha** - Kan gebruikt worden voor complexere wiskundige berekeningen, zodat je geen eigen functies hoeft te schrijven  

Je kunt ook je eigen aangepaste tools maken die het LLM kan aanroepen.

In het onderstaande codevoorbeeld:

- Definiëren we de beschikbare tools (brave_search, wolfram_alpha) in de system prompt.  
- Sturen we een gebruikersprompt die vraagt naar het weer in een bepaalde stad.  
- Zal het LLM reageren met een tool-aanroep naar de Brave Search tool, die er zo uit zal zien: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opmerking: dit voorbeeld maakt alleen de tool-aanroep; als je de resultaten wilt ontvangen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

Hoewel Llama 3.1 een LLM is, heeft het een beperking op het gebied van multimodaliteit. Dat wil zeggen, het kunnen gebruiken van verschillende soorten input zoals afbeeldingen als prompts en daarop reageren. Deze mogelijkheid is een van de belangrijkste kenmerken van Llama 3.2. Andere kenmerken zijn:

- Multimodaliteit - kan zowel tekst- als afbeeldingsprompts verwerken  
- Kleine tot middelgrote varianten (11B en 90B) - bieden flexibele implementatieopties  
- Alleen-tekst varianten (1B en 3B) - maken het mogelijk het model op edge- of mobiele apparaten te draaien met lage latency  

De multimodale ondersteuning is een grote stap voorwaarts in de wereld van open source modellen. Het onderstaande codevoorbeeld gebruikt zowel een afbeelding als een tekstprompt om een analyse van de afbeelding te krijgen van Llama 3.2 90B.

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te verdiepen!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.