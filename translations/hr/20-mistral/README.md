<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:03:55+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s Mistral modelima

## Uvod

Ovaj lekcija će obuhvatiti:
- Istraživanje različitih Mistral modela
- Razumijevanje slučajeva korištenja i scenarija za svaki model
- Primjeri koda pokazuju jedinstvene značajke svakog modela.

## Mistral modeli

U ovoj lekciji istražujemo 3 različita Mistral modela: **Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Svaki od ovih modela dostupan je besplatno na tržištu modela Github. Kod u ovom bilježniku koristit će ove modele za pokretanje koda. Ovdje su dodatni detalji o korištenju Github modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 trenutno je vodeći model od Mistrala i dizajniran je za poslovnu upotrebu.

Model je nadogradnja originalnog Mistral Large modela i nudi:
- Veći kontekstni prozor - 128k naspram 32k
- Bolje performanse u matematičkim i koderskim zadacima - prosječna točnost 76.9% naspram 60.4%
- Povećane višelingvalne performanse - jezici uključuju: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindi.

S ovim značajkama, Mistral Large izvrsno se snalazi u:
- *Generaciji uz pomoć pretraživanja (RAG)* - zahvaljujući većem kontekstnom prozoru
- *Pozivanju funkcija* - ovaj model ima nativno pozivanje funkcija koje omogućava integraciju s vanjskim alatima i API-ima. Pozivi se mogu obavljati paralelno ili jedan za drugim u sekvencijalnom redoslijedu.
- *Generiranju koda* - ovaj model izvrsno generira Python, Java, TypeScript i C++ kod.

### RAG primjer koristeći Mistral Large 2

U ovom primjeru koristimo Mistral Large 2 za pokretanje RAG obrasca preko tekstualnog dokumenta. Pitanje je napisano na korejskom i pita o aktivnostima autora prije fakulteta.

Koristi Cohere Embeddings Model za kreiranje ugrađivanja tekstualnog dokumenta kao i pitanja. Za ovaj primjer koristi faiss Python paket kao spremište vektora.

Upit poslan Mistral modelu uključuje i pitanja i dohvaćene dijelove koji su slični pitanju. Model tada pruža odgovor na prirodnom jeziku.

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
Mistral Small je još jedan model u Mistral obitelji modela u kategoriji premier/enterprise. Kao što ime sugerira, ovaj model je mali jezični model (SLM). Prednosti korištenja Mistral Small su:
- Ušteda troškova u usporedbi s Mistral LLM-ima poput Mistral Large i NeMo - pad cijene od 80%
- Niska latencija - brži odgovor u usporedbi s Mistralovim LLM-ima
- Fleksibilnost - može se implementirati u različitim okruženjima s manje ograničenja na potrebne resurse.

Mistral Small je odličan za:
- Tekstualne zadatke poput sažimanja, analize sentimenta i prevođenja.
- Aplikacije gdje se često šalju zahtjevi zbog njegove isplativosti
- Zadaci koda s niskom latencijom poput pregleda i prijedloga koda

## Usporedba Mistral Small i Mistral Large

Za prikaz razlika u latenciji između Mistral Small i Large, pokrenite dolje navedene ćelije.

Trebali biste vidjeti razliku u vremenima odgovora između 3-5 sekundi. Također obratite pažnju na duljinu i stil odgovora za isti upit.

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

U usporedbi s ostala dva modela koja su raspravljena u ovoj lekciji, Mistral NeMo je jedini besplatni model s Apache2 licencom.

Gleda se kao nadogradnja ranijeg open source LLM-a od Mistrala, Mistral 7B.

Neke druge značajke NeMo modela su:

- *Efikasnija tokenizacija:* Ovaj model koristi Tekken tokenizer umjesto češće korištenog tiktoken. To omogućava bolje performanse u više jezika i kodova.

- *Fino podešavanje:* Osnovni model dostupan je za fino podešavanje. To omogućava veću fleksibilnost za slučajeve korištenja gdje fino podešavanje može biti potrebno.

- *Nativno pozivanje funkcija* - Kao Mistral Large, ovaj model je treniran na pozivanju funkcija. To ga čini jedinstvenim kao jedan od prvih open source modela koji to čini.

### Usporedba tokenizera

U ovom primjeru, pogledat ćemo kako Mistral NeMo rukuje tokenizacijom u usporedbi s Mistral Large.

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

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.