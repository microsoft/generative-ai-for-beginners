# Побудова з моделями Mistral

## Вступ

У цьому уроці ми розглянемо:
- Ознайомлення з різними моделями Mistral
- Розуміння варіантів використання та сценаріїв для кожної моделі
- Ознайомлення з прикладами коду, які демонструють унікальні можливості кожної моделі.

## Моделі Mistral

У цьому уроці ми розглянемо 3 різні моделі Mistral:
**Mistral Large**, **Mistral Small** та **Mistral Nemo**.

Кожна з цих моделей доступна безкоштовно на GitHub Model marketplace. Код у цій зошиті використовує ці моделі для запуску коду. Ось більше деталей про використання GitHub Models для [прототипування з AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 наразі є флагманською моделлю від Mistral і призначена для корпоративного використання.

Ця модель є оновленням оригінальної Mistral Large, пропонуючи:
- Більше контекстне вікно – 128k проти 32k
- Кращу продуктивність у задачах математики та програмування – в середньому 76,9% проти 60,4%
- Покращену багатомовну продуктивність – мови включають: англійську, французьку, німецьку, іспанську, італійську, португальську, нідерландську, російську, китайську, японську, корейську, арабську та хінді.

З цими можливостями Mistral Large відмінно підходить для:
- *Retrieval Augmented Generation (RAG)* – завдяки більшому контекстному вікну
- *Виклик функцій* – ця модель має нативний виклик функцій, що дозволяє інтеграцію з зовнішніми інструментами та API. Виклики можуть виконуватися як паралельно, так і послідовно.
- *Генерації коду* – ця модель відмінно справляється з генерацією Python, Java, TypeScript та C++.

### Приклад RAG за допомогою Mistral Large 2

У цьому прикладі ми використовуємо Mistral Large 2 для запуску патерну RAG над текстовим документом. Питання написане корейською мовою та стосується діяльності автора до університету.

Використовується Cohere Embeddings Model для створення ембедингів текстового документа та запитання. Для цього прикладу використовується Python пакет faiss як векторне сховище.

Промпт, надісланий до моделі Mistral, включає як запитання, так і вирвані частини тексту, схожі на запитання. Модель потім надає відповідь природною мовою.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # відстань, індекс
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
Mistral Small — це ще одна модель в сімействі Mistral у категорії преміум/корпоративних моделей. Як випливає з назви, ця модель є малою мовною моделлю (SLM). Переваги використання Mistral Small полягають у наступному:
- Економія коштів у порівнянні з LLM Mistral, такими як Mistral Large і NeMo — зниження вартості на 80%
- Низька затримка — швидша відповідь у порівнянні з LLM від Mistral
- Гнучкість — може бути розгорнута в різних умовах з меншою кількістю обмежень на необхідні ресурси.

Mistral Small чудово підходить для:
- Текстових завдань, таких як підсумовування, аналіз настроїв і переклад.
- Додатків, де часто надходять запити, завдяки своїй економічності
- Завдань з низькою затримкою, пов'язаних з кодом, таких як огляд і пропозиції щодо коду

## Порівняння Mistral Small і Mistral Large

Щоб показати різницю у затримці між Mistral Small та Large, запустіть наведені нижче клітинки.

Ви повинні побачити різницю у часі відповіді від 3 до 5 секунд. Також зверніть увагу на довжину та стиль відповідей при однаковому промпті.

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

Порівняно з іншими двома моделями, обговореними в цьому уроці, Mistral NeMo є єдиною безкоштовною моделлю з ліцензією Apache2.

Вона розглядається як оновлення раніше відкритої LLM від Mistral, Mistral 7B.

Деякі інші особливості моделі NeMo:

- *Більш ефективна токенізація:* Ця модель використовує токенізатор Tekken замість більш поширеного tiktoken. Це забезпечує кращу продуктивність для більшої кількості мов і коду.

- *Файнтюнінг:* Базова модель доступна для налаштування (файнтюнінгу). Це надає більшу гнучкість для випадків використання, де потрібно налаштування.

- *Нативний виклик функцій* — як і Mistral Large, ця модель була навчена на виклики функцій. Це робить її унікальною як одну з перших відкритих моделей з такою здатністю.

### Порівняння токенізаторів

У цьому прикладі ми розглянемо, як Mistral NeMo обробляє токенізацію у порівнянні з Mistral Large.

Обидва приклади беруть один і той же промпт, але ви повинні побачити, що NeMo повертає менше токенів, ніж Mistral Large.

```bash
pip install mistral-common
```

```python 
# Імпортувати необхідні пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Завантажити токенізатор Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенізувати список повідомлень
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

# Порахувати кількість токенів
print(len(tokens))
```

```python
# Імпортуйте необхідні пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Завантажте токенізатор Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенізуйте список повідомлень
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

# Порахуйте кількість токенів
print(len(tokens))
```

## Навчання на цьому не завершується, продовжуйте шлях

Після завершення цього уроку перегляньте нашу [колекцію для навчання Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання з генеративного штучного інтелекту!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою служби автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->