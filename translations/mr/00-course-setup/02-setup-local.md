# स्थानिक सेटअप 🖥️

**जर तुम्हाला सगळं तुमच्या स्वतःच्या लॅपटॉपवर चालवायचं असेल तर हा मार्गदर्शक वापरा.**  
तुमच्याकडे दोन मार्ग आहेत: **(A) नेटिव्ह Python + virtual-env** किंवा **(B) Docker सह VS Code Dev कंटेनर**.  
ज्या योग्य वाटेल तो पर्याय निवडा — दोन्ही एकाच धड्यांवर नेतात.

## 1. पूर्वअटी

| टूल               | आवृत्ती / नोंदी                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> वरून मिळवा)                                           |
| **Git**            | नवीनतम (Xcode / Git for Windows / Linux पॅकेज मॅनेजरसह येतो)                       |
| **VS Code**        | पर्यायी पण शिफारसीय <https://code.visualstudio.com>                                |
| **Docker Desktop** | केवळ पर्याय B साठी. विनामूल्य इंस्टॉल: <https://docs.docker.com/desktop/>           |

> 💡 **टीप** – टर्मिनलमध्ये टूल्स तपासा:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. पर्याय A – नेटिव्ह Python (सर्वात जलद)

### पाऊल 1  हा रिपो क्लोन करा

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### पाऊल 2 व्हर्च्युअल एंवायरनमेंट तयार करा आणि सक्रिय करा

```bash
python -m venv .venv          # एक तयार करा
source .venv/bin/activate     # macOS / लिनक्स
.\.venv\Scripts\activate      # विंडोज पॉवरशेल
```

✅ प्रॉम्ट आता (.venv) ने सुरू होईल — म्हणजे तुम्ही एंवायरनमेंटमध्ये आहात.

### पाऊल 3 अवलंबित्वे इंस्टॉल करा

```bash
pip install -r requirements.txt
```

[API keys](#3-तुमचे-api-कीज-जोडा) विभागावर जाण्यासाठी थांबा.

## 2. पर्याय B – VS Code Dev कंटेनर (Docker)

आम्ही हा रेपॉझिटरी आणि अभ्यासक्रम [डिव्हलपमेंट कंटेनर](https://containers.dev?WT.mc_id=academic-105485-koreyst) वापरून सेटअप केला आहे ज्यामध्ये Python3, .NET, Node.js आणि Java डेव्हलपमेंटसाठी युनिव्हर्सल रनटाईम आहे. संबंधित कॉन्फिगरेशन `devcontainer.json` फाइलमध्ये आहे जी या रेपॉझिटरीच्या रूटमधील `.devcontainer/` फोल्डरमध्ये आहे.

>**हे का निवडावे?**
>Codespaces सारखेच वातावरण; कोणताही अवलंबित्वांचा फरक नाही.

### पाऊल 0 एक्स्ट्रा टूल्स इंस्टॉल करा

Docker Desktop – `docker --version` चालते याची खात्री करा.
VS Code Remote – Containers विस्तार (ID: ms-vscode-remote.remote-containers).

### पाऊल 1 रिपो VS Code मध्ये उघडा

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code `.devcontainer/` ओळखते आणि प्रॉम्प्ट दाखवते.

### पाऊल 2 कंटेनरमध्ये पुन्हा उघडा

"Reopen in Container" क्लिक करा. Docker प्रथम वेळी इमेज तयार करतो (सुमारे 3 मिनिटे).
जेव्हा टर्मिनल प्रॉम्प्ट दिसतो, तेव्हा तुम्ही कंटेनरमध्ये आहात.

## 2. पर्याय C – मिनिकोंडा

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हा [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python आणि काही पॅकेजेस सोप्या पद्धतीने इंस्टॉल करण्यासाठी हलका इंस्टॉलर आहे.
Conda स्वतः एक पॅकेज मॅनेजर आहे, ज्यामुळे विविध Python [**वर्च्युअल एन्व्हायर्नमेंट**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेस सहज सेटअप व स्विच करता येतात. `pip` द्वारा उपलब्ध नसलेली पॅकेजेस इंस्टॉल करण्यासाठीही उपयुक्त आहे.

### पाऊल 0  मिनिकोंडा इंस्टॉल करा

सेटअपसाठी [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) फॉलो करा.

```bash
conda --version
```

### पाऊल 1 नवीन वर्च्युअल एन्व्हायर्नमेंट तयार करा

नवीन environment फाइल (*environment.yml*) तयार करा. Codespaces वापरत असल्यास, ही फाइल `.devcontainer` डायरेक्टरीमध्ये तयार करा, म्हणजे `.devcontainer/environment.yml`.

### पाऊल 2  environment फाइलमध्ये माहिती भरा

`environment.yml` मध्ये खालील कोड जोडा

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

### पाऊल 3 Conda एन्व्हायर्नमेंट तयार करा

टर्मिनलमध्ये खालील कमांड्स चालवा

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप路径 केवळ Codespace सेटअपसाठी लागू असतो
conda activate ai4beg
```

समस्या आल्यास [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा.

## 2  पर्याय D – क्लासिक Jupyter / Jupyter Lab (तुमच्या ब्राउझरमध्ये)

> **कोणासाठी?**  
> ज्या लोकांना क्लासिक Jupyter इंटरफेस आवडतो किंवा VS Code शिवाय नोटबुक चालवायचे आहेत.  

### पाऊल 1  Jupyter इंस्टॉल आहे की नाही तपासा

स्थानिक Jupyter सुरू करण्यासाठी, टर्मिनल/कमांड लाइन उघडा, कोर्स डायरेक्टरीमध्ये जा आणि खालील कमांड चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

यामुळे Jupyter सुरू होईल आणि त्याला भेट देण्यासाठी URL कमांड लाइन विंडोमध्ये दर्शविली जाईल.

URL वर प्रवेश केल्यावर, तुम्हाला कोर्सची रूपरेषा दिसेल आणि कोणतीही `*.ipynb` फाइल उघडू शकता. उदाहरणार्थ, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. तुमचे API कीज जोडा

कोणत्याही प्रकारचे ॲप तयार करताना तुमच्या API कीज सुरक्षित ठेवणे महत्त्वाचे आहे. आम्ही सुचवतो की API कीज थेट कोडमध्ये न ठेवाव्यात. सार्वजनिक रेपॉझिटरीमध्ये कमिट केल्यास सुरक्षा समस्या उद्भवू शकतात आणि गैरसोयीच्या खर्चाची शक्यता असते.
Python साठी `.env` फाइल कशी तयार करायची आणि Microsoft Foundry Models क्रेडेन्शियल्स कशी जोडायची याचा चरण-दर-चरण मार्गदर्शक खाली दिला आहे:

> **टीप:** GitHub Models (आणि त्याचा `GITHUB_TOKEN` व्हेरिएबल) जुलै 2026 अखेरीस रिटायर होणार आहे. हा मार्गदर्शक [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) वापरतो. पूर्णपणे ऑफलाइन काम करायचे आहे? [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) पहा.

1. **तुमच्या प्रोजेक्ट डायरेक्टरीला जा**: टर्मिनल किंवा कमांड प्रॉम्प्ट उघडा आणि `.env` फाइल तयार करण्यासाठी प्रोजेक्टच्या मूळ फोल्डरमध्ये जा.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाइल तयार करा**: तुमच्या आवडत्या टेक्स्ट एडिटरने `.env` नावाची नवीन फाइल तयार करा. कमांड लाइनवर असल्यास, `touch` (युनिकस सिस्टमवर) किंवा `echo` (Windows वर) वापरू शकता:

   युनिकस सिस्टम्ससाठी:

   ```bash
   touch .env
   ```

   Windows साठी:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल संपादित करा**: `.env` फाइल टेक्स्ट एडिटरमध्ये उघडा (उदा. VS Code, Notepad++, किंवा इतर कोणताही एडिटर). खालील ओळी फाइलमध्ये जोडा आणि प्लेसहोल्डर्स ऐवजी तुमचा Microsoft Foundry प्रोजेक्ट एंडपॉइंट आणि API की प्रविष्ट करा:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फाइल जतन करा**: बदल जतन करा आणि टेक्स्ट एडिटर बंद करा.

5. **`python-dotenv` इंस्टॉल करा**: जर आधी इंस्टॉल नसेल तर, `.env` फाइलमधील पर्यावरण चल (environment variables) Python ॲप्लिकेशनमध्ये लोड करण्यासाठी `python-dotenv` पॅकेज इंस्टॉल करा. `pip` वापरून हे करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्टमध्ये पर्यावरण चल लोड करा**: Python स्क्रिप्टमध्ये `.env` फाइलमधून पर्यावरण चल लोड करण्यासाठी `python-dotenv` पॅकेज वापरा:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाइलमधून पर्यावरणातील चलन लोड करा
   load_dotenv()

   # Microsoft Foundry Models चलनांमध्ये प्रवेश करा
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

एवढेच! तुम्ही यशस्वीपणे `.env` फाइल तयार केली, Microsoft Foundry Models क्रेडेन्शियल्स जोडले आणि ती Python ॲप्लिकेशनमध्ये लोड केली.

🔐 .env कधीही कमिट करू नका — ती आधीच .gitignore मध्ये आहे.
पूर्ण प्रदाता सूचना [`providers.md`](03-providers.md) मध्ये आहेत.

## 4. पुढे काय?

| मला हवंय…          | येथे जा…                                                                |
|---------------------|----------------------------------------------------------------------|
| धडा 1 सुरू करा     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| LLM प्रदाता सेटअप करा | [`providers.md`](03-providers.md)                                  |
| इतर विद्यार्थ्यांशी भेटा | [आमच्या डिस्कॉर्डमध्ये सामील व्हा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. समस्या निवारण

| लक्षण                                   | निराकरण                                                        |
|-----------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Python PATH मध्ये जोडा किंवा इंस्टॉल केल्यावर टर्मिनल पुन्हा उघडा  |
| `pip` व्हील्स बांधू शकत नाही (Windows)  | `pip install --upgrade pip setuptools wheel` नंतर पुन्हा प्रयत्न करा.|
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` चालवा (env इंस्टॉल नसेल).      |
| Docker build अयशस्वी *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → डिस्क साईज वाढवा.    |
| VS Code सतत पुन्हा उघडण्यास सांगतो      | दोन्ही पर्याय सक्रिय असू शकतात; एक निवडा (venv **किंवा** कंटेनर)  |
| OpenAI 401 / 429 त्रुटी                    | `OPENAI_API_KEY` व्हॅल्यू आणि विनंती मर्यादा तपासा.                |
| Conda वापरताना त्रुटी                    | `conda install -c microsoft azure-ai-ml` वापरून Microsoft AI लायब्ररी इंस्टॉल करा.|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->