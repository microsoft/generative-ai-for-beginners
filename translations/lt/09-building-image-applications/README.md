# Vaizdų generavimo programėlių kūrimas

[![Vaizdų generavimo programėlių kūrimas](../../../translated_images/lt/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM pasižymi kur kas daugiau funkcijų nei tik tekstų generavimu. Taip pat galima generuoti vaizdus iš teksto aprašymų. Vaizdų naudojimas kaip moduliacija gali būti labai naudingas daugelyje sričių: medicinos technologijose, architektūroje, turizme, žaidimų kūrime ir kitose. Šiame skyriuje aptarsime du populiariausius vaizdų generavimo modelius – DALL-E ir Midjourney.

## Įvadas

Šioje pamokoje aptarsime:

- Vaizdų generavimą ir jo naudą.
- DALL-E ir Midjourney – kas jie yra ir kaip veikia.
- Kaip sukurti vaizdų generavimo programėlę.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Sukurti vaizdų generavimo programėlę.
- Apibrėžti programėlės ribas meta užklausomis.
- Dirbti su DALL-E ir Midjourney.

## Kodėl kurti vaizdų generavimo programėlę?

Vaizdų generavimo programėlės – puikus būdas tyrinėti generatyvios dirbtinio intelekto galimybes. Jos gali būti naudojamos, pavyzdžiui, šiais tikslais:

- **Vaizdų redagavimas ir sintezė**. Galite generuoti vaizdus įvairiems naudojimo atvejams, tokiems kaip vaizdų redagavimas ir sintezė.

- **Pritaikymas įvairiems sektoriams**. Taip pat galima generuoti vaizdus įvairioms pramonės šakoms, kaip medicinos technologijos, turizmas, žaidimų kūrimas ir kt.

## Scenarijus: Edu4All

Šios pamokos metu tęsiame darbą su mūsų startuoliu Edu4All. Studentai kurs vaizdus savo darbams. Kokius vaizdus kurti – spręsti studentams: jie gali būti iliustracijos jų pasakai, nauji personažai jų istorijai ar idėjų, koncepcijų vizualizavimas.

Štai ką Edu4All studentai galėtų sukurti, jei klasėje dirbtų su pamoka apie paminklus:

![Edu4All startuolis, pamoka apie paminklus, Eifelio bokštas](../../../translated_images/lt/startup.94d6b79cc4bb3f5a.webp)

naudodami užklausą, panašią į:

> „Šuo šalia Eifelio bokšto ankstyvo ryto saulėtą dieną“

## Kas yra DALL-E ir Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ir [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) yra du populiariausi vaizdų generavimo modeliai, leidžiantys generuoti vaizdus naudojant užklausas.

### DALL-E

Pradėkime nuo DALL-E, tai generatyvus DI modelis, generuojantis vaizdus pagal teksto aprašymus.

> [DALL-E yra dviejų modelių – CLIP ir disperguotos dėmesio – kombinacija](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** – modelis, generuojantis įžvalgas (embedding), skaitmenines duomenų reprezentacijas, iš vaizdų ir teksto.

- **Disperguota dėmesio (diffused attention)** – modelis, generuojantis vaizdus iš įžvalgų. DALL-E mokytas su vaizdų ir tekstų duomenų rinkiniu, gali generuoti vaizdus iš teksto aprašymų. Pavyzdžiui, DALL-E gali generuoti katę su skrybėle ar šunį su mohawku.

### Midjourney

Midjourney veikia panašiai kaip DALL-E – generuoja vaizdus pagal tekstines užklausas. Midjourney taip pat gali kurti vaizdus pagal užklausas, tokioms kaip „katė su skrybėle“ arba „šuo su mohawku“.

![Midjourney generuotas vaizdas, mechaninis balandis](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Vaizdo šaltinis Wikipedia, Midjourney generuotas vaizdas_

## Kaip veikia DALL-E ir Midjourney

Pirmiausia [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E yra generatyvus DI modelis, pagrįstas transformerių architektūra su _autoregresiniu transformerių_ modeliu.

_Autoregresinis transformeris_ apibrėžia, kaip modelis generuoja vaizdus iš teksto aprašymų: jis generuoja po vieną pikselį, tada naudoja sugeneruotus pikselius sekančio pikselio generavimui. Tai vyksta per kelis sluoksnius neuroniniame tinkle, kol vaizdas bus visiškai sugeneruotas.

Šiuo procesu DALL-E valdo atributus, objektus, charakteristikas ir kitus elementus generuojamame vaizde. Tačiau DALL-E 2 ir 3 leidžia dar daugiau valdyti sugeneruotą vaizdą.

## Pirmoji vaizdų generavimo programėlė

Ką reikia, kad sukurtumėte vaizdų generavimo programėlę? Reikia šių bibliotekų:

- **python-dotenv** – labai rekomenduojama naudoti šią biblioteką, kad slaptieji raktai būtų saugomi _.env_ faile, atskirai nuo kodo.
- **openai** – tai biblioteka, skirta bendrauti su OpenAI API.
- **pillow** – darbui su vaizdais Python kalboje.
- **requests** – HTTP užklausoms atlikti.

## Sukurkite ir paleiskite Azure OpenAI modelį

Jei dar nepadaryta, vykdykite [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) puslapio instrukcijas
, kad sukurtumėte Azure OpenAI išteklių ir modelį. Pasirinkite modelį **gpt-image-1** (dabartinis Azure OpenAI vaizdų generavimo modelis; DALL-E 3 yra senesnis ir naujiems diegimams nebepalaikomas).

## Kurkite programėlę

1. Sukurkite failą _.env_ su šiuo turiniu:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Šią informaciją rasite Azure OpenAI Foundry portale savo resurso „Deployments“ sekcijoje.

1. Surinkite aukščiau minėtas bibliotekas faile pavadinimu _requirements.txt_ taip:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Toliau, sukurkite virtualią aplinką ir įdiekite bibliotekas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows sistemoje naudokite šias komandas virtualios aplinkos sukūrimui ir aktyvavimui:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Pridėkite šį kodą faile _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # importuoti dotenv
    dotenv.load_dotenv()
    
    # sukonfigūruoti Azure OpenAI paslaugos klientą
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Sukurti paveikslėlį naudojant paveikslėlių generavimo API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Nustatyti katalogą saugomam paveikslėliui
        image_dir = os.path.join(os.curdir, 'images')

        # Jei katalogas neegzistuoja, sukurkite jį
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Inicializuoti paveikslėlio kelią (atkreipkite dėmesį, kad failo tipas turėtų būti png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Gauti sugeneruotą paveikslėlį
        image_url = generation_response.data[0].url  # išgauti paveikslėlio URL iš atsakymo
        generated_image = requests.get(image_url).content  # atsisiųsti paveikslėlį
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Rodyti paveikslėlį numatytame paveikslėlių peržiūros programoje
        image = Image.open(image_path)
        image.show()

    # sugauti išimtis
    except openai.BadRequestError as err:
        print(err)
   ```

Paaiškinkime šį kodą:

- Pirmiausia įkeliame reikalingas bibliotekas, įskaitant OpenAI, dotenv, requests ir Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Tuomet užkrauname aplinkos kintamuosius iš _.env_ failo.

  ```python
  # importuoti dotenv
  dotenv.load_dotenv()
  ```

- Po to sukonfigūruojame Azure OpenAI kliento parametrus

  ```python
  # Gaukite pabaigos tašką ir raktą iš aplinkos kintamųjų
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Toliau generuojame vaizdą:

  ```python
  # Sukurkite paveikslėlį naudodami paveikslėlių generavimo API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Aukščiau pateiktas kodas gauna JSON objektą, kuriame yra sugeneruoto vaizdo URL. Šį URL galime naudoti vaizdui parsisiųsti ir išsaugoti faile.

- Galiausiai atidarome vaizdą ir naudojame standartinį vaizdų peržiūros įrankį:

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

- **prompt** – tai teksto užklausa, pagal kurią generuojamas vaizdas. Šiuo atveju naudojame užklausą „Triušis ant arklio, laikantis saldainį lazdelėje, rūku apgaubtame lauke, kuriame auga narcizai“.
- **size** – generuojamo vaizdo dydis. Šiuo atveju, vaizdas bus 1024x1024 pikselių.
- **n** – generuojamų vaizdų skaičius. Šiuo atveju generuojame du vaizdus.
- **temperature** – parametras, valdymas generatyvaus DI modelio atsitiktinumą. Temperatūra yra reikšmė tarp 0 ir 1, kur 0 reiškia deterministinį (vientisą) rezultatą, o 1 – atsitiktinį. Numatytoji reikšmė yra 0.7.

Yra ir daugiau galimybių darbui su vaizdais, kurias aptarsime kitame skyriuje.

## Papildomos vaizdų generavimo galimybės

Matėte, kaip vos keliais Python kodo eilutėmis galima sukurti vaizdą. Tačiau su vaizdais galima atlikti ir daugiau.

Galite taip pat:

- **Atlikti redagavimus**. Pateikdami esamą vaizdą, kaukę ir užklausą, galite redaguoti vaizdą. Pavyzdžiui, pridėti kažką prie vaizdo dalies. Įsivaizduokite mūsų triušio vaizdą – galite pridėti skrybėlę triušiui. Tam reikia pateikti vaizdą, kaukę (nurodančią sritį pataisymui) ir tekstinę užklausą, ką reikia pakeisti.
> Pastaba: šis funkcionalumas nepalaikomas DALL-E 3. 
 
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

  Pagrindinis vaizdas rodys tik poilsio zoną su baseinu, bet galutiniame vaizde bus flamingas:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/lt/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/lt/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/lt/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Kurti variacijas**. Idėja ta, kad turite esamą vaizdą ir prašote sukurti jo variacijų. Variacijai sukurti pateikite vaizdą ir tekstinę užklausą ir naudokite tokį kodą:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Pastaba, tai palaikoma tik OpenAI DALL-E 2 modelyje, ne gpt-image-1.

## Temperatūra

Temperatūra yra parametras, valdantis generatyvios DI modelio atsitiktinumą. Temperatūra yra skaičius nuo 0 iki 1, kur 0 reiškia deterministinį rezultatą, o 1 – visiškai atsitiktinį. Numatytoji vertė yra 0.7.

Pažiūrėkime, kaip veikia temperatūra, paleisdami užklausą du kartus:

> Užklausa: „Triušis ant arklio, laikantis saldainį lazdelėje, rūku apgaubtame lauke, kuriame auga narcizai“

![Triušis ant arklio laikantis saldainį lazdelėje, versija 1](../../../translated_images/lt/v1-generated-image.a295cfcffa3c13c2.webp)

Dabar paleiskime tą pačią užklausą dar kartą, kad pamatytume, jog gausime skirtingus vaizdus:

![Generuotas triušio ant arklio vaizdas](../../../translated_images/lt/v2-generated-image.33f55a3714efe61d.webp)

Kaip matome, vaizdai panašūs, bet ne identiški. Pabandykime pakeisti temperatūrą į 0.1 ir pažiūrėkime, kas nutiks:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Įveskite savo užklausos tekstą čia
        size='1024x1024',
        n=2
    )
```

### Temperatūros keitimas

Bandykime įvesti daugiau determinizmo į atsakymą. Pažvelgę į du generuotus vaizdus matome, kad pirmajame yra triušis, o antrajame – arklys, taigi vaizdai ženkliai skiriasi.

Todėl pakeisime kodą, nustatydami temperatūrą 0:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Įveskite čia savo užklausos tekstą
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Dabar paleidus šį kodą, gausite šiuos du vaizdus:

- ![Temperatūra 0, v1](../../../translated_images/lt/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatūra 0, v2](../../../translated_images/lt/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Čia aiškiai matosi, kaip vaizdai daugiau primena vienas kitą.

## Kaip apibrėžti programėlės ribas su metaužklausomis

Mūsų demonstracinėje versijoje jau galime generuoti vaizdus klientams. Tačiau turime apibrėžti programėlės ribas.

Pavyzdžiui, nenorime generuoti vaizdų, kurie nėra saugūs darbo vietoje arba netinka vaikams.

Galime tai padaryti naudodami _meta užklausas_. Meta užklausos – tai teksto užklausos, skirtos valdyti generatyvaus DI modelio išvestį. Pavyzdžiui, meta užklausomis galime kontroliuoti išvestį ir užtikrinti, kad generuoti vaizdai būtų saugūs darbo aplinkai ar tinkami vaikams.

### Kaip tai veikia?

Kaip gi veikia meta užklausos?

Meta užklausos – tai teksto užklausos, naudojamos generatyvaus DI modelio išvesčiai kontroliuoti, jos dedamos prieš tekstinę užklausą ir yra įterptos į programėles, kad kontroliuotų modelio išvestį. Užklausos įvestis ir meta užklausos įvestis yra sujungiami į vieną tekstinę užklausą.

Vienas meta užklausos pavyzdys būtų toks:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Dabar pažiūrėkime, kaip galime naudoti meta užklausas mūsų demonstracijoje.

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

# TODO pridėti užklausą paveikslėliui sugeneruoti
```

Iš aukščiau pateiktos užklausos matyti, kaip visi generuojami vaizdai atsižvelgia į meta užklausą.

## Užduotis – leiskime mokiniams kurti vaizdus

Pamokoje pristatėme Edu4All. Dabar metas leisti mokiniams generuoti vaizdus savo darbams.


Studentai kurs atvaizdus savo vertinimams, kuriuose bus paminklai, kokie paminklai priklauso nuo studentų sprendimo. Studentams prašoma panaudoti savo kūrybiškumą šiame uždavinyje, kad šiuos paminklus būtų galima įdėti į skirtingus kontekstus.

## Sprendimas

Štai vienas galimas sprendimas:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# importuoti dotenv
dotenv.load_dotenv()

# Gauti galinį tašką ir raktą iš aplinkos kintamųjų
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
    # Sukurti paveikslėlį naudodami paveikslėlių generavimo API
    generation_response = client.images.generate(
        prompt=prompt,    # Įveskite savo tekstą čia
        size='1024x1024',
        n=1,
    )
    # Nustatyti katalogą saugomam paveikslėliui
    image_dir = os.path.join(os.curdir, 'images')

    # Jei katalogas neegzistuoja, sukurti jį
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inicializuoti paveikslėlio kelią (atkreipkite dėmesį, kad failo tipas turi būti png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Gauti sugeneruotą paveikslėlį
    image_url = generation_response.data[0].url  # Išgauti paveikslėlio URL iš atsakymo
    generated_image = requests.get(image_url).content  # Atsisiųsti paveikslėlį
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Rodyti paveikslėlį numatytame paveikslėlių peržiūros įrenginyje
    image = Image.open(image_path)
    image.show()

# Gaudyti išimtis
except openai.BadRequestError as err:
    print(err)
```

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, patikrinkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau keltumėte savo generatyvios AI žinias į aukštesnį lygį!

Eikite į 10 pamoką, kurioje apžvelgsime, kaip [kurti AI programas naudojant žemo kodo platformas](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->