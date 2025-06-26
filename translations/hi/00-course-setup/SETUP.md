<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:12:16+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hi"
}
-->
# अपने डेवलपमेंट एनवायरनमेंट को सेटअप करें

हमने इस रिपॉजिटरी और कोर्स को एक [डेवलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) के साथ सेटअप किया है, जिसमें एक यूनिवर्सल रनटाइम है जो Python3, .NET, Node.js और Java डेवलपमेंट का समर्थन कर सकता है। संबंधित कॉन्फ़िगरेशन इस रिपॉजिटरी की जड़ में स्थित `.devcontainer/` फोल्डर में `devcontainer.json` फाइल में परिभाषित है।

डेवलपमेंट कंटेनर को सक्रिय करने के लिए, इसे [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड रनटाइम के लिए) या [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (लोकल डिवाइस-होस्टेड रनटाइम के लिए) में लॉन्च करें। VS Code के भीतर डेवलपमेंट कंटेनर कैसे काम करते हैं, इस पर अधिक विवरण के लिए [यह दस्तावेज़](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) पढ़ें।

> [!TIP]  
> हम एक त्वरित शुरुआत के लिए GitHub Codespaces का उपयोग करने की सिफारिश करते हैं। यह व्यक्तिगत खातों के लिए एक उदार [मुफ्त उपयोग कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान करता है। अपने कोटा उपयोग को अधिकतम करने के लिए निष्क्रिय कोडस्पेस को रोकने या हटाने के लिए [टाइमआउट्स](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) को कॉन्फ़िगर करें।

## 1. असाइनमेंट निष्पादित करना

प्रत्येक पाठ में _वैकल्पिक_ असाइनमेंट होंगे जो एक या अधिक प्रोग्रामिंग भाषाओं में प्रदान किए जा सकते हैं, जिनमें शामिल हैं: Python, .NET/C#, Java और JavaScript/TypeScript। यह अनुभाग उन असाइनमेंट को निष्पादित करने से संबंधित सामान्य मार्गदर्शन प्रदान करता है।

### 1.1 पायथन असाइनमेंट

पायथन असाइनमेंट या तो एप्लिकेशन (`.py` फाइलें) या Jupyter नोटबुक (`.ipynb` फाइलें) के रूप में प्रदान की जाती हैं।
- नोटबुक चलाने के लिए, इसे Visual Studio Code में खोलें, फिर _Select Kernel_ (ऊपर दाएं) पर क्लिक करें और दिखाए गए डिफ़ॉल्ट पायथन 3 विकल्प का चयन करें। अब आप नोटबुक को निष्पादित करने के लिए _Run All_ कर सकते हैं।
- कमांड-लाइन से पायथन एप्लिकेशन चलाने के लिए, सुनिश्चित करें कि आप सही फाइलों का चयन करें और आवश्यक तर्क प्रदान करें, इसके लिए असाइनमेंट-विशिष्ट निर्देशों का पालन करें।

## 2. प्रदाताओं को कॉन्फ़िगर करना

असाइनमेंट **शायद** एक या अधिक बड़े भाषा मॉडल (LLM) डिप्लॉयमेंट के साथ काम करने के लिए सेटअप किए जा सकते हैं, जैसे OpenAI, Azure या Hugging Face जैसी समर्थित सेवा प्रदाता के माध्यम से। ये एक _होस्टेड एंडपॉइंट_ (API) प्रदान करते हैं, जिसे हम सही क्रेडेंशियल्स (API कुंजी या टोकन) के साथ प्रोग्रामेटिक रूप से एक्सेस कर सकते हैं। इस कोर्स में, हम इन प्रदाताओं पर चर्चा करते हैं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विभिन्न मॉडलों के साथ जिसमें मुख्य GPT श्रृंखला शामिल है।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) उद्यम तैयारी पर ध्यान केंद्रित करते हुए OpenAI मॉडलों के लिए
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडल और इन्फेरेंस सर्वर के लिए

**इन अभ्यासों के लिए आपको अपने स्वयं के खाते का उपयोग करने की आवश्यकता होगी।** असाइनमेंट वैकल्पिक हैं इसलिए आप अपनी रुचियों के आधार पर एक, सभी - या कोई भी प्रदाता सेटअप करने का चयन कर सकते हैं। साइनअप के लिए कुछ मार्गदर्शन:

| साइनअप | लागत | API कुंजी | प्लेग्राउंड | टिप्पणियाँ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल उपलब्ध हैं |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK त्वरित प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टूडियो त्वरित प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले से एक्सेस के लिए आवेदन करना आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [एक्सेस टोकन](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging चैट](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging चैट में सीमित मॉडल हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

विभिन्न प्रदाताओं के साथ उपयोग के लिए इस रिपॉजिटरी को _कॉन्फ़िगर_ करने के लिए नीचे दिए गए निर्देशों का पालन करें। जिन असाइनमेंट को किसी विशेष प्रदाता की आवश्यकता होगी, उनके फाइलनाम में इनमें से एक टैग होगा:
 - `aoai` - Azure OpenAI एंडपॉइंट, कुंजी की आवश्यकता है
 - `oai` - OpenAI एंडपॉइंट, कुंजी की आवश्यकता है
 - `hf` - Hugging Face टोकन की आवश्यकता है

आप एक, कोई नहीं, या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट बस क्रेडेंशियल्स की कमी पर त्रुटि देंगे।

### 2.1. `.env` फाइल बनाएं

हम मानते हैं कि आपने ऊपर दिए गए मार्गदर्शन को पहले ही पढ़ लिया है और संबंधित प्रदाता के साथ साइन अप किया है, और आवश्यक प्रमाणीकरण क्रेडेंशियल्स (API_KEY या टोकन) प्राप्त किए हैं। Azure OpenAI के मामले में, हम मानते हैं कि आपके पास कम से कम एक GPT मॉडल के साथ एक वैध Azure OpenAI सेवा (एंडपॉइंट) की तैनाती है।

अगला कदम आपके **स्थानीय पर्यावरण चर** को निम्नानुसार कॉन्फ़िगर करना है:

1. जड़ फ़ोल्डर में एक `.env.copy` फाइल देखें, जिसमें इस प्रकार की सामग्री होनी चाहिए:

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

2. नीचे दिए गए कमांड का उपयोग करके उस फाइल को `.env` में कॉपी करें। यह फाइल _gitignore-d_ है, जो रहस्यों को सुरक्षित रखती है।

   ```bash
   cp .env.copy .env
   ```

3. अगला सेक्शन में वर्णित अनुसार मान भरें (बाईं ओर के `=` पर प्लेसहोल्डर्स को बदलें)।

3. (विकल्प) यदि आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास इस रिपॉजिटरी से संबंधित _Codespaces secrets_ के रूप में पर्यावरण चर को सहेजने का विकल्प है। उस स्थिति में, आपको स्थानीय .env फाइल सेटअप करने की आवश्यकता नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प केवल तभी काम करता है जब आप GitHub Codespaces का उपयोग करते हैं।** यदि आप Docker Desktop का उपयोग करते हैं, तो भी आपको .env फाइल सेटअप करने की आवश्यकता होगी।

### 2.2. `.env` फाइल को भरें

आइए जल्दी से वेरिएबल नामों पर नज़र डालें ताकि यह समझ सकें कि वे क्या दर्शाते हैं:

| वेरिएबल  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह वह उपयोगकर्ता एक्सेस टोकन है जिसे आपने अपनी प्रोफ़ाइल में सेटअप किया है |
| OPENAI_API_KEY | यह सेवा का उपयोग करने के लिए गैर-Azure OpenAI एंडपॉइंट्स के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_API_KEY | यह सेवा का उपयोग करने के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI संसाधन के लिए तैनात एंडपॉइंट है |
| AZURE_OPENAI_DEPLOYMENT | यह _टेक्स्ट जेनरेशन_ मॉडल तैनाती एंडपॉइंट है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _टेक्स्ट एंबेडिंग्स_ मॉडल तैनाती एंडपॉइंट है |
| | |

नोट: अंतिम दो Azure OpenAI वेरिएबल्स क्रमशः चैट पूर्णता (टेक्स्ट जेनरेशन) और वेक्टर खोज (एंबेडिंग्स) के लिए एक डिफ़ॉल्ट मॉडल को दर्शाते हैं। उन्हें सेट करने के लिए निर्देश संबंधित असाइनमेंट में परिभाषित किए जाएंगे।

### 2.3 Azure को कॉन्फ़िगर करें: पोर्टल से

Azure OpenAI एंडपॉइंट और कुंजी मान [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में पाए जाएंगे, इसलिए आइए वहां से शुरू करें।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं
1. साइडबार (बाएं मेनू) में **Keys and Endpoint** विकल्प पर क्लिक करें।
1. **Show Keys** पर क्लिक करें - आपको निम्नलिखित देखना चाहिए: KEY 1, KEY 2 और Endpoint।
1. AZURE_OPENAI_API_KEY के लिए KEY 1 मान का उपयोग करें
1. AZURE_OPENAI_ENDPOINT के लिए एंडपॉइंट मान का उपयोग करें

अगला, हमें उन विशिष्ट मॉडलों के लिए एंडपॉइंट्स की आवश्यकता है जिन्हें हमने तैनात किया है।

1. Azure OpenAI संसाधन के लिए साइडबार (बाएं मेनू) में **Model deployments** विकल्प पर क्लिक करें।
1. गंतव्य पृष्ठ पर, **Manage Deployments** पर क्लिक करें

यह आपको Azure OpenAI स्टूडियो वेबसाइट पर ले जाएगा, जहां हम नीचे वर्णित अन्य मान पाएंगे।

### 2.4 Azure को कॉन्फ़िगर करें: स्टूडियो से

1. [Azure OpenAI स्टूडियो](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) पर **अपने संसाधन से** जैसा कि ऊपर वर्णित है, नेविगेट करें।
1. वर्तमान में तैनात मॉडल देखने के लिए **Deployments** टैब (साइडबार, बाएं) पर क्लिक करें।
1. यदि आपका वांछित मॉडल तैनात नहीं है, तो इसे तैनात करने के लिए **Create new deployment** का उपयोग करें।
1. आपको एक _टेक्स्ट-जेनरेशन_ मॉडल की आवश्यकता होगी - हम अनुशंसा करते हैं: **gpt-35-turbo**
1. आपको एक _टेक्स्ट-एंबेडिंग_ मॉडल की आवश्यकता होगी - हम अनुशंसा करते हैं **text-embedding-ada-002**

अब पर्यावरण चर को परिलक्षित करने के लिए _Deployment name_ का उपयोग करके अपडेट करें। यह आमतौर पर मॉडल नाम के समान होगा जब तक कि आपने इसे स्पष्ट रूप से नहीं बदला। तो, उदाहरण के लिए, आपके पास हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**जब हो जाए तो .env फाइल को सहेजना न भूलें**। अब आप फाइल से बाहर निकल सकते हैं और नोटबुक चलाने के निर्देशों पर वापस जा सकते हैं।

### 2.5 OpenAI को कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी OpenAI API कुंजी आपके [OpenAI खाते](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में पाई जा सकती है। यदि आपके पास एक नहीं है, तो आप एक खाता साइन अप कर सकते हैं और एक API कुंजी बना सकते हैं। एक बार जब आपके पास कुंजी हो, तो आप इसे `.env` फाइल में `OPENAI_API_KEY` वेरिएबल में भरने के लिए उपयोग कर सकते हैं।

### 2.6 Hugging Face को कॉन्फ़िगर करें: प्रोफ़ाइल से

आपका Hugging Face टोकन आपके प्रोफ़ाइल में [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) के अंतर्गत पाया जा सकता है। इन्हें सार्वजनिक रूप से पोस्ट या साझा न करें। इसके बजाय, इस प्रोजेक्ट उपयोग के लिए एक नया टोकन बनाएं और इसे `.env` फाइल में `HUGGING_FACE_API_KEY` वेरिएबल के अंतर्गत कॉपी करें। _नोट:_ यह तकनीकी रूप से एक API कुंजी नहीं है, लेकिन प्रमाणीकरण के लिए उपयोग की जाती है, इसलिए हम संगति के लिए उस नामकरण सम्मेलन को बनाए रख रहे हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। इसकी मूल भाषा में मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न होने वाली किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।