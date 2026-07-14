# Registro delle modifiche

Tutte le modifiche significative al curriculum Generative AI for Beginners sono documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Poiché questo è un
curriculum di apprendimento piuttosto che un pacchetto software versionato, le voci sono raggruppate per data.

## [2026-07-06] — Aggiornamento di modernizzazione del contenuto

Un ampio aggiornamento per mantenere il curriculum accurato per il 2026: API moderne, nomi attuali dei prodotti e
nomi dei modelli, linee guida aggiornate per i provider e nuovi strumenti per l'esperienza degli sviluppatori.

### Aggiunto

- Sezione **Microsoft Agent Framework** nella lezione `17-ai-agents` che copre agenti chat singoli,
  strumenti/chiamate di funzione, configurazione Azure OpenAI (Microsoft Foundry) e orchestrazione di flussi di lavoro multi-agente
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentato come provider offline / su dispositivo (insieme a Ollama) in
  `00-course-setup/03-providers.md` e lezione `19-slm`.
- **Workflow di integrazione continua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (applicati al modulo `shared/` mantenuto,
    suggerimento per tutto il resto del curriculum), un passaggio ESLint di avviso e un job pytest.
  - `.github/workflows/security.yml` — Analisi CodeQL (Python + JavaScript/TypeScript) e
    revisione delle dipendenze sulle pull request.
- **Suite di test** sotto `tests/` — 41 test pytest che coprono il modulo utility condiviso.
- **Skill migrazione Azure OpenAI → Responses API** sotto
  `.github/skills/azure-openai-to-responses/` usata per guidare la migrazione API.

### Modificato

- **Chat Completions API → Responses API** in tutti gli esempi Python e TypeScript di chat
  (`client.responses.create(...)` → `response.output_text`), incluse le lezioni 04, 06, 07, 11,
  15 e 18, oltre ai loro README.
- **Modelli GitHub → Modelli Microsoft Foundry** in tutto il testo, link ed esempi. I modelli GitHub
  saranno ritirati alla fine di luglio 2026; gli esempi ora puntano al catalogo modelli Microsoft Foundry e usano
  le variabili d'ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` e documentazione provider** aggiornati per riflettere che Azure OpenAI è ora parte
  di Microsoft Foundry, e la versione API predefinita aggiornata a `2024-10-21`.
- **Esempi TypeScript** (lezioni 06, 07, 08, 11) migrati dal deprecato SDK beta `@azure/openai`
  al pacchetto `openai` (le app di chat usano la Responses API; l'app di ricerca usa il
  client embeddings).
- **Notebook .NET** (`dotnet/*.dib`) standardizzati su `Azure.AI.OpenAI` **2.1.0**: lezioni 06 e 07
  usano l'API `ChatClient`, la lezione 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  la lezione 09 usa `ImageClient` (`GenerateImage`) con `gpt-image-1`, sostituendo il legacy
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` dalla versione `1.0.0-beta.9`.
- **Modernizzazione nomi prodotti**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lezioni 14, 16, 17) e "Bing" → **Microsoft Copilot** (lezione 12), dove tali nomi si riferivano ai
  prodotti attuali.
- **DevContainer** (`.devcontainer/`) ora include estensioni Pylance, Black, Ruff, ESLint, Prettier e Copilot,
  abilita la formattazione al salvataggio e installa `ruff`, `black`, `mypy` e `pytest` così che i controlli CI
  possano essere riprodotti localmente.
- **Generazione immagini** (lezione 09) raccomanda `gpt-image-1` per Azure (il catalogo Azure ha rimosso
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** aggiornato per riflettere i lavori completati (migrazione API, CI,
  DevContainer, test) e fatti attuali (le traduzioni sono prodotte automaticamente da
  Azure Co-op Translator; le Assistants API sono state sostituite dalla Responses API).

### Correzioni

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ora restituisce una
  stringa vuota per input composti solo da spazi bianchi invece di sollevare un errore "troppo corto" (coerente con il
  caso `None`). Individuato e coperto dalla nuova suite di test.
- **Esempi immagini lezione 09** — corretti errori reali: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e una variabile che nascondeva il modulo `openai`.
- **Notebook RAG lezione 15** — riparata la configurazione del client, sostituito il rimosso `DataFrame.append`
  con `pd.concat` e modernizzato l'uso legacy dello SDK.
- Nomi modelli deprecati / ritirati (`gpt-3.5-turbo`, `gpt-35-turbo`) sostituiti con `gpt-4o-mini`
  negli esempi attivi; gli output di fine-tuning storici nella lezione 18 sono stati preservati e annotati
  anziché riscritti.

### Deprecati / Note

- Esempi Modelli Microsoft Foundry che usano lo SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — gli esempi `githubmodels-*` e `js-githubmodels` e lezioni 19, 20,
  e 21 — restano sull'API Model Inference, che **non** supporta la Responses API. Questi sono
  intenzionalmente lasciati su quello SDK.
- `AzureOpenAI()` è mantenuto intenzionalmente dove ancora appropriato (embedding e generazione immagini),
  poiché quei flussi di lavoro non fanno parte della migrazione alla Responses API.
- I riferimenti a `text-embedding-ada-002` sono mantenuti dove un indice embedding precomputato ne dipende.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->