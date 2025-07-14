<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:05:07+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "uk"
}
-->
# Робота з моделями Mistral

## Вступ

У цьому уроці ми розглянемо:  
- Ознайомлення з різними моделями Mistral  
- Розуміння випадків використання та сценаріїв для кожної моделі  
- Приклади коду, які демонструють унікальні можливості кожної моделі.

## Моделі Mistral

У цьому уроці ми розглянемо 3 різні моделі Mistral:  
**Mistral Large**, **Mistral Small** та **Mistral Nemo**.

Кожна з цих моделей доступна безкоштовно на Github Model marketplace. Код у цьому ноутбуці використовуватиме ці моделі для запуску. Детальніше про використання Github Models для [прототипування з AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 наразі є флагманською моделлю від Mistral і призначена для корпоративного використання.

Ця модель є оновленням оригінальної Mistral Large і пропонує:  
- Більше контекстне вікно — 128k проти 32k  
- Кращу продуктивність у задачах з математики та програмування — середня точність 76,9% проти 60,4%  
- Покращену багатомовність — підтримуються мови: англійська, французька, німецька, іспанська, італійська, португальська, нідерландська, російська, китайська, японська, корейська, арабська та хінді.

Завдяки цим можливостям Mistral Large відмінно підходить для:  
- *Retrieval Augmented Generation (RAG)* — завдяки великому контекстному вікну  
- *Function Calling* — ця модель має вбудовану підтримку виклику функцій, що дозволяє інтегруватися з зовнішніми інструментами та API. Виклики можуть виконуватися як паралельно, так і послідовно.  
- *Генерації коду* — модель добре справляється з генерацією коду на Python, Java, TypeScript та C++.

### Приклад RAG з використанням Mistral Large 2

У цьому прикладі ми використовуємо Mistral Large 2 для запуску патерну RAG над текстовим документом. Запитання написане корейською і стосується діяльності автора до вступу до коледжу.

Використовується Cohere Embeddings Model для створення ембеддингів текстового документа та запитання. Для цього прикладу використовується пакет faiss Python як векторне сховище.

Підказка, що надсилається моделі Mistral, містить як запитання, так і витягнуті фрагменти тексту, схожі на запитання. Модель потім надає відповідь природною мовою.

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
Mistral Small — це ще одна модель у сімействі Mistral у категорії преміум/корпоративних моделей. Як випливає з назви, це невелика мовна модель (SLM). Переваги використання Mistral Small:  
- Економія коштів у порівнянні з великими моделями Mistral, такими як Mistral Large та NeMo — зниження вартості на 80%  
- Низька затримка — швидша відповідь у порівнянні з великими моделями Mistral  
- Гнучкість — може бути розгорнута в різних середовищах з меншими вимогами до ресурсів.

Mistral Small ідеально підходить для:  
- Текстових завдань, таких як резюмування, аналіз настроїв та переклад  
- Застосунків з частими запитами завдяки економічності  
- Завдань з низькою затримкою, пов’язаних з кодом, таких як рев’ю та пропозиції коду

## Порівняння Mistral Small та Mistral Large

Щоб побачити різницю в затримці між Mistral Small та Large, запустіть наведені нижче клітинки.

Ви повинні побачити різницю у часі відповіді від 3 до 5 секунд. Також зверніть увагу на довжину та стиль відповіді на той самий запит.

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

Порівняно з двома іншими моделями, розглянутими в цьому уроці, Mistral NeMo — єдина безкоштовна модель з ліцензією Apache2.

Її вважають оновленням ранньої відкритої LLM від Mistral — Mistral 7B.

Деякі інші особливості моделі NeMo:  

- *Більш ефективна токенізація:* ця модель використовує токенізатор Tekken замість більш поширеного tiktoken. Це забезпечує кращу продуктивність для більшої кількості мов і коду.

- *Файнтюнінг:* базова модель доступна для донавчання, що дає більше гнучкості для випадків, де потрібне донавчання.

- *Вбудований виклик функцій* — як і Mistral Large, ця модель навчена виклику функцій. Це робить її унікальною як одну з перших відкритих моделей з такою можливістю.

### Порівняння токенізаторів

У цьому прикладі ми подивимося, як Mistral NeMo обробляє токенізацію у порівнянні з Mistral Large.

Обидва приклади беруть однаковий запит, але ви побачите, що NeMo повертає менше токенів у порівнянні з Mistral Large.

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

Після завершення цього уроку ознайомтеся з нашою [колекцією з навчання генеративного AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжувати підвищувати свої знання у сфері генеративного AI!

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.