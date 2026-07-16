# टेक्स्ट जनरेशन एप्लिकेशन बनाना

[![टेक्स्ट जनरेशन एप्लिकेशन बनाना](../../../translated_images/hi/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(इस पाठ का वीडियो देखने के लिए ऊपर दिए गए चित्र पर क्लिक करें)_

आपने इस पाठ्यक्रम में अब तक देखा है कि कोर अवधारणाएं जैसे कि प्रॉम्प्ट और यहां तक कि "प्रॉम्प्ट इंजीनियरिंग" नामक पूरी एक विधा मौजूद है। कई उपकरण जिनसे आप बातचीत कर सकते हैं जैसे ChatGPT, Office 365, Microsoft Power Platform और अन्य, प्रॉम्प्ट्स का उपयोग करके आपको कुछ हासिल करने में सहायता करते हैं।

एक ऐप में ऐसी अनुभूति जोड़ने के लिए, आपको प्रॉम्प्ट्स, कंप्लीशंस जैसी अवधारणाएं समझनी होंगी और काम करने के लिए एक लाइब्रेरी चुननी होगी। यही आप इस अध्याय में सीखेंगे।

## परिचय

इस अध्याय में, आप:

- openai लाइब्रेरी और इसकी मुख्य अवधारणाओं के बारे में जानेंगे।
- openai का उपयोग करके एक टेक्स्ट जनरेशन ऐप बनाएंगे।
- प्रॉम्प्ट, टेम्परेचर, और टोकन जैसी अवधारणाओं का उपयोग करके टेक्स्ट जनरेशन ऐप बनाना समझेंगे।

## सीखने के लक्ष्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- टेक्स्ट जनरेशन ऐप क्या होता है, समझाएं।
- openai का उपयोग करके टेक्स्ट जनरेशन ऐप बनाएं।
- अपने ऐप को अधिक या कम टोकन उपयोग करने के लिए कॉन्फ़िगर करें और साथ ही आउटपुट को विविध बनाने के लिए टेम्परेचर बदलें।

## टेक्स्ट जनरेशन ऐप क्या होता है?

सामान्यतः जब आप कोई ऐप बनाते हैं, उसमें कुछ प्रकार का इंटरफ़ेस होता है जैसे कि:

- कमांड-आधारित। कंसोल ऐप्स वे ऐप हैं जहाँ आप कमांड टाइप करते हैं और वे कार्य करते हैं। उदाहरण के लिए, `git` एक कमांड-आधारित ऐप है।
- उपयोगकर्ता इंटरफ़ेस (UI)। कुछ ऐप्स में ग्राफिकल यूज़र इंटरफ़ेस (GUIs) होते हैं जहां आप बटन क्लिक करते हैं, टेक्स्ट इनपुट करते हैं, विकल्प चुनते हैं आदि।

### कंसोल और UI ऐप्स सीमित होते हैं

इसे एक कमांड-आधारित ऐप से तुलना करें जहाँ आप कमांड टाइप करते हैं:

- **यह सीमित है**। आप कोई भी कमांड टाइप नहीं कर सकते, केवल वे जिनका ऐप समर्थन करता है।
- **भाषा-विशिष्ट**। कुछ ऐप्स कई भाषाओं का समर्थन करते हैं, लेकिन डिफ़ॉल्ट रूप से ऐप एक विशिष्ट भाषा के लिए बनाया जाता है, भले ही आप और भाषाओं का समर्थन जोड़ सकें।

### टेक्स्ट जनरेशन ऐप के लाभ

तो टेक्स्ट जनरेशन ऐप कैसे अलग है?

टेक्स्ट जनरेशन ऐप में आपके पास अधिक लचीलापन होता है, आप कमांड सेट या विशिष्ट इनपुट भाषा तक सीमित नहीं होते। इसके बजाय, आप प्राकृतिक भाषा का उपयोग करके ऐप से बातचीत कर सकते हैं। एक और लाभ यह है कि आप पहले से ही एक डेटा स्रोत से जुड़ते हैं जो व्यापक जानकारी के संग्रह पर प्रशिक्षित होता है, जबकि एक पारंपरिक ऐप डाटाबेस में मौजूद चीजों तक सीमित हो सकता है।

### टेक्स्ट जनरेशन ऐप से मैं क्या बना सकता हूँ?

आप कई चीजें बना सकते हैं। उदाहरण के लिए:

- **एक चैटबॉट**। एक चैटबॉट जो कंपनी और उसके उत्पादों जैसे विषयों पर प्रश्नों का उत्तर देता है, अच्छा विकल्प हो सकता है।
- **मददगार**। LLM टेक्स्ट सारांशित करना, टेक्स्ट से अंतर्दृष्टि प्राप्त करना, रिज़्यूमे जैसी टेक्स्ट उत्पन्न करना आदि में बहुत अच्छे होते हैं।
- **कोड सहायक**। आपके द्वारा उपयोग किए गए भाषा मॉडल के आधार पर, आप ऐसा कोड सहायक बना सकते हैं जो कोड लिखने में मदद करता है। उदाहरण के लिए, आप GitHub Copilot या ChatGPT जैसे उत्पादों का उपयोग कोड लिखने में मदद के लिए कर सकते हैं।

## मैं कैसे शुरू कर सकता हूँ?

आपको एक LLM के साथ इंटीग्रेट करने का तरीका खोजने की जरूरत है जो आमतौर पर निम्न दो तरीकों में से एक होता है:

- एक API का उपयोग करें। यहां आप अपने प्रॉम्प्ट के साथ वेब अनुरोध बना रहे हैं और जनरेटेड टेक्स्ट वापस प्राप्त कर रहे हैं।
- एक लाइब्रेरी का उपयोग करें। लाइब्रेरी API कॉल को संक्षिप्त करती हैं और उपयोग में आसान बनाती हैं।

## लाइब्रेरी/SDKs

LLMs के साथ काम करने के लिए कुछ प्रसिद्ध लाइब्रेरी हैं जैसे:

- **openai**, यह लाइब्रेरी आपके मॉडल से कनेक्ट करना और प्रॉम्प्ट्स भेजना आसान बनाती है।

फिर ऐसी लाइब्रेरी हैं जो उच्च स्तर पर काम करती हैं जैसे:

- **Langchain**। Langchain अच्छी तरह से जाना जाता है और Python का समर्थन करता है।
- **Semantic Kernel**। Semantic Kernel माइक्रोसॉफ्ट की एक लाइब्रेरी है जो C#, Python, और Java भाषाओं का समर्थन करती है।

## openai का उपयोग करके पहला ऐप

आइए देखें कि हम अपना पहला ऐप कैसे बना सकते हैं, हमें कौन सी लाइब्रेरी चाहिए, कितना आवश्यक है इत्यादि।

### openai इंस्टॉल करें

OpenAI या Azure OpenAI के साथ बातचीत करने के लिए कई लाइब्रेरी उपलब्ध हैं। कई प्रोग्रामिंग भाषाएं भी उपयोग की जा सकती हैं जैसे C#, Python, JavaScript, Java और अधिक। हमने `openai` Python लाइब्रेरी का चयन किया है, इसलिए हम इसे स्थापित करने के लिए `pip` का उपयोग करेंगे।

```bash
pip install openai
```

### एक संसाधन बनाएं

आपको निम्न कदम उठाने होंगे:

- Azure पर एक खाता बनाएँ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI तक पहुँच प्राप्त करें। यहां जाएँ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) और पहुँच के लिए अनुरोध करें।

  > [!NOTE]
  > लेखन के समय, आपको Azure OpenAI के लिए पहुँच हेतु आवेदन करना होगा।

- Python इंस्टॉल करें <https://www.python.org/>
- Azure OpenAI सेवा संसाधन बनाएं। इस मार्गदर्शिका को देखें कि [कैसे संसाधन बनाएँ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुंजी और एंडपॉइंट खोजें

अब आपको अपनी `openai` लाइब्रेरी को यह बताना होगा कि कौन सी API कुंजी का उपयोग करना है। अपनी API कुंजी खोजने के लिए, Azure OpenAI संसाधन के "Keys and Endpoint" सेक्शन पर जाएं और "Key 1" मान कॉपी करें।

![Azure पोर्टल में Keys और Endpoint संसाधन ब्लेड](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब जब आपके पास यह जानकारी कॉपी हो गई है, तो चलिए लाइब्रेरी को इसे उपयोग करने के लिए निर्देशित करते हैं।

> [!NOTE]
> अपनी API कुंजी को अपने कोड से अलग रखना बेहतर है। आप ऐसा वातावरण चर (environment variables) का उपयोग करके कर सकते हैं।
>
> - पर्यावरण चर `OPENAI_API_KEY` को अपनी API कुंजी पर सेट करें।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कॉन्फ़िगरेशन सेटअप करें

यदि आप Azure OpenAI (अब Microsoft Foundry का हिस्सा) का उपयोग कर रहे हैं, तो यह कॉन्फ़िगरेशन सेटअप है। हम स्टैण्डर्ड `OpenAI` क्लाइंट का उपयोग करते हैं जो Azure OpenAI `/openai/v1/` एंडपॉइंट की ओर इशारा करता है, जो Responses API के साथ काम करता है और किसी `api_version` की जरूरत नहीं होती:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ऊपर हम निम्न सेट कर रहे हैं:

- `api_key`, यह आपकी API कुंजी है जो Azure पोर्टल या Microsoft Foundry पोर्टल में मिली है।
- `base_url`, यह आपका Foundry संसाधन एंडपॉइंट है जिसमें `/openai/v1/` जोड़ा गया है। स्थिर v1 एंडपॉइंट OpenAI और Azure OpenAI दोनों के साथ बिना `api_version` प्रबंधन के काम करता है।

> [!NOTE] > `os.environ` वातावरण चर पढ़ता है। आप इसे `AZURE_OPENAI_API_KEY` और `AZURE_OPENAI_ENDPOINT` जैसे वातावरण चर पढ़ने के लिए उपयोग कर सकते हैं। इन वातावरण चर को अपनी टर्मिनल में सेट करें या `dotenv` जैसी लाइब्रेरी का उपयोग करें।

## टेक्स्ट जनरेट करें

टेक्स्ट जनरेट करने का तरीका Responses API के `responses.create` मेथड का उपयोग करना है। यहां एक उदाहरण है:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # यह आपका मॉडल तैनाती नाम है
    input=prompt,
    store=False,
)
print(response.output_text)
```

ऊपर दिए गए कोड में, हम एक रिस्पांस बनाते हैं, उस मॉडल को पास करते हैं जिसे हम उपयोग करना चाहते हैं और प्रॉम्प्ट देते हैं। फिर हम `response.output_text` के ज़रिए उत्पन्न टेक्स्ट प्रिंट करते हैं।

### मल्टी-टर्न वार्तालाप

Responses API एकल-टर्न टेक्स्ट जनरेशन और मल्टी-टर्न चैटबॉट दोनों के लिए उपयुक्त है - आप `input` में संदेशों की एक सूची प्रदान करते हैं ताकि बातचीत बन सके:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

इस कार्यक्षमता के बारे में अधिक जानकारी आगामी अध्याय में मिलेगी।

## अभ्यास - आपका पहला टेक्स्ट जनरेशन ऐप

अब जब हमने openai सेटअप और कॉन्फ़िगर करना सीख लिया है, तो चलिए आपका पहला टेक्स्ट जनरेशन ऐप बनाते हैं। ऐप बनाने के लिए ये कदम अपनाएं:

1. एक वर्चुअल वातावरण बनाएं और openai इंस्टॉल करें:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि आप Windows उपयोग कर रहे हैं, तो `source venv/bin/activate` की जगह `venv\Scripts\activate` टाइप करें।

   > [!NOTE]
   > अपनी Azure OpenAI कुंजी खोजने के लिए [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) पर जाएं और `Open AI` खोजें, `Open AI resource` चुनें, फिर `Keys and Endpoint` पर जाकर `Key 1` कॉपी करें।

1. एक _app.py_ फ़ाइल बनाएं और उसे निम्न कोड दें:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # अपना पूर्णता कोड जोड़ें
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API का उपयोग करके एक अनुरोध करें
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिक्रिया प्रिंट करें
   print(response.output_text)
   ```

   > [!NOTE]
   > यदि आप आम OpenAI (Azure नहीं) का उपयोग कर रहे हैं, तो `client = OpenAI(api_key="<अपनी OpenAI कुंजी यहां डालें>")` का उपयोग करें (कोई `base_url` नहीं) और `gpt-4o-mini` जैसे मॉडल नाम पास करें न कि डिप्लॉयमेंट नाम।

   आपको कुछ इस तरह आउटपुट दिखाई देगा:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विभिन्न प्रकार के प्रॉम्प्ट्स, विभिन्न उद्देश्यों के लिए

अब आपने देखा कि प्रॉम्प्ट के ज़रिए कैसे टेक्स्ट जनरेट किया जाता है। आपके पास एक काम करता प्रोग्राम भी है जिसे आप संशोधित करके विभिन्न प्रकार के टेक्स्ट उत्पन्न कर सकते हैं।

प्रॉम्प्ट्स का उपयोग कई प्रकार के कार्यों के लिए किया जा सकता है। उदाहरण के लिए:

- **किसी प्रकार का टेक्स्ट जनरेट करें**। उदाहरण के लिए, आप एक कविता, क्विज़ के प्रश्न आदि उत्पन्न कर सकते हैं।
- **जानकारी खोजें**। आप प्रॉम्प्ट्स का उपयोग जानकारी खोजने के लिए कर सकते हैं जैसे कि यह उदाहरण 'वेब डेवलपमेंट में CORS का क्या मतलब है?'।
- **कोड जनरेट करें**। आप प्रॉम्प्ट का उपयोग करके कोड उत्पन्न कर सकते हैं, उदाहरण के लिए ईमेल सत्यापन के लिए रेगुलर एक्सप्रेशन बनाना या पूरा प्रोग्राम, जैसे वेब ऐप, बनाना?

## एक अधिक व्यावहारिक उपयोग मामला: रेसिपी जनरेटर

कल्पना करें आपके पास घर पर कुछ सामग्रियां हैं और आप कुछ पकाना चाहते हैं। इसके लिए आपको एक रेसिपी की जरूरत होती है। रेसिपी खोजने के लिए आप सर्च इंजन का उपयोग कर सकते हैं या LLM का इस्तेमाल कर सकते हैं।

आप इस तरह एक प्रॉम्प्ट लिख सकते हैं:

> "निम्नलिखित सामग्री के साथ डिश के लिए 5 रेसिपी दिखाएं: चिकन, आलू, और गाजर। प्रत्येक रेसिपी में इस्तमाल होने वाली सारी सामग्री सूचीबद्ध करें"

ऊपर दिए गए प्रॉम्प्ट के आधार पर, आपको इस तरह का उत्तर मिल सकता है:

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

यह परिणाम अच्छा है, अब मुझे पता है क्या पकाना है। इस बिंदु पर, उपयोगी सुधार हो सकते हैं:

- उन सामग्रियों को छाँटना जो मुझे पसंद नहीं हैं या जिनसे मैं एलर्जिक हूँ।
- एक शॉपिंग लिस्ट बनाना, अगर मेरे पास सभी सामग्री घर पर नहीं हैं।

ऊपर के मामलों के लिए, चलिए एक अतिरिक्त प्रॉम्प्ट जोड़ते हैं:

> "कृपया लहसुन वाली रेसिपी हटा दें क्योंकि मुझे उससे एलर्जी है और उसे किसी अन्य सामग्री से बदल दें। साथ ही, कृपया रेसिपी के लिए एक शॉपिंग लिस्ट भी बनाएं, ध्यान में रखते हुए कि मेरे पास पहले से चिकन, आलू और गाजर हैं।"

अब आपको एक नया परिणाम मिलेगा, जैसे कि:

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

ये आपकी पांच रेसिपी हैं, जिनमें लहसुन नहीं है और आपके पास घर पर जो सामग्री है उसे ध्यान में रखते हुए शॉपिंग लिस्ट भी है।

## अभ्यास - रेसिपी जनरेटर बनाएँ

अब जब हमने एक परिदृश्य खेला है, चलिए उस परिदृश्य के अनुरूप कोड लिखते हैं। ऐसा करने के लिए, ये कदम अपनाएं:

1. मौजूदा _app.py_ फ़ाइल को प्रारंभिक बिंदु के रूप में उपयोग करें
1. `prompt` वैरिएबल को ढूंढें और इसका कोड निम्नलिखित में बदलें:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   यदि आप अब कोड चलाते हैं, तो आपको ऐसा आउटपुट दिख सकता है:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ध्यान दें, आपका LLM नॉनडिटर्मिनिस्टिक है, इसलिए हर बार प्रोग्राम चलाने पर आपको अलग-अलग परिणाम मिल सकते हैं।

   बढ़िया, चलिए देखते हैं कि हम चीज़ों को कैसे सुधार सकते हैं। सुधार के लिए हम चाहते हैं कि कोड लचीला हो ताकि सामग्रियां और रेसिपी की संख्या परिवर्तित और बढ़ायी जा सके।

1. चलिए कोड को इस प्रकार बदलते हैं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # रेसिपी की संख्या को प्रॉम्प्ट और सामग्री में समायोजित करें
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   टेस्ट रन के लिए कोड इस तरह का दिख सकता है:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फ़िल्टर और शॉपिंग लिस्ट जोड़कर सुधार करें

अब हमारे पास एक कार्यशील ऐप है जो रेसिपी उत्पन्न कर सकता है और यह लचीला है क्योंकि यह उपयोगकर्ता से इनपुट पर निर्भर करता है, रेसिपी की संख्या और इस्तेमाल की जाने वाली सामग्री दोनों पर।

हम इसे और सुधारने के लिए निम्न जोड़ना चाहते हैं:

- **सामग्री को छाँटना**। हम उन सामग्रियों को छाँटने में सक्षम होना चाहते हैं जो हमें पसंद नहीं हैं या जिनसे हम एलर्जिक हैं। इसे पूरा करने के लिए, हम अपने मौजूदा प्रॉम्प्ट को एडिट करके इसके अंत में एक फ़िल्टर कंडीशन जोड़ सकते हैं, इस प्रकार:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ऊपर, हमने प्रॉम्प्ट के अंत में `{filter}` जोड़ा है और हम उपयोगकर्ता से फ़िल्टर मान भी ले रहे हैं।

  प्रोग्राम चलाने के उदाहरण इनपुट अब इस प्रकार हो सकता है:

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

  जैसा आप देख सकते हैं, जिन रेसिपीज़ में दूध था वे छांट दी गईं हैं। लेकिन, यदि आप लैक्टोज़ असहिष्णु हैं, तो आप पनीर वाली रेसिपीज़ को भी छाँटना चाहेंगे, इसलिए स्पष्टता आवश्यक है।


- **एक खरीदारी सूची बनाएं**। हम एक खरीदारी सूची बनाना चाहते हैं, यह ध्यान में रखते हुए कि हमारे पास पहले से घर पर क्या है।

  इस कार्यक्षमता के लिए, हम या तो सब कुछ एक प्रॉम्प्ट में हल करने की कोशिश कर सकते हैं या इसे दो प्रॉम्प्ट में विभाजित कर सकते हैं। आइए बाद वाला तरीका आजमाएं। यहां हम एक अतिरिक्त प्रॉम्प्ट जोड़ने का सुझाव दे रहे हैं, लेकिन इसे काम करने के लिए, हमें पहले प्रॉम्प्ट के परिणाम को बाद वाले प्रॉम्प्ट के संदर्भ के रूप में जोड़ना होगा।

  उस कोड के हिस्से को खोजें जो पहले प्रॉम्प्ट से परिणाम प्रिंट करता है और नीचे दिया गया कोड जोड़ें:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया प्रिंट करें
  print("Shopping list:")
  print(response.output_text)
  ```

  निम्न बातों का ध्यान रखें:

  1. हम नया प्रॉम्प्ट बना रहे हैं जिसमें पहले प्रॉम्प्ट का परिणाम नया प्रॉम्प्ट के साथ जोड़ा गया है:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हम एक नया अनुरोध कर रहे हैं, लेकिन पहले प्रॉम्प्ट में मांगे गए टोकन्स की संख्या को ध्यान में रखते हुए, इसलिए इस बार हम कहते हैं कि `max_output_tokens` 1200 है।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     इस कोड को चलाने पर, हमें अब निम्न आउटपुट मिलता है:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## अपनी सेटअप में सुधार करें

अब तक हमारे पास काम करने वाला कोड है, लेकिन कुछ सुधार हैं जिन्हें हमें आगे बेहतर करने के लिए करना चाहिए। कुछ चीज़ें जो हमें करनी चाहिए वे हैं:

- **कोड से सीक्रेट्स अलग करें**, जैसे एपीआई कुंजी। सीक्रेट्स कोड में नहीं होने चाहिए और उन्हें सुरक्षित स्थान पर संग्रहित करना चाहिए। कोड से सीक्रेट्स अलग करने के लिए, हम पर्यावरण चर और `python-dotenv` जैसी लाइब्रेरी का उपयोग करके उन्हें फाइल से लोड कर सकते हैं। कोड में यह कुछ इस तरह दिखेगा:

  1. एक `.env` फाइल बनाएँ जिसमें निम्न सामग्री हो:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ध्यान दें, माइक्रोसॉफ्ट फाउंड्री में Azure OpenAI के लिए, आपको इसके बजाय निम्न पर्यावरण चर सेट करने होंगे:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोड में, आप पर्यावरण चरों को इस प्रकार लोड करेंगे:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लंबाई पर एक शब्द**। हमें यह सोचना चाहिए कि हमें वांछित टेक्स्ट जनरेशन के लिए कितने टोकन चाहिए। टोकन्स खर्चीले होते हैं, इसलिए जहां संभव हो, हमें उपयोग किए गए टोकन की संख्या कम रहने की कोशिश करनी चाहिए। उदाहरण के लिए, क्या हम प्रॉम्प्ट इस प्रकार बना सकते हैं कि कम टोकन का उपयोग हो?

  टोकन्स बदलने के लिए, आप `max_output_tokens` पैरामीटर का उपयोग कर सकते हैं। उदाहरण के लिए, यदि आप 100 टोकन उपयोग करना चाहते हैं, तो आप यह करेंगे:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **टेम्परेचर के साथ प्रयोग**। टेम्परेचर एक ऐसा पैरामीटर है जिसका हमने अब तक उल्लेख नहीं किया है लेकिन यह हमारे प्रोग्राम के प्रदर्शन के लिए महत्वपूर्ण संदर्भ है। उच्च तापमान मान से आउटपुट अधिक यादृच्छिक होगा। इसके विपरीत, कम तापमान मान से आउटपुट अधिक पूर्वानुमेय होगा। विचार करें कि क्या आप अपने आउटपुट में विविधता चाहते हैं या नहीं।

  टेम्परेचर बदलने के लिए, आप `temperature` पैरामीटर का उपयोग कर सकते हैं। उदाहरण के लिए, यदि आप 0.5 तापमान उपयोग करना चाहते हैं, तो आप करेंगे:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ध्यान दें, 1.0 के करीब होने पर आउटपुट अधिक विविध होगा।

## असाइनमेंट

इस असाइनमेंट के लिए, आप चुन सकते हैं कि क्या बनाना है।

यहाँ कुछ सुझाव हैं:

- रेसिपी जेनरेटर ऐप को और बेहतर बनाने के लिए ट्वीक करें। टेम्परेचर मान और प्रॉम्प्ट के साथ खेलें ताकि देखें आप क्या बना सकते हैं।
- एक "स्टडी बडी" बनाएं। यह ऐप किसी विषय जैसे पायथन के बारे में प्रश्नों का उत्तर दे सके। आपके पास प्रॉम्प्ट्स हो सकते हैं जैसे "पायथन में किसी विषय का क्या अर्थ है?", या प्रॉम्प्ट हो सकता है, मुझे किसी विषय के लिए कोड दिखाओ आदि।
- इतिहास बोट, इतिहास को जीवंत बनाएं, बोट को किसी ऐतिहासिक पात्र का रूप निभाने का निर्देश दें और उसके जीवन और काल के बारे में प्रश्न पूछें।

## समाधान

### स्टडी बडी

नीचे एक शुरुआती प्रॉम्प्ट है, देखें कि आप इसे कैसे उपयोग कर सकते हैं और अपनी पसंद के अनुसार सुधार कर सकते हैं।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

यहां कुछ प्रॉम्प्ट हैं जिन्हें आप उपयोग कर सकते हैं:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जाँच

टेम्परेचर अवधारणा क्या करती है?

1. यह नियंत्रित करता है कि आउटपुट कितना यादृच्छिक है।
1. यह नियंत्रित करता है कि प्रतिक्रिया कितनी बड़ी है।
1. यह नियंत्रित करता है कि कितने टोकन्स उपयोग किए गए हैं।

## 🚀 चुनौती

असाइनमेंट पर काम करते समय, टेम्परेचर में बदलाव करने की कोशिश करें, इसे 0, 0.5, और 1 पर सेट करके देखें। याद रखें कि 0 सबसे कम विविध है और 1 सबसे अधिक। आपके ऐप के लिए कौन सा मान सबसे अच्छा काम करता है?

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप Generative AI ज्ञान में और उन्नति कर सकें!

पाठ 7 पर जाएं जहाँ हम देखेंगे कि कैसे [चैट एप्लिकेशन बनाएं](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->