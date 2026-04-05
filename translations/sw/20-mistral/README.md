# Kujenga na Modeli za Mistral 

## Utangulizi 

Somo hili litajumuisha: 
- Kuchunguza Modeli tofauti za Mistral 
- Kuelewa matumizi na hali za kila modeli 
- Kuchunguza mifano ya msimbo unaoonyesha vipengele vya kipekee vya kila modeli. 

## Modeli za Mistral 

Katika somo hili, tutaangalia modeli 3 tofauti za Mistral: 
**Mistral Large**, **Mistral Small** na **Mistral Nemo**. 

Kila mojawapo ya modeli hizi inapatikana bure katika soko la GitHub Model. Msimbo uliopo katika daftari hili utatumia modeli hizi kuendesha msimbo. Hapa kuna maelezo zaidi kuhusu kutumia Modeli za GitHub ku [tengeneza prototipu na modeli za AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Mistral Large 2 kwa sasa ni modeli kuu kutoka Mistral na imeundwa kwa matumizi ya biashara. 

Modeli hii ni maboresho ya Mistral Large ya awali kwa kutoa 
-  Dirisha Kubwa la Muktadha - 128k dhidi ya 32k 
-  Utendaji Bora katika Kazi za Hisabati na Uandishi wa Msimbo - 76.9% usahihi wa wastani dhidi ya 60.4% 
-  Utendaji ulioboreshwa wa lugha nyingi - lugha ni pamoja na: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kiitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa vipengele hivi, Mistral Large huweza vizuri katika 
- *Uzalishaji Ulioboreshwa kwa Urekebishaji (RAG)* - kutokana na dirisha kubwa la muktadha
- *Kupiga Simu za Kazi* - modeli hii ina ugumu wa kupiga simu za kazi kwa asili unaoruhusu kuunganishwa na zana na API za nje. Simu hizi zinaweza kufanywa kwa sambamba au moja baada ya nyingine kwa mfuatano. 
- *Uzalishaji wa Msimbo* - modeli hii ni bora kwa uzalishaji wa Python, Java, TypeScript na C++. 

### Mfano wa RAG ukitumia Mistral Large 2 

Katika mfano huu, tunatumia Mistral Large 2 kuendesha muundo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa lugha ya Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo kikuu. 

Inatumia Modeli ya Cohere Embeddings kuunda embeddings za hati ya maandishi pamoja na swali. Kwa mfano huu, inatumia kifurushi cha faiss cha Python kama hifadhi ya vekta. 

Kiagizo kilichotumwa kwa modeli ya Mistral kina pamoja maswali na vipande vilivyorekebishwa vinavyofanana na swali. Kisha Modeli hutoa jibu la lugha ya kawaida. 

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
Mistral Small ni modeli nyingine katika familia ya Mistral chini ya kundi la premier/biashara. Kama jina linavyosema, modeli hii ni Modeli Ndogo ya Lugha (SLM). Faida za kutumia Mistral Small ni kwamba ni: 
- Inapunguza gharama ikilinganishwa na Mistral LLMs kama Mistral Large na NeMo - punguzo la bei la 80%
- Ucheleweshaji mdogo - majibu haraka ikilinganishwa na LLMs za Mistral
- Inayobadilika - inaweza kutumika katika mazingira tofauti kwa vikwazo kidogo kuhusu rasilimali zinazohitajika. 


Mistral Small ni nzuri kwa: 
- Kazi za maandishi kama muhtasari, uchambuzi wa hisia na tafsiri. 
- Programu ambapo maombi mara kwa mara hufanywa kutokana na ufanisi wake wa gharama 
- Kazi za msimbo zenye ucheleweshaji mdogo kama mapitio na mapendekezo ya msimbo 

## Kulinganisha Mistral Small na Mistral Large 

Ili kuonyesha tofauti za ucheleweshaji kati ya Mistral Small na Large, endesha seli zifuatazo. 

Unapaswa kuona tofauti ya nyakati za jibu kati ya sekunde 3-5. Pia kumbuka urefu wa majibu na mtindo wake kwa kiagizo kimoja.  

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

Ikilinganishwa na modeli nyingine mbili zilizojadiliwa katika somo hili, Mistral NeMo ndio modeli pekee ya bure yenye Leseni ya Apache2. 

Inachukuliwa kuwa maboresho ya LLM ya awali ya chanzo wazi kutoka Mistral, Mistral 7B. 

Vipengele vingine vya modeli ya NeMo ni: 

- *Tokenization yenye ufanisi zaidi:* Modeli hii inatumia tokenizer ya Tekken badala ya tiktoken inayotumika zaidi. Hii inaruhusu utendaji bora zaidi kwa lugha nyingi na msimbo. 

- *Kufunzwa tena kwa undani (Finetuning):* Modeli ya msingi inapatikana kwa finetuning. Hii inaruhusu ufanisi zaidi kwa matumizi ambapo finetuning inaweza kuhitajika. 

- *Kupiga Simu za Kazi asili* - Kama Mistral Large, modeli hii imefundishwa kupiga simu za kazi. Hii inaifanya kuwa ya kipekee kama mojawapo ya modeli za chanzo huria za kwanza kufanya hivyo. 


### Kulinganisha Tokenizers 

Katika mfano huu, tutaangalia jinsi Mistral NeMo inavyoshughulikia tokenization ikilinganishwa na Mistral Large. 

Mifano yote miwili huitoa kiagizo hicho hicho lakini unapaswa kuona NeMo inarudisha tokeni chache kuliko Mistral Large. 

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

# Pakua tokenizer ya Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tumia tokenizer kwa orodha ya ujumbe
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

# Pakia kinatilia Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Gawa orodha ya ujumbe vipande vidogo
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

# Hesabu idadi ya vipande vidogo
print(len(tokens))
```

## Kujifunza hakukomi hapa, endelea safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Uzalishaji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza ujuzi wako wa AI ya Uzalishaji!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Taarifa ya Kukataa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtu mtaalamu inapendekezwa. Hatubebei jukumu lolote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->