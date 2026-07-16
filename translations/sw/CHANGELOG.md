# Mabadiliko

Mabadiliko yote muhimu kwenye mtaala wa AI ya Kizazi kwa Waanzilishi yameandikwa katika faili hii.

Muundo umeongozwa na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Kwa kuwa huu ni
mtaala wa kujifunza badala ya kifurushi cha programu chenye toleo, maingizo yameunganishwa kwa tarehe.

## [2026-07-06] — Uboreshaji wa Maudhui ya Kisasa

Upya mpana ili kuweka mtaala kuwa sahihi kwa mwaka 2026: API za kisasa, majina ya sasa ya bidhaa na
majina ya mifano, maelekezo ya mtoa huduma yaliyosasishwa, na zana mpya za uzoefu wa mtaalamu wa maendeleo.

### Imekuwa

- Sehemu ya **Microsoft Agent Framework** katika somo `17-ai-agents` inahusu mawakala wa mazungumzo mmoja,
  zana/kuitisha kazi, usanidi wa Azure OpenAI (Microsoft Foundry), na upangaji wa kazi wa wakala wengi
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** imeandikwa kama mtoa huduma wa nje ya mtandao / kwenye kifaa (pamoja na Ollama) katika
  `00-course-setup/03-providers.md` na somo `19-slm`.
- **Midendo ya ushirikiano wa kuendelea**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (inalazimishwa kwenye moduli ya `shared/`
    inayodumishwa, ushauri katika mtaala mwingine wote), kipitisho cha ushauri cha ESLint, na kazi ya pytest.
  - `.github/workflows/security.yml` — Uchambuzi wa CodeQL (Python + JavaScript/TypeScript) na
    mapitio ya utegemezi kwenye maombi ya kusogeza.
- **Seti ya majaribio** chini ya `tests/` — majaribio 41 ya pytest yanayohusu moduli ya huduma ya pamoja.
- **Ujuzi wa uhamisho wa Azure OpenAI → Responses API** chini ya
  `.github/skills/azure-openai-to-responses/` inayotumika kuongoza uhamishaji wa API.

### Imebadilishwa

- **Chat Completions API → Responses API** katika sampuli zote za mazungumzo za Python na TypeScript
  (`client.responses.create(...)` → `response.output_text`), zikiwemo somo 04, 06, 07, 11,
  15, na 18, pamoja na README zao.
- **GitHub Models → Microsoft Foundry Models** katika maelezo, viungo, na sampuli. GitHub Models
  zitachezewa mwishoni mwa Julai 2026; sampuli sasa zinahusu katalogi ya mfano wa Microsoft Foundry na zinatumia
  mabadiliko ya mazingira ya `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **.env.copy, AGENTS.md, na nyaraka za mtoa huduma** zimesasishwa kuonyesha kuwa Azure OpenAI sasa ni sehemu
  ya Microsoft Foundry, na toleo la API la kiasili limeongezwa hadi `2024-10-21`.
- **Sampuli za TypeScript** (masomo 06, 07, 08, 11) zimehamishwa kutoka kwenye SDK ya beta iliyoanzishwa `@azure/openai`
  kwenda kifurushi cha `openai` (programu za mazungumzo zinatumia Responses API; programu ya utafutaji inatumia
  mteja wa embeddings).
- **Daftari za .NET** (`dotnet/*.dib`) zimepangwa kwa misingi ya `Azure.AI.OpenAI` **2.1.0**: masomo 06 na 07
  zinatumia API ya `ChatClient`, somo 08 linatumia `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), na
  somo 09 linatumia `ImageClient` (`GenerateImage`) na `gpt-image-1`, kubadilisha zamani
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` kutoka `1.0.0-beta.9`.
- **Uboreshaji wa majina ya bidhaa**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (masomo 14, 16, 17) na "Bing" → **Microsoft Copilot** (somo 12), pale ambapo hayo yalihusiana na
  bidhaa za sasa.
- **DevContainer** (`.devcontainer/`) sasa inaleta viendelezi vya Pylance, Black, Ruff, ESLint, Prettier, na Copilot,
  huwezesha muundo-kwa-kuhifadhi, na kusanidi `ruff`, `black`, `mypy`, na `pytest` ili ukaguzi wa CI
  ujirudie kwa eneo la mtaalamu.
- **Uundaji wa picha** (somo 09) huhimizwa kutumia `gpt-image-1` kwa Azure (katalogi ya Azure iliondoa
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** imesasishwa kuonesha kazi zilizokamilika (uhamisho wa API, CI,
  DevContainer, majaribio) na ukweli wa sasa (tafsiri hutengenezwa moja kwa moja na
  Mtafsiri wa Co-op wa Azure; API ya Assistants imebadilishwa na Responses API).

### Imerekebishwa

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` sasa hurudisha
  kamba tupu kwa ingizo la nafasi tu badala ya kutoa kosa la "fupi sana" (inayolingana na
  kesi ya `None`). Imepatikana na kufunikwa na seti mpya ya majaribio.
- **Sampuli za picha za somo 09** — makosa halisi yamerekebishwa: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  na kigezo kilichoenea module ya `openai`.
- **Daftari la somo 15 la RAG** — muundo wa mteja umeregezwa, ilibadilishwa `DataFrame.append` iliyotolewa
  na `pd.concat`, na matumizi ya zamani ya SDK yameboreshwa.
- Majina ya modeli yaliyopitwa / yaliyotolewa (`gpt-3.5-turbo`, `gpt-35-turbo`) yamebadilishwa na `gpt-4o-mini`
  katika sampuli zenye uhai; matokeo ya zamani ya fine-tuning katika somo 18 yalihifadhiwa na kuandikwa
  badala ya kuandikwa upya.

### Yaliyopitwa / Vidokezo

- Sampuli za **Microsoft Foundry Models** zinazotumia SDK ya `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — sampuli za `githubmodels-*` na `js-githubmodels` na masomo 19, 20,
  na 21 — zipo kwenye Model Inference API, ambayo haijiungi na Responses API. Hizi
  zimeachwa kwa makusudi kwenye SDK hiyo.
- `AzureOpenAI()` bado inahifadhiwa pale inapofaa (embeddings na uundaji wa picha),
  kwa kuwa midendo hiyo si sehemu ya uhamishaji wa Responses API.
- Marejeo ya `text-embedding-ada-002` yamehifadhiwa ambapo faharasa ya embedding iliyohesabiwa awali inategemea.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->