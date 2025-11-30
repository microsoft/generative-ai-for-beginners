<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:01:13+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fi"
}
-->
# Rakentaminen Mistral-malleilla

## Johdanto

Tässä oppitunnissa käsitellään:  
- Eri Mistral-mallien tutkimista  
- Mallien käyttötarkoitusten ja tilanteiden ymmärtämistä  
- Koodiesimerkit näyttävät kunkin mallin ainutlaatuiset ominaisuudet.

## Mistral-mallit

Tässä oppitunnissa tutustumme kolmeen eri Mistral-malliin:  
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Jokainen näistä malleista on saatavilla ilmaiseksi Github Model -markkinapaikalla. Tässä muistikirjassa käytetään näitä malleja koodin suorittamiseen. Lisätietoja Github-mallien käytöstä [prototyyppien tekemiseen AI-malleilla](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) löytyy linkistä.

## Mistral Large 2 (2407)  
Mistral Large 2 on tällä hetkellä Mistralin lippulaivamalli ja suunniteltu yrityskäyttöön.

Malli on päivitys alkuperäiseen Mistral Largeen, ja se tarjoaa  
- Suuremman kontekstin ikkunan – 128k vs 32k  
- Paremmat suoritustulokset matematiikan ja koodauksen tehtävissä – 76,9 % keskimääräinen tarkkuus vs 60,4 %  
- Parannetun monikielisen suorituskyvyn – kielet sisältävät: englanti, ranska, saksa, espanja, italia, portugali, hollanti, venäjä, kiina, japani, korea, arabia ja hindi.

Näiden ominaisuuksien ansiosta Mistral Large on erinomainen  
- *Retrieval Augmented Generation (RAG)* -suorituksissa suuren kontekstin ikkunan ansiosta  
- *Function Calling* -mallissa on natiivi funktiokutsu, joka mahdollistaa integraation ulkoisten työkalujen ja API:en kanssa. Näitä kutsuja voidaan tehdä sekä rinnakkain että peräkkäin.  
- *Koodin generoinnissa* - malli on erityisen hyvä Pythonin, Javan, TypeScriptin ja C++:n generoinnissa.

### RAG-esimerkki käyttäen Mistral Large 2:ta

Tässä esimerkissä käytämme Mistral Large 2:ta suorittamaan RAG-kuvion tekstidokumentille. Kysymys on kirjoitettu koreaksi ja koskee kirjoittajan toimia ennen yliopistoa.

Se käyttää Cohere Embeddings -mallia luodakseen upotuksia tekstidokumentista sekä kysymyksestä. Tässä esimerkissä käytetään faiss Python -pakettia vektorivarastona.

Mistral-mallille lähetetty kehotus sisältää sekä kysymykset että haetut tekstin osat, jotka ovat samankaltaisia kuin kysymys. Malli antaa sitten luonnollisen kielen vastauksen.

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
Mistral Small on toinen Mistral-perheen malli, joka kuuluu premier/enterprise-kategoriaan. Nimensä mukaisesti tämä on pieni kielimalli (SLM). Mistral Smallin käytön etuja ovat:  
- Kustannussäästöt verrattuna Mistralin suuriin LLM-malleihin kuten Mistral Large ja NeMo – 80 % hinnanalennus  
- Alhainen viive – nopeampi vastausaika verrattuna Mistralin LLM-malleihin  
- Joustavuus – voidaan ottaa käyttöön eri ympäristöissä vähemmillä resurssivaatimuksilla.

Mistral Small sopii erinomaisesti:  
- Tekstipohjaisiin tehtäviin, kuten tiivistämiseen, tunteiden analysointiin ja kääntämiseen  
- Sovelluksiin, joissa tehdään usein pyyntöjä kustannustehokkuuden vuoksi  
- Pieniviiveisiin kooditehtäviin, kuten koodin tarkasteluun ja ehdotuksiin

## Mistral Smallin ja Mistral Largen vertailu

Näyttääksesi viive-erot Mistral Smallin ja Largen välillä, suorita alla olevat solut.

Vastausajoissa pitäisi näkyä 3–5 sekunnin ero. Huomioi myös vastausten pituudet ja tyyli samassa kehotteessa.

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

Sitä pidetään päivityksenä aiempaan Mistralin avoimen lähdekoodin LLM-malliin, Mistral 7B:hen.

Joitan muita NeMo-mallin ominaisuuksia ovat:

- *Tehokkaampi tokenisointi:* Tämä malli käyttää Tekken-tokenisaattoria yleisemmin käytetyn tiktokenin sijaan. Tämä mahdollistaa paremman suorituskyvyn useammilla kielillä ja koodissa.

- *Hienosäätö:* Perusmalli on saatavilla hienosäätöä varten. Tämä antaa enemmän joustavuutta käyttötapauksiin, joissa hienosäätö voi olla tarpeen.

- *Natiivifunktiokutsu* – kuten Mistral Large, tämä malli on koulutettu funktiokutsuihin. Tämä tekee siitä ainutlaatuisen yhtenä ensimmäisistä avoimen lähdekoodin malleista, jolla tämä ominaisuus on.

### Tokenisaattoreiden vertailu

Tässä esimerkissä tarkastelemme, miten Mistral NeMo käsittelee tokenisointia verrattuna Mistral Largeen.

Molemmat esimerkit käyttävät samaa kehotetta, mutta NeMo palauttaa vähemmän tokeneita verrattuna Mistral Largeen.

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

Oppitunnin suorittamisen jälkeen tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaamme ja jatka Generative AI -osaamisesi kehittämistä!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.