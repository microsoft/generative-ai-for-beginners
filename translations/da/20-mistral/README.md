<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:00:47+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "da"
}
-->
# Bygning med Mistral-modeller

## Introduktion

Denne lektion vil dække:  
- Gennemgang af de forskellige Mistral-modeller  
- Forståelse af brugsscenarier for hver model  
- Kodeeksempler, der viser de unikke funktioner ved hver model.

## Mistral-modellerne

I denne lektion vil vi udforske 3 forskellige Mistral-modeller:  
**Mistral Large**, **Mistral Small** og **Mistral Nemo**.

Hver af disse modeller er tilgængelige gratis på Github Model marketplace. Koden i denne notesbog vil bruge disse modeller til at køre koden. Her er flere detaljer om brugen af Github Models til at [prototype med AI-modeller](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 er i øjeblikket Mistrals flagskibsmodel og er designet til erhvervsbrug.

Modellen er en opgradering af den oprindelige Mistral Large og tilbyder  
- Større kontekstvindue - 128k vs 32k  
- Bedre præstation på matematik- og kodningsopgaver - 76,9% gennemsnitlig nøjagtighed vs 60,4%  
- Forbedret flersproget ydeevne - sprog inkluderer: engelsk, fransk, tysk, spansk, italiensk, portugisisk, hollandsk, russisk, kinesisk, japansk, koreansk, arabisk og hindi.

Med disse funktioner excellerer Mistral Large i  
- *Retrieval Augmented Generation (RAG)* - takket være det større kontekstvindue  
- *Function Calling* - denne model har indbygget funktionel opkald, som muliggør integration med eksterne værktøjer og API’er. Disse opkald kan foretages både parallelt eller sekventielt.  
- *Kodegenerering* - modellen er særligt god til generering af Python, Java, TypeScript og C++.

### RAG-eksempel med Mistral Large 2

I dette eksempel bruger vi Mistral Large 2 til at køre et RAG-mønster over et tekst dokument. Spørgsmålet er skrevet på koreansk og handler om forfatterens aktiviteter før college.

Den bruger Cohere Embeddings Model til at skabe embeddings af både tekst dokumentet og spørgsmålet. Til dette eksempel anvendes faiss Python-pakken som vektorlager.

Prompten, der sendes til Mistral-modellen, inkluderer både spørgsmålene og de hentede tekststykker, der ligner spørgsmålet. Modellen leverer derefter et svar i naturligt sprog.

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
Mistral Small er en anden model i Mistral-familien under premier/enterprise-kategorien. Som navnet antyder, er det en Small Language Model (SLM). Fordelene ved at bruge Mistral Small er, at den er:  
- Omkostningseffektiv sammenlignet med Mistral LLM’er som Mistral Large og NeMo - 80% prisreduktion  
- Lav latenstid - hurtigere respons sammenlignet med Mistrals LLM’er  
- Fleksibel - kan implementeres i forskellige miljøer med færre krav til ressourcer.

Mistral Small er ideel til:  
- Tekstbaserede opgaver som opsummering, sentimentanalyse og oversættelse.  
- Applikationer med hyppige forespørgsler på grund af dens omkostningseffektivitet  
- Lav latenstid ved kodeopgaver som gennemgang og kodeforslag

## Sammenligning af Mistral Small og Mistral Large

For at vise forskelle i latenstid mellem Mistral Small og Large, kør nedenstående celler.

Du vil kunne se en forskel i svartider på 3-5 sekunder. Bemærk også svarenes længde og stil på samme prompt.

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

Sammenlignet med de to andre modeller i denne lektion, er Mistral NeMo den eneste gratis model med en Apache2-licens.

Den betragtes som en opgradering af den tidligere open source LLM fra Mistral, Mistral 7B.

Nogle andre funktioner ved NeMo-modellen er:

- *Mere effektiv tokenisering:* Denne model bruger Tekken-tokenizeren i stedet for den mere almindelige tiktoken. Det giver bedre ydeevne på flere sprog og kode.

- *Finetuning:* Basismodellen er tilgængelig til finetuning, hvilket giver større fleksibilitet til brugsscenarier, hvor finetuning er nødvendigt.

- *Native Function Calling* - Ligesom Mistral Large er denne model trænet til funktionelle opkald. Det gør den unik som en af de første open source-modeller med denne funktion.

### Sammenligning af tokenizere

I dette eksempel ser vi på, hvordan Mistral NeMo håndterer tokenisering sammenlignet med Mistral Large.

Begge eksempler bruger samme prompt, men du vil kunne se, at NeMo returnerer færre tokens end Mistral Large.

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

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at udvikle din viden om Generativ AI!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.