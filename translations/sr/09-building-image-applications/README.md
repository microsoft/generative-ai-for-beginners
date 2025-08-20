<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:34:19+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sr"
}
-->
# Прављење апликација за генерисање слика

[![Прављење апликација за генерисање слика](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM модели нису само за генерисање текста. Такође је могуће генерисати слике на основу текстуалних описа. Коришћење слика као модалитета може бити изузетно корисно у бројним областима као што су МедТек, архитектура, туризам, развој игара и друге. У овом поглављу ћемо погледати два најпопуларнија модела за генерисање слика, DALL-E и Midjourney.

## Увод

У овој лекцији ћемо обрадити:

- Генерисање слика и зашто је корисно.
- DALL-E и Midjourney, шта су и како функционишу.
- Како направити апликацију за генерисање слика.

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Направите апликацију за генерисање слика.
- Дефинишете границе за вашу апликацију помоћу мета промптова.
- Радите са DALL-E и Midjourney.

## Зашто правити апликацију за генерисање слика?

Апликације за генерисање слика су одличан начин да истражите могућности генеративне вештачке интелигенције. Могу се користити, на пример, за:

- **Уређивање и синтезу слика**. Можете генерисати слике за разне намене, као што су уређивање и синтеза слика.

- **Примена у различитим индустријама**. Такође се могу користити за генерисање слика у различитим индустријама као што су Медтек, туризам, развој игара и друге.

## Сценарио: Edu4All

Као део ове лекције, наставићемо да радимо са нашим стартапом Edu4All. Студенти ће креирати слике за своје задатке, а које слике ће то бити зависи од њих – могу то бити илустрације за њихову бајку, нови лик за причу или помоћ у визуелизацији идеја и концепата.

Ево шта би студенти Edu4All могли да генеришу, на пример, ако раде у учионици на теми споменика:

![Edu4All стартап, час о споменицима, Ајфелова кула](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sr.png)

користећи промпт као што је

> "Пас поред Ајфелове куле у раним јутарњим зрацима сунца"

## Шта су DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) су два од најпопуларнијих модела за генерисање слика, који вам омогућавају да користите промптове за креирање слика.

### DALL-E

Почнимо са DALL-E, који је генеративни AI модел који генерише слике на основу текстуалних описа.

> [DALL-E је комбинација два модела, CLIP и diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** је модел који генерише уграђене представе (ембеддинге), односно нумеричке репрезентације података, из слика и текста.

- **Diffused attention** је модел који генерише слике из уграђених представи. DALL-E је обучен на скупу података слика и текста и може се користити за генерисање слика на основу текстуалних описа. На пример, DALL-E може генерисати слике мачке са шеширом или пса са мустаћима.

### Midjourney

Midjourney ради слично као DALL-E, генерише слике на основу текстуалних промптова. Midjourney се такође може користити за генерисање слика користећи промптове као што су „мачка са шеширом“ или „пас са мустаћима“.

![Слика генерисана помоћу Midjourney, механички голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Извор слике Википедија, слика генерисана помоћу Midjourney_

## Како функционишу DALL-E и Midjourney

Прво, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E је генеративни AI модел заснован на трансформер архитектури са _ауторегресивним трансформером_.

_Ауторегресивни трансформер_ дефинише како модел генерише слике из текстуалних описа – генерише по један пиксел у једном тренутку, а затим користи већ генерисане пикселе да генерише следећи пиксел. Пролази кроз више слојева у неуронској мрежи док слика није комплетна.

Овим процесом, DALL-E контролише атрибуте, објекте, карактеристике и друге детаље на слици коју генерише. Међутим, DALL-E 2 и 3 пружају још већу контролу над генерисаном сликом.

## Прављење ваше прве апликације за генерисање слика

Шта је потребно да направите апликацију за генерисање слика? Потребне су вам следеће библиотеке:

- **python-dotenv**, препоручује се да користите ову библиотеку да бисте чували своје тајне у _.env_ фајлу, одвојено од кода.
- **openai**, ова библиотека служи за интеракцију са OpenAI API-јем.
- **pillow**, за рад са сликама у Python-у.
- **requests**, за слање HTTP захтева.

1. Направите фајл _.env_ са следећим садржајем:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Ове информације пронађите у Azure порталу за ваш ресурс у одељку „Keys and Endpoint“.

1. Прикупите наведене библиотеке у фајл под називом _requirements.txt_ овако:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Затим направите виртуелно окружење и инсталирајте библиотеке:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   За Windows, користите следеће команде за креирање и активирање виртуелног окружења:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Додајте следећи код у фајл под називом _app.py_:

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

Објаснимо овај код:

- Прво увозимо потребне библиотеке, укључујући OpenAI библиотеку, dotenv, requests и Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Затим учитавамо променљиве окружења из _.env_ фајла.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Након тога, подешавамо endpoint, кључ за OpenAI API, верзију и тип.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Следеће, генеришемо слику:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Код враћа JSON објекат који садржи URL генерисане слике. Можемо користити тај URL да преузмемо слику и сачувамо је у фајл.

- На крају, отварамо слику и користимо стандардни прегледач слика да је прикажемо:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Више детаља о генерисању слике

Погледајмо детаљније код који генерише слику:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** је текстуални промпт који се користи за генерисање слике. У овом случају користимо промпт „Зец на коњу, држи лизалицу, на магловитој ливади где расту нарциси“.
- **size** је величина генерисане слике. У овом случају генеришемо слику величине 1024x1024 пиксела.
- **n** је број слика које се генеришу. У овом случају генеришемо две слике.
- **temperature** је параметар који контролише случајност излаза генеративног AI модела. Температура је вредност између 0 и 1, где 0 значи да је излаз детерминистички, а 1 да је излаз случајан. Подразумевана вредност је 0.7.

Постоје још многе ствари које можете радити са сликама, а које ћемо обрадити у следећем одељку.

## Додатне могућности генерисања слика

Видели сте како смо успели да генеришемо слику уз само неколико редова кода у Python-у. Међутим, постоје и друге могућности са сликама.

Можете такође:

- **Извршити измене**. Пружањем постојеће слике, маске и промпта, можете изменити слику. На пример, можете додати нешто на део слике. Замислите нашу слику зеца, можете додати шешир зецу. То се ради тако што се пружи слика, маска (која означава део за измену) и текстуални промпт који описује шта треба урадити.

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

  Основна слика би садржала само зеца, али коначна слика ће имати шешир на зецу.

- **Креирати варијације**. Идеја је да узмете постојећу слику и затражите да се направе варијације. За креирање варијације, пружите слику и текстуални промпт и код као што је овај:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Напомена, ово је подржано само на OpenAI

## Температура

Температура је параметар који контролише случајност излаза генеративног AI модела. Вредност температуре је између 0 и 1, где 0 значи да је излаз детерминистички, а 1 да је излаз случајан. Подразумевана вредност је 0.7.

Погледајмо пример како температура функционише, тако што ћемо покренути овај промпт два пута:

> Промпт: "Зец на коњу, држи лизалицу, на магловитој ливади где расту нарциси"

![Зец на коњу држи лизалицу, верзија 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sr.png)

Сада покренимо исти промпт поново да видимо да нећемо добити исту слику два пута:

![Генерисана слика зеца на коњу](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sr.png)

Као што видите, слике су сличне, али нису идентичне. Покушајмо да променимо вредност температуре на 0.1 и видимо шта ће се десити:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промена температуре

Покушајмо да учинимо одговор више детерминистичким. Из две генерисане слике видели смо да је на првој слици зец, а на другој коњ, па се слике значајно разликују.

Зато ћемо променити код и поставити температуру на 0, овако:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Када покренете овај код, добићете ове две слике:

- ![Температура 0, в1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sr.png)
- ![Температура 0, в2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sr.png)

Овде јасно видите да слике више личе једна на другу.

## Како дефинисати границе за вашу апликацију помоћу метапромптова

У нашем демо примеру већ можемо генерисати слике за наше клијенте. Међутим, потребно је да поставимо неке границе за нашу апликацију.

На пример, не желимо да генеришемо слике које нису безбедне за радно место или које нису прикладне за децу.

То можемо урадити помоћу _метапромптова_. Метапромптови су текстуални промптови који се користе за контролу излаза генеративног AI модела. На пример, можемо користити метапромптове да контролишемо излаз и осигурамо да генерисане слике буду безбедне за радно место или прикладне за децу.

### Како то функционише?

Како метапромптови раде?

Метапромптови су текстуални промптови који се користе за контролу излаза генеративног AI модела, они се постављају пре главног текстуалног промпта и користе се за контролу излаза модела. Уграђују се у апликације како би контролисали излаз модела. На тај начин се у један текстуални промпт обухватају и улазни промпт и метапромпт.

Један пример метапромпта био би следећи:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сада, погледајмо како можемо користити метапромптове у нашем демо примеру.

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

Из горе наведеног промпта видите како све генерисане слике узимају у обзир метапромпт.

## Задатак – омогућимо студентима

Увели смо Edu4All на почетку ове лекције. Сада је време да омогућимо студентима да генеришу слике за своје задатке.

Студенти ће креирати слике за своје задатке које садрже споменике, а који споменици ће то бити зависи од студената. Студенти су позвани да користе своју креативност и поставе ове споменике у различите контексте.

## Решење

Ево једног могућег решења:

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

## Одличан рад! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [колекцију за учење генеративне вештачке интелигенције](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) и наставите да унапређујете своје знање о генеративном AI!

Прелазимо на Лекцију 10 где ћемо погледати како да [правите AI апликације са мало кода](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.