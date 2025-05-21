<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:26:18+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hr"
}
-->
# Izgradnja Aplikacija za Generiranje Slika

[![Izgradnja Aplikacija za Generiranje Slika](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.hr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Generiranje teksta nije jedina funkcionalnost velikih jezičnih modela (LLM). Također je moguće generirati slike iz tekstualnih opisa. Imati slike kao modalitet može biti izuzetno korisno u brojnim područjima, od medicinske tehnologije, arhitekture, turizma, razvoja igara i još mnogo toga. U ovom poglavlju, razmotrit ćemo dva najpopularnija modela za generiranje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji obradit ćemo:

- Generiranje slika i zašto je korisno.
- DALL-E i Midjourney, što su i kako rade.
- Kako izgraditi aplikaciju za generiranje slika.

## Ciljevi Učenja

Nakon završetka ove lekcije, moći ćete:

- Izgraditi aplikaciju za generiranje slika.
- Definirati granice za vašu aplikaciju s meta promptovima.
- Raditi s DALL-E i Midjourney.

## Zašto izgraditi aplikaciju za generiranje slika?

Aplikacije za generiranje slika su odličan način za istraživanje mogućnosti generativne umjetne inteligencije. Mogu se koristiti, na primjer, za:

- **Uređivanje i sintezu slika**. Možete generirati slike za razne slučajeve upotrebe, poput uređivanja slika i sinteze slika.

- **Primjena u raznim industrijama**. Također se mogu koristiti za generiranje slika za razne industrije kao što su medicinska tehnologija, turizam, razvoj igara i još mnogo toga.

## Scenarij: Edu4All

Kao dio ove lekcije, nastavit ćemo raditi s našim startupom, Edu4All. Studenti će stvarati slike za svoje zadatke, točno koje slike prepušteno je studentima, ali to bi mogle biti ilustracije za njihovu bajku ili kreiranje novog lika za njihovu priču ili pomoć u vizualizaciji njihovih ideja i koncepata.

Evo što bi studenti Edu4All mogli generirati, na primjer, ako rade u razredu na spomenicima:

![Edu4All startup, razred o spomenicima, Eiffelov toranj](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.hr.png)

koristeći prompt kao što je

> "Pas pored Eiffelovog tornja u ranojutarnjem suncu"

## Što su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) su dva od najpopularnijih modela za generiranje slika, omogućuju vam korištenje promptova za generiranje slika.

### DALL-E

Počnimo s DALL-E, koji je generativni AI model koji generira slike iz tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i difuzne pažnje](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model koji generira ugradnje, koje su numeričke reprezentacije podataka, iz slika i teksta.

- **Difuzna pažnja**, je model koji generira slike iz ugradnji. DALL-E je treniran na skupu podataka slika i teksta i može se koristiti za generiranje slika iz tekstualnih opisa. Na primjer, DALL-E se može koristiti za generiranje slika mačke u šeširu ili psa s irokezom.

### Midjourney

Midjourney radi na sličan način kao DALL-E, generira slike iz tekstualnih promptova. Midjourney, također se može koristiti za generiranje slika koristeći promptove kao što su "mačka u šeširu" ili "pas s irokezom".

![Slika generirana od Midjourney, mehanički golub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika s Wikipedije, generirana od Midjourney_

## Kako rade DALL-E i Midjourney

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model baziran na arhitekturi transformatora s _autoregresivnim transformatorom_.

_Autoregresivni transformator_ definira kako model generira slike iz tekstualnih opisa, generira jedan piksel po jedan, a zatim koristi generirane piksele za generiranje sljedećeg piksela. Prolazi kroz više slojeva u neuronskoj mreži, sve dok slika nije dovršena.

S ovim procesom, DALL-E, kontrolira atribute, objekte, karakteristike i još mnogo toga u slici koju generira. Međutim, DALL-E 2 i 3 imaju više kontrole nad generiranom slikom.

## Izgradnja vaše prve aplikacije za generiranje slika

Što je potrebno za izgradnju aplikacije za generiranje slika? Trebate sljedeće biblioteke:

- **python-dotenv**, preporučuje se korištenje ove biblioteke za čuvanje vaših tajni u _.env_ datoteci dalje od koda.
- **openai**, ova biblioteka će se koristiti za interakciju s OpenAI API-jem.
- **pillow**, za rad sa slikama u Pythonu.
- **requests**, za pomoć pri izradi HTTP zahtjeva.

1. Kreirajte datoteku _.env_ sa sljedećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Pronađite ove informacije u Azure Portalu za vaš resurs u odjeljku "Keys and Endpoint".

1. Sakupite gore navedene biblioteke u datoteci pod nazivom _requirements.txt_ ovako:

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

   Za Windows, koristite sljedeće naredbe za kreiranje i aktivaciju vašeg virtualnog okruženja:

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

- Nakon toga, postavljamo krajnju točku, ključ za OpenAI API, verziju i tip.

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

- **prompt**, je tekstualni prompt koji se koristi za generiranje slike. U ovom slučaju, koristimo prompt "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi".
- **size**, je veličina slike koja se generira. U ovom slučaju, generiramo sliku veličine 1024x1024 piksela.
- **n**, je broj slika koje se generiraju. U ovom slučaju, generiramo dvije slike.
- **temperature**, je parametar koji kontrolira slučajnost izlaza generativnog AI modela. Temperatura je vrijednost između 0 i 1 gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz slučajan. Zadana vrijednost je 0.7.

Postoji još stvari koje možete raditi sa slikama koje ćemo pokriti u sljedećem odjeljku.

## Dodatne mogućnosti generiranja slika

Dosad ste vidjeli kako smo uspjeli generirati sliku koristeći nekoliko redaka u Pythonu. Međutim, postoje još stvari koje možete raditi sa slikama.

Također možete učiniti sljedeće:

- **Izvršavanje izmjena**. Pružanjem postojeće slike, maske i prompta, možete izmijeniti sliku. Na primjer, možete dodati nešto na dio slike. Zamislite našu sliku zeca, možete dodati šešir zecu. Kako biste to učinili je pružanjem slike, maske (koja identificira dio područja za promjenu) i tekstualnog prompta koji kaže što treba učiniti.

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

- **Stvaranje varijacija**. Ideja je da uzmete postojeću sliku i zatražite da se stvore varijacije. Da biste stvorili varijaciju, pružite sliku i tekstualni prompt i kod kao što je ovaj:

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

Temperatura je parametar koji kontrolira slučajnost izlaza generativnog AI modela. Temperatura je vrijednost između 0 i 1 gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz slučajan. Zadana vrijednost je 0.7.

Pogledajmo primjer kako temperatura radi, pokretanjem ovog prompta dvaput:

> Prompt: "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi"

![Zec na konju drži lizalicu, verzija 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.hr.png)

Sada pokrenimo taj isti prompt samo da vidimo da nećemo dobiti istu sliku dvaput:

![Generirana slika zeca na konju](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.hr.png)

Kao što vidite, slike su slične, ali nisu iste. Pokušajmo promijeniti vrijednost temperature na 0.1 i vidjeti što će se dogoditi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promjena temperature

Pokušajmo učiniti odgovor više determinističkim. Mogli smo primijetiti iz dvije generirane slike da na prvoj slici ima zeca, a na drugoj slici ima konja, tako da se slike jako razlikuju.

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

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.hr.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.hr.png)

Ovdje jasno možete vidjeti kako se slike više međusobno podudaraju.

## Kako definirati granice za vašu aplikaciju s metapromptovima

S našim demo, već možemo generirati slike za naše klijente. Međutim, trebamo stvoriti neke granice za našu aplikaciju.

Na primjer, ne želimo generirati slike koje nisu prikladne za radno okruženje ili koje nisu prikladne za djecu.

To možemo učiniti s _metapromptovima_. Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela. Na primjer, možemo koristiti metapromptove za kontrolu izlaza i osigurati da generirane slike budu prikladne za radno okruženje ili prikladne za djecu.

### Kako to radi?

Sada, kako metapromptovi rade?

Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela, postavljeni su prije tekstualnog prompta i koriste se za kontrolu izlaza modela i ugrađeni su u aplikacije za kontrolu izlaza modela. Obuhvaćaju ulaz prompta i ulaz metaprompta u jedan tekstualni prompt.

Jedan primjer metaprompta bio bi sljedeći:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sada, pogledajmo kako možemo koristiti metapromptove u našem demo.

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

Iz gornjeg prompta možete vidjeti kako sve slike koje se kreiraju uzimaju u obzir metaprompt.

## Zadatak - omogućimo studentima

Predstavili smo Edu4All na početku ove lekcije. Sada je vrijeme da omogućimo studentima generiranje slika za njihove zadatke.

Studenti će stvarati slike za svoje zadatke koji sadrže spomenike, točno koji spomenici prepušteno je studentima. Studenti su zamoljeni da koriste svoju kreativnost u ovom zadatku kako bi smjestili te spomenike u različite kontekste.

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

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili s unapređivanjem svog znanja o generativnoj umjetnoj inteligenciji!

Krenite na Lekciju 10 gdje ćemo pogledati kako [izgraditi AI aplikacije s malo koda](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo za točnost, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.