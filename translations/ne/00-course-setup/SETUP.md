<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:45:24+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ne"
}
-->
# आफ्नो विकास वातावरण सेटअप गर्नुहोस्

हामीले यो रिपोजिटरी र कोर्सलाई [विकास कन्टेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) सँग सेटअप गरेका छौं जसले Python3, .NET, Node.js, र Java विकासलाई समर्थन गर्न सक्ने युनिभर्सल रनटाइम समावेश गर्दछ। सम्बन्धित कन्फिगरेसन यो रिपोजिटरीको मूलमा रहेको `devcontainer.json` फाइलमा `.devcontainer/` फोल्डरमा परिभाषित गरिएको छ।

डेभ कन्टेनर सक्रिय गर्न, यसलाई [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्टेड रनटाइमको लागि) वा [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (स्थानीय उपकरण-होस्टेड रनटाइमको लागि) मा सुरु गर्नुहोस्। VS Code भित्र डेभ कन्टेनर कसरी काम गर्छ भन्ने बारे थप विवरणको लागि [यो दस्तावेज](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) पढ्नुहोस्।

> [!TIP]  
> न्यूनतम प्रयासमा छिटो सुरु गर्न GitHub Codespaces प्रयोग गर्न सिफारिस गरिन्छ। यसले व्यक्तिगत खाताहरूको लागि उदार [नि:शुल्क प्रयोग कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान गर्दछ। आफ्नो कोटा प्रयोगलाई अधिकतम गर्न निष्क्रिय कोडस्पेसहरू रोक्न वा मेटाउन [समय-सीमाहरू](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कन्फिगर गर्नुहोस्।

## 1. असाइनमेन्टहरू कार्यान्वयन गर्दै

प्रत्येक पाठमा _वैकल्पिक_ असाइनमेन्टहरू हुनेछन् जुन एक वा बढी प्रोग्रामिङ भाषाहरूमा प्रदान गर्न सकिन्छ: Python, .NET/C#, Java, र JavaScript/TypeScript। यस खण्डले ती असाइनमेन्टहरू कार्यान्वयन गर्न सम्बन्धित सामान्य मार्गदर्शन प्रदान गर्दछ।

### 1.1 Python असाइनमेन्टहरू

Python असाइनमेन्टहरू एप्लिकेसनहरू (`.py` फाइलहरू) वा Jupyter नोटबुकहरू (`.ipynb` फाइलहरू) को रूपमा प्रदान गरिन्छ।
- नोटबुक चलाउनको लागि, यसलाई Visual Studio Code मा खोल्नुहोस् र त्यसपछि _Select Kernel_ (उपल्लो दायाँमा) क्लिक गर्नुहोस् र देखाइएको डिफल्ट Python 3 विकल्प चयन गर्नुहोस्। अब तपाईं नोटबुक कार्यान्वयन गर्न _Run All_ गर्न सक्नुहुन्छ।
- कमाण्ड-लाइनबाट Python एप्लिकेसनहरू चलाउन, असाइनमेन्ट-विशिष्ट निर्देशनहरू पालना गर्नुहोस् सही फाइलहरू चयन गर्न र आवश्यक तर्कहरू प्रदान गर्न।

## 2. प्रदायकहरू कन्फिगर गर्दै

असाइनमेन्टहरू **साथै** एक वा बढी ठूलो भाषा मोडेल (LLM) परिनियोजनहरू विरुद्ध काम गर्न सेटअप गर्न सकिन्छ, जस्तै OpenAI, Azure वा Hugging Face जस्ता समर्थित सेवा प्रदायक मार्फत। यी _होस्टेड एन्डपॉइन्ट_ (API) प्रदान गर्छन् जुन हामी सही प्रमाणपत्रहरू (API key वा टोकन) संग प्रोग्रामेटिक रूपमा पहुँच गर्न सक्छौं। यस कोर्समा, हामी यी प्रदायकहरूको चर्चा गर्छौं:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विभिन्न मोडेलहरू सहित, मुख्य GPT श्रृंखला सहित।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मोडेलहरूको लागि उद्यम तत्परता केन्द्रित गर्दै
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) खुला-स्रोत मोडेलहरू र इन्फरेन्स सर्भरको लागि

**तपाईंलाई यी अभ्यासहरूको लागि आफ्नै खाताहरू प्रयोग गर्न आवश्यक हुनेछ**। असाइनमेन्टहरू वैकल्पिक छन् त्यसैले तपाईं आफ्नो रुचि अनुसार एक, सबै - वा कुनै पनि प्रदायक सेटअप गर्न छनौट गर्न सक्नुहुन्छ। साइनअपको लागि केही मार्गदर्शन:

| साइनअप | लागत | API Key | Playground | टिप्पणीहरू |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | धेरै मोडेलहरू उपलब्ध छन् |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहिले पहुँचको लागि आवेदन दिनु पर्छ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [एक्सेस टोकनहरू](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatसँग सीमित मोडेलहरू छन्](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

विभिन्न प्रदायकहरूसँग प्रयोगको लागि यो रिपोजिटरी _कन्फिगर_ गर्न तलका निर्देशनहरू पालना गर्नुहोस्। विशेष प्रदायक आवश्यक पर्ने असाइनमेन्टहरूमा ती फाइलनाममा यी ट्यागहरू मध्ये एक हुनेछ:
 - `aoai` - Azure OpenAI एन्डपॉइन्ट, की आवश्यक छ
 - `oai` - OpenAI एन्डपॉइन्ट, की आवश्यक छ
 - `hf` - Hugging Face टोकन आवश्यक छ

तपाईं एक, कुनै, वा सबै प्रदायकहरू कन्फिगर गर्न सक्नुहुन्छ। सम्बन्धित असाइनमेन्टहरू केवल अनुपस्थित प्रमाणपत्रहरूमा त्रुटि देखाउनेछन्।

###  2.1. `.env` फाइल सिर्जना गर्नुहोस्

हामीले माथि उल्लेखित मार्गदर्शन पढेर सम्बन्धित प्रदायकसँग साइन अप गरिसकेको छौं, र आवश्यक प्रमाणपत्रहरू (API_KEY वा टोकन) प्राप्त गरेका छौं भन्ने मान्दछौं। Azure OpenAI को मामलामा, हामीले कम्तिमा एक GPT मोडेल च्याट पूर्णताको लागि परिनियोजित गरेर Azure OpenAI सेवा (एन्डपॉइन्ट) को मान्य परिनियोजन पनि छ भन्ने मान्दछौं।

अर्को चरण भनेको **स्थानीय वातावरण चरहरू** निम्नानुसार कन्फिगर गर्नु हो:

1. मूल फोल्डरमा `.env.copy` फाइल हेर्नुहोस् जसमा यस प्रकारको सामग्री हुनेछ:

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

2. तलको आदेश प्रयोग गरेर त्यो फाइललाई `.env` मा प्रतिलिपि गर्नुहोस्। यो फाइल _gitignore-d_ गरिएको छ, गोप्य कुराहरू सुरक्षित राख्दै।

   ```bash
   cp .env.copy .env
   ```

3. मूल्यहरू भर्नुहोस् (दायाँपट्टि `=` को प्लेसहोल्डरहरू प्रतिस्थापन गर्नुहोस्) जस्तो कि अर्को खण्डमा वर्णन गरिएको छ।

3. (विकल्प) यदि तपाईं GitHub Codespaces प्रयोग गर्नुहुन्छ भने, तपाईंको खातासँग सम्बन्धित _Codespaces secrets_ रूपमा वातावरण चरहरू सुरक्षित गर्ने विकल्प छ। त्यस अवस्थामा, तपाईंलाई स्थानीय .env फाइल सेटअप गर्न आवश्यक हुनेछैन। **तर, ध्यान दिनुहोस् कि यो विकल्प केवल GitHub Codespaces प्रयोग गरेमा मात्र काम गर्दछ।** यदि तपाईं Docker Desktop प्रयोग गर्नुहुन्छ भने तपाईंलाई अझै .env फाइल सेटअप गर्न आवश्यक छ।

### 2.2. `.env` फाइलमा भरपर्दा

चर नामहरू के प्रतिनिधित्व गर्छन् भन्ने बुझ्नको लागि छिटो हेरौं:

| चर  | विवरण  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यो तपाईंको प्रोफाइलमा सेटअप गरिएको प्रयोगकर्ता एक्सेस टोकन हो |
| OPENAI_API_KEY | यो सेवा प्रयोगको लागि गैर-Azure OpenAI एन्डपॉइन्टहरूको लागि प्राधिकरण की हो |
| AZURE_OPENAI_API_KEY | यो सेवा प्रयोगको लागि प्राधिकरण की हो |
| AZURE_OPENAI_ENDPOINT | यो Azure OpenAI स्रोतको लागि परिनियोजित एन्डपॉइन्ट हो |
| AZURE_OPENAI_DEPLOYMENT | यो _पाठ उत्पादन_ मोडेल परिनियोजन एन्डपॉइन्ट हो |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यो _पाठ एम्बेडिङ_ मोडेल परिनियोजन एन्डपॉइन्ट हो |
| | |

टिप्पणी: अन्तिम दुई Azure OpenAI चरहरूले क्रमशः च्याट पूर्णता (पाठ उत्पादन) र भेक्टर खोज (एम्बेडिङहरू) को लागि डिफल्ट मोडेललाई प्रतिबिम्बित गर्छन्। तिनीहरू सेटअप गर्ने निर्देशनहरू सम्बन्धित असाइनमेन्टहरूमा परिभाषित गरिनेछ।

### 2.3 Azure कन्फिगर गर्नुहोस्: पोर्टलबाट

Azure OpenAI एन्डपॉइन्ट र की मानहरू [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा फेला पारिनेछन् त्यसैले सुरु गरौं।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्
1. साइडबारमा (बायाँ मेनुमा) **Keys and Endpoint** विकल्प क्लिक गर्नुहोस्।
1. **Show Keys** क्लिक गर्नुहोस् - तपाईंले निम्न देख्नु पर्नेछ: KEY 1, KEY 2 र एन्डपॉइन्ट।
1. AZURE_OPENAI_API_KEY को लागि KEY 1 मान प्रयोग गर्नुहोस्
1. AZURE_OPENAI_ENDPOINT को लागि एन्डपॉइन्ट मान प्रयोग गर्नुहोस्

अब हामीले परिनियोजित मोडेलहरूको लागि एन्डपॉइन्टहरू चाहिन्छ।

1. Azure OpenAI स्रोतको लागि साइडबार (बायाँ मेनु) मा **Model deployments** विकल्प क्लिक गर्नुहोस्।
1. गन्तव्य पृष्ठमा, **Manage Deployments** क्लिक गर्नुहोस्

यसले तपाईंलाई Azure OpenAI Studio वेबसाइटमा लैजान्छ, जहाँ हामी तल वर्णन गरिएका अन्य मानहरू पत्ता लगाउँछौं।

### 2.4 Azure कन्फिगर गर्नुहोस्: स्टुडियोबाट

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) मा **तपाईंको स्रोतबाट** माथि वर्णन गरिएको अनुसार जानुहोस्।
1. हाल परिनियोजित मोडेलहरू हेर्न **Deployments** ट्याब (साइडबार, बायाँ) क्लिक गर्नुहोस्।
1. यदि तपाईंको इच्छित मोडेल परिनियोजित छैन भने, **Create new deployment** प्रयोग गरेर यसलाई परिनियोजित गर्नुहोस्।
1. तपाईंलाई _पाठ-उत्पादन_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं: **gpt-35-turbo**
1. तपाईंलाई _पाठ-एम्बेडिङ_ मोडेल चाहिन्छ - हामी सिफारिस गर्छौं **text-embedding-ada-002**

अब वातावरण चरहरू परिनियोजन नामलाई प्रतिबिम्बित गर्न अद्यावधिक गर्नुहोस्। यो सामान्यतया मोडेल नामसँग समान हुनेछ जबसम्म तपाईंले यसलाई स्पष्ट रूपमा परिवर्तन गर्नुभएको छैन। त्यसैले, उदाहरणको रूपमा, तपाईंको यो हुन सक्छ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**समाप्त हुँदा .env फाइल बचत गर्न नबिर्सनुहोस्**। अब तपाईं फाइलबाट बाहिर निस्कन सक्नुहुन्छ र नोटबुक चलाउने निर्देशनहरूमा फर्कन सक्नुहुन्छ।

### 2.5 OpenAI कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको OpenAI API key तपाईंको [OpenAI खाता](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मा फेला पार्न सकिन्छ। यदि तपाईंसँग छैन भने, तपाईं खाता खोल्न र API key सिर्जना गर्न साइन अप गर्न सक्नुहुन्छ। एकपटक तपाईंसँग की भए पछि, तपाईं यसलाई `.env` फाइलमा `OPENAI_API_KEY` चरमा भरपर्दा प्रयोग गर्न सक्नुहुन्छ।

### 2.6 Hugging Face कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको Hugging Face टोकन तपाईंको प्रोफाइलमा [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अन्तर्गत फेला पार्न सकिन्छ। यी सार्वजनिक रूपमा पोस्ट वा साझा नगर्नुहोस्। यसको सट्टा, यस परियोजना प्रयोगको लागि नयाँ टोकन सिर्जना गर्नुहोस् र `.env` फाइलमा `HUGGING_FACE_API_KEY` चर अन्तर्गत त्यसलाई प्रतिलिपि गर्नुहोस्। _टिप्पणी:_ यो प्राविधिक रूपमा API key होइन तर प्रमाणीकरणको लागि प्रयोग गरिन्छ त्यसैले हामी निरन्तरताका लागि त्यो नामकरण परम्परा कायम राख्दैछौं।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा असत्यताहरू हुन सक्छ। यसको मूल भाषामा रहेको दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।