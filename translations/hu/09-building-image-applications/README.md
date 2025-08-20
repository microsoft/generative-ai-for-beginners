<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:31:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hu"
}
-->
# Képgeneráló alkalmazások fejlesztése

[![Képgeneráló alkalmazások fejlesztése](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hu.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

A nagy nyelvi modellek (LLM-ek) nem csak szöveg generálására képesek. Lehetőség van arra is, hogy szöveges leírásokból képeket hozzunk létre. A képek, mint egy új modalitás, számos területen nagyon hasznosak lehetnek, például az orvostechnológiában, építészetben, turizmusban, játékfejlesztésben és még sok másban. Ebben a fejezetben a két legnépszerűbb képgeneráló modellt, a DALL-E-t és a Midjourney-t fogjuk megvizsgálni.

## Bevezetés

Ebben a leckében a következőkről lesz szó:

- A képgenerálásról és annak hasznosságáról.
- A DALL-E-ről és a Midjourney-ről, hogy mik ezek és hogyan működnek.
- Hogyan építhetsz képgeneráló alkalmazást.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Képgeneráló alkalmazást fejleszteni.
- Meta promptok segítségével meghatározni az alkalmazásod határait.
- Dolgozni a DALL-E-vel és a Midjourney-vel.

## Miért érdemes képgeneráló alkalmazást fejleszteni?

A képgeneráló alkalmazások remek lehetőséget kínálnak a generatív mesterséges intelligencia képességeinek felfedezésére. Használhatók például:

- **Kép szerkesztésére és szintézisére**. Különféle felhasználási esetekhez generálhatsz képeket, például képszerkesztéshez vagy képszintézishez.

- **Számos iparágban alkalmazhatók**. Képek generálására használhatók többek között az orvostechnológia, turizmus, játékfejlesztés és más területeken.

## Forgatókönyv: Edu4All

A lecke során tovább dolgozunk az Edu4All nevű startupunkkal. A diákok képeket készítenek a feladataikhoz; hogy pontosan milyen képeket, az a diákokon múlik, lehetnek például illusztrációk saját meséjükhöz, új karakterek a történetükhöz, vagy segíthetnek elképzeléseik és koncepcióik vizualizálásában.

Például, ha az Edu4All diákjai az osztályban emlékművekkel foglalkoznak, ilyen képeket generálhatnak:

![Edu4All startup, osztály emlékművekkel, Eiffel-torony](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hu.png)

egy ilyen prompttal:

> "Kutya az Eiffel-torony mellett a kora reggeli napsütésben"

## Mi az a DALL-E és a Midjourney?

A [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) és a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) a legnépszerűbb képgeneráló modellek közé tartoznak, amelyek promptok segítségével képeket hoznak létre.

### DALL-E

Kezdjük a DALL-E-vel, amely egy generatív mesterséges intelligencia modell, és szöveges leírásokból képeket generál.

> [A DALL-E két modell, a CLIP és a diffúz figyelem kombinációja](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** egy olyan modell, amely képekből és szövegekből numerikus reprezentációkat, ún. beágyazásokat (embeddingeket) generál.

- **Diffúz figyelem** egy olyan modell, amely a beágyazásokból képeket generál. A DALL-E-t képek és szövegek adatbázisán tanították, és képes szöveges leírások alapján képeket létrehozni. Például képes képet generálni egy kalapos macskáról vagy egy mohawk frizurás kutyáról.

### Midjourney

A Midjourney hasonlóan működik, mint a DALL-E, szöveges promptokból generál képeket. A Midjourney-vel is létrehozhatsz képeket olyan promptok alapján, mint például „kalapos macska” vagy „mohawk frizurás kutya”.

![Midjourney által generált kép, mechanikus galamb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kép forrása: Wikipedia, Midjourney által generált kép_

## Hogyan működik a DALL-E és a Midjourney?

Először a [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). A DALL-E egy generatív mesterséges intelligencia modell, amely a transformer architektúrán alapul, és egy _autoregresszív transformer_.

Az _autoregresszív transformer_ meghatározza, hogyan generál a modell képeket szöveges leírásokból: egyszerre egy pixelt hoz létre, majd a már generált pixelek alapján generálja a következőt. Több rétegen halad át egy neurális hálózatban, amíg a kép elkészül.

Ezzel a folyamattal a DALL-E képes irányítani a kép attribútumait, tárgyait, jellemzőit és még sok mást. A DALL-E 2 és 3 verziók ennél még nagyobb kontrollt biztosítanak a generált kép felett.

## Első képgeneráló alkalmazásod elkészítése

Mire van szükség egy képgeneráló alkalmazás elkészítéséhez? A következő könyvtárakra:

- **python-dotenv**, erősen ajánlott ennek a könyvtárnak a használata, hogy a titkaidat egy _.env_ fájlban tárold, távol a kódtól.
- **openai**, ezzel a könyvtárral kommunikálsz az OpenAI API-val.
- **pillow**, képek kezeléséhez Pythonban.
- **requests**, HTTP kérésekhez.

1. Hozz létre egy _.env_ fájlt a következő tartalommal:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Ezt az információt az Azure Portálon találod meg az erőforrásod „Kulcsok és végpont” szekciójában.

1. Gyűjtsd össze a fenti könyvtárakat egy _requirements.txt_ fájlba így:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ezután hozd létre a virtuális környezetet és telepítsd a könyvtárakat:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows alatt a következő parancsokkal hozhatod létre és aktiválhatod a virtuális környezetet:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Add hozzá a következő kódot egy _app.py_ nevű fájlba:

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

Magyarázzuk meg ezt a kódot:

- Először importáljuk a szükséges könyvtárakat, beleértve az OpenAI könyvtárat, a dotenv-et, a requests-et és a Pillow-t.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Ezután betöltjük a környezeti változókat a _.env_ fájlból.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Majd beállítjuk az OpenAI API végpontját, kulcsát, verzióját és típusát.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Ezután generáljuk a képet:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  A fenti kód egy JSON objektummal válaszol, amely tartalmazza a generált kép URL-jét. Ezt az URL-t használhatjuk a kép letöltésére és fájlba mentésére.

- Végül megnyitjuk a képet és az alapértelmezett képnézegetővel megjelenítjük:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Részletesebben a kép generálásáról

Nézzük meg részletesebben a képgeneráló kódot:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**: a szöveges utasítás, amely alapján a kép generálódik. Ebben az esetben a prompt: „Nyúl lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek”.
- **size**: a generált kép mérete. Itt 1024x1024 pixeles képet generálunk.
- **n**: a generált képek száma. Ebben az esetben két képet generálunk.
- **temperature**: egy paraméter, amely a generált kimenet véletlenszerűségét szabályozza. Az értéke 0 és 1 között van, ahol 0 determinisztikus (ugyanazt az eredményt adja), 1 pedig teljesen véletlenszerű. Az alapértelmezett érték 0,7.

A képekkel még sok más dolgot is megtehetsz, amiről a következő szakaszban lesz szó.

## A képgenerálás további lehetőségei

Eddig láttad, hogyan tudtunk néhány sor Python kóddal képet generálni. De ennél többre is képes vagy.

Továbbá a következőket is megteheted:

- **Szerkesztések végrehajtása**. Ha megadsz egy meglévő képet, egy maszkkal és egy prompttal, módosíthatod a képet. Például hozzáadhatsz valamit a kép egy részéhez. Képzeld el a nyulas képet, hozzáadhatsz a nyúlhoz egy kalapot. Ehhez meg kell adnod a képet, egy maszkot (ami megjelöli a módosítandó területet) és egy szöveges utasítást, hogy mit kell csinálni.

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

  Az alap kép csak a nyulat tartalmazná, de a végső képen már kalap is lesz a nyúlon.

- **Variációk létrehozása**. Az ötlet az, hogy egy meglévő képből kérsz variációkat. Ehhez megadsz egy képet és egy szöveges promptot, majd a következő kódot használod:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Megjegyzés: ez csak az OpenAI-nál támogatott.

## Temperature (hőmérséklet)

A temperature egy paraméter, amely a generatív modell kimenetének véletlenszerűségét szabályozza. Az értéke 0 és 1 között van, ahol 0 determinisztikus, 1 pedig teljesen véletlenszerű. Az alapértelmezett érték 0,7.

Nézzünk egy példát a temperature működésére, futtassuk le kétszer ezt a promptot:

> Prompt: "Nyúl lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek"

![Nyúl lovon, nyalókát tartva, 1. verzió](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hu.png)

Most futtassuk le ugyanazt a promptot még egyszer, hogy lássuk, nem kapunk ugyanazt a képet kétszer:

![Nyúl lovon generált kép](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hu.png)

Ahogy látható, a képek hasonlóak, de nem azonosak. Próbáljuk meg a temperature értékét 0,1-re állítani, és nézzük meg, mi történik:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### A temperature megváltoztatása

Próbáljuk meg a választ determinisztikusabbá tenni. A két generált képből látható, hogy az első képen nyúl van, a másodikon ló, tehát a képek jelentősen eltérnek.

Ezért módosítsuk a kódot, és állítsuk a temperature értékét 0-ra, így:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ha most lefuttatod ezt a kódot, a következő két képet kapod:

- ![Temperature 0, 1. verzió](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hu.png)
- ![Temperature 0, 2. verzió](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hu.png)

Itt jól látható, hogy a képek sokkal jobban hasonlítanak egymásra.

## Hogyan határozd meg az alkalmazásod határait metapromptokkal?

A demónkkal már képesek vagyunk képeket generálni az ügyfeleinknek. Ugyanakkor szükség van arra, hogy bizonyos határokat szabjunk az alkalmazásnak.

Például nem szeretnénk olyan képeket generálni, amelyek nem munkahelyi környezetbe valók, vagy nem megfelelőek gyerekek számára.

Ezt _metapromptokkal_ érhetjük el. A metapromptok olyan szöveges utasítások, amelyekkel szabályozhatjuk a generatív modell kimenetét. Például metapromptokkal biztosíthatjuk, hogy a generált képek munkahelybarátok legyenek, vagy gyerekek számára megfelelőek.

### Hogyan működik?

Hogyan működnek a metapromptok?

A metapromptok olyan szöveges utasítások, amelyek a generatív modell kimenetének szabályozására szolgálnak. Ezek a prompt előtt helyezkednek el, és beágyazódnak az alkalmazásokba, hogy kontrollálják a modell kimenetét. Egyetlen szöveges promptként kezelik a metaprompt és a felhasználói prompt együttesét.

Egy példa metaprompt lehet a következő:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Most nézzük meg, hogyan használhatjuk a metapromptokat a demónkban.

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

A fenti promptból látható, hogy az összes generált kép figyelembe veszi a metapromptot.

## Feladat – engedélyezzük a diákoknak a képgenerálást

Az elején bemutattuk az Edu4All-t. Most itt az ideje, hogy a diákok is képeket generálhassanak a feladataikhoz.

A diákok képeket készítenek az emlékművekről szóló feladataikhoz, hogy pontosan milyen emlékműveket, az a diákokon múlik. Arra kérjük őket, hogy kreativitásukat használva helyezzék ezeket az emlékműveket különböző kontextusokba.

## Megoldás

Íme egy lehetséges megoldás:

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

## Szép munka! Folytasd a tanulást

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív AI ismereteidet!

Lépj tovább a 10. leckére, ahol azt nézzük meg, hogyan [építhetsz AI alkalmazásokat low-code eszközökkel](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.