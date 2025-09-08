<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T13:51:40+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ru"
}
-->
# Начало работы с этим курсом

Мы очень рады, что вы начинаете этот курс, и с нетерпением ждем, что вас вдохновит создать с помощью генеративного ИИ!

Чтобы вы успешно прошли курс, на этой странице описаны шаги по настройке, технические требования и информация о том, где можно получить помощь при необходимости.

## Шаги по настройке

Чтобы приступить к курсу, выполните следующие шаги.

### 1. Форкните этот репозиторий

[Сделайте форк этого репозитория](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в свой аккаунт GitHub, чтобы иметь возможность изменять код и выполнять задания. Вы также можете [поставить звезду (🌟) этому репозиторию](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), чтобы проще находить его и связанные репозитории.

### 2. Создайте codespace

Чтобы избежать проблем с зависимостями при запуске кода, рекомендуем проходить курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

В вашем форке: **Code -> Codespaces -> New on main**

![Диалоговое окно с кнопками для создания codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Добавьте секрет

1. ⚙️ Значок шестеренки -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Назовите OPENAI_API_KEY, вставьте ваш ключ, Сохраните.

### 3.  Что дальше?

| Я хочу…              | Перейти…                                                                |
|----------------------|-------------------------------------------------------------------------|
| Начать урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работать офлайн      | [`setup-local.md`](02-setup-local.md)                                   |
| Настроить LLM-провайдера | [`providers.md`](providers.md)                                      |
| Познакомиться с другими участниками | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Решение проблем


| Симптом                                   | Решение                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Сборка контейнера зависла > 10 мин         | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Терминал не подключился; нажмите **+** ➜ *bash*                |
| `401 Unauthorized` от OpenAI              | Неверный / истекший `OPENAI_API_KEY`                           |
| VS Code показывает “Dev container mounting…” | Обновите вкладку браузера — Codespaces иногда теряет соединение|
| Ядро ноутбука отсутствует                 | Меню ноутбука ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Для систем на базе Unix:

   ```bash
   touch .env
   ```

   Для Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте файл `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом). Добавьте следующую строку, заменив `your_github_token_here` на ваш реальный токен GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте редактор.

5. **Установите `python-dotenv`**: Если вы еще не сделали этого, установите пакет `python-dotenv`, чтобы загружать переменные окружения из файла `.env` в ваше Python-приложение. Установить можно через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в вашем Python-скрипте**: В вашем скрипте используйте пакет `python-dotenv` для загрузки переменных из файла `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Вы успешно создали файл `.env`, добавили туда токен GitHub и загрузили его в ваше Python-приложение.

## Как запустить локально на вашем компьютере

Чтобы запустить код локально, вам потребуется установить [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Чтобы использовать репозиторий, его нужно склонировать:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Когда все готово, можно приступать!

## Дополнительные шаги

### Установка Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это легкий установщик для [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и некоторых пакетов.
Conda — это менеджер пакетов, который облегчает настройку и переключение между разными [**виртуальными окружениями**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакетами Python. Также он полезен для установки пакетов, которых нет в `pip`.

Следуйте [инструкции по установке MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), чтобы настроить его.

После установки Miniconda склонируйте [репозиторий](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (если вы еще не сделали этого).

Далее создайте виртуальное окружение. Для этого с помощью Conda создайте новый файл окружения (_environment.yml_). Если вы работаете в Codespaces, создайте его в директории `.devcontainer`, то есть `.devcontainer/environment.yml`.

Заполните файл окружения следующим образом:

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

Если при работе с conda возникают ошибки, можно вручную установить библиотеки Microsoft AI с помощью следующей команды в терминале.

```
conda install -c microsoft azure-ai-ml
```

Файл окружения указывает необходимые зависимости. `<environment-name>` — это имя вашего окружения Conda, а `<python-version>` — версия Python, например, `3` — это последняя основная версия.

Теперь можно создать окружение Conda, выполнив команды ниже в командной строке/терминале

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Если возникнут вопросы, обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Использование Visual Studio Code с расширением поддержки Python

Рекомендуем использовать редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с установленным [расширением поддержки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) для этого курса. Это рекомендация, а не обязательное требование.

> **Note**: Открыв репозиторий курса в VS Code, вы можете настроить проект внутри контейнера. Это возможно благодаря [специальной директории `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) в репозитории курса. Подробнее об этом позже.

> **Note**: После клонирования и открытия директории в VS Code, редактор автоматически предложит установить расширение поддержки Python.

> **Note**: Если VS Code предложит открыть репозиторий в контейнере, отклоните это предложение, чтобы использовать локально установленную версию Python.

### Использование Jupyter в браузере

Вы также можете работать над проектом в [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо в браузере. Классический Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставляют удобную среду разработки с автодополнением, подсветкой кода и другими функциями.

Чтобы запустить Jupyter локально, откройте терминал/командную строку, перейдите в директорию курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит Jupyter, и в командной строке появится URL для доступа.

Перейдя по этому URL, вы увидите структуру курса и сможете открыть любой файл `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск в контейнере

Альтернативой настройке на компьютере или в Codespace является использование [контейнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специальная папка `.devcontainer` в репозитории курса позволяет VS Code настроить проект внутри контейнера. Вне Codespaces для этого потребуется установка Docker, и это довольно трудоемко, поэтому рекомендуем этот способ только тем, кто уже работал с контейнерами.

Один из лучших способов хранить ваши API-ключи в безопасности при работе с GitHub Codespaces — использовать Codespace Secrets. Ознакомьтесь с [руководством по управлению секретами Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), чтобы узнать больше.


## Уроки и технические требования

В курсе 6 теоретических уроков и 6 практических.

Для практических уроков используется Azure OpenAI Service. Для запуска кода вам потребуется доступ к Azure OpenAI и API-ключ. Получить доступ можно, [заполнив заявку](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Пока ваша заявка обрабатывается, в каждом практическом уроке есть файл `README.md`, где можно посмотреть код и результаты.

## Первое использование Azure OpenAI Service

Если вы впервые работаете с Azure OpenAI, следуйте этому руководству по [созданию и развертыванию ресурса Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Первое использование OpenAI API

Если вы впервые работаете с OpenAI API, следуйте [руководству по созданию и использованию интерфейса.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Познакомьтесь с другими участниками

Мы создали каналы на нашем официальном [Discord-сервере AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для общения с другими участниками. Это отличный способ познакомиться с единомышленниками — предпринимателями, разработчиками, студентами и всеми, кто хочет развиваться в генеративном ИИ.

[![Присоединиться к Discord-каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекта также будет на этом сервере, чтобы помогать участникам.

## Внесите вклад

Этот курс — инициатива с открытым исходным кодом. Если вы видите, что можно что-то улучшить или нашли ошибку, создайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или опишите проблему в [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекта отслеживает все вклады. Участие в open source — отличный способ развивать карьеру в генеративном ИИ.

Для большинства вкладов потребуется согласиться с Contributor License Agreement (CLA), подтверждающим, что вы имеете право и действительно предоставляете нам права на использование вашего вклада. Подробнее — на [сайте CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при переводе текста в этом репозитории, пожалуйста, не используйте машинный перевод. Мы будем проверять переводы через сообщество, поэтому участвуйте только в переводах на те языки, которыми владеете.

Когда вы отправляете pull request, CLA-bot автоматически определит, нужно ли вам предоставить CLA, и пометит PR соответствующим образом (например, меткой или комментарием). Просто следуйте инструкциям бота. Это нужно сделать только один раз для всех репозиториев, использующих наш CLA.

В этом проекте действует [Кодекс поведения Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Подробнее читайте в FAQ по Кодексу поведения или пишите на [Email opencode](opencode@microsoft.com) с вопросами и комментариями.

## Приступим!
Теперь, когда вы выполнили все необходимые шаги для прохождения этого курса, давайте начнем с [введения в генеративный ИИ и большие языковые модели (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несём ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.