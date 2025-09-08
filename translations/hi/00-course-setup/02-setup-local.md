<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:23:06+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "hi"
}
-->
# लोकल सेटअप 🖥️

**इस गाइड का इस्तेमाल करें अगर आप सब कुछ अपने लैपटॉप पर चलाना चाहते हैं।**  
आपके पास दो रास्ते हैं: **(A) नेटिव Python + वर्चुअल-एन्व** या **(B) VS Code Dev Container with Docker**।  
जो भी आसान लगे, चुनें—दोनों सेम लेसन तक पहुंचाते हैं।

## 1.  आवश्यकताएँ

| टूल                | वर्शन / नोट्स                                                                       |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (यहाँ से लें: <https://python.org>)                                          |
| **Git**            | लेटेस्ट (Xcode / Git for Windows / Linux पैकेज मैनेजर के साथ आता है)                |
| **VS Code**        | ऑप्शनल लेकिन सलाह दी जाती है <https://code.visualstudio.com>                        |
| **Docker Desktop** | *सिर्फ* Option B के लिए। फ्री इंस्टॉल: <https://docs.docker.com/desktop/>            |

> 💡 **टिप** – टूल्स को टर्मिनल में वेरिफाई करें:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  विकल्प A – नेटिव Python (सबसे तेज़)

### स्टेप 1  इस रिपो को क्लोन करें

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### स्टेप 2 वर्चुअल एन्वायरनमेंट बनाएं और एक्टिवेट करें

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ प्रॉम्प्ट अब (.venv) से शुरू होना चाहिए—इसका मतलब है आप एन्व के अंदर हैं।

### स्टेप 3 डिपेंडेंसी इंस्टॉल करें

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) सेक्शन 3 पर जाएं

## 2. विकल्प B – VS Code Dev Container (Docker)

हमने इस रिपॉजिटरी और कोर्स को एक [डेवलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) के साथ सेटअप किया है जिसमें यूनिवर्सल रनटाइम है जो Python3, .NET, Node.js और Java डेवलपमेंट को सपोर्ट करता है। इसका कॉन्फ़िगरेशन `devcontainer.json` फाइल में `.devcontainer/` फोल्डर के अंदर है।

>**इसे क्यों चुनें?**
>कोडस्पेसेस जैसा ही एन्वायरनमेंट; कोई डिपेंडेंसी ड्रिफ्ट नहीं।

### स्टेप 0 एक्स्ट्रा इंस्टॉल करें

Docker Desktop – कन्फर्म करें ```docker --version``` काम करता है।
VS Code Remote – Containers एक्सटेंशन (ID: ms-vscode-remote.remote-containers).

### स्टेप 1 रिपो को VS Code में खोलें

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code `.devcontainer/` डिटेक्ट करता है और एक प्रॉम्प्ट दिखाता है।

### स्टेप 2 कंटेनर में रीओपन करें

“Reopen in Container” पर क्लिक करें। Docker इमेज बनाता है (पहली बार ≈ 3 मिनट)।  
जब टर्मिनल प्रॉम्प्ट दिखे, आप कंटेनर के अंदर हैं।

## 2.  विकल्प C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python और कुछ पैकेज इंस्टॉल करने के लिए।
Conda खुद एक पैकेज मैनेजर है, जिससे अलग-अलग Python [**वर्चुअल एन्वायरनमेंट**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेज सेटअप और स्विच करना आसान होता है। यह उन पैकेज को इंस्टॉल करने में भी मदद करता है जो `pip` से नहीं मिलते।

### स्टेप 0  Miniconda इंस्टॉल करें

[MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) फॉलो करें।

```bash
conda --version
```

### स्टेप 1 वर्चुअल एन्वायरनमेंट बनाएं

नया एन्वायरनमेंट फाइल (*environment.yml*) बनाएं। अगर आप Codespaces इस्तेमाल कर रहे हैं, तो इसे `.devcontainer` डायरेक्टरी में बनाएं, यानी `.devcontainer/environment.yml`।

### स्टेप 2  एन्वायरनमेंट फाइल में कंटेंट डालें

नीचे दिया गया स्निपेट अपने `environment.yml` में जोड़ें

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

### स्टेप 3 अपना Conda एन्वायरनमेंट बनाएं

नीचे दिए गए कमांड्स कमांड लाइन/टर्मिनल में चलाएं

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

अगर कोई दिक्कत आए तो [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

## 2  विकल्प D – क्लासिक Jupyter / Jupyter Lab (ब्राउज़र में)

> **यह किसके लिए है?**  
> जो क्लासिक Jupyter इंटरफेस पसंद करते हैं या बिना VS Code के नोटबुक चलाना चाहते हैं।  

### स्टेप 1  सुनिश्चित करें कि Jupyter इंस्टॉल है

Jupyter लोकली चलाने के लिए टर्मिनल/कमांड लाइन में जाएं, कोर्स डायरेक्टरी में जाएं, और ये चलाएं:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

इससे Jupyter इंस्टेंस शुरू होगा और एक्सेस करने के लिए URL कमांड लाइन विंडो में दिखेगा।

URL खोलने पर आपको कोर्स आउटलाइन दिखेगी और किसी भी `*.ipynb` फाइल पर जा सकते हैं। जैसे, `08-building-search-applications/python/oai-solution.ipynb`।

## 3. अपनी API Keys जोड़ें

कोई भी एप्लिकेशन बनाते समय अपनी API keys को सुरक्षित रखना बहुत जरूरी है। सलाह है कि API keys को सीधे कोड में न रखें। इन्हें पब्लिक रिपॉजिटरी में कमिट करने से सिक्योरिटी इश्यू और अनचाहे खर्च हो सकते हैं।
यहाँ Python के लिए `.env` फाइल बनाने और उसमें `GITHUB_TOKEN` जोड़ने का तरीका है:

1. **अपने प्रोजेक्ट डायरेक्टरी में जाएं**: टर्मिनल या कमांड प्रॉम्प्ट खोलें और उस डायरेक्टरी में जाएं जहाँ `.env` फाइल बनानी है।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाइल बनाएं**: अपनी पसंदीदा टेक्स्ट एडिटर से नई फाइल बनाएं जिसका नाम `.env` हो। कमांड लाइन से `touch` (Unix-based) या `echo` (Windows) इस्तेमाल कर सकते हैं:

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल एडिट करें**: `.env` फाइल को टेक्स्ट एडिटर (जैसे VS Code, Notepad++, या कोई और) में खोलें। इसमें नीचे दी गई लाइन जोड़ें, `your_github_token_here` को अपने असली GitHub टोकन से बदलें:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल सेव करें**: बदलाव सेव करें और एडिटर बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: अगर पहले नहीं किया है, तो `.env` फाइल से environment variables लोड करने के लिए `python-dotenv` पैकेज इंस्टॉल करें। `pip` से इंस्टॉल करें:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्ट में Environment Variables लोड करें**: अपनी Python स्क्रिप्ट में `python-dotenv` पैकेज से `.env` फाइल के environment variables लोड करें:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस! आपने `.env` फाइल बना ली, GitHub टोकन जोड़ लिया, और उसे अपनी Python एप्लिकेशन में लोड कर लिया।

🔐 कभी भी .env को कमिट न करें—यह पहले से .gitignore में है।
पूरा प्रोवाइडर इंस्ट्रक्शन [`providers.md`](03-providers.md) में है।

## 4. आगे क्या?

| मैं चाहता हूँ…         | जाएं…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| लेसन 1 शुरू करें      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM Provider सेटअप करें | [`providers.md`](03-providers.md)                                       |
| अन्य सीखने वालों से मिलें | [हमारे Discord से जुड़ें](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. समस्या समाधान

| लक्षण                                    | समाधान                                                            |
|-------------------------------------------|-------------------------------------------------------------------|
| `python not found`                        | Python को PATH में जोड़ें या इंस्टॉल के बाद टर्मिनल रीओपन करें    |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` फिर ट्राई करें।      |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` चलाएं (env इंस्टॉल नहीं हुआ)।   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → डिस्क साइज बढ़ाएं।    |
| VS Code बार-बार रीओपन प्रॉम्प्ट करता है   | शायद दोनों ऑप्शन एक्टिव हैं; एक चुनें (venv **या** container)     |
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` वैल्यू / रिक्वेस्ट रेट लिमिट्स चेक करें।         |
| Conda इस्तेमाल करते समय errors            | Microsft AI लाइब्रेरी `conda install -c microsoft azure-ai-ml` से इंस्टॉल करें|

---

**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।