<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:02:52+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "mr"
}
-->
# प्रतिमा निर्मिती अनुप्रयोग तयार करणे

LLMs च्या तुलनेत मजकूर निर्मितीपेक्षा बरेच काही आहे. मजकूर वर्णनांमधून प्रतिमा तयार करणे देखील शक्य आहे. प्रतिमा या रूपात असणे हे MedTech, आर्किटेक्चर, पर्यटन, गेम विकास आणि इतर अनेक क्षेत्रांमध्ये अत्यंत उपयुक्त ठरू शकते. या अध्यायात, आपण दोन सर्वात लोकप्रिय प्रतिमा निर्मिती मॉडेल्स, DALL-E आणि Midjourney यांचा अभ्यास करू.

## परिचय

या धड्यात, आपण कव्हर करू:

- प्रतिमा निर्मिती आणि ती का उपयुक्त आहे.
- DALL-E आणि Midjourney, ते काय आहेत आणि ते कसे कार्य करतात.
- आपण प्रतिमा निर्मिती अनुप्रयोग कसा तयार कराल.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, आपण सक्षम असाल:

- प्रतिमा निर्मिती अनुप्रयोग तयार करणे.
- आपल्या अनुप्रयोगासाठी मेटा प्रॉम्प्टसह सीमा परिभाषित करा.
- DALL-E आणि Midjourney सह कार्य करा.

## प्रतिमा निर्मिती अनुप्रयोग का तयार करायचा?

प्रतिमा निर्मिती अनुप्रयोग हे जनरेटिव्ह AI च्या क्षमतांचा शोध घेण्याचा एक उत्तम मार्ग आहे. ते, उदाहरणार्थ, यासाठी वापरले जाऊ शकतात:

- **प्रतिमा संपादन आणि संश्लेषण**. आपण प्रतिमा संपादन आणि प्रतिमा संश्लेषण यासारख्या विविध वापर प्रकरणांसाठी प्रतिमा तयार करू शकता.

- **विविध उद्योगांवर लागू**. ते Medtech, Tourism, Game development आणि इतर अनेक उद्योगांसाठी प्रतिमा तयार करण्यासाठी देखील वापरले जाऊ शकतात.

## प्रसंग: Edu4All

या धड्याचा एक भाग म्हणून, आम्ही Edu4All या आमच्या स्टार्टअपसह काम करत राहू. विद्यार्थी त्यांच्या मूल्यमापनासाठी प्रतिमा तयार करतील, नेमक्या कोणत्या प्रतिमा हे विद्यार्थ्यांवर अवलंबून आहे, परंतु ते त्यांच्या स्वतःच्या परीकथेसाठी चित्रण तयार करू शकतात किंवा त्यांच्या कथेतील नवीन पात्र तयार करू शकतात किंवा त्यांना त्यांच्या कल्पना आणि संकल्पना दृश्यमान करण्यात मदत करू शकतात.

उदाहरणार्थ, जर ते वर्गात स्मारकांवर काम करत असतील तर Edu4All चे विद्यार्थी काय तयार करू शकतील:

![Edu4All स्टार्टअप, स्मारकांवरील वर्ग, आयफेल टॉवर](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.mr.png)

अशा प्रॉम्प्टचा वापर करून

> "सकाळच्या उन्हात आयफेल टॉवरच्या शेजारी कुत्रा"

## DALL-E आणि Midjourney काय आहे?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय प्रतिमा निर्मिती मॉडेल्स आहेत, ते आपल्याला प्रॉम्प्ट्स वापरून प्रतिमा तयार करण्याची परवानगी देतात.

### DALL-E

DALL-E पासून सुरुवात करूया, जे एक जनरेटिव्ह AI मॉडेल आहे जे मजकूर वर्णनांमधून प्रतिमा तयार करते.

> [DALL-E हे दोन मॉडेल्स, CLIP आणि diffused attention यांचे संयोजन आहे](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, हे एक मॉडेल आहे जे प्रतिमा आणि मजकूरातून एम्बेडिंग्ज तयार करते, जे डेटाचे संख्यात्मक प्रतिनिधित्व आहेत.

- **Diffused attention**, हे एक मॉडेल आहे जे एम्बेडिंग्जमधून प्रतिमा तयार करते. DALL-E प्रतिमा आणि मजकूराच्या डेटासेटवर प्रशिक्षित आहे आणि मजकूर वर्णनांमधून प्रतिमा तयार करण्यासाठी वापरले जाऊ शकते. उदाहरणार्थ, DALL-E चा वापर टोपीतील मांजर किंवा मोहॉक असलेल्या कुत्र्याच्या प्रतिमा तयार करण्यासाठी केला जाऊ शकतो.

### Midjourney

Midjourney DALL-E प्रमाणेच कार्य करते, ते मजकूर प्रॉम्प्ट्समधून प्रतिमा तयार करते. Midjourney चा वापर "टोपीतील मांजर" किंवा "मोहॉक असलेले कुत्रा" सारख्या प्रॉम्प्ट्स वापरून प्रतिमा तयार करण्यासाठी देखील केला जाऊ शकतो.

![Midjourney द्वारे तयार केलेली प्रतिमा, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_प्रतिमा क्रेडिट विकिपीडिया, Midjourney द्वारे तयार केलेली प्रतिमा_

## DALL-E आणि Midjourney कसे कार्य करतात

प्रथम, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E हे एक जनरेटिव्ह AI मॉडेल आहे जे ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित आहे ज्यामध्ये एक _autoregressive transformer_ आहे.

एक _autoregressive transformer_ परिभाषित करते की मॉडेल मजकूर वर्णनांमधून प्रतिमा कशी तयार करते, ते एकावेळी एक पिक्सेल तयार करते आणि नंतर पुढील पिक्सेल तयार करण्यासाठी तयार केलेले पिक्सेल वापरते. न्यूरल नेटवर्कमधील अनेक स्तरांमधून जात, प्रतिमा पूर्ण होईपर्यंत.

या प्रक्रियेसह, DALL-E, प्रतिमेत तयार केलेल्या गुणधर्म, वस्तू, वैशिष्ट्ये आणि बरेच काही नियंत्रित करते. तथापि, DALL-E 2 आणि 3 ला तयार केलेल्या प्रतिमेवर अधिक नियंत्रण आहे.

## आपला पहिला प्रतिमा निर्मिती अनुप्रयोग तयार करणे

तर प्रतिमा निर्मिती अनुप्रयोग तयार करण्यासाठी काय आवश्यक आहे? आपल्याला खालील लायब्ररींची आवश्यकता आहे:

- **python-dotenv**, आपले गुपिते कोडपासून दूर _.env_ फाइलमध्ये ठेवण्यासाठी या लायब्ररीचा वापर करण्याची जोरदार शिफारस केली जाते.
- **openai**, ही लायब्ररी OpenAI API सह संवाद साधण्यासाठी आपण वापराल.
- **pillow**, Python मध्ये प्रतिमांसह कार्य करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यात मदत करण्यासाठी.

1. खालील सामग्रीसह एक फाइल _.env_ तयार करा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   आपल्या संसाधनासाठी Azure पोर्टलमध्ये "कळा आणि एंडपॉइंट" विभागात ही माहिती शोधा.

1. वरील लायब्ररी _requirements.txt_ नावाच्या फाइलमध्ये गोळा करा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. पुढे, आभासी वातावरण तयार करा आणि लायब्ररी स्थापित करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows साठी, आपले आभासी वातावरण तयार आणि सक्रिय करण्यासाठी खालील आदेश वापरा:

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

- प्रथम, आम्हाला आवश्यक असलेल्या लायब्ररी आयात करतो, ज्यात OpenAI लायब्ररी, dotenv लायब्ररी, requests लायब्ररी आणि Pillow लायब्ररीचा समावेश आहे.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- पुढे, आम्ही _.env_ फाइलमधून पर्यावरणीय चल लोड करतो.

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

- पुढे, आम्ही प्रतिमा तयार करतो:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  वरील कोड तयार केलेल्या प्रतिमेच्या URL समाविष्ट असलेल्या JSON ऑब्जेक्टसह प्रतिसाद देतो. आम्ही प्रतिमा डाउनलोड करण्यासाठी आणि फाइलमध्ये जतन करण्यासाठी URL वापरू शकतो.

- शेवटी, आम्ही प्रतिमा उघडतो आणि ती प्रदर्शित करण्यासाठी मानक प्रतिमा दर्शक वापरतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा तयार करण्यावरील अधिक तपशील

आम्ही प्रतिमा तयार करणाऱ्या कोडवर अधिक तपशीलवार नजर टाकूया:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ही प्रतिमा तयार करण्यासाठी वापरली जाणारी मजकूर प्रॉम्प्ट आहे. या प्रकरणात, आम्ही "फॉगgy मीडोमध्ये घोड्यावर साखरेची काठी धरलेला ससा, जिथे डॅफोडिल्स उगवतात" हा प्रॉम्प्ट वापरत आहोत.
- **size**, ही तयार केलेल्या प्रतिमेचा आकार आहे. या प्रकरणात, आम्ही 1024x1024 पिक्सेलची प्रतिमा तयार करत आहोत.
- **n**, ही तयार केलेल्या प्रतिमांची संख्या आहे. या प्रकरणात, आम्ही दोन प्रतिमा तयार करत आहोत.
- **temperature**, हा जनरेटिव्ह AI मॉडेलच्या आउटपुटच्या यादृच्छिकतेवर नियंत्रण ठेवणारा पॅरामीटर आहे. तापमान 0 आणि 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट यादृच्छिक आहे. डीफॉल्ट मूल्य 0.7 आहे.

प्रतिमांसह आपण अधिक गोष्टी करू शकता ज्या आपण पुढील विभागात कव्हर करू.

## प्रतिमा निर्मितीच्या अतिरिक्त क्षमता

आपण आतापर्यंत पाहिले आहे की आम्ही काही ओळींचा वापर करून प्रतिमा कशी तयार करू शकलो. तथापि, प्रतिमांसह आपण अधिक गोष्टी करू शकता.

आपण पुढील गोष्टी देखील करू शकता:

- **संपादन करा**. विद्यमान प्रतिमा, मुखवटा आणि प्रॉम्प्ट प्रदान करून, आपण प्रतिमा बदलू शकता. उदाहरणार्थ, आपण प्रतिमेच्या एका भागात काहीतरी जोडू शकता. आपल्या सशाच्या प्रतिमेची कल्पना करा, आपण सशाला टोपी जोडू शकता. आपण प्रतिमा, मुखवटा (बदलासाठी क्षेत्र ओळखणे) आणि काय करावे हे सांगण्यासाठी मजकूर प्रॉम्प्ट प्रदान करून ते कसे कराल.

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

  मूळ प्रतिमेत फक्त ससा असेल परंतु अंतिम प्रतिमेत सशावर टोपी असेल.

- **विविधता तयार करा**. कल्पना अशी आहे की आपण विद्यमान प्रतिमा घेता आणि विविधता तयार करण्याची विनंती करता. विविधता तयार करण्यासाठी, आपण प्रतिमा आणि मजकूर प्रॉम्प्ट प्रदान करता आणि कोड अशा प्रकारे:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > टीप, हे फक्त OpenAI वर समर्थित आहे

## तापमान

तापमान हा जनरेटिव्ह AI मॉडेलच्या आउटपुटच्या यादृच्छिकतेवर नियंत्रण ठेवणारा पॅरामीटर आहे. तापमान 0 आणि 1 दरम्यानचे मूल्य आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट यादृच्छिक आहे. डीफॉल्ट मूल्य 0.7 आहे.

तापमान कसे कार्य करते याचे उदाहरण पाहूया, हा प्रॉम्प्ट दोनदा चालवून:

> प्रॉम्प्ट: "फॉगgy मीडोमध्ये घोड्यावर साखरेची काठी धरलेला ससा, जिथे डॅफोडिल्स उगवतात"

![घोड्यावर साखरेची काठी धरलेला ससा, आवृत्ती 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.mr.png)

आता तोच प्रॉम्प्ट पुन्हा चालवूया फक्त हे पाहण्यासाठी की आपल्याला दोनदा एकसारखी प्रतिमा मिळणार नाही:

![घोड्यावर सशाची तयार केलेली प्रतिमा](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.mr.png)

जसे आपण पाहू शकता, प्रतिमा समान आहेत, परंतु एकसारख्या नाहीत. चला तापमान मूल्य 0.1 वर बदलण्याचा प्रयत्न करूया आणि काय होते ते पाहूया:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलणे

तर चला प्रतिसाद अधिक निश्चित करण्याचा प्रयत्न करूया. आम्ही तयार केलेल्या दोन प्रतिमांमधून निरीक्षण करू शकतो की पहिल्या प्रतिमेत ससा आहे आणि दुसऱ्या प्रतिमेत घोडा आहे, त्यामुळे प्रतिमा खूप वेगवेगळ्या आहेत.

म्हणून चला आपला कोड बदलूया आणि तापमान 0 वर सेट करूया, अशा प्रकारे:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता जेव्हा आपण हा कोड चालवता, तेव्हा आपल्याला या दोन प्रतिमा मिळतात:

- ![तापमान 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.mr.png)
- ![तापमान 0 , v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.mr.png)

येथे आपण स्पष्टपणे पाहू शकता की प्रतिमा एकमेकांशी अधिक साम्य आहेत.

## आपल्या अनुप्रयोगासाठी मेटाप्रॉम्प्ट्ससह सीमा कशी परिभाषित करावी

आमच्या डेमोसह, आम्ही आधीच आमच्या ग्राहकांसाठी प्रतिमा तयार करू शकतो. तथापि, आम्हाला आमच्या अनुप्रयोगासाठी काही सीमा तयार करण्याची आवश्यकता आहे.

उदाहरणार्थ, आम्हाला अशा प्रतिमा तयार करायच्या नाहीत ज्या कामासाठी सुरक्षित नाहीत किंवा मुलांसाठी योग्य नाहीत.

आम्ही हे _मेटाप्रॉम्प्ट्स_ सह करू शकतो. मेटाप्रॉम्प्ट्स हे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरलेले मजकूर प्रॉम्प्ट आहेत. उदाहरणार्थ, आम्ही आउटपुटवर नियंत्रण ठेवण्यासाठी मेटाप्रॉम्प्ट्स वापरू शकतो आणि तयार केलेल्या प्रतिमा कामासाठी सुरक्षित आहेत किंवा मुलांसाठी योग्य आहेत याची खात्री करू शकतो.

### ते कसे कार्य करते?

आता, मेटा प्रॉम्प्ट्स कसे कार्य करतात?

मेटा प्रॉम्प्ट्स हे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरलेले मजकूर प्रॉम्प्ट आहेत, ते मजकूर प्रॉम्प्टच्या आधी स्थित असतात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी अनुप्रयोगांमध्ये एम्बेड केले जातात. प्रॉम्प्ट इनपुट आणि मेटा प्रॉम्प्ट इनपुट एका मजकूर प्रॉम्प्टमध्ये समाविष्ट करणे.

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

वरील प्रॉम्प्टमधून, आपण पाहू शकता की तयार केल्या जाणाऱ्या सर्व प्रतिमा मेटाप्रॉम्प्टचा विचार करतात.

## असाइनमेंट - चला विद्यार्थ्यांना सक्षम करूया

या धड्याच्या सुरुवातीला आम्ही Edu4All चे परिचय दिले. आता विद्यार्थ्यांना त्यांच्या मूल्यमापनासाठी प्रतिमा तयार करण्यास सक्षम करण्याची वेळ आली आहे.

विद्यार्थी त्यांच्या मूल्यमापनासाठी स्मारके असलेल्या प्रतिमा तयार करतील, नेमकी कोणती स्मारके हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना या कार्यात त्यांच्या सर्जनशीलतेचा वापर करण्यास सांगितले जाते आणि या स्मारकांना वेगवेगळ्या संदर्भात ठेवण्यास सांगितले जाते.

## उपाय

येथे एक संभाव्य उपाय आहे:

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

हा धडा पूर्ण केल्यानंतर, आमचे [जनरेटिव्ह AI लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) तपासा जेणेकरून आपले जनरेटिव्ह AI ज्ञान वाढवणे सुरू ठेवा!

धडा 10 वर जा जिथे आपण पाहू की [लो-कोडसह AI अनुप्रयोग कसे तयार करायचे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज प्राधिकृत स्रोत म्हणून मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.