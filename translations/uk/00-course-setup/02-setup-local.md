# Локальна установка 🖥️

**Використовуйте цей посібник, якщо ви віддаєте перевагу запускати все на власному ноутбуці.**  
У вас є два шляхи: **(A) нативний Python + virtual-env** або **(B) VS Code Dev Container з Docker**.  
Обирайте той, який здається легшим — обидва ведуть до тих самих уроків.

## 1. Передумови

| Інструмент           | Версія / Примітки                                                                   |
|----------------------|-------------------------------------------------------------------------------------|
| **Python**           | 3.10 + (отримати з <https://python.org>)                                            |
| **Git**              | Остання (йде з Xcode / Git для Windows / пакетним менеджером Linux)                  |
| **VS Code**          | Необов’язково, але рекомендовано <https://code.visualstudio.com>                     |
| **Docker Desktop**   | *Тільки* для Варіанту B. Безкоштовна установка: <https://docs.docker.com/desktop/>  |

> 💡 **Порада** – Перевірте інструменти в терміналі:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Варіант A – Нативний Python (найшвидший)

### Крок 1 Клонувати цей репозиторій

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Крок 2 Створити та активувати віртуальне середовище

```bash
python -m venv .venv          # зробити один
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Тепер у підказці має бути (.venv) — це означає, що ви в середовищі.

### Крок 3 Встановити залежності

```bash
pip install -r requirements.txt
```

Перейдіть до Розділу 3 про [API ключі](#3-додайте-свої-api-ключі)

## 2. Варіант B – VS Code Dev Container (Docker)

Цей репозиторій та курс налаштовані з використанням [контейнера для розробки](https://containers.dev?WT.mc_id=academic-105485-koreyst), який має універсальне середовище виконання, що підтримує Python3, .NET, Node.js та Java. Відповідна конфігурація визначена у файлі `devcontainer.json`, розташованому у папці `.devcontainer/` в корені репозиторію.

>**Чому обрати це?**
>Ідентичне середовище до Codespaces; відсутність зсуву залежностей.

### Крок 0 Встановіть додаткове програмне забезпечення

Docker Desktop – перевірте, що команда ```docker --version``` працює.
Розширення VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Крок 1 Відкрийте репозиторій у VS Code

Файл ▸ Відкрити папку… → generative-ai-for-beginners

VS Code виявляє .devcontainer/ та відобразить підказку.

### Крок 2 Відкрити повторно в контейнері

Натисніть «Reopen in Container». Docker створює образ (≈ 3 хв перший запуск).
Коли з’явиться термінальна підказка, ви вже всередині контейнера.

## 2. Варіант C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а також кількох пакетів.
Conda — це менеджер пакетів, який полегшує налаштування та перемикання між різними Python [**віртуальними середовищами**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) і пакетами. Він також корисний для встановлення пакетів, які недоступні через `pip`.

### Крок 0 Встановіть Miniconda

Виконайте інструкції в [посібнику з встановлення MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Крок 1 Створіть віртуальне середовище

Створіть новий файл середовища (*environment.yml*). Якщо ви працюєте у Codespaces, створіть його в папці `.devcontainer`, тобто `.devcontainer/environment.yml`.

### Крок 2 Заповніть файл середовища

Додайте наступний фрагмент до вашого `environment.yml`

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

### Крок 3 Створіть середовище Conda

Виконайте команди нижче у вашому командному рядку/терміналі

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Підшлях .devcontainer застосовується лише до налаштувань Codespace
conda activate ai4beg
```

Зверніться до [посібника з Conda середовищ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), якщо виникнуть проблеми.

## 2 Варіант D – Класичний Jupyter / Jupyter Lab (у вашому браузері)

> **Для кого це?**  
> Для тих, хто любить класичний інтерфейс Jupyter або хоче запускати ноутбуки без VS Code.  

### Крок 1 Переконайтеся, що Jupyter встановлено

Щоб запустити Jupyter локально, відкрийте термінал/командний рядок, перейдіть у папку курсу і виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить інстанс Jupyter, і URL для доступу буде показано у вікні командного рядка.

Після переходу за URL, ви побачите план курсу і зможете переходити до будь-якого файлу `*.ipynb`. Наприклад, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Додайте свої API ключі

Важливо тримати ваші API ключі в безпеці при створенні будь-яких додатків. Ми рекомендуємо не зберігати ключі безпосередньо у коді. Збереження цих даних у публічному репозиторії може призвести до проблем з безпекою та навіть небажаних витрат у разі використання сторонніми особами.
Ось покроковий посібник з створення файлу `.env` для Python і додавання ваших облікових даних Microsoft Foundry Models:

> **Примітка:** GitHub Models (та змінна `GITHUB_TOKEN`) буде припинено наприкінці липня 2026 року. Цей посібник використовує [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) замість нього. Бажаєте працювати повністю офлайн? Дивіться [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Перейдіть у директорію вашого проєкту**: Відкрийте термінал або командний рядок і перейдіть у кореневу папку проєкту, де хочете створити файл `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Створіть файл `.env`**: Використайте улюблений текстовий редактор для створення файлу з назвою `.env`. Якщо ви використовуєте командний рядок, можна використати `touch` (в системах Unix) або `echo` (у Windows):

   Для Unix-подібних систем:

   ```bash
   touch .env
   ```

   Для Windows:

   ```cmd
   echo . > .env
   ```

3. **Відредагуйте файл `.env`**: Відкрийте `.env` у текстовому редакторі (наприклад, VS Code, Notepad++ або будь-якому іншому). Додайте наступні рядки, замінивши заповнювачі на ваші реальні значення кінцевої точки проекту Microsoft Foundry та API ключа:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Збережіть файл**: Збережіть зміни і закрийте редактор.

5. **Встановіть `python-dotenv`**: Якщо ще не встановили, вам потрібно встановити пакет `python-dotenv`, щоб завантажувати змінні середовища з файлу `.env` у ваш Python додаток. Встановити можна через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у ваш скрипт Python**: Використайте пакет `python-dotenv`, щоб завантажити змінні середовища з файлу `.env` у вашому Python скрипті:

   ```python
   from dotenv import load_dotenv
   import os

   # Завантажте змінні середовища з файлу .env
   load_dotenv()

   # Отримайте доступ до змінних моделей Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ось і все! Ви успішно створили файл `.env`, додали облікові дані Microsoft Foundry Models та завантажили їх у ваш Python додаток.

🔐 Ніколи не комітьте .env — він уже в .gitignore.
Повні інструкції провайдера знаходяться в [`providers.md`](03-providers.md).

## 4. Що далі?

| Я хочу…               | Перейти до…                                                             |
|-----------------------|------------------------------------------------------------------------|
| Почати урок 1          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Налаштувати LLM провайдера | [`providers.md`](03-providers.md)                                       |
| Познайомитися з іншими учасниками | [Приєднатись до нашого Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Усунення несправностей

| Симптом                                   | Виправлення                                                    |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Додайте Python у PATH або закрийте і відкрийте термінал після встановлення |
| `pip` не може збирати колеса (Windows)   | Виконайте `pip install --upgrade pip setuptools wheel` і спробуйте знову.  |
| `ModuleNotFoundError: dotenv`             | Запустіть `pip install -r requirements.txt` (середовище не було встановлено).|
| Збірка Docker не вдається *No space left*| Docker Desktop ▸ *Settings* ▸ *Resources* → збільшіть розмір диска.         |
| VS Code постійно пропонує повторно відкрити| Можливо, у вас активні обидва варіанти; оберіть один (venv **або** контейнер)|
| OpenAI 401 / 429 помилки                   | Перевірте значення `OPENAI_API_KEY` / обмеження частоти запитів.           |
| Помилки при використанні Conda              | Встановіть бібліотеки Microsoft AI за допомогою `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->