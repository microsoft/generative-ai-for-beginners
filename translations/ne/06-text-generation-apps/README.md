# पाठ उत्पादन अनुप्रयोगहरू निर्माण गर्दै

[![Building Text Generation Applications](../../../translated_images/ne/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(यस पाठको भिडियो हेर्न माथिको तस्बिरमा क्लिक गर्नुहोस्)_

तपाईले अहिलेसम्म यस पाठ्यक्रममार्फत देख्नुभएको छ कि प्रम्प्टहरू जस्ता मूल अवधारणाहरू छन् र "prompt engineering" नामक एउटा पूरा अनुशासन पनि छ। धेरै उपकरणहरू, जस्तै ChatGPT, Office 365, Microsoft Power Platform र थप, तपाईंलाई प्रम्प्टहरू प्रयोग गरेर केहि पूरा गर्न सहयोग गर्छन्।

तपाईलाई यस्तो अनुभव अनुप्रयोगमा थप्नका लागि, प्रम्प्टहरू, पूर्तिहरू जस्ता अवधारणाहरू बुझ्न आवश्यक छ र कुन पुस्तकालयसँग काम गर्ने रोज्नुपर्छ। यसै कुरा तपाईं यस अध्यायमा सिक्नुहुनेछ।

## परिचय

यस अध्यायमा, तपाईं:

- openai पुस्तकालय र यसको मूल अवधारणाहरू सिक्नुहोस्।
- openai प्रयोग गरेर पाठ उत्पादन अनुप्रयोग बनाउनुहोस्।
- प्रम्प्ट, तापक्रम, र टोकनहरू जस्ता अवधारणाहरू कसरी प्रयोग गर्ने बुझ्नुहोस्, पाठ उत्पादन अनुप्रयोग बनाउन।

## सिकाइ लक्ष्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- पाठ उत्पादन अनुप्रयोग के हो व्याख्या गर्न।
- openai प्रयोग गरेर पाठ उत्पादन अनुप्रयोग बनाउन।
- तपाईको अनुप्रयोगलाई बढी वा कम टोकनहरू प्रयोग गर्न कन्फिगर गर्न र तापक्रम परिवर्तन गरेर विभिन्न परिणामहरू प्राप्त गर्न सक्षम हुन।

## पाठ उत्पादन अनुप्रयोग भनेको के हो?

सामान्यतया तपाईं अनुप्रयोग बनाउनुभएको बेला यसमा कस्तो इन्टरफेस हुन्छ, जस्तै:

- आदेश आधारित। कन्सोल अनुप्रयोगहरू त्यस्ता अनुप्रयोगहरू हुन् जहाँ तपाईं आदेश टाइप गर्नुहुन्छ र यो कार्य पूरा गर्छ। उदाहरणको लागि, `git` आदेश आधारित अनुप्रयोग हो।
- प्रयोगकर्ता इन्टरफेस (UI)। केही अनुप्रयोगहरूमा ग्राफिकल प्रयोगकर्ता इन्टरफेस (GUI) हुन्छ जहाँ तपाईं बटनहरू क्लिक गर्नुहुन्छ, पाठ इनपुट गर्नुहुन्छ, विकल्पहरू चयन गर्नुहुन्छ र थप।

### कन्सोल र UI अनुप्रयोगहरू सीमित छन्

एउटा आदेश आधारित अनुप्रयोगसँग तुलना गर्नुहोस् जहाँ तपाईं एक आदेश टाइप गर्नुहुन्छ:

- **यो सीमित छ**। तपाईं जुनसुकै आदेश टाइप गर्न सक्नुहुन्न, केवल ती आदेशहरू जुन अनुप्रयोगले समर्थन गर्छ।
- **भाषा विशेष**। केही अनुप्रयोगहरूले धेरै भाषा समर्थन गर्छन्, तर डिफल्ट रूपमा अनुप्रयोग एउटा विशिष्ट भाषाका लागि बनाइएको हुन्छ, यद्यपि तपाईंले थप भाषा समर्थन थप्न सक्नुहुन्छ।

### पाठ उत्पादन अनुप्रयोगहरूको लाभहरू

त्यसोभए पाठ उत्पादन अनुप्रयोग कसरी फरक छ?

पाठ उत्पादन अनुप्रयोगमा, तपाईंलाई धेरै लचिलोपन हुन्छ, तपाईं आदेशहरूको सेट वा विशिष्ट इनपुट भाषामा सीमित हुनुहुन्न। सट्टामा, तपाईं प्राकृतिक भाषामा अनुप्रयोगसँग अन्तरक्रिया गर्न सक्नुहुन्छ। अर्को फाइदा यो हो कि तपाईं पहिले नै यस्तो डाटा स्रोतसँग अन्तरक्रिया गर्दै हुनुहुन्छ जुन विशाल संकलनमा तालिम प्राप्त छ, जबकि परम्परागत अनुप्रयोग डेटाबेसमा के छ त्यसमा सीमित हुन सक्छ।

### म के निर्माण गर्न सक्छु पाठ उत्पादन अनुप्रयोगले?

तपाईं धेरै कुरा बनाउन सक्नुहुन्छ। उदाहरणका लागि:

- **एक च्याटबोट**। विषयहरूको बारेमा प्रश्नहरूको जवाफ दिने च्याटबोट, जस्तै तपाईंको कम्पनी र त्यसका उत्पादनहरू राम्रो मेल खान सक्छ।
- **सहायक**। LLM हरू राम्रो हुन्छन् पाठ सारांश गर्न, पाठबाट थाहा लिन, पाठ उत्पादन गर्न जस्तै रिजुमेहरू र थप।
- **कोड सहायक**। तपाईले प्रयोग गर्ने भाषा मोडेल अनुसार, तपाईं कोड लेख्न सहयोग गर्ने कोड सहायक बनाउन सक्नुहुन्छ। उदाहरणका लागि, तपाईं GitHub Copilot जस्ता उत्पादनहरू साथै ChatGPT लाई पनि कोड लेख्न सहयोगका लागि प्रयोग गर्न सक्नुहुन्छ।

## म कसरी सुरु गर्न सक्छु?

राम्रो, तपाईंलाई LLM सँग अन्तरक्रिया गर्ने तरिका फेला पार्न आवश्यक छ जुन सामान्यतया दुई तरिकामा हुन्छ:

- API प्रयोग गर्नुहोस्। यहाँ तपाईं वेब अनुरोधहरू आफ्नो प्रम्प्टसहित सिर्जना गर्नुहुन्छ र आफ्ना उत्पन्न पाठ फर्काउनुहुन्छ।
- पुस्तकालय प्रयोग गर्नुहोस्। पुस्तकालयहरूले API कलहरू समेट्छन् र तिनीहरूलाई सजिलो बनाउँछन् प्रयोग गर्न।

## पुस्तकालयहरू/SDK हरू

LLM सँग काम गर्न केही परिचित पुस्तकालयहरू छन् जस्तै:

- **openai**, यो पुस्तकालयले तपाईंको मोडेलमा सजिलो जडान गर्न र प्रम्प्टहरू पठाउन सक्षम बनाउँछ।

त्यसपछि त्यस्ता पुस्तकालयहरू छन् जुन उच्च तहमा सञ्चालन गर्छन् जस्तै:

- **Langchain**। Langchain प्रसिद्ध छ र Python समर्थन गर्छ।
- **Semantic Kernel**। Semantic Kernel माइक्रोसफ्टको पुस्तकालय हो जसले C#, Python, र Java भाषाहरू समर्थन गर्छ।

## पहिलो अनुप्रयोग openai प्रयोग गरी

हेर्नुहोस् कसरी हामीले पहिलो अनुप्रयोग बनाउन सक्छौं, कुन पुस्तकालयहरू आवश्यक छन् र कति आवश्यक छ।

### openai स्थापना गर्नुहोस्

OpenAI वा Azure OpenAI सँग अन्तरक्रिया गर्न धेरै पुस्तकालयहरू उपलब्ध छन्। विभिन्न प्रोग्रामिङ भाषाहरू जस्तै C#, Python, JavaScript, Java र थप प्रयोग गर्न सकिन्छ। हामीले `openai` Python पुस्तकालय रोजेका छौं, त्यसैले `pip` प्रयोग गरेर यसलाई स्थापना गर्नेछौं।

```bash
pip install openai
```

### स्रोत सिर्जना गर्नुहोस्

तपाईंले निम्न चरणहरू पूरा गर्न आवश्यक छ:

- Azure मा खाता सिर्जना गर्नुहोस् [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI पहुँच प्राप्त गर्नुहोस्। जानुहोस् [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) र पहुँचको लागि अनुरोध गर्नुहोस्।

  > [!NOTE]
  > यो सामग्री लेख्ने समयमा, तपाईंले Azure OpenAI पहुँचको लागि आवेदन दिन आवश्यक छ।

- Python स्थापना गर्नुहोस् <https://www.python.org/>
- Azure OpenAI सेवा स्रोत सिर्जना गर्नुभएको छ। यो मार्गनिर्देशन हेर्नुहोस् कसरी [स्रोत सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुञ्जी र अन्त बिन्दु पत्ता लगाउनुहोस्

यस समयमा, तपाईंले आफ्नो `openai` पुस्तकालयलाई कुन API कुञ्जी प्रयोग गर्ने बताउनु पर्छ। आफ्नो API कुञ्जी खोज्न Azure OpenAI स्रोतको "Keys and Endpoint" खण्डमा जानुहोस् र "Key 1" मान कपी गर्नुहोस्।

![Azure पोर्टलमा Keys and Endpoint स्रोत ब्लेड](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब तपाईंसँग यो जानकारी कपी गरिएको छ, पुस्तकालयहरूलाई यसलाई प्रयोग गर्न निर्देशन दिऔं।

> [!NOTE]
> आफ्नो API कुञ्जीलाई कोडबाट अलग राख्नु आवश्यक छ। यसका लागि, तपाईं वातावरण चरहरू प्रयोग गर्न सक्नुहुन्छ।
>
> - वातावरण चर `OPENAI_API_KEY` लाई आफ्नो API कुञ्जीसँग सेट गर्नुहोस्।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कन्फिगरेसन सेटअप

यदि तपाईं Azure OpenAI (अब Microsoft Foundry को भाग) प्रयोग गर्दै हुनुहुन्छ भने, कन्फिगरेसन यसरी सेटअप गर्नुहोस्। हामीले मानक `OpenAI` क्लायन्ट प्रयोग गर्छौं जुन Azure OpenAI `/openai/v1/` अन्त बिन्दुमा सूचित हुन्छ, जसले Responses API सँग काम गर्छ र `api_version` आवश्यक पर्दैन:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

माथि हामीले निम्न सेट गर्दैछौं:

- `api_key`, तपाईको Azure पोर्टल वा Microsoft Foundry पोर्टलमा रहेको API कुञ्जी।
- `base_url`, तपाईको Foundry स्रोत अन्त बिन्दु `/openai/v1/` थपेर। स्थिर v1 अन्त बिन्दु OpenAI र Azure OpenAI दुवैमा काम गर्छ, `api_version` व्यवस्थापन बिना।

> [!NOTE] > `os.environ` वातावरण चरहरू पढ्छ। तपाईं यसलाई `AZURE_OPENAI_API_KEY` र `AZURE_OPENAI_ENDPOINT` जस्ता वातावरण चरहरू पढ्न प्रयोग गर्न सक्नुहुन्छ। यी वातावरण चरहरू तपाईंको टर्मिनलमा सेट गर्नुहोस् वा `dotenv` जस्तो पुस्तकालय प्रयोग गरेर।

## पाठ उत्पन्न गर्नुहोस्

पाठ उत्पन्न गर्ने तरिका हो Responses API लाई `responses.create` विधि मार्फत प्रयोग गर्ने। उदाहरण यस प्रकार छ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # यो तपाईंको मोडेल डिप्लोयमेन्ट नाम हो
    input=prompt,
    store=False,
)
print(response.output_text)
```

माथिको कोडमा, हामी प्रतिक्रिया सिर्जना गर्छौं र हामीले प्रयोग गर्न चाहेको मोडेल र प्रम्प्ट पास गर्छौं। त्यसपछि उत्पन्न पाठ `response.output_text` मार्फत प्रिन्ट गर्छौं।

### बहु-चरण संवादहरू

Responses API एकल-चरण पाठ उत्पादन र बहु-चरण च्याटबोटहरूका लागि उपयुक्त छ - तपाईं `input` मा सन्देशहरूको सूची प्रदान गर्नुहुन्छ संवाद बनाउन:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

यस कार्यक्षमताको बारेमा थप जानकारी आउने अध्यायमा हुनेछ।

## अभ्यास - तपाईंको पहिलो पाठ उत्पादन अनुप्रयोग

अब हामीले कसरी openai सेटअप गर्ने र कन्फिगर गर्ने हामीले सिक्यौं, समय भयो तपाईंको पहिलो पाठ उत्पादन अनुप्रयोग बनाउन। अनुप्रयोग बनाउनका लागि, यी चरणहरू पालना गर्नुहोस्:

1. भर्चुअल वातावरण सिर्जना गर्नुहोस् र openai स्थापना गर्नुहोस्:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि तपाईं Windows प्रयोग गर्दै हुनुहुन्छ भने `source venv/bin/activate` को सट्टा `venv\Scripts\activate` लेख्नुहोस्।

   > [!NOTE]
   > तपाईंको Azure OpenAI कुञ्जी पत्ता लगाउन जानुहोस् [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) र `Open AI` खोज्नुहोस्, त्यसपछि `Open AI resource` चयन गर्नुहोस् र `Keys and Endpoint` मा जानुहोस् र `Key 1` मान कपी गर्नुहोस्।

1. _app.py_ फाइल सिर्जना गर्नुहोस् र निम्न कोड राख्नुहोस्:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # तपाईंको पूर्ति कोड थप गर्नुहोस्
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API प्रयोग गरी अनुरोध गर्नुहोस्
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिक्रिया मुद्रण गर्नुहोस्
   print(response.output_text)
   ```

   > [!NOTE]
   > यदि तपाईंले सामान्य OpenAI (Azure होइन) प्रयोग गर्दै हुनुहुन्छ भने, `client = OpenAI(api_key="<replace this value with your OpenAI key>")` प्रयोग गर्नुहोस् (`base_url` बिना) र मोडेल नाम `gpt-4o-mini` जस्ता सट्टा डिप्लोयमेंट नाम भन्दा।

   तपाईंले निम्न आउटपुट देख्नु पर्छ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विभिन्न प्रकारका प्रम्प्टहरू, विभिन्न कार्यहरूको लागि

अब तपाईंले प्रम्प्ट प्रयोग गरेर पाठ उत्पन्न गर्न सिक्नुभयो। तपाईंसँग एउटा प्रोग्राम पनि छ जुन कार्यरत छ र तपाईंले विभिन्न प्रकारका पाठ उत्पन्न गर्न संशोधन र परिवर्तन गर्न सक्नुहुन्छ।

प्रम्प्टहरू सबै प्रकारका कार्यहरूको लागि प्रयोग गर्न सकिन्छ। उदाहरणका लागि:

- **पाठको प्रकार उत्पन्न गर्नुहोस्**। उदाहरणका लागि, तपाईं कविता, क्विजको प्रश्न आदि उत्पन्न गर्न सक्नुहुन्छ।
- **सूचना खोज्नुहोस्**। तपाईं प्रम्प्टहरू प्रयोग गरेर यस्तो जानकारी खोज्न सक्नुहुन्छ, जस्तै 'वेब विकासमा CORS को अर्थ के हो?'।
- **कोड उत्पन्न गर्नुहोस्**। तपाईं प्रम्प्टहरू प्रयोग गरेर कोड उत्पादन गर्न सक्नुहुन्छ, उदाहरणका लागि इमेल प्रमाणीकरण गर्न रेगुलर एक्स्प्रेशन विकास गर्नु वा पूरै प्रोग्राम जस्तै वेब अनुप्रयोग बनाउनु।

## थप व्यावहारिक प्रयोग केस: एक पकाउने विधि उत्पन्न गर्ने उपकरण

कल्पना गर्नुहोस् तपाईंको घरमा केही सामाग्री छन् र तपाईं केही पकाउन चाहनुहुन्छ। त्यसका लागि, तपाईंलाई एक विधि चाहिन्छ। विधि खोज्नको लागि, तपाईं सर्च इन्जिन प्रयोग गर्न सक्नुहुन्छ वा LLM प्रयोग गर्न सक्नुहुन्छ।

तपाईं यसरी एउटा प्रम्प्ट लेख्न सक्नुहुन्छ:

> "मलाई यी सामग्रीहरूका साथ ५ वटा पकाउने विधि देखाउनुहोस्: कुखुरा, आलु, र गाजर। प्रत्येक विधिका लागि सबै सामग्रीहरूको सूची बनाउनुहोस्"

माथिको प्रम्प्ट दिँदा, तपाईंले निम्न जस्तै उत्तर पाउन सक्नुहुन्छ:

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

यो परिणाम राम्रो छ, मलाई के पकाउने थाहा भयो। यस समयमा, के के सुधारहरू उपयोगी हुन सक्छन्:

- मलाई नपर्ने वा जसमा म एलर्जी छु ती सामग्रीहरू फिल्टर गर्नु।
- मलाई नभएका सामग्रीहरू किन्ने सूची निर्माण गर्नु।

माथिका केसहरूसँग मेल खाने अर्को प्रम्प्ट थपौं:

> "मेरो एलर्जी भएकोले कृपया लसुन भएका विधिहरू हटाउनुहोस् र अन्य कुनै सामग्रीले बदल्नुहोस्। साथै, कृपया पकाउने विधिहरूको लागि किन्ने सूची पनि तयार गर्नुहोस्, मसँग पहिले नै कुखुरा, आलु र गाजर छन्।"

अब तपाईंसँग नयाँ परिणाम छ, अर्थात्:

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

त्यो तपाईंका पाँच विधि हुन्, जसमा लसुन छैन र तपाईंको घरमा भएका सामग्री बुझेर किन्ने सूची पनि छ।

## अभ्यास - एक पकाउने विधि उत्पन्न गर्ने उपकरण बनाउनुहोस्

अब हामीले परिदृश्य खेलेका छौं, त्यस अनुरूप कोड लेखौं। यसका लागि, यी चरणहरू पालना गर्नुहोस्:

1. अवस्थित _app.py_ फाइललाई सुरुको बिन्दु बनाएर प्रयोग गर्नुहोस्
1. `prompt` भेरियन्ट पत्ता लगाउनुहोस् र यसको कोड तल दिएको जस्तो परिवर्तन गर्नुहोस्:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   अब कोड चलाउँदा तपाईंले निम्न जस्तो परिणाम देख्नुहुनेछ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, तपाईंको LLM अनिश्चित छ, त्यसैले तपाईंले प्रोग्राम चलाउँदा फरक परिणामहरू प्राप्त गर्न सक्नुहुन्छ।

   राम्रो छ, हेर्नुहोस् कसरी सुधार गर्न सकिन्छ। सुधार गर्नको लागि, हामी कोडलाई लचिलो बनाउन चाहन्छौं, ताकि सामग्रीहरू र पकाउने विधिको संख्या सजिलै परिवर्तन गर्न सकियोस्।

1. कोड यसरी परिवर्तन गरौं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # नुस्खाहरूको संख्या सामग्री र संकेतमा अन्तरपोल गर्नुहोस्
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   परीक्षण प्रयोजनका लागि कोड यसरी देखिन सक्छ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर र किन्ने सूची थपेर सुधार गर्नुहोस्

अब हामीसँग काम गर्ने अनुप्रयोग छ जसले पकाउने विधि उत्पादन गर्न सक्छ र यसले प्रयोगकर्ताबाट लिने इनपुटहरूमा निर्भर हुन्छ, न त केवल विधिहरूको संख्या मात्र, तर प्रयोग भएका सामग्रीहरूमा पनि।

यसलाई अझ सुधार गर्नका लागि, हामी निम्न थप्न चाहन्छौं:

- **सामाग्रीहरू फिल्टर गर्नुहोस्**। हामीलाई नचाहिने वा एलर्जी भएको सामग्रीहरू फिल्टर गर्न सक्नुपर्छ। यो परिवर्तन गर्नको लागि हामी हाम्रो प्रम्प्ट सम्पादन गरी यसको अन्त्यमा फिल्टर सर्त थप्न सक्छौं यसरी:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  माथि, हामीले प्रम्प्टको अन्त्यमा `{filter}` थपेका छौँ र प्रयोगकर्ताबाट फिल्टर मान पनि समात्न सक्छौँ।

  कार्यक्रम चलाउँदा उदाहरण इनपुट यसरी देखिन सक्छ:

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

  जस्तै तपाईंले देख्नुभयो, दुुध भएको विधिहरू फिल्टर गरिएको छ। तर यदि तपाईंलाई ल्याक्टोज इन्टोलरन्ट छ भने, तपाईंले पनी चीज भएका विधिहरू फिल्टर गर्न चाहानु हुन्छ, त्यसैले स्पष्ट हुनु आवश्यक छ।


- **किनमेल सूची तयार गर्नुहोस्**। हामीसँग पहिले देखि घरमा के छ भनेर विचार गरी किनमेल सूची तयार गर्न चाहन्छौं।

  यो कार्यक्षमताका लागि, हामी सबै केहि एकै पटकमा समाधान गर्ने प्रयास गर्न सक्छौं वा यसलाई दुईवटा प्रम्प्टमा विभाजन गर्न सक्छौं। दोस्रो विधि प्रयास गरौं। यहाँ हामी एक अतिरिक्त प्रम्प्ट थप्ने सुझाव दिइरहेका छौं, तर त्यसको लागि पहिलेको प्रम्प्टको नतिजा दोस्रो प्रम्प्टमा सन्दर्भको रूपमा थप्नुपर्छ।

  पहिलो प्रम्प्टबाट नतिजा प्रिन्ट हुने भाग कोडमा भेट्टाउनुहोस् र तलको कोड थप्नुहोस्:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया प्रिन्ट गर्नुहोस्
  print("Shopping list:")
  print(response.output_text)
  ```

  निम्न कुरा ध्यान दिनुहोस्:

  1. हामी पहिलो प्रम्प्टबाट नतिजा लिएर नयाँ प्रम्प्टको लागि नयाँ प्रम्प्ट तयार गर्दैछौं:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हामी नयाँ अनुरोध गर्छौं, तर पहिलो प्रम्प्टमा मागिएको टोकन संख्या पनि विचार गर्दै, यस पटक `max_output_tokens` 1200 राख्छौं।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     यो कोड चलाउँदा, हामी तलको आउटपुट पाउँछौं:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## आफ्नो सेटअप सुधार गर्नुहोस्

अहिलेसम्म हामीसँग कोड काम गर्दैछ, तर थप सुधारका लागि केही समायोजनहरू गर्नु पर्नेछ। केही गर्नुपर्ने कुरा यस प्रकार छन्:

- **कोडबाट सेक्रेट्स अलग गर्नुहोस्**, जस्तै API कुञ्जी। सेक्रेट्स कोडमा नहाल्नुहोस् र सुरक्षित स्थानमा भण्डारण गर्नुहोस्। सेक्रेट्सलाई कोडबाट अलग गर्न, हामी वातावरणभित्रका भेरिएबलहरू र `python-dotenv` जस्ता पुस्तकालयहरू प्रयोग गर्न सक्छौं जुन फाइलबाट लोड गर्छ। यसरी कोडमा यो देखिन्छ:

  1. `.env` फाइलमा तलको सामग्री बनाउनुहोस्:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > नोट गर्नुहोस्, Microsoft Foundry मा Azure OpenAI प्रयोग गर्दा, यसका लागि तलको वातावरण भेरिएबलहरू सेट गर्नु आवश्यक हुन्छ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमा वातावरण भेरिएबल यसरी लोड गर्नुहुनेछ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लम्बाइ सम्बन्धमा कुरा**। आवश्यक पाठ उत्पादन गर्न कति टोकन चाहिन्छ विचार गर्नुहोस्। टोकनहरूले पैसाको खर्च गर्छ, त्यसैले जहाँ सकिन्छ, टोकनको प्रयोग सस्तो बनाउनुपर्छ। उदाहरणका लागि, के हामी प्रम्प्टलाई यसरी लेख्न सक्छौं कि कम टोकन प्रयोग होस्?

  टोकनको संख्या परिवर्तन गर्न, `max_output_tokens` प्यारामिटर प्रयोग गर्न सकिन्छ। उदाहरणको लागि, १०० टोकन चाहिन्छ भने, यसरी प्रयोग गर्नुस्:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **तापक्रम (temperature) मा प्रयोग गर्दै देख्नुहोस्**। तापक्रमको मानले हाम्रो प्रोग्राम कस्तो प्रदर्शन गर्छ भन्ने सन्दर्भमा महत्त्वपूर्ण छ। उच्च तापक्रम मानबाट आउटपुट धेरै अनियमित हुन्छ। कम तापक्रम मानबाट आउटपुट बढी पूर्वानुमानयोग्य हुन्छ। तपाईंले के चाहनुहुन्छ_outvariability_ वा स्थिरता सोच्नुहोस्।

  तापक्रम परिवर्तन गर्न, `temperature` प्यारामिटर प्रयोग गर्न सकिन्छ। उदाहरणको लागि, ०.५ तापक्रम राख्न यसरी गर्नुहोस्:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > नोट, 1.0 नजिकको मानले आउटपुट धेरै विविध हुन्छ।

## कार्य

यस कार्यका लागि, तपाईंले के बनाउने छनोट गर्न सक्नुहुन्छ।

यहाँ केही सुझावहरू छन्:

- रेसिपी जनरेटर एपलाई अझ सुधार गर्न ट्युन गर्नुहोस्। तापक्रम मानहरू र प्रम्प्टहरू प्रयोग गरेर के कस्तो आउटपुट आउँछ पत्ता लगाउनुहोस्।
- "स्टडी बडी" बनाउनुहोस्। यो एपले कुनै विषय जस्तै Python सम्बन्धी प्रश्नहरूको उत्तर दिन सक्नुपर्छ, जस्तै "Python मा कुनै विषय के हो?", वा कुनै विषयको कोड देखाउन माग गर्ने प्रम्प्टहरू हुन सक्छन्।
- इतिहास बोट, इतिहासलाई जीवित बनाउन, कुनै ऐतिहासिक पात्रको भूमिका निभाउन र त्यसको जीवन र समयका बारेमा प्रश्न सोध्न सकिने बोट बनाउनूहोस्।

## समाधान

### स्टडी बडी

तल एउटा सुरुवाती प्रम्प्ट छ, यसलाई प्रयोग गरेर आफ्नो इच्छाअनुसार परिमार्जन गर्नुहोस्।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

यहाँ केही प्रम्प्टहरू छन् जुन तपाईं प्रयोग गर्न सक्नुहुन्छ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जाँच

तापक्रम (temperature) को अवधारणाले के गर्छ?

1. यसले आउटपुट कति अनियमित हुनेछ नियंत्रित गर्छ।
1. यसले जवाफ कति ठूलो हुन्छ नियन्त्रण गर्छ।
1. यसले कति टोकन प्रयोग हुन्छ नियन्त्रण गर्छ।

## 🚀 चुनौती

कार्य गर्ने क्रममा तापक्रम फरक फरक राखेर प्रयास गर्नुहोस्, जस्तै 0, 0.5, र 1। सम्झनुहोस् 0 सबैभन्दा स्थिर हुन्छ र 1 सबैभन्दा विविध। कुन मान तपाईंको एपका लागि उत्तम काम गर्छ?

## राम्रो काम! आफ्नो सिकाइलाई जारी राख्नुहोस्

यो पाठ पुरा गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) हेर्नुहोस् र आफ्नो Generative AI ज्ञानमा अझ उन्नति गर्नुहोस्!

पाठ 7 मा जानुहोस् जहाँ हामी [च्याट एप्लिकेशनहरू कसरी बनाउन](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) भन्ने कुरा हेरौं!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->