<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:13:45+00:00",
  "source_file": "AGENTS.md",
  "language_code": "my"
}
-->
# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

ဤ repository တွင် Generative AI အခြေခံနှင့် အက်ပလီကေးရှင်းဖွံ့ဖြိုးတိုးတက်မှုကို သင်ကြားပေးသည့် 21-သင်ခန်းစာများပါဝင်သော သင်ခန်းစာအစီအစဉ်တစ်ခုပါဝင်သည်။ သင်ခန်းစာများသည် အခြေခံအကြောင်းအရာများမှ စတင်ပြီး ထုတ်လုပ်မှုအဆင့်အက်ပလီကေးရှင်းများတည်ဆောက်ခြင်းအထိ အဆင့်ဆင့်သင်ကြားပေးရန် ရည်ရွယ်ထားသည်။

**အဓိကနည်းပညာများ:**
- Python 3.9+ နှင့် `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib` စသည်တို့ပါဝင်သော libraries
- TypeScript/JavaScript နှင့် Node.js libraries: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, နှင့် GitHub Models
- Jupyter Notebooks ကို interactive သင်ကြားမှုအတွက် အသုံးပြုခြင်း
- Dev Containers ကို တူညီသော ဖွံ့ဖြိုးတိုးတက်မှုပတ်ဝန်းကျင်အတွက် အသုံးပြုခြင်း

**Repository ဖွဲ့စည်းမှု:**
- 21 ခုသော သင်ခန်းစာ directories (00-21) တွင် README, code examples, နှင့် assignments ပါဝင်သည်
- အမျိုးမျိုးသော အကောင်အထည်ဖော်မှုများ: Python, TypeScript, နှင့် တခါတရံ .NET examples
- 40+ ဘာသာစကား version များပါဝင်သော Translations directory
- `.env` ဖိုင်မှတစ်ဆင့် အချက်အလက်များကို စုစည်းထားခြင်း (`.env.copy` ကို template အဖြစ်အသုံးပြုပါ)

## Setup Commands

### Repository စတင်တပ်ဆင်ခြင်း

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python ပတ်ဝန်းကျင် Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript Setup

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (အကြံပြုထားသည်)

ဤ repository တွင် GitHub Codespaces သို့မဟုတ် VS Code Dev Containers extension အတွက် `.devcontainer` configuration ပါဝင်သည်:

1. GitHub Codespaces သို့မဟုတ် VS Code တွင် repository ကို ဖွင့်ပါ
2. Dev Container သည် အလိုအလျောက်:
   - `requirements.txt` မှ Python dependencies များကို install လုပ်ပါမည်
   - post-create script (`.devcontainer/post-create.sh`) ကို run လုပ်ပါမည်
   - Jupyter kernel ကို setup လုပ်ပါမည်

## ဖွံ့ဖြိုးတိုးတက်မှု Workflow

### Environment Variables

API access လိုအပ်သော သင်ခန်းစာများအားလုံးသည် `.env` တွင် သတ်မှတ်ထားသော environment variables ကို အသုံးပြုသည်:

- `OPENAI_API_KEY` - OpenAI API အတွက်
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service အတွက်
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment name
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment name
- `AZURE_OPENAI_API_VERSION` - API version (default: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face models အတွက်
- `GITHUB_TOKEN` - GitHub Models အတွက်

### Python Examples ကို run လုပ်ခြင်း

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript Examples ကို run လုပ်ခြင်း

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks ကို run လုပ်ခြင်း

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### သင်ခန်းစာအမျိုးအစားများနှင့် အလုပ်လုပ်ခြင်း

- **"Learn" သင်ခန်းစာများ**: README.md documentation နှင့် အကြောင်းအရာများကို အဓိကထားသည်
- **"Build" သင်ခန်းစာများ**: Python နှင့် TypeScript တွင် အလုပ်လုပ်နိုင်သော code examples များပါဝင်သည်
- သင်ခန်းစာတစ်ခုစီတွင် theory, code walkthroughs, နှင့် video content link များပါဝင်သော README.md ပါဝင်သည်

## Code Style Guidelines

### Python

- Environment variable management အတွက် `python-dotenv` ကို အသုံးပြုပါ
- API interactions အတွက် `openai` library ကို import လုပ်ပါ
- Linting အတွက် `pylint` ကို အသုံးပြုပါ (တချို့သော examples တွင် `# pylint: disable=all` ပါဝင်သည်)
- PEP 8 naming conventions ကို လိုက်နာပါ
- API credentials များကို `.env` ဖိုင်တွင် သိမ်းဆည်းပါ၊ code တွင် မထည့်ပါနှင့်

### TypeScript

- Environment variables အတွက် `dotenv` package ကို အသုံးပြုပါ
- App တစ်ခုစီအတွက် `tsconfig.json` တွင် TypeScript configuration ကို သတ်မှတ်ပါ
- Azure services အတွက် `@azure/openai` သို့မဟုတ် `@azure-rest/ai-inference` ကို အသုံးပြုပါ
- Development အတွက် auto-reload အတွက် `nodemon` ကို အသုံးပြုပါ
- Run လုပ်မီ build လုပ်ပါ: `npm run build` ထို့နောက် `npm start`

### အထွေထွေသဘောတရားများ

- Code examples များကို ရိုးရှင်းပြီး သင်ကြားမှုအတွက် အကျိုးရှိအောင်ထားပါ
- အဓိကအကြောင်းအရာများကို ရှင်းလင်းသော comments များထည့်ပါ
- သင်ခန်းစာတစ်ခုစီ၏ code သည် self-contained ဖြစ်ပြီး run လုပ်နိုင်ရမည်
- Consistent naming ကို အသုံးပြုပါ: Azure OpenAI အတွက် `aoai-`, OpenAI API အတွက် `oai-`, GitHub Models အတွက် `githubmodels-`

## Documentation Guidelines

### Markdown Style

- URLs များကို `[text](../../url)` format ဖြင့် wrap လုပ်ထားရမည်၊ အပိုနေရာများမပါရ
- Relative links များသည် `./` သို့မဟုတ် `../` ဖြင့် စတင်ရမည်
- Microsoft domains သို့ link များတွင် tracking ID ပါဝင်ရမည်: `?WT.mc_id=academic-105485-koreyst`
- URLs တွင် နိုင်ငံအလိုက် locales မပါရ (e.g., `/en-us/` မပါရ)
- `./images` folder တွင် descriptive names ဖြင့် images များကို သိမ်းဆည်းပါ
- ဖိုင်နာမည်များတွင် အင်္ဂလိပ်အက္ခရာများ၊ နံပါတ်များ၊ နှင့် dashes ကို အသုံးပြုပါ

### Translation Support

- Repository သည် GitHub Actions မှတစ်ဆင့် 40+ ဘာသာစကားများကို ပံ့ပိုးသည်
- Translations များကို `translations/` directory တွင် သိမ်းဆည်းထားသည်
- အစိတ်အပိုင်း translation များကို မတင်ပါနှင့်
- Machine translations မလက်ခံပါ
- Translated images များကို `translated_images/` directory တွင် သိမ်းဆည်းထားသည်

## Testing and Validation

### Pre-submission Checks

ဤ repository သည် GitHub Actions ကို validation အတွက် အသုံးပြုသည်။ PR မတင်မီ:

1. **Markdown Links ကို စစ်ဆေးပါ**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manual Testing**:
   - Python examples များကို စမ်းသပ်ပါ: venv ကို activate လုပ်ပြီး scripts များကို run လုပ်ပါ
   - TypeScript examples များကို စမ်းသပ်ပါ: `npm install`, `npm run build`, `npm start`
   - Environment variables များကို မှန်ကန်စွာ configure လုပ်ထားကြောင်း စစ်ဆေးပါ
   - API keys များသည် code examples များနှင့် အလုပ်လုပ်ကြောင်း စစ်ဆေးပါ

3. **Code Examples**:
   - Code များသည် error မရှိဘဲ run လုပ်နိုင်ရမည်
   - Azure OpenAI နှင့် OpenAI API နှစ်ခုစလုံးတွင် အလုပ်လုပ်ကြောင်း စမ်းသပ်ပါ
   - GitHub Models ကို support လုပ်သောနေရာများတွင် စမ်းသပ်ပါ

### Automated Tests မပါဝင်ပါ

ဤသည်သည် သင်ကြားမှုနှင့် ဥပမာများအတွက် အဓိကထားသော repository ဖြစ်သည်။ Unit tests သို့မဟုတ် integration tests မပါဝင်ပါ။ Validation သည် အဓိကအားဖြင့်:
- Code examples များကို လက်ဖြင့် စမ်းသပ်ခြင်း
- Markdown validation အတွက် GitHub Actions
- သင်ကြားမှုအကြောင်းအရာများကို Community review

## Pull Request Guidelines

### Submitting မတင်မီ

1. Python နှင့် TypeScript နှစ်ခုစလုံးတွင် code changes များကို စမ်းသပ်ပါ
2. Markdown validation ကို run လုပ်ပါ (PR တင်သောအခါ အလိုအလျောက် run လုပ်သည်)
3. Microsoft URLs တွင် tracking IDs ပါဝင်ကြောင်း စစ်ဆေးပါ
4. Relative links များသည် မှန်ကန်ကြောင်း စစ်ဆေးပါ
5. Images များကို မှန်ကန်စွာ reference လုပ်ထားကြောင်း စစ်ဆေးပါ

### PR Title Format

- ဖော်ပြချက်အကျဉ်းရင်း: `[Lesson 06] Fix Python example typo` သို့မဟုတ် `Update README for lesson 08`
- အရေးပါသော issue နံပါတ်များကို ရည်ညွှန်းပါ: `Fixes #123`

### PR Description

- ပြင်ဆင်ထားသောအရာများနှင့် အကြောင်းရင်းကို ရှင်းပြပါ
- ဆက်စပ်သော issues များ link လုပ်ပါ
- Code changes များအတွက် စမ်းသပ်ထားသော examples များကို ဖော်ပြပါ
- Translation PR များအတွက် အပြည့်အစုံသော translation ဖိုင်များကို ထည့်ပါ

### Contribution Requirements

- Microsoft CLA ကို လက်မှတ်ထိုးပါ (ပထမဆုံး PR တင်သောအခါ အလိုအလျောက်)
- Repository ကို သင့်အကောင့်သို့ fork လုပ်ပြီး ပြင်ဆင်ပါ
- Logical change တစ်ခုစီအတွက် PR တစ်ခု (မသက်ဆိုင်သော fixes များကို ပေါင်းစပ်မထားပါနှင့်)
- PR များကို အလေးမရှိအောင်ထားပြီး အလေးအနက်ထားပါ

## Common Workflows

### Code Example အသစ်တစ်ခု ထည့်သွင်းခြင်း

1. သင့် lesson directory သို့ သွားပါ
2. `python/` သို့မဟုတ် `typescript/` subdirectory တွင် example ကို ဖန်တီးပါ
3. Naming convention ကို လိုက်နာပါ: `{provider}-{example-name}.{py|ts|js}`
4. အမှန်တကယ် API credentials ဖြင့် စမ်းသပ်ပါ
5. Lesson README တွင် အသစ်ထည့်သွင်းထားသော environment variables များကို documentation ပြုလုပ်ပါ

### Documentation ကို Update လုပ်ခြင်း

1. Lesson directory တွင် README.md ကို ပြင်ဆင်ပါ
2. Markdown guidelines ကို လိုက်နာပါ (tracking IDs, relative links)
3. Translation များကို GitHub Actions မှ handle လုပ်သည် (manual edit မလုပ်ပါနှင့်)
4. Links များသည် မှန်ကန်ကြောင်း စမ်းသပ်ပါ

### Dev Containers နှင့် အလုပ်လုပ်ခြင်း

1. Repository တွင် `.devcontainer/devcontainer.json` ပါဝင်သည်
2. Post-create script သည် Python dependencies များကို အလိုအလျောက် install လုပ်သည်
3. Python နှင့် Jupyter အတွက် extensions များကို pre-configure လုပ်ထားသည်
4. Environment သည် `mcr.microsoft.com/devcontainers/universal:2.11.2` အပေါ်မှာ အခြေခံထားသည်

## Deployment နှင့် Publishing

ဤသည်သည် သင်ကြားမှု repository ဖြစ်သည် - deployment လုပ်ငန်းစဉ်မပါဝင်ပါ။ Curriculum ကို အောက်ပါနည်းလမ်းများဖြင့် အသုံးပြုသည်:

1. **GitHub Repository**: Code နှင့် documentation ကို တိုက်ရိုက် access လုပ်နိုင်သည်
2. **GitHub Codespaces**: Pre-configured setup ဖြင့် dev environment ကို ချက်ချင်းအသုံးပြုနိုင်သည်
3. **Microsoft Learn**: Content ကို တရားဝင်သင်ကြားမှု platform သို့ syndicate လုပ်နိုင်သည်
4. **docsify**: Markdown မှ documentation site တည်ဆောက်ထားသည် (e.g., `docsifytopdf.js` နှင့် `package.json`)

### Documentation Site တည်ဆောက်ခြင်း

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Troubleshooting

### အများဆုံးတွေ့ရသောပြဿနာများ

**Python Import Errors**:
- Virtual environment ကို activate လုပ်ထားကြောင်း သေချာပါ
- `pip install -r requirements.txt` ကို run လုပ်ပါ
- Python version သည် 3.9+ ဖြစ်ကြောင်း စစ်ဆေးပါ

**TypeScript Build Errors**:
- App directory တွင် `npm install` ကို run လုပ်ပါ
- Node.js version သည် အထောက်အပံ့ပေးနိုင်ကြောင်း စစ်ဆေးပါ
- `node_modules` ကို ရှင်းပြီး ပြန် install လုပ်ပါ

**API Authentication Errors**:
- `.env` ဖိုင်ရှိကြောင်းနှင့် မှန်ကန်သော values များပါဝင်ကြောင်း စစ်ဆေးပါ
- API keys သည် သက်တမ်းကုန်ဆုံးမထားကြောင်း စစ်ဆေးပါ
- Endpoint URLs သည် region အတွက် မှန်ကန်ကြောင်း စစ်ဆေးပါ

**Missing Environment Variables**:
- `.env.copy` ကို `.env` သို့ copy လုပ်ပါ
- သင်လုပ်နေသော lesson အတွက် လိုအပ်သော values များကို ဖြည့်ပါ
- `.env` ကို update လုပ်ပြီး application ကို ပြန်စတင်ပါ

## အပိုဆောင်းအရင်းအမြစ်များ

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Project-Specific Notes

- ဤသည်သည် **သင်ကြားမှု repository** ဖြစ်ပြီး production code မဟုတ်ပါ
- Examples များသည် ရိုးရှင်းပြီး သင်ကြားမှုအတွက် အဓိကထားသည်
- Code quality ကို သင်ကြားမှုရှင်းလင်းမှုနှင့် အညီချိန်ညှိထားသည်
- သင်ခန်းစာတစ်ခုစီသည် self-contained ဖြစ်ပြီး အချိန်မရွေး ပြီးစီးနိုင်သည်
- Repository သည် API providers များစွာကို ပံ့ပိုးသည်: Azure OpenAI, OpenAI, နှင့် GitHub Models
- Content သည် multilingual ဖြစ်ပြီး automated translation workflows ပါဝင်သည်
- မေးခွန်းများနှင့် အထောက်အပံ့အတွက် Discord တွင် active community ရှိသည်

---

**ဝန်ခံချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ဘာသာပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲသိမှားမှုများ သို့မဟုတ် အဓိပ္ပါယ်မှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။