# Почетак овог курса

Веома смо узбуђени што крећете са овим курсом и радујемо се да видимо шта ћете инспирисати да направите уз генеративну вештачку интелигенцију!

Да бисмо осигурали ваш успех, ова страница описује кораке подешавања, техничке захтеве и где можете добити помоћ ако вам затреба.

## Кораци подешавања

Да бисте започели овај курс, потребно је да извршите следеће кораке.

### 1. Форкајте овај репозиторијум

[Форкајте цео овај репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) на свој GitHub налог да бисте могли да мењате било који код и решавате задатке. Такође можете [поставити звездицу (🌟) овом репозиторијуму](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) како бисте га лакше пронашли и повезане репозиторијуме.

### 2. Креирајте codespace

Да бисте избегли проблеме са зависностима приликом извршавања кода, препоручујемо да овај курс покрећете у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У вашем форку: **Code -> Codespaces -> New on main**

![Дијалог који приказује дугмад за креирање codespace](../../../translated_images/sr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Додајте тајну (secret)

1. ⚙️ Икона зупчаника -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Назив: OPENAI_API_KEY, налепите свој кључ, Сачувајте.

### 3. Шта следи?

| Желим да…          | Погледај…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Започнем Лекцију 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Ради офлајн          | [`setup-local.md`](02-setup-local.md)                                   |
| Подесим ЛЛМ провајдера | [`providers.md`](03-providers.md)                                        |
| Упознам друге ученике | [Придружи нам се на Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Решавање проблема


| Симптом                                      | Решење                                                            |
|----------------------------------------------|------------------------------------------------------------------|
| Контейнер преживљава изградњу > 10 минута   | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                    | Терминал није повезан; кликните **+** ➜ *bash*                    |
| `401 Unauthorized` од OpenAI                    | Нетачан / истекао `OPENAI_API_KEY`                                |
| VS Code приказује “Dev container mounting…” | Освежите картицу прегледача—Codespaces понекад губи везу         |
| Недостаје kernel нотебоока                      | Мени нотебоока ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Измените `.env` фајл**: Отворите `.env` фајл у уређивачу текста (нпр. VS Code, Notepad++ или неком другом уређивачу). Додајте следеће редове у фајл, замењујући фиктивне вредности стварним крајњим тачкама и кључевима Microsoft Foundry Models (погледајте [`providers.md`](03-providers.md) како да добијете ове податке):

   > **Напомена:** GitHub модели (и његова променљива `GITHUB_TOKEN`) престају да се користе крајем јула 2026. Користите уместо тога [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сачувајте фајл**: Сачувајте измене и затворите уређивач текста.

5. **Инсталирајте `python-dotenv`**: Ако већ нисте, потребно је да инсталирате `python-dotenv` пакет да бисте учитали променљиве окружења из `.env` фајла у вашу Python апликацију. Можете га инсталирати користећи `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитајте променљиве окружења у свој Python скрипт**: У вашем Python скрипту користите `python-dotenv` пакет да учитате променљиве окружења из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Учитај променљиве окружења из .env фајла
   load_dotenv()

   # Приступ променљивим Microsoft Foundry модела
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

То је то! Успешно сте креирали `.env` фајл, додали своје креденцијале за Microsoft Foundry Models и учитали их у своју Python апликацију.

## Како покренути локално на свом рачунару

Да бисте покренули код локално на свом рачунару, потребно је да имате инсталирану неку верзију [Python-а](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Затим, да бисте користили репозиторијум, потребно је да га клонате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Када имате све проверено, можете почети!

## Опционални кораци

### Инсталирање Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лагани инсталер за инсталацију [Conda-e](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-а, као и неколико пакета.
Conda је управљач пакета који олакшава подешавање и пребацивање између различитих Python [**виртуелних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Такође је користан за инсталирање пакета који нису доступни преко `pip`.

Можете пратити [MiniConda упутство за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да бисте га подесили.

Након инсталације Miniconda, потребно је да клонате [репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако то већ нисте урадили)

Затим, потребно је да креирате виртуелно окружење. Пре тога направите фајл за окружење (_environment.yml_). Ако пратите коришћење Codespaces, креирајте овај фајл унутар `.devcontainer` директоријума, дакле `.devcontainer/environment.yml`.

Упишите следећи исечак у свој environment фајл:

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

Ако наиђете на грешке приликом коришћења conda, можете ручно инсталирати Microsoft AI библиотеке помоћу следеће команде у терминалу.

```
conda install -c microsoft azure-ai-ml
```

Фајл окружења специфikuје зависности које су нам потребне. `<environment-name>` се односи на име које желите да користите за своје Conda окружење, а `<python-version>` је верзија Python-а коју желите да користите, на пример, `3` је најновија главна верзија Python-а.

Када то урадите, можете креирати Conda окружење покретањем наредби у свом командном реду / терминалу

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer под-путања се примењује само на поставке Codespace-а
conda activate ai4beg
```

Погледајте [указе за Conda окружења](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђете на било какве проблеме.

### Коришћење Visual Studio Code са Python проширењем

Препоручујемо коришћење [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) уређивача са инсталираним [Python проширење](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за овај курс. Међутим, ово је препорука, а не обавезан захтев.

> **Напомена**: Отварањем репозиторијума курса у VS Code имате опцију да подесите пројекат унутар контејнера. То је због посебног `.devcontainer` директоријума у репозиторијуму курса. Више о овоме касније.

> **Напомена**: Када клонате и отворите директоријум у VS Code, аутоматски ће вам понудити да инсталирате Python проширење.

> **Напомена**: Ако VS Code понуди да поново отвори репозиторијум у контејнеру, одбијте тај захтев да бисте користили локално инсталирану верзију Python-а.

### Коришћење Jupyter-а у претраживачу

Такође можете радити на пројекту користећи [Jupyter окружење](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно у свом претраживачу. Како класични Jupyter тако и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) пружају пријатно развојно окружење са функцијама као што су аутоматско допуњавање, истакнути код, итд.

Да бисте покренули Jupyter локално, идите на терминал/командну линију, одите у директоријум курса и извршите:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter инстанцу, а URL за приступ ће бити приказан у командном прозору.

Када приступите URL-у, требало би да видите структуру курса и моћи ћете да отворите било који `*.ipynb` фајл. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

### Покретање у контејнеру

Алтернатива подешавању свега на вашем рачунару или Codespace-у је коришћење [контејнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Посебни `.devcontainer` фолдер у курсовом репозиторијуму омогућава VS Code-у да подеси пројекат унутар контејнера. Изван Codespaces, ово захтева инсталацију Docker-а и, искрено, укључује мало рада, па препоручујемо ово само онима који имају искуство са радом у контејнерима.

Један од најбољих начина да обезбедите своје API кључеве када користите GitHub Codespaces је коришћење Codespace Secrets. Пратите [упутства за управљање тајнама у Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) да бисте сазнали више о овоме.


## Лекције и технички захтеви

Курс има 6 концептуалних лекција и 6 кодирајућих лекција.

За кодирајуће лекције користимо Azure OpenAI Service. Потребан вам је приступ Azure OpenAI сервису и API кључ да бисте покренули овај код. Можете се пријавити за приступ [попуњавањем ове пријаве](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Док чекате обраду ваше пријаве, свака кодирајућа лекција садржи и `README.md` фајл где можете погледати код и излазне резултате.

## Коришћење Azure OpenAI сервиса први пут

Ако радите са Azure OpenAI сервисом први пут, молимо вас да пратите овај водич о томе како да [креирате и имплементирате ресурс Azure OpenAI сервиса.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Коришћење OpenAI API први пут

Ако радите са OpenAI API-јем први пут, молимо вас да пратите водич о томе како да [креирате и користите интерфејс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Упознајте друге ученике

Креирали смо канале на нашем званичном [AI Community Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за упознавање других ученика. Ово је одличан начин за умрежавање са другим предузетницима, градитељима, студентима и свима који желе да напредују у генеративној вештачкој интелигенцији.

[![Придружи се discord каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Тим пројекта ће такође бити на овом Discord серверу да помогне свим ученицима.

## Допринос

Овај курс је иницијатива отвореног кода. Ако видите области за побољшање или проблеме, молимо вас да направите [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или пријавите [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Тим пројекта ће пратити све доприносе. Допринос отвореном коду је сјајан начин да изградите своју каријеру у генеративној вештачкој интелигенцији.

Већина доприноса захтева да пристанете на споразум о лиценци за допринос (CLA) којим изјављујете да имате право и заправо нам дајете права да користимо ваш допринос. За детаље посетите [CLA, Contributor License Agreement вебсајт](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: приликом превођења текста у овом репозиторијуму, молимо вас да не користите машински превод. Преводе ћемо верификовати преко заједнице, тако да се молимо да се пријављујете за преводе само у језицима које добро познајете.

Када пошаљете pull request, CLA-бот ће аутоматски утврдити да ли морате да доставите CLA и одговарајуће означити PR (нпр. етикета, коментар). Само пратите упутства која даје бот. Ово ћете морати да урадите само једном за све репозиторијуме који користе наш CLA.


Овај пројекат је усвојио [Microsoft Open Source Кодекс понашања](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За више информација прочитајте Често Постављана Питања о Кодексу понашања или контактирајте [Email opencode](opencode@microsoft.com) са додатним питањима или коментарима.

## Хајде да почнемо

Сада када сте завршили потребне кораке за овај курс, хајде да почнемо са [уводом у Генеративну Вештачку Интелигенцију и LLM-ове](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->