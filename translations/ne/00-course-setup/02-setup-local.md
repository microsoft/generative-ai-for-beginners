# स्थानीय सेटअप 🖥️

**यदि तपाईं सबै कुरा आफ्नो ल्यापटपमा चलाउन चाहानुहुन्छ भने यो मार्गदर्शन प्रयोग गर्नुहोस्।**  
तपाईंका दुई विकल्पहरू छन्: **(A) मूल Python + virtual-env** वा **(B) VS Code Dev Container सँग Docker**।  
जुनसुकै सहज लाग्छ त्यो रोज्नुहोस्—दुबैले एउटै पाठहरूमा लैजानेछ।  

## १. पूर्वआवश्यकताहरू

| उपकरण            | संस्करण / नोट्स                                                                       |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (यसलाई <https://python.org> बाट प्राप्त गर्न सक्नुहुन्छ)                       |
| **Git**            | नवीनतम (Xcode / Git for Windows / Linux प्याकेज म्यानेजरसँग आउँछ)                    |
| **VS Code**        | वैकल्पिक तर सिफारिस गरिएको <https://code.visualstudio.com>                         |
| **Docker Desktop** | विकल्प B का लागि मात्र। निशुल्क स्थापना: <https://docs.docker.com/desktop/>         |

> 💡 **सुजाब** – टर्मिनलमा उपकरणहरू जाँच्नुहोस्:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## २.  विकल्प A – मूल Python (सबैभन्दा छिटो)

### चरण १ यो रिपोजिटरी क्लोन गर्नुहोस्

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### चरण २ भर्चुअल वातावरण सिर्जना र सक्रिय गर्नुहोस्

```bash
python -m venv .venv          # एउटा बनाउनुहोस्
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ प्रॉम्प्ट अब (.venv) बाट सुरु हुनु पर्छ—यसले तपाईं भर्चुअल वातावरण भित्र हुनुहुन्छ भन्ने जनाउँछ।

### चरण ३ निर्भरताहरू स्थापना गर्नुहोस्

```bash
pip install -r requirements.txt
```

[API कुञ्जीहरू](#३-आफ्नो-api-कुञ्जीहरू-थप्नुहोस्) सम्बन्धी भाग ३ मा जानुहोस्

## २. विकल्प B – VS Code Dev Container (Docker)

हामीले यो रिपोजिटरी र पाठ्यक्रम एउटा [डेभलपमेन्ट कन्टेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) सँग सेटअप गरेका छौं जुन Python3, .NET, Node.js र Java विकासलाई समर्थन गर्न सक्ने युनिभर्सल रनटाइम छ। सम्बन्धित कन्फिगरेसन `devcontainer.json` फाइलमा परिभाषित गरिएको छ जुन यस रिपोजिटरीको रुट `.devcontainer/` फोल्डरमा छ।

>**किन यो रोज्ने?**
>Codespaces सँग समान वातावरण; कुनै निर्भरता फरक छैन।

### चरण ० अतिरिक्तहरू स्थापना गर्नुहोस्

Docker Desktop – सुनिश्चित गर्नुहोस् `docker --version` काम गर्छ।
VS Code Remote – Containers एक्सटेन्सन (ID: ms-vscode-remote.remote-containers)।

### चरण १ रिपोजिटरी VS Code मा खोल्नुहोस्

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code ले .devcontainer/ फोल्डर पत्ता लगाएर प्रॉम्प्ट देखाउँछ।

### चरण २ कन्टेनरमा पुनः खोल्नुहोस्

"Reopen in Container" मा क्लिक गर्नुहोस्। Docker ले इमेज बनाउँछ (पहिलो पटक ≈ ३ मिनेट)।  
टर्मिनल प्रॉम्प्ट देखिँदा, तपाईं कन्टेनर भित्र हुनुहुन्छ।

## २. विकल्प C – मिनिकोंडा

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केही प्याकेजहरू स्थापना गर्न हल्का इंस्टलर हो।
Conda आफैं एउटा प्याकेज म्यानेजर हो, जसले विभिन्न Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू बीच सेटअप र सर्न सजिलो बनाउँछ। यसले `pip` मार्फत उपलब्ध नभएका प्याकेजहरू स्थापना गर्न पनि मद्दत गर्छ।

### चरण ० मिनिकोंडा स्थापना गर्नुहोस्

सेटअप गर्न [MiniConda इंस्टलेसन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) अनुशरण गर्नुहोस्।

```bash
conda --version
```

### चरण १ भर्चुअल वातावरण सिर्जना गर्नुहोस्

नयाँ environment फाइल (*environment.yml*) सिर्जना गर्नुहोस्। यदि तपाईं Codespaces प्रयोग गर्दै हुनुहुन्छ भने, `.devcontainer` डिरेक्टरी भित्र, अर्थात् `.devcontainer/environment.yml` मा यो बनाउनुहोस्।

### चरण २ आफ्नो environment फाइल भर्नुहोस्

तलको अंश `environment.yml` मा थप्नुहोस्

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

### चरण ३ आफ्नो Conda वातावरण सिर्जना गर्नुहोस्

तलका कमाण्डहरू तपाईंको कमाण्ड लाइन/टर्मिनलमा चलाउनुहोस्

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer सब पथ केवल Codespace सेटअपहरूमा लागू हुन्छ
conda activate ai4beg
```

कुनै समस्या आएमा [Conda वातावरण मार्गदर्शन](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

## २. विकल्प D – क्लासिक Jupyter / Jupyter Lab (तपाईंको ब्राउजरमा)

> **यो को लागि हो?**  
> क्लासिक Jupyter इन्टरफेस मन पराउने वा VS Code बिना नोटबुक चलाउन चाहनेहरूका लागि।  

### चरण १ Jupyter स्थापना सुनिश्चित गर्नुहोस्

स्थानीय रूपमा Jupyter सुरु गर्न, टर्मिनल/कमाण्ड लाइनमा जानुहोस्, कोर्स डिरेक्टरीमा नेभिगेट गर्नुहोस्, र यो चलाउनुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter इन्स्ट्यान्स सुरु गर्नेछ र पहुँचको URL कमाण्ड लाइन विन्डोमा देखाइनेछ।

URL मा पहुँच गरेपछि, तपाईंले कोर्सको रूपरेखा देख्नु पर्नेछ र कुनै पनि `*.ipynb` फाइलमा जान सक्नुहुन्छ। उदाहरणका लागि, `08-building-search-applications/python/oai-solution.ipynb`।

## ३. आफ्नो API कुञ्जीहरू थप्नुहोस्

तपाईंको API कुञ्जीहरू सुरक्षित राख्नु कुनै पनि प्रकारको अनुप्रयोग निर्माण गर्दा धेरै महत्त्वपूर्ण हुन्छ। हामी सिफारिस गर्छौं कि तपाईँले कुनै पनि API कुञ्जीहरू सिधै आफ्नो कोडमा भण्डारण नगर्नुहोस्। ती विवरणहरू सार्वजनिक रिपोजिटरीमा कमिट गर्दा सुरक्षा समस्या र दुर्भावनापूर्ण प्रयोगकर्ताबाट अनावश्यक खर्च हुन सक्छ।
यहाँ Python को लागि `.env` फाइल कसरी बनाउने र Microsoft Foundry Models क्रेडेन्शियलहरू कसरी थप्ने भन्ने चरण-दर-चरण मार्गदर्शिका छ:

> **सूचना:** GitHub Models (र यसको `GITHUB_TOKEN` भेरिएबल) जुलाई २०२६ अन्त्यमा बन्द हुँदैछ। यो मार्गदर्शनले [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) प्रयोग गरेको छ। पुरै अनलाइन नचाहनुहुन्छ? [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

१. **आफ्नो परियोजना डिरेक्टरीमा जानुहोस्**: टर्मिनल वा कमाण्ड प्रॉम्प्ट खोल्नुहोस् र `.env` फाइल बनाउन चाहनुभएको परियोजनाको मूल डिरेक्टरीमा जानुहोस्।

   ```bash
   cd path/to/your/project
   ```

२. **`.env` फाइल सिर्जना गर्नुहोस्**: तपाईँले रोजेको टेक्स्ट एडिटर प्रयोग गरेर `.env` नामको नयाँ फाइल सिर्जना गर्नुहोस्। कमाण्ड लाइनबाट, `touch` (Unix आधारित प्रणालीहरूमा) वा `echo` (Windows मा) प्रयोग गर्न सक्नुहुन्छ:

   Unix आधारित प्रणालीहरू:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

३. **`.env` फाइल संपादन गर्नुहोस्**: टेक्स्ट एडिटर (जस्तै VS Code, Notepad++, वा कुनै अन्य एडिटर) मा `.env` फाइल खोल्नुहोस्। तलका लाइनहरू थप्नुहोस्, आफ्नो वास्तविक Microsoft Foundry परियोजना endpoint र API कुञ्जीसहित प्लेसहोल्डरहरू बदल्नुहोस्:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

४. **फाइल सुरक्षित गर्नुहोस्**: परिवर्तनहरू सुरक्षित गरेर टेक्स्ट एडिटर बन्द गर्नुहोस्।

५. **`python-dotenv` स्थापना गर्नुहोस्**: यदि तपाईंले पहिले नै नगरेको भए, `.env` फाइलबाट वातावरण चरहरू Python अनुप्रयोगमा लोड गर्न `python-dotenv` प्याकेज स्थापना गर्न आवश्यक छ। `pip` प्रयोग गरेर यसलाई स्थापना गर्न सक्नुहुन्छ:

   ```bash
   pip install python-dotenv
   ```

६. **आफ्नो Python स्क्रिप्टमा वातावरण चरहरू लोड गर्नुहोस्**: आफ्नो Python स्क्रिप्टमा, `.env` फाइलबाट वातावरण चरहरू लोड गर्न `python-dotenv` प्याकेजको प्रयोग गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाइलबाट वातावरण चरहरू लोड गर्नुहोस्
   load_dotenv()

   # Microsoft Foundry मोडेलहरू चरहरू पहुँच गर्नुहोस्
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

बस! तपाईंले सफलतापूर्वक `.env` फाइल सिर्जना गर्नुभएको छ, आफ्नो Microsoft Foundry Models क्रेडेन्शियलहरू थप्नु भएको छ, र तिनीहरूलाई आफ्नो Python अनुप्रयोगमा लोड गर्नुभएको छ।

🔐 कहिल्यै `.env` कमिट नगर्नुहोस्—यो पहिल्यै `.gitignore` मा छ।
पूरा प्रदायक निर्देशनहरू [`providers.md`](03-providers.md) मा छन्।

## ४. अब के गर्ने?

| म के गर्न चाहन्छु…          | जानुहोस्…                                                                      |
|-----------------------------|--------------------------------------------------------------------------------|
| पाठ १ सुरु गर्ने              | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)             |
| एक LLM प्रदायक सेटअप गर्ने  | [`providers.md`](03-providers.md)                                              |
| अन्य सिक्नेहरूसँग भेट्ने    | [हाम्रो Discord मा देखिनुहोस्](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## ५. समस्या समाधान

| लक्षण                                         | समाधान                                                      |
|-----------------------------------------------|-------------------------------------------------------------|
| `python भेटिएन`                              | Python लाई PATH मा थप्नुहोस् वा स्थापना पछि टर्मिनल पुनः खोल्नुहोस् |
| `pip` ले Windows मा wheels बनाउन सक्दैन      | `pip install --upgrade pip setuptools wheel` त्यसपछि पुन: प्रयास गर्नुहोस्। |
| `ModuleNotFoundError: dotenv`                  | `pip install -r requirements.txt` चलाउनुहोस् (env स्थापना नभएको थियो)।   |
| Docker build मा *No space left* त्रुटि         | Docker Desktop ▸ *Settings* ▸ *Resources* → डिस्क साइज बढाउनुहोस्।       |
| VS Code निरन्तर पुनः खोल्न प्रॉम्प्ट गर्दा    | तपाईंसँग दुवै विकल्प सक्रिय हुन सक्छ; एउटामा मात्र छान्नुहोस् (venv **वा** container) |
| OpenAI 401 / 429 त्रुटिहरू                      | `OPENAI_API_KEY` मान र अनुरोध दर सीमाहरू जाँच्नुहोस्।               |
| Conda प्रयोग गर्दा त्रुटि                        | Microsoft AI लाइब्रेरीहरू `conda install -c microsoft azure-ai-ml` द्वारा स्थापना गर्नुहोस् |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->