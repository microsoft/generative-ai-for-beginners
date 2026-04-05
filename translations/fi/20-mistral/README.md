# Rakentaminen Mistral-malleilla

## Johdanto

Tässä oppitunnissa käydään läpi:
- Eri Mistral-mallien tutkiminen
- Mallien käyttötilanteiden ja -skenaarioiden ymmärtäminen
- Koodiesimerkkien tarkastelu, jotka osoittavat kunkin mallin ainutlaatuiset ominaisuudet.

## Mistral-mallit

Tässä oppitunnissa tutustumme kolmeen eri Mistral-malliin:
**Mistral Large**, **Mistral Small** ja **Mistral Nemo**.

Jokainen näistä malleista on saatavilla ilmaiseksi GitHub Model -markkinapaikalla. Tämän muistikirjan koodi käyttää näitä malleja suorittaakseen koodin. Tässä on lisätietoja GitHub Mallien käytöstä [AI-mallien prototyyppien tekemiseen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 on tällä hetkellä Mistralin lippulaivamalli ja on suunniteltu yrityskäyttöön.

Mallissa on parannuksia alkuperäiseen Mistral Largeen verrattuna, jotka tarjoavat:
- Suurempi konteksti-ikkuna - 128k vs 32k
- Parempi suorituskyky matematiikassa ja koodaustehtävissä - 76,9 % keskimääräinen tarkkuus vs 60,4 %
- Lisätty monikielinen suorituskyky - kielet sisältävät: englanti, ranska, saksa, espanja, italia, portugali, hollanti, venäjä, kiina, japani, korea, arabia ja hindi.

Näillä ominaisuuksilla Mistral Large suoriutuu erinomaisesti
- *Hakua täydentävä generointi (RAG)* - suuremman konteksti-ikkunan ansiosta
- *Funktiokutsut* - tässä mallissa on natiivi funktiokutsujen tuki, joka mahdollistaa integraation ulkoisten työkalujen ja rajapintojen kanssa. Näitä kutsuja voidaan tehdä sekä rinnakkain että peräkkäin.
- *Koodin generointi* - malli on erinomainen Pythonin, Javan, TypeScriptin ja C++:n generoinnissa.

### RAG-esimerkki Mistral Large 2:lla

Tässä esimerkissä käytämme Mistral Large 2:ta suorittamaan RAG-kuviota tekstiasiakirjalle. Kysymys on kirjoitettu koreaksi ja kysyy kirjoittajan toimista ennen yliopistoa.

Se käyttää Cohere Embeddings -mallia luodakseen tekstiasiakirjalle sekä kysymykselle upotukset. Tässä esimerkissä faiss Python -pakettia käytetään vektorivarastona.

Mallille lähetetty kehotus sisältää sekä kysymykset että haetut tekstin palat, jotka ovat samankaltaisia kuin kysymys. Malli antaa sitten luonnollisen kielen vastauksen.

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
Mistral Small on toinen Mistral-perheen malli premier/enterprise-kategoriassa. Nimen mukaisesti tämä malli on pieni kielimalli (SLM). Mistral Smallin käytön etuja ovat:
- Kustannussäästö verrattuna Mistral LLM:iin kuten Mistral Large ja NeMo - 80 % hinnanlasku
- Alhainen viive - nopeampi vastaus Mistralin LLM:iin verrattuna
- Joustava - voidaan ottaa käyttöön eri ympäristöissä vähemmillä resurssivaatimuksiin liittyvillä rajoituksilla.

Mistral Small sopii mainiosti:
- Tekstipohjaisiin tehtäviin, kuten tiivistämiseen, tunteiden analysointiin ja käännöksiin.
- Sovelluksiin, joissa pyyntöjä tehdään usein kustannustehokkuuden vuoksi
- Alhaisen viiveen kooditehtäviin, kuten tarkistukseen ja koodiehdotuksiin

## Mistral Smallin ja Mistral Largen vertailu

Näyttääksesi viive-erot Mistral Smallin ja Largen välillä, suorita alla olevat solut.

Sinun pitäisi nähdä vastausaikojen ero 3–5 sekuntia. Huomioi myös vastausten pituudet ja tyyli samassa kehotteessa.

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

Verrattuna muihin tässä oppitunnissa käsiteltyihin malleihin, Mistral NeMo on ainoa ilmainen Apache2-lisenssillä oleva malli.

Sitä pidetään päivityksenä aiempaan Mistralin avoimen lähdekoodin LLM:ään, Mistral 7B:hen.

Joihinkin NeMo-mallin ominaisuuksiin kuuluvat:

- *Tehokkaampi tokenisointi:* Tämä malli käyttää Tekken-tokenisoijaa yleisemmin käytetyn tiktokenin sijaan. Tämä mahdollistaa paremman suorituskyvyn useammilla kielillä ja koodilla.

- *Fine-tunetettavuus:* Perusmalli on saatavilla hienosäätöä varten. Tämä mahdollistaa joustavamman käytön tilanteissa, joissa hienosäätö on tarpeen.

- *Natiivifunktiokutsut* – Kuten Mistral Large, tämä malli on koulutettu funktiokutsuihin. Tämä tekee siitä ainutlaatuisen, sillä se on yksi ensimmäisistä avoimen lähdekoodin malleista, joka tukee tätä.

### Tokenisoijien vertailu

Tässä esimerkissä tarkastelemme, miten Mistral NeMo käsittelee tokenisointia verrattuna Mistral Largeen.

Molemmat esimerkit ottavat saman kehotteen, mutta NeMon pitäisi palauttaa vähemmän tokeneita kuin Mistral Large.

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

# Lataa Mistral-tokenisoija

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

Oppitunnin jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista inhimillistä käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkintojen seurauksista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->