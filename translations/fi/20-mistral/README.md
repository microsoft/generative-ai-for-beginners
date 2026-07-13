# Rakentaminen Mistral-malleilla 

## Johdanto 

Tässä oppitunnissa käsitellään: 
- Eri Mistral-mallien tutkiminen 
- Kunkin mallin käyttötarkoitusten ja käyttöskenaarioiden ymmärtäminen 
- Koodiesimerkkien tutkiminen, jotka näyttävät kunkin mallin ainutlaatuiset ominaisuudet. 

## Mistral-mallit 

Tässä oppitunnissa tutustumme kolmeen eri Mistral-malliin: 
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**. 

Jokainen näistä malleista on saatavilla ilmaiseksi [Microsoft Foundry Modelsissa](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Tässä muistikirjassa oleva koodi käyttää näitä malleja ajamiseen.

> **Huom:** GitHub Models poistuu käytöstä heinäkuun 2026 lopussa. Tässä on lisää tietoa [Microsoft Foundry Modelsin](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) käyttämisestä AI-mallien prototyypittämiseen. 


## Mistral Large 2 (2407)
Mistral Large 2 on tällä hetkellä Mistralin lipunmiesmalli ja on suunniteltu yrityskäyttöön. 

Malli on päivitys alkuperäiseen Mistral Largeen tarjoamalla 
- Suurempi kontekstikehys – 128k vs 32k 
- Parempi suorituskyky matematiikan ja ohjelmointitehtävissä – 76,9 % keskimääräinen tarkkuus vs 60,4 % 
- Parantunut monikielinen suorituskyky – kielet sisältävät: englanti, ranska, saksa, espanja, italia, portugali, hollanti, venäjä, kiina, japani, korea, arabia ja hindi.

Näiden ominaisuuksien ansiosta Mistral Large loistaa 
- *Retrieval Augmented Generation (RAG)* - suuremman kontekstikehyksen ansiosta
- *Funktiokutsut* - tässä mallissa on natiivifunktiokutsu, joka mahdollistaa integraation ulkoisiin työkaluihin ja rajapintoihin. Näitä kutsuja voidaan tehdä rinnakkain tai peräkkäin. 
- *Ohjelmakoodin generointi* - tämä malli loistaa Python-, Java-, TypeScript- ja C++-koodin generoinnissa. 

### Esimerkki RAGista Mistral Large 2:lla 

Tässä esimerkissä käytämme Mistral Large 2:ta ajamaan RAG-kuviota tekstidokumentin yli. Kysymys on kirjoitettu koreaksi ja kysyy kirjoittajan toiminnasta ennen yliopistoa. 

Se käyttää Cohere Embeddings Model -mallia luodakseen upotukset tekstidokumentista sekä kysymyksestä. Tässä esimerkissä käytetään faiss Python -pakettia vektorivarastona. 

Mallille lähetetty kehotus sisältää sekä kysymyksen että kysymykseen vastaavia löydettyjä osia. Malli antaa sitten luonnollisen kielen vastauksen. 

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

# Hanki nämä Microsoft Foundry -projektisi "Yleiskatsaus" -sivulta
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # etäisyys, indeksi
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
Mistral Small on toinen malli Mistral-perheessä, joka kuuluu premier/enterprise-luokkaan. Kuten nimi kertoo, tämä malli on Pieni Kielenmalli (SLM). Mistral Smallin käyttämisen edut ovat: 
- Kustannussäästö verrattuna Mistral LLM-malleihin kuten Mistral Large ja NeMo - 80 % hinnanlasku
- Alhainen viive – nopeampi vastausaika verrattuna Mistralin LLM-malleihin
- Joustava – voidaan ottaa käyttöön eri ympäristöissä vähemmillä resurssivaatimuksilla. 


Mistral Small soveltuu hyvin: 
- Tekstipohjaisiin tehtäviin kuten tiivistämiseen, tunnesävyanalyysiin ja käännökseen. 
- Sovelluksiin, joissa pyyntöjä tehdään usein sen kustannustehokkuuden vuoksi 
- Alhaisen viiveen kooditehtäviin kuten koodin tarkistukseen ja ehdotuksiin 

## Vertailu Mistral Smallin ja Mistral Largen välillä 

Näyttääksesi viive-erot Mistral Smallin ja Largen välillä, aja alla olevat solut. 

Näet vastauksissa eron 3-5 sekuntia. Huomaa myös vastausten pituus ja tyyli saman kehotteen perusteella.  

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

Verrattuna muihin tässä oppitunnissa käsiteltyihin malleihin, Mistral NeMo on ainoa ilmainen Apache2-lisenssillä varustettu malli. 

Sitä pidetään päivityksenä aikaisempaan Mistralin avoimen lähdekoodin LLM:ään, Mistral 7B:hen. 

Joitakin muita NeMo-mallin ominaisuuksia ovat: 

- *Tehokkaampi tokenisointi:* Tämä malli käyttää Tekken-tokenisoijaa yleisemmin käytetyn tiktokenin sijaan. Tämä mahdollistaa paremman suorituskyvyn useammilla kielillä ja koodissa. 

- *Hienosäätö:* Pohjamalli on saatavilla hienosäätöön. Tämä antaa enemmän joustavuutta käyttötapauksiin, joissa hienosäätöä tarvitaan. 

- *Natiivi funktiokutsutus* - Kuten Mistral Large, tämä malli on koulutettu funktiokutsuihin. Tämä tekee siitä ainutlaatuisen yhtenä ensimmäisistä avoimen lähdekoodin malleista, jolla tämä on toteutettu. 


### Tokenisoijien vertailu 

Tässä esimerkissä tarkastelemme, miten Mistral NeMo käsittelee tokenisointia verrattuna Mistral Largeen. 

Molemmat esimerkit ottavat saman kehotteen, mutta huomaat, että NeMo palauttaa vähemmän tokeneita kuin Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Tuo tarvittavat paketit:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Lataa Mistral-tokenisaattori

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisoi viestilista
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

# Laske tokenien määrä
print(len(tokens))
```

```python
# Tuo tarvittavat kirjastot:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Lataa Mistral-tokenisaattori

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisoi viestilista
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

# Laske tokenien määrä
print(len(tokens))
```

## Oppiminen ei lopu tähän, jatka matkaa

Oppitunnin suorittamisen jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietotaitojesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->