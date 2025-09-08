<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:43:09+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "mr"
}
-->
# LLM प्रदाता निवडणे आणि कॉन्फिगर करणे 🔑

असाइनमेंट्स **कदाचित** एका किंवा अधिक मोठ्या भाषा मॉडेल (LLM) डिप्लॉयमेंटसह काम करण्यासाठी OpenAI, Azure किंवा Hugging Face सारख्या सपोर्टेड सर्व्हिस प्रोव्हायडरद्वारे सेटअप केली जाऊ शकतात. हे _होस्टेड एंडपॉइंट_ (API) पुरवतात, जे आपण योग्य क्रेडेन्शियल्स (API की किंवा टोकन) वापरून प्रोग्रामॅटिकली ऍक्सेस करू शकतो. या कोर्समध्ये, आपण हे प्रोव्हायडर्स पाहणार आहोत:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - विविध मॉडेल्ससह, मुख्य GPT सिरीजसह.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - OpenAI मॉडेल्ससाठी, एंटरप्राइज रेडिनेसवर लक्ष केंद्रित करून
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - ओपन-सोर्स मॉडेल्स आणि इन्फरन्स सर्व्हरसाठी

**या सरावांसाठी तुम्हाला स्वतःचे अकाउंट्स वापरावे लागतील**. असाइनमेंट्स ऐच्छिक आहेत, त्यामुळे तुम्ही एक, सर्व किंवा कोणताही प्रोव्हायडर सेटअप करायचा की नाही हे ठरवू शकता. साइनअपसाठी काही मार्गदर्शन:

| साइनअप | खर्च | API की | प्लेग्राउंड | टिप्पण्या |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [किंमत](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | एकाधिक मॉडेल्स उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [किंमत](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडिओ क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ऍक्सेससाठी आधी अर्ज करावा लागतो](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [किंमत](https://huggingface.co/pricing) | [ऍक्सेस टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मध्ये मर्यादित मॉडेल्स आहेत](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

खालील सूचना पाळा जेणेकरून हे रेपॉजिटरी वेगवेगळ्या प्रोव्हायडर्ससह वापरण्यासाठी _कॉन्फिगर_ करता येईल. ज्या असाइनमेंट्सना विशिष्ट प्रोव्हायडरची आवश्यकता आहे, त्यांच्या फाईलनावात हे टॅग असतील:

- `aoai` - Azure OpenAI एंडपॉइंट, की आवश्यक
- `oai` - OpenAI एंडपॉइंट, की आवश्यक
- `hf` - Hugging Face टोकन आवश्यक

तुम्ही एक, कोणताही किंवा सर्व प्रोव्हायडर्स कॉन्फिगर करू शकता. संबंधित असाइनमेंट्समध्ये जर क्रेडेन्शियल्स नसतील तर त्या एरर देतील.

## `.env` फाईल तयार करा

आम्ही गृहित धरतो की तुम्ही वरील मार्गदर्शन वाचले आहे आणि संबंधित प्रोव्हायडरकडे साइनअप करून आवश्यक ऑथेंटिकेशन क्रेडेन्शियल्स (API_KEY किंवा टोकन) मिळवले आहेत. Azure OpenAI च्या बाबतीत, आम्ही गृहित धरतो की तुमच्याकडे Azure OpenAI सर्व्हिसचे (एंडपॉइंट) वैध डिप्लॉयमेंट आहे आणि किमान एक GPT मॉडेल चॅट पूर्णतेसाठी डिप्लॉय केले आहे.

पुढील पायरी म्हणजे तुमचे **लोकल एन्व्हायर्नमेंट व्हेरिएबल्स** खालीलप्रमाणे कॉन्फिगर करणे:

1. रूट फोल्डरमध्ये `.env.copy` नावाची फाईल शोधा, ज्यात खालीलप्रमाणे कंटेंट असावा:

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

2. ती फाईल खालील कमांड वापरून `.env` नावाने कॉपी करा. ही फाईल _gitignore-d_ आहे, त्यामुळे सीक्रेट्स सुरक्षित राहतात.

   ```bash
   cp .env.copy .env
   ```

3. पुढील विभागात सांगितल्याप्रमाणे, व्हॅल्यूज भरा (उजव्या बाजूच्या placeholders बदलून).

4. (पर्यायी) जर तुम्ही GitHub Codespaces वापरत असाल, तर तुम्ही एन्व्हायर्नमेंट व्हेरिएबल्स _Codespaces secrets_ म्हणून या रेपॉजिटरीसह सेव्ह करू शकता. अशा वेळी, तुम्हाला लोकल .env फाईल सेटअप करण्याची गरज नाही. **पण, हे फक्त GitHub Codespaces वापरत असाल तरच लागू आहे.** जर तुम्ही Docker Desktop वापरत असाल, तरीही .env फाईल सेटअप करावी लागेल.

## `.env` फाईलमध्ये माहिती भरा

चला, व्हेरिएबल नावे काय दर्शवतात ते पटकन पाहूया:

| व्हेरिएबल  | वर्णन  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | हे तुमच्या प्रोफाइलमध्ये सेट केलेले यूजर ऍक्सेस टोकन आहे |
| OPENAI_API_KEY | हे non-Azure OpenAI एंडपॉइंटसाठी सर्व्हिस वापरण्याचे ऑथरायझेशन की आहे |
| AZURE_OPENAI_API_KEY | हे त्या सर्व्हिससाठी ऑथरायझेशन की आहे |
| AZURE_OPENAI_ENDPOINT | हे Azure OpenAI रिसोर्ससाठी डिप्लॉय केलेले एंडपॉइंट आहे |
| AZURE_OPENAI_DEPLOYMENT | हे _टेक्स्ट जनरेशन_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | हे _टेक्स्ट एम्बेडिंग्स_ मॉडेल डिप्लॉयमेंट एंडपॉइंट आहे |
| | |

टीप: शेवटची दोन Azure OpenAI व्हेरिएबल्स अनुक्रमे चॅट पूर्णता (टेक्स्ट जनरेशन) आणि व्हेक्टर सर्च (एम्बेडिंग्स) साठी डिफॉल्ट मॉडेल दर्शवतात. त्यांची सेटिंग संबंधित असाइनमेंट्समध्ये दिली जाईल.

## Azure कॉन्फिगर करा: पोर्टलमधून

Azure OpenAI एंडपॉइंट आणि की व्हॅल्यूज [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मध्ये मिळतील, तर तिथून सुरुवात करूया.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) वर जा
1. साइडबारमधील (डाव्या मेन्यूमधील) **Keys and Endpoint** पर्यायावर क्लिक करा.
1. **Show Keys** वर क्लिक करा - तुम्हाला KEY 1, KEY 2 आणि Endpoint असे दिसेल.
1. AZURE_OPENAI_API_KEY साठी KEY 1 ची व्हॅल्यू वापरा
1. AZURE_OPENAI_ENDPOINT साठी Endpoint ची व्हॅल्यू वापरा

आता, आपण डिप्लॉय केलेल्या विशिष्ट मॉडेल्ससाठी एंडपॉइंट्स मिळवूया.

1. Azure OpenAI रिसोर्ससाठी साइडबारमधील (डाव्या मेन्यूमधील) **Model deployments** पर्यायावर क्लिक करा.
1. डेस्टिनेशन पेजवर, **Manage Deployments** वर क्लिक करा

यामुळे तुम्ही Azure OpenAI Studio वेबसाइटवर जाल, जिथे खालीलप्रमाणे इतर व्हॅल्यूज मिळतील.

## Azure कॉन्फिगर करा: स्टुडिओमधून

1. वरीलप्रमाणे **तुमच्या रिसोर्समधून** [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) वर जा.
1. साइडबारमधील (डावीकडील) **Deployments** टॅबवर क्लिक करा, जेणेकरून सध्या डिप्लॉय केलेली मॉडेल्स दिसतील.
1. हवे असलेले मॉडेल डिप्लॉय केले नसेल, तर **Create new deployment** वापरून ते डिप्लॉय करा.
1. तुम्हाला _text-generation_ मॉडेल लागेल - आम्ही **gpt-35-turbo** सुचवतो
1. तुम्हाला _text-embedding_ मॉडेल लागेल - आम्ही **text-embedding-ada-002** सुचवतो

आता एन्व्हायर्नमेंट व्हेरिएबल्समध्ये _Deployment name_ प्रमाणे अपडेट करा. हे सहसा मॉडेलच्या नावासारखेच असेल, जोपर्यंत तुम्ही ते बदलले नसेल. उदाहरणार्थ, असे असू शकते:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**काम झाल्यावर .env फाईल सेव्ह करायला विसरू नका**. आता तुम्ही फाईलमधून बाहेर पडू शकता आणि नोटबुक चालवण्याच्या सूचनांकडे परत जाऊ शकता.

## OpenAI कॉन्फिगर करा: प्रोफाइलमधून

तुमची OpenAI API की [OpenAI अकाउंटमध्ये](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मिळेल. जर तुमच्याकडे की नसेल, तर अकाउंट तयार करा आणि API की जनरेट करा. की मिळाल्यावर, ती `.env` फाईलमधील `OPENAI_API_KEY` व्हेरिएबलमध्ये भरा.

## Hugging Face कॉन्फिगर करा: प्रोफाइलमधून

तुमचे Hugging Face टोकन [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) मध्ये प्रोफाइलमध्ये मिळेल. हे टोकन सार्वजनिकपणे पोस्ट किंवा शेअर करू नका. या प्रोजेक्टसाठी नवीन टोकन तयार करा आणि ते `.env` फाईलमधील `HUGGING_FACE_API_KEY` व्हेरिएबलमध्ये कॉपी करा. _टीप:_ हे तांत्रिकदृष्ट्या API की नाही, पण ऑथेंटिकेशनसाठी वापरले जाते, म्हणून नावात API_KEY ठेवले आहे.

---

**अस्वीकरण**:  
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अपूर्णता असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.