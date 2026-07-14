# ఈ కోర్సుతో మొదలయ్యే విధానం

మీరు ఈ కోర్సును ప్రారంభించి, Generative AI తో మీరు ఏం సృష్టించగలరో చూడటానికి మేము చాలా ఉత్సాహంగా ఉన్నాము!

మీ విజయం కోసం, ఈ పేజీ సెటప్ దశలు, సాంకేతిక అవసరాలు, మరియు సహాయం అవసరమైతే ఎక్కడ పొందగలరో వివరిస్తుంది.

## సెటప్ దశలు

ఈ కోర్సును ప్రారంభించడానికి, మీరు క్రింది దశలను పూర్తి చేయాలి.

### 1. ఈ రిపోను ఫోర్క్ చేయండి

[ఈ మొత్తం రిపోను ఫోర్క్ చేయండి](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) మీ స్వంత GitHub ఖాతాకు, తద్వారా మీరు ఏ కోడ్ ను మార్చి ఛాలెంజ్‌లు పూర్తి చేయవచ్చు. మీరు కూడా [ఈ రిపోకు స్టార్ (🌟) కూడా ఇవ్వొచ్చు](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) దీనిని మరియు సంబంధించిన రిపోల‌ను తేలికగా కనుగొనేందుకు.

### 2. కోడ్‌స్పేస్ సృష్టించండి

కోడ్ నడపేప్పుడు ఏ డిపెండెన్సీ సమస్యలు రాకుండా ఉండేందుకు, ఈ కోర్సును [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) లో నడపడం సిఫార్సు చేస్తాము.

మీ ఫోర్క్ లో: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/te/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 సీక్రెట్ జోడించండి

1. ⚙️ గేర్ ఐకాన్ -> కమాండ్ పెలెట్ -> Codespaces : Manage user secret -> Add a new secret.
2. పేరు OPENAI_API_KEY, మీ కీని పేస్ట్ చేసి, సేవ్ చేయండి.

### 3. తర్వాత ఏమిటీ?

| నేను ఏమి చేయాలనుకుంటున్నాను... | వెళ్ళే స్థలం...                                                     |
|---------------------|-------------------------------------------------------------------------|
| పాఠం 1 ప్రారంభించండి      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ఆఫ్‌లైన్‌లో పని చేయండి        | [`setup-local.md`](02-setup-local.md)                                   |
| LLM ప్రొవైడర్ సెటప్ చేయండి | [`providers.md`](03-providers.md)                                        |
| ఇతర విద్యార్థులను కలుసుకోండి | [మా Discord లో చేరాలంటే](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## సమస్య పరిష్కారం


| లక్షణం                                   | పరిష్కారం                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| కంటైనర్ బిల్డ్ 10 నిమిషాలకంటే ఎక్కువ సమయం తీసుకుంటున్నది            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | టెర్మినల్ జతచేయబడలేదు; **+** పై క్లిక్ చేసి *bash* ఎంచుకోండి                   |
| OpenAI నుండి `401 Unauthorized`            | తప్పు లేదా కాలపరిమితి వచ్చిన `OPENAI_API_KEY`                                |
| VS Code “Dev container mounting…” చూపిస్తోంది   | బ్రౌజర్ టాబ్‌ను రీఫ్రెష్ చేయండి - Codespaces కొన్నిసార్లు కనెక్షన్ పోతుంది   |
| నోట్‌బుక్ కర్నెల్ లేదు                   | నోట్‌బుక్ మెనూ ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   యూనిక్స్-ఆధారిత సిస్టమ్స్:

   ```bash
   touch .env
   ```

   విండోస్:

   ```cmd
   echo . > .env
   ```

3. **`.env` ఫైల్ ను సవరించండి**: `.env` ఫైల్ ను టెక్స్ట్ ఎడిటర్ లో (ఉదాహరణకు, VS Code, Notepad++, లేదా ఏదైనా ఎడిటర్) తెరిచి, దిగువ లైన్లను జోడించండి, ప్లేస్‌హోల్డర్ల స్థానంలో మీ అసలు Microsoft Foundry Models ఎండ్‌పాయింట్ మరియు కీ ని చేర్చండి (వివరాలకు [`providers.md`](03-providers.md) చూడండి):

   > **గమనిక:** GitHub Models (మరియు దాని `GITHUB_TOKEN` వేరియబుల్) జూలై 2026 ముగింపుకి రిటైర్ అవుతుంది. దాని బదులు [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ఉపయోగించండి.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **ఫైల్ సేవ్ చేయండి**: మార్పులు సేవ్ చేసి, టెక్స్ట్ ఎడిటర్ ను మూసివేయండి.

5. **`python-dotenv` ని ఇన్‌స్టాల్ చేయండి**: మీరు ఇంకా చేయకపోతే, `.env` ఫైల్ నుండి ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ను మీ Python అప్లికేషన్ లో లోడ్ చేయడానికి `python-dotenv` ప్యాకేజీని ఇన్‌స్టాల్ చేయాలి. దీన్ని `pip` ద్వారా ఇన్‌స్టాల్ చేయవచ్చు:

   ```bash
   pip install python-dotenv
   ```

6. **మీ Python స్క్రిప్ట్ లో ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ను లోడ్ చేయండి**: మీ Python స్క్రిప్ట్ లో `python-dotenv` ప్యాకేజీ ఉపయోగించి `.env` ఫైల్ నుండి ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ను లోడ్ చేయండి:

   ```python
   from dotenv import load_dotenv
   import os

   # .env ఫైల్ నుండి వాతావరణ చరాలు లోడ్ చేయండి
   load_dotenv()

   # Microsoft Foundry Models వేరియబుల్స్‌కు அணுகండి
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

అంతే! మీరు విజయవంతంగా `.env` ఫైల్ సృష్టించి, Microsoft Foundry Models క్రెడెన్షియల్స్ జోడించి వాటిని Python అప్లికేషన్ లో లోడ్ చేసుకున్నారు.

## మీ కంప్యూటర్ లో లోకల్ గా ఎలా నడపాలి

కోడ్ ను మీ కంప్యూటర్ లో లోకల్ గా నడపడానికి, మీరు [Python ఇన్‌స్టాల్ చేయాలి](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) అని ఉంటుంది.

తరువాత, రిపోజిటరీ ఉపయోగించడానికి, దాన్ని క్లోన్ చేయాలి:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

అన్ని ఫైల్స్ డౌన్‌లోడ్ అయిన తర్వాత, మీరు ప్రారంభించవచ్చు!

## ఐచ్ఛిక దశలు

### మినీకాండాను ఇన్‌స్టాల్ చేయడం

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) అనేది [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python మరియు కొన్ని ప్యాకేజీలను ఇన్‌స్టాల్ చేయడానికి తేలికపాటి ఇన్‌స్టాలర్.
Conda స్వతంత్రంగా ఒక ప్యాకేజ్ మేనేజర్, ఇది విభిన్న Python [**వర్చువల్ ఎన్విరాన్‌మెంట్స్**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) మరియు ప్యాకేజీలను సులభంగా సెటప్ చేయడం మరియు మారడానికి సహాయపడుతుంది. ఇది `pip` ద్వారా అందుబాటులో లేని ప్యాకేజీలను కూడా ఇన్‌స్టాల్ చేయడానికి ఉపయోగపడుతుంది.

మీరు [MiniConda ఇన్‌స్టాలేషన్ గైడ్](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ను అనుసరించవచ్చు.

Miniconda ఇన్‌స్టాల్ చేసిన తర్వాత, మీరు రిపోజిటరీని క్లోన్ చేయాలి (ఇప్పటికే చేయకపోతే):

తరువాత, మీరు ఒక వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించాలి. Conda తో దీ‌ని చేయడానికి, కొత్త ఎన్విరాన్‌మెంట్ ఫైల్ (_environment.yml_) సృష్టించండి. మీరు Codespaces అనుసరిస్తుంటే, దీన్ని `.devcontainer` డైరెక్టరీ లో, అర్ధం `.devcontainer/environment.yml` లో సృష్టించండి.

మీ ఎన్విరాన్‌మెంట్ ఫైల్‌ను క్రింది కత్తెర‌తో నింపండి:

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

మీరు conda ఉపయోగించేటప్పుడు దోషాలు వస్తున్నాయంటే, మీరు క్రింది కమాండ్ ను టెర్మినల్ లో నేరుగా అమలు చేసి Microsoft AI లైబ్రరీలను మాన్యువల్ గా ఇన్‌స్టాల్ చేయవచ్చు.

```
conda install -c microsoft azure-ai-ml
```

ఎన్విరాన్‌మెంట్ ఫైల్ మనకు అవసరమైన డిపెండెన్సీలను పేర్కొంటుంది. `<environment-name>` అనేది మీరు మీ Conda ఎన్విరాన్‌మెంట్ కి ఇవ్వాలనుకునే పేరు, మరియు `<python-version>` అనేది మీరు ఉపయోగించాలనుకునే Python వెర్షన్, ఉదాహరణకు, `3` అనేది Python తాజా ప్రధాన వెర్షన్.

ఈ దశ పూర్తి అయిన తర్వాత, కింది ఆదేశాలను మీ కమాండ్ లైన్/టెర్మినల్ లో నడపడం ద్వారా మీ Conda ఎన్విరాన్‌మెంట్ సృష్టించవచ్చు.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ఉపపథం కేవలం Codespace సెట్టింగ్స్‌కు అమలు అవుతుంది
conda activate ai4beg
```

ఏదైనా సమస్యలుంటే [Conda ఎన్విరాన్‌మెంట్ గైడ్](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ను చూడండి.

### Python మద్దతు విస్తరణతో Visual Studio Code ఉపయోగించడం

ఈ కోర్సు కోసం, [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ఎడిటర్ ను [Python మద్దతు విస్తరణ](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) తో ఉపయోగించమని మేము సిఫారసు చేస్తాము. ఇది చచ్చిక సిఫారసు కానీ తప్పనిసరి కాదు.

> **గమనిక**: కోర్సు రిపోజిటరీని VS Code లో తెరిచినప్పుడే, మీరు ప్రాజెక్టును కంటైనర్ లో సెటప్ చేసుకోవచ్చు. దీని కారణం కోర్సు రిపోజిటరీలో ఉండే [ప్రత్యేక `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) డైరెక్టరీ.

> **గమనిక**: మీరు రిపోజిటరీని క్లోన్ చేసి VS Code లో తెరిచిన వెంటనే, అది మీరు Python మద్దతు విస్తరణని ఇన్‌స్టాల్ చేయమని సూచిస్తుంది.

> **గమనిక**: VS Code మీరు రిపోజిటరీను కంటైనర్ లో తిరిగి తెరవమని సూచించినా, మీరు లొకల్‌లో ఇన్‌స్టాల్ చేసిన Python వర్షన్ ఉపయోగించేందుకు ఈ సూచనను తిరస్కరించండి.

### బ్రౌజర్‌లో Jupyter ఉపయోగించడం

మీరు ప్రాజెక్టుపై [Jupyter వాతావరణం](https://jupyter.org?WT.mc_id=academic-105485-koreyst) కూడా బ్రౌజర్‌లోనే పనిచేయవచ్చు. క్లాసిక్ Jupyter మరియు [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) తాను ఆటో-కంప్లీషన్, కోడ్ హైలైట్ వంటి ఫీచర్లు కలిగిన మంచి డెవలప్‌మెంట్ వాతావరణం అందిస్తాయి.

లొకల్‌లో Jupyter మొదలుపెట్టాలంటే, టెర్మినల్/కమాండ్ లైన్ కి వెళ్ళి, కోర్సు డైరెక్టరీ లోకి వెళ్లి, క్రింది ఆదేశాన్ని అమలు చేయండి:

```bash
jupyter notebook
```

లేదా

```bash
jupyterhub
```

దీని ఫలితంగా ఒక Jupyter ఇన్‌స్టాన్స్ ప్రారంభమవుతుంది, దాని యాక్సెస్ URL కమాండ్ లైన్ విండో లో చూపబడుతుంది.

మీరు URL ని యాక్సెస్ చేసిన తర్వాత, కోర్సు అవుట్‌లైన్ కనిపిస్తుంది మరియు ఏ `*.ipynb` ఫైల్ కి వెళ్లవచ్చు. ఉదాహరణకు, `08-building-search-applications/python/oai-solution.ipynb`.

### కంటైనర్ లో నడపడం

మీ కంప్యూటర్ లేదా కోడ్‌స్పేస్ లో అన్నిటినీ బదులుగా [కంటైనర్](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) ఉపయోగించవచ్చు. కోర్సు రిపోలో ప్రత్యేక `.devcontainer` ఫోల్డర్ వలన VS Code ప్రాజెక్టును ఒక కంటైనర్ లో సెట్ చేయగలుగుతుంది. Codespaces వెలుపల, ఇది Docker ఇన్‌స్టాల్ చేయాలని అవసరం, ఇది కొంత పని కావచ్చు, కాబట్టి కేవలం కంటైనర్లతో పట్ల అనుభవం ఉన్న వారికే మేము సిఫారసు చేస్తాము.

GitHub Codespaces ఉపయోగించినప్పుడు మీ API కీలు సురక్షితంగా ఉంచుకోవడానికి Codespace Secrets వాడటం ఉత్తమ మార్గం. దయచేసి మరింత సమాచారం కోసం [Codespaces సీక్రెట్స్ మేనేజ్‌మెంట్](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) గైడ్ ని అనుసరించండి.


## పాఠాలు మరియు సాంకేతిక అవసరాలు

ఈ కోర్సులో 6 భావన పాఠాలు మరియు 6 కోడింగ్ పాఠాలు ఉన్నాయి.

కోడింగ్ పాఠాల కోసం, మేము Azure OpenAI సర్వీస్ ఉపయోగిస్తున్నాము. ఈ కోడ్ నడపడానికి Azure OpenAI సర్వీస్ మరియు API కీ యాక్సెస్ ఉండాలి. యాక్సెస్ పొందడానికి మీరు [ఈ అప్లికేషన్ పూర్తి చేయాలి](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

మీ అప్లికేషన్ ప్రక్రియ జరుగుతున్నప్పుడు, ప్రతి కోడింగ్ పాఠం తో కూడిన `README.md` ఫైల్‌లో కోడ్ మరియు అవుట్‌పుట్లను చూడవచ్చు.

## Azure OpenAI సర్వీస్ మొదటిసారి ఉపయోగించేటప్పుడు

మీరు Azure OpenAI సర్వీస్ తో మొదటిసారి పని చేస్తున్నట్లయితే, దయచేసి ఈ గైడ్ అనుసరించండి [Azure OpenAI సర్వీస్ రిసోర్స్ సృష్టించడం మరియు డిప్లాయ్ చేయడం](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API మొదటిసారి ఉపయోగించేటప్పుడు

మీరు OpenAI API తో మొదటిసారి పని చేస్తున్నట్లయితే, దయచేసి ఈ గైడ్ అనుసరించండి [ఇంటర్‌ఫేస్ సృష్టించడం మరియు ఉపయోగించడం](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## ఇతర అభ్యసనార్థులను కలుసుకుందాం

మేము అధికారిక [AI కమ్యూనిటీ Discord సర్వర్](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) లో ఇతర అభ్యసనార్థులను కలుసుకునేందుకు ఛానెల్స్ సృష్టించాము. ఇది Generative AI లో మెరుగుపడాలనుకునే ఒరిగిన భావమున్న వ్యాపారవేత్తలు, బిల్డర్స్, విద్యార్థులు మరియు ఇతరుల నెట్వర్కింగ్ కోసం గొప్ప మార్గం.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ప్రాజెక్ట్ టీమ్ కూడా ఈ Discord సర్వర్ లో ఉండి అభ్యసనార్థులకు సహాయం అందిస్తారు.

## సహాయం చేయండి

ఈ కోర్సు ఓపెన్-సోర్స్ ప్రాజెక్ట్. మీరు ఏ అభివృద్ధులు లేదా సమస్యలు గమనిస్తే, దయచేసి [పుల్ రిక్వెస్ట్](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) సృష్టించండి లేదా [GitHub ఇష్యూ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) నమోదు చేయండి.

ప్రాజెక్ట్ టీమ్ అన్ని కాంట్రిబ్యూషన్లను ట్రాక్ చేస్తుంది. Generative AI లో మీ కెరీర్ నిర్మించడానికి ఓపెన్ సోర్స్ కి తోడ్పడటం అద్భుతమైన మార్గం.

ఎక్కువ భాగం కాంట్రిబ్యూషన్లు మీరు కాంట్రిబ్యూటర్ లైసెన్స్ అగ్రిమెంట్ (CLA) కి అంగీకరిస్తున్నారని మరియు మీ కాంట్రిబ్యూషన్ వాడకం హక్కులను మాకు ఇచ్చేదిగా ప్రకటిస్తున్నారని అవసరం. వివరాలకు [CLA, Contributor License Agreement వెబ్‌సైట్](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) చూడండి.

ముఖ్యమైన విషయం: ఈ రీపో లోని టెక్స్ట్ అనువాదం చేయేప్పుడు, దయచేసి మీకున్న భాషలోనే అనువాదం చేయండి మరియు యంత్ర అనువాదం వాడకండి. మనం అనువాదాలను కమ్యూనిటీ ద్వారా విశ్లేషిస్తాము, కనుక మీరు ప్రావీణ్యం ఉన్న భాషల్లోనే స్వచ్ఛందంగా మాత్రమే అనువదించాలి.

మీరు పుల్ రిక్వెస్ట్ సమర్పించినప్పుడు, CLA-బాట్ మీకు CLA అందజేయాల్సిన అవసరం ఉందో లేదో నిర్ణయించి, PR ని సరైన లేబుల్ లేదా వ్యాఖ్యతో అలంకరించుతుంది. బాట్ ఇచ్చే సూచనలను అనుసరించండి. మీరు ఈ ప్రక్రియను ఒక్కసారి మాత్రమే చేయాలి, అన్ని రిపోస్ కొరకు ఉపయోగించే CLAకి.


ఈ ప్రాజెక్ట్ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ను అంగీకరించింది. మరింత సమాచారం కోసం Code of Conduct FAQ చదవండి లేదా ఏదైన అదనపు ప్రశ్నలు లేదా వ్యాఖ్యల కోసం [Email opencode](opencode@microsoft.com) ను సంప్రదించండి.

## ప్రారంభిద్దాం

ఇప్పుడు మీరు ఈ కోర్సును పూర్తి చేయడానికి అవసరమైన దశలను పూర్తి చేసుకున్నందున, [జనరేటివ్ AI మరియు LLM లకు పరిచయం](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ద్వారా ప్రారంభిద్దాం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->