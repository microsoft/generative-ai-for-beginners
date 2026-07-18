# Рад са Мистрал моделима 

## Увод 

Ова лекција ће обухватити: 
- Истраживање различитих Мистрал модела 
- Разумевање примене и сценарија за сваки модел 
- Истраживање примера кода који показују јединствене карактеристике сваког модела. 

## Мистрал модели 

У овој лекцији ћемо истражити 3 различита Мистрал модела: 
**Mistral Large**, **Mistral Small** и **Mistral Nemo**. 

Сваки од ових модела је доступан бесплатно на [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Код у овом ноутбуку ће користити ове моделе за извршавање кода.

> **Напомена:** GitHub Models се повлачи крајем јула 2026. Више детаља о коришћењу [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипизацију са AI моделима можете пронаћи овде. 


## Mistral Large 2 (2407)
Mistral Large 2 је тренутно водећи модел компаније Mistral и намењен је за корпоративну употребу. 

Модел је надоградња у односу на оригинални Mistral Large нудећи 
- Већи контекстний прозор - 128к уместо 32к 
- Боље перформансе на задацима из математике и програмирања - 76.9% просечне тачности уместо 60.4% 
- Побољшану мултилингвистичку подршку - језици укључују: енглески, француски, немачки, шпански, италијански, португалски, холандски, руски, кинески, јапански, корејски, арапски и хинди.

Са овим карактеристикама, Mistral Large изузетно добро ради на 
- *Retrieval Augmented Generation (RAG)* - захваљујући већем контекстном прозору
- *Function Calling* - овај модел има уграђено позивање функција што омогућава интеграцију са спољним алатима и API-јима. Ови позиви могу бити направљени и паралелно и један за другим по реду. 
- *Code Generation* - овај модел је изузетан у генерисању Питон, Јава, Тајпскрипт и Ц++ кода. 

### Пример RAG користећи Mistral Large 2 

У овом примеру користимо Mistral Large 2 да покренемо RAG образац преко текстуалног документа. Питање је написано на корејском и тражи информације о активностима аутора пре колеџа. 

Користи Cohere Embeddings модел за креирање угнежђених представки текста документа као и питања. За овај пример користи се faiss Python пакет као векторска продавница. 

Подстицај послат Мистрал моделу укључује и питања и пронађене делове текста сличне питању. Затим модел даје одговор на природном језику. 

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

# Узмите ово са странице "Преглед" вашег Microsoft Foundry пројекта
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # растојање, индекс
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
Mistral Small је још један модел из породице Мистрал у премијум/корпоративној категорији. Као што име каже, овај модел је мали језички модел (SLM). Предности коришћења Mistral Small су: 
- Уштеда трошкова у односу на веће Мистрал LLM-ове попут Mistral Large и NeMo - 80% смањења цене
- Ниска латенција - бржи одговор у поређењу са Mistral LLM-овима
- Флексибилан - може се распоредити у различитим окружењима са мање ограничења у потребним ресурсима. 


Mistral Small је одличан за: 
- Задатке засноване на тексту као што су сажимање, анализа сентимента и превођење. 
- Апликације где се врше чести захтеви због ефикасности трошкова 
- Нисколатентне задатке као што су преглед и предлози кода 

## Поређење Mistral Small и Mistral Large 

Да бисте видели разлике у латенцији између Mistral Small и Large, покрените ћелије испод. 

Требало би да видите разлику у времену одговора од 3-5 секунди. Такође обратите пажњу на дужину и стил одговора на исти подстицај.  

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

У поређењу са друга два модела обрађена у овој лекцији, Mistral NeMo је једини бесплатан модел са Apache2 лиценцом. 

Сматра се надоградњом ранијег open source LLM-а од Mistral-а, Mistral 7B. 

Неке друге карактеристике NeMo модела су: 

- *Ефикаснија токенизација:* Овај модел користи Tekken токенизатор уместо чешће коришћеног tiktoken. Ово омогућава боље перформансе преко више језика и кода. 

- *Фајнтјунирање:* Основни модел је доступан за фајнтјунирање. Ово пружа већу флексибилност за употребу у случајевима када је потребно фајнтјунирање. 

- *Нативно позивање функција* - Као и Mistral Large, овај модел је обучен за позивање функција. Ово га чини јединственим као један од првих open source модела са овом могућношћу. 


### Поређење токенизатора 

У овом примеру ћемо видети како Mistral NeMo обрађује токенизацију у поређењу са Mistral Large. 

Оба примера користе исти подстицај, али требало би да видите да NeMo враћа мање токена него Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Увези потребне пакете:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Учитај Mistral токенизер

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизуј листу порука
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

# Изброј број токена
print(len(tokens))
```

```python
# Увези потребне пакете:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Учитај Мистрал токенизер

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизуј листу порука
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

# Изброј број токена
print(len(tokens))
```

## Учити се овде не завршава, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->