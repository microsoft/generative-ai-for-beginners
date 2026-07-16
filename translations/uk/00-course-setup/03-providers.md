# Вибір і конфігурація постачальника LLM 🔑

Завдання **можуть** також бути налаштовані для роботи з одним або декількома розгортаннями великих мовних моделей (LLM) через підтримуваного постачальника сервісів, такого як OpenAI, Azure або Hugging Face. Вони надають _хостингований кінцевий пункт_ (API), до якого ми можемо звертатися програмно з необхідними обліковими даними (ключем API або токеном). У цьому курсі ми розглядаємо таких постачальників:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) з різноманітними моделями, включаючи основну серію GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI з орієнтацією на підприємницькі потреби.
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) для єдиного кінцевого пункту та ключа API для доступу до сотень моделей від OpenAI, Meta, Mistral, Cohere, Microsoft та інших (замінює GitHub Models, які будуть припинені в кінці липня 2026 року).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для відкритих моделей та сервера висновку.
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) або [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), якщо ви хочете запускати моделі повністю офлайн на власному пристрої без підписки на хмару.

**Ви маєте використовувати власні облікові записи для цих вправ**. Вправи є необов’язковими, тож ви можете обрати налаштувати одного, усіх або жодного з постачальників за власним розсудом. Нижче наведено деякі рекомендації щодо реєстрації:

| Реєстрація | Вартість | Ключ API | Платформа | Коментарі |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ціни](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [За проєктом](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без коду, Веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно кілька моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ціни](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Швидкий старт SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Студія швидкого старту](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потрібна попередня реєстрація](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ціни](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Сторінка огляду проєкту](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Доступний безкоштовний рівень; один кінцевий пункт + ключ для багатьох постачальників моделей |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ціни](https://huggingface.co/pricing) | [Токени доступу](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat має обмежені моделі](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Безкоштовно (запускається на вашому пристрої) | Не потрібен | [Локальний CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Повністю офлайн, сумісний з OpenAI кінцевий пункт |
| | | | | |

Дотримуйтесь інструкцій нижче, щоб _налаштувати_ цей репозиторій для роботи з різними постачальниками. Завдання, що потребують певного постачальника, матимуть один із цих тегів у назві файлу:

- `aoai` - потребує кінцевий пункт і ключ Azure OpenAI
- `oai` - потребує кінцевий пункт і ключ OpenAI
- `hf` - потребує токен Hugging Face
- `githubmodels` - потребує кінцевий пункт і ключ Microsoft Foundry Models (GitHub Models буде припинено в кінці липня 2026)

Ви можете налаштувати одного, жодного або всіх постачальників. Завдання, які пов’язані з відсутніми обліковими даними, просто видадуть помилку.

## Створіть файл `.env`

Ми припускаємо, що ви вже ознайомилися з вище наведеними вказівками, зареєструвалися у відповідного постачальника і отримали потрібні облікові дані для автентифікації (API_KEY або токен). У випадку з Azure OpenAI, ми припускаємо, що у вас також є дійсне розгортання служби Azure OpenAI (кінцевий пункт) з наявною принаймні однією моделлю GPT для чат-завершення.

Наступний крок — налаштування ваших **локальних змінних середовища** наступним чином:

1. Знайдіть у кореневій папці файл `.env.copy`, що має приблизно такий вміст:

   ```bash
   # Постачальник OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI у Microsoft Foundry
   ## (Azure OpenAI Service тепер є частиною Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # За замовчуванням встановлено! (поточна стабільна версія GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Моделі Microsoft Foundry (каталог моделей з багатьма постачальниками, замінює GitHub Models, який припиняє підтримку наприкінці липня 2026 року)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Скопіюйте цей файл у `.env` за допомогою команди нижче. Цей файл _ігнорується в git_, щоб зберігати секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть заповнювачі праворуч від `=`) як описано в наступному розділі.

4. (Опційно) Якщо ви використовуєте GitHub Codespaces, у вас є можливість зберегти змінні середовища як _тайни Codespaces_, пов'язані з цим репозиторієм. У такому випадку вам не потрібно налаштовувати локальний файл .env. **Проте зверніть увагу, що ця опція працює лише, якщо ви використовуєте GitHub Codespaces.** Якщо ви використовуєте Docker Desktop, файл .env треба налаштувати.

## Заповнення файлу `.env`

Розглянемо коротко назви змінних і що вони означають:

| Змінна  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Це токен доступу користувача, який ви налаштували у своєму профілі |
| OPENAI_API_KEY | Це ключ авторизації для використання сервісу не через Azure OpenAI |
| AZURE_OPENAI_API_KEY | Це ключ авторизації для використання сервісу Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Це розгорнутий кінцевий пункт ресурсу Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Це кінцевий пункт розгортання моделі для _генерації тексту_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Це кінцевий пункт розгортання моделі для _векторних представлень тексту_ |
| AZURE_INFERENCE_ENDPOINT | Це кінцевий пункт для вашого проєкту Microsoft Foundry, використовується для Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Це ключ API для вашого проєкту Microsoft Foundry |
| | |

Примітка: Дві останні змінні Azure OpenAI відповідають моделі за замовчуванням для чат-завершення (генерації тексту) і векторного пошуку (вбудов) відповідно. Інструкції щодо їх налаштування будуть у відповідних завданнях.

## Налаштування Azure OpenAI: Через портал

> **Примітка:** Послуга Azure OpenAI тепер є частиною [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурси та розгортання все ще знаходяться в Azure Portal, але щоденне керування моделями (розгортання, майданчик, моніторинг) тепер відбувається через портал Foundry, а не через стару автономну "Azure OpenAI Studio".

Значення кінцевого пункту Azure OpenAI та ключа можна знайти в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), тож почнемо звідти.

1. Перейдіть до [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Натисніть опцію **Keys and Endpoint** у бічному меню (зліва).
1. Натисніть **Show Keys** - має з'явитися наступне: KEY 1, KEY 2 та Endpoint.
1. Використайте значення KEY 1 для AZURE_OPENAI_API_KEY
1. Використайте значення Endpoint для AZURE_OPENAI_ENDPOINT

Далі нам потрібні кінцеві точки для конкретних моделей, які ми розгорнули.

1. Натисніть опцію **Model deployments** у бічному меню (ліворуч) для ресурсу Azure OpenAI.
1. На сторінці призначення натисніть **Go to Microsoft Foundry portal** (або **Manage Deployments**, залежно від типу ресурсу).

Це приведе вас до порталу Microsoft Foundry, де ми знайдемо інші значення, описані нижче.

## Налаштування Azure OpenAI: Через портал Microsoft Foundry

1. Перейдіть до [порталу Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **з вашого ресурсу**, як описано вище.
1. Натисніть вкладку **Deployments** (бічне меню ліворуч), щоб переглянути поточні розгорнуті моделі.
1. Якщо бажаної моделі немає, використайте **Deploy model** для розгортання з [каталогу моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Вам потрібна модель _генерації тексту_ — радимо: **gpt-4o-mini**
1. Вам потрібна модель _векторних представлень тексту_ — радимо **text-embedding-3-small**

Тепер оновіть змінні середовища, щоб вони відображали _ім'я розгортання_ (Deployment name), яке використовувалося. Зазвичай це буде таке ж, як ім'я моделі, якщо ви явно його не змінювали. Наприклад, можна мати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забудьте зберегти файл .env після редагування**. Тепер можете закрити файл і повернутися до інструкцій щодо запуску блокноту.

## Налаштування OpenAI: З профілю

Ваш ключ API OpenAI можна знайти у вашому [обліковому записі OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Якщо у вас його немає, можете зареєструвати обліковий запис і створити ключ API. Після отримання ключа використайте його для заповнення змінної `OPENAI_API_KEY` у файлі `.env`.

## Налаштування Hugging Face: З профілю

Ваш токен Hugging Face можна знайти у вашому профілі на сторінці [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публікуйте та не діліться ним публічно. Краще створіть новий токен для використання в цьому проєкті і скопіюйте його у файл `.env` у змінну `HUGGING_FACE_API_KEY`. _Примітка:_ Технічно це не ключ API, але використовується для автентифікації, тому ми зберігаємо таку назву змінної для узгодженості.

## Налаштування Microsoft Foundry Models: Через портал

> **Примітка:** GitHub Models буде припинено в кінці липня 2026. Microsoft Foundry Models є прямою заміною, пропонуючи той самий каталог моделей з безкоштовним пробним доступом і досвід з Azure AI Inference SDK / OpenAI SDK.

1. Перейдіть до [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) і створіть (або відкрийте) проєкт Foundry.
1. Перегляньте [каталог моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) і розгорніть модель, наприклад `gpt-4o-mini`.
1. На сторінці **Overview** проєкту скопіюйте **endpoint** і **ключ API**.
1. Використайте значення endpoint для `AZURE_INFERENCE_ENDPOINT` та ключ API для `AZURE_INFERENCE_CREDENTIAL` у файлі `.env`.

## Офлайн / локальні постачальники

Якщо ви зовсім не хочете використовувати хмарну підписку, ви можете запускати сумісні відкриті моделі безпосередньо на власному пристрої:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - рантайм від Microsoft на пристрої. Він автоматично обирає найкращий виконавчий провайдер (NPU, GPU або CPU) і забезпечує сумісний з OpenAI кінцевий пункт, тому ви можете повторно використовувати більшість прикладів коду з цього курсу з мінімальними змінами. Див. [документацію Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) для початку, або встановіть через `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - популярна альтернатива для запуску відкритих моделей, таких як Llama, Phi, Mistral і Gemma локально.


Дивіться [Урок 19: Побудова за допомогою SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) для прикладів практичного застосування обох варіантів.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->