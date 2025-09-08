<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:03:56+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "bg"
}
-->
# Работа с Mistral модели

## Въведение

В този урок ще разгледаме:  
- Различните Mistral модели  
- Разбиране на приложенията и сценариите за всеки модел  
- Примери с код, които показват уникалните характеристики на всеки модел.

## Mistral модели

В този урок ще разгледаме 3 различни Mistral модела:  
**Mistral Large**, **Mistral Small** и **Mistral Nemo**.

Всеки от тези модели е достъпен безплатно в Github Model marketplace. Кодът в този тетрадка ще използва тези модели за изпълнение. Повече информация за използването на Github Models за [прототипиране с AI модели](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 е в момента водещият модел на Mistral и е предназначен за корпоративна употреба.

Моделът е ъпгрейд на оригиналния Mistral Large, като предлага:  
- По-голям контекстен прозорец - 128k срещу 32k  
- По-добра производителност при задачи с математика и кодиране - средна точност 76.9% срещу 60.4%  
- Подобрена многоезична поддръжка - включва езици като: английски, френски, немски, испански, италиански, португалски, холандски, руски, китайски, японски, корейски, арабски и хинди.

С тези характеристики Mistral Large се отличава в:  
- *Retrieval Augmented Generation (RAG)* - благодарение на по-големия контекстен прозорец  
- *Function Calling* - този модел поддържа нативно извикване на функции, което позволява интеграция с външни инструменти и API-та. Тези извиквания могат да се изпълняват паралелно или последователно.  
- *Генериране на код* - моделът се справя отлично с генериране на Python, Java, TypeScript и C++.

### Пример за RAG с Mistral Large 2

В този пример използваме Mistral Large 2 за изпълнение на RAG модел върху текстов документ. Въпросът е написан на корейски и пита за дейностите на автора преди университета.

Използва се Cohere Embeddings Model за създаване на вграждания на текстовия документ и въпроса. За този пример се използва Python пакетът faiss като векторно хранилище.

Подканата, изпратена към Mistral модела, включва както въпросите, така и извлечените части от текста, които са сходни с въпроса. Моделът след това предоставя отговор на естествен език.

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

Mistral Small е друг модел от семейството на Mistral в категорията премиум/корпоративни модели. Както подсказва името, това е малък езиков модел (SLM). Предимствата на Mistral Small са:  
- Икономия на разходи в сравнение с Mistral LLM като Mistral Large и NeMo - 80% по-ниска цена  
- Ниска латентност - по-бърз отговор в сравнение с LLM моделите на Mistral  
- Гъвкавост - може да се внедрява в различни среди с по-малко изисквания към ресурсите.

Mistral Small е подходящ за:  
- Текстови задачи като обобщаване, анализ на настроения и превод  
- Приложения с чести заявки поради своята икономичност  
- Задачи с ниска латентност като преглед и предложения за код

## Сравнение между Mistral Small и Mistral Large

За да видите разликите в латентността между Mistral Small и Large, изпълнете следващите клетки.

Ще забележите разлика във времето за отговор от 3-5 секунди. Обърнете внимание и на дължината и стила на отговорите при една и съща подканваща фраза.

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

В сравнение с другите два модела, обсъдени в този урок, Mistral NeMo е единственият безплатен модел с лиценз Apache2.

Той се разглежда като ъпгрейд на по-ранния отворен код LLM на Mistral, Mistral 7B.

Някои други характеристики на NeMo модела са:

- *По-ефективна токенизация:* Този модел използва Tekken tokenizer вместо по-често използвания tiktoken. Това позволява по-добра производителност при повече езици и код.

- *Финетюнинг:* Базовият модел е достъпен за финетюнинг, което дава повече гъвкавост за случаи, в които е необходима допълнителна настройка.

- *Нативно извикване на функции* - Подобно на Mistral Large, този модел е обучен за извикване на функции. Това го прави уникален като един от първите отворени модели с такава възможност.

### Сравнение на токенизатори

В този пример ще разгледаме как Mistral NeMo обработва токенизацията в сравнение с Mistral Large.

И двата примера използват една и съща подканваща фраза, но ще видите, че NeMo връща по-малко токени в сравнение с Mistral Large.

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

## Обучението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си в областта на Генеративния AI!

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.