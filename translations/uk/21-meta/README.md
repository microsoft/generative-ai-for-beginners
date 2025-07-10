<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:14:28+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "uk"
}
-->
# Робота з моделями сімейства Meta

## Вступ

У цьому уроці ми розглянемо:

- Два основні моделі сімейства Meta — Llama 3.1 та Llama 3.2
- Застосування та сценарії використання кожної моделі
- Приклад коду, що демонструє унікальні можливості кожної моделі

## Сімейство моделей Meta

У цьому уроці ми ознайомимося з двома моделями з сімейства Meta або "Llama Herd" — Llama 3.1 та Llama 3.2

Ці моделі доступні у різних варіантах на GitHub Model marketplace. Детальніше про використання GitHub Models для [прототипування з AI-моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варіанти моделей:  
- Llama 3.1 — 70B Instruct  
- Llama 3.1 — 405B Instruct  
- Llama 3.2 — 11B Vision Instruct  
- Llama 3.2 — 90B Vision Instruct  

*Примітка: Llama 3 також доступна на GitHub Models, але в цьому уроці не розглядається*

## Llama 3.1

З 405 мільярдами параметрів, Llama 3.1 належить до категорії відкритих LLM.

Ця модель є оновленням попередньої версії Llama 3 і пропонує:

- Більше контекстне вікно — 128k токенів замість 8k  
- Більше максимальне число вихідних токенів — 4096 замість 2048  
- Покращену багатомовну підтримку — завдяки збільшенню кількості токенів для навчання  

Це дозволяє Llama 3.1 ефективно працювати з більш складними завданнями при створенні GenAI-додатків, зокрема:  
- Нативний виклик функцій — можливість викликати зовнішні інструменти та функції поза робочим процесом LLM  
- Покращена продуктивність RAG — завдяки більшому контекстному вікну  
- Генерація синтетичних даних — здатність створювати ефективні дані для таких завдань, як донавчання  

### Нативний виклик функцій

Llama 3.1 була донавчена для більш ефективного виклику функцій або інструментів. Вона також має два вбудовані інструменти, які модель може розпізнати і використовувати на основі запиту користувача. Ці інструменти:

- **Brave Search** — використовується для отримання актуальної інформації, наприклад, погоди, через веб-пошук  
- **Wolfram Alpha** — використовується для складніших математичних обчислень, що дозволяє не писати власні функції  

Ви також можете створювати власні кастомні інструменти, які LLM зможе викликати.

У наведеному нижче прикладі коду:

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) у системному запиті.  
- Надсилаємо запит користувача про погоду в певному місті.  
- LLM відповідає викликом інструменту Brave Search, який виглядає так: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примітка: цей приклад лише виконує виклик інструменту, щоб отримати результати, потрібно створити безкоштовний акаунт на сторінці Brave API та визначити саму функцію*

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

Хоча Llama 3.1 є LLM, вона має обмеження у мультимодальності — здатності використовувати різні типи вхідних даних, наприклад, зображення, як підказки та надавати відповіді. Ця можливість є однією з головних особливостей Llama 3.2. Інші особливості включають:

- Мультимодальність — здатність обробляти як текстові, так і зображення  
- Варіанти малого та середнього розміру (11B та 90B) — забезпечують гнучкі варіанти розгортання  
- Варіанти лише з текстом (1B та 3B) — дозволяють розгортати модель на edge / мобільних пристроях з низькою затримкою  

Підтримка мультимодальності — це великий крок у світі відкритих моделей. Наведений нижче приклад коду приймає як зображення, так і текстову підказку для отримання аналізу зображення від Llama 3.2 90B.

### Підтримка мультимодальності з Llama 3.2

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

## Навчання не закінчується тут, продовжуйте свій шлях

Після завершення цього уроку ознайомтеся з нашою [колекцією навчальних матеріалів з Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжувати підвищувати свої знання у сфері генеративного штучного інтелекту!

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.