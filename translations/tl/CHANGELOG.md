# Tala ng Pagbabago

Lahat ng makabuluhang pagbabago sa Generative AI para sa Kurikulum ng mga Nagsisimula ay itinatala sa file na ito.

Ang format ay batay sa [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dahil ito ay isang
kurikulum sa pag-aaral at hindi isang versioned software package, ang mga entry ay pinaggrupo ayon sa petsa.

## [2026-07-06] — Refresh ng Modernisasyon ng Nilalaman

Isang malawakang refresh upang panatilihing tama ang kurikulum para sa 2026: mga makabagong API, kasalukuyang pangalan ng produkto at
pangalan ng modelo, na-update na gabay para sa provider, at mga bagong tooling para sa karanasan ng developer.

### Idinagdag

- **Microsoft Agent Framework** na seksyon sa leksyon `17-ai-agents` na sumasaklaw sa single chat agents,
  mga tool/pagtawag ng function, konfigurasyon ng Azure OpenAI (Microsoft Foundry), at multi-agent
  workflow orchestration (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** na naitala bilang offline / on-device provider (kasama ang Ollama) sa
  `00-course-setup/03-providers.md` at leksyon `19-slm`.
- **Mga workflow para sa continuous integration**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (ipinatupad sa pinangangalagaang `shared/`
    module, advisory sa buong kurikulum), isang advisory ESLint pass, at isang pytest na trabaho.
  - `.github/workflows/security.yml` — CodeQL analysis (Python + JavaScript/TypeScript) at
    pagsusuri ng dependency sa mga pull request.
- **Test suite** sa ilalim ng `tests/` — 41 na pytest tests na sumasaklaw sa shared utility module.
- **Azure OpenAI → Responses API migration skill** sa ilalim ng
  `.github/skills/azure-openai-to-responses/` na ginagamit upang gabayan ang paglipat ng API.

### Binago

- **Chat Completions API → Responses API** sa lahat ng Python at TypeScript na chat samples
  (`client.responses.create(...)` → `response.output_text`), kabilang ang mga leksyon 04, 06, 07, 11,
  15, at 18, pati na ang kanilang mga README.
- **GitHub Models → Microsoft Foundry Models** sa buong teksto, link, at mga sample. Ang GitHub Models
  ay aalisin sa katapusan ng Hulyo 2026; ang mga sample ay ngayon tumuturo sa catalog ng modelo ng Microsoft Foundry at gumagamit
  ng mga environment variables na `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, at mga dokumento ng provider** na na-update upang ipakita na ang Azure OpenAI ay bahagi na ng
  Microsoft Foundry, at ang default na bersyon ng API ay tininaas sa `2024-10-21`.
- **TypeScript samples** (mga leksyon 06, 07, 08, 11) na nailipat mula sa deprecated `@azure/openai`
  beta SDK papunta sa `openai` na package (ang chat apps ay gumagamit ng Responses API; ang search app ay gumagamit ng
  embeddings client).
- **.NET notebooks** (`dotnet/*.dib`) na standardized sa `Azure.AI.OpenAI` **2.1.0**: ang mga leksyon 06 at 07
  ay gumagamit ng `ChatClient` API, leksyon 08 ay gumagamit ng `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), at
  leksyon 09 ay gumagamit ng `ImageClient` (`GenerateImage`) gamit ang `gpt-image-1`, pinalitan ang legacy
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` mula sa `1.0.0-beta.9`.
- **Modernisasyon ng pangalan ng produkto**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (mga leksyon 14, 16, 17) at "Bing" → **Microsoft Copilot** (leksyon 12), kung saan ang mga iyon ay tumutukoy sa
  kasalukuyang mga produkto.
- **DevContainer** (`.devcontainer/`) ay ngayon may kasamang Pylance, Black, Ruff, ESLint, Prettier, at Copilot
  na mga extension, nagpapagana ng format-on-save, at nag-iinstall ng `ruff`, `black`, `mypy`, at `pytest` upang ang mga CI
  na pagsusuri ay maaaring maulit nang lokal.
- **Pagbuo ng imahe** (leksyon 09) ay nagrerekomenda ng `gpt-image-1` para sa Azure (ang Azure catalog ay nagtanggal
  ng `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** ay na-update upang ipakita ang natapos na gawain (API migration, CI,
  DevContainer, tests) at kasalukuyang mga katotohanan (ang mga pagsasalin ay awtomatikong ginagawa ng
  Azure Co-op Translator; ang Assistants API ay pinalitan na ng Responses API).

### Naayos

- **`shared/python/input_validation.py`** — ang `validate_text_input(allow_empty=True)` ay ngayon nagbabalik ng
  walang laman na string para sa input na whitespace lamang sa halip na magtapon ng error na "masyadong maikli" (ayon sa
  kaso ng `None`). Natuklasan at natakpan ng bagong test suite.
- **Mga sample ng imahe sa leksyon 09** — inayos ang mga tunay na bug: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  at isang variable na nagtatalab sa module na `openai`.
- **Leksiyon 15 RAG notebook** — inayos ang setup ng client, pinalitan ang tinanggal na `DataFrame.append`
  ng `pd.concat`, at inmodernisa ang paggamit ng legacy SDK.
- Tinanggal / inalis na mga pangalan ng modelo (`gpt-3.5-turbo`, `gpt-35-turbo`) ay pinalitan ng `gpt-4o-mini`
  sa mga aktibong sample; ang mga dating output ng fine-tuning sa leksiyon 18 ay iningatan at nilagyan ng anota
  imbes na isulat muli.

### Deprecated / Mga Tala

- **Mga sample ng Microsoft Foundry Models** na gumagamit ng `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ang `githubmodels-*` at `js-githubmodels` na mga sample at mga leksiyon 19, 20,
  at 21 — ay nananatili sa Model Inference API, na **hindi** sumusuporta sa Responses API. Ang mga ito ay
  sadyang nananatili sa SDK na iyon.
- Ang `AzureOpenAI()` ay sadyang pinananatili kung saan naaangkop pa rin (embeddings at pagbuo ng imahe),
  dahil ang mga workflow na iyon ay hindi bahagi ng Responses API migration.
- Ang mga sanggunian sa `text-embedding-ada-002` ay pinananatili kung saan umaasa ang precomputed embedding index sa mga ito.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->