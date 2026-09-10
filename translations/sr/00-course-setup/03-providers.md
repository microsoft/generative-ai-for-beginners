# Избор и конфигурисање провајдера LLM 🔑

Задатке је **могуће** подесити да раде са једним или више развоја великог језичког модела (LLM) путем подржаног сервисног провајдера као што су OpenAI, Azure или Hugging Face. Они пружају _хостирану тачку приступа_ (API) коју можемо програмски користити са исправним акредитивима (API кључ или токен). У овом курсу дискутујемо о овим провајдерима:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) са разноврсним моделима укључујући и основну серију GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI моделе са фокусом на спремност за ентерпрајс
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) за једну тачку приступа и API кључ за приступ стотинама модела од OpenAI, Meta, Mistral, Cohere, Microsoft и више (замењује GitHub Models, који се повлачи крајем јула 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за опен-соурце моделе и inference сервер
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ако више волите да покрећете моделе потпуно офлајн на свом уређају, без претплате на облак

**За ове вежбе ћете морати да користите своје налоге**. Задатци су опциони па можете одабрати да подесите једног, све или ниједног провајдера у складу са својим интересовањима. Нека упутства за регистрацију:

| Регистрација | Цена | API кључ | Плаyграунд | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цене](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Пројектно базирано](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Но-Код, Веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно више модела |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цене](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK брзи почетак](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio брзи почетак](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Морате се пријавити унапред за приступ](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Цене](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница прегледа пројекта](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry плаyграунд](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Бесплатни слој доступан; једна тачка приступа + кључ за више провајдера модела |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цене](https://huggingface.co/pricing) | [Токени приступа](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничене моделе](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Бесплатно (ради на вашем уређају) | Није потребно | [Локални CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Потпуно офлајн, OpenAI-компатибилна тачка приступа |
| | | | | |

Пратите упутства у наставку да бисте _конфигурисали_ овај репозиторijум за употребу са различитим провајдерима. Задатци који захтевају одређеног провајдера ће у свом имену фајла садржати један од ових ознака:

- `aoai` - захтева Azure OpenAI крајњу тачку и кључ
- `oai` - захтева OpenAI крајњу тачку и кључ
- `hf` - захтева Hugging Face токен
- `githubmodels` - захтева Microsoft Foundry Models крајњу тачку и кључ (GitHub Models се повлачи крајем јула 2026)

Можете конфигурисати једног, ниједног или све провајдере. Повећани задаци једноставно ће пријавити грешку ако акредитиви недостају.

## Креирање `.env` фајла

Претпостављамо да сте већ прочитали горња упутства, регистровали се код релевантног провајдера и добили потребне аутентификационе акредитиве (API_KEY или токен). У случају Azure OpenAI, претпостављамо да такође имате валидну инсталацију Azure OpenAI услуге (endpoint) са најмање једним GPT моделом подешеним за чат комплетирање.

Следећи корак је да конфигуришете своје **локалне променљиве окружења** како следи:

1. Потражите у коренском фолдеру `.env.copy` фајл који би требао да има садржај као овај:

   ```bash
   # Provajder OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI u Microsoft Foundry
   ## (Azure OpenAI servis je сада део Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Подразумевано је подешено! (тренутна стабилна GA API верзија)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry модели (каталог модела са више провајдера, замењује GitHub моделe, који се повлачи крајем јула 2026.)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копирајте тај фајл на `.env` користећи команду испод. Овај фајл је _gitignore-д_, што чува тајне безбедним.

   ```bash
   cp .env.copy .env
   ```

3. Попуните вредности (замените плейсхолдере са десне стране знака `=`) како је описано у следећем одељку.

4. (Опционо) Ако користите GitHub Codespaces, постоји могућност да сачувате променљиве окружења као _Codespaces секрети_ повезани са овим репозиторijумом. У том случају нећете морати да подешавате локални .env фајл. **Међутим, имајте на уму да ова опција ради само ако користите GitHub Codespaces.** И даље ћете морати да подесите .env фајл ако користите Docker Desktop.

## Попуњавање `.env` фајла

Хајде да брзо погледамо називе променљивих да бисмо разумели шта представљају:

| Променљива  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ово је кориснички токен приступа који сте подесили у профилу |
| OPENAI_API_KEY | Ово је кључ за ауторизацију коришћења сервиса за не-Azure OpenAI крајње тачке |
| AZURE_OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење тог сервиса |
| AZURE_OPENAI_ENDPOINT | Ово је дистрибуирана крајња тачка за Azure OpenAI ресурс |
| AZURE_OPENAI_DEPLOYMENT | Ово је крајња тачка за развој модела _генерисања текста_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ово је крајња тачка за развој модела _уградње текста_ |
| AZURE_INFERENCE_ENDPOINT | Ово је крајња тачка за ваш Microsoft Foundry пројекат, користи се за Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ово је API кључ за ваш Microsoft Foundry пројекат |
| | |

Напомена: Последње две променљиве Azure OpenAI се односе на подразумевани модел за комплетирање чата (генерисање текста) и претрагу вектора (уградње) редом. Упутства за њихово подешавање биће наведена у релевантним задацима.

## Конфигурисање Azure OpenAI: са портала

> **Напомена:** Azure OpenAI услуга је сада део [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурси и развоји и даље се виде у Azure порталу, али свакодневно управљање моделима (развоји, плаyграунд, надзор) сада се обавља у Foundry порталу уместо у старом самосталном "Azure OpenAI Studio".

Вредности за Azure OpenAI крајњу тачку и кључ биће пронађене у [Azure порталу](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), па да почнемо тамо.

1. Идите на [Azure портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликните опцију **Keys and Endpoint** у бочној траци (мену са леве стране).
1. Кликните **Show Keys** - требало би да видите следеће: KEY 1, KEY 2 и Endpoint.
1. Користите вредност KEY 1 за AZURE_OPENAI_API_KEY
1. Користите вредност Endpoint за AZURE_OPENAI_ENDPOINT

Затим нам требају крајње тачке за специфичне моделе које смо развили.

1. Кликните опцију **Model deployments** у бочној траци (леви мени) за Azure OpenAI ресурс.
1. На одредишној страници кликните **Go to Microsoft Foundry portal** (или **Manage Deployments**, у зависности од типа вашег ресурса)

Ово ће вас одвести у Microsoft Foundry портал, где ћемо пронаћи остале вредности како је описано у наставку.

## Конфигурисање Azure OpenAI: са Microsoft Foundry портала

1. Поново идите на [Microsoft Foundry портал](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **са свог ресурса** како је описано горе.
1. Кликните на таб **Deployments** (бочна трака, лево) да прегледате тренутно постављене моделе.
1. Ако ваш жељени модел није постављен, користите **Deploy model** да га поставите из [каталога модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Требаће вам модел _генерисања текста_ - препоручујемо: **gpt-5-mini**
1. Требаће вам модел _уградње текста_ - препоручујемо **text-embedding-3-small**

Сада ажурирајте променљиве окружења да одражавају име _Deployment_-а који користите. Обично ће бити исто као име модела, осим ако га нисте експлицитно променили. На пример, можете имати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не заборавите да сачувате .env фајл када завршите**. Сада можете изаћи из фајла и вратити се инструкцијама за покретање бележнице.

## Конфигурисање OpenAI: из профила

Ваш OpenAI API кључ можете пронаћи у свом [OpenAI налогу](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако га немате, можете се регистровати и креирати API кључ. Када добијете кључ, употребите га да попуните променљиву `OPENAI_API_KEY` у `.env` фајлу.

## Конфигурисање Hugging Face: из профила

Ваш Hugging Face токен можете пронаћи у свом профилу под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Немојте их објављивати или делити јавно. Уместо тога, креирајте нови токен за ову употребу пројекта и копирајте га у `.env` фајл под променљиву `HUGGING_FACE_API_KEY`. _Напомена:_ Ово технолошки није API кључ, али се користи за аутентификацију па задржавамо ову конвенцију именовања ради доследности.

## Конфигурисање Microsoft Foundry Models: са портала

> **Напомена:** GitHub Models се повлачи крајем јула 2026. Microsoft Foundry Models је директна замена, нудећи исти каталог модела бесплатан за пробу и Azure AI Inference SDK / OpenAI SDK искуство.

1. Идите на [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и креирајте (или отворите) Foundry пројекат.
1. Прегледајте [каталог модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и поставите модел, на пример `gpt-5-mini`.
1. На пројектној страници **Overview**, копирајте **endpoint** и **API кључ**.
1. Користите вредност endpoint за `AZURE_INFERENCE_ENDPOINT` и вредност кључа за `AZURE_INFERENCE_CREDENTIAL` у вашем `.env` фајлу.

## Офлајн / локални провајдери

Ако више волите да уопште не користите претплату на облак, можете покренути компатибилне опен моделе директно на свом уређају:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft-ов рунтајм на уређају. Аутоматски бира најбољег извршног провајдера (NPU, GPU или CPU) и пружа OpenAI-компатибилну крајњу тачку, тако да можете поново користити већину примерног кода из овог курса уз минималне измене. Погледајте [Foundry Local документацију](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) за почетак, или инсталирајте са `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популарна алтернатива за локално покретање опен модела као што су Llama, Phi, Mistral и Gemma.


Погледајте [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) за практичне примере коришћења обе опције.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->