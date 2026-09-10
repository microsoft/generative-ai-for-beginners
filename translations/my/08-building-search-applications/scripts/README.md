# အသံနှင့် စာသားပြောင်းခြင်း ဒေတာ ပြင်ဆင်ခြင်း

အသံနှင့် စာသားပြောင်းခြင်း ဒေတာ ပြင်ဆင်ရေး စကရစ်ပတ်များသည် YouTube ဗီဒီယိုမှ အသံစာတမ်းများကို ဒေါင်းလုပ်လုပ်ပြီး Semantic Search with OpenAI Embeddings and Functions နမူနာနှင့် အသုံးပြုနိုင်ရန် ပြင်ဆင်ပေးသည်။

အသံနှင့် စာသားပြောင်းခြင်း ဒေတာ ပြင်ဆင်ရေး စကရစ်ပတ်များကို Windows 11 နောက်ဆုံးထွက် မိတ်ဆက်မှုများ၊ macOS Ventura နှင့် Ubuntu 22.04 (နှင့်အထက်) တွင် စမ်းသပ်ပြီးဖြစ်သည်။

## လိုအပ်သော Azure OpenAI ဝန်ဆောင်မှု အရင်းအမြစ်များ ဖန်တီးခြင်း

> [!IMPORTANT]
> OpenAI နှင့် တွဲဖက်အသုံးပြုမှု အတွက် သေချာစေရန် Azure CLI ကို နောက်ဆုံးဗားရှင်းသို့‌မြှင့်တင်ရန် အကြံပြုပါသည်။
> ကြည့်ရှုရန် [စာတမ်းများ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Resource group တစ်ခု ဖန်တီးပါ

> [!NOTE]
> ဤညွှန်ကြားချက်များတွင် East US တွင်ရှိသည့် "semantic-video-search" ဟုအမည်ရသော resource group ကို အသုံးပြုထားသည်။
> Resource group အမည်ကို ပြောင်းနိုင်သော်လည်း အရင်းအမြစ်များ၏ တည်နေရာကိုပြောင်းလဲသည့်အခါ 
> [မော်ဒယ် ရရှိနိုင်မှုဇယား](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ကိုစစ်ဆေးပါ။

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Service အရင်းအမြစ် တစ်ခု ဖန်တီးပါ။

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ဤလျှောက်လွှာတွင် အသုံးပြုရန် endpoint နှင့် key များ ရယူပါ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. အောက်ပါ မော်ဒယ်များကို တပ်ဆင်ပါ -
   - `text-embedding-ada-002` ဗားရှင်း `2` သို့မဟုတ် များ၍ `text-embedding-ada-002` ဟုအမည်ပေးထားသည်။
   - `gpt-5-mini` ဟုအမည်ပေးထားသည်။

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

## လိုအပ်သော ဆော့ဖ်ဝဲများ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) သို့မဟုတ် ပိုမိုမူလတန်း

## ပတ်ဝန်းကျင်အပြောင်းအလဲများ

YouTube အသံနှင့် စာသားပြောင်းခြင်း ဒေတာ ပြင်ဆင်ရေး စကရစ်ပတ်များ လုပ်ဆောင်ရန် အောက်ပါ ပတ်ဝန်းကျင်အပြောင်းအလဲများ လိုအပ်သည်။

### Windows ပေါ်တွင်

ပတ်ဝန်းကျင်အပြောင်းအလဲများကို သင်၏ `user` ပတ်ဝန်းကျင်အပြောင်းအလဲများထဲ ထည့်သွင်းရန် အကြံပြုပါသည်။
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` အား [USER] အတွက် > `New` သို့သွားပါ။

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ပတ်ဝန်းကျင်အပြောင်းအလဲများကို သင့် PowerShell profile ထဲသို့ ထည့်နိုင်သည်။

```powershell
$env:AZURE_OPENAI_API_KEY = "<သင့် Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<သင့် Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<သင့် Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<သင့် Google developer API key>"
``` -->

### Linux နှင့် macOS ပေါ်တွင်

အောက်ပါ export များကို သင့် `~/.bashrc` သို့မဟုတ် `~/.zshrc` ဖိုင်ထဲသို့ ထည့်သွင်းရန် အကြံပြုပါသည်။

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## လိုအပ်သော Python စာကြည့်တိုက်များ ထည့်သွင်းခြင်း

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ကို မတပ်ဆင်ရသေးလျှင် ထည့်သွင်းပါ။
1. `Terminal` ပြကြည့်သောပြတင်းပေါက်မှ သင်နှစ်သက်ရာ repo ဖိုင်ဒါသို့ နမူနာကို clone ယူပါ။

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` ဖိုလ်ဒါသို့ သွားရောက်ပါ။

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python virtual environment တစ်ခု ဖန်တီးပါ။

    Windows ပေါ်တွင် -

    ```powershell
    python -m venv .venv
    ```

    macOS နှင့် Linux ပေါ်တွင် -

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment ကို သွားရာ activation လုပ်ပါ။

   Windows ပေါ်တွင် -

   ```powershell
   .venv\Scripts\activate
   ```

   macOS နှင့် Linux ပေါ်တွင် -

   ```bash
   source .venv/bin/activate
   ```

1. လိုအပ်သော စာကြည့်တိုက်များ ထည့်သွင်းပါ။

   Windows ပေါ်တွင် -

   ```powershell
   pip install -r requirements.txt
   ```

   macOS နှင့် Linux ပေါ်တွင် -

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube အသံနှင့် စာသားပြောင်းခြင်း ဒေတာ ပြင်ဆင်ရေး စကရစ်ပတ်များ လုပ်ဆောင်ခြင်း

### Windows ပေါ်တွင်

```powershell
.\transcripts_prepare.ps1
```

### macOS နှင့် Linux ပေါ်တွင်

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->