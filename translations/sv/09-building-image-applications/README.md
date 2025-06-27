<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:23:00+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sv"
}
-->
# Bygga applikationer för bildgenerering

[![Bygga applikationer för bildgenerering](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sv.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Det finns mer till LLMs än textgenerering. Det är också möjligt att generera bilder från textbeskrivningar. Att ha bilder som en modalitet kan vara mycket användbart inom flera områden som MedTech, arkitektur, turism, spelutveckling och mer. I detta kapitel kommer vi att titta på de två mest populära bildgenereringsmodellerna, DALL-E och Midjourney.

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

Applikationer för bildgenerering är ett utmärkt sätt att utforska kapaciteterna hos Generativ AI. De kan användas för exempelvis:

- **Bildredigering och syntes**. Du kan generera bilder för olika användningsområden, såsom bildredigering och bildsyntes.

- **Tillämpas på olika industrier**. De kan också användas för att generera bilder för olika industrier som Medtech, turism, spelutveckling och mer.

## Scenario: Edu4All

Som en del av denna lektion kommer vi att fortsätta arbeta med vår startup, Edu4All, i denna lektion. Studenterna kommer att skapa bilder för sina bedömningar, exakt vilka bilder är upp till studenterna, men de kan vara illustrationer för deras egen saga eller skapa en ny karaktär för sin berättelse eller hjälpa dem att visualisera sina idéer och koncept.

Här är vad Edu4Alls studenter skulle kunna generera till exempel om de arbetar i klassen med monument:

![Edu4All startup, klass om monument, Eiffeltornet](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sv.png)

med en prompt som

> "Hund bredvid Eiffeltornet i tidigt morgonljus"

## Vad är DALL-E och Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) och [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) är två av de mest populära bildgenereringsmodellerna, de låter dig använda prompts för att generera bilder.

### DALL-E

Låt oss börja med DALL-E, som är en Generativ AI-modell som genererar bilder från textbeskrivningar.

> [DALL-E är en kombination av två modeller, CLIP och diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, är en modell som genererar embeddings, vilket är numeriska representationer av data, från bilder och text.

- **Diffused attention**, är en modell som genererar bilder från embeddings. DALL-E är tränad på en dataset av bilder och text och kan användas för att generera bilder från textbeskrivningar. Till exempel kan DALL-E användas för att generera bilder av en katt i en hatt, eller en hund med en mohawk.

### Midjourney

Midjourney fungerar på liknande sätt som DALL-E, det genererar bilder från textprompter. Midjourney kan också användas för att generera bilder med prompter som "en katt i en hatt" eller "en hund med en mohawk".

![Bild genererad av Midjourney, mekanisk duva](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildkredit Wikipedia, bild genererad av Midjourney_

## Hur fungerar DALL-E och Midjourney

Först, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E är en Generativ AI-modell baserad på transformerarkitekturen med en _autoregressiv transformer_.

En _autoregressiv transformer_ definierar hur en modell genererar bilder från textbeskrivningar, den genererar en pixel i taget, och använder sedan de genererade pixlarna för att generera nästa pixel. Den passerar genom flera lager i ett neuralt nätverk, tills bilden är komplett.

Med denna process kontrollerar DALL-E attribut, objekt, egenskaper och mer i bilden den genererar. Dock har DALL-E 2 och 3 mer kontroll över den genererade bilden.

## Bygga din första applikation för bildgenerering

Så vad krävs för att bygga en applikation för bildgenerering? Du behöver följande bibliotek:

- **python-dotenv**, det rekommenderas starkt att använda detta bibliotek för att hålla dina hemligheter i en _.env_ fil bort från koden.
- **openai**, detta bibliotek är vad du kommer att använda för att interagera med OpenAI API.
- **pillow**, för att arbeta med bilder i Python.
- **requests**, för att hjälpa dig göra HTTP-förfrågningar.

1. Skapa en fil _.env_ med följande innehåll:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Hitta denna information i Azure Portal för din resurs i avsnittet "Keys and Endpoint".

1. Samla de ovanstående biblioteken i en fil som heter _requirements.txt_ så här:

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

- Först importerar vi de bibliotek vi behöver, inklusive OpenAI-biblioteket, dotenv-biblioteket, requests-biblioteket och Pillow-biblioteket.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Nästa steg, vi laddar miljövariablerna från _.env_ filen.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Därefter, vi ställer in endpoint, nyckel för OpenAI API, version och typ.

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

- Till sist, vi öppnar bilden och använder standard bildvisaren för att visa den:

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
- **temperature**, är en parameter som styr slumpmässigheten i utdata från en Generativ AI-modell. Temperaturen är ett värde mellan 0 och 1 där 0 betyder att utdata är deterministisk och 1 betyder att utdata är slumpmässig. Standardvärdet är 0.7.

Det finns fler saker du kan göra med bilder som vi kommer att täcka i nästa avsnitt.

## Ytterligare kapaciteter för bildgenerering

Du har hittills sett hur vi kunde generera en bild med några få rader i Python. Men det finns fler saker du kan göra med bilder.

Du kan också göra följande:

- **Utföra redigeringar**. Genom att tillhandahålla en befintlig bild, en mask och en prompt, kan du ändra en bild. Till exempel kan du lägga till något till en del av en bild. Föreställ dig vår kaninbild, du kan lägga till en hatt till kaninen. Hur du skulle göra det är genom att tillhandahålla bilden, en mask (identifiera delen av området för ändringen) och en textprompt för att säga vad som ska göras.

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

- **Skapa variationer**. Idén är att du tar en befintlig bild och ber att variationer skapas. För att skapa en variation tillhandahåller du en bild och en textprompt och kod som så här:

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

Temperatur är en parameter som styr slumpmässigheten i utdata från en Generativ AI-modell. Temperaturen är ett värde mellan 0 och 1 där 0 betyder att utdata är deterministisk och 1 betyder att utdata är slumpmässig. Standardvärdet är 0.7.

Låt oss titta på ett exempel på hur temperatur fungerar genom att köra denna prompt två gånger:

> Prompt : "Kanin på häst, håller en klubba, på en dimmig äng där det växer påskliljor"

![Kanin på en häst håller en klubba, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sv.png)

Nu låt oss köra samma prompt bara för att se att vi inte kommer att få samma bild två gånger:

![Genererad bild av kanin på häst](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sv.png)

Som du kan se är bilderna lika, men inte samma. Låt oss prova att ändra temperaturvärdet till 0.1 och se vad som händer:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ändra temperaturen

Så låt oss försöka göra svaret mer deterministiskt. Vi kunde observera från de två bilderna vi genererade att i den första bilden finns det en kanin och i den andra bilden finns det en häst, så bilderna varierar mycket.

Låt oss därför ändra vår kod och ställa in temperaturen till 0, som så här:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu när du kör denna kod får du dessa två bilder:

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sv.png)
- ![Temperatur 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sv.png)

Här kan du tydligt se hur bilderna liknar varandra mer.

## Hur man definierar gränser för din applikation med metaprompter

Med vår demo kan vi redan generera bilder för våra kunder. Men vi behöver skapa några gränser för vår applikation.

Till exempel vill vi inte generera bilder som inte är säkra för arbete, eller som inte är lämpliga för barn.

Vi kan göra detta med _metaprompter_. Metaprompter är textprompter som används för att kontrollera utdata från en Generativ AI-modell. Till exempel kan vi använda metaprompter för att kontrollera utdata och säkerställa att de genererade bilderna är säkra för arbete eller lämpliga för barn.

### Hur fungerar det?

Nu, hur fungerar metaprompter?

Metaprompter är textprompter som används för att kontrollera utdata från en Generativ AI-modell, de placeras före textprompten och används för att kontrollera utdata från modellen och inbäddas i applikationer för att kontrollera utdata från modellen. Kapsla in promptinmatningen och metapromptinmatningen i en enda textprompt.

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

Från ovanstående prompt kan du se hur alla bilder som skapas tar hänsyn till metaprompten.

## Uppgift - låt oss ge eleverna möjligheter

Vi introducerade Edu4All i början av denna lektion. Nu är det dags att ge eleverna möjligheter att generera bilder för sina bedömningar.

Eleverna kommer att skapa bilder för sina bedömningar som innehåller monument, exakt vilka monument är upp till eleverna. Eleverna ombeds att använda sin kreativitet i denna uppgift för att placera dessa monument i olika sammanhang.

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

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta att utveckla din kunskap om Generativ AI!

Gå vidare till Lektion 10 där vi kommer att titta på hur man [bygger AI-applikationer med låg kod](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.