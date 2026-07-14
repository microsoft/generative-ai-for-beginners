# Избор и конфигурисање провајдера LLM 🔑

Задатке **може** такође бити подешено да раде кроз један или више развоја великих језичких модела (LLM) путем подржаног провајдера услуга као што су OpenAI, Azure или Hugging Face. Они пружају _хостовану тачку за приступ_ (API) којој можемо програмски приступити уз исправне акредитиве (API кључ или токен). У овом курсу, разматрамо ове провајдере:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) са разноврсним моделима укључујући основну серију GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI моделе са фокусом на спремност за предузећа
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) за једну тачку приступа и API кључ за приступ стотинама модела од OpenAI, Meta, Mistral, Cohere, Microsoft и других (замењује GitHub Models, који се гаси крајем јула 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за open-source модели и inference сервер
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ако бисте радије покрeнули моделе потпуно офлајн на свом уређају, без потребе за cloud претплатом

**За ове вежбе ће вам требати ваши налози**. Задате вежбе су опционе па можете одабрати да подесите једног, све - или ниједног - од провајдера у складу са својим интересовањем. Неке смернице за регистрацију:

| Регистрација | Цена | API кључ | Игралиште | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Цене](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Пројектно базирано](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без кода, веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Више доступних модела |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Цене](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK брзи почетак](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Студио брзи почетак](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Морате се пријавити унапред за приступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Цене](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница прегледа пројекта](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry игралиште](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Бесплатан слој доступан; једна тачка и кључ за многе провајдере модела |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Цене](https://huggingface.co/pricing) | [Токени за приступ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничене моделе](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Бесплатно (ради на вашем уређају) | Није потребно | [Локални CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Потпуно офлајн, OpenAI-компатибилна тачка |
| | | | | |

Пратите упутства испод да _конфигуришете_ овај репозиторијум за рад са различитим провајдерима. Задатци који захтевају одређеног провајдера имаће један од ових тагова у имену фајла:

- `aoai` - захтева Azure OpenAI тачку и кључ
- `oai` - захтева OpenAI тачку и кључ
- `hf` - захтева Hugging Face токен
- `githubmodels` - захтева Microsoft Foundry Models тачку и кључ (GitHub Models се гаси крајем јула 2026)

Можете подесити једног, ниједног или све провајдере. Повећани задаци једноставно ће се зауставити са грешком ако недостају акредитиви.

## Креирање `.env` фајла

Претпостављамо да сте већ прочитали горња упутства, регистровали се код релевантног провајдера и добили потребне акредитиве за аутентификацију (API_KEY или токен). У случају Azure OpenAI, претпостављамо да имате важећу имплементацију Azure OpenAI сервиса (endpoint) са минимум једним GPT моделом за chat completion.

Следећи корак је да подесите своје **локалне системске променљиве** на следећи начин:

1. Погледајте у корену фолдера фајл `.env.copy` који би требао да садржи овакве податке:

   ```bash
   # Провајдер OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI у Microsoft Foundry
   ## (Azure OpenAI услуга је сада део Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Подразумевано је подешено! (тренутна стабилна GA верзија API-ја)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry модели (мулти-провајдер каталог модела, замењује GitHub моделе, који ће престати са радом крајем јула 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копирајте тај фајл као `.env` користећи команду испод. Овај фајл је _gitignore-ован_, како би ваши тајни подаци били безбедни.

   ```bash
   cp .env.copy .env
   ```

3. Испуните вредности (замените плејсхолдере десно од `=`) како је описано у следећем делу.

4. (Опционо) Ако користите GitHub Codespaces, имате опцију да сачувате променљиве окружења као _Codespaces тајне_ повезане са овим репозиторијумом. У том случају, неће бити потребно да локално подешавате .env фајл. **Међутим, имајте у виду да ова опција ради само ако користите GitHub Codespaces.** И даље ћете морати да подесите .env фајл уколико користите Docker Desktop.

## Попуњавање `.env` фајла

Хајде да брзо погледамо имена променљивих да бисмо разумели шта представљају:

| Променљива  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ово је кориснички токен за приступ који сте подесили у свом профилу |
| OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење сервиса ван Azure OpenAI тачака |
| AZURE_OPENAI_API_KEY | Ово је кључ за ауторизацију за коришћење тог сервиса |
| AZURE_OPENAI_ENDPOINT | Ово је развијена тачка приступа Azure OpenAI ресурсу |
| AZURE_OPENAI_DEPLOYMENT | Ово је тачка развоја модела за _текстуалну генерацију_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ово је тачка развоја модела за _векторске уградње_ текста |
| AZURE_INFERENCE_ENDPOINT | Ово је тачка приступа за ваш Microsoft Foundry пројекат, коришћена за Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Ово је API кључ за ваш Microsoft Foundry пројекат |
| | |

Напомена: Последње две Azure OpenAI променљиве одражавају подразумевани модел за завршетак ћаскања (генерацију текста) и претрагу вектора (уградње) редоследно. Упутства за њихову конфигурацију ће бити дата у релевантним задацима.

## Конфигурисање Azure OpenAI: Са портала

> **Напомена:** Azure OpenAI Service је сада део [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурси и развоји се и даље виде у Azure порталу, али свакодневно управљање моделима (развој, игралиште, надзор) сада се обавља у Foundry порталу уместо у старом самосталном "Azure OpenAI Studio".

Вредности Azure OpenAI тачке и кључа пронаћи ћете у [Azure порталу](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) па хајде да тамо почнемо.

1. Отворите [Azure портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликните на опцију **Keys and Endpoint** у бочној траци (садржај са леве стране).
1. Кликните **Прикажи кључеве** - требало би да видите следеће: KEY 1, KEY 2 и Endpoint.
1. Користите вредност KEY 1 за AZURE_OPENAI_API_KEY
1. Користите вредност Endpoint за AZURE_OPENAI_ENDPOINT

Следеће, потребне су нам тачке приступа за специфичне моделе које смо развили.

1. Кликните на опцију **Model deployments** у бочној траци (леви мени) за Azure OpenAI ресурс.
1. У одредишној страници кликните **Иди на Microsoft Foundry портал** (или **Manage Deployments**, зависно од врсте вашег ресурса)

Ово ће вас одвести на Microsoft Foundry портал, где ћемо пронаћи друге вредности како је описано доле.

## Конфигурисање Azure OpenAI: Са Microsoft Foundry портала

1. Идите на [Microsoft Foundry портал](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **са свог ресурса** као што је описано горе.
1. Кликните на таб **Deployments** (бочни мени, лево) да бисте видели тренутно развијене моделе.
1. Ако жељени модел није развијен, користите **Deploy model** да га развијете из [каталога модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Потребан вам је _текст-генерациони_ модел - препоручујемо: **gpt-4o-mini**
1. Потребан вам је _текст-уградни_ модел - препоручујемо **text-embedding-3-small**

Сада ажурирајте променљиве окружења да одражавају име _Deployment_-а који се користи. Ово ће обично бити исто као име модела осим ако сте га експлицитно променили. На пример, можете имати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не заборавите да сачувате .env фајл када завршите**. Сада можете затворити фајл и вратити се упутствима за покретање нотебоок-а.

## Конфигурисање OpenAI: Са профила

Ваш OpenAI API кључ можете пронаћи у вашем [OpenAI налогу](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако га немате, можете се регистровати и креирати API кључ. Када добијете кључ, можете га користити за попуњавање променљиве `OPENAI_API_KEY` у `.env` фајлу.

## Конфигурисање Hugging Face: Са профила

Ваш Hugging Face токен можете пронаћи у свом профилу под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Немојте их објављивати или делити јавности. Уместо тога, креирајте нови токен за ову употребу пројекта и копирајте га у `.env` фајл под променљивом `HUGGING_FACE_API_KEY`. _Напомена:_ Технички ово није API кључ, али се користи за аутентификацију па задржавамо ту конвенцију именовања ради конзистенције.

## Конфигурисање Microsoft Foundry Models: Са портала

> **Напомена:** GitHub Models се гаси крајем јула 2026. Microsoft Foundry Models је директна замена, нудећи исти бесплатни каталог модела за пробу и Azure AI Inference SDK / OpenAI SDK искуство.

1. Идите на [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и направите (или отворите) Foundry пројекат.
1. Прегледајте [каталог модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и развијте модел, на пример `gpt-4o-mini`.
1. На страници **Преглед пројекта**, копирајте **endpoint** и **API key**.
1. Користите вредност endpoint за `AZURE_INFERENCE_ENDPOINT` и кључ за `AZURE_INFERENCE_CREDENTIAL` у вашем `.env` фајлу.

## Офлајн / Локални провајдери

Ако не желите уопште користити cloud претплату, можете покретати компатибилне отворене моделе директно на свом уређају:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft-ова извршна околина на уређају. Аутоматски бира најбољег провајдера извршења (NPU, GPU или CPU) и омогућава OpenAI-компатибилну тачку приступа, тако да можете поново користити већину примерног кода из овог курса са минималним изменама. Погледајте [Foundry Local документацију](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) да започнете, или инсталирајте командом `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популарна алтернатива за локално покретање отворених модела као што су Llama, Phi, Mistral и Gemma.


Погледајте [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) за практичне примере коришћења обе опције.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->