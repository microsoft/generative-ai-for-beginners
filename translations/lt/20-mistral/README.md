<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-08-25T12:46:04+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "lt"
}
-->
# Darbas su Mistral modeliais

## Įvadas

Šioje pamokoje aptarsime:
- Skirtingų Mistral modelių apžvalgą
- Kiekvieno modelio naudojimo atvejus ir scenarijus
- Kodo pavyzdžius, parodančius unikalius kiekvieno modelio bruožus

## Mistral modeliai

Šioje pamokoje susipažinsime su 3 skirtingais Mistral modeliais:
**Mistral Large**, **Mistral Small** ir **Mistral Nemo**.

Visi šie modeliai nemokamai prieinami Github Modelų turgavietėje. Šioje užrašinėje pateiktas kodas naudos šiuos modelius. Daugiau informacijos apie Github Models naudojimą [AI modelių prototipavimui](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 šiuo metu yra pagrindinis Mistral modelis, skirtas verslo poreikiams.

Šis modelis yra patobulinta pradinio Mistral Large versija, siūlanti:
- Didesnį konteksto langą – 128k vietoj 32k
- Geresnį našumą matematikos ir programavimo užduotyse – vidutiniškai 76,9% tikslumas vietoj 60,4%
- Pagerintą daugiakalbį veikimą – palaikomos kalbos: anglų, prancūzų, vokiečių, ispanų, italų, portugalų, olandų, rusų, kinų, japonų, korėjiečių, arabų ir hindi.

Dėl šių savybių Mistral Large puikiai tinka:
- *RAG (Retrieval Augmented Generation)* – dėl didesnio konteksto lango
- *Funkcijų kvietimas* – modelis natūraliai palaiko funkcijų kvietimą, leidžiantį integruoti su išoriniais įrankiais ir API. Šiuos kvietimus galima atlikti tiek lygiagrečiai, tiek nuosekliai vieną po kito.
- *Kodo generavimas* – modelis ypač gerai generuoja Python, Java, TypeScript ir C++ kodą.

### RAG pavyzdys su Mistral Large 2

Šiame pavyzdyje naudojame Mistral Large 2, kad pritaikytume RAG šabloną teksto dokumentui. Klausimas užrašytas korėjiečių kalba ir klausia apie autoriaus veiklą prieš universitetą.

Naudojamas Cohere Embeddings Model, kad būtų sukurtos teksto dokumento ir klausimo įterptys. Šiame pavyzdyje vektorių saugyklai naudojamas faiss Python paketas.

Mistral modeliui siunčiamame užklausoje yra tiek klausimas, tiek surasti teksto fragmentai, panašūs į klausimą. Modelis pateikia atsakymą natūralia kalba.

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
Mistral Small yra dar vienas Mistral šeimos modelis, priklausantis aukščiausios/verslo klasės kategorijai. Kaip rodo pavadinimas, tai yra mažasis kalbos modelis (SLM). Mistral Small privalumai:
- Mažesnės išlaidos, palyginti su Mistral LLM, tokiais kaip Mistral Large ir NeMo – 80% kainos sumažėjimas
- Maža delsos trukmė – greitesnis atsakas nei Mistral LLM
- Lankstumas – gali būti diegiamas įvairiose aplinkose su mažesniais resursų reikalavimais

Mistral Small puikiai tinka:
- Teksto užduotims, tokioms kaip santraukų kūrimas, nuotaikos analizė ir vertimas
- Programoms, kuriose dažnai siunčiamos užklausos dėl ekonomiškumo
- Mažos delsos kodo užduotims, pvz., kodo peržiūrai ar pasiūlymams

## Mistral Small ir Mistral Large palyginimas

Norėdami pamatyti delsos skirtumus tarp Mistral Small ir Large, paleiskite žemiau esančias ląsteles.

Turėtumėte pastebėti 3–5 sekundžių skirtumą atsako laikuose. Taip pat atkreipkite dėmesį į atsakymų ilgius ir stilių naudojant tą pačią užklausą.

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

Palyginti su kitais dviem šioje pamokoje aptartais modeliais, Mistral NeMo yra vienintelis nemokamas modelis su Apache2 licencija.

Jis laikomas ankstesnio atvirojo kodo Mistral LLM, Mistral 7B, patobulinimu.

Kitos NeMo modelio savybės:

- *Efektyvesnė tokenizacija:* Šis modelis naudoja Tekken tokenizatorių vietoje dažniau naudojamo tiktoken. Tai leidžia geriau veikti su daugiau kalbų ir kodo.

- *Finetuningas:* Bazinis modelis prieinamas papildomam apmokymui. Tai suteikia daugiau lankstumo, kai reikia pritaikyti modelį specifiniams poreikiams.

- *Natūralus funkcijų kvietimas* – kaip ir Mistral Large, šis modelis apmokytas funkcijų kvietimui. Tai išskiria jį kaip vieną pirmųjų atvirojo kodo modelių su tokia galimybe.

### Tokenizatorių palyginimas

Šiame pavyzdyje pažiūrėsime, kaip Mistral NeMo atlieka tokenizaciją, palyginti su Mistral Large.

Abu pavyzdžiai naudoja tą pačią užklausą, tačiau turėtumėte pastebėti, kad NeMo grąžina mažiau tokenų nei Mistral Large.

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

## Mokymasis nesibaigia čia – tęskite kelionę

Baigę šią pamoką, apsilankykite mūsų [Generatyvaus AI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyvųjį dirbtinį intelektą!

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.