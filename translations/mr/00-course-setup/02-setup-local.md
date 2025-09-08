<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:42:46+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "mr"
}
-->
# स्थानिक सेटअप 🖥️

**जर तुम्हाला सगळं स्वतःच्या लॅपटॉपवर चालवायचं असेल तर हा मार्गदर्शक वापरा.**  
तुमच्याकडे दोन पर्याय आहेत: **(A) नेटिव Python + virtual-env** किंवा **(B) VS Code Dev Container विथ Docker**.  
जे सोपं वाटतं ते निवडा—दोन्ही मार्ग एकाच धड्यांकडे नेतात.

## 1. पूर्वतयारी

| साधन               | आवृत्ती / टिपा                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (येथे मिळवा <https://python.org>)                                            |
| **Git**            | नवीनतम (Xcode / Git for Windows / Linux package manager सोबत येतो)                   |
| **VS Code**        | ऐच्छिक पण शिफारसीय <https://code.visualstudio.com>                                 |
| **Docker Desktop** | *फक्त* पर्याय B साठी. मोफत इन्स्टॉल: <https://docs.docker.com/desktop/>             |

> 💡 **टीप** – टूल्स टर्मिनलमध्ये तपासा:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. पर्याय A – नेटिव Python (सर्वात जलद)

### पायरी 1  हे रेपो क्लोन करा

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### पायरी 2 व्हर्च्युअल एन्व्हायर्नमेंट तयार करा आणि सक्रिय करा

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ प्रॉम्प्ट आता (.venv) ने सुरू होईल—म्हणजे तुम्ही एन्व्हायर्नमेंटमध्ये आहात.

### पायरी 3 डिपेंडन्सीज इन्स्टॉल करा

```bash
pip install -r requirements.txt
```

[API कीज](../../../00-course-setup) या विभागाकडे जा

## 2. पर्याय B – VS Code Dev Container (Docker)

हे रेपो आणि कोर्स [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) सह सेटअप केले आहे, ज्यात Universal runtime आहे आणि Python3, .NET, Node.js आणि Java development सपोर्ट करतो. संबंधित कॉन्फिगरेशन `devcontainer.json` फाईलमध्ये आहे, जी या रेपोच्या मूळमध्ये `.devcontainer/` फोल्डरमध्ये आहे.

>**हे का निवडावे?**
>Codespaces सारखेच वातावरण; डिपेंडन्सी ड्रिफ्ट नाही.

### पायरी 0 एक्स्ट्रा इन्स्टॉल करा

Docker Desktop – खात्री करा ```docker --version``` चालते.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### पायरी 1 रेपो VS Code मध्ये उघडा

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code ला .devcontainer/ सापडते आणि प्रॉम्प्ट दिसतो.

### पायरी 2 कंटेनरमध्ये पुन्हा उघडा

“Reopen in Container” क्लिक करा. Docker इमेज बिल्ड करतो (पहिल्यांदा सुमारे 3 मिनिटे).
टर्मिनल प्रॉम्प्ट दिसल्यावर, तुम्ही कंटेनरमध्ये आहात.

## 2. पर्याय C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हे [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python आणि काही पॅकेजेस इन्स्टॉल करण्यासाठी हलकेवजनाचे इन्स्टॉलर आहे.
Conda हे पॅकेज मॅनेजर आहे, जे वेगवेगळ्या Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेस सेटअप व स्विच करणे सोपे करते. pip वर उपलब्ध नसलेली पॅकेजेस इन्स्टॉल करण्यासाठीही उपयुक्त.

### पायरी 0  Miniconda इन्स्टॉल करा

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) फॉलो करा.

```bash
conda --version
```

### पायरी 1 व्हर्च्युअल एन्व्हायर्नमेंट तयार करा

नवीन environment फाईल (*environment.yml*) तयार करा. जर Codespaces वापरत असाल, तर ही `.devcontainer` डायरेक्टरीमध्ये तयार करा, म्हणजे `.devcontainer/environment.yml`.

### पायरी 2  environment फाईलमध्ये माहिती भरा

तुमच्या `environment.yml` मध्ये खालील स्निपेट जोडा

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

### पायरी 3 Conda एन्व्हायर्नमेंट तयार करा

खालील कमांड्स कमांड लाइन/टर्मिनलमध्ये चालवा

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

[Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा, काही अडचण आल्यास.

## 2 पर्याय D – क्लासिक Jupyter / Jupyter Lab (ब्राउझरमध्ये)

> **हे कोणासाठी?**  
> ज्यांना क्लासिक Jupyter इंटरफेस आवडतो किंवा VS Code शिवाय नोटबुक चालवायचे आहेत.  

### पायरी 1  खात्री करा Jupyter इन्स्टॉल आहे

Jupyter स्थानिकपणे सुरू करण्यासाठी, टर्मिनल/कमांड लाइनमध्ये जा, कोर्स डायरेक्टरीमध्ये जा आणि हे चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

यामुळे Jupyter सुरू होईल आणि त्याचा URL कमांड लाइन विंडोमध्ये दिसेल.

URL वर गेल्यावर, कोर्सचे outline दिसेल आणि कोणत्याही `*.ipynb` फाईलमध्ये जाऊ शकाल. उदाहरणार्थ, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. तुमच्या API कीज जोडा

API कीज सुरक्षित ठेवणे महत्त्वाचे आहे, कोणतीही अ‍ॅप्लिकेशन बनवताना. आम्ही शिफारस करतो की API कीज थेट कोडमध्ये ठेवू नका. त्या माहितीला सार्वजनिक रेपोमध्ये कमिट केल्यास सुरक्षेचा धोका आणि अनावश्यक खर्च होऊ शकतो.
Python साठी `.env` फाईल कशी तयार करायची आणि `GITHUB_TOKEN` कसा जोडायचा यासाठी स्टेप-बाय-स्टेप मार्गदर्शक:

1. **प्रोजेक्ट डायरेक्टरीमध्ये जा**: टर्मिनल किंवा कमांड प्रॉम्प्ट उघडा आणि प्रोजेक्टच्या मूळ डायरेक्टरीमध्ये जा, जिथे `.env` फाईल तयार करायची आहे.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाईल तयार करा**: आवडता टेक्स्ट एडिटर वापरून नवीन `.env` नावाची फाईल तयार करा. कमांड लाइन वापरत असाल तर `touch` (Unix-based systems साठी) किंवा `echo` (Windows साठी) वापरा:

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाईल एडिट करा**: `.env` फाईल टेक्स्ट एडिटरमध्ये उघडा (उदा. VS Code, Notepad++, किंवा इतर). खालील ओळ फाईलमध्ये जोडा, `your_github_token_here` ऐवजी तुमचा GitHub टोकन टाका:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाईल सेव्ह करा**: बदल सेव्ह करा आणि एडिटर बंद करा.

5. **`python-dotenv` इन्स्टॉल करा**: अजून इन्स्टॉल केले नसेल, तर `python-dotenv` पॅकेज इन्स्टॉल करा, जे `.env` फाईलमधून एन्व्हायर्नमेंट व्हेरिएबल्स Python अ‍ॅप्लिकेशनमध्ये लोड करेल. `pip` वापरून इन्स्टॉल करा:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्टमध्ये एन्व्हायर्नमेंट व्हेरिएबल्स लोड करा**: Python स्क्रिप्टमध्ये `python-dotenv` वापरून `.env` फाईलमधून एन्व्हायर्नमेंट व्हेरिएबल्स लोड करा:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस! तुम्ही यशस्वीरित्या `.env` फाईल तयार केली, GitHub टोकन जोडला आणि तो Python अ‍ॅप्लिकेशनमध्ये लोड केला.

🔐 .env कधीही कमिट करू नका—तो आधीच .gitignore मध्ये आहे.
पूर्ण प्रोव्हायडर सूचना [`providers.md`](03-providers.md) मध्ये आहेत.

## 4. पुढे काय?

| मला हे करायचं आहे…          | येथे जा…                                                                  |
|-----------------------------|---------------------------------------------------------------------------|
| धडा 1 सुरू करा              | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| LLM प्रोव्हायडर सेटअप करा    | [`providers.md`](03-providers.md)                                         |
| इतर शिकणाऱ्यांना भेटा        | [आमच्या Discord ला जॉइन करा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. समस्या सोडवणे

| लक्षण                                   | उपाय                                                             |
|------------------------------------------|------------------------------------------------------------------|
| `python not found`                       | Python PATH मध्ये जोडा किंवा इन्स्टॉल नंतर टर्मिनल पुन्हा उघडा  |
| `pip` cannot build wheels (Windows)      | `pip install --upgrade pip setuptools wheel` नंतर पुन्हा प्रयत्न करा.|
| `ModuleNotFoundError: dotenv`            | `pip install -r requirements.txt` चालवा (env इन्स्टॉल झाला नाही).|
| Docker build fails *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → डिस्क साईज वाढवा.   |
| VS Code वारंवार पुन्हा उघडण्याचा प्रॉम्प्ट| दोन्ही पर्याय सक्रिय असू शकतात; एक निवडा (venv **किंवा** container)|
| OpenAI 401 / 429 errors                  | `OPENAI_API_KEY` व्हॅल्यू / request rate limits तपासा.           |
| Conda वापरताना त्रुटी                    | Microsft AI libraries `conda install -c microsoft azure-ai-ml` वापरून इन्स्टॉल करा|

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.