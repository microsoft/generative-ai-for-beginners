<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:10:32+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hi"
}
-->
# टेक्स्ट जनरेशन एप्लिकेशन बनाना

[![टेक्स्ट जनरेशन एप्लिकेशन बनाना](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.hi.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(इस पाठ का वीडियो देखने के लिए ऊपर दी गई छवि पर क्लिक करें)_

आपने अब तक इस पाठ्यक्रम के माध्यम से देखा है कि प्रॉम्प्ट्स जैसे मुख्य अवधारणाएं हैं और यहां तक कि एक पूरा अनुशासन "प्रॉम्प्ट इंजीनियरिंग" कहा जाता है। कई उपकरण जिनके साथ आप बातचीत कर सकते हैं जैसे ChatGPT, Office 365, Microsoft Power Platform और अधिक, आपको कुछ हासिल करने के लिए प्रॉम्प्ट्स का उपयोग करने में सहायता करते हैं।

किसी ऐप में ऐसा अनुभव जोड़ने के लिए, आपको प्रॉम्प्ट्स, पूर्णता और काम करने के लिए एक लाइब्रेरी चुनने जैसी अवधारणाओं को समझना होगा। यही आप इस अध्याय में सीखेंगे।

## परिचय

इस अध्याय में, आप:

- openai लाइब्रेरी और इसके मुख्य अवधारणाओं के बारे में जानेंगे।
- openai का उपयोग करके एक टेक्स्ट जनरेशन ऐप बनाएंगे।
- टेक्स्ट जनरेशन ऐप बनाने के लिए प्रॉम्प्ट, तापमान, और टोकन जैसी अवधारणाओं का उपयोग कैसे करें, समझेंगे।

## सीखने के लक्ष्य

इस पाठ के अंत में, आप सक्षम होंगे:

- समझाएं कि टेक्स्ट जनरेशन ऐप क्या है।
- openai का उपयोग करके एक टेक्स्ट जनरेशन ऐप बनाए।
- अपने ऐप को अधिक या कम टोकन का उपयोग करने के लिए कॉन्फ़िगर करें और तापमान बदलें, ताकि विविध आउटपुट प्राप्त हो सके।

## टेक्स्ट जनरेशन ऐप क्या है?

आमतौर पर जब आप एक ऐप बनाते हैं, तो उसमें कुछ प्रकार का इंटरफ़ेस होता है जैसे:

- कमांड-आधारित। कंसोल ऐप्स सामान्य ऐप्स हैं जहां आप एक कमांड टाइप करते हैं और यह एक कार्य करता है। उदाहरण के लिए, `git` एक कमांड-आधारित ऐप है।
- यूजर इंटरफेस (UI)। कुछ ऐप्स में ग्राफिकल यूजर इंटरफेस (GUIs) होते हैं जहां आप बटन क्लिक करते हैं, टेक्स्ट इनपुट करते हैं, विकल्प चुनते हैं और अधिक।

### कंसोल और UI ऐप्स सीमित हैं

इसे कमांड-आधारित ऐप से तुलना करें जहां आप एक कमांड टाइप करते हैं:

- **यह सीमित है**। आप सिर्फ कोई भी कमांड टाइप नहीं कर सकते, केवल वही जो ऐप समर्थन करता है।
- **भाषा विशेष**। कुछ ऐप्स कई भाषाओं का समर्थन करते हैं, लेकिन डिफ़ॉल्ट रूप से ऐप एक विशेष भाषा के लिए बनाया गया है, भले ही आप अधिक भाषा समर्थन जोड़ सकें।

### टेक्स्ट जनरेशन ऐप्स के लाभ

तो टेक्स्ट जनरेशन ऐप कैसे अलग है?

एक टेक्स्ट जनरेशन ऐप में, आपके पास अधिक लचीलापन होता है, आप एक सेट कमांड्स या एक विशेष इनपुट भाषा तक सीमित नहीं होते हैं। इसके बजाय, आप प्राकृतिक भाषा का उपयोग करके ऐप के साथ बातचीत कर सकते हैं। एक और लाभ यह है कि आप पहले से ही एक डेटा स्रोत के साथ बातचीत कर रहे हैं जो विशाल जानकारी के कॉर्पस पर प्रशिक्षित किया गया है, जबकि एक पारंपरिक ऐप डेटाबेस में क्या है पर सीमित हो सकता है।

### मैं टेक्स्ट जनरेशन ऐप के साथ क्या बना सकता हूँ?

आप कई चीजें बना सकते हैं। उदाहरण के लिए:

- **एक चैटबॉट**। एक चैटबॉट जो विषयों के बारे में प्रश्नों का उत्तर देता है, जैसे आपकी कंपनी और उसके उत्पाद, एक अच्छा मेल हो सकता है।
- **सहायक**। LLMs टेक्स्ट को संक्षेपित करने, टेक्स्ट से अंतर्दृष्टि प्राप्त करने, रिज्यूमे जैसे टेक्स्ट उत्पन्न करने और अधिक चीजों में महान होते हैं।
- **कोड सहायक**। जिस भाषा मॉडल का आप उपयोग करते हैं, उसके आधार पर आप एक कोड सहायक बना सकते हैं जो आपको कोड लिखने में मदद करता है। उदाहरण के लिए, आप GitHub Copilot के साथ-साथ ChatGPT का उपयोग कर सकते हैं ताकि आपको कोड लिखने में मदद मिल सके।

## मैं कैसे शुरू कर सकता हूँ?

खैर, आपको एक LLM के साथ एकीकरण का तरीका खोजने की आवश्यकता है जो आमतौर पर निम्नलिखित दो दृष्टिकोणों को शामिल करता है:

- एक API का उपयोग करें। यहां आप अपने प्रॉम्प्ट के साथ वेब अनुरोध बना रहे हैं और उत्पन्न टेक्स्ट वापस प्राप्त कर रहे हैं।
- एक लाइब्रेरी का उपयोग करें। लाइब्रेरी API कॉल्स को समेटने में मदद करती हैं और उन्हें उपयोग करने में आसान बनाती हैं।

## लाइब्रेरी/SDKs

LLMs के साथ काम करने के लिए कुछ प्रसिद्ध लाइब्रेरी हैं जैसे:

- **openai**, यह लाइब्रेरी आपके मॉडल से जुड़ने और प्रॉम्प्ट्स भेजने में आसानी प्रदान करती है।

फिर कुछ उच्च स्तर पर काम करने वाली लाइब्रेरी हैं जैसे:

- **Langchain**। Langchain प्रसिद्ध है और Python का समर्थन करता है।
- **Semantic Kernel**। Semantic Kernel Microsoft द्वारा एक लाइब्रेरी है जो C#, Python, और Java भाषाओं का समर्थन करती है।

## openai का उपयोग करके पहला ऐप

आइए देखें कि हम अपना पहला ऐप कैसे बना सकते हैं, हमें किन लाइब्रेरी की आवश्यकता है, कितना आवश्यक है और इसी तरह।

### openai इंस्टॉल करें

OpenAI या Azure OpenAI के साथ बातचीत करने के लिए वहां कई लाइब्रेरी हैं। C#, Python, JavaScript, Java और अधिक जैसे कई प्रोग्रामिंग भाषाओं का उपयोग करना संभव है। हमने `openai` Python लाइब्रेरी का उपयोग करने के लिए चुना है, इसलिए हम इसे इंस्टॉल करने के लिए `pip` का उपयोग करेंगे।

```bash
pip install openai
```

### एक संसाधन बनाएँ

आपको निम्नलिखित कदम उठाने की आवश्यकता है:

- Azure पर एक खाता बनाएँ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI तक पहुँच प्राप्त करें। [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) पर जाएं और पहुँच के लिए अनुरोध करें।

  > [!NOTE]
  > लेखन के समय, आपको Azure OpenAI तक पहुँच के लिए आवेदन करना होगा।

- Python इंस्टॉल करें <https://www.python.org/>
- Azure OpenAI सेवा संसाधन बनाया हो। संसाधन बनाने के लिए इस गाइड को देखें [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API कुंजी और एंडपॉइंट ढूंढें

इस बिंदु पर, आपको अपनी `openai` लाइब्रेरी को बताना होगा कि कौन सी API कुंजी का उपयोग करना है। अपनी API कुंजी खोजने के लिए, अपने Azure OpenAI संसाधन के "Keys and Endpoint" अनुभाग पर जाएं और "Key 1" मान को कॉपी करें।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

अब जब आपके पास यह जानकारी कॉपी की गई है, तो लाइब्रेरी को इसका उपयोग करने का निर्देश दें।

> [!NOTE]
> अपने API कुंजी को अपने कोड से अलग करना उचित है। आप इसे पर्यावरणीय चर का उपयोग करके कर सकते हैं।
>
> - पर्यावरणीय चर सेट करें `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### सेटअप कॉन्फ़िगरेशन Azure

यदि आप Azure OpenAI का उपयोग कर रहे हैं, तो यहाँ बताया गया है कि आप कॉन्फ़िगरेशन कैसे सेट करें:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

ऊपर हम निम्नलिखित सेट कर रहे हैं:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` वर्ग। यहाँ एक उदाहरण है:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

ऊपर के कोड में, हम एक पूर्णता ऑब्जेक्ट बनाते हैं और मॉडल और प्रॉम्प्ट को पास करते हैं जिसे हम उपयोग करना चाहते हैं। फिर हम उत्पन्न टेक्स्ट को प्रिंट करते हैं।

### चैट पूर्णता

अब तक, आपने देखा है कि हम `Completion` to generate text. But there's another class called `ChatCompletion` का उपयोग कर रहे हैं जो चैटबॉट्स के लिए अधिक उपयुक्त है। इसका उपयोग करने का एक उदाहरण यहाँ है:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

इस कार्यक्षमता के बारे में अधिक एक आगामी अध्याय में।

## अभ्यास - आपका पहला टेक्स्ट जनरेशन ऐप

अब जब हमने openai को सेटअप और कॉन्फ़िगर करना सीखा है, तो यह आपका पहला टेक्स्ट जनरेशन ऐप बनाने का समय है। अपना ऐप बनाने के लिए, इन चरणों का पालन करें:

1. एक वर्चुअल वातावरण बनाएँ और openai इंस्टॉल करें:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > यदि आप Windows का उपयोग कर रहे हैं, तो `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` मान टाइप करें।

1. एक _app.py_ फ़ाइल बनाएँ और उसमें निम्नलिखित कोड दें:

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
   > यदि आप Azure OpenAI का उपयोग कर रहे हैं, तो आपको `api_type` to `azure` and set the `api_key` को अपने Azure OpenAI कुंजी पर सेट करने की आवश्यकता है।

   आपको निम्नलिखित की तरह एक आउटपुट देखना चाहिए:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विभिन्न प्रकार के प्रॉम्प्ट्स, विभिन्न चीजों के लिए

अब आपने देखा है कि प्रॉम्प्ट का उपयोग करके टेक्स्ट कैसे उत्पन्न किया जाता है। आपके पास एक प्रोग्राम भी चल रहा है जिसे आप संशोधित और बदल सकते हैं ताकि विभिन्न प्रकार के टेक्स्ट उत्पन्न कर सकें।

प्रॉम्प्ट्स का उपयोग सभी प्रकार के कार्यों के लिए किया जा सकता है। उदाहरण के लिए:

- **एक प्रकार का टेक्स्ट उत्पन्न करें**। उदाहरण के लिए, आप एक कविता, क्विज के लिए प्रश्न आदि उत्पन्न कर सकते हैं।
- **सूचना खोजें**। आप प्रॉम्प्ट्स का उपयोग जानकारी खोजने के लिए कर सकते हैं जैसे कि निम्नलिखित उदाहरण 'वेब विकास में CORS का क्या मतलब है?'।
- **कोड उत्पन्न करें**। आप प्रॉम्प्ट्स का उपयोग कोड उत्पन्न करने के लिए कर सकते हैं, उदाहरण के लिए ईमेल को मान्य करने के लिए उपयोग किए जाने वाले नियमित अभिव्यक्ति विकसित करना या क्यों न एक पूरा प्रोग्राम उत्पन्न करें, जैसे एक वेब ऐप?

## एक अधिक व्यावहारिक उपयोग मामला: एक रेसिपी जनरेटर

कल्पना करें कि आपके पास घर पर सामग्री हैं और आप कुछ पकाना चाहते हैं। इसके लिए, आपको एक रेसिपी की आवश्यकता है। रेसिपी खोजने का एक तरीका एक खोज इंजन का उपयोग करना है या आप ऐसा करने के लिए एक LLM का उपयोग कर सकते हैं।

आप एक प्रॉम्प्ट इस तरह लिख सकते हैं:

> "मुझे निम्नलिखित सामग्री के साथ एक डिश के लिए 5 रेसिपी दिखाएं: चिकन, आलू, और गाजर। प्रति रेसिपी, उपयोग की गई सभी सामग्री सूचीबद्ध करें"

उपरोक्त प्रॉम्प्ट के दिए गए, आपको इस तरह का एक प्रतिक्रिया मिल सकता है:

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

यह परिणाम शानदार है, मुझे पता है कि क्या पकाना है। इस बिंदु पर, क्या उपयोगी सुधार हो सकते हैं:

- सामग्री को फ़िल्टर करना जो मुझे पसंद नहीं है या जिससे मुझे एलर्जी है।
- एक शॉपिंग सूची तैयार करें, अगर मेरे पास घर पर सभी सामग्री नहीं हैं।

उपरोक्त मामलों के लिए, चलिए एक अतिरिक्त प्रॉम्प्ट जोड़ते हैं:

> "कृपया लहसुन के साथ रेसिपी हटाएं क्योंकि मुझे एलर्जी है और इसे कुछ और से बदलें। साथ ही, कृपया रेसिपी के लिए एक शॉपिंग सूची तैयार करें, यह मानते हुए कि मेरे पास पहले से ही चिकन, आलू और गाजर घर पर हैं।"

अब आपके पास एक नया परिणाम है, अर्थात:

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

यह आपकी पाँच रेसिपी हैं, जिसमें कोई लहसुन का उल्लेख नहीं है और आपके पास घर पर जो सामग्री पहले से है उसे ध्यान में रखते हुए एक शॉपिंग सूची भी है।

## अभ्यास - एक रेसिपी जनरेटर बनाएं

अब जब हमने एक परिदृश्य खेला है, तो चलिए प्रदर्शित परिदृश्य से मेल खाने के लिए कोड लिखते हैं। ऐसा करने के लिए, इन चरणों का पालन करें:

1. मौजूदा _app.py_ फ़ाइल को प्रारंभिक बिंदु के रूप में उपयोग करें
1. `prompt` चर को खोजें और उसके कोड को निम्नलिखित में बदलें:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   यदि आप अब कोड चलाते हैं, तो आपको इस तरह का एक आउटपुट देखना चाहिए:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > नोट, आपका LLM अनिश्चित है, इसलिए हर बार जब आप प्रोग्राम चलाते हैं तो आपको अलग परिणाम मिल सकते हैं।

   शानदार, चलिए देखते हैं कि हम चीजों को कैसे सुधार सकते हैं। चीजों को सुधारने के लिए, हम चाहते हैं कि कोड लचीला हो, ताकि सामग्री और रेसिपी की संख्या को सुधारा और बदला जा सके।

1. चलिए कोड को निम्नलिखित तरीके से बदलते हैं:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   परीक्षण रन के लिए कोड लेना, इस तरह दिख सकता है:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फ़िल्टर और शॉपिंग सूची जोड़कर सुधार करें

अब हमारे पास एक काम करने वाला ऐप है जो रेसिपी उत्पन्न करने में सक्षम है और यह लचीला है क्योंकि यह उपयोगकर्ता से इनपुट पर निर्भर करता है, न केवल रेसिपी की संख्या बल्कि उपयोग की गई सामग्री पर भी।

इसे और सुधारने के लिए, हम निम्नलिखित जोड़ना चाहते हैं:

- **सामग्री को फ़िल्टर करें**। हम सामग्री को फ़िल्टर करने में सक्षम होना चाहते हैं जिन्हें हम पसंद नहीं करते हैं या जिससे हमें एलर्जी है। इस परिवर्तन को पूरा करने के लिए, हम अपने मौजूदा प्रॉम्प्ट को संपादित कर सकते हैं और उसके अंत में एक फ़िल्टर शर्त जोड़ सकते हैं जैसे:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ऊपर, हम `{filter}` को प्रॉम्प्ट के अंत में जोड़ते हैं और हम उपयोगकर्ता से फ़िल्टर मान भी प्राप्त करते हैं।

  प्रोग्राम चलाने का एक उदाहरण इनपुट अब इस तरह दिख सकता है:

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

  जैसा कि आप देख सकते हैं, किसी भी रेसिपी में दूध नहीं है। लेकिन, अगर आपको लैक्टोज असहिष्णुता है, तो आप रेसिपी में चीज़ को भी फ़िल्टर करना चाह सकते हैं, इसलिए स्पष्ट होना आवश्यक है।

- **एक शॉपिंग सूची तैयार करें**। हम एक शॉपिंग सूची तैयार करना चाहते हैं, यह मानते हुए कि हमारे पास पहले से घर पर क्या है।

  इस कार्यक्षमता के लिए, हम या तो एक ही प्रॉम्प्ट में सब कुछ हल करने की कोशिश कर सकते हैं या हम इसे दो प्रॉम्प्ट में विभाजित कर सकते हैं। चलिए बाद वाले दृष्टिकोण की कोशिश करते हैं। यहाँ हम एक अतिरिक्त प्रॉम्प्ट जोड़ने का सुझाव दे रहे हैं, लेकिन उसके काम करने के लिए, हमें पहले प्रॉम्प्ट के परिणाम को दूसरे प्रॉम्प्ट के संदर्भ के रूप में जोड़ना होगा।

  कोड के उस हिस्से को खोजें जो पहले प्रॉम्प्ट के परिणाम को प्रिंट करता है और उसके नीचे निम्नलिखित कोड जोड़ें:

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

  निम्नलिखित ध्यान दें:

  1. हम पहले प्रॉम्प्ट के परिणाम को नए प्रॉम्प्ट में जोड़कर एक नया प्रॉम्प्ट बना रहे हैं:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. हम एक नया अनुरोध बना रहे हैं, लेकिन पहले प्रॉम्प्ट में मांगे गए टोकन की संख्या को भी ध्यान में रखते हुए, इसलिए इस बार हम कहते हैं `max_tokens` 1200 है।

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     इस कोड को एक स्पिन के लिए लेने पर, हम अब निम्नलिखित आउटपुट पर पहुँचते हैं:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## अपनी सेटअप को सुधारें

जो हमारे पास अब तक है वह काम करने वाला कोड है, लेकिन कुछ सुधार हमें चीजों को और सुधारने के लिए करने चाहिए। कुछ चीजें जो हमें करनी चाहिए:

- **कोड से रहस्यों को अलग करें**, जैसे API कुंजी। रहस्य कोड में नहीं होते हैं और उन्हें सुरक्षित स्थान पर संग्रहीत किया जाना चाहिए। कोड से रहस्यों को अलग करने के लिए, हम पर्यावरणीय चर और लाइब्रेरी जैसे `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` फ़ाइल का उपयोग कर सकते हैं जिसमें निम्नलिखित सामग्री होती है:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > नोट, Azure के लिए, आपको निम्नलिखित पर्यावरणीय चर सेट करने की आवश्यकता है:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     कोड में, आप पर्यावरणीय चर को इस तरह लोड करेंगे:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **टोकन की लंबाई पर एक

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।