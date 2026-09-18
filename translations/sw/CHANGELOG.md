# Mabadiliko ya Msururu

Mabadiliko yote muhimu kwa kozi ya Generative AI kwa Waanzilishi yameandikwa katika faili hii.

Muundo unategemea [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Kwa kuwa hii ni
kozi ya kujifunza badala ya kifurushi cha programu kilicho na matoleo, vitu vimewekwa kwa tarehe.

## [2026-07-16] — Uhakiki wa Yaliyomo + Mali za Picha za Somo la 09

### Imebadilika

- **Somo la 10 (programu za AI za msimbo-chini):** imesasishwa viungo viwili vilivyotoka `docs.microsoft.com/powerapps/...` vya Dataverse
  kwa `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (vimehakikishiwa kuishi).
- **Somo la 17 (mawakala wa AI):** mfano wa zamani wa mfano umeboreshwa (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, na Llama 3.3`) na jina la utumaji wa mfano katika sampuli ya Mfumo wa Mwakala
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Msingi `README.md`:** iliongeza kitambulisho kinachokosa cha ufuatiliaji `?WT.mc_id=academic-105485-koreyst` kwenye
  kiungo cha *Microsoft for Startups*.
- **Mali za picha za somo la 09** zimetengenezwa upya kwa kutumia mfano wa `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, na
  `images/startup.png` (paaru la mfano wa kuhariri kabla/baada lililotengenezwa kwa kutumia
  wito halisi wa `client.images.edit` pamoja na maski iliyotengenezwa).

### Imethibitishwa

- Tulikagua README za masomo 01, 03, 05, 12, 14, na 16 — zote ni za sasa (majina na viungo sahihi vya Microsoft Foundry);
  hakuna mabadiliko yanayohitajika.
- Tulifanya uhakiki kamili wa markdown kwenye faili zote 41 za markdown za ndani (isipokuwa tafsiri) kwa njia za hati zilizotokuwa
  halali, `/en-us/` maeneo ya Microsoft, majina ya bidhaa/mifano ya zamani, kutokuwepo kwa vitambulisho vya ufuatiliaji,
  na viungo/vipicha vilivyovunjika. Kiungo kimoja tu cha ufuatiliaji cha *Microsoft for Startups* kilikuwa cha kutekeleza;
  alama zingine zote zilithibitishwa kuwa bandia (viungo vya tafsiri vya auto-generated,
  placeholders zilizojumlishwa kama maoni, na URLs za muundo wa mtu wa tatu `/en/`).

## [2026-07-15] — Kuandika Upya Somo la 09 (Maombi ya Picha) kwa Mifano ya Picha za GPT

### Imebadilika

- **Ilibadilishwa somo la 09 "Kujenga Maombi ya Uundaji Picha"** kuzunguka familia ya sasa ya mfano **`gpt-image`**
  (chaguo-msingi **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` pia GA), ikichukua nafasi ya
  yaliyomo ya zamani ya DALL·E 2/3. Marekebisho muhimu:
  - mifano ya `gpt-image` hurudisha picha kama **base64 (`b64_json`)**, si URL. Sampuli zote zimesasishwa kutumia
    `base64.b64decode(...)` badala ya kupakua `url` kwa `requests`.
  - Iliongezwa toleo la API la picha hadi `2025-04-01-preview`.
  - Imeondolewa sehemu ya kughushi ya "joto" (mifano ya picha hachukui `temperature`) na yaliyomo ya
    tofauti za picha za DALL·E-2 pekee na sehemu ya **uhariri picha** (maski/ujazo).
  - Imeboreshwa `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, daftari zote mbili
    za usahili (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), na daftari la `.dib` la .NET.

### Imeondolewa

- Sampuli mbili za kale `python/aoai-app-variation.py` na `python/oai-app-variation.py` zimefutwa
  (`images.create_variation` ni ya DALL·E-2 tu na haitegemezwi na `gpt-image`).
- Mali nne za picha zisizohusiana zilizohusishwa na sehemu iliyotolewa ya kulinganisha joto zimefutwa
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Imeondolewa utegemezi usiokuwa wa lazima wa `requests` kutoka kwenye sampuli za Python za somo na mahitaji.

### Imethibitishwa

- Imethibitisha `aoai-app.py` kutoka mwanzo hadi mwisho dhidi ya mfano wa `gpt-image-1.5` uliotumika na kuthibitisha mchakato wa base64
  wa kubadilisha kuhifadhi huzaa PNG. Daftari zimehakikiwa kuwa JSON halali.

## [2026-07-14] — Sasisho la Mfano wa Chaguo-msingi + Mwongozo wa Mfano wa Kuchambua

### Imebadilika

- **Mfano wa mazungumzo wa chaguo-msingi `gpt-4o-mini` → `gpt-5-mini`** katika sampuli zinazosababishwa na kozi,
  nyaraka, na usanidi. Hii ilisababishwa na hali ya maisha ya mfano: kwenye Microsoft Foundry,
  `gpt-4o-mini` (itafutwa 2026-10-01) na familia yote ya `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, itafutwa 2026-10-14) zina **kuwa Hazitumiki**, ilhali familia ya **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) inapatikana kwa umma** (itafutwa 2027-02-06). Imesasishwa:
  - `.env.copy`, `00-course-setup/03-providers.md` (amri za utumaji zilizopendekezwa na `az cognitiveservices`
    deploy), na README za masomo 04, 06, 07, na 15.
  - Sampuli za Python katika somo la 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) na scripts za somo la 08.
  - Sampuli za TypeScript / JavaScript katika masomo 06, 07, na 11, na daftari la .NET `.dib` kwa
    masomo 06 na 07.
  - Daftari za usahili katika masomo 04, 06, 07, na 11 (seli za nambari), pamoja na mifano ya
    docstring `shared/python/api_utils.py`.
- **Mwongozo wa parameter wa mfano wa kuchambua (mpya).** `gpt-5-mini` ni mfano wa *kuchambua*: haitegemezi
  `temperature`/`top_p`, na hutumia `max_completion_tokens` (kamilisho la mazungumzo) /
  `max_output_tokens` (API za Majibu) badala ya `max_tokens`. Kulingana na hayo:
  - Imetolewa `temperature`/`top_p`/`max_tokens` kutoka kwa sampuli ambazo sasa hutumia `gpt-5-mini` kwa default
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, somo la 15 RAG README).
  - Imekuwa na nota ya **"Mifano ya Ufikiri haitumii `temperature`"** katika somo la 06, ikielezea kwamba
    mifano ya ufikiri inaelekezwa kwa **urahisi wa prompt + udhibiti wa ufikiri** badala ya
    vitufe vya sampuli, wakati `temperature`/`top_p` bado ni halali kwenye mifano isiyo ya ufikiri
    (GPT-4.x, Mistral, Llama, Phi, mifano ya wazi).
- **`gpt-5-mini` haitumiki kwa darasa la mafunzo ya utekelezaji wa hali ya juu (somo la 18).** GPT-5 inaunga mkono tu
  utekelezaji wa hali ya juu wa kuimarisha (RFT); somo la 18 la utekelezaji wa hali ya juu uliosimamiwa (SFT) linaendelea kutumia
  `gpt-4.1-mini`, ambayo inaunga mkono SFT/DPO.
- **Mifano ya Joto hutumia mfano wa Llama.** Ili kuendelea kufundisha `temperature` (ambayo mifano ya ufikiri
  hukataa), mfano wa `Llama-3.3-70B-Instruct` hutumiwa kupitia sehemu ya Foundry Models. Imengeza
  variable mpya ya `AZURE_INFERENCE_CHAT_MODEL` katika `.env.copy`; vitabu vya majaribio vya somo la 04/06 `githubmodels`
  na sampuli ya `06` `js-githubmodels` huvijasoma (ikirudi kwa `Llama-3.3-70B-Instruct`) na kuendelea na
  maonyesho yao ya `temperature`/`top_p`/`max_tokens`.
- **Sampuli za JS / .NET zimeboreshwa kwa GPT-5.** Imetolewa `temperature`/`top_p`/`max_tokens` kutoka kwa sampuli za GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ambayo pia huongeza `MaxOutputTokenCount`
  ili lisizifupishe matokeo ya ufikiri). Sampuli ya `06` `js-githubmodels` sasa inatumia Llama kuhifadhi
  maonyesho ya joto. `.dib` inabainisha kwamba `Azure.AI.Inference` + mfano wa Llama ndio njia ya kuonyesha
  `Temperature` katika .NET.
- Imeacha `gpt-4o-mini` / `gpt-5-mini` mahali ambapo bado ni sahihi: rejea za token-encoding za `tiktoken`,
  orodha za upatikanaji wa katalogi za mfano, na mifano ya hotuba ya somo la 02 (`gpt-4o-transcribe`).
- Sampuli la somo 20 (Mistral) na 21 (Meta) zinaendelea kutumia `temperature`/`max_tokens` kwa sababu zinawalenga
  mifano ya Mistral/Llama, ambayo huunga mkono vigezo hivyo.

## [2026-07-06] — Ufanyaji Upya wa Muhtasari wa Maudhui

Marekebisho makubwa ili kuhakikisha mtaala ni sahihi kwa mwaka 2026: API za kisasa, majina ya bidhaa na
majina ya mifano ya sasa, mwongozo ulioboreshwa wa watoa huduma, na zana mpya za uzoefu wa mtaalamu wa programu.

### Imeongezwa

- Sehemu ya **Microsoft Agent Framework** katika somo `17-ai-agents` inayohusu mawakala wa mazungumzo wa moja kwa moja,
  zana/mwito wa kazi, usanidi wa Azure OpenAI (Microsoft Foundry), na ufanisi wa mtiririko wa kazi wa mawakala wengi
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** imeandikwa kama muuzaji wa kando / kwa kifaa (pamoja na Ollama) katika
  `00-course-setup/03-providers.md` na somo `19-slm`.
- **Mtiririko wa usimamizi endelevu**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (inatumwa kwenye moduli ya `shared/`
    inayodumishwa, ushauri kwa mtaala mzima), ESLint ya ushauri, na kazi ya pytest.
  - `.github/workflows/security.yml` — Uchambuzi wa CodeQL (Python + JavaScript/TypeScript) na
    ukaguzi wa utegemezi kwenye maombi ya kuvuta.
- **Suite ya majaribio** chini ya `tests/` — majaribio 41 ya pytest yanayohusiana na moduli ya zana ya pamoja.
- **Uwezo wa uhamisho wa API kutoka Azure OpenAI hadi Responses API** chini ya
  `.github/skills/azure-openai-to-responses/` unaotumika kuongoza uhamisho wa API.

### Imebadilishwa

- **Chat Completions API → Responses API** katika sampuli zote za mazungumzo za Python na TypeScript
  (`client.responses.create(...)` → `response.output_text`), ikiwa ni pamoja na masomo 04, 06, 07, 11,
  15, na 18, pamoja na README zao.
- **GitHub Models → Microsoft Foundry Models** katika maandishi, viungo, na sampuli. GitHub Models
  itafutiwa mwisho wa Julai 2026; sampuli sasa zinaelekeza kwa katalogi ya mfano ya Microsoft Foundry na hutumia
  mabadiliko ya mazingira `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, na nyaraka za watoa huduma** zimebadilishwa kuonyesha kuwa Azure OpenAI sasa ni sehemu ya
  Microsoft Foundry, na toleo la API la default limeboreshwa hadi `2024-10-21`.
- Sampuli za **TypeScript** (masomo 06, 07, 08, 11) zimehamishwa kutoka SDK ya beta iliyopitwa ya `@azure/openai`
  kwenda kifurushi cha `openai` (maombi ya mazungumzo hutumia Responses API; programu ya utafutaji hutumia
  mteja wa embeddings).
- Vitabu vya majaribio vya **.NET** (`dotnet/*.dib`) vimethibitishwa kutumia `Azure.AI.OpenAI` **2.1.0**: masomo 06 na 07
  hutumia API ya `ChatClient`, somo la 08 hutumia `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), na
  somo la 09 hutumia `ImageClient` (`GenerateImage`) na `gpt-image-1`, badala ya zamani
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` kutoka `1.0.0-beta.9`.
- **Uboreshaji wa majina ya bidhaa**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (masomo 14, 16, 17) na "Bing" → **Microsoft Copilot** (somo 12), pale ambapo zilihusiana na
  bidhaa za sasa.
- **DevContainer** (`.devcontainer/`) sasa huleta Pylance, Black, Ruff, ESLint, Prettier, na nyongeza za Copilot,
  kizima muundo-wa-kuita, na kusakinisha `ruff`, `black`, `mypy`, na `pytest` ili ukaguzi wa CI
  uweze kuigwa kwa ndani.
- **Uundaji wa picha** (somo la 09) linapendekeza `gpt-image-1` kwa Azure (katalogi ya Azure imetoa
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** imesasishwa kuonyesha kazi zilizokamilika (uhamishaji wa API, CI,
  DevContainer, majaribio) na ukweli wa sasa (tafsiri hutengenezwa moja kwa moja na
  Mtafsiri wa Azure Co-op; API ya Msaidizi imebadiliwa na API ya Majibu).

### Imetatuliwa

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sasa inarudisha
  mfuatano wa herufi tupu kwa ingizo lenye nafasi tu badala ya kutoa kosa la "fupi sana"
  (inayolingana na kesi ya `None`). Imepatikana na kufunikwa na safu mpya ya majaribio.
- **Mifano ya picha ya Somo 09** — makosa halisi yamejadiliwa: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  na kigezo kilichoficha moduli ya `openai`.
- **Daftari la Somo 15 RAG** — marekebisho ya usanidi wa mteja, kubadilisha `DataFrame.append`
  iliyotolewa na `pd.concat`, na kusasisha matumizi ya SDK ya zamani.
- Majina ya modeli yaliyokataliwa / kuondolewa (`gpt-3.5-turbo`, `gpt-35-turbo`) yamebadiliwa kwa
  `gpt-4o-mini` katika mifano hai; matokeo ya kufinyangwa kihistoria kwenye somo la 18 yamehifadhiwa
  na kuwekwa alama badala ya kuandikwa upya.

### Yaliyokataliwa / Vidokezo

- **Mifano ya Microsoft Foundry Models** inayotumia SDK ya `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — mifano ya `githubmodels-*` na `js-githubmodels` pamoja na masomo ya 19, 20,
  na 21 — bado inatumia API ya Model Inference, ambayo haijiungi na API ya Majibu. Hizi
  zimeachwa kwenye SDK hiyo kwa makusudi.
- `AzureOpenAI()` inahifadhiwa kwa makusudi mahali panapofaa bado (embeddings na uundaji wa picha),
  kwa kuwa mchakato huo haujajumuishwa katika uhamishaji wa API ya Majibu.
- Marejeleo ya `text-embedding-ada-002` yanaendelea kuwepo pale indeksi ya embed iliyotangulia inavyohitaji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->