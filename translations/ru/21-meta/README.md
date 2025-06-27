<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:25:49+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ru"
}
-->
# Построение с моделями семейства Meta

## Введение

Этот урок охватывает:

- Исследование двух основных моделей семейства Meta - Llama 3.1 и Llama 3.2
- Понимание случаев использования и сценариев для каждой модели
- Пример кода, демонстрирующий уникальные особенности каждой модели

## Семейство моделей Meta

В этом уроке мы исследуем 2 модели из семейства Meta или "Стадо Llama" - Llama 3.1 и Llama 3.2.

Эти модели имеют различные варианты и доступны на GitHub Model marketplace. Здесь представлены дополнительные детали по использованию GitHub Models для [прототипирования с AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианты моделей:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Примечание: Llama 3 также доступна на GitHub Models, но не будет рассмотрена в этом уроке.*

## Llama 3.1

С 405 миллиардами параметров Llama 3.1 входит в категорию открытых LLM.

Модель является улучшением предыдущего выпуска Llama 3, предлагая:

- Большое окно контекста - 128k токенов против 8k токенов
- Большое максимальное количество выходных токенов - 4096 против 2048
- Лучшая многоязычная поддержка - благодаря увеличению количества обучающих токенов

Это позволяет Llama 3.1 справляться с более сложными случаями использования при создании приложений GenAI, включая:
- Вызов встроенных функций - возможность вызывать внешние инструменты и функции вне рабочего процесса LLM
- Улучшенная производительность RAG - благодаря увеличенному окну контекста
- Генерация синтетических данных - возможность создавать эффективные данные для задач, таких как дообучение

### Вызов встроенных функций

Llama 3.1 была доработана для более эффективного выполнения вызовов функций или инструментов. У нее также есть два встроенных инструмента, которые модель может определить как необходимые для использования на основе запроса от пользователя. Эти инструменты:

- **Brave Search** - может использоваться для получения актуальной информации, такой как погода, путем выполнения веб-поиска
- **Wolfram Alpha** - может использоваться для более сложных математических расчетов, поэтому написание собственных функций не требуется.

Вы также можете создать свои собственные пользовательские инструменты, которые LLM может вызвать.

В примере кода ниже:

- Мы определяем доступные инструменты (brave_search, wolfram_alpha) в системном запросе.
- Отправляем пользовательский запрос, который спрашивает о погоде в определенном городе.
- LLM ответит вызовом инструмента Brave Search, который будет выглядеть так: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примечание: Этот пример только делает вызов инструмента, если вы хотите получить результаты, вам нужно создать бесплатный аккаунт на странице Brave API и определить саму функцию.*

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

Несмотря на то, что Llama 3.1 является LLM, одним из ее ограничений является мультимодальность. То есть возможность использовать различные типы ввода, такие как изображения, в качестве подсказок и предоставлять ответы. Эта возможность является одной из основных особенностей Llama 3.2. Эти особенности также включают:

- Мультимодальность - имеет возможность оценивать как текстовые, так и графические подсказки
- Варианты малого и среднего размера (11B и 90B) - это обеспечивает гибкие варианты развертывания,
- Варианты только текста (1B и 3B) - это позволяет модели быть развернутой на периферийных / мобильных устройствах и обеспечивает низкую задержку

Поддержка мультимодальности представляет собой большой шаг в мире открытых моделей. Пример кода ниже принимает как изображение, так и текстовую подсказку, чтобы получить анализ изображения от Llama 3.2 90B.

### Поддержка мультимодальности с Llama 3.2

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

## Обучение не заканчивается здесь, продолжайте путешествие

После завершения этого урока ознакомьтесь с нашей [коллекцией обучения Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить совершенствовать свои знания о Generative AI!

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке должен считаться авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.