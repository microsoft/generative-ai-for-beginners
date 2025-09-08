<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:23:51+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hi"
}
-->
# इस कोर्स के साथ शुरुआत करें

हम बहुत उत्साहित हैं कि आप इस कोर्स की शुरुआत कर रहे हैं और देखना चाहते हैं कि आप Generative AI के साथ क्या नया बना सकते हैं!

आपकी सफलता सुनिश्चित करने के लिए, इस पेज पर सेटअप के स्टेप्स, तकनीकी आवश्यकताएँ और ज़रूरत पड़ने पर सहायता कहाँ मिलेगी, इसकी जानकारी दी गई है।

## सेटअप स्टेप्स

इस कोर्स को शुरू करने के लिए, आपको निम्नलिखित स्टेप्स पूरे करने होंगे।

### 1. इस रिपॉजिटरी को फोर्क करें

[इस पूरी रिपॉजिटरी को फोर्क करें](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) अपने खुद के GitHub अकाउंट में, ताकि आप कोड में बदलाव कर सकें और चैलेंज पूरे कर सकें। आप चाहें तो [इस रिपॉजिटरी को स्टार (🌟) भी कर सकते हैं](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), जिससे इसे और संबंधित रिपॉजिटरीज़ को ढूंढना आसान रहेगा।

### 2. एक कोडस्पेस बनाएं

कोड चलाते समय किसी भी डिपेंडेंसी समस्या से बचने के लिए, हम सलाह देते हैं कि आप इस कोर्स को [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) में चलाएँ।

अपने फोर्क में: **Code -> Codespaces -> New on main**

![कोडस्पेस बनाने के लिए डायलॉग बॉक्स](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 एक सीक्रेट जोड़ें

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाम दें OPENAI_API_KEY, अपनी key पेस्ट करें, Save करें।

### 3. आगे क्या?

| मैं यह करना चाहता हूँ…      | यहाँ जाएँ…                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| लेसन 1 शुरू करें           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| ऑफलाइन काम करें            | [`setup-local.md`](02-setup-local.md)                                       |
| LLM प्रोवाइडर सेटअप करें    | [`providers.md`](providers.md)                                              |
| अन्य लर्नर्स से मिलें       | [हमारे Discord से जुड़ें](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## समस्या निवारण

| समस्या                                      | समाधान                                                           |
|----------------------------------------------|------------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनट से ज्यादा अटका है      | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                  | टर्मिनल अटैच नहीं हुआ; **+** ➜ *bash* पर क्लिक करें              |
| OpenAI से `401 Unauthorized`                 | गलत / एक्सपायर्ड `OPENAI_API_KEY`                                |
| VS Code में “Dev container mounting…” दिख रहा| ब्राउज़र टैब रिफ्रेश करें—Codespaces कभी-कभी कनेक्शन खो देता है  |
| नोटबुक कर्नेल गायब है                       | Notebook मेन्यू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   यूनिक्स-बेस्ड सिस्टम्स:

   ```bash
   touch .env
   ```

   विंडोज़:

   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल एडिट करें**: `.env` फ़ाइल को किसी टेक्स्ट एडिटर (जैसे VS Code, Notepad++, या कोई और) में खोलें। नीचे दी गई लाइन जोड़ें, और `your_github_token_here` को अपने असली GitHub टोकन से बदलें:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फ़ाइल सेव करें**: बदलाव सेव करें और एडिटर बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: अगर आपने पहले से नहीं किया है, तो आपको `python-dotenv` पैकेज इंस्टॉल करना होगा ताकि `.env` फ़ाइल से environment variables आपके Python एप्लिकेशन में लोड हो सकें। इसे `pip` से इंस्टॉल करें:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्ट में Environment Variables लोड करें**: अपनी Python स्क्रिप्ट में, `python-dotenv` पैकेज का उपयोग करके `.env` फ़ाइल से environment variables लोड करें:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस! आपने सफलतापूर्वक `.env` फ़ाइल बनाई, अपना GitHub टोकन जोड़ा, और उसे अपने Python एप्लिकेशन में लोड किया।

## अपने कंप्यूटर पर लोकली कैसे चलाएँ

कोड को अपने कंप्यूटर पर लोकली चलाने के लिए, आपके पास [Python का कोई वर्शन इंस्टॉल](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) होना चाहिए।

इसके बाद रिपॉजिटरी का उपयोग करने के लिए, आपको इसे क्लोन करना होगा:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एक बार सब कुछ चेकआउट हो जाए, तो आप शुरुआत कर सकते हैं!

## वैकल्पिक स्टेप्स

### Miniconda इंस्टॉल करना

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है, जिससे आप [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, और कुछ पैकेज इंस्टॉल कर सकते हैं।
Conda खुद एक पैकेज मैनेजर है, जिससे अलग-अलग Python [**वर्चुअल एनवायरनमेंट्स**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेजेस को सेटअप और स्विच करना आसान हो जाता है। यह उन पैकेजेस को इंस्टॉल करने में भी मदद करता है जो `pip` से उपलब्ध नहीं हैं।

आप [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) को फॉलो करके इसे सेटअप कर सकते हैं।

Miniconda इंस्टॉल होने के बाद, आपको [रिपॉजिटरी](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) को क्लोन करना होगा (अगर आपने पहले से नहीं किया है)

इसके बाद, आपको एक वर्चुअल एनवायरनमेंट बनाना होगा। Conda के साथ ऐसा करने के लिए, एक नया environment फाइल (_environment.yml_) बनाएं। अगर आप Codespaces का उपयोग कर रहे हैं, तो इसे `.devcontainer` डायरेक्टरी के अंदर बनाएं, यानी `.devcontainer/environment.yml`।

अब अपने environment फाइल को नीचे दिए गए स्निपेट से भरें:

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

अगर आपको conda का उपयोग करते समय कोई एरर आए, तो आप नीचे दिए गए कमांड से Microsoft AI Libraries मैन्युअली इंस्टॉल कर सकते हैं।

```
conda install -c microsoft azure-ai-ml
```

environment फाइल में हमारी ज़रूरत की dependencies बताई गई हैं। `<environment-name>` वह नाम है जो आप अपने Conda environment के लिए रखना चाहते हैं, और `<python-version>` वह वर्शन है जो आप Python के लिए इस्तेमाल करना चाहते हैं, जैसे `3` Python का लेटेस्ट मेजर वर्शन है।

अब आप नीचे दिए गए कमांड्स को अपने कमांड लाइन/टर्मिनल में चलाकर Conda environment बना सकते हैं

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

अगर कोई समस्या आए तो [Conda environments गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

### Python सपोर्ट एक्सटेंशन के साथ Visual Studio Code का उपयोग

हम सलाह देते हैं कि आप इस कोर्स के लिए [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) एडिटर का उपयोग करें, जिसमें [Python सपोर्ट एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इंस्टॉल हो। हालांकि, यह सिर्फ एक सुझाव है, अनिवार्य नहीं।

> **Note**: जब आप कोर्स रिपॉजिटरी को VS Code में खोलते हैं, तो आपके पास प्रोजेक्ट को कंटेनर में सेटअप करने का विकल्प होता है। ऐसा इसलिए है क्योंकि कोर्स रिपॉजिटरी में [स्पेशल `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डायरेक्टरी है। आगे और जानकारी मिलेगी।

> **Note**: जैसे ही आप डायरेक्टरी को क्लोन करके VS Code में खोलेंगे, यह अपने आप आपको Python सपोर्ट एक्सटेंशन इंस्टॉल करने का सुझाव देगा।

> **Note**: अगर VS Code आपको रिपॉजिटरी को कंटेनर में री-ओपन करने का सुझाव दे, तो इस अनुरोध को मना कर दें ताकि आप लोकली इंस्टॉल किए गए Python वर्शन का उपयोग कर सकें।

### ब्राउज़र में Jupyter का उपयोग

आप इस प्रोजेक्ट पर [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) के ज़रिए भी ब्राउज़र में काम कर सकते हैं। क्लासिक Jupyter और [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोनों ही ऑटो-कम्प्लीशन, कोड हाइलाइटिंग जैसी सुविधाओं के साथ अच्छा डेवलपमेंट अनुभव देते हैं।

Jupyter को लोकली शुरू करने के लिए, टर्मिनल/कमांड लाइन में जाएँ, कोर्स डायरेक्टरी में जाएँ, और यह कमांड चलाएँ:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

इससे Jupyter इंस्टेंस शुरू हो जाएगा और कमांड लाइन विंडो में एक्सेस करने के लिए URL दिखेगा।

URL खोलने पर आपको कोर्स का आउटलाइन दिखेगा और आप किसी भी `*.ipynb` फाइल पर जा सकते हैं। उदाहरण के लिए, `08-building-search-applications/python/oai-solution.ipynb`।

### कंटेनर में चलाना

अपने कंप्यूटर या Codespace पर सब कुछ सेटअप करने का एक विकल्प यह है कि आप [कंटेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) का उपयोग करें। कोर्स रिपॉजिटरी में मौजूद स्पेशल `.devcontainer` फोल्डर की वजह से VS Code प्रोजेक्ट को कंटेनर में सेटअप कर सकता है। Codespaces के बाहर, इसके लिए Docker इंस्टॉल करना होगा, और यह थोड़ा जटिल हो सकता है, इसलिए हम इसे उन्हीं के लिए सुझाते हैं जिन्हें कंटेनर के साथ काम करने का अनुभव है।

GitHub Codespaces का उपयोग करते समय अपने API keys को सुरक्षित रखने का सबसे अच्छा तरीका Codespace Secrets का उपयोग करना है। कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) गाइड देखें।

## पाठ्यक्रम और तकनीकी आवश्यकताएँ

इस कोर्स में 6 कॉन्सेप्ट लेसन और 6 कोडिंग लेसन हैं।

कोडिंग लेसन्स के लिए, हम Azure OpenAI Service का उपयोग कर रहे हैं। इस कोड को चलाने के लिए आपको Azure OpenAI service और एक API key की आवश्यकता होगी। आप [यह आवेदन पूरा करके](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) एक्सेस के लिए आवेदन कर सकते हैं।

जब तक आपका आवेदन प्रोसेस हो रहा है, हर कोडिंग लेसन में एक `README.md` फाइल भी है जिसमें आप कोड और आउटपुट देख सकते हैं।

## पहली बार Azure OpenAI Service का उपयोग करना

अगर आप पहली बार Azure OpenAI service के साथ काम कर रहे हैं, तो कृपया यह गाइड फॉलो करें कि [Azure OpenAI Service resource कैसे बनाएं और डिप्लॉय करें।](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## पहली बार OpenAI API का उपयोग करना

अगर आप पहली बार OpenAI API के साथ काम कर रहे हैं, तो कृपया यह गाइड फॉलो करें कि [Interface कैसे बनाएं और उपयोग करें।](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## अन्य लर्नर्स से मिलें

हमने अपने आधिकारिक [AI Community Discord सर्वर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) में अन्य लर्नर्स से मिलने के लिए चैनल बनाए हैं। यह नेटवर्किंग के लिए शानदार जगह है, जहाँ आप अन्य उद्यमियों, बिल्डर्स, छात्रों और Generative AI में आगे बढ़ने के इच्छुक लोगों से मिल सकते हैं।

[![डिस्कॉर्ड चैनल जॉइन करें](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टीम भी इस Discord सर्वर पर लर्नर्स की मदद के लिए उपलब्ध रहेगी।

## योगदान करें

यह कोर्स एक ओपन-सोर्स पहल है। अगर आपको सुधार की कोई जगह या कोई समस्या दिखे, तो कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) बनाएं या [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) दर्ज करें।

प्रोजेक्ट टीम सभी योगदानों को ट्रैक करेगी। ओपन सोर्स में योगदान करना Generative AI में अपना करियर बनाने का शानदार तरीका है।

अधिकांश योगदानों के लिए आपको Contributor License Agreement (CLA) से सहमत होना होगा, जिसमें आप यह घोषणा करते हैं कि आपके पास योगदान करने का अधिकार है और आप हमें अपने योगदान का उपयोग करने का अधिकार देते हैं। अधिक जानकारी के लिए देखें [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)।

महत्वपूर्ण: जब आप इस रिपॉजिटरी में टेक्स्ट का अनुवाद करें, तो कृपया सुनिश्चित करें कि आप मशीन ट्रांसलेशन का उपयोग न करें। हम अनुवादों को समुदाय के माध्यम से सत्यापित करेंगे, इसलिए केवल उन्हीं भाषाओं में अनुवाद के लिए स्वयंसेवक बनें, जिनमें आप दक्ष हैं।

जब आप pull request सबमिट करेंगे, तो CLA-bot अपने आप तय करेगा कि आपको CLA देना है या नहीं और PR को सही लेबल या कमेंट से सजाएगा। बस बॉट द्वारा दिए गए निर्देशों का पालन करें। आपको यह प्रक्रिया हमारे सभी रिपॉजिटरीज़ में केवल एक बार करनी होगी।

इस प्रोजेक्ट ने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) को अपनाया है। अधिक जानकारी के लिए Code of Conduct FAQ पढ़ें या [Email opencode](opencode@microsoft.com) पर अपने सवाल या सुझाव भेजें।

## चलिए शुरुआत करते हैं
अब जब आपने इस कोर्स को पूरा करने के लिए जरूरी कदम उठा लिए हैं, तो चलिए शुरू करते हैं और [जनरेटिव एआई और LLMs का परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) प्राप्त करते हैं।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।