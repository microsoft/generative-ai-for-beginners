<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:21:07+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "mr"
}
-->
# इमेज जनरेशन अॅप्लिकेशन्स तयार करणे

[![इमेज जनरेशन अॅप्लिकेशन्स तयार करणे](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.mr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs फक्त टेक्स्ट जनरेशनपुरते मर्यादित नाहीत. टेक्स्ट वर्णनांवरून प्रतिमा तयार करणे देखील शक्य आहे. प्रतिमा ही एक माध्यम म्हणून अनेक क्षेत्रांमध्ये खूप उपयुक्त ठरू शकते, जसे की MedTech, आर्किटेक्चर, पर्यटन, गेम डेव्हलपमेंट आणि बरेच काही. या अध्यायात, आपण दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स, DALL-E आणि Midjourney यांचा अभ्यास करू.

## परिचय

या धड्यात आपण खालील गोष्टी पाहणार आहोत:

- इमेज जनरेशन म्हणजे काय आणि ते का उपयुक्त आहे.
- DALL-E आणि Midjourney काय आहेत आणि ते कसे काम करतात.
- इमेज जनरेशन अॅप्लिकेशन कसे तयार कराल.

## शिकण्याचे उद्दिष्ट

हा धडा पूर्ण केल्यानंतर, तुम्ही सक्षम असाल:

- इमेज जनरेशन अॅप्लिकेशन तयार करणे.
- मेटा प्रॉम्प्ट्स वापरून तुमच्या अॅप्लिकेशनसाठी मर्यादा ठरवणे.
- DALL-E आणि Midjourney सोबत काम करणे.

## इमेज जनरेशन अॅप्लिकेशन का तयार करावे?

इमेज जनरेशन अॅप्लिकेशन्स हे Generative AI च्या क्षमतांचा शोध घेण्याचा एक उत्तम मार्ग आहे. त्यांचा वापर खालीलप्रमाणे करता येतो:

- **इमेज एडिटिंग आणि सिंथेसिस**. तुम्ही विविध वापरासाठी प्रतिमा तयार करू शकता, जसे की इमेज एडिटिंग आणि इमेज सिंथेसिस.

- **विविध उद्योगांमध्ये वापर**. Medtech, पर्यटन, गेम डेव्हलपमेंट आणि इतर अनेक उद्योगांसाठी प्रतिमा तयार करण्यासाठी देखील वापरता येतात.

## परिस्थिती: Edu4All

या धड्याचा भाग म्हणून, आपण Edu4All नावाच्या आपल्या स्टार्टअपसह काम सुरू ठेवणार आहोत. विद्यार्थी त्यांच्या मूल्यांकनांसाठी प्रतिमा तयार करतील, कोणत्या प्रतिमा तयार करायच्या आहेत हे विद्यार्थ्यांवर अवलंबून आहे, पण त्या त्यांच्या स्वतःच्या गोष्टीसाठी चित्रे असू शकतात, नवीन पात्र तयार करू शकतात किंवा त्यांच्या कल्पना आणि संकल्पना दृश्यमान करू शकतात.

उदाहरणार्थ, जर Edu4All चे विद्यार्थी वर्गात स्मारकांवर काम करत असतील तर ते काय तयार करू शकतात:

![Edu4All स्टार्टअप, स्मारकांवर वर्ग, एफिल टॉवर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.mr.png)

खालीलप्रमाणे प्रॉम्प्ट वापरून

> "डॉग एफिल टॉवरच्या जवळ सकाळच्या पहाटेच्या सूर्यप्रकाशात"

## DALL-E आणि Midjourney काय आहेत?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) आणि [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) हे दोन सर्वात लोकप्रिय इमेज जनरेशन मॉडेल्स आहेत, जे प्रॉम्प्ट्स वापरून प्रतिमा तयार करतात.

### DALL-E

चला DALL-E पासून सुरुवात करूया, जे एक Generative AI मॉडेल आहे जे टेक्स्ट वर्णनांवरून प्रतिमा तयार करते.

> [DALL-E हे दोन मॉडेल्स, CLIP आणि diffused attention यांचे संयोजन आहे](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, हे एक मॉडेल आहे जे प्रतिमा आणि टेक्स्टमधून डेटा चे संख्यात्मक प्रतिनिधित्व (embeddings) तयार करते.

- **Diffused attention**, हे एक मॉडेल आहे जे embeddings वरून प्रतिमा तयार करते. DALL-E प्रतिमा आणि टेक्स्टच्या डेटासेटवर प्रशिक्षित आहे आणि टेक्स्ट वर्णनांवरून प्रतिमा तयार करू शकते. उदाहरणार्थ, DALL-E वापरून टोपी घातलेला मांजर किंवा मोहॉक असलेला कुत्रा यांसारख्या प्रतिमा तयार करता येतात.

### Midjourney

Midjourney देखील DALL-E प्रमाणेच काम करते, ती टेक्स्ट प्रॉम्प्ट्स वापरून प्रतिमा तयार करते. Midjourney वापरून “टोपी घातलेला मांजर” किंवा “मोहॉक असलेला कुत्रा” यांसारख्या प्रॉम्प्ट्सवरून प्रतिमा तयार करता येतात.

![Midjourney ने तयार केलेली प्रतिमा, यांत्रिक कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_प्रतिमा क्रेडिट: विकिपीडिया, Midjourney ने तयार केलेली प्रतिमा_

## DALL-E आणि Midjourney कसे काम करतात

सर्वप्रथम, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E हा एक Generative AI मॉडेल आहे जो ट्रान्सफॉर्मर आर्किटेक्चरवर आधारित आहे आणि त्यात _autoregressive transformer_ वापरला जातो.

_autoregressive transformer_ म्हणजे मॉडेल कसे टेक्स्ट वर्णनांवरून प्रतिमा तयार करते, हे ठरवणारा तंत्र आहे. तो एकावेळी एक पिक्सेल तयार करतो आणि तयार केलेल्या पिक्सेल्सचा वापर पुढील पिक्सेल तयार करण्यासाठी करतो. हा प्रक्रिया न्यूरल नेटवर्कच्या अनेक स्तरांमधून पार पडते, जोपर्यंत प्रतिमा पूर्ण होत नाही.

या प्रक्रियेमुळे DALL-E प्रतिमेत असलेल्या गुणधर्म, वस्तू, वैशिष्ट्ये आणि बरेच काही नियंत्रित करू शकतो. मात्र, DALL-E 2 आणि 3 मध्ये तयार केलेल्या प्रतिमेवर अधिक नियंत्रण आहे.

## तुमचे पहिले इमेज जनरेशन अॅप्लिकेशन तयार करणे

तर, इमेज जनरेशन अॅप्लिकेशन तयार करण्यासाठी काय लागते? तुम्हाला खालील लायब्ररींची गरज आहे:

- **python-dotenv**, ही लायब्ररी वापरण्याची शिफारस केली जाते ज्यामुळे तुमचे गुपित _.env_ फाईलमध्ये कोडपासून वेगळे ठेवता येते.
- **openai**, ही लायब्ररी OpenAI API शी संवाद साधण्यासाठी वापरली जाते.
- **pillow**, Python मध्ये प्रतिमांसोबत काम करण्यासाठी.
- **requests**, HTTP विनंत्या करण्यासाठी.

1. _.env_ नावाची फाईल तयार करा आणि खालील माहिती भरा:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure पोर्टलमध्ये तुमच्या रिसोर्सच्या "Keys and Endpoint" विभागात ही माहिती मिळेल.

1. वरील लायब्ररींची यादी _requirements.txt_ नावाच्या फाईलमध्ये तयार करा:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. नंतर, व्हर्च्युअल एन्व्हायर्नमेंट तयार करा आणि लायब्ररी इन्स्टॉल करा:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows साठी, व्हर्च्युअल एन्व्हायर्नमेंट तयार करण्यासाठी आणि सक्रिय करण्यासाठी खालील कमांड वापरा:

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

या कोडचे स्पष्टीकरण:

- प्रथम, आवश्यक लायब्ररी आयात करतो, ज्यात OpenAI लायब्ररी, dotenv लायब्ररी, requests लायब्ररी आणि Pillow लायब्ररी यांचा समावेश आहे.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- नंतर, _.env_ फाईलमधून पर्यावरणीय चल (environment variables) लोड करतो.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यानंतर, OpenAI API साठी endpoint, key, version आणि type सेट करतो.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- पुढे, प्रतिमा तयार करतो:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  वरील कोड JSON ऑब्जेक्टमध्ये तयार केलेल्या प्रतिमेचा URL परत करतो. आपण हा URL वापरून प्रतिमा डाउनलोड करून फाईलमध्ये जतन करू शकतो.

- शेवटी, प्रतिमा उघडतो आणि स्टँडर्ड इमेज व्ह्युअर वापरून ती दाखवतो:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### प्रतिमा तयार करण्याबाबत अधिक तपशील

चला प्रतिमा तयार करणाऱ्या कोडवर अधिक सविस्तर नजर टाकूया:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ही टेक्स्ट प्रॉम्प्ट आहे ज्याचा वापर प्रतिमा तयार करण्यासाठी केला जातो. या उदाहरणात, प्रॉम्प्ट आहे "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size**, तयार होणाऱ्या प्रतिमेचा आकार आहे. येथे 1024x1024 पिक्सेल आकाराची प्रतिमा तयार केली जात आहे.
- **n**, तयार होणाऱ्या प्रतिमांची संख्या आहे. येथे दोन प्रतिमा तयार केल्या जात आहेत.
- **temperature**, हा एक पॅरामीटर आहे जो Generative AI मॉडेलच्या आउटपुटमधील अनिश्चिततेचे नियंत्रण करतो. तापमान 0 ते 1 दरम्यान असते, जिथे 0 म्हणजे आउटपुट निश्चित (deterministic) आणि 1 म्हणजे आउटपुट पूर्णपणे यादृच्छिक (random). डीफॉल्ट मूल्य 0.7 आहे.

प्रतिमांसोबत अजून बरेच काही करता येते, जे आपण पुढील विभागात पाहू.

## इमेज जनरेशनच्या अतिरिक्त क्षमता

आत्तापर्यंत आपण पाहिले की Python मध्ये काही ओळींचा वापर करून प्रतिमा कशी तयार करता येते. पण प्रतिमांसोबत अजून बरेच काही करता येते.

तुम्ही खालील गोष्टी देखील करू शकता:

- **एडिट्स करणे**. विद्यमान प्रतिमेला मास्क आणि प्रॉम्प्ट देऊन तुम्ही प्रतिमेत बदल करू शकता. उदाहरणार्थ, एखाद्या प्रतिमेच्या एका भागात काहीतरी जोडू शकता. आपल्या बनीच्या प्रतिमेचा विचार करा, तुम्ही त्याला टोपी घालू शकता. हे करण्यासाठी तुम्ही मूळ प्रतिमा, मास्क (ज्याने बदलायचा भाग ओळखला जातो) आणि टेक्स्ट प्रॉम्प्ट देऊन सांगाल की काय करायचे आहे.

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

  मूळ प्रतिमेत फक्त ससा असेल, पण अंतिम प्रतिमेत सशावर टोपी असेल.

- **व्हेरिएशन्स तयार करणे**. विद्यमान प्रतिमेवरून विविध व्हेरिएशन्स तयार करण्याची कल्पना आहे. व्हेरिएशन तयार करण्यासाठी, तुम्ही प्रतिमा आणि टेक्स्ट प्रॉम्प्ट देऊन खालीलप्रमाणे कोड वापरू शकता:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > लक्षात ठेवा, हे फक्त OpenAI वर समर्थित आहे.

## तापमान (Temperature)

तापमान हा एक पॅरामीटर आहे जो Generative AI मॉडेलच्या आउटपुटमधील अनिश्चिततेचे नियंत्रण करतो. तापमान 0 ते 1 दरम्यान असते, जिथे 0 म्हणजे आउटपुट निश्चित (deterministic) आणि 1 म्हणजे आउटपुट पूर्णपणे यादृच्छिक (random). डीफॉल्ट मूल्य 0.7 आहे.

चला तापमान कसे काम करते याचे उदाहरण पाहू, खालील प्रॉम्प्ट दोन वेळा चालवून:

> प्रॉम्प्ट : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![घोड्यावर बनी, लॉलीपॉप धरलेला, आवरण असलेल्या माळावर](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.mr.png)

आता तोच प्रॉम्प्ट पुन्हा चालवून पाहू, जेणेकरून आपल्याला दोनदा एकसारखी प्रतिमा मिळणार नाही याची खात्री होईल:

![घोड्यावर बनीची तयार केलेली प्रतिमा](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.mr.png)

जसे तुम्ही पाहू शकता, प्रतिमा सारख्या आहेत पण अगदी सारख्या नाहीत. चला तापमानाचे मूल्य 0.1 करून पाहू काय होते:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान बदलणे

तर, चला प्रतिसाद अधिक निश्चित (deterministic) करण्याचा प्रयत्न करूया. आपण तयार केलेल्या दोन प्रतिमांवरून असे दिसले की पहिल्या प्रतिमेत बनी आहे आणि दुसऱ्या प्रतिमेत घोडा आहे, त्यामुळे प्रतिमा खूप वेगवेगळ्या आहेत.

म्हणूनच, आपला कोड बदलून तापमान 0 वर सेट करूया, खालीलप्रमाणे:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

आता जेव्हा तुम्ही हा कोड चालवाल, तेव्हा तुम्हाला खालील दोन प्रतिमा मिळतील:

- ![तापमान 0, आवृत्ती 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.mr.png)
- ![तापमान 0, आवृत्ती 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.mr.png)

येथे तुम्हाला स्पष्टपणे दिसेल की प्रतिमा एकमेकांशी अधिक जुळतात.

## मेटाप्रॉम्प्ट्स वापरून तुमच्या अॅप्लिकेशनसाठी मर्यादा कशा ठरवायच्या

आपल्या डेमोमध्ये, आपण आधीच आपल्या क्लायंटसाठी प्रतिमा तयार करू शकतो. मात्र, आपल्याला आपल्या अॅप्लिकेशनसाठी काही मर्यादा तयार करणे आवश्यक आहे.

उदाहरणार्थ, आपण अशा प्रतिमा तयार करू इच्छित नाही ज्यामुळे कामाच्या ठिकाणी अयोग्य किंवा मुलांसाठी अस्वीकृत असतील.

हे आपण _मेटाप्रॉम्प्ट्स_ वापरून करू शकतो. मेटाप्रॉम्प्ट्स हे टेक्स्ट प्रॉम्प्ट्स असतात जे Generative AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात. उदाहरणार्थ, आपण मेटाप्रॉम्प्ट्स वापरून आउटपुट नियंत्रित करू शकतो आणि तयार होणाऱ्या प्रतिमा कामासाठी सुरक्षित किंवा मुलांसाठी योग्य आहेत याची खात्री करू शकतो.

### हे कसे काम करते?

मेटाप्रॉम्प्ट्स कसे काम करतात?

मेटाप्रॉम्प्ट्स हे टेक्स्ट प्रॉम्प्ट्स असतात जे Generative AI मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात, ते टेक्स्ट प्रॉम्प्टच्या आधी ठेवले जातात आणि मॉडेलच्या आउटपुटवर नियंत्रण ठेवण्यासाठी वापरले जातात. अॅप्लिकेशन्समध्ये मेटाप्रॉम्प्ट्स एम्बेड केले जातात जेणेकरून प्रॉम्प्ट इनपुट आणि मेटाप्रॉम्प्ट इनपुट एकत्रितपणे एका टेक्स्ट प्रॉम्प्टमध्ये असतात.

मेटाप्रॉम्प्टचे एक उदाहरण खालीलप्रमाणे आहे:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

आता, चला पाहूया की आपण आपल्या डेमोमध्ये मेटाप्रॉम्प्ट्स कसे वापरू शकतो.

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

वरील प्रॉम्प्टमधून तुम्हाला दिसेल की तयार होणाऱ्या सर्व प्रतिमा मेटाप्रॉम्प्टचा विचार करतात.

## असाइनमेंट - चला विद्यार्थ्यांना सक्षम करूया

या धड्याच्या सुरुवातीला आपण Edu4All ची ओळख करून दिली होती. आता विद्यार्थ्यांना त्यांच्या मूल्यांकनांसाठी प्रतिमा तयार करण्यास सक्षम करण्याची वेळ आली आहे.

विद्यार्थी त्यांच्या मूल्यांकनांसाठी स्मारकांची प्रतिमा तयार करतील, कोणती स्मारके तयार करायची आहेत हे विद्यार्थ्यांवर अवलंबून आहे. विद्यार्थ्यांना या कार्यात त्यांच्या सर्जनशीलतेचा वापर करून स्मारकांना वेगवेगळ्या संदर्भात ठेवण्यास सांगितले आहे.

## उपाय

येथे एक शक्य तो उपाय आहे:

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

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ला भेट द्या आणि तुमचे Generative AI ज्ञान अधिक वाढवा!

पुढील धडा 10 मध्ये चला जिथे आपण पाहणार आहोत की [लो-कोड वापरून AI अॅप्लिकेशन्स कसे तयार करायचे](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.