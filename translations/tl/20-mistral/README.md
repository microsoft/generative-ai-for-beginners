<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:01:06+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tl"
}
-->
# Pagbuo gamit ang Mistral Models

## Panimula

Tatalakayin sa araling ito ang:
- Pagsusuri sa iba't ibang Mistral Models
- Pag-unawa sa mga gamit at senaryo para sa bawat modelo
- Mga halimbawa ng code na nagpapakita ng natatanging katangian ng bawat modelo.

## Ang Mistral Models

Sa araling ito, susuriin natin ang 3 iba't ibang Mistral models: **Mistral Large**, **Mistral Small**, at **Mistral Nemo**.

Ang bawat isa sa mga modelong ito ay libreng makukuha sa Github Model marketplace. Ang code sa notebook na ito ay gagamit ng mga modelong ito upang patakbuhin ang code. Narito ang karagdagang detalye sa paggamit ng Github Models upang [mag-prototype gamit ang AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Ang Mistral Large 2 ay kasalukuyang nangungunang modelo mula sa Mistral at dinisenyo para sa paggamit ng mga negosyo.

Ang modelo ay isang pag-upgrade sa orihinal na Mistral Large sa pamamagitan ng pag-aalok ng
- Mas Malaking Context Window - 128k kumpara sa 32k
- Mas mahusay na pagganap sa Math at Coding Tasks - 76.9% average accuracy kumpara sa 60.4%
- Pinahusay na multilingual na pagganap - kasama ang mga wika: Ingles, Pranses, Aleman, Espanyol, Italyano, Portuges, Olandes, Ruso, Tsino, Hapones, Koreano, Arabe, at Hindi.

Sa mga katangiang ito, ang Mistral Large ay mahusay sa
- *Retrieval Augmented Generation (RAG)* - dahil sa mas malaking context window
- *Function Calling* - ang modelong ito ay may native function calling na nagbibigay-daan sa integrasyon sa mga panlabas na tools at APIs. Ang mga tawag na ito ay maaaring gawin nang sabay-sabay o sunod-sunod.
- *Code Generation* - ang modelong ito ay mahusay sa Python, Java, TypeScript, at C++ generation.

### Halimbawa ng RAG gamit ang Mistral Large 2

Sa halimbawang ito, ginagamit natin ang Mistral Large 2 upang magpatakbo ng RAG pattern sa isang text document. Ang tanong ay nakasulat sa Koreano at nagtatanong tungkol sa mga gawain ng may-akda bago ang kolehiyo.

Gumagamit ito ng Cohere Embeddings Model upang lumikha ng mga embeddings ng text document pati na rin ang tanong. Para sa halimbawang ito, ginagamit nito ang faiss Python package bilang isang vector store.

Ang prompt na ipinadala sa Mistral model ay kasama ang parehong mga tanong at ang mga nakuha na bahagi na katulad ng tanong. Ang Model ay nagbibigay ng tugon sa natural na wika.

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
Ang Mistral Small ay isa pang modelo sa pamilya ng mga modelo ng Mistral sa ilalim ng premier/enterprise na kategorya. Tulad ng ipinahihiwatig ng pangalan, ang modelong ito ay isang Small Language Model (SLM). Ang mga bentahe ng paggamit ng Mistral Small ay ito ay:
- Nakakatipid sa gastos kumpara sa mga Mistral LLMs tulad ng Mistral Large at NeMo - 80% pagbaba ng presyo
- Mababa ang latency - mas mabilis na tugon kumpara sa mga Mistral LLMs
- Flexible - maaaring i-deploy sa iba't ibang kapaligiran na may mas kaunting mga limitasyon sa kinakailangang mga mapagkukunan.

Mahusay ang Mistral Small para sa:
- Mga task na batay sa teksto tulad ng pagbubuod, pagsusuri ng damdamin at pagsasalin.
- Mga aplikasyon kung saan madalas ang mga kahilingan dahil sa pagiging epektibo sa gastos
- Mga task na may mababang latency code tulad ng pagsusuri at mungkahi ng code

## Paghahambing ng Mistral Small at Mistral Large

Upang ipakita ang mga pagkakaiba sa latency sa pagitan ng Mistral Small at Large, patakbuhin ang mga cell sa ibaba.

Dapat mong makita ang pagkakaiba sa oras ng pagtugon sa pagitan ng 3-5 segundo. Pansinin din ang haba at istilo ng tugon sa parehong prompt.

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

Kumpara sa iba pang dalawang modelong tinalakay sa araling ito, ang Mistral NeMo ay ang tanging libreng modelo na may Apache2 License.

Ito ay tinitingnan bilang isang pag-upgrade sa naunang open source LLM mula sa Mistral, ang Mistral 7B.

Ang ilan pang katangian ng NeMo model ay:

- *Mas mahusay na tokenization:* Ang modelong ito ay gumagamit ng Tekken tokenizer kaysa sa mas karaniwang ginagamit na tiktoken. Ito ay nagpapahintulot sa mas mahusay na pagganap sa mas maraming wika at code.

- *Finetuning:* Ang base model ay available para sa finetuning. Ito ay nagpapahintulot sa mas maraming flexibility para sa mga use-cases kung saan maaaring kailanganin ang finetuning.

- *Native Function Calling* - Tulad ng Mistral Large, ang modelong ito ay sinanay sa function calling. Ginagawa nitong natatangi bilang isa sa mga unang open source models na gawin ito.

### Paghahambing ng Tokenizers

Sa halimbawang ito, titingnan natin kung paano hinahawakan ng Mistral NeMo ang tokenization kumpara sa Mistral Large.

Parehong halimbawa ay gumagamit ng parehong prompt ngunit dapat mong makita na ang NeMo ay nagbabalik ng mas kaunting mga token kumpara sa Mistral Large.

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

## Hindi natatapos ang pag-aaral dito, ipagpatuloy ang Paglalakbay

Matapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapataas ng iyong kaalaman sa Generative AI!

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap namin ang katumpakan, pakitandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.