# Начало работы с этим курсом

Мы очень рады, что вы начинаете этот курс и увидите, что вас вдохновит создать с помощью генеративного ИИ!

Чтобы обеспечить ваш успех, на этой странице описаны шаги настройки, технические требования и места, где можно получить помощь при необходимости.

## Шаги настройки

Чтобы начать этот курс, вам нужно выполнить следующие шаги.

### 1. Форкнуть этот репозиторий

[Сделайте форк всего репозитория](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в свой собственный аккаунт GitHub, чтобы иметь возможность изменять код и выполнять задания. Вы также можете [поставить звезду (🌟) этому репозиторию](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), чтобы проще было его и связанные репозитории находить.

### 2. Создайте codespace

Чтобы избежать проблем с зависимостями при запуске кода, мы рекомендуем запускать этот курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

В вашем форке: **Code -> Codespaces -> New on main**

![Диалоговое окно с кнопками для создания codespace](../../../translated_images/ru/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавьте секрет

1. ⚙️ Значок шестеренки -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Назовите OPENAI_API_KEY, вставьте ваш ключ, Сохраните.

### 3. Что дальше?

| Я хочу…             | Перейти в…                                                                 |
|---------------------|---------------------------------------------------------------------------|
| Начать урок 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| Работать офлайн     | [`setup-local.md`](02-setup-local.md)                                      |
| Настроить поставщика LLM | [`providers.md`](03-providers.md)                                         |
| Познакомиться с другими обучающимися | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Устранение неполадок


| Симптом                                   | Исправление                                                     |
|-------------------------------------------|-----------------------------------------------------------------|
| Сборка контейнера застряла > 10 мин       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Терминал не подключился; нажмите **+** ➜ *bash*                 |
| `401 Unauthorized` от OpenAI              | Неправильный или истекший `OPENAI_API_KEY`                      |
| VS Code показывает «Dev container mounting…»   | Обновите вкладку браузера — Codespaces иногда теряет соединение  |
| Отсутствует ядро в ноутбуке                | Меню ноутбука ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Для Unix-подобных систем:

   ```bash
   touch .env
   ```

   Для Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте файл `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом редакторе). Добавьте следующую строку, заменив `your_github_token_here` на ваш реальный токен GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте редактор.

5. **Установите `python-dotenv`**: Если вы ещё не сделали этого, установите пакет `python-dotenv`, который загружает переменные окружения из файла `.env` в ваше Python-приложение. Установить можно с помощью `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в вашем Python-скрипте**: В вашем Python-скрипте используйте пакет `python-dotenv` для загрузки переменных окружения из файла `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Загрузить переменные окружения из файла .env
   load_dotenv()

   # Получить доступ к переменной GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Вот и всё! Вы успешно создали файл `.env`, добавили в него ваш GitHub токен и загрузили его в ваше Python-приложение.

## Как запускать локально на вашем компьютере

Чтобы запускать код локально на компьютере, вам нужно иметь установленный [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Чтобы использовать репозиторий, его нужно клонировать:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

После того как вы всё скачали, можете начинать!

## Необязательные шаги

### Установка Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это лёгкий установщик для установки [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а также некоторых пакетов.
Conda — это менеджер пакетов, который облегчает настройку и переключение между разными [виртуальными окружениями](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python и пакетами. Он также полезен для установки пакетов, которых нет в `pip`.

Вы можете следовать [руководству по установке Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) для настройки.

С установленным Miniconda вам нужно клонировать [репозиторий](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (если вы ещё не сделали это).

Далее нужно создать виртуальное окружение. Для этого с помощью Conda создайте новый файл окружения (_environment.yml_). Если вы работаете в Codespaces, создайте его внутри директории `.devcontainer`, то есть `.devcontainer/environment.yml`.

Заполните ваш файл окружения сниппетом ниже:

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

Если при использовании conda вы получаете ошибки, можно вручную установить библиотеки Microsoft AI с помощью следующей команды в терминале.

```
conda install -c microsoft azure-ai-ml
```

Файл окружения указывает зависимости, которые нам нужны. `<environment-name>` — это имя, которое вы хотите использовать для окружения Conda, а `<python-version>` — версия Python, которую вы хотите использовать; например, `3` — последняя основная версия Python.

Когда всё готово, создайте ваше окружение Conda, выполнив команды ниже в командной строке/терминале

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпуть .devcontainer применяется только к настройкам Codespace
conda activate ai4beg
```

Обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), если возникнут проблемы.

### Использование Visual Studio Code с расширением поддержки Python

Мы рекомендуем использовать редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с установленным [расширением поддержки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) для этого курса. Однако это скорее рекомендация, а не обязательное требование.

> **Примечание**: Открыв репозиторий курса в VS Code, вы можете настроить проект в контейнере. Это возможно благодаря [специальной директории `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), которая есть в репозитории курса. Подробнее об этом позже.

> **Примечание**: После клонирования и открытия директории в VS Code он автоматически предложит установить расширение поддержки Python.

> **Примечание**: Если VS Code предложит переоткрыть репозиторий в контейнере, отклоните это, чтобы использовать локально установленный Python.

### Использование Jupyter в браузере

Вы также можете работать над проектом в [среде Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо в браузере. Как классический Jupyter, так и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставляют удобную среду разработки с такими функциями, как автодополнение, подсветка кода и др.

Чтобы запустить Jupyter локально, откройте терминал/командную строку, перейдите в директорию курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит инстанс Jupyter, URL для доступа к нему будет показан в окне командной строки.

Перейдя по URL, вы увидите структуру курса и сможете открыть любой файл `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск в контейнере

Альтернативой настройке всего на вашем компьютере или в Codespace является использование [контейнера](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). Специальная папка `.devcontainer` в репозитории курса позволяет VS Code настроить проект в контейнере. За пределами Codespaces для этого потребуется установка Docker, и, честно говоря, это требует определённых навыков, поэтому мы рекомендуем такой способ только тем, кто уже имеет опыт работы с контейнерами.

Один из лучших способов обеспечить безопасность ваших API-ключей при использовании GitHub Codespaces — использовать Секреты Codespace. Пожалуйста, следуйте руководству по [управлению секретами в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), чтобы узнать больше.

## Уроки и технические требования

В курсе 6 концептуальных и 6 практических уроков.

Для практических уроков мы используем Azure OpenAI Service. Для запуска кода вам понадобится доступ к Azure OpenAI service и API-ключ. Вы можете подать заявку на доступ, [заполнив эту форму](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Пока ваша заявка рассматривается, в каждом практическом уроке есть файл `README.md`, где вы можете ознакомиться с кодом и результатами.

## Использование Azure OpenAI Service впервые

Если вы впервые используете Azure OpenAI service, пожалуйста, следуйте этому руководству, чтобы [создать и развернуть ресурс Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Использование OpenAI API впервые

Если вы впервые работаете с OpenAI API, пожалуйста, ознакомьтесь с руководством, как [создавать и использовать интерфейс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Познакомьтесь с другими обучающимися

Мы создали каналы в нашем официальном [AI сообществе Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для знакомства с другими обучающимися. Это отличный способ познакомиться с другими единомышленниками, предпринимателями, разработчиками, студентами и всеми, кто хочет повысить свои знания в генеративном ИИ.

[![Присоединиться к каналу discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекта будет также в этом Discord-сервере для помощи обучающимся.

## Вклад в проект

Этот курс — инициативы с открытым исходным кодом. Если вы видите возможность улучшений или ошибки, пожалуйста, создайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или зарегистрируйте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекта отслеживает все вклады. Вклад в open source — отличный способ развивать карьеру в генеративном ИИ.

Большинство вкладов требуют согласия с Лицензионным соглашением для участников (CLA), где вы подтверждаете свое право и действительно даёте нам права на использование вашего вклада. Подробности на сайте [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при переводе текста в этом репозитории не используйте машинный перевод. Мы проверим переводы через сообщество, поэтому участвуйте только в переводах на тех языках, на которых вы хорошо владеете.

После создания pull request, бот CLA автоматически определит, нужно ли вам предоставить CLA и отметит PR соответствующе (например, меткой или комментарием). Просто следуйте инструкциям бота. Это нужно будет сделать только один раз для всех репозиториев, использующих нашу CLA.

Проект принял [Кодекс поведения Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Подробнее о этом читайте в FAQ или свяжитесь по Email opencode (opencode@microsoft.com) для дополнительных вопросов или комментариев.

## Давайте начинать!
Теперь, когда вы выполнили необходимые шаги для завершения этого курса, давайте начнем с [введения в генеративный ИИ и большие языковые модели (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его языке является официальным и приоритетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или ошибки в интерпретации, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->