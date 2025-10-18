<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-18T02:41:41+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ta"
}
-->
# படங்களை உருவாக்கும் பயன்பாடுகளை உருவாக்குதல்

[![படங்களை உருவாக்கும் பயன்பாடுகளை உருவாக்குதல்](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ta.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM-களின் திறன்கள் எழுத்து உருவாக்கத்தை விட அதிகம். எழுத்து விளக்கங்களிலிருந்து படங்களை உருவாக்கவும் முடியும். படங்களை ஒரு முறைமையாகக் கொண்டிருப்பது MedTech, கட்டிடக்கலை, சுற்றுலா, விளையாட்டு மேம்பாடு மற்றும் பல பகுதிகளில் மிகவும் பயனுள்ளதாக இருக்கலாம். இந்த அத்தியாயத்தில், மிகவும் பிரபலமான இரண்டு பட உருவாக்க மாடல்களான DALL-E மற்றும் Midjourney பற்றி பார்ப்போம்.

## அறிமுகம்

இந்த பாடத்தில், நாம் கற்கப்போவது:

- பட உருவாக்கம் மற்றும் அதன் பயன்கள்.
- DALL-E மற்றும் Midjourney, அவை என்ன, அவை எப்படி செயல்படுகின்றன.
- ஒரு பட உருவாக்க பயன்பாட்டை எப்படி உருவாக்குவது.

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்த பிறகு, நீங்கள்:

- ஒரு பட உருவாக்க பயன்பாட்டை உருவாக்க முடியும்.
- உங்கள் பயன்பாட்டிற்கான எல்லைகளை மெட்டா ப்ராம்ப்ட்களுடன் வரையறுக்க முடியும்.
- DALL-E மற்றும் Midjourney உடன் வேலை செய்ய முடியும்.

## ஏன் ஒரு பட உருவாக்க பயன்பாட்டை உருவாக்க வேண்டும்?

பட உருவாக்க பயன்பாடுகள் Generative AI-யின் திறன்களை ஆராய ஒரு சிறந்த வழியாகும். அவை பலவகையான பயன்பாடுகளுக்கு பயன்படுத்தப்படலாம், உதாரணமாக:

- **பட திருத்தம் மற்றும் தொகுப்பு**. படங்களைத் திருத்தவும், பலவகையான பயன்பாடுகளுக்காக படங்களை உருவாக்கவும் முடியும்.

- **பல தொழில்களில் பயன்படுத்தப்படுகிறது**. MedTech, Tourism, Game Development போன்ற பல தொழில்களில் படங்களை உருவாக்கவும் பயன்படுத்தலாம்.

## சூழல்: Edu4All

இந்த பாடத்தின் ஒரு பகுதியாக, Edu4All என்ற எங்கள் ஸ்டார்ட்அப் நிறுவனத்துடன் தொடர்ந்து பணியாற்றுவோம். மாணவர்கள் தங்கள் மதிப்பீடுகளுக்கான படங்களை உருவாக்குவார்கள், எந்த வகையான படங்கள் என்பதை மாணவர்கள் தீர்மானிக்க வேண்டும், ஆனால் அவர்கள் தங்கள் சொந்த கதைசொல்லிக்கான விளக்கப்படங்கள் அல்லது தங்கள் கதைக்கான புதிய கதாபாத்திரத்தை உருவாக்கலாம் அல்லது தங்கள் யோசனைகள் மற்றும் கருத்துகளை காட்சிப்படுத்த உதவலாம்.

Edu4All மாணவர்கள், எடுத்துக்காட்டாக, நினைவுச்சின்னங்கள் பற்றிய வகுப்பில் பணியாற்றினால், அவர்கள் உருவாக்கக்கூடியது இதுதான்:

![Edu4All ஸ்டார்ட்அப், நினைவுச்சின்னங்கள் பற்றிய வகுப்பு, ஐஃபெல் கோபுரம்](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ta.png)

ப்ராம்ப்ட் போன்றது:

> "காலை சூரிய ஒளியில் ஐஃபெல் கோபுரத்துக்கு அருகில் நாய்"

## DALL-E மற்றும் Midjourney என்ன?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) மற்றும் [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ஆகியவை மிகவும் பிரபலமான இரண்டு பட உருவாக்க மாடல்கள், அவை ப்ராம்ப்ட்களைப் பயன்படுத்தி படங்களை உருவாக்க அனுமதிக்கின்றன.

### DALL-E

முதலில் DALL-E பற்றி பார்ப்போம், இது எழுத்து விளக்கங்களிலிருந்து படங்களை உருவாக்கும் Generative AI மாடல்.

> [DALL-E என்பது இரண்டு மாடல்களின் இணைப்பு, CLIP மற்றும் diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, இது படங்கள் மற்றும் எழுத்துகளிலிருந்து எம்பெடிங்குகளை உருவாக்கும் மாடல், எம்பெடிங்குகள் என்பது தரவின் எண் பிரதிநிதிகள்.

- **Diffused attention**, இது எம்பெடிங்குகளிலிருந்து படங்களை உருவாக்கும் மாடல். DALL-E படங்கள் மற்றும் எழுத்துகளின் தரவுத்தொகுப்பில் பயிற்சி பெறுகிறது மற்றும் எழுத்து விளக்கங்களிலிருந்து படங்களை உருவாக்க பயன்படுத்தப்படுகிறது. உதாரணமாக, DALL-E ஒரு தொப்பியில் பூனை அல்லது மோகாக் கொண்ட நாயின் படங்களை உருவாக்க பயன்படுத்தப்படலாம்.

### Midjourney

Midjourney DALL-E போலவே செயல்படுகிறது, இது எழுத்து ப்ராம்ப்ட்களிலிருந்து படங்களை உருவாக்குகிறது. Midjourney, "தொப்பியில் பூனை" அல்லது "மோகாக் கொண்ட நாய்" போன்ற ப்ராம்ப்ட்களைப் பயன்படுத்தி படங்களை உருவாக்கவும் பயன்படுத்தப்படலாம்.

![Midjourney மூலம் உருவாக்கப்பட்ட படம், இயந்திர புறா](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_படத்தின் உரிமை: விக்கிபீடியா, Midjourney மூலம் உருவாக்கப்பட்ட படம்_

## DALL-E மற்றும் Midjourney எப்படி செயல்படுகின்றன

முதலில், [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E என்பது _ஆட்டோரிகிரசிவ் டிரான்ஸ்ஃபார்மர்_ கொண்ட டிரான்ஸ்ஃபார்மர் கட்டமைப்பின் அடிப்படையில் உருவாக்கப்பட்ட Generative AI மாடல்.

_ஆட்டோரிகிரசிவ் டிரான்ஸ்ஃபார்மர்_ என்பது ஒரு மாடல் எழுத்து விளக்கங்களிலிருந்து படங்களை உருவாக்கும் விதத்தை வரையறுக்கிறது, இது ஒரு பிக்சலை ஒரே நேரத்தில் உருவாக்குகிறது, பின்னர் உருவாக்கப்பட்ட பிக்சல்களை அடுத்த பிக்சலை உருவாக்க பயன்படுத்துகிறது. நரம்பு வலைப்பின்னலின் பல அடுக்குகள் வழியாக செல்கிறது, படத்தை முழுமையாக்கும் வரை.

இந்த செயல்முறையின் மூலம், DALL-E, உருவாக்கப்படும் படத்தில் பண்புகள், பொருட்கள், குணங்கள் மற்றும் பலவற்றை கட்டுப்படுத்துகிறது. எனினும், DALL-E 2 மற்றும் 3 உருவாக்கப்பட்ட படத்தின் மீது அதிக கட்டுப்பாட்டை கொண்டுள்ளது.

## உங்கள் முதல் பட உருவாக்க பயன்பாட்டை உருவாக்குதல்

பட உருவாக்க பயன்பாட்டை உருவாக்க என்ன தேவை? உங்களுக்கு பின்வரும் நூலகங்கள் தேவை:

- **python-dotenv**, உங்கள் ரகசியங்களை _.env_ கோப்பில் இருந்து விலக்கி வைக்க இந்த நூலகத்தைப் பயன்படுத்த பரிந்துரைக்கப்படுகிறது.
- **openai**, OpenAI API உடன் தொடர்பு கொள்ள இந்த நூலகத்தை நீங்கள் பயன்படுத்துவீர்கள்.
- **pillow**, Python-ல் படங்களுடன் வேலை செய்ய.
- **requests**, HTTP கோரிக்கைகளை செய்ய உதவ.

## Azure OpenAI மாடலை உருவாக்கி வெளியிடுதல்

இன்னும் செய்யப்படவில்லை என்றால், [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) பக்கத்தில் உள்ள வழிமுறைகளைப் பின்பற்றவும்
Azure OpenAI வளம் மற்றும் மாடலை உருவாக்க. DALL-E 3 ஐ மாடலாகத் தேர்ந்தெடுக்கவும்.

## பயன்பாட்டை உருவாக்குதல்

1. _.env_ என்ற ஒரு கோப்பை பின்வரும் உள்ளடக்கத்துடன் உருவாக்கவும்:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   உங்கள் வளத்திற்கான Azure OpenAI Foundry Portal இல் "Deployments" பிரிவில் இந்த தகவலைக் கண்டறியவும்.

1. மேலே உள்ள நூலகங்களை _requirements.txt_ என்ற கோப்பில் சேகரிக்கவும்:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. அடுத்ததாக, மெய்நிகர் சூழலை உருவாக்கி நூலகங்களை நிறுவவும்:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows-க்கு, உங்கள் மெய்நிகர் சூழலை உருவாக்கி செயல்படுத்த பின்வரும் கட்டளைகளைப் பயன்படுத்தவும்:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ என்ற கோப்பில் பின்வரும் குறியீட்டைச் சேர்க்கவும்:

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

இந்த குறியீட்டை விளக்குவோம்:

- முதலில், OpenAI நூலகம், dotenv நூலகம், requests நூலகம் மற்றும் Pillow நூலகம் உள்ளிட்ட தேவையான நூலகங்களை இறக்குமதி செய்கிறோம்.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- அடுத்ததாக, _.env_ கோப்பிலிருந்து சூழல் மாறிகளை ஏற்றுகிறோம்.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- அதன் பிறகு, Azure OpenAI சேவை கிளையண்டை அமைக்கிறோம்

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- அடுத்ததாக, படத்தை உருவாக்குகிறோம்:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  மேலே உள்ள குறியீடு உருவாக்கப்பட்ட படத்தின் URL-ஐ உள்ளடக்கிய JSON பொருளுடன் பதிலளிக்கிறது. இந்த URL ஐப் பயன்படுத்தி படத்தை பதிவிறக்கி ஒரு கோப்பில் சேமிக்கலாம்.

- கடைசியாக, படத்தைத் திறந்து, அதைப் பார்வையிடும் சாதனத்தில் காட்டுகிறோம்:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### படத்தை உருவாக்குவதற்கான கூடுதல் விவரங்கள்

படத்தை உருவாக்கும் குறியீட்டை மேலும் விரிவாகப் பார்ப்போம்:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, இது படத்தை உருவாக்க பயன்படுத்தப்படும் எழுத்து ப்ராம்ப்ட். இந்தக் காட்சியில், "தவளை குதிரையில், லாலிபாப் பிடித்துக்கொண்டு, மங்கலான புல்வெளியில், அங்கு மஞ்சள் பூக்கள் வளர்கின்றன" என்ற ப்ராம்ப்ட்டை பயன்படுத்துகிறோம்.
- **size**, இது உருவாக்கப்படும் படத்தின் அளவு. இந்தக் காட்சியில், 1024x1024 பிக்சல்கள் கொண்ட படத்தை உருவாக்குகிறோம்.
- **n**, இது உருவாக்கப்படும் படங்களின் எண்ணிக்கை. இந்தக் காட்சியில், இரண்டு படங்களை உருவாக்குகிறோம்.
- **temperature**, இது Generative AI மாடலின் வெளியீட்டின் சீரற்ற தன்மையை கட்டுப்படுத்தும் அளவீடு. வெப்பநிலை என்பது 0 மற்றும் 1 இடையிலான மதிப்பு, 0 என்றால் வெளியீடு தீர்மானமாக இருக்கும், 1 என்றால் வெளியீடு சீரற்றதாக இருக்கும். இயல்புநிலை மதிப்பு 0.7 ஆகும்.

படங்களுடன் மேலும் செய்யக்கூடிய விஷயங்கள் உள்ளன, அவற்றை அடுத்த பகுதியில் நாம் காண்போம்.

## பட உருவாக்கத்தின் கூடுதல் திறன்கள்

Python-ல் சில வரிகளைக் கொண்டு ஒரு படத்தை உருவாக்கிய விதத்தை நீங்கள் இதுவரை பார்த்தீர்கள். எனினும், படங்களுடன் மேலும் செய்யக்கூடிய விஷயங்கள் உள்ளன.

நீங்கள் பின்வருவனவற்றையும் செய்யலாம்:

- **திருத்தங்களைச் செய்யுங்கள்**. ஒரு உள்ளடக்கப்படம், ஒரு மாஸ்க் மற்றும் ஒரு ப்ராம்ப்ட் கொடுத்து, ஒரு படத்தை மாற்றலாம். உதாரணமாக, ஒரு படத்தின் ஒரு பகுதியை மாற்றுவதற்கு ஏதாவது ஒன்றைச் சேர்க்கலாம். எங்கள் தவளை படத்தை கற்பனை செய்யுங்கள், நீங்கள் தவளைக்கு ஒரு தொப்பியைச் சேர்க்கலாம். அதை எப்படி செய்வது என்றால், படத்தை, ஒரு மாஸ்க் (மாற்றத்திற்கான பகுதியை அடையாளம் காண) மற்றும் ஒரு எழுத்து ப்ராம்ப்ட்டை வழங்க வேண்டும்.
> குறிப்பு: இது DALL-E 3 இல் ஆதரிக்கப்படவில்லை.

இது GPT Image ஐப் பயன்படுத்தி ஒரு எடுத்துக்காட்டு:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  அடிப்படை படம் லாஞ்ச் மற்றும் பூலுடன் மட்டுமே இருக்கும், ஆனால் இறுதி படம் பிங்கோவுடன் இருக்கும்:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ta.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ta.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ta.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **மாறுபாடுகளை உருவாக்குங்கள்**. கருத்து என்னவென்றால், நீங்கள் ஒரு உள்ளடக்கப்படத்தை எடுத்து, மாறுபாடுகளை உருவாக்க கேட்க வேண்டும். மாறுபாட்டை உருவாக்க, நீங்கள் ஒரு படத்தை மற்றும் ஒரு எழுத்து ப்ராம்ப்ட்டை வழங்க வேண்டும் மற்றும் பின்வருமாறு குறியீட்டை பயன்படுத்த வேண்டும்:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > குறிப்பு, இது OpenAI-ல் மட்டுமே ஆதரிக்கப்படுகிறது.

## வெப்பநிலை

வெப்பநிலை என்பது Generative AI மாடலின் வெளியீட்டின் சீரற்ற தன்மையை கட்டுப்படுத்தும் அளவீடு. வெப்பநிலை என்பது 0 மற்றும் 1 இடையிலான மதிப்பு, 0 என்றால் வெளியீடு தீர்மானமாக இருக்கும், 1 என்றால் வெளியீடு சீரற்றதாக இருக்கும். இயல்புநிலை மதிப்பு 0.7 ஆகும்.

வெப்பநிலை எப்படி செயல்படுகிறது என்பதை ஒரு எடுத்துக்காட்டைப் பார்த்து புரிந்துகொள்வோம், இந்த ப்ராம்ப்ட்டை இரண்டு முறை இயக்குவதன் மூலம்:

> ப்ராம்ப்ட் : "தவளை குதிரையில், லாலிபாப் பிடித்துக்கொண்டு, மங்கலான புல்வெளியில், அங்கு மஞ்சள் பூக்கள் வளர்கின்றன"

![தவளை குதிரையில், லாலிபாப் பிடித்துக்கொண்டு, பதிப்பு 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ta.png)

இப்போது அதே ப்ராம்ப்ட்டை மீண்டும் இயக்கி பார்ப்போம், அதே படத்தை இரண்டு முறை பெற முடியாது:

![தவளை குதிரையில் உருவாக்கப்பட்ட படம்](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ta.png)

நீங்கள் காணலாம், படங்கள் ஒரே மாதிரியானவை, ஆனால் ஒரே மாதிரியானவை அல்ல. வெப்பநிலை மதிப்பை 0.1 ஆக மாற்றி என்ன நடக்கிறது என்று பார்ப்போம்:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### வெப்பநிலையை மாற்றுதல்

எனவே பதிலை மேலும் தீர்மானமாக்க முயற்சிக்கலாம். நாம் உருவாக்கிய இரண்டு படங்களில் முதல் படத்தில் தவளை உள்ளது, இரண்டாவது படத்தில் குதிரை உள்ளது என்பதை கவனிக்கலாம், எனவே படங்கள் மிகவும் மாறுபடுகின்றன.

எனவே, நமது குறியீட்டை மாற்றி, வெப்பநிலையை 0 ஆக அமைக்கலாம், பின்வருமாறு:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

இப்போது நீங்கள் இந்தக் குறியீட்டை இயக்கும்போது, இந்த இரண்டு படங்களைப் பெறுவீர்கள்:

- ![வெப்பநிலை 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ta.png)
- ![வெப்பநிலை 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ta.png)

இங்கே நீங்கள் படங்கள் ஒருவருக்கொருவர் மேலும் ஒத்திருக்கின்றன என்பதை தெளிவாகக் காணலாம்.

## மெட்டா ப்ராம்ப்ட்களுடன் உங்கள் பயன்பாட்டிற்கான எல்லைகளை எப்படி வரையறுப்பது

எங்கள் டெமோவுடன், நாங்கள் ஏற்கனவே எங்கள் வாடிக்கையாளர்களுக்கான படங்களை உருவாக்க முடியும். எனினும், நாங்கள் எங்கள் பயன்பாட்டிற்கான சில எல்லைகளை உருவாக்க வேண்டும்.

உதாரணமாக, வேலைக்கு பாதுகாப்பான அல்லது குழந்தைகளுக்கு பொருத்தமான படங்களை உருவாக்க விரும்பவில்லை.

நாம் இதை _மெட்டா ப்ராம்ப்ட்கள்_ மூலம் செய்யலாம். மெட்டா ப்ராம்ப்ட்கள் Generative AI மாடலின் வெளியீட்டை கட்டுப்படுத்த பயன்படுத்தப்படும் எழுத்து ப்ராம்ப்ட்கள் ஆகும். எடுத்துக்காட்டாக, வெளியீட்டை கட்டுப்படுத்தவும், உருவாக்கப்பட்ட படங்கள் வேலைக்கு பாதுகாப்பானவை அல்லது குழந்தைகளுக்கு பொருத்தமானவை என்பதை உறுதிப்படுத்தவும் மெட்டா ப்ராம்ப்ட்களை பயன்படுத்தலாம்.

### இது எப்படி செயல்படுகிறது?

இப்போது, மெட்டா ப்ராம்ப்ட்கள் எப்படி செயல்படுகின்றன?

மெட்டா ப்ராம்ப்ட்கள் Generative AI மாடலின் வெளியீட்டை கட்டுப்படுத்த பயன்படுத்தப்படும் எழுத்து ப்ராம்ப்ட்கள், அவை எழுத்து ப்ராம்ப்ட்டுக்கு முன் அமைக்கப்பட்டுள்ளன, மற்றும் மாடலின் வெளியீட்டை கட்டுப்படுத்த பயன்படுத்தப்படுகின்றன. மெட்டா ப்ராம்ப்ட் உள்ளீடு மற்றும் ப்ராம்ப்ட் உள்ளீட்டை ஒரே எழுத்து ப்ராம்ப்ட்டில் இணைத்து பயன்பாடுகளில் உள்ளடக்கப்படுகின்றன.

மெட்டா ப்ராம்ப்ட்டின் ஒரு எடுத்துக்காட்டு பின்வருமாறு இருக்கும்:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

இப்போது, எங்கள் டெமோவில் மெட்டா ப்ராம்ப்ட்களை எப்படி பயன்படுத்தலாம் என்பதைப் பார்ப்போம்.

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

மேலே உள்ள ப்ராம்ப்ட்டிலிருந்து, உருவாக்கப்படும் அனைத்து படங்களும் மெட்டா ப்ராம்ப்ட்டை கருத்தில் கொள்கின்றன என்பதை நீங்கள் காணலாம்.

## பணிக்குறிப்பு - மாணவர்களை சாத்தியமாக்குவோம்

இந்த பாடத்தின் தொடக்கத்தில் Edu4All ஐ அறிமுகப்படுத்தினோம். இப்போது மாணவர்களை தங்கள் மதிப்பீடுகளுக்கான படங்களை உருவாக்க சாத்தியமாக்கும் நேரம்.

மாணவர்கள் தங்கள் மதிப்பீடுகளுக்கான நினைவுச்சின்னங்களை உள்ளடக்கிய படங்களை உருவாக்குவார்கள், எந்த நினைவுச்சின்னங்கள் என்பது மாணவர்களின் விருப்பத்திற்கு உட்பட்டது. இந்த பணியில் இந்த நினைவுச்சின்னங்களை வெவ்வேறு சூழல்களில் வைக்க, மாணவர்கள் தங்கள் படைப்பாற்றலை பயன்படுத்துமாறு கேட்டுக்கொள்ளப்படுகிறார்கள்.

## தீர்வு

இங்கே ஒரு சாத்தியமான தீர்வு:
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

## சிறந்த வேலை! உங்கள் கற்றலை தொடருங்கள்

இந்த பாடத்தை முடித்த பிறகு, உங்கள் Generative AI அறிவை மேம்படுத்த [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ஐ பாருங்கள்!

Lesson 10-க்கு செல்லுங்கள், அங்கு [குறைந்த குறியீடு கொண்டு AI பயன்பாடுகளை உருவாக்குவது](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) பற்றி பார்க்கப்போகிறோம்.

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.