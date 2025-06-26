<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:32:16+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "no"
}
-->
# Bygging med Meta-familien av modeller

## Introduksjon

Denne leksjonen vil dekke:

- Utforsking av de to hovedmodellene i Meta-familien - Llama 3.1 og Llama 3.2
- Forståelse av bruksområder og scenarier for hver modell
- Kodeeksempel for å vise de unike funksjonene til hver modell

## Meta-familien av modeller

I denne leksjonen vil vi utforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2

Disse modellene kommer i forskjellige varianter og er tilgjengelige på GitHub Model-markedsplassen. Her er flere detaljer om bruk av GitHub Models til [prototyping med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Merk: Llama 3 er også tilgjengelig på GitHub Models, men vil ikke bli dekket i denne leksjonen*

## Llama 3.1

Med 405 milliarder parametere passer Llama 3.1 inn i kategorien for åpen kildekode LLM.

Modellen er en oppgradering fra den tidligere utgivelsen Llama 3 ved å tilby:

- Større kontekstvindu - 128k tokens vs 8k tokens
- Større maks utgangstokens - 4096 vs 2048
- Bedre flerspråklig støtte - på grunn av økning i treningstokens

Disse gjør det mulig for Llama 3.1 å håndtere mer komplekse bruksområder når man bygger GenAI-applikasjoner, inkludert:
- Innfødt funksjonskalling - evnen til å kalle eksterne verktøy og funksjoner utenfor LLM-arbeidsflyten
- Bedre RAG-ytelse - på grunn av det høyere kontekstvinduet
- Syntetisk datagenerering - evnen til å lage effektiv data for oppgaver som finjustering

### Innfødt funksjonskalling

Llama 3.1 har blitt finjustert for å være mer effektiv til å utføre funksjons- eller verktøykall. Den har også to innebygde verktøy som modellen kan identifisere som nødvendige å bruke basert på brukerens forespørsel. Disse verktøyene er:

- **Brave Search** - Kan brukes til å få oppdatert informasjon som været ved å utføre et nettsøk
- **Wolfram Alpha** - Kan brukes til mer komplekse matematiske beregninger, slik at du ikke trenger å skrive dine egne funksjoner.

Du kan også lage dine egne tilpassede verktøy som LLM kan kalle.

I kodeeksempelet nedenfor:

- Vi definerer de tilgjengelige verktøyene (brave_search, wolfram_alpha) i systemforespørselen.
- Sender en brukerforespørsel som spør om været i en bestemt by.
- LLM vil svare med et verktøykall til Brave Search-verktøyet som vil se slik ut `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Merk: Dette eksempelet gjør bare verktøykallet, hvis du ønsker å få resultatene, må du opprette en gratis konto på Brave API-siden og definere funksjonen selv*

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

Selv om det er en LLM, har Llama 3.1 en begrensning når det gjelder multimodalitet. Det vil si å kunne bruke forskjellige typer input som bilder som forespørsler og gi svar. Denne evnen er en av hovedfunksjonene til Llama 3.2. Disse funksjonene inkluderer også:

- Multimodalitet - har evnen til å evaluere både tekst- og bildeforespørsler
- Små til mellomstore størrelsesvarianter (11B og 90B) - dette gir fleksible distribusjonsalternativer,
- Tekstbare varianter (1B og 3B) - dette gjør det mulig å distribuere modellen på kant- / mobile enheter og gir lav ventetid

Den multimodale støtten representerer et stort skritt i verden av åpen kildekode-modeller. Kodeeksempelet nedenfor tar både en bilde- og tekstforespørsel for å få en analyse av bildet fra Llama 3.2 90B.

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

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve din kunnskap om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.