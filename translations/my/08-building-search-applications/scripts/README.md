<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:13:47+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "my"
}
-->
# Transcription data prep

Transcription data prep script များသည် YouTube ဗီဒီယိုစာတမ်းများကိုဒေါင်းလုပ်လုပ်ပြီး Semantic Search with OpenAI Embeddings and Functions နမူနာတွင် အသုံးပြုရန်အတွက် ပြင်ဆင်ပေးသည်။

Transcription data prep script များကို Windows 11 နောက်ဆုံးထွက်ဗားရှင်းများ၊ macOS Ventura နှင့် Ubuntu 22.04 (နှင့်အထက်) တွင် စမ်းသပ်ပြီးဖြစ်သည်။

## လိုအပ်သော Azure OpenAI Service အရင်းအမြစ်များ ဖန်တီးခြင်း

> [!IMPORTANT]
> OpenAI နှင့် ကိုက်ညီမှုရှိစေရန် Azure CLI ကို နောက်ဆုံးဗားရှင်းသို့ အပ်ဒိတ်လုပ်ရန် အကြံပြုပါသည်။
> [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။

1. Resource group တစ်ခု ဖန်တီးပါ။

> [!NOTE]
> ဤညွှန်ကြားချက်များတွင် East US တွင် "semantic-video-search" ဟု အမည်ပေးထားသော resource group ကို အသုံးပြုထားသည်။
> Resource group အမည်ကို ပြောင်းလဲနိုင်သော်လည်း၊ resource များ၏ တည်နေရာကို ပြောင်းလဲသောအခါ
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ကို စစ်ဆေးပါ။

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service resource တစ်ခု ဖန်တီးပါ။

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ဤ application တွင် အသုံးပြုရန် endpoint နှင့် keys များ ရယူပါ။

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. အောက်ပါ မော်ဒယ်များကို တပ်ဆင်ပါ။
   - `text-embedding-ada-002` ဗားရှင်း `2` သို့မဟုတ် အထက်၊ အမည် `text-embedding-ada-002`
   - `gpt-35-turbo` ဗားရှင်း `0613` သို့မဟုတ် အထက်၊ အမည် `gpt-35-turbo`

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

## လိုအပ်သော ဆော့ဖ်ဝဲများ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် အထက်

## ပတ်ဝန်းကျင် အပြောင်းအလဲများ

YouTube transcription data prep script များကို လည်ပတ်ရန် အောက်ပါ ပတ်ဝန်းကျင် အပြောင်းအလဲများ လိုအပ်သည်။

### Windows တွင်

`user` ပတ်ဝန်းကျင် အပြောင်းအလဲများထဲသို့ ထည့်သွင်းရန် အကြံပြုသည်။
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` ကို သွားပါ။

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Linux နှင့် macOS တွင်

အောက်ပါ export များကို သင့် `~/.bashrc` သို့မဟုတ် `~/.zshrc` ဖိုင်ထဲသို့ ထည့်သွင်းရန် အကြံပြုသည်။

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## လိုအပ်သော Python libraries များ ထည့်သွင်းခြင်း

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ကို မထည့်သွင်းထားသေးပါက ထည့်သွင်းပါ။
1. `Terminal` ပြတင်းပေါ်မှ သင့်နှစ်သက်ရာ repo ဖိုလ်ဒါသို့ နမူနာကို clone လုပ်ပါ။

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ဖိုလ်ဒါသို့ သွားပါ။

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python virtual environment တစ်ခု ဖန်တီးပါ။

    Windows တွင်:

    ```powershell
    python -m venv .venv
    ```

    macOS နှင့် Linux တွင်:

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment ကို ဖွင့်ပါ။

   Windows တွင်:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS နှင့် Linux တွင်:

   ```bash
   source .venv/bin/activate
   ```

1. လိုအပ်သော libraries များ ထည့်သွင်းပါ။

   Windows တွင်:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS နှင့် Linux တွင်:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube transcription data prep script များကို လည်ပတ်ခြင်း

### Windows တွင်

```powershell
.\transcripts_prepare.ps1
```

### macOS နှင့် Linux တွင်

```bash
./transcripts_prepare.sh
```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။