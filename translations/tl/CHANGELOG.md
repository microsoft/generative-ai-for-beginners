# Tala ng mga Pagbabago

Nakadokumento sa file na ito ang lahat ng mahahalagang pagbabago sa kurikulum ng Generative AI para sa mga Nagsisimula.

Ang format ay batay sa [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dahil ito ay isang
kurikulum sa pag-aaral at hindi isang versioned na software package, ang mga entry ay inayos ayon sa petsa.

## [2026-07-16] — Pagpapatunay ng Nilalaman + Mga Larawan ng Aralin 09

### Binago

- **Aralin 10 (low-code AI apps):** in-update ang dalawang retiradong `docs.microsoft.com/powerapps/...` Dataverse
  na mga link sa kasalukuyang `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (napatunayan na gumagana).
- **Aralin 17 (AI agents):** iniumangkin ang isang lumang halimbawa ng modelo (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, at Llama 3.3`) at isang placeholder na pangalan ng deployment sa Agent Framework sample
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** idinagdag ang nawawalang `?WT.mc_id=academic-105485-koreyst` tracking ID sa
  link ng *Microsoft for Startups*.
- **Mga asset ng larawan sa Aralin 09** ay muling ginawa gamit ang `gpt-image` na modelo: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, at
  `images/startup.png` (ang halimbawa ng pag-edit ay gawa gamit ang isang totoong
  `client.images.edit` na tawag na may generated mask).

### Napatunayan

- In-audit ang mga README para sa mga aralin 01, 03, 05, 12, 14, at 16 — lahat ay kasalukuyan (tamang pangalan at mga link ng Microsoft Foundry);
  walang kinakailangang pagbabago.
- Pinatakbo ang buong pag-validate ng markdown sa lahat ng 41 na mga markdown file sa repo (hindi kasama ang mga salin) para sa
  deprecated na mga path ng dokumento, `/en-us/` mga locale ng Microsoft, lumang pangalan ng produkto/modelo, nawawalang mga tracking
  ID, at sirang relative na mga link/larawan. Tanging ang nawawalang *Microsoft for Startups* tracking-ID lang ang
  nagawang ayusin; lahat ng iba pang mga flag ay kinumpirmaang false positives (auto-generated na translation links,
  commented-out placeholders, at third-party `/en/` structural URLs).

## [2026-07-15] — Muling Pagsulat ng Aralin 09 (Mga Aplikasyon ng Larawan) para sa GPT Image Models

### Binago

- **Muling isinulat ang aralin 09 "Pagbuo ng Mga Aplikasyon ng Pagbuo ng Larawan"** gamit ang kasalukuyang **`gpt-image`**
  na pamilya ng mga modelo (default na **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ay GA na rin), pinalitan ang
  lumang nilalaman ng DALL·E 2/3. Mga pangunahing koreksyon:
  - Ang mga `gpt-image` na modelo ay nagbabalik ng larawan bilang **base64 (`b64_json`)**, hindi URL. In-update lahat ng halimbawa upang
    gumamit ng `base64.b64decode(...)` imbes na mag-download ng `url` gamit ang `requests`.
  - Inusap ang bersyon ng image API sa `2025-04-01-preview`.
  - Pinalitan ang gawa-gawang "temperature" na seksyon (hindi gumagamit ng `temperature` ang mga image model) at ang
    DALL·E-2-lamang na mga **variation** ng larawan ng nilalaman ng seksyon ng **image editing** (mask/inpainting) na seksyon.
  - In-update ang `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, parehong
    assignment notebook (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), at ang .NET `.dib` notebook.

### Tinanggal

- Tinanggal ang mga lipas na `python/aoai-app-variation.py` at `python/oai-app-variation.py` na mga sample
  (`images.create_variation` ay para lamang sa DALL·E-2 at hindi suportado ng `gpt-image`).
- Tinanggal ang 4 na orphaned na asset ng larawan na nauugnay sa tinanggal na seksyon tungkol sa temperature comparison
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Tinanggal ang hindi kinakailangang dependency na `requests` mula sa mga Python sample at mga requirements ng aralin.

### Napatunayan

- Pinatakbo ang `aoai-app.py` ng mula umpisa hanggang dulo laban sa naka-deploy na `gpt-image-1.5` modelo at kinumpirma na ang
  base64 decode/save flow ay naglalabas ng PNG. Nasigurong valid JSON ang mga notebook.

## [2026-07-14] — Pag-update ng Default Model + Patnubay sa Reasoning-Model

### Binago

- **Default chat model `gpt-4o-mini` → `gpt-5-mini`** sa buong mga runnable sample sa kurikulum,
  dokumentasyon, at configuration. Ito ay dahil sa lifecycle status ng modelo: sa Microsoft Foundry,
  ang `gpt-4o-mini` (magre-retire sa 2026-10-01) at ang buong pamilya ng `gpt-4.1`
  (`gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, magre-retire sa 2026-10-14) ay **Nagde-deprecate**, samantalang ang **Pamilya ng GPT-5**
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) ay Generally Available** (magre-retire sa 2027-02-06). In-update:
  - `.env.copy`, `00-course-setup/03-providers.md` (inirerekomendang deployment at `az cognitiveservices`
    deploy commands), at ang mga README para sa mga aralin 04, 06, 07, at 15.
  - Mga Python sample sa aralin 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) at mga script sa aralin 08.
  - Mga TypeScript / JavaScript sample sa mga aralin 06, 07, at 11, at ang `.dib` na .NET notebooks para sa
    mga aralin 06 at 07.
  - Assignment notebooks sa mga aralin 04, 06, 07, at 11 (mga code cell), kasama ang `shared/python/api_utils.py`
    na mga docstring halimbawa.
- **Patnubay sa parameter ng reasoning-model (bago).** Ang `gpt-5-mini` ay isang *reasoning* na modelo:
  hindi nito sinuportahan ang `temperature`/`top_p`, at gumagamit ng `max_completion_tokens` (para sa chat completions) /
  `max_output_tokens` (para sa Responses API) bilang kapalit ng `max_tokens`. Dahil dito:
  - Tinanggal ang `temperature`/`top_p`/`max_tokens` mula sa mga sample na ngayon ay default sa `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Nagdagdag ng **"Hindi gumagamit ang mga reasoning model ng `temperature`"** na tala sa aralin 06, na nagpapaliwanag na
    ang mga reasoning model ay kinokontrol gamit ang **prompt engineering + reasoning controls** imbes na
    mga sampling knob, habang ang `temperature`/`top_p` ay valid pa rin sa non-reasoning models
    (GPT-4.x, Mistral, Llama, Phi, open models).
- **Hindi ginagamit ang `gpt-5-mini` para sa fine-tuning tutorial (aralin 18).** Suportado lamang ng GPT-5
  ang reinforcement fine-tuning (RFT); ang walkthrough ng supervised fine-tuning (SFT) sa aralin 18 ay nananatili
  sa `gpt-4.1-mini`, na sumusuporta sa SFT/DPO.
- **Ang temperature demos ay gumagamit ng Llama model.** Para mapanatili ang pagtuturo ng `temperature` (na tinatanggihan ng mga reasoning model),
  ginamit ang `Llama-3.3-70B-Instruct` na modelo mula sa Foundry Models endpoint. Nagdagdag ng bagong
  variable na `AZURE_INFERENCE_CHAT_MODEL` sa `.env.copy`; binabasa ito ng lesson 04/06 `githubmodels` notebooks at
  ng `06` `js-githubmodels` sample (na bumababa sa default na `Llama-3.3-70B-Instruct`) at pinananatili ang
  temperature/top_p/max_tokens demos nito.
- **In-update ang mga JS / .NET sample para sa GPT-5.** Tinanggal ang `temperature`/`top_p`/`max_tokens` mula sa mga GPT-5
  sample (`06` `recipe-app` TypeScript, `06` `.dib` .NET - na nagtaas din ng `MaxOutputTokenCount`
  para hindi maputol ang reasoning output). Ginamit ng `06` `js-githubmodels` sample ang Llama para sa temperature demo nito.
  Ang `.dib` ay nagtala na ang `Azure.AI.Inference` + Llama model ang paraan upang
  ipakita ang `Temperature` sa .NET.
- Iniwan ang `gpt-4o-mini` / `gpt-5-mini` sa lugar kung saan ito ay nananatiling tama: mga reference sa `tiktoken` token-encoding,
  availability list ng model catalog, at mga speech model sa aralin 02 (`gpt-4o-transcribe`).
- Pinananatili ng mga sample sa aralin 20 (Mistral) at 21 (Meta) ang `temperature`/`max_tokens` dahil ang mga ito ay target
  ay mga Mistral/Llama models, na sumusuporta sa mga parameter na iyon.

## [2026-07-06] — Refresh ng Modernisasyon ng Nilalaman

Isang malawak na refresh upang panatilihing tumpak ang kurikulum para sa 2026: modernong mga API, kasalukuyang pangalan ng produkto at
mga pangalan ng modelo, na-update na patnubay sa provider, at bagong mga tooling para sa karanasan ng developer.

### Idinagdag

- Seksyon ng **Microsoft Agent Framework** sa aralin `17-ai-agents` na naglalaman ng mga single chat agents,
  mga tools/function calling, Azure OpenAI (Microsoft Foundry) configuration, at multi-agent
  workflow orchestration (`SequentialBuilder` / `ConcurrentBuilder`).
- Dokumentado ang **Foundry Local** bilang offline / on-device na provider (kasama ang Ollama) sa
  `00-course-setup/03-providers.md` at aralin `19-slm`.
- **Continuous integration workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (pinapatupad sa maintained `shared/`
    module, advisory sa buong kurikulum), isang advisory ESLint pass, at isang pytest job.
  - `.github/workflows/security.yml` — CodeQL analysis (Python + JavaScript/TypeScript) at
    dependency review sa mga pull request.
- **Test suite** sa ilalim ng `tests/` — 41 pytest tests na sumasakop sa shared utility module.
- **Kakayahan sa paglipat mula Azure OpenAI → Responses API** sa ilalim ng
  `.github/skills/azure-openai-to-responses/` na ginagamit upang gabayan ang paglipat ng API.

### Binago

- **Chat Completions API → Responses API** sa lahat ng mga Python at TypeScript chat sample
  (`client.responses.create(...)` → `response.output_text`), kabilang ang mga aralin 04, 06, 07, 11,
  15, at 18, kasama ang kanilang mga README.
- **GitHub Models → Microsoft Foundry Models** sa buong teksto, mga link, at mga sample. Magre-retire ang GitHub Models sa katapusan ng Hulyo 2026;
  ang mga sample ay ngayon tumutukoy sa Microsoft Foundry model catalog at gumagamit ng
  mga environment variable na `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- In-update ang **`.env.copy`, `AGENTS.md`, at mga dokumento ng provider** para ipakita na ang Azure OpenAI ay bahagi na
  ng Microsoft Foundry, at ang default na bersyon ng API ay pinalaki sa `2024-10-21`.
- **Mga TypeScript sample** (mga aralin 06, 07, 08, 11) ay nilipat mula sa deprecated na `@azure/openai`
  beta SDK papunta sa `openai` package (ang mga chat app ay gumagamit ng Responses API; ang search app ay gumagamit ng
  embeddings client).
- **.NET notebooks** (`dotnet/*.dib`) ay na-standardize sa `Azure.AI.OpenAI` **2.1.0**: ang mga aralin 06 at 07
  ay gumagamit ng `ChatClient` API, aralin 08 ay gumagamit ng `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), at
  aralin 09 ay gumagamit ng `ImageClient` (`GenerateImage`) gamit ang `gpt-image-1`, papalit sa lumang
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` mula sa `1.0.0-beta.9`.
- **Modernisasyon ng mga pangalan ng produkto**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (mga aralin 14, 16, 17) at "Bing" → **Microsoft Copilot** (aralin 12), kung saan ito ay tumutukoy sa
  mga kasalukuyang produkto.
- **DevContainer** (`.devcontainer/`) ay ngayon may mga extension na Pylance, Black, Ruff, ESLint, Prettier, at Copilot,
  pinapagana ang format-on-save, at ini-install ang `ruff`, `black`, `mypy`, at `pytest` upang ang mga CI
  na pagsusuri ay maaaring gawin nang lokal.
- **Image generation** (aralin 09) ay inirerekomenda ang `gpt-image-1` para sa Azure (tinanggal ng Azure catalog
  ang `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** na-update upang ipakita ang natapos na trabaho (API migration, CI,
  DevContainer, mga pagsusulit) at kasalukuyang mga katotohanan (awtomatikong ginagawa ang mga pagsasalin ng
  Azure Co-op Translator; ang Assistants API ay pinalitan ng Responses API).

### Naayos

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ngayon ay nagbabalik ng
  walang laman na string para sa input na puro whitespace sa halip na maglabas ng error na "too short"
  (ayon sa kaso ng `None`). Natuklasan at nasaklaw ng bagong test suite.
- **Mga larawan ng Lesson 09** — naitama ang mga tunay na bug: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  at isang variable na tumalab sa `openai` na module.
- **Lesson 15 RAG notebook** — inayos ang client setup, pinalitan ang tinanggal na `DataFrame.append`
  ng `pd.concat`, at inayos ang paggamit ng legacy SDK.
- Mga deprecated / hindi na ginagamit na pangalan ng modelo (`gpt-3.5-turbo`, `gpt-35-turbo`) pinalitan ng `gpt-4o-mini`
  sa mga aktibong sample; ang mga historikal na fine-tuning output sa lesson 18 ay pinanatili at nilagyan ng anotasyon
  sa halip na isulat muli.

### Deprecated / Mga Tala

- **Mga sample ng Microsoft Foundry Models** na gumagamit ng `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ang `githubmodels-*` at `js-githubmodels` na mga sample at lessons 19, 20,
  at 21 — nananatili sa Model Inference API, na **hindi** sumusuporta sa Responses API. Sadyang iniwan ito
  sa SDK na iyon.
- `AzureOpenAI()` ay sinasadyang pinanatili kung saan naaangkop pa (embeddings at paggawa ng larawan),
  dahil ang mga workflow na iyon ay hindi bahagi ng migration ng Responses API.
- Ang mga sanggunian sa `text-embedding-ada-002` ay pinanatili kung saan nakadepende ang precomputed embedding index.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->