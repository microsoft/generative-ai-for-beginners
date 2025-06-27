<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:13:31+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "mr"
}
-->
# इमेज जनरेशन अॅप्लिकेशन्स तयार करणे

LLMs च्या क्षमतेपेक्षा अधिक काही आहे, केवळ मजकूर निर्मितीच नाही. मजकूर वर्णनांपासून प्रतिमा निर्माण करणे देखील शक्य आहे. मेडटेक, आर्किटेक्चर, पर्यटन, गेम विकास आणि अधिक क्षेत्रांमध्ये प्रतिमा एक उपयोगी माध्यम असू शकतात. या अध्यायात, आपण दोन सर्वात लोकप्रिय प्रतिमा निर्माण मॉडेल्स, DALL-E आणि Midjourney चा अभ्यास करू.

## परिचय

या धड्यात आपण कव्हर करू:

- प्रतिमा निर्माण आणि त्याचे उपयोग.
- DALL-E आणि Midjourney, ते काय आहेत आणि ते कसे कार्य करतात.
- प्रतिमा निर्माण अॅप कसे तयार करावे.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, आपण सक्षम असाल:

- प्रतिमा निर्माण अॅप्लिकेशन तयार करणे.
- आपल्या अॅप्लिकेशनसाठी मेटा प्रॉम्प्ट्ससह सीमा निश्चित करणे.
- DALL-E आणि Midjourney सह काम करणे.

## प्रतिमा निर्माण अॅप्लिकेशन का तयार करावे?

प्रतिमा निर्माण अॅप्लिकेशन्स जनरेटिव्ह AI च्या क्षमतांचा अभ्यास करण्याचा उत्तम मार्ग आहेत. ते वापरले जाऊ शकतात, उदाहरणार्थ:

- **प्रतिमा संपादन आणि संश्लेषण**. आपण विविध उपयोगांसाठी प्रतिमा निर्माण करू शकता, जसे की प्रतिमा संपादन आणि प्रतिमा संश्लेषण.

- **विविध उद्योगांसाठी लागू**. ते मेडटेक, पर्यटन, गेम विकास आणि अधिक उद्योगांसाठी प्रतिमा निर्माण करण्यासाठी वापरले जाऊ शकतात.

## परिदृश्य: Edu4All

या धड्याचा एक भाग म्हणून, आपण Edu4All या आपल्या स्टार्टअपसह काम करणे सुरू ठेवू. विद्यार्थ्यांना त्यांच्या मूल्यांकनांसाठी प्रतिमा तयार करायच्या आहेत, कोणत्या प्रतिमा तयार करायच्या हे विद्यार्थ्यांवर अवलंबून आहे, परंतु ते त्यांच्या स्वतःच्या परीकथेच्या चित्रणांसाठी किंवा त्यांच्या कथेसाठी नवीन पात्र तयार करण्यासाठी किंवा त्यांच्या कल्पना आणि संकल्पना दृश्यमान करण्यासाठी मदत करू शकतात.

उदाहरणार्थ, जर Edu4All चे विद्यार्थी वर्गात स्मारकांवर काम करत असतील तर ते काय निर्माण करू शकतात:

![Edu4All स्टार्टअप, वर्गात स्मारके, आयफेल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.mr.png)

अशा प्रॉम्प्टचा वापर करून

> "कुत्रा आयफेल टॉवरच्या शेजारी सकाळच्या सुर्योदयात"

## DALL-E आणि Midjourney काय आहेत?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय प्रतिमा निर्माण मॉडेल्स आहेत, ते आपल्याला प्रॉम्प्ट्स वापरून प्रतिमा निर्माण करण्यास अनुमती देतात.

### DALL-E

DALL-E सह सुरुवात करूया, जे एक जनरेटिव्ह AI मॉडेल आहे जे मजकूर वर्णनांपासून प्रतिमा निर्माण करते.

> [DALL-E हे दोन मॉडेल्स, CLIP आणि डिफ्यूज्ड अटेंशनचे संयोजन आहे](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, हे एक मॉडेल आहे जे एम्बेडिंग्ज निर्माण करते, जे डेटा चे संख्यात्मक प्रतिनिधित्व आहेत, प्रतिमा आणि मजकूरातून.

- **डिफ्यूज्ड अटेंशन**, हे एक मॉडेल आहे जे एम्बेडिंग्ज पासून प्रतिमा निर्माण करते. DALL-E प्रतिमा आणि मजकूराच्या डेटासेटवर प्रशिक्षित आहे आणि मजकूर वर्णनांपासून प्रतिमा निर्माण करण्यासाठी वापरले जाऊ शकते. उदाहरणार्थ, DALL-E चा वापर टोपीतील मांजर किंवा मोहॉक असलेल्या कुत्र्याच्या प्रतिमा निर्माण करण्यासाठी केला जाऊ शकतो.

### Midjourney

Midjourney DALL-E प्रमाणेच कार्य करते, ते मजकूर प्रॉम्प्ट्सपासून प्रतिमा निर्माण करते. Midjourney चा वापर "टोपीतील मांजर" किंवा "मोहॉक असलेला कुत्रा" यासारख्या प्रॉम्प्ट्स वापरून प्रतिमा निर्माण करण्यासाठी केला जाऊ शकतो.

![Midjourney द्वारा निर्माण केलेली प्रतिमा, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_प्रतिमा क्रेडिट विकिपीडिया, Midjourney द्वारा निर्माण केलेली प्रतिमा_

## DALL-E आणि Midjourney कसे कार्य करतात

प्रथम, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E हे ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित जनरेटिव्ह AI मॉडेल आहे ज्यामध्ये _ऑटोरिग्रेसिव्ह ट्रान्सफॉर्मर_ आहे.

_ऑटोरिग्रेसिव्ह ट्रान्सफॉर्मर_ एक मॉडेल कसे मजकूर वर्णनांपासून प्रतिमा निर्माण करते हे निश्चित करते, ते एक पिक्सल एकावेळी निर्माण करते आणि नंतर पुढील पिक्सल निर्माण करण्यासाठी निर्माण केलेल्या पिक्सल्सचा वापर करते. एक न्यूरल नेटवर्कमध्ये अनेक स्तरांमधून जात, जोपर्यंत प्रतिमा पूर्ण होत नाही.

या प्रक्रियेसह, DALL-E, निर्माण केलेल्या प्रतिमेत गुणधर्म, वस्तू, वैशिष्ट्ये आणि अधिक नियंत्रित करते. तथापि, DALL-E 2 आणि 3 मध्ये निर्माण केलेल्या प्रतिमेवर अधिक नियंत्रण आहे.

## आपले पहिले प्रतिमा निर्माण अॅप्लिकेशन तयार करणे

तर प्रतिमा निर्माण अॅप्लिकेशन तयार करण्यासाठी काय आवश्यक आहे? आपल्याला खालील लायब्ररी आवश्यक आहेत:

- **python-dotenv**, आपल्याला _.env_ फाइलमध्ये आपली रहस्ये कोडपासून दूर ठेवण्यासाठी ही लायब्ररी वापरण्याची जोरदार शिफारस केली जाते.
- **openai**, ही लायब्ररी OpenAI API शी संवाद साधण्यासाठी आपण वापरणार आहात.
- **pillow**, Python मध्ये प्रतिमांसह काम करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यास मदत करण्यासाठी.

1. खालील सामग्रीसह _.env_ फाइल तयार करा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   आपल्या संसाधनासाठी Azure Portal मध्ये "Keys and Endpoint" विभागात ही माहिती शोधा.

1. वरील लायब्ररी _requirements.txt_ नावाच्या फाइलमध्ये जमा करा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. पुढे, वर्चुअल एन्व्हायर्नमेंट तयार करा आणि लायब्ररी स्थापित करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   विंडोजसाठी, आपले वर्चुअल एन्व्हायर्नमेंट तयार आणि सक्रिय करण्यासाठी खालील कमांड्स वापरा:

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

या कोडचे स्पष्टीकरण करूया:

- प्रथम, आम्ही आवश्यक लायब्ररी आयात करतो, ज्यात OpenAI लायब्ररी, dotenv लायब्ररी, requests लायब्ररी, आणि Pillow लायब्ररी समाविष्ट आहे.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- पुढे, आम्ही _.env_ फाइलमधून पर्यावरणीय व्हेरिएबल्स लोड करतो.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यानंतर, आम्ही OpenAI API साठी एंडपॉइंट, की, आवृत्ती आणि प्रकार सेट करतो.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- पुढे, आम्ही प्रतिमा निर्माण करतो:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  वरील कोड JSON ऑब्जेक्टसह प्रतिसाद देतो ज्यात निर्माण केलेल्या प्रतिमेचा URL असतो. आम्ही URL चा वापर प्रतिमा डाउनलोड करण्यासाठी आणि फाइलमध्ये जतन करण्यासाठी करू शकतो.

- शेवटी, आम्ही प्रतिमा उघडतो आणि मानक प्रतिमा दर्शक वापरून ती प्रदर्शित करतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा निर्माण करण्याचे अधिक तपशील

आम्ही प्रतिमा निर्माण करणाऱ्या कोडकडे अधिक तपशीलात पाहूया:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, हा मजकूर प्रॉम्प्ट आहे जो प्रतिमा निर्माण करण्यासाठी वापरला जातो. या प्रकरणात, आम्ही "घोड्यावर ससा, हातात लॉलीपॉप, फॉगी मीडोवर जिथे डॅफोडिल्स उगवतात" प्रॉम्प्ट वापरत आहोत.
- **size**, ही निर्माण केलेल्या प्रतिमेची आकारमान आहे. या प्रकरणात, आम्ही 1024x1024 पिक्सलची प्रतिमा निर्माण करत आहोत.
- **n**, हे निर्माण केलेल्या प्रतिमांची संख्या आहे. या प्रकरणात, आम्ही दोन प्रतिमा निर्माण करत आहोत.
- **temperature**, हा जनरेटिव्ह AI मॉडेलच्या आउटपुटची अनियमितता नियंत्रित करणारा पॅरामीटर आहे. तापमान हे 0 आणि 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

प्रतिमांसह आपण अधिक गोष्टी करू शकता ज्या आम्ही पुढील विभागात कव्हर करू.

## प्रतिमा निर्माणाची अतिरिक्त क्षमता

आतापर्यंत आपण पाहिले की आम्ही Python मधील काही ओळींचा वापर करून प्रतिमा निर्माण करण्यास सक्षम आहोत. तथापि, प्रतिमांसह आपण अधिक गोष्टी करू शकता.

आपण खालील गोष्टी देखील करू शकता:

- **संपादन करा**. विद्यमान प्रतिमा, मास्क आणि प्रॉम्प्ट प्रदान करून, आपण प्रतिमा बदलू शकता. उदाहरणार्थ, आपण प्रतिमेच्या एका भागात काहीतरी जोडू शकता. आमच्या ससा प्रतिमेची कल्पना करा, आपण सशाला टोपी जोडू शकता. आपण ते कसे कराल ते म्हणजे प्रतिमा, मास्क (बदलासाठी क्षेत्राचा भाग ओळखणे) आणि काय करावे हे सांगण्यासाठी मजकूर प्रॉम्प्ट प्रदान करून.

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

  बेस प्रतिमेत फक्त ससा असेल परंतु अंतिम प्रतिमेत सशावर टोपी असेल.

- **विविधता तयार करा**. कल्पना आहे की आपण विद्यमान प्रतिमा घ्या आणि विचार करा की विविधता तयार केली जावी. विविधता तयार करण्यासाठी, आपण प्रतिमा आणि मजकूर प्रॉम्प्ट प्रदान करा आणि कोड असे:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > लक्षात घ्या, हे केवळ OpenAI वर समर्थित आहे.

## तापमान

तापमान हा जनरेटिव्ह AI मॉडेलच्या आउटपुटची अनियमितता नियंत्रित करणारा पॅरामीटर आहे. तापमान हे 0 आणि 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

तापमान कसे कार्य करते याचे उदाहरण पाहूया, हे प्रॉम्प्ट दोनदा चालवून:

> प्रॉम्प्ट : "घोड्यावर ससा, हातात लॉलीपॉप, फॉगी मीडोवर जिथे डॅफोडिल्स उगवतात"

![घोड्यावर ससा, लॉलीपॉप धरलेला, आवृत्ती 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.mr.png)

आता तोच प्रॉम्प्ट पुन्हा चालवूया फक्त हे पाहण्यासाठी की आम्हाला एकाच प्रतिमा दोनदा मिळणार नाही:

![घोड्यावर ससा निर्माण केलेली प्रतिमा](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.mr.png)

आपण पाहू शकता की प्रतिमा समान आहेत, परंतु एकसारख्या नाहीत. चला तापमान मूल्य 0.1 वर बदलूया आणि काय होते ते पाहूया:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलणे

तर चला प्रतिसाद अधिक निश्चित करण्याचा प्रयत्न करूया. आम्ही निर्माण केलेल्या दोन प्रतिमांमधून पाहू शकतो की पहिल्या प्रतिमेत ससा आहे आणि दुसऱ्या प्रतिमेत घोडा आहे, त्यामुळे प्रतिमा मोठ्या प्रमाणात बदलतात.

म्हणून चला आमचा कोड बदलूया आणि तापमान 0 वर सेट करूया, असे:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता जेव्हा आपण हा कोड चालवता, तेव्हा आपल्याला या दोन प्रतिमा मिळतात:

- ![तापमान 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.mr.png)
- ![तापमान 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.mr.png)

येथे आपण स्पष्टपणे पाहू शकता की प्रतिमा एकमेकांशी अधिक समान आहेत.

## मेटाप्रॉम्प्ट्ससह आपल्या अॅप्लिकेशनसाठी सीमा कशी परिभाषित करावी

आमच्या डेमोसह, आम्ही आधीच आमच्या ग्राहकांसाठी प्रतिमा निर्माण करू शकतो. तथापि, आम्हाला आमच्या अॅप्लिकेशनसाठी काही सीमा निर्माण करणे आवश्यक आहे.

उदाहरणार्थ, आम्हाला अशा प्रतिमा निर्माण करायच्या नाहीत ज्या कामासाठी सुरक्षित नाहीत किंवा मुलांसाठी योग्य नाहीत.

आम्ही हे _मेटाप्रॉम्प्ट्स_ सह करू शकतो. मेटाप्रॉम्प्ट्स हे जनरेटिव्ह AI मॉडेलच्या आउटपुटला नियंत्रित करण्यासाठी वापरले जाणारे मजकूर प्रॉम्प्ट्स आहेत. उदाहरणार्थ, आम्ही आउटपुट नियंत्रित करण्यासाठी आणि निर्माण केलेल्या प्रतिमा कामासाठी सुरक्षित आहेत किंवा मुलांसाठी योग्य आहेत याची खात्री करण्यासाठी मेटाप्रॉम्प्ट्सचा वापर करू शकतो.

### ते कसे कार्य करते?

आता, मेटा प्रॉम्प्ट्स कसे कार्य करतात?

मेटा प्रॉम्प्ट्स हे जनरेटिव्ह AI मॉडेलच्या आउटपुटला नियंत्रित करण्यासाठी वापरले जाणारे मजकूर प्रॉम्प्ट्स आहेत, ते मजकूर प्रॉम्प्टच्या आधी स्थित केले जातात आणि मॉडेलच्या आउटपुटला नियंत्रित करण्यासाठी वापरले जातात आणि अॅप्लिकेशन्समध्ये मॉडेलच्या आउटपुटला नियंत्रित करण्यासाठी एम्बेड केले जातात. प्रॉम्प्ट इनपुट आणि मेटा प्रॉम्प्ट इनपुट एका मजकूर प्रॉम्प्टमध्ये एन्कॅप्सुलेट करणे.

मेटा प्रॉम्प्टचे एक उदाहरण असेल:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

आता, आपण आपल्या डेमोमध्ये मेटा प्रॉम्प्ट्सचा वापर कसा करू शकतो ते पाहूया.

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

वरील प्रॉम्प्टमधून, आपण पाहू शकता की सर्व निर्माण केलेल्या प्रतिमा मेटाप्रॉम्प्ट विचारात घेतात.

## असाइनमेंट - चला विद्यार्थ्यांना सक्षम करूया

आम्ही या धड्याच्या सुरुवातीला Edu4All ची ओळख करून दिली. आता विद्यार्थ्यांना त्यांच्या मूल्यांकनांसाठी प्रतिमा निर्माण करण्यासाठी सक्षम करण्याची वेळ आली आहे.

विद्यार्थ्यांना त्यांच्या मूल्यांकनांसाठी स्मारके असलेल्या प्रतिमा निर्माण करायच्या आहेत, कोणती स्मारके हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना या कार्यात विविध संदर्भांमध्ये या स्मारकांना ठेवण्यासाठी त्यांच्या सर्जनशीलतेचा वापर करण्यास सांगितले जाते.

## समाधान

येथे एक संभाव्य समाधान आहे:

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

## उत्तम काम! आपले शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आपले जनरेटिव्ह AI ज्ञान वाढवण्यासाठी आमचा [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पहा!

लेसन 10 वर जा जिथे आपण [कमी-कोडसह AI अॅप्लिकेशन्स तयार करणे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) पाहू.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अशुद्धता असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानव भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.