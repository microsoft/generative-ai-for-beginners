<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-18T02:27:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "lt"
}
-->
# Vaizdų generavimo programų kūrimas

[![Vaizdų generavimo programų kūrimas](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.lt.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM modeliai nėra skirti vien tik tekstų generavimui. Taip pat galima generuoti vaizdus iš tekstinių aprašymų. Vaizdai kaip modalumas gali būti labai naudingi įvairiose srityse, tokiose kaip medicinos technologijos, architektūra, turizmas, žaidimų kūrimas ir kt. Šiame skyriuje aptarsime du populiariausius vaizdų generavimo modelius – DALL-E ir Midjourney.

## Įvadas

Šioje pamokoje aptarsime:

- Vaizdų generavimą ir kodėl jis naudingas.
- DALL-E ir Midjourney: kas tai yra ir kaip jie veikia.
- Kaip sukurti vaizdų generavimo programą.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Sukurti vaizdų generavimo programą.
- Apibrėžti savo programos ribas naudojant meta promptus.
- Dirbti su DALL-E ir Midjourney.

## Kodėl verta kurti vaizdų generavimo programą?

Vaizdų generavimo programos yra puikus būdas tyrinėti generatyvinio dirbtinio intelekto galimybes. Jos gali būti naudojamos, pavyzdžiui:

- **Vaizdų redagavimas ir sintezė**. Galite generuoti vaizdus įvairiems tikslams, tokiems kaip vaizdų redagavimas ar sintezė.

- **Taikymas įvairiose pramonės šakose**. Taip pat galima generuoti vaizdus įvairioms pramonės šakoms, tokioms kaip medicinos technologijos, turizmas, žaidimų kūrimas ir kt.

## Scenarijus: Edu4All

Šios pamokos metu toliau dirbsime su mūsų startuoliu Edu4All. Studentai kurs vaizdus savo užduotims – kokius vaizdus kurti, priklauso nuo jų pačių, tačiau tai gali būti iliustracijos jų pasakoms, naujo personažo kūrimas jų istorijai arba pagalba vizualizuojant jų idėjas ir koncepcijas.

Štai ką, pavyzdžiui, galėtų sukurti Edu4All studentai, jei klasėje dirbtų su paminklais:

![Edu4All startuolis, pamoka apie paminklus, Eifelio bokštas](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.lt.png)

naudodami tokį promptą:

> "Šuo šalia Eifelio bokšto ankstyvo ryto saulės šviesoje"

## Kas yra DALL-E ir Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ir [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) yra du populiariausi vaizdų generavimo modeliai, leidžiantys naudoti promptus vaizdams generuoti.

### DALL-E

Pradėkime nuo DALL-E – tai generatyvinio dirbtinio intelekto modelis, kuris generuoja vaizdus iš tekstinių aprašymų.

> [DALL-E yra dviejų modelių, CLIP ir difuzinės dėmesio sistemos, derinys](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** – tai modelis, kuris generuoja įterpimus, t. y. duomenų skaitines reprezentacijas, iš vaizdų ir tekstų.

- **Difuzinė dėmesio sistema** – tai modelis, kuris generuoja vaizdus iš įterpimų. DALL-E yra apmokytas vaizdų ir tekstų duomenų rinkiniu ir gali būti naudojamas vaizdams generuoti iš tekstinių aprašymų. Pavyzdžiui, DALL-E gali generuoti vaizdus, kuriuose katė su skrybėle arba šuo su mohawk šukuosena.

### Midjourney

Midjourney veikia panašiai kaip DALL-E – jis generuoja vaizdus iš tekstinių promptų. Midjourney taip pat gali būti naudojamas vaizdams generuoti naudojant promptus, tokius kaip „katė su skrybėle“ arba „šuo su mohawk šukuosena“.

![Vaizdas, sukurtas Midjourney, mechaninis balandis](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Vaizdo autorius Wikipedia, vaizdas sukurtas Midjourney_

## Kaip veikia DALL-E ir Midjourney

Pirmiausia, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E yra generatyvinio dirbtinio intelekto modelis, pagrįstas transformatorių architektūra su _autoregresiniu transformatoriumi_.

_Autoregresinis transformatorius_ apibrėžia, kaip modelis generuoja vaizdus iš tekstinių aprašymų – jis generuoja vieną pikselį vienu metu, o tada naudoja sugeneruotus pikselius kitam pikseliui generuoti. Procesas vyksta per kelis neuroninio tinklo sluoksnius, kol vaizdas tampa pilnas.

Šio proceso metu DALL-E kontroliuoja atributus, objektus, charakteristikas ir kitus elementus generuojamame vaizde. Tačiau DALL-E 2 ir 3 turi daugiau kontrolės galimybių generuojant vaizdą.

## Pirmos vaizdų generavimo programos kūrimas

Taigi, ko reikia norint sukurti vaizdų generavimo programą? Jums reikės šių bibliotekų:

- **python-dotenv** – labai rekomenduojama naudoti šią biblioteką, kad jūsų slaptažodžiai būtų saugomi _.env_ faile, atskirai nuo kodo.
- **openai** – ši biblioteka naudojama sąveikai su OpenAI API.
- **pillow** – darbui su vaizdais Python kalboje.
- **requests** – padeda atlikti HTTP užklausas.

## Sukurkite ir įdiekite Azure OpenAI modelį

Jei dar to nepadarėte, vadovaukitės [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) puslapyje pateiktomis instrukcijomis, kad sukurtumėte Azure OpenAI resursą ir modelį. Pasirinkite DALL-E 3 kaip modelį.

## Sukurkite programą

1. Sukurkite failą _.env_ su šiuo turiniu:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Šią informaciją rasite Azure OpenAI Foundry portale savo resurso „Diegimų“ skiltyje.

1. Surinkite aukščiau nurodytas bibliotekas į failą _requirements.txt_ taip:

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

   Windows operacinėje sistemoje naudokite šias komandas, kad sukurtumėte ir aktyvuotumėte virtualią aplinką:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Į failą _app.py_ pridėkite šį kodą:

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

- Pirmiausia importuojame reikalingas bibliotekas, įskaitant OpenAI biblioteką, dotenv biblioteką, requests biblioteką ir Pillow biblioteką.

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

  Aukščiau pateiktas kodas grąžina JSON objektą, kuriame yra sugeneruoto vaizdo URL. Šį URL galima naudoti vaizdui atsisiųsti ir išsaugoti faile.

- Galiausiai atidarome vaizdą ir naudojame standartinį vaizdų peržiūros įrankį, kad jį parodytume:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Daugiau informacijos apie vaizdo generavimą

Pažvelkime į kodą, kuris generuoja vaizdą, išsamiau:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** – tai tekstinis promptas, naudojamas vaizdui generuoti. Šiuo atveju naudojame promptą „Triušis ant arklio, laikantis ledinuką, rūke apgaubtoje pievoje, kurioje auga narcizai“.
- **size** – tai generuojamo vaizdo dydis. Šiuo atveju generuojame vaizdą, kurio dydis yra 1024x1024 pikseliai.
- **n** – tai generuojamų vaizdų skaičius. Šiuo atveju generuojame du vaizdus.
- **temperature** – tai parametras, kontroliuojantis generatyvinio dirbtinio intelekto modelio išvesties atsitiktinumą. Temperatūra yra reikšmė nuo 0 iki 1, kur 0 reiškia, kad išvestis yra deterministinė, o 1 – kad išvestis yra atsitiktinė. Numatytasis reikšmė yra 0.7.

Yra daugiau dalykų, kuriuos galite daryti su vaizdais, apie tai kalbėsime kitame skyriuje.

## Papildomos vaizdų generavimo galimybės

Jūs jau matėte, kaip galime sugeneruoti vaizdą naudodami kelias Python kodo eilutes. Tačiau yra daugiau dalykų, kuriuos galite daryti su vaizdais.

Taip pat galite:

- **Redaguoti vaizdus**. Pateikdami esamą vaizdą, kaukę ir promptą, galite pakeisti vaizdą. Pavyzdžiui, galite pridėti kažką prie tam tikros vaizdo dalies. Įsivaizduokite mūsų triušio vaizdą – galite pridėti skrybėlę triušiui. Tai daroma pateikiant vaizdą, kaukę (nurodant sritį, kurioje reikia pakeitimų) ir tekstinį promptą, kuriame nurodoma, ką reikia padaryti.
> Pastaba: tai nepalaikoma DALL-E 3.

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

  Pagrindiniame vaizde būtų tik poilsio zona su baseinu, tačiau galutiniame vaizde atsirastų flamingas:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.lt.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.lt.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.lt.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Kurti variacijas**. Idėja yra ta, kad paimamas esamas vaizdas ir prašoma sukurti jo variacijas. Norėdami sukurti variaciją, pateikiate vaizdą ir tekstinį promptą bei kodą, kaip parodyta:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Pastaba: tai palaikoma tik OpenAI.

## Temperatūra

Temperatūra yra parametras, kontroliuojantis generatyvinio dirbtinio intelekto modelio išvesties atsitiktinumą. Temperatūra yra reikšmė nuo 0 iki 1, kur 0 reiškia, kad išvestis yra deterministinė, o 1 – kad išvestis yra atsitiktinė. Numatytasis reikšmė yra 0.7.

Pažvelkime į pavyzdį, kaip veikia temperatūra, paleisdami šį promptą du kartus:

> Promptas: „Triušis ant arklio, laikantis ledinuką, rūke apgaubtoje pievoje, kurioje auga narcizai“

![Triušis ant arklio, laikantis ledinuką, versija 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.lt.png)

Dabar paleiskime tą patį promptą dar kartą, kad pamatytume, jog negausime tokio paties vaizdo du kartus:

![Sugeneruotas triušio ant arklio vaizdas](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.lt.png)

Kaip matote, vaizdai yra panašūs, bet ne identiški. Pabandykime pakeisti temperatūros reikšmę į 0.1 ir pažiūrėkime, kas nutiks:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperatūros keitimas

Pabandykime padaryti išvestį labiau deterministinę. Galime pastebėti iš dviejų sugeneruotų vaizdų, kad pirmame vaizde yra triušis, o antrame – arklys, todėl vaizdai labai skiriasi.

Todėl pakeiskime savo kodą ir nustatykime temperatūrą į 0, kaip parodyta:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Dabar, kai paleisite šį kodą, gausite šiuos du vaizdus:

- ![Temperatūra 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.lt.png)
- ![Temperatūra 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.lt.png)

Čia aiškiai matyti, kaip vaizdai labiau panašūs vienas į kitą.

## Kaip apibrėžti savo programos ribas naudojant meta promptus

Su mūsų demonstracija jau galime generuoti vaizdus savo klientams. Tačiau mums reikia sukurti tam tikras ribas savo programai.

Pavyzdžiui, nenorime generuoti vaizdų, kurie nėra tinkami darbui ar netinkami vaikams.

Tai galime padaryti naudodami _meta promptus_. Meta promptai yra tekstiniai promptai, naudojami generatyvinio dirbtinio intelekto modelio išvesties kontrolei. Pavyzdžiui, galime naudoti meta promptus, kad kontroliuotume išvestį ir užtikrintume, jog sugeneruoti vaizdai būtų tinkami darbui ar vaikams.

### Kaip tai veikia?

Kaip veikia meta promptai?

Meta promptai yra tekstiniai promptai, naudojami generatyvinio dirbtinio intelekto modelio išvesties kontrolei. Jie yra pozicionuojami prieš tekstinį promptą ir naudojami modelio išvesties kontrolei, įterpiami į programas, kad kontroliuotų modelio išvestį. Meta promptas ir promptas yra sujungiami į vieną tekstinį promptą.

Vienas meta prompto pavyzdys galėtų būti toks:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Dabar pažiūrėkime, kaip galime naudoti meta promptus savo demonstracijoje.

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

Iš aukščiau pateikto prompto matyti, kaip visi kuriami vaizdai atsižvelgia į meta promptą.

## Užduotis – padėkime studentams

Pamokos pradžioje pristatėme Edu4All. Dabar laikas padėti studentams generuoti vaizdus jų užduotims.

Studentai kurs vaizdus savo užduotims, susijusioms su paminklais – kokie paminklai bus, priklauso nuo pačių studentų. Studentai kviečiami pasitelkti savo kūrybiškumą šioje užduotyje, kad paminklus patalpintų į įvairius kontekstus.

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

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvinio dirbtinio intelekto mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvinį dirbtinį intelektą!

Eikite į 10 pamoką, kurioje aptarsime, kaip [kurti dirbtinio intelekto programas naudojant mažai kodo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.