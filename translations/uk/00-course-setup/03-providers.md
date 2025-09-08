<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T20:05:23+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "uk"
}
-->
# Вибір і налаштування провайдера LLM 🔑

Завдання **можуть** бути налаштовані для роботи з одним або кількома розгортаннями великих мовних моделей (LLM) через підтримуваного провайдера, такого як OpenAI, Azure або Hugging Face. Вони надають _хостований endpoint_ (API), до якого можна отримати доступ програмно з відповідними обліковими даними (API-ключ або токен). У цьому курсі ми розглядаємо такі сервіси:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) з різноманітними моделями, включаючи основну серію GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) для моделей OpenAI з акцентом на корпоративне використання
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) для відкритих моделей та inference-сервера

**Для виконання вправ вам знадобляться власні акаунти**. Завдання є необов’язковими, тому ви можете налаштувати одного, всіх або жодного з провайдерів — залежно від ваших інтересів. Декілька порад щодо реєстрації:

| Реєстрація | Вартість | API-ключ | Playground | Коментарі |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Ціни](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [На основі проєкту](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Доступно кілька моделей |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Ціни](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Потрібно подати заявку заздалегідь](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Ціни](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat має обмежену кількість моделей](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Дотримуйтесь інструкцій нижче, щоб _налаштувати_ цей репозиторій для роботи з різними провайдерами. Завдання, які вимагають конкретного провайдера, міститимуть один із таких тегів у назві файлу:

- `aoai` - потрібен endpoint та ключ Azure OpenAI
- `oai` - потрібен endpoint та ключ OpenAI
- `hf` - потрібен токен Hugging Face

Ви можете налаштувати одного, жодного або всіх провайдерів. Відповідні завдання просто видадуть помилку, якщо не вистачає облікових даних.

## Створення файлу `.env`

Ми припускаємо, що ви вже ознайомилися з інструкціями вище, зареєструвалися у відповідного провайдера та отримали необхідні облікові дані для автентифікації (API_KEY або токен). У випадку з Azure OpenAI, також потрібно мати дійсне розгортання Azure OpenAI Service (endpoint) з принаймні однією GPT-моделлю для завершення чатів.

Далі потрібно налаштувати **локальні змінні середовища** наступним чином:

1. Знайдіть у кореневій папці файл `.env.copy`, який має містити приблизно таке:

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

2. Скопіюйте цей файл у `.env` за допомогою команди нижче. Цей файл додано до _gitignore_, щоб зберігати секрети в безпеці.

   ```bash
   cp .env.copy .env
   ```

3. Заповніть значення (замініть плейсхолдери праворуч від `=`) згідно з описом у наступному розділі.

4. (Опціонально) Якщо ви використовуєте GitHub Codespaces, можна зберегти змінні середовища як _Codespaces secrets_, пов’язані з цим репозиторієм. У такому випадку локальний файл .env створювати не потрібно. **Зверніть увагу, що ця опція працює лише з GitHub Codespaces.** Якщо ж ви використовуєте Docker Desktop, файл .env все одно потрібно налаштувати.

## Заповнення файлу `.env`

Давайте коротко розглянемо назви змінних, щоб зрозуміти, що вони означають:

| Змінна  | Опис  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Це токен доступу користувача, який ви створили у своєму профілі |
| OPENAI_API_KEY | Це ключ авторизації для використання сервісу (не для Azure OpenAI endpoint) |
| AZURE_OPENAI_API_KEY | Це ключ авторизації для використання цього сервісу |
| AZURE_OPENAI_ENDPOINT | Це endpoint розгорнутого ресурсу Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Це endpoint розгортання моделі _генерації тексту_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Це endpoint розгортання моделі _embeddings_ |
| | |

Примітка: Останні дві змінні Azure OpenAI відповідають моделі за замовчуванням для завершення чатів (генерація тексту) та векторного пошуку (embeddings) відповідно. Інструкції щодо їх налаштування будуть у відповідних завданнях.

## Налаштування Azure: через портал

Значення endpoint та ключа Azure OpenAI можна знайти у [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), тож почнемо звідти.

1. Перейдіть у [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Виберіть опцію **Keys and Endpoint** у бічному меню (зліва).
1. Натисніть **Show Keys** — ви побачите: KEY 1, KEY 2 та Endpoint.
1. Використайте значення KEY 1 для AZURE_OPENAI_API_KEY
1. Використайте значення Endpoint для AZURE_OPENAI_ENDPOINT

Далі нам потрібні endpoint-и для конкретних моделей, які ви розгорнули.

1. Виберіть опцію **Model deployments** у бічному меню (зліва) для ресурсу Azure OpenAI.
1. На сторінці, що відкриється, натисніть **Manage Deployments**

Це переведе вас на сайт Azure OpenAI Studio, де ми знайдемо інші значення, як описано нижче.

## Налаштування Azure: через Studio

1. Перейдіть у [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **з вашого ресурсу**, як описано вище.
1. Виберіть вкладку **Deployments** (бічне меню зліва), щоб переглянути розгорнуті моделі.
1. Якщо потрібна модель ще не розгорнута, скористайтеся **Create new deployment** для її розгортання.
1. Вам потрібна модель _text-generation_ — рекомендуємо: **gpt-35-turbo**
1. Вам потрібна модель _text-embedding_ — рекомендуємо **text-embedding-ada-002**

Тепер оновіть змінні середовища, вказавши _Deployment name_, який ви використали. Зазвичай це збігається з назвою моделі, якщо ви її не змінювали. Наприклад, це може виглядати так:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Не забудьте зберегти файл .env після змін.** Тепер можна закрити файл і повернутися до інструкцій щодо запуску ноутбука.

## Налаштування OpenAI: через профіль

Ваш OpenAI API-ключ можна знайти у [вашому акаунті OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Якщо у вас його ще немає, зареєструйте акаунт і створіть API-ключ. Після отримання ключа використайте його для заповнення змінної `OPENAI_API_KEY` у файлі `.env`.

## Налаштування Hugging Face: через профіль

Ваш токен Hugging Face знаходиться у профілі в розділі [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Не публікуйте та не діліться цим токеном. Створіть новий токен спеціально для цього проєкту та скопіюйте його у файл `.env` у змінну `HUGGING_FACE_API_KEY`. _Примітка:_ Технічно це не API-ключ, але він використовується для автентифікації, тому ми залишаємо таку назву для зручності.

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичний переклад може містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильне тлумачення, що виникли внаслідок використання цього перекладу.