<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T13:00:07+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "bg"
}
-->
# Настройте вашата среда за разработка

Настроихме това хранилище и курс с [контейнер за разработка](https://containers.dev?WT.mc_id=academic-105485-koreyst), който има универсална среда, която може да поддържа разработка на Python3, .NET, Node.js и Java. Свързаната конфигурация е дефинирана в файла `devcontainer.json`, намиращ се в папката `.devcontainer/` в корена на това хранилище.

За да активирате контейнера за разработка, го стартирайте в [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (за среда, хоствана в облака) или в [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (за среда, хоствана на локално устройство). Прочетете [тази документация](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) за повече подробности относно как работят контейнерите за разработка във VS Code.

> [!TIP]  
> Препоръчваме използването на GitHub Codespaces за бърз старт с минимални усилия. Той предоставя щедра [безплатна квота за използване](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) за лични акаунти. Настройте [таймаути](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), за да спрете или изтриете неактивни кодспейси, за да максимизирате използването на вашата квота.


## 1. Изпълнение на задачи

Всяка лекция ще има _опционални_ задачи, които могат да бъдат предоставени на един или повече програмни езици, включително: Python, .NET/C#, Java и JavaScript/TypeScript. Този раздел предоставя общи насоки, свързани с изпълнението на тези задачи.

### 1.1 Задачи на Python

Задачите на Python се предоставят или като приложения (`.py` файлове), или като Jupyter notebooks (`.ipynb` файлове).
- За да изпълните notebook, отворете го в Visual Studio Code и след това кликнете върху _Select Kernel_ (горе вдясно) и изберете показаната опция за Python 3 по подразбиране. Сега можете да използвате _Run All_, за да изпълните notebook.
- За да изпълните Python приложения от командния ред, следвайте специфичните инструкции за задачи, за да се уверите, че избирате правилните файлове и предоставяте необходимите аргументи.

## 2. Конфигуриране на доставчици

Задачите **могат** също да бъдат настроени да работят срещу едно или повече разгръщания на Голям езиков модел (LLM) чрез поддържан доставчик на услуги като OpenAI, Azure или Hugging Face. Те предоставят _хостван крайна точка_ (API), до която можем да получим достъп програмно с правилните идентификационни данни (API ключ или токен). В този курс обсъждаме тези доставчици:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразни модели, включително основната серия GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI модели с акцент върху готовността за предприятия
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за модели с отворен код и сървър за изводи

**Ще трябва да използвате свои собствени акаунти за тези упражнения**. Задачите са опционални, така че можете да изберете да настроите един, всички или нито един от доставчиците въз основа на вашите интереси. Някои насоки за регистрация:

| Регистрация | Цена | API ключ | Playground | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цени](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Базиран на проект](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без код, уеб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Налични са множество модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цени](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Бърз старт на SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Бърз старт на Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Трябва да се кандидатства предварително за достъп](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цени](https://huggingface.co/pricing) | [Токени за достъп](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничени модели](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Следвайте указанията по-долу, за да _конфигурирате_ това хранилище за използване с различни доставчици. Задачите, които изискват конкретен доставчик, ще съдържат един от тези тагове в името на файла:
 - `aoai` - изисква крайна точка и ключ на Azure OpenAI
 - `oai` - изисква крайна точка и ключ на OpenAI
 - `hf` - изисква токен на Hugging Face

Можете да конфигурирате един, нито един или всички доставчици. Свързаните задачи просто ще дадат грешка при липсващи идентификационни данни.

###  2.1. Създайте `.env` файл

Предполагаме, че вече сте прочели указанията по-горе и сте се регистрирали при съответния доставчик, и сте получили необходимите идентификационни данни за удостоверяване (API_KEY или токен). В случай на Azure OpenAI, предполагаме, че имате и валидно разгръщане на услуга Azure OpenAI (крайна точка) с поне един GPT модел, разположен за завършване на чат.

Следващата стъпка е да конфигурирате вашите **локални променливи на средата**, както следва:


1. Потърсете в кореновата папка файл `.env.copy`, който трябва да има съдържание като това:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копирайте този файл в `.env`, използвайки командата по-долу. Този файл е _gitignore-d_, като пази тайни в безопасност.

   ```bash
   cp .env.copy .env
   ```

3. Попълнете стойностите (заменете плейсхолдерите от дясната страна на `=`), както е описано в следващия раздел.

3. (Опция) Ако използвате GitHub Codespaces, имате опцията да запазите променливите на средата като _тайни на Codespaces_, свързани с това хранилище. В този случай няма да е необходимо да настройвате локален .env файл. **Обаче, имайте предвид, че тази опция работи само ако използвате GitHub Codespaces.** Все още ще трябва да настроите .env файла, ако използвате Docker Desktop.


### 2.2. Попълнете `.env` файл

Нека разгледаме бързо имената на променливите, за да разберем какво представляват:

| Променлива  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Това е токенът за достъп, който настройвате във вашия профил |
| OPENAI_API_KEY | Това е ключът за удостоверяване за използване на услугата за не-Azure OpenAI крайни точки |
| AZURE_OPENAI_API_KEY | Това е ключът за удостоверяване за използване на тази услуга |
| AZURE_OPENAI_ENDPOINT | Това е разположената крайна точка за ресурс Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Това е крайна точка за разгръщане на _генерация на текст_ модел |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Това е крайна точка за разгръщане на _вграждане на текст_ модел |
| | |

Забележка: Последните две променливи на Azure OpenAI отразяват модел по подразбиране за завършване на чат (генерация на текст) и търсене на вектори (вграждания) съответно. Указанията за тяхното настройване ще бъдат дефинирани в съответните задачи.


### 2.3 Конфигурирайте Azure: От портала

Стойностите за крайна точка и ключ на Azure OpenAI ще бъдат намерени в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), така че нека започнем там.

1. Отидете на [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликнете върху опцията **Keys and Endpoint** в страничната лента (меню вляво).
1. Кликнете върху **Show Keys** - трябва да видите следното: KEY 1, KEY 2 и Endpoint.
1. Използвайте стойността KEY 1 за AZURE_OPENAI_API_KEY
1. Използвайте стойността на Endpoint за AZURE_OPENAI_ENDPOINT

След това ни трябват крайни точки за конкретните модели, които сме разположили.

1. Кликнете върху опцията **Model deployments** в страничната лента (ляво меню) за ресурс Azure OpenAI.
1. На целевата страница кликнете върху **Manage Deployments**

Това ще ви отведе до уебсайта Azure OpenAI Studio, където ще намерим другите стойности, както е описано по-долу.

### 2.4 Конфигурирайте Azure: От студиото

1. Навигирайте до [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **от вашия ресурс**, както е описано по-горе.
1. Кликнете върху таба **Deployments** (страничната лента, вляво), за да видите текущо разположените модели.
1. Ако вашият желан модел не е разположен, използвайте **Create new deployment**, за да го разположите.
1. Ще ви трябва _модел за генерация на текст_ - препоръчваме: **gpt-35-turbo**
1. Ще ви трябва _модел за вграждане на текст_ - препоръчваме **text-embedding-ada-002**

Сега актуализирайте променливите на средата, за да отразяват _името на разгръщането_, което сте използвали. Това обикновено ще бъде същото като името на модела, освен ако не сте го променили изрично. Така че, като пример, може да имате:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забравяйте да запазите .env файла, когато сте готови**. Можете сега да излезете от файла и да се върнете към инструкциите за изпълнение на notebook.

### 2.5 Конфигурирайте OpenAI: От профила

Вашият OpenAI API ключ може да бъде намерен във вашия [OpenAI акаунт](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако нямате такъв, можете да се регистрирате за акаунт и да създадете API ключ. След като имате ключа, можете да го използвате, за да попълните променливата `OPENAI_API_KEY` в `.env` файла.

### 2.6 Конфигурирайте Hugging Face: От профила

Вашият Hugging Face токен може да бъде намерен във вашия профил под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не ги публикувайте или споделяйте публично. Вместо това, създайте нов токен за използване на този проект и го копирайте в `.env` файла под променливата `HUGGING_FACE_API_KEY`. _Забележка:_ Технически това не е API ключ, но се използва за удостоверяване, така че запазваме тази конвенция за именуване за последователност.

**Отказ от отговорност**: 
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или неправилни интерпретации, произтичащи от използването на този превод.