# Bygge med Meta-familie modellene 

## Introduksjon 

Denne leksjonen vil dekke: 

- Utforske de to hovedmodellene i Meta-familien - Llama 3.1 og Llama 3.2 
- Forstå brukstilfellene og scenariene for hver modell 
- Kodeeksempel som viser de unike funksjonene til hver modell 


## Meta familien av modeller 

I denne leksjonen skal vi utforske 2 modeller fra Meta-familien eller "Llama-flokken" - Llama 3.1 og Llama 3.2.

Disse modellene finnes i forskjellige varianter og er tilgjengelige i [Microsoft Foundry Models-katalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Merk:** GitHub Models avvikles ved slutten av juli 2026. Her er flere detaljer om bruk av [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) for å prototypere med AI-modeller.

Modellvarianter: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Merk: Llama 3 er også tilgjengelig i Microsoft Foundry Models, men dekkes ikke i denne leksjonen*

## Llama 3.1 

Med 405 milliarder parametere passer Llama 3.1 inn i kategorien open source LLM. 

Modellen er en oppgradering av den tidligere utgivelsen Llama 3 ved å tilby: 

- Større kontekstvindu - 128k tokens vs 8k tokens 
- Større maks utgående tokens - 4096 vs 2048 
- Bedre flerspråklig støtte - på grunn av økt antall treningstokener 

Dette gjør at Llama 3.1 kan håndtere mer komplekse brukstilfeller når man bygger GenAI-applikasjoner inkludert: 
- Native funksjonsanrop - muligheten til å kalle eksterne verktøy og funksjoner utenfor LLM-arbeidsflyten
- Bedre RAG-ytelse - på grunn av det høyere kontekstvinduet 
- Syntetisk datagenerering - muligheten til å lage effektiv data for oppgaver som finjustering 

### Native funksjonsanrop 

Llama 3.1 er finjustert for å være mer effektiv til å gjøre funksjons- eller verktøysanrop. Den har også to innebygde verktøy som modellen kan identifisere som nødvendige å bruke basert på brukerens prompt. Disse verktøyene er: 

- **Brave Search** - Kan brukes for å få oppdatert informasjon som vær ved å utføre et nettsøk 
- **Wolfram Alpha** - Kan brukes for mer komplekse matematiske beregninger slik at det ikke er nødvendig å skrive egne funksjoner. 

Du kan også lage dine egne tilpassede verktøy som LLM-en kan kalle. 

I kodeeksemplet nedenfor: 

- Definerer vi de tilgjengelige verktøyene (brave_search, wolfram_alpha) i systemprompten. 
- Sender en brukerprompt som spør om været i en bestemt by. 
- LLM-en vil svare med et verktøysanrop til Brave Search-verktøyet som vil se slik ut `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Merk: Dette eksemplet gjør bare verktøysanropet, hvis du ønsker å få resultatene må du opprette en gratis konto på Brave API-siden og definere funksjonen selv.

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

Til tross for å være en LLM, er en begrensning med Llama 3.1 dens mangel på multimodalitet. Det vil si manglende evne til å bruke forskjellige typer input som bilder som prompts og gi svar. Denne evnen er en av hovedfunksjonene til Llama 3.2. Disse funksjonene inkluderer også: 

- Multimodalitet - har evnen til å evaluere både tekst- og bildeprompter 
- Varianter i små til mellomstore størrelser (11B og 90B) - dette gir fleksible distribusjonsmuligheter, 
- Kun tekst-varianter (1B og 3B) - dette lar modellen distribueres på edge / mobile enheter og gir lav ventetid 

Den multimodale støtten representerer et stort steg i verden for open source-modeller. Kodeeksemplet nedenfor tar både et bilde og tekstprompt for å få en analyse av bildet fra Llama 3.2 90B. 


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

# Få disse fra "Oversikt"-siden i Microsoft Foundry-prosjektet ditt
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

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å bygge på din kunnskap om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->