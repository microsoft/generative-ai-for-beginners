# లోకల్ సెటప్ 🖥️

**మీరు మీ స్వంత ల్యాప్‌టాప్‌లోనే ప్రతిదీ నడపడానికి ఇష్టపడితే ఈ గైడ్‌ను ఉపయోగించండి.**  
మీకు రెండు మార్గాలు ఉన్నాయి: **(A) స్థానిక Python + virtual-env** లేదా **(B) VS Code Dev Containerతో Docker**.  
ఎవరైనా ఈ రెండు పాఠాలకుకు తీసుకెళ్తాయని ఎక్కడైనా సులభంగా అనిపించే దానిని ఎంచుకోండి.

## 1. మునుపటి అవసరాలు

| టూల్              | వెర్షన్ / గమనికలు                                                                  |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> నుండి పొందండి)                                            |
| **Git**            | తాజా (Xcode / Git for Windows / Linux ప్యాకేజ్ మేనేజర్‌తో వస్తుంది)                    |
| **VS Code**        | ఐచ్ఛికం కానీ సిఫారసు చేయబడింది <https://code.visualstudio.com>                             |
| **Docker Desktop** | *మాత్రమే* ఆప్షన్ B కోసం. ఉచిత ఇన్స్టాలేషన్: <https://docs.docker.com/desktop/>                |

> 💡 **సూచన** – టూల్స్‌ను టర్మినల్‌లో తనిఖీ చేయండి:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. ఆప్షన్ A – స్థానిక Python (వేగవంతమైనది)

### దశ 1 ఈ రిపోను క్లోన్ చేయండి

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### దశ 2 వర్చువల్ ఎన్విరాన్‌మెంట్‌ని సృష్టించి సక్రియం చేయండి

```bash
python -m venv .venv          # ఒకటి చేయండి
source .venv/bin/activate     # మాక్‌ఓఎస్ / లినక్స్
.\.venv\Scripts\activate      # విండోస్ పవర్‌షెల్
```

✅ ప్రాంప్ట్ ఇప్పుడు (.venv) తో ప్రారంభం అయితే అది మీరు ఎన్విరాన్‌మెంట్‌లో ఉన్నారని సూచిస్తుంది.

### దశ 3 ఆధారాలను ఇన్స్టాల్ చేయండి

```bash
pip install -r requirements.txt
```

[API కీలు](#3-మీ-api-కీలు-జోడించండి) పై సెక్షన్ 3 కు దాటి మళ్లించండి

## 2. ఆప్షన్ B – VS Code Dev కంటెయినర్ (Docker)

మేము ఈ రిపో మాడ్యూల్ మరియు కోర్సు ను [డెవలప్మెంట్ కంటెయినర్](https://containers.dev?WT.mc_id=academic-105485-koreyst) తో సెటప్ చేసాము, ఇది Python3, .NET, Node.js మరియు Java డెవలప్‌మెంట్‌కు సహాయం చేసే యూనివర్సల్ రంటైమ్ కలిగి ఉంది. సంబంధిత కాన్ఫిగరేషన్ `devcontainer.json` ఫైల్‌లో నిర్వచించబడినది, ఇది ఈ రిపో యొక్క రూట్‌లో ఉన్న `.devcontainer/` ఫోల్డర్‌లో ఉంది.

>**ఇందుకు మీరు ఎందుకు ఎంచుకోవాలి?**
>Codespaces‌కు సమానమైన వాతావరణం; డిపెండెన్సీ డ్రిఫ్ట్ లేదు.

### దశ 0 అదనపు ప్యాకేజీలను ఇన్స్టాల్ చేయండి

Docker Desktop – ```docker --version``` పనిచేస్తుందో నిర్ధారించుకోండి.
VS Code Remote – Containers ఎక్స్‌టెన్షన్ (ID: ms-vscode-remote.remote-containers).

### దశ 1 VS Code లో రిపోని ఓపెన్ చేయండి

ఫైల్ ▸ ఫోల్డర్ ఓపెన్ చేయండి… → generative-ai-for-beginners

VS Code .devcontainer/ గుర్తించి ప్రాంప్ట్ చూపుతుంది.

### దశ 2 కంటెయినర్‌లో మళ్లించి తెరవండి

“Reopen in Container” క్లిక్ చేయండి. Docker మొదటిసారి ఇమేజ్ (≈ 3 నిమిషాలు) తయారు చేస్తుంది.
టర్మినల్ ప్రాంప్ట్ కనిపించినప్పుడు, మీరు కంటెయినర్‌లో ఉన్నారు.

## 2. ఆప్షన్ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python మరియు కొన్ని ప్యాకేజీలను ఇన్స్టాల్ చేయడానికి ఒక లైట్‌వెయిట్ ఇన్స్టాలర్.
Conda స్వయంగా ప్యాకేజీ మేనేజర్, ఇది Python [**వర్చువల్ ఎన్విరాన్‌మెంట్‌లు**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) మరియు ప్యాకేజీల మధ్య సులభంగా సెటప్ మరియు మార్పిడి చేయడం చేస్తుంది. ఇది `pip` ద్వారా అందుబాటులో లేని ప్యాకేజ్‌లను ఇన్స్టాల్ చేయడానికి కూడా ఉపయోగపడుతుంది.

### దశ 0 Miniconda ఇన్స్టాల్ చేయండి

దీనిని సెటప్ చేసుకోవడానికి [MiniConda ఇన్స్టాలేషన్ గైడ్](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ని అనుసరించండి.

```bash
conda --version
```

### దశ 1 వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి

కొత్త ఎన్విరాన్‌మెంట్ ఫైల్ (*environment.yml*) సృష్టించండి. మీరు Codespaces ఉపయోగిస్తుంటే, దాన్ని `.devcontainer` డైరెక్టరీలో సృష్టించండి, అంటే `.devcontainer/environment.yml`.

### దశ 2 మీ ఎన్విరాన్‌మెంట్ ఫైల్‌ను నింపండి

క్రింది స్నిపెట్‌ను మీ `environment.yml`లో జతచేయండి

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

### దశ 3 మీ Conda ఎన్విరాన్‌మెంట్ తయారు చేయండి

కింది కమాండ్లను మీ కమాండ్ లైన్/టర్మినల్లో చెల్లించండి

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ఉప మార్గం కేవలం Codespace సెటప్‌లపై మాత్రమే వర్తిస్తుంది
conda activate ai4beg
```

ఎలాంటి సమస్యలు వస్తే [Conda ఎన్విరాన్‌మెంట్ గైడ్](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) చూడండి.

## 2  ఆప్షన్ D – క్లాసిక్ జుపిటర్ / జుపిటర్ ల్యాబ్ (మీ బ్రౌజర్‌లో)

> **ఇది ఎవరి కోసం?**  
> ఎవరికైనా క్లాసిక్ జుపిటర్ ఇంటర్‌ఫేస్ ఇష్టమైతే లేదా VS Code లేకుండా నోట్‌బుక్‌లు నడపాలనుకున్న వారికి.  

### దశ 1 జుపిటర్ ఇన్స్టాల్ అయిందో లేదో నిర్ధారించుకోండి

జుపిటర్ స్థానికంగా ప్రారంభించడానికి, టర్మినల్/కమాండ్ లైన్‌కి వెళ్లి కోర్సు డైరెక్టరీలో నావిగేట్ చేసి నడపండి:

```bash
jupyter notebook
```

లేదా

```bash
jupyterhub
```

ఇది జుపిటర్ ఇన్స్టాన్స్‌ను ప్రారంభిస్తుంది మరియు యాక్సెస్‌కి URL కమాండ్ లైన్ విండోలో చూపబడుతుంది.

URL యాక్సెస్ చేసిన తరువాత, మీరు కోర్సు అవుట్‌లైన్‌ను చూడగలుగుతారు మరియు ఏ `*.ipynb` ఫైల్‌కు నావిగేట్ చేయవచ్చు. ఉదాహరణకు, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. మీ API కీలు జోడించండి

ఏదైనా రకమైన అప్లికేషన్‌ను నిర్మిస్తుంటే మీ API కీలు సురక్షితంగా ఉంచడం ముఖ్యం. మేము మీ కీ లను ప్రత్యక్షంగా కోడ్‌లో నిల్వ చేయవద్దని సూచిస్తున్నాము. అవి పబ్లిక్ రిపోజిటరీకి కమీట్ చేయబడ్డ VERY దుష్టవ్యక్తి ఉపయోగిస్తే సెక్యూరిటీ సమస్యలు మరియు అనవసర ఖర్చులు కలగవచ్చు.
Python కోసం `.env` ఫైల్‌ను సృష్టించడానికి మరియు మీ Microsoft Foundry Models యొక్క సర్టిఫికెట్లు జోడించడానికి ఒక దశల వారీ గైడ్ ఇక్కడ ఉంది:

> **గమనిక:** GitHub Models (మరియు దాని `GITHUB_TOKEN` వేరియబుల్) జూలై 2026 చివరలో రిటైర్ అవుతాయి. ఈ గైడ్ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ను ఉపయోగిస్తుంది. మీరు పూర్తిగా ఆన్‌లైన్ కాకుండా పనిచేయాలని ఇష్టపడితే [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) చూడండి.

1. **మీ ప్రాజెక్ట్ డైరెక్టరీకి వెళ్లండి**: మీ టర్మినల్ లేదా కమాండ్ ప్రాంప్ట్ తెరవండి మరియు `.env` ఫైల్ సృష్టించాలనుకున్న ప్రాజెక్ట్ రూట్ డైరెక్టరీకి వెళ్లండి.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ఫైల్ సృష్టించండి**: మీ ఇష్టమైన టెక్స్ట్ ఎడిటర్ ఉపయోగించి `.env` పేరుతో ఒక కొత్త ఫైల్ సృష్టించండి. మీరు కమాండ్ లైన్ ఉపయోగిస్తుంటే, Unix-ఆధారిత వ్యవస్థల్లో `touch`, Windowsలో `echo` ఉపయోగించవచ్చు:

   Unix-ఆధారిత వ్యవస్థలు:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ఫైల్ ఎడిట్ చేయండి**: `.env` ఫైల్‌ను VS Code, Notepad++ లేదా మీరు ఉపయోగించే ఎడిటర్‌లో ఓపెన్ చేసి క్రింది లైన్లను జోడించండి, ప్లేస్‌హోల్డర్లను మీ వాస్తవ Microsoft Foundry ప్రాజెక్ట్ ఎండ్పాయింట్ మరియు API కీతో మార్పిడి చేయండి:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ఫైల్ సేవ్ చేయండి**: మార్పులను సేవ్ చేసి టెక్స్ట్ ఎడిటర్ మూసివేయండి.

5. **`python-dotenv` ఇన్స్టాల్ చేయండి**: మీరు ఇంకా చేయకపోతే, `.env` ఫైల్ నుండి వాతావరణ వేరియబుల్‌లను Python అప్లికేషన్‌లో లోడ్ చేయడానికి `python-dotenv` ప్యాకేజీని ఇన్స్టాల్ చేయాలి. మీరు `pip` ఉపయోగించి ఇన్స్టాల్ చేయవచ్చు:

   ```bash
   pip install python-dotenv
   ```

6. **Python స్క్రిప్ట్‌లో వాతావరణ వేరియబుల్‌లను లోడ్ చేయండి**: మీ Python స్క్రిప్ట్‌లో, `.env` ఫైల్ నుండి వాతావరణ వేరియబుల్‌లను లోడ్ చేయడానికి `python-dotenv` ప్యాకేజీని ఉపయోగించండి:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ఫైల్ నుండి వాతావరణ మార్పులు లోడ్ చేయండి
   load_dotenv()

   # Microsoft Foundry Models వాతావరణ మార్పులు యాక్సెస్ చేయండి
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

అంతే! మీరు విజయవంతంగా `.env` ఫైల్ సృష్టించి, Microsoft Foundry Models క్రెడెన్షియల్స్ జోడించి అవి Python అప్లికేషన్‌లో లోడ్ చేసుకున్నారు.

🔐 `.env` ను ఎప్పుడూ కమీట్ చేయవద్దు – ఇది ఇప్పటికే `.gitignore` లో ఉంది.
పూర్తి ప్రొవైడర్ సూచనలు [`providers.md`](03-providers.md) లో ఉన్నాయి.

## 4. తర్వాత ఏం?

| నేను ఇష్టం పడతాను…       | వెళ్ళండి…                                                               |
|--------------------------|-------------------------------------------------------------------------|
| పాఠం 1 ప్రారంభించండి       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM ప్రొవైడర్ సెటప్ చేయండి | [`providers.md`](03-providers.md)                                       |
| ఇతర విద్యార్థులను కలవండి   | [మా Discord చేరండి](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. సమస్యల పరిష్కారం

| లక్షణం                                   | పరిష్కారం                                                     |
|-----------------------------------------|---------------------------------------------------------------|
| `python not found`                        | ఇన్‌స్టాల్ తర్వాత Python PATHకు జోడించండి లేదా టర్మినల్ మళ్లీ ప్రారంభించండి |
| `pip` వృద్ధి చేయలేకపోవడం (Windows)        | `pip install --upgrade pip setuptools wheel` తర్వాత మళ్లీ ప్రయత్నించండి.  |
| `ModuleNotFoundError: dotenv`              | `pip install -r requirements.txt` నడపండి (ఎన్‌వి ఇన్‌స్టాల్ కాలేదు).       |
| Docker బిల్డ్ విఫలం *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → డిస్క్ సైజ్ పెంచండి.      |
| VS Code మళ్లీ తెరవమని అడుగుతుంది           | మీరు రెండు ఆప్షన్‌లు ఒకేసారి యాక్టివ్ అవ్వచ్చు; ఒకదానినై ఎంచుకోండి (venv **లేదా** కంటెయినర్) |
| OpenAI 401 / 429 లోపాలు                     | `OPENAI_API_KEY` విలువ / అభ్యర్ధన రేటు పరిమితులు తనిఖీ చేయండి.       |
| Conda ఉపయోగంలో లోపాలు                     | Microsoft AI లైబ్రరీలను `conda install -c microsoft azure-ai-ml` తో ఇన్స్టాల్ చేయండి |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->