<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:30:20+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sr"
}
-->
# Подешавање Вашег Развојног Окружења

Ми смо подесили овај репозиторијум и курс са [развојним контејнером](https://containers.dev?WT.mc_id=academic-105485-koreyst) који има универзално окружење које може подржати развој на Python3, .NET, Node.js и Java. Повезана конфигурација је дефинисана у `devcontainer.json` датотеци која се налази у `.devcontainer/` фасцикли на корену овог репозиторијума.

Да бисте активирали развојни контејнер, покрените га у [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (за окружење хостовано у облаку) или у [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (за окружење хостовано на локалном уређају). Прочитајте [ову документацију](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) за више детаља о томе како развојни контејнери раде у оквиру VS Code.

> [!TIP]  
> Препоручујемо коришћење GitHub Codespaces за брзи почетак уз минималан напор. Пружа великодушну [бесплатну квоту коришћења](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) за личне налоге. Конфигуришите [временске ограничења](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) да зауставите или избришете неактивне codespaces како бисте максимизовали своју квоту.

## 1. Извршавање Задатака

Свака лекција ће имати _опционе_ задатке који могу бити дати у једном или више програмских језика, укључујући: Python, .NET/C#, Java и JavaScript/TypeScript. Овај одељак пружа опште смернице у вези са извршавањем тих задатака.

### 1.1 Задаци у Python-у

Python задаци су дати или као апликације (`.py` датотеке) или Jupyter свеске (`.ipynb` датотеке).
- Да бисте покренули свеску, отворите је у Visual Studio Code, затим кликните на _Select Kernel_ (горе десно) и изаберите подразумевану Python 3 опцију која је приказана. Сада можете кликнути на _Run All_ да извршите свеску.
- Да бисте покренули Python апликације из командне линије, пратите специфична упутства за задатке како бисте осигурали да одаберете праве датотеке и обезбедите потребне аргументе.

## 2. Конфигурисање Провајдера

Задаци **могу** такође бити подешени да раде против једне или више имплементација великог језичког модела (LLM) преко подржаног провајдера услуга као што су OpenAI, Azure или Hugging Face. Ови провајдери пружају _хостовани крајњи тачка_ (API) који можемо програмски приступити са правим акредитацијама (API кључ или токен). У овом курсу, разматрамо следеће провајдере:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) са различитим моделима укључујући основну серију GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI моделе са фокусом на спремност за предузећа.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за моделе отвореног кода и сервер за инференцију.

**Требаће вам ваши налози за ове вежбе**. Задаци су опциони, тако да можете изабрати да подесите један, све - или ниједан - од провајдера у зависности од ваших интересовања. Неке смернице за регистрацију:

| Регистрација | Цена | API Кључ | Игралиште | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цене](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Пројектно базирано](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без кода, веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступни су различити модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цене](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Брзи почетак SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Брзи почетак студија](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Мора се унапред пријавити за приступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цене](https://huggingface.co/pricing) | [Приступни токени](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничене моделе](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Пратите доле наведена упутства да _конфигуришете_ овај репозиторијум за употребу са различитим провајдерима. Задаци који захтевају специфичног провајдера ће садржати један од ових ознака у свом имену датотеке:
 - `aoai` - захтева Azure OpenAI крајњу тачку, кључ
 - `oai` - захтева OpenAI крајњу тачку, кључ
 - `hf` - захтева Hugging Face токен

Можете конфигурисати једног, ниједног, или све провајдере. Повезани задаци ће једноставно јавити грешку у случају недостатка акредитација.

### 2.1. Креирање `.env` датотеке

Претпостављамо да сте већ прочитали горе наведене смернице и регистровали се код релевантног провајдера, и добили потребне акредитације за аутентификацију (API_KEY или токен). У случају Azure OpenAI, претпостављамо да такође имате важећу имплементацију Azure OpenAI услуге (крајња тачка) са бар једним GPT моделом имплементираним за завршетак чата.

Следећи корак је да конфигуришете своје **локалне променљиве окружења** на следећи начин:

1. Погледајте у коренску фасциклу за `.env.copy` датотеку која би требало да има садржај као што је овај:

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

2. Копирајте ту датотеку у `.env` користећи команду испод. Ова датотека је _gitignore-д_, чувајући тајне безбедним.

   ```bash
   cp .env.copy .env
   ```

3. Попуните вредности (замените резервисана места на десној страни `=`) као што је описано у следећем одељку.

3. (Опција) Ако користите GitHub Codespaces, имате опцију да сачувате променљиве окружења као _Codespaces тајне_ повезане са овим репозиторијумом. У том случају, нећете морати да подешавате локалну .env датотеку. **Међутим, напомињемо да ова опција ради само ако користите GitHub Codespaces.** И даље ћете морати да подесите .env датотеку ако користите Docker Desktop.

### 2.2. Попуњавање `.env` датотеке

Погледајмо брзо имена променљивих да разумемо шта представљају:

| Променљива  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ово је приступни токен корисника који сте поставили у свом профилу |
| OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење услуге за не-Azure OpenAI крајње тачке |
| AZURE_OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење те услуге |
| AZURE_OPENAI_ENDPOINT | Ово је имплементирана крајња тачка за Azure OpenAI ресурс |
| AZURE_OPENAI_DEPLOYMENT | Ово је _имплементациона_ крајња тачка модела за генерисање текста |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ово је _имплементациона_ крајња тачка модела за текстуалне уградње |
| | |

Напомена: Последње две Azure OpenAI променљиве одражавају подразумевани модел за завршетак чата (генерисање текста) и претрагу вектора (уградње) респективно. Упутства за њихово подешавање биће дефинисана у релевантним задацима.

### 2.3 Конфигуришите Azure: Из Портала

Azure OpenAI крајња тачка и вредности кључа ће бити пронађени у [Azure Порталу](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), па хајде да почнемо тамо.

1. Идите на [Azure Портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликните на опцију **Кључеви и крајња тачка** у бочној траци (мени са леве стране).
1. Кликните на **Прикажи кључеве** - требало би да видите следеће: КЉУЧ 1, КЉУЧ 2 и крајња тачка.
1. Користите вредност КЉУЧ 1 за AZURE_OPENAI_API_KEY
1. Користите вредност крајње тачке за AZURE_OPENAI_ENDPOINT

Следеће, потребне су нам крајње тачке за специфичне моделе које смо имплементирали.

1. Кликните на опцију **Имплементације модела** у бочној траци (леви мени) за Azure OpenAI ресурс.
1. На одредишној страници, кликните на **Управљање имплементацијама**

Ово ће вас одвести на Azure OpenAI Studio вебсајт, где ћемо пронаћи друге вредности као што је описано у наставку.

### 2.4 Конфигуришите Azure: Из Студија

1. Идите на [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **из вашег ресурса** као што је горе описано.
1. Кликните на таб **Имплементације** (бочна трака, лево) да видите тренутно имплементиране моделе.
1. Ако ваш жељени модел није имплементиран, користите **Креирај нову имплементацију** да га имплементирате.
1. Потребан вам је модел за _генерисање текста_ - препоручујемо: **gpt-35-turbo**
1. Потребан вам је модел за _текстуалне уградње_ - препоручујемо **text-embedding-ada-002**

Сада ажурирајте променљиве окружења да одражавају _Име имплементације_ које сте користили. Ово ће обично бити исто као име модела осим ако га нисте експлицитно променили. Дакле, као пример, можете имати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не заборавите да сачувате .env датотеку када завршите**. Сада можете изаћи из датотеке и вратити се на упутства за покретање свеске.

### 2.5 Конфигуришите OpenAI: Из Профила

Ваш OpenAI API кључ се може пронаћи у вашем [OpenAI налогу](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако га немате, можете се пријавити за налог и креирати API кључ. Када добијете кључ, можете га користити да попуните `OPENAI_API_KEY` променљиву у `.env` датотеци.

### 2.6 Конфигуришите Hugging Face: Из Профила

Ваш Hugging Face токен се може пронаћи у вашем профилу под [Приступни токени](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Немојте их објављивати или делити јавно. Уместо тога, креирајте нови токен за ову пројектну употребу и копирајте га у `.env` датотеку под `HUGGING_FACE_API_KEY` променљивом. _Напомена:_ Ово технички није API кључ, али се користи за аутентификацију, тако да задржавамо ту конвенцију именовања ради доследности.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која могу произаћи из коришћења овог превода.