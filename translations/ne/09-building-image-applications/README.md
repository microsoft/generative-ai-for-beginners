<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:14:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ne"
}
-->
# चित्र उत्पादन अनुप्रयोगहरू निर्माण गर्दै

[![चित्र उत्पादन अनुप्रयोगहरू निर्माण गर्दै](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ne.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs मा पाठ उत्पादन भन्दा बढी छन्। पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्न पनि सम्भव छ। चित्रहरूलाई एक मोडालिटीको रूपमा राख्नाले मेडटेक, वास्तुकला, पर्यटन, खेल विकास र अन्य धेरै क्षेत्रमा अत्यधिक उपयोगी हुन सक्छ। यस अध्यायमा, हामी दुई सबैभन्दा लोकप्रिय चित्र उत्पादन मोडेलहरू, DALL-E र Midjourney, मा ध्यान दिनेछौं।

## परिचय

यस पाठमा, हामीले समेट्नेछौं:

- चित्र उत्पादन र यसको उपयोगिता किन।
- DALL-E र Midjourney, के हुन् र कसरी काम गर्छन्।
- कसरी तपाईं चित्र उत्पादन अनुप्रयोग निर्माण गर्नुहुन्छ।

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- चित्र उत्पादन अनुप्रयोग निर्माण गर्नुहोस्।
- मेटा प्रम्प्टहरूद्वारा आफ्नो अनुप्रयोगको सीमा परिभाषित गर्नुहोस्।
- DALL-E र Midjourney संग काम गर्नुहोस्।

## किन चित्र उत्पादन अनुप्रयोग निर्माण गर्ने?

चित्र उत्पादन अनुप्रयोगहरू जेनरेटिभ AI को क्षमताहरू अन्वेषण गर्नको लागि उत्कृष्ट तरिका हुन्। तिनीहरूलाई उदाहरणका लागि प्रयोग गर्न सकिन्छ:

- **चित्र सम्पादन र संश्लेषण**। तपाईं चित्र सम्पादन र चित्र संश्लेषण जस्ता विभिन्न प्रयोगका लागि चित्रहरू उत्पादन गर्न सक्नुहुन्छ।

- **विभिन्न उद्योगहरूमा लागू**। तिनीहरूलाई मेडटेक, पर्यटन, खेल विकास र अन्य धेरै उद्योगहरूको लागि चित्रहरू उत्पादन गर्न पनि प्रयोग गर्न सकिन्छ।

## परिदृश्य: Edu4All

यस पाठको रूपमा, हामी हाम्रो स्टार्टअप Edu4All संग काम गर्न जारी राख्नेछौं। विद्यार्थीहरूले आफ्ना मूल्याङ्कनहरूको लागि चित्रहरू सिर्जना गर्नेछन्, कुन चित्रहरू तिनीहरूमा निर्भर गर्दछ, तर तिनीहरूले आफ्नो परी कथाको लागि चित्रणहरू बनाउन सक्छन् वा आफ्नो कथाको लागि नयाँ पात्र सिर्जना गर्न सक्छन् वा तिनीहरूलाई आफ्ना विचारहरू र अवधारणाहरू दृश्यात्मक बनाउन मद्दत गर्न सक्छन्।

यहाँ के Edu4All का विद्यार्थीहरूले सिर्जना गर्न सक्छन् उदाहरणका लागि यदि तिनीहरू वर्गमा स्मारकहरूमा काम गरिरहेका छन् भने:

![Edu4All स्टार्टअप, वर्गमा स्मारकहरू, एफिल टावर](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ne.png)

जस्तै प्रम्प्ट प्रयोग गर्दै

> "एफिल टावरको छेउमा कुकुर बिहानको सूर्यप्रकाशमा"

## DALL-E र Midjourney के हो?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) र [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दुई सबैभन्दा लोकप्रिय चित्र उत्पादन मोडेलहरू हुन्, तिनीहरूले तपाईंलाई प्रम्प्टहरू प्रयोग गरेर चित्रहरू उत्पादन गर्न अनुमति दिन्छन्।

### DALL-E

DALL-E बाट सुरु गरौं, जुन जेनरेटिभ AI मोडेल हो जसले पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्छ।

> [DALL-E दुई मोडेलहरूको संयोजन हो, CLIP र diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एक मोडेल हो जसले चित्रहरू र पाठबाट डेटा को संख्यात्मक प्रतिनिधित्व, embeddings, उत्पादन गर्छ।

- **Diffused attention**, एक मोडेल हो जसले embeddings बाट चित्रहरू उत्पादन गर्छ। DALL-E लाई चित्र र पाठको डेटासेटमा तालिम दिइएको छ र पाठ विवरणहरूबाट चित्रहरू उत्पादन गर्न प्रयोग गर्न सकिन्छ। उदाहरणका लागि, DALL-E लाई टोपीमा बिरालोको चित्र उत्पादन गर्न प्रयोग गर्न सकिन्छ, वा मोहक संग कुकुरको चित्र उत्पादन गर्न प्रयोग गर्न सकिन्छ।

### Midjourney

Midjourney DALL-E जस्तै काम गर्छ, यो पाठ प्रम्प्टहरूबाट चित्रहरू उत्पादन गर्छ। Midjourney, पनि "टोपीमा बिरालो", वा "मोहक संग कुकुर" जस्ता प्रम्प्टहरू प्रयोग गरेर चित्रहरू उत्पादन गर्न प्रयोग गर्न सकिन्छ।

![Midjourney द्वारा उत्पादन गरिएको चित्र, यांत्रिक परेवा](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_चित्र स्रोत विकिपीडिया, Midjourney द्वारा उत्पादन गरिएको चित्र_

## DALL-E र Midjourney कसरी काम गर्छन्

पहिले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक जेनरेटिभ AI मोडेल हो जुन ट्रान्सफर्मर आर्किटेक्चरमा आधारित छ _autoregressive transformer_ संग।

एक _autoregressive transformer_ ले मोडेलले पाठ विवरणहरूबाट चित्रहरू कसरी उत्पादन गर्छ भन्ने कुरा परिभाषित गर्छ, यो एक पटकमा एक पिक्सेल उत्पादन गर्छ, र त्यसपछि अर्को पिक्सेल उत्पादन गर्न उत्पन्न पिक्सेलहरू प्रयोग गर्छ। एक न्यूरल नेटवर्कमा बहु तहहरू पार गर्दै, जबसम्म चित्र पूरा हुँदैन।

यस प्रक्रियासँग, DALL-E, चित्रमा उत्पन्न विशेषताहरू, वस्तुहरू, विशेषताहरू, र अधिक नियन्त्रण गर्दछ। यद्यपि, DALL-E 2 र 3 ले उत्पन्न चित्रमा बढी नियन्त्रण राख्छन्।

## आफ्नो पहिलो चित्र उत्पादन अनुप्रयोग निर्माण गर्दै

चित्र उत्पादन अनुप्रयोग निर्माण गर्न के आवश्यक छ? तपाईंलाई निम्न पुस्तकालयहरू आवश्यक छ:

- **python-dotenv**, तपाईंलाई आफ्नो गोप्य जानकारीलाई कोडबाट टाढा _.env_ फाइलमा राख्न यो पुस्तकालय प्रयोग गर्न अत्यधिक सिफारिस गरिन्छ।
- **openai**, यो पुस्तकालय तपाईंले OpenAI API सँग अन्तरक्रिया गर्न प्रयोग गर्नुहुनेछ।
- **pillow**, Python मा चित्रहरूसँग काम गर्न।
- **requests**, तपाईंलाई HTTP अनुरोधहरू गर्न मद्दत गर्न।

1. निम्न सामग्रीको साथ _.env_ फाइल सिर्जना गर्नुहोस्:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal मा आफ्नो स्रोतको लागि "Keys and Endpoint" सेक्सनमा यो जानकारी खोज्नुहोस्।

1. माथिका पुस्तकालयहरूलाई _requirements.txt_ नामक फाइलमा संकलन गर्नुहोस्:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. अब, भर्चुअल वातावरण सिर्जना गर्नुहोस् र पुस्तकालयहरू स्थापना गर्नुहोस्:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows को लागि, आफ्नो भर्चुअल वातावरण सिर्जना र सक्रिय गर्न निम्न आदेशहरू प्रयोग गर्नुहोस्:

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

यस कोडलाई व्याख्या गरौं:

- पहिले, हामीलाई आवश्यक पुस्तकालयहरू आयात गर्छौं, जसमा OpenAI पुस्तकालय, dotenv पुस्तकालय, requests पुस्तकालय, र Pillow पुस्तकालय समावेश छ।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- त्यसपछि, हामी _.env_ फाइलबाट वातावरण चरहरू लोड गर्छौं।

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

- अब, हामी चित्र उत्पादन गर्छौं:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  माथिको कोडले उत्पन्न चित्रको URL समावेश गर्ने JSON वस्तुसँग प्रतिक्रिया दिन्छ। हामी चित्र डाउनलोड गर्न र फाइलमा सुरक्षित गर्न URL प्रयोग गर्न सक्छौं।

- अन्तमा, हामी चित्र खोल्छौं र यसलाई प्रदर्शन गर्न मानक चित्र दर्शक प्रयोग गर्छौं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### चित्र उत्पादनको थप विवरण

हामी चित्र उत्पादन गर्ने कोडलाई थप विवरणमा हेर्छौं:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, चित्र उत्पादन गर्न प्रयोग गरिएको पाठ प्रम्प्ट हो। यस अवस्थामा, हामी "खरायो घोडामा, चुस्की लिएर, तुवाँलो मैदानमा जहाँ ड्याफोडिल्स उब्जन्छ" प्रम्प्ट प्रयोग गर्दैछौं।
- **size**, उत्पन्न चित्रको आकार हो। यस अवस्थामा, हामी 1024x1024 पिक्सेलको चित्र उत्पादन गर्दैछौं।
- **n**, उत्पन्न चित्रहरूको संख्या हो। यस अवस्थामा, हामी दुई चित्रहरू उत्पादन गर्दैछौं।
- **temperature**, जेनरेटिभ AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्ने प्यारामिटर हो। तापमान 0 र 1 बीचको मान हो जहाँ 0 को अर्थ हो कि उत्पादन निर्धारक हो र 1 को अर्थ हो कि उत्पादन अनियमित हो। पूर्वनिर्धारित मान 0.7 हो।

तपाईं चित्रहरूसँग गर्न सक्ने थप चीजहरू छन् जुन हामी अर्को खण्डमा समेट्नेछौं।

## चित्र उत्पादनको अतिरिक्त क्षमताहरू

तपाईंले देख्नुभयो कि हामीले कसरी केही लाइनहरूमा Python मा चित्र उत्पादन गर्न सक्षम भयौं। यद्यपि, चित्रहरूसँग गर्न सक्ने थप चीजहरू छन्।

तपाईंले निम्न गर्न पनि सक्नुहुन्छ:

- **सम्पादन गर्नुहोस्**। एक अवस्थित चित्र, मास्क र प्रम्प्ट प्रदान गरेर, तपाईं चित्रलाई परिवर्तन गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईं चित्रको एक भागमा केही थप्न सक्नुहुन्छ। हाम्रो खरायो चित्रलाई कल्पना गर्नुहोस्, तपाईं खरायोलाई टोपी थप्न सक्नुहुन्छ। तपाईंले कसरी गर्ने हो भने चित्र, मास्क (परिवर्तनको लागि क्षेत्रको भाग पहिचान गर्दै) र के गरिनु पर्छ भनेर भन्नको लागि पाठ प्रम्प्ट प्रदान गरेर गर्ने हो।

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

  आधार चित्रले मात्र खरायो समावेश गर्नेछ तर अन्तिम चित्रले खरायोमा टोपी समावेश गर्नेछ।

- **भिन्नताहरू सिर्जना गर्नुहोस्**। विचार यो हो कि तपाईं एक अवस्थित चित्र लिन्छ र भिन्नताहरू सिर्जना गर्न सोध्नुहोस्। भिन्नता सिर्जना गर्न, तपाईंले चित्र र पाठ प्रम्प्ट प्रदान गर्नुहुन्छ र यसरी कोड गर्नुहुन्छ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यो केवल OpenAI मा समर्थन गरिन्छ

## तापमान

तापमान एक प्यारामिटर हो जसले जेनरेटिभ AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्छ। तापमान 0 र 1 बीचको मान हो जहाँ 0 को अर्थ हो कि उत्पादन निर्धारक हो र 1 को अर्थ हो कि उत्पादन अनियमित हो। पूर्वनिर्धारित मान 0.7 हो।

तापमान कसरी काम गर्छ भन्ने उदाहरण हेरौं, यो प्रम्प्ट दुई पटक चलाएर:

> प्रम्प्ट : "खरायो घोडामा, चुस्की लिएर, तुवाँलो मैदानमा जहाँ ड्याफोडिल्स उब्जन्छ"

![खरायो घोडामा चुस्की लिएर, संस्करण 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ne.png)

अब त्यही प्रम्प्ट फेरि चलाउँदा हामीले उही चित्र दुई पटक प्राप्त गर्दैनौं भनेर हेर्नुहोस्:

![घोडामा खरायोको उत्पन्न चित्र](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ne.png)

जसरी तपाईं देख्न सक्नुहुन्छ, चित्रहरू समान छन्, तर उस्तै छैनन्। तापमान मान 0.1 मा परिवर्तन गरेर के हुन्छ हेर्न प्रयास गरौं:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापमान परिवर्तन गर्दै

तसर्थ, प्रतिक्रिया अधिक निर्धारक बनाउन प्रयास गरौं। हामीले उत्पन्न गरेका दुई चित्रहरूबाट अवलोकन गर्न सक्थ्यौं कि पहिलो चित्रमा खरायो छ र दोस्रो चित्रमा घोडा छ, त्यसैले चित्रहरू धेरै फरक छन्।

त्यसैले हाम्रो कोड परिवर्तन गरौं र तापमान 0 मा सेट गरौं, यसरी:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब तपाईं यो कोड चलाउनुहुन्छ, तपाईं यी दुई चित्रहरू प्राप्त गर्नुहुन्छ:

- ![तापमान 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ne.png)
- ![तापमान 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ne.png)

यहाँ तपाईं स्पष्ट रूपमा देख्न सक्नुहुन्छ कि चित्रहरू एकअर्कालाई बढी समान छन्।

## मेटाप्रम्प्टहरूद्वारा आफ्नो अनुप्रयोगको लागि सीमा कसरी परिभाषित गर्ने

हाम्रो डेमो संग, हामी पहिले नै हाम्रा ग्राहकहरूको लागि चित्रहरू उत्पादन गर्न सक्छौं। यद्यपि, हामीले हाम्रो अनुप्रयोगको लागि केही सीमाहरू सिर्जना गर्न आवश्यक छ।

उदाहरणका लागि, हामी कामको लागि सुरक्षित नभएका वा बच्चाहरूको लागि उपयुक्त नभएका चित्रहरू उत्पादन गर्न चाहँदैनौं।

हामी यो _मेटाप्रम्प्टहरू_ संग गर्न सक्छौं। मेटाप्रम्प्टहरू जेनरेटिभ AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिने पाठ प्रम्प्टहरू हुन्। उदाहरणका लागि, हामी मेटाप्रम्प्टहरू प्रयोग गरेर उत्पादनलाई नियन्त्रण गर्न सक्छौं, र सुनिश्चित गर्न सक्छौं कि उत्पन्न चित्रहरू कामको लागि सुरक्षित छन्, वा बच्चाहरूको लागि उपयुक्त छन्।

### यो कसरी काम गर्छ?

अब, मेटाप्रम्प्टहरू कसरी काम गर्छन्?

मेटाप्रम्प्टहरू जेनरेटिभ AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिने पाठ प्रम्प्टहरू हुन्, तिनीहरू पाठ प्रम्प्ट भन्दा पहिले स्थित हुन्छन्, र मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छन् र मोडेलको उत्पादनलाई नियन्त्रण गर्न अनुप्रयोगहरूमा सम्मिलित गरिन्छन्। प्रम्प्ट इनपुट र मेटाप्रम्प्ट इनपुटलाई एकल पाठ प्रम्प्टमा समेट्दै।

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

अब, हेरौं कसरी हामी हाम्रो डेमोमा मेटाप्रम्प्टहरू प्रयोग गर्न सक्छौं।

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

माथिको प्रम्प्टबाट, तपाईं देख्न सक्नुहुन्छ कि सबै उत्पन्न गरिएका चित्रहरूले मेटाप्रम्प्टलाई विचार गर्छन्।

## असाइनमेन्ट - विद्यार्थीहरूलाई सक्षम बनाऔं

हामीले यस पाठको सुरुवातमा Edu4All लाई परिचय गरायौं। अब विद्यार्थीहरूलाई आफ्ना मूल्याङ्कनहरूको लागि चित्रहरू उत्पादन गर्न सक्षम बनाउने समय हो।

विद्यार्थीहरूले आफ्नो मूल्याङ्कनहरूको लागि स्मारकहरू समावेश गर्ने चित्रहरू सिर्जना गर्नेछन्, कुन स्मारकहरू तिनीहरूमा निर्भर गर्दछ। विद्यार्थीहरूलाई यी स्मारकहरूलाई विभिन्न सन्दर्भमा राख्न यस कार्यमा आफ्नो सिर्जनात्मकता प्रयोग गर्न भनिएको छ।

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

## उत्कृष्ट काम! आफ्नो सिकाइ जारी राख्नुहोस्

यस पाठ पूरा गरेपछि, हाम्रो [जेनरेटिभ AI सिकाइ सङ्ग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् आफ्नो जेनरेटिभ AI ज्ञान स्तरवृद्धि गर्न जारी राख्न!

पाठ 10 मा जानुहोस् जहाँ हामी [कम-कोड संग AI अनुप्रयोगहरू निर्माण गर्ने](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) हेर्नेछौं।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताका लागि प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुनेछैनौं।