<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:56:33+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hi"
}
-->
# AGENTS.md

## परियोजना का अवलोकन

यह रिपॉजिटरी 21 पाठों का एक व्यापक पाठ्यक्रम प्रदान करती है, जो जनरेटिव AI की मूलभूत बातें और एप्लिकेशन विकास सिखाती है। यह कोर्स शुरुआती लोगों के लिए डिज़ाइन किया गया है और इसमें बुनियादी अवधारणाओं से लेकर प्रोडक्शन-रेडी एप्लिकेशन बनाने तक सब कुछ शामिल है।

**मुख्य तकनीकें:**
- Python 3.9+ और लाइब्रेरीज़: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript और Node.js के साथ लाइब्रेरीज़: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, और GitHub Models
- इंटरैक्टिव लर्निंग के लिए Jupyter Notebooks
- स्थिर विकास वातावरण के लिए Dev Containers

**रिपॉजिटरी संरचना:**
- 21 क्रमांकित पाठ निर्देशिकाएँ (00-21) जिनमें README, कोड उदाहरण और असाइनमेंट शामिल हैं
- कई कार्यान्वयन: Python, TypeScript, और कभी-कभी .NET उदाहरण
- 40+ भाषाओं के संस्करणों के साथ अनुवाद निर्देशिका
- केंद्रीकृत कॉन्फ़िगरेशन `.env` फ़ाइल के माध्यम से (टेम्पलेट के रूप में `.env.copy` का उपयोग करें)

## सेटअप कमांड्स

### प्रारंभिक रिपॉजिटरी सेटअप

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python पर्यावरण सेटअप

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript सेटअप

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container सेटअप (अनुशंसित)

रिपॉजिटरी में GitHub Codespaces या VS Code Dev Containers के लिए `.devcontainer` कॉन्फ़िगरेशन शामिल है:

1. रिपॉजिटरी को GitHub Codespaces या VS Code में Dev Containers एक्सटेंशन के साथ खोलें
2. Dev Container स्वचालित रूप से:
   - `requirements.txt` से Python निर्भरताएँ इंस्टॉल करेगा
   - पोस्ट-क्रिएट स्क्रिप्ट (`.devcontainer/post-create.sh`) चलाएगा
   - Jupyter kernel सेटअप करेगा

## विकास कार्यप्रवाह

### पर्यावरण वेरिएबल्स

API एक्सेस की आवश्यकता वाले सभी पाठ `.env` में परिभाषित पर्यावरण वेरिएबल्स का उपयोग करते हैं:

- `OPENAI_API_KEY` - OpenAI API के लिए
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service के लिए
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - चैट कंप्लीशन मॉडल का डिप्लॉयमेंट नाम
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - एम्बेडिंग्स मॉडल का डिप्लॉयमेंट नाम
- `AZURE_OPENAI_API_VERSION` - API संस्करण (डिफ़ॉल्ट: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face मॉडल्स के लिए
- `GITHUB_TOKEN` - GitHub Models के लिए

### Python उदाहरण चलाना

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript उदाहरण चलाना

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks चलाना

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### विभिन्न प्रकार के पाठों के साथ काम करना

- **"Learn" पाठ**: README.md दस्तावेज़ और अवधारणाओं पर केंद्रित
- **"Build" पाठ**: Python और TypeScript में कार्यशील कोड उदाहरण शामिल हैं
- प्रत्येक पाठ में README.md होता है जिसमें सिद्धांत, कोड वॉकथ्रू और वीडियो सामग्री के लिंक होते हैं

## कोड शैली दिशानिर्देश

### Python

- पर्यावरण वेरिएबल प्रबंधन के लिए `python-dotenv` का उपयोग करें
- API इंटरैक्शन के लिए `openai` लाइब्रेरी आयात करें
- लिंटिंग के लिए `pylint` का उपयोग करें (कुछ उदाहरणों में सादगी के लिए `# pylint: disable=all` शामिल है)
- PEP 8 नामकरण सम्मेलनों का पालन करें
- API क्रेडेंशियल्स को `.env` फ़ाइल में संग्रहीत करें, कोड में कभी नहीं

### TypeScript

- पर्यावरण वेरिएबल्स के लिए `dotenv` पैकेज का उपयोग करें
- प्रत्येक ऐप के लिए `tsconfig.json` में TypeScript कॉन्फ़िगरेशन
- Azure सेवाओं के लिए `@azure/openai` या `@azure-rest/ai-inference` का उपयोग करें
- ऑटो-रिलोड के साथ विकास के लिए `nodemon` का उपयोग करें
- चलाने से पहले निर्माण करें: `npm run build` फिर `npm start`

### सामान्य सम्मेलन

- कोड उदाहरणों को सरल और शैक्षिक रखें
- प्रमुख अवधारणाओं को समझाने वाले टिप्पणियाँ शामिल करें
- प्रत्येक पाठ का कोड आत्मनिर्भर और चलने योग्य होना चाहिए
- सुसंगत नामकरण का उपयोग करें: Azure OpenAI के लिए `aoai-` उपसर्ग, OpenAI API के लिए `oai-`, GitHub Models के लिए `githubmodels-`

## दस्तावेज़ीकरण दिशानिर्देश

### Markdown शैली

- सभी URLs को `[text](../../url)` प्रारूप में लपेटा जाना चाहिए, बिना अतिरिक्त स्पेस के
- सापेक्ष लिंक `./` या `../` से शुरू होने चाहिए
- Microsoft डोमेन के सभी लिंक में ट्रैकिंग ID शामिल होनी चाहिए: `?WT.mc_id=academic-105485-koreyst`
- URLs में देश-विशिष्ट लोकेल नहीं होना चाहिए (जैसे `/en-us/` से बचें)
- छवियाँ `./images` फ़ोल्डर में वर्णनात्मक नामों के साथ संग्रहीत की जानी चाहिए
- फ़ाइल नामों में अंग्रेजी वर्ण, संख्याएँ, और डैश का उपयोग करें

### अनुवाद समर्थन

- रिपॉजिटरी GitHub Actions के माध्यम से 40+ भाषाओं का समर्थन करती है
- अनुवाद `translations/` निर्देशिका में संग्रहीत हैं
- आंशिक अनुवाद सबमिट न करें
- मशीन अनुवाद स्वीकार नहीं किए जाते
- अनुवादित छवियाँ `translated_images/` निर्देशिका में संग्रहीत की जाती हैं

## परीक्षण और मान्यता

### प्री-सबमिशन चेक्स

यह रिपॉजिटरी GitHub Actions का उपयोग मान्यता के लिए करती है। PR सबमिट करने से पहले:

1. **Markdown लिंक जांचें**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **मैनुअल परीक्षण**:
   - Python उदाहरणों का परीक्षण करें: venv सक्रिय करें और स्क्रिप्ट चलाएँ
   - TypeScript उदाहरणों का परीक्षण करें: `npm install`, `npm run build`, `npm start`
   - सुनिश्चित करें कि पर्यावरण वेरिएबल्स सही तरीके से कॉन्फ़िगर किए गए हैं
   - API कुंजियाँ कोड उदाहरणों के साथ काम करती हैं, यह जांचें

3. **कोड उदाहरण**:
   - सुनिश्चित करें कि सभी कोड त्रुटियों के बिना चलते हैं
   - Azure OpenAI और OpenAI API दोनों के साथ परीक्षण करें जहाँ लागू हो
   - GitHub Models के साथ समर्थित उदाहरणों का परीक्षण करें

### कोई स्वचालित परीक्षण नहीं

यह एक शैक्षिक रिपॉजिटरी है जो ट्यूटोरियल और उदाहरणों पर केंद्रित है। चलाने के लिए कोई यूनिट टेस्ट या इंटीग्रेशन टेस्ट नहीं हैं। मान्यता मुख्य रूप से:
- कोड उदाहरणों का मैनुअल परीक्षण
- Markdown मान्यता के लिए GitHub Actions
- शैक्षिक सामग्री की सामुदायिक समीक्षा

## पुल अनुरोध दिशानिर्देश

### सबमिट करने से पहले

1. Python और TypeScript दोनों में कोड परिवर्तनों का परीक्षण करें जहाँ लागू हो
2. Markdown मान्यता चलाएँ (PR पर स्वचालित रूप से ट्रिगर होती है)
3. सुनिश्चित करें कि Microsoft URLs पर ट्रैकिंग IDs मौजूद हैं
4. जांचें कि सापेक्ष लिंक मान्य हैं
5. सुनिश्चित करें कि छवियाँ सही तरीके से संदर्भित हैं

### PR शीर्षक प्रारूप

- वर्णनात्मक शीर्षक का उपयोग करें: `[Lesson 06] Fix Python example typo` या `Update README for lesson 08`
- लागू होने पर मुद्दा संख्या का संदर्भ दें: `Fixes #123`

### PR विवरण

- क्या बदला और क्यों, यह समझाएँ
- संबंधित मुद्दों के लिंक प्रदान करें
- कोड परिवर्तनों के लिए, यह निर्दिष्ट करें कि कौन से उदाहरणों का परीक्षण किया गया
- अनुवाद PRs के लिए, सभी फ़ाइलों को पूर्ण अनुवाद के लिए शामिल करें

### योगदान आवश्यकताएँ

- Microsoft CLA पर हस्ताक्षर करें (पहले PR पर स्वचालित)
- रिपॉजिटरी को अपने खाते में फोर्क करें और फिर परिवर्तन करें
- प्रत्येक तार्किक परिवर्तन के लिए एक PR (असंबंधित सुधारों को संयोजित न करें)
- PRs को केंद्रित और छोटा रखें जहाँ संभव हो

## सामान्य कार्यप्रवाह

### नया कोड उदाहरण जोड़ना

1. उपयुक्त पाठ निर्देशिका पर जाएँ
2. `python/` या `typescript/` उपनिर्देशिका में उदाहरण बनाएँ
3. नामकरण सम्मेलन का पालन करें: `{provider}-{example-name}.{py|ts|js}`
4. वास्तविक API क्रेडेंशियल्स के साथ परीक्षण करें
5. पाठ README में किसी भी नए पर्यावरण वेरिएबल्स का दस्तावेज़ीकरण करें

### दस्तावेज़ीकरण अपडेट करना

1. पाठ निर्देशिका में README.md संपादित करें
2. Markdown दिशानिर्देशों का पालन करें (ट्रैकिंग IDs, सापेक्ष लिंक)
3. अनुवाद GitHub Actions द्वारा संभाले जाते हैं (मैन्युअल रूप से संपादित न करें)
4. सभी लिंक मान्य हैं, यह परीक्षण करें

### Dev Containers के साथ काम करना

1. रिपॉजिटरी में `.devcontainer/devcontainer.json` शामिल है
2. पोस्ट-क्रिएट स्क्रिप्ट स्वचालित रूप से Python निर्भरताएँ इंस्टॉल करता है
3. Python और Jupyter के लिए एक्सटेंशन पहले से कॉन्फ़िगर हैं
4. वातावरण `mcr.microsoft.com/devcontainers/universal:2.11.2` पर आधारित है

## परिनियोजन और प्रकाशन

यह एक शिक्षण रिपॉजिटरी है - कोई परिनियोजन प्रक्रिया नहीं है। पाठ्यक्रम का उपयोग निम्नलिखित तरीकों से किया जाता है:

1. **GitHub रिपॉजिटरी**: कोड और दस्तावेज़ीकरण तक सीधा पहुँच
2. **GitHub Codespaces**: प्री-कॉन्फ़िगर सेटअप के साथ इंस्टेंट डेवलपमेंट वातावरण
3. **Microsoft Learn**: सामग्री आधिकारिक शिक्षण प्लेटफ़ॉर्म पर सिंडिकेट की जा सकती है
4. **docsify**: Markdown से निर्मित दस्तावेज़ीकरण साइट (देखें `docsifytopdf.js` और `package.json`)

### दस्तावेज़ीकरण साइट बनाना

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## समस्या निवारण

### सामान्य समस्याएँ

**Python आयात त्रुटियाँ**:
- सुनिश्चित करें कि वर्चुअल वातावरण सक्रिय है
- `pip install -r requirements.txt` चलाएँ
- Python संस्करण 3.9+ है, यह जांचें

**TypeScript निर्माण त्रुटियाँ**:
- विशिष्ट ऐप निर्देशिका में `npm install` चलाएँ
- Node.js संस्करण संगत है, यह जांचें
- यदि आवश्यक हो तो `node_modules` साफ़ करें और पुनः इंस्टॉल करें

**API प्रमाणीकरण त्रुटियाँ**:
- सुनिश्चित करें कि `.env` फ़ाइल मौजूद है और सही मान हैं
- API कुंजियाँ मान्य हैं और समाप्त नहीं हुई हैं, यह जांचें
- सुनिश्चित करें कि आपके क्षेत्र के लिए endpoint URLs सही हैं

**पर्यावरण वेरिएबल्स गायब हैं**:
- `.env.copy` को `.env` में कॉपी करें
- उस पाठ के लिए सभी आवश्यक मान भरें जिस पर आप काम कर रहे हैं
- `.env` अपडेट करने के बाद अपना एप्लिकेशन पुनः प्रारंभ करें

## अतिरिक्त संसाधन

- [कोर्स सेटअप गाइड](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [योगदान दिशानिर्देश](./CONTRIBUTING.md)
- [आचार संहिता](./CODE_OF_CONDUCT.md)
- [सुरक्षा नीति](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [उन्नत कोड नमूनों का संग्रह](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## परियोजना-विशिष्ट नोट्स

- यह एक **शैक्षिक रिपॉजिटरी** है जो सीखने पर केंद्रित है, प्रोडक्शन कोड पर नहीं
- उदाहरण जानबूझकर सरल और अवधारणाओं को सिखाने पर केंद्रित हैं
- कोड गुणवत्ता को शैक्षिक स्पष्टता के साथ संतुलित किया गया है
- प्रत्येक पाठ आत्मनिर्भर है और स्वतंत्र रूप से पूरा किया जा सकता है
- रिपॉजिटरी कई API प्रदाताओं का समर्थन करती है: Azure OpenAI, OpenAI, और GitHub Models
- सामग्री बहुभाषी है और स्वचालित अनुवाद वर्कफ़्लो के साथ है
- प्रश्नों और समर्थन के लिए Discord पर सक्रिय समुदाय

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।