<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:52:47+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ne"
}
-->
# LLM प्रदायक छान्ने र कन्फिगर गर्ने 🔑

असाइनमेन्टहरू **एक वा बढी** ठूलो भाषा मोडेल (LLM) डिप्लोयमेन्टहरूसँग काम गर्नका लागि OpenAI, Azure वा Hugging Face जस्ता सपोर्टेड सेवा प्रदायकमार्फत सेटअप गर्न सकिन्छ। यीले _होस्ट गरिएको एन्डप्वाइन्ट_ (API) उपलब्ध गराउँछन्, जसलाई हामीले सही प्रमाणिकरण (API key वा टोकन) प्रयोग गरेर प्रोग्रामबाट पहुँच गर्न सक्छौं। यस कोर्समा, हामी यी प्रदायकहरूबारे छलफल गर्छौं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) जसमा मुख्य GPT सिरिजसहित विभिन्न मोडेलहरू छन्।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) जसले OpenAI मोडेलहरूलाई इन्टरप्राइजका लागि तयार पार्छ
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) जसले खुला-स्रोत मोडेलहरू र इन्फरेन्स सर्भर उपलब्ध गराउँछ

**यी अभ्यासहरूका लागि तपाईंले आफ्नै खाता प्रयोग गर्नुपर्नेछ।** असाइनमेन्टहरू वैकल्पिक छन्, त्यसैले तपाईं आफ्नो रुचिअनुसार एक, सबै, वा कुनै पनि प्रदायक सेटअप गर्न सक्नुहुन्छ। साइनअपका लागि केही सुझाव:

| साइनअप | लागत | API Key | Playground | टिप्पणीहरू |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | धेरै मोडेलहरू उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहिले नै पहुँचको लागि आवेदन दिनुपर्छ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मा सीमित मोडेलहरू छन्](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

तलका निर्देशनहरू पालना गरेर यो रिपोजिटरीलाई फरक-फरक प्रदायकसँग प्रयोग गर्न _कन्फिगर_ गर्नुहोस्। कुनै असाइनमेन्टमा यदि विशेष प्रदायक आवश्यक छ भने, त्यसको फाइलनाममा यीमध्ये कुनै ट्याग हुनेछ:

- `aoai` - Azure OpenAI endpoint, key आवश्यक
- `oai` - OpenAI endpoint, key आवश्यक
- `hf` - Hugging Face token आवश्यक

तपाईं एक, कुनै पनि, वा सबै प्रदायक कन्फिगर गर्न सक्नुहुन्छ। सम्बन्धित असाइनमेन्टहरूमा प्रमाणिकरण नभएमा त्रुटि देखिनेछ।

## `.env` फाइल बनाउनुहोस्

हामी मान्छौं कि तपाईंले माथिको निर्देशन पढिसक्नुभएको छ र सम्बन्धित प्रदायकमा साइनअप गरेर आवश्यक प्रमाणिकरण (API_KEY वा टोकन) प्राप्त गर्नुभएको छ। Azure OpenAI को हकमा, तपाईंले कम्तिमा एउटा GPT मोडेल डिप्लोय गरिएको Azure OpenAI Service (endpoint) पनि बनाइसक्नुभएको छ भन्ने मानिन्छ।

अब तपाईंको **स्थानीय environment variables** यसरी कन्फिगर गर्नुहोस्:

1. मूल फोल्डरमा `.env.copy` फाइल खोज्नुहोस्, जसको सामग्री यस प्रकारको हुनेछ:

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

2. तलको कमाण्ड प्रयोग गरेर त्यो फाइललाई `.env` मा प्रतिलिपि गर्नुहोस्। यो फाइल _gitignore_ गरिएको छ, जसले गोप्य जानकारी सुरक्षित राख्छ।

   ```bash
   cp .env.copy .env
   ```

3. तलको खण्डमा वर्णन गरिएअनुसार मानहरू (दायाँपट्टि `=` पछिका placeholder हरू) भर्नुहोस्।

4. (वैकल्पिक) यदि तपाईं GitHub Codespaces प्रयोग गर्नुहुन्छ भने, environment variables लाई _Codespaces secrets_ को रूपमा यो रिपोजिटरीसँग जोड्न सक्नुहुन्छ। त्यस अवस्थामा, तपाईंलाई स्थानीय .env फाइल सेटअप गर्न आवश्यक पर्दैन। **तर, यो विकल्प केवल GitHub Codespaces मा मात्र काम गर्छ।** यदि तपाईं Docker Desktop प्रयोग गर्नुहुन्छ भने, .env फाइल सेटअप गर्नैपर्छ।

## `.env` फाइल भर्नुहोस्

अब हामी variable नामहरू के जनाउँछन् भनेर छिटो हेरौं:

| Variable  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | तपाईंको प्रोफाइलमा सेटअप गरिएको user access token |
| OPENAI_API_KEY | non-Azure OpenAI endpoint हरूका लागि सेवा प्रयोग गर्नको लागि authorization key |
| AZURE_OPENAI_API_KEY | सो सेवा प्रयोग गर्नको लागि authorization key |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI resource को डिप्लोय गरिएको endpoint |
| AZURE_OPENAI_DEPLOYMENT | _text generation_ मोडेलको deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _text embeddings_ मोडेलको deployment endpoint |
| | |

नोट: अन्तिम दुई Azure OpenAI variable हरूले क्रमशः chat completion (text generation) र vector search (embeddings) का लागि default मोडेल जनाउँछन्। तिनीहरू सेटअप गर्ने निर्देशन सम्बन्धित असाइनमेन्टहरूमा दिइनेछ।

## Azure कन्फिगर गर्नुहोस्: Portal बाट

Azure OpenAI endpoint र key मानहरू [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा भेटिन्छन्, त्यसैले त्यहाँबाट सुरु गरौं।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्
1. साइडबार (बायाँ मेनु) मा **Keys and Endpoint** विकल्पमा क्लिक गर्नुहोस्।
1. **Show Keys** मा क्लिक गर्नुहोस् - तपाईंले KEY 1, KEY 2 र Endpoint देख्नुहुनेछ।
1. AZURE_OPENAI_API_KEY का लागि KEY 1 को मान प्रयोग गर्नुहोस्
1. AZURE_OPENAI_ENDPOINT का लागि Endpoint को मान प्रयोग गर्नुहोस्

अब, हामीले डिप्लोय गरेका विशेष मोडेलहरूको endpoint चाहिन्छ।

1. Azure OpenAI resource को साइडबार (बायाँ मेनु) मा **Model deployments** विकल्पमा क्लिक गर्नुहोस्।
1. गन्तव्य पेजमा **Manage Deployments** मा क्लिक गर्नुहोस्

यसले तपाईंलाई Azure OpenAI Studio वेबसाइटमा लैजान्छ, जहाँ हामी तल वर्णन गरिएअनुसार अन्य मानहरू पत्ता लगाउँछौं।

## Azure कन्फिगर गर्नुहोस्: Studio बाट

1. माथि वर्णन गरेअनुसार **आफ्नो resource** बाट [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्।
1. साइडबार (बायाँ) मा **Deployments** ट्याबमा क्लिक गर्नुहोस्, हाल डिप्लोय भएका मोडेलहरू हेर्न।
1. यदि तपाईंले चाहेको मोडेल डिप्लोय गरिएको छैन भने, **Create new deployment** प्रयोग गरेर डिप्लोय गर्नुहोस्।
1. तपाईंलाई _text-generation_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं: **gpt-35-turbo**
1. तपाईंलाई _text-embedding_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं **text-embedding-ada-002**

अब environment variables लाई _Deployment name_ अनुसार अपडेट गर्नुहोस्। यो सामान्यतया मोडेल नामकै जस्तै हुन्छ, जबसम्म तपाईंले परिवर्तन गर्नुभएको छैन। उदाहरणका लागि, तपाईंको मान यसरी हुन सक्छ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**काम सकिएपछि .env फाइल सुरक्षित गर्न नबिर्सनुहोस्।** अब तपाईं फाइलबाट निस्कन सक्नुहुन्छ र नोटबुक चलाउने निर्देशनमा फर्कन सक्नुहुन्छ।

## OpenAI कन्फिगर गर्नुहोस्: Profile बाट

तपाईंको OpenAI API key तपाईंको [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मा भेटिन्छ। यदि छैन भने, खाता बनाएर API key बनाउन सक्नुहुन्छ। एकपटक key पाएपछि, त्यसलाई `.env` फाइलको `OPENAI_API_KEY` variable मा राख्नुहोस्।

## Hugging Face कन्फिगर गर्नुहोस्: Profile बाट

तपाईंको Hugging Face token तपाईंको प्रोफाइलको [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) मा भेटिन्छ। यी सार्वजनिक रूपमा नपोस्ट गर्नुहोस् वा नबाँड्नुहोस्। बरु, यस प्रोजेक्टका लागि नयाँ टोकन बनाएर `.env` फाइलमा `HUGGING_FACE_API_KEY` variable अन्तर्गत राख्नुहोस्। _नोट:_ यो प्राविधिक रूपमा API key होइन, तर authentication का लागि प्रयोग हुन्छ, त्यसैले नाममा निरन्तरता राख्न यसैलाई राखिएको छ।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।