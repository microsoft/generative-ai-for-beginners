<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:29:23+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sr"
}
-->
# Избор и подешавање LLM провајдера 🔑

Задаци **могу** бити подешени да раде са једним или више Large Language Model (LLM) деплојмената преко подржаних сервис провајдера као што су OpenAI, Azure или Hugging Face. Ови провајдери обезбеђују _хостирани ендпоинт_ (API) који можемо да користимо програмски уз одговарајуће акредитиве (API кључ или токен). У овом курсу, говоримо о следећим провајдерима:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) са разноврсним моделима, укључујући основну GPT серију.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI моделе са фокусом на пословну употребу
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за open-source моделе и inference сервер

**За ове вежбе ће вам бити потребни сопствени налози**. Задаци су опционо, тако да можете изабрати да подесите једног, све – или ниједног – од провајдера, у зависности од ваших интересовања. Неколико савета за регистрацију:

| Регистрација | Цена | API кључ | Playground | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цене](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [По пројекту](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Више модела доступно |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цене](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потребно је унапред аплицирати за приступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цене](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничен број модела](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Пратите упутства испод да _подесите_ овај репозиторијум за рад са различитим провајдерима. Задаци који захтевају одређеног провајдера имаће једну од ових ознака у имену фајла:

- `aoai` - захтева Azure OpenAI ендпоинт и кључ
- `oai` - захтева OpenAI ендпоинт и кључ
- `hf` - захтева Hugging Face токен

Можете подесити једног, ниједног или све провајдере. Повезани задаци ће једноставно јавити грешку ако недостају акредитиви.

## Креирање `.env` фајла

Претпостављамо да сте већ прочитали горња упутства, регистровали се код релевантног провајдера и добили потребне акредитиве (API_KEY или токен). У случају Azure OpenAI, претпостављамо да већ имате важећи деплојмент Azure OpenAI сервиса (ендпоинт) са бар једним GPT моделом постављеним за chat completion.

Следећи корак је да подесите своје **локалне променљиве окружења** на следећи начин:

1. Потражите у root фасцикли `.env.copy` фајл који би требало да садржи нешто овако:

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

2. Копирајте тај фајл у `.env` помоћу следеће команде. Овај фајл је _gitignore-ован_, што чува ваше податке безбедним.

   ```bash
   cp .env.copy .env
   ```

3. Упишите вредности (замените placeholder-е десно од `=`) како је описано у следећем одељку.

4. (Опционо) Ако користите GitHub Codespaces, имате могућност да сачувате променљиве окружења као _Codespaces secrets_ повезане са овим репозиторијумом. У том случају, нећете морати да подешавате локални .env фајл. **Међутим, имајте у виду да ова опција ради само ако користите GitHub Codespaces.** И даље ћете морати да подесите .env фајл ако користите Docker Desktop.

## Попуњавање `.env` фајла

Погледајмо брзо имена променљивих да бисмо разумели шта представљају:

| Променљива  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ово је кориснички access token који сте подесили у свом профилу |
| OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење сервиса за non-Azure OpenAI ендпоинте |
| AZURE_OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење тог сервиса |
| AZURE_OPENAI_ENDPOINT | Ово је деплојовани ендпоинт за Azure OpenAI ресурс |
| AZURE_OPENAI_DEPLOYMENT | Ово је _text generation_ модел деплојмент ендпоинт |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ово је _text embeddings_ модел деплојмент ендпоинт |
| | |

Напомена: Последње две Azure OpenAI променљиве представљају подразумевани модел за chat completion (генерисање текста) и претрагу вектора (embeddings). Упутства за њихово подешавање биће дата у релевантним задацима.

## Подешавање Azure: Преко портала

Azure OpenAI ендпоинт и кључ ћете пронаћи у [Azure порталу](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), па кренимо одатле.

1. Идите на [Azure портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликните на опцију **Keys and Endpoint** у бочној траци (мени са леве стране).
1. Кликните на **Show Keys** – требало би да видите: KEY 1, KEY 2 и Endpoint.
1. Вредност KEY 1 користите за AZURE_OPENAI_API_KEY
1. Вредност Endpoint користите за AZURE_OPENAI_ENDPOINT

Затим нам требају ендпоинти за конкретне моделе које смо деплојовали.

1. Кликните на опцију **Model deployments** у бочној траци (леви мени) за Azure OpenAI ресурс.
1. На одредишној страници кликните на **Manage Deployments**

Ово ће вас одвести на Azure OpenAI Studio сајт, где ћемо пронаћи остале вредности као што је описано испод.

## Подешавање Azure: Преко Studio

1. Идите на [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **са свог ресурса** као што је горе описано.
1. Кликните на таб **Deployments** (бочна трака, лево) да видите тренутно деплојоване моделе.
1. Ако жељени модел није деплојован, користите **Create new deployment** да га деплојујете.
1. Потребан вам је _text-generation_ модел – препоручујемо: **gpt-35-turbo**
1. Потребан вам је _text-embedding_ модел – препоручујемо **text-embedding-ada-002**

Сада ажурирајте променљиве окружења тако да одговарају _Deployment name_ који сте користили. То ће обично бити исто као и име модела, осим ако га нисте експлицитно променили. На пример, можете имати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не заборавите да сачувате .env фајл када завршите**. Сада можете изаћи из фајла и вратити се на упутства за покретање нотебука.

## Подешавање OpenAI: Преко профила

Ваш OpenAI API кључ можете пронаћи у свом [OpenAI налогу](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако га немате, можете се регистровати и креирати API кључ. Када добијете кључ, унесите га у променљиву `OPENAI_API_KEY` у `.env` фајлу.

## Подешавање Hugging Face: Преко профила

Ваш Hugging Face токен можете пронаћи у свом профилу под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Немојте их јавно објављивати или делити. Уместо тога, креирајте нови токен за овај пројекат и копирајте га у `.env` фајл под променљивом `HUGGING_FACE_API_KEY`. _Напомена:_ Ово технички није API кључ, али се користи за аутентификацију, па задржавамо ту конвенцију именовања ради доследности.

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразума или погрешна тумачења настала употребом овог превода.