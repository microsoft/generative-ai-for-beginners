<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-12-19T20:44:48+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "te"
}
-->
# ట్రాన్స్క్రిప్షన్ డేటా ప్రిప్

ట్రాన్స్క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్టులు YouTube వీడియో ట్రాన్స్క్రిప్ట్లను డౌన్లోడ్ చేసి, OpenAI ఎంబెడ్డింగ్స్ మరియు ఫంక్షన్స్ తో సెమాంటిక్ సెర్చ్ నమూనా కోసం ఉపయోగించడానికి సిద్ధం చేస్తాయి.

ట్రాన్స్క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్టులు తాజా విడుదలలైన Windows 11, macOS Ventura మరియు Ubuntu 22.04 (మరియు పై) లో పరీక్షించబడ్డాయి.

## అవసరమైన Azure OpenAI సర్వీస్ వనరులను సృష్టించండి

> [!IMPORTANT]
> OpenAI తో అనుకూలత కోసం Azure CLI ను తాజా సంస్కరణకు నవీకరించమని మేము సూచిస్తున్నాము
> [డాక్యుమెంటేషన్](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) చూడండి

1. ఒక రిసోర్స్ గ్రూప్ సృష్టించండి

> [!NOTE]
> ఈ సూచనల కోసం మేము "semantic-video-search" అనే రిసోర్స్ గ్రూప్ ను East US లో ఉపయోగిస్తున్నాము.
> మీరు రిసోర్స్ గ్రూప్ పేరును మార్చవచ్చు, కానీ వనరుల స్థలాన్ని మార్చేటప్పుడు,
> [మోడల్ అందుబాటు పట్టిక](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ను తనిఖీ చేయండి.

```console
az group create --name semantic-video-search --location eastus
```

1. ఒక Azure OpenAI సర్వీస్ వనరును సృష్టించండి.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ఈ అప్లికేషన్ లో ఉపయోగించడానికి ఎండ్‌పాయింట్ మరియు కీలు పొందండి

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. క్రింది మోడల్స్ ను డిప్లాయ్ చేయండి:
   - `text-embedding-ada-002` సంస్కరణ `2` లేదా అంతకంటే ఎక్కువ, పేరు `text-embedding-ada-002`
   - `gpt-35-turbo` సంస్కరణ `0613` లేదా అంతకంటే ఎక్కువ, పేరు `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## అవసరమైన సాఫ్ట్‌వేర్

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) లేదా అంతకంటే ఎక్కువ

## ఎన్విరాన్‌మెంట్ వేరియబుల్స్

YouTube ట్రాన్స్క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్టులను నడపడానికి క్రింది ఎన్విరాన్‌మెంట్ వేరియబుల్స్ అవసరం.

### Windows లో

మీ `user` ఎన్విరాన్‌మెంట్ వేరియబుల్స్ లో వేరియబుల్స్ ను జోడించమని సూచిస్తున్నాము.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] కోసం `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- మీరు మీ PowerShell ప్రొఫైల్ లో ఎన్విరాన్‌మెంట్ వేరియబుల్స్ ను జోడించవచ్చు.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux మరియు macOS లో

మీ `~/.bashrc` లేదా `~/.zshrc` ఫైల్ లో క్రింది ఎగుమతులను జోడించమని సూచిస్తున్నాము.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## అవసరమైన Python లైబ్రరీలను ఇన్‌స్టాల్ చేయండి

1. [git క్లయింట్](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ఇన్‌స్టాల్ చేయబడకపోతే, దాన్ని ఇన్‌స్టాల్ చేయండి.
1. ఒక `Terminal` విండో నుండి, నమూనాను మీ ఇష్టమైన రిపో ఫోల్డర్ కు క్లోన్ చేయండి.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ఫోల్డర్ కు వెళ్లండి.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ఒక Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి.

    Windows లో:

    ```powershell
    python -m venv .venv
    ```

    macOS మరియు Linux లో:

    ```bash
    python3 -m venv .venv
    ```

1. Python వర్చువల్ ఎన్విరాన్‌మెంట్ ను యాక్టివేట్ చేయండి.

   Windows లో:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS మరియు Linux లో:

   ```bash
   source .venv/bin/activate
   ```

1. అవసరమైన లైబ్రరీలను ఇన్‌స్టాల్ చేయండి.

   Windows లో:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS మరియు Linux లో:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ట్రాన్స్క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్టులను నడపండి

### Windows లో

```powershell
.\transcripts_prepare.ps1
```

### macOS మరియు Linux లో

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->