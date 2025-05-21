<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:25:29+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sr"
}
-->
# Izgradnja aplikacija za generisanje slika

[![Izgradnja aplikacija za generisanje slika](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.sr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-ovi nisu samo za generisanje teksta. Takođe je moguće generisati slike iz tekstualnih opisa. Imati slike kao modalitet može biti veoma korisno u brojnim oblastima, od medicinske tehnologije, arhitekture, turizma, razvoja igara i drugih. U ovom poglavlju ćemo se osvrnuti na dva najpopularnija modela za generisanje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji ćemo pokriti:

- Generisanje slika i zašto je korisno.
- DALL-E i Midjourney, šta su i kako funkcionišu.
- Kako biste izgradili aplikaciju za generisanje slika.

## Ciljevi učenja

Nakon završetka ove lekcije, bićete u mogućnosti da:

- Izgradite aplikaciju za generisanje slika.
- Definišete granice za vašu aplikaciju uz pomoć meta prompta.
- Radite sa DALL-E i Midjourney.

## Zašto graditi aplikaciju za generisanje slika?

Aplikacije za generisanje slika su odličan način da istražite mogućnosti Generativne AI. Mogu se koristiti, na primer, za:

- **Uređivanje i sintezu slika**. Možete generisati slike za razne slučajeve upotrebe, kao što su uređivanje i sinteza slika.

- **Primena u različitim industrijama**. Takođe se mogu koristiti za generisanje slika za različite industrije kao što su Medtech, Turizam, Razvoj igara i još mnogo toga.

## Scenario: Edu4All

Kao deo ove lekcije, nastavićemo da radimo sa našim startupom, Edu4All. Studenti će kreirati slike za svoje zadatke, tačno koje slike zavisi od studenata, ali to mogu biti ilustracije za njihovu bajku ili kreiranje novog lika za njihovu priču ili im pomoći da vizualizuju svoje ideje i koncepte.

Evo šta bi studenti Edu4All mogli generisati, na primer, ako rade u razredu na spomenicima:

![Edu4All startup, čas o spomenicima, Ajfelov toranj](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.sr.png)

koristeći prompt poput

> "Pas pored Ajfelovog tornja u jutarnjem suncu"

## Šta su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) su dva od najpopularnijih modela za generisanje slika, omogućavaju vam da koristite promptove za generisanje slika.

### DALL-E

Počnimo sa DALL-E, koji je generativni AI model koji generiše slike iz tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model koji generiše ugradnje, koje su numeričke reprezentacije podataka, iz slika i teksta.

- **Diffused attention**, je model koji generiše slike iz ugradnji. DALL-E je treniran na skupu podataka slika i teksta i može se koristiti za generisanje slika iz tekstualnih opisa. Na primer, DALL-E se može koristiti za generisanje slika mačke u šeširu ili psa sa irokez frizurom.

### Midjourney

Midjourney radi na sličan način kao DALL-E, generiše slike iz tekstualnih promptova. Midjourney se takođe može koristiti za generisanje slika koristeći promptove kao što su “mačka u šeširu” ili “pas sa irokez frizurom”.

![Slika generisana od strane Midjourney, mehanički golub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika sa Wikipedia, slika generisana od strane Midjourney_

## Kako rade DALL-E i Midjourney

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model zasnovan na arhitekturi transformatora sa _autoregresivnim transformatorom_.

_Autoregresivni transformator_ definiše kako model generiše slike iz tekstualnih opisa, generiše jedan piksel po piksel, a zatim koristi generisane piksele da generiše sledeći piksel. Prolazi kroz više slojeva u neuronskoj mreži, dok slika ne bude kompletna.

Kroz ovaj proces, DALL-E, kontroliše atribute, objekte, karakteristike i više u slici koju generiše. Međutim, DALL-E 2 i 3 imaju više kontrole nad generisanom slikom.

## Izgradnja vaše prve aplikacije za generisanje slika

Šta je potrebno za izgradnju aplikacije za generisanje slika? Potrebne su vam sledeće biblioteke:

- **python-dotenv**, preporučuje se da koristite ovu biblioteku kako biste čuvali svoje tajne u _.env_ fajlu dalje od koda.
- **openai**, ova biblioteka će vam pomoći da komunicirate sa OpenAI API-jem.
- **pillow**, za rad sa slikama u Python-u.
- **requests**, da vam pomogne da napravite HTTP zahteve.

1. Kreirajte fajl _.env_ sa sledećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Pronađite ovu informaciju u Azure portalu za vaš resurs u odeljku "Keys and Endpoint".

1. Sakupite navedene biblioteke u fajlu pod nazivom _requirements.txt_ ovako:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Zatim, kreirajte virtuelno okruženje i instalirajte biblioteke:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Za Windows, koristite sledeće komande da kreirate i aktivirate svoje virtuelno okruženje:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodajte sledeći kod u fajl pod nazivom _app.py_:

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

Hajde da objasnimo ovaj kod:

- Prvo, uvozimo potrebne biblioteke, uključujući OpenAI biblioteku, dotenv biblioteku, requests biblioteku i Pillow biblioteku.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Zatim, učitavamo promenljive okruženja iz _.env_ fajla.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Nakon toga, postavljamo endpoint, ključ za OpenAI API, verziju i tip.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Zatim, generišemo sliku:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Gornji kod odgovara JSON objektom koji sadrži URL generisane slike. Možemo koristiti URL za preuzimanje slike i njeno čuvanje u fajlu.

- Na kraju, otvaramo sliku i koristimo standardni pregledač slika da je prikažemo:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Više detalja o generisanju slike

Hajde da pogledamo kod koji generiše sliku detaljnije:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je tekstualni prompt koji se koristi za generisanje slike. U ovom slučaju, koristimo prompt "Zeka na konju, drži lizalicu, na maglovitoj livadi gde rastu narcisi".
- **size**, je veličina slike koja se generiše. U ovom slučaju, generišemo sliku koja je 1024x1024 piksela.
- **n**, je broj slika koje se generišu. U ovom slučaju, generišemo dve slike.
- **temperature**, je parametar koji kontroliše nasumičnost izlaza generativnog AI modela. Temperatura je vrednost između 0 i 1 gde 0 znači da je izlaz deterministički, a 1 znači da je izlaz nasumičan. Podrazumevana vrednost je 0.7.

Postoje još stvari koje možete raditi sa slikama koje ćemo pokriti u sledećem odeljku.

## Dodatne mogućnosti generisanja slika

Do sada ste videli kako smo uspeli da generišemo sliku koristeći nekoliko linija u Python-u. Međutim, postoje još stvari koje možete raditi sa slikama.

Možete takođe uraditi sledeće:

- **Izvršiti izmene**. Pružajući postojeću sliku, masku i prompt, možete izmeniti sliku. Na primer, možete dodati nešto na deo slike. Zamislite našu sliku zeke, možete dodati šešir zeki. Kako biste to uradili je pružanjem slike, maske (identifikovanje dela područja za promenu) i tekstualnog prompta da kažete šta treba uraditi.

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

  Osnovna slika bi sadržala samo zeku, ali konačna slika bi imala šešir na zeki.

- **Kreirati varijacije**. Ideja je da uzmete postojeću sliku i zatražite da se kreiraju varijacije. Da biste kreirali varijaciju, pružate sliku i tekstualni prompt i kod kao što je ovaj:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Napomena, ovo je podržano samo na OpenAI

## Temperatura

Temperatura je parametar koji kontroliše nasumičnost izlaza generativnog AI modela. Temperatura je vrednost između 0 i 1 gde 0 znači da je izlaz deterministički, a 1 znači da je izlaz nasumičan. Podrazumevana vrednost je 0.7.

Hajde da pogledamo primer kako temperatura funkcioniše, pokretanjem ovog prompta dva puta:

> Prompt : "Zeka na konju, drži lizalicu, na maglovitoj livadi gde rastu narcisi"

![Zeka na konju drži lizalicu, verzija 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.sr.png)

Sada hajde da pokrenemo taj isti prompt samo da vidimo da nećemo dobiti istu sliku dva puta:

![Generisana slika zeke na konju](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.sr.png)

Kao što vidite, slike su slične, ali nisu iste. Hajde da pokušamo promeniti vrednost temperature na 0.1 i vidimo šta se dešava:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promena temperature

Dakle, hajde da pokušamo učiniti odgovor više determinističkim. Mogli smo primetiti iz dve slike koje smo generisali da na prvoj slici postoji zeka, a na drugoj slici postoji konj, tako da se slike značajno razlikuju.

Hajde stoga da promenimo naš kod i postavimo temperaturu na 0, ovako:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sada kada pokrenete ovaj kod, dobijate ove dve slike:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.sr.png)
- ![Temperatura 0 , v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.sr.png)

Ovde jasno možete videti kako slike više liče jedna na drugu.

## Kako definisati granice za vašu aplikaciju sa metapromptovima

Sa našim demom, već možemo generisati slike za naše klijente. Međutim, potrebno je da kreiramo neke granice za našu aplikaciju.

Na primer, ne želimo da generišemo slike koje nisu bezbedne za radno okruženje ili koje nisu prikladne za decu.

Možemo to uraditi pomoću _metapromptova_. Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela. Na primer, možemo koristiti metapromptove za kontrolu izlaza i osigurati da generisane slike budu bezbedne za radno okruženje ili prikladne za decu.

### Kako funkcioniše?

Sada, kako metapromptovi funkcionišu?

Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela, postavljeni su pre tekstualnog prompta i koriste se za kontrolu izlaza modela i ugrađeni su u aplikacije kako bi kontrolisali izlaz modela. Obuhvatajući unos prompta i unos metaprompta u jedan tekstualni prompt.

Jedan primer metaprompta bio bi sledeći:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sada, hajde da vidimo kako možemo koristiti metapromptove u našem demu.

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

Iz gornjeg prompta, možete videti kako sve slike koje se kreiraju uzimaju u obzir metaprompt.

## Zadaci - omogućimo studentima

Predstavili smo Edu4All na početku ove lekcije. Sada je vreme da omogućimo studentima da generišu slike za svoje zadatke.

Studenti će kreirati slike za svoje zadatke koji sadrže spomenike, tačno koji spomenici zavisi od studenata. Studenti su zamoljeni da koriste svoju kreativnost u ovom zadatku kako bi postavili ove spomenike u različite kontekste.

## Rešenje

Evo jednog mogućeg rešenja:

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

## Odličan rad! Nastavite sa učenjem

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite sa unapređivanjem svog znanja o Generativnoj AI!

Pređite na Lekciju 10 gde ćemo pogledati kako [izgraditi AI aplikacije sa malo koda](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Одричање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење вештачком интелигенцијом [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразума или погрешна тумачења која настану услед коришћења овог превода.