<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T19:09:53+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sk"
}
-->
# Tvorba aplikácií na generovanie obrázkov

[![Tvorba aplikácií na generovanie obrázkov](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM modely nie sú len o generovaní textu. Je možné generovať aj obrázky na základe textových popisov. Obrázky ako ďalšia modalita môžu byť veľmi užitočné v rôznych oblastiach, ako je medicína, architektúra, cestovný ruch, vývoj hier a ďalšie. V tejto kapitole sa pozrieme na dva najpopulárnejšie modely na generovanie obrázkov – DALL-E a Midjourney.

## Úvod

V tejto lekcii sa budeme venovať:

- Generovaniu obrázkov a jeho využitiu.
- DALL-E a Midjourney – čo sú zač a ako fungujú.
- Ako by ste mohli postaviť vlastnú aplikáciu na generovanie obrázkov.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť:

- Vytvoriť aplikáciu na generovanie obrázkov.
- Nastaviť hranice pre svoju aplikáciu pomocou meta promptov.
- Pracovať s DALL-E a Midjourney.

## Prečo vytvárať aplikáciu na generovanie obrázkov?

Aplikácie na generovanie obrázkov sú skvelým spôsobom, ako preskúmať možnosti generatívnej AI. Môžu sa využiť napríklad na:

- **Úpravu a syntézu obrázkov**. Môžete generovať obrázky pre rôzne prípady použitia, napríklad na úpravu alebo syntézu obrázkov.

- **Využitie v rôznych odvetviach**. Obrázky je možné generovať pre rôzne odvetvia, ako je medicína, cestovný ruch, vývoj hier a ďalšie.

## Scenár: Edu4All

V rámci tejto lekcie budeme pokračovať v práci s naším startupom Edu4All. Študenti budú vytvárať obrázky pre svoje zadania – aké obrázky si zvolia, je na nich. Môžu to byť ilustrácie k vlastnej rozprávke, návrh novej postavy do príbehu alebo vizualizácia ich nápadov a konceptov.

Napríklad, ak študenti v triede pracujú na téme pamiatok, môžu vygenerovať niečo takéto:

![Startup Edu4All, hodina o pamiatkach, Eiffelova veža](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sk.png)

pomocou promptu ako

> "Pes vedľa Eiffelovej veže v rannom slnečnom svetle"

## Čo je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sú dva z najpopulárnejších modelov na generovanie obrázkov, ktoré umožňujú vytvárať obrázky na základe zadaných promptov.

### DALL-E

Začnime s DALL-E, čo je generatívny AI model, ktorý vytvára obrázky z textových popisov.

> [DALL-E je kombináciou dvoch modelov, CLIP a diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ktorý vytvára embeddingy – teda číselné reprezentácie dát – z obrázkov a textu.

- **Diffused attention** je model, ktorý generuje obrázky z embeddingov. DALL-E je trénovaný na množstve obrázkov a textov a dokáže generovať obrázky podľa textového zadania. Napríklad, DALL-E vie vytvoriť obrázok mačky s klobúkom alebo psa s čírom.

### Midjourney

Midjourney funguje podobne ako DALL-E – generuje obrázky na základe textových promptov. Aj tu môžete použiť zadania ako „mačka s klobúkom“ alebo „pes s čírom“.

![Obrázok vygenerovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázok: Wikipedia, vygenerované Midjourney_

## Ako fungujú DALL-E a Midjourney

Najprv [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generatívny AI model založený na transformer architektúre s _autoregresívnym transformerom_.

_Autoregresívny transformer_ určuje, ako model generuje obrázky z textových popisov – generuje jeden pixel za druhým a využíva už vygenerované pixely na vytvorenie ďalšieho. Tento proces prebieha cez viac vrstiev neurónovej siete, až kým nie je obrázok hotový.

Takto DALL-E ovláda vlastnosti, objekty, charakteristiky a ďalšie prvky v generovanom obrázku. Novšie verzie DALL-E 2 a 3 poskytujú ešte väčšiu kontrolu nad výsledkom.

## Vytvorenie prvej aplikácie na generovanie obrázkov

Čo potrebujete na vytvorenie takejto aplikácie? Budete potrebovať tieto knižnice:

- **python-dotenv** – odporúčame použiť túto knižnicu na uchovávanie citlivých údajov v súbore _.env_ mimo zdrojového kódu.
- **openai** – pomocou tejto knižnice budete komunikovať s OpenAI API.
- **pillow** – na prácu s obrázkami v Pythone.
- **requests** – na posielanie HTTP požiadaviek.

## Vytvorenie a nasadenie modelu Azure OpenAI

Ak ste to ešte neurobili, postupujte podľa návodu na stránke [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
a vytvorte si Azure OpenAI resource a model. Ako model zvoľte DALL-E 3.  

## Vytvorenie aplikácie

1. Vytvorte súbor _.env_ s nasledovným obsahom:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Tieto údaje nájdete v Azure OpenAI Foundry Portáli pre váš resource v sekcii "Deployments".

1. Zozbierajte vyššie uvedené knižnice do súboru _requirements.txt_ takto:

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

   Pre Windows použite tieto príkazy na vytvorenie a aktiváciu virtuálneho prostredia:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Pridajte nasledujúci kód do súboru _app.py_:

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

Vysvetlime si tento kód:

- Najskôr importujeme potrebné knižnice vrátane OpenAI, dotenv, requests a Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Potom načítame environmentálne premenné zo súboru _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Následne nakonfigurujeme klienta Azure OpenAI služby

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Potom generujeme obrázok:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Tento kód vráti JSON objekt, ktorý obsahuje URL vygenerovaného obrázka. Túto URL môžeme použiť na stiahnutie obrázka a uloženie do súboru.

- Nakoniec otvoríme obrázok a zobrazíme ho v štandardnom prehliadači obrázkov:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Podrobnejšie o generovaní obrázka

Pozrime sa detailnejšie na kód, ktorý generuje obrázok:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** je textové zadanie, na základe ktorého sa obrázok generuje. V tomto prípade používame prompt "Zajac na koni, držiaci lízanku, na zahmlenej lúke, kde rastú narcisy".
- **size** je veľkosť vygenerovaného obrázka. Tu generujeme obrázok s rozmermi 1024x1024 pixelov.
- **n** je počet vygenerovaných obrázkov. V tomto prípade generujeme dva obrázky.
- **temperature** je parameter, ktorý ovplyvňuje náhodnosť výstupu generatívneho AI modelu. Hodnota je medzi 0 a 1, kde 0 znamená deterministický výstup a 1 úplne náhodný. Predvolená hodnota je 0.7.

S obrázkami sa dá robiť ešte viac, čo si ukážeme v ďalšej časti.

## Ďalšie možnosti generovania obrázkov

Videli ste, že obrázok sa dá vygenerovať pomocou pár riadkov v Pythone. S obrázkami však môžete robiť aj ďalšie veci.

Môžete napríklad:

- **Upravovať obrázky**. Ak poskytnete existujúci obrázok, masku a prompt, môžete obrázok zmeniť. Napríklad môžete do časti obrázka niečo pridať. Predstavte si nášho zajaca – môžete mu pridať klobúk. Stačí zadať obrázok, masku (určujúcu oblasť zmeny) a textový prompt, čo sa má vykonať.
> Poznámka: toto nie je podporované v DALL-E 3.
 
Tu je príklad s GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Pôvodný obrázok obsahuje len lounge s bazénom, ale výsledný obrázok už bude mať aj plameniaka:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Vytvárať variácie**. Môžete zobrať existujúci obrázok a požiadať o vytvorenie jeho variácií. Na to stačí zadať obrázok, textový prompt a použiť kód ako:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: toto je podporované len v OpenAI

## Teplota (Temperature)

Teplota je parameter, ktorý ovplyvňuje náhodnosť výstupu generatívneho AI modelu. Hodnota je medzi 0 a 1, kde 0 znamená deterministický výstup a 1 úplne náhodný. Predvolená hodnota je 0.7.

Pozrime sa na príklad, ako teplota funguje, keď spustíme tento prompt dvakrát:

> Prompt: "Zajac na koni, držiaci lízanku, na zahmlenej lúke, kde rastú narcisy"

![Zajac na koni s lízankou, verzia 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sk.png)

Teraz spustíme ten istý prompt znova, aby sme videli, že nedostaneme dvakrát ten istý obrázok:

![Vygenerovaný obrázok zajaca na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sk.png)

Ako vidíte, obrázky sú si podobné, ale nie sú rovnaké. Skúsme zmeniť hodnotu teploty na 0.1 a pozrime sa, čo sa stane:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmena teploty

Skúsme teda spraviť výstup viac deterministický. Pri dvoch vygenerovaných obrázkoch sme si všimli, že na prvom je zajac a na druhom kôň, takže obrázky sa dosť líšia.

Zmeňme teda kód a nastavme teplotu na 0, takto:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Keď teraz spustíte tento kód, dostanete tieto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sk.png)
- ![Teplota 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sk.png)

Tu jasne vidíte, že obrázky sa na seba viac podobajú.

## Ako nastaviť hranice aplikácie pomocou metapromptov

S našou ukážkou už vieme generovať obrázky pre klientov. Potrebujeme však nastaviť určité hranice pre našu aplikáciu.

Napríklad nechceme generovať obrázky, ktoré nie sú vhodné do práce alebo pre deti.

Na to môžeme použiť _metaprompty_. Metaprompty sú textové zadania, ktoré slúžia na ovládanie výstupu generatívneho AI modelu. Pomocou nich môžeme zabezpečiť, že vygenerované obrázky budú vhodné do práce alebo pre deti.

### Ako to funguje?

Ako teda fungujú meta prompty?

Meta prompty sú textové zadania, ktoré sa používajú na ovládanie výstupu generatívneho AI modelu. Umiestňujú sa pred hlavný prompt a sú súčasťou aplikácie, aby ovplyvnili výstup modelu. Prompt a metaprompt sa spoja do jedného textového zadania.

Príklad metapromptu môže byť:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Pozrime sa, ako môžeme meta prompty použiť v našej ukážke.

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

Z vyššie uvedeného promptu vidíte, že všetky vytvárané obrázky zohľadňujú metaprompt.

## Zadanie – umožnime študentom tvoriť

Na začiatku lekcie sme predstavili Edu4All. Teraz je čas umožniť študentom generovať obrázky pre ich zadania.

Študenti budú vytvárať obrázky s pamiatkami – aké pamiatky si zvolia, je na nich. Majú využiť svoju kreativitu a umiestniť tieto pamiatky do rôznych kontextov.

## Riešenie

Tu je jedno z možných riešení:

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

## Skvelá práca! Pokračujte v učení
Po dokončení tejto lekcie si pozrite našu [kolekciu o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste si ďalej rozširovali vedomosti o generatívnej umelej inteligencii!

Pokračujte na Lekciu 10, kde sa pozrieme na to, ako [vytvárať AI aplikácie s nízkym kódom](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.