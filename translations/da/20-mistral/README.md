# Bygning med Mistral-modeller 

## Introduktion 

Denne lektion vil dække: 
- Udforskning af de forskellige Mistral-modeller 
- Forståelse af anvendelsestilfælde og scenarier for hver model 
- Udforskning af kodeeksempler, der viser de unikke egenskaber ved hver model. 

## Mistral-modellerne 

I denne lektion vil vi udforske 3 forskellige Mistral-modeller: 
**Mistral Large**, **Mistral Small** og **Mistral Nemo**. 

Hver af disse modeller er tilgængelige gratis på [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Koden i denne notesbog vil bruge disse modeller til at køre koden.

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. Her er flere detaljer om brug af [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) til at prototype med AI-modeller. 


## Mistral Large 2 (2407)
Mistral Large 2 er i øjeblikket flagskibsmodellen fra Mistral og er designet til erhvervsbrug. 

Modellen er en opgradering af den oprindelige Mistral Large ved at tilbyde 
- Større kontekstvindue - 128k vs 32k 
- Bedre ydeevne på matematik- og kodningsopgaver - 76,9% gennemsnitlig nøjagtighed vs 60,4% 
- Øget flersproget ydeevne - sprog inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, hollandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funktioner excellerer Mistral Large i 
- *Retrieval Augmented Generation (RAG)* - på grund af det større kontekstvindue
- *Funktionsopkald* - denne model har indbygget funktionsopkald, som tillader integration med eksterne værktøjer og API'er. Disse opkald kan foretages både parallelt eller sekventielt i rækkefølge. 
- *Kodegenerering* - denne model excellerer i generering af Python, Java, TypeScript og C++. 

### RAG-eksempel med Mistral Large 2 

I dette eksempel bruger vi Mistral Large 2 til at køre et RAG-mønster over et tekstdokument. Spørgsmålet er skrevet på koreansk og handler om forfatterens aktiviteter før college. 

Det bruger Cohere Embeddings Model til at skabe indlejring af tekstdokumentet samt spørgsmålet. Til dette eksempel bruges faiss Python-pakken som en vektorlager. 

Prompet sendt til Mistral-modellen inkluderer både spørgsmålene og de hentede klumper, der ligner spørgsmålet. Modellen giver derefter et natur-sprogs svar. 

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

# Få disse fra din Microsoft Foundry-projekts "Oversigt" side
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # afstand, indeks
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small 
Mistral Small er en anden model i Mistral-familien under premier/erhvervskategorien. Som navnet antyder, er denne model en lille sprogmodel (SLM). Fordelene ved at bruge Mistral Small er, at den er: 
- Omkostningsbesparende sammenlignet med Mistral LLM'er som Mistral Large og NeMo - 80% prisfald
- Lav latenstid - hurtigere responstid sammenlignet med mistrals LLM'er
- Fleksibel - kan implementeres på forskellige miljøer med færre begrænsninger på nødvendige ressourcer. 


Mistral Small er fremragende til: 
- Tekstbaserede opgaver såsom opsummering, sentimentanalyse og oversættelse. 
- Applikationer hvor hyppige forespørgsler foretages på grund af den omkostningseffektivitet 
- Lav latenstid kodeopgaver som gennemgang og kodesuggestioner 

## Sammenligning af Mistral Small og Mistral Large 

For at vise forskelle i latenstid mellem Mistral Small og Large, kør nedenstående celler. 

Du bør se en forskel i svartider på 3-5 sekunder. Bemærk også svarlængder og stil over det samme prompt.  

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

Sammenlignet med de to andre modeller diskuteret i denne lektion, er Mistral NeMo den eneste gratis model med en Apache2-licens. 

Det betragtes som en opgradering af den tidligere open source LLM fra Mistral, Mistral 7B. 

Nogle andre funktioner ved NeMo-modellen er: 

- *Mere effektiv tokenisering:* Denne model bruger Tekken-tokenizeren i stedet for den mere almindeligt anvendte tiktoken. Dette giver bedre ydeevne over flere sprog og kode. 

- *Finjustering:* Basismodellen er tilgængelig for finjustering. Dette giver større fleksibilitet til anvendelsestilfælde, hvor finjustering kan være nødvendig. 

- *Indbygget funktionsopkald* - Som Mistral Large er denne model trænet til funktionsopkald. Dette gør den unik som en af de første open source modeller til at gøre det. 


### Sammenligning af tokenizerere 

I dette eksempel vil vi se på, hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large. 

Begge eksempler tager det samme prompt, men du bør se, at NeMo returnerer færre tokens end Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importer nødvendige pakker:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Indlæs Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser en liste af beskeder
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Tæl antallet af tokens
print(len(tokens))
```

```python
# Importer nødvendige pakker:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Indlæs Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser en liste af beskeder
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Tæl antallet af tokens
print(len(tokens))
```

## Læringen stopper ikke her, fortsæt rejsen

Efter at have gennemført denne lektion, tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->