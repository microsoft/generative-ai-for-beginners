# छवि उत्पादन अनुप्रयोग बनाना

[![छवि उत्पादन अनुप्रयोग बनाना](../../../translated_images/hi/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs केवल टेक्स्ट उत्पादन से अधिक हैं। टेक्स्ट विवरण से छवियाँ उत्पन्न करना भी संभव है। छवियाँ एक प्रकार के रूप में कई क्षेत्रों में उपयोगी हो सकती हैं जैसे MedTech, वास्तुकला, पर्यटन, गेम विकास और अधिक। इस अध्याय में, हम दो सबसे लोकप्रिय छवि उत्पादन मॉडलों, DALL-E और Midjourney पर चर्चा करेंगे।

## परिचय

इस पाठ में, हम निम्नलिखित विषयों को कवर करेंगे:

- छवि उत्पादन और इसके उपयोगिता के बारे में।
- DALL-E और Midjourney क्या हैं और ये कैसे काम करते हैं।
- आप एक छवि उत्पादन अनुप्रयोग कैसे बनाएंगे।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप सक्षम होंगे:

- एक छवि उत्पादन अनुप्रयोग बनाना।
- अपने अनुप्रयोग की सीमाएँ मेटा प्रॉम्प्ट्स के साथ परिभाषित करना।
- DALL-E और Midjourney के साथ काम करना।

## एक छवि उत्पादन अनुप्रयोग क्यों बनाएं?

छवि उत्पादन अनुप्रयोग जनरेटिव AI की क्षमताओं का अन्वेषण करने का एक शानदार तरीका हैं। इन्हें, उदाहरण के लिए, निम्नलिखित के लिए उपयोग किया जा सकता है:

- **छवि संपादन और संश्लेषण**। आप कई उपयोग मामलों के लिए छवियाँ उत्पन्न कर सकते हैं, जैसे छवि संपादन और छवि संश्लेषण।

- **विभिन्न उद्योगों में लागू**। इन्हें Medtech, पर्यटन, गेम विकास और अधिक जैसे विभिन्न उद्योगों के लिए छवियाँ उत्पन्न करने के लिए भी उपयोग किया जा सकता है।

## परिदृश्य: Edu4All

इस पाठ के भाग के रूप में, हम अपने स्टार्टअप, Edu4All के साथ काम जारी रखेंगे। छात्र अपनी आकलनों के लिए छवियाँ बनाएंगे, वे छवियाँ क्या होंगी यह छात्रों पर निर्भर है, लेकिन वे अपनी कहानी के लिए चित्र हो सकते हैं या कोई नया पात्र बना सकते हैं या अपने आइडिया और अवधारणाओं का दृश्य रूप बना सकते हैं।

उदाहरण के लिए, यदि वे कक्षा में स्मारकों पर काम कर रहे हैं तो Edu4All के छात्र इस तरह की छवियाँ उत्पन्न कर सकते हैं:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/hi/startup.94d6b79cc4bb3f5a.webp)

इस तरह के प्रॉम्प्ट का उपयोग कर के

> "सुबह की जल्दी धूप में एफिल टॉवर के बगल में कुत्ता"

## DALL-E और Midjourney क्या हैं?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) और [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दो सबसे लोकप्रिय छवि उत्पादन मॉडल हैं, ये आपको प्रॉम्प्ट्स का उपयोग करके छवियाँ उत्पन्न करने की अनुमति देते हैं।

### DALL-E

चलिए DALL-E से शुरू करते हैं, जो एक जनरेटिव AI मॉडल है जो टेक्स्ट विवरण से छवियाँ उत्पन्न करता है।

> [DALL-E दो मॉडलों, CLIP और Diffused Attention, का संयोजन है](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मॉडल है जो छवियों और टेक्स्ट से डेटा के संख्या रूपों में प्रतिनिधित्व (एम्बेडिंग) उत्पन्न करता है।

- **Diffused Attention**, एक मॉडल है जो एम्बेडिंग से छवियाँ उत्पन्न करता है। DALL-E एक छवि और टेक्स्ट डेटासेट पर प्रशिक्षित है और टेक्स्ट विवरण से छवि उत्पन्न करने के लिए उपयोग किया जा सकता है। उदाहरण के लिए, DALL-E एक टोपी पहने हुए बिल्ली या मोहॉक वाले कुत्ते की छवियाँ उत्पन्न कर सकता है।

### Midjourney

Midjourney DALL-E की तरह ही काम करता है, यह टेक्स्ट प्रॉम्प्ट्स से तस्वीरें उत्पन्न करता है। Midjourney का उपयोग “टोपी पहने बिल्ली” या “मोहॉक वाला कुत्ता” जैसी प्रॉम्प्ट्स से चित्र बनाने के लिए किया जा सकता है।

![Midjourney द्वारा उत्पन्न छवि, मैकेनिकल कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_छवि क्रेडिट विकिपीडिया, Midjourney द्वारा उत्पन्न छवि_

## DALL-E और Midjourney कैसे काम करते हैं

सबसे पहले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जनरेटिव AI मॉडल है जो ट्रांसफॉर्मर आर्किटेक्चर पर आधारित है जिसमें _ऑटोरिग्रेसिव ट्रांसफॉर्मर_ होता है।

एक _ऑटोरिग्रेसिव ट्रांसफॉर्मर_ यह परिभाषित करता है कि मॉडल टेक्स्ट विवरण से चित्र कैसे उत्पन्न करता है, यह एक समय में एक पिक्सेल उत्पन्न करता है और फिर अगला पिक्सेल उत्पन्न करने के लिए पहले से उत्पन्न पिक्सेल्स का उपयोग करता है। यह नूरल नेटवर्क में कई लेयर्स से गुजरता है जब तक कि छवि पूरी नहीं हो जाती।

इस प्रक्रिया से, DALL-E छवि में विशेषताएँ, वस्तुएं, लक्षण आदि नियंत्रित करता है। हालांकि, DALL-E 2 और 3 में उत्पन्न छवि पर अधिक नियंत्रण है।

## अपना पहला छवि उत्पादन अनुप्रयोग बनाना

तो छवि उत्पादन अनुप्रयोग बनाने के लिए क्या चाहिए? आपको निम्नलिखित पुस्तकालयों की आवश्यकता होगी:

- **python-dotenv**, इस लाइब्रेरी का उपयोग करने की अत्यधिक सिफारिश की जाती है ताकि आपके रहस्य एक _.env_ फ़ाइल में कोड से दूर सुरक्षित रहें।
- **openai**, इस लाइब्रेरी का उपयोग आप OpenAI API के साथ इंटरैक्ट करने के लिए करेंगे।
- **pillow**, पायथन में छवियों के साथ काम करने के लिए।
- **requests**, HTTP अनुरोध करने में सहायता के लिए।

## एक Azure OpenAI मॉडल बनाएं और तैनात करें

यदि आपने पहले से नहीं किया है, तो [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) पृष्ठ पर दिए गए निर्देशों का पालन करें
और एक Azure OpenAI संसाधन और मॉडल बनाएं। मॉडल के रूप में **gpt-image-1** चुनें (वर्तमान पीढ़ी का Azure OpenAI छवि मॉडल; DALL-E 3 अब नया तैनाती के लिए उपलब्ध नहीं है)।

## ऐप बनाएं

1. एक _.env_ फ़ाइल बनाएं जिसमें निम्नलिखित सामग्री हो:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   अपने संसाधन के लिए Azure OpenAI Foundry पोर्टल के "डिप्लॉयमेंट्स" सेक्शन में यह जानकारी ढूंढें।

1. उपरोक्त लाइब्रेरीज़ को एक फ़ाइल _requirements.txt_ में इस प्रकार इकट्ठा करें:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. अगला, एक वर्चुअल एन्वायरनमेंट बनाएं और लाइब्रेरीज़ इंस्टॉल करें:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   विंडोज़ के लिए, वर्चुअल एन्वायरनमेंट बनाने और सक्रिय करने के लिए निम्न कमांड्स का उपयोग करें:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फ़ाइल में निम्न कोड जोड़ें:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # Azure OpenAI सेवा क्लाइंट कॉन्फ़िगर करें
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # इमेज जनरेशन API का उपयोग करके एक चित्र बनाएं
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # संग्रहीत छवि के लिए निर्देशिका सेट करें
        image_dir = os.path.join(os.curdir, 'images')

        # यदि निर्देशिका मौजूद नहीं है, तो इसे बनाएं
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # छवि पथ प्रारंभ करें (ध्यान दें कि फ़ाइल प्रकार png होना चाहिए)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # उत्पन्न छवि प्राप्त करें
        image_url = generation_response.data[0].url  # प्रतिक्रिया से छवि URL निकालें
        generated_image = requests.get(image_url).content  # छवि डाउनलोड करें
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # डिफ़ॉल्ट छवि दर्शक में छवि प्रदर्शित करें
        image = Image.open(image_path)
        image.show()

    # अपवाद पकड़ें
    except openai.BadRequestError as err:
        print(err)
   ```

आइए इस कोड को समझें:

- पहले, हम आवश्यक लाइब्रेरीज़ आयात करते हैं, जिनमें OpenAI लाइब्रेरी, dotenv लाइब्रेरी, requests लाइब्रेरी, और Pillow लाइब्रेरी शामिल हैं।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- उसके बाद, हम _.env_ फ़ाइल से पर्यावरण परिवर्तनीय लोड करते हैं।

  ```python
  # डॉटएनव आयात करें
  dotenv.load_dotenv()
  ```

- उसके बाद, हम Azure OpenAI सर्विस क्लाइंट को कॉन्फ़िगर करते हैं 

  ```python
  # एंडपॉइंट और कुंजी वातावरण चर से प्राप्त करें
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- अगले, हम छवि उत्पन्न करते हैं:

  ```python
  # इमेज जनरेशन API का उपयोग करके एक छवि बनाएं
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ऊपर दिया गया कोड एक JSON वस्तु के साथ उत्तर देता है जिसमें उत्पन्न छवि का URL शामिल होता है। हम इस URL का उपयोग करके छवि डाउनलोड कर सकते हैं और फ़ाइल में सहेज सकते हैं।

- अंत में, हम छवि को खोलते हैं और इसे प्रदर्शित करने के लिए सामान्य इमेज व्यूअर का उपयोग करते हैं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### छवि उत्पन्न करने के बारे में और विवरण

आइए उस कोड को विस्तार से देखें जो छवि उत्पन्न करता है:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, वह टेक्स्ट प्रॉम्प्ट है जिसका उपयोग छवि उत्पन्न करने के लिए किया जाता है। इस मामले में, हम प्रॉम्प्ट "खरगोश घोड़े पर, लॉलीपॉप पकड़े हुए, धुंधले मैदान में जहां डैफोडिल्स उगते हैं" का उपयोग कर रहे हैं।
- **size**, उत्पन्न छवि का आकार है। इस मामले में, हम 1024x1024 पिक्सेल की छवि उत्पन्न कर रहे हैं।
- **n**, उत्पन्न होने वाली छवियों की संख्या है। इस मामले में, हम दो छवियाँ उत्पन्न कर रहे हैं।
- **temperature**, यह जनरेटिव AI मॉडल के आउटपुट की यादृच्छिकता नियंत्रित करने वाला पैरामीटर है। तापमान 0 से 1 के बीच एक मान है, जहाँ 0 मतलब आउटपुट निश्चित है और 1 मतलब आउटपुट यादृच्छिक है। डिफ़ॉल्ट मान 0.7 है।

आप छवियों के साथ और भी चीजें कर सकते हैं जिन्हें हम अगले अनुभाग में कवर करेंगे।

## छवि उत्पादन की अतिरिक्त क्षमताएँ

अब तक आपने देखा कि हमने पायथन में कुछ पंक्तियों का उपयोग करके छवि उत्पन्न करना कैसे संभव बनाया। लेकिन आप छवियों के साथ और भी काम कर सकते हैं।

आप निम्नलिखित भी कर सकते हैं:

- **संपादन करें**। कोई मौजूदा छवि, मास्क और प्रॉम्प्ट प्रदान करके, आप छवि में बदलाव कर सकते हैं। उदाहरण के लिए, आप एक छवि के किसी हिस्से में कुछ जोड़ सकते हैं। मान लीजिए कि हमारी खरगोश छवि को देखें, आप खरगोश को टोपियां पहनाने के लिए ऐसा कर सकते हैं। आप यह कैसे करेंगे? आप छवि, मास्क (उस क्षेत्र के हिस्से की पहचान जो बदलना है) और टेक्स्ट प्रॉम्प्ट देते हैं जो बताते हैं कि क्या बदलाव करना है। 
> नोट: यह DALL-E 3 में समर्थित नहीं है। 
 
यहाँ GPT Image का एक उदाहरण है:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  मूल छवि में केवल पूल के साथ लाउंज होता है लेकिन अंतिम छवि में एक फ़्लेमिंगो शामिल होगा:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/hi/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hi/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hi/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **विविधताएँ बनाएं**। विचार यह है कि आप एक मौजूदा छवि लेते हैं और उससे विविधताएँ बनाने के लिए कहते हैं। विविधता बनाने के लिए, आप एक छवि और टेक्स्ट प्रॉम्प्ट प्रदान करते हैं और इस प्रकार कोड लिखते हैं:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > नोट, यह केवल OpenAI के DALL-E 2 मॉडल पर समर्थित है, gpt-image-1 पर नहीं।

## तापमान (Temperature)

तापमान एक पैरामीटर है जो जनरेटिव AI मॉडल के आउटपुट की यादृच्छिकता को नियंत्रित करता है। तापमान 0 से 1 के बीच का मान है, जहाँ 0 मतलब आउटपुट निश्चित (डिटर्मिनिस्टिक) है और 1 मतलब आउटपुट यादृच्छिक है। डिफ़ॉल्ट मान 0.7 है।

चलिए देखते हैं कि तापमान कैसे काम करता है, इस प्रॉम्प्ट को दो बार चलाकर:

> प्रॉम्प्ट: "खरगोश घोड़े पर, लॉलीपॉप पकड़े हुए, धुंधले मैदान में जहां डैफोडिल्स उगते हैं"

![घोड़े पर लॉलीपॉप पकड़े खरगोश, संस्करण 1](../../../translated_images/hi/v1-generated-image.a295cfcffa3c13c2.webp)

अब चलिए उसी प्रॉम्प्ट को फिर से चलाएं ताकि देखें कि हमें दो बार एक ही छवि नहीं मिलेगी:

![घोड़े पर खरगोश की उत्पन्न छवि](../../../translated_images/hi/v2-generated-image.33f55a3714efe61d.webp)

जैसा कि आप देख सकते हैं, छवियाँ समान हैं, लेकिन एक जैसी नहीं हैं। चलिए तापमान मान को 0.1 पर बदलकर देखते हैं कि क्या होता है:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # अपना प्रम्प्ट टेक्स्ट यहाँ दर्ज करें
        size='1024x1024',
        n=2
    )
```

### तापमान बदलना

तो चलिए प्रतिक्रिया को अधिक निश्चित बनाने की कोशिश करते हैं। हमने जिन दो छवियों को उत्पन्न किया, उनमें पहला खरगोश था और दूसरा घोड़ा था, इसलिए छवियाँ काफी भिन्न थीं।

इसलिए चलिए अपना कोड बदलते हैं और तापमान 0 सेट करते हैं, इस प्रकार:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # अपना प्रॉम्प्ट टेक्स्ट यहाँ दर्ज करें
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब आप यह कोड चलाते हैं, तो आपको ये दो छवियाँ मिलती हैं:

- ![तापमान 0, संस्करण 1](../../../translated_images/hi/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![तापमान 0, संस्करण 2](../../../translated_images/hi/v2-temp-generated-image.871d0c920dbfb0f1.webp)

यहाँ आप स्पष्ट रूप से देख सकते हैं कि छवियाँ एक-दूसरे से अधिक मिलती-जुलती हैं।

## मेटाप्रोम्प्ट के साथ अपने अनुप्रयोग के लिए सीमाएँ कैसे परिभाषित करें

हमारे डेमो के साथ, हम पहले से ही अपने क्लाइंट्स के लिए छवियाँ उत्पन्न कर सकते हैं। हालांकि, हमें अपने अनुप्रयोग के लिए कुछ सीमाएँ बनानी होंगी।

उदाहरण के लिए, हम ऐसी छवियाँ उत्पन्न नहीं करना चाहते जो कार्य स्थल के लिए सुरक्षित न हों, या जो बच्चों के लिए उपयुक्त न हों।

हम यह _मेटाप्रोम्प्ट्स_ के साथ कर सकते हैं। मेटाप्रोम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जिनका उपयोग जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए किया जाता है। उदाहरण के लिए, हम मेटाप्रोम्प्ट्स का उपयोग आउटपुट को नियंत्रित करने और सुनिश्चित करने के लिए कर सकते हैं कि उत्पन्न छवियाँ कार्यस्थल के लिए सुरक्षित और बच्चों के लिए उपयुक्त हों।

### यह कैसे काम करता है?

मेटाप्रोम्प्ट्स कैसे काम करते हैं?

मेटाप्रोम्प्ट्स टेक्स्ट प्रॉम्प्ट्स होते हैं जिन्हें जनरेटिव AI मॉडल के आउटपुट को नियंत्रित करने के लिए उपयोग किया जाता है, ये टेक्स्ट प्रॉम्प्ट से पहले स्थित होते हैं, और मॉडल के आउटपुट को नियंत्रित करने के लिए एप्लिकेशन में अंतर्निहित होते हैं। प्रॉम्प्ट इनपुट और मेटा प्रॉम्प्ट इनपुट को एक ही टेक्स्ट प्रॉम्प्ट में कैप्सुलेट किया जाता है।

मेटा प्रॉम्प्ट का एक उदाहरण इस प्रकार होगा:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, देखें कि हम अपने डेमो में मेटाप्रोम्प्ट्स का उपयोग कैसे कर सकते हैं।

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

# TODO छवि उत्पन्न करने के लिए अनुरोध जोड़ें
```

ऊपर दिए गए प्रॉम्प्ट से, आप देख सकते हैं कि बनाई गई सभी छवियाँ मेटाप्रोम्प्ट को ध्यान में रखती हैं।

## असाइनमेंट - चलिए छात्रों को सक्षम बनाएं

हमने इस पाठ की शुरुआत में Edu4All को प्रस्तुत किया था। अब समय है कि हम छात्रों को उनकी आकलनों के लिए छवियाँ उत्पन्न करने के लिए सक्षम बनाएं।


छात्र अपने आकलनों के लिए स्मारकों की छवियां बनाएंगे, स्मारक ठीक कौन से होंगे यह छात्रों पर निर्भर है। छात्रों से कहा गया है कि वे इस कार्य में अपनी रचनात्मकता का उपयोग करके इन स्मारकों को विभिन्न संदर्भों में रखें।

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

# पर्यावरण चर से एंडपॉइंट और कुंजी प्राप्त करें
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # इमेज जनरेशन एपीआई का उपयोग करके एक छवि बनाएं
    generation_response = client.images.generate(
        prompt=prompt,    # अपना प्रॉम्प्ट टेक्स्ट यहाँ दर्ज करें
        size='1024x1024',
        n=1,
    )
    # संग्रहित छवि के लिए निर्देशिका सेट करें
    image_dir = os.path.join(os.curdir, 'images')

    # यदि निर्देशिका मौजूद नहीं है, तो इसे बनाएं
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # छवि पथ आरंभ करें (ध्यान दें कि फाइल प्रकार png होना चाहिए)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # उत्पन्न छवि पुनः प्राप्त करें
    image_url = generation_response.data[0].url  # प्रतिक्रिया से छवि URL निकालें
    generated_image = requests.get(image_url).content  # छवि डाउनलोड करें
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # डिफ़ॉल्ट छवि दर्शक में छवि प्रदर्शित करें
    image = Image.open(image_path)
    image.show()

# अपवाद पकड़ें
except openai.BadRequestError as err:
    print(err)
```

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारा [जनरेटिव AI लर्निंग कलेक्शन](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) देखें जिससे आप जनरेटिव AI ज्ञान को और बढ़ा सकें!

पाठ 10 में जाएं जहां हम देखेंगे कि [लो-कोड के साथ AI एप्लिकेशन कैसे बनाएं](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->