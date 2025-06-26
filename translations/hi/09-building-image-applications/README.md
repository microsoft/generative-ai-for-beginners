<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:11:08+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hi"
}
-->
# इमेज जनरेशन एप्लिकेशन बनाना

LLMs के पास सिर्फ टेक्स्ट जनरेशन से ज्यादा कुछ है। यह टेक्स्ट विवरण से इमेज भी जनरेट कर सकते हैं। इमेज को एक माध्यम के रूप में रखने से MedTech, वास्तुकला, पर्यटन, गेम डेवलपमेंट और अन्य कई क्षेत्रों में अत्यधिक उपयोगी हो सकता है। इस अध्याय में, हम दो सबसे लोकप्रिय इमेज जनरेशन मॉडल, DALL-E और Midjourney पर विचार करेंगे।

## परिचय

इस पाठ में, हम कवर करेंगे:

- इमेज जनरेशन और यह क्यों उपयोगी है।
- DALL-E और Midjourney, ये क्या हैं, और ये कैसे काम करते हैं।
- आप एक इमेज जनरेशन ऐप कैसे बनाएंगे।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- एक इमेज जनरेशन एप्लिकेशन बनाना।
- अपने एप्लिकेशन के लिए मेटा प्रॉम्प्ट्स के साथ सीमाएँ निर्धारित करना।
- DALL-E और Midjourney के साथ काम करना।

## इमेज जनरेशन एप्लिकेशन क्यों बनाएं?

इमेज जनरेशन एप्लिकेशन जनरेटिव AI की क्षमताओं का पता लगाने का एक शानदार तरीका है। इन्हें, उदाहरण के लिए, उपयोग किया जा सकता है:

- **इमेज संपादन और संश्लेषण**। आप विभिन्न उपयोग मामलों के लिए इमेज जनरेट कर सकते हैं, जैसे कि इमेज संपादन और इमेज संश्लेषण।

- **विभिन्न उद्योगों में लागू**। इन्हें MedTech, पर्यटन, गेम डेवलपमेंट और अन्य कई उद्योगों के लिए इमेज जनरेट करने के लिए भी उपयोग किया जा सकता है।

## परिदृश्य: Edu4All

इस पाठ के एक भाग के रूप में, हम इस पाठ में हमारे स्टार्टअप, Edu4All के साथ काम करना जारी रखेंगे। छात्र अपनी मूल्यांकनों के लिए इमेज जनरेट करेंगे, ठीक किस प्रकार की इमेज यह छात्रों पर निर्भर करता है, लेकिन वे अपनी खुद की परीकथा के लिए चित्रण कर सकते हैं या अपनी कहानी के लिए एक नया पात्र बना सकते हैं या अपने विचारों और अवधारणाओं को दृष्टिगत बनाने में मदद कर सकते हैं।

यहाँ एक उदाहरण है कि अगर वे कक्षा में स्मारकों पर काम कर रहे हैं तो Edu4All के छात्र क्या जनरेट कर सकते हैं:

![Edu4All स्टार्टअप, स्मारकों पर कक्षा, एफिल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hi.png)

एक प्रॉम्प्ट का उपयोग करते हुए

> "सुबह की धूप में एफिल टॉवर के बगल में कुत्ता"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय इमेज जनरेशन मॉडल हैं, ये आपको प्रॉम्प्ट्स का उपयोग करके इमेज जनरेट करने की अनुमति देते हैं।

### DALL-E

आइए DALL-E से शुरू करते हैं, जो एक जनरेटिव AI मॉडल है जो टेक्स्ट विवरण से इमेज जनरेट करता है।

> [DALL-E दो मॉडलों, CLIP और डिफ्यूज्ड अटेंशन का संयोजन है](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो इमेज और टेक्स्ट से डेटा के संख्यात्मक प्रतिनिधित्व, जिसे एम्बेडिंग कहते हैं, जनरेट करता है।

- **डिफ्यूज्ड अटेंशन**, एक मॉडल है जो एम्बेडिंग से इमेज जनरेट करता है। DALL-E इमेज और टेक्स्ट के डेटासेट पर प्रशिक्षित है और इसे टेक्स्ट विवरण से इमेज जनरेट करने के लिए उपयोग किया जा सकता है। उदाहरण के लिए, DALL-E को टोपी में बिल्ली या मोहॉक के साथ कुत्ते की इमेज जनरेट करने के लिए उपयोग किया जा सकता है।

### Midjourney

Midjourney DALL-E की तरह काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से इमेज जनरेट करता है। Midjourney को प्रॉम्प्ट्स का उपयोग करके इमेज जनरेट करने के लिए भी उपयोग किया जा सकता है जैसे "टोपी में बिल्ली", या "मोहॉक के साथ कुत्ता"।

![Midjourney द्वारा जनरेट की गई इमेज, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_चित्र साभार: विकिपीडिया, Midjourney द्वारा जनरेट की गई इमेज_

## DALL-E और Midjourney कैसे काम करते हैं

पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफार्मर आर्किटेक्चर पर आधारित है जिसमें _ऑटोरिग्रेसिव ट्रांसफार्मर_ होता है।

एक _ऑटोरिग्रेसिव ट्रांसफार्मर_ यह परिभाषित करता है कि एक मॉडल टेक्स्ट विवरण से इमेज कैसे जनरेट करता है, यह एक पिक्सेल को एक बार में जनरेट करता है, और फिर अगला पिक्सेल जनरेट करने के लिए जनरेट किए गए पिक्सेल का उपयोग करता है। एक न्यूरल नेटवर्क में कई परतों के माध्यम से गुजरते हुए, जब तक कि इमेज पूरी न हो जाए।

इस प्रक्रिया के साथ, DALL-E, जनरेट की गई इमेज में विशेषताओं, वस्तुओं, विशेषताओं और अधिक को नियंत्रित करता है। हालाँकि, DALL-E 2 और 3 के पास जनरेट की गई इमेज पर अधिक नियंत्रण है।

## अपना पहला इमेज जनरेशन एप्लिकेशन बनाना

तो एक इमेज जनरेशन एप्लिकेशन बनाने के लिए क्या आवश्यक है? आपको निम्नलिखित लाइब्रेरीज़ की आवश्यकता है:

- **python-dotenv**, यह लाइब्रेरी आपके रहस्यों को कोड से दूर _.env_ फ़ाइल में रखने के लिए अत्यधिक अनुशंसित है।
- **openai**, यह लाइब्रेरी है जिसका उपयोग आप OpenAI API के साथ बातचीत करने के लिए करेंगे।
- **pillow**, पायथन में इमेज के साथ काम करने के लिए।
- **requests**, HTTP अनुरोध करने में आपकी मदद करने के लिए।

1. निम्नलिखित सामग्री के साथ एक फ़ाइल _.env_ बनाएं:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   अपने संसाधन के लिए Azure Portal में "कुंजियाँ और समापन बिंदु" अनुभाग में यह जानकारी ढूंढें।

1. उपरोक्त लाइब्रेरीज़ को _requirements.txt_ नामक फ़ाइल में एकत्र करें:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. इसके बाद, वर्चुअल एन्वायरनमेंट बनाएं और लाइब्रेरीज़ इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   विंडोज़ के लिए, अपना वर्चुअल एन्वायरनमेंट बनाने और सक्रिय करने के लिए निम्नलिखित कमांड का उपयोग करें:

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

आइए इस कोड की व्याख्या करें:

- सबसे पहले, हम उन लाइब्रेरीज़ को इंपोर्ट करते हैं जिनकी हमें आवश्यकता है, जिसमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी, और Pillow लाइब्रेरी शामिल हैं।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- इसके बाद, हम _.env_ फ़ाइल से पर्यावरणीय वेरिएबल्स को लोड करते हैं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- उसके बाद, हम OpenAI API के लिए समापन बिंदु, कुंजी, संस्करण और प्रकार सेट करते हैं।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- फिर, हम इमेज जनरेट करते हैं:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  उपरोक्त कोड एक JSON ऑब्जेक्ट के साथ प्रतिक्रिया करता है जिसमें जनरेट की गई इमेज का URL होता है। हम इमेज को डाउनलोड करने और उसे फ़ाइल में सेव करने के लिए URL का उपयोग कर सकते हैं।

- अंत में, हम इमेज को खोलते हैं और इसे प्रदर्शित करने के लिए मानक इमेज व्यूअर का उपयोग करते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### इमेज जनरेट करने पर अधिक विवरण

आइए उस कोड पर नज़र डालें जो इमेज जनरेट करता है:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, वह टेक्स्ट प्रॉम्प्ट है जिसका उपयोग इमेज जनरेट करने के लिए किया जाता है। इस मामले में, हम "बनी घोड़े पर, लॉलीपॉप पकड़े हुए, धुंधले मैदान में जहां डैफोडिल्स उगते हैं" प्रॉम्प्ट का उपयोग कर रहे हैं।
- **size**, जनरेट की गई इमेज का आकार है। इस मामले में, हम 1024x1024 पिक्सेल की इमेज जनरेट कर रहे हैं।
- **n**, जनरेट की गई इमेज की संख्या है। इस मामले में, हम दो इमेज जनरेट कर रहे हैं।
- **temperature**, एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। तापमान 0 और 1 के बीच एक मान है जहां 0 का अर्थ है कि आउटपुट निर्धारक है और 1 का अर्थ है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

इमेज के साथ और भी चीजें की जा सकती हैं जिन्हें हम अगले खंड में कवर करेंगे।

## इमेज जनरेशन की अतिरिक्त क्षमताएं

अब तक आपने देखा कि कैसे हम पायथन में कुछ लाइनों का उपयोग करके इमेज जनरेट कर पाए। हालांकि, इमेज के साथ और भी चीजें की जा सकती हैं।

आप निम्नलिखित भी कर सकते हैं:

- **संपादन करें**। एक मौजूदा इमेज, एक मास्क और एक प्रॉम्प्ट प्रदान करके, आप एक इमेज को बदल सकते हैं। उदाहरण के लिए, आप एक इमेज के एक हिस्से में कुछ जोड़ सकते हैं। हमारी बनी इमेज की कल्पना करें, आप बनी को एक टोपी जोड़ सकते हैं। आप यह कैसे करेंगे यह इमेज, मास्क (बदलाव के लिए क्षेत्र की पहचान करना) और एक टेक्स्ट प्रॉम्प्ट प्रदान करके किया जाएगा।

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

  बेस इमेज में केवल खरगोश होगा लेकिन अंतिम इमेज में खरगोश पर टोपी होगी।

- **विविधताएं बनाएं**। विचार यह है कि आप एक मौजूदा इमेज लें और उससे विविधताएं बनाने के लिए कहें। एक विविधता बनाने के लिए, आप एक इमेज और एक टेक्स्ट प्रॉम्प्ट प्रदान करते हैं और कोड इस प्रकार होता है:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ध्यान दें, यह केवल OpenAI पर समर्थित है

## तापमान

तापमान एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। तापमान 0 और 1 के बीच एक मान है जहां 0 का अर्थ है कि आउटपुट निर्धारक है और 1 का अर्थ है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

आइए देखें कि तापमान कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट: "बनी घोड़े पर, लॉलीपॉप पकड़े हुए, धुंधले मैदान में जहां डैफोडिल्स उगते हैं"

![घोड़े पर लॉलीपॉप पकड़े हुए बनी, संस्करण 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hi.png)

अब उसी प्रॉम्प्ट को चलाएं ताकि यह देखा जा सके कि हमें दो बार एक ही इमेज नहीं मिलेगी:

![घोड़े पर बनी की जनरेट की गई इमेज](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hi.png)

जैसा कि आप देख सकते हैं, इमेज समान हैं, लेकिन एक जैसी नहीं हैं। आइए तापमान मान को 0.1 पर बदलें और देखें कि क्या होता है:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलना

तो आइए प्रतिक्रिया को अधिक निर्धारक बनाने की कोशिश करें। हम उन दो इमेजों से देख सकते हैं जिन्हें हमने जनरेट किया था कि पहली इमेज में एक बनी है और दूसरी इमेज में एक घोड़ा है, इसलिए इमेज बहुत भिन्न हैं।

आइए इसलिए हमारे कोड को बदलें और तापमान को 0 पर सेट करें, इस प्रकार:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप इस कोड को चलाते हैं, तो आपको ये दो इमेज मिलती हैं:

- ![तापमान 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hi.png)
- ![तापमान 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hi.png)

यहाँ आप स्पष्ट रूप से देख सकते हैं कि इमेज एक-दूसरे से अधिक मिलती-जुलती हैं।

## मेटाप्रॉम्प्ट्स के साथ अपने एप्लिकेशन के लिए सीमाएं कैसे निर्धारित करें

हमारे डेमो के साथ, हम पहले से ही अपने ग्राहकों के लिए इमेज जनरेट कर सकते हैं। हालांकि, हमें अपने एप्लिकेशन के लिए कुछ सीमाएं बनाने की जरूरत है।

उदाहरण के लिए, हम ऐसी इमेज जनरेट नहीं करना चाहते जो काम के लिए सुरक्षित नहीं हैं, या जो बच्चों के लिए उपयुक्त नहीं हैं।

हम यह _मेटाप्रॉम्प्ट्स_ के साथ कर सकते हैं। मेटाप्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स हैं जिनका उपयोग जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए किया जाता है। उदाहरण के लिए, हम मेटाप्रॉम्प्ट्स का उपयोग आउटपुट को नियंत्रित करने के लिए कर सकते हैं, और यह सुनिश्चित कर सकते हैं कि जनरेट की गई इमेज काम के लिए सुरक्षित हैं, या बच्चों के लिए उपयुक्त हैं।

### यह कैसे काम करता है?

अब, मेटा प्रॉम्प्ट्स कैसे काम करते हैं?

मेटा प्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स हैं जिनका उपयोग जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए किया जाता है, इन्हें टेक्स्ट प्रॉम्प्ट से पहले रखा जाता है, और इन्हें मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किया जाता है और एप्लिकेशन में एम्बेड किया जाता है ताकि मॉडल के आउटपुट को नियंत्रित किया जा सके। प्रॉम्प्ट इनपुट और मेटा प्रॉम्प्ट इनपुट को एक ही टेक्स्ट प्रॉम्प्ट में समाहित करते हुए।

एक मेटा प्रॉम्प्ट का उदाहरण निम्नलिखित होगा:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, आइए देखें कि हम अपने डेमो में मेटा प्रॉम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

ऊपर दिए गए प्रॉम्प्ट से, आप देख सकते हैं कि सभी इमेज जो बनाई जा रही हैं वे मेटाप्रॉम्प्ट पर विचार करती हैं।

## असाइनमेंट - छात्रों को सक्षम करें

हमने इस पाठ की शुरुआत में Edu4All को पेश किया था। अब समय है कि छात्रों को उनकी मूल्यांकनों के लिए इमेज जनरेट करने के लिए सक्षम किया जाए।

छात्र अपनी मूल्यांकनों के लिए स्मारकों वाली इमेज बनाएंगे, ठीक कौन से स्मारक यह छात्रों पर निर्भर करता है। छात्रों से यह कार्य करने में अपनी रचनात्मकता का उपयोग करने के लिए कहा जाता है ताकि ये स्मारक विभिन्न संदर्भों में रखे जा सकें।

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

इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव AI लर्निंग कलेक्शन](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखना सुनिश्चित करें ताकि आप अपनी जनरेटिव AI ज्ञान को और बढ़ा सकें!

पाठ 10 पर जाएं जहां हम देखेंगे कि [कम-कोड AI एप्लिकेशन कैसे बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।