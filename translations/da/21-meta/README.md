<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:12:24+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "da"
}
-->
# Bygning med Meta-familien af modeller

## Introduktion

Denne lektion vil dække:

- Udforskning af de to hovedmodeller i Meta-familien - Llama 3.1 og Llama 3.2
- Forståelse af anvendelsesområder og scenarier for hver model
- Kodeeksempel til at vise de unikke funktioner ved hver model

## Meta-familien af modeller

I denne lektion vil vi udforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2.

Disse modeller kommer i forskellige varianter og er tilgængelige på GitHub Model marketplace. Her er flere detaljer om brug af GitHub Models til [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelvarianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Bemærk: Llama 3 er også tilgængelig på GitHub Models, men vil ikke blive dækket i denne lektion*

## Llama 3.1

Med 405 milliarder parametre passer Llama 3.1 ind i kategorien open source LLM.

Modellen er en opgradering til den tidligere udgivelse Llama 3 ved at tilbyde:

- Større kontekstvindue - 128k tokens vs 8k tokens
- Større Maks Output Tokens - 4096 vs 2048
- Bedre flersproget støtte - på grund af stigning i træningstokens

Disse gør Llama 3.1 i stand til at håndtere mere komplekse anvendelser ved opbygning af GenAI-applikationer, herunder:
- Native Function Calling - evnen til at kalde eksterne værktøjer og funktioner uden for LLM-arbejdsgangen
- Bedre RAG-ydeevne - på grund af det højere kontekstvindue
- Syntetisk datagenerering - evnen til at skabe effektiv data til opgaver som finjustering

### Native Function Calling

Llama 3.1 er blevet finjusteret til at være mere effektiv til at lave funktion- eller værktøjskald. Den har også to indbyggede værktøjer, som modellen kan identificere som nødvendige at bruge baseret på brugerens prompt. Disse værktøjer er:

- **Brave Search** - Kan bruges til at få opdateret information som vejret ved at udføre en websøgning
- **Wolfram Alpha** - Kan bruges til mere komplekse matematiske beregninger, så det ikke er nødvendigt at skrive dine egne funktioner.

Du kan også oprette dine egne tilpassede værktøjer, som LLM kan kalde.

I kodeeksemplet nedenfor:

- Vi definerer de tilgængelige værktøjer (brave_search, wolfram_alpha) i systemprompten.
- Sender en brugerprompt, der spørger om vejret i en bestemt by.
- LLM vil svare med et værktøjskald til Brave Search-værktøjet, som vil se sådan ud `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Bemærk: Dette eksempel laver kun værktøjskaldet, hvis du gerne vil have resultaterne, skal du oprette en gratis konto på Brave API-siden og definere funktionen selv*

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

Selvom det er en LLM, har Llama 3.1 en begrænsning i multimodalitet. Det vil sige at kunne bruge forskellige typer input såsom billeder som prompts og give svar. Denne evne er en af de vigtigste funktioner i Llama 3.2. Disse funktioner inkluderer også:

- Multimodalitet - har evnen til at evaluere både tekst- og billedprompts
- Små til mellemstore størrelsesvarianter (11B og 90B) - dette giver fleksible implementeringsmuligheder,
- Kun tekstvarianter (1B og 3B) - dette gør det muligt for modellen at blive implementeret på edge / mobile enheder og giver lav latenstid

Den multimodale støtte repræsenterer et stort skridt i verden af open source-modeller. Kodeeksemplet nedenfor tager både et billede og tekstprompt for at få en analyse af billedet fra Llama 3.2 90B.

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

## Læring stopper ikke her, fortsæt rejsen

Efter at have afsluttet denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generative AI!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Mens vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger som følge af brugen af denne oversættelse.