<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:33:45+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sk"
}
-->
# Tvorba aplikácií na generovanie obrázkov

[![Tvorba aplikácií na generovanie obrázkov](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM nie sú len o generovaní textu. Je tiež možné generovať obrázky z textových popisov. Mať obrázky ako modalitu môže byť veľmi užitočné v mnohých oblastiach, ako sú MedTech, architektúra, cestovný ruch, vývoj hier a ďalšie. V tejto kapitole sa pozrieme na dva najpopulárnejšie modely na generovanie obrázkov, DALL-E a Midjourney.

## Úvod

V tejto lekcii sa budeme zaoberať:

- Generovanie obrázkov a prečo je užitočné.
- DALL-E a Midjourney, čo sú zač a ako fungujú.
- Ako by ste vytvorili aplikáciu na generovanie obrázkov.

## Ciele učenia

Po dokončení tejto lekcie budete schopní:

- Vytvoriť aplikáciu na generovanie obrázkov.
- Definovať hranice pre vašu aplikáciu pomocou meta promptov.
- Pracovať s DALL-E a Midjourney.

## Prečo vytvárať aplikáciu na generovanie obrázkov?

Aplikácie na generovanie obrázkov sú skvelým spôsobom, ako preskúmať schopnosti Generatívnej AI. Môžu byť použité napríklad na:

- **Úpravu a syntézu obrázkov**. Môžete generovať obrázky pre rôzne použitia, ako je úprava obrázkov a syntéza obrázkov.

- **Použitie v rôznych odvetviach**. Môžu byť tiež použité na generovanie obrázkov pre rôzne odvetvia, ako sú MedTech, cestovný ruch, vývoj hier a ďalšie.

## Scenár: Edu4All

Ako súčasť tejto lekcie budeme pokračovať v práci s našim startupom, Edu4All. Študenti budú vytvárať obrázky pre svoje hodnotenia, presne aké obrázky je na študentoch, ale môžu to byť ilustrácie pre ich vlastnú rozprávku alebo vytvoriť novú postavu pre ich príbeh alebo im pomôcť vizualizovať ich nápady a koncepty.

Tu je príklad, čo by mohli študenti Edu4All vytvoriť, ak pracujú v triede na pamiatkach:

![Edu4All startup, trieda o pamiatkach, Eiffelova veža](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sk.png)

pomocou promptu ako

> "Pes vedľa Eiffelovej veže v rannom slnečnom svetle"

## Čo je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sú dva z najpopulárnejších modelov na generovanie obrázkov, ktoré umožňujú používať prompty na generovanie obrázkov.

### DALL-E

Začnime s DALL-E, čo je model Generatívnej AI, ktorý generuje obrázky z textových popisov.

> [DALL-E je kombináciou dvoch modelov, CLIP a diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, je model, ktorý generuje embeddings, čo sú číselné reprezentácie dát, z obrázkov a textu.

- **Diffused attention**, je model, ktorý generuje obrázky z embeddings. DALL-E je trénovaný na dátovej sade obrázkov a textu a môže byť použitý na generovanie obrázkov z textových popisov. Napríklad, DALL-E môže byť použitý na generovanie obrázkov mačky v klobúku alebo psa s čírom.

### Midjourney

Midjourney funguje podobne ako DALL-E, generuje obrázky z textových promptov. Midjourney môže byť tiež použitý na generovanie obrázkov pomocou promptov ako „mačka v klobúku“ alebo „pes s čírom“.

![Obrázok generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázok z Wikipédie, generovaný Midjourney_

## Ako funguje DALL-E a Midjourney

Najprv [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je model Generatívnej AI založený na transformerovej architektúre s _autoregresívnym transformérom_.

_Autoregresívny transformér_ definuje, ako model generuje obrázky z textových popisov, generuje jeden pixel po druhom a potom používa generované pixely na generovanie ďalšieho pixelu. Prechádza viacerými vrstvami v neurónovej sieti, až kým nie je obrázok kompletný.

Týmto procesom DALL-E riadi atribúty, objekty, charakteristiky a ďalšie v generovanom obrázku. Avšak DALL-E 2 a 3 majú viac kontroly nad generovaným obrázkom.

## Vytváranie vašej prvej aplikácie na generovanie obrázkov

Čo teda potrebujete na vytvorenie aplikácie na generovanie obrázkov? Potrebujete nasledujúce knižnice:

- **python-dotenv**, dôrazne sa odporúča použiť túto knižnicu na uchovávanie vašich tajomstiev v súbore _.env_ mimo kódu.
- **openai**, táto knižnica je to, čo použijete na interakciu s OpenAI API.
- **pillow**, na prácu s obrázkami v Pythone.
- **requests**, na pomoc pri vytváraní HTTP požiadaviek.

1. Vytvorte súbor _.env_ s nasledujúcim obsahom:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Túto informáciu nájdete v Azure Portal pre váš zdroj v sekcii "Keys and Endpoint".

1. Zhromaždite vyššie uvedené knižnice v súbore _requirements.txt_ takto:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ďalej vytvorte virtuálne prostredie a nainštalujte knižnice:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Pre Windows použite nasledujúce príkazy na vytvorenie a aktiváciu virtuálneho prostredia:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Pridajte nasledujúci kód do súboru s názvom _app.py_:

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

- Najprv importujeme knižnice, ktoré potrebujeme, vrátane knižnice OpenAI, knižnice dotenv, knižnice requests a knižnice Pillow.

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

  Vyššie uvedený kód odpovedá JSON objektom, ktorý obsahuje URL generovaného obrázka. Môžeme použiť URL na stiahnutie obrázka a jeho uloženie do súboru.

- Nakoniec otvoríme obrázok a použijeme štandardný prehliadač obrázkov na jeho zobrazenie:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Viac detailov o generovaní obrázka

Pozrime sa na kód, ktorý generuje obrázok podrobnejšie:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, je textový prompt, ktorý sa používa na generovanie obrázka. V tomto prípade používame prompt "Zajac na koni, držiaci lízatko, na hmlistom lúke, kde rastú narcisy".
- **size**, je veľkosť generovaného obrázka. V tomto prípade generujeme obrázok s rozmermi 1024x1024 pixelov.
- **n**, je počet generovaných obrázkov. V tomto prípade generujeme dva obrázky.
- **temperature**, je parameter, ktorý kontroluje náhodnosť výstupu Generatívneho AI modelu. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0.7.

Existujú ďalšie veci, ktoré môžete robiť s obrázkami, ktoré pokryjeme v ďalšej časti.

## Ďalšie schopnosti generovania obrázkov

Videli ste doteraz, ako sme boli schopní generovať obrázok pomocou niekoľkých riadkov v Pythone. Avšak, existujú ďalšie veci, ktoré môžete robiť s obrázkami.

Môžete tiež robiť nasledujúce:

- **Upravovať obrázky**. Poskytnutím existujúceho obrázka, masky a promptu môžete zmeniť obrázok. Napríklad, môžete niečo pridať do časti obrázka. Predstavte si náš obrázok zajaca, môžete pridať klobúk na zajaca. Ako by ste to urobili, je poskytnúť obrázok, masku (identifikujúcu časť oblasti na zmenu) a textový prompt na povedanie, čo by sa malo urobiť.

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

- **Vytvárať variácie**. Myšlienka je, že vezmete existujúci obrázok a požiadate, aby boli vytvorené variácie. Na vytvorenie variácie poskytnete obrázok a textový prompt a kód takto:

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

Teplota je parameter, ktorý kontroluje náhodnosť výstupu Generatívneho AI modelu. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0.7.

Pozrime sa na príklad, ako teplota funguje, spustením tohto promptu dvakrát:

> Prompt : "Zajac na koni, držiaci lízatko, na hmlistom lúke, kde rastú narcisy"

![Zajac na koni držiaci lízatko, verzia 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sk.png)

Teraz spustíme ten istý prompt len na zistenie, že nedostaneme dvakrát ten istý obrázok:

![Generovaný obrázok zajaca na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sk.png)

Ako vidíte, obrázky sú podobné, ale nie rovnaké. Skúsme zmeniť hodnotu teploty na 0.1 a uvidíme, čo sa stane:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmena teploty

Skúsme teda urobiť odpoveď viac deterministickú. Mohli sme pozorovať z dvoch generovaných obrázkov, že na prvom obrázku je zajac a na druhom obrázku je kôň, takže obrázky sa výrazne líšia.

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

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sk.png)
- ![Teplota 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sk.png)

Tu môžete jasne vidieť, ako sa obrázky viac podobajú.

## Ako definovať hranice pre vašu aplikáciu pomocou metapromptov

S našou ukážkou už môžeme generovať obrázky pre našich klientov. Avšak, musíme vytvoriť nejaké hranice pre našu aplikáciu.

Napríklad, nechceme generovať obrázky, ktoré nie sú vhodné na pracovisko, alebo ktoré nie sú vhodné pre deti.

Môžeme to urobiť pomocou _metapromptov_. Metaprompty sú textové prompty, ktoré sa používajú na kontrolu výstupu Generatívneho AI modelu. Napríklad, môžeme použiť metaprompty na kontrolu výstupu a zabezpečiť, že generované obrázky sú vhodné na pracovisko, alebo vhodné pre deti.

### Ako to funguje?

Ako teda metaprompty fungujú?

Metaprompty sú textové prompty, ktoré sa používajú na kontrolu výstupu Generatívneho AI modelu, sú umiestnené pred textovým promptom a používajú sa na kontrolu výstupu modelu a sú zakomponované do aplikácií na kontrolu výstupu modelu. Zapuzdrujú vstup promptu a vstup metapromptu do jedného textového promptu.

Jedným príkladom metapromptu by bol nasledujúci:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Teraz sa pozrime, ako môžeme použiť metaprompty v našej ukážke.

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

Študenti budú vytvárať obrázky pre svoje hodnotenia obsahujúce pamiatky, presne aké pamiatky je na študentoch. Študenti sú požiadaní, aby použili svoju kreativitu v tejto úlohe a umiestnili tieto pamiatky do rôznych kontextov.

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

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia o Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zlepšovaní svojich vedomostí o Generatívnej AI!

Prejdite na lekciu 10, kde sa pozrieme na to, ako [budovať AI aplikácie s nízkym kódom](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.