<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:43:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "mr"
}
-->
# या कोर्ससह सुरुवात करा

तुम्ही हा कोर्स सुरू करत आहात याचा आम्हाला खूप आनंद आहे आणि जनरेटिव AI वापरून तुम्ही काय तयार करता याची उत्सुकता आहे!

तुमच्या यशासाठी, या पृष्ठावर सेटअपची पावले, तांत्रिक आवश्यकता आणि मदतीसाठी कुठे संपर्क साधावा याची माहिती दिली आहे.

## सेटअपची पावले

हा कोर्स सुरू करण्यासाठी, तुम्हाला खालील पावले पूर्ण करावी लागतील.

### 1. हे रिपो Fork करा

[Fork करा हे संपूर्ण रिपो](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तुमच्या स्वतःच्या GitHub अकाउंटवर, जेणेकरून तुम्ही कोडमध्ये बदल करू शकता आणि चॅलेंजेस पूर्ण करू शकता. तुम्ही [repo ला स्टार (🌟) देखील देऊ शकता](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) जेणेकरून हे आणि संबंधित रिपो सहज सापडतील.

### 2. Codespace तयार करा

कोड चालवताना dependency संबंधित समस्या टाळण्यासाठी, आम्ही हा कोर्स [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मध्ये चालवण्याची शिफारस करतो.

तुमच्या fork मध्ये: **Code -> Codespaces -> New on main**

![Codespace तयार करण्यासाठी डायलॉग](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Secret जोडा

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाव OPENAI_API_KEY, तुमची key paste करा, Save करा.

### 3. पुढे काय?

| मला हे करायचे आहे…      | येथे जा…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| पहिला धडा सुरू करा      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ऑफलाइन काम करा        | [`setup-local.md`](02-setup-local.md)                                   |
| LLM Provider सेटअप करा | [`providers.md`](providers.md)                                        |
| इतर शिकणाऱ्यांना भेटा | [आमच्या Discord ला जॉइन करा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या सोडवणे

| लक्षण                                   | उपाय                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build १० मिनिटांपेक्षा जास्त वेळ घेत आहे            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal attach झाले नाही; **+** ➜ *bash* क्लिक करा                    |
| OpenAI कडून `401 Unauthorized`            | चुकीची / कालबाह्य `OPENAI_API_KEY`                                |
| VS Code मध्ये “Dev container mounting…”   | Browser tab refresh करा—Codespaces कधी कधी connection हरवतो   |
| Notebook kernel missing                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल एडिट करा**: `.env` फाइल text editor मध्ये उघडा (उदा. VS Code, Notepad++, किंवा इतर). खालील ओळ फाइलमध्ये जोडा, `your_github_token_here` ऐवजी तुमचा GitHub token टाका:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल सेव्ह करा**: बदल सेव्ह करा आणि editor बंद करा.

5. **`python-dotenv` इंस्टॉल करा**: जर अजून केले नसेल, तर तुम्हाला `python-dotenv` पॅकेज इंस्टॉल करावे लागेल जेणेकरून environment variables `.env` फाइलमधून Python app मध्ये लोड होतील. हे `pip` वापरून इंस्टॉल करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **Python script मध्ये Environment Variables लोड करा**: Python script मध्ये `python-dotenv` वापरून `.env` फाइलमधून variables लोड करा:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

बस! तुम्ही यशस्वीरित्या `.env` फाइल तयार केली, GitHub token जोडला, आणि तो Python app मध्ये लोड केला.

## तुमच्या संगणकावर लोकली कसे चालवायचे

कोड लोकली चालवण्यासाठी, [Python ची काही आवृत्ती इंस्टॉल](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) असणे आवश्यक आहे.

रिपॉझिटरी वापरण्यासाठी, तुम्हाला ते clone करावे लागेल:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सर्व काही तयार झाल्यावर, तुम्ही सुरुवात करू शकता!

## पर्यायी पावले

### Miniconda इंस्टॉल करणे

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हे [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python आणि काही पॅकेजेस इंस्टॉल करण्यासाठी हलके installer आहे.
Conda हे एक package manager आहे, जे वेगवेगळ्या Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेस सेटअप व switch करणे सोपे करते. काही पॅकेजेस जे `pip` वर उपलब्ध नाहीत, ते इंस्टॉल करण्यासाठी देखील Conda उपयुक्त आहे.

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) फॉलो करून ते सेटअप करा.

Miniconda इंस्टॉल झाल्यावर, [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) clone करा (जर अजून केले नसेल).

पुढे, virtual environment तयार करा. Conda वापरून environment file (_environment.yml_) तयार करा. Codespaces वापरत असाल तर, हे `.devcontainer` directory मध्ये तयार करा, म्हणजे `.devcontainer/environment.yml`.

तुमच्या environment file मध्ये खालील snippet टाका:

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

जर Conda वापरताना त्रुटी आल्या तर, Microsoft AI Libraries खालील कमांड वापरून manually इंस्टॉल करू शकता.

```
conda install -c microsoft azure-ai-ml
```

Environment file मध्ये लागणाऱ्या dependencies specify केल्या आहेत. `<environment-name>` म्हणजे Conda environment साठी तुम्हाला हवे असलेले नाव, आणि `<python-version>` म्हणजे Python ची आवृत्ती, उदा. `3` ही Python ची नवीन आवृत्ती आहे.

हे पूर्ण झाल्यावर, खालील कमांड्स वापरून Conda environment तयार करा:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

काही अडचण आल्यास [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा.

### Python support extension सह Visual Studio Code वापरणे

आम्ही [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor आणि [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) इंस्टॉल करण्याची शिफारस करतो. हे फक्त शिफारस आहे, गरजेचे नाही.

> **Note**: VS Code मध्ये कोर्स रिपॉझिटरी उघडल्यावर, प्रोजेक्ट कंटेनरमध्ये सेटअप करण्याचा पर्याय मिळतो. हे [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory मुळे शक्य आहे. याबद्दल पुढे अधिक माहिती मिळेल.

> **Note**: रिपॉझिटरी clone करून VS Code मध्ये उघडल्यावर, Python support extension इंस्टॉल करण्याचा suggestion येईल.

> **Note**: VS Code कंटेनरमध्ये रिपॉझिटरी उघडण्याचा सल्ला देत असेल, तर तो नाकारून लोकली इंस्टॉल केलेला Python वापरा.

### ब्राउझरमध्ये Jupyter वापरणे

तुम्ही [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ब्राउझरमध्ये वापरून प्रोजेक्टवर काम करू शकता. Classic Jupyter आणि [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोन्हीमध्ये auto-completion, code highlighting इ. सुविधा मिळतात.

Jupyter लोकली सुरू करण्यासाठी, terminal/command line मध्ये जा, कोर्स directory मध्ये जा, आणि हे चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

यामुळे Jupyter instance सुरू होईल आणि त्याचा URL command line window मध्ये दिसेल.

URL access केल्यावर, कोर्स outline दिसेल आणि कोणत्याही `*.ipynb` फाइलवर जाऊ शकता. उदा. `08-building-search-applications/python/oai-solution.ipynb`.

### कंटेनरमध्ये चालवणे

तुमच्या संगणकावर किंवा Codespace मध्ये सर्व सेटअप करण्याचा पर्याय नको असेल, तर [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) वापरू शकता. कोर्स रिपॉझिटरीतील `.devcontainer` फोल्डरमुळे VS Code मध्ये प्रोजेक्ट कंटेनरमध्ये सेटअप करता येतो. Codespaces शिवाय, यासाठी Docker इंस्टॉल करावे लागेल, आणि हे थोडे जास्त काम आहे, त्यामुळे कंटेनरमध्ये कामाचा अनुभव असलेल्या लोकांसाठीच हे शिफारसीय आहे.

GitHub Codespaces वापरताना API keys सुरक्षित ठेवण्यासाठी Codespace Secrets वापरणे उत्तम आहे. [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide फॉलो करा.

## धडे आणि तांत्रिक आवश्यकता

कोर्समध्ये ६ संकल्पना धडे आणि ६ कोडिंग धडे आहेत.

कोडिंग धड्यांसाठी, आम्ही Azure OpenAI Service वापरत आहोत. हे कोड चालवण्यासाठी Azure OpenAI service आणि API key ची आवश्यकता आहे. [हे application पूर्ण करून](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) access मिळवू शकता.

तुमचे application process होईपर्यंत, प्रत्येक कोडिंग धड्यात `README.md` फाइल आहे, जिथे तुम्ही कोड आणि outputs पाहू शकता.

## Azure OpenAI Service प्रथमच वापरत असाल तर

जर तुम्ही Azure OpenAI service प्रथमच वापरत असाल, तर [Azure OpenAI Service resource कसे तयार व deploy करायचे](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) हे guide फॉलो करा.

## OpenAI API प्रथमच वापरत असाल तर

जर तुम्ही OpenAI API प्रथमच वापरत असाल, तर [Interface कसे तयार व वापरायचे](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) हे guide फॉलो करा.

## इतर शिकणाऱ्यांना भेटा

आम्ही आमच्या अधिकृत [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) वर इतर शिकणाऱ्यांना भेटण्यासाठी channels तयार केले आहेत. हे नेटवर्किंगसाठी उत्तम आहे, जिथे उद्योजक, builders, विद्यार्थी आणि जनरेटिव AI मध्ये प्रगती करू इच्छिणारे लोक भेटू शकतात.

[![Discord channel जॉइन करा](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टीम देखील या Discord server वर शिकणाऱ्यांना मदत करण्यासाठी उपलब्ध असेल.

## योगदान द्या

हा कोर्स open-source initiative आहे. सुधारणा किंवा समस्या दिसल्यास, कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) तयार करा किंवा [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लॉग करा.

प्रोजेक्ट टीम सर्व योगदान ट्रॅक करेल. Open source मध्ये योगदान देणे हे जनरेटिव AI मध्ये करिअर घडवण्यासाठी उत्तम आहे.

बहुतेक योगदानांसाठी Contributor License Agreement (CLA) मान्य करणे आवश्यक आहे, ज्यात तुम्ही तुमचे योगदान वापरण्याचा अधिकार आम्हाला देता. अधिक माहितीसाठी [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) पहा.

महत्त्वाचे: या रिपोमध्ये मजकूर भाषांतर करताना, कृपया मशीन ट्रान्सलेशन वापरू नका. आम्ही कम्युनिटीद्वारे भाषांतर तपासू, त्यामुळे फक्त त्या भाषेत प्रवीण असाल तरच भाषांतरासाठी स्वयंसेवक व्हा.

Pull request सबमिट केल्यावर, CLA-bot आपोआप तपासेल की CLA आवश्यक आहे का आणि PR ला योग्य लेबल/कॉमेंट लावेल. Bot ने दिलेल्या सूचनांचे पालन करा. हे सर्व रिपॉझिटरीजसाठी एकदाच करावे लागेल.

या प्रोजेक्टने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) स्वीकारला आहे. अधिक माहितीसाठी Code of Conduct FAQ वाचा किंवा [Email opencode](opencode@microsoft.com) वर प्रश्न/कॉमेंट पाठवा.

## चला सुरुवात करूया
आता तुम्ही या कोर्ससाठी आवश्यक असलेली सर्व पावले पूर्ण केली आहेत, चला सुरुवात करूया आणि [जनरेटिव्ह AI आणि LLMs ची ओळख](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) घेऊया.

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.