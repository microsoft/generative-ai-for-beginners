<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:58:19+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sl"
}
-->
# Gradnja aplikacij za generiranje slik

[![Gradnja aplikacij za generiranje slik](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-ji niso omejeni le na generiranje besedila. Možno je tudi generirati slike iz besedilnih opisov. Slike kot modalnost so lahko izjemno uporabne na številnih področjih, kot so MedTech, arhitektura, turizem, razvoj iger in še več. V tem poglavju bomo raziskali dva najbolj priljubljena modela za generiranje slik, DALL-E in Midjourney.

## Uvod

V tej lekciji bomo obravnavali:

- Generiranje slik in zakaj je koristno.
- DALL-E in Midjourney, kaj sta in kako delujeta.
- Kako zgraditi aplikacijo za generiranje slik.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Zgradili aplikacijo za generiranje slik.
- Določili meje za svojo aplikacijo z meta prompti.
- Delali z DALL-E in Midjourney.

## Zakaj zgraditi aplikacijo za generiranje slik?

Aplikacije za generiranje slik so odličen način za raziskovanje zmogljivosti generativne umetne inteligence. Uporabljajo se lahko na primer za:

- **Urejanje in sintezo slik**. Lahko generirate slike za različne namene, kot so urejanje slik in sinteza slik.

- **Uporaba v različnih industrijah**. Uporabljajo se lahko tudi za generiranje slik za različne industrije, kot so MedTech, turizem, razvoj iger in še več.

## Scenarij: Edu4All

V tej lekciji bomo nadaljevali delo z našim startupom Edu4All. Študenti bodo ustvarjali slike za svoje naloge, pri čemer je izbira slik prepuščena njim. Lahko ustvarijo ilustracije za svojo pravljico, nov lik za svojo zgodbo ali pa jim slike pomagajo vizualizirati njihove ideje in koncepte.

Tukaj je primer, kaj bi lahko študenti Edu4All ustvarili, če bi v razredu obravnavali spomenike:

![Startup Edu4All, razred o spomenikih, Eifflov stolp](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sl.png)

z uporabo prompta, kot je:

> "Pes poleg Eifflovega stolpa v jutranji sončni svetlobi"

## Kaj sta DALL-E in Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) in [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sta dva najbolj priljubljena modela za generiranje slik, ki omogočata uporabo promptov za generiranje slik.

### DALL-E

Začnimo z DALL-E, ki je generativni AI model, ki generira slike iz besedilnih opisov.

> [DALL-E je kombinacija dveh modelov, CLIP in razpršene pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ki generira vektorske predstavitve podatkov iz slik in besedila.

- **Razpršena pozornost** je model, ki generira slike iz vektorskih predstavitev. DALL-E je treniran na podatkovni zbirki slik in besedila ter se lahko uporablja za generiranje slik iz besedilnih opisov. Na primer, DALL-E lahko generira slike mačke v klobuku ali psa z irokezo.

### Midjourney

Midjourney deluje podobno kot DALL-E; generira slike iz besedilnih promptov. Midjourney lahko generira slike z uporabo promptov, kot so "mačka v klobuku" ali "pes z irokezo".

![Slika, generirana z Midjourney, mehanska golobica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika: Wikipedia, generirana z Midjourney_

## Kako delujeta DALL-E in Midjourney

Najprej [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model, ki temelji na arhitekturi transformatorjev z _avtoregresivnim transformatorjem_.

_Avtoregresivni transformator_ določa, kako model generira slike iz besedilnih opisov; generira en piksel naenkrat in nato uporabi generirane piksle za generiranje naslednjega piksla. Proces poteka skozi več slojev v nevronski mreži, dokler slika ni dokončana.

S tem procesom DALL-E nadzoruje atribute, objekte, značilnosti in več v generirani sliki. Vendar pa imata DALL-E 2 in 3 več nadzora nad generirano sliko.

## Gradnja vaše prve aplikacije za generiranje slik

Kaj potrebujete za gradnjo aplikacije za generiranje slik? Potrebujete naslednje knjižnice:

- **python-dotenv**, močno priporočamo uporabo te knjižnice za shranjevanje vaših skrivnosti v datoteki _.env_ stran od kode.
- **openai**, ta knjižnica se uporablja za interakcijo z OpenAI API-jem.
- **pillow**, za delo s slikami v Pythonu.
- **requests**, za pomoč pri pošiljanju HTTP zahtevkov.

## Ustvarjanje in uvajanje modela Azure OpenAI

Če tega še niste storili, sledite navodilom na strani [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), da ustvarite vir in model Azure OpenAI. Izberite model DALL-E 3.

## Ustvarjanje aplikacije

1. Ustvarite datoteko _.env_ z naslednjo vsebino:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Poiščite te informacije v Azure OpenAI Foundry Portal za vaš vir v razdelku "Deployments".

1. Zberite zgoraj navedene knjižnice v datoteki _requirements.txt_ na naslednji način:

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

   Za Windows uporabite naslednje ukaze za ustvarjanje in aktiviranje virtualnega okolja:

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

Pojasnimo to kodo:

- Najprej uvozimo knjižnice, ki jih potrebujemo, vključno s knjižnico OpenAI, knjižnico dotenv, knjižnico requests in knjižnico Pillow.

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

- Nato konfiguriramo odjemalca storitve Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Nato generiramo sliko:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Zgornja koda vrne JSON objekt, ki vsebuje URL generirane slike. URL lahko uporabimo za prenos slike in shranjevanje v datoteko.

- Na koncu odpremo sliko in jo prikažemo z uporabo standardnega pregledovalnika slik:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Več podrobnosti o generiranju slike

Poglejmo podrobneje kodo, ki generira sliko:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** je besedilni prompt, ki se uporablja za generiranje slike. V tem primeru uporabljamo prompt "Zajček na konju, drži liziko, na meglenem travniku, kjer rastejo narcise".
- **size** je velikost generirane slike. V tem primeru generiramo sliko velikosti 1024x1024 pikslov.
- **n** je število generiranih slik. V tem primeru generiramo dve sliki.
- **temperature** je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, 1 pa pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Obstajajo še druge stvari, ki jih lahko počnete s slikami, o katerih bomo govorili v naslednjem razdelku.

## Dodatne zmogljivosti generiranja slik

Videli ste, kako smo lahko generirali sliko z nekaj vrsticami kode v Pythonu. Vendar pa obstajajo še druge stvari, ki jih lahko počnete s slikami.

Lahko naredite naslednje:

- **Urejanje slik**. Z zagotavljanjem obstoječe slike, maske in prompta lahko spremenite sliko. Na primer, lahko dodate nekaj na določen del slike. Predstavljajte si našo sliko zajčka; lahko dodate klobuk zajčku. To storite tako, da zagotovite sliko, masko (ki identificira del območja za spremembo) in besedilni prompt, ki pove, kaj naj se naredi.
> Opomba: to ni podprto v DALL-E 3.

Tukaj je primer z uporabo GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Osnovna slika bi vsebovala le salon z bazenom, končna slika pa bi imela flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.sl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.sl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.sl.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Ustvarjanje različic**. Ideja je, da vzamete obstoječo sliko in zahtevate, da se ustvarijo različice. Za ustvarjanje različice zagotovite sliko in besedilni prompt ter kodo, kot je prikazano:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Opomba: to je podprto samo na OpenAI.

## Temperatura

Temperatura je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni, da je izhod determinističen, 1 pa pomeni, da je izhod naključen. Privzeta vrednost je 0.7.

Poglejmo primer, kako deluje temperatura, tako da dvakrat zaženemo ta prompt:

> Prompt: "Zajček na konju, drži liziko, na meglenem travniku, kjer rastejo narcise"

![Zajček na konju, drži liziko, različica 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sl.png)

Zdaj zaženimo isti prompt še enkrat, da vidimo, da ne bomo dobili iste slike dvakrat:

![Generirana slika zajčka na konju](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sl.png)

Kot lahko vidite, so slike podobne, vendar niso enake. Poskusimo spremeniti vrednost temperature na 0.1 in poglejmo, kaj se zgodi:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Spreminjanje temperature

Poskusimo narediti odziv bolj determinističen. Opazili smo, da se v prvih dveh generiranih slikah zajček in konj precej razlikujeta.

Spremenimo torej našo kodo in nastavimo temperaturo na 0, kot sledi:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ko zaženete to kodo, dobite ti dve sliki:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sl.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sl.png)

Tukaj lahko jasno vidite, kako se slike bolj podobajo druga drugi.

## Kako določiti meje za svojo aplikacijo z meta prompti

Z našo predstavitvijo lahko že generiramo slike za naše stranke. Vendar pa moramo določiti nekatere meje za našo aplikacijo.

Na primer, ne želimo generirati slik, ki niso primerne za delo ali ki niso primerne za otroke.

To lahko storimo z _meta prompti_. Meta prompti so besedilni prompti, ki se uporabljajo za nadzor izhoda generativnega AI modela. Na primer, lahko uporabimo meta prompt za nadzor izhoda in zagotovimo, da so generirane slike primerne za delo ali primerne za otroke.

### Kako deluje?

Kako torej delujejo meta prompti?

Meta prompti so besedilni prompti, ki se uporabljajo za nadzor izhoda generativnega AI modela. Postavljeni so pred besedilni prompt in se uporabljajo za nadzor izhoda modela ter so vgrajeni v aplikacije za nadzor izhoda modela. Združujejo vhodni prompt in meta prompt v en sam besedilni prompt.

Primer meta prompta bi bil naslednji:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zdaj poglejmo, kako lahko uporabimo meta prompt v naši predstavitvi.

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

Iz zgornjega prompta lahko vidite, kako vse generirane slike upoštevajo meta prompt.

## Naloga - omogočimo študentom

Na začetku te lekcije smo predstavili Edu4All. Zdaj je čas, da omogočimo študentom generiranje slik za njihove naloge.

Študenti bodo ustvarjali slike za svoje naloge, ki vsebujejo spomenike. Točno kateri spomeniki so izbrani, je prepuščeno študentom. Študenti so pozvani, da uporabijo svojo ustvarjalnost pri tej nalogi in postavijo te spomenike v različne kontekste.

## Rešitev

Tukaj je ena možna rešitev:
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

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni umetni inteligenci!

Pojdite na Lekcijo 10, kjer bomo raziskali, kako [graditi AI aplikacije z malo kode](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.