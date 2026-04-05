# Работа с моделями Mistral

## Введение

В этом уроке рассмотрим:  
- Изучение различных моделей Mistral  
- Понимание областей применения и сценариев для каждой модели  
- Изучение примеров кода, демонстрирующих уникальные особенности каждой модели.  

## Модели Mistral

В этом уроке мы изучим 3 различные модели Mistral:  
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Каждая из этих моделей доступна бесплатно на GitHub Model marketplace. Код в этой тетради будет использовать эти модели для выполнения. Вот подробнее о использовании GitHub Models для [прототипирования с AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 — это в настоящее время флагманская модель от Mistral, предназначенная для корпоративного использования.

Модель является улучшением оригинальной Mistral Large, предлагая:  
- Больший контекстный окно — 128k против 32k  
- Лучшие результаты в математике и кодировании — средняя точность 76,9% против 60,4%  
- Повышенную многоязычную производительность — поддержка языков: английский, французский, немецкий, испанский, итальянский, португальский, нидерландский, русский, китайский, японский, корейский, арабский и хинди.

Благодаря этим особенностям Mistral Large отлично подходит для  
- *Retrieval Augmented Generation (RAG)* — благодаря большему контекстному окну  
- *Вызова функций* — эта модель имеет встроенный вызов функций, что позволяет интегрироваться с внешними инструментами и API. Вызовы могут выполняться как параллельно, так и последовательно один за другим.  
- *Генерации кода* — модель отлично справляется с генерацией на Python, Java, TypeScript и C++.

### Пример RAG с использованием Mistral Large 2

В этом примере используется Mistral Large 2 для выполнения шаблона RAG на текстовом документе. Вопрос написан на корейском языке и касается деятельности автора до университета.  

Используется модель встраивания Cohere Embeddings для создания эмбеддингов текста документа и вопроса. Для примера используется Python библиотека faiss в качестве векторного хранилища.

Промпт, отправляемый в модель Mistral, включает как вопросы, так и найденные фрагменты, близкие к вопросу. Модель затем дает ответ на естественном языке.

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
Mistral Small — еще одна модель из семейства Mistral в категории премиум/корпоративных. Как следует из названия, это маленькая языковая модель (SLM). Преимущества использования Mistral Small:  
- Экономия средств по сравнению с Mistral LLM, такими как Mistral Large и NeMo — снижение стоимости на 80%  
- Низкая задержка — более быстрый ответ по сравнению с LLM Mistral  
- Гибкость — может быть развернута в разных средах с меньшими требованиями к ресурсам.

Mistral Small отлично подходит для:  
- Задач обработки текста, таких как суммаризация, анализ настроений и перевод  
- Приложений с частыми запросами благодаря своей экономичности  
- Задач с низкой задержкой, связанных с кодом, таких как обзор и предложения по коду  

## Сравнение Mistral Small и Mistral Large

Чтобы увидеть разницу в задержках между Mistral Small и Large, выполните следующие ячейки.

Вы должны заметить разницу во времени ответа порядка 3-5 секунд. Также обратите внимание на длину и стиль ответа при одинаковом промпте.

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

По сравнению с двумя другими моделями, рассмотренными в этом уроке, Mistral NeMo является единственной бесплатной моделью с лицензией Apache2.

Рассматривается как улучшение более ранней открытой LLM модели от Mistral, Mistral 7B.

Некоторые другие особенности модели NeMo:

- *Более эффективная токенизация:* Эта модель использует токенизатор Tekken вместо более распространенного tiktoken. Это обеспечивает лучшую производительность при работе с большим числом языков и кода.

- *Доводка (finetuning):* Базовая модель доступна для дополнительного обучения. Это дает больше гибкости для использования в сценариях, где требуется доводка.

- *Встроенный вызов функций* — как и Mistral Large, эта модель обучена работать с вызовами функций. Это делает её уникальной, одной из первых открытых моделей с такой возможностью.

### Сравнение токенизаторов

В этом примере мы рассмотрим, как Mistral NeMo обрабатывает токенизацию по сравнению с Mistral Large.

Обе модели получают одинаковый промпт, но вы увидите, что NeMo возвращает меньше токенов, чем Mistral Large.

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

# Загрузить токенизатор Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизировать список сообщений
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

# Подсчитать количество токенов
print(len(tokens))
```
  
```python
# Импортировать необходимые пакеты:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Загрузить токенизатор Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизировать список сообщений
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

# Подсчитать количество токенов
print(len(tokens))
```
  
## Обучение на этом не заканчивается, продолжайте путь

После завершения этого урока ознакомьтесь с нашей [коллекцией по обучению генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить углублять свои знания о генеративном ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется воспользоваться услугами профессионального переводчика. Мы не несем ответственность за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->