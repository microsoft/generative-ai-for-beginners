<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:34:48+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hi"
}
-->
# इमेज जनरेशन एप्लिकेशन बनाना

LLMs में टेक्स्ट जनरेशन से अधिक कुछ है। टेक्स्ट विवरणों से इमेज बनाना भी संभव है। इमेज को एक मोडालिटी के रूप में कई क्षेत्रों में अत्यधिक उपयोगी माना जा सकता है जैसे MedTech, आर्किटेक्चर, पर्यटन, गेम डेवलपमेंट और अधिक। इस अध्याय में, हम दो सबसे लोकप्रिय इमेज जनरेशन मॉडल, DALL-E और Midjourney को देखेंगे।

## परिचय

इस पाठ में, हम कवर करेंगे:

- इमेज जनरेशन और क्यों यह उपयोगी है।
- DALL-E और Midjourney, वे क्या हैं, और वे कैसे काम करते हैं।
- कैसे आप एक इमेज जनरेशन एप बना सकते हैं।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- एक इमेज जनरेशन एप्लिकेशन बनाना।
- अपने एप्लिकेशन के लिए मेटा प्रॉम्प्ट्स के साथ सीमाएं परिभाषित करना।
- DALL-E और Midjourney के साथ काम करना।

## इमेज जनरेशन एप्लिकेशन क्यों बनाएं?

इमेज जनरेशन एप्लिकेशन जनरेटिव AI की क्षमताओं का अन्वेषण करने का एक शानदार तरीका है। वे उदाहरण के लिए उपयोग किए जा सकते हैं:

- **इमेज एडिटिंग और सिंथेसिस**। आप इमेज एडिटिंग और इमेज सिंथेसिस जैसे विभिन्न उपयोग मामलों के लिए इमेज जनरेट कर सकते हैं।

- **विभिन्न उद्योगों में लागू**। वे Medtech, पर्यटन, गेम डेवलपमेंट और अधिक जैसे विभिन्न उद्योगों के लिए इमेज जनरेट करने के लिए भी उपयोग किए जा सकते हैं।

## परिदृश्य: Edu4All

इस पाठ के हिस्से के रूप में, हम अपने स्टार्टअप, Edu4All के साथ काम करना जारी रखेंगे। छात्र अपनी असाइनमेंट्स के लिए इमेज बनाएंगे, ठीक क्या इमेज बनाई जाए यह छात्रों पर निर्भर है, लेकिन वे अपनी परी कथा के लिए चित्र बना सकते हैं या अपनी कहानी के लिए एक नया पात्र बना सकते हैं या उन्हें अपने विचारों और अवधारणाओं को चित्रित करने में मदद कर सकते हैं।

उदाहरण के लिए, यदि वे कक्षा में स्मारकों पर काम कर रहे हैं तो Edu4All के छात्र क्या जनरेट कर सकते हैं:

![Edu4All स्टार्टअप, कक्षा स्मारकों पर, एफिल टॉवर](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.hi.png)

एक प्रॉम्प्ट का उपयोग करते हुए जैसे

> "सुबह की धूप में एफिल टॉवर के पास कुत्ता"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय इमेज जनरेशन मॉडल हैं, वे आपको प्रॉम्प्ट्स का उपयोग करके इमेज जनरेट करने की अनुमति देते हैं।

### DALL-E

चलो DALL-E से शुरू करते हैं, जो एक जनरेटिव AI मॉडल है जो टेक्स्ट विवरणों से इमेज जनरेट करता है।

> [DALL-E दो मॉडलों, CLIP और डिफ्यूज्ड अटेंशन का संयोजन है](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो इमेज और टेक्स्ट से एम्बेडिंग्स, जो डेटा के संख्यात्मक प्रतिनिधित्व होते हैं, जनरेट करता है।

- **डिफ्यूज्ड अटेंशन**, एक मॉडल है जो एम्बेडिंग्स से इमेज जनरेट करता है। DALL-E इमेज और टेक्स्ट के डेटासेट पर प्रशिक्षित है और टेक्स्ट विवरणों से इमेज जनरेट करने के लिए उपयोग किया जा सकता है। उदाहरण के लिए, DALL-E का उपयोग टोपी में बिल्ली की या मोहॉक के साथ कुत्ते की इमेज जनरेट करने के लिए किया जा सकता है।

### Midjourney

Midjourney DALL-E के समान तरीके से काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से इमेज जनरेट करता है। Midjourney का उपयोग प्रॉम्प्ट्स जैसे "टोपी में बिल्ली", या "मोहॉक के साथ कुत्ता" का उपयोग करके इमेज जनरेट करने के लिए भी किया जा सकता है।

![Midjourney द्वारा जनरेट की गई इमेज, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_इमेज क्रेडिट विकिपीडिया, Midjourney द्वारा जनरेट की गई इमेज_

## DALL-E और Midjourney कैसे काम करते हैं

पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफार्मर आर्किटेक्चर पर आधारित है जिसमें एक _ऑटोरेग्रेसिव ट्रांसफार्मर_ होता है।

एक _ऑटोरेग्रेसिव ट्रांसफार्मर_ परिभाषित करता है कि एक मॉडल टेक्स्ट विवरणों से इमेज कैसे जनरेट करता है, यह एक समय में एक पिक्सेल जनरेट करता है, और फिर जनरेट किए गए पिक्सेल का उपयोग करके अगला पिक्सेल जनरेट करता है। एक न्यूरल नेटवर्क में कई लेयरों से गुजरते हुए, जब तक कि इमेज पूरी नहीं हो जाती।

इस प्रक्रिया के साथ, DALL-E, इमेज में जनरेट की गई विशेषताओं, वस्तुओं, लक्षणों और अधिक को नियंत्रित करता है। हालांकि, DALL-E 2 और 3 के पास जनरेट की गई इमेज पर अधिक नियंत्रण होता है।

## अपनी पहली इमेज जनरेशन एप्लिकेशन बनाना

तो एक इमेज जनरेशन एप्लिकेशन बनाने के लिए क्या चाहिए? आपको निम्नलिखित लाइब्रेरी की आवश्यकता है:

- **python-dotenv**, आप अत्यधिक अनुशंसा करते हैं कि इस लाइब्रेरी का उपयोग करके अपने सीक्रेट्स को कोड से दूर _.env_ फ़ाइल में रखें।
- **openai**, यह लाइब्रेरी वह है जिसका उपयोग आप OpenAI API के साथ इंटरैक्ट करने के लिए करेंगे।
- **pillow**, Python में इमेज के साथ काम करने के लिए।
- **requests**, आपको HTTP अनुरोध करने में मदद करने के लिए।

1. निम्नलिखित सामग्री के साथ एक फ़ाइल _.env_ बनाएँ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal में अपने संसाधन के लिए "Keys and Endpoint" अनुभाग में इस जानकारी का पता लगाएँ।

1. उपरोक्त लाइब्रेरी को _requirements.txt_ नामक फ़ाइल में इस प्रकार एकत्रित करें:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. इसके बाद, वर्चुअल एनवायरनमेंट बनाएं और लाइब्रेरी इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   विंडोज के लिए, अपने वर्चुअल एनवायरनमेंट को बनाने और सक्रिय करने के लिए निम्नलिखित कमांड का उपयोग करें:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फ़ाइल में निम्नलिखित कोड जोड़ें:

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

इस कोड को समझाएं:

- पहले, हम आवश्यक लाइब्रेरी आयात करते हैं, जिसमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी, और Pillow लाइब्रेरी शामिल हैं।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- इसके बाद, हम _.env_ फ़ाइल से एनवायरनमेंट वेरिएबल्स लोड करते हैं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- उसके बाद, हम OpenAI API के लिए एंडपॉइंट, की, वर्जन और प्रकार सेट करते हैं।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- इसके बाद, हम इमेज जनरेट करते हैं:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  ऊपर का कोड एक JSON ऑब्जेक्ट के साथ प्रतिक्रिया करता है जिसमें जनरेट की गई इमेज का URL होता है। हम URL का उपयोग करके इमेज डाउनलोड कर सकते हैं और इसे एक फ़ाइल में सहेज सकते हैं।

- अंत में, हम इमेज खोलते हैं और इसे मानक इमेज व्यूअर का उपयोग करके प्रदर्शित करते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### इमेज जनरेट करने पर अधिक विवरण

आइए उस कोड को अधिक विस्तार से देखें जो इमेज जनरेट करता है:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **प्रॉम्प्ट**, वह टेक्स्ट प्रॉम्प्ट है जिसका उपयोग इमेज जनरेट करने के लिए किया जाता है। इस मामले में, हम प्रॉम्प्ट "घोड़े पर बनी, लॉलीपॉप पकड़ते हुए, धुंधली घास के मैदान पर जहां डैफोडिल्स उगते हैं" का उपयोग कर रहे हैं।
- **साइज**, वह आकार है जो जनरेट की गई इमेज का होता है। इस मामले में, हम 1024x1024 पिक्सल की इमेज जनरेट कर रहे हैं।
- **n**, वह संख्या है जो जनरेट की गई इमेज की होती है। इस मामले में, हम दो इमेज जनरेट कर रहे हैं।
- **टेम्परेचर**, एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। टेम्परेचर एक मान है जो 0 और 1 के बीच होता है जहां 0 का अर्थ है कि आउटपुट निश्चित है और 1 का अर्थ है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

इमेज के साथ और भी चीजें हैं जो हम अगले सेक्शन में कवर करेंगे।

## इमेज जनरेशन की अतिरिक्त क्षमताएं

आपने अब तक देखा कि हम कुछ पंक्तियों में Python का उपयोग करके इमेज जनरेट करने में सक्षम थे। हालांकि, इमेज के साथ और भी चीजें हैं जो आप कर सकते हैं।

आप निम्नलिखित भी कर सकते हैं:

- **संपादन करें**। एक मौजूदा इमेज, मास्क और प्रॉम्प्ट प्रदान करके, आप इमेज को बदल सकते हैं। उदाहरण के लिए, आप इमेज के एक हिस्से में कुछ जोड़ सकते हैं। हमारी बनी इमेज की कल्पना करें, आप बनी को एक टोपी जोड़ सकते हैं। आप ऐसा कैसे करेंगे, यह इमेज, मास्क (परिवर्तन के लिए क्षेत्र की पहचान करने वाला) और टेक्स्ट प्रॉम्प्ट प्रदान करके किया जाएगा।

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

  बेस इमेज केवल खरगोश को शामिल करेगी लेकिन अंतिम इमेज में खरगोश पर टोपी होगी।

- **वेरिएशन बनाएं**। विचार यह है कि आप एक मौजूदा इमेज लेते हैं और अनुरोध करते हैं कि वेरिएशन बनाए जाएं। एक वेरिएशन बनाने के लिए, आप एक इमेज और एक टेक्स्ट प्रॉम्प्ट प्रदान करते हैं और कोड इस प्रकार होता है:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यह केवल OpenAI पर समर्थित है

## टेम्परेचर

टेम्परेचर एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। टेम्परेचर एक मान है जो 0 और 1 के बीच होता है जहां 0 का अर्थ है कि आउटपुट निश्चित है और 1 का अर्थ है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

आइए देखें कि टेम्परेचर कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट : "घोड़े पर बनी, लॉलीपॉप पकड़ते हुए, धुंधली घास के मैदान पर जहां डैफोडिल्स उगते हैं"

![घोड़े पर बनी लॉलीपॉप पकड़ते हुए, संस्करण 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.hi.png)

अब चलो वही प्रॉम्प्ट चलाएं ताकि हम देख सकें कि हमें एक ही इमेज दो बार नहीं मिलेगी:

![घोड़े पर बनी की जनरेट की गई इमेज](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.hi.png)

जैसा कि आप देख सकते हैं, इमेजें समान हैं, लेकिन एक जैसी नहीं हैं। आइए टेम्परेचर मान को 0.1 में बदलने की कोशिश करें और देखें क्या होता है:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### टेम्परेचर बदलना

तो चलो प्रतिक्रिया को अधिक निश्चित बनाने की कोशिश करें। हम देख सकते हैं कि हमने जो दो इमेजें जनरेट की हैं उनमें से पहली इमेज में एक खरगोश है और दूसरी इमेज में एक घोड़ा है, इसलिए इमेजें बहुत भिन्न हैं।

आइए इसलिए हमारा कोड बदलें और टेम्परेचर को 0 सेट करें, जैसे:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप इस कोड को चलाते हैं, तो आपको ये दो इमेजें मिलती हैं:

- ![टेम्परेचर 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.hi.png)
- ![टेम्परेचर 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.hi.png)

यहाँ आप स्पष्ट रूप से देख सकते हैं कि इमेजें एक-दूसरे से अधिक मिलती हैं।

## मेटाप्रोम्प्ट्स के साथ अपने एप्लिकेशन के लिए सीमाएं कैसे परिभाषित करें

हमारे डेमो के साथ, हम पहले से ही अपने ग्राहकों के लिए इमेज जनरेट कर सकते हैं। हालांकि, हमें अपने एप्लिकेशन के लिए कुछ सीमाएं बनाने की आवश्यकता है।

उदाहरण के लिए, हम ऐसी इमेज जनरेट नहीं करना चाहते हैं जो काम के लिए सुरक्षित न हों, या जो बच्चों के लिए उपयुक्त न हों।

हम _मेटाप्रोम्प्ट्स_ के साथ ऐसा कर सकते हैं। मेटाप्रोम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जिनका उपयोग जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए किया जाता है। उदाहरण के लिए, हम मेटाप्रोम्प्ट्स का उपयोग आउटपुट को नियंत्रित करने के लिए कर सकते हैं, और सुनिश्चित कर सकते हैं कि जनरेट की गई इमेज काम के लिए सुरक्षित हों, या बच्चों के लिए उपयुक्त हों।

### यह कैसे काम करता है?

अब, मेटाप्रोम्प्ट्स कैसे काम करते हैं?

मेटाप्रोम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जिनका उपयोग जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए किया जाता है, वे टेक्स्ट प्रॉम्प्ट से पहले स्थित होते हैं, और मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किए जाते हैं और एप्लिकेशन में मॉडल के आउटपुट को नियंत्रित करने के लिए एम्बेड किए जाते हैं। प्रॉम्प्ट इनपुट और मेटाप्रोम्प्ट इनपुट को एकल टेक्स्ट प्रॉम्प्ट में संलग्न करना।

मेटाप्रोम्प्ट का एक उदाहरण निम्नलिखित होगा:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, चलो देखें कि हम अपने डेमो में मेटाप्रोम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

ऊपर के प्रॉम्प्ट से, आप देख सकते हैं कि सभी बनाई जा रही इमेजें मेटाप्रोम्प्ट को ध्यान में रखती हैं।

## असाइनमेंट - चलो छात्रों को सक्षम करें

हमने इस पाठ की शुरुआत में Edu4All का परिचय दिया। अब समय है कि छात्रों को उनकी असाइनमेंट्स के लिए इमेज जनरेट करने में सक्षम बनाएं।

छात्र अपनी असाइनमेंट्स के लिए स्मारकों को शामिल करने वाली इमेज बनाएंगे, ठीक क्या स्मारक बनाए जाएं यह छात्रों पर निर्भर है। छात्रों को इस कार्य में अपनी रचनात्मकता का उपयोग करने के लिए कहा गया है ताकि ये स्मारक विभिन्न संदर्भों में रखे जा सकें।

## समाधान

यहाँ एक संभावित समाधान है:

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

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारी [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपने जनरेटिव AI ज्ञान को बढ़ाते रहें!

Lesson 10 पर जाएं जहां हम देखेंगे कि कैसे [कम-कोड के साथ AI एप्लिकेशन बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।