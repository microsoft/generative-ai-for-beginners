<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:58:32+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "da"
}
-->
# Byg med Mistral-modeller

## Introduktion

Denne lektion vil dække:
- Udforskning af de forskellige Mistral-modeller
- Forståelse af anvendelsesmuligheder og scenarier for hver model
- Kodeeksempler viser de unikke funktioner ved hver model.

## Mistral-modellerne

I denne lektion vil vi udforske 3 forskellige Mistral-modeller: **Mistral Large**, **Mistral Small** og **Mistral Nemo**.

Hver af disse modeller er tilgængelige gratis på Github Model-markedspladsen. Koden i denne notesbog vil bruge disse modeller til at køre koden. Her er flere detaljer om brug af Github-modeller til [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 er i øjeblikket den førende model fra Mistral og er designet til erhvervsbrug.

Modellen er en opgradering til den originale Mistral Large ved at tilbyde:
- Større kontekstvindue - 128k vs 32k
- Bedre ydeevne på matematik- og kodningsopgaver - 76,9% gennemsnitlig nøjagtighed vs 60,4%
- Øget flersproget ydeevne - sprog inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, hollandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funktioner udmærker Mistral Large sig ved:
- *Retrieval Augmented Generation (RAG)* - på grund af det større kontekstvindue
- *Funktionskald* - denne model har indbygget funktionskald, som tillader integration med eksterne værktøjer og API'er. Disse kald kan foretages både parallelt eller efter hinanden i en sekventiel rækkefølge.
- *Kodegenerering* - denne model udmærker sig i Python, Java, TypeScript og C++ generering.

### RAG Eksempel ved brug af Mistral Large 2

I dette eksempel bruger vi Mistral Large 2 til at køre et RAG-mønster over et tekst-dokument. Spørgsmålet er skrevet på koreansk og spørger om forfatterens aktiviteter før college.

Den bruger Cohere Embeddings Model til at skabe embeddings af tekst-dokumentet samt spørgsmålet. For dette eksempel bruger den faiss Python-pakken som en vektorlagring.

Prompten sendt til Mistral-modellen inkluderer både spørgsmålene og de hentede stykker, der ligner spørgsmålet. Modellen giver derefter et svar på naturligt sprog.

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Mistral Small er en anden model i Mistral-familien af modeller under premier/enterprise-kategorien. Som navnet antyder, er denne model en Small Language Model (SLM). Fordelene ved at bruge Mistral Small er, at den er:
- Omkostningsbesparende sammenlignet med Mistral LLMs som Mistral Large og NeMo - 80% prisfald
- Lav ventetid - hurtigere respons sammenlignet med Mistrals LLMs
- Fleksibel - kan implementeres på tværs af forskellige miljøer med færre begrænsninger på nødvendige ressourcer.

Mistral Small er fremragende til:
- Tekstbaserede opgaver som opsummering, sentimentanalyse og oversættelse.
- Applikationer hvor der laves hyppige forespørgsler på grund af dens omkostningseffektivitet
- Lav ventetids kodeopgaver som gennemgang og kodeforslag

## Sammenligning af Mistral Small og Mistral Large

For at vise forskelle i ventetid mellem Mistral Small og Large, kør nedenstående celler.

Du bør se en forskel i responstider mellem 3-5 sekunder. Bemærk også responslængder og stil over den samme prompt.

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

Den betragtes som en opgradering til den tidligere open source LLM fra Mistral, Mistral 7B.

Nogle andre funktioner ved NeMo-modellen er:

- *Mere effektiv tokenisering:* Denne model bruger Tekken-tokenizeren i stedet for den mere almindeligt brugte tiktoken. Dette tillader bedre ydeevne på flere sprog og kode.

- *Finjustering:* Basismodellen er tilgængelig til finjustering. Dette giver mere fleksibilitet til anvendelsesscenarier, hvor finjustering kan være nødvendig.

- *Indbygget funktionskald* - Ligesom Mistral Large er denne model blevet trænet på funktionskald. Dette gør den unik som en af de første open source-modeller til at gøre det.

### Sammenligning af tokenizere

I dette eksempel vil vi se på, hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large.

Begge eksempler tager den samme prompt, men du bør se, at NeMo returnerer færre tokens sammenlignet med Mistral Large.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## Læringen stopper ikke her, fortsæt rejsen

Efter at have gennemført denne lektion, tjek vores [Generativ AI Læringssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.