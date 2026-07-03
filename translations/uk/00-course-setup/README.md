# Початок роботи з цим курсом

Ми дуже раді, що ви починаєте цей курс і дізнаєтесь, що зможете створити за допомогою генеративного ШІ!

Щоб забезпечити ваш успіх, на цій сторінці наведено кроки налаштування, технічні вимоги та інформацію про те, де можна отримати допомогу, якщо буде потрібно.

## Кроки налаштування

Щоб почати цей курс, вам потрібно виконати наступні кроки.

### 1. Форкнути цей репозиторій

[Форкніть весь цей репозиторій](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) у свій власний акаунт GitHub, щоб мати змогу змінювати будь-який код і виконувати завдання. Ви також можете [поставити зірочку (🌟) цьому репозиторію](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), щоб легше знаходити його та пов’язані репозиторії.

### 2. Створіть codespace

Щоб уникнути проблем із залежностями під час запуску коду, ми рекомендуємо запускати цей курс у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У вашому форку: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/uk/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Додайте секрет

1. ⚙️ Іконка шестерні -> Command Pallete -> Codespaces: Manage user secret -> Add a new secret.
2. Назвіть його OPENAI_API_KEY, вставте свій ключ, збережіть.

### 3. Що далі?

| Я хочу…               | Перейти до…                                                            |
|-----------------------|------------------------------------------------------------------------|
| Почати урок 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Працювати офлайн      | [`setup-local.md`](02-setup-local.md)                                   |
| Налаштувати провайдера LLM | [`providers.md`](03-providers.md)                                   |
| Познайомитися з іншими учнями | [Приєднатися до нашого Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Вирішення проблем


| Симптом                                   | Виправлення                                                  |
|-------------------------------------------|--------------------------------------------------------------|
| Процес побудови контейнера затягнувся більше 10 хвилин   | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | Термінал не підключився; натисніть **+** ➜ *bash*            |
| `401 Unauthorized` від OpenAI             | Невірний або прострочений `OPENAI_API_KEY`                   |
| VS Code показує “Dev container mounting…”| Оновіть вкладку браузера — іноді Codespaces втрачає з’єднання |
| Відсутнє ядро блокнота                    | Меню блокнота ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Для Unix-подібних систем:

   ```bash
   touch .env
   ```

   Для Windows:

   ```cmd
   echo . > .env
   ```

3. **Редагуйте файл `.env`**: Відкрийте файл `.env` у текстовому редакторі (наприклад, VS Code, Notepad++ або інший редактор). Додайте наступний рядок у файл, замінивши `your_github_token_here` на ваш фактичний токен GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Збережіть файл**: Збережіть внесені зміни та закрийте текстовий редактор.

5. **Встановіть `python-dotenv`**: Якщо ви цього ще не зробили, потрібно встановити пакет `python-dotenv`, щоб завантажувати змінні середовища з файлу `.env` у вашу Python-програму. Ви можете встановити його за допомогою `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у вашому Python-скрипті**: У вашому Python-скрипті використайте пакет `python-dotenv` для завантаження змінних середовища з файлу `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Завантажити змінні оточення з файлу .env
   load_dotenv()

   # Отримати доступ до змінної GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ось і все! Ви успішно створили файл `.env`, додали свій токен GitHub і підключили його до своєї Python-програми.

## Як запускати локально на вашому комп’ютері

Для запуску коду локально у вас на комп’ютері має бути встановлена якась версія [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Щоб використати репозиторій, його потрібно клонувати:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Після того, як ви все завантажили, можете починати!

## Необов’язкові кроки

### Встановлення Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а також деяких пакетів.
Conda — це менеджер пакетів, який полегшує налаштування та перемикання між різними Python-[**віртуальними середовищами**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) і пакетами. Він також зручний для встановлення пакетів, недоступних через `pip`.

Ви можете дотримуватись [інструкції з встановлення MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) для установки.

Після встановлення Miniconda потрібно клонувати [репозиторій](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (якщо ви цього ще не зробили).

Далі потрібно створити віртуальне середовище. Щоб зробити це з Conda, створіть новий файл середовища (_environment.yml_). Якщо ви працюєте в Codespaces, створіть його в каталозі `.devcontainer`, тобто `.devcontainer/environment.yml`.

Заповніть файл середовища наступним кодом:

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

Якщо виникають помилки з conda, можна вручну встановити Microsoft AI Libraries, використавши команду в терміналі:

```
conda install -c microsoft azure-ai-ml
```

Файл середовища визначає необхідні залежності. `<environment-name>` — це назва, яку ви хочете використати для вашого Conda середовища, а `<python-version>` — версія Python, яку ви хочете використовувати, наприклад, `3` — це остання основна версія Python.

Після цього ви можете створити Conda середовище, виконавши команди нижче у командному рядку/терміналі

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer підшлях застосовується лише до налаштувань Codespace
conda activate ai4beg
```

За потреби зверніться до [інструкції по роботі з Conda середовищами](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Використання Visual Studio Code з розширенням підтримки Python

Для цього курсу ми рекомендуємо використовувати редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) з встановленим [розширенням для підтримки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Це радше рекомендація, а не обов’язкова вимога.

> **Примітка**: Відкривши репозиторій курсу у VS Code, ви матимете змогу налаштувати проєкт у контейнері. Це можливо завдяки спеціальному каталогу [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) у репозиторії курсу. Детальніше про це пізніше.

> **Примітка**: Після клонування та відкриття каталогу у VS Code автоматично з’явиться пропозиція встановити розширення підтримки Python.

> **Примітка**: Якщо VS Code запропонує повторно відкрити репозиторій у контейнері, відмовтесь від цієї пропозиції, щоб використовувати локально встановлену версію Python.

### Використання Jupyter у браузері

Ви також можете працювати над проєктом, використовуючи [середовище Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) прямо у браузері. Класичний Jupyter та [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) забезпечують зручне середовище розробки з автозаповненням, підсвічуванням коду тощо.

Щоб запустити Jupyter локально, відкрийте термінал/командний рядок, перейдіть до каталогу курсу і виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить інстанцію Jupyter, а URL для доступу буде показано у вікні командного рядка.

Після переходу за URL ви побачите план курсу та зможете переходити до будь-яких файлів `*.ipynb`. Наприклад, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск у контейнері

Альтернативою налаштуванню всього на вашому комп’ютері або використанню Codespace є використання [контейнера](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Спеціальна папка `.devcontainer` у репозиторії курсу дає можливість VS Code налаштовувати проєкт у контейнері. Поза Codespaces це вимагатиме встановлення Docker і дещо більше зусиль, тому ми рекомендуємо це тільки тим, хто має досвід роботи з контейнерами.

Один із найкращих способів безпечно зберігати свої API-ключі при роботі з GitHub Codespaces — це використання секретів Codespaces. Будь ласка, ознайомтеся з [керівництвом з керування секретами в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Уроки та технічні вимоги

Курс містить 6 уроків концептуального рівня та 6 уроків з кодування.

Для уроків з кодування ми використовуємо службу Azure OpenAI. Вам потрібен доступ до служби Azure OpenAI та ключ API для запуску цього коду. Ви можете подати заявку на доступ, [заповнивши цю форму](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Поки триває обробка вашої заявки, кожен урок із кодування також має файл `README.md`, у якому можна переглянути код та результати.

## Використання служби Azure OpenAI вперше

Якщо ви вперше працюєте з Azure OpenAI, будь ласка, дотримуйтесь цього посібника, як [створити та розгорнути ресурс Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Використання OpenAI API вперше

Якщо ви вперше працюєте з OpenAI API, будь ласка, ознайомтеся з посібником, як [створити та використовувати інтерфейс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Познайомтеся з іншими учнями

Ми створили канали в нашому офіційному [сервері AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для знайомства з іншими учнями. Це чудовий спосіб налагодити зв’язки з іншими однодумцями-підприємцями, розробниками, студентами та всіма, хто хоче підвищити рівень у генеративному ШІ.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проєкту також буде на цьому сервері Discord, щоб допомагати учням.

## Внесок у проєкт

Цей курс є ініціативою з відкритим кодом. Якщо ви бачите можливості для покращень або проблеми, будь ласка, створіть [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) або зареєструйте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проєкту стежитиме за усіма внесками. Внесок у проєкти з відкритим кодом — це чудовий спосіб розвивати кар’єру у галузі генеративного ШІ.

Більшість внесків вимагає від вас погодитися з Угодою про ліцензію для контриб’юторів (CLA), яка засвідчує, що ви маєте права і фактично передаєте нам права використовувати ваш внесок. Деталі читайте на сайті [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важливо: при перекладі тексту в цьому репозиторії, будь ласка, не використовуйте машинний переклад. Ми перевірятимемо переклади через спільноту, тому просимо брати участь у перекладах лише тих мов, якими ви володієте.

Коли ви створюєте pull request, бот CLA автоматично визначить, чи потрібно вам надати CLA, та відповідно позначить PR (наприклад, міткою, коментарем). Просто дотримуйтесь інструкцій бота. Вам це потрібно буде зробити лише один раз для всіх репозиторіїв, що використовують наш CLA.

Цей проєкт прийняв [Кодекс поведінки Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для додаткової інформації читайте FAQ Кодексу поведінки або звертайтесь на [Email opencode](opencode@microsoft.com) з будь-якими додатковими питаннями чи коментарями.

## Розпочнемо роботу!
Тепер, коли ви виконали всі необхідні кроки для завершення цього курсу, почнемо з [вступу до генеративного ШІ та великих мовних моделей (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу ШІ [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->