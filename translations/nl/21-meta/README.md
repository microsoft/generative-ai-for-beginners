# Bouwen met de Meta Familie Modellen 

## Introductie 

Deze les behandelt: 

- Verkenning van de twee belangrijkste Meta familiewerkmodellen - Llama 3.1 en Llama 3.2, plus de momenteel beschikbare alternatieven die in de codevoorbeelden worden gebruikt (Llama 3.3 en Llama 4) 
- Begrip van de gebruikssituaties en scenario’s voor elk model 
- Codevoorbeeld om de unieke kenmerken van elk model te tonen 


## De Meta Familie van Modellen 

In deze les verkennen we 2 modellen uit de Meta familie of "Llama Kudde" - Llama 3.1 en Llama 3.2. De uitvoerbare codevoorbeelden gebruiken Llama 3.3 en Llama 4, die momenteel beschikbare alternatieven zijn in de Microsoft Foundry Models catalogus.

Deze modellen zijn er in verschillende varianten en zijn beschikbaar in de [Microsoft Foundry Models catalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Opmerking:** GitHub Modellen wordt uitgefaseerd eind juli 2026. Hier vind je meer details over het gebruik van [Microsoft Foundry Modellen](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) om met AI-modellen te prototypen.

> **Opmerking:** De specifieke modelversies waartegen deze les oorspronkelijk was geschreven (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) zijn sindsdien uit de Microsoft Foundry Models catalogus verwijderd. De codevoorbeelden hieronder gebruiken `Llama-3.3-70B-Instruct` en `Llama-4-Scout-17B-16E-Instruct` als momenteel beschikbare alternatieven in de Microsoft Foundry Models catalogus, dus ze werken vandaag nog steeds.

Modelvarianten (zoals oorspronkelijk in deze les behandeld): 
- Llama 3.1 - 70B Instruct (uitgefaseerd) 
- Llama 3.1 - 405B Instruct (uitgefaseerd) 
- Llama 3.2 - 11B Vision Instruct (uitgefaseerd) 
- Llama 3.2 - 90B Vision Instruct (uitgefaseerd) 

Momenteel beschikbare alternatieven die in de codevoorbeelden worden gebruikt: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Opmerking: De hierboven besproken Llama 3-varianten worden bewaard voor historische context en zijn niet langer beschikbaar in Microsoft Foundry Models.*

## Llama 3.1 

Met 405 miljard parameters valt Llama 3.1 in de categorie open source LLM. 

Het model is een upgrade ten opzichte van de eerdere release Llama 3 door te bieden: 

- Groter contextvenster - 128k tokens versus 8k tokens 
- Groter Max Output Tokens - 4096 versus 2048 
- Betere meertalige ondersteuning - dankzij de toename van trainings-tokens 

Hierdoor kan Llama 3.1 complexere gebruikssituaties aan bij het bouwen van GenAI-toepassingen, waaronder: 
- Native Function Calling - de mogelijkheid om externe tools en functies buiten de LLM workflow aan te roepen
- Betere RAG-prestaties - vanwege het grotere contextvenster 
- Synthese van gegevensgeneratie - de mogelijkheid om effectieve data te creëren voor taken zoals fine-tuning 

### Native Function Calling 

Llama 3.1 is verfijnd om effectiever te zijn bij het maken van functie- of toolaanroepen. Het heeft ook twee ingebouwde tools die het model kan herkennen als nodig om te gebruiken op basis van de prompt van de gebruiker. Deze tools zijn:

- **Brave Search** - Kan worden gebruikt om up-to-date informatie zoals het weer te krijgen door een webzoekopdracht uit te voeren
- **Wolfram Alpha** - Kan worden gebruikt voor complexere wiskundige berekeningen zodat het schrijven van je eigen functies niet nodig is.

Je kunt ook je eigen aangepaste tools maken die het LLM kan aanroepen.

In het onderstaande codevoorbeeld:

- Definiëren we de beschikbare tools (brave_search, wolfram_alpha) in de systeem prompt.
- Sturen we een gebruikersprompt die vraagt naar het weer in een bepaalde stad.
- Zal het LLM reageren met een toolaanroep naar de Brave Search tool die er zo uit zal zien `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opmerking: Dit voorbeeld maakt alleen de toolaanroep, als je de resultaten wilt ontvangen, moet je een gratis account aanmaken op de Brave API-pagina en de functie zelf definiëren.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Ondanks dat het een LLM is, is een beperking van Llama 3.1 het gebrek aan multimodaliteit. Dat wil zeggen, het onvermogen om verschillende soorten input zoals afbeeldingen als prompts te gebruiken en daar reacties op te geven. Deze mogelijkheid is een van de belangrijkste kenmerken van Llama 3.2. Deze functies omvatten ook:

- Multimodaliteit - kan zowel tekst- als afbeeldingsprompts evalueren
- Kleine tot middelgrote varianten (11B en 90B) - dit biedt flexibele implementatieopties,
- Alleen-tekst varianten (1B en 3B) - dit maakt het mogelijk het model te implementeren op edge/mobiele apparaten en biedt lage latentie

De multimodale ondersteuning vertegenwoordigt een grote stap in de wereld van open-source modellen. Het volgende codevoorbeeld neemt zowel een afbeelding als een tekstprompt om een analyse van de afbeelding te krijgen. Omdat Llama 3.2 90B Vision Instruct met pensioen is gegaan, gebruikt het voorbeeld `Llama-4-Scout-17B-16E-Instruct`, een momenteel beschikbare native multimodale alternatief.


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Het leren stopt hier niet, ga verder met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je Generative AI kennis verder te vergroten!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->