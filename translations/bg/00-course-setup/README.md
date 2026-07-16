# Започване с този курс

Много се радваме, че започвате този курс и ще видите какво ще ви вдъхнови да създадете с Генеративен AI!

За да гарантираме вашия успех, тази страница описва стъпките за настройка, техническите изисквания и къде да потърсите помощ при нужда.

## Стъпки за настройка

За да започнете този курс, ще трябва да изпълните следните стъпки.

### 1. Форкнете този репо

[Форкнете това цялостно репо](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) във вашия GitHub акаунт, за да можете да променяте код и да изпълнявате предизвикателствата. Можете също да [добавите звездичка (🌟) на това репо](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), за да го намирате по-лесно заедно със свързани репозитории.

### 2. Създайте Codespace

За да избегнете проблеми с зависимости при стартиране на кода, препоръчваме да използвате този курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Във вашия fork: **Code -> Codespaces -> New on main**

![Диалог, показващ бутони за създаване на codespace](../../../translated_images/bg/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавете секретен ключ

1. ⚙️ Икона зъбно колело -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Име OPENAI_API_KEY, поставете вашия ключ, Запазете.

### 3. Какво следва?

| Искам да…           | Отиди на…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Започна урок 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работя офлайн       | [`setup-local.md`](02-setup-local.md)                                   |
| Настройка на LLM доставчик | [`providers.md`](03-providers.md)                                        |
| Срещна други учащи | [Присъединете се към Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Отстраняване на неизправности


| Симптом                                  | Решение                                                         |
|------------------------------------------|-----------------------------------------------------------------|
| Сглобяване на контейнер зацикля > 10 мин | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Терминалът не се е свързал; кликнете **+** ➜ *bash*            |
| `401 Unauthorized` от OpenAI             | Грешен / изтекъл `OPENAI_API_KEY`                              |
| VS Code показва “Dev container mounting…” | Презаредете таба на браузъра—понякога Codespaces губи връзка   |
| Ядро на бележник липсва                  | Меню на бележника ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактирайте `.env` файла**: Отворете .env файла в текстов редактор (напр. VS Code, Notepad++ или друг). Добавете следните редове, като замените плейсхолдърите с вашата реална крайна точка и ключ за Microsoft Foundry Models (вижте [`providers.md`](03-providers.md) за инструкции как да ги получите):

   > **Забележка:** GitHub Models (с променливата `GITHUB_TOKEN`) ще бъде пенсиониран в края на юли 2026. Използвайте вместо това [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Запазете файла**: Запазете промените и затворете текстовия редактор.

5. **Инсталирайте `python-dotenv`**: Ако още не сте, трябва да инсталирате пакета `python-dotenv`, който зарежда променливите от .env файла във вашето Python приложение. Можете да го инсталирате с `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Заредете променливите от околната среда в Python скрипта си**: В скрипта си използвайте `python-dotenv` за да заредите променливите от .env файла:

   ```python
   from dotenv import load_dotenv
   import os

   # Заредете променливите на околната среда от .env файла
   load_dotenv()

   # Достъп до променливите на Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Това е! Успешно създадохте `.env` файл, добавихте идентификационни данни за Microsoft Foundry Models и ги заредихте във вашето Python приложение.

## Как да стартирате локално на вашия компютър

За да стартирате кода локално на вашия компютър, трябва да имате инсталирана някаква версия на [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

За да използвате репозитория, трябва да го клонирате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Когато сте готови с всичко, може да започнете!

## Допълнителни стъпки

### Инсталиране на Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за инсталиране на [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python и няколко пакета.
Conda е пакетен мениджър, който улеснява настройката и смяната между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Полезен е и за инсталиране на пакети, които не са налични през `pip`.

Можете да следвате [инструкциите за инсталиране на Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) за настройка.

След като инсталирате Miniconda, трябва да клонирате [репозитория](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако още не сте го направили).

След това създайте виртуална среда. За да направите това с Conda, създайте нов файл за средата (_environment.yml_). Ако използвате Codespaces, създайте този файл в директорията `.devcontainer`, тоест `.devcontainer/environment.yml`.

Добавете в този файл следния кодов фрагмент:

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

Ако срещнете грешки при използването на conda, можете ръчно да инсталирате Microsoft AI библиотеките чрез следната команда в терминала.

```
conda install -c microsoft azure-ai-ml
```

Файлът на средата задава зависимостите, които са нужни. `<environment-name>` е името, което желаете за вашата Conda среда, а `<python-version>` е версията на Python, например, `3` за последната главна версия на Python.

След това създайте вашата Conda среда като изпълните командите по-долу в командния ред/терминала.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Под-пътят .devcontainer се прилага само за настройки на Codespace
conda activate ai4beg
```

Вижте [упътването за Conda среди](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ако срещнете проблеми.

### Използване на Visual Studio Code с разширение за Python

Препоръчваме да използвате [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с инсталирано [разширение за Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за този курс. Това е препоръка, а не строго изискване.

> **Забележка**: Като отворите курса в VS Code, имате опцията да настроите проекта във контейнер. Това е благодарение на [специалната `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) папка, намираща се в курсовия репозиторий. Подробнее за това по-късно.

> **Забележка**: След като клонирате и отворите директорията в VS Code, автоматично ще ви се предложи да инсталирате разширение за Python.

> **Забележка**: Ако VS Code ви предложи да презаредите репозитория във контейнер, откажете, за да използвате локално инсталираната версия на Python.

### Използване на Jupyter в браузъра

Можете да работите по проекта и с [Jupyter среда](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно в браузъра си. Класическият Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) осигуряват приятна работна среда с функции като авто-допълване, оцветяване на кода и други.

За да стартирате Jupyter локално, отворете терминал/команден прозорец, навигирайте до директорията на курса и изпълнете:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира Jupyter и URL за достъп ще се покаже в командния прозорец.

След като достъпите URL, ще видите структурата на курса и ще можете да навигирате до всеки `*.ipynb` файл, например, `08-building-search-applications/python/oai-solution.ipynb`.

### Стартиране в контейнер

Алтернатива на настройването на всичко на вашия компютър или Codespace е използването на [контейнер](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специалната `.devcontainer` папка на курсовия репозиторий позволява на VS Code да настрои проекта в контейнер. Извън Codespaces това изисква инсталиране на Docker и малко повече работа, затова препоръчваме това само за опитни с контейнери.

Един от най-добрите начини за защита на API ключовете при използване на GitHub Codespaces е чрез използването на Codespace Secrets. Моля, следвайте [упътването за управление на тайни в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Уроци и технически изисквания

Курсът съдържа 6 концептуални урока и 6 урока по кодиране.

За уроките по кодиране използваме Azure OpenAI Сървис. Ще ви е необходим достъп до Azure OpenAI услугата и API ключ за стартирането на кода. Можете да кандидатствате за достъп като [попълните тази заявка](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Докато чакате обработката на вашата заявка, всеки урок по кодиране включва `README.md` файл, където можете да видите кода и изходите.

## Използване на Azure OpenAI услуга за първи път

Ако използвате Azure OpenAI услугата за първи път, моля следвайте това ръководство как да [създадете и разположите Azure OpenAI услуга.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Използване на OpenAI API за първи път

Ако използвате OpenAI API за първи път, моля следвайте ръководството как да [създадете и използвате интерфейса.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Срещнете други учащи

Създадохме канали в официалния ни [AI Community Discord сървър](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за срещи с други учащи. Това е чудесен начин да се свържете с други с подобни интереси предприемачи, строители, студенти и всички, които искат да се развиват в Генеративен AI.

[![Присъединете се към дискорд канал](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Проектният екип също ще бъде на този Discord сървър, за да помогне на всички учащи.

## Принос

Този курс е проект с отворен код. Ако видите области за подобрение или проблеми, моля, създайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или докладвайте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Проектният екип ще следи всички приноси. Участието в проекти с отворен код е страхотен начин да изградите кариера в Генеративен AI.

Повечето приноси изискват да се съгласите с Договор за лиценз на приносител (CLA), който декларира, че имате право и предоставяте на нас правата за използване на вашия принос. За подробности посетете [CLA, уебсайт за Договор за лиценз на приносител](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при превод на текст в този репо, моля не използвайте машинен превод. Ще проверяваме преводите чрез общността, така че се включвайте само в езиците, в които сте компетентни.

Когато подадете pull request, CLA-бот автоматично ще определи дали трябва да предоставите CLA и ще маркира PR подходящо (напр. етикет, коментар). Просто следвайте инструкциите на бота. Това се прави само веднъж за всички репозиторита, използващи нашия CLA.


Този проект е приел [Кодекса за поведение на Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За повече информация прочетете Често задаваните въпроси за Кодекса за поведение или се свържете с [Email opencode](opencode@microsoft.com) за допълнителни въпроси или коментари.

## Нека започнем

Сега, когато сте завършили необходимите стъпки за завършване на този курс, нека започнем с [въведение в Генеративния AI и LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->