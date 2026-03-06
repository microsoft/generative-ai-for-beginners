# Építés a Mistral Modellekkel

## Bevezetés

Ez a lecke a következőket fogja lefedni:
- A különböző Mistral modellek felfedezése
- Az egyes modellek használati eseteinek és szcenárióinak megértése
- Kódminták vizsgálata, amelyek bemutatják az egyes modellek egyedi jellemzőit.

## A Mistral Modellek

Ebben a leckében három különböző Mistral modellt fogunk felfedezni:
**Mistral Large**, **Mistral Small** és **Mistral Nemo**.

Ezek a modellek ingyenesen elérhetők a GitHub Model piactéren. A jegyzetfüzet kódja ezen modellek használatával futtatja a kódot. Itt további részletek találhatók a GitHub Modellek AI modellekkel való [prototípus készítéséhez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
A Mistral Large 2 jelenleg a Mistral zászlóshajó modellje, és vállalati használatra tervezték.

A modell az eredeti Mistral Large továbbfejlesztése az alábbiakkal:
- Nagyobb kontextusablak – 128k kontra 32k
- Jobb teljesítmény matematika és kódolási feladatokban – 76,9% átlagos pontosság kontra 60,4%
- Fokozott többnyelvű teljesítmény – a nyelvek között szerepel: angol, francia, német, spanyol, olasz, portugál, holland, orosz, kínai, japán, koreai, arab és hindi.

Ezekkel a funkciókkal a Mistral Large kiváló:
- *Retrieval Augmented Generation (RAG)* – a nagyobb kontextusablak miatt
- *Funkcióhívás* – ennek a modellnek natív funkcióhívása van, ami lehetővé teszi külső eszközökkel és API-kkal való integrációt. Ezeket a hívásokat párhuzamosan vagy egymás után, szekvenciálisan is végre lehet hajtani.
- *Kódgenerálás* – ez a modell kiemelkedő a Python, Java, TypeScript és C++ generálásában.

### RAG példa a Mistral Large 2 használatával

Ebben a példában a Mistral Large 2 modellt használjuk egy RAG mintázat futtatására egy szöveges dokumentum felett. A kérdés koreai nyelven íródott és az író főiskola előtti tevékenységeiről kérdez.

A Cohere Embeddings Modelt használja a szöveges dokumentum és a kérdés embeddingjeinek létrehozásához. Ehhez a mintához a faiss Python csomagot alkalmazza vektoráruházként.

A Mistral modellnek küldött prompt tartalmazza mind a kérdéseket, mind a kérdéshez hasonlóan lekért részleteket. A modell ezután természetes nyelvi választ ad.

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
A Mistral Small egy másik modell a Mistral család premier/vállalati kategóriájában. A névnek megfelelően ez egy kicsi nyelvi modell (SLM). A Mistral Small használatának előnyei:
- Költségmegtakarítás a Mistral nagyobb LLM-jeihez képest, például Mistral Large és NeMo – 80% árcsökkenés
- Alacsony válaszidő – gyorsabb válasz a Mistral LLM-jeihez képest
- Rugalmasság – különböző környezetekben telepíthető kevesebb erőforrás-korlátozással.

A Mistral Small nagyszerű:
- Szövegalapú feladatokra, például összefoglalásra, érzelemfelismerésre és fordításra.
- Alkalmazásokhoz, ahol gyakori lekérések vannak, a költséghatékonysága miatt
- Alacsony késleltetésű kódolási feladatokra, mint a kód átnézése és javaslatok

## A Mistral Small és Mistral Large összehasonlítása

A válaszidők közötti különbség bemutatásához futtassa le az alábbi cellákat.

Az elvárt különbség a válaszidőben 3–5 másodperc között van. Érdemes megfigyelni a válasz hosszt és stílust ugyanazon prompt esetén.

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

A két előző modellhez képest a Mistral NeMo az egyetlen ingyenes modell Apache2 licenccel.

Az előző, nyílt forráskódú Mistral LLM-hez, a Mistral 7B-hez képest ezt az upgrade-nek tekintik.

A NeMo modell más jellemzői:

- *Hatékonyabb tokenizáció:* Ez a modell a Tekken tokenizert használja a gyakrabban használt tiktoken helyett. Ez jobb teljesítményt tesz lehetővé több nyelv és kód esetében.

- *Finomhangolás:* Az alapmodell elérhető finomhangolásra. Ez nagyobb rugalmasságot ad olyan esetekben, amikor finomhangolásra lehet szükség.

- *Natív funkcióhívás* – A Mistral Large-hez hasonlóan ezt a modellt is funkcióhívásra képezték ki. Ez egyedülállóvá teszi, mint az egyik első nyílt forráskódú modell, amely így működik.

### Tokenizerek összehasonlítása

Ebben a mintában megnézzük, hogyan kezeli a Mistral NeMo a tokenizációt a Mistral Large-hoz képest.

Mindkét minta ugyanazt a promptot veszi, de látható, hogy NeMo kevesebb tokennel tér vissza, mint a Mistral Large.

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

# A tokenek számának megszámlálása
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

# A tokenek számának megszámlálása
print(len(tokens))
```

## A tanulás itt nem áll meg, folytasd az utazást

A lecke befejezése után tekintsd meg a [Generatív AI Oktatás gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd Generatív AI ismereteidet!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy félreértelmezésért, amely ezen fordítás használatából ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->