# एक LLM प्रदाता चुनना और कॉन्फ़िगर करना 🔑

असाइनमेंट को एक या एक से अधिक बड़े भाषा मॉडल (LLM) परिनियोजन के खिलाफ काम करने के लिए भी सेट अप किया जा सकता है, जैसे OpenAI, Azure या Hugging Face जैसे समर्थित सेवा प्रदाता के माध्यम से। ये एक _होस्टेड एंडपॉइंट_ (API) प्रदान करते हैं, जिसे हम सही क्रेडेंशियल्स (API कुंजी या टोकन) के साथ प्रोग्रामैटिक रूप से एक्सेस कर सकते हैं। इस कोर्स में, हम इन प्रदाताओं पर चर्चा करते हैं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विभिन्न मॉडल सहित मुख्य GPT श्रृंखला के साथ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडलों के लिए, जिसमें एंटरप्राइज़ रेडीनेस पर ध्यान केंद्रित है
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एकल एंडपॉइंट और API कुंजी के लिए कई मॉडलों, जैसे OpenAI, Meta, Mistral, Cohere, Microsoft और अन्य तक पहुँचने के लिए (यह GitHub Models को प्रतिस्थापित करता है, जो जुलाई 2026 के अंत में रिटायर हो रहा है)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडल और इन्फ्लुएंस सर्वर के लिए
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) या [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) यदि आप मॉडल को पूरी तरह से ऑफ़लाइन अपने डिवाइस पर चलाना चाहते हैं, बिना किसी क्लाउड सदस्यता के

**इन अभ्यासों के लिए आपको अपने ही खाते का उपयोग करना होगा।** असाइनमेंट वैकल्पिक हैं इसलिए आप अपनी रुचि के आधार पर एक, सभी - या कोई भी - प्रदाता सेट अप कर सकते हैं। साइनअप के लिए कुछ मार्गदर्शन:

| साइनअप | लागत | API कुंजी | प्लेग्राउंड | टिप्पणियाँ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टूडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले से आवेदन करना आवश्यक](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [प्रोजेक्ट अवलोकन पेज](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry प्लेग्राउंड](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | निःशुल्क स्तर उपलब्ध; कई मॉडल प्रदाताओं के लिए एक एंडपॉइंट + कुंजी |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [ऐक्सेस टोकन](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat के पास सीमित मॉडल हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | नि:शुल्क (आपके डिवाइस पर चलता है) | आवश्यक नहीं | [स्थानीय CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूरी तरह से ऑफ़लाइन, OpenAI-समर्थित एंडपॉइंट |
| | | | | |

इस रिपॉजिटरी को विभिन्न प्रदाताओं के साथ उपयोग के लिए _कॉन्फ़िगर_ करने हेतु नीचे दिए निर्देशों का पालन करें। जिन असाइनमेंट्स को विशिष्ट प्रदाता की आवश्यकता होगी, उनकी फाइल नाम में निम्नलिखित टैग होंगे:

- `aoai` - Azure OpenAI एंडपॉइंट, कुंजी आवश्यक है
- `oai` - OpenAI एंडपॉइंट, कुंजी आवश्यक है
- `hf` - Hugging Face टोकन आवश्यक है
- `githubmodels` - Microsoft Foundry Models एंडपॉइंट, कुंजी आवश्यक है (GitHub Models जुलाई 2026 के अंत में रिटायर हो रहा है)

आप एक, कोई या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट केवल क्रेडेंशियल्स न होने पर त्रुटि दिखाएंगे।

## `.env` फ़ाइल बनाएं

हम मानते हैं कि आपने ऊपर दिए गए मार्गदर्शन को पढ़ लिया है, संबंधित प्रदाता के साथ साइन अप कर लिया है, और आवश्यक प्रमाणिकरण क्रेडेंशियल्स (API_KEY या टोकन) प्राप्त कर लिए हैं। Azure OpenAI के मामले में, मान लेते हैं कि आपके पास Azure OpenAI सेवा (एंडपॉइंट) का वैध परिनियोजन है, जिसमें कम से कम एक GPT मॉडल चैट पूर्णता के लिए तैनात है।

अगला चरण आपके **स्थानीय पर्यावरण चर** को निम्नानुसार कॉन्फ़िगर करना है:

1. रूट फ़ोल्डर में `.env.copy` नामक फ़ाइल देखें, जिसमें निम्नलिखित जैसा सामग्री होना चाहिए:

   ```bash
   # OpenAI प्रदाता
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry में Azure OpenAI
   ## (Azure OpenAI सेवा अब Microsoft Foundry का हिस्सा है: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # डिफ़ॉल्ट सेट है! (वर्तमान स्थिर GA API संस्करण)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry मॉडल (मल्टी-प्रोवाइडर मॉडल कैटलॉग, जो GitHub मॉडल की जगह लेता है, जो जुलाई 2026 के अंत में बंद हो जाएगा)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## हगींग फेस
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. नीचे दिए गए कमांड का उपयोग करके उस फ़ाइल को `.env` कॉपी करें। यह फ़ाइल _gitignore-d_ है, जिससे आपके गुप्त जानकारी सुरक्षित रहती है।

   ```bash
   cp .env.copy .env
   ```

3. मानों को भरें (जैसे लेफ्ट साइड के बाद की जगह को प्रतिस्थापित करें) जैसा अगले खंड में वर्णित है।

4. (वैकल्पिक) यदि आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास पर्यावरण चर (environment variables) को इस रिपॉजिटरी से जुड़ी _Codespaces secrets_ के रूप में सहेजने का विकल्प है। उस स्थिति में, आपको स्थानीय .env फ़ाइल सेटअप करने की आवश्यकता नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प केवल तब काम करता है जब आप GitHub Codespaces का उपयोग करते हैं।** यदि आप Docker Desktop का उपयोग कर रहे हैं तो आपको फिर भी .env फ़ाइल सेटअप करनी होगी।

## `.env` फ़ाइल भरें

आइए जल्दी से उन वेरिएबल नामों को देखें ताकि समझ सकें कि वे क्या दर्शाते हैं:

| वेरिएबल  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह उपयोगकर्ता एक्सेस टोकन है जिसे आपने अपने प्रोफ़ाइल में सेट किया है |
| OPENAI_API_KEY | यह सेवा का उपयोग करने के लिए प्राधिकरण कुंजी है गैर-Azure OpenAI एंडपॉइंट्स के लिए |
| AZURE_OPENAI_API_KEY | यह उस सेवा के उपयोग के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI संसाधन के लिए तैनात एंडपॉइंट है |
| AZURE_OPENAI_DEPLOYMENT | यह _टेक्स्ट जनरेशन_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _टेक्स्ट एम्बेडिंग्स_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| AZURE_INFERENCE_ENDPOINT | यह आपके Microsoft Foundry प्रोजेक्ट का एंडपॉइंट है, जो Microsoft Foundry Models के लिए उपयोग होता है |
| AZURE_INFERENCE_CREDENTIAL | यह आपके Microsoft Foundry प्रोजेक्ट के लिए API कुंजी है |
| | |

नोट: अंतिम दो Azure OpenAI वेरिएबल चैट पूर्णता (टेक्स्ट जनरेशन) और वेक्टर खोज (एम्बेडिंग्स) के लिए डिफ़ॉल्ट मॉडल को दर्शाते हैं। इन्हें सेट करने के निर्देश संबंधित असाइनमेंट्स में दिए जाएंगे।

## Azure OpenAI कॉन्फ़िगर करें: पोर्टल से

> **नोट:** Azure OpenAI सेवा अब [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) का हिस्सा है। संसाधन और डिप्लॉयमेंट Azure पोर्टल में अभी भी दिखाई देते हैं, लेकिन दैनिक मॉडल प्रबंधन (डिप्लॉयमेंट्स, प्लेग्राउंड, मॉनीटरिंग) अब पुराने स्टैंडअलोन "Azure OpenAI Studio" के बजाय Foundry पोर्टल में होता है।

Azure OpenAI एंडपॉइंट और कुंजी मान [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में मिलेंगे, तो चलिए वहीं से शुरू करते हैं।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं
1. साइडबार (बाएँ मेनू) में **कुंजी और एंडपॉइंट्स** विकल्प पर क्लिक करें।
1. **कुंजी दिखाएं** पर क्लिक करें - आपको निम्न दिखाई देगा: KEY 1, KEY 2 और Endpoint।
1. AZURE_OPENAI_API_KEY के लिए KEY 1 मान का उपयोग करें
1. AZURE_OPENAI_ENDPOINT के लिए Endpoint मान का उपयोग करें

अब हमें उन विशिष्ट मॉडलों के एंडपॉइंट्स चाहिए जिन्हें हमने तैनात किया है।

1. Azure OpenAI संसाधन के लिए साइडबार (बाएँ मेनू) में **मॉडल डिप्लॉयमेंट्स** विकल्प पर क्लिक करें।
1. गंतव्य पृष्ठ में, **Microsoft Foundry पोर्टल पर जाएं** (या आपके संसाधन प्रकार के आधार पर **डिप्लॉयमेंट प्रबंधित करें**) पर क्लिक करें

इससे आप Microsoft Foundry पोर्टल पर पहुंचेंगे, जहाँ हम अन्य मान नीचे दिए अनुसार पाएंगे।

## Azure OpenAI कॉन्फ़िगर करें: Microsoft Foundry पोर्टल से

1. ऊपर वर्णित अनुसार अपने संसाधन से [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) पर नेविगेट करें।
1. वर्तमान में तैनात मॉडलों को देखने के लिए **Deployments** टैब (साइडबार, बाएँ) पर क्लिक करें।
1. यदि आपका इच्छित मॉडल तैनात नहीं है, तो [मॉडल कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) से मॉडल को तैनात करने के लिए **Deploy model** का उपयोग करें।
1. आपको एक _text-generation_ मॉडल की आवश्यकता होगी - हम सुझाव देते हैं: **gpt-5-mini**
1. आपको एक _text-embedding_ मॉडल की आवश्यकता होगी - हम सुझाव देते हैं **text-embedding-3-small**

अब पर्यावरण चर को अपडेट करें ताकि वे उपयोग किए गए _Deployment name_ को दर्शाएं। यह आमतौर पर मॉडल नाम के समान होगा जब तक आपने इसे स्पष्ट रूप से नहीं बदला हो। उदाहरण के लिए, कुछ ऐसा हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**बदलाव के बाद .env फ़ाइल को सहेजना न भूलें**। अब आप फ़ाइल से बाहर निकल सकते हैं और नोटबुक चलाने के निर्देशों पर लौट सकते हैं।

## OpenAI कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी OpenAI API कुंजी आपके [OpenAI खाते](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में मिल सकती है। यदि आपके पास कुंजी नहीं है, तो आप एक खाता बनाएँ और API कुंजी बनाएं। कुंजी मिलने के बाद, आप इसे `.env` फ़ाइल में `OPENAI_API_KEY` वेरिएबल में भर सकते हैं।

## Hugging Face कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी Hugging Face टोकन आपकी प्रोफ़ाइल में [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) के अंतर्गत पाया जा सकता है। इन्हें सार्वजनिक रूप से पोस्ट या साझा न करें। इसके बजाय, इस प्रोजेक्ट के उपयोग के लिए एक नया टोकन बनाएं और उसे `.env` फ़ाइल में `HUGGING_FACE_API_KEY` वेरिएबल में कॉपी करें। _नोट:_ यह तकनीकी रूप से API कुंजी नहीं है, लेकिन प्रमाणीकरण के लिए उपयोग किया जाता है इसलिए हम संगति के लिए इस नामकरण का उपयोग कर रहे हैं।

## Microsoft Foundry Models कॉन्फ़िगर करें: पोर्टल से

> **नोट:** GitHub Models जुलाई 2026 के अंत में रिटायर हो रहे हैं। Microsoft Foundry Models इसका सीधा प्रतिस्थापन है, जो एक जैसे निशुल्क परीक्षण मॉडल कैटलॉग और Azure AI Inference SDK / OpenAI SDK अनुभव देता है।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं और एक Foundry प्रोजेक्ट बनाएं या खोलें।
1. [मॉडल कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ब्राउज़ करें और एक मॉडल तैनात करें, उदाहरण के लिए `gpt-5-mini`।
1. प्रोजेक्ट के **अवलोकन** पेज पर, **एंडपॉइंट** और **API कुंजी** कॉपी करें।
1. अपने `.env` फ़ाइल में `AZURE_INFERENCE_ENDPOINT` के लिए एंडपॉइंट मान और `AZURE_INFERENCE_CREDENTIAL` के लिए कुंजी मान का उपयोग करें।

## ऑफ़लाइन / स्थानीय प्रदाता

यदि आप बिलकुल भी क्लाउड सदस्यता का उपयोग नहीं करना चाहते हैं, तो आप संगत खुले मॉडल सीधे अपने डिवाइस पर चला सकते हैं:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft का ऑन-डिवाइस रनटाइम। यह स्वचालित रूप से सर्वश्रेष्ठ निष्पादन प्रदाता (NPU, GPU, या CPU) का चयन करता है और एक OpenAI-समर्थित एंडपॉइंट प्रदान करता है, जिससे आप इस कोर्स के अधिकांश उदाहरण कोड को न्यूनतम बदलावों के साथ फिर से उपयोग कर सकते हैं। शुरू करने के लिए [Foundry Local दस्तावेज़](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) देखें, या `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) के साथ इंस्टॉल करें।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral और Gemma जैसे खुले मॉडलों को स्थानीय रूप से चलाने के लिए लोकप्रिय विकल्प।


दोनों विकल्पों का उपयोग करते हुए व्यावहारिक उदाहरणों के लिए [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) देखें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->