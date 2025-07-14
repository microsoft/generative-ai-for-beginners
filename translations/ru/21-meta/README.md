<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:06:03+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ru"
}
-->
# Создание с моделями семейства Meta

## Введение

В этом уроке мы рассмотрим:

- Два основных представителя семейства Meta — Llama 3.1 и Llama 3.2  
- Сценарии и области применения каждой модели  
- Пример кода, демонстрирующий уникальные возможности каждой модели  

## Семейство моделей Meta

В этом уроке мы познакомимся с двумя моделями из семейства Meta, или «Llama Herd» — Llama 3.1 и Llama 3.2.

Эти модели представлены в разных вариантах и доступны на GitHub Model marketplace. Подробнее о том, как использовать GitHub Models для [прототипирования с AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианты моделей:  
- Llama 3.1 — 70B Instruct  
- Llama 3.1 — 405B Instruct  
- Llama 3.2 — 11B Vision Instruct  
- Llama 3.2 — 90B Vision Instruct  

*Примечание: Llama 3 также доступна на GitHub Models, но в этом уроке не рассматривается.*

## Llama 3.1

С 405 миллиардами параметров Llama 3.1 относится к категории открытых LLM.

Эта модель является улучшенной версией предыдущей Llama 3 и предлагает:

- Большое окно контекста — 128k токенов вместо 8k  
- Увеличенный максимальный размер выходных данных — 4096 вместо 2048  
- Улучшенную поддержку нескольких языков — благодаря увеличенному объему обучающих данных  

Это позволяет Llama 3.1 справляться с более сложными задачами при создании приложений на базе генеративного ИИ, включая:  
- Вызов нативных функций — возможность обращаться к внешним инструментам и функциям вне рабочего процесса LLM  
- Улучшенную работу с RAG — благодаря большему окну контекста  
- Генерацию синтетических данных — возможность создавать эффективные данные для дообучения  

### Вызов нативных функций

Llama 3.1 была донастроена для более эффективного вызова функций и инструментов. В ней есть два встроенных инструмента, которые модель может определить и использовать в зависимости от запроса пользователя. Эти инструменты:

- **Brave Search** — позволяет получать актуальную информацию, например, погоду, выполняя веб-поиск  
- **Wolfram Alpha** — используется для сложных математических вычислений, что избавляет от необходимости писать собственные функции  

Вы также можете создавать свои собственные инструменты, которые LLM сможет вызывать.

В примере кода ниже:

- В системном промпте определены доступные инструменты (brave_search, wolfram_alpha).  
- Отправляется запрос пользователя с вопросом о погоде в определённом городе.  
- LLM отвечает вызовом инструмента Brave Search, который выглядит так: `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Примечание: в этом примере происходит только вызов инструмента. Чтобы получить результаты, необходимо создать бесплатный аккаунт на странице Brave API и определить саму функцию.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Несмотря на то, что Llama 3.1 — это LLM, у неё есть ограничение — отсутствие мультимодальности, то есть возможности использовать разные типы входных данных, например изображения, в качестве подсказок и получать ответы. Эта возможность является одной из ключевых особенностей Llama 3.2. К другим её функциям относятся:

- Мультимодальность — способность обрабатывать как текстовые, так и визуальные подсказки  
- Варианты среднего и малого размера (11B и 90B) — обеспечивают гибкие варианты развертывания  
- Варианты только с текстом (1B и 3B) — позволяют запускать модель на устройствах с ограниченными ресурсами, таких как edge или мобильные устройства, с низкой задержкой  

Поддержка мультимодальности — большой шаг вперёд в мире открытых моделей. Пример кода ниже принимает и изображение, и текстовую подсказку для анализа изображения с помощью Llama 3.2 90B.

### Мультимодальная поддержка в Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Обучение не заканчивается здесь — продолжайте путь

После прохождения этого урока ознакомьтесь с нашей [коллекцией по генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.