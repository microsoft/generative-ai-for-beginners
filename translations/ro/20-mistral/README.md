<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:03:39+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ro"
}
-->
# Construirea cu Modelele Mistral

## Introducere

Această lecție va acoperi:  
- Explorarea diferitelor modele Mistral  
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model  
- Exemple de cod care evidențiază caracteristicile unice ale fiecărui model.

## Modelele Mistral

În această lecție, vom explora 3 modele diferite Mistral:  
**Mistral Large**, **Mistral Small** și **Mistral Nemo**.

Fiecare dintre aceste modele este disponibil gratuit pe piața de modele Github. Codul din acest notebook va folosi aceste modele pentru a rula codul. Iată mai multe detalii despre utilizarea modelelor Github pentru [prototiparea cu modele AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 este în prezent modelul de top de la Mistral și este conceput pentru utilizare în mediul enterprise.

Modelul reprezintă un upgrade față de Mistral Large original, oferind:  
- Fereastră de context mai mare - 128k față de 32k  
- Performanțe mai bune la sarcini de matematică și programare - acuratețe medie de 76,9% față de 60,4%  
- Performanță multilingvă îmbunătățită - limbile incluse sunt: engleză, franceză, germană, spaniolă, italiană, portugheză, olandeză, rusă, chineză, japoneză, coreeană, arabă și hindi.

Cu aceste caracteristici, Mistral Large excelează la:  
- *Retrieval Augmented Generation (RAG)* - datorită ferestrei de context mai mari  
- *Function Calling* - acest model are apeluri native către funcții, permițând integrarea cu instrumente și API-uri externe. Aceste apeluri pot fi făcute atât în paralel, cât și secvențial, unul după altul.  
- *Generare de cod* - acest model excelează în generarea de cod Python, Java, TypeScript și C++.

### Exemplu RAG folosind Mistral Large 2

În acest exemplu, folosim Mistral Large 2 pentru a rula un pattern RAG pe un document text. Întrebarea este scrisă în coreeană și întreabă despre activitățile autorului înainte de facultate.

Se folosește modelul Cohere Embeddings pentru a crea embedding-uri ale documentului text, precum și ale întrebării. Pentru acest exemplu, se utilizează pachetul Python faiss ca vector store.

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
Mistral Small este un alt model din familia Mistral, în categoria premier/enterprise. După cum sugerează și numele, acest model este un Small Language Model (SLM). Avantajele utilizării Mistral Small sunt:  
- Economii de cost comparativ cu LLM-urile Mistral precum Mistral Large și NeMo - reducere de preț de 80%  
- Latentă scăzută - răspuns mai rapid comparativ cu LLM-urile Mistral  
- Flexibil - poate fi implementat în diferite medii cu mai puține restricții privind resursele necesare.

Mistral Small este ideal pentru:  
- Sarcini bazate pe text, cum ar fi sumarizarea, analiza sentimentelor și traducerea.  
- Aplicații unde se fac cereri frecvente datorită costului redus  
- Sarcini de cod cu latență scăzută, cum ar fi revizuirea și sugestiile de cod

## Compararea Mistral Small și Mistral Large

Pentru a evidenția diferențele de latență între Mistral Small și Large, rulează celulele de mai jos.

Ar trebui să observi o diferență în timpii de răspuns între 3-5 secunde. De asemenea, observă lungimea și stilul răspunsurilor pentru același prompt.

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

Este considerat un upgrade față de primul LLM open source de la Mistral, Mistral 7B.

Alte caracteristici ale modelului NeMo sunt:

- *Tokenizare mai eficientă:* Acest model folosește tokenizer-ul Tekken în locul celui mai des folosit tiktoken. Aceasta permite performanțe mai bune pe mai multe limbi și cod.

- *Finetuning:* Modelul de bază este disponibil pentru finetuning. Aceasta oferă mai multă flexibilitate pentru cazurile de utilizare unde este nevoie de ajustări suplimentare.

- *Native Function Calling* - La fel ca Mistral Large, acest model a fost antrenat pentru apeluri către funcții. Aceasta îl face unic, fiind unul dintre primele modele open source care oferă această funcționalitate.

### Compararea Tokenizer-elor

În acest exemplu, vom vedea cum Mistral NeMo gestionează tokenizarea comparativ cu Mistral Large.

Ambele exemple folosesc același prompt, dar vei observa că NeMo returnează mai puțini tokeni față de Mistral Large.

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

După ce ai terminat această lecție, consultă colecția noastră de [Învățare Generativă AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.