# Избор и конфигуриране на доставчик на LLM 🔑

Задачите **могат** също да бъдат настроени да работят с една или повече инсталации на Голям езиков модел (LLM) чрез поддържан доставчик на услуги като OpenAI, Azure или Hugging Face. Те предоставят _хостван крайна точка_ (API), до която можем да имаме програматичен достъп с правилните идентификационни данни (API ключ или токен). В този курс обсъждаме следните доставчици:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразни модели, включително основната серия GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI модели с фокус върху готовността за предприятия
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) за една крайна точка и API ключ за достъп до стотици модели от OpenAI, Meta, Mistral, Cohere, Microsoft и други (замества GitHub Models, който ще бъде прекратен в края на юли 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за отворени модели и сървър за извод
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) или [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ако предпочитате да стартирате модели изцяло офлайн на собственото си устройство, без необходимост от облачен абонамент

**Ще трябва да използвате собствени акаунти за тези упражнения**. Задачите са по избор, така че можете да изберете да настроите един, всички или нито един от доставчиците според своите интереси. Ето някои насоки за регистрация:

| Регистрация | Цена | API ключ | Пясъчник | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ценообразуване](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Базирано на проекти](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без код, уеб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Налични множество модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ценообразуване](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Бърз старт](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Бърз старт](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Трябва да кандидатствате предварително за достъп](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ценообразуване](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Страница с преглед на проекта](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Пясъчник](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Наличен безплатен ниво; една крайна точка + ключ за много доставчици на модели |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ценообразуване](https://huggingface.co/pricing) | [Токени за достъп](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничени модели](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Безплатно (работи на Вашето устройство) | Не е необходим | [Локален CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Изцяло офлайн, съвместим с OpenAI крайна точка |
| | | | | |

Следвайте посочените по-долу инструкции, за да _настроите_ това хранилище за използване с различните доставчици. Задачите, които изискват конкретен доставчик, ще съдържат един от тези тагове в името на файла си:

- `aoai` - изисква крайна точка и ключ за Azure OpenAI
- `oai` - изисква крайна точка и ключ за OpenAI
- `hf` - изисква токен от Hugging Face
- `githubmodels` - изисква крайна точка и ключ за Microsoft Foundry Models (GitHub Models ще бъде прекратен в края на юли 2026)

Можете да настроите един, никакъв или всички доставчици. Свързаните задачи просто ще дадат грешка при липса на идентификационни данни.

## Създаване на файл `.env`

Предполагаме, че вече сте прочели горните насоки и сте се регистрирали при релевантния доставчик, и сте получили необходимите удостоверителни данни (API_KEY или токен). В случай на Azure OpenAI, предполагаме, че също така имате валидно разгръщане на услуга Azure OpenAI (крайна точка) с поне един GPT модел, разположен за чат завършване.

Следващата стъпка е да настроите **локалните променливи на средата** както следва:

1. Потърсете във кореновата папка файл `.env.copy`, който трябва да има съдържание като това:

   ```bash
   # OpenAI доставчик
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI в Microsoft Foundry
   ## (Azure OpenAI услугата вече е част от Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # По подразбиране е зададено! (текуща стабилна GA API версия)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Модели на Microsoft Foundry (многодоставъчен каталог с модели, заменя GitHub моделите, които се прекратяват в края на юли 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копирайте този файл в `.env` с командата по-долу. Този файл е _gitignore-нат_, за да се пазят тайните.

   ```bash
   cp .env.copy .env
   ```

3. Попълнете стойностите (заменете плейсхолдерите вдясно от `=`) както е описано в следващия раздел.

4. (Опция) Ако използвате GitHub Codespaces, имате възможност да запазите променливите на средата като _Codespaces secrets_, свързани с това хранилище. В този случай няма да е нужно да настройвате локален .env файл. **Въпреки това, отбележете, че тази опция работи само ако използвате GitHub Codespaces.** Все още ще трябва да настроите .env файла, ако използвате Docker Desktop.

## Попълнете файла `.env`

Нека да разгледаме накратко имената на променливите, за да разберем какво представляват:

| Променлива  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Това е потребителският токен за достъп, който сте настроили в своя профил |
| OPENAI_API_KEY | Това е ключът за упълномощаване за използване на услугата за не-Azure OpenAI крайни точки |
| AZURE_OPENAI_API_KEY | Това е ключът за упълномощаване за използване на тази услуга |
| AZURE_OPENAI_ENDPOINT | Това е разположената крайна точка за ресурс на Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Това е крайната точка на разположения модел за _генериране на текст_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Това е крайната точка на разположения модел за _векторни вграждания_ |
| AZURE_INFERENCE_ENDPOINT | Това е крайната точка за Вашия Microsoft Foundry проект, използвана за Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Това е API ключът за Вашия Microsoft Foundry проект |
| | |

Забележка: Последните две променливи за Azure OpenAI отразяват подразбиращ се модел за чат завършване (генериране на текст) и векторно търсене (вграждания) съответно. Инструкциите за тяхното задаване ще бъдат определени в релевантни задачи.

## Конфигуриране на Azure OpenAI: От портал

> **Забележка:** Услугата Azure OpenAI вече е част от [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурсите и разгръщанията все още се виждат в Azure портала, но ежедневното управление на модели (разгръщания, пясъчник, мониторинг) вече се извършва в портала на Foundry вместо в остарялото самостоятелно приложение "Azure OpenAI Studio".

Стойностите на крайна точка и ключ за Azure OpenAI ще бъдат намерени в [Azure портала](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), така че нека започнем от там.

1. Отидете на [Azure портал](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликнете върху опцията **Keys and Endpoint** в страничното меню (меню вляво).
1. Кликнете върху **Show Keys** - трябва да видите следното: KEY 1, KEY 2 и Endpoint.
1. Използвайте стойността на KEY 1 за AZURE_OPENAI_API_KEY
1. Използвайте стойността на Endpoint за AZURE_OPENAI_ENDPOINT

След това ни трябват крайните точки за конкретните модели, които сме разположили.

1. Кликнете върху опцията **Model deployments** в страничното меню (вляво) за ресурс Azure OpenAI.
1. В страницата за дестинация кликнете върху **Go to Microsoft Foundry portal** (или **Manage Deployments**, в зависимост от типа на Вашия ресурс)

Това ще Ви отведе в портала Microsoft Foundry, където ще намерим останалите стойности, както е описано по-долу.

## Конфигуриране на Azure OpenAI: От портал Microsoft Foundry

1. Навигирайте до [портала Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **от Вашия ресурс**, както е описано по-горе.
1. Кликнете върху таба **Deployments** (странична лента, вляво), за да видите текущо разположените модели.
1. Ако желаният модел не е разположен, използвайте **Deploy model**, за да го разположите от [каталога с модели](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Ще Ви трябва модел за _генериране на текст_ – препоръчваме: **gpt-5-mini**
1. Ще Ви трябва модел за _вграждане на текст_ – препоръчваме **text-embedding-3-small**

Сега актуализирайте променливите на средата, за да отразяват използваното _Име на разполагането_. Това обикновено ще бъде същото като името на модела, освен ако не сте го променили изрично. Като пример, може да имате:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забравяйте да запазите .env файла, след като приключите**. Сега можете да излезете от файла и да се върнете към инструкциите за стартиране на тетрадката.

## Конфигуриране на OpenAI: От профила

Вашият OpenAI API ключ може да бъде намерен във Вашия [OpenAI акаунт](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако нямате такъв, можете да се регистрирате и да създадете API ключ. След като имате ключа, можете да го използвате, за да попълните променливата `OPENAI_API_KEY` във файла `.env`.

## Конфигуриране на Hugging Face: От профила

Вашият Hugging Face токен може да бъде намерен във Вашия профил под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикувайте или споделяйте тези публично. Вместо това, създайте нов токен за това проектно използване и го копирайте във файла `.env` под променливата `HUGGING_FACE_API_KEY`. _Забележка:_ Това технически не е API ключ, но се използва за удостоверяване, затова запазваме това именуване за консистентност.

## Конфигуриране на Microsoft Foundry Models: От портал

> **Забележка:** GitHub Models ще бъде прекратен в края на юли 2026. Microsoft Foundry Models е директната замяна, осигуряваща същия каталог с безплатни за проба модели и опит с Azure AI Inference SDK / OpenAI SDK.

1. Отидете в [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) и създайте (или отворете) проект в Foundry.
1. Разгледайте [каталога с модели](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) и разположете модел, например `gpt-5-mini`.
1. В страницата с **Обзор** на проекта копирайте **крайната точка** и **API ключа**.
1. Използвайте стойността на крайната точка за `AZURE_INFERENCE_ENDPOINT` и стойността на ключа за `AZURE_INFERENCE_CREDENTIAL` във Вашия `.env` файл.

## Офлайн / Локални доставчици

Ако предпочитате изобщо да не използвате облачен абонамент, можете да стартирате съвместими отворени модели директно на Вашето собствено устройство:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - изпълнителна среда на Microsoft за локално устройство. Автоматично избира най-добрия изпълнител (NPU, GPU или CPU) и осигурява крайна точка съвместима с OpenAI, така че можете да използвате по-голямата част от примерния код в този курс с минимални промени. Вижте [документацията на Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) за да започнете, или инсталирайте с `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популярен алтернативен вариант за стартиране на отворени модели като Llama, Phi, Mistral и Gemma локално.


Вижте [Урок 19: Създаване с SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) за практически примери с използване на двата варианта.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->