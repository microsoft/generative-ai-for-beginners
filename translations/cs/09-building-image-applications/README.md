<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:32:27+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "cs"
}
-->
# Tvorba aplikací pro generování obrázků

[![Tvorba aplikací pro generování obrázků](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.cs.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM nejsou jen o generování textu. Je také možné generovat obrázky z textových popisů. Obrázky jako modalita mohou být velmi užitečné v mnoha oblastech, od MedTechu, architektury, turismu, vývoje her a dalších. V této kapitole se podíváme na dva nejoblíbenější modely pro generování obrázků, DALL-E a Midjourney.

## Úvod

V této lekci se budeme věnovat:

- Generování obrázků a proč je užitečné.
- DALL-E a Midjourney, co to jsou a jak fungují.
- Jak vytvořit aplikaci pro generování obrázků.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Definovat hranice vaší aplikace pomocí metapromptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat možnosti Generativní AI. Mohou být využity například pro:

- **Úpravu a syntézu obrázků**. Můžete generovat obrázky pro různé účely, jako je úprava obrázků nebo jejich syntéza.

- **Použití v různých odvětvích**. Mohou být také použity k vytváření obrázků pro různá odvětví, jako je Medtech, turismus, vývoj her a další.

## Scénář: Edu4All

V rámci této lekce budeme pokračovat v práci s naším startupem Edu4All. Studenti budou vytvářet obrázky pro své úkoly, jaké přesně obrázky, to záleží na nich – mohou to být ilustrace k jejich vlastní pohádce, vytvoření nové postavy pro jejich příběh nebo pomoc s vizualizací jejich nápadů a konceptů.

Tady je příklad, co by studenti Edu4All mohli vytvořit, pokud pracují ve třídě na památkách:

![Edu4All startup, třída o památkách, Eiffelova věž](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.cs.png)

pomocí promptu

> "Pes vedle Eiffelovy věže v ranním slunečním světle"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů pro generování obrázků, které umožňují generovat obrázky na základě textových promptů.

### DALL-E

Začněme s DALL-E, což je model Generativní AI, který vytváří obrázky z textových popisů.

> [DALL-E je kombinací dvou modelů, CLIP a diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, který vytváří embeddingy, tedy číselné reprezentace dat, z obrázků a textu.

- **Diffused attention** je model, který generuje obrázky z embeddingů. DALL-E je trénován na datech obsahujících obrázky a text a může být použit k vytváření obrázků na základě textových popisů. Například DALL-E může vytvořit obrázek kočky v klobouku nebo psa s mohawkem.

### Midjourney

Midjourney funguje podobně jako DALL-E, generuje obrázky z textových promptů. Midjourney lze také použít k vytvoření obrázků na základě promptů jako „kočka v klobouku“ nebo „pes s mohawkem“.

![Obrázek vytvořený Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázek z Wikipedie, vytvořeno Midjourney_

## Jak fungují DALL-E a Midjourney

Nejprve [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model Generativní AI založený na architektuře transformeru s _autoregresivním transformerem_.

_Autoregresivní transformer_ určuje, jak model generuje obrázky z textových popisů – generuje jeden pixel po druhém a využívá již vygenerované pixely k vytvoření dalších. Prochází přitom několika vrstvami neuronové sítě, dokud není obrázek kompletní.

Tímto způsobem DALL-E ovládá atributy, objekty, charakteristiky a další prvky v generovaném obrázku. Nicméně DALL-E 2 a 3 mají nad generovaným obrázkem ještě větší kontrolu.

## Vytvoření první aplikace pro generování obrázků

Co je potřeba k vytvoření aplikace pro generování obrázků? Budete potřebovat následující knihovny:

- **python-dotenv**, doporučujeme tuto knihovnu pro uchování vašich tajných klíčů v souboru _.env_ mimo kód.
- **openai**, tato knihovna slouží k interakci s OpenAI API.
- **pillow**, pro práci s obrázky v Pythonu.
- **requests**, pro usnadnění HTTP požadavků.

1. Vytvořte soubor _.env_ s následujícím obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Tyto informace najdete v Azure Portálu u vašeho zdroje v sekci „Keys and Endpoint“.

1. Vytvořte soubor _requirements.txt_ s následujícím obsahem:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Vytvořte virtuální prostředí a nainstalujte knihovny:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pro Windows použijte tyto příkazy k vytvoření a aktivaci virtuálního prostředí:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Přidejte následující kód do souboru _app.py_:

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

Vysvětlíme si tento kód:

- Nejprve importujeme potřebné knihovny, včetně OpenAI, dotenv, requests a Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Poté načteme proměnné prostředí ze souboru _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Následně nastavíme endpoint, klíč pro OpenAI API, verzi a typ.

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

  Výše uvedený kód vrací JSON objekt obsahující URL vygenerovaného obrázku. Tuto URL můžeme použít ke stažení obrázku a jeho uložení do souboru.

- Nakonec otevřeme obrázek a zobrazíme ho pomocí standardního prohlížeče obrázků:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnější pohled na generování obrázku

Podívejme se podrobněji na kód, který generuje obrázek:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** je textový prompt, který se používá k vytvoření obrázku. V tomto případě používáme prompt „Zajíček na koni, držící lízátko, na mlhavé louce, kde rostou narcisy“.
- **size** je velikost generovaného obrázku. V tomto případě generujeme obrázek o rozměrech 1024x1024 pixelů.
- **n** je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature** je parametr, který ovlivňuje náhodnost výstupu modelu Generativní AI. Hodnota teploty je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 náhodný výstup. Výchozí hodnota je 0,7.

Existuje ještě více možností, co s obrázky dělat, o tom si povíme v další části.

## Další možnosti generování obrázků

Už jste viděli, jak jsme pomocí pár řádků v Pythonu vytvořili obrázek. Ale existuje i další možnosti práce s obrázky.

Můžete také:

- **Provádět úpravy**. Poskytnutím existujícího obrázku, masky a promptu můžete obrázek upravit. Například můžete přidat něco do určité části obrázku. Představte si náš obrázek se zajíčkem, můžete mu přidat klobouk. Jak na to? Poskytnete obrázek, masku (která označuje oblast pro změnu) a textový prompt, co se má udělat.

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

  Základní obrázek by obsahoval pouze zajíčka, ale finální obrázek by měl klobouk na zajíčkovi.

- **Vytvářet variace**. Myšlenka je, že vezmete existující obrázek a požádáte o vytvoření jeho variací. Pro vytvoření variace poskytnete obrázek a textový prompt a použijete kód jako tento:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: tato funkce je podporována pouze v OpenAI.

## Teplota (Temperature)

Teplota je parametr, který ovlivňuje náhodnost výstupu modelu Generativní AI. Hodnota teploty je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 náhodný výstup. Výchozí hodnota je 0,7.

Podívejme se na příklad, jak teplota funguje, když spustíme tento prompt dvakrát:

> Prompt: „Zajíček na koni, držící lízátko, na mlhavé louce, kde rostou narcisy“

![Zajíček na koni držící lízátko, verze 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.cs.png)

Nyní spustíme stejný prompt znovu, abychom viděli, že nedostaneme stejný obrázek dvakrát:

![Vygenerovaný obrázek zajíčka na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.cs.png)

Jak vidíte, obrázky jsou podobné, ale ne stejné. Zkusme změnit hodnotu teploty na 0,1 a uvidíme, co se stane:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Zkusme tedy udělat odpověď více deterministickou. Z obrázků, které jsme vytvořili, vidíme, že na prvním je zajíček a na druhém kůň, takže se obrázky výrazně liší.

Proto změníme náš kód a nastavíme teplotu na 0, takto:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Když teď tento kód spustíte, dostanete tyto dva obrázky:

- ![Teplota 0, verze 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.cs.png)
- ![Teplota 0, verze 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.cs.png)

Zde je jasně vidět, že obrázky jsou si mnohem podobnější.

## Jak definovat hranice vaší aplikace pomocí metapromptů

S naší ukázkou už můžeme generovat obrázky pro naše klienty. Nicméně je potřeba nastavit určité hranice pro naši aplikaci.

Například nechceme generovat obrázky, které nejsou vhodné pro práci (NSFW) nebo nejsou vhodné pro děti.

To můžeme udělat pomocí _metapromptů_. Metaprompt jsou textové prompt, které slouží k řízení výstupu modelu Generativní AI. Například můžeme metaprompt použít k zajištění, že generované obrázky jsou bezpečné pro práci nebo vhodné pro děti.

### Jak to funguje?

Jak tedy metaprompt fungují?

Metaprompt jsou textové prompt, které se používají k řízení výstupu modelu Generativní AI, umisťují se před hlavní textový prompt a slouží k řízení výstupu modelu. Jsou integrovány do aplikací, aby kontrolovaly výstup modelu. Vstupní prompt a metaprompt jsou spojeny do jednoho textového promptu.

Příklad metaprompt může vypadat takto:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Podívejme se nyní, jak můžeme metaprompt použít v naší ukázce.

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

Z výše uvedeného promptu vidíte, že všechny generované obrázky berou v úvahu metaprompt.

## Zadání – umožněme studentům tvořit

Na začátku lekce jsme představili Edu4All. Nyní je čas umožnit studentům generovat obrázky pro jejich úkoly.

Studenti budou vytvářet obrázky obsahující památky, jaké přesně památky, to je na nich. Studenti mají v tomto úkolu využít svou kreativitu a umístit tyto památky do různých kontextů.

## Řešení

Tady je jedno možné řešení:

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

## Skvělá práce! Pokračujte ve svém vzdělávání

Po dokončení této lekce si prohlédněte naši [kolekci Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozšiřování svých znalostí o Generativní AI!

Přejděte na Lekci 10, kde se podíváme, jak [vytvářet AI aplikace s nízkým kódem](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.