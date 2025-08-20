<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:04:23+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s Mistral modelima

## Uvod

Ova lekcija obuhvaća:  
- Istraživanje različitih Mistral modela  
- Razumijevanje primjena i scenarija za svaki model  
- Primjere koda koji pokazuju jedinstvene značajke svakog modela.

## Mistral modeli

U ovoj lekciji istražit ćemo 3 različita Mistral modela:  
**Mistral Large**, **Mistral Small** i **Mistral Nemo**.

Svaki od ovih modela dostupan je besplatno na Github Model marketplaceu. Kod u ovom bilježniku koristi ove modele za izvođenje koda. Više detalja o korištenju Github modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) možete pronaći na navedenoj poveznici.

## Mistral Large 2 (2407)  
Mistral Large 2 trenutno je vodeći model iz Mistrala i namijenjen je za poslovnu upotrebu.

Model je nadogradnja originalnog Mistral Large modela i nudi:  
- Veće kontekstno okno - 128k naspram 32k  
- Bolje rezultate na zadacima iz matematike i programiranja - prosječna točnost 76,9% naspram 60,4%  
- Povećanu podršku za više jezika - uključujući: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindi.

Zahvaljujući ovim značajkama, Mistral Large se ističe u:  
- *Retrieval Augmented Generation (RAG)* - zbog većeg kontekstnog okna  
- *Pozivanje funkcija* - ovaj model ima ugrađenu podršku za pozivanje funkcija što omogućuje integraciju s vanjskim alatima i API-jima. Pozivi se mogu izvršavati paralelno ili jedan za drugim u sekvencijalnom redoslijedu.  
- *Generiranje koda* - model je posebno dobar u generiranju koda u Pythonu, Javi, TypeScriptu i C++.

### Primjer RAG-a koristeći Mistral Large 2

U ovom primjeru koristimo Mistral Large 2 za izvođenje RAG obrasca nad tekstualnim dokumentom. Pitanje je napisano na korejskom i odnosi se na aktivnosti autora prije fakulteta.

Koristi Cohere Embeddings Model za stvaranje urezaka (embeddings) teksta i pitanja. Za ovaj primjer koristi se Python paket faiss kao spremište vektora.

Prompt koji se šalje Mistral modelu uključuje i pitanje i dohvaćene dijelove teksta koji su slični pitanju. Model zatim daje odgovor na prirodnom jeziku.

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
Mistral Small je još jedan model iz Mistral obitelji, smješten u premier/enterprise kategoriju. Kao što ime sugerira, radi se o malom jezičnom modelu (SLM). Prednosti korištenja Mistral Small modela su:  
- Ušteda troškova u usporedbi s Mistral LLM-ovima poput Mistral Large i NeMo - smanjenje cijene za 80%  
- Niska latencija - brži odgovor u odnosu na Mistral LLM-ove  
- Fleksibilnost - može se implementirati u različitim okruženjima s manje ograničenja u pogledu potrebnih resursa.

Mistral Small je odličan za:  
- Tekstualne zadatke poput sažimanja, analize sentimenta i prevođenja  
- Aplikacije s čestim zahtjevima zbog svoje isplativosti  
- Zadace s niskom latencijom poput pregleda i prijedloga koda

## Usporedba Mistral Small i Mistral Large

Za prikaz razlika u latenciji između Mistral Small i Large modela, pokrenite dolje navedene ćelije.

Trebali biste primijetiti razliku u vremenu odgovora od 3 do 5 sekundi. Također obratite pažnju na duljinu i stil odgovora na isti prompt.

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

U usporedbi s ostala dva modela iz ove lekcije, Mistral NeMo je jedini besplatni model s Apache2 licencom.

Smatra se nadogradnjom ranijeg open source LLM modela iz Mistrala, Mistral 7B.

Neke dodatne značajke NeMo modela su:

- *Efikasnija tokenizacija:* Ovaj model koristi Tekken tokenizer umjesto češće korištenog tiktokena. To omogućuje bolje performanse na više jezika i kodova.

- *Finetuning:* Osnovni model dostupan je za fino podešavanje, što pruža veću fleksibilnost za slučajeve gdje je potrebno dodatno treniranje.

- *Nativno pozivanje funkcija* - Kao i Mistral Large, ovaj model je treniran za pozivanje funkcija. To ga čini jedinstvenim kao jedan od prvih open source modela s tom mogućnošću.

### Usporedba tokenizera

U ovom primjeru pogledat ćemo kako Mistral NeMo obrađuje tokenizaciju u usporedbi s Mistral Large modelom.

Oba primjera koriste isti prompt, ali trebali biste primijetiti da NeMo vraća manje tokena u odnosu na Mistral Large.

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

## Učenje ne prestaje ovdje, nastavi svoje putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) i nastavi podizati svoje znanje o Generativnoj AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.