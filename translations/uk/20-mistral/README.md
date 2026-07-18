# Робота з моделями Mistral 

## Вступ 

У цьому уроці розглянемо: 
- Ознайомлення з різними моделями Mistral 
- Розуміння сфери застосування та сценаріїв для кожної моделі 
- Ознайомлення з прикладами коду, що демонструють унікальні особливості кожної моделі. 

## Моделі Mistral 

У цьому уроці ми дослідимо 3 різні моделі Mistral: 
**Mistral Large**, **Mistral Small** та **Mistral Nemo**. 

Кожна з цих моделей доступна безкоштовно на [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Код у цій ноутбуці використовуватиме ці моделі для виконання.

> **Примітка:** GitHub Models буде припинено наприкінці липня 2026 року. Ось деталі про використання [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипування на основі AI моделей. 


## Mistral Large 2 (2407)
Mistral Large 2 наразі є флагманською моделлю Mistral і призначена для корпоративного використання. 

Модель є оновленням оригінальної Mistral Large, пропонуючи 
-  Більше контекстне вікно - 128k проти 32k 
-  Кращу продуктивність у задачах з математики та кодування - середня точність 76,9% проти 60,4% 
-  Покращену багатомовність - підтримувані мови: англійська, французька, німецька, іспанська, італійська, португальська, голландська, російська, китайська, японська, корейська, арабська та хінді.

Завдяки цим характеристикам Mistral Large відмінно підходить для 
- *Retrieval Augmented Generation (RAG)* - завдяки більшому контекстному вікну
- *Виклику функцій* - ця модель має нативний виклик функцій, що дозволяє інтегруватися з зовнішніми інструментами та API. Виклики можна виконувати як паралельно, так і послідовно. 
- *Генерації коду* - ця модель відмінно працює з генерацією Python, Java, TypeScript та C++. 

### Приклад RAG з використанням Mistral Large 2 

У цьому прикладі ми використовуємо Mistral Large 2 для виконання шаблону RAG над текстовим документом. Запитання написане корейською та стосується діяльності автора до вступу до коледжу. 

Використовується Cohere Embeddings Model для створення векторних уявлень текстового документа та запитання. У цьому прикладі використовується пакет faiss Python як сховище векторів. 

Запит, надісланий до моделі Mistral, включає як запитання, так і отримані частини тексту, схожі на запитання. Потім модель надає відповідь природною мовою. 

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

# Отримайте це зі сторінки "Огляд" вашого проекту Microsoft Foundry
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
Mistral Small — це інша модель у сімействі Mistral у категорії преміум/корпоративних моделей. Як зрозуміло з назви, це компактна мовна модель (SLM). Переваги використання Mistral Small такі: 
- Економія коштів у порівнянні з великими модельми Mistral, як-от Mistral Large та NeMo — зниження вартості на 80%
- Низька затримка — швидша відповідь у порівнянні з великими LLM Mistral
- Гнучкість — може бути розгорнута в різних середовищах з меншими обмеженнями на ресурси. 


Mistral Small підходить для: 
- Текстових завдань, таких як реферування, аналіз сентименту та переклад. 
- Додатків з частими запитами завдяки економічності 
- Завдань з кодування з низькою затримкою, таких як ревʼю і пропозиції щодо коду 

## Порівняння Mistral Small та Mistral Large 

Щоб показати різницю в затримці між Mistral Small та Large, виконайте наступні клітинки. 

Ви побачите різницю у часі відповіді приблизно 3-5 секунд. Також зверніть увагу на довжину та стиль відповідей на той самий запит.  

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

У порівнянні з іншими двома моделями, розглянутими у цьому уроці, Mistral NeMo — єдина безкоштовна модель з ліцензією Apache2. 

Вважається оновленням раніше відкритої LLM моделі від Mistral, Mistral 7B. 

Деякі інші характеристики моделі NeMo: 

- *Ефективніша токенізація:* ця модель використовує Tekken tokenizer замість більш поширеного tiktoken. Це забезпечує кращу продуктивність для більшої кількості мов та коду. 

- *Тонке налаштування (finetuning):* базова модель доступна для тонкого налаштування. Це дає більшу гнучкість для випадків, коли потрібне тонке налаштування. 

- *Нативний виклик функцій* — як і Mistral Large, ця модель навчена на викликах функцій. Це робить її унікальною як одну з перших відкритих моделей з такою можливістю. 


### Порівняння токенізаторів 

У цьому прикладі ми розглянемо, як Mistral NeMo обробляє токенізацію порівняно з Mistral Large. 

Обидва приклади беруть однаковий запит, але ви побачите, що NeMo повертає менше токенів, ніж Mistral Large. 

```bash
pip install mistral-common
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
# Імпортуйте потрібні пакети:
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

# Підрахуйте кількість токенів
print(len(tokens))
```

## Навчання не закінчується, продовжуйте шлях

Після завершення цього уроку перегляньте нашу [колекцію навчання генеративного AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання в генеративному AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->