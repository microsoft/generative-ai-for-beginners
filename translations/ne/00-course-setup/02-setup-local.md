<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:52:26+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ne"
}
-->
# स्थानीय सेटअप 🖥️

**यदि तपाईं सबै कुरा आफ्नै ल्यापटपमा चलाउन चाहनुहुन्छ भने यो गाइड प्रयोग गर्नुहोस्।**  
तपाईंसँग दुई विकल्प छन्: **(A) नेटिभ Python + virtual-env** वा **(B) VS Code Dev Container with Docker**।  
आफ्नो लागि सजिलो लाग्ने विकल्प छान्नुहोस्—दुवैबाट एउटै पाठहरू सुरु हुन्छन्।

## 1.  आवश्यक पूर्व तयारी

| उपकरण               | संस्करण / नोट्स                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (यहाँबाट प्राप्त गर्नुहोस् <https://python.org>)                               |
| **Git**            | पछिल्लो संस्करण (Xcode / Git for Windows / Linux package manager सँग आउँछ)           |
| **VS Code**        | वैकल्पिक तर सिफारिस गरिन्छ <https://code.visualstudio.com>                          |
| **Docker Desktop** | *केवल* विकल्प B का लागि। निःशुल्क स्थापना: <https://docs.docker.com/desktop/>       |

> 💡 **टिप** – टर्मिनलमा उपकरणहरू जाँच गर्नुहोस्:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  विकल्प A – नेटिभ Python (सबैभन्दा छिटो)

### चरण 1  यो रेपो क्लोन गर्नुहोस्

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### चरण 2  भर्चुअल वातावरण बनाउनुहोस् र सक्रिय गर्नुहोस्

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ अब प्रॉम्प्ट (.venv) बाट सुरु हुनुपर्छ—यसको अर्थ तपाईं वातावरण भित्र हुनुहुन्छ।

### चरण 3  निर्भरता स्थापना गर्नुहोस्

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) मा जानुहोस्

## 2. विकल्प B – VS Code Dev Container (Docker)

हामीले यो रेपो र कोर्सलाई [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) सँग सेटअप गरेका छौं जसमा Universal runtime छ, जसले Python3, .NET, Node.js र Java विकासलाई समर्थन गर्छ। सम्बन्धित कन्फिगरेसन `devcontainer.json` फाइलमा छ, जुन यो रेपोको मूलमा `.devcontainer/` फोल्डरमा छ।

>**किन छान्ने?**
>Codespaces जस्तै वातावरण; निर्भरता फरक पर्दैन।

### चरण 0  अतिरिक्तहरू स्थापना गर्नुहोस्

Docker Desktop – ```docker --version``` काम गर्छ कि जाँच गर्नुहोस्।
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers) स्थापना गर्नुहोस्।

### चरण 1  रेपो VS Code मा खोल्नुहोस्

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code ले .devcontainer/ पत्ता लगाउँछ र प्रॉम्प्ट देखाउँछ।

### चरण 2  कन्टेनरमा पुन: खोल्नुहोस्

“Reopen in Container” क्लिक गर्नुहोस्। Docker ले इमेज बनाउँछ (पहिलो पटक लगभग ३ मिनेट लाग्न सक्छ)।
टर्मिनल प्रॉम्प्ट देखिएपछि, तपाईं कन्टेनर भित्र हुनुहुन्छ।

## 2.  विकल्प C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हल्का इन्स्टलर हो, जसले [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, र केही प्याकेजहरू इन्स्टल गर्न मद्दत गर्छ।
Conda आफैंमा प्याकेज म्यानेजर हो, जसले विभिन्न Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) र प्याकेजहरू सजिलै सेटअप र स्विच गर्न मद्दत गर्छ। pip बाट उपलब्ध नभएका प्याकेजहरू इन्स्टल गर्न पनि उपयोगी छ।

### चरण 0  Miniconda स्थापना गर्नुहोस्

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) अनुसरण गरेर सेटअप गर्नुहोस्।

```bash
conda --version
```

### चरण 1  भर्चुअल वातावरण बनाउनुहोस्

नयाँ environment फाइल (*environment.yml*) बनाउनुहोस्। यदि तपाईं Codespaces प्रयोग गर्दै हुनुहुन्छ भने, यो `.devcontainer` डाइरेक्टरी भित्र बनाउनुहोस्, अर्थात् `.devcontainer/environment.yml`।

### चरण 2  environment फाइलमा सामग्री थप्नुहोस्

तलको स्निपेट `environment.yml` मा थप्नुहोस्

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

### चरण 3  Conda वातावरण बनाउनुहोस्

तलका कमाण्डहरू कमाण्ड लाइन/टर्मिनलमा चलाउनुहोस्

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

यदि समस्या आयो भने [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्।

## 2  विकल्प D – क्लासिक Jupyter / Jupyter Lab (ब्राउजरमा)

> **यो कसका लागि?**  
> क्लासिक Jupyter इन्टरफेस मन पराउने वा VS Code बिना नोटबुक चलाउन चाहने सबैका लागि।  

### चरण 1  Jupyter इन्स्टल भएको छ कि छैन जाँच गर्नुहोस्

Jupyter स्थानीय रूपमा सुरु गर्न टर्मिनल/कमाण्ड लाइनमा जानुहोस्, कोर्स डाइरेक्टरीमा जानुहोस्, र निम्न कमाण्ड चलाउनुहोस्:

```bash
jupyter notebook
```

वा

```bash
jupyterhub
```

यसले Jupyter instance सुरु गर्छ र पहुँच गर्न URL कमाण्ड लाइनमा देखिन्छ।

URL खोल्दा, तपाईंले कोर्स outline देख्नुहुन्छ र कुनै पनि `*.ipynb` फाइलमा जान सक्नुहुन्छ। जस्तै, `08-building-search-applications/python/oai-solution.ipynb`।

## 3. आफ्नो API Keys थप्नुहोस्

कुनै पनि एप्लिकेसन बनाउँदा API keys सुरक्षित राख्नु महत्त्वपूर्ण छ। हामी सिफारिस गर्छौं कि API keys सिधै कोडमा नराख्नुहोस्। ती विवरणहरू सार्वजनिक रेपोमा कमिट गर्दा सुरक्षा समस्या र अनावश्यक खर्च हुन सक्छ।
Python का लागि `.env` फाइल कसरी बनाउने र `GITHUB_TOKEN` थप्ने चरणहरू यहाँ छन्:

1. **आफ्नो प्रोजेक्ट डाइरेक्टरीमा जानुहोस्**: टर्मिनल वा कमाण्ड प्रॉम्प्ट खोल्नुहोस् र प्रोजेक्टको मूल डाइरेक्टरीमा जानुहोस् जहाँ तपाईं `.env` फाइल बनाउने हो।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाइल बनाउनुहोस्**: मनपर्ने टेक्स्ट एडिटर प्रयोग गरेर नयाँ `.env` नामको फाइल बनाउनुहोस्। कमाण्ड लाइनबाट `touch` (Unix-based सिस्टममा) वा `echo` (Windows मा) प्रयोग गर्न सक्नुहुन्छ:

   Unix-based सिस्टम:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल एडिट गर्नुहोस्**: `.env` फाइल टेक्स्ट एडिटर (जस्तै VS Code, Notepad++, वा अन्य) मा खोल्नुहोस्। तलको लाइन थप्नुहोस्, `your_github_token_here` लाई आफ्नो वास्तविक GitHub token ले बदल्नुहोस्:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल सेभ गर्नुहोस्**: परिवर्तनहरू सेभ गरेर एडिटर बन्द गर्नुहोस्।

5. **`python-dotenv` स्थापना गर्नुहोस्**: यदि पहिले स्थापना गर्नुभएको छैन भने, `.env` फाइलबाट environment variables लोड गर्न `python-dotenv` प्याकेज स्थापना गर्नुहोस्। `pip` प्रयोग गरेर इन्स्टल गर्न सक्नुहुन्छ:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्टमा Environment Variables लोड गर्नुहोस्**: Python स्क्रिप्टमा `python-dotenv` प्रयोग गरेर `.env` फाइलबाट environment variables लोड गर्नुहोस्:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

यत्ति हो! तपाईंले सफलतापूर्वक `.env` फाइल बनाउनु भयो, GitHub token थप्नुभयो, र Python एप्लिकेसनमा लोड गर्नुभयो।

🔐 .env कहिल्यै commit नगर्नुहोस्—यो पहिले नै .gitignore मा छ।
पूर्ण प्रदायक निर्देशनहरू [`providers.md`](03-providers.md) मा छन्।

## 4. अब के गर्ने?

| म गर्न चाहन्छु…          | जानुहोस्…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| पाठ १ सुरु गर्नुहोस्      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM प्रदायक सेटअप गर्नुहोस् | [`providers.md`](03-providers.md)                                       |
| अन्य सिक्नेहरूसँग भेट्नुहोस् | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. समस्या समाधान

| लक्षण                                   | समाधान                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Python लाई PATH मा थप्नुहोस् वा स्थापना पछि टर्मिनल पुन: खोल्नुहोस्            |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` चलाएर पुन: प्रयास गर्नुहोस्.        |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` चलाउनुहोस् (env स्थापना भएको छैन).   |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → disk size बढाउनुहोस्. |
| VS Code keeps prompting to reopen         | तपाईंले दुवै विकल्प सक्रिय गर्नुभएको हुन सक्छ; एउटा छान्नुहोस् (venv **वा** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` को मान / request rate limits जाँच गर्नुहोस्.             |
| Conda प्रयोग गर्दा त्रुटि                 | Microsft AI libraries `conda install -c microsoft azure-ai-ml` प्रयोग गरेर स्थापना गर्नुहोस्|

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको मूल दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।