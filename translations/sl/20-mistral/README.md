# Gradnja z modeli Mistral 

## Uvod 

Ta lekcija bo pokrila: 
- Raziskovanje različnih modelov Mistral 
- Razumevanje primerov uporabe in scenarijev za vsak model 
- Raziskovanje vzorcev kode, ki prikazujejo edinstvene funkcije posameznega modela. 

## Modeli Mistral 

V tej lekciji bomo raziskali 3 različne modele Mistral: 
**Mistral Large**, **Mistral Small** in **Mistral Nemo**. 

Vsak od teh modelov je na voljo brezplačno na GitHub Model Marketplace. Koda v tem zvezku bo uporabljala te modele za izvajanje kode. Tukaj so podrobnejše informacije o uporabi GitHub Modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodilni model podjetja Mistral, namenjen uporabi v podjetjih. 

Model je nadgradnja originalnega Mistral Large in ponuja 
-  Večje okno konteksta - 128k proti 32k 
-  Boljšo zmogljivost pri matematičnih in kodnih nalogah - povprečna natančnost 76,9 % proti 60,4 % 
-  Povečano večjezično zmogljivost - jeziki vključujejo: angleščino, francoščino, nemščino, španščino, italijanščino, portugalščino, nizozemščino, ruščino, kitajščino, japonščino, korejščino, arabščino in hindijščino.

S temi funkcijami Mistral Large izstopa pri 
- *Generiranje z obogatitvijo iskanja (RAG)* - zaradi večjega okna konteksta
- *Klicanje funkcij* - ta model ima nativno klicanje funkcij, kar omogoča integracijo z zunanjimi orodji in API-ji. Ti klici so lahko izvedeni tako vzporedno kot zaporedno. 
- *Generiranje kode* - ta model izstopa pri generiranju v Pythonu, Javi, TypeScriptu in C++. 

### Primer RAG z uporabo Mistral Large 2 

V tem primeru uporabljamo Mistral Large 2 za izvajanje vzorca RAG nad besedilnim dokumentom. Vprašanje je zapisano v korejščini in sprašuje o avtorjevih dejavnostih pred fakulteto. 

Uporablja Cohere Embeddings Model za ustvarjanje vdelav besedilnega dokumenta in vprašanja. Za ta primer uporablja Python paket faiss kot vektorsko bazo. 

Poziv, poslan modelu Mistral, vključuje tako vprašanja kot pridobljene odseke, ki so podobni vprašanju. Model nato zagotovi odgovor v naravnem jeziku. 

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # razdalja, indeks
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
Mistral Small je še en model v družini Mistral v premier/enterprise kategoriji. Kot že ime pove, je ta model majhen jezikovni model (SLM). Prednosti uporabe Mistral Small so: 
- Prihranek stroškov v primerjavi z Mistral LLM, kot sta Mistral Large in NeMo - zmanjšanje cene za 80 %
- Nizka zakasnitev - hitrejši odziv v primerjavi z Mistral LLM
- Prilagodljivost - lahko se namešča v različnih okoljih z manj omejitvami glede zahtevanih virov. 


Mistral Small je odličen za: 
- Besedilne naloge kot so povzemanje, analiza čustev in prevajanje. 
- Aplikacije, kjer se izvajajo pogoste zahteve zaradi stroškovne učinkovitosti 
- Naloge z nizko zakasnitvijo, kot so pregled kode in predlogi kode 

## Primerjava Mistral Small in Mistral Large 

Za prikaz razlik v zamiku med Mistral Small in Large zaženite spodnje celice. 

Opazili boste razliko v času odziva med 3 in 5 sekund. Prav tako opazite dolžino in slog odziva pri istem pozivu.  

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

V primerjavi z drugima dvema modeloma, predstavljenima v tej lekciji, je Mistral NeMo edini brezplačni model z licenco Apache2. 

Obravnava se kot nadgradnja prej odprtokodnega LLM podjetja Mistral, Mistral 7B. 

Nekatere druge funkcije modela NeMo so: 

- *Učinkovitejša tokenizacija:* Ta model uporablja tokenizator Tekken namesto pogosto uporabljenega tiktoken. To omogoča boljšo zmogljivost pri več jezikih in kodi. 

- *Finetuning:* Osnovni model je na voljo za finetuning. To omogoča večjo prilagodljivost za primere uporabe, kjer je finetuning potreben. 

- *Nativno klicanje funkcij* - Tako kot Mistral Large je bil ta model usposobljen za klicanje funkcij. To ga naredi edinstvenega kot enega izmed prvih odprtokodnih modelov, ki to omogočajo. 


### Primerjava tokenizatorjev 

V tem vzorcu bomo pogledali, kako Mistral NeMo obdeluje tokenizacijo v primerjavi z Mistral Large. 

Oba vzorca obravnavata isti poziv, vendar bi morali opaziti, da NeMo vrne manj tokenov kot Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Uvozi potrebne pakete:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Naloži Mistral tokenizator

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniziraj seznam sporočil
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

# Preštej število tokenov
print(len(tokens))
```

```python
# Uvozi potrebne pakete:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Naloži Mistral tokenizator

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniziraj seznam sporočil
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

# Preštej število tokenov
print(len(tokens))
```

## Učenje se tukaj ne konča, nadaljujte pot

Po zaključku te lekcije preverite našo [Zbirko učenja o generativni AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nadaljnje nadgrajevanje vašega znanja o generativni AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatsko prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v matičnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni prevod s strani človeka. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->