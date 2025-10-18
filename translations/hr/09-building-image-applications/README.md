<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-18T01:33:53+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hr"
}
-->
# Izrada aplikacija za generiranje slika

[![Izrada aplikacija za generiranje slika](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hr.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM-ovi nisu ograničeni samo na generiranje teksta. Također je moguće generirati slike iz tekstualnih opisa. Imati slike kao modalitet može biti izuzetno korisno u brojnim područjima poput medicinske tehnologije, arhitekture, turizma, razvoja igara i više. U ovom poglavlju ćemo istražiti dva najpopularnija modela za generiranje slika, DALL-E i Midjourney.

## Uvod

U ovoj lekciji obradit ćemo:

- Generiranje slika i zašto je korisno.
- DALL-E i Midjourney, što su i kako funkcioniraju.
- Kako izraditi aplikaciju za generiranje slika.

## Ciljevi učenja

Nakon završetka ove lekcije, moći ćete:

- Izraditi aplikaciju za generiranje slika.
- Definirati granice za svoju aplikaciju pomoću meta prompta.
- Raditi s DALL-E i Midjourney.

## Zašto izraditi aplikaciju za generiranje slika?

Aplikacije za generiranje slika odličan su način za istraživanje mogućnosti generativne umjetne inteligencije. Mogu se koristiti, na primjer:

- **Uređivanje i sinteza slika**. Možete generirati slike za razne primjene, poput uređivanja slika i sinteze slika.

- **Primjena u raznim industrijama**. Također se mogu koristiti za generiranje slika za razne industrije poput medicinske tehnologije, turizma, razvoja igara i više.

## Scenarij: Edu4All

Kao dio ove lekcije, nastavit ćemo raditi s našim startupom, Edu4All. Studenti će kreirati slike za svoje zadatke, točno koje slike ovisi o studentima, ali to mogu biti ilustracije za njihovu vlastitu bajku, kreiranje novog lika za njihovu priču ili im pomoći vizualizirati njihove ideje i koncepte.

Evo što bi studenti Edu4All-a mogli generirati, na primjer, ako rade u razredu na spomenicima:

![Startup Edu4All, razred o spomenicima, Eiffelov toranj](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hr.png)

koristeći prompt poput

> "Pas pored Eiffelovog tornja u jutarnjem svjetlu"

## Što su DALL-E i Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) i [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) dva su najpopularnija modela za generiranje slika, omogućuju vam korištenje prompta za generiranje slika.

### DALL-E

Počnimo s DALL-E, koji je generativni AI model koji generira slike iz tekstualnih opisa.

> [DALL-E je kombinacija dva modela, CLIP i difuzne pažnje](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model koji generira ugrađene podatke, numeričke reprezentacije podataka, iz slika i teksta.

- **Difuzna pažnja**, je model koji generira slike iz ugrađenih podataka. DALL-E je treniran na skupu podataka slika i teksta i može se koristiti za generiranje slika iz tekstualnih opisa. Na primjer, DALL-E se može koristiti za generiranje slika mačke s kapom ili psa s irokezom.

### Midjourney

Midjourney radi na sličan način kao DALL-E, generira slike iz tekstualnih prompta. Midjourney se također može koristiti za generiranje slika koristeći prompte poput "mačka s kapom" ili "pas s irokezom".

![Slika generirana pomoću Midjourney, mehanička golubica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Autor slike Wikipedia, slika generirana pomoću Midjourney_

## Kako funkcioniraju DALL-E i Midjourney

Prvo, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativni AI model temeljen na arhitekturi transformatora s _autoregresivnim transformatorom_.

_Autoregresivni transformator_ definira kako model generira slike iz tekstualnih opisa, generira jedan piksel po piksel, a zatim koristi generirane piksele za generiranje sljedećeg piksela. Prolazi kroz više slojeva u neuronskoj mreži dok slika ne bude dovršena.

Ovim procesom DALL-E kontrolira atribute, objekte, karakteristike i više u slici koju generira. Međutim, DALL-E 2 i 3 imaju veću kontrolu nad generiranom slikom.

## Izrada vaše prve aplikacije za generiranje slika

Što je potrebno za izradu aplikacije za generiranje slika? Potrebne su vam sljedeće biblioteke:

- **python-dotenv**, preporučuje se korištenje ove biblioteke za čuvanje vaših tajni u datoteci _.env_ odvojeno od koda.
- **openai**, ova biblioteka koristi se za interakciju s OpenAI API-jem.
- **pillow**, za rad sa slikama u Pythonu.
- **requests**, za pomoć pri slanju HTTP zahtjeva.

## Kreiranje i implementacija Azure OpenAI modela

Ako to već niste učinili, slijedite upute na stranici [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 
za kreiranje Azure OpenAI resursa i modela. Odaberite DALL-E 3 kao model.  

## Kreiranje aplikacije

1. Kreirajte datoteku _.env_ sa sljedećim sadržajem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Ove informacije pronađite u Azure OpenAI Foundry portalu za vaš resurs u odjeljku "Deployments".

1. Prikupite gore navedene biblioteke u datoteci pod nazivom _requirements.txt_ na sljedeći način:

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

- Prvo, uvozimo potrebne biblioteke, uključujući OpenAI biblioteku, dotenv biblioteku, requests biblioteku i Pillow biblioteku.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Zatim učitavamo varijable okruženja iz datoteke _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Nakon toga konfiguriramo klijenta za Azure OpenAI uslugu.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Zatim generiramo sliku:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Gornji kod vraća JSON objekt koji sadrži URL generirane slike. Možemo koristiti URL za preuzimanje slike i spremanje u datoteku.

- Na kraju, otvaramo sliku i koristimo standardni preglednik slika za prikaz:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Više detalja o generiranju slike

Pogledajmo kod koji generira sliku detaljnije:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, je tekstualni prompt koji se koristi za generiranje slike. U ovom slučaju, koristimo prompt "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi".
- **size**, je veličina generirane slike. U ovom slučaju, generiramo sliku veličine 1024x1024 piksela.
- **n**, je broj generiranih slika. U ovom slučaju, generiramo dvije slike.
- **temperature**, je parametar koji kontrolira nasumičnost izlaza generativnog AI modela. Vrijednost temperature je između 0 i 1, gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz nasumičan. Zadana vrijednost je 0.7.

Postoje još mnoge stvari koje možete raditi sa slikama, a o tome ćemo govoriti u sljedećem dijelu.

## Dodatne mogućnosti generiranja slika

Do sada ste vidjeli kako smo uspjeli generirati sliku koristeći nekoliko linija koda u Pythonu. Međutim, postoje još mnoge stvari koje možete raditi sa slikama.

Također možete učiniti sljedeće:

- **Izvršiti izmjene**. Pružanjem postojeće slike, maske i prompta, možete izmijeniti sliku. Na primjer, možete dodati nešto na dio slike. Zamislite našu sliku zeca, možete dodati šešir zecu. Kako biste to učinili, trebate pružiti sliku, masku (koja identificira dio područja za promjenu) i tekstualni prompt koji opisuje što treba učiniti. 
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

  Osnovna slika bi sadržavala samo salon s bazenom, ali konačna slika bi imala flaminga:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.hr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.hr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.hr.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Kreirati varijacije**. Ideja je da uzmete postojeću sliku i zatražite da se kreiraju varijacije. Za kreiranje varijacije, pružate sliku i tekstualni prompt te kod poput ovog:

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

Temperatura je parametar koji kontrolira nasumičnost izlaza generativnog AI modela. Vrijednost temperature je između 0 i 1, gdje 0 znači da je izlaz deterministički, a 1 znači da je izlaz nasumičan. Zadana vrijednost je 0.7.

Pogledajmo primjer kako temperatura funkcionira, pokretanjem ovog prompta dva puta:

> Prompt : "Zec na konju, drži lizalicu, na maglovitoj livadi gdje rastu narcisi"

![Zec na konju drži lizalicu, verzija 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hr.png)

Sada pokrenimo isti prompt ponovno da vidimo da nećemo dobiti istu sliku dva puta:

![Generirana slika zeca na konju](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hr.png)

Kao što možete vidjeti, slike su slične, ali nisu iste. Pokušajmo promijeniti vrijednost temperature na 0.1 i vidjeti što će se dogoditi:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Promjena temperature

Pokušajmo učiniti odgovor više determinističkim. Mogli smo primijetiti iz dvije generirane slike da na prvoj slici postoji zec, a na drugoj slici konj, pa se slike značajno razlikuju.

Stoga promijenimo naš kod i postavimo temperaturu na 0, ovako:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sada kada pokrenete ovaj kod, dobit ćete ove dvije slike:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hr.png)
- ![Temperatura 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hr.png)

Ovdje jasno možete vidjeti kako se slike više međusobno podudaraju.

## Kako definirati granice za svoju aplikaciju pomoću meta prompta

S našim demo primjerom već možemo generirati slike za naše klijente. Međutim, trebamo postaviti neke granice za našu aplikaciju.

Na primjer, ne želimo generirati slike koje nisu prikladne za radno okruženje ili koje nisu primjerene za djecu.

To možemo učiniti pomoću _meta prompta_. Meta prompti su tekstualni prompti koji se koriste za kontrolu izlaza generativnog AI modela. Na primjer, možemo koristiti meta prompte za kontrolu izlaza i osigurati da generirane slike budu prikladne za radno okruženje ili za djecu.

### Kako to funkcionira?

Kako funkcioniraju meta prompti?

Meta prompti su tekstualni prompti koji se koriste za kontrolu izlaza generativnog AI modela, postavljaju se prije tekstualnog prompta i koriste se za kontrolu izlaza modela te se ugrađuju u aplikacije kako bi kontrolirali izlaz modela. Kombiniraju unos prompta i unos meta prompta u jedan tekstualni prompt.

Jedan primjer meta prompta bio bi sljedeći:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sada, pogledajmo kako možemo koristiti meta prompt u našem demo primjeru.

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

Iz gornjeg prompta možete vidjeti kako sve generirane slike uzimaju u obzir meta prompt.

## Zadatak - omogućimo studentima

Na početku ove lekcije predstavili smo Edu4All. Sada je vrijeme da omogućimo studentima generiranje slika za njihove zadatke.

Studenti će kreirati slike za svoje zadatke koji uključuju spomenike, točno koji spomenici ovisi o studentima. Od studenata se traži da koriste svoju kreativnost u ovom zadatku kako bi smjestili te spomenike u različite kontekste.

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

## Sjajan posao! Nastavite učiti

Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje o generativnoj AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj AI!

Prijeđite na Lekciju 10 gdje ćemo istražiti kako [izraditi AI aplikacije s malo koda](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.