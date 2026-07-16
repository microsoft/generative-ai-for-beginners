# Kujenga na Mifano ya Mistral 

## Utangulizi 

Somo hili litajumuisha: 
- Kuchunguza Mifano tofauti ya Mistral 
- Kuelewa matumizi na hali za kila mfano 
- Kuchunguza mifano ya msimbo unaoonyesha sifa za kipekee za kila mfano. 

## Mifano ya Mistral 

Katika somo hili, tutachunguza mifano 3 tofauti ya Mistral: 
**Mistral Large**, **Mistral Small** na **Mistral Nemo**. 

Kila mmoja wa mifano hii inapatikana bure kwenye [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Msimbo kwenye daftari hili utatumia mifano hii kuendesha msimbo.

> **Kumbuka:** GitHub Models itafutwa mwishoni mwa Julai 2026. Hapa kuna maelezo zaidi juu ya kutumia [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kutengeneza prototypes na mifano ya AI. 


## Mistral Large 2 (2407)
Mistral Large 2 kwa sasa ni mfano mkuu kutoka Mistral na umewekwa kwa matumizi ya biashara. 

Mfano huu ni uboreshaji wa Mistral Large wa awali kwa kutoa 
- Dirisha Kubwa la Muktadha - 128k dhidi ya 32k 
- Utendaji Bora katika Majukumu ya Hisabati na Uandishi wa Msimbo - wastani wa usahihi 76.9% dhidi ya 60.4% 
- Uboreshaji wa utendaji wa lugha nyingi - lugha ni pamoja na: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa sifa hizi, Mistral Large huonyesha ufanisi katika 
- *Uzalishaji ulioboreshwa kwa Kupata Taarifa (RAG)* - kutokana na dirisha kubwa la muktadha
- *Kupiga Simu za Kazi* - mfano huu una uwezo wa asili wa kupiga simu za kazi ambao unaruhusu kuunganishwa na zana za nje na APIs. Simu hizi zinaweza kufanyika kwa wakati mmoja au mmoja baada ya mwingine kwa mpangilio wa mfuatano. 
- *Uzalishaji wa Msimbo* - mfano huu ni bora katika uzalishaji wa Python, Java, TypeScript na C++. 

### Mfano wa RAG ukitumia Mistral Large 2 

Katika mfano huu, tunatumia Mistral Large 2 kuendesha mtindo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo kikuu. 

Inatumia Mfano wa Cohere Embeddings kuunda embeddings za hati ya maandishi pamoja na swali. Kwa mfano huu, inatumia kifurushi cha faiss cha Python kama hifadhi ya vekta. 

Ombi lililotumwa kwa mfano wa Mistral linajumuisha maswali pamoja na vipande vilivyopatikana vinavyofanana na swali. Kisha Mfano hutoa jibu la lugha ya asili. 

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

# Pata hizi kutoka kwenye ukurasa wa "Muhtasari" wa mradi wako wa Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # umbali, fahirisi
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
Mistral Small ni mfano mwingine katika familia ya mifano ya Mistral chini ya kategoria ya premier/enterprise. Kama jina linavyosema, mfano huu ni Mfano Mdogo wa Lugha (SLM). Faida za kutumia Mistral Small ni kwamba ni: 
- Kuokoa Gharama ikilinganishwa na Mistral LLMs kama Mistral Large na NeMo - punguzo la bei la 80%
- Ucheleweshaji Mdogo - jibu la haraka ikilinganishwa na LLMs za Mistral
- Kubadilika - inaweza kuanzishwa katika mazingira tofauti na vizuizi vichache kwa rasilimali zinazohitajika. 


Mistral Small ni mzuri kwa: 
- Majukumu yanayotegemea maandishi kama muhtasari, uchambuzi wa hisia na tafsiri. 
- Programu ambapo maombi mara kwa mara hufanywa kutokana na ufanisi wa gharama yake 
- Majukumu ya msimbo yenye ucheleweshaji mdogo kama kupitia ukaguzi na mapendekezo ya msimbo 

## Kulinganisha Mistral Small na Mistral Large 

Kuonyesha tofauti za ucheleweshaji kati ya Mistral Small na Large, endesha seli zilizo hapa chini. 

Unapaswa kuona tofauti ya nyakati za majibu kati ya sekunde 3-5. Pia kumbuka urefu na mtindo wa majibu kwa ombi lile lile.  

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

Ukilinganisha na mifano mingine miwili iliyojadiliwa katika somo hili, Mistral NeMo ni mfano pekee bure unao na Leseni ya Apache2. 

Unachukuliwa kama uboreshaji wa awali wa LLM ya chanzo huria kutoka Mistral, Mistral 7B. 

Baadhi ya sifa nyingine za mfano wa NeMo ni: 

- *Tokenization yenye ufanisi zaidi:* Mfano huu unatumia tokenize ya Tekken badala ya tiktoken inayotumika zaidi. Hii inaruhusu utendaji bora kwa lugha nyingi na msimbo. 

- *Kufinywa kwa utaalamu:* Mfano msingi upo kwa kufinywa kwa utaalamu. Hii inaruhusu kubadilika zaidi kwa matumizi ambapo kufinywa kunaweza kuhitajika. 

- *Kupiga Simu za Kazi kama Asili* - Kama Mistral Large, mfano huu umefundishwa kupiga simu za kazi. Hii inaufanya kuwa wa kipekee kama mojawapo ya mifano ya chanzo huria ya kwanza kufanya hivyo. 


### Kulinganisha Tokenizers 

Katika mfano huu, tutaangalia jinsi Mistral NeMo inavyoshughulikia tokenization ikilinganishwa na Mistral Large. 

Sampuli zote mbili huchukua ombi lile lile lakini unapaswa kuona kwamba NeMo inarudisha tokeni chache kuliko Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Ingiza vifurushi vinavyohitajika:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Pakia tokenizer ya Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Gawanya orodha ya ujumbe
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

# Hesabu idadi ya tokens
print(len(tokens))
```

```python
# Ingiza vifurushi vinavyohitajika:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Pakia tokenizer ya Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tenganisha orodha ya ujumbe
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

# Hesabu idadi ya tokeni
print(len(tokens))
```

## Kujifunza hakukomi hapa, endelea safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI Inayotengeneza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuinua maarifa yako ya AI Inayotengeneza!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->