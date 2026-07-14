# Roadmap per Funzionalità Migliorate e Miglioramenti

Questo documento delinea miglioramenti e perfezionamenti raccomandati per il curriculum Generative AI for Beginners, basati su una revisione completa del codice e analisi delle best practice del settore.

## Sintesi Esecutiva

Il codice è stato analizzato per sicurezza, qualità del codice ed efficacia educativa. Questo documento fornisce raccomandazioni per correzioni immediate, miglioramenti a breve termine e potenziamenti futuri.

---

## 1. Miglioramenti della Sicurezza (Priorità: Critica)

### 1.1 Correzioni Immediate (Completate)

| Problema | File Interessati | Stato |
|-------|----------------|--------|
| SECRET_KEY hardcoded | `05-advanced-prompts/python/aoai-solution.py` | Risolto |
| Mancata validazione env | Diversi file JS/TS | Risolto |
| Chiamate a funzioni non sicure | `11-integrating-with-function-calling/js-githubmodels/app.js` | Risolto |
| Perdita di handle di file | `08-building-search-applications/scripts/` | Risolto |
| Mancati timeout nelle richieste | `09-building-image-applications/python/` | Risolto |

### 1.2 Funzionalità di Sicurezza Aggiuntive Raccomandate

1. **Esempi di Rate Limiting**
   - Aggiungere codice di esempio che mostra come implementare il rate limiting per le chiamate API
   - Dimostrare pattern di backoff esponenziale

2. **Rotazione delle Chiavi API**
   - Aggiungere documentazione sulle best practice per la rotazione delle chiavi API
   - Includere esempi di utilizzo di Azure Key Vault o servizi simili

3. **Integrazione per la Sicurezza dei Contenuti**
   - Aggiungere esempi di utilizzo dell’API Azure Content Safety
   - Dimostrare pattern di moderazione input/output

---

## 2. Miglioramenti della Qualità del Codice

### 2.1 Aggiunti File di Configurazione

| File | Scopo |
|------|---------|
| `.eslintrc.json` | Regole di linting per JavaScript/TypeScript |
| `.prettierrc` | Standard di formattazione del codice |
| `pyproject.toml` | Configurazione degli strumenti Python (Black, Ruff, mypy) |

### 2.2 Creazione di Utility Condivise

Nuovo modulo `shared/python/` con:
- `env_utils.py` - Gestione variabili d’ambiente
- `input_validation.py` - Validazione e sanificazione input
- `api_utils.py` - Wrapper sicuri per richieste API

### 2.3 Miglioramenti Consigliati al Codice

1. **Copertura dei Type Hint**
   - Aggiungere type hint a tutti i file Python
   - Abilitare la modalità TypeScript rigorosa in tutti i progetti TS

2. **Standard di Documentazione**
   - Aggiungere docstring a tutte le funzioni Python
   - Aggiungere commenti JSDoc a tutte le funzioni JavaScript/TypeScript

3. **Framework di Testing**
   - Aggiungere configurazione pytest ed esempi di test _(fatto: config pytest in `pyproject.toml`; esempi di test per le utility condivise in [`tests/`](../../../tests) eseguiti in CI)_
   - Aggiungere configurazione Jest per JavaScript/TypeScript

---

## 3. Miglioramenti Educativi

### 3.1 Nuovi Argomenti per Lezioni

1. **Sicurezza nelle Applicazioni AI** (Lezione proposta 22)
   - Attacchi e difese da injection di prompt
   - Gestione chiavi API
   - Moderazione dei contenuti
   - Rate limiting e prevenzione abusi

2. **Deployment in Produzione** (Lezione proposta 23)
   - Containerizzazione con Docker
   - Pipeline CI/CD
   - Monitoraggio e logging
   - Gestione dei costi

3. **Tecniche RAG Avanzate** (Lezione proposta 24)
   - Ricerca ibrida (keyword + semantica)
   - Strategie di re-ranking
   - RAG multimodale
   - Metriche di valutazione

### 3.2 Miglioramenti alle Lezioni Esistenti

| Lezione | Miglioramento Raccomandato |
|--------|------------------------|
| 06 - Generazione Testo | Aggiungere esempi di risposta in streaming |
| 07 - Applicazioni Chat | Aggiungere pattern di memoria per conversazioni |
| 08 - Applicazioni di Ricerca | Aggiungere confronto tra database vettoriali |
| 09 - Generazione Immagini | Aggiungere esempi di modifica/variazione immagini |
| 11 - Funzione di Chiamata | Aggiungere chiamate a funzioni parallele |
| 15 - RAG | Aggiungere confronto tra strategie di chunking |
| 17 - Agenti AI | Aggiungere orchestrazione multi-agente |

---

## 4. Modernizzazione API

### 4.1 Pattern API Deprecati (Migrazione Completata)

Tutti i campioni Python e TypeScript **chat** sono stati migrati dalla Chat Completions API alla **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Vecchio Pattern | Nuovo Pattern | Stato |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Completato |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Completato |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` package `client.responses.create()` → `response.output_text` | Completato |
| `df.append()` (pandas) | `pd.concat()` | Completato |

> **Nota:** I campioni Microsoft Foundry Models che usano gli SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) rimangono sulla Model Inference API, che non supporta la Responses API. `AzureOpenAI()` viene mantenuto intenzionalmente dove ancora valido (embeddings e generazione immagini).

### 4.2 Nuove Funzionalità API da Dimostrare

1. **Output Strutturati** (OpenAI)
   - Modalità JSON
   - Chiamata a funzioni con schemi rigidi

2. **Capacità Vision**
   - Analisi immagini con GPT-4o (vision)
   - Prompt multimodali

3. **Strumenti Integrati Responses API** (sostituisce la vecchia Assistants API)
   - Interprete codice
   - Ricerca file
   - Ricerca web e strumenti personalizzati

---

## 5. Miglioramenti dell’Infrastruttura

### 5.1 Miglioramenti CI/CD

Implementato in [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Linting/formattazione Python (Ruff + Black) **obbligatorio** sul modulo delle utility `shared/` mantenuto e **consigliato** sul resto del curriculum, oltre a un passaggio ESLint consigliativo per JavaScript/TypeScript. La baseline illustrativa era:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Scansione della Sicurezza

Implementato in [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Analisi CodeQL per Python e JavaScript/TypeScript (su push, pull request e pianificazione settimanale) più revisione delle dipendenze sulle pull request. La baseline illustrativa era:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Miglioramenti nell’Esperienza Sviluppatore

### 6.1 Miglioramenti DevContainer


Implementato in [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) e [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): il contenitore ora include le estensioni Pylance, il formatter Black, Ruff, ESLint, Prettier e Copilot, abilita il format-on-save collegato alla configurazione Black/Prettier del repository e installa gli strumenti per sviluppatori (`ruff`, `black`, `mypy`, `pytest`) così che il [workflow di qualità del codice](../../../.github/workflows/code-quality.yml) possa essere riprodotto localmente. L'immagine base `mcr.microsoft.com/devcontainers/universal` include già Python e Node, quindi non sono necessarie funzionalità aggiuntive. La baseline illustrativa era:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Playground Interattivo

Considerare l'aggiunta di:
- Notebook Jupyter con chiavi API precompilate (tramite ambiente)
- Demo Gradio/Streamlit per apprendenti visivi
- Quiz interattivi per la valutazione della conoscenza

---

## 7. Supporto Multilingue

### 7.1 Copertura Linguistica Attuale

| Tecnologia | Lezioni Coperte | Stato |
|------------|-----------------|--------|
| Python | Tutte | Completo |
| TypeScript | 06-09, 11 | Parziale |
| JavaScript | 06-08, 11 | Parziale |
| .NET/C# | Alcune | Parziale |

### 7.2 Aggiunte Consigliate

1. **Go** - Crescente negli strumenti AI/ML
2. **Rust** - Applicazioni a prestazioni critiche
3. **Java/Kotlin** - Applicazioni aziendali

---

## 8. Ottimizzazioni delle Prestazioni

### 8.1 Ottimizzazioni a Livello di Codice

1. **Pattern Async/Await**
   - Aggiungere esempi async per elaborazione batch
   - Dimostrare chiamate API concorrenti

2. **Strategie di Caching**
   - Aggiungere esempi di caching di embedding
   - Dimostrare modelli di caching delle risposte

3. **Ottimizzazione dei Token**
   - Aggiungere esempi di utilizzo di tiktoken
   - Dimostrare tecniche di compressione del prompt

### 8.2 Esempi di Ottimizzazione dei Costi

Aggiungere esempi che mostrano:
- Selezione del modello in base alla complessità del compito
- Ingegneria del prompt per efficienza dei token
- Elaborazione batch per operazioni in blocco

---

## 9. Accessibilità e Internazionalizzazione

### 9.1 Stato Attuale della Traduzione

Tutte le traduzioni sono **complete** e generate automaticamente dal [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), che produce e mantiene sincronizzate oltre 50 versioni linguistiche del curriculum con la fonte inglese. I contenuti tradotti sono sotto `translations/` e le immagini localizzate sotto `translated_images/`; la lista completa delle lingue disponibili è pubblicata in cima al README del repository.

| Aspetto | Stato |
|--------|--------|
| Copertura della traduzione | Completa — più di 50 lingue, tutte le lezioni |
| Metodo di traduzione | Automatizzato tramite [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Mantenuto sincronizzato con la fonte inglese | Sì — rigenerato automaticamente |

### 9.2 Miglioramenti di Accessibilità

1. Aggiungere testo alternativo a tutte le immagini
2. Assicurarsi che gli esempi di codice abbiano una corretta evidenziazione della sintassi
3. Aggiungere trascrizioni video a tutti i contenuti video
4. Assicurarsi che il contrasto dei colori sia conforme alle linee guida WCAG

---

## 10. Priorità di Implementazione

### Fase 1: Immediata (Settimane 1-2)
- [x] Risolvere problemi critici di sicurezza
- [x] Aggiungere configurazione per la qualità del codice
- [x] Creare utility condivise
- [x] Documentare le linee guida di sicurezza

### Fase 2: Breve termine (Settimane 3-4)
- [x] Aggiornare pattern API deprecati (Chat Completions → Responses API, Python + TypeScript)
- [ ] Aggiungere suggerimenti di tipo a tutti i file Python (fatto per il modulo mantenuto `shared/`; esempi delle lezioni mantenuti semplici)
- [x] Aggiungere workflow CI/CD per la qualità del codice
- [x] Creare workflow di scansione della sicurezza

### Fase 3: Medio termine (Mesi 2-3)
- [ ] Aggiungere nuova lezione sulla sicurezza
- [ ] Aggiungere lezione sul deployment in produzione
- [x] Migliorare la configurazione del DevContainer
- [ ] Aggiungere demo interattive

### Fase 4: Lungo termine (Mese 4+)
- [ ] Aggiungere lezione avanzata RAG
- [ ] Espandere la copertura linguistica
- [ ] Aggiungere suite di test completa
- [ ] Creare programma di certificazione

---

## Conclusione

Questa roadmap fornisce un approccio strutturato per migliorare il curriculum Generative AI for Beginners. Affrontando questioni di sicurezza, aggiornando le API e aggiungendo contenuti educativi, il corso preparerà meglio gli studenti allo sviluppo di applicazioni AI nel mondo reale.

Per domande o contributi, si prega di aprire un issue nel repository GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->