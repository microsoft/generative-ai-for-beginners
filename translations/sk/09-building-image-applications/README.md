<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:54:45+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sk"
}
-->
# Vytváranie aplikácií na generovanie obrázkov

[![Vytváranie aplikácií na generovanie obrázkov](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sk.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Generatívne jazykové modely (LLM) nie sú len o generovaní textu. Je možné generovať aj obrázky na základe textových popisov. Obrázky ako modality môžu byť veľmi užitočné v mnohých oblastiach, ako je medicínska technológia, architektúra, cestovný ruch, vývoj hier a ďalšie. V tejto kapitole sa pozrieme na dva najpopulárnejšie modely na generovanie obrázkov: DALL-E a Midjourney.

## Úvod

V tejto lekcii sa budeme venovať:

- Generovaniu obrázkov a jeho užitočnosti.
- Modelom DALL-E a Midjourney, čo sú a ako fungujú.
- Ako vytvoriť aplikáciu na generovanie obrázkov.

## Ciele učenia

Po absolvovaní tejto lekcie budete schopní:

- Vytvoriť aplikáciu na generovanie obrázkov.
- Definovať hranice pre svoju aplikáciu pomocou meta promptov.
- Pracovať s modelmi DALL-E a Midjourney.

## Prečo vytvárať aplikáciu na generovanie obrázkov?

Aplikácie na generovanie obrázkov sú skvelým spôsobom, ako preskúmať schopnosti generatívnej AI. Môžu byť použité napríklad na:

- **Úpravu a syntézu obrázkov**. Môžete generovať obrázky pre rôzne použitia, ako je úprava obrázkov a ich syntéza.

- **Aplikáciu v rôznych odvetviach**. Môžu byť použité na generovanie obrázkov pre rôzne odvetvia, ako je medicínska technológia, cestovný ruch, vývoj hier a ďalšie.

## Scenár: Edu4All

V rámci tejto lekcie budeme pokračovať v práci s naším startupom Edu4All. Študenti budú vytvárať obrázky pre svoje hodnotenia. Aké obrázky si vyberú, je na nich, ale môžu to byť ilustrácie pre ich vlastnú rozprávku, vytvorenie nového charakteru pre ich príbeh alebo pomoc pri vizualizácii ich nápadov a konceptov.

Tu je príklad toho, čo by mohli študenti Edu4All vytvoriť, ak pracujú v triede na téme pamätihodností:

![Startup Edu4All, trieda o pamätihodnostiach, Eiffelova veža](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sk.png)

pomocou promptu ako:

> "Pes vedľa Eiffelovej veže v rannom slnečnom svetle"

## Čo je DALL-E a Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) a [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sú dva z najpopulárnejších modelov na generovanie obrázkov, ktoré umožňujú používať prompty na generovanie obrázkov.

### DALL-E

Začnime s DALL-E, čo je generatívny AI model, ktorý generuje obrázky na základe textových popisov.

> [DALL-E je kombináciou dvoch modelov, CLIP a difúznej pozornosti](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** je model, ktorý generuje embeddings, čo sú číselné reprezentácie dát, z obrázkov a textu.

- **Difúzna pozornosť** je model, ktorý generuje obrázky z embeddings. DALL-E je trénovaný na dátovom súbore obrázkov a textu a môže byť použitý na generovanie obrázkov na základe textových popisov. Napríklad DALL-E môže byť použitý na generovanie obrázkov mačky v klobúku alebo psa s mohawkom.

### Midjourney

Midjourney funguje podobne ako DALL-E, generuje obrázky na základe textových promptov. Midjourney môže byť tiež použitý na generovanie obrázkov pomocou promptov ako „mačka v klobúku“ alebo „pes s mohawkom“.

![Obrázok generovaný Midjourney, mechanický holub](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Obrázok: Wikipedia, generovaný Midjourney_

## Ako fungujú DALL-E a Midjourney

Najprv [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E je generatívny AI model založený na architektúre transformátora s _autoregresívnym transformátorom_.

_Autoregresívny transformátor_ definuje, ako model generuje obrázky na základe textových popisov. Generuje jeden pixel naraz a potom používa vygenerované pixely na generovanie ďalšieho pixelu. Prechádza cez viacero vrstiev v neurónovej sieti, až kým nie je obrázok kompletný.

Pomocou tohto procesu DALL-E kontroluje atribúty, objekty, charakteristiky a ďalšie prvky v generovanom obrázku. Avšak DALL-E 2 a 3 majú väčšiu kontrolu nad generovaným obrázkom.

## Vytvorenie vašej prvej aplikácie na generovanie obrázkov

Čo je potrebné na vytvorenie aplikácie na generovanie obrázkov? Potrebujete nasledujúce knižnice:

- **python-dotenv**, odporúča sa používať túto knižnicu na uchovávanie tajných údajov v súbore _.env_ mimo kódu.
- **openai**, táto knižnica sa používa na interakciu s OpenAI API.
- **pillow**, na prácu s obrázkami v Pythone.
- **requests**, na pomoc pri vytváraní HTTP požiadaviek.

## Vytvorenie a nasadenie modelu Azure OpenAI

Ak ste to ešte neurobili, postupujte podľa pokynov na stránke [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal), aby ste vytvorili zdroj a model Azure OpenAI. Vyberte model DALL-E 3.

## Vytvorenie aplikácie

1. Vytvorte súbor _.env_ s nasledujúcim obsahom:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Nájdite tieto informácie v Azure OpenAI Foundry Portáli pre váš zdroj v sekcii „Deployments“.

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

   Pre Windows použite nasledujúce príkazy na vytvorenie a aktiváciu virtuálneho prostredia:

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

Vysvetlime tento kód:

- Najprv importujeme potrebné knižnice, vrátane knižnice OpenAI, knižnice dotenv, knižnice requests a knižnice Pillow.

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

- Potom nakonfigurujeme klienta služby Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Následne generujeme obrázok:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Vyššie uvedený kód odpovedá JSON objektom, ktorý obsahuje URL vygenerovaného obrázku. URL môžeme použiť na stiahnutie obrázku a jeho uloženie do súboru.

- Nakoniec otvoríme obrázok a použijeme štandardný prehliadač obrázkov na jeho zobrazenie:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Viac detailov o generovaní obrázku

Pozrime sa na kód, ktorý generuje obrázok, podrobnejšie:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** je textový prompt, ktorý sa používa na generovanie obrázku. V tomto prípade používame prompt „Zajac na koni, držiaci lízatko, na hmlistom lúke, kde rastú narcisy“.
- **size** je veľkosť generovaného obrázku. V tomto prípade generujeme obrázok s rozmermi 1024x1024 pixelov.
- **n** je počet generovaných obrázkov. V tomto prípade generujeme dva obrázky.
- **temperature** je parameter, ktorý ovláda náhodnosť výstupu generatívneho AI modelu. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický, a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0,7.

Existuje viac vecí, ktoré môžete robiť s obrázkami, o ktorých sa budeme venovať v ďalšej sekcii.

## Ďalšie schopnosti generovania obrázkov

Doteraz ste videli, ako sme dokázali generovať obrázok pomocou niekoľkých riadkov v Pythone. Existujú však ďalšie veci, ktoré môžete robiť s obrázkami.

Môžete tiež:

- **Vykonávať úpravy**. Poskytnutím existujúceho obrázku, masky a promptu môžete upraviť obrázok. Napríklad môžete pridať niečo na určitú časť obrázku. Predstavte si náš obrázok zajaca, môžete pridať klobúk zajacovi. Ako by ste to urobili, je poskytnutím obrázku, masky (identifikujúcej časť oblasti pre zmenu) a textového promptu, ktorý určuje, čo by sa malo urobiť.
> Poznámka: toto nie je podporované v DALL-E 3.

Tu je príklad pomocou GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Základný obrázok by obsahoval iba salónik s bazénom, ale konečný obrázok by mal plameniaka:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.sk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.sk.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.sk.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Vytvárať variácie**. Myšlienka je, že vezmete existujúci obrázok a požiadate o vytvorenie variácií. Na vytvorenie variácie poskytnete obrázok a textový prompt a kód ako takýto:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Poznámka: toto je podporované iba na OpenAI.

## Teplota

Teplota je parameter, ktorý ovláda náhodnosť výstupu generatívneho AI modelu. Teplota je hodnota medzi 0 a 1, kde 0 znamená, že výstup je deterministický, a 1 znamená, že výstup je náhodný. Predvolená hodnota je 0,7.

Pozrime sa na príklad, ako teplota funguje, spustením tohto promptu dvakrát:

> Prompt: „Zajac na koni, držiaci lízatko, na hmlistom lúke, kde rastú narcisy“

![Zajac na koni držiaci lízatko, verzia 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sk.png)

Teraz spustíme ten istý prompt, aby sme videli, že nedostaneme dvakrát ten istý obrázok:

![Generovaný obrázok zajaca na koni](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sk.png)

Ako vidíte, obrázky sú podobné, ale nie rovnaké. Skúsme zmeniť hodnotu teploty na 0,1 a uvidíme, čo sa stane:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Zmena teploty

Skúsme urobiť odpoveď viac deterministickou. Mohli sme pozorovať z dvoch generovaných obrázkov, že na prvom obrázku je zajac a na druhom obrázku je kôň, takže obrázky sa značne líšia.

Preto zmeníme náš kód a nastavíme teplotu na 0, takto:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Teraz, keď spustíte tento kód, dostanete tieto dva obrázky:

- ![Teplota 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sk.png)
- ![Teplota 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sk.png)

Tu jasne vidíte, ako sa obrázky viac podobajú.

## Ako definovať hranice pre vašu aplikáciu pomocou meta promptov

S našou ukážkou už môžeme generovať obrázky pre našich klientov. Avšak potrebujeme vytvoriť určité hranice pre našu aplikáciu.

Napríklad nechceme generovať obrázky, ktoré nie sú vhodné pre pracovné prostredie alebo ktoré nie sú vhodné pre deti.

Môžeme to urobiť pomocou _meta promptov_. Meta prompty sú textové prompty, ktoré sa používajú na kontrolu výstupu generatívneho AI modelu. Napríklad môžeme použiť meta prompty na kontrolu výstupu a zabezpečiť, že generované obrázky sú vhodné pre pracovné prostredie alebo vhodné pre deti.

### Ako to funguje?

Ako fungujú meta prompty?

Meta prompty sú textové prompty, ktoré sa používajú na kontrolu výstupu generatívneho AI modelu. Sú umiestnené pred textovým promptom a používajú sa na kontrolu výstupu modelu a sú zabudované do aplikácií na kontrolu výstupu modelu. Zahrňujú vstup promptu a vstup meta promptu do jedného textového promptu.

Jedným príkladom meta promptu by bol nasledujúci:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Teraz sa pozrime, ako môžeme použiť meta prompty v našej ukážke.

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

Z vyššie uvedeného promptu môžete vidieť, ako všetky generované obrázky zohľadňujú meta prompt.

## Zadanie - umožnime študentom

Na začiatku tejto lekcie sme predstavili Edu4All. Teraz je čas umožniť študentom generovať obrázky pre ich hodnotenia.

Študenti budú vytvárať obrázky pre svoje hodnotenia obsahujúce pamätihodnosti. Aké pamätihodnosti si vyberú, je na nich. Študenti sú vyzvaní, aby použili svoju kreativitu v tejto úlohe a umiestnili tieto pamätihodnosti do rôznych kontextov.

## Riešenie

Tu je jedno možné riešenie:
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

## Skvelá práca! Pokračujte vo svojom učení

Po dokončení tejto lekcie si pozrite našu [zbierku učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste si ďalej rozšírili svoje znalosti o generatívnej AI!

Prejdite na Lekciu 10, kde sa pozrieme na to, ako [vytvárať AI aplikácie s nízkym kódom](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.