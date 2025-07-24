<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:33:51+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bg"
}
-->
# Създаване на приложения за генериране на изображения

[![Създаване на приложения за генериране на изображения](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.bg.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM моделите не са само за генериране на текст. Възможно е също така да се генерират изображения от текстови описания. Използването на изображения като модалност може да бъде изключително полезно в различни области като Медицински технологии, архитектура, туризъм, разработка на игри и други. В тази глава ще разгледаме двата най-популярни модела за генериране на изображения – DALL-E и Midjourney.

## Въведение

В този урок ще разгледаме:

- Генериране на изображения и защо е полезно.
- Какво представляват DALL-E и Midjourney и как работят.
- Как да създадете приложение за генериране на изображения.

## Цели на обучението

След завършване на този урок ще можете да:

- Създавате приложение за генериране на изображения.
- Определяте граници за вашето приложение с помощта на мета промпти.
- Работите с DALL-E и Midjourney.

## Защо да създавате приложение за генериране на изображения?

Приложенията за генериране на изображения са отличен начин да изследвате възможностите на Генеративния AI. Те могат да се използват, например, за:

- **Редактиране и синтез на изображения**. Можете да генерирате изображения за различни случаи на употреба, като редактиране и синтез на изображения.

- **Приложение в различни индустрии**. Те могат да се използват за създаване на изображения в различни индустрии като Медицински технологии, Туризъм, Разработка на игри и други.

## Сценарий: Edu4All

В рамките на този урок ще продължим да работим със стартиращата ни компания Edu4All. Учениците ще създават изображения за своите оценки – какви точно изображения зависи от тях, но това могат да бъдат илюстрации за собствена приказка, нов герой за тяхната история или помощ за визуализиране на идеи и концепции.

Ето какво биха могли да създадат учениците на Edu4All, ако работят в час по темата за паметници:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.bg.png)

с помощта на промпт като

> "Куче до Айфеловата кула в ранна сутрешна светлина"

## Какво са DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) са два от най-популярните модела за генериране на изображения, които позволяват използването на промпти за създаване на изображения.

### DALL-E

Нека започнем с DALL-E, който е генеративен AI модел, създаващ изображения от текстови описания.

> [DALL-E е комбинация от два модела – CLIP и diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** е модел, който създава вграждания (embeddings) – числови представяния на данни – от изображения и текст.

- **Diffused attention** е модел, който генерира изображения от тези вграждания. DALL-E е обучен върху набор от изображения и текст и може да се използва за създаване на изображения от текстови описания. Например, DALL-E може да генерира изображения на котка с шапка или куче с ирокез.

### Midjourney

Midjourney работи по подобен начин на DALL-E – генерира изображения от текстови промпти. Midjourney също може да създава изображения с промпти като „котка с шапка“ или „куче с ирокез“.

![Изображение, генерирано от Midjourney, механичен гълъб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_Източник: Wikipedia, изображение, генерирано от Midjourney_

## Как работят DALL-E и Midjourney

Първо, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E е генеративен AI модел, базиран на архитектурата на трансформър с _авторегресивен трансформър_.

_Авторегресивният трансформър_ определя как моделът генерира изображения от текстови описания – той създава по един пиксел наведнъж и използва вече генерираните пиксели, за да създаде следващия. Процесът преминава през множество слоеве в невронна мрежа, докато изображението е завършено.

С този процес DALL-E контролира атрибути, обекти, характеристики и други в генерираното изображение. Въпреки това, DALL-E 2 и 3 предлагат по-голям контрол върху генерираното изображение.

## Създаване на първото ви приложение за генериране на изображения

Какво е необходимо, за да създадете приложение за генериране на изображения? Трябват ви следните библиотеки:

- **python-dotenv** – силно препоръчително е да използвате тази библиотека, за да съхранявате тайните си в _.env_ файл, отделен от кода.
- **openai** – тази библиотека ще използвате за взаимодействие с OpenAI API.
- **pillow** – за работа с изображения в Python.
- **requests** – за изпращане на HTTP заявки.

1. Създайте файл _.env_ със следното съдържание:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Намерете тази информация в Azure Portal за вашия ресурс в секцията „Keys and Endpoint“.

1. Съберете горните библиотеки в файл с име _requirements.txt_ по следния начин:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. След това създайте виртуална среда и инсталирайте библиотеките:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   За Windows използвайте следните команди за създаване и активиране на виртуалната среда:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Добавете следния код във файл с име _app.py_:

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

Нека обясним този код:

- Първо импортираме необходимите библиотеки, включително OpenAI, dotenv, requests и Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- След това зареждаме променливите на средата от _.env_ файла.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- След това задаваме endpoint, ключ за OpenAI API, версия и тип.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- След това генерираме изображението:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Горният код връща JSON обект, съдържащ URL адреса на генерираното изображение. Можем да използваме този URL, за да изтеглим изображението и да го запишем във файл.

- Накрая отваряме изображението и използваме стандартен преглед на изображения, за да го покажем:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Повече подробности за генерирането на изображението

Нека разгледаме кода за генериране на изображението по-подробно:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** е текстовият промпт, използван за генериране на изображението. В този случай използваме промпта „Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси“.
- **size** е размерът на генерираното изображение. В този случай генерираме изображение с размер 1024x1024 пиксела.
- **n** е броят на генерираните изображения. В този случай генерираме две изображения.
- **temperature** е параметър, който контролира случайността на изхода на генеративния AI модел. Температурата е стойност между 0 и 1, където 0 означава детерминиран изход, а 1 – случаен. По подразбиране е 0.7.

Има още неща, които можете да правите с изображения, които ще разгледаме в следващия раздел.

## Допълнителни възможности при генериране на изображения

Вече видяхте как с няколко реда Python код успяхме да генерираме изображение. Но има още възможности с изображенията.

Можете също така да:

- **Правите редакции**. Като предоставите съществуващо изображение, маска и промпт, можете да променяте изображението. Например, можете да добавите нещо в част от изображението. Представете си нашето зайче – можете да му добавите шапка. Това става като подадете изображението, маска (определяща зоната за промяна) и текстов промпт, описващ какво трябва да се направи.

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

  Основното изображение съдържа само зайчето, но крайното изображение ще има шапка на зайчето.

- **Създавате вариации**. Идеята е да вземете съществуващо изображение и да поискате да се създадат вариации. За да създадете вариация, подавате изображение и текстов промпт и използвате код като този:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Забележка: това се поддържа само в OpenAI

## Температура

Температурата е параметър, който контролира случайността на изхода на генеративен AI модел. Стойността е между 0 и 1, където 0 означава детерминиран изход, а 1 – случаен. По подразбиране е 0.7.

Нека видим пример как работи температурата, като изпълним този промпт два пъти:

> Промпт: "Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси"

![Зайче на кон, държащо близалка, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.bg.png)

Сега нека изпълним същия промпт отново, за да видим, че няма да получим същото изображение два пъти:

![Генерирано изображение на зайче на кон](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.bg.png)

Както виждате, изображенията са сходни, но не еднакви. Нека опитаме да променим стойността на температурата на 0.1 и да видим какво ще се случи:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промяна на температурата

Нека опитаме да направим отговора по-детерминиран. От двете генерирани изображения видяхме, че в първото има зайче, а във второто – кон, така че изображенията се различават значително.

Затова нека променим кода и зададем температурата на 0, както следва:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сега, когато изпълните този код, ще получите тези две изображения:

- ![Температура 0, версия 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.bg.png)
- ![Температура 0, версия 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.bg.png)

Тук ясно се вижда, че изображенията са много по-подобни.

## Как да определите граници за вашето приложение с мета промпти

С нашето демо вече можем да генерираме изображения за нашите клиенти. Въпреки това, трябва да създадем някои граници за приложението.

Например, не искаме да генерираме изображения, които не са подходящи за работна среда или за деца.

Това може да се направи с помощта на _мета промпти_. Мета промптите са текстови промпти, използвани за контролиране на изхода на генеративен AI модел. Например, можем да използваме мета промпти, за да гарантираме, че генерираните изображения са безопасни за работна среда или подходящи за деца.

### Как работи това?

Как работят мета промптите?

Мета промптите са текстови промпти, които се поставят преди основния текстов промпт и служат за контролиране на изхода на модела. Те се вграждат в приложенията, за да управляват резултатите от модела, като обединяват входа на основния промпт и мета промпта в един текстов промпт.

Един пример за мета промпт е следният:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сега нека видим как можем да използваме мета промпти в нашето демо.

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

От горния промпт се вижда как всички генерирани изображения вземат предвид мета промпта.

## Задача – нека дадем възможност на учениците

В началото на урока представихме Edu4All. Сега е време да дадем възможност на учениците да генерират изображения за своите оценки.

Учениците ще създават изображения, съдържащи паметници – кои точно паметници зависи от тях. Те са насърчени да използват креативността си, за да поставят тези паметници в различни контексти.

## Решение

Ето едно възможно решение:

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

## Отлична работа! Продължете обучението си

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си в областта на Генеративния AI!

Преминете към Урок 10, където ще разгледаме как да [създавате AI приложения с нисък код](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.