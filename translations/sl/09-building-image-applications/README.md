<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:27:42+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sl"
}
-->
# Izgradnja aplikacij za generiranje slik

LLM-ji niso namenjeni le generiranju besedila. Možno je tudi generirati slike iz besedilnih opisov. Imati slike kot način izražanja je lahko zelo koristno na številnih področjih, od medicinske tehnologije, arhitekture, turizma, razvoja iger in še več. V tem poglavju bomo pogledali dva najbolj priljubljena modela za generiranje slik, DALL-E in Midjourney.

## Uvod

V tej lekciji bomo pokrili:

- Generiranje slik in zakaj je koristno.
- DALL-E in Midjourney, kaj sta in kako delujeta.
- Kako bi zgradili aplikacijo za generiranje slik.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Zgradili aplikacijo za generiranje slik.
- Določili meje za vašo aplikacijo z metaprompti.
- Delali z DALL-E in Midjourney.

## Zakaj zgraditi aplikacijo za generiranje slik?

Aplikacije za generiranje slik so odličen način za raziskovanje zmogljivosti generativne umetne inteligence. Uporabljajo se lahko na primer za:

- **Urejanje in sintezo slik**. Lahko generirate slike za različne primere uporabe, kot so urejanje slik in sinteza slik.

- **Uporaba v različnih industrijah**. Prav tako se lahko uporabijo za generiranje slik za različne industrije, kot so medicinska tehnologija, turizem, razvoj iger in še več.

## Scenarij: Edu4All

Kot del te lekcije bomo nadaljevali delo z našim startupom, Edu4All. Študenti bodo ustvarjali slike za svoje ocenjevanje, katere slike bodo ustvarili, je odvisno od njih. Lahko bi bile ilustracije za njihovo lastno pravljico, ustvarjanje novega lika za njihovo zgodbo ali pomoč pri vizualizaciji njihovih idej in konceptov.

Tukaj je primer, kaj bi lahko študenti Edu4All ustvarili, če bi delali v razredu na temo spomenikov:

![Edu4All startup, razred na temo spomenikov, Eifflov stolp](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.sl.png)

uporabljajoč prompt, kot je

> "Pes poleg Eifflovega stolpa v jutranji sončni svetlobi"

## Kaj sta DALL-E in Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) in [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sta dva izmed najbolj priljubljenih modelov za generiranje slik, ki omogočata uporabo promptov za generiranje slik.

### DALL-E

Začnimo z DALL-E, ki je model generativne umetne inteligence, ki generira slike iz besedilnih opisov.

> [DALL-E je kombinacija dveh modelov, CLIP in difuzne pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ki generira vdelave, kar so numerične predstavitve podatkov, iz slik in besedila.

- **Difuzna pozornost** je model, ki generira slike iz vdelav. DALL-E je treniran na naboru podatkov slik in besedila ter se lahko uporablja za generiranje slik iz besedilnih opisov. Na primer, DALL-E se lahko uporablja za generiranje slik mačke s klobukom ali psa z irokezo.

### Midjourney

Midjourney deluje na podoben način kot DALL-E, generira slike iz besedilnih promptov. Midjourney se lahko uporablja tudi za generiranje slik z uporabo promptov, kot so "mačka s klobukom" ali "pes z irokezo".

![Slika, generirana z Midjourney, mehanski golob](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika iz Wikipedije, generirana z Midjourney_

## Kako delujeta DALL-E in Midjourney

Najprej, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model generativne umetne inteligence, ki temelji na arhitekturi transformatorja z _avtoregresivnim transformatorjem_.

_Avtoregresivni transformator_ določa, kako model generira slike iz besedilnih opisov, generira eno slikovno piko naenkrat, nato pa uporablja generirane slikovne pike za generiranje naslednje slikovne pike. Prehaja skozi več plasti v nevronski mreži, dokler slika ni dokončana.

S tem procesom DALL-E nadzira atribute, objekte, značilnosti in še več na sliki, ki jo generira. Vendar pa imata DALL-E 2 in 3 več nadzora nad generirano sliko.

## Izgradnja vaše prve aplikacije za generiranje slik

Kaj je potrebno za izgradnjo aplikacije za generiranje slik? Potrebujete naslednje knjižnice:

- **python-dotenv**, zelo priporočljivo je, da uporabite to knjižnico za shranjevanje vaših skrivnosti v datoteki _.env_ stran od kode.
- **openai**, ta knjižnica se uporablja za interakcijo z OpenAI API-jem.
- **pillow**, za delo s slikami v Pythonu.
- **requests**, za pomoč pri izvajanju HTTP zahtevkov.

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

   Za Windows uporabite naslednje ukaze za ustvarjanje in aktiviranje vašega virtualnega okolja:

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

Pojasnimo to kodo:

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

- Po tem nastavimo končno točko, ključ za OpenAI API, različico in tip.

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

  Zgornja koda se odzove z JSON objektom, ki vsebuje URL generirane slike. Uporabimo lahko URL za prenos slike in shranjevanje v datoteko.

- Na koncu odpremo sliko in uporabimo standardni pregledovalnik slik za prikaz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Več podrobnosti o generiranju slike

Poglejmo kodo, ki generira sliko, bolj podrobno:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** je besedilni poziv, ki se uporablja za generiranje slike. V tem primeru uporabljamo poziv "Zajček na konju, ki drži liziko, na megleni travi, kjer rastejo narcise".
- **size** je velikost slike, ki se generira. V tem primeru generiramo sliko, ki je 1024x1024 pikslov.
- **n** je število slik, ki se generirajo. V tem primeru generiramo dve sliki.
- **temperature** je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, 1 pa pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Obstajajo še druge stvari, ki jih lahko naredite s slikami, ki jih bomo pokrili v naslednjem razdelku.

## Dodatne zmogljivosti generiranja slik

Doslej ste videli, kako smo lahko generirali sliko z nekaj vrsticami v Pythonu. Vendar pa obstajajo še druge stvari, ki jih lahko naredite s slikami.

Lahko naredite tudi naslednje:

- **Izvedite urejanje**. S tem, da zagotovite obstoječo sliko, masko in poziv, lahko spremenite sliko. Na primer, lahko dodate nekaj na del slike. Predstavljajte si našo sliko zajčka, lahko dodate klobuk zajčku. Kako bi to naredili, je tako, da zagotovite sliko, masko (ki identificira del območja za spremembo) in besedilni poziv, ki pove, kaj naj se naredi.

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

- **Ustvarite različice**. Ideja je, da vzamete obstoječo sliko in zahtevate, da se ustvarijo različice. Za ustvarjanje različice zagotovite sliko in besedilni poziv in kodo, kot sledi:

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

Temperatura je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, 1 pa pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Poglejmo primer, kako deluje temperatura, z izvajanjem tega poziva dvakrat:

> Poziv: "Zajček na konju, ki drži liziko, na megleni travi, kjer rastejo narcise"

![Zajček na konju, ki drži liziko, različica 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.sl.png)

Zdaj pa ponovno izvedimo isti poziv, da vidimo, da ne bomo dobili iste slike dvakrat:

![Generirana slika zajčka na konju](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.sl.png)

Kot lahko vidite, so slike podobne, vendar niso enake. Poskusimo spremeniti vrednost temperature na 0.1 in poglejmo, kaj se zgodi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Spreminjanje temperature

Poskusimo narediti odziv bolj determinističen. Opazili smo, da je na prvi sliki zajček in na drugi sliki konj, tako da se slike močno razlikujejo.

Zato spremenimo našo kodo in nastavimo temperaturo na 0, tako:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Zdaj, ko zaženete to kodo, dobite ti dve sliki:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.sl.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.sl.png)

Tukaj lahko jasno vidite, kako so si slike bolj podobne.

## Kako določiti meje za vašo aplikacijo z metaprompti

Z našim demom lahko že generiramo slike za naše stranke. Vendar pa moramo ustvariti nekatere meje za našo aplikacijo.

Na primer, ne želimo generirati slik, ki niso primerne za delo, ali ki niso primerne za otroke.

To lahko naredimo z _metaprompti_. Metaprompti so besedilni pozivi, ki se uporabljajo za nadzor izhoda generativnega AI modela. Na primer, lahko uporabimo metaprompti za nadzor izhoda in zagotovimo, da so generirane slike primerne za delo ali primerne za otroke.

### Kako deluje?

Kako torej delujejo metaprompti?

Metaprompti so besedilni pozivi, ki se uporabljajo za nadzor izhoda generativnega AI modela, postavljeni so pred besedilni poziv in se uporabljajo za nadzor izhoda modela, vgrajeni v aplikacije za nadzor izhoda modela. Vključujejo vhod poziva in vhod metaprompta v en sam besedilni poziv.

En primer metaprompta bi bil naslednji:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zdaj pa poglejmo, kako lahko uporabimo metaprompti v našem demu.

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

Iz zgornjega poziva lahko vidite, kako vse slike, ki so ustvarjene, upoštevajo metaprompt.

## Naloga - omogočimo študentom

Na začetku te lekcije smo predstavili Edu4All. Zdaj je čas, da omogočimo študentom generiranje slik za njihove ocene.

Študenti bodo ustvarjali slike za svoje ocene, ki vsebujejo spomenike, kateri spomeniki so, je odvisno od študentov. Študenti so pozvani, da uporabijo svojo ustvarjalnost pri tej nalogi in postavijo te spomenike v različne kontekste.

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

Po zaključku te lekcije preverite našo [zbirko učenja generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

Pojdite na lekcijo 10, kjer bomo pogledali, kako [zgraditi AI aplikacije z nizko kodo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno prevajanje s strani človeka. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.