<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:10:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sv"
}
-->
# Bygga med Meta Family-modellerna

## Introduktion

Den här lektionen täcker:

- Utforska de två huvudsakliga Meta Family-modellerna – Llama 3.1 och Llama 3.2  
- Förstå användningsområden och scenarier för varje modell  
- Kodexempel som visar varje modells unika funktioner  

## Meta Family-modellerna

I den här lektionen kommer vi att utforska 2 modeller från Meta-familjen eller "Llama Herd" – Llama 3.1 och Llama 3.2

Dessa modeller finns i olika varianter och är tillgängliga på GitHub Model marketplace. Här är mer information om hur du använder GitHub Models för att [prototypa med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:  
- Llama 3.1 – 70B Instruct  
- Llama 3.1 – 405B Instruct  
- Llama 3.2 – 11B Vision Instruct  
- Llama 3.2 – 90B Vision Instruct  

*Notera: Llama 3 finns också på GitHub Models men tas inte upp i den här lektionen*

## Llama 3.1

Med 405 miljarder parametrar tillhör Llama 3.1 kategorin open source LLM.

Modellen är en uppgradering av den tidigare versionen Llama 3 och erbjuder:

- Större kontextfönster – 128k tokens jämfört med 8k tokens  
- Större max antal output-tokens – 4096 jämfört med 2048  
- Bättre flerspråkigt stöd – tack vare fler träningsdata  

Detta gör att Llama 3.1 kan hantera mer komplexa användningsfall vid utveckling av GenAI-applikationer, inklusive:  
- Native Function Calling – möjligheten att anropa externa verktyg och funktioner utanför LLM-flödet  
- Bättre RAG-prestanda – tack vare det större kontextfönstret  
- Syntetisk datagenerering – förmågan att skapa effektiv data för uppgifter som finjustering  

### Native Function Calling

Llama 3.1 har finjusterats för att bli bättre på att göra funktions- eller verktygsanrop. Den har också två inbyggda verktyg som modellen kan identifiera att den behöver använda baserat på användarens prompt. Dessa verktyg är:

- **Brave Search** – Kan användas för att hämta uppdaterad information som väder genom att göra en webbsökning  
- **Wolfram Alpha** – Kan användas för mer avancerade matematiska beräkningar så att du slipper skriva egna funktioner  

Du kan också skapa egna anpassade verktyg som LLM kan anropa.

I kodexemplet nedan:

- Definierar vi tillgängliga verktyg (brave_search, wolfram_alpha) i systemprompten.  
- Skickar en användarprompt som frågar om vädret i en viss stad.  
- LLM svarar med ett verktygsanrop till Brave Search-verktyget som ser ut så här `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Notera: Detta exempel gör endast verktygsanropet, om du vill få resultaten behöver du skapa ett gratis konto på Brave API-sidan och definiera funktionen själv*

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

Trots att Llama 3.1 är en LLM finns en begränsning i multimodalitet, det vill säga att kunna använda olika typer av input som bilder som prompt och ge svar. Denna förmåga är en av huvudfunktionerna i Llama 3.2. Andra funktioner inkluderar:

- Multimodalitet – kan hantera både text- och bildpromptar  
- Små till medelstora varianter (11B och 90B) – ger flexibla distributionsalternativ  
- Endast text-varianter (1B och 3B) – möjliggör distribution på edge-/mobila enheter med låg latens  

Det multimodala stödet är ett stort steg framåt inom open source-modeller. Kodexemplet nedan tar både en bild och en textprompt för att få en analys av bilden från Llama 3.2 90B.

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

## Lärandet slutar inte här, fortsätt resan

Efter att ha genomfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generative AI!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.