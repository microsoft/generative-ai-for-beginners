# Почетак овог курса

Веома смо узбуђени што крећете са овим курсом и што ћете видети шта ћете добити инспирацију да направите са Генеративном вештачком интелигенцијом!

Да бисмо осигурали ваш успех, ова страница описује кораке за подешавање, техничке захтеве и где добити помоћ ако је потребно.

## Кораци за подешавање

Да бисте почели са овим курсом, потребно је да завршите следеће кораке.

### 1. Форкујте овај репо

[Форкујте цео овај репозиторijум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) на свој GitHub налог да бисте могли мењати било који код и завршавати изазове. Такође можете [означити звездицом (🌟) овај репо](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) да бисте га лакше пронашли заједно са сродним репозиторijумима.

### 2. Креирајте codespace

Да бисте избегли било какве проблеме са зависностима приликом извођења кода, препоручујемо да овај курс покренете у [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

У свом форку: **Код -> Codespaces -> New on main**

![Дијалог који приказује дугмад за креирање codespace-а](../../../translated_images/sr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Додајте тајну

1. ⚙️ Икона зупчаника -> Командна палета -> Codespaces : Manage user secret -> Add a new secret.
2. Назив: OPENAI_API_KEY, налепите свој кључ, сачувајте.

### 3. Шта даље?

| Желим да…            | Идите на…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Почнем Лекцију 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Радим офлајн         | [`setup-local.md`](02-setup-local.md)                                   |
| Подесим LLM провајдера | [`providers.md`](03-providers.md)                                        |
| Упознам друге учеснике | [Придружите се нашем Discord-у](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Решавање проблема

| Симптом                                   | Решење                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Контейнер за грађу заглављен > 10 минута | **Codespaces ➜ „Rebuild Container“**                            |
| `python: command not found`               | Терминал није прикачен; кликните **+** ➜ *bash*                 |
| `401 Unauthorized` од OpenAI              | Погрешан / истекао `OPENAI_API_KEY`                             |
| VS Code приказује „Dev container mounting…“ | Освежите картицу у прегледачу — Codespaces понекад губи везу        |
| Недостаје notebook kernel                 | Мени у notebook-у ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   За Unix-системе:

   ```bash
   touch .env
   ```

   За Windows:

   ```cmd
   echo . > .env
   ```

3. **Уредите `.env` фајл**: Отворите `.env` фајл у уређивачу текста (нпр. VS Code, Notepad++ или неки други уређивач). Додајте следећу линију у фајл, замењујући `your_github_token_here` својим стварним GitHub токеном:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Сачувајте фајл**: Сачувајте измене и затворите уређивач текста.

5. **Инсталирајте `python-dotenv`**: Ако већ нисте, потребно је да инсталирате `python-dotenv` пакет како бисте учитали променљиве окружења из `.env` фајла у своју Python апликацију. Можете га инсталирати преко `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Учитајте променљиве окружења у свој Python скрипт**: У свом Python скрипту користите `python-dotenv` пакет да учитате променљиве окружења из `.env` фајла:

   ```python
   from dotenv import load_dotenv
   import os

   # Учитај променљиве окружења из .env фајла
   load_dotenv()

   # Приступи променљивој GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

То је то! Успешно сте креирали `.env` фајл, додали свој GitHub токен и учитали га у своју Python апликацију.

## Како покренути локално на рачунару

Да бисте покренули код локално на свом рачунару, потребно је да имате инсталирану неку верзију [Python-а](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Затим, да бисте користили репозиторijум, морате га клонити:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Када сте све проверили, можете почети!

## Опциони кораци

### Инсталација Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) је лагани инсталер за инсталацију [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-а и неколико пакета.
Сама Conda је менаџер пакета који олакшава постављање и пребацивање између различитих Python [**виртуалних окружења**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) и пакета. Такође је корисна за инсталирање пакета који нису доступни преко `pip`.

Можете пратити [MiniConda водич за инсталацију](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) да бисте је подесили.

Када инсталирате Miniconda, потребно је да клоните [репозиторijум](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ако то већ нисте урадили)

Затим морате да направите виртуелно окружење. Да бисте то урадили помоћу Conde, направите нови фајл околине (_environment.yml_). Ако користите Codespaces, направите овај фајл унутар `.devcontainer` директоријума, односно `.devcontainer/environment.yml`.

Попуните свој фајл окружења следећим примером:

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

Ако добијате грешке приликом коришћења conda, можете ручно инсталирати Microsoft AI библиотеке користећи следећу команду у терминалу.

```
conda install -c microsoft azure-ai-ml
```

Фајл окружења одређује зависности које су нам потребне. `<environment-name>` се односи на име окружења које желите да користите, а `<python-version>` на верзију Python-а коју желите, на пример, `3` је најновија главна верзија Python-а.

Када завршите, можете направити своје Conda окружење покретањем следећих команди у командној линији/терминалу

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer под-путања се примењује само на Codespace подешавања
conda activate ai4beg
```

Погледајте [Conda упутство о окружењима](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ако наиђете на проблеме.

### Коришћење Visual Studio Code-а са Python додатком

Препоручујемо коришћење уређивача [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) са инсталираним [Python додатком](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) за овај курс. Међутим, ово је више препорука него ипак обавезан захтев.

> **Напомена**: Отварањем репозиторijума курса у VS Code-у, имате опцију да подесите пројекат унутар контејнера. То је због [специјалног `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) директоријума унутар репозиторijума курса. Више о томе касније.

> **Напомена**: Када клоните и отворите директоријум у VS Code-у, аутоматски ће вам предложити да инсталирате Python додатак.

> **Напомена**: Ако вам VS Code предложи да поново отворите репозиторijум у контејнеру, одбијте тај захтев да бисте користили локално инсталирану верзију Python-а.

### Коришћење Jupyter-а у прегледачу

Такође можете радити на пројекту користећи [Jupyter окружење](https://jupyter.org?WT.mc_id=academic-105485-koreyst) директно у вашем прегледачу. И класични Jupyter и [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) пружају угодно развојно окружење са функцијама као што су аутоматско допуњавање, истицање кода и сл.

Да бисте покренули Jupyter локално, идите у терминал/командну линију, идите у фасциклу са курсом и покрените:

```bash
jupyter notebook
```

или

```bash
jupyterhub
```

Ово ће покренути Jupyter инстанцу, а URL за приступ биће приказан у терминалу.

Када приступите URL-у, требало би да видите распоред курса и можете отворити било који `*.ipynb` фајл. На пример, `08-building-search-applications/python/oai-solution.ipynb`.

### Покретање у контејнеру

Алтернатива постављању свега на вашем рачунару или Codespace-у је коришћење [контејнера](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). Специјална `.devcontainer` фасцикла унутар репоа курса омогућава VS Code-у да подеси пројекат унутар контејнера. Изван Codespaces-а, ово захтева инсталацију Docker-а, а искрено, то укључује доста посла, па ову опцију препоручујемо само онима са искуством рада са контејнерима.

Један од најбољих начина да своје API кључеве држите безбедним приликом коришћења GitHub Codespaces-а је коришћење Codespace Secrets. Молимо пратите [упутство за управљање Codespaces тајнама](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) да сазнате више о овоме.

## Лекције и технички захтеви

Курс има 6 концептуалних лекција и 6 кодирачких лекција.

За кодирачке лекције користимо Azure OpenAI сервис. Потребан вам је приступ Azure OpenAI сервису и API кључ да покренете овај код. Можете се пријавити за приступ тако што ћете [попунити ову пријаву](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Док чекате да се ваша пријава обради, свака кодирачка лекција садржи и `README.md` фајл у којем можете видети код и резултате.

## Коришћење Azure OpenAI сервиса по први пут

Ако је ово ваш први пут да радите са Azure OpenAI сервисом, молимо пратите овај водич о томе како да [креирате и распоредите Azure OpenAI Service ресурс.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Коришћење OpenAI API-ja по први пут

Ако је ово ваш први пут да радите са OpenAI API-јем, молимо пратите водич о томе како да [креирате и користите интерфејс.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Упознајте друге учеснике

Креирали смо канале на нашем званичном [AI Community Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) за упознавање других учесника. Ово је одличан начин да ступите у контакт са другим предузетницима, креаторима, студентима и свима који желе да се унапреде у Генеративној вештачкој интелигенцији.

[![Придружите се discord каналу](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Тим пројекта ће такође бити на овом Discord серверу и помоћи свим учесницима.

## Допринос

Овај курс је иницијатива отвореног кода. Ако приметите области за побољшање или проблеме, молимо направите [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) или пријавите [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Тим пројекта прати све доприносе. Допринос отвореном коду је фантастичан начин да изградите своју каријеру у Генеративној вештачкој интелигенцији.

Већина доприноса захтева да се сложите са Уговором о лиценци за доприносе (CLA) који изјављује да имате право и заиста дајете нам права да користимо ваш допринос. За више детаља посетите [CLA, Чланак о лиценци за доприносе](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Важно: приликом превођења текста у овом репозиторијуму, молимо уверите се да не користите машински превод. Преводе ће верификовати заједница, па молимо пружите добровољни превод само за језике које добро познајете.

Када пошаљете pull request, CLA-бот ће аутоматски одредити да ли је потребно да доставите CLA и одговарајуће означити PR (нпр. етикета, коментар). Једноставно пратите упутства које пружа бот. Ово ћете морати урадити само једном за све репозиторијуме који користе наш CLA.

Овај пројекат је усвојио [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). За више информација прочитајте Често постављана питања о Кодексу понашања или контактирајте [Email opencode](opencode@microsoft.com) за додатна питања или коментаре.

## Хајде да почнемо
Сада када сте завршили потребне кораке за завршетак овог курса, хајде да почнемо тако што ћемо добити [увод у генеритивну вештачку интелигенцију и LLM-ове](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен помоћу AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског стручњака. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произлазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->