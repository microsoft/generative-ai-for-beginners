<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:02:31+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tl"
}
-->
# Paggawa gamit ang Mistral Models

## Panimula

Saklaw ng araling ito ang:  
- Pagsusuri sa iba't ibang Mistral Models  
- Pag-unawa sa mga gamit at sitwasyon para sa bawat modelo  
- Mga halimbawa ng code na nagpapakita ng natatanging katangian ng bawat modelo.

## Ang mga Mistral Models

Sa araling ito, tatalakayin natin ang 3 iba't ibang Mistral models:  
**Mistral Large**, **Mistral Small**, at **Mistral Nemo**.

Lahat ng mga modelong ito ay libre at makukuha sa Github Model marketplace. Gagamitin ang mga modelong ito sa notebook na ito para patakbuhin ang code. Narito ang karagdagang detalye sa paggamit ng Github Models para sa [prototyping gamit ang AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Ang Mistral Large 2 ang kasalukuyang pangunahing modelo mula sa Mistral at idinisenyo para sa paggamit sa enterprise.

Ang modelong ito ay isang upgrade mula sa orihinal na Mistral Large sa pamamagitan ng pagbibigay ng  
- Mas Malaking Context Window - 128k kumpara sa 32k  
- Mas mahusay na performance sa Math at Coding Tasks - 76.9% average accuracy kumpara sa 60.4%  
- Mas mataas na multilingual na performance - kabilang ang mga wika: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, at Hindi.

Dahil sa mga katangiang ito, mahusay ang Mistral Large sa  
- *Retrieval Augmented Generation (RAG)* - dahil sa mas malaking context window  
- *Function Calling* - may native function calling ang modelong ito na nagpapahintulot ng integrasyon sa mga external tools at APIs. Maaaring gawin ang mga tawag na ito nang sabay-sabay o sunod-sunod.  
- *Code Generation* - mahusay ang modelong ito sa pagbuo ng Python, Java, TypeScript, at C++ code.

### Halimbawa ng RAG gamit ang Mistral Large 2

Sa halimbawang ito, ginagamit natin ang Mistral Large 2 para patakbuhin ang RAG pattern sa isang text document. Ang tanong ay nakasulat sa Korean at nagtatanong tungkol sa mga gawain ng may-akda bago pumasok sa kolehiyo.

Gumagamit ito ng Cohere Embeddings Model para gumawa ng embeddings ng text document pati na rin ng tanong. Sa sample na ito, ginagamit ang faiss Python package bilang vector store.

Kasama sa prompt na ipinapadala sa Mistral model ang parehong mga tanong at mga nakuha na bahagi ng teksto na kahawig ng tanong. Pagkatapos, nagbibigay ang Model ng sagot sa natural na wika.

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

Ang Mistral Small ay isa pang modelo sa pamilya ng Mistral na kabilang sa premier/enterprise category. Gaya ng pangalan, ito ay isang Small Language Model (SLM). Ang mga benepisyo ng paggamit ng Mistral Small ay:  
- Nakakatipid sa gastos kumpara sa mga Mistral LLM tulad ng Mistral Large at NeMo - 80% mas mura  
- Mababang latency - mas mabilis ang tugon kumpara sa mga LLM ng Mistral  
- Flexible - maaaring i-deploy sa iba't ibang environment na may mas kaunting limitasyon sa kinakailangang resources.

Magaling ang Mistral Small para sa:  
- Mga text-based na gawain tulad ng pagsasummarize, sentiment analysis, at pagsasalin  
- Mga aplikasyon na madalas ang mga request dahil sa pagiging cost-effective nito  
- Mga code task na nangangailangan ng mababang latency tulad ng review at mga suhestiyon sa code

## Paghahambing ng Mistral Small at Mistral Large

Para ipakita ang pagkakaiba sa latency ng Mistral Small at Large, patakbuhin ang mga sumusunod na cells.

Makikita mo ang pagkakaiba sa oras ng tugon na nasa pagitan ng 3-5 segundo. Pansinin din ang haba at estilo ng tugon sa parehong prompt.

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

Kumpara sa dalawang modelong tinalakay sa araling ito, ang Mistral NeMo lamang ang libreng modelo na may Apache2 License.

Tinuturing itong upgrade mula sa naunang open source LLM ng Mistral, ang Mistral 7B.

Ilan pang mga katangian ng NeMo model ay:

- *Mas epektibong tokenization:* Ginagamit ng modelong ito ang Tekken tokenizer kumpara sa mas karaniwang ginagamit na tiktoken. Nagbibigay ito ng mas mahusay na performance sa mas maraming wika at code.

- *Finetuning:* Available ang base model para sa finetuning. Nagbibigay ito ng mas malaking flexibility para sa mga use-case na nangangailangan ng finetuning.

- *Native Function Calling* - Tulad ng Mistral Large, sinanay ang modelong ito sa function calling. Ginagawa nitong kakaiba ito bilang isa sa mga unang open source models na may ganitong kakayahan.

### Paghahambing ng mga Tokenizer

Sa sample na ito, titingnan natin kung paano hinahandle ng Mistral NeMo ang tokenization kumpara sa Mistral Large.

Parehong gumagamit ng parehong prompt ang dalawang sample ngunit makikita mong mas kaunti ang tokens na ibinabalik ng NeMo kumpara sa Mistral Large.

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

## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang paglalakbay

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.