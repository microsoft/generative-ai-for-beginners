# Construirea cu Modelele Mistral

## Introducere

Această lecție va acoperi:
- Explorarea diferitelor modele Mistral
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model
- Explorarea exemplului de cod care arată caracteristicile unice ale fiecărui model.

## Modelele Mistral

În această lecție, vom explora 3 modele diferite Mistral:
**Mistral Large**, **Mistral Small** și **Mistral Nemo**.

Fiecare dintre aceste modele este disponibil gratuit pe [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Codul din acest notebook va folosi aceste modele pentru a rula codul.

> **Notă:** GitHub Models se va retrage la sfârșitul lunii iulie 2026. Iată mai multe detalii despre utilizarea [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pentru prototiparea cu modele AI.


## Mistral Large 2 (2407)
Mistral Large 2 este în prezent modelul emblematic al Mistral și este destinat utilizării în domeniul enterprise.

Modelul este o actualizare a modelului original Mistral Large, oferind
- Fereastră de context mai mare - 128k vs 32k
- Performanță mai bună la sarcini de matematică și codare - acuratețe medie 76,9% vs 60,4%
- Performanță multilingvistică îmbunătățită - limbile includ: engleză, franceză, germană, spaniolă, italiană, portugheză, olandeză, rusă, chineză, japoneză, coreeană, arabă și hindi.

Cu aceste caracteristici, Mistral Large excelează în
- *Generare augmentată prin recuperare (RAG)* - datorită ferestrei de context mai mari
- *Apelare de funcții* - acest model are apelare nativă de funcții care permite integrarea cu unelte și API-uri externe. Aceste apeluri pot fi făcute în paralel sau unul după altul în ordine secvențială.
- *Generare de cod* - acest model excelează în generarea de cod Python, Java, TypeScript și C++.

### Exemplu RAG folosind Mistral Large 2

În acest exemplu, folosim Mistral Large 2 pentru a rula un tipar RAG pe un document text. Întrebarea este scrisă în coreeană și întreabă despre activitățile autorului înainte de facultate.

Folosește modelul Cohere Embeddings pentru a crea embedding-uri atât ale documentului text cât și ale întrebării. Pentru acest exemplu, utilizează pachetul Python faiss ca magazin vectorial.

Promptul trimis către modelul Mistral include atât întrebările cât și bucățile recuperate care sunt similare cu întrebarea. Modelul oferă apoi un răspuns în limbaj natural.

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

# Obțineți acestea de pe pagina "Prezentare generală" a proiectului dvs. Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distanță, index
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
Mistral Small este un alt model din familia de modele Mistral din categoria premier/enterprise. După cum sugerează și numele, acest model este un Model Mic de Limbaj (SLM). Avantajele utilizării Mistral Small sunt:
- Economie de costuri comparativ cu LLM-urile Mistral precum Mistral Large și NeMo - reducere de 80% a prețului
- Latență scăzută - răspuns mai rapid comparativ cu LLM-urile Mistral
- Flexibil - poate fi implementat în diferite medii cu mai puține restricții privind resursele necesare.


Mistral Small este excelent pentru:
- Sarcini bazate pe text, cum ar fi sumarizarea, analiza sentimentului și traducerea.
- Aplicații unde cererile frecvente sunt făcute datorită eficienței costurilor
- Sarcini de cod cu latență scăzută, cum ar fi revizii și sugestii de cod

## Compararea Mistral Small și Mistral Large

Pentru a arăta diferențele de latență între Mistral Small și Large, rulați celulele de mai jos.

Ar trebui să vedeți o diferență a timpului de răspuns între 3-5 secunde. De asemenea, observați lungimea și stilul răspunsului pentru același prompt.

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

Comparativ cu celelalte două modele discutate în această lecție, Mistral NeMo este singurul model gratuit cu licență Apache2.

Este văzut ca o actualizare a modelului open source anterior de la Mistral, Mistral 7B.

Alte caracteristici ale modelului NeMo sunt:

- *Tokenizare mai eficientă:* Acest model folosește tokenizer-ul Tekken în locul celui mai utilizat tiktoken. Acest lucru permite o performanță mai bună pentru mai multe limbi și cod.

- *Finetuning:* Modelul de bază este disponibil pentru finetuning. Aceasta oferă mai multă flexibilitate pentru cazurile de utilizare unde este necesar finetuning.

- *Apelare nativă de funcții* - Ca și Mistral Large, acest model a fost antrenat pentru apelare de funcții. Acest lucru îl face unic ca fiind unul dintre primele modele open source care suportă această funcționalitate.


### Compararea Tokenizatoarelor

În acest exemplu, vom vedea cum Mistral NeMo gestionează tokenizarea comparativ cu Mistral Large.

Ambele exemple iau același prompt, dar ar trebui să observați că NeMo returnează mai puțini tokeni decât Mistral Large.

```bash
pip install mistral-common
```

```python 
# Importă pachetele necesare:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Încarcă tokenizerul Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizează o listă de mesaje
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

# Numără numărul de token-uri
print(len(tokens))
```

```python
# Importă pachetele necesare:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Încarcă tokenizer-ul Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenizează o listă de mesaje
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

# Numără numărul de tokeni
print(len(tokens))
```

## Învățarea nu se oprește aici, continuă călătoria

După ce ai terminat această lecție, verifică colecția noastră de [Învățare Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->