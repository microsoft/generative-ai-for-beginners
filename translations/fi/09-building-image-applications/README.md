# Kuvantuotantosovellusten rakentaminen

[![Kuvantuotantosovellusten rakentaminen](../../../translated_images/fi/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Kielenmallit eivät rajoitu pelkkään tekstintuotantoon. On mahdollista luoda kuvia tekstikuvausten pohjalta. Kuvien hyödyntäminen voi olla erittäin hyödyllistä monilla aloilla, kuten lääketieteessä, arkkitehtuurissa, matkailussa, pelikehityksessä ja muussa. Tässä luvussa tutustumme kahteen suosituimpaan kuvantuotantomalliin, DALL-Een ja Midjourneyhin.

## Johdanto

Tässä oppitunnissa käsittelemme:

- Kuvantuotantoa ja miksi se on hyödyllistä.
- DALL-E ja Midjourney, mitä ne ovat ja miten ne toimivat.
- Kuinka rakentaisit kuvantuotantosovelluksen.

## Oppimistavoitteet

Oppitunnin jälkeen osaat:

- Rakentaa kuvantuotantosovelluksen.
- Määritellä sovelluksellesi rajat meta-kehotteilla.
- Työskennellä DALL-E:n ja Midjourneyn kanssa.

## Miksi rakentaa kuvantuotantosovellus?

Kuvantuotantosovellukset ovat erinomainen tapa tutkia Generatiivisen tekoälyn kykyjä. Niitä voi käyttää esimerkiksi seuraaviin tarkoituksiin:

- **Kuvien muokkaus ja synteesi**. Voit luoda kuvia monenlaisiin käyttötarkoituksiin, kuten kuvanmuokkaukseen ja kuvasynteesiin.

- **Soveltaminen useille toimialoille**. Kuvia voidaan myös hyödyntää monilla toimialoilla, kuten lääketieteessä, matkailussa, pelikehityksessä ja muissa.

## Tilanne: Edu4All

Tässä oppitunnissa jatkamme startup-yrityksemme Edu4All:n kanssa työskentelyä. Oppilaat luovat kuvia omiin tehtäviinsä; millaisia kuvia luovat, on heidän päätettävissään, mutta ne voivat olla vaikkapa omia satujen kuvituksia, uusia hahmoja tarinaansa varten tai avustaa ideoiden ja konseptien visualisoinnissa.

Tässä esimerkkejä, mitä Edu4Allin oppilaat voisivat luoda esimerkiksi monumentteihin liittyvän luokan tehtävissä:

![Edu4All startup, luokka monumenteista, Eiffel-torni](../../../translated_images/fi/startup.94d6b79cc4bb3f5a.webp)

käyttäen kehotetta kuten

> "Koira Eiffel-tornin vieressä varhaisessa aamun auringonvalossa"

## Mitä ovat DALL-E ja Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ja [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ovat kaksi suosituimmista kuvantuotantomalleista, joiden avulla voit käyttää kehotteita kuvien luomiseen.

### DALL-E

Aloitetaan DALL-E:stä, joka on Generatiivinen tekoälymalli, joka luo kuvia tekstikuvauksista.

> [DALL-E yhdistää kaksi mallia, CLIPin ja diffusoidun huomion](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** on malli, joka tuottaa upotuksia, eli numeerisia edustuksia datasta, kuvista ja tekstistä.

- **Diffusoitu huomio** on malli, joka luo kuvia upotuksista. DALL-E koulutetaan kuvien ja tekstin datamassalla, ja sitä voi käyttää luomaan kuvia tekstikuvauksista. Esimerkiksi DALL-E voi luoda kuvia kissasta hatun kanssa tai koirasta, jolla on mohikaani.

### Midjourney

Midjourney toimii pitkälti samalla tavalla kuin DALL-E: se luo kuvia tekstikehotteista. Midjourneyllä voi myös luoda kuvia kehotteilla kuten ”kissa hatussa” tai ”mohikaanilla oleva koira”.

![Midjourneyn tuottama kuva, mekaaninen kyyhky](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kuvan lähde Wikipedia, kuva luotu Midjourneyllä_

## Miten DALL-E ja Midjourney toimivat

Aloitetaan [DALL-E:stä](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E on Generatiivinen tekoälymalli, joka perustuu transformeri-arkkitehtuuriin ja on _autoregressiivinen transformer_.

_Autoregressiivinen transformer_ määrittelee, miten malli luo kuvia tekstikuvauksista: se generoi kuvan pikseli pikseliltä ja käyttää kunkin luodun pikselin tietoa seuraavan pikselin luomiseksi. Prosessi etenee läpi useiden kerrosten neuroverkossa, kunnes kuva on valmis.

Tämän prosessin avulla DALL-E hallitsee kuvan ominaisuuksia, esineitä, piirteitä ja muuta. DALL-E 2:lla ja 3:lla on vielä tarkempi hallinta tuotetusta kuvasta.

## Ensimmäisen kuvantuotantosovelluksesi rakentaminen

Mitä tarvitaan kuvantuotantosovelluksen rakentamiseen? Tarvitset seuraavat kirjastot:

- **python-dotenv**, tätä kirjastoa suositellaan salaisten tietojen säilyttämiseen _.env_-tiedostossa erillään koodista.
- **openai**, tätä kirjastoa käytät kommunikoidessasi OpenAI-rajapinnan kanssa.
- **pillow**, kuvien käsittelyyn Pythonissa.
- **requests**, HTTP-pyyntöjen tekemiseen.

## Luo ja ota käyttöön Azure OpenAI -malli

Jos et ole vielä tehnyt niin, seuraa ohjeita [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) -sivulla
luodaksesi Azure OpenAI -resurssin ja mallin. Valitse malliksi **gpt-image-1** (tämän hetken Azure OpenAI -kuvamalli; DALL-E 3 on vanhentunut eikä sitä enää tarjota uusissa käyttöönotossa).

## Luo sovellus

1. Luo tiedosto _.env_ seuraavalla sisällöllä:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Etsi nämä tiedot Azure OpenAI Foundry Portaalista resurssisi "Deployments"-osiosta.

1. Kerää yllä mainitut kirjastot tiedostoon _requirements.txt_ seuraavasti:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Luo virtuaaliympäristö ja asenna kirjastot:

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

1. Lisää seuraava koodi tiedostoon _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # importoi dotenv
    dotenv.load_dotenv()
    
    # konfiguroi Azure OpenAI -palvelun asiakas
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Luo kuva käyttämällä kuvageneraation API:a
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Aseta hakemisto tallennetulle kuvalle
        image_dir = os.path.join(os.curdir, 'images')

        # Jos hakemistoa ei ole, luo se
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Alusta kuvan polku (huomaa, että tiedostotyyppi tulisi olla png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Hae generoitu kuva
        image_url = generation_response.data[0].url  # poimi kuvan URL vastauksesta
        generated_image = requests.get(image_url).content  # lataa kuva
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Näytä kuva oletuskuvankatseluohjelmassa
        image = Image.open(image_path)
        image.show()

    # käsittele poikkeukset
    except openai.BadRequestError as err:
        print(err)
   ```

Selitetään tämä koodi:

- Ensin tuomme tarvitsemamme kirjastot, mukaan lukien OpenAI-kirjaston, dotenv-kirjaston, requests-kirjaston ja Pillow-kirjaston.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Seuraavaksi luemme ympäristömuuttujat _.env_-tiedostosta.

  ```python
  # tuo dotenv
  dotenv.load_dotenv()
  ```

- Tämän jälkeen konfiguroimme Azure OpenAI -palvelun asiakkaan

  ```python
  # Hae päätepiste ja avain ympäristömuuttujista
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Seuraavaksi generoimme kuvan:

  ```python
  # Luo kuva käyttämällä kuvanluonti-API:a
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Yllä oleva koodi palauttaa JSON-objektin, joka sisältää luodun kuvan URL-osoitteen. Sivusto-osoitetta voidaan käyttää kuvan lataamiseen ja tallentamiseen tiedostoon.

- Lopuksi avaamme kuvan ja käytämme tavallista kuvan katseluohjelmaa sen näyttämiseen:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Lisätietoja kuvan muodostamisesta

Tarkastellaan lähemmin kuvan muodostamista koodia:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** on tekstikehote, jota käytetään kuvan luomiseen. Tässä tapauksessa käytämme kehottetta "Pupu hevosen selässä, pitää tikkaria, sumuisella niityllä jossa kasvaa narsisseja".
- **size** määrittää luotavan kuvan koon. Tässä tapauksessa luomme 1024x1024 pikselin kuvan.
- **n** on luotavien kuvien lukumäärä. Tässä tapauksessa luomme kaksi kuvaa.
- **temperature** on parametri, joka säätelee generatiivisen tekoälymallin tuotosten satunnaisuutta. Lämpötilaarvo on välillä 0 ja 1, jossa 0 tarkoittaa determinististä (ennustettua) tuotosta ja 1 satunnaista tuotosta. Oletusarvo on 0,7.

Kuvilla voi tehdä vielä monia muitakin asioita, joista keskustelemme seuraavassa osassa.

## Kuvantuotannon lisäominaisuudet

Olet nähnyt, kuinka pystyimme luomaan kuvan muutamalla rivillä Pythonia. Kuvilla voi kuitenkin tehdä seuraavia lisätoimia:

Voit myös:

- **Tehdä muokkauksia**. Antamalla olemassa olevalle kuvalle maskin ja kehotteen voit muuttaa kuvaa. Voit esimerkiksi lisätä jotakin kuvan tietylle alueelle. Kuvittele pupukuvamme, johon voit lisätä hatun. Teet tämän antamalla kuvan, maskin (joka määrittää muutettavan alueen) ja tekstikehotteen, joka kertoo, mitä tulee tehdä.
> Huom: tätä ei tueta DALL-E 3:ssa.
 
Tässä esimerkki GPT Imagella:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Peruskuva sisältäisi vain altaallisen oleskelutilan, mutta lopullisessa kuvassa olisi mukana myös flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/fi/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fi/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fi/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Luo variaatioita**. Ajatuksena on ottaa olemassa oleva kuva ja pyytää siitä variaatioiden luomista. Variatioita luodessasi annat kuvan ja tekstikehotteen ja koodin toimii seuraavasti:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Huomioi, että tätä tukee vain OpenAI:n DALL-E 2 -malli, ei gpt-image-1.

## Lämpötila

Lämpötila on parametri, joka säätelee generatiivisen tekoälymallin tuotosten satunnaisuutta. Arvo on välillä 0 ja 1, jossa 0 tarkoittaa determinististä eli ennustettavaa lopputulosta ja 1 satunnaista. Oletusarvo on 0,7.

Katsotaan esimerkki lämpötilan vaikutuksesta ajamalla sama kehotte kahdesti:

> Kehote: "Pupu hevosen selässä, pitää tikkaria, sumuisella niityllä jossa kasvaa narsisseja"

![Pupu hevosen selässä, versio 1](../../../translated_images/fi/v1-generated-image.a295cfcffa3c13c2.webp)

Ajetaan sama kehote uudestaan nähdäksesi, ettei saatu samaa kuvaa kahdesti:

![Luotu kuva pupusta hevosen selässä](../../../translated_images/fi/v2-generated-image.33f55a3714efe61d.webp)

Kuten näet, kuvat ovat samantyyppisiä, mutta eivät identtisiä. Yritetään muuttaa lämpötilan arvoksi 0,1 ja katsotaan, mitä tapahtuu:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Syötä kehotetekstisi tähän
        size='1024x1024',
        n=2
    )
```

### Lämpötilan muuttaminen

Yritetään saada vastaus deterministisemmaksi. Voimme havaita luoduista kahdesta kuvasta, että ensimmäisessä on pupu ja toisessa hevonen, joten kuvat eroavat paljon toisistaan.

Muutetaan siis koodiamme ja asetetaan lämpötilaksi 0 seuraavasti:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Syötä kehotetekstisi tähän
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Kun ajat tämän koodin, saat nämä kaksi kuvaa:

- ![Lämpötila 0, v1](../../../translated_images/fi/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Lämpötila 0, v2](../../../translated_images/fi/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Tässä voit selvästi nähdä, että kuvat muistuttavat toisiaan enemmän.

## Kuinka määritellä sovelluksesi rajat metakehotteilla

Demossamme voimme jo luoda kuvia asiakkaillemme. Kuitenkin meidän täytyy asettaa sovellukselle rajat.

Esimerkiksi emme halua luoda kuvia, jotka eivät ole sopivia työympäristöön tai jotka eivät sovellu lapsille.

Tämä voidaan tehdä _metakehoteilla_. Metakehotteet ovat tekstikehotteita, joiden avulla hallitaan generatiivisen tekoälymallin tuotosdataa. Esimerkiksi metakehotteilla voidaan varmistaa, että luodut kuvat ovat sopivia työympäristöön tai lapsille.

### Miten se toimii?

Miten siis metakehotteet toimivat?

Metakehotteet ovat tekstikehotteita, joita käytetään hallitsemaan generatiivisen tekoälymallin tuotoksia. Ne sijoitetaan tekstikehotteen eteen, ja niitä käytetään ohjaamaan mallin tuotosta sekä upotetaan sovelluksiin hallitsemaan mallin tuotoksia. Näin tekstikehote ja metakehote on kapseloitu yhdeksi tekstikehotteeksi.

Yksi esimerkki metakehotteesta voisi olla seuraava:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Katsotaan nyt, miten voimme käyttää metakehotteita demossamme.

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

# TODO lisää pyyntö kuvan luomiseksi
```

Yllä olevasta kehotteesta näet, miten kaikki luodut kuvat ottavat metakehotteen huomioon.

## Tehtävä – annetaan opiskelijoille mahdollisuus

Esittelimme Edu4All:n tämän oppitunnin alussa. Nyt on aika antaa opiskelijoille mahdollisuus luoda kuvia omiin arviointeihinsa.


Oppilaat luovat kuvia arviointejaan varten, jotka sisältävät monumentteja; tarkemmin mitä monumentteja, se jää oppilaiden päätettäväksi. Oppilaita pyydetään käyttämään luovuuttaan tässä tehtävässä sijoittaakseen nämä monumentit erilaisiin yhteyksiin.

## Ratkaisu

Tässä on yksi mahdollinen ratkaisu:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Hae päätepiste ja avain ympäristömuuttujista
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
    # Luo kuva käyttämällä kuvageneraattorin APIa
    generation_response = client.images.generate(
        prompt=prompt,    # Syötä kehotetekstisi tähän
        size='1024x1024',
        n=1,
    )
    # Aseta tallennetun kuvan hakemisto
    image_dir = os.path.join(os.curdir, 'images')

    # Jos hakemistoa ei ole, luo se
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Alusta kuvatiedoston polku (huomaa, että tiedostotyyppi tulisi olla png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Hae luotu kuva
    image_url = generation_response.data[0].url  # poimi kuvan URL vastauskentästä
    generated_image = requests.get(image_url).content  # lataa kuva
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Näytä kuva oletuskuvankatseluohjelmassa
    image = Image.open(image_path)
    image.show()

# käsittele poikkeukset
except openai.BadRequestError as err:
    print(err)
```

## Hienoa työtä! Jatka oppimista

Tämän oppitunnin jälkeen tutustu [Generative AI -oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietämyksesi kehittämistä!

Siirry Oppitunnille 10, jossa tarkastelemme, kuinka [rakentaa tekoälysovelluksia vähän koodilla](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->