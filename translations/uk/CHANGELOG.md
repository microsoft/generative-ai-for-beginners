# Журнал змін

Усі значущі зміни у навчальному курсі Generative AI for Beginners задокументовані в цьому файлі.

Формат базується на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Оскільки це
навчальний курс, а не версійний програмний пакет, записи згруповані за датою.

## [2026-07-06] — Оновлення модернізації контенту

Широке оновлення для збереження актуальності курсу на 2026 рік: сучасні API, поточні назви продуктів і
моделей, оновлені рекомендації для провайдерів і нові інструменти для досвіду розробника.

### Додано

- Розділ **Microsoft Agent Framework** у уроці `17-ai-agents`, що охоплює агентів із одним чатом,
  інструменти/виклики функцій, конфігурацію Azure OpenAI (Microsoft Foundry) і оркестрацію
  багатоагентного робочого процесу (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** документовано як офлайн / локального провайдера (поряд з Ollama) у
  `00-course-setup/03-providers.md` та уроці `19-slm`.
- **Робочі потоки безперервної інтеграції**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (наглядається у підтримуваному модулі `shared/`,
    порада для решти курсу), додатковий ESLint pass та завдання pytest.
  - `.github/workflows/security.yml` — аналіз CodeQL (Python + JavaScript/TypeScript) та
    перевірка залежностей при pull request.
- **Тестовий набір** у `tests/` — 41 тест pytest, що охоплюють спільний утилітний модуль.
- Навичка **міграції Azure OpenAI → Responses API** у
  `.github/skills/azure-openai-to-responses/` для керування міграцією API.

### Змінено

- **Chat Completions API → Responses API** у всіх прикладах чату на Python і TypeScript
  (`client.responses.create(...)` → `response.output_text`), включно з уроками 04, 06, 07, 11,
  15 і 18, а також їх README.
- **GitHub Models → Microsoft Foundry Models** у всьому тексті, посиланнях і прикладах. GitHub Models
  припиняється наприкінці липня 2026 року; приклади тепер посилаються на каталог моделей Microsoft Foundry і використовують
  змінні оточення `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Оновлено **`.env.copy`, `AGENTS.md` та документацію провайдерів**, щоб відобразити, що Azure OpenAI тепер є частиною
  Microsoft Foundry, а версія API за замовчуванням підвищена до `2024-10-21`.
- Приклади на **TypeScript** (уроки 06, 07, 08, 11) переміщені з застарілого бета SDK `@azure/openai`
  до пакунка `openai` (додатки чату використовують Responses API; додаток пошуку — клієнт embeddings).
- **.NET блокноти** (`dotnet/*.dib`) стандартизовані на версії `Azure.AI.OpenAI` **2.1.0**: уроки 06 і 07
  використовують API `ChatClient`, урок 08 — `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), а
  урок 09 — `ImageClient` (`GenerateImage`) з `gpt-image-1`, замість застарілих
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` з `1.0.0-beta.9`.
- Модернізація назв продуктів: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (уроки 14, 16, 17) та "Bing" → **Microsoft Copilot** (урок 12), там, де йшлося про
  актуальні продукти.
- DevContainer (`.devcontainer/`) тепер містить розширення Pylance, Black, Ruff, ESLint, Prettier і Copilot,
  увімкнено форматування при збереженні, а також встановлені `ruff`, `black`, `mypy` і `pytest` для
  локального відтворення перевірок у CI.
- У генерації зображень (урок 09) рекомендовано `gpt-image-1` для Azure (каталог Azure прибрав
  `dall-e-3`).
- Оновлено **`docs/ENHANCED_FEATURES_ROADMAP.md`** для відображення виконаних робіт (міграція API, CI,
  DevContainer, тести) і поточних фактів (переклади автоматично створює
  Azure Co-op Translator; API Assistant замінено на Responses API).




  порожній рядок для вводу, що складається лише з пробілів, замість помилки "занадто коротко" (услід за
  випадком `None`). Знайдено та охоплено новим тестовим набором.
- Виправлені справжні помилки у зразках зображень уроку 09: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  і змінна, яка перекривала модуль `openai`.
- Відновлено налаштування клієнта в блокноті RAG уроку 15, замінено вилучений `DataFrame.append`
  на `pd.concat` і модернізовано використання застарілого SDK.
- Застарілі / вилучені назви моделей (`gpt-3.5-turbo`, `gpt-35-turbo`) замінено на `gpt-4o-mini`
  у активних прикладах; історичні результати тонкого налаштування в уроці 18 збережено і прокоментовано,
  а не переписано.




  (`client.complete()`) — приклади `githubmodels-*`, `js-githubmodels` та уроки 19, 20,
  21 — залишаються на Model Inference API, який **не** підтримує Responses API. Вони
  свідомо залишені на цьому SDK.
- `AzureOpenAI()` свідомо збережено там, де це все ще доречно (векторні подання та генерація зображень),
  оскільки ці робочі процеси не входять до міграції Responses API.
- Залишено посилання на `text-embedding-ada-002`, де попередньо обчислений індекс векторів
  на них залежить.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->