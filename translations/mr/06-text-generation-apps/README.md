# टेक्स्ट जनरेशन अ‍ॅप्लिकेशन्स तयार करणे

[![टेक्स्ट जनरेशन अ‍ॅप्लिकेशन्स तयार करणे](../../../translated_images/mr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील चित्रावर क्लिक करा)_

तुम्ही आतापर्यंत या अभ्यासक्रमाद्वारे पाहिले आहे की प्रॉम्प्टसारख्या मूलभूत संकल्पना आहेत आणि "प्रॉम्प्ट अभियांत्रण" नावाचा एक संपूर्ण शिस्तदेखील आहे. तुम्ही ChatGPT, Office 365, Microsoft Power Platform आणि इतर अनेक साधने वापरू शकता, ज्यात काहीतरी साध्य करण्यासाठी प्रॉम्प्ट वापरले जातात.

तुम्हाला अशी अनुभव अ‍ॅपमध्ये जोडायची असल्यास, तुम्हाला प्रॉम्प्ट, पूर्णता यासारख्या संकल्पना समजून घ्याव्या लागतील आणि काम करण्यासाठी एक लायब्ररी निवडावी लागेल. याच गोष्टींचा तुम्हाला या प्रकरणात शिकायला मिळेल.

## परिचय

या प्रकरणात, तुम्ही:

- openai लायब्ररी आणि तिच्या मूलभूत संकल्पनांविषयी जाणून घ्या.
- openai वापरून एक टेक्स्ट जनरेशन अ‍ॅप तयार करा.
- प्रॉम्प्ट, तापमान आणि टोकन्स यांसारख्या संकल्पना कशा वापरायच्या ते समजून घ्या, ज्याद्वारे टेक्स्ट जनरेशन अ‍ॅप तयार करता येईल.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- टेक्स्ट जनरेशन अ‍ॅप म्हणजे काय ते समजावून सांगा.
- openai वापरून टेक्स्ट जनरेशन अ‍ॅप तयार करा.
- तुमचे अ‍ॅप अधिक किंवा कमी टोकन्स वापरण्यासाठी आणि तापमान बदलण्यासाठी सुसज्ज करा, ज्यामुळे वेगळा आउटपुट मिळेल.

## टेक्स्ट जनरेशन अ‍ॅप म्हणजे काय?

सामान्यतः अ‍ॅप तयार करताना त्याला काही प्रकारचे इंटरफेस असतो, खालीलप्रमाणे:

- कमांड-आधारित. कन्सोल अ‍ॅप्स असे अ‍ॅप्स असतात जेथे तुम्ही एक कमांड टाइप करता आणि ते एखादे कार्य पार पाडते. उदाहरणार्थ, `git` हा एक कमांड-आधारित अ‍ॅप आहे.
- युजर इंटरफेस (UI). काही अ‍ॅप्समध्ये ग्राफिकल युजर इंटरफेस (GUIs) असतात जिथे तुम्ही बटणे क्लिक करता, मजकूर टाइप करता, पर्याय निवडता इत्यादी.

### कन्सोल आणि UI अ‍ॅप्स मर्यादित आहेत

त्यांची तुलना करा जिथे तुम्ही कमांड टाइप करता तेथे:

- **ही मर्यादित आहेत**. तुम्ही काहीही कमांड टाइप करू शकत नाही, फक्त अ‍ॅप जे समर्थन करते त्या कमांड्सच.
- **भाषा-विशिष्ट**. काही अ‍ॅप्स अनेक भाषा समर्थित करतात, पण साधारणपणे अ‍ॅप एक विशिष्ट भाषेसाठी तयार केलेले असते, जरी तुम्ही अधिक भाषा समर्थन जोडू शकता.

### टेक्स्ट जनरेशन अ‍ॅप्सचे फायदे

तर मग टेक्स्ट जनरेशन अ‍ॅप कसे वेगळे आहे?

टेक्स्ट जनरेशन अ‍ॅपमध्ये तुम्हाला जास्त लवचिकता असते, तुम्ही कमांड्सच्या सेट किंवा विशिष्ट इनपुट भाषेपुरते मर्यादित नाही. त्याऐवजी, तुम्ही नैसर्गिक भाषेतून अ‍ॅपशी संवाद साधू शकता. आणखी एक फायदा म्हणजे तुम्ही आधीच अशा डेटाच्या स्रोताशी संवाद साधत आहात ज्यावर विशाल माहिती संचावर प्रशिक्षण घेतले गेले आहे, तर पारंपरिक अ‍ॅप एका डेटाबेसशी मर्यादित असू शकते.

### टेक्स्ट जनरेशन अ‍ॅपने काय करता येईल?

तुम्ही बरेच काही तयार करू शकता. उदाहरणार्थ:

- **चॅटबोट**. एखादा चॅटबोट जो तुमच्या कंपनी आणि त्याच्या उत्पादनांविषयी प्रश्नांची उत्तरे देतो, तो चांगला पर्याय ठरू शकतो.
- **सहायक**. LLMs सारखे मोठे भाषा मॉडेल्स मजकूर सारांशित करण्यास, त्यातून अंतर्दृष्टी मिळविण्यास, रेझ्युमे सारखे मजकूर तयार करण्यास चांगले आहेत.
- **कोड सहाय्यक**. तुम्ही वापरत असलेल्या भाषा मॉडेलवर अवलंबून, तुम्ही कोड लिहिण्यास मदत करणारा कोड सहाय्यक तयार करू शकता. उदाहरणार्थ, GitHub Copilot आणि ChatGPT सारखे उत्पादन वापरून तुम्हाला कोड लिहिण्यात मदत करता येईल.

## मी कसे सुरू करू शकतो?

तुम्हाला LLM सह एकत्रित होण्याचा मार्ग सापडावा लागेल, जो सामान्यतः खालील दोन मार्गांनी साध्य होतो:

- API वापरा. येथे तुम्ही तुमच्या प्रॉम्प्टसह वेब विनंत्या तयार करता आणि निर्मित टेक्स्ट परत मिळवता.
- लायब्ररी वापरा. लायब्रऱ्या API कॉल्स वेगळे करतात आणि वापरायला सोपे करतात.

## लायब्रऱ्या/SDKs

LLMs सह काम करण्यासाठी काही प्रसिद्ध लायब्रऱ्या आहेत जसे की:

- **openai**, ही लायब्ररी तुमच्या मॉडेलशी सहज कनेक्ट होण्यास आणि प्रॉम्प्ट पाठवण्यास मदत करते.

त्यानंतर, काही उच्च पातळीवरील लायब्रऱ्या आहेत जसे की:

- **Langchain**. Langchain प्रसिद्ध आहे आणि Python सपोर्ट करते.
- **Semantic Kernel**. Semantic Kernel ही Microsoft ची लायब्ररी आहे जी C#, Python आणि Java भाषा समर्थन करते.

## openai वापरून पहिला अ‍ॅप

चला पाहूया की आपण आपला पहिला अ‍ॅप कसा तयार करू शकतो, कोणत्या लायब्रऱ्या आवश्यक आहेत, किती आवश्यक आहे आणि इतर.

### openai इन्स्टॉल करा

OpenAI किंवा Azure OpenAI शी संवाद साधण्यासाठी अनेक लायब्रऱ्या उपलब्ध आहेत. तुम्ही विविध प्रोग्रामिंग भाषा देखील वापरू शकता जसे की C#, Python, JavaScript, Java आणि अधिक. आम्ही `openai` Python लायब्ररी वापरण्यासाठी निवड केली आहे, म्हणून आम्ही `pip` वापरून ती इन्स्टॉल करू.

```bash
pip install openai
```

### एक संसाधन तयार करा

तुम्हाला खालील प्रत्येक चरण पार पाडावे लागतील:

- Azure वर एक खाते तयार करा [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI ची प्रवेश मिळवा. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) येथे जा आणि प्रवेशाची विनंती करा.

  > [!NOTE]
  > लेखनाच्या वेळी, तुम्हाला Azure OpenAI साठी प्रवेशासाठी अर्ज करावा लागतो.

- Python इन्स्टॉल करा <https://www.python.org/>
- Azure OpenAI सेवा संसाधन तयार करा. कसे [संसाधन तयार करायचे](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) ते या मार्गदर्शकात पहा.

### API की आणि एंडपॉइंट शोधा

या टप्प्यावर, तुम्हाला तुमच्या `openai` लायब्ररीला कोणती API की वापरायची आहे ते सांगावे लागेल. तुमची API की शोधण्यासाठी, तुमच्या Azure OpenAI संसाधनाच्या "किज आणि एंडपॉइंट" विभागात जा आणि "की 1" मूल्य कॉपी करा.

![Azure पोर्टलमधील कीज आणि एंडपॉइंट संसाधन ब्लेड](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

आता या माहितीची कॉपी झाल्यानंतर, लायब्ररी याचा वापर कसा करायचा ते निर्देश करूया.

> [!NOTE]
> तुमची API की कोडपासून वेगळी ठेवणे उपयुक्त आहे. तुम्ही हे वातावरण बदलणाऱ्या (environment variables) वापरून करू शकता.
>
> - पर्यावरण चल `OPENAI_API_KEY` आपल्या API कीसाठी सेट करा.
>   `export OPENAI_API_KEY='sk-...'`

### Azure कॉन्फिगरेशन सेटअप करा

जर तुम्ही Azure OpenAI वापरत असाल (आता Microsoft Foundry चा भाग), तर कॉन्फिगरेशन सेटअप कसा करायचा ते येथे आहे. आम्ही सामान्य `OpenAI` क्लायंट वापरतो ज्याने Azure OpenAI `/openai/v1/` एंडपॉइंटकडे निर्देश केला आहे, जे Responses API सोबत कार्य करते आणि कोणतीही `api_version` आवश्यकता नाही:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

वर आम्ही खालील सेट करत आहोत:

- `api_key`, ही तुमची API की आहे जी Azure पोर्टल किंवा Microsoft Foundry पोर्टलमध्ये सापडेल.
- `base_url`, ही तुमची Foundry संसाधन एंडपॉइंट आहे ज्यावर `/openai/v1/` जोडलेले आहे. स्थिर v1 एंडपॉइंट OpenAI आणि Azure OpenAI मध्ये कोणतीही `api_version` व्यवस्थापनाशिवाय काम करते.

> [!NOTE] > `os.environ` पर्यावरण चल वाचते. तुम्ही हे वापरून `AZURE_OPENAI_API_KEY` आणि `AZURE_OPENAI_ENDPOINT` सारखे पर्यावरण बदलणारे वाचू शकता. हे पर्यावरण चल तुमच्या टर्मिनलमध्ये सेट करा किंवा `dotenv` सारखी लायब्ररी वापरा.

## टेक्स्ट जनरेट करा

टेक्स्ट जनरेट करण्याचा मार्ग म्हणजे Responses API वापरून `responses.create` पद्धत वापरणे. उदाहरण पाहा:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

वर दिलेल्या कोडमध्ये, आम्ही एक प्रतिसाद तयार करतो आणि वापरायच्या मॉडेलसह प्रॉम्प्ट देतो. नंतर आम्ही `response.output_text` द्वारे तयार झालेला मजकूर छापतो.

### बहु-टर्न संभाषणे

Responses API एकट्या-टर्नच्या टेक्स्ट जनरेशनसाठी आणि बहु-टर्न चॅटबॉट्ससाठी योग्य आहे - तुम्ही `input` मध्ये संदेशांची यादी पुरवून संभाषण तयार करता:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

या कार्यक्षमतेवर अधिक माहिती येणाऱ्या प्रकरणात दिली जाईल.

## सराव - तुमचा पहिला टेक्स्ट जनरेशन अ‍ॅप

आम्ही कसे openai सेटअप आणि कॉन्फिगर करायचे ते शिकलो, आता तुमचा पहिला टेक्स्ट जनरेशन अ‍ॅप तयार करू या. तुमचे अ‍ॅप तयार करण्यासाठी, खालील चरण पाळा:

1. एक वर्चुअल वातावरण तयार करा आणि openai इन्स्टॉल करा:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > जर तुम्ही Windows वापरत असाल तर `venv\Scripts\activate` टाइप करा, `source venv/bin/activate` ऐवजी.

   > [!NOTE]
   > तुमची Azure OpenAI की शोधण्यासाठी [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) येथे जा, `Open AI` शोधा, नंतर `Open AI resource` निवडा, त्यानंतर `Keys and Endpoint` निवडा आणि `Key 1` मूल्यास कॉपी करा.

1. एक _app.py_ फाइल तयार करा आणि त्यात खालील कोड द्या:

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
   > जर तुम्ही साधा OpenAI वापरत असाल (Azure नाही), तर `client = OpenAI(api_key="<replace this value with your OpenAI key>")` वापरा (कोणतीही `base_url` नाही) आणि डिप्लॉयमेंट नावाऐवजी `gpt-5-mini` सारखे मॉडेल नाव द्या.

   तुम्हाला असाच आउटपुट दिसेल:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## वेगवेगळ्या प्रकारचे प्रॉम्प्ट्स, वेगवेगळ्या गोष्टींसाठी

आता तुम्ही प्रॉम्प्ट वापरून टेक्स्ट कसा जनरेट करायचा ते पाहिले आहे. तुमच्याकडे एक प्रोग्राम आहे जे तुम्ही सुधारू शकता आणि बदलू शकता वेगळ्या प्रकारच्या टेक्स्टसाठी.

प्रॉम्प्ट्स सर्व प्रकारच्या कामांसाठी वापरले जाऊ शकतात. उदाहरणार्थ:

- **एका प्रकारचा टेक्स्ट तयार करा**. उदाहरणार्थ, तुम्ही कविता, क्विझसाठी प्रश्न वगैरे तयार करू शकता.
- **माहिती शोधा**. तुम्ही प्रॉम्प्ट्स वापरून माहिती शोधू शकता जसे की हा उदाहरण 'वेब डेव्हलपमेंट मध्ये CORS म्हणजे काय?'.
- **कोड तयार करा**. तुम्ही प्रॉम्प्ट वापरून कोड तयार करू शकता, जसे की इमेल्सची वैधता तपासण्यासाठी रेग्युलर एक्सप्रेशन तयार करणे किंवा संपूर्ण प्रोग्राम तयार करणे, जसे वेब अ‍ॅप तयार करणे.

## एक अधिक व्यावहारिक वापर केस: रेसिपी जनरेटर

समजा तुमच्याकडे घरच्या गॅरोमध्ये साहित्य आहे आणि तुम्हाला काहीतरी स्वयंपाक करायचे आहे. त्यासाठी तुम्हाला रेसिपी लागेल. रेसिपी शोधण्यासाठी तुम्ही सर्च इंजिन वापरू शकता किंवा तुम्ही LLM वापरू शकता.

तुम्ही अशा प्रकारचा प्रॉम्प्ट लिहू शकता:

> "खालिल साहित्यांसह ५ पदार्थांच्या रेसिपी दाखवा: चिकन, बटाटे आणि गाजर. प्रत्येक रेसिपीसाठी सर्व साहित्य सूचीबद्ध करा"

वर दिलेल्या प्रॉम्प्टनुसार, तुम्हाला खालीलप्रमाणे प्रतिसाद मिळू शकतो:

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

हा परिणाम चांगला आहे, मला काय बनवायचे ते कळाले. या टप्प्यावर, उपयुक्त सुधारणा असू शकतील:

- मला न आवडणारे किंवा ज्यांना मला अलर्जी आहे असे साहित्य हटवणे.
- जर माझ्याकडे सर्व साहित्य नसेल तर खरेदी यादी तयार करणे.

वरील प्रकरणांसाठी, आणखी एक प्रॉम्प्ट जोडूया:

> "कृपया लसूण असलेली रेसिपी काढून टाका कारण मला त्याची अलर्जी आहे आणि ते काही दुसऱ्या वस्तूपासून बदला. तसेच, कृपया रेसिपींसाठी खरेदी यादी तयार करा, लक्षात ठेवा माझ्याकडे आधीच चिकन, बटाटे आणि गाजर आहे."

आता तुमच्याकडे नवीन निकाल आहे, म्हणजे:

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

ही तुमची पाच रेसिपी आहेत, ज्या लसूणशिवाय आहेत आणि तुमच्याकडे असलेल्या सामग्रीसाठी एक खरेदी यादी देखील आहे.

## सराव - रेसिपी जनरेटर तयार करा

आता आपण एक प्रकरण सादर केले, चला त्यानुसार कोड लिहूया. असे करण्यासाठी, खालील चरण पाळा:

1. विद्यमान _app.py_ फाइल वापरून सुरुवात करा
1. `prompt` चल शोधा आणि त्याचा कोड खालीलप्रमाणे बदला:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   जर तुम्ही कोड चालवला, तर अशी आउटपुट दिसेल:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > लक्षात ठेवा, तुमचा LLM गैरनिश्चित आहे, त्यामुळे प्रत्येक वेळी वेगळे निकाल मिळू शकतात.

   उत्कृष्ट, बघूया आपण कसे सुधारणा करू शकतो. सुधारणा करण्यासाठी, आपण कोड लवचिक केला पाहिजे, जेणेकरून साहित्य आणि रेसिपींची संख्या बदलता येईल.

1. कोड खालीलप्रमाणे बदला:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   चाचणी रनसाठी कोड असे दिसू शकतो:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर आणि खरेदी यादी जोडून सुधारणा करा

आता आपल्याकडे रेसिपी तयार करणारा कार्यशील अ‍ॅप आहे आणि तो वापरकर्त्याच्या इनपुटवर आधारित आहे, रेसिपींच्या संख्येसह तसेच वापरण्यात आलेल्या साहित्यावरही.

अधिक सुधारण्यासाठी, खालील वैशिष्ट्ये जोडायची आहेत:

- **साहित्य फिल्टर करा**. आपण नको असलेले किंवा ज्यांना आपण अस्वस्थ आहोत असे साहित्य फिल्टर करू शकतो. हे करण्यासाठी आपल्या प्रॉम्प्टमध्ये एक फिल्टर स्थिती खालीलप्रमाणे जोडू शकतो:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  वर, आपण प्रॉम्प्टच्या शेवटी `{filter}` जोडतो आणि वापरकर्त्याकडून फिल्टरची किंमतही घेतो.

  प्रोग्राम चालवताना उदाहरणात्मक इनपुट असं दिसू शकतो:

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

  दिसतं की, दुध असलेली कोणतीही रेसिपी फिल्टर झाली आहे. पण जर तुम्हाला लॅक्टोज असहिष्णूता असेल तर तुम्हाला चीज असलेली रेसिपी देखील फिल्टर करायची असेल, त्यामुळे स्पष्ट असणे आवश्यक आहे.

- **खरेदी यादी तयार करा**. आपण आधीपासून घरात असलेल्या सामग्रीचा विचार करून खरेदी यादी तयार करू इच्छितो.

  या कार्यासाठी, आपण सगळं एकाच प्रॉम्प्टमध्ये केल्यास किंवा दोन प्रॉम्प्ट्समध्ये विभाजित केल्यास चालेल, आपण दुसरा मार्ग वापरू. येथे आम्ही एक अतिरिक्त प्रॉम्प्ट जोडण्याचा सल्ला देतो, पण ते काम करण्यासाठी आधीच्या प्रॉम्प्टचा परिणाम दुसऱ्या प्रॉम्प्टच्या संदर्भ म्हणून जोडणे आवश्यक आहे.

  पहिल्या प्रॉम्प्टच्या निकालाला प्रिंट करणाऱ्या कोडच्या भागातून खालील कोड जोडा:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  लक्षात घ्या:

  1. आम्ही नवीन प्रॉम्प्ट तयार करत आहोत ज्यात पहिल्या प्रॉम्प्टचा निकाल जोडला आहे:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. नवीन विनंती करतो, पण पहिल्या प्रॉम्प्टमधील टोकन्सच्या संख्येचा विचार करत, यावेळी आम्ही म्हणतो `max_output_tokens` हे 1200 आहे.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     या कोडला वापरून आम्ही आता खालील आउटपुटपर्यंत पोहोचतो:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## तुमच्या सेटअपमध्ये सुधारणा करा

आतापर्यंत आपल्याकडे काम करणारा कोड आहे, परंतु आणखी सुधारण्यासाठी काही बदल केले पाहिजेत. काही गोष्टी ज्या आपण करायला पाहिजेत त्या आहेत:

- **गुपिते कोडपासून वेगळे करा**, जसं की API की. गुपिते कोडमध्ये असू नयेत आणि सुरक्षित ठिकाणी संग्रहित केले पाहिजेत. गुपिते कोडपासून वेगळे करण्यासाठी, आपण एन्व्हायर्नमेंट व्हेरिएबल्स आणि `python-dotenv` सारख्या लायब्ररींचा वापर करू शकतो ज्यामुळे ते फाईलमधून लोड करता येतील. कोडमध्ये ते कसे दिसेल ते खाली आहे:

  1. खालील सामग्रीसह `.env` फाईल तयार करा:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > लक्षात ठेवा, Microsoft Foundry मध्ये Azure OpenAI साठी, खालील एन्व्हायर्नमेंट व्हेरिएबल्स सेट करणे आवश्यक आहे:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमध्ये, आपण एन्व्हायर्नमेंट व्हेरिएबल्स खालीलप्रमाणे लोड कराल:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लांबीबाबत एक शब्द**. आपल्याला हवे असलेले टेक्स्ट तयार करण्यासाठी किती टोकन लागतात याचा विचार करणे आवश्यक आहे. टोकनसाठी पैसे लागतात, त्यामुळे शक्य तितक्या कमी टोकन वापरण्याचा प्रयत्न करा. उदाहरणार्थ, आपल्याला शंका विचारण्यासाठी टोकन कमी कसे वापरू शकतो याचा विचार करा.

  वापरले जाणारे टोकन बदलण्यासाठी, आपण `max_output_tokens` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर आपल्याला 100 टोकन्स वापरायचे असतील तर:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **तापमानाने प्रयोग करणे**. तापमान हा एक महत्त्वाचा संदर्भ आहे ज्यामुळे आपल्या प्रोग्रामचे प्रदर्शन ठरते. तापमानाची मूल्य जास्त असेल तर आउटपुट जास्त रँडम (असहज) होईल. तुलनेत, तापमान कमी असेल तर आउटपुट अधिक अपेक्षित असेल. आपण आपल्याला हवे तसे आउटपुट विविधतेसाठी विचार करा.

  तापमान बदलण्यासाठी, आपण `temperature` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर आपण 0.5 तापमान राखू इच्छित असाल तर:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > लक्षात ठेवा, 1.0 जवळजवळ तापमान जास्त विविधतेसाठी आहे.

- **कारण सांगणाऱ्या मॉडेल्सना `temperature` वापरायची गरज नाही**. हे महत्वाचे 2026 चे परिवर्तन आहे. सध्या Microsoft Foundry मध्ये गैर-डिप्रिकेटेड मॉडेल्स म्हणजे **कारण सांगणारे मॉडेल्स** (GPT-5 कुटुंब, o-series) - आणि ते **`temperature` किंवा `top_p` समर्थन करीत नाहीत** (आणि नाही `max_tokens`; त्यासाठी `max_output_tokens` वापरा). जर आपण `temperature` ला `gpt-5-mini` पेक्षा पाठवले तर "parameter not supported" त्रुटी मिळेल. त्यामुळे वरील तापमान उदाहरणासाठी, अशा मॉडेलकडे निदर्शित करा जे अजून Sampling controls समर्थन करते - उदाहरणार्थ, एक मुक्त **Llama** मॉडेल जसे की `Llama-3.3-70B-Instruct` [Microsoft Foundry मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मधून, Foundry Models / Azure AI Inference एपीआयद्वारे (जसे की `githubmodels-*` नमुन्यांमध्ये). कारण सांगणाऱ्या मॉडेल्ससाठी GPT-5 सारख्या, आउटपुट वेगळ्या पद्धतीने नियंत्रित करता येते:
  - **प्रॉम्प्ट इंजिनिअरिंग** - स्पष्ट निर्देश, उदाहरणे, आणि संरचित आउटपुट (पाठ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) पहा) जे Sampling नियंत्रक करत होते ते आता करते.
  - **कारण नियंत्रण** - पॅरामीटर्स जसे की reasoning effort/verbosity हे reasoning च्या खोलपणाला लेटन्सी आणि खर्च यांच्या विरुद्ध सांभाळतात.

  सारांश: `temperature`/`top_p` अनेक मॉडेल्सवर (Llama, Mistral, Phi, आणि GPT-4.x कुटुंब - तरी GPT-4.x डिप्रिकेट होतो आहे) अजूनही वैध आहेत, पण प्रवासाचा दिशादर्शक प्रॉम्प्ट इंजिनिअरिंग + कारण नियंत्रणावर GPT-5 सारख्या कारण सांगणाऱ्या मॉडेल्सवर आहे.

## असाइनमेंट

या असाइनमेंटसाठी, तुम्ही काय तयार करायचे ते निवडू शकता.

येथे काही सुचना आहेत:

- रेसिपी जनरेटर अॅप अधिक सुधारण्यासाठी त्यात फेरफार करा. तापमान मूल्यांसोबत आणि प्रॉम्प्टसह प्रयोग करा व पहा काय तयार करू शकता.
- "स्टडी बडी" तयार करा. हा अॅप एखाद्या विषयासंबंधी प्रश्नांची उत्तरे देऊ शकतो, उदाहरणार्थ Python, ज्यासाठी तुम्ही "Python मधील कोणता तरी विषय काय आहे?" किंवा "एखाद्या विषयासाठी कोड दाखवा" अशा प्रॉम्प्ट्स वापरू शकता.
- इतिहास बॉट, इतिहास जिवंत करा, बॉटला एखाद्या ऐतिहासिक व्यक्तिरेखेची भूमिका बजावायला सांगा आणि त्याच्याशी त्याच्या जीवन आणि काळाबाबत प्रश्न विचारा.

## सोल्यूशन

### स्टडी बडी

खाली एक सुरवातीचा प्रॉम्प्ट आहे, पाहा तुम्ही कसा वापरू शकता आणि कसा आपल्या पसंतीनुसार बदल करू शकता.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बॉट

तुम्ही खालील प्रॉम्प्ट्स वापरू शकता:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान तपासणी

तापमान संकल्पना काय करते?

1. हे आउटपुट किती रँडम (असहज) आहे ते नियंत्रित करते.
1. हे प्रतिसाद किती मोठा आहे ते नियंत्रित करते.
1. हे किती टोकन वापरले जातात ते नियंत्रित करते.

## 🚀 आव्हान

असाइनमेंटवर काम करताना, तापमान वेगवेगळे करून पहा, त्याला 0, 0.5, आणि 1 असे सेट करून पहा. लक्षात ठेवा की 0 सर्वात कमी विविधतेचे आणि 1 सर्वाधिक विविधतेचे आहे. तुमच्या अॅपसाठी कोणते मूल्य सर्वोत्तम कार्य करते?

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमचा [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पाहा आणि तुमच्या Generative AI ज्ञानाला पुढे वाढवा!

पुढे जा धडा 7 कडे जिथे आपण [चॅट अँप्लिकेशन्स कसे तयार करायचे](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ते पाहू!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->