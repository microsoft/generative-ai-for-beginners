# LLM प्रदाता निवडणे आणि संरचीत करणे 🔑

असाइनमेंट्स **कदाचित** OpenAI, Azure किंवा Hugging Face सारख्या समर्थीत सेवा प्रदात्या मार्फत एक किंवा अधिक Large Language Model (LLM) वितरणांवर काम करण्यासाठी देखील सेटअप केला जाऊ शकतो. हे एक _होस्ट केलेले एंडपॉइंट_ (API) प्रदान करतात ज्याला आम्ही योग्य प्रमाणपत्रांसह (API की किंवा टोकन) प्रोग्रामेटिकली प्रवेश करू शकतो. या कोर्समध्ये, आपण या प्रदात्यांबद्दल चर्चा करतो:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मॉडेल्ससह ज्यात कोर GPT मालिका समाविष्ट आहे.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडेल्ससाठी ज्यामध्ये एंटरप्राइझ तयार करण्यावर लक्ष केंद्रित आहे
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एकाच एंडपॉइंट आणि API कीद्वारे OpenAI, Meta, Mistral, Cohere, Microsoft आणि इतर अनेक मॉडेल्ससाठी प्रवेश (GitHub Models चे स्थान घेणारे, जे जुलै 2026 च्या शेवटी बंद होत आहे)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) मुक्त स्रोत मॉडेल्स आणि इनफरन्स सर्व्हरसाठी
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) किंवा [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) जर तुम्हाला मॉडेल पूर्णपणे ऑफलाइन तुमच्या स्वतःच्या डिव्हाइसवर चालवायचे असतील, कोणताही क्लाउड सबस्क्रिप्शन नको असेल तर

**तुम्हाला या व्यायामांसाठी तुमचे स्वतःचे खाते वापरावे लागेल**. असाइनमेंट्स ऐच्छिक आहेत म्हणून तुम्ही तुमच्या आवडींनुसार एक, सर्व किंवा कोणताही प्रदाता सेटअप करू शकता. काही नोंदी-नोंदणीसाठी मार्गदर्शन:

| नोंदणी | खर्च | API की | प्लेग्राउंड | टिप्पण्या |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्यनिर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | अनेक मॉडेल्स उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्यनिर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विक्स्टार्ट](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडिओ क्विक्स्टार्ट](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पूर्वपरवानगी आवश्यक](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [मूल्यनिर्धारण](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [प्रोजेक्ट विहंगावलोकन पृष्ठ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry प्लेग्राउंड](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | फुकट स्तर उपलब्ध; अनेक मॉडेल प्रदात्यांसाठी एक एंडपॉइंट + की |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्यनिर्धारण](https://huggingface.co/pricing) | [प्रवेश टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | मोफत (तुमच्या डिव्हाइसवर चालवते) | आवश्यक नाही | [लोकल CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूर्णपणे ऑफलाइन, OpenAI-योग्यतेचा एंडपॉइंट |
| | | | | |

वेगवेगळ्या प्रदात्यांसाठी _कॉन्फिगर_ करण्यासाठी खाली दिलेल्या सूचनांचे पालन करा. विशिष्ट प्रदात्याची गरज असलेले असाइनमेंट्स त्यांच्या फाइलनाम्ही यापैकी एक टॅग असतील:

- `aoai` - Azure OpenAI एंडपॉइंट, की आवश्यक
- `oai` - OpenAI एंडपॉइंट, की आवश्यक
- `hf` - Hugging Face टोकन आवश्यक
- `githubmodels` - Microsoft Foundry Models एंडपॉइंट, की आवश्यक (GitHub Models जुलै 2026 च्या शेवटी बंद होत आहे)

तुम्ही एक, काहीही नाही किंवा सर्व प्रदाते कॉन्फिगर करू शकता. संबंधित असाइनमेंट्स योग्य प्रमाणपत्रे नसल्यास फक्त त्रुटी दाखवतील.

## `.env` फाइल तयार करा

आम्ही गृहित धरतो की तुम्ही वरील मार्गदर्शन वाचलेले आहे आणि संबंधित प्रदात्यासह साइन अप केले आहे, आणि आवश्यक प्रमाणीकरण प्रमाणपत्रे (API_KEY किंवा टोकन) मिळवले आहेत. Azure OpenAI च्या बाबतीत, आम्ही गृहित धरतो की तुमच्याकडे Azure OpenAI सेवा (एंडपॉइंट) चे वैध वितरण आहे ज्यात किमान एक GPT मॉडेल चॅट पूर्णतेसाठी तैनात केलेले आहे.

पुढील टप्पा म्हणजे तुमच्या **लोकल पर्यावरण चल** खालीलप्रमाणे कॉन्फिगर करणे:

1. मूळ फोल्डरमध्ये `.env.copy` नावाची फाइल शोधा ज्यामध्ये अशी सामग्री असावी:

   ```bash
   # OpenAI प्रदाता
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry मधील Azure OpenAI
   ## (Azure OpenAI सेवा आता Microsoft Foundry चा भाग आहे: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # डीफॉल्ट सेट केले गेले आहे! (सध्याचा स्थिर GA API आवृत्ती)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry मॉडेल्स (मल्टी-प्रोव्हायडर मॉडेल कॅटलॉग, GitHub मॉडेल्स ची जागा घेतो, ज्याचा वापर जुलै 2026 च्या शेवटी बंद होईल)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. त्या फाइलला खालील आदेशाने `.env` मध्ये कॉपी करा. ही फाइल _gitignore-केली आहे_, म्हणजे गुपित सुरक्षित राहते.

   ```bash
   cp .env.copy .env
   ```

3. मूल्ये भरा (=` च्या उजव्या बाजूला असलेल्या प्लेसहोल्डर बदल करा) पुढील विभागात वर्णन केल्याप्रमाणे.

4. (पर्याय) जर तुम्ही GitHub Codespaces वापरत असाल, तर तुमच्याकडे या रेपॉजिटरीशी संबंधित _Codespaces secrets_ म्हणून पर्यावरण चल जतन करण्याचा पर्याय आहे. अशा परिस्थितीत, तुम्हाला लोकल .env फाइल सेटअप करणे आवश्यक नाही. **तथापि, लक्षात घ्या की हा पर्याय फक्त तुम्ही GitHub Codespaces वापरत असल्यास कार्य करतो.** जर तुम्ही Docker Desktop वापरत असाल तर तरीही .env फाइल सेटअप करावी लागेल.

## `.env` फाइलमध्ये मूल्ये भरा

चल नावे काय सूचित करतात हे समजून घेऊया:

| चल नाव  | वर्णन  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हा तुमच्या प्रोफाइलमध्ये सेट केलेला वापरकर्ता प्रवेश टोकन आहे |
| OPENAI_API_KEY | हा गैर-Azure OpenAI एंडपॉइंट्ससाठी सेवा वापरण्यासाठी अधिकृत की आहे |
| AZURE_OPENAI_API_KEY | हि त्या सेवेची अधिकृत की आहे |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI स्त्रोतासाठी तैनात केलेला एंडपॉइंट आहे |
| AZURE_OPENAI_DEPLOYMENT | _टेक्स्ट जनरेशन_ मॉडेल वितरण एंडपॉइंट आहे |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _टेक्स्ट एम्बेडिंग्स_ मॉडेल वितरण एंडपॉइंट आहे |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry प्रोजेक्टसाठी एंडपॉइंट, ज्याचा उपयोग Microsoft Foundry Models साठी होतो |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry प्रोजेक्टसाठी API की आहे |
| | |

टीप: शेवटचे दोन Azure OpenAI चल चॅट पूर्णतेसाठी (टेक्स्ट जनरेशन) आणि व्हेक्टर शोधासाठी (एम्बेडिंग्स) अनुक्रमे डीफॉल्ट मॉडेल प्रतिबिंबित करतात. त्यांना सेट करण्याचे निर्देश संबंधित असाइनमेंट्समध्ये दिले जातील.

## Azure OpenAI कॉन्फिगर करा: पोर्टलमधून

> **टीप:** Azure OpenAI सेवा आता [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) चा भाग आहे. स्त्रोत आणि वितरण अजूनही Azure पोर्टलकडे दिसतात, पण रोजच्या मॉडेल व्यवस्थापनाचे (वितरण, प्लेग्राउंड, मॉनिटरिंग) काम आता जुना स्वतंत्र "Azure OpenAI Studio" च्या ऐवजी Foundry पोर्टलमध्ये होते.

Azure OpenAI एंडपॉइंट आणि की मूल्ये [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये मिळतील; चला तेथे सुरू करूया.

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा
1. साईडबारमध्ये (डाव्या बाजूला मेनू) **की आणि एंडपॉइंट** पर्याय क्लिक करा.
1. **की दाखवा** क्लिक करा - तुम्हाला पुढील दिसेल: KEY 1, KEY 2 आणि Endpoints.
1. AZURE_OPENAI_API_KEY साठी KEY 1 मूल्य वापरा
1. AZURE_OPENAI_ENDPOINT साठी Endpoint मूल्य वापरा

आता, आपण तैनात केलेल्या विशिष्ट मॉडेलसाठी एंडपॉइंट्सची गरज आहे.

1. Azure OpenAI स्त्रोतासाठी साइडबारमध्ये (डाव्या मेनूमध्ये) **मॉडेल वितरण** पर्याय क्लिक करा.
1. लक्ष्य पृष्ठावर, **Microsoft Foundry पोर्टलवर जा** (किंवा **Deployments व्यवस्थापित करा**, तुमच्या स्त्रोत प्रकारानुसार)

हे तुम्हाला Microsoft Foundry पोर्टलवर घेऊन जाईल, जिथे आपण खाली वर्णन केलेली इतर मूल्ये शोधणार आहोत.

## Azure OpenAI कॉन्फिगर करा: Microsoft Foundry पोर्टलवरून

1. वरीलप्रमाणे तुमच्या स्त्रोतातून [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) वर जा.
1. सध्या तैनात केलेल्या मॉडेल्स पाहण्यासाठी साइडबारमधील (डावा) **Deployments** टॅब क्लिक करा.
1. जर तुमचे इच्छित मॉडेल तैनात नसेल, तर [मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मधून ते तैनात करण्यासाठी **Deploy model** वापरा.
1. तुम्हाला एक _टेक्स्ट-जनरेशन_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो: **gpt-5-mini**
1. तुम्हाला एक _टेक्स्ट-एम्बेडिंग_ मॉडेल आवश्यक आहे - आम्ही शिफारस करतो **text-embedding-3-small**

आता पर्यावरण चल अपडेट करा जेणेकरून वापरलेले _Deployment नाव_ प्रतिबिंबित होईल. सहसा हे मॉडेल नावासारखेच असेल जोपर्यंत तुम्ही ते खुल्या रितीने बदलले नाही. उदाहरणार्थ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**कार्य पूर्ण केल्यानंतर .env फाइल सेव्ह करायला विसरू नका**. आता तुम्ही फाइल बंद करू शकता आणि नोटबुक चालवण्यासाठी सूचनांकडे परत जाऊ शकता.

## OpenAI कॉन्फिगर करा: प्रोफाइलमधून

तुमची OpenAI API की तुमच्या [OpenAI खात्यात](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) सापडेल. जर तुमच्याकडे नसेल, तर तुम्ही खाते तयार करून API की बनवू शकता. एकदा की मिळाल्यानंतर, `.env` फाइलमधील `OPENAI_API_KEY` चल भरण्यासाठी ते वापरा.

## Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

तुमचा Hugging Face टोकन तुमच्या प्रोफाइलमध्ये [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अंतर्गत सापडेल. यांना सार्वजनिकरित्या पोस्ट किंवा शेअर करू नका. त्याऐवजी, या प्रोजेक्टसाठी नवीन टोकन तयार करा आणि ते `.env` फाईलमधील `HUGGING_FACE_API_KEY` चलाखाली कॉपी करा. _टीप:_ तांत्रिकदृष्ट्या ही API की नाही परंतु प्रमाणीकरणासाठी वापरली जाते म्हणून सुसंगततेसाठी त्याच नावाने ठेवले आहे.

## Microsoft Foundry Models कॉन्फिगर करा: पोर्टलमधून

> **टीप:** GitHub Models जुलै 2026 च्या शेवटी बंद होत आहे. Microsoft Foundry Models थेट पर्याय आहे, ज्यामुळे समान फ्री-टू-ट्राय मॉडेल कॅटलॉग आणि Azure AI Inference SDK / OpenAI SDK अनुभव मिळतो.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) वर जा आणि Foundry प्रोजेक्ट तयार करा (किंवा उघडा).
1. [मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ब्राउज करा आणि उदाहरणार्थ `gpt-5-mini` मॉडल तैनात करा.
1. प्रोजेक्टच्या **विहंगावलोकन** पृष्ठावरून, **एंडपॉइंट** आणि **API की** कॉपी करा.
1. `.env` फाइलमध्ये `AZURE_INFERENCE_ENDPOINT` साठी एंडपॉइंट मूल्य आणि `AZURE_INFERENCE_CREDENTIAL` साठी की मूल्य वापरा.

## ऑफलाइन / लोकल प्रदाते

जर तुम्हाला क्लाउड सदस्यता वापरायची नसेल, तर तुम्ही तुमच्या स्वतःच्या डिव्हाइसवर थेट सुसंगत मुक्त मॉडेल चालवू शकता:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft चे ऑन-डिव्हाइस रनटाइम. हे आपोआप सर्वोत्तम अंमलबजावणी प्रदाता (NPU, GPU, किंवा CPU) निवडते आणि OpenAI-सुसंगत एंडपॉइंट प्रदान करते, त्यामुळे तुम्ही या कोर्समधील नमुना कोडमध्ये थोड्याफार बदलांबरोबर पुनर्वापर करू शकता. सुरू करण्यासाठी [Foundry Local दस्तऐवज](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) पहा, किंवा `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) वापरून इन्स्टॉल करा.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral आणि Gemma सारख्या मुक्त मॉडेल्सना स्थानिकपणे चालवण्यासाठी लोकप्रिय पर्याय.


कृपया दोन्ही पर्याय वापरण्यासाठी प्रत्यक्ष उदाहरणांसाठी [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) पाहा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->