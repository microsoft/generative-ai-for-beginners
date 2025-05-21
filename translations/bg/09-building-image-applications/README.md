<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:24:30+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bg"
}
-->
# Създаване на приложения за генериране на изображения

[![Създаване на приложения за генериране на изображения](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.bg.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Генерирането на текст не е единственото, което може да се постигне с LLMs. Възможно е също така да се генерират изображения от текстови описания. Изображенията като модалност могат да бъдат изключително полезни в различни области като MedTech, архитектура, туризъм, разработка на игри и други. В тази глава ще разгледаме двата най-популярни модела за генериране на изображения, DALL-E и Midjourney.

## Въведение

В този урок ще разгледаме:

- Генериране на изображения и защо е полезно.
- DALL-E и Midjourney, какво представляват и как работят.
- Как да създадете приложение за генериране на изображения.

## Цели на обучението

След завършване на този урок ще можете да:

- Създадете приложение за генериране на изображения.
- Определите граници за вашето приложение с метапромпти.
- Работите с DALL-E и Midjourney.

## Защо да създадете приложение за генериране на изображения?

Приложенията за генериране на изображения са чудесен начин да изследвате възможностите на Генеративния AI. Те могат да се използват за, например:

- **Редактиране и синтез на изображения**. Можете да генерирате изображения за различни случаи на употреба, като редактиране и синтез на изображения.

- **Приложение в различни индустрии**. Те също така могат да се използват за генериране на изображения за различни индустрии като MedTech, Туризъм, Разработка на игри и други.

## Сценарий: Edu4All

Като част от този урок ще продължим да работим с нашия стартъп, Edu4All. Учениците ще създават изображения за своите оценки, като точно какви изображения зависи от тях, но те биха могли да бъдат илюстрации за собствена приказка или да създадат нов герой за своята история или да им помогнат да визуализират своите идеи и концепции.

Ето какво биха могли да генерират учениците на Edu4All, ако работят в клас върху паметници:

![Стартъп Edu4All, клас върху паметници, Айфелова кула](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.bg.png)

използвайки промпт като

> "Куче до Айфеловата кула в ранна утринна светлина"

## Какво представляват DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) са два от най-популярните модели за генериране на изображения, които ви позволяват да използвате промпти за генериране на изображения.

### DALL-E

Нека започнем с DALL-E, който е генеративен AI модел, генериращ изображения от текстови описания.

> [DALL-E е комбинация от два модела, CLIP и дифузно внимание](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, е модел, който генерира вграждания, които са числови представяния на данни, от изображения и текст.

- **Дифузно внимание**, е модел, който генерира изображения от вграждания. DALL-E е обучен върху набор от данни от изображения и текст и може да се използва за генериране на изображения от текстови описания. Например, DALL-E може да се използва за генериране на изображения на котка с шапка или куче с мохак.

### Midjourney

Midjourney работи по подобен начин на DALL-E, генерира изображения от текстови промпти. Midjourney също може да се използва за генериране на изображения с промпти като „котка с шапка“ или „куче с мохак“.

![Изображение, генерирано от Midjourney, механичен гълъб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Изображение от Wikipedia, генерирано от Midjourney_

## Как работят DALL-E и Midjourney

Първо, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E е генеративен AI модел, базиран на трансформаторната архитектура с _авторегресивен трансформатор_.

_Авторегресивен трансформатор_ определя как модел генерира изображения от текстови описания, генерира по един пиксел наведнъж и след това използва генерираните пиксели, за да генерира следващия пиксел. Преминавайки през множество слоеве в невронна мрежа, докато изображението бъде завършено.

С този процес DALL-E контролира атрибути, обекти, характеристики и други в изображението, което генерира. Въпреки това, DALL-E 2 и 3 имат повече контрол върху генерираното изображение.

## Създаване на първото ви приложение за генериране на изображения

Какво е необходимо, за да създадете приложение за генериране на изображения? Нуждаете се от следните библиотеки:

- **python-dotenv**, препоръчително е да използвате тази библиотека, за да пазите вашите тайни в _.env_ файл, далеч от кода.
- **openai**, тази библиотека ще използвате за взаимодействие с OpenAI API.
- **pillow**, за работа с изображения в Python.
- **requests**, за да ви помогне да правите HTTP заявки.

1. Създайте файл _.env_ със следното съдържание:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Намерете тази информация в Azure Portal за вашия ресурс в секцията "Ключове и крайна точка".

1. Съберете горепосочените библиотеки в файл, наречен _requirements.txt_ по следния начин:

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

   За Windows използвайте следните команди, за да създадете и активирате вашата виртуална среда:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Добавете следния код във файл, наречен _app.py_:

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

- Първо, импортираме библиотеките, които ни трябват, включително библиотеката OpenAI, библиотеката dotenv, библиотеката requests и библиотеката Pillow.

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

- След това задаваме крайна точка, ключ за OpenAI API, версия и тип.

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

  Горният код отговаря с JSON обект, който съдържа URL на генерираното изображение. Можем да използваме URL, за да изтеглим изображението и да го запазим във файл.

- Накрая, отваряме изображението и използваме стандартния преглед на изображения, за да го покажем:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Повече детайли за генерирането на изображението

Нека разгледаме кода, който генерира изображението по-подробно:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, е текстовият промпт, който се използва за генериране на изображението. В този случай използваме промпт "Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси".
- **size**, е размерът на генерираното изображение. В този случай генерираме изображение с размер 1024x1024 пиксела.
- **n**, е броят на генерираните изображения. В този случай генерираме две изображения.
- **temperature**, е параметър, който контролира случайността на изхода на генеративния AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. Стойността по подразбиране е 0.7.

Има още неща, които можете да правите с изображения, които ще разгледаме в следващата секция.

## Допълнителни възможности на генерирането на изображения

Досега видяхте как успяхме да генерираме изображение с няколко реда в Python. Въпреки това, има още неща, които можете да правите с изображения.

Можете също така да направите следното:

- **Извършване на редакции**. Като предоставите съществуващо изображение, маска и промпт, можете да промените изображение. Например, можете да добавите нещо към част от изображение. Представете си нашето изображение със зайче, можете да добавите шапка на зайчето. Как ще го направите е като предоставите изображението, маска (идентифицираща частта от зоната за промяна) и текстов промпт, който да каже какво трябва да се направи.

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

  Основното изображение ще съдържа само зайчето, но крайното изображение ще има шапка на зайчето.

- **Създаване на вариации**. Идеята е, че взимате съществуващо изображение и искате да се създадат вариации. За да създадете вариация, предоставяте изображение и текстов промпт и код по следния начин:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Забележка, това се поддържа само от OpenAI

## Температура

Температурата е параметър, който контролира случайността на изхода на генеративния AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. Стойността по подразбиране е 0.7.

Нека разгледаме пример за това как работи температурата, като изпълним този промпт два пъти:

> Промпт : "Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси"

![Зайче на кон, държащо близалка, версия 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.bg.png)

Сега нека изпълним същия промпт, за да видим, че няма да получим същото изображение два пъти:

![Генерирано изображение на зайче на кон](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.bg.png)

Както виждате, изображенията са сходни, но не са същите. Нека опитаме да променим стойността на температурата на 0.1 и да видим какво ще се случи:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промяна на температурата

Нека опитаме да направим отговора по-детерминиран. Можем да наблюдаваме от двете изображения, които генерирахме, че в първото изображение има зайче, а във второто изображение има кон, така че изображенията се различават значително.

Затова нека променим кода си и зададем температурата на 0, по следния начин:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сега, когато изпълните този код, ще получите тези две изображения:

- ![Температура 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.bg.png)
- ![Температура 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.bg.png)

Тук ясно можете да видите как изображенията си приличат повече.

## Как да определите граници за вашето приложение с метапромпти

С нашето демо вече можем да генерираме изображения за нашите клиенти. Въпреки това, трябва да създадем някои граници за нашето приложение.

Например, не искаме да генерираме изображения, които не са безопасни за работа или които не са подходящи за деца.

Можем да направим това с _метапромпти_. Метапромптите са текстови промпти, които се използват за контролиране на изхода на генеративния AI модел. Например, можем да използваме метапромпти, за да контролираме изхода и да гарантираме, че генерираните изображения са безопасни за работа или подходящи за деца.

### Как работи?

Сега, как работят метапромптите?

Метапромптите са текстови промпти, които се използват за контролиране на изхода на генеративния AI модел, те са поставени преди текстовия промпт и се използват за контролиране на изхода на модела и са вградени в приложенията, за да контролират изхода на модела. Те обединяват входа на промпта и входа на метапромпта в един текстов промпт.

Един пример за метапромпт би бил следният:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сега, нека видим как можем да използваме метапромпти в нашето демо.

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

От горния промпт можете да видите как всички създадени изображения взимат предвид метапромпта.

## Задача - нека дадем възможност на учениците

Представихме Edu4All в началото на този урок. Сега е време да дадем възможност на учениците да генерират изображения за своите оценки.

Учениците ще създават изображения за своите оценки, съдържащи паметници, като точно какви паметници зависи от тях. Учениците са помолени да използват своята креативност в тази задача, за да поставят тези паметници в различни контексти.

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

## Отлична работа! Продължете своето обучение

След завършване на този урок, разгледайте нашата [Генеративна AI колекция за обучение](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да усъвършенствате своите знания по Генеративен AI!

Насочете се към Урок 10, където ще разгледаме как да [създавате AI приложения с нисък код](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Отказ от отговорност**: 
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Докато се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.