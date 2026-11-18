# កំណត់ហេតុបម្លែង

ការផ្លាស់ប្តូរទាំងអស់ដែលគួរឱ្យចាប់អារម្មណ៍ចំពោះមេរៀន AI បង្កើតសម្រាប់អ្នកចាប់ផ្តើមត្រូវបានរាយនាមនៅក្នុងឯកសារ​នេះ។

រចនាសម្ព័ន្ធតាមគោលការណ៍ [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)។ ដូចដែលនេះគឺជា
មេរៀនសម្រាប់ការសិក្សាមិនមែនជាកញ្ចប់កម្មវិធីដែលមានកំណែចេញផ្សាយទេ អ្នករាយនាមត្រូវបានចែកតាមថ្ងៃខែឆ្នាំ។

## [2026-07-16] — ការបញ្ជាក់មាតិកា + ទ្រព្យសកម្មរូបភាពមេរៀនទី 09

### បានផ្លាស់ប្តូរ

- **មេរៀនទី ១០ (កម្មវិធី AI ដោយកូដទាប):** បានធ្វើបច្ចុប្បន្នភាពតំណខ្សែពីរ `docs.microsoft.com/powerapps/...` Dataverse ដែលបានផ្អាក
  ទៅកាន់ `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` បច្ចុប្បន្ន
  (បានបញ្ជាក់ថាសកម្ម)។
- **មេរៀនទី ១៧ (ភាសាង AI):** បានធ្វើឱ្យទំនើបនូវគំរូដែលចាស់ (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) និងឈ្មោះដាក់ទីតាំងបញ្ចូនអ្នកលក់នៅក្នុងគំរូ Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`)។
- **រស្មី `README.md`:** បានបន្ថែមលេខសម្គាល់តាមដាន `?WT.mc_id=academic-105485-koreyst` ដែលខ្វះទៅនៅ
  តំណភ្ជាប់ *Microsoft for Startups* ។
- **ទ្រព្យសម្បត្តិតស៊ូរូបភាពមេរៀនទី ០៩** បានបង្កើតឡើងវិញជាមួយម៉ូឌែល `gpt-image`៖ `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, និង
  `images/startup.png` (គូរឧទាហរណ៍ការកែសម្រួលមុន/ក្រោយត្រូវបានផលិតតាមរយៈការហៅចំឡើយ
  `client.images.edit` ជាមួយនឹងម៉ាស់ដែលបង្កើតขึ้น)។

### បានឆ្លងកាត់ការត្រួតពិនិត្យ

- ត្រួតពិនិត្យ READMEs សម្រាប់មេរៀន ០១, ០៣, ០៥, ១២, ១៤, និង ១៦ — ទាំងអស់គ្នាសព្វថ្ងៃ (ឈ្មោះ និងតំណ Microsoft Foundry ត្រឹមត្រូវ);
  មិនចាំបាច់ធ្វើបម្លែងអ្វីទេ។
- បើកដំណើរការត្រួតពិនិត្យ markdown ពេញលេញទាំង ៤១ ឯកសារ markdown នៅក្នុង仓庫 (មិនរាប់បញ្ចូលការប្រែសម្រួល) សម្រាប់
  តំបneal ឯកសារដែលចាស់, `/en-us/` តំបន់ Microsoft, ឈ្មោះផលិតផល/ម៉ូដែលចាស់, លំដាប់តាមដានខ្វះ,
  លេខសម្គាល់, និងតំណរភ្ជាប់/រូបភាពទាក់ទងខូច។ មានតែចន្លោះលេខសម្គាល់តាមដាន *Microsoft for Startups* មួយគត់ដែលអាច
  ប្រតិបត្តិការបាន; ទង់ភ្លើងផ្សេងទៀតទាំងអស់ត្រូវបានបញ្ជាក់ថាជាករណីប៉ុន្មានបញ្ច្រាស់ទេ (តំណភ្ជាប់បកប្រែដែលផលិតដោយស្វ័យប្រវត្តិ,
  កន្លែងដាក់ពាក្យសុំដែលបានយកចេញ, និងតំណរទំព័រចេញពី `/en/` ផ្នែករចនាសម្ព័ន្ធភាគីទីបី)។

## [2026-07-15] — មេរៀនទី 09 (កម្មវិធីរូបភាព) ការសរសេរថ្មីសម្រាប់ម៉ូដែលរូបភាព GPT

### ប្រែប្រួល

- **បានសរសេរថ្មីមេរៀនទី 09 "ការបង្កើតកម្មវិធីបង្កើតរូបភាព"** ជុំវិញ **`gpt-image`**  
  គ្រួសារ ម៉ូដែលបច្ចុប្បន្ន (លំនាំដើម **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ក៏បានជាផ្លូវការដែរ), ជំនួស  
  សមាសភាគ DALL·E 2/3 ដែលចាស់។ ការកែលម្អសំខាន់ៗ៖  
  - ម៉ូដែល `gpt-image` ផ្ទេររូបភាពជាទ្រង់ទ្រាយ **base64 (`b64_json`)** មិនមែនជាURLទេ។ បានធ្វើបច្ចុប្បន្នភាពគំរូទាំងអស់ទៅ  
    `base64.b64decode(...)` ជំនួសការទាញយក `url` ជាមួយ `requests`។  
  - បានលើកកំណែ API រូបភាពទៅកាន់ `2025-04-01-preview`។  
  - បានជំនួសផ្នែក "សម្ពាធ" ដែលបង្កើតឡើង (ម៉ូដែលរូបភាពមិនទទួល `temperature` ទេ) និង   
    មាតិកា **ការបម្រែលខុសគ្នារូបភាព** សម្រាប់ DALL·E-2 ដោយផ្នែក **កែសម្រួលរូបភាព** (mask/inpainting)។  
  - បានបច្ចុប្បន្នភាព `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ទាំង    ​  
    សៀវភៅកំណត់ត្រាចាត់តាំង (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),  
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), និងសៀវភៅកំណត់ត្រា .NET `.dib`។  

### លុបចោល

- លុបតំរូវការគំរូ `python/aoai-app-variation.py` និង `python/oai-app-variation.py` ដែលចាស់
  (`images.create_variation` គឺសម្រាប់ DALL·E-2 ប៉ុណ្ណោះ ហើយមិនគាំទ្រដោយ `gpt-image`)។
- លុបអចលនទ្រព្យរូបភាពចំនួន 4 ដែលខូចខាតដែលភ្ជាប់ទៅកាន់ផ្នែកបញ្ចៀសសីតុណ្ហភាពដែលបានលុប
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`)។
- ដក dependency `requests` ដែលមិនចាំបាច់ចេញពីគំរូ Python និងតម្រូវការបង្រៀន។

### បានផ្ទៀងផ្ទាត់

- រាការត្រួតពិនិត្យ `aoai-app.py` ពីដើមទៅចប់ទល់នឹងគំរូ `gpt-image-1.5` ដែលបានដាក់ចេញ ហើយបញ្ជាក់ថាប្រតិបត្តិការរុំតួ BASE64 និងរក្សាទុកផលិតរូបភាព PNG ត្រូវបានអនុវត្ត។ សៀវភៅសម្គាល់ត្រូវបានផ្ទៀងផ្ទាត់ថាជា JSON ត្រឹមត្រូវ។






- **ម៉ូដែលជជែកលំនាំដើម `gpt-4o-mini` → `gpt-5-mini`** ក្នុងគំរូដែលអាចដំណើរការបានទូទាំងមូល,
  ឯកសារ និងការកំណត់រចនាសម្ព័ន្ធ។ នេះនៅក្នុងបំណងពីស្ថានភាពជីវិតម៉ូដែល៖ នៅលើ Microsoft Foundry,
  `gpt-4o-mini` (នឹងចាកចេញនៅថ្ងៃទី ២០២៦-១០-០១) និងគ្រួសារ `gpt-4.1` ទាំងមូល (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, នឹងចាកចេញនៅថ្ងៃទី ២០២៦-១០-១៤) គឺ **កំពុងត្រូវបានរំលង**, ខណៈដែលក្រុម **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) គឺអាចប្រើបានទូទៅ** (នឹងចាកចេញនៅ ២០២៧-០២-០៦)។ បានធ្វើបច្ចុប្បន្នភាព៖
  - `.env.copy`, `00-course-setup/03-providers.md` (ការត្រូវបានណែនាំឱ្យប្រើ និងពាក្យបញ្ជា `az cognitiveservices`
    ដាក់ចេញ), និងឯកសារ README សម្រាប់មេរៀនលេខ ០៤, ០៦, ០៧, និង ១៥។
  - គំរូ Python នៅមេរៀន ០៦ (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) និង script មេរៀន ០៨។
  - គំរូ TypeScript / JavaScript នៅមេរៀន ០៦, ០៧, និង ១១ និងកំណត់ត្រា `.dib` .NET សម្រាប់
    មេរៀន ០៦ និង ០៧។
  - កំណត់ត្រាការងារជាកម្មវិធីនៅមេរៀន ០៤, ០៦, ០៧, និង ១១ (កូដសែល) បូកបន្ថែមទៅឧទាហរណ៍ docstring `shared/python/api_utils.py`។

- **ការណែនាំអំពីប៉ារ៉ាម៉ែត្រម៉ូដែលការយល់ឃើញ (ថ្មី).** `gpt-5-mini` ជា ម៉ូដែល *ការយល់ឃើញ*៖ វា **មិន**
  គាំទ្រ `temperature`/`top_p` និងប្រើ `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) ជំនួស `max_tokens`។ ដូច្នេះ៖
  - បានដក `temperature`/`top_p`/`max_tokens` ចេញពីគំរូដែលឥឡូវនេះមានលំនាំដើមទៅ `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README RAG មេរៀន ១៥)។
  - បានបន្ថែមកំណត់សម្គាល់ **"ម៉ូដែលហែកិច្ចមិនប្រើ `temperature`"** ទៅមេរៀន 06 ដែលពិពណ៌នាថា
    ម៉ូដែលហែកិច្ចត្រូវបានគ្រប់គ្រងដោយ **វិស្វកម្មការផ្ដល់ដំណើរការ + ការត្រួតពិនិត្យហែកិច្ច** ជាង
    កុងតាក់សំណុំឆ្នោត ខណៈដែល `temperature`/`top_p` នៅតែមានសុពលភាពលើម៉ូដែលមិនមែនហែកិច្ច
    (GPT-4.x, Mistral, Llama, Phi, ម៉ូដែលបើកចំហ)។
- **`gpt-5-mini` មិនត្រូវបានប្រើសម្រាប់មេរៀនបំលែងលម្អ (lessson 18) ទេ។** GPT-5 គាំទ្រតែ
  ការបំលែងលម្អដោយការបន្តផ្សារជំនួយ (RFT); មេរៀន 18 សម្រាប់ការបំលែងលម្អក្រោមការត្រួតពិនិត្យ (SFT) កាន់តែរក្សា
  `gpt-4.1-mini` ដែលគាំទ្រការបំលែងលម្អ SFT/DPO។
- **ការបង្ហាញអំពីសីតុណ្ហភាពប្រើម៉ូដែល Llama។** ដើម្បីបន្តបង្រៀន `temperature` (ដែលម៉ូដែលហេតុផល
  បដិសេធ), ម៉ូដែល `Llama-3.3-70B-Instruct` ត្រូវបានប្រើតាមរយៈចំណុចប្រទាក់ Foundry Models។ បានបន្ថែម
  អថេរ `AZURE_INFERENCE_CHAT_MODEL` ថ្មីមួយទៅកាន់ `.env.copy`; សៀវភៅកំណត់ត្រា 04/06 `githubmodels` និង
  គំរូ `06` `js-githubmodels` បានអានវា (ត្រឡប់ទៅកាន់ `Llama-3.3-70B-Instruct`) ហើយរក្សាទុក
  ការបង្ហាញ `temperature`/`top_p`/`max_tokens` របស់ពួកគេ។
- **គំរូ JS / .NET បានអាប់ដេតសម្រាប់ GPT-5។** បានយកចេញ `temperature`/`top_p`/`max_tokens` ពី GPT-5
  ឧទាហរណ៍ (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ដែលក៏បង្កើតឡើង `MaxOutputTokenCount`
  ដូច្នេះការចេញម៉តិយោបល់មិនត្រូវបានកាត់បន្ថយទេ)។ ឧទាហរណ៍ `06` `js-githubmodels` ឥឡូវនេះប្រើ Llama ដើម្បីរក្សា
  ផង្ហាញសីតុណ្ហភាព។ `.dib` គួរបញ្ជាក់ថា `Azure.AI.Inference` + ម៉ូដែល Llama គឺជាវិធីសម្រាប់
  បង្ហាញ `Temperature` នៅក្នុង .NET។
- ប្រុង `gpt-4o-mini` / `gpt-5-mini` នៅកន្លែងដែលវានៅត្រឹមត្រូវ: `tiktoken` ការជម្រះសញ្ញា token-encoding
  យោង, បញ្ជីប្រើប្រាស់ម៉ូដែលប្រភេទកាតាឡុក, និងម៉ូដែលសំលេងមេរៀន 02 (`gpt-4o-transcribe`)។
- សំណំមេរៀន 20 (Mistral) និង 21 (Meta) រក្សា `temperature`/`max_tokens` ដោយសារតែពួកវាគោលដៅលើ
  ម៉ូដែល Mistral/Llama ដែលគាំទ្រព៉ារ៉ាមែតេស្តទាំងនោះ។

## [2026-07-06] — ពិនិត្យឡើងវិញនូវការអភិវឌ្ឍមុខម៉ាតខ្លឹមវត្ថុ

ការបន្ទាន់សម័យយ៉ាងទូលំទូលាយ ដើម្បីរក្សាឲ្យមុខវិជ្ជាសិក្សាមានភាពត្រឹមត្រូវសម្រាប់ឆ្នាំ ២០២៦ៈ API ទំនើប ឈ្មោះផលិតផលបច្ចុប្បន្ន និង
ឈ្មោះគំរូបច្ចុប្បន្ន ការណែនាំអ្នកផ្គត់ផ្គង់បានធ្វើបច្ចុប្បន្នភាព និងឧបករណ៍ធ្វើតេស្តបទពិសោធន៍អ្នកអភិវឌ្ឍន៍ថ្មី។

### បានបន្ថែម

- ផ្នែក **Microsoft Agent Framework** ក្នុងមេរៀន `17-ai-agents` ដែលគ្របដណ្តប់ដល់ភាសាចតឯកជនមួយ,
  ឧបករណ៍/ការហៅមុខងារ, ការកំណត់ Azure OpenAI (Microsoft Foundry), និងភាសាចតច្រើន
  ការត្រួតពិនិត្យដំណើរការងារ (`SequentialBuilder` / `ConcurrentBuilder`)។
- **Foundry Local** បានឯកសារជាអ្នកផ្តល់សេវាប្រើក្រៅបណ្ដាញ / លើឧបករណ៍ (ជាមួយ Ollama) ក្នុង
  `00-course-setup/03-providers.md` និងមេរៀន `19-slm`។
- **ដំណើរការងាររួមបញ្ចូលជាបន្ត**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (បានអនុវត្តនៅលើ `shared/` ដែលបានរក្សាទុក module,
    សូមប្រឹក្សានៅលើវគ្គសិក្សាដទៃទៀត), ការបញ្ជូន ESLint សម្រាប់ប្រឹក្សា, និងការងារ pytest។
  - `.github/workflows/security.yml` — ការវិភាគ CodeQL (Python + JavaScript/TypeScript) និង
    ការពិនិត្យផ្នែកអាសយដ្ឋានលើ pull requests។
- **Test suite** នៅក្រោម `tests/` — 41 ការប្រឡង pytest ដែលគ្របដណ្តប់លើ module សេវាភាពរួម។
- **Azure OpenAI → Responses API migration skill** នៅក្រោម
  `.github/skills/azure-openai-to-responses/` ដែលបានប្រើដើម្បីណែនាំការផ្លាស់ប្ដូរ API។

### មានការផ្លាស់ប្ដូរ

- **Chat Completions API → Responses API** នៅក្នុងគំរូសន្ទនាទាំងអស់ Python និង TypeScript
  (`client.responses.create(...)` → `response.output_text`), រួមទាំងមេរៀន 04, 06, 07, 11, 
  15, និង 18 ជា​និង README របស់ពួកវា។
- **GitHub Models → Microsoft Foundry Models** នៅពេលហើយ, តំណភ្ជាប់ និងគំរូ។ GitHub Models
  នឹងបិទនៅចុងខែកក្កដា ឆ្នាំ 2026; គំរូឥឡូវនេះបង្ហាញទៅសៀវភៅម៉ូដែល Microsoft Foundry និងប្រើ
  អថេរបរិស្ថាន `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`។
- **`.env.copy`, `AGENTS.md`, និងឯកសារផ្ដល់សេវា** បានធ្វើបច្ចុប្បន្នភាពដើម្បីបញ្ជាក់ថា Azure OpenAI ឥឡូវនេះជាផ្នែក
  នៃ Microsoft Foundry និងកំណែ API ទំនុះបានបន្ថែមទៅ `2024-10-21`។
- **គំរូ TypeScript** (មេរៀន 06, 07, 08, 11) ផ្លាស់ប្ដូរចេញពីផ្សារទំនើបនៃ  `@azure/openai`
  beta SDK ទៅកញ្ចប់ `openai` (កម្មវិធីchat ប្រើ Responses API; កម្មវិធីស្វែងរកប្រើ
  កម្មវិធីភ្ញៀវ embeddings)។
- **ណូតប៊ុក .NET** (`dotnet/*.dib`) ត្រូវបានស្តង់ដារនៅលើ `Azure.AI.OpenAI` **2.1.0**: មេរៀន 06 និង 07
  ប្រើ API `ChatClient`, មេរៀន 08 ប្រើ `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), និង
  មេរៀន 09 ប្រើ `ImageClient` (`GenerateImage`) ជាមួយ `gpt-image-1` ជំនួសចាស់
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` ពី `1.0.0-beta.9`។
- **ការទំនើបភាពឈ្មោះផលិតផល**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (មេរៀន 14, 16, 17) និង "Bing" → **Microsoft Copilot** (មេរៀន 12), នៅទីនោះដែលបានយោង
  ផលិតផលបច្ចុប្បន្ន។
- **DevContainer** (`.devcontainer/`) ឥឡូវនេះផ្ដល់ជូននូវផ្នែកបន្ថែម Pylance, Black, Ruff, ESLint, Prettier, និង Copilot
  អនុញ្ញាតឲ្យបំលែងតាមពេលរក្សាទុក និងដំឡើង `ruff`, `black`, `mypy`, និង `pytest` ដើម្បីឲ្យ
  ការត្រួតពិនិត្យ CI អាចបង្កើតឡើងវិញតាមមូលដ្ឋានក្នុងតំបន់។
- **ការបង្កើតរូបភាព** (មេរៀន 09) ស្នើឱ្យប្រើប្រាស់ `gpt-image-1` សម្រាប់ Azure (каталог Azure បានដក
  `dall-e-3`)។
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** បានអាប់ដេត ដើម្បីបញ្ចេញការងារដែលបានបញ្ចប់ (ការផ្លាស់ប្តូរ API, CI,
  DevContainer, ការប្រឡង) និងការពិតបច្ចុប្បន្ន (ការបកប្រែត្រូវបានផលិតដោយស្វ័យប្រវត្តិ ដោយ
  Azure Co-op Translator; API អ្នកជំនួយត្រូវបានជំនួសដោយ API ចម្លើយ)។

### ដោះស្រាយ

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ឥឡូវនេះត្រឡប់មកវិញជា
  ខ្សែអក្សរទទេសម្រាប់ការបញ្ចូលមានតែចន្លោះទត្តដើម្បីជំនួសកំហុស "ខ្លីពេក" (ស្របទៅនឹង
  ករណី `None`) ត្រូវបានរកឃើញ និងគ្របដណ្ដប់ដោយសំណួរប្រឡងថ្មី។
- **គំរូរូបភាពមេរៀន 09** — បានកែលម្អកំហុសពិតៗ៖ `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  និងអថេរមួយដែលស្របត្រង់ទៅលើម៉ូឌុល `openai`។
- **សៀវភៅកំណត់ចំណាំ RAG មេរៀន 15** — បានជួសជុលការដំឡើងអ្នកអតិថិជន ប្រើជំនួស `DataFrame.append`
  ជាមួយ `pd.concat` ហើយបំពេញអត្ថប្រយោជន៍ប្រើប្រាស់ SDK ដ៏ចាស់។
- ឈ្មោះម៉ូដែលដែលបាត់បង់ / បញ្ឈប់ប្រើប្រាស់ (`gpt-3.5-turbo`, `gpt-35-turbo`) ត្រូវបានជំនួសដោយ `gpt-4o-mini`
  ក្នុងគំរូសកម្ម; លទ្ធផលបង្ហាត់បច្ចុប្បន្នក្នុងមេរៀន 18 ត្រូវបានរក្សាទុក និងបញ្ចូលកត់សម្គាល់
  មិនបានសរសេរឡើងវិញ។

### បង្រ្កាប / កំណត់សម្គាល់

- **គំរូ Microsoft Foundry Models** ដែលប្រើប្រាស់ `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — រួមមានគំរូ `githubmodels-*` និង `js-githubmodels` និងមេរៀនលេខ ១៩, ២០,
  និង ២១ — នៅតែមើលឃើញនៅលើ Model Inference API ដែលមិនគាំទ្រ Responses API ទេ។ ទាំងនេះ
  ត្រូវបានទុកនៅលើ SDK នោះតែម្នាក់ៗ។
- `AzureOpenAI()` ត្រូវបានរក្សាទុកដោយមានបំណងនៅកន្លែងដែលមិនទាន់សមរម្យ (ការ​ពង្រីក និងការបង្កើតរូបភាព),
  ពីព្រោះចរន្ត​ការងារទាំងនោះមិនមែនជ భాగមួយនៃការផ្លាស់ប្ដូរ​ប្រព័ន្ធ​Responses API ទេ។
- `text-embedding-ada-002` ត្រូវបានរក្សាទុកនៅពេលដែលសន្ទស្សន៍ embedding ដែលបានគណនាមុនអាស្រ័យលើវា។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->