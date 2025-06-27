<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:33:01+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "cs"
}
-->
# Vytváření aplikací pro generování obrázků

[![Vytváření aplikací pro generování obrázků](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.cs.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM nejsou jen o generování textu. Je také možné generovat obrázky z textových popisů. Mít obrázky jako modalitu může být velmi užitečné v řadě oblastí od MedTech, architektury, turismu, vývoje her a dalších. V této kapitole se podíváme na dva nejpopulárnější modely generování obrázků, DALL-E a Midjourney.

## Úvod

V této lekci se budeme zabývat:

- Generování obrázků a proč je to užitečné.
- DALL-E a Midjourney, co to je a jak fungují.
- Jak byste vytvořili aplikaci pro generování obrázků.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Definovat hranice pro vaši aplikaci pomocí meta promptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat možnosti Generativní AI. Mohou být použity například pro:

- **Úpravy a syntézu obrázků**. Můžete generovat obrázky pro různé případy použití, jako jsou úpravy obrázků a syntéza obrázků.

- **Použití v různých odvětvích**. Mohou být také použity k generování obrázků pro různá odvětví jako MedTech, Turismus, Vývoj her a další.

## Scénář: Edu4All

V rámci této lekce budeme pokračovat v práci s naším startupem, Edu4All. Studenti vytvoří obrázky pro své hodnocení, přesně jaké obrázky je na studentech, ale mohou to být ilustrace pro jejich vlastní pohádku nebo vytvořit novou postavu pro svůj příběh nebo jim pomoci vizualizovat jejich nápady a koncepty.

Zde je příklad toho, co by studenti Edu4All mohli generovat, pokud pracují ve třídě na památkách:

![Startup Edu4All, třída o památkách, Eiffelova věž](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.cs.png)

používající prompt jako

> "Pes vedle Eiffelovy věže v ranním slunečním světle"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů generování obrázků, umožňují vám používat prompty k generování obrázků.

### DALL-E

Začněme s DALL-E, což je model Generativní AI, který generuje obrázky z textových popisů.

> [DALL-E je kombinací dvou modelů, CLIP a rozptýlené pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model, který generuje vnoření, což jsou číselné reprezentace dat, z obrázků a textu.

- **Rozptýlená pozornost**, je model, který generuje obrázky z vnoření. DALL-E je trénován na datové sadě obrázků a textu a může být použit k generování obrázků z textových popisů. Například DALL-E může být použit k generování obrázků kočky v klobouku nebo psa s mohawkem.

### Midjourney

Midjourney funguje podobně jako DALL-E, generuje obrázky z textových promptů. Midjourney, může být také použit k generování obrázků pomocí promptů jako "kočka v klobouku" nebo "pes s mohawkem".

![Obrázek generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázek Wikipedia, generovaný Midjourney_

## Jak funguje DALL-E a Midjourney

Nejprve, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model Generativní AI založený na architektuře transformátoru s _autoregresivním transformátorem_.

_Autoregresivní transformátor_ definuje, jak model generuje obrázky z textových popisů, generuje jeden pixel po druhém a pak používá generované pixely k generování dalšího pixelu. Prochází několika vrstvami v neuronové síti, dokud není obrázek dokončen.

Tímto procesem DALL-E, kontroluje atributy, objekty, charakteristiky a další v generovaném obrázku. Nicméně, DALL-E 2 a 3 mají větší kontrolu nad generovaným obrázkem.

## Vytvoření vaší první aplikace pro generování obrázků

Co tedy potřebujete k vytvoření aplikace pro generování obrázků? Potřebujete následující knihovny:

- **python-dotenv**, je velmi doporučeno používat tuto knihovnu k uchování vašich tajemství v souboru _.env_ mimo kód.
- **openai**, tato knihovna je to, co budete používat k interakci s OpenAI API.
- **pillow**, pro práci s obrázky v Pythonu.
- **requests**, k pomoci s vytvářením HTTP požadavků.

1. Vytvořte soubor _.env_ s následujícím obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Najděte tyto informace v Azure Portal pro váš zdroj v sekci "Klíče a koncový bod".

1. Shromážděte výše uvedené knihovny do souboru _requirements.txt_ takto:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Dále vytvořte virtuální prostředí a nainstalujte knihovny:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pro Windows použijte následující příkazy k vytvoření a aktivaci vašeho virtuálního prostředí:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Přidejte následující kód do souboru nazvaného _app.py_:

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

Vysvětlíme tento kód:

- Nejprve importujeme knihovny, které potřebujeme, včetně knihovny OpenAI, knihovny dotenv, knihovny requests a knihovny Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Dále načteme proměnné prostředí ze souboru _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Poté nastavíme koncový bod, klíč pro OpenAI API, verzi a typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Dále generujeme obrázek:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Výše uvedený kód odpovídá s JSON objektem, který obsahuje URL generovaného obrázku. Můžeme použít URL k stažení obrázku a uložení do souboru.

- Nakonec otevřeme obrázek a použijeme standardní prohlížeč obrázků k jeho zobrazení:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Více podrobností o generování obrázku

Podívejme se na kód, který generuje obrázek podrobněji:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je textový prompt, který je použit k generování obrázku. V tomto případě používáme prompt "Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy".
- **size**, je velikost generovaného obrázku. V tomto případě generujeme obrázek, který je 1024x1024 pixelů.
- **n**, je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature**, je parametr, který kontroluje náhodnost výstupu Generativní AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0.7.

Existuje více věcí, které můžete s obrázky dělat, které pokryjeme v další části.

## Další schopnosti generování obrázků

Viděli jste zatím, jak jsme byli schopni generovat obrázek pomocí několika řádků v Pythonu. Nicméně, existuje více věcí, které můžete s obrázky dělat.

Můžete také dělat následující:

- **Provádět úpravy**. Poskytnutím existujícího obrázku masku a prompt, můžete změnit obrázek. Například můžete přidat něco do části obrázku. Představte si náš obrázek králíka, můžete přidat klobouk na králíka. Jak byste to udělali, je poskytnutím obrázku, masky (identifikující části oblasti pro změnu) a textového promptu, který říká, co by mělo být uděláno.

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

  Základní obrázek by obsahoval pouze králíka, ale finální obrázek by měl klobouk na králíkovi.

- **Vytvářet variace**. Myšlenka je, že vezmete existující obrázek a požádáte, aby byly vytvořeny variace. K vytvoření variace poskytnete obrázek a textový prompt a kód takto:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note, toto je podporováno pouze na OpenAI

## Teplota

Teplota je parametr, který kontroluje náhodnost výstupu Generativní AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0.7.

Podívejme se na příklad, jak teplota funguje, spuštěním tohoto promptu dvakrát:

> Prompt : "Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy"

![Králík na koni držící lízátko, verze 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.cs.png)

Nyní spusťme ten samý prompt jen abychom viděli, že nedostaneme stejný obrázek dvakrát:

![Generovaný obrázek králíka na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.cs.png)

Jak vidíte, obrázky jsou podobné, ale nejsou stejné. Zkusme změnit hodnotu teploty na 0.1 a uvidíme, co se stane:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Takže zkusme udělat odpověď více deterministickou. Mohli jsme pozorovat z dvou obrázků, které jsme generovali, že na prvním obrázku je králík a na druhém obrázku je kůň, takže obrázky se velmi liší.

Zkusme tedy změnit náš kód a nastavit teplotu na 0, takto:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nyní když spustíte tento kód, dostanete tyto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.cs.png)
- ![Teplota 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.cs.png)

Zde můžete jasně vidět, jak se obrázky více podobají.

## Jak definovat hranice pro vaši aplikaci pomocí metapromptů

S naším demem už můžeme generovat obrázky pro naše klienty. Nicméně, potřebujeme vytvořit nějaké hranice pro naši aplikaci.

Například, nechceme generovat obrázky, které nejsou bezpečné pro práci nebo nejsou vhodné pro děti.

Můžeme to udělat pomocí _metapromptů_. Metaprompty jsou textové prompty, které jsou použity k řízení výstupu Generativní AI modelu. Například, můžeme použít metaprompty k řízení výstupu a zajistit, že generované obrázky jsou bezpečné pro práci nebo vhodné pro děti.

### Jak to funguje?

Jak tedy metaprompty fungují?

Metaprompty jsou textové prompty, které jsou použity k řízení výstupu Generativní AI modelu, jsou umístěny před textovým promptem a jsou použity k řízení výstupu modelu a zabudovány do aplikací k řízení výstupu modelu. Zapouzdřují vstup promptu a vstup metapromptu do jednoho textového promptu.

Jedním příkladem metapromptu by byl následující:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nyní se podívejme, jak můžeme použít metaprompty v našem demu.

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

Z výše uvedeného promptu můžete vidět, jak všechny generované obrázky zohledňují metaprompt.

## Úkol - umožněme studentům

Na začátku této lekce jsme představili Edu4All. Nyní je čas umožnit studentům generovat obrázky pro jejich hodnocení.

Studenti vytvoří obrázky pro své hodnocení obsahující památky, přesně jaké památky je na studentech. Studenti jsou vyzváni, aby použili svou kreativitu v tomto úkolu a umístili tyto památky do různých kontextů.

## Řešení

Zde je jedno možné řešení:

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

## Skvělá práce! Pokračujte ve svém učení

Po dokončení této lekce se podívejte na naši [sbírku učení Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte ve zvyšování své znalosti Generativní AI!

Přejděte na Lekci 10, kde se podíváme na to, jak [vytvářet AI aplikace s nízkým kódem](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument ve svém rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.