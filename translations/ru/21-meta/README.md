# Создание с Семейством Моделей Meta

## Введение

В этом уроке будут рассмотрены:

- Исследование двух основных моделей семейства Meta — Llama 3.1 и Llama 3.2
- Понимание сценариев использования для каждой модели
- Пример кода, демонстрирующий уникальные особенности каждой модели

## Семейство моделей Meta

В этом уроке мы рассмотрим 2 модели из семейства Meta, или "стада Llama" — Llama 3.1 и Llama 3.2.

Эти модели представлены в разных вариантах и доступны на торговой площадке GitHub Model. Вот подробности о том, как использовать GitHub Models для [прототипирования с AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варианты моделей:
- Llama 3.1 — 70B Instruct
- Llama 3.1 — 405B Instruct
- Llama 3.2 — 11B Vision Instruct
- Llama 3.2 — 90B Vision Instruct

*Примечание: Llama 3 также доступна на GitHub Models, но в этом уроке не рассматривается*

## Llama 3.1

С 405 миллиардами параметров, Llama 3.1 относится к категории открытых LLM.

Модель является улучшенной версией более раннего релиза Llama 3, предлагая:

- Большое окно контекста — 128k токенов против 8k токенов
- Большое максимальное количество выходных токенов — 4096 против 2048
- Улучшенная многоязычная поддержка — за счет увеличения количества обучающих токенов

Все это позволяет Llama 3.1 обрабатывать более сложные сценарии при создании приложений GenAI, включая:
- Вызов встроенных функций — возможность вызывать внешние инструменты и функции вне рабочего процесса LLM
- Улучшенная производительность RAG — благодаря большему окну контекста
- Генерация синтетических данных — возможность создавать эффективные данные для задач, таких как дообучение

### Встроенный вызов функций

Llama 3.1 была донастроена для более эффективного вызова функций или инструментов. В ней также есть два встроенных инструмента, которые модель может определить как необходимые для использования на основе запроса пользователя. Эти инструменты:

- **Brave Search** — может использоваться для получения актуальной информации, например о погоде, через веб-поиск
- **Wolfram Alpha** — может применяться для более сложных математических вычислений, что исключает необходимость писать собственные функции

Вы также можете создавать собственные настраиваемые инструменты, которые LLM сможет вызывать.

В приведённом ниже примере кода:

- Определяются доступные инструменты (brave_search, wolfram_alpha) в системном запросе.
- Отправляется пользовательский запрос о погоде в определённом городе.
- LLM ответит вызовом инструмента Brave Search, который будет выглядеть так: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примечание: в этом примере вызывается только инструмент, если вы хотите получить результаты, вам нужно создать бесплатный аккаунт на странице API Brave и определить функцию.*

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

Несмотря на то, что это LLM, одним из ограничений Llama 3.1 является отсутствие мультимодальности. То есть, невозможность использовать различные типы входных данных, такие как изображения, в качестве подсказок и получать на них ответы. Эта возможность является одной из ключевых функций Llama 3.2. Другие особенности включают:

- Мультимодальность — способность обрабатывать как текстовые, так и графические подсказки
- Вариации малого и среднего размера (11B и 90B) — предоставляют гибкие варианты развертывания
- Вариации только с текстом (1B и 3B) — позволяют развертывать модель на периферийных/мобильных устройствах с низкой задержкой

Поддержка мультимодальности представляет собой большой шаг в мире моделей с открытым исходным кодом. Приведённый ниже пример кода принимает одновременно изображение и текстовую подсказку для анализа изображения с помощью Llama 3.2 90B.

### Мультимодальная поддержка с Llama 3.2

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

## Обучение не заканчивается здесь, продолжайте путь

После завершения этого урока ознакомьтесь с нашей [коллекцией по генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышение своих знаний в области генеративного ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервисa автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->