<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:59:10+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Mistral-malleilla

## Johdanto

Tässä oppitunnissa käsitellään:
- Eri Mistral-mallien tutkimista
- Kunkin mallin käyttötapauksien ja skenaarioiden ymmärtämistä
- Koodiesimerkkejä, jotka näyttävät kunkin mallin ainutlaatuiset ominaisuudet.

## Mistral-mallit

Tässä oppitunnissa tutkimme kolmea eri Mistral-mallia: **Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Kaikki nämä mallit ovat ilmaiseksi saatavilla Github Model -markkinapaikalla. Tämän muistikirjan koodi käyttää näitä malleja koodin suorittamiseen. Tässä on lisätietoja Github Models -mallien käytöstä [AI-mallien prototyyppauksessa](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 on tällä hetkellä Mistralin lippulaivamalli ja se on suunniteltu yrityskäyttöön.

Malli on parannus alkuperäiseen Mistral Large -malliin tarjoamalla
- Suurempi konteksti-ikkuna - 128k vs 32k
- Parempi suorituskyky matematiikan ja koodauksen tehtävissä - 76,9 % keskimääräinen tarkkuus vs 60,4 %
- Parempi monikielinen suorituskyky - kieliin kuuluvat: englanti, ranska, saksa, espanja, italia, portugali, hollanti, venäjä, kiina, japani, korea, arabia ja hindi.

Näillä ominaisuuksilla Mistral Large loistaa
- *Hakuperustainen sukupolvi (RAG)* - suuremman konteksti-ikkunan ansiosta
- *Funktiokutsut* - tämä malli tukee natiivisti funktiokutsuja, jotka mahdollistavat integraation ulkoisten työkalujen ja API:iden kanssa. Näitä kutsuja voidaan tehdä sekä rinnakkain että peräkkäin.
- *Koodin generointi* - tämä malli on erinomainen Python-, Java-, TypeScript- ja C++-koodin generoinnissa.

### RAG-esimerkki Mistral Large 2:lla

Tässä esimerkissä käytämme Mistral Large 2:ta suorittamaan RAG-kuvion tekstidokumentin yli. Kysymys on kirjoitettu koreaksi ja kysyy kirjoittajan toimista ennen yliopistoa.

Se käyttää Cohere Embeddings Modelia luomaan tekstidokumentin ja kysymyksen upotukset. Tässä esimerkissä käytetään faiss Python -pakettia vektorivarastona.

Mistral-mallille lähetetty kehotus sisältää sekä kysymykset että haetut kysymykseen liittyvät osat. Malli tarjoaa sitten luonnollisen kielen vastauksen.

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

Mistral Small on toinen malli Mistral-malliperheessä premier/enterprise-kategoriassa. Kuten nimi viittaa, tämä malli on pieni kielimalli (SLM). Mistral Smallin käytön edut ovat, että se on:
- Kustannustehokas verrattuna Mistral LLM:iin kuten Mistral Large ja NeMo - 80 % hinnan alennus
- Alhainen viive - nopeampi vastaus verrattuna Mistralin LLM:iin
- Joustava - voidaan ottaa käyttöön eri ympäristöissä vähemmillä resurssivaatimuksilla.

Mistral Small on erinomainen:
- Tekstipohjaisissa tehtävissä, kuten tiivistämisessä, sentimenttianalyysissä ja käännöksissä.
- Sovelluksissa, joissa tehdään usein pyyntöjä sen kustannustehokkuuden vuoksi
- Alhaisen viiveen kooditehtävissä, kuten tarkastelu ja koodiehdotukset

## Mistral Smallin ja Mistral Largen vertailu

Näyttääksesi eroja viiveessä Mistral Smallin ja Largen välillä, suorita alla olevat solut.

Sinun pitäisi nähdä ero vasteajoissa 3-5 sekuntia. Huomioi myös vastausten pituudet ja tyyli samassa kehotuksessa.

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

Verrattuna muihin tässä oppitunnissa käsiteltyihin malleihin, Mistral NeMo on ainoa ilmainen malli, jolla on Apache2-lisenssi.

Sitä pidetään parannuksena aiempaan avoimen lähdekoodin LLM:ään Mistralilta, Mistral 7B:hen.

Muita NeMo-mallin ominaisuuksia ovat:

- *Tehokkaampi tokenisointi:* Tämä malli käyttää Tekken-tokenisoijaa yleisemmin käytetyn tiktokenin sijaan. Tämä mahdollistaa paremman suorituskyvyn useammissa kielissä ja koodissa.

- *Hienosäätö:* Perusmalli on saatavilla hienosäätöä varten. Tämä tarjoaa enemmän joustavuutta käyttötapauksissa, joissa hienosäätöä saatetaan tarvita.

- *Natiivi funktiokutsu* - Kuten Mistral Large, tämä malli on koulutettu funktiokutsuihin. Tämä tekee siitä ainutlaatuisen yhtenä ensimmäisistä avoimen lähdekoodin malleista, joka tekee niin.

### Tokenisoijien vertailu

Tässä esimerkissä tarkastelemme, kuinka Mistral NeMo käsittelee tokenisointia verrattuna Mistral Largeen.

Molemmat esimerkit käyttävät samaa kehotusta, mutta sinun pitäisi nähdä, että NeMo palauttaa vähemmän tokenia kuin Mistral Large.

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

Tämän oppitunnin jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietämyksesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ole tietoinen siitä, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoriteettina. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.