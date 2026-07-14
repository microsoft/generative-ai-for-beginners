# या अभ्यासक्रमासह सुरू करणे

तुम्ही हा अभ्यासक्रम सुरू करून आणि जनरेटिव्ह AI सह काय तयार करण्यास प्रेरित होता, हे पाहण्यास आम्हाला खूप आनंद होत आहे!

तुमच्या यशासाठी, या पृष्ठावर सेटअप चरण, तांत्रिक आवश्यकता आणि आवश्यक असल्यास मदत कुठे मिळेल याचे वर्णन केले आहे.

## सेटअप चरण

हा अभ्यासक्रम सुरू करण्यासाठी, तुम्हाला खालील चरण पूर्ण करावे लागतील.

### 1. हा रिपॉ Fork करा

[हा संपूर्ण रिपॉ Fork करा](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) तुमच्या स्वत: च्या GitHub खात्यात जेणेकरून कोणताही कोड बदलू शकता आणि आव्हाने पूर्ण करू शकता. तुम्ही तसेच [हा रिपॉ स्टार (🌟) करू शकता](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ज्यामुळे तो आणि संबंधित रिपॉ सापडणे सोपे होते.

### 2. कोडस्पेस तयार करा

कोड चालवताना कोणत्याही अवलंबित्व समस्या टाळण्यासाठी, आम्ही शिफारस करतो की हा अभ्यासक्रम [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मध्ये चालवा.

तुमच्या Fork मध्ये: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/mr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 एक गुपित जोडा

1. ⚙️ गियर आयकॉन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाव OPENAI_API_KEY, तुमची की पेस्ट करा, जतन करा.

### 3. पुढे काय?

| मला… हवे आहे        | येथे जा…                                                                |
|---------------------|-------------------------------------------------------------------------|
| धडा 1 सुरू करा       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| ऑफलाइन काम करा      | [`setup-local.md`](02-setup-local.md)                                  |
| LLM प्रदाते सेट करा  | [`providers.md`](03-providers.md)                                      |
| इतर शिकणाऱ्यांना भेटा | [आमच्या Discord मध्ये सामील व्हा](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## समस्या निवारण


| लक्षण                                   | उपाय                                                         |
|-------------------------------------------|---------------------------------------------------------------|
| कंटेनर बिल्ड 10 मिनिटांपेक्षा जास्त अडकलेले | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | टर्मिनल जोडले गेले नाही; **+** क्लिक करा ➜ *bash*                |
| OpenAI कडून `401 Unauthorized`            | चुकीचा / कालबाह्य `OPENAI_API_KEY`                           |
| VS Code मध्ये “Dev container mounting…” दर्शविते | ब्राउजर टॅब रीफ्रेश करा—Codespaces कधी कधी कनेक्शन गमावते        |
| नोटबुक कर्नेल गायब आहे                  | नोटबुक मेनू ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-आधारित प्रणाली:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल संपादित करा**: `.env` फाइल एखाद्या टेक्स्ट संपादकात उघडा (उदा. VS Code, Notepad++, किंवा इतर कोणताही संपादक). फाईलमध्ये खालील ओळी जोडा, तुमच्या Microsoft Foundry Models एंडपॉइंट आणि की ने बदलून (कसे मिळवायचे यासाठी पहिले [`providers.md`](03-providers.md) पहा):

   > **टिप:** GitHub Models (आणि त्याचा `GITHUB_TOKEN` व्हेरिएबल) जुलै 2026 अखेरीस रिटायर होत आहे. त्याऐवजी [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) वापरा.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **फाइल जतन करा**: बदल जतन करा आणि टेक्स्ट संपादक बंद करा.

5. **`python-dotenv` इंस्टॉल करा**: जर तुम्ही आधीच केले नसेल तर, `.env` फाइलमधील एनवायरनमेंट व्हेरिएबल्स तुमच्या Python ॲप्लिकेशनमध्ये लोड करण्यासाठी `python-dotenv` पॅकेज इंस्टॉल करावे लागेल. तुम्ही `pip` वापरून ते इंस्टॉल करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **तुमच्या Python स्क्रिप्ट मध्ये एनवायरनमेंट व्हेरिएबल्स लोड करा**: तुमच्या Python स्क्रिप्टमध्ये, `.env` फाइलमधून एनवायरनमेंट व्हेरिएबल्स लोड करण्यासाठी `python-dotenv` पॅकेज वापरा:

   ```python
   from dotenv import load_dotenv
   import os

   # .env फायलीतून पर्यावरण व्हेअरीएबल्स लोड करा
   load_dotenv()

   # Microsoft Foundry मॉडेल्स व्हेअरीएबल्स प्रवेश करा
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

एवढंच! तुम्ही यशस्वीरित्या `.env` फाइल तयार केली, Microsoft Foundry Models चे क्रेडेन्शियल्स जोडले, आणि त्यांना तुमच्या Python ॲप्लिकेशनमध्ये लोड केले.

## तुमच्या संगणकावर स्थानिकरित्या कसे चालवायचे

कोड स्थानिकरित्या तुमच्या संगणकावर चालवण्यासाठी, तुमच्याकडे [Python ची काही आवृत्ती स्थापित](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) असावी लागेल.

मग रेजिस्ट्री वापरण्यासाठी, तुम्हाला ती क्लोन करावी लागेल:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

सर्व काही तपासल्यानंतर, तुम्ही सुरू करू शकता!

## ऐच्छिक चरण

### मिनिकोंडा स्थापित करणे

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हा Conda, Python आणि काही पॅकेजेस इंस्टॉल करण्यासाठी एक हलका इंस्टॉलर आहे.
Conda म्हणजे एक पॅकेज मॅनेजर जो विविध Python [**आभासी वातावरणांमध्ये**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेसमध्ये सेटअप आणि स्विच करणे सोपे करते. तसेच, ज्यांना `pip` द्वारे उपलब्ध नसलेले पॅकेजेस इंस्टॉल करायचे असतील त्यांच्या साठी उपयुक्त आहे.

तुम्ही [MiniConda इंस्टॉलेशन मार्गदर्शक](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) फॉलो करू शकता.

Miniconda स्थापित केल्यावर, तुम्हाला [रेपॉ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) क्लोन करावी लागेल (जर आधी केले नसेल तर)

नंतर, तुम्हाला आभासी वातावरण तयार करावे लागेल. Conda सह हे करण्यासाठी, एक नवीन वातावरण फाइल (_environment.yml_) तयार करा. जर तुम्ही Codespaces वापरत असाल तर हे `.devcontainer` निर्देशिकेमध्ये तयार करा, म्हणजे `.devcontainer/environment.yml`.

खालील स्निपेटने तुमची वातावरण फाइल भरून द्या:

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

जर conda वापरून त्रुटी येत असतील तर तुम्ही खालील कमांडने Microsoft AI लायब्ररी मॅन्युअली इंस्टॉल करू शकता.

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइल हवी असलेली अवलंबित्वे निर्दिष्ट करते. `<environment-name>` म्हणजे तुम्ही तुमच्या Conda वातावरणासाठी वापरू इच्छित असलेले नाव, आणि `<python-version>` हा Python ची तुम्हाला हवा असलेला व्हर्जन आहे, उदा. `3` हा Python चा नवीनतम प्रमुख व्हर्जन आहे.

हे पूर्ण झाल्यावर, खालील कमांड्स वापरून तुमचे Conda वातावरण तयार करा:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer उप पथ फक्त Codespace सेटअपसाठी लागू आहे
conda activate ai4beg
```

काही अडचणी आल्यास [Conda environments मार्गदर्शिका](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पाहा.

### Python सपोर्ट विस्तारासहित Visual Studio Code वापररणे

या अभ्यासक्रमासाठी आम्ही [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) संपादकाचा आणि [Python सपोर्ट विस्तार](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) चा वापर करण्याची शिफारस करतो. मात्र, ही एक शिफारस आहे, नक्की गरज नाही.

> **टीप**: कोर्स रिपॉजिटरी VS Code मध्ये उघडल्यावर, तुमच्याकडे प्रोजेक्ट कंटेनर मध्ये सेट करण्याचा पर्याय असतो. कारण [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) निर्देशिका आहे. याबद्दल नंतर अधिक माहिती.

> **टीप**: एकदा तुम्ही रिपॉजिटरी क्लोन आणि VS Code मध्ये उघडलात, ते आपोआप तुम्हाला Python सपोर्ट विस्तार इंस्टॉल करण्याचा सल्ला देईल.

> **टीप**: VS Code तुम्हाला कंटेनरमध्ये रिपॉजिटरी पुन्हा उघडण्याचा सल्ला दिल्यास, स्थानिकरित्या स्थापित Python वापरण्यासाठी हा विनंती नाकारावी.

### ब्राउजरमध्ये Jupyter वापरणे

तुम्ही प्रकल्पावर [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) वापरून थेट तुमच्या ब्राउजरमध्ये काम करू शकता. क्लासिक Jupyter आणि [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोन्ही एक आनंददायी विकास वातावरण पुरवतात ज्यात ऑटो-कंप्लीशन, कोड हायलाइटिंग सारख्या वैशिष्ट्यांचा समावेश आहे.

Jupyter स्थानिकरित्या सुरू करण्यासाठी, टर्मिनल/कमान्ड लाइन वर जा, अभ्यासक्रम निर्देशिकेत जा, आणि चालवा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

यामुळे Jupyter इंस्टन्स सुरू होईल आणि त्याचा प्रवेश URL कमाण्ड लाइन विंडो मध्ये दाखवला जाईल.

URL वर प्रवेश केल्यावर, तुम्हाला अभ्यासक्रमाचे आराखडा दिसेल आणि तुम्ही कोणतीही `*.ipynb` फाइलमध्ये जाऊ शकता. उदाहरणार्थ, `08-building-search-applications/python/oai-solution.ipynb`.

### कंटेनरमध्ये चालवणे

तुमच्या संगणकावर किंवा Codespace वर सर्व काही सेट करण्याचा एक पर्याय म्हणजे [कंटेनर वापरणे](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). हा अभ्यासक्रम रिपॉजिटरीतील खास `.devcontainer` फोल्डर मुळे VS Code प्रोजेक्ट कंटेनरमध्ये सेट करू शकतो. Codespaces वगळता, यासाठी Docker स्थापित करावा लागेल आणि हे थोडं कामाचे आहे, त्यामुळे कंटेनरवर काम करण्याचा अनुभव असलेल्या लोकांसाठीच आम्ही शिफारस करतो.

GitHub Codespaces वापरताना तुमच्या API की सुरक्षित ठेवण्याचा एक सर्वोत्तम मार्ग म्हणजे Codespace Secrets वापरणे. कृपया [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) मार्गदर्शकाचा वापर करा.


## धडे आणि तांत्रिक आवश्यकता

या अभ्यासक्रमात 6 संकल्पना धडे आणि 6 कोडिंग धडे आहेत.

कोडिंग धड्यासाठी, आम्ही Azure OpenAI सेवा वापरत आहोत. तुम्हाला Azure OpenAI सेवा आणि API की लागेल कोड चालवण्यासाठी. तुम्ही [हा अर्ज पूर्ण करून](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) प्रवेश मिळवू शकता.

तुमचा अर्ज प्रक्रियेत असतानाच, प्रत्येक कोडिंग धडकडे एक `README.md` फाइल देखील आहे जिथे तुम्ही कोड आणि उत्पादन पाहू शकता.

## प्रथमच Azure OpenAI सेवा वापरत असल्यास

तुम्ही Azure OpenAI सेवा प्रथमच वापरत असाल, तर कृपया [Azure OpenAI सेवा रिसोर्स तयार आणि तैनात करण्याचा](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) मार्गदर्शक फॉलो करा.

## प्रथमच OpenAI API वापरत असल्यास

जर तुम्ही OpenAI API प्रथमच वापरत असाल, तर कृपया [इंटरफेस तयार करण्याचा आणि वापरण्याचा](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) मार्गदर्शक फॉलो करा.

## इतर शिकणाऱ्यांना भेटा

आम्ही आमच्या अधिकृत [AI Community Discord सर्व्हर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मध्ये इतर शिकणाऱ्यांशी भेटण्यासाठी चॅनेल तयार केले आहेत. हे जेनरेटिव्ह AI मध्ये प्राविण्य मिळवण्याच्या इच्छुक उद्योजक, बिल्डर्स, विद्यार्थी आणि इतरांसोबत जाळे विस्तारण्याचा उत्तम मार्ग आहे.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रकल्प संघ देखील या Discord सर्व्हरवर शिकणाऱ्यांना मदत करण्यासाठी असेल.

## योगदान करा

हा अभ्यासक्रम एक खुला स्रोत उपक्रम आहे. जर तुम्हाला सुधारणा किंवा समस्या दिसल्या, तर कृपया [Pull Request तयार करा](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) किंवा [GitHub issue नोंदवा](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

प्रकल्प संघ सर्व योगदानांचे निरीक्षण करेल. खुल्या स्रोतात योगदान देणे हे जेनरेटिव्ह AI मध्ये तुमचा करिअर घडवण्याचा एक उत्कृष्ट मार्ग आहे.

बहुतेक योगदानांसाठी तुम्हाला Contributor License Agreement (CLA) मान्य करावा लागेल ज्यात तुम्ही हे घोषित करता की तुम्हाला तुमच्या योगदानाचा वापर करण्याचा अधिकार आहे आणि तुम्ही तो आम्हाला वापरण्याचा अधिकार द्याल. तपशीलांसाठी, [CLA, Contributor License Agreement वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) पहा.

महत्त्वाचे: या रिपॉजिटरीमधील मजकूर भाषांतर करताना कृपया मशीन अनुवाद वापरू नका. आम्ही समुदायाद्वारे भाषांतरांची पडताळणी करू, त्यामुळे फक्त त्या भाषांमध्ये प्रवीण असाल त्या भाषांतरासाठी स्वयंसेवा करा.

जेव्हा तुम्ही पुल विनंती सबमिट करता, तेव्हा CLA-бот आपोआप ठरवेल की तुम्हाला CLA प्रदान करायची गरज आहे का आणि PR योग्य त्या लेबल/कमेंटसह सजवेल. फक्त बोटने दिलेल्या सूचनांचे पालन करा. एकदाच सर्व रिपॉजिटरीजमध्ये हा प्रोसेस करावा लागेल.


या प्रोजेक्टने [मायक्रोसॉफ्ट मुक्त स्रोत आचार संहिता](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) स्वीकारली आहे. अधिक माहितीसाठी आचार संहिता FAQ वाचा किंवा कोणत्याही अतिरिक्त प्रश्नांसाठी किंवा अभिप्रायांसाठी [Email opencode](opencode@microsoft.com) शी संपर्क साधा.

## चला सुरू करूया

आता आपण या कोर्सच्या आवश्यक पायऱ्या पूर्ण केल्या आहेत, तर चला [जनरेटिव्ह AI आणि LLMs चा परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) घेऊन सुरू करूया.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->