# इस कोर्स की शुरुआत

हम आपके इस कोर्स को शुरू करने और जनरेटिव AI के साथ आप क्या बनाना चाहते हैं, इसे देखने के लिए बहुत उत्साहित हैं!

आपकी सफलता सुनिश्चित करने के लिए, इस पृष्ठ पर सेटअप चरण, तकनीकी आवश्यकताएं, और जरूरत पड़ने पर सहायता कहां मिलेगी, यह बताया गया है।

## सेटअप चरण

इस कोर्स को शुरू करने के लिए, आपको निम्नलिखित चरण पूरे करने होंगे।

### 1. इस रिपो को फोर्क करें

[इस पूरे रिपो को फोर्क करें](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ताकि आप अपने GitHub खाते में किसी भी कोड को बदल सकें और चुनौतियों को पूरा कर सकें। आप इसे और संबंधित रिपोज को आसानी से खोजने के लिए [इस रिपो को स्टार (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) भी कर सकते हैं।

### 2. एक कोडस्पेस बनाएं

कोड चलाते समय किसी भी निर्भरता से बचने के लिए, हम इस कोर्स को [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) में चलाने की सलाह देते हैं।

अपने फोर्क में: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/hi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 एक सीक्रेट जोड़ें

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret।  
2. नाम OPENAI_API_KEY दें, अपनी कुंजी पेस्ट करें, और सेव करें।

### 3. अब आगे क्या करें?

| मैं करना चाहता हूँ…          | जाएं…                                                                  |
|-----------------------------|-------------------------------------------------------------------------|
| लेसन 1 शुरू करें           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ऑफलाइन काम करें            | [`setup-local.md`](02-setup-local.md)                                   |
| एक LLM प्रदाता सेटअप करें | [`providers.md`](03-providers.md)                                        |
| अन्य शिक्षार्थियों से मिलें | [हमारा डिस्कॉर्ड ज्वाइन करें](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या निवारण


| लक्षण                                   | समाधान                                                             |
|-----------------------------------------|------------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनट से अधिक रुका हुआ  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | टर्मिनल संलग्न नहीं हुआ; क्लिक करें **+** ➜ *bash*             |
| OpenAI से `401 Unauthorized`             | गलत / समाप्त `OPENAI_API_KEY`                                    |
| VS Code “Dev container mounting…” दिखाता है| ब्राउज़र टैब रिफ्रेश करें—Codespaces कभी-कभी कनेक्शन खो देता है|
| नोटबुक कर्नेल गायब                     | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   यूनिक्स-आधारित सिस्टम:

   ```bash
   touch .env
   ```

   विंडोज़:

   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल संपादित करें**: `.env` फ़ाइल को किसी टेक्स्ट एडिटर (जैसे VS Code, Notepad++, या कोई और) में खोलें। इस फ़ाइल में निम्नलिखित पंक्ति जोड़ें, जहां `your_github_token_here` को अपने वास्तविक GitHub टोकन से बदलें:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फ़ाइल सहेजें**: परिवर्तनों को सहेजें और टेक्स्ट एडिटर बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: यदि आपने पहले से इंस्टॉल नहीं किया है, तो आपको `python-dotenv` पैकेज इंस्टॉल करना होगा ताकि `.env` फ़ाइल से पर्यावरण चर को अपने Python एप्लिकेशन में लोड कर सकें। `pip` का उपयोग करके इसे इंस्टॉल करें:

   ```bash
   pip install python-dotenv
   ```

6. **अपने Python स्क्रिप्ट में पर्यावरण चर लोड करें**: अपने Python स्क्रिप्ट में, `python-dotenv` पैकेज का उपयोग करके `.env` फ़ाइल से पर्यावरण चर लोड करें:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फ़ाइल से पर्यावरण चर लोड करें
   load_dotenv()

   # GITHUB_TOKEN चर तक पहुँचें
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस इतना ही! आपने सफलतापूर्वक `.env` फ़ाइल बनाई, अपना GitHub टोकन जोड़ा, और इसे अपने Python एप्लिकेशन में लोड किया।

## अपने कंप्यूटर पर लोकल रूप से कैसे चलाएं

अपने कंप्यूटर पर कोड लोकल रूप से चलाने के लिए, आपके पास किसी संस्करण का [Python इंस्टॉल होना चाहिए](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)।

फिर रिपोजिटरी का उपयोग करने के लिए, आपको इसे क्लोन करना होगा:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एक बार जब आपके पास सब कुछ तैयार हो जाए, तो आप शुरुआत कर सकते हैं!

## वैकल्पिक चरण

### मिनीकॉन्डा स्थापित करना

[मिनीकॉन्डा](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है जो [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, और कुछ पैकेज स्थापित करता है।  
Conda एक पैकेज मैनेजर है, जो विभिन्न Python [**वर्चुअल वातावरण**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेजों को सेटअप और स्विच करना आसान बनाता है। यह उन पैकेजों को इंस्टॉल करने के लिए भी उपयोगी है जो `pip` के ज़रिए उपलब्ध नहीं हैं।

आप इसे सेटअप करने के लिए [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) का पालन कर सकते हैं।

मिनीकॉन्डा इंस्टॉल करने के बाद, यदि आपने अभी तक रिपोजिटरी क्लोन नहीं किया है तो क्लोन करें: [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)।

इसके बाद, वर्चुअल वातावरण बनाना होगा। Conda के साथ ऐसा करने के लिए, एक नया environment फ़ाइल (_environment.yml_) बनाएं। यदि आप Codespaces का उपयोग कर रहे हैं, तो इसे `.devcontainer` डायरेक्टरी के अंदर बनाएं, यानी `.devcontainer/environment.yml`।

अपने environment फ़ाइल को नीचे दिए स्निपेट से भरें:

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

यदि आपको Conda का उपयोग करते समय त्रुटियां मिल रही हैं, तो आप टर्मिनल में निम्नलिखित कमांड का उपयोग करके Microsoft AI Libraries मैन्युअली इंस्टॉल कर सकते हैं।

```
conda install -c microsoft azure-ai-ml
```

यह environment फ़ाइल आवश्यक निर्भरताओं को निर्दिष्ट करती है। `<environment-name>` उस नाम को संदर्भित करता है जिसे आप अपने Conda environment के लिए उपयोग करना चाहते हैं, और `<python-version>` उस Python संस्करण को, उदाहरण के लिए, `3` Python का नवीनतम मुख्य संस्करण है।

इसके बाद, नीचे दिए गए कमांड चलाकर Conda environment बना सकते हैं:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप पथ केवल Codespace सेटअप्स पर लागू होता है
conda activate ai4beg
```

यदि कोई समस्या आती है, तो [Conda वातावरण गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

### Python सपोर्ट एक्सटेंशन के साथ Visual Studio Code का उपयोग

हम इस कोर्स के लिए [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) संपादक के साथ [Python सपोर्ट एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) उपयोग करने की सिफारिश करते हैं। यह बाध्यकारी नहीं है, बल्कि केवल एक सुझाव है।

> **नोट**: कोर्स रिपोजिटरी को VS Code में खोलते समय, आपके पास इसे एक कंटेनर के भीतर सेटअप करने का विकल्प होता है। ऐसा इसलिए क्योंकि कोर्स रिपोजिटरी में एक [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डायरेक्टरी होती है। इसके बारे में बाद में और जानकारी दी जाएगी।

> **नोट**: रिपोजिटरी क्लोन करके VS Code में खोलते समय, यह स्वतः ही Python सपोर्ट एक्सटेंशन इंस्टॉल करने का सुझाव देगा।

> **नोट**: यदि VS Code आपको रिपोजिटरी को कंटेनर में पुनः खोलने का सुझाव देता है, तो स्थानीय रूप से इंस्टॉल Python का उपयोग करने के लिए इस अनुरोध को अस्वीकार करें।

### ब्राउज़र में Jupyter का उपयोग करना

आप इस प्रोजेक्ट पर [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) का उपयोग करके सीधे अपने ब्राउज़र में भी काम कर सकते हैं। क्लासिक Jupyter और [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोनों अच्छी विकास सुविधाएं जैसे ऑटो-कंप्लीशन, कोड हाइलाइटिंग आदि प्रदान करते हैं।

लोकल Jupyter शुरू करने के लिए, टर्मिनल/कमांड लाइन खोलें, कोर्स डायरेक्टरी में जाएं और निम्न कमांड चलाएं:

```bash
jupyter notebook
```

या फिर

```bash
jupyterhub
```

यह एक Jupyter इंस्टेंस शुरू करेगा और इसे एक्सेस करने के लिए URL कमांड लाइन विंडो में दिखाया जाएगा।

URL पर पहुँचने के बाद, आपको कोर्स की रूपरेखा दिखेगी और आप किसी भी `*.ipynb` फ़ाइल पर नेविगेट कर सकेंगे, उदाहरण के लिए, `08-building-search-applications/python/oai-solution.ipynb`।

### कंटेनर में चलाना

अपने कंप्यूटर या Codespace पर सब कुछ सेटअप करने के विकल्प के रूप में, आप [कंटेनर](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) का उपयोग कर सकते हैं। कोर्स रिपोजिटरी के भीतर खास `.devcontainer` फ़ोल्डर VS Code को कंटेनर के अंदर प्रोजेक्ट सेटअप करने की अनुमति देता है। Codespaces के बाहर, इसके लिए Docker स्थापित करना होगा, और यह थोड़ा काम माँगता है, इसलिए हम इसे केवल कंटेनर के साथ अनुभव रखने वालों को सलाह देते हैं।

GitHub Codespaces का उपयोग करते समय आपकी API कुंजियों को सुरक्षित रखने का एक बेहतरीन तरीका Codespace Secrets का उपयोग करना है। कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड का पालन करें।

## पाठ और तकनीकी आवश्यकताएं

इस कोर्स में 6 अवधारणा पाठ और 6 कोडिंग पाठ हैं।

कोडिंग पाठों के लिए, हम Azure OpenAI Service का उपयोग कर रहे हैं। आपको Azure OpenAI सेवा और एक API कुंजी की आवश्यकता होगी ताकि आप यह कोड चला सकें। आप [इस आवेदन को पूरा करके](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) एक्सेस के लिए आवेदन कर सकते हैं।

जब तक आपका आवेदन प्रक्रियाधीन है, प्रत्येक कोडिंग पाठ में एक `README.md` फ़ाइल भी होती है जहां आप कोड और आउटपुट देख सकते हैं।

## पहली बार Azure OpenAI Service का उपयोग करना

यदि आप Azure OpenAI सेवा का पहली बार उपयोग कर रहे हैं, तो कृपया इस गाइड का पालन करें जिससे आप [Azure OpenAI Service संसाधन बना और तैनात कर सकें।](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## पहली बार OpenAI API का उपयोग करना

यदि आप पहली बार OpenAI API का उपयोग कर रहे हैं, तो कृपया गाइड का पालन करें कि कैसे [इंटरफ़ेस बनाएं और उपयोग करें।](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## अन्य शिक्षार्थियों से मिलें

हमने अपने आधिकारिक [AI Community Discord सर्वर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) में अन्य शिक्षार्थियों से मिलने के लिए चैनल बनाए हैं। यह समान विचारधारा वाले उद्यमियों, निर्माताओं, छात्रों, और जनरेटिव AI में आगे बढ़ने के इच्छुक किसी भी व्यक्ति के साथ नेटवर्क बनाने का शानदार तरीका है।

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टीम भी इस Discord सर्वर पर रहती है ताकि किसी भी शिक्षार्थी की सहायता कर सके।

## योगदान दें

यह कोर्स एक ओपन-सोर्स पहल है। यदि आप सुधार के क्षेत्र या समस्याएँ देखें, तो कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाएं या [GitHub समस्या](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) दर्ज करें।

प्रोजेक्ट टीम सभी योगदानों पर नजर रखेगी। ओपन सोर्स में योगदान देना जनरेटिव AI में आपके करियर का एक अद्भुत तरीका है।

अधिकांश योगदानों के लिए आपसे एक योगदानकर्ता लाइसेंस समझौते (CLA) पर सहमति मांगी जाती है जिसमें आप पुष्टि करते हैं कि आपके पास योगदान प्रदान करने का अधिकार है और आप हमें इसे उपयोग करने का अधिकार देते हैं। विवरण के लिए देखें [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

महत्वपूर्ण: इस रिपो में टेक्स्ट अनुवाद करते समय कृपया मशीन ट्रांसलेशन का उपयोग न करें। हम समुदाय के माध्यम से अनुवादों की जांच करेंगे, इसलिए कृपया केवल उन भाषाओं में अनुवाद के लिए स्वयंसेवक बनें जिनमें आप निपुण हैं।

जब आप पुल रिक्वेस्ट भेजते हैं, तो एक CLA-बोट स्वचालित रूप से यह निर्धारित करेगा कि आपको CLA प्रदान करना है या नहीं और PR को उपयुक्त रूप से चिन्हित करेगा (जैसे, लेबल, टिप्पणी)। बस बोट द्वारा दिए गए निर्देशों का पालन करें। आपको हमारी CLA का उपयोग करने वाले सभी रिपोज में केवल एक बार ही ऐसा करना होगा।

इस प्रोजेक्ट ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) को अपनाया है। अधिक जानकारी के लिए कोड ऑफ कंडक्ट FAQ पढ़ें या अतिरिक्त प्रश्नों या टिप्पणियों के लिए [Email opencode](opencode@microsoft.com) से संपर्क करें।

## चलिए शुरू करते हैं!
अब जबकि आपने इस कोर्स को पूरा करने के लिए आवश्यक कदम पूरे कर लिए हैं, आइए शुरू करते हैं [Generative AI और LLMs का परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त करके।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करते हुए किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान रखें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ अपने मूल भाषा में आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->