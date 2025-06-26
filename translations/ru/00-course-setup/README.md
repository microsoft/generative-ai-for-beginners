<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:35:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ru"
}
-->
# Начало работы с этим курсом

Мы очень рады, что вы начинаете этот курс, и с нетерпением ждем, что вы вдохновитесь на создание с помощью генеративного ИИ!

Чтобы обеспечить ваш успех, на этой странице изложены шаги по настройке, технические требования и информация о том, где получить помощь при необходимости.

## Шаги по настройке

Чтобы начать прохождение этого курса, вам нужно выполнить следующие шаги.

### 1. Форкните этот репозиторий

[Сделайте форк всего этого репозитория](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в свой собственный аккаунт GitHub, чтобы иметь возможность изменять любой код и выполнять задания. Вы также можете [поставить звезду (🌟) этому репозиторию](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), чтобы легче находить его и связанные репозитории.

### 2. Создайте codespace

Чтобы избежать проблем с зависимостями при запуске кода, мы рекомендуем запускать этот курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Это можно сделать, выбрав опцию `Code` в вашей форкнутой версии этого репозитория и выбрав опцию **Codespaces**.

![Диалоговое окно с кнопками для создания codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Хранение ваших API-ключей

Важно хранить ваши API-ключи в безопасности при создании любого типа приложения. Мы рекомендуем не хранить API-ключи непосредственно в вашем коде. Коммит этих данных в публичный репозиторий может привести к проблемам с безопасностью и даже нежелательным расходам, если они будут использованы злоумышленником. Вот пошаговое руководство по созданию файла `.env` для Python и добавлению `GITHUB_TOKEN`:

1. **Перейдите в каталог вашего проекта**: Откройте ваш терминал или командную строку и перейдите в корневой каталог вашего проекта, где вы хотите создать файл `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Создайте файл `.env`**: Используйте предпочитаемый текстовый редактор для создания нового файла с именем `.env`. Если вы используете командную строку, вы можете использовать `touch` (on Unix-based systems) or `echo` (в Windows):

   На системах Unix:
   ```bash
   touch .env
   ```

   В Windows:
   ```cmd
   echo . > .env
   ```

3. **Отредактируйте файл `.env`**: Откройте файл `.env` в текстовом редакторе (например, VS Code, Notepad++ или любом другом редакторе). Добавьте следующую строку в файл, заменив `your_github_token_here` вашим фактическим токеном GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сохраните файл**: Сохраните изменения и закройте текстовый редактор.

5. **Установите пакет `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` для загрузки переменных окружения из файла `.env` в ваше Python-приложение. Вы можете установить его с помощью `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Загрузите переменные окружения в ваш Python-скрипт**: В вашем Python-скрипте используйте пакет `python-dotenv` для загрузки переменных окружения из файла `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Вот и все! Вы успешно создали файл `.env`, добавили ваш токен GitHub и загрузили его в ваше Python-приложение.

## Как запустить локально на вашем компьютере

Чтобы запустить код локально на вашем компьютере, вам нужно иметь какую-то версию [Python установленной](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Затем, чтобы использовать репозиторий, вам нужно клонировать его:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Как только у вас все будет готово, вы можете приступать!

## Дополнительные шаги

### Установка Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — это легкий установщик для установки [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а также нескольких пакетов. Conda сама по себе является менеджером пакетов, который облегчает настройку и переключение между различными [**виртуальными окружениями**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакетами Python. Она также пригодится для установки пакетов, которые недоступны через `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Заполните ваш файл окружения следующим сниппетом:

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

Если вы столкнулись с ошибками при использовании conda, вы можете вручную установить библиотеки Microsoft AI, используя следующую команду в терминале.

```
conda install -c microsoft azure-ai-ml
```

Файл окружения указывает на зависимости, которые нам нужны. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` — это последняя основная версия Python.

После этого вы можете создать ваше окружение Conda, выполнив команды ниже в вашей командной строке/терминале

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Обратитесь к [руководству по окружениям Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), если у вас возникнут какие-либо проблемы.

### Использование Visual Studio Code с расширением поддержки Python

Мы рекомендуем использовать редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с установленным [расширением поддержки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) для этого курса. Однако это больше рекомендация, чем обязательное требование.

> **Примечание**: Открыв репозиторий курса в VS Code, у вас будет возможность настроить проект в контейнере. Это связано с [особой директорией `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), находящейся в репозитории курса. Подробнее об этом позже.

> **Примечание**: Как только вы клонируете и откроете директорию в VS Code, он автоматически предложит вам установить расширение поддержки Python.

> **Примечание**: Если VS Code предложит вам переоткрыть репозиторий в контейнере, откажитесь от этого предложения, чтобы использовать локально установленную версию Python.

### Использование Jupyter в браузере

Вы также можете работать над проектом, используя [среду Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо в вашем браузере. Как классический Jupyter, так и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставляют приятную среду разработки с такими функциями, как автозавершение, подсветка кода и т.д.

Чтобы запустить Jupyter локально, перейдите в терминал/командную строку, перейдите в директорию курса и выполните:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Это запустит экземпляр Jupyter, и URL для доступа к нему будет показан в окне командной строки.

Как только вы получите доступ к URL, вы должны увидеть план курса и сможете перейти к любому файлу `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, где вы можете просматривать код и результаты.

## Использование сервиса Azure OpenAI в первый раз

Если это ваш первый опыт работы с сервисом Azure OpenAI, пожалуйста, следуйте этому руководству о том, как [создать и развернуть ресурс сервиса Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Использование API OpenAI в первый раз

Если это ваш первый опыт работы с API OpenAI, пожалуйста, следуйте руководству о том, как [создать и использовать интерфейс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Встреча с другими учащимися

Мы создали каналы в нашем официальном [сервере Discord сообщества ИИ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для встреч с другими учащимися. Это отличный способ наладить связи с другими предпринимателями, строителями, студентами и всеми, кто хочет повысить свой уровень в генеративном ИИ.

[![Присоединиться к каналу Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекта также будет на этом сервере Discord, чтобы помочь учащимся.

## Вклад

Этот курс является инициативой с открытым исходным кодом. Если вы видите области для улучшения или проблемы, пожалуйста, создайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или зарегистрируйте [проблему на GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекта будет отслеживать все вклады. Внесение вклада в открытый исходный код — это удивительный способ построить свою карьеру в генеративном ИИ.

Большинство вкладов требуют, чтобы вы согласились с Соглашением о лицензировании вкладчика (CLA), заявляя, что вы имеете право и действительно предоставляете нам права на использование вашего вклада. Для получения подробной информации посетите [веб-сайт Соглашения о лицензировании вкладчика (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при переводе текста в этом репозитории, пожалуйста, убедитесь, что вы не используете машинный перевод. Мы будем проверять переводы через сообщество, поэтому, пожалуйста, участвуйте в переводах только на те языки, в которых вы разбираетесь.

Когда вы отправите запрос на слияние, CLA-бот автоматически определит, нужно ли вам предоставить CLA, и соответствующим образом украсит PR (например, меткой, комментарием). Просто следуйте инструкциям, предоставленным ботом. Вам нужно будет сделать это только один раз для всех репозиториев, использующих наш CLA.

Этот проект принял [Кодекс поведения Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для получения дополнительной информации прочитайте FAQ по Кодексу поведения или свяжитесь с [Email opencode](opencode@microsoft.com) с любыми дополнительными вопросами или комментариями.

## Давайте начнем

Теперь, когда вы завершили необходимые шаги для прохождения этого курса, давайте начнем с [введения в генеративный ИИ и LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Отказ от ответственности**:  
Этот документ был переведен с использованием службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.