<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:37:13+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "bg"
}
-->
# Настройване на средата за разработка

Настроихме това хранилище и курса с [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), който има универсална среда за изпълнение, поддържаща Python3, .NET, Node.js и Java разработка. Свързаната конфигурация е дефинирана във файла `devcontainer.json`, намиращ се в папката `.devcontainer/` в корена на това хранилище.

За да активирате dev контейнера, стартирайте го в [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (за облачна среда за изпълнение) или в [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (за локална среда за изпълнение на устройството). Прочетете [тази документация](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) за повече подробности как работят dev контейнерите във VS Code.

> [!TIP]  
> Препоръчваме използването на GitHub Codespaces за бърз старт с минимални усилия. Той предлага щедър [безплатен лимит](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) за лични акаунти. Конфигурирайте [таймаути](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), за да спирате или изтривате неактивни codespaces и така да използвате максимално квотата си.

## 1. Изпълнение на задачи

Всяка лекция ще има _по избор_ задачи, които могат да бъдат предоставени на един или повече програмни езици, включително: Python, .NET/C#, Java и JavaScript/TypeScript. Този раздел дава общи насоки за изпълнението на тези задачи.

### 1.1 Python задачи

Python задачите се предоставят като приложения (`.py` файлове) или Jupyter notebooks (`.ipynb` файлове).  
- За да стартирате notebook, отворете го във Visual Studio Code, след това кликнете върху _Select Kernel_ (в горния десен ъгъл) и изберете показаната по подразбиране опция Python 3. След това можете да изберете _Run All_, за да изпълните целия notebook.  
- За да стартирате Python приложения от командния ред, следвайте инструкциите, специфични за задачата, за да изберете правилните файлове и да подадете необходимите аргументи.

## 2. Конфигуриране на доставчици

Задачите **могат** да бъдат настроени да работят с един или повече Large Language Model (LLM) деплойменти чрез поддържан доставчик на услуги като OpenAI, Azure или Hugging Face. Те предоставят _хостван крайна точка_ (API), до която можем да имаме достъп програмно с правилните идентификационни данни (API ключ или токен). В този курс разглеждаме следните доставчици:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразни модели, включително основната серия GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI модели с фокус върху корпоративна готовност  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за отворени модели и inference сървър

**Ще трябва да използвате собствени акаунти за тези упражнения**. Задачите са по избор, така че можете да настроите един, всички или нито един от доставчиците според интересите си. Някои насоки за регистрация:

| Регистрация | Цена | API ключ | Playground | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Ценоразпис](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Проектно-базиран](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без код, уеб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Налични множество модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Ценоразпис](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Трябва да кандидатствате предварително за достъп](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ценоразпис](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat има ограничен набор от модели](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Следвайте указанията по-долу, за да _конфигурирате_ това хранилище за работа с различни доставчици. Задачите, които изискват конкретен доставчик, ще съдържат един от тези тагове в името на файла:  
 - `aoai` - изисква Azure OpenAI крайна точка и ключ  
 - `oai` - изисква OpenAI крайна точка и ключ  
 - `hf` - изисква Hugging Face токен

Можете да конфигурирате един, нито един или всички доставчици. Свързаните задачи просто ще дадат грешка при липса на идентификационни данни.

### 2.1. Създаване на `.env` файл

Предполагаме, че вече сте прочели горните указания, регистрирали сте се при съответния доставчик и сте получили необходимите идентификационни данни (API_KEY или токен). В случай на Azure OpenAI, предполагаме, че имате валидно разгръщане на Azure OpenAI Service (крайна точка) с поне един GPT модел, разположен за чат.

Следващата стъпка е да конфигурирате **локалните променливи на средата** по следния начин:

1. Потърсете в кореновата папка файл `.env.copy`, който трябва да съдържа нещо подобно на:

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

2. Копирайте този файл като `.env` с командата по-долу. Този файл е _gitignore-нат_, за да пази тайните.

   ```bash
   cp .env.copy .env
   ```

3. Попълнете стойностите (заменете плейсхолдърите вдясно от `=`) както е описано в следващия раздел.

3. (Опция) Ако използвате GitHub Codespaces, имате възможност да запазите променливите на средата като _Codespaces secrets_, свързани с това хранилище. В този случай няма да е нужно да настройвате локален .env файл. **Обаче, имайте предвид, че тази опция работи само ако използвате GitHub Codespaces.** Все пак ще трябва да настроите .env файла, ако използвате Docker Desktop.

### 2.2. Попълване на `.env` файла

Нека бързо разгледаме имената на променливите, за да разберем какво представляват:

| Променлива  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Това е потребителският токен за достъп, който сте настроили в профила си |
| OPENAI_API_KEY | Това е ключът за упълномощаване за използване на услугата за не-Azure OpenAI крайни точки |
| AZURE_OPENAI_API_KEY | Това е ключът за упълномощаване за използване на тази услуга |
| AZURE_OPENAI_ENDPOINT | Това е разположената крайна точка за Azure OpenAI ресурс |
| AZURE_OPENAI_DEPLOYMENT | Това е крайна точка за разгръщане на _текстогенериращ_ модел |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Това е крайна точка за разгръщане на _текстови embeddings_ модел |
| | |

Забележка: Последните две променливи за Azure OpenAI отразяват по подразбиране модел за чат (текстогенериране) и за векторно търсене (embeddings). Инструкциите за настройка ще бъдат описани в съответните задачи.

### 2.3 Конфигуриране на Azure: От портала

Стойностите за крайна точка и ключ за Azure OpenAI могат да бъдат намерени в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), така че нека започнем оттам.

1. Отидете в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Кликнете върху опцията **Keys and Endpoint** в страничното меню (вляво).  
1. Кликнете върху **Show Keys** - трябва да видите следното: KEY 1, KEY 2 и Endpoint.  
1. Използвайте стойността на KEY 1 за AZURE_OPENAI_API_KEY  
1. Използвайте стойността на Endpoint за AZURE_OPENAI_ENDPOINT

След това ни трябват крайните точки за конкретните модели, които сме разположили.

1. Кликнете върху опцията **Model deployments** в страничното меню (вляво) за Azure OpenAI ресурса.  
1. В страницата, която се отваря, кликнете върху **Manage Deployments**

Това ще ви отведе до уебсайта на Azure OpenAI Studio, където ще намерим останалите стойности, както е описано по-долу.

### 2.4 Конфигуриране на Azure: От Studio

1. Навигирайте до [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **от вашия ресурс**, както е описано по-горе.  
1. Кликнете върху таба **Deployments** (странично меню, вляво), за да видите текущо разположените модели.  
1. Ако желаният модел не е разположен, използвайте **Create new deployment**, за да го разположите.  
1. Ще ви трябва _текстогенериращ_ модел - препоръчваме: **gpt-35-turbo**  
1. Ще ви трябва _текстов embedding_ модел - препоръчваме **text-embedding-ada-002**

Сега актуализирайте променливите на средата, за да отразяват името на _Deployment_, което използвате. Обикновено това е същото като името на модела, освен ако не сте го променили изрично. Например, може да имате:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забравяйте да запазите .env файла след като приключите**. Можете да затворите файла и да се върнете към инструкциите за стартиране на notebook-а.

### 2.5 Конфигуриране на OpenAI: От профила

Вашият OpenAI API ключ може да бъде намерен във вашия [OpenAI акаунт](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако нямате такъв, можете да се регистрирате и да създадете API ключ. След като имате ключа, използвайте го, за да попълните променливата `OPENAI_API_KEY` в `.env` файла.

### 2.6 Конфигуриране на Hugging Face: От профила

Вашият Hugging Face токен може да бъде намерен в профила ви под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикувайте и не споделяйте тези токени публично. Вместо това, създайте нов токен за използване в този проект и го копирайте в `.env` файла под променливата `HUGGING_FACE_API_KEY`. _Забележка:_ Технически това не е API ключ, но се използва за удостоверяване, затова запазваме това наименование за последователност.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.