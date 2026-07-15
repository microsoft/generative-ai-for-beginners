# Kūrimas su Mistral modeliais 

## Įvadas 

Šiame pamokoje aptarsime: 
- Skirtingų Mistral modelių tyrimą 
- Supratimą apie kiekvieno modelio panaudojimo atvejus ir scenarijus 
- Kodo pavyzdžių tyrimą, kurie demonstruoja kiekvieno modelio unikalias savybes. 

## Mistral modeliai 

Šioje pamokoje pažvelgsime į 3 skirtingus Mistral modelius: 
**Mistral Large**, **Mistral Small** ir **Mistral Nemo**. 

Kiekvienas iš šių modelių yra nemokamai prieinamas [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) platformoje. Šioje užrašų knygoje naudojami šie modeliai kodui vykdyti.

> **Pastaba:** GitHub modeliai bus nutraukti 2026 metų liepos pabaigoje. Daugiau informacijos apie [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) naudojimą prototipavimui su AI modeliais rasite čia. 


## Mistral Large 2 (2407)
Mistral Large 2 šiuo metu yra pagrindinis Mistral modelis, sukurtas verslo naudojimui. 

Modelis yra patobulinimas originaliam Mistral Large, siūlant: 
- Didesnį konteksto langą - 128k prieš 32k 
- Geresnį našumą matematikos ir programavimo užduotyse - 76,9% vidutinis tikslumas prieš 60,4% 
- Padidintą daugiakalbį našumą - kalbos apima: anglų, prancūzų, vokiečių, ispanų, italų, portugalų, olandų, rusų, kinų, japonų, korėjiečių, arabų ir hindi.

Su šiomis savybėmis Mistral Large pasižymi 
- *Paieškos papildytą generavimą (RAG)* - dėl didesnio konteksto lango
- *Funkcijų kvietimą* - šis modelis turi gimtą funkcijų kvietimą, leidžiantį integraciją su išoriniais įrankiais ir API. Šie kvietimai gali būti atliekami tiek lygiagrečiai, tiek vienas po kito sekos tvarka. 
- *Kodo generavimą* - šis modelis puikiai veikia generuojant Python, Java, TypeScript ir C++ kodą. 

### RAG pavyzdys naudojant Mistral Large 2 

Šiame pavyzdyje naudojame Mistral Large 2 vykdyti RAG modelio šabloną teksto dokumentui. Klausimas yra parašytas korėjiečių kalba ir klausia apie autoriaus veiklas prieš koledžą. 

Naudojamas Cohere Embeddings modelis kuriant teksto dokumento ir klausimo įterpimus. Šiame pavyzdyje kaip vektorinė saugykla naudojama faiss Python biblioteka. 

Į modelį siunčiamas prašymas apima tiek klausimus, tiek gautus fragmentus, kurie yra panašūs į klausimą. Tada modelis pateikia natūralios kalbos atsakymą. 

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

# Gaukite juos iš savo Microsoft Foundry projekto "Apžvalga" puslapio
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # atstumas, indeksas
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
Mistral Small yra kitas modelis iš Mistral šeimos pagal premier/verslo kategoriją. Kaip rodo pavadinimas, tai yra Mažas Kalbos Modelis (SLM). Naudos naudojant Mistral Small yra tokios: 
- Kainų taupymas palyginti su Mistral LLM, tokiais kaip Mistral Large ir NeMo - kaina sumažėja 80%
- Mažas vėlinimas - greitesnis atsakymas palyginti su Mistral LLM
- Lankstus - gali būti diegiamas skirtingose aplinkose su mažesniais ribojimais reikalaujamų išteklių atžvilgiu. 


Mistral Small puikiai tinka: 
- Tekstinėms užduotims, tokioms kaip santraukos rengimas, nuotaikos analizė ir vertimas. 
- Programėlėms, kur dažnai atliekami užklausimai dėl jo ekonomiškumo 
- Mažo vėlinimo kodo užduotims, tokioms kaip kodo peržiūra ir pasiūlymai 

## Mistral Small ir Mistral Large palyginimas 

Norėdami pamatyti vėlinimo skirtumus tarp Mistral Small ir Large, paleiskite žemiau esančias ląsteles. 

Turėtumėte pastebėti atsakymo laikų skirtumą nuo 3 iki 5 sekundžių. Taip pat atkreipkite dėmesį į atsakymų ilgius ir stilių to paties prašymo metu.  

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

Palyginti su dviem kitais šiame pamokoje aptartais modeliais, Mistral NeMo yra vienintelis nemokamas modelis su Apache2 licencija. 

Jis laikomas atnaujinimu ankstesniam atviro kodo Mistral modeliui, Mistral 7B. 

Kai kurios kitos NeMo modelio savybės yra: 

- *Efektyvesnė tokenizacija:* Šis modelis naudoja Tekken tokenizatorių vietoje dažniau naudojamo tiktoken. Tai leidžia geresnį našumą daugiau kalbų ir kodų atžvilgiu. 

- *Modelio tobulinimas (finetuning):* Bazinis modelis yra prieinamas tobulinimui. Tai suteikia daugiau lankstumo panaudojimo atvejams, kai gali prireikti tobulinimo. 

- *Gimtasis funkcijų kvietimas* - Kaip ir Mistral Large, šis modelis buvo išmokytas funkcijų kvietimui. Tai padaro jį unikaliu kaip vieną iš pirmųjų atviro kodo modelių, turinčių šią savybę. 


### Tokenizatorių palyginimas 

Šiame pavyzdyje pažiūrėsime, kaip Mistral NeMo tvarko tokenizaciją palyginti su Mistral Large. 

Abu pavyzdžiai naudoja tą patį prašymą, tačiau turėtumėte pastebėti, kad NeMo grąžina mažiau tokenų nei Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importuokite reikalingas paketas:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Įkelkite Mistral žodžių daliklių

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Išskaidykite žinučių sąrašą į žodžių dalis
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

# Suskaičiuokite žodžių dalių skaičių
print(len(tokens))
```

```python
# Importuoti reikalingas paketas:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Įkelti Mistral žodyną

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Sužodžiuoti žinučių sąrašą
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

# Suskaičiuoti žodžių skaičių
print(len(tokens))
```

## Mokymasis čia nesibaigia, tęskite kelionę

Pabaigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau kelkite savo generatyvios AI žinias!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->