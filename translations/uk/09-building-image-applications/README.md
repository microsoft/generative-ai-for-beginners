<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:37:08+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "uk"
}
-->
# Створення додатків для генерації зображень

[![Створення додатків для генерації зображень](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.uk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM — це не лише генерація тексту. Також можливо створювати зображення на основі текстових описів. Використання зображень як модальності може бути дуже корисним у багатьох сферах: від медичних технологій, архітектури, туризму, розробки ігор і не тільки. У цьому розділі ми розглянемо дві найпопулярніші моделі генерації зображень — DALL-E та Midjourney.

## Вступ

У цьому уроці ми розглянемо:

- Генерацію зображень і чому це корисно.
- DALL-E та Midjourney: що це таке і як вони працюють.
- Як створити додаток для генерації зображень.

## Цілі навчання

Після проходження цього уроку ви зможете:

- Створити додаток для генерації зображень.
- Визначати межі вашого додатку за допомогою мета-промптів.
- Працювати з DALL-E та Midjourney.

## Чому варто створювати додаток для генерації зображень?

Додатки для генерації зображень — це чудовий спосіб дослідити можливості генеративного ШІ. Вони можуть бути використані, наприклад, для:

- **Редагування та синтезу зображень**. Ви можете створювати зображення для різних випадків використання, таких як редагування чи синтез зображень.

- **Застосування у різних галузях**. Їх також можна використовувати для створення зображень у різних сферах, таких як медичні технології, туризм, розробка ігор тощо.

## Сценарій: Edu4All

У рамках цього уроку ми продовжимо працювати з нашим стартапом Edu4All. Студенти створюватимуть зображення для своїх завдань. Які саме — вирішують вони самі: це можуть бути ілюстрації до власної казки, створення нового персонажа для історії або допомога у візуалізації ідей та концепцій.

Ось що, наприклад, могли б створити студенти Edu4All, якщо вони працюють у класі над пам’ятками:

![Стартап Edu4All, урок про пам’ятки, Ейфелева вежа](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.uk.png)

використовуючи промпт

> "Собака біля Ейфелевої вежі на ранковому сонці"

## Що таке DALL-E та Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) та [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — дві з найпопулярніших моделей генерації зображень, які дозволяють створювати зображення за допомогою текстових промптів.

### DALL-E

Почнемо з DALL-E — це модель генеративного ШІ, яка створює зображення на основі текстових описів.

> [DALL-E — це поєднання двох моделей, CLIP та diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — модель, яка створює вбудовування (embedding), тобто числові представлення даних, зображень і тексту.

- **Diffused attention** — модель, яка генерує зображення на основі цих вбудовувань. DALL-E навчається на наборі даних із зображень і тексту і може створювати зображення за текстовими описами. Наприклад, DALL-E може створити зображення кота в капелюсі або собаки з ірокезом.

### Midjourney

Midjourney працює схожим чином на DALL-E — генерує зображення за текстовими промптами. Midjourney також можна використовувати для створення зображень за промптами на кшталт «кіт у капелюсі» або «собака з ірокезом».

![Зображення, створене Midjourney, механічний голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Джерело зображення: Wikipedia, створено Midjourney_

## Як працюють DALL-E та Midjourney

Спершу про [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — це модель генеративного ШІ на основі архітектури трансформера з _авторегресивним трансформером_.

_Авторегресивний трансформер_ визначає, як модель створює зображення з текстових описів: вона генерує по одному пікселю за раз, використовуючи вже створені пікселі для генерації наступного. Проходить через кілька шарів нейронної мережі, доки зображення не буде завершене.

Завдяки цьому процесу DALL-E контролює атрибути, об’єкти, характеристики та інші деталі зображення, яке створює. Однак DALL-E 2 і 3 мають ще більший контроль над створеним зображенням.

## Створення вашого першого додатку для генерації зображень

Що потрібно, щоб створити додаток для генерації зображень? Вам знадобляться такі бібліотеки:

- **python-dotenv** — рекомендується використовувати цю бібліотеку, щоб зберігати секрети у файлі _.env_ окремо від коду.
- **openai** — ця бібліотека потрібна для взаємодії з OpenAI API.
- **pillow** — для роботи з зображеннями у Python.
- **requests** — для виконання HTTP-запитів.

1. Створіть файл _.env_ з таким вмістом:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Цю інформацію можна знайти в Azure Portal у розділі "Keys and Endpoint" для вашого ресурсу.

1. Зберіть перелічені бібліотеки у файл _requirements.txt_ так:

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

   Для Windows використайте такі команди для створення та активації віртуального середовища:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Додайте наступний код у файл _app.py_:

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

- Спершу імпортуємо потрібні бібліотеки: OpenAI, dotenv, requests та Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Потім завантажуємо змінні середовища з файлу _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Далі встановлюємо endpoint, ключ для OpenAI API, версію та тип.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Потім генеруємо зображення:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Цей код повертає JSON-об’єкт із URL створеного зображення. Ми можемо використати цей URL, щоб завантажити зображення та зберегти його у файл.

- Нарешті, відкриваємо зображення та показуємо його у стандартному переглядачі зображень:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детальніше про генерацію зображення

Розглянемо код, який генерує зображення, детальніше:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** — текстовий промпт, який використовується для генерації зображення. У цьому випадку це "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси".
- **size** — розмір створеного зображення. Тут генерується зображення розміром 1024x1024 пікселів.
- **n** — кількість створених зображень. Тут створюються два зображення.
- **temperature** — параметр, що контролює випадковість результату генеративної моделі. Температура — це значення від 0 до 1, де 0 означає детермінований (передбачуваний) результат, а 1 — максимально випадковий. За замовчуванням — 0.7.

Існує ще багато можливостей роботи із зображеннями, які ми розглянемо у наступному розділі.

## Додаткові можливості генерації зображень

Ви вже бачили, як можна створити зображення за кілька рядків коду на Python. Але з зображеннями можна робити ще більше.

Ви також можете:

- **Редагувати зображення**. Надсилаючи існуюче зображення, маску та промпт, можна змінювати зображення. Наприклад, додати щось до певної частини зображення. Уявімо наше зображення з кроликом — можна додати йому капелюх. Для цього потрібно надати зображення, маску (яка визначає область для зміни) та текстовий промпт, що описує, що потрібно зробити.

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

  Початкове зображення містить лише кролика, а фінальне — кролика з капелюхом.

- **Створювати варіації**. Ідея полягає в тому, щоб взяти існуюче зображення і попросити створити його варіації. Для цього надають зображення, текстовий промпт і код, наприклад:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Примітка: ця функція підтримується лише в OpenAI.

## Температура

Температура — це параметр, що контролює випадковість результату генеративної моделі. Значення від 0 до 1, де 0 означає детермінований результат, а 1 — випадковий. За замовчуванням — 0.7.

Розглянемо приклад роботи температури, запустивши цей промпт двічі:

> Промпт: "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси"

![Кролик на коні з льодяником, версія 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.uk.png)

Тепер запустимо той самий промпт ще раз, щоб побачити, що зображення не будуть однаковими:

![Згенероване зображення кролика на коні](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.uk.png)

Як бачите, зображення схожі, але не однакові. Спробуємо змінити значення temperature на 0.1 і подивимось, що станеться:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Зміна температури

Спробуємо зробити відповідь більш детермінованою. З двох згенерованих зображень видно, що на першому — кролик, а на другому — кінь, тобто зображення суттєво відрізняються.

Тож змінимо код і встановимо temperature в 0, ось так:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Тепер, коли ви запустите цей код, отримаєте такі два зображення:

- ![Температура 0, версія 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.uk.png)
- ![Температура 0, версія 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.uk.png)

Тут чітко видно, що зображення стали більш схожими.

## Як визначити межі для вашого додатку за допомогою мета-промптів

У нашому демо ми вже можемо генерувати зображення для клієнтів. Проте нам потрібно встановити певні межі для додатку.

Наприклад, ми не хочемо створювати зображення, які не підходять для роботи (NSFW) або неприйнятні для дітей.

Цього можна досягти за допомогою _мета-промптів_. Мета-промпти — це текстові промпти, які використовуються для контролю результату генеративної моделі. Наприклад, ми можемо використовувати мета-промпти, щоб гарантувати, що створені зображення будуть безпечними для роботи або підходящими для дітей.

### Як це працює?

Як працюють мета-промпти?

Мета-промпти — це текстові промпти, які розміщуються перед основним текстовим промптом і використовуються для контролю результату моделі. Вони вбудовуються в додатки для контролю виходу моделі, об’єднуючи вхідний промпт і мета-промпт в один текстовий запит.

Ось приклад мета-промпта:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Тепер подивимось, як ми можемо використовувати мета-промпти у нашому демо.

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

З наведеного промпта видно, що всі створені зображення враховують мета-промпт.

## Завдання — давайте допоможемо студентам

Ми познайомилися зі стартапом Edu4All на початку уроку. Тепер настав час дати студентам можливість створювати зображення для своїх завдань.

Студенти створюватимуть зображення з пам’ятками, які вони оберуть самі. Їх просять проявити креативність і розмістити ці пам’ятки в різних контекстах.

## Розв’язок

Ось один із можливих варіантів розв’язку:

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

prompt = f"""{meta_prompt}
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

## Чудова робота! Продовжуйте навчання

Після проходження цього уроку ознайомтеся з нашою [колекцією навчальних матеріалів з генеративного ШІ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання!

Перейдіть до уроку 10, де ми розглянемо, як [створювати AI-додатки з мінімальним кодуванням](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.