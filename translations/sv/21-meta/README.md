# Bygga med Meta Family-modellerna

## Introduktion

Den här lektionen kommer att täcka:

- Utforska de två huvudsakliga Meta family-modellerna - Llama 3.1 och Llama 3.2
- Förstå användningsfall och scenarier för varje modell
- Kodexempel som visar de unika funktionerna hos varje modell

## Meta Family av modeller

I denna lektion kommer vi att utforska 2 modeller från Meta-familjen eller "Llama Herd" - Llama 3.1 och Llama 3.2.

Dessa modeller finns i olika varianter och är tillgängliga på GitHub Model-marknaden. Här är mer information om att använda GitHub Models för att [prototypa med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Obs: Llama 3 finns också tillgänglig på GitHub Models men kommer inte att täckas i denna lektion*

## Llama 3.1

Med 405 miljarder parametrar passar Llama 3.1 in i kategorin open source LLM.

Modellen är en uppgradering av den tidigare utgåvan Llama 3 genom att erbjuda:

- Större kontextfönster - 128k tokens kontra 8k tokens
- Större Max Output Tokens - 4096 kontra 2048
- Bättre flerspråkigt stöd - tack vare ökat antal tränings-tokens

Dessa möjliggör för Llama 3.1 att hantera mer komplexa användningsfall vid byggande av GenAI-applikationer inklusive:
- Native Function Calling - möjligheten att anropa externa verktyg och funktioner utanför LLM-flödet
- Bättre RAG-prestanda - tack vare det större kontextfönstret
- Syntetisk datagenerering - förmågan att skapa effektiv data för uppgifter som finjustering

### Native Function Calling

Llama 3.1 har finjusterats för att vara mer effektiv vid funktions- eller verktygsanrop. Den har också två inbyggda verktyg som modellen kan identifiera att den behöver använda baserat på användarens prompt. Dessa verktyg är:

- **Brave Search** - Kan användas för att få uppdaterad information som väder genom att göra en webbsökning
- **Wolfram Alpha** - Kan användas för mer komplexa matematiska beräkningar så du behöver inte skriva egna funktioner.

Du kan även skapa dina egna anpassade verktyg som LLM kan anropa.

I kodexemplet nedan:

- Definierar vi de tillgängliga verktygen (brave_search, wolfram_alpha) i systempromten.
- Skickar en användarprompt som frågar om vädret i en viss stad.
- LLM svarar med ett verktygsanrop till Brave Search-verktyget som kommer se ut så här `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Obs: Detta exempel gör endast verktygsanropet, om du vill få resultaten behöver du skapa ett gratis konto på Brave API-sidan och definiera själva funktionen.

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

Trots att det är en LLM är en begränsning för Llama 3.1 dess brist på multimodalitet. Det vill säga oförmåga att använda olika typer av indata som bilder som prompts och ge svar. Denna förmåga är en av huvudfunktionerna i Llama 3.2. Dessa funktioner inkluderar också:

- Multimodalitet - har förmågan att utvärdera både text- och bildprompter
- Små till medelstora variationer (11B och 90B) - detta ger flexibla distributionsalternativ,
- Endast text-variationer (1B och 3B) - detta tillåter modellen att distribueras på edge/mobila enheter och ger låg latens

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

Efter att du har genomfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av den AI-baserade översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->