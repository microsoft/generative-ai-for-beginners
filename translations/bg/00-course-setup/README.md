<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T09:00:10+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bg"
}
-->
# Започване на курса

Много сме развълнувани, че започвате този курс и ще видите какво ще ви вдъхнови да създадете с Генеративния AI!

За да гарантираме вашия успех, тази страница описва стъпките за настройка, техническите изисквания и къде да получите помощ, ако е необходимо.

## Стъпки за настройка

За да започнете този курс, трябва да изпълните следните стъпки.

### 1. Форкнете това репо

[Форкнете цялото репо](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) към вашия собствен GitHub акаунт, за да можете да променяте код и да изпълнявате предизвикателствата. Можете също така да [звездите (🌟) това репо](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), за да го намерите и свързани репота по-лесно.

### 2. Създайте кодово пространство

За да избегнете проблеми със зависимостите при изпълнението на кода, препоръчваме да изпълните този курс в [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Това може да бъде създадено чрез избиране на опцията `Code` на вашата форкната версия на това репо и избиране на опцията **Codespaces**.

![Диалог, показващ бутони за създаване на кодово пространство](../../../00-course-setup/images/who-will-pay.webp)

### 3. Съхраняване на вашите API ключове

Да запазите вашите API ключове безопасни и сигурни е важно при създаването на всякакъв вид приложение. Препоръчваме да не съхранявате никакви API ключове директно в кода си. Комитирането на тези детайли в публично репо може да доведе до проблеми със сигурността и дори нежелани разходи, ако бъдат използвани от злонамерен актьор.
Ето ръководство стъпка по стъпка как да създадете файл `.env` за Python и да добавите `GITHUB_TOKEN`:

1. **Навигирайте до директорията на вашия проект**: Отворете вашия терминал или команден прозорец и навигирайте до главната директория на вашия проект, където искате да създадете файла `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Създайте файла `.env`**: Използвайте предпочитания от вас текстов редактор, за да създадете нов файл, наречен `.env`. Ако използвате командния ред, можете да използвате `touch` (on Unix-based systems) or `echo` (на Windows):

   Unix-базирани системи:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Редактирайте файла `.env`**: Отворете файла `.env` в текстов редактор (например VS Code, Notepad++ или друг редактор). Добавете следния ред към файла, като замените `your_github_token_here` с вашия реален GitHub токен:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Запазете файла**: Запазете промените и затворете текстовия редактор.

5. **Инсталирайте пакета `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, за да заредите променливите на средата от файла `.env` във вашето Python приложение. Можете да го инсталирате с `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Заредете променливите на средата във вашия Python скрипт**: Във вашия Python скрипт използвайте пакета `python-dotenv`, за да заредите променливите на средата от файла `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Това е всичко! Успешно създадохте файл `.env`, добавихте вашия GitHub токен и го заредихте във вашето Python приложение.

## Как да изпълните локално на вашия компютър

За да изпълните кода локално на вашия компютър, трябва да имате някаква версия на [Python инсталирана](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

За да използвате репото, трябва да го клонирате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

След като имате всичко проверено, можете да започнете!

## Допълнителни стъпки

### Инсталиране на Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) е лек инсталатор за инсталиране на [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, както и няколко пакета.
Conda сам по себе си е мениджър на пакети, който прави лесно настройването и превключването между различни Python [**виртуални среди**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакети. Той също така е полезен за инсталиране на пакети, които не са налични чрез `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Попълнете вашия файл със среда с фрагмента по-долу:

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

Ако откриете грешки при използването на conda, можете ръчно да инсталирате Microsoft AI Libraries, използвайки следната команда в терминала.

```
conda install -c microsoft azure-ai-ml
```

Файлът със средата определя зависимостите, които са ни необходими. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` е последната голяма версия на Python.

С това направено, можете да създадете вашата Conda среда, като изпълните командите по-долу във вашия команден ред/терминал

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Вижте [ръководството за Conda среди](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), ако срещнете някакви проблеми.

### Използване на Visual Studio Code с разширение за поддръжка на Python

Препоръчваме използването на редактора [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) с инсталирано [разширение за поддръжка на Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за този курс. Това обаче е повече препоръка, отколкото категорично изискване.

> **Забележка**: Като отворите репото на курса във VS Code, имате опция да настроите проекта в контейнер. Това е заради [специалната `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) директория, намерена в репото на курса. Повече за това по-късно.

> **Забележка**: След като клонирате и отворите директорията във VS Code, тя автоматично ще ви предложи да инсталирате разширение за поддръжка на Python.

> **Забележка**: Ако VS Code ви предложи да преотворите репото в контейнер, откажете тази заявка, за да използвате локално инсталираната версия на Python.

### Използване на Jupyter в браузъра

Можете също така да работите по проекта, използвайки [Jupyter среда](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно в браузъра си. Както класическият Jupyter, така и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) предоставят доста приятна среда за разработка с функции като автоматично довършване, подчертаване на код и др.

За да стартирате Jupyter локално, отидете до терминала/командния ред, навигирайте до директорията на курса и изпълнете:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Това ще стартира инстанция на Jupyter и URL адресът за достъп ще бъде показан в прозореца на командния ред.

След като достъпите URL адреса, трябва да видите съдържанието на курса и да можете да навигирате до всеки файл `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, където можете да видите кода и изходите.

## Използване на Azure OpenAI Service за първи път

Ако за първи път работите с услугата Azure OpenAI, моля, следвайте това ръководство за това как да [създадете и разположите ресурс на Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Използване на OpenAI API за първи път

Ако за първи път работите с OpenAI API, моля, следвайте ръководството за това как да [създадете и използвате интерфейса.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Срещнете други обучаващи се

Създадохме канали в нашия официален [AI Community Discord сървър](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за срещи с други обучаващи се. Това е страхотен начин да се свържете с други предприемачи, създатели, студенти и всеки, който иска да се развива в Генеративния AI.

[![Присъединете се към Discord канала](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Екипът на проекта също ще бъде в този Discord сървър, за да помага на обучаващите се.

## Принос

Този курс е инициатива с отворен код. Ако видите области за подобрение или проблеми, моля, създайте [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или логнете [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Екипът на проекта ще следи всички приноси. Приносът към отворен код е невероятен начин да изградите кариера в Генеративния AI.

Повечето приноси изискват от вас да се съгласите с Лицензионно споразумение за принос (CLA), което декларира, че имате право и наистина предоставяте ни правата да използваме вашия принос. За подробности посетете [CLA, уебсайт за Лицензионно споразумение за принос](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: когато превеждате текст в това репо, моля, уверете се, че не използвате машинен превод. Ще проверим преводите чрез общността, така че моля, доброволствайте за преводи само на езици, в които сте компетентни.

Когато изпратите pull request, CLA-ботът автоматично ще определи дали трябва да предоставите CLA и ще украси PR съответно (например, етикет, коментар). Просто следвайте инструкциите, предоставени от бота. Ще трябва да направите това само веднъж за всички репота, използващи нашия CLA.

Този проект е приел [Кодекс за поведение на Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За повече информация прочетете Често задаваните въпроси за Кодекса за поведение или се свържете с [Email opencode](opencode@microsoft.com) с допълнителни въпроси или коментари.

## Да започнем

Сега, когато сте изпълнили необходимите стъпки за завършване на този курс, нека започнем с [въведение в Генеративния AI и LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Докато се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.