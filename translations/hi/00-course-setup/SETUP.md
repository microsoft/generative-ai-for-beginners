<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:06:21+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hi"
}
-->
# अपने डेवलपमेंट एनवायरनमेंट को सेटअप करें

हमने इस रिपॉजिटरी और कोर्स को [डेवलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) के साथ सेटअप किया है, जिसमें एक यूनिवर्सल रनटाइम है जो Python3, .NET, Node.js और Java डेवलपमेंट को सपोर्ट कर सकता है। संबंधित कॉन्फ़िगरेशन इस रिपॉजिटरी के रूट में स्थित `.devcontainer/` फोल्डर में `devcontainer.json` फ़ाइल में परिभाषित है।

डेवलपमेंट कंटेनर को सक्रिय करने के लिए, इसे [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड रनटाइम के लिए) या [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (स्थानीय डिवाइस-होस्टेड रनटाइम के लिए) में लॉन्च करें। VS Code के भीतर डेवलपमेंट कंटेनर कैसे काम करते हैं, इसके बारे में अधिक विवरण के लिए [इस दस्तावेज़](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) को पढ़ें।

> [!TIP]  
> हम न्यूनतम प्रयास के साथ तेजी से शुरुआत करने के लिए GitHub Codespaces का उपयोग करने की सलाह देते हैं। यह व्यक्तिगत खातों के लिए एक उदार [मुफ्त उपयोग कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान करता है। अपने कोटा उपयोग को अधिकतम करने के लिए निष्क्रिय कोडस्पेस को रोकने या हटाने के लिए [समय सीमा](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) को कॉन्फ़िगर करें।

## 1. असाइनमेंट निष्पादित करना

प्रत्येक पाठ में _वैकल्पिक_ असाइनमेंट होंगे जो एक या अधिक प्रोग्रामिंग भाषाओं में प्रदान किए जा सकते हैं, जिनमें शामिल हैं: Python, .NET/C#, Java और JavaScript/TypeScript। यह अनुभाग उन असाइनमेंट को निष्पादित करने से संबंधित सामान्य मार्गदर्शन प्रदान करता है।

### 1.1 Python असाइनमेंट

Python असाइनमेंट या तो एप्लिकेशन (`.py` फ़ाइलें) या Jupyter नोटबुक (`.ipynb` फ़ाइलें) के रूप में प्रदान किए जाते हैं।
- नोटबुक चलाने के लिए, इसे Visual Studio Code में खोलें, फिर _Select Kernel_ (ऊपर दाईं ओर) पर क्लिक करें और दिखाई देने वाले डिफ़ॉल्ट Python 3 विकल्प का चयन करें। अब आप नोटबुक को निष्पादित करने के लिए _Run All_ कर सकते हैं।
- कमांड-लाइन से Python एप्लिकेशन चलाने के लिए, सुनिश्चित करें कि आप सही फ़ाइलें चुनें और आवश्यक तर्क प्रदान करें, इसके लिए असाइनमेंट-विशिष्ट निर्देशों का पालन करें।

## 2. प्रदाताओं को कॉन्फ़िगर करना

असाइनमेंट **एक या अधिक बड़े भाषा मॉडल (LLM) डिप्लॉयमेंट के खिलाफ काम करने के लिए भी सेटअप किए जा सकते हैं** जैसे कि OpenAI, Azure या Hugging Face के माध्यम से समर्थित सेवा प्रदाता। ये एक _होस्टेड एंडपॉइंट_ (API) प्रदान करते हैं जिसे हम सही क्रेडेंशियल्स (API कुंजी या टोकन) के साथ प्रोग्रामेटिक रूप से एक्सेस कर सकते हैं। इस कोर्स में, हम इन प्रदाताओं पर चर्चा करते हैं:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विभिन्न मॉडलों के साथ, जिनमें मुख्य GPT श्रृंखला शामिल है।
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडलों के लिए, जिसमें उद्यम तैयारियों पर ध्यान केंद्रित किया गया है।
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडल और इन्फ्रेंस सर्वर के लिए।

**आपको इन अभ्यासों के लिए अपने स्वयं के खातों का उपयोग करने की आवश्यकता होगी**। असाइनमेंट वैकल्पिक हैं इसलिए आप अपनी रुचियों के आधार पर एक, सभी - या कोई भी प्रदाता सेटअप करने का चयन कर सकते हैं। साइनअप के लिए कुछ मार्गदर्शन:

| साइनअप | लागत | API कुंजी | प्लेग्राउंड | टिप्पणियाँ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK त्वरित प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टूडियो त्वरित प्रारंभ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले पहुंच के लिए आवेदन करना आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [एक्सेस टोकन](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat के पास सीमित मॉडल हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

नीचे दिए गए निर्देशों का पालन करें ताकि अलग-अलग प्रदाताओं के साथ उपयोग के लिए इस रिपॉजिटरी को _कॉन्फ़िगर_ किया जा सके। जिन असाइनमेंट को एक विशिष्ट प्रदाता की आवश्यकता होगी, उनकी फ़ाइलनाम में इनमें से एक टैग होगा:
- `aoai` - Azure OpenAI एंडपॉइंट, कुंजी की आवश्यकता है
- `oai` - OpenAI एंडपॉइंट, कुंजी की आवश्यकता है
- `hf` - Hugging Face टोकन की आवश्यकता है

आप एक, कोई, या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट बस गायब क्रेडेंशियल्स पर त्रुटि देंगे।

### 2.1. `.env` फ़ाइल बनाएं

हम मानते हैं कि आपने ऊपर दिए गए मार्गदर्शन को पहले ही पढ़ लिया है और संबंधित प्रदाता के साथ साइन अप कर लिया है, और आवश्यक प्रमाणीकरण क्रेडेंशियल्स (API_KEY या टोकन) प्राप्त कर लिया है। Azure OpenAI के मामले में, हम मानते हैं कि आपके पास एक GPT मॉडल के साथ कम से कम एक Azure OpenAI सेवा (एंडपॉइंट) का एक वैध डिप्लॉयमेंट है।

अगला कदम आपके **स्थानीय पर्यावरण चर** को निम्नानुसार कॉन्फ़िगर करना है:

1. रूट फ़ोल्डर में `.env.copy` फ़ाइल देखें, जिसमें इस तरह की सामग्री होनी चाहिए:

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

2. नीचे दिए गए कमांड का उपयोग करके उस फ़ाइल को `.env` में कॉपी करें। यह फ़ाइल _gitignore-d_ है, जो गुप्त को सुरक्षित रखती है।

   ```bash
   cp .env.copy .env
   ```

3. अगले अनुभाग में वर्णित अनुसार मान भरें (दाईं ओर के `=` पर प्लेसहोल्डर्स को बदलें)।

3. (विकल्प) यदि आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास इस रिपॉजिटरी से जुड़े _Codespaces secrets_ के रूप में पर्यावरण चर को सहेजने का विकल्प है। उस मामले में, आपको स्थानीय .env फ़ाइल सेटअप करने की आवश्यकता नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प केवल तभी काम करता है जब आप GitHub Codespaces का उपयोग करते हैं।** यदि आप Docker Desktop का उपयोग करते हैं तो आपको अभी भी .env फ़ाइल सेटअप करने की आवश्यकता होगी।

### 2.2. `.env` फ़ाइल भरें

आइए जल्दी से चर नामों पर नज़र डालें ताकि समझ सकें कि वे क्या प्रतिनिधित्व करते हैं:

| चर  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह वह उपयोगकर्ता एक्सेस टोकन है जिसे आपने अपनी प्रोफ़ाइल में सेटअप किया है |
| OPENAI_API_KEY | यह सेवा का उपयोग करने के लिए गैर-Azure OpenAI एंडपॉइंट्स के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_API_KEY | यह सेवा का उपयोग करने के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI संसाधन के लिए तैनात एंडपॉइंट है |
| AZURE_OPENAI_DEPLOYMENT | यह _टेक्स्ट जनरेशन_ मॉडल तैनाती एंडपॉइंट है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _टेक्स्ट एम्बेडिंग_ मॉडल तैनाती एंडपॉइंट है |
| | |

ध्यान दें: अंतिम दो Azure OpenAI चर चैट कंप्लीशन (टेक्स्ट जनरेशन) और वेक्टर सर्च (एम्बेडिंग) के लिए एक डिफ़ॉल्ट मॉडल को दर्शाते हैं। उन्हें सेट करने के निर्देश संबंधित असाइनमेंट में परिभाषित किए जाएंगे।

### 2.3 Azure कॉन्फ़िगर करें: पोर्टल से

Azure OpenAI एंडपॉइंट और कुंजी मान [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में पाए जाएंगे, तो आइए वहां से शुरू करें।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं
1. साइडबार (बाएं मेनू) में **Keys and Endpoint** विकल्प पर क्लिक करें।
1. **Show Keys** पर क्लिक करें - आपको निम्नलिखित दिखाई देना चाहिए: KEY 1, KEY 2 और Endpoint।
1. AZURE_OPENAI_API_KEY के लिए KEY 1 मान का उपयोग करें
1. AZURE_OPENAI_ENDPOINT के लिए Endpoint मान का उपयोग करें

अगला, हमें उन विशिष्ट मॉडलों के लिए एंडपॉइंट्स की आवश्यकता है जिन्हें हमने तैनात किया है।

1. Azure OpenAI संसाधन के लिए साइडबार (बाएं मेनू) में **Model deployments** विकल्प पर क्लिक करें।
1. गंतव्य पृष्ठ पर, **Manage Deployments** पर क्लिक करें

यह आपको Azure OpenAI Studio वेबसाइट पर ले जाएगा, जहां हम नीचे वर्णित अन्य मान पाएंगे।

### 2.4 Azure कॉन्फ़िगर करें: स्टूडियो से

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) पर **अपने संसाधन से** ऊपर वर्णित अनुसार नेविगेट करें।
1. वर्तमान में तैनात मॉडलों को देखने के लिए **Deployments** टैब (साइडबार, बाएं) पर क्लिक करें।
1. यदि आपका इच्छित मॉडल तैनात नहीं है, तो उसे तैनात करने के लिए **Create new deployment** का उपयोग करें।
1. आपको एक _टेक्स्ट-जनरेशन_ मॉडल की आवश्यकता होगी - हम अनुशंसा करते हैं: **gpt-35-turbo**
1. आपको एक _टेक्स्ट-एम्बेडिंग_ मॉडल की आवश्यकता होगी - हम अनुशंसा करते हैं **text-embedding-ada-002**

अब पर्यावरण चर को तैनाती नाम को दर्शाने के लिए अपडेट करें। यह आमतौर पर मॉडल नाम के समान होगा जब तक कि आपने इसे स्पष्ट रूप से नहीं बदला। इसलिए, उदाहरण के लिए, आपके पास हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**जब हो जाए तो .env फ़ाइल को सहेजना न भूलें**। अब आप फ़ाइल से बाहर निकल सकते हैं और नोटबुक चलाने के निर्देशों पर लौट सकते हैं।

### 2.5 OpenAI कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी OpenAI API कुंजी आपके [OpenAI खाते](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में पाई जा सकती है। यदि आपके पास एक नहीं है, तो आप एक खाता बना सकते हैं और API कुंजी बना सकते हैं। एक बार जब आपके पास कुंजी हो, तो आप `.env` फ़ाइल में `OPENAI_API_KEY` चर को भरने के लिए इसका उपयोग कर सकते हैं।

### 2.6 Hugging Face कॉन्फ़िगर करें: प्रोफ़ाइल से

आपका Hugging Face टोकन आपके प्रोफ़ाइल में [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) के तहत पाया जा सकता है। इन्हें सार्वजनिक रूप से पोस्ट या साझा न करें। इसके बजाय, इस प्रोजेक्ट उपयोग के लिए एक नया टोकन बनाएं और `.env` फ़ाइल में `HUGGING_FACE_API_KEY` चर के तहत उसे कॉपी करें। _ध्यान दें:_ यह तकनीकी रूप से एक API कुंजी नहीं है लेकिन प्रमाणीकरण के लिए उपयोग किया जाता है इसलिए हम स्थिरता के लिए उस नामकरण सम्मेलन को बनाए रख रहे हैं।

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।