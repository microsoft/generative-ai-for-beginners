# इस कोर्स के साथ शुरुआत करना

हम आपके लिए इस कोर्स को शुरू करने और देखें कि आप जनरेटिव AI के साथ क्या बनाने के लिए प्रेरित होते हैं, इसके लिए बहुत उत्साहित हैं!

आपकी सफलता सुनिश्चित करने के लिए, यह पृष्ठ सेटअप चरणों, तकनीकी आवश्यकताओं, और यदि आवश्यक हो तो मदद कहाँ प्राप्त करें, को बताता है।

## सेटअप चरण

इस कोर्स को शुरू करने के लिए, आपको निम्नलिखित चरणों को पूरा करना होगा।

### 1. इस रिपॉजिटरी को फोर्क करें

[इस पूरे रिपॉजिटरी को फोर्क करें](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) अपने GitHub अकाउंट में, ताकि आप किसी भी कोड को बदल सकें और चुनौतियों को पूरा कर सकें। आप इसे और संबंधित रिपॉजिटरी को आसान खोजने के लिए [इस रिपॉजिटरी को स्टार (🌟) भी कर सकते हैं](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)।

### 2. एक कोडस्पेस बनाएं

कोड चलाते समय किसी भी निर्भरता की समस्याओं से बचने के लिए, हम इस कोर्स को [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) में चलाने की सलाह देते हैं।

अपने फोर्क में: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 एक सीक्रेट जोड़ें

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाम OPENAI_API_KEY रखें, अपनी कुंजी पेस्ट करें, सेव करें।

### 3. अगला क्या है?

| मैं करना चाहता हूँ…   | जाऊं…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| पाठ 1 शुरू करें      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ऑफ़लाइन काम करें    | [`setup-local.md`](02-setup-local.md)                                   |
| एक LLM प्रदाता सेट करें | [`providers.md`](03-providers.md)                                        |
| अन्य सीखने वालों से मिलें | [हमारे Discord में शामिल हों](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या निवारण


| लक्षण                                   | समाधान                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| कंटेनर निर्माण 10 मिनट से अधिक समय तक अटका था | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | टर्मिनल जुड़ा नहीं था; क्लिक करें **+** ➜ *bash*                    |
| OpenAI से `401 Unauthorized`             | गलत / समाप्त हो चुका `OPENAI_API_KEY`                             |
| VS Code में “Dev container mounting…” दिख रहा है | ब्राउज़र टैब को रिफ्रेश करें—Codespaces कभी-कभी कनेक्शन खो देता है   |
| नोटबुक कर्नेल गायब                      | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-आधारित सिस्टम:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल संपादित करें**: `.env` फ़ाइल को किसी टेक्स्ट एडिटर (जैसे VS Code, Notepad++, या कोई अन्य एडिटर) में खोलें। फ़ाइल में नीचे दी गई पंक्तियां जोड़ें, अपने वास्तविक Microsoft Foundry Models endpoint और key के साथ प्लेसहोल्डर को बदलते हुए (देखें [`providers.md`](03-providers.md) में इसे कैसे प्राप्त करें):

   > **नोट:** GitHub Models (और इसका `GITHUB_TOKEN` वेरिएबल) जुलाई 2026 के अंत में सेवानिवृत्त हो रहा है। इसके बजाय [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) का उपयोग करें।

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फ़ाइल सहेजें**: बदलाव सहेजें और टेक्स्ट एडिटर को बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: यदि आपने अभी तक नहीं किया है, तो आपको `python-dotenv` पैकेज इंस्टॉल करना होगा ताकि आप `.env` फ़ाइल से पर्यावरण चर (environment variables) को अपने Python ऐप्लिकेशन में लोड कर सकें। आप इसे `pip` से इंस्टॉल कर सकते हैं:

   ```bash
   pip install python-dotenv
   ```

6. **अपने Python स्क्रिप्ट में Environment Variables लोड करें**: अपने Python स्क्रिप्ट में, `python-dotenv` पैकेज का उपयोग करके `.env` फ़ाइल से environment variables लोड करें:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फ़ाइल से पर्यावरण चर लोड करें
   load_dotenv()

   # Microsoft Foundry Models चर तक पहुँचें
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

बस हो गया! आपने सफलतापूर्वक `.env` फ़ाइल बनाई, अपने Microsoft Foundry Models क्रेडेंशियल जोड़े, और उन्हें अपने Python ऐप्लिकेशन में लोड किया।

## अपने कंप्यूटर पर लोकल रूप से कैसे चलाएं

अपने कंप्यूटर पर कोड को लोकल रूप से चलाने के लिए, आपके पास [Python का कुछ संस्करण इंस्टॉल किया होना चाहिए](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

उसके बाद रिपॉजिटरी का उपयोग करने के लिए, आपको इसे क्लोन करना होगा:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

जब आपके पास सब कुछ चेक आउट हो जाए, तो आप शुरुआत कर सकते हैं!

## वैकल्पिक चरण

### मिनीकॉन्डा इंस्टॉल करना

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है जो [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, और कुछ अन्य पैकेज इंस्टॉल करता है।
Conda स्वयं एक पैकेज मैनेजर है, जो अलग Python [**वर्चुअल एनवायरनमेंट्स**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेज के बीच बदलाव करना आसान बनाता है। यह `pip` के माध्यम से उपलब्ध नहीं पैकेज इंस्टॉल करने में भी सहायक होता है।

आप [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) का पालन कर इसे सेटअप कर सकते हैं।

Miniconda इंस्टॉल करने के बाद, आपको रिपॉजिटरी क्लोन करनी होगी (यदि आपने पहले नहीं किया है)।

इसके बाद, आपको एक वर्चुअल एनवायरनमेंट बनाना होगा। इसके लिए Conda के साथ, एक नया एनवायरनमेंट फ़ाइल (_environment.yml_) बनाएं। यदि आप Codespaces का उपयोग कर रहे हैं, तो इसे `.devcontainer` डायरेक्टरी के अंदर बनाएं, यानी `.devcontainer/environment.yml`।

अपना एनवायरनमेंट फ़ाइल नीचे दिए गए स्निपेट से भरें:

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

यदि आपको conda का उपयोग करते समय त्रुटियाँ मिल रही हैं, तो आप टर्मिनल में निम्नलिखित कमांड के जरिए Microsoft AI Libraries मैन्युअली इंस्टॉल कर सकते हैं।

```
conda install -c microsoft azure-ai-ml
```

एनवायरनमेंट फ़ाइल में आवश्यक निर्भरताओं को निर्दिष्ट किया गया है। `<environment-name>` से तात्पर्य उस नाम से है जो आप अपने Conda एनवायरनमेंट के लिए उपयोग करना चाहते हैं, और `<python-version>` वह Python संस्करण है जो आप उपयोग करना चाहते हैं, उदाहरण के लिए, `3` Python का नवीनतम मेजर वर्ज़न है।

ये सब करने के बाद, आप नीचे दिए गए कमांड अपने कमांड लाइन/टर्मिनल में चलाकर अपना Conda एनवायरनमेंट बना सकते हैं।

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप पथ केवल Codespace सेटअप पर ही लागू होता है
conda activate ai4beg
```

यदि आपको कोई समस्या आती है, तो [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

### Python सपोर्ट एक्सटेंशन के साथ Visual Studio Code का उपयोग करना

हम इस कोर्स के लिए [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) एडिटर का उपयोग करने की सलाह देते हैं जिसमें [Python सपोर्ट एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इंस्टॉल हो। हालांकि, यह केवल एक सुझाव है, अनिवार्य नहीं।

> **नोट**: जब आप कोर्स रिपॉजिटरी को VS Code में खोलते हैं, तो आपके पास प्रोजेक्ट को कंटेनर के अंदर सेटअप करने का विकल्प होता है। इसका कारण है कोर्स रिपॉजिटरी में पाया जाने वाला [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) फोल्डर। इस पर बाद में और जानकारी दी जाएगी।

> **नोट**: जब आप रिपॉजिटरी क्लोन और VS Code में खोलते हैं, तो यह आपको Python सपोर्ट एक्सटेंशन इंस्टॉल करने का सुझाव खुद-ब-खुद देगा।

> **नोट**: यदि VS Code आपको रिपॉजिटरी को कंटेनर में फिर से खोलने का सुझाव देता है, तो यह अनुरोध अस्वीकार कर दें ताकि आप लोकल इंस्टॉल्ड Python संस्करण का उपयोग कर सकें।

### ब्राउज़र में Jupyter का उपयोग करना

आप प्रोजेक्ट पर अपने ब्राउज़र के भीतर [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) का भी उपयोग कर सकते हैं। क्लासिक Jupyter और [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोनों एक सुखद विकास वातावरण प्रदान करते हैं जिसके फीचर स्वचालित पूर्ति, कोड हाइलाइटिंग, इत्यादि हैं।

लोकल Jupyter शुरू करने के लिए, टर्मिनल/कमांड लाइन में जाएं, कोर्स डायरेक्टरी पर नेविगेट करें, और चलाएं:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

यह एक Jupyter इंस्टेंस शुरू करेगा और इसे एक्सेस करने के लिए URL कमांड लाइन विंडो में दिखाया जाएगा।

URL तक पहुँचने पर, आप कोर्स की रूपरेखा देख सकेंगे और किसी भी `*.ipynb` फ़ाइल पर नेविगेट कर सकेंगे। उदाहरण के लिए, `08-building-search-applications/python/oai-solution.ipynb`।

### कंटेनर में चलाना

अपने कंप्यूटर या Codespace पर सब कुछ सेटअप करने का एक विकल्प है [कंटेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) का उपयोग करना। कोर्स रिपॉजिटरी में विशेष `.devcontainer` फोल्डर की वजह से VS Code प्रोजेक्ट को कंटेनर में सेटअप कर सकता है। Codespaces के बाहर, इसके लिए Docker इंस्टॉल करना होगा, और सच कहें तो, इसमें थोड़ा काम शामिल होता है, इसलिए हम इसे केवल कंटेनर के साथ काम करने के अनुभव वाले लोगों को सलाह देते हैं।

GitHub Codespaces का उपयोग करते समय अपने API कुंजी सुरक्षित रखने के सर्वोत्तम तरीकों में से एक है Codespace Secrets का उपयोग करना। कृपया इस बारे में अधिक जानने के लिए [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड का पालन करें।


## पाठ और तकनीकी आवश्यकताएँ

कोर्स में 6 कॉन्सेप्ट पाठ और 6 कोडिंग पाठ हैं।

कोडिंग पाठों के लिए, हम Azure OpenAI Service का उपयोग कर रहे हैं। इस कोड को चलाने के लिए आपको Azure OpenAI सेवा और एक API कुंजी की आवश्यकता होगी। आप [यहाँ आवेदन करके](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) एक्सेस प्राप्त कर सकते हैं।

आपकी आवेदन प्रक्रिया पूरी होने तक, प्रत्येक कोडिंग पाठ में एक `README.md` फ़ाइल भी शामिल है जहां आप कोड और आउटपुट देख सकते हैं।

## पहली बार Azure OpenAI सेवा का उपयोग करना

यदि यह आपका Azure OpenAI सेवा के साथ पहला अनुभव है, तो कृपया [Azure OpenAI सेवा संसाधन बनाने और तैनात करने](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) के बारे में यह मार्गदर्शिका देखें।

## पहली बार OpenAI API का उपयोग करना

यदि यह आपका OpenAI API के साथ पहला अनुभव है, तो कृपया [इंटरफेस बनाने और उपयोग करने](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) के लिए निर्देश देखें।

## अन्य सीखने वालों से मिलें

हमने अन्य सीखने वालों से मिलने के लिए हमारे आधिकारिक [AI Community Discord सर्वर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) में चैनल बनाए हैं। यह अन्य समान विचारधारा वाले उद्यमियों, बिल्डरों, छात्रों, और जनरेटिव AI में स्तर बढ़ाने के इच्छुक किसी भी व्यक्ति से नेटवर्क बनाने का शानदार तरीका है।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

परियोजना टीम भी इस Discord सर्वर पर होगी ताकि किसी भी सीखने वाले की मदद कर सके।

## योगदान करें

यह कोर्स एक ओपन-सोर्स पहल है। यदि आप सुधार के क्षेत्र या समस्याएं देखते हैं, तो कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाएं या [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) दर्ज करें।

परियोजना टीम सभी योगदानों को ट्रैक करेगी। ओपन सोर्स में योगदान करना जनरेटिव AI में अपने करियर को विकसित करने का एक शानदार तरीका है।

अधिकांश योगदानों के लिए आपको एक Contributor License Agreement (CLA) से सहमत होना होगा जिसमें आप घोषणा करते हैं कि आपके पास अपने योगदान का उपयोग करने के अधिकार हैं और वास्तव में उस अधिकार को हमें प्रदान करते हैं। विवरण के लिए, देखें [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

महत्वपूर्ण: इस रिपॉजिटरी में जब भी आप टेक्स्ट का अनुवाद करें, कृपया सुनिश्चित करें कि आप मशीन अनुवाद का उपयोग न करें। हम सामाजिक समुदाय के माध्यम से अनुवादों का सत्यापन करेंगे, इसलिए केवल उन भाषाओं के लिए स्वयंसेवक के रूप में अनुवाद करें जिनमें आप प्रवीण हैं।

जब आप पુલ रिक्वेस्ट सबमिट करते हैं, तो CLA-बॉट स्वचालित रूप से यह निर्धारित करेगा कि क्या आपको CLA प्रदान करना है और PR गणवेश को उपयुक्त रूप से सजाएगा (जैसे लेबल, टिप्पणी)। बस बॉट द्वारा दिए गए निर्देशों का पालन करें। आपको यह एक बार सभी रिपॉजिटरी में करना होगा जो हमारे CLA का उपयोग करते हैं।


इस परियोजना ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) को अपनाया है। अधिक जानकारी के लिए Code of Conduct FAQ पढ़ें या किसी भी अतिरिक्त प्रश्नों या टिप्पणियों के लिए [Email opencode](opencode@microsoft.com) से संपर्क करें।

## चलिए शुरू करते हैं

अब जब आपने इस कोर्स को पूरा करने के लिए आवश्यक कदम पूरे कर लिए हैं, तो चलिए शुरू करते हैं और [Generative AI और LLMs का परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त करते हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->