# Започване с този курс

Много сме развълнувани, че започвате този курс и ще видите какво ще ви вдъхнови да създадете с Генеративния AI!

За да гарантираме вашия успех, тази страница описва стъпките за настройка, техническите изисквания и къде да получите помощ, ако е необходимо.

## Стъпки за настройка

За да започнете да посещавате този курс, трябва да изпълните следните стъпки.

### 1. Форкнете това хранилище

[Форкнете цялото това хранилище](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) в собствен акаунт в GitHub, за да можете да променяте какъвто и да е код и да изпълнявате задачите. Можете също така да [отметнете (🌟) това хранилище](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), за да го намирате по-лесно заедно с други свързани хранилища.

### 2. Създайте кодно пространство (codespace)

За да избегнете проблеми с зависимости при стартиране на кода, препоръчваме да стартирате този курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Във вашия форк: **Code -> Codespaces -> New on main**

![Диалогов прозорец с бутони за създаване на кодно пространство](../../../translated_images/bg/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Добавете таен ключ

1. ⚙️ Икона с предавка -> Командна палитра -> Codespaces : Управление на потребителски тайни -> Добавяне на нов таен ключ.
2. Име OPENAI_API_KEY, поставете вашия ключ, Запазете.

### 3. Какво следва?

| Искам да…         | Отиди на…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Започна Урок 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Работя офлайн        | [`setup-local.md`](02-setup-local.md)                                   |
| Настройка на доставчик на големи езикови модели | [`providers.md`](03-providers.md)               |
| Среща с други ученици | [Присъединете се към нашия Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Отстраняване на проблеми


| Симптом                                 | Решение                                                      |
|-----------------------------------------|-------------------------------------------------------------|
| Създаването на контейнера е блокирано > 10 минути | **Codespaces ➜ „Прегенерирай контейнера“**               |
| `python: command not found`              | Терминалът не се е присъединил, кликнете върху **+** ➜ *bash* |
| `401 Unauthorized` от OpenAI             | Неправилен или изтекъл `OPENAI_API_KEY`                    |
| VS Code показва „Dev container mounting…“ | Презаредете раздела на браузъра — понякога Codespaces губи връзка |
| Ядрото на тетрадката липсва             | Меню на тетрадката ➜ **Kernel ▸ Избери ядро ▸ Python 3**    |

   За системи базирани на Unix:

   ```bash
   touch .env
   ```

   За Windows:

   ```cmd
   echo . > .env
   ```

3. **Редактирайте файла `.env`**: Отворете файла `.env` в текстов редактор (например VS Code, Notepad++ или друг редактор). Добавете следните редове във файла, като заместите плейсхолдърите с вашите действителни крайна точка и ключ за Microsoft Foundry Models (вижте [`providers.md`](03-providers.md) за инструкции как да ги получите):

   > **Забележка:** GitHub Models (и неговата променлива `GITHUB_TOKEN`) ще бъдат премахнати в края на юли 2026 г. Използвайте вместо това [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Запазете файла**: Запазете промените и затворете текстовия редактор.

5. **Инсталирайте `python-dotenv`**: Ако все още не сте го направили, трябва да инсталирате пакета `python-dotenv`, за да заредите променливите на околната среда от файла `.env` във вашето Python приложение. Можете да го инсталирате с помощта на `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Заредете променливите на околната среда във вашия Python скрипт**: Във вашия Python скрипт използвайте пакета `python-dotenv`, за да заредите променливите на околната среда от файла `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Заредете променливите на средата от .env файла
   load_dotenv()

   # Достъп до променливите на Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Това е всичко! Успешно създадохте файл `.env`, добавихте вашите идентификационни данни за Microsoft Foundry Models и ги заредихте във вашето Python приложение.

## Как да стартирате локално на вашия компютър

За да стартирате кода локално на компютъра си, ще трябва да имате инсталирана някаква версия на [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

След това, за да използвате хранилището, трябва да го клонирате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

След като всичко е копирано, можете да започнете!

## Допълнителни стъпки

### Инсталиране на Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за инсталиране на [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, както и някои пакети.
Самият Conda е пакетен мениджър, който улеснява настройването и превключването между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Той също така е полезен за инсталиране на пакети, които не са налични чрез `pip`.

Можете да следвате [ръководството за инсталиране на MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) за настройка.

След като Miniconda е инсталиран, трябва да клонирате [хранилището](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако още не сте го направили).

След това трябва да създадете виртуална среда. За да направите това с Conda, създайте нов файл на средата (_environment.yml_). Ако следвате инструкциите с Codespaces, създайте файла в директорията `.devcontainer`, тоест `.devcontainer/environment.yml`.

Попълнете файла на средата със следния кодов фрагмент:

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

Ако срещнете грешки при използване на conda, можете ръчно да инсталирате Microsoft AI Libraries със следната команда в терминал.

```
conda install -c microsoft azure-ai-ml
```

Файлът на средата уточнява зависимостите, които са ни нужни. `<environment-name>` се отнася до името, което искате да използвате за вашата Conda среда, а `<python-version>` е версията на Python, която искате да използвате, например `3` е последната основна версия на Python.

След като това е готово, можете да създадете Conda средата си, като изпълните командите по-долу в командния ред/терминала

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Подпътят .devcontainer се прилага само за конфигурации на Codespace
conda activate ai4beg
```

Обърнете се към [ръководството за Conda среди](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ако срещнете проблеми.

### Използване на Visual Studio Code с разширение за Python

Препоръчваме да използвате редактора [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с инсталирано [разширение за Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за този курс. Това е по-скоро препоръка, отколкото задължително изискване.

> **Забележка**: Когато отворите хранилището на курса в VS Code, имате опцията да настроите проекта в контейнер. Това е възможно благодарение на [специалната директория `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst), намираща се в хранилището на курса. Повече за това по-късно.

> **Забележка**: След като клонирате и отворите директорията в VS Code, автоматично ще ви бъде предложено да инсталирате разширение за поддръжка на Python.

> **Забележка**: Ако VS Code ви предложи да отворите хранилището в контейнер, откажете тази заявка, за да използвате локално инсталираната версия на Python.

### Използване на Jupyter в браузър

Можете да работите по проекта и с [Jupyter среда](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно в браузъра си. Класическият Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предлагат удобна среда за разработка с функции като автоматично допълване, оцветяване на кода и др.

За да стартирате Jupyter локално, отворете терминала/командния ред, навигирайте до директорията на курса и изпълнете:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира инстанция на Jupyter и URL адресът за достъп ще бъде показан в прозореца на командния ред.

След като достъпите URL адреса, ще видите структурата на курса и ще можете да навигирате до всеки файл с разширение `*.ipynb`. Например, `08-building-search-applications/python/oai-solution.ipynb`.

### Стартиране в контейнер

Алтернатива на настройването на всичко на компютъра ви или Codespace е да използвате [контейнер](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специалната папка `.devcontainer` в хранилището на курса позволява на VS Code да настрои проекта в контейнер. Извън Codespaces това изисква инсталиране на Docker, което наистина изисква някакъв опит, затова препоръчваме това само за потребители с опит в работата с контейнери.

Един от най-добрите начини да защитите вашите API ключове при използване на GitHub Codespaces е чрез използването на Тайните на Codespaces. Моля, следвайте [ръководството за управление на тайни в Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), за да научите повече.


## Уроци и технически изисквания

Курсът има "Учебни" уроци, които обясняват концепции за Генеративния AI, и "Практически" уроци с практически кодови примери както на **Python**, така и на **TypeScript**, където е възможно.

За уроците с код използваме Azure OpenAI в Microsoft Foundry. Ще ви трябва Azure абонамент и API ключ. Достъпът е отворен - няма нужда от кандидатстване - така че можете да [създадете ресурс в Microsoft Foundry и да разположите модел](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), за да получите вашата крайна точка и ключ.

Всеки урок с код също включва файл `README.md`, където можете да разгледате кода и резултатите без да стартирате нищо.

## Първо използване на услугата Azure OpenAI

Ако ползвате услугата Azure OpenAI за първи път, моля, следвайте това ръководство за това как да [създадете и разположите ресурс в Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Първо използване на OpenAI API

Ако използвате OpenAI API за първи път, моля, следвайте ръководството как да [създадете и използвате интерфейса.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Срещнете други учащи се

Създадохме канали в нашия официален [AI Community Discord сървър](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за среща с други учащи се. Това е чудесен начин да се свържете с други ентусиасти, предприемачи, студенти и всички, които искат да се развиват в Генеративния AI.

[![Присъединяване към Discord канал](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Екипът по проекта ще присъства и в този Discord сървър, за да помогне на всички учащи се.

## Принос

Този курс е инициатива с отворен код. Ако видите възможности за подобрение или проблеми, моля, създайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или регистрирайте [GitHub проблем](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Екипът по проекта ще следи всички приноси. Приносът към проекти с отворен код е отличен начин да изградите своята кариера в Генеративния AI.

Повечето приноси изискват да се съгласите с Лицензионно споразумение за приноси (CLA), с което декларирате, че имате правото и наистина предоставяте права за използване на приноса си. За подробности посетете [CLA, уебсайт на Лицензионното споразумение за приноси](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: при превод на текст в това хранилище, моля, уверете се, че не използвате машинен превод. Ние ще проверяваме преводите чрез общността, затова моля, доброволно превеждайте само на езици, на които владеете добре.


Когато изпратите pull request, CLA-бот автоматично ще определи дали е необходимо да предоставите CLA и ще декорира PR подходящо (напр. етикет, коментар). Просто следвайте инструкциите, предоставени от бота. Трябва да направите това само веднъж за всички репозитории, използващи нашия CLA.

Този проект е приел [Кодекса на поведение за отворен код на Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За повече информация прочетете Често задавани въпроси за Кодекса на поведение или се свържете с [Email opencode](opencode@microsoft.com) при допълнителни въпроси или коментари.

## Нека започнем

Сега, когато сте завършили необходимите стъпки за завършване на този курс, нека започнем с [въведение в Генеративния ИИ и LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->