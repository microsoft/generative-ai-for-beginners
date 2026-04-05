# Bouwen met de Meta Family modellen

## Introductie

Deze les behandelt:

- Verkenning van de twee belangrijkste Meta Family modellen - Llama 3.1 en Llama 3.2
- Begrijpen van de toepassingsgevallen en scenario's voor elk model
- Codevoorbeeld om de unieke functies van elk model te tonen

## De Meta Family van Modellen

In deze les verkennen we 2 modellen uit de Meta Family of "Llama Herd" - Llama 3.1 en Llama 3.2.

Deze modellen zijn verkrijgbaar in verschillende varianten en beschikbaar op de GitHub Model-marktplaats. Hier vindt u meer details over het gebruik van GitHub Models om te [prototypen met AI-modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelvarianten:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Opmerking: Llama 3 is ook beschikbaar op GitHub Models, maar wordt niet behandeld in deze les*

## Llama 3.1

Met 405 miljard parameters valt Llama 3.1 in de categorie open source LLM.

Het model is een upgrade ten opzichte van de eerdere release Llama 3 door het bieden van:

- Groter contextvenster - 128k tokens vs 8k tokens
- Groter maximaal aantal output tokens - 4096 vs 2048
- Betere meertalige ondersteuning - dankzij toename in trainingsdata

Deze mogelijkheden maken Llama 3.1 geschikt voor complexere gebruiksscenario’s bij het bouwen van GenAI-toepassingen, waaronder:
- Native Function Calling - de mogelijkheid om externe tools en functies buiten de LLM-werkstroom aan te roepen
- Betere RAG-prestaties - dankzij het hogere contextvenster
- Genereren van synthetische data - de mogelijkheid om effectieve data te creëren voor taken zoals fine-tuning

### Native Function Calling

Llama 3.1 is fijn afgestemd om effectiever te zijn in het maken van functie- of tool-aanroepen. Het heeft ook twee ingebouwde tools die het model kan herkennen als nodig op basis van de prompt van de gebruiker. Deze tools zijn:

- **Brave Search** - kan worden gebruikt om up-to-date informatie te verkrijgen, zoals het weer door een webzoekopdracht uit te voeren
- **Wolfram Alpha** - kan worden gebruikt voor complexere wiskundige berekeningen zodat het schrijven van eigen functies niet nodig is

Je kunt ook je eigen aangepaste tools maken die het LLM kan aanroepen.

In het onderstaande codevoorbeeld:

- Definiëren we de beschikbare tools (brave_search, wolfram_alpha) in de system prompt.
- Versturen we een gebruikersprompt die vraagt naar het weer in een bepaalde stad.
- Zal het LLM reageren met een tool-aanroep naar de Brave Search tool die er zo uitziet `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opmerking: Dit voorbeeld maakt alleen de tool-aanroep; als je de resultaten wilt ontvangen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren.

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

Ondanks dat het een LLM is, is een beperking van Llama 3.1 het gebrek aan multimodaliteit. Dat wil zeggen, de onmogelijkheid om verschillende soorten invoer zoals afbeeldingen als prompts te gebruiken en daarop te reageren. Deze mogelijkheid is een van de belangrijkste kenmerken van Llama 3.2. Deze functies omvatten ook:

- Multimodaliteit - kan zowel tekst- als afbeeldingsprompts beoordelen
- Kleinere tot middelgrote varianten (11B en 90B) - dit biedt flexibele implementatie-opties,
- Alleen tekst varianten (1B en 3B) - dit maakt het mogelijk het model op edge/mobiele apparaten in te zetten en zorgt voor lage latency

De ondersteuning voor multimodaliteit is een grote stap in de wereld van open source modellen. Het onderstaande codevoorbeeld neemt zowel een afbeelding als een tekstprompt om een analyse van de afbeelding te krijgen van Llama 3.2 90B.

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

## Leren stopt hier niet, ga door met je reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning-collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generative AI verder te vergroten!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortkomen uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->