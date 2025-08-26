<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:59:01+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ne"
}
-->
# इमेज जेनेरेशन एप्लिकेशनहरू बनाउने

[![इमेज जेनेरेशन एप्लिकेशनहरू बनाउने](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ne.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM हरू केवल पाठ उत्पादनका लागि मात्र होइनन्। तपाईंले पाठ विवरणबाट पनि तस्बिरहरू बनाउन सक्नुहुन्छ। तस्बिरहरू एउटा modality को रूपमा हुनु धेरै क्षेत्रहरूमा उपयोगी हुन सक्छ, जस्तै MedTech, वास्तुकला, पर्यटन, गेम विकास आदि। यस अध्यायमा, हामी दुई सबैभन्दा लोकप्रिय इमेज जेनेरेशन मोडेलहरू, DALL-E र Midjourney, को बारेमा हेर्नेछौं।

## परिचय

यस पाठमा, हामी यी विषयहरू समेट्नेछौं:

- इमेज जेनेरेशन के हो र किन उपयोगी छ।
- DALL-E र Midjourney के हुन्, र कसरी काम गर्छन्।
- तपाईंले कसरी इमेज जेनेरेशन एप्लिकेशन बनाउने।

## सिकाइका उद्देश्यहरू

यो पाठ पूरा गरेपछि, तपाईंले गर्न सक्नुहुन्छ:

- एउटा इमेज जेनेरेशन एप्लिकेशन बनाउने।
- आफ्नो एप्लिकेशनका लागि meta prompts प्रयोग गरेर सीमा निर्धारण गर्ने।
- DALL-E र Midjourney सँग काम गर्ने।

## किन इमेज जेनेरेशन एप्लिकेशन बनाउने?

इमेज जेनेरेशन एप्लिकेशनहरू Generative AI को क्षमताहरू अन्वेषण गर्नको लागि उत्कृष्ट तरिका हुन्। यी विभिन्न प्रयोजनका लागि प्रयोग गर्न सकिन्छ, जस्तै:

- **इमेज सम्पादन र synthesis**। तपाईंले विभिन्न प्रयोजनका लागि तस्बिरहरू बनाउन सक्नुहुन्छ, जस्तै तस्बिर सम्पादन र synthesis।

- **विभिन्न उद्योगहरूमा प्रयोग**। यी एप्लिकेशनहरू Medtech, पर्यटन, गेम विकास जस्ता विभिन्न उद्योगहरूमा तस्बिरहरू बनाउन प्रयोग गर्न सकिन्छ।

## परिदृश्य: Edu4All

यस पाठको भागको रूपमा, हामी हाम्रो स्टार्टअप Edu4All सँग काम गर्न जारी राख्नेछौं। विद्यार्थीहरूले आफ्नो मूल्याङ्कनका लागि तस्बिरहरू बनाउनेछन्, कुन तस्बिर बनाउने भन्ने कुरा विद्यार्थीहरूकै जिम्मामा हुनेछ, जस्तै आफ्नै परीकथाका लागि चित्रण, नयाँ पात्र सिर्जना, वा आफ्ना विचार र अवधारणाहरू visualization गर्न।

यहाँ एउटा उदाहरण छ, यदि Edu4All का विद्यार्थीहरूले कक्षामा स्मारकहरूमा काम गरिरहेका छन् भने:

![Edu4All स्टार्टअप, स्मारकहरूको कक्षा, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ne.png)

यसरी prompt प्रयोग गरेर

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-E र Midjourney के हुन्?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) र [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) दुई सबैभन्दा लोकप्रिय इमेज जेनेरेशन मोडेलहरू हुन्, जसले तपाईंलाई prompt प्रयोग गरेर तस्बिरहरू बनाउन दिन्छ।

### DALL-E

DALL-E बाट सुरु गरौं, यो एउटा Generative AI मोडेल हो जसले पाठ विवरणबाट तस्बिरहरू बनाउँछ।

> [DALL-E दुई मोडेलहरूको संयोजन हो, CLIP र diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, एउटा मोडेल हो जसले तस्बिर र पाठबाट embedding (संख्यात्मक प्रतिनिधित्व) बनाउँछ।

- **Diffused attention**, एउटा मोडेल हो जसले embedding बाट तस्बिर बनाउँछ। DALL-E लाई तस्बिर र पाठको dataset मा तालिम दिइएको छ र यसले पाठ विवरणबाट तस्बिर बनाउन सक्छ। उदाहरणका लागि, DALL-E ले टोपी लगाएको बिरालो, वा mohawk भएको कुकुरको तस्बिर बनाउन सक्छ।

### Midjourney

Midjourney पनि DALL-E जस्तै काम गर्छ, यसले text prompt बाट तस्बिर बनाउँछ। Midjourney मा पनि तपाईंले “a cat in a hat” वा “dog with a mohawk” जस्ता prompt प्रयोग गरेर तस्बिर बनाउन सक्नुहुन्छ।

![Midjourney द्वारा बनाइएको तस्बिर, मेकानिकल परेवा](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_छवि स्रोत Wikipedia, तस्बिर Midjourney द्वारा बनाइएको_

## DALL-E र Midjourney कसरी काम गर्छन्

पहिले, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E एउटा Generative AI मोडेल हो जुन transformer architecture मा आधारित छ, जसमा _autoregressive transformer_ प्रयोग गरिएको छ।

_autoregressive transformer_ ले मोडेलले कसरी पाठ विवरणबाट तस्बिर बनाउँछ भन्ने कुरा निर्धारण गर्छ, यसले एक पटकमा एक पिक्सेल बनाउँछ, अनि बनेका पिक्सेलहरू प्रयोग गरेर अर्को पिक्सेल बनाउँछ। यो प्रक्रिया neural network का धेरै तहहरू हुँदै जान्छ, जबसम्म तस्बिर पूरा हुँदैन।

यस प्रक्रियाबाट, DALL-E ले तस्बिरमा attributes, objects, characteristics आदि नियन्त्रण गर्न सक्छ। तर, DALL-E 2 र 3 मा अझ बढी नियन्त्रण गर्न सकिन्छ।

## आफ्नो पहिलो इमेज जेनेरेशन एप्लिकेशन बनाउने

एउटा इमेज जेनेरेशन एप्लिकेशन बनाउन के चाहिन्छ? तपाईंलाई यी लाइब्रेरीहरू चाहिन्छ:

- **python-dotenv**, तपाईंको गोप्य जानकारी _.env_ फाइलमा राख्नका लागि यो लाइब्रेरी प्रयोग गर्न सिफारिस गरिन्छ।
- **openai**, OpenAI API सँग अन्तरक्रिया गर्नका लागि यो लाइब्रेरी प्रयोग हुन्छ।
- **pillow**, Python मा तस्बिरहरूसँग काम गर्नका लागि।
- **requests**, HTTP अनुरोध गर्नका लागि।

## Azure OpenAI मोडेल सिर्जना र डिप्लोय गर्नुहोस्

यदि पहिले गरिसक्नु भएको छैन भने, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) पृष्ठको निर्देशनहरू पालना गर्नुहोस्
Azure OpenAI resource र मोडेल सिर्जना गर्न। मोडेलको रूपमा DALL-E 3 चयन गर्नुहोस्।  

## एप बनाउनुहोस्

1. _.env_ नामको फाइलमा तलको सामग्री राख्नुहोस्:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   यो जानकारी Azure OpenAI Foundry Portal मा तपाईंको resource को "Deployments" सेक्सनमा पाउन सकिन्छ।

1. माथिका लाइब्रेरीहरू _requirements.txt_ नामको फाइलमा यसरी राख्नुहोस्:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. अब, virtual environment बनाउनुहोस् र लाइब्रेरीहरू इन्स्टल गर्नुहोस्:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows को लागि, virtual environment बनाउन र सक्रिय गर्न तलका कमाण्डहरू प्रयोग गर्नुहोस्:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ नामको फाइलमा तलको कोड राख्नुहोस्:

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

यो कोड के गर्छ भन्ने कुरा बुझौं:

- सुरुमा, हामीलाई चाहिने लाइब्रेरीहरू import गर्छौं, जसमध्ये OpenAI, dotenv, requests, र Pillow लाइब्रेरी छन्।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- त्यसपछि, _.env_ फाइलबाट environment variables लोड गर्छौं।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- त्यसपछि, Azure OpenAI service client configure गर्छौं

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- अब, तस्बिर generate गर्छौं:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  माथिको कोडले generated image को URL भएको JSON object फर्काउँछ। हामीले त्यो URL प्रयोग गरेर तस्बिर डाउनलोड गर्न र फाइलमा सुरक्षित गर्न सक्छौं।

- अन्त्यमा, तस्बिर खोल्छौं र standard image viewer मा देखाउँछौं:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### तस्बिर generate गर्ने कोडको थप विवरण

अब तस्बिर generate गर्ने कोडलाई विस्तारमा हेरौं:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, त्यो पाठ हो जसको आधारमा तस्बिर बनाइन्छ। यहाँ हामी "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" prompt प्रयोग गर्दैछौं।
- **size**, बनाइने तस्बिरको साइज हो। यहाँ 1024x1024 pixels को तस्बिर बनाइँदैछ।
- **n**, बनाइने तस्बिरहरूको संख्या हो। यहाँ दुईवटा तस्बिर बनाइँदैछ।
- **temperature**, यो parameter ले Generative AI मोडेलको output कति random हुने भन्ने नियन्त्रण गर्छ। temperature 0 देखि 1 सम्मको मान हो, जहाँ 0 ले deterministic output दिन्छ र 1 ले random output दिन्छ। default मान 0.7 हो।

तस्बिरहरूसँग अझ धेरै कुरा गर्न सकिन्छ, जुन हामी अर्को खण्डमा हेर्नेछौं।

## इमेज जेनेरेशनका थप क्षमताहरू

अहिलेसम्म तपाईंले देख्नुभयो, केही लाइन Python कोडले तस्बिर बनाउन सकिन्छ। तर, तस्बिरहरूसँग अझ धेरै कुरा गर्न सकिन्छ।

तपाईंले यी कामहरू पनि गर्न सक्नुहुन्छ:

- **सम्पादन गर्नुहोस्**। पहिलेको तस्बिर, एउटा mask र prompt दिएर तस्बिर परिवर्तन गर्न सकिन्छ। उदाहरणका लागि, तपाईंले तस्बिरको कुनै भागमा केही थप्न सक्नुहुन्छ। हाम्रो bunny तस्बिरमा, तपाईंले bunny लाई टोपी थप्न सक्नुहुन्छ। यसका लागि तस्बिर, mask (परिवर्तन गर्नुपर्ने भाग चिनाउने) र के गर्नुपर्छ भन्ने text prompt दिनुपर्छ।
> Note: यो DALL-E 3 मा समर्थित छैन। 
 
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

  base image मा केवल lounge with pool हुनेछ, तर अन्तिम तस्बिरमा flamingo थपिएको हुनेछ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **भिन्नता बनाउनुहोस्**। यसको अर्थ, तपाईंले पहिलेको तस्बिर लिएर त्यसको भिन्नता बनाउन भन्न सक्नुहुन्छ। भिन्नता बनाउन, तस्बिर र text prompt दिनुपर्छ र यसरी कोड लेख्नुपर्छ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note, यो केवल OpenAI मा मात्र समर्थित छ

## Temperature

Temperature एउटा parameter हो जसले Generative AI मोडेलको output कति random हुने भन्ने निर्धारण गर्छ। temperature 0 देखि 1 सम्मको मान हो, जहाँ 0 ले deterministic output दिन्छ र 1 ले random output दिन्छ। default मान 0.7 हो।

temperature कसरी काम गर्छ भन्ने बुझ्नका लागि, यो prompt दुई पटक चलाउँदा:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ne.png)

अब त्यही prompt फेरि चलाउँदा, तपाईंले देख्नुहुन्छ कि एउटै तस्बिर फेरि आउँदैन:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ne.png)

यहाँ देख्न सकिन्छ, तस्बिरहरू मिल्दोजुल्दो छन्, तर एउटै छैनन्। अब temperature को मान 0.1 मा परिवर्तन गरेर हेरौं:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature परिवर्तन गर्दै

अब response अझ deterministic बनाउन प्रयास गरौं। हामीले बनाएका दुई तस्बिरहरूमा, पहिलोमा bunny छ, दोस्रोमा घोडा छ, तस्बिरहरू धेरै फरक छन्।

अब हाम्रो कोडमा temperature 0 राखौं:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

अब यो कोड चलाउँदा, तपाईंले यी दुई तस्बिरहरू पाउनुहुन्छ:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ne.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ne.png)

यहाँ स्पष्ट देख्न सकिन्छ, तस्बिरहरू एकअर्कासँग धेरै मिल्दोजुल्दो छन्।

## आफ्नो एप्लिकेशनका लागि सीमा कसरी निर्धारण गर्ने (metaprompts प्रयोग गरेर)

हाम्रो डेमोमा, हामीले पहिले नै आफ्ना ग्राहकका लागि तस्बिरहरू बनाउन सक्छौं। तर, एप्लिकेशनका लागि केही सीमा तोक्न आवश्यक छ।

उदाहरणका लागि, हामीले कामका लागि अनुपयुक्त, वा बच्चाहरूका लागि उपयुक्त नभएका तस्बिरहरू बनाउन चाहँदैनौं।

यो _metaprompts_ प्रयोग गरेर गर्न सकिन्छ। Metaprompts त्यस्ता text prompts हुन्, जसले Generative AI मोडेलको output नियन्त्रण गर्छ। उदाहरणका लागि, metaprompts प्रयोग गरेर सुनिश्चित गर्न सकिन्छ कि बनाइएका तस्बिरहरू कामका लागि सुरक्षित छन्, वा बच्चाहरूका लागि उपयुक्त छन्।

### यो कसरी काम गर्छ?

अब, meta prompts कसरी काम गर्छन्?

Meta prompts त्यस्ता text prompts हुन्, जसले Generative AI मोडेलको output नियन्त्रण गर्छन्, यी prompt भन्दा अगाडि राखिन्छन्, र मोडेलको output नियन्त्रण गर्न प्रयोग गरिन्छन्। एप्लिकेशनमा prompt input र meta prompt input एउटै text prompt मा encapsulate गरिन्छ।

Meta prompt को एउटा उदाहरण यस्तो हुन सक्छ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

अब, हेरौं कसरी हाम्रो डेमोमा meta prompts प्रयोग गर्न सकिन्छ।

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

माथिको prompt बाट देख्न सकिन्छ, सबै बनाइएका तस्बिरहरूले metaprompt लाई ध्यानमा राख्छन्।

## अभ्यास - विद्यार्थीहरूलाई सक्षम बनाऔं

हामीले यो पाठको सुरुमा Edu4All को परिचय गराएका थियौं। अब विद्यार्थीहरूलाई आफ्नो मूल्याङ्कनका लागि तस्बिर बनाउन सक्षम बनाउने समय आएको छ।

विद्यार्थीहरूले आफ्नो मूल्याङ्कनका लागि स्मारकहरू भएका तस्बिरहरू बनाउनेछन्, कुन स्मारक बनाउने भन्ने कुरा विद्यार्थीहरूकै जिम्मामा हुनेछ। विद्यार्थीहरूलाई यो कार्यमा आफ्नो सिर्जनशीलता प्रयोग गर्न भनिएको छ, र ती स्मारकहरूलाई विभिन्न सन्दर्भमा राख्न भनिएको छ।

## समाधान

यहाँ एउटा सम्भावित समाधान छ:

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

## राम्रो काम! आफ्नो सिकाइ जारी राख्नुहोस्
यो पाठ समाप्त गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञान अझ बढाउनुहोस्!

अब पाठ १० तिर जानुहोस् जहाँ हामी [कम कोड प्रयोग गरेर AI एप्लिकेसन कसरी बनाउने](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) भन्ने कुरा हेर्नेछौं।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलत बुझाइ वा व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।