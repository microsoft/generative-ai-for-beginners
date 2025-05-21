<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:44:40+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mr"
}
-->
# तुमचे देव वातावरण सेटअप करा

आम्ही या रिपॉझिटरी आणि कोर्ससाठी एक [विकसनशील कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) सेटअप केला आहे ज्यामध्ये Python3, .NET, Node.js आणि Java विकासाला समर्थन देणारा युनिव्हर्सल रनटाइम आहे. संबंधित कॉन्फिगरेशन `devcontainer.json` फाइलमध्ये परिभाषित आहे जी या रिपॉझिटरीच्या मुळामध्ये `.devcontainer/` फोल्डरमध्ये आहे.

डेव कंटेनर सक्रिय करण्यासाठी, [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड रनटाइमसाठी) किंवा [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (स्थानिक डिव्हाइस-होस्टेड रनटाइमसाठी) मध्ये लॉन्च करा. VS Code मध्ये डेव कंटेनर कसे कार्य करतात याबद्दल अधिक तपशीलांसाठी [हे दस्तऐवजीकरण](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) वाचा.

> [!TIP]  
> कमी प्रयत्नात जलद सुरुवातीसाठी GitHub Codespaces वापरण्याची शिफारस आम्ही करतो. हे वैयक्तिक खात्यांसाठी उदार [मोफत वापर कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान करते. तुमचा कोटा वापर वाढवण्यासाठी निष्क्रिय कोडस्पेसेस थांबवण्यासाठी किंवा हटवण्यासाठी [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कॉन्फिगर करा.

## 1. असाइनमेंट्स कार्यान्वित करणे

प्रत्येक धडा मध्ये _ऐच्छिक_ असाइनमेंट्स असतील ज्यात एक किंवा अधिक प्रोग्रामिंग भाषा वापरल्या जाऊ शकतात: Python, .NET/C#, Java आणि JavaScript/TypeScript. या विभागात त्या असाइनमेंट्स कार्यान्वित करण्यासंबंधी सामान्य मार्गदर्शन दिले आहे.

### 1.1 Python असाइनमेंट्स

Python असाइनमेंट्स ऍप्लिकेशन्स (`.py` फाइल्स) किंवा Jupyter नोटबुक्स (`.ipynb` फाइल्स) म्हणून दिले जातात.
- नोटबुक चालवण्यासाठी, Visual Studio Code मध्ये ते उघडा आणि _Select Kernel_ (वर उजवीकडे) क्लिक करा आणि दर्शविलेला डीफॉल्ट Python 3 पर्याय निवडा. तुम्ही आता _Run All_ क्लिक करून नोटबुक चालवू शकता.
- कमांड-लाइन वरून Python ऍप्लिकेशन्स चालवण्यासाठी, योग्य फाइल्स निवडण्यासाठी आणि आवश्यक आर्ग्युमेंट्स प्रदान करण्यासाठी असाइनमेंट-विशिष्ट सूचनांचे पालन करा.

## 2. प्रदात्यांचे कॉन्फिगरेशन करणे

असाइनमेंट्स **कदाचित** एक किंवा अधिक मोठ्या भाषा मॉडेल (LLM) डिप्लॉयमेंट्स विरुद्ध कार्य करण्यासाठी OpenAI, Azure किंवा Hugging Face सारख्या समर्थित सेवा प्रदात्याद्वारे सेटअप केले जातील. हे एक _होस्टेड एंडपॉइंट_ (API) प्रदान करतात ज्यामध्ये योग्य क्रेडेन्शियल्स (API की किंवा टोकन) सह प्रोग्रामेटिकली प्रवेश केला जाऊ शकतो. या कोर्समध्ये, आम्ही या प्रदात्यांचा विचार करतो:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मॉडेल्ससह ज्यात मुख्य GPT मालिका आहे.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडेल्ससाठी जे एंटरप्राइज रेडीनेसवर लक्ष केंद्रित करते
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडेल्स आणि इनफेरन्स सर्व्हरसाठी

**तुम्हाला या व्यायामांसाठी तुमचे स्वतःचे खाते वापरणे आवश्यक आहे**. असाइनमेंट्स ऐच्छिक आहेत म्हणून तुम्ही तुमच्या आवडींनुसार एक, सर्व - किंवा काहीही सेटअप करण्याचे निवडू शकता. साइनअपसाठी काही मार्गदर्शन:

| साइनअप | खर्च | API की | प्लेग्राउंड | टिप्पण्या |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [किंमत](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | अनेक मॉडेल्स उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [किंमत](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK जलद प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडिओ जलद प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [प्रवेशासाठी आधी अर्ज करणे आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [किंमत](https://huggingface.co/pricing) | [ऍक्सेस टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

खालील निर्देशांचे अनुसरण करा या रिपॉझिटरीला विविध प्रदात्यांसह वापरण्यासाठी _कॉन्फिगर_ करण्यासाठी. विशिष्ट प्रदात्याची आवश्यकता असलेल्या असाइनमेंट्स त्यांच्या फाइलनाममध्ये या टॅग्सपैकी एक असतील:
 - `aoai` - Azure OpenAI एंडपॉइंट, की आवश्यक आहे
 - `oai` - OpenAI एंडपॉइंट, की आवश्यक आहे
 - `hf` - Hugging Face टोकन आवश्यक आहे

तुम्ही एक, काहीही किंवा सर्व प्रदाते कॉन्फिगर करू शकता. संबंधित असाइनमेंट्स फक्त अनुपस्थित क्रेडेन्शियल्सवर त्रुटी दर्शवतील.

### 2.1. `.env` फाइल तयार करा

आम्ही मानतो की तुम्ही वरील मार्गदर्शन आधीच वाचले आहे आणि संबंधित प्रदात्यांसह साइन अप केले आहे आणि आवश्यक प्रमाणीकरण क्रेडेन्शियल्स (API_KEY किंवा टोकन) मिळवले आहे. Azure OpenAI च्या बाबतीत, आम्ही मानतो की तुमच्याकडे किमान एक GPT मॉडेल चॅट पूर्ण करण्यासाठी तैनात केलेल्या Azure OpenAI सेवा (एंडपॉइंट) ची वैध तैनाती देखील आहे.

पुढील चरण तुमच्या **स्थानिक पर्यावरणीय व्हेरिएबल्स** कॉन्फिगर करणे आहे:

1. मुख्य फोल्डरमध्ये `.env.copy` फाइल पहा ज्यामध्ये खालीलप्रमाणे सामग्री असावी:

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

2. खालील आदेश वापरून ती फाइल `.env` मध्ये कॉपी करा. ही फाइल _gitignore-d_ आहे, गुपिते सुरक्षित ठेवण्यासाठी.

   ```bash
   cp .env.copy .env
   ```

3. पुढील विभागात वर्णन केल्याप्रमाणे मूल्ये भरा ( `=` च्या उजव्या बाजूला placeholders बदला).

3. (पर्याय) तुम्ही GitHub Codespaces वापरत असल्यास, तुम्हाला या रिपॉझिटरीशी संबंधित पर्यावरणीय व्हेरिएबल्स _Codespaces secrets_ म्हणून सेव्ह करण्याचा पर्याय आहे. त्या बाबतीत, तुम्हाला स्थानिक .env फाइल सेटअप करण्याची आवश्यकता नाही. **तथापि, लक्षात ठेवा की हा पर्याय फक्त तुम्ही GitHub Codespaces वापरत असल्यास कार्य करतो.** तुम्ही Docker Desktop वापरत असल्यास तुम्हाला तरीही .env फाइल सेटअप करणे आवश्यक आहे.

### 2.2. `.env` फाइल भरा

व्हेरिएबल्स काय दर्शवतात हे समजण्यासाठी चल नावांकडे जलद दृष्टीक्षेप टाकूया:

| व्हेरिएबल | वर्णन |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हे तुमच्या प्रोफाइलमध्ये सेट केलेले वापरकर्ता ऍक्सेस टोकन आहे |
| OPENAI_API_KEY | हे non-Azure OpenAI एंडपॉइंट्ससाठी सेवा वापरण्याचे अधिकृत की आहे |
| AZURE_OPENAI_API_KEY | हे त्या सेवेसाठी वापरण्याचे अधिकृत की आहे |
| AZURE_OPENAI_ENDPOINT | हे Azure OpenAI संसाधनासाठी तैनात एंडपॉइंट आहे |
| AZURE_OPENAI_DEPLOYMENT | हे _टेक्स्ट जनरेशन_ मॉडेल तैनाती एंडपॉइंट आहे |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | हे _टेक्स्ट एम्बेडिंग्स_ मॉडेल तैनाती एंडपॉइंट आहे |
| | |

टीप: शेवटचे दोन Azure OpenAI व्हेरिएबल्स एक डीफॉल्ट मॉडेल चॅट पूर्ण करण्यासाठी (टेक्स्ट जनरेशन) आणि व्हेक्टर शोध (एम्बेडिंग्स) साठी दर्शवतात. त्यांना सेट करण्याच्या सूचना संबंधित असाइनमेंट्समध्ये परिभाषित केल्या जातील.

### 2.3 Azure कॉन्फिगर करा: पोर्टलमधून

Azure OpenAI एंडपॉइंट आणि की मूल्ये [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये सापडतील म्हणून चला तेथे सुरुवात करूया.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा
1. साइडबार (डाव्या मेनू) मध्ये **Keys and Endpoint** पर्याय क्लिक करा.
1. **Show Keys** क्लिक करा - तुम्हाला खालीलप्रमाणे दिसेल: KEY 1, KEY 2 आणि Endpoint.
1. AZURE_OPENAI_API_KEY साठी KEY 1 मूल्य वापरा
1. AZURE_OPENAI_ENDPOINT साठी Endpoint मूल्य वापरा

पुढे, आपण तैनात केलेल्या विशिष्ट मॉडेल्ससाठी एंडपॉइंट्स आवश्यक आहेत.

1. Azure OpenAI संसाधनासाठी साइडबार (डाव्या मेनू) मध्ये **Model deployments** पर्याय क्लिक करा.
1. गंतव्य पृष्ठावर, **Manage Deployments** क्लिक करा

हे तुम्हाला Azure OpenAI Studio वेबसाइटवर घेऊन जाईल, जिथे आम्हाला खाली वर्णन केल्याप्रमाणे इतर मूल्ये सापडतील.

### 2.4 Azure कॉन्फिगर करा: स्टुडिओमधून

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **तुमच्या संसाधनातून** वर वर्णन केल्याप्रमाणे नेव्हिगेट करा.
1. साइडबार, डाव्या बाजूस **Deployments** टॅब क्लिक करा, सध्या तैनात मॉडेल्स पाहण्यासाठी.
1. तुमचे इच्छित मॉडेल तैनात नसल्यास, **Create new deployment** वापरून ते तैनात करा.
1. तुम्हाला _टेक्स्ट जनरेशन_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो: **gpt-35-turbo**
1. तुम्हाला _टेक्स्ट एम्बेडिंग_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो **text-embedding-ada-002**

आता पर्यावरणीय व्हेरिएबल्स अपडेट करा जे तैनाती नाव दर्शवतात. हे सहसा मॉडेल नावासारखेच असेल, जोपर्यंत तुम्ही ते स्पष्टपणे बदलले नाही. म्हणून, उदाहरण म्हणून, तुमच्याकडे असे असू शकते:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**पूर्ण झाल्यावर .env फाइल सेव्ह करायला विसरू नका**. तुम्ही आता फाइल बंद करू शकता आणि नोटबुक चालवण्याच्या सूचनांकडे परत जाऊ शकता.

### 2.5 OpenAI कॉन्फिगर करा: प्रोफाइलमधून

तुमची OpenAI API की तुमच्या [OpenAI खात्यामध्ये](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) सापडू शकते. तुम्हाला एक नसल्यास, तुम्ही खाते तयार करू शकता आणि API की तयार करू शकता. एकदा तुम्हाला की मिळाल्यानंतर, तुम्ही `.env` फाइलमध्ये `OPENAI_API_KEY` व्हेरिएबल भरण्यासाठी वापरू शकता.

### 2.6 Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

तुमचे Hugging Face टोकन तुमच्या प्रोफाइलमध्ये [ऍक्सेस टोकन्स](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अंतर्गत सापडू शकते. हे सार्वजनिकपणे पोस्ट किंवा शेअर करू नका. त्याऐवजी, या प्रकल्पाच्या वापरासाठी नवीन टोकन तयार करा आणि `.env` फाइलमध्ये `HUGGING_FACE_API_KEY` व्हेरिएबल अंतर्गत कॉपी करा. _टीप:_ हे तांत्रिकदृष्ट्या API की नाही परंतु प्रमाणीकरणासाठी वापरले जाते म्हणून आम्ही सुसंगततेसाठी ती नामकरण पद्धती ठेवत आहोत.

**अस्वीकृती**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला गेला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार नाही.