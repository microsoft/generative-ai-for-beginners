<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T19:45:20+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hr"
}
-->
# Izrada aplikacija za generiranje slika

[![Izrada aplikacija za generiranje slika](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-ovi nisu ograničeni samo na generiranje teksta. Moguće je generirati slike iz tekstualnih opisa. Imati slike kao modalitet može biti izuzetno korisno u raznim područjima, od medicinske tehnologije, arhitekture, turizma, razvoja igara i još mnogo toga. U ovom poglavlju upoznat ćemo se s dva najpopularnija modela za generiranje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji obradit ćemo:

- Generiranje slika i zašto je korisno.
- DALL-E i Midjourney, što su i kako rade.
- Kako izraditi aplikaciju za generiranje slika.

## Ciljevi učenja

Nakon završetka ove lekcije moći ćete:

- Izraditi aplikaciju za generiranje slika.
- Definirati granice za svoju aplikaciju pomoću metapromptova.
- Raditi s DALL-E i Midjourney.

## Zašto izraditi aplikaciju za generiranje slika?

Aplikacije za generiranje slika odličan su način za istraživanje mogućnosti Generativne AI. Mogu se koristiti, na primjer, za:

- **Uređivanje i sintezu slika**. Možete generirati slike za razne svrhe, poput uređivanja i sinteze slika.

- **Primjena u raznim industrijama**. Također se mogu koristiti za generiranje slika za različite industrije poput medicinske tehnologije, turizma, razvoja igara i drugih.

## Scenarij: Edu4All

Kroz ovu lekciju nastavljamo raditi s našim startupom, Edu4All. Učenici će stvarati slike za svoje zadatke, točno koje slike prepušteno je njima, ali to mogu biti ilustracije za vlastitu bajku, kreiranje novog lika za svoju priču ili vizualizacija ideja i koncepata.

Primjerice, učenici Edu4All-a mogli bi generirati sljedeće ako rade na satu o znamenitostima:

![Startup Edu4All, sat o znamenitostima, Eiffelov toranj](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hr.png)

koristeći prompt poput

> "Pas pored Eiffelovog tornja u jutarnjem suncu"

## Što su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) dva su najpopularnija modela za generiranje slika, koji omogućuju korištenje promptova za generiranje slika.

### DALL-E

Krenimo s DALL-E, koji je generativni AI model za generiranje slika iz tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i difuzne pažnje](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model koji generira ugrađene vektore, odnosno numeričke prikaze podataka, iz slika i teksta.

- **Difuzna pažnja** je model koji generira slike iz tih vektora. DALL-E je treniran na skupu podataka slika i teksta te može generirati slike iz tekstualnih opisa. Na primjer, DALL-E može generirati slike mačke s šeširom ili psa s irokezom.

### Midjourney

Midjourney radi slično kao DALL-E, generira slike iz tekstualnih promptova. Midjourney se također može koristiti za generiranje slika pomoću promptova poput “mačka s šeširom” ili “pas s irokezom”.

![Slika generirana Midjourneyem, mehanički golub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Slika: Wikipedia, generirano Midjourneyem_

## Kako rade DALL-E i Midjourney

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model temeljen na transformer arhitekturi s _autoregresivnim transformerom_.

_Autoregresivni transformer_ određuje kako model generira slike iz tekstualnih opisa, generira piksel po piksel, a zatim koristi generirane piksele za generiranje sljedećeg piksela. Prolazi kroz više slojeva neuronske mreže dok slika ne bude gotova.

Ovim postupkom DALL-E kontrolira atribute, objekte, karakteristike i još mnogo toga u generiranoj slici. No, DALL-E 2 i 3 imaju još veću kontrolu nad generiranom slikom.

## Izrada prve aplikacije za generiranje slika

Što je potrebno za izradu aplikacije za generiranje slika? Potrebne su vam sljedeće biblioteke:

- **python-dotenv**, preporučuje se koristiti ovu biblioteku za čuvanje tajnih podataka u _.env_ datoteci, odvojeno od koda.
- **openai**, ova biblioteka služi za interakciju s OpenAI API-jem.
- **pillow**, za rad sa slikama u Pythonu.
- **requests**, za slanje HTTP zahtjeva.

## Kreirajte i implementirajte Azure OpenAI model

Ako to još niste učinili, slijedite upute na [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) stranici
za kreiranje Azure OpenAI resursa i modela. Odaberite DALL-E 3 kao model.  

## Izrada aplikacije

1. Kreirajte datoteku _.env_ sa sljedećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Ove podatke pronađite u Azure OpenAI Foundry portalu za svoj resurs u odjeljku "Deployments".

1. Prikupite gore navedene biblioteke u datoteku _requirements.txt_ ovako:

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

1. Dodajte sljedeći kod u datoteku _app.py_:

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

Objašnjenje koda:

- Prvo uvozimo potrebne biblioteke, uključujući OpenAI, dotenv, requests i Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Zatim učitavamo varijable okruženja iz _.env_ datoteke.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Nakon toga konfiguriramo klijent za Azure OpenAI servis 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Sljedeće, generiramo sliku:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Gornji kod vraća JSON objekt koji sadrži URL generirane slike. Taj URL možemo koristiti za preuzimanje slike i spremanje u datoteku.

- Na kraju otvaramo sliku i prikazujemo je pomoću standardnog preglednika slika:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Više detalja o generiranju slike

Pogledajmo detaljnije kod koji generira sliku:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** je tekstualni prompt koji se koristi za generiranje slike. U ovom slučaju koristimo prompt "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi".
- **size** je veličina generirane slike. Ovdje generiramo sliku veličine 1024x1024 piksela.
- **n** je broj generiranih slika. Ovdje generiramo dvije slike.
- **temperature** je parametar koji kontrolira nasumičnost izlaza generativnog AI modela. Vrijednost temperature je između 0 i 1, gdje 0 znači da je izlaz deterministički, a 1 da je izlaz nasumičan. Zadana vrijednost je 0.7.

Postoji još mogućnosti rada sa slikama koje ćemo obraditi u sljedećem dijelu.

## Dodatne mogućnosti generiranja slika

Vidjeli ste kako smo generirali sliku s nekoliko linija koda u Pythonu. No, sa slikama možete učiniti još mnogo toga.

Također možete:

- **Uređivati slike**. Ako pružite postojeću sliku, masku i prompt, možete izmijeniti sliku. Na primjer, možete dodati nešto na dio slike. Zamislite našu sliku zeca, možete mu dodati šešir. To se radi tako da se dostavi slika, maska (koja označava dio za promjenu) i tekstualni prompt koji opisuje što treba napraviti. 
> Napomena: ovo nije podržano u DALL-E 3. 
 
Evo primjera korištenja GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Osnovna slika prikazuje samo lounge s bazenom, a konačna slika ima i flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Stvarati varijacije**. Ideja je da uzmete postojeću sliku i zatražite da se stvore varijacije. Za izradu varijacije, dostavite sliku i tekstualni prompt te kod poput ovog:

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

Temperatura je parametar koji kontrolira nasumičnost izlaza generativnog AI modela. Vrijednost temperature je između 0 i 1, gdje 0 znači da je izlaz deterministički, a 1 da je izlaz nasumičan. Zadana vrijednost je 0.7.

Pogledajmo primjer kako temperatura funkcionira, pokretanjem ovog prompta dvaput:

> Prompt: "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi"

![Zec na konju drži lizalicu, verzija 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hr.png)

Sada pokrenimo isti prompt još jednom da vidimo da nećemo dobiti istu sliku dvaput:

![Generirana slika zeca na konju](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hr.png)

Kao što vidite, slike su slične, ali nisu iste. Pokušajmo promijeniti vrijednost temperature na 0.1 i vidjeti što se događa:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promjena temperature

Pokušajmo učiniti odgovor više determinističkim. Iz dvije generirane slike možemo primijetiti da je na prvoj slici zec, a na drugoj konj, pa se slike dosta razlikuju.

Zato promijenimo kod i postavimo temperaturu na 0, ovako:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sada, kad pokrenete ovaj kod, dobit ćete ove dvije slike:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hr.png)
- ![Temperatura 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hr.png)

Ovdje jasno vidite da su slike puno sličnije jedna drugoj.

## Kako definirati granice za svoju aplikaciju pomoću metapromptova

S našom demo aplikacijom već možemo generirati slike za klijente. No, potrebno je postaviti određene granice za aplikaciju.

Na primjer, ne želimo generirati slike koje nisu prikladne za radno okruženje ili za djecu.

To možemo postići pomoću _metapromptova_. Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela. Na primjer, metapromptovima možemo kontrolirati izlaz i osigurati da generirane slike budu prikladne za radno okruženje ili za djecu.

### Kako to funkcionira?

Kako zapravo rade metapromptovi?

Metapromptovi su tekstualni promptovi koji se koriste za kontrolu izlaza generativnog AI modela, postavljaju se prije glavnog prompta i koriste se za kontrolu izlaza modela te se ugrađuju u aplikacije radi kontrole izlaza modela. Spoje se unos prompta i metaprompta u jedan tekstualni prompt.

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

Sada, pogledajmo kako možemo koristiti metapromptove u našem demo-u.

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

Iz gornjeg prompta vidite kako se svi generirani prikazi uzimaju u obzir metaprompt.

## Zadatak - omogućimo učenicima

Na početku lekcije predstavili smo Edu4All. Sada je vrijeme da omogućimo učenicima generiranje slika za njihove zadatke.

Učenici će kreirati slike za svoje zadatke koji sadrže znamenitosti, točno koje znamenitosti prepušteno je njima. Učenici su pozvani da budu kreativni i smjeste te znamenitosti u različite kontekste.

## Rješenje

Evo jednog mogućeg rješenja:

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

## Odlično! Nastavite s učenjem
Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje o generativnoj umjetnoj inteligenciji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili usavršavati svoje znanje o generativnoj AI!

Prijeđite na Lekciju 10 gdje ćemo vidjeti kako [izraditi AI aplikacije uz malo programiranja](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.