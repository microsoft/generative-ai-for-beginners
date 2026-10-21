# पाठ निर्माण एप्लिकेसनहरू बनाउँदै

[![पाठ निर्माण एप्लिकेसनहरू बनाउँदै](../../../translated_images/ne/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(यो पाठको भिडियो हेर्नका लागि माथिको तस्बिरमा क्लिक गर्नुहोस्)_

तपाईंले अहिलेसम्म यस पाठक्रममा देख्नुभएको छ कि मुख्य अवधारणाहरू जस्तै प्रॉम्प्टहरू र यहाँसम्म कि "प्रॉम्प्ट इन्जिनियरिङ" भन्ने एक पूर्ण विधा पनि छ। तपाईंले अन्तरक्रिया गर्न सक्ने धेरै उपकरणहरू जस्तै ChatGPT, Office 365, Microsoft Power Platform र अन्यले तपाईंलाई केहि गर्न प्रॉम्प्टहरू प्रयोग गरेर मद्दत गर्छन्।

तपाईंले एपमा यस प्रकारको अनुभव थप्नको लागि, तपाईंले प्रॉम्प्टहरू, समापनहरू जस्ता अवधारणा बुझ्न र काम गर्न लाइब्रेरी छनौट गर्न आवश्यक छ। तपाईंले यस अध्यायमा यही कुरा सिक्न गइरहेको हुनुहुन्छ।

## परिचय

यस अध्यायमा, तपाईंले:

- openai लाइब्रेरी र यसको मुख्य अवधारणाहरूको बारेमा सिक्नुहुनेछ।
- openai प्रयोग गरेर एक पाठ निर्माण एप बनाउनुहोस्।
- प्रॉम्प्ट, तापक्रम, र टोकनहरू जस्ता अवधारणाहरू कसरी प्रयोग गर्ने बुझ्नुहोस् ताकि पाठ निर्माण एप बनाउन सकियोस्।

## सिकाइका लक्ष्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- पाठ निर्माण एप के हो भन्ने व्याख्या गर्नुहोस्।
- openai प्रयोग गरेर एक पाठ निर्माण एप बनाउनुहोस्।
- तपाईँको एपलाई बढी वा कम टोकनहरू प्रयोग गर्न र तापक्रम परिवर्तन गर्न कन्फिगर गर्नुहोस्, फरक परिणामहरूको लागि।

## पाठ निर्माण एप के हो?

सामान्यतया जब तपाईं एप बनाउनुहुन्छ, यसमा केही प्रकारको इन्टरफेस हुन्छ जस्तै:

- कमाण्ड-आधारित। कन्सोल एपहरू प्राय: त्यस्ता एपहरू हुन्छन् जहाँ तपाईं कमाण्ड टाइप गर्नुहुन्छ र यसले काम पूरा गर्छ। उदाहरणका लागि, `git` कमाण्ड-आधारित एप हो।
- प्रयोगकर्ता इन्टरफेस (UI)। केही एपहरूले ग्राफिकल यूजर इन्टरफेस (GUI) राख्छन् जहाँ तपाईं बटनहरू क्लिक गर्नुहुन्छ, टेक्स्ट इनपुट गर्नुहुन्छ, विकल्पहरू छान्नुहुन्छ र थप।

### कन्सोल र UI एपहरू सीमित छन्

यसलाई त्यस कमाण्ड-आधारित एपसँग तुलना गर्नुहोस् जहाँ तपाईं कमाण्ड टाइप गर्नुहुन्छ:

- **यो सीमित छ।** तपाईं जहिले पनि कुनै पनि कमाण्ड टाइप गर्न सक्नुहुन्न, केवल ती कमाण्डहरू जुन एपले समर्थन गर्छ।
- **भाषा विशिष्ट।** केही एपहरूले धेरै भाषाहरू समर्थन गर्छन्, तर डिफल्ट रूपमा एप विशेष भाषा लागि बनेको हुन्छ, यद्यपि तपाईं थप भाषा समर्थन थप्न सक्नुहुन्छ।

### पाठ निर्माण एपहरूको फाइदा

त्यसो भए पाठ निर्माण एप कसरी फरक हुन्छ?

पाठ निर्माण एपमा तपाईंलाई बढी लचिलोपन हुन्छ, तपाईं आदेशहरूको सीमित सेट वा निश्चित इनपुट भाषा भित्र सीमिति हुनुहुन्न। यसको सट्टा, तपाईं प्राकृतिक भाषामा एपसँग अन्तरक्रिया गर्न सक्नुहुन्छ। अर्को फाइदा भनेको तपाईंले पहिले नै एउटा डाटास्रोतसँग अन्तरक्रिया गर्दै हुनुहुन्छ जुन विशाल जानकारीको संग्रहमाथि प्रशिक्षित छ, जबकि परम्परागत एप डेटाबेसभित्र के छ सीमित हुन सक्छ।

### म पाठ निर्माण एपबाट के निर्माण गर्न सक्छु?

तपाईं धेरै कुरा निर्माण गर्न सक्नुहुन्छ। उदाहरणका लागि:

- **च्याटबोट।** तपाईंको कम्पनी र यसको उत्पादनहरूबाट सम्बन्धित विषयहरूमा प्रश्नहरूको उत्तर दिने च्याटबोट राम्रो मेल हुन सक्छ।
- **सहायक।** LLM हरू जस्तै पाठ संक्षेपण, पाठबाट अन्तर्दृष्टि प्राप्ति, रिजुमे जस्ता सामग्री उत्पादनमा उत्कृष्ट छन्।
- **कोड सहायक।** तपाईंले प्रयोग गर्ने भाषा मोडेल अनुसार, तपाईं कोड लेख्न मद्दत गर्ने कोड सहायक निर्माण गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईं GitHub Copilot जस्ता उत्पादनहरू साथै ChatGPT प्रयोग गर्न सक्नुहुन्छ तपाईँलाई कोड लेख्न सहयोग पुर्याउन।

## म कसरी सुरु गर्न सक्छु?

ठिक छ, तपाईंले LLM सँग एकीकृत हुने तरिका पत्ता लगाउन आवश्यक छ जुन सामान्यतया तलका दुई तरिकाहरू हुन्छन्:

- API प्रयोग गर्नुहोस्। यहाँ तपाईं आफ्नो प्रॉम्प्टसहित वेब अनुरोधहरू निर्माण गर्दै जेनरेट गरिएको पाठ प्राप्त गर्नुहुन्छ।
- लाइब्रेरी प्रयोग गर्नुहोस्। लाइब्रेरीहरूले API कलहरू समेटेर प्रयोग सहज बनाउँछन्।

## लाइब्रेरीहरू/SDK हरू

LLM हरू सँग काम गर्न केही प्रख्यात लाइब्रेरीहरू छन् जस्तै:

- **openai**, यस लाइब्रेरीले तपाईंको मोडेलसँग जडान गर्न र प्रॉम्प्टहरू पठाउन सजिलो बनाउँछ।

त्यसपछि त्यहाँ उच्च स्तरमा काम गर्ने लाइब्रेरीहरू छन् जस्तै:

- **Langchain**। Langchain प्रख्यात छ र Python समर्थन गर्दछ।
- **Semantic Kernel**। Semantic Kernel माइक्रोसफ्टको लाइब्रेरी हो जसले C#, Python, र Java भाषाहरू समर्थन गर्दछ।

## openai प्रयोग गरेर पहिलो एप

हामी कसरी हाम्रो पहिलो एप बनाउने, हामीलाई कुन लाइब्रेरीहरू चाहिन्छ, कति आवश्यक छ आदि हेर्नेछौं।

### openai स्थापना गर्नुहोस्

OpenAI वा Azure OpenAI सँग अन्तरक्रिया गर्न धेरै लाइब्रेरीहरू उपलब्ध छन्। C#, Python, JavaScript, Java लगायत विभिन्न प्रोग्रामिङ भाषाहरू पनि प्रयोग गर्न सकिन्छ। हामीले Python लाइब्रेरी `openai` प्रयोग गर्ने निर्णय गरेका छौं, त्यसैले हामी यसलाई स्थापना गर्न `pip` प्रयोग गर्नेछौं।

```bash
pip install openai
```

### स्रोत सिर्जना गर्नुहोस्

तपाईंले तलका चरणहरू पूरा गर्न आवश्यक छ:

- Azure मा खाता सिर्जना गर्नुहोस् [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI पहुँच प्राप्त गर्नुहोस्। [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) मा जानुहोस् र पहुँचको लागि अनुरोध गर्नुहोस्।

  > [!NOTE]
  > लेखाइको समयमा, तपाईंले Azure OpenAI पहुँचको लागि आवेदन दिनु आवश्यक छ।

- Python स्थापना गर्नुहोस् <https://www.python.org/>
- Azure OpenAI सेवा स्रोत सिर्जना गर्नुहोस्। कसरी [स्रोत सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst भनेर यो मार्गदर्शिका हेरौं।

### API कुञ्जी र अन्तिम विन्दु खोज्नुहोस्

अब तपाईंले आफ्नो `openai` लाइब्रेरीलाई कुन API कुञ्जी प्रयोग गर्ने भनेर बताउनु पर्छ। आफ्नो API कुञ्जी फेला पार्न, Azure OpenAI स्रोतको "कुञ्जी र अन्तिम बिन्दु" खण्डमा जानुहोस् र "कुञ्जी १" को मान प्रतिलिपि गर्नुहोस्।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब जब तपाईंले यो जानकारी प्रतिलिपि गर्नुभयो, लाइब्रेरीलाई यसलाई प्रयोग गर्न निर्देशन दिऔं।

> [!NOTE]
> तपाईंको API कुञ्जीलाई कोडबाट अलग राख्न लाभदायक हुन्छ। तपाईं यसलाई वातावरणीय चरहरू प्रयोग गरेर गर्न सक्नुहुन्छ।
>
> - वातावरणीय चर `OPENAI_API_KEY` आफ्नो API कुञ्जीमा सेट गर्नुहोस्।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कन्फिगरेसन सेटअप गर्नुहोस्

यदि तपाईं Azure OpenAI (अहिले Microsoft Foundry को भाग) प्रयोग गर्नुहुन्छ भने, यसरी कन्फिगरेसन सेटअप गर्ने। हामी मानक `OpenAI` क्लाइन्ट प्रयोग गर्दछौं जुन Azure OpenAI `/openai/v1/` अन्तिम बिन्दुमा निर्देशित छ, जुन Responses API सँग काम गर्छ र कुनै `api_version` आवश्यक पर्दैन:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

माथि हामी निम्न कुरा सेट गर्दैछौं:

- `api_key`, यो तपाईंको Azure Portal वा Microsoft Foundry पोर्टलमा फेला परेको API कुञ्जी हो।
- `base_url`, यो तपाईंको Foundry स्रोत अन्तिम बिन्दु हो जसमा `/openai/v1/` संलग्न गरिएको छ। स्थिर v1 अन्तिम बिन्दु OpenAI र Azure OpenAI दुवैमा काम गर्छ र कुनै `api_version` व्यवस्थापन आवश्यक पर्दैन।

> [!NOTE] > `os.environ` वातावरणीय चरहरू पढ्छ। तपाईं यसलाई `AZURE_OPENAI_API_KEY` र `AZURE_OPENAI_ENDPOINT` जस्ता वातावरणीय चरहरू पढ्न प्रयोग गर्न सक्नुहुन्छ। यी वातावरणीय चरहरू टर्मिनलमा वा `dotenv` जस्ता लाइब्रेरी प्रयोग गरेर सेट गर्नुहोस्।

## पाठ जेनरेट गर्नुहोस्

पाठ जेनरेट गर्नको तरिका Responses API को `responses.create` विधि प्रयोग गर्नु हो। यहाँ एक उदाहरण छ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

माथिको कोडमा, हामी एक प्रतिक्रिया सिर्जना गर्छौं र प्रयोग गर्न चाहेको मोडेल र प्रॉम्प्ट दिन्छौं। त्यसपछि हामी `response.output_text` मार्फत जेनरेट गरिएको पाठ print गर्छौं।

### बहु-पटकको संवाद

Responses API एकल-पटक पाठ जेनरेशन र बहु-पटकको च्याटबोटहरू दोनोंका लागि उपयुक्त छ - तपाईं एउटा संवाद निर्मित गर्न `input` मा सन्देशहरूको सूची प्रदान गर्नुहुन्छ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

यस कार्यक्षमताबारे थप जानकारी आगामी अध्यायमा हुनेछ।

## अभ्यास - तपाईंको पहिलो पाठ निर्माण एप

अब हामीले openai कसरी सेट अप र कन्फिगर गर्ने सिक्यौं, तपाईंको पहिलो पाठ निर्माण एप बनाउने पालो हो। तपाईंको एप बनाउन निम्न चरणहरू पालना गर्नुहोस्:

1. भर्चुअल वातावरण सिर्जना गर्नुहोस् र openai स्थापना गर्नुहोस्:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि तपाईं Windows प्रयोग गर्दै हुनुहुन्छ भने `venv\Scripts\activate` टाइप गर्नुहोस्, `source venv/bin/activate` को सट्टा।

   > [!NOTE]
   > आफ्नो Azure OpenAI कुञ्जी पत्ता लगाउन [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) मा जानुहोस्, `Open AI` खोज्नुहोस् र `Open AI resource` छनौट गर्नुहोस् र त्यसपछि `Keys and Endpoint` छनौट गरी `Key 1` मान प्रतिलिपि गर्नुहोस्।

1. _app.py_ फाइल सिर्जना गर्नुहोस् र तलको कोड दिनुहोस्:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > यदि तपाईं सामान्य OpenAI (Azure होइन) प्रयोग गर्दै हुनुहुन्छ भने `client = OpenAI(api_key="<replace this value with your OpenAI key>")` प्रयोग गर्नुहोस् (कुनै `base_url` बिना) र मोडेल नाम `gpt-5-mini` जस्तो दिनुहोस् सट्टा डेप्लोयमेन्ट नाम।

   तपाईंले जस्तै निम्न आउटपुट देख्न सक्नुहुन्छ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## फरक प्रकारका प्रॉम्प्टहरू, फरक कामहरूका लागि

अब तपाईंले प्रॉम्प्ट प्रयोग गरेर पाठ जेनरेट कसरी गर्ने देख्नुभयो। तपाईंसँग एउटा चलिरहेको प्रोग्राम पनि छ जुन तपाईंले मोडिफाइ गरेर विभिन्न प्रकारका पाठ उत्पादन गर्न सक्नुहुन्छ।

प्रॉम्प्टहरू सबै प्रकारका कार्यहरूका लागि प्रयोग गर्न सकिन्छ। उदाहरणका लागि:

- **पाठको प्रकार उत्पादन गर्नुहोस्।** उदाहरणका लागि, तपाईं कविता, क्विजका प्रश्नहरू आदि उत्पन्न गर्न सक्नुहुन्छ।
- **जानकारी खोज्नुहोस्।** तल उदाहरणजस्तो 'वेब विकासमा CORS को अर्थ के हो?' जस्ता जानकारी खोज्न प्रॉम्प्टहरू प्रयोग गर्न सकिन्छ।
- **कोड निर्माण गर्नुहोस्।** तपाईं प्रॉम्प्ट प्रयोग गरेर कोड निर्माण गर्न सक्नुहुन्छ, उदाहरणका लागि इमेल प्रमाणीकरणका लागि नियमित अभिव्यक्ति विकास वा पूरै वेब एप जस्तो प्रोग्राम निर्माण गर्न।

## अझ व्यावहारिक प्रयोग: एक रेसिपी जेनेरेटर

कल्पना गर्नुहोस् तपाईंको घरमा केहि सामग्रीहरू छन् र तपाईं केही पकाउन चाहनुहुन्छ। त्यसका लागि तपाईंलाई रेसिपी चाहिन्छ। रेसिपी खोज्न एक खोज इन्जिन प्रयोग गर्ने वा LLM प्रयोग गर्ने विकल्प छ।

तपाईं यसरी प्रॉम्प्ट लेख्न सक्नुहुन्छ:

> "मलाई निम्न सामग्रीहरू भएको पकवानका लागि ५ वटा रेसिपी देखाउनुहोस्: कुखुरा, आलु, र गाजर। प्रति रेसिपी प्रयोग गरिएका सबै सामग्रीहरू सूचीकृत गर्नुहोस्"

माथिको प्रॉम्प्ट दिनुभएकोमा, तपाईं यस्तो समान प्रतिक्रिया पाउन सक्नुहुन्छ:

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

यो नतिजा राम्रो छ, मलाई के पकाउने थाहा छ। यस समयमा, के के सुधार उपयोगी हुन सक्छ:

- म इन्ग्रिडिएन्टहरू फिल्टर गर्न चाहन्छु जुन मलाई मन पर्दैन वा मलाई एलर्जी छ।
- यदि मसँग सबै सामग्री नभएमा किनमेल सूची उत्पादन गर्न।

माथिका केसहरूका लागि, अर्को प्रॉम्प्ट थपौं:

> "कृपया मलाई एलर्जी भएको कारण लसुन भएका रेसिपीहरू हटाउनुहोस् र अरू केहि राख्नुहोस्। साथै, कृपया रेसिपीहरूको लागि किनमेल सूची पनि उत्पादन गर्नुहोस्, ध्यान दिनुहोस् मसँग पहिले नै कुखुरा, आलु र गाजर छन्।"

अब तपाईंको नयाँ परिणाम छ, अर्थात्:

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

तपाईंको पाँचवटा रेसिपीहरू छन्, लसुन बिना, र तपाईंलाई पहिले नै भएका सामग्रीहरूलाई ध्यान दिँदै किनमेल सूची पनि छ।

## अभ्यास - रेसिपी जेनेरेटर बनाउनुहोस्

अब जब हामीले एउटा परिदृश्य खेलेका छौं, देखाइएको परिदृश्यसँग मेल खाने कोड लेखौं। यसका लागि, तलका चरणहरू पालना गर्नुहोस्:

1. अवस्थित _app.py_ फाइललाई सुरु गर्ने बिन्दुको रूपमा प्रयोग गर्नुहोस्।
1. `prompt` भेरिएबल लोकेट गर्नुहोस् र यसको कोड तलको जस्तो परिवर्तन गर्नुहोस्:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   यदि अहिले कोड चलाउनु भयो भने, तपाईँलाई यस जस्तै आउटपुट देखिनु पर्छ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > नोट, तपाईंको LLM अनिश्चित (nondeterministic) छ, त्यसैले जबसुकै तपाईंले फरक परिणामहरू पाउन सक्नुहुन्छ।

   राम्ररी, हेर्नुहोस् हामी कसरी सुधार गर्न सक्दछौं। सुधारका लागि, हामीले कोड लचिलो बनाउन चाहन्छौं, ताकि सामग्रीहरू र रेसिपीहरूको संख्या सहजै परिवर्तन गर्न सकियोस्।

1. कोड यसरी परिवर्तन गरौं:

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

### फिल्टर र किनमेल सूची थपेर सुधार गर्नुहोस्

अब हामीसँग रेसिपीहरू उत्पादन गर्ने काम गर्ने एप छ र यो लचिलो छ किनभने यसले प्रयोगकर्ताबाट सामग्रीहरू र रेसिपीहरूको संख्या दुवैमा आधारित इनपुटहरू लिन्छ।

यसलाई अझ सुधार गर्न, हामीले निम्न थप्न चाहन्छौं:

- **सामग्रीहरू फिल्टर गर्नुहोस्।** हामीले मन नपर्ने वा एलर्जी हुने सामग्रीहरू फिल्टर गर्न चाहन्छौं। यो परिवर्तनका लागि हामी हाम्रो प्रॉम्प्टमा अन्त्यमा फिल्टर अवस्था थप्न सकिन्छ जस्तै:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

माथि, हामीले प्रॉम्प्टको अन्त्यमा `{filter}` थपेका छौं र प्रयोगकर्ताबाट फिल्टर मान पनि समेटेका छौं।

प्रोग्राम चलाउँदा एउटा उदाहरण इनपुट यस प्रकार देखिन सक्छ:

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

देख्नुभयो जस्तै, दूध भएको कुनै पनि रेसिपी फिल्टर भइसकेको छ। तर, यदि तपाईं लैक्टोज असहिष्णु हुनुहुन्छ भने, तपाईं चीज भएका रेसिपीहरू पनि फिल्टर गर्न चाहनुहुन्छ, त्यसैले स्पष्ट हुन आवश्यक छ।

- **किनमेल सूची उत्पादन गर्नुहोस्।** हामी जुन सामग्री पहिले नै छ ध्यानमा राख्दै किनमेल सूची उत्पादन गर्न चाहन्छौं।

यसको लागि, हामी सबै कुरा एउटै प्रॉम्प्टमा गर्ने प्रयास गर्न सक्दछौं वा दुई प्रॉम्प्टमा विभाजन गर्ने। हामी दोस्रो विधि प्रयास गर्नेछौं। यहाँ हामी अतिरिक्त प्रॉम्प्ट थप्न सुझाव दिइरहेका छौं, तर त्यसका लागि पहिलाको प्रॉम्प्टको परिणामलाई नयाँ प्रॉम्प्टको सन्दर्भको रूपमा थप्न आवश्यक छ।

कोडको त्यो भाग जहाँ पहिलो प्रॉम्प्टको परिणाम print गरिन्छ, त्यस मुनि तलको कोड थप्नुहोस्:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

तल ध्यान दिनुहोस्:

1. हामी नयाँ प्रॉम्प्ट निर्माण गर्दैछौं जुन पहिलेको प्रॉम्प्टको परिणाम पनि समावेश गर्छ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

1. हामी नयाँ अनुरोध गर्दैछौं, तर पहिलो प्रॉम्प्टमा सोधिएको टोकन संख्या पनि ध्यानमा राख्दै, यस पटक हामी `max_output_tokens` 1200 राख्छौं।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

यस कोड चलाउँदा हामी अहिले तलको आउटपुटमा जान्छौं:

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

अहिलेसम्म हामीसँग रहेको कोड काम गर्छ, तर अझै सुधार गर्न केही संशोधनहरू गर्नुपर्छ। हामीले गर्नुपर्ने केही कामहरू छन्:

- **गुप्त जानकारीहरूलाई कोडबाट अलग गर्नुहोस्**, जस्तै API कुञ्जी। गुप्त जानकारीहरू कोडमा राख्नु हुँदैन र सुरक्षित स्थानमा राखिनुपर्ने हुन्छ। गुप्त जानकारीहरूलाई कोडबाट अलग गर्न, हामी वातावरण चरहरू र `python-dotenv` जस्ता पुस्तकालयहरू प्रयोग गरेर तिनीहरूलाई फाइलबाट लोड गर्न सक्छौं। कोडमा यो यसरी देखिन्छ:

  1. `.env` फाइल निम्न सामग्रीका साथ बनाउनुहोस्:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > नोट, Microsoft Foundry मा Azure OpenAI का लागि, तपाईंले सट्टा निम्न वातावरण चरहरू सेट गर्नुपर्नेछ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमा, तपाईं वातावरण चरहरू यसरी लोड गर्नुहुनेछ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लम्बाइबारे एउटा कुरा**। हामीले चाहेको पाठ उत्पन्न गर्न कति टोकनहरू चाहिन्छ विचार गर्नु आवश्यक छ। टोकनहरू खर्चिलो हुन्छन्, त्यसैले जहाँ सकिन्छ, हामीले प्रयोग गर्ने टोकनहरूको सङ्ख्या कम राख्ने कोसिस गर्नुपर्छ। उदाहरणको लागि, के हामी प्रॉम्प्टलाई यसरी बनाउनु सक्छौं कि कम टोकनहरू प्रयोग होस्?

  टोकनहरू परिवर्तन गर्न, तपाईं `max_output_tokens` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, यदि तपाईं १०० टोकन प्रयोग गर्न चाहनुहुन्छ भने, तपाईंले यसरी गर्नुहुनेछ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **तापमानसँग प्रयोग गरेर परीक्षण गर्ने कुरा**। तापमान त्यो हो जुन हामीले अहिलेसम्म उल्लेख गरेका छैनौं तर हाम्रो कार्यक्रम कसरी प्रदर्शन गर्छ भन्ने महत्वपूर्ण सन्दर्भ हो। तापमान मान जति उच्च, आउटपुट उति अनिश्चित हुने छ। उल्टो, तापमान मान जति कम, आउटपुट उति पूर्वानुमेय हुने छ। तपाईंलाई आफ्नो आउटपुटमा भिन्नता चाहिन्छ वा छैन भनेर विचार गर्नुहोस्।

  तापमान परिवर्तन गर्न, तपाईं `temperature` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईं ०.५ तापमान चाहनुहुन्छ भने यसरी गर्नुहोस्:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > नोट, १.० जति नजिक, आउटपुट उति विविध हुनेछ।

- **तर्क गर्ने मोडेलहरूले `temperature` प्रयोग गर्दैनन्**। यो एक महत्त्वपूर्ण २०२६ बदलाव हो। Microsoft Foundry मा हालका, अप्रचलित नभएका मोडेलहरू **तर्क गर्ने मोडेलहरू** हुन् (GPT-5 परिवार, o-श्रृंखला) - र तिनीहरूले `temperature` वा `top_p` (र `max_tokens` पनि होइन; यसको सट्टा `max_output_tokens` प्रयोग गर्नुहोस्) समर्थन गर्दैनन्। यदि तपाईं `temperature` लाई `gpt-5-mini` मा पठाउनु भयो भने "प्यारामिटर समर्थित छैन" त्रुटि पाउनुहुनेछ। त्यसैले माथिको तापमान उदाहरण प्रयास गर्न, यस्तो मोडेलमा पठाउनुहोस् जुन अझै नमूना नियन्त्रणहरू समर्थन गर्दछ - उदाहरणका लागि खुला **Llama** मोडेल जस्तै `Llama-3.3-70B-Instruct` जुन [Microsoft Foundry मोडेल क्याटलग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) बाट हो, Foundry Models / Azure AI Inference एन्डप्वाइन्ट मार्फत कल गरिन्छ (ठ्याक्कै `githubmodels-*` नमूनाहरू जस्तै)। GPT-5 जस्ता तर्क गर्ने मोडेलहरूमा आउटपुट भिन्न तरिकाले चलाउनु पर्छ:
  - **प्रॉम्प्ट इन्जिनियरिङ** - स्पष्ट निर्देशनहरू, उदाहरणहरू र संरचित आउटपुट (पाठ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्) ले पहले नमूना नियन्त्रकहरूको काम गर्दछन्।
  - **तर्क नियन्त्रणहरू** - तर्क प्रयास/व्याख्या जस्ता प्यारामिटरहरूले तर्कको गहिराइलाई विलम्बता र खर्चसँग सन्तुलन गर्छन्।

  संक्षेपमा: `temperature`/`top_p` धेरै मोडेलहरूमा (Llama, Mistral, Phi, र GPT-4.x परिवार - यद्यपि GPT-4.x अप्रचलित हुँदैछ) अझै पनि मान्य छन्, तर यात्रा दिशा भनेको GPT-5 जस्ता तर्क गर्ने मोडेलहरूमा प्रॉम्प्ट इन्जिनियरिङ र तर्क नियन्त्रणहरू पो हो।

## कार्य

यस कार्यका लागि, तपाईंले के बनाउने चयन गर्न सक्नुहुन्छ।

यहाँ केहि सुझावहरू छन्:

- रेसिपी जेनेरेटर एप्लिकेसनलाई अझ सुधार गर्न ट्वीक गर्नुहोस्। तापमान मानहरू र प्रॉम्प्टहरूमा खेल्नुहोस् र के बनाउन सकिन्छ हेर्नुहोस्।
- "अध्ययन साथी" बनाउनुहोस्। यो एपले कुनै विषयबारे प्रश्नहरूको उत्तर दिन सक्षम हुनुपर्छ, जस्तै पाइथनका लागि "पाइथनमा कुनै निश्चित विषय के हो?" जस्ता प्रॉम्प्टहरू वा कुनै विषयको लागि कोड देखाउने प्रॉम्प्टहरू हुन सक्छन्।
- इतिहास बोट, इतिहासलाई जीवित बनाउन, बोटलाई कुनै ऐतिहासिक पात्रको रुपमा खेलेर त्यसको जीवन र समयमा प्रश्नहरू सोध्नुहोस्।

## समाधान

### अध्ययन साथी

तल एक सुरुआती प्रॉम्प्ट छ, कसरी प्रयोग गर्ने र आफ्नो मनपर्ने अनुसार ट्वीक गर्ने प्रयास गर्नुहोस्।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

यहाँ केहि प्रॉम्प्टहरू छन् जसलाई तपाईं प्रयोग गर्न सक्नुहुन्छ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जाँच

तापमान भन्नाले के हो?

1. यसले आउटपुट कति अनियमित हुन्छ भन्ने नियन्त्रण गर्दछ।
1. यसले जवाफ कति ठूलो हुन्छ भन्ने नियन्त्रण गर्दछ।
1. यसले कति टोकनहरू प्रयोग गरिन्छ भन्ने नियन्त्रण गर्दछ।

## 🚀 चुनौती

कार्यमा काम गर्दा, तापमान फरक-फरक राख्न प्रयास गर्नुहोस्, जस्तै ०, ०.५, र १ मा सेट गर्नुहोस्। सम्झनुहोस् ० सबैभन्दा कम विविधता हो र १ सबैभन्दा धेरै हो। कुन मान तपाईंको एपका लागि उत्तम छ?

## सुन्दर कार्य! तपाईंको सिकाइ जारी राख्नुहोस्

यो पाठ पूरा गरेपछि, हाम्रो [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र तपाईंको Generative AI ज्ञान अझ बढाउनुहोस्!

पाठ ७ मा जानुहोस् जहाँ हामी [च्याट अनुप्रयोगहरू कसरी बनाउने](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) हेर्नेछौं!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->