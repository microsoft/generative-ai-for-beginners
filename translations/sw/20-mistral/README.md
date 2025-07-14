<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:02:43+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sw"
}
-->
# Kujenga na Mifano ya Mistral

## Utangulizi

Somo hili litajumuisha:  
- Kuchunguza mifano tofauti ya Mistral  
- Kuelewa matumizi na hali za kila mfano  
- Sampuli za msimbo zinaonyesha sifa za kipekee za kila mfano.

## Mifano ya Mistral

Katika somo hili, tutachunguza mifano 3 tofauti ya Mistral:  
**Mistral Large**, **Mistral Small** na **Mistral Nemo**.

Kila mojawapo ya mifano hii inapatikana bure kwenye soko la Mifano la Github. Msimbo katika daftari hili utatumia mifano hii kuendesha msimbo. Hapa kuna maelezo zaidi kuhusu kutumia Mifano ya Github kwa [kuchora mfano na mifano ya AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 kwa sasa ni mfano mkuu kutoka Mistral na umebuniwa kwa matumizi ya biashara.

Mfano huu ni toleo lililoboreshwa la Mistral Large asili kwa kutoa  
- Dirisha kubwa la muktadha - 128k dhidi ya 32k  
- Utendaji bora katika kazi za Hisabati na Uandishi wa Msimbo - usahihi wa wastani wa 76.9% dhidi ya 60.4%  
- Utendaji ulioboreshwa wa lugha nyingi - lugha ni pamoja na: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kiitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa sifa hizi, Mistral Large huonyesha ubora katika  
- *Uundaji wa Maandishi kwa Msaada wa Urejeshaji (RAG)* - kutokana na dirisha kubwa la muktadha  
- *Kupiga Simu za Kazi* - mfano huu una uwezo wa asili wa kupiga simu za kazi unaoruhusu kuunganishwa na zana na API za nje. Simu hizi zinaweza kufanywa kwa wakati mmoja au mfululizo.  
- *Uundaji wa Msimbo* - mfano huu una ubora katika uundaji wa Python, Java, TypeScript na C++.

### Mfano wa RAG ukitumia Mistral Large 2

Katika mfano huu, tunatumia Mistral Large 2 kuendesha muundo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo kikuu.

Inatumia Mfano wa Cohere Embeddings kuunda embeddings za hati ya maandishi pamoja na swali. Kwa sampuli hii, inatumia kifurushi cha Python cha faiss kama hifadhi ya vekta.

Maelekezo yanayotumwa kwa mfano wa Mistral yanajumuisha maswali pamoja na vipande vilivyorekebishwa vinavyofanana na swali. Kisha Mfano hutoa jibu la lugha ya asili.

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

Mistral Small ni mfano mwingine katika familia ya Mistral chini ya kundi la premier/enterprise. Kama jina linavyosema, mfano huu ni Mfano Mdogo wa Lugha (SLM). Faida za kutumia Mistral Small ni kwamba ni:  
- Hutoa akiba ya gharama ikilinganishwa na Mistral LLM kama Mistral Large na NeMo - punguzo la bei la 80%  
- Ucheleweshaji mdogo - majibu ya haraka ikilinganishwa na LLM za Mistral  
- Uwezo wa kubadilika - unaweza kutumika katika mazingira tofauti kwa vikwazo vidogo vya rasilimali zinazohitajika.

Mistral Small ni mzuri kwa:  
- Kazi zinazotegemea maandishi kama muhtasari, uchambuzi wa hisia na tafsiri.  
- Programu ambapo maombi mara kwa mara hufanywa kutokana na ufanisi wake wa gharama  
- Kazi za msimbo zenye ucheleweshaji mdogo kama mapitio na mapendekezo ya msimbo

## Kulinganisha Mistral Small na Mistral Large

Ili kuonyesha tofauti za ucheleweshaji kati ya Mistral Small na Large, endesha seli zilizo hapa chini.

Unapaswa kuona tofauti ya muda wa majibu kati ya sekunde 3-5. Pia zingatia urefu na mtindo wa majibu kwa maelekezo yale yale.

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

Ikilinganishwa na mifano mingine miwili iliyojadiliwa katika somo hili, Mistral NeMo ni mfano pekee wa bure wenye Leseni ya Apache2.

Unachukuliwa kama toleo lililoboreshwa la LLM ya awali ya chanzo huria kutoka Mistral, Mistral 7B.

Baadhi ya sifa nyingine za mfano wa NeMo ni:

- *Tokenization yenye ufanisi zaidi:* Mfano huu unatumia tokenizer ya Tekken badala ya tiktoken inayotumika zaidi. Hii inaruhusu utendaji bora kwa lugha na msimbo zaidi.

- *Finetuning:* Mfano msingi unapatikana kwa finetuning. Hii inatoa ufanisi zaidi kwa matumizi ambapo finetuning inaweza kuhitajika.

- *Kupiga Simu za Kazi kwa Asili* - Kama Mistral Large, mfano huu umefundishwa kupiga simu za kazi. Hii humfanya kuwa wa kipekee kama mojawapo ya mifano ya chanzo huria ya kwanza kufanya hivyo.

### Kulinganisha Tokenizers

Katika sampuli hii, tutaangalia jinsi Mistral NeMo inavyoshughulikia tokenization ikilinganishwa na Mistral Large.

Sampuli zote mbili zinachukua maelekezo yale yale lakini unapaswa kuona kuwa NeMo hurudisha tokeni chache ikilinganishwa na Mistral Large.

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

## Kujifunza hakukomi hapa, endelea Safari

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza ujuzi wako wa AI ya Kizazi!

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.