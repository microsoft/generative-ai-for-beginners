<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:45:34+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ru"
}
-->
# Создание с моделями Mistral

## Введение

Этот урок охватывает:
- Изучение различных моделей Mistral
- Понимание вариантов использования и сценариев для каждой модели
- Примеры кода показывают уникальные особенности каждой модели.

## Модели Mistral

В этом уроке мы рассмотрим 3 различные модели Mistral: **Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Каждая из этих моделей доступна бесплатно на рынке моделей Github. Код в этом блокноте будет использовать эти модели для выполнения кода. Вот более подробная информация о использовании моделей Github для [прототипирования с AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 в настоящее время является флагманской моделью от Mistral и предназначена для использования в корпоративной среде.

Модель является улучшением оригинальной Mistral Large, предлагая
- Большое окно контекста - 128k против 32k
- Лучшее выполнение математических и кодировочных задач - средняя точность 76,9% против 60,4%
- Повышенная многозадачность - языки включают: английский, французский, немецкий, испанский, итальянский, португальский, голландский, русский, китайский, японский, корейский, арабский и хинди.

С этими функциями Mistral Large превосходит в
- *Генерация с использованием дополненного поиска (RAG)* - благодаря большому окну контекста
- *Вызов функций* - эта модель имеет встроенный вызов функций, который позволяет интеграцию с внешними инструментами и API. Эти вызовы могут выполняться как параллельно, так и последовательно.
- *Генерация кода* - эта модель превосходит в генерации Python, Java, TypeScript и C++.

### Пример RAG с использованием Mistral Large 2

В этом примере мы используем Mistral Large 2 для выполнения шаблона RAG над текстовым документом. Вопрос написан на корейском языке и спрашивает о деятельности автора до колледжа.

Он использует модель Cohere Embeddings для создания векторных представлений текстового документа, а также вопроса. Для этого примера используется пакет faiss Python в качестве хранилища векторов.

Запрос, отправленный в модель Mistral, включает как вопросы, так и извлеченные фрагменты, которые похожи на вопрос. Модель затем предоставляет ответ на естественном языке.

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
Mistral Small - это еще одна модель в семействе моделей Mistral, относящихся к категории премиум/корпоративные. Как следует из названия, эта модель является малой языковой моделью (SLM). Преимущества использования Mistral Small заключаются в том, что она:
- Экономит затраты по сравнению с LLMs Mistral, такими как Mistral Large и NeMo - снижение цены на 80%
- Низкая задержка - более быстрый ответ по сравнению с LLMs Mistral
- Гибкость - может быть развернута в различных средах с меньшими ограничениями на требуемые ресурсы.

Mistral Small отлично подходит для:
- Задач, связанных с текстом, таких как суммаризация, анализ настроений и перевод.
- Приложений, где часто поступают запросы, благодаря ее экономичности
- Задач с низкой задержкой, таких как обзор и предложения кода

## Сравнение Mistral Small и Mistral Large

Чтобы показать различия в задержке между Mistral Small и Large, выполните следующие ячейки.

Вы должны увидеть разницу во времени ответа между 3-5 секунд. Также обратите внимание на длину и стиль ответа на один и тот же запрос.

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

Она рассматривается как улучшение предыдущей открытой LLM от Mistral, Mistral 7B.

Некоторые другие особенности модели NeMo:

- *Более эффективная токенизация:* Эта модель использует токенизатор Tekken вместо более распространенного tiktoken. Это позволяет добиться лучшей производительности по большему количеству языков и кода.

- *Тонкая настройка:* Базовая модель доступна для тонкой настройки. Это позволяет большей гибкости для вариантов использования, где может потребоваться тонкая настройка.

- *Встроенный вызов функций* - Как и Mistral Large, эта модель обучена на вызове функций. Это делает ее уникальной как одну из первых открытых моделей, которые это делают.

### Сравнение токенизаторов

В этом примере мы посмотрим, как Mistral NeMo обрабатывает токенизацию по сравнению с Mistral Large.

Оба примера используют один и тот же запрос, но вы должны увидеть, что NeMo возвращает меньше токенов по сравнению с Mistral Large.

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

## Обучение не останавливается здесь, продолжайте путешествие

После завершения этого урока, ознакомьтесь с нашей [коллекцией обучения генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышать свои знания о генеративном ИИ!

**Отказ от ответственности**:  
Этот документ был переведен с помощью AI-сервиса перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.