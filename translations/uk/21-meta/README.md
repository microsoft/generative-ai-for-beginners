# Робота з моделями родини Meta 

## Вступ 

У цьому уроці розглянемо: 

- Дослідження двох основних моделей родини Meta — Llama 3.1 і Llama 3.2, а також доступних альтернатив, що використовуються у прикладах коду (Llama 3.3 і Llama 4) 
- Розуміння випадків використання і сценаріїв для кожної моделі 
- Приклад коду, щоб показати унікальні особливості кожної моделі 


## Родина моделей Meta 

У цьому уроці ми розглянемо 2 моделі з родини Meta або "стадо Llama" — Llama 3.1 і Llama 3.2. Виконувані приклади коду використовують Llama 3.3 і Llama 4, які наразі є доступними альтернативами в каталозі Microsoft Foundry Models.

Ці моделі існують у різних варіантах і доступні в [каталозі Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Примітка:** GitHub Models буде закрито наприкінці липня 2026 року. Ось більше інформації про використання [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипування з моделями штучного інтелекту.

> **Примітка:** Конкретні версії моделей, на яких був спочатку написаний цей урок (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), згодом були вилучені з каталогу Microsoft Foundry Models. Приклади коду нижче використовують `Llama-3.3-70B-Instruct` і `Llama-4-Scout-17B-16E-Instruct` як наразі доступні альтернативи у каталозі Microsoft Foundry Models, тому вони досі працюють.

Варіанти моделей (як було спочатку описано в цьому уроці): 
- Llama 3.1 — 70B Instruct (знято з використання) 
- Llama 3.1 — 405B Instruct (знято з використання) 
- Llama 3.2 — 11B Vision Instruct (знято з використання) 
- Llama 3.2 — 90B Vision Instruct (знято з використання) 

Наразі доступні альтернативи, які використовуються у прикладах коду: 
- Llama 3.3 — 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout — 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Примітка: Варіанти Llama 3, згадані вище, збережені для історичного контексту і більше не доступні у Microsoft Foundry Models.*

## Llama 3.1 

Модель Llama 3.1 має 405 мільярдів параметрів і належить до категорії відкритих моделей LLM. 

Модель є оновленням попередньої версії Llama 3, пропонуючи: 

- Більше вікно контексту — 128 тис. токенів замість 8 тис. токенів 
- Більше максимальна кількість вихідних токенів — 4096 замість 2048 
- Кращу багатомовну підтримку — за рахунок збільшення кількості токенів, використаних для навчання 

Це дозволяє Llama 3.1 працювати з більш складними випадками використання при створенні застосунків GenAI, таких як: 
- Вбудований виклик функцій — можливість викликати зовнішні інструменти та функції поза робочим процесом LLM
- Поліпшена продуктивність RAG — завдяки більшому вікну контексту 
- Генерація синтетичних даних — можливість створювати ефективні дані для таких завдань, як донавчання 

### Вбудований виклик функцій 

Llama 3.1 була дороблена для більш ефективного виклику функцій або інструментів. Вона також має два вбудовані інструменти, які модель може ідентифікувати як потрібні для використання за підказкою користувача. Ці інструменти є: 

- **Brave Search** — може використовуватися для отримання актуальної інформації, наприклад про погоду, шляхом веб-пошуку 
- **Wolfram Alpha** — може використовуватися для більш складних математичних обчислень, тому немає потреби писати власні функції. 

Ви також можете створити власні інструменти, які LLM зможе викликати. 

У прикладі коду нижче: 

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) у системному промпті. 
- Відправляємо підказку користувача, що запитує про погоду у певному місті. 
- LLM відповість викликом інструменту Brave Search, що виглядатиме так `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Примітка: цей приклад лише здійснює виклик інструменту, якщо ви хочете отримати результати, потрібно створити безкоштовний обліковий запис на сторінці Brave API і визначити саму функцію.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Незважаючи на те, що Llama 3.1 є LLM, одним із обмежень є відсутність мультимодальності — тобто неможливість використовувати різні типи вводу, як-от зображення, як підказки та надавати на них відповіді. Ця здатність є однією з основних особливостей Llama 3.2. Інші особливості включають: 

- Мультимодальність — здатність обробляти як текстові, так і візуальні підказки 
- Варіанти малого та середнього розміру (11B і 90B) — це надає гнучкі варіанти розгортання, 
- Варіанти лише з текстом (1B і 3B) — це дозволяє розгортати модель на периферійних / мобільних пристроях та забезпечує низьку затримку 

Підтримка мультимодальності є великим кроком у світі відкритих моделей. Наведений нижче приклад коду приймає і зображення, і текстову підказку для отримання аналізу зображення. Оскільки Llama 3.2 90B Vision Instruct була знята з використання, приклад використовує `Llama-4-Scout-17B-16E-Instruct`, наразі доступну нативно мультимодальну альтернативу. 


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Навчання не закінчується на цьому, продовжуйте шлях

Після завершення цього уроку ознайомтеся з нашою [колекцією Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжувати вдосконалювати свої знання у галузі генеративного ШІ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->