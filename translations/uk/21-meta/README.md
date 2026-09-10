# Робота з моделями родини Meta 

## Вступ 

В цьому уроці буде розглянуто: 

- Дослідження двох основних моделей родини Meta - Llama 3.1 та Llama 3.2 
- Розуміння випадків використання та сценаріїв для кожної моделі 
- Приклад коду, що демонструє унікальні особливості кожної моделі 


## Родина моделей Meta 

У цьому уроці ми розглянемо 2 моделі з родини Meta або "стада Ллами" - Llama 3.1 та Llama 3.2.

Ці моделі доступні у різних варіантах у [каталозі моделей Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Примітка:** GitHub Models припинить роботу в кінці липня 2026 року. Детальніше про використання [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) для прототипування з AI моделями.

Варіанти моделей: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Примітка: Llama 3 також доступна в Microsoft Foundry Models, але не буде розглядатися в цьому уроці*

## Llama 3.1 

Модель Llama 3.1 з 405 мільярдами параметрів належить до категорії відкритих LLM. 

Ця модель є оновленням до попередньої версії Llama 3, і пропонує: 

- Більше контекстне вікно - 128k токенів проти 8k токенів 
- Більше максимальної кількості токенів на виході - 4096 проти 2048 
- Кращу підтримку мультимовності - завдяки збільшенню кількості тренувальних токенів 

Це дозволяє Llama 3.1 справлятися з більш складними випадками, коли створюються GenAI додатки, включно з: 
- Нативним викликом функцій - можливістю викликати зовнішні інструменти і функції поза робочим процесом LLM
- Кращою продуктивністю RAG - завдяки більшому контекстному вікну 
- Генерацією синтетичних даних - можливістю створювати ефективні дані для таких завдань, як тонке налаштування 

### Нативний виклик функцій 

Llama 3.1 була тонко налаштована для кращої ефективності у виклику функцій чи інструментів. Вона також має два вбудованих інструменти, які модель може визначити як необхідні для використання на основі запиту користувача. Ці інструменти: 

- **Brave Search** - може використовуватися для отримання актуальної інформації, наприклад погоди, через веб-пошук 
- **Wolfram Alpha** - може використовуватися для складніших математичних обчислень, тож немає потреби писати власні функції. 

Ви також можете створювати власні інструменти, які LLM може викликати. 

У прикладі коду нижче: 

- Ми визначаємо доступні інструменти (brave_search, wolfram_alpha) в системному запиті. 
- Надсилаємо запит від користувача з питанням про погоду у певному місті. 
- LLM відповість викликом інструменту Brave Search, що виглядає так: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Примітка: цей приклад лише здійснює виклик інструменту. Якщо ви хочете отримати результати, вам потрібно створити безкоштовний акаунт на сторінці Brave API та визначити саму функцію.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Отримайте їх зі сторінки "Огляд" вашого проекту Microsoft Foundry
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

Незважаючи на те, що Llama 3.1 є LLM, її обмеженням є відсутність мультимодальності. Тобто, неможливість використовувати різні типи вхідних даних, як от зображення у ролі запитів, і надавати відповіді. Ця можливість є однією з основних функцій Llama 3.2. Серед інших особливостей: 

- Мультимодальність - здатність аналізувати як текстові, так і зображувальні запити 
- Варіації малого та середнього розміру (11B та 90B) - це забезпечує гнучкі варіанти розгортання 
- Варіанти тільки з текстом (1B і 3B) - дозволяють запускати модель на пристроях на межі або мобільних і забезпечують низьку затримку 

Підтримка мультимодальності є великим кроком у світі відкритих моделей. Приклад коду нижче приймає як зображення, так і текстовий запит для отримання аналізу зображення від Llama 3.2 90B. 


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

## Навчання на цьому не закінчується, продовжуйте далі

Після завершення цього уроку ознайомтеся з нашою [колекцією з навчання Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищення свого рівня знань у генеративному AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->