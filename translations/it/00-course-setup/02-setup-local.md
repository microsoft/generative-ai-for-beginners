<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T14:43:18+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "it"
}
-->
# Configurazione Locale 🖥️

**Usa questa guida se preferisci eseguire tutto sul tuo laptop.**  
Hai due opzioni: **(A) Python nativo + virtual-env** oppure **(B) VS Code Dev Container con Docker**.  
Scegli quella che ti sembra più semplice—entrambe portano alle stesse lezioni.

## 1.  Prerequisiti

| Strumento          | Versione / Note                                                                    |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (scaricalo da <https://python.org>)                                        |
| **Git**            | Ultima versione (incluso in Xcode / Git per Windows / gestore pacchetti Linux)    |
| **VS Code**        | Opzionale ma consigliato <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Solo* per l’Opzione B. Installazione gratuita: <https://docs.docker.com/desktop/>|

> 💡 **Suggerimento** – Verifica gli strumenti in un terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opzione A – Python Nativo (la più veloce)

### Passo 1  Clona questo repository

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Passo 2 Crea e attiva un ambiente virtuale

```bash
python -m venv .venv          # crea uno
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Il prompt dovrebbe ora iniziare con (.venv)—significa che sei dentro l’ambiente.

### Passo 3 Installa le dipendenze

```bash
pip install -r requirements.txt
```

Vai direttamente alla Sezione 3 su [API keys](../../../00-course-setup)

## 2. Opzione B – VS Code Dev Container (Docker)

Abbiamo configurato questo repository e corso con un [contenitore di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che ha un runtime universale che supporta Python3, .NET, Node.js e sviluppo Java. La configurazione correlata è definita nel file `devcontainer.json` situato nella cartella `.devcontainer/` alla radice di questo repository.

>**Perché scegliere questa opzione?**  
>Ambiente identico a Codespaces; nessuna deriva delle dipendenze.

### Passo 0 Installa gli extra

Docker Desktop – conferma che ```docker --version``` funzioni.  
Estensione VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Apri il repository in VS Code

File ▸ Apri cartella…  → generative-ai-for-beginners

VS Code rileva .devcontainer/ e mostra un prompt.

### Passo 2 Riapri nel contenitore

Clicca su “Riapri nel contenitore”. Docker costruisce l’immagine (≈ 3 min la prima volta).  
Quando appare il prompt del terminale, sei dentro il contenitore.

## 2.  Opzione C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, e alcuni pacchetti.  
Conda è un gestore di pacchetti che facilita la configurazione e il passaggio tra diversi [ambienti virtuali](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti non disponibili tramite `pip`.

### Passo 0  Installa Miniconda

Segui la [guida all’installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

```bash
conda --version
```

### Passo 1 Crea un ambiente virtuale

Crea un nuovo file ambiente (*environment.yml*). Se stai seguendo usando Codespaces, crealo nella directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

### Passo 2  Popola il file ambiente

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

Esegui i comandi qui sotto nel terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Il sottopercorso .devcontainer si applica solo alle configurazioni di Codespace
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

## 2  Opzione D – Jupyter classico / Jupyter Lab (nel browser)

> **Per chi è?**  
> Per chi ama l’interfaccia classica di Jupyter o vuole eseguire notebook senza VS Code.

### Passo 1  Assicurati che Jupyter sia installato

Per avviare Jupyter localmente, apri il terminale/command line, vai nella cartella del corso, ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un’istanza Jupyter e l’URL per accedervi sarà mostrato nella finestra del terminale.

Una volta che accedi all’URL, dovresti vedere l’indice del corso e poter navigare in qualsiasi file `*.ipynb`. Per esempio, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Aggiungi le tue API Keys

Mantenere le tue API keys sicure è importante quando costruisci qualsiasi tipo di applicazione. Raccomandiamo di non memorizzare le API keys direttamente nel codice. Commettere questi dettagli in un repository pubblico potrebbe causare problemi di sicurezza e costi indesiderati se usati da malintenzionati.  
Ecco una guida passo-passo su come creare un file `.env` per Python e aggiungere il `GITHUB_TOKEN`:

1. **Vai nella cartella del tuo progetto**: Apri il terminale o prompt dei comandi e naviga nella cartella principale del progetto dove vuoi creare il file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea il file `.env`**: Usa il tuo editor di testo preferito per creare un nuovo file chiamato `.env`. Se usi la riga di comando, puoi usare `touch` (su sistemi Unix) o `echo` (su Windows):

   Sistemi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (es. VS Code, Notepad++, o altro). Aggiungi la seguente riga, sostituendo `your_github_token_here` con il tuo token GitHub reale:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor.

5. **Installa `python-dotenv`**: Se non l’hai già fatto, devi installare il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo con `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili d’ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carica le variabili d'ambiente dal file .env
   load_dotenv()

   # Accedi alla variabile GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ecco fatto! Hai creato con successo un file `.env`, aggiunto il tuo token GitHub e caricato tutto nella tua applicazione Python.

🔐 Non commettere mai .env—è già incluso in .gitignore.  
Le istruzioni complete per i provider sono in [`providers.md`](03-providers.md).

## 4. Cosa fare dopo?

| Voglio…             | Vai a…                                                                 |
|---------------------|------------------------------------------------------------------------|
| Iniziare la Lezione 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Configurare un provider LLM | [`providers.md`](03-providers.md)                                  |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Risoluzione dei problemi

| Sintomo                                   | Soluzione                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Aggiungi Python al PATH o riapri il terminale dopo l’installazione|
| `pip` non riesce a costruire wheels (Windows) | `pip install --upgrade pip setuptools wheel` poi riprova.       |
| `ModuleNotFoundError: dotenv`             | Esegui `pip install -r requirements.txt` (l’ambiente non è stato installato). |
| Docker build fallisce *No space left*     | Docker Desktop ▸ *Impostazioni* ▸ *Risorse* → aumenta lo spazio disco. |
| VS Code continua a chiedere di riaprire  | Potresti avere entrambe le opzioni attive; scegline una (venv **o** container)|
| Errori OpenAI 401 / 429                   | Controlla il valore di `OPENAI_API_KEY` / limiti di richiesta.   |
| Errori usando Conda                       | Installa le librerie Microsoft AI con `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->