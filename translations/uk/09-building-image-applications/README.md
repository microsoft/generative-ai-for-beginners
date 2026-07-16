# Створення додатків для генерації зображень

[![Створення додатків для генерації зображень](../../../translated_images/uk/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Лінгвістичні моделі не обмежуються генерацією тексту. Також можна генерувати зображення з текстових описів. Наявність зображень як модальності може бути надзвичайно корисною в багатьох сферах — від медичних технологій, архітектури, туризму, розробки ігор і більше. У цьому розділі ми розглянемо дві найпопулярніші моделі генерації зображень — DALL-E та Midjourney.

## Вступ

У цьому уроці ми розглянемо:

- Генерацію зображень і чому це корисно.
- Моделі DALL-E та Midjourney, що це таке і як вони працюють.
- Як створити додаток для генерації зображень.

## Цілі навчання

Після завершення цього уроку ви зможете:

- Створити додаток для генерації зображень.
- Визначати межі для вашого додатка за допомогою мета-підказок.
- Працювати з DALL-E і Midjourney.

## Чому створювати додаток для генерації зображень?

Додатки для генерації зображень — це чудовий спосіб дослідити можливості генеративного ШІ. Їх можна використовувати, наприклад, для:

- **Редагування та синтез зображень**. Ви можете генерувати зображення для різних випадків використання, наприклад для редагування та синтезу зображень.

- **Застосування у різних галузях**. Їх також можна застосовувати для створення зображень у різних галузях, як-от медтехнології, туризм, розробка ігор та інші.

## Сценарій: Edu4All

У рамках цього уроку ми продовжимо працювати з нашим стартапом Edu4All. Студенти створять зображення для їхніх завдань, які саме — вирішують вони: це можуть бути ілюстрації для власної казки, створення нового персонажа для історії або візуалізація ідей та концепцій.

Ось що студенти Edu4All могли б згенерувати, наприклад, якщо вони працюють у класі над монументами:

![Стартап Edu4All, урок про пам'ятники, Ейфелева вежа](../../../translated_images/uk/startup.94d6b79cc4bb3f5a.webp)

використовуючи підказку

> "Собака біля Ейфелевої вежі на ранковому сонячному світлі"

## Що таке DALL-E і Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) та [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — дві найпопулярніші моделі для генерації зображень, вони дозволяють використовувати підказки для створення зображень.

### DALL-E

Почнемо з DALL-E, яка є генеративною моделлю ШІ, що генерує зображення з текстових описів.

> [DALL-E — це комбінація двох моделей, CLIP і дифузної уваги](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — це модель, яка генерує ембеддинги, числові представлення даних, зображень та тексту.

- **Дифузна увага** — це модель, яка генерує зображення з ембеддингів. DALL-E навчена на наборі даних зображень і тексту та може створювати зображення з текстових описів. Наприклад, DALL-E може згенерувати зображення кота в капелюсі чи собаки з ірокезом.

### Midjourney

Midjourney працює схожим чином, генерує зображення з текстових підказок. Midjourney також можна використовувати для генерації зображень за підказками, як-от «кіт у капелюсі» чи «собака з ірокезом».

![Зображення, створене Midjourney, механічний голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Джерело зображення: Вікіпедія, зображення створене Midjourney_

## Як працюють DALL-E і Midjourney

Спершу про [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — генеративна модель ШІ на основі архітектури трансформера з _авторегресивним трансформером_.

_Авторегресивний трансформер_ визначає, як модель генерує зображення з текстових описів: вона створює по одному пікселю за раз і використовує згенеровані пікселі для створення наступного пікселя, проходячи через кілька шарів нейронної мережі, поки зображення не буде завершене.

За цим процесом DALL-E контролює атрибути, об’єкти, характеристики та інші елементи зображення, яке генерує. Однак DALL-E 2 і 3 мають більший контроль над створеним зображенням.

## Створення вашого першого додатка для генерації зображень

Що потрібно, щоб створити додаток для генерації зображень? Вам потрібні такі бібліотеки:

- **python-dotenv** — настійно рекомендуємо використовувати цю бібліотеку, щоб зберігати ваші секрети у файлі _.env_ подалі від коду.
- **openai** — ця бібліотека використовується для взаємодії з API OpenAI.
- **pillow** — для роботи з зображеннями в Python.
- **requests** — для допомоги у виконанні HTTP-запитів.

## Створення та розгортання моделі Azure OpenAI

Якщо ще не зробили цього, дотримуйтесь інструкцій на сторінці [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 
для створення ресурсу Azure OpenAI та моделі. Оберіть модель **gpt-image-1** (поточна генерація моделі зображень Azure OpenAI; DALL-E 3 — застаріла і більше недоступна для нових розгортань).

## Створення додатка

1. Створіть файл _.env_ з таким вмістом:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Знайдіть цю інформацію в Порталі Azure OpenAI Foundry у розділі "Deployments" для вашого ресурсу.

1. Зберіть перелік згаданих бібліотек у файлі _requirements.txt_ таким чином:

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

   Для Windows використовуйте наступні команди, щоб створити й активувати віртуальне середовище:

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
    
    # імпортувати dotenv
    dotenv.load_dotenv()
    
    # налаштувати клієнта служби Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Створити зображення за допомогою API генерації зображень
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Встановити каталог для збереженого зображення
        image_dir = os.path.join(os.curdir, 'images')

        # Якщо каталог не існує, створити його
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Ініціалізувати шлях до зображення (зверніть увагу, що тип файлу повинен бути png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Отримати згенероване зображення
        image_url = generation_response.data[0].url  # витягнути URL зображення з відповіді
        generated_image = requests.get(image_url).content  # завантажити зображення
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Відобразити зображення у стандартному переглядачі зображень
        image = Image.open(image_path)
        image.show()

    # обробити винятки
    except openai.BadRequestError as err:
        print(err)
   ```

Пояснимо цей код:

- Спершу імпортуємо потрібні бібліотеки, зокрема OpenAI, dotenv, requests і Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Далі завантажуємо змінні середовища з файлу _.env_.

  ```python
  # імпортувати dotenv
  dotenv.load_dotenv()
  ```

- Потім налаштовуємо клієнта сервісу Azure OpenAI 

  ```python
  # Отримати кінцеву точку та ключ із змінних середовища
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Далі генеруємо зображення:

  ```python
  # Створіть зображення за допомогою API генерації зображень
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Вищенаведений код повертає JSON-об'єкт з URL згенерованого зображення. Ми можемо використати URL, щоб завантажити зображення та зберегти його у файл.

- Нарешті, відкриваємо зображення і відображаємо його стандартним переглядачем зображень:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детальніше про генерацію зображення

Розглянемо докладніше код, який генерує зображення:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** — текстова підказка, яка використовується для генерації зображення. У цьому випадку ми використовуємо підказку "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси".
- **size** — розмір генерованого зображення. Тут ми генеруємо зображення розмірами 1024x1024 пікселів.
- **n** — кількість згенерованих зображень. Тут ми генеруємо два зображення.
- **temperature** — параметр, що керує випадковістю вихідних даних генеративної моделі ШІ. Температура — це значення між 0 та 1, де 0 означає детермінований вихід, а 1 — випадковий. Значення за замовчуванням — 0.7.

Зі зображеннями можна виконувати більше операцій, про це ми поговоримо в наступному розділі.

## Додаткові можливості генерації зображень

Ви вже побачили, як можна згенерувати зображення у кілька рядків пухнастою мовою Python. Але є й інші можливості роботи із зображеннями.

Ви також можете:

- **Виконувати редагування**. Надаючи на вхід існуюче зображення, маску та підказку, ви можете змінювати зображення. Наприклад, можна додати щось до певної ділянки зображення. Уявімо наше зображення з кроликом — можна додати капелюх. Для цього передаємо зображення, маску (яка ідентифікує область для зміни) та текстову підказку, що описує потрібну операцію.
> Примітка: це не підтримується у DALL-E 3.
 
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

  Початкове зображення містить лише лаунж із басейном, але кінцеве зображення матиме фламінго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/uk/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/uk/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/uk/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Створювати варіації**. Ідея полягає в тому, що ви берете наявне зображення і просите створити його варіації. Щоб створити варіацію, надайте зображення, текстову підказку і код, як наведено нижче:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Примітка, це підтримується лише у моделі OpenAI DALL-E 2, не в gpt-image-1

## Температура

Температура — це параметр, що керує випадковістю вихідних даних генеративної моделі ШІ. Температура — значення між 0 і 1, де 0 означає детермінованість виходу, а 1 — випадковість. За замовчуванням – 0.7.

Розглянемо приклад роботи температури, запустивши цю підказку двічі:

> Підказка: "Кролик на коні, тримає льодяник, на туманному лузі, де ростуть нарциси"

![Кролик на коні, що тримає льодяник, версія 1](../../../translated_images/uk/v1-generated-image.a295cfcffa3c13c2.webp)

Тепер запустимо ту саму підказку ще раз, щоб переконатися, що ми не отримаємо однакове зображення двічі:

![Згенероване зображення кролика на коні](../../../translated_images/uk/v2-generated-image.33f55a3714efe61d.webp)

Як бачите, зображення схожі, але не однакові. Спробуємо змінити значення температури на 0.1 і подивимося, що станеться:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Введіть текст підказки тут
        size='1024x1024',
        n=2
    )
```

### Зміна температури

Отже, давайте спробуємо зробити відповідь більш детермінованою. За двома згенерованими зображеннями ми помітили, що на першому є кролик, а на другому — кінь, тому зображення значно відрізняються.

Тож змінимо код і встановимо температуру в 0 так:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Введіть текст підказки тут
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Тепер, запускаючи цей код, ви отримаєте ці два зображення:

- ![Температура 0, версія 1](../../../translated_images/uk/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Температура 0, версія 2](../../../translated_images/uk/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Тут чітко видно, що зображення зовсім більше схожі одне на одне.

## Як визначати межі для вашого додатка за допомогою метапідказок

За допомогою нашої демо-версії ми вже можемо генерувати зображення для наших клієнтів. Проте нам треба встановити певні межі для додатка.

Наприклад, ми не хочемо генерувати зображення, які не є безпечними для робочого середовища або неприйнятними для дітей.

Ми можемо зробити це за допомогою _метапідказок_. Метапідказки — це текстові підказки, котрі використовуються для контролю результату генеративної моделі ШІ. Наприклад, можна застосувати метапідказки, щоб керувати виходом і гарантувати, що створені зображення безпечні для робочого середовища та прийнятні для дітей.

### Як це працює?

Отже, як працюють метапідказки?

Метапідказки — це текстові запити, які контролюють вихід генеративної моделі. Вони розташовуються перед основною підказкою і використовуються для обмеження результату моделі, вбудовуються у додатки як єдиний текстовий запит, що поєднує метапідказку і основний запит.

Приклад метапідказки:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Тепер подивимося, як ми можемо використати метапідказки у нашій демонстрації.

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

# TODO додати запит на генерацію зображення
```

З наведеного запиту видно, що всі створені зображення враховують метапідказку.

## Завдання — навчимо студентів

Ми згадали Edu4All на початку уроку. Тепер час надати студентам можливість генерувати зображення для їхніх завдань.


Студенти створять зображення для своїх оцінювань з пам’ятниками, які саме пам’ятники — вирішують студенти. Їх просять використовувати свою творчість у цьому завданні, щоб розміщувати ці пам’ятники в різних контекстах.

## Рішення

Ось одне можливе рішення:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# імпортувати dotenv
dotenv.load_dotenv()

# Отримати кінцеву точку та ключ з змінних оточення
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # Створити зображення за допомогою API генерації зображень
    generation_response = client.images.generate(
        prompt=prompt,    # Введіть тут текст запиту
        size='1024x1024',
        n=1,
    )
    # Встановити директорію для збереженого зображення
    image_dir = os.path.join(os.curdir, 'images')

    # Якщо директорія не існує, створити її
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Ініціалізувати шлях до зображення (зауважте, тип файлу повинен бути png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Отримати згенероване зображення
    image_url = generation_response.data[0].url  # витягнути URL зображення з відповіді
    generated_image = requests.get(image_url).content  # завантажити зображення
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Відобразити зображення у стандартному переглядачі зображень
    image = Image.open(image_path)
    image.show()

# обробити виключення
except openai.BadRequestError as err:
    print(err)
```

## Відмінна робота! Продовжуйте навчання

Після завершення цього уроку перегляньте нашу [колекцію навчання генеративного ШІ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб продовжити підвищувати свої знання з генеративного ШІ!

Перейдіть до Уроку 10, де ми розглянемо, як [будувати ШІ-застосунки з низьким кодом](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->