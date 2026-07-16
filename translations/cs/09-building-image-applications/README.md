# Vytváření aplikací pro generování obrázků

[![Vytváření aplikací pro generování obrázků](../../../translated_images/cs/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM nejsou určeny jen pro generování textu. Je také možné generovat obrázky z textových popisů. Mít obrázky jako modalitu může být vysoce užitečné v mnoha oblastech, od MedTech, architektury, turismu, vývoje her a další. V této kapitole se podíváme na dva nejpopulárnější modely pro generování obrázků, DALL-E a Midjourney.

## Úvod

V této lekci se budeme věnovat:

- Generování obrázků a proč je užitečné.
- DALL-E a Midjourney, co jsou zač a jak fungují.
- Jak vytvořit aplikaci pro generování obrázků.

## Cíle učení

Po dokončení této lekce budete schopni:

- Vytvořit aplikaci pro generování obrázků.
- Definovat hranice pro vaši aplikaci pomocí meta promptů.
- Pracovat s DALL-E a Midjourney.

## Proč vytvářet aplikaci pro generování obrázků?

Aplikace pro generování obrázků jsou skvělým způsobem, jak prozkoumat schopnosti generativní AI. Mohou být použity například pro:

- **Úpravu a syntézu obrázků**. Můžete generovat obrázky pro různé případy užití, jako je úprava obrázků a syntéza obrázků.

- **Aplikace v různých průmyslových odvětvích**. Mohou být také použity k tvorbě obrázků pro různá odvětví, jako jsou Medtech, turismus, vývoj her a další.

## Scénář: Edu4All

V rámci této lekce budeme pokračovat ve spolupráci s naší startupovou firmou Edu4All. Studenti budou vytvářet obrázky pro své hodnocení, jaké obrázky to budou, je na nich, ale mohou to být ilustrace k jejich vlastní pohádce, vytvoření nového charakteru pro jejich příběh nebo pomoc s vizualizací jejich myšlenek a konceptů.

Zde je příklad toho, co by studenti Edu4All mohli vytvořit, pokud by pracovali ve třídě na památkách:

![Startup Edu4All, třída o památkách, Eiffelova věž](../../../translated_images/cs/startup.94d6b79cc4bb3f5a.webp)

pomocí promptu jako

> "Pes vedle Eiffelovy věže za časného ranního slunečního světla"

## Co je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) jsou dva z nejpopulárnějších modelů pro generování obrázků, které umožňují použít prompty k tvorbě obrázků.

### DALL-E

Začněme s DALL-E, což je generativní AI model, který generuje obrázky z textových popisů.

> [DALL-E je kombinace dvou modelů, CLIP a difuzní pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, který vytváří embeddingy, což jsou číselné reprezentace dat, z obrázků a textu.

- **Difuzní pozornost** je model, který generuje obrázky z embeddingů. DALL-E je trénován na datové sadě obrázků a textu a lze jej použít k vytváření obrázků z textových popisů. Například DALL-E může generovat obrázky kočky s kloboukem nebo psa s irokézou.

### Midjourney

Midjourney pracuje podobně jako DALL-E, generuje obrázky z textových promptů. Midjourney lze také použít k generování obrázků pomocí promptů jako „kočka s kloboukem“ nebo „pes s irokézou“.

![Obrázek generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Zdroj obrázku Wikipedia, obrázek generovaný Midjourney_

## Jak fungují DALL-E a Midjourney

Nejprve [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generativní AI model založený na architektuře transformeru s _autoregresivním transformerem_.

_Autoregresivní transformer_ definuje, jak model generuje obrázky z textových popisů, generuje jeden pixel po druhém a pak použije vygenerované pixely k vytvoření dalšího pixelu. Prochází několika vrstvami v neuronové síti, dokud není obrázek kompletní.

Tímto procesem DALL-E ovládá atributy, objekty, charakteristiky a další prvky obrázku, který generuje. Nicméně DALL-E 2 a 3 mají větší kontrolu nad vygenerovaným obrázkem.

## Vytvoření vaší první aplikace pro generování obrázků

Co je tedy potřeba k vytvoření aplikace pro generování obrázků? Potřebujete následující knihovny:

- **python-dotenv**, je velmi doporučeno použít tuto knihovnu pro uchování vašich tajemství v souboru _.env_ mimo kód.
- **openai**, tato knihovna je ta, kterou použijete pro komunikaci s API OpenAI.
- **pillow**, pro práci s obrázky v Pythonu.
- **requests**, aby vám pomohla dělat HTTP požadavky.

## Vytvoření a nasazení modelu Azure OpenAI

Pokud to ještě není hotovo, postupujte podle pokynů na stránce [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
pro vytvoření zdroje Azure OpenAI a modelu. Jako model zvolte **gpt-image-1** (aktuální generace Azure OpenAI modelu pro obrázky; DALL-E 3 je zastaralý a už není dostupný pro nové nasazení).

## Vytvoření aplikace

1. Vytvořte soubor _.env_ s následujícím obsahem:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Informace naleznete v Azure OpenAI Foundry portálu pro váš zdroj v sekci "Deployments".

1. Shromážděte uvedené knihovny do souboru _requirements.txt_ takto:

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

1. Přidejte následující kód do souboru s názvem _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # importovat dotenv
    dotenv.load_dotenv()
    
    # nakonfigurovat klienta služby Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Vytvořit obrázek pomocí API pro generování obrázků
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Nastavit adresář pro uložený obrázek
        image_dir = os.path.join(os.curdir, 'images')

        # Pokud adresář neexistuje, vytvořit jej
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Inicializovat cestu k obrázku (pozor, typ souboru by měl být png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Získat vygenerovaný obrázek
        image_url = generation_response.data[0].url  # extrahovat URL obrázku z odpovědi
        generated_image = requests.get(image_url).content  # stáhnout obrázek
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Zobrazit obrázek v výchozím prohlížeči obrázků
        image = Image.open(image_path)
        image.show()

    # zachytit výjimky
    except openai.BadRequestError as err:
        print(err)
   ```

Vysvětlíme tento kód:

- Nejprve importujeme knihovny, které potřebujeme, včetně knihovny OpenAI, dotenv, requests a Pillow.

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

- Poté nakonfigurujeme klienta služby Azure OpenAI

  ```python
  # Získejte koncový bod a klíč z proměnných prostředí
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Následně generujeme obrázek:

  ```python
  # Vytvořte obrázek pomocí rozhraní API pro generování obrázků
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Výše uvedený kód odpovídá JSON objektem obsahujícím URL vygenerovaného obrázku. URL můžeme použít ke stažení obrázku a jeho uložení do souboru.

- Nakonec otevřeme obrázek a zobrazíme ho pomocí standardního prohlížeče obrázků:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnosti o generování obrázku

Podívejme se na kód, který generuje obrázek, podrobněji:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, je textový prompt použitý k uzpůsobení obrázku. V tomto případě používáme prompt "Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy".
- **size**, je velikost generovaného obrázku. V tomto případě generujeme obrázek o rozměrech 1024x1024 pixelů.
- **n**, je počet generovaných obrázků. V tomto případě generujeme dva obrázky.
- **temperature**, je parametr, který řídí náhodnost výstupu generativního AI modelu. Hodnota teploty je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 znamená náhodný výstup. Výchozí hodnota je 0.7.

Existuje více možností, co můžete s obrázky dělat, což pokryjeme v další části.

## Další schopnosti generování obrázků

Zatím jste viděli, jak jsme dokázali vygenerovat obrázek pomocí několika řádků Pythonu. Nicméně, existují další věci, které můžete s obrázky dělat.

Můžete také provést následující:

- **Provádět úpravy**. Poskytnutím existujícího obrázku, masky a promptu můžete obrázek upravit. Například můžete přidat něco do části obrázku. Představte si náš obrázek králíka, můžete mu přidat klobouk. Jak to udělat? Poskytnete obrázek, masku (která vyznačuje oblast pro změnu) a textový prompt říkající, co má být uděláno.
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

  Základní obrázek by obsahoval pouze salon s bazénem, ale výsledný obrázek bude mít plameňáka:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/cs/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/cs/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/cs/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Vytvářet variace**. Myšlenka je, že vezmete existující obrázek a požádáte o vytvoření variací. Pro vytvoření variace poskytnete obrázek a textový prompt a kód takto:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Poznámka, toto je podporováno pouze modelem OpenAI DALL-E 2, nikoliv gpt-image-1

## Teplota (Temperature)

Teplota je parametr, který řídí náhodnost výstupu generativního AI modelu. Hodnota teploty je mezi 0 a 1, kde 0 znamená deterministický výstup a 1 znamená náhodný výstup. Výchozí hodnota je 0.7.

Podívejme se na příklad, jak teplota funguje, spuštěním tohoto promptu dvakrát:

> Prompt: "Králík na koni, držící lízátko, na mlhavé louce, kde rostou narcisy"

![Králík na koni držící lízátko, verze 1](../../../translated_images/cs/v1-generated-image.a295cfcffa3c13c2.webp)

Nyní spusťme stejný prompt ještě jednou, abychom viděli, že nedostaneme stejný obrázek dvakrát:

![Vygenerovaný obrázek králíka na koni](../../../translated_images/cs/v2-generated-image.33f55a3714efe61d.webp)

Jak vidíte, obrázky jsou podobné, ale ne stejné. Zkusme změnit hodnotu teploty na 0.1 a podívejme se, co se stane:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Zadejte zde svůj text výzvy
        size='1024x1024',
        n=2
    )
```

### Změna teploty

Zkusme tedy udělat odpověď více deterministickou. Můžeme z pozorování dvou vygenerovaných obrázků vidět, že na prvním obrázku je králík a na druhém koník, takže obrázky se velmi liší.

Proto upravme náš kód a nastavme teplotu na 0, takto:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Zadejte zde text svého promptu
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Když nyní tento kód spustíte, získáte tyto dva obrázky:

- ![Teplota 0, verze 1](../../../translated_images/cs/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Teplota 0, verze 2](../../../translated_images/cs/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Zde je jasně vidět, že obrázky jsou si více podobné.

## Jak definovat hranice pro vaši aplikaci pomocí metapromptů

S naší demo aplikací již můžeme generovat obrázky pro naše klienty. Nicméně, potřebujeme vytvořit nějaké hranice pro naši aplikaci.

Například nechceme generovat obrázky, které nejsou vhodné do práce nebo nejsou vhodné pro děti.

Můžeme to udělat pomocí _metapromptů_. Metaprompt jsou textové prompty, které se používají k řízení výstupu generativního AI modelu. Například můžeme použít metaprompt k řízení výstupu a zajistit, aby generované obrázky byly vhodné do práce nebo pro děti.

### Jak to funguje?

Jak tedy metaprompt funguje?

Metaprompt jsou textové prompty, které slouží k řízení výstupu generativního AI modelu, jsou umístěny před textovým promptem a slouží k řízení výstupu modelu a jsou vloženy do aplikací, aby řídily výstup modelu. Kapslují vstup promptu a metapromptu v jediném textovém promptu.

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

Nyní si ukažme, jak můžeme v našem demu použít metaprompt.

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

# TODO přidat požadavek na generování obrázku
```

Z výše uvedeného promptu můžete vidět, jak všechny vytvářené obrázky berou v úvahu metaprompt.

## Zadání - umožněme studentům

Na začátku této lekce jsme představili Edu4All. Nyní je čas studentům umožnit generovat obrázky pro jejich hodnocení.


Studenti vytvoří obrázky pro své hodnocení obsahující památky, které památky to budou, záleží na studentech. Studenti mají v tomto úkolu využít svou kreativitu a umístit tyto památky do různých kontextů.

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

# Získejte koncový bod a klíč z proměnných prostředí
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
    # Vytvořte obrázek pomocí API pro generování obrázků
    generation_response = client.images.generate(
        prompt=prompt,    # Zadejte zde svůj textový prompt
        size='1024x1024',
        n=1,
    )
    # Nastavte adresář pro uložený obrázek
    image_dir = os.path.join(os.curdir, 'images')

    # Pokud adresář neexistuje, vytvořte ho
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Inicializujte cestu k obrázku (pozor, formát souboru by měl být png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Získejte vygenerovaný obrázek
    image_url = generation_response.data[0].url  # Extrahujte URL obrázku z odpovědi
    generated_image = requests.get(image_url).content  # Stáhněte obrázek
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Zobrazte obrázek v implicitním prohlížeči obrázků
    image = Image.open(image_path)
    image.show()

# zachyťte výjimky
except openai.BadRequestError as err:
    print(err)
```

## Skvělá práce! Pokračujte ve svém učení

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali ve zvyšování svých znalostí o Generative AI!

Přejděte na Lekci 10, kde se podíváme na to, jak [vytvářet AI aplikace s nízkým kódem](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->