<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:18:34+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "no"
}
-->
# Bygge med Mistral-modeller

## Introduksjon

Denne leksjonen vil dekke:
- Utforske de forskjellige Mistral-modellene
- Forstå bruksområder og scenarier for hver modell
- Kodeeksempler viser de unike funksjonene til hver modell.

## Mistral-modellene

I denne leksjonen vil vi utforske 3 forskjellige Mistral-modeller: **Mistral Large**, **Mistral Small** og **Mistral Nemo**.

Hver av disse modellene er tilgjengelig gratis på Github Model-markedsplassen. Koden i denne notatboken vil bruke disse modellene til å kjøre koden. Her er mer informasjon om hvordan du bruker Github Models til å [lage prototyper med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 er for øyeblikket flaggskipmodellen fra Mistral og er designet for bedriftsbruk.

Modellen er en oppgradering av den opprinnelige Mistral Large ved å tilby
- Større kontekstvindu - 128k vs 32k
- Bedre ytelse på matte- og kodingsoppgaver - 76,9 % gjennomsnittlig nøyaktighet vs 60,4 %
- Økt flerspråklig ytelse - språk inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, nederlandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funksjonene utmerker Mistral Large seg på
- *Retrieval Augmented Generation (RAG)* - på grunn av det større kontekstvinduet
- *Funksjonskalling* - denne modellen har innebygd funksjonskalling som tillater integrasjon med eksterne verktøy og APIer. Disse kallene kan gjøres både parallelt eller en etter en i sekvensiell rekkefølge.
- *Kodegenerering* - denne modellen utmerker seg på generering av Python, Java, TypeScript og C++.

### RAG-eksempel med Mistral Large 2

I dette eksempelet bruker vi Mistral Large 2 til å kjøre et RAG-mønster over et tekstdokument. Spørsmålet er skrevet på koreansk og spør om forfatterens aktiviteter før college.

Det bruker Cohere Embeddings Model til å lage embeddings av tekstdokumentet samt spørsmålet. For dette eksempelet bruker det faiss Python-pakken som en vektorbutikk.

Prompten sendt til Mistral-modellen inkluderer både spørsmålene og de gjenfunnede delene som er lik spørsmålet. Modellen gir deretter et naturlig språkrespons.

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

Mistral Small er en annen modell i Mistral-familien av modeller under premier/enterprise-kategorien. Som navnet antyder, er denne modellen en Small Language Model (SLM). Fordelene med å bruke Mistral Small er at den er:
- Kostnadsbesparende sammenlignet med Mistral LLMs som Mistral Large og NeMo - 80 % prisnedgang
- Lav ventetid - raskere respons sammenlignet med Mistrals LLMs
- Fleksibel - kan distribueres på tvers av forskjellige miljøer med færre begrensninger på nødvendige ressurser.

Mistral Small er flott for:
- Tekstbaserte oppgaver som oppsummering, sentimentanalyse og oversettelse.
- Applikasjoner der hyppige forespørsler gjøres på grunn av sin kostnadseffektivitet
- Lav ventetid kodeoppgaver som gjennomgang og kodeforslag

## Sammenligning av Mistral Small og Mistral Large

For å vise forskjeller i ventetid mellom Mistral Small og Large, kjør cellene nedenfor.

Du bør se en forskjell i responstider mellom 3-5 sekunder. Merk også responslengder og stil over samme prompt.

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

Sammenlignet med de to andre modellene diskutert i denne leksjonen, er Mistral NeMo den eneste gratis modellen med en Apache2-lisens.

Den anses som en oppgradering til den tidligere open source LLM fra Mistral, Mistral 7B.

Noen andre funksjoner ved NeMo-modellen er:

- *Mer effektiv tokenisering:* Denne modellen bruker Tekken-tokenizer over den mer vanlig brukte tiktoken. Dette gir bedre ytelse over flere språk og kode.

- *Finjustering:* Basismodellen er tilgjengelig for finjustering. Dette gir mer fleksibilitet for bruksområder der finjustering kan være nødvendig.

- *Innebygd funksjonskalling* - Som Mistral Large, er denne modellen trent på funksjonskalling. Dette gjør den unik som en av de første open source-modellene til å gjøre det.

### Sammenligning av tokenizers

I dette eksempelet vil vi se på hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large.

Begge eksemplene tar den samme prompten, men du bør se at NeMo returnerer færre tokens sammenlignet med Mistral Large.

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

## Læring stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å forbedre din kunnskap om generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi etterstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.