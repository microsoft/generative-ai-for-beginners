<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:20:10+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "bg"
}
-->
# Избор и конфигуриране на LLM доставчик 🔑

Задачите **могат** да бъдат настроени да работят с едно или повече разгръщания на големи езикови модели (LLM) чрез поддържан доставчик на услуги като OpenAI, Azure или Hugging Face. Те предоставят _хостван крайна точка_ (API), до която можем да имаме достъп програмно с правилните идентификационни данни (API ключ или токен). В този курс разглеждаме следните доставчици:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) с разнообразни модели, включително основната серия GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) за OpenAI модели с фокус върху корпоративна употреба
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) за отворен код модели и inference сървър

**Ще трябва да използвате собствени акаунти за тези упражнения**. Задачите са по избор, така че можете да изберете да настроите един, всички – или нито един – от доставчиците според вашите интереси. Ето някои насоки за регистрация:

| Регистрация | Цена | API ключ | Playground | Коментари |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ценообразуване](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [На база проект](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Налични са множество модели |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ценообразуване](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Трябва да кандидатствате предварително за достъп](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ценообразуване](https://huggingface.co/pricing) | [Достъп токени](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat има ограничени модели](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Следвайте инструкциите по-долу, за да _конфигурирате_ това хранилище за работа с различни доставчици. Задачите, които изискват конкретен доставчик, ще съдържат един от следните тагове в името на файла:

- `aoai` - изисква Azure OpenAI endpoint и ключ
- `oai` - изисква OpenAI endpoint и ключ
- `hf` - изисква Hugging Face токен

Можете да конфигурирате един, нито един или всички доставчици. Свързаните задачи просто ще дадат грешка при липсващи идентификационни данни.

## Създаване на `.env` файл

Приемаме, че вече сте прочели горните насоки, регистрирали сте се при съответния доставчик и сте получили необходимите идентификационни данни за удостоверяване (API_KEY или токен). В случая с Azure OpenAI, приемаме, че имате и валидно разгръщане на Azure OpenAI Service (endpoint) с поне един GPT модел, разположен за chat completion.

Следващата стъпка е да конфигурирате **локалните променливи на средата** по следния начин:

1. Потърсете в основната папка файл `.env.copy`, който трябва да съдържа нещо подобно:

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

2. Копирайте този файл като `.env` с командата по-долу. Този файл е _gitignore-нат_, за да пази тайните ви.

   ```bash
   cp .env.copy .env
   ```

3. Попълнете стойностите (заменете плейсхолдерите вдясно от `=`), както е описано в следващата секция.

4. (По избор) Ако използвате GitHub Codespaces, имате възможност да запазите променливите на средата като _Codespaces secrets_, свързани с това хранилище. В този случай няма да е нужно да настройвате локален .env файл. **Имайте предвид, че тази опция работи само ако използвате GitHub Codespaces.** Ако използвате Docker Desktop, все пак ще трябва да настроите .env файла.

## Попълване на `.env` файла

Нека разгледаме бързо имената на променливите, за да разберем какво означават:

| Променлива  | Описание  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Това е токенът за достъп, който сте създали в профила си |
| OPENAI_API_KEY | Това е ключът за оторизация за използване на услугата за не-Azure OpenAI endpoint-и |
| AZURE_OPENAI_API_KEY | Това е ключът за оторизация за използване на тази услуга |
| AZURE_OPENAI_ENDPOINT | Това е разположеният endpoint за Azure OpenAI ресурс |
| AZURE_OPENAI_DEPLOYMENT | Това е endpoint-ът за разгръщане на _текстово генериране_ модел |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Това е endpoint-ът за разгръщане на _текстови embedding-и_ модел |
| | |

Забележка: Последните две Azure OpenAI променливи отразяват модел по подразбиране за chat completion (генериране на текст) и търсене по вектори (embedding-и) съответно. Инструкции за настройката им ще бъдат дадени в съответните задачи.

## Конфигуриране на Azure: През портала

Стойностите за Azure OpenAI endpoint и ключ ще намерите в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), така че нека започнем оттам.

1. Отидете в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Кликнете на опцията **Keys and Endpoint** в страничното меню (отляво).
1. Кликнете **Show Keys** – трябва да видите: KEY 1, KEY 2 и Endpoint.
1. Използвайте стойността на KEY 1 за AZURE_OPENAI_API_KEY
1. Използвайте стойността на Endpoint за AZURE_OPENAI_ENDPOINT

След това ще ни трябват endpoint-ите за конкретните модели, които сме разположили.

1. Кликнете на опцията **Model deployments** в страничното меню (отляво) за Azure OpenAI ресурса.
1. На целевата страница кликнете **Manage Deployments**

Това ще ви отведе до уебсайта Azure OpenAI Studio, където ще намерим останалите стойности, както е описано по-долу.

## Конфигуриране на Azure: През Studio

1. Отидете в [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **от вашия ресурс**, както е описано по-горе.
1. Кликнете на таба **Deployments** (странично меню, вляво), за да видите текущо разположените модели.
1. Ако желаният от вас модел не е разположен, използвайте **Create new deployment**, за да го разположите.
1. Ще ви трябва _текстово-генериращ_ модел – препоръчваме: **gpt-35-turbo**
1. Ще ви трябва _текстов embedding_ модел – препоръчваме **text-embedding-ada-002**

Сега обновете променливите на средата, за да отразяват _Deployment name_, който сте използвали. Обикновено това ще е същото като името на модела, освен ако не сте го сменили изрично. Например, може да имате:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забравяйте да запазите .env файла, когато приключите**. Можете да затворите файла и да се върнете към инструкциите за стартиране на notebook-а.

## Конфигуриране на OpenAI: През профила

Вашият OpenAI API ключ може да бъде намерен във вашия [OpenAI акаунт](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ако нямате такъв, можете да си създадете акаунт и да генерирате API ключ. След като имате ключа, използвайте го, за да попълните променливата `OPENAI_API_KEY` във файла `.env`.

## Конфигуриране на Hugging Face: През профила

Вашият Hugging Face токен може да бъде намерен в профила ви под [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публикувайте и не споделяйте тези токени публично. Вместо това създайте нов токен за този проект и го копирайте във файла `.env` под променливата `HUGGING_FACE_API_KEY`. _Забележка:_ Това технически не е API ключ, но се използва за удостоверяване, затова запазваме тази конвенция за именуване за последователност.

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали от използването на този превод.