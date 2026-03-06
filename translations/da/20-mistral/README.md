# Bygning med Mistral-modeller

## Introduktion

Denne lektion dækker:
- Udforskning af de forskellige Mistral-modeller
- Forståelse af brugsscenarier og situationer for hver model
- Udforskning af kodeeksempler, der viser de unikke funktioner ved hver model.

## Mistral-modellerne

I denne lektion vil vi udforske 3 forskellige Mistral-modeller:
**Mistral Large**, **Mistral Small** og **Mistral Nemo**.

Hver af disse modeller er tilgængelige gratis på GitHub Model Marketplace. Koden i denne notesbog vil bruge disse modeller til at køre koden. Her er flere oplysninger om brugen af GitHub Models til at [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 er i øjeblikket Mistrals flagskibsmodel og er designet til virksomhedsanvendelse.

Modellen er en opgradering af den oprindelige Mistral Large ved at tilbyde
- Større kontekstvindue - 128k vs 32k
- Bedre ydeevne på matematik- og kodningsopgaver - 76,9 % gennemsnitlig nøjagtighed vs 60,4 %
- Øget flersproget ydeevne - sprog inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, hollandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funktioner udmærker Mistral Large sig ved
- *Retrieval Augmented Generation (RAG)* - på grund af det større kontekstvindue
- *Funktionkald* - denne model har indbygget funktionkald, som muliggør integration med eksterne værktøjer og API’er. Disse kald kan foretages både parallelt eller én efter én i rækkefølge.
- *Kodegenerering* - denne model udmærker sig i Python-, Java-, TypeScript- og C++-generering.

### RAG-eksempel med Mistral Large 2

I dette eksempel bruger vi Mistral Large 2 til at køre et RAG-mønster over et tekst dokument. Spørgsmålet er skrevet på koreansk og spørger om forfatterens aktiviteter før college.

Den bruger Cohere Embeddings Model til at skabe embeddings af tekst dokumentet samt spørgsmålet. Til dette eksempel anvendes faiss Python-pakken som en vektorbutik.

Prompten, der sendes til Mistral-modellen, indeholder både spørgsmålene og de hentede tekststykker, der ligner spørgsmålet. Modellen giver derefter et naturligt sprogsvar.

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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
Mistral Small er en anden model i Mistral-familien under premium/enterprise-kategorien. Som navnet antyder, er denne model en Small Language Model (SLM). Fordelene ved at bruge Mistral Small er, at den er:
- Omkostningsbesparende sammenlignet med Mistral LLM’er som Mistral Large og NeMo - 80 % prisnedgang
- Lav latency - hurtigere svar sammenlignet med Mistral’s LLM’er
- Fleksibel - kan implementeres på forskellige miljøer med færre begrænsninger på krævede ressourcer.

Mistral Small er god til:
- Tekstbaserede opgaver såsom opsummering, sentimentanalyse og oversættelse.
- Applikationer, hvor der fremsendes hyppige forespørgsler på grund af dens omkostningseffektivitet
- Lav-latency kodeopgaver som gennemgang og kodningsforslag

## Sammenligning af Mistral Small og Mistral Large

For at vise forskelle i latency mellem Mistral Small og Large, kør cellerne nedenfor.

Du bør kunne se en forskel i svartider på 3-5 sekunder. Bemærk også svarlængderne og stilen over samme prompt.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

Sammenlignet med de to andre modeller, der er diskuteret i denne lektion, er Mistral NeMo den eneste gratis model med en Apache2-licens.

Den ses som en opgradering af den tidligere open source LLM fra Mistral, Mistral 7B.

Nogle andre funktioner ved NeMo-modellen er:

- *Mere effektiv tokenisering:* Denne model bruger Tekken-tokenizeren frem for den mere almindeligt anvendte tiktoken. Dette muliggør bedre ydeevne på flere sprog og kode.

- *Finjustering:* Basismodellen er tilgængelig for finjustering. Dette giver mere fleksibilitet til brugsscenarier, hvor finjustering kan være nødvendig.

- *Indbygget funktionkald* - Ligesom Mistral Large er denne model trænet i funktionkald. Det gør den unik som en af de første open source-modeller til det.

### Sammenligning af tokenizere

I dette eksempel vil vi se på, hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large.

Begge eksempler tager samme prompt, men du bør kunne se, at NeMo returnerer færre tokens end Mistral Large.

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

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at øge din viden om Generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->