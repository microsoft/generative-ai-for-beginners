<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:12:16+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sv"
}
-->
# Bygga applikationer för bildgenerering

[![Bygga applikationer för bildgenerering](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.sv.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Det finns mer att utforska inom LLM än bara textgenerering. Det är också möjligt att generera bilder från textbeskrivningar. Att ha bilder som en modalitet kan vara mycket användbart inom flera områden som MedTech, arkitektur, turism, spelutveckling och mer. I detta kapitel kommer vi att titta på de två mest populära modellerna för bildgenerering, DALL-E och Midjourney.

## Introduktion

I denna lektion kommer vi att täcka:

- Bildgenerering och varför det är användbart.
- DALL-E och Midjourney, vad de är och hur de fungerar.
- Hur du skulle bygga en applikation för bildgenerering.

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Bygga en applikation för bildgenerering.
- Definiera gränser för din applikation med metaprompter.
- Arbeta med DALL-E och Midjourney.

## Varför bygga en applikation för bildgenerering?

Applikationer för bildgenerering är ett utmärkt sätt att utforska kapabiliteterna hos Generativ AI. De kan användas för exempelvis:

- **Bildredigering och syntes**. Du kan generera bilder för olika användningsområden, såsom bildredigering och bildsyntes.

- **Användning inom olika industrier**. De kan också användas för att generera bilder för olika industrier som Medtech, turism, spelutveckling och mer.

## Scenario: Edu4All

Som en del av denna lektion kommer vi att fortsätta arbeta med vår startup, Edu4All. Studenterna kommer att skapa bilder för sina bedömningar, exakt vilka bilder är upp till studenterna, men de kan vara illustrationer för deras egen saga eller skapa en ny karaktär för deras berättelse eller hjälpa dem att visualisera sina idéer och koncept.

Här är vad Edu4Alls studenter kan generera, till exempel om de arbetar i klassen med monument:

![Edu4All startup, klass om monument, Eiffeltornet](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.sv.png)

med en prompt som

> "Hund bredvid Eiffeltornet i tidigt morgonljus"

## Vad är DALL-E och Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) och [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) är två av de mest populära modellerna för bildgenerering, de låter dig använda prompts för att generera bilder.

### DALL-E

Låt oss börja med DALL-E, som är en Generativ AI-modell som genererar bilder från textbeskrivningar.

> [DALL-E är en kombination av två modeller, CLIP och diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, är en modell som genererar embeddings, vilket är numeriska representationer av data, från bilder och text.

- **Diffused attention**, är en modell som genererar bilder från embeddings. DALL-E är tränad på en dataset av bilder och text och kan användas för att generera bilder från textbeskrivningar. Till exempel, DALL-E kan användas för att generera bilder av en katt i en hatt, eller en hund med en mohawk.

### Midjourney

Midjourney fungerar på ett liknande sätt som DALL-E, det genererar bilder från textprompter. Midjourney kan också användas för att generera bilder med prompts som "en katt i en hatt" eller "en hund med en mohawk".

![Bild genererad av Midjourney, mekanisk duva](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildkredit Wikipedia, bild genererad av Midjourney_

## Hur fungerar DALL-E och Midjourney

Först, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E är en Generativ AI-modell baserad på transformerarkitekturen med en _autoregressiv transformer_.

En _autoregressiv transformer_ definierar hur en modell genererar bilder från textbeskrivningar, den genererar en pixel i taget, och använder sedan de genererade pixlarna för att generera nästa pixel. Den passerar genom flera lager i ett neuralt nätverk, tills bilden är komplett.

Med denna process, DALL-E, kontrollerar attribut, objekt, egenskaper och mer i den bild den genererar. Dock har DALL-E 2 och 3 mer kontroll över den genererade bilden.

## Bygga din första applikation för bildgenerering

Så vad krävs det för att bygga en applikation för bildgenerering? Du behöver följande bibliotek:

- **python-dotenv**, du rekommenderas starkt att använda detta bibliotek för att hålla dina hemligheter i en _.env_-fil borta från koden.
- **openai**, detta bibliotek är vad du kommer att använda för att interagera med OpenAI API.
- **pillow**, för att arbeta med bilder i Python.
- **requests**, för att hjälpa dig göra HTTP-förfrågningar.

1. Skapa en fil _.env_ med följande innehåll:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Lokalisera denna information i Azure Portal för din resurs i sektionen "Nycklar och Endpoint".

1. Samla ovanstående bibliotek i en fil som heter _requirements.txt_ så här:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Nästa steg, skapa en virtuell miljö och installera biblioteken:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   För Windows, använd följande kommandon för att skapa och aktivera din virtuella miljö:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Lägg till följande kod i en fil som heter _app.py_:

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

Låt oss förklara denna kod:

- Först, importerar vi de bibliotek vi behöver, inklusive OpenAI-biblioteket, dotenv-biblioteket, requests-biblioteket och Pillow-biblioteket.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Nästa steg, vi laddar miljövariablerna från _.env_-filen.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Efter det, vi ställer in endpoint, nyckel för OpenAI API, version och typ.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Nästa steg, vi genererar bilden:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Koden ovan svarar med ett JSON-objekt som innehåller URL:en för den genererade bilden. Vi kan använda URL:en för att ladda ner bilden och spara den till en fil.

- Slutligen, vi öppnar bilden och använder den standardbildvisaren för att visa den:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mer detaljer om att generera bilden

Låt oss titta på koden som genererar bilden mer i detalj:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, är textprompten som används för att generera bilden. I detta fall använder vi prompten "Kanin på häst, håller en klubba, på en dimmig äng där det växer påskliljor".
- **size**, är storleken på den bild som genereras. I detta fall genererar vi en bild som är 1024x1024 pixlar.
- **n**, är antalet bilder som genereras. I detta fall genererar vi två bilder.
- **temperature**, är en parameter som kontrollerar slumpmässigheten i outputen från en Generativ AI-modell. Temperaturen är ett värde mellan 0 och 1 där 0 betyder att outputen är deterministisk och 1 betyder att outputen är slumpmässig. Standardvärdet är 0.7.

Det finns fler saker du kan göra med bilder som vi kommer att täcka i nästa avsnitt.

## Ytterligare kapabiliteter för bildgenerering

Du har sett hittills hur vi kunde generera en bild med några få rader i Python. Men det finns fler saker du kan göra med bilder.

Du kan också göra följande:

- **Utföra redigeringar**. Genom att tillhandahålla en befintlig bild, en mask och en prompt, kan du ändra en bild. Till exempel, du kan lägga till något till en del av en bild. Föreställ dig vår kaninbild, du kan lägga till en hatt på kaninen. Hur du skulle göra det är genom att tillhandahålla bilden, en mask (identifiera den del av området för förändringen) och en textprompt för att säga vad som ska göras.

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

  Basbilden skulle bara innehålla kaninen men den slutliga bilden skulle ha hatten på kaninen.

- **Skapa variationer**. Idén är att du tar en befintlig bild och ber att variationer skapas. För att skapa en variation, tillhandahåller du en bild och en textprompt och kodar så här:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Observera, detta stöds endast på OpenAI

## Temperatur

Temperatur är en parameter som kontrollerar slumpmässigheten i outputen från en Generativ AI-modell. Temperaturen är ett värde mellan 0 och 1 där 0 betyder att outputen är deterministisk och 1 betyder att outputen är slumpmässig. Standardvärdet är 0.7.

Låt oss titta på ett exempel på hur temperatur fungerar, genom att köra denna prompt två gånger:

> Prompt: "Kanin på häst, håller en klubba, på en dimmig äng där det växer påskliljor"

![Kanin på en häst håller en klubba, version 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.sv.png)

Nu låt oss köra samma prompt bara för att se att vi inte får samma bild två gånger:

![Genererad bild av kanin på häst](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.sv.png)

Som du kan se, bilderna är liknande, men inte samma. Låt oss försöka ändra temperaturvärdet till 0.1 och se vad som händer:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ändra temperaturen

Så låt oss försöka göra svaret mer deterministiskt. Vi kunde observera från de två bilderna vi genererade att i den första bilden finns det en kanin och i den andra bilden finns det en häst, så bilderna varierar mycket.

Låt oss därför ändra vår kod och ställa in temperaturen till 0, så här:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu när du kör denna kod, får du dessa två bilder:

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.sv.png)
- ![Temperatur 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.sv.png)

Här kan du tydligt se hur bilderna liknar varandra mer.

## Hur man definierar gränser för din applikation med metaprompter

Med vår demo kan vi redan generera bilder för våra kunder. Men vi behöver skapa några gränser för vår applikation.

Till exempel, vi vill inte generera bilder som inte är lämpliga för arbetsmiljöer, eller som inte är lämpliga för barn.

Vi kan göra detta med _metaprompter_. Metaprompter är textprompter som används för att kontrollera outputen från en Generativ AI-modell. Till exempel, vi kan använda metaprompter för att kontrollera outputen och säkerställa att de genererade bilderna är lämpliga för arbetsmiljöer, eller lämpliga för barn.

### Hur fungerar det?

Nu, hur fungerar metaprompter?

Metaprompter är textprompter som används för att kontrollera outputen från en Generativ AI-modell, de är placerade före textprompten och används för att kontrollera outputen från modellen och inbäddas i applikationer för att kontrollera outputen från modellen. Inkapsla promptinmatningen och metapromptinmatningen i en enda textprompt.

Ett exempel på en metaprompt skulle vara följande:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nu, låt oss se hur vi kan använda metaprompter i vår demo.

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

Från prompten ovan kan du se hur alla bilder som skapas tar hänsyn till metaprompten.

## Uppgift - låt oss möjliggöra för studenter

Vi introducerade Edu4All i början av denna lektion. Nu är det dags att möjliggöra för studenterna att generera bilder för sina bedömningar.

Studenterna kommer att skapa bilder för sina bedömningar som innehåller monument, exakt vilka monument är upp till studenterna. Studenterna uppmanas att använda sin kreativitet i denna uppgift för att placera dessa monument i olika sammanhang.

## Lösning

Här är en möjlig lösning:

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

## Bra jobbat! Fortsätt ditt lärande

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

Gå vidare till Lektion 10 där vi kommer att titta på hur man [bygger AI-applikationer med lågkod](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiserade översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår vid användningen av denna översättning.