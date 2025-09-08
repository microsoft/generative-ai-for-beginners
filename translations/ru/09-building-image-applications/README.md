<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T13:57:27+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ru"
}
-->
# Создание приложений для генерации изображений

[![Создание приложений для генерации изображений](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ru.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM умеют не только генерировать текст. С их помощью можно создавать изображения по текстовому описанию. Использование изображений как отдельной модальности может быть очень полезно в таких сферах, как медицина, архитектура, туризм, разработка игр и других. В этой главе мы рассмотрим две самые популярные модели генерации изображений — DALL-E и Midjourney.

## Введение

В этом уроке мы разберём:

- Генерацию изображений и её преимущества.
- DALL-E и Midjourney: что это такое и как они работают.
- Как создать собственное приложение для генерации изображений.

## Цели обучения

После прохождения этого урока вы сможете:

- Создать приложение для генерации изображений.
- Определять границы для вашего приложения с помощью метаподсказок.
- Работать с DALL-E и Midjourney.

## Зачем создавать приложение для генерации изображений?

Приложения для генерации изображений — отличный способ познакомиться с возможностями генеративного ИИ. Их можно использовать, например, для:

- **Редактирования и синтеза изображений**. Можно создавать изображения для разных задач, например, для редактирования или синтеза.

- **Применения в различных отраслях**. Такие приложения могут быть полезны в медицине, туризме, игровой индустрии и других сферах.

## Сценарий: Edu4All

В рамках этого урока мы продолжаем работать с нашим стартапом Edu4All. Студенты будут создавать изображения для своих заданий — какие именно, решают они сами: это могут быть иллюстрации к собственной сказке, новый персонаж для истории или визуализация идей и концепций.

Например, если студенты Edu4All изучают памятники, они могут сгенерировать такое изображение:

![Стартап Edu4All, урок о памятниках, Эйфелева башня](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ru.png)

используя такой запрос:

> "Собака рядом с Эйфелевой башней на рассвете"

## Что такое DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — две самые популярные модели генерации изображений, которые позволяют создавать картинки по текстовым подсказкам.

### DALL-E

Начнём с DALL-E — это генеративная модель ИИ, создающая изображения по текстовому описанию.

> [DALL-E — это комбинация двух моделей: CLIP и diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — модель, которая создаёт эмбеддинги (числовые представления данных) из изображений и текста.

- **Diffused attention** — модель, которая генерирует изображения на основе эмбеддингов. DALL-E обучена на большом наборе изображений и текстов, и может создавать картинки по текстовому описанию. Например, DALL-E может нарисовать кота в шляпе или собаку с ирокезом.

### Midjourney

Midjourney работает похожим образом: она тоже создаёт изображения по текстовым подсказкам. Например, можно сгенерировать картинку с “котом в шляпе” или “собакой с ирокезом”.

![Изображение, созданное Midjourney, механический голубь](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Источник: Wikipedia, изображение создано Midjourney_

## Как работают DALL-E и Midjourney

Сначала [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — это генеративная модель ИИ на архитектуре трансформеров с _авторегрессивным трансформером_.

_Авторегрессивный трансформер_ определяет, как модель создаёт изображение по тексту: она генерирует по одному пикселю за раз, используя уже созданные пиксели для генерации следующих, проходя через несколько слоёв нейросети, пока картинка не будет готова.

Благодаря этому процессу DALL-E может управлять атрибутами, объектами, характеристиками и другими деталями изображения. DALL-E 2 и 3 дают ещё больше контроля над результатом.

## Создаём первое приложение для генерации изображений

Что нужно для создания такого приложения? Понадобятся следующие библиотеки:

- **python-dotenv** — рекомендуется использовать для хранения секретов в файле _.env_ отдельно от кода.
- **openai** — библиотека для работы с OpenAI API.
- **pillow** — для работы с изображениями в Python.
- **requests** — для HTTP-запросов.

## Создайте и разверните модель Azure OpenAI

Если вы ещё не сделали этого, следуйте инструкции на [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
для создания ресурса и модели Azure OpenAI. В качестве модели выберите DALL-E 3.  

## Создаём приложение

1. Создайте файл _.env_ со следующим содержимым:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Найдите эту информацию в Azure OpenAI Foundry Portal для вашего ресурса в разделе "Deployments".

1. Соберите вышеуказанные библиотеки в файле _requirements.txt_ вот так:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Далее создайте виртуальное окружение и установите библиотеки:

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

Объясним этот код:

- Сначала импортируем необходимые библиотеки: OpenAI, dotenv, requests и Pillow.

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

- После этого настраиваем клиент Azure OpenAI Service

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Далее генерируем изображение:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Этот код возвращает JSON-объект с URL сгенерированного изображения. Мы можем скачать картинку по этому адресу и сохранить её в файл.

- В конце открываем изображение и показываем его в стандартном просмотрщике:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Подробнее о генерации изображения

Рассмотрим подробнее код, который отвечает за генерацию изображения:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** — текстовая подсказка, по которой создаётся изображение. В данном случае: "Кролик на лошади, держит леденец, на туманном лугу, где растут нарциссы".
- **size** — размер создаваемого изображения. Здесь — 1024x1024 пикселей.
- **n** — количество генерируемых изображений. В данном случае — два.
- **temperature** — параметр, определяющий степень случайности результата генеративной модели. Значение от 0 до 1: 0 — результат детерминированный, 1 — случайный. По умолчанию — 0.7.

О других возможностях работы с изображениями поговорим далее.

## Дополнительные возможности генерации изображений

Вы уже увидели, как можно сгенерировать изображение с помощью нескольких строк кода на Python. Но возможностей гораздо больше.

Можно делать следующее:

- **Редактировать изображения**. Если предоставить исходное изображение, маску и текстовую подсказку, можно изменить картинку. Например, добавить что-то в определённую область. Представьте наш кролика — можно добавить ему шляпу. Для этого нужно передать изображение, маску (область для изменений) и текстовую подсказку, описывающую, что нужно сделать.
> Обратите внимание: эта функция не поддерживается в DALL-E 3.

Вот пример с использованием GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Исходное изображение содержит только лаунж с бассейном, а итоговое — уже с фламинго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Создавать вариации**. Можно взять существующее изображение и попросить создать его варианты. Для этого передаётся изображение, текстовая подсказка и код примерно такой:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Обратите внимание: это поддерживается только в OpenAI

## Температура

Температура — это параметр, который определяет степень случайности результата генеративной модели. Значение от 0 до 1: 0 — результат детерминированный, 1 — случайный. По умолчанию — 0.7.

Посмотрим, как работает температура, если дважды выполнить такой запрос:

> Запрос: "Кролик на лошади, держит леденец, на туманном лугу, где растут нарциссы"

![Кролик на лошади с леденцом, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ru.png)

Теперь повторим тот же запрос и увидим, что результат будет отличаться:

![Сгенерированное изображение кролика на лошади](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ru.png)

Как видно, изображения похожи, но не идентичны. Попробуем изменить значение температуры на 0.1 и посмотрим, что получится:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Изменение температуры

Попробуем сделать результат более предсказуемым. Мы видим, что на первом изображении есть кролик, а на втором — лошадь, то есть различия довольно заметны.

Изменим код и установим температуру в 0:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Теперь при запуске этого кода получаем такие изображения:

- ![Температура 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ru.png)
- ![Температура 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ru.png)

Здесь видно, что изображения стали гораздо более похожими друг на друга.

## Как задать границы для приложения с помощью метаподсказок

В нашем демо мы уже можем генерировать изображения для клиентов. Но нам нужно задать определённые границы для приложения.

Например, мы не хотим создавать изображения, которые не подходят для работы или для детей.

Для этого используются _метаподсказки_. Метаподсказки — это текстовые подсказки, которые позволяют контролировать результат генеративной модели. С их помощью можно, например, гарантировать, что изображения будут безопасны для работы или для детей.

### Как это работает?

Как работают метаподсказки?

Метаподсказки — это текстовые подсказки, которые размещаются перед основным запросом и используются для управления результатом модели. Они внедряются в приложение и позволяют контролировать результат, объединяя основной запрос и метаподсказку в одну строку.

Пример метаподсказки:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Теперь посмотрим, как использовать метаподсказки в нашем демо.

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

Из этого запроса видно, что все создаваемые изображения учитывают метаподсказку.

## Задание — даём возможность студентам

В начале урока мы познакомились с Edu4All. Теперь пришло время дать студентам возможность создавать изображения для своих заданий.

Студенты будут создавать изображения с памятниками для своих работ — какие именно памятники, решают они сами. Им предлагается проявить креативность и поместить памятники в разные контексты.

## Решение

Вот один из возможных вариантов решения:

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

## Отличная работа! Продолжайте обучение
После завершения этого урока загляните в нашу [коллекцию по обучению генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

Переходите к уроку 10, где мы рассмотрим, как [создавать AI-приложения с помощью low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.