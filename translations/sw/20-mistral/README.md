<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:20:54+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "sw"
}
-->
# Kujenga na Mifano ya Mistral

## Utangulizi

Somo hili litafunika:
- Kuchunguza mifano mbalimbali ya Mistral
- Kuelewa matumizi na hali za kila mfano
- Sampuli za kodi zinaonyesha vipengele vya kipekee vya kila mfano.

## Mifano ya Mistral

Katika somo hili, tutachunguza mifano 3 tofauti ya Mistral:
**Mistral Large**, **Mistral Small** na **Mistral Nemo**.

Kila moja ya mifano hii inapatikana bure kwenye soko la Modeli la Github. Kodi katika daftari hili itatumia mifano hii kuendesha kodi. Hapa kuna maelezo zaidi juu ya kutumia Mifano ya Github [kuunda mfano wa AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 kwa sasa ni mfano mkuu kutoka Mistral na imeundwa kwa matumizi ya biashara.

Mfano huu ni uboreshaji wa Mistral Large ya awali kwa kutoa:
- Dirisha la muktadha kubwa zaidi - 128k dhidi ya 32k
- Utendaji bora kwenye kazi za Hisabati na Uandishi wa Kodi - 76.9% usahihi wa wastani dhidi ya 60.4%
- Utendaji bora wa lugha nyingi - lugha zinajumuisha: Kiingereza, Kifaransa, Kijerumani, Kihispania, Kiitaliano, Kireno, Kiholanzi, Kirusi, Kichina, Kijapani, Kikorea, Kiarabu, na Kihindi.

Kwa vipengele hivi, Mistral Large ina uwezo wa juu katika:
- *Utoaji wa Kuimarishwa kwa Urejeshaji (RAG)* - kutokana na dirisha kubwa la muktadha
- *Kuita Kazi* - mfano huu una uwezo wa kuita kazi asili ambayo inaruhusu ushirikiano na zana na API za nje. Mito hii inaweza kufanywa kwa pamoja au moja baada ya nyingine kwa mpangilio wa mfuatano.
- *Utoaji wa Kodi* - mfano huu ni bora katika uundaji wa Python, Java, TypeScript na C++.

### Mfano wa RAG kutumia Mistral Large 2

Katika mfano huu, tunatumia Mistral Large 2 kuendesha muundo wa RAG juu ya hati ya maandishi. Swali limeandikwa kwa Kikorea na linauliza kuhusu shughuli za mwandishi kabla ya chuo.

Inatumia Mfano wa Uwekaji wa Cohere kuunda uwekaji wa hati ya maandishi pamoja na swali. Kwa sampuli hii, inatumia pakiti ya faiss Python kama duka la vector.

Kidokezo kilichotumwa kwa mfano wa Mistral kinajumuisha maswali na vipande vilivyopatikana ambavyo vinafanana na swali. Mfano kisha hutoa jibu la lugha ya asili.

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
Mistral Small ni mfano mwingine katika familia ya mifano ya Mistral chini ya kikundi cha kipaumbele/biashara. Kama jina linavyoonyesha, mfano huu ni Mfano wa Lugha Ndogo (SLM). Faida za kutumia Mistral Small ni kwamba:
- Hupunguza gharama ikilinganishwa na Mistral LLMs kama Mistral Large na NeMo - upunguzaji wa bei kwa 80%
- Latency ya chini - majibu ya haraka ikilinganishwa na LLMs za Mistral
- Kubadilika - inaweza kutekelezwa katika mazingira tofauti na vizuizi vichache juu ya rasilimali zinazohitajika.

Mistral Small ni nzuri kwa:
- Kazi za msingi wa maandishi kama muhtasari, uchambuzi wa hisia na tafsiri.
- Programu ambapo maombi ya mara kwa mara yanafanywa kutokana na ufanisi wa gharama yake
- Kazi za kodi za latency ya chini kama ukaguzi na mapendekezo ya kodi

## Kulinganisha Mistral Small na Mistral Large

Kuonyesha tofauti za latency kati ya Mistral Small na Large, endesha seli zilizo hapa chini.

Unapaswa kuona tofauti katika nyakati za majibu kati ya sekunde 3-5. Pia angalia urefu wa majibu na mtindo juu ya kidokezo sawa.

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

Inachukuliwa kama uboreshaji wa LLM ya awali ya chanzo huria kutoka Mistral, Mistral 7B.

Baadhi ya vipengele vingine vya mfano wa NeMo ni:

- *Uwekaji wa tokeni bora zaidi:* Mfano huu unatumia tokeni ya Tekken badala ya tiktoken inayotumiwa zaidi. Hii inaruhusu utendaji bora zaidi juu ya lugha nyingi na kodi.

- *Kufinyanga:* Mfano wa msingi unapatikana kwa kufinyanga. Hii inaruhusu kubadilika zaidi kwa matumizi ambapo kufinyanga kunaweza kuhitajika.

- *Kuita Kazi Asili* - Kama Mistral Large, mfano huu umefundishwa juu ya kuita kazi. Hii inafanya kuwa ya kipekee kama mojawapo ya mifano ya kwanza ya chanzo huria kufanya hivyo.

### Kulinganisha Tokeni

Katika sampuli hii, tutatazama jinsi Mistral NeMo inavyoshughulikia uwekaji wa tokeni ikilinganishwa na Mistral Large.

Sampuli zote mbili zinachukua kidokezo sawa lakini unapaswa kuona kwamba NeMo inarejesha tokeni chache ikilinganishwa na Mistral Large.

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

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia mkusanyiko wetu wa [Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.