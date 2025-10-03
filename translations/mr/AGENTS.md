<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:57:57+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mr"
}
-->
# AGENTS.md

## प्रकल्पाचा आढावा

हे रिपॉझिटरी जनरेटिव्ह AI च्या मूलभूत गोष्टी आणि अनुप्रयोग विकास शिकवणाऱ्या 21-धड्यांच्या अभ्यासक्रमाचा समावेश करते. हा कोर्स नवशिक्यांसाठी तयार करण्यात आला आहे आणि मूलभूत संकल्पनांपासून उत्पादन-तयार अनुप्रयोग तयार करण्यापर्यंत सर्वकाही समाविष्ट करतो.

**मुख्य तंत्रज्ञान:**
- Python 3.9+ आणि लायब्ररी: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript आणि Node.js लायब्ररी: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, आणि GitHub Models
- इंटरॅक्टिव्ह शिक्षणासाठी Jupyter Notebooks
- सुसंगत विकास वातावरणासाठी Dev Containers

**रिपॉझिटरीची रचना:**
- 21 क्रमांकित धड्यांचे डिरेक्टरी (00-21) ज्यामध्ये README, कोड उदाहरणे आणि असाइनमेंट्स आहेत
- अनेक अंमलबजावणी: Python, TypeScript, आणि कधी कधी .NET उदाहरणे
- 40+ भाषांमध्ये अनुवादांसाठी डिरेक्टरी
- `.env` फाइलद्वारे केंद्रीकृत कॉन्फिगरेशन (`.env.copy` टेम्पलेट म्हणून वापरा)

## सेटअप कमांड्स

### प्रारंभिक रिपॉझिटरी सेटअप

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

### Dev Container सेटअप (शिफारस केलेले)

रिपॉझिटरीमध्ये GitHub Codespaces किंवा VS Code Dev Containers साठी `.devcontainer` कॉन्फिगरेशन समाविष्ट आहे:

1. GitHub Codespaces किंवा Dev Containers एक्स्टेंशनसह VS Code मध्ये रिपॉझिटरी उघडा
2. Dev Container आपोआप:
   - `requirements.txt` मधून Python dependencies इंस्टॉल करेल
   - पोस्ट-क्रिएट स्क्रिप्ट (`.devcontainer/post-create.sh`) चालवेल
   - Jupyter kernel सेटअप करेल

## विकास कार्यप्रवाह

### पर्यावरणीय व्हेरिएबल्स

API ऍक्सेस आवश्यक असलेल्या सर्व धड्यांमध्ये `.env` मध्ये परिभाषित पर्यावरणीय व्हेरिएबल्स वापरल्या जातात:

- `OPENAI_API_KEY` - OpenAI API साठी
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service साठी
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion मॉडेल डिप्लॉयमेंटचे नाव
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings मॉडेल डिप्लॉयमेंटचे नाव
- `AZURE_OPENAI_API_VERSION` - API आवृत्ती (डिफॉल्ट: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face मॉडेल्ससाठी
- `GITHUB_TOKEN` - GitHub Models साठी

### Python उदाहरणे चालवणे

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript उदाहरणे चालवणे

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks चालवणे

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### विविध प्रकारच्या धड्यांसोबत काम करणे

- **"Learn" धडे**: README.md दस्तऐवज आणि संकल्पनांवर लक्ष केंद्रित
- **"Build" धडे**: Python आणि TypeScript मध्ये कार्यरत कोड उदाहरणे समाविष्ट
- प्रत्येक धड्याचा README.md मध्ये सिद्धांत, कोड वॉकथ्रू आणि व्हिडिओ सामग्रीसाठी दुवे असतात

## कोड शैली मार्गदर्शक तत्त्वे

### Python

- पर्यावरणीय व्हेरिएबल्स व्यवस्थापनासाठी `python-dotenv` वापरा
- API संवादांसाठी `openai` लायब्ररी आयात करा
- लिंटिंगसाठी `pylint` वापरा (काही उदाहरणांमध्ये सोपेपणासाठी `# pylint: disable=all` समाविष्ट आहे)
- PEP 8 नामकरण नियमांचे पालन करा
- API क्रेडेन्शियल्स कोडमध्ये कधीही संग्रहित करू नका, फक्त `.env` फाइलमध्ये ठेवा

### TypeScript

- पर्यावरणीय व्हेरिएबल्ससाठी `dotenv` पॅकेज वापरा
- प्रत्येक ऍपसाठी `tsconfig.json` मध्ये TypeScript कॉन्फिगरेशन
- Azure सेवांसाठी `@azure/openai` किंवा `@azure-rest/ai-inference` वापरा
- ऑटो-रिलोडसाठी `nodemon` वापरा
- चालवण्यापूर्वी बिल्ड करा: `npm run build` नंतर `npm start`

### सामान्य परंपरा

- कोड उदाहरणे सोपी आणि शैक्षणिक ठेवा
- मुख्य संकल्पना स्पष्ट करणारे टिप्पण्या समाविष्ट करा
- प्रत्येक धड्याचा कोड स्वतंत्र आणि चालवण्यायोग्य असावा
- सुसंगत नामकरण वापरा: Azure OpenAI साठी `aoai-`, OpenAI API साठी `oai-`, GitHub Models साठी `githubmodels-`

## दस्तऐवज मार्गदर्शक तत्त्वे

### Markdown शैली

- सर्व URLs `[text](../../url)` स्वरूपात असावेत, अतिरिक्त जागा नसावी
- सापेक्ष दुवे `./` किंवा `../` ने सुरू व्हावेत
- Microsoft डोमेनवरील सर्व दुव्यांमध्ये ट्रॅकिंग ID समाविष्ट असावा: `?WT.mc_id=academic-105485-koreyst`
- URLs मध्ये देश-विशिष्ट स्थानिक भाषा नसावी (उदा. `/en-us/` टाळा)
- प्रतिमा `./images` फोल्डरमध्ये वर्णनात्मक नावांसह संग्रहित करा
- फाइल नावांमध्ये इंग्रजी अक्षरे, संख्या, आणि डॅशेस वापरा

### अनुवाद समर्थन

- रिपॉझिटरी GitHub Actions च्या माध्यमातून 40+ भाषांना समर्थन देते
- अनुवाद `translations/` डिरेक्टरीमध्ये संग्रहित
- अपूर्ण अनुवाद सबमिट करू नका
- मशीन अनुवाद स्वीकारले जात नाहीत
- अनुवादित प्रतिमा `translated_images/` डिरेक्टरीमध्ये संग्रहित

## चाचणी आणि पडताळणी

### प्री-सबमिशन तपासणी

हे रिपॉझिटरी GitHub Actions चा वापर करून पडताळणी करते. PR सबमिट करण्यापूर्वी:

1. **Markdown दुवे तपासा**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **मॅन्युअल चाचणी**:
   - Python उदाहरणे तपासा: venv सक्रिय करा आणि स्क्रिप्ट चालवा
   - TypeScript उदाहरणे तपासा: `npm install`, `npm run build`, `npm start`
   - पर्यावरणीय व्हेरिएबल्स योग्यरित्या कॉन्फिगर केले आहेत याची खात्री करा
   - API की कोड उदाहरणांसह कार्यरत आहेत याची खात्री करा

3. **कोड उदाहरणे**:
   - सर्व कोड त्रुटीशिवाय चालतो याची खात्री करा
   - Azure OpenAI आणि OpenAI API सह चाचणी करा (लागू असल्यास)
   - GitHub Models सह उदाहरणे कार्यरत आहेत याची खात्री करा

### स्वयंचलित चाचण्या नाहीत

हे शैक्षणिक रिपॉझिटरी आहे जे ट्यूटोरियल्स आणि उदाहरणांवर लक्ष केंद्रित करते. चालवण्यासाठी कोणत्याही युनिट चाचण्या किंवा इंटिग्रेशन चाचण्या नाहीत. पडताळणी प्रामुख्याने:
- कोड उदाहरणांची मॅन्युअल चाचणी
- Markdown पडताळणीसाठी GitHub Actions
- शैक्षणिक सामग्रीचे समुदाय पुनरावलोकन

## पुल रिक्वेस्ट मार्गदर्शक तत्त्वे

### सबमिट करण्यापूर्वी

1. Python आणि TypeScript मध्ये कोड बदल चाचणी करा (लागू असल्यास)
2. Markdown पडताळणी चालवा (PR वर स्वयंचलितपणे ट्रिगर होते)
3. Microsoft URLs वर ट्रॅकिंग IDs आहेत याची खात्री करा
4. सापेक्ष दुवे वैध आहेत याची खात्री करा
5. प्रतिमा योग्यरित्या संदर्भित आहेत याची पडताळणी करा

### PR शीर्षक स्वरूप

- वर्णनात्मक शीर्षके वापरा: `[Lesson 06] Fix Python example typo` किंवा `Update README for lesson 08`
- लागू असल्यास समस्या क्रमांक संदर्भित करा: `Fixes #123`

### PR वर्णन

- काय बदलले आणि का ते स्पष्ट करा
- संबंधित समस्यांशी दुवा जोडा
- कोड बदलांसाठी, कोणती उदाहरणे चाचणी केली ते निर्दिष्ट करा
- अनुवाद PR साठी, संपूर्ण अनुवादासाठी सर्व फाइल्स समाविष्ट करा

### योगदान आवश्यकता

- Microsoft CLA साइन करा (पहिल्या PR वर स्वयंचलित)
- बदल करण्यापूर्वी रिपॉझिटरी आपल्या खात्यावर फोर्क करा
- प्रत्येक लॉजिकल बदलासाठी एक PR (असंबंधित दुरुस्त्या एकत्र करू नका)
- PRs लक्ष केंद्रित आणि शक्य तितक्या लहान ठेवा

## सामान्य कार्यप्रवाह

### नवीन कोड उदाहरण जोडणे

1. संबंधित धड्याच्या डिरेक्टरीमध्ये जा
2. `python/` किंवा `typescript/` सबडिरेक्टरीमध्ये उदाहरण तयार करा
3. नामकरण परंपरा पाळा: `{provider}-{example-name}.{py|ts|js}`
4. वास्तविक API क्रेडेन्शियल्ससह चाचणी करा
5. धड्याच्या README मध्ये कोणतेही नवीन पर्यावरणीय व्हेरिएबल्स दस्तऐवजीकरण करा

### दस्तऐवज अद्यतनित करणे

1. धड्याच्या डिरेक्टरीमध्ये README.md संपादित करा
2. Markdown मार्गदर्शक तत्त्वांचे पालन करा (ट्रॅकिंग IDs, सापेक्ष दुवे)
3. अनुवाद GitHub Actions द्वारे हाताळले जातात (मॅन्युअली संपादित करू नका)
4. सर्व दुवे वैध आहेत याची चाचणी करा

### Dev Containers सोबत काम करणे

1. रिपॉझिटरीमध्ये `.devcontainer/devcontainer.json` समाविष्ट आहे
2. पोस्ट-क्रिएट स्क्रिप्ट आपोआप Python dependencies इंस्टॉल करते
3. Python आणि Jupyter साठी एक्स्टेंशन्स पूर्व-कॉन्फिगर केलेले आहेत
4. पर्यावरण `mcr.microsoft.com/devcontainers/universal:2.11.2` वर आधारित आहे

## डिप्लॉयमेंट आणि प्रकाशन

हे एक शिक्षण रिपॉझिटरी आहे - येथे कोणतीही डिप्लॉयमेंट प्रक्रिया नाही. अभ्यासक्रमाचा वापर खालील प्रकारे केला जातो:

1. **GitHub रिपॉझिटरी**: कोड आणि दस्तऐवज थेट ऍक्सेस
2. **GitHub Codespaces**: प्री-कॉन्फिगर सेटअपसह त्वरित विकास वातावरण
3. **Microsoft Learn**: अधिकृत शिक्षण प्लॅटफॉर्मवर सामग्री सिंडिकेट केली जाऊ शकते
4. **docsify**: Markdown वरून तयार केलेली दस्तऐवज साइट (`docsifytopdf.js` आणि `package.json` पहा)

### दस्तऐवज साइट तयार करणे

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## समस्या सोडवणे

### सामान्य समस्या

**Python आयात त्रुटी**:
- व्हर्च्युअल पर्यावरण सक्रिय आहे याची खात्री करा
- `pip install -r requirements.txt` चालवा
- Python आवृत्ती 3.9+ आहे याची खात्री करा

**TypeScript बिल्ड त्रुटी**:
- विशिष्ट ऍप डिरेक्टरीमध्ये `npm install` चालवा
- Node.js आवृत्ती सुसंगत आहे याची खात्री करा
- `node_modules` क्लिअर करा आणि पुन्हा इंस्टॉल करा

**API प्रमाणीकरण त्रुटी**:
- `.env` फाइल अस्तित्वात आहे आणि योग्य मूल्ये आहेत याची खात्री करा
- API की वैध आहेत आणि कालबाह्य नाहीत याची खात्री करा
- आपल्या प्रदेशासाठी endpoint URLs योग्य आहेत याची खात्री करा

**हरवलेले पर्यावरणीय व्हेरिएबल्स**:
- `.env.copy` `.env` मध्ये कॉपी करा
- आपण काम करत असलेल्या धड्यासाठी सर्व आवश्यक मूल्ये भरा
- `.env` अपडेट केल्यानंतर आपला अनुप्रयोग पुन्हा सुरू करा

## अतिरिक्त संसाधने

- [कोर्स सेटअप मार्गदर्शक](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [योगदान मार्गदर्शक तत्त्वे](./CONTRIBUTING.md)
- [आचारसंहिता](./CODE_OF_CONDUCT.md)
- [सुरक्षा धोरण](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [प्रगत कोड नमुन्यांचा संग्रह](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## प्रकल्प-विशिष्ट टिप्पण्या

- हे एक **शैक्षणिक रिपॉझिटरी** आहे जे शिक्षणावर लक्ष केंद्रित करते, उत्पादन कोडवर नाही
- उदाहरणे हेतुपुरस्सर सोपी आणि संकल्पना शिकवण्यावर लक्ष केंद्रित केलेली आहेत
- कोड गुणवत्ता शैक्षणिक स्पष्टतेसह संतुलित आहे
- प्रत्येक धडा स्वतंत्र आहे आणि स्वतंत्रपणे पूर्ण केला जाऊ शकतो
- रिपॉझिटरी अनेक API प्रदात्यांना समर्थन देते: Azure OpenAI, OpenAI, आणि GitHub Models
- सामग्री बहुभाषिक आहे आणि स्वयंचलित अनुवाद कार्यप्रवाहांसह आहे
- प्रश्न आणि समर्थनासाठी Discord वर सक्रिय समुदाय

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.