# Избор и конфигуриране на доставчик на LLM 🔑

Задачите **могат** също да се настроят да работят с един или повече разгръщания на големи езикови модели (LLM) чрез поддържан доставчик на услуги като OpenAI, Azure или Hugging Face. Те предоставят _хостван краен пункт_ (API), към който можем да имаме програматичен достъп с правилните идентификационни данни (API ключ или токен). В този курс разглеждаме тези доставчици:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразни модели, включително основната серия GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI модели с фокус върху готовността за предприятия
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) за един краен пункт и API ключ за достъп до стотици модели от OpenAI, Meta, Mistral, Cohere, Microsoft и други (замества GitHub Models, който се закрива в края на юли 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за отворени модели и сървър за инференция
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ако предпочитате да пускате модели напълно офлайн на собственото си устройство, без нужда от абонамент в облака

**Трябва да използвате собствени акаунти за тези упражнения**. Задачите са по избор, така че можете да изберете да настроите един, всички или никой от доставчиците според интересите си. Някои насоки за регистрация:

| Регистрация | Цена | API ключ | Игрална среда | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ценоразпис](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Проектно базиран](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без код, уеб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Налични множество модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ценоразпис](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Стартиране с SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Стартиране със Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Необходими са предварителни заявки за достъп](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ценоразпис](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница с преглед на проекта](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry игрална среда](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Наличен безплатен слой; един краен пункт + ключ за много доставчици на модели |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ценоразпис](https://huggingface.co/pricing) | [Достъпни токени](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничени модели](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Безплатно (работи на вашето устройство) | Не е необходим | [Локален CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Напълно офлайн, съвместим с OpenAI краен пункт |
| | | | | |

Следвайте инструкциите по-долу, за да _конфигурирате_ това хранилище за използване с различни доставчици. Задачите, които изискват конкретен доставчик, ще съдържат някой от тези тагове в името на файла:

- `aoai` - изисква Azure OpenAI краен пункт, ключ
- `oai` - изисква OpenAI краен пункт, ключ
- `hf` - изисква Hugging Face токен
- `githubmodels` - изисква Microsoft Foundry Models краен пункт, ключ (GitHub Models се закрива в края на юли 2026)

Можете да конфигурирате един, никой или всички доставчици. Свързаните задачи просто ще дадат грешка при липсващи идентификационни данни.

## Създаване на `.env` файл

Предполагаме, че вече сте прочели насоките по-горе и сте се регистрирали при съответния доставчик, като сте получили необходимите удостоверителни данни (API_KEY или токен). В случая с Azure OpenAI, предполагаме, че имате и валидно разгръщане на Azure OpenAI Service (краен пункт) с поне един GPT модел разположен за чат завършване.

Следващата стъпка е да конфигурирате вашите **локални променливи на средата** по следния начин:

1. Потърсете в главната папка файл `.env.copy`, който трябва да съдържа следното:

   ```bash
   # Доставчик OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI в Microsoft Foundry
   ## (Azure OpenAI Service вече е част от Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # По подразбиране е зададено! (текуща стабилна GA версия на API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Модели на Microsoft Foundry (каталог с модели от множество доставчици, замества GitHub Models, които се пенсионират в края на юли 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копирайте този файл до `.env` с командата по-долу. Този файл е _gitignore-нат_, за да пази тайните в безопасност.

   ```bash
   cp .env.copy .env
   ```

3. Попълнете стойностите (заменете плейсхолдерите вдясно от `=`) както е описано в следващия раздел.

4. (Опция) Ако използвате GitHub Codespaces, имате възможност да запазите променливите на средата като _тайни на Codespaces_, свързани с това хранилище. В такъв случай няма да е необходимо да настройвате локален .env файл. **Въпреки това, имайте предвид, че тази опция работи само ако използвате GitHub Codespaces.** Все пак ще трябва да настроите .env файла, ако използвате Docker Desktop.

## Попълване на `.env` файл

Нека разгледаме бързо имената на променливите, за да разберем какво представляват:

| Променлива  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Това е потребителският достъп токен, който сте настроили в профила си |
| OPENAI_API_KEY | Това е ключът за авторизация за използване на услугата за OpenAI крайни точки, различни от Azure |
| AZURE_OPENAI_API_KEY | Това е ключът за авторизация за използване на тази услуга |
| AZURE_OPENAI_ENDPOINT | Това е разположеният краен пункт за ресурс Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Това е крайният пункт на разгръщането на _тексто-генериращ_ модел |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Това е крайният пункт на разгръщането на _текстовите вграждания_ модел |
| AZURE_INFERENCE_ENDPOINT | Това е крайният пункт за вашия Microsoft Foundry проект, използван за Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Това е API ключът за вашия Microsoft Foundry проект |
| | |

Забележка: Последните две променливи на Azure OpenAI отразяват подразбиращ се модел за чат завършване (текстова генерация) и векторно търсене (вграждания) съответно. Инструкциите за тяхното задаване ще бъдат описани в съответните задачи.

## Конфигуриране на Azure OpenAI: От портала

> **Забележка:** Azure OpenAI Service вече е част от [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурсите и разгръщанията все още се показват в Azure портала, но ежедневното управление на модели (разгръщания, игрова среда, мониторинг) вече се извършва в портала Foundry вместо в старото самостоятелно "Azure OpenAI Studio".

Стойностите за краен пункт и ключ на Azure OpenAI ще се намират в [Azure портала](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), затова нека започнем от там.

1. Отидете в [Azure портала](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликнете върху опцията **Keys and Endpoint** в страничната лента (меню вляво).
1. Кликнете върху **Show Keys** - трябва да видите следното: KEY 1, KEY 2 и Endpoint.
1. Използвайте стойността на KEY 1 за AZURE_OPENAI_API_KEY
1. Използвайте стойността на Endpoint за AZURE_OPENAI_ENDPOINT

След това ни трябват крайните точки за конкретните модели, които сме разположили.

1. Кликнете върху опцията **Model deployments** в страничната лента (ляво меню) за ресурса Azure OpenAI.
1. На целевата страница кликнете върху **Go to Microsoft Foundry portal** (или **Manage Deployments**, в зависимост от типа на вашия ресурс)

Това ще ви отведе до портала Microsoft Foundry, където ще намерим останалите стойности както е описано по-долу.

## Конфигуриране на Azure OpenAI: От портала Microsoft Foundry

1. Навигирайте към [Microsoft Foundry портала](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **от вашия ресурс**, както е описано по-горе.
1. Кликнете върху таба **Deployments** (странична лента, вляво), за да видите текущо разположените модели.
1. Ако желаният от вас модел не е разположен, използвайте **Deploy model**, за да го разположите от [каталога с модели](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Ще ви трябва _тексто-генериращ_ модел - препоръчваме: **gpt-4o-mini**
1. Ще ви трябва _тексто-вграждащ_ модел - препоръчваме **text-embedding-3-small**

Сега актуализирайте променливите на средата, за да отразяват името на _Deployment_, което се използва. Това обикновено е същото като името на модела, освен ако не сте го променили изрично. Така че, като пример, може да имате:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забравяйте да запазите .env файла, когато приключите**. Сега можете да излезете от файла и да се върнете към инструкциите за изпълнение на тетрадката.

## Конфигуриране на OpenAI: От профила

Вашият OpenAI API ключ може да се намери във вашия [OpenAI акаунт](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако нямате такъв, можете да се регистрирате за акаунт и да създадете API ключ. След като получите ключа, можете да го използвате, за да попълните променливата `OPENAI_API_KEY` във файла `.env`.

## Конфигуриране на Hugging Face: От профила

Вашият Hugging Face токен може да се намери в профила ви под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикувайте и не споделяйте тези публично. Вместо това създайте нов токен за употреба в този проект и го копирайте във файла `.env` под променливата `HUGGING_FACE_API_KEY`. _Забележка:_ Това технически не е API ключ, но се използва за удостоверяване, така че запазваме това именуване за последователност.

## Конфигуриране на Microsoft Foundry Models: От портала

> **Забележка:** GitHub Models се закрива в края на юли 2026. Microsoft Foundry Models е директната замяна, предлагаща същия каталог с безплатни за проба модели и Azure AI Inference SDK / OpenAI SDK опит.

1. Отидете в [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и създайте (или отворете) Foundry проект.
1. Разгледайте [каталога с модели](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и разположете модел, например `gpt-4o-mini`.
1. На **Overview** страницата на проекта копирайте **крайна точка** и **API ключ**.
1. Използвайте стойността на крайния пункт за `AZURE_INFERENCE_ENDPOINT` и ключа за `AZURE_INFERENCE_CREDENTIAL` във файла `.env`.

## Офлайн / Локални доставчици

Ако предпочитате да не използвате облачен абонамент, можете да пускате съвместими отворени модели директно на собственото си устройство:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - он-устройство изпълнителна среда на Microsoft. Тя автоматично избира най-добрия изпълнител (NPU, GPU или CPU) и предоставя OpenAI-съвместима крайна точка, така че можете да използвате повечето от примерния код в този курс с минимални промени. Вижте [документацията на Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), за да започнете, или инсталирайте с `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популярна алтернатива за пускане на отворени модели като Llama, Phi, Mistral и Gemma локално.


Вижте [Урок 19: Създаване с SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) за практически примери с използване и на двата варианта.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->