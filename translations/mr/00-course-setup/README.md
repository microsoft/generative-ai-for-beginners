<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:43:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "mr"
}
-->
# या कोर्ससह सुरुवात करणे

तुम्ही हा कोर्स सुरू करत आहात आणि जनरेटिव्ह AI सह तुम्ही काय तयार करण्यासाठी प्रेरित होता हे पाहण्यासाठी आम्हाला खूप आनंद होत आहे!

तुमच्या यशासाठी, या पृष्ठात सेटअप चरण, तांत्रिक आवश्यकता, आणि आवश्यक असल्यास मदत कुठे मिळवायची याचे वर्णन केले आहे.

## सेटअप चरण

हा कोर्स घेण्यास सुरुवात करण्यासाठी, तुम्हाला खालील चरण पूर्ण करणे आवश्यक आहे.

### 1. या रेपोला फोर्क करा

कोणताही कोड बदलण्यासाठी आणि आव्हाने पूर्ण करण्यासाठी तुमच्या स्वतःच्या GitHub खात्यावर [हा संपूर्ण रेपो फोर्क करा](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). तुम्ही याला आणि संबंधित रेपोला सोप्या पद्धतीने शोधण्यासाठी [स्टार (🌟) देखील देऊ शकता](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. कोडस्पेस तयार करा

कोड चालवताना कोणत्याही अवलंबित्व समस्यांना टाळण्यासाठी, आम्ही हा कोर्स [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) मध्ये चालवण्याची शिफारस करतो.

हे तुमच्या फोर्क केलेल्या रेपोच्या आवृत्तीवर `Code` पर्याय निवडून आणि **Codespaces** पर्याय निवडून तयार केले जाऊ शकते.

![कोडस्पेस तयार करण्यासाठी बटण दाखवणारा संवाद](../../../00-course-setup/images/who-will-pay.webp)

### 3. तुमचे API कीज साठवणे

कोणत्याही प्रकारचे अॅप्लिकेशन तयार करताना तुमचे API कीज सुरक्षित ठेवणे महत्वाचे आहे. आम्ही शिफारस करतो की कोणतेही API कीज थेट तुमच्या कोडमध्ये साठवू नका. त्या तपशीलांना सार्वजनिक रेपॉझिटरीमध्ये कमिट करणे सुरक्षा समस्या आणि एखाद्या चुकीच्या व्यक्तीद्वारे वापरल्यास अनावश्यक खर्च होऊ शकतो.
Python साठी `.env` फाइल कशी तयार करावी आणि `GITHUB_TOKEN` जोडण्यासाठी एक स्टेप-बाय-स्टेप मार्गदर्शक येथे आहे:

1. **तुमच्या प्रोजेक्ट निर्देशिकेवर जा**: तुमचे टर्मिनल किंवा कमांड प्रॉम्प्ट उघडा आणि जिथे तुम्हाला `.env` फाइल तयार करायची आहे त्या प्रोजेक्टच्या मूळ निर्देशिकेत जा.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` फाइल तयार करा**: तुमच्या आवडत्या टेक्स्ट एडिटरचा वापर करून `.env` नावाची एक नवीन फाइल तयार करा. जर तुम्ही कमांड लाइन वापरत असाल, तर तुम्ही `touch` (on Unix-based systems) or `echo` (विंडोजवर) वापरू शकता:

   Unix-आधारित प्रणाली:
   ```bash
   touch .env
   ```

   विंडोज:
   ```cmd
   echo . > .env
   ```

3. **`.env` फाइल संपादित करा**: `.env` फाइल टेक्स्ट एडिटरमध्ये (उदा., VS कोड, Notepad++ किंवा इतर कोणताही एडिटर) उघडा. फाइलमध्ये खालील ओळ जोडा, `your_github_token_here` ला तुमच्या वास्तविक GitHub टोकनने बदला:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **फाइल सेव्ह करा**: बदल सेव्ह करा आणि टेक्स्ट एडिटर बंद करा.

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` पॅकेज इन्स्टॉल करा जेणेकरून तुमच्या Python अॅप्लिकेशनमध्ये `.env` फाइलमधून पर्यावरणीय चल लोड करता येईल. तुम्ही `pip` वापरून हे इन्स्टॉल करू शकता:

   ```bash
   pip install python-dotenv
   ```

6. **तुमच्या Python स्क्रिप्टमध्ये पर्यावरणीय चल लोड करा**: तुमच्या Python स्क्रिप्टमध्ये, `.env` फाइलमधून पर्यावरणीय चल लोड करण्यासाठी `python-dotenv` पॅकेज वापरा:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

हेच झाले! तुम्ही यशस्वीरित्या `.env` फाइल तयार केली आहे, तुमचे GitHub टोकन जोडले आहे आणि ते तुमच्या Python अॅप्लिकेशनमध्ये लोड केले आहे.

## तुमच्या संगणकावर स्थानिकरित्या कसे चालवायचे

तुमच्या संगणकावर कोड स्थानिकरित्या चालवण्यासाठी, तुमच्याकडे काही आवृत्ती [Python इन्स्टॉल केलेली](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) असणे आवश्यक आहे.

त्यानंतर रेपो वापरण्यासाठी, तुम्हाला ते क्लोन करावे लागेल:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

एकदा सर्व काही तपासून घेतल्यानंतर, तुम्ही सुरुवात करू शकता!

## पर्यायी चरण

### Miniconda इन्स्टॉल करणे

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) हा [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, तसेच काही पॅकेजेस इन्स्टॉल करण्यासाठी एक हलका इंस्टॉलर आहे.
Conda स्वतः एक पॅकेज मॅनेजर आहे, ज्यामुळे विविध Python [**आभासी वातावरणे**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) आणि पॅकेजेस सेटअप आणि स्विच करणे सोपे होते. हे `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` द्वारे उपलब्ध नसलेल्या पॅकेजेस इन्स्टॉल करण्यासाठी देखील उपयुक्त आहे.

खालील स्निपेटसह तुमची वातावरण फाइल भरण्यासाठी पुढे जा:

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

जर तुम्हाला conda वापरताना त्रुटी आढळल्यास, तुम्ही टर्मिनलमध्ये खालील कमांड वापरून Microsoft AI लायब्ररी मॅन्युअली इन्स्टॉल करू शकता.

```
conda install -c microsoft azure-ai-ml
```

वातावरण फाइल आवश्यक अवलंबित्व निर्दिष्ट करते. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python ची नवीनतम प्रमुख आवृत्ती आहे.

ते पूर्ण झाल्यावर, तुम्ही तुमच्या कमांड लाइन/टर्मिनलमध्ये खालील कमांड चालवून तुमचे Conda वातावरण तयार करू शकता

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

जर तुम्हाला कोणत्याही समस्यांचा सामना करावा लागला तर [Conda वातावरण मार्गदर्शक](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) पहा.

### Python समर्थन विस्तारासह Visual Studio Code वापरणे

आम्ही या कोर्ससाठी [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) संपादक वापरण्याची शिफारस करतो ज्यामध्ये [Python समर्थन विस्तार](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) स्थापित आहे. हे, तथापि, अधिक शिफारस आहे आणि निश्चित आवश्यकता नाही.

> **टीप**: VS कोडमध्ये कोर्स रेपॉझिटरी उघडून, तुम्हाला प्रकल्प कंटेनरमध्ये सेट अप करण्याचा पर्याय आहे. हे कोर्स रेपॉझिटरीमध्ये आढळणाऱ्या [विशेष `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) निर्देशिकेमुळे आहे. याबद्दल अधिक माहिती नंतर.

> **टीप**: एकदा तुम्ही रेपॉझिटरी क्लोन केली आणि VS कोडमध्ये निर्देशिका उघडली की, ते तुम्हाला Python समर्थन विस्तार स्थापित करण्याची आपोआप सूचना देईल.

> **टीप**: जर VS कोड तुम्हाला रेपॉझिटरी कंटेनरमध्ये पुन्हा उघडण्याची सूचना देत असेल, तर स्थानिकरित्या स्थापित केलेल्या Python आवृत्तीचा वापर करण्यासाठी हा विनंती नाकारावी.

### ब्राउझरमध्ये Jupyter वापरणे

तुम्ही तुमच्या ब्राउझरमध्ये [Jupyter वातावरण](https://jupyter.org?WT.mc_id=academic-105485-koreyst) वापरून प्रकल्पावर देखील काम करू शकता. क्लासिक Jupyter आणि [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) दोन्ही ऑटो-कम्प्लीशन, कोड हायलाइटिंग इत्यादी वैशिष्ट्यांसह खूप छान विकास वातावरण प्रदान करतात.

Jupyter स्थानिकरित्या सुरू करण्यासाठी, टर्मिनल/कमांड लाइनवर जा, कोर्स निर्देशिकेकडे जा आणि कार्यान्वित करा:

```bash
jupyter notebook
```

किंवा

```bash
jupyterhub
```

यामुळे Jupyter उदाहरण सुरू होईल आणि त्याचा प्रवेश करण्यासाठी URL कमांड लाइन विंडोमध्ये दर्शविला जाईल.

एकदा तुम्ही URL प्रवेश केल्यावर, तुम्हाला कोर्सची रूपरेषा दिसेल आणि कोणत्याही `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` फाइलवर नेव्हिगेट करण्यास सक्षम असाल जिथे तुम्ही कोड आणि आउटपुट पाहू शकता.

## Azure OpenAI सेवा प्रथमच वापरणे

जर तुम्ही Azure OpenAI सेवा प्रथमच वापरत असाल, तर [Azure OpenAI सेवा संसाधन कसे तयार करावे आणि तैनात करावे](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) याबद्दल हा मार्गदर्शक अनुसरा.

## OpenAI API प्रथमच वापरणे

जर तुम्ही OpenAI API प्रथमच वापरत असाल, तर [इंटरफेस कसे तयार करावे आणि वापरावे](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) याबद्दल मार्गदर्शक अनुसरा.

## इतर शिकणाऱ्यांना भेटा

आम्ही इतर शिकणाऱ्यांना भेटण्यासाठी आमच्या अधिकृत [AI Community Discord सर्व्हर](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) मध्ये चॅनेल तयार केले आहेत. हे समान विचारसरणीच्या उद्योजक, निर्माते, विद्यार्थी आणि जनरेटिव्ह AI मध्ये स्तर वाढवण्याचा प्रयत्न करणाऱ्या कोणाशीही नेटवर्क करण्याचा एक उत्तम मार्ग आहे.

[![डिस्कॉर्ड चॅनेलमध्ये सामील व्हा](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

प्रकल्प टीम देखील कोणत्याही शिकणाऱ्यांना मदत करण्यासाठी या Discord सर्व्हरवर असेल.

## योगदान द्या

हा कोर्स एक ओपन-सोर्स उपक्रम आहे. तुम्हाला सुधारणा किंवा समस्या दिसल्यास, कृपया [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) तयार करा किंवा [GitHub समस्या](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) लॉग करा.

प्रकल्प टीम सर्व योगदानांचे मागोवा ठेवेल. ओपन सोर्सला योगदान देणे हे जनरेटिव्ह AI मध्ये तुमचा करिअर तयार करण्याचा एक अद्भुत मार्ग आहे.

बहुतेक योगदानांमध्ये तुम्हाला योगदानकर्ता परवाना करार (CLA) सहमत होण्याची आवश्यकता आहे, ज्यात तुम्हाला अधिकार आहेत आणि खरोखरच, आम्हाला तुमचे योगदान वापरण्याचे अधिकार देतात. तपशीलांसाठी, [CLA, योगदानकर्ता परवाना करार वेबसाइट](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ला भेट द्या.

महत्वाचे: या रेपोमधील मजकूर अनुवादित करताना, कृपया मशीन अनुवाद वापरू नका याची खात्री करा. आम्ही समुदायाद्वारे अनुवाद सत्यापित करू, त्यामुळे कृपया फक्त अशा भाषांमध्ये अनुवादासाठी स्वयंसेवक बना ज्यामध्ये तुम्ही प्रवीण आहात.

जेव्हा तुम्ही पुल रिक्वेस्ट सबमिट करता, तेव्हा CLA-बॉट आपोआप ठरवेल की तुम्हाला CLA प्रदान करण्याची आवश्यकता आहे की नाही आणि PR योग्यरित्या सजवेल (उदा., लेबल, टिप्पणी). बॉटद्वारे प्रदान केलेल्या सूचनांचे फक्त अनुसरण करा. आमच्या CLA वापरणाऱ्या सर्व रेपॉझिटरीमध्ये तुम्हाला हे फक्त एकदाच करणे आवश्यक आहे.

या प्रकल्पाने [Microsoft ओपन सोर्स आचारसंहिता](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) स्वीकारली आहे. अधिक माहितीसाठी आचारसंहितेच्या FAQ वाचा किंवा [Email opencode](opencode@microsoft.com) वर कोणतेही अतिरिक्त प्रश्न किंवा टिप्पण्या सह संपर्क साधा.

## चला सुरुवात करूया

आता तुम्ही हा कोर्स पूर्ण करण्यासाठी आवश्यक चरण पूर्ण केले आहेत, [जनरेटिव्ह AI आणि LLMs परिचय](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) घेऊन सुरुवात करूया.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकारिक स्रोत मानावा. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.