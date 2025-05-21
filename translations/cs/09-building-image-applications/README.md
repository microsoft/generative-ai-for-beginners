<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:22:00+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "cs"
}
-->
# Budování aplikací pro generování obrázků

[![Budování aplikací pro generování obrázků](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.cs.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM nejsou jen o generování textu. Je také možné generovat obrázky z textových popisů. Mít obrázky jako modalitu může být velmi užitečné v mnoha oblastech, jako je zdravotnická technologie, architektura, cestovní ruch, vývoj her a další. V této kapitole se podíváme na dva nejpopulárnější modely pro generování obrázků, DALL-E a Midjourney.

## Úvod

V této lekci se budeme zabývat:

- Generování obrázků a proč je to užitečné.
- DALL-E a Midjourney, co jsou zač a jak fungují.
- Jak byste postavili aplikaci pro generování obrázků.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Definovat hranice pro vaši aplikaci pomocí meta promptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat schopnosti generativní AI. Mohou být použity například pro:

- **Úpravy a syntézu obrázků**. Můžete generovat obrázky pro různé účely, jako jsou úpravy obrázků a syntéza obrázků.

- **Aplikace v různých odvětvích**. Mohou být také použity k generování obrázků pro různá odvětví, jako je zdravotnická technologie, cestovní ruch, vývoj her a další.

## Scénář: Edu4All

V rámci této lekce budeme pokračovat v práci s naším startupem, Edu4All. Studenti vytvoří obrázky pro své hodnocení, přesně jaké obrázky je na studentech, ale mohli by to být ilustrace pro jejich vlastní pohádku nebo vytvořit novou postavu pro jejich příběh nebo jim pomoci vizualizovat jejich nápady a koncepty.

Zde je příklad, co by studenti Edu4All mohli vygenerovat, pokud pracují ve třídě na památkách:

![Edu4All startup, třída o památkách, Eiffelova věž](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.cs.png)

pomocí promptu jako

> "Pes vedle Eiffelovy věže za ranního slunce"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů pro generování obrázků, které vám umožňují používat prompty k generování obrázků.

### DALL-E

Začněme s DALL-E, což je generativní AI model, který generuje obrázky z textových popisů.

> [DALL-E je kombinací dvou modelů, CLIP a difuzní pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, který generuje vnoření, což jsou číselné reprezentace dat, z obrázků a textu.

- **Difuzní pozornost** je model, který generuje obrázky z vnoření. DALL-E je trénován na datasetu obrázků a textu a může být použit k generování obrázků z textových popisů. Například DALL-E může být použit k generování obrázků kočky v klobouku nebo psa s čírem.

### Midjourney

Midjourney funguje podobně jako DALL-E, generuje obrázky z textových promptů. Midjourney může být také použit k generování obrázků pomocí promptů jako "kočka v klobouku" nebo "pes s čírem".

![Obrázek generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázek z Wikipedie, generovaný Midjourney_

## Jak funguje DALL-E a Midjourney

Nejprve [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativní AI model založený na architektuře transformátoru s _autoregresivním transformátorem_.

_Autoregresivní transformátor_ definuje, jak model generuje obrázky z textových popisů, generuje jeden pixel po druhém a poté používá vygenerované pixely k generování dalšího pixelu. Prochází několika vrstvami v neuronové síti, dokud není obrázek kompletní.

S tímto procesem DALL-E ovládá atributy, objekty, charakteristiky a další prvky v generovaném obrázku. Nicméně DALL-E 2 a 3 mají větší kontrolu nad generovaným obrázkem.

## Budování vaší první aplikace pro generování obrázků

Co je potřeba k vytvoření aplikace pro generování obrázků? Potřebujete následující knihovny:

- **python-dotenv**, je vysoce doporučeno používat tuto knihovnu k uložení vašich tajemství do souboru _.env_ mimo kód.
- **openai**, tato knihovna je to, co použijete k interakci s OpenAI API.
- **pillow**, pro práci s obrázky v Pythonu.
- **requests**, k pomoci s prováděním HTTP požadavků.

1. Vytvořte soubor _.env_ s následujícím obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Najděte tyto informace v Azure Portálu pro váš zdroj v sekci "Klíče a koncový bod".

1. Shromážděte výše uvedené knihovny do souboru nazvaného _requirements.txt_ takto:

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

- Nejprve importujeme potřebné knihovny, včetně knihovny OpenAI, knihovny dotenv, knihovny requests a knihovny Pillow.

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

- Následně vygenerujeme obrázek:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Výše uvedený kód odpovídá JSON objektem, který obsahuje URL vygenerovaného obrázku. URL můžeme použít ke stažení obrázku a jeho uložení do souboru.

- Nakonec otevřeme obrázek a použijeme standardní prohlížeč obrázků k jeho zobrazení:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnosti o generování obrázku

Podívejme se na kód, který generuje obrázek, podrobněji:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** je textový prompt, který je použit k generování obrázku. V tomto případě používáme prompt "Zajíc na koni, držící lízátko, na mlhavé louce, kde rostou narcisy".
- **size** je velikost generovaného obrázku. V tomto případě generujeme obrázek o velikosti 1024x1024 pixelů.
- **n** je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature** je parametr, který ovládá náhodnost výstupu generativního AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0.7.

Existuje více věcí, které můžete s obrázky dělat, o kterých se budeme bavit v další části.

## Další schopnosti generování obrázků

Doposud jste viděli, jak jsme byli schopni generovat obrázek pomocí několika řádků v Pythonu. Nicméně, existuje více věcí, které můžete s obrázky dělat.

Můžete také provádět následující:

- **Provádět úpravy**. Poskytnutím existujícího obrázku, masky a promptu můžete změnit obrázek. Například můžete přidat něco do části obrázku. Představte si náš obrázek zajíce, můžete přidat klobouk zajícovi. Jak byste to udělali, je poskytnutí obrázku, masky (určující část oblasti pro změnu) a textového promptu, co by mělo být provedeno.

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

  Základní obrázek by obsahoval pouze zajíce, ale finální obrázek by měl klobouk na zajíci.

- **Vytvářet variace**. Myšlenka je, že vezmete existující obrázek a požádáte, aby byly vytvořeny variace. K vytvoření variace poskytnete obrázek a textový prompt a kód takto:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: Toto je podporováno pouze na OpenAI

## Teplota

Teplota je parametr, který ovládá náhodnost výstupu generativního AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0.7.

Podívejme se na příklad, jak teplota funguje, spuštěním tohoto promptu dvakrát:

> Prompt: "Zajíc na koni, držící lízátko, na mlhavé louce, kde rostou narcisy"

![Zajíc na koni držící lízátko, verze 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.cs.png)

Nyní spusťme ten samý prompt jen abychom viděli, že nedostaneme dvakrát stejný obrázek:

![Generovaný obrázek zajíce na koni](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.cs.png)

Jak vidíte, obrázky jsou podobné, ale nejsou stejné. Zkusme změnit hodnotu teploty na 0.1 a podívejme se, co se stane:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Takže se pokusme udělat výstup více deterministický. Mohli jsme pozorovat z obou generovaných obrázků, že na prvním obrázku je zajíc a na druhém obrázku je kůň, takže se obrázky velmi liší.

Proto změňme náš kód a nastavme teplotu na 0, takto:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nyní, když spustíte tento kód, dostanete tyto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.cs.png)
- ![Teplota 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.cs.png)

Zde můžete jasně vidět, jak se obrázky více podobají.

## Jak definovat hranice pro vaši aplikaci pomocí metapromptů

S naším demem již můžeme generovat obrázky pro naše klienty. Nicméně, potřebujeme vytvořit nějaké hranice pro naši aplikaci.

Například nechceme generovat obrázky, které nejsou vhodné pro práci, nebo které nejsou vhodné pro děti.

Můžeme to udělat pomocí _metapromptů_. Metaprompty jsou textové prompty, které jsou použity k ovládání výstupu generativního AI modelu. Například, můžeme použít metaprompty k ovládání výstupu a zajistit, že generované obrázky jsou vhodné pro práci nebo vhodné pro děti.

### Jak to funguje?

Jak tedy metaprompty fungují?

Metaprompty jsou textové prompty, které jsou použity k ovládání výstupu generativního AI modelu, jsou umístěny před textovým promptem a jsou použity k ovládání výstupu modelu a vloženy do aplikací k ovládání výstupu modelu. Zapouzdřují vstup promptu a vstup metapromptu do jednoho textového promptu.

Jeden příklad metapromptu by byl následující:

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

Z výše uvedeného promptu můžete vidět, jak všechny vytvářené obrázky zohledňují metaprompt.

## Úkol - povzbuzujme studenty

Na začátku této lekce jsme představili Edu4All. Nyní je čas umožnit studentům generovat obrázky pro jejich hodnocení.

Studenti vytvoří obrázky pro své hodnocení obsahující památky, přesně jaké památky je na studentech. Studenti jsou vyzváni, aby při této úloze použili svou kreativitu a umístili tyto památky do různých kontextů.

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

Po dokončení této lekce se podívejte na naši [sbírku učení generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali ve zvyšování svých znalostí o generativní AI!

Přejděte na lekci 10, kde se podíváme na to, jak [vytvářet AI aplikace s nízkým kódem](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.