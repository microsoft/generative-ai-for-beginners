# Bygning af billedgenereringsapplikationer

[![Bygning af billedgenereringsapplikationer](../../../translated_images/da/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Der er mere til LLM'er end tekstgenerering. Det er også muligt at generere billeder ud fra tekstbeskrivelser. At have billeder som en modalitet kan være meget nyttigt inden for en række områder fra MedTech, arkitektur, turisme, spiludvikling og mere. I dette kapitel vil vi kigge på de to mest populære billedgenereringsmodeller, DALL-E og Midjourney.

## Introduktion

I denne lektion vil vi dække:

- Billedgenerering og hvorfor det er nyttigt.
- DALL-E og Midjourney, hvad de er, og hvordan de fungerer.
- Hvordan du ville bygge en billedgenereringsapp.

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Bygge en billedgenereringsapplikation.
- Definere grænser for din applikation med metaprompter.
- Arbejde med DALL-E og Midjourney.

## Hvorfor bygge en billedgenereringsapplikation?

Billedgenereringsapplikationer er en fantastisk måde at udforske mulighederne med Generativ AI på. De kan bruges til eksempelvis:

- **Billedredigering og syntese**. Du kan generere billeder til en række forskellige anvendelser, såsom billedredigering og billedsyntese.

- **Anvendt til en række brancher**. De kan også bruges til at generere billeder til en række brancher som Medtech, turisme, spiludvikling og mere.

## Scenarie: Edu4All

Som en del af denne lektion vil vi fortsætte med at arbejde med vores startup, Edu4All, i denne lektion. Eleverne vil skabe billeder til deres vurderinger, præcis hvilke billeder er op til eleverne, men de kunne være illustrationer til deres egen eventyrfortælling eller skabe en ny karakter til deres historie eller hjælpe dem med at visualisere deres ideer og koncepter.

Her er hvad Edu4All's elever kunne generere for eksempel hvis de arbejder i klassen med monumenter:

![Edu4All startup, klasse om monumenter, Eiffeltårnet](../../../translated_images/da/startup.94d6b79cc4bb3f5a.webp)

ved brug af en prompt som

> "Hund ved siden af Eiffeltårnet i tidligt morgenslys"

## Hvad er DALL-E og Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) og [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) er to af de mest populære billedgenereringsmodeller, de tillader dig at bruge prompts til at generere billeder.

### DALL-E

Lad os starte med DALL-E, som er en Generativ AI-model, der genererer billeder ud fra tekstbeskrivelser.

> [DALL-E er en kombination af to modeller, CLIP og diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** er en model, der genererer embeddings, som er numeriske repræsentationer af data, fra billeder og tekst.

- **Diffused attention** er en model, der genererer billeder fra embeddings. DALL-E er trænet på et datasæt af billeder og tekst og kan bruges til at generere billeder ud fra tekstbeskrivelser. For eksempel kan DALL-E bruges til at generere billeder af en kat med hat, eller en hund med mohawk.

### Midjourney

Midjourney fungerer på en lignende måde som DALL-E, den genererer billeder ud fra tekstprompter. Midjourney kan også bruges til at generere billeder med prompts som “en kat med hat” eller en “hund med mohawk”.

![Billede genereret af Midjourney, mekanisk due](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Billedkilde Wikipedia, billede genereret af Midjourney_

## Hvordan fungerer DALL-E og Midjourney

Først [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E er en Generativ AI-model baseret på transformer-arkitekturen med en _autoregressiv transformer_.

En _autoregressiv transformer_ definerer, hvordan en model genererer billeder ud fra tekstbeskrivelser, den genererer én pixel ad gangen og bruger derefter de genererede pixels til at generere den næste pixel. Den passerer gennem flere lag i et neuralt netværk, indtil billedet er færdigt.

Med denne proces styrer DALL-E attributter, objekter, karakteristika og mere i det billede, den genererer. Dog har DALL-E 2 og 3 mere kontrol over det genererede billede.

## Byg din første billedgenereringsapplikation

Så hvad kræver det at bygge en billedgenereringsapplikation? Du har brug for følgende biblioteker:

- **python-dotenv**, det anbefales kraftigt at bruge dette bibliotek til at holde dine hemmeligheder i en _.env_-fil væk fra koden.
- **openai**, dette bibliotek vil du bruge til at interagere med OpenAI API'en.
- **pillow**, til at arbejde med billeder i Python.
- **requests**, til at hjælpe dig med at lave HTTP-forespørgsler.

## Opret og udrul en Azure OpenAI-model

Hvis du ikke allerede har gjort det, følg instruktionerne på [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) siden
for at oprette en Azure OpenAI-ressource og model. Vælg **gpt-image-1** som model (den nuværende generation Azure OpenAI billedmodel; DALL-E 3 er legacy og ikke længere tilgængelig for nye udrulninger).

## Opret appen

1. Opret en fil _.env_ med følgende indhold:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Find disse oplysninger i Azure OpenAI Foundry Portal for din ressource i "Deployments"-sektionen.

1. Saml bibliotekerne ovenfor i en fil kaldet _requirements.txt_ sådan her:

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
    
    # konfigurer Azure OpenAI service klient
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Opret et billede ved at bruge billedgenererings-API'en
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Indstil mappen til det gemte billede
        image_dir = os.path.join(os.curdir, 'images')

        # Hvis mappen ikke findes, opret den
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialiser billedstien (bemærk at filtypen skal være png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Hent det genererede billede
        image_url = generation_response.data[0].url  # udtræk billed-URL fra svar
        generated_image = requests.get(image_url).content  # download billedet
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Vis billedet i standard billedfremviser
        image = Image.open(image_path)
        image.show()

    # fang undtagelser
    except openai.BadRequestError as err:
        print(err)
   ```

Lad os forklare denne kode:

- Først importerer vi de nødvendige biblioteker, herunder OpenAI-biblioteket, dotenv-biblioteket, requests-biblioteket og Pillow-biblioteket.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Dernæst indlæser vi miljøvariablerne fra _.env_-filen.

  ```python
  # importér dotenv
  dotenv.load_dotenv()
  ```

- Derefter konfigurerer vi Azure OpenAI service klienten 

  ```python
  # Hent slutpunkt og nøgle fra miljøvariabler
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Dernæst genererer vi billedet:

  ```python
  # Opret et billede ved hjælp af billedgenererings-API'en
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Koden ovenfor svarer med et JSON-objekt, der indeholder URL'en til det genererede billede. Vi kan bruge URL'en til at downloade billedet og gemme det i en fil.

- Til sidst åbner vi billedet og bruger standard billedfremviser til at vise det:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Flere detaljer om genereringen af billedet

Lad os se nærmere på koden, der genererer billedet:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** er tekstprompten, som bruges til at generere billedet. I dette tilfælde bruger vi prompten "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size** er størrelsen på det genererede billede. I dette tilfælde genererer vi et billede, der er 1024x1024 pixels.
- **n** er antallet af billeder, der genereres. I dette tilfælde genererer vi to billeder.
- **temperature** er en parameter, der styrer tilfældighederne i outputtet fra en Generativ AI-model. Temperaturværdien er mellem 0 og 1, hvor 0 betyder, at outputtet er deterministisk, og 1 betyder, at outputtet er tilfældigt. Standardværdien er 0,7.

Der er flere ting, du kan gøre med billeder, som vi vil dække i det næste afsnit.

## Yderligere kapabiliteter ved billedgenerering

Du har indtil nu set, hvordan vi kunne generere et billede ved hjælp af få linjer i Python. Men der er flere ting, du kan gøre med billeder.

Du kan også gøre følgende:

- **Udføre redigeringer**. Ved at give et eksisterende billede en maske og en prompt kan du ændre et billede. For eksempel kan du tilføje noget til en del af et billede. Forestil dig vores kaninbillede, du kan tilføje en hat til kaninen. Det gøres ved at give billedet, en maske (identificere den del af området, der skal ændres) og en tekstprompt, som siger, hvad der skal gøres. 
> Bemærk: dette understøttes ikke i DALL-E 3. 
 
Her er et eksempel der bruger GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Basisbilledet vil kun indeholde loungen med poolen, men det endelige billede vil have en flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/da/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/da/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/da/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Opret variationer**. Ideen er, at du tager et eksisterende billede og beder om, at der bliver oprettet variationer. For at oprette en variation, giver du et billede og en tekstprompt og kode som dette:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Bemærk, dette understøttes kun på OpenAI’s DALL-E 2-model, ikke gpt-image-1

## Temperatur

Temperatur er en parameter, der styrer tilfældighederne i outputtet fra en Generativ AI-model. Temperaturværdien er mellem 0 og 1, hvor 0 betyder, at outputtet er deterministisk, og 1 betyder, at outputtet er tilfældigt. Standardværdien er 0,7.

Lad os se et eksempel på, hvordan temperaturen fungerer, ved at køre denne prompt to gange:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Kanin på hest med en slikkepind, version 1](../../../translated_images/da/v1-generated-image.a295cfcffa3c13c2.webp)

Nu kører vi den samme prompt igen bare for at se, at vi ikke får det samme billede to gange:

![Genereret billede af kanin på hest](../../../translated_images/da/v2-generated-image.33f55a3714efe61d.webp)

Som du kan se, er billederne lignende, men ikke ens. Lad os prøve at ændre temperaturværdien til 0,1 og se, hvad der sker:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Indtast din prompttekst her
        size='1024x1024',
        n=2
    )
```

### Ændring af temperaturen

Så lad os forsøge at gøre svaret mere deterministisk. Vi kunne i de to genererede billeder observere, at i det første billede er der en kanin, og i det andet billede er der en hest, så billederne varierer meget.

Derfor ændrer vi vores kode og sætter temperaturen til 0, sådan her:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Indtast din prompttekst her
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu, når du kører denne kode, får du disse to billeder:

- ![Temperatur 0, v1](../../../translated_images/da/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatur 0, v2](../../../translated_images/da/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Her kan du tydeligt se, hvordan billederne ligner hinanden mere.

## Hvordan du definerer grænser for din applikation med metaprompter

Med vores demo kan vi allerede generere billeder til vores kunder. Men vi skal lave nogle grænser for vores applikation.

For eksempel ønsker vi ikke at generere billeder, der ikke er arbejdspladsvenlige, eller som ikke er passende for børn.

Dette kan vi gøre med _metaprompter_. Metaprompter er tekstprompter, der bruges til at kontrollere outputtet fra en Generativ AI-model. For eksempel kan vi bruge metaprompter til at kontrollere outputtet og sikre, at de genererede billeder er arbejdspladsvenlige eller passende for børn.

### Hvordan fungerer det?

Nu, hvordan fungerer metaprompter?

Metaprompter er tekstprompter, der bruges til at kontrollere outputtet fra en Generativ AI-model, de placeres foran tekstprompten, og bruges til at kontrollere output fra modellen og indlejres i applikationer til kontrol af output fra modellen. Det indkapsler promptinputtet og metapromptinputtet i en enkelt tekstprompt.

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

Nu skal vi se, hvordan vi kan bruge metaprompter i vores demo.

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

# TODO tilføj anmodning om at generere billede
```

Fra prompten ovenfor kan du se, hvordan alle billeder, der oprettes, tager metaprompten i betragtning.

## Opgave - lad os aktivere eleverne

Vi introducerede Edu4All i begyndelsen af denne lektion. Nu er det tid til at aktivere eleverne til at generere billeder til deres vurderinger.


Eleverne skal lave billeder til deres vurderinger, der indeholder monumenter, præcis hvilke monumenter er op til eleverne. Eleverne bliver bedt om at bruge deres kreativitet i denne opgave til at placere disse monumenter i forskellige kontekster.

## Løsning

Her er en mulig løsning:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Hent endpoint og nøgle fra miljøvariabler
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
    # Opret et billede ved hjælp af billedgenererings-API'en
    generation_response = client.images.generate(
        prompt=prompt,    # Indtast din prompttekst her
        size='1024x1024',
        n=1,
    )
    # Indstil mappen til det gemte billede
    image_dir = os.path.join(os.curdir, 'images')

    # Hvis mappen ikke eksisterer, opret den
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialiser billedstien (bemærk at filtypen skal være png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Hent det genererede billede
    image_url = generation_response.data[0].url  # udtræk billed-URL fra svaret
    generated_image = requests.get(image_url).content  # download billedet
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Vis billedet i standard billedfremviser
    image = Image.open(image_path)
    image.show()

# Fang undtagelser
except openai.BadRequestError as err:
    print(err)
```

## Flot arbejde! Fortsæt din læring

Efter at have gennemført denne lektion, kan du tjekke vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opgradere din viden om Generativ AI!

Gå videre til Lektion 10, hvor vi ser på, hvordan man [bygger AI-applikationer med low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->