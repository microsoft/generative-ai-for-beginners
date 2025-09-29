<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T22:00:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "uk"
}
-->
# Створення додатків для генерації зображень

[![Створення додатків для генерації зображень](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.uk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Генеративні мовні моделі (LLM) можуть робити більше, ніж просто генерувати текст. Вони також здатні створювати зображення на основі текстових описів. Можливість працювати із зображеннями може бути надзвичайно корисною в багатьох сферах, таких як медична технологія, архітектура, туризм, розробка ігор тощо. У цьому розділі ми розглянемо дві найпопулярніші моделі генерації зображень: DALL-E та Midjourney.

## Вступ

У цьому уроці ми розглянемо:

- Генерацію зображень та її корисність.
- DALL-E та Midjourney: що це таке і як вони працюють.
- Як створити додаток для генерації зображень.

## Цілі навчання

Після завершення цього уроку ви зможете:

- Створити додаток для генерації зображень.
- Визначити межі для вашого додатка за допомогою метапідказок.
- Працювати з DALL-E та Midjourney.

## Чому варто створювати додаток для генерації зображень?

Додатки для генерації зображень — це чудовий спосіб дослідити можливості генеративного штучного інтелекту. Вони можуть бути використані, наприклад, для:

- **Редагування та синтезу зображень**. Ви можете створювати зображення для різних цілей, таких як редагування та синтез зображень.

- **Застосування в різних галузях**. Вони також можуть бути використані для створення зображень у таких галузях, як медична технологія, туризм, розробка ігор тощо.

## Сценарій: Edu4All

У рамках цього уроку ми продовжимо працювати з нашим стартапом Edu4All. Студенти створюватимуть зображення для своїх завдань. Які саме зображення — залежить від студентів, але це можуть бути ілюстрації до їхньої казки, створення нового персонажа для їхньої історії або допомога у візуалізації їхніх ідей та концепцій.

Ось що, наприклад, можуть створити студенти Edu4All, якщо вони працюють у класі над темою пам'ятників:

![Стартап Edu4All, клас про пам'ятники, Ейфелева вежа](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.uk.png)

використовуючи підказку, наприклад:

> "Собака біля Ейфелевої вежі на ранковому сонці"

## Що таке DALL-E та Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) та [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — це дві найпопулярніші моделі генерації зображень, які дозволяють використовувати текстові підказки для створення зображень.

### DALL-E

Почнемо з DALL-E — генеративної моделі штучного інтелекту, яка створює зображення на основі текстових описів.

> [DALL-E — це комбінація двох моделей: CLIP та розсіяної уваги](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — це модель, яка створює векторні представлення даних (ембеддинги) з зображень та тексту.

- **Розсіяна увага** — це модель, яка створює зображення з ембеддингів. DALL-E навчена на наборі даних із зображень та тексту і може використовуватися для створення зображень на основі текстових описів. Наприклад, DALL-E може створити зображення кота в капелюсі або собаки з ірокезом.

### Midjourney

Midjourney працює схожим чином до DALL-E, генеруючи зображення на основі текстових підказок. Midjourney також може використовуватися для створення зображень за підказками, такими як "кіт у капелюсі" або "собака з ірокезом".

![Зображення, створене Midjourney, механічний голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Автор зображення: Wikipedia, зображення створене Midjourney_

## Як працюють DALL-E та Midjourney

Спочатку [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — це генеративна модель штучного інтелекту, заснована на архітектурі трансформера з _авторегресивним трансформером_.

_Авторегресивний трансформер_ визначає, як модель створює зображення з текстових описів: вона генерує один піксель за раз, а потім використовує створені пікселі для генерації наступного пікселя. Процес проходить через кілька шарів нейронної мережі, поки зображення не буде завершене.

Завдяки цьому процесу DALL-E контролює атрибути, об'єкти, характеристики та інші елементи зображення, яке вона створює. Однак DALL-E 2 та 3 мають більше можливостей для контролю над створеним зображенням.

## Створення вашого першого додатка для генерації зображень

Що потрібно для створення додатка для генерації зображень? Вам знадобляться наступні бібліотеки:

- **python-dotenv** — настійно рекомендується використовувати цю бібліотеку для зберігання секретів у файлі _.env_ окремо від коду.
- **openai** — ця бібліотека використовується для взаємодії з API OpenAI.
- **pillow** — для роботи із зображеннями в Python.
- **requests** — для виконання HTTP-запитів.

## Створення та розгортання моделі Azure OpenAI

Якщо це ще не зроблено, дотримуйтесь інструкцій на сторінці [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), щоб створити ресурс та модель Azure OpenAI. Виберіть DALL-E 3 як модель.

## Створення додатка

1. Створіть файл _.env_ із наступним вмістом:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Знайдіть цю інформацію в порталі Azure OpenAI Foundry для вашого ресурсу в розділі "Deployments".

1. Зберіть зазначені бібліотеки у файлі _requirements.txt_ таким чином:

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

   Для Windows використовуйте наступні команди для створення та активації віртуального середовища:

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Спочатку ми імпортуємо необхідні бібліотеки, включаючи бібліотеку OpenAI, бібліотеку dotenv, бібліотеку requests та бібліотеку Pillow.

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

- Після цього ми налаштовуємо клієнт сервісу Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Потім ми генеруємо зображення:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Наведений код відповідає JSON-об'єктом, який містить URL створеного зображення. Ми можемо використовувати URL для завантаження зображення та збереження його у файл.

- Нарешті, ми відкриваємо зображення та використовуємо стандартний переглядач зображень для його відображення:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детальніше про генерацію зображення

Розглянемо код, який генерує зображення, детальніше:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** — текстова підказка, яка використовується для створення зображення. У цьому випадку ми використовуємо підказку "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси".
- **size** — розмір створеного зображення. У цьому випадку ми створюємо зображення розміром 1024x1024 пікселів.
- **n** — кількість створених зображень. У цьому випадку ми створюємо два зображення.
- **temperature** — параметр, який контролює випадковість результату генеративної моделі штучного інтелекту. Температура — це значення між 0 і 1, де 0 означає, що результат детермінований, а 1 — що результат випадковий. Значення за замовчуванням — 0.7.

Є ще багато можливостей роботи із зображеннями, які ми розглянемо у наступному розділі.

## Додаткові можливості генерації зображень

Ви вже бачили, як ми змогли створити зображення за допомогою кількох рядків коду на Python. Однак є ще багато можливостей роботи із зображеннями.

Ви також можете:

- **Редагувати зображення**. Надати існуюче зображення, маску та підказку, щоб змінити зображення. Наприклад, ви можете додати щось до певної частини зображення. Уявіть наше зображення з кроликом — ви можете додати капелюх кролику. Для цього потрібно надати зображення, маску (визначення області для зміни) та текстову підказку, яка описує, що потрібно зробити.
> Примітка: це не підтримується в DALL-E 3.

Ось приклад використання GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Базове зображення міститиме лише лаунж із басейном, але фінальне зображення матиме фламінго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.uk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.uk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.uk.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Створювати варіації**. Ідея полягає в тому, щоб взяти існуюче зображення та попросити створити його варіації. Для створення варіації потрібно надати зображення та текстову підказку, а також код, як показано нижче:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Примітка: це підтримується лише в OpenAI.

## Температура

Температура — це параметр, який контролює випадковість результату генеративної моделі штучного інтелекту. Температура — це значення між 0 і 1, де 0 означає, що результат детермінований, а 1 — що результат випадковий. Значення за замовчуванням — 0.7.

Розглянемо приклад, як працює температура, запустивши цей запит двічі:

> Підказка: "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси"

![Кролик на коні, тримає льодяник, версія 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.uk.png)

Тепер запустимо той самий запит ще раз, щоб побачити, що ми не отримаємо те саме зображення двічі:

![Створене зображення кролика на коні](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.uk.png)

Як ви бачите, зображення схожі, але не однакові. Спробуємо змінити значення температури на 0.1 і подивимося, що станеться:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Зміна температури

Спробуємо зробити результат більш детермінованим. Ми могли спостерігати, що в першому зображенні є кролик, а в другому — кінь, тому зображення значно відрізняються.

Тому змінімо наш код і встановимо температуру на 0, як показано нижче:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Тепер, коли ви запустите цей код, ви отримаєте ці два зображення:

- ![Температура 0, версія 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.uk.png)
- ![Температура 0, версія 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.uk.png)

Тут ви чітко бачите, як зображення більше схожі одне на одного.

## Як визначити межі для вашого додатка за допомогою метапідказок

З нашим демо ми вже можемо створювати зображення для наших клієнтів. Однак нам потрібно створити деякі межі для нашого додатка.

Наприклад, ми не хочемо створювати зображення, які не є безпечними для роботи або не підходять для дітей.

Ми можемо зробити це за допомогою _метапідказок_. Метапідказки — це текстові підказки, які використовуються для контролю результату генеративної моделі штучного інтелекту. Наприклад, ми можемо використовувати метапідказки для контролю результату та забезпечення того, щоб створені зображення були безпечними для роботи або підходили для дітей.

### Як це працює?

Як працюють метапідказки?

Метапідказки — це текстові підказки, які використовуються для контролю результату генеративної моделі штучного інтелекту. Вони розташовуються перед текстовою підказкою і використовуються для контролю результату моделі, вбудовуючись у додатки для контролю результату моделі. Вони об'єднують введення підказки та введення метапідказки в одну текстову підказку.

Один приклад метапідказки може виглядати так:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Тепер подивимося, як ми можемо використовувати метапідказки в нашому демо.

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

З наведеної підказки видно, як усі створені зображення враховують метапідказку.

## Завдання — допоможемо студентам

Ми представили Edu4All на початку цього уроку. Тепер настав час допомогти студентам створювати зображення для їхніх завдань.

Студенти створюватимуть зображення для своїх завдань, що містять пам'ятники. Які саме пам'ятники — залежить від студентів. Студентам пропонується використати свою творчість у цьому завданні, щоб розмістити ці пам'ятники в різних контекстах.

## Рішення

Ось одне з можливих рішень:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Чудова робота! Продовжуйте навчання

Після завершення цього уроку перегляньте нашу [колекцію навчальних матеріалів з генеративного штучного інтелекту](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити вдосконалювати свої знання про генеративний штучний інтелект!

Перейдіть до уроку 10, де ми розглянемо, як [створювати AI-додатки за допомогою low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.