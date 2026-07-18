# Kujenga kwa Kutumia Mifano ya Mistral 

## Utangulizi 

Somo hili litashughulikia: 
- Kuchunguza Mifano tofauti ya Mistral 
- Kuelewa matumizi na hali mbalimbali kwa kila mfano 
- Kuchunguza mifano ya msimbo inayonyesha sifa za kipekee za kila mfano. 

## Mifano ya Mistral 

Katika somo hili, tutaangalia mifano 3 tofauti ya Mistral: 
**Mistral Large**, **Mistral Small** na **Mistral Nemo**. 

Kila mfano wa haya upo bure kwa [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Msimbo katika daftari hili utatumia mifano hii kuendesha msimbo. 

> **Kumbuka:** GitHub Models itasimama mwishoni mwa Julai 2026. Hapa kuna maelezo zaidi kuhusu kutumia [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kutengeneza mifano ya AI. 


## Mistral Large 2 (2407)
Mistral Large 2 kwa sasa ni mfano mkuu wa Mistral na umeundwa kwa matumizi ya biashara. 

Mfano huu ni toleo lililoboreshwa la Mistral Large wa awali kwa kutoa 
- Dirisha Kubwa la Muktadha - 128k dhidi ya 32k 
- Utendaji Bora kwenye Kazi za Hisabati na Uprogramu - usahihi wa wastani wa 76.9% dhidi ya 60.4% 
- Utendaji Bora wa lugha nyingi - lugha ni pamoja na: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kiitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa sifa hizi, Mistral Large hutawala katika 
- *Uzalishaji wa Kusisimua Utambulisho (RAG)* - kutokana na dirisha kubwa la muktadha
- *Kupiga Simu za Kazi* - modeli hii ina kipengele cha kupiga simu za kazi moja kwa moja kinachowezesha kuunganishwa na zana na APIs za nje. Simu hizi zinaweza kufanywa kwa pamoja au mfukoni baada ya mwingine kwa mfuatano wa mpango. 
- *Uzalishaji wa Msimbo* - mfano huu una ustadi mkubwa katika uzalishaji wa Python, Java, TypeScript na C++. 

### Mfano wa RAG ukitumia Mistral Large 2 

Katika mfano huu, tunatumia Mistral Large 2 kufanya muundo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo kikuu. 

Inatumia Mfano wa Cohere Embeddings kuunda maelezo ya hati ya maandishi pamoja na swali. Kwa sampuli hii, inatumia kifurushi cha Python cha faiss kama hifadhi ya vekta. 

Ombi lililotumwa kwa mfano wa Mistral linajumuisha maswali pamoja na vipande vilivyopatikana ambavyo vinafanana na swali. Kisha Mfano hutoa jibu la lugha ya asili. 

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

# Pata hizi kutoka kwa ukurasa wa "Muhtasari" wa mradi wako wa Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # umbali, faharasa
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
Mistral Small ni mfano mwingine katika familia ya mifano ya Mistral chini ya kundi la premier/biashara. Kama jina linavyosema, mfano huu ni Mfano Mdogo wa Lugha (SLM). Faida za kutumia Mistral Small ni kwamba ni: 
- Kuokoa Gharama ikilinganishwa na Mistral LLMs kama Mistral Large na NeMo - kupungua kwa bei kwa 80%
- Kasi ya chini ya ucheleweshaji - jibu la haraka ikilinganishwa na LLMs za Mistral
- Kubadilika - inaweza kuendeshwa katika mazingira tofauti kwa vikwazo vichache juu ya rasilimali zinazohitajika. 


Mistral Small ni mzuri kwa: 
- Kazi za maandishi kama muhtasari, uchambuzi wa hisia na tafsiri. 
- Programu ambapo maombi mara kwa mara hufanywa kutokana na ufanisi wake wa gharama 
- Kazi za msimbo zenye ucheleweshaji mdogo kama mapitio na mapendekezo ya msimbo 

## Kulinganisha Mistral Small na Mistral Large 

Kuonyesha tofauti za ucheleweshaji kati ya Mistral Small na Large, endesha seli zilizo hapa chini. 

Unapaswa kuona tofauti za nyakati za majibu kati ya sekunde 3-5. Pia angalia urefu na mtindo wa majibu kwa ombi lilelile.  

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

Ikilinganishwa na mifano mingine miwili iliyoelezwa katika somo hili, Mistral NeMo ndilo mfano pekee wa bure wenye Leseni ya Apache2. 

Unaangaliwa kama toleo lililoboreshwa la LLM ya chanzo huria ya awali kutoka Mistral, Mistral 7B. 

Baadhi ya sifa nyingine za mfano wa NeMo ni: 

- *Tokenization yenye ufanisi zaidi:* Mfano huu unatumia tokenizer ya Tekken badala ya tiktoken inayotumika zaidi. Hii inaruhusu utendaji bora katika lugha na msimbo zaidi. 

- *Finetuning:* Mfano msingi upo kwa ajili ya kurekebisha kwa kina. Hii inaruhusu kubadilika zaidi kwa matumizi ambapo marekebisho yanaweza kuhitajika. 

- *Kupiga Simu za Kazi Moja kwa Moja* - Kama Mistral Large, mfano huu umefundishwa juu ya kupiga simu za kazi. Hii inaufanya uwe wa kipekee ikiwa mojawapo ya mifano ya chanzo huria ya kwanza kufanya hivyo. 


### Kulinganisha Tokenizers 

Katika sampuli hii, tutaangalia jinsi Mistral NeMo inavyoshughulikia tokenization ikilinganishwa na Mistral Large. 

Sampuli zote mbili zinachukua ombi lilelile lakini unapaswa kuona kwamba NeMo inarudisha tokeni chache kuliko Mistral Large. 

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

# Tengeneza alama za orodha ya ujumbe
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

# Hesabu idadi ya alama
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

# Gawanya orodha ya ujumbe kwa tokens
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

## Kujifunza hakiishi hapa, endelea safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kuumba](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuboresha ujuzi wako wa AI ya Kuumba!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->