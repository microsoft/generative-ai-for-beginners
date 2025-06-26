<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:13:46+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mr"
}
-->
# आपल्या डेव्हलपमेंट वातावरणाची सेटअप करा

आम्ही या रेपॉझिटरी आणि कोर्सला एक [डेव्हलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) सह सेटअप केले आहे ज्यात Python3, .NET, Node.js आणि Java डेव्हलपमेंटला समर्थन देणारी युनिव्हर्सल रनटाइम आहे. संबंधित कॉन्फिगरेशन `devcontainer.json` फाईलमध्ये परिभाषित केले आहे जी या रेपॉझिटरीच्या मुळात `.devcontainer/` फोल्डरमध्ये आहे.

डेव्हलपमेंट कंटेनर सक्रिय करण्यासाठी, [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) मध्ये (क्लाउड-होस्टेड रनटाइमसाठी) किंवा [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) मध्ये (स्थानिक डिव्हाइस-होस्टेड रनटाइमसाठी) लॉन्च करा. VS Code मध्ये डेव्हलपमेंट कंटेनर कसे कार्य करतात याबद्दल अधिक तपशीलांसाठी [ही दस्तऐवज](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) वाचा.

> [!TIP]  
> कमी प्रयत्नात जलद सुरुवातीसाठी GitHub Codespaces वापरण्याची शिफारस करतो. वैयक्तिक खात्यांसाठी उदार [मोफत वापर कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान करते. आपल्या कोटा वापर वाढवण्यासाठी नॉन-एक्टिव्ह कोडस्पेस थांबवण्यासाठी किंवा हटवण्यासाठी [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कॉन्फिगर करा.

## 1. असाइनमेंट्स कार्यान्वित करणे

प्रत्येक धड्याला _ऐच्छिक_ असाइनमेंट्स असतील जे एक किंवा अधिक प्रोग्रामिंग भाषांमध्ये दिले जाऊ शकतात, ज्यात Python, .NET/C#, Java आणि JavaScript/TypeScript समाविष्ट आहेत. या विभागात त्या असाइनमेंट्स कार्यान्वित करण्यासंबंधी सामान्य मार्गदर्शन प्रदान केले आहे.

### 1.1 Python असाइनमेंट्स

Python असाइनमेंट्स अॅप्लिकेशन्स (`.py` फाईल्स) किंवा Jupyter नोटबुक्स (`.ipynb` फाईल्स) म्हणून प्रदान केले जातात.
- नोटबुक चालवण्यासाठी, Visual Studio Code मध्ये उघडा आणि _Select Kernel_ (वरच्या उजवीकडे) क्लिक करा आणि दर्शवलेला डिफॉल्ट Python 3 पर्याय निवडा. आता नोटबुक कार्यान्वित करण्यासाठी _Run All_ क्लिक करू शकता.
- कमांड-लाइनवरून Python अॅप्लिकेशन्स चालवण्यासाठी, योग्य फाईल्स निवडण्यासाठी आणि आवश्यक युक्तिवाद प्रदान करण्यासाठी असाइनमेंट-विशिष्ट सूचना अनुसरण करा.

## 2. प्रदात्यांची कॉन्फिगरेशन करणे

असाइनमेंट्स **कदाचित** एक किंवा अधिक मोठे भाषा मॉडेल (LLM) डिप्लॉयमेंट्ससाठी समर्थन केलेल्या सेवा प्रदात्या द्वारे सेटअप केले जातील जसे की OpenAI, Azure किंवा Hugging Face. हे _होस्टेड एंडपॉइंट_ (API) प्रदान करतात ज्यांना आम्ही योग्य प्रमाणपत्रांसह (API key किंवा टोकन) प्रोग्रामेटिकली ऍक्सेस करू शकतो. या कोर्समध्ये, आम्ही या प्रदात्यांबद्दल चर्चा करतो:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मॉडेल्ससह ज्यात मुख्य GPT मालिका समाविष्ट आहे.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडेल्ससाठी ज्यात एंटरप्राइझ तयार असण्यावर लक्ष केंद्रित आहे.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडेल्स आणि इन्फरन्स सर्व्हरसाठी.

**आपल्याला या व्यायामांसाठी स्वतःचे खाते वापरावे लागेल**. असाइनमेंट्स ऐच्छिक आहेत त्यामुळे आपण आपल्या आवडींनुसार एक, सर्व - किंवा कोणतेही प्रदाता सेटअप करण्याचा निर्णय घेऊ शकता. साइनअपसाठी काही मार्गदर्शन:

| साइनअप | खर्च | API Key | Playground | टिप्पण्या |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [किंमत](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | उपलब्ध अनेक मॉडेल्स |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [किंमत](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK जलद प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडिओ जलद प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ऍक्सेससाठी आधी अर्ज करणे आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [किंमत](https://huggingface.co/pricing) | [ऍक्सेस टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

खालील निर्देशांचे अनुसरण करा विविध प्रदात्यांसह वापरण्यासाठी या रेपॉझिटरीचे _कॉन्फिगर_ करण्यासाठी. विशिष्ट प्रदात्याची आवश्यकता असलेल्या असाइनमेंट्स त्यांच्या फाईलनाममध्ये एक या टॅग्सपैकी एक असेल:
- `aoai` - Azure OpenAI एंडपॉइंट, की आवश्यक आहे
- `oai` - OpenAI एंडपॉइंट, की आवश्यक आहे
- `hf` - Hugging Face टोकन आवश्यक आहे

आपण एक, कोणताही, किंवा सर्व प्रदाता कॉन्फिगर करू शकता. संबंधित असाइनमेंट्स फक्त अनुपस्थित प्रमाणपत्रांवर त्रुटी देतात.

### 2.1. `.env` फाईल तयार करा

आम्ही मानतो की आपण वरील मार्गदर्शन वाचले आहे आणि संबंधित प्रदात्यांसह साइन अप केले आहे आणि आवश्यक प्रमाणपत्रे प्राप्त केली आहेत (API_KEY किंवा टोकन). Azure OpenAI च्या बाबतीत, आम्ही मानतो की Azure OpenAI सेवाचे वैध डिप्लॉयमेंट (एंडपॉइंट) आहे ज्यामध्ये कमीतकमी एक GPT मॉडेल चॅट पूर्ण करण्यासाठी डिप्लॉय केले आहे.

पुढील चरण आपल्या **स्थानिक पर्यावरण चलांचे** कॉन्फिगर करणे आहे:

1. मुळ फोल्डरमध्ये `.env.copy` फाईल शोधा ज्यामध्ये खालीलप्रमाणे सामग्री असावी:

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

2. खालील कमांडचा वापर करून त्या फाईलला `.env` मध्ये कॉपी करा. ही फाईल _gitignore-d_ आहे, गुपिते सुरक्षित ठेवते.

   ```bash
   cp .env.copy .env
   ```

3. पुढील विभागात वर्णन केल्याप्रमाणे मूल्ये (डाव्या बाजूला `=` च्या जागी प्लेसहोल्डर्स बदला) भरा.

3. (पर्याय) आपण GitHub Codespaces वापरत असल्यास, आपल्याला या रेपॉझिटरीशी संबंधित पर्यावरण चलांना _Codespaces secrets_ म्हणून जतन करण्याचा पर्याय आहे. त्या बाबतीत, आपल्याला स्थानिक .env फाईल सेटअप करण्याची आवश्यकता नाही. **तथापि, लक्षात घ्या की हा पर्याय फक्त आपण GitHub Codespaces वापरत असल्यास कार्य करतो.** आपण Docker Desktop वापरत असल्यास आपल्याला .env फाईल सेटअप करणे आवश्यक आहे.

### 2.2. `.env` फाईल भरा

चल नावांवर एक द्रुत नजर टाकूया ते काय दर्शवतात ते समजून घेण्यासाठी:

| चल | वर्णन |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हे आपल्या प्रोफाइलमध्ये सेट केलेले वापरकर्ता ऍक्सेस टोकन आहे |
| OPENAI_API_KEY | हे non-Azure OpenAI एंडपॉइंट्ससाठी सेवा वापरण्यासाठी अधिकृतता की आहे |
| AZURE_OPENAI_API_KEY | हे त्या सेवेसाठी अधिकृतता की आहे |
| AZURE_OPENAI_ENDPOINT | हे Azure OpenAI संसाधनासाठी डिप्लॉय केलेले एंडपॉइंट आहे |
| AZURE_OPENAI_DEPLOYMENT | हे _टेक्स्ट जनरेशन_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | हे _टेक्स्ट एम्बेडिंग्स_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| | |

टीप: शेवटचे दोन Azure OpenAI चल चॅट पूर्ण करण्यासाठी (टेक्स्ट जनरेशन) आणि वेक्टर शोध (एम्बेडिंग्स) साठी अनुक्रमे एक डिफॉल्ट मॉडेल दर्शवतात. त्यांचे सेटिंगसाठी निर्देश संबंधित असाइनमेंट्समध्ये परिभाषित केले जातील.

### 2.3 Azure कॉन्फिगर करा: पोर्टलमधून

Azure OpenAI एंडपॉइंट आणि की मूल्ये [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये सापडतील त्यामुळे तिथे सुरुवात करूया.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा
1. साइडबारमध्ये (डाव्या मेनूमध्ये) **Keys and Endpoint** पर्याय क्लिक करा.
1. **Show Keys** क्लिक करा - आपल्याला खालील दिसेल: KEY 1, KEY 2 आणि Endpoint.
1. AZURE_OPENAI_API_KEY साठी KEY 1 मूल्य वापरा
1. AZURE_OPENAI_ENDPOINT साठी Endpoint मूल्य वापरा

पुढे, आम्हाला आम्ही डिप्लॉय केलेल्या विशिष्ट मॉडेल्ससाठी एंडपॉइंट्सची आवश्यकता आहे.

1. Azure OpenAI संसाधनासाठी साइडबार (डाव्या मेनू) मध्ये **Model deployments** पर्याय क्लिक करा.
1. गंतव्य पृष्ठावर, **Manage Deployments** क्लिक करा

हे आपल्याला Azure OpenAI स्टुडिओ वेबसाइटवर घेऊन जाईल, जिथे आम्ही खाली वर्णन केल्याप्रमाणे इतर मूल्ये शोधू.

### 2.4 Azure कॉन्फिगर करा: स्टुडिओमधून

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **आपल्या संसाधनातून** वर वर्णन केल्याप्रमाणे जा.
1. साइडबार (डावा) मध्ये **Deployments** टॅब क्लिक करा जेणेकरून सध्या डिप्लॉय केलेले मॉडेल्स पाहता येतील.
1. आपले इच्छित मॉडेल डिप्लॉय नसेल, तर **Create new deployment** वापरून ते डिप्लॉय करा.
1. आपल्याला _टेक्स्ट जनरेशन_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो: **gpt-35-turbo**
1. आपल्याला _टेक्स्ट एम्बेडिंग_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो **text-embedding-ada-002**

आता आपण वापरलेल्या _Deployment name_ दर्शवण्यासाठी पर्यावरण चल अद्यतनित करा. हे सहसा मॉडेलच्या नावासारखेच असेल, जोपर्यंत आपण ते स्पष्टपणे बदलले नाही. म्हणून, उदाहरणार्थ, आपल्याकडे असे असू शकते:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**पूर्ण झाल्यावर .env फाईल जतन करायला विसरू नका**. आपण आता फाईल बंद करू शकता आणि नोटबुक चालवण्याच्या सूचनांकडे परत जाऊ शकता.

### 2.5 OpenAI कॉन्फिगर करा: प्रोफाइलमधून

आपली OpenAI API की आपल्या [OpenAI खात्यामध्ये](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) सापडेल. आपल्याकडे नसल्यास, आपण खाते साइन अप करू शकता आणि API की तयार करू शकता. एकदा आपल्याकडे की असल्यास, आपण ती `.env` फाईलमधील `OPENAI_API_KEY` चल भरण्यासाठी वापरू शकता.

### 2.6 Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

आपले Hugging Face टोकन आपल्या प्रोफाइलमध्ये [ऍक्सेस टोकन्स](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अंतर्गत सापडेल. हे सार्वजनिकपणे पोस्ट किंवा शेअर करू नका. त्याऐवजी, या प्रोजेक्टच्या वापरासाठी नवीन टोकन तयार करा आणि `.env` फाईलमध्ये `HUGGING_FACE_API_KEY` चल अंतर्गत कॉपी करा. _टीप:_ हे तांत्रिकदृष्ट्या API की नाही परंतु प्रमाणीकरणासाठी वापरले जाते त्यामुळे आम्ही सातत्यासाठी ती नामकरण परंपरा ठेवत आहोत.

**अस्वीकृती**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अपूर्णता असू शकते. मूळ भाषेतील दस्तऐवज अधिकृत स्रोत म्हणून विचारात घेतला पाहिजे. महत्त्वपूर्ण माहितीसाठी, व्यावसायिक मानव अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.