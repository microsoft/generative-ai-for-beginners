# या कोर्ससह सुरूवात करणे

आम्ही तुमचे हे कोर्स सुरू करण्यासाठी खूप उत्साहित आहोत आणि पाहू इच्छितो की तुम्ही जनरेटिव्ह AI सह काय प्रेरित व्हाल आणि काय तयार कराल!

तुमच्या यशासाठी, हे पृष्ठ सेटअप चरण, तांत्रिक आवश्यकता आणि गरज असल्यास मदत कुठे मिळेल हे सांगते.

## सेटअप चरण

हा कोर्स घेण्यास सुरूवात करण्यासाठी, तुम्हाला खालील चरण पूर्ण करावे लागतील.

### 1. हा Repo Fork करा

तुमच्या स्वतःच्या GitHub खात्यावर [हा संपूर्ण repo Fork करा](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) जेणेकरुन तुम्ही कोणतीही कोड बदलू शकता आणि आव्हाने पूर्ण करू शकता. तुम्ही हे repo सोडून [स्टार (🌟) देखील देऊ शकता](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) जेणेकरुन ते आणि संबंधित repos सहज सापडतील.

### 2. एक codespace तयार करा

कोड चालवताना कोणतीही अवलंबित्व समस्या टाळण्यासाठी, आम्ही हा कोर्स [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मध्ये चालवण्यासाठी शिफारस करतो.

तुमच्या fork मध्ये: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/mr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 गुपित जोडा

1. ⚙️ गियर आयकॉन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाव द्या OPENAI_API_KEY, तुमचा की पेस्ट करा, जतन करा.

### 3. पुढे काय?

| मला हवे आहे...           | येथे जा...                                                               |
|--------------------------|-------------------------------------------------------------------------|
| लेसन 1 सुरू करा          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ऑफलाइन काम करा          | [`setup-local.md`](02-setup-local.md)                                   |
| LLM प्रदाता सेटअप करा    | [`providers.md`](03-providers.md)                                        |
| इतर शिकणाऱ्यांशी भेटा    | [आमच्या Discord मध्ये सामील व्हा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या निराकरण


| लक्षण                                   | उपाय                                                            |
|-----------------------------------------|-----------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनिटांपेक्षा जास्त अडकले | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | टर्मिनल जोडलेला नाही; **+** वर क्लिक करा ➜ *bash*              |
| OpenAI कडून `401 Unauthorized`           | चुकीचा / कालबाह्य `OPENAI_API_KEY`                            |
| VS Code “Dev container mounting…” दाखवतो | ब्राउझर टॅब रिफ्रेश करा—Codespaces कधी कधी कनेक्शन गमावते    |
| नोटबुक कर्नेल गायब                          | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix आधारित सिस्टम्स:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल संपादित करा**: `.env` फाइल एखाद्या टेक्स्ट एडिटरमध्ये (उदा. VS Code, Notepad++, किंवा कोणत्याही दुसऱ्या एडिटर) उघडा. खालील ओळ फाइलमध्ये जोडा, `your_github_token_here` या जागी तुमचा वास्तविक GitHub टोकन प्रविष्ट करा:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल जतन करा**: बदल जतन करा आणि टेक्स्ट एडिटर बंद करा.

5. **`python-dotenv` इन्स्टॉल करा**: जर तुम्ही आधीच केले नसेल, तर या पॅकेजची गरज आहे जेणेकरुन `.env` फाइलमधील पर्यावरण चर Python अ‍ॅप्लिकेशनमध्ये लोड करता येतील. तुम्ही ते `pip` वापरून इन्स्टॉल करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **Python स्क्रिप्टमध्ये पर्यावरण चर लोड करा**: तुमच्या Python स्क्रिप्टमध्ये `python-dotenv` पॅकेज वापरून `.env` फाइलमधील पर्यावरण चर लोड करा:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाईलमधून पर्यावरण चल लोड करा
   load_dotenv()

   # GITHUB_TOKEN चल ऍक्सेस करा
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

इतकंच! तुम्ही यशस्वीरित्या `.env` फाइल तयार केली, तुमचा GitHub टोकन जोडला आणि ते तुमच्या Python अ‍ॅप्लिकेशनमध्ये लोड केले.

## तुमच्या संगणकावर स्थानिक पद्धतीने कसे चालवायचे

कोड स्थानिकरित्या चालवण्यासाठी, तुमच्या संगणकावर [Python ची एखादी आवृत्ती स्थापित](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) असणे आवश्यक आहे.

नंतर, रेपॉजिटरी वापरण्यासाठी, तुम्हाला ते क्लोन करावे लागेल:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एकदा सर्व काही तपासले की, तुम्ही सुरुवात करू शकता!

## ऐच्छिक चरण

### Miniconda स्थापित करणे

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हा [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python आणि काही पॅकेजेस स्थापित करण्यासाठी हलका इंस्टॉलर आहे.
Conda स्वतः एक पॅकेज मॅनेजर आहे, ज्यामुळे वेगवेगळ्या Python [**व्हर्च्युअल एन्व्हायर्नमेंट्स**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेसची सोपी सेटअप आणि व्यवस्थापन करता येते. `pip` द्वारे उपलब्ध नसलेल्या पॅकेजेससाठी देखील हे मदत करते.

तुम्ही [MiniConda ची इन्स्टॉलेशन मार्गदर्शिका](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) यांचे अनुसरण करू शकता.

Miniconda स्थापित केल्यावर, तुम्हाला [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) क्लोन करावी लागेल (जर आधी न केले असेल तर)

पुढे, तुम्हाला एक व्हर्च्युअल एन्व्हायर्नमेंट तयार करावी लागेल. Conda वापरून हे करण्यासाठी, नवीन एन्व्हायर्नमेंट फाइल (_environment.yml_) तयार करा. जर तुम्ही Codespaces वापरत असाल तर `.devcontainer` फोल्डरमध्ये हे तयार करा म्हणजे `.devcontainer/environment.yml`.

खालील तुकडा तुमच्या एन्व्हायर्नमेंट फाइलमध्ये ठेवा:

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

जर तुम्हाला Conda वापरताना त्रुटी येत असतील, तर तुम्ही टर्मिनलमध्ये खालील आदेश वापरून Microsoft AI Libraries हस्तचालन करू शकता.

```
conda install -c microsoft azure-ai-ml
```

एन्व्हायर्नमेंट फाइलमध्ये आवश्यक अवलंबित्वे नमूद आहेत. `<environment-name>` म्हणजे तुम्हाला वापरायचे Conda एन्व्हायर्नमेंटचे नाव, आणि `<python-version>` म्हणजे वापरायचा Python चा आवृत्ती, उदा., `3` ही Python ची नवीनतम मुख्य आवृत्ती आहे.

हे केल्यानंतर, तुम्ही खालील कमांड्स टर्मिनलमध्ये चालवून तुमचे Conda एन्व्हायर्नमेंट तयार करू शकता:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उपपथ फक्त Codespace सेटअपसाठी लागू आहे
conda activate ai4beg
```

कुठलीही अडचण आल्यास, [Conda एन्व्हायर्नमेंट्स मार्गदर्शिका](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा.

### Visual Studio Code सोबत Python सपोर्ट एक्स्टेंशन वापरणे

आम्ही या कोर्ससाठी [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) एडिटर आणि [Python सपोर्ट एक्स्टेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) वापरण्याची शिफारस करतो. हे केवळ शिफारस आहे, नक्की गरज नाही.

> **टीप**: कोर्स रेपॉजिटरी VS Code मध्ये उघडल्यावर, तुम्हाला प्रोजेक्ट कंटेनरमध्ये सेट करण्याचा पर्याय मिळतो. कारण कोर्स रेपॉजिटरीमध्ये [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) डायरेक्टरी आहे. याबद्दल नंतर अधिक माहिती.

> **टीप**: रेपॉजिटरी क्लोन करून VS Code मध्ये उघडल्यावर, तो आपोआप Python सपोर्ट एक्स्टेंशन इन्स्टॉल करण्याचा सल्ला देईल.

> **टीप**: जर VS Code तुम्हाला रेपॉजिटरी कंटेनरमध्ये पुन्हा उघडण्याचा प्रस्ताव देत असेल, तर स्थानिकरित्या इन्स्टॉल केलेला Python वापरण्यासाठी हा प्रस्ताव नाकारावा.

### ब्राउझरमध्ये Jupyter वापरणे

तुम्ही [Jupyter पर्यावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ब्राउझरमध्ये थेट वापरून प्रोजेक्टवर काम करू शकता. क्लासिक Jupyter आणि [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोन्ही एक सुंदर डेव्हलपमेंट पर्यावरण देतात जसे की ऑटो-कंप्लीशन, कोड हायलाइटिंग इत्यादी.

स्थानिकरित्या Jupyter सुरू करण्यासाठी, टर्मिनल/कमांड लाईनवर जा, कोर्स डायरेक्टरीमध्ये नेव्हिगेट करा आणि हे चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

हे Jupyter इंस्टन्स सुरू करेल आणि त्याचा URL कमांड लाईन विंडोमध्ये दिसेल.

URL मध्ये प्रवेश केल्यावर, तुम्हाला कोर्स रेखाचित्र दिसेल आणि कोणतीही `*.ipynb` फाइल उघडता येईल. उदाहरणार्थ, `08-building-search-applications/python/oai-solution.ipynb`.

### कंटेनरमध्ये चालवणे

तुमच्या संगणकावर किंवा Codespace वर सगळं सेटअप करण्याऐवजी [कंटेनर](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) वापरण्याचा पर्याय आहे. कोर्स रेपॉजिटरीतील विशेष `.devcontainer` फोल्डरमुळे VS Code प्रोजेक्ट कंटेनरमध्ये सेट करू शकते. Codespaces व्यतिरिक्त, यासाठी Docker इन्स्टॉल करणे गरजेचे आहे, आणि थोडे काम आहे, त्यामुळे हा पर्याय कंटेनर वापराचा अनुभव असलेल्या लोकांसाठीच सुचवतो.

GitHub Codespaces वापरताना API कीज सुरक्षित ठेवण्याचे सर्वोत्तम मार्गांपैकी एक म्हणजे Codespace Secrets वापरणे. कृपया [Codespaces गुपित व्यवस्थापन](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) मार्गदर्शक वाचा.

## धड्यांचा आणि तांत्रिक आवश्यकता

कोर्समध्ये 6 संकल्पनात्मक धडे आणि 6 कोडिंग धडे आहेत.

कोडिंग धड्यांसाठी, आम्ही Azure OpenAI सेवा वापरत आहोत. तुम्हाला Azure OpenAI सेवेसाठी प्रवेश आणि API कीची गरज आहे. तुम्ही [हा अर्ज पूर्ण करून](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) प्रवेश मिळवू शकता.

अप्लिकेशन प्रक्रियेची वाट पाहत असताना, प्रत्येक कोडिंग धड्यात `README.md` फाइल असते जिथे तुम्ही कोड आणि आउटपुट बघू शकता.

## Azure OpenAI सेवा प्रथमच वापरत आहात का?

जर तुम्ही Azure OpenAI सेवा प्रथमच वापरत असाल, तर कृपया [Azure OpenAI सेवा रिसोर्स कसे तयार करायचे आणि डिप्लॉय करायचे याबाबत मार्गदर्शक](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) फॉलो करा.

## OpenAI API प्रथमच वापरत आहात का?

जर तुम्ही OpenAI API प्रथमच वापरत असाल, तर कृपया [इंटरफेस कसे तयार करायचे आणि वापरायचे](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) मार्गदर्शक वाचा.

## इतर शिकणाऱ्यांशी भेटा

आम्ही आमच्या अधिकृत [AI Community Discord सर्व्हर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मध्ये इतर शिकणाऱ्यांसाठी चॅनेल तयार केले आहेत. हे समान आवडीच्या उद्योजक, बांधकाम करणारे, विद्यार्थी आणि जनरेटिव्ह AI साठी पुढे जाण्याची इच्छा असलेल्या लोकांसह नेटवर्किंग करण्याचा उत्तम मार्ग आहे.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टीम देखील या Discord सर्व्हरवर शिकणाऱ्यांना मदत करण्यासाठी असेल.

## योगदान द्या

हा कोर्स एक ओपन-सोर्स उपक्रम आहे. तुम्हाला सुधारणा किंवा समस्या दिसल्यास, कृपया [Pull Request तयार करा](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) किंवा [GitHub इश्यू नोंदवा](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

प्रोजेक्ट टीम सर्व योगदानांचे निरीक्षण करेल. ओपन सोर्समध्ये योगदान देणे जनरेटिव्ह AI मध्ये तुमचा करिअर बनवण्याचा एक उत्कृष्ट मार्ग आहे.

बहुतेक योगदानांसाठी तुम्हाला Contributor License Agreement (CLA) सहमत होणे आवश्यक आहे ज्यामध्ये तुम्ही दावा करता की तुम्हाला योगदान वापरण्याचा योग्य अधिकार आहे. तपशीलासाठी, [CLA, Contributor License Agreement संकेतस्थळ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) भेट द्या.

महत्त्वाचे: या repo मधील मजकूराचा अनुवाद करताना, कृपया मशीन अनुवाद वापरू नका. आम्ही समुदायाद्वारे अनुवादांची पडताळणी करू, त्यामुळे कृपया तुम्हाला पारंगत असलेल्या भाषांसाठीच अनुवादासाठी स्वयंसेवा करा.

तुम्ही पुश रिक्वेस्ट सबमिट करताना, CLA-बॉट आपोआप ठरवेल की तुम्हाला CLA पुरवण्याची गरज आहे की नाही आणि PR योग्यरित्या सजवेल (उदा. लेबल, कमेंट). दिलेल्या सूचनांचे अनुसरण करा. तुम्हाला हे सर्व्हिसेस चालवणार्‍या सर्व रेपॉजिटरीजसाठी एकदाच करायचे आहे.

हा प्रोजेक्ट [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) स्वीकारतो. अधिक माहितीसाठी Code of Conduct FAQ वाचा किंवा कोणत्याही अतिरिक्त प्रश्नांसाठी [Email opencode](opencode@microsoft.com) ला संपर्क करा.

## चला सुरू करूया
आता जेव्हा तुम्ही हा कोर्स पूर्ण करण्यासाठी आवश्यक पावलां पूर्ण केले आहेत, तेव्हा चला सुरुवात करूया [Generative AI आणि LLMs ची ओळख](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) मिळवून.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवेद्वारे अनुवादित केला आहे [Co-op Translator](https://github.com/Azure/co-op-translator). आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा चुका असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वपूर्ण माहिती साठी व्यावसायिक मानव भाषांतर शिफारस केली जाते. या भाषांतराचा वापर करून होणाऱ्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थसंग्रहासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->