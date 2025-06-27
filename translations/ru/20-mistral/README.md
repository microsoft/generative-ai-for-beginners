<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:11:04+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ru"
}
-->
# Построение с моделями Mistral

## Введение

Этот урок охватывает:
- Исследование различных моделей Mistral
- Понимание вариантов использования и сценариев для каждой модели
- Примеры кода показывают уникальные особенности каждой модели.

## Модели Mistral

В этом уроке мы рассмотрим 3 разные модели Mistral: **Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Каждая из этих моделей доступна бесплатно на торговой площадке Github Model. Код в этой тетради будет использовать эти модели для выполнения кода. Здесь представлена дополнительная информация о том, как использовать модели Github для [прототипирования с AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 в настоящее время является флагманской моделью от Mistral и предназначена для использования в корпоративной среде.

Модель является обновлением оригинальной Mistral Large и предлагает:
- Увеличенное окно контекста - 128k против 32k
- Лучшее выполнение математических и кодировочных задач - средняя точность 76.9% против 60.4%
- Повышенная многокультурная производительность - языки включают: английский, французский, немецкий, испанский, итальянский, португальский, голландский, русский, китайский, японский, корейский, арабский и хинди.

С этими функциями Mistral Large превосходно справляется с:
- *Генерацией с увеличенным извлечением (RAG)* - благодаря большому окну контекста
- *Вызовом функций* - эта модель имеет встроенный вызов функций, что позволяет интеграцию с внешними инструментами и API. Эти вызовы могут выполняться как параллельно, так и последовательно.
- *Генерацией кода* - эта модель отлично справляется с генерацией на Python, Java, TypeScript и C++.

### Пример RAG с использованием Mistral Large 2

В этом примере мы используем Mistral Large 2 для выполнения RAG-паттерна над текстовым документом. Вопрос написан на корейском языке и спрашивает о деятельности автора до колледжа.

Он использует модель Cohere Embeddings для создания векторных представлений текстового документа и вопроса. Для этого примера используется пакет faiss Python как хранилище векторов.

Запрос, отправленный модели Mistral, включает как вопросы, так и извлеченные фрагменты, которые схожи с вопросом. Модель затем предоставляет ответ на естественном языке.

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

Mistral Small - это другая модель из семейства моделей Mistral в категории премиум/корпоративных. Как следует из названия, эта модель является малой языковой моделью (SLM). Преимущества использования Mistral Small заключаются в том, что она:
- Экономит средства по сравнению с LLM Mistral, такими как Mistral Large и NeMo - снижение цены на 80%
- Низкая задержка - более быстрый ответ по сравнению с LLM Mistral
- Гибкость - может быть развернута в различных средах с меньшими ограничениями на необходимые ресурсы.

Mistral Small отлично подходит для:
- Задач, основанных на тексте, таких как суммаризация, анализ настроений и перевод.
- Приложений, где часто делаются запросы благодаря экономической эффективности.
- Задач с низкой задержкой, таких как обзор и предложения кода.

## Сравнение Mistral Small и Mistral Large

Чтобы показать различия в задержке между Mistral Small и Large, выполните нижеуказанные ячейки.

Вы должны увидеть разницу во времени ответа между 3-5 секундами. Также обратите внимание на длину и стиль ответа на один и тот же запрос.

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

По сравнению с двумя другими моделями, обсуждаемыми в этом уроке, Mistral NeMo является единственной бесплатной моделью с лицензией Apache2.

Она рассматривается как обновление предыдущей открытой LLM от Mistral, Mistral 7B.

Некоторые другие особенности модели NeMo:

- *Более эффективная токенизация:* Эта модель использует токенизатор Tekken вместо более распространенного tiktoken. Это позволяет добиться лучшей производительности для большего количества языков и кода.

- *Тонкая настройка:* Базовая модель доступна для тонкой настройки. Это позволяет больше гибкости для случаев использования, где может понадобиться тонкая настройка.

- *Вызов встроенных функций* - Как и Mistral Large, эта модель обучена на вызове функций. Это делает ее уникальной, так как она является одной из первых открытых моделей, способных на это.

### Сравнение токенизаторов

В этом примере мы посмотрим, как Mistral NeMo обрабатывает токенизацию по сравнению с Mistral Large.

Обе модели получают один и тот же запрос, но вы должны увидеть, что NeMo возвращает меньше токенов, чем Mistral Large.

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

## Обучение не заканчивается здесь, продолжайте путь

После завершения этого урока, ознакомьтесь с нашей [коллекцией по изучению генеративного AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить углублять свои знания в области генеративного AI!

**Отказ от ответственности**:  
Этот документ был переведен с помощью AI-сервиса перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учтите, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критической информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.