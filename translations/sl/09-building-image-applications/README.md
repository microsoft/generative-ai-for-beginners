<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:39:04+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sl"
}
-->
# Gradnja aplikacij za generiranje slik

[![Gradnja aplikacij za generiranje slik](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-ji niso namenjeni le generiranju besedil. Možno je tudi generirati slike iz besedilnih opisov. Imati slike kot modaliteto je lahko zelo koristno na številnih področjih, kot so MedTech, arhitektura, turizem, razvoj iger in še več. V tem poglavju bomo pogledali dva najbolj priljubljena modela za generiranje slik, DALL-E in Midjourney.

## Uvod

V tej lekciji bomo obravnavali:

- Generiranje slik in zakaj je koristno.
- DALL-E in Midjourney, kaj sta in kako delujeta.
- Kako bi zgradili aplikacijo za generiranje slik.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Zgradili aplikacijo za generiranje slik.
- Določili meje za vašo aplikacijo z meta pozivi.
- Delali z DALL-E in Midjourney.

## Zakaj zgraditi aplikacijo za generiranje slik?

Aplikacije za generiranje slik so odličen način za raziskovanje zmožnosti generativne umetne inteligence. Uporabljajo se lahko na primer za:

- **Urejanje in sinteza slik**. Lahko generirate slike za različne primere uporabe, kot sta urejanje slik in sinteza slik.

- **Uporaba v različnih industrijah**. Lahko se uporabljajo tudi za generiranje slik za različne industrije, kot so MedTech, turizem, razvoj iger in še več.

## Scenarij: Edu4All

V okviru te lekcije bomo nadaljevali z delom z našim startupom, Edu4All. Študentje bodo ustvarjali slike za svoje ocene, točno katere slike bodo ustvarili je odvisno od njih, lahko pa bi bile to ilustracije za njihovo pravljico ali ustvarjanje novega lika za njihovo zgodbo ali pa jim pomagajo vizualizirati njihove ideje in koncepte.

Tukaj je primer, kaj bi lahko študentje Edu4All ustvarili, če delajo v razredu na spomenikih:

![Startup Edu4All, razred o spomenikih, Eifflov stolp](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sl.png)

z uporabo poziva kot

> "Pes poleg Eifflovega stolpa v jutranji sončni svetlobi"

## Kaj sta DALL-E in Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) in [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sta dva najbolj priljubljena modela za generiranje slik, omogočata uporabo pozivov za generiranje slik.

### DALL-E

Začnimo z DALL-E, ki je generativni AI model, ki generira slike iz besedilnih opisov.

> [DALL-E je kombinacija dveh modelov, CLIP in razpršene pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ki generira vdelave, ki so numerične predstavitve podatkov, iz slik in besedil.

- **Razpršena pozornost** je model, ki generira slike iz vdelav. DALL-E je treniran na podatkovnem naboru slik in besedil ter se lahko uporablja za generiranje slik iz besedilnih opisov. Na primer, DALL-E se lahko uporablja za generiranje slik mačke s klobukom ali psa z mohawk frizuro.

### Midjourney

Midjourney deluje na podoben način kot DALL-E, generira slike iz besedilnih pozivov. Midjourney se lahko uporablja tudi za generiranje slik z uporabo pozivov, kot sta "mačka s klobukom" ali "pes z mohawk frizuro".

![Slika, generirana z Midjourney, mehanska golobica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika: Wikipedia, slika generirana z Midjourney_

## Kako delujeta DALL-E in Midjourney

Najprej [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model, ki temelji na arhitekturi transformatorjev z _avtoregresivnim transformatorjem_.

_Avtoregresivni transformator_ določa, kako model generira slike iz besedilnih opisov, generira en piksel naenkrat, nato pa uporabi generirane piksle za generiranje naslednjega piksla. Prehaja skozi več slojev v nevronski mreži, dokler slika ni končana.

S tem postopkom DALL-E nadzoruje atribute, objekte, značilnosti in več v sliki, ki jo generira. Vendar pa imata DALL-E 2 in 3 več nadzora nad generirano sliko.

## Gradnja vaše prve aplikacije za generiranje slik

Kaj je potrebno za gradnjo aplikacije za generiranje slik? Potrebujete naslednje knjižnice:

- **python-dotenv**, zelo priporočljivo je, da uporabite to knjižnico za shranjevanje vaših skrivnosti v datoteki _.env_ stran od kode.
- **openai**, to je knjižnica, ki jo boste uporabili za interakcijo z OpenAI API.
- **pillow**, za delo s slikami v Pythonu.
- **requests**, za pomoč pri izvajanju HTTP zahtev.

1. Ustvarite datoteko _.env_ z naslednjo vsebino:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Poiščite te informacije v Azure Portalu za vaš vir v razdelku "Ključi in končna točka".

1. Zberite zgoraj navedene knjižnice v datoteki _requirements.txt_ tako:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Nato ustvarite virtualno okolje in namestite knjižnice:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Za Windows uporabite naslednje ukaze za ustvarjanje in aktivacijo vašega virtualnega okolja:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodajte naslednjo kodo v datoteko _app.py_:

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

Razložimo to kodo:

- Najprej uvozimo knjižnice, ki jih potrebujemo, vključno z OpenAI knjižnico, dotenv knjižnico, requests knjižnico in Pillow knjižnico.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Nato naložimo okoljske spremenljivke iz datoteke _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Potem nastavimo končno točko, ključ za OpenAI API, verzijo in tip.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Nato generiramo sliko:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Zgornja koda se odzove z JSON objektom, ki vsebuje URL generirane slike. URL lahko uporabimo za prenos slike in shranjevanje v datoteko.

- Na koncu odpremo sliko in jo prikažemo z običajnim pregledovalnikom slik:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Več podrobnosti o generiranju slike

Poglejmo si kodo, ki generira sliko, bolj podrobno:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je besedilni poziv, ki se uporablja za generiranje slike. V tem primeru uporabljamo poziv "Zajček na konju, ki drži liziko, na meglenem travniku, kjer rastejo narcise".
- **size**, je velikost generirane slike. V tem primeru generiramo sliko, ki je 1024x1024 pikslov.
- **n**, je število generiranih slik. V tem primeru generiramo dve sliki.
- **temperature**, je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, in 1 pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Obstajajo še druge stvari, ki jih lahko počnete s slikami, ki jih bomo obravnavali v naslednjem razdelku.

## Dodatne zmožnosti generiranja slik

Doslej ste videli, kako smo lahko generirali sliko z nekaj vrsticami v Pythonu. Vendar pa obstajajo še druge stvari, ki jih lahko počnete s slikami.

Lahko tudi naredite naslednje:

- **Izvajanje urejanj**. Z zagotavljanjem obstoječe slike, maske in poziva lahko spremenite sliko. Na primer, lahko dodate nekaj na del slike. Predstavljajte si našo zajčjo sliko, lahko dodate klobuk zajčku. Kako bi to storili, je z zagotavljanjem slike, maske (ki identificira del območja za spremembo) in besedilnega poziva, ki pove, kaj je treba storiti.

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

  Osnovna slika bi vsebovala le zajčka, končna slika pa bi imela klobuk na zajčku.

- **Ustvarjanje različic**. Ideja je, da vzamete obstoječo sliko in zahtevate, da se ustvarijo različice. Za ustvarjanje različice zagotovite sliko in besedilni poziv ter kodo, kot sledi:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Opomba, to je podprto le na OpenAI

## Temperatura

Temperatura je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, in 1 pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Poglejmo primer, kako temperatura deluje, z izvedbo tega poziva dvakrat:

> Poziv: "Zajček na konju, ki drži liziko, na meglenem travniku, kjer rastejo narcise"

![Zajček na konju, ki drži liziko, verzija 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sl.png)

Zdaj pa izvedimo isti poziv, da vidimo, da ne bomo dvakrat dobili iste slike:

![Generirana slika zajčka na konju](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sl.png)

Kot vidite, so slike podobne, vendar niso enake. Poskusimo spremeniti vrednost temperature na 0.1 in poglejmo, kaj se zgodi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Spreminjanje temperature

Poskusimo narediti odziv bolj determinističen. Opazili smo, da je na prvi sliki zajček, na drugi pa konj, tako da se slike močno razlikujejo.

Zato spremenimo našo kodo in nastavimo temperaturo na 0, kot sledi:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Zdaj, ko zaženete to kodo, dobite ti dve sliki:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sl.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sl.png)

Tukaj lahko jasno vidite, kako si slike bolj podobne.

## Kako določiti meje za vašo aplikacijo z metapozivi

Z našim demo že lahko generiramo slike za naše stranke. Vendar pa moramo ustvariti nekaj mej za našo aplikacijo.

Na primer, ne želimo generirati slik, ki niso primerne za delo ali niso primerne za otroke.

To lahko storimo z _metapozivi_. Metapozivi so besedilni pozivi, ki se uporabljajo za nadzor izhoda generativnega AI modela. Na primer, lahko uporabimo metapozive za nadzor izhoda in zagotovimo, da so generirane slike primerne za delo ali primerne za otroke.

### Kako deluje?

Kako delujejo metapozivi?

Metapozivi so besedilni pozivi, ki se uporabljajo za nadzor izhoda generativnega AI modela, postavljeni so pred besedilni poziv in se uporabljajo za nadzor izhoda modela ter vgrajeni v aplikacije za nadzor izhoda modela. Združujejo vnos poziva in vnos metapoziva v en sam besedilni poziv.

En primer metapoziva bi bil naslednji:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zdaj pa poglejmo, kako lahko uporabimo metapozive v našem demo.

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

Iz zgornjega poziva lahko vidite, kako vse ustvarjene slike upoštevajo metapoziv.

## Naloga - omogočimo študentom

Na začetku te lekcije smo predstavili Edu4All. Zdaj je čas, da omogočimo študentom generiranje slik za njihove ocene.

Študentje bodo ustvarjali slike za svoje ocene, ki vsebujejo spomenike, točno kateri spomeniki je odvisno od študentov. Študentje so pozvani, da uporabijo svojo ustvarjalnost v tej nalogi in postavijo te spomenike v različne kontekste.

## Rešitev

Tukaj je ena možna rešitev:

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

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [kolekcijo učenja generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni AI!

Pojdite na lekcijo 10, kjer bomo pogledali, kako [graditi AI aplikacije z malo kode](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.