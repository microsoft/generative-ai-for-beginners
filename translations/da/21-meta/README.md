# Bygning Med Meta Familie Modellerne 

## Introduktion 

Denne lektion vil dække: 

- Udforskning af de to hoved Meta familie modeller - Llama 3.1 og Llama 3.2 
- Forståelse af anvendelsestilfælde og scenarier for hver model 
- Kodestykke der viser de unikke funktioner i hver model 


## Meta Familien af Modeller 

I denne lektion vil vi udforske 2 modeller fra Meta familien eller "Llama-flokken" - Llama 3.1 og Llama 3.2.

Disse modeller findes i forskellige varianter og er tilgængelige i [Microsoft Foundry Models kataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Bemærk:** GitHub Models pensioneres ved slutningen af juli 2026. Her er flere detaljer om brugen af [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) til at prototypere med AI-modeller.

Modelvarianter: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Bemærk: Llama 3 er også tilgængelig i Microsoft Foundry Models, men vil ikke blive dækket i denne lektion*

## Llama 3.1 

Ved 405 milliarder parametre passer Llama 3.1 ind i kategorien åbne kildesprogmodeller (LLM). 

Modellen er en opgradering af den tidligere version Llama 3 ved at tilbyde: 

- Større kontekstvindue - 128k tokens mod 8k tokens 
- Større Maksimum Output Tokens - 4096 mod 2048 
- Bedre flersproget understøttelse - på grund af øget antal træningstokens 

Disse giver Llama 3.1 mulighed for at håndtere mere komplekse anvendelsestilfælde ved opbygning af GenAI applikationer, herunder: 
- Indbygget Funktionskald - evnen til at kalde eksterne værktøjer og funktioner uden for LLM-arbejdsgangen
- Bedre RAG-ydelse - på grund af det større kontekstvindue 
- Syntetisk Datagenerering - evnen til at skabe effektiv data til opgaver som finjustering 

### Indbygget Funktionskald 

Llama 3.1 er finjusteret til at være mere effektiv til at lave funktions- eller værktøjskald. Den har også to indbyggede værktøjer, som modellen kan identificere som nødvendige at bruge baseret på brugerens prompt. Disse værktøjer er: 

- **Brave Search** - Kan bruges til at få opdaterede informationer som vejret ved at udføre et web-søgning 
- **Wolfram Alpha** - Kan bruges til mere komplekse matematiske beregninger, så det ikke er nødvendigt at skrive egne funktioner. 

Du kan også oprette dine egne brugerdefinerede værktøjer, som LLM kan kalde. 

I kodeeksemplet nedenfor: 

- Definerer vi de tilgængelige værktøjer (brave_search, wolfram_alpha) i systemprompten. 
- Sender en brugerprompt, der spørger om vejret i en bestemt by. 
- LLM vil svare med et værktøjskald til Brave Search-værktøjet, som vil se sådan ud `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Bemærk: Dette eksempel foretager kun værktøjskaldet; hvis du vil have resultaterne, skal du oprette en gratis konto på Brave API-siden og definere funktionen selv.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Få disse fra din Microsoft Foundry-projekts "Oversigt" side
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

Selvom det er en LLM, er en begrænsning ved Llama 3.1 dens mangel på multimodalitet. Det vil sige, manglende evne til at bruge forskellige typer input såsom billeder som prompts og give svar. Denne evne er en af hovedfunktionerne i Llama 3.2. Disse funktioner omfatter også: 

- Multimodalitet - har evnen til at evaluere både tekst- og billedprompter 
- Små til mellemstore størrelsesvariationer (11B og 90B) - hvilket giver fleksible muligheder for udrulning, 
- Tekst-only variationer (1B og 3B) - dette tillader modellen at blive udrullet på edge/mobilenheder og giver lav latenstid 

Den multimodale understøttelse repræsenterer et stort skridt i open source-modellernes verden. Kodeeksemplet nedenfor tager både et billede og en tekstprompt for at få en analyse af billedet fra Llama 3.2 90B. 


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

# Hent disse fra din Microsoft Foundry projekts "Oversigt" side
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

## Læringen stopper ikke her, fortsæt rejsen

Når du har fuldført denne lektion, så tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at øge din viden om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->