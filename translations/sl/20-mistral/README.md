<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:04:36+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sl"
}
-->
# Gradnja z modeli Mistral

## Uvod

Ta lekcija bo zajemala:  
- Raziskovanje različnih modelov Mistral  
- Razumevanje primerov uporabe in scenarijev za vsak model  
- Primeri kode, ki prikazujejo edinstvene lastnosti posameznega modela.

## Modeli Mistral

V tej lekciji bomo raziskali 3 različne modele Mistral:  
**Mistral Large**, **Mistral Small** in **Mistral Nemo**.

Vsak od teh modelov je brezplačno na voljo na Github Model marketplace. Koda v tem zvezku bo uporabljala te modele za izvajanje kode. Tukaj so podrobnejše informacije o uporabi Github Modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 je trenutno vodilni model podjetja Mistral in je zasnovan za poslovno uporabo.

Model je nadgradnja originalnega Mistral Large in ponuja:  
- Večje kontekstno okno - 128k v primerjavi z 32k  
- Boljšo zmogljivost pri matematičnih in programerskih nalogah - povprečna natančnost 76,9 % v primerjavi z 60,4 %  
- Izboljšano večjezično zmogljivost - jeziki vključujejo: angleščino, francoščino, nemščino, španščino, italijanščino, portugalščino, nizozemščino, ruščino, kitajščino, japonščino, korejščino, arabščino in hindijščino.

Zaradi teh lastnosti Mistral Large izstopa pri:  
- *Retrieval Augmented Generation (RAG)* - zaradi večjega kontekstnega okna  
- *Klicanju funkcij* - ta model ima vgrajeno podporo za klic funkcij, kar omogoča integracijo z zunanjimi orodji in API-ji. Klice je mogoče izvajati vzporedno ali zaporedno.  
- *Generiranju kode* - model odlično deluje pri generiranju kode v Pythonu, Javi, TypeScriptu in C++.

### Primer RAG z uporabo Mistral Large 2

V tem primeru uporabljamo Mistral Large 2 za izvajanje RAG vzorca nad besedilnim dokumentom. Vprašanje je napisano v korejščini in sprašuje o avtorjevih dejavnostih pred fakulteto.

Uporablja Cohere Embeddings Model za ustvarjanje vdelav tekstovnega dokumenta in vprašanja. Za ta primer uporablja Python paket faiss kot vektorsko bazo.

Poziv, poslan modelu Mistral, vključuje tako vprašanja kot pridobljene odlomke, ki so podobni vprašanju. Model nato poda odgovor v naravnem jeziku.

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
Mistral Small je še en model iz družine Mistral, ki spada v premier/enterprise kategorijo. Kot ime pove, gre za majhen jezikovni model (SLM). Prednosti uporabe Mistral Small so:  
- Prihranek stroškov v primerjavi z Mistral LLM, kot sta Mistral Large in NeMo - 80 % nižja cena  
- Nizka zakasnitev - hitrejši odziv v primerjavi z Mistral LLM  
- Prilagodljivost - lahko se namesti v različnih okoljih z manj omejitvami glede potrebnih virov.

Mistral Small je odličen za:  
- Naloge, ki temeljijo na besedilu, kot so povzemanje, analiza sentimenta in prevajanje.  
- Aplikacije z velikim številom zahtev zaradi stroškovne učinkovitosti  
- Naloge z nizko zakasnitvijo, kot so pregled kode in predlogi za kodo

## Primerjava Mistral Small in Mistral Large

Za prikaz razlik v zakasnitvi med Mistral Small in Large zaženite spodnje celice.

Videli boste razliko v času odziva med 3 in 5 sekundami. Prav tako opazite dolžino in slog odgovorov na isti poziv.

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

V primerjavi z ostalima dvema modeloma, predstavljenima v tej lekciji, je Mistral NeMo edini brezplačni model z licenco Apache2.

Šteje se za nadgradnjo prejšnjega odprtokodnega LLM iz Mistral, Mistral 7B.

Nekatere druge lastnosti modela NeMo so:

- *Učinkovitejša tokenizacija:* Ta model uporablja Tekken tokenizer namesto bolj pogosto uporabljenega tiktoken. To omogoča boljšo zmogljivost pri več jezikih in kodi.

- *Finetuning:* Osnovni model je na voljo za finetuning, kar omogoča večjo prilagodljivost za primere uporabe, kjer je finetuning potreben.

- *Nativno klicanje funkcij* - Tako kot Mistral Large je bil ta model usposobljen za klicanje funkcij. To ga naredi edinstvenega kot enega izmed prvih odprtokodnih modelov s to zmožnostjo.

### Primerjava tokenizatorjev

V tem primeru bomo pogledali, kako Mistral NeMo obravnava tokenizacijo v primerjavi z Mistral Large.

Oba primera uporabljata isti poziv, vendar boste opazili, da NeMo vrne manj tokenov kot Mistral Large.

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

## Učenje se tukaj ne konča, nadaljujte pot

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) in nadaljujte z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.