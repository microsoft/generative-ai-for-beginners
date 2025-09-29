<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:48:05+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "nl"
}
-->
# Applicaties voor het genereren van afbeeldingen bouwen

[![Applicaties voor het genereren van afbeeldingen bouwen](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.nl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Er is meer mogelijk met LLM's dan alleen tekstgeneratie. Het is ook mogelijk om afbeeldingen te genereren op basis van tekstbeschrijvingen. Het gebruik van afbeeldingen als modaliteit kan zeer nuttig zijn in verschillende gebieden, zoals MedTech, architectuur, toerisme, gameontwikkeling en meer. In dit hoofdstuk bekijken we de twee meest populaire modellen voor het genereren van afbeeldingen: DALL-E en Midjourney.

## Introductie

In deze les behandelen we:

- Het genereren van afbeeldingen en waarom dit nuttig is.
- DALL-E en Midjourney: wat ze zijn en hoe ze werken.
- Hoe je een applicatie voor het genereren van afbeeldingen kunt bouwen.

## Leerdoelen

Na het voltooien van deze les kun je:

- Een applicatie voor het genereren van afbeeldingen bouwen.
- Grenzen definiëren voor je applicatie met metaprompts.
- Werken met DALL-E en Midjourney.

## Waarom een applicatie voor het genereren van afbeeldingen bouwen?

Applicaties voor het genereren van afbeeldingen zijn een geweldige manier om de mogelijkheden van Generatieve AI te verkennen. Ze kunnen bijvoorbeeld worden gebruikt voor:

- **Afbeeldingsbewerking en -synthese**. Je kunt afbeeldingen genereren voor verschillende toepassingen, zoals het bewerken en synthetiseren van afbeeldingen.

- **Toepassing in verschillende industrieën**. Ze kunnen ook worden gebruikt om afbeeldingen te genereren voor verschillende industrieën, zoals MedTech, toerisme, gameontwikkeling en meer.

## Scenario: Edu4All

Als onderdeel van deze les blijven we werken met onze startup, Edu4All. De studenten zullen afbeeldingen maken voor hun opdrachten. Wat voor afbeeldingen ze maken, is aan de studenten, maar ze kunnen bijvoorbeeld illustraties maken voor hun eigen sprookje, een nieuw personage creëren voor hun verhaal, of hen helpen hun ideeën en concepten te visualiseren.

Hier is een voorbeeld van wat de studenten van Edu4All zouden kunnen genereren als ze in de klas werken aan monumenten:

![Edu4All startup, klas over monumenten, Eiffeltoren](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.nl.png)

met een prompt zoals:

> "Hond naast de Eiffeltoren in het ochtendzonlicht"

## Wat zijn DALL-E en Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) en [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) zijn twee van de meest populaire modellen voor het genereren van afbeeldingen. Ze stellen je in staat om afbeeldingen te genereren met behulp van prompts.

### DALL-E

Laten we beginnen met DALL-E, een Generatieve AI-model dat afbeeldingen genereert op basis van tekstbeschrijvingen.

> [DALL-E is een combinatie van twee modellen, CLIP en diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** is een model dat embeddings genereert, numerieke representaties van data, uit afbeeldingen en tekst.

- **Diffused attention** is een model dat afbeeldingen genereert uit embeddings. DALL-E is getraind op een dataset van afbeeldingen en tekst en kan worden gebruikt om afbeeldingen te genereren op basis van tekstbeschrijvingen. Bijvoorbeeld, DALL-E kan worden gebruikt om afbeeldingen te genereren van een kat met een hoed, of een hond met een hanenkam.

### Midjourney

Midjourney werkt op een vergelijkbare manier als DALL-E; het genereert afbeeldingen op basis van tekstprompts. Midjourney kan ook worden gebruikt om afbeeldingen te genereren met prompts zoals "een kat met een hoed" of "een hond met een hanenkam".

![Afbeelding gegenereerd door Midjourney, mechanische duif](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Afbeelding afkomstig van Wikipedia, gegenereerd door Midjourney_

## Hoe werken DALL-E en Midjourney?

Eerst [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E is een Generatieve AI-model gebaseerd op de transformer-architectuur met een _autoregressieve transformer_.

Een _autoregressieve transformer_ bepaalt hoe een model afbeeldingen genereert op basis van tekstbeschrijvingen. Het genereert één pixel tegelijk en gebruikt vervolgens de gegenereerde pixels om de volgende pixel te genereren. Dit proces herhaalt zich door meerdere lagen in een neuraal netwerk totdat de afbeelding compleet is.

Met dit proces kan DALL-E attributen, objecten, kenmerken en meer in de gegenereerde afbeelding beheersen. DALL-E 2 en 3 bieden echter meer controle over de gegenereerde afbeelding.

## Je eerste applicatie voor het genereren van afbeeldingen bouwen

Wat heb je nodig om een applicatie voor het genereren van afbeeldingen te bouwen? Je hebt de volgende bibliotheken nodig:

- **python-dotenv**, het wordt sterk aanbevolen om deze bibliotheek te gebruiken om je geheimen in een _.env_-bestand te bewaren, weg van de code.
- **openai**, deze bibliotheek gebruik je om te communiceren met de OpenAI API.
- **pillow**, om met afbeeldingen in Python te werken.
- **requests**, om HTTP-verzoeken te maken.

## Een Azure OpenAI-model maken en implementeren

Als dit nog niet is gedaan, volg dan de instructies op de [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) pagina om een Azure OpenAI-resource en -model te maken. Selecteer DALL-E 3 als model.  

## De applicatie maken

1. Maak een bestand _.env_ met de volgende inhoud:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Zoek deze informatie in het Azure OpenAI Foundry Portal voor je resource in de sectie "Deployments".

1. Verzamel de bovenstaande bibliotheken in een bestand genaamd _requirements.txt_ zoals hieronder:

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

   Voor Windows gebruik je de volgende commando's om je virtuele omgeving te maken en te activeren:

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

Laten we deze code uitleggen:

- Eerst importeren we de bibliotheken die we nodig hebben, waaronder de OpenAI-bibliotheek, de dotenv-bibliotheek, de requests-bibliotheek en de Pillow-bibliotheek.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Vervolgens laden we de omgevingsvariabelen uit het _.env_-bestand.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Daarna configureren we de Azure OpenAI-serviceclient.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Vervolgens genereren we de afbeelding:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  De bovenstaande code geeft een JSON-object terug dat de URL van de gegenereerde afbeelding bevat. We kunnen de URL gebruiken om de afbeelding te downloaden en op te slaan in een bestand.

- Tot slot openen we de afbeelding en gebruiken we de standaard afbeeldingsviewer om deze weer te geven:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Meer details over het genereren van de afbeelding

Laten we de code die de afbeelding genereert in meer detail bekijken:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** is de tekstprompt die wordt gebruikt om de afbeelding te genereren. In dit geval gebruiken we de prompt "Konijn op paard, met een lolly, op een mistige weide waar narcissen groeien".
- **size** is de grootte van de gegenereerde afbeelding. In dit geval genereren we een afbeelding van 1024x1024 pixels.
- **n** is het aantal afbeeldingen dat wordt gegenereerd. In dit geval genereren we twee afbeeldingen.
- **temperature** is een parameter die de willekeurigheid van de output van een Generatieve AI-model controleert. De temperatuur is een waarde tussen 0 en 1, waarbij 0 betekent dat de output deterministisch is en 1 betekent dat de output willekeurig is. De standaardwaarde is 0,7.

Er zijn meer dingen die je kunt doen met afbeeldingen, die we in de volgende sectie zullen behandelen.

## Aanvullende mogelijkheden voor het genereren van afbeeldingen

Je hebt tot nu toe gezien hoe we een afbeelding konden genereren met slechts een paar regels Python. Er zijn echter meer dingen die je kunt doen met afbeeldingen.

Je kunt ook het volgende doen:

- **Bewerkingen uitvoeren**. Door een bestaande afbeelding, een masker en een prompt te geven, kun je een afbeelding wijzigen. Bijvoorbeeld, je kunt iets toevoegen aan een deel van een afbeelding. Stel je onze konijn-afbeelding voor; je kunt een hoed toevoegen aan het konijn. Hoe je dat doet, is door de afbeelding, een masker (dat het deel van het gebied voor de wijziging identificeert) en een tekstprompt te geven om te zeggen wat er moet worden gedaan. 
> Opmerking: dit wordt niet ondersteund in DALL-E 3. 
 
Hier is een voorbeeld met GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  De basisafbeelding zou alleen de lounge met zwembad bevatten, maar de uiteindelijke afbeelding zou een flamingo hebben:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.nl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.nl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.nl.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Variaties creëren**. Het idee is dat je een bestaande afbeelding neemt en vraagt om variaties te maken. Om een variatie te creëren, geef je een afbeelding en een tekstprompt en code zoals hieronder:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Opmerking: dit wordt alleen ondersteund door OpenAI.

## Temperatuur

Temperatuur is een parameter die de willekeurigheid van de output van een Generatieve AI-model controleert. De temperatuur is een waarde tussen 0 en 1, waarbij 0 betekent dat de output deterministisch is en 1 betekent dat de output willekeurig is. De standaardwaarde is 0,7.

Laten we een voorbeeld bekijken van hoe temperatuur werkt door deze prompt twee keer uit te voeren:

> Prompt: "Konijn op paard, met een lolly, op een mistige weide waar narcissen groeien"

![Konijn op een paard met een lolly, versie 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.nl.png)

Nu voeren we dezelfde prompt opnieuw uit om te zien dat we niet twee keer dezelfde afbeelding krijgen:

![Gegenereerde afbeelding van konijn op paard](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.nl.png)

Zoals je kunt zien, lijken de afbeeldingen op elkaar, maar zijn ze niet hetzelfde. Laten we proberen de temperatuurwaarde te veranderen naar 0,1 en kijken wat er gebeurt:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### De temperatuur veranderen

Laten we proberen de respons meer deterministisch te maken. We konden uit de twee afbeeldingen die we genereerden observeren dat er in de eerste afbeelding een konijn is en in de tweede afbeelding een paard, dus de afbeeldingen variëren sterk.

Laten we daarom onze code wijzigen en de temperatuur instellen op 0, zoals hieronder:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu, wanneer je deze code uitvoert, krijg je deze twee afbeeldingen:

- ![Temperatuur 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.nl.png)
- ![Temperatuur 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.nl.png)

Hier kun je duidelijk zien hoe de afbeeldingen meer op elkaar lijken.

## Hoe grenzen definiëren voor je applicatie met metaprompts

Met onze demo kunnen we al afbeeldingen genereren voor onze klanten. We moeten echter enkele grenzen stellen voor onze applicatie.

Bijvoorbeeld, we willen geen afbeeldingen genereren die niet geschikt zijn voor op de werkplek of die niet geschikt zijn voor kinderen.

We kunnen dit doen met _metaprompts_. Metaprompts zijn tekstprompts die worden gebruikt om de output van een Generatieve AI-model te controleren. Bijvoorbeeld, we kunnen metaprompts gebruiken om de output te controleren en ervoor te zorgen dat de gegenereerde afbeeldingen geschikt zijn voor op de werkplek of geschikt zijn voor kinderen.

### Hoe werkt het?

Hoe werken metaprompts?

Metaprompts zijn tekstprompts die worden gebruikt om de output van een Generatieve AI-model te controleren. Ze worden vóór de tekstprompt geplaatst en worden gebruikt om de output van het model te controleren en ingebed in applicaties om de output van het model te controleren. Ze encapsuleren de promptinput en de metapromptinput in een enkele tekstprompt.

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

Nu, laten we zien hoe we metaprompts kunnen gebruiken in onze demo.

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

We hebben Edu4All geïntroduceerd aan het begin van deze les. Nu is het tijd om de studenten in staat te stellen afbeeldingen te genereren voor hun opdrachten.

De studenten zullen afbeeldingen maken voor hun opdrachten met monumenten. Welke monumenten ze kiezen, is aan de studenten. Ze worden gevraagd hun creativiteit te gebruiken in deze taak om deze monumenten in verschillende contexten te plaatsen.

## Oplossing

Hier is een mogelijke oplossing:
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

## Goed gedaan! Ga door met leren

Na het voltooien van deze les, bekijk onze [Generative AI Learning-collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder uit te breiden!

Ga naar Les 10, waar we gaan kijken hoe je [AI-toepassingen kunt bouwen met low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.