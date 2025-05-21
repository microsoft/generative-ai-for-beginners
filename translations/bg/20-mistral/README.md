<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T11:03:12+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "bg"
}
-->
# Изграждане с модели Mistral

## Въведение

Този урок ще обхване:
- Изследване на различните модели Mistral
- Разбиране на случаите на употреба и сценариите за всеки модел
- Примери за код, показващи уникалните функции на всеки модел.

## Моделите Mistral

В този урок ще разгледаме 3 различни модела Mistral: **Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Всеки от тези модели е наличен безплатно на пазара за модели в Github. Кодът в тази тетрадка ще използва тези модели за изпълнение на кода. Ето още подробности за използването на моделите от Github за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 в момента е водещият модел от Mistral и е предназначен за корпоративна употреба.

Моделът е надстройка на оригиналния Mistral Large, като предлага
- По-голям контекстен прозорец - 128k срещу 32k
- По-добра производителност при математически и програмиращи задачи - 76.9% средна точност срещу 60.4%
- Повишена мултиезикова производителност - езиците включват: английски, френски, немски, испански, италиански, португалски, холандски, руски, китайски, японски, корейски, арабски и хинди.

С тези функции, Mistral Large се отличава в
- *Генериране с разширено извличане (RAG)* - поради по-големия контекстен прозорец
- *Извикване на функции* - този модел има вградено извикване на функции, което позволява интеграция с външни инструменти и API. Тези извиквания могат да бъдат направени както паралелно, така и последователно.
- *Генериране на код* - този модел се отличава в генерирането на Python, Java, TypeScript и C++.

### Пример за RAG с използване на Mistral Large 2

В този пример използваме Mistral Large 2, за да изпълним RAG модел върху текстов документ. Въпросът е написан на корейски и пита за дейностите на автора преди колежа.

Той използва Cohere Embeddings Model, за да създаде вграждания на текстовия документ, както и на въпроса. За този пример се използва faiss Python пакет като векторно хранилище.

Подканата, изпратена към модела Mistral, включва както въпросите, така и извлечените части, които са подобни на въпроса. Моделът след това предоставя отговор на естествен език.

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
Mistral Small е друг модел от семейството на Mistral моделите под категорията премиум/корпоративни. Както подсказва името, този модел е малък езиков модел (SLM). Предимствата на използването на Mistral Small са, че е:
- Икономичен в сравнение с Mistral LLMs като Mistral Large и NeMo - 80% намаление на цената
- Ниска латентност - по-бърз отговор в сравнение с LLMs на Mistral
- Гъвкав - може да бъде разположен в различни среди с по-малко ограничения върху необходимите ресурси.

Mistral Small е отличен за:
- Задачи, базирани на текст, като обобщение, анализ на настроения и превод.
- Приложения, където се правят чести заявки поради икономичността му
- Задачи с ниска латентност като преглед и предложения за код

## Сравнение на Mistral Small и Mistral Large

За да покажем разликите в латентността между Mistral Small и Large, изпълнете клетките по-долу.

Трябва да видите разлика във времето за отговор между 3-5 секунди. Също така обърнете внимание на дължините и стила на отговорите на една и съща подканя.

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

В сравнение с другите два модела, разгледани в този урок, Mistral NeMo е единственият безплатен модел с лиценз Apache2.

Той се разглежда като надстройка на по-ранния отворен източник LLM от Mistral, Mistral 7B.

Някои други функции на модела NeMo са:

- *По-ефективна токенизация:* Този модел използва Tekken токенизатор вместо по-често използвания tiktoken. Това позволява по-добра производителност при повече езици и код.

- *Финна настройка:* Основният модел е наличен за финна настройка. Това позволява повече гъвкавост за случаи на употреба, където може да е необходима финна настройка.

- *Вградено извикване на функции* - Както Mistral Large, този модел е обучен за извикване на функции. Това го прави уникален като един от първите отворени източници модели, които го правят.

### Сравнение на токенизаторите

В този пример ще разгледаме как Mistral NeMo се справя с токенизацията в сравнение с Mistral Large.

И двата примера използват една и съща подканя, но трябва да видите, че NeMo връща по-малко токени в сравнение с Mistral Large.

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

## Обучението не спира тук, продължете пътуването

След завършване на този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си за Генеративния AI!

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.