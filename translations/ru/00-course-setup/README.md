# Начало работы с этим курсом

Мы очень рады, что вы начинаете этот курс и увидите, что вас вдохновит создать с помощью Генеративного ИИ!

Чтобы обеспечить ваш успех, на этой странице описаны шаги по настройке, технические требования и где можно получить помощь при необходимости.

## Шаги по настройке

Чтобы начать обучение на этом курсе, вам нужно выполнить следующие шаги.

### 1. Форкните этот репозиторий

[Сделайте форк всего репозитория](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в свой собственный аккаунт GitHub, чтобы иметь возможность изменять любой код и выполнять задания. Вы также можете [поставить звезду (🌟) этому репозиторию](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), чтобы проще было его находить и находить связанные репозитории.

### 2. Создайте codespace

Чтобы избежать проблем с зависимостями при запуске кода, мы рекомендуем запускать этот курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

В своём форке: **Code -> Codespaces -> New on main**

![Диалоговое окно с кнопками для создания codespace](../../../translated_images/ru/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавьте секрет

1. ⚙️ Иконка шестерёнки -> Command Pallete-> Codespaces : Управление пользовательскими секретами -> Добавить новый секрет.
2. Имя OPENAI_API_KEY, вставьте свой ключ, Сохранить.

### 3. Что дальше?

| Я хочу…             | Перейти к…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Начать урок 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работать оффлайн    | [`setup-local.md`](02-setup-local.md)                                   |
| Настроить провайдера LLM | [`providers.md`](03-providers.md)                                        |
| Познакомиться с другими учащимися | [Присоединиться к нашему Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Устранение неполадок


| Симптом                                   | Решение                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Сборка контейнера зависла > 10 мин       | **Codespaces ➜ «Пересобрать контейнер»**                      |
| `python: command not found`               | Терминал не прикрепился; нажмите **+** ➜ *bash*                |
| `401 Unauthorized` от OpenAI              | Неправильный / просроченный `OPENAI_API_KEY`                   |
| VS Code показывает «Dev container mounting…» | Обновите вкладку браузера — иногда Codespaces теряет соединение  |
| Отсутствует ядро блокнота                  | Меню блокнота ➜ **Kernel ▸ Выбрать ядро ▸ Python 3**           |

   Unix-подобные системы:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте файл `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом). Добавьте следующие строки в файл, заменяя заполнители на ваши реальные конечные точки и ключи Microsoft Foundry Models (см. [`providers.md`](03-providers.md) для получения информации, как их получить):

   > **Примечание:** GitHub Models (и переменная `GITHUB_TOKEN`) будет закрыт в конце июля 2026 года. Вместо этого используйте [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте текстовый редактор.

5. **Установите `python-dotenv`**: Если вы ещё не сделали этого, вам нужно установить пакет `python-dotenv`, чтобы загружать переменные окружения из файла `.env` в ваше Python-приложение. Его можно установить с помощью `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в вашем Python-скрипте**: В вашем Python-скрипте воспользуйтесь пакетом `python-dotenv` для загрузки переменных из файла `.env`:

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

Вот и всё! Вы успешно создали файл `.env`, добавили туда данные своей учётной записи Microsoft Foundry Models и загрузили их в своё Python-приложение.

## Как запускать локально на вашем компьютере

Для запуска кода локально на вашем компьютере потребуется установленная версия [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Чтобы использовать репозиторий, нужно его клонировать:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Как только все загрузится, вы можете начать работать!

## Дополнительные шаги

### Установка Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это лёгкий установщик для установки [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а также некоторых пакетов.
Сам Conda — это менеджер пакетов, который упрощает настройку и переключение между разными Python [**виртуальными окружениями**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакетами. Также он полезен для установки пакетов, недоступных через `pip`.

Вы можете следовать [руководству установки MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), чтобы настроить её.

После установки Miniconda нужно клонировать [репозиторий](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (если вы ещё этого не сделали)

Далее необходимо создать виртуальное окружение. Для этого с помощью Conda создайте новый файл окружения (_environment.yml_). Если вы используете Codespaces, создайте его в директории `.devcontainer`, то есть `.devcontainer/environment.yml`.

Заполните файл окружения следующим фрагментом:

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

Если у вас возникают ошибки при использовании conda, можно вручную установить Microsoft AI Libraries командой ниже в терминале.

```
conda install -c microsoft azure-ai-ml
```

Файл окружения задаёт необходимые зависимости. `<environment-name>` — имя вашего Conda-окружения, а `<python-version>` — используемая версия Python, например, `3` — последняя мажорная версия Python.

После этого создайте Conda-окружение, выполнив команды ниже в командной строке/терминале

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпуть .devcontainer применяется только к установкам Codespace
conda activate ai4beg
```

Обратитесь к [руководству по управлению окружениями Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), если возникнут проблемы.

### Использование Visual Studio Code с расширением поддержки Python

Для этого курса мы рекомендуем использовать редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с установленным [расширением поддержки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Однако это скорее рекомендация, а не обязательное требование.

> **Примечание**: Открыв репозиторий курса в VS Code, вы можете настроить проект внутри контейнера. Это возможно благодаря [специальной директории `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), которая находится в репозитории курса. Подробнее об этом далее.

> **Примечание**: После клонирования и открытия директории в VS Code он автоматически предложит установить расширение Python.

> **Примечание**: Если VS Code предложит открыть репозиторий в контейнере, отклоните запрос, чтобы использовать локально установленную версию Python.

### Использование Jupyter в браузере

Вы также можете работать над проектом через [среду Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо в браузере. И классический Jupyter, и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставляют удобную среду разработки с такими функциями, как автозаполнение, подсветка кода и так далее.

Чтобы запустить Jupyter локально, откройте терминал/командную строку, перейдите в папку с курсом и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит экземпляр Jupyter, и URL для доступа к нему будет выведен в командной строке.

По переходу по ссылке вы увидите план курса и сможете открыть любой файл с расширением `*.ipynb`. Например `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск в контейнере

Альтернативой настройке всего локально или на Codespace является использование [контейнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специальная папка `.devcontainer` в репозитории курса позволяет VS Code настроить проект внутри контейнера. За пределами Codespaces это потребует установки Docker и, честно говоря, немного усилий, поэтому мы рекомендуем этот путь только тем, кто уже работал с контейнерами.

Один из лучших способов обезопасить ваши API-ключи при использовании GitHub Codespaces — это использование Secrets в Codespace. Пожалуйста, ознакомьтесь с руководством по [управлению секретами в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Уроки и технические требования

Курс состоит из 6 концептуальных и 6 кодовых уроков.

Для кодовых уроков мы используем Azure OpenAI Service. Вам потребуется доступ к Azure OpenAI Service и API ключ для запуска кода. Вы можете подать заявку на доступ, [заполнив эту форму](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Пока вы ждёте обработки заявки, в каждом кодовом уроке есть файл `README.md`, где вы можете просмотреть код и результаты.

## Использование Azure OpenAI Service впервые

Если вы впервые работаете с Azure OpenAI Service, пожалуйста, следуйте руководству по [созданию и развертыванию ресурса Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Использование OpenAI API впервые

Если вы впервые работаете с OpenAI API, пожалуйста, следуйте руководству по [созданию и использованию интерфейса](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Познакомьтесь с другими учащимися

Мы создали каналы в нашем официальном [Discord-сервере AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для общения с другими учащимися. Это отличный способ наладить связи с другими единомышленниками, предпринимателями, разработчиками, студентами и всеми, кто хочет развиваться в Генеративном ИИ.

[![Присоединиться к Discord-каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекта также будет на этом Discord-сервере, чтобы помочь всем учащимся.

## Вклад в проект

Этот курс — инициатива с открытым исходным кодом. Если вы заметили области для улучшения или проблемы, пожалуйста, создайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или зарегистрируйте [проблему на GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекта будет отслеживать все вклады. Внесение вклада в открытое ПО — отличный способ построить карьеру в Генеративном ИИ.

Большинство вкладов требует согласия с Лицензионным соглашением с участником (CLA), в котором вы подтверждаете, что имеете право и фактически предоставляете нам права на использование вашего вклада. Подробнее смотрите на сайте [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при переводе текста в этом репозитории, пожалуйста, не используйте машинный перевод. Мы будем проверять переводы через сообщество, поэтому участвуйте в переводе только на тех языках, которыми вы владеете профессионально.

При отправке pull request, CLA-бот автоматически определит, нужно ли вам предоставить CLA и отметит PR соответствующим образом (например, ярлыком, комментарием). Просто следуйте инструкциям бота. Это нужно сделать только один раз для всех репозиториев, использующих наш CLA.


Этот проект принял [Кодекс поведения Microsoft с открытым исходным кодом](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для получения дополнительной информации прочитайте Часто задаваемые вопросы о Кодексе поведения или свяжитесь с [Email opencode](opencode@microsoft.com) для любых дополнительных вопросов или комментариев.

## Давайте начнем

Теперь, когда вы выполнили необходимые шаги для завершения этого курса, давайте начнем с [введения в генеративный ИИ и LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->