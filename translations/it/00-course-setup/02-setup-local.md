# Configurazione Locale 🖥️

**Usa questa guida se preferisci eseguire tutto sul tuo portatile.**   
Hai due opzioni: **(A) Python nativo + virtual-env** oppure **(B) VS Code Dev Container con Docker**.  
Scegli quella che ti sembra più semplice—entrambe portano alle stesse lezioni.

## 1.  Prerequisiti

| Strumento          | Versione / Note                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (scaricalo da <https://python.org>)                                         |
| **Git**            | Ultima versione (incluso in Xcode / Git per Windows / gestori pacchetti Linux)      |
| **VS Code**        | Opzionale ma consigliato <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Solo* per l’Opzione B. Installazione gratuita: <https://docs.docker.com/desktop/>  |

> 💡 **Consiglio** – Verifica gli strumenti in un terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opzione A – Python Nativo (più veloce)

### Passo 1  Clona questo repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Passo 2 Crea e attiva un ambiente virtuale

```bash
python -m venv .venv          # creane uno
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Il prompt dovrebbe ora iniziare con (.venv)—significa che sei dentro l’ambiente.

### Passo 3 Installa le dipendenze

```bash
pip install -r requirements.txt
```

Passa alla Sezione 3 su [Chiavi API](#3-aggiungi-le-tue-chiavi-api)

## 2. Opzione B – VS Code Dev Container (Docker)

Abbiamo configurato questo repository e corso con un [contenitore di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che ha un runtime universale in grado di supportare Python3, .NET, Node.js e sviluppo Java. La configurazione correlata è definita nel file `devcontainer.json` situato nella cartella `.devcontainer/` alla radice di questo repository.

>**Perché scegliere questa opzione?**
>Ambiente identico a Codespaces; nessuna deriva delle dipendenze.

### Passo 0 Installa i componenti extra

Docker Desktop – verifica che ```docker --version``` funzioni.
Estensione VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Apri il repo in VS Code

File ▸ Apri cartella…  → generative-ai-for-beginners

VS Code rileva .devcontainer/ e mostra una richiesta.

### Passo 2 Riapri nel contenitore

Clicca su “Riapri nel Contenitore”. Docker costruisce l’immagine (≈ 3 minuti la prima volta).
Quando appare il prompt del terminale, sei dentro il contenitore.

## 2.  Opzione C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, oltre ad alcuni pacchetti.
Conda è un gestore di pacchetti, che rende facile configurare e passare tra diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È inoltre utile per installare pacchetti non disponibili tramite `pip`.

### Passo 0  Installa Miniconda

Segui la [guida all’installazione di Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

```bash
conda --version
```

### Passo 1 Crea un ambiente virtuale

Crea un nuovo file ambiente (*environment.yml*). Se stai seguendo tramite Codespaces, crealo nella directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

### Passo 2  Popola il tuo file ambiente

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

### Passo 3 Crea il tuo ambiente Conda

Esegui i comandi sotto nella tua linea di comando/terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Il sotto-percorso .devcontainer si applica solo alle configurazioni di Codespace
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

## 2  Opzione D – Jupyter Classico / Jupyter Lab (nel browser)

> **Per chi è?**  
> Chiunque ami l’interfaccia classica di Jupyter o voglia eseguire notebook senza VS Code.  

### Passo 1  Assicurati che Jupyter sia installato

Per avviare Jupyter localmente, apri il terminale/linea di comando, naviga nella directory del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un’istanza Jupyter e l’URL per accedervi sarà mostrato nella finestra della linea di comando.

Una volta che accederai all’URL, vedrai la struttura del corso e potrai navigare in qualsiasi file `*.ipynb`. Per esempio, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Aggiungi le tue Chiavi API

Mantenere le chiavi API sicure è importante quando si costruisce qualsiasi tipo di applicazione. Raccomandiamo di non salvare mai chiavi API direttamente nel codice. Commettere questi dettagli in un repository pubblico potrebbe causare problemi di sicurezza e costi indesiderati se usati da persone malintenzionate.
Ecco una guida passo passo su come creare un file `.env` per Python e aggiungere le tue credenziali Microsoft Foundry Models:

> **Nota:** GitHub Models (e la sua variabile `GITHUB_TOKEN`) sarà ritirato a fine luglio 2026. Questa guida utilizza invece [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Preferisci lavorare completamente offline? Vedi [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Vai alla tua directory di progetto**: Apri il terminale o prompt dei comandi e naviga nella directory principale del tuo progetto dove vuoi creare il file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea il file `.env`**: Usa il tuo editor di testo preferito per creare un nuovo file chiamato `.env`. Se usi il terminale, puoi usare `touch` (su sistemi Unix) oppure `echo` (su Windows):

   Sistemi basati su Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (es. VS Code, Notepad++ o altro). Aggiungi le seguenti righe, sostituendo i segnaposto con il vero endpoint e la chiave API del tuo progetto Microsoft Foundry:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor.

5. **Installa `python-dotenv`**: Se non l’hai già fatto, installa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili d’ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carica le variabili d'ambiente dal file .env
   load_dotenv()

   # Accedi alle variabili dei modelli Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

È tutto! Hai creato con successo un file `.env`, aggiunto le credenziali Microsoft Foundry Models, e caricato tutto nella tua applicazione Python.

🔐 Non commettere mai il file .env—è già incluso in .gitignore.
Le istruzioni complete fornite dal provider sono in [`providers.md`](03-providers.md).

## 4. Cosa fare dopo?

| Voglio…              | Vai a…                                                                |
|-----------------------|-----------------------------------------------------------------------|
| Iniziare la Lezione 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| Configurare un Provider LLM | [`providers.md`](03-providers.md)                                   |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Risoluzione dei problemi

| Sintomo                                  | Soluzione                                                        |
|-----------------------------------------|-----------------------------------------------------------------|
| `python non trovato`                    | Aggiungi Python al PATH o riapri il terminale dopo l’installazione |
| `pip` non riesce a costruire le ruote (Windows) | `pip install --upgrade pip setuptools wheel` poi riprova.          |
| `ModuleNotFoundError: dotenv`           | Esegui `pip install -r requirements.txt` (l’ambiente non è stato installato). |
| La build di Docker fallisce *No space left* | Docker Desktop ▸ *Impostazioni* ▸ *Risorse* → aumenta lo spazio disco. |
| VS Code continua a chiedere di riaprire | Potresti avere attive entrambe le opzioni; scegline una (venv **o** contenitore)|
| Errori OpenAI 401 / 429                 | Controlla il valore di `OPENAI_API_KEY` / limiti di frequenza delle richieste. |
| Errori usando Conda                      | Installa le librerie Microsoft AI con `conda install -c microsoft azure-ai-ml`  |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->