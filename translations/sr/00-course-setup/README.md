# Започињање са овим курсом

Јако смо узбуђени што ћете започети овај курс и видети шта ћете бити инспирисани да створите уз генеративну вештачку интелигенцију!

Да бисмо осигурали ваш успех, ова страница описује кораке за подешавање, техничке захтеве и где можете добити помоћ ако буде потребно.

## Кораци подешавања

Да бисте почели са овим курсом, потребно је да завршите следеће кораке.

### 1. Форкујте овај репозиторијум

[Форкујте цео овај репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) на свој GitHub налог да бисте могли да мењате било који код и завршавате изазове. Такође можете [означити (🌟) овај репозиторијум](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) да бисте га лакше нашли заједно са повезаним репоима.

### 2. Креирајте кодспејс

Да бисте избегли проблеме са зависностима при покретању кода, препоручујемо да овај курс покрећете у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У вашем форку: **Code -> Codespaces -> New on main**

![Дијалог који показује дугмад за креирање кодспејса](../../../translated_images/sr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Додајте тајну

1. ⚙️ Икона зупчаника -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Назовите је OPENAI_API_KEY, налепите свој кључ и сачувајте.

### 3. Шта следи?

| Желим да…          | Идите на…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Почнем Лекцију 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Радим ван мреже        | [`setup-local.md`](02-setup-local.md)                                   |
| Подесим LLM Провајдера | [`providers.md`](03-providers.md)                                        |
| Упознам друге ученике | [Придружите се нашем Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Решавање проблема


| Симптом                                   | Решење                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Састављање контејнера заглављено > 10 мин | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Терминал се није прикључио; кликните **+** ➜ *bash*              |
| `401 Unauthorized` од OpenAI              | Погрешан / истекао `OPENAI_API_KEY`                              |
| VS Code показује “Dev container mounting…” | Освежите картицу претраживача — понекад Codespaces губи везу     |
| Недостаје језгро за нотебоок              | Менy нотебоока ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Unix-базирани системи:

   ```bash
   touch .env
   ```

   Виндоус:

   ```cmd
   echo . > .env
   ```

3. **Уредите `.env` фајл**: Отворите `.env` фајл у уређивачу текста (нпр. VS Code, Notepad++ или неком другом уређивачу). Додајте следеће линије у фајл, замењујући ознаке са вашим стварним Microsoft Foundry Models крајњим тачкама и кључем (погледајте [`providers.md`](03-providers.md) како да их добијете):

   > **Напомена:** GitHub Models (и његова променљива `GITHUB_TOKEN`) се повлачи крајем јула 2026. Користите [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) уместо тога.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Сачувајте фајл**: Сачувајте промене и затворите уређивач.

5. **Инсталирајте `python-dotenv`**: Ако нисте већ, потребно је да инсталирате пакет `python-dotenv` да бисте учитали променљиве окружења из `.env` фајла у вашу Python апликацију. Можете га инсталирати користећи `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитајте променљиве окружења у вашем Python скрипту**: У вашем Python скрипту, користите пакет `python-dotenv` да учитате променљиве окружења из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Учитајте променљиве окружења из .env фајла
   load_dotenv()

   # Приступите променљивим Microsoft Foundry модела
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

То је то! Успешно сте креирали `.env` фајл, додали своје Microsoft Foundry Models креденцијале и учитали их у вашу Python апликацију.

## Како покренути локално на вашем рачунару

Да бисте покренули код локално на вашем рачунару, потребно је да имате неку верзију [Python-а инсталирану](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Да бисте користили репозиторијум, потребно је да га клонирате:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Када све имате припремљено, можете започети!

## Опционо

### Инсталирање Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лаган инсталер за инсталирање [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-а, као и неколико пакета.
Conda је пакет менаџер који олакшава подешавање и пребацивање између различитих Python [**виртуелних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Такође је користан за инсталирање пакета које није могуће набавити преко `pip`.

Можете пратити [MiniConda упутства за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да бисте га подесили.

Када инсталирате Miniconda, потребно је да клонирате [репозиторијум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако већ нисте)

Затим је потребно да креирате виртуелно окружење. Да бисте то урадили користећи Conda, направите нови фајл окружења (_environment.yml_). Ако користите Codespaces, направите овај фајл унутар `.devcontainer` директоријума, односно `.devcontainer/environment.yml`.

Попуните ваш environment.yml фајл са следећим примером:

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

Ако добијате грешке при коришћењу conda, ручно инсталирајте Microsoft AI библиотеке користећи следећу команду у терминалу.

```
conda install -c microsoft azure-ai-ml
```

Фајл окружења дефинише зависности које су нам потребне. `<environment-name>` је име које желите да користите за Conda окружење, а `<python-version>` је верзија Python-а коју желите, на пример `3` је најновија главна верзија Python-а.

Када завршите, можете креирати Conda окружење покретањем следећих команди у командној линији/терминалу

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer под-путања важи само за поставке Codespace-а
conda activate ai4beg
```

Погледајте [упутство за Conda окружења](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђете на проблеме.

### Коришћење Visual Studio Code-а уз Python подршку

Препоручујемо коришћење [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) уредника са инсталираним [Python подршка екстензијом](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за овај курс. Међутим, ово је само препорука, а не обавезан захтев.

> **Напомена**: Отварањем репозиторијума курса у VS Code-у, имате опцију да подесите пројекат унутар контејнера. То је због [специјалног `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) директоријума који се налази у репозиторијуму курса. Више о овоме касније.

> **Напомена**: Када клон и отворите директоријум у VS Code, аутоматски ће вам предложити да инсталирате Python подршку екстензију.

> **Напомена**: Ако вам VS Code предложи да поново отворите репозиторијум у контејнеру, одбијте ову опцију да бисте користили локално инсталирану верзију Python-а.

### Коришћење Jupyter-а у прегледачу

Такође можете радити на пројекту користећи [Jupyter окружење](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно у вашем прегледачу. Класични Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) пружају пријатно развојно окружење са функцијама као што су аутоматско допуњавање, истакнуће кода итд.

Да бисте покренули Jupyter локално, идите у терминал/командну линију, позиционирајте се у директоријум курса и извршите:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter инстанцу и URL за приступ ће бити приказан у командној линији.

Када приступите URL-у, требало би да видите нацрт курса и моћи ћете да приступите било ком `*.ipynb` фајлу. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

### Покретање у контејнеру

Алтернатива подешавању свега на вашем рачунару или у Кодспејсу је коришћење [контејнера](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Специјални `.devcontainer` фолдер унутар репозиторијума курса омогућава VS Code-у да подеси пројекат унутар контејнера. Изван Codespaces, ово ће захтевати инсталацију Docker-а и, искрено, захтева доста рада, па ову опцију препоручујемо само онима који имају искуства са радом са контејнерима.

Један од најбољих начина да ваша API кључеви буду безбедни када користите GitHub Codespaces јесте коришћење Codespace Secrets. Молимо пратите [упутства за управљање тастерама у Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) да сазнате више.


## Лекције и технички захтеви

Овај курс има "Learn" лекције које објашњавају концепте генеративне вештачке интелигенције и "Build" лекције са практичним примерима кода како у **Python-у** тако и у **TypeScript-у** кад год је могуће.

За кодирање користимо Azure OpenAI у Microsoft Foundry-у. Потребна вам је Azure претплата и API кључ. Приступ је отворен – није потребна пријава – па можете [креирати Microsoft Foundry ресурс и имплементирати модел](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) да бисте добили крајњу тачку и кључ.

Свака лекција за програмирање укључује и `README.md` фајл у ком можете видети код и резултате без потребе да било шта покрећете.

## Коришћење Azure OpenAI сервиса први пут

Ако први пут радите са Azure OpenAI сервисом, пратите ова упутства о томе како да [креирате и поставите Azure OpenAI Service ресурс.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Коришћење OpenAI API-ја први пут

Ако први пут користите OpenAI API, пратите упутства о томе како да [направите и користите интерфејс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Упознајте друге ученике

Креирали смо канале у нашем званичном [AI Community Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за упознавање других учесника. Ово је сјајан начин за умрежавање са другим предузетницима заинтересованим за генеративну вештачку интелигенцију, градитељима, студентима и свима који желе да напредују у овој области.

[![Придружите се discord каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Тим пројекта ће такође бити присутан на овом Discord серверу да помогне свим ученицима.

## Учешће

Овај курс је иницијатива отвореног кода. Ако видите могућности за побољшање или проблеме, направите [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или отворите [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Тим пројекта ће пратити све доприносе. Учешће у пројектима отвореног кода је одличан начин да изградите своју каријеру у генеративној вештачкој интелигенцији.

Већина доприноса захтева да се сложите са Уговором о лиценци за доприносе (CLA) којим потврђујете да имате права и дозвољавате нам да користимо ваш допринос. За детаље посетите [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: приликом превођења текста у овом репозиторијуму, молимо вас да не користите машински превод. Преводе ће проверити заједница, зато се пријављујте за преводе само у језицима које добро познајете.


Када пошаљете pull request, CLA-бот ће аутоматски утврдити да ли морате да доставите CLA и означити PR на одговарајући начин (нпр. ознака, коментар). Једноставно следите упутства која вам да бот. Ово ћете морати да урадите само једном за све репозиторијуме који користе наш CLA.

Овај пројекат је усвојио [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За више информација прочитајте Често Постављана Питања о Правилима понашања или контактирајте [Email opencode](opencode@microsoft.com) за додатна питања или коментаре.

## Хајде да почнемо

Сада када сте завршили потребне кораке за завршетак овог курса, хајде да почнемо са [уводом у Генеративну АИ и LLM-ове](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->