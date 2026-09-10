# Pagtatrabaho gamit ang Mistral Models 

## Panimula 

Saklaw ng leksyong ito: 
- Pagsusuri sa iba't ibang Mistral Models 
- Pag-unawa sa mga gamit at senaryo para sa bawat modelo 
- Pagsusuri sa mga halimbawa ng code na nagpapakita ng natatanging mga tampok ng bawat modelo. 

## Ang mga Mistral Models 

Sa leksyong ito, susuriin natin ang 3 iba't ibang Mistral models: 
**Mistral Large**, **Mistral Small** at **Mistral Nemo**. 

Ang bawat isa sa mga modelong ito ay libreng makukuha sa [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Ang code sa notebook na ito ay gagamit ng mga modelong ito upang patakbuhin ang code.

> **Tandaan:** Ang GitHub Models ay titigil na sa katapusan ng Hulyo 2026. Narito ang higit pang mga detalye sa paggamit ng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para sa pag-prototype gamit ang mga AI models. 


## Mistral Large 2 (2407)
Ang Mistral Large 2 ay kasalukuyang pangunahing modelo mula sa Mistral at dinisenyo para sa paggamit ng mga negosyo. 

Ang modelo ay isang upgrade sa orihinal na Mistral Large sa pamamagitan ng pag-aalok ng 
- Mas Malaking Context Window - 128k kumpara sa 32k 
- Mas Magandang performance sa Math at Coding Tasks - 76.9% average accuracy kumpara sa 60.4% 
- Pinalakas na multilingual performance - mga wika ay kinabibilangan ng: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, at Hindi.

Sa mga tampok na ito, mahusay ang Mistral Large sa 
- *Retrieval Augmented Generation (RAG)* - dahil sa mas malaking context window
- *Function Calling* - ang modelong ito ay may katutubong function calling na nagpapahintulot ng integrasyon sa mga panlabas na tool at APIs. Ang mga tawag na ito ay maaaring gawin ng sabay-sabay o sunud-sunod. 
- *Code Generation* - mahusay ang modelong ito sa Python, Java, TypeScript at C++ na generation. 

### Halimbawa ng RAG gamit ang Mistral Large 2 

Sa halimbawang ito, ginagamit natin ang Mistral Large 2 upang patakbuhin ang RAG pattern sa isang tekstong dokumento. Ang tanong ay nakasulat sa Korean at nagtatanong tungkol sa mga gawain ng may-akda bago pumasok sa kolehiyo. 

Ginagamit nito ang Cohere Embeddings Model upang lumikha ng embeddings ng tekstong dokumento pati na rin ng tanong. Para sa sample na ito, ginagamit nito ang faiss Python package bilang vector store. 

Ang prompt na ipinadala sa Mistral model ay kinabibilangan ng mga tanong at mga nakuha na bahagi na katulad ng tanong. Ang modelo ay nagbibigay ng sagot gamit ang natural na wika. 

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

# Kunin ito mula sa pahina ng "Overview" ng iyong proyekto sa Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distansya, index
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
Ang Mistral Small ay isa pang modelo sa pamilya ng Mistral na nasa ilalim ng premier/enterprise na kategorya. Gaya ng pangalan, ang modelong ito ay isang Small Language Model (SLM). Ang mga pakinabang ng paggamit ng Mistral Small ay: 
- Nakakatipid ng gastos kumpara sa mga Mistral LLMs gaya ng Mistral Large at NeMo - 80% bawas sa presyo
- Mababang latency - mas mabilis na tugon kumpara sa mga LLMs ng Mistral
- Flexible - maaaring i-deploy sa iba’t ibang mga kapaligiran na may mas kaunting mga limitasyon sa kinakailangang mga resources. 


Ang Mistral Small ay maganda para sa: 
- Mga gawain na nakabase sa teksto tulad ng pagsasagawa ng buod, pagsusuri ng damdamin at pagsasalin. 
- Mga aplikasyon kung saan madalas ang mga kahilingan dahil ito ay cost-effective 
- Mababang latency sa mga gawain sa code tulad ng pagsusuri at mga mungkahi sa code 

## Paghahambing ng Mistral Small at Mistral Large 

Upang ipakita ang mga pagkakaiba sa latency sa pagitan ng Mistral Small at Large, patakbuhin ang mga cell sa ibaba. 

Makikita mo ang pagkakaiba sa oras ng tugon ng 3-5 segundo. Ito rin ay tandaan ang haba ng mga tugon at estilo gamit ang parehong prompt.  

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

Kumpara sa dalawang ibang modelo na tinalakay sa leksyon na ito, ang Mistral NeMo ang nag-iisang libreng modelo na may Apache2 License. 

Tinitingnan ito bilang isang upgrade sa naunang open source LLM mula sa Mistral, ang Mistral 7B. 

Ilan pang mga tampok ng NeMo model ay: 

- *Mas epektibong tokenization:* Ang modelong ito ay gumagamit ng Tekken tokenizer kumpara sa mas karaniwang ginagamit na tiktoken. Ito ay nagpapahintulot ng mas mahusay na performance para sa mas maraming mga wika at code. 

- *Finetuning:* Ang base model ay available para sa finetuning. Ito ay nagbibigay ng mas maraming flexibility para sa mga kaso ng paggamit kung saan kinakailangan ang finetuning. 

- *Katutubong Function Calling* - Gaya ng Mistral Large, ang modelong ito ay sinanay para sa function calling. Ginagawa nitong natatangi bilang isa sa mga unang open source models na gumawa nito. 


### Paghahambing ng mga Tokenizer 

Sa sample na ito, titingnan natin kung paano hinahawakan ng Mistral NeMo ang tokenization kumpara sa Mistral Large. 

Parehong mga sample ay kumuha ng parehong prompt pero mapapansin mong mas kakaunti ang token na ibinabalik ng NeMo kumpara sa Mistral Large. 

```bash
pip install mistral-common
```

```python 
# I-import ang mga kinakailangang package:
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

# Bilangin ang dami ng mga token
print(len(tokens))
```

```python
# Mag-import ng mga kailangan na pakete:
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

Pagkatapos matapos ang lekisyon na ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->