<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:55:43+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ru"
}
-->
# Работа с моделями Mistral

## Введение

В этом уроке мы рассмотрим:  
- Различные модели Mistral  
- Сценарии и области применения каждой модели  
- Примеры кода, демонстрирующие уникальные возможности каждой модели.

## Модели Mistral

В этом уроке мы познакомимся с тремя моделями Mistral:  
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Все эти модели доступны бесплатно на Github Model marketplace. В этом блокноте мы будем использовать именно эти модели для запуска кода. Подробнее о работе с Github Models для [прототипирования с AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 — это флагманская модель от Mistral, разработанная для корпоративного использования.

Эта модель является улучшенной версией оригинальной Mistral Large и предлагает:  
- Большое окно контекста — 128k против 32k  
- Лучшие результаты в задачах по математике и программированию — средняя точность 76,9% против 60,4%  
- Повышенную производительность в многоязычной среде — поддерживаются английский, французский, немецкий, испанский, итальянский, португальский, голландский, русский, китайский, японский, корейский, арабский и хинди.

Благодаря этим возможностям Mistral Large отлично подходит для:  
- *Retrieval Augmented Generation (RAG)* — благодаря большему окну контекста  
- *Function Calling* — модель поддерживает нативный вызов функций, что позволяет интегрироваться с внешними инструментами и API. Вызовы могут выполняться как параллельно, так и последовательно.  
- *Генерация кода* — модель хорошо справляется с генерацией кода на Python, Java, TypeScript и C++.

### Пример RAG с использованием Mistral Large 2

В этом примере мы используем Mistral Large 2 для реализации паттерна RAG на текстовом документе. Вопрос задан на корейском языке и касается деятельности автора до поступления в колледж.

Для создания эмбеддингов текста и вопроса используется Cohere Embeddings Model. В этом примере в качестве векторного хранилища применяется пакет faiss для Python.

В запрос, отправляемый модели Mistral, включены как вопросы, так и извлечённые фрагменты текста, похожие на вопрос. Модель затем формирует ответ на естественном языке.

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

Mistral Small — ещё одна модель из семейства Mistral в категории премиум/корпоративных моделей. Как следует из названия, это небольшая языковая модель (SLM). Преимущества использования Mistral Small:  
- Экономия средств по сравнению с крупными моделями Mistral, такими как Mistral Large и NeMo — снижение стоимости на 80%  
- Низкая задержка — более быстрая реакция по сравнению с крупными моделями Mistral  
- Гибкость — может быть развернута в различных средах с меньшими требованиями к ресурсам.

Mistral Small отлично подходит для:  
- Текстовых задач, таких как суммирование, анализ тональности и перевод  
- Приложений с частыми запросами благодаря своей экономичности  
- Задач с низкой задержкой, например, обзора кода и предложений по улучшению кода

## Сравнение Mistral Small и Mistral Large

Чтобы увидеть разницу в задержке между Mistral Small и Large, запустите следующие ячейки.

Вы заметите разницу во времени отклика в пределах 3-5 секунд. Также обратите внимание на длину и стиль ответов на одинаковый запрос.

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

В отличие от двух предыдущих моделей, Mistral NeMo — единственная бесплатная модель с лицензией Apache2.

Её рассматривают как улучшение по сравнению с ранней открытой LLM от Mistral — Mistral 7B.

Некоторые особенности модели NeMo:  

- *Более эффективная токенизация:* Эта модель использует токенизатор Tekken вместо более распространённого tiktoken, что обеспечивает лучшую производительность для большего числа языков и кода.

- *Тонкая настройка:* Базовая модель доступна для дообучения, что даёт больше гибкости для сценариев, где требуется адаптация модели.

- *Нативный вызов функций* — как и Mistral Large, эта модель обучена работе с вызовами функций, что делает её одной из первых открытых моделей с такой возможностью.

### Сравнение токенизаторов

В этом примере мы посмотрим, как Mistral NeMo обрабатывает токенизацию по сравнению с Mistral Large.

В обоих случаях используется один и тот же запрос, но вы увидите, что NeMo возвращает меньше токенов, чем Mistral Large.

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

## Обучение не заканчивается здесь — продолжайте путь

После завершения этого урока ознакомьтесь с нашей [коллекцией по генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.