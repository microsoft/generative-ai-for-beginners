<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T17:00:56+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "my"
}
-->
# အသံဖျော်ဖြေရေး ဒေတာ ပြင်ဆင်ခြင်း

အသံဖျော်ဖြေရေး ဒေတာ ပြင်ဆင်ခြင်း script များသည် YouTube ဗီဒီယို အသံဖျော်ဖြေရေးများကို ဒေါင်းလုဒ်လုပ်ပြီး OpenAI Embeddings နှင့် Functions နမူနာနှင့်အတူ အသုံးပြုရန် ပြင်ဆင်ပေးသည်။

အသံဖျော်ဖြေရေး ဒေတာ ပြင်ဆင်ခြင်း script များကို နောက်ဆုံးထွက်ရှိထားသော Windows 11, macOS Ventura နှင့် Ubuntu 22.04 (နှင့် အထက်) တွင် စမ်းသပ်ပြီးဖြစ်သည်။

## လိုအပ်သော Azure OpenAI Service ရင်းမြစ်များ ဖန်တီးရန်

> [!IMPORTANT]
> OpenAI နှင့် သင့်လျော်မှုရှိစေရန် အတွက် Azure CLI ကို နောက်ဆုံးဗားရှင်းသို့ အပ်ဒိတ်လုပ်ရန် အကြံပြုပါသည်။
> [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။

1. ရင်းမြစ်အုပ်စုတစ်ခု ဖန်တီးပါ

> [!NOTE]
> ဤညွှန်ကြားချက်များအတွက် ကျွန်ုပ်တို့သည် East US ရှိ "semantic-video-search" ဟုခေါ်သော ရင်းမြစ်အုပ်စုကို အသုံးပြုပါသည်။
> ရင်းမြစ်အုပ်စု၏ အမည်ကို ပြောင်းလဲနိုင်ပါသည်၊ ဒါပေမယ့် ရင်းမြစ်များအတွက် တည်နေရာကို ပြောင်းလဲသည့်အခါ 
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ကို စစ်ဆေးပါ။

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service ရင်းမြစ်တစ်ခု ဖန်တီးပါ။

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ဤအပလီကေးရှင်းတွင် အသုံးပြုရန် endpoint နှင့် keys ကို ရယူပါ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. အောက်ပါ မော်ဒယ်များကို တင်ဆောင်ပါ:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

## လိုအပ်သော ဆော့ဖ်ဝဲ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် အထက်

## ပတ်ဝန်းကျင် အပြောင်းအလဲများ

YouTube အသံဖျော်ဖြေရေး ဒေတာ ပြင်ဆင်ခြင်း script များကို အလုပ်လုပ်ရန် အောက်ပါ ပတ်ဝန်းကျင် အပြောင်းအလဲများ လိုအပ်ပါသည်။

### Windows တွင်

သင့် `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` တွင် အပြောင်းအလဲများ ထည့်သွင်းရန် အကြံပြုပါသည်။

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux နှင့် macOS တွင်

သင့် `~/.bashrc` or `~/.zshrc` ဖိုင်တွင် အောက်ပါ exports များ ထည့်သွင်းရန် အကြံပြုပါသည်။

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## လိုအပ်သော Python စာကြည့်တိုက်များ ထည့်သွင်းပါ

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ကို ထည့်သွင်းပါ၊ ထည့်သွင်းပြီးသားမဟုတ်လျှင်။
1. `Terminal` ဝင်းဒိုးမှ သင့်နှစ်သက်ရာ repo ဖိုလ်ဒါသို့ နမူနာကို clone လုပ်ပါ။

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

1. Python virtual environment ကို အကောင်အထည်ဖော်ပါ။

   Windows တွင်:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS နှင့် Linux တွင်:

   ```bash
   source .venv/bin/activate
   ```

1. လိုအပ်သော စာကြည့်တိုက်များ ထည့်သွင်းပါ။

   Windows တွင်:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS နှင့် Linux တွင်:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube အသံဖျော်ဖြေရေး ဒေတာ ပြင်ဆင်ခြင်း script များကို အလုပ်လုပ်ပါ

### Windows တွင်

```powershell
.\transcripts_prepare.ps1
```

### macOS နှင့် Linux တွင်

```bash
./transcripts_prepare.sh
```

**ဖြန့်ချိချက်**:  
ဒီစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ဆိုခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို လိုက်နာရမည့် အရင်းအမြစ်အဖြစ် စဉ်းစားသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူကြီးမင်းများ သက်ဆိုင်ရာ လူသား ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အနားလျားမှုများ သို့မဟုတ် အဓိပ္ပာယ် မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။