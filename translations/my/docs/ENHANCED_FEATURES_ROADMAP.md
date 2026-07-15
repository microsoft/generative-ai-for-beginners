# တိုးတက်ပြောင်းလဲချက်များနှင့် အဆင့်မြှင့်တင်ခြင်းလမ်းပြမြေပုံ

ဤစာတမ်းသည် Generative AI for Beginners သင်ရိုးညွှန်းတမ်းအတွက် ကုဒ်သုံးသပ်ချက်ပြည့်စုံနှင့် စက်မှုလက်မှုဆိုင်ရာအကောင်းဆုံးအတွေ့အကြုံများအပေါ်မှ အထောက်အကူပြု ဆန်းသစ်တိုးတက်မှုများနှင့် အဆင့်မြှင့်တင်မှုများကို ဖော်ပြထားသည်။

## အကြောင်းအကျဉ်း

ကုဒ်အခြေခံများကို လုံခြုံရေး၊ ကုဒ်အရည်အသွေးနှင့် ပညာရေး ထိရောက်မှုအတွက် စိစစ်ထားပြီး၊ ဤစာတမ်းတွင် ချက်ချင်းပြင်ဆင်ရန်အကြံပြုချက်များ၊ နီးစပ်သည့်အချိန်အတွင်း တိုးတက်မြှင့်တင်ရန်နှင့် အနာဂတ်တိုးတက်စေမည့်အကြံပြုချက်များအား ပေးထားသည်။

---

## ၁။ လုံခြုံရေးပြုပြင်မွမ်းမံမှုများ (အလေးပေးမှု: အရေးကြီး)

### ၁.၁ ချက်ချင်းပြင်ဆင်ခဲ့သည် (ပြီးစီး)

| ပြဿနာ | ဖိုင်များ | အခြေအနေ |
|-------|----------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | ပြင်ဆင်ပြီး |
| env validation မပါရှိခြင်း | မတူညီသော JS/TS ဖိုင်များ | ပြင်ဆင်ပြီး |
| မလုံခြုံသော function ခေါ်ဆိုမှုများ | `11-integrating-with-function-calling/js-githubmodels/app.js` | ပြင်ဆင်ပြီး |
| ဖိုင် handle တွေချွတ်ကျန်မှု | `08-building-search-applications/scripts/` | ပြင်ဆင်ပြီး |
| request timeouts မပါရှိခြင်း | `09-building-image-applications/python/` | ပြင်ဆင်ပြီး |

### ၁.၂ အကြံပြုလုံခြုံရေးအကျိုးအမြတ်များ

၁။ **Rate Limiting ဥပမာများ**
   - API ခေါ်ဆိုမှုများအတွက် rate limiting ကိုပြုလုပ်နည်း ဥပမာကုဒ်များထည့်ရန်
   - exponential backoff ပုံစံများကိုဖော်ပြရန်

၂။ **API Key ပြောင်းလဲခြင်း**
   - API key ပြောင်းလဲမှုအတွက် အကောင်းဆုံးနည်းလမ်းများကိုစာရွက်စာတမ်းထဲမှာထည့်သွင်းရန်
   - Azure Key Vault သို့မဟုတ် ဆင်တူဝန်ဆောင်မှုများသုံးပြီး ဥပမာများထည့်ရန်

၃။ **Content Safety ပေါင်းစပ်ခြင်း**
   - Azure Content Safety API သုံးလျက် ဥပမာများထည့်ရန်
   - input/output moderation ပုံစံများပြသရန်

---

## ၂။ ကုဒ်အရည်အသွေး မြှင့်တင်ခြင်း

### ၂.၁ ပုံသေအဖြစ် ဖိုင်များထည့်သွင်းခြင်း

| ဖိုင် | ရည်ရွယ်ချက် |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript linting စည်းကမ်းများ |
| `.prettierrc` | ကုဒ်ပုံစံညှိနှိုင်းမှု စံချိန်များ |
| `pyproject.toml` | Python tooling သတ်မှတ်ချက်များ (Black, Ruff, mypy) |

### ၂.၂ ပူးပေါင်းအသုံးပြုနိုင်သော utilities ဖန်တီးခြင်း

အသစ်ထည့်သွင်းသော `shared/python/` module တစ်ခုတွင်:
- `env_utils.py` - Environment variable ကိုလုပ်ထုံးလုပ်နည်း
- `input_validation.py` - ထည့်သွင်းမှု စစ်ဆေးမှုနှင့် သန့်ရှင်းမှု
- `api_utils.py` - လုံခြုံသော API request wrapping များ

### ၂.၃ အကြံပြုကုဒ်မြှင့်တင်မှုများ

၁။ **Type Hints ကို အပြည့်အဝ ဖော်ပြခြင်း**
   - Python ဖိုင်အားလုံးတွင် type hints ထည့်သွင်းရန်
   - TypeScript ပရောဂျက်များအားလုံးတွင် strict mode ကိုဖွင့်ထားရန်

၂။ **စာရွက်စာတမ်းစံထားများ**
   - Python function အားလုံးတွင် docstrings ထည့်သွင်းရန်
   - JavaScript/TypeScript function များတွင် JSDoc မှတ်ချက်များထည့်ရန်

၃။ **စမ်းသပ်ခြင်းကွန်ယက်**
   - pytest စီမံကိန်းနှင့် အကြောင်းပြကျွမ်းကျင်မှုများထည့်သွင်းရန် _(ပြီးစီးပြီ: `pyproject.toml` တွင် pytest စီမံချက်ပါရှိပြီး၊ shared utilities များအတွက် ဥပမာစမ်းသပ်မှုများကို [`tests/`](../../../tests) အတွင်း CI မှာ ပြေးနေ)_
   - JavaScript/TypeScript အတွက် Jest စီမံချက်ထည့်ရန်

---

## ၃။ ပညာရေးနှင့်သင်ကြားမှုတိုးတက်မှုများ

### ၃.၁ သင်ခန်းစာအသစ် အကြောင်းအရာများ

၁။ **AI application များတွင် လုံခြုံရေး** (အကြံပြုသင်ခန်းစာ ၂၂)
   - Prompt injection နှင့် ကာကွယ်နည်းများ
   - API key စီမံခန့်ခွဲမှု
   - အကြောင်းအရာ ကြပ်မတ်မှု
   - Rate limiting နှင့် မသုံးစွဲခွင့်ပိတ်ဆို့မှု

၂။ **ထုတ်လုပ်မှု စနစ်ထည့်သွင်းခြင်း** (အကြံပြုသင်ခန်းစာ ၂၃)
   - Docker ဖြင့် containerization
   - CI/CD pipeline များ
   - စောင့်ကြည့်ခြင်းနှင့် မှတ်တမ်းတင်ခြင်း
   - ကိုင်တွယ်မှုကျသင့်သော စရိတ်

၃။ **အဆင့်မြင့် RAG နည်းပညာများ** (အကြံပြုသင်ခန်းစာ ၂၄)
   - Hybrid ရှာဖွေရေး (keywords + semantic)
   - ပြန်လည်သုံးသပ်မှုနည်းလမ်းများ
   - Multi-modal RAG
   - အကဲဖြတ်မည့်အတိုင်းအတာများ

### ၃.၂ ရှိပြီးသား သင်ခန်းစာပြင်ဆင်မှုများ

| သင်ခန်းစာ | အကြံပြုမှုပြင်ဆင်ချက် |
|--------|------------------------|
| 06 - စာသားဖန်တီးမှု | Streaming response ဥပမာများ ထည့်ရန် |
| 07 - စကားပြော အက်ပ်များ | အပြောအဆိုမှတ်ဉာဏ်ပုံစံများ ထည့်ရန် |
| 08 - ရှာဖွေရေး အက်ပ်များ | Vector database နှိုင်းယှဉ် တင်ပြရန် |
| 09 - ပုံဖန်တီးမှု | ပုံတည်းဖြတ်ခြင်း/အမျိုးမျိုးပြောင်းလဲမှု ဥပမာများ ထည့်ရန် |
| 11 - Function Calling | တန်းလျှောက် function ခေါ်ချက် များ ထည့်ရန် |
| 15 - RAG | Chunking လုပ်နည်း နှိုင်းယှဉ်မှု ထည့်ရန် |
| 17 - AI agents | Multi-agent စီမံခန့်ခွဲမှု ထည့်ရန် |

---

## ၄။ API ခေတ်မီမှု

### ၄.၁ သုံးစွဲမှု မရသော API ပုံစံများ (ပြောင်းရွှေ့မှု ပြီးစီး)

Python နှင့် TypeScript **chat** စမ်းသပ်မှုများအားလုံးသည် Chat Completions API မှ **Responses API** (`client.responses.create(...)` → `response.output_text`) သို့ ပြောင်းရွှေ့ပြီး ဖြစ်သည်။

| အဟောင်းပုံစံ | အသစ်ပုံစံ | အခြေအနေ |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | ပြီးစီး |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | ပြီးစီး |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` package `client.responses.create()` → `response.output_text` | ပြီးစီး |
| `df.append()` (pandas) | `pd.concat()` | ပြီးစီး |

> **မှတ်ချက်:** Microsoft Foundry Models စမ်းသပ်မှုများသည် `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) ကိုအသုံးပြု၍ Model Inference API ပေါ်မှာ ဆက်လက်ရှိပါတယ်။ Responses API ပံ့ပိုးမှုမပါဘဲ ဖြစ်ပြီး၊ `AzureOpenAI()` ကို embedding နှင့်ပုံဖန်တီးမှု များအတွက် ဆက်လက်သုံးစွဲနိုင်သည်။

### ၄.၂ အသစ်ထည့်သွင်းရန် API လုပ်ဆောင်ချက်များ ပြသခြင်း

၁။ **ဖွဲ့စည်းထားသော ထွက်ပေါက်များ** (OpenAI)
   - JSON မုဒ်
   - ကွပ်မျဉ်းတိကျသော schema များနဲ့ function ခေါ်ဆိုမှု

၂။ **မြင်ကွင်း ဆိုင်ရာ စွမ်းဆောင်ရည်များ**
   - GPT-4o (vision) ဖြင့် ပုံစံဆန်းစစ်ချက်
   - Multi-modal prompt များ

၃။ **Responses API ထုတ်လုပ်မှုကိရိယာများ** (Assistants API အစား)
   - Code interpreter
   - ဖိုင်ရှာဖွေမှု
   - ဝက်ဘ်ရှာဖွေမှုနှင့် စိတ်ကြိုက်ကိရိယာများ

---

## ၅။ အင်ဖရန်စထရပ်ချာပြုပြင်မွမ်းမံမှုများ

### ၅.၁ CI/CD တိုးတက်မှုများ

[`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) တွင် ကုဒ်အရည်အသွေး စစ်ဆေးမှုများသွင်းထားသည်။ Python linting/formatting (Ruff + Black) ကို `shared/` utilities module တွင် **တင်းကြပ်စွာ** သုံးစွဲသည်။ ကျန်သေးသော သင်ရိုးအစိတ်အပိုင်းများတွင် advisory အဖြစ် အပြေးရှိပြီး JavaScript/TypeScript အတွက် ESLint pass advisory သိပ္ပံပြုသည်။ အခြေခံအစီအစဉ်မှာ-

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### ၅.၂ လုံခြုံရေး စစ်ဆေးမှု

[`.github/workflows/security.yml`](../../../.github/workflows/security.yml) တွင် CodeQL သုံးပြီး Python နှင့် JavaScript/TypeScript အတွက် စစ်ဆေးမှုများ ထည့်သွင်းထားသည် (push, pull request နှင့် အပတ်စဉ်အချိန်ဇယားများတွင်သွား)၊ pull request များမှာ dependency နှင့်စစ်ဆေးမှု ပါဝင်သည်။ အခြေခံအစီအစဉ်မှာ-

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## ၆။ ဖွံ့ဖြိုးသူ အတွေ့အကြုံ တိုးတက်စေမှုများ

### ၆.၁ DevContainer တိုးတက်မှု

[`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) နှင့် [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) တွင် ထည့်သွင်းထားသည်။ Container သည် Pylance, Black formatter, Ruff, ESLint, Prettier, Copilot extensions များပါ ပါက်ခြင်းနှင့် format-on-save ကို repo ၏ Black/Prettier ဖိုင်သတ်မှတ်ချက်နှင့်ချိတ်ဆက်ထားပြီး developer tooling (`ruff`, `black`, `mypy`, `pytest`) များကို တပ်ဆင်သည်။ ထို့ကြောင့် [code-quality workflow](../../../.github/workflows/code-quality.yml) ကို ဒေသစ်တွင် ပြန်လည်ရရှိနိုင်သည်။ `mcr.microsoft.com/devcontainers/universal` base image သည် Python နှင့် Node ကို bundle ထားပြီးသောကြောင့် နောက်ထပ် features မလိုအပ်ပါ။ အခြေခံအစီအစဉ်မှာ-

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### ၆.၂ အပြန်အလှန်ပြသမှုကွင်း

ထည့်သွင်းရန်စဉ်းစားကြည့်ပါ-
- ပတ်ဝန်းကျင်မှ API key ကြိုတင်ဖြည့်ထားသည့် Jupyter notebooks များ
- visual သင်ယူသူများအတွက် Gradio/Streamlit ဆင်ခြင်မှုငယ်ငယ်များ
- အချက်အလက် စမ်းသပ်မှုများအတွက် အပြန်အလှန် စစ်ဆေးမှုများ

---

## ၇။ ဘာသာစကားစုံထောက်ခံမှု

### ၇.၁ လက်ရှိ ဘာသာစကား များမီ

| နည်းပညာ | သင်ခန်းစာများ မျှဝေ | အခြေအနေ |
|------------|-----------------|--------|
| Python | အားလုံး | ပြီးစီး |
| TypeScript | 06-09, 11 | တစ်စိတ်တစ်ပိုင်း |
| JavaScript | 06-08, 11 | တစ်စိတ်တစ်ပိုင်း |
| .NET/C# | အချို့ | တစ်စိတ်တစ်ပိုင်း |

### ၇.၂ အကြံပြု တိုးချဲ့မှုများ

၁။ **Go** - AI/ML tooling အတွက် တိုးတက်မှုရှိနေ
၂။ **Rust** - ဆောင်ရွက်မှုအရေးကြီးသော application များ
၃။ **Java/Kotlin** - လုပ်ငန်းခြေ application များ

---

## ၈။ ဒေတာ လည်ပတ်မှု မြှင့်တင်ခြင်း

### ၈.၁ ကုဒ် အဆင့် မြှင့်တင်မှုများ

၁။ **Async/Await ပုံစံများ**
   - batch processing အတွက် async ဥပမာများ ထည့်ရန်
   - concurrent API ခေါ်ဆိုမှုများ ပြသရန်

၂။ **Caching နည်းလမ်းများ**
   - embedding cache ထည့်သွင်းရန်ဥပမာများ
   - response cache ပုံစံများ ဖော်ပြရန်

၃။ **Token အထိရောက်ဆုံးပြုလုပ်ခြင်း**
   - tiktoken သုံးနည်း ဥပမာများ ထည့်ရန်
   - prompt compression နည်းလမ်းများ ပြသရန်

### ၈.၂ ကုန်ကျစရိတ် ထိရောက်စွာ စီမံခန့်ခွဲမှု ဥပမာများ

ကြည့်ချင်သည်-
- ဆောင်ရွက်ရမည့် အလုပ်၏ ရှုပ်ထွေးမှုအရ မော်ဒယ်ရွေးချယ်ခြင်း
- Token ထိရောက်စေရေး prompt အင်ဂျင်နီယာနည်း
- အုပ်စုအလုပ်များအတွက် batch processing

---

## ၉။ အသုံးပြုရ လွယ်ကူမှုနှင့် အပြည်ပြည်ဆိုင်ရာ များ

### ၉.၁ လက်ရှိ ဘာသာပြန် အခြေအနေ

စာမျက်နှာအားလုံးကို [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) မှ အလိုအလျောက် ဘာသာပြန်ပြီး၊ ၅၀ ကျော် ဘာသာစကား များနှင့် သက်ဆိုင်ရာ သင်ရိုးညွှန်းတမ်းများကို အင်္ဂလိပ်မူရင်းနှင့် အမြဲတမ်း နောက်ဆက်တွဲထားသည်။ ဘာသာပြန်ထားသော အကြောင်းအရာများကို `translations/` ပိုင်းတွင်၊ ဒေသိယဓာတ်ပုံများကို `translated_images/` တွင် သိမ်းဆည်းထားသည်။ ပျမ်းမျှ ဘာသာစကားများစာရင်းကို repository README ထိပ်တွင် အရှင်းပြထားသည်။

| အချက်အလက် | အခြေအနေနှင့် |
|--------|--------|
| ဘာသာပြန်ပမာဏ | ပြီးစီး — ၅၀ ကျော် ဘာသာစကား၊ သင်ခန်းစာအားလုံး |
| ဘာသာပြန်နည်းလမ်း | [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) ဖြင့် အလိုအလျောက် |
| အင်္ဂလိပ်မူရင်းနဲ့ ထပ်တူညီပြောင်စေခြင်း | ဟုတ် — အလိုအလျောက် ပြန်လုပ်ခြင်း |

### ၉.၂ အသုံးပြုရ လွယ်ကူစေရန် တိုးတက်မှုများ

၁။ ပုံများအားလုံးကို alt text ထည့်ရန်
၂။ ကုဒ် ဥပမာများ syntax highlighting မှန်ကန်စေရန် သေချာလုပ်ရန်
၃။ ဗီဒီယိုအကြောင်းအရာ အားလုံးအတွက် ဗီဒီယိုစာတမ်းများ ထည့်သွင်းရန်
၄။ အရောင်ကွာဟမှုသည် WCAG လမ်းညွန်ချက်နှင့်ကိုက်ညီမှု ရှိစေရန် သေချာလုပ်ရန်

---

## ၁၀။ အကောင်အထည်ဖော်မှု ဦးစားပေးမှု

### အဆင့် ၁: ချက်ချင်း (အပတ် ၁-၂)
- [x] အရေးကြီးလုံခြုံရေးပြဿနာများ ပြင်ဆင်ခြင်း
- [x] ကုဒ်အရည်အသွေး စီမံချက် ထည့်သွင်းခြင်း
- [x] ပူးပေါင်းအသုံးပြုရေး utilities ဖန်တီးခြင်း
- [x] လုံခြုံရေး လမ်းညွှန်ချက်များ စာတမ်းရေးခြင်း

### အဆင့် ၂: မကြာခဏ (အပတ် ၃-၄)
- [x] သုံးစွဲမှုမရ API pattern များ ပြောင်းရွှေ့သည်(Chat Completions → Responses API, Python + TypeScript)
- [ ] Python ဖိုင်အားလုံးတွင် type hints ထည့်သွင်းရန် (shared/ module တွင် ပြီးသား; သင်ခန်းစာများကို ရိုးရှင်းစွာ ထား)
- [x] CI/CD workflows တွင် ကုဒ်အရည်အသွေး ပြုလုပ်ထားခြင်း
- [x] လုံခြုံရေး စစ်ဆေးမှု workflow ဖန်တီးခြင်း

### အဆင့် ၃: အလယ်အလတ် (လ ၂-၃)
- [ ] လုံခြုံရေးသင်ခန်းစာ အသစ် ထည့်သွင်းရန်
- [ ] ထုတ်လုပ်မှုစနစ် သင်ခန်းစာ ထည့်သွင်းရန်
- [x] DevContainer ဆက်တင်တိုးတက်စေခြင်း
- [ ] အပြန်အလှန် ပြသမှုများ ထည့်သွင်းရန်

### အဆင့် ၄: ရေရှည် (လ ၄+)
- [ ] အဆင့်မြင့် RAG သင်ခန်းစာ ထည့်သွင်းရန်
- [ ] ဘာသာစကားထောက်ခံမှု တိုးချဲ့ရန်
- [ ] စစ်ဆေးမှုအစုံလမ်း စုပြုလုပ်ရန်
- [ ] လက်မှတ်ပေးအစီအစဉ် ဖန်တီးရန်

---

## နိဂုံးချုပ်

ဤလမ်းပြမြေပုံသည် Generative AI for Beginners သင်ရိုးညွှန်းတမ်းကို တိုးတက်စေဖို့ စနစ်တကျ ချမှတ်ထားသောနည်းလမ်းဖြစ်သည်။ လုံခြုံရေးပြဿနာများကို ဖြေပေါ်ဖယ်ရှားခြင်း၊ API များကို ခေတ်မီလာစေခြင်းနှင့် ပညာရေး အကြောင်းအရာများ ထည့်သွင်းခြင်းဖြင့် သင်တန်းသားများအတွက် အတော်လေးကောင်းမွန်သော နိုင်ငံတကာ AI အသုံးပြုမှုဖွံ့ဖြိုးတိုးတက်မှုအတွက် ပြင်ဆင်ပေးမည် ဖြစ်သည်။

မေးခွန်းများ သို့မဟုတ် ဆောင်ရွက်လှူဒါန်းမှုများအတွက် GitHub repository တွင် issue ဖွင့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->