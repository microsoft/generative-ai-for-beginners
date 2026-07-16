# LLM प्रदायक छनोट र कन्फिगर गर्ने 🔑

असाइनमेन्टहरू **साथै** एक वा बढी ठूलो भाषा मोडेल (LLM) परिनियोजनहरूलाई समर्पित सेवा प्रदायक जस्तै OpenAI, Azure वा Hugging Face मार्फत काम गर्न सेटअप गर्न सकिन्छ। यीहरूले _होस्टेड इन्डपोइन्ट_ (API) प्रदान गर्छन् जुन हामीले सही प्रमाणपत्र (API की वा टोकन) सहित प्रोग्रामेटिक रूपमा पहुँच गर्न सक्छौं। यस पाठ्यक्रममा, हामी यी प्रदायकहरूलाई छलफल गर्छौं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मोडेलहरू सहित मुख्य GPT श्रृंखला।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मोडेलहरूको लागि उद्यम तत्परता केन्द्रित
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) एउटा एकल इन्डपोइन्ट र API की मार्फत OpenAI, Meta, Mistral, Cohere, Microsoft र अन्य सयौं मोडेलहरू पहुँच गर्न (GitHub Models लाई प्रतिस्थापन गर्ने, जुन जुलाई 2026 को अन्त्यमा रोकिहाल्ने छ)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) खुल्ला स्रोत मोडेलहरू र इन्फरेन्स सर्भरको लागि
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) वा [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) यदि तपाईं आफ्नो उपकरणमा पूर्ण रूपमा अफलाइन मोडेलहरू चलाउन चाहनुहुन्छ भने, क्लाउड सदस्यता आवश्यक छैन

**यी अभ्यासहरूको लागि तपाईंले आफ्नै खाता प्रयोग गर्नुपर्नेछ**। असाइनमेन्टहरू वैकल्पिक छन् त्यसैले तपाईं आफ्नो रुचि अनुसार एउटा, सबै वा कुनै पनि प्रदायक सेटअप गर्न सक्नुहुन्छ। साइनअपका लागि केही मार्गनिर्देशन:

| साइनअप | खर्च | API की | प्लेग्राउन्ड | टिप्पणीहरू |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [परियोजना-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | धेरै मोडेलहरू उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहिले नै पहुँचका लागि आवेदन दिनु पर्ने](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [परियोजना अवलोकन पृष्ठ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry प्लेग्राउन्ड](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | निशुल्क तह उपलब्ध; धेरै मोडेल प्रदायकका लागि एउटै इन्डपोइन्ट + की |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [प्रवेश टोकनहरू](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मा सीमित मोडेलहरू छन्](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | निशुल्क (तपाईंको उपकरणमा चल्छ) | आवश्यक छैन | [स्थानीय CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | पूर्ण रूपमा अफलाइन, OpenAI-अनुरूप इन्डपोइन्ट |
| | | | | |

तलका निर्देशनहरू पालना गरी यस रेपोजिटरीलाई विभिन्न प्रदायकहरूसँग प्रयोगको लागि _कन्फिगर_ गर्नुहोस्। विशेष प्रदायक आवश्यक पर्ने असाइनमेन्टहरूमा फाइलनाममा यी टैगहरूमध्ये एउटा हुनेछ:

- `aoai` - Azure OpenAI इन्डपोइन्ट, की आवश्यक
- `oai` - OpenAI इन्डपोइन्ट, की आवश्यक
- `hf` - Hugging Face टोकन आवश्यक
- `githubmodels` - Microsoft Foundry Models इन्डपोइन्ट, की आवश्यक (GitHub Models जुलाई 2026 को अन्त्यमा रोकिनेछ)

तपाईं एउटा, कुनै पनि वा सबै प्रदायकहरू कन्फिगर गर्न सक्नुहुन्छ। सम्बन्धित असाइनमेन्टहरू प्रमाणपत्रहरू नभएमा त्रुटि दिन्छन्।

## `.env` फाइल बनाउनुहोस्

हामीले माथिल्लो मार्गनिर्देशन पढेको र सम्बन्धित प्रदायकमा साइनअप गरेर आवश्यक प्रमाणपत्र (API_KEY वा टोकन) प्राप्त गरेको मान्दछौं। Azure OpenAI को अवस्थामा, हामीसँग कम्तीमा एउटा GPT मोडेल डिप्लोई गरिएको Azure OpenAI सेवा (इन्डपोइन्ट) वैध रूपमा परिनियोजित छ भनी पनि मान्दछौं।

अर्को चरण तपाईंको **स्थानीय वातावरणका चरहरू** निम्नानुसार कन्फिगर गर्नु हो:

1. मूल फोल्डरमा `.env.copy` फाइल खोज्नुहोस् जुन यस प्रकारको सामग्री हुने छ:

   ```bash
   # OpenAI प्रदायक
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## माइक्रोसफ्ट फाउन्ड्रीमा Azure OpenAI
   ## (Azure OpenAI सेवा अब माइक्रोसफ्ट फाउन्ड्रीको भाग हो: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # पूर्वनिर्धारित सेट गरिएको छ! (हालको स्थिर GA API संस्करण)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## माइक्रोसफ्ट फाउन्ड्री मोडेलहरू (बहु-प्रदायक मोडेल क्याटलग, GitHub मोडेलहरूलाई प्रतिस्थापन गर्दछ, जुन जुलाई २०२६ को अन्त्यमा बन्द हुन्छ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. तलको आदेश प्रयोग गरी उक्त फाइललाई `.env` मा कपी गर्नुहोस्। यो फाइल _gitignore-ड_ छ, जसले गुप्त विवरणहरू सुरक्षित राख्छ।

   ```bash
   cp .env.copy .env
   ```

3. मानहरू भर्नुहोस् (`=` को दायाँपट्टि रहेका प्लेसहोल्डरहरू प्रतिस्थापन गर्नुहोस्) जस्तो कि अर्को खण्डमा वर्णन गरिएको छ।

4. (वैकल्पिक) यदि तपाईं GitHub Codespaces प्रयोग गर्नुहुन्छ भने, तपाईंले आफ्नो अभिनय चरहरूलाई यस रेपोजिटरीमा सम्बन्धित _Codespaces secrets_ रूपमा सुरक्षित गर्न सक्नुहुन्छ। त्यस अवस्थामा तपाईंले स्थानीय .env फाइल सेटअप गर्नु पर्दैन। **तर, यो विकल्प केवल GitHub Codespaces प्रयोग गर्दा मात्र काम गर्छ।** डोकर डेस्कटप प्रयोग गरेमा तब पनि .env फाइल सेटअप गर्नुपर्ने हुन्छ।

## `.env` फाइलमा मानहरू भर्नुहोस्

के-कसरी चर नामले अर्थ राख्छन् छिटो हेर्नुहोस्:

| चर नाम  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | तपाईंले आफ्नो प्रोफाइलमा सेट गरेको प्रयोगकर्ता पहुँच टोकन |
| OPENAI_API_KEY | गैर-Azure OpenAI इन्डपोइन्टको लागि सेवा प्रयोगको अनुमति कुञ्जी |
| AZURE_OPENAI_API_KEY | Azure OpenAI सेवाको लागि अनुमति कुञ्जी |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI स्रोतको परिनियोजित इन्डपोइन्ट |
| AZURE_OPENAI_DEPLOYMENT | _पाठ उत्पादन_ मोडेल परिनियोजन इन्डपोइन्ट |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _पाठ एम्बेडिङ_ मोडेल परिनियोजन इन्डपोइन्ट |
| AZURE_INFERENCE_ENDPOINT | तपाईंको Microsoft Foundry परियोजनाको इन्डपोइन्ट, Microsoft Foundry Models का लागि प्रयोग हुने |
| AZURE_INFERENCE_CREDENTIAL | तपाईंको Microsoft Foundry परियोजनाको API की |
| | |

नोट: अन्तिम दुई Azure OpenAI चरहरूले क्रमशः कुराकानी पूर्तिका लागि पूर्वनिर्धारित मोडेल (पाठ उत्पादन) र भेक्टर खोज (एम्बेडिङ) जनाउँछन्। तिनीहरूको सेटअप निर्देशन सम्बन्धित असाइनमेन्टहरूमा दिइने छ।

## Azure OpenAI कन्फिगर गर्नुहोस्: पोर्टलबाट

> **नोट:** Azure OpenAI सेवा अहिले [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) को भाग हो। स्रोत र परिनियोजनहरू अझै Azure पोर्टलमा देखिन्छन्, तर दैनिक मोडेल व्यवस्थापन (परिनियोजन, प्लेग्राउन्ड, निरीक्षण) पुरानो स्वतन्त्र "Azure OpenAI स्टुडियो" को सट्टा Foundry पोर्टलमा हुन्छ।

Azure OpenAI इन्डपोइन्ट र की मानहरू [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा पाइन्छन्, त्यसैले त्यहाँबाट सुरु गरौं।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) खोल्नुहोस्
1. साइडबार (बायाँ मेनु) मा **की र इन्डपोइन्ट** विकल्पमा क्लिक गर्नुहोस्।
1. **किज देखाउनुहोस्** क्लिक गर्नुहोस् - तपाईंले KEY 1, KEY 2 र इन्डपोइन्ट देख्नुहुनेछ।
1. KEY 1 मान `AZURE_OPENAI_API_KEY` का लागि प्रयोग गर्नुहोस्
1. इन्डपोइन्ट मान `AZURE_OPENAI_ENDPOINT` का लागि प्रयोग गर्नुहोस्

पछि, हामीले परिनियोजित विशिष्ट मोडेलहरूको लागि इन्डपोइन्टहरू चाहिन्छ।

1. Azure OpenAI स्रोतको साइडबार (बायाँ मेनु) मा **मोडेल परिनियोजनहरू** विकल्पमा क्लिक गर्नुहोस्।
1. गन्तव्य पृष्ठमा, **Microsoft Foundry पोर्टल जानुहोस्** (वा **परिनियोजनहरू व्यवस्थापन गर्नुहोस्**, तपाईंको स्रोत प्रकार अनुसार)

यसले तपाईंलाई Microsoft Foundry पोर्टलमा लैजानेछ, जहाँ तल वर्णित अन्य मानहरू फेला पार्नेछौं।

## Azure OpenAI कन्फिगर गर्नुहोस्: Microsoft Foundry पोर्टलबाट

1. माथि वर्णन अनुसार तपाईंको स्रोतबाट [Microsoft Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्।
1. हाल परिनियोजित मोडेलहरू हेर्न **परिनियोजनहरू** ट्याब (साइडबार, बायाँ) क्लिक गर्नुहोस्।
1. तपाईंले चाहेको मोडेल परिनियोजित नभए, [मोडेल सूची](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) बाट **मोडेल परिनियोजन गर्नुहोस्** प्रयोग गरी परिनियोजित गर्नुहोस्।
1. तपाईंलाई एउटा _पाठ-उत्पादन_ मोडेल चाहिनेछ - हामी सिफारिस गर्छौं: **gpt-4o-mini**
1. तपाईंलाई एउटा _पाठ-एम्बेडिङ_ मोडेल चाहिनेछ - हामी सिफारिस गर्छौं **text-embedding-3-small**

अब वातावरण चरहरू अपडेट गर्नुहोस् जसले प्रयोग गरिएको _परिनियोजन नाम_ देखाउँछ। यो प्रायः मोडेल नामकै समान हुनेछ जबसम्म तपाईंले स्पष्ट रूपमा परिवर्तन गर्नुभएन। उदाहरणका लागि तपाईं हुनसक्छ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**पूरा भएपछि .env फाइल सेभ गर्न नबिर्सनुहोस्**। अब फाइल बन्द गरेर नोटबुक चलाउने निर्देशनहरूमा फर्कन सक्नुहुन्छ।

## OpenAI कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको OpenAI API की तपाईंको [OpenAI खाता](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मा पाइन्छ। यदि छैन भने, खाता साइन अप गरी API की बनाउन सक्नुहुन्छ। की पाएपछि `.env` फाइलमा `OPENAI_API_KEY` चर पूर्ति गर्नुहोस्।

## Hugging Face कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको Hugging Face टोकन तपाईंको प्रोफाइलमा [प्रवेश टोकनहरू](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अन्तर्गत पाइन्छ। यी सार्वजनिक रूपमा पोस्ट वा साझा नगर्नुहोस्। बरु, यस परियोजनाको लागि नयाँ टोकन बनाएर त्यसलाई `.env` फाइलमा `HUGGING_FACE_API_KEY` चरमा राख्नुहोस्। _नोट:_ यो प्राविधिक रूपमा API की होइन तर प्रमाणीकरणका लागि प्रयोग हुन्छ त्यसैले नामकरण तेस्तै राखिएको छ।

## Microsoft Foundry Models कन्फिगर गर्नुहोस्: पोर्टलबाट

> **नोट:** GitHub Models जुलाई 2026 को अन्त्यमा रोकिइरहेको छ। Microsoft Foundry Models यसलाई सिधा प्रतिस्थापन हो, त्यही नि:शुल्क प्रयासयोग्य मोडेल सूची र Azure AI इन्फरेन्स SDK / OpenAI SDK अनुभव प्रदान गर्दै।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस् र Foundry परियोजना सिर्जना वा खोल्नुहोस्।
1. [मोडेल सूची](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ब्राउज गरेर एउटा मोडेल जस्तै `gpt-4o-mini` परिनियोजन गर्नुहोस्।
1. परियोजनाको **अवलोकन** पृष्ठमा, **इन्डपोइन्ट** र **API की** कपी गर्नुहोस्।
1. `.env` फाइलमा `AZURE_INFERENCE_ENDPOINT` को लागि इन्डपोइन्ट मान र `AZURE_INFERENCE_CREDENTIAL` को लागि की मान राख्नुहोस्।

## अफलाइन / स्थानीय प्रदायकहरू

यदि तपाईं क्लाउड सदस्यता प्रयोग गर्न चाहन्न भने, तपाईं सिधै आफ्नो उपकरणमा मिल्ने खुला मोडेलहरू चलाउन सक्नुहुन्छ:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft को उपकरणमा चल्ने रनटाइम। यसले उत्तम कार्यान्वयन प्रदायक (NPU, GPU, वा CPU) बुझेर OpenAI-अनुरूप इन्डपोइन्ट खोल्छ, यस पाठ्यक्रमका नमूना कोडहरू न्यूनतम परिवर्तनमा पुन: प्रयोग गर्न सकिन्छ। शुरू गर्न [Foundry Local कागजात](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्, वा `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) बाट स्थापना गर्नुहोस्।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma जस्ता खुला मोडेलहरू स्थानीय रूपमा चलाउने लोकप्रिय विकल्प।


दुबै विकल्पहरू प्रयोग गरेर व्यावहारिक उदाहरणहरूको लागि [पाठ १९: SLMs सँग निर्माण गर्दै](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->