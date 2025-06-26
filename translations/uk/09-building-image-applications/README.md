<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:41:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "uk"
}
-->
# Створення додатків для генерації зображень

Є більше можливостей у LLM, ніж просто генерація тексту. Також можливо створювати зображення з текстових описів. Зображення як модальність можуть бути надзвичайно корисними в багатьох сферах, таких як медичні технології, архітектура, туризм, розробка ігор тощо. У цьому розділі ми розглянемо дві найпопулярніші моделі генерації зображень, DALL-E і Midjourney.

## Вступ

У цьому уроці ми розглянемо:

- Генерацію зображень та чому вона корисна.
- DALL-E і Midjourney, що це таке і як вони працюють.
- Як створити додаток для генерації зображень.

## Навчальні цілі

Після завершення цього уроку ви зможете:

- Створити додаток для генерації зображень.
- Визначити межі для вашого додатку за допомогою мета-підказок.
- Працювати з DALL-E і Midjourney.

## Чому варто створити додаток для генерації зображень?

Додатки для генерації зображень - це чудовий спосіб дослідити можливості генеративного ШІ. Вони можуть бути використані, наприклад, для:

- **Редагування та синтезу зображень**. Ви можете створювати зображення для різноманітних випадків використання, таких як редагування зображень та синтез зображень.

- **Застосування в різних галузях**. Вони також можуть бути використані для створення зображень для різних галузей, таких як медичні технології, туризм, розробка ігор тощо.

## Сценарій: Edu4All

У рамках цього уроку ми продовжимо працювати з нашим стартапом, Edu4All. Студенти створюватимуть зображення для своїх оцінок, саме які зображення — це вирішувати студентам, але це можуть бути ілюстрації для їхньої власної казки або створення нового персонажа для їхньої історії, або допомога у візуалізації їхніх ідей та концепцій.

Ось що студенти Edu4All могли б створити, наприклад, якщо вони працюють у класі над пам'ятками:

![Стартап Edu4All, клас на тему пам'яток, Ейфелева вежа](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.uk.png)

використовуючи підказку на зразок

> "Собака поруч з Ейфелевою вежею на ранковому сонці"

## Що таке DALL-E і Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) і [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — це дві з найпопулярніших моделей генерації зображень, які дозволяють використовувати підказки для створення зображень.

### DALL-E

Почнемо з DALL-E, який є генеративною моделлю ШІ, що створює зображення з текстових описів.

> [DALL-E — це комбінація двох моделей, CLIP і дифузійної уваги](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — це модель, яка генерує вбудовування, які є числовими представленнями даних, з зображень і тексту.

- **Дифузійна увага** — це модель, яка генерує зображення з вбудовувань. DALL-E навчений на наборі даних зображень і тексту і може використовуватися для генерації зображень з текстових описів. Наприклад, DALL-E може бути використаний для створення зображень кота в капелюсі або собаки з ірокезом.

### Midjourney

Midjourney працює подібно до DALL-E, він генерує зображення з текстових підказок. Midjourney також може бути використаний для створення зображень за допомогою підказок на кшталт "кіт у капелюсі" або "собака з ірокезом".

![Зображення, згенероване Midjourney, механічний голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Кредити зображення Wikipedia, зображення, згенероване Midjourney_

## Як працюють DALL-E і Midjourney

Спочатку [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — це генеративна модель ШІ, заснована на архітектурі трансформера з _авторегресивним трансформером_.

_Авторегресивний трансформер_ визначає, як модель генерує зображення з текстових описів, генерує один піксель за раз, а потім використовує згенеровані пікселі для створення наступного пікселя. Проходячи через кілька шарів у нейронній мережі, поки зображення не буде завершено.

Завдяки цьому процесу DALL-E контролює атрибути, об'єкти, характеристики та інше в зображенні, яке він генерує. Однак DALL-E 2 і 3 мають більше контролю над згенерованим зображенням.

## Створення вашого першого додатку для генерації зображень

Отже, що потрібно для створення додатку для генерації зображень? Вам потрібні наступні бібліотеки:

- **python-dotenv**, настійно рекомендується використовувати цю бібліотеку для зберігання ваших секретів у файлі _.env_ подалі від коду.
- **openai**, ця бібліотека використовується для взаємодії з OpenAI API.
- **pillow**, для роботи з зображеннями в Python.
- **requests**, для допомоги у виконанні HTTP-запитів.

1. Створіть файл _.env_ з наступним вмістом:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Знайдіть цю інформацію в Azure Portal для вашого ресурсу в розділі "Ключі та кінцева точка".

1. Зберіть вищезазначені бібліотеки у файлі _requirements.txt_ наступним чином:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Далі створіть віртуальне середовище та встановіть бібліотеки:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Для Windows використовуйте наступні команди для створення та активації вашого віртуального середовища:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Додайте наступний код у файл під назвою _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Пояснимо цей код:

- Спочатку ми імпортуємо необхідні бібліотеки, включаючи бібліотеку OpenAI, бібліотеку dotenv, бібліотеку requests і бібліотеку Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Далі ми завантажуємо змінні середовища з файлу _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Після цього ми встановлюємо кінцеву точку, ключ для OpenAI API, версію та тип.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Далі ми генеруємо зображення:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Вищезазначений код відповідає об'єктом JSON, який містить URL згенерованого зображення. Ми можемо використовувати URL для завантаження зображення та збереження його у файл.

- Нарешті, ми відкриваємо зображення та використовуємо стандартний переглядач зображень для його відображення:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детальніше про генерацію зображення

Давайте розглянемо код, що генерує зображення, більш детально:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** — це текстова підказка, яка використовується для генерації зображення. У цьому випадку ми використовуємо підказку "Кролик на коні, що тримає льодяник, на туманному лузі, де ростуть нарциси".
- **size** — це розмір згенерованого зображення. У цьому випадку ми генеруємо зображення розміром 1024x1024 пікселів.
- **n** — це кількість згенерованих зображень. У цьому випадку ми генеруємо два зображення.
- **temperature** — це параметр, який контролює випадковість виходу генеративної моделі ШІ. Температура — це значення між 0 і 1, де 0 означає, що вихід детермінований, а 1 означає, що вихід випадковий. Значення за замовчуванням — 0,7.

Є ще багато речей, які ви можете зробити із зображеннями, які ми розглянемо в наступному розділі.

## Додаткові можливості генерації зображень

Ви вже бачили, як ми змогли створити зображення за допомогою кількох рядків у Python. Однак, є ще більше речей, які ви можете зробити із зображеннями.

Ви також можете зробити наступне:

- **Виконувати редагування**. Надаючи існуюче зображення, маску та підказку, ви можете змінити зображення. Наприклад, ви можете додати щось до частини зображення. Уявіть наше зображення з кроликом, ви можете додати капелюх до кролика. Як це зробити, це надати зображення, маску (визначаючи частину області для зміни) та текстову підказку, щоб сказати, що має бути зроблено.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Базове зображення міститиме лише кролика, але кінцеве зображення матиме капелюх на кролику.

- **Створювати варіації**. Ідея полягає в тому, щоб взяти існуюче зображення і попросити створити варіації. Щоб створити варіацію, ви надаєте зображення та текстову підказку і код, як показано нижче:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Зверніть увагу, це підтримується лише в OpenAI

## Температура

Температура — це параметр, який контролює випадковість виходу генеративної моделі ШІ. Температура — це значення між 0 і 1, де 0 означає, що вихід детермінований, а 1 означає, що вихід випадковий. Значення за замовчуванням — 0,7.

Давайте розглянемо приклад, як працює температура, запустивши цю підказку двічі:

> Підказка: "Кролик на коні, що тримає льодяник, на туманному лузі, де ростуть нарциси"

![Кролик на коні, що тримає льодяник, версія 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.uk.png)

Тепер давайте запустимо цю саму підказку, щоб побачити, що ми не отримаємо одне і те ж зображення двічі:

![Згенероване зображення кролика на коні](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.uk.png)

Як ви бачите, зображення схожі, але не ідентичні. Давайте спробуємо змінити значення температури на 0,1 і подивимося, що станеться:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Зміна температури

Отже, спробуємо зробити відповідь більш детермінованою. Ми могли спостерігати з двох згенерованих зображень, що на першому зображенні є кролик, а на другому зображенні є кінь, тому зображення значно відрізняються.

Тому давайте змінімо наш код і встановимо температуру на 0, як показано нижче:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Тепер, коли ви запустите цей код, ви отримаєте ці два зображення:

- ![Температура 0, версія 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.uk.png)
- ![Температура 0, версія 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.uk.png)

Тут ви можете чітко бачити, як зображення більше схожі одне на одне.

## Як визначити межі для вашого додатку за допомогою мета-підказок

З нашим демо ми вже можемо генерувати зображення для наших клієнтів. Однак нам потрібно створити деякі межі для нашого додатку.

Наприклад, ми не хочемо генерувати зображення, які не є безпечними для роботи, або які не є відповідними для дітей.

Ми можемо зробити це за допомогою _мета-підказок_. Мета-підказки — це текстові підказки, які використовуються для контролю виходу генеративної моделі ШІ. Наприклад, ми можемо використовувати мета-підказки для контролю виходу і забезпечення того, щоб згенеровані зображення були безпечними для роботи або відповідними для дітей.

### Як це працює?

Тепер, як працюють мета-підказки?

Мета-підказки — це текстові підказки, які використовуються для контролю виходу генеративної моделі ШІ, вони розміщені перед текстовою підказкою і використовуються для контролю виходу моделі та вбудовані в додатки для контролю виходу моделі. Інкапсулюючи вхід підказки та вхід мета-підказки в одну текстову підказку.

Один приклад мета-підказки може бути наступним:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Тепер давайте подивимося, як ми можемо використовувати мета-підказки в нашому демо.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

З вищезазначеної підказки ви можете бачити, як усі створювані зображення враховують мета-підказку.

## Завдання - давайте підтримаємо студентів

Ми представили Edu4All на початку цього уроку. Тепер настав час підтримати студентів у створенні зображень для їхніх оцінок.

Студенти створюватимуть зображення для своїх оцінок, що містять пам'ятки, саме які пам'ятки — це вирішувати студентам. Студентів просять використовувати свою креативність у цьому завданні, щоб розмістити ці пам'ятки в різних контекстах.

## Рішення

Ось одне з можливих рішень:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Чудова робота! Продовжуйте своє навчання

Після завершення цього уроку ознайомтеся з нашою [колекцією навчання з генеративного ШІ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання з генеративного ШІ!

Перейдіть до Уроку 10, де ми розглянемо, як [створювати додатки ШІ з низьким кодом](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Ми прагнемо до точності, але зверніть увагу, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ на рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.