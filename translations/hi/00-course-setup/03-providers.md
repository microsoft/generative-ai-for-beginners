<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:23:28+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "hi"
}
-->
# LLM प्रदाता चुनना और कॉन्फ़िगर करना 🔑

असाइनमेंट्स को एक या एक से अधिक बड़े भाषा मॉडल (LLM) डिप्लॉयमेंट्स के साथ काम करने के लिए सेटअप किया जा सकता है, जो कि OpenAI, Azure या Hugging Face जैसे सपोर्टेड सर्विस प्रदाताओं के माध्यम से उपलब्ध हैं। ये एक _होस्टेड एंडपॉइंट_ (API) प्रदान करते हैं, जिसे हम सही क्रेडेंशियल्स (API key या टोकन) के साथ प्रोग्रामेटिकली एक्सेस कर सकते हैं। इस कोर्स में, हम इन प्रदाताओं पर चर्चा करेंगे:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) जिसमें कई मॉडल्स हैं, जिनमें मुख्य GPT सीरीज़ शामिल है।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) जो OpenAI मॉडल्स को एंटरप्राइज़ के लिए तैयार करता है
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडल्स और इन्फेरेंस सर्वर के लिए

**इन एक्सरसाइज़ के लिए आपको अपने खुद के अकाउंट्स का उपयोग करना होगा।** असाइनमेंट्स ऑप्शनल हैं, इसलिए आप अपनी रुचि के अनुसार एक, सभी या कोई भी प्रदाता सेटअप कर सकते हैं। साइनअप के लिए कुछ गाइडेंस:

| साइनअप | लागत | API Key | प्लेग्राउंड | टिप्पणियाँ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [प्राइसिंग](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल्स उपलब्ध हैं |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [प्राइसिंग](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टूडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले से अप्लाई करना जरूरी है](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [प्राइसिंग](https://huggingface.co/pricing) | [एक्सेस टोकन्स](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat में सीमित मॉडल्स हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

नीचे दिए गए निर्देशों का पालन करें ताकि इस रिपॉजिटरी को अलग-अलग प्रदाताओं के साथ उपयोग के लिए _कॉन्फ़िगर_ किया जा सके। जिन असाइनमेंट्स को किसी विशेष प्रदाता की आवश्यकता होगी, उनकी फाइलनाम में इनमें से कोई टैग होगा:

- `aoai` - Azure OpenAI एंडपॉइंट, key की आवश्यकता है
- `oai` - OpenAI एंडपॉइंट, key की आवश्यकता है
- `hf` - Hugging Face टोकन की आवश्यकता है

आप एक, कोई नहीं, या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट्स में अगर क्रेडेंशियल्स नहीं हैं तो वे एरर देंगे।

## `.env` फाइल बनाएं

हम मानते हैं कि आपने ऊपर दिए गए गाइडेंस को पढ़ लिया है, संबंधित प्रदाता के साथ साइनअप कर लिया है, और आवश्यक ऑथेंटिकेशन क्रेडेंशियल्स (API_KEY या टोकन) प्राप्त कर लिए हैं। Azure OpenAI के मामले में, हम मानते हैं कि आपके पास Azure OpenAI Service (एंडपॉइंट) का वैध डिप्लॉयमेंट है, जिसमें कम से कम एक GPT मॉडल चैट कम्प्लीशन के लिए डिप्लॉय किया गया है।

अगला कदम है अपने **लोकल एनवायरनमेंट वेरिएबल्स** को इस तरह कॉन्फ़िगर करना:

1. रूट फोल्डर में `.env.copy` फाइल देखें, जिसमें कुछ इस तरह का कंटेंट होना चाहिए:

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

2. उस फाइल को नीचे दिए गए कमांड से `.env` में कॉपी करें। यह फाइल _gitignore_ की गई है, जिससे सीक्रेट्स सुरक्षित रहते हैं।

   ```bash
   cp .env.copy .env
   ```

3. वैल्यूज़ भरें (राइट साइड के प्लेसहोल्डर्स को बदलें) जैसा कि अगले सेक्शन में बताया गया है।

4. (विकल्प) अगर आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास एनवायरनमेंट वेरिएबल्स को _Codespaces secrets_ के रूप में इस रिपॉजिटरी से जोड़ने का विकल्प है। उस स्थिति में, आपको लोकल .env फाइल सेटअप करने की जरूरत नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प सिर्फ GitHub Codespaces के लिए काम करता है।** अगर आप Docker Desktop का उपयोग करते हैं, तो आपको .env फाइल सेटअप करनी ही होगी।

## `.env` फाइल में वैल्यू भरें

आइए वेरिएबल नामों को जल्दी से देखें और समझें कि वे क्या दर्शाते हैं:

| वेरिएबल  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह वह यूज़र एक्सेस टोकन है जिसे आपने अपनी प्रोफाइल में सेटअप किया है |
| OPENAI_API_KEY | यह सर्विस का ऑथराइज़ेशन key है, जो non-Azure OpenAI एंडपॉइंट्स के लिए है |
| AZURE_OPENAI_API_KEY | यह उस सर्विस का ऑथराइज़ेशन key है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI रिसोर्स के लिए डिप्लॉय किया गया एंडपॉइंट है |
| AZURE_OPENAI_DEPLOYMENT | यह _टेक्स्ट जनरेशन_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _टेक्स्ट एम्बेडिंग्स_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| | |

नोट: आखिरी दो Azure OpenAI वेरिएबल्स डिफॉल्ट मॉडल को दर्शाते हैं - चैट कम्प्लीशन (टेक्स्ट जनरेशन) और वेक्टर सर्च (एम्बेडिंग्स) के लिए। इन्हें सेट करने के निर्देश संबंधित असाइनमेंट्स में दिए जाएंगे।

## Azure कॉन्फ़िगर करें: पोर्टल से

Azure OpenAI एंडपॉइंट और key वैल्यूज़ आपको [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में मिलेंगी, तो चलिए वहीं से शुरू करते हैं।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं
1. साइडबार (बाएं मेन्यू) में **Keys and Endpoint** विकल्प पर क्लिक करें।
1. **Show Keys** पर क्लिक करें - आपको KEY 1, KEY 2 और Endpoint दिखना चाहिए।
1. AZURE_OPENAI_API_KEY के लिए KEY 1 वैल्यू का उपयोग करें
1. AZURE_OPENAI_ENDPOINT के लिए Endpoint वैल्यू का उपयोग करें

अब हमें उन मॉडल्स के एंडपॉइंट्स चाहिए, जिन्हें हमने डिप्लॉय किया है।

1. Azure OpenAI रिसोर्स के लिए साइडबार (बाएं मेन्यू) में **Model deployments** विकल्प पर क्लिक करें।
1. डेस्टिनेशन पेज में **Manage Deployments** पर क्लिक करें

यह आपको Azure OpenAI Studio वेबसाइट पर ले जाएगा, जहां हम नीचे बताए गए अन्य वैल्यूज़ पाएंगे।

## Azure कॉन्फ़िगर करें: स्टूडियो से

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) पर **अपने रिसोर्स से** जाएं जैसा कि ऊपर बताया गया है।
1. साइडबार (बाएं) में **Deployments** टैब पर क्लिक करें ताकि वर्तमान में डिप्लॉय किए गए मॉडल्स दिखें।
1. अगर आपका मनचाहा मॉडल डिप्लॉय नहीं है, तो **Create new deployment** का उपयोग करके उसे डिप्लॉय करें।
1. आपको एक _टेक्स्ट-जनरेशन_ मॉडल चाहिए - हम सलाह देते हैं: **gpt-35-turbo**
1. आपको एक _टेक्स्ट-एम्बेडिंग_ मॉडल चाहिए - हम सलाह देते हैं **text-embedding-ada-002**

अब एनवायरनमेंट वेरिएबल्स को _Deployment name_ के अनुसार अपडेट करें। यह आमतौर पर मॉडल नाम जैसा ही होगा, जब तक आपने इसे बदल न दिया हो। उदाहरण के लिए, आपके पास हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**.env फाइल सेव करना न भूलें जब हो जाए।** अब आप फाइल से बाहर जा सकते हैं और नोटबुक चलाने के निर्देशों पर लौट सकते हैं।

## OpenAI कॉन्फ़िगर करें: प्रोफाइल से

आपकी OpenAI API key आपके [OpenAI अकाउंट](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में मिलेगी। अगर आपके पास नहीं है, तो आप अकाउंट बना सकते हैं और API key बना सकते हैं। एक बार key मिल जाए, तो उसे `.env` फाइल में `OPENAI_API_KEY` वेरिएबल में डालें।

## Hugging Face कॉन्फ़िगर करें: प्रोफाइल से

आपका Hugging Face टोकन आपकी प्रोफाइल में [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) के तहत मिलेगा। इन्हें पब्लिकली पोस्ट या शेयर न करें। इसके बजाय, इस प्रोजेक्ट के लिए नया टोकन बनाएं और उसे `.env` फाइल में `HUGGING_FACE_API_KEY` वेरिएबल के तहत कॉपी करें। _नोट:_ यह टेक्निकली API key नहीं है, लेकिन ऑथेंटिकेशन के लिए उपयोग होता है, इसलिए हम नामकरण में कंसिस्टेंसी के लिए यही नाम रख रहे हैं।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।