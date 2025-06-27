<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:24:27+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "uk"
}
-->
# Побудова з моделями Mistral

## Вступ

Цей урок охоплює:
- Дослідження різних моделей Mistral
- Розуміння варіантів використання та сценаріїв для кожної моделі
- Зразки коду демонструють унікальні можливості кожної моделі.

## Моделі Mistral

У цьому уроці ми досліджуватимемо 3 різні моделі Mistral:
**Mistral Large**, **Mistral Small** та **Mistral Nemo**.

Кожна з цих моделей доступна безкоштовно на ринку моделей Github. Код у цьому ноутбуці буде використовувати ці моделі для виконання коду. Ось більше деталей про використання моделей Github для [прототипування з AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 наразі є флагманською моделлю від Mistral і призначена для корпоративного використання.

Модель є оновленням оригінальної Mistral Large, пропонуючи:
- Більше вікно контексту - 128k проти 32k
- Краща продуктивність у задачах математики та кодування - середня точність 76.9% проти 60.4%
- Підвищена багатомовна продуктивність - включені мови: англійська, французька, німецька, іспанська, італійська, португальська, нідерландська, російська, китайська, японська, корейська, арабська та хінді.

З цими можливостями Mistral Large відзначається в:
- *Генерація з підвищеним відтворенням (RAG)* - завдяки більшому вікну контексту
- *Виклик функцій* - ця модель має вбудований виклик функцій, що дозволяє інтеграцію з зовнішніми інструментами та API. Ці виклики можуть бути виконані як паралельно, так і послідовно один за одним.
- *Генерація коду* - ця модель відзначається в генерації Python, Java, TypeScript та C++.

### Приклад RAG з використанням Mistral Large 2

У цьому прикладі ми використовуємо Mistral Large 2 для запуску шаблону RAG над текстовим документом. Питання написано корейською мовою і запитує про діяльність автора перед коледжем.

Він використовує модель Cohere Embeddings для створення ембедингів текстового документа, а також питання. Для цього зразка використовується пакет faiss Python як векторне сховище.

Запит, надісланий моделі Mistral, включає як питання, так і отримані фрагменти, що схожі на питання. Модель потім надає відповідь природною мовою.

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
Mistral Small є ще однією моделлю в сімействі моделей Mistral під категорією преміум/корпоративний. Як випливає з назви, ця модель є малою мовною моделлю (SLM). Переваги використання Mistral Small полягають у тому, що вона:
- Економія коштів у порівнянні з Mistral LLMs, такими як Mistral Large і NeMo - зниження ціни на 80%
- Низька затримка - швидша відповідь у порівнянні з LLMs Mistral
- Гнучка - може бути розгорнута в різних середовищах з меншими обмеженнями на необхідні ресурси.

Mistral Small чудово підходить для:
- Текстових завдань, таких як узагальнення, аналіз настроїв і переклад.
- Додатків, де часто робляться запити завдяки її економічності
- Завдань коду з низькою затримкою, таких як огляд і пропозиції коду

## Порівняння Mistral Small і Mistral Large

Щоб показати різницю в затримці між Mistral Small і Large, запустіть наведені нижче клітинки.

Ви повинні побачити різницю у часі відповіді від 3 до 5 секунд. Зверніть також увагу на довжину і стиль відповіді на той самий запит.

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

У порівнянні з двома іншими моделями, обговореними в цьому уроці, Mistral NeMo є єдиною безкоштовною моделлю з ліцензією Apache2.

Вона розглядається як оновлення до попередньої відкритої LLM від Mistral, Mistral 7B.

Деякі інші особливості моделі NeMo:

- *Більш ефективна токенізація:* Ця модель використовує токенізатор Tekken замість більш поширеного tiktoken. Це дозволяє кращу продуктивність для більшої кількості мов і коду.

- *Тонке налаштування:* Базова модель доступна для тонкого налаштування. Це дозволяє більше гнучкості для варіантів використання, де може знадобитися тонке налаштування.

- *Вбудований виклик функцій* - Як і Mistral Large, ця модель була навчена на виклику функцій. Це робить її унікальною як одну з перших відкритих моделей, що робить це.

### Порівняння токенізаторів

У цьому зразку ми розглянемо, як Mistral NeMo обробляє токенізацію в порівнянні з Mistral Large.

Обидва зразки беруть той самий запит, але ви повинні побачити, що NeMo повертає менше токенів у порівнянні з Mistral Large.

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

## Навчання не закінчується тут, продовжуйте шлях

Після завершення цього уроку перегляньте нашу [колекцію навчання Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищення знань про Generative AI!

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматизованого перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.