<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:26:50+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mr"
}
-->
# तुमचे डेव्हलपमेंट वातावरण सेट करा

आम्ही या रेपॉझिटरी आणि कोर्ससाठी [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) वापरला आहे ज्यामध्ये Python3, .NET, Node.js आणि Java विकासासाठी Universal runtime आहे. संबंधित कॉन्फिगरेशन `devcontainer.json` फाईलमध्ये परिभाषित आहे जी या रेपॉझिटरीच्या मूळ `.devcontainer/` फोल्डरमध्ये आहे.

डेव्ह कंटेनर सक्रिय करण्यासाठी, ते [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड runtime साठी) किंवा [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (लोकल डिव्हाइस-होस्टेड runtime साठी) मध्ये सुरू करा. VS Code मध्ये dev containers कसे कार्य करतात याबाबत अधिक माहितीसाठी [ही दस्तऐवज वाचा](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).

> [!TIP]  
> आम्ही GitHub Codespaces वापरण्याचा सल्ला देतो कारण ते कमी प्रयत्नात जलद सुरुवात करण्यास मदत करते. वैयक्तिक खात्यांसाठी ते उदार [फ्री वापर कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) देते. तुमचा कोटा जास्तीत जास्त वापरण्यासाठी निष्क्रिय codespaces थांबवण्यासाठी किंवा हटवण्यासाठी [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कॉन्फिगर करा.


## 1. असाइनमेंट्स चालविणे

प्रत्येक धड्यात _ऐच्छिक_ असाइनमेंट्स असू शकतात जे Python, .NET/C#, Java आणि JavaScript/TypeScript यांसारख्या एक किंवा अधिक प्रोग्रामिंग भाषांमध्ये दिले जातील. या विभागात त्या असाइनमेंट्स चालविण्याबाबत सामान्य मार्गदर्शन दिले आहे.

### 1.1 Python असाइनमेंट्स

Python असाइनमेंट्स अ‍ॅप्लिकेशन्स (`.py` फाइल्स) किंवा Jupyter notebooks (`.ipynb` फाइल्स) स्वरूपात दिले जातात.  
- नोटबुक चालविण्यासाठी, Visual Studio Code मध्ये ते उघडा, नंतर वर उजव्या कोपऱ्यातील _Select Kernel_ वर क्लिक करा आणि दिसणाऱ्या डीफॉल्ट Python 3 पर्यायाची निवड करा. आता तुम्ही _Run All_ करून नोटबुक चालवू शकता.  
- कमांड-लाइनवरून Python अ‍ॅप्लिकेशन्स चालविण्यासाठी, असाइनमेंट-विशिष्ट सूचना पाळा ज्यामुळे योग्य फाइल्स निवडता येतील आणि आवश्यक आर्ग्युमेंट्स दिले जातील.

## 2. प्रदाते कॉन्फिगर करणे

असाइनमेंट्स **कदाचित** एक किंवा अधिक Large Language Model (LLM) डिप्लॉयमेंट्ससाठी OpenAI, Azure किंवा Hugging Face सारख्या समर्थित सेवा प्रदात्यांद्वारे काम करण्यासाठी सेटअप केले जाऊ शकतात. हे प्रदाते _hosted endpoint_ (API) पुरवतात ज्याला योग्य प्रमाणपत्रांसह (API key किंवा token) प्रोग्रामॅटिकली प्रवेश करता येतो. या कोर्समध्ये आम्ही खालील प्रदात्यांवर चर्चा करतो:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ज्यामध्ये मुख्य GPT सिरीजसह विविध मॉडेल्स आहेत.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) जे OpenAI मॉडेल्ससाठी एंटरप्राइझ रेडीनेसवर लक्ष केंद्रित करते  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) मुक्त स्रोत मॉडेल्स आणि इन्फरन्स सर्व्हरसाठी

**या व्यायामांसाठी तुम्हाला तुमची स्वतःची खाती वापरावी लागतील**. असाइनमेंट्स ऐच्छिक आहेत त्यामुळे तुम्ही तुमच्या आवडीनुसार एक, सर्व किंवा कोणतेही प्रदाते सेटअप करू शकता. साइनअपसाठी काही मार्गदर्शन:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | अनेक मॉडेल्स उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [प्रवेशासाठी पूर्व अर्ज आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

वेगवेगळ्या प्रदात्यांसाठी या रेपॉझिटरीला _कॉन्फिगर_ करण्यासाठी खालील सूचनांचे पालन करा. विशिष्ट प्रदाता आवश्यक असलेल्या असाइनमेंट्सच्या फाइलनाम्यात खालील टॅग्स असतील:  
 - `aoai` - Azure OpenAI endpoint, key आवश्यक  
 - `oai` - OpenAI endpoint, key आवश्यक  
 - `hf` - Hugging Face token आवश्यक  

तुम्ही एक, काहीही किंवा सर्व प्रदाते कॉन्फिगर करू शकता. संबंधित असाइनमेंट्समध्ये प्रमाणपत्रे नसल्यास त्रुटी येतील.

###  2.1. `.env` फाइल तयार करा

आम्ही गृहित धरतो की तुम्ही वरील मार्गदर्शन वाचले आहे, संबंधित प्रदात्यांसाठी साइन अप केले आहे आणि आवश्यक प्रमाणीकरण क्रेडेन्शियल्स (API_KEY किंवा token) मिळवले आहेत. Azure OpenAI च्या बाबतीत, तुम्हाकडे Azure OpenAI सेवा (endpoint) ची वैध डिप्लॉयमेंट आणि किमान एक GPT मॉडेल चॅट पूर्णतेसाठी डिप्लॉय केलेले आहे.

पुढील पायरी म्हणजे तुमच्या **लोकल पर्यावरणातील व्हेरिएबल्स** खालीलप्रमाणे कॉन्फिगर करणे:

1. मूळ फोल्डरमध्ये `.env.copy` नावाची फाइल शोधा ज्यामध्ये खालीलप्रमाणे सामग्री असावी:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. खालील कमांड वापरून ती फाइल `.env` मध्ये कॉपी करा. ही फाइल _gitignore_ केलेली आहे, त्यामुळे गुपिते सुरक्षित राहतात.

   ```bash
   cp .env.copy .env
   ```

3. पुढील विभागात दिल्याप्रमाणे `=` च्या उजव्या बाजूला असलेली जागा योग्य माहितीने भरा.

3. (पर्यायी) जर तुम्ही GitHub Codespaces वापरत असाल, तर तुम्हाला या रेपॉझिटरीशी संबंधित _Codespaces secrets_ म्हणून पर्यावरणीय व्हेरिएबल्स जतन करण्याचा पर्याय आहे. अशा परिस्थितीत तुम्हाला लोकल .env फाइल सेटअप करण्याची गरज नाही. **तथापि, हा पर्याय फक्त GitHub Codespaces वापरत असल्यासच कार्य करतो.** Docker Desktop वापरत असल्यास तुम्हाला .env फाइल सेटअप करावीच लागेल.

### 2.2. `.env` फाइल भरा

व्हेरिएबल्स काय दर्शवतात हे समजून घेण्यासाठी त्यांची नावे पाहूया:

| Variable  | वर्णन  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हा तुमच्या प्रोफाइलमध्ये सेट केलेला वापरकर्ता प्रवेश टोकन आहे |
| OPENAI_API_KEY | Azure नसलेल्या OpenAI endpoints साठी सेवा वापरण्याचा अधिकृत की |
| AZURE_OPENAI_API_KEY | Azure OpenAI सेवा वापरण्याचा अधिकृत की |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI संसाधनासाठी डिप्लॉय केलेला endpoint |
| AZURE_OPENAI_DEPLOYMENT | _टेक्स्ट जनरेशन_ मॉडेल डिप्लॉयमेंट endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _टेक्स्ट एम्बेडिंग्स_ मॉडेल डिप्लॉयमेंट endpoint |
| | |

टीप: शेवटचे दोन Azure OpenAI व्हेरिएबल्स चॅट पूर्णता (टेक्स्ट जनरेशन) आणि व्हेक्टर शोध (एम्बेडिंग्स) साठी डीफॉल्ट मॉडेल दर्शवतात. त्यांचे सेटअप संबंधित असाइनमेंट्समध्ये दिले जाईल.

### 2.3 Azure कॉन्फिगर करा: पोर्टलमधून

Azure OpenAI endpoint आणि key ची माहिती [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये मिळेल, तर तेथे सुरुवात करूया.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा  
1. साइडबारमधील (डाव्या बाजूचा मेनू) **Keys and Endpoint** पर्यायावर क्लिक करा  
1. **Show Keys** वर क्लिक करा - KEY 1, KEY 2 आणि Endpoint दिसतील  
1. AZURE_OPENAI_API_KEY साठी KEY 1 वापरा  
1. AZURE_OPENAI_ENDPOINT साठी Endpoint वापरा  

आता आपल्याला डिप्लॉय केलेल्या विशिष्ट मॉडेल्ससाठी endpoints लागतील.

1. Azure OpenAI संसाधनासाठी साइडबारमधील **Model deployments** पर्यायावर क्लिक करा  
1. गंतव्य पृष्ठावर, **Manage Deployments** वर क्लिक करा  

हे तुम्हाला Azure OpenAI Studio वेबसाइटवर घेऊन जाईल, जिथे पुढील मूल्ये मिळतील.

### 2.4 Azure कॉन्फिगर करा: स्टुडिओमधून

1. वर दिलेल्या प्रमाणे तुमच्या संसाधनातून [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) वर जा  
1. साइडबारमधील (डावीकडील) **Deployments** टॅबवर क्लिक करा जेथे सध्या डिप्लॉय केलेले मॉडेल्स दिसतील  
1. तुमचे इच्छित मॉडेल डिप्लॉय नसेल तर **Create new deployment** वापरून ते डिप्लॉय करा  
1. तुम्हाला _text-generation_ मॉडेलची गरज आहे - आम्ही **gpt-35-turbo** शिफारस करतो  
1. तुम्हाला _text-embedding_ मॉडेलची गरज आहे - आम्ही **text-embedding-ada-002** शिफारस करतो  

आता पर्यावरणीय व्हेरिएबल्समध्ये _Deployment name_ अपडेट करा. हे सहसा मॉडेलच्या नावासारखेच असते जोपर्यंत तुम्ही ते स्पष्टपणे बदलले नसेल. उदाहरणार्थ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**काम पूर्ण झाल्यावर .env फाइल जतन करायला विसरू नका**. आता तुम्ही फाइल बंद करू शकता आणि नोटबुक चालविण्याच्या सूचनांकडे परत जाऊ शकता.

### 2.5 OpenAI कॉन्फिगर करा: प्रोफाइलमधून

तुमचा OpenAI API key तुमच्या [OpenAI खात्यात](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) सापडेल. जर तुमच्याकडे खाते नसेल तर तुम्ही साइन अप करून API key तयार करू शकता. की मिळाल्यानंतर `.env` फाइलमधील `OPENAI_API_KEY` व्हेरिएबलमध्ये ती भरा.

### 2.6 Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

तुमचा Hugging Face टोकन तुमच्या प्रोफाइलमधील [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) मध्ये सापडेल. हे सार्वजनिकपणे पोस्ट करू नका किंवा शेअर करू नका. त्याऐवजी, या प्रोजेक्टसाठी नवीन टोकन तयार करा आणि ते `.env` फाइलमधील `HUGGING_FACE_API_KEY` व्हेरिएबलमध्ये कॉपी करा. _टीप:_ हे तांत्रिकदृष्ट्या API key नाही, पण प्रमाणीकरणासाठी वापरले जाते म्हणून आम्ही नाव ठेवले आहे जेणेकरून सुसंगतता राहील.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.