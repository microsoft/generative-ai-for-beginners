# ផ្លូវផែនការពង្រឹងមុខងារ និងការកែលម្អ

ឯកសារនេះបង្ហាញពីការផ្តល់អនុសាសន៍សម្រាប់ការពង្រឹង និងការកែលម្អសម្រាប់មេរៀន Generative AI សម្រាប់អ្នកចាប់ផ្តើម ដែលផ្អែកលើការត្រួតពិនិត្យកូដយ៉ាងទូលំទូលាយ និងវិភាគលើការអនុវត្តល្អបំផុតក្នុងឧស្សាហកម្ម។

## សង្ខេបអគ្គិសនី

មូលដ្ឋានកូដត្រូវបានវិភាគសម្រាប់សុវត្ថិភាព គុណភាពកូដ និងប្រសិទ្ធភាពសិក្សា។ ឯកសារនេះផ្តល់អនុសាសន៍សម្រាប់ការជួសជុលបន្ទាន់ ការកែលម្អរយៈពេលខ្លី និងការពង្រឹងដំណាក់កាលអនាគត។

---

## ១. ការពង្រឹងសុវត្ថិភាព (អាទិភាព៖ សំខាន់)

### ១.១ ការជួសជុលបន្ទាន់ (បានបញ្ចប់)

| បញ្ហា | ឯកសារប៉ះពាល់ | ស្ថានភាព |
|-------|----------------|--------|
| SECRET_KEY ខ្ទេចខ្លួន | `05-advanced-prompts/python/aoai-solution.py` | បានជួសជុល |
| ខ្វះការត្រួតពិនិត្យ env | ឯកសារ JS/TS ច្រើន | បានជួសជុល |
| ការហៅមុខងារមានហានិភ័យ | `11-integrating-with-function-calling/js-githubmodels/app.js` | បានជួសជុល |
| ការបាត់បង់ handle ឯកសារ | `08-building-search-applications/scripts/` | បានជួសជុល |
| ខ្វះកំណត់ពេលវេលា request | `09-building-image-applications/python/` | បានជួសជុល |

### ១.២ មុខងារសុវត្ថិភាពបន្ថែមដែលបានផ្តល់អនុសាសន៍

១. **ឧទាហរណ៍ការគ្រប់គ្រងអត្រា (Rate Limiting)**
   - បន្ថែមកូដឧទាហរណ៍បង្ហាញរបៀបអនុវត្តការគ្រប់គ្រងអត្រា សម្រាប់ការហៅ API
   - បង្ហាញលំនាំបញ្ច្រាសវាស់តម្លៃជាលំដាប់បូកគ្នា (exponential backoff)

២. **ការប្រែប្រួលកន្លែងប្រាក់ API Key**
   - បន្ថែមឯកសារពាក់ព័ន្ធនឹងការអនុវត្តល្អបំផុតសម្រាប់ការប្រែប្រួលកន្លែងប្រាក់ API Key
   - រួមបញ្ចូលឧទាហរណ៍ប្រើ Azure Key Vault ឬសេវាកម្មដូចគ្នា

៣. **ការតភ្ជាប់សុវត្ថិភាពមាតិកា (Content Safety Integration)**
   - បន្ថែមឧទាហរណ៍ប្រើ Azure Content Safety API
   - បង្ហាញលំនាំបញ្ច្រាសការត្រួតពិនិត្យការបញ្ចូល/ចេញ

---

## ២. ការកែលម្អគុណភាពកូដ

### ២.១ បន្ថែមឯកសារកំណត់រចនា

| ឯកសារ | គោលបំណង |
|------|---------|
| `.eslintrc.json` | ច្បាប់ linting សម្រាប់ JavaScript/TypeScript |
| `.prettierrc` | ស្តង់ដារការរៀបចំកូដ |
| `pyproject.toml` | ការកំណត់ឧបករណ៍ Python (Black, Ruff, mypy) |

### ២.២ បង្កើតឧបករណ៍ចែករំលែក

ម៉ូឌុល `shared/python/` ថ្មី ជាមួយ៖
- `env_utils.py` - ការដោះស្រាយអថេរបរិស្ថាន
- `input_validation.py` - ការត្រួតពិនិត្យនិងសម្អាតការបញ្ចូល
- `api_utils.py` - ការការពារខ្ទង់ជំរុញ API

### ២.៣ ការផ្តល់អនុសាសន៍កែលម្អកូដ

១. **ការគ្របដណ្តប់ការ Type Hints**
   - បន្ថែម type hints ទៅឯកសារពី Python ទាំងអស់
   - បើករបៀប strict TypeScript ទៅរាល់គម្រោង TS

២. **ស្តង់ដារឯកសារព័ត៌មាន**
   - បន្ថែម docstrings ទៅមុខងារ Python ទាំងអស់
   - បន្ថែមសកម្មជំនួយ JSDoc ទៅមុខងារ JavaScript/TypeScript ទាំងអស់

៣. **ស៊ុមតេស្ដ Framework**
   - បន្ថែមការកំណត់ pytest និងការតេស្តឧទាហរណ៍ _(បានធ្វើរួច៖ កំណត់ pytest នៅ `pyproject.toml`; តេស្តឧទាហរណ៍សម្រាប់ឧបករណ៍ចែករំលែកនៅ [`tests/`](../../../tests) ដំណើរការនៅ CI)_
   - បន្ថែមការកំណត់ Jest សម្រាប់ JavaScript/TypeScript

---

## ៣. ការពង្រឹងការអប់រំ

### ៣.១ មុខវិជ្ជាថ្មី

១. **សុវត្ថិភាពក្នុងកម្មវិធី AI** (មុខវិជ្ជាផ្តល់អនុសាសន៍លេខ ២២)
   - ការវាយប្រហារចាក់បញ្ចូល (prompt injection) និងការការពារ
   - ការគ្រប់គ្រង API key
   - ការត្រួតពិនិត្យមាតិកា
   - ការគ្រប់គ្រងអត្រា និងការការពារការបំពាន

២. **ការដាក់ឲ្យដំណើរការផលិតកម្ម** (មុខវិជ្ជាផ្តល់អនុសាសន៍លេខ ២៣)
   - ការប្រើ container ជាមួយ Docker
   - CI/CD pipeline
   - ការត្រួតពិនិត្យ និងកំណត់ហេតុ
   - ការគ្រប់គ្រងថ្លៃដើម

៣. **បច្ចេកវិទ្យា RAG ជ្រាលជ្រៅ** (មុខវិជ្ជាផ្តល់អនុសាសន៍លេខ ២៤)
   - ស្វែងរកតម្រង (keyword + semantic)
   - គោលការណ៍រៀបចំឡើងវិញ
   - RAG ច្រើនម៉ូត
   - គោលវិនិច្ឆ័យ

### ៣.២ ការកែលម្អមុខវិជ្ជាមុនមាន

| មុខវិជ្ជា | ការកែលម្អដែលផ្តល់អនុសាសន៍ |
|--------|----------------------------|
| ០៦ - ការបង្កើតអត្ថបទ | បន្ថែមឧទាហរណ៍ចម្លើយចាក់ផ្សាយបន្តផ្ទាល់ |
| ០៧ - កម្មវិធីចាប់អារម្មណ៍ | បន្ថែមលំនាំការចងចាំសន្ទនា |
| ០៨ - កម្មវិធីស្វែងរក | បន្ថែមការប្រៀបធៀបមូលដ្ឋានទិន្នន័យវ៉ិចទ័រ |
| ០៩ - ការបង្កើតរូបភាព | បន្ថែមឧទាហរណ៍កែប្រែ/បម្លែងរូបភាព |
| ១១ - ការហៅមុខងារ | បន្ថែមការហៅមុខងារប្រតិបត្តិការជាប្រភាគ |
| ១៥ - RAG | បន្ថែមការប្រៀបធៀបយុទ្ធសាស្ត្របែងចែក |
| ១៧ - អ្នកប្រើ AI | បន្ថែមការគ្រប់គ្រងអង្គភាពអ្នកប្រើច្រើន |

---

## ៤. ការអភិវឌ្ឍ API ទាន់សម័យ

### ៤.១ លំនាំ API ដែលបានដកចេញ (ការផ្លាស់ប្តូរបានបញ្ចប់)

គំរូ chat ទាំងអស់សម្រាប់ Python និង TypeScript ត្រូវបានផ្លាស់ប្តូរពី Chat Completions API ទៅ Responses API (`client.responses.create(...)` → `response.output_text`)។

| លំនាំចាស់ | លំនាំថ្មី | ស្ថានភាព |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | បានបញ្ចប់ |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | បានបញ្ចប់ |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | កញ្ចប់ `openai` `client.responses.create()` → `response.output_text` | បានបញ្ចប់ |
| `df.append()` (pandas) | `pd.concat()` | បានបញ្ចប់ |

> **សម្គាល់៖** គំរូ Microsoft Foundry Models ដែលប្រើ `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) នៅតែប្រើ Model Inference API ដែលមិនគាំទ្រ Responses API។ `AzureOpenAI()` ត្រូវបានរក្សាទុកដោយចេតនា នៅកន្លែងដែលនៅសុពលភាព (embeddings និងការបង្កើតរូបភាព)។

### ៤.២ មុខងារ API ថ្មីសម្រាប់បង្ហាញ

១. **លទ្ធផលមានរចនាសម្ព័ន្ធ** (OpenAI)
   - របៀប JSON
   - ការហៅមុខងារជាមួយ schema ដែលតឹងរ៉ឹង

២. **សមត្ថភាពមើលឃើញ**
   - វិភាគរូបភាពជាមួយ GPT-4o (vision)
   - និទ្ទេសម៉ូដច្រើន

៣. **ឧបករណ៍ក្នុង Responses API** (ជំនុំបច្ចុប្បន្ននៃ Assistants API ប្រកបដោយកន្លែងបច្ចុប្បន្ន)
   - អ្នកប្រែសម្រួលកូដ
   - ស្វែងរកឯកសារ
   - ស្វែងរកវេបសាយ និងឧបករណ៍ផ្ទាល់ខ្លួន

---

## ៥. ការកែលម្អហេដ្ឋារចនាសម្ព័ន្ធ

### ៥.១ ការពង្រឹង CI/CD

អនុវត្តនៅក្នុង [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): ការត្រួតពិនិត្យ/រៀបចំ Python (Ruff + Black) ត្រូវបានអនុវត្តយ៉ាងម៉ឺងម៉ាត់លើម៉ូឌុលឧបករណ៍ចែករំលែក `shared/` ហើយដំណើរការជាអនុសាសន៍សម្រាប់មេរៀនផ្សេងទៀត ជាមួយនឹង ESLint ដំណើរការជាអនុសាសន៍សម្រាប់ JavaScript/TypeScript។ ម៉ូឌែលគំរូគឺ៖

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

### ៥.២ ការស្កេនសុវត្ថិភាព

អនុវត្តនៅក្នុង [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): វិភាគ CodeQL សម្រាប់ Python និង JavaScript/TypeScript (នៅពេលអ្នកបញ្ចូល ការស្នើសុំ pull និងកាលវិភាគប្រចាំសប្តាហ៍) រួមជាមួយពិនិត្យាពាក្យទំនាក់ទំនងនៅការស្នើសុំ pull។ ម៉ូឌែលគំរូគឺ៖

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

## ៦. ការកែលម្អបទពិសោធន៍អ្នកអភិវឌ្ឍ

### ៦.១ ការពង្រឹង DevContainer

អនុវត្តនៅក្នុង [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) និង [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): container ឥឡូវនេះផ្ញើ Pylance, អ្នករៀបចំកូដ Black, Ruff, ESLint, Prettier និងជំនួយ Copilot, បើកការរៀបចំដោយស្វ័យប្រវត្តិពេលរក្សាទុកតភ្ជាប់ទៅកំណត់ Black/Prettier របស់ repo និងដំឡើងឧបករណ៍អភិវឌ្ឍន៍ (`ruff`, `black`, `mypy`, `pytest`) ដើម្បីអាចកាត់ថ្មបំណុល [code-quality workflow](../../../.github/workflows/code-quality.yml) នៅជាលokal។ រូបភាពមូលដ្ឋាន `mcr.microsoft.com/devcontainers/universal` មាន Python និង Node រួចហើយ ដូច្នេះមិនចាំបាច់រំពឹងមុខងារថ្មីទៀតឡើយ។ ម៉ូឌែលគំរូគឺ៖

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

### ៦.២ វាលលេងអន្តរកម្ម

ចងចាំបន្ថែម៖
- សៀវភៅ Jupyter ដែលបំពេញ API key ស្រាប់ (តាមអថេរបរិស្ថាន)
- ការបង្ហាញ Gradio/Streamlit សម្រាប់អ្នករៀនមានទស្សនៈ
- គណនាការប្រលងអន្តរកម្មសម្រាប់វាយតម្លៃចំណេះដឹង

---

## ៧. ការគាំទ្រភាសាជាច្រើន

### ៧.១ ការគ្របដណ្តប់ភាសាបច្ចុប្បន្ន

| បច្ចេកវិទ្យា | មុខវិជ្ជាដែលគ្របដណ្តប់ | ស្ថានភាព |
|------------|-----------------|--------|
| Python | ទាំងអស់ | សម្រេច |
| TypeScript | ០៦-០៩, ១១ | ផ្នែក |
| JavaScript | ០៦-០៨, ១១ | ផ្នែក |
| .NET/C# | មួយចំនួន | ផ្នែក |

### ៧.២ ការបន្ថែមដែលផ្តល់អនុសាសន៍

១. **Go** - កំពុងធំឡើងក្នុងឧបករណ៍ AI/ML
២. **Rust** - កម្មវិធីដែលត្រូវការសមត្ថភាពខ្ពស់
៣. **Java/Kotlin** - កម្មវិធីសហគ្រាស

---

## ៨. ការបង្កើនប្រសិទ្ធភាព

### ៨.១ ការបង្កើនប្រសិទ្ធភាពកូដ

១. **លំនាំ Async/Await**
   - បន្ថែមឧទាហរណ៍ async សម្រាប់ការបង្ហោះជាកញ្ចប់
   - បង្ហាញការហៅ API សម័យជាប្រភាគ

២. **យុទ្ធសាស្ត្រការបញ្ចូលបង្រួចទៅដើម្បីប្រើប្រាស់ម្ដងទៀត**
   - បន្ថែមឧទាហរណ៍ caching embedding
   - បង្ហាញលំនាំ caching ចម្លើយ

៣. **ពន្លឿនកំណត់ចំនួន token**
   - បន្ថែមឧទាហរណ៍ប្រើ tiktoken
   - បង្ហាញបច្ចេកទេសបង្រួបបំបែក prompt

### ៨.២ ឧទាហរណ៍កែលម្អថ្លៃដើម

បន្ថែមឧទាហរណ៍បង្ហាញ៖
- ជ្រើសរើសម៉ូឌែលផ្អែកលើភាពស្មុគស្មាញនៃភារកិច្ច
- វិជ្ជាជីវៈ prompt សម្រាប់ប្រសិទ្ធភាព token
- ការដាក់បង្ហោះជាកញ្ចប់សម្រាប់ប្រតិបត្តិការជាច្រើន

---

## ៩. ការចូលប្រើ និងអន្តរជាតិ

### ៩.១ ស្ថានភាពបកប្រែបច្ចុប្បន្ន

ការបកប្រែទាំងអស់គឺ **សម្រេចរួច** និងផលិតដោយស្វ័យប្រវត្តិដោយ [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) ដែលបង្កើត និងរក្សាមូលដ្ឋានមេរៀនច្រើនជាង ៥០ ភាសាឲ្យឲ្យម៉េចស្របគ្នាជាមួយប្រភពភាសាអង់គ្លេស។ អត្ថបទបកប្រែមាននៅក្នុង `translations/` និងរូបភាពត្រូវបានបំលែងនៅក្នុង `translated_images/`; បញ្ជីភាសាដែលមានមានផ្សាយនៅកំពូល README របស់ repository។

| មុខងារ | ស្ថានភាព |
|--------|--------|
| ការគ្របដណ្តប់ការបកប្រែ | សម្រេច — ៥០+ ភាសា, មុខវិជ្ជាទាំងអស់ |
| វិធីសាស្ត្របកប្រែ | ស្វ័យប្រវត្តិតាម [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| រក្សាជាមួយប្រភពភាសាអង់គ្លេស | បាទ — ធ្វើឡើងវិញដោយស្វ័យប្រវត្តិ |

### ៩.២ ការពង្រឹងការចូលប្រើ

១. បន្ថែមអត្ថបទ alt ទៅកាន់រូបភាពទាំងអស់
២. បញ្ជាក់ឲ្យគំរូកូដមានការបញ្ចេញពណ៌ syntax ត្រឹមត្រូវ
៣. បន្ថែមអត្ថបទបកប្រែវីដេអូសម្រាប់សារវីដេអូទាំងអស់
៤. បញ្ជាក់ឲ្យការប្រៀបផ្ទៃពណ៌ផ្គូរផ្គងតាមលក្ខខណ្ឌ WCAG

---

## ១០. អាទិភាពអនុវត្ត

### ជំហាន ១: បន្ទាន់ (សប្តាហ៍ ១-២)
- [x] ជួសជុលបញ្ហាសុវត្ថិភាពសំខាន់
- [x] បន្ថែមកំណត់រចនាគុណភាពកូដ
- [x] បង្កើតឧបករណ៍ចែករំលែក
- [x] លាយបញ្ចូលគោលការណ៍សុវត្ថិភាព

### ជំហាន ២: រយៈពេលខ្លី (សប្តាហ៍ ៣-៤)
- [x] បន្ទាន់សម័យលំនាំ API ដែលដកចេញ (Chat Completions → Responses API, Python + TypeScript)
- [ ] បន្ថែម type hints ទៅឯកសារ Python ទាំងអស់ (បានធ្វើសម្រាប់ម៉ូឌុល `shared/` ដែលគ្រប់គ្រង; គំរូមេរៀនរក្សាទុកឲ្យសាមញ្ញ)
- [x] បន្ថែមប្រតិបត្តិការចងក្រង CI/CD សម្រាប់គុណភាពកូដ
- [x] បង្កើតប្រតិបត្តិការ scanning សុវត្ថិភាព

### ជំហាន ៣: រយៈពេលមធ្យម (ខែ ២-៣)
- [ ] បន្ថែមមេរៀនសុវត្ថិភាពថ្មី
- [ ] បន្ថែមមេរៀនដាក់ប្រែកម្មវិធីផលិតកម្ម
- [x] កែលម្អការកំណត់ DevContainer
- [ ] បន្ថែមការបង្ហាញអន្តរកម្ម

### ជំហាន ៤: រយៈពេលយូរ (ខែ ៤+)
- [ ] បន្ថែមមេរៀន RAG ជ្រាលជ្រៅ
- [ ] ពង្រីកការគ្របដណ្តប់ភាសា
- [ ] បន្ថែមស៊ុមតេស្ដទូលំទូលាយ
- [ ] បង្កើតកម្មវិធីបញ្ញត្តិ

---

## សេចក្ដីសន្និដ្ឋាន

ផ្លូវផែនការនេះផ្តល់ជាទិដ្ឋភាពរៀបចំប្រព័ន្ធសម្រាប់ការកែលម្អមេរៀន Generative AI សម្រាប់អ្នកចាប់ផ្តើម។ ដោយដោះស្រាយបញ្ហាសុវត្ថិភាព អភិវឌ្ឍ API ទាន់សម័យ និងបន្ថែមចំណុចអប់រំថ្មីៗ វគ្គសិក្សាទាំងនេះនឹងជួយឲ្យសិស្សមានការរៀបចំល្អសម្រាប់ការអភិវឌ្ឍកម្មវិធី AI នៅពិភពជំនួញពិត។

សម្រាប់សំណួរ ឬការចូលរួម អញ្ជើញបើកបញ្ហានៅក្នុង repository GitHub។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->