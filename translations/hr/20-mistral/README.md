# Izgradnja s Mistral modelima 

## Uvod 

Ova lekcija će obuhvatiti: 
- Istraživanje različitih Mistral modela 
- Razumijevanje slučajeva uporabe i scenarija za svaki model 
- Istraživanje primjera koda koji pokazuju jedinstvene značajke svakog modela. 

## Mistral modeli 

U ovoj lekciji istražit ćemo 3 različita Mistral modela: 
**Mistral Large**, **Mistral Small** i **Mistral Nemo**. 

Svaki od ovih modela dostupan je besplatno na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kod u ovom bilježniku koristiće ove modele za izvršavanje koda.

> **Napomena:** GitHub Models se povlači krajem srpnja 2026. Više detalja o korištenju [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipove s AI modelima možete pronaći ovdje. 


## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodeći model od Mistrala i dizajniran je za poslovnu upotrebu. 

Model predstavlja nadogradnju na originalni Mistral Large nudeći 
-  Veći kontekstni prozor - 128k u odnosu na 32k 
-  Bolje performanse na zadacima iz matematike i kodiranja - prosječna točnost od 76,9% u odnosu na 60,4% 
-  Povećane višejezične performanse - jezici uključuju: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindi.

Sa ovim značajkama, Mistral Large izvrsno radi u 
- *Retrieval Augmented Generation (RAG)* - zbog većeg kontekstnog prozora
- *Pozivanje funkcija* - ovaj model ima ugrađeno pozivanje funkcija što omogućuje integraciju s vanjskim alatima i API-jima. Pozivi se mogu vršiti paralelno ili jedan za drugim u sekvencijalnom redu. 
- *Generiranje koda* - ovaj model izvrsno generira Python, Java, TypeScript i C++ kod. 

### Primjer RAG koristeći Mistral Large 2 

U ovom primjeru koristimo Mistral Large 2 da izvršimo RAG obrazac nad tekstualnim dokumentom. Pitanje je napisano na korejskom i odnosi se na aktivnosti autora prije fakulteta. 

Koristi Cohere Embeddings Model za stvaranje uembicija tekstualnog dokumenta kao i pitanja. Za ovaj uzorak koristi faiss Python paket kao spremište vektora. 

Upit poslan Mistral modelu uključuje i pitanja i dohvaćene dijelove koji su slični pitanju. Model zatim daje odgovor na prirodnom jeziku. 

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

# Nabavite ih sa stranice "Pregled" vašeg Microsoft Foundry projekta
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
Mistral Small je još jedan model iz obitelji Mistral modela u kategoriji premier/enterprise. Kao što ime kaže, ovaj model je mali jezični model (SLM). Prednosti korištenja Mistral Small su da je: 
- Ušteda troškova u usporedbi s Mistral LLM modelima poput Mistral Large i NeMo - pad cijene od 80%
- Niska latencija - brži odgovor u usporedbi s Mistral LLM-ovima
- Fleksibilan - može se implementirati u različita okruženja uz manje ograničenja na potrebne resurse. 


Mistral Small je odličan za: 
- Tekstualne zadatke poput sažimanja, analize sentimenta i prevođenja. 
- Aplikacije gdje se često šalju zahtjevi zbog relativno niskih troškova 
- Zadaci koda s niskom latencijom poput pregleda i prijedloga koda 

## Usporedba Mistral Small i Mistral Large 

Za prikaz razlika u latenciji između Mistral Small i Large, pokrenite donje ćelije. 

Trebali biste primijetiti razliku u vremenima odgovora između 3-5 sekundi. Također obratite pažnju na duljinu i stil odgovora kod istog upita.  

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

U usporedbi s preostala dva modela razmatrana u ovoj lekciji, Mistral NeMo je jedini besplatni model s Apache2 licencom. 

Smatra se nadogradnjom ranije otvorenog LLM modela Mistral 7B. 

Neke druge značajke NeMo modela su: 

- *Učinkovitija tokenizacija:* Ovaj model koristi Tekken tokenizer umjesto češće korištenog tiktoken. To omogućuje bolje performanse na više jezika i kodova. 

- *Fino podešavanje:* Osnovni model je dostupan za fino podešavanje. Ovo omogućuje veću fleksibilnost za slučajeve uporabe gdje je potrebno fino podešavanje. 

- *Izvorno pozivanje funkcija* - Kao i Mistral Large, ovaj model je treniran za pozivanje funkcija. To ga čini jedinstvenim kao jednim od prvih open source modela koji to podržavaju. 


### Usporedba tokenizer-a 

U ovom uzorku pogledat ćemo kako Mistral NeMo obrađuje tokenizaciju u usporedbi s Mistral Large. 

Oba uzorka uzimaju isti upit, no trebali biste vidjeti da NeMo vraća manje tokena nego Mistral Large. 

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

# Tokeniziraj listu poruka
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

# Učitaj Mistral tokenizator

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokeniziraj listu poruka
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

## Učenje ovdje ne prestaje, nastavite putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili usavršavati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->