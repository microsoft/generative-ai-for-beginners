# Bygge med Meta-familie modellene 

## Innledning 

Denne leksjonen vil dekke: 

- Utforske de to hovedmodellene i Meta-familien - Llama 3.1 og Llama 3.2 
- Forstå brukstilfellene og scenariene for hver modell 
- Kodeeksempel for å vise de unike funksjonene til hver modell 


## Meta-familien av modeller 

I denne leksjonen vil vi utforske 2 modeller fra Meta-familien eller "Llama-stammen" - Llama 3.1 og Llama 3.2.

Disse modellene kommer i forskjellige varianter og er tilgjengelige i [Microsoft Foundry Models katalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Merk:** GitHub Models avsluttes i slutten av juli 2026. Her er flere detaljer om bruk av [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) for å prototype med AI-modeller.

Modellvarianter: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Merk: Llama 3 er også tilgjengelig i Microsoft Foundry Models, men vil ikke bli dekket i denne leksjonen*

## Llama 3.1 

Med 405 milliarder parametere, faller Llama 3.1 inn i kategorien open source LLM. 

Modellen er en oppgradering av den tidligere utgivelsen Llama 3 ved å tilby: 

- Større kontekstvindu - 128k tokens vs 8k tokens 
- Større Maks Utgangs-Tokens - 4096 vs 2048 
- Bedre flerspråklig støtte - på grunn av økning i treningstokener 

Disse gjør at Llama 3.1 kan håndtere mer komplekse brukstilfeller når du bygger GenAI-applikasjoner, inkludert: 
- Native Funksjonskalling - muligheten til å kalle eksterne verktøy og funksjoner utenfor LLM-arbeidsflyten
- Bedre RAG-ytelse - takket være det høyere kontekstvinduet 
- Syntetisk datagenerering - muligheten til å lage effektiv data for oppgaver som finjustering 

### Native Funksjonskalling 

Llama 3.1 har blitt finjustert for å være mer effektiv til å gjøre funksjons- eller verktøykall. Den har også to innebygde verktøy som modellen kan identifisere som nødvendige å bruke basert på brukerens prompt. Disse verktøyene er: 

- **Brave Search** - Kan brukes for å få oppdatert informasjon som været ved å utføre et nettsøk 
- **Wolfram Alpha** - Kan brukes for mer komplekse matematiske beregninger, så det er ikke nødvendig å skrive dine egne funksjoner. 

Du kan også lage dine egne tilpassede verktøy som LLM-en kan kalle. 

I kodeeksempelet nedenfor: 

- Definerer vi tilgjengelige verktøy (brave_search, wolfram_alpha) i systemprompten. 
- Sender en brukerprompt som spør om været i en bestemt by. 
- LLM-en vil svare med et verktøykall til Brave Search-verktøyet som vil se slik ut `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Merk: Dette eksempelet gjør bare verktøykallet, dersom du vil ha resultatene må du opprette en gratis konto på Brave API-siden og definere funksjonen selv.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Hent disse fra "Oversikt"-siden i Microsoft Foundry-prosjektet ditt
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

Til tross for å være en LLM, er en begrensning med Llama 3.1 dens mangel på multimodalitet. Det vil si manglende evne til å bruke forskjellige typer input som bilder som prompt og gi svar. Denne evnen er en av hovedfunksjonene til Llama 3.2. Disse funksjonene inkluderer også: 

- Multimodalitet - har evnen til å evaluere både tekst- og bilde-prompt 
- Varianter i liten til medium størrelse (11B og 90B) - dette gir fleksible distribusjonsmuligheter, 
- Tekst-only-varianter (1B og 3B) - dette gjør at modellen kan distribueres på edge / mobile enheter og gir lav ventetid 

Multimodal støtte representerer et stort steg i verden av open source modeller. Kodeeksempelet nedenfor tar både et bilde og en tekstprompt for å få en analyse av bildet fra Llama 3.2 90B. 


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

# Hent disse fra "Oversikt"-siden i Microsoft Foundry-prosjektet ditt
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

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å øke din kunnskap om Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->