<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:00:58+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "no"
}
-->
# Bygging med Mistral-modeller

## Introduksjon

Denne leksjonen vil dekke:  
- Utforske de forskjellige Mistral-modellene  
- Forstå bruksområder og scenarier for hver modell  
- Kodeeksempler som viser de unike funksjonene til hver modell.

## Mistral-modellene

I denne leksjonen skal vi utforske 3 forskjellige Mistral-modeller:  
**Mistral Large**, **Mistral Small** og **Mistral Nemo**.

Hver av disse modellene er tilgjengelige gratis på Github Model marketplace. Koden i denne notatboken vil bruke disse modellene for å kjøre koden. Her er mer informasjon om bruk av Github Models for å [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 er for øyeblikket flaggskipmodellen fra Mistral og er designet for bedriftsbruk.

Modellen er en oppgradering av den originale Mistral Large ved å tilby  
- Større kontekstvindu – 128k vs 32k  
- Bedre ytelse på matte- og kodeoppgaver – 76,9 % gjennomsnittlig nøyaktighet vs 60,4 %  
- Økt flerspråklig ytelse – språk inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, nederlandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funksjonene utmerker Mistral Large seg på  
- *Retrieval Augmented Generation (RAG)* – takket være det større kontekstvinduet  
- *Function Calling* – denne modellen har innebygd funksjonskalling som gjør det mulig å integrere med eksterne verktøy og API-er. Disse kallene kan gjøres både parallelt eller sekvensielt.  
- *Kodegenerering* – denne modellen er spesielt god på generering av Python, Java, TypeScript og C++.

### RAG-eksempel med Mistral Large 2

I dette eksempelet bruker vi Mistral Large 2 for å kjøre et RAG-mønster over et tekst-dokument. Spørsmålet er skrevet på koreansk og handler om forfatterens aktiviteter før college.

Det bruker Cohere Embeddings Model for å lage embeddings av tekst-dokumentet samt spørsmålet. For dette eksempelet brukes faiss Python-pakken som en vektor-lagring.

Prompten som sendes til Mistral-modellen inkluderer både spørsmålene og de hentede tekstbitene som ligner på spørsmålet. Modellen gir deretter et svar på naturlig språk.

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
Mistral Small er en annen modell i Mistral-familien under premier/enterprise-kategorien. Som navnet antyder, er dette en Small Language Model (SLM). Fordelene med å bruke Mistral Small er at den er:  
- Kostnadsbesparende sammenlignet med Mistral LLM-er som Mistral Large og NeMo – 80 % prisreduksjon  
- Lav ventetid – raskere respons sammenlignet med Mistral sine LLM-er  
- Fleksibel – kan distribueres i ulike miljøer med færre begrensninger på nødvendige ressurser.

Mistral Small passer godt til:  
- Tekstbaserte oppgaver som oppsummering, sentimentanalyse og oversettelse.  
- Applikasjoner med hyppige forespørsler på grunn av kostnadseffektiviteten  
- Kodeoppgaver med lav ventetid som gjennomgang og kodeforslag

## Sammenligning av Mistral Small og Mistral Large

For å vise forskjeller i ventetid mellom Mistral Small og Large, kjør cellene nedenfor.

Du bør se en forskjell i responstid på 3–5 sekunder. Legg også merke til forskjeller i responslengde og stil på samme prompt.

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

Sammenlignet med de to andre modellene som er diskutert i denne leksjonen, er Mistral NeMo den eneste gratismodellen med Apache2-lisens.

Den regnes som en oppgradering av den tidligere open source-LLM-en fra Mistral, Mistral 7B.

Noen andre funksjoner ved NeMo-modellen er:

- *Mer effektiv tokenisering:* Denne modellen bruker Tekken-tokenizer i stedet for den mer brukte tiktoken. Dette gir bedre ytelse på flere språk og kode.

- *Finjustering:* Basismodellen er tilgjengelig for finjustering. Dette gir større fleksibilitet for brukstilfeller hvor finjustering kan være nødvendig.

- *Native Function Calling* – Som Mistral Large er denne modellen trent på funksjonskalling. Dette gjør den unik som en av de første open source-modellene med denne funksjonaliteten.

### Sammenligning av tokenizere

I dette eksempelet ser vi på hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large.

Begge eksemplene bruker samme prompt, men du vil se at NeMo returnerer færre tokens enn Mistral Large.

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

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.