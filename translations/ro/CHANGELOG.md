# Changelog

Toate modificările notabile din curriculumul Generative AI for Beginners sunt documentate în acest fișier.

Formatul se bazează pe [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Deoarece acesta este un
curriculum de învățare, nu un pachet software versiune, înregistrările sunt grupate după dată.

## [2026-07-06] — Actualizare modernizare conținut

O actualizare amplă pentru a menține curriculumul corect pentru 2026: API-uri moderne, nume actuale de produse și
modele, îndrumări actualizate pentru furnizori și noi unelte pentru experiența dezvoltatorului.

### Adăugat

- Secțiunea **Microsoft Agent Framework** din lecția `17-ai-agents` care acoperă agenți chat unici,
  apeluri funcții/unelte, configurarea Azure OpenAI (Microsoft Foundry) și orchestrarea fluxului de lucru multi-agent
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentat ca furnizor offline / pe dispozitiv (alături de Ollama) în
  `00-course-setup/03-providers.md` și lecția `19-slm`.
- **Fluxuri de integrare continuă**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (aplicate pe modulul `shared/` menținut,
    recomandări pentru restul curriculumului), o trecere ESLint opțională și un job pytest.
  - `.github/workflows/security.yml` — Analiza CodeQL (Python + JavaScript/TypeScript) și
    revizuire dependențe la pull requesturi.
- **Suită de teste** în `tests/` — 41 teste pytest acoperind modulul utilitar comun.
- **Skill migrator Azure OpenAI → Responses API** în
  `.github/skills/azure-openai-to-responses/` folosit pentru ghidarea migrării API-ului.

### Modificat

- **Chat Completions API → Responses API** în toate exemplele de chat Python și TypeScript
  (`client.responses.create(...)` → `response.output_text`), inclusiv lecțiile 04, 06, 07, 11,
  15 și 18, plus documentațiile lor README.
- **GitHub Models → Microsoft Foundry Models** în întregul conținut, linkuri și exemple. GitHub Models
  se retrage la sfârșitul lunii iulie 2026; exemplele indică acum catalogul de modele Microsoft Foundry și folosesc
  variabilele de mediu `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` și documentația furnizorului** actualizate să reflecte că Azure OpenAI face parte acum
  din Microsoft Foundry, iar versiunea implicită a API-ului a fost majorată la `2024-10-21`.
- **Exemple TypeScript** (lecțiile 06, 07, 08, 11) migrate de la SDK-ul beta depreciat `@azure/openai`
  la pachetul `openai` (aplicațiile de chat folosesc Responses API; aplicația de căutare folosește
  clientul de embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) standardizate pe `Azure.AI.OpenAI` **2.1.0**: lecțiile 06 și 07
  folosesc API-ul `ChatClient`, lecția 08 folosește `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), iar
  lecția 09 folosește `ImageClient` (`GenerateImage`) cu `gpt-image-1`, înlocuind vechiul
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` din `1.0.0-beta.9`.
- **Modernizarea numelor produselor**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lecțiile 14, 16, 17) și "Bing" → **Microsoft Copilot** (lecția 12), unde acestea se refereau la
  produsele actuale.
- **DevContainer** (`.devcontainer/`) acum include extensiile Pylance, Black, Ruff, ESLint, Prettier și Copilot,
  activează formatarea la salvare și instalează `ruff`, `black`, `mypy` și `pytest` pentru reproducerea verificărilor CI
  local.
- **Generare imagine** (lecția 09) recomandă `gpt-image-1` pentru Azure (catalogul Azure a eliminat
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** actualizat pentru a reflecta munca finalizată (migrare API, CI,
  DevContainer, teste) și realitățile curente (traducerile sunt produse automat de
  Azure Co-op Translator; API-ul Assistants este înlocuit de Responses API).

### Remediat

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` returnează acum un
  șir gol pentru input format doar din spații albe în loc să genereze o eroare de „prea scurt” (consistent cu
  cazul `None`). Găsit și acoperit de noua suită de teste.
- **Exemplele de imagine din lecția 09** — corecturi de erori reale: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  și o variabilă care suprascria modulul `openai`.
- **Notebook-ul RAG din lecția 15** — reparat setup-ul clientului, înlocuit `DataFrame.append` eliminat
  cu `pd.concat` și modernizat utilizarea SDK-ului vechi.
- Numele modelelor depreciate/retrasd (`gpt-3.5-turbo`, `gpt-35-turbo`) înlocuite cu `gpt-4o-mini`
  în exemplele active; ieșirile fine-tuning istorice din lecția 18 au fost păstrate și notate
  în loc să fie rescrise.

### Deprecated / Note

- Exemplele Microsoft Foundry Models care folosesc SDK-ul `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — exemplele `githubmodels-*` și `js-githubmodels` și lecțiile 19, 20,
  și 21 — rămân pe Model Inference API, care nu suportă Responses API. Acestea sunt
  lăsate intenționat pe acel SDK.
- `AzureOpenAI()` este păstrat intenționat acolo unde mai este potrivit (embeddings și generare imagine),
  deoarece acele fluxuri de lucru nu fac parte din migrarea Responses API.
- Referințele la `text-embedding-ada-002` sunt păstrate unde un index pre-calculat de embedding depinde de ele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->