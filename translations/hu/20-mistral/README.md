<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:02:56+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hu"
}
-->
# Építés Mistral modellekkel

## Bevezetés

Ebben a leckében a következőkről lesz szó:  
- A különböző Mistral modellek felfedezése  
- Az egyes modellek használati eseteinek és helyzeteinek megértése  
- Kódpéldák, amelyek bemutatják az egyes modellek egyedi jellemzőit.

## A Mistral modellek

Ebben a leckében három különböző Mistral modellt ismerünk meg:  
**Mistral Large**, **Mistral Small** és **Mistral Nemo**.

Ezek a modellek ingyenesen elérhetők a Github Model piacterén. A jegyzetfüzetben található kód ezekkel a modellekkel fog futni. További részletek a Github Modellek használatáról az [AI modellekkel való prototípus készítéshez](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

A Mistral Large 2 jelenleg a Mistral zászlóshajó modellje, amely vállalati használatra készült.

Ez a modell az eredeti Mistral Large továbbfejlesztett változata, amely  
- Nagyobb kontextusablakot kínál – 128k vs 32k  
- Jobb teljesítményt nyújt matematikai és kódolási feladatokban – 76,9% átlagos pontosság vs 60,4%  
- Javított többnyelvű teljesítményt – a támogatott nyelvek között szerepel az angol, francia, német, spanyol, olasz, portugál, holland, orosz, kínai, japán, koreai, arab és hindi.

Ezekkel a tulajdonságokkal a Mistral Large kiválóan alkalmas  
- *Retrieval Augmented Generation (RAG)* feladatokra – a nagyobb kontextusablak miatt  
- *Funkcióhívásra* – a modell natív funkcióhívást támogat, ami lehetővé teszi külső eszközök és API-k integrációját. Ezek a hívások párhuzamosan vagy egymás után, sorosan is végrehajthatók.  
- *Kódgenerálásra* – különösen jól teljesít Python, Java, TypeScript és C++ generálásban.

### RAG példa Mistral Large 2-vel

Ebben a példában a Mistral Large 2 modellt használjuk egy RAG mintázat futtatására egy szöveges dokumentumon. A kérdés koreai nyelven íródott, és az író egyetemi előtti tevékenységeiről érdeklődik.

A Cohere Embeddings modellt használja a szöveges dokumentum és a kérdés beágyazásainak létrehozásához. Ehhez a mintához a faiss Python csomagot használja vektortárolóként.

A Mistral modellhez küldött prompt tartalmazza a kérdéseket és a kérdéshez hasonlóan visszakeresett szövegrészeket. A modell ezután természetes nyelvű választ ad.

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

A Mistral Small a Mistral család egy másik modellje, amely a prémium/vállalati kategóriába tartozik. Ahogy a neve is mutatja, ez egy kis méretű nyelvi modell (SLM). A Mistral Small használatának előnyei:  
- Költséghatékonyabb a Mistral nagyobb LLM-jeihez, mint a Mistral Large és NeMo képest – 80%-os árcsökkenés  
- Alacsony késleltetés – gyorsabb válaszidő a Mistral LLM-ekhez képest  
- Rugalmas – különböző környezetekben telepíthető, kevesebb erőforrás-korlátozással.

A Mistral Small kiválóan alkalmas:  
- Szöveges feladatokra, mint például összefoglalás, érzelemelemzés és fordítás  
- Olyan alkalmazásokhoz, ahol gyakori lekérések vannak a költséghatékonyság miatt  
- Alacsony késleltetésű kódolási feladatokra, például kódáttekintésre és javaslatokra

## Mistral Small és Mistral Large összehasonlítása

A késleltetésbeli különbségek bemutatásához a Mistral Small és Large között futtassa le az alábbi cellákat.

3-5 másodperces válaszidő-különbséget kell tapasztalnia. Figyelje meg a válaszok hosszát és stílusát ugyanazon prompt esetén.

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

A leckében tárgyalt két másik modellhez képest a Mistral NeMo az egyetlen ingyenes modell Apache2 licenccel.

Ez a modell a korábbi, nyílt forráskódú Mistral 7B modell továbbfejlesztett változatának tekinthető.

A NeMo modell további jellemzői:  

- *Hatékonyabb tokenizálás:* Ez a modell a Tekken tokenizálót használja a gyakrabban használt tiktoken helyett. Ez jobb teljesítményt tesz lehetővé több nyelven és kód esetén.

- *Finomhangolás:* Az alapmodell elérhető finomhangolásra, ami nagyobb rugalmasságot biztosít olyan esetekben, ahol finomhangolásra lehet szükség.

- *Natív funkcióhívás* – A Mistral Large-hoz hasonlóan ez a modell is funkcióhívásra lett betanítva. Ez egyedivé teszi, mivel az elsők között van a nyílt forráskódú modellek között, amelyek ezt támogatják.

### Tokenizálók összehasonlítása

Ebben a példában megnézzük, hogyan kezeli a Mistral NeMo a tokenizálást a Mistral Large-hoz képest.

Mindkét minta ugyanazt a promptot használja, de látható, hogy a NeMo kevesebb tokent ad vissza, mint a Mistral Large.

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

## A tanulás itt nem ér véget, folytasd az utazást

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív AI ismereteidet!

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.