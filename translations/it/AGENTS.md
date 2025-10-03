<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:00:53+00:00",
  "source_file": "AGENTS.md",
  "language_code": "it"
}
-->
# AGENTS.md

## Panoramica del Progetto

Questo repository contiene un curriculum completo di 21 lezioni che insegna i fondamenti dell'Intelligenza Artificiale Generativa e lo sviluppo di applicazioni. Il corso è progettato per principianti e copre tutto, dai concetti di base alla creazione di applicazioni pronte per la produzione.

**Tecnologie Chiave:**
- Python 3.9+ con librerie: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript con Node.js e librerie: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Servizio Azure OpenAI, API OpenAI e Modelli GitHub
- Jupyter Notebooks per l'apprendimento interattivo
- Dev Containers per un ambiente di sviluppo coerente

**Struttura del Repository:**
- 21 directory numerate per le lezioni (00-21) contenenti README, esempi di codice e compiti
- Implementazioni multiple: Python, TypeScript e talvolta esempi .NET
- Directory delle traduzioni con versioni in oltre 40 lingue
- Configurazione centralizzata tramite file `.env` (utilizzare `.env.copy` come modello)

## Comandi di Configurazione

### Configurazione Iniziale del Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Configurazione dell'Ambiente Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configurazione Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurazione del Dev Container (Consigliata)

Il repository include una configurazione `.devcontainer` per GitHub Codespaces o VS Code Dev Containers:

1. Apri il repository in GitHub Codespaces o VS Code con l'estensione Dev Containers
2. Il Dev Container configurerà automaticamente:
   - Installazione delle dipendenze Python da `requirements.txt`
   - Esecuzione dello script post-creazione (`.devcontainer/post-create.sh`)
   - Configurazione del kernel Jupyter

## Flusso di Lavoro per lo Sviluppo

### Variabili d'Ambiente

Tutte le lezioni che richiedono accesso alle API utilizzano variabili d'ambiente definite in `.env`:

- `OPENAI_API_KEY` - Per l'API OpenAI
- `AZURE_OPENAI_API_KEY` - Per il Servizio Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL dell'endpoint Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nome del modello di completamento chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome del modello di embedding
- `AZURE_OPENAI_API_VERSION` - Versione API (predefinita: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Per i modelli Hugging Face
- `GITHUB_TOKEN` - Per i Modelli GitHub

### Esecuzione degli Esempi Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Esecuzione degli Esempi TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Esecuzione dei Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Lavorare con Tipi Diversi di Lezioni

- **Lezioni "Learn"**: Si concentrano sulla documentazione README.md e sui concetti
- **Lezioni "Build"**: Includono esempi di codice funzionanti in Python e TypeScript
- Ogni lezione ha un README.md con teoria, walkthrough del codice e link a contenuti video

## Linee Guida per lo Stile del Codice

### Python

- Utilizzare `python-dotenv` per la gestione delle variabili d'ambiente
- Importare la libreria `openai` per le interazioni con l'API
- Utilizzare `pylint` per il linting (alcuni esempi includono `# pylint: disable=all` per semplicità)
- Seguire le convenzioni di denominazione PEP 8
- Conservare le credenziali API nel file `.env`, mai nel codice

### TypeScript

- Utilizzare il pacchetto `dotenv` per le variabili d'ambiente
- Configurazione TypeScript in `tsconfig.json` per ogni app
- Utilizzare `@azure/openai` o `@azure-rest/ai-inference` per i servizi Azure
- Utilizzare `nodemon` per lo sviluppo con auto-reload
- Compilare prima di eseguire: `npm run build` poi `npm start`

### Convenzioni Generali

- Mantenere gli esempi di codice semplici ed educativi
- Includere commenti che spiegano i concetti chiave
- Il codice di ogni lezione deve essere autonomo ed eseguibile
- Utilizzare una denominazione coerente: prefisso `aoai-` per Azure OpenAI, `oai-` per API OpenAI, `githubmodels-` per Modelli GitHub

## Linee Guida per la Documentazione

### Stile Markdown

- Tutti gli URL devono essere racchiusi nel formato `[testo](../../url)` senza spazi extra
- I link relativi devono iniziare con `./` o `../`
- Tutti i link ai domini Microsoft devono includere l'ID di tracciamento: `?WT.mc_id=academic-105485-koreyst`
- Evitare localizzazioni specifiche per paese negli URL (evitare `/en-us/`)
- Le immagini devono essere archiviate nella cartella `./images` con nomi descrittivi
- Utilizzare caratteri inglesi, numeri e trattini nei nomi dei file

### Supporto per le Traduzioni

- Il repository supporta oltre 40 lingue tramite GitHub Actions automatizzati
- Le traduzioni sono archiviate nella directory `translations/`
- Non inviare traduzioni parziali
- Le traduzioni automatiche non sono accettate
- Le immagini tradotte sono archiviate nella directory `translated_images/`

## Test e Validazione

### Controlli Pre-invio

Questo repository utilizza GitHub Actions per la validazione. Prima di inviare PR:

1. **Controllare i Link Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Test Manuale**:
   - Testare gli esempi Python: Attivare venv ed eseguire gli script
   - Testare gli esempi TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificare che le variabili d'ambiente siano configurate correttamente
   - Controllare che le chiavi API funzionino con gli esempi di codice

3. **Esempi di Codice**:
   - Assicurarsi che tutto il codice venga eseguito senza errori
   - Testare sia con Azure OpenAI che con l'API OpenAI quando applicabile
   - Verificare che gli esempi funzionino con i Modelli GitHub dove supportati

### Nessun Test Automatizzato

Questo è un repository educativo focalizzato su tutorial ed esempi. Non ci sono test unitari o di integrazione da eseguire. La validazione è principalmente:
- Test manuale degli esempi di codice
- GitHub Actions per la validazione Markdown
- Revisione comunitaria dei contenuti educativi

## Linee Guida per le Pull Request

### Prima di Inviare

1. Testare le modifiche al codice sia in Python che in TypeScript quando applicabile
2. Eseguire la validazione Markdown (attivata automaticamente su PR)
3. Assicurarsi che gli ID di tracciamento siano presenti su tutti gli URL Microsoft
4. Controllare che i link relativi siano validi
5. Verificare che le immagini siano correttamente referenziate

### Formato del Titolo della PR

- Utilizzare titoli descrittivi: `[Lesson 06] Fix Python example typo` o `Update README for lesson 08`
- Fare riferimento ai numeri delle issue quando applicabile: `Fixes #123`

### Descrizione della PR

- Spiegare cosa è stato modificato e perché
- Collegare alle issue correlate
- Per le modifiche al codice, specificare quali esempi sono stati testati
- Per le PR di traduzione, includere tutti i file per una traduzione completa

### Requisiti per la Contribuzione

- Firmare il Microsoft CLA (automatico alla prima PR)
- Fork del repository sul proprio account prima di apportare modifiche
- Una PR per ogni modifica logica (non combinare correzioni non correlate)
- Mantenere le PR focalizzate e piccole quando possibile

## Flussi di Lavoro Comuni

### Aggiungere un Nuovo Esempio di Codice

1. Navigare nella directory della lezione appropriata
2. Creare l'esempio nella sottodirectory `python/` o `typescript/`
3. Seguire la convenzione di denominazione: `{provider}-{example-name}.{py|ts|js}`
4. Testare con credenziali API reali
5. Documentare eventuali nuove variabili d'ambiente nel README della lezione

### Aggiornare la Documentazione

1. Modificare il README.md nella directory della lezione
2. Seguire le linee guida Markdown (ID di tracciamento, link relativi)
3. Gli aggiornamenti delle traduzioni sono gestiti da GitHub Actions (non modificare manualmente)
4. Testare che tutti i link siano validi

### Lavorare con i Dev Containers

1. Il repository include `.devcontainer/devcontainer.json`
2. Lo script post-creazione installa automaticamente le dipendenze Python
3. Le estensioni per Python e Jupyter sono preconfigurate
4. L'ambiente si basa su `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribuzione e Pubblicazione

Questo è un repository didattico - non esiste un processo di distribuzione. Il curriculum è utilizzato tramite:

1. **Repository GitHub**: Accesso diretto al codice e alla documentazione
2. **GitHub Codespaces**: Ambiente di sviluppo istantaneo con configurazione predefinita
3. **Microsoft Learn**: Il contenuto può essere distribuito sulla piattaforma di apprendimento ufficiale
4. **docsify**: Sito di documentazione costruito da Markdown (vedi `docsifytopdf.js` e `package.json`)

### Creazione del Sito di Documentazione

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Risoluzione dei Problemi

### Problemi Comuni

**Errori di Importazione Python**:
- Assicurarsi che l'ambiente virtuale sia attivato
- Eseguire `pip install -r requirements.txt`
- Controllare che la versione di Python sia 3.9+

**Errori di Compilazione TypeScript**:
- Eseguire `npm install` nella directory dell'app specifica
- Controllare che la versione di Node.js sia compatibile
- Cancellare `node_modules` e reinstallare se necessario

**Errori di Autenticazione API**:
- Verificare che il file `.env` esista e contenga valori corretti
- Controllare che le chiavi API siano valide e non scadute
- Assicurarsi che gli URL degli endpoint siano corretti per la propria regione

**Variabili d'Ambiente Mancanti**:
- Copiare `.env.copy` in `.env`
- Compilare tutti i valori richiesti per la lezione su cui si sta lavorando
- Riavviare l'applicazione dopo aver aggiornato `.env`

## Risorse Aggiuntive

- [Guida alla Configurazione del Corso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Linee Guida per la Contribuzione](./CONTRIBUTING.md)
- [Codice di Condotta](./CODE_OF_CONDUCT.md)
- [Politica di Sicurezza](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collezione di Esempi di Codice Avanzati](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note Specifiche del Progetto

- Questo è un **repository educativo** focalizzato sull'apprendimento, non sul codice di produzione
- Gli esempi sono intenzionalmente semplici e focalizzati sull'insegnamento dei concetti
- La qualità del codice è bilanciata con la chiarezza educativa
- Ogni lezione è autonoma e può essere completata indipendentemente
- Il repository supporta più fornitori di API: Azure OpenAI, OpenAI e Modelli GitHub
- Il contenuto è multilingue con flussi di lavoro di traduzione automatizzati
- Comunità attiva su Discord per domande e supporto

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.