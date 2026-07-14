# ការតំឡើងក្នុងតំបន់ 🖥️

**ប្រើមេរៀននេះបើអ្នកចូលចិត្តរត់គ្រប់យ៉ាងលើកុំព្យូទ័រយួរដៃផ្ទាល់ខ្លួន។**  
អ្នកមានផ្លូវពីរជម្រើស: **(A) Python ដើម + virtual-env** ឬ **(B) VS Code Dev Container ជាមួយ Docker**។  
ជ្រើសរើសអ្វីដែលមានភាពងាយស្រួល—ទាំងពីរនាំឱ្យទៅកាន់មេរៀនដដែល។

## 1.  តម្រូវការមុន

| ឧបករណ៍           | កំណែ / កំណត់សម្គាល់                                                               |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 ឬលើកើន (ទាញយកពី <https://python.org>)                                        |
| **Git**            | ថ្មីជាងគេ (មានជាមួយ Xcode / Git សម្រាប់ Windows / កម្មវិធីរៀបចំ Linux)               |
| **VS Code**        | ជាជម្រើសប៉ុន្តែសូមណែនាំ <https://code.visualstudio.com>                          |
| **Docker Desktop** | *មានតែ* សម្រាប់ជម្រើស B។ ដំឡើងដោយឥតគិតថ្លៃ: <https://docs.docker.com/desktop/>  |

> 💡 **រំលឹក** – ពិនិត្យឧបករណ៍នៅក្នុងតំបន់បញ្ជា:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  ជម្រើស A – Python ដើម (រហ័សបំផុត)

### ជំហ៊ាន 1 ចម្លង repo នេះ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ជំហ៊ាន 2 បង្កើត និងដំណើរការ virtual environment

```bash
python -m venv .venv          # បង្កើតមួយ
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ ពេលនេះបញ្ជាបញ្ជាជារូបតូច (.venv) មានន័យថាអ្នកនៅខាងក្នុង environment។

### ជំហ៊ាន 3 ដំឡើងការពឹងផ្អែក

```bash
pip install -r requirements.txt
```

ចាញ់ទៅផ្នែកទី 3 នៅលើ [API keys](#3-បញ្ចូល-api-keys-របស់អ្នក)

## 2. ជម្រើស B – VS Code Dev Container (Docker)

យើងបានតំឡើងឃ្លាំងសមាសភាគនេះ និងវគ្គសិក្សាជាមួយ [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ដែលមាន runtime សកល អាចគាំទ្រ Python3, .NET, Node.js និង Java។ ការកំណត់ពាក់ព័ន្ធត្រូវបានកំណត់ក្នុងឯកសារ `devcontainer.json` ដែលមានស្ថិតនៅក្នុងថត `.devcontainer/` នៅជ្រុងឫសរបស់ឃ្លាំងនេះ។

>**ហេតុអ្វីបានជាជ្រើសរើសនេះ?**
>បរិយាកាសដូចCodespaces; គ្មានការស្ទាក់ស្ទើរការពឹងផ្អែក។

### ជំហ៊ាន 0 ដំឡើងរបស់បន្ថែម

Docker Desktop – ផ្ទៀងផ្ទាត់ ```docker --version``` ប្រើបាន។
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers)។

### ជំហ៊ាន 1 បើក repo ក្នុង VS Code

ព័តមាន ▸ បើកថត…  → generative-ai-for-beginners

VS Code ស្គាល់ថាតម្លៃ .devcontainer/ ហើយដាក់ផ្ទាំងសំណូមពរឡើង។

### ជំហ៊ាន 2 បើកម្តងទៀតក្នុង container

ចុច “Reopen in Container”។ Docker នឹងចាប់ផ្តើមបង្កើតរូបភាព (ប្រហែល 3 នាទីដំបូង)។
ពេលដែលបញ្ជាបញ្ជាបង្ហាញ អ្នកនៅក្នុង container ហើយ។

## 2.  ជម្រើស C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) គឺជាឧបករណ៍តំឡើងមានទំងន់ស្រាលសម្រាប់ដំឡើង [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python និងបណ្ណាល័យខ្លះៗ។
Conda ដើមគឺ​ជា​កម្មវិធី​គ្រប់គ្រង​ឯកតា ដែលធ្វើឲ្យងាយស្រួលក្នុងការតំឡើង និងផ្លាស់ប្តូរវិចទ័រផ្សេងៗ Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) និងការទាញយកបណ្ណាល័យ។ វាផ្តល់អត្ថប្រយោជន៍សម្រាប់ដំឡើងកញ្ចប់ដែលវាមិនមានក្នុង `pip` ទេ។

### ជំហ៊ាន 0  ដំឡើង Miniconda

អនុវត្តតាម [មេរៀនតំឡើង MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ដើម្បីចាប់ផ្តើម។

```bash
conda --version
```

### ជំហ៊ាន 1 បង្កើត virtual environment

បង្កើតឯកសារបរិយាកាសថ្មី (*environment.yml*)។ បើអ្នកប្រើ Codespaces អនុវត្តក្នុងថត `.devcontainer` ដូច្នេះវានៅ `.devcontainer/environment.yml`។

### ជំហ៊ាន 2 បញ្ចូលព័ត៌មានទៅឯកសារបរិយាកាសរបស់អ្នក

បន្ថែមខ្សែបញ្ជាពីក្រោមទៅក្នុង `environment.yml` របស់អ្នក

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

### ជំហ៊ាន 3 បង្កើតស្ថានបរិយាកាស Conda របស់អ្នក

ប្រតិបត្តិការបញ្ជាទាំងអស់ខាងក្រោមនៅ​លើ​បន្ទាត់បញ្ជា/terminal របស់អ្នក

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # មគ្គុទេសក៍រង .devcontainer ដំណើរការក្នុងការតំឡើង Codespace ដោយផ្តាច់មុខតែប៉ុណ្ណោះ
conda activate ai4beg
```

មើលទៅ [មេរៀន Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ប្រសិនបើអ្នកប្រទះបញ្ហា។

## 2  ជម្រើស D – Jupyter / Jupyter Lab បែបចាស់ (នៅក្នុងកម្មវិធីរុករក)

> **គេសម្រាប់នរណា?**  
> អ្នកណាដែលចូលចិត្តផ្ទាំងដើម Jupyter ឬចង់រត់សៀវភៅកំណត់ត្រាប្រាកដណាស់ដោយគ្មាន VS Code។  

### ជំហ៊ាន 1  ប្រាកដថារបស់ Jupyter ត្រូវបានដំឡើង

ដើម្បីចាប់ផ្តើម Jupyter នៅលើកុំព្យូទ័រផ្ទាល់ បើក terminal/command line, ទៅថតវគ្គសិក្សា ហើយបញ្ចូល:

```bash
jupyter notebook
```

ឬ

```bash
jupyterhub
```

នេះនឹងចាប់ផ្តើម instance Jupyter ហើយ URL សម្រាប់ចូលប្រើ នឹងបង្ហាញក្នុងបន្ទាត់បញ្ជា។

នៅពេលអ្នកចូល URL នោះ អ្នកគួរតែឃើញរចនាសម្ព័ន្ធវគ្គសិក្សា និងអាចរុករកទៅឯកសារ `*.ipynb` របស់អ្នក, ឧ. `08-building-search-applications/python/oai-solution.ipynb`។

## 3. បញ្ចូល API Keys របស់អ្នក

រក្សាទុកកូនសោ API របស់អ្នកឱ្យមានសុវត្ថិភាពគឺសំខាន់ពេលបង្កើតកម្មវិធីណាមួយ។ យើងណែនាំឲ្យកុំផ្ទុកកូនសោ API ត្បិតក្នុងកូដរបស់អ្នក។ ការបញ្ជូនព័ត៌មានទាំងនោះទៅនៅឃ្លាំងសាធារណៈអាចបណ្តាលឲ្យមានបញ្ហាសុវត្ថិភាព និងថ្លៃដើមមិនចង់បាន ប្រសិនបើមានអ្នកប្រើប្រាស់អាក្រក់។
នេះជាមេរៀនជំហ៊ាន​ដើម្បីបង្កើតឯកសារ `.env` សម្រាប់ Python ហើយបន្ថែមគណនេយ្យ Microsoft Foundry Models របស់អ្នក:

> **ចំណាំ:** GitHub Models (និងអថេរ `GITHUB_TOKEN`) នឹងបញ្ឈប់នៅចុងខែកក្កដា ឆ្នាំ 2026។ មេរៀននេះប្រើ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ជំនួសវិញ។ ចង់ធ្វើការយ៉ាងដាច់ខាត offline? មើល [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)។

1. **ទៅថតគម្រោងរបស់អ្នក**: បើក terminal ឬ command prompt ហើយទៅកាន់ថតឫសគម្រោងដែលអ្នកចង់បង្កើតឯកសារ `.env`។

   ```bash
   cd path/to/your/project
   ```

2. **បង្កើតឯកសារ `.env`**: ប្រើកម្មវិធីកែសម្រួលអត្ថបទដែលអ្នកចូលចិត្ត ដើម្បីបង្កើតឯកសារថ្មីឈ្មោះ `.env`។ បើអ្នកប្រើបន្ទាត់បញ្ជា អ្នកអាចប្រើ `touch` (លើប្រព័ន្ធ Unix) ឬ `echo` (លើ Windows)៖

   ប្រព័ន្ធ Unix៖

   ```bash
   touch .env
   ```

   Windows៖

   ```cmd
   echo . > .env
   ```

3. **កែសម្រួលឯកសារ `.env`**: បើក `.env` ក្នុងកម្មវិធីកែសម្រួលអត្ថបទ (ឧ. VS Code, Notepad++, ឬកម្មវិធីកែសម្រួលផ្សេងទៀត)។ បន្ថែមខ្សែបញ្ជាខាងក្រោមទៅឯកសារ នាំជាមួយប្ដូរដែលអ្នកត្រូវការជាមួយ Microsoft Foundry គម្រោង endpoint និងកូនសោ API:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **រក្សាទុកឯកសារ**: រក្សាទុកបម្លាស់ប្តូរ ហើយបិទកម្មវិធីកែសម្រួល។

5. **ដំឡើង `python-dotenv`**: ប្រសិនបើអ្នកមិនទាន់បានដំឡើង អ្នកត្រូវដំឡើងកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកអថេរក្នុងបរិយាកាសពីឯកសារ `.env` ទៅកម្មវិធី Python របស់អ្នក។ អ្នកអាចដំឡើងដោយប្រើ `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **ផ្ទុកអថេរក្នុងបរិយាកាសនៅក្នុងកូដ Python របស់អ្នក**: នៅក្នុងស្គ្រីប Python របស់អ្នក ប្រើកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកអថេរក្នុងបរិយាកាសពីឯកសារ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # បង្ហោះខ្សែអថេរបរិបទពីឯកសារ .env
   load_dotenv()

   # ចូលប្រើខ្សែអថេរ Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

ហើយនេះជាវិធីសាស្រ្ត! អ្នកបានបង្កើតឯកសារ `.env` ជោគជ័យ បន្ថែមគណនេយ្យ Microsoft Foundry Models របស់អ្នក ហើយផ្ទុកវាទៅក្នុងកម្មវិធី Python របស់អ្នក។

🔐 មិនធ្វើ commit .env ទេ—វាអ្នកបានរំលងនៅក្នុង .gitignore រួចហើយ។
សេចក្តីណែនាំពេញលេញសម្រាប់អ្នកផ្គត់ផ្គង់មាននៅក្នុង [`providers.md`](03-providers.md)។

## 4. តើយើងធ្វើអ្វីបន្ទាប់?

| ខ្ញុំចង់…         | ទៅកាន់…                                                                |
|---------------------|-------------------------------------------------------------------------|
| ចាប់ផ្តើមមេរៀន 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| តំឡើង LLM Provider | [`providers.md`](03-providers.md)                                       |
| ស្គាល់អ្នករៀនផ្សេងទៀត | [ចូលរួម Discord របស់យើង](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. ការដោះស្រាយបញ្ហា

| លក្ខណៈរោគ                              | ដោះស្រាយ                                                        |
|-----------------------------------------|-----------------------------------------------------------------|
| `python មិនត្រូវបានរកឃើញ`             | បន្ថែម Python ទៅ PATH ឬបើកឡើង terminal ម្ដងទៀតបន្ទាប់ពីដំឡើង       |
| `pip` មិនអាចបង្កើតរុក្ខជាតិ (Windows) | `pip install --upgrade pip setuptools wheel` បន្ទាប់មកសាកល្បងម្ដងទៀត។       |
| `ModuleNotFoundError: dotenv`            | បើក `pip install -r requirements.txt` (env មិនទាន់បានដំឡើង)               |
| ការបង្កើត Docker លំបាក *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → បន្ថែមទំហំឌីស។                  |
| VS Code បន្តផ្តល់សំណូមពរឱ្យបើកឡើងម្តងទៀត | អ្នកអាចមានជម្រើសពីរចូលប្រើ; ជ្រើសរើសមួយ (venv **ឬ** container)            |
| កំហុស OpenAI 401 / 429                  | ពិនិត្យ `OPENAI_API_KEY` ខុស / កំណត់កម្រិតសំណើ។                          |
| កំហុសប្រើប្រាស់ Conda                   | ដំឡើងបណ្ណាល័យ Microsoft AI ដោយប្រើ `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->