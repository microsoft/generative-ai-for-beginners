<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:04:17+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ru"
}
-->
# Создание приложений для генерации изображений

[![Создание приложений для генерации изображений](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ru.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM могут делать не только генерацию текста. Также возможно создавать изображения из текстовых описаний. Наличие изображений в качестве модальности может быть чрезвычайно полезным во многих областях, таких как медицинские технологии, архитектура, туризм, разработка игр и многое другое. В этой главе мы рассмотрим две наиболее популярные модели генерации изображений, DALL-E и Midjourney.

## Введение

В этом уроке мы рассмотрим:

- Генерацию изображений и почему это полезно.
- DALL-E и Midjourney, что это такое и как они работают.
- Как создать приложение для генерации изображений.

## Цели обучения

После завершения этого урока вы сможете:

- Создать приложение для генерации изображений.
- Определить границы для вашего приложения с помощью метаподсказок.
- Работать с DALL-E и Midjourney.

## Почему создавать приложение для генерации изображений?

Приложения для генерации изображений — отличный способ изучить возможности генеративного ИИ. Они могут использоваться, например, для:

- **Редактирование и синтез изображений**. Вы можете генерировать изображения для различных случаев использования, таких как редактирование изображений и синтез изображений.

- **Применение в различных отраслях**. Они также могут использоваться для генерации изображений для различных отраслей, таких как медицинские технологии, туризм, разработка игр и многое другое.

## Сценарий: Edu4All

В рамках этого урока мы продолжим работу с нашим стартапом Edu4All. Студенты создадут изображения для своих оценок, какие именно изображения — на усмотрение студентов, но они могут быть иллюстрациями для их собственной сказки или создания нового персонажа для их истории или помочь им визуализировать свои идеи и концепции.

Вот что, например, студенты Edu4All могли бы создать, если бы они работали в классе над памятниками:

![Стартап Edu4All, класс по памятникам, Эйфелева башня](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ru.png)

используя такую подсказку:

> "Собака рядом с Эйфелевой башней на утреннем солнце"

## Что такое DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — две из самых популярных моделей генерации изображений, которые позволяют использовать подсказки для генерации изображений.

### DALL-E

Начнем с DALL-E, который является генеративной моделью ИИ, создающей изображения из текстовых описаний.

> [DALL-E — это комбинация двух моделей, CLIP и рассеянного внимания](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — это модель, которая создает встраивания, численные представления данных, из изображений и текста.

- **Рассеянное внимание** — это модель, которая создает изображения из встраиваний. DALL-E обучен на наборе данных изображений и текста и может использоваться для создания изображений из текстовых описаний. Например, DALL-E может использоваться для создания изображений кота в шляпе или собаки с ирокезом.

### Midjourney

Midjourney работает аналогично DALL-E, он генерирует изображения из текстовых подсказок. Midjourney также может использоваться для генерации изображений с использованием подсказок, таких как "кот в шляпе" или "собака с ирокезом".

![Изображение, созданное Midjourney, механический голубь](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Кредиты изображения Википедия, изображение создано Midjourney_

## Как работают DALL-E и Midjourney

Сначала [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — это генеративная модель ИИ, основанная на архитектуре трансформера с _авторегрессивным трансформером_.

_Авторегрессивный трансформер_ определяет, как модель создает изображения из текстовых описаний: она генерирует один пиксель за раз, а затем использует сгенерированные пиксели для генерации следующего пикселя, проходя через несколько слоев нейронной сети, пока изображение не будет завершено.

С помощью этого процесса DALL-E контролирует атрибуты, объекты, характеристики и многое другое в создаваемом изображении. Однако DALL-E 2 и 3 имеют больше контроля над созданным изображением.

## Создание вашего первого приложения для генерации изображений

Итак, что нужно для создания приложения для генерации изображений? Вам понадобятся следующие библиотеки:

- **python-dotenv**, настоятельно рекомендуется использовать эту библиотеку для хранения ваших секретов в файле _.env_ вдали от кода.
- **openai**, эта библиотека будет использоваться для взаимодействия с API OpenAI.
- **pillow**, для работы с изображениями в Python.
- **requests**, чтобы помочь вам делать HTTP-запросы.

1. Создайте файл _.env_ со следующим содержанием:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Найдите эту информацию в Azure Portal для вашего ресурса в разделе "Ключи и конечная точка".

1. Соберите вышеупомянутые библиотеки в файл _requirements.txt_ следующим образом:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Далее создайте виртуальную среду и установите библиотеки:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Для Windows используйте следующие команды для создания и активации виртуальной среды:

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

Давайте объясним этот код:

- Сначала мы импортируем необходимые библиотеки, включая библиотеку OpenAI, библиотеку dotenv, библиотеку requests и библиотеку Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Далее загружаем переменные окружения из файла _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- После этого устанавливаем конечную точку, ключ для API OpenAI, версию и тип.

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

  Вышеприведенный код отвечает JSON-объектом, содержащим URL сгенерированного изображения. Мы можем использовать URL для загрузки изображения и сохранения его в файл.

- Наконец, открываем изображение и используем стандартный просмотрщик изображений для его отображения:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Подробнее о генерации изображения

Давайте подробнее рассмотрим код, который генерирует изображение:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** — это текстовая подсказка, используемая для генерации изображения. В данном случае мы используем подсказку "Кролик на лошади, держащий леденец, на туманном лугу, где растут нарциссы".
- **size** — это размер создаваемого изображения. В данном случае мы создаем изображение размером 1024x1024 пикселей.
- **n** — количество создаваемых изображений. В данном случае мы создаем два изображения.
- **temperature** — это параметр, который контролирует случайность вывода генеративной модели ИИ. Температура — это значение между 0 и 1, где 0 означает, что вывод детерминирован, а 1 означает, что вывод случайен. Значение по умолчанию — 0.7.

Есть еще много вещей, которые можно делать с изображениями, о которых мы поговорим в следующем разделе.

## Дополнительные возможности генерации изображений

Вы уже видели, как мы смогли создать изображение с помощью нескольких строк в Python. Однако, есть еще много возможностей работы с изображениями.

Вы также можете делать следующее:

- **Вносить изменения**. Предоставляя существующее изображение, маску и подсказку, вы можете изменить изображение. Например, вы можете добавить что-то в часть изображения. Представьте наше изображение с кроликом, вы можете добавить шляпу кролику. Как это сделать — предоставьте изображение, маску (определяющую часть области для изменения) и текстовую подсказку, чтобы указать, что должно быть сделано.

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

  Базовое изображение будет содержать только кролика, но окончательное изображение будет с шляпой на кролике.

- **Создание вариаций**. Идея заключается в том, что вы берете существующее изображение и просите создать его вариации. Чтобы создать вариацию, вы предоставляете изображение и текстовую подсказку и код следующим образом:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Примечание: это поддерживается только в OpenAI

## Температура

Температура — это параметр, который контролирует случайность вывода генеративной модели ИИ. Температура — это значение между 0 и 1, где 0 означает, что вывод детерминирован, а 1 означает, что вывод случайен. Значение по умолчанию — 0.7.

Давайте посмотрим пример, как работает температура, запустив эту подсказку дважды:

> Подсказка: "Кролик на лошади, держащий леденец, на туманном лугу, где растут нарциссы"

![Кролик на лошади, держащий леденец, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ru.png)

Теперь давайте запустим ту же подсказку, чтобы увидеть, что мы не получим одно и то же изображение дважды:

![Сгенерированное изображение кролика на лошади](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ru.png)

Как вы видите, изображения похожи, но не одинаковы. Давайте попробуем изменить значение температуры на 0.1 и посмотрим, что произойдет:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Изменение температуры

Давайте попробуем сделать ответ более детерминированным. Мы могли наблюдать из двух сгенерированных изображений, что на первом изображении есть кролик, а на втором изображении — лошадь, поэтому изображения сильно различаются.

Таким образом, давайте изменим наш код и установим температуру на 0, следующим образом:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Теперь, когда вы запустите этот код, вы получите эти два изображения:

- ![Температура 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ru.png)
- ![Температура 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ru.png)

Здесь вы можете ясно видеть, как изображения больше напоминают друг друга.

## Как определить границы для вашего приложения с помощью метаподсказок

С нашим демо мы уже можем генерировать изображения для наших клиентов. Однако нам нужно создать некоторые границы для нашего приложения.

Например, мы не хотим генерировать изображения, которые не подходят для работы или не подходят для детей.

Мы можем сделать это с помощью _метаподсказок_. Метаподсказки — это текстовые подсказки, которые используются для контроля вывода генеративной модели ИИ. Например, мы можем использовать метаподсказки для контроля вывода и обеспечения того, чтобы создаваемые изображения были безопасными для работы или подходили для детей.

### Как это работает?

Теперь, как работают метаподсказки?

Метаподсказки — это текстовые подсказки, которые используются для контроля вывода генеративной модели ИИ, они размещаются перед текстовой подсказкой и используются для контроля вывода модели и встроены в приложения для контроля вывода модели. Инкапсулируя ввод подсказки и ввод метаподсказки в одну текстовую подсказку.

Примером метаподсказки может быть следующее:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Теперь давайте посмотрим, как мы можем использовать метаподсказки в нашем демо.

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

Из приведенной выше подсказки вы можете увидеть, как все создаваемые изображения учитывают метаподсказку.

## Задание — давайте дадим возможность студентам

Мы представили Edu4All в начале этого урока. Теперь пришло время дать студентам возможность генерировать изображения для их оценок.

Студенты создадут изображения для своих оценок, содержащие памятники, какие именно памятники — на усмотрение студентов. Студентам предлагается использовать свою креативность в этой задаче, чтобы разместить эти памятники в различных контекстах.

## Решение

Вот одно из возможных решений:

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

## Отличная работа! Продолжайте обучение

После завершения этого урока ознакомьтесь с нашей [коллекцией обучения генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышение уровня своих знаний о генеративном ИИ!

Перейдите к уроку 10, где мы рассмотрим, как [создавать AI-приложения с использованием мало кода](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.