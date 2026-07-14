# Промени по версиите

Всички значими промени в учебната програма по Генеративен AI за начинаещи са документирани в този файл.

Форматът се базира на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Тъй като това е
учебна програма, а не софтуерен пакет с версии, записите са групирани по дата.

## [2026-07-06] — Актуализация и модернизация на съдържанието

Широка актуализация за поддържане на точността на учебната програма за 2026: модерни API, актуални имена на продукти и
модели, обновени указания за доставчици и нови инструменти за разработка.

### Добавено

- Раздел **Microsoft Agent Framework** в урока `17-ai-agents`, покриващ агенти за един чат,
  инструменти/извикване на функции, конфигурация на Azure OpenAI (Microsoft Foundry) и мултиагентски
  оркестрационни работни процеси (`SequentialBuilder` / `ConcurrentBuilder`).
- Документиран **Foundry Local** като офлайн/на устройството доставчик (заедно с Ollama) в
  `00-course-setup/03-providers.md` и урок `19-slm`.
- **Работни потоци за непрекъсната интеграция**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (принудително в поддържания модул `shared/`,
    съветници в останалата част от учебната програма), съветническо извършване на ESLint и задача pytest.
  - `.github/workflows/security.yml` — анализ с CodeQL (Python + JavaScript/TypeScript) и
    преглед на зависимости при pull заявки.
- **Тестов пакет** под `tests/` — 41 pytest теста покриващи споделения модул с помощни функции.
- **Умение за миграция от Azure OpenAI към Responses API** под
  `.github/skills/azure-openai-to-responses/`, използвано за насочване на API миграцията.

### Променено

- **Chat Completions API → Responses API** във всички примерни чатове на Python и TypeScript
  (`client.responses.create(...)` → `response.output_text`), включително уроци 04, 06, 07, 11,
  15 и 18, плюс техните README файлове.
- **GitHub Models → Microsoft Foundry Models** в текстове, връзки и примери. GitHub Models
  се отказва в края на юли 2026; примерите вече сочат към каталога на модели Microsoft Foundry и използват
  променливите на средата `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Обновени **`.env.copy`, `AGENTS.md` и документация за доставчиците**, за да отразят, че Azure OpenAI вече е част
  от Microsoft Foundry, и версията на API по подразбиране е повишена до `2024-10-21`.
- **TypeScript примери** (уроци 06, 07, 08, 11) мигрирани от остарелия бета SDK `@azure/openai`
  към пакета `openai` (чат приложенията използват Responses API; приложението за търсене използва
  клиента за embeddings).
- **.NET тетрадки** (`dotnet/*.dib`) стандартизирани на `Azure.AI.OpenAI` **2.1.0**: уроци 06 и 07
  използват API `ChatClient`, урок 08 използва `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), и
  урок 09 използва `ImageClient` (`GenerateImage`) с `gpt-image-1`, замествайки остарелите
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` от `1.0.0-beta.9`.
- Модернизация на имена на продукти: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (уроци 14, 16, 17) и "Bing" → **Microsoft Copilot** (урок 12), там където това се отнасяше до
  текущите продукти.
- **DevContainer** (`.devcontainer/`) вече включва разширенията Pylance, Black, Ruff, ESLint, Prettier и Copilot,
  активира форматиране при запис и инсталира `ruff`, `black`, `mypy` и `pytest`, за да могат проверките в CI
  да се възпроизведат локално.
- **Генериране на изображения** (урок 09) препоръчва `gpt-image-1` за Azure (каталогът на Azure премахна
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** обновен, за да отрази завършената работа (API миграция, CI,
  DevContainer, тестове) и актуалните факти (преводите се генерират автоматично от
  Azure Co-op Translator; Assistants API е заменен от Responses API).

### Отстранени грешки

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` сега връща
  празен низ за вход само с интервали вместо да хвърля грешка за "твърде кратко" (съответства на
  случая `None`). Открито и покрито с новата тестова колекция.
- Примерите за изображения в урок 09 — коригирани реални грешки: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  и променлива, която засенчваше модула `openai`.
- Раг тетрадката в урок 15 — поправена настройката на клиента, заменен премахнатия `DataFrame.append`
  с `pd.concat` и модернизирана употребата на остарелия SDK.
- Остарели / оттеглени имена на модели (`gpt-3.5-turbo`, `gpt-35-turbo`) заменени с `gpt-4o-mini`
  в активните примери; историческите резултати от фино настройване в урок 18 са запазени и анотирани
  вместо да бъдат пренаписани.

### Остарели / Бележки

- Примерите за Microsoft Foundry Models, които използват SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — например `githubmodels-*` и `js-githubmodels` и уроци 19, 20,
  и 21 — остават на Model Inference API, който **не** поддържа Responses API. Те са
  умишлено запазени на този SDK.
- `AzureOpenAI()` е умишлено запазен, където все още е подходящ (embeddings и генериране на изображения),
  защото тези работни потоци не са част от миграцията към Responses API.
- Запазени са препратки към `text-embedding-ada-002`, където предварително изчислен индекс от embedding зависи от тях.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->