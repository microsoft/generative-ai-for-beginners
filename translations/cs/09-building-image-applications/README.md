<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T19:01:55+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "cs"
}
-->
# Vytváření aplikací pro generování obrázků

[![Vytváření aplikací pro generování obrázků](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.cs.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM nejsou jen o generování textu. Je možné generovat obrázky na základě textových popisů. Obrázky jako další způsob vyjádření jsou velmi užitečné v mnoha oblastech, například v medicíně, architektuře, cestovním ruchu, vývoji her a dalších. V této kapitole se podíváme na dva nejpopulárnější modely pro generování obrázků: DALL-E a Midjourney.

## Úvod

V této lekci se dozvíte:

- Co je generování obrázků a proč je užitečné.
- Co jsou DALL-E a Midjourney, jak fungují.
- Jak vytvořit aplikaci pro generování obrázků.

## Cíle lekce

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Nastavit hranice pro svou aplikaci pomocí metapromptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat možnosti generativní AI. Můžete je využít například pro:

- **Úpravu a syntézu obrázků**. Můžete generovat obrázky pro různé účely, například pro úpravy nebo tvorbu nových obrázků.

- **Využití v různých odvětvích**. Dají se použít k tvorbě obrázků pro různá odvětví jako medicína, cestovní ruch, vývoj her a další.

## Scénář: Edu4All

V této lekci budeme pokračovat v práci s naším startupem Edu4All. Studenti budou vytvářet obrázky pro své zadání – jaké obrázky si zvolí, je na nich. Mohou to být ilustrace k vlastní pohádce, nový hrdina do příběhu nebo vizualizace jejich nápadů a konceptů.

Například, pokud studenti v hodině pracují na tématu památek, mohou vytvořit:

![Startup Edu4All, hodina o památkách, Eiffelova věž](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.cs.png)

pomocí promptu jako

> "Pes vedle Eiffelovy věže za ranního slunečního svitu"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů pro generování obrázků, které umožňují vytvářet obrázky na základě zadaných promptů.

### DALL-E

Začněme s DALL-E, což je generativní AI model, který vytváří obrázky z textových popisů.

> [DALL-E je kombinací dvou modelů, CLIP a diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, který vytváří embeddingy, tedy číselné reprezentace dat, z obrázků a textu.

- **Diffused attention** je model, který generuje obrázky z embeddingů. DALL-E je natrénován na datové sadě obrázků a textů a umožňuje generovat obrázky na základě textových popisů. Například DALL-E může vytvořit obrázek kočky s kloboukem nebo psa s čírem.

### Midjourney

Midjourney funguje podobně jako DALL-E, generuje obrázky na základě textových promptů. Midjourney lze použít k tvorbě obrázků pomocí promptů jako „kočka s kloboukem“ nebo „pes s čírem“.

![Obrázek vytvořený Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázek z Wikipedie, vytvořený pomocí Midjourney_

## Jak fungují DALL-E a Midjourney

Nejprve [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativní AI model založený na architektuře transformerů s _autoregresivním transformerem_.

_Autoregresivní transformer_ určuje, jak model generuje obrázky z textových popisů – generuje jeden pixel po druhém a využívá již vytvořené pixely k tvorbě dalších. Prochází několika vrstvami neuronové sítě, dokud není obrázek hotový.

Díky tomuto procesu DALL-E ovládá atributy, objekty, vlastnosti a další detaily v generovaném obrázku. Novější verze DALL-E 2 a 3 mají nad generovaným obrázkem ještě větší kontrolu.

## Vytvoření první aplikace pro generování obrázků

Co je potřeba k vytvoření aplikace pro generování obrázků? Budete potřebovat tyto knihovny:

- **python-dotenv** – doporučujeme použít tuto knihovnu pro uchování citlivých údajů v souboru _.env_ mimo zdrojový kód.
- **openai** – knihovna pro komunikaci s OpenAI API.
- **pillow** – pro práci s obrázky v Pythonu.
- **requests** – pro HTTP požadavky.

## Vytvoření a nasazení modelu Azure OpenAI

Pokud jste to ještě neudělali, postupujte podle návodu na stránce [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
a vytvořte si Azure OpenAI resource a model. Jako model zvolte DALL-E 3.  

## Vytvoření aplikace

1. Vytvořte soubor _.env_ s tímto obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Tyto údaje najdete v Azure OpenAI Foundry Portal ve vaší resource v sekci "Deployments".

1. Seznamte všechny potřebné knihovny v souboru _requirements.txt_ takto:

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

   Pro Windows použijte následující příkazy pro vytvoření a aktivaci virtuálního prostředí:

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

Vysvětlení kódu:

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

- Následně nastavíme klienta pro Azure OpenAI službu.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Dále generujeme obrázek:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Výše uvedený kód vrací JSON objekt, který obsahuje URL vygenerovaného obrázku. Tuto URL můžeme použít ke stažení obrázku a jeho uložení do souboru.

- Nakonec obrázek otevřeme a zobrazíme ve standardním prohlížeči obrázků:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnosti k generování obrázku

Podívejme se podrobněji na kód, který generuje obrázek:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** je textový prompt, který slouží k vygenerování obrázku. V tomto případě použijeme prompt "Králíček na koni, drží lízátko, na mlhavé louce, kde rostou narcisy".
- **size** je velikost generovaného obrázku. V tomto případě generujeme obrázek o rozměrech 1024x1024 pixelů.
- **n** je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature** je parametr, který určuje míru náhodnosti výstupu generativního AI modelu. Hodnota je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 znamená náhodný výstup. Výchozí hodnota je 0,7.

V další části si ukážeme další možnosti práce s obrázky.

## Další možnosti generování obrázků

Viděli jste, jak lze pomocí několika řádků v Pythonu vygenerovat obrázek. S obrázky ale můžete dělat ještě více.

Můžete například:

- **Provádět úpravy**. Pokud zadáte existující obrázek, masku a prompt, můžete obrázek upravit. Například můžete do části obrázku něco přidat. Představte si obrázek králíčka – můžete mu přidat klobouk. Stačí zadat obrázek, masku (určující oblast změny) a textový prompt, co má být provedeno.
> Poznámka: toto není podporováno v DALL-E 3. 
 
Zde je příklad použití GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Základní obrázek obsahuje pouze lounge s bazénem, ale výsledný obrázek bude mít plameňáka:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Vytvářet varianty**. Můžete vzít existující obrázek a nechat vytvořit jeho varianty. K tomu zadáte obrázek, textový prompt a použijete kód jako:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: toto je podporováno pouze v OpenAI

## Teplota

Teplota je parametr, který určuje míru náhodnosti výstupu generativního AI modelu. Hodnota je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 znamená náhodný výstup. Výchozí hodnota je 0,7.

Podívejme se na příklad, jak teplota funguje, když spustíme tento prompt dvakrát:

> Prompt : "Králíček na koni, drží lízátko, na mlhavé louce, kde rostou narcisy"

![Králíček na koni s lízátkem, verze 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.cs.png)

Nyní spustíme stejný prompt znovu, abychom viděli, že nedostaneme dvakrát stejný obrázek:

![Vygenerovaný obrázek králíčka na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.cs.png)

Jak vidíte, obrázky jsou podobné, ale nejsou stejné. Zkusme změnit hodnotu teploty na 0,1 a podívejme se, co se stane:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Zkusme tedy udělat výstup více deterministický. Z předchozích dvou obrázků jsme viděli, že na prvním je králíček a na druhém kůň, takže se obrázky dost liší.

Proto změníme kód a nastavíme teplotu na 0, například takto:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Když tento kód spustíte, získáte tyto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.cs.png)
- ![Teplota 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.cs.png)

Zde je jasně vidět, že se obrázky více podobají.

## Jak nastavit hranice aplikace pomocí metapromptů

V naší ukázce už můžeme generovat obrázky pro klienty. Je ale potřeba nastavit určité hranice pro naši aplikaci.

Například nechceme generovat obrázky, které nejsou vhodné do práce nebo pro děti.

To lze řešit pomocí _metapromptů_. Metaprompt je textový prompt, který slouží ke kontrole výstupu generativního AI modelu. Můžeme tak zajistit, že generované obrázky budou vhodné do práce nebo pro děti.

### Jak to funguje?

Jak tedy metaprompt funguje?

Metaprompt je textový prompt, který slouží ke kontrole výstupu generativního AI modelu. Zadává se před hlavní prompt a používá se k ovlivnění výstupu modelu. V aplikacích se prompt a metaprompt spojují do jednoho textového promptu.

Příklad metapromptu může vypadat takto:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Podívejme se, jak metaprompt použít v naší ukázce.

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

Z výše uvedeného promptu je vidět, že všechny vytvářené obrázky zohledňují metaprompt.

## Zadání – umožněme studentům tvořit

Na začátku lekce jsme představili Edu4All. Teď je čas umožnit studentům generovat obrázky pro jejich zadání.

Studenti budou vytvářet obrázky památek pro svá zadání – jaké památky si zvolí, je na nich. Mají za úkol využít svou kreativitu a umístit památky do různých kontextů.

## Řešení

Jedno možné řešení:

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

## Skvělá práce! Pokračujte ve studiu
Po dokončení této lekce se podívejte na naši [sbírku o Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde můžete dále rozvíjet své znalosti o generativní umělé inteligenci!

Pokračujte na Lekci 10, kde se podíváme na to, jak [vytvářet AI aplikace pomocí low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho rodném jazyce. Pro kritické informace doporučujeme profesionální lidský překlad. Nenese odpovědnost za jakékoli nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.