<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:13:17+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "nl"
}
-->
# Bouwen met de Meta Familie Modellen

## Inleiding

Deze les behandelt:

- Het verkennen van de twee belangrijkste Meta familie modellen - Llama 3.1 en Llama 3.2
- Het begrijpen van de gebruiksscenario's voor elk model
- Een codevoorbeeld om de unieke kenmerken van elk model te laten zien

## De Meta Familie van Modellen

In deze les verkennen we 2 modellen uit de Meta familie of "Llama Kudde" - Llama 3.1 en Llama 3.2

Deze modellen komen in verschillende varianten en zijn beschikbaar op de GitHub Model marktplaats. Hier zijn meer details over het gebruik van GitHub Modellen om te [prototypen met AI-modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelvarianten:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Opmerking: Llama 3 is ook beschikbaar op GitHub Modellen maar zal niet in deze les worden behandeld*

## Llama 3.1

Met 405 miljard parameters valt Llama 3.1 in de open source LLM categorie.

De modus is een upgrade van de eerdere release Llama 3 door het bieden van:

- Groter contextvenster - 128k tokens vs 8k tokens
- Grotere Max Output Tokens - 4096 vs 2048
- Betere meertalige ondersteuning - door toename in training tokens

Dit stelt Llama 3.1 in staat om complexere gebruiksscenario's aan te pakken bij het bouwen van GenAI-toepassingen, waaronder:
- Native Function Calling - de mogelijkheid om externe tools en functies buiten de LLM workflow aan te roepen
- Betere RAG-prestaties - dankzij het grotere contextvenster
- Synthese van gegevens - de mogelijkheid om effectieve gegevens te creëren voor taken zoals fine-tuning

### Native Function Calling

Llama 3.1 is verfijnd om effectiever te zijn in het maken van functie- of tooloproepen. Het heeft ook twee ingebouwde tools die het model kan identificeren als nodig om te worden gebruikt op basis van de prompt van de gebruiker. Deze tools zijn:

- **Brave Search** - Kan worden gebruikt om actuele informatie zoals het weer te verkrijgen door een webzoekopdracht uit te voeren
- **Wolfram Alpha** - Kan worden gebruikt voor complexere wiskundige berekeningen, zodat het schrijven van je eigen functies niet nodig is.

Je kunt ook je eigen aangepaste tools maken die LLM kan aanroepen.

In het codevoorbeeld hieronder:

- We definiëren de beschikbare tools (brave_search, wolfram_alpha) in de systeemprompt.
- Stuur een gebruikersprompt die vraagt naar het weer in een bepaalde stad.
- De LLM zal reageren met een tooloproep naar de Brave Search tool die er als volgt uitziet `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opmerking: Dit voorbeeld maakt alleen de tooloproep, als je de resultaten wilt krijgen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren*

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

Ondanks dat het een LLM is, heeft Llama 3.1 een beperking op het gebied van multimodaliteit. Dat wil zeggen, het kunnen gebruiken van verschillende soorten invoer zoals afbeeldingen als prompts en het geven van antwoorden. Deze mogelijkheid is een van de belangrijkste kenmerken van Llama 3.2. Deze kenmerken omvatten ook:

- Multimodaliteit - heeft de mogelijkheid om zowel tekst- als afbeeldingsprompts te evalueren
- Kleine tot middelgrote variaties (11B en 90B) - dit biedt flexibele implementatie-opties,
- Alleen tekstvariaties (1B en 3B) - dit stelt het model in staat om op rand- / mobiele apparaten te worden ingezet en biedt lage latentie

De multimodale ondersteuning vertegenwoordigt een grote stap in de wereld van open source modellen. Het codevoorbeeld hieronder neemt zowel een afbeelding als een tekstprompt om een analyse van de afbeelding te krijgen van Llama 3.2 90B.

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

## Het leren stopt hier niet, vervolg de Reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generatieve AI verder uit te breiden!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.