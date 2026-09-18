# Історія змін

Усі помітні зміни у навчальній програмі Generative AI for Beginners задокументовані у цьому файлі.

Формат базується на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Оскільки це
навчальна програма, а не версійний програмний пакет, записи згруповані за датою.

## [2026-07-16] — Перевірка вмісту + Зображення для уроку 09

### Змінено

- **Урок 10 (низькокодові AI-додатки):** оновлено два застарілі посилання `docs.microsoft.com/powerapps/...` Dataverse
  на поточні `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (перевірено в реальному часі).
- **Урок 17 (AI агенти):** оновлено застарілий приклад моделі (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) та ім'я маски розгортання у прикладі Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Кореневий `README.md`:** додано відсутній `?WT.mc_id=academic-105485-koreyst` ідентифікатор відстеження до
  посилання *Microsoft for Startups*.
- **Зображення для уроку 09** згенеровані заново за моделлю `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, та
  `images/startup.png` (пара до/після прикладу редагування була створена через реальний
  виклик `client.images.edit` з автоствореною маскою).

### Перевірено

- Перевірено README файли уроків 01, 03, 05, 12, 14 та 16 — усі актуальні (правильні імена Microsoft Foundry
  і посилання); змін не потрібно.
- Виконана повна перевірка синтаксису markdown у всіх 41 markdown файлах репозиторію (без перекладів) на
  застарілі шляхи документації, локалі Microsoft `/en-us/`, застарілі назви продуктів/моделей, відсутні
  ідентифікатори відстеження та пошкоджені відносні посилання/зображення. Єдина проблема була
  з відсутнім ідентифікатором відстеження *Microsoft for Startups*; всі інші помітки виявились помилковими
  (автоматично згенеровані посилання на переклади, закоментовані заповнювачі та сторонні структурні URL `/en/`).

## [2026-07-15] — Перепис уроку 09 (Застосування зображень) для моделей GPT Image

### Змінено

- **Переписано урок 09 "Створення додатків генерації зображень"** на основі поточної сім’ї моделей **`gpt-image`**
  (за замовчуванням **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` також GA), замість
  застарілого контенту DALL·E 2/3. Основні корекції:
  - Моделі `gpt-image` повертають зображення у форматі **base64 (`b64_json`)**, а не URL. Оновлено всі приклади
    для використання `base64.b64decode(...)` замість завантаження `url` через `requests`.
  - Оновлено версію API зображень до `2025-04-01-preview`.
  - Замінено вигаданий розділ "temperature" (моделі зображень не використовують `temperature`) і
    контент DALL·E-2-only зображень **варіації** на розділ **редагування зображень** (маскування/домальовування).
  - Оновлено `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, обидва
    зошити для завдань (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), і `.dib` .NET зошит.

### Видалено

- Видалено застарілі зразки `python/aoai-app-variation.py` і `python/oai-app-variation.py`
  (`images.create_variation` підтримує тільки DALL·E-2 і не підтримується `gpt-image`).
- Видалено 4 покинуті активи зображень, пов’язані з видаленим розділом порівняння температури
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Прибрано непотрібну залежність `requests` з прикладів на Python і вимог уроку.

### Перевірено

- Виконано `aoai-app.py` повністю з розгорнутою моделлю `gpt-image-1.5` і підтверджено, що
  процес розкодування/збереження base64 виробляє PNG. Зошити підтверджено як дійсний JSON.

## [2026-07-14] — Оновлення моделі за замовчуванням + керівництво з моделей розуміння

### Зміни

- **Модель чату за замовчуванням `gpt-4o-mini` → `gpt-5-mini`** в робочих прикладах
  навчального курсу, документації та налаштуваннях. Це було викликано статусом життєвого циклу моделі:
  у Microsoft Foundry, `gpt-4o-mini` (припиняється 2026-10-01) і вся сім’я `gpt-4.1`
  (`gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, припиняються 2026-10-14) **знімаються з підтримки**, тоді як
  **сім’я GPT-5 (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) є загальнодоступною** (припиняється 2027-02-06).
  Оновлено:
  - `.env.copy`, `00-course-setup/03-providers.md` (рекомендовані команди розгортання та `az cognitiveservices`),
    і README для уроків 04, 06, 07 і 15.
  - Приклади Python в уроці 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) і скрипти уроку 08.
  - Приклади TypeScript / JavaScript в уроках 06, 07 і 11 та `.dib` .NET зошити для
    уроків 06 і 07.
  - Зошити для завдань в уроках 04, 06, 07 і 11 (кодні клітинки), а також приклади у docstring файлі `shared/python/api_utils.py`.
- **Рекомендації щодо параметрів моделі логічного мислення (нове).** `gpt-5-mini` — це модель *логічного мислення*: вона **не** 
  підтримує `temperature`/`top_p` і замість `max_tokens` використовує `max_completion_tokens` (чат-відповіді) / 
  `max_output_tokens` (Responses API). Відповідно:
  - Видалено `temperature`/`top_p`/`max_tokens` зі зразків, які тепер за замовчуванням використовують `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Додано примітку **"Моделі міркувань не використовують `temperature`"** до уроку 06, яка пояснює, що
    моделі міркувань керуються **інженерією підказок + контролем міркувань**, а не
    налаштуваннями семплування, тоді як `temperature`/`top_p` залишаються дійсними для неміркувальних моделей
    (GPT-4.x, Mistral, Llama, Phi, відкриті моделі).
- **`gpt-5-mini` не використовується для уроку з тонкого налаштування (lesson 18).** GPT-5 підтримує
  лише підкріплене тонке налаштування (RFT); у уроці 18 з керованого тонкого налаштування (SFT) залишається
  `gpt-4.1-mini`, який підтримує SFT/DPO.
- **Демонстрації Temperature використовують модель Llama.** Щоб продовжити навчання `temperature` (який заперечують моделі міркувань),
  використовується модель `Llama-3.3-70B-Instruct` через кінцеву точку Foundry Models. Додано нову
  змінну `AZURE_INFERENCE_CHAT_MODEL` до `.env.copy`; ноутбуки уроків 04/06 `githubmodels` та
  зразок `06` `js-githubmodels` читають її (з відкатом до `Llama-3.3-70B-Instruct`) і зберігають свої
  демонстрації `temperature`/`top_p`/`max_tokens`.
- **Оновлені зразки JS / .NET під GPT-5.** Видалено `temperature`/`top_p`/`max_tokens` зі зразків GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - в яких також піднято `MaxOutputTokenCount`,
  щоб запобігти обрізанню виводу міркувань). У зразку `06` `js-githubmodels` тепер використовується Llama, щоб зберегти
  демонстрацію temperature. `.dib` зазначає, що `Azure.AI.Inference` + модель Llama є способом
  демонстрації `Temperature` у .NET.
- Залишено `gpt-4o-mini` / `gpt-5-mini` на місцях, де це залишалося точним: посилання на кодування токенів у `tiktoken`,
  списки доступності в каталозі моделей і мовленнєві моделі уроку 02 (`gpt-4o-transcribe`).
- Зразки уроків 20 (Mistral) та 21 (Meta) зберігають `temperature`/`max_tokens`, оскільки вони націлені на
  моделі Mistral/Llama, які підтримують ці параметри.

## [2026-07-06] — Оновлення модернізації контенту

Широке оновлення для збереження актуальності навчальної програми на 2026 рік: сучасні API, поточні назви продуктів та
імена моделей, оновлені рекомендації постачальників і нові інструменти для покращення досвіду розробника.

### Додано

- Розділ **Microsoft Agent Framework** в уроці `17-ai-agents`, що висвітлює одно-чатові агенти,
  інструменти/виклик функцій, конфігурацію Azure OpenAI (Microsoft Foundry) та багатоеагентну
  оркестрацію робочих процесів (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** задокументовано як офлайн / локальний провайдер (пліч-о-пліч з Ollama) у
  `00-course-setup/03-providers.md` та у уроці `19-slm`.
- **Безперервна інтеграція**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (навантаження на підтримуваний модуль `shared/`,
    порада для решти курсу), порада ESLint, та pytest завдання.
  - `.github/workflows/security.yml` — аналіз CodeQL (Python + JavaScript/TypeScript) та
    перевірка залежностей на запитах на злиття.
- **Набір тестів** у `tests/` — 41 pytest тест, що покриває спільний утилітний модуль.
- **Навичка міграції Azure OpenAI → Responses API** у
  `.github/skills/azure-openai-to-responses/`, що використовувалась для керівництва міграцією API.

### Змінено

- **Chat Completions API → Responses API** у всіх прикладах чатів на Python та TypeScript
  (`client.responses.create(...)` → `response.output_text`), включно з уроками 04, 06, 07, 11,
  15 і 18, а також їхніми README.
- **GitHub Models → Microsoft Foundry Models** у всьому тексті, посиланнях і прикладах. GitHub Models
  припиняє роботу наприкінці липня 2026; приклади тепер вказують на каталог моделей Microsoft Foundry і використовують
  змінні середовища `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **Оновлено `.env.copy`, `AGENTS.md` та документацію провайдера**, щоб відобразити, що Azure OpenAI тепер є частиною
  Microsoft Foundry, і стандартна версія API піднята до `2024-10-21`.
- **Приклади на TypeScript** (уроки 06, 07, 08, 11) мігрували зі застарілого бета SDK `@azure/openai`
  на пакет `openai` (чат-застосунки використовують Responses API; застосунок пошуку - embeddings client).

- **.NET блокноти** (`dotnet/*.dib`) стандартизовані на `Azure.AI.OpenAI` **2.1.0**: уроки 06 і 07
  використовують API `ChatClient`, урок 08 використовує `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), а
  урок 09 використовує `ImageClient` (`GenerateImage`) з `gpt-image-1`, замінюючи застарілі
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` з `1.0.0-beta.9`.
- **Модернізація назв продуктів**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (уроки 14, 16, 17) і "Bing" → **Microsoft Copilot** (урок 12), де ці назви стосувалися
  поточних продуктів.
- **DevContainer** (`.devcontainer/`) тепер постачається з розширеннями Pylance, Black, Ruff, ESLint, Prettier та Copilot,
  увімкнено форматування під час збереження та інстальовано `ruff`, `black`, `mypy` та `pytest`, щоб
  перевірки CI можна було відтворити локально.
- **Генерація зображень** (урок 09) рекомендує `gpt-image-1` для Azure (каталог Azure прибрав
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** оновлено, щоб відобразити виконану роботу (міграція API, CI,
  DevContainer, тести) і поточні факти (переклади створюються автоматично за допомогою
  Azure Co-op Translator; API асистентів замінено API відповідей).

### Виправлено

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` тепер повертає
  порожній рядок для вводу, що складається лише з пробілів, замість генерації помилки "занадто короткий"
  (послідовно з випадком `None`). Знайдено та покрито новим набором тестів.
- **Зразки з Lesson 09 зображень** — виправлені реальні помилки: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  а також змінна, що затіняла модуль `openai`.
- **Ноутбук Lesson 15 RAG** — відновлено налаштування клієнта, замінено вилучений `DataFrame.append`
  на `pd.concat`, оновлено використання застарілого SDK.
- Застарілі / вилучені імена моделей (`gpt-3.5-turbo`, `gpt-35-turbo`) замінено на `gpt-4o-mini`
  у активних зразках; історичні результати донавчання в уроці 18 збережено та прокоментовано,
  а не переписано.

### Застаріле / Примітки

- **Зразки моделей Microsoft Foundry**, які використовують SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — зразки `githubmodels-*` і `js-githubmodels`, а також уроки 19, 20,
  і 21 — залишаються на Model Inference API, який **не** підтримує Responses API. Вони
  навмисно залишені на цьому SDK.
- `AzureOpenAI()` умисно зберігається там, де це ще доречно (векторні подання та генерація зображень),
  оскільки ці робочі процеси не є частиною міграції Responses API.
- Посилання на `text-embedding-ada-002` збережено там, де на них залежить заздалегідь обчислений індекс embedding.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->