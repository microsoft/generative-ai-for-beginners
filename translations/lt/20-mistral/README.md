# Kūrimas su Mistral modeliais 

## Įvadas 

Ši pamoka apims: 
- Skirtingų Mistral modelių tyrinėjimą 
- Supratimą apie kiekvieno modelio panaudojimo atvejus ir scenarijus 
- Kodo pavyzdžius, kurie parodo kiekvieno modelio unikalius bruožus. 

## Mistral modeliai 

Šioje pamokoje mes nagrinėsime 3 skirtingus Mistral modelius: 
**Mistral Large**, **Mistral Small** ir **Mistral Nemo**. 

Visi šie modeliai yra nemokamai prieinami [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Šio užrašo kode bus naudojami šie modeliai vykdyti kodą.

> **Pastaba:** GitHub Models bus nutraukta 2026 m. liepos pabaigoje. Čia rasite daugiau informacijos apie [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) naudojimą dirbtinio intelekto modelių prototipavimui. 


## Mistral Large 2 (2407)
Mistral Large 2 šiuo metu yra pagrindinis Mistral modelis ir skirtas verslo naudojimui. 

Šis modelis yra atnaujinimas nuo originalaus Mistral Large, siūlantis 
- Didesnę konteksto langą - 128k prieš 32k 
- Geresnį našumą matematikos ir programavimo užduotyse - 76,9 % vidutinio tikslumo prieš 60,4 % 
- Pagerintą daugiakalbį veikimą - kalbos yra: anglų, prancūzų, vokiečių, ispanų, italų, portugalų, olandų, rusų, kinų, japonų, korėjiečių, arabų ir hindi.

Su šiomis savybėmis Mistral Large puikiai tinka 
- *Retrieval Augmented Generation (RAG)* - dėl didesnio konteksto lango
- *Funkcijų kvietimui* - šis modelis turi natyvų funkcijų kvietimą, leidžiantį integruotis su išoriniais įrankiais ir API. Šie kvietimai gali būti atliekami tiek lygiagrečiai, tiek vienas po kito sekančia tvarka. 
- *Kodo generavimui* - šis modelis puikiai generuoja Python, Java, TypeScript ir C++ kalbomis. 

### RAG pavyzdys naudojant Mistral Large 2 

Šiame pavyzdyje mes naudojame Mistral Large 2 vykdyti RAG modelio šabloną teksto dokumentui. Klausimas parašytas korėjiečių kalba ir klausia apie autoriaus veiklas prieš kolegiją. 

Jis naudoja Cohere Embeddings modelį, kad sukurtų teksto dokumento ir klausimo įterpimus. Šiame pavyzdyje naudojama faiss Python paketo vektorinė saugykla. 

Į Mistral modelį siunčiamas pranešimas apima tiek klausimus, tiek gautus kirstinius, panašius į klausimą. Modelis tada suteikia natūralios kalbos atsakymą. 

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

# Gaukite šiuos iš savo Microsoft Foundry projekto „Peržiūros“ puslapio
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
Mistral Small yra dar vienas modelis Mistral šeimoje, priklausantis premier/enterprise kategorijai. Kaip rodo pavadinimas, šis modelis yra mažas kalbos modelis (SLM). Privalumai naudojant Mistral Small yra: 
- Kainos taupymas lyginant su Mistral LLM kaip Mistral Large ir NeMo - 80 % kainos sumažėjimas
- Mažas delsimas - greitesnė reakcija lyginant su Mistral LLM
- Lankstumas - gali būti diegiamas įvairiose aplinkose su mažiau apribojimų dėl reikalaujamų resursų. 


Mistral Small puikiai tinka: 
- Teksto užduotims, tokioms kaip santraukos, jausmų analizė ir vertimas. 
- Programėlėms, kur dažnai siuntinėjami užklausimai dėl jos efektyvumo kainos atžvilgiu 
- Mažo delsimo kodo užduotims, tokioms kaip peržiūra ir kodo pasiūlymai 

## Mistral Small ir Mistral Large palyginimas 

Norėdami pamatyti delsimo skirtumus tarp Mistral Small ir Large, paleiskite žemiau esančias ląsteles. 

Turėtumėte matyti atsako laikų skirtumą 3-5 sekundžių. Taip pat atkreipkite dėmesį į atsakymų ilgį ir stilių su tuo pačiu užklausa.  

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

Lyginant su kitais dviem šioje pamokoje nagrinėtais modeliais, Mistral NeMo yra vienintelis nemokamas modelis su Apache2 licencija. 

Jis laikomas atnaujinimu ankstesniam Mistral atvirojo kodo LLM, Mistral 7B. 

Kai kurios kitos NeMo modelio savybės yra: 

- *Efektyvesnis tokenizavimas:* Šis modelis naudoja Tekken tokenizatorių, o ne labiau paplitusią tiktoken. Tai leidžia geriau veikti daugybėje kalbų ir kode. 

- *Tinkinimas:* Bazinis modelis yra prieinamas tinkinimui. Tai suteikia daugiau lankstumo atvejams, kai gali būti reikalingas tinkinimas. 

- *Natyvus funkcijų kvietimas* - Kaip ir Mistral Large, šis modelis buvo apmokytas funkcijų kvietimams. Tai daro jį unikaliu kaip vieną pirmųjų atviro kodo modelių, turinčių šią funkciją. 


### Tokenizatorių palyginimas 

Šiame pavyzdyje pamatysime, kaip Mistral NeMo atlieka tokenizaciją, lyginant su Mistral Large. 

Abu pavyzdžiai naudoja tą patį užklausą, tačiau turėtumėte matyti, kad NeMo grąžina mažiau tokenų nei Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Importuoti reikiamus paketus:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Įkelti Mistral žymeklių skirstytuvą

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Suskirstyti žinučių sąrašą į žymeklius
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

# Suskaičiuoti žymeklių skaičių
print(len(tokens))
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

# Užkraukite Mistral žodžių skaidytuvą

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Išskaidykite sąrašą žinučių į žodžius
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

# Suskaičiuokite žodžių skaičių
print(len(tokens))
```

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvinio DI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau tobulintumėte savo generatyvinio DI žinias!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->