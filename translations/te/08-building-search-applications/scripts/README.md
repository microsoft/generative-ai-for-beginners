# ట్రాన్స్‌క్రిప్షన్ డేటా ప్రిప్  

ట్రాన్స్‌క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్ట్‌లు యూట్యూబ్ వీడియో ట్రాన్స్‌క్రిప్ట్‌లను డౌన్లోడ్ చేసి, OpenAI ఎంబెడ్డింగ్స్ మరియు ఫంక్షన్స్ సమ్మిళిత సెమాంటిక్ సెర్చ్ కోసం ఉపయోగించడానికి సిద్ధం చేస్తాయి.  

ట్రాన్స్‌క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్ట్‌లు తాజా రిలీజ్‌లైన Windows 11, macOS Ventura మరియు Ubuntu 22.04 (మరియు పై) వద్ద పరీక్షించబడ్డాయి.  

## అవసరమైన Azure OpenAI సర్వీస్ వనరులు సృష్టించండి  

> [!IMPORTANT]  
> OpenAI తో అనుకూలత కలిగి ఉండేందుకు Azure CLI ను తాజా సంస్కరణకు అప్డేట్ చేయాలని మేము సూచిస్తున్నాము  
> [డాక్యుమెంటేషన్](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) చూడండి  

1. ఒక రిసోర్స్ గ్రూప్ సృష్టించండి  

> [!NOTE]  
> ఈ సూచనల కోసం మేము "semantic-video-search" అనే రిసోర్స్ గ్రూపును East US లో ఉపయోగిస్తున్నాము.  
> రిసోర్స్ గ్రూపు పేరును మీరు మార్చవచ్చు, కానీ వనరుల స్థానాన్ని మార్చేటప్పుడు,  
> [మోడల్ అందుబాటు పట్టిక](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ని పరిశీలించండి.  

```console
az group create --name semantic-video-search --location eastus
```
  
1. ఒక Azure OpenAI సర్వీస్ వనరును సృష్టించండి.  

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```
  
1. ఈ అప్లికేషన్‌లో ఉపయోగించడానికి ఎండ్పాయింట్ మరియు కీలు పొందండి  

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```
  
1. క్రింద పేర్కొన్న మోడళ్లను డిప్లాయ్ చేయండి:  
   - `text-embedding-ada-002` వెర్షన్ `2` లేదా అంతకంటే ఎక్కువ, పేరు `text-embedding-ada-002`  
   - `gpt-5-mini` పేరు `gpt-5-mini`  

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```
  
## అవసరమైన సాఫ్ట్‌వేర్  

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) లేదా అంతకంటే ఎక్కువ  

## పర్యావరణ వేరియబుల్స్  

యూట్యూబ్ ట్రాన్స్‌క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్ట్‌లను నడపడానికి క్రింది పర్యావరణ వేరియబుల్స్ అవసరం.  

### Windows పై  

వేరియబుల్స్‌ను మీ `user` పర్యావరణ వేరియబుల్స్‌లో జోడించమంటున్నాము.  
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] కి చెందిన `User variables` > `New`.  

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```
  
<!-- మీరు మీ PowerShell ప్రొఫైల్‌కు ఈ వేరియబుల్స్ జోడించవచ్చు.  

```powershell  
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"  
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"  
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"  
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"  
``` -->  

### Linux మరియు macOS పై  

కింది ఎగుమతులను మీ `~/.bashrc` లేదా `~/.zshrc` ఫైల్‌కు జోడించమంటున్నాము.  

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```
  
## అవసరమైన Python లైబ్రరీలను ఇన్‌స్టాల్ చేయండి  

1. [git క్లయింట్](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ఇన్‌స్టాల్ కాకపోతే ఇన్‌స్టాల్ చేయండి.  
1. `Terminal` విండో నుండి, సాంపిల్ కోడ్‌ను మీ ఇష్టమైన రిపో ఫోల్డర్‌కు క్లోన్ చేయండి.  

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```
  
1. `data_prep` ఫోల్డర్‌లోకి వెళ్ళండి.  

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```
  
1. ఒక Python వర్చువల్ ఎన్‌విరాన్మెంట్ సృష్టించండి.  

    Windows పై:  

    ```powershell
    python -m venv .venv
    ```
  
    macOS మరియు Linux పై:  

    ```bash
    python3 -m venv .venv
    ```
  
1. Python వర్చువల్ ఎన్‌విరాన్మెంట్ ను యాక్టివేట్ చేయండి.  

   Windows పై:  

   ```powershell
   .venv\Scripts\activate
   ```
  
   macOS మరియు Linux పై:  

   ```bash
   source .venv/bin/activate
   ```
  
1. అవసరమైన లైబ్రరీలను ఇన్‌స్టాల్ చేయండి.  

   Windows పై:  

   ```powershell
   pip install -r requirements.txt
   ```
  
   macOS మరియు Linux పై:  

   ```bash
   pip3 install -r requirements.txt
   ```
  
## YouTube ట్రాన్స్‌క్రిప్షన్ డేటా ప్రిప్ స్క్రిప్ట్‌లను నడిపించండి  

### Windows పై  

```powershell
.\transcripts_prepare.ps1
```
  
### macOS మరియు Linux పైన  

```bash
./transcripts_prepare.sh
```  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->