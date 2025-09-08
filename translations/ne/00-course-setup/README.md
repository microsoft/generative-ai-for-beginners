<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:53:11+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ne"
}
-->
# यो कोर्स सुरु गर्दै

हामी तपाईंलाई यो कोर्स सुरु गर्न पाउँदा निकै उत्साहित छौं र तपाईंले Generative AI सँग के के बनाउन प्रेरणा पाउनुहुन्छ भन्ने हेर्न चाहन्छौं!

तपाईंको सफलताको लागि, यो पृष्ठमा सेटअपका चरणहरू, प्राविधिक आवश्यकताहरू, र आवश्यक परेमा सहायता कहाँ पाउने भन्ने कुरा उल्लेख गरिएको छ।

## सेटअपका चरणहरू

यो कोर्स लिन सुरु गर्न, तपाईंले तलका चरणहरू पूरा गर्नुपर्नेछ।

### १. यो रिपो Fork गर्नुहोस्

[पूरै रिपो Fork गर्नुहोस्](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तपाईंको आफ्नै GitHub खातामा, जसले गर्दा तपाईंले कुनै पनि कोड परिवर्तन गर्न र चुनौतीहरू पूरा गर्न सक्नुहुन्छ। तपाईंले [यो रिपोमा स्टार (🌟) पनि दिन सक्नुहुन्छ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ताकि यसलाई र सम्बन्धित रिपोहरू सजिलै फेला पार्न सक्नुहोस्।

### २. Codespace बनाउनुहोस्

कोड चलाउँदा कुनै निर्भरता समस्या नआओस् भनेर, हामी यो कोर्स [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मा चलाउन सिफारिस गर्छौं।

तपाईंको fork मा: **Code -> Codespaces -> New on main**

![Codespace बनाउने बटनहरू देखाउने संवाद](../../../00-course-setup/images/who-will-pay.webp)

#### २.१ Secret थप्नुहोस्

१. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> नयाँ secret थप्नुहोस्।
२. नाम OPENAI_API_KEY राख्नुहोस्, तपाईंको key टाँस्नुहोस्, Save गर्नुहोस्।

### ३. अब के गर्ने?

| म चाहन्छु…           | जानुहोस्…                                                                 |
|---------------------|----------------------------------------------------------------------------|
| पाठ १ सुरु गर्न     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| अफलाइन काम गर्न     | [`setup-local.md`](02-setup-local.md)                                      |
| LLM Provider सेटअप गर्न | [`providers.md`](providers.md)                                         |
| अन्य सिक्नेहरूसँग भेट्न | [हाम्रो Discord मा सामेल हुनुहोस्](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## समस्या समाधान

| लक्षण                                    | समाधान                                                          |
|------------------------------------------|-----------------------------------------------------------------|
| कन्टेनर बनाउने प्रक्रिया १० मिनेटभन्दा बढी अड्कियो | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Terminal जडान भएन; **+** क्लिक गर्नुहोस् ➜ *bash*               |
| OpenAI बाट `401 Unauthorized`            | गलत / म्याद सकिएको `OPENAI_API_KEY`                            |
| VS Code मा “Dev container mounting…” देखियो | ब्राउजर ट्याब रिफ्रेश गर्नुहोस्—कहिलेकाहीं Codespaces जडान छुट्छ |
| Notebook kernel हरायो                    | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-आधारित प्रणालीहरू:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

३. **`.env` फाइल सम्पादन गर्नुहोस्**: `.env` फाइललाई कुनै पनि text editor (जस्तै VS Code, Notepad++, वा अन्य) मा खोल्नुहोस्। तलको लाइन थप्नुहोस्, जहाँ `your_github_token_here` लाई तपाईंको वास्तविक GitHub token ले बदल्नुहोस्:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

४. **फाइल Save गर्नुहोस्**: परिवर्तनहरू Save गर्नुहोस् र text editor बन्द गर्नुहोस्।

५. **`python-dotenv` इन्स्टल गर्नुहोस्**: यदि तपाईंले पहिले इन्स्टल गर्नुभएको छैन भने, तपाईंले `python-dotenv` प्याकेज इन्स्टल गर्नुपर्नेछ जसले `.env` फाइलबाट environment variables तपाईंको Python एप्लिकेसनमा लोड गर्छ। यसलाई `pip` प्रयोग गरेर इन्स्टल गर्न सक्नुहुन्छ:

   ```bash
   pip install python-dotenv
   ```

६. **Python स्क्रिप्टमा Environment Variables लोड गर्नुहोस्**: तपाईंको Python स्क्रिप्टमा, `python-dotenv` प्याकेज प्रयोग गरेर `.env` फाइलबाट environment variables लोड गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

यत्ति हो! तपाईंले सफलतापूर्वक `.env` फाइल बनाउनु भयो, तपाईंको GitHub token थप्नुभयो, र Python एप्लिकेसनमा लोड गर्नुभयो।

## तपाईंको कम्प्युटरमा स्थानीय रूपमा कसरी चलाउने

कोड तपाईंको कम्प्युटरमा स्थानीय रूपमा चलाउन, तपाईंले [Python को कुनै संस्करण](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) इन्स्टल गर्नुपर्नेछ।

त्यसपछि रिपोजिटरी प्रयोग गर्न, तपाईंले यसलाई clone गर्नुपर्नेछ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सबै कुरा checkout भएपछि, तपाईं सुरु गर्न सक्नुहुन्छ!

## वैकल्पिक चरणहरू

### Miniconda इन्स्टल गर्दै

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) भनेको [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केही प्याकेजहरू इन्स्टल गर्नका लागि हलुका इन्स्टलर हो।
Conda आफैंमा प्याकेज म्यानेजर हो, जसले विभिन्न Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सजिलै सेटअप र स्विच गर्न सजिलो बनाउँछ। साथै, `pip` बाट उपलब्ध नभएका प्याकेजहरू इन्स्टल गर्न पनि उपयोगी छ।

[MiniConda इन्स्टलेसन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) अनुसरण गरेर सेटअप गर्न सक्नुहुन्छ।

Miniconda इन्स्टल भएपछि, तपाईंले [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) clone गर्नुपर्नेछ (यदि पहिले गर्नुभएको छैन भने)।

अब, तपाईंले virtual environment बनाउनुपर्नेछ। Conda प्रयोग गरेर environment फाइल (_environment.yml_) बनाउनुहोस्। यदि तपाईं Codespaces प्रयोग गर्दै हुनुहुन्छ भने, यो `.devcontainer` डाइरेक्टरी भित्र बनाउनुहोस्, अर्थात् `.devcontainer/environment.yml`।

तलको स्निपेट प्रयोग गरेर environment फाइल तयार गर्नुहोस्:

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

यदि conda प्रयोग गर्दा समस्या आयो भने, तलको कमाण्ड प्रयोग गरेर Microsoft AI Libraries म्यानुअली इन्स्टल गर्न सक्नुहुन्छ।

```
conda install -c microsoft azure-ai-ml
```

Environment फाइलले आवश्यक dependencies जनाउँछ। `<environment-name>` भनेको तपाईंको Conda environment को नाम हो, र `<python-version>` भनेको तपाईंले प्रयोग गर्न चाहनुभएको Python को संस्करण हो, जस्तै `3` भनेको Python को पछिल्लो major version हो।

अब, तलका कमाण्डहरू कमाण्ड लाइन/टर्मिनलमा चलाएर Conda environment बनाउन सक्नुहुन्छ

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

यदि समस्या आयो भने [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

### Python support extension सहित Visual Studio Code प्रयोग गर्दै

हामी यो कोर्सका लागि [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor र [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इन्स्टल गर्न सिफारिस गर्छौं। तर, यो अनिवार्य होइन, केवल सिफारिस मात्र हो।

> **Note**: VS Code मा कोर्स रिपोजिटरी खोल्दा, तपाईंले प्रोजेक्टलाई कन्टेनर भित्र सेटअप गर्ने विकल्प पाउनुहुन्छ। यो [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डाइरेक्टरीका कारण हो। यसबारे पछि थप जानकारी हुनेछ।

> **Note**: Clone गरेर डायरेक्टरी VS Code मा खोल्दा, Python support extension इन्स्टल गर्न सुझाव आउनेछ।

> **Note**: यदि VS Code ले रिपोजिटरी कन्टेनरमा पुन: खोल्न सुझाव दियो भने, तपाईंले यो अस्वीकार गर्नुहोस् ताकि तपाईंले स्थानीय रूपमा इन्स्टल गरिएको Python प्रयोग गर्न सक्नुहोस्।

### ब्राउजरमा Jupyter प्रयोग गर्दै

तपाईं [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) प्रयोग गरेर पनि प्रोजेक्टमा काम गर्न सक्नुहुन्छ। Classic Jupyter र [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दुवैले auto-completion, code highlighting जस्ता सुविधासहित राम्रो विकास वातावरण दिन्छन्।

Jupyter स्थानीय रूपमा सुरु गर्न, टर्मिनल/कमाण्ड लाइनमा जानुहोस्, कोर्स डायरेक्टरीमा जानुहोस्, र निम्न कमाण्ड चलाउनुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter instance सुरु गर्छ र त्यसमा पहुँच गर्न URL कमाण्ड लाइनमा देखिन्छ।

URL खोल्दा, तपाईंले कोर्स outline देख्नुहुनेछ र कुनै पनि `*.ipynb` फाइलमा जान सक्नुहुन्छ। जस्तै, `08-building-search-applications/python/oai-solution.ipynb`।

### कन्टेनरमा चलाउँदै

तपाईंको कम्प्युटर वा Codespace मा सबै कुरा सेटअप नगरीकन, [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) प्रयोग गर्न सक्नुहुन्छ। कोर्स रिपोजिटरी भित्रको विशेष `.devcontainer` फोल्डरले VS Code लाई कन्टेनर भित्र प्रोजेक्ट सेटअप गर्न सम्भव बनाउँछ। Codespaces बाहिर, यसका लागि Docker इन्स्टल गर्नुपर्ने हुन्छ, र यो अलि जटिल हुन सक्छ, त्यसैले कन्टेनरमा काम गर्ने अनुभव भएकाहरूलाई मात्र सिफारिस गरिन्छ।

GitHub Codespaces प्रयोग गर्दा API key सुरक्षित राख्न Codespace Secrets प्रयोग गर्नु उत्तम हो। थप जान्नका लागि [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड हेर्नुहोस्।

## पाठहरू र प्राविधिक आवश्यकताहरू

यो कोर्समा ६ वटा अवधारणात्मक पाठहरू र ६ वटा कोडिङ पाठहरू छन्।

कोडिङ पाठहरूका लागि, हामी Azure OpenAI Service प्रयोग गर्दैछौं। तपाईंलाई Azure OpenAI सेवा र API key को पहुँच चाहिन्छ। तपाईं [यो आवेदन](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) भरेर पहुँचको लागि आवेदन दिन सक्नुहुन्छ।

जबसम्म तपाईंको आवेदन प्रक्रिया हुँदैछ, प्रत्येक कोडिङ पाठमा `README.md` फाइल पनि छ जहाँ तपाईंले कोड र नतिजा हेर्न सक्नुहुन्छ।

## Azure OpenAI Service पहिलो पटक प्रयोग गर्दा

यदि तपाईंले Azure OpenAI सेवा पहिलो पटक प्रयोग गर्दै हुनुहुन्छ भने, [Azure OpenAI Service resource कसरी बनाउने र डिप्लोय गर्ने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) गाइड अनुसरण गर्नुहोस्।

## OpenAI API पहिलो पटक प्रयोग गर्दा

यदि तपाईंले OpenAI API पहिलो पटक प्रयोग गर्दै हुनुहुन्छ भने, [Interface कसरी बनाउने र प्रयोग गर्ने](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) गाइड अनुसरण गर्नुहोस्।

## अन्य सिक्नेहरूसँग भेट्नुहोस्

हामीले हाम्रो आधिकारिक [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मा अन्य सिक्नेहरूसँग भेट्नका लागि च्यानलहरू बनाएका छौं। यो समान सोच भएका उद्यमी, निर्माता, विद्यार्थी, र Generative AI मा स्तरवृद्धि गर्न चाहने सबैका लागि नेटवर्किङको राम्रो माध्यम हो।

[![discord च्यानलमा सामेल हुनुहोस्](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टिम पनि यो Discord server मा तपाईंलाई सहायता गर्न उपस्थित हुनेछ।

## योगदान गर्नुहोस्

यो कोर्स खुला-स्रोत पहल हो। यदि तपाईंले सुधार गर्नुपर्ने वा समस्या देख्नुभयो भने, कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाउनुहोस् वा [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) दर्ता गर्नुहोस्।

प्रोजेक्ट टिमले सबै योगदान ट्र्याक गर्नेछ। खुला-स्रोतमा योगदान गर्नु Generative AI मा तपाईंको करियर बनाउनको लागि उत्कृष्ट उपाय हो।

धेरैजसो योगदानका लागि तपाईंले Contributor License Agreement (CLA) मा सहमति जनाउनुपर्नेछ, जसले तपाईंले योगदान गर्न अधिकार छ र हामीलाई प्रयोग गर्न अनुमति दिनुहुन्छ भन्ने घोषणा गर्छ। थप जानकारीका लागि [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

महत्वपूर्ण: यो रिपोमा पाठ्य सामग्री अनुवाद गर्दा, कृपया मेसिन अनुवाद प्रयोग नगर्नुहोस्। हामी अनुवादलाई समुदायमार्फत प्रमाणित गर्नेछौं, त्यसैले तपाईं दक्ष भाषा मात्र अनुवाद गर्न स्वयंसेवक बन्नुहोस्।

जब तपाईं pull request पठाउनुहुन्छ, CLA-bot ले स्वचालित रूपमा तपाईंले CLA दिनुपर्ने हो कि होइन भनेर निर्धारण गर्छ र PR मा लेबल, टिप्पणी आदि थप्छ। बोटले दिएको निर्देशन पालना गर्नुहोस्। तपाईंले यो सबै रिपोजिटरीमा एकपटक मात्र गर्नुपर्नेछ।

यो प्रोजेक्टले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) अपनाएको छ। थप जानकारीका लागि Code of Conduct FAQ पढ्नुहोस् वा [Email opencode](opencode@microsoft.com) मा थप प्रश्न वा टिप्पणी पठाउनुहोस्।

## सुरु गरौं
अब तपाईंले यो पाठ्यक्रम पूरा गर्न आवश्यक सबै चरणहरू पूरा गर्नुभएको छ, अब सुरु गरौं [Generative AI र LLMs को परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) बाट।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको मूल दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।