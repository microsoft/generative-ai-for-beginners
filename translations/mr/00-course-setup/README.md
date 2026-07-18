# या कोर्ससह सुरूवात करणे

आम्ही तुम्हाला हा कोर्स सुरू करताना आणि तुम्ही जनरेटिव्ह AI सह काय तयार कराल हे पाहताना अत्यंत उत्साहित आहोत!

तुमच्या यशासाठी, या पृष्ठावर सेटअप पावले, तांत्रिक आवश्यकता, आणि आवश्यक असल्यास मदत कुठे मिळेल हे स्पष्ट केले आहे.

## सेटअप पावले

हा कोर्स सुरू करण्यासाठी, तुम्हाला खालील पावले पूर्ण करावी लागतील.

### 1. हा रेपो Fork करा

[हा संपूर्ण रेपो Fork करा](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तुमच्या स्वतःच्या GitHub खात्यावर जेणेकरून तुम्ही कोणताही कोड बदलू शकता आणि आव्हाने पूर्ण करू शकता. तुम्ही हा रेपो आणि संबंधित रेपोज शोधण्यासाठी [स्टार (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) देखील देऊ शकता.

### 2. कोडस्पेस तयार करा

कोड चालवताना कोणत्याही अवलंबित्वाच्या समस्या टाळण्यासाठी, आम्ही शिफारस करतो की तुम्ही हा कोर्स [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मध्ये चालवा.

आपल्या Fork मध्ये: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/mr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 एक गुपित जोडा

1. ⚙️ गियर आयकॉन -> कमांड पॅलेट -> Codespaces : Manage user secret -> नव्या गुपित जोडा.
2. नाव OPENAI_API_KEY, तुमचा की पेस्ट करा, जतन करा.

### 3. पुढे काय?

| मला काय करायचंय…        | येथे जा…                                                            |
|------------------------|--------------------------------------------------------------------|
| धडा 1 सुरू करा          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ऑफलाइन काम करा         | [`setup-local.md`](02-setup-local.md)                                   |
| LLM प्रदाता सेटअप करा   | [`providers.md`](03-providers.md)                                        |
| इतर शिकणाऱ्यांना भेटा   | [आमच्या Discord मध्ये सामील व्हा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## समस्या निराकरण


| लक्षण                                   | निराकरण                                                       |
|---------------------------------------|---------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनिटांपेक्षा जास्त अडकला | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`              | टर्मिनल जोडले नाही; **+** क्लिक करा ➜ *bash*                   |
| OpenAI कडून `401 Unauthorized`           | चुकीचा / कालबाह्य `OPENAI_API_KEY`                          |
| VS Code “Dev container mounting…” दाखवतो | ब्राउझर टॅब रिफ्रेश करा—Codespaces कधी कधी कनेक्शन गमावतो   |
| नोटबुक कर्नल गायब                     | नोटबुक मेन्यू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-आधारित सिस्टमसाठी:

   ```bash
   touch .env
   ```

   Windows साठी:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल संपादित करा**: `.env` फाइल टेक्स्ट एडिटरमध्ये (जसे VS Code, Notepad++, किंवा इतर कोणताही) उघडा. खालील ओळ तुमच्या Microsoft Foundry Models चे एंडपॉइंट आणि कीसह फाइलमध्ये जोडा (हे कसे मिळवायचे ते पाहण्यासाठी [`providers.md`](03-providers.md) पहा):

   > **टीप:** GitHub Models (आणि त्याचा `GITHUB_TOKEN` व्हेरिएबल) जुलै 2026 च्या शेवटी बंद होणार आहे. त्याऐवजी [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) वापरा.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फाइल जतन करा**: बदल जतन करून टेक्स्ट एडिटर बंद करा.

5. **`python-dotenv` इंस्टॉल करा**: जर तुम्ही आधीपासून न केल्यास, `.env` फाइलमधील पर्यावरण व्हेरिएबल्स तुमच्या Python अ‍ॅप्लिकेशनमध्ये लोड करण्यासाठी `python-dotenv` पॅकेज इंस्टॉल करावे लागेल. तुम्ही `pip` वापरून हे इंस्टॉल करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **तुमच्या Python स्क्रिप्टमध्ये पर्यावरण व्हेरिएबल्स लोड करा**: तुमच्या Python स्क्रिप्टमध्ये, `.env` फाइलमधील व्हेरिएबल्स लोड करण्यासाठी `python-dotenv` पॅकेज वापरा:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फाईलमधून पर्यावरण चल वाचा
   load_dotenv()

   # Microsoft Foundry Models चलांना प्रवेश करा
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

एवढेच! तुम्ही यशस्वीपणे `.env` फाइल तयार केली आहे, तुमचे Microsoft Foundry Models क्रेडेन्शियल्स जोडले आहेत आणि त्यांना Python अ‍ॅप्लिकेशनमध्ये लोड केले आहे.

## तुमच्या संगणकावर लोकली कसे चालवायचे

कोड तुमच्या संगणकावर लोकली चालविण्यासाठी, तुम्हाला काही आवृत्तीचे [Python इंस्टॉल करणे](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) आवश्यक आहे.

नंतर रेपॉजिटरी वापरण्यासाठी, तुम्हाला ते क्लोन करावे लागेल:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एकदा सगळे चेकआउट केल्यावर, तुम्ही सुरुवात करू शकता!

## पर्यायी पावले

### Miniconda इंस्टॉल करणे

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हा [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python आणि काही पॅकेजेस इंस्टॉल करण्यासाठी एक हलका इंस्टॉलर आहे.
Conda हा एक पॅकेज मॅनेजर आहे, जो विविध Python [**व्हर्चुअल एन्व्हायर्नमेंट्स**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेस सेटअप करणे आणि स्विच करणे सुलभ करतो. तसेच काही पॅकेजेस जे `pip` द्वारे उपलब्ध नाहीत, ते इंस्टॉल करण्यासाठी उपयुक्त आहे.

तुम्ही [MiniConda इंस्टॉलेशन गाइड](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) अनुसरू शकता.

Miniconda इंस्टॉल केल्यावर, तुम्हाला रेपॉजिटरी क्लोन करावी लागेल (जर तुम्ही आधीच केले नसेल तर) [रेपॉजिटरी](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst).

पुढे, तुम्हाला एक व्हर्चुअल एन्व्हायर्नमेंट तयार करावी लागेल. Conda वापरून हे करण्यासाठी, एका नवीन एन्भायर्नमेंट फाइल (_environment.yml_) तयार करा. जर तुम्ही Codespaces वापरत असाल तर ती `.devcontainer` डायरेक्टरीमध्ये तयार करा, म्हणजे `.devcontainer/environment.yml`.

खालील कोड स्निपेटने तुमची एन्व्हायर्नमेंट फाइल भरून ठेवा:

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

जर तुम्हाला conda वापरताना त्रुटी येत असतील तर तुम्ही खालील कमांडने Microsoft AI Libraries manually इंस्टॉल करू शकता.

```
conda install -c microsoft azure-ai-ml
```

एन्व्हायर्नमेंट फाइलमध्ये आपल्याला आवश्यक अवलंबित्वे नमूद केली आहेत. `<environment-name>` हे तुमच्या Conda एन्व्हायर्नमेंटचे नाव असून, `<python-version>` ही Python ची आवृत्ती आहे जी तुम्हाला वापरायची आहे, उदाहरणार्थ, `3` ही Python ची नवीनतम मुख्य आवृत्ती आहे.

आता, खालील कमांड्स चालवून तुमची Conda एन्व्हायर्नमेंट तयार करा:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उपपथ फक्त Codespace सेटअपसाठी लागू होते
conda activate ai4beg
```

काही समस्या आल्यास [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा.

### Python सपोर्ट एक्स्टेंशनसह Visual Studio Code वापरणे

या कोर्ससाठी आमच्या शिफारशीमध्ये [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) एडिटर आणि [Python सपोर्ट एक्स्टेंशन](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) चा समावेश आहे. मात्र ही केवळ शिफारस आहे, नक्की गरज नाही.

> **टीप:** कोर्स रेपॉजिटरी VS Code मध्ये उघडल्यानंतर, तुम्हाला प्रोजेक्ट कंटेनरमध्ये सेटअप करण्याचा पर्याय मिळेल. ते कारण म्हणजे कोर्स रेपॉजिटरीमध्ये [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) फोल्डर आहे. याबद्दल खाली अधिक माहिती आहे.

> **टीप:** रेपॉजिटरी क्लोन आणि VS Code मध्ये उघडल्यावर, तो आपोआप तुम्हाला Python सपोर्ट एक्स्टेंशन इंस्टॉल करण्याचा प्रस्ताव देतो.

> **टीप:** जर VS Code तुम्हाला रेपो कंटेनरमध्ये पुन्हा उघडण्याचा प्रस्ताव दिला, तर तो नाकारून लोकली इंस्टॉल केलेला Python वापरा.

### ब्राउझरमध्ये Jupyter वापरणे

तुम्ही प्रोजेक्ट ब्राउझरमध्येच [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) वापरून देखील काम करू शकता. पारंपरिक Jupyter आणि [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोघेही ऑटो-कम्प्लीशन, कोड हायलाइटिंग अशा सुविधांसह छान विकास वातावरण पुरवतात.

लोकली Jupyter सुरू करण्यासाठी, टर्मिनल/कमांड लाईनमध्ये जा, कोर्स डायरेक्टरीमध्ये जा, आणि हे चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

ही Jupyter इन्स्टन्स सुरू करेल आणि त्याचा URL कमांड लाइन विंडोमध्ये दिसेल.

URL ऍक्सेस केल्यावर, तुम्हाला कोर्सचे आऊटलाइन दिसेल आणि तुम्ही कोणत्याही `*.ipynb` फाइलवर जाऊ शकता. उदा., `08-building-search-applications/python/oai-solution.ipynb`.

### कंटेनरमध्ये चालवणे

संगणकावर किंवा Codespace वर सगळे सेटअप करण्याचा पर्याय म्हणजे [कंटेनर](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) वापरणे. कोर्स रेपॉजिटरीमधील `.devcontainer` फोल्डर VS Code ला प्रोजेक्ट कंटेनरमध्ये सेटअप करण्यास मदत करतो. Codespaces व्यतिरिक्त, यासाठी Docker इंस्टॉल करावा लागेल, आणि थोडा काम लागतो, म्हणून कंटेनर काम करता येणाऱ्यांसाठीच याची शिफारस करतो.

GitHub Codespaces मध्ये API की सुरक्षित ठेवण्याचा सर्वोत्तम मार्ग म्हणजे Codespace Secrets वापरणे. यासाठी कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) मार्गदर्शक वाचा.


## धडे आणि तांत्रिक आवश्यकता

कोर्समध्ये "Learn" धडे आहेत जे जनरेटिव्ह AI संकल्पना समजावतात आणि "Build" धडे आहेत ज्यात शक्य असल्यास **Python** आणि **TypeScript** मध्ये प्रत्यक्ष कोड उदाहरणे आहेत.

कोडिंग धड्यांसाठी, आम्ही Microsoft Foundry मध्ये Azure OpenAI वापरतो. तुम्हाला Azure सबस्क्रिप्शन व API की लागेल. प्रवेश खुला आहे - कोणतीही अर्ज करण्याची गरज नाही - म्हणून तुम्ही [Microsoft Foundry रिसोर्स तयार करा आणि मॉडेल तैनात करा](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) आणि एंडपॉइंट व की मिळवा.

प्रत्येक कोडिंग धड्याबरोबर `README.md` फाइल असते, जी कोड आणि आउटपुट रन न करता पाहता येते.

## प्रथमच Azure OpenAI सेवा वापरताना

जर तुम्ही प्रथमच Azure OpenAI सेवा वापरत असाल, तर कृपया [Azure OpenAI सेवा रिसोर्स तयार करणे आणि तैनात करणे](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) मार्गदर्शक फॉलो करा.

## प्रथमच OpenAI API वापरताना

जर तुम्ही प्रथमच OpenAI API वापरत असाल, तर कृपया [Interface तयार करणे आणि वापरणे](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) मार्गदर्शक फॉलो करा.

## इतर शिकणाऱ्यांना भेटा

आम्ही अधिक शिकणाऱ्यांना भेटण्यासाठी आमच्या अधिकृत [AI Community Discord सर्व्हर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मध्ये चॅनेल तयार केले आहेत. हे इतर समान विचारसरणीच्या उद्योजक, निर्मात्या, विद्यार्थ्यांशी नेटवर्किंग करण्याचा उत्तम मार्ग आहे आणि जनरेटिव्ह AI मध्ये वाढ करण्यासाठी उपयुक्त आहे.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रोजेक्ट टीमही या Discord सर्व्हरवर शिकणाऱ्यांना मदत करण्यासाठी असेल.

## योगदान द्या

हा कोर्स एक ओपन-सोर्स उपक्रम आहे. तुम्हाला सुधारणा किंवा समस्या दिसल्या तर कृपया [Pull Request तयार करा](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) किंवा [GitHub Issue नोंदवा](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

प्रोजेक्ट टीम सर्व योगदानांवर लक्ष ठेवेल. ओपन सोर्स मध्ये योगदान करणे हे जनरेटिव्ह AI मध्ये आपले करिअर घडवण्याचा अद्भुत मार्ग आहे.

बहुतेक योगदानांसाठी तुम्हाला Contributor License Agreement (CLA) सहमत व्हावे लागते ज्यात तुम्ही स्पष्ट करता की तुम्हाला तुमच्या योगदानाचा वापर करण्याचा अधिकार आहे. तपशीलासाठी येथे पहा: [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

महत्त्वाचे: या रेपॉमध्ये मजकूर अनुवाद करताना कृपया मशीन अनुवाद वापरू नका. आम्ही समुदायाद्वारे अनुवादांची तपासणी करू, म्हणून फक्त तुम्हाला चांगल्या प्राविण्य असलेल्या भाषांमध्येच अनुवादासाठी स्वयंसेवक व्हा.


जेव्हा आपण पुल विनंती सादर करता, तेव्हा CLA-बॉट आपोआप ठरवेल की आपल्याला CLA प्रदान करण्याची आवश्यकता आहे का आणि PR योग्यरित्या डेकोरेट करेल (उदा., लेबल, टिप्पण्या). फक्त बॉटद्वारे दिलेल्या सूचनांचे पालन करा. आपल्याला आमच्या CLA वापरणाऱ्या सर्व रेपॉजिटरीमध्ये हे एकदाच करायचे आहे.

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) स्वीकारला आहे. अधिक माहितीसाठी Code of Conduct FAQ वाचा किंवा अतिरिक्त प्रश्न किंवा टिप्पण्या असल्यास [Email opencode](opencode@microsoft.com) शी संपर्क साधा.

## चला सुरू करूया

आता आपण हा कोर्स पूर्ण करण्यासाठी आवश्यक टप्पे पूर्ण केले आहेत, तर चला सुरू करू या [Generative AI आणि LLMs परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) घेऊन.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->