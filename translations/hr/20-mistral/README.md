# Izgradnja s Mistral modelima

## Uvod

Ova lekcija će obuhvatiti:
- Istraživanje različitih Mistral modela
- Razumijevanje primjena i scenarija za svaki model
- Istraživanje primjera koda koji prikazuju jedinstvene značajke svakog modela.

## Mistral modeli

U ovoj lekciji istražit ćemo 3 različita Mistral modela:
**Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Svaki od ovih modela je dostupan besplatno na GitHub Model marketplace-u. Kod u ovom bilježniku koristiće ove modele za pokretanje koda. Evo više detalja o korištenju GitHub Modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).


## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodeći model tvrtke Mistral i namijenjen je za poslovnu upotrebu.

Model je nadogradnja na originalni Mistral Large koji nudi
- Veće kontekstno područje - 128k u odnosu na 32k
- Bolje performanse na zadacima iz matematike i programiranja - 76,9% prosječne točnosti u odnosu na 60,4%
- Povećane višelingvalne performanse - jezici uključuju: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindi.

S ovim značajkama, Mistral Large briljira u
- *Generiranju uz podršku pretraživanja (RAG)* - zbog većeg kontekstnog područja
- *Pozivanju funkcija* - ovaj model ima izvorno pozivanje funkcija što omogućava integraciju s vanjskim alatima i API-jima. Pozivi se mogu vršiti paralelno ili jedan za drugim u sekvencijalnom redoslijedu.
- *Generiranju koda* - ovaj model briljira u generiranju Python, Java, TypeScript i C++ koda.

### RAG primjer korištenjem Mistral Large 2

U ovom primjeru koristimo Mistral Large 2 za izvođenje RAG šablona preko tekstualnog dokumenta. Pitanje je napisano na korejskom i odnosi se na aktivnosti autora prije fakulteta.

Koristi Cohere Embeddings model za stvaranje uputa tekstualnog dokumenta kao i pitanja. Za ovaj primjer koristi faiss Python paket kao spremište vektora.

Uput koji se šalje Mistral modelu uključuje i pitanja i dohvaćene dijelove koji su slični pitanju. Model zatim daje odgovor u prirodnom jeziku.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # udaljenost, indeks
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
Mistral Small je još jedan model iz Mistral obitelji modela u premijernoj/poslovnoj kategoriji. Kao što ime sugerira, ovaj model je mali jezični model (SLM). Prednosti korištenja Mistral Small su:
- Ušteda troškova u odnosu na Mistral LLM poput Mistral Large i NeMo - pad cijene od 80%
- Niska latencija - brži odgovor u odnosu na Mistral LLM-ove
- Fleksibilnost - može se implementirati u različitim okruženjima s manje ograničenja u potrebnim resursima.

Mistral Small je izvrstan za:
- Zadace temeljene na tekstu kao što su sažimanje, analiza sentimenta i prevođenje.
- Aplikacije gdje se često šalju zahtjevi zbog isplativosti
- Zadace niske latencije poput pregleda i prijedloga koda

## Usporedba Mistral Small i Mistral Large

Kako biste vidjeli razlike u latenciji između Mistral Small i Large, pokrenite donje ćelije.

Trebali biste vidjeti razliku u vremenima odgovora između 3-5 sekundi. Također obratite pažnju na dužinu i stil odgovora na isti upit.

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

U usporedbi s druga dva modela obrađena u ovoj lekciji, Mistral NeMo je jedini besplatni model s Apache2 licencom.

Gleda se kao nadogradnja ranijeg open source LLM iz Mistral-a, Mistral 7B.

Neke druge značajke NeMo modela su:

- *Učinkovitija tokenizacija:* Ovaj model koristi Tekken tokenizer umjesto češće korištenog tiktoken. To omogućuje bolje performanse za više jezika i kodova.

- *Finetuning:* Osnovni model je dostupan za fino podešavanje. To omogućuje veću fleksibilnost za primjene gdje je fino podešavanje potrebno.

- *Izvorno pozivanje funkcija* - Kao i Mistral Large, ovaj model je treniran za pozivanje funkcija. Time je jedinstven kao jedan od prvih open source modela koji to podržava.

### Usporedba Tokenizera

U ovom primjeru vidjet ćemo kako Mistral NeMo obrađuje tokenizaciju u usporedbi s Mistral Large.

Oba primjera koriste isti upit, no trebali biste vidjeti da NeMo vraća manje tokena nego Mistral Large.

```bash
pip install mistral-common
```

```python 
# Uvezi potrebne pakete:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Učitaj Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniziraj popis poruka
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

# Izbroji broj tokena
print(len(tokens))
```

```python
# Uvezi potrebne pakete:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Učitaj Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniziraj popis poruka
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

# Izbroji broj tokena
print(len(tokens))
```

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje generativne umjetne inteligencije](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili usavršavati svoje znanje o generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge prijevoda [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili krive interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->