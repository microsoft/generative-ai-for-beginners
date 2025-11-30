<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:12:07+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sr"
}
-->
# AGENTS.md

## Преглед пројекта

Овај репозиторијум садржи свеобухватан курикулум од 21 лекције који подучава основе генеративне вештачке интелигенције и развој апликација. Курс је намењен почетницима и покрива све, од основних концепата до изградње апликација спремних за производњу.

**Кључне технологије:**
- Python 3.9+ са библиотекама: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript са Node.js и библиотекама: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API и GitHub Models
- Jupyter Notebooks за интерактивно учење
- Dev Containers за конзистентно развојно окружење

**Структура репозиторијума:**
- 21 директоријум лекција са бројевима (00-21) који садрже README датотеке, примере кода и задатке
- Више имплементација: Python, TypeScript, а понекад и .NET примери
- Директоријум за преводе са верзијама на 40+ језика
- Централизована конфигурација преко `.env` датотеке (користите `.env.copy` као шаблон)

## Команде за подешавање

### Почетно подешавање репозиторијума

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Подешавање Python окружења

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Подешавање Node.js/TypeScript окружења

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Подешавање Dev Container-а (препоручено)

Репозиторијум укључује `.devcontainer` конфигурацију за GitHub Codespaces или VS Code Dev Containers:

1. Отворите репозиторијум у GitHub Codespaces или VS Code са Dev Containers екстензијом
2. Dev Container ће аутоматски:
   - Инсталирати Python зависности из `requirements.txt`
   - Покренути скрипту након креирања (`.devcontainer/post-create.sh`)
   - Подесити Jupyter kernel

## Радни ток развоја

### Променљиве окружења

Све лекције које захтевају приступ API-ју користе променљиве окружења дефинисане у `.env`:

- `OPENAI_API_KEY` - За OpenAI API
- `AZURE_OPENAI_API_KEY` - За Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL за Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT` - Назив модела за завршетак разговора
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Назив модела за уграђивање
- `AZURE_OPENAI_API_VERSION` - Верзија API-ја (подразумевано: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - За Hugging Face моделе
- `GITHUB_TOKEN` - За GitHub Models

### Покретање Python примера

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Покретање TypeScript примера

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Покретање Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Рад са различитим типовима лекција

- **Лекције "Learn"**: Фокусирају се на README.md документацију и концепте
- **Лекције "Build"**: Укључују радне примере кода у Python-у и TypeScript-у
- Свака лекција има README.md са теоријом, објашњењем кода и линковима ка видео садржају

## Упутства за стил кода

### Python

- Користите `python-dotenv` за управљање променљивама окружења
- Увозите `openai` библиотеку за интеракцију са API-јем
- Користите `pylint` за проверу кода (неки примери укључују `# pylint: disable=all` ради једноставности)
- Пратите PEP 8 конвенције именовања
- Чувајте API креденцијале у `.env` датотеци, никада у коду

### TypeScript

- Користите `dotenv` пакет за променљиве окружења
- Конфигурација TypeScript-а у `tsconfig.json` за сваку апликацију
- Користите `@azure/openai` или `@azure-rest/ai-inference` за Azure услуге
- Користите `nodemon` за развој са аутоматским поновним учитавањем
- Компилирајте пре покретања: `npm run build` затим `npm start`

### Опште конвенције

- Држите примере кода једноставним и едукативним
- Укључите коментаре који објашњавају кључне концепте
- Код сваке лекције треба да буде самосталан и извршив
- Користите конзистентно именовање: `aoai-` префикс за Azure OpenAI, `oai-` за OpenAI API, `githubmodels-` за GitHub Models

## Упутства за документацију

### Стил Markdown-а

- Сви URL-ови морају бити у формату `[текст](../../url)` без додатних размака
- Релативни линкови морају почети са `./` или `../`
- Сви линкови ка Microsoft доменима морају укључити ID за праћење: `?WT.mc_id=academic-105485-koreyst`
- Без локалних поставки специфичних за земљу у URL-овима (избегавајте `/en-us/`)
- Слике се чувају у директоријуму `./images` са описним именима
- Користите енглеске карактере, бројеве и цртице у именима датотека

### Подршка за превод

- Репозиторијум подржава 40+ језика преко аутоматизованих GitHub Actions
- Преводи се чувају у директоријуму `translations/`
- Не подносите делимичне преводе
- Машински преводи нису прихваћени
- Преведене слике се чувају у директоријуму `translated_images/`

## Тестирање и валидација

### Провере пре подношења

Овај репозиторијум користи GitHub Actions за валидацију. Пре подношења PR-ова:

1. **Проверите Markdown линкове**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Ручно тестирање**:
   - Тестирајте Python примере: Активирајте venv и покрените скрипте
   - Тестирајте TypeScript примере: `npm install`, `npm run build`, `npm start`
   - Проверите да ли су променљиве окружења правилно конфигурисане
   - Проверите да ли API кључеви раде са примерима кода

3. **Примери кода**:
   - Уверите се да се сав код извршава без грешака
   - Тестирајте са Azure OpenAI и OpenAI API где је применљиво
   - Проверите да примери раде са GitHub Models где је подржано

### Без аутоматизованих тестова

Ово је едукативни репозиторијум фокусиран на туторијале и примере. Не постоје јединични или интеграциони тестови за покретање. Валидација је углавном:
- Ручно тестирање примера кода
- GitHub Actions за валидацију Markdown-а
- Преглед образовног садржаја од стране заједнице

## Упутства за Pull Request

### Пре подношења

1. Тестирајте измене кода у Python-у и TypeScript-у где је применљиво
2. Покрените валидацију Markdown-а (аутоматски се покреће на PR)
3. Уверите се да су ID-ови за праћење присутни на свим Microsoft URL-овима
4. Проверите да су релативни линкови валидни
5. Проверите да су слике правилно референциране

### Формат наслова PR-а

- Користите описне наслове: `[Lesson 06] Fix Python example typo` или `Update README for lesson 08`
- Референцирајте бројеве проблема где је применљиво: `Fixes #123`

### Опис PR-а

- Објасните шта је промењено и зашто
- Линкујте повезане проблеме
- За измене кода, наведите који примери су тестирани
- За PR-ове превода, укључите све датотеке за комплетан превод

### Захтеви за допринос

- Потпишите Microsoft CLA (аутоматски на првом PR-у)
- Форкујте репозиторијум на свој налог пре прављења измена
- Један PR по логичној промени (не комбинујте неповезане исправке)
- Држите PR-ове фокусиране и мале кад год је могуће

## Уобичајени радни токови

### Додавање новог примера кода

1. Идите у одговарајући директоријум лекције
2. Креирајте пример у `python/` или `typescript/` поддиректоријуму
3. Пратите конвенцију именовања: `{provider}-{example-name}.{py|ts|js}`
4. Тестирајте са стварним API креденцијалима
5. Документујте све нове променљиве окружења у README лекције

### Ажурирање документације

1. Уредите README.md у директоријуму лекције
2. Пратите упутства за Markdown (ID-ови за праћење, релативни линкови)
3. Ажурирање превода се обрађује преко GitHub Actions (не уређујте ручно)
4. Тестирајте да су сви линкови валидни

### Рад са Dev Containers

1. Репозиторијум укључује `.devcontainer/devcontainer.json`
2. Скрипта након креирања аутоматски инсталира Python зависности
3. Екстензије за Python и Jupyter су унапред конфигурисане
4. Окружење се базира на `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Деплојмент и објављивање

Ово је репозиторијум за учење - не постоји процес деплојмента. Курикулум се користи преко:

1. **GitHub репозиторијума**: Директан приступ коду и документацији
2. **GitHub Codespaces**: Инстант развојно окружење са унапред конфигурисаним подешавањем
3. **Microsoft Learn**: Садржај може бити синдициран на званичну платформу за учење
4. **docsify**: Сајт документације изграђен из Markdown-а (погледајте `docsifytopdf.js` и `package.json`)

### Изградња сајта документације

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Решавање проблема

### Уобичајени проблеми

**Грешке при увозу Python-а**:
- Уверите се да је виртуелно окружење активирано
- Покрените `pip install -r requirements.txt`
- Проверите да је верзија Python-а 3.9+

**Грешке при компилацији TypeScript-а**:
- Покрените `npm install` у одређеном директоријуму апликације
- Проверите да је верзија Node.js компатибилна
- Очистите `node_modules` и поново инсталирајте ако је потребно

**Грешке при аутентификацији API-ја**:
- Проверите да `.env` датотека постоји и има исправне вредности
- Проверите да ли су API кључеви валидни и нису истекли
- Уверите се да су URL-ови endpoint-а исправни за ваш регион

**Недостају променљиве окружења**:
- Копирајте `.env.copy` у `.env`
- Попуните све потребне вредности за лекцију на којој радите
- Поново покрените апликацију након ажурирања `.env`

## Додатни ресурси

- [Водич за подешавање курса](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Упутства за допринос](./CONTRIBUTING.md)
- [Кодекс понашања](./CODE_OF_CONDUCT.md)
- [Политика безбедности](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Збирка напредних примера кода](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Напомене специфичне за пројекат

- Ово је **образовни репозиторијум** фокусиран на учење, а не на производни код
- Примери су намерно једноставни и фокусирани на подучавање концепата
- Квалитет кода је уравнотежен са образовном јасноћом
- Свака лекција је самостална и може се завршити независно
- Репозиторијум подржава више API провајдера: Azure OpenAI, OpenAI и GitHub Models
- Садржај је вишејезичан са аутоматизованим радним токовима за превод
- Активна заједница на Discord-у за питања и подршку

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.