# Вибір і налаштування постачальника LLM 🔑

Завдання **можуть** також бути налаштовані для роботи з одним або кількома розгортаннями великих мовних моделей (LLM) через підтримуваного сервісного провайдера, такого як OpenAI, Azure або Hugging Face. Вони надають _хостингову кінцеву точку_ (API), до якої ми можемо програмно звертатися за наявності відповідних облікових даних (API-ключ чи токен). У цьому курсі ми обговорюємо цих провайдерів:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) з різноманітними моделями, включаючи основну серію GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI з орієнтацією на готовність до підприємств
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) для однієї кінцевої точки та API-ключа для доступу до сотень моделей від OpenAI, Meta, Mistral, Cohere, Microsoft і інших (замінює GitHub Models, які припиняють роботу наприкінці липня 2026 року)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для відкритих моделей та сервера висновків
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) або [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), якщо ви хочете запускати моделі повністю офлайн на власному пристрої без необхідності підписки на хмару

**Для цих вправ вам знадобляться власні акаунти**. Завдання є необов’язковими, тож ви можете вибрати налаштування одного, усіх або жодного з провайдерів відповідно до ваших інтересів. Ось деякі підказки щодо реєстрації:

| Реєстрація | Вартість | API-ключ | Пісочниця | Коментарі |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ціноутворення](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Проєктні ключі](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без коду, Веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно кілька моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ціноутворення](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Швидкий початок SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Швидкий початок Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потрібна попередня заявка для доступу](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Ціноутворення](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Сторінка огляду проєкту](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Пісочниця Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Безкоштовний рівень; одна кінцева точка + ключ для багатьох провайдерів моделей |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ціноутворення](https://huggingface.co/pricing) | [Токени доступу](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat має обмежену кількість моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Безкоштовно (працює на вашому пристрої) | Не потрібно | [Локальний CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Повністю офлайн, OpenAI-сумісна кінцева точка |
| | | | | |

Дотримуйтесь вказівок нижче для _налаштування_ цього репозиторію для використання з різними провайдерами. Завдання, які вимагають конкретного провайдера, матимуть один із цих тегів у назві файлу:

- `aoai` - потрібні кінцева точка Azure OpenAI, ключ
- `oai` - потрібні кінцева точка OpenAI, ключ
- `hf` - потрібен токен Hugging Face
- `githubmodels` - потрібні кінцева точка Microsoft Foundry Models, ключ (GitHub Models припиняють роботу наприкінці липня 2026)

Ви можете налаштувати одного, жодного або всіх провайдерів. Пов’язані завдання просто видаватимуть помилку за відсутності облікових даних.

## Створення файлу `.env`

Ми припускаємо, що ви вже прочитали вказівки вище, зареєструвалися у відповідного провайдера та отримали необхідні облікові дані для автентифікації (API_KEY або токен). У випадку Azure OpenAI, ми припускаємо, що у вас також є дійсне розгортання служби Azure OpenAI (кінцева точка) з мінімум одною GPT-моделлю, розгорнутою для чат-завершень.

Наступним кроком є налаштування ваших **локальних змінних середовища** таким чином:

1. Знайдіть у кореневій папці файл `.env.copy`, він повинен містити такий вміст:

   ```bash
   # Провайдер OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI у Microsoft Foundry
   ## (Сервіс Azure OpenAI тепер є частиною Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # За замовчуванням встановлено! (поточна стабільна версія GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Моделі Microsoft Foundry (каталог моделей кількох провайдерів, замінює моделі GitHub, які будуть виведені з експлуатації наприкінці липня 2026 року)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Копіюйте цей файл у `.env` за допомогою наведеної нижче команди. Цей файл є _ gitignore_, щоб зберегти секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть заповнювачі праворуч від `=`), як описано у наступному розділі.

4. (Опціонально) Якщо ви використовуєте GitHub Codespaces, у вас є можливість зберегти змінні середовища як _Codespaces secrets_, пов’язані з цим репозиторієм. У цьому випадку вам не потрібно налаштовувати локальний файл .env. **Однак зауважте, що цей варіант працює лише тоді, коли ви користуєтесь GitHub Codespaces.** Вам все одно доведеться налаштовувати файл .env, якщо ви користуєтеся Docker Desktop.

## Заповнення файлу `.env`

Давайте швидко розглянемо назви змінних, щоб зрозуміти, що вони означають:

| Змінна  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Це токен доступу користувача, який ви налаштували у профілі |
| OPENAI_API_KEY | Це ключ авторизації для використання сервісу не Azure OpenAI |
| AZURE_OPENAI_API_KEY | Це ключ авторизації для використання цього сервісу |
| AZURE_OPENAI_ENDPOINT | Це розгорнута кінцева точка ресурсу Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Це точка розгортання _моделі генерації тексту_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Це точка розгортання _моделі ембеддінгів тексту_ |
| AZURE_INFERENCE_ENDPOINT | Це кінцева точка для вашого проєкту Microsoft Foundry, використовується для Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Це API-ключ вашого проєкту Microsoft Foundry |
| | |

Примітка: Останні дві змінні Azure OpenAI відображають модель за замовчуванням для чат-завершення (генерації тексту) та пошуку векторів (ембеддінгів) відповідно. Інструкції щодо їх налаштування будуть описані у відповідних завданнях.

## Налаштування Azure OpenAI: З порталу

> **Примітка:** Сервіс Azure OpenAI тепер є частиною [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ресурси та розгортання все ще відображаються в порталі Azure, але щоденне керування моделями (розгортання, пісочниця, моніторинг) тепер відбувається у порталі Foundry замість старого окремого "Azure OpenAI Studio".

Значення кінцевої точки та ключа Azure OpenAI можна знайти в [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), тому почнемо звідти.

1. Перейдіть до [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Клікніть опцію **Keys and Endpoint** у боковій панелі (меню зліва).
1. Натисніть **Show Keys** — ви побачите таке: KEY 1, KEY 2 та Endpoint.
1. Використайте значення KEY 1 як AZURE_OPENAI_API_KEY
1. Використайте значення Endpoint як AZURE_OPENAI_ENDPOINT

Далі нам потрібні кінцеві точки для конкретних моделей, які ми розгорнули.

1. Клікніть опцію **Model deployments** у боковій панелі (лівому меню) для ресурсу Azure OpenAI.
1. На сторінці призначення клацніть **Перейти до порталу Microsoft Foundry** (або **Керувати розгортаннями**, залежно від типу ресурсу)

Ви потрапите до порталу Microsoft Foundry, де знайдемо інші значення, описані нижче.

## Налаштування Azure OpenAI: З порталу Microsoft Foundry

1. Перейдіть до [порталу Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **з вашого ресурсу**, як описано вище.
1. Виберіть вкладку **Deployments** (бокова панель, зліва) для перегляду поточно розгорнутих моделей.
1. Якщо бажана модель не розгорнута, використайте **Deploy model** для її розгортання зі [каталогу моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Вам потрібна модель _text-generation_ — рекомендуємо: **gpt-5-mini**
1. Вам потрібна модель _text-embedding_ — рекомендуємо **text-embedding-3-small**

Тепер оновіть змінні середовища, щоб відобразити _ім’я розгортання_, яке було використано. Зазвичай воно співпадає з назвою моделі, якщо ви явно його не змінювали. Отже, як приклад, у вас може бути:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Не забудьте зберегти файл .env після завершення.** Тепер можете закрити файл і повернутися до інструкцій для запуску ноутбука.

## Налаштування OpenAI: З профілю

Ваш API-ключ OpenAI можна знайти у вашому [акаунті OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Якщо у вас його немає, ви можете зареєструватися і створити API-ключ. Отриманий ключ використовуйте для заповнення змінної `OPENAI_API_KEY` у файлі `.env`.

## Налаштування Hugging Face: З профілю

Ваш токен Hugging Face можна знайти у вашому профілі на сторінці [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публікуйте і не діліться ним публічно. Натомість створіть новий токен для використання у цьому проєкті і скопіюйте його у файл `.env` у змінну `HUGGING_FACE_API_KEY`. _Примітка:_ технічно це не API-ключ, але використовується для автентифікації, тож ми зберігаємо цю назву для послідовності.

## Налаштування Microsoft Foundry Models: З порталу

> **Примітка:** GitHub Models припиняє роботу наприкінці липня 2026 року. Microsoft Foundry Models є прямою заміною, пропонуючи той самий каталог моделей із безкоштовною демоверсією та досвід користування Azure AI Inference SDK / OpenAI SDK.

1. Перейдіть до [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) та створіть (або відкрийте) проєкт Foundry.
1. Перегляньте [каталог моделей](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) і розгорніть обрану модель, наприклад `gpt-5-mini`.
1. На сторінці **Огляд** проєкту скопіюйте **кінцеву точку** й **API-ключ**.
1. Використайте значення кінцевої точки як `AZURE_INFERENCE_ENDPOINT` і ключ як `AZURE_INFERENCE_CREDENTIAL` у файлі `.env`.

## Офлайн / локальні провайдери

Якщо ви взагалі не хочете користуватися хмарною підпискою, можна запускати сумісні відкриті моделі безпосередньо на власному пристрої:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – середовище виконання Microsoft на пристрої. Автоматично вибирає найкращого постачальника виконання (NPU, GPU або CPU) і надає OpenAI-сумісну кінцеву точку, тож можна використовувати більшість зразків коду цього курсу з мінімальними змінами. Ознайомтеся з [документацією Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) для початку або встановіть командою `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – популярна альтернатива для запуску відкритих моделей на кшталт Llama, Phi, Mistral і Gemma локально.


Дивіться [Урок 19: Побудова за допомогою SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) для практичних прикладів використання обох варіантів.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->