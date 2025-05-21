<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:02:55+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ro"
}
-->
# Construirea cu Modelele Mistral

## Introducere

Această lecție va acoperi:
- Explorarea diferitelor modele Mistral
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model
- Exemple de cod care arată caracteristicile unice ale fiecărui model.

## Modelele Mistral

În această lecție, vom explora 3 modele Mistral diferite: **Mistral Large**, **Mistral Small** și **Mistral Nemo**.

Fiecare dintre aceste modele este disponibil gratuit pe piața de modele Github. Codul din acest notebook va folosi aceste modele pentru a rula codul. Iată mai multe detalii despre utilizarea modelelor Github pentru [prototiparea cu modele AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 este în prezent modelul de vârf de la Mistral și este conceput pentru utilizarea în întreprinderi.

Modelul este o actualizare la Mistral Large original, oferind:
- Fereastră de context mai mare - 128k vs 32k
- Performanță mai bună la sarcini de matematică și codare - acuratețe medie de 76.9% vs 60.4%
- Performanță multilingvistică crescută - limbile includ: engleză, franceză, germană, spaniolă, italiană, portugheză, olandeză, rusă, chineză, japoneză, coreeană, arabă și hindi.

Cu aceste caracteristici, Mistral Large excelează la:
- *Generarea augmentată prin recuperare (RAG)* - datorită ferestrei de context mai mari
- *Apelarea funcțiilor* - acest model are apelarea funcțiilor nativă, care permite integrarea cu instrumente externe și API-uri. Aceste apeluri pot fi făcute atât în paralel, cât și una după alta, într-o ordine secvențială.
- *Generarea de cod* - acest model excelează la generarea de cod în Python, Java, TypeScript și C++.

### Exemplu RAG folosind Mistral Large 2

În acest exemplu, folosim Mistral Large 2 pentru a rula un model RAG pe un document text. Întrebarea este scrisă în coreeană și întreabă despre activitățile autorului înainte de facultate.

Folosește Modelul de Încapsulare Cohere pentru a crea încapsulări ale documentului text precum și ale întrebării. Pentru acest exemplu, folosește pachetul Python faiss ca magazin de vectori.

Promptul trimis modelului Mistral include atât întrebările, cât și fragmentele recuperate care sunt similare cu întrebarea. Modelul oferă apoi un răspuns în limbaj natural.

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
Mistral Small este un alt model din familia de modele Mistral din categoria premier/enterprise. După cum sugerează și numele, acest model este un Small Language Model (SLM). Avantajele utilizării Mistral Small sunt că este:
- Economisire de costuri comparativ cu LLM-urile Mistral, cum ar fi Mistral Large și NeMo - reducere de preț de 80%
- Latență redusă - răspuns mai rapid comparativ cu LLM-urile Mistral
- Flexibil - poate fi implementat în diferite medii cu mai puține restricții asupra resurselor necesare.

Mistral Small este ideal pentru:
- Sarcini bazate pe text, cum ar fi sumarizarea, analiza sentimentului și traducerea.
- Aplicații unde se fac cereri frecvente datorită eficienței sale de cost
- Sarcini de cod cu latență redusă, cum ar fi revizuirea și sugestiile de cod

## Compararea Mistral Small și Mistral Large

Pentru a arăta diferențele de latență între Mistral Small și Large, rulați celulele de mai jos.

Ar trebui să vedeți o diferență în timpii de răspuns între 3-5 secunde. De asemenea, notați lungimile și stilul răspunsurilor pentru același prompt.

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

Comparativ cu celelalte două modele discutate în această lecție, Mistral NeMo este singurul model gratuit cu licență Apache2.

Este văzut ca o actualizare la LLM-ul open source anterior de la Mistral, Mistral 7B.

Alte caracteristici ale modelului NeMo sunt:

- *Tokenizare mai eficientă:* Acest model folosește tokenizer-ul Tekken în locul celui mai frecvent utilizat tiktoken. Acest lucru permite o performanță mai bună în mai multe limbi și coduri.

- *Finisare:* Modelul de bază este disponibil pentru finisare. Acest lucru permite mai multă flexibilitate pentru cazurile de utilizare unde poate fi necesară finisarea.

- *Apelarea funcțiilor nativă* - La fel ca Mistral Large, acest model a fost antrenat pentru apelarea funcțiilor. Acest lucru îl face unic, fiind unul dintre primele modele open source care fac acest lucru.

### Compararea Tokenizatoarelor

În acest exemplu, vom analiza cum Mistral NeMo gestionează tokenizarea comparativ cu Mistral Large.

Ambele exemple folosesc același prompt, dar ar trebui să vedeți că NeMo returnează mai puțini tokeni față de Mistral Large.

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

## Învățarea nu se oprește aici, continuă călătoria

După ce ai terminat această lecție, verifică colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți dezvolți cunoștințele despre Generative AI!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.