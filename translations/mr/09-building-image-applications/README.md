<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:49:52+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "mr"
}
-->
# इमेज जनरेशन अ‍ॅप्लिकेशन्स तयार करणे

[![इमेज जनरेशन अ‍ॅप्लिकेशन्स तयार करणे](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.mr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs केवळ मजकूर जनरेशनपुरते मर्यादित नाहीत. मजकूर वर्णनांमधून प्रतिमा तयार करणे देखील शक्य आहे. प्रतिमा हा एक माध्यम म्हणून वापरणे, MedTech, आर्किटेक्चर, पर्यटन, गेम डेव्हलपमेंट आणि इतर अनेक क्षेत्रांमध्ये खूप उपयुक्त ठरू शकते. या अध्यायात आपण दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स, DALL-E आणि Midjourney, यांचा अभ्यास करू.

## परिचय

या धड्यात आपण खालील गोष्टी शिकणार आहोत:

- इमेज जनरेशन म्हणजे काय आणि ते कसे उपयुक्त आहे.
- DALL-E आणि Midjourney, हे काय आहेत आणि ते कसे कार्य करतात.
- इमेज जनरेशन अ‍ॅप कसे तयार करावे.

## शिकण्याची उद्दिष्टे

ही धडा पूर्ण केल्यानंतर, तुम्ही हे करू शकाल:

- इमेज जनरेशन अ‍ॅप्लिकेशन तयार करणे.
- मेटा प्रॉम्प्ट्स वापरून तुमच्या अ‍ॅप्लिकेशनसाठी मर्यादा ठरवणे.
- DALL-E आणि Midjourney सोबत काम करणे.

## इमेज जनरेशन अ‍ॅप्लिकेशन का तयार करावे?

इमेज जनरेशन अ‍ॅप्लिकेशन्स हे जनरेटिव्ह AI च्या क्षमतेचा शोध घेण्यासाठी उत्तम मार्ग आहेत. ते खालीलप्रमाणे वापरता येतात:

- **इमेज एडिटिंग आणि सिंथेसिस**. विविध वापरांसाठी प्रतिमा तयार करता येतात, जसे की इमेज एडिटिंग किंवा इमेज सिंथेसिस.

- **विविध उद्योगांमध्ये वापर**. हे अ‍ॅप्लिकेशन्स Medtech, पर्यटन, गेम डेव्हलपमेंट आणि इतर अनेक उद्योगांसाठी प्रतिमा तयार करण्यासाठी वापरता येतात.

## उदाहरण: Edu4All

या धड्यात, आपण आपल्या स्टार्टअप, Edu4All, सोबत काम करणे सुरू ठेवणार आहोत. विद्यार्थी त्यांच्या मूल्यांकनासाठी प्रतिमा तयार करतील, कोणत्या प्रतिमा तयार करायच्या हे विद्यार्थ्यांवर अवलंबून आहे, पण ते त्यांच्या स्वतःच्या परीकथेची चित्रे तयार करू शकतात, किंवा त्यांच्या गोष्टीसाठी नवीन पात्र तयार करू शकतात किंवा त्यांच्या कल्पना आणि संकल्पना प्रत्यक्षात आणू शकतात.

उदाहरणार्थ, जर Edu4All चे विद्यार्थी वर्गात स्मारकांवर काम करत असतील, तर ते असे काही तयार करू शकतात:

![Edu4All स्टार्टअप, स्मारकांवरील वर्ग, आयफेल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.mr.png)

असा प्रॉम्प्ट वापरून

> "डॉग आयफेल टॉवरच्या शेजारी, सकाळच्या सुर्यप्रकाशात"

## DALL-E आणि Midjourney म्हणजे काय?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स आहेत, जे प्रॉम्प्ट्स वापरून प्रतिमा तयार करू देतात.

### DALL-E

DALL-E पासून सुरुवात करूया, हे एक जनरेटिव्ह AI मॉडेल आहे जे मजकूर वर्णनांमधून प्रतिमा तयार करते.

> [DALL-E हे दोन मॉडेल्सचे संयोजन आहे, CLIP आणि डिफ्यूज्ड अटेंशन](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, हे मॉडेल आहे जे इमेज आणि मजकूरातून एम्बेडिंग्ज (डेटाचे संख्यात्मक प्रतिनिधित्व) तयार करते.

- **डिफ्यूज्ड अटेंशन**, हे मॉडेल आहे जे एम्बेडिंग्जमधून प्रतिमा तयार करते. DALL-E ला प्रतिमा आणि मजकूराच्या डेटासेटवर ट्रेन केले आहे आणि ते मजकूर वर्णनांमधून प्रतिमा तयार करण्यासाठी वापरता येते. उदाहरणार्थ, DALL-E वापरून टोपी घातलेल्या मांजरीची किंवा मोहॉक असलेल्या कुत्र्याची प्रतिमा तयार करता येते.

### Midjourney

Midjourney देखील DALL-E प्रमाणेच कार्य करते, हे मजकूर प्रॉम्प्ट्समधून प्रतिमा तयार करते. Midjourney वापरून देखील “टोपी घातलेली मांजर” किंवा “मोहॉक असलेला कुत्रा” अशा प्रॉम्प्ट्स वापरून प्रतिमा तयार करता येतात.

![Midjourney ने तयार केलेली प्रतिमा, मेकॅनिकल कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_प्रतिमा स्त्रोत: Wikipedia, प्रतिमा Midjourney ने तयार केली आहे_

## DALL-E आणि Midjourney कसे कार्य करतात

सुरुवातीला, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E हे जनरेटिव्ह AI मॉडेल आहे जे ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित आहे आणि _ऑटोरिग्रेसिव्ह ट्रान्सफॉर्मर_ वापरते.

_ऑटोरिग्रेसिव्ह ट्रान्सफॉर्मर_ हे ठरवते की मॉडेल मजकूर वर्णनांमधून प्रतिमा कशा तयार करेल, हे एकावेळी एक पिक्सेल तयार करते, आणि तयार झालेल्या पिक्सेल्सचा वापर पुढील पिक्सेल तयार करण्यासाठी करते. हे सर्व न्यूरल नेटवर्कच्या अनेक स्तरांतून जातं, जोपर्यंत प्रतिमा पूर्ण होत नाही.

या प्रक्रियेतून, DALL-E तयार होणाऱ्या प्रतिमेतील गुणधर्म, ऑब्जेक्ट्स, वैशिष्ट्ये इ. नियंत्रित करू शकते. मात्र, DALL-E 2 आणि 3 मध्ये प्रतिमेवर अधिक नियंत्रण मिळते.

## तुमचे पहिले इमेज जनरेशन अ‍ॅप्लिकेशन तयार करणे

तर, इमेज जनरेशन अ‍ॅप्लिकेशन तयार करण्यासाठी काय लागते? तुम्हाला खालील लायब्ररी लागतील:

- **python-dotenv**, ही लायब्ररी वापरण्याची शिफारस केली जाते जेणेकरून तुमची गुपिते _.env_ फाइलमध्ये ठेवता येतील.
- **openai**, ही लायब्ररी OpenAI API शी संवाद साधण्यासाठी वापरता येते.
- **pillow**, Python मध्ये प्रतिमांसोबत काम करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यासाठी.

## Azure OpenAI मॉडेल तयार करा आणि डिप्लॉय करा

जर अजून केले नसेल, तर [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पेजवरील सूचना फॉलो करा
Azure OpenAI रिसोर्स आणि मॉडेल तयार करण्यासाठी. मॉडेल म्हणून DALL-E 3 निवडा.  

## अ‍ॅप तयार करा

1. _.env_ नावाची फाइल तयार करा आणि त्यात खालील मजकूर ठेवा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ही माहिती Azure OpenAI Foundry Portal मध्ये "Deployments" विभागात मिळेल.

1. वरील लायब्ररी _requirements.txt_ नावाच्या फाइलमध्ये खालीलप्रमाणे लिहा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. पुढे, व्हर्च्युअल एन्व्हायर्नमेंट तयार करा आणि लायब्ररी इन्स्टॉल करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows साठी, व्हर्च्युअल एन्व्हायर्नमेंट तयार व अ‍ॅक्टिव्हेट करण्यासाठी हे कमांड्स वापरा:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नावाच्या फाइलमध्ये खालील कोड टाका:

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

हा कोड समजावून घेऊया:

- प्रथम, आपल्याला लागणाऱ्या लायब्ररी इम्पोर्ट करतो, ज्यात OpenAI, dotenv, requests आणि Pillow लायब्ररी आहेत.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- पुढे, _.env_ फाइलमधून एन्व्हायर्नमेंट व्हेरिएबल्स लोड करतो.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यानंतर, Azure OpenAI सर्व्हिस क्लायंट कॉन्फिगर करतो

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- पुढे, प्रतिमा तयार करतो:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  वरील कोडमधून एक JSON ऑब्जेक्ट मिळतो ज्यात तयार झालेल्या प्रतिमेचा URL असतो. आपण हा URL वापरून प्रतिमा डाउनलोड करून फाइलमध्ये सेव्ह करू शकतो.

- शेवटी, प्रतिमा उघडतो आणि स्टँडर्ड इमेज व्ह्युअरमध्ये दाखवतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा तयार करण्याचा अधिक तपशील

प्रतिमा तयार करणारा कोड अधिक तपशीलात पाहूया:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, हा मजकूर प्रॉम्प्ट आहे जो प्रतिमा तयार करण्यासाठी वापरला जातो. इथे आपण "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" हा प्रॉम्प्ट वापरतो.
- **size**, ही तयार होणाऱ्या प्रतिमेचा आकार आहे. इथे आपण 1024x1024 पिक्सेल्सची प्रतिमा तयार करतो.
- **n**, ही तयार होणाऱ्या प्रतिमांची संख्या आहे. इथे आपण दोन प्रतिमा तयार करतो.
- **temperature**, हा जनरेटिव्ह AI मॉडेलच्या आउटपुटमधील रँडमनेस नियंत्रित करणारा पॅरामीटर आहे. temperature 0 ते 1 दरम्यान असतो, 0 म्हणजे आउटपुट निश्चित आणि 1 म्हणजे पूर्णपणे रँडम. डीफॉल्ट व्हॅल्यू 0.7 आहे.

प्रतिमांसोबत अजून बरेच काही करता येते, जे आपण पुढील विभागात पाहू.

## इमेज जनरेशनची अतिरिक्त क्षमताएं

आत्तापर्यंत आपण पाहिले की काही ओळींच्या कोडने Python मध्ये प्रतिमा तयार करता येते. मात्र, प्रतिमांसोबत अजून बरेच काही करता येते.

तुम्ही हे देखील करू शकता:

- **एडिट्स करा**. एखाद्या विद्यमान प्रतिमेला मास्क आणि प्रॉम्प्ट देऊन, प्रतिमेत बदल करू शकता. उदाहरणार्थ, प्रतिमेच्या एका भागात काहीतरी जोडू शकता. आपल्या bunny प्रतिमेला टोपी घालू शकता. हे करण्यासाठी प्रतिमा, मास्क (बदल करायचा भाग ओळखणारा) आणि काय करायचे हे सांगणारा मजकूर प्रॉम्प्ट द्यावा लागतो.
> लक्षात घ्या: हे DALL-E 3 मध्ये सपोर्टेड नाही.

GPT Image वापरून एक उदाहरण:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  मूळ प्रतिमेत फक्त पूल असलेला लाउंज असेल, पण अंतिम प्रतिमेत फ्लेमिंगो असेल:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **व्हेरिएशन्स तयार करा**. म्हणजेच, विद्यमान प्रतिमेवरून विविध व्हेरिएशन्स तयार करणे. यासाठी प्रतिमा आणि मजकूर प्रॉम्प्ट द्यावा लागतो आणि कोड खालीलप्रमाणे असतो:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > लक्षात घ्या, हे फक्त OpenAI वर सपोर्टेड आहे

## Temperature

Temperature हा जनरेटिव्ह AI मॉडेलच्या आउटपुटमधील रँडमनेस नियंत्रित करणारा पॅरामीटर आहे. temperature 0 ते 1 दरम्यान असतो, 0 म्हणजे आउटपुट निश्चित आणि 1 म्हणजे पूर्णपणे रँडम. डीफॉल्ट व्हॅल्यू 0.7 आहे.

Temperature कसे कार्य करते हे पाहण्यासाठी, हा प्रॉम्प्ट दोनदा चालवूया:

> प्रॉम्प्ट : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.mr.png)

आता तोच प्रॉम्प्ट पुन्हा चालवूया, पाहूया की आपल्याला एकसारखी प्रतिमा मिळते का:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.mr.png)

पाहू शकता, प्रतिमा सारख्या आहेत, पण एकसारख्या नाहीत. आता temperature 0.1 करूया आणि पाहूया काय होते:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature बदलणे

तर, आता आउटपुट अधिक निश्चित (deterministic) करूया. आपण तयार केलेल्या दोन प्रतिमांमध्ये पहिल्या प्रतिमेत bunny आहे आणि दुसऱ्यात horse आहे, म्हणजे प्रतिमांमध्ये बरीच फरक आहे.

म्हणून, आपला कोड बदलून temperature 0 करूया:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता हा कोड चालवल्यावर, तुम्हाला या दोन प्रतिमा मिळतील:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.mr.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.mr.png)

इथे स्पष्टपणे दिसते की प्रतिमा एकमेकांसारख्या आहेत.

## मेटाप्रॉम्प्ट्स वापरून अ‍ॅप्लिकेशनसाठी मर्यादा कशा ठरवाव्यात

आपल्या डेमोमध्ये, आपण आधीच क्लायंटसाठी प्रतिमा तयार करू शकतो. मात्र, आपल्याला अ‍ॅप्लिकेशनसाठी काही मर्यादा घालाव्या लागतील.

उदाहरणार्थ, आपण अशा प्रतिमा तयार करू इच्छित नाही ज्या ऑफिससाठी सुरक्षित नाहीत किंवा मुलांसाठी योग्य नाहीत.

हे आपण _मेटाप्रॉम्प्ट्स_ वापरून करू शकतो. मेटाप्रॉम्प्ट्स हे मजकूर प्रॉम्प्ट्स आहेत जे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात. उदाहरणार्थ, आपण मेटाप्रॉम्प्ट्स वापरून आउटपुट नियंत्रित करू शकतो आणि तयार होणाऱ्या प्रतिमा ऑफिससाठी सुरक्षित किंवा मुलांसाठी योग्य आहेत याची खात्री करू शकतो.

### हे कसे कार्य करते?

मग, मेटाप्रॉम्प्ट्स कसे कार्य करतात?

मेटाप्रॉम्प्ट्स हे मजकूर प्रॉम्प्ट्स आहेत जे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात, हे मुख्य प्रॉम्प्टच्या आधी दिले जातात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी अ‍ॅप्लिकेशनमध्ये एम्बेड केले जातात. प्रॉम्प्ट इनपुट आणि मेटाप्रॉम्प्ट इनपुट एकत्र करून एकच मजकूर प्रॉम्प्ट तयार केला जातो.

मेटाप्रॉम्प्टचे एक उदाहरण असे असेल:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

आता, आपल्या डेमोमध्ये मेटाप्रॉम्प्ट्स कसे वापरायचे ते पाहूया.

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

वरील प्रॉम्प्टमधून, तुम्ही पाहू शकता की तयार होणाऱ्या सर्व प्रतिमांमध्ये मेटाप्रॉम्प्ट विचारात घेतला जातो.

## असाइनमेंट - चला विद्यार्थ्यांना सक्षम करूया

या धड्याच्या सुरुवातीला आपण Edu4All ची ओळख करून दिली. आता विद्यार्थ्यांना त्यांच्या मूल्यांकनासाठी प्रतिमा तयार करण्याची संधी देऊया.

विद्यार्थी त्यांच्या मूल्यांकनासाठी स्मारकांची प्रतिमा तयार करतील, कोणती स्मारके हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना त्यांच्या सर्जनशीलतेचा वापर करून ही स्मारके वेगवेगळ्या संदर्भात ठेवण्यास सांगितले आहे.

## सोल्यूशन

हे एक शक्य सोल्यूशन आहे:

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

## छान काम! तुमचे शिक्षण पुढे सुरू ठेवा
ही धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि तुमचे Generative AI ज्ञान आणखी वाढवा!

पुढील धडा १० मध्ये चला जिथे आपण [low-code वापरून AI applications कसे तयार करायचे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) हे पाहणार आहोत.

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अपूर्णता असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.