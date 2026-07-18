# Construind cu modelele Mistral 

## Introducere 

Această lecție va acoperi: 
- Explorarea diferitelor modele Mistral 
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model 
- Explorarea exemplelor de cod care arată caracteristicile unice ale fiecărui model. 

## Modelele Mistral 

În această lecție, vom explora 3 modele Mistral diferite: 
**Mistral Large**, **Mistral Small** și **Mistral Nemo**. 

Fiecare dintre aceste modele este disponibil gratuit pe [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Codul din acest notebook va folosi aceste modele pentru a rula codul.

> **Notă:** GitHub Models se va retrage la sfârșitul lunii iulie 2026. Iată mai multe detalii despre utilizarea [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pentru prototiparea cu modele AI. 


## Mistral Large 2 (2407)
Mistral Large 2 este în prezent modelul emblematic al Mistral și este conceput pentru utilizare în întreprinderi. 

Modelul este o actualizare a modelului original Mistral Large, oferind 
- Fereastră de context mai mare - 128k vs 32k 
- Performanță mai bună la sarcini de matematică și programare - acuratețe medie de 76,9% vs 60,4% 
- Performanță multilingvă îmbunătățită - limbile includ: engleză, franceză, germană, spaniolă, italiană, portugheză, olandeză, rusă, chineză, japoneză, coreeană, arabă și hindi.

Cu aceste caracteristici, Mistral Large excelează la 
- *Generare augmentată prin recuperare (RAG)* - datorită ferestrei de context mai mari
- *Apelarea funcțiilor* - acest model are apelare nativă de funcții care permite integrarea cu instrumente și API-uri externe. Aceste apeluri pot fi realizate în paralel sau unul după altul în ordine secvențială. 
- *Generarea de cod* - acest model excelează la generarea de cod în Python, Java, TypeScript și C++. 

### Exemplu RAG folosind Mistral Large 2 

În acest exemplu, folosim Mistral Large 2 pentru a rula un model RAG pe un document text. Întrebarea este scrisă în coreeană și întreabă despre activitățile autorului înainte de facultate. 

Folosește modelul Cohere Embeddings pentru a crea embeddinguri ale documentului text, precum și ale întrebării. Pentru acest exemplu, folosește pachetul Python faiss ca magazin vectorial. 

Promptul trimis modelului Mistral include atât întrebările, cât și fragmentarele recuperate care sunt similare cu întrebarea. Modelul apoi oferă un răspuns în limbaj natural. 

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

# Obțineți acestea de pe pagina „Prezentare generală” a proiectului dvs. Microsoft Foundry
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
Mistral Small este un alt model din familia Mistral, în categoria premier/enterprise. După cum sugerează numele, acest model este un Model Mic de Limbaj (SLM). Avantajele utilizării Mistral Small sunt că este: 
- Economisitor de costuri comparativ cu LLM-urile Mistral precum Mistral Large și NeMo - reducere de preț de 80%
- Latentă scăzută - răspuns mai rapid comparativ cu LLM-urile Mistral
- Flexibil - poate fi implementat în diferite medii cu mai puține restricții asupra resurselor necesare. 


Mistral Small este ideal pentru: 
- Sarcini bazate pe text cum ar fi sumarizarea, analiza sentimentelor și traducerea. 
- Aplicații în care se fac cereri frecvente datorită costului efectiv 
- Sarcini de cod cu latență scăzută, cum ar fi revizuirea și sugestiile de cod 

## Comparând Mistral Small și Mistral Large 

Pentru a arăta diferențele de latență între Mistral Small și Large, rulați celulele de mai jos. 

Ar trebui să observați o diferență în timpii de răspuns de 3-5 secunde. De asemenea, notați lungimile și stilul răspunsurilor la același prompt.  

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

Este considerat o actualizare a modelului open source anterior de la Mistral, Mistral 7B. 

Alte caracteristici ale modelului NeMo sunt: 

- *Tokenizare mai eficientă:* Acest model folosește tokenizerul Tekken în locul tiktoken mai folosit. Aceasta permite o performanță mai bună pe mai multe limbi și cod. 

- *Finetuning:* Modelul de bază este disponibil pentru finetuning. Aceasta permite o flexibilitate mai mare pentru cazuri de utilizare unde finetuning-ul este necesar. 

- *Apelul nativ al funcțiilor* - Ca Mistral Large, acest model a fost antrenat pentru apelul de funcții. Aceasta îl face unic ca fiind unul dintre primele modele open source care fac acest lucru. 


### Comparând tokenizerele 

În acest exemplu, vom vedea cum Mistral NeMo tratează tokenizarea comparativ cu Mistral Large. 

Ambele exemple folosesc același prompt, dar ar trebui să observați că NeMo returnează mai puțini tokeni decât Mistral Large. 

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

# Încarcă tokenizer-ul Mistral

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

# Numără numărul de tokeni
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

După ce ați terminat această lecție, consultați colecția noastră de [Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a vă continua dezvoltarea cunoștințelor în AI generativ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->