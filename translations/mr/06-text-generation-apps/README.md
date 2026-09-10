# मजकूर निर्मिती अनुप्रयोग तयार करणे

[![मजकूर निर्मिती अनुप्रयोग तयार करणे](../../../translated_images/mr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(हा पाठाचा व्हिडिओ पाहण्यासाठी वरील प्रतिमा क्लिक करा)_

तूम्ही आतापर्यंत या अभ्यासक्रमाद्वारे पाहिले आहे की प्रॉम्प्टसारखे मूलभूत संकल्पना आहेत आणि अगदी "प्रॉम्प्ट अभियांत्रिकी" नावाचा एक पूर्ण विषयसुद्धा आहे. ChatGPT, Office 365, Microsoft Power Platform आणि बरेच अन्य उपकरणे जी तुम्ही संवाद साधू शकता, ते प्रॉम्प्ट वापरून काहीतरी साध्य करण्यात तुमची मदत करतात.

अशा अनुभवाला अनुप्रयोगात जोडण्यासाठी, तुम्हाला प्रॉम्प्ट, पूर्णता यांसारख्या संकल्पना समजून घ्याव्या लागतात आणि काम करण्यासाठी एखादं पुस्तकालय (library) निवडावं लागतं. हाच तुम्ही या प्रकरणात शिकणार आहात.

## परिचय

या प्रकरणात, तुम्ही:

- openai पुस्तकालय आणि त्याच्या मूलभूत संकल्पना जाणून घ्याल.
- openai वापरून मजकूर निर्मितीचा अनुप्रयोग तयार कराल.
- मजकूर निर्मितीचा अनुप्रयोग तयार करण्यासाठी प्रॉम्प्ट, तापमान, आणि टोकन्स यांसारख्या संकल्पना कशा वापरायच्या ते समजून घ्याल.

## शिकण्याच्या उद्दिष्टे

या पाठाच्या शेवटी, तुम्ही करू शकाल:

- मजकूर निर्मितीचा अनुप्रयोग म्हणजे काय ते समजावून सांगा.
- openai वापरून मजकूर निर्मितीचा अनुप्रयोग तयार करा.
- तुमचा अनुप्रयोग अधिक किंवा कमी टोकन्स वापरण्यासाठी आणि विविध आउटपुटसाठी तापमान बदलण्यास सुसज्ज करा.

## मजकूर निर्मितीचा अनुप्रयोग म्हणजे काय?

सामान्यतः जेव्हा तुम्ही एखादा अनुप्रयोग बनवता तेव्हा त्याला खालील प्रकारचे काहीतरी इंटरफेस असतो:

- आदेशावर आधारित. कन्सोल अनुप्रयोग हे पारंपारिक अनुप्रयोग आहेत जिथे तुम्ही आदेश टाइप करता आणि तो एखादा कार्य पार पाडतो. उदाहरणार्थ, `git` हा आदेश आधारित अनुप्रयोग आहे.
- वापरकर्ता इंटरफेस (UI). काही अनुप्रयोगांमध्ये ग्राफिकल वापरकर्ता इंटरफेस (GUI) असतो जिथे तुम्ही बटणे क्लिक करता, मजकूर टाकता, पर्याय निवडता आणि बरेच काही करता येते.

### कन्सोल आणि UI अनुप्रयोग मर्यादित असतात

त्याची तुलना एक आदेश आधारित अनुप्रयोगाशी करा जिथे तुम्ही आदेश टाइप करता:

- **तो मर्यादित आहे**. तुम्ही फक्त अनुप्रयोग समर्थन करणारेच आदेश टाइप करू शकता.
- **भाषा विशेष**. काही अनुप्रयोग अनेक भाषा समर्थन करतात, पण पूर्वनिर्धारितरित्या अनुप्रयोग विशिष्ट भाषेसाठी बनवलेला असतो, जरी तुम्ही अधिक भाषा समर्थन जोडू शकता.

### मजकूर निर्मिती अनुप्रयोगांचे फायदे

तर मजकूर निर्मितीचा अनुप्रयोग कसा वेगळा आहे?

मजकूर निर्मिती अनुप्रयोगात तुम्हाला अधिक लवचिकता असते, तुम्ही आदेशांच्या संचाशी किंवा विशिष्ट इनपुट भाषेशी मर्यादित नाही असता. त्याऐवजी, तुम्ही अनुप्रयोगाशी संवाद साधण्यासाठी नैसर्गिक भाषा वापरू शकता. आणखी एक फायदा म्हणजे तुम्ही आधीच असे डेटास्रोत वापरत आहात ज्याला मोठ्या माहितीच्या संग्रहावर प्रशिक्षण दिले गेले आहे, जिथे पारंपारिक अनुप्रयोग डेटाबेसमधील मर्यादित माहितीवर अवलंबून असू शकतात.

### मजकूर निर्मिती अनुप्रयोग वापरून काय तयार करू शकतो?

तुम्ही बरेच काही तयार करू शकता. उदाहरणार्थ:

- **चॅटबॉट**. कंपनी आणि तिच्या उत्पादनांबद्दल प्रश्नांची उत्तरे देणारा चॅटबॉट चांगला पर्याय ठरू शकतो.
- **सहायक**. LLMs सारखी भाषा मॉडेल्स मजकूर संक्षेप, मजकूरातून अंतर्दृष्टी घेणे, रेस्यूमे तयार करणे यांसारख्या गोष्टींमध्ये उत्कृष्ट आहेत.
- **कोड सहाय्यक**. तुम्ही वापरत असलेल्या भाषा मॉडेलनुसार, तुम्ही कोड लिहिण्यास मदत करणारा कोड सहाय्यक तयार करू शकता. उदाहरणार्थ, तुम्ही GitHub Copilot किंवा ChatGPT सारख्या उत्पादनांचा वापर करून कोड लिहिण्यात मदत घेऊ शकता.

## मी कसे सुरुवात करू शकतो?

साधारणपणे, तुम्हाला LLM सह एकत्रिकरण करण्याचा मार्ग शोधावा लागतो जो सहसा खालील दोन पध्दतींनी होतो:

- API वापरा. येथे तुम्ही तुमचा प्रॉम्प्ट वापरून वेब विनंत्या तयार करता आणि निर्मित मजकूर परत मिळतो.
- पुस्तकालय वापरा. पुस्तकालय API कॉल्स सुलभपणे कॅप्सुलेट करतात आणि वापरण्यास सोपे करतात.

## पुस्तकालये/SDKs

LLM सह काम करण्यासाठी काही प्रसिद्ध पुस्तकालये आहेत जसे:

- **openai**, हे पुस्तकालय तुमच्या मॉडेलशी जोडणे आणि प्रॉम्प्ट पाठवणे सोपे करते.

त्यानंतर आहेत उच्च स्तरावर काम करणारी पुस्तकालये जसे:

- **Langchain**. Langchain प्रसिद्ध असून Python ला समर्थन देतो.
- **Semantic Kernel**. Semantic Kernel ही मायक्रोसॉफ्टची एक पुस्तकालय आहे जी C#, Python, आणि Java भाषा समर्थित करते.

## openai वापरून प्रथम अनुप्रयोग

चला पाहूया, आपण आपला पहिला अनुप्रयोग कसा तयार करु, कोणती पुस्तकालये लागतात, किती आवश्यक आहे इत्यादी.

### openai प्रतिष्ठापित करा

OpenAI किंवा Azure OpenAI सह संवाद करण्यासाठी अनेक पुस्तकालये उपलब्ध आहेत. C#, Python, JavaScript, Java तसेच अनेक प्रोग्रामिंग भाषा वापरणे शक्य आहे. आम्ही `openai` Python पुस्तकालय वापरण्याचा निर्णय घेतला आहे, त्यामुळे `pip` वापरून ते स्थापित करू.

```bash
pip install openai
```

### संसाधन तयार करा

तुम्हाला खालील चरण पार पाडावे लागतील:

- Azure वर खाते तयार करा [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI मध्ये प्रवेश मिळवा. येथे जा [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) आणि प्रवेशासाठी विनंती करा.

  > [!NOTE]
  > लिहित असताना, तुम्हाला Azure OpenAI साठी प्रवेशासाठी अर्ज करावा लागतो.

- Python स्थापित करा <https://www.python.org/>
- Azure OpenAI सेवा संसाधन तयार केले आहे. संसाधन कसे तयार करायचे ह्याबाबत मार्गदर्शक पाहा [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API की आणि एंडपॉइंट शोधा

आता, तुम्हाला तुमच्या `openai` पुस्तकालयाला कोणती API की वापरायची ते सांगायचे आहे. तुमची API की शोधण्यासाठी, तुमच्या Azure OpenAI संसाधनाच्या "Keys and Endpoint" विभागाकडे जा आणि "Key 1" मूल्य कॉपी करा.

![Azure Portal मधील Keys and Endpoint संसाधन ब्लेड](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

आता ही माहिती कॉपी केल्यानंतर, पुस्तकालयांना याचा वापर करण्यास निर्देश देऊया.

> [!NOTE]
> तुमची API की तुमच्या कोडपासून वेगळी ठेवणे योग्य आहे. तुम्ही पर्यावरण चल (environment variables) वापरून हे करू शकता.
>
> - पर्यावरण चल `OPENAI_API_KEY` तुमच्या API कीसाठी सेट करा.
>   `export OPENAI_API_KEY='sk-...'`

### Azure कॉन्फिगरेशन सेटअप करा

जर तुम्ही Azure OpenAI (आता Microsoft Foundry चा भाग) वापरत असाल, तर कॉन्फिगरेशन कसे सेट करायचे ते येथे आहे. आम्ही स्टँडर्ड `OpenAI` क्लायंट वापरतो जो Azure OpenAI च्या `/openai/v1/` एंडपॉइंटकडे निर्देशित आहे, जो Responses API सोबत कार्य करतो आणि `api_version` ची गरज नाही:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

वर आम्ही खालील सेट करत आहोत:

- `api_key`, हे तुमची API की आहे जी Azure Portal किंवा Microsoft Foundry पोर्टलमध्ये आढळते.
- `base_url`, हे तुमच्या Foundry संसाधनाचा एंडपॉइंट आहे ज्यामध्ये `/openai/v1/` जोडले आहे. स्थिर v1 एंडपॉइंट OpenAI आणि Azure OpenAI या दोन्हीशी कार्य करतो आणि `api_version` व्यवस्थापनाची गरज नाही.

> [!NOTE] > `os.environ` पर्यावरण चल वाचते. तुम्ही त्याचा वापर `AZURE_OPENAI_API_KEY` आणि `AZURE_OPENAI_ENDPOINT` सारखे पर्यावरण चल वाचण्यासाठी करू शकता. टर्मिनलमध्ये किंवा `dotenv` सारख्या पुस्तकालयाचा वापर करून हे सेट करा.

## मजकूर निर्माण करा

मजकूर निर्माण करण्याचा मार्ग म्हणजे Responses API चा `responses.create` पद्धतीद्वारे वापर करणे. उदाहरण:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # हे तुमचे मॉडेल डिप्लॉयमेंट नाव आहे
    input=prompt,
    store=False,
)
print(response.output_text)
```

वरचा कोडमध्ये, आम्ही एक प्रतिसाद तयार करतो आणि वापरायचा मॉडेल आणि प्रॉम्प्ट देतो. नंतर `response.output_text` द्वारे तयार झालेला मजकूर छापतो.

### मल्टी-टर्न संभाषणे

Responses API एकट्या-turn मजकूर निर्मिती आणि मल्टी-टर्न चॅटबॉट्ससाठी योग्य आहे - तुम्ही `input` मध्ये संदेशांची यादी देऊन संभाषण तयार करता:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

या कार्यक्षमतेवर पुढील प्रकरणात अधिक माहिती दिली जाईल.

## व्यायाम - तुमचा पहिला मजकूर निर्मितीचा अनुप्रयोग

आता आपण openai कसे सेटअप आणि कॉन्फिगर करायचे ते शिकलो, तुमचा पहिला मजकूर निर्मितीचा अनुप्रयोग तयार करण्याची वेळ आली आहे. अनुप्रयोग तयार करण्यासाठी खालील चरणांचे पालन करा:

1. एक आभासी वातावरण (virtual environment) तयार करा आणि openai स्थापित करा:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows वापरत असल्यास `source venv/bin/activate` च्या ऐवजी `venv\Scripts\activate` टाइप करा.

   > [!NOTE]
   > तुमची Azure OpenAI की शोधण्यासाठी [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) येथे जा, `Open AI` शोधा, `Open AI resource` निवडा, नंतर `Keys and Endpoint` येथे जाऊन `Key 1` मूल्य कॉपी करा.

1. _app.py_ नावाची फाइल तयार करा आणि त्यात खालील कोड द्या:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # तुमचा पूर्ण करण्याचा कोड जोडा
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API वापरून विनंती करा
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिसाद छापा
   print(response.output_text)
   ```

   > [!NOTE]
   > जर तुम्ही फक्त OpenAI (Azure नाही) वापरत असाल, तर `client = OpenAI(api_key="<replace this value with your OpenAI key>")` वापरा (`base_url` नाही) आणि डिप्लॉयमेंट नावाऐवजी `gpt-5-mini` सारखा मॉडेल नाव द्या.

   तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## वेगवेगळ्या प्रकारचे प्रॉम्प्ट, वेगवेगळ्या कामांसाठी

आता तुम्ही प्रॉम्प्ट वापरून मजकूर कसा तयार करायचा ते पाहिले आहे. तुमच्याकडे एक चालू असलेला प्रोग्राम आहे ज्याला तुम्ही वेगवेगळ्या प्रकारचे मजकूर तयार करण्यासाठी बदलू शकता.

प्रॉम्प्ट्स सर्व प्रकारच्या कामांसाठी वापरले जाऊ शकतात. उदाहरणार्थ:

- **काही प्रकारचा मजकूर तयार करा**. उदाहरणार्थ, तुम्ही कविता, क्विझसाठी प्रश्न इत्यादी तयार करू शकता.
- **माहिती शोधा**. तुम्ही प्रॉम्प्ट वापरून खालीलप्रमाणे माहिती शोधू शकता 'वेब डेव्हलपमेंटमध्ये CORS चा अर्थ काय आहे?'.
- **कोड तयार करा**. तुम्ही प्रॉम्प्ट वापरून कोड तयार करू शकता, उदाहरणार्थ ईमेल्स वैध करण्यासाठी रेग्युलर एक्स्प्रेशन तयार करणे किंवा संपूर्ण वेब अनुप्रयोग तयार करणे.

## अधिक व्यावहारिक वापराचा प्रकरण: रेसिपी जनरेटर

समजा तुमच्याकडे घरी साहित्य आहे आणि तुम्हाला काहीतरी स्वयंपाक करायचा आहे. त्यासाठी तुम्हाला रेसिपीची गरज आहे. रेसिपी शोधण्याचा एक मार्ग म्हणजे शोध इंजिन वापरणे किंवा तुम्ही LLM वापरू शकता.

तुम्ही पुढीलप्रमाणे प्रॉम्प्ट लिहू शकता:

> "खालील साहित्याने बनवलेला पदार्थासाठी ५ रेसिपी दाखवा: चिकन, बटाटे, आणि गाजर. प्रत्येक रेसिपीसाठी वापरलेली सर्व साहित्य यादीत करा."

वरील प्रॉम्प्ट दिल्यास, तुम्हाला खालीलप्रमाणे प्रतिसाद मिळू शकतो:

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

हा परिणाम छान आहे, मला काय बनवायचं आहे ते कळलं. या वेळी, उपयोगी सुधारणा काय असू शकतात:

- मला न आवडणारे किंवा ज्यांना मला अ‍ॅलर्जी आहे अशा साहित्यांना फिल्टर करा.
- जर काही साहित्य घरी नसेल तर खरेदीच्या यादी तयार करा.

वरील बाबींसाठी, एक अतिरिक्त प्रॉम्प्ट जोडूया:

> "कृपया लसूण असलेल्या रेसिपी काढून टाका कारण मला त्याला अ‍ॅलर्जी आहे आणि त्याऐवजी काही तरी दुसरे ठेवा. तसेच, चिकन, बटाटे व गाजर आधीच आहेत लक्षात घेऊन खरेदीची यादी तयार करा."

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

हि तुमची ५ रेसिपी आहेत, लसणी नव्हती आणि खरेदी यादीसुद्धा आहे जी आधीच तुमच्याकडे असलेल्या साहित्यानुसार आहे.

## व्यायाम - रेसिपी जनरेटर तयार करा

आता आपणच एक उदाहरण पाहिले, त्या उदाहरणाशी जुळणारा कोड लिहूया. हे करण्यासाठी खालील चरणांचे पालन करा:

1. विद्यमान _app.py_ फाइल वापरा.
1. `prompt` चल शोधा आणि त्याचा कोड खालीलप्रमाणे बदला:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   आता कोड चालविल्यास तुम्हाला असा आउटपुट दिसेल:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > लक्षात घ्या की तुमचा LLM nondeterministic आहे, त्यामुळे प्रोग्राम प्रत्येक वेळेस चालविल्यावर वेगवेगळे निकाल मिळू शकतात.

   छान, आणखी सुधारणा कशी करू शकतो ते पाहूया. सुधारणा करण्यासाठी, आम्हाला कोड लवचीक करायचा आहे, म्हणजे साहित्य आणि रेसिपींची संख्या सहज सुधारता येईल.

1. कोड पुढीलप्रमाणे बदला:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # रेसिपींच्या संख्येला प्रॉम्प्ट आणि साहित्यांमध्ये समाकलित करा
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

### फिल्टर आणि शॉपिंग लिस्ट जोडून सुधारणा करा

आता आमच्याकडे एक कार्यरत अनुप्रयोग आहे जो रेसिपी तयार करू शकतो आणि वापरकर्त्याच्या इनपुटवर आधारित लवचीक आहे, रेसिपींची संख्या आणि साहित्य दोन्ही नियंत्रित करता येतात.

आणखी सुधारणा करण्यासाठी, खालील बाबी जोडूया:

- **साहित्य फिल्टर करा**. आपल्याला ते साहित्य फिल्टर करता यावे जे आपल्याला आवडत नाही किंवा ज्यांना आपल्याला अ‍ॅलर्जी आहे. हे करण्यासाठी आपला विद्यमान प्रॉम्प्ट संपवून खालीलप्रमाणे फिल्टर अटी जोडा:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  वरीलप्रमाणे, आम्ही प्रॉम्प्टच्या शेवटी `{filter}` जोडले आहे आणि वापरकर्त्याकडून फिल्टर मूल्य घेतले आहे.

  प्रोग्राम चालविल्यावर उदाहरण इनपुट असे दिसू शकते:

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

  तुम्हाला दिसेल की ज्यात दूध आहे अशा रेसिपी फिल्टर केल्या आहेत. पण जर तुम्हाला लॅक्टोज असहिष्णुता असेल तर तुम्हाला चीज असलेल्या रेसिपींनाही फिल्टर करायचे असू शकते, म्हणून स्पष्ट असणे गरजेचे आहे.


- **खरेदीची यादी तयार करा**. आपल्याला एक खरेदी यादी तयार करायची आहे, आणि यासाठी घरात आधीपासून काय आहे ते विचारात घ्यायचे आहे.

  या फंक्शनॅलिटीसाठी, आपण एकाच प्रॉम्प्टमध्ये सगळे सोडवण्याचा प्रयत्न करू शकतो किंवा दोन प्रॉम्प्टमध्ये विभाजित करू शकतो. चला दुसऱ्या पद्धतीचा प्रयत्न करूया. येथे आम्ही एक अतिरिक्त प्रॉम्प्ट जोडण्याचा प्रस्ताव देत आहोत, पण ते काम करण्यासाठी, आपल्याला आधीच्या प्रॉम्प्टमधील निकाल पुढील प्रॉम्प्टच्या संदर्भात जोडणे आवश्यक आहे.

  कोडमधील तो भाग शोधा जो पहिल्या प्रॉम्प्टमधून निकाल छापतो आणि खालील कोड त्याखाली जोडा:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया छापा
  print("Shopping list:")
  print(response.output_text)
  ```

  लक्षात ठेवा:

  1. आम्ही नवीन प्रॉम्प्ट तयार करत आहोत ज्यात पहिल्या प्रॉम्प्टमधून निकाल नवीन प्रॉम्प्टमध्ये जोडला आहे:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. आम्ही नवीन विनंती करतो, पण पहिल्या प्रॉम्प्टमध्ये विचारलेल्या टोकन्सच्या संख्येचा विचारही करतो, त्यामुळे यावेळी `max_output_tokens` 1200 असे सांगतो.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     हा कोड वापरून आपल्याला आता खालील आउटपुट मिळते:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## आपली सेटअप सुधारित करा

जे आपल्याकडे आतापर्यंत आहे ते काम करते, पण अजून सुधारणा करण्यासाठी काही फेरफार करायला हवेत. आम्ही कोणते काही सुधारणे करायला हवे:

- **गुपिते कोडपासून वेगळी करा**, जसे की API की. गुपिते कोडमध्ये असू नये आणि सुरक्षित ठिकाणी साठवावी. गुपिते कोडपासून वेगळे करण्यासाठी, आपण एन्व्हायर्नमेंट व्हेरिएबल्स आणि `python-dotenv` सारख्या लायब्ररी वापरू शकतो जे फायलीतून त्यांना लोड करतात. कोडमध्ये हे दिसायला असेल तर असे असेल:

  1. `.env` फाइल तयार करा खालील सामग्रीसह:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > लक्षात ठेवा, Microsoft Foundry मधील Azure OpenAI साठी, खालील एन्व्हायर्नमेंट व्हेरिएबल्स सेट करणे आवश्यक आहे:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमध्ये, आपण एन्व्हायर्नमेंट व्हेरिएबल्स असे लोड करता:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन लांबीवर एक शब्द**. आपल्याला हवे तितके टेक्स्ट तयार करण्यासाठी किती टोकन्स लागतील हे विचारात घ्यायला हवे. टोकन्सला किंमत लागते, त्यामुळे शक्य तितक्या कमी टोकन्स वापरण्याचा प्रयत्न करायला हवा. उदाहरणार्थ, आपण प्रॉम्प्ट इतका लावू शकतो का की कमी टोकन्स लागतील?

  वापरल्या जाणार्‍या टोकन्स बदलण्यासाठी, आपण `max_output_tokens` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर तुम्हाला 100 टोकन्स वापरायचे असतील तर:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **टेम्परेचर वापरून प्रयोग**. टेम्परेचर ही गोष्ट आपण आतापर्यंत उल्लेखलेली नाही पण आपला प्रोग्राम कसा काम करतो यासाठी महत्त्वाची आहे. टेम्परेचरची किंमत जितकी जास्त तितका आउटपुट जास्त यादृच्छिक होतो. उलट, टेम्परेचरची किंमत जितकी कमी तितका आउटपुट जास्त अनुकूलनीय होतो. आपल्याला विविधता हवी आहे की नाही हे विचार करा.

  टेम्परेचर बदलायला, आपण `temperature` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर तुम्हाला 0.5 टेम्परेचर वापरायचा असेल तर:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > लक्षात ठेवा, 1.0 जवळजवळ तसा आउटपुट अधिक वेगवेगळा होतो.

- **तर्कशास्त्र मॉडेल temperature वापरत नाहीत**. हे 2026 मधील एक महत्त्वाचा बदल आहे. Microsoft Foundry वरील सध्याचे, न वापरलेले नाहीसे झालेले मॉडेल म्हणजे **तर्कशास्त्र मॉडेल्स** (GPT-5 कुटुंब, o-सीरीज) - आणि ते **`temperature` किंवा `top_p` वापरत नाहीत** (किंवा `max_tokens`, त्याऐवजी `max_output_tokens` वापरा). जर तुम्ही `gpt-5-mini` ला `temperature` वापरून कॉल केला, तर तुम्हाला "parameter not supported" त्रुटी मिळेल. तर त्यामुळे वरील temperature उदाहरण वापरायचे असल्यास, असे मॉडेल वापरा जे अजून सॅम्पलिंग कंट्रोल्सला समर्थन करतात - उदाहरणार्थ open **Llama** मॉडेल जसे `Llama-3.3-70B-Instruct` [Microsoft Foundry मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मधून, ज्याला Foundry Models / Azure AI Inference endpoint वरून कॉल करता येते (githubmodels-* नमुन्यांप्रमाणेच). GPT-5 सारख्या तर्कशास्त्र मॉडेल्ससाठी आउटपुट वेगळ्या प्रकारे नियंत्रित करतात:
  - **प्रॉम्प्ट इंजिनिअरिंग** - स्पष्ट सूचना, उदाहरणे, आणि रचनेतून आउटपुट (पाठ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) पहा) सॅम्पलिंग नॉब्सचा कार्य करतात.
  - **तर्क नियंत्रण** - तर्कशक्ती प्रयास/वाचाळपणा सारखे पॅरामीटर्स तर्क खोलवर आणि विलंब, खर्च यांच्यात ताळमेळ साधतात.

  थोडक्यात: `temperature`/`top_p` अनेक मॉडेल्सवर (Llama, Mistral, Phi, आणि GPT-4.x कुटुंबावर - जरी GPT-4.x कमी होत आहे) अजूनही वैध आहेत, परंतु प्रवासाचा दिशा म्हणजे GPT-5 सारख्या तर्कशास्त्र मॉडेलवर प्रॉम्प्ट इंजिनिअरिंग + तर्क नियंत्रण.

## कार्य

या कार्यासाठी, तुम्ही काय तयार करायचे ते ठरवू शकता.

येथे काही सूचना आहेत:

- रेसिपी जनरेटर अ‍ॅप अधिक सुधारण्यासाठी त्याचे तापमान मूल्ये आणि प्रॉम्प्ट्ससह प्रयोग करा आणि पाहा काय करता येते.
- "स्टडी बडी" तयार करा. हा अ‍ॅप एखाद्या विषयाबाबत प्रश्नांची उत्तरे देऊ शकेल, उदाहरणार्थ Python, तुम्ही असे प्रॉम्प्ट वापरू शकता "Python मधील एखादा विशिष्ट विषय काय आहे?" किंवा "त्याबाबत कोड दाखवा" असे.
- इतिहास बोट तयार करा, इतिहास जिवंत करा, बोटला एखाद्या ऐतिहासिक व्यक्तीची भूमिका द्या आणि त्याच्या आयुष्यातील आणि काळातील प्रश्न विचारा.

## उपाय

### स्टडी बडी

खाली प्रारंभिक प्रॉम्प्ट दिला आहे, बघा तुम्ही याचा कसा वापर करू शकता आणि आवडीनुसार कसा सुधारू शकता.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बोट

येथे काही प्रॉम्प्ट्स आहेत जे तुम्ही वापरू शकता:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञानाची तपासणी

temperature संकल्पनेचा अर्थ काय आहे?

1. हे आउटपुट किती यादृच्छिक आहे हे नियंत्रित करते.
1. हे उत्तर किती मोठे आहे हे नियंत्रित करते.
1. हे किती टोकन्स वापरले जातात हे नियंत्रित करते.

## 🚀 आव्हान

कार्य करताना temperature विविध करण्याचा प्रयत्न करा, त्याला 0, 0.5, आणि 1 असे सेट करा. लक्षात ठेवा की 0 हा सर्वांत कमी विविधता आहे आणि 1 हा सर्वांत जास्त विविधता आहे. तुमच्या अ‍ॅपसाठी कोणती किंमत सर्वोत्तम कार्य करते?

## छान काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यावर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) कडे पाहा आणि तुमचे Generative AI ज्ञान वाढवत ठेवा!

धडा 7 कडे जा जिथे आपण [चॅट ऍप्लिकेशन्स कसे तयार करायचे](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) याचा अभ्यास करू!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->