<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:51:43+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "mr"
}
-->
# टेक्स्ट जनरेशन अॅप्लिकेशन्स तयार करणे

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.mr.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(वरील प्रतिमा क्लिक करून या धड्याचा व्हिडिओ पाहा)_

या अभ्यासक्रमादरम्यान तुम्ही पाहिलं आहे की प्रॉम्प्टसारख्या मूलभूत संकल्पना आहेत आणि "प्रॉम्प्ट इंजिनिअरिंग" नावाचं एक संपूर्ण क्षेत्रही आहे. ChatGPT, Office 365, Microsoft Power Platform आणि इतर अनेक टूल्स तुम्हाला प्रॉम्प्ट वापरून काही साध्य करण्यास मदत करतात.

तुम्हाला अशा अनुभवाला अॅपमध्ये समाविष्ट करायचं असल्यास, प्रॉम्प्ट, पूर्णता (completions) यांसारख्या संकल्पना समजून घेणं आणि कामासाठी योग्य लायब्ररी निवडणं आवश्यक आहे. हेच तुम्ही या प्रकरणात शिकणार आहात.

## परिचय

या प्रकरणात, तुम्ही:

- openai लायब्ररी आणि तिच्या मूलभूत संकल्पनांबद्दल शिकाल.
- openai वापरून टेक्स्ट जनरेशन अॅप तयार कराल.
- प्रॉम्प्ट, तापमान (temperature), टोकन्स यांसारख्या संकल्पनांचा वापर करून टेक्स्ट जनरेशन अॅप कसा तयार करायचा हे समजून घ्याल.

## शिकण्याचे उद्दिष्ट

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- टेक्स्ट जनरेशन अॅप म्हणजे काय ते समजावून सांगू शकता.
- openai वापरून टेक्स्ट जनरेशन अॅप तयार करू शकता.
- तुमच्या अॅपमध्ये टोकन्सची संख्या कमी-जास्त करण्यासाठी आणि तापमान बदलण्यासाठी कॉन्फिगर करू शकता, ज्यामुळे वेगवेगळा आउटपुट मिळेल.

## टेक्स्ट जनरेशन अॅप म्हणजे काय?

सामान्यतः जेव्हा तुम्ही अॅप तयार करता, तेव्हा त्यात काही प्रकारचा इंटरफेस असतो, जसे:

- कमांड-आधारित. कन्सोल अॅप्स अशा प्रकारचे असतात जिथे तुम्ही कमांड टाइप करता आणि ती काम पूर्ण करते. उदाहरणार्थ, `git` हा कमांड-आधारित अॅप आहे.
- युजर इंटरफेस (UI). काही अॅप्समध्ये ग्राफिकल युजर इंटरफेस (GUI) असतो जिथे तुम्ही बटणे क्लिक करता, टेक्स्ट इनपुट करता, पर्याय निवडता इत्यादी.

### कन्सोल आणि UI अॅप्सची मर्यादा

कमांड-आधारित अॅपशी तुलना करा जिथे तुम्ही कमांड टाइप करता:

- **मर्यादित आहे**. तुम्ही कोणतीही कमांड टाइप करू शकत नाही, फक्त तीच जी अॅप सपोर्ट करते.
- **भाषा-विशिष्ट**. काही अॅप्स अनेक भाषा सपोर्ट करतात, पण डीफॉल्टने अॅप विशिष्ट भाषेसाठी तयार केलेला असतो, जरी तुम्ही अधिक भाषा सपोर्ट जोडू शकता.

### टेक्स्ट जनरेशन अॅप्सचे फायदे

तर टेक्स्ट जनरेशन अॅप कसा वेगळा आहे?

टेक्स्ट जनरेशन अॅपमध्ये तुम्हाला अधिक लवचिकता असते, तुम्ही कमांड्सच्या सेट किंवा विशिष्ट इनपुट भाषेपुरते मर्यादित नसता. त्याऐवजी, तुम्ही नैसर्गिक भाषा वापरून अॅपशी संवाद साधू शकता. आणखी एक फायदा म्हणजे तुम्ही आधीच अशा डेटासोर्सशी संवाद साधत आहात ज्यावर मोठ्या प्रमाणात माहितीचा प्रशिक्षण दिलेला आहे, तर पारंपरिक अॅप डेटाबेसमध्ये असलेल्या माहितीपुरते मर्यादित असू शकतो.

### टेक्स्ट जनरेशन अॅपने काय तयार करू शकतो?

तुम्ही अनेक गोष्टी तयार करू शकता. उदाहरणार्थ:

- **चॅटबॉट**. तुमच्या कंपनी आणि तिच्या उत्पादनांबद्दल प्रश्नांची उत्तरे देणारा चॅटबॉट चांगला पर्याय असू शकतो.
- **सहायक**. LLMs सारखे मॉडेल्स टेक्स्ट सारांशित करणे, माहिती मिळवणे, रेज्युमे सारखा टेक्स्ट तयार करणे यांसारख्या कामांसाठी उपयुक्त आहेत.
- **कोड सहाय्यक**. तुम्ही वापरत असलेल्या भाषा मॉडेलवर अवलंबून, तुम्ही कोड लिहिण्यास मदत करणारा कोड सहाय्यक तयार करू शकता. उदाहरणार्थ, GitHub Copilot किंवा ChatGPT वापरून कोड लिहिण्यात मदत मिळू शकते.

## सुरुवात कशी करावी?

तुम्हाला LLM शी कनेक्ट होण्याचा मार्ग शोधावा लागेल, जो सहसा खालील दोन पद्धतींपैकी एक असतो:

- API वापरा. येथे तुम्ही तुमचा प्रॉम्प्ट वापरून वेब विनंत्या तयार करता आणि जनरेट केलेला टेक्स्ट परत मिळवता.
- लायब्ररी वापरा. लायब्ररी API कॉल्सला समेटून त्यांचा वापर सोपा करतात.

## लायब्ररीज/SDKs

LLMs सोबत काम करण्यासाठी काही प्रसिद्ध लायब्ररीज आहेत जसे:

- **openai**, ही लायब्ररी तुमच्या मॉडेलशी कनेक्ट होणे आणि प्रॉम्प्ट पाठवणे सोपे करते.

त्याचबरोबर उच्च स्तरावर काम करणाऱ्या लायब्ररीज आहेत जसे:

- **Langchain**. Langchain प्रसिद्ध आहे आणि Python ला सपोर्ट करते.
- **Semantic Kernel**. Semantic Kernel ही Microsoft ची लायब्ररी आहे जी C#, Python, आणि Java भाषा सपोर्ट करते.

## openai वापरून पहिला अॅप

चला पाहूया की आपला पहिला अॅप कसा तयार करायचा, कोणत्या लायब्ररीजची गरज आहे, किती आवश्यक आहे इत्यादी.

### openai इन्स्टॉल करा

OpenAI किंवा Azure OpenAI शी संवाद साधण्यासाठी अनेक लायब्ररीज उपलब्ध आहेत. तुम्ही C#, Python, JavaScript, Java आणि इतर अनेक प्रोग्रामिंग भाषा वापरू शकता. आम्ही `openai` Python लायब्ररी वापरण्याचा निर्णय घेतला आहे, त्यामुळे `pip` वापरून ती इन्स्टॉल करू.

```bash
pip install openai
```

### रिसोर्स तयार करा

खालील पावले पार पाडा:

- Azure वर खाते तयार करा [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI साठी प्रवेश मिळवा. येथे जा [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) आणि प्रवेशासाठी विनंती करा.

  > [!NOTE]
  > लेखनाच्या वेळी, Azure OpenAI साठी प्रवेशासाठी अर्ज करणे आवश्यक आहे.

- Python इन्स्टॉल करा <https://www.python.org/>
- Azure OpenAI Service रिसोर्स तयार करा. कसे तयार करायचे ते पाहण्यासाठी हा मार्गदर्शक पहा [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API की आणि एंडपॉइंट शोधा

आता तुम्हाला `openai` लायब्ररीला कोणती API की वापरायची ते सांगायचं आहे. तुमची API की शोधण्यासाठी, Azure OpenAI रिसोर्सच्या "Keys and Endpoint" विभागात जा आणि "Key 1" ची कॉपी करा.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

आता ही माहिती कॉपी केल्यावर, लायब्ररीजना ती वापरण्यास सांगा.

> [!NOTE]
> तुमची API की कोडपासून वेगळी ठेवणं चांगलं. तुम्ही हे पर्यावरणीय चल (environment variables) वापरून करू शकता.
>
> - पर्यावरणीय चल `OPENAI_API_KEY` तुमच्या API कीसाठी सेट करा.
>   `export OPENAI_API_KEY='sk-...'`

### Azure कॉन्फिगरेशन सेटअप करा

जर तुम्ही Azure OpenAI वापरत असाल, तर कॉन्फिगरेशन सेटअप कसं करायचं ते खालीलप्रमाणे:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

वरील कोडमध्ये आम्ही खालील सेट करत आहोत:

- `api_type` ला `azure` सेट करत आहोत. यामुळे लायब्ररी Azure OpenAI वापरेल, OpenAI नाही.
- `api_key`, ही तुमची Azure Portal मधील API की आहे.
- `api_version`, तुम्हाला वापरायची API ची आवृत्ती. लेखनाच्या वेळी, नवीनतम आवृत्ती `2023-05-15` आहे.
- `api_base`, API चा एंडपॉइंट. तुम्ही Azure Portal मध्ये तुमच्या API कीजवळ हे पाहू शकता.

> [!NOTE] > `os.getenv` ही एक फंक्शन आहे जी पर्यावरणीय चल वाचते. तुम्ही याचा वापर `OPENAI_API_KEY` आणि `API_BASE` सारखे पर्यावरणीय चल वाचण्यासाठी करू शकता. टर्मिनलमध्ये किंवा `dotenv` सारखी लायब्ररी वापरून हे सेट करा.

## टेक्स्ट जनरेट करा

टेक्स्ट जनरेट करण्यासाठी `Completion` क्लास वापरतात. उदाहरण:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

वरील कोडमध्ये, आम्ही एक completion ऑब्जेक्ट तयार करतो आणि वापरायचा मॉडेल व प्रॉम्प्ट देतो. नंतर जनरेट केलेला टेक्स्ट प्रिंट करतो.

### चॅट पूर्णता (Chat completions)

आत्तापर्यंत तुम्ही `Completion` वापरून टेक्स्ट जनरेट कसा करायचा पाहिला आहे. पण `ChatCompletion` नावाचा आणखी एक क्लास आहे जो चॅटबॉटसाठी अधिक योग्य आहे. वापराचं उदाहरण:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

या फंक्शनॅलिटीबद्दल पुढील प्रकरणात अधिक माहिती मिळेल.

## सराव - तुमचा पहिला टेक्स्ट जनरेशन अॅप

आता आपण openai सेटअप आणि कॉन्फिगर कसा करायचा ते शिकलो, तुमचा पहिला टेक्स्ट जनरेशन अॅप तयार करण्याची वेळ आली आहे. अॅप तयार करण्यासाठी खालील पावले पाळा:

1. वर्चुअल एन्व्हायर्नमेंट तयार करा आणि openai इन्स्टॉल करा:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows वापरत असाल तर `source venv/bin/activate` ऐवजी `venv\Scripts\activate` टाइप करा.

   > [!NOTE]
   > तुमची Azure OpenAI की शोधण्यासाठी [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) येथे जा, `Open AI` शोधा, `Open AI resource` निवडा, नंतर `Keys and Endpoint` मध्ये जाऊन `Key 1` कॉपी करा.

1. _app.py_ नावाचा फाइल तयार करा आणि खालील कोड द्या:

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
   > Azure OpenAI वापरत असाल तर `api_type` ला `azure` सेट करा आणि `api_key` तुमची Azure OpenAI की द्या.

   तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## वेगवेगळ्या प्रकारचे प्रॉम्प्ट्स, वेगवेगळ्या कामांसाठी

आता तुम्ही पाहिलं की प्रॉम्प्ट वापरून टेक्स्ट कसा जनरेट करायचा. तुमच्याकडे एक प्रोग्राम आहे ज्याला तुम्ही बदलून वेगवेगळ्या प्रकारचा टेक्स्ट तयार करू शकता.

प्रॉम्प्ट्स विविध कामांसाठी वापरले जाऊ शकतात. उदाहरणार्थ:

- **टेक्स्टचा प्रकार तयार करा**. उदाहरणार्थ, कविता, क्विझसाठी प्रश्न इत्यादी.
- **माहिती शोधा**. तुम्ही प्रॉम्प्ट वापरून माहिती शोधू शकता, जसे 'वेब डेव्हलपमेंटमध्ये CORS म्हणजे काय?'.
- **कोड जनरेट करा**. प्रॉम्प्ट वापरून कोड तयार करू शकता, जसे ईमेल तपासण्यासाठी रेग्युलर एक्स्प्रेशन तयार करणे किंवा संपूर्ण वेब अॅप तयार करणे.

## अधिक व्यावहारिक वापर: रेसिपी जनरेटर

कल्पना करा की तुमच्याकडे घरात काही साहित्य आहे आणि तुम्हाला काहीतरी स्वयंपाक करायचा आहे. त्यासाठी तुम्हाला रेसिपी पाहिजे. रेसिपी शोधण्यासाठी तुम्ही सर्च इंजिन वापरू शकता किंवा LLM वापरू शकता.

तुम्ही असा प्रॉम्प्ट लिहू शकता:

> "खालील साहित्य वापरून ५ रेसिपी दाखवा: चिकन, बटाटे, आणि गाजर. प्रत्येक रेसिपीसाठी वापरलेले सर्व साहित्य यादी करा."

वरील प्रॉम्प्ट दिल्यावर, तुम्हाला खालीलप्रमाणे उत्तर मिळू शकते:

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

हा परिणाम छान आहे, मला काय बनवायचं ते कळलं. आता पुढील सुधारणा उपयुक्त ठरू शकतात:

- मला नको असलेले किंवा ज्यांना मला अॅलर्जी आहे अशा साहित्याला फिल्टर करणे.
- जर काही साहित्य घरात नसेल तर खरेदीची यादी तयार करणे.

वरील बाबींसाठी, एक अतिरिक्त प्रॉम्प्ट जोडा:

> "कृपया लसूण असलेल्या रेसिपी काढून टाका कारण मला त्याला अॅलर्जी आहे आणि त्याऐवजी काहीतरी दुसरे द्या. तसेच, रेसिपींसाठी खरेदीची यादी तयार करा, लक्षात ठेवा की माझ्याकडे आधीच चिकन, बटाटे आणि गाजर आहेत."

आता तुम्हाला नवीन निकाल मिळेल, म्हणजे:

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

ही तुमची पाच रेसिपी आहेत, ज्यात लसूण नाही आणि तुमच्याकडे आधीच जे साहित्य आहे त्यानुसार खरेदीची यादीही आहे.

## सराव - रेसिपी जनरेटर तयार करा

आता आपण एक उदाहरण पाहिलं आहे, त्यानुसार कोड लिहूया. खालील पावले पाळा:

1. आधीचा _app.py_ फाइल वापरा.
1. `prompt` व्हेरिएबल शोधा आणि त्याचा कोड खालीलप्रमाणे बदला:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   आता कोड चालवल्यास, तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, तुमचा LLM नॉन-डिटर्मिनिस्टिक आहे, त्यामुळे प्रत्येक वेळी वेगळे निकाल मिळू शकतात.

छान, आता सुधारणा कशी करायची ते पाहूया. सुधारणा करण्यासाठी, कोड लवचिक असावा म्हणजे साहित्य आणि रेसिपींची संख्या बदलता येईल.

1. कोड खालीलप्रमाणे बदला:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   टेस्ट रनसाठी कोड असे दिसू शकतो:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर आणि खरेदी यादी जोडून सुधारणा करा

आता आपल्याकडे एक काम करणारा अॅप आहे जो रेसिपी तयार करू शकतो आणि वापरकर्त्याच्या इनपुटवर आधारित लवचिक आहे, रेसिपींची संख्या आणि साहित्य दोन्ही बदलता येतात.

अधिक सुधारण्यासाठी, खालील गोष्टी जोडूया:

- **साहित्य फिल्टर करा**. आपल्याला नको असलेले किंवा ज्यांना अॅलर्जी आहे असे साहित्य फिल्टर करता यावे. यासाठी, आपल्या प्रॉम्प्टमध्ये शेवटी फिल्टरची अट जोडू शकतो:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  वर `{filter}` प्रॉम्प्टच्या शेवटी जोडले आहे आणि वापरकर्त्यांकडून फिल्टर मूल्य घेतले आहे.

  प्रोग्राम चालवताना उदाहरण इनपुट असे दिसू शकते:

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

  जसे तुम्ही पाहू शकता, ज्यात दूध आहे अशा रेसिपी फिल्टर केल्या आहेत. पण जर तुम्हाला लॅक्टोज इन्टॉलरंट असाल तर कदाचित चीज असलेल्या रेसिपीही फिल्टर करायच्या असतील, त्यामुळे स्पष्ट असणे आवश्यक आहे.

- **खरेदी यादी तयार करा**. आपल्याकडे आधीच जे साहित्य आहे त्यानुसार खरेदी यादी तयार करायची आहे.

  यासाठी, आपण एकाच प्रॉम्प्टमध्ये सर्व काही करण्याचा प्रयत्न करू शकतो किंवा दोन प्रॉम्प्ट्समध्ये विभागू शकतो. दुसऱ्या पद्धतीचा प्रयत्न करूया. येथे आपण अतिरिक्त प्रॉम्प्ट जोडण्याचा प्रस्ताव देत आहोत, पण त्यासाठी पहिल्या प्रॉम्प्टचा निकाल दुसऱ्या प्रॉम्प्टसाठी संदर्भ म्हणून जोडावा लागेल.

  कोडमध्ये पहिल्या प्रॉम्प्टचा निकाल प्रिंट होणाऱ्या भागाजवळ खालील कोड जोडा:

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

  लक्षात ठेवा:

  1. आम्ही नवीन प्रॉम्प्ट तयार करत आहोत ज्यात पहिल्या प्रॉम्प्टचा निकाल जोडला आहे:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. आपण नवीन विनंती करतो, पण पहिल्या प्रॉम्प्टमध्ये विचारलेल्या टोकन्सच्या संख्येचा देखील विचार करतो, त्यामुळे यावेळी आपण `max_tokens` 1200 असे सेट करतो.

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

हा कोड वापरून, आपल्याला खालील आउटपुट मिळते:

```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## तुमचे सेटअप सुधारित करा

आत्तापर्यंत आपल्याकडे काम करणारा कोड आहे, पण अजून सुधारणा करण्यासाठी काही बदल करणे आवश्यक आहे. काही गोष्टी ज्या आपण करायला हव्यात त्या आहेत:

- **कोडपासून गुपिते वेगळी ठेवा**, जसे की API की. गुपिते कोडमध्ये नसावीत आणि सुरक्षित ठिकाणी साठवली पाहिजेत. गुपिते कोडपासून वेगळी करण्यासाठी आपण environment variables आणि `python-dotenv` सारख्या लायब्ररींचा वापर करू शकतो ज्यामुळे ती फाइलमधून लोड करता येतात. कोडमध्ये ते कसे दिसेल ते खालीलप्रमाणे:

  1. `.env` नावाची फाइल तयार करा आणि त्यात खालील सामग्री ठेवा:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> लक्षात ठेवा, Azure साठी खालील environment variables सेट करणे आवश्यक आहे:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     कोडमध्ये environment variables असे लोड करता येतात:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **टोकन लांबीबाबत एक शब्द**. आपल्याला हवे असलेले टेक्स्ट तयार करण्यासाठी किती टोकन्स लागतील हे विचारात घ्यावे. टोकन्स वापरण्यास पैसे लागतात, त्यामुळे शक्य तितके टोकन्स कमी वापरण्याचा प्रयत्न करा. उदाहरणार्थ, आपण प्रॉम्प्ट असे कसे मांडू शकतो जेणेकरून कमी टोकन्स वापरता येतील?

  टोकन्स बदलण्यासाठी, `max_tokens` पॅरामीटर वापरू शकता. उदाहरणार्थ, 100 टोकन्स वापरायचे असल्यास:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **temperature सोबत प्रयोग करणे**. temperature हा एक महत्त्वाचा घटक आहे ज्याचा आपण आतापर्यंत उल्लेख केला नाही, पण तो आपल्या प्रोग्रामच्या कामगिरीसाठी महत्त्वाचा आहे. temperature जास्त असल्यास आउटपुट अधिक अनियमित (random) होतो. उलट temperature कमी असल्यास आउटपुट अधिक ठराविक (predictable) असतो. तुम्हाला आउटपुटमध्ये विविधता हवी आहे की नाही हे विचार करा.

  temperature बदलण्यासाठी, `temperature` पॅरामीटर वापरा. उदाहरणार्थ, temperature 0.5 वापरायचा असल्यास:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > लक्षात ठेवा, 1.0 जवळील मूल्य अधिक विविधता दर्शवते.

## असाइनमेंट

या असाइनमेंटसाठी, तुम्ही काय तयार करायचे ते निवडू शकता.

काही सूचना:

- रेसिपी जनरेटर अॅपमध्ये सुधारणा करा. temperature मूल्ये आणि प्रॉम्प्ट्ससह प्रयोग करा आणि काय तयार होते ते पाहा.
- "स्टडी बडी" तयार करा. हा अॅप एखाद्या विषयाबाबत प्रश्नांची उत्तरे देऊ शकेल, उदाहरणार्थ Python. तुम्ही प्रॉम्प्ट्स वापरू शकता जसे "Python मधील एखादा विषय काय आहे?", किंवा "एखाद्या विषयासाठी कोड दाखवा" असे.
- इतिहास बॉट तयार करा, इतिहास जिवंत करा, बॉटला एखाद्या ऐतिहासिक व्यक्तीची भूमिका बजावण्यास सांगा आणि त्याच्या जीवनाबाबत प्रश्न विचारा.

## सोल्यूशन

### स्टडी बडी

खाली एक प्रारंभिक प्रॉम्प्ट दिला आहे, पाहा तुम्ही त्याचा कसा वापर करू शकता आणि तुमच्या आवडीनुसार कसा बदल करू शकता.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बॉट

खाली काही प्रॉम्प्ट्स आहेत जे तुम्ही वापरू शकता:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान तपासणी

temperature संकल्पना काय करते?

1. आउटपुट किती अनियमित आहे हे नियंत्रित करते.
1. प्रतिसाद किती मोठा आहे हे नियंत्रित करते.
1. किती टोकन्स वापरले जातात हे नियंत्रित करते.

## 🚀 आव्हान

असाइनमेंट करताना temperature बदलून पाहा, 0, 0.5, आणि 1 असे सेट करा. लक्षात ठेवा की 0 म्हणजे सर्वात कमी विविधता आणि 1 म्हणजे सर्वात जास्त. तुमच्या अॅपसाठी कोणते मूल्य सर्वोत्तम काम करते?

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) मध्ये भेट द्या आणि तुमचे Generative AI ज्ञान अधिक वाढवा!

पुढील धडा 7 मध्ये चला जिथे आपण [चॅट अॅप्लिकेशन्स कसे तयार करायचे](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ते पाहणार आहोत!

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.