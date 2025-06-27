<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:37:43+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hr"
}
-->
# Izgradnja aplikacija za generiranje slika

Postoji više od LLM-ova osim generiranja teksta. Također je moguće generirati slike iz tekstualnih opisa. Imati slike kao modalitet može biti izuzetno korisno u brojnim područjima kao što su MedTech, arhitektura, turizam, razvoj igara i više. U ovom poglavlju ćemo razmotriti dva najpopularnija modela za generiranje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji obradit ćemo:

- Generiranje slika i zašto je korisno.
- DALL-E i Midjourney, što su i kako rade.
- Kako izgraditi aplikaciju za generiranje slika.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Izgraditi aplikaciju za generiranje slika.
- Definirati granice za svoju aplikaciju s meta promptima.
- Raditi s DALL-E i Midjourney.

## Zašto izgraditi aplikaciju za generiranje slika?

Aplikacije za generiranje slika su izvrstan način za istraživanje mogućnosti Generativne AI. Mogu se koristiti, na primjer, za:

- **Uređivanje i sintezu slika**. Možete generirati slike za razne slučajeve korištenja, kao što su uređivanje slika i sinteza slika.

- **Primjena u raznim industrijama**. Također se mogu koristiti za generiranje slika za razne industrije poput Medtech, turizma, razvoja igara i više.

## Scenarij: Edu4All

Kao dio ove lekcije, nastavit ćemo raditi s našim startupom, Edu4All. Studenti će stvarati slike za svoje procjene, točno koje slike je na studentima, ali mogle bi biti ilustracije za njihovu vlastitu bajku ili stvaranje novog lika za njihovu priču ili im pomoći vizualizirati njihove ideje i koncepte.

Evo što bi studenti Edu4All-a mogli generirati, na primjer, ako rade na satu o spomenicima:

koristeći prompt poput

> "Pas pored Eiffelovog tornja u ranim jutarnjim sunčevim zrakama"

## Što su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) su dva od najpopularnijih modela za generiranje slika, omogućuju vam korištenje prompta za generiranje slika.

### DALL-E

Započnimo s DALL-E, koji je Generativni AI model koji generira slike iz tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i difuzna pažnja](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model koji generira ugrađivanja, koja su numeričke reprezentacije podataka, iz slika i teksta.

- **Difuzna pažnja**, je model koji generira slike iz ugrađivanja. DALL-E je treniran na skupu podataka slika i teksta i može se koristiti za generiranje slika iz tekstualnih opisa. Na primjer, DALL-E se može koristiti za generiranje slika mačke u šeširu ili psa s irokez frizurom.

### Midjourney

Midjourney radi na sličan način kao DALL-E, generira slike iz tekstualnih prompta. Midjourney se također može koristiti za generiranje slika koristeći prompte poput "mačka u šeširu" ili "pas s irokez frizurom".

## Kako DALL-E i Midjourney rade

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je Generativni AI model temeljen na arhitekturi transformatora s _autoregresivnim transformatorom_.

Autoregresivni transformator definira kako model generira slike iz tekstualnih opisa, generira jedan piksel po jedan, a zatim koristi generirane piksele za generiranje sljedećeg piksela. Prolazi kroz više slojeva u neuronskoj mreži, sve dok slika nije gotova.

S ovim procesom, DALL-E kontrolira atribute, objekte, karakteristike i više u slici koju generira. Međutim, DALL-E 2 i 3 imaju više kontrole nad generiranom slikom.

## Izgradnja vaše prve aplikacije za generiranje slika

Što je potrebno za izgradnju aplikacije za generiranje slika? Potrebne su vam sljedeće biblioteke:

- **python-dotenv**, preporučuje se korištenje ove biblioteke za čuvanje vaših tajni u _.env_ datoteci dalje od koda.
- **openai**, ova biblioteka je ono što ćete koristiti za interakciju s OpenAI API-jem.
- **pillow**, za rad sa slikama u Pythonu.
- **requests**, za pomoć pri slanju HTTP zahtjeva.

1. Kreirajte datoteku _.env_ sa sljedećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Pronađite ove informacije u Azure Portalu za svoj resurs u odjeljku "Keys and Endpoint".

1. Sakupite gore navedene biblioteke u datoteku pod nazivom _requirements.txt_ ovako:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Zatim kreirajte virtualno okruženje i instalirajte biblioteke:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Za Windows, koristite sljedeće naredbe za kreiranje i aktiviranje vašeg virtualnog okruženja:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodajte sljedeći kod u datoteku pod nazivom _app.py_:

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

Objasnimo ovaj kod:

- Prvo, uvozimo biblioteke koje trebamo, uključujući OpenAI biblioteku, dotenv biblioteku, requests biblioteku i Pillow biblioteku.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Zatim, učitavamo varijable okruženja iz _.env_ datoteke.

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

- Zatim, generiramo sliku:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Gornji kod odgovara JSON objektom koji sadrži URL generirane slike. Možemo koristiti URL za preuzimanje slike i spremanje u datoteku.

- Na kraju, otvaramo sliku i koristimo standardni preglednik slika za prikaz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Više detalja o generiranju slike

Pogledajmo kod koji generira sliku detaljnije:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je tekstualni prompt koji se koristi za generiranje slike. U ovom slučaju, koristimo prompt "Zeko na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi".
- **size**, je veličina slike koja se generira. U ovom slučaju, generiramo sliku veličine 1024x1024 piksela.
- **n**, je broj slika koje se generiraju. U ovom slučaju, generiramo dvije slike.
- **temperature**, je parametar koji kontrolira slučajnost izlaza Generativnog AI modela. Temperatura je vrijednost između 0 i 1 gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz slučajan. Zadana vrijednost je 0.7.

Postoji više stvari koje možete učiniti sa slikama koje ćemo obraditi u sljedećem dijelu.

## Dodatne mogućnosti generiranja slika

Do sada ste vidjeli kako smo mogli generirati sliku koristeći nekoliko linija u Pythonu. Međutim, postoje još stvari koje možete učiniti sa slikama.

Također možete učiniti sljedeće:

- **Izvršiti izmjene**. Davanjem postojeće slike, maske i prompta, možete izmijeniti sliku. Na primjer, možete dodati nešto na dio slike. Zamislite našu sliku zeca, možete dodati šešir zecu. Kako biste to učinili je davanjem slike, maske (identificiranje dijela područja za promjenu) i tekstualnog prompta da kažete što treba učiniti.

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

  Osnovna slika bi sadržavala samo zeca, ali konačna slika bi imala šešir na zecu.

- **Stvoriti varijacije**. Ideja je da uzmete postojeću sliku i zatražite da se stvore varijacije. Za stvaranje varijacije, pružate sliku i tekstualni prompt i kod ovako:

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

Temperatura je parametar koji kontrolira slučajnost izlaza Generativnog AI modela. Temperatura je vrijednost između 0 i 1 gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz slučajan. Zadana vrijednost je 0.7.

Pogledajmo primjer kako temperatura radi, pokretanjem ovog prompta dva puta:

> Prompt : "Zeko na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi"

Sada pokrenimo taj isti prompt samo da vidimo da nećemo dobiti istu sliku dvaput:

Kao što vidite, slike su slične, ali nisu iste. Pokušajmo promijeniti vrijednost temperature na 0.1 i vidjeti što će se dogoditi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promjena temperature

Pokušajmo učiniti odgovor determinističkijim. Mogli smo primijetiti iz dviju generiranih slika da na prvoj slici ima zeca, a na drugoj slici ima konja, tako da se slike jako razlikuju.

Stoga promijenimo naš kod i postavimo temperaturu na 0, ovako:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sada kada pokrenete ovaj kod, dobit ćete ove dvije slike:

Ovdje jasno možete vidjeti kako se slike više međusobno podudaraju.

## Kako definirati granice za svoju aplikaciju s metapromptima

S našim demo, već možemo generirati slike za naše klijente. Međutim, trebamo stvoriti neke granice za našu aplikaciju.

Na primjer, ne želimo generirati slike koje nisu prikladne za radno okruženje ili koje nisu prikladne za djecu.

To možemo učiniti s _metapromptima_. Metaprompti su tekstualni prompti koji se koriste za kontrolu izlaza Generativnog AI modela. Na primjer, možemo koristiti metaprompti za kontrolu izlaza i osigurati da su generirane slike prikladne za radno okruženje ili prikladne za djecu.

### Kako to radi?

Sada, kako metaprompti rade?

Metaprompti su tekstualni prompti koji se koriste za kontrolu izlaza Generativnog AI modela, oni su pozicionirani prije tekstualnog prompta i koriste se za kontrolu izlaza modela i ugrađeni su u aplikacije za kontrolu izlaza modela. Obuhvaćajući unos prompta i unos metaprompta u jedan tekstualni prompt.

Jedan primjer metaprompta bi bio sljedeći:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sada, pogledajmo kako možemo koristiti metaprompti u našem demo.

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

Iz gornjeg prompta, možete vidjeti kako sve slike koje se stvaraju uzimaju u obzir metaprompt.

## Zadatak - omogućimo studentima

Predstavili smo Edu4All na početku ove lekcije. Sada je vrijeme da omogućimo studentima da generiraju slike za svoje procjene.

Studenti će stvarati slike za svoje procjene koje sadrže spomenike, točno koji spomenici je na studentima. Studenti su zamoljeni da koriste svoju kreativnost u ovom zadatku kako bi postavili te spomenike u različite kontekste.

## Rješenje

Evo jednog mogućeg rješenja:

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

## Odlično! Nastavite s učenjem

Nakon završetka ove lekcije, provjerite našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

Pređite na Lekciju 10 gdje ćemo pogledati kako [izgraditi AI aplikacije s malo koda](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.