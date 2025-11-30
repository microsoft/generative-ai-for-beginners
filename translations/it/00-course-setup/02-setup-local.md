<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:30:10+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "it"
}
-->
# Configurazione Locale 🖥️

**Segui questa guida se preferisci lavorare direttamente sul tuo portatile.**  
Hai due possibilità: **(A) Python nativo + virtual-env** oppure **(B) Dev Container di VS Code con Docker**.  
Scegli quella che ti sembra più semplice—entrambe portano agli stessi contenuti.

## 1.  Prerequisiti

| Strumento           | Versione / Note                                                                      |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (scaricalo da <https://python.org>)                                           |
| **Git**             | Ultima versione (incluso in Xcode / Git per Windows / gestore pacchetti Linux)       |
| **VS Code**         | Facoltativo ma consigliato <https://code.visualstudio.com>                           |
| **Docker Desktop**  | *Solo* per l’Opzione B. Installazione gratuita: <https://docs.docker.com/desktop/>   |

> 💡 **Tip** – Verifica gli strumenti nel terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opzione A – Python Nativo (la più veloce)

### Step 1  Clona questo repository

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 Crea & attiva un ambiente virtuale

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Il prompt ora dovrebbe iniziare con (.venv)—significa che sei dentro l’ambiente virtuale.

### Step 3 Installa le dipendenze

```bash
pip install -r requirements.txt
```

Salta alla Sezione 3 sulle [API keys](../../../00-course-setup)

## 2. Opzione B – Dev Container VS Code (Docker)

Abbiamo preparato questo repository e corso con un [container di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che offre un ambiente universale per Python3, .NET, Node.js e Java. La configurazione si trova nel file `devcontainer.json` nella cartella `.devcontainer/` alla radice del repository.

>**Perché scegliere questa opzione?**
>Ambiente identico a Codespaces; nessun problema di dipendenze.

### Step 0 Installa gli extra

Docker Desktop – verifica che ```docker --version``` funzioni.
Estensione VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Step 1 Apri il repository in VS Code

File ▸ Apri cartella…  → generative-ai-for-beginners

VS Code rileva .devcontainer/ e mostra un messaggio.

### Step 2 Riapri nel container

Clicca su “Reopen in Container”. Docker costruisce l’immagine (≈ 3 min la prima volta).
Quando appare il prompt nel terminale, sei dentro il container.

## 2.  Opzione C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alcuni pacchetti.
Conda è un gestore di pacchetti che semplifica la creazione e la gestione di diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacchetti Python. È utile anche per installare pacchetti non disponibili tramite `pip`.

### Step 0  Installa Miniconda

Segui la [guida di installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

```bash
conda --version
```

### Step 1 Crea un ambiente virtuale

Crea un nuovo file di ambiente (*environment.yml*). Se stai seguendo con Codespaces, crealo nella directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

### Step 2  Compila il file di ambiente

Aggiungi il seguente snippet al tuo `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### Step 3 Crea il tuo ambiente Conda

Esegui i comandi qui sotto nel terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

## 2  Opzione D – Jupyter Classico / Jupyter Lab (nel browser)

> **A chi è rivolto?**  
> Chi preferisce l’interfaccia classica di Jupyter o vuole lavorare sui notebook senza VS Code.  

### Step 1  Assicurati che Jupyter sia installato

Per avviare Jupyter in locale, apri il terminale, vai nella cartella del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà Jupyter e l’URL per accedervi verrà mostrato nel terminale.

Una volta aperto l’URL, vedrai la struttura del corso e potrai navigare tra i file `*.ipynb`. Ad esempio, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Aggiungi le tue API Keys

Proteggere le API keys è fondamentale quando sviluppi applicazioni. Ti consigliamo di non salvare mai le API keys direttamente nel codice. Se le pubblichi in un repository pubblico, rischi problemi di sicurezza e costi indesiderati se qualcuno le usa in modo improprio.
Ecco una guida passo-passo per creare un file `.env` per Python e aggiungere il `GITHUB_TOKEN`:

1. **Vai nella cartella del tuo progetto**: Apri il terminale e spostati nella directory principale del progetto dove vuoi creare il file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea il file `.env`**: Usa il tuo editor preferito per creare un nuovo file chiamato `.env`. Dal terminale puoi usare `touch` (su sistemi Unix) o `echo` (su Windows):

   Sistemi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` con un editor di testo (es. VS Code, Notepad++, o altro). Aggiungi questa riga, sostituendo `your_github_token_here` con il tuo vero token GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor.

5. **Installa `python-dotenv`**: Se non l’hai già fatto, installa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo con `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili d’ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Fatto! Hai creato il file `.env`, aggiunto il tuo token GitHub e lo hai caricato nella tua applicazione Python.

🔐 Non committare mai .env—è già incluso in .gitignore.
Le istruzioni complete per i provider sono in [`providers.md`](03-providers.md).

## 4. E ora?

| Voglio…             | Vai a…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Iniziare la Lezione 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurare un provider LLM | [`providers.md`](03-providers.md)                                       |
| Conoscere altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Risoluzione dei problemi

| Sintomo                                   | Soluzione                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Aggiungi Python al PATH o riapri il terminale dopo l’installazione|
| `pip` non riesce a costruire wheels (Windows) | `pip install --upgrade pip setuptools wheel` e riprova.          |
| `ModuleNotFoundError: dotenv`             | Esegui `pip install -r requirements.txt` (l’ambiente non è stato installato).|
| Errore build Docker *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → aumenta lo spazio su disco.|
| VS Code continua a chiedere di riaprire   | Potresti avere entrambe le opzioni attive; scegli una (venv **o** container)|
| Errori OpenAI 401 / 429                   | Controlla il valore di `OPENAI_API_KEY` / limiti di richieste.   |
| Errori con Conda                          | Installa le librerie Microsoft AI con `conda install -c microsoft azure-ai-ml`|

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.