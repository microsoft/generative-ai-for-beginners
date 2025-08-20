<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:21:40+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ne"
}
-->
# छवि उत्पादन अनुप्रयोगहरू निर्माण गर्ने

[![छवि उत्पादन अनुप्रयोगहरू निर्माण गर्ने](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ne.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM हरू केवल पाठ उत्पादनमा सीमित छैनन्। पाठ विवरणहरूबाट छविहरू पनि उत्पादन गर्न सकिन्छ। छविहरूलाई एक माध्यमको रूपमा प्रयोग गर्नु धेरै क्षेत्रहरूमा उपयोगी हुन सक्छ, जस्तै MedTech, वास्तुकला, पर्यटन, खेल विकास र अन्य। यस अध्यायमा, हामी दुई सबैभन्दा लोकप्रिय छवि उत्पादन मोडेलहरू, DALL-E र Midjourney, को बारेमा अध्ययन गर्नेछौं।

## परिचय

यस पाठमा हामीले समेट्नेछौं:

- छवि उत्पादन र यसको उपयोगिता।
- DALL-E र Midjourney के हुन् र कसरी काम गर्छन्।
- कसरी छवि उत्पादन अनुप्रयोग निर्माण गर्ने।

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- छवि उत्पादन अनुप्रयोग निर्माण गर्न।
- मेटा प्रॉम्प्टहरू प्रयोग गरी आफ्नो अनुप्रयोगका सीमाहरू निर्धारण गर्न।
- DALL-E र Midjourney सँग काम गर्न।

## किन छवि उत्पादन अनुप्रयोग बनाउने?

छवि उत्पादन अनुप्रयोगहरू जनरेटिभ AI को क्षमता अन्वेषण गर्ने उत्कृष्ट तरिका हुन्। तिनीहरू निम्नका लागि प्रयोग गर्न सकिन्छ:

- **छवि सम्पादन र संश्लेषण**। तपाईं विभिन्न प्रयोगका लागि छविहरू उत्पादन गर्न सक्नुहुन्छ, जस्तै छवि सम्पादन र संश्लेषण।

- **विभिन्न उद्योगहरूमा लागू**। तिनीहरू Medtech, पर्यटन, खेल विकास लगायत विभिन्न उद्योगहरूका लागि छविहरू उत्पादन गर्न पनि प्रयोग गर्न सकिन्छ।

## परिदृश्य: Edu4All

यस पाठको भागको रूपमा, हामी हाम्रो स्टार्टअप Edu4All सँग काम जारी राख्नेछौं। विद्यार्थीहरूले आफ्नो मूल्याङ्कनका लागि छविहरू सिर्जना गर्नेछन्, कुन प्रकारका छविहरू बनाउने भन्ने निर्णय विद्यार्थीहरूमा निर्भर छ, जस्तै आफ्नै परी कथा का चित्रहरू, कथाका नयाँ पात्रहरू सिर्जना गर्ने वा आफ्ना विचार र अवधारणाहरूलाई दृश्यात्मक बनाउने।

यदि विद्यार्थीहरूले कक्षामा स्मारकहरूमा काम गरिरहेका छन् भने Edu4All का विद्यार्थीहरूले निम्न जस्तो छवि उत्पादन गर्न सक्छन्:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ne.png)

यसरी प्रॉम्प्ट प्रयोग गरेर

> "डग ईफल टावरको छेउमा बिहानको पहिलाको घाममा"

## DALL-E र Midjourney के हुन्?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) र [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दुई सबैभन्दा लोकप्रिय छवि उत्पादन मोडेलहरू हुन्, जसले प्रॉम्प्टहरू प्रयोग गरी छविहरू उत्पादन गर्न अनुमति दिन्छन्।

### DALL-E

DALL-E बाट सुरु गरौं, जुन एक जनरेटिभ AI मोडेल हो जसले पाठ विवरणहरूबाट छविहरू उत्पादन गर्छ।

> [DALL-E दुई मोडेलहरूको संयोजन हो, CLIP र diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एउटा मोडेल हो जसले छवि र पाठबाट डेटा को संख्यात्मक प्रतिनिधित्व (embeddings) उत्पादन गर्छ।

- **Diffused attention**, एउटा मोडेल हो जसले embeddings बाट छविहरू उत्पादन गर्छ। DALL-E लाई छवि र पाठको डेटासेटमा तालिम दिइएको छ र यसले पाठ विवरणबाट छविहरू उत्पादन गर्न सक्छ। उदाहरणका लागि, DALL-E ले टोपी लगाएको बिरालो वा मोहक कुकुरको छवि उत्पादन गर्न सक्छ।

### Midjourney

Midjourney पनि DALL-E जस्तै काम गर्छ, यो पाठ प्रॉम्प्टहरूबाट छविहरू उत्पादन गर्छ। Midjourney ले पनि “टोपी लगाएको बिरालो” वा “मोहक कुकुर” जस्ता प्रॉम्प्टहरू प्रयोग गरेर छविहरू बनाउन सक्छ।

![Midjourney द्वारा उत्पादन गरिएको छवि, मेकानिकल कबूतर](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_छवि स्रोत विकिपीडिया, Midjourney द्वारा उत्पादन गरिएको_

## DALL-E र Midjourney कसरी काम गर्छन्

पहिले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) लाई हेरौं। DALL-E एक जनरेटिभ AI मोडेल हो जुन ट्रान्सफर्मर आर्किटेक्चरमा आधारित छ र _autoregressive transformer_ प्रयोग गर्छ।

_autoregressive transformer_ ले मोडेलले कसरी पाठ विवरणबाट छवि उत्पादन गर्छ भन्ने परिभाषित गर्छ, यो एक पटकमा एक पिक्सेल उत्पादन गर्छ र त्यसपछि उत्पादन गरिएका पिक्सेलहरूलाई प्रयोग गरेर अर्को पिक्सेल उत्पादन गर्छ। यो प्रक्रिया न्यूरल नेटवर्कका धेरै तहहरू पार गर्दै छवि पूरा हुन्छ।

यस प्रक्रियाले DALL-E लाई छविमा वस्तुहरू, विशेषताहरू, र अन्य तत्वहरू नियन्त्रण गर्न सक्षम बनाउँछ। यद्यपि, DALL-E 2 र 3 मा उत्पादन गरिएका छविहरूमा अझ बढी नियन्त्रण हुन्छ।

## तपाईंको पहिलो छवि उत्पादन अनुप्रयोग कसरी बनाउने

त्यसैले छवि उत्पादन अनुप्रयोग बनाउन के चाहिन्छ? तपाईंलाई निम्न पुस्तकालयहरू चाहिन्छ:

- **python-dotenv**, यो पुस्तकालय प्रयोग गरेर तपाईं आफ्नो गोप्य जानकारी _.env_ फाइलमा राख्न सक्नुहुन्छ, जसले कोडबाट अलग राख्छ।
- **openai**, यो पुस्तकालय OpenAI API सँग अन्तरक्रिया गर्न प्रयोग हुन्छ।
- **pillow**, Python मा छविहरू सँग काम गर्न।
- **requests**, HTTP अनुरोधहरू बनाउन सहयोग पुर्‍याउन।

1. _.env_ नामक फाइल बनाउनुहोस् र यसमा निम्न सामग्री राख्नुहोस्:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal मा आफ्नो स्रोतको "Keys and Endpoint" सेक्सनमा यो जानकारी पाउन सकिन्छ।

1. माथिका पुस्तकालयहरूलाई _requirements.txt_ नामक फाइलमा सङ्कलन गर्नुहोस्:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. त्यसपछि, भर्चुअल वातावरण सिर्जना गरी पुस्तकालयहरू स्थापना गर्नुहोस्:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows मा भर्चुअल वातावरण सिर्जना र सक्रिय गर्न निम्न आदेशहरू प्रयोग गर्नुहोस्:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फाइलमा निम्न कोड थप्नुहोस्:

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

अब यस कोडलाई व्याख्या गरौं:

- पहिले, हामीले आवश्यक पुस्तकालयहरू आयात गर्छौं, जसमा OpenAI, dotenv, requests, र Pillow पुस्तकालयहरू समावेश छन्।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- त्यसपछि, _.env_ फाइलबाट वातावरणीय चरहरू लोड गर्छौं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यसपछि, OpenAI API को endpoint, key, संस्करण र प्रकार सेट गर्छौं।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- त्यसपछि, छवि उत्पादन गर्छौं:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  माथिको कोडले JSON वस्तुमा प्रतिक्रिया दिन्छ जसमा उत्पादन गरिएको छविको URL हुन्छ। हामी यो URL प्रयोग गरेर छवि डाउनलोड गरी फाइलमा सुरक्षित गर्न सक्छौं।

- अन्तमा, छवि खोल्छौं र मानक छवि दर्शक प्रयोग गरी देखाउँछौं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### छवि उत्पादन गर्ने कोडको थप विवरण

छवि उत्पादन गर्ने कोडलाई विस्तारमा हेरौं:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, छवि उत्पादन गर्न प्रयोग गरिएको पाठ प्रॉम्प्ट हो। यस अवस्थामा, हामीले "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" प्रयोग गरेका छौं।
- **size**, उत्पादन गरिने छविको आकार हो। यस अवस्थामा, 1024x1024 पिक्सेलको छवि उत्पादन गर्दैछौं।
- **n**, उत्पादन गरिने छविहरूको संख्या हो। यस अवस्थामा, दुई छविहरू उत्पादन गर्दैछौं।
- **temperature**, जनरेटिभ AI मोडेलको आउटपुटको अनियमितता नियन्त्रण गर्ने प्यारामिटर हो। यसको मान 0 देखि 1 को बीचमा हुन्छ, जहाँ 0 भनेको आउटपुट निश्चित हुन्छ र 1 भनेको आउटपुट पूर्ण रूपमा अनियमित हुन्छ। डिफल्ट मान 0.7 हो।

अर्को खण्डमा हामी छविहरू सँग गर्न सकिने थप कुराहरू समेट्नेछौं।

## छवि उत्पादनका अतिरिक्त क्षमता

अहिलेसम्म तपाईंले देख्नुभयो कि Python को केही लाइनहरू प्रयोग गरेर कसरी छवि उत्पादन गर्न सकिन्छ। तर छविहरू सँग गर्न सकिने थप कुराहरू पनि छन्।

तपाईं निम्न गर्न सक्नुहुन्छ:

- **सम्पादन गर्नुहोस्**। पहिलेको छवि, मास्क र प्रॉम्प्ट प्रदान गरेर छविमा परिवर्तन गर्न सकिन्छ। उदाहरणका लागि, तपाईं छविको कुनै भागमा केही थप्न सक्नुहुन्छ। हाम्रो खरायोको छविमा टोपी थप्न सकिन्छ। यसका लागि छवि, मास्क (परिवर्तन गर्नुपर्ने क्षेत्र पहिचान गर्ने) र पाठ प्रॉम्प्ट दिनुपर्छ।

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

  आधारभूत छविमा केवल खरायो हुनेछ तर अन्तिम छविमा खरायोमा टोपी हुनेछ।

- **भिन्नता सिर्जना गर्नुहोस्**। यसले पहिलेको छवि लिएर त्यसका भिन्नता सिर्जना गर्न अनुमति दिन्छ। भिन्नता सिर्जना गर्न, तपाईं छवि र पाठ प्रॉम्प्ट दिनुहुन्छ र यसरी कोड लेख्नुहुन्छ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यो केवल OpenAI मा समर्थित छ।

## तापक्रम (Temperature)

तापक्रम जनरेटिभ AI मोडेलको आउटपुटको अनियमितता नियन्त्रण गर्ने प्यारामिटर हो। यसको मान 0 देखि 1 को बीचमा हुन्छ, जहाँ 0 भनेको आउटपुट निश्चित हुन्छ र 1 भनेको आउटपुट अनियमित हुन्छ। डिफल्ट मान 0.7 हो।

तापक्रम कसरी काम गर्छ भन्ने उदाहरण हेरौं, यो प्रॉम्प्ट दुई पटक चलाएर:

> प्रॉम्प्ट: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ne.png)

अब सोही प्रॉम्प्ट फेरि चलाउँदा, हामीले दुई पटक एउटै छवि नपाउने देख्न सकिन्छ:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ne.png)

जसरी देख्न सकिन्छ, छविहरू समान छन् तर बिल्कुल एउटै छैनन्। अब तापक्रम मान 0.1 मा परिवर्तन गरेर हेरौं:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापक्रम परिवर्तन

अब प्रतिक्रिया अझ निश्चित बनाउन प्रयास गरौं। हामीले दुई छविहरूमा देख्यौं कि पहिलोमा खरायो छ र दोस्रोमा घोडा छ, त्यसैले छविहरू धेरै फरक छन्।

त्यसैले हाम्रो कोड परिवर्तन गरी तापक्रम 0 मा सेट गरौं:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब तपाईं यो कोड चलाउनुहुन्छ, तपाईंलाई यी दुई छविहरू प्राप्त हुन्छन्:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ne.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ne.png)

यहाँ स्पष्ट देख्न सकिन्छ कि छविहरू एकअर्कासँग धेरै समान छन्।

## मेटाप्रॉम्प्टहरू प्रयोग गरी अनुप्रयोगका सीमाहरू कसरी निर्धारण गर्ने

हाम्रो डेमोमा, हामीले पहिले नै ग्राहकहरूको लागि छविहरू उत्पादन गर्न सक्छौं। तर हामीले अनुप्रयोगका लागि केही सीमाहरू बनाउनु आवश्यक छ।

उदाहरणका लागि, हामी अश्लील वा बालबालिकाका लागि अनुपयुक्त छविहरू उत्पादन गर्न चाहँदैनौं।

यो हामी _मेटाप्रॉम्प्ट_ हरू प्रयोग गरेर गर्न सक्छौं। मेटाप्रॉम्प्टहरू पाठ प्रॉम्प्टहरू हुन् जसले जनरेटिभ AI मोडेलको आउटपुट नियन्त्रण गर्छन्। उदाहरणका लागि, हामी मेटाप्रॉम्प्टहरू प्रयोग गरेर आउटपुटलाई नियन्त्रण गर्न सक्छौं र सुनिश्चित गर्न सक्छौं कि उत्पादन गरिएका छविहरू सुरक्षित र उपयुक्त छन्।

### यो कसरी काम गर्छ?

अब, मेटाप्रॉम्प्टहरू कसरी काम गर्छन्?

मेटाप्रॉम्प्टहरू पाठ प्रॉम्प्टहरू हुन् जुन जनरेटिभ AI मोडेलको आउटपुट नियन्त्रण गर्न प्रयोग गरिन्छ, तिनीहरू पाठ प्रॉम्प्टभन्दा पहिले राखिन्छन् र मोडेलको आउटपुट नियन्त्रण गर्न प्रयोग गरिन्छ। अनुप्रयोगहरूमा तिनीहरू समावेश गरिन्छन् जसले मोडेलको आउटपुट नियन्त्रण गर्छ। प्रॉम्प्ट इनपुट र मेटाप्रॉम्प्ट इनपुटलाई एउटै पाठ प्रॉम्प्टमा समेटिन्छ।

मेटाप्रॉम्प्टको एउटा उदाहरण यस प्रकार छ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, हेरौं हामी हाम्रो डेमोमा मेटाप्रॉम्प्टहरू कसरी प्रयोग गर्न सक्छौं।

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

माथिको प्रॉम्प्टबाट, तपाईं देख्न सक्नुहुन्छ कि सबै उत्पादन गरिएका छविहरू मेटाप्रॉम्प्टलाई ध्यानमा राखेर बनाइएका छन्।

## असाइनमेन्ट - विद्यार्थीहरूलाई सक्षम बनाऔं

यस पाठको सुरुमै हामीले Edu4All परिचय गरायौं। अब विद्यार्थीहरूलाई आफ्नो मूल्याङ्कनका लागि छविहरू उत्पादन गर्न सक्षम बनाउने समय आएको छ।

विद्यार्थीहरूले स्मारकहरू समावेश गर्ने मूल्याङ्कनका लागि छविहरू सिर्जना गर्नेछन्, कुन स्मारकहरू बनाउने भन्ने निर्णय विद्यार्थीहरूमा निर्भर छ। विद्यार्थीहरूलाई यस कार्यमा आफ्नो सिर्जनात्मकता प्रयोग गर्न भनिएको छ र ती स्मारकहरूलाई विभिन्न सन्दर्भहरूमा राख्न भनिएको छ।

## समाधान

यहाँ एउटा सम्भावित समाधान छ:

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

## उत्कृष्ट काम! आफ्नो सिकाइ जारी राख्नुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [जनरेटिभ AI सिकाइ संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो जनरेटिभ AI ज्ञानलाई अझ उचाइमा पुर्‍याउनुहोस्!

पाठ १० मा जानुहोस् जहाँ हामी [कम कोड प्रयोग गरी AI अनुप्रयोगहरू कसरी बनाउने](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) बारे अध्ययन गर्नेछौं।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।