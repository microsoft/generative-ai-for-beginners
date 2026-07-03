# ఈ కోర్సును ప్రారంభించడం

మీరు ఈ కోర్సును ప్రారంభించి, జనరేటివ్ AI తో మీరు ఏం సృష్టించగలరో చూడడానికి మేము చాలా ఉత్సాహంగా ఉన్నాము!

మీ విజయం కోసం, ఈ పేజీ సెట్‌అప్ దశలు, సాంకేతిక అవసరాలు మరియు అవసరమైతే సహాయం పొందవచ్చు ఎక్కడను వివరించింది.

## సెట్‌అప్ దశలు

ఈ కోర్సు ప్రారంభించడానికి, మీరు క్రింద పేర్కొన్న దశలను పూర్తి చేయాలి.

### 1. ఈ రిపోను ఫోర్క్ చేయండి

ఈ మొత్తం రిపోను మీ స్వంత GitHub అక్కౌంట్లోకి [ఫోర్క్ చేయండి](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ताकि మీరు ఏ కోడ్ లోనైనా మార్పులు చేసి సవాళ్లను పూర్తి చేయగలుగుతారు. మీరు ఈ రిపోను [స్టార్ (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) చేయవచ్చు, అది మరియు సంబంధిత రిపోలు సులభంగా కనుగొనడానికి.

### 2. కోడ్స్‌పేస్ సృష్టించండి

కోడ్ నడుపుతున్నప్పుడు ఏదైనా డిపెండెన్సీ సమస్యలు నివారించడానికి, ఈ కోర్సును [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) లో నడపడం మేము సిఫార్సు చేస్తాము.

మీ ఫోర్క్ లో: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/te/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 సీక్రెట్ జోడించండి

1. ⚙️ గేర్ ఐకాన్ -> Command Pallete -> Codespaces : Manage user secret -> కొత్త సీక్రెట్ జోడించండి.
2. OPENAI_API_KEY అని పేరు పెట్టి, మీ కీ పేస్ట్ చేసి, Save చేయండి.

### 3. తదుపరి ఏం చేయాలి?

| నేను చేయాలనుకునేది…       | వెళ్ళండి…                                                            |
|---------------------------|---------------------------------------------------------------------|
| పాఠం 1 ప్రారంభించండి     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| ఆఫ్‌లైన్‌లో పని చేయాలి   | [`setup-local.md`](02-setup-local.md)                               |
| LLM ప్రొవైడర్ సెట్ చేయండి | [`providers.md`](03-providers.md)                                    |
| ఇతర విద్యార్థులతో కలవండి | [మా Discord లో చేరండి](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## సమస్య పరిష్కారం

| లక్షణం                                   | పరిష్కారం                                                  |
|------------------------------------------|-----------------------------------------------------------|
| కంటైనర్ నిర్మాణం 10 నిమిషాలకంటే ఎక్కువుగా నిలిచింది | **Codespaces ➜ “Rebuild Container”**                      |
| `python: command not found`              | ట్మినల్ అనుసంధానం కాలేదు; **+** క్లిక్ చేసి *bash* ఎంచుకోండి |
| OpenAI నుండి `401 Unauthorized`           | తప్పు లేదా కాలం ముగిసిన `OPENAI_API_KEY`                   |
| VS Code "Dev container mounting…" చూపిస్తుంది   | బ్రౌజర్ ట్యాబ్ రిఫ్రెష్ చేయండి — Codespaces కొన్నిసార్లు కనెక్షన్ కోల్పోతుంది |
| నోట్బుక్ కర్నల్ లేవు                    | నోట్బుక్ మెనూ ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   యూనిక్స్-ఆధారిత వ్యస్థలు:

   ```bash
   touch .env
   ```

   విండోస్:

   ```cmd
   echo . > .env
   ```

3. **`.env` ఫైలును సవరించండి**: `.env` ఫైలును ఎడిటర్ లో (ఉదా: VS Code, Notepad++, లేదా ఇతర ఎడిటర్) తెరవండి. ఈ కింది లైన్‌ను జోడించండి, `your_github_token_here` స్థానంలో మీ GitHub టోకెన్ ను ఉంచండి:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ఫైలును సేవ్ చేయండి**: మార్పులను సేవ్ చేసి ఎడిటర్ ను మూసివేయండి.

5. **`python-dotenv` ను ఇనస్టాల్ చేయండి**: మీరు ఇప్పటివరకూ చేయకపోతే, `.env` ఫైల్ నుండి ఎన్‌విరాన్మెంట్ వేరియబుల్స్ లోడ్ చేయడానికి `python-dotenv` ప్యాకేజీని `pip` ద్వారా ఇనస్టాల్ చేయండి:

   ```bash
   pip install python-dotenv
   ```

6. **మీ పైథాన్ స్క్రిప్టులో ఎన్‌విరాన్మెంట్ వేరియబుల్స్ లోడ్ చేయండి**: మీ పైథాన్ స్క్రిప్ట్‌లో ఈ ప్యాకేజీని ఉపయోగించి `.env` ఫైల్ నుండి ఎన్‌విరాన్మెంట్ వేరియబుల్స్ ని లోడ్ చేయండి:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ఫైల్ నుండి పర్యావరణ చరాలు లోడ్ చేయండి
   load_dotenv()

   # GITHUB_TOKEN చరాన్ని యాక్సెస్ చేయండి
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ఇది మొత్తమయింది! మీరు సఫలముగా `.env` ఫైల్ తయారు చేసి, GitHub టోకెన్ జోడించి, దాన్ని మీ పైథాన్ అప్లికేషన్‌లో లోడ్ చేసుకున్నారు.

## మీ కంప్యూటరులో స్థానికంగా ఎలా నడపాలి

మీ కంప్యూటరులో కోడ్ స్థానికంగా నడపడానికి, మీ దగ్గర ఏదైనా [Python వెర్షన్ ఇన్స్టాల్ చేయబడినది ఉండాలి](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

తపి రిపోను ఉపయోగించాలంటే, దానిని క్లోన్ చేయాలి:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

అన్నీ సెట్ చేసుకున్న తర్వాత, మీరు మొదలు పెట్టవచ్చు!

## ఐచ్ఛిక దశలు

### మినికాండా ఇన్స్టాల్ చేయడం

[మినికాండా](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) అనేది [కాండా](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python మరియు కొన్ని ప్యాకేజీలను ఇన్స్టాల్ చేయడానికి తేలికపాటి ఇన్స్టాలర్.
కాండా ఒక ప్యాకేజ్ మేనేజర్, ఇది వివిధ Python [**వర్చ്വల్ ఎన్విరాన్మెంట్లు**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) మరియు ప్యాకేజీల మధ్య సులభంగా సెట్ అప్ చేయడానికి మరియు మారడానికి సహాయ పడుతుంది. ఇది పిప్ ద్వారా లభ్యం కాని ప్యాకేజీలను ఇన్స్టాల్ చేయడానికి కూడా బాగా ఉపయోగపడుతుంది.

మీరు [MiniConda ఇన్స్టలేషన్ గైడ్](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ను అనుసరించి సెట్ అప్ చేయవచ్చు.

మినికాండా ఇన్స్టాల్ చేసిన తర్వాత, మీరు రిపోను క్లోన్ చేయాలి (మించి చేస్తే):

[https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)

తర్వాత, మీరు వర్చువల్ ఎన్విరాన్మెంట్ సృష్టించాలి. దీనికి కాండాతో వెళ్లి ఒక కొత్త ఎన్విరాన్మెంట్ ఫైల్ (_environment.yml_) సృష్టించండి. మీరు Codespaces ఉపయోగిస్తున్నట్లయితే, ఇది `.devcontainer` డైరెక్టరీలో ఉంచండి, అంటే `.devcontainer/environment.yml`.

కిందివరకు మీ ఎన్విరాన్మెంట్ ఫైల్ ని భర్తీ చేయండి:

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

మీరు కాండా ఉపయోగిస్తుండగా ఎర్రర్లు వస్తే, మీరు మాన్యువల్‌గా Microsoft AI లైబ్రరిలను టెర్మినల్‌లో ఈ కమాండ్ ద్వారా ఇన్స్టాల్ చేయవచ్చు.

```
conda install -c microsoft azure-ai-ml
```

ఈ ఎన్విరాన్మెంట్ ఫైల్ మాకు కావలసిన డిపెండెన్సీలను పేర్కొంటుంది. `<environment-name>` అనే పేరు మీరు మీ Conda ఎన్విరాన్మెంట్ కు ఇవ్వదలచిన పేరు, `<python-version>` అనేది మీరు ఉపయోగించదలచిన Python వెర్షన్, ఉదాహరణకు, `3` అనేది Python యొక్క తాజా ప్రధాన సంస్కరణ.

ఇప్పుడు, మీరు ఈ క్రింది ఆజ్ఞలను టెర్మినల్ లేదా కమాండ్ లైన్ లో నడపడం ద్వారా మీ Conda ఎన్విరాన్మెంట్ సృష్టించవచ్చు:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ఉప మార్గం కేవలం కోడ్స్పేస్ సెట్‌అప్స్‌కు వర్తిస్తుంది
conda activate ai4beg
```

ఏదైనా సమస్యలు ఎదురైనప్పుడు [కాండా ఎన్విరాన్మెంట్స్ గైడ్](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) చూడండి.

### పైథాన్ సపోర్ట్ ఎక్స్‌టెన్షన్‌తో Visual Studio Code ఉపయోగించడం

ఈ కోర్సుకు మేము [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ఎడిటర్‌ను [Python సపోర్ట్ ఎక్స్‌టెన్షన్](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)తో ఉపయోగించూడని సిఫార్సు చేస్తున్నాము. ఇది తప్పనిసరి కాదు కానీ సిఫార్సు మాత్రమే.

> **గమనిక**: కోర్సు రిపోను VS Codeలో తెరిచేటప్పుడు, ప్రాజెక్ట్‌ను కంటైనర్‌లో సెట్ అప్ చేసే ఆప్షన్ ఉంటుంది. ఇది కోర్సు రిపోలోని [ప్రత్యేక `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) డైరెక్టరీ కారణంగా ఉంటుంది. దీనిపై తర్వాత మరింత వివరాలు ఉంటాయి.

> **గమనిక**: మీరు రిపోను క్లోన్ చేసి VS Codeలో తెరిచిన వెంటనే ఇది Python సపోర్ట్ ఎక్స్‌టెన్షన్ ఇన్స్టాల్ చేయమని సూచిస్తుంది.

> **గమనిక**: VS Code రిపోను కంటైనర్‌లో మళ్లీ తెరవమని సూచిస్తే, మీరు స్థానికంగా ఇన్‌స్టాల్ చేసిన Python వర్షన్ ఉపయోగించడానికి ఆ అభ్యర్థనను తిరస్కరించండి.

### బ్రౌజర్‌లో జూపిటర్ ఉపయోగించడం

మీరు ప్రాజెక్టుపై [Jupyter వాతావరణం](https://jupyter.org?WT.mc_id=academic-105485-koreyst)ను కూడా మీ బ్రౌజర్లోనే నడపవచ్చు. క్లాసిక్ Jupyter మరియు [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) స్వీకృత అభివృద్ధి వాతావరణం ఇవ్వడానికి, ఆటో కంప్లీషన్, కోడ్ హైలైటింగ్ వంటి లక్షణాలు కలిగివుంటాయి.

Jupyterను స్థానికంగా ప్రారంభించాలంటే, టెర్మినల్/కమాండ్ లైన్లోకి వెళ్లి కోర్సు డైరెక్టరీలో నేవిగేట్ చేసి ఈ ఆజ్ఞను నడపండి:

```bash
jupyter notebook
```

లేదా

```bash
jupyterhub
```

ఇది Jupyter ఇన్స్టెన్స్ని ప్రారంభిస్తుంది మరియు యాక్సెస్ చేయడానికి URL టెర్మినల్ విండోలో చూపబడుతుంది.

URL ను యాక్సెస్ చేసిన తర్వాత, మీరు కోర్సు అవుట్‌లైన్ చూడగలరు మరియు ఏ `*.ipynb` ఫైలు అయినా నావిగేట్ చేయవచ్చు. ఉదాహరణకు, `08-building-search-applications/python/oai-solution.ipynb`.

### కంటైనర్‌లో నడిపించడం

మీ కంప్యూటర్ లేదా Codespaceలో అన్ని సెట్ అప్ చేయాలంటే ఒక ఎంపికగా [కంటైనర్](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) ఉపయోగించవచ్చు. కోర్సు రిపోలోని ప్రత్యేక `.devcontainer` ఫోల్డర్ ద్వారా VS Code ఈ ప్రాజెక్టును కంటైనర్‌లో సెట్ అప్ చేయగలదు. Codespaces కాకుండా ఇది Docker ఇన్స్టాలేషన్ అవసరం, మరియు కొంత పని ఉంటుంది, కాబట్టి కంటైనర్లలో అనుభవం ఉన్న వారికి మాత్రమే మేము అందరికి సిఫారసు చేస్తాము.

GitHub Codespaces ఉపయోగిస్తున్నప్పుడు మీ API కీస్ సురక్షితంగా ఉంచడానికి Codespace Secrets ఉపయోగించడం ఉత్తమ మార్గాలలో ఒకటి. దయచేసి [Codespaces సీక్రెట్స్ నిర్వహణ](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) మార్గదర్శకాన్ని అనుసరించండి.

## పాఠాలు మరియు సాంకేతిక అవసరాలు

ఈ కోర్సులో 6 కాన్సెప్ట్ పాఠాలు మరియు 6 కోడింగ్ పాఠాలు ఉన్నాయి.

కోడింగ్ పాఠాల కోసం, మేము Azure OpenAI సర్వీస్ ఉపయోగిస్తున్నాము. ఈ కోడ్ నడపడానికి మీకు Azure OpenAI సర్వీస్ మరియు ఒక API కీ అవసరం. మీరు [ఈ అప్లికేషన్ పూర్తి చేసి](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) అక్సెస్ తీసుకోవచ్చు.

మీ అప్లికేషన్ ప్రాసెస్ అవ్వడానికి వేచి ఉన్నప్పుడు, ప్రతి కోడింగ్ పాఠంలో కూడా `README.md` ఫైల్ ఉంటుంది, అక్కడ మీరు కోడ్ మరియు అవుట్పుట్లు చూడవచ్చు.

## Azure OpenAI సర్వీస్‌ను మొదటిసారి ఉపయోగించడం

మీరు Azure OpenAI సర్వీస్‌తో మొదటిసారి పనిచేస్తున్నట్లయితే, దయచేసి [Azure OpenAI సర్వీస్ వనరు ఎలా సృష్టించి అమర్చాలో](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) గైడ్ అనుసరించండి.

## OpenAI API ను మొదటిసారి ఉపయోగించడం

OpenAI APIతో మొదటిసారి పనిచేస్తున్నట్లయితే, దయచేసి [ఇంటర్ఫేస్ ఎలా సృష్టించి ఉపయోగించాలో](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) గైడ్ అనుసరించండి.

## ఇతర లెర్నర్లను కలవండి

మేము అధికారిక [AI Community Discord సర్వర్](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)లో ఇతర లెర్నర్లను కలుసుకునేందుకు చానెల్స్ yaratించారు. ఇది ఇతర ఇష్టమైన వ్యాపారవేత్తలు, నిర్మాణకర్తలు, విద్యార్థులు మరియు జనరేటివ్ AIలో మెరుగుపడాలని కోరుకునేవారితో నెట్‌వర్క్ చేసుకోవడానికి గొప్ప మార్గం.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ప్రాజెక్ట్ టీమ్ కూడా ఈ Discord సర్వర్‌లో ఉండి సహాయం చేస్తుంది.

## సహకరించండి

ఈ కోర్సు ఓపెన్ స్రోర్స్ ప్రాజెక్ట్. మీరు అభివృద్ధి కావలసిన ప్రాంతాలు లేదా సమస్యలను చూసినా, దయచేసి [పుల్ రిక్వెస్ట్](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) సృష్టించండి లేదా [GitHub ఇషూ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) నమోదు చేయండి.

ప్రాజెక్ట్ టీమ్ అన్ని కాంట్రిబ్యూషన్స్ ని గమనిస్తుంది. ఓపెన్ సోర్స్ లో సహకరించడం జనరేటివ్ AIలో మీ కెరీర్‌ను నిర్మించడానికి అద్భుతమైన మార్గం.

అధికাংশ కాంట్రిబ్యూషన్లు మీరు కనెక్ట్ చేసిన కాంట్రిబ్యూటర్ లైసెన్స్ అగ్రిమెంట్ (CLA) కి అంగీకరించవలసిన అవసరం ఉంటుందని నిర్వచిస్తాయి. వివరాలకు [CLA, Contributor License Agreement వెబ్‌సైట్](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) చూడండి.

ముఖ్యమైనది: ఈ రిపోలో టెక్స్ట్ అనువదించే సమయంలో, దయచేసి యంత్ర అనువాదం ఉపయోగించరాదు. మేము అనువాదాలను కమ్యూనిటీ ద్వారా నిర్ధారించడం జరుగుతుంది, కనుక మీరు పరిపక్వంగా ఉన్న భాషల్లోనే అనువాదానికి స్వయంగా ముందుకు రావాల్సిని కోరుకుంటున్నాము.

మీరు పుల్ రిక్వెస్ట్ సమర్పించినప్పుడు, CLA-బాట్ మీకు CLA అందించవలసి ఉంటుందో లేదో నిర్ణయించి, PR ను తగిన ఉల్లేఖనాలతో చిహ్నింత్తుంది (ఉదాహరణకు, లేబుల్, వ్యాఖ్య). బాట్ ఇచ్చిన సూచనలను మాత్రమే అనుసరించండి. ఈ ప్రక్రియ మీరు అన్ని రిపోలను కోసం ఒకసారి మాత్రమే చేయాలి.

ఈ ప్రాజెక్ట్ [Microsoft ఓపెన్ సోర్స్ కోడ్ ఆఫ్ కండక్ట్](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ను అనుసరించింది. మరింత సమాచారం కోసం కోడ్ ఆఫ్ కండక్ట్ FAQ చదవండి లేదా అదనపు సందేహాలు లేదా వ్యాఖ్యల కోసం [Email opencode](opencode@microsoft.com) ని సంప్రదించండి.

## మనం మొదలు పెడదాం!
ఇప్పుడు మీరు ఈ కోర్సును పూర్తి చేయడానికి అవసరమైన దశలను పూర్తి చేసుకున్నందున, [Generative AI మరియు LLMs కు పరిచయము](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) పొందుతూ మొదలు పెడదాం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**విధివిధాన వ్యాఖ్యానం**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సర్వీసు [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము సరైన అనువాదానికి ప్రయత్నిస్తుండగా, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా పొరపాట్లు ఉండవచ్చు అని దయచేసి జాగ్రత్తగా గమనించండి. స్థానిక భాషలో ఉన్న అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి ప్రొఫెషనల్ మానవ అనువాదం చేయించడం ఉత్తమం. ఈ అనువాదం వలన వచ్చే ఏదైనా భ్రమలు లేదా తప్పుగా అర్థమయ్యే పరిస్థితులకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->