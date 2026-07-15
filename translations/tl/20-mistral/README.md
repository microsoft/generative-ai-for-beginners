# Pagtatrabaho gamit ang mga Mistral Models 

## Panimula 

Tatalakayin sa araling ito: 
- Paggalugad sa iba't ibang Mistral Models 
- Pag-unawa sa mga gamit at sitwasyon para sa bawat modelo 
- Paggalugad ng mga halimbawa ng code na nagpapakita ng mga natatanging katangian ng bawat modelo. 

## Ang mga Mistral Models 

Sa araling ito, susuriin natin ang 3 iba't ibang Mistral models: 
**Mistral Large**, **Mistral Small** at **Mistral Nemo**. 

Ang bawat isa sa mga modelong ito ay libre at matatagpuan sa [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Ang code sa notebook na ito ay gagamit ng mga modelong ito upang patakbuhin ang code.

> **Tandaan:** Ang GitHub Models ay magtatapos na sa katapusan ng Hulyo 2026. Narito ang higit pang detalye tungkol sa paggamit ng [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para sa pagbuo ng prototype gamit ang AI models. 


## Mistral Large 2 (2407)
Ang Mistral Large 2 ay kasalukuyang ang pangunahing modelo mula sa Mistral at dinisenyo para sa paggamit ng negosyo. 

Ang modelo ay upgrade mula sa orihinal na Mistral Large sa pamamagitan ng pag-aalok ng 
- Mas Malaking Context Window - 128k kumpara sa 32k 
- Mas mahusay na performance sa Math at Coding Tasks - 76.9% average accuracy kumpara sa 60.4% 
- Tumaas na multilingual na performance - kasama ang mga wika: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, at Hindi.

Sa mga katangiang ito, ang Mistral Large ay mahusay sa 
- *Retrieval Augmented Generation (RAG)* - dahil sa mas malaking context window
- *Function Calling* - ang modelong ito ay may native function calling na nagpapahintulot sa integrasyon sa mga panlabas na tools at API. Ang mga tawag na ito ay maaaring gawin nang sabay-sabay o sunud-sunod. 
- *Code Generation* - mahusay ang modelong ito sa pagbuo ng Python, Java, TypeScript at C++ na code. 

### Halimbawa ng RAG gamit ang Mistral Large 2 

Sa halimbawang ito, ginagamit natin ang Mistral Large 2 upang patakbuhin ang isang RAG pattern sa isang dokumento ng teksto. Ang tanong ay nakasulat sa Korean at nagtatanong tungkol sa mga gawain ng may-akda bago pumasok sa kolehiyo. 

Ginagamit nito ang Cohere Embeddings Model upang gumawa ng embeddings ng dokumento ng teksto pati na rin ng tanong. Para sa sample na ito, gamit ang faiss Python package bilang vector store. 

Kasama sa prompt na ipinadala sa Mistral model ang parehong mga tanong at ang mga na-retrieve na bahagi na kahawig ng tanong. Pagkatapos, nagbibigay ang Modelo ng natural na sagot sa wikang pantao. 

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

# Kunin ito mula sa iyong Microsoft Foundry proyekto na "Overview" na pahina
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distansya, indeks
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
Ang Mistral Small ay isa pang modelo sa pamilya ng Mistral models sa ilalim ng premier/enterprise na kategorya. Tulad ng ipinahihiwatig ng pangalan, ang modelong ito ay isang Small Language Model (SLM). Ang mga pakinabang ng paggamit ng Mistral Small ay: 
- Mas tipid sa gastos kumpara sa Mistral LLMs gaya ng Mistral Large at NeMo - 80% pagbaba ng presyo
- Mababa ang latency - mas mabilis ang tugon kumpara sa mga LLM ng Mistral
- Flexible - maaaring i-deploy sa iba't ibang kapaligiran nang may mas kaunting limitasyon sa mga kinakailangang resources. 


Ang Mistral Small ay mahusay para sa: 
- Mga gawaing nakabase sa teksto tulad ng pagbubuod, pagsusuri ng damdamin, at pagsasalin. 
- Mga aplikasyon na nangangailangan ng madalas na kahilingan dahil sa pagiging matipid nito 
- Mga gawain sa code na mababa ang latency tulad ng pagsusuri at mga mungkahi sa code 

## Paghahambing ng Mistral Small at Mistral Large 

Upang ipakita ang mga pinagkaiba sa latency sa pagitan ng Mistral Small at Large, patakbuhin ang mga sumusunod na cells. 

Makikita mo ang pagkakaiba sa oras ng tugon na nasa pagitan ng 3-5 segundo. Pansinin din ang haba at istilo ng tugon sa parehong prompt.  

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

Kumpara sa dalawang ibang mga modelong tinalakay sa araling ito, ang Mistral NeMo lamang ang libreng modelo na may Apache2 License. 

Tinitingnan ito bilang upgrade sa naunang open source LLM mula sa Mistral, ang Mistral 7B. 

Ilan pang mga katangian ng NeMo model ay: 

- *Mas epektibong tokenization:* Ginagamit ng modelong ito ang Tekken tokenizer sa halip na ang mas karaniwang ginagamit na tiktoken. Pinapabuti nito ang performance para sa mas maraming wika at code. 

- *Finetuning:* Ang base model ay pwede i-finetune. Nagbibigay ito ng mas maraming kakayahang umangkop para sa mga gamit na nangangailangan ng finetuning. 

- *Native Function Calling* - Tulad ng Mistral Large, sinanay ang modelong ito sa function calling. Ginagawa nitong natatangi bilang isa sa mga unang open source models na mayroon nito. 


### Paghahambing ng mga Tokenizer 

Sa sample na ito, titingnan natin kung paano hinahandle ng Mistral NeMo ang tokenization kumpara sa Mistral Large. 

Parehong sample ay kumuha ng parehong prompt ngunit makikita mo na ang NeMo ay nagbabalik ng mas kaunting tokens kaysa sa Mistral Large. 

```bash
pip install mistral-common
```

```python 
# I-import ang mga kailangang package:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# I-load ang Mistral tokenizer

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# I-tokenize ang isang listahan ng mga mensahe
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

# Bilangin ang bilang ng mga token
print(len(tokens))
```

```python
# Mag-import ng mga kinakailangang package:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# I-load ang Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# I-tokenize ang listahan ng mga mensahe
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

# Bilangin ang bilang ng mga token
print(len(tokens))
```

## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->