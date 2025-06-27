<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:18:48+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Mistral-malleilla

## Johdanto

Tässä oppitunnissa käsitellään:
- Erilaisten Mistral-mallien tutkiminen
- Käyttötapauksien ja skenaarioiden ymmärtäminen jokaiselle mallille
- Koodiesimerkit, jotka esittelevät kunkin mallin ainutlaatuisia ominaisuuksia.

## Mistral-mallit

Tässä oppitunnissa tutkimme kolmea erilaista Mistral-mallia: **Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Kaikki nämä mallit ovat saatavilla ilmaiseksi Github Model -kauppapaikalla. Tämän muistikirjan koodi käyttää näitä malleja koodin suorittamiseen. Tässä on lisätietoja Github-mallien käytöstä [AI-mallien prototyyppien luomiseen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 on tällä hetkellä Mistralin lippulaivamalli ja se on suunniteltu yrityskäyttöön.

Malli on päivitys alkuperäiseen Mistral Large -malliin tarjoamalla
- Suurempi kontekstin ikkuna - 128k vs 32k
- Parempi suorituskyky matematiikka- ja kooditehtävissä - 76,9 % keskimääräinen tarkkuus vs 60,4 %
- Lisääntynyt monikielinen suorituskyky - kielet sisältävät: englanti, ranska, saksa, espanja, italia, portugali, hollanti, venäjä, kiina, japani, korea, arabia ja hindi.

Näiden ominaisuuksien ansiosta Mistral Large erottuu
- *Retrieval Augmented Generation (RAG)* - suuremman kontekstin ikkunan ansiosta
- *Function Calling* - tämä malli tukee natiivisti funktiokutsuja, mikä mahdollistaa integraation ulkoisten työkalujen ja API:en kanssa. Nämä kutsut voidaan tehdä joko rinnakkain tai peräkkäin.
- *Code Generation* - tämä malli erottuu Python-, Java-, TypeScript- ja C++-generoinnissa.

### RAG-esimerkki käyttäen Mistral Large 2

Tässä esimerkissä käytämme Mistral Large 2 -mallia suorittamaan RAG-kuvion tekstidokumentin yli. Kysymys on kirjoitettu koreaksi ja kysyy tekijän toiminnasta ennen yliopistoa.

Se käyttää Cohere Embeddings -mallia luomaan upotuksia tekstidokumentista sekä kysymyksestä. Tässä esimerkissä se käyttää faiss Python -pakettia vektorivarastona.

Mistral-mallille lähetetty kehotus sisältää sekä kysymykset että haetut osat, jotka ovat samankaltaisia kysymyksen kanssa. Malli antaa sitten luonnollisen kielen vastauksen.

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

Mistral Small on toinen malli Mistral-mallien perheessä, joka kuuluu premium/yrityskategoriaan. Kuten nimi viittaa, tämä malli on pieni kielimalli (SLM). Mistral Small -mallin käytön edut ovat:
- Kustannussäästö verrattuna Mistral LLM:iin kuten Mistral Large ja NeMo - 80 % hinnanalennus
- Alhainen viive - nopeampi vaste verrattuna Mistralin LLM:iin
- Joustavuus - voidaan ottaa käyttöön eri ympäristöissä vähemmillä rajoituksilla tarvittavien resurssien suhteen.

Mistral Small on erinomainen:
- Tekstipohjaisissa tehtävissä kuten tiivistämisessä, sentimenttianalyysissä ja kääntämisessä.
- Sovelluksissa, joissa tehdään usein pyyntöjä kustannustehokkuuden vuoksi
- Alhaisen viiveen kooditehtävissä kuten tarkastelu ja koodiehdotukset

## Mistral Smallin ja Mistral Largen vertailu

Näyttääksemme eroja viiveessä Mistral Smallin ja Largen välillä, suorita alla olevat solut.

Sinun pitäisi nähdä ero vasteajoissa 3-5 sekunnin välillä. Huomaa myös vastauksen pituudet ja tyyli saman kehotuksen kohdalla.

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

Verrattuna muihin kahteen malliin, joita käsitellään tässä oppitunnissa, Mistral NeMo on ainoa ilmainen malli, jolla on Apache2-lisenssi.

Sitä pidetään päivityksenä aiempaan avoimen lähdekoodin LLM:ään Mistralilta, Mistral 7B:hen.

Muita NeMo-mallin ominaisuuksia ovat:

- *Tehokkaampi tokenisointi:* Tämä malli käyttää Tekken-tokenisoijaa yleisemmin käytetyn tiktokenin sijaan. Tämä mahdollistaa paremman suorituskyvyn useammissa kielissä ja koodissa.

- *Finetuning:* Perusmalli on saatavilla hienosäätöön. Tämä mahdollistaa enemmän joustavuutta käyttötapauksissa, joissa hienosäätöä voidaan tarvita.

- *Natiivifunktiokutsut* - Kuten Mistral Large, tämä malli on koulutettu funktiokutsuille. Tämä tekee siitä ainutlaatuisen yhtenä ensimmäisistä avoimen lähdekoodin malleista, joka tekee niin.

### Tokenisointien vertailu

Tässä esimerkissä tarkastelemme, miten Mistral NeMo käsittelee tokenisointia verrattuna Mistral Largeen.

Molemmat esimerkit ottavat saman kehotuksen, mutta sinun pitäisi nähdä, että NeMo palauttaa vähemmän tokeneita verrattuna Mistral Largeen.

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

## Oppiminen ei lopu tähän, jatka matkaa

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietämyksesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta otathan huomioon, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää auktoriteettina. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.