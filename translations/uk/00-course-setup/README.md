# Початок роботи з цим курсом

Ми дуже раді, що ви починаєте цей курс і хочемо побачити, що вас надихне створювати за допомогою Генеративного ШІ!

Щоб забезпечити ваш успіх, ця сторінка містить кроки налаштування, технічні вимоги та інформацію, де можна отримати допомогу у разі потреби.

## Кроки налаштування

Щоб почати проходити цей курс, вам потрібно виконати наступні кроки.

### 1. Форкніть це сховище

[Форкніть це сховище цілком](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) на свій власний обліковий запис GitHub, щоб мати змогу змінювати будь-який код і виконувати завдання. Також ви можете [поставити ⭐ цьому репозиторію](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), щоб легше знаходити його та пов’язані сховища.

### 2. Створіть codespace

Щоб уникнути проблем із залежностями під час запуску коду, ми рекомендуємо виконувати цей курс у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У вашому форку: **Code -> Codespaces -> New on main**

![Діалог, що показує кнопки для створення codespace](../../../translated_images/uk/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Додайте секрет

1. ⚙️ Іконка налаштувань -> Command Palette-> Codespaces : Керування секретами користувача -> Додати новий секрет.
2. Ім'я OPENAI_API_KEY, вставте свій ключ, Зберегти.

### 3. Що далі?

| Я хочу…              | Перейти до…                                                            |
|---------------------|-------------------------------------------------------------------------|
| Почати Урок 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Працювати офлайн     | [`setup-local.md`](02-setup-local.md)                                   |
| Налаштувати Провайдера LLM | [`providers.md`](03-providers.md)                                  |
| Познайомитись з іншими учнями| [Приєднатись до нашого Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Вирішення проблем


| Симптом                                  | Виправлення                                                    |
|------------------------------------------|----------------------------------------------------------------|
| Збірка контейнера зависає > 10 хв        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Терминал не прикріпився; натисніть **+** ➜ *bash*               |
| `401 Unauthorized` від OpenAI             | Неправильний / прострочений `OPENAI_API_KEY`                     |
| VS Code показує “Dev container mounting…”| Оновіть вкладку браузера — іноді Codespaces втрачає з’єднання   |
| Відсутнє ядро ноутбука                    | Меню ноутбука ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Системи на основі Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Редагуйте файл `.env`**: Відкрийте файл `.env` у текстовому редакторі (наприклад, VS Code, Notepad++ або будь-якому іншому). Додайте до файлу наступні рядки, замінивши заповнювачі на ваш дійсний кінцевий пункт і ключ Microsoft Foundry Models (див. [`providers.md`](03-providers.md) для отримання інформації як їх отримати):

   > **Примітка:** GitHub Models (і змінна `GITHUB_TOKEN`) припиняють роботу наприкінці липня 2026 року. Замість них використовуйте [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Збережіть файл**: Збережіть зміни і закрийте текстовий редактор.

5. **Встановіть `python-dotenv`**: Якщо ви ще не встановили його, вам потрібно буде встановити пакет `python-dotenv`, щоб завантажувати змінні середовища з файлу `.env` у вашу Python-програму. Ви можете встановити його за допомогою `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Завантажте змінні середовища у ваш Python-скрипт**: У вашому Python-скрипті використовуйте пакет `python-dotenv` для завантаження змінних середовища з файлу `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Завантажити змінні оточення з файлу .env
   load_dotenv()

   # Отримати доступ до змінних Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Ось і все! Ви успішно створили файл `.env`, додали до нього облікові дані Microsoft Foundry Models і завантажили їх у вашу Python-застосунок.

## Як запустити локально на вашому комп’ютері

Щоб запускати код локально на вашому комп’ютері, вам потрібно мати встановлену деяку версію [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Щоб використовувати репозиторій, його потрібно клонувати:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Коли у вас буде все готово, можете починати!

## Додаткові кроки

### Встановлення Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) — це легкий інсталятор для встановлення [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, а також кількох пакетів.
Conda — це менеджер пакетів, який полегшує налаштування та перемикання між різними [віртуальними середовищами](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python і пакетами. Також він корисний для встановлення пакетів, яких немає у `pip`.

Ви можете дотримуватися [керівництва із встановлення MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Після встановлення Miniconda вам потрібно клонувати [репозиторій](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (якщо ви ще цього не зробили).

Далі потрібно створити віртуальне середовище. Для цього з Conda створіть файл середовища (_environment.yml_). Якщо ви користуєтеся Codespaces, створіть його у каталозі `.devcontainer`, тобто `.devcontainer/environment.yml`.

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

Якщо виникають помилки при використанні conda, ви можете вручну встановити Microsoft AI Libraries, використовуючи таку команду в терміналі.

```
conda install -c microsoft azure-ai-ml
```

Файл середовища визначає залежності, які нам потрібні. `<environment-name>` — це назва середовища Conda, яку ви хочете використовувати, а `<python-version>` — це версія Python, яку ви хочете встановити, наприклад, `3` — остання основна версія Python.

Після цього створіть Conda-середовище, виконавши наведені команди у командному рядку / терміналі.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Підшлях .devcontainer застосовується лише до налаштувань Codespace
conda activate ai4beg
```

Якщо виникають проблеми, дивіться [керівництво по Conda-середовищах](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Використання Visual Studio Code з розширенням підтримки Python

Для цього курсу ми рекомендуємо використовувати редактор [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) з встановленим [розширенням підтримки Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Проте це рекомендація, а не жорстка вимога.

> **Примітка**: Відкривши репозиторій курсу у VS Code, ви маєте можливість налаштувати проєкт у контейнері. Це можливо завдяки спеціальній директорії [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) всередині репозиторію. Детальніше про це пізніше.

> **Примітка**: Після клонування та відкриття каталогу у VS Code, редактор автоматично запропонує встановити розширення підтримки Python.

> **Примітка**: Якщо VS Code запропонує вам відкрити репозиторій у контейнері, відмовтесь від цієї пропозиції, щоб використовувати локально встановлену версію Python.

### Використання Jupyter у браузері

Ви також можете працювати над проектом, використовуючи середовище [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) безпосередньо у вашому браузері. Класичний Jupyter і [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) забезпечують приємне середовище розробки з такими функціями, як автозаповнення, підсвічування коду і т. ін.

Щоб запустити Jupyter локально, відкрийте термінал/командний рядок, перейдіть у каталог курсу і виконайте:

```bash
jupyter notebook
```

або

```bash
jupyterhub
```

Це запустить екземпляр Jupyter, і URL для доступу буде показаний у вікні командного рядка.

Коли ви перейдете за URL, побачите структуру курсу та зможете переходити до будь-якого файлу `*.ipynb`. Наприклад, `08-building-search-applications/python/oai-solution.ipynb`.

### Запуск у контейнері

Альтернативою встановленню у вашому комп’ютері чи Codespace є використання [контейнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Спеціальна папка `.devcontainer` у репозиторії курсу дозволяє VS Code налаштувати проєкт у контейнері. За межами Codespaces це потребує встановлення Docker і, чесно кажучи, це досить складно, тому ми рекомендуємо цей варіант лише тим, хто має досвід роботи з контейнерами.

Один із найкращих способів зберегти ключі API в безпеці під час використання GitHub Codespaces — це використання секретів Codespace. Будь ласка, ознайомтеся з керівництвом [керування секретами Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Уроки та технічні вимоги

Курс містить 6 концептуальних уроків та 6 уроків програмування.

Для уроків програмування ми використовуємо Azure OpenAI Service. Вам потрібен доступ до сервісу Azure OpenAI та ключ API для запуску цього коду. Ви можете подати заявку на доступ, [заповнивши цю форму](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Поки ваша заявка опрацьовується, кожен урок програмування також містить файл `README.md`, де можна переглянути код і результати.

## Використання Azure OpenAI Service вперше

Якщо ви вперше працюєте із Azure OpenAI service, будь ласка, дотримуйтесь цього посібника як [створити та розгорнути ресурс Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Використання OpenAI API вперше

Якщо ви вперше працюєте з OpenAI API, дотримуйтесь керівництва як [створити і використовувати Інтерфейс](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Познайомтесь з іншими учнями

Ми створили канали в нашому офіційному [AI Community Discord сервері](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) для знайомств з іншими учнями. Це чудовий спосіб познайомитись з однодумцями — підприємцями, розробниками, студентами та всіма, хто прагне піднятися на новий рівень у Генеративному ШІ.

[![Приєднатись до каналу discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Команда проєкту також буде на цьому Discord-сервері, щоб допомагати учням.

## Внесок

Цей курс є ініціативою з відкритим кодом. Якщо ви бачите можливості для покращення чи помилки, будь ласка, створіть [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) або зареєструйте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Команда проєкту відстежуватиме всі внески. Участь у відкритому коді — це чудовий спосіб розвивати кар’єру у сфері Генеративного ШІ.

Більшість внесків вимагає погодження з Угодою ліцензії контриб'ютора (CLA), в якій ви заявляєте про право і реальне надання нам прав на використання вашого внеску. Детальніше дивіться на [вебсайті CLA, Угода ліцензії контриб'ютора](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важливо: при перекладі тексту у цьому репозиторії просимо не використовувати машинний переклад. Ми перевірятимемо переклади через спільноту, тому просимо братися лише за переклади мов, якими ви володієте професійно.

Коли ви створюєте pull request, CLA-бот автоматично визначить, чи потрібно вам надавати CLA, і відповідно позначить PR (наприклад, міткою чи коментарем). Просто дотримуйтесь інструкцій бота. Це потрібно буде зробити лише один раз для всіх репозиторіїв, що використовують нашу CLA.


Цей проєкт прийняв [Кодекс поведінки відкритого коду Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Для отримання додаткової інформації прочитайте FAQ щодо Кодексу поведінки або зв’яжіться з [Email opencode](opencode@microsoft.com) з будь-якими додатковими питаннями чи коментарями.

## Почнемо

Оскільки ви виконали необхідні кроки для проходження цього курсу, давайте почнемо з [вступу до генеративного ШІ та LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->