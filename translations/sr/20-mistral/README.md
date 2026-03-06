# Рад са Мистрал моделима

## Увод

Ова лекција ће обухватити:
- Истраживање различитих Мистрал модела
- Разумијевање случајева употребе и сценарија за сваки модел
- Истраживање примера кода који показују јединствене особине сваког модела.

## Мистрал модели

У овој лекцији ћемо истражити 3 различита Мистрал модела:
**Мистрал Ларге**, **Мистрал Смол** и **Мистрал Немо**.

Сви ови модели су доступни бесплатно на GitHub Model маркету. Код у овом нотебуку ће користити ове моделе за покретање кода. Ево више детаља о коришћењу GitHub Модела за [прототипирање са AI моделима](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Мистрал Ларге 2 (2407)
Мистрал Ларге 2 је тренутно водећи модел из Мистрал породице и намењен је за пословну употребу.

Модел представља унапређење у односу на оригинални Мистрал Ларге нудећи
- Већи контекстни прозор - 128k уместо 32k
- Боље перформансе у задацима из математике и кода - 76.9% просечне тачности уместо 60.4%
- Повећане вишезичне перформансе - језици укључују: енглески, француски, немачки, шпански, италијански, португалски, холандски, руски, кинески, јапански, корејски, арапски и хинди.

Са овим особинама, Мистрал Ларге одлично ради у
- *Retrieval Augmented Generation (RAG)* - због већег контекстног прозора
- *Function Calling* - овај модел има нативно позивање функција које омогућава интеграцију са екстерним алатима и API-јима. Позиви могу бити обављени паралелно или један за другим у секвенцијалном редоследу.
- *Code Generation* - овај модел одлично генерише код у Питону, Јави, TypeScript-у и C++.

### RAG пример коришћењем Мистрал Ларге 2

У овом примеру користимо Мистрал Ларге 2 за покретање РАГ шаблона преко текстуалног документа. Питање је написано на корејском и тиче се активности аутора пре факултета.

Користи Cohere Embeddings модел за креирање ембеддинга текста документа као и питања. За овај пример користи се faiss Python пакет као векторска база.

Подстицај послат Мистрал моделу обухвата и питања и пронађене делове сличне питању. Модел затим пружа одговор у природном језику.

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

## Мистрал Смол
Мистрал Смол је још један модел у Мистрал породици, у премијум/пословном сегменту. Као што име каже, овај модел је мали језички модел (SLM). Предности коришћења Мистрал Смол су:
- Уштеда трошкова у поређењу са Мистрал LLM-овима попут Мистрал Ларге и Немо - смањење цене за 80%
- Ниска латенција - бржи одговор у односу на Мистрал LLM-ове
- Флексибилан - може се имплементирати у различитим окружењима са мање ограничења у погледу потребних ресурса.

Мистрал Смол је одличан за:
- Задаке засноване на тексту као што су резимирање, анализа сентимента и превођење
- Апликације где се честим упитима постиже економичност
- Задаке са ниском латенцијом везане за код, као што су преглед и предлози кода

## Поређење Мистрал Смол и Мистрал Ларге

Да бисте видели разлике у латенцији између Мистрал Смол и Ларге, покрените ћелије испод.

Требало би да видите разлику у времену одговора између 3-5 секунди. Такође обратите пажњу на дужине и стил одговора на исти подстицај.

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

## Мистрал Немо

У поређењу са друга два модела која смо разматрали у овој лекцији, Мистрал Немо је једини бесплатни модел под Apache2 лиценцом.

Сматра се надоградњом ранијег open source LLM-а из Мистрал породице, Мистрал 7B.

Неке друге карактеристике Немо модела су:

- *Ефикаснија токенизација:* Овај модел користи Tekken токенизер уместо чешће коришћеног tiktoken-а. Ово омогућава боље перформансе на више језика и кода.

- *Фајнтунинг:* Основни модел је доступан за фајнтунинг што пружа више флексибилности у случајевима где фајнтунинг може бити потребан.

- *Нативно позивање функција* - Као и Мистрал Ларге, овај модел је обучаван за позив функција. Ово га чини јединственим као један од првих open source модела са таквом способношћу.

### Поређење токенизера

У овом примеру погледаћемо како Мистрал Немо обрађује токенизацију у поређењу са Мистрал Ларге.

Оба примера узимају исти подстицај, али требало би да видите да Немо враћа мање токена него Мистрал Ларге.

```bash
pip install mistral-common
```

```python 
# Импортујте потребне пакете:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Учитајте Mistral токенизатор

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизујте листу порука
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

# Избројте број токена
print(len(tokens))
```

```python
# Импортовање потребних пакета:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Учитавање Mistral токенизатора

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизовање листе порука
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

# Бројање броја токена
print(len(tokens))
```

## Учитиљење не престаје овде, наставите путовање

Након завршетка ове лекције, погледајте нашу [Generative AI Learning колекцију](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) за наставак унапређења знања о генеративној вештачкој интелигенцији!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да буде прецизно, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква недоразумевања или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->