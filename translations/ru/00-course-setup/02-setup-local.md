# Локальная настройка 🖥️

**Используйте это руководство, если предпочитаете запускать всё на своём ноутбуке.**   
У вас есть два варианта: **(A) нативный Python + виртуальное окружение** или **(B) VS Code Dev Container с Docker**.  
Выберите любой, какой покажется проще — оба ведут к одним и тем же урокам.

## 1. Требования

| Инструмент           | Версия / Примечания                                                                  |
|----------------------|--------------------------------------------------------------------------------------|
| **Python**           | 3.10+ (скачайте с <https://python.org>)                                              |
| **Git**              | Последняя версия (входит в Xcode / Git для Windows / пакетный менеджер Linux)         |
| **VS Code**          | Опционально, но рекомендуется <https://code.visualstudio.com>                         |
| **Docker Desktop**   | *Только* для варианта B. Бесплатная установка: <https://docs.docker.com/desktop/>     |

> 💡 **Совет** – Проверьте инструменты в терминале:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Вариант А – Нативный Python (быстрее всего)

### Шаг 1 Клонируйте этот репозиторий

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Шаг 2 Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv          # сделать один
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Теперь приглашение командной строки должно начинаться с (.venv) — значит, вы в виртуальном окружении.

### Шаг 3 Установите зависимости

```bash
pip install -r requirements.txt
```

Перейдите к разделу 3 про [API ключи](#3-добавьте-свои-api-ключи)

## 2. Вариант B – VS Code Dev Container (Docker)

Мы подготовили этот репозиторий и курс с помощью [dev container](https://containers.dev?WT.mc_id=academic-105485-koreyst), который обеспечивает универсальную среду выполнения для разработки на Python3, .NET, Node.js и Java. Конфигурация описана в файле `devcontainer.json`, расположенном в папке `.devcontainer/` в корне репозитория.

>**Почему выбрать этот способ?**
>Среда полностью идентична Codespaces; отсутствует разбежка зависимостей.

### Шаг 0 Установите дополнительное ПО

Docker Desktop – проверьте, что команда ```docker --version``` работает.
Расширение VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Шаг 1 Откройте репозиторий в VS Code

Файл ▸ Открыть папку…  → generative-ai-for-beginners

VS Code обнаружит `.devcontainer/` и покажет всплывающее окно.

### Шаг 2 Повторно открыть в контейнере

Нажмите «Reopen in Container». Docker собирает образ (≈ 3 минуты при первом запуске).
Когда появится приглашение терминала, вы внутри контейнера.

## 2. Вариант C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — лёгкий установщик для [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и нескольких пакетов.
Сам Conda — это менеджер пакетов, который облегчает создание и переключение между разными Python [виртуальными окружениями](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакетами. Он также полезен для установки пакетов, отсутствующих в `pip`.

### Шаг 0 Установите Miniconda

Следуйте [инструкции по установке MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Шаг 1 Создайте виртуальное окружение

Создайте файл окружения (*environment.yml*). Если вы работаете с Codespaces, создайте его внутри папки `.devcontainer`, то есть `.devcontainer/environment.yml`.

### Шаг 2 Заполните файл окружения

Добавьте следующий фрагмент в `environment.yml`

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
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпуть .devcontainer применяется только к настройкам Codespace
conda activate ai4beg
```

Обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), если возникнут проблемы.

## 2 Вариант D – Классический Jupyter / Jupyter Lab (в браузере)

> **Для кого это?**  
> Для тех, кто предпочитает классический интерфейс Jupyter или хочет запускать ноутбуки без VS Code.  

### Шаг 1 Убедитесь, что Jupyter установлен

Чтобы запустить Jupyter локально, откройте терминал/командную строку, перейдите в каталог курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Запустится экземпляр Jupyter, URL для доступа к нему отобразится в окне командной строки.

После доступа по URL вы увидите структуру курса и сможете открыть любой файл `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Добавьте свои API ключи

Важно хранить API ключи в безопасности при разработке любых приложений. Рекомендуем не сохранять ключи напрямую в коде. Выкладка этих данных в публичный репозиторий может привести к проблемам с безопасностью и нежелательным расходам, если ключи попадут к злоумышленникам.
Вот пошаговое руководство, как создать файл `.env` для Python и добавить ваши учетные данные Microsoft Foundry Models:

> **Примечание:** GitHub Models (и переменная `GITHUB_TOKEN`) будет закрыт в конце июля 2026. Это руководство использует [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Предпочитаете полностью офлайн? Смотрите [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Перейдите в каталог проекта**: Откройте терминал или командную строку и перейдите в корневой каталог вашего проекта, где создадите файл `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Создайте файл `.env`**: Используйте любимый текстовый редактор для создания файла с именем `.env`. В командной строке можно использовать `touch` (на Unix) или `echo` (на Windows):

   На Unix-системах:

   ```bash
   touch .env
   ```

   На Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом). Добавьте следующие строки, заменив заполнители на реальные данные вашего проекта Microsoft Foundry и API ключ:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте редактор.

5. **Установите `python-dotenv`**: Если ещё не сделали, установите пакет `python-dotenv`, чтобы загружать переменные окружения из файла `.env` в ваше Python-приложение. Установите через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в скрипте Python**: В вашем скрипте используйте пакет `python-dotenv`, чтобы загрузить переменные из `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Загрузить переменные окружения из файла .env
   load_dotenv()

   # Получить доступ к переменным Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Вот и всё! Вы успешно создали `.env` файл, добавили учетные данные Microsoft Foundry Models и загрузили их в Python-приложение.

🔐 Никогда не коммитьте `.env` — он уже добавлен в `.gitignore`.
Полные инструкции от провайдера доступны в [`providers.md`](03-providers.md).

## 4. Что дальше?

| Я хочу…               | Перейти к…                                                             |
|-----------------------|------------------------------------------------------------------------|
| Начать урок 1          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Настроить провайдера LLM | [`providers.md`](03-providers.md)                                     |
| Познакомиться с другими учениками | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Устранение неполадок

| Симптом                                   | Решение                                                         |
|-------------------------------------------|----------------------------------------------------------------|
| `python не найден`                        | Добавьте Python в PATH или перезапустите терминал после установки |
| `pip` не может собрать колёса (Windows)   | Выполните `pip install --upgrade pip setuptools wheel` и повторите попытку. |
| `ModuleNotFoundError: dotenv`             | Выполните `pip install -r requirements.txt` (окружение не установлено). |
| Сбой сборки Docker *No space left*        | Docker Desktop ▸ *Настройки* ▸ *Ресурсы* → увеличьте размер диска. |
| VS Code постоянно предлагает повторно открыть | Возможно, активны оба варианта; выберите один (venv **или** контейнер) |
| Ошибки OpenAI 401 / 429                    | Проверьте значение `OPENAI_API_KEY` / лимиты запросов.           |
| Ошибки при использовании Conda            | Установите библиотеки Microsoft AI через `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->