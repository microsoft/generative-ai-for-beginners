# Izgradnja s Mistral modelima 

## Uvod 

Ova lekcija će pokriti: 
- Istraživanje različitih Mistral modela 
- Razumijevanje slučajeva upotrebe i scenarija za svaki model 
- Istraživanje primjera koda koji pokazuju jedinstvene značajke svakog modela. 

## Mistral modeli 

U ovoj lekciji istražit ćemo 3 različita Mistral modela: 
**Mistral Large**, **Mistral Small** i **Mistral Nemo**. 

Svaki od ovih modela dostupan je besplatno na [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kod u ovom bilježničkom dokumentu koristiće ove modele za pokretanje koda.

> **Napomena:** GitHub modeli se povlače krajem srpnja 2026. Više detalja o korištenju [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiziranje s AI modelima potražite ovdje. 


## Mistral Large 2 (2407)
Mistral Large 2 je trenutno vodeći model iz Mistrala i dizajniran je za poduzeća. 

Model je nadogradnja originalnog Mistral Large modela nudi 
-  Veće kontekstno okno - 128k naspram 32k 
-  Bolju izvedbu na zadacima iz matematike i programiranja - 76,9% prosječne točnosti u odnosu na 60,4% 
-  Povećanu višekulturnu izvedbu - jezici uključuju: engleski, francuski, njemački, španjolski, talijanski, portugalski, nizozemski, ruski, kineski, japanski, korejski, arapski i hindijski.

S ovim značajkama, Mistral Large odlično obavlja 
- *Generiranje s podrškom za dohvaćanje podataka (RAG)* - zbog većeg kontekstnog okna
- *Pozivanje funkcija* - ovaj model ima ugrađeno pozivanje funkcija što omogućuje integraciju s vanjskim alatima i API-jima. Ovi pozivi mogu se izvršavati paralelno ili jedan za drugim u sekvencijalnom redoslijedu. 
- *Generiranje koda* - ovaj model briljira u generiranju Python, Java, TypeScript i C++ koda. 

### Primjer RAG-a koristeći Mistral Large 2 

U ovom primjeru koristimo Mistral Large 2 za izvođenje RAG obrasca nad tekstualnim dokumentom. Pitanje je napisano na korejskom i pita o autorovim aktivnostima prije fakulteta. 

Koristi Cohere Embeddings model za stvaranje ugradbi (embeddinga) dokumenta kao i pitanja. Za ovaj primjer koristi Python paket faiss kao vektor-store. 

Upit poslan Mistral modelu uključuje i pitanja i dohvaćene dijelove teksta slične pitanju. Model zatim daje odgovor na prirodnom jeziku. 

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

# Nabavite ih s "Pregled" stranice vašeg Microsoft Foundry projekta
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
Mistral Small je još jedan model iz Mistral obitelji u kategoriji premier/poduzeća. Kao što ime sugerira, ovaj model je Mali jezični model (SLM). Prednosti korištenja Mistral Small su: 
- Ušteda troškova u usporedbi s Mistral LLM-ovima poput Mistral Large i NeMo - smanjenje cijene za 80%
- Niska latencija - brži odgovor u usporedbi s Mistral LLM-ovima
- Fleksibilan - može se implementirati u različitim okruženjima s manje ograničenja potrebnih resursa. 


Mistral Small je odličan za: 
- Zadatke temeljene na tekstu poput sažimanja, analize sentimenta i prevođenja. 
- Aplikacije gdje se učestalo šalju zahtjevi zbog svoje isplativosti 
- Zadatke koda s niskom latencijom poput pregleda i prijedloga koda 

## Usporedba Mistral Small i Mistral Large 

Za prikaz razlika u latenciji između Mistral Small i Large, pokrenite donje ćelije. 

Trebali biste vidjeti razlikuju u vremenima odgovora od 3-5 sekundi. Također obratite pažnju na duljinu i stil odgovora na isti upit.  

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

U usporedbi s druga dva modela razmatrana u ovoj lekciji, Mistral NeMo je jedini besplatni model s Apache2 licencom. 

Smatra se nadogradnjom ranijeg open-source LLM-a iz Mistrala, Mistral 7B. 

Neke druge značajke NeMo modela su: 

- *Efikasnija tokenizacija:* Ovaj model koristi Tekken tokenizer umjesto češće korištenog tiktokena. To omogućava bolju performansu na većem broju jezika i koda. 

- *Finetuning:* Bazni model dostupan je za fino podešavanje. To pruža veću fleksibilnost za slučajeve upotrebe gdje je fino podešavanje potrebno. 

- *Ugrađeno Pozivanje funkcija* - Kao i Mistral Large, ovaj model je treniran na pozivanju funkcija. To ga čini jedinstvenim kao jednim od prvih open-source modela s tom mogućnošću. 


### Usporedba Tokenizera 

U ovom primjeru gledat ćemo kako Mistral NeMo obrađuje tokenizaciju u usporedbi s Mistral Large modelom. 

Oba primjera koriste isti upit, ali trebali biste vidjeti da NeMo vraća manje tokena nego Mistral Large. 

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

# Prebroji broj tokena
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

Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->