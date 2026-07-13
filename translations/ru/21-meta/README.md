# Работа с моделями семейства Meta 

## Введение 

В этом уроке будут рассмотрены: 

- Исследование двух основных моделей семейства Meta — Llama 3.1 и Llama 3.2 
- Понимание сценариев и вариантов использования каждой модели 
- Пример кода, показывающий уникальные особенности каждой модели 


## Семейство моделей Meta 

В этом уроке мы изучим 2 модели из семейства Meta или «стада Llama» — Llama 3.1 и Llama 3.2.

Эти модели доступны в разных вариантах в [каталоге моделей Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Примечание:** GitHub Models завершает работу в конце июля 2026 года. Здесь можно найти больше информации по использованию [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипирования с AI-моделями.

Варианты моделей: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Примечание: Llama 3 также доступна в Microsoft Foundry Models, но не рассматривается в этом уроке*

## Llama 3.1 

С параметрами в 405 миллиардов Llama 3.1 относится к категории открытых LLM.

Эта модель представляет собой обновление предыдущего выпуска Llama 3, предлагая: 

- Более длинное окно контекста — 128k токенов против 8k токенов 
- Максимальное количество выходных токенов больше — 4096 против 2048 
- Более лучшую поддержку нескольких языков — за счёт увеличенного объёма обучающих токенов 

Это позволяет Llama 3.1 работать с более сложными задачами при создании приложений GenAI, включая: 
- Нативный вызов функций — возможность вызывать внешние инструменты и функции вне рабочего процесса LLM
- Лучшее выполнение RAG — благодаря большему окну контекста 
- Генерация синтетических данных — возможность создавать эффективные данные для задач, таких как дообучение 

### Нативный вызов функций 

Llama 3.1 была дополнительно настроена для более эффективного вызова функций или инструментов. У неё также есть два встроенных инструмента, которые модель может определить как необходимые к использованию на основе запроса пользователя. Эти инструменты: 

- **Brave Search** — можно использовать для получения актуальной информации, например, о погоде, выполняя веб-поиск 
- **Wolfram Alpha** — используется для более сложных математических вычислений, чтобы не требовалось писать собственные функции. 

Вы также можете создавать свои собственные пользовательские инструменты, которые LLM может вызывать. 

В примере кода ниже: 

- Мы определяем доступные инструменты (brave_search, wolfram_alpha) в системном запросе. 
- Отправляем пользовательский запрос с вопросом о погоде в определённом городе. 
- LLM ответит вызовом инструмента Brave Search, который будет выглядеть так: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Примечание: этот пример только выполняет вызов инструмента, чтобы получить результаты, вам нужно зарегистрироваться на странице Brave API и определить функцию вызова.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Получите это на странице "Обзор" вашего проекта Microsoft Foundry
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

Несмотря на то, что Llama 3.1 является LLM, одним из её ограничений является отсутствие мультимодальности — неспособность использовать различные типы вводных данных, например, изображения в качестве запросов и предоставлять ответы. Эта возможность — одна из основных особенностей Llama 3.2. Другие её особенности включают: 

- Мультимодальность — способность обрабатывать как текстовые, так и графические запросы 
- Варианты малого и среднего размера (11B и 90B) — обеспечивают гибкие варианты развёртывания, 
- Варианты только с текстом (1B и 3B) — позволяют развертывать модель на пограничных/мобильных устройствах с низкой задержкой 

Поддержка мультимодальности представляет собой большой шаг в мире моделей с открытым исходным кодом. Пример кода ниже принимает как изображение, так и текстовый запрос, чтобы получить анализ изображения с помощью Llama 3.2 90B. 


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

# Получите это на странице "Обзор" вашего проекта Microsoft Foundry
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

## Обучение не заканчивается здесь, продолжайте путь

После завершения этого урока ознакомьтесь с нашей [коллекцией по обучению генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышать свои знания в области генеративного ИИ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->