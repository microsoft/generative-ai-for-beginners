# ထည့်သွင်းရေးသားမှုဒေတာပြင်ဆင်ခြင်း

ထည့်သွင်းရေးသားမှုဒေတာပြင်ဆင်ခြင်း စက်ရုံများသည် YouTube ဗီဒီယိုစာတမ်းများကိုဒေါင်းလုဒ်ဆွဲပြီး Semantic Search with OpenAI Embeddings and Functions စမ်းသပ်မှုနမူနာနှင့် အသုံးပြုနိုင်ရန်အတွက် ပြင်ဆင်ပေးသည်။

ထည့်သွင်းရေးသားမှုဒေတာပြင်ဆင်ခြင်း စက်ရုံများကို Windows 11, macOS Ventura နှင့် Ubuntu 22.04 (နှင့်အထက်) ၏ နောက်ဆုံးထုတ်ဗားရှင်းများပေါ်တွင် စမ်းသပ်ပြီးဖြစ်ပါသည်။

## လိုအပ်သော Azure OpenAI Service သင့်တော်မှုများကို ဖန်တီးရန်

> [!IMPORTANT]
> OpenAI နှင့် သွယ်တန်းမှုရှိအောင် Azure CLI ကို နောက်ဆုံးဗားရှင်းသို့ تحديث ပြုလုပ်ရန် ညွှန်ကြားပါသည်
> [Documents](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) တွင်ကြည့်ရှုပါ

1. Resource group တစ်ခု ဖန်တီးပါ

> [!NOTE]
> ဤညွှန်ကြားချက်များတွင် "semantic-video-search" ဟုအမည်ပေးထားသော အရှေ့အမေရိက resource group ကို အသုံးပြုပါသည်။
> သင် resource group အမည်ပြောင်းနိုင်သော်လည်း resource များအတွက် တည်နေရာပြောင်းလဲသောအခါမှာ၊
> [မော်ဒယ် ရရှိနိုင်မှု အရေအတွက်ဇယား](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ကို စစ်ဆေးပါ။

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service resource တစ်ခု ဖန်တီးပါ။

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ဤ application တွင် အသုံးပြုရန် endpoint နှင့် key များ ရယူပါ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. အောက်ပါ မော်ဒယ်များကို ထည့်သွင်းပါ -
   - `text-embedding-ada-002` ဗားရှင်း `2` အထက် သို့မဟုတ် အထက်ဆုံး၊ အမည် `text-embedding-ada-002`
   - `gpt-4o-mini` အမည် `gpt-4o-mini`

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

## လိုအပ်သော ဆော့ဖ်ဝဲများ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် ထက်မြင့်သောဗားရှင်း

## ပတ်ဝန်းကျင် အနက်အကြောင်းအရာများ

အောက်ပါ ပတ်ဝန်းကျင် အနက်အကြောင်းအရာများသည် YouTube ထည့်သွင်းရေးသားမှုဒေတာပြင်ဆင်ခြင်း စက်ရုံများ အသုံးပြုမှုအတွက် လိုအပ်သည်။

### Windows တွင်

ပတ်ဝန်းကျင်အနက်များကို သင့် `user` ပတ်ဝန်းကျင်အနက်များသို့ ထည့်သွင်းရန် အကြံပြုသည်။
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] ၏ `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- သင်၏ PowerShell profile တွင် ပတ်ဝန်းကျင်အနက်များကို ထည့်သွင်းနိုင်ပါသည်။

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux နှင့် macOS တွင်

အောက်ပါ export များကို သင့် `~/.bashrc` သို့မဟုတ် `~/.zshrc` ဖိုင်များတွင် ထည့်သွင်းရန် အကြံပြုသည်။

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## လိုအပ်သော Python အသုံးပြုနိုင်သော စာကြည့်တိုက်များ ထည့်သွင်းရန်

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)ကို မထည့်သွင်းထားပါက ထည့်သွင်းပါ။
1. `Terminal` ပြတင်းပေါက်မှ စမ်းသပ်မှုကို သင့်ကြိုက်နှစ်သက်ရာ repo ဖိုဒါသို့ clone ဆွဲပါ။

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ဖိုဒါသို့ သွားပါ။

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python virtual environment တစ်ခု ဖန်တီးပါ။

    Windows တွင် -

    ```powershell
    python -m venv .venv
    ```

    macOS နှင့် Linux တွင် -

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment ကို active လုပ်ပါ။

   Windows တွင် -

   ```powershell
   .venv\Scripts\activate
   ```

   macOS နှင့် Linux တွင် -

   ```bash
   source .venv/bin/activate
   ```

1. လိုအပ်သော စာကြည့်တိုက်များ ထည့်သွင်းပါ။

   Windows တွင် -

   ```powershell
   pip install -r requirements.txt
   ```

   macOS နှင့် Linux တွင် -

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ထည့်သွင်းရေးသားမှုဒေတာပြင်ဆင်ခြင်း စက်ရုံများကို လည်ပတ်ပါ

### Windows တွင်

```powershell
.\transcripts_prepare.ps1
```

### macOS နှင့် Linux တွင်

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->