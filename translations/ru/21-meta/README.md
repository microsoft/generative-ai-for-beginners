<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:05:41+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ru"
}
-->
# Создание с моделями семейства Meta

## Введение

Этот урок охватывает:

- Исследование двух основных моделей семейства Meta - Llama 3.1 и Llama 3.2
- Понимание случаев использования и сценариев для каждой модели
- Пример кода, демонстрирующий уникальные особенности каждой модели

## Семейство моделей Meta

В этом уроке мы изучим 2 модели из семейства Meta или "Llama Herd" - Llama 3.1 и Llama 3.2

Эти модели представлены в различных вариантах и доступны на торговой площадке GitHub Model. Вот дополнительные подробности о том, как использовать модели GitHub для [прототипирования с AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианты моделей:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Примечание: Llama 3 также доступна на GitHub Models, но не будет рассмотрена в этом уроке*

## Llama 3.1

С 405 миллиардами параметров Llama 3.1 относится к категории открытых LLM.

Эта модель является обновлением предыдущего выпуска Llama 3 и предлагает:

- Более широкий контекстный окно - 128k токенов против 8k токенов
- Увеличенное максимальное количество выходных токенов - 4096 против 2048
- Лучшая поддержка многоязычности - благодаря увеличению количества тренировочных токенов

Это позволяет Llama 3.1 справляться с более сложными случаями использования при создании приложений GenAI, включая:
- Вызов встроенных функций - возможность вызывать внешние инструменты и функции вне рабочего процесса LLM
- Улучшенная производительность RAG - благодаря более широкому контекстному окну
- Генерация синтетических данных - возможность создавать эффективные данные для задач, таких как тонкая настройка

### Вызов встроенных функций

Llama 3.1 была оптимизирована для более эффективного выполнения вызовов функций или инструментов. У нее также есть два встроенных инструмента, которые модель может идентифицировать как необходимые для использования на основе запроса пользователя. Эти инструменты:

- **Brave Search** - можно использовать для получения актуальной информации, такой как погода, выполняя поиск в интернете
- **Wolfram Alpha** - можно использовать для более сложных математических расчетов, поэтому написание собственных функций не требуется

Вы также можете создавать свои собственные инструменты, которые LLM может вызывать.

В примере кода ниже:

- Мы определяем доступные инструменты (brave_search, wolfram_alpha) в системном запросе.
- Отправляем запрос пользователя, который спрашивает о погоде в определенном городе.
- LLM ответит вызовом инструмента Brave Search, который будет выглядеть так `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примечание: Этот пример только выполняет вызов инструмента, если вы хотите получить результаты, вам нужно будет создать бесплатный аккаунт на странице Brave API и определить саму функцию*

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

Несмотря на то, что Llama 3.1 является LLM, одним из ее ограничений является мультимодальность. То есть способность использовать разные типы ввода, такие как изображения, в качестве запросов и предоставлять ответы. Эта возможность является одной из основных особенностей Llama 3.2. Эти функции также включают:

- Мультимодальность - возможность оценивать как текстовые, так и визуальные запросы
- Вариации от малого до среднего размера (11B и 90B) - это обеспечивает гибкие варианты развертывания,
- Вариации только для текста (1B и 3B) - это позволяет модели развертываться на периферийных / мобильных устройствах и обеспечивает низкую задержку

Поддержка мультимодальности представляет собой большой шаг в мире открытых моделей. Пример кода ниже принимает как изображение, так и текстовый запрос, чтобы получить анализ изображения от Llama 3.2 90B.

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

После завершения этого урока, ознакомьтесь с нашей [коллекцией обучения Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить совершенствование ваших знаний в области Generative AI!

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на родном языке следует считать авторитетным источником. Для критической информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.