# Работа с Mistral модели 

## Въведение 

Този урок ще обхване: 
- Изследване на различните Mistral модели 
- Разбиране на употребите и сценариите за всеки модел 
- Изследване на примерен код, който показва уникалните функции на всеки модел. 

## Mistral моделите 

В този урок ще разгледаме 3 различни Mistral модела: 
**Mistral Large**, **Mistral Small** и **Mistral Nemo**. 

Всеки от тези модели е достъпен безплатно на [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Кодът в тази тетрадка ще използва тези модели за изпълнение на кода.

> **Забележка:** GitHub Models ще бъде прекратен в края на юли 2026 г. Ето повече детайли за използването на [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) за прототипиране с AI модели. 


## Mistral Large 2 (2407)
Mistral Large 2 в момента е водещият модел на Mistral и е проектиран за използване в предприятия. 

Моделът е ъпгрейд на оригиналния Mistral Large, като предлага 
- По-голям контекстен прозорец - 128k срещу 32k 
- По-добра производителност при задачи по математика и програмиране - средна точност 76.9% срещу 60.4% 
- Повишена многоезикова производителност - включва езици: английски, френски, немски, испански, италиански, португалски, холандски, руски, китайски, японски, корейски, арабски и хинди.

С тези характеристики Mistral Large се отличава в: 
- *Retrieval Augmented Generation (RAG)* - благодарение на по-големия контекстен прозорец
- *Викане на функции* - този модел има родно извикване на функции, което позволява интеграция с външни инструменти и API-та. Тези повиквания могат да се правят както паралелно, така и едно след друго в последователен ред. 
- *Генериране на код* - този модел се отличава при генериране на код на Python, Java, TypeScript и C++. 

### Пример за RAG с Mistral Large 2 

В този пример използваме Mistral Large 2 за изпълнение на RAG модел върху текстов документ. Въпросът е написан на корейски и пита за дейностите на автора преди колежа. 

Използва Cohere Embeddings модел за създаване на вграждания на текстовия документ, както и на въпроса. За този пример използва Python пакета faiss като векторно хранилище. 

Подканата, изпратена към Mistral модела, включва както въпросите, така и намерените части, които са сходни с въпроса. След това моделът предоставя отговор на естествен език. 

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
Mistral Small е друг модел от семейството Mistral в категорията премиум/предприятие. Както подсказва името, този модел е малък езиков модел (SLM). Предимствата на използване на Mistral Small са: 
- Спестяване на разходи в сравнение с Mistral LLMs като Mistral Large и NeMo - намаление на цената с 80%
- Ниска латентност - по-бърз отговор в сравнение с LLMs на Mistral
- Гъвкав - може да бъде внедрен в различни среди с по-малко ограничения за изискваните ресурси. 


Mistral Small е подходящ за: 
- Задачи, базирани на текст като обобщаване, анализ на настроения и превод. 
- Приложения, при които се правят чести заявки поради ефективност по отношение на разходите 
- Кодови задачи с ниска латентност като преглед и предложения за код 

## Сравнение между Mistral Small и Mistral Large 

За да покажем разликите в латентността между Mistral Small и Large, изпълнете долните клетки. 

Трябва да видите разлика във времето за отговор между 3-5 секунди. Също така обърнете внимание на дължината и стила на отговорите за една и съща подканваща команда.  

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

В сравнение с другите два модела, обсъдени в този урок, Mistral NeMo е единственият безплатен модел с Apache2 лиценз. 

Той се разглежда като ъпгрейд на по-ранния отворен LLM от Mistral, Mistral 7B. 

Някои други характеристики на модела NeMo са: 

- *По-ефективна токенизация:* Този модел използва Tekken токенизатора вместо по-често използвания tiktoken. Това позволява по-добра производителност при повече езици и код. 

- *Финетюнинг:* Базовият модел е достъпен за финетюнинг. Това осигурява повече гъвкавост за случаи на употреба, където финетюнинг може да е необходим. 

- *Родно извикване на функции* - Подобно на Mistral Large, този модел е обучен на извикване на функции. Това го прави уникален като един от първите отворени модели с такава възможност. 


### Сравнение между токенизаторите 

В този пример ще разгледаме как Mistral NeMo обработва токенизацията в сравнение с Mistral Large. 

И двата примера използват една и съща подканваща команда, но трябва да видите, че NeMo връща по-малко токени в сравнение с Mistral Large. 

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

# Заредете Mistral токенизатор

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизирайте списък с съобщения
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
# Импортиране на нужните пакети:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Зареди Mistral токенизатора

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Токенизирай списък със съобщения
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

# Преброй броя токени
print(len(tokens))
```

## Обучението не спира тук, продължете пътешествието

След като завършите този урок, разгледайте нашата [Колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да подобрявате знанията си за Генеративен AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->