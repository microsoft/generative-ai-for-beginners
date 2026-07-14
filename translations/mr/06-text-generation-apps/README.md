# मजकूर निर्मिती अनुप्रयोगांची निर्मिती

[![मजकूर निर्मिती अनुप्रयोगांची निर्मिती](../../../translated_images/mr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वर दिलेल्या प्रतिमेवर क्लिक करा)_

तुम्ही आतापर्यंत अभ्यासक्रमातून पाहिले आहे की प्रॉम्प्टसारखे मूलभूत संकल्पना आहेत आणि "प्रॉम्प्ट इंजिनिअरिंग" नावाचे एक संपूर्ण शाखा आहे. ChatGPT, Office 365, Microsoft Power Platform आणि अधिक सारखे अनेक साधने ज्यांच्याशी तुम्ही संवाद साधू शकता, ते तुम्हाला काही साध्य करण्यासाठी प्रॉम्प्ट वापरण्याची अनुमती देतात.

अशा अनुभवाचा समावेश एखाद्या अनुप्रयोगात करण्यासाठी, तुम्हाला प्रॉम्प्ट, पूर्णता यांसारख्या संकल्पना समजून घेणे आवश्यक आहे आणि कामासाठी लायब्ररी निवडणे आवश्यक आहे. हेच तुम्हाला या अध्यायात शिकवले जाईल.

## परिचय

या अध्यायात, तुम्ही:

- openai लायब्ररी आणि याच्या मूलभूत संकल्पना जाणून घेणार आहात.
- openai वापरून मजकूर निर्मिती अनुप्रयोग तयार करणार आहात.
- प्रॉम्प्ट, तापमान (temperature), टोकन्स यांसारख्या संकल्पनांचा वापर कसा करायचा हे समजून घेणार आहात.

## शिक्षण उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही करू शकाल:

- मजकूर निर्मिती अनुप्रयोग म्हणजे काय हे स्पष्ट करा.
- openai वापरून मजकूर निर्मिती अनुप्रयोग तयार करा.
- तुमच्या अनुप्रयोगाला जास्त किंवा कमी टोकन्स वापरायला सक्षम करा आणि विविध आउटपुटसाठी तापमान बदला.

## मजकूर निर्मिती अनुप्रयोग म्हणजे काय?

सामान्यतः तुम्ही जेव्हा अनुप्रयोग तयार करता तेव्हा त्याला काही प्रकारचे इंटरफेस असते, पुढीलप्रमाणे:

- आदेश-आधारित (Command-based). कन्सोल अनुप्रयोग ही अशी सामान्य ऍप्स आहेत जिथे तुम्ही आदेश टाइप करता आणि ते कार्य पार पाडते. उदाहरणार्थ, `git` हा आदेश-आधारित अनुप्रयोग आहे.
- वापरकर्ता इंटरफेस (UI). काही अनुप्रयोगांमध्ये ग्राफिकल वापरकर्ता इंटरफेस (GUI) असतो जिथे तुम्ही बटणे क्लिक करता, मजकूर टाइप करता, पर्याय निवडता आणि अधिक करता.

### कन्सोल आणि UI अनुप्रयोग मर्यादित आहेत

एखाद्या आदेश-आधारित अनुप्रयोगाशी तुलना करा जिथे तुम्ही आदेश टाइप करता:

- **हे मर्यादित आहे**. तुम्ही कोणताही आदेश टाइप करू शकत नाही, फक्त ते आदेश जे अनुप्रयोग समर्थित करतो.
- **भाषा-विशिष्ट**. काही अनुप्रयोग अनेक भाषा समर्थन करतात, पण प्रारूपाने अनुप्रयोग एका विशिष्ट भाषेसाठी तयार केला जातो, जरी तुम्ही अधिक भाषा समर्थन जोडू शकता.

### मजकूर निर्मिती अनुप्रयोगांचे फायदे

मग मजकूर निर्मिती अनुप्रयोग वेगळा कसा आहे?

मजकूर निर्मिती अनुप्रयोगात, तुम्हाला अधिक लवचिकता मिळते, तुम्ही आदेशाच्या संचाशी किंवा विशिष्ट इनपुट भाषेशी मर्यादित नसता. त्याऐवजी, तुम्ही निसर्ग भाषेचा वापर अनुप्रयोगाशी संवाद साधण्यासाठी करू शकता. आणखी एक फायदा म्हणजे तुम्ही आधीच या डेटास्रोताशी संवाद साधत आहात ज्यावर मोठ्या प्रमाणात माहितीचे प्रशिक्षण झाले आहे, तर पारंपारिक अनुप्रयोग डेटाबेसातील मर्यादित माहितीवर अवलंबून असू शकतो.

### मजकूर निर्मिती अनुप्रयोगाने काय बनवू शकतो?

तुम्ही बरेच काही तयार करू शकता. उदाहरणार्थ:

- **चॅटबॉट**. तुमच्या कंपनी आणि त्याच्या उत्पादनांबाबत प्रश्नांची उत्तरे देणारा चॅटबॉट चांगला पर्याय असू शकतो.
- **साहाय्यक**. LLMs सारखी मोठ्या भाषेची मॉडेल्स मजकूराचा सारांश काढणे, मजकूरातून माहिती मिळवणे, रिज्युमे सारखे मजकूर तयार करणे अशा कामांसाठी उत्कृष्ट आहेत.
- **कोड सहाय्यक**. तुम्ही वापरत असलेल्या भाषेच्या मॉडेलवर अवलंबून, तुम्ही कोड लिखाणासाठी सहाय्यक तयार करू शकता. उदाहरणार्थ, GitHub Copilot आणि ChatGPT सारख्या उत्पादनांचा वापर करून तुम्ही कोड लिहिण्यास मदत करू शकता.

## सुरुवात कशी करायची?

बरं, तुम्हाला LLM सह एकत्रीकरण करण्याचा मार्ग सापडवावा लागेल, जो सहसा पुढील दोन पद्धतींना समाविष्ट करतो:

- API वापरा. येथे तुम्ही तुमच्या प्रॉम्प्टसह वेब विनंत्या तयार करता आणि निर्मित मजकूर परत मिळवता.
- लायब्ररी वापरा. लायब्ररी API कॉल सुलभपणे सादर करतात आणि त्यांचा वापर सोपा करतात.

## लायब्ररी/SDKs

LLMs च्या सहकार्याने कार्य करण्यासाठी काही प्रसिद्ध लायब्ररीज आहेत उदा.:

- **openai**, ही लायब्ररी तुमच्या मॉडेलशी सहज जोडणी करण्यात मदत करते आणि प्रॉम्प्ट पाठवते.

नंतर काही لायब्ररीज जास्त उच्च पातळीवर काम करतात उदा.:

- **Langchain**. Langchain प्रसिद्ध आहे आणि Python ला समर्थन देते.
- **Semantic Kernel**. Semantic Kernel ही Microsoft द्वारे तयार केलेली लायब्ररी आहे जी C#, Python, आणि Java या भाषांना समर्थन करते.

## openai वापरून पहिले अनुप्रयोग तयार करा

चला पाहूया आपण पहिले अनुप्रयोग कसे तयार करू शकतो, कोणत्या लायब्ररी आवश्यक आहेत, किती प्रमाणात आणि कसा सुरू करायचा.

### openai स्थापित करा

OpenAI किंवा Azure OpenAI सह संवाद साधण्यासाठी अनेक लायब्ररी उपलब्ध आहेत. C#, Python, JavaScript, Java आणि इतर अनेक प्रोग्रामिंग भाषा वापरता येतात. आपण `openai` Python लायब्ररी वापरण्याचा निर्णय घेतला आहे, त्यामुळे आपण `pip` वापरून ती स्थापित करू.

```bash
pip install openai
```

### एक संसाधन तयार करा

तुम्हाला खालील पायऱ्या पार पाडाव्या लागतील:

- Azure वर खाते तयार करा [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI मध्ये प्रवेश मिळवा. येथे जा [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) आणि प्रवेशासाठी विनंती करा.

  > [!NOTE]
  > लेखनाच्या वेळी, तुम्हाला Azure OpenAI साठी प्रवेशासाठी अर्ज करावा लागतो.

- Python स्थापित करा <https://www.python.org/>
- Azure OpenAI सेवा संसाधन तयार केले आहे. संसाधन कसे तयार करावे यासाठी हा मार्गदर्शक पहा [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API की आणि अंत बिंदू शोधा

सध्या, तुम्हाला तुमच्या `openai` लायब्ररीला कोणती API की वापरायची ते सांगायचे आहे. तुमची API की शोधण्यासाठी, Azure OpenAI संसाधनाच्या "Keys and Endpoint" विभागात जा आणि "Key 1" मूल्य कॉपी करा.

![Azure पोर्टलमधील Keys आणि Endpoint संसाधन ब्लेड](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

आता ही माहिती कॉपी केल्यावर, लायब्ररींना ती वापरण्यास सांगा.

> [!NOTE]
> तुमची API की कोडपासून वेगळी ठेवणे चांगले. तुम्ही हे पर्यावरण चल (environment variables) वापरून करू शकता.
>
> - पर्यावरण चल `OPENAI_API_KEY` तुमच्या API कीमुळे सेट करा.
>   `export OPENAI_API_KEY='sk-...'`

### Azure साठी कॉन्फिगरेशन सेट करा

जर तुम्ही Azure OpenAI (सध्या Microsoft Foundry चा भाग) वापरत असाल, तर कॉन्फिगरेशन अशी सेट करा. आम्ही मानक `OpenAI` क्लाएंट वापरतो जो Azure OpenAI च्या `/openai/v1/` अंतबिंदूवर निर्देशीत आहे, जो Responses API सह कार्य करतो आणि `api_version` ची गरज नाही:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

वर आपण पुढील सेट करत आहोत:

- `api_key`, ही तुमची Azure पोर्टल किंवा Microsoft Foundry पोर्टलमध्ये सापडणारी API की आहे.
- `base_url`, ही तुमची Foundry संसाधनाचा अंतबिंदू `/openai/v1/` जोडून. स्थिर v1 अंतबिंदू OpenAI आणि Azure OpenAI वर कोणत्याही `api_version` व्यवस्थापनाशिवाय कार्य करतो.

> [!NOTE] > `os.environ` पर्यावरणीय चल वाचते. तुम्ही याचा वापर `AZURE_OPENAI_API_KEY` आणि `AZURE_OPENAI_ENDPOINT` सारखे पर्यावरणीय चल वाचण्यासाठी करू शकता. टर्मिनलमध्ये किंवा `dotenv` सारख्या लायब्ररीचा वापर करून हे सेट करा.

## मजकूर तयार करा

मजकूर निर्माण करण्याचा मार्ग म्हणजे Responses API चा `responses.create` पद्धती वापरणे. एक उदाहरण येथे आहे:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # हे तुमचे मॉडेल तैनात नाव आहे
    input=prompt,
    store=False,
)
print(response.output_text)
```

वर दिलेल्या कोडमध्ये, आपण प्रतिसाद तयार करतो आणि आम्हाला हवा असलेला मॉडेल आणि प्रॉम्प्ट पास करतो. नंतर `response.output_text` वापरून निर्मित मजकूर प्रदर्शित करतो.

### बहु-चक्र संवाद

Responses API एकल-चक्र मजकूर निर्मितीसाठी आणि बहु-चक्र चॅटबॉट्ससाठी योग्य आहे - तुम्ही संवाद तयार करण्यासाठी `input` मध्ये संदेशांची यादी पुरवता:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

या कार्यक्षमतेवर पुढील अध्यायात अधिक माहिती दिली जाईल.

## सराव - तुमचा पहिला मजकूर निर्मिती अनुप्रयोग

आता आपण openai कसे सेट अप करायचे ते शिकलो आहोत, तुमचा पहिला मजकूर निर्मिती अनुप्रयोग तयार करण्याची वेळ आहे. अनुप्रयोग तयार करण्यासाठी खालील चरणांचे पालन करा:

1. वर्च्युअल एन्व्हायर्नमेंट तयार करा आणि openai स्थापित करा:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > जर तुम्ही Windows वापरत असाल तर `source venv/bin/activate` च्या ऐवजी `venv\Scripts\activate` टाइप करा.

   > [!NOTE]
   > तुमचा Azure OpenAI की शोधण्यासाठी [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) येथे जा, `Open AI` शोधून निवडा नंतर `Keys and Endpoint` मध्ये जाऊन `Key 1` मूल्य कॉपी करा.

1. _app.py_ फाइल तयार करा आणि खालील कोड द्या:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # तुमचा पूर्णता कोड जोडा
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API वापरून विनंती करा
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # प्रतिसाद छापा
   print(response.output_text)
   ```

   > [!NOTE]
   > जर तुम्ही सामान्य OpenAI (Azure नव्हे) वापरत असाल, तर `client = OpenAI(api_key="<replace this value with your OpenAI key>")` वापरा (`base_url` नाही) आणि `gpt-4o-mini` सारखे मॉडेल नाव वापरा, deployment नावाऐवजी.

   तुम्हाला खालील प्रमाणे आउटपुट दिसेल:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## विविध प्रकारचे प्रॉम्प्ट्स, वेगवेगळ्या कामांसाठी

आता तुम्ही प्रॉम्प्ट वापरून मजकूर तयार करण्याचे मार्ग पाहिले आहे. तुम्हाचं एक प्रोग्राम सुद्धा असून तुम्ही तो बदलून विविध प्रकारचे मजकूर निर्माण करू शकता.

प्रॉम्प्ट्स विविध कामांसाठी वापरता येतात. उदाहरणार्थ:

- **एक प्रकारचा मजकूर तयार करा**. उदाहरणार्थ, कविता, क्विझसाठी प्रश्न इत्यादी.
- **माहिती शोधा**. तुम्ही प्रॉम्प्ट वापरून अशा माहिती साठी शोधू शकता जसे की 'वेब डेव्हलपमेंटमध्ये CORS म्हणजे काय?'.
- **कोड तयार करा**. प्रॉम्प्ट वापरून कोड तयार करू शकता, उदाहरणार्थ ईमेलसाठी regex तयार करणे किंवा संपूर्ण वेब अनुप्रयोग तयार करणे.

## अधिक व्यावहारिक वापर: पाककृती जनरेटर

कल्पना करा की तुमच्याकडे घरी साहित्य आहे आणि तुम्हाला काही शिजवायचे आहे. त्यासाठी तुम्हाला पाककृती हवी आहे. पाककृती शोधण्यासाठी तुम्ही सर्च इंजिन वापरू शकता अथवा LLM वापरू शकता.

तुम्ही खालीलप्रमाणे प्रॉम्प्ट लिहू शकता:

> "खालील साहित्यांसह जेवणासाठी ५ पाककृती दाखवा: कोंबडी, बटाटे, आणि गाजर. प्रत्येक पाककृतीसाठी वापरलेले सर्व साहित्य यादी करा"

वरच्या प्रॉम्प्टनुसार, तुम्हाला खालीलप्रमाणे प्रतिसाद मिळू शकतो:

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

हा निकाल छान आहे, मला काय शिजवायचं ते समजलं. पुढील सुधारणा म्हणून उपयुक्त असू शकतात:

- मला नको असलेल्या किंवा मला अलर्जी असलेल्या साहित्याला फिल्टर करणे.
- जर घरी सर्व साहित्य नसेल तर खरेदी यादी तयार करणे.

वरील प्रकरणांसाठी, आपण आणखी एक प्रॉम्प्ट जोडूया:

> "कृपया लसूण असलेल्या पाककृती काढा कारण मला त्यावर अलर्जी आहे आणि त्याऐवजी काहीतरी दुसरे बदला. तसेच, पाककृतींसाठी खरेदी यादी तयार करा, लक्षात घेऊन की माझ्याकडे आधीच कोंबडी, बटाटे आणि गाजर आहेत."

आत्ता तुमच्याकडे नवीन निकाल आहे, म्हणजे:

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

ते तुमची पाच पाककृती आहेत ज्यात लसूण नाही आहे आणि तुमच्याकडे घरात जी सामग्री आहे त्याचा विचार करून खरेदी यादी आहे.

## सराव - पाककृती जनरेटर तयार करा

आता आपल्याला एक परिस्थिती दाखवली आहे, तर त्याला जुळवणारा कोड लिहूया. त्यासाठी, खालील चरणांचे पालन करा:

1. विद्यमान _app.py_ फाइल वापरून प्रारंभ करा
1. `prompt` व्हेरिएबल शोधा आणि याचा कोड खालीलप्रमाणे बदला:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   तुम्ही आता कोड चालविल्यास, खालीलप्रमाणे आउटपुट पाहू शकता:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > लक्षात घ्या, तुमचे LLM नॉनडिटर्मिनिस्टिक आहे, म्हणून प्रत्येक वेळी प्रोग्राम चालविल्यावर वेगवेगळे निकाल येऊ शकतात.

   उत्तम, आता पाहूया आपण पुढे कसे सुधारणा करू शकतो. सुधारणा करण्यासाठी, आपल्याला कोड लवचिक ठेवायचा आहे, म्हणजे साहित्य व पाककृतींची संख्या सुधारता आणि बदलता यावी.

1. कोड खालीलप्रमाणे बदला:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # कृतींची संख्या प्रॉम्प्ट आणि साहित्यांमध्ये मध्यवर्ती करा
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   चाचणीसाठी कोड चालविल्यास, असे दिसू शकते:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### फिल्टर आणि खरेदी यादी जोडून सुधारणा करा

आता आपल्याकडे एक काम करणारा अनुप्रयोग आहे जो पाककृती तयार करू शकतो आणि वापरकर्त्यांकडील इनपुटवर लवचिकपणे अवलंबून आहे, पाककृतींची संख्या तसेच वापरलेले साहित्य.

पुढील सुधारण्यासाठी, आपल्याला खालील जोडायचे आहे:

- **साहित्य फिल्टर करा**. आपण नको असलेले किंवा ज्याला आपल्याला अलर्जी आहे ते साहित्य फिल्टर करू शकुया. यासाठी आपला विद्यमान प्रॉम्प्ट संपवून खालीलप्रमाणे फिल्टर अटी जोडा:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  वर, आपण प्रॉम्प्टच्या शेवटी `{filter}` जोडले आहे आणि वापरकर्त्याकडून फिल्टर मूल्य घेतले आहे.

  प्रोग्राम चालवण्याचा उदाहरण इनपुट आता असे दिसू शकतो:

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

  तुम्हाला दिसेल, ज्यामध्ये दूध आहे अशा पाककृती काढून टाकल्या आहेत. परंतु, जर तुम्हाला लॅक्टोज असहिष्णूता असेल तर कदाचित चीज असलेल्या पाककृती देखील काढून टाकायच्या असतील, त्यामुळे स्पष्टता आवश्यक आहे.


- **खरेदीची यादी तयार करा**. आपल्याकडे घरात काय आहे हे लक्षात घेता, आपल्याला एक खरेदीची यादी तयार करायची आहे.

  या कार्यासाठी, आपण सर्व काही एका प्रॉम्प्टमध्ये सोडवण्याचा प्रयत्न करू शकतो किंवा दोन प्रॉम्प्टमध्ये विभाजित करू शकतो. चला, दुसऱ्या पर्यायाचा प्रयत्न करूया. येथे आम्ही अतिरिक्त प्रॉम्प्ट जोडण्याचा प्रस्ताव देत आहोत, परंतु त्यासाठी पहिल्या प्रॉम्प्टचा निकाल दुसऱ्या प्रॉम्प्टसाठी संदर्भ म्हणून जोडावा लागेल.

  कोडमध्ये तो भाग शोधा जो पहिल्या प्रॉम्प्टचा निकाल छापतो आणि खालील कोड त्याच्या खाली जोडा:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # प्रतिक्रिया छापा
  print("Shopping list:")
  print(response.output_text)
  ```

  पुढील गोष्टी लक्षात घ्या:

  1. आम्ही पहिल्या प्रॉम्प्टचा निकाल नवीन प्रॉम्प्टमध्ये जोडून नवीन प्रॉम्प्ट तयार करत आहोत:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. आम्ही नवीन विनंती पाठवतो, पण पहिल्या प्रॉम्प्टसाठी विचारलेल्या टोकन्सच्या संख्येचा देखील विचार करतो, म्हणून या वेळी `max_output_tokens` 1200 म्हणतो.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     हा कोड चालवून, आता आपण खालील आउटपुटवर पोहोचतो:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## आपले सेटअप सुधारित करा

आतापर्यंत आपल्याकडे कार्य करणारा कोड आहे, पण अजून काही सुधारणा कराव्या लागतील. काही गोष्टी ज्या आपल्याला कराव्या लागतील त्या आहेत:

- **कोडमधून रहस्ये वेगळी करा**, जसे API की. रहस्ये कोडमध्ये ठेवू नयेत आणि सुरक्षित ठिकाणी संग्रहित केली पाहिजेत. रहस्ये वेगळी करण्यासाठी, आपण पर्यावरण चल (environment variables) आणि `python-dotenv` सारख्या लायब्ररींचा वापर करू शकतो ज्यामुळे ती फाईलमधून लोड होतात. कोडमध्ये हे अशा प्रकारे दिसेल:

  1. `.env` नावाची फाईल तयार करा ज्यामध्ये खालील सामग्री असेल:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > नोंद, Microsoft Foundry मध्ये Azure OpenAI साठी, परंतु पुढील पर्यावरण चल सेट करा:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     कोडमध्ये पर्यावरण चल अशा प्रकारे लोड कराल:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **टोकन्सची लांबी याविषयी एक शब्द**. आपल्याला हवा असलेला मजकूर निर्माण करण्यासाठी किती टोकन्स लागतील हे लक्षात घ्यावे. टोकन्सची किंमत लागते, त्यामुळे शक्य असल्यास, आपल्याला वापरले जाणारे टोकन्स कमी करण्याचा प्रयत्न करावा. उदाहरणार्थ, आपण प्रॉम्प्ट असे लिहू शकलो का ज्यामुळे कमी टोकन्स लागतील?

  वापरले जाणारे टोकन्स बदलण्यासाठी, आपण `max_output_tokens` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर तुम्हाला 100 टोकन्स वापरायचे असतील, तर असे करा:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **तापमानासोबत प्रयोग**. तापमान हा एक महत्त्वाचा संदर्भ आहे जो आतापर्यंत आपण उल्लेख केला नाही पण आपल्या प्रोग्रामच्या कामगिरीसाठी महत्त्वाचा आहे. तापमान जास्त असले तर आउटपुट जास्त अनियमित होतो. उलट, तापमान कमी असले तर आउटपुट अधिक पूर्वनिर्धारित वाटतो. आपण आपल्या आउटपुटमध्ये विविधता हवी आहे का हे विचार करा.

  तापमान बदलण्यासाठी, आपण `temperature` पॅरामीटर वापरू शकता. उदाहरणार्थ, जर तुम्हाला तापमान 0.5 वापरायचे असेल, तर असे करा:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > नोंद, 1.0 कडे जास्त जवळ असल्यास आउटपुट अधिक विविध असतो.

## Assignment

या असाइनमेंटसाठी, आपण काय तयार करायचे ते निवडू शकता.

येथे काही सूचना आहेत:

- रेसिपी जनरेटर अॅप सुधारण्यासाठी त्यास अजून चांगले करा. तापमान मूल्यांसोबत आणि प्रॉम्प्टसह खेळा आणि बघा काय नवीन येते.
- "स्टडी बड्डी" तयार करा. हा अॅप एखाद्या विषयाबाबत प्रश्नांची उत्तरे देण्यास सक्षम असावा, उदाहरणार्थ Python; तुम्ही प्रॉम्प्ट देऊ शकता "Python मधील एखाद्या विषयाचा अर्थ काय?", किंवा "काही विषयासाठी कोड दाखवा" असे काही.
- इतिहास बॉट, इतिहास जिवंत करा, बॉटला एखाद्या ऐतिहासिक व्यक्तीची भूमिका द्या आणि त्याच्या आयुष्याबद्दल प्रश्न विचारा.

## समाधान

### स्टडी बड्डी

खाली एक प्रारंभिक प्रॉम्प्ट दिला आहे, बघा तुम्ही याचा वापर कसा करू शकता आणि त्याला तुमच्या आवडीनुसार कसा बदलू शकता.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### इतिहास बॉट

येथे काही प्रॉम्प्ट आहेत जे तुम्ही वापरू शकता:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ज्ञान तपासणी

तापमान संकल्पना काय करते?

1. ती आउटपुट किती अनियमित असेल हे नियंत्रित करते.
1. ती प्रतिसाद किती मोठा असेल हे नियंत्रित करते.
1. ती किती टोकन्स वापरले जातील हे नियंत्रित करते.

## 🚀 आव्हान

असाइनमेंटवर काम करताना, तापमान वेगवेगळे करून बघा, 0, 0.5, आणि 1 अशी सेटिंग करा. लक्षात ठेवा की 0 कमी अनियमित आहे आणि 1 जास्त. तुमच्या अॅपसाठी कोणते मूल्य उत्तम काम करते?

## उत्कृष्ट काम! तुमचे शिक्षण सुरू ठेवा

हा धडा पूर्ण केल्यानंतर, आमच्या [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) पाहा आणि तुमचे Generative AI ज्ञान अधिक वाढवा!

पुढील धडा 7 पहा जिथे आपण कसे [चॅट अॅप्लिकेशन तयार करायचे](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) हे पाहणार आहोत!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->