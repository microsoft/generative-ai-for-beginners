<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:12:07+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sv"
}
-->
# Bygga med Meta-familjens modeller

## Introduktion

Denna lektion kommer att täcka:

- Utforska de två huvudmodellerna i Meta-familjen - Llama 3.1 och Llama 3.2
- Förstå användningsfall och scenarier för varje modell
- Kodexempel för att visa de unika egenskaperna hos varje modell

## Meta-familjens modeller

I denna lektion kommer vi att utforska 2 modeller från Meta-familjen eller "Llama Herd" - Llama 3.1 och Llama 3.2

Dessa modeller finns i olika varianter och är tillgängliga på GitHub Model-marknadsplatsen. Här är mer information om att använda GitHub-modeller för att [prototypa med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Obs: Llama 3 är också tillgänglig på GitHub-modeller men kommer inte att täckas i denna lektion*

## Llama 3.1

Med 405 miljarder parametrar passar Llama 3.1 in i kategorin öppen källkod LLM.

Modellen är en uppgradering av den tidigare versionen Llama 3 genom att erbjuda:

- Större kontextfönster - 128k tokens vs 8k tokens
- Större Max Output Tokens - 4096 vs 2048
- Bättre flerspråkigt stöd - på grund av ökning i träningstokens

Dessa möjliggör för Llama 3.1 att hantera mer komplexa användningsfall vid byggande av GenAI-applikationer inklusive:
- Inbyggd funktionsanrop - förmågan att anropa externa verktyg och funktioner utanför LLM-arbetsflödet
- Bättre RAG-prestanda - tack vare det större kontextfönstret
- Generering av syntetiska data - förmågan att skapa effektiv data för uppgifter som finjustering

### Inbyggd funktionsanrop

Llama 3.1 har finjusterats för att vara mer effektiv vid funktions- eller verktygsanrop. Den har också två inbyggda verktyg som modellen kan identifiera som behövande att användas baserat på användarens prompt. Dessa verktyg är:

- **Brave Search** - Kan användas för att få uppdaterad information som väder genom att utföra en webbsökning
- **Wolfram Alpha** - Kan användas för mer komplexa matematiska beräkningar så att du inte behöver skriva egna funktioner.

Du kan också skapa egna anpassade verktyg som LLM kan anropa.

I kodexemplet nedan:

- Vi definierar de tillgängliga verktygen (brave_search, wolfram_alpha) i systemprompten.
- Skicka en användarprompt som frågar om vädret i en viss stad.
- LLM kommer att svara med ett verktygsanrop till Brave Search-verktyget som kommer att se ut så här `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Obs: Detta exempel gör bara verktygsanropet, om du vill få resultaten måste du skapa ett gratis konto på Brave API-sidan och definiera funktionen själv`

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

Trots att det är en LLM har Llama 3.1 en begränsning i multimodalitet. Det vill säga att kunna använda olika typer av input som bilder som prompts och ge svar. Denna förmåga är en av huvudfunktionerna hos Llama 3.2. Dessa funktioner inkluderar också:

- Multimodalitet - har förmågan att utvärdera både text- och bildprompts
- Små till medelstora storleksvariationer (11B och 90B) - detta ger flexibla distributionsalternativ,
- Endast textvariationer (1B och 3B) - detta gör det möjligt för modellen att distribueras på edge / mobila enheter och ger låg latens

Det multimodala stödet representerar ett stort steg i världen av öppna källkodsmodeller. Kodexemplet nedan tar både en bild och textprompt för att få en analys av bilden från Llama 3.2 90B.

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

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja din kunskap om Generative AI!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår från användningen av denna översättning.