# Építés Mistral modellekkel

## Bevezetés

Ez a lecke a következőket fogja lefedni:
- A különböző Mistral modellek felfedezése
- Minden modell használati eseteinek és szcenárióinak megértése
- Kódpéldák felfedezése, amelyek bemutatják az egyes modellek egyedi jellemzőit.

## A Mistral modellek

Ebben a leckében három különböző Mistral modellt vizsgálunk meg:
**Mistral Large**, **Mistral Small** és **Mistral Nemo**.

Ezek a modellek ingyenesen elérhetők a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) oldalon. Ez a jegyzetfüzet ezeket a modelleket fogja használni a kód futtatásához.

> **Megjegyzés:** A GitHub Models 2026 júliusának végén megszűnik. További részletek a [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) használatáról az AI modellekkel való prototípus készítéshez.


## Mistral Large 2 (2407)
A Mistral Large 2 jelenleg a Mistral zászlóshajó modellje, vállalati használatra tervezve.

A modell az eredeti Mistral Large továbbfejlesztése az alábbi jellemzőkkel:
- Nagyobb Kontexthossz - 128k vs 32k
- Jobb teljesítmény matematikai és programozási feladatokban - 76,9% átlagos pontosság vs 60,4%
- Javított többnyelvű teljesítmény - a nyelvek között szerepel: angol, francia, német, spanyol, olasz, portugál, holland, orosz, kínai, japán, koreai, arab és hindi.

Ezekkel a jellemzőkkel a Mistral Large kiválóan teljesít
- *Retrieval Augmented Generation (RAG)* - a nagyobb kontexthossz miatt
- *Funkcióhívás* - ez a modell natív funkcióhívási képességgel rendelkezik, ami lehetővé teszi külső eszközök és API-k integrálását. Ezek a hívások párhuzamosan vagy egymás után szekvenciálisan is történhetnek.
- *Kódgenerálás* - ez a modell kiválóan teljesít Python, Java, TypeScript és C++ kód generálásában.

### RAG példa Mistral Large 2 használatával

Ebben a példában a Mistral Large 2-t egy RAG mintázat futtatására használjuk egy szöveges dokumentumon. A kérdés koreai nyelven íródott, és a szerző főiskola előtti tevékenységeire kérdez rá.

A Cohere Embeddings modellt használja a szöveges dokumentum és a kérdés beágyazásainak létrehozásához. Ehhez a példához a faiss Python csomagot használja vektortárként.

A Mistral modellnek küldött prompt tartalmazza mind a kérdéseket, mind azokat a lekért szövegrészleteket, amelyek hasonlítanak a kérdésre. A modell ezután természetes nyelvű választ ad.

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

# Szerezze be ezeket a Microsoft Foundry projektje "Áttekintés" oldaláról
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # távolság, index
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
A Mistral Small a Mistral család egy másik modellje a premier/vállalati kategóriában. A név alapján ez a modell egy Kis Nyelvi Modell (SLM). A Mistral Small használatának előnyei:
- Költséghatékonyság a Mistral nagyobb LLM-jei, mint a Mistral Large és NeMo-hoz képest - 80% árcsökkenés
- Alacsony késleltetés - gyorsabb válaszidő a Mistral LLM-jeihez képest
- Rugalmas - különböző környezetekben kevésbé erőforráskorlát mellett telepíthető


A Mistral Small kiváló:
- Szövegalapú feladatokra, mint például összefoglalás, érzelemelemzés és fordítás
- Gyakori kérés igényű alkalmazásokhoz a költséghatékonyság miatt
- Alacsony késleltetésű kódolási feladatokhoz, például kódáttekintéshez és javaslatokhoz

## Mistral Small és Mistral Large összehasonlítása

A Mistral Small és Large közötti késleltetésbeli különbségek bemutatásához futtassa le az alábbi cellákat.

Látnia kell egy 3-5 másodperces különbséget a válaszidők között. Figyelje meg a válasz hosszt és stílust ugyanazon prompt esetén.

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

A tanult két modellhez képest a Mistral NeMo az egyetlen ingyenes modell, amely Apache2 licenccel rendelkezik.

Ez az előző nyílt forráskódú Mistral LLM, a Mistral 7B továbbfejlesztéseként tekinthető.

Néhány további jellemzője a NeMo modellnek:

- *Hatékonyabb tokenizálás:* Ez a modell a Tekken tokenizer-t használja a gyakrabban használt tiktoken helyett. Ez jobb teljesítményt tesz lehetővé több nyelv és kód esetén.

- *Finomhangolás:* Az alapmodell elérhető finomhangolásra. Ez nagyobb rugalmasságot biztosít olyan használati esetekhez, ahol szükség lehet a finomhangolásra.

- *Natív funkcióhívás* - A Mistral Large-hoz hasonlóan ezt a modellt is funkcióhívásra képezték ki. Ez teszi egyedivé, mint az első nyílt forrású modellek egyikét, amely ezt támogatja.


### Tokenizálók összehasonlítása

Ebben a példában megnézzük, hogyan kezeli a Mistral NeMo a tokenizálást a Mistral Large-hoz képest.

Mindkét minta ugyanazt a promptot használja, de látható, hogy a NeMo kevesebb tokent ad vissza, mint a Mistral Large.

```bash
pip install mistral-common
```

```python 
# Szükséges csomagok importálása:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizáló betöltése

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Üzenetek listájának tokenizálása
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

# A tokenek számolása
print(len(tokens))
```

```python
# Szükséges csomagok importálása:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenizáló betöltése

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Üzenetek listájának tokenizálása
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

# Tokenek számának megszámlálása
print(len(tokens))
```

## A tanulás nem ér véget itt, folytasd az utat

A lecke befejezése után nézd meg a [Generative AI Learning gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy folytathasd a Generatív AI ismereteid fejlesztését!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->