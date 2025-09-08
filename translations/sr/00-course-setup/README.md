<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:29:59+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sr"
}
-->
# Почетак рада са овим курсом

Веома смо узбуђени што почињеш овај курс и радујемо се да видимо шта ћеш инспирисан/а направити уз Генеративни АИ!

Да бисмо ти помогли да успешно започнеш, на овој страници су описани кораци за подешавање, технички захтеви и где можеш да потражиш помоћ ако затреба.

## Кораци за подешавање

Да би започео/ла са курсом, потребно је да завршиш следеће кораке.

### 1. Форкуј овај репозиторијум

[Форкуј цео овај репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) на свој GitHub налог да би могао/ла да мењаш код и решаваш изазове. Можеш и да [дадаш звездицу (🌟) овом репозиторијуму](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) како би га лакше пронашао/ла, као и сродне репозиторијуме.

### 2. Креирај codespace

Да би избегао/ла проблеме са зависностима приликом покретања кода, препоручујемо да овај курс радиш у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У свом форку: **Code -> Codespaces -> New on main**

![Дијалог са дугмадима за креирање codespace-а](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Додај тајну (secret)

1. ⚙️ Икона зупчаника -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Назив OPENAI_API_KEY, налепи свој кључ, Сачувај.

### 3.  Шта даље?

| Желим да…           | Иди на…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Почнем прву лекцију | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Радим офлајн        | [`setup-local.md`](02-setup-local.md)                                   |
| Подесим LLM провајдера | [`providers.md`](providers.md)                                       |
| Упознам друге полазнике | [Придружи се нашем Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Решавање проблема


| Симптом                                   | Решење                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Градња контејнера стоји > 10 мин          | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Терминал није повезан; кликни **+** ➜ *bash*                    |
| `401 Unauthorized` од OpenAI              | Погрешан / истекао `OPENAI_API_KEY`                             |
| VS Code приказује “Dev container mounting…” | Освежи таб у прегледачу—Codespaces понекад изгуби везу         |
| Недостаје kernel за Notebook              | Notebook мени ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Измени `.env` фајл**: Отвори `.env` фајл у неком едитору текста (нпр. VS Code, Notepad++, или било ком другом едитору). Додај следећу линију у фајл, замењујући `your_github_token_here` са својим стварним GitHub токеном:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сачувај фајл**: Сачувај измене и затвори едитор.

5. **Инсталирај `python-dotenv`**: Ако већ ниси, треба да инсталираш пакет `python-dotenv` да би учитао/ла променљиве окружења из `.env` фајла у своју Python апликацију. Можеш га инсталирати помоћу `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитај променљиве окружења у свом Python скрипту**: У свом Python скрипту, користи пакет `python-dotenv` да учиташ променљиве окружења из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

То је то! Успешно си креирао/ла `.env` фајл, додао/ла свој GitHub токен и учитао/ла га у своју Python апликацију.

## Како покренути локално на свом рачунару

Да би покренуо/ла код локално на свом рачунару, потребно је да имаш неку верзију [Python-а инсталирану](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Да би користио/ла репозиторијум, треба да га клонираш:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Када све преузмеш, спреман/на си да почнеш!

## Опциони кораци

### Инсталација Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лаган инсталер за инсталацију [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-а и неколико пакета.
Conda је менаџер пакета који олакшава подешавање и пребацивање између различитих Python [**виртуелних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Такође је користан за инсталацију пакета који нису доступни преко `pip`.

Можеш пратити [MiniConda упутство за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да је подесиш.

Када инсталираш Miniconda, треба да клонираш [репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако већ ниси).

Затим треба да креираш виртуелно окружење. Да би то урадио/ла са Conda-ом, креирај нови фајл окружења (_environment.yml_). Ако радиш у Codespaces-у, креирај га унутар `.devcontainer` директоријума, дакле `.devcontainer/environment.yml`.

Попуни свој фајл окружења следећим садржајем:

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

Ако наиђеш на грешке са conda-ом, можеш ручно инсталирати Microsoft AI библиотеке помоћу следеће команде у терминалу.

```
conda install -c microsoft azure-ai-ml
```

Фајл окружења наводи зависности које су нам потребне. `<environment-name>` је име које желиш да користиш за своје Conda окружење, а `<python-version>` је верзија Python-а коју желиш да користиш, на пример, `3` је најновија главна верзија Python-а.

Када то завршиш, можеш креирати своје Conda окружење покретањем следећих команди у командној линији/терминалу

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Погледај [Conda упутство за окружења](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђеш на проблеме.

### Коришћење Visual Studio Code са Python екстензијом

Препоручујемо да користиш [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) едитор са инсталираном [Python екстензијом](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за овај курс. Ово је само препорука, није обавезно.

> **Note**: Када отвориш репозиторијум курса у VS Code-у, имаш опцију да подесиш пројекат унутар контејнера. Ово је могуће захваљујући [посебном `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) директоријуму унутар репозиторијума курса. Више о томе касније.

> **Note**: Када клонираш и отвориш директоријум у VS Code-у, VS Code ће ти аутоматски предложити да инсталираш Python екстензију.

> **Note**: Ако ти VS Code предложи да поново отвориш репозиторијум у контејнеру, одбиј ту опцију ако желиш да користиш локално инсталиран Python.

### Коришћење Jupyter-а у прегледачу

Можеш радити на пројекту и користећи [Jupyter окружење](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно у свом прегледачу. И класични Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) пружају пријатно окружење за развој са функцијама као што су аутоматско довршавање, истицање кода и сл.

Да би покренуо/ла Jupyter локално, отвори терминал/командну линију, пређи у директоријум курса и покрени:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter инстанцу и URL за приступ ће бити приказан у прозору командне линије.

Када приступиш URL-у, требало би да видиш структуру курса и можеш да отвориш било који `*.ipynb` фајл. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

### Покретање у контејнеру

Алтернатива подешавању свега на свом рачунару или Codespace-у је коришћење [контејнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Посебан `.devcontainer` директоријум унутар репозиторијума курса омогућава VS Code-у да подеси пројекат унутар контејнера. Ван Codespaces-а, ово захтева инсталацију Docker-а и мало више посла, па ово препоручујемо само онима који већ имају искуства са контејнерима.

Један од најбољих начина да сачуваш своје API кључеве безбедним када користиш GitHub Codespaces је коришћење Codespace Secrets. Погледај [упутство за управљање Codespaces тајнама](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) за више информација.


## Лекције и технички захтеви

Курс има 6 концептуалних и 6 програмерских лекција.

За програмерске лекције користимо Azure OpenAI Service. Биће ти потребан приступ Azure OpenAI сервису и API кључ да би покренуо/ла овај код. Можеш се пријавити за приступ [попуњавањем ове пријаве](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Док чекаш да ти пријава буде обрађена, свака програмерска лекција садржи и `README.md` фајл где можеш да видиш код и излазе.

## Прво коришћење Azure OpenAI сервиса

Ако први пут радиш са Azure OpenAI сервисом, прати ово упутство како да [креираш и поставиш Azure OpenAI Service ресурс.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Прво коришћење OpenAI API-ја

Ако први пут радиш са OpenAI API-јем, прати упутство како да [креираш и користиш интерфејс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Упознај друге полазнике

Направили смо канале на нашем званичном [AI Community Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за упознавање других полазника. Ово је одличан начин да се повежеш са другим предузетницима, градитељима, студентима и свима који желе да напредују у области Генеративног АИ.

[![Придружи се discord каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Тим који ради на пројекту ће такође бити на овом Discord серверу да помогне свим полазницима.

## Доприноси

Овај курс је отвореног кода. Ако видиш простор за унапређење или неки проблем, направи [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или пријави [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Тим ће пратити све доприносе. Допринос отвореном коду је сјајан начин да изградиш каријеру у области Генеративног АИ.

Већина доприноса захтева да се сагласиш са Contributor License Agreement (CLA) којим потврђујеш да имаш право и заиста дајеш нам право да користимо твој допринос. За више детаља, посети [CLA, Contributor License Agreement сајт](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: када преводиш текст у овом репозиторијуму, молимо те да не користиш машински превод. Провераваћемо преводе преко заједнице, зато се пријави само за језике које добро познајеш.

Када пошаљеш pull request, CLA-бот ће аутоматски проверити да ли треба да потпишеш CLA и обележити PR (нпр. етикетом, коментаром). Само прати упутства која добијеш од бота. Ово треба да урадиш само једном за све репозиторијуме који користе наш CLA.

Овај пројекат користи [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За више информација прочитај Code of Conduct FAQ или контактирај [Email opencode](opencode@microsoft.com) за додатна питања или коментаре.

## Хајде да почнемо
Сада када сте завршили све потребне кораке за овај курс, хајде да започнемо са [уводом у генеративну вештачку интелигенцију и LLM-ове](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала употребом овог превода.