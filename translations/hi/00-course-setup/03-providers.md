# एक LLM प्रदाता चुनना और कॉन्फ़िगर करना 🔑

असाइनमेंट्स **शायद** एक या अधिक बड़े भाषा मॉडल (LLM) डिप्लॉयमेंट्स के खिलाफ काम करने के लिए एक समर्थित सेवा प्रदाता जैसे OpenAI, Azure या Hugging Face के माध्यम से सेटअप किए जा सकते हैं। ये एक _होस्टेड एंडपॉइंट_ (API) प्रदान करते हैं जिसे हम सही प्रमाण-पत्रों (API कुंजी या टोकन) के साथ प्रोग्रामैटिक रूप से एक्सेस कर सकते हैं। इस पाठ्यक्रम में, हम इन प्रदाताओं पर चर्चा करते हैं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मॉडलों के साथ जिसमें मुख्य GPT श्रृंखला शामिल है।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मॉडलों के लिए उद्यम तत्परता पर ध्यान केंद्रित करते हुए
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एकल एंडपॉइंट और API कुंजी के लिए OpenAI, Meta, Mistral, Cohere, Microsoft और अधिक से सैकड़ों मॉडलों तक पहुँच के लिए (GitHub Models का स्थान लेता है, जो जुलाई 2026 के अंत में सेवानिवृत्त हो रहा है)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ओपन-सोर्स मॉडलों और इंफ़ेरेंस सर्वर के लिए
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) या [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) यदि आप अपने स्वयं के डिवाइस पर पूरी तरह ऑफ़लाइन मॉडल चलाना पसंद करते हैं, बिना किसी क्लाउड सदस्यता के

**आपको इन अभ्यासों के लिए अपने खुद के खातों का उपयोग करना होगा**। असाइनमेंट वैकल्पिक हैं इसलिए आप अपनी रुचियों के आधार पर एक, सभी या कोई भी प्रदाता सेटअप कर सकते हैं। साइनअप के लिए कुछ मार्गदर्शन:

| साइनअप | लागत | API कुंजी | प्लेग्राउंड | टिप्पणियाँ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [परियोजना-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | कई मॉडल उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टूडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहले से आवेदन करना आवश्यक](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [परियोजना अवलोकन पृष्ठ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry प्लेग्राउंड](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | मुफ़्त स्तर उपलब्ध; कई मॉडल प्रदाताओं के लिए एक एंडपॉइंट + कुंजी |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [एक्सेस टोकन](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat में सीमित मॉडल हैं](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | मुफ़्त (आपके डिवाइस पर चलाता है) | आवश्यक नहीं | [स्थानीय CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूरी तरह से ऑफ़लाइन, OpenAI-समर्थित एंडपॉइंट |
| | | | | |

नीचे दिए गए निर्देशों का पालन करके इस रिपॉजिटरी को विभिन्न प्रदाताओं के उपयोग के लिए _कॉन्फ़िगर_ करें। जिन असाइनमेंट्स को किसी विशिष्ट प्रदाता की आवश्यकता होगी, उनके फ़ाइलनाम में निम्नलिखित टैग होंगे:

- `aoai` - Azure OpenAI एंडपॉइंट, कुंजी की आवश्यकता
- `oai` - OpenAI एंडपॉइंट, कुंजी की आवश्यकता
- `hf` - Hugging Face टोकन की आवश्यकता
- `githubmodels` - Microsoft Foundry Models एंडपॉइंट, कुंजी की आवश्यकता (GitHub Models जुलाई 2026 के अंत में सेवानिवृत्त हो रहे हैं)

आप एक, कोई या सभी प्रदाताओं को कॉन्फ़िगर कर सकते हैं। संबंधित असाइनमेंट्स गायब प्रमाण-पत्रों पर त्रुटि दिखाएंगे।

## `.env` फ़ाइल बनाएँ

हम मानते हैं कि आपने ऊपर दिए गए मार्गदर्शन को पहले ही पढ़ लिया है और संबंधित प्रदाता के साथ साइन अप कर लिया है, और आवश्यक प्रमाण-पत्र (API_KEY या टोकन) प्राप्त कर लिए हैं। Azure OpenAI के मामले में, हम यह भी मानते हैं कि आपके पास Azure OpenAI सेवा (एंडपॉइंट) की एक वैध डिप्लॉयमेंट है जिसमें कम से कम एक GPT मॉडल चैट पूर्णता के लिए तैनात है।

अगला चरण आपके **लोकल पर्यावरण चरों** को निम्नानुसार कॉन्फ़िगर करना है:

1. रूट फोल्डर में `.env.copy` फ़ाइल देखें जिसमें इस तरह की सामग्री होनी चाहिए:

   ```bash
   # OpenAI प्रदाता
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## माइक्रोसॉफ्ट फाउंड्री में Azure OpenAI
   ## (Azure OpenAI सेवा अब Microsoft Foundry का हिस्सा है: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # डिफ़ॉल्ट सेट है! (वर्तमान स्थिर GA API संस्करण)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## माइक्रोसॉफ्ट फाउंड्री मॉडल (मल्टी-प्रोवाइडर मॉडल कैटलॉग, GitHub मॉडल को प्रतिस्थापित करता है, जो जुलाई 2026 के अंत में सेवा समाप्त करेगा)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## हगिंग फेस
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. नीचे दिए गए कमांड का उपयोग करके उस फ़ाइल को `.env` में कॉपी करें। यह फ़ाइल _gitignore-d_ है, जो गोपनीयता बनाए रखती है।

   ```bash
   cp .env.copy .env
   ```

3. मान भरें (दाएँ तरफ `=` के बाद मौजूद प्लेसहोल्डर बदलें) जैसा कि अगले सेक्शन में वर्णित है।

4. (वैकल्पिक) यदि आप GitHub Codespaces का उपयोग करते हैं, तो आपके पास पर्यावरण चर को इस रिपॉजिटरी से जुड़े _Codespaces रहस्यों_ के रूप में सहेजने का विकल्प होता है। ऐसी स्थिति में, आपको लोकल .env फ़ाइल सेटअप करने की आवश्यकता नहीं होगी। **हालांकि, ध्यान दें कि यह विकल्प केवल तब काम करता है जब आप GitHub Codespaces का उपयोग करते हैं।** अगर आप Docker Desktop इस्तेमाल करते हैं, तो .env फ़ाइल सेटअप करना आवश्यक होगा।

## `.env` फ़ाइल भरें

आइए चर नामों पर एक नज़र डालते हैं ताकि हम समझ सकें वे क्या दर्शाते हैं:

| चर  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यह उपयोगकर्ता एक्सेस टोकन है जिसे आपने अपने प्रोफ़ाइल में सेटअप किया है |
| OPENAI_API_KEY | यह Azure OpenAI के बाहर सेवा उपयोग के लिए प्राधिकरण कुंजी है |
| AZURE_OPENAI_API_KEY | यह उस सेवा का प्राधिकरण कुंजी है |
| AZURE_OPENAI_ENDPOINT | यह Azure OpenAI संसाधन के लिए तैनात एंडपॉइंट है |
| AZURE_OPENAI_DEPLOYMENT | यह _टेक्स्ट जेनरेशन_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यह _टेक्स्ट एम्बेडिंग्स_ मॉडल डिप्लॉयमेंट एंडपॉइंट है |
| AZURE_INFERENCE_ENDPOINT | यह आपके Microsoft Foundry प्रोजेक्ट के लिए एंडपॉइंट है, जो Microsoft Foundry Models के लिए उपयोग होता है |
| AZURE_INFERENCE_CREDENTIAL | यह आपके Microsoft Foundry प्रोजेक्ट के लिए API कुंजी है |
| | |

नोट: अंतिम दो Azure OpenAI चर चैट पूर्णता (टेक्स्ट जेनरेशन) और वेक्टर खोज (एम्बेडिंग्स) के लिए डिफ़ॉल्ट मॉडल को प्रतिबिंबित करते हैं। इन्हें सेटअप करने के निर्देश संबंधित असाइनमेंट्स में दिए जाएंगे।

## Azure OpenAI कॉन्फ़िगर करें: पोर्टल से

> **नोट:** Azure OpenAI सेवा अब [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) का हिस्सा है। संसाधन और डिप्लॉयमेंट अब भी Azure पोर्टल में दिखाई देते हैं, लेकिन रोज़ाना मॉडल प्रबंधन (डिप्लॉयमेंट, प्लेग्राउंड, मॉनिटरिंग) अब पुराने स्वतंत्र "Azure OpenAI स्टूडियो" के बजाय Foundry पोर्टल में होता है।

Azure OpenAI एंडपॉइंट और कुंजी मान [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) में पाए जाएंगे, तो आइए वहीं से शुरू करें।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएँ
1. साइडबार (बाएं मेनू) में **Keys and Endpoint** विकल्प पर क्लिक करें।
1. **Show Keys** पर क्लिक करें - आपको निम्न मिलेगा: KEY 1, KEY 2 और एंडपॉइंट।
1. AZURE_OPENAI_API_KEY के लिए KEY 1 मान का उपयोग करें
1. AZURE_OPENAI_ENDPOINT के लिए एंडपॉइंट मान का उपयोग करें

अब, हमें उन विशिष्ट मॉडलों के एंडपॉइंट्स चाहिए जिन्हें हमने डिप्लॉय किया है।

1. Azure OpenAI संसाधन के लिए साइडबार (बाएं मेनू) में **Model deployments** विकल्प पर क्लिक करें।
1. गंतव्य पृष्ठ पर, **Go to Microsoft Foundry portal** (या आपके संसाधन प्रकार के अनुसार **Manage Deployments**) पर क्लिक करें।

यह आपको Microsoft Foundry पोर्टल पर ले जाएगा, जहाँ हम नीचे दिए गए अनुसार अन्य मान पाएंगे।

## Azure OpenAI कॉन्फ़िगर करें: Microsoft Foundry पोर्टल से

1. उपरोक्त वर्णित तरीके से [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं **अपने संसाधन से**।
1. वर्तमान में डिप्लॉय किए गए मॉडलों को देखने के लिए **Deployments** टैब (साइडबार, बाएं) पर क्लिक करें।
1. यदि आपका इच्छित मॉडल डिप्लॉय नहीं है, तो [मॉडल कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) से इसे डिप्लॉय करने के लिए **Deploy model** का उपयोग करें।
1. आपको एक _text-generation_ मॉडल की आवश्यकता होगी - हम सुझाते हैं: **gpt-4o-mini**
1. आपको एक _text-embedding_ मॉडल की आवश्यकता होगी - हम सुझाते हैं **text-embedding-3-small**

अब पर्यावरण चर को उस _Deployment name_ के अनुसार अपडेट करें जो उपयोग किया गया है। यह आमतौर पर मॉडल नाम के समान होगा जब तक कि आपने इसे स्पष्ट रूप से न बदला हो। उदाहरण के लिए, आपके पास हो सकता है:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**पूरा करने पर .env फ़ाइल को सहेजना न भूलें**। अब आप फ़ाइल से बाहर निकल सकते हैं और नोटबुक चलाने के निर्देशों पर वापस आ सकते हैं।

## OpenAI कॉन्फ़िगर करें: प्रोफ़ाइल से

आपकी OpenAI API कुंजी आपकी [OpenAI खाते](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) में मिल सकती है। यदि आपके पास कुंजी नहीं है, तो आप एक खाता बना सकते हैं और API कुंजी बना सकते हैं। कुंजी प्राप्त करने के बाद, आप इसे `.env` फ़ाइल में `OPENAI_API_KEY` चर भरने के लिए उपयोग कर सकते हैं।

## Hugging Face कॉन्फ़िगर करें: प्रोफ़ाइल से

आपका Hugging Face टोकन आपके प्रोफ़ाइल के [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) में पाया जा सकता है। इन्हें सार्वजनिक रूप से पोस्ट या साझा न करें। इसके बजाय, इस प्रोजेक्ट उपयोग के लिए एक नया टोकन बनाएं और उसे `.env` फ़ाइल में `HUGGING_FACE_API_KEY` चर के तहत कॉपी करें। _नोट:_ यह तकनीकी रूप से API कुंजी नहीं है लेकिन प्रमाणीकरण के लिए उपयोग किया जाता है इसलिए संगति के लिए हम इसे API कुंजी का नाम दे रहे हैं।

## Microsoft Foundry Models कॉन्फ़िगर करें: पोर्टल से

> **नोट:** GitHub Models जुलाई 2026 के अंत में सेवानिवृत्त हो रहे हैं। Microsoft Foundry Models इसका प्रत्यक्ष विकल्प है, जो समान मुफ्त-ट्राय मॉडल कैटलॉग और Azure AI इंफ़ेरेंस SDK / OpenAI SDK अनुभव प्रदान करता है।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) पर जाएं और Foundry प्रोजेक्ट बनाएं (या खोलें)।
1. [मॉडल कैटलॉग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ब्राउज़ करें और एक मॉडल डिप्लॉय करें, उदाहरण के लिए `gpt-4o-mini`।
1. प्रोजेक्ट के **Overview** पृष्ठ पर, **एंडपॉइंट** और **API कुंजी** कॉपी करें।
1. `.env` फ़ाइल में `AZURE_INFERENCE_ENDPOINT` के लिए एंडपॉइंट मान और `AZURE_INFERENCE_CREDENTIAL` के लिए कुंजी मान का उपयोग करें।

## ऑफ़लाइन / स्थानीय प्रदाता

यदि आप क्लाउड सदस्यता बिल्कुल उपयोग नहीं करना चाहते हैं, तो आप संगत खुले मॉडलों को सीधे अपने डिवाइस पर चला सकते हैं:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft का ऑन-डिवाइस रनटाइम। यह स्वचालित रूप से सबसे अच्छा निष्पादन प्रदाता (NPU, GPU, या CPU) चुनता है और एक OpenAI-संगत एंडपॉइंट प्रदान करता है, इसलिए आप इस पाठ्यक्रम के अधिकांश सैंपल कोड को न्यूनतम बदलाव के साथ पुन: उपयोग कर सकते हैं। आरंभ करने के लिए [Foundry Local दस्तावेज़](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) देखें, या इसे `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) के साथ इंस्टॉल करें।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, और Gemma जैसे खुले मॉडलों को स्थानीय रूप से चलाने के लिए लोकप्रिय विकल्प।


दोनों विकल्पों का उपयोग करते हुए व्यावहारिक उदाहरणों के लिए [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) देखें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->