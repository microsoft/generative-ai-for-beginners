# Mistrali mudelitega ehitamine 

## Sissejuhatus 

Selles õppetükis käsitleme: 
- Erinevate Mistrali mudelite uurimist 
- Iga mudeli kasutusjuhtude ja stsenaariumite mõistmist 
- Koodi näidete uurimist, mis näitavad iga mudeli ainulaadseid omadusi. 

## Mistrali mudelid 

Selles õppetükis uurime kolme erinevat Mistrali mudelit: 
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**. 

Kõik need mudelid on tasuta kättesaadavad saidil [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Selle märkmeraamatu kood kasutab neid mudeleid koodi käivitamiseks.

> **Märkus:** GitHub Models suletakse 2026. aasta juuli lõpus. Siit leiate lisateavet [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kasutamise kohta AI mudelite prototüüpimiseks. 


## Mistral Large 2 (2407)
Mistral Large 2 on praegu Mistrali lipulaev mudel ja on mõeldud ettevõtete kasutamiseks. 

Mudel on uuendus võrreldes algse Mistral Large mudeliga, pakkudes 
-  Suuremat konteksti akent - 128k vs 32k 
-  Paremad tulemused matemaatika ja programmeerimise ülesannetes - 76,9% keskmine täpsus vs 60,4% 
-  Suurenenud mitmekeelseid tulemusi - toetatud keeled: inglise, prantsuse, saksa, hispaania, itaalia, portugali, hollandi, vene, hiina, jaapani, korea, araabia ja hindi.

Nende omadustega paistab Mistral Large silma järgnevates valdkondades: 
- *Taastekstimisel põhinev loomine (RAG)* - tänu suuremale konteksti aknale
- *Funktsioonikõne* - see mudel toetab natiivset funktsioonikõnet, mis võimaldab integreeritud kasutada väliseid tööriistu ja API-sid. Neid kõnesid saab teha paralleelselt või ükshaaval järjestikku. 
- *Koodi genereerimine* - see mudel on eriti tugev Python, Java, TypeScripti ja C++ genereerimisel. 

### RAG näide kasutades Mistral Large 2 mudelit

Selles näites kasutame Mistral Large 2 mudelit, et rakendada RAG-mustrit tekstidokumendi peal. Küsimus on kirjutatud koreakeelsena ja küsib autori tegevuste kohta enne kolledžit. 

Kasutatakse Cohere Embeddings mudelit, et luua teksti- ja küsimuse manuseid. Selle näite puhul kasutatakse vektoripoes faiss Python paketti. 

Mistral mudelile saadetav prompt sisaldab nii küsimusi kui ka küsimusele sarnaseid tagastatud lõike. Mudel annab seejärel loomulikus keeles vastuse. 

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
Mistral Small on teine mudel Mistrali pere mudelite hulgas peamise/ettevõtte kategooria all. Nime järgi on see väike keelemudel (SLM). Mistral Small kasutamise eelised on järgmised: 
- Säästab kulusid võrreldes Mistrali suurte LLM-idega nagu Mistral Large ja NeMo - 80% hinnalangus
- Madal latentsus - kiirem reageerimine võrreldes Mistrali LLM-idega
- Paindlik - saab paigaldada erinevatesse keskkondadesse, nõudes vähem ressursse.


Mistral Small sobib hästi: 
- Tekstipõhisteks ülesanneteks nagu kokkuvõtete tegemine, meeleolu analüüs ja tõlkimine. 
- Rakendused, kus tehakse sageli päringuid tänu selle kuluefektiivsusele 
- Madala latentsusega kodeerimise ülesanded, nagu koodi ülevaatus ja koodisoovitused 

## Mistral Small ja Mistral Large võrdlus 

Näitamaks latentsus erinevusi Mistral Small ja Large vahel, käivitage allolevad rakud. 

Näete vastuse aegade erinevust umbes 3-5 sekundit. Pöörake tähelepanu ka vastuste pikkusele ja stiilile sama prompti puhul.  

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

Võrreldes teiste selles õppetükis käsitletud mudelitega on Mistral NeMo ainus tasuta mudel, mille litsents on Apache2. 

Seda peetakse uuenduseks varasemale Mistrali avatud lähtekoodiga LLM-ile, Mistral 7B-le. 

Mõned muud NeMo mudeli omadused on: 

- *Tõhusam tokeniseerimine:* See mudel kasutab Tekkeni tokeniseerijat, mis on parem valik kui sagedamini kasutatav tiktoken. See tagab paremad tulemused mitmes keeles ja koodis. 

- *Häälestamise võimalus:* Põhimudel on saadaval peenhäälestamiseks. See annab suurema paindlikkuse kasutusjuhtudel, kus võib olla vaja peenhäälestust. 

- *Natiivne funktsioonikõne* - Nagu Mistral Large, on ka see mudel treenitud funktsioonikõneks. See muudab selle ainulaadseks ning on üks esimesi avatud lähtekoodiga mudeleid, mis seda toetab. 


### Tokeniseerijate võrdlus 

Selles näites vaatleme, kuidas Mistral NeMo käsitleb tokeniseerimist võrreldes Mistral Large'iga. 

Mõlemad näited võtavad sama prompti, kuid näete, et NeMo tagastab vähem tokeneid kui Mistral Large. 

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

# Laadi Mistrali tokeniseerijat

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

# Loe tokenite arv
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

# Laadi Mistrali tokenisaator

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniseeri sõnumite loend
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

## Õppimine ei lõpe siin, jätka teekonda

Pärast selle õppetüki lõpetamist vaadake meie [Generatiivse tehisintellekti õppematerjalide kogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste süvendamist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->