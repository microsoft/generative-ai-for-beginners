<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-10-11T11:22:42+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "et"
}
-->
# Mistrali mudelite kasutamine

## Sissejuhatus

Selles õppetükis käsitletakse:
- Erinevate Mistrali mudelite uurimist
- Iga mudeli kasutusjuhtude ja stsenaariumide mõistmist
- Koodinäited, mis näitavad iga mudeli unikaalseid omadusi

## Mistrali mudelid

Selles õppetükis uurime kolme erinevat Mistrali mudelit: **Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Kõik need mudelid on tasuta saadaval Githubi mudelite turul. Selle õppetüki kood kasutab neid mudeleid koodi käivitamiseks. Siin on rohkem teavet Githubi mudelite kasutamise kohta [tehisintellekti mudelite prototüüpimiseks](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 on praegu Mistrali lipulaevamudel, mis on mõeldud ettevõtetele.

Mudelit on täiustatud võrreldes algse Mistral Large mudeliga, pakkudes:
- Suuremat kontekstiakent - 128k vs 32k
- Paremat jõudlust matemaatika ja kodeerimisülesannetes - keskmine täpsus 76,9% vs 60,4%
- Suurenenud mitmekeelset jõudlust - keeled hõlmavad: inglise, prantsuse, saksa, hispaania, itaalia, portugali, hollandi, vene, hiina, jaapani, korea, araabia ja hindi.

Nende omaduste tõttu paistab Mistral Large silma:
- *Retrieval Augmented Generation (RAG)* - tänu suuremale kontekstiaknale
- *Funktsioonikutsed* - mudelil on loomulik funktsioonikutsumine, mis võimaldab integreerimist väliste tööriistade ja API-dega. Need kutsed saab teha nii paralleelselt kui ka järjestikku.
- *Koodigeneratsioon* - mudel on suurepärane Python, Java, TypeScript ja C++ koodi genereerimisel.

### RAG näide, kasutades Mistral Large 2

Selles näites kasutame Mistral Large 2 mudelit, et rakendada RAG mustrit tekstidokumendi peal. Küsimus on kirjutatud korea keeles ja küsib autori tegevuste kohta enne ülikooli.

See kasutab Cohere Embeddings mudelit, et luua tekstidokumendi ja küsimuse sisendvektoreid. Näites kasutatakse faiss Python paketti vektorite salvestamiseks.

Mistrali mudelile saadetud sisend sisaldab nii küsimust kui ka leitud tekstilõikeid, mis on küsimusega sarnased. Mudel annab seejärel loomuliku keele vastuse.

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

Mistral Small on teine mudel Mistrali mudelite perekonnas, mis kuulub esmaklassilise/ettevõtte kategooriasse. Nagu nimigi viitab, on see väike keelemudel (SLM). Mistral Small kasutamise eelised on:
- Kulude kokkuhoid võrreldes Mistrali LLM-idega nagu Mistral Large ja NeMo - 80% hinnalangus
- Madal latentsus - kiirem vastus võrreldes Mistrali LLM-idega
- Paindlikkus - saab kasutada erinevates keskkondades, kus ressursinõuded on väiksemad.

Mistral Small sobib suurepäraselt:
- Tekstipõhiste ülesannete jaoks, nagu kokkuvõtete tegemine, sentimentanalüüs ja tõlkimine.
- Rakenduste jaoks, kus tehakse sagedasi päringuid, tänu kulutõhususele.
- Madala latentsusega koodiga seotud ülesannete jaoks, nagu ülevaated ja koodisoovitused.

## Mistral Small ja Mistral Large võrdlus

Et näidata latentsuse erinevusi Mistral Small ja Large vahel, käivitage allolevad lahtrid.

Peaksite nägema vastuseaegade erinevust 3-5 sekundi vahel. Pange tähele ka vastuste pikkust ja stiili sama sisendi puhul.

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

Võrreldes kahe teise mudeliga, mida selles õppetükis käsitleti, on Mistral NeMo ainus tasuta mudel, millel on Apache2 litsents.

Seda peetakse varasema avatud lähtekoodiga Mistrali LLM-i, Mistral 7B, täiustatud versiooniks.

Mõned NeMo mudeli muud omadused on:
- *Tõhusam tokeniseerimine:* See mudel kasutab Tekken tokeniseerijat, mitte tavaliselt kasutatavat tiktokenit. See võimaldab paremat jõudlust rohkemates keeltes ja koodis.
- *Peenhäälestamine:* Baasmudel on saadaval peenhäälestamiseks. See pakub rohkem paindlikkust kasutusjuhtude jaoks, kus peenhäälestamine võib olla vajalik.
- *Loomulik funktsioonikutsumine:* Nagu Mistral Large, on ka see mudel treenitud funktsioonikutsumisel. See teeb selle ainulaadseks, olles üks esimesi avatud lähtekoodiga mudeleid, mis seda toetab.

### Tokeniseerijate võrdlus

Selles näites vaatame, kuidas Mistral NeMo käsitleb tokeniseerimist võrreldes Mistral Large mudeliga.

Mõlemad näited kasutavad sama sisendit, kuid peaksite nägema, et NeMo tagastab vähem tokeneid võrreldes Mistral Large mudeliga.

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


## Õppimine ei lõpe siin, jätkake teekonda

Pärast selle õppetüki läbimist vaadake meie [Generatiivse AI õppekollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata generatiivse AI teadmiste arendamist!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.