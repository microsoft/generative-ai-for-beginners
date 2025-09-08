<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:52:25+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ne"
}
-->
# टेक्स्ट जेनेरेसन एप्लिकेसनहरू बनाउने

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ne.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(यो पाठको भिडियो हेर्न माथिको तस्बिरमा क्लिक गर्नुहोस्)_

यस पाठ्यक्रममा अहिलेसम्म तपाईंले देख्नुभएको छ कि प्रॉम्प्टहरू जस्ता आधारभूत अवधारणाहरू छन् र एउटा पूरा विषय क्षेत्र नै "प्रॉम्प्ट इन्जिनियरिङ" भनिन्छ। तपाईंले जस्तै ChatGPT, Office 365, Microsoft Power Platform लगायतका धेरै उपकरणहरूसँग प्रॉम्प्टहरू प्रयोग गरेर कुराकानी गर्न सक्नुहुन्छ र केही काम पूरा गर्न सक्नुहुन्छ।

एउटा एप्लिकेसनमा यस्तो अनुभव थप्नका लागि, तपाईंले प्रॉम्प्ट, कम्प्लिशनहरू जस्ता अवधारणाहरू बुझ्नुपर्छ र काम गर्नको लागि एउटा लाइब्रेरी छान्नुपर्छ। यो नै तपाईंले यस अध्यायमा सिक्ने कुरा हो।

## परिचय

यस अध्यायमा, तपाईंले:

- openai लाइब्रेरी र यसको मुख्य अवधारणाहरूको बारेमा सिक्नुहुनेछ।
- openai प्रयोग गरेर टेक्स्ट जेनेरेसन एप्लिकेसन बनाउनुहुनेछ।
- प्रॉम्प्ट, टेम्परेचर, र टोकनहरू जस्ता अवधारणाहरू कसरी प्रयोग गर्ने भनेर बुझ्नुहुनेछ।

## सिकाइका लक्ष्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- टेक्स्ट जेनेरेसन एप्लिकेसन के हो भनेर व्याख्या गर्न।
- openai प्रयोग गरेर टेक्स्ट जेनेरेसन एप्लिकेसन बनाउन।
- आफ्नो एप्लिकेसनलाई बढी वा कम टोकनहरू प्रयोग गर्न र टेम्परेचर परिवर्तन गर्न कन्फिगर गर्न, जसले फरक-फरक नतिजा दिन्छ।

## टेक्स्ट जेनेरेसन एप्लिकेसन के हो?

सामान्यतया जब तपाईं एप्लिकेसन बनाउनुहुन्छ, त्यसमा केही प्रकारको इन्टरफेस हुन्छ, जस्तै:

- कमाण्ड-आधारित। कन्सोल एपहरू त्यस्ता एपहरू हुन् जहाँ तपाईं कमाण्ड टाइप गर्नुहुन्छ र त्यो काम पूरा गर्छ। उदाहरणका लागि, `git` एउटा कमाण्ड-आधारित एप हो।
- प्रयोगकर्ता इन्टरफेस (UI)। केही एपहरूमा ग्राफिकल यूजर इन्टरफेस (GUI) हुन्छ जहाँ तपाईं बटन क्लिक गर्नुहुन्छ, टेक्स्ट इनपुट गर्नुहुन्छ, विकल्पहरू छान्नुहुन्छ आदि।

### कन्सोल र UI एपहरू सीमित छन्

कमाण्ड-आधारित एपसँग तुलना गर्दा जहाँ तपाईं कमाण्ड टाइप गर्नुहुन्छ:

- **सीमित हुन्छ**। तपाईं जुनसुकै कमाण्ड टाइप गर्न सक्नुहुन्न, केवल ती कमाण्डहरू जुन एपले समर्थन गर्छ।
- **भाषा विशेष**। केही एपहरूले धेरै भाषाहरू समर्थन गर्छन्, तर डिफल्टमा एप एउटा विशेष भाषाका लागि बनाइएको हुन्छ, यद्यपि तपाईं थप भाषा समर्थन थप्न सक्नुहुन्छ।

### टेक्स्ट जेनेरेसन एपहरूको फाइदा

टेक्स्ट जेनेरेसन एप कसरी फरक हुन्छ?

टेक्स्ट जेनेरेसन एपमा तपाईंलाई बढी लचिलोपन हुन्छ, तपाईं कमाण्डहरूको सेट वा विशेष इनपुट भाषामा सीमित हुनुहुन्न। यसको सट्टा, तपाईं प्राकृतिक भाषामा एपसँग कुराकानी गर्न सक्नुहुन्छ। अर्को फाइदा भनेको तपाईं पहिले नै ठूलो मात्रामा जानकारीमा प्रशिक्षित डाटास्रोतसँग अन्तरक्रिया गर्दै हुनुहुन्छ, जबकि परम्परागत एपहरू डेटाबेसमा भएका कुरामा सीमित हुन सक्छन्।

### टेक्स्ट जेनेरेसन एपबाट के के बनाउन सकिन्छ?

धेरै कुरा बनाउन सकिन्छ। उदाहरणका लागि:

- **च्याटबोट**। कम्पनी र यसको उत्पादनहरूबारे प्रश्नहरूको उत्तर दिने च्याटबोट राम्रो विकल्प हुन सक्छ।
- **सहायक**। LLM हरू जस्तै टेक्स्ट सारांश गर्ने, टेक्स्टबाट जानकारी निकाल्ने, रिजुमे जस्ता टेक्स्ट उत्पादन गर्ने काममा उत्कृष्ट हुन्छन्।
- **कोड सहायक**। तपाईंले प्रयोग गर्ने भाषा मोडेल अनुसार, तपाईं कोड लेख्न सहयोग गर्ने कोड सहायक बनाउन सक्नुहुन्छ। उदाहरणका लागि, GitHub Copilot वा ChatGPT जस्ता उत्पादनहरू कोड लेख्न सहयोग गर्छन्।

## कसरी सुरु गर्ने?

तपाईंले LLM सँग एकीकृत हुने तरिका खोज्नुपर्छ जुन सामान्यतया यी दुई तरिकाहरूमा हुन्छ:

- API प्रयोग गर्ने। यहाँ तपाईं आफ्नो प्रॉम्प्टसहित वेब अनुरोधहरू बनाउनुहुन्छ र जेनेरेट गरिएको टेक्स्ट प्राप्त गर्नुहुन्छ।
- लाइब्रेरी प्रयोग गर्ने। लाइब्रेरीहरूले API कलहरू समेटेर प्रयोग गर्न सजिलो बनाउँछन्।

## लाइब्रेरीहरू/SDK हरू

LLM सँग काम गर्नका लागि केही प्रख्यात लाइब्रेरीहरू छन्:

- **openai**, यो लाइब्रेरीले तपाईंको मोडेलसँग जडान गर्न र प्रॉम्प्टहरू पठाउन सजिलो बनाउँछ।

त्यसपछि उच्च स्तरमा काम गर्ने लाइब्रेरीहरू छन्:

- **Langchain**। Langchain प्रख्यात छ र Python समर्थन गर्छ।
- **Semantic Kernel**। Semantic Kernel माइक्रोसफ्टको लाइब्रेरी हो जसले C#, Python, र Java भाषाहरू समर्थन गर्छ।

## openai प्रयोग गरेर पहिलो एप

हेरौं कसरी पहिलो एप बनाउने, कुन लाइब्रेरीहरू चाहिन्छ, कति आवश्यक छ आदि।

### openai इन्स्टल गर्ने

OpenAI वा Azure OpenAI सँग अन्तरक्रिया गर्न धेरै लाइब्रेरीहरू उपलब्ध छन्। C#, Python, JavaScript, Java लगायत धेरै प्रोग्रामिङ भाषाहरू प्रयोग गर्न सकिन्छ। हामीले `openai` Python लाइब्रेरी छानेका छौं, त्यसैले `pip` प्रयोग गरेर इन्स्टल गर्नेछौं।

```bash
pip install openai
```

### स्रोत सिर्जना गर्ने

तपाईंले तलका चरणहरू पूरा गर्नुपर्छ:

- Azure मा खाता खोल्नुहोस् [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI पहुँच प्राप्त गर्नुहोस्। जानुहोस् [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) र पहुँचको लागि अनुरोध गर्नुहोस्।

  > [!NOTE]
  > लेख्ने समयमा, Azure OpenAI पहुँचका लागि आवेदन दिन आवश्यक छ।

- Python इन्स्टल गर्नुहोस् <https://www.python.org/>
- Azure OpenAI सेवा स्रोत सिर्जना गर्नुहोस्। कसरी स्रोत सिर्जना गर्ने भनेर यो मार्गदर्शन हेर्नुहोस् [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुञ्जी र एन्डपोइन्ट पत्ता लगाउने

अब तपाईंले `openai` लाइब्रेरीलाई कुन API कुञ्जी प्रयोग गर्ने हो भन्नु पर्छ। आफ्नो API कुञ्जी पत्ता लगाउन, Azure OpenAI स्रोतको "Keys and Endpoint" सेक्सनमा जानुहोस् र "Key 1" को मान कपी गर्नुहोस्।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब यो जानकारी कपी गरेपछि, लाइब्रेरीहरूलाई यसलाई प्रयोग गर्न निर्देशन दिनुहोस्।

> [!NOTE]
> आफ्नो API कुञ्जीलाई कोडबाट अलग राख्नु राम्रो हुन्छ। तपाईंले यसलाई वातावरण चरहरू (environment variables) प्रयोग गरेर गर्न सक्नुहुन्छ।
>
> - वातावरण चर `OPENAI_API_KEY` लाई आफ्नो API कुञ्जीमा सेट गर्नुहोस्।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कन्फिगरेसन सेटअप गर्ने

यदि तपाईं Azure OpenAI प्रयोग गर्दै हुनुहुन्छ भने, यसरी कन्फिगरेसन सेटअप गर्नुहोस्:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

माथि हामीले निम्न कुरा सेट गरेका छौं:

- `api_type` लाई `azure` सेट गरेका छौं। यसले लाइब्रेरीलाई OpenAI होइन Azure OpenAI प्रयोग गर्न भन्छ।
- `api_key`, यो तपाईंको Azure पोर्टलमा भेटिने API कुञ्जी हो।
- `api_version`, तपाईंले प्रयोग गर्न चाहेको API को संस्करण हो। लेख्ने समयमा, सबैभन्दा नयाँ संस्करण `2023-05-15` हो।
- `api_base`, यो API को एन्डपोइन्ट हो। तपाईंले Azure पोर्टलमा आफ्नो API कुञ्जीको छेउमा पाउन सक्नुहुन्छ।

> [!NOTE]
> `os.getenv` एउटा फङ्सन हो जसले वातावरण चरहरू पढ्छ। तपाईं यसलाई `OPENAI_API_KEY` र `API_BASE` जस्ता वातावरण चरहरू पढ्न प्रयोग गर्न सक्नुहुन्छ। यी वातावरण चरहरू तपाईंको टर्मिनलमा वा `dotenv` जस्ता लाइब्रेरी प्रयोग गरेर सेट गर्न सकिन्छ।

## टेक्स्ट जेनेरेट गर्ने

टेक्स्ट जेनेरेट गर्न `Completion` क्लास प्रयोग गरिन्छ। यहाँ एउटा उदाहरण छ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

माथिको कोडमा, हामीले कम्प्लिशन वस्तु बनायौं र प्रयोग गर्न चाहेको मोडेल र प्रॉम्प्ट पास गर्यौं। त्यसपछि जेनेरेट गरिएको टेक्स्ट प्रिन्ट गर्यौं।

### च्याट कम्प्लिशनहरू

अहिलेसम्म, तपाईंले `Completion` कसरी प्रयोग गर्ने देख्नुभयो। तर अर्को क्लास छ `ChatCompletion` जुन च्याटबोटहरूका लागि उपयुक्त छ। यसको प्रयोगको उदाहरण:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

यो कार्यक्षमताबारे थप जानकारी आगामी अध्यायमा हुनेछ।

## अभ्यास - तपाईंको पहिलो टेक्स्ट जेनेरेसन एप

अब हामीले openai कसरी सेटअप र कन्फिगर गर्ने सिक्यौं, तपाईंको पहिलो टेक्स्ट जेनेरेसन एप बनाउन समय भयो। एप बनाउनका लागि यी चरणहरू पालना गर्नुहोस्:

1. भर्चुअल वातावरण बनाउनुहोस् र openai इन्स्टल गर्नुहोस्:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि तपाईं Windows प्रयोग गर्दै हुनुहुन्छ भने `source venv/bin/activate` को सट्टा `venv\Scripts\activate` टाइप गर्नुहोस्।

   > [!NOTE]
   > आफ्नो Azure OpenAI कुञ्जी पत्ता लगाउन [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) मा जानुहोस्, `Open AI` खोज्नुहोस्, `Open AI resource` छान्नुहोस्, त्यसपछि `Keys and Endpoint` मा जानुहोस् र `Key 1` को मान कपी गर्नुहोस्।

1. _app.py_ फाइल बनाउनुहोस् र यसमा तलको कोड राख्नुहोस्:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > यदि तपाईं Azure OpenAI प्रयोग गर्दै हुनुहुन्छ भने `api_type` लाई `azure` र `api_key` लाई आफ्नो Azure OpenAI कुञ्जीमा सेट गर्नुहोस्।

   तपाईंले यस्तो आउटपुट देख्नुहुनेछ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## फरक-फरक प्रकारका प्रॉम्प्टहरू, फरक-फरक कामका लागि

अब तपाईंले प्रॉम्प्ट प्रयोग गरेर टेक्स्ट कसरी जेनेरेट गर्ने देख्नुभयो। तपाईंको एउटा प्रोग्राम पनि चलिरहेको छ जुन तपाईंले परिवर्तन गरेर फरक-फरक प्रकारका टेक्स्ट जेनेरेट गर्न सक्नुहुन्छ।

प्रॉम्प्टहरू विभिन्न कामका लागि प्रयोग गर्न सकिन्छ। उदाहरणका लागि:

- **टेक्स्टको प्रकार जेनेरेट गर्ने**। जस्तै, कविता, क्विजका प्रश्नहरू आदि।
- **जानकारी खोज्ने**। तपाईं प्रॉम्प्ट प्रयोग गरेर जानकारी खोज्न सक्नुहुन्छ, जस्तै 'वेब विकासमा CORS को अर्थ के हो?'।
- **कोड जेनेरेट गर्ने**। तपाईं प्रॉम्प्ट प्रयोग गरेर कोड जेनेरेट गर्न सक्नुहुन्छ, जस्तै इमेल मान्यकरणका लागि रेगुलर एक्सप्रेसन बनाउने वा पुरै वेब एप्लिकेसन बनाउने।

## अझ व्यावहारिक प्रयोग: रेसिपी जेनेरेटर

कल्पना गर्नुहोस् तपाईंको घरमा केही सामग्रीहरू छन् र तपाईं केही पकाउन चाहनुहुन्छ। त्यसका लागि तपाईंलाई रेसिपी चाहिन्छ। रेसिपी खोज्नको लागि तपाईं सर्च इन्जिन प्रयोग गर्न सक्नुहुन्छ वा LLM प्रयोग गर्न सक्नुहुन्छ।

तपाईं यस्तो प्रॉम्प्ट लेख्न सक्नुहुन्छ:

> "मलाई यी सामग्रीहरू: कुखुरा, आलु, र गाजर प्रयोग गरेर ५ वटा रेसिपी देखाउनुहोस्। प्रत्येक रेसिपीमा प्रयोग भएका सबै सामग्रीहरू सूचीबद्ध गर्नुहोस्।"

माथिको प्रॉम्प्ट अनुसार तपाईंलाई यस्तो जवाफ मिल्न सक्छ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

यो नतिजा राम्रो छ, मलाई के पकाउने थाहा भयो। यस अवस्थामा, केहि उपयोगी सुधारहरू हुन सक्छन्:

- मलाई मन नपर्ने वा एलर्जी भएका सामग्रीहरू फिल्टर गर्ने।
- यदि सबै सामग्रीहरू घरमा छैन भने किनमेल सूची बनाउने।

यी अवस्थाहरूका लागि, अर्को प्रॉम्प्ट थपौं:

> "कृपया लसुन भएका रेसिपीहरू हटाउनुहोस् किनकि मलाई लसुनमा एलर्जी छ र त्यसको सट्टा केही अर्को राख्नुहोस्। साथै, कृपया रेसिपीहरूको लागि किनमेल सूची बनाउनुहोस्, मसँग पहिले नै कुखुरा, आलु र गाजर छन्।"

अब तपाईंलाई नयाँ नतिजा मिल्छ, जसमा लसुन नभएका पाँच रेसिपीहरू छन् र तपाईंको घरमा भएका सामग्रीहरूलाई ध्यानमा राखेर किनमेल सूची पनि छ।

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

## अभ्यास - रेसिपी जेनेरेटर बनाउने

अब हामीले एउटा परिदृश्य खेल्यौं, त्यसलाई मेल खाने कोड लेखौं। यसका लागि यी चरणहरू पालना गर्नुहोस्:

1. पहिलेको _app.py_ फाइललाई सुरुको आधारको रूपमा प्रयोग गर्नुहोस्।
2. `prompt` भेरिएबल पत्ता लगाउनुहोस् र यसको कोड तलको अनुसार परिवर्तन गर्नुहोस्:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   अब यदि तपाईं कोड चलाउनु भयो भने, यस्तो आउटपुट देख्नुहुनेछ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, तपाईंको LLM ननडिटर्मिनिस्टिक हुन्छ, त्यसैले प्रोग्राम हरेक पटक चलाउँदा फरक नतिजा आउन सक्छ।

   राम्रो छ, अब सुधार गर्ने तरिका हेरौं। सुधार गर्न हामी चाहन्छौं कोड लचिलो होस्, ताकि सामग्रीहरू र रेसिपीहरूको संख्या सजिलै परिवर्तन गर्न सकियोस्।

3. कोड यसरी परिवर्तन गरौं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   परीक्षणका लागि कोड यसरी देखिन सक्छ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर र किनमेल सूची थपेर सुधार गर्ने

हामीसँग अब एउटा काम गर्ने एप छ जुन रेसिपीहरू उत्पादन गर्न सक्षम छ र प्रयोगकर्ताबाट सामग्री र रेसिपी संख्या लिने भएकाले लचिलो छ।

अझ सुधार गर्न हामीले यी थप्न चाहन्छौं:

- **मन नपर्ने सामग्रीहरू फिल्टर गर्ने**। हामीलाई मन नपर्ने वा एलर्जी भएका सामग्रीहरू फिल्टर गर्न सक्ने बनाउनुपर्छ। यसका लागि हामीले हाम्रो प्रॉम्प्टको अन्त्यमा फिल्टर सर्त थप्न सक्छौं, जस्तै:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  माथि, हामीले प्रॉम्प्टको अन्त्यमा `{filter}` थप्यौं र प्रयोगकर्ताबाट फिल्टर मान पनि लियौं।

  प्रोग्राम चलाउँदा यस्तो इनपुट हुन सक्छ:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  यहाँ देख्न सकिन्छ, दूध भएका रेसिपीहरू फिल्टर भएका छन्। तर यदि तपाईंलाई लैक्टोज इन्टोलरन्स छ भने, तपाईंले चीज भएका रेसिपीहरू पनि फिल्टर गर्न चाहनुहुन्छ, त्यसैले स्पष्ट हुन आवश्यक छ।

- **किनमेल सूची बनाउने**। हामीले घरमा भएका सामग्रीहरूलाई ध्यानमा राखेर किनमेल सूची बनाउन चाहन्छौं।

  यसका लागि, हामी सबै कुरा एउटै प्रॉम्प्टमा समाधान गर्न सक्दछौं वा दुई प्रॉम्प्टमा विभाजन गर्न सक्दछौं। दोस्रो तरिका प्रयास गरौं। यहाँ हामी अर्को प्रॉम्प्ट थप्न सुझाव दिइरहेका छौं, तर त्यसका लागि पहिलो प्रॉम्प्टको नतिजा दोस्रो प्रॉम्प्टको सन्दर्भ (context) को रूपमा थप्नुपर्छ।

  पहिलो प्रॉम्प्टको नतिजा प्रिन्ट गर्ने भागमा तलको कोड थप्नुहोस्:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  ध्यान दिनुहोस्:

  1. हामी नयाँ प्रॉम्प्ट बनाउँदैछौं जसमा पहिलो प्रॉम्प्टको नतिजा थपिएको छ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
  1. हामी नयाँ अनुरोध गर्छौं, तर पहिलो प्रॉम्प्टमा सोधिएका टोकनहरूको संख्या पनि विचार गर्छौं, त्यसैले यस पटक हामी `max_tokens` लाई 1200 राख्छौं।

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     यो कोड चलाउँदा, हामीले निम्न आउटपुट पाउँछौं:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## आफ्नो सेटअप सुधार्नुहोस्

अहिलेसम्म हामीसँग काम गर्ने कोड छ, तर अझ सुधार गर्न केही समायोजनहरू गर्नुपर्छ। हामीले गर्नुपर्ने केही कुराहरू:

- **कोडबाट गोप्य जानकारी अलग गर्नुहोस्**, जस्तै API कुञ्जी। गोप्य जानकारी कोडमा हुनु हुँदैन र सुरक्षित स्थानमा राखिनुपर्छ। गोप्य जानकारीलाई कोडबाट अलग गर्न, हामी environment variables र `python-dotenv` जस्ता लाइब्रेरीहरू प्रयोग गरेर फाइलबाट लोड गर्न सक्छौं। कोडमा यसरी देखिन्छ:

  1. `.env` फाइल निम्न सामग्रीसहित बनाउनुहोस्:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> नोट, Azure को लागि, तपाईंले निम्न environment variables सेट गर्नुपर्छ:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     कोडमा, environment variables यसरी लोड गर्नुहुन्छ:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **टोकन लम्बाइको बारेमा एउटा कुरा**। हामीले चाहेको पाठ उत्पादन गर्न कति टोकन चाहिन्छ भनेर विचार गर्नुपर्छ। टोकनले खर्च लाग्छ, त्यसैले जहाँ सकिन्छ, टोकनको संख्या कम राख्न प्रयास गर्नुपर्छ। उदाहरणका लागि, के हामी प्रॉम्प्टलाई यसरी लेख्न सक्छौं कि कम टोकन प्रयोग होस्?

  टोकनको संख्या परिवर्तन गर्न, तपाईं `max_tokens` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, १०० टोकन प्रयोग गर्न चाहनुहुन्छ भने:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **temperature सँग प्रयोग गर्ने प्रयोग**। temperature एउटा कुरा हो जुन हामीले अहिलेसम्म उल्लेख गरेका छैनौं तर हाम्रो प्रोग्रामको प्रदर्शनमा महत्वपूर्ण छ। temperature को मान जति उच्च हुन्छ, आउटपुट त्यति नै अनियमित हुन्छ। उल्टो, temperature को मान जति कम हुन्छ, आउटपुट त्यति नै पूर्वानुमानयोग्य हुन्छ। तपाईंले आफ्नो आउटपुटमा विविधता चाहनुहुन्छ कि छैन भनेर विचार गर्नुहोस्।

  temperature परिवर्तन गर्न, तपाईं `temperature` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, 0.5 temperature चाहनुहुन्छ भने:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > नोट, 1.0 नजिक हुँदा आउटपुट धेरै विविध हुन्छ।

## असाइनमेन्ट

यस असाइनमेन्टका लागि, तपाईंले के बनाउने निर्णय गर्न सक्नुहुन्छ।

यहाँ केही सुझावहरू छन्:

- रेसिपी जेनेरेटर एपलाई अझ सुधार गर्न ट्युनिङ गर्नुहोस्। temperature मानहरू र प्रॉम्प्टहरू सँग खेल्नुहोस् र के के बनाउन सकिन्छ हेर्नुहोस्।
- "स्टडी बडी" बनाउनुहोस्। यो एपले कुनै विषय जस्तै Python सम्बन्धी प्रश्नहरूको उत्तर दिन सक्नुपर्छ, जस्तै "Python मा कुनै विषय के हो?" वा "कुनै विषयको कोड देखाऊ" जस्ता प्रॉम्प्टहरू हुन सक्छन्।
- इतिहास बोट, इतिहासलाई जीवित बनाउनुहोस्, बोटलाई कुनै ऐतिहासिक पात्रको भूमिका दिनुहोस् र त्यसको जीवन र समयका बारेमा प्रश्नहरू सोध्नुहोस्।

## समाधान

### स्टडी बडी

तल एउटा प्रारम्भिक प्रॉम्प्ट छ, यसलाई कसरी प्रयोग गर्ने र आफ्नो रुचिअनुसार कसरी परिमार्जन गर्ने हेर्नुहोस्।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

यहाँ केही प्रॉम्प्टहरू छन् जुन तपाईं प्रयोग गर्न सक्नुहुन्छ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जाँच

temperature को अवधारणाले के गर्छ?

1. यसले आउटपुट कति अनियमित हुन्छ नियन्त्रण गर्छ।
1. यसले प्रतिक्रिया कति ठूलो हुन्छ नियन्त्रण गर्छ।
1. यसले कति टोकन प्रयोग हुन्छ नियन्त्रण गर्छ।

## 🚀 चुनौती

असाइनमेन्टमा काम गर्दा, temperature फरक-फरक मानमा सेट गरेर हेर्नुहोस्, जस्तै 0, 0.5, र 1। याद राख्नुहोस् 0 सबैभन्दा कम विविधता हो र 1 सबैभन्दा बढी। कुन मान तपाईंको एपका लागि सबैभन्दा राम्रो काम गर्छ?

## राम्रो काम! आफ्नो सिकाइ जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मा जानुहोस् र आफ्नो Generative AI ज्ञान अझ बढाउनुहोस्!

पाठ 7 मा जानुहोस् जहाँ हामी [च्याट एप्लिकेसनहरू कसरी बनाउने](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) बारे हेर्नेछौं!

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।