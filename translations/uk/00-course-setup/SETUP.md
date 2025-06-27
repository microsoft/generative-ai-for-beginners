<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:33:26+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "uk"
}
-->
# Налаштування середовища розробки

Ми налаштували цей репозиторій і курс з [контейнером розробки](https://containers.dev?WT.mc_id=academic-105485-koreyst), який має універсальне середовище виконання, що підтримує розробку на Python3, .NET, Node.js та Java. Відповідна конфігурація визначена у файлі `devcontainer.json`, який знаходиться у папці `.devcontainer/` на корені цього репозиторію.

Щоб активувати контейнер розробки, запустіть його в [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (для хмарного середовища виконання) або в [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (для локального середовища виконання на пристрої). Прочитайте [цю документацію](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) для отримання більш детальної інформації про те, як контейнери розробки працюють у VS Code.

> [!TIP]  
> Ми рекомендуємо використовувати GitHub Codespaces для швидкого старту з мінімальними зусиллями. Він надає щедру [безкоштовну квоту використання](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) для особистих акаунтів. Налаштуйте [тайм-аути](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), щоб зупинити або видалити неактивні codespaces і максимізувати використання вашої квоти.

## 1. Виконання завдань

Кожен урок буде містити _опціональні_ завдання, які можуть бути представлені на одній або більше мовах програмування, включаючи: Python, .NET/C#, Java та JavaScript/TypeScript. Цей розділ надає загальні рекомендації щодо виконання цих завдань.

### 1.1 Завдання на Python

Завдання на Python представлені або як додатки (файли `.py`) або як блокноти Jupyter (файли `.ipynb`).
- Щоб запустити блокнот, відкрийте його у Visual Studio Code, потім натисніть _Select Kernel_ (вгорі праворуч) і виберіть показаний варіант Python 3 за замовчуванням. Тепер ви можете _Run All_ для виконання блокноту.
- Щоб запустити додатки Python з командного рядка, дотримуйтесь інструкцій, специфічних для завдання, щоб переконатися, що ви вибрали правильні файли і надали необхідні аргументи.

## 2. Налаштування провайдерів

Завдання **можуть** також бути налаштовані для роботи з одним або більше розгортанням великих мовних моделей (LLM) через підтримуваного провайдера послуг, такого як OpenAI, Azure або Hugging Face. Вони надають _хостований кінцевий пункт_ (API), до якого ми можемо отримати доступ програмно з правильними обліковими даними (ключ API або токен). У цьому курсі ми обговорюємо цих провайдерів:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) з різноманітними моделями, включаючи основну серію GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI з акцентом на готовність до підприємства.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для моделей з відкритим кодом і сервера інференції.

**Вам потрібно буде використовувати свої власні акаунти для цих вправ**. Завдання є опціональними, тому ви можете вибрати налаштування одного, всіх - або жодного - з провайдерів залежно від ваших інтересів. Деякі рекомендації щодо реєстрації:

| Реєстрація | Вартість | Ключ API | Ігровий майданчик | Коментарі |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ціни](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Проектний](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Без коду, Веб](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступні кілька моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ціни](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Швидкий старт SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Швидкий старт студії](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потрібно подати заявку заздалегідь для доступу](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ціни](https://huggingface.co/pricing) | [Токени доступу](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat має обмежені моделі](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Дотримуйтесь наведених нижче інструкцій, щоб _налаштувати_ цей репозиторій для використання з різними провайдерами. Завдання, які потребують конкретного провайдера, міститимуть один з цих тегів у своєму імені файлу:
- `aoai` - потребує кінцевий пункт Azure OpenAI, ключ
- `oai` - потребує кінцевий пункт OpenAI, ключ
- `hf` - потребує токен Hugging Face

Ви можете налаштувати одного, жодного або всіх провайдерів. Відповідні завдання просто видадуть помилку при відсутності облікових даних.

### 2.1 Створення файлу `.env`

Ми припускаємо, що ви вже прочитали наведені вище рекомендації, зареєструвалися у відповідного провайдера і отримали необхідні облікові дані для аутентифікації (API_KEY або токен). У випадку з Azure OpenAI ми припускаємо, що у вас також є дійсне розгортання служби Azure OpenAI (кінцевий пункт) з принаймні однією моделлю GPT, розгорнутою для завершення чату.

Наступний крок - налаштувати ваші **локальні змінні середовища** наступним чином:

1. Подивіться у кореневій папці файл `.env.copy`, який повинен мати такий вміст:

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

2. Скопіюйте цей файл у `.env`, використовуючи команду нижче. Цей файл _gitignore-d_, зберігаючи секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть заповнювачі на правій стороні `=`) як описано в наступному розділі.

3. (Опція) Якщо ви використовуєте GitHub Codespaces, у вас є можливість зберігати змінні середовища як _секрети Codespaces_, пов'язані з цим репозиторієм. У цьому випадку вам не потрібно буде налаштовувати локальний .env файл. **Однак, зверніть увагу, що ця опція працює лише якщо ви використовуєте GitHub Codespaces.** Ви все ще повинні налаштувати .env файл, якщо використовуєте Docker Desktop.

### 2.2 Заповнення файлу `.env`

Давайте швидко переглянемо назви змінних, щоб зрозуміти, що вони представляють:

| Змінна | Опис |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Це токен доступу користувача, який ви налаштували у своєму профілі |
| OPENAI_API_KEY | Це ключ авторизації для використання сервісу для не-Azure OpenAI кінцевих точок |
| AZURE_OPENAI_API_KEY | Це ключ авторизації для використання цього сервісу |
| AZURE_OPENAI_ENDPOINT | Це розгорнутий кінцевий пункт для ресурсу Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Це кінцевий пункт розгортання моделі _генерації тексту_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Це кінцевий пункт розгортання моделі _вбудовування тексту_ |
| | |

Примітка: Останні дві змінні Azure OpenAI відображають модель за замовчуванням для завершення чату (генерація тексту) та пошуку векторів (вбудовування) відповідно. Інструкції щодо їх налаштування будуть визначені у відповідних завданнях.

### 2.3 Налаштування Azure: З порталу

Значення кінцевої точки та ключа Azure OpenAI будуть знайдені в [порталі Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), тому почнемо там.

1. Перейдіть до [порталу Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Натисніть опцію **Keys and Endpoint** у бічному меню (меню зліва).
1. Натисніть **Show Keys** - ви повинні побачити наступне: KEY 1, KEY 2 та Endpoint.
1. Використовуйте значення KEY 1 для AZURE_OPENAI_API_KEY
1. Використовуйте значення Endpoint для AZURE_OPENAI_ENDPOINT

Далі нам потрібні кінцеві точки для конкретних моделей, які ми розгорнули.

1. Натисніть опцію **Model deployments** у бічному меню (меню зліва) для ресурсу Azure OpenAI.
1. На цільовій сторінці натисніть **Manage Deployments**

Це перенесе вас на веб-сайт Azure OpenAI Studio, де ми знайдемо інші значення, як описано нижче.

### 2.4 Налаштування Azure: З студії

1. Перейдіть до [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **з вашого ресурсу**, як описано вище.
1. Натисніть вкладку **Deployments** (бічне меню, зліва), щоб переглянути розгорнуті моделі.
1. Якщо ваша бажана модель не розгорнута, використовуйте **Create new deployment** для її розгортання.
1. Вам потрібна модель _генерації тексту_ - ми рекомендуємо: **gpt-35-turbo**
1. Вам потрібна модель _вбудовування тексту_ - ми рекомендуємо **text-embedding-ada-002**

Тепер оновіть змінні середовища, щоб відобразити _ім'я розгортання_, яке використовується. Це зазвичай буде таке ж, як ім'я моделі, якщо ви не змінили його явно. Отже, наприклад, ви можете мати:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забудьте зберегти файл .env після завершення**. Тепер ви можете вийти з файлу і повернутися до інструкцій щодо запуску блокноту.

### 2.5 Налаштування OpenAI: З профілю

Ваш ключ API OpenAI можна знайти у вашому [акаунті OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Якщо у вас його немає, ви можете зареєструватися для акаунту і створити ключ API. Після того, як у вас є ключ, ви можете використовувати його для заповнення змінної `OPENAI_API_KEY` у файлі `.env`.

### 2.6 Налаштування Hugging Face: З профілю

Ваш токен Hugging Face можна знайти у вашому профілі у розділі [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публікуйте або не діліться ними публічно. Замість цього створіть новий токен для використання в цьому проекті і скопіюйте його у файл `.env` під змінною `HUGGING_FACE_API_KEY`. _Примітка:_ Це технічно не ключ API, але використовується для аутентифікації, тому ми зберігаємо цю назву для узгодженості.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо точності, будь ласка, майте на увазі, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ на рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають у результаті використання цього перекладу.