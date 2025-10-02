<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T20:12:02+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "uk"
}
-->
# Створення застосунків для генерації зображень

[![Створення застосунків для генерації зображень](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.uk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Можливості LLM не обмежуються лише генерацією тексту. Також можна створювати зображення на основі текстових описів. Використання зображень як окремої модальності може бути дуже корисним у багатьох сферах: від медичних технологій, архітектури, туризму, розробки ігор тощо. У цьому розділі ми розглянемо дві найпопулярніші моделі для генерації зображень — DALL-E та Midjourney.

## Вступ

У цьому уроці ми розглянемо:

- Генерацію зображень і чому це корисно.
- DALL-E та Midjourney: що це таке і як вони працюють.
- Як створити власний застосунок для генерації зображень.

## Навчальні цілі

Після завершення цього уроку ви зможете:

- Створити застосунок для генерації зображень.
- Визначати межі для вашого застосунку за допомогою метапромптів.
- Працювати з DALL-E та Midjourney.

## Навіщо створювати застосунок для генерації зображень?

Застосунки для генерації зображень — чудовий спосіб дослідити можливості генеративного ШІ. Вони можуть використовуватись, наприклад, для:

- **Редагування та синтезу зображень**. Можна створювати зображення для різних задач, наприклад, для редагування чи синтезу зображень.

- **Використання у різних галузях**. Також їх можна застосовувати для створення зображень у таких сферах, як медичні технології, туризм, розробка ігор тощо.

## Сценарій: Edu4All

У цьому уроці ми продовжимо працювати з нашим стартапом Edu4All. Учні створюватимуть зображення для своїх завдань — які саме зображення, вирішують самі учні: це можуть бути ілюстрації до власної казки, створення нового персонажа для історії або візуалізація своїх ідей та концепцій.

Ось приклад того, що можуть створити учні Edu4All, якщо вони працюють на уроці над пам’ятками:

![Стартап Edu4All, урок про пам’ятки, Ейфелева вежа](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.uk.png)

використовуючи такий промпт:

> "Собака біля Ейфелевої вежі на ранковому сонці"

## Що таке DALL-E та Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) та [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — це дві найпопулярніші моделі для генерації зображень, які дозволяють створювати зображення за допомогою текстових підказок.

### DALL-E

Почнемо з DALL-E — це генеративна модель ШІ, яка створює зображення на основі текстових описів.

> [DALL-E — це поєднання двох моделей: CLIP та дифузної уваги](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — це модель, яка створює ембедінги (числові представлення даних) для зображень і тексту.

- **Дифузна увага** — це модель, яка генерує зображення на основі ембедінгів. DALL-E навчається на великій кількості зображень і текстів, і може створювати зображення за текстовими описами. Наприклад, DALL-E може створити зображення кота в капелюсі або собаки з ірокезом.

### Midjourney

Midjourney працює схожим чином до DALL-E: генерує зображення за текстовими підказками. Midjourney також можна використовувати для створення зображень за промптами на кшталт “кіт у капелюсі” або “собака з ірокезом”.

![Зображення, згенероване Midjourney, механічний голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Джерело: Wikipedia, зображення згенероване Midjourney_

## Як працюють DALL-E та Midjourney

Почнемо з [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — це генеративна модель ШІ, побудована на архітектурі трансформерів з _авторегресивним трансформером_.

_Авторегресивний трансформер_ визначає, як модель створює зображення з текстових описів: генерує по одному пікселю за раз, використовуючи вже створені пікселі для наступних, проходячи через кілька шарів нейромережі, поки зображення не буде завершене.

Завдяки цьому процесу DALL-E може контролювати атрибути, об’єкти, характеристики та інше на створюваному зображенні. Проте DALL-E 2 та 3 дають ще більше контролю над результатом.

## Створення першого застосунку для генерації зображень

Що потрібно для створення застосунку для генерації зображень? Вам знадобляться такі бібліотеки:

- **python-dotenv** — дуже рекомендується використовувати цю бібліотеку, щоб зберігати секрети у файлі _.env_ окремо від коду.
- **openai** — ця бібліотека потрібна для взаємодії з OpenAI API.
- **pillow** — для роботи із зображеннями у Python.
- **requests** — для виконання HTTP-запитів.

## Створення та розгортання моделі Azure OpenAI

Якщо ви ще цього не зробили, дотримуйтесь інструкцій на сторінці [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
щоб створити ресурс і модель Azure OpenAI. Виберіть модель DALL-E 3.  

## Створення застосунку

1. Створіть файл _.env_ з таким вмістом:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Знайдіть цю інформацію у порталі Azure OpenAI Foundry для вашого ресурсу в розділі "Deployments".

1. Зберіть вищезгадані бібліотеки у файл _requirements.txt_ ось так:

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

   Для Windows використовуйте такі команди для створення та активації віртуального середовища:

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

Пояснення коду:

- Спочатку імпортуємо потрібні бібліотеки, зокрема OpenAI, dotenv, requests та Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Далі завантажуємо змінні середовища з файлу _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Після цього налаштовуємо клієнт Azure OpenAI service

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Далі генеруємо зображення:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Вищенаведений код повертає JSON-об’єкт, який містить URL згенерованого зображення. Ми можемо використати цей URL, щоб завантажити зображення та зберегти його у файл.

- Нарешті, відкриваємо зображення та використовуємо стандартний переглядач для його відображення:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детальніше про генерацію зображення

Давайте детальніше розглянемо код, який генерує зображення:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** — це текстова підказка, яка використовується для створення зображення. У цьому випадку ми використовуємо промпт "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси".
- **size** — розмір згенерованого зображення. У цьому випадку створюється зображення 1024x1024 пікселів.
- **n** — кількість згенерованих зображень. Тут створюється два зображення.
- **temperature** — параметр, який визначає ступінь випадковості результату генеративної моделі ШІ. Значення temperature — від 0 до 1, де 0 означає детермінований результат, а 1 — випадковий. Значення за замовчуванням — 0.7.

Є ще багато можливостей роботи із зображеннями, які ми розглянемо далі.

## Додаткові можливості генерації зображень

Ви вже побачили, як можна згенерувати зображення за допомогою кількох рядків коду на Python. Але є ще більше можливостей.

Також можна:

- **Редагувати зображення**. Якщо надати існуюче зображення, маску та промпт, можна змінити зображення. Наприклад, можна додати щось до певної частини зображення. Уявіть наше зображення з кроликом — можна додати кролику капелюх. Для цього потрібно надати зображення, маску (яка визначає область для змін) і текстовий промпт, що саме потрібно зробити.
> Зверніть увагу: ця функція не підтримується у DALL-E 3.

Ось приклад з GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Базове зображення міститиме лише лаунж із басейном, а фінальне — ще й фламінго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Створювати варіації**. Ідея полягає в тому, щоб взяти існуюче зображення і створити його варіації. Для цього потрібно надати зображення, текстовий промпт і код, наприклад:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Зверніть увагу: це підтримується лише в OpenAI

## Temperature

Temperature — це параметр, який визначає ступінь випадковості результату генеративної моделі ШІ. Значення temperature — від 0 до 1, де 0 означає детермінований результат, а 1 — випадковий. Значення за замовчуванням — 0.7.

Давайте подивимось на приклад, як працює temperature, запустивши цей промпт двічі:

> Промпт: "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси"

![Кролик на коні з льодяником, версія 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.uk.png)

Тепер запустимо той самий промпт ще раз, щоб побачити, що зображення не повторюються:

![Згенероване зображення кролика на коні](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.uk.png)

Як бачите, зображення схожі, але не ідентичні. Спробуємо змінити значення temperature на 0.1 і подивимось, що вийде:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Зміна temperature

Спробуємо зробити результат більш детермінованим. Ми помітили, що на першому зображенні є кролик, а на другому — кінь, тобто зображення досить різні.

Тому змінимо код і встановимо temperature на 0, ось так:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Тепер, коли ви запустите цей код, отримаєте такі два зображення:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.uk.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.uk.png)

Тут чітко видно, що зображення стали більш схожими між собою.

## Як визначати межі для вашого застосунку за допомогою метапромптів

З нашим демо ми вже можемо генерувати зображення для клієнтів. Але потрібно встановити певні межі для застосунку.

Наприклад, ми не хочемо генерувати зображення, які не підходять для роботи чи для дітей.

Це можна зробити за допомогою _метапромптів_. Метапромпти — це текстові підказки, які використовуються для контролю результату генеративної моделі ШІ. Наприклад, можна використати метапромпти, щоб переконатися, що згенеровані зображення підходять для роботи чи для дітей.

### Як це працює?

Як працюють метапромпти?

Метапромпти — це текстові підказки, які використовуються для контролю результату генеративної моделі ШІ. Вони розміщуються перед основним промптом і вбудовуються у застосунок для контролю результату моделі. Тобто, промпт користувача та метапромпт об’єднуються в один текстовий запит.

Ось приклад метапромпта:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Тепер подивимось, як можна використати метапромпти у нашому демо.

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

З цього промпта видно, що всі створювані зображення враховують метапромпт.

## Завдання — давайте допоможемо учням

На початку уроку ми познайомилися з Edu4All. Тепер настав час дати учням можливість створювати зображення для своїх завдань.

Учні створюватимуть зображення для своїх завдань, пов’язаних із пам’ятками. Які саме пам’ятки — вирішують самі учні. Їм пропонується проявити креативність і розмістити ці пам’ятки у різних контекстах.

## Рішення

Ось один із можливих варіантів рішення:

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
Після завершення цього уроку перегляньте нашу [колекцію навчальних матеріалів з генеративного ШІ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити поглиблювати свої знання про генеративний ШІ!

Переходьте до уроку 10, де ми розглянемо, як [створювати AI-додатки з використанням low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для отримання критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.