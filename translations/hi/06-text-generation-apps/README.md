# टेक्स्ट जनरेशन एप्लिकेशन बनाना

[![टेक्स्ट जनरेशन एप्लिकेशन बनाना](../../../translated_images/hi/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

आपने अब तक इस पाठ्यक्रम में देखा कि कोर कांसेप्ट्स जैसे प्रॉम्प्ट्स होते हैं और यहां तक कि एक पूरा कोर्स है जिसे "प्रॉम्प्ट इंजीनियरिंग" कहा जाता है। कई टूल्स जिनसे आप इंटरैक्ट कर सकते हैं जैसे ChatGPT, Office 365, Microsoft Power Platform और भी बहुत कुछ, प्रॉम्प्ट्स का उपयोग करके कुछ पूरा करने में आपकी मदद करते हैं।

एक ऐप में ऐसा अनुभव जोड़ने के लिए, आपको प्रॉम्प्ट्स, कम्प्लीशंस जैसे कांसेप्ट्स को समझना होगा और एक लाइब्रेरी चुननी होगी। यही बात आप इस अध्याय में सीखेंगे।

## परिचय

इस अध्याय में, आप:

- openai लाइब्रेरी और इसके कोर कांसेप्ट्स के बारे में जानेंगे।
- openai का उपयोग करके एक टेक्स्ट जनरेशन ऐप बनाएंगे।
- प्रॉम्प्ट, टेम्परेचर, और टोकन जैसे कांसेप्ट्स का उपयोग करके टेक्स्ट जनरेशन ऐप बनाने का तरीका समझेंगे।

## सीखने के लक्ष्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- टेक्स्ट जनरेशन ऐप क्या होता है, समझाना।
- openai का उपयोग करके टेक्स्ट जनरेशन ऐप बनाना।
- अपने ऐप को.configure करना ताकि वह अधिक या कम टोकन का उपयोग करे और टेम्परेचर बदले, जिससे आउटपुट में विविधता आए।

## टेक्स्ट जनरेशन ऐप क्या है?

आम तौर पर जब आप कोई ऐप बनाते हैं तो उसमें कुछ प्रकार का इंटरफेस होता है जैसे कि:

- कमांड-आधारित। कंसोल ऐप्स ऐसे ऐप होते हैं जहां आप कमांड टाइप करते हैं और वह कार्य करता है। उदाहरण के लिए, `git` एक कमांड-आधारित ऐप है।
- उपयोगकर्ता इंटरफेस (UI)। कुछ ऐप्स के ग्राफिकल यूजर इंटरफेस (GUIs) होते हैं जहां आप बटन क्लिक करते हैं, टेक्स्ट इनपुट करते हैं, विकल्प चुनते हैं आदि।

### कंसोल और UI ऐप सीमित होते हैं

इसे एक कमांड-आधारित ऐप के मुकाबले देखें जहां आप एक कमांड टाइप करते हैं:

- **यह सीमित है**। आप कोई भी कमांड नहीं टाइप कर सकते, केवल वे कमांड जो ऐप सपोर्ट करता है।
- **भाषा-विशिष्ट**। कुछ ऐप कई भाषाओं का समर्थन करते हैं, लेकिन डिफ़ॉल्ट रूप से ऐप किसी विशेष भाषा के लिए बनाया गया होता है, भले ही आप अन्य भाषाओं का समर्थन जोड़ सकें।

### टेक्स्ट जनरेशन ऐप्स के लाभ

तो टेक्स्ट जनरेशन ऐप कैसे अलग होता है?

टेक्स्ट जनरेशन ऐप में आपके पास अधिक लचीलापन होता है, आप कमांड सेट या विशिष्ट इनपुट भाषा तक सीमित नहीं होते। इसके बजाय, आप प्राकृतिक भाषा का उपयोग करके ऐप से इंटरैक्ट कर सकते हैं। एक और लाभ यह है कि आप पहले से ही एक ऐसे डेटा स्रोत से इंटरैक्ट कर रहे हैं जिसे विशाल सामग्री पर प्रशिक्षित किया गया है, जबकि एक पारंपरिक ऐप डेटाबेस में सीमित हो सकता है।

### मैं टेक्स्ट जनरेशन ऐप से क्या बना सकता हूँ?

आप कई चीजें बना सकते हैं। उदाहरण के लिए:

- **एक चैटबोट**। एक चैटबोट आपके कंपनी और उसके उत्पादों जैसे विषयों पर सवालों का जवाब देने के लिए अच्छा हो सकता है।
- **सहायक**। LLMs टेक्स्ट का सारांश बनाने, टेक्स्ट से जानकारी निकालने, रिज्यूमे जैसे टेक्स्ट बनाने जैसी चीजों में उत्कृष्ट होते हैं।
- **कोड सहायक**। जिस भाषा मॉडल का आप उपयोग करते हैं, उसके आधार पर आप एक कोड सहायक बना सकते हैं जो कोड लिखने में मदद करता है। उदाहरण के लिए, आप GitHub Copilot या ChatGPT जैसे उत्पादों का उपयोग कर सकते हैं।

## मैं कैसे शुरू कर सकता हूँ?

आपको LLM के साथ एकीकृत करने का तरीका ढूंढना होगा जो आमतौर पर निम्न दो तरीकों में से होता है:

- API का उपयोग करें। यहां आप अपने प्रॉम्प्ट के साथ वेब रिक्वेस्ट बनाते हैं और वापस जनरेट किया गया टेक्स्ट प्राप्त करते हैं।
- लाइब्रेरी का उपयोग करें। लाइब्रेरी API कॉल्स को संक्षिप्त करती हैं और उपयोग में आसान बनाती हैं।

## लाइब्रेरी/SDKs

LLMs के साथ काम करने के लिए कुछ प्रसिद्ध लाइब्रेरीज़ हैं जैसे:

- **openai**, यह लाइब्रेरी आपके मॉडल से जुड़ने और प्रॉम्प्ट भेजने को आसान बनाती है।

फिर कुछ लाइब्रेरीज़ हैं जो उच्च स्तरीय पर काम करती हैं जैसे:

- **Langchain**। Langchain प्रसिद्ध है और Python का समर्थन करता है।
- **Semantic Kernel**। Semantic Kernel माइक्रोसॉफ्ट की लाइब्रेरी है जो C#, Python, और Java भाषाओं का समर्थन करती है।

## openai के साथ पहला ऐप

आइए देखें कि हम अपना पहला ऐप कैसे बना सकते हैं, हमें किन लाइब्रेरीज़ की जरूरत है, कितना चाहिए आदि।

### openai इंस्टॉल करें

OpenAI या Azure OpenAI के साथ इंटरैक्ट करने के लिए कई लाइब्रेरीज़ उपलब्ध हैं। कई प्रोग्रामिंग भाषाओं का उपयोग संभव है जैसे C#, Python, JavaScript, Java और अन्य। हमने `openai` Python लाइब्रेरी चुन ली है, इसलिए इसे इंस्टॉल करने के लिए हम `pip` का उपयोग करेंगे।

```bash
pip install openai
```

### एक संसाधन बनाएँ

आपको निम्न कदम उठाने होंगे:

- Azure पर एक खाता बनाएँ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI तक पहुंच प्राप्त करें। इसके लिए [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) पर जाएं और पहुंच का अनुरोध करें।

  > [!NOTE]
  > लेखन के समय, Azure OpenAI की पहुंच प्राप्त करने के लिए आवेदन करना जरूरी है।

- Python इंस्टॉल करें <https://www.python.org/>
- Azure OpenAI सर्विस संसाधन बनाएं। इसके लिए इस गाइड को देखें कि [कैसे संसाधन बनाएं](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुंजी और एन्डपॉइंट का पता लगाएं

अब आपको अपनी `openai` लाइब्रेरी को बताना है कि वह कौन सी API कुंजी का उपयोग करे। अपनी API कुंजी पाने के लिए Azure OpenAI रिसोर्स के "Keys and Endpoint" सेक्शन में जाएं और "Key 1" कॉपी करें।

![Azure पोर्टल में Keys and Endpoint रिसोर्स ब्लेड](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब जब आपके पास यह जानकारी है, आइए लाइब्रेरी को इसे उपयोग करने के लिए निर्देशित करें।

> [!NOTE]
> अपने कोड से API कुंजी अलग रखना बेहतर है। आप ऐसा एनवायरनमेंट वेरिएबल्स का उपयोग करके कर सकते हैं।
>
> - एनवायरनमेंट वेरिएबल `OPENAI_API_KEY` को अपनी API कुंजी पर सेट करें।
>   `export OPENAI_API_KEY='sk-...'`

### Azure कॉन्फ़िगरेशन सेटअप करें

यदि आप Azure OpenAI का उपयोग कर रहे हैं (जो अब Microsoft Foundry का हिस्सा है), तो कॉन्फ़िगरेशन इस प्रकार सेट करें। हम सामान्य `OpenAI` क्लाइंट का उपयोग करते हैं जो Azure OpenAI `/openai/v1/` एन्डपॉइंट पर पॉइंट करता है, जो Responses API के साथ काम करता है और कोई `api_version` आवश्यक नहीं है:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ऊपर हम निम्न सेट कर रहे हैं:

- `api_key`, यह आपकी Azure पोर्टल या Microsoft Foundry पोर्टल से मिली API कुंजी है।
- `base_url`, यह आपका Foundry संसाधन एन्डपॉइंट है जिसमे `/openai/v1/` जोड़ा गया है। वांछित v1 एन्डपॉइंट OpenAI और Azure OpenAI दोनों के साथ बिना `api_version` प्रबंधन के काम करता है।

> [!NOTE] > `os.environ` एनवायरनमेंट वेरिएबल्स पढ़ता है। आप इसे `AZURE_OPENAI_API_KEY` और `AZURE_OPENAI_ENDPOINT` जैसे वेरिएबल्स पढ़ने के लिए उपयोग कर सकते हैं। इन्हें अपने टर्मिनल में या किसी लाइब्रेरी जैसे `dotenv` के सहारे सेट करें।

## टेक्स्ट जनरेट करें

टेक्स्ट जनरेट करने का तरीका Responses API के माध्यम से `responses.create` मेथड का उपयोग करना है। एक उदाहरण देखें:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # यह आपका मॉडल डिप्लॉयमेंट नाम है
    input=prompt,
    store=False,
)
print(response.output_text)
```

ऊपर के कोड में, हम एक प्रतिक्रिया बनाते हैं और उपयोग करने के लिए मॉडल और प्रॉम्प्ट भेजते हैं। फिर हम `response.output_text` द्वारा जनरेट किया गया टेक्स्ट प्रिंट करते हैं।

### मल्टी-टर्न संवाद

Responses API एकल टर्न टेक्स्ट जनरेशन और मल्टी-टर्न चैटबोट दोनों के लिए उपयुक्त है - आप `input` में संदेशों की सूचि प्रदान करते हैं ताकि बातचीत तैयार हो सके:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

इस फंक्शनैलिटी पर अगली कड़ी में अधिक जानकारी मिलेगी।

## अभ्यास - आपका पहला टेक्स्ट जनरेशन ऐप

अब जब हमने openai सेटअप और कॉन्फ़िगर करना सीख लिया है, तो चलिए आपका पहला टेक्स्ट जनरेशन ऐप बनाते हैं। ऐप बनाने के लिए ये कदम उठाएं:

1. एक वर्चुअल एनवायरनमेंट बनाएँ और openai इंस्टॉल करें:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > अगर आप Windows का उपयोग कर रहे हैं तो `source venv/bin/activate` की जगह `venv\Scripts\activate` टाइप करें।

   > [!NOTE]
   > अपनी Azure OpenAI कुंजी खोजने के लिए [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) पर जाएं, `Open AI` खोजें, `Open AI resource` चुनें, फिर `Keys and Endpoint` पर जाएं और `Key 1` कॉपी करें।

1. एक _app.py_ फ़ाइल बनाएँ और निम्नलिखित कोड दें:

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

   # Responses API का उपयोग करके एक अनुरोध बनाएं
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिक्रिया प्रिंट करें
   print(response.output_text)
   ```

   > [!NOTE]
   > यदि आप सिंपल OpenAI (Azure नहीं) का उपयोग कर रहे हैं, तो `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (कोई `base_url` नहीं) उपयोग करें और डिप्लॉयमेंट नाम की बजाय मॉडल नाम जैसे `gpt-5-mini` पास करें।

   आपको निम्नलिखित आउटपुट देखना चाहिए:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विभिन्न प्रकार के प्रॉम्प्ट्स, विभिन्न कार्यों के लिए

अब आपने देखा कि प्रॉम्प्ट का उपयोग करके टेक्स्ट कैसे जनरेट करते हैं। आपके पास एक प्रोग्राम चल रहा है जिसे आप बदल कर अलग-अलग प्रकार का टेक्स्ट बना सकते हैं।

प्रॉम्प्ट्स का उपयोग कई तरह के कार्यों के लिए किया जा सकता है। उदाहरण के लिए:

- **एक प्रकार का टेक्स्ट जनरेट करें**। उदाहरण के लिए, आप कविता, क्विज़ के प्रश्न आदि जनरेट कर सकते हैं।
- **जानकारी खोजें**। आप प्रॉम्प्ट्स का उपयोग जानकारी खोजने के लिए कर सकते हैं, जैसे 'वेब विकास में CORS का क्या अर्थ है?'।
- **कोड जनरेट करें**। आप प्रॉम्प्ट्स का उपयोग कोड बनाने के लिए कर सकते हैं, उदाहरण के लिए ईमेल सत्यापन के लिए रेगुलर एक्सप्रेशन विकसित करना या पूरी प्रोग्रामिंग जैसे वेब ऐप बनाना?

## एक अधिक व्यावहारिक उपयोग केस: रेसिपी जनरेटर

कल्पना करें कि आपके पास घर पर सामग्री है और आप कुछ पकाना चाहते हैं। इसके लिए आपको रेसिपी चाहिए। रेसिपी खोजने का एक तरीका सर्च इंजन है या आप LLM का उपयोग कर सकते हैं।

आप इस प्रकार प्रॉम्प्ट लिख सकते हैं:

> "मुझे निम्न सामग्री वाली डिश के लिए 5 रेसिपी दिखाएं: चिकन, आलू, और गाजर। प्रत्येक रेसिपी में उपयोग की गई सभी सामग्री की सूची बनाएं"

ऊपर दिए प्रॉम्प्ट के अनुसार, आपको इस तरह की प्रतिक्रिया मिल सकती है:

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

यह परिणाम शानदार है, मुझे पता चल गया क्या बनाना है। इस समय, उपयोगी सुधार हो सकते हैं:

- उन सामग्री को फ़िल्टर करना जो मुझे पसंद नहीं या जिनसे मैं एलर्जिक हूँ।
- अगर मेरे पास सभी सामग्री नहीं हैं तो खरीदारी की सूची बनाना।

ऊपर के मामलों के लिए, एक अतिरिक्त प्रॉम्प्ट जोड़ें:

> "कृपया लहसुन वाली रेसिपी हटा दें क्योंकि मैं उससे एलर्जिक हूँ और उसे किसी अन्य चीज़ से बदलें। इसके अलावा, कृपया रेसिपीज़ के लिए एक खरीदारी सूची बनाएं, ध्यान में रखते हुए कि मेरे पास चिकन, आलू और गाजर पहले से ही हैं।"

अब आपको एक नया परिणाम मिलेगा, अर्थात्:

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

यहीं आपकी पांच रेसिपी हैं, जिनमें लहसुन नहीं है और आपके घर में जो सामान है, उसे ध्यान में रखकर एक खरीदारी सूचि भी है।

## अभ्यास - रेसिपी जनरेटर बनाएँ

अब जब हमने एक परिदृश्य खेला, आइए उस परिदृश्य के अनुसार कोड लिखें। ऐसा करने के लिए, ये कदम उठाएं:

1. वर्तमान _app.py_ फ़ाइल का उपयोग प्रारंभिक बिंदु के रूप में करें
1. `prompt` वेरिएबल ढूंढें और इसका कोड निम्नलिखित बदलें:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   यदि आप अब कोड चलाएंगे, तो आपको कुछ ऐसा आउटपुट मिलना चाहिए:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ध्यान दें, आपका LLM गैर-नियतात्मक है, इसलिए आपको हर बार प्रोग्राम चलाने पर अलग परिणाम मिल सकते हैं।

   बढ़िया, आइए देखें कि हम चीज़ें कैसे सुधार सकते हैं। सुधार के लिए हम चाहते हैं कि कोड लचीला हो, जिससे सामग्री और रेसिपीज़ की संख्या बदली जा सके।

1. कोड को इस तरह बदलें:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # रेसिपीज़ की संख्या को प्रॉम्प्ट और सामग्री में इंटरपोल करें
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   टेस्ट रन के लिए कोड इस तरह दिख सकता है:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फ़िल्टर और खरीदारी सूची जोड़कर सुधार करें

अब हमारे पास एक काम करने वाला ऐप है जो रेसिपीज़ बना सकता है और यह लचीला है क्योंकि यह उपयोगकर्ता के इनपुट पर निर्भर करता है, न केवल रेसिपीज़ की संख्या पर बल्कि सामग्री पर भी।

इसे और बेहतर बनाने के लिए हम निम्न जोड़ना चाहते हैं:

- **सामग्री फ़िल्टर करें**। हम उन सामग्री को फ़िल्टर करना चाहते हैं जो हमें पसंद नहीं हैं या जिनके लिए हम एलर्जिक हैं। इसके लिए हम अपने मौजूदा प्रॉम्प्ट को संपादित कर इसके अंत में फ़िल्टर कंडीशन जोड़ सकते हैं इस प्रकार:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ऊपर, हमने प्रॉम्प्ट के अंत में `{filter}` जोड़ा है और उपयोगकर्ता से फ़िल्टर मान भी प्राप्त कर रहे हैं।

  प्रोग्राम चलाने का एक उदाहरण इनपुट अब इस प्रकार हो सकता है:

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

  जैसा कि आप देख सकते हैं, किसी भी रेसिपी में दूध वाली सामग्री को फ़िल्टर कर दिया गया है। लेकिन अगर आपको लैक्टोज़ असहिष्णुता है, तो आप पनीर वाली रेसिपी भी फ़िल्टर करना चाहेंगे, इसलिए स्पष्ट होना जरूरी है।


- **खरीदारी की सूची बनाएं**। हम एक खरीदारी की सूची बनाना चाहते हैं, यह ध्यान में रखते हुए कि हमारे पास घर पर पहले से क्या है।

  इस कार्यक्षमता के लिए, हम सब कुछ एक ही प्रॉम्प्ट में हल करने की कोशिश कर सकते हैं या इसे दो प्रॉम्प्ट्स में बाँट सकते हैं। आइए बाद वाले तरीके को आजमाएं। यहाँ हम एक अतिरिक्त प्रॉम्प्ट जोड़ने का सुझाव दे रहे हैं, लेकिन इसके काम करने के लिए, हमें पहले प्रॉम्प्ट के परिणाम को संदर्भ के रूप में बाद वाले प्रॉम्प्ट में जोड़ना होगा।

  कोड में उस हिस्से को ढूंढें जो पहले प्रॉम्प्ट के परिणाम को प्रिंट करता है और नीचे दिया गया कोड जोड़ें:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया प्रिंट करें
  print("Shopping list:")
  print(response.output_text)
  ```

  निम्नलिखित बातों का ध्यान रखें:

  1. हम एक नया प्रॉम्प्ट बना रहे हैं जिसमें पहले प्रॉम्प्ट के परिणाम को नए प्रॉम्प्ट में जोड़ रहे हैं:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हम एक नया अनुरोध करते हैं, लेकिन पहले प्रॉम्प्ट में पूछे गए टोकन की संख्या को भी ध्यान में रखते हुए, इसलिए इस बार हम कहते हैं `max_output_tokens` 1200 है।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     इस कोड को चलाने पर, हमें निम्नलिखित आउटपुट मिलता है:

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

अब तक हमारे पास कोड है जो काम करता है, लेकिन कुछ समायोजन हैं जिन्हें हमें चीजों को और बेहतर बनाने के लिए करना चाहिए। कुछ चीजें जो हमें करनी चाहिए वे हैं:

- **कोड से सीक्रेट्स अलग करें**, जैसे API कुंजी। सीक्रेट्स कोड में नहीं होने चाहिए और इन्हें एक सुरक्षित स्थान पर संग्रहीत किया जाना चाहिए। कोड से सीक्रेट्स को अलग करने के लिए, हम पर्यावरण चर (environment variables) और `python-dotenv` जैसी लाइब्रेरी का उपयोग कर सकते हैं जो इन्हें एक फ़ाइल से लोड करती है। कोड में यह कुछ इस तरह दिखेगा:

  1. निम्नलिखित सामग्री वाला `.env` फ़ाइल बनाएं:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ध्यान दें, Microsoft Foundry में Azure OpenAI के लिए, आपको इसके बजाय निम्नलिखित पर्यावरण चर सेट करने होंगे:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोड में, आप पर्यावरण चर इस प्रकार लोड करेंगे:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन की लंबाई पर एक शब्द**। हमें विचार करना चाहिए कि हमें जिस टेक्स्ट को जनरेट करना है उसके लिए कितने टोकन की जरूरत है। टोकन की लागत होती है, इसलिए जहाँ संभव हो, हमें जितने टोकन उपयोग किये जाएं उनमें सावधानी बरतनी चाहिए। उदाहरण के लिए, क्या हम प्रॉम्प्ट इस प्रकार बना सकते हैं कि टोकन कम लगें?

  टोकन की संख्या बदलने के लिए, आप `max_output_tokens` पैरामीटर का उपयोग कर सकते हैं। उदाहरण के लिए, यदि आप 100 टोकन उपयोग करना चाहते हैं, तो आप ऐसा करेंगे:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **टेम्परेचर के साथ प्रयोग**। टेम्परेचर एक ऐसी चीज़ है जिसका हमने अब तक उल्लेख नहीं किया है, लेकिन यह हमारे प्रोग्राम के प्रदर्शन के लिए महत्वपूर्ण संदर्भ है। टेम्परेचर का मान जितना अधिक होगा आउटपुट उतना ही अधिक यादृच्छिक होगा। इसके विपरीत, टेम्परेचर का मान जितना कम होगा आउटपुट उतना ही अधिक पूर्वानुमानित होगा। विचार करें कि आप अपने आउटपुट में विविधता चाहते हैं या नहीं।

  टेम्परेचर बदलने के लिए, आप `temperature` पैरामीटर का उपयोग कर सकते हैं। उदाहरण के लिए, यदि आप 0.5 टेम्परेचर उपयोग करना चाहते हैं, तो आप ऐसा करेंगे:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ध्यान दें, 1.0 के करीब होने पर आउटपुट अधिक विविध होगा।

- **तर्क मॉडल `temperature` का उपयोग नहीं करते**। यह 2026 का एक महत्वपूर्ण बदलाव है। Microsoft Foundry पर वर्तमान में गैर-अप्रियुक्त मॉडल **तर्क मॉडल** हैं (GPT-5 परिवार, o-सीरीज़) - और ये **`temperature` या `top_p` का समर्थन नहीं करते** (और न ही `max_tokens`; इसके बजाय `max_output_tokens` का उपयोग करें)। यदि आप `temperature` को `gpt-5-mini` को भेजेंगे तो आपको "parameter not supported" त्रुटि मिलेगी। इसलिए उपर्युक्त टेम्परेचर उदाहरण आज़माने के लिए, किसी ऐसे मॉडल का चयन करें जो अभी भी सैंपलिंग नियंत्रणों का समर्थन करता है - उदाहरण के लिए खुला **Llama** मॉडल जैसे `Llama-3.3-70B-Instruct` [Microsoft Foundry मॉडल कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) से, जिसे Foundry Models / Azure AI Inference एंडपॉइंट के माध्यम से कॉल किया जाता है (उसी तरीके से जैसे `githubmodels-*` नमूने)। GPT-5 जैसे तर्क मॉडल के लिए, आप आउटपुट को अलग तरीके से नियंत्रित करते हैं:
  - **प्रॉम्प्ट इंजीनियरिंग** - स्पष्ट निर्देश, उदाहरण, और संरचित आउटपुट (देखें पाठ [04 - प्रॉम्प्ट इंजीनियरिंग](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) वे काम करते हैं जो सैंपलिंग नियंत्रण पहले करते थे।
  - **तर्क नियंत्रण** - पैरामीटर जैसे तर्क प्रयास/विवरण तर्क की गहराई को विलंबता और लागत के खिलाफ संतुलित करते हैं।

  संक्षेप में: `temperature`/`top_p` अभी भी कई मॉडलों (Llama, Mistral, Phi, और GPT-4.x परिवार - हालांकि GPT-4.x समाप्त हो रहा है) पर मान्य हैं, लेकिन दिशा प्रॉम्प्ट इंजीनियरिंग + तर्क नियंत्रण की ओर है जैसे GPT-5 जैसे तर्क मॉडल पर।

## असाइनमेंट

इस असाइनमेंट के लिए, आप चुन सकते हैं कि क्या बनाना है।

यहाँ कुछ सुझाव हैं:

- रेसिपी जेनरेटर ऐप को और बेहतर बनाने के लिए समायोजन करें। टेम्परेचर मानों और प्रॉम्प्ट्स के साथ खेलें ताकि देखें आप क्या नया कर सकते हैं।
- एक "स्टडी बडी" बनाएं। यह ऐप किसी विषय, उदाहरण के लिए Python, पर प्रश्नों का उत्तर देने में सक्षम होना चाहिए, आप प्रॉम्प्ट्स दे सकते हैं जैसे "Python में एक निश्चित विषय क्या है?" या "किसी निश्चित विषय के कोड को दिखाओ" आदि।
- इतिहास बॉट, इतिहास को जीवंत बनाएं, बॉट को किसी ऐतिहासिक व्यक्ति का रूप देने के लिए निर्देश दें और उसके जीवन और समय के बारे में प्रश्न पूछें।

## समाधान

### स्टडी बडी

नीचे एक प्रारंभिक प्रॉम्प्ट है, देखें कि आप इसे कैसे उपयोग कर सकते हैं और अपनी पसंद के अनुसार इसमें बदलाव कर सकते हैं।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बॉट

यहां कुछ प्रॉम्प्ट्स हैं जो आप उपयोग कर सकते हैं:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान जांच

टेम्परेचर विचार क्या करता है?

1. यह नियंत्रित करता है कि आउटपुट कितना यादृच्छिक है।
1. यह नियंत्रित करता है कि प्रतिक्रिया कितनी बड़ी है।
1. यह नियंत्रित करता है कि कितने टोकन उपयोग किए जाते हैं।

## 🚀 चुनौती

असाइनमेंट पर काम करते समय, टेम्परेचर को बदलने की कोशिश करें, इसे 0, 0.5, और 1 पर सेट करें। याद रखें कि 0 सबसे कम विविध है और 1 सबसे अधिक। आपके ऐप के लिए कौन सा मान सबसे अच्छा काम करता है?

## बढ़िया काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारी [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) देखें ताकि आप अपनी जनरेटिव AI ज्ञान को और बढ़ा सकें!

अब पाठ 7 पर जाएं जहाँ हम देखेंगे कि [कैसे चैट एप्लिकेशन बनाएँ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->