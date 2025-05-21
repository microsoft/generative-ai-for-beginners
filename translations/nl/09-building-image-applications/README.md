<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:16:06+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "nl"
}
-->
# Toepassingen voor afbeeldingsgeneratie bouwen

Er is meer aan LLMs dan alleen tekstgeneratie. Het is ook mogelijk om afbeeldingen te genereren vanuit tekstbeschrijvingen. Afbeeldingen als modaliteit kunnen zeer nuttig zijn in verschillende gebieden, van MedTech, architectuur, toerisme, game-ontwikkeling en meer. In dit hoofdstuk zullen we kijken naar de twee meest populaire modellen voor afbeeldingsgeneratie, DALL-E en Midjourney.

## Inleiding

In deze les behandelen we:

- Afbeeldingsgeneratie en waarom het nuttig is.
- DALL-E en Midjourney, wat ze zijn en hoe ze werken.
- Hoe je een applicatie voor afbeeldingsgeneratie zou bouwen.

## Leerdoelen

Na het voltooien van deze les kun je:

- Een applicatie voor afbeeldingsgeneratie bouwen.
- Grenzen voor je applicatie definiëren met metaprompts.
- Werken met DALL-E en Midjourney.

## Waarom een applicatie voor afbeeldingsgeneratie bouwen?

Applicaties voor afbeeldingsgeneratie zijn een geweldige manier om de mogelijkheden van Generatieve AI te verkennen. Ze kunnen bijvoorbeeld worden gebruikt voor:

- **Afbeeldingsbewerking en synthese**. Je kunt afbeeldingen genereren voor verschillende toepassingen, zoals afbeeldingsbewerking en afbeeldingssynthese.

- **Toegepast in verschillende industrieën**. Ze kunnen ook worden gebruikt om afbeeldingen te genereren voor verschillende industrieën zoals Medtech, Toerisme, Game-ontwikkeling en meer.

## Scenario: Edu4All

Als onderdeel van deze les blijven we werken met onze startup, Edu4All. De studenten zullen afbeeldingen maken voor hun beoordelingen, precies welke afbeeldingen is aan de studenten, maar ze kunnen illustraties zijn voor hun eigen sprookje of een nieuw personage voor hun verhaal creëren of hen helpen hun ideeën en concepten te visualiseren.

Hier is een voorbeeld van wat Edu4All's studenten zouden kunnen genereren als ze in de klas werken aan monumenten:

![Edu4All startup, klas over monumenten, Eiffeltoren](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.nl.png)

met een prompt zoals

> "Hond naast de Eiffeltoren in de vroege ochtendzon"

## Wat zijn DALL-E en Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) en [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) zijn twee van de meest populaire modellen voor afbeeldingsgeneratie, ze stellen je in staat om met prompts afbeeldingen te genereren.

### DALL-E

Laten we beginnen met DALL-E, een Generatieve AI-model dat afbeeldingen genereert vanuit tekstbeschrijvingen.

> [DALL-E is een combinatie van twee modellen, CLIP en diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, is een model dat embeddings genereert, wat numerieke representaties van data zijn, vanuit afbeeldingen en tekst.

- **Diffused attention**, is een model dat afbeeldingen genereert vanuit embeddings. DALL-E is getraind op een dataset van afbeeldingen en tekst en kan worden gebruikt om afbeeldingen te genereren vanuit tekstbeschrijvingen. Bijvoorbeeld, DALL-E kan worden gebruikt om afbeeldingen te genereren van een kat met een hoed, of een hond met een hanenkam.

### Midjourney

Midjourney werkt op een vergelijkbare manier als DALL-E, het genereert afbeeldingen vanuit tekstprompts. Midjourney kan ook worden gebruikt om afbeeldingen te genereren met prompts zoals "een kat met een hoed", of een "hond met een hanenkam".

![Afbeelding gegenereerd door Midjourney, mechanische duif](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Afbeelding cred Wikipedia, afbeelding gegenereerd door Midjourney_

## Hoe werken DALL-E en Midjourney

Eerst, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E is een Generatieve AI-model gebaseerd op de transformer architectuur met een _autoregressieve transformer_.

Een _autoregressieve transformer_ definieert hoe een model afbeeldingen genereert vanuit tekstbeschrijvingen, het genereert één pixel tegelijk, en gebruikt dan de gegenereerde pixels om de volgende pixel te genereren. Dit proces gaat door meerdere lagen in een neuraal netwerk, totdat de afbeelding compleet is.

Met dit proces controleert DALL-E, attributen, objecten, kenmerken en meer in de afbeelding die het genereert. Echter, DALL-E 2 en 3 hebben meer controle over de gegenereerde afbeelding.

## Je eerste applicatie voor afbeeldingsgeneratie bouwen

Wat is er nodig om een applicatie voor afbeeldingsgeneratie te bouwen? Je hebt de volgende bibliotheken nodig:

- **python-dotenv**, je wordt sterk aangeraden om deze bibliotheek te gebruiken om je geheimen in een _.env_ bestand weg te houden van de code.
- **openai**, deze bibliotheek gebruik je om te communiceren met de OpenAI API.
- **pillow**, om met afbeeldingen in Python te werken.
- **requests**, om je te helpen HTTP-verzoeken te maken.

1. Maak een bestand _.env_ met de volgende inhoud:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Zoek deze informatie in Azure Portal voor je resource in de sectie "Keys and Endpoint".

1. Verzamel de bovenstaande bibliotheken in een bestand genaamd _requirements.txt_ zoals volgt:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Maak vervolgens een virtuele omgeving en installeer de bibliotheken:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Voor Windows, gebruik de volgende commando's om je virtuele omgeving te maken en te activeren:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Voeg de volgende code toe in een bestand genaamd _app.py_:

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

Laten we deze code uitleggen:

- Eerst importeren we de bibliotheken die we nodig hebben, inclusief de OpenAI bibliotheek, de dotenv bibliotheek, de requests bibliotheek en de Pillow bibliotheek.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Vervolgens laden we de omgevingsvariabelen uit het _.env_ bestand.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Daarna stellen we het eindpunt, de sleutel voor de OpenAI API, versie en type in.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Vervolgens genereren we de afbeelding:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  De bovenstaande code reageert met een JSON-object dat de URL van de gegenereerde afbeelding bevat. We kunnen de URL gebruiken om de afbeelding te downloaden en op te slaan in een bestand.

- Ten slotte openen we de afbeelding en gebruiken de standaard afbeeldingsviewer om deze weer te geven:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Meer details over het genereren van de afbeelding

Laten we naar de code kijken die de afbeelding genereert in meer detail:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, is de tekstprompt die wordt gebruikt om de afbeelding te genereren. In dit geval gebruiken we de prompt "Konijn op paard, met een lolly, op een mistige weide waar narcissen groeien".
- **size**, is de grootte van de afbeelding die wordt gegenereerd. In dit geval genereren we een afbeelding van 1024x1024 pixels.
- **n**, is het aantal afbeeldingen dat wordt gegenereerd. In dit geval genereren we twee afbeeldingen.
- **temperature**, is een parameter die de willekeurigheid van de output van een Generatieve AI-model controleert. De temperatuur is een waarde tussen 0 en 1 waarbij 0 betekent dat de output deterministisch is en 1 betekent dat de output willekeurig is. De standaardwaarde is 0.7.

Er zijn meer dingen die je met afbeeldingen kunt doen die we in de volgende sectie zullen behandelen.

## Aanvullende mogelijkheden van afbeeldingsgeneratie

Je hebt tot nu toe gezien hoe we in staat waren om een afbeelding te genereren met een paar regels in Python. Er zijn echter meer dingen die je met afbeeldingen kunt doen.

Je kunt ook het volgende doen:

- **Bewerkingen uitvoeren**. Door een bestaande afbeelding een masker en een prompt te geven, kun je een afbeelding wijzigen. Bijvoorbeeld, je kunt iets toevoegen aan een deel van een afbeelding. Stel je onze konijnenafbeelding voor, je kunt een hoed toevoegen aan het konijn. Hoe je dat zou doen is door de afbeelding, een masker (dat het deel van het gebied voor de verandering identificeert) en een tekstprompt te geven om te zeggen wat er moet worden gedaan.

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

  De basisafbeelding zou alleen het konijn bevatten, maar de uiteindelijke afbeelding zou de hoed op het konijn hebben.

- **Variaties creëren**. Het idee is dat je een bestaande afbeelding neemt en vraagt dat er variaties worden gemaakt. Om een variatie te creëren, geef je een afbeelding en een tekstprompt en code zoals volgt:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Opmerking, dit wordt alleen ondersteund op OpenAI

## Temperatuur

Temperatuur is een parameter die de willekeurigheid van de output van een Generatieve AI-model controleert. De temperatuur is een waarde tussen 0 en 1 waarbij 0 betekent dat de output deterministisch is en 1 betekent dat de output willekeurig is. De standaardwaarde is 0.7.

Laten we eens kijken naar een voorbeeld van hoe temperatuur werkt, door deze prompt twee keer uit te voeren:

> Prompt: "Konijn op paard, met een lolly, op een mistige weide waar narcissen groeien"

![Konijn op een paard met een lolly, versie 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.nl.png)

Laten we nu diezelfde prompt nog eens uitvoeren om te zien dat we niet twee keer dezelfde afbeelding krijgen:

![Gegenereerde afbeelding van konijn op paard](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.nl.png)

Zoals je kunt zien, zijn de afbeeldingen vergelijkbaar, maar niet hetzelfde. Laten we proberen de temperatuurwaarde te veranderen naar 0.1 en zien wat er gebeurt:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### De temperatuur veranderen

Laten we dus proberen de reactie meer deterministisch te maken. We konden observeren van de twee afbeeldingen die we genereerden dat in de eerste afbeelding er een konijn is en in de tweede afbeelding een paard, dus de afbeeldingen variëren sterk.

Laten we daarom onze code veranderen en de temperatuur instellen op 0, zoals volgt:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu, wanneer je deze code uitvoert, krijg je deze twee afbeeldingen:

- ![Temperatuur 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.nl.png)
- ![Temperatuur 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.nl.png)

Hier kun je duidelijk zien hoe de afbeeldingen meer op elkaar lijken.

## Hoe grenzen voor je applicatie definiëren met metaprompts

Met onze demo kunnen we al afbeeldingen genereren voor onze klanten. We moeten echter enkele grenzen creëren voor onze applicatie.

Bijvoorbeeld, we willen geen afbeeldingen genereren die niet geschikt zijn voor werk, of die niet geschikt zijn voor kinderen.

We kunnen dit doen met _metaprompts_. Metaprompts zijn tekstprompts die worden gebruikt om de output van een Generatieve AI-model te controleren. Bijvoorbeeld, we kunnen metaprompts gebruiken om de output te controleren en ervoor te zorgen dat de gegenereerde afbeeldingen geschikt zijn voor werk, of geschikt zijn voor kinderen.

### Hoe werkt het?

Nu, hoe werken metaprompts?

Metaprompts zijn tekstprompts die worden gebruikt om de output van een Generatieve AI-model te controleren, ze worden vóór de tekstprompt geplaatst en worden gebruikt om de output van het model te controleren en ingebed in applicaties om de output van het model te controleren. Ze kapselen de promptinvoer en de metapromptinvoer in een enkele tekstprompt in.

Een voorbeeld van een metaprompt zou het volgende zijn:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Laten we nu eens kijken hoe we metaprompts kunnen gebruiken in onze demo.

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

Uit de bovenstaande prompt kun je zien hoe alle afbeeldingen die worden gemaakt rekening houden met de metaprompt.

## Opdracht - laten we studenten in staat stellen

We hebben Edu4All aan het begin van deze les geïntroduceerd. Nu is het tijd om de studenten in staat te stellen afbeeldingen te genereren voor hun beoordelingen.

De studenten zullen afbeeldingen maken voor hun beoordelingen die monumenten bevatten, precies welke monumenten is aan de studenten. De studenten worden gevraagd hun creativiteit in deze taak te gebruiken om deze monumenten in verschillende contexten te plaatsen.

## Oplossing

Hier is een mogelijke oplossing:

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

## Geweldig werk! Ga door met je leerproces

Na het voltooien van deze les, bekijk onze [Generatieve AI Leerverzameling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder te verdiepen!

Ga naar Les 10 waar we zullen kijken hoe we [AI-toepassingen met low-code kunnen bouwen](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.