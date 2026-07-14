# ట్రాన్స్‌క్ఫిప్షన్ డేటా ప్రిప్

ట్రాన్స్‌క్ఫిప్షన్ డేటా ప్రిప్ స్క్రిప్టులు YouTube వీడియో ట్రాన్స్‌క్ఫిప్ట్స్‌ను డౌన్లోడ్ చేసి, ఆప్టెన్‌ఏఐ ఎంబెడ్డింగ్స్ మరియు ఫంక్షన్స్ నమూనాతో సెమాంటిక్ సర్చ్ కోసం తయారుచేస్తాయి.

ట్రాన్స్‌క్ఫిప్షన్ డేటా ప్రిప్ స్క్రిప్టులు తాజా విడుదలలు Windows 11, macOS Ventura మరియు Ubuntu 22.04 (మరియు దాని పై) లో పరీక్షించబడ్డాయి.

## అవసరమైన Azure OpenAI సేవ వనరులు సృష్టించండి

> [!IMPORTANT]
> OpenAI తో అనుకూలతపూర్వకంగా ఉండేందుకు Azure CLIని తాజాకరణ చేయమని మేము సూచిస్తున్నాము
> [డాక్యుమెంటేషన్](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) చూడండి

1. రిసోర్స్ గ్రూప్ సృష్టించండి

> [!NOTE]
> ఈ సూచనల కోసం మేము East US లో "semantic-video-search" అనే రిసోర్స్ గ్రూప్ ఉపయోగిస్తున్నాము.
> మీరు రిసోర్స్ గ్రూప్ పేరును మార్చుకోవచ్చు, కానీ వనరుల యొక్క స్థానాన్ని మార్చేటప్పుడు, 
> [మోడల్ అందుబాటు పట్టిక](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)ని తనిఖీ చేయండి.

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI సేవ వనరును సృష్టించండి.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ఈ ప్రవర్జనలో వినియోగించడానికి ఎండ్పాయింట్ మరియు కీలను పొందండి

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ఈ మోడల్స్‌ను డిప్లాయ్ చేయండి:
   - `text-embedding-ada-002` సంచిక `2` లేదా ఎక్కువ, పేరు `text-embedding-ada-002`
   - `gpt-4o-mini` పేరు `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## అవసరమైన సాఫ్ట్‌వేర్

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) లేదా ఎక్కువ

## పర్యావరణ ఛరాలు

YouTube ట్రాన్స్‌క్ఫిప్షన్ డేటా ప్రిప్ స్క్రిప్టులను నడిపించడానికి క్రింది పర్యావరణ ఛరాలు అవసరం.

### Windows పై

మీ `user` పర్యావరణ ఛరాలలో ఈ ఛరాలను చేర్చడం సిఫార్సు చేయబడుతుంది.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] కోసం `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- మీరు ఈ పర్యావరణ ఛరాలను మీ PowerShell ప్రొఫైలులో చేర్చుకోవచ్చు.

```powershell
$env:AZURE_OPENAI_API_KEY = "<మీ Azure OpenAI సేవ API కీ>"
$env:AZURE_OPENAI_ENDPOINT = "<మీ Azure OpenAI సేవ ఎండ్పాయింట్>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<మీ Azure OpenAI సేవ మోడల్ డిప్లాయ్ పేరు>"
$env:GOOGLE_DEVELOPER_API_KEY = "<మీ Google డెవలపర్ API కీ>"
``` -->

### Linux మరియు macOS పై

మీ `~/.bashrc` లేదా `~/.zshrc` ఫైల్‌లో క్రింది ఎగుమతులను చేర్పించాలని సూచించబడింది.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## అవసరమైన Python లైబ్రరీలను ఇన్స్టాల్ చేయండి

1. [git క్లయింట్](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ఇన్స్టాల్ చేయబడలేదంటే, దాన్ని ఇన్స్టాల్ చేయండి.
1. ఒక `Terminal` విండో నుండి, నమూనాను మీ ఇష్టమైన రిపో ఫోల్డర్‌కు క్లోన్ చేయండి.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ఫోల్డర్‌కి వెళ్లండి.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి.

    Windows పై:

    ```powershell
    python -m venv .venv
    ```

    macOS మరియు Linux పై:

    ```bash
    python3 -m venv .venv
    ```

1. Python వర్చువల్ ఎన్విరాన్‌మెంట్ సక్రియం చేయండి.

   Windows పై:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS మరియు Linux పై:

   ```bash
   source .venv/bin/activate
   ```

1. అవసరమైన లైబ్రరీలను ఇన్స్టాల్ చేయండి.

   Windows పై:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS మరియు Linux పై:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ట్రాన్స్‌క్ఫిప్షన్ డేటా ప్రిప్ స్క్రిప్ట్‌లను నడపండి

### Windows పై

```powershell
.\transcripts_prepare.ps1
```

### macOS మరియు Linux పై

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->