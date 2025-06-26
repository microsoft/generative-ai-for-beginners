<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:41:49+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hi"
}
-->
# इस पाठ्यक्रम की शुरुआत करें

हम इस पाठ्यक्रम को शुरू करने के लिए आपके उत्साह से बहुत खुश हैं और देखना चाहते हैं कि आप जनरेटिव एआई के साथ क्या बनाने के लिए प्रेरित होते हैं!

आपकी सफलता सुनिश्चित करने के लिए, यह पृष्ठ सेटअप चरणों, तकनीकी आवश्यकताओं, और आवश्यकता पड़ने पर मदद कहां प्राप्त करें, इसके बारे में जानकारी देता है।

## सेटअप चरण

इस पाठ्यक्रम को शुरू करने के लिए, आपको निम्नलिखित चरणों को पूरा करना होगा।

### 1. इस रिपॉजिटरी को फोर्क करें

[इस पूरी रिपॉजिटरी को फोर्क करें](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) अपने खुद के GitHub खाते में ताकि आप किसी भी कोड को बदल सकें और चुनौतियों को पूरा कर सकें। आप इस रिपॉजिटरी को [स्टार (🌟) भी कर सकते हैं](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ताकि इसे और संबंधित रिपॉजिटरी को ढूंढना आसान हो जाए।

### 2. एक कोडस्पेस बनाएं

कोड चलाते समय किसी भी निर्भरता समस्या से बचने के लिए, हम इस पाठ्यक्रम को [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) में चलाने की सलाह देते हैं।

यह आपके फोर्क किए गए रिपॉजिटरी के `Code` विकल्प को चुनकर और **Codespaces** विकल्प का चयन करके बनाया जा सकता है।

![कोडस्पेस बनाने के लिए बटन दिखाने वाला संवाद](../../../00-course-setup/images/who-will-pay.webp)

### 3. अपने एपीआई कुंजियों को सुरक्षित रखें

किसी भी प्रकार के एप्लिकेशन का निर्माण करते समय अपनी एपीआई कुंजियों को सुरक्षित और सुरक्षित रखना महत्वपूर्ण है। हम सलाह देते हैं कि किसी भी एपीआई कुंजी को सीधे अपने कोड में संग्रहीत न करें। उन विवरणों को सार्वजनिक रिपॉजिटरी में प्रतिबद्ध करने से सुरक्षा समस्याएं हो सकती हैं और यदि कोई बुरा अभिनेता उनका उपयोग करता है तो अवांछित लागत भी हो सकती है। यहाँ एक चरण-दर-चरण मार्गदर्शिका है कि कैसे एक `.env` फ़ाइल Python के लिए बनाएं और `GITHUB_TOKEN` जोड़ें:

1. **अपने प्रोजेक्ट डायरेक्टरी पर नेविगेट करें**: अपनी टर्मिनल या कमांड प्रॉम्प्ट खोलें और अपने प्रोजेक्ट की रूट डायरेक्टरी पर नेविगेट करें जहां आप `.env` फ़ाइल बनाना चाहते हैं।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फ़ाइल बनाएं**: अपने पसंदीदा टेक्स्ट एडिटर का उपयोग करके `.env` नामक एक नई फ़ाइल बनाएं। यदि आप कमांड लाइन का उपयोग कर रहे हैं, तो आप `touch` (on Unix-based systems) or `echo` (विंडोज़ पर) का उपयोग कर सकते हैं:

   यूनिक्स-आधारित सिस्टम:
   ```bash
   touch .env
   ```

   विंडोज़:
   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल संपादित करें**: `.env` फ़ाइल को एक टेक्स्ट एडिटर (जैसे, VS Code, Notepad++, या कोई अन्य एडिटर) में खोलें। फ़ाइल में निम्न पंक्ति जोड़ें, `your_github_token_here` को अपने वास्तविक GitHub टोकन से बदलें:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फ़ाइल सहेजें**: परिवर्तनों को सहेजें और टेक्स्ट एडिटर को बंद करें।

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` पैकेज इंस्टॉल करें ताकि `.env` फ़ाइल से आपके Python एप्लिकेशन में पर्यावरणीय वेरिएबल्स लोड हो सकें। आप इसे `pip` का उपयोग करके इंस्टॉल कर सकते हैं:

   ```bash
   pip install python-dotenv
   ```

6. **अपने Python स्क्रिप्ट में पर्यावरणीय वेरिएबल्स लोड करें**: अपने Python स्क्रिप्ट में, `python-dotenv` पैकेज का उपयोग करके `.env` फ़ाइल से पर्यावरणीय वेरिएबल्स लोड करें:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस इतना ही! आपने सफलतापूर्वक एक `.env` फ़ाइल बनाई, अपने GitHub टोकन जोड़ा, और इसे अपने Python एप्लिकेशन में लोड किया।

## अपने कंप्यूटर पर स्थानीय रूप से कैसे चलाएं

अपने कंप्यूटर पर कोड को स्थानीय रूप से चलाने के लिए, आपके पास कुछ संस्करण का [Python इंस्टॉल होना चाहिए](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

इसके बाद रिपॉजिटरी का उपयोग करने के लिए, आपको इसे क्लोन करना होगा:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एक बार जब आपके पास सब कुछ चेक आउट हो जाए, तो आप शुरू कर सकते हैं!

## वैकल्पिक चरण

### मिनिकोंडा इंस्टॉल करना

[मिनिकोंडा](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, और कुछ पैकेज इंस्टॉल करने के लिए एक हल्का इंस्टॉलर है। Conda स्वयं एक पैकेज मैनेजर है, जो विभिन्न Python [**वर्चुअल पर्यावरणों**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेजों के बीच सेटअप और स्विच करना आसान बनाता है। यह उन पैकेजों को इंस्टॉल करने में भी सहायक होता है जो `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` के माध्यम से उपलब्ध नहीं हैं।

अपने पर्यावरण फ़ाइल को नीचे दिए गए स्निपेट से भरें:

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

यदि आपको कोंडा का उपयोग करते समय त्रुटियां मिल रही हैं, तो आप निम्नलिखित कमांड का उपयोग करके Microsoft AI लाइब्रेरीज़ को मैन्युअली इंस्टॉल कर सकते हैं।

```
conda install -c microsoft azure-ai-ml
```

पर्यावरण फ़ाइल उन निर्भरताओं को निर्दिष्ट करती है जिनकी हमें आवश्यकता है। `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python का नवीनतम प्रमुख संस्करण है।

इसके साथ ही, आप अपने कोंडा पर्यावरण को अपने कमांड लाइन/टर्मिनल में नीचे दिए गए कमांड चलाकर बना सकते हैं

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

यदि आपको कोई समस्या होती है, तो [कोंडा पर्यावरण गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) का संदर्भ लें।

### Python समर्थन एक्सटेंशन के साथ Visual Studio Code का उपयोग करना

हम इस पाठ्यक्रम के लिए [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) संपादक का उपयोग करने की सिफारिश करते हैं जिसमें [Python समर्थन एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इंस्टॉल है। हालांकि यह अधिक एक सिफारिश है और कोई निश्चित आवश्यकता नहीं है।

> **नोट**: VS Code में कोर्स रिपॉजिटरी खोलने पर, आपके पास प्रोजेक्ट को एक कंटेनर के भीतर सेटअप करने का विकल्प होता है। ऐसा इसलिए है क्योंकि कोर्स रिपॉजिटरी में [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डायरेक्टरी पाई जाती है। इस पर बाद में अधिक।

> **नोट**: एक बार जब आप VS Code में डायरेक्टरी को क्लोन और खोलते हैं, तो यह आपको स्वचालित रूप से Python समर्थन एक्सटेंशन इंस्टॉल करने का सुझाव देगा।

> **नोट**: यदि VS Code आपको रिपॉजिटरी को कंटेनर में फिर से खोलने का सुझाव देता है, तो इस अनुरोध को अस्वीकार करें ताकि आप Python के स्थानीय रूप से इंस्टॉल किए गए संस्करण का उपयोग कर सकें।

### ब्राउज़र में Jupyter का उपयोग करना

आप [Jupyter पर्यावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) का उपयोग करके भी प्रोजेक्ट पर काम कर सकते हैं, सीधे अपने ब्राउज़र में। क्लासिक Jupyter और [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोनों एक सुखद विकास पर्यावरण प्रदान करते हैं जिसमें ऑटो-कम्प्लीशन, कोड हाइलाइटिंग आदि जैसी विशेषताएं होती हैं।

Jupyter को स्थानीय रूप से शुरू करने के लिए, टर्मिनल/कमांड लाइन पर जाएं, कोर्स डायरेक्टरी पर नेविगेट करें, और निष्पादित करें:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

यह एक Jupyter इंस्टेंस शुरू करेगा और इसे एक्सेस करने के लिए URL कमांड लाइन विंडो में दिखाया जाएगा।

एक बार जब आप URL तक पहुंच जाते हैं, तो आपको कोर्स का आउटलाइन दिखेगा और आप किसी भी `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` फ़ाइल पर नेविगेट कर सकते हैं जहां आप कोड और आउटपुट देख सकते हैं।

## पहली बार Azure OpenAI सेवा का उपयोग करना

यदि यह पहली बार है जब आप Azure OpenAI सेवा के साथ काम कर रहे हैं, तो कृपया इस गाइड का पालन करें कि कैसे [Azure OpenAI सेवा संसाधन बनाएं और तैनात करें।](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## पहली बार OpenAI API का उपयोग करना

यदि यह पहली बार है जब आप OpenAI API के साथ काम कर रहे हैं, तो कृपया गाइड का पालन करें कि कैसे [इंटरफेस बनाएं और उपयोग करें।](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## अन्य शिक्षार्थियों से मिलें

हमने अन्य शिक्षार्थियों से मिलने के लिए हमारे आधिकारिक [AI Community Discord सर्वर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) में चैनल बनाए हैं। यह समान विचारधारा वाले उद्यमियों, निर्माताओं, छात्रों और जनरेटिव एआई में आगे बढ़ने की कोशिश कर रहे किसी भी व्यक्ति के साथ नेटवर्क बनाने का एक शानदार तरीका है।

[![डिस्कॉर्ड चैनल में शामिल हों](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टीम भी इस Discord सर्वर पर शिक्षार्थियों की मदद के लिए मौजूद होगी।

## योगदान दें

यह पाठ्यक्रम एक ओपन-सोर्स पहल है। यदि आप सुधार के क्षेत्र या समस्याएं देखते हैं, तो कृपया एक [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाएं या एक [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लॉग करें।

परियोजना टीम सभी योगदानों को ट्रैक करेगी। ओपन-सोर्स में योगदान देना जनरेटिव एआई में अपने करियर को बनाने का एक अद्भुत तरीका है।

अधिकांश योगदानों के लिए आपको एक योगदानकर्ता लाइसेंस अनुबंध (CLA) से सहमत होना आवश्यक है, जिसमें यह घोषणा करना होता है कि आपके पास अपने योगदान का उपयोग करने के लिए हमें अधिकार देने का अधिकार है। विवरण के लिए [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) पर जाएं।

महत्वपूर्ण: जब इस रिपॉजिटरी में पाठ का अनुवाद करते हैं, तो कृपया सुनिश्चित करें कि आप मशीन अनुवाद का उपयोग नहीं करते हैं। हम अनुवादों की सत्यता समुदाय के माध्यम से सुनिश्चित करेंगे, इसलिए कृपया केवल उन्हीं भाषाओं में अनुवाद के लिए स्वयंसेवा करें जिनमें आप प्रवीण हैं।

जब आप एक पुल अनुरोध सबमिट करते हैं, तो एक CLA-बॉट स्वचालित रूप से निर्धारित करेगा कि क्या आपको CLA प्रदान करने की आवश्यकता है और PR को उपयुक्त रूप से सजाएगा (जैसे, लेबल, टिप्पणी)। बस बॉट द्वारा प्रदान किए गए निर्देशों का पालन करें। आपको यह हमारे सभी रिपॉजिटरीज़ में केवल एक बार करना होगा।

इस परियोजना ने [Microsoft ओपन-सोर्स आचार संहिता](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) को अपनाया है। अधिक जानकारी के लिए आचार संहिता FAQ पढ़ें या किसी भी अतिरिक्त प्रश्न या टिप्पणियों के साथ [Email opencode](opencode@microsoft.com) से संपर्क करें।

## चलिए शुरू करते हैं

अब जब आपने इस पाठ्यक्रम को पूरा करने के लिए आवश्यक कदम पूरे कर लिए हैं, तो चलिए [जनरेटिव एआई और LLMs का परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त करके शुरू करते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।