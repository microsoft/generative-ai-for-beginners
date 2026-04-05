# Mistral mudelitega ehitamine

## Sissejuhatus

Selles õppetükis käsitleme:
- Erinevate Mistral mudelite uurimist
- Iga mudeli kasutusjuhtude ja stsenaariumide mõistmist
- Koodi näidete uurimist, mis näitavad iga mudeli unikaalseid omadusi.

## Mistral mudelid

Selles õppetükis uurime 3 erinevat Mistral mudelit:
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Iga neist mudelitest on GitHubi mudeliturgudel tasuta saadaval. Selle märkme kood kasutab nende mudelite käitamiseks neid mudeleid. Rohkem teavet GitHubi mudelite kasutamise kohta leiate siit: [prototüüpimine AI mudelitega](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 on hetkel Mistrali lipulaevmudel ja on loodud ettevõtte kasutamiseks.

Mudelit on uuendatud võrreldes originaaliga Mistral Large, pakkudes
- Suuremat konteksti akent - 128k vs 32k
- Paremat sooritust matemaatika ja programmeerimise ülesannetes - 76.9% keskmine täpsus vs 60.4%
- Suurenenud mitmekeelseid võimalusi - keeled hõlmavad: inglise, prantsuse, saksa, hispaania, itaalia, portugali, hollandi, vene, hiina, jaapani, korea, araabia ja hindi keeli.

Nende omadustega on Mistral Large suurepärane:
- *Andmete rikastatud genereerimiseks (RAG)* - tänu suuremale konteksti aknale
- *Funktsioonikõnedele* - see mudel toetab natiivset funktsioonikõnede tegemist, mis võimaldab integreerimist väliste tööriistade ja API-dega. Neid kõnesid saab teha nii paralleelselt kui ka järjestikku.
- *Koodigeneratsiooniks* - mudel on väga hea Python-, Java-, TypeScript- ja C++-koodi genereerimisel.

### RAG näide, kasutades Mistral Large 2 mudelit

Selles näites kasutame Mistral Large 2 mudelit, et teostada RAG mustrit tekstidokumendi põhjal. Küsimus on kirjutatud korea keeles ja küsib autori tegevuste kohta enne kolledžit.

See kasutab Cohere Embeddings mudelit, et luua tekstidokumendi ja küsimuse manuseid. Selle näite puhul kasutatakse faiss Python paketti vektorpoodina.

Mudelitele saadetud sisend sisaldab nii küsimusi kui ka leitud tekstiosasid, mis on küsimusega sarnased. Mudel annab seejärel loomuliku keele vastuse.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # vahemaa, indeks
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

Mistral Small on veel üks mudel Mistrali perekonnas, kuuludes tipp/ettevõtte kategooriasse. Nime järgi on tegu väikese keelemudeliga (SLM). Mistral Small kasutamise eelised on:
- Kuluefektiivsus võrreldes Mistral LLM-idega nagu Mistral Large ja NeMo - 80% hinnalangus
- Madal latentsus - kiirem reageerimine võrreldes Mistral LLM-idega
- Paindlikkus - saab juurutada erinevates keskkondades, nõudes vähem ressursse.

Mistral Small sobib hästi:
- Tekstipõhisteks ülesanneteks nagu kokkuvõtete koostamine, meeleolu analüüs ja tõlkimine.
- Rakendusteks, kus esitatakse sagedasi päringuid tänu selle kuluefektiivsusele
- Madala latentsusega koodülesanneteks nagu koodi ülevaatus ja soovitused

## Mistral Small ja Mistral Large võrdlus

Et näha latentsuse erinevusi Mistral Small ja Large vahel, käivitage alljärgnevad lahtrid.

Te peaksite nägema reageerimisajade erinevust 3-5 sekundi vahel. Pöörake ka tähelepanu vastuse pikkusele ja stiilile sama sisendi puhul.

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

Võrreldes teiste kahe mudeliga, mis selles õppetükis käsitletud, on Mistral NeMo ainus tasuta mudel, millel on Apache2 litsents.

Seda peetakse uuenduseks varasemale Mistrali avatud lähtekoodiga LLM-ile, Mistral 7B-le.

Mõned muud NeMo mudeli omadused on:

- *Tõhusam tokeniseerimine:* See mudel kasutab Tekkeni tokeniseerijat, mitte sagedamini kasutatavat tiktokenit. See võimaldab paremat tootlikkust mitmete keelte ja koodide puhul.

- *Täpsustamine:* Baasmudel on saadaval täpsustamiseks. See võimaldab suuremat paindlikkust kasutusjuhtudeks, kus võib vaja minna mudeli täpsustamist.

- *Natiivne funktsioonikõne* - Nagu Mistral Large, on seda mudelit õpetatud funktsioonikõnete teostamiseks. See teeb sellest ühe esimestest avatud lähtekoodiga mudelitest, mis seda toetab.

### Tokeniseerijate võrdlus

Selles näites vaatleme, kuidas Mistral NeMo tokeniseerimist teostab võrreldes Mistral Large mudeliga.

Mõlemad näited kasutavad sama sisendit, kuid te peaksite nägema, et NeMo tagastab vähem tokeneid kui Mistral Large.

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

# Laadi Mistrali tokeniseerija

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

# Laadi Mistrali tokenisaator

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


## Õppimine ei lõpe siin, jätkake teekonda

Pärast selle õppetüki lõpetamist vaadake meie [Generative AI õppimiskogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste tõstmist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun pidage meeles, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument oma emakeeles tuleks pidada autoriteetseks allikaks. Tähtsa info puhul soovitatakse kasutada professionaalse inimese tõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->