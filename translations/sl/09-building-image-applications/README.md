# Gradnja aplikacij za generiranje slik

[![Gradnja aplikacij za generiranje slik](../../../translated_images/sl/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM-ji niso pomembni samo za generiranje besedila. Možno je tudi generirati slike iz besedilnih opisov. Imati slike kot modaliteto je lahko zelo uporabno na številnih področjih, kot so MedTech, arhitektura, turizem, razvoj iger in še več. V tem poglavju bomo pogledali dva najbolj priljubljena modela za generiranje slik, DALL-E in Midjourney.

## Uvod

V tej lekciji bomo pokrili:

- Generiranje slik in zakaj je uporabno.
- DALL-E in Midjourney, kaj sta in kako delujeta.
- Kako bi zgradili aplikacijo za generiranje slik.

## Cilji učenja

Po zaključku te lekcije boste lahko:

- Zgradili aplikacijo za generiranje slik.
- Določili meje vaše aplikacije z meta prompti.
- Delali z DALL-E in Midjourney.

## Zakaj zgraditi aplikacijo za generiranje slik?

Aplikacije za generiranje slik so odličen način za raziskovanje zmogljivosti generativne umetne inteligence. Uporabljajo se lahko, na primer, za:

- **Urejanje in sinteza slik**. Lahko generirate slike za različne primere uporabe, kot so urejanje slik in sinteza slik.

- **Uporabljene v različnih industrijah**. Uporabljajo se lahko tudi za generiranje slik za različne industrije, kot so Medtech, turizem, razvoj iger in druge.

## Scenarij: Edu4All

Kot del te lekcije bomo nadaljevali delo z našim startupom Edu4All. Učenci bodo ustvarjali slike za svoje ocene; kaj natančno bodo slike, je odvisno od učencev, lahko so ilustracije za njihovo lastno pravljico, ustvarijo novega lika za svojo zgodbo ali si pomagajo vizualizirati svoje ideje in koncepte.

Tukaj je primer, kaj bi učenci Edu4All lahko ustvarili, če delajo v razredu na temo spomenikov:

![Startup Edu4All, razred o spomenikih, Eifflov stolp](../../../translated_images/sl/startup.94d6b79cc4bb3f5a.webp)

z ukazom:

> "Pes poleg Eifflovega stolpa ob zgodnjem jutranjem soncu"

## Kaj sta DALL-E in Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) in [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sta dva najbolj priljubljena modela za generiranje slik, ki omogočata uporabo promptov za generiranje slik.

### DALL-E

Začnimo z DALL-E, ki je model generativne umetne inteligence, ki generira slike iz besedilnih opisov.

> [DALL-E je kombinacija dveh modelov, CLIP in diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ki generira vdelane predstavitve (embeddinge), to so numerične predstavitve podatkov iz slik in besedila.

- **Diffused attention** je model, ki generira slike iz embeddingov. DALL-E je usposobljen na zbirki podatkov slik in besedil ter se lahko uporablja za generiranje slik iz besedilnih opisov. Na primer, DALL-E lahko uporabiš za generiranje slike mačke s klobukom ali psa s mohavkom.

### Midjourney

Midjourney deluje na podoben način kot DALL-E, generira slike iz besedilnih promptov. Midjourney se lahko uporablja za generiranje slik z ukazi, kot so »mačka s klobukom« ali »pes s mohavkom«.

![Slika, ki jo je ustvaril Midjourney, mehanski golob](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Vir slike Wikipedia, sliko je ustvaril Midjourney_

## Kako delujeta DALL-E in Midjourney

Najprej, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model generativne umetne inteligence, ki temelji na arhitekturi transformatorja z _avtoregresivnim transformatorjem_.

_Avtoregresivni transformator_ opredeljuje, kako model generira slike iz besedilnih opisov: generira en piksel naenkrat, nato uporabi ustvarjene piksle za generiranje naslednjega piksla. Prehaja skozi več plasti v nevronski mreži, dokler slika ni končana.

S tem procesom DALL-E nadzoruje atribute, predmete, značilnosti in še več na sliki, ki jo generira. Vendar pa imata DALL-E 2 in 3 večji nadzor nad ustvarjeno sliko.

## Gradnja vaše prve aplikacije za generiranje slik

Kaj potrebujete za izgradnjo aplikacije za generiranje slik? Potrebujete naslednje knjižnice:

- **python-dotenv**, močno priporočamo uporabo te knjižnice, da shranite svoje skrivnosti v datoteko _.env_ stran od kode.
- **openai**, to knjižnico boste uporabili za interakcijo z OpenAI API.
- **pillow**, za delo s slikami v Pythonu.
- **requests**, ki pomaga pri pošiljanju HTTP zahtevkov.

## Ustvarjanje in nameščanje Azure OpenAI modela

Če še ni opravljeno, sledite navodilom na strani [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
za ustvarjanje vira in modela Azure OpenAI. Izberite **gpt-image-1** kot model (trenutna generacija modela za generiranje slik Azure OpenAI; DALL-E 3 je zastarel in ni več na voljo za nove distribucije).

## Ustvarite aplikacijo

1. Ustvarite datoteko _.env_ z naslednjo vsebino:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Te informacije najdete v Azure OpenAI Foundry Portalu za vaš vir v razdelku "Deployments".

1. Zberite zgoraj omenjene knjižnice v datoteko imenovano _requirements.txt_ tako:

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
    
    # uvozi dotenv
    dotenv.load_dotenv()
    
    # konfiguriraj odjemalca za Azure OpenAI storitev
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Ustvari sliko z uporabo API-ja za generiranje slik
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Nastavi mapo za shranjeno sliko
        image_dir = os.path.join(os.curdir, 'images')

        # Če mapa ne obstaja, jo ustvari
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Inicializiraj pot do slike (upoštevaj, da mora biti vrsta datoteke png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Pridobi generirano sliko
        image_url = generation_response.data[0].url  # izvleci URL slike iz odgovora
        generated_image = requests.get(image_url).content  # prenesi sliko
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Prikaži sliko v privzetem pregledovalniku slik
        image = Image.open(image_path)
        image.show()

    # ujemi izjeme
    except openai.BadRequestError as err:
        print(err)
   ```

Razložimo to kodo:

- Najprej uvozimo potrebne knjižnice, med drugim OpenAI knjižnico, dotenv, requests in Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Nato naložimo okoljske spremenljivke iz _.env_ datoteke.

  ```python
  # uvozi dotenv
  dotenv.load_dotenv()
  ```

- Po tem konfiguriramo klienta za Azure OpenAI storitev

  ```python
  # Pridobi končno točko in ključ iz okoljskih spremenljivk
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Nato generiramo sliko:

  ```python
  # Ustvari sliko z uporabo API-ja za ustvarjanje slik
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Koda prej vrne JSON objekt, ki vsebuje URL ustvarjene slike. URL lahko uporabimo za prenos slike in shranjevanje v datoteko.

- Nazadnje odpremo sliko in jo prikažemo s standardnim pregledovalnikom slik:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Več podrobnosti o generiranju slike

Podrobneje si poglejmo kodo, ki generira sliko:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** je besedilni ukaz, ki se uporabi za generiranje slike. V tem primeru uporabljamo prompt "Zajček na konju, drži liziko, na megleni travi, kjer rastejo zvončki".
- **size** je velikost generirane slike. V tem primeru ustvarjamo sliko velikosti 1024x1024 pikslov.
- **n** je število generiranih slik. V tem primeru generiramo dve sliki.
- **temperature** je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni determinističen izhod, 1 pa naključnega. Privzeta vrednost je 0.7.

Obstaja še več možnosti za delo s slikami, ki jih bomo predstavili v naslednjem razdelku.

## Dodatne zmogljivosti generiranja slik

Do sedaj ste videli, kako lahko generiramo sliko z nekaj vrsticami kode v Pythonu. Vendar pa obstaja še več stvari, ki jih lahko delate s slikami.

Prav tako lahko naredite naslednje:

- **Urejanje slik**. Z zagotovitvijo obstoječe slike, maske in prompta lahko spreminjate sliko. Na primer, lahko dodate nekaj na določeni del slike. Predstavljajte si našo sliko zajčka, lahko mu dodate klobuk. To storite tako, da zagotovite sliko, masko (ki določa del območja za spremembo) in besedilni prompt, ki določi, kaj naj se naredi.
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

  Osnovna slika bi vsebovala samo salon s bazenom, a končna slika bi imela flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sl/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sl/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sl/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Ustvarjanje variacij**. Ideja je, da vzamete obstoječo sliko in zahtevate, da se ustvarijo variacije. Za ustvarjanje variacije podate sliko in besedilni prompt, ter kodo kot sledi:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Opomba, to je podprto samo na OpenAI-jevem modelu DALL-E 2, ne na gpt-image-1.

## Temperatura

Temperatura je parameter, ki nadzoruje naključnost izhoda generativnega AI modela. Temperatura je vrednost med 0 in 1, kjer 0 pomeni determinističen izhod, 1 pa naključnega. Privzeta vrednost je 0.7.

Poglejmo primer, kako deluje temperatura, tako da ta prompt zaženemo dvakrat:

> Prompt : "Zajček na konju, drži liziko, na megleni travi, kjer rastejo zvončki"

![Zajček na konju, drži liziko, verzija 1](../../../translated_images/sl/v1-generated-image.a295cfcffa3c13c2.webp)

Zdaj pa zaženimo isti prompt, da vidimo, da ne bomo dobili enake slike dvakrat:

![Generirana slika zajčka na konju](../../../translated_images/sl/v2-generated-image.33f55a3714efe61d.webp)

Kot vidite, sta sliki podobni, a ne enaki. Poskusimo spremeniti vrednost temperature na 0.1 in poglejmo, kaj se zgodi:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Vnesite besedilo vaše pozivke tukaj
        size='1024x1024',
        n=2
    )
```

### Spreminjanje temperature

Poskusimo narediti odgovor bolj determinističen. Iz dveh ustvarjenih slik lahko opazimo, da je na prvi sliki zajček, na drugi pa konj, torej se sliki precej razlikujeta.

Zato spremenimo našo kodo in nastavim temperaturu na 0, tako:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Vnesite besedilo vašega poziva tukaj
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ko zaženete to kodo, dobite ti dve sliki:

- ![Temperatura 0, v1](../../../translated_images/sl/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatura 0 , v2](../../../translated_images/sl/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Tukaj jasno vidite, da se slike bolj med seboj podobajo.

## Kako določiti meje za vašo aplikacijo z metaprompti

Z našo predstavitvijo lahko že generiramo slike za naše stranke. Vendar pa moramo za aplikacijo ustvariti nekatere meje.

Na primer, ne želimo generirati slik, ki niso primerne za delo ali ki niso primerne za otroke.

To lahko naredimo z _metaprompti_. Metaprompti so besedilni prompti, ki se uporabljajo za nadzor izhoda generativnega AI modela. Na primer, metaprompti nam omogočajo nadzorovati izhod in zagotoviti, da so ustvarjene slike primerne za delo oziroma otroke.

### Kako delujejo?

Kako pravzaprav delujejo metaprompti?

Metaprompti so besedilni prompti, ki se uporabljajo za nadzor izhoda generativnega modela, postavljeni so pred glavni prompt in so vključeni v aplikacije, da nadzorujejo izhod modela. Tako so vhodni prompt in metaprompt združeni v en sam besedilni prompt.

Primer metaprompta je naslednji:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Zdaj pa poglejmo, kako lahko v naši predstavitvi uporabimo metaprompte.

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

# TODO dodaj zahtevo za generiranje slike
```

Iz zgornjega prompta lahko vidite, da vse ustvarjene slike upoštevajo metaprompt.

## Naloga - omogočimo učencem

Predstavili smo Edu4All na začetku te lekcije. Zdaj je čas, da omogočimo učencem ustvarjanje slik za njihove ocene.


Študenti bodo ustvarili slike za svoje ocenjevanje, ki bodo vsebovale spomenike, natančno kateri spomeniki, pa je prepuščeno študentom. Študenti so povabljeni, da pri tem opravilu uporabijo svojo ustvarjalnost in spomenike postavijo v različne kontekste.

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

# Pridobite konec točke in ključ iz okoljskih spremenljivk
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
    # Ustvari sliko z uporabo API-ja za generiranje slik
    generation_response = client.images.generate(
        prompt=prompt,    # Vnesite besedilo spodbude tukaj
        size='1024x1024',
        n=1,
    )
    # Nastavite imenik za shranjeno sliko
    image_dir = os.path.join(os.curdir, 'images')

    # Če imenik ne obstaja, ga ustvarite
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inicializirajte pot slike (upoštevajte, da mora biti tip datoteke png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Pridobite ustvarjeno sliko
    image_url = generation_response.data[0].url  # izvleci URL slike iz odgovora
    generated_image = requests.get(image_url).content  # prenesite sliko
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Prikaži sliko v privzetem pregledovalniku slik
    image = Image.open(image_path)
    image.show()

# ujemi izjeme
except openai.BadRequestError as err:
    print(err)
```

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [zbirko za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da boste še naprej nadgrajevali svoje znanje o Generativni AI!

Oglejte si Lekcijo 10, kjer bomo pogledali, kako [graditi AI aplikacije z nizko kodo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->