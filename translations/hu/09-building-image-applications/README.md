<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:21:05+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hu"
}
-->
# Képgeneráló alkalmazások építése

[![Képgeneráló alkalmazások építése](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.hu.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Az LLM-ek nem csak szöveggenerálásra alkalmasak. Szöveges leírásokból képeket is lehet generálni. A képek mint modalitás rendkívül hasznosak lehetnek számos területen, mint például MedTech, építészet, turizmus, játékfejlesztés és sok más. Ebben a fejezetben a két legnépszerűbb képgeneráló modell, a DALL-E és a Midjourney kerül bemutatásra.

## Bevezetés

Ebben a leckében az alábbi témákat fogjuk áttekinteni:

- Képgenerálás és miért hasznos.
- DALL-E és Midjourney, mik ezek és hogyan működnek.
- Hogyan építenél képgeneráló alkalmazást.

## Tanulási célok

A lecke befejezése után képes leszel:

- Képgeneráló alkalmazást építeni.
- Meghatározni az alkalmazásod határait meta promptokkal.
- Dolgozni a DALL-E és Midjourney modellekkel.

## Miért építsünk képgeneráló alkalmazást?

A képgeneráló alkalmazások nagyszerű módot kínálnak a Generatív AI képességeinek felfedezésére. Használhatók például:

- **Képszerkesztés és szintézis**. Különböző felhasználási esetekhez generálhatsz képeket, mint például képszerkesztés és képszintézis.

- **Különböző iparágakban alkalmazható**. Különböző iparágak számára is generálhatnak képeket, mint például Medtech, turizmus, játékfejlesztés és még sok más.

## Forgatókönyv: Edu4All

Ebben a leckében folytatjuk munkánkat az Edu4All startupunkkal. A diákok képeket készítenek a felméréseikhez, hogy pontosan milyen képeket, az a diákok döntése, de lehetnek például illusztrációk a saját meséjükhöz, új karaktert alkothatnak a történetükhöz, vagy segíthetnek nekik elképzelni az ötleteiket és koncepcióikat.

Például, ha az Edu4All diákjai az osztályban a műemlékekkel dolgoznak, a következőket generálhatják:

![Edu4All startup, osztály a műemlékekről, Eiffel-torony](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.hu.png)

egy ilyen prompt használatával:

> "Kutya az Eiffel-torony mellett kora reggeli napsütésben"

## Mi a DALL-E és Midjourney?

A [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) és a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) a két legnépszerűbb képgeneráló modell, amelyek lehetővé teszik, hogy promptok segítségével képeket generálj.

### DALL-E

Kezdjük a DALL-E-vel, amely egy Generatív AI modell, ami képeket generál szöveges leírások alapján.

> [A DALL-E két modell kombinációja, a CLIP és a diffúz figyelem](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, egy modell, amely embeddingeket generál, amelyek a képek és szövegek numerikus ábrázolásai.

- **Diffúz figyelem**, egy modell, amely képeket generál az embeddingekből. A DALL-E egy képek és szövegek adathalmazán van betanítva, és használható képek generálására szöveges leírások alapján. Például a DALL-E képeket tud generálni egy kalapos macskáról vagy egy punk frizurás kutyáról.

### Midjourney

A Midjourney hasonló módon működik, mint a DALL-E, szöveges promptokból generál képeket. A Midjourney is használható képek generálására olyan promptokkal, mint "macska kalapban" vagy "kutya punk frizurával".

![A Midjourney által generált kép, mechanikus galamb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kép forrása Wikipedia, Midjourney által generált kép_

## Hogyan működik a DALL-E és Midjourney

Először is, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). A DALL-E egy Generatív AI modell, amely a transformer architektúrára épül, egy _autoregresszív transformerrel_.

Az _autoregresszív transformer_ meghatározza, hogyan generál egy modell képeket szöveges leírásokból, egy pixelt generál egyszerre, majd a generált pixeleket használja a következő pixel generálásához. Több rétegen keresztül halad át egy neurális hálózatban, amíg a kép elkészül.

Ezzel a folyamattal a DALL-E kontrollálja a képekben generált attribútumokat, objektumokat, jellemzőket és még sok mást. Azonban a DALL-E 2 és 3 több kontrollt biztosít a generált képek felett.

## Az első képgeneráló alkalmazás építése

Tehát mit igényel egy képgeneráló alkalmazás építése? Az alábbi könyvtárakra van szükséged:

- **python-dotenv**, erősen ajánlott ezt a könyvtárat használni a titkok tárolására egy _.env_ fájlban, távol a kódtól.
- **openai**, ezt a könyvtárat használod az OpenAI API-val való interakcióhoz.
- **pillow**, képekkel való munkához Pythonban.
- **requests**, HTTP kérések küldéséhez.

1. Hozz létre egy _.env_ fájlt az alábbi tartalommal:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Keresse meg ezt az információt az Azure Portálon a forrásod "Kulcsok és végpontok" szekciójában.

1. Gyűjtsd össze a fenti könyvtárakat egy _requirements.txt_ nevű fájlban, így:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ezután hozz létre virtuális környezetet és telepítsd a könyvtárakat:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows esetén használja a következő parancsokat a virtuális környezet létrehozásához és aktiválásához:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Add hozzá a következő kódot egy _app.py_ nevű fájlhoz:

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

Magyarázzuk el ezt a kódot:

- Először importáljuk a szükséges könyvtárakat, beleértve az OpenAI könyvtárat, a dotenv könyvtárat, a requests könyvtárat és a Pillow könyvtárat.

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

- Utána beállítjuk az OpenAI API végpontját, kulcsát, verzióját és típusát.

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

  A fenti kód egy JSON objektummal válaszol, amely tartalmazza a generált kép URL-jét. Az URL-t használhatjuk a kép letöltésére és fájlba mentésére.

- Végül megnyitjuk a képet és a szokásos képnézőt használjuk a megjelenítéséhez:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### További részletek a kép generálásáról

Nézzük meg részletesebben a kép generálásához használt kódot:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, az a szöveges prompt, amelyet a kép generálásához használunk. Ebben az esetben a "Nyuszi lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek" promptot használjuk.
- **size**, a generált kép mérete. Ebben az esetben 1024x1024 pixel méretű képet generálunk.
- **n**, a generált képek száma. Ebben az esetben két képet generálunk.
- **temperature**, egy paraméter, amely a Generatív AI modell kimenetének véletlenszerűségét szabályozza. A hőmérséklet 0 és 1 közötti érték, ahol 0 azt jelenti, hogy a kimenet determinisztikus, és 1 azt jelenti, hogy a kimenet véletlenszerű. Az alapértelmezett érték 0,7.

További dolgokat is tehetsz a képekkel, amit a következő szekcióban fogunk tárgyalni.

## A képgenerálás további képességei

Láttad, hogy néhány sor Python kóddal képesek voltunk képet generálni. Azonban még több dolgot tehetsz a képekkel.

Ezen kívül a következőket is teheted:

- **Változtatások végrehajtása**. Egy meglévő kép, egy maszk és egy prompt megadásával megváltoztathatsz egy képet. Például hozzáadhatsz valamit a kép egy részéhez. Képzeld el a nyuszi képünket, hozzáadhatsz egy kalapot a nyuszihoz. Ezt úgy teheted meg, hogy megadod a képet, egy maszkot (azonosítva a változtatás területét) és egy szöveges promptot, hogy mit kell tenni.

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

  Az alap kép csak a nyuszit tartalmazná, de a végleges kép a kalapot is tartalmazná a nyuszin.

- **Variációk létrehozása**. Az ötlet az, hogy egy meglévő képet veszel, és kérsz, hogy variációk készüljenek. A variáció létrehozásához megadod a képet és egy szöveges promptot, és a kódot így:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Megjegyzés, ez csak az OpenAI-n támogatott

## Hőmérséklet

A hőmérséklet egy paraméter, amely a Generatív AI modell kimenetének véletlenszerűségét szabályozza. A hőmérséklet 0 és 1 közötti érték, ahol 0 azt jelenti, hogy a kimenet determinisztikus, és 1 azt jelenti, hogy a kimenet véletlenszerű. Az alapértelmezett érték 0,7.

Nézzünk meg egy példát arra, hogyan működik a hőmérséklet, futtassuk ezt a promptot kétszer:

> Prompt : "Nyuszi lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek"

![Nyuszi lovon, nyalókát tartva, verzió 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.hu.png)

Most futtassuk ugyanazt a promptot, csak hogy lássuk, nem kapjuk meg kétszer ugyanazt a képet:

![Generált kép nyusziról lovon](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.hu.png)

Ahogy látható, a képek hasonlóak, de nem azonosak. Próbáljuk meg a hőmérséklet értékét 0,1-re változtatni, és nézzük meg, mi történik:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### A hőmérséklet változtatása

Próbáljuk meg a választ inkább determinisztikussá tenni. Megfigyelhettük a két generált képből, hogy az első képen van egy nyuszi, a második képen pedig egy ló, tehát a képek jelentősen eltérnek.

Ezért változtassuk meg a kódunkat, és állítsuk a hőmérsékletet 0-ra, így:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Most, amikor futtatod ezt a kódot, ezeket a képeket kapod:

- ![Hőmérséklet 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.hu.png)
- ![Hőmérséklet 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.hu.png)

Itt egyértelműen láthatod, hogy a képek jobban hasonlítanak egymásra.

## Hogyan határozzuk meg az alkalmazás határait metapromptokkal

A demónkkal már képeket tudunk generálni az ügyfeleink számára. Azonban néhány határt kell létrehoznunk az alkalmazásunk számára.

Például nem akarunk olyan képeket generálni, amelyek nem megfelelőek a munkahelyen, vagy nem megfelelőek gyerekek számára.

Ezt _metapromptokkal_ tehetjük meg. A metapromptok szöveges promptok, amelyeket a Generatív AI modell kimenetének szabályozására használnak. Például metapromptokat használhatunk a kimenet szabályozására, és biztosíthatjuk, hogy a generált képek megfelelőek legyenek a munkahelyen, vagy megfelelőek legyenek gyerekek számára.

### Hogyan működik?

Most, hogyan működnek a metapromptok?

A metapromptok szöveges promptok, amelyeket a Generatív AI modell kimenetének szabályozására használnak, a szöveges prompt előtt helyezkednek el, és a modell kimenetének szabályozására használják, beágyazva az alkalmazásokba a modell kimenetének szabályozására. A prompt input és a metaprompt input egyetlen szöveges promptban történő kapszulázása.

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

A fenti promptból láthatod, hogy minden létrehozott kép figyelembe veszi a metapromptot.

## Feladat - engedélyezzük a diákokat

Az Edu4All-t a lecke elején mutattuk be. Most itt az ideje, hogy engedélyezzük a diákokat, hogy képeket generáljanak a felméréseikhez.

A diákok képeket készítenek a felméréseikhez, amelyek műemlékeket tartalmaznak, pontosan milyen műemlékeket, az a diákok döntése. A diákok felkérést kapnak, hogy használják kreativitásukat ebben a feladatban, hogy ezeket a műemlékeket különböző kontextusokba helyezzék.

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

## Nagyszerű munka! Folytasd a tanulást

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI tudásodat!

Lépj tovább a 10. leckére, ahol megnézzük, hogyan építhetünk AI alkalmazásokat alacsony kóddal](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.