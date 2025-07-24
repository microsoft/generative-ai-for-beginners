<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:25:50+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "hi"
}
-->
# अपने Dev Environment को सेटअप करें

हमने इस रिपॉजिटरी और कोर्स को एक [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) के साथ सेटअप किया है जिसमें एक Universal runtime है जो Python3, .NET, Node.js और Java डेवलपमेंट को सपोर्ट करता है। संबंधित कॉन्फ़िगरेशन `devcontainer.json` फाइल में परिभाषित है जो इस रिपॉजिटरी की रूट `.devcontainer/` फोल्डर में स्थित है।

Dev container को सक्रिय करने के लिए, इसे [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड runtime के लिए) या [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (लोकल डिवाइस-होस्टेड runtime के लिए) में लॉन्च करें। VS Code के अंदर dev containers कैसे काम करते हैं, इसके बारे में अधिक जानकारी के लिए [इस दस्तावेज़](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) को पढ़ें।  

> [!TIP]  
> हम GitHub Codespaces का उपयोग करने की सलाह देते हैं क्योंकि यह कम प्रयास में जल्दी शुरुआत करने के लिए उपयुक्त है। यह व्यक्तिगत खातों के लिए एक उदार [फ्री उपयोग कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान करता है। अपने कोटा का अधिकतम उपयोग करने के लिए निष्क्रिय codespaces को रोकने या हटाने के लिए [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कॉन्फ़िगर करें।  


## 1. असाइनमेंट्स को निष्पादित करना

प्रत्येक पाठ में _वैकल्पिक_ असाइनमेंट हो सकते हैं जो एक या अधिक प्रोग्रामिंग भाषाओं में प्रदान किए जा सकते हैं, जिनमें Python, .NET/C#, Java और JavaScript/TypeScript शामिल हैं। यह अनुभाग उन असाइनमेंट्स को निष्पादित करने से संबंधित सामान्य मार्गदर्शन प्रदान करता है।

### 1.1 Python असाइनमेंट्स

Python असाइनमेंट्स या तो एप्लिकेशन (`.py` फाइलें) के रूप में या Jupyter नोटबुक (`.ipynb` फाइलें) के रूप में प्रदान किए जाते हैं।  
- नोटबुक चलाने के लिए, इसे Visual Studio Code में खोलें, फिर ऊपर दाईं ओर _Select Kernel_ पर क्लिक करें और दिखाए गए डिफ़ॉल्ट Python 3 विकल्प को चुनें। अब आप _Run All_ करके नोटबुक को निष्पादित कर सकते हैं।  
- कमांड-लाइन से Python एप्लिकेशन चलाने के लिए, असाइनमेंट-विशिष्ट निर्देशों का पालन करें ताकि आप सही फाइलें चुनें और आवश्यक आर्गुमेंट्स प्रदान करें।  

## 2. Providers को कॉन्फ़िगर करना

असाइनमेंट्स **शायद** एक या अधिक Large Language Model (LLM) डिप्लॉयमेंट्स के खिलाफ काम करने के लिए सेटअप किए जा सकते हैं, जो OpenAI, Azure या Hugging Face जैसे समर्थित सेवा प्रदाताओं के माध्यम से होते हैं। ये एक _hosted endpoint_ (API) प्रदान करते हैं जिसे हम सही क्रेडेंशियल्स (API key या token) के साथ प्रोग्रामेटिकली एक्सेस कर सकते हैं। इस कोर्स में, हम इन प्रदाताओं पर चर्चा करते हैं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) जिसमें कोर GPT सीरीज सहित विविध मॉडल शामिल हैं।  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) जो OpenAI मॉडल्स के लिए एंटरप्राइज रेडीनेस पर केंद्रित है।  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) जो ओपन-सोर्स मॉडल्स और इन्फरेंस सर्वर प्रदान करता है।  

**आपको इन अभ्यासों के लिए अपने स्वयं के खाते का उपयोग करना होगा**। असाइनमेंट वैकल्पिक हैं इसलिए आप अपनी रुचि के अनुसार एक, सभी या कोई भी प्रदाता सेटअप कर सकते हैं। साइनअप के लिए कुछ मार्गदर्शन:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल उपलब्ध हैं |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले से आवेदन करना आवश्यक है](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat में सीमित मॉडल हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

इस रिपॉजिटरी को विभिन्न प्रदाताओं के साथ उपयोग के लिए _configure_ करने के निर्देश नीचे दिए गए हैं। जिन असाइनमेंट्स को किसी विशेष प्रदाता की आवश्यकता होगी, उनके फाइलनाम में निम्न टैग होंगे:  
 - `aoai` - Azure OpenAI endpoint, key की आवश्यकता  
 - `oai` - OpenAI endpoint, key की आवश्यकता  
 - `hf` - Hugging Face token की आवश्यकता  

आप एक, कोई या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट्स क्रेडेंशियल्स न मिलने पर त्रुटि दिखाएंगे।  

###  2.1. `.env` फाइल बनाएं

हम मानते हैं कि आपने ऊपर दिए गए मार्गदर्शन को पढ़ लिया है, संबंधित प्रदाता के साथ साइन अप कर लिया है, और आवश्यक प्रमाणीकरण क्रेडेंशियल्स (API_KEY या token) प्राप्त कर लिए हैं। Azure OpenAI के मामले में, हम मानते हैं कि आपके पास Azure OpenAI Service (endpoint) का एक वैध डिप्लॉयमेंट है जिसमें कम से कम एक GPT मॉडल चैट कंप्लीशन के लिए डिप्लॉय किया गया है।

अगला कदम है अपने **लोकल environment variables** को निम्नानुसार कॉन्फ़िगर करना:

1. रूट फोल्डर में `.env.copy` नामक फाइल देखें, जिसमें इस तरह की सामग्री होनी चाहिए:

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

2. नीचे दिए गए कमांड का उपयोग करके उस फाइल को `.env` में कॉपी करें। यह फाइल _gitignore-d_ है, जिससे आपके सीक्रेट्स सुरक्षित रहते हैं।

   ```bash
   cp .env.copy .env
   ```

3. मान भरें (दाएँ तरफ `=` के बाद के प्लेसहोल्डर्स को बदलें) जैसा कि अगले सेक्शन में बताया गया है।

3. (वैकल्पिक) यदि आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास environment variables को इस रिपॉजिटरी से जुड़े _Codespaces secrets_ के रूप में सेव करने का विकल्प होता है। उस स्थिति में, आपको लोकल .env फाइल सेटअप करने की आवश्यकता नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प केवल GitHub Codespaces के उपयोग पर ही काम करता है।** यदि आप Docker Desktop का उपयोग करते हैं तो आपको फिर भी .env फाइल सेटअप करनी होगी।  

### 2.2. `.env` फाइल भरें

आइए जल्दी से उन वेरिएबल नामों पर नज़र डालें और समझें कि वे क्या दर्शाते हैं:

| Variable  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह वह यूजर एक्सेस टोकन है जो आपने अपने प्रोफ़ाइल में सेटअप किया है |
| OPENAI_API_KEY | यह गैर-Azure OpenAI endpoints के लिए सेवा का उपयोग करने की अनुमति देने वाली कुंजी है |
| AZURE_OPENAI_API_KEY | यह Azure OpenAI सेवा के लिए अनुमति कुंजी है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI संसाधन के लिए डिप्लॉय किया गया endpoint है |
| AZURE_OPENAI_DEPLOYMENT | यह _text generation_ मॉडल डिप्लॉयमेंट endpoint है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _text embeddings_ मॉडल डिप्लॉयमेंट endpoint है |
| | |

नोट: अंतिम दो Azure OpenAI वेरिएबल्स चैट कंप्लीशन (टेक्स्ट जनरेशन) और वेक्टर सर्च (एम्बेडिंग्स) के लिए डिफ़ॉल्ट मॉडल को दर्शाते हैं। इन्हें सेट करने के निर्देश संबंधित असाइनमेंट्स में दिए जाएंगे।  

### 2.3 Azure कॉन्फ़िगर करें: पोर्टल से

Azure OpenAI endpoint और key मान [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में मिलेंगे, तो आइए वहीं से शुरू करें।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं  
1. साइडबार (बाएं मेनू) में **Keys and Endpoint** विकल्प पर क्लिक करें।  
1. **Show Keys** पर क्लिक करें - आपको KEY 1, KEY 2 और Endpoint दिखाई देंगे।  
1. AZURE_OPENAI_API_KEY के लिए KEY 1 मान का उपयोग करें।  
1. AZURE_OPENAI_ENDPOINT के लिए Endpoint मान का उपयोग करें।  

अब हमें उन विशिष्ट मॉडलों के endpoints चाहिए जिन्हें हमने डिप्लॉय किया है।

1. Azure OpenAI संसाधन के लिए साइडबार (बाएं मेनू) में **Model deployments** विकल्प पर क्लिक करें।  
1. गंतव्य पृष्ठ पर, **Manage Deployments** पर क्लिक करें।  

यह आपको Azure OpenAI Studio वेबसाइट पर ले जाएगा, जहाँ हम नीचे बताए गए अन्य मान पाएंगे।  

### 2.4 Azure कॉन्फ़िगर करें: स्टूडियो से

1. ऊपर बताए अनुसार अपने संसाधन से [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं।  
1. वर्तमान में डिप्लॉय किए गए मॉडलों को देखने के लिए साइडबार (बाएं) में **Deployments** टैब पर क्लिक करें।  
1. यदि आपका इच्छित मॉडल डिप्लॉय नहीं है, तो इसे डिप्लॉय करने के लिए **Create new deployment** का उपयोग करें।  
1. आपको एक _text-generation_ मॉडल की आवश्यकता होगी - हम सुझाव देते हैं: **gpt-35-turbo**  
1. आपको एक _text-embedding_ मॉडल की आवश्यकता होगी - हम सुझाव देते हैं: **text-embedding-ada-002**  

अब environment variables को अपडेट करें ताकि वे उपयोग किए गए _Deployment name_ को दर्शाएं। यह आमतौर पर मॉडल नाम के समान होगा जब तक कि आपने इसे स्पष्ट रूप से न बदला हो। उदाहरण के लिए, आपके पास हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**काम पूरा होने पर .env फाइल को सेव करना न भूलें**। अब आप फाइल से बाहर निकल सकते हैं और नोटबुक चलाने के निर्देशों पर वापस जा सकते हैं।  

### 2.5 OpenAI कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी OpenAI API key आपके [OpenAI खाते](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में मिल सकती है। यदि आपके पास खाता नहीं है, तो आप साइन अप कर सकते हैं और API key बना सकते हैं। एक बार key मिलने के बाद, आप इसे `.env` फाइल में `OPENAI_API_KEY` वेरिएबल में भर सकते हैं।  

### 2.6 Hugging Face कॉन्फ़िगर करें: प्रोफ़ाइल से

आपका Hugging Face टोकन आपके प्रोफ़ाइल में [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) के अंतर्गत मिलेगा। इन्हें सार्वजनिक रूप से पोस्ट या साझा न करें। इसके बजाय, इस प्रोजेक्ट के उपयोग के लिए एक नया टोकन बनाएं और उसे `.env` फाइल में `HUGGING_FACE_API_KEY` वेरिएबल के तहत कॉपी करें। _नोट:_ तकनीकी रूप से यह API key नहीं है, लेकिन प्रमाणीकरण के लिए उपयोग किया जाता है इसलिए हम संगति बनाए रखने के लिए इसी नामकरण का उपयोग कर रहे हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।