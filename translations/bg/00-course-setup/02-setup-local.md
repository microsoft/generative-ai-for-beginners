# Локална настройка 🖥️

**Използвайте това ръководство, ако предпочитате да работите всичко на собствения си лаптоп.**   
Имаш две възможности: **(A) нативен Python + virtual-env** или **(B) VS Code Dev Container с Docker**.  
Избери това, което ти е по-лесно — и двете водят до същите уроци.

## 1. Предварителни изисквания

| Инструмент          | Версия / Забележки                                                                  |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (вземи го от <https://python.org>)                                           |
| **Git**            | Най-актуалната (идва с Xcode / Git за Windows / Linux пакетен мениджър)             |
| **VS Code**        | По избор, но препоръчително <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Само* за Опция B. Безплатна инсталация: <https://docs.docker.com/desktop/>         |

> 💡 **Съвет** – Провери инструментите в терминала:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Опция A – Нативен Python (най-бързо)

### Стъпка 1 Клонирай това хранилище

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Стъпка 2 Създай и активирай виртуална среда

```bash
python -m venv .venv          # направи един
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Подканата трябва сега да започва с (.venv) — означава, че си в средата.

### Стъпка 3 Инсталирай зависимости

```bash
pip install -r requirements.txt
```

Прескочи към Раздел 3 за [API ключове](#3-добави-твоите-api-ключове)

## 2. Опция B – VS Code Dev Container (Docker)

Настроихме това хранилище и курса с [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), който разполага с Универсална среда за изпълнение, поддържаща Python3, .NET, Node.js и Java разработка. Свързаната конфигурация е дефинирана в `devcontainer.json` файл, който се намира в `.devcontainer/` папката в корена на това хранилище.

>**Защо да избереш това?**
>Идентична среда като Codespaces; няма изместване на зависимости.

### Стъпка 0 Инсталирай допълнителните неща

Docker Desktop – потвърди с ```docker --version```, че работи.
VS Code Remote – Containers разширение (ID: ms-vscode-remote.remote-containers).

### Стъпка 1 Отвори хранилището във VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code разпознава .devcontainer/ и показва подканващ прозорец.

### Стъпка 2 Преотвори в контейнер

Кликни „Reopen in Container“. Docker изгражда образа (≈ 3 минути първи път).
Когато се появи терминалът, си вътре в контейнера.

## 2. Опция C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за инсталиране на [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, както и няколко пакета.
Conda сам по себе си е пакетен мениджър, който улеснява настройването и превключването между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Той е полезен и за инсталиране на пакети, които не са налични чрез `pip`.

### Стъпка 0 Инсталирай Miniconda

Следвай [Ръководството за инсталация на MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), за да я настроиш.

```bash
conda --version
```

### Стъпка 1 Създай виртуална среда

Създай нов файл на средата (*environment.yml*). Ако използваш Codespaces, създай го в `.devcontainer` директорията, т.е. `.devcontainer/environment.yml`.

### Стъпка 2 Попълни файла с конфигурация на средата

Добави следния кодов фрагмент в твоя `environment.yml`

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

### Стъпка 3 Създай Conda средата

Изпълни командите по-долу в командния ред/терминал

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer подпътят се прилага само за настройки на Codespace
conda activate ai4beg
```

Обърни се към [Ръководството за Conda среди](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ако имаш проблеми.

## 2. Опция D – Класически Jupyter / Jupyter Lab (в браузъра)

> **За кого е това?**  
> За всеки, който обича класическия интерфейс на Jupyter или иска да използва бележници без VS Code.  

### Стъпка 1 Увери се, че Jupyter е инсталиран

За да стартираш Jupyter локално, отиди на терминала/командния ред, насочи се в директорията на курса и изпълни:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира Jupyter инстанция, а URL адресът за достъп до нея ще се покаже в командния прозорец.

След като достъпиш URL адреса, трябва да видиш съдържанието на курса и да можеш да навигираш до всеки `*.ipynb` файл. Например, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Добави твоите API ключове

Защитата на API ключовете ти е важна при изграждането на всякакви приложения. Препоръчваме да не съхраняваш API ключове директно в кода си. Качването на тези данни в публично хранилище може да доведе до проблеми със сигурността и дори нежелани разходи, ако бъдат използвани злонамерено.
Ето стъпка по стъпка ръководство как да създадеш `.env` файл за Python и да добавиш своите идентификационни данни за Microsoft Foundry Models:

> **Забележка:** GitHub Models (и неговата променлива `GITHUB_TOKEN`) се прекратяват в края на юли 2026 г. Това ръководство използва [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Предпочиташ да работиш изцяло офлайн? Виж [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Навигирай до директорията на проекта си**: Отвори терминала или командния ред и се насочи до кореновата директория на проекта, където искаш да създадеш `.env` файла.

   ```bash
   cd path/to/your/project
   ```

2. **Създай `.env` файла**: Използвай предпочитания текстов редактор, за да създадеш нов файл с име `.env`. Ако използваш командния ред, можеш да използваш `touch` (на Unix базирани системи) или `echo` (на Windows):

   Unix базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактирай `.env` файла**: Отвори `.env` файла в текстов редактор (напр. VS Code, Notepad++ или друг). Добави следните редове във файла, като заместиш шаблоните със своята действителна крайна точка на Microsoft Foundry проект и API ключ:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Запази файла**: Запази промените и затвори редактора.

5. **Инсталирай `python-dotenv`**: Ако още не си го направил, трябва да инсталираш пакет `python-dotenv`, за да зареждаш променливите на средата от `.env` файла в Python приложението си. Можеш да го инсталираш чрез `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Зареди променливите на средата в Python скрипта си**: В Python скрипта си използвай пакета `python-dotenv`, за да заредиш променливите на средата от `.env` файла:

   ```python
   from dotenv import load_dotenv
   import os

   # Зареждане на променливи на средата от .env файл
   load_dotenv()

   # Достъп до променливите на Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Това е! Успешно създаде `.env` файл, добави своите идентификационни данни на Microsoft Foundry Models и ги зареди в Python приложението си.

🔐 Никога не комитвай `.env` — той вече е в `.gitignore`.
Пълните инструкции за доставчиците се намират в [`providers.md`](03-providers.md).

## 4. Какво следва?

| Искам да…         | Отиди на…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Започна урок 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Настроя LLM доставчик| [`providers.md`](03-providers.md)                                       |
| Срещна други ученици | [Присъедини се към нашия Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Отстраняване на проблеми

| Симптом                                   | Решение                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Добави Python в PATH или отвори терминала отново след инсталация|
| `pip` не може да компилира колела (Windows) | Изпълни `pip install --upgrade pip setuptools wheel` и опитай пак.|
| `ModuleNotFoundError: dotenv`             | Изпълни `pip install -r requirements.txt` (средата не е инсталирана).|
| Docker build се проваля *No space left*  | Docker Desktop ▸ *Settings* ▸ *Resources* → увеличи дисковото пространство.|
| VS Code продължава да иска преотваряне    | Вероятно имаш активни и двете опции; избери една (venv **или** контейнер)|
| OpenAI 401 / 429 грешки                   | Провери стойността на `OPENAI_API_KEY` / ограничения в заявките.|
| Грешки при използване на Conda            | Инсталирай Microsoft AI библиотеки с `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->