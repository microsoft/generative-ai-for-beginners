<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:39:33+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "uk"
}
-->
# Налаштування вашого середовища розробки

Ми налаштували цей репозиторій і курс з використанням [контейнера для розробки](https://containers.dev?WT.mc_id=academic-105485-koreyst), який має універсальне середовище виконання, що підтримує розробку на Python3, .NET, Node.js та Java. Відповідна конфігурація визначена у файлі `devcontainer.json`, який знаходиться у папці `.devcontainer/` в корені цього репозиторію.

Щоб активувати контейнер для розробки, запустіть його у [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (для хмарного середовища виконання) або у [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (для локального середовища). Детальніше про роботу контейнерів для розробки у VS Code читайте у [цьому посібнику](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst).  

> [!TIP]  
> Рекомендуємо використовувати GitHub Codespaces для швидкого старту з мінімальними зусиллями. Він надає щедру [безкоштовну квоту використання](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) для персональних акаунтів. Налаштуйте [таймаути](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), щоб зупиняти або видаляти неактивні codespaces і максимально ефективно використовувати квоту.

## 1. Виконання завдань

Кожен урок міститиме _необов’язкові_ завдання, які можуть бути надані однією або кількома мовами програмування, зокрема: Python, .NET/C#, Java та JavaScript/TypeScript. У цьому розділі наведено загальні рекомендації щодо виконання таких завдань.

### 1.1 Завдання на Python

Завдання на Python надаються у вигляді додатків (`.py` файли) або Jupyter ноутбуків (`.ipynb` файли).  
- Щоб запустити ноутбук, відкрийте його у Visual Studio Code, потім натисніть _Select Kernel_ (у верхньому правому куті) і виберіть стандартний варіант Python 3. Тепер можна виконати _Run All_ для запуску всього ноутбука.  
- Щоб запускати Python-додатки з командного рядка, дотримуйтесь інструкцій, специфічних для завдання, щоб вибрати правильні файли та передати необхідні аргументи.

## 2. Налаштування провайдерів

Завдання **можуть** бути налаштовані для роботи з одним або кількома розгортаннями великих мовних моделей (LLM) через підтримуваних провайдерів сервісів, таких як OpenAI, Azure або Hugging Face. Вони надають _хостингову кінцеву точку_ (API), до якої ми можемо програмно звертатися з правильними обліковими даними (API ключ або токен). У цьому курсі ми розглядаємо такі провайдери:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) з різноманітними моделями, включно з основною серією GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI з орієнтацією на корпоративне використання.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для відкритих моделей та сервера інференсу.

**Для цих вправ вам знадобляться власні акаунти**. Завдання є необов’язковими, тож ви можете налаштувати одного, усіх або жодного з провайдерів залежно від ваших інтересів. Ось деякі рекомендації щодо реєстрації:

| Реєстрація | Вартість | API ключ | Пісочниця | Коментарі |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ціни](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Проєктні ключі](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без коду, веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно кілька моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ціни](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Швидкий старт SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Швидкий старт Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потрібна попередня заявка на доступ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ціни](https://huggingface.co/pricing) | [Токени доступу](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat має обмежену кількість моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Дотримуйтесь інструкцій нижче, щоб _налаштувати_ цей репозиторій для роботи з різними провайдерами. Завдання, які потребують конкретного провайдера, матимуть один із цих тегів у назві файлу:
 - `aoai` - потребує кінцеву точку Azure OpenAI та ключ
 - `oai` - потребує кінцеву точку OpenAI та ключ
 - `hf` - потребує токен Hugging Face

Ви можете налаштувати одного, кількох або всіх провайдерів. Якщо облікові дані відсутні, відповідні завдання просто видадуть помилку.

###  2.1. Створення файлу `.env`

Припускаємо, що ви вже ознайомилися з вказівками вище, зареєструвалися у відповідного провайдера та отримали необхідні облікові дані для автентифікації (API_KEY або токен). У випадку Azure OpenAI, припускаємо, що у вас також є дійсне розгортання служби Azure OpenAI (endpoint) з принаймні однією GPT-моделлю для чат-комплішену.

Наступний крок — налаштувати ваші **локальні змінні середовища** таким чином:

1. Знайдіть у кореневій папці файл `.env.copy`, який має приблизно такий вміст:

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

2. Скопіюйте цей файл у `.env` за допомогою наведеної нижче команди. Цей файл додано до _gitignore_, щоб зберегти секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть плейсхолдери праворуч від `=`) відповідно до опису у наступному розділі.

3. (Опціонально) Якщо ви використовуєте GitHub Codespaces, у вас є можливість зберегти змінні середовища як _секрети Codespaces_, пов’язані з цим репозиторієм. У такому разі локальний файл .env налаштовувати не потрібно. **Однак зверніть увагу, що ця опція працює лише з GitHub Codespaces.** Якщо ви використовуєте Docker Desktop, файл .env все одно потрібно налаштувати.

### 2.2. Заповнення файлу `.env`

Давайте швидко розглянемо назви змінних, щоб зрозуміти, що вони означають:

| Змінна  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Це токен доступу користувача, який ви налаштували у своєму профілі |
| OPENAI_API_KEY | Ключ авторизації для використання сервісу OpenAI, не пов’язаного з Azure |
| AZURE_OPENAI_API_KEY | Ключ авторизації для використання сервісу Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Кінцева точка розгортання ресурсу Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Кінцева точка розгортання моделі для _генерації тексту_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Кінцева точка розгортання моделі для _векторних уявлень тексту_ |
| | |

Примітка: Останні дві змінні Azure OpenAI відповідають за модель за замовчуванням для чат-комплішену (генерації тексту) та пошуку за векторами (ембеддінги) відповідно. Інструкції щодо їх налаштування будуть наведені у відповідних завданнях.

### 2.3 Налаштування Azure: через портал

Значення кінцевої точки та ключа Azure OpenAI можна знайти у [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), тож почнемо звідти.

1. Перейдіть до [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. У бічному меню (зліва) натисніть опцію **Keys and Endpoint**  
3. Натисніть **Show Keys** — ви побачите: KEY 1, KEY 2 та Endpoint  
4. Використайте значення KEY 1 для AZURE_OPENAI_API_KEY  
5. Використайте значення Endpoint для AZURE_OPENAI_ENDPOINT

Далі нам потрібні кінцеві точки для конкретних моделей, які ми розгорнули.

1. У бічному меню (зліва) для ресурсу Azure OpenAI натисніть **Model deployments**  
2. На сторінці, що відкриється, натисніть **Manage Deployments**

Це перенаправить вас на сайт Azure OpenAI Studio, де ми знайдемо інші необхідні значення, як описано нижче.

### 2.4 Налаштування Azure: через Studio

1. Перейдіть до [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **через ваш ресурс**, як описано вище.  
2. Натисніть вкладку **Deployments** (бічне меню зліва), щоб переглянути поточні розгортання моделей.  
3. Якщо потрібна модель не розгорнута, скористайтеся **Create new deployment** для її розгортання.  
4. Вам потрібна модель для _генерації тексту_ — рекомендуємо: **gpt-35-turbo**  
5. Вам потрібна модель для _векторних уявлень тексту_ — рекомендуємо **text-embedding-ada-002**

Тепер оновіть змінні середовища, щоб відобразити ім’я _Deployment_, яке ви використовуєте. Зазвичай це таке саме, як ім’я моделі, якщо ви явно його не змінювали. Наприклад, у вас може бути:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забудьте зберегти файл .env після внесення змін**. Тепер ви можете закрити файл і повернутися до інструкцій щодо запуску ноутбука.

### 2.5 Налаштування OpenAI: через профіль

Ваш OpenAI API ключ можна знайти у вашому [акаунті OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Якщо у вас його немає, зареєструйтеся та створіть API ключ. Після отримання ключа внесіть його у змінну `OPENAI_API_KEY` у файлі `.env`.

### 2.6 Налаштування Hugging Face: через профіль

Ваш токен Hugging Face можна знайти у вашому профілі в розділі [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публікуйте і не діліться ним публічно. Замість цього створіть новий токен для використання у цьому проєкті і скопіюйте його у файл `.env` у змінну `HUGGING_FACE_API_KEY`. _Примітка:_ технічно це не API ключ, але використовується для автентифікації, тому ми зберігаємо цю назву для узгодженості.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.