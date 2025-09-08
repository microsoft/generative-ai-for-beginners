<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:19:51+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "bg"
}
-->
# Локална настройка 🖥️

**Използвайте това ръководство, ако предпочитате да работите на собствения си лаптоп.**  
Имате два варианта: **(A) native Python + virtual-env** или **(B) VS Code Dev Container с Docker**.  
Изберете този, който ви е по-удобен—и двата водят до едни и същи уроци.

## 1. Предварителни изисквания

| Инструмент          | Версия / Бележки                                                                |
|---------------------|---------------------------------------------------------------------------------|
| **Python**          | 3.10 + (изтеглете от <https://python.org>)                                      |
| **Git**             | Най-новата (идва с Xcode / Git for Windows / Linux пакет мениджър)               |
| **VS Code**         | По избор, но препоръчителен <https://code.visualstudio.com>                     |
| **Docker Desktop**  | *Само* за Вариант B. Безплатна инсталация: <https://docs.docker.com/desktop/>   |

> 💡 **Съвет** – Проверете инструментите в терминала:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Вариант A – Native Python (най-бърз)

### Стъпка 1 Клонирайте това репо

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Стъпка 2 Създайте и активирайте виртуална среда

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ В началото на реда трябва да се появи (.venv)—това означава, че сте в средата.

### Стъпка 3 Инсталирайте зависимостите

```bash
pip install -r requirements.txt
```

Прескочете към Секция 3 за [API ключове](../../../00-course-setup)

## 2. Вариант B – VS Code Dev Container (Docker)

Това репо и курс са настроени с [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), който има универсална среда и поддържа Python3, .NET, Node.js и Java. Конфигурацията е описана във файла `devcontainer.json` в папката `.devcontainer/` в основата на репото.

>**Защо да изберете това?**
>Идентична среда като Codespaces; няма разминавания в зависимостите.

### Стъпка 0 Инсталирайте допълнителните инструменти

Docker Desktop – проверете дали ```docker --version``` работи.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Стъпка 1 Отворете репото във VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code засича .devcontainer/ и показва съобщение.

### Стъпка 2 Отворете в контейнер

Натиснете “Reopen in Container”. Docker ще изгради образа (≈ 3 мин първия път).
Когато се появи терминалът, вече сте в контейнера.

## 2. Вариант C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и някои пакети.
Conda е пакетен мениджър, който улеснява настройката и превключването между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Също така е полезен за инсталиране на пакети, които не са налични през `pip`.

### Стъпка 0 Инсталирайте Miniconda

Следвайте [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), за да го настроите.

```bash
conda --version
```

### Стъпка 1 Създайте виртуална среда

Създайте нов файл за среда (*environment.yml*). Ако работите в Codespaces, създайте го в `.devcontainer` директорията, т.е. `.devcontainer/environment.yml`.

### Стъпка 2 Попълнете файла за среда

Добавете следния код към вашия `environment.yml`

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

### Стъпка 3 Създайте Conda среда

Изпълнете следните команди в терминала

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ако срещнете проблеми, вижте [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2 Вариант D – Класически Jupyter / Jupyter Lab (в браузъра)

> **За кого е това?**  
> Всеки, който харесва класическия Jupyter интерфейс или иска да работи с notebooks без VS Code.  

### Стъпка 1 Уверете се, че Jupyter е инсталиран

За да стартирате Jupyter локално, отворете терминала, отидете в директорията на курса и изпълнете:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира Jupyter и URL за достъп ще се покаже в прозореца на терминала.

След като отворите URL-а, ще видите структурата на курса и ще можете да навигирате до всеки `*.ipynb` файл. Например, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Добавете вашите API ключове

Да пазите API ключовете си е важно при създаване на всякакви приложения. Препоръчваме да не ги записвате директно в кода си. Ако ги качите в публично репо, може да имате проблеми със сигурността и нежелани разходи, ако някой ги използва неправомерно.
Ето стъпка по стъпка как да създадете `.env` файл за Python и да добавите `GITHUB_TOKEN`:

1. **Отидете в директорията на проекта**: Отворете терминала и отидете в основната директория на проекта, където искате да създадете `.env` файла.

   ```bash
   cd path/to/your/project
   ```

2. **Създайте `.env` файл**: Използвайте любимия си текстов редактор, за да създадете нов файл с име `.env`. Ако сте в командния ред, може да използвате `touch` (на Unix-базирани системи) или `echo` (на Windows):

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактирайте `.env` файла**: Отворете `.env` файла с текстов редактор (например VS Code, Notepad++ или друг). Добавете следния ред, като замените `your_github_token_here` с вашия реален GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Запазете файла**: Запазете промените и затворете редактора.

5. **Инсталирайте `python-dotenv`**: Ако още не сте, трябва да инсталирате пакета `python-dotenv`, за да заредите променливите от `.env` файла във вашето Python приложение. Може да го инсталирате с `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Заредете променливите в Python скрипта си**: В Python скрипта си използвайте `python-dotenv`, за да заредите променливите от `.env` файла:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Вече имате `.env` файл, добавен GitHub токен и той е зареден във вашето Python приложение.

🔐 Никога не качвайте .env—вече е в .gitignore.
Пълни инструкции за доставчиците има в [`providers.md`](03-providers.md).

## 4. Какво следва?

| Искам да…           | Отиди на…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Започна Урок 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Настроя LLM доставчик | [`providers.md`](03-providers.md)                                        |
| Срещна други курсисти | [Присъедини се към Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Проблеми и решения

| Симптом                                   | Решение                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Добавете Python към PATH или рестартирайте терминала след инсталация |
| `pip` не може да build-не wheels (Windows)| `pip install --upgrade pip setuptools wheel` и опитайте пак.    |
| `ModuleNotFoundError: dotenv`             | Изпълнете `pip install -r requirements.txt` (средата не е инсталирана).|
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → увеличете дисковото пространство. |
| VS Code постоянно пита да се отвори наново| Може би имате активни и двата варианта; изберете един (venv **или** container)|
| OpenAI 401 / 429 грешки                   | Проверете стойността на `OPENAI_API_KEY` / лимитите за заявки.  |
| Грешки с Conda                            | Инсталирайте Microsoft AI libraries с `conda install -c microsoft azure-ai-ml`|

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали от използването на този превод.