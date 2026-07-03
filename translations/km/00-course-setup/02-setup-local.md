# ការតំឡើងក្នុងតំបន់ 🖥️

**ប្រើមគ្គុទេសក៍នេះ ប្រសិនបើអ្នកចូលចិត្តរត់គ្រប់យ៉ាងនៅលើកុំព្យូទ័រយួរដៃរបស់អ្នក។**  
អ្នកមានផ្លូវពីរ៖ **(A) Python ដើម + virtual-env** ឬ **(B) VS Code Dev Container ជាមួយ Docker**។  
ជ្រើសរើសអ្វីដែលងាយស្រួលជាង—ពីរយ៉ាងនេះនាំឲ្យបានមេរៀនដដែល។

## 1.  អ្វីដែលត្រូវមានមុន

| ឧបករណ៍            | កំណែ / ចំណាំ                                                                    |
|--------------------|----------------------------------------------------------------------------------|
| **Python**         | 3.10+ (ទាញយកពី <https://python.org>)                                           |
| **Git**            | ថ្មីបំផុត (អាចបានជាមួយ Xcode / Git សម្រាប់ Windows / ប្រព័ន្ធគ្រប់គ្រងបន្ទប់លីនុច)       |
| **VS Code**        | ជាជម្រើស ប៉ុន្តេទាមទារជាក្រិត <https://code.visualstudio.com>                  |
| **Docker Desktop** | *សម្រាប់ជម្រើស B តែប៉ុណ្ណោះ*។ ដំឡើងដោយឥតគិតថ្លៃៈ <https://docs.docker.com/desktop/> |

> 💡 **ជំនួយ** – ពិនិត្យឧបករណ៍នៅក្នុងផ្ទាំងបញ្ជា:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. ជម្រើស A – Python ដើម (លឿនបំផុត)

### ជំហាន 1 ចម្លង repo នេះ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ជំហាន 2 បង្កើត និងបើក virtual environment

```bash
python -m venv .venv          # បង្កើតមួយ
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ បន្ទាត់បញ្ជាគួរតែចាប់ផ្តើមជាមួយ (.venv)—មានន័យថាអ្នកនៅក្នុង env រួចហើយ។

### ជំហាន 3 ដំឡើងការពឹងផ្អែក

```bash
pip install -r requirements.txt
```

រាតត្បាតទៅផ្នែក 3៖ [API keys](#3-បញ្ចូលapi-keys-របស់អ្នក)

## 2. ជម្រើស B – VS Code Dev Container (Docker)

យើងបានដំឡើងទុក repo និងមេរៀននេះជាមួយនឹង [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ដែលមាន runtime សាកសមសម្រាប់ Python3, .NET, Node.js និង Java។ រចនាសម្ព័ន្ធពាក់ព័ន្ធត្រូវបានកំណត់នៅក្នុងឯកសារ `devcontainer.json` ដែលស្ថិតនៅក្នុងថត `.devcontainer/` នៅជាន់ដើមនៃ repo នេះ។

>**ហេតុអ្វីជ្រើសរើសនេះ?**  
>បរិវេណដូចគ្នានឹង Codespaces; មិនមានការបែកបាក់ផ្នែកផ្នែកពឹងផ្អែកពីក្រៅ។

### ជំហាន 0 ដំឡើងបន្ថែម

Docker Desktop – បញ្ជាក់ថា ```docker --version``` ធ្វើការ។  
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers)។

### ជំហាន 1 បើក repo ក្នុង VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code ចាប់ផ្តើមមើលឃើញ .devcontainer/ ហើយបង្ហាញផ្ទាំងណែនាំ។

### ជំហាន 2 បើកឡើងវិញនៅក្នុង container

ចុច “Reopen in Container”។ Docker ក៏កំពុងសង់រូបភាព (≈ 3 នាទីដំបូង)។
ពេលដែលបន្ទាត់បញ្ជាដាក់បង្ហាញ អ្នកកំពុងនៅក្នុង container។

## 2. ជម្រើស C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ជា installer ទម្ងន់ស្រាលសម្រាប់ដំឡើង [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python និងការវេចខ្ចប់ខ្លះៗផងដែរ។  
Conda ផ្ទាល់ខ្លួនគឺជាម៉េដែលគ្រប់គ្រងកញ្ចប់មួយ ដែលធ្វើឲ្យងាយស្រួលក្នុងការតំឡើង និងប្ដូរវាតាក់ Python និងកញ្ចប់ផ្សេងៗ។ វាក៏មានប្រយោជន៍សម្រាប់ដំឡើងកញ្ចប់ដែលមិនអាចទាញយកបានពី `pip`។

### ជំហាន 0 ដំឡើង Miniconda

អនុវត្តតាម [មគ្គុទេសក៍ដំឡើង MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ដើម្បីដំឡើង។

```bash
conda --version
```

### ជំហាន 1 បង្កើត virtual environment

បង្កើតឯកសារបរិស្ថានថ្មី (*environment.yml*)។ ប្រសិនបើអ្នកកំពុងប្រើ Codespaces សូមបង្កើតក្នុងថត `.devcontainer` ដូច្នេះជា `.devcontainer/environment.yml`។

### ជំហាន 2 បំពេញឯកសារបរិស្ថានរបស់អ្នក

បន្ថែមឈុតខាងក្រោមទៅក្នុង `environment.yml`

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

### ជំហាន 3 បង្កើតបរិស្ថាន Conda របស់អ្នក

ដំណើរការបញ្ជាខាងក្រោមនៅក្នុងបន្ទាត់បញ្ជា/terminal របស់អ្នក

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # ផ្លូវរង .devcontainer ដំណើរការត្រឹមតែការតំឡើង Codespace ប៉ុណ្ណោះ
conda activate ai4beg
```

មើលទៅ [មគ្គុទេសក៍ពីបរិស្ថាន Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ប្រសិនបើមានបញ្ហាណាមួយ។

## 2 ជម្រើស D – Jupyter / Jupyter Lab ដើរដោយភ្លាម (នៅក្នុងគេហទំព័រ)

> **សម្រាប់នរណា?**  
> មនុស្សដែលចូលចិត្តផ្ទាំងប្រើប្រាស់ Jupyter ដើម ឬចង់រត់សៀវភៅកំណត់ត្រាដោយគ្មាន VS Code។

### ជំហាន 1 ប្រាកដថា Jupyter ត្រូវបានដំឡើង

ដើម្បីបើក Jupyter ក្នុងកន្លែងភ្លាម សូមទៅផ្ទាំងបញ្ជា/command line, ប្រែប្រួលទៅថតមេរបស់មេរៀន ហើយបញ្ជា៖

```bash
jupyter notebook
```

ឬ

```bash
jupyterhub
```

នេះនឹងបើកឲ្យមានអាគារស្មារតី Jupyter ហើយ URL សម្រាប់ចូលទៅកាន់វានឹងបង្ហាញក្នុងផ្ទាំងបញ្ជា។

ពេលដែលអ្នកចូល URL នោះ អ្នកគួរតែឃើញសេរ៉ូមេរៀន ហើយអាចចូលទៅកាន់ឯកសារ `*.ipynb` តែម្តង។ ឧទាហរណ៍ `08-building-search-applications/python/oai-solution.ipynb`។

## 3. បញ្ចូលAPI Keys របស់អ្នក

ការកាន់កាប់ API keys របស់អ្នកឲ្យមានសុវត្ថិភាព គឺមានសារៈសំខាន់នៅពេលបង្កើតកម្មវិធីគ្រប់ប្រភេទមួយ។ យើងណែនាំកុំផ្ទុក API keys ផ្ទាល់នៅក្នុងកូដ។ ការប្តូរព័ត៌មានទាំងនេះទៅ repo សាធារណៈអាចបណ្តាលឲ្យមានបញ្ហាសុវត្ថិភាព ហើយថ្លៃចំណាយដែលមិនចង់បាន ប្រសិនបើមានអ្នកមិនល្អប្រើប្រាស់។  
នេះជាមគ្គុទេសក៍ជំហានជំហានរបៀបបង្កើតឯកសារ `.env` សម្រាប់ Python និងបន្ថែម `GITHUB_TOKEN`៖

1. **ទៅទៅកាន់ថតគម្រោងរបស់អ្នក**៖ បើក terminal ឬ command prompt ហើយទៅកាន់ថតមេរបស់គម្រោង ដែលអ្នកចង់បង្កើត `.env`។

   ```bash
   cd path/to/your/project
   ```

2. **បង្កើតឯកសារ `.env`**៖ ប្រើកម្មវិធីកែសម្រួលអត្ថបទដែលអ្នកចូលចិត្ត ដើម្បីបង្កើតឯកសារថ្មីឈ្មោះ `.env`។ ប្រសិនបើប្រើ command line អ្នកអាចប្រើ `touch` (លើប្រព័ន្ធ Unix) ឬ `echo` (លើ Windows)៖

   ប្រព័ន្ធ Unix៖

   ```bash
   touch .env
   ```

   Windows៖

   ```cmd
   echo . > .env
   ```

3. **កែប្រែឯកសារ `.env`**៖ បើក `.env` លើកម្មវិធីកែសម្រួលអត្ថបទ (ឧ. VS Code, Notepad++, ឬក៏កែសម្រួលផ្សេងៗ)។ បន្ថែមបន្ទាត់ខាងក្រោមនៅក្នុងឯកសារ ដើម្បីជំនួស `your_github_token_here` ជាមួយ token GitHub ច្បាស់របស់អ្នក៖

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **រក្សាទុកឯកសារ**៖ រក្សាទុកការផ្លាស់ប្តូរ ហើយបិទកម្មវិធីកែសម្រួលអត្ថបទ។

5. **ដំឡើង `python-dotenv`**៖ ប្រសិនបើអ្នកមិនទាន់ដំឡើងទេ អ្នកត្រូវតែដំឡើងកញ្ចប់ `python-dotenv` ដើម្បីបញ្ចូល environment variables ពី `.env` ទៅកម្មវិធី Python របស់អ្នក។ អ្នកអាចដំឡើងវាបានដោយប្រើ `pip`៖

   ```bash
   pip install python-dotenv
   ```

6. **បញ្ចូល environment variables នៅក្នុង script Python របស់អ្នក**៖ នៅក្នុង script Python របស់អ្នក ប្រើកញ្ចប់ `python-dotenv` ដើម្បីបញ្ចូល environment variables ពី `.env`៖

   ```python
   from dotenv import load_dotenv
   import os

   # បង្ហាញអថេរបរិស្ថានពីឯកសារ .env
   load_dotenv()

   # ចូលប្រើអថេរ GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ប៉ុន្តែប៉ុណ្ណោះ! អ្នកបានបង្កើត `.env` ដោយជោគជ័យ បន្ថែម GitHub token ហើយបញ្ចូលវាទៅកម្មវិធី Python រួចហើយ។

🔐 មិនចាំបាច់ commit .env—វាបានដាក់នៅក្នុង .gitignore រួចហើយ។  
សេចក្តីណែនាំពេញលេញសម្រាប់អ្នកផ្គត់ផ្គង់ស្ថិតក្នុង [`providers.md`](03-providers.md)។

## 4. ត្រូវធ្វើយ៉ាងដូចម្តេចបន្ទាប់?

| អ្វីដែលខ្ញុំចង់ធ្វើ… | ទៅកាន់…                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| ចាប់ផ្តើមមេរៀនទី 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| តំឡើងអ្នកផ្គត់ផ្គង់ LLM | [`providers.md`](03-providers.md)                                       |
| ជួបអ្នករៀនផ្សេងទៀត  | [ចូលរួម Discord របស់យើង](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. ដោះស្រាយបញ្ហា

| របាំងសញ្ញា                             | ដំណោះស្រាយ                                                             |
|-------------------------------------|-----------------------------------------------------------------------|
| `python not found`                  | បន្ថែម Python ទៅ PATH ឬបើកផ្ទាំងបញ្ជាថ្មីបន្ទាប់ពីដំឡើង            |
| `pip` មិនអាចសង់ wheels បាន (Windows) | `pip install --upgrade pip setuptools wheel` បន្ទាប់ម្តងសាកល្បងម្ដងទៀត។        |
| `ModuleNotFoundError: dotenv`       | ប្រើ `pip install -r requirements.txt` (env មិនបានដំឡើងទេ)              |
| ការសង់ Docker បរាជ័យ *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → បន្ថែមទំហំ hard drive។          |
| VS Code ផ្តល់ជូនបន្តផ្តើមបើកឡើងវិញ | អ្នកប្រហែលជាមាន Option ទាំងពីរដំណើរការ; ជ្រើស Option មួយ (venv **ឬ** container) |
| ផ្សាយ OpenAI 401 / 429 errors       | ពិនិត្យតម្លៃ `OPENAI_API_KEY` / កម្រិតសំណើកំពូល។                           |
| បញ្ហាក្នុងការប្រើ Conda              | ដំឡើងបណ្ណាល័យ Microsoft AI ដោយប្រើ `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានយកចិត្តទុកដាក់ទៅជាមូលដ្ឋានយុត្តិធម៌។ សម្រាប់ព័ត៌មានសំខាន់ៗ ខ្មែរ្ជម៉្យើងណែនាំឲ្យមានការបកប្រែដោយមនុស្សជំនាញជាវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសរបស់បកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->