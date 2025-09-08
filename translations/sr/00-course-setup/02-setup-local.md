<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:28:59+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "sr"
}
-->
# Локално подешавање 🖥️

**Користите овај водич ако желите да све покренете на свом лаптопу.**  
Постоје два пута: **(A) нативни Python + virtual-env** или **(B) VS Code Dev Container са Docker-ом**.  
Изаберите шта вам је лакше—оба воде до истих лекција.

## 1.  Предуслови

| Алат                | Верзија / Напомене                                                                 |
|---------------------|------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (преузмите са <https://python.org>)                                         |
| **Git**             | Најновији (долази са Xcode / Git for Windows / Linux package manager-ом)           |
| **VS Code**         | Није обавезан, али се препоручује <https://code.visualstudio.com>                  |
| **Docker Desktop**  | *Само* за опцију Б. Бесплатно: <https://docs.docker.com/desktop/>                  |

> 💡 **Савет** – Проверите алате у терминалу:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Опција А – Нативни Python (најбрже)

### Корак 1  Клонирајте овај репо

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Корак 2 Креирајте и активирајте виртуелно окружење

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt сада треба да почиње са (.venv)—то значи да сте унутар окружења.

### Корак 3 Инсталирајте зависности

```bash
pip install -r requirements.txt
```

Прескочите на одељак 3 о [API кључевима](../../../00-course-setup)

## 2. Опција Б – VS Code Dev Container (Docker)

Овај репозиторијум и курс су подешени са [development container-ом](https://containers.dev?WT.mc_id=academic-105485-koreyst) који има универзални runtime и подржава Python3, .NET, Node.js и Java развој. Конфигурација се налази у `devcontainer.json` фајлу у `.devcontainer/` фасцикли на корену репозиторијума.

>**Зашто одабрати ово?**
>Идентично окружење као Codespaces; нема разлике у зависностима.

### Корак 0 Инсталирајте додатке

Docker Desktop – проверите да ли ```docker --version``` ради.
VS Code Remote – Containers екстензија (ID: ms-vscode-remote.remote-containers).

### Корак 1 Отворите репо у VS Code-у

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code препознаје .devcontainer/ и појављује се обавештење.

### Корак 2 Поново отворите у контејнеру

Кликните “Reopen in Container”. Docker гради слику (≈ 3 мин први пут).
Када се појави терминал prompt, унутар сте контејнера.

## 2.  Опција Ц – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лаган инсталер за [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и неколико пакета.
Conda је менаџер пакета који олакшава подешавање и пребацивање између различитих Python [**виртуелних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Корисно је и за инсталацију пакета који нису доступни преко `pip`.

### Корак 0  Инсталирајте Miniconda

Пратите [MiniConda упутство за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да је подесите.

```bash
conda --version
```

### Корак 1 Креирајте виртуелно окружење

Креирајте нови environment фајл (*environment.yml*). Ако радите у Codespaces-у, направите га унутар `.devcontainer` директоријума, дакле `.devcontainer/environment.yml`.

### Корак 2  Попуните environment фајл

Додајте следећи део у ваш `environment.yml`

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

### Корак 3 Креирајте Conda окружење

Покрените следеће команде у командној линији/терминалу

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Погледајте [Conda environments водич](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђете на проблеме.

## 2  Опција Д – Класични Jupyter / Jupyter Lab (у вашем прегледачу)

> **За кога је ово?**  
> За све који воле класични Jupyter интерфејс или желе да покрећу бележнице без VS Code-а.  

### Корак 1  Проверите да ли је Jupyter инсталиран

Да бисте покренули Jupyter локално, идите у терминал/командну линију, уђите у фасциклу курса и покрените:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter и URL за приступ ће бити приказан у командној линији.

Када приступите URL-у, видећете садржај курса и можете да отворите било који `*.ipynb` фајл. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Додајте своје API кључеве

Чување ваших API кључева безбедним је важно при изради било које апликације. Препоручујемо да никада не чувате API кључеве директно у коду. Ако их пошаљете у јавни репозиторијум, то може довести до безбедносних проблема и нежељених трошкова ако их неко злоупотреби.
Ево корак-по-корак упутства како да направите `.env` фајл за Python и додате `GITHUB_TOKEN`:

1. **Идите у фасциклу пројекта**: Отворите терминал или командну линију и идите у коренску фасциклу пројекта где желите да направите `.env` фајл.

   ```bash
   cd path/to/your/project
   ```

2. **Направите `.env` фајл**: Користите омиљени едитор да направите нови фајл под именом `.env`. Ако користите командну линију, можете користити `touch` (на Unix системима) или `echo` (на Windows-у):

   Unix системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Измените `.env` фајл**: Отворите `.env` у едитору (нпр. VS Code, Notepad++ или било ком другом). Додајте следећу линију, замените `your_github_token_here` са вашим стварним GitHub токеном:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сачувајте фајл**: Сачувајте измене и затворите едитор.

5. **Инсталирајте `python-dotenv`**: Ако већ нисте, инсталирајте `python-dotenv` пакет да бисте учитали променљиве окружења из `.env` фајла у вашу Python апликацију. Инсталирајте га преко `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитајте променљиве окружења у Python скрипти**: У вашој Python скрипти користите `python-dotenv` да учитате променљиве из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

То је то! Успешно сте направили `.env` фајл, додали свој GitHub токен и учитали га у Python апликацију.

🔐 Никада не шаљите .env—већ је у .gitignore.
Потпуно упутство за провајдере је у [`providers.md`](03-providers.md).

## 4. Шта даље?

| Желим да…           | Иди на…                                                                  |
|---------------------|--------------------------------------------------------------------------|
| Почнем лекцију 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Подесим LLM провајдера | [`providers.md`](03-providers.md)                                      |
| Упознам друге полазнике | [Придружи се нашем Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Решавање проблема

| Симптом                                   | Решење                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Додајте Python у PATH или поново покрените терминал након инсталације |
| `pip` не може да направи wheels (Windows) | `pip install --upgrade pip setuptools wheel` па покушајте поново.|
| `ModuleNotFoundError: dotenv`             | Покрените `pip install -r requirements.txt` (env није инсталиран).|
| Docker build не успева *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → повећајте простор на диску.|
| VS Code стално тражи да поново отворите   | Можда су обе опције активне; изаберите једну (venv **или** container)|
| OpenAI 401 / 429 грешке                   | Проверите вредност `OPENAI_API_KEY` / лимите захтева.           |
| Грешке са Conda                           | Инсталирајте Microsft AI библиотеке са `conda install -c microsoft azure-ai-ml`|

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала употребом овог превода.