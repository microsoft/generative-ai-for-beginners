<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:37:39+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sr"
}
-->
# Подешавање вашег развојног окружења

Овај репозиторијум и курс су подешени са [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) који има универзално окружење за извршавање које подржава Python3, .NET, Node.js и Java развој. Потребна конфигурација је дефинисана у фајлу `devcontainer.json` који се налази у фасцикли `.devcontainer/` у корену овог репозиторијума.

Да бисте активирали дев контејнер, покрените га у [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (за cloud-hosted runtime) или у [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (за локално окружење). Прочитајте [ову документацију](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) за више детаља о томе како дев контејнери функционишу у VS Code-у.

> [!TIP]  
> Препоручујемо коришћење GitHub Codespaces-а за брз почетак уз минималан напор. Он пружа великодушан [бесплатни квоту](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) за личне налоге. Конфигуришите [таймауте](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) за заустављање или брисање неактивних codespaces-а како бисте максимално искористили квоту.

## 1. Извршавање задатака

Свака лекција ће имати _опционалне_ задатке који могу бити доступни у једном или више програмских језика, укључујући: Python, .NET/C#, Java и JavaScript/TypeScript. Овај одељак даје општа упутства у вези са извршавањем тих задатака.

### 1.1 Python задаци

Python задаци су доступни као апликације (`.py` фајлови) или Jupyter бележнице (`.ipynb` фајлови).  
- Да бисте покренули бележницу, отворите је у Visual Studio Code-у, затим кликните на _Select Kernel_ (горе десно) и изаберите подразумевану Python 3 опцију. Сада можете кликнути на _Run All_ да извршите бележницу.  
- За покретање Python апликација из командне линије, пратите упутства специфична за задатак како бисте изабрали праве фајлове и проследили потребне аргументе.

## 2. Конфигурисање провајдера

Задаци **могу** бити подешени да раде са једним или више Large Language Model (LLM) сервиса преко подржаних провајдера као што су OpenAI, Azure или Hugging Face. Они пружају _hosted endpoint_ (API) којем можемо приступити програмски уз одговарајуће креденцијале (API кључ или токен). У овом курсу ћемо радити са следећим провајдерима:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) са разноврсним моделима укључујући основну GPT серију.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI моделе са фокусом на спремност за предузећа  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за open-source моделе и inference сервер

**За ове вежбе ћете морати да користите своје налоге**. Задаци су опциони, па можете изабрати да подесите једног, све или ниједног од провајдера у складу са својим интересовањима. Нека упутства за регистрацију:

| Регистрација | Цена | API кључ | Playground | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цене](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Пројектно базирано](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без кода, веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Више доступних модела |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цене](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потребна претходна пријава за приступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цене](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничене моделе](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Пратите упутства испод да _конфигуришете_ овај репозиторијум за рад са различитим провајдерима. Задаци који захтевају одређеног провајдера имаће једну од ових ознака у имену фајла:  
 - `aoai` - захтева Azure OpenAI endpoint и кључ  
 - `oai` - захтева OpenAI endpoint и кључ  
 - `hf` - захтева Hugging Face токен

Можете подесити једног, ниједног или све провајдере. Задаци који захтевају одређеног провајдера ће пријавити грешку ако креденцијали недостају.

###  2.1. Креирање `.env` фајла

Претпостављамо да сте већ прочитали горе наведена упутства, регистровали се код релевантног провајдера и добили потребне аутентификационе креденцијале (API_KEY или токен). У случају Azure OpenAI, претпостављамо да имате важећу имплементацију Azure OpenAI сервиса (endpoint) са најмање једним GPT моделом за chat completion.

Следећи корак је да подесите своје **локалне променљиве окружења** на следећи начин:

1. Потражите у корену пројекта `.env.copy` фајл који би требало да садржи нешто овако:

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

2. Копирајте тај фајл у `.env` користећи команду испод. Овај фајл је _gitignore-ован_, што значи да тајне остају безбедне.

   ```bash
   cp .env.copy .env
   ```

3. Попуните вредности (замените плейсхолдере са десне стране знака `=`) како је описано у следећем одељку.

3. (Опционо) Ако користите GitHub Codespaces, имате могућност да сачувате променљиве окружења као _Codespaces secrets_ повезане са овим репозиторијумом. У том случају не морате да подешавате локални `.env` фајл. **Међутим, имајте на уму да ова опција ради само ако користите GitHub Codespaces.** Ако користите Docker Desktop, и даље морате да подесите `.env` фајл.

### 2.2. Попуњавање `.env` фајла

Хајде да брзо погледамо имена променљивих да бисмо разумели шта представљају:

| Променљива  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ово је кориснички приступни токен који сте подесили у свом профилу |
| OPENAI_API_KEY | Ово је ауторизациони кључ за коришћење сервиса за non-Azure OpenAI endpoint-ове |
| AZURE_OPENAI_API_KEY | Ово је ауторизациони кључ за коришћење тог сервиса |
| AZURE_OPENAI_ENDPOINT | Ово је endpoint за Azure OpenAI ресурс који сте имплементирали |
| AZURE_OPENAI_DEPLOYMENT | Ово је endpoint за deployment _text generation_ модела |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ово је endpoint за deployment _text embeddings_ модела |
| | |

Напомена: Последње две Azure OpenAI променљиве одговарају подразумеваном моделу за chat completion (генерисање текста) и претрагу вектора (ембеддинзи). Упутства за њихово подешавање биће дефинисана у релевантним задацима.

### 2.3. Конфигурисање Azure: Са портала

Вредности за Azure OpenAI endpoint и кључ можете пронаћи у [Azure порталу](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), па хајде да почнемо одатле.

1. Идите на [Azure портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Кликните на опцију **Keys and Endpoint** у бочној траци (леви мени).  
1. Кликните на **Show Keys** - требало би да видите: KEY 1, KEY 2 и Endpoint.  
1. Користите вредност KEY 1 за AZURE_OPENAI_API_KEY  
1. Користите вредност Endpoint за AZURE_OPENAI_ENDPOINT

Затим нам требају endpoint-ови за конкретне моделе које сте имплементирали.

1. Кликните на опцију **Model deployments** у бочној траци (леви мени) за Azure OpenAI ресурс.  
1. На страници која се отвори, кликните на **Manage Deployments**

Ово ће вас одвести на веб сајт Azure OpenAI Studio, где ћете пронаћи остале вредности како је описано у наставку.

### 2.4. Конфигурисање Azure: Са студија

1. Идите на [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **са свог ресурса** као што је описано горе.  
1. Кликните на таб **Deployments** (бочна трака, лево) да бисте видели тренутно имплементиране моделе.  
1. Ако ваш жељени модел није имплементиран, користите **Create new deployment** да га имплементирате.  
1. Потребан вам је _text-generation_ модел - препоручујемо: **gpt-35-turbo**  
1. Потребан вам је _text-embedding_ модел - препоручујемо **text-embedding-ada-002**

Сада ажурирајте променљиве окружења да одговарају имену _Deployment_-а који користите. Обично ће то бити исто као име модела, осим ако га нисте експлицитно променили. На пример, можете имати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не заборавите да сачувате .env фајл када завршите**. Сада можете изаћи из фајла и вратити се упутствима за покретање бележнице.

### 2.5. Конфигурисање OpenAI: Са профила

Ваш OpenAI API кључ можете пронаћи у свом [OpenAI налогу](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако га немате, можете се регистровати и креирати API кључ. Када добијете кључ, користите га да попуните променљиву `OPENAI_API_KEY` у `.env` фајлу.

### 2.6. Конфигурисање Hugging Face: Са профила

Ваш Hugging Face токен можете пронаћи у свом профилу под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Немојте их објављивати или делити јавно. Уместо тога, креирајте нови токен за ову употребу у пројекту и копирајте га у `.env` фајл под променљиву `HUGGING_FACE_API_KEY`. _Напомена:_ Технички ово није API кључ, али се користи за аутентификацију, па смо задржали ову конвенцију именовања ради доследности.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.