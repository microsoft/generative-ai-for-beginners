<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:01:31+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sw"
}
-->
# Kujenga na Mifano ya Mistral

## Utangulizi

Somohili litajumuisha:
- Kuchunguza mifano tofauti ya Mistral
- Kuelewa matumizi na hali za kila mfano
- Sampuli za kodi zinaonyesha sifa za kipekee za kila mfano.

## Mifano ya Mistral

Katika somo hili, tutachunguza mifano 3 tofauti ya Mistral: **Mistral Large**, **Mistral Small**, na **Mistral Nemo**.

Kila moja ya mifano hii inapatikana bure kwenye soko la Github Model. Kodi katika daftari hili itatumia mifano hii kuendesha kodi. Hapa kuna maelezo zaidi juu ya kutumia Mifano ya Github [kujaribu na mifano ya AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 kwa sasa ni mfano wa bendera kutoka Mistral na imeundwa kwa matumizi ya biashara.

Mfano huu ni uboreshaji wa Mistral Large ya awali kwa kutoa:
- Dirisha la Muktadha Kubwa - 128k vs 32k
- Utendaji bora kwenye Majukumu ya Hisabati na Uandishi wa Kodi - 76.9% usahihi wa wastani vs 60.4%
- Utendaji ulioboreshwa wa lugha nyingi - lugha zinajumuisha: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kiitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa sifa hizi, Mistral Large inang'aa katika:
- *Uzalishaji Ulioimarishwa kwa Urejeleaji (RAG)* - kutokana na dirisha kubwa la muktadha
- *Kuita Kazi* - mfano huu una kuita kazi asili ambayo inaruhusu kuunganishwa na zana za nje na API. Simu hizi zinaweza kufanywa kwa pamoja au moja baada ya nyingine kwa mpangilio wa mfululizo.
- *Uzalishaji wa Kodi* - mfano huu unafanya vizuri katika uzalishaji wa Python, Java, TypeScript, na C++.

### Mfano wa RAG ukitumia Mistral Large 2

Katika mfano huu, tunatumia Mistral Large 2 kuendesha muundo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo.

Inatumia Mfano wa Embeddings wa Cohere kuunda embeddings za hati ya maandishi pamoja na swali. Kwa sampuli hii, inatumia kifurushi cha faiss Python kama duka la vector.

Hojaji iliyotumwa kwa mfano wa Mistral inajumuisha maswali pamoja na vipande vilivyopatikana ambavyo ni sawa na swali. Mfano kisha hutoa majibu kwa lugha ya asili.

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
Mistral Small ni mfano mwingine katika familia ya mifano ya Mistral chini ya kategoria ya premier/biashara. Kama jina linavyoashiria, mfano huu ni Mfano Mdogo wa Lugha (SLM). Faida za kutumia Mistral Small ni kwamba:
- Inaokoa gharama ikilinganishwa na LLM za Mistral kama Mistral Large na NeMo - upunguzaji wa bei kwa 80%
- Upungufu wa muda wa kusubiri - majibu ya haraka ikilinganishwa na LLM za Mistral
- Kubadilika - inaweza kutumiwa katika mazingira tofauti na vizuizi vichache juu ya rasilimali zinazohitajika.

Mistral Small ni nzuri kwa:
- Majukumu yanayohusiana na maandishi kama muhtasari, uchambuzi wa hisia na tafsiri.
- Programu ambapo maombi ya mara kwa mara yanatolewa kutokana na ufanisi wa gharama zake
- Majukumu ya kodi ya upungufu wa muda wa kusubiri kama ukaguzi na mapendekezo ya kodi

## Kulinganisha Mistral Small na Mistral Large

Kuonyesha tofauti za muda wa kusubiri kati ya Mistral Small na Large, endesha seli zilizo hapa chini.

Unapaswa kuona tofauti ya muda wa majibu kati ya sekunde 3-5. Pia kumbuka urefu wa majibu na mtindo juu ya hojaji ile ile.

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

Ikilinganishwa na mifano mingine miwili iliyojadiliwa katika somo hili, Mistral NeMo ni mfano pekee wa bure na Leseni ya Apache2.

Inachukuliwa kama uboreshaji wa LLM ya awali ya chanzo wazi kutoka Mistral, Mistral 7B.

Baadhi ya sifa nyingine za mfano wa NeMo ni:

- *Uwekaji alama wa tokeni wenye ufanisi zaidi:* Mfano huu unatumia tokenizer ya Tekken juu ya tiktoken inayotumiwa kwa kawaida. Hii inaruhusu utendaji bora juu ya lugha zaidi na kodi.

- *Kubadilisha faini:* Mfano wa msingi unapatikana kwa kubadilisha faini. Hii inaruhusu kubadilika zaidi kwa matumizi ambapo kubadilisha faini kunaweza kuhitajika.

- *Kuita Kazi Asili* - Kama Mistral Large, mfano huu umefundishwa kwenye kuita kazi. Hii inafanya kuwa wa kipekee kama mmoja wa mifano ya chanzo wazi ya kwanza kufanya hivyo.

### Kulinganisha Tokenizers

Katika sampuli hii, tutaangalia jinsi Mistral NeMo inavyoshughulikia uwekaji alama wa tokeni ikilinganishwa na Mistral Large.

Sampuli zote zinachukua hojaji ile ile lakini unapaswa kuona kwamba NeMo inarejesha tokeni chache ikilinganishwa na Mistral Large.

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

## Kujifunza hakusimami hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia [mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuelewana. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.