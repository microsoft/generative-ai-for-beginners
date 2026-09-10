# Bygging med Mistral-modeller 

## Introduksjon 

Denne leksjonen vil dekke: 
- Utforsking av de forskjellige Mistral-modellene 
- Forstå brukstilfeller og scenarier for hver modell 
- Utforsking av kodeeksempler som viser de unike funksjonene til hver modell. 

## Mistral-modellene 

I denne leksjonen vil vi utforske 3 forskjellige Mistral-modeller: 
**Mistral Large**, **Mistral Small** og **Mistral Nemo**. 

Hver av disse modellene er tilgjengelig gratis på [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Koden i denne notatboken vil bruke disse modellene til å kjøre koden.

> **Merk:** GitHub Models fases ut ved slutten av juli 2026. Her er mer informasjon om hvordan man bruker [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) for å prototype med AI-modeller. 


## Mistral Large 2 (2407)
Mistral Large 2 er for tiden flaggskipmodellen fra Mistral og er designet for bedriftsbruk. 

Modellen er en oppgradering av den originale Mistral Large ved å tilby 
-  Større kontekstvindu - 128k mot 32k 
-  Bedre ytelse på matematikk- og kodeoppgaver - 76,9 % gjennomsnittlig nøyaktighet mot 60,4 % 
-  Økt flerspråklig ytelse - språk inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, nederlandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funksjonene utmerker Mistral Large seg innen 
- *Retrieval Augmented Generation (RAG)* - på grunn av det større kontekstvinduet
- *Funksjonskalling* - denne modellen har innfødt funksjonskalling som tillater integrasjon med eksterne verktøy og API-er. Disse kallene kan gjøres både parallelt eller etter hverandre i sekvensiell rekkefølge. 
- *Kodegenerering* - denne modellen utmerker seg på generering av Python, Java, TypeScript og C++. 

### RAG-eksempel med Mistral Large 2 

I dette eksemplet bruker vi Mistral Large 2 for å kjøre et RAG-mønster over et tekstdokument. Spørsmålet er skrevet på koreansk og handler om forfatterens aktiviteter før universitetet. 

Den bruker Cohere Embeddings Model for å lage embeddings av tekstdokumentet samt spørsmålet. For dette eksempelet bruker den Python-pakken faiss som en vektorlagring. 

Prompten som sendes til Mistral-modellen inkluderer både spørsmålene og de hentede delene som ligner på spørsmålet. Modellen gir deretter et naturlig språk-svar. 

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

# Hent disse fra "Oversikt"-siden i Microsoft Foundry-prosjektet ditt
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # avstand, indeks
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
Mistral Small er en annen modell i Mistral-familien under premier/bedriftskategorien. Som navnet tilsier, er dette en liten språkmodell (SLM). Fordelene med å bruke Mistral Small er at den er: 
- Kostnadsbesparende sammenlignet med Mistral LLM-er som Mistral Large og NeMo - 80 % prisreduksjon
- Lav ventetid - raskere respons sammenlignet med Mistral sine LLM-er
- Fleksibel - kan distribueres i forskjellige miljøer med færre restriksjoner på nødvendige ressurser. 


Mistral Small er flott for: 
- Tekstbaserte oppgaver som oppsummering, sentimentanalyse og oversettelse. 
- Applikasjoner hvor det gjøres hyppige forespørsler på grunn av kostnadseffektivitet 
- Kodeoppgaver med lav ventetid som gjennomgang og kodeforslag 

## Sammenligning av Mistral Small og Mistral Large 

For å vise forskjeller i ventetid mellom Mistral Small og Large, kjør cellene nedenfor. 

Du bør se en forskjell i responstider på 3–5 sekunder. Merk også responslengdene og stilen over samme prompt.  

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

Sammenlignet med de to andre modellene som omtales i denne leksjonen, er Mistral NeMo den eneste gratismodellen med en Apache2-lisens. 

Den sees på som en oppgradering av den tidligere åpen kildekode-LLM fra Mistral, Mistral 7B. 

Noen andre funksjoner ved NeMo-modellen er: 

- *Mer effektiv tokenisering:* Denne modellen bruker Tekken-tokenizer i stedet for den mer vanlige tiktoken. Dette gir bedre ytelse over flere språk og kode. 

- *Finjustering:* Basismodellen er tilgjengelig for finjustering. Dette gir mer fleksibilitet for brukstilfeller der finjustering kan være nødvendig. 

- *Innfødt funksjonskalling* - Som Mistral Large er denne modellen trent på funksjonskalling. Dette gjør den unik som en av de første åpen kildekode-modellene som gjør dette. 


### Sammenligning av tokenizere 

I dette eksemplet ser vi på hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large. 

Begge eksempler tar samme prompt, men du bør se at NeMo returnerer færre tokens enn Mistral Large. 

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

# Last inn Mistral-tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser en liste med meldinger
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

# Tell antall tokens
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

# Last inn Mistral-tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniser en liste med meldinger
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

# Tell antall tokens
print(len(tokens))
```

## Læringen stopper ikke her, fortsett reisen

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve din kunnskap om generativ AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->