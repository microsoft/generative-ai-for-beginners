# ការចាប់ផ្តើមជាមួយវគ្គសិក្សានេះ

យើងមានទឹកចិត្តរីករាយយ៉ាងខ្លាំងដែលអ្នកចាប់ផ្តើមវគ្គនេះ ហើយឃើញថាអ្នកមានការបញ្ចូលចិត្តក្នុងការសាងសង់អ្វីមួយជាមួយ Generative AI!

ដើម្បីធានាការជោគជ័យរបស់អ្នក ទំព័រនេះបង្ហាញពីជំហានដំឡើង អ wymag technical ក៏ដូចជាកន្លែងដែលអាចទទួលបានជំនួយប្រសិនបើចាំបាច់។

## ជំហានដំឡើង

ដើម្បីចាប់ផ្តើមវគ្គនេះ អ្នកត្រូវបញ្ចប់ជំហានដូចខាងក្រោម។

### 1. Fork repo นี้

[Fork repoទាំងមូលនេះ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ទៅគណនី GitHub របស់អ្នក ដើម្បីអាចផ្លាស់ប្តូរកូដណាមួយ និងបញ្ចប់ប挑战។ អ្នកក៏អាច [star (🌟) repoនេះ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ដើម្បីស្វែងរកវា និង repos ដែលទាក់ទងបានកាន់តែងាយស្រួល។

### 2. បង្កើត codespace

ដើម្បីជៀសវាងបញ្ហាអាស្រ័យភាពនៅពេលរត់កូដ យើងផ្តល់អនុសាសន៍ឲ្យដំណើរការវគ្គនេះនៅក្នុង [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)។

នៅក្នុង fork របស់អ្នក: **Code -> Codespaces -> New on main**

![ប្រអប់ការភ្ជាប់បង្ហាញប៊ូតុងសម្រាប់បង្កើត codespace](../../../translated_images/km/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 បន្ថែមសម្ងាត់

1. ⚙️ រូបតំណាងឧបករណ៍ -> Command Palette -> Codespaces : Manage user secret -> Add a new secret។
2. ឈ្មោះ OPENAI_API_KEY, បិទបិទកូនសោររបស់អ្នក, រក្សាទុក។

### 3. តើជំហានបន្ទាប់ជា​អ្វី?

| ខ្ញុំចង់…              | ទៅកាន់…                                                               |
|-------------------------|------------------------------------------------------------------------|
| ចាប់ផ្តើមមេរៀន 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ធ្វើការក្រៅបណ្តាញ        | [`setup-local.md`](02-setup-local.md)                                   |
| ដំឡើងអ្នកផ្គត់ផ្គង់ LLM | [`providers.md`](03-providers.md)                                        |
| ស្គាល់អ្នករៀនផ្សេងទៀត    | [ចូលរួម Discord របស់យើង](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ការដោះស្រាយបញ្ហា


| រោគសញ្ញា                               | ការដោះស្រាយ                                                     |
|-----------------------------------------|-----------------------------------------------------------------|
| ការសាងសង់ container ឈប់ស្ទើរពេញ > 10 នាទី    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | Terminal មិនបានភ្ជាប់; ចុច **+** ➜ *bash*                    |
| `401 Unauthorized` ពី OpenAI             | `OPENAI_API_KEY` មិនត្រឹមត្រូវ / ផុតកំណត់                      |
| VS Code បង្ហាញ “Dev container mounting…” | ធ្វើការបញ្ចូលទំព័រស៊ើបអ៊ិនហ្សើ—Codespaces មួយចំហៀងខ្សែកន្លង់ |
| មេដឹកនាំNotebookខ្វះ          | ម៉ឺនុយ Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   ប្រព័ន្ធ Unix-based:

   ```bash
   touch .env
   ```

   ប្រព័ន្ធ Windows:

   ```cmd
   echo . > .env
   ```

3. **កែសម្រួលឯកសារ `.env`**: បើកឯកសារ `.env` ក្នុងកម្មវិធីកែសម្រួលអក្សរ (ឧ. VS Code, Notepad++, ឬកម្មវិធីកែសម្រួលផ្សេងទៀត)។ បន្ថែមបន្ទាត់ខាងក្រោមទៅឯកសារ ប្តូរចន្លោះជាមួយចំណុចផ្តោតពិតរបស់អ្នកក្នុង Microsoft Foundry Models endpoint និង key (មើល [`providers.md`](03-providers.md) ដើម្បីស្វែងរករបៀបទទួលបាន)។

   > **កំណត់សម្គាល់:** GitHub Models (និង `GITHUB_TOKEN` variable) នឹងបញ្ឈប់ប្រើនៅចុងខែកក្កដា ២០២៦។ សូមប្រើប្រាស់ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ជំនួស។

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **រក្សាទុកឯកសារ**: រក្សាទុកការផ្លាស់ប្តូរ ហើយបិទកម្មវិធីកែសម្រួលអក្សរ។

5. **ដំឡើង `python-dotenv`**: ប្រសិនបើអ្នកមិនទាន់បានដំឡើង ទំព័រនេះត្រូវការដំឡើងកញ្ចប់ `python-dotenv` ដើម្បីដំណើរការបទលក្ខណៈបរិបទពី `.env` ទៅកម្មវិធី Python របស់អ្នក។ អ្នកអាចដំឡើងដោយប្រើ `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **ផ្ទុកបរិមាសបរិយាកាសក្នុង script Python របស់អ្នក**: ក្នុង script Python របស់អ្នក ប្រើកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកបរិមាសបរិយាកាសពីឯកសារ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # បញ្ចូលអថេរបរិស្ថិតពីឯកសារ .env
   load_dotenv()

   # ចូលប្រើអថេរលំនាំ Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

នេះហើយ! អ្នកបានបង្កើតឯកសារ `.env` រៀបរយ មានទិន្នន័យ Microsoft Foundry Models របស់អ្នក ហើយបានផ្ទុកវាទៅក្នុងកម្មវិធី Python របស់អ្នកដោយជោគជ័យ។

## របៀបរត់លើកុំព្យូទ័រពីរម៉ោង​របស់អ្នក

ដើម្បីរត់កូដនៅលើកុំព្យូទ័រពីរម៉ោងរបស់អ្នក អ្នកត្រូវតែមានកំណែ​មួយនៃ [Python ដែលបានដំឡើង](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)។

បន្ទាប់មក ដើម្បីប្រើ repository ត្រូវ clone វា៖

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ពេលអ្នកបានទៅពិនិត្យតម្រូវការទាំងអស់រួច អ្នកអាចចាប់ផ្តើមបាន!

## ជំហានជាជម្រើស

### ការដំឡើង Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) គឺជាកម្មវិធីដំឡើងស្រាលសម្រាប់ដំឡើង [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python និងកញ្ចប់មួយចំនួន។
Conda ជាគ្រប់គ្រងកញ្ចប់មួយដែលធ្វើឲ្យងាយក្នុងការតំឡើង និងផ្លាស់ប្តូរចន្លោះ Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) និងកញ្ចប់។ វាក៏មានប្រយោជន៍ក្នុងការដំឡើងកញ្ចប់មិនមាននៅក្នុង `pip` ផងដែរ។

អ្នកអាចអនុវត្តតាម [មគ្គុទ្ទេសក៍ដំឡើង MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ដើម្បីតំឡើងវា។

បន្ទាប់ពីដំឡើង Miniconda អ្នកត្រូវ clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ប្រសិនបើអ្នកមិនទាន់បាន)

បន្ទាប់មក អ្នកត្រូវបង្កើត virtual environment។ ដើម្បីធ្វើនេះជាមួយ Conda សូមបង្កើតឯកសារបរិយាកាសថ្មីមួយ (_environment.yml_)។ ប្រសិនបើអ្នកប្រើ Codespaces សូមបង្កើត ក្នុងថត `.devcontainer` គឺ `.devcontainer/environment.yml`។

សូមបញ្ចូលទិន្នន័យនៅក្នុងឯកសារបរិយាកាសដូចខាងក្រោម៖

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

ប្រសិនបើអ្នកមានកំហុសប្រើ conda អ្នកអាចដំឡើង Microsoft AI Libraries ដោយដំណើរការបញ្ជា Command ខាងក្រោម នៅក្នុង terminal។

```
conda install -c microsoft azure-ai-ml
```

ឯកសារបរិយាកាស បញ្ជាក់អាស្រ័យភាពដែលយើងត្រូវការ។ `<environment-name>` ជាឈ្មោះដែលអ្នកចង់ប្រើសម្រាប់ environment Conda របស់អ្នក ហើយ `<python-version>` ជាកំណែ Python ដែលអ្នកចង់ប្រើ ឧ. `3` ជាកំណែធំចុងក្រោយ។

បន្ទាប់ពីធ្វើរួច អ្នកអាចបង្កើត environment Conda ដោយបញ្ជារបញ្ជាទាំងនេះនៅ command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ផ្លូវរង .devcontainer មានប្រសិទ្ធភាពត្រឹមតែការដំឡើង Codespace ប៉ុណ្ណោះ
conda activate ai4beg
```

សូមយោងទៅ [មគ្គុទ្ទេសក៍ប្រើប្រាស់ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ប្រសិនបើមានបញ្ហា។

### ប្រើ Visual Studio Code ជាមួយផ្នែកបន្ថែម Python

យើងផ្តល់អនុសាសន៍ឲ្យប្រើ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ជាមួយ [ផ្នែកបន្ថែម Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) សម្រាប់វគ្គនេះ។ នេះគឺជាការផ្ដល់អនុសាសន៍មួយ ប៉ុន្តែមិនមែនជាការទាមទារគាប់គ្មាន។

> **កំណត់សម្គាល់**: ដោយបើក repo វគ្គសិក្សានៅក្នុង VS Code អ្នកអាចជ្រើសរើសដំឡើងគម្រោងក្នុង container។ សារសំខាន់សម្រាប់ [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ដែលមាននៅក្នុង repo វគ្គសិក្សា។ ព័ត៌មានបន្ថែមផ្នែកនេះនៅក្រោយ។

> **កំណត់សម្គាល់**: បន្ទាប់ពីអ្នក clone និងបើកថតក្នុង VS Code វានឹងផ្ដល់សំណើរ ដំឡើងផ្នែកបន្ថែម Python ដោយស្វ័យប្រវត្តិ។

> **កំណត់សម្គាល់**: ប្រសិនបើ VS Code ផ្ដល់សំណើរ ដើម្បីបើក repo ម្តងទៀតនៅក្នុង container សូមបដិសេធ ដើម្បីប្រើគ្រឿងចក្រ Python ដែលត្រូវបានដំឡើងក្នុងម៉ាស៊ីន។

### ប្រើ Jupyter នៅក្នុងកម្មវិធីរុករក

អ្នកអាចធ្វើការប្រើប្រាស់គម្រោងតាមបរិយាកាស [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ដោយផ្ទាល់នៅក្នុងកម្មវិធីរុករករបស់អ្នក។ Jupyter ត្រៀមខ្លួនដោយច្រើនជម្រើស រួមមាន auto-completion, code highlighting និងផ្សេងៗទៀត។

ដើម្បីចាប់ផ្តើម Jupyter នៅក្នុងមෂ៊ីន, ទៅកាន់ terminal/command line, ចូលទៅថតវគ្គសិក្សា ហើយបញ្ចូល៖

```bash
jupyter notebook
```

ឬ

```bash
jupyterhub
```

វានឹងចាប់ផ្តើម instance Jupyter ហើយ URL សម្រាប់ចូលប្រើវានឹងបង្ហាញនៅក្នុងបង្អួច command line។

មុខពេលអ្នកចូល URL នោះ អ្នកគួរមើលឃើញរ៉ូស៊ីលវគ្គសិក្សា ហើយអាចបញ្ជូនទៅឯកសារ `*.ipynb` ណាមួយបាន។ ឧ. `08-building-search-applications/python/oai-solution.ipynb`។

### រត់ក្នុង container

ជាជម្រើសមួយផ្សេងទៀតសម្រាប់ការតំឡើងគ្រប់យ៉ាងលើកុំព្យូទ័ររបស់អ្នក ឬ Codespace គឺប្រើ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)។ ថត `.devcontainer` ពិសេសនៅក្នុង repo វគ្គអនុញ្ញាតឲ្យ VS Code តំឡើងគម្រោងក្នុង container។ ក្រៅពី Codespaces នេះត្រូវការដំឡើង Docker ហើយ វាដ៏ស្មុគស្មាញមួយ ប៉ុន្តែយើងផ្តល់អនុសាសន៍សម្រាប់អ្នកមានបទពិពណ៌នាធ្វើការជាមួយ container។

មួយក្នុងវិធីល្អបំផុតក្នុងការទុកសោ API keys របស់អ្នកឲ្យមានសុវត្ថិភាពពេលប្រើ GitHub Codespaces គឺដោយប្រើ Codespace Secrets។ សូមតាមដាន [ការគ្រប់គ្រង Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ដើម្បីស្វែងយល់បន្ថែម។


## មេរៀន និងតម្រូវការបច្ចេកទេស

វគ្គសិក្សានេះមានមេរៀន "សិក្សា" ដែលពន្យល់ពីមូលដ្ឋាន Generative AI និងមេរៀន "សាងសង់" ដែលមានឧទាហរណ៍កូដជាក់ស្តែងក្នុងភាសា **Python** និង **TypeScript** នៅកន្លែងដែលអាចធ្វើ។

សម្រាប់មេរៀនកូដយើងប្រើ Azure OpenAI ក្នុង Microsoft Foundry។ អ្នកត្រូវការជាវ Azure និង API key មួយ។ ការចូលប្រើច្រើន - មិនចាំបាច់ដាក់ពាក្យ - ដូច្នេះអ្នកអាច [បង្កើត Microsoft Foundry resource និងចែកចាយម៉ូដែល](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ដើម្បីទទួល endpoint និង key របស់អ្នក។

មេរៀនកូដនីមួយៗក៏មានឯកសារ `README.md` ដែលអ្នកអាចមើលកូដ និងលទ្ធផលដោយមិនចាំបាច់រត់វា។

## ប្រើសេវា Azure OpenAI ជាលើកដំបូង

ប្រសិនបើនេះជាលើកដំបូងអ្នកប្រើសេវា Azure OpenAI សូមអនុវត្តតាមមគ្គុទ្ទេសក៍នេះ អំពីរបៀប [បង្កើត និងចែកចាយ Azure OpenAI Service resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)។

## ប្រើ OpenAI API ជាលើកដំបូង

ប្រសិនបើនេះជាលើកដំបូងអ្នកប្រើ OpenAI API សូមអនុវត្តតាមមគ្គុទ្ទេសក៍អំពីរបៀប [បង្កើត និងប្រើ Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)។

## ស្គាល់អ្នករៀនផ្សេងទៀត

យើងបានបង្កើតឆានែលនៅក្នុង [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) របស់យើង សម្រាប់ជួបគ្នាអ្នករៀនផ្សេងទៀត។ នេះជារបៀបដ៏ល្អសម្រាប់បង្កើតបណ្តាញជាមួយអ្នកចាប់ផ្តើម និយមន័យ ឬសិស្សដែលចង់ជម្រះលក្ខណៈនៅក្នុង Generative AI។

[![ចូលឆានែល discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ក្រុមគម្រោងក៏នឹងមាននៅក្នុង Discord server នេះដើម្បីជួយអ្នករៀនណាមួយ។

## អរិយធម៌ចូលរួម

វគ្គសិក្សានេះគឺជាគ្រឹះបឋមជំនួយទូលំទូលាយ។ ប្រសិនបើអ្នកឃើញកន្លែងដែលអាចធ្វើបានល្អ ឬបញ្ហា សូមបង្កើត [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ឬកត់ត្រា [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)។

ក្រុមគម្រោងនឹងតាមដានការចូលរួមទាំងអស់។ ការ​ចូលរួម​ក្នុង open source គឺជា​របៀប​ពិតជាល្អក្នុង​ការ​សាងសង់​អាជីព​របស់​អ្នក​នៅ Generative AI។

ភាគច្រើនការចូលរួមត្រូវការឱ្យអ្នកយល់ព្រមលើ Contributor License Agreement (CLA) ស្ថិតិថាអ្នកមានសិទ្ធិ និងពិតជាអនុញ្ញាតឲ្យយើងប្រើការចូលរួមរបស់អ្នក។ សម្រាប់ព័ត៌មានលម្អិត សូមទៅកាន់ [គេហទំព័រ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)។

សំខាន់៖ ពេលបកប្រែក្នុង repo នេះ សូមប្រាកដថាអ្នកមិនប្រើប្រាស់ការបកប្រែដោយម៉ាស៊ីន។ យើងនឹងពិនិត្យការបកប្រែក្នុងសហគមន៍ ដូច្នេះសូមចូលរួមជួយបកប្រែគ្រាន់តែភាសាដែលអ្នកមានជំនាញ។


នៅពេលដែលអ្នកដាក់សំណើ pull request មួយ CLA-bot នឹងកំណត់ដោយស្វ័យប្រវត្តិថាតើអ្នកត្រូវផ្តល់ CLA មែនទេ ហើយតុបតែង PR ឲ្យសមរម្យ (ដូចជា ស្លាក ឬយោបល់)។ គ្រាន់តែអនុវត្តតាមការណែនាំដែលបានផ្តល់ឲ្យដោយ bot ។ អ្នកត្រូវធ្វើបែបនេះត្រឹមតែម្ដងប៉ុណ្ណោះសម្រាប់គ្រប់ឃ្លាំងទិន្នន័យដែលប្រើ CLA របស់យើង។

គម្រោងនេះបានអនុម័ត [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)។ សម្រាប់ព័ត៌មានបន្ថែម សូមអាន Code of Conduct FAQ ឬទាក់ទង [Email opencode](opencode@microsoft.com) ប្រសិនបើមានសំណួរឬមតិយោបល់បន្ថែមណាមួយ។

## ចាប់ផ្តើម

ឥឡូវនេះដែលអ្នកបានបញ្ចប់ជំហានដែលចាំបាច់ដើម្បីបញ្ចប់វគ្គនេះ សូមចាប់ផ្តើមដោយស្វែងយល់អំពី [បុព្វបទនៃ Generative AI និង LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->