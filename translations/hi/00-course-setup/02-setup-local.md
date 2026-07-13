# स्थानीय सेटअप 🖥️

**इस गाइड का उपयोग करें यदि आप सब कुछ अपने स्वयं के लैपटॉप पर चलाना पसंद करते हैं।**  
आपके पास दो विकल्प हैं: **(A) नेटिव पायथन + वर्चुअल-एन्व** या **(B) डॉकर के साथ VS कोड डेव कंटेनर**।  
जो भी आसान लगे चुनें — दोनों से वही लेसन मिलेंगे।

## 1. पूर्व आवश्यकताएँ

| उपकरण               | संस्करण / नोट्स                                                                         |
|--------------------|--------------------------------------------------------------------------------------|
| **पायथन**           | 3.10+ (इसे <https://python.org> से प्राप्त करें)                                       |
| **गिट**             | नवीनतम (Xcode / Git for Windows / Linux पैकेज मैनेजर के साथ आता है)                   |
| **VS कोड**          | वैकल्पिक लेकिन अनुशंसित <https://code.visualstudio.com>                              |
| **डॉकर डेस्कटॉप**   | *केवल* विकल्प B के लिए। मुफ्त इंस्टालेशन: <https://docs.docker.com/desktop/>         |

> 💡 **टिप** – टर्मिनल में टूल्स की जाँच करें:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. विकल्प A – नेटिव पायथन (सबसे तेज)

### चरण 1 इस रिपो को क्लोन करें

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### चरण 2 एक वर्चुअल एन्वायरनमेंट बनाएं और सक्रिय करें

```bash
python -m venv .venv          # एक बनाएं
source .venv/bin/activate     # macOS / लिनक्स
.\.venv\Scripts\activate      # विंडोज पावरशेल
```

✅ प्रॉम्प्ट अब (.venv) से शुरू होना चाहिए — मतलब आप एन्व के अंदर हैं।

### चरण 3 निर्भरता इंस्टॉल करें

```bash
pip install -r requirements.txt
```

[API keys](#3-अपनी-api-कुंजी-जोड़ें) अनुभाग 3 पर जाएं

## 2. विकल्प B – VS कोड डेव कंटेनर (डॉकर)

हमने इस रिपॉजिटरी और कोर्स को इस तरह सेटअप किया है कि इसमें [डेवलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) शामिल है जो Python3, .NET, Node.js और Java डेवलपमेंट का यूनिवर्सल रनटाइम सपोर्ट करता है। संबंधित कॉन्फ़िगरेशन `devcontainer.json` फाइल में परिभाषित है जो इस रिपॉजिटरी की जड़ों में `.devcontainer/` फोल्डर में स्थित है।

>**क्यों इसे चुनें?**
>Codespaces के समान पर्यावरण; कोई डिपेंडेंसी ड्रिफ्ट नहीं।

### चरण 0 अतिरिक्त चीजें इंस्टॉल करें

डॉकर डेस्कटॉप – पुष्टि करें कि ```docker --version``` काम करता हो।
VS कोड रिमोट – कंटेनर्स एक्सटेंशन (ID: ms-vscode-remote.remote-containers)।

### चरण 1 VS कोड में रिपो खोलें

File ▸ Open Folder… → generative-ai-for-beginners

VS कोड .devcontainer/ को पहचानता है और प्रॉम्प्ट दिखाता है।

### चरण 2 कंटेनर में पुनः खोलें

“Reopen in Container” पर क्लिक करें। डॉकर इमेज बनाता है (पहली बार लगभग 3 मिनट)।  
जब टर्मिनल प्रॉम्प्ट दिखे, आप कंटेनर के अंदर हैं।

## 2. विकल्प C – मिनिकोंडा

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) एक हल्का इंस्टॉलर है जो [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), पायथन, और कुछ पैकेज इंस्टॉल करता है।  
Conda एक पैकेज मैनेजर है, जो विभिन्न पायथन [**वर्चुअल एन्वायरनमेंट्स**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) और पैकेजेस को सेटअप और स्विच करना आसान बनाता है। इसके अलावा ये उन पैकेजों को इंस्टॉल करने में भी मदद करता है जो `pip` से नहीं मिलते।

### चरण 0 मिनिकोंडा इंस्टॉल करें

[MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) का अनुसरण करें।

```bash
conda --version
```

### चरण 1 एक वर्चुअल एन्वायरनमेंट बनाएं

एक नई एन्वायरनमेंट फाइल (*environment.yml*) बनाएं। यदि आप Codespaces का उपयोग कर रहे हैं, तो इसे `.devcontainer` डायरेक्टरी के अंदर बनाएं, जैसे `.devcontainer/environment.yml`।

### चरण 2 अपनी एन्वायरनमेंट फाइल भरें

अपनी `environment.yml` में निम्न कट एन्ड पेस्ट करें

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

### चरण 3 अपना Conda एन्वायरनमेंट बनाएं

नीच के कमांड लाइन/टर्मिनल में चलाएं

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer सब पाथ केवल Codespace सेटअप्स पर लागू होता है
conda activate ai4beg
```

अगर समस्या आए तो [Conda एन्वायर्नमेंट गाइड](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) देखें।

## 2 विकल्प D – क्लासिक जुपिटर / जुपिटर लैब (अपने ब्राउज़र में)

> **किसके लिए?**  
> जो लोग क्लासिक जुपिटर इंटरफेस पसंद करते हैं या बिना VS कोड के नोटबुक चलाना चाहते हैं।  

### चरण 1 सुनिश्चित करें कि जुपिटर इंस्टॉल है

लोकल में जुपिटर स्टार्ट करने के लिए टर्मिनल/कमांड लाइन खोलें, कोर्स डायरेक्टरी में जाएं, और निष्पादित करें:

```bash
jupyter notebook
```

या

```bash
jupyterhub
```

इससे जुपिटर इंस्टेंस शुरू होगा और URL जिसे एक्सेस करना है, कमांड लाइन विंडो में दिखेगा।

URL एक्सेस करने पर आपको कोर्स की रूपरेखा दिखेगी और आप किसी भी `*.ipynb` फाइल पर जा पाएंगे। जैसे, `08-building-search-applications/python/oai-solution.ipynb`।

## 3. अपनी API कुंजी जोड़ें

अपनी API कुंजियों को सुरक्षित रखना जरूरी है जब आप कोई भी एप्लिकेशन बना रहे हों। हम सलाह देते हैं कि API कुंजियाँ सीधे आपके कोड में स्टोर न करें। ये विवरण सार्वजनिक रिपॉजिटरी में रखने से सुरक्षा जोखिम और बुरे उपयोगकर्ता द्वारा खामियां हो सकती हैं, और अनचाहे खर्चे हो सकते हैं।
यहाँ एक स्टेप-बाय-स्टेप गाइड है कि कैसे एक `.env` फाइल बनाएं पायथन के लिए और Microsoft Foundry Models की क्रेडेंशियल्स डालें:

> **नोट:** GitHub Models (और इसका `GITHUB_TOKEN` वेरिएबल) जुलाई 2026 के अंत में बंद हो रहा है। यह गाइड इसके बजाय [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) का उपयोग करता है। पूरी तरह ऑफ़लाइन काम करना चाहते हैं? देखें [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)।

1. **अपने प्रोजेक्ट डायरेक्टरी में जाएं**: टर्मिनल या कमांड प्रॉम्प्ट खोलें और उस प्रोजेक्ट की रूट डायरेक्टरी में जाएं जहाँ आप `.env` फ़ाइल बनाना चाहते हैं।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फ़ाइल बनाएं**: अपनी पसंद के टेक्स्ट एडिटर से एक नया `.env` फ़ाइल बनाएं। कमांड लाइन पर Unix आधारित सिस्टम में `touch` या Windows में `echo` का उपयोग कर सकते हैं:

   Unix आधारित सिस्टम:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फ़ाइल को संपादित करें**: `.env` फ़ाइल को टेक्स्ट एडिटर (जैसे VS कोड, नोटपैड++, या कोई अन्य संपादक) में खोलें। निम्न पंक्तियाँ जोड़ें, प्लेसहोल्डर्स की जगह अपने वास्तविक Microsoft Foundry प्रोजेक्ट एंडपॉइंट और API की डालें:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फ़ाइल सेव करें**: परिवर्तनों को सेव करें और टेक्स्ट एडिटर बंद करें।

5. **`python-dotenv` इंस्टॉल करें**: यदि पहले से नहीं किया है, तो आपको `python-dotenv` पैकेज इंस्टॉल करना होगा ताकि `.env` फ़ाइल से पर्यावरण वेरिएबल्स आपके पायथन ऐप्लिकेशन में लोड हो सकें। इसे `pip` से इंस्टॉल करें:

   ```bash
   pip install python-dotenv
   ```

6. **अपने पायथन स्क्रिप्ट में ENV वेरिएबल्स लोड करें**: अपने पायथन स्क्रिप्ट में `python-dotenv` का उपयोग करें ताकि `.env` फ़ाइल से एन्वायर्नमेंट वेरिएबल्स लोड हो जाएं:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फ़ाइल से पर्यावरण चर लोड करें
   load_dotenv()

   # Microsoft Foundry मॉडल्स चर तक पहुँचें
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

बस! आपने सफलतापूर्वक `.env` फ़ाइल बनाई, अपनी Microsoft Foundry Models क्रेडेंशियल्स जोड़ी, और उन्हें अपने पायथन ऐप्लिकेशन में लोड किया।

🔐 कभी भी .env कमिट न करें—यह पहले से ही .gitignore में है।
पूर्ण प्रदाता निर्देश [`providers.md`](03-providers.md) में उपलब्ध हैं।

## 4. अगला क्या?

| मैं क्या करना चाहता हूँ… | जाएं…                                                                   |
|------------------------|-------------------------------------------------------------------------|
| लेसन 1 शुरू करें      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| एक LLM प्रदाता सेटअप करें | [`providers.md`](03-providers.md)                                        |
| अन्य शिक्षार्थियों से मिलें | [हमारा डिसकॉर्ड जॉइन करें](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. समस्या निवारण

| लक्षण                                       | समाधान                                                             |
|--------------------------------------------|-------------------------------------------------------------------|
| `python not found`                         | इंस्टॉल के बाद पायथन को PATH में जोड़ें या टर्मिनल फिर से खोलें    |
| `pip` विंडोज़ पर व्हील्स बिल्ड नहीं कर पाता | `pip install --upgrade pip setuptools wheel` करें फिर पुनः प्रयास करें। |
| `ModuleNotFoundError: dotenv`               | `pip install -r requirements.txt` चलाएं (एन्व इंस्टॉल नहीं था)।   |
| डॉकर बिल्ड फेल होता है *No space left*     | Docker Desktop ▸ *Settings* ▸ *Resources* → डिस्क साइज बढ़ाएं।   |
| VS कोड बार-बार पुनः खोलने का अनुरोध करता है | आपके पास दोनों विकल्प सक्रिय हो सकते हैं; एक चुनें (venv **या** कंटेनर) |
| OpenAI 401 / 429 त्रुटियाँ                   | `OPENAI_API_KEY` मान जांचें / अनुरोध दर सीमाएँ देखें।             |
| Conda का उपयोग करते समय त्रुटियाँ            | Microsoft AI लाइब्रेरी `conda install -c microsoft azure-ai-ml` से इंस्टॉल करें।|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->