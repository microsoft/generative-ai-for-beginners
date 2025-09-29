<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T22:17:41+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bg"
}
-->
# Създаване на приложения за генериране на изображения

[![Създаване на приложения за генериране на изображения](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.bg.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Генеративните езикови модели (LLM) не се ограничават само до генериране на текст. Възможно е също така да се генерират изображения от текстови описания. Наличието на изображения като модалност може да бъде изключително полезно в редица области като медицински технологии, архитектура, туризъм, разработка на игри и други. В тази глава ще разгледаме двата най-популярни модела за генериране на изображения – DALL-E и Midjourney.

## Въведение

В този урок ще разгледаме:

- Генериране на изображения и защо е полезно.
- DALL-E и Midjourney – какво представляват и как работят.
- Как да създадете приложение за генериране на изображения.

## Цели на обучението

След завършване на този урок ще можете:

- Да създадете приложение за генериране на изображения.
- Да дефинирате граници за вашето приложение с помощта на мета промптове.
- Да работите с DALL-E и Midjourney.

## Защо да създадем приложение за генериране на изображения?

Приложенията за генериране на изображения са чудесен начин да изследвате възможностите на Генеративния AI. Те могат да се използват например за:

- **Редактиране и синтез на изображения**. Можете да генерирате изображения за различни случаи на употреба, като редактиране и синтез на изображения.

- **Приложение в различни индустрии**. Те могат да се използват за генериране на изображения за различни индустрии като медицински технологии, туризъм, разработка на игри и други.

## Сценарий: Edu4All

Като част от този урок ще продължим да работим с нашия стартъп Edu4All. Учениците ще създават изображения за своите задачи – какви точно изображения зависи от тях, но те могат да бъдат илюстрации за собствена приказка, нов герой за тяхната история или визуализация на идеи и концепции.

Ето какво биха могли да генерират учениците на Edu4All, ако работят в клас върху паметници:

![Стартъп Edu4All, клас за паметници, Айфеловата кула](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.bg.png)

с помощта на промпт като:

> "Куче до Айфеловата кула в ранна утринна светлина"

## Какво представляват DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) са два от най-популярните модели за генериране на изображения, които позволяват използването на промптове за създаване на изображения.

### DALL-E

Да започнем с DALL-E, който е генеративен AI модел, създаващ изображения от текстови описания.

> [DALL-E е комбинация от два модела – CLIP и дифузно внимание](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** е модел, който генерира ембединг (числови представяния на данни) от изображения и текст.

- **Дифузно внимание** е модел, който генерира изображения от ембединг. DALL-E е обучен върху набор от данни с изображения и текст и може да се използва за създаване на изображения от текстови описания. Например, DALL-E може да се използва за генериране на изображения на котка с шапка или куче с ирокез.

### Midjourney

Midjourney работи по подобен начин на DALL-E – генерира изображения от текстови промптове. Midjourney също може да се използва за създаване на изображения с промптове като „котка с шапка“ или „куче с ирокез“.

![Изображение, генерирано от Midjourney, механичен гълъб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Кредит: Wikipedia, изображение, генерирано от Midjourney_

## Как работят DALL-E и Midjourney

Първо, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E е генеративен AI модел, базиран на трансформаторна архитектура с _авторегресивен трансформатор_.

_Авторегресивен трансформатор_ определя как моделът генерира изображения от текстови описания – генерира един пиксел наведнъж и след това използва генерираните пиксели, за да създаде следващия пиксел. Процесът преминава през множество слоеве в невронна мрежа, докато изображението бъде завършено.

С този процес DALL-E контролира атрибути, обекти, характеристики и други елементи в генерираното изображение. Въпреки това, DALL-E 2 и 3 предоставят повече контрол върху генерираното изображение.

## Създаване на първото приложение за генериране на изображения

Какво е необходимо за създаване на приложение за генериране на изображения? Трябват ви следните библиотеки:

- **python-dotenv** – препоръчително е да използвате тази библиотека, за да съхранявате тайните си в _.env_ файл, далеч от кода.
- **openai** – тази библиотека се използва за взаимодействие с OpenAI API.
- **pillow** – за работа с изображения в Python.
- **requests** – за улесняване на HTTP заявки.

## Създаване и разгръщане на модел в Azure OpenAI

Ако все още не сте го направили, следвайте инструкциите на страницата [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), за да създадете ресурс и модел в Azure OpenAI. Изберете DALL-E 3 като модел.

## Създаване на приложението

1. Създайте файл _.env_ със следното съдържание:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Намерете тази информация в Azure OpenAI Foundry Portal за вашия ресурс в секцията „Deployments“.

1. Съберете горепосочените библиотеки в файл, наречен _requirements.txt_, по следния начин:

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

   За Windows използвайте следните команди, за да създадете и активирате виртуалната си среда:

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

Обяснение на кода:

- Първо, импортираме необходимите библиотеки, включително OpenAI библиотеката, dotenv библиотеката, requests библиотеката и Pillow библиотеката.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- След това зареждаме променливите на средата от файла _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- След това конфигурираме клиента за Azure OpenAI услуга.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- След това генерираме изображението:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Горният код връща JSON обект, който съдържа URL на генерираното изображение. Можем да използваме URL, за да изтеглим изображението и да го запазим във файл.

- Накрая отваряме изображението и използваме стандартния зрител на изображения, за да го покажем:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Повече подробности за генерирането на изображението

Нека разгледаме кода за генериране на изображението по-подробно:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** е текстовият промпт, който се използва за генериране на изображението. В този случай използваме промпт „Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси“.
- **size** е размерът на генерираното изображение. В този случай генерираме изображение с размер 1024x1024 пиксела.
- **n** е броят на генерираните изображения. В този случай генерираме две изображения.
- **temperature** е параметър, който контролира случайността на изхода на генеративния AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. Стойността по подразбиране е 0.7.

Има още неща, които можете да правите с изображения, които ще разгледаме в следващия раздел.

## Допълнителни възможности за генериране на изображения

Досега видяхте как успяхме да генерираме изображение с няколко реда код в Python. Въпреки това има още неща, които можете да правите с изображения.

Можете също така да:

- **Извършвате редакции**. Като предоставите съществуващо изображение, маска и промпт, можете да промените изображение. Например, можете да добавите нещо към част от изображението. Представете си нашето изображение със зайчето – можете да добавите шапка на зайчето. Това се прави, като предоставите изображението, маска (идентифицираща частта от областта за промяна) и текстов промпт, който описва какво трябва да се направи.
> Забележка: това не се поддържа в DALL-E 3.

Ето пример с GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Основното изображение би съдържало само салона с басейна, но крайното изображение би имало фламинго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.bg.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.bg.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.bg.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Създавате вариации**. Идеята е да вземете съществуващо изображение и да поискате да се създадат вариации. За да създадете вариация, предоставяте изображение и текстов промпт и код като този:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Забележка: това се поддържа само в OpenAI.

## Температура

Температурата е параметър, който контролира случайността на изхода на генеративния AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. Стойността по подразбиране е 0.7.

Нека разгледаме пример за това как работи температурата, като изпълним този промпт два пъти:

> Промпт: „Зайче на кон, държащо близалка, на мъглива поляна, където растат нарциси“

![Зайче на кон, държащо близалка, версия 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.bg.png)

Сега нека изпълним същия промпт, за да видим, че няма да получим едно и също изображение два пъти:

![Генерирано изображение на зайче на кон](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.bg.png)

Както виждате, изображенията са подобни, но не идентични. Нека опитаме да променим стойността на температурата на 0.1 и да видим какво ще се случи:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промяна на температурата

Нека опитаме да направим отговора по-детерминиран. Можем да наблюдаваме от двете генерирани изображения, че в първото изображение има зайче, а във второто изображение има кон, така че изображенията се различават значително.

Затова нека променим кода си и зададем температурата на 0, както следва:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сега, когато изпълните този код, ще получите тези две изображения:

- ![Температура 0, версия 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.bg.png)
- ![Температура 0, версия 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.bg.png)

Тук ясно се вижда как изображенията си приличат повече.

## Как да дефинирате граници за вашето приложение с мета промптове

С нашата демонстрация вече можем да генерираме изображения за нашите клиенти. Въпреки това трябва да създадем някои граници за нашето приложение.

Например, не искаме да генерираме изображения, които не са подходящи за работа или които не са подходящи за деца.

Можем да направим това с _мета промптове_. Мета промптовете са текстови промптове, които се използват за контролиране на изхода на генеративния AI модел. Например, можем да използваме мета промптове, за да контролираме изхода и да гарантираме, че генерираните изображения са подходящи за работа или за деца.

### Как работи?

Как работят мета промптовете?

Мета промптовете са текстови промптове, които се използват за контролиране на изхода на генеративния AI модел. Те се позиционират преди текстовия промпт и се използват за контролиране на изхода на модела, като се вграждат в приложенията за контролиране на изхода на модела. Те обединяват входа на промпта и входа на мета промпта в един текстов промпт.

Един пример за мета промпт би бил следният:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сега нека видим как можем да използваме мета промптове в нашата демонстрация.

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

От горния промпт можете да видите как всички създадени изображения вземат предвид мета промпта.

## Задача – да дадем възможност на учениците

В началото на този урок представихме Edu4All. Сега е време да дадем възможност на учениците да генерират изображения за своите задачи.

Учениците ще създават изображения за своите задачи, съдържащи паметници – какви точно паметници зависи от тях. Учениците са помолени да използват своята креативност в тази задача, за да поставят тези паметници в различни контексти.

## Решение

Ето едно възможно решение:
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

## Страхотна работа! Продължете да учите

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си за Генеративен AI!

Преминете към Урок 10, където ще разгледаме как да [създаваме AI приложения с нисък код](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.