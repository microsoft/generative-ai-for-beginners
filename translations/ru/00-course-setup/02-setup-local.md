<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T13:50:40+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ru"
}
-->
# Локальная установка 🖥️

**Используйте это руководство, если хотите запускать всё на своём ноутбуке.**  
У вас есть два варианта: **(A) нативный Python + virtual-env** или **(B) Dev Container VS Code с Docker**.  
Выбирайте тот, что удобнее — оба приведут к одним и тем же урокам.

## 1. Необходимое ПО

| Инструмент           | Версия / Примечания                                                                |
|----------------------|-----------------------------------------------------------------------------------|
| **Python**           | 3.10+ (скачать: <https://python.org>)                                             |
| **Git**              | Последняя версия (идёт с Xcode / Git for Windows / менеджер пакетов Linux)        |
| **VS Code**          | Необязательно, но рекомендуется <https://code.visualstudio.com>                   |
| **Docker Desktop**   | *Только* для варианта B. Бесплатно: <https://docs.docker.com/desktop/>            |

> 💡 **Совет** – Проверьте инструменты в терминале:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Вариант A – Нативный Python (самый быстрый)

### Шаг 1  Клонируйте этот репозиторий

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Шаг 2 Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ В начале строки должно появиться (.venv) — это значит, что вы внутри окружения.

### Шаг 3 Установите зависимости

```bash
pip install -r requirements.txt
```

Переходите к разделу 3 про [API-ключи](../../../00-course-setup)

## 2. Вариант B – Dev Container VS Code (Docker)

Мы подготовили этот репозиторий и курс с помощью [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), который содержит универсальное окружение для разработки на Python3, .NET, Node.js и Java. Соответствующая конфигурация описана в файле `devcontainer.json` в папке `.devcontainer/` в корне репозитория.

>**Почему выбрать этот вариант?**
>Окружение идентично Codespaces; никаких различий в зависимостях.

### Шаг 0 Установите дополнительные инструменты

Docker Desktop – убедитесь, что ```docker --version``` работает.  
Расширение VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Шаг 1 Откройте репозиторий в VS Code

Файл ▸ Открыть папку…  → generative-ai-for-beginners

VS Code обнаружит .devcontainer/ и покажет соответствующее уведомление.

### Шаг 2 Откройте в контейнере

Нажмите “Reopen in Container”. Docker соберёт образ (≈ 3 минуты при первом запуске).  
Когда появится приглашение терминала, вы уже внутри контейнера.

## 2. Вариант C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это облегчённый установщик для [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и некоторых пакетов.  
Conda — это менеджер пакетов, который упрощает создание и переключение между разными [**виртуальными окружениями**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакетами. Также удобно для установки пакетов, которых нет в `pip`.

### Шаг 0  Установите Miniconda

Следуйте [инструкции по установке MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Шаг 1 Создайте виртуальное окружение

Создайте новый файл окружения (*environment.yml*). Если вы работаете в Codespaces, создайте его в папке `.devcontainer`, то есть `.devcontainer/environment.yml`.

### Шаг 2  Заполните файл окружения

Добавьте следующий фрагмент в ваш `environment.yml`

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

### Шаг 3 Создайте окружение Conda

Выполните команды ниже в командной строке/терминале

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Если возникнут проблемы, обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. Вариант D – Классический Jupyter / Jupyter Lab (в браузере)

> **Для кого это?**  
> Для тех, кто предпочитает классический интерфейс Jupyter или хочет запускать ноутбуки без VS Code.  

### Шаг 1  Убедитесь, что Jupyter установлен

Чтобы запустить Jupyter локально, откройте терминал/командную строку, перейдите в папку курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит Jupyter, и в командной строке появится URL для доступа.

После перехода по этому адресу вы увидите структуру курса и сможете открыть любой файл `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Добавьте свои API-ключи

Безопасность ваших API-ключей очень важна при создании любых приложений. Мы рекомендуем не хранить ключи прямо в коде. Если вы случайно добавите их в публичный репозиторий, это может привести к проблемам с безопасностью и даже финансовым потерям, если кто-то воспользуется ими в своих целях.
Вот пошаговая инструкция, как создать файл `.env` для Python и добавить туда `GITHUB_TOKEN`:

1. **Перейдите в папку проекта**: Откройте терминал или командную строку и перейдите в корневую папку проекта, где хотите создать файл `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Создайте файл `.env`**: Используйте любимый текстовый редактор, чтобы создать новый файл с именем `.env`. В командной строке можно использовать `touch` (на Unix-системах) или `echo` (на Windows):

   Unix-системы:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте `.env` в редакторе (например, VS Code, Notepad++ или любом другом). Добавьте строку ниже, заменив `your_github_token_here` на ваш реальный GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте редактор.

5. **Установите `python-dotenv`**: Если ещё не сделали этого, установите пакет `python-dotenv`, чтобы загружать переменные окружения из файла `.env` в ваше Python-приложение. Установить можно через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в вашем Python-скрипте**: В вашем скрипте используйте пакет `python-dotenv`, чтобы загрузить переменные из `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Вы успешно создали файл `.env`, добавили туда GitHub токен и загрузили его в своё Python-приложение.

🔐 Никогда не коммитьте .env — он уже добавлен в .gitignore.  
Полные инструкции по провайдерам смотрите в [`providers.md`](03-providers.md).

## 4. Что дальше?

| Я хочу…              | Перейти к…                                                                |
|----------------------|----------------------------------------------------------------------------|
| Начать урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| Настроить LLM-провайдера | [`providers.md`](03-providers.md)                                         |
| Познакомиться с другими | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Решение проблем

| Симптом                                   | Решение                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Добавьте Python в PATH или перезапустите терминал после установки|
| `pip` не может собрать wheels (Windows)   | `pip install --upgrade pip setuptools wheel` и попробуйте снова.|
| `ModuleNotFoundError: dotenv`             | Выполните `pip install -r requirements.txt` (окружение не установлено).|
| Ошибка сборки Docker *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → увеличьте размер диска.|
| VS Code постоянно предлагает открыть заново| Возможно, активны оба варианта; выберите один (venv **или** контейнер)|
| Ошибки OpenAI 401 / 429                   | Проверьте значение `OPENAI_API_KEY` / лимиты запросов.           |
| Ошибки при работе с Conda                 | Установите библиотеки Microsoft AI командой `conda install -c microsoft azure-ai-ml`|

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.