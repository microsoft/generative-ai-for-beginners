# AGENTS.md

## Panoramica del Progetto

Questo repository contiene un curriculum completo di 21 lezioni che insegna i fondamenti dell'IA Generativa e lo sviluppo di applicazioni. Il corso è pensato per principianti e copre tutto, dai concetti di base alla costruzione di applicazioni pronte per la produzione.

**Tecnologie Chiave:**
- Python 3.9+ con librerie: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript con Node.js e librerie: `openai` (Azure OpenAI tramite endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API e Microsoft Foundry Models (GitHub Models verrà ritirato a fine luglio 2026)
- Jupyter Notebooks per l'apprendimento interattivo
- Dev Containers per un ambiente di sviluppo coerente

**Struttura del Repository:**
- 21 cartelle delle lezioni numerate (00-21) contenenti README, esempi di codice e esercizi
- Diverse implementazioni: esempi in Python, TypeScript e talvolta .NET
- Cartella delle traduzioni con oltre 40 versioni linguistiche
- Configurazione centralizzata tramite file `.env` (usa `.env.copy` come modello)

## Comandi di Configurazione

### Configurazione Iniziale del Repository

```bash
# Clona il repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copia il modello dell'ambiente
cp .env.copy .env
# Modifica .env con le tue chiavi API e gli endpoint
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

# Per gli esempi TypeScript delle singole lezioni, vai alla lezione specifica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurazione Dev Container (Consigliata)

Il repository include una configurazione `.devcontainer` per GitHub Codespaces o VS Code Dev Containers:

1. Apri il repository in GitHub Codespaces o VS Code con l'estensione Dev Containers
2. Il Dev Container eseguirà automaticamente:
   - Installazione delle dipendenze Python da `requirements.txt`
   - Esecuzione dello script post-creazione (`.devcontainer/post-create.sh`)
   - Configurazione del kernel Jupyter

## Flusso di Lavoro per lo Sviluppo

### Variabili di Ambiente

Tutte le lezioni che richiedono accesso API usano variabili di ambiente definite in `.env`:

- `OPENAI_API_KEY` - Per OpenAI API
- `AZURE_OPENAI_API_KEY` - Per Azure OpenAI in Microsoft Foundry (Azure OpenAI Service ora parte di Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint risorsa Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome deployment modello per completamento chat (default corso: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome deployment modello embeddings (default corso: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versione API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Per modelli Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (catalogo modelli multi-fornitore)
- `AZURE_INFERENCE_CREDENTIAL` - Chiave API Microsoft Foundry Models (sostituisce il `GITHUB_TOKEN` in fase di pensionamento)
- `AZURE_INFERENCE_CHAT_MODEL` - Modello non di ragionamento (es. `Llama-3.3-70B-Instruct`) usato negli esempi con `temperature`, poiché i modelli di ragionamento non supportano i controlli di campionamento

### Convenzioni Modello (importante)

- **Modello chat predefinito è `gpt-5-mini`** - un modello di **ragionamento** corrente e non deprecato. Dal 2026 i modelli "mini" con supporto temperatura più vecchi (`gpt-4o-mini`, `gpt-4.1-mini`) sono *deprecati*, quindi il curriculum si standardizza sulla famiglia GPT-5.
- **I modelli di ragionamento rifiutano `temperature` e `top_p`**, e usano `max_output_tokens` (Responses API) / `max_completion_tokens` (completamenti chat) invece di `max_tokens`. Non aggiungere **temperatura**/`top_p`/`max_tokens` negli esempi che chiamano `gpt-5-mini`.
- **Per dimostrare `temperature`**, gli esempi usano un modello **Llama** (`Llama-3.3-70B-Instruct`) tramite l'endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Dirigi i modelli di ragionamento con prompt engineering + controlli di ragionamento invece di manopole di campionamento.
- **Fine-tuning (lezione 18)** mantiene `gpt-4.1-mini`: GPT-5 supporta solo il fine-tuning a rinforzo (RFT), non il fine-tuning supervisionato (SFT) mostrato lì.
- Le lezioni 20 (Mistral) e 21 (Meta) mantengono `temperature`/`max_tokens` perché si rivolgono a modelli Mistral/Llama, che li supportano.

### Eseguire Esempi Python

```bash
# Naviga nella directory della lezione
cd 06-text-generation-apps/python

# Esegui uno script Python
python aoai-app.py
```

### Eseguire Esempi TypeScript

```bash
# Naviga alla directory dell'app TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compila il codice TypeScript
npm run build

# Esegui l'applicazione
npm start
```

### Eseguire Jupyter Notebooks

```bash
# Avvia Jupyter nella radice del repository
jupyter notebook

# Oppure usa VS Code con l'estensione Jupyter
```

### Lavorare con Diversi Tipi di Lezione

- Lezioni **"Learn"**: Focus sulla documentazione README.md e concetti
- Lezioni **"Build"**: Includono esempi di codice funzionante in Python e TypeScript
- Ogni lezione ha un README.md con teoria, walkthrough di codice e link a contenuti video

## Linee Guida per lo Stile del Codice

### Python

- Usa `python-dotenv` per la gestione delle variabili ambiente
- Importa la libreria `openai` per le interazioni API
- Usa `pylint` per il linting (alcuni esempi includono `# pylint: disable=all` per semplicità)
- Segui le convenzioni di denominazione PEP 8
- Conserva le credenziali API nel file `.env`, mai nel codice

### TypeScript

- Usa il pacchetto `dotenv` per le variabili ambiente
- Configurazione TypeScript in `tsconfig.json` per ogni app
- Usa il pacchetto `openai` per Azure OpenAI (puntare il client all'endpoint `/openai/v1/` e chiamare `client.responses.create`); usa `@azure-rest/ai-inference` per Microsoft Foundry Models
- Usa `nodemon` per lo sviluppo con ricarica automatica
- Compila prima di eseguire: `npm run build` poi `npm start`

### Convenzioni Generali

- Mantieni gli esempi di codice semplici ed educativi
- Includi commenti che spiegano concetti chiave
- Il codice di ogni lezione deve essere autonomo ed eseguibile
- Usa una nomenclatura coerente: prefisso `aoai-` per Azure OpenAI, `oai-` per OpenAI API, `githubmodels-` per Microsoft Foundry Models (prefisso legacy ereditato dall’era GitHub Models)

## Linee Guida per la Documentazione

### Stile Markdown

- Tutti gli URL devono essere racchiusi nel formato `[testo](../../url)` senza spazi aggiuntivi
- I link relativi devono iniziare con `./` o `../`
- Tutti i link a domini Microsoft devono includere ID tracciamento: `?WT.mc_id=academic-105485-koreyst`
- Nessuna localizzazione specifica per paese negli URL (evitare `/en-us/`)
- Immagini archiviate nella cartella `./images` con nomi descrittivi
- Usa caratteri inglesi, numeri e trattini nei nomi dei file

### Supporto alla Traduzione

- Il repository supporta oltre 40 lingue tramite GitHub Actions automatizzate
- Le traduzioni sono archiviate nella cartella `translations/`
- Non inviare traduzioni parziali
- Traduzioni automatiche non sono accettate
- Immagini tradotte archiviate nella cartella `translated_images/`

## Test e Validazione

### Controlli Pre-Invio

Questo repository usa GitHub Actions per la validazione. Prima di inviare PR:

1. **Controlla i Link Markdown**:
   ```bash
   # Il workflow validate-markdown.yml verifica:
   # - Percorsi relativi interrotti
   # - ID di tracciamento mancanti sui percorsi
   # - ID di tracciamento mancanti sugli URL
   # - URL con locale paese
   # - URL esterni interrotti
   ```

2. **Test Manuali**:
   - Testa gli esempi Python: attiva il venv ed esegui gli script
   - Testa gli esempi TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifica che le variabili ambiente siano configurate correttamente
   - Controlla che le chiavi API funzionino con gli esempi di codice

3. **Esempi di Codice**:
   - Assicurati che tutto il codice venga eseguito senza errori
   - Testa sia con Azure OpenAI che OpenAI API quando applicabile
   - Verifica che gli esempi funzionino con Microsoft Foundry Models dove supportati

### Nessun Test Automatizzato

Questo è un repository educativo focalizzato su tutorial ed esempi. Non ci sono test unitari o di integrazione da eseguire. La validazione è principalmente:
- Test manuali degli esempi di codice
- GitHub Actions per la validazione Markdown
- Revisione comunitaria dei contenuti educativi

## Linee Guida per le Pull Request

### Prima di Inviare

1. Testa le modifiche di codice sia in Python che in TypeScript quando applicabile
2. Esegui la validazione Markdown (attivata automaticamente sulle PR)
3. Assicurati che gli ID tracciamento siano presenti su tutti gli URL Microsoft
4. Verifica che i link relativi siano validi
5. Controlla che le immagini siano correttamente referenziate

### Formato del Titolo PR

- Usa titoli descrittivi: `[Lesson 06] Correzione errore esempio Python` o `Aggiorna README per lezione 08`
- Fai riferimento ai numeri di issue quando applicabile: `Fixes #123`

### Descrizione PR

- Spiega cosa è stato cambiato e perché
- Collega a issue correlate
- Per modifiche di codice, specifica quali esempi sono stati testati
- Per PR di traduzione, includi tutti i file per una traduzione completa

### Requisiti di Contributo

- Firma la Microsoft CLA (automatico alla prima PR)
- Fai fork del repository nel tuo account prima di fare modifiche
- Una PR per ogni modifica logica (non combinare correzioni non correlate)
- Mantieni le PR focalizzate e piccole quando possibile

## Flussi di Lavoro Comuni

### Aggiungere un Nuovo Esempio di Codice

1. Naviga nella cartella della lezione appropriata
2. Crea l'esempio nella sottocartella `python/` o `typescript/`
3. Segui la convenzione di denominazione: `{provider}-{nome-esempio}.{py|ts|js}`
4. Testa con credenziali API effettive
5. Documenta eventuali nuove variabili ambiente nel README della lezione

### Aggiornare la Documentazione

1. Modifica il README.md nella cartella della lezione
2. Segui le linee guida Markdown (ID tracciamento, link relativi)
3. Gli aggiornamenti delle traduzioni sono gestiti da GitHub Actions (non modificare manualmente)
4. Verifica che tutti i link siano validi

### Lavorare con Dev Containers

1. Il repository include `.devcontainer/devcontainer.json`
2. Lo script post-creazione installa automaticamente le dipendenze Python
3. Estensioni per Python e Jupyter preconfigurate
4. Ambiente basato su `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribuzione e Pubblicazione

Questo è un repository didattico - non esiste un processo di distribuzione. Il curriculum è fruibile tramite:

1. **GitHub Repository**: Accesso diretto a codice e documentazione
2. **GitHub Codespaces**: Ambiente di sviluppo istantaneo con configurazione predefinita
3. **Microsoft Learn**: I contenuti possono essere distribuiti sulla piattaforma ufficiale di apprendimento
4. **docsify**: Sito di documentazione costruito da Markdown (vedi `docsifytopdf.js` e `package.json`)

### Costruire il Sito di Documentazione

```bash
# Genera PDF dalla documentazione (se necessario)
npm run convert
```

## Risoluzione Problemi

### Problemi Comuni

**Errori di Import in Python**:
- Assicurarsi che l'ambiente virtuale sia attivato
- Eseguire `pip install -r requirements.txt`
- Verificare che la versione di Python sia 3.9+

**Errori di Compilazione TypeScript**:
- Eseguire `npm install` nella cartella specifica dell'app
- Verificare che la versione di Node.js sia compatibile
- Pulire `node_modules` e reinstallare se necessario

**Errori di Autenticazione API**:
- Verificare che il file `.env` esista e contenga valori corretti
- Controllare che le chiavi API siano valide e non scadute
- Assicurarsi che gli URL endpoint siano corretti per la propria regione

**Variabili Ambiente Mancanti**:
- Copiare `.env.copy` in `.env`
- Compilare tutti i valori richiesti per la lezione su cui si sta lavorando
- Riavviare l'applicazione dopo aver aggiornato `.env`

## Risorse Aggiuntive

- [Guida alla Configurazione del Corso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Linee Guida per il Contributo](./CONTRIBUTING.md)
- [Codice di Condotta](./CODE_OF_CONDUCT.md)
- [Politica di Sicurezza](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Raccolta di Esempi di Codice Avanzati](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note Specifiche del Progetto

- Questo è un **repository didattico** focalizzato sull'apprendimento, non codice di produzione
- Gli esempi sono intenzionalmente semplici e focalizzati sull'insegnamento dei concetti
- La qualità del codice è bilanciata con la chiarezza educativa
- Ogni lezione è autonoma e può essere completata indipendentemente
- Il repository supporta molteplici fornitori API: Azure OpenAI, OpenAI, Microsoft Foundry Models e fornitori offline come Foundry Local e Ollama
- I contenuti sono multilingue con flussi di lavoro di traduzione automatizzata
- Comunità attiva su Discord per domande e supporto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->