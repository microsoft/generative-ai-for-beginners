<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T14:03:45+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ne"
}
-->
# छविहरू निर्माण गर्ने एप्लिकेसनहरू

[![छविहरू निर्माण गर्ने एप्लिकेसनहरू](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ne.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs केवल पाठ निर्माणका लागि मात्र होइन। पाठ विवरणबाट छविहरू निर्माण गर्न पनि सम्भव छ। छविहरूको प्रयोग विभिन्न क्षेत्रहरूमा उपयोगी हुन सक्छ, जस्तै MedTech, वास्तुकला, पर्यटन, खेल विकास र अन्य। यस अध्यायमा, हामी दुई लोकप्रिय छवि निर्माण मोडेलहरू, DALL-E र Midjourney, को बारेमा चर्चा गर्नेछौं।

## परिचय

यस पाठमा, हामी निम्न विषयहरू समेट्नेछौं:

- छवि निर्माण र यसको उपयोगिता।
- DALL-E र Midjourney, के हुन् र कसरी काम गर्छन्।
- छवि निर्माण एप्लिकेसन कसरी बनाउने।

## सिक्ने लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं सक्षम हुनुहुनेछ:

- छवि निर्माण एप्लिकेसन बनाउने।
- मेटा प्रम्प्टहरू प्रयोग गरेर आफ्नो एप्लिकेसनको सीमा निर्धारण गर्ने।
- DALL-E र Midjourney सँग काम गर्ने।

## किन छवि निर्माण एप्लिकेसन बनाउने?

छवि निर्माण एप्लिकेसनहरू Generative AI को क्षमता अन्वेषण गर्ने उत्कृष्ट तरिका हुन्। तिनीहरू निम्न कार्यहरूको लागि प्रयोग गर्न सकिन्छ:

- **छवि सम्पादन र संश्लेषण**। तपाईं विभिन्न प्रयोजनहरूको लागि छविहरू निर्माण गर्न सक्नुहुन्छ, जस्तै छवि सम्पादन र छवि संश्लेषण।

- **विभिन्न उद्योगहरूमा लागू**। तिनीहरू MedTech, पर्यटन, खेल विकास र अन्य जस्ता विभिन्न उद्योगहरूको लागि छविहरू निर्माण गर्न प्रयोग गर्न सकिन्छ।

## परिदृश्य: Edu4All

यस पाठको भागको रूपमा, हामी हाम्रो स्टार्टअप, Edu4All, सँग काम जारी राख्नेछौं। विद्यार्थीहरूले आफ्नो मूल्याङ्कनका लागि छविहरू निर्माण गर्नेछन्। कुन प्रकारका छविहरू निर्माण गर्ने भन्ने कुरा विद्यार्थीहरूको निर्णयमा निर्भर हुनेछ। उनीहरूले आफ्नै परीकथाको लागि चित्रणहरू बनाउन सक्दछन्, नयाँ पात्र सिर्जना गर्न सक्दछन्, वा आफ्ना विचार र अवधारणाहरूलाई दृश्यात्मक बनाउन मद्दत गर्न सक्दछन्।

यहाँ Edu4All का विद्यार्थीहरूले कक्षामा स्मारकहरूमा काम गरिरहेको अवस्थामा निर्माण गर्न सक्ने उदाहरण छ:

![Edu4All स्टार्टअप, स्मारकहरूको कक्षा, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ne.png)

प्रम्प्ट प्रयोग गर्दै:

> "कुकुर Eiffel Tower को छेउमा बिहानको घामको प्रकाशमा"

## DALL-E र Midjourney के हुन्?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) र [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दुई लोकप्रिय छवि निर्माण मोडेलहरू हुन्। तिनीहरूले प्रम्प्टहरू प्रयोग गरेर छविहरू निर्माण गर्न अनुमति दिन्छन्।

### DALL-E

DALL-E बाट सुरु गरौं, जुन एक Generative AI मोडेल हो जसले पाठ विवरणहरूबाट छविहरू निर्माण गर्छ।

> [DALL-E दुई मोडेलहरूको संयोजन हो, CLIP र diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एउटा मोडेल हो जसले छविहरू र पाठबाट संख्यात्मक प्रतिनिधित्वहरू (embeddings) निर्माण गर्छ।

- **Diffused attention**, एउटा मोडेल हो जसले embeddings बाट छविहरू निर्माण गर्छ। DALL-E छविहरू र पाठको डेटासेटमा प्रशिक्षित छ र पाठ विवरणहरूबाट छविहरू निर्माण गर्न प्रयोग गर्न सकिन्छ। उदाहरणका लागि, DALL-E ले टोपी लगाएको बिरालो वा मोहक कपाल भएको कुकुरको छवि निर्माण गर्न सक्छ।

### Midjourney

Midjourney DALL-E जस्तै काम गर्छ। यो पाठ प्रम्प्टहरू प्रयोग गरेर छविहरू निर्माण गर्छ। Midjourney ले "टोपी लगाएको बिरालो" वा "मोहक कपाल भएको कुकुर" जस्ता प्रम्प्टहरू प्रयोग गरेर छविहरू निर्माण गर्न सक्दछ।

![Midjourney द्वारा निर्माण गरिएको छवि, यान्त्रिक परेवा](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_छवि स्रोत Wikipedia, Midjourney द्वारा निर्माण गरिएको छवि_

## DALL-E र Midjourney कसरी काम गर्छन्

पहिले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एक Generative AI मोडेल हो जुन _transformer architecture_ मा आधारित छ र _autoregressive transformer_ प्रयोग गर्छ।

_autoregressive transformer_ ले मोडेलले पाठ विवरणहरूबाट छविहरू कसरी निर्माण गर्छ भन्ने परिभाषित गर्छ। यो एक पटकमा एक पिक्सेल निर्माण गर्छ, र त्यसपछि निर्माण गरिएको पिक्सेलहरू प्रयोग गरेर अर्को पिक्सेल निर्माण गर्छ। यो प्रक्रिया neural network का विभिन्न तहहरूबाट पार हुन्छ, जबसम्म छवि पूरा हुँदैन।

यस प्रक्रियासँग, DALL-E ले निर्माण गरिएको छविमा विशेषताहरू, वस्तुहरू, विशेषताहरू र अन्य कुराहरू नियन्त्रण गर्छ। तर, DALL-E 2 र 3 ले निर्माण गरिएको छविमा अझ बढी नियन्त्रण प्रदान गर्छ।

## आफ्नो पहिलो छवि निर्माण एप्लिकेसन बनाउने

छवि निर्माण एप्लिकेसन बनाउन के चाहिन्छ? तपाईंलाई निम्न पुस्तकालयहरू चाहिन्छ:

- **python-dotenv**, तपाईंलाई आफ्नो गोप्य जानकारी _.env_ फाइलमा राख्न सिफारिस गरिन्छ।
- **openai**, यो पुस्तकालय OpenAI API सँग अन्तरक्रिया गर्न प्रयोग गरिन्छ।
- **pillow**, Python मा छविहरूसँग काम गर्न।
- **requests**, HTTP अनुरोधहरू गर्न मद्दत गर्न।

## Azure OpenAI मोडेल सिर्जना र परिनियोजन गर्नुहोस्

यदि पहिले गरिएको छैन भने, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पृष्ठमा निर्देशनहरू पालना गर्नुहोस्
Azure OpenAI स्रोत र मोडेल सिर्जना गर्न। DALL-E 3 लाई मोडेलको रूपमा चयन गर्नुहोस्।  

## एप्लिकेसन बनाउनुहोस्

1. _.env_ नामक फाइल सिर्जना गर्नुहोस् निम्न सामग्रीसहित:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Azure OpenAI Foundry Portal मा आफ्नो स्रोतको "Deployments" खण्डमा यो जानकारी पत्ता लगाउनुहोस्।

1. माथिका पुस्तकालयहरू _requirements.txt_ नामक फाइलमा संकलन गर्नुहोस्:

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

   Windows को लागि, भर्चुअल वातावरण सिर्जना र सक्रिय गर्न निम्न आदेशहरू प्रयोग गर्नुहोस्:

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

यस कोडलाई व्याख्या गरौं:

- पहिलो, हामीलाई चाहिने पुस्तकालयहरू आयात गर्छौं, जस्तै OpenAI पुस्तकालय, dotenv पुस्तकालय, requests पुस्तकालय, र Pillow पुस्तकालय।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- त्यसपछि, हामी _.env_ फाइलबाट वातावरणीय चरहरू लोड गर्छौं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यसपछि, हामी Azure OpenAI सेवा क्लाइन्टलाई कन्फिगर गर्छौं।

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- त्यसपछि, हामी छवि निर्माण गर्छौं:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  माथिको कोडले निर्माण गरिएको छविको URL समावेश गर्ने JSON वस्तुमा प्रतिक्रिया दिन्छ। हामी यो URL प्रयोग गरेर छवि डाउनलोड गर्न र फाइलमा बचत गर्न सक्छौं।

- अन्तमा, हामी छवि खोल्छौं र मानक छवि दर्शक प्रयोग गरेर प्रदर्शन गर्छौं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### छवि निर्माणको थप विवरण

छवि निर्माण गर्ने कोडलाई थप विवरणमा हेरौं:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, छवि निर्माण गर्न प्रयोग गरिएको पाठ प्रम्प्ट हो। यस अवस्थामा, हामी "घोडामा खरायो, ललिपप समातेको, कुहिरो मैदानमा जहाँ डाफोडिलहरू उम्रन्छन्" प्रम्प्ट प्रयोग गर्दैछौं।
- **size**, निर्माण गरिएको छविको आकार हो। यस अवस्थामा, हामी 1024x1024 पिक्सेलको छवि निर्माण गर्दैछौं।
- **n**, निर्माण गरिएका छविहरूको संख्या हो। यस अवस्थामा, हामी दुई छविहरू निर्माण गर्दैछौं।
- **temperature**, एक प्यारामिटर हो जसले Generative AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्छ। तापक्रम 0 देखि 1 सम्मको मान हो जहाँ 0 ले उत्पादन निर्धारणात्मक छ र 1 ले उत्पादन अनियमित छ भन्ने जनाउँछ। डिफल्ट मान 0.7 हो।

छविहरूसँग गर्न सकिने थप कुराहरू हामी अर्को खण्डमा समेट्नेछौं।

## छवि निर्माणको अतिरिक्त क्षमता

तपाईंले अहिलेसम्म देख्नुभएको छ कि हामीले Python मा केही लाइनहरू प्रयोग गरेर छवि निर्माण गर्न सक्षम भएका छौं। तर, छविहरूसँग गर्न सकिने थप कुराहरू छन्।

तपाईं निम्न कार्यहरू पनि गर्न सक्नुहुन्छ:

- **सम्पादन गर्नुहोस्**। एउटा विद्यमान छवि, मास्क र प्रम्प्ट प्रदान गरेर, तपाईं छविमा परिवर्तन गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईं छविको कुनै भागमा केही थप्न सक्नुहुन्छ। हाम्रो खरायो छविको कल्पना गर्नुहोस्, तपाईं खरायोमा टोपी थप्न सक्नुहुन्छ। तपाईंले यो कसरी गर्ने भनेको छवि, मास्क (परिवर्तनको क्षेत्र पहिचान गर्ने) र पाठ प्रम्प्ट प्रदान गरेर हो। 
> नोट: यो DALL-E 3 मा समर्थित छैन। 
 
यहाँ GPT Image प्रयोग गरेर एउटा उदाहरण छ:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  आधार छविमा केवल पूलसहितको लाउन्ज हुनेछ तर अन्तिम छविमा फ्लेमिंगो हुनेछ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ne.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ne.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ne.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **भिन्नताहरू सिर्जना गर्नुहोस्**। विचार यो हो कि तपाईं एउटा विद्यमान छवि लिन्छन् र सो छविको विभिन्न संस्करणहरू सिर्जना गर्न अनुरोध गर्नुहोस्। भिन्नता सिर्जना गर्न, तपाईंले छवि र पाठ प्रम्प्ट प्रदान गर्नुहोस् र यस्तो कोड प्रयोग गर्नुहोस्:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > नोट, यो केवल OpenAI मा समर्थित छ।

## तापक्रम

तापक्रम एक प्यारामिटर हो जसले Generative AI मोडेलको उत्पादनको अनियमितता नियन्त्रण गर्छ। तापक्रम 0 देखि 1 सम्मको मान हो जहाँ 0 ले उत्पादन निर्धारणात्मक छ र 1 ले उत्पादन अनियमित छ भन्ने जनाउँछ। डिफल्ट मान 0.7 हो।

तापक्रम कसरी काम गर्छ भन्ने उदाहरण हेरौं, यो प्रम्प्ट दुई पटक चलाएर:

> प्रम्प्ट : "घोडामा खरायो, ललिपप समातेको, कुहिरो मैदानमा जहाँ डाफोडिलहरू उम्रन्छन्"

![घोडामा खरायो ललिपप समातेको, संस्करण 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ne.png)

अब त्यही प्रम्प्ट फेरि चलाउँदा हेर्नुहोस् कि हामीले दुई पटक एउटै छवि प्राप्त गर्दैनौं:

![घोडामा खरायोको निर्माण गरिएको छवि](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ne.png)

जस्तो देखिन्छ, छविहरू समान छन्, तर उस्तै छैनन्। अब तापक्रम मानलाई 0.1 मा परिवर्तन गरौं र के हुन्छ हेर्नुहोस्:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### तापक्रम परिवर्तन गर्दै

अब प्रतिक्रिया अझ निर्धारणात्मक बनाउन प्रयास गरौं। हामीले निर्माण गरेका दुई छविहरूबाट देख्न सक्थ्यौं कि पहिलो छविमा खरायो छ र दोस्रो छविमा घोडा छ, त्यसैले छविहरू धेरै फरक छन्।

त्यसैले, हाम्रो कोड परिवर्तन गरौं र तापक्रमलाई 0 मा सेट गरौं, यस्तो:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब जब तपाईं यो कोड चलाउनुहुन्छ, तपाईंले यी दुई छविहरू प्राप्त गर्नुहुनेछ:

- ![तापक्रम 0, संस्करण 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ne.png)
- ![तापक्रम 0, संस्करण 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ne.png)

यहाँ तपाईं स्पष्ट रूपमा देख्न सक्नुहुन्छ कि छविहरू एक अर्कासँग धेरै मिल्दोजुल्दो छन्।

## मेटा प्रम्प्टहरू प्रयोग गरेर आफ्नो एप्लिकेसनको सीमा कसरी निर्धारण गर्ने

हाम्रो डेमोको साथ, हामी पहिले नै हाम्रो ग्राहकहरूको लागि छविहरू निर्माण गर्न सक्छौं। तर, हामीले हाम्रो एप्लिकेसनको लागि केही सीमा सिर्जना गर्न आवश्यक छ।

उदाहरणका लागि, हामी कामको लागि सुरक्षित नभएका छविहरू वा बच्चाहरूको लागि उपयुक्त नभएका छविहरू निर्माण गर्न चाहँदैनौं।

हामी यो _मेटा प्रम्प्टहरू_ प्रयोग गरेर गर्न सक्छौं। मेटा प्रम्प्टहरू पाठ प्रम्प्टहरू हुन् जसले Generative AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ। उदाहरणका लागि, हामी मेटा प्रम्प्टहरू प्रयोग गरेर उत्पादनलाई नियन्त्रण गर्न सक्छौं, र सुनिश्चित गर्न सक्छौं कि निर्माण गरिएका छविहरू कामको लागि सुरक्षित छन् वा बच्चाहरूको लागि उपयुक्त छन्।

### यो कसरी काम गर्छ?

अब, मेटा प्रम्प्टहरू कसरी काम गर्छन्?

मेटा प्रम्प्टहरू पाठ प्रम्प्टहरू हुन् जसले Generative AI मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ। तिनीहरू पाठ प्रम्प्टको अगाडि राखिन्छन्, र मोडेलको उत्पादनलाई नियन्त्रण गर्न प्रयोग गरिन्छ। मेटा प्रम्प्ट इनपुट र प्रम्प्ट इनपुटलाई एकल पाठ प्रम्प्टमा समेटेर एप्लिकेसनहरूमा समावेश गरिन्छ।

मेटा प्रम्प्टको एउटा उदाहरण निम्न हुनेछ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, हाम्रा डेमोमा मेटा प्रम्प्टहरू कसरी प्रयोग गर्न सकिन्छ हेर्नुहोस्।

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

माथिको प्रम्प्टबाट, तपाईं देख्न सक्नुहुन्छ कि निर्माण गरिएका सबै छविहरूले मेटा प्रम्प्टलाई विचार गर्छन्।

## असाइनमेन्ट - विद्यार्थीहरूलाई सक्षम बनाऔं

हामीले यस पाठको सुरुमा Edu4All प्रस्तुत गरेका थियौं। अब समय आएको छ कि विद्यार्थीहरूलाई आफ्नो मूल्याङ्कनका लागि छविहरू निर्माण गर्न सक्षम बनाउने।

विद्यार्थीहरूले आफ्नो मूल्याङ्कनका लागि स्मारकहरू समावेश गर्ने छविहरू निर्माण गर्नेछन्। कुन स्मारकहरू समावेश गर्ने भन्ने कुरा विद्यार्थीहरूको निर्णयमा निर्भर हुनेछ। विद्यार्थीहरूलाई यस कार्यमा आफ्नो रचनात्मकता प्रयोग गर्न अनुरोध गरिएको छ ताकि तिनीहरूले यी स्मारकहरूलाई विभिन्न सन्दर्भहरूमा राख्न सकून्।

## समाधान

यहाँ एउटा सम्भावित समाधान:
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

## उत्कृष्ट काम! आफ्नो सिकाइ जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञानलाई अझ उचाइमा पुर्‍याउनुहोस्!

पाठ १० मा जानुहोस् जहाँ हामी [कम-कोडको साथ AI एप्लिकेसन निर्माण गर्ने](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) बारेमा हेर्नेछौं।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।