<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:10:37+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "da"
}
-->
# Byg med Meta Family-modellerne

## Introduktion

Denne lektion vil dække:

- Gennemgang af de to hovedmodeller i Meta-familien - Llama 3.1 og Llama 3.2  
- Forståelse af anvendelsestilfælde og scenarier for hver model  
- Kodeeksempel, der viser de unikke funktioner i hver model  

## Meta-familien af modeller

I denne lektion vil vi udforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2

Disse modeller findes i forskellige varianter og er tilgængelige på GitHub Model-markedspladsen. Her er flere detaljer om brugen af GitHub Models til at [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelvarianter:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Bemærk: Llama 3 er også tilgængelig på GitHub Models, men vil ikke blive dækket i denne lektion*

## Llama 3.1

Med 405 milliarder parametre hører Llama 3.1 til i kategorien open source LLM.

Modellen er en opgradering af den tidligere udgave Llama 3 og tilbyder:

- Større kontekstvindue - 128k tokens mod 8k tokens  
- Større maks. output tokens - 4096 mod 2048  
- Bedre flersproget support - takket være flere træningstokens  

Disse forbedringer gør Llama 3.1 i stand til at håndtere mere komplekse anvendelsestilfælde, når man bygger GenAI-applikationer, herunder:  
- Native Function Calling - evnen til at kalde eksterne værktøjer og funktioner uden for LLM-arbejdsgangen  
- Bedre RAG-ydeevne - takket være det større kontekstvindue  
- Syntetisk datagenerering - evnen til at skabe effektiv data til opgaver som finjustering  

### Native Function Calling

Llama 3.1 er finjusteret til at være mere effektiv til at foretage funktions- eller værktøjskald. Den har også to indbyggede værktøjer, som modellen kan identificere som nødvendige at bruge baseret på brugerens prompt. Disse værktøjer er:

- **Brave Search** - Kan bruges til at hente opdaterede oplysninger som vejret ved at udføre en web-søgning  
- **Wolfram Alpha** - Kan bruges til mere komplekse matematiske beregninger, så du ikke behøver at skrive dine egne funktioner  

Du kan også oprette dine egne brugerdefinerede værktøjer, som LLM kan kalde.

I kodeeksemplet nedenfor:

- Definerer vi de tilgængelige værktøjer (brave_search, wolfram_alpha) i systemprompten.  
- Sender en brugerprompt, der spørger om vejret i en bestemt by.  
- LLM vil svare med et værktøjskald til Brave Search-værktøjet, som vil se sådan ud `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Bemærk: Dette eksempel foretager kun værktøjskaldet. Hvis du vil have resultaterne, skal du oprette en gratis konto på Brave API-siden og definere funktionen selv*  

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

Selvom Llama 3.1 er en LLM, har den en begrænsning i forhold til multimodalitet. Det vil sige evnen til at bruge forskellige typer input som billeder som prompts og give svar. Denne evne er en af hovedfunktionerne i Llama 3.2. Disse funktioner inkluderer også:

- Multimodalitet - evnen til at evaluere både tekst- og billedprompter  
- Små til mellemstore varianter (11B og 90B) - giver fleksible implementeringsmuligheder  
- Tekst-only varianter (1B og 3B) - gør det muligt at implementere modellen på edge-/mobilenheder med lav latenstid  

Den multimodale support repræsenterer et stort skridt i open source-modellernes verden. Kodeeksemplet nedenfor tager både et billede og en tekstprompt for at få en analyse af billedet fra Llama 3.2 90B.

### Multimodal support med Llama 3.2

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

## Læringen stopper ikke her, fortsæt rejsen

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at udvikle din viden om Generative AI!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.