<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:30:34+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "hi"
}
-->
# इमेज जनरेशन एप्लिकेशन बनाना

[![इमेज जनरेशन एप्लिकेशन बनाना](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.hi.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs सिर्फ टेक्स्ट जनरेशन तक सीमित नहीं हैं। आप टेक्स्ट डिस्क्रिप्शन से इमेज भी बना सकते हैं। इमेज एक मोडैलिटी के रूप में कई क्षेत्रों में बहुत उपयोगी हो सकती है, जैसे मेडटेक, आर्किटेक्चर, टूरिज्म, गेम डेवलपमेंट आदि। इस चैप्टर में हम दो सबसे लोकप्रिय इमेज जनरेशन मॉडल्स, DALL-E और Midjourney के बारे में जानेंगे।

## परिचय

इस पाठ में हम कवर करेंगे:

- इमेज जनरेशन और यह क्यों उपयोगी है।
- DALL-E और Midjourney, ये क्या हैं और कैसे काम करते हैं।
- इमेज जनरेशन ऐप कैसे बनाएं।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- एक इमेज जनरेशन एप्लिकेशन बनाना।
- अपने एप्लिकेशन के लिए मेटा प्रॉम्प्ट्स के साथ सीमाएं तय करना।
- DALL-E और Midjourney के साथ काम करना।

## इमेज जनरेशन एप्लिकेशन क्यों बनाएं?

इमेज जनरेशन एप्लिकेशन जनरेटिव AI की क्षमताओं को एक्सप्लोर करने का शानदार तरीका है। इन्हें कई तरह से इस्तेमाल किया जा सकता है, जैसे:

- **इमेज एडिटिंग और सिंथेसिस**। आप कई उपयोग के मामलों के लिए इमेज बना सकते हैं, जैसे इमेज एडिटिंग और इमेज सिंथेसिस।

- **कई इंडस्ट्रीज में लागू**। इन्हें मेडटेक, टूरिज्म, गेम डेवलपमेंट जैसी कई इंडस्ट्रीज के लिए इमेज जनरेट करने में भी इस्तेमाल किया जा सकता है।

## परिदृश्य: Edu4All

इस पाठ के हिस्से के रूप में, हम अपने स्टार्टअप Edu4All के साथ काम करना जारी रखेंगे। छात्र अपनी असाइनमेंट्स के लिए इमेज बनाएंगे, कौन सी इमेज बनानी है यह छात्रों पर निर्भर है, वे अपनी परियों की कहानी के लिए इलस्ट्रेशन बना सकते हैं, या अपनी कहानी के लिए नया कैरेक्टर बना सकते हैं, या अपने विचारों और कॉन्सेप्ट्स को विजुअलाइज़ कर सकते हैं।

उदाहरण के लिए, अगर Edu4All के छात्र क्लास में मॉन्यूमेंट्स पर काम कर रहे हैं, तो वे ऐसा कुछ बना सकते हैं:

![Edu4All स्टार्टअप, क्लास ऑन मॉन्यूमेंट्स, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.hi.png)

ऐसे प्रॉम्प्ट का उपयोग करके

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय इमेज जनरेशन मॉडल्स हैं, ये आपको प्रॉम्प्ट्स के जरिए इमेज जनरेट करने देते हैं।

### DALL-E

चलो DALL-E से शुरू करते हैं, यह एक जनरेटिव AI मॉडल है जो टेक्स्ट डिस्क्रिप्शन से इमेज बनाता है।

> [DALL-E दो मॉडल्स का कॉम्बिनेशन है, CLIP और diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो इमेज और टेक्स्ट से एम्बेडिंग्स बनाता है, जो डेटा का न्यूमेरिकल रिप्रेजेंटेशन होता है।

- **Diffused attention**, एक मॉडल है जो एम्बेडिंग्स से इमेज बनाता है। DALL-E को इमेज और टेक्स्ट के डेटासेट पर ट्रेन किया गया है और यह टेक्स्ट डिस्क्रिप्शन से इमेज जनरेट कर सकता है। उदाहरण के लिए, DALL-E से आप टोपी पहने बिल्ली या मोहॉक वाले कुत्ते की इमेज बना सकते हैं।

### Midjourney

Midjourney भी DALL-E की तरह ही काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से इमेज बनाता है। Midjourney से भी आप “a cat in a hat” या “dog with a mohawk” जैसे प्रॉम्प्ट्स से इमेज बना सकते हैं।

![Midjourney द्वारा जनरेटेड इमेज, मैकेनिकल कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_इमेज क्रेडिट: Wikipedia, इमेज Midjourney द्वारा जनरेट की गई_

## DALL-E और Midjourney कैसे काम करते हैं

सबसे पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफॉर्मर आर्किटेक्चर पर आधारित है और इसमें _autoregressive transformer_ होता है।

_autoregressive transformer_ यह तय करता है कि मॉडल टेक्स्ट डिस्क्रिप्शन से इमेज कैसे बनाता है, यह एक बार में एक पिक्सल जनरेट करता है, और फिर जनरेट किए गए पिक्सल्स का उपयोग अगले पिक्सल को बनाने के लिए करता है। यह न्यूरल नेटवर्क की कई लेयर्स से गुजरता है, जब तक इमेज पूरी नहीं हो जाती।

इस प्रक्रिया के साथ, DALL-E इमेज में एट्रिब्यूट्स, ऑब्जेक्ट्स, कैरेक्टरिस्टिक्स आदि को कंट्रोल करता है। हालांकि, DALL-E 2 और 3 में जनरेटेड इमेज पर और ज्यादा कंट्रोल है।

## अपनी पहली इमेज जनरेशन एप्लिकेशन बनाना

तो इमेज जनरेशन एप्लिकेशन बनाने के लिए आपको क्या चाहिए? आपको ये लाइब्रेरीज़ चाहिए:

- **python-dotenv**, इस लाइब्रेरी का उपयोग करना बहुत अच्छा रहेगा ताकि आप अपनी सीक्रेट्स को _.env_ फाइल में कोड से अलग रख सकें।
- **openai**, इस लाइब्रेरी से आप OpenAI API के साथ इंटरैक्ट करेंगे।
- **pillow**, Python में इमेज के साथ काम करने के लिए।
- **requests**, HTTP रिक्वेस्ट्स भेजने के लिए।

## Azure OpenAI मॉडल बनाएं और डिप्लॉय करें

अगर आपने अभी तक नहीं किया है, तो [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पेज पर दिए गए निर्देशों का पालन करें
Azure OpenAI रिसोर्स और मॉडल बनाने के लिए। मॉडल के रूप में DALL-E 3 चुनें।  

## ऐप बनाएं

1. _.env_ नाम की फाइल बनाएं और उसमें निम्नलिखित कंटेंट डालें:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   यह जानकारी Azure OpenAI Foundry Portal में अपने रिसोर्स के "Deployments" सेक्शन में देखें।

1. ऊपर दी गई लाइब्रेरीज़ को _requirements.txt_ नाम की फाइल में इस तरह लिखें:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. अब, वर्चुअल एनवायरनमेंट बनाएं और लाइब्रेरीज़ इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   विंडोज़ के लिए, वर्चुअल एनवायरनमेंट बनाने और एक्टिवेट करने के लिए ये कमांड्स इस्तेमाल करें:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नाम की फाइल में निम्नलिखित कोड डालें:

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

आइए इस कोड को समझते हैं:

- सबसे पहले, हम जिन लाइब्रेरीज़ की जरूरत है उन्हें इम्पोर्ट करते हैं, जिसमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी और Pillow लाइब्रेरी शामिल हैं।

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

- फिर, Azure OpenAI सर्विस क्लाइंट को कॉन्फ़िगर करते हैं 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- अब, हम इमेज जनरेट करते हैं:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ऊपर दिया गया कोड एक JSON ऑब्जेक्ट के साथ रिस्पॉन्ड करता है जिसमें जनरेटेड इमेज का URL होता है। हम इस URL का उपयोग करके इमेज डाउनलोड कर सकते हैं और फाइल में सेव कर सकते हैं।

- अंत में, हम इमेज खोलते हैं और स्टैंडर्ड इमेज व्यूअर से दिखाते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### इमेज जनरेट करने के बारे में और जानकारी

आइए उस कोड को विस्तार से देखें जो इमेज जनरेट करता है:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, वह टेक्स्ट प्रॉम्प्ट है जिससे इमेज जनरेट होती है। इस केस में, हम "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" प्रॉम्प्ट इस्तेमाल कर रहे हैं।
- **size**, जनरेटेड इमेज का साइज है। यहां हम 1024x1024 पिक्सल की इमेज बना रहे हैं।
- **n**, जनरेट होने वाली इमेज की संख्या है। यहां हम दो इमेज बना रहे हैं।
- **temperature**, यह पैरामीटर जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को कंट्रोल करता है। इसका मान 0 से 1 के बीच होता है, जहां 0 का मतलब आउटपुट डिटरमिनिस्टिक है और 1 का मतलब आउटपुट रैंडम है। डिफॉल्ट वैल्यू 0.7 है।

इमेज के साथ और भी बहुत कुछ किया जा सकता है, जिसे हम अगले सेक्शन में देखेंगे।

## इमेज जनरेशन की अतिरिक्त क्षमताएं

अब तक आपने देखा कि कैसे कुछ लाइनों के कोड से Python में इमेज जनरेट की जा सकती है। लेकिन इमेज के साथ और भी बहुत कुछ किया जा सकता है।

आप ये भी कर सकते हैं:

- **एडिट्स करें**। किसी मौजूदा इमेज, एक मास्क और एक प्रॉम्प्ट देकर आप इमेज को बदल सकते हैं। उदाहरण के लिए, आप इमेज के किसी हिस्से में कुछ जोड़ सकते हैं। जैसे हमारे bunny इमेज में, आप bunny को टोपी पहना सकते हैं। इसके लिए आपको इमेज, मास्क (जिस हिस्से में बदलाव करना है) और टेक्स्ट प्रॉम्प्ट देना होगा कि क्या बदलाव करना है।
> ध्यान दें: यह DALL-E 3 में सपोर्टेड नहीं है। 
 
यहां GPT Image का उदाहरण है:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  बेस इमेज में सिर्फ लाउंज और पूल होगा, लेकिन फाइनल इमेज में फ्लेमिंगो भी होगा:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **वेरिएशन्स बनाएं**। इसका मतलब है कि आप किसी मौजूदा इमेज से अलग-अलग वेरिएशन्स बनवा सकते हैं। वेरिएशन बनाने के लिए आप इमेज और टेक्स्ट प्रॉम्प्ट देते हैं और ऐसा कोड लिखते हैं:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ध्यान दें, यह सिर्फ OpenAI पर सपोर्टेड है

## टेम्परेचर

टेम्परेचर एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की रैंडमनेस को कंट्रोल करता है। इसका मान 0 से 1 के बीच होता है, जहां 0 का मतलब आउटपुट डिटरमिनिस्टिक है और 1 का मतलब आउटपुट रैंडम है। डिफॉल्ट वैल्यू 0.7 है।

आइए एक उदाहरण देखें कि टेम्परेचर कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.hi.png)

अब वही प्रॉम्प्ट फिर से चलाएं, देखेंगे कि दोनों बार एक जैसी इमेज नहीं मिलेगी:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.hi.png)

जैसा कि आप देख सकते हैं, इमेज मिलती-जुलती हैं, लेकिन एक जैसी नहीं हैं। अब टेम्परेचर वैल्यू को 0.1 पर सेट करके देखें:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### टेम्परेचर बदलना

अब चलो रिस्पॉन्स को और डिटरमिनिस्टिक बनाते हैं। हमने जो दो इमेज जनरेट कीं उनमें पहली में bunny है और दूसरी में horse है, तो इमेज काफी अलग हैं।

इसलिए, चलो कोड बदलते हैं और टेम्परेचर को 0 पर सेट करते हैं:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप यह कोड चलाएंगे, तो ये दो इमेज मिलेंगी:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.hi.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.hi.png)

यहां आप साफ देख सकते हैं कि दोनों इमेज एक-दूसरे से काफी मिलती हैं।

## अपने एप्लिकेशन के लिए सीमाएं कैसे तय करें मेटाप्रॉम्प्ट्स के साथ

हमारे डेमो के साथ, हम अपने क्लाइंट्स के लिए इमेज जनरेट कर सकते हैं। लेकिन हमें अपने एप्लिकेशन के लिए कुछ सीमाएं तय करनी होंगी।

उदाहरण के लिए, हम ऐसी इमेज नहीं बनाना चाहते जो वर्क के लिए सुरक्षित न हों, या बच्चों के लिए उपयुक्त न हों।

हम यह _मेटाप्रॉम्प्ट्स_ के जरिए कर सकते हैं। मेटाप्रॉम्प्ट्स ऐसे टेक्स्ट प्रॉम्प्ट्स होते हैं जिनसे जनरेटिव AI मॉडल के आउटपुट को कंट्रोल किया जाता है। उदाहरण के लिए, हम मेटाप्रॉम्प्ट्स का उपयोग आउटपुट को कंट्रोल करने के लिए कर सकते हैं, और सुनिश्चित कर सकते हैं कि जनरेटेड इमेज वर्क के लिए सुरक्षित हों या बच्चों के लिए उपयुक्त हों।

### यह कैसे काम करता है?

तो, मेटाप्रॉम्प्ट्स कैसे काम करते हैं?

मेटाप्रॉम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जिनसे जनरेटिव AI मॉडल के आउटपुट को कंट्रोल किया जाता है, ये टेक्स्ट प्रॉम्प्ट से पहले लगाए जाते हैं, और मॉडल के आउटपुट को कंट्रोल करने के लिए एप्लिकेशन में एम्बेड किए जाते हैं। प्रॉम्प्ट इनपुट और मेटाप्रॉम्प्ट इनपुट को एक ही टेक्स्ट प्रॉम्प्ट में जोड़ दिया जाता है।

मेटाप्रॉम्प्ट का एक उदाहरण इस तरह हो सकता है:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, चलो देखते हैं कि हम अपने डेमो में मेटाप्रॉम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

ऊपर दिए गए प्रॉम्प्ट से आप देख सकते हैं कि सभी इमेज बनाते समय मेटाप्रॉम्प्ट को ध्यान में रखा गया है।

## असाइनमेंट - चलो छात्रों को सक्षम बनाएं

हमने इस पाठ की शुरुआत में Edu4All का परिचय दिया था। अब समय है कि छात्रों को अपनी असाइनमेंट्स के लिए इमेज जनरेट करने में सक्षम बनाएं।

छात्र अपनी असाइनमेंट्स के लिए मॉन्यूमेंट्स वाली इमेज बनाएंगे, कौन से मॉन्यूमेंट्स होंगे यह छात्रों पर निर्भर है। छात्रों को इस टास्क में अपनी क्रिएटिविटी का इस्तेमाल करने के लिए कहा गया है ताकि वे इन मॉन्यूमेंट्स को अलग-अलग संदर्भों में रख सकें।

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
इस पाठ को पूरा करने के बाद, हमारे [जनरेटिव एआई लर्निंग संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपनी जनरेटिव एआई की जानकारी को और बेहतर बना सकें!

अब पाठ 10 पर जाएँ जहाँ हम देखेंगे कि [लो-कोड के साथ एआई एप्लिकेशन कैसे बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।