<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:56:55+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sr"
}
-->
# Изградња апликација за генерисање слика

[![Изградња апликација за генерисање слика](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Генеративни језички модели (LLM) нису ограничени само на генерисање текста. Могуће је генерисати и слике на основу текстуалних описа. Имање слика као модалитета може бити веома корисно у бројним областима као што су медицинска технологија, архитектура, туризам, развој игара и друге. У овом поглављу ћемо се фокусирати на два најпопуларнија модела за генерисање слика, DALL-E и Midjourney.

## Увод

У овој лекцији ћемо обрадити:

- Генерисање слика и зашто је корисно.
- DALL-E и Midjourney, шта су и како функционишу.
- Како изградити апликацију за генерисање слика.

## Циљеви учења

Након завршетка ове лекције, бићете у могућности да:

- Изградите апликацију за генерисање слика.
- Дефинишете границе за вашу апликацију помоћу мета промптова.
- Радите са DALL-E и Midjourney.

## Зашто изградити апликацију за генерисање слика?

Апликације за генерисање слика су одличан начин за истраживање могућности генеративне вештачке интелигенције. Могу се користити, на пример:

- **Уређивање и синтеза слика**. Можете генерисати слике за различите намене, као што су уређивање и синтеза слика.

- **Примена у различитим индустријама**. Такође се могу користити за генерисање слика у различитим индустријама као што су медицинска технологија, туризам, развој игара и друге.

## Сценарио: Edu4All

У оквиру ове лекције настављамо рад са нашим стартапом, Edu4All. Студенти ће креирати слике за своје задатке. Које слике ће креирати зависи од њих, али могу бити илустрације за њихову бајку, креирање новог лика за њихову причу или помоћ у визуализацији њихових идеја и концепата.

Ево шта би студенти Edu4All-а могли да генеришу, на пример, ако раде у учионици на теми споменика:

![Edu4All стартап, учионица о споменицима, Ајфелова кула](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sr.png)

користећи промпт као:

> "Пас поред Ајфелове куле у јутарњем сунцу"

## Шта су DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) су два најпопуларнија модела за генерисање слика који омогућавају коришћење промптова за генерисање слика.

### DALL-E

Почнимо са DALL-E, генеративним AI моделом који генерише слике на основу текстуалних описа.

> [DALL-E је комбинација два модела, CLIP и дифузне пажње](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** је модел који генерише ембединг, нумеричке репрезентације података, из слика и текста.

- **Дифузна пажња** је модел који генерише слике из ембединга. DALL-E је обучен на скупу података слика и текста и може се користити за генерисање слика на основу текстуалних описа. На пример, DALL-E може генерисати слике мачке са шеширом или пса са ирокезом.

### Midjourney

Midjourney функционише на сличан начин као DALL-E, генерише слике на основу текстуалних промптова. Midjourney се такође може користити за генерисање слика користећи промптове као што су „мачка са шеширом“ или „пас са ирокезом“.

![Слика генерисана помоћу Midjourney, механички голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Извор слике: Википедија, слика генерисана помоћу Midjourney_

## Како функционишу DALL-E и Midjourney

Прво, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E је генеративни AI модел заснован на архитектури трансформера са _ауторегресивним трансформером_.

_Ауторегресивни трансформер_ дефинише како модел генерише слике на основу текстуалних описа, генерише један пиксел по пиксел, а затим користи генерисане пикселе за генерисање следећег пиксела. Процес пролази кроз више слојева у неуронској мрежи док слика не буде комплетна.

Овим процесом, DALL-E контролише атрибуте, објекте, карактеристике и више у слици коју генерише. Међутим, DALL-E 2 и 3 имају већу контролу над генерисаном сликом.

## Изградња ваше прве апликације за генерисање слика

Шта је потребно за изградњу апликације за генерисање слика? Потребне су вам следеће библиотеке:

- **python-dotenv**, препоручује се коришћење ове библиотеке за чување ваших тајни у _.env_ датотеци далеко од кода.
- **openai**, библиотека коју ћете користити за интеракцију са OpenAI API-јем.
- **pillow**, за рад са сликама у Python-у.
- **requests**, за помоћ у прављењу HTTP захтева.

## Креирање и постављање Azure OpenAI модела

Ако то већ нисте урадили, пратите упутства на [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) страници
да креирате Azure OpenAI ресурс и модел. Изаберите DALL-E 3 као модел.  

## Креирање апликације

1. Креирајте датотеку _.env_ са следећим садржајем:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Пронађите ову информацију у Azure OpenAI Foundry порталу за ваш ресурс у одељку "Deployments".

1. Сакупите горе наведене библиотеке у датотеци _requirements.txt_ овако:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Затим, креирајте виртуелно окружење и инсталирајте библиотеке:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   За Windows, користите следеће команде за креирање и активирање вашег виртуелног окружења:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Додајте следећи код у датотеку названу _app.py_:

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

Објаснимо овај код:

- Прво, увозимо библиотеке које су нам потребне, укључујући OpenAI библиотеку, dotenv библиотеку, requests библиотеку и Pillow библиотеку.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Затим учитавамо променљиве окружења из _.env_ датотеке.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Након тога, конфигуришемо Azure OpenAI сервис клијент.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Затим генеришемо слику:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Горњи код одговара JSON објектом који садржи URL генерисане слике. Можемо користити URL за преузимање слике и чување у датотеци.

- На крају, отварамо слику и користимо стандардни прегледач слика за њено приказивање:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Више детаља о генерисању слике

Погледајмо код који генерише слику детаљније:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, је текстуални промпт који се користи за генерисање слике. У овом случају, користимо промпт "Зец на коњу, држи лизалицу, на магловитој ливади где расту нарциси".
- **size**, је величина генерисане слике. У овом случају, генеришемо слику величине 1024x1024 пиксела.
- **n**, је број генерисаних слика. У овом случају, генеришемо две слике.
- **temperature**, је параметар који контролише случајност излаза генеративног AI модела. Температура је вредност између 0 и 1 где 0 значи да је излаз детерминистички, а 1 значи да је излаз случајан. Подразумевана вредност је 0.7.

Постоје још ствари које можете радити са сликама, које ћемо обрадити у следећем одељку.

## Додатне могућности генерисања слика

До сада сте видели како смо успели да генеришемо слику користећи неколико линија кода у Python-у. Међутим, постоје још ствари које можете радити са сликама.

Такође можете урадити следеће:

- **Извршити измене**. Пружањем постојеће слике, маске и промпта, можете изменити слику. На пример, можете додати нешто на део слике. Замислите нашу слику са зецом, можете додати шешир зецу. Како бисте то урадили је пружањем слике, маске (која идентификује део области за промену) и текстуалног промпта који каже шта треба урадити. 
> Напомена: ово није подржано у DALL-E 3. 
 
Ево примера коришћењем GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Основна слика би садржавала само салон са базеном, али коначна слика би имала фламинга:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.sr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.sr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.sr.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Креирати варијације**. Идеја је да узмете постојећу слику и затражите да се креирају варијације. Да бисте креирали варијацију, пружате слику и текстуални промпт и код овако:

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

Температура је параметар који контролише случајност излаза генеративног AI модела. Температура је вредност између 0 и 1 где 0 значи да је излаз детерминистички, а 1 значи да је излаз случајан. Подразумевана вредност је 0.7.

Погледајмо пример како температура функционише, покретањем овог промпта два пута:

> Промпт: "Зец на коњу, држи лизалицу, на магловитој ливади где расту нарциси"

![Зец на коњу држи лизалицу, верзија 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sr.png)

Сада покренимо исти промпт поново да видимо да нећемо добити исту слику два пута:

![Генерисана слика зеца на коњу](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sr.png)

Као што видите, слике су сличне, али нису исте. Покушајмо да променимо вредност температуре на 0.1 и видимо шта ће се десити:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промена температуре

Покушајмо да учинимо одговор детерминистичкијим. Могли смо да приметимо из две генерисане слике да на првој слици постоји зец, а на другој коњ, тако да се слике значајно разликују.

Зато променимо наш код и поставимо температуру на 0, овако:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сада када покренете овај код, добијате ове две слике:

- ![Температура 0, верзија 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sr.png)
- ![Температура 0, верзија 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sr.png)

Овде јасно можете видети како се слике више личе једна на другу.

## Како дефинисати границе за вашу апликацију помоћу мета промптова

Са нашим демоом, већ можемо генерисати слике за наше клијенте. Међутим, потребно је да креирамо неке границе за нашу апликацију.

На пример, не желимо да генеришемо слике које нису прикладне за радно окружење или које нису прикладне за децу.

Ово можемо урадити помоћу _мета промптова_. Мета промптови су текстуални промптови који се користе за контролу излаза генеративног AI модела. На пример, можемо користити мета промптове за контролу излаза и осигурати да генерисане слике буду прикладне за радно окружење или за децу.

### Како функционише?

Како функционишу мета промптови?

Мета промптови су текстуални промптови који се користе за контролу излаза генеративног AI модела, позиционирани су пре текстуалног промпта и користе се за контролу излаза модела, уграђени у апликације за контролу излаза модела. Инкапсулирајући улаз промпта и улаз мета промпта у један текстуални промпт.

Један пример мета промпта био би следећи:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сада, погледајмо како можемо користити мета промптове у нашем демоу.

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

Из горњег промпта можете видети како све генерисане слике узимају у обзир мета промпт.

## Задатак - омогућимо студентима

На почетку ове лекције представили смо Edu4All. Сада је време да омогућимо студентима да генеришу слике за своје задатке.

Студенти ће креирати слике за своје задатке који садрже споменике, тачно који споменици ће бити изабрани зависи од студената. Од студената се тражи да користе своју креативност у овом задатку и поставе те споменике у различите контексте.

## Решење

Ево једног могућег решења:
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

## Одличан рад! Наставите са учењем

Након што завршите ову лекцију, погледајте нашу [колекцију за учење о генеративној вештачкој интелигенцији](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) како бисте наставили да унапређујете своје знање о генеративној вештачкој интелигенцији!

Прелазите на лекцију 10 где ћемо истражити како да [правите апликације засноване на вештачкој интелигенцији уз помоћ low-code алата](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.