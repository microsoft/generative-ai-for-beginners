# इमेज जनरेशन अॅप्लिकेशन्स तयार करणे

[![इमेज जनरेशन अॅप्लिकेशन्स तयार करणे](../../../translated_images/mr/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM हे फक्त मजकूर तयार करण्यापुरते मर्यादित नाहीत. मजकूर वर्णनांमधून प्रतिमा तयार करणे देखील शक्य आहे. प्रतिमा ही एक माध्यम म्हणून अनेक क्षेत्रांमध्ये अत्यंत उपयुक्त ठरू शकते जसे की मेडटेक, आर्किटेक्चर, पर्यटन, गेम डेव्हलपमेंट आणि बरेच काही. या प्रकरणात, आपण दोन सर्वात लोकप्रिय प्रतिमा जनरेशन मॉडेल्स, DALL-E आणि Midjourney यांचा आढावा घेणार आहोत.

## परिचय

या धड्यात आपण पुढील बाबी पाहणार आहोत:

- इमेज जनरेशन आणि त्याचा उपयुक्तपणा.
- DALL-E आणि Midjourney म्हणजे काय आणि ते कसे कार्य करतात.
- तुम्ही कसे इमेज जनरेशन अॅप्लिकेशन तयार कराल.

## शिक्षण उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्हाला सक्षम व्हाल:

- प्रतिमा जनरेशन अॅप्लिकेशन तयार करणे.
- मेटा प्रॉम्प्टसह आपल्या अॅप्लिकेशनसाठी मर्यादा निश्चित करणे.
- DALL-E आणि Midjourney सह काम करणे.

## इमेज जनरेशन अॅप्लिकेशन का तयार करावे?

इमेज जनरेशन अॅप्लिकेशन्स हे जनरेटिव्ह AI च्या क्षमतांचा शोध घेण्यासाठी एक छान मार्ग आहे. त्यांचा वापर उदाहरणार्थ खालील गोष्टीसाठी करता येतो:

- **इमेज संपादन आणि संश्लेषण**. तुम्ही अनेक वापर प्रकरणांकरिता प्रतिमा तयार करू शकता, जसे की प्रतिमा संपादन आणि प्रतिमा संश्लेषण.

- **विविध उद्योगांमध्ये लागू**. ते मेडटेक, पर्यटन, गेम डेव्हलपमेंट आणि इतर उद्योगांसाठी प्रतिमा तयार करण्यासाठी देखील वापरले जाऊ शकतात.

## उदाहरण: Edu4All

या धड्याचा भाग म्हणून, आपण Edu4All नावाच्या स्टार्टअपने काम चालू ठेवणार आहोत. विद्यार्थी त्यांच्या मूल्यमापनांसाठी प्रतिमा तयार करतील, कोणत्या प्रकारच्या प्रतिमा तयार करायच्या आहेत हे विद्यार्थ्यांवर अवलंबून आहे, पण त्या त्यांच्या स्वतःच्या गोष्टींचे चित्रण किंवा त्यांच्या कथेतील नवीन पात्र तयार करणे किंवा त्यांच्या कल्पना आणि संकल्पना दृश्यरुप देण्यास मदत करू शकतात.

जर विद्यार्थी वर्गातील स्मारकांवर काम करत असतील तर Edu4All च्या विद्यार्थ्यांनी उदाहरणार्थ काय तयार करू शकतात हे पाहा:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/mr/startup.94d6b79cc4bb3f5a.webp)

वापरलेला प्रॉम्प्ट:

> "सकाळच्या सुर्यप्रकाशात एफिल टॉवरजवळ कुत्रा"

## DALL-E आणि Midjourney म्हणजे काय?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय प्रतिमा जनरेशन मॉडेल्स आहेत, जे तुम्हाला प्रॉम्प्ट वापरून प्रतिमा तयार करण्याची परवानगी देतात.

### DALL-E

चला DALL-E पासून सुरुवात करूया, हे एक जनरेटिव्ह AI मॉडेल आहे जे मजकूर वर्णनांपासून प्रतिमा तयार करते.

> [DALL-E हा दोन मॉडेल्स CLIP आणि डिफ्यूज्ड अटेंशन यांचा संयोजन आहे](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, एक मॉडेल आहे जे प्रतिमा आणि मजकूरातून एम्बेडिंग्स तयार करते, जे डेटाचे संख्यात्मक प्रतिनिधित्व असते.

- **डिफ्यूज्ड अटेंशन**, एक मॉडेल आहे जे एम्बेडिंग्समधून प्रतिमा तयार करते. DALL-E इमेजेस आणि मजकूर यांचे डेटासेट वापरून प्रशिक्षित केले आहे आणि मजकूर वर्णनांपासून प्रतिमा तयार करण्यासाठी वापरले जाऊ शकते. उदाहरणार्थ, DALL-E वापरून टोपी घातलेला मांजर किंवा मोहॉकसह कुत्रा यांची प्रतिमा तयार केली जाऊ शकते.

### Midjourney

Midjourney देखील DALL-E सारखेच काम करते, तो मजकूर प्रॉम्प्ट वापरून प्रतिमा तयार करतो. Midjourney वापरून “टोपी घातलेले मांजर” किंवा “मोहॉकसह कुत्रा” यांसारख्या प्रॉम्प्टसाठी प्रतिमा तयार करता येतात.

![Midjourney ने तयार केलेली प्रतिमा, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_प्रतिमा क्रेडिट विकिपीडिया, Midjourney कडून तयार केलेली प्रतिमा_

## DALL-E आणि Midjourney कसे कार्य करतात

प्रथम [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) पाहूया. DALL-E हा एक जनरेटिव्ह AI मॉडेल आहे जो ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित असून त्यात _ऑटोरेग्रेसिव्ह ट्रान्सफॉर्मर_ आहे.

_ऑटोरेग्रेसिव्ह ट्रान्सफॉर्मर_ हे कसे मजकूर वर्णनांमधून प्रतिमा तयार करतो हे ठरवतो, तो एकावेळेस एक पिक्सेल तयार करतो आणि तयार केलेल्या पिक्सेल्सचा वापर पुढील पिक्सेल तयार करण्यासाठी करतो. तो न्यूरल नेटवर्कमधील अनेक स्तरांमधून पार होतो जोपर्यंत प्रतिमा पूर्ण होत नाही.

या प्रक्रियेने, DALL-E प्रतिमेतले गुणधर्म, वस्तू, वैशिष्ट्ये आणि बरेच काही नियंत्रित करतो. तथापि, DALL-E 2 आणि 3 मध्ये तयार केलेल्या प्रतिमेवर अधिक नियंत्रण आहे.

## आपले पहिले इमेज जनरेशन अॅप्लिकेशन तयार करणे

इमेज जनरेशन अॅप्लिकेशन तयार करण्यासाठी काय लागते? आपल्याला खालील लायब्ररींची आवश्यकता आहे:

- **python-dotenv**, ही लायब्ररी वापरण्याचा सल्ला दिला जातो जेणेकरून तुमच्या रहस्यांना _.env_ फाईलमध्ये ठेवू शकता आणि कोडपासून वेगळे ठेवू शकता.
- **openai**, ही लायब्ररी OpenAI API शी संवाद साधण्यासाठी वापरली जाते.
- **pillow**, Python मध्ये प्रतिमांसह काम करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यास मदत करण्यासाठी.

## Azure OpenAI मॉडेल तयार आणि डिप्लॉय करा

जर आधी न केले असेल, तर [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) पानावरील सूचना फॉलो करा 
Azure OpenAI संसाधन आणि मॉडेल तयार करण्यासाठी. मॉडेल म्हणून **gpt-image-1** निवडा (सद्यस्थितीत जेनरेशन्आझूर OpenAI इमेज मॉडेल; DALL-E 3 हा जुना असून नव्या डिप्लॉयमेंटसाठी उपलब्ध नाही).

## अॅप तयार करा

1. खालील सामग्रीसह _.env_ नावाची फाईल तयार करा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Azure OpenAI Foundry पोर्टलमध्ये आपल्या संसाधनासाठी "Deployments" विभागात ही माहिती शोधा.

1. वरील लायब्ररींसह _requirements.txt_ नावाची फाईल तयार करा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. नंतर, व्हर्चुअल एनवायरनमेंट तयार करा आणि लायब्ररी इंस्टॉल करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows साठी, आपल्या व्हर्चुअल एनवायरनमेंट तयार आणि सक्रिय करण्यासाठी खालील आदेश वापरा:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नावाच्या फाईलमध्ये खालील कोड जोडा:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv आयात करा
    dotenv.load_dotenv()
    
    # Azure OpenAI सेवा क्लायंट कॉन्फिगर करा
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # प्रतिमा निर्मिती API वापरुन प्रतिमा तयार करा
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # साठवलेल्या प्रतिमेसाठी निर्देशिका सेट करा
        image_dir = os.path.join(os.curdir, 'images')

        # निर्देशिका अस्तित्वात नसेल तर ती तयार करा
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # प्रतिमेचा मार्ग प्रारंभ करा (फाईल प्रकार png असावा)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # तयार केलेली प्रतिमा मिळवा
        image_url = generation_response.data[0].url  # प्रतिसादातून प्रतिमा URL काढा
        generated_image = requests.get(image_url).content  # प्रतिमा डाउनलोड करा
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # डिफॉल्ट प्रतिमा दर्शकात प्रतिमा दर्शवा
        image = Image.open(image_path)
        image.show()

    # अपवाद पकडा
    except openai.BadRequestError as err:
        print(err)
   ```

चला या कोडचे स्पष्टीकरण करूया:

- प्रथम, आपल्याला आवश्यक असलेल्या लायब्ररी आयात करतो, ज्यामध्ये OpenAI लायब्ररी, dotenv लायब्ररी, requests लायब्ररी आणि Pillow लायब्ररी आहेत.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- नंतर, _.env_ फाईलमधून पर्यावरणीय चल (environment variables) लोड करतो.

  ```python
  # dotenv आयात करा
  dotenv.load_dotenv()
  ```

- त्यानंतर, Azure OpenAI सेवा ग्राहक कॉन्फिगर करतो

  ```python
  # पर्यावरण चलांमधून अंतिम बिंदू आणि की मिळवा
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- नंतर, प्रतिमा तयार करतो:

  ```python
  # इमेज जनरेशन API वापरून प्रतिमा तयार करा
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  वर दिलेला कोड जनरेट केलेल्या प्रतिमेचा URL असलेला JSON ऑब्जेक्ट परत करतो. आपण हा URL वापरून प्रतिमा डाउनलोड करू शकतो आणि फाईल म्हणून जतन करू शकतो.

- शेवटी, आपण प्रतिमा उघडतो आणि त्यासाठी डिफॉल्ट इमेज व्ह्युअर वापरतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा तयार करण्याविषयी अधिक तपशील

चला प्रतिमा तयार करणारा कोड अधिक तपशीलाने पाहूया:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, हे मजकूर प्रॉम्प्ट आहे ज्याचा वापर प्रतिमा तयार करण्यासाठी केला जातो. या प्रकरणात, आपण प्रॉम्प्ट "घोड्यावर बनी, लॉलीपॉप धरलेले, धुके असलेल्या मेदावर जिथे डॅफोडिल्स वाढतात" वापरत आहोत.
- **size**, तयार होणाऱ्या प्रतिमेचा आकार आहे. या प्रकरणात, आपण 1024x1024 पिक्सेल आकाराची प्रतिमा तयार करत आहोत.
- **n**, उत्पन्न केलेल्या प्रतिमांची संख्या आहे. या प्रकरणात, आपण दोन प्रतिमा तयार करत आहोत.
- **temperature**, हा एक पॅरामीटर आहे जो जनरेटिव्ह AI मॉडेलच्या आउटपुटची अनियमितता नियंत्रित करतो. तापमान 0 ते 1 दरम्यान आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

आणखी काही गोष्टी ज्या तुम्ही प्रतिमांसाठी करू शकता त्या पुढील विभागात आपण पाहणार आहोत.

## प्रतिमा जनरेशनच्या अतिरिक्त क्षमता

आतापर्यंत तुम्ही पाहिले की आपण Python मधील काही ओळी वापरून प्रतिमा तयार करू शकलो. मात्र प्रतिमांसह आणखी बरेच काही करता येते.

तुम्ही खालीलही करू शकता:

- **संपादने करा**. एखाद्या विद्यमान प्रतिमेला मास्क आणि प्रॉम्प्ट देऊन तुम्ही प्रतिमेत बदल करू शकता. उदाहरणार्थ, एका भागात काहीतरी जोडू शकता. आपल्या बनी प्रतिमेचा विचार करा, तुम्ही बनीला टोप सही करू शकता. त्यासाठी तुम्हाला प्रतिमा, मास्क (बदल करायचा भाग ओळखण्यासाठी) आणि मजकूर प्रॉम्प्ट देणे आवश्यक आहे जे काय करायचे ते सांगतो.
> लक्षात ठेवा: हे DALL-E 3 मध्ये समर्थित नाही.
 
GPT इमेज वापरून एक उदाहरण:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  बेस इमेजमध्ये फक्त पूलसह लाउंज असेल पण अंतिम प्रतिमेत फ्लेमिंगो असेल:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/mr/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mr/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mr/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **भिन्न रूपे तयार करा**. कल्पना अशी आहे की तुम्ही विद्यमान प्रतिमा घेता आणि त्याच्यासाठी विविध रूपे तयार करायची विनंती करता. विविध रूप तयार करण्यासाठी, तुम्ही प्रतिमा आणि मजकूर प्रॉम्प्ट देता आणि खालीलप्रमाणे कोड वापरता:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > लक्षात ठेवा, हे फक्त OpenAI च्या DALL-E 2 मॉडेलवर समर्थित आहे, gpt-image-1 वर नाही

## तापमान (Temperature)

तापमान हा एक पॅरामीटर आहे जो जनरेटिव्ह AI मॉडेलच्या आउटपुटचा अनियमितपणा नियंत्रित करतो. तापमान 0 ते 1 दरम्यान आहे जिथे 0 म्हणजे आउटपुट निश्चित आहे आणि 1 म्हणजे आउटपुट अनियमित आहे. डीफॉल्ट मूल्य 0.7 आहे.

तापमान कसे कार्य करते याचे उदाहरण पाहूया, हा प्रॉम्प्ट दोन वेळा चालवत:

> प्रॉम्प्ट : "घोड्यावर बनी, लॉलीपॉप धरलेला, धुके असलेल्या मेदावर जिथे डॅफोडिल्स वाढतात"

![घोड्यावर बनी लॉलीपॉप धरलेला, आवृत्ती 1](../../../translated_images/mr/v1-generated-image.a295cfcffa3c13c2.webp)

आता तोच प्रॉम्प्ट पुन्हा चालवूया जसे की आपण दोनदा तोच प्रतिमा प्राप्त करणार नाही याची खात्री करण्यासाठी:

![घोड्यावर बनी ची तयार केलेली प्रतिमा](../../../translated_images/mr/v2-generated-image.33f55a3714efe61d.webp)

तुम्हाला दिसेल की प्रतिमा सारख्या आहेत, पण अगदी सारख्या नाहीत. चला तापमानाचे मूल्य 0.1 करा आणि काय होते ते पाहूया:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # आपला प्रॉम्प्ट मजकूर येथे टाका
        size='1024x1024',
        n=2
    )
```

### तापमान बदलणे

म्हणून, प्रत्युत्तर अधिक निश्चित करण्याचा प्रयत्न करू. आपण तयार केलेल्या दोन प्रतिमा पाहून असे लक्षात येते की पहिल्या प्रतिमेत बनी आहे आणि दुसऱ्या प्रतिमेत घोडा, त्यामुळे प्रतिमा खूप वेगळ्या आहेत.

म्हणून आपण आपला कोड सुधारून तापमान 0 असा सेट करू:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # आपला प्रॉम्प्ट मजकूर येथे टाका
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता जेव्हा तुम्ही हा कोड चालवाल, तेव्हा तुम्हाला या दोन प्रतिमा मिळतील:

- ![तापमान 0, आवृत्ती 1](../../../translated_images/mr/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![तापमान 0, आवृत्ती 2](../../../translated_images/mr/v2-temp-generated-image.871d0c920dbfb0f1.webp)

येथे तुम्हाला स्पष्टपणे दिसेल की प्रतिमा अधिक समान आहेत.

## कसे मेटाप्रोम्प्टसह आपल्या अॅप्लिकेशनसाठी मर्यादा निश्चित कराव्यात

आपल्या डेमोमध्ये, आपण आधीच आपल्या क्लायंटसाठी प्रतिमा तयार करू शकतो. तथापि, आपल्याला आपल्या अॅप्लिकेशनसाठी काही मर्यादा तयार करण्याची गरज आहे.

उदाहरणार्थ, आपण अशा प्रतिमा तयार करू इच्छित नाही ज्या कामासाठी योग्य नाहीत किंवा ज्या मुलांसाठी योग्य नाहीत.

आपण हे _मेटाप्रोम्प्ट्स_ द्वारे करू शकतो. मेटाप्रोम्प्ट्स हे मजकूर प्रॉम्प्ट आहेत जे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवतात. उदाहरणार्थ, आपण मेटाप्रोम्प्ट्स वापरून आउटपुट नियंत्रित करू शकतो, आणि तयार केलेल्या प्रतिमांची कामासाठी सुरक्षितता किंवा मुलांसाठी योग्यतेची खात्री करू शकतो.

### ते कसे कार्य करते?

आता, मेटाप्रोम्प्ट कसे कार्य करतात?

मेटाप्रोम्प्ट्स हे मजकूर प्रॉम्प्ट असतात जे जनरेटिव्ह AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवतात, ते मजकूर प्रॉम्प्टच्या अगोदर ठेवले जातात, आणि आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात. अॅप्लिकेशन्समध्ये त्यांचा समावेश केला जातो जेणेकरून मॉडेलच्या आउटपुटवर नियंत्रण ठेवता येऊ शकेल. हा संपूर्ण मजकूर प्रॉम्प्ट एकत्र आखलेला असतो ज्यात मेटाप्रोम्प्ट आणि प्रॉम्प्ट दोन्ही असतात.

एका मेटा प्रॉम्प्टचे उदाहरण खालीलप्रमाणे असू शकते:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

आता, चला पाहूया की डेमोमध्ये आपण मेटाप्रोम्प्ट कसे वापरू शकतो.

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

# TODO प्रतिमा तयार करण्यासाठी विनंती जोडा
```

वरील प्रॉम्प्टमधून तुम्हाला दिसते की तयार होणाऱ्या सर्व प्रतिमा मेटाप्रोम्प्टचा विचार करतात.

## असाइनमेंट - विद्यार्थ्यांना सक्षम करूया

आपण या धड्याच्या सुरुवातीस Edu4All ओळखले. आता विद्यार्थ्यांना त्यांच्या मूल्यमापनांसाठी प्रतिमा तयार करू देण्याची वेळ आली आहे.


विद्यार्थी त्यांच्या मूल्यांकनांसाठी स्मारके असलेली चित्रे तयार करतील, कोणती स्मारके असतील हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना या कार्यामध्ये त्यांच्या सर्जनशीलतेचा वापर करण्याचा आग्रह केला जातो ज्याने ते वेगवेगळ्या संदर्भांत स्मारकांची ठिकाणे ठरवतील.

## उपाय

येथे एक शक्य तो उपाय आहे:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv आयात करा
dotenv.load_dotenv()

# पर्यावरण चलांमधून endpoint आणि key मिळवा
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
    # प्रतिमा निर्मिती API वापरून प्रतिमा तयार करा
    generation_response = client.images.generate(
        prompt=prompt,    # आपला प्रॉम्प्ट मजकूर येथे प्रविष्ट करा
        size='1024x1024',
        n=1,
    )
    # संचयन केलेल्या प्रतिमेसाठी निर्देशिका सेट करा
    image_dir = os.path.join(os.curdir, 'images')

    # जर निर्देशिका अस्तित्वात नसेल, तर ती तयार करा
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # प्रतिमा मार्ग प्रारंभ करा (टीप, फाइल प्रकार png असावा)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # निर्मित प्रतिमा पुनर्प्राप्त करा
    image_url = generation_response.data[0].url  # प्रतिसादातून प्रतिमेचा URL काढा
    generated_image = requests.get(image_url).content  # प्रतिमा डाउनलोड करा
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # डीफॉल्ट प्रतिमा दर्शकात प्रतिमा दर्शवा
    image = Image.open(image_path)
    image.show()

# अपवाद पकडा
except openai.BadRequestError as err:
    print(err)
```

## उत्कृष्ट काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [जनरेटिव्ह AI शिक्षण संकलनात](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पहा जेणेकरून तुम्ही तुमचे जनरेटिव्ह AI ज्ञान आणखी वाढवू शकता!

धडा 10 कडे जा जिथे आपण पाहणार आहोत की [कम-कोड वापरून AI अॅप्लिकेशन्स कसे तयार करायचे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->