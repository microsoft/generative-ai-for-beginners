# LLM प्रदायक छान्ने र कन्फिगर गर्ने 🔑

कार्यहरू **सक्छन्** एउटा वा बढी ठूलो भाषा मोडेल (LLM) डिप्लोइमेन्टहरू विरूद्ध समर्थित सेवा प्रदायक जस्तै OpenAI, Azure वा Hugging Face मार्फत काम गर्ने गरी सेटअप गरिने। यीले एक _होस्ट गरिएको अन्तबिन्दु_ (API) प्रदान गर्दछन् जुन हामी सहि प्रमाणीकरण विवरण (API कुञ्जी वा टोकन) संग प्रोग्रामिङमार्फत पहुँच गर्न सक्छौं। यो कोर्षमा हामी यी प्रदायकहरूको चर्चा गर्छौं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विभिन्न मोडेलहरूसहित मुख्य GPT शृंखला सहित।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मोडेलहरूका लागि, उद्यम तत्परता केन्द्रित
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एकल अन्तबिन्दु र API कुञ्जीमार्फत OpenAI, Meta, Mistral, Cohere, Microsoft र थपका सयौं मोडेलहरू पहुँच गर्न (GitHub Models लाई प्रतिस्थापन गर्दछ, जुन जुलाई २०२६ को अन्त्यमा अवसान हुँदैछ)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) खुला स्रोत मोडेल र निष्कर्ष सर्वरका लागि
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) वा [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) यदि तपाईं आफ्नो आफ्नै उपकरणमा पूर्णरूपले अफलाइन मोडेल चलाउन चाहनुहुन्छ भने, कुनै क्लाउड सदस्यता आवश्यक छैन

**यी अभ्यासहरूको लागि तपाईंले आफ्नै अकाउन्टहरू प्रयोग गर्नुपर्नेछ**। कार्यहरू वैकल्पिक छन्, त्यसैले तपाईंले आफ्नो रुचि अनुसार एक, सबै - वा कुनै पनि - प्रदायकहरू सेटअप गर्न सक्छन्। दर्ताका लागि केही मार्गदर्शन:

| दर्ता | लागत | API कुञ्जी | खेल मैदान | टिप्पणीहरू |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [परियोजना-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | धेरै मोडेलहरू उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK छिटो प्रारम्भ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडियो छिटो प्रारम्भ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहिले पहुँचका लागि आवेदन दिनु आवश्यक](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [परियोजना अवलोकन पृष्ठ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry खेल मैदान](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | नि:शुल्क तह उपलब्ध; धेरै मोडेल प्रदायकहरूसँग एक अन्तबिन्दु + कुञ्जी |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [पहुँच टोकनहरू](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat का सीमित मोडेलहरू छन्](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | नि:शुल्क (तपाईंको उपकरणमा चल्छ) | आवश्यक छैन | [स्थानीय CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूर्ण अफलाइन, OpenAI-संग मेल खाने अन्तबिन्दु |
| | | | | |

यो रिपोजिटरीलाई विभिन्न प्रदायकहरूसँग प्रयोग गर्न कन्फिगर गर्न तलका निर्देशनहरू पालना गर्नुहोस्। विशिष्ट प्रदायक आवश्यक पर्ने कार्यहरूको फाइलनाममा यी ट्यागमध्ये एक हुनेछ:

- `aoai` - Azure OpenAI अन्तबिन्दु, कुञ्जी आवश्यक
- `oai` - OpenAI अन्तबिन्दु, कुञ्जी आवश्यक
- `hf` - Hugging Face टोकन आवश्यक
- `githubmodels` - Microsoft Foundry Models अन्तबिन्दु, कुञ्जी आवश्यक (GitHub Models जुलाई २०२६ को अन्त्यमा अवसान हुँदैछ)

तपाईं एक, कुनै पनि नभई, वा सबै प्रदायकहरू कन्फिगर गर्न सक्नुहुन्छ। सम्बन्धित कार्यहरूले अभावमा क्रेडेन्सियलहरू नहुँदा त्रुटि दिनेछन्।

## `.env` फाइल सिर्जना गर्नुहोस्

हामी मान्छौं कि तपाईंले माथिको मार्गदर्शन पहिले नै पढिसक्नुभएको छ, सम्बन्धित प्रदायकसँग दर्ता गर्नुभएको छ, र आवश्यक प्रमाणीकरण क्रेडेन्सियलहरू (API_KEY वा टोकन) प्राप्त गर्नुभएको छ। Azure OpenAI को अवस्थामा, हामी मान्नेछौं तपाईंले Azure OpenAI सेवा (अन्तबिन्दु) को वैध डिप्लोइमेन्ट पनि गर्नुभएको छ, जसमा कम्तीमा एउटा GPT मोडेल चैट पूरा गर्न तैनात गरिएको छ।

अर्को कदम तपाईँका **स्थानीय वातावरण चरहरू** निम्न अनुसार कन्फिगर गर्नु हो:

1. जाँच्नुहोस् कि रुट फोल्डरमा `.env.copy` फाइल छ, जसमा यसरी सामग्री हुन्छ:

   ```bash
   # OpenAI प्रदायक
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry मा Azure OpenAI
   ## (Azure OpenAI सेवा अब Microsoft Foundry को भाग हो: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # पूर्वनिर्धारित सेट गरिएको छ! (हालको स्थिर GA API संस्करण)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry मोडेलहरू (बहु-प्रदायक मोडेल क्याटलग, GitHub मोडेलहरूको ठाउँ लिने, जुन जुलाई 2026 को अन्त्यमा रिटायर हुन्छ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. उक्त फाइललाई तलको आदेश प्रयोग गरी `.env` मा कपी गर्नुहोस्। यो फाइल _gitignore गरिएको_ छ, जसले गोप्य जानकारी सुरक्षित राख्दछ।

   ```bash
   cp .env.copy .env
   ```

3. मानहरू भर्नुहोस् (`=` को दायाँपट्टि राखिएका स्थान ग्रहणहरू प्रतिस्थापन गर्नुहोस्) जसरी अर्को खण्डमा वर्णन गरिएको छ।

4. (वैकल्पिक) यदि तपाईं GitHub Codespaces प्रयोग गर्नुहुन्छ भने, तपाईंले वातावरण चरहरूलाई यस रिपोजिटरीसँग सम्बन्धित _Codespaces secrets_ को रूपमा बचत गर्ने विकल्प छ। त्यस्तो अवस्थामा, स्थानीय .env फाइल सेटअप गर्न आवश्यक पर्दैन। **तर यो विकल्प केवल GitHub Codespaces प्रयोग गरेमा मात्र काम गर्छ।** यदि तपाईं Docker Desktop प्रयोग गर्नुहुन्छ भने अझै .env फाइल सेटअप गर्नुपर्नेछ।

## `.env` फाइल भर्नुहोस्

के के चरहरूले के जनाउँछन् बुझ्नका लागि छिटो जाँच गरौँ:

| चर | विवरण |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यो प्रयोगकर्ताको पहुँच टोकन हो जुन तपाईंले आफ्नो प्रोफाइलमा सेटअप गर्नुभएको छ |
| OPENAI_API_KEY | यो सेवा प्रयोग गर्नको लागि गैर-Azure OpenAI अन्तबिन्दुको प्राधिकरण कुञ्जी हो |
| AZURE_OPENAI_API_KEY | त्यो सेवाको प्राधिकरण कुञ्जी हो |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI स्रोतको तैनाथ गरिएको अन्तबिन्दु हो |
| AZURE_OPENAI_DEPLOYMENT | _पाठ उत्पादन_ मोडेल डिप्लोइमेन्ट अन्तबिन्दु हो |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _पाठ एम्बेडिङ_ मोडेल डिप्लोइमेन्ट अन्तबिन्दु हो |
| AZURE_INFERENCE_ENDPOINT | तपाईंको Microsoft Foundry परियोजनाको अन्तबिन्दु हो, Microsoft Foundry Models प्रयोगको लागि |
| AZURE_INFERENCE_CREDENTIAL | तपाईंको Microsoft Foundry परियोजनाको API कुञ्जी हो |
| | |

नोट: पछिल्ला दुई Azure OpenAI चरहरूले वार्तालाप पूरा गर्न (पाठ उत्पादन) र भेक्टर खोज (एम्बेडिङहरू) का लागि डिफल्ट मोडेललाई प्रतिबिम्बित गर्दछन्। तिनीहरू सेटअप गर्ने निर्देशन सम्बन्धित कार्यहरूमा प्रदान गरिनेछ।

## Azure OpenAI कन्फिगर गर्नुहोस्: पोर्टलबाट

> **नोट:** Azure OpenAI सेवा अहिले [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) को हिस्सा हो। स्रोतहरू र डिप्लोइमेन्टहरू अझै Azure पोर्टलमा देखिन्छन्, तर दैनन्दिन मोडेल व्यवस्थापन (डिप्लोइमेन्ट, खेल मैदान, अनुगमन) अब Foundry पोर्टलमा हुन्छ, पुरानो स्वतन्त्र "Azure OpenAI Studio" स्थानमा छैन।

Azure OpenAI अन्तबिन्दु र कुञ्जी मानहरू [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा पाइन्छ, त्यसैले त्यहाँबाट सुरु गरौं।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) जानुहोस्
1. साइडबारमा (बाँया मेनु) **Keys and Endpoint** विकल्पमा क्लिक गर्नुहोस्।
1. **Show Keys** मा क्लिक गर्नुहोस् - तपाईंले तपाईंसँग KEYS 1, KEYS 2 र अन्तबिन्दु देख्नु पर्नेछ।
1. AZURE_OPENAI_API_KEY को लागि KEY 1 मान प्रयोग गर्नुहोस्
1. AZURE_OPENAI_ENDPOINT को लागि अन्तबिन्दु मान प्रयोग गर्नुहोस्

अब हामीले तैनाथ गरेका विशेष मोडेलहरूका लागि अन्तबिन्दुहरू चाहिन्छ।

1. Azure OpenAI स्रोतको लागि साइडबारमा (बायाँ मेनु) **Model deployments** विकल्पमा क्लिक गर्नुहोस्।
1. गन्तव्य पृष्ठमा, **Go to Microsoft Foundry portal** (वा **Manage Deployments**, स्रोत प्रकार अनुसार) क्लिक गर्नुहोस्।

यो तपाईंलाई Microsoft Foundry पोर्टलमा लैजान्छ, जहाँ हामी तल वर्णन गरिएको अन्य मानहरू पाउनेछौं।

## Azure OpenAI कन्फिगर गर्नुहोस्: Microsoft Foundry पोर्टलबाट

1. माथि विवरण अनुसार तपाईंको स्रोतबाट [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्।
1. हाल तैनाथ गरिएका मोडेलहरू हेर्न साइडबार (बायाँ) मा **Deployments** ट्याब क्लिक गर्नुहोस्।
1. यदि तपाईंले चाहेको मोडेल तैनाथ गरिएको छैन भने, [मोडेल कटालग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) बाट तैनाथ गर्न **Deploy model** प्रयोग गर्नुहोस्।
1. तपाईंलाई _पाठ-उत्पादन_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं: **gpt-5-mini**
1. तपाईंलाई _पाठ-एम्बेडिङ_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं **text-embedding-3-small**

अब वातावरण चरहरू अद्यावधिक गर्नुहोस् जसले प्रयोग गरिएको _डिप्लोइमेन्ट नाम_ झल्काउँछ। यो प्रायः मोडेल नामसँग उस्तै हुन्छ जबसम्म तपाईंले स्पष्ट रूपमा परिवर्तन गर्नुभएको छैन। उदाहरणका लागि:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**संपादन पछि .env फाइल सुरक्षित गर्न नबिर्सनुहोस्**। तपाईं अब फाइलबाट बाहिर निस्केर नोटबुक चलाउने निर्देशहरूमा फर्कन सक्नुहुन्छ।

## OpenAI कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको OpenAI API कुञ्जी तपाईंको [OpenAI खाता](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मा फेला पार्न सकिन्छ। यदि तपाईंसँग छैन भने, खाता दर्ता गरेर API कुञ्जी सिर्जना गर्न सक्नुहुन्छ। कुञ्जी पाएपछि, तपाईंले `.env` फाइलमा `OPENAI_API_KEY` चर भर्न सक्नुहुन्छ।

## Hugging Face कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको Hugging Face टोकन तपाईंको प्रोफाइलमा [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अन्तर्गत फेला पार्न सकिन्छ। यी सार्वजनिक रूपमा पोस्ट वा सेयर नगर्नुहोस्। यसको सट्टा, यो परियोजनाको लागि नयाँ टोकन सिर्जना गर्नुहोस् र त्यसलाई `.env` फाइलमा `HUGGING_FACE_API_KEY` चरमा कपी गर्नुहोस्। _नोट:_ यो प्राविधिक रूपमा API कुञ्जी होइन् तर प्रमाणीकरणका लागि प्रयोग हुन्छ, त्यसैले नामकरण एकनरूपताका लागि त्यहि राखिएको छ।

## Microsoft Foundry Models कन्फिगर गर्नुहोस्: पोर्टलबाट

> **नोट:** GitHub Models जुलाई २०२६ को अन्त्यमा अवसान हुँदैछ। Microsoft Foundry Models सिधा प्रतिस्थापन हो, नि:शुल्क मोडेल कटालग र Azure AI Inference SDK / OpenAI SDK अनुभव प्रदान गर्दै।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) जानुहोस् र Foundry परियोजना सिर्जना वा खोल्नुहोस्।
1. [मोडेल कटालग](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) बाट मोडेल तैनाथ गर्नुहोस्, जस्तै `gpt-5-mini`।
1. परियोजनाको **Overview** पृष्ठमा, **अन्तबिन्दु** र **API कुञ्जी** कपी गर्नुहोस्।
1. `.env` फाइलमा `AZURE_INFERENCE_ENDPOINT` को लागि अन्तबिन्दु मान र `AZURE_INFERENCE_CREDENTIAL` को लागि कुञ्जी मान प्रयोग गर्नुहोस्।

## अफलाइन / स्थानीय प्रदायकहरू

यदि तपाईं क्लाउड सदस्यता बिल्कुलै प्रयोग गर्न चाहनुहुन्न भने, तपाईं अनुकूल खुला मोडेलहरू आफ्नो आफ्नै उपकरणमा सिधै चलाउन सक्नुहुन्छ:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft को उपकरणमा चल्ने रनटाइम। यसले स्वतः सबैभन्दा उपयुक्त कार्यसम्पादन प्रदायक (NPU, GPU, वा CPU) चयन गर्छ र OpenAI-अनुकूल अन्तबिन्दु दिन्छ, जसले यस कोर्सका उदाहरण कोडहरु धेरै सानो परिवर्तनमा पुन: प्रयोग गर्न मिल्छ। सुरु गर्न [Foundry Local कागजात](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्, वा `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) प्रयोग गरेर इन्स्टल गर्नुहोस्।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, र Gemma जस्ता खुला मोडेलहरू स्थानीय रूपमा चलाउने एक लोकप्रिय विकल्प।


दुवै विकल्पहरू प्रयोग गरेर व्यावहारिक उदाहरणहरूको लागि [पाठ १९: SLMs संग निर्माण](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->