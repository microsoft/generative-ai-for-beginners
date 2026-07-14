# ការចាប់ផ្តើមជាមួយវគ្គសិក្សានេះ

យើងមានការរំភើបមួយសម្រាប់អ្នកក្នុងការចាប់ផ្តើមវគ្គសិក្សានេះ និងមើលថាតើអ្វីដែលអ្នកទទួលបានជាការប្រឹងប្រែងក្នុងការកសាងជាមួយ AI ស្នាដៃបង្កើត!

ដើម្បីធានា ជោគជ័យរបស់អ្នក តំណកនេះបង្ហាញពីជំហានការតម្លើង លក្ខខណ្ឌបច្ចេកទេស និងកន្លែងយកជំនួយ ប្រសិនបើត្រូវការ។

## ជំហានតម្លើង

ដើម្បីចាប់ផ្តើមយកវគ្គសិក្សានេះ អ្នកត្រូវបញ្ចប់ជំហានខាងក្រោម។

### 1. រំលាយ Repo នេះ

[រំលាយមួយ Repo ទាំងមូលនេះ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ទៅក្នុងគណនី GitHub ផ្ទាល់របស់អ្នក ដើម្បីអាចផ្លាស់ប្តូរកូដណាមួយ និងបញ្ចប់បញ្ហាត្រូវបានផ្ដល់ជូន។ អ្នកក៏អាច [ផ្ដល់ផ្កាយ (🌟) Repo នេះ](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ដើម្បីរកវា និង Repo ដែលពាក់ព័ន្ធបានងាយស្រួល។

### 2. បង្កើត codespace

ដើម្បីការពារការជួបប្រទៈបញ្ហាឧបសគ្គអាស្រ័យភាពពេលដំណើរការកូដ យើងណែនាំឲ្យដំណើរការវគ្គសិក្សានេះនៅក្នុង [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)។

នៅក្នុង fork របស់អ្នក: **Code -> Codespaces -> New on main**

![ប្រអប់សន្ទនា ដែលបង្ហាញប៊ូតុងសម្រាប់បង្កើត codespace](../../../translated_images/km/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 បន្ថែមអ្វីសម្ងាត់មួយ

1. ⚙️ រូបតំណាងកង់ -> Command Pallete-> Codespaces : គ្រប់គ្រងអ្វីសម្ងាត់របស់អ្នកប្រើ -> បន្ថែមអ្វីសម្ងាត់ថ្មីមួយ។
2. ឈ្មោះ OPENAI_API_KEY, បញ្ចូល key របស់អ្នក ហើយរក្សាទុក។

### 3. តើអ្វីជាជំហានបន្ទាប់?

| ខ្ញុំចង់…         | ទៅកាន់…                                                             |
|---------------------|-------------------------------------------------------------------------|
| អនុវត្តមេរៀនទី 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ធ្វើការងារបិទភ្ជាប់     | [`setup-local.md`](02-setup-local.md)                                   |
| តម្លើងអ្នកផ្គត់ផ្គង់ LLM | [`providers.md`](03-providers.md)                                        |
| ជួបអ្នករៀនផ្សេងទៀត | [ចូលរួមក្នុង Discord របស់យើង](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ការដោះស្រាយបញ្ហា


| ប្រតិកម្ម                         | ដោះស្រាយ                                                      |
|-----------------------------------|-----------------------------------------------------------------|
| ការសាងសង់កុងតឺន័រ ឈប់ជាង 10 នាទី | **Codespaces ➜ “សាងសង់កុងតឺន័រឡើងវិញ”**                            |
| `python: command not found`      | Terminal មិនភ្ជាប់; ចុច **+** ➜ *bash*                              |
| `401 Unauthorized` ពី OpenAI     | key `OPENAI_API_KEY` មិនត្រឹមត្រូវ / ផុតកំណត់                                |
| VS Code បង្ហាញា “Dev container mounting…” | បន្ទាត់ម៉ឺនុយឡើងវិញដើម្បីភ្ជាប់ - Codespaces ពេលខ្លះបាត់ការតភ្ជាប់                     |
| គ្មាន Notebook kernel              | មឺនុយ Notebook ➜ **Kernel ▸ ជ្រើស Kernel ▸ Python 3**            |

   ប្រព័ន្ធ Unix:

   ```bash
   touch .env
   ```

   ប្រព័ន្ធ Windows:

   ```cmd
   echo . > .env
   ```

3. **កែប្រែឯកសារ `.env`**: បើកឯកសារ `.env` ក្នុងកម្មវិធីកែសម្រួលអត្ថបទ (ដូចជា VS Code, Notepad++, ឬកម្មវិធីកែសម្រួលផ្សេងទៀត) បន្ថែមបន្ទាត់ដូចខាងក្រោមទៅក្នុងឯកសារ ដោយជំនួសតម្លៃកន្លែងកំណត់ជាមួយចំណុចបញ្ចូល Microsoft Foundry Models របស់អ្នក និង key (មើល [`providers.md`](03-providers.md) សម្រាប់វិធីទទួលយកបណ្តាញនេះ):

   > **សំគាល់:** GitHub Models (និងអថេរ `GITHUB_TOKEN` របស់វា) នឹងបញ្ឈប់នៅចុងខែ ខែកក្កដា ឆ្នាំ ២០២៦។ សូមប្រើ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ជំនួស។

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **រក្សាទុកឯកសារ**: រក្សាទុកការផ្លាស់ប្តូរ ហើយបិទកម្មវិធីកែសម្រួលអត្ថបទ។

5. **ដំឡើង `python-dotenv`**: ប្រសិនបើអ្នកមិនទាន់មាន អ្នកត្រូវតែដំឡើងកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកអថេរពិសេសពីឯកសារ `.env` ចូលទៅក្នុងកម្មវិធី Python របស់អ្នក។ អ្នកអាចដំឡើងដោយប្រើ `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **ផ្ទុកអថេរពិសេសបរិស្ថាននៅក្នុង Script Python របស់អ្នក**: នៅក្នុង script Python របស់អ្នក ប្រើកញ្ចប់ `python-dotenv` ដើម្បីផ្ទុកអថេរពិសេសពីឯកសារ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # បញ្ចូលអថិជនបរិស្ថានពីឯកសារ .env
   load_dotenv()

   # ចូលប្រើអថិជនបរិស្ថានម៉ូដែល Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

ប៉ុន្មាននេះហើយ! អ្នកបានបង្កើតឯកសារ `.env` ជោគជ័យ បន្ថែមសិទ្ធិ Microsoft Foundry Models របស់អ្នក ហើយបានផ្ទុកវាចូលទៅក្នុងកម្មវិធី Python របស់អ្នក។

## របៀបដំណើរការនៅលើកុំព្យូទ័រផ្ទាល់ខ្លួនរបស់អ្នក

ដើម្បីដំណើរការកូដនៅលើកុំព្យូទ័រផ្ទាល់ខ្លួន ត្រូវការតំឡើង [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) តែមួយវង់។

បន្ទាប់មកដើម្បីប្រើ repository អ្នកត្រូវតែ clone វា:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

បន្ទាប់ពីអ្នកមានគ្រប់យ៉ាងរួច អ្នកអាចចាប់ផ្តើមបានហើយ!

## ជំហានជាជម្រើស

### ដំឡើង Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) គឺជាតំឡើងខ្សែល្មូនសម្រាប់ដំឡើង [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, និងកញ្ចប់មួយចំនួន។
Conda មានតួនាទីជាអ្នកគ្រប់គ្រងកញ្ចប់ ដែលធ្វើឲ្យងាយស្រួលក្នុងការតំឡើង និងប្ដូរវគ្គផ្ទាល់ Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) និងកញ្ចប់។ វាក៏មានប្រយោជន៍ក្នុងការដំឡើងកញ្ចប់ដែលមិនអាចបើកដោយ `pip` បាន។

អ្នកអាចអនុវត្តតាម [មគ្គុទេសក៍ដំឡើង MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ដើម្បីដំឡើងវា។

បន្ទាប់ពីដំឡើង Miniconda អ្នកត្រូវតែ clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ប្រសិនបើអ្នកមិនទាន់បានធ្វើ)។

បន្ទាប់មក អ្នកត្រូវបង្កើតបរិស្ថាន virtual ។ ដើម្បីធ្វើនេះជាមួយ Conda សូមបង្កើតតំបន់បរិស្ថានថ្មីមួយឈ្មោះឯកសារ (_environment.yml_)។ ប្រសិនបើអ្នកប្រើ Codespaces អ្នកត្រូវបង្កើតវានៅក្នុងថត `.devcontainer` ដូច្នេះជា `.devcontainer/environment.yml`។

សូមបំពេញឯកសារបរិស្ថានរបស់អ្នកជាមួយកូដខាងក្រោមៈ

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

ប្រសិនបើអ្នកមានបញ្ហា អ្នកអាចដំឡើងបណ្ណាល័យ Microsoft AI libraries ដោយប្រើពាក្យបញ្ជាទាំងខាងក្រោមនៅក្នុង terminal។

```
conda install -c microsoft azure-ai-ml
```

ឯកសារបរិស្ថាននេះបញ្ជាក់អំពីអាស្រ័យភាពដែលយើងត្រូវការ។ `<environment-name>` មានន័យថាឈ្មោះដែលអ្នកចង់ប្រើសម្រាប់បរិស្ថាន Conda របស់អ្នក ហើយ `<python-version>` គឺជាកំណែ Python ដែលអ្នកចង់ប្រើ ឧទាហរណ៍ `3` ជាកំណែធំនៃ Python នាពេលបច្ចុប្បន្ន។

បន្ទាប់ពីបានរួច អ្នកអាចបង្កើតបរិស្ថាន Conda របស់អ្នកដោយដំណើរការពាក្យបញ្ជាខាងក្រោមនៅលើ command line/terminal របស់អ្នក

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ផ្លូវរង .devcontainer ប្រើសម្រាប់ការកំណត់ Codespace តែប៉ុណ្ណោះ
conda activate ai4beg
```

សូមយោងទៅកាន់ [មគ្គុទេសក៍បរិស្ថាន Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ប្រសិនបើអ្នកមានបញ្ហាណាមួយ។

### ការប្រើប្រាស់ Visual Studio Code ជាមួយផ្នែកពង្រឹង Python support

យើងណែនាំឲ្យប្រើកម្មវិធីកែសម្រួល [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ជាគ្រឿងឧបករណ៍ បូករួមជាមួយ [ ផ្នែកពង្រឹង Python support](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) សម្រាប់វគ្គសិក្សានេះ។ ទោះយ៉ាងណា វាគ្រាន់តែជាការណែនាំ មិនមែនជាការទាមទារត្រឹមត្រូវទេ។

> **សំគាល់**: ដោយបើក repository វគ្គសិក្សានៅក្នុង VS Code អ្នកមានជម្រើសក្នុងការតម្លើងគម្រោងក្នុងនាម container។ នេះដោយសារតែថត [.devcontainer](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ពិសេសដែលមាននៅក្នុង repository វគ្គសិក្សា។ នឹងពន្យល់បន្ថែមនៅក្រោយ។

> **សំគាល់**: នៅពេលអ្នក clone និងបើកថតនៅក្នុង VS Code វានឹងផ្តល់អនុសាសន៍ឲ្យអ្នកតំឡើងផ្នែកពង្រឹង Python support ទៅជាមួយ។

> **សំគាល់**: ប្រសិនបើ VS Code ផ្តល់អនុសាសន៍ឲ្យបើក repo វាគ្មាន container សូមបដិសេធសំណើនេះ ដើម្បីប្រើកំណែ Python ដែលបានដំឡើងនៅក្នុងកុំព្យូទ័ររបស់អ្នក។

### ការប្រើប្រាស់ Jupyter នៅក្នុងកម្មវិធីរុករក

អ្នកអាចធ្វើការងារលើគម្រោងដោយប្រើបរិស្ថាន [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) នៅក្នុងកម្មវិធីរុករករបស់អ្នកផ្ទាល់។ ការប្រើប្រាស់ Jupyter យ៉ាងសម្បូរបែប និង [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ផ្តល់បរិស្ថានអភិវឌ្ឍមានភាពរលូនជាមួយលក្ខណៈពិសេសដូចជាការបំពេញស្វ័យប្រវត្តិ ការកំណត់ពណ៌កូដ។

ដើម្បីចាប់ផ្តើម Jupyter នៅលើកុំព្យូទ័រផ្ទាល់ ជាទីសំគាល់ទៅ terminal/command line គ្រាន់ដំណើរការឥឡូវនេះ នៅក្នុងថតវគ្គសិក្សា៖

```bash
jupyter notebook
```

ឬ

```bash
jupyterhub
```

នេះនឹងចាប់ផ្តើមកម្មវិធី Jupyter ហើយ URL សម្រាប់ចូលប្រើវានឹងបង្ហាញនៅក្នុងបង្អួច command line។

ពេលអ្នកចូលដល់ URL អ្នកនឹងឃើញផែនការវគ្គសិក្សា និងអាចរុករកទៅឯកសារ `*.ipynb` មួយណាមួយ។ ឧទាហរណ៍ `08-building-search-applications/python/oai-solution.ipynb`។

### ការប្រើប្រាស់ក្នុង container

មធ្យោបាយមួយជំនួសក្នុងការតម្លើងគ្រប់យ៉ាងនៅលើកុំព្យូទ័ររបស់អ្នក ឬ Codespace គឺការប្រើ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)។ ថត `.devcontainer` ពិសេសនៅក្នុង repository វគ្គសិក្សា ធ្វើឲ្យ VS Code អាចតម្លើងគម្រោងនៅក្នុង container បាន។ ក្រៅពី Codespaces ការបើក container នេះទាមទារការតំឡើង Docker ហើយពិតប្រាកដវាត្រូវការប្រតិបត្តិការជាច្រើន ដូច្នេះយើងណែនាំសម្រាប់អ្នកមានបទពិសោធន៍ក្នុងការប្រើ container។

វិធីល្អបំផុតសម្រាប់រក្សាសុវត្ថិភាព key API របស់អ្នកនៅពេលប្រើ GitHub Codespaces គឺប្រើ Codespace Secrets។ សូមអនុវត្តតាម [មគ្គុទេសក៍គ្រប់គ្រង Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ដើម្បីស្វែងយល់បន្ថែម។


## មេរៀន និងលក្ខខណ្ឌបច្ចេកទេស

វគ្គសិក្សាមានមេរៀន ៦ មេរៀនគតិ និងមេរៀន ៦ មេរៀនកូដ។

សម្រាប់មេរៀនកូដ យើងប្រើសេវាកម្ម Azure OpenAI។ អ្នកត្រូវការចូលដំណើរការ Azure OpenAI ហើយមានកូនសោ API ដើម្បីដំណើរការកូដនេះ។ អ្នកអាចដាក់ពាក្យស្នើសុំការចូលដំណើរការដោយ [បញ្ចប់ពាក្យស្នើសុំនេះ](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)។

ខណៈរង់ចាំការបញ្ចប់ពាក្យស្នើសុំរបស់អ្នក មេរៀនកូដនីមួយៗក៏រួមបញ្ចូលឯកសារ `README.md` ដែលអ្នកអាចមើលកូដ និងលទ្ធផលបាន។

## ការប្រើសេវាកម្ម Azure OpenAI ដំបូង

ប្រសិនបើនេះជាលើកដំបូងរបស់អ្នកក្នុងការប្រើសេវាកម្ម Azure OpenAI សូមអនុវត្តតាមមគ្គុទេសក៍នេះដើម្បី [បង្កើត និងដាក់ជាសហគ្រិនសេវាកម្ម Azure OpenAI ។](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## ការប្រើប្រាស់ OpenAI API ដំបូង

ប្រសិនបើនេះជាលើកដំបូងរបស់អ្នកក្នុងការប្រើ OpenAI API សូមអនុវត្តតាមមគ្គុទេសក៍លើវិធី [បង្កើត និងប្រើ Interface។](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## ជួបអ្នករៀនផ្សេងទៀត

យើងបានបង្កើតប៉ុស្តិ៍នៅក្នុង [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) ផ្លូវការរបស់យើងសម្រាប់ជួបអ្នករៀនផ្សេងទៀត។ នេះជាវិធីល្អបំផុតសម្រាប់បង្កើតទំនាក់ទំនងជាមួយសហគ្រិន អ្នកសង់ សិស្ស និងអ្នកណាដែលចង់រីកចម្រើនក្នុង Generative AI។

[![ចូលរួមប៉ុស្តិ៍ discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ក្រុមគម្រោងនឹងស្ថិតនៅលើ Discord នេះដើម្បីជួយអ្នករៀនណាមួយ។

## មានចំណូលចិត្តចូលរួម

វគ្គសិក្សានេះជាគម្រោង open-source។ ប្រសិនបើអ្នកឃើញកន្លែងដែលអាចបន្ថែមកែលម្អ ឬមានបញ្ហា សូមបង្កើត [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ឬកត់ត្រា [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)។

ក្រុមគម្រោងនឹងតាមដានចំណូលចិត្តទាំងអស់។ ការចូលរួមក្នុង open source ជាវិធីដ៏អស្ចារ្យមួយសម្រាប់បង្កើតអាជីពក្នុង Generative AI។

ភាគច្រើននៃការចូលរួមតំរូវឲ្យអ្នកយល់ព្រមលើសន្ធិសញ្ញាអ្នកចូលរួម (Contributor License Agreement - CLA) ដែលប្រកាន់ថាអ្នកមានសិទ្ធិ និងពិតជាអនុញ្ញាតបញ្ជូនសិទ្ធិការប្រើប្រាស់ចំណូលចិត្តរបស់អ្នក។ សម្រាប់ព័ត៌មានលម្អិត សូមចូលទៅកាន់ [គេហទំព័រ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)។

សំខាន់: នៅពេលបញ្ចូលការប្រែសម្រួលអត្ថបទនៅក្នុង repo នេះ សូមប្រាកដថាអ្នកមិនប្រើការប្រែសម្រួលដោយម៉ាស៊ីន។ យើងនឹងធ្វើការត្រួតពិនិត្យការប្រែសម្រួលតាមសហគមន៍ ដូច្នេះសូមស្ម័គ្រចិត្តចូលរួមប្រែសម្រួលចំពោះភាសាដែលអ្នកមានជំនាញ។

នៅពេលអ្នកបញ្ជូន pull request មើលថា CLA-bot នឹងសម្រេចថាតើអ្នកត្រូវការ ផ្តល់ CLA ឬ និងតភ្ជាប់នូវស្លាក (label), ការពិពណ៌នា (comment) ដែលសមរម្យ។ អ្នកគ្រាន់តែអនុវត្តតាមណែនាំរបស់ bot ទេ។ អ្នកត្រូវធ្វើដំណើរការនេះតែមួយដងគត់ សម្រាប់គ្រប់ repository ពីរដោយប្រើ CLA របស់យើង។


គម្រោងនេះបានអនុម័តកូដអធិបតីកម្មប្រភពបើករបស់ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)។ សម្រាប់ព័ត៌មានបន្ថែម សូមអានសំណួរញឹកញាប់អំពីកូដអធិបតីកម្ម (Code of Conduct FAQ) ឬទំនាក់ទំនង [Email opencode](opencode@microsoft.com) ប្រសិនបើមានសំណួរឬមតិយោបល់បន្ថែមណាមួយ។

## ចាប់ផ្តើមទាំងអស់គ្នា

ឥឡូវនេះបន្ទាប់ពីអ្នកបានបញ្ចប់ជំហានដែលចាំបាច់សម្រាប់បញ្ចប់វគ្គនេះហើយ យើង​ចាប់ផ្តើមដោយទទួលបាន [ការណែនាំអំពី Generative AI និង LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->