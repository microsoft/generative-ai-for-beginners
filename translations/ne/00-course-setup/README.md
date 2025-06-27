<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:43:54+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ne"
}
-->
# यस पाठ्यक्रमको साथ सुरु गर्दै

हामी तपाईंलाई यो पाठ्यक्रम सुरु गर्न र जेनेरेटिभ एआईसँग के निर्माण गर्न प्रेरित हुनुहुन्छ भनेर हेर्न पाउँदा धेरै उत्साहित छौं!

तपाईंको सफलता सुनिश्चित गर्न, यो पृष्ठले सेटअप चरणहरू, प्राविधिक आवश्यकताहरू, र आवश्यक पर्दा कहाँ सहयोग प्राप्त गर्ने भनेर विवरण दिन्छ।

## सेटअप चरणहरू

यो पाठ्यक्रम लिन सुरु गर्न, तपाईंले निम्न चरणहरू पूरा गर्न आवश्यक छ।

### १. यस रिपो फोर्क गर्नुहोस्

कुनै पनि कोड परिवर्तन गर्न र चुनौतीहरू पूरा गर्न आफ्नो GitHub खातामा [यस सम्पूर्ण रिपो फोर्क गर्नुहोस्](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)। तपाईं यसलाई र सम्बन्धित रिपोहरू सजिलै भेट्न [स्टार (🌟) गर्न पनि सक्नुहुन्छ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)।

### २. कोडस्पेस सिर्जना गर्नुहोस्

कोड चलाउँदा कुनै निर्भरता समस्याहरूबाट बच्न, हामी यो पाठ्यक्रम [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मा चलाउन सिफारिस गर्छौं।

यो तपाईंको फोर्क गरिएको संस्करणमा `Code` विकल्प चयन गरेर र **Codespaces** विकल्प चयन गरेर सिर्जना गर्न सकिन्छ।

![कोडस्पेस सिर्जना गर्न बटनहरू देखाउने संवाद](../../../00-course-setup/images/who-will-pay.webp)

### ३. तपाईंको API कुञ्जीहरू भण्डारण गर्नुहोस्

कुनै पनि प्रकारको अनुप्रयोग निर्माण गर्दा तपाईंको API कुञ्जीहरू सुरक्षित र सुरक्षित राख्नु महत्त्वपूर्ण छ। हामी तपाईंको कोडमा कुनै पनि API कुञ्जीहरू सिधै भण्डारण नगर्न सिफारिस गर्छौं। ती विवरणहरू सार्वजनिक रिपोजिटरीमा प्रतिबद्ध गर्दा सुरक्षा समस्याहरू र यदि नराम्रो कार्यकर्ताले प्रयोग गरेमा अनावश्यक लागतहरू पनि हुन सक्छ।
यहाँ कसरी Python को लागि `.env` फाइल सिर्जना गर्ने र `GITHUB_TOKEN` थप्ने चरण-दर-चरण मार्गदर्शन छ:

1. **तपाईंको परियोजना निर्देशिकामा नेभिगेट गर्नुहोस्**: तपाईंको टर्मिनल वा कमाण्ड प्रॉम्प्ट खोल्नुहोस् र तपाईंको परियोजनाको मूल निर्देशिकामा नेभिगेट गर्नुहोस् जहाँ तपाईं `.env` फाइल सिर्जना गर्न चाहनुहुन्छ।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाइल सिर्जना गर्नुहोस्**: तपाईंको मनपर्ने पाठ सम्पादक प्रयोग गरेर `.env` नामको नयाँ फाइल सिर्जना गर्नुहोस्। यदि तपाईं कमाण्ड लाइन प्रयोग गर्दै हुनुहुन्छ भने, तपाईं `touch` (on Unix-based systems) or `echo` (विन्डोजमा) प्रयोग गर्न सक्नुहुन्छ:

   Unix-आधारित प्रणालीहरू:
   ```bash
   touch .env
   ```

   विन्डोज:
   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल सम्पादन गर्नुहोस्**: पाठ सम्पादक (जस्तै, VS कोड, Notepad++, वा कुनै अन्य सम्पादक) मा `.env` फाइल खोल्नुहोस्। फाइलमा निम्न लाइन थप्नुहोस्, `your_github_token_here` लाई तपाईंको वास्तविक GitHub टोकनले प्रतिस्थापन गर्दै:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल सुरक्षित गर्नुहोस्**: परिवर्तनहरू सुरक्षित गर्नुहोस् र पाठ सम्पादक बन्द गर्नुहोस्।

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` प्याकेज स्थापना गर्नुहोस् जसले तपाईंको Python अनुप्रयोगमा `.env` फाइलबाट वातावरणीय भेरिएबलहरू लोड गर्न अनुमति दिन्छ। तपाईं यसलाई `pip` प्रयोग गरेर स्थापना गर्न सक्नुहुन्छ:

   ```bash
   pip install python-dotenv
   ```

6. **तपाईंको Python स्क्रिप्टमा वातावरणीय भेरिएबलहरू लोड गर्नुहोस्**: तपाईंको Python स्क्रिप्टमा, `.env` फाइलबाट वातावरणीय भेरिएबलहरू लोड गर्न `python-dotenv` प्याकेज प्रयोग गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

त्यसै हो! तपाईंले सफलतापूर्वक `.env` फाइल सिर्जना गर्नुभयो, तपाईंको GitHub टोकन थप्नुभयो, र यसलाई तपाईंको Python अनुप्रयोगमा लोड गर्नुभयो।

## तपाईंको कम्प्युटरमा स्थानीय रूपमा कसरी चलाउने

तपाईंको कम्प्युटरमा स्थानीय रूपमा कोड चलाउन, तपाईंलाई [Python को कुनै संस्करण स्थापना गरिएको](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) हुनु आवश्यक छ।

त्यसपछि रिपोजिटरी प्रयोग गर्न, तपाईंले यसलाई क्लोन गर्नु पर्छ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सबै कुरा जाँच गरेपछि, तपाईं सुरु गर्न सक्नुहुन्छ!

## वैकल्पिक चरणहरू

### मिनिकन्डा स्थापना गर्दै

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, साथै केही प्याकेजहरू स्थापना गर्नको लागि एक हल्का तौलको इन्स्टलर हो।
Conda आफैंमा एक प्याकेज प्रबन्धक हो, जसले विभिन्न Python [**भर्चुअल वातावरणहरू**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सेटअप गर्न र स्विच गर्न सजिलो बनाउँछ। यसले `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` मार्फत उपलब्ध नभएका प्याकेजहरू स्थापना गर्न पनि सजिलो बनाउँछ।

तलको स्निपेटसँग आफ्नो वातावरण फाइल भर्नुहोस्:

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

यदि तपाईंले conda प्रयोग गर्दा त्रुटिहरू पाउनुभयो भने तपाईंले निम्न आदेश प्रयोग गरेर टर्मिनलमा Microsoft AI Libraries म्यानुअली स्थापना गर्न सक्नुहुन्छ।

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइलले हामीलाई आवश्यक निर्भरताहरू निर्दिष्ट गर्दछ। `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python को नवीनतम प्रमुख संस्करण हो।

त्यो भएपछि, तपाईं आफ्नो कमाण्ड लाइन/टर्मिनलमा तलका आदेशहरू चलाएर आफ्नो Conda वातावरण सिर्जना गर्न सक्नुहुन्छ

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

कुनै समस्या आएमा [Conda वातावरणहरू मार्गदर्शन](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

### Python समर्थन विस्तारको साथ Visual Studio Code प्रयोग गर्दै

हामी [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) सम्पादकलाई [Python समर्थन विस्तार](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) संग स्थापना गरिएको सिफारिस गर्छौं। यो, तथापि, सिफारिस मात्र हो र कुनै निश्चित आवश्यकता होइन।

> **नोट**: VS Code मा पाठ्यक्रम रिपोजिटरी खोल्दा, तपाईंको लागि परियोजना कन्टेनर भित्र सेट अप गर्न विकल्प छ। यो [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) निर्देशिकाको कारण हो जुन पाठ्यक्रम रिपोजिटरी भित्र फेला परेको छ। यसबारे पछि थप।

> **नोट**: एकपटक तपाईंले VS Code मा निर्देशिका क्लोन र खोल्नुभयो भने, यसले स्वचालित रूपमा तपाईंलाई Python समर्थन विस्तार स्थापना गर्न सुझाव दिनेछ।

> **नोट**: यदि VS Code ले तपाईंलाई रिपोजिटरीलाई कन्टेनरमा पुनः खोल्न सुझाव दिन्छ भने, स्थानीय रूपमा स्थापना गरिएको Python को संस्करण प्रयोग गर्न यस अनुरोधलाई अस्वीकार गर्नुहोस्।

### ब्राउजरमा Jupyter प्रयोग गर्दै

तपाईंले [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) को प्रयोग गरेर पनि परियोजनामा काम गर्न सक्नुहुन्छ। दुवै क्लासिक Jupyter र [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ले स्वतः-सम्पूर्णता, कोड हाइलाइटिङ, आदि जस्ता सुविधाहरू सहित एक रमाइलो विकास वातावरण प्रदान गर्दछ।

Jupyter स्थानीय रूपमा सुरु गर्न, टर्मिनल/कमाण्ड लाइनमा जानुहोस्, पाठ्यक्रम निर्देशिकामा नेभिगेट गर्नुहोस्, र निम्न आदेश कार्यान्वयन गर्नुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter इन्स्टेन्स सुरु गर्नेछ र यसलाई पहुँच गर्न URL कमाण्ड लाइन विन्डोमा देखाइनेछ।

एकपटक तपाईंले URL पहुँच गर्नुभयो भने, तपाईंले पाठ्यक्रमको रूपरेखा देख्नुहुनेछ र कुनै पनि `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` फाइलमा जान सक्नुहुन्छ जहाँ तपाईंले कोड र आउटपुटहरू हेर्न सक्नुहुन्छ।

## पहिलो पटक Azure OpenAI सेवा प्रयोग गर्दै

यदि यो Azure OpenAI सेवासँग तपाईंको पहिलो पटक हो भने, [Azure OpenAI सेवा स्रोत सिर्जना र परिनियोजन कसरी गर्ने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) बारेमा यस मार्गदर्शनलाई अनुसरण गर्नुहोस्।

## पहिलो पटक OpenAI API प्रयोग गर्दै

यदि यो OpenAI API सँग तपाईंको पहिलो पटक हो भने, [इन्टरफेस सिर्जना र प्रयोग कसरी गर्ने](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) बारेमा मार्गदर्शनलाई अनुसरण गर्नुहोस्।

## अन्य शिक्षार्थीहरूलाई भेट्नुहोस्

हामीले हाम्रो आधिकारिक [AI समुदाय Discord सर्भर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मा अन्य शिक्षार्थीहरूलाई भेट्नका लागि च्यानलहरू सिर्जना गरेका छौं। यो समान विचारधाराका उद्यमीहरू, निर्माताहरू, विद्यार्थीहरू, र जेनेरेटिभ एआईमा स्तरवृद्धि गर्न खोजिरहेका व्यक्तिहरूसँग नेटवर्किङ गर्ने एक उत्कृष्ट तरिका हो।

[![Discord च्यानलमा सामेल हुनुहोस्](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टोलीले पनि कुनै पनि शिक्षार्थीहरूलाई मद्दत गर्न यस Discord सर्भरमा हुनेछ।

## योगदान गर्नुहोस्

यो पाठ्यक्रम एक खुला-स्रोत पहल हो। यदि तपाईंले सुधारका क्षेत्रहरू वा समस्याहरू देख्नुभयो भने, कृपया [पुल अनुरोध](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) सिर्जना गर्नुहोस् वा [GitHub समस्या](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लग गर्नुहोस्।

परियोजना टोलीले सबै योगदानहरू ट्र्याक गर्नेछ। खुला स्रोतमा योगदान गर्नु जेनेरेटिभ एआईमा तपाईंको करियर निर्माण गर्ने एक अद्भुत तरिका हो।

धेरैजसो योगदानहरूले तपाईंलाई एक योगदानकर्ता लाइसेन्स सम्झौता (CLA) मा सहमत हुन आवश्यक छ जसले तपाईंलाई यो अधिकार छ र वास्तवमा हामीलाई तपाईंको योगदान प्रयोग गर्ने अधिकार दिन्छ। विवरणहरूको लागि, [CLA, योगदानकर्ता लाइसेन्स सम्झौता वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) मा जानुहोस्।

महत्त्वपूर्ण: यस रिपोमा पाठ अनुवाद गर्दा, कृपया मेसिन अनुवाद प्रयोग नगर्नुहोस् सुनिश्चित गर्नुहोस्। हामी समुदाय मार्फत अनुवादहरू प्रमाणित गर्नेछौं, त्यसैले कृपया मात्र तपाईंले दक्षता हासिल गरेका भाषाहरूमा अनुवादको लागि स्वयंसेवक गर्नुहोस्।

जब तपाईं एक पुल अनुरोध पेश गर्नुहुन्छ, एक CLA-बोटले स्वचालित रूपमा निर्धारण गर्नेछ कि तपाईंले CLA प्रदान गर्न आवश्यक छ कि छैन र PR लाई उपयुक्त रूपमा सजाउनुहोस् (जस्तै, लेबल, टिप्पणी)। बोटले प्रदान गरेका निर्देशनहरू मात्र पालना गर्नुहोस्। तपाईंले हाम्रो CLA प्रयोग गर्ने सबै रिपोजिटरीहरूमा मात्र एकपटक यो गर्नु आवश्यक छ।

यस परियोजनाले [Microsoft खुला स्रोत आचार संहिता](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) अपनाएको छ। थप जानकारीको लागि आचार संहिताको FAQ पढ्नुहोस् वा कुनै थप प्रश्न वा टिप्पणीहरूका लागि [इमेल ओपनकोड](opencode@microsoft.com) मा सम्पर्क गर्नुहोस्।

## सुरु गरौं

अब तपाईंले यो पाठ्यक्रम पूरा गर्न आवश्यक चरणहरू पूरा गर्नुभएको छ, [जेनेरेटिभ एआई र LLMs को परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त गरेर सुरु गरौं।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।