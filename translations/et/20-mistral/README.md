# Mistral mudelitega ehitamine 

## Sissejuhatus 

See õppetund käsitleb: 
- Erinevate Mistral mudelite uurimist 
- Iga mudeli kasutusjuhtude ja stsenaariumide mõistmist 
- Koodinäidete uurimist, mis näitavad iga mudeli ainulaadseid omadusi. 

## Mistral mudelid 

Selles õppetunnis uurime kolme erinevat Mistral mudelit: 
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**. 

Iga neist mudelitest on tasuta saadaval aadressil [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Selle märkmiku kood kasutab neid mudeleid koodi käivitamiseks.

> **Märkus:** GitHub Models pensionile jääb 2026. aasta juuli lõpus. Rohkem teavet AI mudelite prototüüpimiseks kasutamise kohta leiate [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) juurest. 


## Mistral Large 2 (2407)
Mistral Large 2 on praegu Mistrali lipulaevmudel ja on mõeldud ettevõtte kasutuseks. 

Mudel on täiendus originaalsele Mistral Large mudelile, pakkudes 
- Suuremat konteksti akent - 128k vs 32k 
- Paremat tulemuslikkust matemaatika ja koodi ülesannetes - 76,9% keskmist täpsust vs 60,4% 
- Suurenenud mitmekeelseid võimekusi - keeled hõlmavad: inglise, prantsuse, saksa, hispaania, itaalia, portugali, hollandi, vene, hiina, jaapani, korea, araabia ja hindi keelt.

Nende omadustega paistab Mistral Large silma: 
- *Taasesitusega täiendatud genereerimine (RAG)* - suurema konteksti akna tõttu
- *Funktsioonikõned* - see mudel toetab natiivset funktsioonikõnede kasutamist, mis võimaldab integreerumist väliste tööriistade ja API-dega. Need kõned võivad toimuda nii paralleelselt kui ka järjestikku.
- *Koodigeneerimine* - see mudel on väga hea Pythoni, Java, TypeScripti ja C++ genereerimisel. 

### RAG näide, kasutades Mistral Large 2 

Selles näites kasutame Mistral Large 2 RAG mustriga tekstidokumendi töötlemiseks. Küsimus on kirjutatud korea keeles ja küsib autori tegevusi enne ülikooli. 

See kasutab Cohere embedimist mudelit, et luua embedimised tekstidokumendi ja küsimuse jaoks. Selle näite puhul kasutatakse faiss Python paketti vektoripoena. 

Mudelile saadetav prompt sisaldab nii küsimust kui ka leitud lõike, mis on küsimusega sarnased. Mudel seejärel vastab loomulikus keeles. 

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

# Hankige need oma Microsoft Foundry projekti "Ülevaade" lehelt
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # kaugus, indeks
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
Mistral Small on teine mudel Mistrali mudelite peres, kuuludes premier/ettevõtte kategooriasse. Nagu nimigi vihjab, on see mudel väike keelemudel (Small Language Model, SLM). Mistral Small kasutamise eelised on: 
- Kuluefektiivsus võrreldes Mistral LLM-dega nagu Mistral Large ja NeMo - 80% hinnalangus
- Madal latentsus - vastused kiiremad võrreldes Mistral LLM-dega
- Paindlikkus - saab kasutada erinevates keskkondades, kus ressursinõuded on kergemad. 


Mistral Small sobib suurepäraselt: 
- Tekstipõhisteks ülesanneteks nagu kokkuvõtete tegemine, meeleoluanalüüs ja tõlkimine. 
- Rakendustesse, kus päringuid tehakse sageli, tänu selle soodsale hinnale 
- Madala latentsusega koodiülesannete jaoks nagu ülevaatus ja koodisoovitused 

## Mistral Small ja Mistral Large võrdlus 

Latentsuse erinevuste demonstreerimiseks Mistral Small ja Large vahel käivita allolevad lahtrid. 

Peaksid nägema vastuseaja erinevust umbes 3–5 sekundit. Pane tähele ka vastuse pikkust ja stiili sama prompti puhul.  

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

Võrreldes kahe eelnevalt käsitletud mudeliga on Mistral NeMo ainus tasuta mudel, millel on Apache2 litsents. 

Seda peetakse täienduseks varasemale avatud lähtekoodiga Mistrali suurele keelemudelile Mistral 7B-le. 

Mõned NeMo mudeli muud omadused on: 

- *Tõhusam tokeniseerimine:* See mudel kasutab Tekken tokenisaatorit, mis on paindlikum kui tavapärasem tiktoken. See tagab parema jõudluse paljudes keeltes ja koodis. 

- *Peenhäälestus:* Põhimudel on saadaval peenhäälestamiseks. See võimaldab rohkem paindlikkust kasutusjuhtudel, kus peenhäälestus võib vajalik olla. 

- *Natiivne funktsioonikõnede tugi* - Nagu Mistral Large, on see mudel koolitatud funktsioonikõnedele. See teeb temast unikaalse, kuna tegemist on ühe esimese avatud lähtekoodiga mudeliga, mis seda toetab. 


### Tokenisaatorite võrdlus 

Selles näites vaatleme, kuidas Mistral NeMo tokeniseerib võrreldes Mistral Large mudeliga. 

Mõlemad näited kasutavad sama prompti, kuid näed, et NeMo tagastab vähem tähemärke kui Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Impordi vajalikud paketid:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Laadi Mistral tokeniseerija

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniseeri sõnumite nimekiri
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

# Loenda tokenite arv
print(len(tokens))
```

```python
# Impordi vajalikud paketid:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Laadi Mistral tokeniseerija

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniseeri sõnumite nimekiri
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

# Loe tokenite arvu
print(len(tokens))
```

## Õppimine ei peatu siin, jätka teekonda

Pärast selle õppetunni lõpetamist vaata meie [Generative AI õppe kollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste tõstmist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->