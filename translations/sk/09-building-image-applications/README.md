<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:22:53+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sk"
}
-->
# Vytváranie aplikácií na generovanie obrázkov

[![Vytváranie aplikácií na generovanie obrázkov](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.sk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM sú viac než len generovanie textu. Je možné generovať aj obrázky z textových popisov. Obrázky ako modalita môžu byť veľmi užitočné v mnohých oblastiach, od MedTech, architektúry, turizmu, vývoja hier a ďalších. V tejto kapitole sa pozrieme na dva najpopulárnejšie modely na generovanie obrázkov, DALL-E a Midjourney.

## Úvod

V tejto lekcii sa zameriame na:

- Generovanie obrázkov a prečo je užitočné.
- DALL-E a Midjourney, čo sú zač a ako fungujú.
- Ako by ste mohli vytvoriť aplikáciu na generovanie obrázkov.

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Vytvoriť aplikáciu na generovanie obrázkov.
- Definovať hranice pre vašu aplikáciu pomocou meta promptov.
- Pracovať s DALL-E a Midjourney.

## Prečo vytvárať aplikáciu na generovanie obrázkov?

Aplikácie na generovanie obrázkov sú skvelým spôsobom, ako preskúmať schopnosti Generatívnej AI. Môžu sa použiť napríklad na:

- **Úpravu a syntézu obrázkov**. Môžete generovať obrázky pre rôzne prípady použitia, ako je úprava obrázkov a syntéza obrázkov.

- **Aplikáciu v rôznych odvetviach**. Môžu sa tiež použiť na generovanie obrázkov pre rôzne odvetvia, ako Medtech, Turizmus, Vývoj hier a ďalšie.

## Scenár: Edu4All

V rámci tejto lekcie budeme pokračovať v práci s naším startupom Edu4All. Študenti budú vytvárať obrázky pre svoje hodnotenia, presne aké obrázky je na študentoch, ale môžu to byť ilustrácie pre ich vlastnú rozprávku alebo vytvorenie nového charakteru pre ich príbeh alebo im pomôcť vizualizovať ich nápady a koncepty.

Tu je príklad toho, čo by študenti Edu4All mohli generovať, ak pracujú v triede na pamätníkoch:

![Edu4All startup, trieda na pamätníkoch, Eiffelova veža](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.sk.png)

pomocou promptu ako

> "Pes vedľa Eiffelovej veže v rannom slnečnom svetle"

## Čo je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sú dva z najpopulárnejších modelov na generovanie obrázkov, umožňujú vám používať prompty na generovanie obrázkov.

### DALL-E

Začnime s DALL-E, čo je model Generatívnej AI, ktorý generuje obrázky z textových popisov.

> [DALL-E je kombinácia dvoch modelov, CLIP a rozptýlená pozornosť](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model, ktorý generuje embeddings, čo sú číselné reprezentácie dát, z obrázkov a textu.

- **Rozptýlená pozornosť**, je model, ktorý generuje obrázky z embeddings. DALL-E je trénovaný na dátovom súbore obrázkov a textu a môže sa použiť na generovanie obrázkov z textových popisov. Napríklad, DALL-E môže byť použitý na generovanie obrázkov mačky v klobúku alebo psa s mohawkom.

### Midjourney

Midjourney funguje podobne ako DALL-E, generuje obrázky z textových promptov. Midjourney môže tiež byť použitý na generovanie obrázkov pomocou promptov ako „mačka v klobúku“ alebo „pes s mohawkom“.

![Obrázok generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit obrázku Wikipedia, obrázok generovaný Midjourney_

## Ako funguje DALL-E a Midjourney

Najprv [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model Generatívnej AI založený na transformátorovej architektúre s _autoregresívnym transformátorom_.

_Autoregresívny transformátor_ definuje, ako model generuje obrázky z textových popisov, generuje jeden pixel po druhom a potom používa generované pixely na generovanie ďalšieho pixelu. Prechádza cez viacero vrstiev v neurónovej sieti, až kým nie je obrázok kompletný.

S týmto procesom, DALL-E, kontroluje atribúty, objekty, charakteristiky a ďalšie v obrázku, ktorý generuje. Avšak, DALL-E 2 a 3 majú viac kontroly nad generovaným obrázkom.

## Vytváranie vašej prvej aplikácie na generovanie obrázkov

Takže čo je potrebné na vytvorenie aplikácie na generovanie obrázkov? Potrebujete nasledujúce knižnice:

- **python-dotenv**, je veľmi odporúčané používať túto knižnicu na uchovávanie vašich tajomstiev v súbore _.env_ mimo kódu.
- **openai**, táto knižnica je to, čo použijete na interakciu s OpenAI API.
- **pillow**, na prácu s obrázkami v Pythone.
- **requests**, na pomoc pri vykonávaní HTTP požiadaviek.

1. Vytvorte súbor _.env_ s nasledujúcim obsahom:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Nájdite tieto informácie v Azure Portáli pre váš zdroj v sekcii "Keys and Endpoint".

1. Zozbierajte vyššie uvedené knižnice do súboru _requirements.txt_ takto:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ďalej, vytvorte virtuálne prostredie a nainštalujte knižnice:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pre Windows, použite nasledujúce príkazy na vytvorenie a aktiváciu vášho virtuálneho prostredia:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Pridajte nasledujúci kód do súboru nazvaného _app.py_:

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

Vysvetlime tento kód:

- Najprv importujeme potrebné knižnice, vrátane OpenAI knižnice, dotenv knižnice, requests knižnice a Pillow knižnice.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Ďalej načítame premenné prostredia zo súboru _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Potom nastavíme endpoint, kľúč pre OpenAI API, verziu a typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Ďalej generujeme obrázok:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Vyššie uvedený kód odpovedá s JSON objektom, ktorý obsahuje URL generovaného obrázku. Môžeme použiť URL na stiahnutie obrázku a uloženie do súboru.

- Nakoniec otvoríme obrázok a použijeme štandardný prehliadač obrázkov na jeho zobrazenie:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Viac detailov o generovaní obrázku

Pozrime sa na kód, ktorý generuje obrázok podrobnejšie:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je textový prompt, ktorý sa používa na generovanie obrázku. V tomto prípade používame prompt "Zajac na koni, držiaci lízanku, na zahmlenej lúke, kde rastú narcisy".
- **size**, je veľkosť generovaného obrázku. V tomto prípade generujeme obrázok, ktorý má 1024x1024 pixelov.
- **n**, je počet generovaných obrázkov. V tomto prípade generujeme dva obrázky.
- **temperature**, je parameter, ktorý kontroluje náhodnosť výstupu Generatívnej AI. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0.7.

Existujú ďalšie veci, ktoré môžete robiť s obrázkami, ktoré pokryjeme v nasledujúcej sekcii.

## Ďalšie schopnosti generovania obrázkov

Doteraz ste videli, ako sme boli schopní generovať obrázok pomocou niekoľkých riadkov v Pythone. Existujú však ďalšie veci, ktoré môžete robiť s obrázkami.

Môžete tiež robiť nasledovné:

- **Vykonávať úpravy**. Poskytnutím existujúceho obrázku, masky a promptu môžete zmeniť obrázok. Napríklad môžete pridať niečo na časť obrázku. Predstavte si náš obrázok zajaca, môžete pridať klobúk na zajaca. Ako by ste to urobili, je poskytnutím obrázku, masky (identifikujúcej časť oblasti pre zmenu) a textového promptu, ktorý hovorí, čo by sa malo urobiť.

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

  Základný obrázok by obsahoval iba zajaca, ale konečný obrázok by mal klobúk na zajacovi.

- **Vytvárať variácie**. Myšlienka je, že vezmete existujúci obrázok a požiadate, aby sa vytvorili variácie. Na vytvorenie variácie poskytnete obrázok a textový prompt a kód takto:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka, toto je podporované iba na OpenAI

## Teplota

Teplota je parameter, ktorý kontroluje náhodnosť výstupu Generatívnej AI. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0.7.

Pozrime sa na príklad, ako teplota funguje, spustením tohto promptu dvakrát:

> Prompt: "Zajac na koni, držiaci lízanku, na zahmlenej lúke, kde rastú narcisy"

![Zajac na koni držiaci lízanku, verzia 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.sk.png)

Teraz spustíme ten istý prompt len aby sme videli, že nedostaneme rovnaký obrázok dvakrát:

![Generovaný obrázok zajaca na koni](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.sk.png)

Ako môžete vidieť, obrázky sú podobné, ale nie rovnaké. Skúsme zmeniť hodnotu teploty na 0.1 a uvidíme, čo sa stane:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmena teploty

Skúsme teda urobiť odpoveď viac deterministickou. Mohli sme pozorovať z dvoch generovaných obrázkov, že na prvom obrázku je zajac a na druhom obrázku je kôň, takže obrázky sa veľmi líšia.

Preto zmeníme náš kód a nastavíme teplotu na 0, takto:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, keď spustíte tento kód, dostanete tieto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.sk.png)
- ![Teplota 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.sk.png)

Tu môžete jasne vidieť, ako sa obrázky viac podobajú.

## Ako definovať hranice pre vašu aplikáciu pomocou metapromptov

S naším demom môžeme už generovať obrázky pre našich klientov. Avšak, potrebujeme vytvoriť nejaké hranice pre našu aplikáciu.

Napríklad, nechceme generovať obrázky, ktoré nie sú bezpečné pre prácu alebo ktoré nie sú vhodné pre deti.

To môžeme urobiť pomocou _metapromptov_. Metaprompty sú textové prompty, ktoré sa používajú na kontrolu výstupu Generatívnej AI. Napríklad, môžeme použiť metaprompty na kontrolu výstupu a zabezpečiť, že generované obrázky sú bezpečné pre prácu alebo vhodné pre deti.

### Ako to funguje?

Ako fungujú metaprompty?

Metaprompty sú textové prompty, ktoré sa používajú na kontrolu výstupu Generatívnej AI, sú umiestnené pred textovým promptom a používajú sa na kontrolu výstupu modelu a sú zakomponované do aplikácií na kontrolu výstupu modelu. Zapuzdrujú vstup promptu a vstup metapromptu do jediného textového promptu.

Jedným príkladom metapromptu by bolo nasledovné:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Teraz, pozrime sa, ako môžeme použiť metaprompty v našom deme.

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

Z vyššie uvedeného promptu môžete vidieť, ako všetky vytvorené obrázky zohľadňujú metaprompt.

## Úloha - umožnime študentom

Na začiatku tejto lekcie sme predstavili Edu4All. Teraz je čas umožniť študentom generovať obrázky pre ich hodnotenia.

Študenti budú vytvárať obrázky pre svoje hodnotenia obsahujúce pamätníky, presne aké pamätníky je na študentoch. Študenti sú vyzvaní, aby použili svoju kreativitu v tejto úlohe a umiestnili tieto pamätníky do rôznych kontextov.

## Riešenie

Tu je jedno možné riešenie:

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

## Skvelá práca! Pokračujte vo svojom učení

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zvyšovaní svojej znalosti Generatívnej AI!

Prejdite na Lekciu 10, kde sa pozrieme na to, ako [vytvárať AI aplikácie s nízkym kódom](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.