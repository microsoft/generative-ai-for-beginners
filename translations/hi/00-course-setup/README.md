# इस कोर्स के साथ शुरुआत

हम बहुत उत्साहित हैं कि आप इस कोर्स को शुरू करें और देखें कि आप जनरेटिव AI के साथ क्या बनाना चाहते हैं!

आपकी सफलता सुनिश्चित करने के लिए, इस पृष्ठ में सेटअप स्टेप्स, तकनीकी आवश्यकताएं, और मदद कहाँ प्राप्त करें इसकी जानकारी दी गई है।

## सेटअप स्टेप्स

इस कोर्स को शुरू करने के लिए, आपको निम्नलिखित स्टेप्स को पूरा करना होगा।

### 1. इस रिपो को फोर्क करें

[पूरे इस रिपो को फोर्क करें](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) अपने GitHub अकाउंट पर ताकि आप किसी भी कोड को बदल सकें और चुनौतियों को पूरा कर सकें। आप इसे और संबंधित रिपोज़ को आसान तलाश के लिए [स्टार (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) भी कर सकते हैं।

### 2. कोडस्पेस बनाएं

कोड चलाते वक्त किसी भी निर्भरता की समस्या से बचने के लिए, हम इस कोर्स को [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) में चलाने की सलाह देते हैं।

अपने फोर्क में: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 एक सीक्रेट जोड़ें

1. ⚙️ गियर आइकन -> कमांड पैलेट -> Codespaces : Manage user secret -> Add a new secret.
2. नाम OPENAI_API_KEY रखें, अपनी कुंजी पेस्ट करें, Save करें।

### 3. आगे क्या?

| मैं क्या करना चाहता हूँ…    | जाएं…                                                                |
|---------------------------|----------------------------------------------------------------------|
| लेसन 1 शुरू करें          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| ऑफलाइन काम करें           | [`setup-local.md`](02-setup-local.md)                                |
| एक LLM प्रदाता सेटअप करें  | [`providers.md`](03-providers.md)                                    |
| अन्य शिक्षार्थियों से मिलें | [हमारे डिस्कॉर्ड में शामिल हों](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## समस्या निवारण


| लक्षण                                     | समाधान                                                      |
|-------------------------------------------|------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनट से अधिक रुका हुआ      | **Codespaces ➜ “Rebuild Container”**                        |
| `python: command not found`               | टर्मिनल जुड़ा नहीं; क्लिक करें **+** ➜ *bash*              |
| OpenAI से `401 Unauthorized`               | गलत / एक्सपायर `OPENAI_API_KEY`                            |
| VS कोड दिखाता है “Dev container mounting…”| ब्राउज़र टैब रीफ्रेश करें — Codespaces कभी-कभी कनेक्शन खो देता है |
| नोटबुक कर्नेल गायब                      | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   यूनिक्स-आधारित सिस्टम:

   ```bash
   touch .env
   ```

   विंडोज़:

   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल एडिट करें**: `.env` फाइल को टेक्स्ट एडिटर (जैसे VS Code, Notepad++, या कोई अन्य) में खोलें। निम्नलिखित लाइनें जोड़ें, इनपुट ढेर (placeholder) को अपने वास्तविक Microsoft Foundry Models एंडपॉइंट और की से बदलें (कैसे प्राप्त करें, देखें [`providers.md`](03-providers.md)):

   > **नोट:** GitHub Models (और इसका `GITHUB_TOKEN` वैरिएबल) जुलाई 2026 के अंत में बंद हो रहा है। इसके बजाय [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) का उपयोग करें।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फ़ाइल सेव करें**: बदलाव सेव करें और टेक्स्ट एडिटर बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: यदि आपने पहले से नहीं किया है, तो `.env` फाइल से एनवायरनमेंट वेरिएबल्स को अपने Python एप्लिकेशन में लोड करने के लिए `python-dotenv` पैकेज इंस्टॉल करें। आप इसे `pip` से इंस्टॉल कर सकते हैं:

   ```bash
   pip install python-dotenv
   ```

6. **अपनी Python स्क्रिप्ट में एनवायरनमेंट वेरिएबल लोड करें**: अपनी Python स्क्रिप्ट में `.env` फाइल से एनवायरनमेंट वेरिएबल लोड करने के लिए `python-dotenv` पैकेज का उपयोग करें:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फ़ाइल से पर्यावरण चर लोड करें
   load_dotenv()

   # Microsoft Foundry मॉडल चर तक पहुँचें
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

बस इतना ही! आपने सफलतापूर्वक `.env` फाइल बनाई, अपने Microsoft Foundry Models क्रेडेंशियल जोड़े और उन्हें अपनी Python एप्लिकेशन में लोड किया।

## अपने कंप्यूटर पर लोकली कैसे रन करें

कोड को अपने कंप्यूटर पर लोकली चलाने के लिए, आपके पास किसी संस्करण का [Python इंस्टॉल होना चाहिए](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

फिर रिपोज़िटरी को क्लोन करें:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

जब सब कुछ चेक आउट हो जाए, तब आप शुरू कर सकते हैं!

## वैकल्पिक स्टेप्स

### मिनीकोंडा इंस्टॉल करना

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है जो [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python और कुछ पैकेज इंस्टॉल करता है।
Conda खुद एक पैकेज मैनेजर है जो आपको विभिन्न Python [**वर्चुअल वातावरणों**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेजों के बीच सेटअप और स्विचिंग को आसान बनाता है। साथ ही यह उन पैकेजों को इंस्टॉल करने में मदद करता है जो `pip` के माध्यम से उपलब्ध नहीं हैं।

आप [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) का पालन करके इसे सेटअप कर सकते हैं।

Miniconda इंस्टॉल करने के बाद, आपको [रिपोज़िटरी](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) को क्लोन करना होगा (यदि पहले नहीं किया है)

इसके बाद, आपको एक वर्चुअल एनवायरनमेंट बनाना होगा। Conda के साथ ऐसा करने के लिए, एक नया एनवायरनमेंट फ़ाइल (_environment.yml_) बनाएं। यदि आप Codespaces का उपयोग कर रहे हैं, तो इसे `.devcontainer` डाइरेक्टरी के भीतर बनाएं, यानी `.devcontainer/environment.yml`।

आप नीचे दिए गए स्निपेट के साथ अपना एनवायरनमेंट फ़ाइल भर सकते हैं:

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

यदि आपको Conda का उपयोग करते हुए त्रुटियां मिलती हैं, तो आप मैन्युअली Microsoft AI लाइब्रेरीज़ निम्न कमांड से टर्मिनल में इंस्टॉल कर सकते हैं।

```
conda install -c microsoft azure-ai-ml
```

एनवायरनमेंट फ़ाइल में दी गई निर्भरताएं नमूना हैं। `<environment-name>` वह नाम है जिसे आप अपने Conda एनवायरनमेंट के लिए उपयोग करना चाहते हैं, और `<python-version>` वह Python का संस्करण है जिसे आप उपयोग करना चाहते हैं, उदाहरण के लिए `3` Python का नवीनतम प्रमुख संस्करण है।

ये सब हो जाने पर, आप अपने कमांड लाइन/टर्मिनल में नीचे दिए गए कमांड चलाकर अपना Conda एनवायरनमेंट बना सकते हैं

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उपपथ केवल Codespace सेटअप पर लागू होता है
conda activate ai4beg
```

किसी भी समस्या आने पर [Conda वातावरण गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

### Python सपोर्ट एक्सटेंशन के साथ Visual Studio Code का उपयोग

हम इस कोर्स के लिए [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) संपादक का उपयोग करने की सलाह देते हैं जिसमें [Python सपोर्ट एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इंस्टॉल हो। यह केवल सलाह है, अनिवार्य नहीं।

> **नोट**: कोर्स रिपोजिटरी को VS Code में खोलकर, आपके पास प्रोजेक्ट को कंटेनर के भीतर सेटअप करने का विकल्प होता है। इसका कारण कोर्स रिपोजिटरी के भीतर मौजूद [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) निर्देशिका है। इसके बारे में आगे विस्तार में बताया जाएगा।

> **नोट**: जब आप रिपोजिटरी को क्लोन करके VS Code में खोलते हैं, तो यह अपने आप आपको Python सपोर्ट एक्सटेंशन इंस्टॉल करने का सुझाव देगा।

> **नोट**: यदि VS Code सुझाव दे कि रिपोजिटरी को पुनः कंटेनर में खोलें, तो इस अनुरोध को अस्वीकार करें ताकि आप लोकली इंस्टॉल किए गए Python का उपयोग कर सकें।

### ब्राउज़र में Jupyter का उपयोग

आप प्रोजेक्ट पर ब्राउज़र में ही [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) का उपयोग कर सकते हैं। क्लासिक Jupyter और [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोनों एक सुखद विकास वातावरण प्रदान करते हैं जिनमें ऑटो-कंप्लीशन, कोड हाईलाइटिंग जैसी सुविधाएँ होती हैं।

Jupyter लोकली स्टार्ट करने के लिए, टर्मिनल/कमांड लाइन पर जाएं, कोर्स डाइरेक्टरी में नेविगेट करें और यह कमांड चलाएं:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

यह Jupyter इंस्टेंस स्टार्ट करेगा और इसका एक्सेस URL कमांड लाइन विंडो में दिखेगा।

एक बार URL एक्सेस करने पर, आप कोर्स आउटलाइन देख सकते हैं और किसी भी `*.ipynb` फाइल पर नेविगेट कर सकते हैं। उदाहरण के लिए, `08-building-search-applications/python/oai-solution.ipynb`।

### कंटेनर में रन करना

अपने कंप्यूटर या Codespace पर सब कुछ सेटअप करने के एक विकल्प के रूप में, आप [कंटेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) का उपयोग कर सकते हैं। कोर्स रिपोज़िटरी के विशेष `.devcontainer` फोल्डर की मदद से VS Code प्रोजेक्ट को कंटेनर के भीतर सेटअप कर सकता है। Codespaces के बाहर, इसके लिए Docker इंस्टॉलेशन आवश्यक होगा, और काफी कार्य लगेगा, इसलिए हम इसे उन ही लोगों को सलाह देते हैं जिन्हें कंटेनर के साथ काम करने का अनुभव हो।

GitHub Codespaces का उपयोग करते समय आपकी API कुंजियाँ सुरक्षित रखने के सबसे अच्छे तरीकों में से एक Codespace Secrets का उपयोग करना है। कृपया [Codespaces Secrets प्रबंधन](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड का पालन करें।


## लेसन और तकनीकी आवश्यकताएं

इस कोर्स में "Learn" लेसन होते हैं जो जनरेटिव AI अवधारणाएं समझाते हैं और "Build" लेसन होते हैं जिनमें संभावित जगहों पर **Python** और **TypeScript** में हैंड्स-ऑन कोड उदाहरण होते हैं।

कोडिंग लेसन के लिए, हम Microsoft Foundry में Azure OpenAI का उपयोग करते हैं। आपके पास Azure सब्सक्रिप्शन और API कुंजी होनी चाहिए। एक्सेस खुला है - कोई आवेदन आवश्यक नहीं - इसलिए आप [Microsoft Foundry resource बनाकर और मॉडल तैनात करके](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) अपना एंडपॉइंट और कुंजी प्राप्त कर सकते हैं।

प्रत्येक कोडिंग लेसन में एक `README.md` फ़ाइल भी शामिल होती है जहाँ आप बिना चलाए कोड और आउटपुट देख सकते हैं।

## पहली बार Azure OpenAI सेवा का उपयोग

यदि आप पहली बार Azure OpenAI सेवा का उपयोग कर रहे हैं, तो कृपया यह गाइड देखें कि [Azure OpenAI Service resource कैसे बनाएं और तैनात करें।](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## पहली बार OpenAI API का उपयोग

यदि आप पहली बार OpenAI API का उपयोग कर रहे हैं, तो कृपया गाइड का पालन करें कि [इंटरफ़ेस कैसे बनाएं और उपयोग करें।](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## अन्य शिक्षार्थियों से मिलें

हमने आधिकारिक [AI Community Discord सर्वर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) में अन्य शिक्षार्थियों से मिलने के लिए चैनल बनाए हैं। यह अन्य समान विचारधारा वाले उद्यमियों, बिल्डरों, छात्रों और जो कोई जनरेटिव AI में आगे बढ़ना चाहता है, उनके साथ नेटवर्किंग करने का शानदार तरीका है।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टीम भी इस Discord सर्वर पर किसी भी शिक्षार्थी की मदद करेगी।

## योगदान करें

यह कोर्स एक ओपन-सोर्स प्रयास है। यदि आप सुधार के क्षेत्र या मुद्दे देखें, तो कृपया [पुल रिक्वेस्ट](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाएं या [GitHub इश्यू](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) दर्ज करें।

परियोजना टीम सभी योगदानों की निगरानी करेगी। ओपन-सोर्स में योगदान जनरेटिव AI में अपना करियर बनाने का एक अद्भुत तरीका है।

अधिकांश योगदानों के लिए आपको एक Contributor License Agreement (CLA) से सहमत होना आवश्यक है, जिसमें आप घोषित करते हैं कि आपके पास अपने योगदान का उपयोग करने का अधिकार है। विवरण के लिए देखें [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

महत्वपूर्ण: इस रिपोजिटरी में टेक्स्ट का अनुवाद करते समय कृपया मशीन अनुवाद का उपयोग न करें। हम समुदाय के माध्यम से अनुवादों की जाँच करेंगे, इसलिए कृपया केवल उन भाषाओं में अनुवाद के लिए स्वयंसेवक बनें जिनमें आप प्रवीण हैं।


जब आप एक पुल अनुरोध सबमिट करते हैं, तो एक CLA-बॉट स्वचालित रूप से यह निर्धारित करेगा कि क्या आपको CLA प्रदान करने की आवश्यकता है और पीआर को उपयुक्त रूप से सजाएगा (जैसे, लेबल, टिप्पणी)। बस बॉट द्वारा प्रदान किए गए निर्देशों का पालन करें। आपको हमारे CLA का उपयोग करने वाले सभी रिपॉजिटरीज में यह केवल एक बार करना होगा।

इस प्रोजेक्ट ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) को अपनाया है। अधिक जानकारी के लिए कृपया Code of Conduct FAQ पढ़ें या किसी भी अतिरिक्त प्रश्न या टिप्पणियों के लिए [Email opencode](opencode@microsoft.com) से संपर्क करें।

## चलिए शुरू करते हैं

अब जब आपने इस कोर्स को पूरा करने के लिए आवश्यक कदम पूरे कर लिए हैं, तो चलिए [Generative AI और LLMs का परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त करके शुरू करते हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->