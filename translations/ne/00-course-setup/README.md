# यस कोर्ससँग सुरु गर्दै

हामी तपाईंलाई यो कोर्स सुरु गर्न र जेनेरेटिभ AI सँग के निर्माण गर्ने प्रेरणा मिल्छ हेर्नका लागि उत्साहित छौं!

तपाईंको सफलताको सुनिश्चित गर्नका लागि, यो पृष्ठले सेटअप कदमहरू, प्राविधिक आवश्यकताहरू, र आवश्यक परे सहयोग कहाँ प्राप्त गर्ने जानकारी दिन्छ।

## सेटअप कदमहरू

यो कोर्स लिन सुरु गर्न, तपाईंले तलका कदमहरू पूरा गर्न आवश्यक छ।

### १. यो रिपो फोर्क गर्नुहोस्

[पूरा रिपो फोर्क गर्नुहोस्](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तपाईंको आफ्नै GitHub खातामा जसले तपाईंलाई कुनै पनि कोड परिवर्तन गर्न र चुनौतीहरू पूरा गर्न सक्षम बनाउँछ। तपाईं [यो रिपोमा स्टार (🌟) पनि दिन सक्नुहुन्छ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) जसले यसलाई र सम्बन्धित रिपोलाई सजिलै फेला पार्न मद्दत गर्दछ।

### २. कोडस्पेस बनाउनुहोस्

कोड चलाउँदा कुनै निर्भरता सम्बन्धी समस्या नहोस् भनी, हामी यो कोर्सलाई [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मा चलाउन सिफारिस गर्छौं।

तपाईंको फोर्कमा: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ne/who-will-pay.4c0609b1c7780f44.webp)

#### २.१ एउटा गोप्य कुञ्जी थप्नुहोस्

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret।
2. नाम OPENAI_API_KEY राख्नुहोस्, आफ्नो कुञ्जी पेस्ट गरेर Save गर्नुहोस्।

### ३. के गर्ने?

| म के गर्न चाहन्छु…    | जानुहोस्…                                                             |
|-----------------------|-------------------------------------------------------------------------|
| पाठ १ सुरु गर्नुहोस् | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| अफलाइन काम गर्नुहोस्   | [`setup-local.md`](02-setup-local.md)                                   |
| LLM प्रदायक सेटअप गर्नुहोस् | [`providers.md`](03-providers.md)                                        |
| अन्य सिक्नेहरूलाई भेट्नुहोस् | [हाम्रो Discord मा सहभागी हुनुस्](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या समाधान


| समस्या                                    | समाधान                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| कन्टेनर निर्माण १० मिनेट भन्दा बढी रोकिएको | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | टर्मिनल जडित भएन; **+** क्लिक गरेर *bash* खोल्नुहोस्          |
| OpenAI बाट `401 Unauthorized`              | गलत वा समाप्त `OPENAI_API_KEY`                                    |
| VS Code मा “Dev container mounting…” देखिन्छ | ब्राउजर ट्याब रिफ्रेस गर्नुहोस्—Codespaces कहिलेकाहीँ कनेक्सन हराउँछ |
| नोटबुक कर्नेल हराएको छ                  | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   युनिक्स-आधारित प्रणालीहरू:

   ```bash
   touch .env
   ```

   विन्डोज:

   ```cmd
   echo . > .env
   ```

३. **`.env` फाइल सम्पादन गर्नुहोस्**: `.env` फाइललाई कुनै टेक्स्ट एडिटरमा (जस्तै VS Code, Notepad++, वा अरू कुनै एडिटर) खोल्नुहोस्। तलको लाइन थप्नुहोस्, जहाँ `your_github_token_here` लाई आफ्नो वास्तविक GitHub टोकनले प्रतिस्थापन गर्नुहोस्:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

४. **फाइल बचत गर्नुहोस्**: परिवर्तनहरूको बचत गरी टेक्स्ट एडिटर बन्द गर्नुहोस्।

५. **`python-dotenv` इन्स्टल गर्नुहोस्**: यदि तपाईंले यो पहिले गरेन भने, `python-dotenv` प्याकेज इन्स्टल गर्नु आवश्यक हुन्छ जसले `.env` फाइलबाट वातावरण चरहरू तपाईंको Python एप्लिकेशनमा लोड गर्छ। `pip` प्रयोग गरेर यसलाई इन्स्टल गर्न सकिन्छ:

   ```bash
   pip install python-dotenv
   ```

६. **तपाईंको Python स्क्रिप्टमा पर्यावरण चरहरू लोड गर्नुहोस्**: आफ्नो Python स्क्रिप्टमा `python-dotenv` प्याकेज प्रयोग गरेर `.env` फाइलबाट वातावरण चरहरू लोड गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाइलबाट वातावरण परिवर्तकहरू लोड गर्नुहोस्
   load_dotenv()

   # GITHUB_TOKEN परिवर्तक पहुँच गर्नुहोस्
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

त्यो हो! तपाईंले सफलतापूर्वक `.env` फाइल सिर्जना गर्नुभयो, आफ्नो GitHub टोकन थप्नुभयो, र यसलाई तपाईंको Python एप्लिकेशनमा लोड गर्नुभयो।

## कसरी कम्प्युटरमा लोकल रूपमा चलाउने

तपाईंको कम्प्युटरमा कोड लोकल रूपमा चलाउनको लागि, तपाईंलाई [Python को कुनै संस्करण इन्स्टल गर्नुपर्नेछ](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

त्यसपछि रिपो प्रयोग गर्न, यो क्लोन गर्न आवश्यक छ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सबै कुरा सेट भएपछि, तपाईं सुरु गर्न सक्नुहुन्छ!

## वैकल्पिक कदमहरू

### मिनिकोंडा इन्स्टल गर्नुहोस्

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हल्का वजनको इन्स्टलर हो जसले [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केहि प्याकेजहरू इन्स्टल गर्न मद्दत गर्छ।  
Conda आफैं एक प्याकेज म्यानेजर हो जसले विभिन्न Python [**भर्चुअल वातावरणहरू**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सेटअप गर्न र स्विच गर्न सजिलो बनाउँछ। यसले `pip` बाट उपलब्ध नभएका प्याकेजहरू इन्स्टल गर्न पनि मद्दत गर्छ।

तपाईं [MiniConda इन्स्टलेसन मार्गदर्शन](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) लाई अनुसरण गर्न सक्नुहुन्छ।

मिनिकोंडा इन्स्टल गरेपछि, तपाईंले [रिपोजिटरी क्लोन](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) गर्न आवश्यक छ (यदि पहिले गर्नुभएको छैन भने)।

पछी, तपाईंले वर्चुअल वातावरण बनाउन आवश्यक छ। Conda प्रयोग गरेर यसका लागि नयाँ वातावरण फाइल (_environment.yml_) बनाउनुहोस्। यदि तपाईं Codespaces मा काम गर्दै हुनुहुन्छ भने, यसलाई `.devcontainer` डिरेक्टरी भित्र बनाउनुहोस् जसले `.devcontainer/environment.yml` हुन्छ।

तलको स्निपेट प्रयोग गर्दै आफ्नो वातावरण फाइल पूरा गर्नुहोस्:

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

यदि तपाईंले Conda प्रयोग गर्दा समस्या आउँछ भने, तपाईं म्यानुअली Microsoft AI Libraries टर्मिनलमा तलको कमाण्ड प्रयोग गरी इन्स्टल गर्न सक्नुहुन्छ।

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइलले हामीलाई चाहिने निर्भरता उल्लेख गर्दछ। `<environment-name>` तपाईंले आफ्नो Conda वातावरणको लागि उपयोग गर्न चाहने नाम हो, र `<python-version>` तपाईं चाहनु भएको Python को संस्करण हो, उदाहरणका लागि `3` सबैभन्दा नयाँ मुख्य Python संस्करण हो।

त्यसपछि, तलको कमाण्डहरू टर्मिनलमा चलाएर आफ्नो Conda वातावरण सिर्जना गर्नुहोस्:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप पथ केवल Codespace सेटअपहरूमा लागू हुन्छ
conda activate ai4beg
```

यदि कुनै समस्या आएमा [Conda वातावरणहरू गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

### Visual Studio Code सँग Python समर्थन एक्स्टेन्सन प्रयोग गर्नुहोस्

हामी यो कोर्सका लागि [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) एडिटरलाई [Python समर्थन एक्स्टेन्सन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) सहित चलाउन सिफारिस गर्छौं। यो सिफारिस हो र अनिवार्य छैन।

> **टिप्पणी**: कोर्स रिपोजिटरी VS Code मा खोल्दा तपाईंलाई प्रोजेक्टलाई कन्टेनर भित्र सेटअप गर्ने विकल्प आउँछ। यसको कारण हो कोर्स रिपोजिटरी भित्र रहेको [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डिरेक्टरी। यसबारे पछि थप जानकारी दिइनेछ।

> **टिप्पणी**: जब तपाईंले रिपोजिटरी क्लोन गरेर VS Code मा खोल्नुहुन्छ, तेस्रो पक्षले तपाईंलाई Python समर्थन एक्स्टेन्सन इन्स्टल गर्न सुझाव दिन्छ।

> **टिप्पणी**: VS Code ले तपाईंलाई रिपोजिटरीलाई कन्टेनरमा पुनः खोल्न सुझाव दिएमा, स्थानिय रूपमा इन्स्टल गरिएको Python संस्करण प्रयोग गर्न यस अनुरोध अस्वीकृत गर्नुहोस्।

### ब्राउजरमा Jupyter प्रयोग गर्नुहोस्

तपाईं https://jupyter.org?WT.mc_id=academic-105485-koreyst भित्र यो परियोजनामा ब्राउजरमा नै Jupyter वातावरण प्रयोग गरेर काम गर्न सक्नुहुन्छ। दुई क्लासिक Jupyter र [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) स्वत: पूर्ति, कोड हाइलाइटिंग जस्ता सुविधाहरू सहित सुखद विकास वातावरण प्रदान गर्छन्।

लोकल Jupyter सुरु गर्नको लागि, टर्मिनल/कमाण्ड लाइनमा गएर, कोर्स डिरेक्टरीमा गएर यस कमाण्ड चलाउनुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter इन्टेन्स सुरु गर्नेछ र पहुँचको URL कमाण्ड लाइन विन्डोमा देखाइनेछ।

URL पहुँच गरेपछि, तपाईंले कोर्सको संरचना देख्नुहुनेछ र कुनै पनि `*.ipynb` फाइलमा नेभिगेट गर्न सक्नुहुन्छ। उदाहरणका लागि, `08-building-search-applications/python/oai-solution.ipynb`।

### कन्टेनरमा चलाउने

तपाईंको कम्प्युटर वा Codespace मा सबै कुरा सेटअप गर्ने विकल्पको विकल्पका रूपमा, तपाईं [कन्टेनर](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) प्रयोग गर्न सक्नुहुन्छ। कोर्स रिपोजिटरी भित्रको विशेष `.devcontainer` फोल्डरले VS Code लाई प्रोजेक्ट कन्टेनर भित्र सेटअप गर्न सक्षम बनाउँछ। Codespaces बाहिर, यो Docker इन्स्टल गर्न आवश्यक पर्छ, र केही काम लाग्छ, त्यसैले हामी यसलाई कन्टेनरसँग काम गर्ने अनुभव भएका मानिसहरूलाई मात्र सिफारिस गर्छौं।

GitHub Codespaces प्रयोग गर्दा API कुञ्जीहरू सुरक्षित राख्ने उत्तम तरिकाहरू मध्ये एक Codespace Secrets को प्रयोग हो। कृपया यसबारे थप जान्नको लागि [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) मार्गदर्शन पालना गर्नुहोस्।

## पाठहरू र प्राविधिक आवश्यकताहरू

कोर्समा ६ वटा अवधारणा पाठ र ६ वटा कोडिंग पाठहरू छन्।

कोडिंग पाठहरूका लागि, हामी Azure OpenAI सेवा प्रयोग गर्दैछौं। तपाईंलाई Azure OpenAI सेवामा पहुँच र API कुञ्जी आवश्यक पर्छ यो कोड चलाउनका लागि। पहुँच प्राप्त गर्न [यो आवेदन पूरा गर्नुहोस्](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)।

आवेदन प्रक्रिया हुँदा, प्रत्येक कोडिंग पाठसँग एक `README.md` फाइल पनि हुन्छ जहाँ तपाईंले कोड र आउटपुट देख्न सक्नुहुन्छ।

## Azure OpenAI सेवा पहिलोपटक प्रयोग गर्दा

यदि तपाईं पहिलो पटक Azure OpenAI सेवा प्रयोग गर्दै हुनुहुन्छ भने, कृपया यो मार्गदर्शन पालना गर्नुहोस् जुन [Azure OpenAI सेवा स्रोत कसरी सिर्जना र परिनियोजन गर्ने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) सम्बन्धी छ।

## OpenAI API पहिलोपटक प्रयोग गर्दा

यदि यो तपाईंको OpenAI API पहिलो पटक प्रयोग हो भने, कृपया [इन्टरफेस कसरी सिर्जना र प्रयोग गर्ने](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) गाइड पालना गर्नुहोस्।

## अन्य सिक्नेहरूसँग भेट्नुहोस्

हामीले आधिकारिक [AI Community Discord सर्भर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मा अरू सिक्नेहरूसँग भेटघाटका लागि च्यानलहरू बनाएका छौं। यो समान सोच र उद्यमी, बिल्डर, विद्यार्थीहरू, र जेनेरेटिभ AI सिक्न चाहने सबैका लागि नेटवर्किङको राम्रो माध्यम हो।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टोली पनि यस Discord सर्भरमा अन्य सिक्नेहरूलाई सहयोग गर्न हुनेछ।

## योगदान गर्नुहोस्

यो कोर्स खुला स्रोत पहल हो। यदि तपाईंले सुधार वा समस्याहरू देख्नु भयो भने, कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) सिर्जना गर्नुहोस् वा [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लग गर्नुहोस्।

परियोजना टोलीले सबै योगदानहरू ट्र्याक गर्नेछ। खुला स्रोतमा योगदान गर्नु भनेको जेनेरेटिभ AI मा तपाईंको करियर बनाउन अद्भुत उपाय हो।

धेरै योगदानहरूमा तपाईंले एक Contributor License Agreement (CLA) स्वीकार गर्नुपर्छ जसले तपाईंले योगदान गर्न अधिकार राख्नु भएको र साँच्चिकै हामीलाई प्रयोग गर्ने अधिकार दिनुभएको घोषणा गर्छ। विवरणको लागि हेर्नुहोस् [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

महत्त्वपूर्ण: यस रिपोमा अनुवाद गर्दा कृपया मेशिन अनुवाद नप्रयोग गर्नुहोस्। हामी समुदाय मार्फत अनुवादहरू जाँच गर्नेछौं, त्यसैले तपाईं सक्षम भएका भाषाहरूमा मात्र अनुवादका लागि स्वयंसेवा गर्नुहोस्।

जब तपाईं पुल अनुरोध पठाउनुहुन्छ, एक CLA-बटले स्वतः निर्धारण गर्नेछ तपाईंलाई CLA आवश्यक छ कि छैन र PR लाई उपयुक्त लेबल वा टिप्पणी गर्नेछ। बटले दिएको निर्देशनहरू पालना गर्नुहोस्। यो कार्य तपाईंले सबै रिपोजिटरीमा एक पटक मात्र गर्नुपर्छ।

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) अपनाएको छ। थप जानकारीका लागि Code of Conduct FAQ पढ्नुहोस् वा थप प्रश्न वा टिप्पणीका लागि [Email opencode](opencode@microsoft.com) सँग सम्पर्क गर्नुहोस्।

## सुरु गरौं!
अब तपाईँले यो कोर्स पूरा गर्न आवश्यक कदमहरू पूरा गर्नुभएको छ, आउनुहोस् सुरु गरौं [Generative AI र LLMs को परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त गरेर।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गरिरहेका छौं, तर कृपया जानकार हुनुहोस् कि स्वतः अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा मान्य स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यो अनुवाद प्रयोग गर्दा उत्पन्न हुने कुनै पनि गलतफहमी वा व्याख्यागत त्रुटिहरूको लागि हामी जिम्मेवार हुनेछौं भनी मानिन्न।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->