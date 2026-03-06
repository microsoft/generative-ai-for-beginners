# Kūrimas su Mistral modeliais

## Įvadas

Ši pamoka apims:  
- Skirtingų Mistral modelių tyrinėjimą  
- Supratimą apie kiekvieno modelio naudojimo atvejus ir scenarijus  
- Kodo pavyzdžių, rodančių kiekvieno modelio unikalias savybes, tyrinėjimą.

## Mistral modeliai

Šioje pamokoje tyrinėsime 3 skirtingus Mistral modelius:  
**Mistral Large**, **Mistral Small** ir **Mistral Nemo**.

Kiekvienas iš šių modelių yra nemokamai prieinamas GitHub Model rinkoje. Šio užrašų knygutės kodas naudos šiuos modelius vykdymui. Daugiau informacijos apie GitHub Modelių naudojimą [kuriant su AI modeliais](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) rasite nuorodoje.

## Mistral Large 2 (2407)  
Mistral Large 2 šiuo metu yra pagrindinis Mistral modelis ir skirtas verslo naudojimui.

Modelis yra patobulinimas prie originalaus Mistral Large, siūlantis  
- Didesnį konteksto langą – 128k prieš 32k  
- Geresnį našumą matematikos ir programavimo užduotyse – 76,9 % vidutinė tikslumas prieš 60,4 %  
- Padidintą daugiakalbį našumą – kalbos apima: anglų, prancūzų, vokiečių, ispanų, italų, portugalų, olandų, rusų, kinų, japonų, korėjiečių, arabų ir hindi.

Su šiomis savybėmis Mistral Large pasižymi  
- *Retrieval Augmented Generation (RAG)* – dėl didesnio konteksto lango  
- *Funkcijų kvietimu* – šis modelis turi gimtąjį funkcijų kvietimą, leidžiantį integruotis su išorinėmis priemonėmis ir API. Šie kvietimai gali būti atliekami tiek lygiagrečiai, tiek vienas po kito seka.  
- *Kodo generavimu* – modelis puikiai veikia generuojant Python, Java, TypeScript ir C++ kodą.

### RAG pavyzdys naudojant Mistral Large 2

Šiame pavyzdyje naudojame Mistral Large 2, kad vykdytume RAG modelį teksto dokumentui. Klausimas yra parašytas korėjiečių kalba ir klausia apie autoriaus veiklas prieš kolegiją.

Jis naudoja Cohere embeddings modelį, kad sukurtų įterpimus (embeddings) teksto dokumentui ir klausimui. Šiame pavyzdyje naudojama faiss Python biblioteka kaip vektorių saugykla.

Pranešimas, siunčiamas Mistral modeliui, apima tiek klausimus, tiek panašias į klausimą rastas teksto dalis. Modelis tada pateikia natūralios kalbos atsakymą.

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
Mistral Small yra dar vienas modelis Mistral modelių šeimoje, priklausantis premier/enterprise kategorijai. Kaip rodo pavadinimas, šis modelis yra mažas kalbos modelis (SLM). Pagrindiniai Mistral Small pranašumai yra:  
- Sąnaudų taupymas, palyginti su Mistral didžiaisiais modeliais, tokiais kaip Mistral Large ir NeMo – 80 % kainos sumažėjimas  
- Mažas delsimas – greitesnis atsakymas, palyginti su Mistral LLM  
- Lankstumas – gali būti diegiamas skirtingose aplinkose su mažesniais reikalavimais resursams.

Mistral Small puikiai tinka:  
- Teksto pagrindu atliktoms užduotims, tokioms kaip santraukos sudarymas, nuotaikų analizė ir vertimas  
- Programėlėms, kuriose dažnai atliekami užklausimai dėl kaštų efektyvumo  
- Žemo delsimo kodo užduotims, tokioms kaip apžvalga ir kodo pasiūlymai

## Mistral Small ir Mistral Large palyginimas

Norėdami parodyti delsimo skirtumus tarp Mistral Small ir Large, vykdykite žemiau esančias ląsteles.

Turėtumėte pamatyti atsakymo laiko skirtumą nuo 3 iki 5 sekundžių. Taip pat atkreipkite dėmesį į atsakymų ilgį ir stilių pagal tą patį užklausą.

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

Lyginant su kitais dviem šiame pamokoje aptartais modeliais, Mistral NeMo yra vienintelis nemokamas modelis su Apache2 licencija.

Jis vertinamas kaip atnaujinimas ankstesniam atvirojo kodo LLM iš Mistral, Mistral 7B.

Kitos NeMo modelio savybės:

- *Efektyvesnė tokenizacija:* Šis modelis naudoja Tekken tokenizatorių, o ne dažniausiai naudojamą tiktoken. Tai leidžia geriau veikti su daugiau kalbų ir kodo.

- *Finetuning:* Bazinis modelis prieinamas derinimui (finetune). Tai suteikia didesnį lankstumą atvejams, kai reikalingas derinimas.

- *Gimtasis funkcijų kvietimas* – kaip ir Mistral Large, šis modelis buvo apmokytas funkcijų kvietimui. Tai daro jį unikaliu, kaip vieną iš pirmųjų atvirojo kodo modelių, turinčių tokią funkciją.

### Tokenizatorių palyginimas

Šiame pavyzdyje pažvelgsime, kaip Mistral NeMo atlieka tokenizaciją, palyginti su Mistral Large.

Abu pavyzdžiai naudoja tą patį užklausą, bet turėtumėte matyti, kad NeMo grąžina mažiau tokenų nei Mistral Large.

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

# Įkelkite Mistral žodžių skaidytuvą

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Atlikite žinučių sąrašo tokenizavimą
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

# Įkelkite Mistral žodžių skaidyklę

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Paskaidykite žinučių sąrašą į žodžius
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

Baigę šią pamoką, apsilankykite mūsų [Generatyvios AI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau keltumėte savo žinias apie Generatyvią AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar klaidų interpretuotes, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->