<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:14:33+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ne"
}
-->
# आफ्नो विकास वातावरण सेटअप गर्नुहोस्

हामीले यो रिपोजिटरी र कोर्सलाई [विकास कन्टेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) को साथ सेटअप गरेका छौं जसमा युनिभर्सल रनटाइम छ जुन Python3, .NET, Node.js र Java विकासलाई समर्थन गर्न सक्छ। सम्बन्धित कन्फिगरेसन यो रिपोजिटरीको रूटमा रहेको `.devcontainer/` फोल्डरमा रहेको `devcontainer.json` फाइलमा परिभाषित गरिएको छ।

डेभ कन्टेनर सक्रिय गर्न, यसलाई [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (क्लाउड-होस्ट गरिएको रनटाइमको लागि) वा [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (स्थानीय उपकरण-होस्ट गरिएको रनटाइमको लागि) मा लन्च गर्नुहोस्। VS Code भित्र डेभ कन्टेनर कसरी काम गर्छ भन्ने थप विवरणको लागि [यो डकुमेन्टेशन](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) पढ्नुहोस्।

> [!TIP]  
> न्यूनतम प्रयासमा छिटो सुरु गर्नका लागि हामी GitHub Codespaces प्रयोग गर्न सिफारिस गर्दछौं। यसले व्यक्तिगत खाताहरूको लागि उदार [निःशुल्क प्रयोग कोटा](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) प्रदान गर्दछ। आफ्नो कोटा प्रयोगलाई अधिकतम बनाउन निष्क्रिय कोडस्पेसहरू रोक्न वा मेटाउन [समय सीमा](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) कन्फिगर गर्नुहोस्।

## १. असाइनमेन्टहरू कार्यान्वयन गर्दै

प्रत्येक पाठमा एक वा बढी प्रोग्रामिङ भाषाहरूमा दिइन सक्ने _वैकल्पिक_ असाइनमेन्टहरू हुनेछन्, जस्तै: Python, .NET/C#, Java र JavaScript/TypeScript। यो खण्डले ती असाइनमेन्टहरू कार्यान्वयनसँग सम्बन्धित सामान्य मार्गदर्शन प्रदान गर्दछ।

### १.१ Python असाइनमेन्टहरू

Python असाइनमेन्टहरू एप्लिकेसनहरू (`.py` फाइलहरू) वा Jupyter नोटबुकहरू (`.ipynb` फाइलहरू) को रूपमा प्रदान गरिन्छन्।
- नोटबुक चलाउन, यसलाई Visual Studio Code मा खोल्नुहोस् र त्यसपछि _Select Kernel_ (माथिल्लो दायाँमा) क्लिक गर्नुहोस् र देखाइएको डिफल्ट Python 3 विकल्प चयन गर्नुहोस्। अब तपाईं _Run All_ क्लिक गरेर नोटबुक चलाउन सक्नुहुन्छ।
- कमाण्ड-लाइनबाट Python एप्लिकेसनहरू चलाउन, निश्चित गर्नुहोस् कि तपाईंले सही फाइलहरू चयन गर्नुभएको छ र आवश्यक आर्गुमेन्टहरू प्रदान गर्नुभएको छ भन्ने सुनिश्चित गर्न असाइनमेन्ट-विशिष्ट निर्देशनहरू पालना गर्नुहोस्।

## २. प्रदायकहरू कन्फिगर गर्दै

असाइनमेन्टहरू **सक्छन्** पनि एक वा बढी ठूला भाषा मोडेल (LLM) डिप्लोइमेन्टहरू विरुद्ध समर्थित सेवा प्रदायक जस्तै OpenAI, Azure वा Hugging Face मार्फत काम गर्न सेटअप गरिन सक्छन्। यीले हामीले सही प्रमाणपत्रहरू (API key वा टोकन) का साथ प्रोग्रामेटिक रूपमा पहुँच गर्न सक्ने _होस्ट गरिएको अन्तबिन्दु_ (API) प्रदान गर्छन्। यस कोर्समा, हामी यी प्रदायकहरू छलफल गर्छौं:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) विविध मोडेलहरूसँग, जसमा कोर GPT श्रृंखला समावेश छ।
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI मोडेलहरूको लागि उद्यम तयारीमा केन्द्रित
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) खुला स्रोत मोडेलहरू र इन्फरेन्स सर्भरको लागि

**तपाईंलाई यी अभ्यासहरूको लागि आफ्नै खाताहरू प्रयोग गर्न आवश्यक हुनेछ**। असाइनमेन्टहरू वैकल्पिक छन् त्यसैले तपाईं आफ्नो चासोका आधारमा एउटा, सबै - वा कुनै पनि - प्रदायकहरू सेटअप गर्न चयन गर्न सक्नुहुन्छ। साइनअपको लागि केही मार्गदर्शन:

| साइनअप | लागत | API Key | प्लेग्राउन्ड | टिप्पणीहरू |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [प्रोजेक्ट-आधारित](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [नो-कोड, वेब](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | विभिन्न मोडेलहरू उपलब्ध |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [मूल्य निर्धारण](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [स्टुडियो क्विकस्टार्ट](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [पहिले नै पहुँचको लागि आवेदन दिनु पर्छ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [मूल्य निर्धारण](https://huggingface.co/pricing) | [प्रवेश टोकनहरू](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat मा सीमित मोडेलहरू छन्](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

विभिन्न प्रदायकहरूसँग प्रयोगको लागि यो रिपोजिटरी _कन्फिगर_ गर्न तलका निर्देशनहरू पालना गर्नुहोस्। विशेष प्रदायक आवश्यक पर्ने असाइनमेन्टहरूमा तिनीहरूको फाइलनाममा यी ट्यागहरू मध्ये एक हुनेछ:

- `aoai` - Azure OpenAI अन्तबिन्दु, कुञ्जी आवश्यक छ
- `oai` - OpenAI अन्तबिन्दु, कुञ्जी आवश्यक छ
- `hf` - Hugging Face टोकन आवश्यक छ

तपाईं एक, कुनै पनि, वा सबै प्रदायकहरू कन्फिगर गर्न सक्नुहुन्छ। सम्बन्धित असाइनमेन्टहरू केवल हराइरहेका प्रमाणपत्रहरूमा त्रुटि उत्पन्न हुनेछ।

### २.१. `.env` फाइल बनाउनुहोस्

हामी मान्दछौं कि तपाईंले माथिको मार्गदर्शन पहिले नै पढ्नु भएको छ र सम्बन्धित प्रदायकसँग साइन अप गर्नुभएको छ, र आवश्यक प्रमाणीकरण प्रमाणपत्रहरू (API_KEY वा टोकन) प्राप्त गर्नुभएको छ। Azure OpenAI को हकमा, हामी मान्दछौं कि तपाईंले कम्तिमा एक GPT मोडेल डिप्लोइ गरिएको Azure OpenAI सेवा (अन्तबिन्दु) को मान्य डिप्लोइमेन्ट पनि छ।

अर्को चरण भनेको तपाईंको **स्थानीय वातावरण भेरिएबलहरू** तलको रूपमा कन्फिगर गर्नु हो:

1. रूट फोल्डरमा हेर्नुहोस् `.env.copy` फाइलको लागि जसको सामग्री यस प्रकारको हुनुपर्छ:

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

2. तलको कमाण्ड प्रयोग गरेर त्यो फाइललाई `.env` मा प्रतिलिपि गर्नुहोस्। यो फाइल _gitignore-d_ छ, जसले गोप्य कुराहरू सुरक्षित राख्छ।

   ```bash
   cp .env.copy .env
   ```

3. तलको खण्डमा वर्णन गरिएका अनुसार मानहरू भर्नुहोस् (दायाँपट्टि `=` को स्थानमा राखिएको प्लेसहोल्डरहरू प्रतिस्थापन गर्नुहोस्)।

3. (विकल्प) यदि तपाईं GitHub Codespaces प्रयोग गर्नुहुन्छ भने, तपाईंले यस रिपोजिटरीसँग सम्बन्धित _Codespaces गोप्य_ रूपमा वातावरण भेरिएबलहरू बचत गर्ने विकल्प छ। यस अवस्थामा, तपाईंले स्थानीय .env फाइल सेटअप गर्न आवश्यक हुनेछैन। **यद्यपि, ध्यान दिनुहोस् कि यो विकल्प केवल तपाईंले GitHub Codespaces प्रयोग गरेमा मात्र काम गर्छ।** तपाईंले Docker Desktop प्रयोग गरेमा पनि .env फाइल सेटअप गर्न आवश्यक हुनेछ।

### २.२. `.env` फाइल भर्नुहोस्

भेरिएबल नामहरू के प्रतिनिधित्व गर्छन् भनेर बुझ्नका लागि छिटो हेरौं:

| भेरिएबल | विवरण |
| :--- | :--- |
| HUGGING_FACE_API_KEY | यो तपाईंको प्रोफाइलमा सेटअप गरिएको प्रयोगकर्ता पहुँच टोकन हो |
| OPENAI_API_KEY | यो गैर-Azure OpenAI अन्तबिन्दुहरूको लागि सेवा प्रयोग गर्नको लागि प्रमाणीकरण कुञ्जी हो |
| AZURE_OPENAI_API_KEY | यो सेवा प्रयोग गर्नको लागि प्रमाणीकरण कुञ्जी हो |
| AZURE_OPENAI_ENDPOINT | यो Azure OpenAI स्रोतको लागि डिप्लोइ गरिएको अन्तबिन्दु हो |
| AZURE_OPENAI_DEPLOYMENT | यो _पाठ उत्पादन_ मोडेल डिप्लोइमेन्ट अन्तबिन्दु हो |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | यो _पाठ इम्बेडिङ_ मोडेल डिप्लोइमेन्ट अन्तबिन्दु हो |
| | |

नोट: अन्तिम दुई Azure OpenAI भेरिएबलहरू क्रमशः च्याट पूरा (पाठ उत्पादन) र भेक्टर खोज (इम्बेडिङ) को लागि डिफल्ट मोडेललाई प्रतिबिम्बित गर्छन्। तिनीहरू सेटअप गर्ने निर्देशनहरू सम्बन्धित असाइनमेन्टहरूमा परिभाषित गरिनेछ।

### २.३ Azure कन्फिगर गर्नुहोस्: पोर्टलबाट

Azure OpenAI अन्तबिन्दु र कुञ्जी मानहरू [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा फेला पार्न सकिन्छ त्यसैले त्यहाँबाट सुरु गरौं।

1. [Azure पोर्टल](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्
1. साइडबार (बायाँतिरको मेनु) मा **Keys and Endpoint** विकल्प क्लिक गर्नुहोस्।
1. **Show Keys** क्लिक गर्नुहोस् - तपाईंले निम्न देख्नु पर्छ: KEY 1, KEY 2 र Endpoint।
1. AZURE_OPENAI_API_KEY को लागि KEY 1 मान प्रयोग गर्नुहोस्
1. AZURE_OPENAI_ENDPOINT को लागि Endpoint मान प्रयोग गर्नुहोस्

अर्को, हामीले डिप्लोइ गरिएको विशेष मोडेलहरूको लागि अन्तबिन्दुहरू आवश्यक छ।

1. Azure OpenAI स्रोतको लागि साइडबार (बायाँ मेनु) मा **Model deployments** विकल्प क्लिक गर्नुहोस्।
1. गन्तव्य पृष्ठमा, **Manage Deployments** क्लिक गर्नुहोस्

यसले तपाईंलाई Azure OpenAI स्टुडियो वेबसाइटमा लैजान्छ, जहाँ हामीले तल वर्णन गरिएका अन्य मानहरू फेला पार्नेछौं।

### २.४ Azure कन्फिगर गर्नुहोस्: स्टुडियोबाट

1. माथि वर्णन गरे अनुसार **तपाईंको स्रोतबाट** [Azure OpenAI स्टुडियो](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्।
1. हाल डिप्लोइ गरिएका मोडेलहरू हेर्न **Deployments** ट्याब (साइडबार, बायाँ) क्लिक गर्नुहोस्।
1. यदि तपाईंको इच्छित मोडेल डिप्लोइ गरिएको छैन भने, **Create new deployment** प्रयोग गरेर यसलाई डिप्लोइ गर्नुहोस्।
1. तपाईंलाई _पाठ-उत्पादन_ मोडेल आवश्यक छ - हामी सिफारिस गर्छौं: **gpt-35-turbo**
1. तपाईंलाई _पाठ-इम्बेडिङ_ मोडेल आवश्यक छ - हामी सिफारिस गर्छौं **text-embedding-ada-002**

अब वातावरण भेरिएबलहरूलाई डिप्लोइमेन्ट नाम प्रतिबिम्बित गर्न अपडेट गर्नुहोस्। यो प्रायः मोडेल नाम जस्तै हुनेछ जबसम्म तपाईंले यसलाई स्पष्ट रूपमा परिवर्तन गर्नुभएको छैन। त्यसैले, उदाहरणको रूपमा, तपाईंले यस प्रकारको हुन सक्छ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**सम्पन्न भएपछि .env फाइल बचत गर्न नबिर्सनुहोस्**। अब तपाईं फाइलबाट बाहिर निस्कन सक्नुहुन्छ र नोटबुक चलाउने निर्देशनहरूमा फर्कन सक्नुहुन्छ।

### २.५ OpenAI कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको OpenAI API कुञ्जी तपाईंको [OpenAI खाता](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) मा फेला पार्न सकिन्छ। यदि तपाईंको एउटा छैन भने, तपाईं खाता साइन अप गर्न सक्नुहुन्छ र API कुञ्जी बनाउन सक्नुहुन्छ। एकपटक तपाईंले कुञ्जी प्राप्त गरेपछि, तपाईं यसलाई `.env` फाइलमा `OPENAI_API_KEY` भेरिएबलमा प्रयोग गर्न सक्नुहुन्छ।

### २.६ Hugging Face कन्फिगर गर्नुहोस्: प्रोफाइलबाट

तपाईंको Hugging Face टोकन तपाईंको प्रोफाइलमा [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) अन्तर्गत फेला पार्न सकिन्छ। यी सार्वजनिक रूपमा पोस्ट वा साझा नगर्नुहोस्। यसको सट्टा, यस परियोजना प्रयोगको लागि नयाँ टोकन बनाउनुहोस् र यसलाई `.env` फाइलमा `HUGGING_FACE_API_KEY` भेरिएबल अन्तर्गत प्रतिलिपि गर्नुहोस्। _नोट:_ यो प्राविधिक रूपमा API कुञ्जी होइन तर प्रमाणीकरणको लागि प्रयोग गरिन्छ त्यसैले हामी निरन्तरता कायम राख्नको लागि यो नामकरण परम्परा राख्दैछौं।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी सटीकताको लागि प्रयास गर्छौं, कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा असत्यताहरू हुन सक्छ। यसको मातृभाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्या लागि हामी जिम्मेवार हुनेछैनौं।