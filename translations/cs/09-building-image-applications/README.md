<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:54:04+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "cs"
}
-->
# Vytváření aplikací pro generování obrázků

[![Vytváření aplikací pro generování obrázků](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.cs.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Generativní jazykové modely (LLM) nejsou jen o generování textu. Je také možné generovat obrázky na základě textových popisů. Obrázky jako modality mohou být velmi užitečné v mnoha oblastech, jako je zdravotnická technologie, architektura, cestovní ruch, vývoj her a další. V této kapitole se podíváme na dva nejpopulárnější modely pro generování obrázků, DALL-E a Midjourney.

## Úvod

V této lekci se zaměříme na:

- Generování obrázků a jeho užitečnost.
- DALL-E a Midjourney, co to je a jak fungují.
- Jak vytvořit aplikaci pro generování obrázků.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Definovat hranice pro vaši aplikaci pomocí meta promptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat možnosti generativní AI. Mohou být použity například pro:

- **Úpravy a syntézu obrázků**. Můžete generovat obrázky pro různé účely, jako je úprava obrázků nebo jejich syntéza.

- **Použití v různých odvětvích**. Mohou být také použity k generování obrázků pro různá odvětví, jako je zdravotnická technologie, cestovní ruch, vývoj her a další.

## Scénář: Edu4All

V rámci této lekce budeme pokračovat v práci s naším startupem Edu4All. Studenti budou vytvářet obrázky pro své úkoly, konkrétní obrázky závisí na nich, ale mohou to být ilustrace pro jejich vlastní pohádku, vytvoření nové postavy pro jejich příběh nebo pomoc při vizualizaci jejich nápadů a konceptů.

Například, pokud studenti Edu4All pracují ve třídě na tématu památek, mohli by vytvořit něco takového:

![Startup Edu4All, třída o památkách, Eiffelova věž](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.cs.png)

pomocí promptu jako:

> "Pes vedle Eiffelovy věže za ranního slunečního světla"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů pro generování obrázků, které umožňují používat prompty k vytváření obrázků.

### DALL-E

Začněme s DALL-E, což je generativní AI model, který generuje obrázky na základě textových popisů.

> [DALL-E je kombinací dvou modelů, CLIP a difúzní pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, který generuje vektory (numerické reprezentace dat) z obrázků a textu.

- **Difúzní pozornost** je model, který generuje obrázky z vektorů. DALL-E je trénován na datovém souboru obrázků a textu a může být použit k generování obrázků na základě textových popisů. Například DALL-E může být použit k vytvoření obrázku kočky v klobouku nebo psa s čírem.

### Midjourney

Midjourney funguje podobně jako DALL-E, generuje obrázky na základě textových promptů. Midjourney může být také použit k vytvoření obrázků pomocí promptů jako „kočka v klobouku“ nebo „pes s čírem“.

![Obrázek vytvořený Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázek z Wikipedie, vytvořený Midjourney_

## Jak fungují DALL-E a Midjourney

Nejprve [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativní AI model založený na architektuře transformátorů s _autoregresivním transformátorem_.

_Autoregresivní transformátor_ definuje, jak model generuje obrázky na základě textových popisů. Generuje jeden pixel po druhém a poté používá vygenerované pixely k vytvoření dalšího pixelu. Tento proces probíhá přes více vrstev neuronové sítě, dokud není obrázek kompletní.

Díky tomuto procesu DALL-E kontroluje atributy, objekty, charakteristiky a další prvky v generovaném obrázku. Nicméně DALL-E 2 a 3 mají větší kontrolu nad generovaným obrázkem.

## Vytvoření první aplikace pro generování obrázků

Co je potřeba k vytvoření aplikace pro generování obrázků? Potřebujete následující knihovny:

- **python-dotenv**, doporučuje se používat tuto knihovnu k uchování tajných klíčů v souboru _.env_ mimo kód.
- **openai**, tato knihovna slouží k interakci s OpenAI API.
- **pillow**, pro práci s obrázky v Pythonu.
- **requests**, pro pomoc při vytváření HTTP požadavků.

## Vytvoření a nasazení modelu Azure OpenAI

Pokud jste to ještě neudělali, postupujte podle pokynů na stránce [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), abyste vytvořili zdroj a model Azure OpenAI. Vyberte model DALL-E 3.

## Vytvoření aplikace

1. Vytvořte soubor _.env_ s následujícím obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Tyto informace najdete v Azure OpenAI Foundry Portálu pro váš zdroj v sekci "Deployments".

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

   Pro Windows použijte následující příkazy k vytvoření a aktivaci virtuálního prostředí:

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

Vysvětlení tohoto kódu:

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

- Poté nakonfigurujeme klienta služby Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Následně generujeme obrázek:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Výše uvedený kód odpovídá JSON objektem, který obsahuje URL vygenerovaného obrázku. URL můžeme použít ke stažení obrázku a jeho uložení do souboru.

- Nakonec otevřeme obrázek a použijeme standardní prohlížeč obrázků k jeho zobrazení:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnosti o generování obrázku

Podívejme se podrobněji na kód, který generuje obrázek:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** je textový prompt, který se používá k vytvoření obrázku. V tomto případě používáme prompt „Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy“.
- **size** je velikost generovaného obrázku. V tomto případě generujeme obrázek o rozměrech 1024x1024 pixelů.
- **n** je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature** je parametr, který ovládá náhodnost výstupu generativního AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický, a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0,7.

Existují další věci, které můžete s obrázky dělat, a ty pokryjeme v další sekci.

## Další možnosti generování obrázků

Viděli jste, jak jsme byli schopni vygenerovat obrázek pomocí několika řádků v Pythonu. Existují však další věci, které můžete s obrázky dělat.

Můžete také:

- **Provádět úpravy**. Poskytnutím existujícího obrázku, masky a promptu můžete upravit obrázek. Například můžete přidat něco do určité části obrázku. Představte si náš obrázek králíka, můžete přidat klobouk králíkovi. Jak to uděláte, je poskytnutí obrázku, masky (identifikující části oblasti pro změnu) a textového promptu, který říká, co by mělo být provedeno.
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

  Základní obrázek by obsahoval pouze lounge s bazénem, ale finální obrázek by měl plameňáka:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.cs.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.cs.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.cs.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Vytvářet variace**. Myšlenka je, že vezmete existující obrázek a požádáte o vytvoření variací. Pro vytvoření variace poskytnete obrázek a textový prompt a kód takto:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: toto je podporováno pouze na OpenAI.

## Teplota

Teplota je parametr, který ovládá náhodnost výstupu generativního AI modelu. Teplota je hodnota mezi 0 a 1, kde 0 znamená, že výstup je deterministický, a 1 znamená, že výstup je náhodný. Výchozí hodnota je 0,7.

Podívejme se na příklad, jak teplota funguje, spuštěním tohoto promptu dvakrát:

> Prompt: „Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy“

![Králík na koni držící lízátko, verze 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.cs.png)

Nyní spusťme stejný prompt znovu, abychom viděli, že nedostaneme stejný obrázek dvakrát:

![Vygenerovaný obrázek králíka na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.cs.png)

Jak vidíte, obrázky jsou podobné, ale nejsou stejné. Zkusme změnit hodnotu teploty na 0,1 a uvidíme, co se stane:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Zkusme tedy udělat odpověď více deterministickou. Mohli jsme pozorovat z dvou obrázků, které jsme vygenerovali, že na prvním obrázku je králík a na druhém obrázku je kůň, takže obrázky se značně liší.

Změňme tedy náš kód a nastavme teplotu na 0, takto:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nyní, když spustíte tento kód, získáte tyto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.cs.png)
- ![Teplota 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.cs.png)

Zde můžete jasně vidět, jak se obrázky více podobají.

## Jak definovat hranice pro vaši aplikaci pomocí meta promptů

S naším demem již můžeme generovat obrázky pro naše klienty. Nicméně, potřebujeme vytvořit určité hranice pro naši aplikaci.

Například nechceme generovat obrázky, které nejsou vhodné pro práci nebo nejsou vhodné pro děti.

To můžeme udělat pomocí _meta promptů_. Meta prompty jsou textové prompty, které se používají k ovládání výstupu generativního AI modelu. Například můžeme použít meta prompty k ovládání výstupu a zajistit, že generované obrázky jsou vhodné pro práci nebo pro děti.

### Jak to funguje?

Jak tedy meta prompty fungují?

Meta prompty jsou textové prompty, které se používají k ovládání výstupu generativního AI modelu. Jsou umístěny před textovým promptem a používají se k ovládání výstupu modelu a jsou zabudovány do aplikací k ovládání výstupu modelu. Spojují vstup promptu a vstup meta promptu do jednoho textového promptu.

Jedním příkladem meta promptu by mohl být následující:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nyní se podívejme, jak můžeme použít meta prompty v našem demu.

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

Z výše uvedeného promptu můžete vidět, jak všechny vytvořené obrázky zohledňují meta prompt.

## Úkol - umožněme studentům

Na začátku této lekce jsme představili Edu4All. Nyní je čas umožnit studentům generovat obrázky pro jejich úkoly.

Studenti budou vytvářet obrázky pro své úkoly obsahující památky, konkrétní památky závisí na nich. Studenti jsou vyzváni, aby v tomto úkolu použili svou kreativitu a umístili tyto památky do různých kontextů.

## Řešení

Zde je jedno možné řešení:
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

## Skvělá práce! Pokračujte ve svém učení

Po dokončení této lekce se podívejte na naši [sbírku učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste si dále rozšířili znalosti o generativní AI!

Přejděte na Lekci 10, kde se podíváme na to, jak [vytvářet AI aplikace pomocí low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.