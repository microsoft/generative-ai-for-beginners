# Registro delle modifiche

Tutte le modifiche significative al curriculum Generative AI for Beginners sono documentate in questo file.

Il formato si basa su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Poiché si tratta di un
curriculum di apprendimento anziché di un pacchetto software versionato, le voci sono raggruppate per data.

## [2026-07-16] — Validazione del contenuto + Risorse immagine della Lezione 09

### Modificato

- **Lezione 10 (app AI low-code):** aggiornati due link ritirati `docs.microsoft.com/powerapps/...` di Dataverse
  con i link attuali `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verificati attivi).
- **Lezione 17 (agenti AI):** modernizzato un esempio di modello datato (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, e Llama 3.3`) e il nome del deployment segnaposto nell'esempio Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** aggiunto il tracking ID mancante `?WT.mc_id=academic-105485-koreyst` al link
  *Microsoft for Startups*.
- **Risorse immagine della Lezione 09** rigenerate con il modello `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, e
  `images/startup.png` (la coppia prima/dopo dell'esempio di editing è stata prodotta tramite una vera
  chiamata `client.images.edit` con una maschera generata).

### Validato

- Revisionati i README delle lezioni 01, 03, 05, 12, 14 e 16 — tutti attuali (nomenclatura e link Microsoft Foundry corretti);
  nessuna modifica richiesta.
- Eseguita una validazione completa del markdown su tutti i 41 file markdown nel repository (escluse le traduzioni)
  per percorsi doc deprecati, localizzazioni Microsoft `/en-us/`, nomi di prodotti/modelli obsoleti, ID di tracking mancanti,
  e link/immagini relativi interrotti. L'unica lacuna individuata è stata l'ID di tracking *Microsoft for Startups*;
  tutti gli altri avvisi si sono rivelati falsi positivi (link di traduzione auto-generati,
  segnaposto commentati e URL strutturali terzi parti `/en/`).

## [2026-07-15] — Riscrittura Lezione 09 (Applicazioni Immagini) per modelli GPT Image

### Modificato

- **Riscritta la lezione 09 "Costruire Applicazioni di Generazione di Immagini"** attorno alla famiglia di modelli
  **`gpt-image`** attuale (default **`gpt-image-2`**; GA anche `gpt-image-1.5` / `gpt-image-1-mini`), sostituendo il contenuto legacy DALL·E 2/3.
  Correzioni chiave:
  - i modelli `gpt-image` restituiscono l'immagine in **base64 (`b64_json`)**, non un URL. Aggiornati tutti gli esempi per usare
    `base64.b64decode(...)` invece di scaricare un `url` con `requests`.
  - Aggiornata la versione API immagini a `2025-04-01-preview`.

  - Sostituita la sezione "temperature" inventata (i modelli di immagini non usano `temperature`) e il
    contenuto delle **variazioni** immagine solo DALL·E-2 con una sezione di **modifica immagine** (maschera/ritocco).
  - Aggiornati `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, entrambi
    i notebook dell'assegnazione (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), e il notebook .NET `.dib`.

### Rimosso

- Cancellati i campioni obsoleti `python/aoai-app-variation.py` e `python/oai-app-variation.py`
  (`images.create_variation` è solo DALL·E-2 e non supportato da `gpt-image`).
- Cancellate 4 risorse immagine orfane legate alla sezione di confronto temperature rimossa
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Eliminata la dipendenza non necessaria `requests` dai campioni Python e requisiti della lezione.

### Validato

- Eseguito `aoai-app.py` end-to-end contro un modello `gpt-image-1.5` distribuito e confermato che il
  flusso di decodifica/salvataggio base64 produce un PNG. Notebook confermati validi JSON.

## [2026-07-14] — Aggiornamento Modello Predefinito + Guida Modello di Ragionamento

### Cambiato

- **Modello chat predefinito `gpt-4o-mini` → `gpt-5-mini`** in tutti i campioni eseguibili del curriculum,
  documentazione e configurazione. Questo è stato determinato dallo stato del ciclo di vita dei modelli: su Microsoft Foundry,
  `gpt-4o-mini` (ritirato il 2026-10-01) e l'intera famiglia `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ritirati il 2026-10-14) sono **in fase di deprecazione**, mentre la **famiglia GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) è Generalmente Disponibile** (ritirato il 2027-02-06). Aggiornati:
  - `.env.copy`, `00-course-setup/03-providers.md` (raccomandazioni per il deployment e comandi `az cognitiveservices`),
    e i README delle lezioni 04, 06, 07 e 15.
  - Campioni Python nella lezione 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) e script della lezione 08.
  - Campioni TypeScript / JavaScript nelle lezioni 06, 07 e 11, e i notebook `.dib` .NET per
    le lezioni 06 e 07.
  - Notebook di assegnazione nelle lezioni 04, 06, 07 e 11 (celle codice), più esempi per docstring in `shared/python/api_utils.py`.
  - .

- **Guida ai parametri del modello di ragionamento (nuovo).** `gpt-5-mini` è un modello di *ragionamento*: non supporta **`temperature`/`top_p`, e utilizza `max_completion_tokens` (chat completions) / 
  `max_output_tokens` (Responses API) invece di `max_tokens`. Di conseguenza:**
 

  - Rimosso `temperature`/`top_p`/`max_tokens` dai campioni che ora usano `gpt-5-mini` di default
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Aggiunta una nota **"I modelli di reasoning non usano `temperature`"** alla lezione 06, spiegando che
    i modelli di reasoning sono guidati con **prompt engineering + controlli di reasoning** piuttosto che
    manopole di sampling, mentre `temperature`/`top_p` rimangono valide per modelli non di reasoning
    (GPT-4.x, Mistral, Llama, Phi, modelli open).
- **`gpt-5-mini` non è utilizzato per il tutorial di fine-tuning (lezione 18).** GPT-5 supporta solo
  il fine-tuning rinforzato (RFT); la walkthrough di fine-tuning supervisionato (SFT) della lezione 18 mantiene
  `gpt-4.1-mini`, che supporta SFT/DPO.
- **Le demo di Temperature usano un modello Llama.** Per continuare a insegnare `temperature` (che i modelli di reasoning
  rifiutano), un modello `Llama-3.3-70B-Instruct` è usato tramite l'endpoint Foundry Models. Aggiunta una nuova
  variabile `AZURE_INFERENCE_CHAT_MODEL` a `.env.copy`; i notebook `githubmodels` delle lezioni 04/06 e il
  campione `06` `js-githubmodels` la leggono (tornando a `Llama-3.3-70B-Instruct`) e mantengono le loro
  demo di `temperature`/`top_p`/`max_tokens`.
- **Campioni JS / .NET aggiornati per GPT-5.** Rimosso `temperature`/`top_p`/`max_tokens` dai campioni GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - che alza anche `MaxOutputTokenCount`
  così l'output reasoning non è troncato). Il campione `06` `js-githubmodels` ora usa Llama per mantenere la demo
  di temperatura. Il `.dib` sottolinea che `Azure.AI.Inference` + un modello Llama è il modo per
  dimostrare `Temperature` in .NET.
- Rimasti `gpt-4o-mini` / `gpt-5-mini` nei posti dove restano accurati: riferimenti all’encoding token di `tiktoken`,
  liste di disponibilità del catalogo modello e modelli vocali della lezione 02 (`gpt-4o-transcribe`).
- Le lezioni 20 (Mistral) e 21 (Meta) mantengono `temperature`/`max_tokens` perché mirano
  ai modelli Mistral/Llama, che supportano quei parametri.

## [2026-07-06] — Aggiornamento di Modernizzazione dei Contenuti

Un ampio aggiornamento per mantenere il curriculum accurato per il 2026: API moderne, nomi prodotti e
nomi modelli attuali, guida aggiornata ai provider e nuovo tooling per l’esperienza dello sviluppatore.

### Aggiunto

- Sezione **Microsoft Agent Framework** nella lezione `17-ai-agents` che copre agenti singoli di chat,
  chiamate a strumenti/funzioni, configurazione Azure OpenAI (Microsoft Foundry) e orchestrazione di workflow multi-agente
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentato come provider offline / on-device (insieme a Ollama) in
  `00-course-setup/03-providers.md` e lezione `19-slm`.
- **Workflow di integrazione continua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (applicati sul modulo `shared/` mantenuto,
    raccomandazione per il resto del curriculum), passaggio consigliato ESLint e un job pytest.
  - `.github/workflows/security.yml` — Analisi CodeQL (Python + JavaScript/TypeScript) e
    revisione dipendenze sulle pull request.
- **Suite di test** sotto `tests/` — 41 test pytest che coprono il modulo di utilità condiviso.
- **Skill di migrazione Azure OpenAI → Responses API** sotto
  `.github/skills/azure-openai-to-responses/` usata per guidare la migrazione API.

### Cambiato

- **Chat Completions API → Responses API** in tutti i campioni Python e TypeScript di chat
  (`client.responses.create(...)` → `response.output_text`), incluse le lezioni 04, 06, 07, 11,
  15 e 18, più i loro README.
- **GitHub Models → Microsoft Foundry Models** in tutta la prosa, link e campioni. GitHub Models
  verrà ritirato alla fine di luglio 2026; i campioni ora puntano al catalogo modelli Microsoft Foundry e usano
  le variabili ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` e documentazione provider** aggiornate per riflettere che Azure OpenAI ora fa parte
  di Microsoft Foundry, e la versione API di default è aggiornata a `2024-10-21`.
- **Campioni TypeScript** (lezioni 06, 07, 08, 11) migrati dal deprecato SDK beta `@azure/openai`
  al pacchetto `openai` (le app chat usano la Responses API; l’app di ricerca usa il
  client embeddings).
- **Notebook .NET** (`dotnet/*.dib`) standardizzati su `Azure.AI.OpenAI` **2.1.0**: lezioni 06 e 07
  usano l’API `ChatClient`, la lezione 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  la lezione 09 usa `ImageClient` (`GenerateImage`) con `gpt-image-1`, rimpiazzando il vecchio
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` da `1.0.0-beta.9`.
- **Modernizzazione dei nomi prodotto**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lezioni 14, 16, 17) e "Bing" → **Microsoft Copilot** (lezione 12), dove si riferivano ai
  prodotti attuali.
- **DevContainer** (`.devcontainer/`) ora include Pylance, Black, Ruff, ESLint, Prettier, e Copilot
  come estensioni, abilita il format-on-save e installa `ruff`, `black`, `mypy` e `pytest` così che i controlli CI
  possano essere replicati localmente.
- **Generazione immagini** (lezione 09) raccomanda `gpt-image-1` per Azure (il catalogo Azure ha rimosso
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** aggiornato per riflettere il lavoro completato (migrazione API, CI,
  DevContainer, test) e i fatti attuali (le traduzioni sono prodotte automaticamente dal
  Azure Co-op Translator; l'API Assistants è sostituita dall'API Responses).

### Correzioni

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ora restituisce una
  stringa vuota per input composti solo da spazi bianchi invece di generare un errore "troppo corto" (coerente con il
  caso `None`). Individuato e coperto dalla nuova suite di test.
- **Campioni immagine Lezione 09** — corretti bug reali: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e una variabile che sovrascriveva il modulo `openai`.
- **Notebook Lezione 15 RAG** — riparata la configurazione del client, sostituito il metodo rimosso `DataFrame.append`
  con `pd.concat`, e modernizzato l'uso dell'SDK legacy.
- Nomi di modelli deprecati/ritirati (`gpt-3.5-turbo`, `gpt-35-turbo`) sostituiti con `gpt-4o-mini`
  nei campioni attivi; gli output storici di fine-tuning della lezione 18 sono stati conservati e annotati
  invece di essere riscritti.

### Deprecati / Note

- **Campioni Microsoft Foundry Models** che usano l'SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — i campioni `githubmodels-*` e `js-githubmodels` e le lezioni 19, 20,
  e 21 — rimangono sull'API Model Inference, che **non** supporta l'API Responses. Questi sono
  intenzionalmente lasciati su quell'SDK.
- `AzureOpenAI()` è intenzionalmente mantenuto dove ancora appropriato (embedding e generazione immagini),
  poiché questi flussi di lavoro non fanno parte della migrazione all'API Responses.
- Riferimenti a `text-embedding-ada-002` sono mantenuti dove un indice di embedding precomputato ne dipende.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->