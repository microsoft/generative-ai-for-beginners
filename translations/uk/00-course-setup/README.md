<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T20:05:45+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "uk"
}
-->
# Початок роботи з цим курсом

Ми дуже раді, що ви починаєте цей курс, і з нетерпінням чекаємо, що ви створите, надихнувшись генеративним ШІ!

Щоб допомогти вам досягти успіху, на цій сторінці описані кроки налаштування, технічні вимоги та інформація, де можна отримати допомогу, якщо це буде потрібно.

## Кроки налаштування

Щоб почати проходити цей курс, вам потрібно виконати наступні кроки.

### 1. Форкніть цей репозиторій

[Зробіть форк цього репозиторію](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) у свій обліковий запис GitHub, щоб мати змогу змінювати код і виконувати завдання. Також ви можете [додати зірочку (🌟) цьому репозиторію](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), щоб легше знаходити його та пов’язані репозиторії.

### 2. Створіть codespace

Щоб уникнути проблем із залежностями під час запуску коду, рекомендуємо проходити цей курс у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У вашому форку: **Code -> Codespaces -> New on main**

![Діалогове вікно з кнопками для створення codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Додайте секрет

1. ⚙️ Іконка шестерні -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Назвіть OPENAI_API_KEY, вставте свій ключ, Збережіть.

### 3. Що далі?

| Я хочу…              | Перейти до…                                                              |
|----------------------|--------------------------------------------------------------------------|
| Почати урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Працювати офлайн     | [`setup-local.md`](02-setup-local.md)                                    |
| Налаштувати LLM-провайдера | [`providers.md`](providers.md)                                 |
| Познайомитися з іншими учасниками | [Приєднатися до нашого Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Вирішення проблем


| Симптом                                   | Рішення                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Збірка контейнера триває > 10 хв           | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Термінал не підключився; натисніть **+** ➜ *bash*              |
| `401 Unauthorized` від OpenAI             | Неправильний або прострочений `OPENAI_API_KEY`                 |
| VS Code показує “Dev container mounting…” | Оновіть вкладку браузера — Codespaces іноді втрачає з’єднання  |
| Відсутнє ядро для ноутбука                | Меню ноутбука ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Для Unix-подібних систем:

   ```bash
   touch .env
   ```

   Для Windows:

   ```cmd
   echo . > .env
   ```

3. **Відредагуйте файл `.env`**: Відкрийте файл `.env` у текстовому редакторі (наприклад, VS Code, Notepad++ або будь-якому іншому). Додайте наступний рядок у файл, замінивши `your_github_token_here` на ваш реальний GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Збережіть файл**: Збережіть зміни та закрийте редактор.

5. **Встановіть `python-dotenv`**: Якщо ви ще не зробили цього, потрібно встановити пакет `python-dotenv`, щоб завантажувати змінні середовища з файлу `.env` у ваш Python-додаток. Встановити можна через `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у вашому Python-скрипті**: У вашому Python-скрипті використайте пакет `python-dotenv`, щоб завантажити змінні середовища з файлу `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Ви успішно створили файл `.env`, додали свій GitHub токен і завантажили його у свій Python-додаток.

## Як запускати локально на вашому комп’ютері

Щоб запускати код локально на вашому комп’ютері, потрібно мати встановлений [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Щоб скористатися репозиторієм, потрібно його клонувати:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Після того, як усе буде скопійовано, можна починати!

## Додаткові кроки

### Встановлення Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python та кількох пакетів.
Conda — це менеджер пакетів, який спрощує налаштування та перемикання між різними [**віртуальними середовищами**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python і пакетами. Також він зручний для встановлення пакетів, які недоступні через `pip`.

Ви можете скористатися [інструкцією з встановлення MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), щоб налаштувати його.

Після встановлення Miniconda потрібно клонувати [репозиторій](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (якщо ви ще цього не зробили).

Далі потрібно створити віртуальне середовище. Для цього з Conda створіть новий файл середовища (_environment.yml_). Якщо ви працюєте у Codespaces, створіть його у директорії `.devcontainer`, тобто `.devcontainer/environment.yml`.

Заповніть файл середовища наступним фрагментом:

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

Якщо у вас виникають помилки при використанні conda, ви можете вручну встановити бібліотеки Microsoft AI за допомогою наступної команди у терміналі.

```
conda install -c microsoft azure-ai-ml
```

Файл середовища визначає потрібні залежності. `<environment-name>` — це назва, яку ви хочете дати своєму середовищу Conda, а `<python-version>` — версія Python, яку ви хочете використовувати, наприклад, `3` — це остання основна версія Python.

Після цього ви можете створити своє середовище Conda, виконавши наступні команди у командному рядку/терміналі

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Якщо виникнуть проблеми, зверніться до [інструкції з роботи з середовищами Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Використання Visual Studio Code з розширенням для Python

Рекомендуємо використовувати редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) з встановленим [розширенням для підтримки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) для цього курсу. Проте це лише рекомендація, а не обов’язкова вимога.

> **Note**: Відкривши репозиторій курсу у VS Code, ви можете налаштувати проєкт у контейнері. Це можливо завдяки [спеціальній директорії `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), яка є у репозиторії курсу. Детальніше про це — далі.

> **Note**: Після клонування та відкриття директорії у VS Code, редактор автоматично запропонує встановити розширення для підтримки Python.

> **Note**: Якщо VS Code запропонує відкрити репозиторій у контейнері, відхиліть цю пропозицію, щоб використовувати локально встановлену версію Python.

### Використання Jupyter у браузері

Ви також можете працювати над проєктом у [середовищі Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо у браузері. Класичний Jupyter і [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) забезпечують зручне середовище розробки з автодоповненням, підсвічуванням коду тощо.

Щоб запустити Jupyter локально, відкрийте термінал/командний рядок, перейдіть у директорію курсу та виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить екземпляр Jupyter, і у вікні командного рядка з’явиться URL для доступу.

Після переходу за цим URL ви побачите структуру курсу і зможете відкрити будь-який файл `*.ipynb`. Наприклад, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск у контейнері

Альтернативою налаштуванню всього на комп’ютері чи у Codespace є використання [контейнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Спеціальна папка `.devcontainer` у репозиторії курсу дозволяє VS Code налаштувати проєкт у контейнері. За межами Codespaces для цього потрібно встановити Docker, і це трохи складніше, тому рекомендуємо цей варіант лише тим, хто вже має досвід роботи з контейнерами.

Один із найкращих способів зберігати ваші API-ключі у безпеці при використанні GitHub Codespaces — це використовувати Codespace Secrets. Будь ласка, ознайомтеся з [інструкцією з керування секретами Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), щоб дізнатися більше.

## Уроки та технічні вимоги

Курс містить 6 теоретичних уроків і 6 практичних.

Для практичних уроків ми використовуємо Azure OpenAI Service. Щоб запускати цей код, вам потрібен доступ до Azure OpenAI service і API-ключ. Ви можете подати заявку на доступ, [заповнивши цю форму](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Поки ваша заявка розглядається, у кожному практичному уроці є файл `README.md`, де можна переглянути код і результати.

## Використання Azure OpenAI Service вперше

Якщо ви вперше працюєте з Azure OpenAI service, скористайтеся цією інструкцією, щоб [створити та розгорнути ресурс Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Використання OpenAI API вперше

Якщо ви вперше працюєте з OpenAI API, скористайтеся інструкцією, як [створити та використовувати інтерфейс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Познайомтеся з іншими учасниками

Ми створили канали на нашому офіційному [Discord сервері AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для знайомства з іншими учасниками. Це чудова можливість познайомитися з однодумцями — підприємцями, розробниками, студентами та всіма, хто хоче розвиватися у сфері генеративного ШІ.

[![Приєднатися до каналу discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проєкту також буде на цьому Discord сервері, щоб допомагати учасникам.

## Долучайтеся до розвитку

Цей курс — відкрита ініціатива. Якщо ви бачите, що можна щось покращити або знайшли проблему, створіть [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) або залиште [issue на GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проєкту відстежує всі внески. Долучення до open source — чудовий спосіб розвивати свою кар’єру у сфері генеративного ШІ.

Більшість внесків вимагають погодження Contributor License Agreement (CLA), яким ви підтверджуєте, що маєте право і дійсно надаєте нам права використовувати ваш внесок. Детальніше — на [сайті CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важливо: при перекладі тексту в цьому репозиторії, будь ласка, не використовуйте машинний переклад. Ми перевірятимемо переклади через спільноту, тому долучайтеся до перекладу лише мовами, якими ви володієте.

Коли ви створюєте pull request, CLA-bot автоматично визначить, чи потрібно вам підписати CLA, і позначить PR відповідним чином (наприклад, додасть мітку чи коментар). Просто дотримуйтесь інструкцій від бота. Це потрібно зробити лише один раз для всіх репозиторіїв, які використовують наш CLA.

У цьому проєкті діє [Кодекс поведінки Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для додаткової інформації ознайомтеся з FAQ Кодексу поведінки або звертайтеся на [Email opencode](opencode@microsoft.com) з додатковими питаннями чи коментарями.

## Почнемо!
Тепер, коли ви виконали всі необхідні кроки для проходження цього курсу, давайте розпочнемо з [вступу до генеративного ШІ та LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.