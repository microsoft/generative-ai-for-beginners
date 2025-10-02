<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T17:22:45+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sv"
}
-->
# Bygga applikationer för bildgenerering

[![Bygga applikationer för bildgenerering](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sv.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Det finns mer med LLM:er än bara textgenerering. Det är också möjligt att skapa bilder utifrån textbeskrivningar. Att ha bilder som en modalitet kan vara väldigt användbart inom många områden, som MedTech, arkitektur, turism, spelutveckling och mycket mer. I det här kapitlet ska vi titta närmare på de två mest populära modellerna för bildgenerering, DALL-E och Midjourney.

## Introduktion

I den här lektionen kommer vi att gå igenom:

- Bildgenerering och varför det är användbart.
- DALL-E och Midjourney, vad de är och hur de fungerar.
- Hur du bygger en applikation för bildgenerering.

## Lärandemål

Efter att ha slutfört denna lektion kommer du kunna:

- Bygga en applikation för bildgenerering.
- Sätta gränser för din applikation med metaprompter.
- Arbeta med DALL-E och Midjourney.

## Varför bygga en applikation för bildgenerering?

Applikationer för bildgenerering är ett utmärkt sätt att utforska möjligheterna med Generativ AI. De kan till exempel användas för:

- **Bildredigering och syntes**. Du kan skapa bilder för olika användningsområden, som bildredigering och bildsyntes.

- **Användas inom olika branscher**. De kan också användas för att generera bilder för olika branscher som Medtech, turism, spelutveckling och mycket mer.

## Scenario: Edu4All

Som en del av denna lektion fortsätter vi att arbeta med vårt startup, Edu4All. Eleverna kommer att skapa bilder till sina uppgifter, exakt vilka bilder är upp till eleverna själva, men det kan till exempel vara illustrationer till deras egen saga, skapa en ny karaktär till sin berättelse eller hjälpa dem att visualisera sina idéer och koncept.

Här är ett exempel på vad Edu4Alls elever kan skapa om de jobbar med monument i klassrummet:

![Edu4All startup, klass om monument, Eiffeltornet](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sv.png)

med en prompt som

> "Hund bredvid Eiffeltornet i tidigt morgonljus"

## Vad är DALL-E och Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) och [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) är två av de mest populära modellerna för bildgenerering, de låter dig använda prompts för att skapa bilder.

### DALL-E

Vi börjar med DALL-E, som är en Generativ AI-modell som skapar bilder utifrån textbeskrivningar.

> [DALL-E är en kombination av två modeller, CLIP och diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** är en modell som skapar inbäddningar, det vill säga numeriska representationer av data, från bilder och text.

- **Diffused attention** är en modell som genererar bilder från inbäddningar. DALL-E är tränad på en datamängd av bilder och text och kan användas för att skapa bilder utifrån textbeskrivningar. Till exempel kan DALL-E användas för att skapa bilder av en katt med hatt, eller en hund med mohawk.

### Midjourney

Midjourney fungerar på liknande sätt som DALL-E, den genererar bilder utifrån textprompter. Midjourney kan också användas för att skapa bilder med prompts som “en katt med hatt” eller “en hund med mohawk”.

![Bild genererad av Midjourney, mekanisk duva](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Bildkälla Wikipedia, bild genererad av Midjourney_

## Hur fungerar DALL-E och Midjourney

Först, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E är en Generativ AI-modell baserad på transformer-arkitektur med en _autoregressiv transformer_.

En _autoregressiv transformer_ beskriver hur en modell genererar bilder från textbeskrivningar, den skapar en pixel i taget och använder de genererade pixlarna för att skapa nästa pixel. Bilden passerar genom flera lager i ett neuralt nätverk tills den är klar.

Med denna process kan DALL-E styra attribut, objekt, egenskaper och mer i bilden den skapar. Dock har DALL-E 2 och 3 ännu mer kontroll över den genererade bilden.

## Bygg din första applikation för bildgenerering

Vad krävs för att bygga en applikation för bildgenerering? Du behöver följande bibliotek:

- **python-dotenv**, det rekommenderas starkt att använda detta bibliotek för att hålla dina hemligheter i en _.env_-fil utanför koden.
- **openai**, detta bibliotek används för att interagera med OpenAI API.
- **pillow**, för att arbeta med bilder i Python.
- **requests**, för att hjälpa dig göra HTTP-anrop.

## Skapa och distribuera en Azure OpenAI-modell

Om du inte redan gjort det, följ instruktionerna på [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
för att skapa en Azure OpenAI-resurs och modell. Välj DALL-E 3 som modell.  

## Skapa appen

1. Skapa en fil _.env_ med följande innehåll:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Hitta denna information i Azure OpenAI Foundry Portal för din resurs under avsnittet "Deployments".

1. Samla ovanstående bibliotek i en fil som heter _requirements.txt_ så här:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Skapa sedan en virtuell miljö och installera biblioteken:

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

Låt oss förklara denna kod:

- Först importerar vi de bibliotek vi behöver, inklusive OpenAI-biblioteket, dotenv-biblioteket, requests-biblioteket och Pillow-biblioteket.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Sedan laddar vi miljövariablerna från _.env_-filen.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Därefter konfigurerar vi Azure OpenAI service-klienten 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Sedan genererar vi bilden:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Koden ovan svarar med ett JSON-objekt som innehåller URL:en till den genererade bilden. Vi kan använda URL:en för att ladda ner bilden och spara den till en fil.

- Slutligen öppnar vi bilden och använder standardbildvisaren för att visa den:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mer om att generera bilden

Låt oss titta närmare på koden som genererar bilden:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** är textprompten som används för att generera bilden. I detta fall använder vi prompten "Kanin på häst, håller en klubba, på en dimmig äng där det växer påskliljor".
- **size** är storleken på bilden som genereras. Här genererar vi en bild som är 1024x1024 pixlar.
- **n** är antalet bilder som genereras. Här genererar vi två bilder.
- **temperature** är en parameter som styr slumpmässigheten i utdata från en Generativ AI-modell. Temperatur är ett värde mellan 0 och 1 där 0 betyder att utdata är deterministisk och 1 betyder att utdata är slumpmässig. Standardvärdet är 0,7.

Det finns fler saker du kan göra med bilder, vilket vi tar upp i nästa avsnitt.

## Ytterligare möjligheter med bildgenerering

Du har hittills sett hur vi kunde generera en bild med några rader Python. Men det finns mer du kan göra med bilder.

Du kan också göra följande:

- **Redigera bilder**. Genom att tillhandahålla en befintlig bild, en mask och en prompt kan du ändra en bild. Till exempel kan du lägga till något på en del av en bild. Tänk dig vår kaninbild, du kan lägga till en hatt på kaninen. Hur du gör det är genom att tillhandahålla bilden, en mask (som identifierar området som ska ändras) och en textprompt som beskriver vad som ska göras. 
> Observera: detta stöds inte i DALL-E 3. 
 
Här är ett exempel med GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Grundbilden skulle bara innehålla loungen med pool, men slutbilden skulle ha en flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Skapa variationer**. Tanken är att du tar en befintlig bild och ber modellen skapa variationer. För att skapa en variation tillhandahåller du en bild och en textprompt och kod som så här:

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

Temperatur är en parameter som styr slumpmässigheten i utdata från en Generativ AI-modell. Temperatur är ett värde mellan 0 och 1 där 0 betyder att utdata är deterministisk och 1 betyder att utdata är slumpmässig. Standardvärdet är 0,7.

Låt oss titta på ett exempel på hur temperatur fungerar genom att köra denna prompt två gånger:

> Prompt: "Kanin på häst, håller en klubba, på en dimmig äng där det växer påskliljor"

![Kanin på häst som håller en klubba, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sv.png)

Nu kör vi samma prompt igen för att se att vi inte får exakt samma bild två gånger:

![Genererad bild av kanin på häst](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sv.png)

Som du ser är bilderna lika, men inte identiska. Låt oss prova att ändra temperaturvärdet till 0,1 och se vad som händer:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Ändra temperaturen

Låt oss försöka göra svaret mer deterministiskt. Vi kunde se från de två bilderna vi genererade att på den första bilden finns en kanin och på den andra en häst, så bilderna skiljer sig mycket åt.

Låt oss därför ändra vår kod och sätta temperaturen till 0, så här:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Nu när du kör denna kod får du dessa två bilder:

- ![Temperatur 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sv.png)
- ![Temperatur 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sv.png)

Här ser du tydligt hur bilderna liknar varandra mer.

## Hur du sätter gränser för din applikation med metaprompter

Med vår demo kan vi redan generera bilder åt våra användare. Men vi behöver skapa vissa gränser för vår applikation.

Till exempel vill vi inte generera bilder som inte är lämpliga på arbetsplatsen eller som inte är passande för barn.

Detta kan vi göra med _metaprompter_. Metaprompter är textprompter som används för att styra utdata från en Generativ AI-modell. Vi kan till exempel använda metaprompter för att styra utdata och säkerställa att de genererade bilderna är lämpliga för arbetsplatsen eller för barn.

### Hur fungerar det?

Hur fungerar då metaprompter?

Metaprompter är textprompter som används för att styra utdata från en Generativ AI-modell, de placeras före textprompten och används för att styra modellens utdata och bäddas in i applikationer för att styra modellens utdata. Man kapslar in promptinmatningen och metapromptinmatningen i en och samma textprompt.

Ett exempel på en metaprompt kan vara följande:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Nu ska vi se hur vi kan använda metaprompter i vår demo.

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

Av prompten ovan kan du se hur alla bilder som skapas tar hänsyn till metaprompten.

## Uppgift – låt oss ge eleverna möjlighet

Vi introducerade Edu4All i början av denna lektion. Nu är det dags att låta eleverna skapa bilder till sina uppgifter.

Eleverna kommer att skapa bilder till sina uppgifter som innehåller monument, exakt vilka monument är upp till eleverna. Eleverna uppmanas att använda sin kreativitet i denna uppgift och placera dessa monument i olika sammanhang.

## Lösning

Här är en möjlig lösning:

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

## Bra jobbat! Fortsätt lära dig
När du har slutfört den här lektionen, ta en titt på vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla dina kunskaper inom Generativ AI!

Gå vidare till Lektion 10 där vi kommer att titta på hur man [bygger AI-applikationer med low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.