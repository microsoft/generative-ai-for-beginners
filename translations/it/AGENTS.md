# AGENTS.md

## Panoramica del Progetto

Questo repository contiene un curriculum completo di 21 lezioni che insegna le basi dell'IA Generativa e lo sviluppo di applicazioni. Il corso è progettato per principianti e copre tutto, dai concetti di base alla creazione di applicazioni pronte per la produzione.

**Tecnologie Chiave:**
- Python 3.9+ con librerie: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript con Node.js e librerie: `openai` (Azure OpenAI tramite endpoint v1 + API Responses), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API e Microsoft Foundry Models (GitHub Models sarà ritirato entro fine luglio 2026)
- Jupyter Notebooks per apprendimento interattivo
- Dev Containers per un ambiente di sviluppo consistente

**Struttura del Repository:**
- 21 directory numerate delle lezioni (00-21) contenenti README, esempi di codice e compiti
- Implementazioni multiple: esempi Python, TypeScript e talvolta .NET
- Directory traduzioni con oltre 40 versioni in varie lingue
- Configurazione centralizzata tramite file `.env` (usa `.env.copy` come modello)

## Comandi di Installazione

### Configurazione Iniziale del Repository

```bash
# Clona il repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copia il modello di ambiente
cp .env.copy .env
# Modifica il file .env con le tue chiavi API e gli endpoint
```

### Configurazione Ambiente Python

```bash
# Crea ambiente virtuale
python3 -m venv venv

# Attiva ambiente virtuale
# Su macOS/Linux:
source venv/bin/activate
# Su Windows:
venv\Scripts\activate

# Installa dipendenze
pip install -r requirements.txt
```

### Configurazione Node.js/TypeScript

```bash
# Installa le dipendenze a livello root (per gli strumenti di documentazione)
npm install

# Per esempi TypeScript di singole lezioni, naviga alla lezione specifica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurazione Dev Container (Consigliata)

Il repository include una configurazione `.devcontainer` per GitHub Codespaces o VS Code Dev Containers:

1. Apri il repository in GitHub Codespaces o VS Code con l'estensione Dev Containers
2. Il Dev Container eseguirà automaticamente:
   - L'installazione delle dipendenze Python da `requirements.txt`
   - L'esecuzione dello script post-creazione (`.devcontainer/post-create.sh`)
   - La configurazione del kernel Jupyter

## Flusso di Lavoro di Sviluppo

### Variabili d'Ambiente

Tutte le lezioni che necessitano accesso API usano variabili d'ambiente definite in `.env`:

- `OPENAI_API_KEY` - Per OpenAI API
- `AZURE_OPENAI_API_KEY` - Per Azure OpenAI in Microsoft Foundry (Azure OpenAI Service ora parte di Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint risorsa Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome deployment modello per completamento chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome deployment modello per embeddings
- `AZURE_OPENAI_API_VERSION` - Versione API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Per modelli Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (catalogo modelli multi-fornitore)
- `AZURE_INFERENCE_CREDENTIAL` - Chiave API Microsoft Foundry Models (sostituisce il `GITHUB_TOKEN` in pensionamento)

### Esecuzione Esempi Python

```bash
# Naviga alla directory della lezione
cd 06-text-generation-apps/python

# Esegui uno script Python
python aoai-app.py
```

### Esecuzione Esempi TypeScript

```bash
# Naviga alla directory dell'app TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compila il codice TypeScript
npm run build

# Esegui l'applicazione
npm start
```

### Esecuzione Jupyter Notebooks

```bash
# Avvia Jupyter nella radice del repository
jupyter notebook

# Oppure usa VS Code con l'estensione Jupyter
```

### Gestione dei Diversi Tipi di Lezioni

- Lezioni **"Learn"**: focalizzate sulla documentazione README.md e sui concetti
- Lezioni **"Build"**: includono esempi di codice funzionante in Python e TypeScript
- Ogni lezione ha un README.md con teoria, walkthrough del codice e link a contenuti video

## Linee Guida per lo Stile del Codice

### Python

- Usa `python-dotenv` per la gestione delle variabili d'ambiente
- Importa la libreria `openai` per interazioni API
- Usa `pylint` per il linting (alcuni esempi includono `# pylint: disable=all` per semplicità)
- Segui le convenzioni di denominazione PEP 8
- Conserva le credenziali API nel file `.env`, mai nel codice

### TypeScript

- Usa il pacchetto `dotenv` per le variabili d'ambiente
- Configurazione TypeScript in `tsconfig.json` per ogni app
- Usa il pacchetto `openai` per Azure OpenAI (puntare il client all'endpoint `/openai/v1/` e chiamare `client.responses.create`); usa `@azure-rest/ai-inference` per Microsoft Foundry Models
- Usa `nodemon` per lo sviluppo con ricarica automatica
- Compila prima di eseguire: `npm run build` poi `npm start`

### Convenzioni Generali

- Mantieni esempi di codice semplici e didattici
- Includi commenti che spiegano i concetti chiave
- Il codice di ogni lezione dovrebbe essere autonomo ed eseguibile
- Usa denominazioni coerenti: prefisso `aoai-` per Azure OpenAI, `oai-` per OpenAI API, `githubmodels-` per Microsoft Foundry Models (prefisso legacy mantenuto dall'era GitHub Models)

## Linee Guida per la Documentazione

### Stile Markdown

- Tutti gli URL devono essere racchiusi nel formato `[testo](../../url)` senza spazi aggiuntivi
- I link relativi devono iniziare con `./` o `../`
- Tutti i link verso domini Microsoft devono includere l'ID di tracciamento: `?WT.mc_id=academic-105485-koreyst`
- Evita localizzazioni specifiche per paese negli URL (evita `/en-us/`)
- Le immagini sono archiviate nella cartella `./images` con nomi descrittivi
- Usa caratteri inglesi, numeri e trattini nei nomi dei file

### Supporto per la Traduzione

- Il repository supporta oltre 40 lingue tramite GitHub Actions automatizzati
- Le traduzioni sono archiviate nella directory `translations/`
- Non inviare traduzioni parziali
- Non sono accettate traduzioni automatiche
- Le immagini tradotte sono archiviate nella directory `translated_images/`

## Testing e Validazione

### Controlli Pre-Invio

Questo repository utilizza GitHub Actions per la validazione. Prima di inviare PR:

1. **Controlla i Link Markdown**:
   ```bash
   # Il flusso di lavoro validate-markdown.yml verifica:
   # - Percorsi relativi interrotti
   # - ID di tracciamento mancanti sui percorsi
   # - ID di tracciamento mancanti sugli URL
   # - URL con localizzazione per paese
   # - URL esterni interrotti
   ```

2. **Test Manuale**:
   - Testa gli esempi Python: attiva venv ed esegui gli script
   - Testa gli esempi TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifica che le variabili d'ambiente siano configurate correttamente
   - Controlla che le chiavi API funzionino con gli esempi di codice

3. **Esempi di Codice**:
   - Assicurati che tutto il codice venga eseguito senza errori
   - Testa sia con Azure OpenAI che con OpenAI API quando applicabile
   - Verifica che gli esempi funzionino con Microsoft Foundry Models dove supportato

### Nessun Test Automatizzato

Questo è un repository educativo focalizzato su tutorial ed esempi. Non ci sono test unitari o test di integrazione da eseguire. La validazione è principalmente:
- Test manuale degli esempi di codice
- GitHub Actions per la validazione Markdown
- Revisione comunitaria dei contenuti didattici

## Linee Guida per le Pull Request

### Prima di Inviare

1. Testa le modifiche al codice sia in Python che TypeScript quando applicabile
2. Esegui la validazione Markdown (scatenata automaticamente sulle PR)
3. Assicurati che gli ID di tracciamento siano presenti su tutti gli URL Microsoft
4. Verifica che i link relativi siano validi
5. Controlla che le immagini siano correttamente referenziate

### Formato del Titolo PR

- Usa titoli descrittivi: `[Lezione 06] Correggi errore esempio Python` oppure `Aggiorna README per la lezione 08`
- Riferisci i numeri delle issue quando applicabile: `Fixes #123`

### Descrizione PR

- Spiega cosa è stato cambiato e perché
- Inserisci link alle issue correlate
- Per modifiche di codice, specifica quali esempi sono stati testati
- Per PR di traduzione, includi tutti i file per una traduzione completa

### Requisiti per il Contributo

- Firma il CLA Microsoft (automatico alla prima PR)
- Fai fork del repository nel tuo account prima di effettuare modifiche
- Una PR per ogni modifica logica (non combinare correzioni non correlate)
- Mantieni le PR focalizzate e piccole quando possibile

## Flussi di Lavoro Comuni

### Aggiunta di un Nuovo Esempio di Codice

1. Naviga nella directory della lezione appropriata
2. Crea l’esempio nella sottodirectory `python/` o `typescript/`
3. Segui la convenzione di denominazione: `{provider}-{nome-esempio}.{py|ts|js}`
4. Testa con credenziali API reali
5. Documenta ogni nuova variabile d'ambiente nel README della lezione

### Aggiornamento della Documentazione

1. Modifica il README.md nella directory della lezione
2. Segui le linee guida Markdown (ID di tracciamento, link relativi)
3. Le traduzioni vengono gestite da GitHub Actions (non modificare manualmente)
4. Testa che tutti i link siano validi

### Lavorare con Dev Containers

1. Il repository include `.devcontainer/devcontainer.json`
2. Lo script post-creazione installa automaticamente le dipendenze Python
3. Le estensioni per Python e Jupyter sono preconfigurate
4. L'ambiente si basa su `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deploy e Pubblicazione

Questo è un repository di apprendimento - non c'è un processo di deploy. Il curriculum è fruito tramite:

1. **Repository GitHub**: accesso diretto a codice e documentazione
2. **GitHub Codespaces**: ambiente dev istantaneo con setup preconfigurato
3. **Microsoft Learn**: i contenuti possono essere distribuiti sulla piattaforma ufficiale di apprendimento
4. **docsify**: sito di documentazione costruito da Markdown (vedi `docsifytopdf.js` e `package.json`)

### Costruzione del Sito di Documentazione

```bash
# Genera PDF dalla documentazione (se necessario)
npm run convert
```

## Risoluzione Problemi

### Problemi Comuni

**Errori di Importazione Python**:
- Assicurati che l'ambiente virtuale sia attivato
- Esegui `pip install -r requirements.txt`
- Verifica che la versione di Python sia 3.9+

**Errori di Compilazione TypeScript**:
- Esegui `npm install` nella directory specifica dell'app
- Verifica che la versione di Node.js sia compatibile
- Cancella `node_modules` e reinstalla se necessario

**Errori di Autenticazione API**:
- Verifica che il file `.env` esista e contenga valori corretti
- Controlla che le chiavi API siano valide e non scadute
- Assicurati che gli URL endpoint siano corretti per la tua regione

**Variabili d'Ambiente Mancanti**:
- Copia `.env.copy` in `.env`
- Compila tutti i valori richiesti per la lezione su cui stai lavorando
- Riavvia l'applicazione dopo aver aggiornato `.env`

## Risorse Aggiuntive

- [Guida alla Configurazione del Corso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Linee Guida per il Contributo](./CONTRIBUTING.md)
- [Codice di Condotta](./CODE_OF_CONDUCT.md)
- [Politica di Sicurezza](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Raccolta di Codice Avanzato](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note Specifiche del Progetto

- Questo è un **repository educativo** focalizzato sull'apprendimento, non su codice di produzione
- Gli esempi sono intenzionalmente semplici e mirano a insegnare concetti
- La qualità del codice è bilanciata con la chiarezza didattica
- Ogni lezione è autonoma e può essere completata indipendentemente
- Il repository supporta molteplici provider API: Azure OpenAI, OpenAI, Microsoft Foundry Models e provider offline come Foundry Local e Ollama
- Il contenuto è multilingue con flussi di lavoro di traduzione automatizzata
- Comunità attiva su Discord per domande e supporto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->