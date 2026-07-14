# LLM प्रदाता निवडणे व कॉन्फिगर करणे 🔑

असाइनमेंट्स **किंवा** मोठ्या भाषा मॉडेल (LLM) डिप्लॉयमेंट्ससाठी समर्थन करणार्‍या सेवा प्रदात्यांसारख्या OpenAI, Azure किंवा Hugging Face च्या माध्यमातून काम करण्यासाठी सेटअप केली जाऊ शकतात. हे _होस्टेड एंडपॉइंट_ (API) प्रदान करतात ज्याला योग्य प्रमाणपत्रांसहित (API की किंवा टोकन) प्रोग्रामॅटिकली प्रवेश करता येऊ शकतो. या कोर्समध्ये, आपण हे प्रदाते चर्चा करतो:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) मध्ये कोरस GPT सिरीजसह विविध मॉडेल्स आहेत.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) मध्ये OpenAI मॉडेल्ससाठी एंटरप्राइझ रेडीनेसवर लक्ष केंद्रित केले आहे.
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एका एंडपॉइंट आणि API किल्या द्वारे OpenAI, Meta, Mistral, Cohere, Microsoft व इतर अनेकांकडून शेकडो मॉडेल्स वापरण्यासाठी (GitHub Models ची जागा घेणारे, जे जुलै 2026 च्या शेवटी बंद होत आहे).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) मुक्त स्रोत मॉडेल्स आणि इन्फरन्स सर्व्हरसाठी
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) किंवा [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) जर तुम्हाला तुमच्या स्वतःच्या डिव्हाइसवर पूर्णपणे ऑफलाइन मॉडेल्स चालवायचे असतील, ज्यासाठी कोणतीही क्लाउड सबस्क्रिप्शन गरज नाही.

**या व्यायामांसाठी तुम्हाला तुमचे स्वतःचे खाते वापरावे लागेल**. असाइनमेंट्स ऐच्छिक असतात त्यामुळे तुम्ही तुमच्या आवडीवर आधारित एक, सर्व किंवा कोणतेही प्रदाते सेटअप करू शकता. काही नोंदींसाठी मार्गदर्शन:

| साइनअप | खर्च | API की | प्लेग्राउंड | टिप्पण्या |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रकल्प-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | अनेक मॉडेल्स उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडिओ क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [प्रवेशासाठी पूर्वमा अर्ज करणे आवश्यक आहे](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [प्रकल्प संदर्भ पृष्ठ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | मोफत स्तर उपलब्ध; अनेक मॉडेल प्रदात्यांसाठी एक एंडपॉइंट + की |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [ऍक्सेस टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | मोफत (तुमच्या डिव्हाइसमध्ये चालते) | आवश्यक नाही | [Local CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूर्णपणे ऑफलाइन, OpenAI-योग्य एंडपॉइंट |
| | | | | |

विविध प्रदात्यांसह वापरसाठी या रिपॉझिटरीचे _कॉन्फिगर_ करण्यासाठी खालील सूचना अवलंबा. विशिष्ट प्रदाता आवश्यक असलेल्या असाइनमेंट्सच्या फाईलच्या नावात खालील टॅगपैकी एक असतो:

- `aoai` - Azure OpenAI एंडपॉइंट, की आवश्यक
- `oai` - OpenAI एंडपॉइंट, की आवश्यक
- `hf` - Hugging Face टोकन आवश्यक
- `githubmodels` - Microsoft Foundry Models एंडपॉइंट, की आवश्यक (GitHub Models जुलै 2026 च्या शेवटी बंद होत आहे)

तुम्ही एक, कोणतेही किंवा सर्व प्रदाते कॉन्फिगर करू शकता. संबंधित असाइनमेंट्स आवश्यक प्रमाणपत्रे नसल्यास त्रुटी देतील.

## `.env` फाईल तयार करा

आम्ही गृहित धरतो की तुम्ही वरचे मार्गदर्शन वाचले आहे, संबंधित प्रदात्यासह साइन अप केले आहे, आणि आवश्यक प्रमाणपत्रे (API_KEY किंवा टोकन) प्राप्त केली आहेत. Azure OpenAI च्या बाबतीत, किमान एक GPT मॉडेल चॅट पूर्णतेसाठी डिप्लॉय केलेले Azure OpenAI सेवा (एंडपॉइंट) वैध आहे असे समजतो.

पुढील पाऊल म्हणजे तुमचे **स्थानिक पर्यावरणीय चल** पुढीलप्रमाणे कॉन्फिगर करणे:

1. मूळ फोल्डरमध्ये `.env.copy` नावाची फाईल शोधा, ज्यात खालीलप्रमाणे सामग्री असावी:

   ```bash
   # OpenAI प्रदाता
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## मायक्रोसॉफ्ट फाउंड्रीतील Azure OpenAI
   ## (Azure OpenAI सेवा आता मायक्रोसॉफ्ट फाउंड्रीचा भाग आहे: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # डीफॉल्ट सेट केले आहे! (सध्याचा स्थिर GA API आवृत्ती)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## मायक्रोसॉफ्ट फाउंड्री मॉडेल्स (मल्टी-प्रोव्हायडर मॉडेल कॅटलॉग, GitHub मॉडेल्सची जागा घेतो, जे जुलै 2026 च्या शेवटी बंद होणार आहे)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## हगिंग फेस
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. खालील आदेश वापरून ती फाईल `.env` मध्ये कॉपी करा. ही फाईल _gitignore_ करण्यात आलेली आहे, ज्यामुळे रहस्ये सुरक्षित राहतात.

   ```bash
   cp .env.copy .env
   ```

3. पुढील विभागात वर्णन केल्याप्रमाणे मूल्ये (=`च्या उजव्या बाजूच्या प्लेसहोल्डर`) भरा.

4. (पर्यायी) जर तुम्ही GitHub Codespaces वापरत असाल, तर या रिपॉझिटरीशी संबंधित _Codespaces secrets_ म्हणून पर्यावरणीय चल साठवण्याचा पर्याय आहे. अशा स्थितीत, तुम्हाला स्थानिक .env फाईल सेटअप करावी लागणार नाही. **पण, लक्षात ठेवा की हा पर्याय फक्त GitHub Codespaces वापरत असाल तेव्हाच चालतो.** जर तुम्ही Docker Desktop वापरत असाल तर अद्याप तुम्हाला .env फाईल सेटअप करावी लागेल.

## `.env` फाईल भरून पूर्ण करा

काय दर्शवतात ते समजून घेण्यासाठी चलांच्या नावांकडे थोडक्यात पाहूया:

| चलाचे नाव  | वर्णन  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हे वापरकर्त्याचे प्रवेश टोकन आहे जे तुम्ही तुमच्या प्रोफाइलमध्ये सेट केले आहे |
| OPENAI_API_KEY | हे सेवा वापरण्यासाठी प्राधिकरण की आहे, जे non-Azure OpenAI एंडपॉइंटसाठी वापरले जाते |
| AZURE_OPENAI_API_KEY | ही त्या सेवेचा प्राधिकरण की आहे |
| AZURE_OPENAI_ENDPOINT | ही Azure OpenAI संसाधनाची डिप्लॉय केलेली एंडपॉइंट आहे |
| AZURE_OPENAI_DEPLOYMENT | हा _टेक्स्ट जनरेशन_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | हा _टेक्स्ट एम्बेडिंग्ज_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| AZURE_INFERENCE_ENDPOINT | तुमच्या Microsoft Foundry प्रोजेक्टचा एंडपॉइंट, जे Microsoft Foundry Models साठी वापरले जाते |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry प्रोजेक्टसाठी API की |
| | |

नोंद: शेवटचे दोन Azure OpenAI बदलणारे एक साधा मॉडेल आहेत, एक चॅट पूर्ण करण्यासाठी (टेक्स्ट जनरेशन) आणि दुसरे व्हेक्टर शोधण्यासाठी (एम्बेडिंग्ज). त्यांची सेटिंग संबंधित असाइनमेंटमध्ये दिली जाईल.

## Azure OpenAI कॉन्फिगर करा: पोर्टलवरून

> **नोंद:** Azure OpenAI सेवा आता [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) चा भाग आहे. संसाधने आणि डिप्लॉयमेंट अजूनही Azure Portals मध्ये दिसतात, पण दररोजचे मॉडेल व्यवस्थापन (डिप्लॉयमेंट, प्लेग्राउंड, मॉनिटरिंग) आता Foundry पोर्टलमध्ये केले जाते, जुन्या स्वतंत्र "Azure OpenAI Studio" ऐवजी.

Azure OpenAI एंडपॉइंट आणि कीची मूल्ये [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये मिळतील, तर चला तेथून सुरू करूया.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा
1. साइडबारमध्ये (डाव्या मेनूमध्ये) **कीज आणि एंडपॉइंट** पर्यायावर क्लिक करा.
1. **कीज दाखवा** क्लिक करा - तुम्हाला KEY 1, KEY 2 आणि एंडपॉइंट दिसेल.
1. AZURE_OPENAI_API_KEY साठी KEY 1 चे मूल्य वापरा
1. AZURE_OPENAI_ENDPOINT साठी एंडपॉइंटचे मूल्य वापरा

नंतर, आपण डिप्लॉय केलेल्या विशिष्ट मॉडेल्ससाठी एंडपॉइंट्स पाहूया.

1. Azure OpenAI संसाधनासाठी साइडबारमध्ये (डावीकडील मेनूमध्ये) **मॉडेल डिप्लॉयमेंट्स** पर्यायावर क्लिक करा.
1. गन्तव्य पृष्ठावर, **Microsoft Foundry पोर्टलला जा** (किंवा **डिप्लॉयमेंट्स व्यवस्थापित करा**, संसाधन प्रकारानुसार) क्लिक करा

हे तुम्हाला Microsoft Foundry पोर्टलकडे नेतं, जिथून खालील प्रमाणे इतर मूल्ये शोधू.

## Azure OpenAI कॉन्फिगर करा: Microsoft Foundry पोर्टलवरून

1. [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) वर आपल्या संसाधनापासून साहजिकरीत्या प्रविष्ट व्हा.
1. **डिप्लॉयमेंट्स** टॅब (साइडबार, डावीकडे) वर क्लिक करा, जेथे सध्या डिप्लॉय केलेली मॉडेल्स दिसतील.
1. हवं असलेलं मॉडेल डिप्लॉय केलेले नसेल, तर [मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मधून **मॉडेल डिप्लॉय करा** वापरा.
1. तुम्हाला एक _टेक्स्ट जनरेशन_ मॉडेल पाहिजे - आम्ही सुचवतो: **gpt-4o-mini**
1. तुम्हाला एक _टेक्स्ट एम्बेडिंग्ज_ मॉडेल पाहिजे - आम्ही सुचवतो: **text-embedding-3-small**

आता पर्यावरणीय चलं तुमच्या _डिप्लॉयमेंट नावाने_ अपडेट करा, जे सामान्यतः मॉडेल नावासारखंच असते जोपर्यंत तुम्ही ते स्पष्टपणे बदलले नाही. उदाहरणार्थ, तुम्हाकडे असू शकते:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**पूर्ण झाल्यावर .env फाईल जतन करायला विसरू नका**. तुम्ही आता फाईल बंद करू शकता आणि नोटबुक चालवण्याच्या सूचनांकडे परत जाऊ शकता.

## OpenAI कॉन्फिगर करा: प्रोफाइलमधून

तुमची OpenAI API की तुमच्या [OpenAI खात्यामध्ये](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) सापडेल. जर तुमचं खाते नसेल, तर तुम्ही खाती तयार करून API की तयार करू शकता. की मिळाल्यानंतर तुम्ही ती `.env` फाईलमधील `OPENAI_API_KEY` मध्ये भरू शकता.

## Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

तुमचा Hugging Face टोकन तुमच्या प्रोफाइलमधील [ऍक्सेस टोकन्स](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) मध्ये असतो. हे सार्वजनिकपणे पोस्ट करू नका किंवा शेअर करू नका. त्याऐवजी ह्या प्रकल्पासाठी नवीन टोकन तयार करा आणि ते `.env` फाईलमधील `HUGGING_FACE_API_KEY` मध्ये कॉपी करा. _नोंद:_ हे तांत्रिकदृष्ट्या API की नाही, पण प्रमाणीकरणासाठी वापरले जाते, त्यामुळे नावाचा सुसंगती राखण्यासाठी ते अशाच नावाने ठेवले आहे.

## Microsoft Foundry Models कॉन्फिगर करा: पोर्टलवरून

> **नोंद:** GitHub Models जुलै 2026 च्या शेवटी बंद होत आहेत. Microsoft Foundry Models थेट पर्याय आहे, जो मोफत ट्रायसाठी मॉडेल कॅटलॉग आणि Azure AI Inference SDK / OpenAI SDK अनुभव देते.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) वर जा आणि Foundry प्रोजेक्ट तयार करा (किंवा उघडा).
1. [मॉडेल कॅटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) मध्ये शोध करा आणि उदाहरणार्थ `gpt-4o-mini` मॉडेल डिप्लॉय करा.
1. प्रोजेक्टच्या **अवलोकन** पृष्ठावरून **एंडपॉइंट** व **API की** कॉपी करा.
1. `.env` फाईलमधील `AZURE_INFERENCE_ENDPOINT` साठी एंडपॉइंटची मूल्ये आणि `AZURE_INFERENCE_CREDENTIAL` साठी कीचे मूल्य वापरा.

## ऑफलाईन / स्थानिक प्रदाते

जर तुम्हाला क्लाउड सबस्क्रिप्शन वापरायचं नसेल तर, तुम्ही तुमच्या स्वतःच्या डिव्हाइसवर थेट सुसंगत खुले मॉडेल्स चालवू शकता:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - मायक्रोसॉफ्टचा ऑन-डिव्हाइस रनटाइम. हा आपोआप सर्वोत्तम कार्यान्वयन प्रदाता (NPU, GPU, किंवा CPU) निवडतो आणि एक OpenAI-योग्य एंडपॉइंट देते, त्यामुळे तुम्हाला या कोर्समधील नमुना कोडवर सूक्ष्मतः बदल करून पुनर्वापर करता येईल. सुरुवात करण्यासाठी [Foundry Local दस्तऐवज](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) पहा, किंवा `winget install Microsoft.FoundryLocal` (विंडोज) / `brew install microsoft/foundrylocal/foundrylocal` (मॅकओएस) वापरून इन्स्टॉल करा.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral आणि Gemma सारख्या खुले मॉडेल्स स्थानिकपणे चालवण्यासाठी लोकप्रिय पर्याय.


दोन्ही पर्यायांसह व्यावहारिक उदाहरणांसाठी [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) पहा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->