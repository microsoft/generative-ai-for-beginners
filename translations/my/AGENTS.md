# AGENTS.md

## စီမံကိန်း အနှစ်ချုပ်

ဤrepository တွင် Generative AI အခြေခံ အကြောင်းအရာများနှင့် အက်ပ်ဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားပေးသည့် ဆယ့်ချဉ်းတစ်ဆယ့်တစ်ပုဒ်သာ ပါဝင်သော မဟာဗျူဟာ သင်တန်းအစီအစဉ် တစ်ခု ပါဝင်သည်။ သင်တန်းမှာ သစၥတနည်းပညာသို့ အသစ်စပြင်သူများအတွက် သင်ကြားဖို့အစီအစဉ်တင်ထားပြီး အခြေခံအယူအဆများ မှ ထွက်ပြီး ထုတ်လုပ်သူဆော့ဖ်ဝဲတည်ဆောက်ခြင်းအထိ လေ့လာနိုင်သည်။

**အဓိက နည်းပညာများ။**
- Python 3.9+ နှင့် ไลဘရေရီများ: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript နှင့် Node.js နှင့် ไลဘရေရ်များ: `openai` (Azure OpenAI v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, နှင့် Microsoft Foundry Models (GitHub Models ကို 2026 ခုနှစ် ဇူလိုင်လကုန်တွင် ဆင်းပယ်သွားမည်)
- ခုခံလေ့လာမှုအတွက် Jupyter Notebooks များ
- တည်ငြိမ်သော ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်အတွက် Dev Containers များ

**Repository ဖွဲ့စည်းပုံ။**
- ၂၁ ခုသော နံပါတ်စဉ်သင်ခန်းစာဖိုလ်ဒါများ (00-21) အတွင်းတွင် README များ၊ ကုဒ်နမူနာများ၊ အစီအစဉ်များ ပါရှိသည်
- Python, TypeScript, နဲ့တစ်ခါတစ်ရံ .NET နမူနာများ ပါဝင်သည်
- ဘာသာစကား ၄၀ ကျော် ဘာသာပြန် ဖိုလ်ဒါ
- ရည်ညွှန်းချက် `.env` ဖိုင်မှ စုပေါင်း ထိန်းချုပ်မှုပေးထားသည် (`.env.copy` ကို template အဖြစ် အသုံးပြု)

## စတင် အသုံးပြုရန် အမိန့်များ

### Repository စတင် ချိန်ဆ

```bash
# အရင်းအမြစ်ကို မိတ္တူလုပ်ပါ
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# ပတ်ဝန်းကျင် ပုံစံကို ကူးယူပါ
cp .env.copy .env
# သင့် API key နှင့် endpoint များဖြင့် .env ကို ပြင်ဆင်ပါ
```

### Python ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း

```bash
# ဗားချွင်းပတ်ဝန်းကျင် ဖန်တီးပါ
python3 -m venv venv

# ဗားချွင်းပတ်ဝန်းကျင်ကို ဖွင့်ပါ
# macOS/Linux မှာ:
source venv/bin/activate
# Windows မှာ:
venv\Scripts\activate

# လိုအပ်သည့်သူတို့ကို တပ်ဆင်ပါ
pip install -r requirements.txt
```

### Node.js/TypeScript ပြင်ဆင်ခြင်း

```bash
# မူရင်းအဆင့်တွင် လိုအပ်သော လျှောက်လွှာများ 설치 (စာတမ်းရေးကိရိယာများအတွက်)
npm install

# တစ်ဦးချင်း သင်ခန်းစာ TypeScript ဥပမာများအတွက် သတ်မှတ်ထားသော သင်ခန်းစာသို့ ခရီးသွားပါ။
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container ပြင်ဆင်ခြင်း (အကြံပြု)

Repository တွင် GitHub Codespaces သို့မဟုတ် VS Code Dev Containers များအတွက် `.devcontainer` ဖိုင်ပါဝင်သည်။

၁။ GitHub Codespaces သို့မဟုတ် VS Code Dev Containers extension ဖြင့် repository သို့ ဝင်ပါ
၂။ Dev Container မှအလိုအလျောက်လုပ်ဆောင်သည်-
   - `requirements.txt` မှ Python အားလိုအပ်ချက်များ ထည့်သွင်းမည်
   - post-create စကရစ်ပတ်ကို (`.devcontainer/post-create.sh`) မောင်းမည်
   - Jupyter kernel ကို စတစ်အပ်တင်မည်

## ဖွံ့ဖြိုးတိုးတက်မှု လမ်းညွှန်ချက်များ

### ပတ်ဝန်းကျင် ဆက်တင်များ

API ဝင်ရောက်ခွင့်လိုသော သင်ခန်းစာအားလုံးတွင် `.env` တွင် သတ်မှတ်ထားသော ပတ်ဝန်းကျင်ဆက်တင်များကို အသုံးပြုသည်။

- `OPENAI_API_KEY` - OpenAI API အတွက်
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry (Azure OpenAI Service သည် ယခု Microsoft Foundry ၏ အစိတ်အပိုင်း ဖြစ်သည်: https://ai.azure.com) အတွက် Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion မော်ဒယ်တပ်ဆင်မှု အမည် (သင်တန်း ပုံမှန်: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings မော်ဒယ်တပ်ဆင်မှု အမည် (သင်တန်း ပုံမှန်: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API ဗားရှင်း (ပုံမှန်: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face မော်ဒယ်များအတွက်
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider model catalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API key (အစားထိုး ပျက်သိမ်းမည့် `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - reasoning မဟုတ်သော မော်ဒယ် (ဥပမာ - `Llama-3.3-70B-Instruct`) ကို `temperature` နမူနာများတွင် သုံးသည်။ reasoning မော်ဒယ်များတွင် sampling controls မထောက်ပံ့ပါ။

### မော်ဒယ် စံနမူနာများ (အရေးကြီး)

- **ပုံမှန် chat မော်ဒယ်သည် `gpt-5-mini`** - ယနေ့ အသုံးပြုနေသော non-deprecated **reasoning** မော်ဒယ်ဖြစ်သည်။ ၂၀၂၆ ခုနှစ်၌ ဟောင်းကင်းလာနေသော temperature ထောက်ပံ့မှုရှိ "mini" မော်ဒယ်များ (`gpt-4o-mini`, `gpt-4.1-mini`) ကို ပျက်ကွက်မှုရှိလာသည်၊ သင်တန်းတွင် GPT-5 မိသားစုကို စံထားသည်။
- **reasoning မော်ဒယ်များတွင် `temperature` နှင့် `top_p` ကို လက်မခံကြပါ**။ Responses API တွင် `max_output_tokens` / chat completions တွင် `max_completion_tokens` သုံးပြီး `max_tokens` မသုံးပါ။ `gpt-5-mini` ကိုခေါ်သော နမူနာများတွင် `temperature`, `top_p`, `max_tokens` မထည့်ပါနှင့်။
- **`temperature` ကို ပြသရန်** samples တွင် Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`) မှ **Llama** မော်ဒယ် (`Llama-3.3-70B-Instruct`) ကို သုံးသည်။ reasoning မော်ဒယ်များကို prompt engineering နှင့် reasoning control များဖြင့် စီမံပါ။
- **Fine-tuning (သင်ခန်းစာ ၁၈)** တွင် `gpt-4.1-mini` ကို ထိန်းသိမ်းထားသည်- GPT-5 သည် reinforcement fine-tuning (RFT) ကိုသာ အထောက်အပံ့ ပြုသည့်ကြောင့် supervised fine-tuning (SFT) မထောက်ပံ့ပါ။
- သင်ခန်းစာ ၂၀ (Mistral) နှင့် ၂၁ (Meta) တွင် `temperature`/`max_tokens` ကို ထိန်းသိမ်းပါသည်၊ ထိုများမှာ Mistral/Llama မော်ဒယ်များကို လမ်းညွှန်ပြုလုပ်သည်။

### Python နမူနာများ ပြေးဆွဲခြင်း

```bash
# သင်ခန်းစာ ဒိုင်ရက်ထရီသို့သွားပါ
cd 06-text-generation-apps/python

# Python စခရစ်ပြေးပါ
python aoai-app.py
```

### TypeScript နမူနာများ ပြေးဆွဲခြင်း

```bash
# TypeScript အက်ပ်ဖိုလ်ဒါသို့သွားပါ
cd 06-text-generation-apps/typescript/recipe-app

# TypeScript ကုဒ်ကို တည်ဆောက်ပါ
npm run build

# အက်ပ်လီကေးရှင်းကို ပြေးပါ
npm start
```

### Jupyter Notebooks များ အသုံးပြုခြင်း

```bash
# သိုလှောင်ရာအမြစ်တွင် Jupyter ကို စတင်ပါ
jupyter notebook

# ဒါမှမဟုတ် Jupyter extension ပါသော VS Code ကို အသုံးပြုပါ
```

### သင်ခန်းစာ မတူညီသော အမျိုးအစားများနှင့်အတူ အလုပ်လုပ်ခြင်း

- **"လေ့လာ" သင်ခန်းစာများ**: README.md အကြောင်းအရာနှင့် အယူအဆ များအပေါ် ဦးတည်သည်
- **"ဆောက်လုပ်" သင်ခန်းစာများ**: Python နှင့် TypeScript သုံးကွဲ ကုဒ်နမူနာများ ပါဝင်သည်
- သင်ခန်းစာတိုင်းတွင် နည်းဗျူဟာ၊ ကုဒ်ပြ walkthrough များ၊ ဗီဒီယို အကြောင်းအရာ လင့်ခ်များပါရှိသည်

## ကုဒ် စံ ပြင်ဆင်ချက်များ

### Python

- ပတ်ဝန်းကျင် ဆက်တင် ကျင့်သုံးမှုအတွက် `python-dotenv` အသုံးပြုခြင်း
- API နှင့် ဆက်သွယ်ရန် `openai` 라이브러리를 သုံးခြင်း
- linting အတွက် `pylint` ကိုသုံးသည် (အချို့ နမူနာများတွင် `# pylint: disable=all` ပါရှိသည်)
- PEP 8 နာမည်ပုံစံများ ကိုလိုက်နာပါ
- API ကီးများကို `.env` ဖိုင်တွင် သိမ်းဆည်းပါ၊ ကုဒ်ထဲတွင် မထားပါနှင့်

### TypeScript

- ပတ်ဝန်းကျင် ဆက်တင်အတွက် `dotenv` package ကိုအသုံးပြုခြင်း
- 每个应用程序的 `tsconfig.json` 中配置 TypeScript
- Azure OpenAI အတွက် `openai` package အသုံးပြုပါ (client ကို `/openai/v1/` endpoint သို့ ယူ၍ `client.responses.create` ခေါ်ပါ)၊ Microsoft Foundry Models အတွက် `@azure-rest/ai-inference` သုံးပါ
- auto-reload ပေါ်မူတည် dev အတွက် `nodemon` ကိုသုံးပါ
- run မလုပ်မီ `npm run build` ပြီးနောက် `npm start`

### အထွေထွေ စံနမူနာများ

- ကုဒ်နမူနာများကို ရိုးရှင်းပြီး အတတ်ပညာသင်ကြားမှု အတွက် သီးသန့် ထားပါ
- အကြောင်းအရာ လေ့လာရှင်းလင်းမှု အတွက် မှတ်ချက်များ ထည့်သွင်းပါ
- သင်ခန်းစာတိုင်း၏ ကုဒ် သည့်ဆောက်လုပ်နိုင်ပြီး မျှဝေဖို့ ပြင်ဆင်ထားသည်
- နာမည်တူကွဲပြားမှု ထိန်းသိမ်းပါ: Azure OpenAI အတွက် `aoai-`, OpenAI API အတွက် `oai-`, Microsoft Foundry Models အတွက် `githubmodels-` (GitHub Models အခါမှ သာယာ)။

## အညွှန်း စံနမူနာများ

### Markdown ပုံစံ

- URL များအားလုံးကို `[text](../../url)` ပုံစံဖြင့် လေ့လာရေး သဟဇာတစွာ ဖြည့်ပါ
- ဆက်စပ်လင့်ခ်များသည် `./` သို့မဟုတ် `../` ဖြင့် စတင်ရမည်
- Microsoft domain များသို့ လင့်ခ်တိုင်းတွင် ခရီးလမ်းသတင်း အမှတ်မှတ်ပုံတင်ထားရမည်: `?WT.mc_id=academic-105485-koreyst`
- URL များတွင် နိုင်ငံအလိုက် locale မပါဝင် ရစေ (`/en-us/` ကို သတိပြုမိပါ)
- ပုံများကို `./images` ဖိုလ်ဒါ အတွင်း သင့်တော်သည့် အမည်များဖြင့် သိမ်းဆည်းပါ
- ဖိုင်အမည်တွင် အင်္ဂလိပ်စာလုံး၊ နံပါတ်များ နှင့် ဒက်ရှ် (-) များကို အသုံးပြုပါ

### ဘာသာပြန်ကူညီမှု

- Repository သည် automated GitHub Actions မှတစ်ဆင့် 40+ ဘာသာစကား ထောက်ပံ့သည်
- ဘာသာပြန်ထားသော မြေပုံများကို `translations/` ဖိုလ်ဒါတွင် သိမ်းဆည်းသည်
- အပိုင်းအစ ဘာသာပြန်ချက် မတင်ပြရပါ
- စက်ဘာသာပြန် မလက်ခံပါ
- ဘာသာပြန်ထားသော ပုံများကို `translated_images/` ဖိုလ်ဒါတွင် သိမ်းဆည်းသည်

## စမ်းသပ်မှုနှင့် အတည်ပြုခြင်း

### စတင်တင်သွင်းခြင်း မတိုင်မှီ စစ်ဆေးမှုများ

Repository သည် GitHub Actions ကို validation အတွက်အသုံးပြုသည်။ PR များ တင်ရန်မတိုင်မှီ

၁။ **Markdown လင့်ခ်များ စစ်ဆေးပါ**
   ```bash
   # validate-markdown.yml အလုပ်စဉ်သည် စစ်ဆေးသည်။
   # - ပျက်သွားသော နီးစပ်ရာလမ်းကြောင်းများ
   # - လမ်းကြောင်းများပေါ်တွင် လိုက်လံသည့် ID မရှိခြင်း
   # - URL များပေါ်တွင် လိုက်လံသည့် ID မရှိခြင်း
   # - နိုင်ငံတစ်နိုင်ငံ ရွက်စက္ကူပါရှိသည့် URL များ
   # - ပျက်စီးသော အပြင်ပေါ် URL များ
   ```

၂။ **လက်ခံစစ်ဆေးမှု**
   - Python နမူနာများ စမ်းသပ်ရန်: venv ကိုဖွင့်ပြီး စကရစ်ပတ်များ မောင်းပါ
   - TypeScript နမူနာများ စမ်းသပ်ရန်: `npm install`, `npm run build`, `npm start` အား အသုံးပြုပါ
   - ပတ်ဝန်းကျင်ဆက်တင် များမှန်ကန်မှု စစ်ဆေးပါ
   - API ကီးများက ကုဒ် နမူနာများနှင့်လုပ်ဆောင်နိုင်မှု ကြည့်ရှုပါ

၃။ **ကုဒ် နမူနာများ**
   - စားလုံး ကုဒ်များ error မရှိဘဲ ပြေးနိုင်မှုရှိသင့်သည်
   - Azure OpenAI နှင့် OpenAI API နှစ်ခုလုံးဖြင့် စမ်းသပ်ပါ
   - Microsoft Foundry Models တွင် ထောက်ပံ့သော နေရာများတွင် နမူနာများ စစ်ဆေးပါ

### အလိုအလျောက် စမ်းသပ်မှု မရှိ

ဤ repository သည် သင်ခန်းစာနှင့် နမူနာများအပေါ် ဦးစားပေးထားသဖြင့် unit test သို့မဟုတ် integration test မပါရှိပါ။ validation အဓိကအားဖြင့်:
- ကုဒ် နမူနာများ လက်စွဲ စမ်းသပ်မှု
- GitHub Actions မှ Markdown စစ်ဆေးမှု
- ပညာရေး အကြောင်းအရာအပေါ် အသိုင်းအဝိုင်း သုံးသပ်ချက်များ

## Pull Request လမ်းညွှန်ချက်များ

### တင်သွင်းခင်

၁။ Python နှင့် TypeScript နှစ်ကိုယ်တော် ပြောင်းလဲမှုများ စမ်းသပ်ပါ
၂။ Markdown စစ်ဆေးမှုကို (PR အပေါ် အလိုအလျောက် စတင်) ပြုလုပ်ပါ
၃။ Microsoft URL များ၌ tracking ID များ ရှိမှန်း သေချာစေပါ
၄။ ဆက်စပ်လင့်ခ်များ မှန်ကန်မှု စစ်ဆေးပါ
၅။ ပုံ အသုံးပြုခြင်း မှန်ကန်သည်ကို အတည်ပြုပါ

### PR ခေါင်းစဉ်ပုံစံ

- ရည်ညွှန်းချက်ပြည့်စုံသော ခေါင်းစဉ်များ သုံးပါ: `[Lesson 06] Fix Python example typo` သို့မဟုတ် `Update README for lesson 08`
- လိုအပ်ပါက issue နံပါတ်တွေသာ တွဲဖက်ပါ: `Fixes #123`

### PR ဖော်ပြချက်

- မည်သည်ကို ပြင်ဆင်ခဲ့သည်နှင့် အကြောင်းရင်းကို ဖေါ်ပြပါ
- ဆက်စပ် issue များ link ပါ
- ကုဒ် ပြောင်းလဲမှုများအတွက် စမ်းသပ်ခဲ့သော နမူနာများ ဖော်ပြပါ
- ဘာသာပြန် PR များအတွက် ပြည့်စုံသော ဘာသာပြန် ဖိုင်များပါဝင်သည်

### နည်းလမ်း ဝင်ရောက်ပုံ အချက်အလက်များ

- Microsoft CLA ကို နှိပ်ဆွဲ (ပထမဆုံး PR တွင် အလိုအလျောက်)
- ပြောင်းလဲမှုလုပ်မည့်အခါ repository ကို သင့်အကောင့်သို့ကွဲထွက်ပါ
- တစ် PR တည်းကို တစ် နည်းလမ်းပြောင်းလဲမှုအတွက်သာ သုံးပါ ( မဆိုင်ဘဲ ပြင်ဆင်မှုများ မပေါင်းစပ်ရ)
- PR များကို အလွန်ကြီးမားခွဲခြမ်းမပြုနိုင်ပါက သေးငယ်သည့် အရာများအထိ အာရုံစိုက်ပါ

## လူကြိုက်များ သုံး Workflow များ

### နယ်ပယ်အသစ်အတွက် ကုဒ် နမူနာ အသစ် ထည့်ခြင်း

၁။ သင်ခန်းစာသင့်တော်ရာ ဖိုလ်ဒါသို့ သွားပါ
၂။ `python/` သို့မဟုတ် `typescript/` ဆိုတဲ့ အဖွဲ့အစည်းတွင် နမူနာတည်ဆောက်ပါ
၃။ နာမည်ပုံစံကိုလိုက်နာပါ: `{provider}-{example-name}.{py|ts|js}`
၄။ အမှန် API ကီးများနှင့် စမ်းသပ်ပါ
၅။ သင်ခန်းစာ README တွင် အသစ်ထည့်သော ပတ်ဝန်းကျင်ဆက်တင်များကို မှတ်တမ်းတင်ပါ

### အညွှန်း စာတမ်း ပြုပြင်ခြင်း

၁။ သင်ခန်းစာ ဖိုလ်ဒါ၏ README.md ကို ပြင်ဆင်ပါ
၂။ Markdown စံများ (tracking ID များ၊ ဆက်စပ် လင့်ခ်များ) ကိုလိုက်နာပါ
၃။ ဘာသာပြန်ချက်များကို GitHub Actions မှ စီမံပေးသည် (လက်ဖြင့် မပြင်ဆင်ရ)
၄။ လင့်ခ်အားလုံး မှန်ကန်မှု စစ်ဆေးပါ

### Dev Containers နှင့်အတူ အလုပ်လုပ်ခြင်း

၁။ Repository တွင် `.devcontainer/devcontainer.json` ပါရှိသည်
၂။ post-create script က Python အားလိုအပ်ချက်များကို အလိုအလျောက် ထည့်သွင်းမည်
၃။ Python နှင့် Jupyter Extensions များ ကြိုတင်တပ်ဆင်ထားသည်
၄။ ပတ်ဝန်းကျင်သည် `mcr.microsoft.com/devcontainers/universal:2.11.2` အပေါ် မူတည်သည်

## ထုတ်ပိုးနှင့် ထုတ်ဝေရေး

ဤသည် သင်ယူမှု repository ဖြစ်ပြီး ထုတ်လွှင့်ရေး လုပ်ငန်းစဉ် မရှိပါ။ သင်တန်း အကြောင်းအရာများကို အသုံးပြုသည့် နည်းလမ်းများမှာ

၁။ **GitHub Repository**: ကုဒ်နှင့် စာရွက်စာတမ်း များကို တိုက်ရိုက် ဝင်ကြည့်နိုင်ခြင်း
၂။ **GitHub Codespaces**: ကြိုတင် ပြင်ဆင်ထားသော ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်ကို ချက်ချင်းအသုံးပြုနိုင်ခြင်း
၃။ **Microsoft Learn**: တရားဝင် သင်ကြားမှု စင်တာတွင် အကြောင်းအရာ တင်သွင်းနိုင်ခြင်း
၄။ **docsify**: Markdown ကနေ ဖွဲ့စည်းထားသော စာရွက်စာတမ်း ဝက်ဘ်ဆိုက် (ကြည့်ပါ `docsifytopdf.js` နှင့် `package.json`)

### စာရွက်စာတမ်း စက်တင်လုပ်ခြင်း

```bash
# ကိုယ်ရေးရာဇဝင်မှ PDF ဖိုင်ကို (လိုအပ်လျှင်) ဖန်တီးပါ။
npm run convert
```

## ပြဿနာ ဖြေရှင်းခြင်း

### လူသုံး များထွက် ပြဿနာများ

**Python Import အမှားများ:**
- virtual environment ကို ဖြင့်ထားကြောင်း သေချာစေပါ
- `pip install -r requirements.txt` ကို အကောင်အထည်ဖော်ပါ
- Python ဗားရှင်း သည် 3.9+ ဖြစ်မှန်း စစ်ဆေးပါ

**TypeScript တည်ဆောက်မှု အမှားများ:**
- အထူးသတ်မှတ်ထားသော app ဖိုလ်ဒါတွင် `npm install` ကို ပြုလုပ်ပါ
- Node.js ဗားရှင်း ကို သင့်တော်မှု ရှိမှန်း စစ်ဆေးပါ
- `node_modules` ကို ဖယ်ရှားပြီး ပြန်လည် ထည့်သွင်းပါ (လိုအပ်ပါက)

**API Authentication အမှားများ:**
- `.env` ဖိုင် ရှိပြီး တိကျသော တန်ဖိုးများ ပါဝင်ကြောင်း သေချာစေပါ
- API key များ သက်တမ်းကုန်ဆုံးမဟုတ်ကြောင်း သေချာစေပါ
- နေရာဒေသ အတွက် endpoint URL များ မှန်ကန်ကြောင်း စစ်ဆေးပါ

**ပတ်ဝန်းကျင် ဆက်တင် မပါသောအခြေအနေ:**
- `.env.copy` ကို `.env` သို့ ကူးယူပါ
- သင်လေ့လာနေသည့် သင်ခန်းစာ လိုအပ်ချက်ရှိသည့် တန်ဖိုးများအားလုံး ဖြည့်စွက်ပါ
- `.env` ပြင်ဆင်ပြီးနောက် သင့် အက်ပ်ကို ပြန်စတင်ပါ

## ထပ်ဆင့် အရင်းအမြစ်များ

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## စီမံကိန်း သီးသန့် မှတ်ချက်များ

- ဤသည်မှာ **ပညာရေး repository** ဖြစ်ပြီး ထုတ်လုပ်မှုကုဒ်မဟုတ်ပါ
- နမူနာများသည် ရိုးရှင်းပြီး အယူအဆ သင်ကြားရန် ရည်ရွယ်သည်
- ကုဒ် အရည်အသွေးသည် ပညာရေး ရှင်းလင်းမှုနှင့် ညီမျှစွာ ထိန်းသိမ်းထားသည်
- သင်ခန်းစာတိုင်းသည် ပူးပေါင်းထားပြီး ကိုယ်ပိုင်အောင်မြင်မှု ရရှိနိုင်သည်
- Repository တွင် အုပ်စုအားလုံး Azure OpenAI, OpenAI, Microsoft Foundry Models နှင့် offline provider များဖြစ်သော Foundry Local နှင့် Ollama များကို ထောက်ပံ့သည်
- အကြောင်းအရာသည် ဘာသာစကားစုံ အသုံးပြုထားပြီး automated ဘာသာပြန် လုပ်ငန်းစဉ်များ ပါရှိသည်
- Discord တွင် မေးခွန်းမေးရန်နှင့် ကူညီပေးရန် အဖွဲ့ဝင်များ တက်ကြွစွာ ပါဝင်သည်

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->