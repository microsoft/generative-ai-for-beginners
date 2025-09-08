<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:20:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bg"
}
-->
# Начало на този курс

Много се радваме, че започваш този курс и нямаме търпение да видим какво ще те вдъхнови да създадеш с Генеративен AI!

За да си гарантираш успех, на тази страница ще намериш стъпките за настройка, техническите изисквания и информация къде да потърсиш помощ при нужда.

## Стъпки за настройка

За да започнеш курса, трябва да изпълниш следните стъпки.

### 1. Форкни това репо

[Форкни цялото това репо](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в твоя GitHub акаунт, за да можеш да променяш кода и да изпълняваш задачите. Можеш също да [добавиш звезда (🌟) на това репо](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), за да го намираш по-лесно, както и свързаните с него репота.

### 2. Създай codespace

За да избегнеш проблеми с зависимости при стартиране на кода, препоръчваме да използваш [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) за този курс.

Във форкнатото репо: **Code -> Codespaces -> New on main**

![Диалогов прозорец с бутони за създаване на codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Добави secret

1. ⚙️ Икона на зъбно колело -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Име OPENAI_API_KEY, постави своя ключ, Запази.

### 3. Какво следва?

| Искам да…           | Отиди на…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Да започна Урок 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Да работя офлайн    | [`setup-local.md`](02-setup-local.md)                                    |
| Да настроя LLM доставчик | [`providers.md`](providers.md)                                      |
| Да се запозная с други участници | [Присъедини се към нашия Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Отстраняване на проблеми

| Симптом                                   | Решение                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| Създаването на контейнер отнема > 10 мин  | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Терминалът не се е свързал; натисни **+** ➜ *bash*               |
| `401 Unauthorized` от OpenAI              | Грешен/изтекъл `OPENAI_API_KEY`                                  |
| VS Code показва “Dev container mounting…” | Опресни таба на браузъра—понякога Codespaces губи връзка         |
| Липсва ядро на Notebook                   | Меню Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактирай файла `.env`**: Отвори файла `.env` в текстов редактор (например VS Code, Notepad++ или друг). Добави следния ред във файла, като замениш `your_github_token_here` с твоя реален GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Запази файла**: Запази промените и затвори редактора.

5. **Инсталирай `python-dotenv`**: Ако още не си, трябва да инсталираш пакета `python-dotenv`, за да зареждаш променливите на средата от `.env` файла в Python приложението си. Можеш да го инсталираш с `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Зареди променливите на средата в Python скрипта си**: В Python скрипта си използвай пакета `python-dotenv`, за да заредиш променливите от `.env` файла:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Готово! Успешно създаде `.env` файл, добави своя GitHub токен и го зареди в Python приложението си.

## Как да стартираш локално на компютъра си

За да стартираш кода локално, трябва да имаш инсталирана някаква версия на [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

След това трябва да клонираш репозиторито:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

След като всичко е изтеглено, можеш да започнеш!

## Допълнителни стъпки

### Инсталиране на Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и някои основни пакети.
Conda е мениджър на пакети, който улеснява създаването и превключването между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Също така е полезен за инсталиране на пакети, които не са налични чрез `pip`.

Можеш да следваш [ръководството за инсталиране на MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), за да го настроиш.

След като Miniconda е инсталиран, трябва да клонираш [репозиторито](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако още не си го направил).

Следващата стъпка е да създадеш виртуална среда. За да го направиш с Conda, създай нов файл за средата (_environment.yml_). Ако работиш в Codespaces, създай го в директорията `.devcontainer`, т.е. `.devcontainer/environment.yml`.

Попълни файла за средата със следния код:

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

Ако срещнеш грешки с conda, можеш ръчно да инсталираш Microsoft AI Libraries с тази команда в терминала:

```
conda install -c microsoft azure-ai-ml
```

Файлът за средата определя нужните зависимости. `<environment-name>` е името, което искаш да дадеш на Conda средата си, а `<python-version>` е версията на Python, която искаш да използваш, например `3` е последната основна версия.

След това можеш да създадеш Conda средата си, като изпълниш следните команди в терминала:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ако имаш проблеми, виж [ръководството за среди в Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Използване на Visual Studio Code с разширение за Python

Препоръчваме да използваш [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с инсталирано [разширение за Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за този курс. Това е препоръка, не задължително изискване.

> **Note**: Като отвориш репозиторито на курса във VS Code, имаш възможност да го настроиш в контейнер. Това е възможно благодарение на [специалната директория `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) в репозиторито. Повече за това по-късно.

> **Note**: След като клонираш и отвориш директорията във VS Code, ще ти бъде предложено автоматично да инсталираш разширението за Python.

> **Note**: Ако VS Code ти предложи да отвориш репозиторито в контейнер, откажи, за да използваш локално инсталирания Python.

### Използване на Jupyter в браузъра

Можеш да работиш по проекта и чрез [Jupyter среда](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно в браузъра си. Класическият Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предлагат приятна среда за разработка с функции като автодовършване, оцветяване на кода и др.

За да стартираш Jupyter локално, отвори терминал/команден ред, отиди в директорията на курса и изпълни:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира Jupyter и ще покаже URL адреса за достъп в прозореца на терминала.

След като отвориш този адрес, ще видиш структурата на курса и ще можеш да навигираш до всеки `*.ipynb` файл. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Стартиране в контейнер

Алтернатива на настройката на компютъра или в Codespace е използването на [контейнер](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специалната папка `.devcontainer` в репозиторито позволява на VS Code да настрои проекта в контейнер. Извън Codespaces това изисква инсталиране на Docker и е малко по-сложно, затова го препоръчваме само на хора с опит с контейнери.

Един от най-добрите начини да пазиш API ключовете си сигурни при използване на GitHub Codespaces е чрез Codespace Secrets. Следвай [ръководството за управление на secrets в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), за да научиш повече.

## Уроци и технически изисквания

Курсът включва 6 концептуални и 6 практически урока.

За практическите уроци използваме Azure OpenAI Service. Ще ти трябва достъп до Azure OpenAI и API ключ, за да стартираш кода. Можеш да кандидатстваш за достъп, като [попълниш тази заявка](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Докато чакаш заявката ти да бъде обработена, всеки практически урок съдържа и файл `README.md`, където можеш да разгледаш кода и резултатите.

## Първи стъпки с Azure OpenAI Service

Ако за първи път работиш с Azure OpenAI, следвай това ръководство как да [създадеш и разположиш ресурс за Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Първи стъпки с OpenAI API

Ако за първи път работиш с OpenAI API, следвай ръководството как да [създадеш и използваш интерфейса.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Запознай се с други участници

Създадохме канали в нашия официален [AI Community Discord сървър](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), където можеш да се запознаеш с други участници. Това е чудесен начин да се свържеш с други предприемачи, създатели, студенти и всички, които искат да се развиват в Генеративен AI.

[![Присъедини се към discord канала](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Екипът на проекта също ще бъде в този Discord сървър, за да помага на участниците.

## Приноси

Този курс е с отворен код. Ако забележиш нещо за подобряване или проблем, създай [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или докладвай [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Екипът на проекта ще следи всички приноси. Приносът към отворен код е чудесен начин да развиеш кариерата си в Генеративен AI.

Повечето приноси изискват да се съгласиш с Contributor License Agreement (CLA), с което декларираш, че имаш право да предоставиш приноса си и ни даваш права да го използваме. За повече информация посети [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при превод на текстове в това репо, моля не използвай машинен превод. Ще проверяваме преводите чрез общността, затова се включвай само за езици, които владееш добре.

Когато изпратиш pull request, CLA-bot автоматично ще определи дали трябва да подпишеш CLA и ще отбележи PR-а (например с етикет или коментар). Просто следвай инструкциите на бота. Това се прави само веднъж за всички репозита, използващи нашия CLA.

Този проект следва [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За повече информация прочети FAQ за Code of Conduct или пиши на [Email opencode](opencode@microsoft.com) при въпроси или коментари.

## Да започваме!
След като вече сте изпълнили необходимите стъпки за завършване на този курс, нека започнем с [въведение в Генеративния AI и LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали от използването на този превод.