# Istoricul modificărilor

Toate schimbările notabile din curriculumul Generative AI for Beginners sunt documentate în acest fișier.

Formatul se bazează pe [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Deoarece acesta este un
curriculum de învățare și nu un pachet software versionat, înregistrările sunt grupate după dată.

## [2026-07-16] — Validarea conținutului + resurse imagini lecția 09

### Modificat

- **Lecția 10 (aplicații AI low-code):** actualizate două linkuri retrase `docs.microsoft.com/powerapps/...` din Dataverse
  către cele curente `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verificate live).
- **Lecția 17 (agenți AI):** modernizat un exemplu de model învechit (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, și Llama 3.3`) și un nume de implementare placeholder în exemplul Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Fișierul rădăcină `README.md`:** adăugat ID-ul de urmărire lipsă `?WT.mc_id=academic-105485-koreyst` la linkul
  *Microsoft for Startups*.
- **Resursele imagini pentru lecția 09** regenerate cu modelul `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, și
  `images/startup.png` (perechea înainte/după exemplul de editare a fost produsă printr-un apel real
  `client.images.edit` cu o mască generată).

### Validat

- Auditat fișierele README pentru lecțiile 01, 03, 05, 12, 14 și 16 — toate actualizate (nomenclatură corectă și linkuri Microsoft Foundry);
  nu sunt necesare modificări.
- Rulat o validare completă markdown pentru toate cele 41 de fișiere markdown din depozit (excluzând traducerile) pentru
  căi documentație învechite, locale Microsoft `/en-us/`, denumiri de produse/modele depășite, ID-uri de urmărire lipsă,
  și linkuri/imagine relative rupte. Singurul gol activat a fost cel pentru ID-ul de urmărire *Microsoft for Startups*;
  toate celelalte semnale au fost confirmate ca fals pozitive (linkuri automate de traducere,
  placeholder-e comentate, și URL-uri structurale terțe `/en/`).

## [2026-07-15] — Rescriere lecția 09 (Aplicații imagini) pentru modelele GPT Image

### Modificat

- **Rescris lecția 09 "Construirea aplicațiilor de generare a imaginilor"** în jurul familiei actuale de modele **`gpt-image`**
  (implicit **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` de asemenea GA), înlocuind conținutul
  învechit DALL·E 2/3. Corecții cheie:
  - Modelele `gpt-image` returnează imaginea ca **base64 (`b64_json`)**, nu un URL. Actualizate toate exemplele pentru
    `base64.b64decode(...)` în loc de descărcarea unui `url` cu `requests`.
  - Ridicată versiunea API-ului de imagini la `2025-04-01-preview`.

  - Secțiunea fabricată „temperature” a fost înlocuită (modelele de imagine nu folosesc `temperature`) și
    conținutul pentru **variații** de imagine exclusiv DALL·E-2 cu o secțiune de **editare imagine** (mască/retușare).
  - Actualizat `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ambele
    caiete de temă (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), și caietul .NET `.dib`.

### Eliminat

- Au fost șterse mostrele învechite `python/aoai-app-variation.py` și `python/oai-app-variation.py`
  (`images.create_variation` este doar pentru DALL·E-2 și nu este suportat de `gpt-image`).
- Au fost șterse 4 resurse de imagine orfane legate de secțiunea eliminată de comparație a temperaturii
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- A fost eliminată dependența inutilă `requests` din mostrele Python și din cerințele lecției.

### Validat

- A fost rulat `aoai-app.py` complet pe un model `gpt-image-1.5` implementat și confirmat că fluxul de
  decodare/salvare base64 produce un PNG. Caietele au fost confirmate ca JSON valid.

## [2026-07-14] — Actualizare Model Implicit + Ghidare prin Model de Raționament

### Modificat

- **Modelul de chat implicit `gpt-4o-mini` → `gpt-5-mini`** în toate mostrele executabile din curriculum,
  documentație și configurare. Acest lucru a fost determinat de statusul ciclului de viață al modelului: pe Microsoft Foundry,
  `gpt-4o-mini` (iese din uz la 2026-10-01) și întreaga familie `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ies din uz la 2026-10-14) sunt **Dezacreditate**, în timp ce familia **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) este General Disponibilă** (iese din uz la 2027-02-06). Actualizate:
  - `.env.copy`, `00-course-setup/03-providers.md` (comenzile recomandate de implementare și `az cognitiveservices`
    deploy), și READMEs pentru lecțiile 04, 06, 07 și 15.
  - Mostre Python în lecția 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) și scripturile lecției 08.
  - Mostre TypeScript / JavaScript din lecțiile 06, 07, și 11, și caietele .NET `.dib` pentru
    lecțiile 06 și 07.
  - Caietele de temă din lecțiile 04, 06, 07, și 11 (celule de cod), plus exemplarele docstring din `shared/python/api_utils.py`.
    .

- **Ghid pentru parametrii modelului de raționament (nou).** `gpt-5-mini` este un model de *raționament*: nu acceptă `temperature`/`top_p` și folosește `max_completion_tokens` (chat completions) /  
  `max_output_tokens` (Responses API) în loc de `max_tokens`. În consecință:  
  

  - Eliminat `temperature`/`top_p`/`max_tokens` din exemplele care acum utilizează implicit `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lecția 15 RAG README).
  - Adăugat o notă **"Modelele de raționament nu folosesc `temperature`"** la lecția 06, explicând că
    modelele de raționament sunt ghidate prin **inginierie de prompt + controale de raționament** mai degrabă decât
    prin setările de eșantionare, în timp ce `temperature`/`top_p` rămân valide pentru modelele non-raționament
    (GPT-4.x, Mistral, Llama, Phi, modelele open).
- **`gpt-5-mini` nu este folosit pentru tutorialul de fine-tuning (lecția 18).** GPT-5 suportă doar
  fine-tuning-ul prin întărire (RFT); lecția 18 de fine-tuning supravegheat (SFT) păstrează
  `gpt-4.1-mini`, care suportă SFT/DPO.
- **Demonstrațiile Temperature folosesc un model Llama.** Pentru a continua predarea `temperature` (pe care modelele de raționament
  îl resping), se folosește un model `Llama-3.3-70B-Instruct` prin endpoint-ul Foundry Models. Adăugat o variabilă nouă
  `AZURE_INFERENCE_CHAT_MODEL` în `.env.copy`; noteboook-urile `githubmodels` din lecțiile 04/06 și
  exemplul `06` `js-githubmodels` o citesc (caz în care revine la `Llama-3.3-70B-Instruct`) și păstrează
  demonstrațiile pentru `temperature`/`top_p`/`max_tokens`.
- **Exemplele JS / .NET actualizate pentru GPT-5.** Eliminat `temperature`/`top_p`/`max_tokens` din exemplele GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET – care de asemenea mărește `MaxOutputTokenCount`
  astfel încât ieșirea modelelor de raționament să nu fie trunchiată). Exemplul `06` `js-githubmodels` folosește acum Llama pentru a-și păstra
  demonstrația temperature. `.dib` notează că `Azure.AI.Inference` + un model Llama este modalitatea de
  a demonstra `Temperature` în .NET.
- Păstrat `gpt-4o-mini` / `gpt-5-mini` acolo unde acestea rămân corecte: referințe de tokenizare `tiktoken`,
  listele de disponibilitate a catalogului modelelor și modelele vocale din lecția 02 (`gpt-4o-transcribe`).
- Exemplele lecțiilor 20 (Mistral) și 21 (Meta) păstrează `temperature`/`max_tokens` deoarece vizează
  modelele Mistral/Llama, care suportă acești parametri.

## [2026-07-06] — Reîmprospătare a conținutului

O reîmprospătare extinsă pentru menținerea acurateței curriculumului în 2026: API-uri moderne, nume actuale de produse și
nume de modele, ghiduri actualizate pentru furnizori și noi unelte pentru experiența dezvoltatorului.

### Adăugat

- Secțiunea **Microsoft Agent Framework** în lecția `17-ai-agents` care acoperă agenți de chat simpli,
  instrumente/apeluri funcționale, configurarea Azure OpenAI (Microsoft Foundry) și orchestrarea fluxului de lucru multi-agent
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentat ca furnizor offline / pe dispozitiv (alături de Ollama) în
  `00-course-setup/03-providers.md` și lecția `19-slm`.
- **Fluxuri de integrare continuă**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (impuse modulului `shared/` menținut,
    recomandare peste restul curriculumului), o trecere ESLint recomandativă și un job pytest.
  - `.github/workflows/security.yml` — Analiză CodeQL (Python + JavaScript/TypeScript) și
    revizuire de dependențe la pull request-uri.
- **Suită de teste** sub `tests/` — 41 teste pytest care acoperă modulul de utilitare partajat.
- **Competență de migrare Azure OpenAI → Responses API** în
  `.github/skills/azure-openai-to-responses/` folosită pentru a ghida migrarea API.

### Modificat

- **Chat Completions API → Responses API** în toate exemplele Python și TypeScript de chat
  (`client.responses.create(...)` → `response.output_text`), incluzând lecțiile 04, 06, 07, 11,
  15 și 18, plus READMEs aferente.
- **GitHub Models → Microsoft Foundry Models** în tot textul, linkurile și exemplele. GitHub Models
  se închide la sfârșitul lunii iulie 2026; exemplele indică acum catalogul de modele Microsoft Foundry și folosesc
  variabilele de mediu `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Actualizate **`.env.copy`, `AGENTS.md` și documentația furnizorilor** pentru a reflecta că Azure OpenAI face acum parte
  din Microsoft Foundry, iar versiunea implicită a API-ului a fost majorată la `2024-10-21`.
- Exemplele **TypeScript** (lecțiile 06, 07, 08, 11) migrate de pe SDK-ul beta învechit `@azure/openai`
  către pachetul `openai` (aplicațiile de chat folosesc Responses API; aplicația de căutare folosește
  clientul embeddings).
- Notebook-uri **.NET** (`dotnet/*.dib`) standardizate pe `Azure.AI.OpenAI` **2.1.0**: lecțiile 06 și 07
  folosesc API-ul `ChatClient`, lecția 08 utilizează `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), iar
  lecția 09 folosește `ImageClient` (`GenerateImage`) cu `gpt-image-1`, înlocuind vechiul
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` din versiunea `1.0.0-beta.9`.
- Modernizarea numelor de produse: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lecțiile 14, 16, 17) și "Bing" → **Microsoft Copilot** (lecția 12), acolo unde acestea se refereau la
  produsele curente.
- Containerele de dezvoltare **DevContainer** (`.devcontainer/`) includ acum extensiile Pylance, Black, Ruff, ESLint, Prettier și Copilot,
  activează formatarea la salvare și instalează `ruff`, `black`, `mypy` și `pytest` astfel încât verificările CI
  să poată fi reproduse local.
- Generarea de imagini (lecția 09) recomandă `gpt-image-1` pentru Azure (catalogul Azure a eliminat
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** actualizat pentru a reflecta munca finalizată (migrare API, CI,
  DevContainer, teste) și faptele curente (traducerile sunt produse automat de
  Azure Co-op Translator; API-ul Asistenților este înlocuit de API-ul Răspunsurilor).

### Corectat

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` acum returnează un
  șir gol pentru intrarea formată numai din spații albe în loc să ridice o eroare de tip "prea scurt" (consistent cu
  cazul `None`). Identificat și acoperit de noua suită de teste.
- **Eșantioane imagine Lecția 09** — corectate erori reale: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  și o variabilă care masca modulul `openai`.
- **Notebook Lecția 15 RAG** — reparat setup-ul clientului, înlocuit `DataFrame.append` eliminat
  cu `pd.concat` și modernizată utilizarea SDK-ului vechi.
- Numele modelelor depreciate/retras (`gpt-3.5-turbo`, `gpt-35-turbo`) înlocuite cu `gpt-4o-mini`
  în eșantioanele active; ieșirile fine-tuning istorice din lecția 18 au fost păstrate și anotate
  în loc să fie rescrise.

### Depreciate / Note

- **Eșantioane Microsoft Foundry Models** care utilizează SDK-ul `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — eșantioanele `githubmodels-*` și `js-githubmodels` și lecțiile 19, 20,
  și 21 — rămân pe Model Inference API, care nu suportă API-ul Răspunsurilor. Acestea sunt
  lăsate intenționat pe acel SDK.
- `AzureOpenAI()` este reținut intenționat acolo unde încă este potrivit (embedding-uri și generare imagini),
  deoarece acele fluxuri de lucru nu fac parte din migrarea API-ului Răspunsurilor.
- Referințele la `text-embedding-ada-002` sunt păstrate unde un index de embedding precalculat depinde de ele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->