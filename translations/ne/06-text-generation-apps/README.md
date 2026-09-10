# पाठ उत्पादन अनुप्रयोगहरू निर्माण गर्दै

[![पाठ उत्पादन अनुप्रयोगहरू निर्माण गर्दै](../../../translated_images/ne/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(यस पाठको भिडियो हेर्न माथि दिइएको तस्वीरमा क्लिक गर्नुहोस्)_

यो पाठ्यक्रममार्फत तपाईँले अहिलेसम्म हेर्नुभएको छ कि प्रम्प्टहरू जस्ता मूल अवधारणाहरू हुन्छन् र यहाँसम्म कि "प्रम्प्ट इन्जिनियरिङ" भनिने एक पूर्ण विषयशाखा पनि छ। धेरै उपकरणहरू जस्तै ChatGPT, Office 365, Microsoft Power Platform र अन्यहरूले केही काम पूरा गर्न प्रम्प्टहरू प्रयोग गर्न समर्थन गर्दछन्।

एउटा अनुप्रयोगमा यस्ता अनुभव थप्नको लागि तपाईँले प्रम्प्ट, पूर्णताहरू जस्ता अवधारणाहरू बुझ्न आवश्यक छ र काम गर्नको लागि एउटा पुस्तकालय चयन गर्नुपर्छ। यो बिल्कुलै यो अध्यायमा तपाईँले सिक्नु हुने कुरा हो।

## परिचय

यस अध्यायमा, तपाईँले:

- openai पुस्तकालय र यसको मूल अवधारणाहरूको बारेमा जान्नु हुनेछ।
- openai प्रयोग गरेर एक पाठ उत्पादन अनुप्रयोग निर्माण गर्नुहोस्।
- प्रम्प्ट, तापक्रम, र टोकन्स जस्ता अवधारणाहरू कसरी प्रयोग गर्ने भनेर बुझ्नुहोस् पाठ उत्पादन अनुप्रयोग बनाउन।

## सिकाइ लक्ष्यहरू

यस पाठको अन्त्यमा, तपाईँ सक्षम हुनुहुनेछ:

- पाठ उत्पादन अनुप्रयोग के हो भनेर व्याख्या गर्न।
- openai प्रयोग गरी पाठ उत्पादन अनुप्रयोग बनाउने।
- तपाईँको अनुप्रयोगलाई बढी वा कम टोकन्स प्रयोग गर्न र तापक्रम परिवर्तन गर्न कन्फिगर गर्न, विविध आउटपुटका लागि।

## पाठ उत्पादन अनुप्रयोग के हो?

सामान्यतया जब तपाईँ अनुप्रयोग बनाउनुहुन्छ त्यसमा यस्तो प्रकारको इन्टरफेस हुन्छ:

- कमाण्ड-आधारित। कन्सोल अनुप्रयोगहरू त्यस्ता अनुप्रयोगहरू हुन् जहाँ तपाईँ कमाण्ड टाइप गर्नुहुन्छ र त्यो काम सम्पन्न गर्छ। उदाहरणको लागि, `git` एउटा कमाण्ड-आधारित अनुप्रयोग हो।
- प्रयोगकर्ता इन्टरफेस (UI)। केही अनुप्रयोगहरूमा ग्राफिकल प्रयोगकर्ता इन्टरफेस (GUIs) हुन्छ जहाँ तपाईँ बटनहरू क्लिक गर्नुहुन्छ, पाठ इनपुट गर्नुहुन्छ, विकल्पहरू छान्नुहुन्छ र अन्य।

### कन्सोल र UI अनुप्रयोगहरू सीमित छन्

एउटा कमाण्ड-आधारित अनुप्रयोगसँग तुलना गर्नुहोस् जहाँ तपाईँ कमाण्ड टाइप गर्नुहुन्छ:

- **यो सीमित हुन्छ**। तपाईँले कुनै पनि कमाण्ड टाइप गर्न सक्नुहुन्न, केवल ती कमाण्डहरू जुन अनुप्रयोग समर्थन गर्छ।
- **भाषा विशेष**। केही अनुप्रयोगहरूले धेरै भाषाहरू समर्थन गर्छन्, तर डिफल्ट रूपमा अनुप्रयोग एउटा विशिष्ट भाषाको लागि बनाइएको हुन्छ, यद्यपि थप भाषा समर्थन थप्न सकिन्छ।

### पाठ उत्पादन अनुप्रयोगहरूको फाइदाहरू

त्यसैले पाठ उत्पादन अनुप्रयोग कसरी फरक छ?

पाठ उत्पादन अनुप्रयोगमा, तपाईँसँग बढी लचिलोपन हुन्छ, तपाईँ कमाण्डहरूको सेट वा कुनै विशिष्ट इनपुट भाषामा सीमित हुनुहुन्न। यसको सट्टामा, तपाईँ प्राकृतिक भाषामा अनुप्रयोगसँग संवाद गर्न सक्नुहुन्छ। अर्को फाइदा यो हो कि तपाईँ पहिले नै यस्तो डेटा स्रोतसँग संवाद गर्दै हुनुहुन्छ जुन विशाल सूचना कोर्पसमा प्रशिक्षित गरिएको छ, जुन पारंपरिक अनुप्रयोगले डेटाबेसमा भएका कुरामा सीमित हुन सक्छ।

### म पाठ उत्पादन अनुप्रयोगबाट के निर्माण गर्न सक्छु?

तपाईँ धेरै कुराहरु बनाउन सक्नुहुन्छ। उदाहरणका लागि:

- **एक च्याटबोट**। तपाईँको कम्पनी र यसका उत्पादनहरू सम्बन्धी प्रश्नहरूको जवाफ दिने च्याटबोट राम्रो मेल हुन सक्छ।
- **सहायक**। LLMs पाठ सारांश गर्ने, पाठबाट अन्तर्दृष्टि निकाल्ने, रिजुमे जस्ता पाठ उत्पादन गर्ने काममा उत्कृष्ट हुन्छन्।
- **कोड सहायक**। तपाईँ प्रयोग गर्ने भाषागत मोडेलमा निर्भर गर्दै, तपाईँ एउटा कोड सहायक बनाउन सक्नुहुन्छ जुन तपाईँलाई कोड लेख्न मद्दत गर्छ। उदाहरणका लागि, GitHub Copilot वा ChatGPT जस्ता उत्पादनहरू प्रयोग गर्न सक्नुहुन्छ।

## म कसरी सुरु गर्न सक्छु?

तийм, तपाईँले एउटा LLM सँग एकीकृत गर्ने तरिका फेला पार्नुपर्छ जुन सामान्यतया यी दुई तरिकाहरू हुन्छन्:

- API प्रयोग गर्नुहोस्। यहाँ तपाईँ तपाईँको प्रम्प्टसँग वेब अनुरोधहरू निर्माण गर्नुहुन्छ र टेक्स्ट प्राप्त गर्नुहुन्छ।
- पुस्तकालय प्रयोग गर्नुहोस्। पुस्तकालयहरूले API कलहरू समेट्छन् र प्रयोग गर्न सजिलो बनाउँछन्।

## पुस्तकालयहरू/SDK हरू

LLMs संग काम गर्ने केही प्रसिद्ध पुस्तकालयहरू छन्:

- **openai**, यस पुस्तकालयले तपाईँको मोडेलसँग जडान गर्न र प्रम्प्टहरू पठाउन सजिलो बनाउँछ।

त्यसपछि माथिल्लो तहमा काम गर्ने पुस्तकालयहरू छन् जस्तै:

- **Langchain**। Langchain राम्रो परिचित छ र Python समर्थन गर्छ।
- **Semantic Kernel**। Semantic Kernel माइक्रोसफ्टको पुस्तकालय हो जसले C#, Python, र Java भाषाहरू समर्थन गर्छ।

## openai प्रयोग गरेर पहिलो अनुप्रयोग

हेर्नुहोस् हामी कसरी हाम्रो पहिलो अनुप्रयोग बनाउन सक्छौं, कुन पुस्तकालयहरू चाहिन्छ, कति आवश्यक छ र यस्तै।

### openai स्थापना गर्नुहोस्

OpenAI वा Azure OpenAI सँग इन्टर्याक्ट गर्न धेरै पुस्तकालयहरू उपलब्ध छन्। बिभिन्न प्रोग्रामिङ भाषाहरू पनि प्रयोग गर्न सकिन्छ जस्तै C#, Python, JavaScript, Java र अन्य। हामीले `openai` Python पुस्तकालय चयन गरेका छौं, त्यसैले हामी `pip` प्रयोग गरेर यसलाई स्थापना गर्नेछौं।

```bash
pip install openai
```

### स्रोत सिर्जना गर्नुहोस्

तपाईँले निम्न कदमहरू लिनुपर्छ:

- Azure मा एक खाता सिर्जना गर्नुहोस् [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI पहुँच प्राप्त गर्नुहोस्। जानुहोस् [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) र पहुँचको लागि अनुरोध गर्नुहोस्।

  > [!NOTE]
  > लेख्दा समयमा, तपाईंले Azure OpenAI पहुँचको लागि आवेदन दिनु आवश्यक छ।

- Python स्थापना गर्नुहोस् <https://www.python.org/>
- Azure OpenAI सेवा स्रोत सिर्जना गर्नु भएको छ। यस गाइड हेर्नुहोस् कसरी [स्रोत सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुञ्जी र अन्तबिन्दु (endpoint) पत्ता लगाउनुहोस्

यो बिन्दुमा, तपाईँले `openai` पुस्तकालयलाई कुन API कुञ्जी प्रयोग गर्ने भन्नुपर्नेछ। तपाईँको API कुञ्जी फेला पार्न जानुहोस् Azure OpenAI स्रोतको " कुञ्जीहरू र अन्तबिन्दु" भागमा र "Key 1" मान कॉपी गर्नुहोस्।

![Azure Portal मा कुञ्जीहरू र अन्तबिन्दु स्रोत ब्लेड](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब तपाईंसँग यी विवरणहरू छन्, पुस्तकालयहरूलाई यसलाई प्रयोग गर्न निर्देशन दिनुहोस्।

> [!NOTE]
> तपाईँको API कुञ्जीलाई कोडबाट अलग राख्नु राम्रो हुन्छ। यसलाई वातावरणीय चरहरू प्रयोग गरेर गर्न सकिन्छ।
>
> - वातावरणीय चर `OPENAI_API_KEY` तपाईँको API कुञ्जीमा सेट गर्नुहोस्।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कन्फिगरेसन सेटअप गर्नुहोस्

यदि तपाईँ Azure OpenAI (अहिले Microsoft Foundry को भाग) प्रयोग गर्दै हुनुहुन्छ भने, यसरी कन्फिगरेसन सेटअप गर्नुहोस्। हामी सामान्य `OpenAI` क्लाएन्ट प्रयोग गर्छौं जुन Azure OpenAI `/openai/v1/` अन्तबिन्दुमा निर्देशित हुन्छ, जुन Responses API सँग काम गर्छ र `api_version` चाहिँदैन:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

माथि हामीले निम्न कुरा सेट गरिरहेका छौं:

- `api_key`, यो तपाईँको API कुञ्जी हो जुन Azure Portal वा Microsoft Foundry पोर्टलबाट प्राप्त हुन्छ।
- `base_url`, यो तपाईँको Foundry स्रोत अन्तबिन्दु हो जसमा `/openai/v1/` थपिएको हुन्छ। स्थिर v1 अन्तबिन्दु OpenAI र Azure OpenAI दुबैमा बिना `api_version` व्यवस्थापन काम गर्छ।

> [!NOTE] > `os.environ` वातावरणीय चरहरू पढ्छ। तपाईँ यसलाई `AZURE_OPENAI_API_KEY` र `AZURE_OPENAI_ENDPOINT` जस्ताहरू पढ्न प्रयोग गर्न सक्नुहुन्छ। यी वातावरणीय चरहरू तपाईँको टर्मिनलमा वा `dotenv` जस्तो पुस्तकालय प्रयोग गरेर सेट गर्नुहोस्।

## पाठ उत्पादन गर्नुहोस्

पाठ उत्पादन गर्ने तरिका हो Responses API मार्फत `responses.create` विधि प्रयोग गर्नु। यहाँ एउटा उदाहरण छ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # यो तपाईंको मोडेल डिप्लॉयमेन्ट नाम हो
    input=prompt,
    store=False,
)
print(response.output_text)
```

माथिको कोडमा, हामी एउटा प्रतिक्रिया सिर्जना गर्छौं र जुन मोडेल प्रयोग गर्ने र प्रम्प्ट पठाउने बताउँछौं। त्यसपछि हामी `response.output_text` मार्फत उत्पन्न पाठ प्रिन्ट गर्छौं।

### बहु-टक कन्वर्सेसनहरू

Responses API एकटक पाठ उत्पादन र बहु-टक च्याटबोटहरूको लागि उपयुक्त छ - तपाईँले `input` मा सन्देशहरूको सूची दिनुहुन्छ कुराकानी बनाउन:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

यस कार्यक्षमतामा थप कुरा आउने अध्यायमा हुनेछ।

## अभ्यास - तपाईँको पहिलो पाठ उत्पादन अनुप्रयोग

अब जब हामीले openai कसरी सेट अप गर्ने र कन्फिगर गर्ने कुरा सिक्यौं, तपाईँको पहिलो पाठ उत्पादन अनुप्रयोग बनाउने समय हो। अनुप्रयोग बनाउनका लागि यी कदमहरू अनुसरण गर्नुहोस्:

1. भर्चुअल वातावरण सिर्जना गर्नुहोस् र openai स्थापना गर्नुहोस्:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि तपाईँ Windows प्रयोग गर्दै हुनुहुन्छ भने `venv\Scripts\activate` टाइप गर्नुहोस् `source venv/bin/activate` को सट्टा।

   > [!NOTE]
   > तपाईँको Azure OpenAI कुञ्जी पत्ता लगाउन जानुहोस् [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) र `Open AI` खोज्नुहोस्, `Open AI resource` चयन गर्नुहोस्, त्यसपछि `Keys and Endpoint` जाँदा `Key 1` मूल्य कॉपी गर्नुहोस्।

1. _app.py_ फाइल सिर्जना गर्नुहोस् र त्यसमा निम्न कोड राख्नुहोस्:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # तपाईंको पूरा गर्ने कोड थप्नुहोस्
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API प्रयोग गरेर अनुरोध गर्नुहोस्
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिक्रिया प्रिन्ट गर्नुहोस्
   print(response.output_text)
   ```

   > [!NOTE]
   > यदि तपाईँ सामान्य OpenAI (Azure नभएको) प्रयोग गर्दै हुनुहुन्छ भने `client = OpenAI(api_key="<replace this value with your OpenAI key>")` प्रयोग गर्नुहोस् (`base_url` छैन) र मोडेल नाम जस्तै `gpt-5-mini` पास गर्नुहोस् प्रक्षेपण नामको सट्टा।

   तपाईँले यस्तो आउटपुट देख्नु पर्नेछ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## फरक-फरक प्रकारका प्रम्प्टहरू, फरक-फरक कुराको लागि

अब तपाईँले हेर्नुभयो कसरी प्रम्प्ट प्रयोग गरेर पाठ उत्पादन गर्ने। तपाईँसँग यस्तो कार्यक्रम छ जुन तपाईँ परिमार्जन गरेर फरक प्रकारका पाठ उत्पादन गर्न सक्नुहुन्छ।

प्रम्प्टहरू सबै प्रकारका कार्यहरूका लागि प्रयोग गर्न सकिन्छ। उदाहरणका लागि:

- **पाठको प्रकार उत्पादन गर्नुहोस्**। उदाहरणका लागि, तपाईँ कविताहरु, प्रश्नहरू जस्तै सिर्जना गर्न सक्नुहुन्छ।
- **जानकारी खोज्नुहोस्**। तपाईँ प्रम्प्टहरू प्रयोग गरेर यस्तो प्रश्नहरूको जानकारी खोज्न सक्नुहुन्छ जस्तै 'वेब विकासमा CORS को अर्थ के हो?'।
- **कोड उत्पादन गर्नुहोस्**। तपाईँ प्रम्प्टहरू प्रयोग गरेर कोड निर्मित गर्न सक्नुहुन्छ, उदाहरण स्वरूप इमेलहरू मान्य गर्न रेगुलर एक्सप्रेशन विकास गर्ने वा पुरै कार्यक्रम जस्तै वेब अनुप्रयोग बनाउन।

## एउटा थप व्यवहारिक उपयोग केस: एउटा रेसिपी जेनरेटर

कल्पना गर्नुहोस् तपाईंसँग घरमा सामग्रीहरू छन् र तपाईँ केही पकाउन चाहनुहुन्छ। त्यसको लागि तपाईँलाई रेसिपी चाहिन्छ। रेसिपी खोज्नको लागि तपाईँ सर्च इन्जिन प्रयोग गर्न सक्नुहुन्छ वा LLM प्रयोग गर्न सक्नुहुन्छ।

तपाईँ यस्तो प्रम्प्ट लेख्न सक्नुहुन्छ:

> "मलाई यी सामग्रीहरूसँग ५ वटा परिकारहरूको रेसिपी देखाउनुहोस्: कुखुरा, आलु र गाजरहरू। प्रत्येक रेसिपीमा सबै प्रयुक्त सामग्रीहरूको सूची दिनुहोस्"

माथिको प्रम्प्ट दिएपछि, तपाईँ यस्तो प्रतिक्रिया पाउन सक्नुहुन्छ:

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

यो परिणाम राम्रो छ, म के पकाउने थाहा पाएँ। अहिलेसम्म, उपयोगी सुधारहरू हुन सक्छन्:

- म मन नपर्ने वा मलाई एलर्जी हुने सामग्रीहरू फिल्टर गर्नु।
- किनमेल सूची तयार गर्नु, यदि घरमा सबै सामग्री छैन भने।

माथिका अवस्थाहरूको लागि, अर्को प्रम्प्ट थपौं:

> "कृपया लसुन भएका रेसिपीहरू हटाउनुहोस् किनभने मलाई एलर्जी छ र त्यसलाई केही अरूले प्रतिस्थापन गर्नुहोस्। रेसिपीहरूको लागि किनमेल सूची पनि तयार गर्नुहोस्, मसँग पहिले नै कुखुरा, आलु र गाजर छ।"

अब तपाईंसँग नयाँ नतिजा छ, जुन हो:

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

ती तपाईँका पाँच रेसिपीहरू हुन्, जसमा कुनै लसुन छैन र घरमा भएका सामग्रीहरूलाई ध्यानमा राखेर किनमेल सूची समेत छ।

## अभ्यास - रेसिपी जेनरेटर बनाउनुहोस्

अहिले हामीले एउटा परिदृश्य खेल्दै सिक्यौं, अब त्यस परिदृश्य अनुसार कोड लेखौं। यसका लागि यी चरणहरू पालना गर्नुहोस्:

1. पहिलाको _app.py_ फाइललाई सुरुवात बिन्दुका रूपमा प्रयोग गर्नुहोस्
1. `prompt` चरहरू फेला पार्नुहोस् र त्यसको कोड निम्नमा परिवर्तन गर्नुहोस्:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   अब यदि तपाईँ कोड चलाउनु भयो भने, यो जस्तो नतिजा देखिनु पर्नेछ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > नोट, तपाईँको LLM अपरिभाषित हुन्छ, त्यसैले हरेक पटक दौडाउँदा फरक नतिजा आउन सक्छ।

   राम्रो, अब सुधार कसरी गर्ने हेरौं। सुधार गर्ने हेतुले हामी चाहन्छौं कोड लचिलो होस्, ताकि सामग्रीहरू र रेसिपीहरूको संख्या परिवर्तन गर्न सकियोस्।

1. अब कोड यस प्रकार परिवर्तन गरौं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # पकाउने विधिहरूको संख्या र सामग्रीहरूलाई प्रॉम्प्टमा समाहित गर्नुहोस्
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   परीक्षण दौडका लागि कोड यसरी देखिन सक्छ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर र किनमेल सूची थपेर सुधार गर्नुहोस्

अब हामीसँग काम गर्ने अनुप्रयोग छ जुन रेसिपी उत्पादन गर्न सक्छ र यो प्रयोगकर्ताका इनपुटहरूमा भर पर्दछ, रेसिपीहरूको संख्या र सामग्री दुवैमा लचिलो छ।

थप सुधार गर्नका लागि, हामीले यी थप्न चाहन्छौं:

- **सामग्रीहरू फिल्टर गर्नुहोस्**। हामी आफ्ना मन नपर्ने वा एलर्जी हुने सामग्रीहरू फिल्टर गर्न सक्षम हुन चाहन्छौं। यसका लागि हामीले हाम्रो प्रम्प्ट सम्पादन गरी यसमा फिल्टर सर्तको अन्त्यमा थप गर्न सक्छौं यसरी:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

माथि, हामीले `{filter}` प्रम्प्टको अन्त्यमा थप्यौं र प्रयोगकर्ताबाट फिल्टर मूल्य पनि समात्यौं।

कार्यक्रम चलाउँदा यो इनपुट जस्तो देखिन सक्छ:

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

जस्तो तपाईँले देख्नुभयो, दूध भएका कुनै पनि रेसिपीहरू फिल्टर गरिएको छ। यदि तपाईँलाई लैक्टोज असहिष्णुता छ भने, तपाईँ चीज भएका रेसिपीहरू पनि फिल्टर गर्न चाहनुहुन्छ, त्यसैले स्पष्ट हुन आवश्यक छ।


- **किनमेल सूची तयार पार्नुहोस्**। हामीले पहिले नै घरमा के छ भन्ने विचार गर्दै किनमेल सूची तयार पार्न चाहन्छौं।

  यो कार्यक्षमता को लागि, हामीले सबै कुरा एउटै प्रम्प्टमा समाधान गर्न सक्नेछौं वा यसलाई दुई प्रम्प्टहरूमा विभाजन गर्न सक्नेछौं। हामी दोस्रो तरिका प्रयास गरौं। यहाँ हामी थप प्रम्प्ट थप्न सल्लाह दिँदैछौं, तर त्यसका लागि पहिलो प्रम्प्टको नतिजालाई दोस्रो प्रम्प्टको सन्दर्भमा थप्न आवश्यक छ।

  कोडमा त्यो भाग पत्ता लगाउनुहोस् जुन पहिलो प्रम्प्टको नतिजा प्रिन्ट गर्छ र तलको कोड थप्नुहोस्:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया प्रिन्ट गर्नुहोस्
  print("Shopping list:")
  print(response.output_text)
  ```

  तलका कुरा ध्यान दिनुहोस्:

  1. हामी नयाँ प्रम्प्ट बनाउन पहिलो प्रम्प्टको नतिजा नयाँ प्रम्प्टमा थप्दैछौं:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हामी नयाँ अनुरोध गर्छौं, तर पहिलो प्रम्प्टमा सोधिएको टोकनहरूको संख्या पनि विचार गर्दै, यस पटक `max_output_tokens` 1200 हुन्छ भनिरहेका छौं।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     यो कोड चलाउँदा, हामीले तल को परिणाम पाउँछौं:

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

अहिलेसम्म हाम्रोसँग काम गर्ने कोड छ, तर अझ सुधार गर्न केही परिमार्जनहरू गर्नुपर्छ। केही गर्नुपर्ने कुरा यसप्रकार छन्:

- **गोप्य जानकारीलाई कोडबाट अलग गर्नुहोस्**, जस्तै API कुञ्जी। गोप्य जानकारी कोडमा हुनुहुँदैन र सुरक्षा भएको स्थानमा राखिनु पर्छ। गोप्य जानकारीलाई कोडबाट अलग गर्न हामी वातावरण चर र `python-dotenv` जस्ता पुस्तकालयहरू प्रयोग गरेर फाइलबाट लोड गर्न सक्छौं। कोडमा यसरी देखिन्छ:

  1. `.env` फाइल तलको सामग्रीसहित बनाउनुहोस्:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > नोट, Microsoft Foundry मा Azure OpenAI का लागि, तलका वातावरण चरहरू सेट गर्न आवश्यक छ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमा, तपाईं यसरी वातावरण चरहरू लोड गर्नुहुन्छ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लम्बाइ को बारेमा एक शब्द**। हामीले चाहेको टेक्स्ट उत्पादन गर्न कति टोकनहरू चाहिन्छ भनेर विचार गर्नु पर्छ। टोकनहरू लागत लाग्छ, त्यसैले जतिसक्दो कम टोकन प्रयोग गर्ने प्रयास गर्नु पर्छ। उदाहरणका लागि, के हामी प्रम्प्ट यसरी राख्न सक्छौं कि कम टोकन प्रयोग हुन्छ?

  टोकनहरू परिवर्तन गर्न, तपाईं `max_output_tokens` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, १०० टोकनहरू प्रयोग गर्न चाहनुहुन्छ भने यसो गर्नुहोस्:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **तापक्रम (temperature) संग प्रयोग गर्ने प्रयोग**। तापक्रम के हो भन्ने हामी अहिलेसम्म बताएको छैन तर यो हाम्रो प्रोग्रामले कसरी काम गर्दछ भन्ने महत्वपूर्ण सन्दर्भ हो। तापक्रमको मान उच्च हुँदा आउटपुट बढी अनियमित हुन्छ। तापक्रमको मान कम हुँदा आउटपुट अधिक पूर्वानुमानयोग्य हुन्छ। तपाईंको आउटपुटमा विविधता चाहिन्छ कि हुँदैन भनेर विचार गर्नुहोस्।

  तापक्रम परिवर्तन गर्न, तपाईं `temperature` प्यारामिटर प्रयोग गर्न सक्नुहुन्छ। उदाहरणका लागि, ०.५ तापक्रम प्रयोग गर्न चाहानुहुन्छ भने यसो गर्नुहोस्:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > नोट, १.० को नजिक हुँदा आउटपुट बढी विभिन्न हुन्छ।

- **तर्क गर्ने मोडेलहरूले `temperature` प्रयोग गर्दैनन्**। यो २०२६ को एक महत्वपूर्ण परिवर्तन हो। Microsoft Foundry मा हालको, डिप्रेकेट नभएका मोडेलहरू **तर्क गर्ने मोडेलहरू** हुन् (GPT-5 परिवार, o-series) - र तिनीहरूले `temperature` वा `top_p` समर्थन गर्दैनन् (र `max_tokens` होइन; `max_output_tokens` प्रयोग गर्नुहोस्)। यदि तपाईं `gpt-5-mini` मा `temperature` पठाउनु भयो भने "parameter not supported" त्रुटि आउँछ। तसर्थ माथिको तापक्रम उदाहरण प्रयास गर्न, यस्तो मोडेलमा प्रयोग गर्नुहोस् जसले अझै sampling control समर्थन गर्छ - जस्तै खुला **Llama** मोडेल `Llama-3.3-70B-Instruct` [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) बाट, Foundry Models / Azure AI Inference endpoint मार्फत कल गरिन्छ (जस्तै `githubmodels-*` नमूनाहरूमा)। GPT-5 जस्ता तर्क मोडेलहरूमा आउटपुटलाई फरक प्रकारले नियन्त्रण गरिन्छ:
  - **प्रम्प्ट इन्जिनियरिङ** - स्पष्ट निर्देशनहरू, उदाहरणहरू, र संरचित आउटपुट (पाठ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्) sampling controls को काम गर्दछन्।
  - **तर्क नियन्त्रणहरू** - reasoning effort/verbosity जस्ता प्यारामिटरहरूले reasoning को गहिराइलाई विलम्ब र लागतसँग सन्तुलन गर्छन्।

  संक्षेपमा: `temperature`/`top_p` धेरै मोडेलहरू (Llama, Mistral, Phi, र GPT-4.x परिवार - यद्यपि GPT-4.x डिप्रेकेट हुँदैछ) मा अझै मान्य छन्, तर दिशा तर्क मोडेलहरूजस्तै GPT-5 को लागि प्रम्प्ट इन्जिनियरिङ + reasoning controls तर्फ छ।

## कार्यपत्र

यस कार्यपत्रमा, तपाईं के बनाउन चाहनुहुन्छ रोज्न सक्नुहुन्छ।

यहाँ केही सुझावहरू छन्:

- रेसिपी जेनेरेटर एप्लिकेसनलाई अझ सुधार गर्न ट्यून गर्नुहोस्। तापक्रम मानहरू र प्रम्प्टहरूसँग खेल्नुहोस् र के कुराहरू निक्लिन्छन् हेर्नुहोस्।
- "स्टडी बडी" बनाउनुहोस्। यो एप्लिकेसनले एउटा विषय बारे प्रश्नहरूको उत्तर दिन सक्नुपर्छ, उदाहरणका लागि Python। तपाईंले प्रम्प्टहरू राख्न सक्नुहुन्छ, जस्तै "Python मा कुनै विषय के हो?", वा "कुनै विषयको कोड देखाउनुहोस्" आदि।
- इतिहास बोट, इतिहासलाई जीवन्त बनाउनुहोस्, बोटलाई कुनै ऐतिहासिक पात्रको भूमिका दिने र त्यसको जीवन तथा समयमा प्रश्न गर्ने।

## समाधान

### स्टडी बडी

तल एउटा सुरुवाती प्रम्प्ट छ, यसलाई कसरी प्रयोग गर्ने र आफ्नो इच्छाअनुसार कसरी परिमार्जन गर्ने हेर्नुहोस्।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

तपाईंले प्रयोग गर्न सक्ने केही प्रम्प्टहरू यहाँ छन्:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जाँच

तापक्रम (temperature) अवधारणाले के गर्छ?

1. यसले आउटपुट कति अनियमित हुन्छ नियन्त्रण गर्छ।
1. यसले जवाफ कति ठूलो हुन्छ नियन्त्रण गर्छ।
1. यसले कति टोकनहरू प्रयोग हुनेछन् नियन्त्रण गर्छ।

## 🚀 चुनौती

कार्यपत्रमा काम गर्दा तापक्रमलाई विभिन्न बनाउन प्रयास गर्नुहोस्, ०, ०.५, र १ मा सेट गर्नुहोस्। याद राख्नुस् ० सबैभन्दा कम विविधता र १ सबैभन्दा बढी विविधता हो। तपाईंको एपका लागि कुन मान सबैभन्दा राम्रो काम गर्छ?

## उत्कृष्ट काम! आफ्नो सिकाइ जारी राख्नुहोस्

यो पाठ समाप्त गरेपछि, हाम्रो [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मा हेर्नुहोस् र तपाईंको Generative AI ज्ञान बढाउनुहोस्!

पाठ ७ मा जानुहोस् जहाँ हामी [च्याट एप्लिकेसनहरू कसरी बनाउने](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) हेरिन्छौं!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->