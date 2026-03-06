# Bygge med Meta-familie-modellene

## Introduksjon

Denne leksjonen vil dekke:

- Utforske de to hovedmodellene i Meta-familien - Llama 3.1 og Llama 3.2
- Forstå bruksområder og scenarier for hver modell
- Kodeeksempel som viser de unike funksjonene til hver modell

## Meta-familien av modeller

I denne leksjonen skal vi utforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2.

Disse modellene finnes i forskjellige varianter og er tilgjengelige på GitHub Model marketplace. Her er mer informasjon om bruk av GitHub Models for å [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Merk: Llama 3 er også tilgjengelig på GitHub Models, men vil ikke bli dekket i denne leksjonen*

## Llama 3.1

Med 405 milliarder parametere faller Llama 3.1 inn i kategorien åpen kildekode LLM.

Modellen er en oppgradering av den tidligere utgivelsen Llama 3 ved å tilby:

- Større kontekstvindu - 128k tokens vs 8k tokens
- Større maks output tokens - 4096 vs 2048
- Bedre flerspråklig støtte - på grunn av økning i trenings-tokens

Disse egenskapene gjør at Llama 3.1 kan håndtere mer komplekse bruksområder ved bygging av GenAI-applikasjoner inkludert:
- Innebygd funksjonskalling - evnen til å kalle eksterne verktøy og funksjoner utenfor LLM-arbeidsflyten
- Bedre RAG-ytelse - på grunn av det større kontekstvinduet
- Syntetisk datagenerering - evnen til å lage effektiv data for oppgaver som finjustering

### Innebygd funksjonskalling

Llama 3.1 har blitt finjustert for å være mer effektiv til å utføre funksjons- eller verktøykall. Den har også to innebygde verktøy som modellen kan identifisere som nødvendige å bruke basert på brukerens prompt. Disse verktøyene er:

- **Brave Search** - Kan brukes for å hente oppdatert informasjon som vær ved å utføre et nettsøk
- **Wolfram Alpha** - Kan brukes for mer komplekse matematiske beregninger, så du trenger ikke skrive dine egne funksjoner.

Du kan også lage egne egendefinerte verktøy som LLM kan kalle.

I kodeeksemplet under:

- Definerer vi tilgjengelige verktøy (brave_search, wolfram_alpha) i systemprompten.
- Sender en brukerprompt som spør om været i en bestemt by.
- LLM vil svare med et verktøykall til Brave Search-verktøyet som vil se slik ut `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Merk: Dette eksempelet utfører bare verktøykallet, hvis du vil ha resultatene må du opprette en gratis konto på Brave API-siden og definere funksjonen selv.

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

Til tross for å være en LLM, har Llama 3.1 den begrensningen at den ikke er multimodal. Det vil si, den kan ikke bruke ulike typer input som bilder som prompt og gi svar. Denne muligheten er en av hovedfunksjonene i Llama 3.2. Disse funksjonene inkluderer også:

- Multimodalitet - har evnen til å evaluere både tekst- og bilde-prompter
- Små til mellomstore varianter (11B og 90B) - dette gir fleksible distribusjonsalternativer,
- Tekst-only varianter (1B og 3B) - dette gjør at modellen kan distribueres på edge / mobile enheter og gir lav ventetid

Multimodal støtten representerer et stort steg i verden av open source-modeller. Kodeeksemplet under tar både et bilde og tekst prompt for å få en analyse av bildet fra Llama 3.2 90B.

### Multimodal støtte med Llama 3.2

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

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi påtar oss ikke ansvar for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->