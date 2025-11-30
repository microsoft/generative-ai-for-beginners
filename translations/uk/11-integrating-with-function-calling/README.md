<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-18T02:11:59+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "uk"
}
-->
# Інтеграція з викликом функцій

[![Інтеграція з викликом функцій](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.uk.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Ви вже багато чого дізналися з попередніх уроків. Однак ми можемо вдосконалити наші знання ще більше. Деякі аспекти, які варто розглянути, включають отримання більш узгодженого формату відповідей, щоб спростити роботу з ними в подальшому. Також ми можемо додати дані з інших джерел для покращення нашого застосунку.

Цей розділ присвячений вирішенню зазначених проблем.

## Вступ

Цей урок охоплює:

- Пояснення, що таке виклик функцій і його можливі застосування.
- Створення виклику функції за допомогою Azure OpenAI.
- Як інтегрувати виклик функції в застосунок.

## Цілі навчання

Після завершення цього уроку ви зможете:

- Пояснити мету використання виклику функцій.
- Налаштувати виклик функції за допомогою Azure OpenAI Service.
- Розробити ефективні виклики функцій для вашого застосунку.

## Сценарій: Покращення нашого чат-бота за допомогою функцій

У цьому уроці ми хочемо створити функцію для нашого освітнього стартапу, яка дозволить користувачам використовувати чат-бот для пошуку технічних курсів. Ми будемо рекомендувати курси, які відповідають їхньому рівню навичок, поточній ролі та цікавій технології.

Для виконання цього сценарію ми використаємо комбінацію:

- `Azure OpenAI` для створення чат-досвіду для користувача.
- `Microsoft Learn Catalog API` для допомоги користувачам у пошуку курсів на основі їхніх запитів.
- `Function Calling` для обробки запиту користувача та передачі його функції для виконання запиту до API.

Щоб розпочати, давайте розглянемо, чому ми взагалі хочемо використовувати виклик функцій:

## Чому виклик функцій

До появи виклику функцій відповіді від LLM були неструктурованими та непослідовними. Розробникам доводилося писати складний код перевірки, щоб переконатися, що вони можуть обробляти кожну варіацію відповіді. Користувачі не могли отримувати відповіді на запитання, як-от "Яка зараз погода у Стокгольмі?". Це тому, що моделі були обмежені часом, коли дані були навчені.

Виклик функцій — це функція Azure OpenAI Service, яка допомагає подолати наступні обмеження:

- **Узгоджений формат відповіді**. Якщо ми можемо краще контролювати формат відповіді, ми зможемо легше інтегрувати її в інші системи.
- **Зовнішні дані**. Можливість використовувати дані з інших джерел застосунку в контексті чату.

## Ілюстрація проблеми через сценарій

> Ми рекомендуємо вам скористатися [включеним блокнотом](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst), якщо ви хочете виконати наведений нижче сценарій. Ви також можете просто прочитати, оскільки ми намагаємося проілюструвати проблему, яку функції можуть допомогти вирішити.

Розглянемо приклад, який ілюструє проблему формату відповіді:

Припустимо, ми хочемо створити базу даних студентів, щоб рекомендувати їм відповідні курси. Нижче наведено два описи студентів, які дуже схожі за даними, які вони містять.

1. Створіть з'єднання з нашим ресурсом Azure OpenAI:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   Нижче наведено код на Python для налаштування нашого з'єднання з Azure OpenAI, де ми встановлюємо `api_type`, `api_base`, `api_version` та `api_key`.

1. Створення двох описів студентів за допомогою змінних `student_1_description` та `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Ми хочемо надіслати наведені вище описи студентів до LLM для аналізу даних. Ці дані можуть бути використані в нашому застосунку, надіслані до API або збережені в базі даних.

1. Давайте створимо два однакові запити, в яких ми інструктуємо LLM, яку інформацію ми хочемо отримати:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   Наведені вище запити інструктують LLM витягувати інформацію та повертати відповідь у форматі JSON.

1. Після налаштування запитів і з'єднання з Azure OpenAI ми тепер надішлемо запити до LLM, використовуючи `openai.ChatCompletion`. Ми зберігаємо запит у змінній `messages` і призначаємо роль `user`. Це імітує повідомлення від користувача, написане чат-боту.

   ```python
   # response from prompt one
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # response from prompt two
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

Тепер ми можемо надіслати обидва запити до LLM і перевірити отриману відповідь, знайшовши її, наприклад, так: `openai_response1['choices'][0]['message']['content']`.

1. Нарешті, ми можемо конвертувати відповідь у формат JSON, викликавши `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Відповідь 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Відповідь 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Хоча запити однакові, а описи схожі, ми бачимо, що значення властивості `Grades` мають різний формат, наприклад, іноді ми отримуємо формат `3.7`, а іноді `3.7 GPA`.

   Це результат того, що LLM бере неструктуровані дані у вигляді написаного запиту і також повертає неструктуровані дані. Нам потрібно мати структурований формат, щоб знати, чого очікувати при збереженні або використанні цих даних.

Отже, як вирішити проблему форматування? Використовуючи виклик функцій, ми можемо забезпечити отримання структурованих даних. При використанні виклику функцій LLM фактично не викликає і не виконує жодних функцій. Натомість ми створюємо структуру, яку LLM має дотримуватися у своїх відповідях. Потім ми використовуємо ці структуровані відповіді, щоб знати, яку функцію виконати в наших застосунках.

![function flow](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.uk.png)

Потім ми можемо взяти те, що повертається з функції, і надіслати це назад до LLM. LLM потім відповість, використовуючи природну мову, щоб відповісти на запит користувача.

## Сценарії використання викликів функцій

Існує багато різних сценаріїв, де виклики функцій можуть покращити ваш застосунок, наприклад:

- **Виклик зовнішніх інструментів**. Чат-боти чудово відповідають на запитання користувачів. Використовуючи виклик функцій, чат-боти можуть використовувати повідомлення від користувачів для виконання певних завдань. Наприклад, студент може попросити чат-бота: "Надішли електронний лист моєму викладачу, що мені потрібна додаткова допомога з цього предмету". Це може викликати функцію `send_email(to: string, body: string)`.

- **Створення запитів до API або бази даних**. Користувачі можуть знаходити інформацію, використовуючи природну мову, яка перетворюється на форматований запит або запит до API. Наприклад, викладач може запитати: "Хто зі студентів завершив останнє завдання", що може викликати функцію `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Створення структурованих даних**. Користувачі можуть взяти блок тексту або CSV і використовувати LLM для витягування важливої інформації з нього. Наприклад, студент може конвертувати статтю з Вікіпедії про мирні угоди, щоб створити AI-картки для запам'ятовування. Це можна зробити за допомогою функції `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Створення вашого першого виклику функції

Процес створення виклику функції включає три основні кроки:

1. **Виклик** API Chat Completions зі списком ваших функцій і повідомленням користувача.
2. **Читання** відповіді моделі для виконання дії, тобто виконання функції або запиту до API.
3. **Здійснення** ще одного виклику до API Chat Completions з відповіддю від вашої функції, щоб використати цю інформацію для створення відповіді користувачу.

![LLM Flow](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.uk.png)

### Крок 1 - створення повідомлень

Перший крок — створити повідомлення користувача. Це можна динамічно призначити, взявши значення текстового вводу, або призначити значення тут. Якщо ви вперше працюєте з API Chat Completions, нам потрібно визначити `role` і `content` повідомлення.

`role` може бути `system` (створення правил), `assistant` (модель) або `user` (кінцевий користувач). Для виклику функцій ми призначимо це як `user` і наведемо приклад запитання.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Призначаючи різні ролі, стає зрозуміло для LLM, чи це система щось говорить, чи користувач, що допомагає створити історію розмови, на основі якої LLM може працювати.

### Крок 2 - створення функцій

Далі ми визначимо функцію та параметри цієї функції. Ми використаємо лише одну функцію під назвою `search_courses`, але ви можете створити кілька функцій.

> **Важливо**: Функції включаються в системне повідомлення для LLM і враховуються в кількості доступних токенів.

Нижче ми створюємо функції як масив елементів. Кожен елемент є функцією і має властивості `name`, `description` і `parameters`:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Давайте детальніше опишемо кожен екземпляр функції:

- `name` - Назва функції, яку ми хочемо викликати.
- `description` - Опис того, як працює функція. Тут важливо бути конкретним і чітким.
- `parameters` - Список значень і формат, який ми хочемо, щоб модель створила у своїй відповіді. Масив параметрів складається з елементів, де елементи мають наступні властивості:
  1.  `type` - Тип даних, у якому будуть зберігатися властивості.
  1.  `properties` - Список конкретних значень, які модель буде використовувати для своєї відповіді.
      1. `name` - Ключ — це назва властивості, яку модель буде використовувати у своєму форматованому відповіді, наприклад, `product`.
      1. `type` - Тип даних цієї властивості, наприклад, `string`.
      1. `description` - Опис конкретної властивості.

Також є необов'язкова властивість `required` — обов'язкова властивість для завершення виклику функції.

### Крок 3 - Виконання виклику функції

Після визначення функції нам потрібно включити її у виклик до API Chat Completion. Ми робимо це, додаючи `functions` до запиту. У цьому випадку `functions=functions`.

Також є опція встановити `function_call` як `auto`. Це означає, що ми дозволимо LLM вирішувати, яку функцію слід викликати на основі повідомлення користувача, а не призначати її самостійно.

Ось код нижче, де ми викликаємо `ChatCompletion.create`, зверніть увагу, як ми встановлюємо `functions=functions` і `function_call="auto"`, тим самим надаючи LLM можливість вирішувати, коли викликати надані функції:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

Відповідь, що повертається, виглядає так:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Тут ми бачимо, як була викликана функція `search_courses` і з якими аргументами, як зазначено у властивості `arguments` у відповіді JSON.

Висновок: LLM зміг знайти дані, які відповідають аргументам функції, витягуючи їх із значення, наданого параметру `messages` у виклику Chat Completion. Нижче наведено нагадування про значення `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Як бачите, `student`, `Azure` і `beginner` були витягнуті з `messages` і встановлені як вхідні дані для функції. Використання функцій таким чином — це чудовий спосіб витягувати інформацію з запиту, а також надавати структуру LLM і мати функціональність, яку можна повторно використовувати.

Тепер нам потрібно побачити, як ми можемо використовувати це у нашому застосунку.

## Інтеграція викликів функцій у застосунок

Після того, як ми протестували форматовану відповідь від LLM, ми можемо інтегрувати це у застосунок.

### Управління процесом

Щоб інтегрувати це у наш застосунок, виконаємо наступні кроки:

1. Спочатку зробимо виклик до сервісів OpenAI і збережемо повідомлення у змінній під назвою `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Тепер ми визначимо функцію, яка викличе Microsoft Learn API для отримання списку курсів:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   Зверніть увагу, як ми тепер створюємо фактичну функцію Python, яка відповідає назвам функцій, введеним у змінну `functions`. Ми також здійснюємо реальні зовнішні виклики API для отримання необхідних даних. У цьому випадку ми звертаємося до Microsoft Learn API для пошуку навчальних модулів.

Отже, ми створили змінні `functions` і відповідну функцію Python, як ми можемо сказати LLM, як зіставити ці два разом, щоб викликати нашу функцію Python?

1. Щоб перевірити, чи потрібно викликати функцію Python, нам потрібно заглянути у відповідь LLM і перевірити, чи є частина `function_call`, і викликати зазначену функцію. Ось як ви можете зробити зазначену перевірку нижче:

   ```python
   # Check if the model wants to call a function
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # Call the function.
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   Ці три рядки забезпечують витяг назви функції, аргументів і виконання виклику:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Нижче наведено вихідні дані після виконання нашого коду:

   **Вихідні дані**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Тепер ми надішлемо оновлене повідомлення, `messages`, до LLM, щоб отримати відповідь природною мовою замість відповіді у форматі JSON API.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # get a new response from GPT where it can see the function response


   print(second_response.choices[0].message)
   ```

   **Вихідні дані**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Завдання

Щоб продовжити навчання Azure OpenAI Function Calling, ви можете створити:

- Більше параметрів функції, які можуть допомогти учням знайти більше курсів.
- Створити ще один виклик функції, який враховує більше інформації про учня, наприклад, його рідну мову.
- Створіть обробку помилок, якщо виклик функції та/або API не повертає жодних відповідних курсів.

Підказка: Ознайомтеся зі сторінкою [Learn API reference documentation](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst), щоб дізнатися, як і де доступні ці дані.

## Чудова робота! Продовжуйте навчання

Після завершення цього уроку перегляньте нашу [колекцію навчальних матеріалів про генеративний штучний інтелект](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити вдосконалювати свої знання про генеративний штучний інтелект!

Перейдіть до уроку 12, де ми розглянемо, як [розробляти UX для AI-додатків](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.