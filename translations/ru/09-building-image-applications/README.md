<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T15:06:17+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ru"
}
-->
# Создание приложений для генерации изображений

[![Создание приложений для генерации изображений](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ru.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Генерация текста — это не единственное, что могут делать LLM. Также возможно создавать изображения на основе текстовых описаний. Наличие изображений как модальности может быть чрезвычайно полезным в различных областях, таких как медицинские технологии, архитектура, туризм, разработка игр и многое другое. В этой главе мы рассмотрим две самые популярные модели генерации изображений: DALL-E и Midjourney.

## Введение

В этом уроке мы рассмотрим:

- Генерацию изображений и её полезность.
- DALL-E и Midjourney: что это такое и как они работают.
- Как создать приложение для генерации изображений.

## Цели обучения

После завершения этого урока вы сможете:

- Создать приложение для генерации изображений.
- Определить границы для вашего приложения с помощью метаподсказок.
- Работать с DALL-E и Midjourney.

## Зачем создавать приложение для генерации изображений?

Приложения для генерации изображений — отличный способ изучить возможности генеративного ИИ. Они могут быть использованы, например, для:

- **Редактирования и синтеза изображений**. Вы можете создавать изображения для различных целей, таких как редактирование и синтез изображений.

- **Применение в различных отраслях**. Они также могут быть использованы для создания изображений для различных отраслей, таких как медицинские технологии, туризм, разработка игр и многое другое.

## Сценарий: Edu4All

В рамках этого урока мы продолжим работать с нашим стартапом Edu4All. Студенты будут создавать изображения для своих заданий. Какие именно изображения — решать студентам, но это могут быть иллюстрации для их собственной сказки, создание нового персонажа для их истории или помощь в визуализации их идей и концепций.

Вот пример того, что студенты Edu4All могут создать, если они работают в классе над темой памятников:

![Стартап Edu4All, класс о памятниках, Эйфелева башня](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ru.png)

используя подсказку вроде:

> "Собака рядом с Эйфелевой башней на утреннем солнце"

## Что такое DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) — две из самых популярных моделей генерации изображений, которые позволяют использовать подсказки для создания изображений.

### DALL-E

Начнем с DALL-E — генеративной модели ИИ, которая создает изображения на основе текстовых описаний.

> [DALL-E — это комбинация двух моделей: CLIP и diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** — модель, которая создает эмбеддинги, числовые представления данных, из изображений и текста.

- **Diffused attention** — модель, которая создает изображения из эмбеддингов. DALL-E обучена на наборе данных изображений и текста и может использоваться для создания изображений на основе текстовых описаний. Например, DALL-E может быть использована для создания изображения кота в шляпе или собаки с ирокезом.

### Midjourney

Midjourney работает аналогично DALL-E, создавая изображения на основе текстовых подсказок. Midjourney также может быть использована для генерации изображений с подсказками вроде "кот в шляпе" или "собака с ирокезом".

![Изображение, созданное Midjourney, механический голубь](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Источник изображения: Wikipedia, изображение создано Midjourney_

## Как работают DALL-E и Midjourney

Сначала [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E — это генеративная модель ИИ, основанная на архитектуре трансформеров с _авторегрессионным трансформером_.

_Авторегрессионный трансформер_ определяет, как модель создает изображения на основе текстовых описаний: она генерирует один пиксель за раз, а затем использует созданные пиксели для генерации следующего пикселя. Проходя через несколько слоев нейронной сети, пока изображение не будет завершено.

С помощью этого процесса DALL-E контролирует атрибуты, объекты, характеристики и многое другое в создаваемом изображении. Однако DALL-E 2 и 3 обеспечивают больший контроль над созданным изображением.

## Создание вашего первого приложения для генерации изображений

Итак, что нужно для создания приложения для генерации изображений? Вам понадобятся следующие библиотеки:

- **python-dotenv** — настоятельно рекомендуется использовать эту библиотеку для хранения секретов в файле _.env_ отдельно от кода.
- **openai** — библиотека, которая используется для взаимодействия с API OpenAI.
- **pillow** — для работы с изображениями в Python.
- **requests** — для выполнения HTTP-запросов.

## Создание и развертывание модели Azure OpenAI

Если это еще не сделано, следуйте инструкциям на странице [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), чтобы создать ресурс и модель Azure OpenAI. Выберите модель DALL-E 3.

## Создание приложения

1. Создайте файл _.env_ со следующим содержанием:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Найдите эту информацию в портале Azure OpenAI Foundry для вашего ресурса в разделе "Deployments".

1. Соберите вышеуказанные библиотеки в файле _requirements.txt_ следующим образом:

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

- Сначала мы импортируем необходимые библиотеки, включая библиотеку OpenAI, библиотеку dotenv, библиотеку requests и библиотеку Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Затем мы загружаем переменные окружения из файла _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- После этого мы настраиваем клиент сервиса Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Далее мы генерируем изображение:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Этот код возвращает JSON-объект, содержащий URL созданного изображения. Мы можем использовать URL для загрузки изображения и сохранения его в файл.

- Наконец, мы открываем изображение и используем стандартный просмотрщик изображений для его отображения:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Подробнее о генерации изображения

Давайте подробнее рассмотрим код, который генерирует изображение:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** — текстовая подсказка, которая используется для генерации изображения. В данном случае мы используем подсказку "Кролик на лошади, держащий леденец, на туманном лугу, где растут нарциссы".
- **size** — размер создаваемого изображения. В данном случае мы создаем изображение размером 1024x1024 пикселей.
- **n** — количество создаваемых изображений. В данном случае мы создаем два изображения.
- **temperature** — параметр, который контролирует случайность вывода генеративной модели ИИ. Температура — это значение от 0 до 1, где 0 означает детерминированный вывод, а 1 — случайный. Значение по умолчанию — 0.7.

Есть еще много возможностей работы с изображениями, которые мы рассмотрим в следующем разделе.

## Дополнительные возможности генерации изображений

Вы уже видели, как мы смогли создать изображение с помощью нескольких строк кода на Python. Однако есть еще много возможностей работы с изображениями.

Вы также можете:

- **Редактировать изображения**. Предоставив существующее изображение, маску и подсказку, вы можете изменить изображение. Например, вы можете добавить что-то на часть изображения. Представьте наше изображение с кроликом, вы можете добавить шляпу кролику. Для этого нужно предоставить изображение, маску (определяющую часть области для изменения) и текстовую подсказку, чтобы указать, что должно быть сделано.
> Примечание: это не поддерживается в DALL-E 3.

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

  Исходное изображение будет содержать только лаунж с бассейном, но итоговое изображение будет включать фламинго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ru.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ru.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ru.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Создавать вариации**. Идея заключается в том, чтобы взять существующее изображение и попросить создать его вариации. Для создания вариации вы предоставляете изображение и текстовую подсказку, а код выглядит следующим образом:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Примечание: это поддерживается только в OpenAI.

## Температура

Температура — это параметр, который контролирует случайность вывода генеративной модели ИИ. Температура — это значение от 0 до 1, где 0 означает детерминированный вывод, а 1 — случайный. Значение по умолчанию — 0.7.

Давайте рассмотрим пример работы температуры, запустив эту подсказку дважды:

> Подсказка: "Кролик на лошади, держащий леденец, на туманном лугу, где растут нарциссы"

![Кролик на лошади, держащий леденец, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ru.png)

Теперь запустим ту же подсказку снова, чтобы увидеть, что мы не получим одно и то же изображение дважды:

![Созданное изображение кролика на лошади](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ru.png)

Как видите, изображения похожи, но не идентичны. Давайте попробуем изменить значение температуры на 0.1 и посмотрим, что произойдет:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Изменение температуры

Попробуем сделать вывод более детерминированным. Мы могли наблюдать, что на первом изображении есть кролик, а на втором — лошадь, так что изображения сильно различаются.

Давайте изменим наш код и установим температуру на 0, вот так:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Теперь, когда вы запустите этот код, вы получите эти два изображения:

- ![Температура 0, версия 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ru.png)
- ![Температура 0, версия 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ru.png)

Здесь вы можете ясно видеть, как изображения больше похожи друг на друга.

## Как определить границы для вашего приложения с помощью метаподсказок

С помощью нашего демо мы уже можем создавать изображения для наших клиентов. Однако нам нужно установить некоторые границы для нашего приложения.

Например, мы не хотим создавать изображения, которые не подходят для работы или не подходят для детей.

Мы можем сделать это с помощью _метаподсказок_. Метаподсказки — это текстовые подсказки, которые используются для контроля вывода генеративной модели ИИ. Например, мы можем использовать метаподсказки для контроля вывода и обеспечения того, чтобы создаваемые изображения были подходящими для работы или детей.

### Как это работает?

Итак, как работают метаподсказки?

Метаподсказки — это текстовые подсказки, которые используются для контроля вывода генеративной модели ИИ. Они размещаются перед текстовой подсказкой и используются для контроля вывода модели, внедряясь в приложения для управления выводом модели. Инкапсулируя ввод подсказки и ввод метаподсказки в одну текстовую подсказку.

Пример метаподсказки может выглядеть следующим образом:

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

Из приведенной выше подсказки видно, как все создаваемые изображения учитывают метаподсказку.

## Задание — давайте дадим возможность студентам

Мы представили Edu4All в начале этого урока. Теперь пришло время дать студентам возможность создавать изображения для их заданий.

Студенты будут создавать изображения для своих заданий, содержащих памятники. Какие именно памятники — решать студентам. Студенты должны проявить свою креативность в этом задании, размещая эти памятники в различных контекстах.

## Решение

Вот одно из возможных решений:
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

После завершения этого урока ознакомьтесь с нашей [коллекцией обучения генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышать свои знания о генеративном ИИ!

Перейдите к уроку 10, где мы рассмотрим, как [создавать AI-приложения с использованием low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.