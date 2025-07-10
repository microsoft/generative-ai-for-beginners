<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:34:59+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hr"
}
-->
# Izrada aplikacija za generiranje slika

[![Izrada aplikacija za generiranje slika](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM modeli nisu samo za generiranje teksta. Također je moguće generirati slike na temelju tekstualnih opisa. Korištenje slika kao modaliteta može biti izuzetno korisno u mnogim područjima poput MedTecha, arhitekture, turizma, razvoja igara i drugih. U ovom poglavlju upoznat ćemo se s dva najpopularnija modela za generiranje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji obradit ćemo:

- Generiranje slika i zašto je korisno.
- DALL-E i Midjourney, što su i kako funkcioniraju.
- Kako izraditi aplikaciju za generiranje slika.

## Ciljevi učenja

Nakon završetka ove lekcije moći ćete:

- Izraditi aplikaciju za generiranje slika.
- Definirati granice svoje aplikacije pomoću meta promptova.
- Raditi s DALL-E i Midjourney.

## Zašto izraditi aplikaciju za generiranje slika?

Aplikacije za generiranje slika odličan su način za istraživanje mogućnosti Generativne AI. Mogu se koristiti, na primjer, za:

- **Uređivanje i sintezu slika**. Možete generirati slike za različite primjene, poput uređivanja i sinteze slika.

- **Primjenu u raznim industrijama**. Također se mogu koristiti za generiranje slika u industrijama poput Medtecha, turizma, razvoja igara i drugih.

## Scenarij: Edu4All

Kao dio ove lekcije nastavljamo raditi sa startupom Edu4All. Studenti će stvarati slike za svoje zadatke, a što će točno biti na slikama ovisi o njima – mogu to biti ilustracije za vlastitu bajku, novi lik za priču ili pomoć u vizualizaciji njihovih ideja i koncepata.

Evo što bi studenti Edu4All-a mogli generirati, primjerice ako rade u razredu na spomenicima:

![Edu4All startup, razred o spomenicima, Eiffelov toranj](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hr.png)

koristeći prompt poput

> "Pas pored Eiffelovog tornja u ranom jutarnjem svjetlu"

## Što su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) su dva najpopularnija modela za generiranje slika, koji vam omogućuju da pomoću promptova generirate slike.

### DALL-E

Počnimo s DALL-E, Generativnim AI modelom koji generira slike na temelju tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model koji generira embeddings, numeričke prikaze podataka, iz slika i teksta.

- **Diffused attention** je model koji generira slike iz embeddingsa. DALL-E je treniran na skupu podataka slika i teksta te se može koristiti za generiranje slika na temelju tekstualnih opisa. Na primjer, DALL-E može generirati slike mačke s kapom ili psa s mohawkom.

### Midjourney

Midjourney radi na sličan način kao DALL-E, generira slike na temelju tekstualnih promptova. Midjourney također može generirati slike koristeći promptove poput “mačka s kapom” ili “pas s mohawkom”.

![Slika generirana pomoću Midjourney, mehanički golub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika: Wikipedia, generirano pomoću Midjourney_

## Kako DALL-E i Midjourney funkcioniraju

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je Generativni AI model baziran na transformer arhitekturi s _autoregresivnim transformerom_.

Autoregresivni transformer definira kako model generira slike iz tekstualnih opisa – generira jedan piksel po piksel, a zatim koristi već generirane piksele za generiranje sljedećeg. Prolazi kroz više slojeva u neuronskoj mreži dok slika nije kompletna.

Ovim procesom DALL-E kontrolira atribute, objekte, karakteristike i druge detalje u generiranoj slici. Međutim, DALL-E 2 i 3 imaju veću kontrolu nad generiranom slikom.

## Izrada prve aplikacije za generiranje slika

Što je potrebno za izradu aplikacije za generiranje slika? Trebat će vam sljedeće biblioteke:

- **python-dotenv**, preporučuje se za pohranu tajni u _.env_ datoteku, odvojeno od koda.
- **openai**, biblioteka za interakciju s OpenAI API-jem.
- **pillow**, za rad sa slikama u Pythonu.
- **requests**, za slanje HTTP zahtjeva.

1. Kreirajte datoteku _.env_ sa sljedećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Ove podatke pronađite u Azure Portalu za svoj resurs u odjeljku "Keys and Endpoint".

1. Nabrojite potrebne biblioteke u datoteci _requirements.txt_ ovako:

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

   Za Windows koristite sljedeće naredbe za kreiranje i aktivaciju virtualnog okruženja:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Dodajte sljedeći kod u datoteku nazvanu _app.py_:

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

- Prvo uvozimo potrebne biblioteke, uključujući OpenAI, dotenv, requests i Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Zatim učitavamo varijable okoline iz _.env_ datoteke.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Nakon toga postavljamo endpoint, ključ za OpenAI API, verziju i tip.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Sljedeće, generiramo sliku:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Gornji kod vraća JSON objekt koji sadrži URL generirane slike. Taj URL možemo koristiti za preuzimanje slike i spremanje u datoteku.

- Na kraju, otvaramo sliku i prikazujemo je u standardnom pregledniku slika:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Detaljnije o generiranju slike

Pogledajmo detaljnije kod koji generira sliku:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** je tekstualni prompt koji se koristi za generiranje slike. U ovom slučaju koristimo prompt "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi".
- **size** je veličina generirane slike. Ovdje generiramo sliku dimenzija 1024x1024 piksela.
- **n** je broj generiranih slika. Ovdje generiramo dvije slike.
- **temperature** je parametar koji kontrolira nasumičnost izlaza Generativnog AI modela. Vrijednost je između 0 i 1, gdje 0 znači deterministički izlaz, a 1 nasumični. Zadana vrijednost je 0.7.

Postoje i druge mogućnosti rada sa slikama koje ćemo obraditi u sljedećem dijelu.

## Dodatne mogućnosti generiranja slika

Do sada ste vidjeli kako generirati sliku s nekoliko redaka Pythona. No, postoji još toga što možete raditi sa slikama.

Također možete:

- **Izvršavati izmjene**. Pružajući postojeću sliku, masku i prompt, možete mijenjati sliku. Na primjer, možete dodati nešto na dio slike. Zamislite našu sliku sa zecom – možete mu dodati šešir. To se radi tako da se dostavi slika, maska (koja označava dio slike za promjenu) i tekstualni prompt koji opisuje što treba napraviti.

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

  Osnovna slika sadrži samo zeca, a konačna slika će imati šešir na zecu.

- **Kreirati varijacije**. Ideja je da uzmete postojeću sliku i zatražite da se naprave varijacije. Za to se dostavlja slika i tekstualni prompt, te se koristi kod poput ovog:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Napomena, ovo je podržano samo na OpenAI platformi

## Temperature

Temperature je parametar koji kontrolira nasumičnost izlaza Generativnog AI modela. Vrijednost je između 0 i 1, gdje 0 znači deterministički izlaz, a 1 nasumični. Zadana vrijednost je 0.7.

Pogledajmo primjer kako temperature funkcionira, pokretanjem ovog prompta dva puta:

> Prompt: "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi"

![Zec na konju drži lizalicu, verzija 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hr.png)

Sada pokrenimo isti prompt još jednom da vidimo da nećemo dobiti istu sliku dva puta:

![Generirana slika zeca na konju](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hr.png)

Kao što vidite, slike su slične, ali nisu iste. Pokušajmo promijeniti vrijednost temperature na 0.1 i vidjeti što će se dogoditi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promjena temperature

Pokušajmo sada učiniti odgovor determinističnijim. Primijetili smo da na prvoj slici imamo zeca, a na drugoj konja, pa se slike znatno razlikuju.

Stoga ćemo promijeniti kod i postaviti temperature na 0, ovako:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Kad pokrenete ovaj kod, dobit ćete ove dvije slike:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hr.png)
- ![Temperature 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hr.png)

Ovdje jasno vidite da se slike međusobno više podudaraju.

## Kako definirati granice za svoju aplikaciju pomoću metapromptova

U našem demo primjeru već možemo generirati slike za naše korisnike. Međutim, potrebno je postaviti neke granice za aplikaciju.

Na primjer, ne želimo generirati slike koje nisu prikladne za radno okruženje ili nisu primjerene za djecu.

To možemo postići pomoću _metapromptova_. Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza Generativnog AI modela. Na primjer, možemo koristiti metapromptove da osiguramo da generirane slike budu sigurne za rad i prikladne za djecu.

### Kako to funkcionira?

Kako metapromptovi rade?

Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza Generativnog AI modela, postavljaju se prije glavnog prompta i ugrađuju u aplikacije kako bi kontrolirali izlaz modela. Time se ulazni prompt i metaprompt kombiniraju u jedan tekstualni prompt.

Primjer metaprompta bio bi sljedeći:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sada pogledajmo kako možemo koristiti metapromptove u našem demo primjeru.

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

Iz gornjeg prompta vidite kako sve generirane slike uzimaju u obzir metaprompt.

## Zadatak - omogućimo studentima

Na početku lekcije predstavili smo Edu4All. Sada je vrijeme da omogućimo studentima generiranje slika za njihove zadatke.

Studenti će stvarati slike za svoje zadatke koje sadrže spomenike, a točno koji spomenici su na njima ovisi o studentima. Traži se da koriste svoju kreativnost i smjeste spomenike u različite kontekste.

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

## Odličan posao! Nastavite s učenjem

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) i nastavite usavršavati svoje znanje o Generativnoj AI!

Krenite na Lekciju 10 gdje ćemo pogledati kako [izraditi AI aplikacije s low-code pristupom](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.