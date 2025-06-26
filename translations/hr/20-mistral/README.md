<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:23:24+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s Mistral Modelima

## Uvod

Ova lekcija će pokriti:
- Istraživanje različitih Mistral modela
- Razumijevanje slučajeva korištenja i scenarija za svaki model
- Primjeri koda pokazuju jedinstvene značajke svakog modela.

## Mistral modeli

U ovoj lekciji istražujemo 3 različita Mistral modela: **Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Svaki od ovih modela dostupan je besplatno na tržištu modela Github. Kod u ovom bilježniku koristi ove modele za pokretanje koda. Evo više detalja o korištenju Github modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 trenutno je vodeći model iz Mistrala i dizajniran je za poslovnu upotrebu.

Model je nadogradnja originalnog Mistral Largea i nudi:
- Veći kontekstualni prozor - 128k naspram 32k
- Bolju izvedbu na matematičkim i koderskim zadacima - prosječna točnost 76,9% naspram 60,4%
- Povećanu višelingvalnu izvedbu - jezici uključuju: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindi.

S ovim značajkama, Mistral Large se ističe u:
- *Retrieval Augmented Generation (RAG)* - zbog većeg kontekstualnog prozora
- *Pozivanje funkcija* - ovaj model ima nativno pozivanje funkcija što omogućava integraciju s vanjskim alatima i API-jima. Ovi pozivi mogu se izvršiti paralelno ili jedan za drugim u sekvencijalnom redu.
- *Generiranje koda* - ovaj model se ističe u generiranju Python, Java, TypeScript i C++ koda.

### RAG primjer koristeći Mistral Large 2

U ovom primjeru, koristimo Mistral Large 2 za pokretanje RAG uzorka preko tekstualnog dokumenta. Pitanje je napisano na korejskom i pita o aktivnostima autora prije fakulteta.

Koristi Cohere Embeddings Model za kreiranje ugrađenih vrijednosti tekstualnog dokumenta kao i pitanja. Za ovaj uzorak koristi faiss Python paket kao vektorsku pohranu.

Upit poslan Mistral modelu uključuje i pitanja i dohvaćene dijelove koji su slični pitanju. Model tada daje odgovor na prirodnom jeziku.

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
Mistral Small je još jedan model u obitelji Mistral modela pod kategorijom premier/enterprise. Kao što ime implicira, ovaj model je Mali Jezični Model (SLM). Prednosti korištenja Mistral Small su da je:
- Ušteda troškova u usporedbi s Mistral LLM-ima kao što su Mistral Large i NeMo - pad cijene od 80%
- Niska latencija - brži odgovor u usporedbi s Mistralovim LLM-ima
- Fleksibilnost - može se implementirati u različitim okruženjima s manje ograničenja na potrebne resurse.

Mistral Small je odličan za:
- Zadaci temeljeni na tekstu kao što su sažimanje, analiza sentimenta i prevođenje.
- Aplikacije gdje se često postavljaju zahtjevi zbog njegove isplativosti
- Zadaci kodiranja s niskom latencijom kao što su pregled i prijedlozi koda

## Usporedba Mistral Small i Mistral Large

Kako bismo pokazali razlike u latenciji između Mistral Small i Large, pokrenite donje ćelije.

Trebali biste vidjeti razliku u vremenima odgovora između 3-5 sekundi. Također primijetite duljinu i stil odgovora na isti upit.

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

U usporedbi s ostala dva modela raspravljena u ovoj lekciji, Mistral NeMo je jedini besplatni model s Apache2 licencom.

Smatra se nadogradnjom ranijeg open source LLM-a iz Mistrala, Mistral 7B.

Neke druge značajke NeMo modela su:

- *Učinkovitija tokenizacija:* Ovaj model koristi Tekken tokenizator umjesto češće korištenog tiktokena. To omogućava bolju izvedbu preko više jezika i koda.

- *Finetuning:* Osnovni model je dostupan za finetuning. To omogućava veću fleksibilnost za slučajeve korištenja gdje je finetuning možda potreban.

- *Nativno pozivanje funkcija* - Kao Mistral Large, ovaj model je treniran na pozivanju funkcija. To ga čini jednim od prvih open source modela koji to čine.

### Usporedba tokenizatora

U ovom uzorku, pogledat ćemo kako Mistral NeMo obrađuje tokenizaciju u usporedbi s Mistral Large.

Oba uzorka uzimaju isti upit, ali trebali biste vidjeti da NeMo vraća manje tokena u usporedbi s Mistral Large.

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

## Učenje se ne zaustavlja ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo za točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.