<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T13:49:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "mr"
}
-->
# इमेज जनरेशन अ‍ॅप्लिकेशन्स तयार करणे

[![इमेज जनरेशन अ‍ॅप्लिकेशन्स तयार करणे](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.mr.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs केवळ टेक्स्ट जनरेशनसाठीच मर्यादित नाहीत. टेक्स्ट वर्णनांमधून प्रतिमा तयार करणे देखील शक्य आहे. प्रतिमा ही एक महत्त्वाची माध्यम असू शकते, जी MedTech, आर्किटेक्चर, पर्यटन, गेम डेव्हलपमेंट आणि इतर अनेक क्षेत्रांमध्ये उपयुक्त ठरते. या अध्यायात, आपण दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स, DALL-E आणि Midjourney यांचा अभ्यास करू.

## परिचय

या धड्यात आपण खालील गोष्टींचा अभ्यास करू:

- इमेज जनरेशन आणि त्याचे महत्त्व.
- DALL-E आणि Midjourney, ते काय आहेत आणि कसे कार्य करतात.
- इमेज जनरेशन अ‍ॅप कसे तयार करावे.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, आपण हे करू शकता:

- इमेज जनरेशन अ‍ॅप तयार करा.
- आपल्या अ‍ॅप्लिकेशनसाठी मेटा प्रॉम्प्ट्ससह मर्यादा निश्चित करा.
- DALL-E आणि Midjourney सह कार्य करा.

## इमेज जनरेशन अ‍ॅप्लिकेशन का तयार करावे?

इमेज जनरेशन अ‍ॅप्लिकेशन्स हे जनरेटिव AI च्या क्षमतांचा अभ्यास करण्याचा एक उत्कृष्ट मार्ग आहे. ते खालीलप्रमाणे वापरले जाऊ शकतात:

- **इमेज एडिटिंग आणि सिंथेसिस**. विविध उपयोगांसाठी प्रतिमा तयार करण्यासाठी, जसे की इमेज एडिटिंग आणि इमेज सिंथेसिस.

- **विविध उद्योगांमध्ये लागू**. MedTech, पर्यटन, गेम डेव्हलपमेंट आणि इतर अनेक उद्योगांसाठी प्रतिमा तयार करण्यासाठी देखील ते वापरले जाऊ शकतात.

## उदाहरण: Edu4All

या धड्याचा भाग म्हणून, आपण Edu4All नावाच्या आपल्या स्टार्टअपसह काम सुरू ठेवू. विद्यार्थी त्यांच्या मूल्यांकनासाठी प्रतिमा तयार करतील, कोणत्या प्रकारच्या प्रतिमा तयार करायच्या आहेत हे विद्यार्थ्यांवर अवलंबून आहे, परंतु ते त्यांच्या स्वतःच्या परीकथेसाठी चित्रे तयार करू शकतात किंवा त्यांच्या कथेतील नवीन पात्र तयार करू शकतात किंवा त्यांच्या कल्पना आणि संकल्पना दृश्यमान करण्यास मदत करू शकतात.

उदाहरणार्थ, Edu4All चे विद्यार्थी वर्गात स्मारकांवर काम करत असल्यास ते खालीलप्रमाणे प्रतिमा तयार करू शकतात:

![Edu4All स्टार्टअप, वर्गात स्मारकांवर काम, आयफेल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.mr.png)

प्रॉम्प्ट वापरून:

> "आयफेल टॉवरच्या शेजारी कुत्रा, सकाळच्या सुर्यप्रकाशात"

## DALL-E आणि Midjourney काय आहेत?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स आहेत, जे प्रॉम्प्ट्स वापरून प्रतिमा तयार करण्याची परवानगी देतात.

### DALL-E

DALL-E पासून सुरुवात करूया, जे एक जनरेटिव AI मॉडेल आहे जे टेक्स्ट वर्णनांमधून प्रतिमा तयार करते.

> [DALL-E हे दोन मॉडेल्स, CLIP आणि diffused attention यांचे संयोजन आहे](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, हे एक मॉडेल आहे जे प्रतिमा आणि टेक्स्टमधून एम्बेडिंग्ज तयार करते, जे डेटा चे संख्यात्मक प्रतिनिधित्व असते.

- **Diffused attention**, हे एक मॉडेल आहे जे एम्बेडिंग्जमधून प्रतिमा तयार करते. DALL-E प्रतिमा आणि टेक्स्टच्या डेटासेटवर प्रशिक्षित आहे आणि टेक्स्ट वर्णनांमधून प्रतिमा तयार करण्यासाठी वापरले जाऊ शकते. उदाहरणार्थ, DALL-E चा वापर टोपीतील मांजर किंवा मोहॉक असलेल्या कुत्र्याच्या प्रतिमा तयार करण्यासाठी केला जाऊ शकतो.

### Midjourney

Midjourney DALL-E प्रमाणेच कार्य करते, ते टेक्स्ट प्रॉम्प्ट्स वापरून प्रतिमा तयार करते. Midjourney चा वापर "टोपीतील मांजर" किंवा "मोहॉक असलेला कुत्रा" यासारख्या प्रॉम्प्ट्ससह प्रतिमा तयार करण्यासाठी देखील केला जाऊ शकतो.

![Midjourney द्वारे तयार केलेली प्रतिमा, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_प्रतिमा क्रेडिट विकिपीडिया, Midjourney द्वारे तयार केलेली प्रतिमा_

## DALL-E आणि Midjourney कसे कार्य करतात

[DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) पासून सुरुवात करूया. DALL-E हे ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित जनरेटिव AI मॉडेल आहे ज्यामध्ये _autoregressive transformer_ आहे.

_autoregressive transformer_ हे मॉडेल टेक्स्ट वर्णनांमधून प्रतिमा कशा तयार करते हे परिभाषित करते, ते एकावेळी एक पिक्सेल तयार करते आणि नंतर तयार केलेल्या पिक्सेल्सचा वापर पुढील पिक्सेल तयार करण्यासाठी करते. न्यूरल नेटवर्कमधील अनेक स्तरांमधून जात, प्रतिमा पूर्ण होईपर्यंत.

या प्रक्रियेद्वारे, DALL-E तयार केलेल्या प्रतिमेमध्ये गुणधर्म, वस्तू, वैशिष्ट्ये आणि बरेच काही नियंत्रित करते. तथापि, DALL-E 2 आणि 3 मध्ये तयार केलेल्या प्रतिमेवर अधिक नियंत्रण आहे.

## आपले पहिले इमेज जनरेशन अ‍ॅप तयार करणे

तर इमेज जनरेशन अ‍ॅप तयार करण्यासाठी काय आवश्यक आहे? आपल्याला खालील लायब्ररी लागतील:

- **python-dotenv**, आपले गुपिते _.env_ फाइलमध्ये कोडपासून दूर ठेवण्यासाठी ही लायब्ररी वापरण्याची जोरदार शिफारस केली जाते.
- **openai**, ही लायब्ररी OpenAI API सह संवाद साधण्यासाठी वापरली जाते.
- **pillow**, Python मध्ये प्रतिमांसह कार्य करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यासाठी मदत करण्यासाठी.

## Azure OpenAI मॉडेल तयार करा आणि तैनात करा

जर अद्याप केले नसेल, तर [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पृष्ठावरील सूचनांचे अनुसरण करा
Azure OpenAI संसाधन आणि मॉडेल तयार करण्यासाठी. DALL-E 3 मॉडेल निवडा.  

## अ‍ॅप तयार करा

1. खालील सामग्रीसह _.env_ नावाची फाइल तयार करा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Azure OpenAI Foundry Portal मध्ये आपल्या संसाधनाच्या "Deployments" विभागात ही माहिती शोधा.

1. वरील लायब्ररी _requirements.txt_ नावाच्या फाइलमध्ये गोळा करा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. नंतर, वर्च्युअल एन्व्हायर्नमेंट तयार करा आणि लायब्ररी इंस्टॉल करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows साठी, वर्च्युअल एन्व्हायर्नमेंट तयार करण्यासाठी आणि सक्रिय करण्यासाठी खालील कमांड वापरा:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नावाच्या फाइलमध्ये खालील कोड जोडा:

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

या कोडचे स्पष्टीकरण देऊया:

- प्रथम, आम्ही आवश्यक लायब्ररी आयात करतो, ज्यामध्ये OpenAI लायब्ररी, dotenv लायब्ररी, requests लायब्ररी आणि Pillow लायब्ररी समाविष्ट आहे.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- नंतर, आम्ही _.env_ फाइलमधून एन्व्हायर्नमेंट व्हेरिएबल्स लोड करतो.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यानंतर, आम्ही Azure OpenAI सेवा क्लायंट कॉन्फिगर करतो.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- नंतर, आम्ही प्रतिमा तयार करतो:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  वरील कोड JSON ऑब्जेक्टसह प्रतिसाद देतो ज्यामध्ये तयार केलेल्या प्रतिमेचा URL असतो. आम्ही प्रतिमा डाउनलोड करण्यासाठी आणि ती फाइलमध्ये सेव्ह करण्यासाठी URL वापरू शकतो.

- शेवटी, आम्ही प्रतिमा उघडतो आणि ती प्रदर्शित करण्यासाठी मानक प्रतिमा दर्शक वापरतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा तयार करण्याबद्दल अधिक तपशील

आता आपण प्रतिमा तयार करणाऱ्या कोडचा अधिक तपशीलवार अभ्यास करूया:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ही प्रतिमा तयार करण्यासाठी वापरली जाणारी टेक्स्ट प्रॉम्प्ट आहे. या प्रकरणात, आम्ही "घोड्यावर बसलेला ससा, हातात लॉलीपॉप, धुकट कुरणावर जिथे डॅफोडिल्स उगवतात" हा प्रॉम्प्ट वापरत आहोत.
- **size**, ही तयार केलेल्या प्रतिमेचा आकार आहे. या प्रकरणात, आम्ही 1024x1024 पिक्सेलची प्रतिमा तयार करत आहोत.
- **n**, ही तयार केलेल्या प्रतिमांची संख्या आहे. या प्रकरणात, आम्ही दोन प्रतिमा तयार करत आहोत.
- **temperature**, हा जनरेटिव AI मॉडेलच्या आउटपुटची अनियमितता नियंत्रित करणारा पॅरामीटर आहे. तापमान 0 ते 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

प्रतिमांसह आपण आणखी बरेच काही करू शकतो, जे आपण पुढील विभागात कव्हर करू.

## इमेज जनरेशनच्या अतिरिक्त क्षमता

आतापर्यंत आपण पाहिले की आम्ही Python मधील काही ओळींचा वापर करून प्रतिमा तयार करू शकलो. तथापि, प्रतिमांसह आपण आणखी बरेच काही करू शकतो.

आपण खालील गोष्टी देखील करू शकता:

- **एडिट्स करा**. विद्यमान प्रतिमा, मास्क आणि प्रॉम्प्ट प्रदान करून, आपण प्रतिमेत बदल करू शकता. उदाहरणार्थ, आपण प्रतिमेच्या एका भागात काहीतरी जोडू शकता. आपल्या सशाच्या प्रतिमेची कल्पना करा, आपण सशाला टोपी घालू शकता. आपण प्रतिमा, मास्क (बदलासाठी क्षेत्र ओळखणे) आणि काय करावे याबद्दल टेक्स्ट प्रॉम्प्ट प्रदान करून ते करू शकता. 
> लक्षात ठेवा: DALL-E 3 मध्ये हे समर्थित नाही. 
 
GPT Image वापरून एक उदाहरण येथे आहे:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  मूळ प्रतिमेमध्ये फक्त पूलसह लाउंज असेल परंतु अंतिम प्रतिमेमध्ये फ्लेमिंगो असेल:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.mr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.mr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.mr.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **विविधता तयार करा**. कल्पना अशी आहे की आपण विद्यमान प्रतिमा घेऊन विचारतो की विविधता तयार केली जावी. विविधता तयार करण्यासाठी, आपण प्रतिमा आणि टेक्स्ट प्रॉम्प्ट प्रदान करता आणि कोड खालीलप्रमाणे असतो:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > लक्षात ठेवा, हे फक्त OpenAI वर समर्थित आहे.

## तापमान

तापमान हा जनरेटिव AI मॉडेलच्या आउटपुटची अनियमितता नियंत्रित करणारा पॅरामीटर आहे. तापमान 0 ते 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

तापमान कसे कार्य करते याचे उदाहरण पाहूया, हा प्रॉम्प्ट दोनदा चालवून:

> प्रॉम्प्ट : "घोड्यावर बसलेला ससा, हातात लॉलीपॉप, धुकट कुरणावर जिथे डॅफोडिल्स उगवतात"

![घोड्यावर बसलेला ससा, लॉलीपॉप धरलेला, आवृत्ती 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.mr.png)

आता तोच प्रॉम्प्ट पुन्हा चालवूया आणि पाहूया की आपल्याला एकसारखी प्रतिमा दोनदा मिळत नाही:

![घोड्यावर बसलेला ससा तयार केलेली प्रतिमा](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.mr.png)

जसे आपण पाहू शकता, प्रतिमा समान आहेत, परंतु एकसारख्या नाहीत. तापमान मूल्य 0.1 वर बदलून काय होते ते पाहूया:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलणे

तर चला प्रतिसाद अधिक निश्चित करण्याचा प्रयत्न करूया. आम्ही तयार केलेल्या दोन प्रतिमांमधून निरीक्षण करू शकतो की पहिल्या प्रतिमेमध्ये ससा आहे आणि दुसऱ्या प्रतिमेमध्ये घोडा आहे, त्यामुळे प्रतिमा खूप वेगळ्या आहेत.

म्हणूनच, आपला कोड बदलूया आणि तापमान 0 वर सेट करूया, खालीलप्रमाणे:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता आपण हा कोड चालवला तर आपल्याला या दोन प्रतिमा मिळतात:

- ![तापमान 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.mr.png)
- ![तापमान 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.mr.png)

येथे आपण स्पष्टपणे पाहू शकता की प्रतिमा एकमेकांशी अधिक साम्य आहेत.

## आपल्या अ‍ॅप्लिकेशनसाठी मेटा प्रॉम्प्ट्ससह मर्यादा कशा परिभाषित कराव्यात

आमच्या डेमोसह, आम्ही आधीच आमच्या क्लायंटसाठी प्रतिमा तयार करू शकतो. तथापि, आम्हाला आमच्या अ‍ॅप्लिकेशनसाठी काही मर्यादा तयार करणे आवश्यक आहे.

उदाहरणार्थ, आम्हाला अशा प्रतिमा तयार करायच्या नाहीत ज्या कामासाठी सुरक्षित नाहीत किंवा मुलांसाठी योग्य नाहीत.

आम्ही हे _मेटा प्रॉम्प्ट्स_ च्या मदतीने करू शकतो. मेटा प्रॉम्प्ट्स हे टेक्स्ट प्रॉम्प्ट्स आहेत जे जनरेटिव AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात. उदाहरणार्थ, आम्ही मेटा प्रॉम्प्ट्सचा वापर आउटपुटवर नियंत्रण ठेवण्यासाठी करू शकतो आणि तयार केलेल्या प्रतिमा कामासाठी सुरक्षित आहेत किंवा मुलांसाठी योग्य आहेत याची खात्री करू शकतो.

### हे कसे कार्य करते?

आता, मेटा प्रॉम्प्ट्स कसे कार्य करतात?

मेटा प्रॉम्प्ट्स हे टेक्स्ट प्रॉम्प्ट्स आहेत जे जनरेटिव AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात, ते टेक्स्ट प्रॉम्प्टच्या आधी स्थित असतात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी अ‍ॅप्लिकेशन्समध्ये एम्बेड केले जातात. प्रॉम्प्ट इनपुट आणि मेटा प्रॉम्प्ट इनपुट एका टेक्स्ट प्रॉम्प्टमध्ये समाविष्ट करणे.

मेटा प्रॉम्प्टचे एक उदाहरण खालीलप्रमाणे असेल:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

आता, आपण आपल्या डेमोमध्ये मेटा प्रॉम्प्ट्स कसे वापरू शकतो ते पाहूया.

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

वरील प्रॉम्प्टमधून, आपण पाहू शकता की तयार केलेल्या सर्व प्रतिमा मेटा प्रॉम्प्ट विचारात घेतात.

## असाइनमेंट - चला विद्यार्थ्यांना सक्षम करूया

या धड्याच्या सुरुवातीला आम्ही Edu4All ची ओळख करून दिली. आता विद्यार्थ्यांना त्यांच्या मूल्यांकनासाठी प्रतिमा तयार करण्यास सक्षम करण्याची वेळ आली आहे.

विद्यार्थी त्यांच्या मूल्यांकनासाठी स्मारकांसह प्रतिमा तयार करतील, कोणते स्मारक तयार करायचे आहे हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना या कार्यात त्यांच्या सर्जनशीलतेचा वापर करून या स्मारकांना वेगवेगळ्या संदर्भात ठेवण्याचे आवाहन केले जाते.

## समाधान

येथे एक संभाव्य समाधान आहे:
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

## उत्तम काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि तुमचे Generative AI ज्ञान वाढवा!

धडा 10 कडे जा, जिथे आपण [कमी कोड वापरून AI अनुप्रयोग तयार करणे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) याबद्दल शिकू.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपयास लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.