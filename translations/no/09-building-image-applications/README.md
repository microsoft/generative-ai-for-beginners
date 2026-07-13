# Lage applikasjoner for bilde-generering

[![Lage applikasjoner for bilde-generering](../../../translated_images/no/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Det er mer med LLM-er enn tekstgenerering. Det er også mulig å generere bilder fra tekstbeskrivelser. Å ha bilder som en modalitet kan være svært nyttig innen flere områder, fra MedTech, arkitektur, turisme, spillutvikling og mer. I dette kapitlet skal vi se på de to mest populære modellene for bilde-generering, DALL-E og Midjourney.

## Introduksjon

I denne leksjonen skal vi dekke:

- Bildegenerering og hvorfor det er nyttig.
- DALL-E og Midjourney, hva de er og hvordan de fungerer.
- Hvordan du kan bygge en applikasjon for bilde-generering.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Bygge en applikasjon for bilde-generering.
- Definere grenser for applikasjonen din med metaprompter.
- Arbeide med DALL-E og Midjourney.

## Hvorfor bygge en applikasjon for bilde-generering?

Applikasjoner for bilde-generering er en flott måte å utforske mulighetene til Generativ AI. De kan brukes til blant annet:

- **Bildebehandling og syntese**. Du kan generere bilder til en rekke bruksområder, som bildebehandling og bildesyntese.

- **Brukt i ulike bransjer**. De kan også brukes til å generere bilder for forskjellige bransjer som Medtech, Turisme, Spillutvikling og mer.

## Scenario: Edu4All

Som en del av denne leksjonen vil vi fortsette å jobbe med startupen vår, Edu4All. Studentene skal lage bilder til sine vurderinger; hva slags bilder det blir bestemmer studentene, men det kan være illustrasjoner til egen eventyrfortelling, lage en ny karakter til historien sin eller hjelpe til med å visualisere ideer og konsepter.

Her er et eksempel på hva Edu4All-studentene kunne generere hvis de jobber i klassen med monumenter:

![Edu4All startup, klasse om monumenter, Eiffeltårnet](../../../translated_images/no/startup.94d6b79cc4bb3f5a.webp)

ved å bruke en prompt som

> "Hund ved siden av Eiffeltårnet i tidlig morgensol"

## Hva er DALL-E og Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) og [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) er to av de mest populære modellene for bilde-generering. De lar deg bruke prompter for å generere bilder.

### DALL-E

La oss starte med DALL-E, som er en Generativ AI-modell som genererer bilder fra tekstbeskrivelser.

> [DALL-E er en kombinasjon av to modeller, CLIP og diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** er en modell som genererer embeddings, som er numeriske representasjoner av data, fra bilder og tekst.

- **Diffused attention** er en modell som genererer bilder fra embeddings. DALL-E er trent på et datasett av bilder og tekst og kan brukes til å generere bilder fra tekstbeskrivelser. For eksempel kan DALL-E brukes til å lage bilder av en katt med hatt, eller en hund med mohawk.

### Midjourney

Midjourney fungerer på en lignende måte som DALL-E; den genererer bilder fra tekstprompter. Midjourney kan også brukes til å generere bilder ved hjelp av prompter som «en katt med hatt» eller «en hund med mohawk».

![Bilde generert av Midjourney, mekanisk due](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildet er hentet fra Wikipedia, generert av Midjourney_

## Hvordan fungerer DALL-E og Midjourney

Først, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E er en Generativ AI-modell basert på transformer-arkitekturen med en _autoregressiv transformer_.

En _autoregressiv transformer_ definerer hvordan en modell genererer bilder fra tekstbeskrivelser; den genererer en piksel av gangen, og bruker de genererte pikslene for å generere neste piksel. Den går gjennom flere lag i et nevralt nettverk, helt til bildet er komplett.

Med denne prosessen kontrollerer DALL-E egenskaper, objekter, trekk og mer i bildet den genererer. Men DALL-E 2 og 3 har mer kontroll over det genererte bildet.

## Bygge din første applikasjon for bilde-generering

Så, hva trenger man for å bygge en applikasjon for bilde-generering? Du trenger følgende biblioteker:

- **python-dotenv**, det anbefales sterkt å bruke dette biblioteket for å holde hemmeligheter i en _.env_-fil unna koden.
- **openai**, dette biblioteket bruker du for å kommunisere med OpenAI API.
- **pillow**, for å arbeide med bilder i Python.
- **requests**, for å gjøre HTTP-forespørsler.

## Opprette og distribuere en Azure OpenAI-modell

Hvis du ikke har gjort det allerede, følg instruksjonene på [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)-siden
for å opprette en Azure OpenAI-ressurs og modell. Velg **gpt-image-1** som modell (nåværende generasjons Azure OpenAI bilde-modell; DALL-E 3 er legacy og ikke lenger tilgjengelig for nye distribusjoner).

## Opprett appen

1. Opprett en fil _.env_ med følgende innhold:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Denne informasjonen finner du i Azure OpenAI Foundry-portalen for ressursen din under "Distribusjoner".

1. Samle de nevnte bibliotekene i en fil kalt _requirements.txt_ slik:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Neste, opprett et virtuelt miljø og installer bibliotekene:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   For Windows, bruk følgende kommandoer for å lage og aktivere ditt virtuelle miljø:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Legg inn følgende kode i filen kalt _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # konfigurer Azure OpenAI-tjenesteklient
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Opprett et bilde ved å bruke bildegenererings-API-et
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Angi katalogen for det lagrede bildet
        image_dir = os.path.join(os.curdir, 'images')

        # Hvis katalogen ikke eksisterer, opprett den
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialiser bildebane (merk at filtypen skal være png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Hent det genererte bildet
        image_url = generation_response.data[0].url  # hent ut bilde-URL fra responsen
        generated_image = requests.get(image_url).content  # last ned bildet
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Vis bildet i standard bildeviser
        image = Image.open(image_path)
        image.show()

    # fang unntak
    except openai.BadRequestError as err:
        print(err)
   ```

La oss forklare denne koden:

- Først importerer vi de nødvendige bibliotekene, inkludert OpenAI-biblioteket, dotenv, requests og Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Deretter laster vi miljøvariablene fra _.env_-filen.

  ```python
  # importer dotenv
  dotenv.load_dotenv()
  ```

- Etter det konfigurerer vi Azure OpenAI-tjenesteklienten.

  ```python
  # Hent endepunkt og nøkkel fra miljøvariabler
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Så genererer vi bildet:

  ```python
  # Opprett et bilde ved å bruke bildegenererings-API-en
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Koden over gir svar med et JSON-objekt som inneholder URL-en til det genererte bildet. Vi kan bruke URL-en for å laste ned bildet og lagre det.

- Til slutt åpner vi bildet og bruker standard bildeviser for å vise det:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mer detaljer om bilde-generering

La oss se mer detaljert på koden som genererer bildet:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** er tekstprompten som brukes til å generere bildet. I dette tilfellet bruker vi prompten "Kanin på hest, holder en slikkepinne, på en tåket eng hvor det vokser påskeliljer".
- **size** er størrelsen på bildet som genereres. Her genererer vi et bilde på 1024x1024 piksler.
- **n** er antallet bilder som genereres. Her genererer vi to bilder.
- **temperature** er en parameter som styrer tilfeldigheten i utdataene fra en Generativ AI-modell. Temperaturen er en verdi mellom 0 og 1 hvor 0 betyr at utdataene er deterministiske og 1 betyr at utdataene er tilfeldige. Standardverdien er 0.7.

Det finnes flere ting du kan gjøre med bilder som vi vil dekke i neste seksjon.

## Ytterligere muligheter med bilde-generering

Du har så langt sett hvordan vi kunne generere et bilde med noen få linjer Python. Men det er mer du kan gjøre med bilder.

Du kan også gjøre følgende:

- **Utføre redigeringer**. Ved å gi et eksisterende bilde, en maske og en prompt kan du endre et bilde. For eksempel kan du legge til noe i en del av bildet. Tenk på vårt kaninbilde; du kan legge hat på kaninen. Hvordan du gjør det er ved å gi bildet, en maske (som identifiserer delen som skal endres) og en tekstprompt som beskriver hva som skal gjøres.
> Merk: dette støttes ikke i DALL-E 3.
 
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

  Basisk bildet inneholder bare loungen med basseng, men det endelige bildet vil ha en flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/no/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/no/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/no/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Lag variasjoner**. Ideen er at du tar et eksisterende bilde og ber om at variasjoner blir laget. For å lage en variasjon gir du et bilde og en tekstprompt og kode slik:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Merk, dette støttes kun på OpenAIs DALL-E 2 modell, ikke gpt-image-1

## Temperatur

Temperatur er en parameter som styrer tilfeldigheten i utdataene fra en Generativ AI-modell. Temperaturen er en verdi mellom 0 og 1 hvor 0 betyr deterministisk utdata og 1 betyr tilfeldige utdata. Standardverdien er 0.7.

La oss se på et eksempel på hvordan temperatur fungerer ved å kjøre denne prompten to ganger:

> Prompt : "Kanin på hest, holder en slikkepinne, på en tåket eng hvor det vokser påskeliljer"

![Kanin på hest som holder en slikkepinne, versjon 1](../../../translated_images/no/v1-generated-image.a295cfcffa3c13c2.webp)

Nå kjører vi den samme prompten bare for å se at vi ikke får samme bilde to ganger:

![Generert bilde av kanin på hest](../../../translated_images/no/v2-generated-image.33f55a3714efe61d.webp)

Som du ser, bildene er like, men ikke identiske. La oss prøve å endre temperaturverdien til 0.1 og se hva som skjer:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Skriv inn promptteksten din her
        size='1024x1024',
        n=2
    )
```

### Endre temperaturen

Så la oss prøve å gjøre responsen mer deterministisk. Vi kan observere fra de to genererte bildene at det i det første bildet er en kanin, og i det andre bildet er det en hest, så bildene varierer mye.

La oss derfor endre koden vår og sette temperaturen til 0, slik:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Skriv inn forespørselsteksten din her
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nå når du kjører denne koden, får du disse to bildene:

- ![Temperatur 0, v1](../../../translated_images/no/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Temperatur 0, v2](../../../translated_images/no/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Her kan du tydelig se hvordan bildene ligner mer på hverandre.

## Hvordan definere grenser for applikasjonen din med metaprompter

Med demoen vår kan vi allerede generere bilder for kundene våre. Men vi må lage noen grenser for applikasjonen vår.

For eksempel ønsker vi ikke å generere bilder som ikke er trygge å vise på jobb, eller som ikke egner seg for barn.

Vi kan gjøre dette med _metaprompter_. Metaprompter er tekstprompter som brukes for å kontrollere utdataene fra en Generativ AI-modell. For eksempel kan vi bruke metaprompter til å kontrollere utdataene og sørge for at de genererte bildene er trygge for jobbsammenhenger, eller egnet for barn.

### Hvordan fungerer det?

Hvordan fungerer metaprompter?

Metaprompter er tekstprompter som brukes for å kontrollere utdataene fra en Generativ AI modell. De plasseres før tekstprompten, og brukes for å kontrollere modellens output. De er innebygd i applikasjoner for å kontrollere modellens utdata. De omslutter både prompt input og meta prompt input i en enkel tekstprompt.

Et eksempel på en metaprompt kan være følgende:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nå, la oss se hvordan vi kan bruke metaprompter i demoen vår.

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

# TODO legg til forespørsel for å generere bilde
```

Fra prompten over kan du se hvordan alle bildene som lages tar hensyn til metaprompten.

## Oppgave - la oss gi studentene muligheten

Vi introduserte Edu4All i begynnelsen av denne leksjonen. Nå er det på tide å gi studentene muligheten til å generere bilder til vurderingene sine.


Studentene skal lage bilder til sine vurderinger som inneholder monumenter, nøyaktig hvilke monumenter er opp til studentene. Studentene blir bedt om å bruke sin kreativitet i denne oppgaven for å plassere disse monumentene i forskjellige kontekster.

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

# Hent endepunkt og nøkkel fra miljøvariabler
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
    # Lag et bilde ved hjelp av bildegenererings-APIet
    generation_response = client.images.generate(
        prompt=prompt,    # Skriv inn prompt-teksten din her
        size='1024x1024',
        n=1,
    )
    # Sett katalogen for det lagrede bildet
    image_dir = os.path.join(os.curdir, 'images')

    # Hvis katalogen ikke finnes, opprett den
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialiser bildebane (merk at filtypen skal være png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Hent det genererte bildet
    image_url = generation_response.data[0].url  # hent ut bilde-URL fra responsen
    generated_image = requests.get(image_url).content  # last ned bildet
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Vis bildet i standard bildeviser
    image = Image.open(image_path)
    image.show()

# fang unntak
except openai.BadRequestError as err:
    print(err)
```

## Flott arbeid! Fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å bygge opp kunnskapen din om Generativ AI!

Gå videre til Leksjon 10 hvor vi skal se på hvordan man [bygger AI-applikasjoner med lavkode](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->