<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T17:31:29+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "da"
}
-->
# Bygning af billedgenereringsapplikationer

[![Bygning af billedgenereringsapplikationer](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.da.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM’er kan meget mere end bare tekstgenerering. Det er også muligt at generere billeder ud fra tekstbeskrivelser. At have billeder som modalitet kan være utroligt nyttigt inden for mange områder som MedTech, arkitektur, turisme, spiludvikling og meget mere. I dette kapitel ser vi nærmere på de to mest populære billedgenereringsmodeller, DALL-E og Midjourney.

## Introduktion

I denne lektion gennemgår vi:

- Billedgenerering og hvorfor det er nyttigt.
- DALL-E og Midjourney, hvad de er, og hvordan de fungerer.
- Hvordan du kan bygge en billedgenereringsapp.

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Bygge en billedgenereringsapplikation.
- Definere rammer for din applikation med metaprompter.
- Arbejde med DALL-E og Midjourney.

## Hvorfor bygge en billedgenereringsapplikation?

Billedgenereringsapplikationer er en fantastisk måde at udforske mulighederne med Generativ AI. De kan for eksempel bruges til:

- **Billedredigering og syntese**. Du kan generere billeder til mange forskellige formål, som fx billedredigering og billedsyntese.

- **Anvendt i mange brancher**. De kan også bruges til at generere billeder til forskellige brancher som MedTech, turisme, spiludvikling og meget mere.

## Scenarie: Edu4All

Som en del af denne lektion fortsætter vi med at arbejde med vores startup, Edu4All. Eleverne skal skabe billeder til deres opgaver – præcis hvilke billeder, er op til eleverne, men det kan fx være illustrationer til deres eget eventyr, skabe en ny karakter til deres historie eller hjælpe dem med at visualisere deres idéer og koncepter.

Her er et eksempel på, hvad Edu4Alls elever kunne generere, hvis de arbejder med monumenter i klassen:

![Edu4All startup, klasse om monumenter, Eiffeltårnet](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.da.png)

ved at bruge en prompt som

> "Hund ved siden af Eiffeltårnet i tidligt morgensollys"

## Hvad er DALL-E og Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) og [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) er to af de mest populære billedgenereringsmodeller, som gør det muligt at bruge prompts til at generere billeder.

### DALL-E

Lad os starte med DALL-E, som er en Generativ AI-model, der genererer billeder ud fra tekstbeskrivelser.

> [DALL-E er en kombination af to modeller, CLIP og diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** er en model, der genererer embeddings, altså numeriske repræsentationer af data, ud fra billeder og tekst.

- **Diffused attention** er en model, der genererer billeder ud fra embeddings. DALL-E er trænet på et datasæt af billeder og tekst og kan bruges til at generere billeder ud fra tekstbeskrivelser. For eksempel kan DALL-E bruges til at generere billeder af en kat med hat eller en hund med mohawk.

### Midjourney

Midjourney fungerer på samme måde som DALL-E – den genererer billeder ud fra tekstprompter. Midjourney kan også bruges til at generere billeder med prompts som “en kat med hat” eller “en hund med mohawk”.

![Billede genereret af Midjourney, mekanisk due](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Billedkilde Wikipedia, billede genereret af Midjourney_

## Hvordan fungerer DALL-E og Midjourney

Først, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E er en Generativ AI-model baseret på transformer-arkitekturen med en _autoregressiv transformer_.

En _autoregressiv transformer_ definerer, hvordan en model genererer billeder ud fra tekstbeskrivelser – den genererer én pixel ad gangen og bruger de genererede pixels til at lave den næste pixel. Dette gentages gennem flere lag i et neuralt netværk, indtil billedet er færdigt.

Med denne proces kan DALL-E styre attributter, objekter, karakteristika og mere i det billede, der genereres. DALL-E 2 og 3 har dog endnu mere kontrol over det genererede billede.

## Byg din første billedgenereringsapplikation

Hvad skal der til for at bygge en billedgenereringsapplikation? Du skal bruge følgende biblioteker:

- **python-dotenv**, det anbefales kraftigt at bruge dette bibliotek til at holde dine hemmeligheder i en _.env_-fil væk fra koden.
- **openai**, dette bibliotek bruges til at interagere med OpenAI API’et.
- **pillow**, til at arbejde med billeder i Python.
- **requests**, til at hjælpe dig med at lave HTTP-forespørgsler.

## Opret og deploy en Azure OpenAI-model

Hvis du ikke allerede har gjort det, så følg instruktionerne på [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)-siden
for at oprette en Azure OpenAI-ressource og model. Vælg DALL-E 3 som model.  

## Opret appen

1. Opret en fil _.env_ med følgende indhold:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Find disse oplysninger i Azure OpenAI Foundry Portal for din ressource under sektionen "Deployments".

1. Saml ovenstående biblioteker i en fil kaldet _requirements.txt_ således:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Opret derefter et virtuelt miljø og installer bibliotekerne:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   For Windows, brug følgende kommandoer til at oprette og aktivere dit virtuelle miljø:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Tilføj følgende kode i en fil kaldet _app.py_:

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

Lad os forklare denne kode:

- Først importerer vi de nødvendige biblioteker, herunder OpenAI-biblioteket, dotenv, requests og Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Dernæst indlæser vi miljøvariablerne fra _.env_-filen.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Herefter konfigurerer vi Azure OpenAI service-klienten 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Så genererer vi billedet:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Ovenstående kode svarer med et JSON-objekt, der indeholder URL’en til det genererede billede. Vi kan bruge URL’en til at downloade billedet og gemme det i en fil.

- Til sidst åbner vi billedet og bruger standard billedfremviser til at vise det:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Flere detaljer om billedgenereringen

Lad os se nærmere på koden, der genererer billedet:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** er tekstprompten, der bruges til at generere billedet. I dette tilfælde bruger vi prompten "Kanin på hest, holder en slikkepind, på en tåget eng hvor der vokser påskeliljer".
- **size** er størrelsen på det billede, der genereres. Her genererer vi et billede på 1024x1024 pixels.
- **n** er antallet af billeder, der genereres. Her genererer vi to billeder.
- **temperature** er en parameter, der styrer tilfældigheden i outputtet fra en Generativ AI-model. Temperatur er en værdi mellem 0 og 1, hvor 0 betyder, at outputtet er deterministisk, og 1 betyder, at outputtet er tilfældigt. Standardværdien er 0,7.

Der er flere ting, du kan gøre med billeder, som vi gennemgår i næste afsnit.

## Yderligere muligheder med billedgenerering

Du har nu set, hvordan vi kan generere et billede med få linjer Python. Men der er flere ting, du kan gøre med billeder.

Du kan også gøre følgende:

- **Foretage redigeringer**. Ved at give et eksisterende billede en maske og en prompt, kan du ændre et billede. For eksempel kan du tilføje noget til en del af et billede. Forestil dig vores kaninbillede – du kan tilføje en hat til kaninen. Det gør du ved at give billedet, en maske (der identificerer det område, der skal ændres) og en tekstprompt, der beskriver, hvad der skal gøres. 
> Note: dette understøttes ikke i DALL-E 3. 
 
Her er et eksempel med GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Grundbilledet indeholder kun loungen med pool, men det endelige billede har en flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Opret variationer**. Ideen er, at du tager et eksisterende billede og beder om at få lavet variationer. For at lave en variation giver du et billede og en tekstprompt og kode som dette:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note, dette understøttes kun på OpenAI

## Temperatur

Temperatur er en parameter, der styrer tilfældigheden i outputtet fra en Generativ AI-model. Temperatur er en værdi mellem 0 og 1, hvor 0 betyder, at outputtet er deterministisk, og 1 betyder, at outputtet er tilfældigt. Standardværdien er 0,7.

Lad os se et eksempel på, hvordan temperatur fungerer, ved at køre denne prompt to gange:

> Prompt : "Kanin på hest, holder en slikkepind, på en tåget eng hvor der vokser påskeliljer"

![Kanin på hest med slikkepind, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.da.png)

Lad os nu køre den samme prompt igen for at se, at vi ikke får det samme billede to gange:

![Genereret billede af kanin på hest](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.da.png)

Som du kan se, ligner billederne hinanden, men de er ikke ens. Lad os prøve at ændre temperaturværdien til 0,1 og se, hvad der sker:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ændring af temperaturen

Lad os prøve at gøre svaret mere deterministisk. Vi kunne se på de to billeder, vi genererede, at der på det første billede er en kanin, og på det andet billede er der en hest, så billederne varierer meget.

Lad os derfor ændre vores kode og sætte temperaturen til 0, sådan her:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Når du nu kører denne kode, får du disse to billeder:

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.da.png)
- ![Temperatur 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.da.png)

Her kan du tydeligt se, hvordan billederne ligner hinanden mere.

## Sådan definerer du rammer for din applikation med metaprompter

Med vores demo kan vi allerede generere billeder til vores brugere. Men vi skal sætte nogle rammer for vores applikation.

For eksempel ønsker vi ikke at generere billeder, der ikke er egnede til arbejdspladsen, eller som ikke er passende for børn.

Det kan vi gøre med _metaprompter_. Metaprompter er tekstprompter, der bruges til at styre outputtet fra en Generativ AI-model. For eksempel kan vi bruge metaprompter til at styre outputtet og sikre, at de genererede billeder er egnede til arbejdspladsen eller passende for børn.

### Hvordan fungerer det?

Hvordan fungerer metaprompter?

Metaprompter er tekstprompter, der bruges til at styre outputtet fra en Generativ AI-model. De placeres før tekstprompten og bruges til at styre modellens output og indlejres i applikationer for at styre modellens output. Man samler prompt-input og metaprompt-input i én samlet tekstprompt.

Et eksempel på en metaprompt kunne være følgende:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Lad os nu se, hvordan vi kan bruge metaprompter i vores demo.

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

Ud fra ovenstående prompt kan du se, hvordan alle billeder, der bliver skabt, tager højde for metaprompten.

## Opgave – lad os give eleverne mulighed for at prøve

Vi introducerede Edu4All i starten af denne lektion. Nu er det tid til at give eleverne mulighed for at generere billeder til deres opgaver.

Eleverne skal skabe billeder til deres opgaver, der indeholder monumenter – præcis hvilke monumenter, er op til eleverne. Eleverne opfordres til at bruge deres kreativitet i denne opgave og placere monumenterne i forskellige sammenhænge.

## Løsning

Her er én mulig løsning:

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

## Godt arbejde! Fortsæt din læring
Når du har gennemført denne lektion, kan du tage et kig på vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at udvide din viden om Generativ AI!

Gå videre til Lektion 10, hvor vi ser på, hvordan man [bygger AI-applikationer med low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.