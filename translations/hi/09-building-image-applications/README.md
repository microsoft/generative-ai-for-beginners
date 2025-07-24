<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:20:09+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hi"
}
-->
# इमेज जनरेशन एप्लिकेशन बनाना

[![इमेज जनरेशन एप्लिकेशन बनाना](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hi.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM केवल टेक्स्ट जनरेशन तक सीमित नहीं हैं। टेक्स्ट विवरणों से इमेज भी बनाई जा सकती हैं। इमेज एक माध्यम के रूप में कई क्षेत्रों में बेहद उपयोगी हो सकती हैं, जैसे MedTech, वास्तुकला, पर्यटन, गेम डेवलपमेंट और भी बहुत कुछ। इस अध्याय में, हम दो सबसे लोकप्रिय इमेज जनरेशन मॉडल, DALL-E और Midjourney के बारे में जानेंगे।

## परिचय

इस पाठ में, हम निम्नलिखित विषयों को कवर करेंगे:

- इमेज जनरेशन क्या है और यह क्यों उपयोगी है।
- DALL-E और Midjourney क्या हैं, और ये कैसे काम करते हैं।
- आप एक इमेज जनरेशन ऐप कैसे बना सकते हैं।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- एक इमेज जनरेशन एप्लिकेशन बनाना।
- मेटा प्रॉम्प्ट्स के साथ अपने एप्लिकेशन की सीमाएं निर्धारित करना।
- DALL-E और Midjourney के साथ काम करना।

## इमेज जनरेशन एप्लिकेशन क्यों बनाएं?

इमेज जनरेशन एप्लिकेशन जनरेटिव AI की क्षमताओं को समझने का एक शानदार तरीका हैं। इन्हें निम्नलिखित के लिए इस्तेमाल किया जा सकता है:

- **इमेज एडिटिंग और सिंथेसिस**। आप विभिन्न उपयोग मामलों के लिए इमेज बना सकते हैं, जैसे इमेज एडिटिंग और इमेज सिंथेसिस।

- **विभिन्न उद्योगों में उपयोग**। इन्हें Medtech, पर्यटन, गेम डेवलपमेंट जैसे कई उद्योगों के लिए इमेज बनाने में भी इस्तेमाल किया जा सकता है।

## परिदृश्य: Edu4All

इस पाठ के हिस्से के रूप में, हम अपने स्टार्टअप Edu4All के साथ काम जारी रखेंगे। छात्र अपनी असाइनमेंट के लिए इमेज बनाएंगे, जो कि पूरी तरह से छात्रों पर निर्भर है कि वे क्या बनाना चाहते हैं। वे अपनी खुद की परी कथा के लिए चित्र बना सकते हैं, अपनी कहानी के लिए नया पात्र बना सकते हैं, या अपने विचारों और अवधारणाओं को विज़ुअलाइज़ कर सकते हैं।

उदाहरण के लिए, अगर Edu4All के छात्र स्मारकों पर कक्षा में काम कर रहे हैं, तो वे निम्नलिखित इमेज बना सकते हैं:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hi.png)

प्रॉम्प्ट का उपयोग करते हुए

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय इमेज जनरेशन मॉडल हैं, जो प्रॉम्प्ट्स का उपयोग करके इमेज बनाते हैं।

### DALL-E

आइए DALL-E से शुरू करते हैं, जो एक जनरेटिव AI मॉडल है जो टेक्स्ट विवरणों से इमेज बनाता है।

> [DALL-E दो मॉडलों, CLIP और diffused attention का संयोजन है](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो इमेज और टेक्स्ट से एम्बेडिंग्स (डेटा के संख्यात्मक प्रतिनिधित्व) बनाता है।

- **Diffused attention**, एक मॉडल है जो एम्बेडिंग्स से इमेज बनाता है। DALL-E को इमेज और टेक्स्ट के डेटासेट पर प्रशिक्षित किया गया है और यह टेक्स्ट विवरणों से इमेज बना सकता है। उदाहरण के लिए, DALL-E एक टोपी पहने हुए बिल्ली या मोकहॉक वाले कुत्ते की इमेज बना सकता है।

### Midjourney

Midjourney भी DALL-E की तरह काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से इमेज बनाता है। Midjourney का उपयोग “a cat in a hat” या “dog with a mohawk” जैसे प्रॉम्प्ट्स से इमेज बनाने के लिए किया जा सकता है।

![Midjourney द्वारा बनाई गई इमेज, मैकेनिकल कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_इमेज क्रेडिट: विकिपीडिया, Midjourney द्वारा बनाई गई इमेज_

## DALL-E और Midjourney कैसे काम करते हैं

सबसे पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफॉर्मर आर्किटेक्चर पर आधारित है, जिसमें _autoregressive transformer_ होता है।

एक _autoregressive transformer_ यह निर्धारित करता है कि मॉडल टेक्स्ट विवरणों से इमेज कैसे बनाता है, यह एक बार में एक पिक्सेल बनाता है, और फिर अगले पिक्सेल को बनाने के लिए पहले से बने पिक्सेल का उपयोग करता है। यह प्रक्रिया न्यूरल नेटवर्क की कई परतों से गुजरती है, जब तक कि इमेज पूरी न हो जाए।

इस प्रक्रिया के साथ, DALL-E इमेज में वस्तुएं, गुण, विशेषताएं आदि नियंत्रित करता है। हालांकि, DALL-E 2 और 3 में जनरेट की गई इमेज पर अधिक नियंत्रण होता है।

## अपनी पहली इमेज जनरेशन एप्लिकेशन बनाना

तो, इमेज जनरेशन एप्लिकेशन बनाने के लिए क्या चाहिए? आपको निम्नलिखित लाइब्रेरीज़ की जरूरत होगी:

- **python-dotenv**, यह लाइब्रेरी आपके सीक्रेट्स को कोड से अलग _.env_ फाइल में रखने के लिए अत्यधिक अनुशंसित है।
- **openai**, यह लाइब्रेरी OpenAI API के साथ इंटरैक्ट करने के लिए है।
- **pillow**, Python में इमेज के साथ काम करने के लिए।
- **requests**, HTTP रिक्वेस्ट बनाने में मदद के लिए।

1. एक _.env_ फाइल बनाएं और निम्नलिखित सामग्री डालें:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   यह जानकारी Azure Portal में आपके रिसोर्स के "Keys and Endpoint" सेक्शन में मिलेगी।

1. ऊपर दी गई लाइब्रेरीज़ को एक फाइल _requirements.txt_ में इकट्ठा करें:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. फिर, वर्चुअल एनवायरनमेंट बनाएं और लाइब्रेरीज़ इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows के लिए, वर्चुअल एनवायरनमेंट बनाने और सक्रिय करने के लिए निम्न कमांड्स का उपयोग करें:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फाइल में निम्न कोड जोड़ें:

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

आइए इस कोड को समझते हैं:

- सबसे पहले, हम आवश्यक लाइब्रेरीज़ इम्पोर्ट करते हैं, जिनमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी, और Pillow लाइब्रेरी शामिल हैं।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- इसके बाद, हम _.env_ फाइल से पर्यावरण चर (environment variables) लोड करते हैं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- फिर, OpenAI API के लिए endpoint, key, version और type सेट करते हैं।

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

  ऊपर दिया गया कोड एक JSON ऑब्जेक्ट रिटर्न करता है जिसमें जनरेट की गई इमेज का URL होता है। हम इस URL का उपयोग करके इमेज डाउनलोड कर सकते हैं और फाइल में सेव कर सकते हैं।

- अंत में, हम इमेज खोलते हैं और इसे डिफ़ॉल्ट इमेज व्यूअर में दिखाते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### इमेज जनरेट करने वाले कोड का विस्तार से विवरण

आइए इमेज जनरेट करने वाले कोड को विस्तार से देखें:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, वह टेक्स्ट प्रॉम्प्ट है जिसका उपयोग इमेज बनाने के लिए किया जाता है। इस उदाहरण में, प्रॉम्प्ट है "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"।
- **size**, जनरेट की गई इमेज का आकार है। इस उदाहरण में, इमेज 1024x1024 पिक्सेल की है।
- **n**, जनरेट की जाने वाली इमेज की संख्या है। इस उदाहरण में, दो इमेज बनाई जा रही हैं।
- **temperature**, यह पैरामीटर जनरेटिव AI मॉडल के आउटपुट की यादृच्छिकता (randomness) को नियंत्रित करता है। तापमान 0 से 1 के बीच होता है, जहां 0 का मतलब है आउटपुट निश्चित (deterministic) और 1 का मतलब है आउटपुट यादृच्छिक (random)। डिफ़ॉल्ट मान 0.7 है।

इमेज के साथ आप और भी कई चीजें कर सकते हैं, जिन्हें हम अगले सेक्शन में कवर करेंगे।

## इमेज जनरेशन की अतिरिक्त क्षमताएं

अब तक आपने देखा कि हम कुछ पंक्तियों के Python कोड से इमेज कैसे बना सकते हैं। लेकिन इमेज के साथ आप और भी बहुत कुछ कर सकते हैं।

आप निम्नलिखित कर सकते हैं:

- **एडिट करें**। एक मौजूदा इमेज, मास्क और प्रॉम्प्ट प्रदान करके आप इमेज में बदलाव कर सकते हैं। उदाहरण के लिए, आप इमेज के एक हिस्से में कुछ जोड़ सकते हैं। कल्पना करें कि हमारे बनी की इमेज है, आप बनी को टोपी पहनाने के लिए इमेज, मास्क (जिसमें बदलाव के लिए क्षेत्र की पहचान हो) और टेक्स्ट प्रॉम्प्ट देंगे।

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

  मूल इमेज में केवल खरगोश होगा, लेकिन अंतिम इमेज में खरगोश के सिर पर टोपी होगी।

- **वैरिएशंस बनाएं**। इसका मतलब है कि आप एक मौजूदा इमेज लेते हैं और उससे वैरिएशंस बनवाते हैं। वैरिएशन बनाने के लिए, आप एक इमेज और टेक्स्ट प्रॉम्प्ट देते हैं, और कोड इस प्रकार होगा:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ध्यान दें, यह केवल OpenAI पर समर्थित है।

## तापमान (Temperature)

तापमान एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की यादृच्छिकता को नियंत्रित करता है। तापमान 0 से 1 के बीच होता है, जहां 0 का मतलब है आउटपुट निश्चित और 1 का मतलब है आउटपुट यादृच्छिक। डिफ़ॉल्ट मान 0.7 है।

आइए देखें तापमान कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hi.png)

अब वही प्रॉम्प्ट फिर से चलाते हैं ताकि देखें कि हमें एक जैसी इमेज दो बार नहीं मिलेगी:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hi.png)

जैसा कि आप देख सकते हैं, इमेजें समान हैं, लेकिन बिल्कुल एक जैसी नहीं। अब तापमान मान को 0.1 करते हैं और देखते हैं क्या होता है:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलना

तो चलिए प्रतिक्रिया को अधिक निश्चित बनाने की कोशिश करते हैं। हमने जो दो इमेज बनाईं, उनमें पहली में बनी है और दूसरी में घोड़ा, इसलिए इमेज काफी अलग हैं।

इसलिए, हम अपना कोड बदलकर तापमान को 0 कर देते हैं, इस तरह:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप यह कोड चलाएंगे, तो आपको ये दो इमेज मिलेंगी:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hi.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hi.png)

यहां आप स्पष्ट रूप से देख सकते हैं कि इमेजें एक-दूसरे से अधिक मिलती-जुलती हैं।

## मेटाप्रॉम्प्ट्स के साथ अपने एप्लिकेशन की सीमाएं कैसे निर्धारित करें

हमारे डेमो के साथ, हम पहले ही अपने क्लाइंट्स के लिए इमेज बना सकते हैं। लेकिन हमें अपने एप्लिकेशन के लिए कुछ सीमाएं बनानी होंगी।

उदाहरण के लिए, हम ऐसी इमेज नहीं बनाना चाहते जो कार्यस्थल के लिए सुरक्षित न हों, या जो बच्चों के लिए उपयुक्त न हों।

हम यह _मेटाप्रॉम्प्ट्स_ के साथ कर सकते हैं। मेटाप्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जो जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किए जाते हैं। उदाहरण के लिए, हम मेटाप्रॉम्प्ट्स का उपयोग आउटपुट को नियंत्रित करने के लिए कर सकते हैं, और सुनिश्चित कर सकते हैं कि जनरेट की गई इमेजें कार्यस्थल के लिए सुरक्षित हों या बच्चों के लिए उपयुक्त हों।

### यह कैसे काम करता है?

अब, मेटाप्रॉम्प्ट्स कैसे काम करते हैं?

मेटाप्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जो जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करते हैं, ये टेक्स्ट प्रॉम्प्ट से पहले रखे जाते हैं, और मॉडल के आउटपुट को नियंत्रित करने के लिए एप्लिकेशन में एम्बेड किए जाते हैं। प्रॉम्प्ट इनपुट और मेटाप्रॉम्प्ट इनपुट को एक ही टेक्स्ट प्रॉम्प्ट में समाहित किया जाता है।

मेटाप्रॉम्प्ट का एक उदाहरण इस प्रकार होगा:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, आइए देखें कि हम अपने डेमो में मेटाप्रॉम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

ऊपर दिए गए प्रॉम्प्ट से आप देख सकते हैं कि सभी बनाई जा रही इमेजें मेटाप्रॉम्प्ट को ध्यान में रखती हैं।

## असाइनमेंट - चलिए छात्रों को सक्षम बनाएं

हमने इस पाठ की शुरुआत में Edu4All का परिचय दिया था। अब समय है कि छात्रों को उनकी असाइनमेंट के लिए इमेज बनाने में सक्षम बनाएं।

छात्र अपनी असाइनमेंट के लिए स्मारकों की इमेज बनाएंगे, कि कौन से स्मारक होंगे यह पूरी तरह छात्रों पर निर्भर है। छात्रों से कहा गया है कि वे इस कार्य में अपनी रचनात्मकता का उपयोग करें और इन स्मारकों को विभिन्न संदर्भों में रखें।

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

prompt = f"""{meta_prompt}
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

इस पाठ को पूरा करने के बाद, हमारी [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) देखें ताकि आप अपनी जनरेटिव AI की जानकारी को और बढ़ा सकें!

अगले पाठ 10 पर जाएं, जहां हम देखेंगे कि [लो-कोड के साथ AI एप्लिकेशन कैसे बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।