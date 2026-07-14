# Локална подешавања 🖥️

**Користите овај водич ако више волите да све покрећете на свом лаптопу.**   
Имате два пута: **(А) нативни Python + виртуелно окружење** или **(Б) VS Code Dev контейнер са Docker-ом**.  
Изаберите оно што вам је лакше — обоје воде ка истим лекцијама.

## 1.  Предуслови

| Алат               | Верзија / Напомене                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10+ (преузмите са <https://python.org>)                                        |
| **Git**            | Најновија (долази са Xcode / Git за Windows / Linux пакет менаџером)             |
| **VS Code**        | Опционо али препоручено <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Само* за Опцију Б. Бесплатна инсталација: <https://docs.docker.com/desktop/>     |

> 💡 **Савет** – Проверите алате у терминалу:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Опција А – Нативни Python (најбрже)

### Корак 1  Клонирајте овај репозиторијум

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Корак 2 Креирајте и активирајте виртуелно окружење

```bash
python -m venv .venv          # направи један
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Упит би сада требао почети са (.venv)—што значи да сте унутар окружења.

### Корак 3 Инсталирајте зависности

```bash
pip install -r requirements.txt
```

Прескочите на Одељак 3 о [API кључевима](#3-додајте-своје-api-кључеве)

## 2. Опција Б – VS Code Dev контејнер (Docker)

Поставили смо овај репозиторијум и курс са [развојним контејнером](https://containers.dev?WT.mc_id=academic-105485-koreyst) који има Универзални runtime који подржава развој за Python3, .NET, Node.js и Java. Поред тога, конфигурација је дефинисана у фајлу `devcontainer.json` који се налази у фасцикли `.devcontainer/` у корену овог репозиторијума.

>**Зашто одабрати ово?**
>Идентично окружење као Codespaces; без проблема са зависностима.

### Корак 0 Инсталирајте додатке

Docker Desktop – потврдите да команда ```docker --version``` ради.
VS Code Remote – Containers екстензија (ID: ms-vscode-remote.remote-containers).

### Корак 1 Отворите репозиторијум у VS Code

Фајл ▸ Отвори фасциклу…  → generative-ai-for-beginners

VS Code детектује .devcontainer/ и приказује упит.

### Корак 2 Поново отвори у контејнеру

Кликните „Ре-отворити у контејнеру“. Docker гради слику (≈ 3 мин први пут).
Када се појави терминалски упит, унутар сте контејнера.

## 2.  Опција Ц – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лагани инсталер за постављање [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-а као и неколико пакета.
Conda је менаџер пакета који олакшава подешавање и пребацивање између различитих Python [**виртуелних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Такође је користан за инсталацију пакета који нису доступни преко `pip`.

### Корак 0  Инсталирајте Miniconda

Пратите [MiniConda упутство за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да бисте га поставили.

```bash
conda --version
```

### Корак 1 Креирајте виртуелно окружење

Креирајте нови фајл окружења (*environment.yml*). Ако пратите упутство користећи Codespaces, направите га унутар директоријума `.devcontainer`, дакле `.devcontainer/environment.yml`.

### Корак 2  Попуните ваш фајл окружења

Додајте следећи исечак у ваш `environment.yml`

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

Покрените доленаведене команде у вашем командном реду/терминалу

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer под-путања се примењује само на Codespace поставке
conda activate ai4beg
```

Погледајте [упутство за Conda окружења](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђете на проблеме.

## 2  Опција Д – Класични Jupyter / Jupyter Lab (у прегледачу)

> **Ко је ово?**  
> Сви који воле класичан Jupyter интерфејс или желе да покрећу нотебоок-ове без VS Code-а.  

### Корак 1  Уверите се да је Jupyter инсталиран

Да бисте покренули Jupyter локално, идите у терминал/командну линију, навигирајте до директоријума курса и покрените:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter инстанцу и URL за приступ биће видљив у командном прозору.

Када приступите URL-у, треба да видите план курса и бићете у могућности да отворите било који `*.ipynb` фајл. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Додајте своје API кључеве

Чување ваших API кључева безбедним и сигурним је важно када градите било који тип апликације. Препоручујемо да не чувате API кључеве директно у свом коду. Комитовање тих података у јавни репозиторијум може довести до безбедносних проблема и чак непожељних трошкова ако их злоупотреби злонамерни корисник.
Ево корак-по-корак водича како да направите `.env` фајл за Python и додате своје Microsoft Foundry Models креденцијале:

> **Напомена:** GitHub Models (и његова `GITHUB_TOKEN` променљива) се гаси крајем јула 2026. године. Овај водич користи [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) уместо тога. Жељни радити потпуно офлајн? Погледајте [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Идите до свог директоријума пројекта**: Отворите терминал или командну линију и идите у коренски директоријум вашег пројекта у коме желите да направите `.env` фајл.

   ```bash
   cd path/to/your/project
   ```

2. **Направите `.env` фајл**: Користите свој омиљени уређивач текста да направите нови фајл под именом `.env`. Ако користите командну линију, можете користити `touch` (на Unix системима) или `echo` (на Windows-у):

   Unix системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Уредите `.env` фајл**: Отворите `.env` фајл у уређивачу текста (нпр. VS Code, Notepad++, или други уређивач). Додајте следеће линије у фајл, замењујући места за унос својим стварним Microsoft Foundry project endpoint-ом и API кључем:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сачувајте фајл**: Сачувајте измене и затворите уређивач текста.

5. **Инсталирајте `python-dotenv`**: Ако већ нисте, требаће вам пакет `python-dotenv` да бисте учитали променљиве окружења из `.env` фајла у вашу Python апликацију. Можете га инсталирати преко `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитајте променљиве окружења у вашем Python скрипту**: У вашем Python скрипту користите пакет `python-dotenv` да учитате променљиве окружења из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Учитај променљиве окружења из .env фајла
   load_dotenv()

   # Приступи променљивим Microsoft Foundry модела
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

То је то! Успешно сте креирали `.env` фајл, додали своје Microsoft Foundry Models креденцијале и учитали их у своју Python апликацију.

🔐 Никад не комитујте .env — већ је у .gitignore.
Потпуна упутства провајдера налазе се у [`providers.md`](03-providers.md).

## 4. Шта следи?

| Желим да…          | Идем на…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Почнем лекцију 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Подесим LLM провајдера | [`providers.md`](03-providers.md)                                       |
| Упознам друге ученике | [Придружи се нашем Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Решавање проблема

| Симптом                                   | Решење                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Додајте Python у PATH или поново отворите терминал након инсталације |
| `pip` не може направити wheele (Windows)  | Покрените `pip install --upgrade pip setuptools wheel` и покушајте поново. |
| `ModuleNotFoundError: dotenv`             | Покрените `pip install -r requirements.txt` (виртуелно окружење није инсталирано). |
| Docker build не успева *Нема више простора*| Docker Desktop ▸ *Settings* ▸ *Resources* → повећајте величину диска.   |
| VS Code стално тражи да се поново отвори    | Могуће је да су обе опције активне; изаберите само једну (venv **или** контејнер). |
| OpenAI 401 / 429 грешке                   | Проверите вредност `OPENAI_API_KEY` / ограничења броја упита.       |
| Грешке при коришћењу Conda                 | Инсталирајте Microsoft AI библиотеке користећи `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->