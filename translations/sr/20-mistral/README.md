# Рад са Мистрал моделима 

## Увод 

Ова лекција ће покрити: 
- Истраживање различитих Мистрал модела 
- Разумевање случајева коришћења и сценарија за сваки модел 
- Истраживање примера кода који показују јединствене особине сваког модела. 

## Мистрал модели 

У овој лекцији ћемо истражити 3 различита Мистрал модела: 
**Mistral Large**, **Mistral Small** и **Mistral Nemo**. 

Сваки од ових модела је доступан бесплатно на [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Код у овом нотебуку ће користити ове моделе за извршавање кода.

> **Напомена:** GitHub Models престаје да ради крајем јула 2026. године. Више детаља о коришћењу [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипове са AI моделима можете наћи овде. 


## Mistral Large 2 (2407)
Mistral Large 2 је тренутно водећи модел компаније Mistral и дизајниран је за корпоративну употребу. 

Модел је надоградња оригиналног Mistral Large нудећи 
-  Веће контекстуално окно - 128k уместо 32k 
-  Боље перформансе на математичким и програмерским задацима - 76.9% просечне тачности уместо 60.4% 
-  Повећане мултијезичке перформансе - језици укључују: енглески, француски, немачки, шпански, италијански, португалски, холандски, руски, кинески, јапански, корејски, арапски и хинди.

Са овим функцијама, Mistral Large се одлично сналази у 
- *Retrieval Augmented Generation (RAG)* - због већег контекстуалног окна
- *Function Calling* - овај модел има нативно позивање функција које омогућава интеграцију са спољним алатима и API-јима. Позиви се могу правити паралелно или један за другим у секвенцијалном редоследу. 
- *Code Generation* - овај модел се истиче у генерисању кода на Python, Java, TypeScript и C++. 

### Примерак RAG са Mistral Large 2 

У овом примеру користимо Mistral Large 2 да покренемо RAG образац преко текстуалног документа. Питање је написано на корејском и тиче се активности аутора пре факултета. 

Користи Cohere Embeddings Model за креирање угнежђивања текста документа и питања. За овај пример користи faiss Python пакет као векторску базу. 

Подстицај послат Mistral моделу укључује и питања и пронађене делове документа који су слични питању. Модел затим даје одговор у природном језику. 

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

# Преузмите ово са странице "Преглед" вашег Microsoft Foundry пројекта
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # удаљеност, индекс
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
Mistral Small је још један модел у Mistral породици модела у премијум/корпоративној категорији. Као што име каже, овај модел је мали језички модел (SLM). Предности коришћења Mistral Small су да је: 
- Економичан у односу на Mistral LLM моделе као што су Mistral Large и NeMo - пад цене за 80%
- Ниска латенција - бржи одговор у односу на друге Mistral LLM моделе
- Флексибилан - може бити распоређен у различитим окружењима са мање ограничења у потребним ресурсима. 


Mistral Small је одличан за: 
- Задацима заснованим на тексту као што су сумирање, анализа сентимента и превођење. 
- Апликације у којима се често праве захтеви због његове исплативости 
- Задаци кода са ниском латенцијом као што су преглед и предлози кода 

## Упоређивање Mistral Small и Mistral Large 

Да бисте показали разлике у латенцији између Mistral Small и Large, покрените доње ћелије. 

Требало би да видите разлику у времену одговора између 3-5 секунди. Такође обратите пажњу на дужине и стил одговора за исти подстицај.  

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

У поређењу са друга два модела обрађена у овој лекцији, Mistral NeMo је једини бесплатни модел са Apache2 лиценцом. 

Сматра се надоградњом ранијег отвореног LLM-а компаније Mistral, модела Mistral 7B. 

Неке друге карактеристике NeMo модела су: 

- *Ефикасније токенизација:* Овај модел користи Tekken токенизер уместо чешће коришћеног tiktoken. Ово омогућава боље перформансе на више језика и кода. 

- *Фине-тјунинг:* Основни модел је доступан за финетјунинг. Ово пружа већу флексибилност за случајеве коришћења где је фине-тјунинг потребан. 

- *Нативно позивање функција* - Као и Mistral Large, овај модел је обучен на позивање функција. Ово га чини јединственим као једним од првих отворених модела који то омогућавају. 


### Упоређивање токенизера 

У овом примеру, погледаћемо како Mistral NeMo обрађује токенизацију у поређењу са Mistral Large. 

Обоја узорка користе исти подстицај, али требало би да видите да NeMo враћа мање токена него Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Увези неопходне пакете:
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

# Изброји број токена
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

# Учитај Mistral тoкенизер

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

## Учитељство овде не престаје, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили с надоградњом знања о Генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->