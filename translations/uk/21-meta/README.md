# Побудова з моделями родини Meta

## Вступ

Цей урок охоплює:

- Ознайомлення з двома основними моделями родини Meta — Llama 3.1 і Llama 3.2
- Розуміння випадків використання та сценаріїв для кожної моделі
- Приклад коду, що демонструє унікальні функції кожної моделі

## Родина моделей Meta

У цьому уроці ми розглянемо 2 моделі з родини Meta або "Llama Herd" — Llama 3.1 і Llama 3.2.

Ці моделі доступні у різних варіантах на GitHub Model marketplace. Докладніше про використання GitHub Models для [прототипування з AI моделями](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Варіанти моделей:
- Llama 3.1 — 70B Instruct
- Llama 3.1 — 405B Instruct
- Llama 3.2 — 11B Vision Instruct
- Llama 3.2 — 90B Vision Instruct

*Примітка: Llama 3 також доступна на GitHub Models, але в цьому уроці не розглядається*

## Llama 3.1

З 405 мільярдами параметрів, Llama 3.1 належить до категорії відкритих LLM.

Модель є оновленням раннього випуску Llama 3 і пропонує:

- Більше вікно контексту — 128 тис. токенів проти 8 тис. токенів
- Більше максимальне число вихідних токенів — 4096 проти 2048
- Покращену багатомовну підтримку — завдяки збільшенню кількості токенів для тренування

Це дозволяє Llama 3.1 обробляти складніші випадки використання при створенні GenAI застосунків, у тому числі:
- Нативний виклик функцій — можливість викликати зовнішні інструменти та функції поза робочим процесом LLM
- Покращена продуктивність RAG — завдяки більшому вікну контексту
- Генерація синтетичних даних — можливість створювати ефективні дані для таких завдань, як донавчання

### Нативний виклик функцій

Llama 3.1 донавчена для більш ефективного виклику функцій чи інструментів. У неї також є два вбудовані інструменти, які модель може ідентифікувати як потрібні для використання на основі запиту користувача. Ці інструменти:

- **Brave Search** — використовується для отримання актуальної інформації, наприклад, погоди, виконуючи веб-пошук
- **Wolfram Alpha** — використовується для складніших математичних обчислень, тому не потрібно писати власні функції

Ви також можете створити власні інструменти, які LLM зможе викликати.

У наведеному нижче прикладі коду:

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) у системному підказуванні.
- Надсилаємо підказку користувача з питанням про погоду в певному місті.
- LLM відповідає викликом інструменту Brave Search, що виглядає так: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Примітка: цей приклад лише робить виклик інструменту, щоб отримати результати, потрібно створити безкоштовний обліковий запис на сторінці Brave API і визначити саму функцію.

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

Хоча Llama 3.1 є LLM, одним із обмежень є відсутність мультимодальності — неможливість використовувати різні типи вхідних даних, такі як зображення, як підказки та генерувати відповіді. Ця можливість є однією з головних функцій Llama 3.2. Інші особливості включають:

- Мультимодальність — здатність оцінювати як текстові, так і зображення
- Варіанти малого та середнього розміру (11B та 90B) — забезпечують гнучкі варіанти розгортання
- Варіанти лише з текстом (1B та 3B) — дозволяють розгортати модель на пристроях на кордоні мережі / мобільних пристроях з низькою затримкою

Підтримка мультимодальності представляє великий крок у світі відкритих моделей. Наведений нижче приклад коду приймає і зображення, і текстову підказку для отримання аналізу зображення від Llama 3.2 90B.

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

## Навчання не закінчується тут, продовжуйте подорож

Після завершення цього уроку перегляньте нашу [колекцію навчання Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжувати підвищувати свої знання про генеративний ШІ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми і прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для важливої інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли у результаті використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->