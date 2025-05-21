<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:50:02+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ne"
}
-->
# पाठ्य निर्माण अनुप्रयोगहरू निर्माण गर्दै

[![पाठ्य निर्माण अनुप्रयोगहरू निर्माण गर्दै](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.ne.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(यस पाठको भिडियो हेर्न माथिको चित्रमा क्लिक गर्नुहोस्)_

यस पाठ्यक्रममा अहिलेसम्म तपाईंले देख्नुभएको छ कि त्यहाँ प्रोत्साहनहरू जस्ता कोर अवधारणाहरू छन् र "प्रोत्साहन इन्जिनियरिङ" भनिने सम्पूर्ण विषय पनि छ। धेरै उपकरणहरू जससँग तपाईं अन्तरक्रिया गर्न सक्नुहुन्छ जस्तै ChatGPT, Office 365, Microsoft Power Platform र अन्य, तपाईंलाई केहि गर्न प्रोत्साहनहरू प्रयोग गर्न समर्थन गर्छन्।

तपाईंले कुनै अनुप्रयोगमा यस्ता अनुभव थप्नको लागि, तपाईंले प्रोत्साहन, पूरा र काम गर्न पुस्तकालय चयन गर्ने जस्ता अवधारणाहरू बुझ्न आवश्यक छ। यही कुरा तपाईंले यस अध्यायमा सिक्नुहुनेछ।

## परिचय

यस अध्यायमा, तपाईंले:

- openai पुस्तकालय र यसको कोर अवधारणाहरूको बारेमा सिक्नुहोस्।
- openai प्रयोग गरेर पाठ्य निर्माण अनुप्रयोग निर्माण गर्नुहोस्।
- प्रोत्साहन, तापक्रम, र टोकनहरू जस्ता अवधारणाहरू कसरी प्रयोग गर्ने भनेर बुझ्न, पाठ्य निर्माण अनुप्रयोग निर्माण गर्न।

## सिकाइ लक्ष्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- पाठ्य निर्माण अनुप्रयोग के हो भनेर व्याख्या गर्नुहोस्।
- openai प्रयोग गरेर पाठ्य निर्माण अनुप्रयोग निर्माण गर्नुहोस्।
- आफ्नो अनुप्रयोगलाई थप वा कम टोकनहरू प्रयोग गर्न र तापक्रम परिवर्तन गर्न कन्फिगर गर्नुहोस्, विविध आउटपुटको लागि।

## पाठ्य निर्माण अनुप्रयोग के हो?

सामान्यतया जब तपाईं अनुप्रयोग निर्माण गर्नुहुन्छ यसमा निम्न जस्तो केही प्रकारको इन्टरफेस हुन्छ:

- आदेश-आधारित। कन्सोल अनुप्रयोगहरू सामान्य अनुप्रयोगहरू हुन् जहाँ तपाईं आदेश टाइप गर्नुहुन्छ र यसले कार्य सम्पन्न गर्छ। उदाहरणको लागि, `git` एक आदेश-आधारित अनुप्रयोग हो।
- प्रयोगकर्ता इन्टरफेस (UI)। केही अनुप्रयोगहरूमा ग्राफिकल प्रयोगकर्ता इन्टरफेसहरू (GUIs) हुन्छन् जहाँ तपाईं बटनहरू क्लिक गर्नुहुन्छ, पाठ इनपुट गर्नुहुन्छ, विकल्पहरू चयन गर्नुहुन्छ र थप।

### कन्सोल र UI अनुप्रयोगहरू सीमित छन्

यसलाई आदेश-आधारित अनुप्रयोगसँग तुलना गर्नुहोस् जहाँ तपाईं आदेश टाइप गर्नुहुन्छ:

- **यो सीमित छ**। तपाईं कुनै पनि आदेश टाइप गर्न सक्नुहुन्न, केवल ती जो अनुप्रयोगले समर्थन गर्छ।
- **भाषा विशेष**। केही अनुप्रयोगहरूले धेरै भाषाहरू समर्थन गर्छन्, तर डिफल्टमा अनुप्रयोग विशेष भाषाको लागि निर्माण गरिएको हुन्छ, यदि तपाईं थप भाषा समर्थन थप्न सक्नुहुन्छ भने पनि।

### पाठ्य निर्माण अनुप्रयोगहरूको लाभ

त्यसोभए पाठ्य निर्माण अनुप्रयोग कसरी फरक छ?

पाठ्य निर्माण अनुप्रयोगमा, तपाईंले अधिक लचिलोपन प्राप्त गर्नुहुन्छ, तपाईं एक आदेशको सेट वा विशेष इनपुट भाषामा सीमित हुनुहुन्न। यसको सट्टा, तपाईंले प्राकृतिक भाषाको प्रयोग गरेर अनुप्रयोगसँग अन्तरक्रिया गर्न सक्नुहुन्छ। अर्को लाभ यो हो कि तपाईं पहिले नै जानकारीको विशाल कोषमा प्रशिक्षित गरिएको डाटा स्रोतसँग अन्तरक्रिया गर्दै हुनुहुन्छ, जबकि पारम्परिक अनुप्रयोग डेटाबेसमा सीमित हुन सक्छ।

### पाठ्य निर्माण अनुप्रयोगको साथ म के निर्माण गर्न सक्छु?

धेरै कुराहरू तपाईं निर्माण गर्न सक्नुहुन्छ। उदाहरणका लागि:

- **च्याटबट**। च्याटबटले तपाईंको कम्पनी र यसको उत्पादनहरू जस्ता विषयहरूमा प्रश्नहरूको उत्तर दिन सक्ने राम्रो मिलान हुन सक्छ।
- **सहायक**। LLMs पाठलाई संक्षेपमा प्रस्तुत गर्ने, पाठबाट अन्तर्दृष्टि प्राप्त गर्ने, रेजुमे जस्ता पाठ उत्पादन गर्ने जस्ता कुराहरूमा उत्कृष्ट छन्।
- **कोड सहायक**। तपाईंले प्रयोग गर्ने भाषा मोडेलको आधारमा, तपाईंले कोड लेख्न मद्दत गर्ने कोड सहायक निर्माण गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाईंले GitHub Copilot जस्तै उत्पादनको साथ साथै ChatGPT प्रयोग गर्न सक्नुहुन्छ जसले तपाईंलाई कोड लेख्न मद्दत गर्छ।

## म कसरी सुरु गर्न सक्छु?

खैर, तपाईंले LLMसँग एकीकृत गर्ने तरिका फेला पार्न आवश्यक छ जुन सामान्यतया निम्न दुई दृष्टिकोणहरू समावेश गर्दछ:

- API प्रयोग गर्नुहोस्। यहाँ तपाईंले आफ्नो प्रोत्साहनको साथ वेब अनुरोधहरू निर्माण गर्दै हुनुहुन्छ र उत्पन्न पाठ फर्काउँछन्।
- पुस्तकालय प्रयोग गर्नुहोस्। पुस्तकालयहरूले API कलहरू संक्षेपमा प्रस्तुत गर्न मद्दत गर्छन् र तिनीहरूलाई प्रयोग गर्न सजिलो बनाउँछन्।

## पुस्तकालयहरू/SDKs

LLMs सँग काम गर्नका लागि केही राम्ररी परिचित पुस्तकालयहरू छन् जस्तै:

- **openai**, यो पुस्तकालयले तपाईंको मोडेलमा जडान गर्न र प्रोत्साहनहरू पठाउन सजिलो बनाउँछ।

त्यसपछि त्यहाँ उच्च स्तरमा सञ्चालन गर्ने पुस्तकालयहरू छन् जस्तै:

- **Langchain**। Langchain राम्ररी परिचित छ र Pythonलाई समर्थन गर्छ।
- **Semantic Kernel**। Semantic Kernel Microsoft द्वारा एक पुस्तकालय हो जसले C#, Python, र Java भाषाहरूलाई समर्थन गर्छ।

## openai प्रयोग गरेर पहिलो अनुप्रयोग

हेरौं कसरी हामीले पहिलो अनुप्रयोग निर्माण गर्न सक्छौं, कुन पुस्तकालयहरू आवश्यक छन्, कति आवश्यक छ र यस्तै।

### openai स्थापना गर्नुहोस्

OpenAI वा Azure OpenAI सँग अन्तरक्रिया गर्नका लागि त्यहाँ धेरै पुस्तकालयहरू छन्। विभिन्न प्रोग्रामिङ भाषाहरू जस्तै C#, Python, JavaScript, Java र अन्य प्रयोग गर्न सम्भव छ। हामीले `openai` Python पुस्तकालय प्रयोग गर्ने छनौट गरेका छौं, त्यसैले हामीले `pip` प्रयोग गरेर यसलाई स्थापना गर्नेछौं।

```bash
pip install openai
```

### स्रोत सिर्जना गर्नुहोस्

तपाईंले निम्न चरणहरू पूरा गर्न आवश्यक छ:

- Azure मा खाता सिर्जना गर्नुहोस् [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI मा पहुँच प्राप्त गर्नुहोस्। [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) मा जानुहोस् र पहुँचको लागि अनुरोध गर्नुहोस्।

  > [!NOTE]
  > लेख्दाको समयमा, तपाईंले Azure OpenAI मा पहुँचको लागि आवेदन दिन आवश्यक छ।

- Python स्थापना गर्नुहोस् <https://www.python.org/>
- Azure OpenAI सेवा स्रोत सिर्जना गरिएको छ। [स्रोत सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) कसरी गर्ने यो मार्गदर्शिका हेर्नुहोस्।

### API कुञ्जी र अन्त बिन्दु स्थान निर्धारण गर्नुहोस्

यस समयमा, तपाईंले आफ्नो `openai` पुस्तकालयलाई कुन API कुञ्जी प्रयोग गर्ने भनेर बताउनु आवश्यक छ। तपाईंको API कुञ्जी फेला पार्न, Azure OpenAI स्रोतको "कुञ्जीहरू र अन्त बिन्दु" खण्डमा जानुहोस् र "कुञ्जी 1" मान प्रतिलिपि गर्नुहोस्।

![Azure पोर्टलमा कुञ्जीहरू र अन्त बिन्दु स्रोत ब्लेड](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब तपाईंले यो जानकारी प्रतिलिपि गर्नुभएको छ, पुस्तकालयहरूलाई यसलाई प्रयोग गर्न निर्देशन दिनुहोस्।

> [!NOTE]
> तपाईंको API कुञ्जीलाई तपाईंको कोडबाट अलग गर्नुहोस्। तपाईंले वातावरणीय चरहरूको प्रयोग गरेर यसो गर्न सक्नुहुन्छ।
>
> - वातावरणीय चर सेट गर्नुहोस् `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Azure कन्फिगरेसन सेटअप गर्नुहोस्

यदि तपाईं Azure OpenAI प्रयोग गर्दै हुनुहुन्छ भने, यहाँ कसरी कन्फिगरेसन सेटअप गर्ने:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

माथि हामीले निम्न सेट गरिरहेका छौं:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` वर्ग। यहाँ एक उदाहरण छ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

माथिको कोडमा, हामीले एक पूरा वस्तु सिर्जना गरेका छौं र प्रयोग गर्न चाहेको मोडेल र प्रोत्साहन पास गरेका छौं। त्यसपछि हामी उत्पन्न पाठ प्रिन्ट गर्छौं।

### च्याट पूरा

अहिलेसम्म, तपाईंले देख्नुभएको छ कि हामीले कसरी `Completion` to generate text. But there's another class called `ChatCompletion` प्रयोग गरिरहेका छौं जुन च्याटबटहरूको लागि बढी उपयुक्त छ। यसलाई प्रयोग गर्ने उदाहरण यहाँ छ:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

यस कार्यक्षमता मा थप जानकारी आगामी अध्यायमा।

## व्यायाम - तपाईंको पहिलो पाठ्य निर्माण अनुप्रयोग

अब हामीले openai सेट अप र कन्फिगर गर्ने तरिका सिक्यौं, तपाईंको पहिलो पाठ्य निर्माण अनुप्रयोग निर्माण गर्ने समय हो। तपाईंको अनुप्रयोग निर्माण गर्नका लागि, यी चरणहरू अनुसरण गर्नुहोस्:

1. भर्चुअल वातावरण सिर्जना गर्नुहोस् र openai स्थापना गर्नुहोस्:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि तपाईं Windows प्रयोग गर्दै हुनुहुन्छ भने `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI स्रोत` and then select `कुञ्जीहरू र अन्त बिन्दु` and copy the `कुञ्जी 1` मान टाइप गर्नुहोस्।

1. एक _app.py_ फाइल सिर्जना गर्नुहोस् र यसमा निम्न कोड दिनुहोस्:

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
   > यदि तपाईं Azure OpenAI प्रयोग गर्दै हुनुहुन्छ भने, तपाईंले `api_type` to `azure` and set the `api_key` आफ्नो Azure OpenAI कुञ्जीमा सेट गर्न आवश्यक छ।

   तपाईंले निम्न जस्तै आउटपुट देख्नुहुनेछ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विभिन्न प्रकारका प्रोत्साहनहरू, विभिन्न कुराहरूको लागि

अब तपाईंले प्रोत्साहन प्रयोग गरेर पाठ उत्पन्न कसरी गर्ने देख्नुभएको छ। तपाईंले चलिरहेको प्रोग्राम पनि प्राप्त गर्नुभएको छ जसलाई तपाईंले परिमार्जन गर्न र परिवर्तन गर्न सक्नुहुन्छ विभिन्न प्रकारको पाठ उत्पन्न गर्न।

प्रोत्साहनहरू सबै प्रकारका कार्यहरूको लागि प्रयोग गर्न सकिन्छ। उदाहरणका लागि:

- **पाठको प्रकार उत्पन्न गर्नुहोस्**। उदाहरणका लागि, तपाईंले कविता, क्विजको लागि प्रश्नहरू आदि उत्पन्न गर्न सक्नुहुन्छ।
- **जानकारी खोज्नुहोस्**। तपाईंले निम्न उदाहरण 'वेब विकासमा CORS को अर्थ के हो?' जस्तो जानकारी खोज्न प्रोत्साहनहरू प्रयोग गर्न सक्नुहुन्छ।
- **कोड उत्पन्न गर्नुहोस्**। तपाईंले कोड उत्पन्न गर्न प्रोत्साहनहरू प्रयोग गर्न सक्नुहुन्छ, उदाहरणका लागि इमेलहरूलाई मान्य गर्न प्रयोग गरिएको नियमित अभिव्यक्ति विकास गर्न वा किन सम्पूर्ण प्रोग्राम उत्पन्न नगर्ने, जस्तै वेब अनुप्रयोग?

## एक अधिक व्यावहारिक प्रयोग केस: रेसिपी उत्पन्नकर्ता

कल्पना गर्नुहोस् तपाईंको घरमा सामग्रीहरू छन् र तपाईंले केहि पकाउन चाहनुहुन्छ। त्यसको लागि, तपाईंलाई रेसिपी आवश्यक छ। रेसिपी खोज्ने तरिका खोज इन्जिन प्रयोग गर्नु हो वा तपाईंले त्यसो गर्न LLM प्रयोग गर्न सक्नुहुन्छ।

तपाईंले निम्न जस्तै प्रोत्साहन लेख्न सक्नुहुन्छ:

> "चिकन, आलु, र गाजर सामग्रीहरू भएको पकवानको लागि 5 रेसिपीहरू देखाउनुहोस्। प्रति रेसिपी, प्रयोग गरिएका सबै सामग्रीहरू सूचीबद्ध गर्नुहोस्"

माथिको प्रोत्साहन दिइएमा, तपाईंलाई निम्न जस्तो प्रतिक्रिया प्राप्त हुन सक्छ:

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

यो नतिजा उत्कृष्ट छ, मलाई के पकाउने थाहा छ। यस समयमा, के उपयोगी सुधारहरू हुन सक्छन्:

- म नपसन्द गर्ने वा एलर्जी भएको सामग्रीहरू हटाउनुहोस्।
- किनमेल सूची उत्पादन गर्नुहोस्, यदि मेरो घरमा सबै सामग्रीहरू छैनन् भने।

माथिका केसहरूको लागि, हामीले अतिरिक्त प्रोत्साहन थपौं:

> "कृपया लसुन भएका रेसिपीहरू हटाउनुहोस् किनकि म एलर्जी छु र केहि अन्य सामग्रीसँग बदल्नुहोस्। साथै, कृपया रेसिपीहरूको लागि किनमेल सूची उत्पादन गर्नुहोस्, विचार गर्दै मसँग पहिले नै चिकन, आलु र गाजर घरमा छन्।"

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

त्यो तपाईंको पाँच रेसिपीहरू हो, कुनै लसुन उल्लेख नगरिएको र तपाईंसँग पनि घरमा के छ विचार गर्दै किनमेल सूची छ।

## व्यायाम - रेसिपी उत्पन्नकर्ता निर्माण गर्नुहोस्

अब हामीले परिदृश्य प्रदर्शन गरेका छौं, कोड लेख्न मिलाउन कोसिस गरौं। यसो गर्नका लागि, यी चरणहरू अनुसरण गर्नुहोस्:

1. _app.py_ फाइललाई सुरुवात बिन्दुको रूपमा प्रयोग गर्नुहोस्
1. `प्रोत्साहन` भेरिएबल फेला पार्नुहोस् र यसको कोडलाई निम्नमा परिवर्तन गर्नुहोस्:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   यदि तपाईंले अहिले कोड चलाउनुहुन्छ भने, तपाईंले निम्न जस्तै आउटपुट देख्नुहुनेछ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > नोट, तपाईंको LLM अनिश्चित छ, त्यसैले तपाईंले हरेक पटक कार्यक्रम चलाउँदा फरक परिणाम प्राप्त गर्न सक्नुहुन्छ।

   उत्कृष्ट, हेरौं कसरी हामीले चीजहरू सुधार गर्न सक्छौं। चीजहरू सुधार गर्नका लागि, हामीले सुनिश्चित गर्न चाहन्छौं कि कोड लचिलो छ, त्यसैले सामग्रीहरू र रेसिपीहरूको संख्या सुधार गर्न र परिवर्तन गर्न सकिन्छ।

1. कोडलाई निम्न तरिकामा परिवर्तन गरौं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   परीक्षणका लागि कोडलाई चलाउँदा, यसले यसरी देखिन सक्छ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर र किनमेल सूची थपेर सुधार गर्नुहोस्

हामीसँग अब काम गर्ने अनुप्रयोग छ जसले रेसिपीहरू उत्पादन गर्न सक्षम छ र यो लचिलो छ किनकि यसले प्रयोगकर्ताबाट इनपुटमा निर्भर गर्दछ, रेसिपीहरूको संख्या मात्र होइन तर प्रयोग गरिएका सामग्रीहरू पनि।

यसलाई थप सुधार गर्नका लागि, हामीले निम्न थप्न चाहन्छौं:

- **सामग्रीहरू फिल्टर गर्नुहोस्**। हामीले नपसन्द गर्ने वा एलर्जी भएका सामग्रीहरू फिल्टर गर्न सक्षम हुन चाहन्छौं। यस परिवर्तनलाई पूरा गर्नका लागि, हामीले हाम्रो विद्यमान प्रोत्साहनलाई सम्पादन गर्न सक्छौं र यसमा फिल्टर सर्तलाई यसरी थप्न सक्छौं:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  माथि, हामीले `{filter}` लाई प्रोत्साहनको अन्त्यमा थपेका छौं र हामीले फिल्टर मानलाई प्रयोगकर्ताबाट पनि कब्जा गरेका छौं।

  अब कार्यक्रम चलाउने उदाहरण इनपुट यसरी देखिन सक्छ:

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

  तपाईंले देख्न सक्नुहुन्छ, दूध भएका कुनै पनि रेसिपीहरू फिल्टर गरिएको छ। तर, यदि तपाईं लैक्टोज असहिष्णु हुनुहुन्छ भने, तपाईंले चीज भएका रेसिपीहरू पनि फिल्टर गर्न चाहन सक्नुहुन्छ, त्यसैले स्पष्ट हुनु आवश्यक छ।

- **किनमेल सूची उत्पादन गर्नुहोस्**। हामीले घरमा के छ विचार गर्दै किनमेल सूची उत्पादन गर्न चाहन्छौं।

  यस कार्यक्षमताको लागि, हामीले सबै कुरा एक प्रोत्साहनमा समाधान गर्ने प्रयास गर्न सक्छौं वा हामीले यसलाई दुई प्रोत्साहनहरूमा विभाजन गर्न सक्छौं। दोस्रो दृष्टिकोण प्रयास गरौं। यहाँ हामीले अतिरिक्त प्रोत्साहन थप्ने सुझाव दिएका छौं, तर त्यसको लागि काम गर्न, हामीले पहिलो प्रोत्साहनको परिणामलाई दोस्रो प्रोत्साहनको सन्दर्भमा थप्न आवश्यक छ।

  पहिलो प्रोत्साहनको परिणाम प्रिन्ट गर्ने कोडको भाग फेला पार्नुहोस् र तल निम्न कोड थप्नुहोस्:

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

  निम्न कुराहरूमा ध्यान दिनुहोस्:

  1. हामीले नयाँ प्रोत्साहन निर्माण गरिरहेका छौं पहिलो प्रोत्साहनको परिणामलाई नयाँ प्रोत्साहनमा थपेर:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हामीले नयाँ अनुरोध गरेका छौं, तर हामीले पहिलो प्रोत्साहनमा सोधेका टोकनहरूको संख्यालाई विचार गर्दै, यस पटक हामीले `max_tokens` लाई 1200 भनेका छौं।

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     यस कोडलाई चलाउँदा, हामीले निम्न आउटपुटमा पुग्छौं:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## तपाईंको सेटअप सुधार गर्नुहोस्

हामीसँग अहिलेसम्म काम गर्ने कोड छ, तर त्यहाँ केही सुधारहरू छन् जसले चीजहरूलाई अझ राम्रो बनाउने प्रयास गर्नु पर्छ। केही सुधारहरू गर्नु पर्ने कुराहरू छन्:

- **गोप्य जानकारीलाई कोडबाट अलग गर्नुहोस्**, जस्तै API कुञ्जी। गोप्य जानकारी कोडमा हुँदैन र सुरक्षित स्थानमा भण्डारण गर्नुपर्छ

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, कृपया सचेत रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोतको रूपमा मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।