# यो कोर्ससँग सुरूवात गर्दै

हामी तपाईंलाई यो कोर्स सुरु गर्ने र जनरेटिभ AI सँग के बनाउन प्रेरित हुनुहुन्छ भनेर देख्न धेरै उत्साहित छौं!

तपाईंको सफलताको सुनिश्चितताको लागि, यस पृष्ठले सेटअप चरणहरू, प्राविधिक आवश्यकताहरू, र आवश्यक परेमा सहयोग कहाँ पाउने भनेर व्याख्या गर्दछ।

## सेटअप चरणहरू

यो कोर्स लिन सुरु गर्न, तपाईंले निम्न चरणहरू पूरा गर्नुपर्नेछ।

### १. यो रिपो फोर्क गर्नुहोस्

[यहाँ सम्पूर्ण रिपो फोर्क गर्नुहोस्](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) आफ्नो GitHub खातामा जसले तपाईंलाई कुनै पनि कोड परिवर्तन गर्न र चुनौतीहरू पूरा गर्न सकिनेछ। तपाईंले [यो रिपोमा स्टार (🌟) पनि दिन सक्नुहुन्छ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) जसले यसलाई र सम्बन्धित रिपोहरूलाई सजिलै खोज्न मद्दत पुर्‍याउँछ।

### २. कोडस्पेस सिर्जना गर्नुहोस्

कोड चलाउँदा कुनै निर्भरता समस्या नहोस् भनेर, हामी यो कोर्सलाई [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मा चलाउन सिफारिस गर्छौं।

तपाइँको फोर्कमा: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ne/who-will-pay.4c0609b1c7780f44.webp)

#### २.१ गोप्य जानकारी थप्नुहोस्

१. ⚙️ गियर आइकन -> कमाण्ड प्यालेट -> Codespaces : Manage user secret -> नयाँ गोप्य जानकारी थप्नुहोस्।
२. नाम OPENAI_API_KEY राख्नुहोस्, तपाईंको कुञ्जी पेस्ट गर्नुहोस्, सुरक्षित गर्नुहोस्।

### ३. के गर्ने?

| म के गर्न चाहन्छु…    | जानुहोस्…                                                               |
|---------------------|-------------------------------------------------------------------------|
| पाठ १ सुरु गर्ने    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| अफलाइन काम गर्ने    | [`setup-local.md`](02-setup-local.md)                                   |
| LLM प्रदायक सेटअप गर्ने | [`providers.md`](03-providers.md)                                        |
| अन्य सिक्नेहरूसँग भेट   | [हाम्रो Discord मा सहभागी हुनुहोस्](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या समाधान


| लक्षण                                   | समाधान                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| कन्टेनर बिल्ड १० मिनेट भन्दा बढी रोकिएको | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | टर्मिनल जडान भएन; **+** क्लिक गरी *bash* छनौट गर्नुहोस्            |
| OpenAI बाट `401 Unauthorized`            | गलत / समय समाप्त भएको `OPENAI_API_KEY` हो                           |
| VS Code ले “Dev container mounting…” देखाउँछ | ब्राउजर ट्याब रिफ्रेस गर्नुहोस् — Codespaces कहिलेकाहीं जडान हराउँछ |
| नोटबुक कर्नेल हराएको छ                   | नोटबुक मेन्यु ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   यूनिक्स-आधारित प्रणालीहरू:

   ```bash
   touch .env
   ```

   विन्डोज:

   ```cmd
   echo . > .env
   ```

३. **`.env` फाइल सम्पादन गर्नुहोस्**: `.env` फाइललाई कुनै पाठ सम्पादकमा (जस्तै VS Code, Notepad++, वा अन्य कुनै पनि) खोल्नुहोस्। तल दिइएका पंक्तिहरू थप्नुहोस्, जहाँ प्लेसहोल्डरहरू तपाईंको वास्तविक Microsoft Foundry Models को अन्त्यबिन्दु र कुञ्जीले प्रतिस्थापन गर्नुहोस् (कसरी पाउने थाहा पाउन [`providers.md`](03-providers.md) हेर्नुहोस्):

   > **सूचना:** GitHub Models (र यसको `GITHUB_TOKEN` भेरिएबल) जुलाई २०२६ को अन्त्यमा बन्द हुँदैछ। यसको सट्टा [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) प्रयोग गर्नुहोस्।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

४. **फाइल सुरक्षित गर्नुहोस्**: परिवर्तनहरू सुरक्षित गरी पाठ सम्पादक बन्द गर्नुहोस्।

५. **`python-dotenv` इन्स्टल गर्नुहोस्**: यदि पहिले गर्नुभएको छैन भने, तपाईंले `python-dotenv` प्याकेज इन्स्टल गर्नुपर्नेछ जुन `.env` फाइलबाट वातावरण चरहरू Python एप्लिकेशनमा लोड गर्न प्रयोग हुन्छ। यसलाई `pip` मार्फत इन्स्टल गर्न सकिन्छ:

   ```bash
   pip install python-dotenv
   ```

६. **Python स्क्रिप्टमा वातावरण चरहरू लोड गर्नुहोस्**: आफ्नो Python स्क्रिप्टमा `python-dotenv` प्याकेज प्रयोग गरी `.env` फाइलबाट वातावरण चरहरू लोड गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाइलबाट वातावरण चरहरू लोड गर्नुहोस्
   load_dotenv()

   # Microsoft Foundry मोडेल चरहरू पहुँच गर्नुहोस्
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

यति नै हो! तपाईंले सफलतापूर्वक `.env` फाइल बनाउनु भयो, Microsoft Foundry Models प्रमाणपत्र थप्नुभयो, र तिनीहरूलाई Python एप्लिकेशनमा लोड गर्नुभयो।

## आफ्नो कम्प्युटरमा स्थानीय रूपमा कसरी चलाउने

कोड आफ्नो कम्प्युटरमा स्थानीय स्तरमा चलाउन, तपाईंलाई [Python को कुनै संस्करण स्थापना](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) गरिएको हुन आवश्यक छ।

त्यसपछि रिपोजिटोरी प्रयोग गर्न, तपाईंले त्यसलाई क्लोन गर्नुपर्छ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सबै कुरा चेकआउट भएपछि, तपाईं सुरु गर्न सक्नुहुन्छ!

## वैकल्पिक चरणहरू

### Miniconda इन्स्टल गर्दै

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हल्का वजनको इन्स्टलर हो जसले [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केही प्याकेजहरू इन्स्टल गर्न मद्दत गर्छ।
Conda आफैं एक प्याकेज प्रबन्धक हो, जुन विभिन्न Python [**भर्चुअल वातावरणहरू**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सेटअप र स्विच गर्न सजिलो बनाउँछ। यो `pip` मार्फत उपलब्ध नभएका प्याकेजहरू इन्स्टल गर्न पनि उपयोगी हुन्छ।

तपाईंले यसको लागि [MiniConda इन्स्टलेसन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) पालना गर्न सक्नुहुन्छ।

Miniconda इन्स्टल भएपछि, तपाईंले रिपोजिटोरी क्लोन गर्नुपर्छ (यदि पहिले नगरेका हुनुहुन्छ भने)

त्यसपछि, तपाईंले भर्चुअल वातावरण बनाउनुपर्छ। Conda प्रयोग गरेर, नयाँ वातावरण फाइल (_environment.yml_) सिर्जना गर्नुहोस्। Codespaces मा काम गर्दै हुनुहुन्छ भने, `.devcontainer` डाइरेक्टरी भित्र यो फाइल बनाउनुस्, जस्तै `.devcontainer/environment.yml`।

तपाइँको वातावरण फाइल यस प्रकार भरिदिनुहोस्:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

यदि तपाईंलाई conda प्रयोग गर्दा त्रुटिहरू आयो भने, तपाईं टर्मिनलमा तलको कमाण्ड चलाएर Microsoft AI Libraries म्यानुअली इन्स्टल गर्न सक्नुहुन्छ।

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइलले हामीलाई चाहिने निर्भरतालाई निर्दिष्ट गर्छ। `<environment-name>` तपाईंले Conda वातावरणको नाम राख्ने स्थान हो, र `<python-version>` तपाईंले चाहनुभएको Python को संस्करण हो, उदाहरणका लागि `3` Python को सबैभन्दा नयाँ मुख्य संस्करण हो।

यसपछि, तपाइँ आफ्नो Conda वातावरण निम्न आदेशहरूले चलाएर बनाउन सक्नुहुन्छ:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer सब पथ केवल Codespace सेटअपहरूमा लागू हुन्छन्
conda activate ai4beg
```

कुनै समस्या आएमा [Conda वातावरणहरू गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

### Visual Studio Code मा Python समर्थन विस्तार प्रयोग गर्दै

हामी यो कोर्सको लागि [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) सम्पादकलाई [Python समर्थन विस्तार](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) सहित प्रयोग गर्न सिफारिस गर्छौं। यो, तथापि, थप सुझाव हो, अनिवार्य होइन।

> **सूचना**: कोर्स रिपोजिटोरी VS Code मा खोल्दा, तपाईंले परियोजना कन्टेनर भित्र सेटअप गर्ने विकल्प पाउनुहुन्छ। यो कोर्स रिपोजिटोरीको भित्र रहेका [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डाइरेक्टरीको कारण हो। यो बारे पछि थप जानकारी।

> **सूचना**: रिपोजिटोरी क्लोन गरी VS Code मा खोल्दा, यसले तपाईंलाई Python समर्थन विस्तार इन्स्टल गर्न स्वतः सुझाव दिन्छ।

> **सूचना**: यदि VS Code ले तपाईलाई रिपोजिटोरी कन्टेनर भित्र पुनः खोल्न सुझाव दिन्छ भने, यो अनुरोध अस्वीकार गर्नुहोस् ताकि तपाईंले लोकल इन्स्टल गरिएको Python संस्करण प्रयोग गर्न सक्नुहोस्।

### ब्राउजरमा Jupyter प्रयोग गर्दै

तपाईंले यस परियोजनामा [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) सिधै ब्राउजरमा प्रयोग गर्न सक्नुहुन्छ। क्लासिक Jupyter र [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दुवैले स्वचालित पुरा गर्ने, कोड हाइलाइटिङ जस्ता सुविधाहरू सहित रमाइलो विकास वातावरण प्रदान गर्छन्।

Jupyter स्थानीय रूपमा सुरु गर्न, टर्मिनल/कमाण्ड लाइनमा जानुहोस्, कोर्स डाइरेक्टरीमा नेभिगेट गर्नुहोस्, र निम्न कमाण्ड चलाउनुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter सर्भर सुरु गर्नेछ र पहुँचको लागि URL कमाण्ड लाइन विन्डोमा देखाइनेछ।

URL पहुँच गरेपछि, तपाईंले कोर्स आउटलाइन् देख्नसक्नुहुन्छ र कुनै पनि `*.ipynb` फाइलमा जान सक्नुहुन्छ। उदाहरणका लागि, `08-building-search-applications/python/oai-solution.ipynb`।

### कन्टेनरमा चलाउँदै

आफ्नो कम्प्युटर वा Codespace मा सबै सेटअप नगर्ने विकल्पको रूपमा [कन्टेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) प्रयोग गर्न सकिन्छ। कोर्स रिपोमा रहेका `.devcontainer` फोल्डरले VS Code लाई परियोजना कन्टेनर भित्र सेटअप गर्न सक्षम बनाउँछ। Codespaces बाहेक, यसका लागि Docker इन्स्टल गर्नुपर्नेछ, जसले केही काम माग्छ; यसैले हामी यो केवल कन्टेनर सम्बन्धी अनुभव भएका व्यक्तिलाई सिफारिस गर्छौं।

GitHub Codespaces प्रयोग गर्दा तपाईंको API कुञ्जीहरू सुरक्षित राख्न उत्तम तरिका Codespace Secrets प्रयोग गर्नु हो। यसबारे थप जान्न कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड पालना गर्नुहोस्।


## पाठहरू र प्राविधिक आवश्यकताहरू

कोर्समा "शिक्षा" पाठहरू हुन्छन् जुन जनरेटिभ AI अवधारणाहरू व्याख्या गर्छन् र "निर्माण" पाठहरू छन् जसमा **Python** र **TypeScript** दुवैले सम्भव भएमा प्रत्यक्ष कोड उदाहरणहरू दिइन्छ।

कोडिङका लागि, हामी Microsoft Foundry मा Azure OpenAI प्रयोग गर्छौं। तपाईंलाई Azure सदस्यता र API कुञ्जी चाहिन्छ। पहुँच खुला छ - कुनै आवेदन आवश्यक छैन - त्यसैले तपाईं [Microsoft Foundry स्रोत सिर्जना गरी मोडेल डिप्लोय गर्न सक्नुहुन्छ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) र आफ्नो अन्त्यबिन्दु र कुञ्जी प्राप्त गर्न सक्नुहुन्छ।

प्रत्येक कोडिंग पाठसँग `README.md` फाइल पनि हुन्छ जहाँ तपाईं कुनै पनि कोड चलाउनु नपरी कोड र परिणाम हेर्न सक्नुहुन्छ।

## Azure OpenAI सेवा पहिलो पटक प्रयोग गर्ने

यदि तपाईं Azure OpenAI सेवा पहिलो पटक प्रयोग गर्दै हुनुहुन्छ भने, कृपया यो गाइड पालन गर्नुहोस्: [Azure OpenAI सेवा स्रोत कसरी सिर्जना र डिप्लोय गर्ने।](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API पहिलो पटक प्रयोग गर्ने

यदि तपाईं OpenAI API पहिलो पटक प्रयोग गर्दै हुनुहुन्छ भने, त्यसका लागि [ईन्टरफेस कसरी सिर्जना र प्रयोग गर्ने](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) गाइड पालना गर्नुहोस्।

## अन्य सिक्नेहरूसँग भेट

हामीले आधिकारिक [AI Community Discord सर्भर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मा अन्य सिक्नेहरूसँग भेट गर्न च्यानलहरू बनाएका छौं। यो अन्य सँगसँगै सोच्ने उद्यमी, निर्माताहरू, विद्यार्थीहरू, र जनरेटिभ AI मा स्तर बढाउन चाहनेहरूका लागि उत्कृष्ट नेटवर्किङ माध्यम हो।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टोली पनि यो Discord सर्भरमा हुनेछ जसले कुनै पनि सिक्नेहरूलाई सहयोग गर्नेछ।

## योगदान गर्नुहोस्

यो कोर्स एक खुला स्रोत पहल हो। सुधार वा समस्या देखेमा कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाउनुहोस् वा [GitHub मुद्दा](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लगाउनुहोस्।

परियोजना टोली सबै योगदानहरू ट्र्याक गर्नेछ। खुला स्रोत योगदान जनरेटिभ AI मा तपाईंको क्यारियर बनाउने एक अद्भुत तरिका हो।

धेरै योगदानहरूले तपाईंले योगदान प्रयोग गर्ने अधिकार हामीलाई दिदै हुनुहुन्छ भन्ने घोषित गर्ने Contributor License Agreement (CLA) मा सहमति चाहिन्छ। विस्तृत जानकारीका लागि [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

महत्वपूण: यस रिपोमा पाठ अनुवाद गर्दा कृपया मेसिन अनुवाद प्रयोग नगर्नुहोस्। हामी समुदायमार्फत अनुवादहरूको जाँच गर्नेछौं, त्यसैले केवल तपाईं दक्ष भाषाहरूमा अनुवादमा स्वयंसेवा गर्नुहोस्।


जब तपाईं पुल अनुरोध पेश गर्नुहुन्छ, CLA-बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंलाई CLA प्रदान गर्न आवश्यक छ वा छैन र PR लाई उपयुक्त रूपमा सजाउनेछ (जस्तै, लेबल, टिप्पणी)। कृपया बोटले प्रदान गरेको निर्देशहरू पालना गर्नुहोस्। तपाईंले हाम्रो CLA प्रयोग गर्ने सबै रेपोजिटोरीहरूमा यो एक पटक मात्र गर्नु पर्नेछ।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) अपनाएको छ। थप जानकारीका लागि Code of Conduct FAQ पढ्नुहोस् वा थप प्रश्नहरू वा टिप्पणीहरूका लागि [Email opencode](opencode@microsoft.com) सम्पर्क गर्नुहोस्।

## सुरु गरौं

अब जब तपाईंले यो कोर्स पूरा गर्न आवश्यक चरणहरू पूरा गर्नुभयो, आउनुहोस् [जनरेटिभ AI र LLMs को परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) पाउँदा सुरु गरौं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->