# Побудова з моделями сімейства Meta 

## Вступ 

У цьому уроці ми розглянемо: 

- Огляд двох основних моделей сімейства Meta - Llama 3.1 та Llama 3.2 
- Розуміння варіантів використання та сценаріїв для кожної моделі 
- Приклад коду, який демонструє унікальні особливості кожної моделі 


## Сімейство моделей Meta 

У цьому уроці ми дослідимо 2 моделі з сімейства Meta або "Лосицький табун" - Llama 3.1 і Llama 3.2.

Ці моделі доступні у різних варіантах і представлені в [каталозі моделей Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Примітка:** GitHub Models буде виведено з експлуатації наприкінці липня 2026 року. Детальніше про використання [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипування з AI-моделями.

Варіанти моделей: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Примітка: Llama 3 також доступна в Microsoft Foundry Models, але не розглядається в цьому уроці*

## Llama 3.1 

При 405 мільярдах параметрів, Llama 3.1 належить до категорії відкритих джерел LLM. 

Ця модель є оновленням попередньої версії Llama 3 і надає: 

- Більше контекстне вікно - 128k токенів проти 8k токенів 
- Більша максимальна кількість вихідних токенів - 4096 проти 2048 
- Покращена багатомовна підтримка - завдяки збільшенню кількості навчальних токенів 

Це дозволяє Llama 3.1 працювати з більш складними варіантами використання при створенні GenAI додатків, включаючи: 
- Рідне викликання функцій - можливість виклику зовнішніх інструментів та функцій поза робочим процесом LLM
- Покращену продуктивність RAG - завдяки більшому контекстному вікну 
- Генерація синтетичних даних - можливість створювати ефективні дані для задач, таких як тонке налаштування 

### Рідне викликання функцій 

Llama 3.1 була донавчена для більш ефективного виклику функцій або інструментів. Вона також має два вбудовані інструменти, які модель може ідентифікувати як необхідні до використання на основі підказки користувача. Ці інструменти: 

- **Brave Search** - можна використовувати для отримання актуальної інформації, такої як погода, шляхом веб-пошуку 
- **Wolfram Alpha** - можна використовувати для більш складних математичних обчислень, тому написання власних функцій не потрібне. 

Ви також можете створити власні інструменти, які LLM може викликати. 

У прикладі коду нижче: 

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) у системній підказці. 
- Надсилаємо підказку від користувача з питанням про погоду у певному місті. 
- LLM відповість викликом інструмента Brave Search, який виглядатиме так `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Примітка: цей приклад лише здійснює виклик інструмента, якщо ви хочете отримати результати, вам потрібно створити безкоштовний акаунт на сторінці Brave API та визначити саму функцію.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Отримайте це зі сторінки "Огляд" вашого проекту Microsoft Foundry
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

Незважаючи на те, що це LLM, однією з обмежень Llama 3.1 є відсутність мультимодальності. Тобто, неможливість використовувати різні типи вхідних даних, такі як зображення, як підказки і надавати відповіді. Ця здатність є однією з основних особливостей Llama 3.2. Ці можливості також включають: 

- Мультимодальність - здатність оцінювати як текстові, так і зображувальні підказки 
- Варіанти малого та середнього розміру (11B та 90B) - це забезпечує гнучкі варіанти розгортання, 
- Варіанти лише з текстом (1B та 3B) - це дозволяє розгортати модель на пристроях на периферії / мобільних пристроях і забезпечує низьку затримку 

Підтримка мультимодальності є значним кроком у світі моделей з відкритим кодом. Приклад коду нижче приймає як зображення, так і текстову підказку, щоб отримати аналіз зображення від Llama 3.2 90B. 


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

# Отримайте це зі сторінки "Огляд" вашого проекту Microsoft Foundry
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

## Навчання не завершується тут, продовжуй подорож

Після проходження цього уроку ознайомтеся з нашою [колекцією навчання Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжувати підвищувати свої знання про Генеративний Штучний Інтелект!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->