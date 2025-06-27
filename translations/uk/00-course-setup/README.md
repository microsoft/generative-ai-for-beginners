<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:03:23+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "uk"
}
-->
# Початок роботи з цим курсом

Ми дуже раді, що ви починаєте цей курс, і з нетерпінням чекаємо, що ви надихнетеся створити з Генеративним ШІ!

Щоб забезпечити ваш успіх, на цій сторінці описані кроки налаштування, технічні вимоги та місця, де можна отримати допомогу, якщо це потрібно.

## Кроки налаштування

Щоб почати проходити цей курс, вам потрібно виконати наступні кроки.

### 1. Форкніть цей репозиторій

[Форкніть весь цей репозиторій](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) у свій власний обліковий запис GitHub, щоб мати можливість змінювати будь-який код і виконувати завдання. Ви також можете [додати зірочку (🌟) цьому репозиторію](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), щоб легше знаходити його та пов'язані репозиторії.

### 2. Створіть кодовий простір

Щоб уникнути будь-яких проблем із залежностями при запуску коду, ми рекомендуємо запускати цей курс у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Це можна зробити, вибравши опцію `Code` у вашій форкнутій версії цього репозиторію та обравши опцію **Codespaces**.

![Діалогове вікно, що показує кнопки для створення кодового простору](../../../00-course-setup/images/who-will-pay.webp)

### 3. Зберігання ваших API ключів

Забезпечення безпеки та захисту ваших API ключів важливо при створенні будь-якого типу додатків. Ми рекомендуємо не зберігати API ключі безпосередньо в коді. Занесення цих даних до публічного репозиторію може призвести до проблем з безпекою та навіть небажаних витрат, якщо їх використовує зловмисник. Ось покрокова інструкція, як створити файл `.env` для Python і додати `GITHUB_TOKEN`:

1. **Перейдіть до каталогу вашого проекту**: Відкрийте ваш термінал або командний рядок і перейдіть до кореневого каталогу вашого проекту, де ви хочете створити файл `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Створіть файл `.env`**: Використовуйте ваш улюблений текстовий редактор, щоб створити новий файл з назвою `.env`. Якщо ви використовуєте командний рядок, ви можете використати `touch` (on Unix-based systems) or `echo` (на Windows):

   Unix-подібні системи:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Редагуйте файл `.env`**: Відкрийте файл `.env` у текстовому редакторі (наприклад, VS Code, Notepad++ або будь-якому іншому редакторі). Додайте наступний рядок до файлу, замінивши `your_github_token_here` вашим фактичним токеном GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Збережіть файл**: Збережіть зміни та закрийте текстовий редактор.

5. **Встановіть пакет `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, щоб завантажити змінні середовища з файлу `.env` у ваш Python-додаток. Ви можете встановити його за допомогою `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у вашому Python-скрипті**: У вашому Python-скрипті використовуйте пакет `python-dotenv`, щоб завантажити змінні середовища з файлу `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

От і все! Ви успішно створили файл `.env`, додали ваш GitHub-токен і завантажили його у ваш Python-додаток.

## Як запустити локально на вашому комп'ютері

Щоб запустити код локально на вашому комп'ютері, вам потрібно мати деяку версію [Python встановлену](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Потім, щоб використовувати репозиторій, вам потрібно клонувати його:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Після того, як ви все перевірили, можете починати!

## Додаткові кроки 

### Встановлення Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а також кількох пакетів. Conda сама по собі є менеджером пакетів, що робить легким налаштування та переключення між різними [**віртуальними середовищами**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python і пакетами. Вона також зручна для встановлення пакетів, які недоступні через `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Заповніть ваш файл середовища фрагментом нижче:

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

Якщо ви отримуєте помилки при використанні conda, ви можете вручну встановити бібліотеки Microsoft AI, використовуючи наступну команду в терміналі.

```
conda install -c microsoft azure-ai-ml
```

Файл середовища вказує на залежності, які нам потрібні. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` — це остання основна версія Python.

З цим завершено, ви можете створити ваше Conda середовище, виконавши команди нижче у вашому командному рядку/терміналі

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Зверніться до [керівництва по середовищам Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), якщо ви зіткнулися з будь-якими проблемами.

### Використання Visual Studio Code з розширенням підтримки Python

Ми рекомендуємо використовувати редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) з встановленим [розширенням підтримки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) для цього курсу. Однак це більше рекомендація, ніж обов'язкова вимога.

> **Примітка**: Відкривши репозиторій курсу у VS Code, у вас є можливість налаштувати проект у контейнері. Це через [спеціальну `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) директорію, що знаходиться у репозиторії курсу. Більше про це пізніше.

> **Примітка**: Як тільки ви клонували та відкрили директорію у VS Code, він автоматично запропонує вам встановити розширення підтримки Python.

> **Примітка**: Якщо VS Code пропонує вам повторно відкрити репозиторій у контейнері, відхиліть цю пропозицію, щоб використовувати локально встановлену версію Python.

### Використання Jupyter у браузері

Ви також можете працювати над проектом, використовуючи [Jupyter середовище](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо у вашому браузері. І класичний Jupyter, і [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) забезпечують досить приємне середовище для розробки з такими функціями, як автозаповнення, підсвічування коду тощо.

Щоб запустити Jupyter локально, перейдіть до терміналу/командного рядка, перейдіть до каталогу курсу та виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить інстанцію Jupyter, і URL для доступу до неї буде показано у вікні командного рядка.

Після доступу до URL ви повинні побачити структуру курсу і мати можливість перейти до будь-якого файлу `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, де ви можете переглянути код і результати.

## Використання служби Azure OpenAI вперше

Якщо це ваш перший раз роботи з сервісом Azure OpenAI, будь ласка, дотримуйтесь цього керівництва щодо [створення та розгортання ресурсу Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Використання OpenAI API вперше

Якщо це ваш перший раз роботи з OpenAI API, будь ласка, дотримуйтесь керівництва щодо [створення та використання інтерфейсу.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Зустрічайте інших учасників

Ми створили канали на нашому офіційному [сервері Discord спільноти AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для зустрічі з іншими учасниками. Це чудовий спосіб налагодити контакти з іншими підприємцями, розробниками, студентами та будь-ким, хто хоче підвищити свій рівень у Генеративному ШІ.

[![Приєднатися до каналу Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проекту також буде на цьому сервері Discord, щоб допомагати учасникам.

## Внесок

Цей курс є ініціативою з відкритим вихідним кодом. Якщо ви бачите області для покращення або проблеми, будь ласка, створіть [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) або зареєструйте [проблему на GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проекту буде відстежувати всі внески. Внесок у відкритий код — це чудовий спосіб побудувати вашу кар'єру в Генеративному ШІ.

Більшість внесків вимагає від вас згоди з Угодою про ліцензію учасника (CLA), що підтверджує, що ви маєте право та дійсно надаєте нам права на використання вашого внеску. Для деталей відвідайте [вебсайт CLA, Угода про ліцензію учасника](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важливо: при перекладі тексту в цьому репозиторії, будь ласка, переконайтеся, що ви не використовуєте машинний переклад. Ми перевіримо переклади через спільноту, тому, будь ласка, тільки добровольцями для перекладів мовами, в яких ви володієте.

Коли ви надсилаєте запит на злиття, бот CLA автоматично визначить, чи потрібно вам надати CLA, і відповідно відмітить PR (наприклад, міткою, коментарем). Просто дотримуйтесь інструкцій, наданих ботом. Вам потрібно буде зробити це лише один раз для всіх репозиторіїв, які використовують наш CLA.

Цей проект прийняв [Кодекс поведінки відкритого коду Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для отримання додаткової інформації прочитайте FAQ Кодексу поведінки або зв'яжіться з [Email opencode](opencode@microsoft.com) з будь-якими додатковими питаннями або коментарями.

## Почнемо

Тепер, коли ви виконали необхідні кроки для завершення цього курсу, давайте почнемо з [вступу до Генеративного ШІ та LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу AI-перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо точності, будь ласка, майте на увазі, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.