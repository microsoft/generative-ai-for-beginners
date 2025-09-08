<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T20:05:01+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "uk"
}
-->
# Локальне налаштування 🖥️

**Скористайтеся цим гайдом, якщо хочете запускати все на власному ноутбуці.**  
У вас є два шляхи: **(A) нативний Python + virtual-env** або **(B) Dev Container у VS Code з Docker**.  
Обирайте той, що зручніше—обидва ведуть до однакових уроків.

## 1. Необхідне

| Інструмент          | Версія / Примітки                                                                 |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10+ (завантажити з <https://python.org>)                                        |
| **Git**             | Остання (йде з Xcode / Git for Windows / менеджер пакунків Linux)                 |
| **VS Code**         | Необов’язково, але рекомендовано <https://code.visualstudio.com>                  |
| **Docker Desktop**  | *Тільки* для Варіанту B. Безкоштовно: <https://docs.docker.com/desktop/>          |

> 💡 **Порада** – Перевірте інструменти у терміналі:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Варіант A – Нативний Python (найшвидше)

### Крок 1  Клонувати цей репозиторій

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Крок 2 Створити та активувати віртуальне середовище

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ У рядку запрошення має з’явитися (.venv)—це означає, що ви всередині середовища.

### Крок 3 Встановити залежності

```bash
pip install -r requirements.txt
```

Переходьте до Розділу 3 про [API-ключі](../../../00-course-setup)

## 2. Варіант B – VS Code Dev Container (Docker)

Ми налаштували цей репозиторій і курс із [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), який має універсальне середовище для Python3, .NET, Node.js та Java. Відповідна конфігурація описана у файлі `devcontainer.json` у папці `.devcontainer/` у корені репозиторію.

>**Чому обрати це?**
>Однакове середовище з Codespaces; жодних розбіжностей у залежностях.

### Крок 0 Встановіть додаткове

Docker Desktop – переконайтеся, що ```docker --version``` працює.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Крок 1 Відкрийте репозиторій у VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code знаходить .devcontainer/ і показує підказку.

### Крок 2 Відкрити у контейнері

Натисніть “Reopen in Container”. Docker збере образ (≈ 3 хвилини вперше).
Коли з’явиться термінал, ви вже всередині контейнера.

## 2. Варіант C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python і кількох пакетів.
Conda — це менеджер пакетів, який спрощує створення та перемикання між різними [**віртуальними середовищами**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python і пакетами. Також зручно для встановлення пакетів, яких немає у `pip`.

### Крок 0  Встановіть Miniconda

Дотримуйтесь [інструкції з встановлення MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), щоб налаштувати її.

```bash
conda --version
```

### Крок 1 Створіть віртуальне середовище

Створіть новий файл середовища (*environment.yml*). Якщо ви працюєте у Codespaces, створіть його у папці `.devcontainer`, тобто `.devcontainer/environment.yml`.

### Крок 2  Заповніть файл середовища

Додайте цей фрагмент у ваш `environment.yml`

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

### Крок 3 Створіть Conda-середовище

Виконайте ці команди у терміналі/командному рядку

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Якщо виникнуть проблеми, зверніться до [гайду по середовищах Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Варіант D – Класичний Jupyter / Jupyter Lab (у браузері)

> **Для кого це?**  
> Для тих, хто любить класичний інтерфейс Jupyter або хоче запускати ноутбуки без VS Code.  

### Крок 1  Переконайтеся, що Jupyter встановлено

Щоб запустити Jupyter локально, відкрийте термінал, перейдіть у папку курсу і виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить Jupyter, і у вікні командного рядка з’явиться URL для доступу.

Після переходу за цим URL ви побачите структуру курсу і зможете відкрити будь-який файл `*.ipynb`. Наприклад, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Додайте свої API-ключі

Зберігати API-ключі у безпеці дуже важливо при створенні будь-яких застосунків. Ми радимо не зберігати ключі прямо у коді. Якщо додати їх у публічний репозиторій, це може призвести до проблем із безпекою і навіть небажаних витрат, якщо хтось скористається ними.
Ось покрокова інструкція, як створити `.env` файл для Python і додати `GITHUB_TOKEN`:

1. **Перейдіть у папку проєкту**: Відкрийте термінал і перейдіть у кореневу папку проєкту, де хочете створити `.env` файл.

   ```bash
   cd path/to/your/project
   ```

2. **Створіть файл `.env`**: Використайте улюблений редактор, щоб створити новий файл з назвою `.env`. Якщо працюєте у командному рядку, можна скористатися `touch` (Unix-системи) або `echo` (Windows):

   Unix-системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Відредагуйте файл `.env`**: Відкрийте `.env` у редакторі (наприклад, VS Code, Notepad++ чи будь-якому іншому). Додайте такий рядок, замінивши `your_github_token_here` на свій справжній GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Збережіть файл**: Збережіть зміни і закрийте редактор.

5. **Встановіть `python-dotenv`**: Якщо ще не встановили, потрібно додати пакет `python-dotenv`, щоб завантажувати змінні середовища з `.env` у ваш застосунок Python. Встановіть через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у Python-скрипті**: У вашому скрипті використайте пакет `python-dotenv`, щоб підвантажити змінні з `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Ви успішно створили `.env`, додали GitHub токен і підвантажили його у Python-застосунок.

🔐 Ніколи не комітьте .env—він вже у .gitignore.
Повна інструкція для провайдерів у [`providers.md`](03-providers.md).

## 4. Що далі?

| Я хочу…              | Перейти до…                                                                |
|----------------------|----------------------------------------------------------------------------|
| Почати урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| Налаштувати LLM-провайдера | [`providers.md`](03-providers.md)                                 |
| Познайомитися з іншими | [Приєднатися до Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Вирішення проблем

| Симптом                                   | Рішення                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Додайте Python у PATH або перезапустіть термінал після встановлення |
| `pip` не може зібрати wheels (Windows)    | `pip install --upgrade pip setuptools wheel` і спробуйте ще раз.|
| `ModuleNotFoundError: dotenv`             | Запустіть `pip install -r requirements.txt` (середовище не встановлено).|
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → збільшіть розмір диску.|
| VS Code постійно пропонує reopen          | Можливо, активні обидва варіанти; оберіть один (venv **або** container)|
| OpenAI 401 / 429 errors                   | Перевірте значення `OPENAI_API_KEY` / ліміти запитів.          |
| Помилки з Conda                           | Встановіть бібліотеки Microsoft AI через `conda install -c microsoft azure-ai-ml`|

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.