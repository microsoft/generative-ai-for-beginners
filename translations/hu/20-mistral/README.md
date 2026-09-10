# Építés Mistral modellekkel 

## Bevezetés 

Ez a lecke a következőket fogja lefedni: 
- A különböző Mistral modellek felfedezése 
- Minden modell használati esetének és szcenáriójának megértése 
- Kódminták bemutatása, amelyek a modellek egyedi jellemzőit mutatják be. 

## A Mistral modellek 

Ebben a leckében 3 különböző Mistral modellt fogunk megvizsgálni: 
**Mistral Large**, **Mistral Small** és **Mistral Nemo**. 

Mindegyik modell ingyenesen elérhető a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) oldalán. Ebben a jegyzetfüzetben ezen modelleket használjuk a kód futtatásához.

> **Megjegyzés:** A GitHub Models 2026 júliusának végén megszűnik. További részletek a [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) használatáról AI modellek prototípus készítéséhez. 


## Mistral Large 2 (2407)
A Mistral Large 2 jelenleg a Mistral zászlóshajó modellje, vállalati használatra tervezve. 

A modell az eredeti Mistral Large továbbfejlesztése a következőkkel: 
- Nagyobb Kontextusablak - 128k vs 32k 
- Jobb teljesítmény matematikai és kódolási feladatokban - átlagosan 76,9% pontosság vs 60,4% 
- Fokozott többnyelvű teljesítmény - a támogatott nyelvek: angol, francia, német, spanyol, olasz, portugál, holland, orosz, kínai, japán, koreai, arab és hindi.

Ezekkel a jellemzőkkel a Mistral Large kiváló a következőkre: 
- *Retrieval Augmented Generation (RAG)* - a nagyobb kontextusablak miatt
- *Funkcióhívás* - ez a modell natív funkcióhívási képességgel rendelkezik, amely lehetővé teszi külső eszközök és API-k integrálását. Ezek a hívások párhuzamosan vagy egymás után, szekvenciálisan is végrehajthatók. 
- *Kódgenerálás* - a modell kiemelkedik Python, Java, TypeScript és C++ generálásban. 

### RAG példa Mistral Large 2-vel 

Ebben a példában Mistral Large 2-t használunk egy RAG mintázat futtatásához egy szöveges dokumentumon. A kérdés koreai nyelven van, és az író főiskola előtti tevékenységeiről érdeklődik. 

A Cohere Embeddings Modelt használja a szöveges dokumentum és a kérdés beágyazásainak létrehozására. Ehhez a mintához a faiss Python csomagot használja vektor tárolóként. 

A Mistral modellnek küldött üzenet tartalmazza a kérdéseket és a kérdéshez hasonló visszanyert darabokat. A modell természetes nyelvű választ ad. 

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
A Mistral Small egy másik modell a Mistral családból, a prémium/vállalati kategóriában. Ahogy a neve is jelzi, ez egy kis méretű nyelvi modell (SLM). A Mistral Small használatának előnyei: 
- Költségmegtakarítás a Mistral nagyobb LLM-jeihez, mint a Mistral Large és NeMo képest - 80%-os árcsökkenés
- Alacsony késleltetés - gyorsabb válaszidő a Mistral LLM-jeihez képest
- Rugalmasság - különböző környezetekben is telepíthető, kevesebb korlátozással a szükséges erőforrásokra vonatkozóan. 


A Mistral Small ideális: 
- Szövegalapú feladatokra, például összefoglalásra, érzelem elemzésre és fordításra. 
- Olyan alkalmazásokhoz, ahol gyakori lekérések vannak a költséghatékonyság miatt 
- Alacsony késleltetésű kód feladatokra, mint kód átvizsgálás és javaslatok 

## Mistral Small és Mistral Large összehasonlítása 

A késleltetésbeli különbségek megmutatásához a Mistral Small és Large között, futtassa az alábbi cellákat. 

3-5 másodperces különbséget kell tapasztalnia a válaszidők között. Figyelje meg a válaszok hosszát és stílusát ugyanazon prompt esetén is.  

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

A másik két modellhez képest, melyeket ebben a leckében tárgyalunk, a Mistral NeMo az egyetlen ingyenes modell Apache2 licenccel. 

Ez az korábbi nyílt forráskódú Mistral 7B modell továbbfejlesztett változata. 

A NeMo modell további jellemzői: 

- *Hatékonyabb tokenizáció:* Ez a modell a Tekken tokenizert használja az általánosabban használt tiktoken helyett. Ez jobb teljesítményt biztosít több nyelven és kód esetén. 

- *Finomhangolás:* Az alapmodell finomhangolásra elérhető. Ez nagyobb rugalmasságot biztosít azokhoz az esetekhez, amikor finomhangolás szükséges lehet. 

- *Natív funkcióhívás* - A Mistral Large-hoz hasonlóan ez a modell is funkcióhívásra lett kiképezve. Ez egyedülállóvá teszi, mint az egyik első nyílt forráskódú modellt, amely ezt tudja. 


### Tokenizálók összehasonlítása 

Ebben a példában megnézzük, hogyan kezeli a tokenizációt a Mistral NeMo a Mistral Large-hoz képest. 

Mindkét minta ugyanazt a promptot használja, de látható, hogy NeMo kevesebb tokent ad vissza, mint a Mistral Large. 

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

# A tokenek számának megszámlálása
print(len(tokens))
```

## A tanulás itt nem ér véget, folytasd az utat

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább bővítsd generatív AI tudásodat!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->