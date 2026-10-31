# Bygning med Meta-familie modellerne 

## Introduktion 

Denne lektion vil dække: 

- Udforskning af de to hovedmodeller i Meta-familien - Llama 3.1 og Llama 3.2, samt de nuværende tilgængelige alternativer brugt i kodeeksemplerne (Llama 3.3 og Llama 4) 
- Forståelse af anvendelsestilfælde og scenarier for hver model 
- Kodeeksempel for at vise de unikke funktioner i hver model 


## Meta-familien af modeller 

I denne lektion vil vi udforske 2 modeller fra Meta-familien eller "Llama Herd" - Llama 3.1 og Llama 3.2. De kørbare kodeeksempler bruger Llama 3.3 og Llama 4, som i øjeblikket er tilgængelige alternativer i Microsoft Foundry Models-kataloget.

Disse modeller kommer i forskellige varianter og er tilgængelige i [Microsoft Foundry Models kataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Note:** GitHub Models udfases ved slutningen af juli 2026. Her er flere detaljer om brugen af [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) til prototyping med AI-modeller.

> **Bemærk:** De specifikke modelversioner, som denne lektion oprindeligt blev skrevet imod (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), er siden blevet udfaset fra Microsoft Foundry Models-kataloget. Kodeeksemplerne nedenfor bruger `Llama-3.3-70B-Instruct` og `Llama-4-Scout-17B-16E-Instruct` som nu tilgængelige alternativer i Microsoft Foundry Models-kataloget, så de stadig kan køre i dag.

Modelvarianter (som oprindeligt dækket i denne lektion): 
- Llama 3.1 - 70B Instruktionsmodel (udgået) 
- Llama 3.1 - 405B Instruktionsmodel (udgået) 
- Llama 3.2 - 11B Vision Instruktionsmodel (udgået) 
- Llama 3.2 - 90B Vision Instruktionsmodel (udgået) 

Nuværende tilgængelige alternativer brugt i kodeeksemplerne: 
- Llama 3.3 - 70B Instrukt (`Llama-3.3-70B-Instruct`) 
- Llama 4 Spejder - 17B 16E Instrukt (`Llama-4-Scout-17B-16E-Instruct`) 

*Note: De ovennævnte Llama 3-varianter bevares til historisk kontekst og er ikke længere tilgængelige i Microsoft Foundry Models.*

## Llama 3.1 

Med 405 milliarder parametre hører Llama 3.1 til kategorien af open source LLM'er. 

Modellen er en opgradering fra den tidligere udgivelse Llama 3 ved at tilbyde: 

- Større kontekstvindue - 128k tokens vs 8k tokens 
- Større maks output tokens - 4096 vs 2048 
- Bedre flersproget support - på grund af flere træningstokens 

Disse gør det muligt for Llama 3.1 at håndtere mere komplekse anvendelsesscenarier ved opbygning af GenAI-applikationer inklusive: 
- Indbygget funktion opkald - evnen til at kalde eksterne værktøjer og funktioner uden for LLM-arbejdsgangen
- Bedre RAG-ydeevne - på grund af det større kontekstvindue 
- Syntetisk datagenerering - evnen til at skabe effektiv data til opgaver som finjustering 

### Indbygget funktion opkald 

Llama 3.1 er finjusteret til at være mere effektiv til funktion- eller værktøjsopkald. Den har også to indbyggede værktøjer, som modellen kan identificere som nødvendige at bruge baseret på brugerens prompt. Disse værktøjer er: 

- **Brave Search** - Kan bruges til at få opdaterede oplysninger som vejret via et web-søgning 
- **Wolfram Alpha** - Kan bruges til mere komplekse matematiske beregninger, så det ikke er nødvendigt at skrive egne funktioner. 

Du kan også skabe dine egne brugerdefinerede værktøjer, som LLM kan kalde. 

I kodeeksemplet nedenfor: 

- Definerer vi de tilgængelige værktøjer (brave_search, wolfram_alpha) i systemprompten. 
- Sender et brugerprompt, som spørger om vejret i en bestemt by. 
- LLM vil svare med et værktøjsopkald til Brave Search-værktøjet, som vil se sådan ud `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: Dette eksempel foretager kun værktøjsopkaldet, hvis du ønsker at få resultaterne, skal du oprette en gratis konto på Brave API-siden og definere funktionen selv.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Selvom den er en LLM, er en begrænsning ved Llama 3.1 dens manglende multimodalitet. Det vil sige evnen til at bruge forskellige typer input som billeder som prompt og give svar. Denne evne er en af hovedfunktionerne i Llama 3.2. Andre funktioner inkluderer: 

- Multimodalitet - har evnen til at evaluere både tekst- og billed frembringelser 
- Små til mellemstore varianter (11B og 90B) - hvilket giver fleksible udrulningsmuligheder 
- Tekst-only varianter (1B og 3B) - giver mulighed for udrulning på edge / mobile enheder og giver lav latenstid 

Den multimodale support repræsenterer et stort skridt i verdenen af open source-modeller. kodeeksemplet nedenfor tager både et billede og en tekstprompt for at få en analyse af billedet. Fordi Llama 3.2 90B Vision Instruct er blevet pensioneret, bruger eksemplet `Llama-4-Scout-17B-16E-Instruct`, et aktuelt tilgængeligt native multimodalt alternativ. 


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

Efter at have gennemført denne lektion, så tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at øge din viden om Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->