<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:23:41+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sl"
}
-->
# Gradnja z modeli Mistral

## Uvod

Ta lekcija bo pokrivala:
- Raziskovanje različnih modelov Mistral
- Razumevanje primerov uporabe in scenarijev za vsak model
- Vzorci kode, ki prikazujejo edinstvene značilnosti vsakega modela.

## Mistral modeli

V tej lekciji bomo raziskali 3 različne modele Mistral: **Mistral Large**, **Mistral Small** in **Mistral Nemo**.

Vsak od teh modelov je brezplačno dostopen na tržnici modelov Github. Koda v tej beležnici bo uporabljala te modele za izvajanje kode. Tukaj so več podrobnosti o uporabi Github modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodilni model Mistral in je zasnovan za poslovno uporabo.

Model je nadgradnja originalnega Mistral Large z izboljšavami:
- Večje kontekstno okno - 128k proti 32k
- Boljša zmogljivost pri matematičnih in kodirnih nalogah - povprečna natančnost 76,9% proti 60,4%
- Povečana večjezična zmogljivost - jeziki vključujejo: angleščino, francoščino, nemščino, španščino, italijanščino, portugalščino, nizozemščino, ruščino, kitajščino, japonščino, korejščino, arabščino in hindujščino.

Zaradi teh lastnosti Mistral Large izstopa pri:
- *Generacija z izboljšanim iskanjem (RAG)* - zaradi večjega kontekstnega okna
- *Klic funkcij* - ta model ima nativno klicanje funkcij, kar omogoča integracijo z zunanjimi orodji in API-ji. Te klice je mogoče izvesti vzporedno ali zaporedno.
- *Generiranje kode* - ta model izstopa pri generiranju Python, Java, TypeScript in C++.

### Primer RAG z uporabo Mistral Large 2

V tem primeru uporabljamo Mistral Large 2 za izvajanje RAG vzorca nad besedilnim dokumentom. Vprašanje je napisano v korejščini in sprašuje o avtorjevih dejavnostih pred fakulteto.

Uporablja Cohere Embeddings Model za ustvarjanje vdelav besedilnega dokumenta in vprašanja. Za ta vzorec uporablja Python paket faiss kot skladišče vektorjev.

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
Mistral Small je še en model iz družine modelov Mistral v kategoriji premier/enterprise. Kot pove že ime, je ta model majhen jezikovni model (SLM). Prednosti uporabe Mistral Small so:
- Prihranek stroškov v primerjavi z Mistral LLM-ji, kot sta Mistral Large in NeMo - 80% znižanje cene
- Nizka zakasnitev - hitrejši odziv v primerjavi z LLM-ji Mistral
- Prilagodljiv - se lahko izvaja v različnih okoljih z manj omejitvami glede potrebnih virov.

Mistral Small je odličen za:
- Naloge na podlagi besedila, kot so povzemanje, analiza sentimenta in prevajanje.
- Aplikacije, kjer se pogosto izvajajo zahteve zaradi njegove stroškovne učinkovitosti
- Naloge kode z nizko zakasnitvijo, kot so pregled in predlogi kode

## Primerjava Mistral Small in Mistral Large

Za prikaz razlik v zakasnitvi med Mistral Small in Large, zaženite spodnje celice.

Opaziti bi morali razliko v odzivnih časih med 3-5 sekundami. Prav tako bodite pozorni na dolžino in slog odziva na isti poziv.

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

V primerjavi z drugima dvema modeloma, obravnavanima v tej lekciji, je Mistral NeMo edini brezplačni model z licenco Apache2.

Šteje se kot nadgradnja prejšnjega odprtokodnega LLM iz Mistral, Mistral 7B.

Nekatere druge značilnosti modela NeMo so:

- *Učinkovitejša tokenizacija:* Ta model uporablja tokenizator Tekken namesto bolj pogosto uporabljenega tiktoken. To omogoča boljšo zmogljivost pri več jezikih in kodi.

- *Fino nastavljanje:* Osnovni model je na voljo za fino nastavljanje. To omogoča večjo prilagodljivost za primere uporabe, kjer je fino nastavljanje morda potrebno.

- *Nativno klicanje funkcij* - Kot Mistral Large je bil ta model usposobljen za klicanje funkcij. To ga dela edinstvenega kot enega prvih odprtokodnih modelov, ki to omogoča.

### Primerjava tokenizatorjev

V tem vzorcu bomo pogledali, kako Mistral NeMo obravnava tokenizacijo v primerjavi z Mistral Large.

Oba vzorca vzameta isti poziv, vendar bi morali videti, da NeMo vrne manj tokenov v primerjavi z Mistral Large.

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

## Učenje se tukaj ne konča, nadaljujte potovanje

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Medtem ko si prizadevamo za natančnost, vas prosimo, da se zavedate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.