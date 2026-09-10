# ఈ కోర్సుతో ప్రారంభించటం

మీరు ఈ కోర్సును ప్రారంభించి, జనరేటివ్ AI తో మీరు నిర్మించేందుకు ఉత్తేజితం అవ్వదలచుకున్నది చూడటానికి మేము చాలా ఉత్సాహంగా ఉన్నాము!

మీ విజయం కోసం, ఈ పేజీ సెటప్ దశలు, సాంకేతిక అవసరాలు మరియు అవసరమైతే సహాయం పొందే ప్రదేశాలను అందిస్తుంది.

## సెటప్ దశలు

ఈ కోర్సును ప్రారంభించేందుకు, మీరు క్రింది దశలను పూర్తి చేయాలి.

### 1. ఈ రిపోను ఫోర్క్ చేయండి

మీ స్వంత GitHub ఖాతాకు [ఈ మొత్తం రిపోను ఫోర్క్ చేయండి](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst), తద్వారా మీరు ఏ కోడ్‌లోనైనా మార్పులు చేయగలరు మరియు ఛాలెంజ్‌లను పూర్తి చేయవచ్చు. మీరు దీన్ని మరియు సంబంధిత రిపోల్ని సులభంగా కనుగొనడానికి కూడా [స్టార్ (🌟) చేయవచ్చు](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. కోడ్స్‌పేస్‌ను సృష్టించండి

కోడ్ నడపేటప్పుడు ఏదైనా డిపెండెన్సీ సమస్యలు ఎదురవకుండా ఉండేందుకు, ఈ కోర్సును [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)లో నడపటం మేము సిఫార్సు చేస్తాము.

మీ ఫోర్క్‌లో: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/te/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 సీక్రెట్ జోడించండి

1. ⚙️ గేర్ ఐకాన్ -> కమాండ్ పాలెట్ -> Codespaces : మేనేజ్ యూజర్ సీక్రెట్ -> కొత్త సీక్రెట్ జోడించండి.
2. పేరు OPENAI_API_KEY, మీ కీను పేస్ట్ చేసి, సేవ్ చేయండి.

### 3. తర్వాత ఏమి?

| నేను చేయాలనుకుంటున్నది…         | వెళ్లండి…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| లెసన్ 1 ప్రారంభించండి          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ఆఫ్లైన్‌లో పని చేయండి           | [`setup-local.md`](02-setup-local.md)                                   |
| LLM ప్రొవైడర్ సెటప్ చేయండి       | [`providers.md`](03-providers.md)                                        |
| ఇతర అభ్యసనకర్తలతో కలిసేవారు     | [మా డిస్కోర్డ్‌లో చేరండి](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## సమస్య పరిష్కారం


| లక్షణం                                    | పరిష్కారం                                                              |
|-------------------------------------------|------------------------------------------------------------------------|
| కంటైనర్ నిర్మాణం 10 నిమిషాలు గడిచినా ఉండటం  | **Codespaces ➜ “Rebuild Container”**                                    |
| `python: command not found`               | టెర్మినల్ అంటిచేయలేదు; క్లిక్ చేయండి **+** ➜ *bash*                      |
| OpenAI నుండి `401 Unauthorized`           | తప్పు / కాలం పూర్తయిన `OPENAI_API_KEY`                                  |
| VS Code "Dev container mounting…" చూపిస్తే | బ్రౌజర్ ట్యాబ్ రిఫ్రెష్ చేయండి — Codespaces కొన్ని సార్లు కనెక్షన్ కోల్పోతుంది | // 
| నోట్బుక్ కర్నల్ గాయపడింది              | నోట్బుక్ మెనూ ➜ **Kernel ▸ Select Kernel ▸ Python 3**                     |

   యూనిక్స్ ఆధారిత వ్యవస్థలు:

   ```bash
   touch .env
   ```

   విండోస్:

   ```cmd
   echo . > .env
   ```

3. **`.env` ఫైల్‌ను సవరించండి**: ఒక టెక్స్ట్ ఎడిటర్ లో `.env` ఫైల్‌ను తెరవండి (ఉదా: VS Code, Notepad++ లేదా ఏదైనా ఎడిటర్). ఫైల్‌లో క్రింది లైన్లను జోడించండి, మీరు మీ అసలు Microsoft Foundry Models ఎండ్‌పాయింట్ మరియు కీని ప్లేస్‌హోల్డర్స్ తో మార్చండి (పొందే విధానమును చూడటానికి [`providers.md`](03-providers.md) చూడండి):

   > **గమనిక:** GitHub Models (మరియు దాని `GITHUB_TOKEN` వేరియబుల్) జూలై 2026 చివరికి రిటైర్ అవుతోుంటుంది. దేనికంటే [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ఉపయోగించండి.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ఫైల్‌ను సేవ్ చేయండి**: మార్పులను సేవ్ చేసి టెక్స్ట్ ఎడిటర్‌ను మూసివేయండి.

5. **`python-dotenv` ఇన్‌స్టాల్ చేయండి**: మీరు ఇప్పటి వరకు చేయలేదు అయితే, `.env` ఫైల్ నుండి పర్యావరణ వేరియబుల్స్ ను మీ Python అప్లికేషన్‌లో లోడ్ చేయడానికి `python-dotenv` ప్యాకేజ్‌ను ఇన్‌స్టాల్ చేయాలి. దీన్ని `pip` ఉపయోగించి ఇన్‌స్టాల్ చేయవచ్చు:

   ```bash
   pip install python-dotenv
   ```

6. **మీ Python స్క్రిప్ట్‌లో పర్యావరణ వేరియబుల్స్‌ను లోడ్ చేయండి**: మీ Python స్క్రిప్ట్‌లో `.env` ఫైల్ నుండి వేరియబుల్స్ ను లోడ్ చేయడానికి `python-dotenv` ప్యాకేజ్ ను ఉపయోగించండి:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ఫైల్ నుండి వాతావరణ వేరియబుల్స్ లోడ్ చేయండి
   load_dotenv()

   # Microsoft Foundry Models వేరియబుల్స్‌కి pristum అవ్వండి
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

అంతే! మీరు విజయవంతంగా `.env` ఫైల్ సృష్టించి, Microsoft Foundry Models యొక్క క్రెడెన్షియల్స్ జోడించి, వాటిని మీ Python అప్లికేషన్‌లో లోడ్ చేశారు.

## మీ కంప్యూటర్‌లో స్థానికంగా ఎలా నడిపెయ్యాలి

కోడ్‌ను మీ కంప్యూటర్‌లో స్థానికంగా నడపడానికి, మీకు [Python ఇన్స్టాల్ చేసిన వర్షన్](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ఉండాలి.

ఆపై రిపాజిటరీని క్లోన్ చేయాలి:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

మీ వద్ద అన్నీ సరిగ్గా ఉన్న తర్వాత, మీరు ప్రారంభించవచ్చు!

## ఐచ్ఛిక దశలు

### మినికోండా ఇన్‌స్టాలేషన్

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) అనేది [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python మరియు కొన్ని ప్యాకేజీలు ఇన్‌స్టాల్ చేసుకోవడానికి లైట్ వెయిట్ ఇన్‌స్టాలర్.
Conda స్వయంగా ఒక ప్యాకేజ్ మేనేజర్, ఇది వివిధ Python [**వర్చువల్ ఎన్విరాన్మెంట్స్**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) మరియు ప్యాకేజీల మధ్య సులువుగా సెటప్ చేయడంలో మరియు మార్చుకోవడంలో సహాయపడుతుంది. ఇది `pip` ద్వారా అందుబాటులో లేనివి ఇన్స్టాల్ చేసుకోవడంలో ఉపయోగపడుతుంది.

మీరు [MiniConda ఇన్స్టాలేషన్ గైడ్](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ని అనుసరించి సెట్ అప్ చేసుకోవచ్చు.

Miniconda ఇన్‌స్టాలేషన్ చేసిన తర్వాత, మీరు రిపాజిటరీని (ఇంకా చేయలేదు అయితే) [క్లోన్](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) చేయాలి

తదుపరి, మీరు వర్చువల్ ఎన్విరాన్మెంట్ సృష్టించాలి. Condaతో ఇది చేయడానికి, కొత్త ఎన్విరాన్మెంట్ ఫైల్ (_environment.yml_) సృష్టించండి. మీరు Codespaces ను అనుసరించి ఉంటే, ఇది `.devcontainer` డైరెక్టరీలో, అంటే `.devcontainer/environment.yml` లో సృష్టించండి.

మీ ఎన్విరాన్మెంట్ ఫైల్ ను క్రింద చూపించిన స్నిపెట్‌తో నింపండి:

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

మీరు Conda ఉపయోగిస్తూ errors వస్తున్నట్లయితే, క్రింది కమాండ్‌ను టెర్మినల్‌లో ఉపయోగించి Microsoft AI లైబ్రరీలను మాన్యువీగా ఇన్‌స్టాల్ చేయవచ్చు.

```
conda install -c microsoft azure-ai-ml
```

ఎన్విరాన్మెంట్ ఫైల్ మనకు అవసరమైన డిపెండెన్సీలను స్పెసిఫై చేస్తుంది. `<environment-name>` అనేది మీరు మీ Conda ఎన్విరాన్మెంట్‌కు కేటాయించాలనుకునే పేరు, మరియు `<python-version>` అనేది మీరు ఉపయోగించదలచుకున్న Python వెర్షన్, ఉదా: `3` అనేది Python యొక్క తాజా ప్రధాన వెర్షన్.

అది పూర్తయ్యాక, మీ కమాండ్ లైన్/టెర్మినల్‌లో క్రింది కమాండ్లు అమలు చేసి మీ Conda ఎన్విరాన్మెంట్‌ను సృష్టించండి

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ఉప మార్గం కేవలం Codespace అమరికలకు మాత్రమే వర్తిస్తుంది
conda activate ai4beg
```

ఏదైనా సమస్యలు ఎదురైతే, [Conda ఎన్విరాన్మెంట్స్ గైడ్](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) చూడండి.

### Visual Studio Codeలో Python సపోర్ట్ ఎక్స్‌టెన్షన్‌తో ఉపయోగించడం

ఈ కోర్సుకు, మేము [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ఎడిటర్‌ను, [Python సపోర్ట్ ఎక్స్‌టెన్షన్](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)తో అమర్చుకోవడం సిఫార్సు చేస్తాము. ఇది అయినప్పటికీ, కఠిన అవసరం కాకుండా సిఫార్సు మాత్రమే.

> **గమనిక**: కోర్సు రిపాజిటరీని VS Codeలో తెరిచినప్పుడు, ప్రాజెక్ట్‌ను కంటైనర్‌లో సెటప్ చేసుకోవడానికి అవకాశం ఉంటుంది. ఇది కోర్సు రిపాజిటరీలో ఉన్న [ప్రత్యేక `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) డైరెక్టరీ కారణంగా జరుగుతుంది. దీనిపై మరింత తర్వాత తెలిపిస్తాము.

> **గమనిక**: మీరు రిపాజిటరీని క్లోన్ చేసి VS Codeలో తెరిచిన తర్వాత, అది ఆటోమేటిక్‌గా Python సపోర్ట్ ఎక్స్‌టెన్షన్ ఇన్‌స్టాల్ చేయమని సూచిస్తుంది.

> **గమనిక**: VS Code మీరు రిపాజిటరీని కంటైనర్‌లో పునఃప్రారంభించమని సూచిస్తే, మీరు స్థానికంగా ఇన్‌స్టాల్ చేసిన Pythonను ఉపయోగించాలనుకుంటే అటువంటి అభ్యర్థనను నిరాకరించండి.

### బ్రౌజర్‌లో Jupyter ను ఉపయోగించడం

మీరు ప్రాజెక్టుపై బ్రౌజర్‌లోనే [Jupyter వాతావరణం](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ఉపయోగించి పని చేయవచ్చు. క్లాసిక్ Jupyter మరియు [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) రెండు స్వాగతకరమైన అభివృద్ధి వాతావరణాన్ని అందిస్తాయి, ఆటో-కంప్లీషన్, కోడ్ హైలైటింగ్ వంటి ఫీచర్లతో.

స్థానికంగా Jupyter ను ప్రారంభించడానికి, టెర్మినల్/కమాండ్ లైన్ లోకి వెళ్లి, కోర్స్ డైరెక్టరీకి పోయి క్రింద అమలు చేయండి:

```bash
jupyter notebook
```

లేదా

```bash
jupyterhub
```

ఇది Jupyter ఇన్‌స్టెన్స్ ప్రారంభిస్తుంది మరియు ప్రవేశించడానికి URL ను కమాండ్ లైన్ విండోలో చూపిస్తుంది.

URLకి ప్రవేశించిన తర్వాత, మీరు కోర్సు అవుట్‌లైన్ చూసి `*.ipynb` ఫైల్‌లకు వెళ్లగలుగుతారు. ఉదా: `08-building-search-applications/python/oai-solution.ipynb`.

### కంటైనర్‌లో నడపటం

మీ కంప్యూటరులో లేదా Codespace లో అన్ని సెటప్ చేసుకోవడం బదులు, మీరు [కంటైనర్](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ఉపయోగించవచ్చు. కోర్సు రిపాజిటరీలో ప్రత్యేక `.devcontainer` ఫోల్డర్ వల్ల VS Code ప్రాజెక్ట్‌ను కంటైనర్‌లో సెటప్ చేయగలదు. Codespaces కాకుండా, దీని కోసం Docker ఇన్‌స్టాల్ చేయాలి, ఇది కొంత చింతం కలిగించే పని, కాబట్టి కేవలం కంటైనర్లలో అనుభవం ఉన్నవారికి మాత్రమే మేము సిఫార్సు చేస్తాము.

GitHub Codespaces ఉపయోగించేటప్పుడు మీ API కీలు సురక్షితంగా ఉంచటానికి ఉత్తమ మార్గాలలో ఒకటి కోడ్స్‌పేస్ సీక్రెట్లు ఉపయోగించడం. దీనిపై మరింత తెలుసుకోవడానికి [Codespaces సీక్రెట్స్ మేనేజ్‌మెంట్](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) గైడ్‌ను అనుసరించండి.


## పాఠాలు మరియు సాంకేతిక అవసరాలు

ఈ కోర్సులో జనరేటివ్ AI భావనలను వివరిస్తూ "Learn" పాఠాలు మరియు సాధ్యమైన చోట్ల **Python** మరియు **TypeScript** లో చేతితో రాసిన కోడ్ ఉదాహరణలతో "Build" పాఠాలు ఉన్నాయి.

కోడింగ్ పాఠాల కోసం, మేము Microsoft Foundry లో Azure OpenAI ఉపయోగిస్తాము. మీకు Azure సబ్‌స్క్రిప్షన్ మరియు API కీ అవసరం. యాక్సెస్ ఓపెన్ - అప్లికేషన్ అవసరం లేదు - కాబట్టి మీరు [Microsoft Foundry రిసోర్సును సృష్టించి మోడల్‌ను డిప్లాయ్ చేయండి](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) మీ ఎండ్‌పాయింట్ మరియు కీ కోసం.

ప్రతి కోడింగ్ పాఠంలో కూడా కోడ్ మరియు ఫలితాలను నడిపి చూడకుండానే చూడగలిగే `README.md` ఫైల్ ఉంటుంది.

## Azure OpenAI సేవను తొలిసారిగా ఉపయోగించడం

Azure OpenAI సేవతో మీరు తొలిసారిగా పని చేయనున్నట్లయితే, దీన్ని సృష్టించి డిప్లాయ్ చేయడానికి ఈ గైడ్‌ను అనుసరించండి: [create and deploy an Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI APIని తొలిసారిగా ఉపయోగించడం

OpenAI APIతో తొలిసారిగా పనిచేస్తున్నట్లయితే, [create and use the Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) గైడ్‌ను అనుసరించండి.

## ఇతర అభ్యసనకర్తలతో కలవడం

మేము మా అధికారిక [AI Community Discord సర్వర్](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)లో ఇతర అభ్యసనకర్తలతో కలవటానికి ఛానల్స్ సృష్టించాము. ఇది ఇతర మానసిక స్థితిలో ఉన్న వ్యాపారులు, బిల్డర్లు, విద్యార్థులు మరియు జనరేటివ్ AIలో స్థాయిని పెంచుకోవాలనుకునేవారితో నెట్‌వర్క్ చేయడానికి గొప్ప మార్గం.

[![డిస్కోర్డ్ ఛానెల్‌లో చేరండి](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ప్రాజెక్ట్ టీమ్ కూడా ఈ డిస్కోర్డ్ సర్వర్‌లో ఉంటుంది మరియు ఏదైనా అభ్యసనకర్తలకు సహాయం చేస్తుంది.

## సహకారం చేయండి

ఈ కోర్సు ఓపెన్-సోర్స్ ప్రయత్నం. మీరు మెరుగుదలలు లేదా సమస్యలను చూడగలిగితే, దయచేసి [పుల్ రిక్వెస్ట్](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) సృష్టించండి లేదా [GitHub ఇషూ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) లాగ్ చేయండి.

ప్రాజెక్ట్ టీమ్ అన్ని సహకారాలను ట్రాక్ చేస్తుంది. ఓపెన్ సోర్స్‌కు సహకరించడం జనరేటివ్ AIలో మీ వృత్తి నిర్మాణానికి అద్భుత మార్గం.

చాలా సహకారాలు మీరు మీరు చేసిన సహకారాన్ని ఉపయోగించుకునే హక్కు కలిగి ఉన్నారు మరియు నిజంగా హక్కులు వినియోగదారులకు ఇవ్వడాన్ని ప్రకటించే Contributor License Agreement (CLA)కు ఒప్పందం కావాల్సి ఉంటుంది. వివరాలకు, [CLA, Contributor License Agreement వెబ్‌సైట్](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) చూడండి.

ముఖ్యమైన ముద్రణ: ఈ రిపోలో టెక్స్ట్ అనువదించేటప్పుడు, దయచేసి యంత్ర అనువాదాన్ని ఉపయోగించకండి. మేము అనువాదాలను కమ్యూనిటీ ద్వారా ధ్రువీకరిస్తాము, కాబట్టి మీరు నైపుణ్యం ఉన్న భాషల్లో మీరు మాత్రమే అనువాదానికి ఎటువంటి సహాయం అందించాలని భావించండి.


మీరు ఒక పుల్ రిక్వెస్ట్ సమర్పించినప్పుడు, CLA-బాట్ స్వయంచాలకంగా మీరు CLA అందించాల్సిన అవసరం ఉందో లేదో నిర్ణయించి PR ని సరిగ్గా అలంకరించుతుంది (ఉదా: లేబుల్, వ్యాఖ్య). బాట్ ఇచ్చే సూచనలను అనుసరించండి. మా CLA ఉపయోగించే అన్ని రిపోజిటరీలలో ఇది మీరు ఒక్కసారి మాత్రమే చేయాలి.

ఈ ప్రాజెక్టు [Microsoft ఓపెన్ సోర్స్ కోడ్ ఆఫ్ కండక్ట్](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ను అనుసరించింది. మరింత సమాచారం కోసం కోడ్ ఆఫ్ కండక్ట్ FAQ ని చదవండి లేదా అదనపు ప్రశ్నలు లేదా వ్యాఖ్యల కోసం [Email opencode](opencode@microsoft.com) ని సంప్రదించండి.

## బాగుందడి దాద్దాం

మీరు కోర్సును పూర్తి చేయడానికి అవసరమైన దశలను జరిగినందున, ఇపుడు [జెనరేటివ్ AI మరియు LLM ల పరిచయాన్ని](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) పొందడం ద్వారా ప్రారంభిద్దాం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->