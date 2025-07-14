<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:15:46+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ru"
}
-->
# Создание приложений для генерации изображений

[![Создание приложений для генерации изображений](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ru.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM — это не только генерация текста. Также можно создавать изображения на основе текстовых описаний. Использование изображений как модальности может быть очень полезным во многих сферах: от медицины и архитектуры до туризма, разработки игр и других областей. В этой главе мы рассмотрим два самых популярных модели генерации изображений — DALL-E и Midjourney.

## Введение

В этом уроке мы рассмотрим:

- Генерацию изображений и её полезность.
- Что такое DALL-E и Midjourney, и как они работают.
- Как создать приложение для генерации изображений.

## Цели обучения

После прохождения этого урока вы сможете:

- Создавать приложение для генерации изображений.
- Определять границы вашего приложения с помощью мета-промптов.
- Работать с DALL-E и Midjourney.

## Зачем создавать приложение для генерации изображений?

Приложения для генерации изображений — отличный способ исследовать возможности генеративного ИИ. Их можно использовать, например, для:

- **Редактирования и синтеза изображений**. Вы можете создавать изображения для разных задач, таких как редактирование и синтез.

- **Применения в различных отраслях**. Их также можно использовать для создания изображений в таких сферах, как медицина, туризм, разработка игр и другие.

## Сценарий: Edu4All

В рамках этого урока мы продолжим работать с нашим стартапом Edu4All. Студенты будут создавать изображения для своих заданий — какие именно, решают они сами: это могут быть иллюстрации к собственной сказке, создание нового персонажа для истории или визуализация идей и концепций.

Вот что студенты Edu4All могли бы создать, если работают в классе над темой памятников:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ru.png)

используя такой промпт

> "Собака рядом с Эйфелевой башней на рассвете"

## Что такое DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — две из самых популярных моделей генерации изображений, которые позволяют создавать картинки по текстовым запросам.

### DALL-E

Начнём с DALL-E — это модель генеративного ИИ, которая создаёт изображения на основе текстовых описаний.

> [DALL-E — это сочетание двух моделей, CLIP и diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — модель, которая создаёт эмбеддинги, то есть числовые представления данных, из изображений и текста.

- **Diffused attention** — модель, которая генерирует изображения из эмбеддингов. DALL-E обучена на наборе данных из изображений и текстов и может создавать картинки по текстовым описаниям. Например, DALL-E может сгенерировать изображение кота в шляпе или собаки с ирокезом.

### Midjourney

Midjourney работает похожим образом — она создаёт изображения по текстовым промптам. Midjourney также может генерировать картинки по запросам вроде «кот в шляпе» или «собака с ирокезом».

![Изображение, созданное Midjourney, механический голубь](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Источник изображения: Wikipedia, создано Midjourney_

## Как работают DALL-E и Midjourney

Сначала о [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — это модель генеративного ИИ на основе архитектуры трансформера с _авторегрессионным трансформером_.

_Авторегрессионный трансформер_ описывает, как модель создаёт изображения из текстовых описаний: она генерирует по одному пикселю за раз, используя уже сгенерированные пиксели для создания следующего. Проходя через несколько слоёв нейронной сети, пока изображение не будет полностью сформировано.

Таким образом, DALL-E контролирует атрибуты, объекты, характеристики и другие детали создаваемого изображения. Однако DALL-E 2 и 3 обеспечивают ещё более точный контроль над результатом.

## Создание вашего первого приложения для генерации изображений

Что нужно для создания приложения генерации изображений? Вам понадобятся следующие библиотеки:

- **python-dotenv** — настоятельно рекомендуется использовать эту библиотеку, чтобы хранить секреты в файле _.env_, отдельно от кода.
- **openai** — библиотека для взаимодействия с OpenAI API.
- **pillow** — для работы с изображениями в Python.
- **requests** — для выполнения HTTP-запросов.

1. Создайте файл _.env_ со следующим содержимым:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Найдите эту информацию в Azure Portal для вашего ресурса в разделе «Keys and Endpoint».

1. Соберите перечисленные библиотеки в файл _requirements.txt_ следующим образом:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Затем создайте виртуальное окружение и установите библиотеки:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Для Windows используйте следующие команды для создания и активации виртуального окружения:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Добавьте следующий код в файл _app.py_:

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

Объясним этот код:

- Сначала импортируем необходимые библиотеки, включая OpenAI, dotenv, requests и Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Затем загружаем переменные окружения из файла _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- После этого задаём endpoint, ключ для OpenAI API, версию и тип.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Далее генерируем изображение:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Этот код возвращает JSON-объект с URL сгенерированного изображения. Мы можем использовать этот URL, чтобы скачать изображение и сохранить его в файл.

- Наконец, открываем изображение и показываем его с помощью стандартного просмотрщика:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Подробнее о генерации изображения

Рассмотрим код генерации изображения более подробно:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** — текстовый запрос для генерации изображения. В данном случае это «Заяц на лошади, держащий леденец, на туманном лугу, где растут нарциссы».
- **size** — размер создаваемого изображения. Здесь это 1024x1024 пикселей.
- **n** — количество создаваемых изображений. Здесь создаются два изображения.
- **temperature** — параметр, контролирующий случайность результата генеративной модели. Значение от 0 до 1, где 0 означает детерминированный результат, а 1 — максимально случайный. Значение по умолчанию — 0.7.

В следующем разделе мы рассмотрим дополнительные возможности работы с изображениями.

## Дополнительные возможности генерации изображений

Вы уже видели, как можно создать изображение всего несколькими строками кода на Python. Но с изображениями можно делать гораздо больше.

Вы также можете:

- **Вносить изменения**. Предоставив существующее изображение, маску и промпт, можно изменить картинку. Например, добавить что-то на часть изображения. Представьте наше изображение с зайцем — можно добавить ему шляпу. Для этого нужно предоставить исходное изображение, маску (обозначающую область для изменения) и текстовый запрос, описывающий, что нужно сделать.

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

  Исходное изображение содержит только зайца, а итоговое — зайца в шляпе.

- **Создавать вариации**. Идея в том, чтобы взять существующее изображение и попросить создать его вариации. Для этого нужно предоставить изображение и текстовый запрос, а затем использовать такой код:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Обратите внимание, что эта функция поддерживается только в OpenAI.

## Температура

Температура — параметр, который регулирует случайность результата генеративной модели. Значение от 0 до 1, где 0 означает детерминированный результат, а 1 — максимально случайный. Значение по умолчанию — 0.7.

Рассмотрим пример работы температуры, выполнив этот промпт дважды:

> Промпт: "Заяц на лошади, держащий леденец, на туманном лугу, где растут нарциссы"

![Заяц на лошади с леденцом, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ru.png)

Теперь выполним тот же промпт ещё раз, чтобы убедиться, что изображения не будут одинаковыми:

![Сгенерированное изображение зайца на лошади](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ru.png)

Как видите, изображения похожи, но не идентичны. Попробуем изменить значение температуры на 0.1 и посмотрим, что получится:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Изменение температуры

Попробуем сделать результат более детерминированным. По двум сгенерированным изображениям видно, что в первом изображён заяц, а во втором — лошадь, то есть картинки сильно отличаются.

Поэтому изменим код и установим температуру в 0:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Теперь при запуске этого кода вы получите следующие два изображения:

- ![Температура 0, версия 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ru.png)
- ![Температура 0, версия 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ru.png)

Здесь видно, что изображения стали гораздо более похожими друг на друга.

## Как определить границы для вашего приложения с помощью мета-промптов

С нашим демо мы уже можем генерировать изображения для клиентов. Однако нам нужно задать некоторые ограничения для приложения.

Например, мы не хотим создавать изображения, которые не подходят для работы или неуместны для детей.

Это можно сделать с помощью _мета-промптов_. Мета-промпты — это текстовые запросы, которые используются для контроля вывода генеративной модели. Например, с их помощью можно гарантировать, что создаваемые изображения будут безопасными для работы или подходящими для детей.

### Как это работает?

Итак, как работают мета-промпты?

Мета-промпты — это текстовые запросы, которые размещаются перед основным промптом и служат для контроля вывода модели. Они встроены в приложения для управления результатом, объединяя ввод основного промпта и мета-промпта в один текстовый запрос.

Пример мета-промпта:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Теперь посмотрим, как использовать мета-промпты в нашем демо.

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

Из приведённого промпта видно, что все создаваемые изображения учитывают мета-промпт.

## Задание — давайте дадим возможность студентам

В начале урока мы познакомились со стартапом Edu4All. Теперь пришло время дать студентам возможность создавать изображения для своих заданий.

Студенты будут создавать изображения с памятниками, какие именно — решают они сами. Им предлагается проявить творческий подход и разместить памятники в разных контекстах.

## Решение

Вот один из возможных вариантов решения:

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

## Отличная работа! Продолжайте обучение

После прохождения этого урока ознакомьтесь с нашей [коллекцией по генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

Переходите к уроку 10, где мы рассмотрим, как [создавать AI-приложения с помощью low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.