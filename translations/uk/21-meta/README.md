<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:37:21+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "uk"
}
-->
# Побудова з моделями родини Meta

## Вступ

Цей урок охоплює:

- Дослідження двох основних моделей родини Meta - Llama 3.1 та Llama 3.2
- Розуміння випадків використання та сценаріїв для кожної моделі
- Приклад коду для демонстрації унікальних можливостей кожної моделі

## Родина моделей Meta

У цьому уроці ми дослідимо 2 моделі з родини Meta або "Стадо Llama" - Llama 3.1 та Llama 3.2.

Ці моделі мають різні варіанти та доступні на ринку моделей GitHub. Ось більше деталей про використання GitHub Models для [створення прототипів з AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варіанти моделей:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Примітка: Llama 3 також доступна на GitHub Models, але не буде розглянута в цьому уроці*

## Llama 3.1

З 405 мільярдами параметрів, Llama 3.1 входить до категорії відкритих LLM.

Ця модель є оновленням попередньої версії Llama 3, пропонуючи:

- Більше вікно контексту - 128k токенів проти 8k токенів
- Більше максимальне число вихідних токенів - 4096 проти 2048
- Краща багатомовна підтримка - завдяки збільшенню кількості тренувальних токенів

Це дозволяє Llama 3.1 обробляти більш складні випадки використання при створенні додатків GenAI, включаючи:
- Виклик нативних функцій - можливість викликати зовнішні інструменти та функції поза робочим процесом LLM
- Краща продуктивність RAG - завдяки більшому вікну контексту
- Генерація синтетичних даних - можливість створювати ефективні дані для завдань, таких як тонке налаштування

### Виклик нативних функцій

Llama 3.1 була налаштована для більш ефективного виклику функцій або інструментів. Вона також має два вбудовані інструменти, які модель може ідентифікувати як необхідні для використання на основі підказки від користувача. Ці інструменти:

- **Brave Search** - Може бути використаний для отримання актуальної інформації, як-от погода, шляхом виконання веб-пошуку
- **Wolfram Alpha** - Може бути використаний для більш складних математичних розрахунків, тому написання власних функцій не є необхідним.

Ви також можете створити власні інструменти, які LLM може викликати.

У прикладі коду нижче:

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) у системній підказці.
- Надсилаємо користувацьку підказку, яка запитує про погоду в певному місті.
- LLM відповість викликом інструменту Brave Search, який виглядатиме так: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примітка: Цей приклад лише робить виклик інструменту, якщо ви хочете отримати результати, вам потрібно створити безкоштовний обліковий запис на сторінці API Brave та визначити саму функцію`

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

Незважаючи на те, що Llama 3.1 є LLM, однією з її обмежень є мультимодальність. Тобто, можливість використовувати різні типи вхідних даних, такі як зображення, як підказки та надавати відповіді. Ця можливість є однією з головних особливостей Llama 3.2. Ці особливості також включають:

- Мультимодальність - здатність оцінювати як текстові, так і зображувальні підказки
- Варіації малого та середнього розміру (11B та 90B) - це забезпечує гнучкі варіанти розгортання,
- Варіації лише для тексту (1B та 3B) - це дозволяє моделі бути розгорнутою на крайових / мобільних пристроях і забезпечує низьку затримку

Підтримка мультимодальності представляє великий крок у світі відкритих моделей. Приклад коду нижче приймає як зображення, так і текстову підказку для отримання аналізу зображення від Llama 3.2 90B.

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

## Навчання не закінчується тут, продовжуйте шлях

Після завершення цього уроку, перегляньте нашу [колекцію навчальних матеріалів з генеративного AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити вдосконалювати свої знання про генеративний AI!

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою служби автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.