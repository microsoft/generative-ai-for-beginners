<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:04:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ne"
}
-->
# चित्र उत्पादन अनुप्रयोगहरू निर्माण गर्दै

LLMs मा पाठ उत्पादन भन्दा धेरै छ। पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्न पनि सम्भव छ। चित्रहरू एक मोडालिटीको रूपमा धेरै क्षेत्रहरूमा अत्यधिक उपयोगी हुन सक्छन्, जस्तै मेडटेक, वास्तुकला, पर्यटन, खेल विकास र अन्य धेरै। यस अध्यायमा, हामी दुई सबैभन्दा लोकप्रिय चित्र उत्पादन मोडेलहरू, DALL-E र Midjourney मा ध्यान केन्द्रित गर्नेछौं।

## परिचय

यस पाठमा, हामीले समेट्नेछौं:

- चित्र उत्पादन र यसको उपयोगिता किन छ।
- DALL-E र Midjourney, के हुन् र कसरी काम गर्छन्।
- कसरी तपाईं चित्र उत्पादन अनुप्रयोग निर्माण गर्नुहुन्छ।

## सिकाइ लक्ष्यहरू

यो पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- चित्र उत्पादन अनुप्रयोग निर्माण गर्नुहोस्।
- मेटा प्रम्प्टहरू प्रयोग गरेर तपाईंको अनुप्रयोगको सिमानाहरू परिभाषित गर्नुहोस्।
- DALL-E र Midjourney संग काम गर्नुहोस्।

## किन चित्र उत्पादन अनुप्रयोग निर्माण गर्ने?

चित्र उत्पादन अनुप्रयोगहरू जनरेटिभ AI को क्षमताहरू अन्वेषण गर्ने उत्कृष्ट तरिका हुन्। तिनीहरू विभिन्न उपयोगका लागि प्रयोग गर्न सकिन्छ, जस्तै:

- **चित्र सम्पादन र संश्लेषण**। तपाईं विभिन्न उपयोगका लागि चित्रहरू उत्पादन गर्न सक्नुहुन्छ, जस्तै चित्र सम्पादन र चित्र संश्लेषण।

- **विभिन्न उद्योगहरूमा लागू गर्न सकिने**। तिनीहरू मेडटेक, पर्यटन, खेल विकास र अन्य धेरै जस्ता विभिन्न उद्योगहरूको लागि चित्रहरू उत्पादन गर्न पनि प्रयोग गर्न सकिन्छ।

## परिदृश्य: Edu4All

यस पाठको रूपमा, हामी हाम्रो स्टार्टअप, Edu4All, सँग काम जारी राख्नेछौं। विद्यार्थीहरूले आफ्नो मूल्याङ्कनहरूको लागि चित्रहरू सिर्जना गर्नेछन्, के चित्रहरू सिर्जना गर्ने भन्ने विद्यार्थीहरूमा निर्भर हुन्छ, तर तिनीहरूले आफ्नै परी कथा को लागि चित्रणहरू वा आफ्नो कथाको लागि नयाँ पात्र सिर्जना गर्न वा उनीहरूको विचार र अवधारणाहरूलाई दृश्य बनाउन सक्छन्।

यहाँ Edu4All का विद्यार्थीहरूले के सिर्जना गर्न सक्थे उदाहरणको रूपमा यदि तिनीहरू वर्गमा स्मारकहरूमा काम गर्दैछन्:

![Edu4All स्टार्टअप, स्मारकहरूमा वर्ग, एफिल टावर](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.ne.png)

प्रम्प्ट जस्तै प्रयोग गर्दै

> "एफिल टावरको छेउमा कुकुर बिहानको प्रारम्भिक सूर्यको प्रकाशमा"

## DALL-E र Midjourney के हो?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) र [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दुई सबैभन्दा लोकप्रिय चित्र उत्पादन मोडेलहरू हुन्, तिनीहरूले तपाईंलाई प्रम्प्टहरू प्रयोग गरेर चित्रहरू उत्पादन गर्न अनुमति दिन्छन्।

### DALL-E

आउनुहोस्, DALL-E बाट सुरु गरौं, जुन पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्ने एक जनरेटिभ AI मोडेल हो।

> [DALL-E दुई मोडेलहरू, CLIP र diffused attention को संयोजन हो](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मोडेल हो जसले इम्बेडिङहरू, जुन डेटा को संख्यात्मक प्रतिनिधित्वहरू हुन्, चित्र र पाठबाट उत्पन्न गर्दछ।

- **Diffused attention**, एक मोडेल हो जसले इम्बेडिङहरूबाट चित्रहरू उत्पन्न गर्दछ। DALL-E चित्र र पाठको डेटासेटमा तालिम प्राप्त छ र पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्न प्रयोग गर्न सकिन्छ। उदाहरणका लागि, DALL-E एक टोपीमा बिरालो वा माउखक भएको कुकुरको चित्र उत्पादन गर्न प्रयोग गर्न सकिन्छ।

### Midjourney

Midjourney DALL-E जस्तै तरिकामा काम गर्दछ, यसले पाठ प्रम्प्टहरूबाट चित्रहरू उत्पादन गर्दछ। Midjourney पनि "टोपीमा बिरालो" वा "माउखक भएको कुकुर" जस्ता प्रम्प्टहरू प्रयोग गरेर चित्रहरू उत्पादन गर्न प्रयोग गर्न सकिन्छ।

![Midjourney द्वारा उत्पन्न चित्र, यान्त्रिक परेवा](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_चित्र श्रेय विकिपीडिया, Midjourney द्वारा उत्पन्न चित्र_

## DALL-E र Midjourney कसरी काम गर्छन्

पहिले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक ट्रान्सफर्मर आर्किटेक्चरमा आधारित जनरेटिभ AI मोडेल हो जुन _autoregressive transformer_ हो।

एक _autoregressive transformer_ ले कसरी एक मोडेल पाठ विवरणहरूबाट चित्रहरू उत्पन्न गर्दछ भनेर परिभाषित गर्दछ, यो एक पटकमा एक पिक्सेल उत्पन्न गर्दछ, र त्यसपछि उत्पन्न पिक्सेलहरूलाई अर्को पिक्सेल उत्पन्न गर्न प्रयोग गर्दछ। एक न्यूरल नेटवर्कमा धेरै तहहरू पार गर्दै, जबसम्म चित्र पूरा हुँदैन।

यस प्रक्रियासँग, DALL-E, चित्रमा उत्पन्न हुने विशेषताहरू, वस्तुहरू, विशेषताहरू, र थपहरू नियन्त्रण गर्दछ। यद्यपि, DALL-E 2 र 3 ले उत्पन्न चित्रमा बढी नियन्त्रण राख्छन्।

## तपाईंको पहिलो चित्र उत्पादन अनुप्रयोग निर्माण गर्दै

तपाईंलाई चित्र उत्पादन अनुप्रयोग निर्माण गर्न के आवश्यक छ? तपाईंलाई निम्न पुस्तकालयहरू आवश्यक छन्:

- **python-dotenv**, तपाईंलाई तपाईंको गोप्य कुरा _.env_ फाइलमा कोडबाट टाढा राख्न यो पुस्तकालय प्रयोग गर्न अत्यधिक सिफारिस गरिएको छ।
- **openai**, यो पुस्तकालय हो जसलाई तपाईं OpenAI API सँग अन्तरक्रिया गर्न प्रयोग गर्नुहुन्छ।
- **pillow**, Python मा चित्रहरूसँग काम गर्न।
- **requests**, तपाईंलाई HTTP अनुरोधहरू गर्न मद्दत गर्न।

1. तलको सामग्रीको साथ _.env_ फाइल सिर्जना गर्नुहोस्:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   यो जानकारी Azure Portal मा तपाईंको स्रोतको लागि "Keys and Endpoint" खण्डमा पत्ता लगाउनुहोस्।

1. माथिका पुस्तकालयहरूलाई _requirements.txt_ नामक फाइलमा यसरी सङ्कलन गर्नुहोस्:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. त्यसपछि, भर्चुअल वातावरण सिर्जना गर्नुहोस् र पुस्तकालयहरू स्थापना गर्नुहोस्:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows को लागि, तपाईंको भर्चुअल वातावरण सिर्जना र सक्रिय गर्न निम्न आदेशहरू प्रयोग गर्नुहोस्:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामक फाइलमा तलको कोड थप्नुहोस्:

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

यस कोडलाई व्याख्या गरौं:

- पहिले, हामीलाई आवश्यक पर्ने पुस्तकालयहरू आयात गर्छौं, OpenAI पुस्तकालय, dotenv पुस्तकालय, requests पुस्तकालय, र Pillow पुस्तकालय समावेश गर्दै।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- त्यसपछि, हामी _.env_ फाइलबाट वातावरणीय भेरिएबलहरू लोड गर्छौं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यसपछि, हामी OpenAI API को लागि अन्त बिन्दु, कुञ्जी, संस्करण र प्रकार सेट गर्छौं।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- त्यसपछि, हामी चित्र उत्पादन गर्छौं:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  माथिको कोडले उत्पन्न चित्रको URL समावेश गर्ने JSON वस्तु संग प्रतिक्रिया गर्दछ। हामी चित्र डाउनलोड गर्न र फाइलमा सुरक्षित गर्न URL प्रयोग गर्न सक्छौं।

- अन्तमा, हामी चित्र खोल्छौं र मानक चित्र दर्शक प्रयोग गरेर प्रदर्शन गर्छौं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### चित्र उत्पादनको थप विवरणहरू

हामी चित्र उत्पादन गर्ने कोडलाई थप विवरणमा हेरौं:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, पाठ प्रम्प्ट हो जसले चित्र उत्पादन गर्न प्रयोग गर्दछ। यस अवस्थामा, हामी "घोडामा बनी, ललिपप समातेको, कुहिरोको मैदानमा जहाँ डफोडिलहरू उच्छिन्छन्" प्रम्प्ट प्रयोग गर्दैछौं।
- **size**, उत्पन्न चित्रको आकार हो। यस अवस्थामा, हामी 1024x1024 पिक्सेलको चित्र उत्पादन गर्दैछौं।
- **n**, उत्पन्न चित्रहरूको संख्या हो। यस अवस्थामा, हामी दुई चित्रहरू उत्पादन गर्दैछौं।
- **temperature**, एक जनरेटिभ AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्ने प्यारामिटर हो। तापक्रम 0 र 1 बीचको मान हो जहाँ 0 ले उत्पादन निर्धारणात्मक छ र 1 ले उत्पादन अनियमित छ भन्ने अर्थ हुन्छ। डिफल्ट मान 0.7 हो।

तपाईंले चित्रहरूसँग गर्न सक्ने थप कुराहरू छन् जुन हामी अर्को खण्डमा समेट्नेछौं।

## चित्र उत्पादनको थप क्षमताहरू

तपाईंले देख्नु भएको छ कि हामीले केही लाइनहरूको Python मा चित्र उत्पन्न गर्न सक्षम भयौं। तथापि, तपाईं चित्रहरूसँग गर्न सक्ने थप कुराहरू छन्।

तपाईं निम्न पनि गर्न सक्नुहुन्छ:

- **सम्पादन गर्नुहोस्**। अवस्थित चित्रलाई मास्क र प्रम्प्ट प्रदान गरेर, तपाईं चित्र परिवर्तन गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईं चित्रको एक भागमा केहि थप्न सक्नुहुन्छ। हाम्रो बनी चित्रको कल्पना गर्नुहोस्, तपाईं बनीलाई टोपी थप्न सक्नुहुन्छ। तपाईंले कसरी यो गर्नुहुन्छ भने चित्र, मास्क (परिवर्तनको लागि क्षेत्रको पहिचान गर्दै) र पाठ प्रम्प्ट प्रदान गरेर के गरिनु पर्छ भनेर भन्नुहोस्।

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

  आधार चित्रमा केवल खरायो मात्र हुनेछ तर अन्तिम चित्रमा खरायोमा टोपी हुनेछ।

- **भिन्नताहरू सिर्जना गर्नुहोस्**। विचार यो हो कि तपाईं अवस्थित चित्र लिन्छ र भिन्नताहरू सिर्जना गर्न सोध्नुहुन्छ। भिन्नता सिर्जना गर्न, तपाईं चित्र र पाठ प्रम्प्ट प्रदान गर्नुहोस् र यसरी कोड गर्नुहोस्:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यो केवल OpenAI मा समर्थित छ

## तापक्रम

तापक्रम एक जनरेटिभ AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्ने प्यारामिटर हो। तापक्रम 0 र 1 बीचको मान हो जहाँ 0 ले उत्पादन निर्धारणात्मक छ र 1 ले उत्पादन अनियमित छ भन्ने अर्थ हुन्छ। डिफल्ट मान 0.7 हो।

हामी कसरी तापक्रम काम गर्छ हेर्न एक उदाहरण हेरौं, यो प्रम्प्ट दुई पटक चलाएर:

> प्रम्प्ट : "घोडामा बनी, ललिपप समातेको, कुहिरोको मैदानमा जहाँ डफोडिलहरू उच्छिन्छन्"

![घोडामा बनी ललिपप समातेको, संस्करण 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.ne.png)

अब उही प्रम्प्ट फेरि चलाउँछौं ताकि हामी दुई पटक एउटै चित्र नपाउनेछौं:

![घोडामा बनी घोडामा उत्पन्न चित्र](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.ne.png)

जसरी तपाईं देख्न सक्नुहुन्छ, चित्रहरू मिल्दोजुल्दो छन्, तर उस्तै छैनन्। तापक्रम मानलाई 0.1 मा परिवर्तन गरेर के हुन्छ हेर्न प्रयास गरौं:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापक्रम परिवर्तन गर्दै

त्यसैले प्रतिक्रिया अधिक निर्धारणात्मक बनाउन प्रयास गरौं। हामीले उत्पन्न गरेका दुई चित्रहरूबाट अवलोकन गर्न सक्थ्यौं कि पहिलो चित्रमा खरायो छ र दोस्रो चित्रमा घोडा छ, त्यसैले चित्रहरू धेरै भिन्न छन्।

त्यसैले हाम्रो कोड परिवर्तन गरौं र तापक्रमलाई 0 मा सेट गरौं, यसरी:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब तपाईं यो कोड चलाउनुहुन्छ, तपाईं यी दुई चित्रहरू प्राप्त गर्नुहुन्छ:

- ![तापक्रम 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.ne.png)
- ![तापक्रम 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.ne.png)

यहाँ तपाईं स्पष्ट रूपमा देख्न सक्नुहुन्छ कि चित्रहरू एकअर्कासँग बढी समान छन्।

## तपाईंको अनुप्रयोगको लागि मेटाप्रम्प्टहरू प्रयोग गरेर सिमानाहरू कसरी परिभाषित गर्ने

हाम्रो डेमोको साथ, हामी पहिले नै हाम्रा ग्राहकहरूको लागि चित्रहरू उत्पन्न गर्न सक्छौं। यद्यपि, हामीलाई हाम्रो अनुप्रयोगको लागि केही सिमानाहरू सिर्जना गर्न आवश्यक छ।

उदाहरणका लागि, हामी कामको लागि सुरक्षित नभएका वा बच्चाहरूको लागि उपयुक्त नभएका चित्रहरू उत्पन्न गर्न चाहँदैनौं।

हामी यो _मेटाप्रम्प्टहरू_ को साथ गर्न सक्छौं। मेटाप्रम्प्टहरू पाठ प्रम्प्टहरू हुन् जसले जनरेटिभ AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ। उदाहरणका लागि, हामीले मेटाप्रम्प्टहरू प्रयोग गरेर उत्पादनलाई नियन्त्रण गर्न सक्छौं, र सुनिश्चित गर्न सक्छौं कि उत्पन्न चित्रहरू कामको लागि सुरक्षित छन्, वा बच्चाहरूको लागि उपयुक्त छन्।

### यो कसरी काम गर्छ?

अब, मेटाप्रम्प्टहरू कसरी काम गर्छन्?

मेटाप्रम्प्टहरू पाठ प्रम्प्टहरू हुन् जसले जनरेटिभ AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ, तिनीहरू पाठ प्रम्प्टको अघि राखिएका हुन्छन्, र मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ र अनुप्रयोगहरूमा मोडेलको उत्पादनलाई नियन्त्रण गर्न समाहित गरिन्छ। प्रम्प्ट इनपुट र मेटाप्रम्प्ट इनपुटलाई एउटै पाठ प्रम्प्टमा संलग्न गर्दै।

मेटाप्रम्प्टको एउटा उदाहरण निम्न हुनेछ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, हेरौं कि हामी हाम्रो डेमोमा मेटाप्रम्प्टहरू कसरी प्रयोग गर्न सक्छौं।

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

माथिको प्रम्प्टबाट, तपाईंले देख्न सक्नुहुन्छ कि सबै उत्पन्न चित्रहरूले मेटाप्रम्प्टलाई विचार गर्छन्।

## असाइनमेन्ट - विद्यार्थीहरूलाई सक्षम बनाऔं

हामीले Edu4All लाई यस पाठको सुरुवातमा प्रस्तुत गर्यौं। अब यो विद्यार्थीहरूलाई उनीहरूको मूल्याङ्कनहरूको लागि चित्रहरू उत्पन्न गर्न सक्षम बनाउने समय हो।

विद्यार्थीहरूले स्मारकहरू समावेश गर्ने उनीहरूको मूल्याङ्कनहरूको लागि चित्रहरू सिर्जना गर्नेछन्, के स्मारकहरू सिर्जना गर्ने भन्ने विद्यार्थीहरूमा निर्भर हुन्छ। विद्यार्थीहरूलाई यस कार्यमा उनीहरूको सिर्जनशीलता प्रयोग गर्न सोधिएको छ ताकि यी स्मारकहरूलाई विभिन्न सन्दर्भहरूमा राख्न सकून्।

## समाधान

यहाँ एक सम्भावित समाधान छ:

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

## राम्रो काम! तपाईंको सिकाइ जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् ताकि तपाईंको जनरेटिभ AI ज्ञानलाई स्तरवृद्धि गर्न जारी राख्न सक्नुहोस्!

पाठ 10 तर्फ जानुहोस् जहाँ हामी [कम-कोड AI अनुप्रयोगहरू निर्माण गर्ने](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) हेर्नेछौं।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गरिरहे पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी उत्तरदायी हुनेछैनौं।