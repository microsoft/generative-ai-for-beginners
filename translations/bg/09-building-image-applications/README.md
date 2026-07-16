# Създаване на приложения за генериране на изображения

[![Създаване на приложения за генериране на изображения](../../../translated_images/bg/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Голямата езикова модели не са само за генериране на текст. Също така е възможно да се генерират изображения от текстови описания. Използването на изображения като модалност може да бъде изключително полезно в редица области като Медицински технологии, архитектура, туризъм, разработка на игри и други. В тази глава ще разгледаме двата най-популярни модела за генериране на изображения, DALL-E и Midjourney.

## Въведение

В този урок ще разгледаме:

- Генериране на изображения и защо е полезно.
- DALL-E и Midjourney: какво представляват и как работят.
- Как да създадете приложение за генериране на изображения.

## Учебни цели

След завършване на този урок ще можете да:

- Създавате приложение за генериране на изображения.
- Определяте границите за вашето приложение с метаподсказки.
- Работите с DALL-E и Midjourney.

## Защо да създавате приложение за генериране на изображения?

Приложенията за генериране на изображения са чудесен начин да изследвате възможностите на Генеративния AI. Те могат да се използват, например, за:

- **Редактиране и синтез на изображения**. Можете да генерирате изображения за различни случаи на употреба, като редактиране и синтез на изображения.

- **Приложими в различни индустрии**. Те могат да се използват за генериране на изображения за различни индустрии – Медицински технологии, туризъм, разработка на игри и други.

## Сценарий: Edu4All

В рамките на този урок ще продължим да работим с нашия стартъп Edu4All. Учениците ще създават изображения за своите оценки, какви изображения ще бъдат – зависи от тях, но те могат да са илюстрации за собствената им приказка, да създадат нов герой за историята си или да помогнат да визуализират идеите и концепциите си.

Ето какво могат да създадат учениците на Edu4All, ако работят в час по тема паметници:

![Edu4All стартъп, час по паметници, Айфеловата кула](../../../translated_images/bg/startup.94d6b79cc4bb3f5a.webp)

с помощта на подсказка като

> "Куче до Айфеловата кула в ранна сутрешна светлина"

## Какво са DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) са два от най-популярните модели за генериране на изображения, които ви позволяват да използвате подсказки, за да генерирате изображения.

### DALL-E

Нека започнем с DALL-E, което е модел на Генеративен AI, който генерира изображения от текстови описания.

> [DALL-E е комбинация от два модела, CLIP и разпространено внимание](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** е модел, който генерира вграждания – числови представяния на данни от изображения и текст.

- **Разпространено внимание** е модел, който генерира изображения от вграждания. DALL-E е обучен върху набор от данни с изображения и текст и може да бъде използван за генериране на изображения по текстови описания. Например, DALL-E може да генерира изображения на котка с шапка или куче с мохаук.

### Midjourney

Midjourney работи по подобен начин като DALL-E – генерира изображения от текстови подсказки. Midjourney също може да се използва за генериране на изображения с подсказки като „котка с шапка“ или „куче с мохаук“.

![Изображение, генерирано от Midjourney, механичен гълъб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821д-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Източник на изображението: Wikipedia, изображение, генерирано от Midjourney_

## Как работят DALL-E и Midjourney

Първо, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E е модел на Генеративен AI, базиран на архитектурата трансформър с _авторегресивен трансформър_.

_Авторегресивният трансформър_ определя как моделът генерира изображения от текстови описания – той генерира по един пиксел наведнъж и след това използва вече генерираните пиксели, за да създаде следващия. Минава през множество слоеве в невронна мрежа, докато изображението бъде завършено.

С този процес DALL-E контролира атрибути, обекти, характеристики и други в изображението, което генерира. Въпреки това, DALL-E 2 и 3 имат по-голям контрол върху изображението.

## Създаване на първото ви приложение за генериране на изображения

Какво е необходимо, за да създадете приложение за генериране на изображения? Трябват ви следните библиотеки:

- **python-dotenv**, силно препоръчваме да използвате тази библиотека, за да съхранявате вашите тайни в _.env_ файл извън кода.
- **openai**, тази библиотека ще използвате за взаимодействие с OpenAI API.
- **pillow**, за работа с изображения в Python.
- **requests**, за да ви помага с HTTP заявки.

## Създайте и внедрете Azure OpenAI модел

Ако все още не сте го направили, следвайте инструкциите на страницата [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst),
за да създадете ресурс и модел Azure OpenAI. Изберете **gpt-image-1** като модел (текущото поколение Azure OpenAI модел за изображения; DALL-E 3 вече не е достъпен за нови внедрявания).

## Създайте приложението

1. Създайте файл _.env_ със следното съдържание:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Намерете тази информация в портала Azure OpenAI Foundry за вашия ресурс в секцията "Deployments".

1. Съберете горепосочените библиотеки във файл на име _requirements.txt_, както следва:

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

   За Windows използвайте следните команди за създаване и активиране на виртуална среда:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Добавете следния код във файл наречен _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # Конфигуриране на клиента за услугата Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Създаване на изображение с помощта на API за генериране на изображения
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Задаване на директорията за съхранение на изображението
        image_dir = os.path.join(os.curdir, 'images')

        # Ако директорията не съществува, създайте я
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Инициализиране на пътя към изображението (внимавайте файловият тип да е png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Вземане на генерираното изображение
        image_url = generation_response.data[0].url  # Извличане на URL адреса на изображението от отговора
        generated_image = requests.get(image_url).content  # Изтегляне на изображението
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Показване на изображението в стандартния прегледач на изображения
        image = Image.open(image_path)
        image.show()

    # Хващане на изключения
    except openai.BadRequestError as err:
        print(err)
   ```

Нека обясним този код:

- Първо, импортираме нужните библиотеки, включително OpenAI библиотеката, dotenv библиотеката, requests библиотеката и Pillow библиотеката.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- След това зареждаме променливите на околната среда от _.env_ файла.

  ```python
  # внасяне на dotenv
  dotenv.load_dotenv()
  ```

- След това конфигурираме клиента за Azure OpenAI услуга

  ```python
  # Вземете крайната точка и ключа от променливите на околната среда
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- След това генерираме изображението:

  ```python
  # Създайте изображение, използвайки API за генериране на изображения
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Гореописаният код отговаря с JSON обект, съдържащ URL адреса на генерираното изображение. Можем да използваме URL-то, за да изтеглим изображението и да го запазим в файл.

- Накрая отваряме изображението и използваме стандартния преглед на изображения, за да го покажем:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Повече подробности за генериране на изображението

Нека разгледаме кода за генериране на изображението по-подробно:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, е текстовата подсказка, използвана за генериране на изображението. В този случай използваме подсказката "Зайче на кон, държейки близалка, на мъгливо поле, където растат нарциси".
- **size**, е размерът на изображенията, които се генерират. В този случай генерираме изображение с размер 1024x1024 пиксела.
- **n**, е броят на генерираните изображения. В този случай генерираме две изображения.
- **temperature**, е параметър, който контролира случайността на изхода на Генеративен AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. По подразбиране е 0.7.

Има и други възможности с изображенията, които ще разгледаме в следващия раздел.

## Допълнителни възможности за генериране на изображения

Вече видяхте как успяхме да генерираме изображение с няколко реда Python. Въпреки това, има още неща, които можете да направите с изображения.

Можете също така да:

- **Правите редакции**. Като предоставите съществуващо изображение, маска и подсказка, можете да променяте изображението. Например, можете да добавите нещо към определена част от изображението. Представете си нашето изображение с зайчето, можете да му добавите шапка. Как да го направите: предоставяте изображение, маска (идентифицираща частта за промяна) и текстова подсказка, която указва какво трябва да бъде направено.
> Забележка: това не се поддържа в DALL-E 3.
 
Ето пример с използване на GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Основното изображение би съдържало само лаундж зоната с басейна, но крайното изображение би имало фламинго:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/bg/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bg/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bg/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Създавате вариации**. Идеята е да вземете съществуващо изображение и да поискате да се създадат вариации. За да създадете вариация, предоставяте изображение и текстова подсказка и използвате код като следния:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Забележка: това се поддържа само от модела DALL-E 2 на OpenAI, а не от gpt-image-1

## Температура

Температурата е параметър, който контролира случайността на изхода от Генеративен AI модел. Температурата е стойност между 0 и 1, където 0 означава, че изходът е детерминиран, а 1 означава, че изходът е случаен. По подразбиране е 0.7.

Нека разгледаме пример как работи температурата, като изпълним тази подсказка два пъти:

> Подсказка : "Зайче на кон, държейки близалка, на мъгливо поле, където растат нарциси"

![Зайче на кон държейки близалка, версия 1](../../../translated_images/bg/v1-generated-image.a295cfcffa3c13c2.webp)

Сега нека изпълним същата подсказка, за да видим, че няма да получим същото изображение два пъти:

![Генерирано изображение на зайче на кон](../../../translated_images/bg/v2-generated-image.33f55a3714efe61d.webp)

Както виждате, изображенията са подобни, но не са еднакви. Нека опитаме да променим стойността на температурата на 0.1 и да видим какво ще стане:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Въведете текста на вашата подсказка тук
        size='1024x1024',
        n=2
    )
```

### Промяна на температурата

Нека се опитаме да направим отговора по-детерминиран. Може да забележим от двете генерирани изображения, че в първото има зайче, а във второто има кон, така че изображенията варират значително.

Затова нека променим кода и зададем температурата на 0, както следва:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Въведете вашия текст за запитване тук
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сега когато изпълните този код, ще получите тези две изображения:

- ![Температура 0, версия 1](../../../translated_images/bg/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Температура 0, версия 2](../../../translated_images/bg/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Тук ясно се вижда колко повече изображенията си приличат.

## Как да определите границите за вашето приложение с метаподсказки

В нашето демо вече можем да генерираме изображения за нашите клиенти. Въпреки това, трябва да създадем някои граници за нашето приложение.

Например, не искаме да генерираме изображения, които са неподходящи за работно място или неподходящи за деца.

Това може да се направи с _метаподсказки_. Метаподсказките са текстови подсказки, използвани за контролиране на изхода на Генеративен AI модел. Например, можем да използваме метаподсказки, за да контролираме изхода и да осигурим, че генерираните изображения са безопасни за работно място или подходящи за деца.

### Как работи това?

Как точно работят метаподсказките?

Метаподсказките са текстови подсказки, които се използват за контролиране на изхода на Генеративен AI модел. Те се поставят преди основната текстова подсказка и са вградени в приложенията, за да контролират изхода на модела. Те обединяват входа на основната подсказка и метаподсказката в единен текстов вход.

Един пример за метаподсказка е следният:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сега да видим как можем да използваме метаподсказки в нашето демо.

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

# TODO добавете заявка за генериране на изображение
```

От горната подсказка можете да видите как всички създавани изображения отчитат метаподсказката.

## Задание - нека дадем възможност на учениците

Запознахме се с Edu4All в началото на този урок. Сега е време да дадем възможност на учениците да генерират изображения за своите оценки.


Студентите ще създадат изображения за своите оценки, съдържащи паметници, кои точно паметници са оставени на техния избор. От студентите се иска да използват своето въображение в тази задача, за да поставят тези паметници в различни контексти.

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

# Вземете крайна точка и ключ от променливи на околната среда
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
    # Създайте изображение, използвайки API за генериране на изображения
    generation_response = client.images.generate(
        prompt=prompt,    # Въведете вашия текст за заявка тук
        size='1024x1024',
        n=1,
    )
    # Задайте директорията за съхранение на изображението
    image_dir = os.path.join(os.curdir, 'images')

    # Ако директорията не съществува, създайте я
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Инициализирайте пътя на изображението (имайте предвид, че типът на файла трябва да е png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Вземете генерираното изображение
    image_url = generation_response.data[0].url  # извлечете URL на изображението от отговора
    generated_image = requests.get(image_url).content  # изтеглете изображението
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Покажете изображението в стандартния визуализатор на изображения
    image = Image.open(image_path)
    image.show()

# прихващане на изключения
except openai.BadRequestError as err:
    print(err)
```

## Отлична работа! Продължете своето обучение

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си по Генеративен AI!

Отидете на Урок 10, където ще разгледаме как да [създаваме AI приложения с ниско кодиране](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->