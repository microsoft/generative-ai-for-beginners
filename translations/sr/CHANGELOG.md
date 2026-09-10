# Промене

Све значајне измене у наставном плану за Генеративну вештачку интелигенцију за почетнике су документиране у овом фајлу.

Формат је заснован на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Пошто је ово
наставни план, а не верзионисани софтверски пакет, записи су груписани по датуму.

## [2026-07-16] — Валидација садржаја + сликовни материјали за лекцију 09

### Измењено

- **Лекција 10 (апликације са мало кода и АИ):** ажуриране су две пензионисане везе `docs.microsoft.com/powerapps/...` за Dataverse
  на тренутну `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (проверавано уживо).
- **Лекција 17 (АИ агенти):** модернизован је застарели пример модела (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, и Llama 3.3`) и име примерка поставке у Agent Framework примеру
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Коренски README.md:** додат је недостајући ID праћења `?WT.mc_id=academic-105485-koreyst` у
  вези *Microsoft for Startups*.
- **Сликовни материјали за лекцију 09** поново генерисани моделом `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, и
  `images/startup.png` (пар пре/после у примеру уређивања је направљен позивом из стварног
  `client.images.edit` са генерисаном маском).

### Верификовано

- Ревидирани су README фајлови за лекције 01, 03, 05, 12, 14, и 16 — сви су тренутни (исправно име Microsoft Foundry
  и везе); није било потребе за изменама.
- Покренута је потпуна провера markdown фајлова (преводи искључени) међу свих 41 markdown фајлом у репозиторијуму
  ради застарелих путања у документацији, `/en-us/` Microsoft локација, застарелих имења производа/модела, недостајућих ID-јева за праћење,
  и покварених релативних веза/слика. Једини уочени проблем је била једна рупа у ID-ју за праћење *Microsoft for Startups*;
  све друге означене ствари показале су се као лажно позитивне (аутоматски генерисане везе за превод,
  коментарисани плейсхолдери и треће стране `/en/` структурне URL адресе).

## [2026-07-15] — Писање лекције 09 (сликовне апликације) за GPT Image моделе

### Измењено

- **Преобликована лекција 09 "Прављење апликација за генерисање слика"** око актуелне **`gpt-image`**
  породице модела (подразумевани је **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` су такође GA), замењујући
  застарели DALL·E 2/3 садржај. Кључне исправке:
  - `gpt-image` модели враћају слику као **base64 (`b64_json`)**, а не URL. Ажурирани су сви примери да користе
    `base64.b64decode(...)` уместо преузимања `url` са `requests`.
  - Подигнута верзија APIја за слике на `2025-04-01-preview`.
  - Замена измисленог дела "temperature" (сликовни модели не користе `temperature`) и DALL·E-2 само садржаја слика
    **варијације** са одељком о **уређивању слика** (маска/инпеинтинг).
  - Ажурирани су `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, оба
    assignment notebook-а (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), и .NET `.dib` notebook.

### Уклоњено

- Обрисани застарели примери `python/aoai-app-variation.py` и `python/oai-app-variation.py`
  (`images.create_variation` је DALL·E-2 само и није подржан од стране `gpt-image`).
- Уклоњене 4 слике које се више не користе, везане за уклоњени одељак о поређењу temperature
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Уклоњена непотребна зависност `requests` из Python примера у лекцији и њених dependency фајлова.

### Верификовано

- Покренут `aoai-app.py` од почетка до краја против деплојованог модела `gpt-image-1.5` и потврђено да процедура
  декодирања/снимања base64 резултира у PNG фајлу. Notebook-ови су потврђени да су валидан JSON.

## [2026-07-14] — Подразумевани модел ажурман + Упутства за reasoning модел

### Измењено

- **Подразумевани chat модел `gpt-4o-mini` → `gpt-5-mini`** у свим извршним примерима у наставном плану,
  документацији и конфигурацији. Ова промена је покренута статусом животног циклуса модела: на Microsoft Foundry,
  `gpt-4o-mini` (пензионише се 2026-10-01) и цела породицу `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, пензионишу се 2026-10-14) су **застаревајући**, док је **породица GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) опште доступна** (пензионише се 2027-02-06). Ажурирано:
  - `.env.copy`, `00-course-setup/03-providers.md` (препоручене команде за деплојмент и `az cognitiveservices`
    deploy), и README фајлови за лекције 04, 06, 07, и 15.
  - Python примери у лекцији 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) и скриптама из лекције 08.
  - TypeScript / JavaScript примери у лекцијама 06, 07 и 11, и `.dib` .NET notebook-ови за
    лекције 06 и 07.
  - Assignment notebook-ови у лекцијама 04, 06, 07 и 11 (код ћелије), као и `shared/python/api_utils.py`
    примери у docstring-у.
- **Упутства за параметре reasoning-модела (ново).** `gpt-5-mini` је *reasoning* модел: он не подржава
  `temperature`/`top_p`, и уместо `max_tokens` користи `max_completion_tokens` (chat претпоставке) /
  `max_output_tokens` (Responses API). Према томе:

  - Уклоњени `temperature`/`top_p`/`max_tokens` из примера који сада подразумевано користе `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, лекција 15 RAG README).
  - Додата белешка **"Разлози зашто модели за расуђивање не користе `temperature`"** у лекцију 06, која објашњава да
    се модели за расуђивање усмеравају помоћу **prompt инжењеринга + контрола расуђивања** уместо
    ручки за узорковање, док `temperature`/`top_p` остају валидни за немоделе за расуђивање
    (GPT-4.x, Mistral, Llama, Phi, отворени модели).
- **`gpt-5-mini` се не користи у туторијалу за фина подешавања (лекција 18).** GPT-5 подржава само
  појачано фино подешавање (RFT); туторијал за надгледано фино подешавање (SFT) у лекцији 18 задржава
  `gpt-4.1-mini`, који подржава SFT/DPO.
- **Демо пример за Temperature користи Llama модел.** Да би се наставило обучавање `temperature` (којег модели за расуђивање
  одбацују), користи се модел `Llama-3.3-70B-Instruct` преко Foundry Models endpoint-а. Додата је нова
  променљива `AZURE_INFERENCE_CHAT_MODEL` у `.env.copy`; lekcije 04/06 `githubmodels` notebook-ови и
  `06` пример `js-githubmodels` је читају (са резервом на `Llama-3.3-70B-Instruct`) и задржавају своје
  демо примере за `temperature`/`top_p`/`max_tokens`.
- **JS / .NET примери ажурирани за GPT-5.** Уклоњени `temperature`/`top_p`/`max_tokens` из GPT-5
  примера (`06` `recipe-app` TypeScript, `06` `.dib` .NET - који такође повећава `MaxOutputTokenCount`
  како се излаз расуђивања не би скраћивао). `06` `js-githubmodels` пример сада користи Llama за своје
  temperature демо. `.dib` примећује да је `Azure.AI.Inference` + Llama модел начин
  за демонстрацију `Temperature` у .NET-у.
- Задржани `gpt-4o-mini` / `gpt-5-mini` на местима где су и даље прецизни: референце за кодирање тиковa у `tiktoken`,
  листе доступности модела у каталогу и говорни модели из лекције 02 (`gpt-4o-transcribe`).
- Лекције 20 (Mistral) и 21 (Meta) примери задржавају `temperature`/`max_tokens` јер циљају
  Mistral/Llama моделе који подржавају те параметре.

## [2026-07-06] — Освежавање модернизације садржаја

Општи освежавајући корак да би се наставни план и програм одржавао прецизним за 2026: модерни API-ји, актуелна имена производа и
имена модела, ажуриране смернице за провајдере и нови алати за побољшање искуства програмера.

### Додато

- Секција **Microsoft Agent Framework** у лекцији `17-ai-agents` која покрива једноструке чат агенте,
  позиве алата/функција, Azure OpenAI (Microsoft Foundry) конфигурацију и оркестрацију више агената
  ток рада (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** документован као офлајн / на уређају провајдер (уз Ollama) у
  `00-course-setup/03-providers.md` и лекцији `19-slm`.
- **Континуирани интеграциони токови рада**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (примењено на одржавани `shared/`
    модул, саветодавно у целој осталој настави), ESLint проследна провера и pytest задатак.
  - `.github/workflows/security.yml` — CodeQL анализа (Python + JavaScript/TypeScript) и
    преглед зависности на pull захтевима.
- **Тестни скуп** под `tests/` — 41 pytest тест који покрива заједнички услужни модул.
- **Вештина миграције од Azure OpenAI на Responses API** под
  `.github/skills/azure-openai-to-responses/` коришћена за вођење миграције API-ја.

### Промењено

- **Chat Completions API → Responses API** у свим Python и TypeScript chat примерима
  (`client.responses.create(...)` → `response.output_text`), укључујући лекције 04, 06, 07, 11,
  15 и 18, плус њихове README-ове.
- **GitHub Models → Microsoft Foundry Models** у целом тексту, линковима и примерима. GitHub Models
  се повлачи крајем јула 2026; примери сада указују на Microsoft Foundry модел каталог и користе
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` променљиве окружења.
- **`.env.copy`, `AGENTS.md`, и документација провајдера** ажурирани да одразе да је Azure OpenAI сада део
  Microsoft Foundry, и подразумевана верзија API-ја увећана на `2024-10-21`.
- **TypeScript примери** (лекције 06, 07, 08, 11) мигрирани са застарелог `@azure/openai`
  бета SDK на `openai` пакет (чат апликације користе Responses API; апликација за претрагу користи
  embeddings клијент).
- **.NET notebook-ови** (`dotnet/*.dib`) стандартизовани на `Azure.AI.OpenAI` **2.1.0**: лекције 06 и 07
  користе `ChatClient` API, лекција 08 користи `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), и
  лекција 09 користи `ImageClient` (`GenerateImage`) са `gpt-image-1`, замењујући стару
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` из `1.0.0-beta.9`.
- **Модернизација имена производа**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (лекције 14, 16, 17) и "Bing" → **Microsoft Copilot** (лекција 12), када су се односили на
  тренутне производе.
- **DevContainer** (`.devcontainer/`) сада укључује Pylance, Black, Ruff, ESLint, Prettier и Copilot
  екстензије, омогућава формат-он-саве и инсталира `ruff`, `black`, `mypy` и `pytest` како би
  CI провере могле да се репродукују локално.
- **Генерација слика** (лекција 09) препоручује `gpt-image-1` за Azure (Azure каталог је уклонио
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ажуриран да одражава завршени рад (миграција API-ја, CI,
  DevContainer, тестови) и тренутне чињенице (преводи се аутоматски производе помоћу
  Azure Co-op Translator; Assistants API је замењен Responses API-јем).

### Исправљено

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` сада враћа
  празан низ за унос који садржи само размаке уместо да баца грешку "превише кратак" (усклађено са
  случајем `None`). Пронађено и покривено новим скупом тестова.
- **Примери слика из Лекције 09** — исправљене стварне грешке: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  и променљива која је засенчила модул `openai`.
- **Лекција 15 RAG нотебоок** — поправљена конфигурација клијента, замењен уклоњени `DataFrame.append`
  са `pd.concat`, и модернизована употреба застарелог SDK-а.
- Застарели / повучени називи модела (`gpt-3.5-turbo`, `gpt-35-turbo`) замењени са `gpt-4o-mini`
  у активним примерима; излаз финог подешавања из лекције 18 сачуван и означен
  уместо преписан.

### Застарело / Напомене

- **Примери Microsoft Foundry модела** који користе `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — узорци `githubmodels-*` и `js-githubmodels` и лекције 19, 20,
  и 21 — остају на Model Inference API-ју, који **не** подржава Responses API. Они су
  намерно остављени на том SDK-у.
- `AzureOpenAI()` је намерно задржан тамо где је још увек прикладан (за уграђивања и генерисање слика),
  јер ти токови рада нису део миграције на Responses API.
- Референце на `text-embedding-ada-002` су сачуване тамо где се ослањају на предрачунски индекс уграђивања.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->