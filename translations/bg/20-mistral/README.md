# Работа с модели Mistral 

## Въведение 

Този урок ще покрие: 
- Разглеждане на различните модели Mistral 
- Разбиране на употребите и сценариите за всеки модел 
- Изследване на примерен код, който показва уникалните характеристики на всеки модел. 

## Моделите Mistral 

В този урок ще разгледаме 3 различни модела Mistral: 
**Mistral Large**, **Mistral Small** и **Mistral Nemo**. 

Всеки от тези модели е наличен безплатно в [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Кодът в този бележник ще използва тези модели за изпълнение на кода.

> **Забележка:** GitHub Models се прекратява в края на юли 2026 г. Ето повече подробности за използването на [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипиране с ИИ модели. 


## Mistral Large 2 (2407)
Mistral Large 2 в момента е водещият модел от Mistral и е предназначен за корпоративна употреба. 

Моделът е подобрение на оригиналния Mistral Large, като предлага 
- По-голям контекстен прозорец - 128k срещу 32k 
- По-добра производителност при задачи по математика и кодиране - средна точност 76.9% срещу 60.4% 
- Повишена мултиезична производителност - езици включват: английски, френски, немски, испански, италиански, португалски, холандски, руски, китайски, японски, корейски, арабски и хинди.

С тези функции Mistral Large се отличава при 
- *Ретривъл-усилено генериране (RAG)* - заради по-големия контекстен прозорец
- *Извикване на функции* - този модел има родно извикване на функции, което позволява интеграция с външни инструменти и API. Тези извиквания могат да се правят както паралелно, така и едно след друго в последователен ред. 
- *Генериране на код* - този модел се отличава в генериране на Python, Java, TypeScript и C++. 

### Пример за RAG с Mistral Large 2 

В този пример използваме Mistral Large 2, за да изпълним RAG модел върху текстов документ. Въпросът е написан на корейски и пита за дейностите на автора преди колежа. 

Той използва Cohere Embeddings Model за създаване на вградания на текстовия документ и въпроса. За този пример се използва Python пакета faiss като векторно хранилище. 

Запитването, изпратено към модела Mistral, включва както въпросите, така и извлечените части, които са подобни на въпроса. Моделът след това предоставя отговор на естествен език. 

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

# Вземете ги от страницата "Преглед" на вашия проект Microsoft Foundry
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # разстояние, индекс
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
Mistral Small е друг модел от семейството на Mistral в категорията премиум/корпоративни модели. Както подсказва името, този модел е Малък езиков модел (SLM). Предимствата на Mistral Small са, че той е: 
- Икономичен в сравнение с Mistral LLM модели като Mistral Large и NeMo - 80% по-ниска цена
- Ниска латентност - по-бърз отговор в сравнение с LLM на Mistral
- Гъвкав - може да бъде внедрен в различни среди с по-малко ограничения за изискваните ресурси. 


Mistral Small е подходящ за: 
- Текстови задачи като обобщаване, анализ на настроения и превод. 
- Приложения, където често се правят заявки заради икономичността му 
- Задачи с код с ниска латентност като преглед и предложения за код 

## Сравнение между Mistral Small и Mistral Large 

За да покажем разлики в латентността между Mistral Small и Large, изпълнете следващите клетки. 

Ще видите разлика в времената за отговор между 3-5 секунди. Обърнете внимание и на дължината и стила на отговорите при същото запитване.  

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

В сравнение с другите два модела, разгледани в този урок, Mistral NeMo е единственият безплатен модел с лиценз Apache2. 

Той се разглежда като надграждане на по-ранния отворен код LLM от Mistral, Mistral 7B. 

Някои други характеристики на модела NeMo са: 

- *По-ефективна токенизация:* Този модел използва токенизатора Tekken вместо по-често използвания tiktoken. Това позволява по-добра производителност при повече езици и код. 

- *Фино настройване:* Основният модел е наличен за фино настройване. Това осигурява повече гъвкавост за случаи на употреба, където е нужно фино настройване. 

- *Родно извикване на функции* - Подобно на Mistral Large, този модел е обучен за извикване на функции. Това го прави уникален като един от първите модели с отворен код с такава способност. 


### Сравнение на токенизатори 

В този пример ще видим как Mistral NeMo обработва токенизацията в сравнение с Mistral Large. 

И в двата примера се използва една и съща заявка, но ще видите, че NeMo връща по-малко токени от Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Импортирайте необходимите пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Заредете токенизатора на Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизирайте списък със съобщения
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

# Брой на токените
print(len(tokens))
```

```python
# Импортирайте нужните пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Заредете Mistral токенизатора

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизирайте списък със съобщения
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

# Бройте броя на токените
print(len(tokens))
```

## Обучението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [колекция за обучение по генеративен ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да усъвършенствате знанията си по генеративен ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->