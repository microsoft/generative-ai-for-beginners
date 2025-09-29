<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:34:39+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hi"
}
-->
# इमेज जनरेशन एप्लिकेशन बनाना

[![इमेज जनरेशन एप्लिकेशन बनाना](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hi.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs केवल टेक्स्ट जनरेशन तक ही सीमित नहीं हैं। टेक्स्ट विवरणों से इमेज बनाना भी संभव है। इमेज को एक माध्यम के रूप में उपयोग करना कई क्षेत्रों में अत्यधिक उपयोगी हो सकता है, जैसे मेडटेक, आर्किटेक्चर, पर्यटन, गेम डेवलपमेंट और अन्य। इस अध्याय में, हम दो सबसे लोकप्रिय इमेज जनरेशन मॉडल, DALL-E और Midjourney के बारे में जानेंगे।

## परिचय

इस पाठ में, हम निम्नलिखित विषयों को कवर करेंगे:

- इमेज जनरेशन और इसका महत्व।
- DALL-E और Midjourney, ये क्या हैं और कैसे काम करते हैं।
- इमेज जनरेशन ऐप कैसे बनाया जाए।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप:

- एक इमेज जनरेशन एप्लिकेशन बना सकेंगे।
- अपने एप्लिकेशन के लिए मेटा प्रॉम्प्ट्स के साथ सीमाएं परिभाषित कर सकेंगे।
- DALL-E और Midjourney के साथ काम कर सकेंगे।

## इमेज जनरेशन एप्लिकेशन क्यों बनाएं?

इमेज जनरेशन एप्लिकेशन जनरेटिव AI की क्षमताओं का पता लगाने का एक शानदार तरीका है। इन्हें निम्नलिखित उद्देश्यों के लिए उपयोग किया जा सकता है:

- **इमेज एडिटिंग और सिंथेसिस**। आप विभिन्न उपयोग मामलों के लिए इमेज बना सकते हैं, जैसे इमेज एडिटिंग और इमेज सिंथेसिस।

- **विभिन्न उद्योगों में लागू**। इन्हें मेडटेक, पर्यटन, गेम डेवलपमेंट और अन्य जैसे विभिन्न उद्योगों के लिए इमेज बनाने के लिए भी उपयोग किया जा सकता है।

## परिदृश्य: Edu4All

इस पाठ के हिस्से के रूप में, हम अपने स्टार्टअप, Edu4All के साथ काम करना जारी रखेंगे। छात्र अपनी असाइनमेंट्स के लिए इमेज बनाएंगे। ये इमेज क्या होंगी, यह छात्रों पर निर्भर है, लेकिन वे अपनी खुद की परीकथा के लिए चित्र बना सकते हैं, अपनी कहानी के लिए एक नया पात्र बना सकते हैं, या अपने विचारों और अवधारणाओं को विज़ुअलाइज़ करने में मदद कर सकते हैं।

उदाहरण के लिए, यदि Edu4All के छात्र कक्षा में स्मारकों पर काम कर रहे हैं, तो वे निम्नलिखित इमेज बना सकते हैं:

![Edu4All स्टार्टअप, स्मारकों पर कक्षा, एफिल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hi.png)

एक प्रॉम्प्ट का उपयोग करते हुए जैसे:

> "सुबह की धूप में एफिल टॉवर के पास कुत्ता"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय इमेज जनरेशन मॉडल हैं, जो आपको प्रॉम्प्ट्स का उपयोग करके इमेज बनाने की अनुमति देते हैं।

### DALL-E

चलो DALL-E से शुरू करते हैं, जो एक जनरेटिव AI मॉडल है जो टेक्स्ट विवरणों से इमेज बनाता है।

> [DALL-E दो मॉडलों, CLIP और डिफ्यूज्ड अटेंशन का संयोजन है](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो इमेज और टेक्स्ट से एम्बेडिंग्स (डेटा के संख्यात्मक प्रतिनिधित्व) बनाता है।

- **डिफ्यूज्ड अटेंशन**, एक मॉडल है जो एम्बेडिंग्स से इमेज बनाता है। DALL-E को इमेज और टेक्स्ट के डेटासेट पर प्रशिक्षित किया गया है और इसे टेक्स्ट विवरणों से इमेज बनाने के लिए उपयोग किया जा सकता है। उदाहरण के लिए, DALL-E का उपयोग टोपी में बिल्ली या मोहॉक वाले कुत्ते की इमेज बनाने के लिए किया जा सकता है।

### Midjourney

Midjourney DALL-E के समान तरीके से काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से इमेज बनाता है। Midjourney का उपयोग "टोपी में बिल्ली" या "मोहॉक वाले कुत्ते" जैसे प्रॉम्प्ट्स का उपयोग करके इमेज बनाने के लिए भी किया जा सकता है।

![Midjourney द्वारा बनाई गई इमेज, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_चित्र स्रोत: विकिपीडिया, Midjourney द्वारा बनाई गई इमेज_

## DALL-E और Midjourney कैसे काम करते हैं

पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफॉर्मर आर्किटेक्चर पर आधारित है और इसमें _ऑटोरेग्रेसिव ट्रांसफॉर्मर_ है।

एक _ऑटोरेग्रेसिव ट्रांसफॉर्मर_ परिभाषित करता है कि मॉडल टेक्स्ट विवरणों से इमेज कैसे बनाता है। यह एक समय में एक पिक्सल बनाता है और फिर बनाए गए पिक्सल का उपयोग अगले पिक्सल को बनाने के लिए करता है। यह प्रक्रिया तब तक चलती है जब तक इमेज पूरी नहीं हो जाती।

इस प्रक्रिया के साथ, DALL-E इमेज में बनाए गए गुण, वस्तुएं, विशेषताएं और अन्य चीजों को नियंत्रित करता है। हालांकि, DALL-E 2 और 3 में बनाई गई इमेज पर अधिक नियंत्रण होता है।

## अपनी पहली इमेज जनरेशन एप्लिकेशन बनाना

तो इमेज जनरेशन एप्लिकेशन बनाने के लिए आपको क्या चाहिए? आपको निम्नलिखित लाइब्रेरीज़ की आवश्यकता होगी:

- **python-dotenv**, यह लाइब्रेरी आपके सीक्रेट्स को कोड से दूर _.env_ फाइल में रखने के लिए अत्यधिक अनुशंसित है।
- **openai**, यह लाइब्रेरी OpenAI API के साथ इंटरैक्ट करने के लिए उपयोग की जाती है।
- **pillow**, Python में इमेज के साथ काम करने के लिए।
- **requests**, HTTP अनुरोध करने में मदद करने के लिए।

## Azure OpenAI मॉडल बनाएं और डिप्लॉय करें

यदि पहले से नहीं किया गया है, तो [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पेज पर दिए गए निर्देशों का पालन करें
Azure OpenAI संसाधन और मॉडल बनाने के लिए। मॉडल के रूप में DALL-E 3 का चयन करें।  

## ऐप बनाएं

1. एक फाइल _.env_ बनाएं जिसमें निम्नलिखित सामग्री हो:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Azure OpenAI Foundry Portal में अपने संसाधन के "Deployments" सेक्शन में इस जानकारी को ढूंढें।

1. ऊपर दी गई लाइब्रेरीज़ को _requirements.txt_ नामक फाइल में इकट्ठा करें, जैसे:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. इसके बाद, वर्चुअल एनवायरनमेंट बनाएं और लाइब्रेरीज़ इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows के लिए, वर्चुअल एनवायरनमेंट बनाने और सक्रिय करने के लिए निम्नलिखित कमांड का उपयोग करें:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फाइल में निम्नलिखित कोड जोड़ें:

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

इस कोड को समझते हैं:

- सबसे पहले, हम उन लाइब्रेरीज़ को इम्पोर्ट करते हैं जिनकी हमें आवश्यकता है, जिसमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी और Pillow लाइब्रेरी शामिल हैं।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- इसके बाद, हम _.env_ फाइल से एनवायरनमेंट वेरिएबल्स लोड करते हैं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- फिर, हम Azure OpenAI सेवा क्लाइंट को कॉन्फ़िगर करते हैं।

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- इसके बाद, हम इमेज जनरेट करते हैं:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ऊपर दिया गया कोड एक JSON ऑब्जेक्ट के साथ प्रतिक्रिया करता है जिसमें जनरेट की गई इमेज का URL होता है। हम इस URL का उपयोग इमेज डाउनलोड करने और इसे फाइल में सेव करने के लिए कर सकते हैं।

- अंत में, हम इमेज को खोलते हैं और इसे मानक इमेज व्यूअर का उपयोग करके प्रदर्शित करते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### इमेज जनरेट करने पर अधिक विवरण

आइए उस कोड को देखें जो इमेज जनरेट करता है:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, वह टेक्स्ट प्रॉम्प्ट है जिसका उपयोग इमेज जनरेट करने के लिए किया जाता है। इस मामले में, हम "घोड़े पर खरगोश, लॉलीपॉप पकड़े हुए, कोहरे वाले घास के मैदान में जहां डैफोडिल्स उगते हैं" प्रॉम्प्ट का उपयोग कर रहे हैं।
- **size**, वह आकार है जो जनरेट की गई इमेज का होता है। इस मामले में, हम 1024x1024 पिक्सल की इमेज जनरेट कर रहे हैं।
- **n**, वह संख्या है जो जनरेट की गई इमेज की होती है। इस मामले में, हम दो इमेज जनरेट कर रहे हैं।
- **temperature**, एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। टेम्परेचर 0 और 1 के बीच का मान होता है, जहां 0 का मतलब है कि आउटपुट निश्चित है और 1 का मतलब है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

इमेज के साथ और भी चीजें की जा सकती हैं, जिन्हें हम अगले सेक्शन में कवर करेंगे।

## इमेज जनरेशन की अतिरिक्त क्षमताएं

अब तक आपने देखा कि हम कुछ लाइनों के कोड का उपयोग करके इमेज जनरेट कर सकते हैं। हालांकि, इमेज के साथ और भी चीजें की जा सकती हैं।

आप निम्नलिखित भी कर सकते हैं:

- **एडिट्स करें**। एक मौजूदा इमेज, मास्क और प्रॉम्प्ट प्रदान करके, आप इमेज को बदल सकते हैं। उदाहरण के लिए, आप इमेज के किसी हिस्से में कुछ जोड़ सकते हैं। कल्पना करें कि हमारे खरगोश की इमेज में, आप खरगोश को टोपी पहना सकते हैं। ऐसा करने के लिए, आपको इमेज, मास्क (जिस हिस्से में बदलाव करना है उसे पहचानने के लिए) और टेक्स्ट प्रॉम्प्ट प्रदान करना होगा। 
> नोट: यह DALL-E 3 में समर्थित नहीं है। 
 
यहां GPT इमेज का उपयोग करते हुए एक उदाहरण है:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  बेस इमेज में केवल पूल के साथ लाउंज होगा, लेकिन अंतिम इमेज में फ्लेमिंगो होगा:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.hi.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.hi.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.hi.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **वेरिएशंस बनाएं**। विचार यह है कि आप एक मौजूदा इमेज लें और उससे वेरिएशंस बनाने के लिए कहें। वेरिएशन बनाने के लिए, आप एक इमेज और टेक्स्ट प्रॉम्प्ट प्रदान करते हैं और कोड इस प्रकार होता है:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यह केवल OpenAI पर समर्थित है।

## टेम्परेचर

टेम्परेचर एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को नियंत्रित करता है। टेम्परेचर 0 और 1 के बीच का मान होता है, जहां 0 का मतलब है कि आउटपुट निश्चित है और 1 का मतलब है कि आउटपुट रैंडम है। डिफ़ॉल्ट मान 0.7 है।

आइए देखें कि टेम्परेचर कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट: "घोड़े पर खरगोश, लॉलीपॉप पकड़े हुए, कोहरे वाले घास के मैदान में जहां डैफोडिल्स उगते हैं"

![घोड़े पर खरगोश, लॉलीपॉप पकड़े हुए, संस्करण 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hi.png)

अब उसी प्रॉम्प्ट को फिर से चलाते हैं ताकि देखें कि हमें एक ही इमेज दो बार नहीं मिलेगी:

![घोड़े पर खरगोश की जनरेट की गई इमेज](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hi.png)

जैसा कि आप देख सकते हैं, इमेज समान हैं, लेकिन बिल्कुल एक जैसी नहीं हैं। आइए टेम्परेचर मान को 0.1 पर बदलकर देखें कि क्या होता है:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### टेम्परेचर बदलना

तो चलिए प्रतिक्रिया को अधिक निश्चित बनाने की कोशिश करते हैं। हमने जो दो इमेज जनरेट की थीं, उनमें देखा कि पहली इमेज में खरगोश है और दूसरी इमेज में घोड़ा है, इसलिए इमेज काफी भिन्न हैं।

इसलिए, चलिए अपने कोड को बदलते हैं और टेम्परेचर को 0 पर सेट करते हैं, इस प्रकार:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप इस कोड को चलाते हैं, तो आपको ये दो इमेज मिलती हैं:

- ![टेम्परेचर 0, संस्करण 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hi.png)
- ![टेम्परेचर 0, संस्करण 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hi.png)

यहां आप स्पष्ट रूप से देख सकते हैं कि इमेज एक-दूसरे से अधिक मिलती-जुलती हैं।

## अपने एप्लिकेशन के लिए मेटा प्रॉम्प्ट्स के साथ सीमाएं कैसे परिभाषित करें

हमारे डेमो के साथ, हम पहले ही अपने क्लाइंट्स के लिए इमेज जनरेट कर सकते हैं। हालांकि, हमें अपने एप्लिकेशन के लिए कुछ सीमाएं बनानी होंगी।

उदाहरण के लिए, हम ऐसी इमेज जनरेट नहीं करना चाहते जो कार्यस्थल के लिए सुरक्षित न हों या बच्चों के लिए उपयुक्त न हों।

हम इसे _मेटा प्रॉम्प्ट्स_ के साथ कर सकते हैं। मेटा प्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जो जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किए जाते हैं। उदाहरण के लिए, हम मेटा प्रॉम्प्ट्स का उपयोग आउटपुट को नियंत्रित करने और यह सुनिश्चित करने के लिए कर सकते हैं कि जनरेट की गई इमेज कार्यस्थल के लिए सुरक्षित हों या बच्चों के लिए उपयुक्त हों।

### यह कैसे काम करता है?

अब, मेटा प्रॉम्प्ट्स कैसे काम करते हैं?

मेटा प्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जो जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किए जाते हैं। इन्हें टेक्स्ट प्रॉम्प्ट से पहले रखा जाता है और मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किया जाता है। इन्हें एप्लिकेशन में एम्बेड किया जाता है ताकि मॉडल के आउटपुट को नियंत्रित किया जा सके। प्रॉम्प्ट इनपुट और मेटा प्रॉम्प्ट इनपुट को एक ही टेक्स्ट प्रॉम्प्ट में समाहित किया जाता है।

मेटा प्रॉम्प्ट का एक उदाहरण निम्नलिखित होगा:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, चलिए देखते हैं कि हम अपने डेमो में मेटा प्रॉम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

ऊपर दिए गए प्रॉम्प्ट से, आप देख सकते हैं कि बनाई गई सभी इमेज मेटा प्रॉम्प्ट को ध्यान में रखती हैं।

## असाइनमेंट - चलिए छात्रों को सक्षम बनाते हैं

हमने इस पाठ की शुरुआत में Edu4All का परिचय दिया। अब समय है कि छात्रों को उनकी असाइनमेंट्स के लिए इमेज जनरेट करने में सक्षम बनाया जाए।

छात्र अपनी असाइनमेंट्स के लिए स्मारकों वाली इमेज बनाएंगे। कौन से स्मारक होंगे, यह छात्रों पर निर्भर है। छात्रों से इस कार्य में अपनी रचनात्मकता का उपयोग करने के लिए कहा गया है ताकि वे इन स्मारकों को विभिन्न संदर्भों में रख सकें।

## समाधान

यहां एक संभावित समाधान है:
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

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें और अपनी Generative AI की जानकारी को और बढ़ाएं!

पाठ 10 पर जाएं, जहां हम देखेंगे कि [कम-कोड के साथ AI एप्लिकेशन कैसे बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।