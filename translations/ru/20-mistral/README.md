# Работа с моделями Mistral

## Введение

В этом уроке будут рассмотрены:
- Изучение различных моделей Mistral
- Понимание вариантов использования и сценариев для каждой модели
- Изучение примеров кода, показывающих уникальные особенности каждой модели.

## Модели Mistral

В этом уроке мы рассмотрим 3 разные модели Mistral:
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Каждая из этих моделей доступна бесплатно на [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Код в этой тетради будет использовать эти модели для запуска.

> **Примечание:** GitHub Models прекратит работу в конце июля 2026 года. Здесь вы найдете подробности об использовании [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипирования с AI-моделями.


## Mistral Large 2 (2407)
Mistral Large 2 в настоящее время является флагманской моделью от Mistral и предназначена для использования в корпоративной среде.

Модель является обновлением оригинальной Mistral Large, предлагая
- Большое окно контекста — 128k против 32k
- Лучшие показатели в математических и программных задачах — средняя точность 76,9% против 60,4%
- Повышенную многоязычную производительность — включены языки: английский, французский, немецкий, испанский, итальянский, португальский, нидерландский, русский, китайский, японский, корейский, арабский и хинди.

Благодаря этим особенностям, Mistral Large отлично подходит для
- *Retrieval Augmented Generation (RAG)* — благодаря большему окну контекста
- *Вызова функций* — эта модель поддерживает нативный вызов функций, что позволяет интегрироваться с внешними инструментами и API. Вызовы могут выполняться как параллельно, так и последовательно один за другим.
- *Генерации кода* — эта модель прекрасно справляется с генерацией на Python, Java, TypeScript и C++.

### Пример RAG с использованием Mistral Large 2

В этом примере мы используем Mistral Large 2 для выполнения шаблона RAG по текстовому документу. Вопрос написан на корейском языке и касается деятельности автора до университета.

Используется модель Cohere Embeddings для создания эмбеддингов текстового документа и вопроса. Для этого примера применяется пакет faiss Python в качестве векторного хранилища.

В запросе, отправляемом модели Mistral, содержатся как вопросы, так и извлечённые фрагменты, похожие на вопрос. Модель затем предоставляет ответ на естественном языке.

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

# Получите их со страницы "Обзор" вашего проекта Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # расстояние, индекс
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
Mistral Small — это ещё одна модель из семейства Mistral в категории премиум/корпоративных моделей. Как следует из названия, это небольшая языковая модель (SLM). Преимущества использования Mistral Small:
- Экономия средств по сравнению с LLM Mistral, такими как Mistral Large и NeMo — снижение цены на 80%
- Низкая задержка — более быстрый отклик по сравнению с LLM от Mistral
- Гибкость — может быть развернута в различных средах с меньшими ограничениями по необходимым ресурсам.


Mistral Small отлично подходит для:
- Задач, основанных на тексте, таких как суммирование, анализ тональности и перевод.
- Приложений с частыми запросами благодаря экономической эффективности
- Задач с низкой задержкой в коде, таких как обзор и предложения по коду

## Сравнение Mistral Small и Mistral Large

Чтобы увидеть разницу в задержке между Mistral Small и Large, выполните приведённые ниже ячейки.

Вы увидите разницу во времени отклика в 3-5 секунд. Также обратите внимание на длину и стиль ответов на одинаковый запрос.

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

По сравнению с двумя другими моделями, рассмотренными в этом уроке, Mistral NeMo — единственная бесплатная модель с лицензией Apache2.

Она рассматривается как улучшение предыдущей открытой LLM от Mistral, Mistral 7B.

Некоторые другие особенности модели NeMo:

- *Более эффективная токенизация:* Эта модель использует токенизатор Tekken вместо более распространённого tiktoken. Это обеспечивает лучшую производительность для большего числа языков и кода.

- *Дополнительная настройка:* Базовая модель доступна для тонкой настройки, что дает большую гибкость для сценариев, где требуется дообучение.

- *Нативный вызов функций* — как и Mistral Large, эта модель обучена работе с вызовом функций. Это делает её уникальной одной из первых открытых моделей с такой возможностью.


### Сравнение токенизаторов

В этом примере мы рассмотрим, как Mistral NeMo справляется с токенизацией по сравнению с Mistral Large.

В обеих примерах используется один и тот же запрос, но вы увидите, что NeMo возвращает меньше токенов, чем Mistral Large.

```bash
pip install mistral-common
```

```python 
# Импорт необходимых пакетов:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Загрузка токенизатора Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизация списка сообщений
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

# Подсчет количества токенов
print(len(tokens))
```

```python
# Импорт необходимых пакетов:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Загрузка токенизатора Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизация списка сообщений
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

# Подсчет количества токенов
print(len(tokens))
```

## Обучение не заканчивается здесь, продолжайте путь

После завершения этого урока ознакомьтесь с нашей [коллекцией по обучению генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжать повышать свои знания в генеративном ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->