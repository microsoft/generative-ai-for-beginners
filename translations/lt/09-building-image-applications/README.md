<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T20:20:32+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "lt"
}
-->
# Vaizdų generavimo programų kūrimas

[![Vaizdų generavimo programų kūrimas](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.lt.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM modeliai gali generuoti ne tik tekstą. Taip pat galima kurti vaizdus pagal tekstinius aprašymus. Vaizdai kaip modalumas yra labai naudingi įvairiose srityse – nuo medicinos technologijų, architektūros, turizmo, žaidimų kūrimo ir dar daugiau. Šiame skyriuje susipažinsime su dviem populiariausiais vaizdų generavimo modeliais: DALL-E ir Midjourney.

## Įvadas

Šioje pamokoje aptarsime:

- Vaizdų generavimą ir jo naudą.
- DALL-E ir Midjourney: kas tai ir kaip jie veikia.
- Kaip sukurti vaizdų generavimo programą.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Sukurti vaizdų generavimo programą.
- Apibrėžti programos ribas naudojant metapromptus.
- Dirbti su DALL-E ir Midjourney.

## Kodėl verta kurti vaizdų generavimo programą?

Vaizdų generavimo programos – puikus būdas išbandyti generatyvaus dirbtinio intelekto galimybes. Jos gali būti naudojamos, pavyzdžiui:

- **Vaizdų redagavimui ir sintezei**. Galite generuoti vaizdus įvairiems poreikiams, pavyzdžiui, redaguoti ar kurti naujus vaizdus.

- **Pritaikymas įvairiose industrijose**. Tokios programos gali būti naudojamos kuriant vaizdus medicinos technologijoms, turizmui, žaidimų kūrimui ir kitoms sritims.

## Scenarijus: Edu4All

Šioje pamokoje toliau dirbsime su savo startuoliu Edu4All. Mokiniai kurs vaizdus savo užduotims – kokius vaizdus jie kurs, priklauso nuo jų pačių: tai gali būti iliustracijos pasakai, naujo personažo sukūrimas ar idėjų ir koncepcijų vizualizavimas.

Pavyzdžiui, jei Edu4All mokiniai pamokoje nagrinėja paminklus, jie galėtų sukurti tokį vaizdą:

![Edu4All startuolis, pamoka apie paminklus, Eifelio bokštas](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.lt.png)

naudodami tokį promptą:

> „Šuo šalia Eifelio bokšto ankstyvą rytą saulės šviesoje“

## Kas yra DALL-E ir Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ir [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) – du populiariausi vaizdų generavimo modeliai, leidžiantys kurti vaizdus pagal tekstinius promptus.

### DALL-E

Pradėkime nuo DALL-E – tai generatyvaus DI modelis, kuris kuria vaizdus pagal tekstinius aprašymus.

> [DALL-E sudaro du modeliai: CLIP ir diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** – modelis, kuris generuoja embeddingus, t. y. skaitmeninius duomenų atvaizdus, iš vaizdų ir teksto.

- **Diffused attention** – modelis, kuris kuria vaizdus iš embeddingų. DALL-E apmokytas su vaizdų ir tekstų duomenų rinkiniu, todėl gali generuoti vaizdus pagal tekstinius aprašymus. Pavyzdžiui, DALL-E gali sukurti vaizdą, kuriame katinas su skrybėle arba šuo su mohawk šukuosena.

### Midjourney

Midjourney veikia panašiai kaip DALL-E – generuoja vaizdus pagal tekstinius promptus. Midjourney taip pat galima naudoti su promptais, tokiais kaip „katinas su skrybėle“ ar „šuo su mohawk šukuosena“.

![Midjourney sugeneruotas vaizdas, mechaninis balandis](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Vaizdo autorius Wikipedia, vaizdas sugeneruotas Midjourney_

## Kaip veikia DALL-E ir Midjourney

Pirmiausia, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E – generatyvaus DI modelis, paremtas transformer architektūra su _autoregresiniu transformeriu_.

_Autoregresinis transformeris_ apibrėžia, kaip modelis generuoja vaizdus pagal tekstinius aprašymus: jis kuria vaizdą po vieną pikselį, naudodamas jau sugeneruotus pikselius kitų pikselių generavimui. Taip vaizdas kuriamas per kelis neuroninio tinklo sluoksnius, kol gaunamas pilnas rezultatas.

Tokiu būdu DALL-E gali kontroliuoti vaizde esančius atributus, objektus, savybes ir kt. DALL-E 2 ir 3 versijos leidžia dar labiau kontroliuoti generuojamą vaizdą.

## Pirmoji vaizdų generavimo programa

Ką reikia turėti, norint sukurti vaizdų generavimo programą? Reikės šių bibliotekų:

- **python-dotenv** – labai rekomenduojama naudoti šią biblioteką, kad slapti duomenys būtų saugomi _.env_ faile, atskirai nuo kodo.
- **openai** – ši biblioteka naudojama darbui su OpenAI API.
- **pillow** – darbui su vaizdais Python aplinkoje.
- **requests** – HTTP užklausų siuntimui.

## Sukurkite ir įdiekite Azure OpenAI modelį

Jei dar to nepadarėte, vadovaukitės [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) instrukcijomis,
kad sukurtumėte Azure OpenAI resursą ir modelį. Pasirinkite DALL-E 3 kaip modelį.  

## Sukurkite programą

1. Sukurkite _.env_ failą su šiuo turiniu:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Šią informaciją rasite Azure OpenAI Foundry portale, savo resurso „Deployments“ skiltyje.

1. Surinkite aukščiau minėtas bibliotekas į _requirements.txt_ failą taip:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Toliau sukurkite virtualią aplinką ir įdiekite bibliotekas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows naudotojams šios komandos leis sukurti ir aktyvuoti virtualią aplinką:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Įrašykite šį kodą į _app.py_ failą:

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

Paaiškinkime šį kodą:

- Pirmiausia importuojame reikalingas bibliotekas: OpenAI, dotenv, requests ir Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Toliau įkeliame aplinkos kintamuosius iš _.env_ failo.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Po to konfigūruojame Azure OpenAI paslaugos klientą.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Toliau generuojame vaizdą:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Šis kodas grąžina JSON objektą su sugeneruoto vaizdo URL. Galime naudoti šį URL, kad atsisiųstume vaizdą ir išsaugotume jį faile.

- Galiausiai atidarome vaizdą ir rodome jį standartiniame vaizdų peržiūros lange:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Daugiau apie vaizdo generavimą

Pažvelkime detaliau į vaizdo generavimo kodą:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** – tekstinis promptas, pagal kurį generuojamas vaizdas. Šiuo atveju naudojamas promptas „Triušis ant arklio, laikantis saldainį, rūke apaugusioje pievoje, kur auga narcizai“.
- **size** – generuojamo vaizdo dydis. Šiuo atveju – 1024x1024 pikselių.
- **n** – generuojamų vaizdų skaičius. Šiuo atveju – du vaizdai.
- **temperature** – parametras, kontroliuojantis generatyvaus DI modelio atsakymo atsitiktinumą. Temperatūra – nuo 0 iki 1: 0 reiškia, kad atsakymas bus deterministinis, 1 – visiškai atsitiktinis. Numatyta reikšmė – 0,7.

Yra ir daugiau galimybių, kurias aptarsime kitame skyriuje.

## Papildomos vaizdų generavimo galimybės

Matėte, kaip galima sugeneruoti vaizdą vos keliomis Python eilutėmis. Tačiau su vaizdais galima nuveikti ir daugiau.

Galite atlikti šiuos veiksmus:

- **Redaguoti vaizdus**. Pateikę esamą vaizdą, kaukę ir promptą, galite pakeisti vaizdą. Pavyzdžiui, galite pridėti objektą tam tikroje vaizdo dalyje. Tarkime, norite mūsų triušiui uždėti skrybėlę – tam reikia pateikti vaizdą, kaukę (nurodančią keičiamą sritį) ir tekstinį promptą, kas turi būti padaryta.
> Pastaba: ši funkcija DALL-E 3 modelyje nepalaikoma.

Štai pavyzdys naudojant GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Pradiniame vaizde matytume tik poilsio zoną su baseinu, o galutiniame – jau ir flamingą:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Kurti variacijas**. Galite paimti esamą vaizdą ir paprašyti sukurti jo variacijas. Tam reikia pateikti vaizdą, tekstinį promptą ir naudoti tokį kodą:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Pastaba: ši funkcija palaikoma tik OpenAI

## Temperatūra

Temperatūra – parametras, kontroliuojantis generatyvaus DI modelio atsakymo atsitiktinumą. Temperatūra – nuo 0 iki 1: 0 reiškia, kad atsakymas bus deterministinis, 1 – visiškai atsitiktinis. Numatyta reikšmė – 0,7.

Pažiūrėkime, kaip veikia temperatūra, paleisdami šį promptą du kartus:

> Promptas: „Triušis ant arklio, laikantis saldainį, rūke apaugusioje pievoje, kur auga narcizai“

![Triušis ant arklio su saldainiu, 1 versija](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.lt.png)

Dabar paleiskime tą patį promptą dar kartą – pamatysime, kad vaizdas bus kitoks:

![Sugeneruotas triušio ant arklio vaizdas](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.lt.png)

Kaip matote, vaizdai panašūs, bet ne identiški. Pabandykime pakeisti temperatūrą į 0,1 ir pažiūrėkime, kas bus:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperatūros keitimas

Pabandykime padaryti atsakymą labiau deterministinį. Iš dviejų sugeneruotų vaizdų matome, kad pirmame yra triušis, antrame – arklys, tad skirtumai dideli.

Todėl pakeiskime kodą ir nustatykime temperatūrą į 0:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Dabar paleidus kodą gausite šiuos du vaizdus:

- ![Temperatūra 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.lt.png)
- ![Temperatūra 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.lt.png)

Aiškiai matyti, kad vaizdai daug labiau panašūs.

## Kaip apibrėžti programos ribas naudojant metapromptus

Mūsų demonstracijoje jau galime generuoti vaizdus klientams. Tačiau reikia nustatyti tam tikras ribas.

Pavyzdžiui, nenorime generuoti vaizdų, kurie netinkami darbui ar vaikams.

Tam naudojami _metapromptai_. Metapromptai – tai tekstiniai promptai, skirti kontroliuoti generatyvaus DI modelio atsakymą. Pavyzdžiui, galime naudoti metapromptus, kad generuojami vaizdai būtų tinkami darbui ar vaikams.

### Kaip tai veikia?

Kaip veikia metapromptai?

Metapromptai – tai tekstiniai promptai, kurie dedami prieš pagrindinį promptą ir naudojami modelio atsakymui kontroliuoti. Jie integruojami į programą, kad ribotų modelio atsakymus. Promptas ir metapromptas sujungiami į vieną tekstinį promptą.

Štai pavyzdys metapromptui:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Dabar pažiūrėkime, kaip galime naudoti metapromptus savo demonstracijoje.

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

Iš šio prompto matyti, kad visi kuriami vaizdai atsižvelgia į metapromptą.

## Užduotis – įgalinkime mokinius

Pamokos pradžioje pristatėme Edu4All. Dabar laikas įgalinti mokinius generuoti vaizdus savo užduotims.

Mokiniai kurs vaizdus, kuriuose bus paminklai – kokie paminklai, priklauso nuo jų pačių. Mokiniai raginami pasitelkti kūrybiškumą ir pavaizduoti paminklus įvairiuose kontekstuose.

## Sprendimas

Štai vienas galimas sprendimas:

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

## Puiku! Tęskite mokymąsi
Baigę šią pamoką, peržiūrėkite mūsų [Generatyvaus dirbtinio intelekto mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyvų DI!

Pereikite prie 10 pamokos, kurioje nagrinėsime, kaip [kurti DI programas naudojant mažai kodo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.