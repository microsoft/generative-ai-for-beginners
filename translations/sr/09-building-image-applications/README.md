<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T19:36:36+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sr"
}
-->
# Изградња апликација за генерисање слика

[![Изградња апликација за генерисање слика](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-ови нису само за генерисање текста. Могуће је и генерисати слике на основу текстуалних описа. Слике као модалитет могу бити изузетно корисне у разним областима као што су медициска технологија, архитектура, туризам, развој игара и још много тога. У овом поглављу ћемо се упознати са два најпопуларнија модела за генерисање слика, DALL-E и Midjourney.

## Увод

У овој лекцији ћемо обрадити:

- Генерисање слика и зашто је то корисно.
- DALL-E и Midjourney, шта су и како функционишу.
- Како направити апликацију за генерисање слика.

## Циљеви учења

Након завршене лекције, моћи ћете да:

- Направите апликацију за генерисање слика.
- Дефинишете границе за вашу апликацију помоћу метапромптова.
- Радите са DALL-E и Midjourney.

## Зашто правити апликацију за генерисање слика?

Апликације за генерисање слика су одличан начин да истражите могућности генеративне вештачке интелигенције. Могу се користити, на пример, за:

- **Уређивање и синтезу слика**. Можете генерисати слике за разне намене, као што су уређивање и синтеза слика.

- **Примена у различитим индустријама**. Могу се користити за генерисање слика у разним индустријама као што су медтек, туризам, развој игара и друго.

## Сценарио: Edu4All

У оквиру ове лекције настављамо рад са нашим стартапом, Edu4All. Ученици ће креирати слике за своје задатке, а које ће то слике бити зависи од њих самих – могу бити илустрације за њихову бајку, нови лик за причу или помоћ у визуелизацији идеја и концепата.

Ево шта би ученици Edu4All-а могли да направе, на пример, ако на часу раде о споменицима:

![Edu4All стартап, час о споменицима, Ајфелова кула](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sr.png)

користећи промпт као што је

> "Пас поред Ајфелове куле на раном јутарњем сунцу"

## Шта су DALL-E и Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) и [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) су два најпопуларнија модела за генерисање слика, који вам омогућавају да користите промптове за креирање слика.

### DALL-E

Почнимо са DALL-E, који је генеративни AI модел који генерише слике на основу текстуалних описа.

> [DALL-E је комбинација два модела, CLIP и дифузне пажње](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** је модел који генерише ембедингсе, односно нумеричке репрезентације података, из слика и текста.

- **Дифузна пажња** је модел који генерише слике из ембединга. DALL-E је трениран на скупу података слика и текста и може се користити за генерисање слика на основу текстуалних описа. На пример, DALL-E може да направи слику мачке са шеширом или пса са ирокез фризуром.

### Midjourney

Midjourney ради на сличан начин као DALL-E, генерише слике на основу текстуалних промптова. Midjourney се такође може користити за генерисање слика помоћу промптова као што су „мачка са шеширом“ или „пас са ирокез фризуром“.

![Слика коју је генерисао Midjourney, механички голуб](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Извор: Википедија, слику је генерисао Midjourney_

## Како функционишу DALL-E и Midjourney

Прво, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E је генеративни AI модел заснован на трансформер архитектури са _ауторегресивним трансформером_.

_Ауторегресивни трансформер_ одређује како модел генерише слике из текстуалних описа – генерише један по један пиксел, а затим користи већ генерисане пикселе да направи следећи. Овај процес пролази кроз више слојева неуронске мреже, све док слика не буде комплетна.

Овим процесом DALL-E контролише атрибуте, објекте, карактеристике и још много тога на слици коју генерише. Међутим, DALL-E 2 и 3 имају још већу контролу над генерисаном сликом.

## Изградња ваше прве апликације за генерисање слика

Шта је све потребно да направите апликацију за генерисање слика? Потребне су вам следеће библиотеке:

- **python-dotenv** – препоручује се да ову библиотеку користите како бисте чували тајне у _.env_ фајлу, одвојено од кода.
- **openai** – ова библиотека служи за комуникацију са OpenAI API-јем.
- **pillow** – за рад са сликама у Python-у.
- **requests** – за слање HTTP захтева.

## Креирајте и деплоујте Azure OpenAI модел

Ако већ нисте, пратите упутства на [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) страници
да бисте креирали Azure OpenAI ресурс и модел. Изаберите DALL-E 3 као модел.  

## Креирајте апликацију

1. Креирајте фајл _.env_ са следећим садржајем:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Ове податке пронађите у Azure OpenAI Foundry порталу за ваш ресурс у одељку "Deployments".

1. Сакупите наведене библиотеке у фајл _requirements.txt_ овако:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Затим, направите виртуелно окружење и инсталирајте библиотеке:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   За Windows, користите следеће команде за креирање и активацију виртуелног окружења:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Додајте следећи код у фајл _app.py_:

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

Хајде да објаснимо овај код:

- Прво, увозимо потребне библиотеке, укључујући OpenAI библиотеку, dotenv, requests и Pillow.

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

- После тога, конфигуришемо Azure OpenAI сервис клијент 

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

  Овај код враћа JSON објекат који садржи URL генерисане слике. URL можемо искористити да преузмемо слику и сачувамо је у фајл.

- На крају, отварамо слику и приказујемо је у стандардном прегледачу слика:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Детаљније о генерисању слике

Погледајмо детаљније код који генерише слику:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** је текстуални промпт који се користи за генерисање слике. У овом примеру користимо промпт "Зека на коњу, држи лизалицу, на магловитој ливади где расту нарциси".
- **size** је величина слике која се генерише. Овде генеришемо слику од 1024x1024 пиксела.
- **n** је број слика које се генеришу. Овде генеришемо две слике.
- **temperature** је параметар који контролише насумичност излаза генеративног AI модела. Temperature је вредност између 0 и 1, где 0 значи да је излаз детерминистички, а 1 да је насумичан. Подразумевана вредност је 0.7.

Постоји још ствари које можете радити са сликама, о чему ћемо говорити у наредном делу.

## Додатне могућности генерисања слика

Видели сте како смо могли да генеришемо слику са неколико линија кода у Python-у. Међутим, постоје и друге ствари које можете радити са сликама.

Можете, на пример:

- **Уређивати слике**. Ако дате постојећу слику, маску и промпт, можете изменити слику. На пример, можете додати нешто на део слике. Замислите нашу слику зеке – можете додати шешир зеки. То се ради тако што дате слику, маску (која означава део који се мења) и текстуални промпт који описује шта треба урадити. 
> Напомена: ово није подржано у DALL-E 3. 
 
Ево примера са GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Основна слика би садржала само дневну собу са базеном, али коначна слика би имала и фламинга:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Правити варијације**. Идеја је да узмете постојећу слику и затражите да се направе варијације. Да бисте направили варијацију, дате слику и текстуални промпт и код као у примеру:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Напомена: ово је подржано само на OpenAI

## Temperature

Temperature је параметар који контролише насумичност излаза генеративног AI модела. Temperature је вредност између 0 и 1, где 0 значи да је излаз детерминистички, а 1 да је насумичан. Подразумевана вредност је 0.7.

Погледајмо пример како temperature функционише, тако што ћемо покренути овај промпт два пута:

> Промпт: "Зека на коњу, држи лизалицу, на магловитој ливади где расту нарциси"

![Зека на коњу држи лизалицу, верзија 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sr.png)

Сада покренимо исти промпт поново да видимо да нећемо добити исту слику два пута:

![Генерисана слика зеке на коњу](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sr.png)

Као што видите, слике су сличне, али нису исте. Пробајмо да променимо вредност temperature на 0.1 и видимо шта ће се десити:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Промена temperature

Пробајмо да направимо одговор детерминистичкијим. Могли смо да приметимо на претходне две слике да је на првој зека, а на другој коњ, дакле слике се доста разликују.

Зато ћемо променити код и поставити temperature на 0, овако:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Сада, када покренете овај код, добићете ове две слике:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sr.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sr.png)

Овде јасно видите да се слике много више личе.

## Како дефинисати границе за вашу апликацију помоћу метапромптова

Са нашим демом већ можемо да генеришемо слике за клијенте. Међутим, потребно је да поставимо неке границе за апликацију.

На пример, не желимо да генеришемо слике које нису прикладне за радно окружење или нису примерене за децу.

Ово можемо урадити помоћу _метапромптова_. Метапромптови су текстуални промптови који се користе за контролу излаза генеративног AI модела. На пример, можемо користити метапромптове да контролишемо излаз и осигурамо да су генерисане слике безбедне за радно окружење или примерене за децу.

### Како то функционише?

Како функционишу метапромптови?

Метапромптови су текстуални промптови који се користе за контролу излаза генеративног AI модела, постављају се испред главног промпта и користе се за контролу излаза модела, а уграђују се у апликације ради контроле излаза. На тај начин се у један текстуални промпт обједињују унос промпта и метапромпта.

Један пример метапромпта би био следећи:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Сада, да видимо како можемо користити метапромптове у нашем демоу.

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

Из горњег промпта видите како све слике које се креирају узимају у обзир метапромпт.

## Задатак – омогућимо ученицима

На почетку лекције смо представили Edu4All. Сада је време да омогућимо ученицима да генеришу слике за своје задатке.

Ученици ће креирати слике за своје задатке који садрже споменике, а који ће то споменици бити зависи од њих. Од ученика се тражи да буду креативни и поставе те споменике у различите контексте.

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

## Одличан посао! Наставите са учењем
Након што завршите ову лекцију, погледајте нашу [Збирку за учење о генеративној вештачкој интелигенцији](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите са унапређивањем знања о генеративној вештачкој интелигенцији!

Пређите на лекцију 10 где ћемо видети како се [праве AI апликације уз мало програмирања](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.