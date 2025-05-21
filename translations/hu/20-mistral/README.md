<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:01:49+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hu"
}
-->
# Építés Mistral Modellek segítségével

## Bevezetés

Ez a lecke a következőkről szól:
- A különböző Mistral Modellek felfedezése
- Az egyes modellek használati eseteinek és forgatókönyveinek megértése
- Kódminták, amelyek bemutatják az egyes modellek egyedi jellemzőit.

## A Mistral Modellek

Ebben a leckében 3 különböző Mistral modellt fogunk megvizsgálni: **Mistral Large**, **Mistral Small** és **Mistral Nemo**.

Ezek a modellek ingyenesen elérhetők a Github Model piacon. A jegyzetfüzetben szereplő kód ezekkel a modellekkel futtatja a kódot. További részletek a Github Modellek használatáról az [AI modellekkel való prototípus-készítéshez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
A Mistral Large 2 jelenleg a Mistral zászlóshajó modellje, és vállalati felhasználásra készült.

A modell fejlesztést jelent az eredeti Mistral Large-hoz képest, a következőkkel:
- Nagyobb kontextusablak - 128k vs 32k
- Jobb teljesítmény matematikai és kódolási feladatoknál - 76,9% átlagos pontosság vs 60,4%
- Növelt többnyelvű teljesítmény - a nyelvek között: angol, francia, német, spanyol, olasz, portugál, holland, orosz, kínai, japán, koreai, arab és hindi.

Ezekkel a funkciókkal a Mistral Large kiemelkedik a következőkben:
- *Retrieval Augmented Generation (RAG)* - a nagyobb kontextusablak miatt
- *Függvényhívás* - ez a modell natív függvényhívással rendelkezik, amely lehetővé teszi a külső eszközökkel és API-kkal való integrációt. Ezek a hívások párhuzamosan vagy egymás után, szekvenciálisan is elvégezhetők.
- *Kódgenerálás* - ez a modell kiválóan teljesít a Python, Java, TypeScript és C++ generálásban.

### RAG Példa a Mistral Large 2 használatával

Ebben a példában a Mistral Large 2-t használjuk egy RAG minta futtatására egy szöveges dokumentumon. A kérdés koreaiul van írva, és az író tevékenységeiről kérdez az egyetem előtt.

A Cohere Embeddings Modelt használja a szöveges dokumentum és a kérdés beágyazásának létrehozásához. Ehhez a példához a faiss Python csomagot használja vektor tárolóként.

A Mistral modellhez küldött prompt tartalmazza mind a kérdéseket, mind a kérdéshez hasonló visszakeresett részeket. A modell ezután természetes nyelvű választ ad.

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
A Mistral Small egy másik modell a Mistral modellek családjában a prémium/vállalati kategóriában. Ahogy a neve is sugallja, ez a modell egy Kis Nyelvi Modell (SLM). A Mistral Small használatának előnyei a következők:
- Költségmegtakarítás a Mistral LLM-ekhez képest, mint a Mistral Large és NeMo - 80%-os árcsökkenés
- Alacsony késleltetés - gyorsabb válasz a Mistral LLM-ekhez képest
- Rugalmas - különböző környezetekben telepíthető, kevesebb korlátozással a szükséges erőforrásokra.

A Mistral Small nagyszerű a következőkre:
- Szövegalapú feladatok, mint az összefoglalás, érzelemelemzés és fordítás.
- Alkalmazások, ahol gyakori kérések érkeznek, költséghatékonysága miatt
- Alacsony késleltetésű kód feladatok, mint az átnézés és kódjavaslatok

## Mistral Small és Mistral Large összehasonlítása

A Mistral Small és Large közötti késleltetési különbségek bemutatására futtassa az alábbi cellákat.

Látnia kell a válaszidők közötti különbséget 3-5 másodperc között. Figyelje meg a válaszok hosszát és stílusát is ugyanazon prompt esetén.

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

A leckében tárgyalt másik két modellhez képest a Mistral NeMo az egyetlen ingyenes modell Apache2 licenccel.

Úgy tekintik, mint a korábbi nyílt forráskódú LLM fejlesztése a Mistral-tól, a Mistral 7B-től.

A NeMo modell néhány másik jellemzője:

- *Hatékonyabb tokenizálás:* Ez a modell a Tekken tokenizálót használja a gyakrabban használt tiktoken helyett. Ez jobb teljesítményt tesz lehetővé több nyelven és kódon.

- *Finomhangolás:* Az alapmodell elérhető finomhangolásra. Ez nagyobb rugalmasságot biztosít olyan használati esetekhez, ahol finomhangolásra lehet szükség.

- *Natív függvényhívás* - A Mistral Large-hoz hasonlóan ez a modell is képzett függvényhívásokra. Ez egyedivé teszi, mivel az egyik első nyílt forráskódú modell, amely képes erre.

### Tokenizálók összehasonlítása

Ebben a példában megnézzük, hogyan kezeli a Mistral NeMo a tokenizálást a Mistral Large-hoz képest.

Mindkét minta ugyanazt a promptot veszi, de látnia kell, hogy a NeMo kevesebb tokent ad vissza, mint a Mistral Large.

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

## A tanulás itt nem áll meg, folytassa az utat

A lecke befejezése után nézze meg a [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI ismereteit!

**Felelősség kizárása**:  
Ezt a dokumentumot az AI fordítószolgáltatással, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentumot annak eredeti nyelvén kell tekinteni a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget semmilyen félreértésért vagy félremagyarázásért, amely a fordítás használatából ered.