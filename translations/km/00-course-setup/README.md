# ការចាប់ផ្តើមជាមួយវគ្គនេះ

យើងរីករាយខ្លាំងណាស់ដែលអ្នកបានចាប់ផ្តើមវគ្គនេះ និងមើលថាតើអ្នកទទួលបានការបំផុសគំនិតអ្វីខ្លះដើម្បីបង្កើតជាមួយ Generative AI!

ដើម្បីធានាថាអ្នកអាចសម្រេចបានជោគជ័យ ទំព័រនេះបង្ហាញពីជំហានផ្ទៀងផ្ទាត់ ការទាមទារបច្ចេកទេស និងចំពោះកន្លែងដែលអាចទទួលបានជំនួយបើត្រូវការ។

## ជំហានផ្ទៀងផ្ទាត់

ដើម្បីចាប់ផ្តើមរៀនវគ្គនេះ អ្នកត្រូវតែបញ្ចប់ជំហានខាងក្រោម។

### 1. បំបែក Repo នេះ

[បំបែក repo ទាំងមូលនេះ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ទៅក្នុងគណនី GitHub របស់អ្នកផ្ទាល់ ដើម្បីអាចកែប្រែកូដណាមួយ និងបញ្ចប់បញ្ហាប្រកួត។ អ្នកអាច [ផ្ដល់ចំណាប់អារម្មណ៍ (🌟) លើ repo នេះ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ដើម្បីស្វែងរកវា និង repo ទាក់ទងបានងាយស្រួលជាងមុន។

### 2. បង្កើត codespace

ដើម្បីជៀសវាងបញ្ហាការពឹងផ្អែកណាមួយនៅពេលរត់កូដ យើងណែនាំឱ្យរត់វគ្គនេះនៅក្នុង [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)។

នៅក្នុង fork របស់អ្នក៖ **Code -> Codespaces -> New on main**

![កម្មវិធីនេះបង្ហាញប៊ូតុងបង្កើត codespace](../../../translated_images/km/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 បន្ថែមសម្ងាត់មួយ

1. ⚙️ រូបតំណាក់ -> Command Pallete-> Codespaces : Manage user secret -> បន្ថែមសម្ងាត់ថ្មី។
2. ឈ្មោះ OPENAI_API_KEY, បញ្ជូលកូនសោរបស់អ្នក, រក្សាទុក។

### 3. តើអ្វីទៅជាជំហានបន្ទាប់?

| ខ្ញុំចង់...        | ទៅកាន់...                                                             |
|---------------------|-------------------------------------------------------------------------|
| ចាប់ផ្តើមមេរៀនទី 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ធ្វើការវិលតាមoffline  | [`setup-local.md`](02-setup-local.md)                                   |
| កំណត់អ្នកផ្តល់ LLM   | [`providers.md`](03-providers.md)                                       |
| ស្គាល់អ្នករៀនផ្សេង | [ចូលរួម Discord របស់យើង](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ការដោះស្រាយបញ្ហា


| រោគសញ្ញា                                   | ដោះស្រាយ                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| ការបង្កើត container ឈរជាង ១០ នាទី     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal មិនភ្ជាប់; ចុច **+** ➜ *bash*                    |
| `401 Unauthorized` ពី OpenAI              | `OPENAI_API_KEY` មិនត្រឹមត្រូវ / ហួសកំណត់                     |
| VS Code បង្ហាញ “Dev container mounting…” | ផ្ទេរទំព័រទៅកាន់Browser ថ្មី—Codespaces ពេលខ្លះបាត់ការតភ្ជាប់|
| មើលមិនឃើញ kernel នៅក្នុង Notebook    | មេនុយ Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   រដ្ឋប្រព័ន្ធ Unix:

   ```bash
   touch .env
   ```

   រដ្ឋប្រព័ន្ធ Windows:

   ```cmd
   echo . > .env
   ```

3. **កែសម្រួលក файл `.env`**: បើកក файл `.env` ជាមួយកម្មវិធីកែសម្រួលអត្ថបទមួយ (ឧ. VS Code, Notepad++, ឬកម្មវិធីកែសម្រួលផ្សេងទៀត)។ បន្ថែមបន្ទាត់ខាងក្រោមចូលក្នុងក файл ដោយប្តូរពាក្យ `your_github_token_here` ជាមួយកូនសោ GitHub របស់អ្នក៖

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **រក្សាទុកក файл**: រក្សាទុកការផ្លាស់ប្តូរ ហើយបិទកម្មវិធីកែសម្រួលអត្ថបទ។

5. **ដំឡើង `python-dotenv`**: ប្រសិនបើអ្នកមិនទាន់បានដំឡើង `python-dotenv` កញ្ចប់នេះទេ អ្នកត្រូវតែដំឡើងសម្រាប់បញ្ចូលអថេរបរិស្ថានពីក файл `.env` ទៅក្នុងកម្មវិធី Python របស់អ្នក។ អ្នកអាចដំឡើងវា ដោយប្រើ `pip`៖

   ```bash
   pip install python-dotenv
   ```

6. **ផ្ទុកអថេរបរិស្ថានក្នុងឯកសារ Python របស់អ្នក**: នៅក្នុងស្គ្រីប Python អ្នកប្រើកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកអថេរបរិស្ថានពីក файл `.env` ដូចខាងក្រោម៖

   ```python
   from dotenv import load_dotenv
   import os

   # ផ្ទុកអថេរបរិស្ថានពីឯកសារ .env
   load_dotenv()

   # ចូលដំណើរការ​អថេរ GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ហើយនោះទៀត! អ្នកបានបង្កើតក файл `.env` បានជោគជ័យ បន្ថែមកូនសោ GitHub ហើយផ្ទុកវាទៅក្នុងកម្មវិធី Python របស់អ្នក។

## របៀបរត់ក្នុងកុំព្យូទ័រផ្ទាល់ខ្លួន

ដើម្បីរត់កូដនេះក្នុងកុំព្យូទ័រផ្ទាល់ខ្លួន អ្នកត្រូវតែមានជំនាន់មួយនៃ [Python ដំឡើងរួច](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)។

បន្ទាប់មក ដើម្បីប្រើ repository នេះ អ្នកត្រូវតែ clone វា៖

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ពេលដែលអ្នកបានទាញយកមកពេញលេញ អ្នកអាចចាប់ផ្តើមបាន!

## ជំហានជាជម្រើស

### ដំឡើង Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) គឺជាកម្មវិធីតំឡើងទន់ខ្សោយសម្រាប់ដំឡើង [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python និងបញ្ចីកញ្ចប់មួយចំនួន។
Conda ផ្ទាល់ជាអ្នកគ្រប់គ្រងកញ្ចប់ដែលធ្វើឱ្យការកំណត់ និងប្ដូរវិភាគ Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ស្រួលឡើង។ វាក៏មានប្រយោជន៍សម្រាប់ដំឡើងកញ្ចប់ដែលមិនអាចទាញយកដោយ `pip` បាន។

អ្នកអាចអនុវត្តតាម [មគ្គុទេសក៍ដំឡើង MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) សម្រាប់តំឡើងវា។

បន្ទាប់ពីបានដំឡើង Miniconda អ្នកសូម clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (បើអ្នកមិនទាន់បានធ្វើ)។

បន្ទាប់មក អ្នកត្រូវបង្កើត virtual environment មួយ។ ដើម្បីធ្វើនេះជាមួយ Conda សូមបង្កើតក файл សម្រាប់ environment ចំណាំ (_environment.yml_)។ បើអ្នកប្រើ Codespaces សូមបង្កើតក្នុងថត `.devcontainer` ដូច្នេះក файл ត្រូវជា `.devcontainer/environment.yml`។

សូមបំពេញក файл environment របស់អ្នកជាមួយស្នាដៃខាងក្រោម៖

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

បើអ្នកឃើញកំហុសបំពេញកូដ conda អ្នកអាចដំឡើងក្រុមបណ្ណាល័យ Microsoft AI Library ដោយដំណើរការបញ្ជារ​ដូចខាងក្រោមនៅក្នុង terminal ។

```
conda install -c microsoft azure-ai-ml
```

ក файл environment កំណត់បរិមាណ dependencies ដែលត្រូវការ។ `<environment-name>` ជាឈ្មោះដែលអ្នកចង់ប្រើសម្រាប់ Conda environment របស់អ្នក និង `<python-version>` គឺជាជំនាន់ Python ដែលអ្នកចង់ដំណើរការ ឧ. `3` ជាជំនាន់ Python ដែលថ្មីបំផុត។

បន្ទាប់ពីធ្វើរួច អ្នកអាចបង្កើត Conda environment របស់អ្នក ដោយដំណើរការបញ្ជារខាងក្រោមនៅក្នុង command line/terminal របស់អ្នក៖

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ច្រកផ្លូវរង .devcontainer ដំណើរការដល់ការដំឡើង Codespace ផ្ទាល់តែប៉ុណ្ណោះ
conda activate ai4beg
```

សូមយោងទៅកាន់ [មគ្គុទេសក៍ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ប្រសិនបើអ្នកបញ្ហាណាមួយ។

### ការប្រើ Visual Studio Code ជាមួយជំនួយ Python support extension

យើងណែនាំឱ្យប្រើកម្មវិធីកែសម្រួល [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ជាមួយ [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) សម្រាប់វគ្គនេះ។ ទោះជាយ៉ាងណា វាជាការណែនាំមួយ មិនមែនជាការទាមទារ។

> **ចំណាំ**: ដោយបើក repo វគ្គនៅក្នុង VS Code អ្នកអាចជ្រើសរើសតំឡើងគម្រោងនៅក្នុង container។ នេះដោយសារតែថត [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ពិសេសដែលមាននៅក្នុង repo វគ្គ។ នេះនឹងពន្យល់បន្ថែមនៅក្រោយ។

> **ចំណាំ**: ពេលដែលអ្នក clone និងបើកថតក្នុង VS Code វានឹងជូនដំណឹងសម្រាប់តំឡើង Python support extension ដោយស្វ័យប្រវត្តិ។

> **ចំណាំ**: ប្រសិនបើ VS Code ស្នើឱ្យបើក repo នៅក្នុង container សូមបដិសេធដើម្បីប្រើ Python ដែលបានដំឡើងក្នុងកុំព្យូទ័រម្ដងទៀត។

### ប្រើ Jupyter នៅក្នុង Browser

អ្នកអាចធ្វើការលើគម្រោងនេះដោយប្រើបរិយាកាស [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) នៅក្នុង Browser របស់អ្នកផងដែរ។ ទាំង Jupyter គ្រប់ប្រភេទ និង [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ផ្តល់បរិយាកាសអភិវឌ្ឍន៍ល្អ ដោយមានលក្ខណៈពិសេសដូចជា auto-completion ការបំភ្លឺកូដ។

ដើម្បីចាប់ផ្តើម Jupyter នៅក្នុងកុំព្យូទ័រផ្ទាល់ ខលទៅ terminal/command line ចុចទៅក្នុងថតវគ្គ ហើយបញ្ជារបញ្ជាខាងក្រោម៖

```bash
jupyter notebook
```

ឬ

```bash
jupyterhub
```

នេះនឹងចាប់ផ្តើម Jupyter instance ហើយ URL សម្រាប់ចូលប្រើ នឹងត្រូវបង្ហាញក្នុង command line។

ពេលដែលអ្នកចូលទៅ URL នេះ អ្នកគួរតែឃើញសេចក្តីសង្ខេបវគ្គ និងអាចរំកិលទៅកាន់ឯកសារ `*.ipynb` មួយណាមួយបាន។ ឧ. `08-building-search-applications/python/oai-solution.ipynb`។

### រត់នៅក្នុង container

មួយជំនួសដើម្បីកំណត់របស់របរទាំងអស់នៅលើកុំព្យូទ័ររបស់អ្នក ឬ Codespace គឺប្រើ [container](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)។ថត `.devcontainer` ពិសេសនៅក្នុង repo វគ្គ ធ្វើឱ្យ VS Code អាចបង្កើតគម្រោងនៅក្នុង container បាន។ នៅខាងក្រៅ Codespaces វាចាំបាច់តំឡើង Docker ហើយ វាពិតជាលំបាកមួយចំនួន ដូច្នេះយើងណែនាំសម្រាប់អ្នកដែលមានបទពិសោធន៍ក្នុងការ ប្រើ container ប៉ុណ្ណោះ។

វិធីល្អបំផុតក្នុងការការពារអាសយដ្ឋាន API key របស់អ្នកពេលប្រើ GitHub Codespaces គឺដោយប្រើ Codespace Secrets។ សូមអនុវត្តតាម [មគ្គុទេសក៍គ្រប់គ្រងសម្ងាត់ Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ដើម្បីស្វែងយល់បន្ថែម។

## មេរៀន និង ការទាមទារបច្ចេកទេស

វគ្គនេះមានមេរៀន គំនិតចំនួន 6 និងមេរៀនកូដចំនួន 6។

សម្រាប់មេរៀនកូដ យើងប្រើសេវា Azure OpenAI។ អ្នកត្រូវការចូលប្រើសេវា Azure OpenAI និងកូនសោ API មួយដើម្បីរត់កូដនេះ។ អ្នកអាចដាក់ពាក្យស្នើសុំដើម្បីទទួលការចូលប្រើដោយ [បញ្ចប់ការដាក់ពាក្យនេះ](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)។

ពេលអ្នករង់ចាំសំណើររបស់អ្នក ត្រង់មេរៀនកូដនិមួយៗក៏មានសរសេរ README.md ដែលអ្នកអាចមើលកូដ និងលទ្ធផលបាន។

## ប្រើសេវា Azure OpenAI ជាលើកដំបូង

បើនេះជាលើកដំបូងដែលអ្នកប្រើសេវា Azure OpenAI សូមអនុវត្តតាមមគ្គុទេសក៍នេះដើម្បី [បង្កើត និងចេញផ្សាយធនធាន Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)។

## ប្រើ OpenAI API ជាលើកដំបូង

បើនេះជាលើកដំបូងដែលអ្នកប្រើ OpenAI API សូមអនុវត្តតាមមគ្គុទេសក៍ [បង្កើត និងប្រើ Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)។

## ស្គាល់អ្នករៀនផ្សេងទៀត

យើងបានបង្កើតប៉ុស្តិ៍ក្នុងម៉ាស៊ីនមេ Discord ផ្លូវការរបស់យើង [សហគមន៍ AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) សម្រាប់ជួបអ្នករៀនផ្សេងទៀត។ វាជាវិធីល្អក្នុងការតភ្ជាប់ជាមួយអ្នកសហគ្រិន អ្នកសាងសង់ សិស្ស និងគ្រប់គ្នាដែលចង់បង្កើនជំនាញក្នុង Generative AI។

[![ចូលរួមប៉ុស្តិ៍ discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ក្រុមគម្រោងនឹងមានប្រតិបត្តិការលើម៉ាស៊ីនមេ Discord នេះ ដើម្បីជួយអ្នករៀន។

## ចូលរួម

វគ្គនេះជាគម្រោងកម្មវិធីបើកចំហ។ ប្រសិនបើអ្នកឃើញកន្លែងដែលអាចកែលម្អ ឬបញ្ហា សូមបង្កើត [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ឬដាក់កំណត់បញ្ហា [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)។

ក្រុមគម្រោងនឹងតាមដានការចូលរួមទាំងអស់។ ការចូលរួមក្នុងឯកសារបើកចំហជាវិធីដ៏អស្ចារ្យក្នុងការបង្កើតអាជីពរបស់អ្នកក្នុង Generative AI។

ការចូលរួមភាគច្រើនតម្រូវឱ្យអ្នកយល់ព្រមលើ Contributor License Agreement (CLA) ដែលបញ្ជាក់ថាអ្នកមានសិទ្ធិ និងពិតជាប្រើសិទ្ធិដើម្បីផ្តល់សិទ្ធិឲ្យយើងប្រើប្រាស់ការចូលរួមរបស់អ្នក។ សម្រាប់ព័ត៌មានលម្អិត សូមចូលទៅ [គេហទំព័រ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)។

សំខាន់៖ ពេលបកប្រែអត្ថបទនៅក្នុង repo នេះ សូមធានាថាអ្នកមិនប្រើការបកប្រែដោយម៉ាស៊ីនឡើយ។ យើងនឹងពិនិត្យការបកប្រែតាមរយៈសហគមន៍ ដូច្នេះសូមចូលរួមបកប្រែតែភាសាដែលអ្នកស្គាល់ពេញលេញ។

ពេលអ្នកដាក់សំណើ pull request តែម្ដង អ្នកប្រភេទ CLA-bot នឹងកំណត់ថាអ្នកត្រូវផ្តល់ CLA ឬអត់ ហើយបន្សំ PR តាមបែបគ្រាប់ (ឧ. ស្លាក ឬមតិ)។ ត្រឹមត្រូវអនុវត្តតាមសេចក្តីណែនាំពី bot។ អ្នកត្រូវធ្វើនេះតែម្ដងប៉ុណ្ណោះសម្រាប់គម្រោងទាំងមូលដែលប្រើ CLA របស់យើង។

គម្រោងនេះបានទទួលយក [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ។ សម្រាប់ព័ត៌មានបន្ថែម សូមអានព័ត៌មាន FAQ Code of Conduct ឬទាក់ទង [អ៊ីមែល opencode](opencode@microsoft.com) សម្រាប់សំណួរឬមតិយោបល់បន្ថែម។

## ចាប់ផ្តើមទៅ!
ឥឡូវនេះដែលអ្នកបានបញ្ចប់ជំហានចាំបាច់ដើម្បីបញ្ចប់វគ្គសិក្សានេះហើយ យើងចាប់ផ្ដើមដោយទទួលបាន [បទបង្ហាញអំពី Generative AI និង LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការ​ព្រមាន**៖  
ឯកសារ​នេះ​ត្រូវបាន​ប្រែសម្រួល​ដោយ​ប្រើសេវា​ប្រែសម្រួល AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេល​ដែល​យើងខំប្រឹងប្រែង​ដើម្បី​ការពារ​ការពិតត្រឹមត្រូវ សូម​អោយស្គាល់​ថា​ការ​ប្រែសម្រួល​ដោយ​ស្វ័យ​ប្រវត្តិ​អាចមាន​កំហុស ឬ​ភាពមិន​ត្រឹមត្រូវ។ ឯកសារ​ដើម​នៅ​ភាសាម្ចាស់​កំណត់គួរតែ​ត្រូវ​បាន​ពិចារណាជាដើមទុន​ដែល​មាន​សុពលភាព។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ ការប្រែសម្រួលដោយមនុស្ស​ជំនាញ​ត្រូវបានផ្តល់អនុសាសន៍។ យើង​មិនទទួលខុសត្រូវចំពោះ​ការ​យល់ច្រឡំ ឬ​ការ​អនុវត្តបម្រុង​មិនត្រឹមត្រូវ ដែលកើតឡើង​ពីការប្រើប្រាស់​ការ​ប្រែសម្រួល​នេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->