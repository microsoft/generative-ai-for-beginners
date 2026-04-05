# Paggawa gamit ang Mga Mistral na Modelo

## Panimula

Saklaw ng leksyon na ito:  
- Pagsusuri sa iba't ibang mga Mistral na Modelo  
- Pag-unawa sa mga gamit at senaryo para sa bawat modelo  
- Pagsusuri ng mga halimbawa ng kodigo na nagpapakita ng natatanging mga tampok ng bawat modelo.

## Ang mga Mistral na Modelo

Sa leksyon na ito, susuriin natin ang 3 magkakaibang Mistral na modelo:  
**Mistral Large**, **Mistral Small** at **Mistral Nemo**.

Ang bawat isa sa mga modelong ito ay libre at makukuha sa GitHub Model marketplace. Gagamitin ang mga modelong ito sa kodigo sa notebook na ito upang patakbuhin ang mga halimbawa. Narito ang karagdagang detalye sa paggamit ng GitHub Models upang [gumawa ng prototype gamit ang AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Ang Mistral Large 2 ay kasalukuyang pangunahing modelo mula sa Mistral at idinisenyo para sa paggamit sa enterprise.

Ang modelo ay isang upgrade mula sa orihinal na Mistral Large na nag-aalok ng  
- Mas Malaking Context Window - 128k kumpara sa 32k  
- Mas mahusay na performance sa Math at Coding Tasks - 76.9% average accuracy kumpara sa 60.4%  
- Tumaas na multilingual na performance - kabilang ang mga wika: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, at Hindi.

Sa mga tampok na ito, namumukod-tangi ang Mistral Large sa  
- *Retrieval Augmented Generation (RAG)* - dahil sa mas malaking context window  
- *Function Calling* - ang modelong ito ay may native function calling na nagpapahintulot ng integrasyon sa mga panlabas na kasangkapan at API. Maaaring gawin ang mga tawag na ito nang sabay-sabay o sunod-sunod.  
- *Code Generation* - mahusay ang modelong ito sa pagbuo ng Python, Java, TypeScript, at C++ na kodigo.

### Halimbawa ng RAG gamit ang Mistral Large 2

Sa halimbawa na ito, ginagamit natin ang Mistral Large 2 upang patakbuhin ang pattern na RAG sa isang dokumento ng teksto. Ang tanong ay nakasulat sa Korean at nagtatanong tungkol sa mga gawain ng may-akda bago pumasok sa kolehiyo.

Gumagamit ito ng Cohere Embeddings Model upang lumikha ng embeddings ng dokumento ng teksto pati na rin ng tanong. Sa sample na ito, ginagamit ang package na faiss Python bilang vector store.

Ang prompt na ipinapadala sa Mistral na modelo ay kinabibilangan ng parehong mga tanong at mga nakuha na bahagi ng teksto na katulad ng tanong. Ang Modelo ay nagbibigay ng sagot sa natural na wika.

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
Ang Mistral Small ay isa pang modelo sa pamilya ng Mistral sa ilalim ng premier/enterprise na kategorya. Tulad ng ipinahihiwatig ng pangalan, ang modelong ito ay isang Small Language Model (SLM). Ang mga bentahe ng paggamit ng Mistral Small ay:  
- Tipid sa gastos kumpara sa mga Mistral LLM gaya ng Mistral Large at NeMo - 80% pagbagsak ng presyo  
- Mababang latency - mas mabilis na tugon kumpara sa mga LLM ng Mistral  
- Flexible - maaaring i-deploy sa iba't ibang mga kapaligiran na may mas kaunting mga limitasyon sa kinakailangang mga resources.  

Magaling ang Mistral Small para sa:  
- Mga gawaing nakabase sa teksto tulad ng pagbuod, pagsusuri ng damdamin at pagsasalin  
- Mga aplikasyon kung saan madalas ang mga kahilingan dahil sa pagiging cost effective nito  
- Mga gawaing may mababang latency sa kodigo katulad ng pag-review at mga suhestiyon sa kodigo

## Paghahambing ng Mistral Small at Mistral Large

Upang ipakita ang pagkakaiba sa latency ng Mistral Small at Large, patakbuhin ang mga cell sa ibaba.

Makikita mo ang diperensya sa oras ng tugon na 3-5 segundo. Pansinin din ang haba ng tugon at estilo gamit ang parehong prompt.

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

Kumpara sa dalawang nabanggit na modelo sa leksyon na ito, ang Mistral NeMo lamang ang libreng modelo na may Apache2 License.

Ito ay itinuturing na upgrade sa mas naunang open source LLM mula sa Mistral, ang Mistral 7B.

Ilan pang mga tampok ng NeMo na modelo ay:

- *Mas epektibong tokenization:* Ginagamit ng modelong ito ang Tekken tokenizer kumpara sa mas karaniwang ginagamit na tiktoken. Pinapahusay nito ang performance sa mas maraming wika at kodigo.

- *Finetuning:* Ang base model ay available para sa finetuning na nagbibigay ng mas maraming kakayahan para sa mga use-case na nangangailangan ng ganito.

- *Native Function Calling* - Tulad ng Mistral Large, ang modelong ito ay sinanay sa function calling. Ginagawa itong natatangi bilang isa sa mga unang open source na modelo na may ganitong kakayahan.

### Paghahambing ng mga Tokenizer

Sa sample na ito, titingnan natin kung paano hinahandle ng Mistral NeMo ang tokenization kumpara sa Mistral Large.

Parehong kumuha ang dalawang sample ng parehong prompt pero makikita mo na mas kakaunti ang tokens na ibinabalik ng NeMo kumpara sa Mistral Large.

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

# Bilangin ang bilang ng mga token
print(len(tokens))
```
  
```python
# I-import ang mga kinakailangang pakete:
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

# Bilangin ang dami ng mga token
print(len(tokens))
```
  
## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang paglalakbay

Matapos makumpleto ang leksyon na ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-angat ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsisikap kami ng katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sarili nitong wika ang dapat ituring bilang pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->