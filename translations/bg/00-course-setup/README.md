# Започване с този курс

Много сме развълнувани, че започвате този курс и ще видите какво ще ви вдъхнови да създадете с Генеративен ИИ!

За да осигурим вашия успех, тази страница очертава стъпките за настройка, техническите изисквания и къде да потърсите помощ, ако е необходимо.

## Стъпки за настройка

За да започнете да вземате този курс, ще трябва да изпълните следните стъпки.

### 1. Форкнете това Репо

[Форкнете цялото това репо](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в собствен акаунт в GitHub, за да можете да променяте всякакъв код и да завършвате предизвикателствата. Можете също да [дадете звезда (🌟) на това репо](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), за да го намирате и свързаните с него репота по-лесно.

### 2. Създайте codespace

За да избегнете проблеми с зависимости при изпълнение на кода, препоръчваме да стартирате този курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

В своя форк: **Code -> Codespaces -> New on main**

![Диалог показващ бутони за създаване на codespace](../../../translated_images/bg/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавете таен ключ

1. ⚙️ Икона на зъбно колело -> Палитра с команди -> Codespaces : Manage user secret -> Добавете нов таен ключ.
2. Име OPENAI_API_KEY, поставете своя ключ и запазете.

### 3. Какво следва?

| Искам да…           | Отидете на…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Започна урок 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работя офлайн       | [`setup-local.md`](02-setup-local.md)                                   |
| Настроя доставчик на LLM | [`providers.md`](03-providers.md)                                        |
| Срещна други учащи  | [Присъединете се към нашия Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Отстраняване на проблеми

| Симптом                                   | Решение                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Изграждането на контейнера се задържа > 10 мин  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Терминалът не се закачи; кликнете върху **+** ➜ *bash*          |
| `401 Unauthorized` от OpenAI              | Грешен или изтекъл `OPENAI_API_KEY`                             |
| VS Code показва „Dev container mounting…“| Обновете таба на браузъра — понякога Codespaces губи връзка       |
| Липсва ядро на Notebook                   | Меню на Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   За Unix-базирани системи:

   ```bash
   touch .env
   ```

   За Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактиране на файла `.env`**: Отворете файла `.env` в текстов редактор (например, VS Code, Notepad++ или друг). Добавете следния ред, като заместите `your_github_token_here` със своя реален GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Запишете файла**: Запазете промените и затворете редактора.

5. **Инсталирайте `python-dotenv`**: Ако все още не сте, трябва да инсталирате пакета `python-dotenv`, за да зареждате променливи на средата от `.env` файла в Python приложението. Можете да го инсталирате с `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Заредете променливите на средата в Python скрипта**: В своя Python скрипт използвайте пакета `python-dotenv`, за да заредите променливите от `.env` файла:

   ```python
   from dotenv import load_dotenv
   import os

   # Зареждане на променливи на средата от .env файл
   load_dotenv()

   # Достъп до променливата GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Това е! Успешно създадохте `.env` файл, добавихте GitHub токена и го заредихте в Python приложението си.

## Как да стартирате локално на своя компютър

За да стартирате кода локално на своя компютър, ще трябва да имате инсталирана някаква версия на [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

След това, за да използвате хранилището, трябва да го клонирате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Когато всичко е готово, можете да започнете!

## Опционални стъпки

### Инсталиране на Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за инсталиране на [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, както и няколко пакета.
Conda е мениджър на пакети, който улеснява създаването и превключването между различни [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети за Python. Той е полезен и за инсталиране на пакети, които не са достъпни чрез `pip`.

Можете да следвате [инструкциите за инсталиране на MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), за да го настроите.

След като инсталирате Miniconda, трябва да клонирате [репозиторито](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако още не сте го направили).

След това трябва да създадете виртуална среда. За да го направите с Conda, създайте нов файл за средата (_environment.yml_). Ако използвате Codespaces, създайте го в директорията `.devcontainer`, т.е. `.devcontainer/environment.yml`.

Попълнете файла за средата със следния код:

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

Ако получите грешки при използване на conda, можете ръчно да инсталирате Microsoft AI Libraries с командата долу в терминала.

```
conda install -c microsoft azure-ai-ml
```

Файлът за средата уточнява нужните зависимости. `<environment-name>` е името, което искате да използвате за вашата Conda среда, а `<python-version>` е версията на Python, която искате да използвате, например, `3` е последната основна версия на Python.

След това можете да създадете Conda средата, като изпълните следните команди в командния ред/терминала:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпътят .devcontainer се прилага само за настройки на Codespace
conda activate ai4beg
```

Вижте [Ръководството за Conda среди](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ако имате проблеми.

### Използване на Visual Studio Code с разширение за Python

Препоръчваме използването на редактора [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с инсталирано [разширение за поддръжка на Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за този курс. Това е препоръка, а не задължение.

> **Забележка**: Отваряйки учебното репо във VS Code, имате опцията да настроите проекта в контейнер. Това е възможно благодарение на [специалната директория `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), която е част от курса. Повече за това по-нататък.

> **Забележка**: След като клонирате и отворите директорията във VS Code, редакторът автоматично ще предложи да инсталирате разширение за Python.

> **Забележка**: Ако VS Code предложи да отворите хранилището в контейнер, отхвърлете заявката, ако желаете да използвате локално инсталираната версия на Python.

### Използване на Jupyter в браузър

Можете също да работите по проекта в [Jupyter среда](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно в браузъра. Класическият Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставят удобна среда за разработка с функции като автодовършване, оцветяване на кода и др.

За да стартирате Jupyter локално, отворете терминала/командния ред, навигирайте до директорията на курса и изпълнете:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира Jupyter инстанция и URL адресът за достъп ще бъде показан в прозореца на командния ред.

След като влезете в URL адреса, ще видите очертанието на курса и ще можете да навигирате до всеки `*.ipynb` файл. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Стартиране в контейнер

Алтернатива на настройката на всичко на вашия компютър или Codespace е използването на [контейнер](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специалната папка `.devcontainer` в учебното репо позволява на VS Code да настрои проекта в контейнер. Извън Codespaces това изисква инсталиране на Docker и определено включва малко повече работа, затова препоръчваме това само на тези с опит в работата с контейнери.

Един от най-добрите начини да защитите API ключовете си, когато използвате GitHub Codespaces, е чрез използване на Codespace Secrets. Моля, следвайте [Ръководството за управление на тайни в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), за да научите повече.

## Уроци и технически изисквания

Курсът има 6 концептуални урока и 6 урока за програмиране.

За уроците за програмиране използваме Azure OpenAI Service. Ще ви е необходим достъп до Azure OpenAI Service и API ключ, за да стартирате кода. Можете да кандидатствате за достъп, като [попълните тази заявка](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Докато чакате заявката ви да бъде обработена, всеки урок за програмиране включва и `README.md` файл, където можете да видите кода и резултатите.

## Използване на Azure OpenAI Service за първи път

Ако ползвате Azure OpenAI Service за първи път, моля следвайте това ръководство как да [създадете и разположите ресурс Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Използване на OpenAI API за първи път

Ако ползвате OpenAI API за първи път, моля следвайте ръководството как да [създадете и използвате интерфейса](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Срещнете други учащи

Създадохме канали в нашия официален [AI Community Discord сървър](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), за да се срещнете с други учащи. Това е чудесен начин да се свържете с други амбициозни предприемачи, разработчици, студенти и всички, които искат да напреднат в Генеративния ИИ.

[![Присъединете се към Discord канал](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Екипът на проекта също ще бъде в този Discord сървър, за да помага на учащите.

## Приноси

Този курс е инициатива с отворен код. Ако видите възможности за подобрения или проблеми, моля направете [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или регистрирайте [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Екипът на проекта ще следи всички приноси. Приносът към отворен код е чудесен начин да развиете кариерата си в Генеративния ИИ.

Повечето приноси изискват съгласие с Contributor License Agreement (CLA), който декларира, че имате право и всъщност предоставяте права за използване на вашия принос. За подробности вижте [CLA, Contributor License Agreement уебсайт](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: когато превеждате текст в това репо, моля, не използвайте машинен превод. Ще проверяваме преводите чрез общността, затова доброволствайте за преводи само на езици, които владеете добре.

Когато подадете pull request, CLA-бот автоматично ще определи дали трябва да предоставите CLA и ще маркира PR подходящо (например етикет, коментар). Просто следвайте инструкциите на бота. Ще го правите само веднъж за всички репота, използващи нашия CLA.

Този проект е приел [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За повече информация прочетете Често задавани въпроси относно Кодекса на поведение или се свържете по имейл с [Email opencode](opencode@microsoft.com) за допълнителни въпроси или коментари.

## Нека започваме!
Сега, когато сте завършили необходимите стъпки за преминаване на този курс, нека започнем с [въведение в Генеративния AI и LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неверни тълкувания, възникнали от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->