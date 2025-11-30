<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:10:50+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "no"
}
-->
# Bygge med Meta-familie-modellene

## Introduksjon

Denne leksjonen vil dekke:

- Utforske de to hovedmodellene i Meta-familien – Llama 3.1 og Llama 3.2
- Forstå bruksområder og scenarier for hver modell
- Kodeeksempel som viser de unike funksjonene til hver modell

## Meta-familien av modeller

I denne leksjonen skal vi utforske 2 modeller fra Meta-familien eller "Llama Herd" – Llama 3.1 og Llama 3.2

Disse modellene finnes i ulike varianter og er tilgjengelige på GitHub Model-markedet. Her er mer informasjon om hvordan du bruker GitHub Models for å [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianter:  
- Llama 3.1 – 70B Instruct  
- Llama 3.1 – 405B Instruct  
- Llama 3.2 – 11B Vision Instruct  
- Llama 3.2 – 90B Vision Instruct  

*Merk: Llama 3 er også tilgjengelig på GitHub Models, men dekkes ikke i denne leksjonen*

## Llama 3.1

Med 405 milliarder parametere, plasserer Llama 3.1 seg i kategorien åpne kildekode LLM.

Modellen er en oppgradering av den tidligere utgivelsen Llama 3 ved å tilby:

- Større kontekstvindu – 128k tokens mot 8k tokens  
- Større maks utgangstokens – 4096 mot 2048  
- Bedre flerspråklig støtte – takket være økt antall trenings-tokens  

Dette gjør at Llama 3.1 kan håndtere mer komplekse bruksområder når man bygger GenAI-applikasjoner, inkludert:  
- Native Function Calling – muligheten til å kalle eksterne verktøy og funksjoner utenfor LLM-arbeidsflyten  
- Bedre RAG-ytelse – takket være det større kontekstvinduet  
- Syntetisk datagenerering – evnen til å lage effektiv data for oppgaver som finjustering  

### Native Function Calling

Llama 3.1 er finjustert for å være mer effektiv til å gjøre funksjons- eller verktøysanrop. Den har også to innebygde verktøy som modellen kan identifisere at den trenger å bruke basert på brukerens prompt. Disse verktøyene er:

- **Brave Search** – Kan brukes for å hente oppdatert informasjon som værmelding ved å utføre et nettsøk  
- **Wolfram Alpha** – Kan brukes til mer komplekse matematiske beregninger, så du slipper å skrive egne funksjoner  

Du kan også lage dine egne tilpassede verktøy som LLM kan kalle.

I kodeeksempelet under:

- Definerer vi tilgjengelige verktøy (brave_search, wolfram_alpha) i systemprompten.  
- Sender en brukerprompt som spør om været i en bestemt by.  
- LLM vil svare med et verktøysanrop til Brave Search-verktøyet som vil se slik ut `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Merk: Dette eksempelet gjør kun verktøysanropet, hvis du ønsker å få resultatene må du opprette en gratis konto på Brave API-siden og definere funksjonen selv*

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

Selv om Llama 3.1 er en LLM, har den en begrensning når det gjelder multimodalitet. Det vil si evnen til å bruke ulike typer input som bilder som prompt og gi svar. Denne evnen er en av hovedfunksjonene i Llama 3.2. Andre funksjoner inkluderer:

- Multimodalitet – har evnen til å evaluere både tekst- og bildeprompter  
- Små til mellomstore varianter (11B og 90B) – gir fleksible distribusjonsmuligheter  
- Tekst-only varianter (1B og 3B) – gjør det mulig å kjøre modellen på edge-/mobilenheter med lav ventetid  

Den multimodale støtten representerer et stort steg i verden av åpne kildekode-modeller. Kodeeksempelet under tar både et bilde og en tekstprompt for å få en analyse av bildet fra Llama 3.2 90B.

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

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.