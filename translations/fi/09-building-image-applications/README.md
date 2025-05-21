<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:15:20+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fi"
}
-->
# Kuvien luontisovellusten rakentaminen

LLM-mallit tarjoavat muutakin kuin tekstin luomista. On myös mahdollista luoda kuvia tekstikuvauksista. Kuvien käyttö voi olla erittäin hyödyllistä monilla aloilla, kuten lääketeknologiassa, arkkitehtuurissa, matkailussa, pelikehityksessä ja muussa. Tässä luvussa tarkastelemme kahta suosituinta kuvien luontimallia, DALL-E:tä ja Midjourneytä.

## Johdanto

Tässä oppitunnissa käsittelemme:

- Kuvien luomista ja miksi se on hyödyllistä.
- DALL-E ja Midjourney, mitä ne ovat ja miten ne toimivat.
- Miten rakentaa kuvien luontisovellus.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Rakentaa kuvien luontisovelluksen.
- Määritellä sovelluksesi rajat meta-kehotteilla.
- Työskennellä DALL-E:n ja Midjourneyn kanssa.

## Miksi rakentaa kuvien luontisovellus?

Kuvien luontisovellukset ovat loistava tapa tutkia Generatiivisen AI:n kykyjä. Niitä voidaan käyttää esimerkiksi:

- **Kuvien muokkaus ja synteesi**. Voit luoda kuvia erilaisiin käyttötarkoituksiin, kuten kuvien muokkaukseen ja synteesiin.

- **Sovellettavissa eri toimialoille**. Niitä voidaan käyttää myös kuvien luomiseen eri toimialoille, kuten lääketeknologia, matkailu, pelikehitys ja muu.

## Tilanne: Edu4All

Osana tätä oppituntia jatkamme työskentelyä startupimme, Edu4All:n, kanssa. Oppilaat luovat kuvia arviointejaan varten, tarkalleen millaisia kuvia, on oppilaiden päätettävissä, mutta ne voivat olla kuvituksia omalle sadulleen tai uuden hahmon luomista tarinaansa varten tai auttamaan heitä visualisoimaan ideoitaan ja käsitteitään.

Esimerkiksi, jos Edu4All:n oppilaat työskentelevät luokassa monumenttien parissa, he voisivat luoda tällaisia kuvia:

käyttäen kehotetta kuten

> "Koira Eiffel-tornin vieressä varhaisen aamun auringonvalossa"

## Mitä ovat DALL-E ja Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ja [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ovat kaksi suosituinta kuvien luontimallia, jotka mahdollistavat kuvien luomisen kehotteiden avulla.

### DALL-E

Aloitetaan DALL-E:stä, joka on Generatiivinen AI-malli, joka luo kuvia tekstikuvauksista.

> [DALL-E on yhdistelmä kahta mallia, CLIP ja diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, on malli, joka luo upotuksia, jotka ovat numeerisia esityksiä datasta, kuvista ja tekstistä.

- **Diffused attention**, on malli, joka luo kuvia upotuksista. DALL-E on koulutettu kuvien ja tekstin tietokannalla ja sitä voidaan käyttää kuvien luomiseen tekstikuvauksista. Esimerkiksi, DALL-E:llä voi luoda kuvia kissasta hatun kanssa tai koirasta irokeesilla.

### Midjourney

Midjourney toimii samalla tavalla kuin DALL-E, se luo kuvia tekstikehotteista. Midjourneytä voidaan käyttää myös kuvien luomiseen kehotteilla kuten "kissa hatussa" tai "koira irokeesilla".

## Miten DALL-E ja Midjourney toimivat

Ensinnäkin, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E on Generatiivinen AI-malli, joka perustuu transformer-arkkitehtuuriin _autoregressiivisella transformerilla_.

_Autoregressiivinen transformer_ määrittelee, miten malli luo kuvia tekstikuvauksista, se luo yhden pikselin kerrallaan ja käyttää sitten luotuja pikseleitä seuraavan pikselin luomiseen. Tämä tapahtuu kulkemalla useiden hermoverkon kerrosten läpi, kunnes kuva on valmis.

Tällä prosessilla DALL-E hallitsee ominaisuuksia, esineitä, piirteitä ja muuta luomassaan kuvassa. Kuitenkin DALL-E 2 ja 3 tarjoavat enemmän kontrollia luotuun kuvaan.

## Ensimmäisen kuvien luontisovelluksen rakentaminen

Mitä siis tarvitaan kuvien luontisovelluksen rakentamiseen? Tarvitset seuraavat kirjastot:

- **python-dotenv**, on suositeltavaa käyttää tätä kirjastoa pitämään salaisuudet _.env_ tiedostossa erillään koodista.
- **openai**, tämä kirjasto on se, jota käytät ollaksesi vuorovaikutuksessa OpenAI API:n kanssa.
- **pillow**, kuvien käsittelyyn Pythonissa.
- **requests**, auttamaan HTTP-pyyntöjen tekemisessä.

1. Luo tiedosto _.env_ seuraavalla sisällöllä:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Etsi tämä tieto Azure Portaalista resurssillesi "Keys and Endpoint" -osiossa.

1. Kerää yllä olevat kirjastot tiedostoon nimeltä _requirements.txt_ näin:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Seuraavaksi luo virtuaaliympäristö ja asenna kirjastot:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windowsissa käytä seuraavia komentoja luodaksesi ja aktivoidaksesi virtuaaliympäristön:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Lisää seuraava koodi tiedostoon nimeltä _app.py_:

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

Selitetään tämä koodi:

- Ensin tuomme tarvitsemamme kirjastot, mukaan lukien OpenAI-kirjasto, dotenv-kirjasto, requests-kirjasto ja Pillow-kirjasto.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Seuraavaksi lataamme ympäristömuuttujat _.env_ tiedostosta.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Sen jälkeen asetamme OpenAI API:n päätepisteen, avaimen, version ja tyypin.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Seuraavaksi luomme kuvan:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Yllä oleva koodi vastaa JSON-objektilla, joka sisältää luodun kuvan URL-osoitteen. Voimme käyttää URL-osoitetta ladataksemme kuvan ja tallentaaksemme sen tiedostoon.

- Lopuksi avaamme kuvan ja käytämme standardia kuvan katseluohjelmaa sen näyttämiseen:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Tarkemmin kuvan luomisesta

Katsotaan tarkemmin koodia, joka luo kuvan:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, on tekstikehote, jota käytetään kuvan luomiseen. Tässä tapauksessa käytämme kehotetta "Pupu hevosella, pidellen tikkaria, sumuisella niityllä, jossa kasvaa narsisseja".
- **size**, on luodun kuvan koko. Tässä tapauksessa luomme kuvan, joka on 1024x1024 pikseliä.
- **n**, on luotavien kuvien määrä. Tässä tapauksessa luomme kaksi kuvaa.
- **temperature**, on parametri, joka ohjaa Generatiivisen AI-mallin tuottaman tuloksen satunnaisuutta. Lämpötila on arvo välillä 0 ja 1, jossa 0 tarkoittaa, että tulos on deterministinen ja 1 tarkoittaa, että tulos on satunnainen. Oletusarvo on 0.7.

On paljon muitakin asioita, joita voit tehdä kuvilla, ja käsittelemme niitä seuraavassa osiossa.

## Kuvien luomisen lisäominaisuudet

Olet nähnyt, miten pystyimme luomaan kuvan muutamalla rivillä Pythonia. Kuitenkin, on muitakin asioita, joita voit tehdä kuvilla.

Voit myös tehdä seuraavaa:

- **Suorittaa muokkauksia**. Antamalla olemassa olevan kuvan maskin ja kehotteen, voit muuttaa kuvaa. Esimerkiksi voit lisätä jotain kuvan osaan. Kuvittele pupumme kuva, voit lisätä hatun pupulle. Tämä tehdään antamalla kuva, maski (joka tunnistaa osan alueesta muutosta varten) ja tekstikehote, joka kertoo mitä pitäisi tehdä.

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

  Peruskuva sisältäisi vain pupun, mutta lopullisessa kuvassa pupulla olisi hattu.

- **Luoda variaatioita**. Ajatuksena on, että otat olemassa olevan kuvan ja pyydät, että siitä luodaan variaatioita. Luodaksesi variaation, annat kuvan ja tekstikehotteen ja koodin näin:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Huomaa, tämä on tuettu vain OpenAI:ssa

## Lämpötila

Lämpötila on parametri, joka ohjaa Generatiivisen AI-mallin tuottaman tuloksen satunnaisuutta. Lämpötila on arvo välillä 0 ja 1, jossa 0 tarkoittaa, että tulos on deterministinen ja 1 tarkoittaa, että tulos on satunnainen. Oletusarvo on 0.7.

Katsotaan esimerkkiä, miten lämpötila toimii, ajamalla tämä kehote kahdesti:

> Kehote: "Pupu hevosella, pidellen tikkaria, sumuisella niityllä, jossa kasvaa narsisseja"

Nyt ajetaan sama kehote uudelleen vain nähdäksemme, ettemme saa samaa kuvaa kahdesti:

Kuten näet, kuvat ovat samanlaisia, mutta eivät samoja. Kokeillaan muuttaa lämpötila-arvoa 0.1:een ja katsotaan mitä tapahtuu:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Lämpötilan muuttaminen

Kokeillaan tehdä vastaus deterministisemmäksi. Voimme havaita kahdesta luodusta kuvasta, että ensimmäisessä kuvassa on pupu ja toisessa kuvassa on hevonen, joten kuvat eroavat suuresti.

Muutetaan siis koodiamme ja asetetaan lämpötila 0:ksi, näin:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nyt kun ajat tämän koodin, saat nämä kaksi kuvaa:

Tässä näet selvästi, kuinka kuvat muistuttavat toisiaan enemmän.

## Miten määritellä sovelluksesi rajat meta-kehotteilla

Demonstraatiomme avulla voimme jo luoda kuvia asiakkaillemme. Kuitenkin, meidän on luotava joitain rajoja sovelluksellemme.

Esimerkiksi emme halua luoda kuvia, jotka eivät ole sopivia työpaikalle tai eivät ole sopivia lapsille.

Voimme tehdä tämän _meta-kehotteilla_. Meta-kehotteet ovat tekstikehotteita, joita käytetään ohjaamaan Generatiivisen AI-mallin tuottamaa tulosta. Esimerkiksi, voimme käyttää meta-kehotteita ohjaamaan tulosta ja varmistamaan, että luodut kuvat ovat sopivia työpaikalle tai sopivia lapsille.

### Miten se toimii?

Nyt, miten meta-kehotteet toimivat?

Meta-kehotteet ovat tekstikehotteita, joita käytetään ohjaamaan Generatiivisen AI-mallin tuottamaa tulosta, ne sijoitetaan tekstikehotteen eteen ja niitä käytetään ohjaamaan mallin tuottamaa tulosta ja ne upotetaan sovelluksiin ohjaamaan mallin tuottamaa tulosta. Yhdistäen kehoteinputin ja meta-kehoteinputin yhdeksi tekstikehotteeksi.

Yksi esimerkki meta-kehotteesta voisi olla seuraava:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nyt katsotaan, miten voimme käyttää meta-kehotteita demossamme.

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

Yllä olevasta kehotteesta voit nähdä, miten kaikki luodut kuvat ottavat huomioon meta-kehotteen.

## Tehtävä - annetaan oppilaille mahdollisuus

Esittelimme Edu4All:n tämän oppitunnin alussa. Nyt on aika antaa oppilaille mahdollisuus luoda kuvia arviointejaan varten.

Oppilaat luovat kuvia arviointejaan varten sisältäen monumentteja, tarkalleen mitä monumentteja, on oppilaiden päätettävissä. Oppilaita pyydetään käyttämään luovuuttaan tässä tehtävässä sijoittamaan nämä monumentit eri konteksteihin.

## Ratkaisu

Tässä on yksi mahdollinen ratkaisu:

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

## Hyvää työtä! Jatka oppimistasi

Tämän oppitunnin jälkeen tutustu [Generatiivinen AI -oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generatiivisen AI:n tietämyksesi kehittämistä!

Siirry oppituntiin 10, jossa tarkastelemme, kuinka [rakentaa AI-sovelluksia low-code-työkaluilla](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomaa, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa olevan auktoritatiivinen lähde. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.