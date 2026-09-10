# Работа с моделями семейства Meta 

## Введение 

В этом уроке рассмотрим: 

- Исследование двух основных моделей семейства Meta — Llama 3.1 и Llama 3.2 
- Понимание случаев использования и сценариев для каждой модели 
- Пример кода, демонстрирующий уникальные возможности каждой модели 


## Семейство моделей Meta 

В этом уроке мы рассмотрим 2 модели из семейства Meta или "Llama Herd" — Llama 3.1 и Llama 3.2.

Эти модели доступны в разных вариантах в [каталоге моделей Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Примечание:** GitHub Models прекращает работу в конце июля 2026 года. Подробнее о работе с [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипирования AI-моделей.

Варианты моделей: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Примечание: Llama 3 также доступна в Microsoft Foundry Models, но не рассматривается в этом уроке*

## Llama 3.1 

При 405 миллиардах параметров Llama 3.1 относится к категории открытых LLM. 

Модель является улучшением по сравнению с предыдущей версией Llama 3, предлагая: 

- Большое окно контекста — 128k токенов вместо 8k токенов 
- Большое максимальное количество выходных токенов — 4096 вместо 2048 
- Улучшенная многоязычная поддержка — благодаря увеличению количества тренировочных токенов 

Это позволяет Llama 3.1 работать с более сложными сценариями при создании приложений GenAI, включая: 
- Вызов внешних функций — возможность вызывать внешние инструменты и функции за пределами рабочего процесса LLM
- Улучшенная производительность RAG — благодаря большему окну контекста 
- Генерация синтетических данных — возможность создавать эффективные данные для задач тонкой настройки 

### Вызов внешних функций 

Llama 3.1 была тонко настроена для более эффективного вызова функций или инструментов. В ней также есть два встроенных инструмента, которые модель может определить как необходимые для использования на основании запроса пользователя. Эти инструменты: 

- **Brave Search** — может использоваться для получения актуальной информации, например, о погоде, выполняя веб-поиск 
- **Wolfram Alpha** — может использоваться для более сложных математических вычислений, поэтому писать собственные функции не требуется. 

Вы также можете создавать свои собственные инструменты, которые LLM сможет вызывать. 

В примере кода ниже: 

- Определяем доступные инструменты (brave_search, wolfram_alpha) в системном запросе. 
- Отправляем запрос пользователя о погоде в определенном городе. 
- LLM ответит вызовом инструмента Brave Search, что будет выглядеть так `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Примечание: Этот пример только выполняет вызов инструмента, чтобы получить результаты, необходимо создать бесплатный аккаунт на странице Brave API и определить функцию.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Получите их на странице "Обзор" вашего проекта Microsoft Foundry.
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Несмотря на то, что Llama 3.1 является LLM, одним из её ограничений является отсутствие мультимодальности — то есть невозможность использовать разные типы входных данных, такие как изображения в качестве подсказок, и предоставлять ответы. Эта возможность является одной из основных особенностей Llama 3.2. К этим особенностям также относятся: 

- Мультимодальность — способность работать с текстовыми и графическими подсказками 
- Варианты малого и среднего размера (11B и 90B) — обеспечивают гибкие варианты развертывания, 
- Варианты только с текстом (1B и 3B) — позволяют развертывать модель на edge / мобильных устройствах с низкой задержкой 

Поддержка мультимодальности — большой шаг в мире открытых моделей. Пример кода ниже принимает как изображение, так и текстовую подсказку, чтобы получить анализ изображения от Llama 3.2 90B. 


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

# Получите это на странице «Обзор» вашего проекта Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## Обучение не заканчивается здесь, продолжайте развитие

После завершения этого урока ознакомьтесь с нашей [коллекцией обучения по Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжать повышать свои знания в области генеративного ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->