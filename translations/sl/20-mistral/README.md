# Gradnja z modeli Mistral 

## Uvod 

Ta lekcija bo zajemala: 
- Raziskovanje različnih modelov Mistral 
- Razumevanje primerov uporabe in scenarijev za vsak model 
- Raziskovanje vzorcev kode, ki prikazujejo edinstvene značilnosti vsakega modela. 

## Modeli Mistral 

V tej lekciji bomo raziskali 3 različne modele Mistral: 
**Mistral Large**, **Mistral Small** in **Mistral Nemo**. 

Vsak od teh modelov je brezplačno na voljo na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Koda v tej zvezki bo uporabila te modele za izvajanje kode.

> **Opomba:** GitHub Models se bo upokojil konec julija 2026. Tukaj so dodatne podrobnosti o uporabi [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiranje z AI modeli. 


## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodilni model podjetja Mistral in je zasnovan za podjetniško uporabo. 

Model je nadgradnja prvotnega Mistral Large z zagotavljanjem 
-  Večjega kontekstnega okna - 128k v primerjavi z 32k 
-  Boljše zmogljivosti pri matematičnih in programerskih nalogah - 76,9 % povprečne natančnosti proti 60,4 % 
-  Povečane večjezične zmogljivosti - jeziki vključujejo: angleščino, francoščino, nemščino, španščino, italijanščino, portugalščino, nizozemščino, ruščino, kitajščino, japonščino, korejščino, arabščino in hindijščino.

S temi lastnostmi Mistral Large izstopa pri 
- *Pridobitveno podprti generaciji (RAG)* - zaradi večjega kontekstnega okna
- *Klicu funkcij* - ta model ima vgrajen klic funkcij, ki omogoča integracijo z zunanjimi orodji in API-ji. Ti klici se lahko izvajajo vzporedno ali zaporedoma v nizu. 
- *Generaciji kode* - ta model izstopa pri generiranju v Pythonu, Javi, TypeScriptu in C++. 

### Primer RAG z uporabo Mistral Large 2 

V tem primeru uporabljamo Mistral Large 2 za izvajanje vzorca RAG na besedilnem dokumentu. Vprašanje je napisano v korejščini in sprašuje o dejavnostih avtorja pred fakulteto. 

Uporablja model vdelav Cohere za ustvarjanje vdelav besedilnega dokumenta in vprašanja. Za ta vzorec uporablja Python paket faiss kot shrambo vektorjev. 

Poziv, poslan modelu Mistral, vključuje tako vprašanja kot pridobljene dele, ki so podobni vprašanju. Model nato poda odgovor v naravnem jeziku. 

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

# Pridobite te s strani "Pregled" vašega Microsoft Foundry projekta
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
Mistral Small je še en model v družini modelov Mistral v kategoriji premier/podjetniški. Kot ime pove, je ta model majhen jezikovni model (SLM). Prednosti uporabe Mistral Small so: 
- Varčevanje stroškov v primerjavi z LLM modeli Mistral, kot so Mistral Large in NeMo - 80 % znižanje cene
- Majhna latenca - hitrejši odziv v primerjavi z LLM modeli Mistral
- Prilagodljiv - lahko je nameščen v različnih okoljih z manj omejitvami glede potrebnih virov. 


Mistral Small je odličen za: 
- Naloge, ki temeljijo na besedilu, kot so povzemanje, analiza sentimenta in prevajanje. 
- Aplikacije, kjer so pogoste zahteve zaradi stroškovne učinkovitosti 
- Naloge kode z nizko latenco, kot so pregled in predlogi kode 

## Primerjava Mistral Small in Mistral Large 

Za prikaz razlik v latenci med Mistral Small in Large, zaženite spodnje celice. 

Opazili boste razliko v časih odziva med 3-5 sekundami. Prav tako opazite dolžine in slog odgovorov na enak poziv.  

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

V primerjavi z drugima dvema modeloma, predstavljenima v tej lekciji, je Mistral NeMo edini brezplačni model z licenco Apache2. 

Šteje se za nadgradnjo prejšnjega odprtokodnega LLM-ja podjetja Mistral, Mistral 7B. 

Nekatere druge značilnosti modela NeMo so: 

- *Učinkovitejše tokeniziranje:* Ta model uporablja tokenizator Tekken namesto bolj pogosto uporabljenega tiktoken. To omogoča boljšo zmogljivost v več jezikih in kodi. 

- *Finetuning:* Osnovni model je na voljo za nadaljnje prilagajanje. To omogoča večjo prilagodljivost za primere uporabe, kjer je prilagajanje potrebno. 

- *Vgrajen klic funkcij* - tako kot Mistral Large, je bil ta model usposobljen za klic funkcij. To ga naredi edinstvenega kot enega prvih odprtokodnih modelov s to funkcionalnostjo. 


### Primerjava tokenizatorjev 

V tem vzorcu bomo pogledali, kako Mistral NeMo obravnava tokenizacijo v primerjavi z Mistral Large. 

Oba vzorca vzameta isti poziv, vendar boste opazili, da NeMo vrne manj tokenov kot Mistral Large. 

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

# Naloži Mistral tokenizer

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

## Učenje tukaj ne konča, nadaljujte pot

Po končani tej lekciji si oglejte našo [Zbirko učenja o generativni AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->