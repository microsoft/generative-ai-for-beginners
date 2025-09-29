<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:53:11+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hu"
}
-->
# Képgeneráló alkalmazások építése

[![Képgeneráló alkalmazások építése](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hu.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Az LLM-ek nem csak szöveg generálására alkalmasak. Szöveges leírások alapján képek is létrehozhatók. A képek mint modalitás számos területen hasznosak lehetnek, például az orvostechnológia, az építészet, a turizmus, a játékfejlesztés és még sok más terület esetében. Ebben a fejezetben a két legnépszerűbb képgeneráló modellt, a DALL-E-t és a Midjourney-t vizsgáljuk meg.

## Bevezetés

Ebben a leckében az alábbiakat tárgyaljuk:

- Képgenerálás és annak hasznossága.
- DALL-E és Midjourney: mik ezek, és hogyan működnek.
- Hogyan építhetsz képgeneráló alkalmazást.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Képgeneráló alkalmazást építeni.
- Meghatározni az alkalmazás határait meta promptokkal.
- Dolgozni a DALL-E és Midjourney modellekkel.

## Miért érdemes képgeneráló alkalmazást építeni?

A képgeneráló alkalmazások remek lehetőséget kínálnak a generatív mesterséges intelligencia képességeinek felfedezésére. Például az alábbiakra használhatók:

- **Képszerkesztés és szintézis**. Különféle felhasználási esetekhez generálhatsz képeket, például képszerkesztéshez és képszintézishez.

- **Számos iparágban alkalmazható**. Képek generálására is használhatók különféle iparágakban, mint például az orvostechnológia, turizmus, játékfejlesztés és más területek.

## Szenárió: Edu4All

A lecke részeként továbbra is az Edu4All startupunkkal dolgozunk. A diákok képeket készítenek a feladataikhoz, hogy pontosan milyen képeket, az a diákokon múlik. Lehetnek például illusztrációk saját meséjükhöz, új karakterek létrehozása a történetükhöz, vagy ötleteik és koncepcióik vizualizálása.

Íme, mit generálhatnak az Edu4All diákjai például, ha az osztályban műemlékekkel dolgoznak:

![Edu4All startup, osztály a műemlékekről, Eiffel-torony](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hu.png)

egy ilyen prompt segítségével:

> "Kutya az Eiffel-torony mellett kora reggeli napsütésben"

## Mi az a DALL-E és Midjourney?

A [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) és a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) a két legnépszerűbb képgeneráló modell, amelyek lehetővé teszik, hogy promptok segítségével képeket generálj.

### DALL-E

Kezdjük a DALL-E-vel, amely egy generatív mesterséges intelligencia modell, amely szöveges leírásokból képeket generál.

> [A DALL-E két modell, a CLIP és a diffúz figyelem kombinációja](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, egy modell, amely beágyazásokat generál, amelyek az adatok numerikus reprezentációi, képekből és szövegekből.

- **Diffúz figyelem**, egy modell, amely beágyazásokból képeket generál. A DALL-E-t képek és szövegek adatállományán tanították, és szöveges leírásokból képek generálására használható. Például a DALL-E képes generálni egy kalapos macska vagy egy mohawk frizurás kutya képét.

### Midjourney

A Midjourney hasonló módon működik, mint a DALL-E, szöveges promptokból generál képeket. A Midjourney szintén használható képek generálására olyan promptokkal, mint például „egy kalapos macska” vagy „egy mohawk frizurás kutya”.

![Midjourney által generált kép, mechanikus galamb](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kép forrása: Wikipedia, Midjourney által generált kép_

## Hogyan működik a DALL-E és a Midjourney?

Először is, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). A DALL-E egy generatív mesterséges intelligencia modell, amely a transzformer architektúrán alapul, egy _autoregresszív transzformerrel_.

Az _autoregresszív transzformer_ meghatározza, hogyan generál egy modell képeket szöveges leírásokból: egy pixelt generál egyszerre, majd a generált pixeleket használja a következő pixel generálásához. Több rétegen keresztül halad egy neurális hálózatban, amíg a kép elkészül.

Ezzel a folyamattal a DALL-E szabályozza a generált kép attribútumait, objektumait, jellemzőit és egyebeket. Azonban a DALL-E 2 és 3 nagyobb kontrollt biztosít a generált kép felett.

## Az első képgeneráló alkalmazásod építése

Mit igényel egy képgeneráló alkalmazás építése? Az alábbi könyvtárakra van szükséged:

- **python-dotenv**, erősen ajánlott ezt a könyvtárat használni, hogy a titkos adataidat egy _.env_ fájlban tartsd távol a kódtól.
- **openai**, ezt a könyvtárat használod az OpenAI API-val való interakcióhoz.
- **pillow**, képek kezeléséhez Pythonban.
- **requests**, HTTP kérések küldéséhez.

## Azure OpenAI modell létrehozása és telepítése

Ha még nem tetted meg, kövesd az utasításokat a [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) oldalon, hogy létrehozz egy Azure OpenAI erőforrást és modellt. Válaszd a DALL-E 3 modellt.

## Az alkalmazás létrehozása

1. Hozz létre egy _.env_ fájlt az alábbi tartalommal:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Ezt az információt az Azure OpenAI Foundry Portálon találod meg az erőforrásod "Deployments" szekciójában.

1. Gyűjtsd össze a fenti könyvtárakat egy _requirements.txt_ nevű fájlban, így:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ezután hozz létre egy virtuális környezetet, és telepítsd a könyvtárakat:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows esetén használd az alábbi parancsokat a virtuális környezet létrehozásához és aktiválásához:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Add hozzá az alábbi kódot egy _app.py_ nevű fájlba:

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

- Utána konfiguráljuk az Azure OpenAI szolgáltatás kliensét.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Ezután generáljuk a képet:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  A fenti kód egy JSON objektummal válaszol, amely tartalmazza a generált kép URL-jét. Az URL-t használhatjuk a kép letöltésére és fájlba mentésére.

- Végül megnyitjuk a képet, és a standard képnézegetővel megjelenítjük:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### A kép generálásának részletei

Nézzük meg részletesebben a képgeneráló kódot:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, a szöveges prompt, amelyet a kép generálásához használunk. Ebben az esetben a prompt: "Nyúl lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek".
- **size**, a generált kép mérete. Ebben az esetben 1024x1024 pixeles képet generálunk.
- **n**, a generált képek száma. Ebben az esetben két képet generálunk.
- **temperature**, egy paraméter, amely a generatív mesterséges intelligencia modell kimenetének véletlenszerűségét szabályozza. A hőmérséklet értéke 0 és 1 között van, ahol 0 azt jelenti, hogy a kimenet determinisztikus, és 1 azt jelenti, hogy a kimenet véletlenszerű. Az alapértelmezett érték 0,7.

További dolgokat is tehetsz a képekkel, amelyeket a következő szekcióban tárgyalunk.

## A képgenerálás további képességei

Eddig láthattad, hogyan tudtunk néhány sor Python kóddal képet generálni. Azonban további dolgokat is tehetsz a képekkel.

Ezeket is megteheted:

- **Szerkesztés végrehajtása**. Egy meglévő kép, egy maszk és egy prompt megadásával módosíthatod a képet. Például hozzáadhatsz valamit egy kép egy részéhez. Képzeld el a nyúl képünket, hozzáadhatsz egy kalapot a nyúlhoz. Ezt úgy teheted meg, hogy megadod a képet, egy maszkot (amely azonosítja a változtatás területét), és egy szöveges promptot, amely leírja, mit kell tenni.
> Megjegyzés: ez nem támogatott a DALL-E 3-ban.

Íme egy példa a GPT Image használatával:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Az alap kép csak a medencés lounge-t tartalmazná, de a végső kép egy flamingót is tartalmazna:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.hu.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.hu.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.hu.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Variációk létrehozása**. Az ötlet az, hogy egy meglévő képet veszel, és variációkat kérsz róla. A variáció létrehozásához megadod a képet és egy szöveges promptot, valamint ilyen kódot:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Megjegyzés: ez csak az OpenAI-nál támogatott.

## Hőmérséklet

A hőmérséklet egy paraméter, amely a generatív mesterséges intelligencia modell kimenetének véletlenszerűségét szabályozza. A hőmérséklet értéke 0 és 1 között van, ahol 0 azt jelenti, hogy a kimenet determinisztikus, és 1 azt jelenti, hogy a kimenet véletlenszerű. Az alapértelmezett érték 0,7.

Nézzünk egy példát arra, hogyan működik a hőmérséklet, ha kétszer futtatjuk ezt a promptot:

> Prompt: "Nyúl lovon, nyalókát tartva, ködös réten, ahol nárciszok nőnek"

![Nyúl lovon, nyalókát tartva, verzió 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hu.png)

Most futtassuk ugyanazt a promptot, hogy lássuk, nem kapunk kétszer ugyanazt a képet:

![Generált kép nyúl lovon](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hu.png)

Ahogy látható, a képek hasonlóak, de nem azonosak. Próbáljuk meg megváltoztatni a hőmérséklet értékét 0,1-re, és nézzük meg, mi történik:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### A hőmérséklet megváltoztatása

Próbáljuk meg a választ determinisztikusabbá tenni. Az első két generált képből megfigyelhettük, hogy az első képen van egy nyúl, a másodikon pedig egy ló, tehát a képek jelentősen eltérnek.

Ezért változtassuk meg a kódunkat, és állítsuk a hőmérsékletet 0-ra, így:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Most, amikor futtatod ezt a kódot, ezeket a képeket kapod:

- ![Hőmérséklet 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hu.png)
- ![Hőmérséklet 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hu.png)

Itt egyértelműen látható, hogy a képek jobban hasonlítanak egymásra.

## Hogyan határozzuk meg az alkalmazás határait meta promptokkal?

A demónkkal már képeket tudunk generálni az ügyfeleink számára. Azonban szükségünk van arra, hogy bizonyos határokat állítsunk az alkalmazásunk számára.

Például nem szeretnénk olyan képeket generálni, amelyek nem biztonságosak munkahelyi környezetben, vagy nem megfelelőek gyermekek számára.

Ezt _meta promptokkal_ tehetjük meg. A meta promptok olyan szöveges promptok, amelyeket a generatív mesterséges intelligencia modell kimenetének szabályozására használunk. Például meta promptokkal szabályozhatjuk a kimenetet, és biztosíthatjuk, hogy a generált képek biztonságosak legyenek munkahelyi környezetben, vagy megfelelőek legyenek gyermekek számára.

### Hogyan működik?

Hogyan működnek a meta promptok?

A meta promptok olyan szöveges promptok, amelyeket a generatív mesterséges intelligencia modell kimenetének szabályozására használnak. Ezek a szöveges prompt előtt helyezkednek el, és a modell kimenetének szabályozására szolgálnak, beágyazva az alkalmazásokba, hogy szabályozzák a modell kimenetét. A prompt bemenetet és a meta prompt bemenetet egyetlen szöveges promptba foglalják.

Egy meta prompt példája lehet a következő:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Most nézzük meg, hogyan használhatjuk a meta promptokat a demónkban.

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

A fenti promptból látható, hogy minden létrehozott kép figyelembe veszi a meta promptot.

## Feladat - segítsük a diákokat

A lecke elején bemutattuk az Edu4All-t. Most itt az ideje, hogy lehetőséget adjunk a diákoknak, hogy képeket generáljanak a feladataikhoz.

A diákok képeket készítenek a feladataikhoz, amelyek műemlékeket tartalmaznak, pontosan milyen műemlékeket, az a diákokon múlik. A diákokat arra kérjük, hogy használják kreativitásukat ebben a feladatban, és helyezzék ezeket a műemlékeket különböző kontextusokba.

## Megoldás

Íme egy lehetséges megoldás:
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

## Nagyszerű munka! Folytasd a tanulást

Miután befejezted ezt a leckét, nézd meg a [Generatív AI tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszthesd a generatív AI-val kapcsolatos tudásodat!

Lépj tovább a 10. leckére, ahol azt vizsgáljuk meg, hogyan lehet [AI alkalmazásokat építeni alacsony kódú megoldásokkal](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.