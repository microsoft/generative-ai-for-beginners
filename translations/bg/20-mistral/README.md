# Работа с модели Mistral

## Въведение

Този урок ще обхване:
- Изследване на различните модели Mistral
- Разбиране на случаите на употреба и сценарии за всеки модел
- Изследване на примерен код, който показва уникалните характеристики на всеки модел.

## Моделите Mistral

В този урок ще разгледаме 3 различни модела Mistral:
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Всеки от тези модели е достъпен безплатно на GitHub Model marketplace. Кодът в този ноутбук ще използва тези модели за изпълнение на кода. Ето повече подробности за използването на GitHub Models за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 в момента е водещият модел от Mistral и е предназначен за корпоративна употреба.

Моделът е ъпгрейд на оригиналния Mistral Large, като предлага
- По-голям контекстен прозорец - 128k срещу 32k
- По-добра производителност при задачи по математика и програмиране - средна точност 76.9% срещу 60.4%
- Повишена многоезична производителност - езици включват: английски, френски, немски, испански, италиански, португалски, холандски, руски, китайски, японски, корейски, арабски и хинди.

С тези характеристики Mistral Large се отличава в
- *Retrieval Augmented Generation (RAG)* - поради по-големия контекстен прозорец
- *Function Calling* - този модел има вградена поддръжка за извикване на функции, което позволява интеграция с външни инструменти и API-та. Тези повиквания могат да се извършват паралелно или едно след друго последователно.
- *Генериране на код* - този модел се представя отлично при генериране на Python, Java, TypeScript и C++.

### Пример за RAG с Mistral Large 2

В този пример използваме Mistral Large 2 за изпълнение на RAG модел върху текстов документ. Въпросът е написан на корейски и пита за дейностите на автора преди университета.

Използва се моделът Cohere Embeddings за създаване на вграждания на текста в документа, както и на въпроса. За този пример се използва faiss Python пакет като векторно хранилище.

Подканата, изпратена към модела Mistral, включва както въпросите, така и извлечените части от текста, които са сходни с въпроса. Моделът след това предоставя отговор на естествен език.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # разстояние, индекс
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
Mistral Small е друг модел от семейството на Mistral в категорията премиум/корпоративни модели. Както подсказва името, този модел е малък езиков модел (SLM). Предимствата на Mistral Small са, че той е:
- Икономичен в сравнение с Mistral LLM модели като Mistral Large и NeMo - 80% по-ниска цена
- Ниска латентност - по-бърз отговор в сравнение с LLM моделите на Mistral
- Гъвкав - може да бъде разположен в различни среди с по-малко ограничения за необходимите ресурси.

Mistral Small е отличен за:
- Задачи с текст като обобщаване, анализ на настроения и превод.
- Приложения, където се правят чести заявки поради икономичността му
- Задачи с код с ниска латентност като преглед и предложения за код

## Сравнение между Mistral Small и Mistral Large

За да покажем разликите в латентността между Mistral Small и Large, изпълнете долните клетки.

Трябва да видите разлика в времето за отговор между 3-5 секунди. Също така обърнете внимание на дължините и стила на отговорите за една и съща подканваща фраза.

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

В сравнение с другите два модела, обсъдени в този урок, Mistral NeMo е единственият безплатен модел с лиценз Apache2.

Той се разглежда като ъпгрейд на по-ранния отворен модел LLM от Mistral, Mistral 7B.

Някои други характеристики на NeMo модела са:

- *По-ефективна токенизация:* Този модел използва токенизатор Tekken вместо по-често използвания tiktoken. Това позволява по-добра производителност при повече езици и код.

- *Финетюнинг:* Базовият модел е наличен за финетюнинг. Това дава повече гъвкавост за случаи на употреба, където е необходима донастройка.

- *Вградено извикване на функции* - Както Mistral Large, този модел е обучаван за извикване на функции. Това го прави уникален като един от първите отворени модели с такава възможност.

### Сравнение на токенизатори

В този пример ще разгледаме как Mistral NeMo обработва токенизация в сравнение с Mistral Large.

И двата примера използват една и съща подканваща фраза, но трябва да видите, че NeMo връща по-малко токени от Mistral Large.

```bash
pip install mistral-common
```

```python 
# Импортиране на необходимите пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Зареждане на токенизатора Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизиране на списък с съобщения
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

# Броене на броя токени
print(len(tokens))
```

```python
# Импортиране на необходимите пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Зареждане на токенизатора Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизиране на списък с съобщения
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

# Броене на броя на токените
print(len(tokens))
```

## Обучението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [колекция за учене на Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да усъвършенствате знанията си за Генеративен AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен чрез AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия първоначален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->