# Bygning med Meta-familie modellerne

## Introduktion

Denne lektion vil dække:

- Udforskning af de to hoved Meta-familie modeller - Llama 3.1 og Llama 3.2
- Forståelse af brugsscenarier og situationer for hver model
- Kodeeksempel til at vise de unikke funktioner i hver model

## Meta-familien af Modeller

I denne lektion vil vi udforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2.

Disse modeller findes i forskellige varianter og er tilgængelige på GitHub Model-markedspladsen. Her er flere detaljer om brug af GitHub Models til at [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Model Varianter:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Bemærk: Llama 3 er også tilgængelig på GitHub Models, men vil ikke blive dækket i denne lektion*

## Llama 3.1

Med 405 milliarder parametre passer Llama 3.1 ind i kategorien open source LLM.

Modellen er en opgradering af den tidligere version Llama 3 ved at tilbyde:

- Større kontekstvindue - 128k tokens mod 8k tokens
- Større Maks Output Tokens - 4096 mod 2048
- Bedre Multisproglig Support - på grund af større mængde træningsdata

Disse egenskaber gør det muligt for Llama 3.1 at håndtere mere komplekse brugssituationer ved opbygning af GenAI-applikationer, herunder:
- Native Function Calling - evnen til at kalde eksterne værktøjer og funktioner uden for LLM-arbejdsgangen
- Bedre RAG Ydeevne - på grund af det større kontekstvindue
- Syntetisk Datagenerering - evnen til at skabe effektiv data til opgaver som finjustering

### Native Function Calling

Llama 3.1 er finjusteret for bedre at kunne foretage funktions- eller værktøjskald. Den har også to indbyggede værktøjer, som modellen kan identificere behovet for at bruge baseret på brugerens prompt. Disse værktøjer er:

- **Brave Search** - Kan bruges til at få opdaterede oplysninger som vejret ved at lave en websøgeforespørgsel
- **Wolfram Alpha** - Kan bruges til mere komplekse matematiske beregninger, så det ikke er nødvendigt at skrive egne funktioner.

Du kan også oprette dine egne brugerdefinerede værktøjer, som LLM kan kalde.

I kodeeksemplet nedenfor:

- Definerer vi de tilgængelige værktøjer (brave_search, wolfram_alpha) i systemprompten.
- Sender en brugerprompt, som spørger om vejret i en bestemt by.
- LLM vil svare med et værktøjskald til Brave Search-værktøjet, som vil se sådan ud `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Bemærk: Dette eksempel foretager kun værktøjskaldet, hvis du vil have resultaterne, skal du oprette en gratis konto på Brave API-siden og definere funktionen selv.

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

Selvom det er en LLM, er en begrænsning ved Llama 3.1 dets mangel på multimodalitet. Det vil sige manglende evne til at bruge forskellige inputtyper som billeder som prompts og give svar. Denne evne er en af hovedfunktionerne i Llama 3.2. Disse funktioner inkluderer også:

- Multimodalitet - har evnen til at evaluere både tekst- og billedprompter
- Små til mellemstore variationer (11B og 90B) - giver fleksible implementeringsmuligheder
- Tekst-only variationer (1B og 3B) - gør det muligt at implementere modellen på edge / mobile enheder og giver lav latenstid

Den multimodale understøttelse repræsenterer et stort skridt i open source modellernes verden. Kodeeksemplet nedenfor tager både et billede og en tekstprompt for at få en analyse af billedet fra Llama 3.2 90B.

### Multimodal Support med Llama 3.2

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

Efter at have gennemført denne lektion, tag et kig på vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at forbedre din Generative AI-viden!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->