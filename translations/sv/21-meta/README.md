# Bygga med Meta Family-modellerna 

## Introduktion 

Denna lektion kommer att täcka: 

- Utforska de två huvudmodellerna i Meta-familjen - Llama 3.1 och Llama 3.2 
- Förstå användningsområden och scenarier för varje modell 
- Kodexempel som visar varje modells unika funktioner 


## Meta Family av modeller 

I denna lektion kommer vi att utforska 2 modeller från Meta-familjen eller "Llama Herd" - Llama 3.1 och Llama 3.2.

Dessa modeller finns i olika varianter och är tillgängliga i [Microsoft Foundry Models-katalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Notera:** GitHub Models fasas ut i slutet av juli 2026. Här finns mer information om att använda [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) för att prototypa med AI-modeller.

Modellvarianter: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Notera: Llama 3 finns också i Microsoft Foundry Models men kommer inte att täckas i denna lektion*

## Llama 3.1 

Med 405 miljarder parametrar passar Llama 3.1 in i kategorin open source LLM. 

Modellen är en uppgradering av den tidigare versionen Llama 3 genom att erbjuda: 

- Större kontextfönster - 128k tokens jämfört med 8k tokens 
- Större Max Output Tokens - 4096 jämfört med 2048 
- Bättre flerspråkigt stöd - tack vare ökat antal tränings-tokens 

Dessa möjliggör att Llama 3.1 kan hantera mer komplexa användningsfall vid byggande av GenAI-applikationer inklusive: 
- Inbyggda funktionsanrop - möjligheten att anropa externa verktyg och funktioner utanför LLM-flödet
- Bättre RAG-prestanda - tack vare det större kontextfönstret 
- Syntetisk datagenerering - möjligheten att skapa effektiv data för uppgifter som finjustering 

### Inbyggda funktionsanrop 

Llama 3.1 har finjusterats för att vara mer effektiv vid funktions- eller verktygsanrop. Den har också två inbyggda verktyg som modellen kan identifiera som behövande användas baserat på användarens prompt. Dessa verktyg är: 

- **Brave Search** - Kan användas för att få uppdaterad information som väder genom att göra en webbsökning 
- **Wolfram Alpha** - Kan användas för mer komplexa matematiska beräkningar så att du inte behöver skriva egna funktioner. 

Du kan också skapa egna anpassade verktyg som LLM kan anropa. 

I kodexemplet nedan: 

- Definierar vi tillgängliga verktyg (brave_search, wolfram_alpha) i systemprompten. 
- Skickar en användarprompt som frågar om vädret i en viss stad. 
- LLM svarar med ett verktygsanrop till Brave Search-verktyget som kommer att se ut så här `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Notera: Detta exempel gör endast verktygsanropet, om du vill få resultatet behöver du skapa ett gratis konto på Brave API-sidan och definiera funktionen själv.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Hämta dessa från din Microsoft Foundry-projekts "Översikt"-sida
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

Trots att det är en LLM, är en begränsning med Llama 3.1 dess brist på multimodalitet. Det vill säga, oförmågan att använda olika typer av indata som bilder som prompts och ge svar. Denna förmåga är en av huvudfunktionerna i Llama 3.2. Dessa funktioner inkluderar också: 

- Multimodalitet - har förmågan att utvärdera både text- och bildprompter 
- Mindre till medelstora storleksvarianter (11B och 90B) - detta ger flexibla distributionsalternativ, 
- Endast text-varianter (1B och 3B) - detta gör att modellen kan distribueras på edge / mobila enheter och ger låg latens 

Det multimodala stödet representerar ett stort steg i världen av open source-modeller. Kodexemplet nedan tar både en bild och en textprompt för att få en analys av bilden från Llama 3.2 90B. 


### Multimodalt stöd med Llama 3.2

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

# Hämta dessa från din Microsoft Foundry-projekts "Översikt"-sida
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

## Lärandet slutar inte här, fortsätt resan

Efter att ha genomfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->