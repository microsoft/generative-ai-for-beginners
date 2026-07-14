# यस कोर्ससँग सुरूवात गर्दै

हामी तपाईंलाई यो कोर्स सुरु गर्न र जेनरेटिभ एआईको साथ के निर्माण गर्ने प्रेरणा पाउनुहुनेछ भन्ने कुरामा अत्यन्त उत्साहित छौं!

तपाईंको सफलताको सुनिश्चितताका लागि, यो पृष्ठले सेटअप चरणहरू, प्राविधिक आवश्यकताहरू, र आवश्यक परेको खण्डमा सहयोग कहाँ पाउने बारे जानकारी दिन्छ।

## सेटअप चरणहरू

यस कोर्स लिन सुरु गर्न निम्न चरणहरू पूरा गर्न आवश्यक पर्छ।

### 1. यो रिपो फोर्क गर्नुहोस्

[यो सम्पूर्ण रिपो फोर्क गर्नुहोस्](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तपाईंको आफ्नै GitHub खातामा जसले तपाईंलाई कुनै पनि कोड परिवर्तन गर्न र चुनौतीहरू पूरा गर्न सक्षम बनाउँछ। तपाईं यस रिपोलाई र सम्बन्धित रिपोलाई सजिलै फेला पार्न [स्टार (🌟) दिन पनि सक्नुहुन्छ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)।

### 2. कोडस्पेस सिर्जना गर्नुहोस्

कोड चलाउँदा निर्भरता समस्याबाट जोगिन, हामी सिफारिस गर्छौं यो कोर्सलाई [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मा चलाउन।

तपाईंको फोर्कमा: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ne/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 गोप्य जानकारी थप्नुहोस्

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> नयाँ गोप्य जानकारी थप्नुहोस्।
2. नाम खुला OPENAI_API_KEY, तपाईंको कुञ्जी पेस्ट गर्नुहोस्, Save गर्नुहोस्।

### 3. के गर्ने?

| म चाहन्छु…          | जानुहोस्…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| पाठ १ सुरु गर्ने      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| अफलाइन काम गर्ने     | [`setup-local.md`](02-setup-local.md)                                   |
| LLM प्रदायक सेटअप गर्ने | [`providers.md`](03-providers.md)                                        |
| अन्य सिक्नेहरूसँग भेट्ने | [हाम्रो डिस्कोर्डमा सामेल हुनुहोस्](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या समाधान


| लक्षण                                   | सुधार                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| कन्टेनर बिल्ड १० मिनेट भन्दा बढी रोकियो    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | टर्मिनल जडान भएन; **+** मा क्लिक गर्नुहोस् ➜ *bash*                    |
| OpenAI बाट `401 Unauthorized`            | गलत / समाप्त भयो `OPENAI_API_KEY`                                |
| VS Code मा “Dev container mounting…” देखिन्छ | ब्राउजर ट्याब रिफ्रेस गर्नुहोस्—Codespaces कहिलेकाहीं जडान हराउँछ   |
| नोटबुक कर्नेल हरायो                      | नोटबुक मेनु ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   युनिक्‍स आधारित प्रणालीहरू:

   ```bash
   touch .env
   ```

   विन्डोज:

   ```cmd
   echo . > .env
   ```

३. **`.env` फाइल सम्पादन गर्नुहोस्**: `.env` फाइल कुनैपनि टेक्स्ट सम्पादक (जस्तै, VS Code, Notepad++, वा अन्य कुनै पनि सम्पादक) मा खोल्नुहोस्। तल उल्लेखित लाइनहरू फाइलमा थप्नुहोस्, तपाईंको Microsoft Foundry Models अन्त बिन्दु र कुञ्जी राखेर (कसरी प्राप्त गर्ने जान्न [`providers.md`](03-providers.md) हेर्नुहोस्):

   > **सूचना:** GitHub मोडेलहरू (र यसको `GITHUB_TOKEN` भेरिएबल) जुलाई २०२६ को अन्त्यमा अवसान हुँदैछन्। यसको सट्टा [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) प्रयोग गर्नुहोस्।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

४. **फाइल सुरक्षित गर्नुहोस्**: परिवर्तनहरू सुरक्षित गरेर टेक्स्ट सम्पादक बन्द गर्नुहोस्।

५. **`python-dotenv` इन्स्टल गर्नुहोस्**: यदि तपाईंले अझै इन्स्टल गर्नुभएको छैन भने, तपाईंको Python उपयोगितामा `.env` फाइल बाट वातावरण भेरिएबलहरू लोड गर्न `python-dotenv` प्याकेज इन्स्टल गर्नु आवश्यक छ। `pip` प्रयोग गरेर इन्स्टल गर्न सक्नुहुन्छ:

   ```bash
   pip install python-dotenv
   ```

६. **तपाईंको Python स्क्रिप्टमा वातावरण भेरिएबलहरू लोड गर्नुहोस्**: तपाईंको Python स्क्रिप्टमा, `python-dotenv` प्याकेजलाई `.env` फाइल बाट वातावरण भेरिएबलहरू लोड गर्न प्रयोग गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाइलबाट वातावरण भेरिएबलहरू लोड गर्नुहोस्
   load_dotenv()

   # Microsoft Foundry Models भेरिएबलहरू पहुँच गर्नुहोस्
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

त्यति हो! तपाईंले सफलतापूर्वक `.env` फाइल सिर्जना गर्नुभयो, आफ्नो Microsoft Foundry Models प्रमाण-पत्रहरू थप्नुभयो, र तिनीहरूलाई तपाईंको Python अनुप्रयोगमा लोड गर्नुभयो।

## आफ्नो कम्प्युटरमा स्थानीय रूपमा सञ्चालन गर्ने तरिका

आफ्नो कम्प्युटरमा कोड स्थानीय रूपमा चलाउन, तपाईंले कुनै संस्करणको [Python इन्स्टल गर्नुपर्ने हुन्छ](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

त्यसपछि, रिपोजिटोरीलाई क्लोन गर्न आवश्यक हुन्छ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सबै कुरा तयार भएपछि, तपाईं सुरु गर्न सक्नुहुन्छ!

## वैकल्पिक चरणहरू

### मिनिकन्डा इन्स्टल गर्नुहोस्

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केही प्याकेजहरू इन्स्टल गर्नको लागि हल्का बनाउन इन्स्टलर हो।
Conda आफैंमा एउटा प्याकेज व्यवस्थापक हो, जसले विभिन्न Python [**भर्चुअल वातावरणहरू**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सेटअप गर्ने र स्विच गर्न सजिलो बनाउँछ। यसले `pip` मार्फत उपलब्ध नभएका प्याकेजहरू इन्स्टल गर्न पनि मद्दत गर्छ।

तपाईंले [MiniConda इन्स्टलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) अनुसरण गर्न सक्नुहुन्छ सेटअप गर्न।

Miniconda इन्स्टल गरेपछि, यदि तपाईंले अझै नभएको खण्डमा रिपोजिटोरी [क्लोन](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) गर्नुहोस्।

त्यसपछि, भर्चुअल वातावरण सिर्जना गर्न आवश्यक पर्छ। Conda प्रयोग गरेर यो गर्न, नयाँ वातावरण फाइल (_environment.yml_) सिर्जना गर्नुहोस्। यदि तपाईं Codespaces प्रयोग गर्दै हुनुहुन्छ भने, `.devcontainer` निर्देशिकामा यो सिर्जना गर्नुहोस्, अर्थात् `.devcontainer/environment.yml`।

आफ्नो वातावरण फाइल तल दिइएको टुक्राले भरि दिनुहोस्:

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

यदि तपाईंलाई conda प्रयोग गर्दा त्रुटि आउँछ भने, तपाईं Microsoft AI लाइब्रेरीहरूलाई टर्मिनलमा तलको आदेशमार्फत म्यानुअली इन्स्टल गर्न सक्नुहुन्छ।

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइलले हामीलाई आवश्यक निर्भरता निर्दिष्ट गर्छ। `<environment-name>` तपाईंले आफ्नो Conda वातावरणको लागि प्रयोग गर्न खोजेको नाम हो, र `<python-version>` तपाईंले चाहेको Python संस्करण हो, उदाहरणका लागि `3` सब भन्दा नयाँ प्रमुख संस्करण हो।

यो भएपछि, तपाईंले तलका आदेशहरू आफ्नो कमाण्ड लाइन/टर्मिनलमा चलाएर Conda वातावरण सिर्जना गर्न सक्नुहुन्छ।

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप-पथ केवल Codespace सेटअपहरूमा लागू हुन्छ
conda activate ai4beg
```

यदि कुनै समस्या आएमा, [Conda वातावरण मार्गदर्शक](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

### Visual Studio Code लाई Python सपोर्ट एक्सटेन्सनसहित प्रयोग गर्ने तरिका

हामी सिफारिस गर्छौं यो कोर्सका लागि [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) सम्पादकलाई [Python सपोर्ट एक्सटेन्सन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) का साथ प्रयोग गर्न। यद्यपि यो सिफारिस मात्र हो, अनिवार्य होइन।

> **सूचना**: कोर्स रिपोजिटोरी VS Code मा खोल्दा, तपाईंले परियोजनालाई कन्टेनर भित्र सेट अप गर्ने विकल्प पाउनुहुन्छ। यसको कारण कोर्स रिपोजिटोरी भित्र रहेको [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) निर्देशिका हो। यो पछि थप चर्चा गरिनेछ।

> **सूचना**: रिपोजिटोरी क्लोन र VS Code मा खोल्नासाथ, यो स्वतः तपाईंलाई Python सपोर्ट एक्सटेन्सन इन्स्टल गर्न सुझाव दिनेछ।

> **सूचना**: यदि VS Code ले रिपोजिटोरी पुन: कन्टेनरमा खोल्न सुझाव दियो भने, स्थानीय रूपमा इन्स्टल गरेको Python प्रयोग गर्न यो अनुरोध अस्विकार गर्नुहोस्।

### ब्राउजरमा Jupyter प्रयोग गर्ने तरिका

तपाईंले परियोजनामा काम गर्न [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) पनि ब्राउजरबाटै प्रयोग गर्न सक्नुहुन्छ। दुवै क्लासिक Jupyter र [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) स्वयंपूर्णता, कोड हाइलाइटिङजस्ता सुविधासहित निकै सुखद विकास वातावरण प्रदान गर्छ।

Jupyter स्थानीय रूपमा सुरु गर्न, टर्मिनल/कमाण्ड लाइनमा जानुहोस्, कोर्स निर्देशिकामा नेभिगेट गर्नुहोस्, र निम्न आदेश कार्यान्वयन गर्नुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter सत्र सुरु गर्नेछ र पहुँच गर्न URL कमाण्ड लाइन विन्डोमा देखाउनेछ।

URL पहुँच गरेपछि, तपाईंले कोर्सको रूपरेखा देख्नुहुनेछ र कुनै पनि `*.ipynb` फाइलमा जा सक्नुहुन्छ। उदाहरणका लागि, `08-building-search-applications/python/oai-solution.ipynb`।

### कन्टेनरमा सञ्चालन

तपाईंको कम्प्युटर वा Codespace मा सबै सेटअप गर्ने विकल्पको सट्टा, [कन्टेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) प्रयोग गर्न सक्नुहुन्छ। कोर्स रिपोजिटोरी भित्रको विशेष `.devcontainer` फोल्डरले VS Code लाई परियोजनालाई कन्टेनर भित्र सेटअप गर्न अनुमति दिन्छ। Codespaces बाहिर, यसका लागि Docker इन्स्टल गर्नुपर्ने हुन्छ, र साँचो कुरा भन्नुपर्दा, यसमा केही काम लाग्छ, त्यसैले हामी यसलाई कन्टेनरसँग काम गर्ने अनुभव भएका व्यक्तिलाई मात्र सिफारिस गर्छौं।

GitHub Codespaces प्रयोग गर्दा तपाईंका API कुञ्जीहरू सुरक्षित राख्न सर्वश्रेष्ठ तरिकाहरू मध्ये एउटाले Codespace Secrets प्रयोग गर्नु हो। यो सम्बन्धमा थप जान्न कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड अनुसरण गर्नुहोस्।


## पाठहरू र प्राविधिक आवश्यकताहरू

कोर्समा ६ अवधारणा पाठहरू र ६ कोडिङ पाठहरू छन्।

कोडिङ पाठहरूका लागि, हामी Azure OpenAI सेवा प्रयोग गर्दैछौं। तपाईंले Azure OpenAI सेवा पहुँच गर्न र यो कोड चलाउन API कुञ्जी आवश्यक पर्छ। तपाईं [यो आवेदन पुरा गरेर](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) पहुँचको लागि आवेदन दिन सक्नुहुन्छ।

आवेदन प्रक्रिया सुरू हुनु अगाडि, प्रत्येक कोडिङ पाठसँग `README.md` फाइल पनि हुन्छ जहाँ तपाईं कोड र परिणामहरू हेर्न सक्नुहुन्छ।

## पहिलो पटक Azure OpenAI सेवा प्रयोग गर्दा

यदि तपाईं पहिलो पटक Azure OpenAI सेवा प्रयोग गर्दै हुनुहुन्छ भने, कृपया यस गाइडलाई अनुसरण गर्नुहोस् [Azure OpenAI सेवा स्रोत सिर्जना र डिप्लोमेन्ट गर्ने तरिका](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)।

## पहिलो पटक OpenAI API प्रयोग गर्दा

यदि तपाईं पहिलो पटक OpenAI API प्रयोग गर्दै हुनुहुन्छ भने, कृपया यो गाइड अनुसरण गर्नुहोस् कसरी [इन्टरफेस सिर्जना र प्रयोग गर्ने।](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## अन्य सिक्नेहरूसँग भेट्नुहोस्

हामीले हाम्रो आधिकारिक [AI समुदाय डिस्कोर्ड सर्भर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मा अन्य सिक्नेहरूसँग भेट्न च्यानलहरू सिर्जना गरेका छौं। यो जेनरेटिभ एआईमा स्तर बढाउन चाहने समान सोच भएका उद्यमी, निर्माताहरू, विद्यार्थीहरू र अरू सबैका लागि एक उत्कृष्ट नेटवर्किङ अवसर हो।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टोली यस डिस्कोर्ड सर्भरमा पनि सिक्नेहरूलाई सहयोग गर्न हुनेछ।

## योगदान गर्नुहोस्

यो कोर्स एउटा खुला स्रोत पहल हो। तपाईंले सुधारका क्षेत्रहरू वा समस्याहरू देख्नुभयो भने, कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) सिर्जना गर्नुहोस् वा [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लग गर्नुहोस्।

परियोजना टोलीले सबै योगदानहरू ट्र्याक गर्नेछ। खुला स्रोतमा योगदान गर्नु तपाईंको जेनरेटिभ एआई क्यारियर बनाउन एक आश्चर्यजनक तरीका हो।

धेरै योगदानहरूले तपाईंलाई Contributor License Agreement (CLA) मा सहमत हुन आवश्यक पर्दछ जसले प्रमाणित गर्दछ कि तपाईंको योगदान प्रयोग गर्ने अधिकार तपाईंलाई छ। थप जानकारीका लागि [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

महत्वपूर्ण: यस रिपोमा अनुवाद गर्दा कृपया मेसिन अनुवाद प्रयोग नगर्नुहोला। हामी अनुवादहरू समुदायमार्फ़त जाँच गर्नेछौं, त्यसैले कृपया जुन भाषामा तपाईं दक्ष हुनुहुन्छ मात्र अनुवादका लागि स्वयंसेवक हुनुहोस्।

जब तपाईंले पुल अनुरोध पेश गर्नुहुन्छ, CLA-bot स्वतः निर्णय गर्नेछ कि तपाईंलाई CLA आवश्यक छ कि छैन र PR उपयुक्त रूपमा चिन्ह लगाउनेछ (जस्तै लेबल, टिप्पणी)। कृपया बोटले दिएको निर्देशहरू पालना गर्नुहोस्। तपाईंले यो एकपटक मात्र सबै रिपोजिटोरीमा गर्ने हुनुहुन्छ।


यस प्रोजेक्टले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) अपनाएको छ। थप जानकारीको लागि Code of Conduct FAQ पढ्नुहोस् वा कुनै अतिरिक्त प्रश्न वा टिप्पणीका लागि [Email opencode](opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## सुरु गरौं

अब जब तपाईंले यस कोर्स पूरा गर्न आवश्यक चरणहरू पूरा गर्नुभएको छ, आउनुहोस् [Generative AI र LLMs मा परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) बाट सुरू गरौं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->