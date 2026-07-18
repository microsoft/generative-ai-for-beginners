# Начало работы с этим курсом

Мы очень рады, что вы начинаете этот курс и увидите, что вдохновит вас создавать с помощью генеративного ИИ!

Чтобы обеспечить ваш успех, на этой странице описаны шаги по настройке, технические требования и информация о том, где получить помощь при необходимости.

## Шаги настройки

Чтобы начать этот курс, вам нужно выполнить следующие шаги.

### 1. Форкнуть этот репозиторий

[Форкните весь этот репозиторий](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в свой аккаунт GitHub, чтобы иметь возможность изменять код и выполнять задания. Также вы можете [поставить звезду (🌟) этому репозиторию](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), чтобы легче находить его и связанные репозитории.

### 2. Создать codespace

Чтобы избежать проблем с зависимостями при запуске кода, мы рекомендуем запускать этот курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

В вашем форке: **Code -> Codespaces -> New on main**

![Диалоговое окно с кнопками для создания codespace](../../../translated_images/ru/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавить секрет

1. ⚙️ Иконка шестеренки -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Назовите его OPENAI_API_KEY, вставьте свой ключ, Сохраните.

### 3. Что дальше?

| Я хочу…              | Перейти к…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Начать урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работать офлайн      | [`setup-local.md`](02-setup-local.md)                                   |
| Настроить поставщика LLM | [`providers.md`](03-providers.md)                                        |
| Познакомиться с другими учащимися | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Решение проблем


| Симптом                                   | Решение                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Сборка контейнера застряла > 10 мин       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | Терминал не подключился; нажмите **+** ➜ *bash*                |
| `401 Unauthorized` от OpenAI                | Неправильный / просроченный `OPENAI_API_KEY`                    |
| VS Code показывает «Dev container mounting…» | Обновите вкладку браузера — Codespaces иногда теряет соединение |
| Отсутствует ядро ноутбука                  | Меню ноутбука ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Системы на базе Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте файл `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом). Добавьте в файл следующие строки, заменив заполнители на действительные конечную точку и ключ Microsoft Foundry Models (смотрите [`providers.md`](03-providers.md) для информации, как их получить):

   > **Примечание:** GitHub Models (и переменная `GITHUB_TOKEN`) будет закрыт в конце июля 2026 года. Используйте вместо него [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте текстовый редактор.

5. **Установите `python-dotenv`**: Если вы еще этого не сделали, установите пакет `python-dotenv`, чтобы загружать переменные окружения из файла `.env` в ваше Python-приложение. Это можно сделать с помощью `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в вашем Python-скрипте**: В вашем Python-скрипте используйте пакет `python-dotenv` для загрузки переменных из файла `.env`:

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

Всё! Вы успешно создали файл `.env`, добавили туда учетные данные Microsoft Foundry Models и загрузили их в своё Python-приложение.

## Как запускать локально на вашем компьютере

Чтобы запускать код локально на вашем компьютере, необходимо иметь установленную версию [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Чтобы использовать репозиторий, вам нужно его клонировать:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

После того, как вы всё скачали, можно приступать!

## Дополнительные шаги

### Установка Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это легкий установщик для установки [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и нескольких пакетов.
Сам Conda — это менеджер пакетов, который облегчает настройку и переключение между разными [виртуальными окружениями](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python и пакетами. Также он пригодится для установки пакетов, недоступных через `pip`.

Вы можете следовать [руководству по установке MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) для настройки.

После установки Miniconda нужно клонировать [репозиторий](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (если вы ещё не сделали этого)

Далее нужно создать виртуальное окружение. Для этого с Conda создайте новый файл окружения (_environment.yml_). Если вы используете Codespaces, разместите этот файл в директории `.devcontainer`, то есть `.devcontainer/environment.yml`.

Заполните ваш файл окружения следующим фрагментом:

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

Если возникают ошибки с Conda, вы можете вручную установить библиотеки Microsoft AI с помощью следующей команды в терминале.

```
conda install -c microsoft azure-ai-ml
```

Файл окружения указывает необходимые зависимости. `<environment-name>` — имя вашего Conda-окружения, `<python-version>` — версия Python, которую вы хотите использовать, например, `3` — последняя основная версия Python.

После этого создайте окружение Conda, выполнив следующие команды в командной строке/терминале

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпуть .devcontainer применяется только к настройкам Codespace
conda activate ai4beg
```

Обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), если столкнетесь с проблемами.

### Использование Visual Studio Code с расширением поддержки Python

Для этого курса мы рекомендуем использовать редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с установленным [расширением поддержки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Однако это лишь рекомендация, а не обязательное требование.

> **Примечание**: Открыв репозиторий курса в VS Code, у вас появится возможность установить проект внутри контейнера благодаря специальной директории [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) в репозитории курса. Об этом чуть позже.

> **Примечание**: После клонирования и открытия директории в VS Code вам автоматически предложат установить расширение поддержки Python.

> **Примечание**: Если VS Code предложит повторно открыть репозиторий в контейнере, отклоните это предложение, чтобы использовать локально установленную версию Python.

### Использование Jupyter в браузере

Вы также можете работать над проектом, используя среду [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо в браузере. Как классический Jupyter, так и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставляют приятную среду разработки с автодополнением, подсветкой кода и прочим.

Чтобы запустить Jupyter локально, откройте терминал или командную строку, перейдите в директорию курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит экземпляр Jupyter, и URL для доступа к нему будет показан в окне командной строки.

Открыв этот URL, вы увидите оглавление курса и сможете перейти к любому файлу `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск в контейнере

Альтернатива установке на компьютере или в Codespace — использование [контейнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специальная папка `.devcontainer` в репозитории курса позволяет VS Code настроить проект в контейнере. Вне Codespaces потребуется установка Docker, и, честно говоря, это немного сложнее, поэтому мы рекомендуем это только тем, кто уже имеет опыт работы с контейнерами.

Один из лучших способов сохранить ваши API-ключи в безопасности при использовании GitHub Codespaces — использовать секреты Codespace. Ознакомьтесь с [руководством по управлению секретами Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), чтобы узнать больше.


## Уроки и технические требования

В курсе есть уроки "Учимся", которые объясняют концепции генеративного ИИ, и уроки "Строим" с практическими примерами кода на **Python** и **TypeScript**, где это возможно.

Для уроков по программированию мы используем Azure OpenAI в Microsoft Foundry. Вам понадобится подписка Azure и API-ключ. Доступ открыт — заявление не требуется — вы можете [создать ресурс Microsoft Foundry и развернуть модель](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), чтобы получить конечную точку и ключ.

Каждый урок по программированию также включает файл `README.md`, в котором можно посмотреть код и результаты без запуска.

## Использование Azure OpenAI Service впервые

Если вы впервые работаете с Azure OpenAI Service, пожалуйста, следуйте этому руководству по [созданию и развертыванию ресурса Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Использование OpenAI API впервые

Если вы впервые работаете с OpenAI API, следуйте руководству по [созданию и использованию интерфейса](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Познакомьтесь с другими учащимися

Мы создали каналы в нашем официальном [Discord-сервере сообщества AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для знакомства с другими учениками. Это отличный способ познакомиться с единомышленниками — предпринимателями, разработчиками, студентами и всеми, кто хочет прокачать себя в генеративном ИИ.

[![Присоединиться к каналу discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекта также будет на этом Discord-сервере, чтобы помогать учащимся.

## Вклад в проект

Этот курс — проект с открытым исходным кодом. Если вы видите области для улучшения или ошибки, пожалуйста, создайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или зарегистрируйте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекта отслеживает все вклады. Участие в open source — отличный способ построить карьеру в генеративном ИИ.

Большинство вклады требуют согласия с Лицензионным соглашением для вклада (CLA), которое подтверждает, что вы имеете право и действительно предоставляете нам права на использование вашего вклада. Подробнее смотрите на сайте [CLA, Лицензионное соглашение для участников](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при переводе текста в этом репозитории, пожалуйста, не используйте машинный перевод. Мы будем проверять переводы сообществом, поэтому беритесь за переводы только на тех языках, которыми вы владеете хорошо.


Когда вы создаете pull request, CLA-бот автоматически определит, нужно ли вам предоставить CLA, и соответствующим образом отметит PR (например, меткой, комментарием). Просто следуйте инструкциям, предоставленным ботом. Вам нужно будет сделать это только один раз для всех репозиториев, использующих наш CLA.

Этот проект принял [Кодекс поведения с открытым исходным кодом Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для получения дополнительной информации прочитайте FAQ по Кодексу поведения или свяжитесь с [Email opencode](opencode@microsoft.com) для любых дополнительных вопросов или комментариев.

## Начнем

Теперь, когда вы выполнили необходимые шаги для завершения этого курса, начнем с [введения в генеративный ИИ и большие языковые модели](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->