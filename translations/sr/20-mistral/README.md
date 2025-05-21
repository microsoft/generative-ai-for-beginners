<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:03:33+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sr"
}
-->
# Izgradnja sa Mistral Modelima

## Uvod

Ova lekcija pokriva:
- Istraživanje različitih Mistral modela
- Razumevanje slučajeva upotrebe i scenarija za svaki model
- Primeri koda koji pokazuju jedinstvene karakteristike svakog modela.

## Mistral modeli

U ovoj lekciji ćemo istražiti 3 različita Mistral modela: **Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Svaki od ovih modela je dostupan besplatno na Github Model tržištu. Kod u ovom beležniku će koristiti ove modele za pokretanje koda. Ovde su dodatni detalji o korišćenju Github Modela za [prototipiziranje sa AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodeći model iz Mistrala i dizajniran je za poslovnu upotrebu.

Model je unapređenje originalnog Mistral Large sa:
- Većim kontekstualnim prozorom - 128k naspram 32k
- Boljom performansom na matematičkim i programerskim zadacima - 76.9% prosečne tačnosti naspram 60.4%
- Povećanom višelingvalnom performansom - jezici uključuju: engleski, francuski, nemački, španski, italijanski, portugalski, holandski, ruski, kineski, japanski, korejski, arapski i hindi.

Sa ovim karakteristikama, Mistral Large se ističe u:
- *Generaciji sa poboljšanim preuzimanjem (RAG)* - zbog većeg kontekstualnog prozora
- *Pozivanju funkcija* - ovaj model ima nativno pozivanje funkcija što omogućava integraciju sa spoljnim alatima i API-jevima. Ova pozivanja mogu biti izvršena paralelno ili jedno nakon drugog u sekvencijalnom redu.
- *Generaciji koda* - ovaj model se ističe u generaciji za Python, Java, TypeScript i C++.

### RAG primer korišćenjem Mistral Large 2

U ovom primeru koristimo Mistral Large 2 za pokretanje RAG šablona preko teksta. Pitanje je napisano na korejskom i postavlja se o aktivnostima autora pre fakulteta.

Koristi Cohere Embeddings Model za kreiranje embedinga tekstualnog dokumenta kao i pitanja. Za ovaj primer koristi faiss Python paket kao vektorsku prodavnicu.

Upit poslat Mistral modelu uključuje i pitanja i preuzete delove koji su slični pitanju. Model zatim pruža odgovor na prirodnom jeziku.

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
Mistral Small je još jedan model iz Mistral porodice modela u premier/enterprise kategoriji. Kao što ime sugeriše, ovaj model je Mali Jezički Model (SLM). Prednosti korišćenja Mistral Small su:
- Ušteda troškova u poređenju sa Mistral LLM-ovima poput Mistral Large i NeMo - 80% niža cena
- Niska latencija - brži odgovor u poređenju sa Mistralovim LLM-ovima
- Fleksibilnost - može biti implementiran u različitim okruženjima sa manje ograničenja na potrebne resurse.

Mistral Small je odličan za:
- Zadaci bazirani na tekstu kao što su sažimanje, analiza sentimenta i prevođenje.
- Aplikacije gde se često prave zahtevi zbog njegove isplativosti
- Zadaci sa niskom latencijom kao što su pregled i sugestije koda

## Poređenje Mistral Small i Mistral Large

Da biste pokazali razlike u latenciji između Mistral Small i Large, pokrenite sledeće ćelije.

Trebalo bi da vidite razliku u vremenu odgovora između 3-5 sekundi. Takođe obratite pažnju na dužinu i stil odgovora na isti upit.

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

U poređenju sa druga dva modela diskutovana u ovoj lekciji, Mistral NeMo je jedini besplatni model sa Apache2 licencom.

Smatra se unapređenjem ranijeg open source LLM-a iz Mistrala, Mistral 7B.

Neke druge karakteristike NeMo modela su:

- *Efikasnija tokenizacija:* Ovaj model koristi Tekken tokenizator umesto češće korišćenog tiktokena. Ovo omogućava bolje performanse za više jezika i kodova.

- *Fino podešavanje:* Osnovni model je dostupan za fino podešavanje. Ovo omogućava veću fleksibilnost za slučajeve upotrebe gde je fino podešavanje možda potrebno.

- *Nativno pozivanje funkcija* - Kao i Mistral Large, ovaj model je treniran na pozivanju funkcija. Ovo ga čini jedinstvenim kao jednim od prvih open source modela koji to radi.

### Poređenje tokenizatora

U ovom primeru ćemo pogledati kako Mistral NeMo rukuje tokenizacijom u poređenju sa Mistral Large.

Oba primera uzimaju isti upit, ali trebalo bi da vidite da NeMo vraća manje tokena u odnosu na Mistral Large.

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

## Učenje se ne zaustavlja ovde, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili da unapređujete svoje znanje o Generativnoj AI!

**Одричање од одговорности**:  
Овај документ је преведен користећи AI услугу превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални људски превод. Не сносимо одговорност за било каква погрешна разумевања или тумачења која произилазе из употребе овог превода.