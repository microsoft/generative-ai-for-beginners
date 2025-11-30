<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T00:48:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "it"
}
-->
# Introduzione a questo corso

Siamo molto entusiasti che tu inizi questo corso e non vediamo l'ora di scoprire cosa ti ispirerà a creare con l'Intelligenza Artificiale Generativa!

Per garantire il tuo successo, questa pagina descrive i passaggi di configurazione, i requisiti tecnici e dove trovare supporto, se necessario.

## Passaggi di configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Fai un fork di questo repository

[Fai un fork di questo intero repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare qualsiasi codice e completare le sfide. Puoi anche [aggiungere una stella (🌟) a questo repository](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo e accedere più facilmente ai repository correlati.

### 2. Crea uno spazio di lavoro

Per evitare problemi di dipendenze durante l'esecuzione del codice, ti consigliamo di seguire questo corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Nel tuo fork: **Code -> Codespaces -> New on main**

![Dialogo che mostra i pulsanti per creare uno spazio di lavoro](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Aggiungi un segreto

1. ⚙️ Icona dell'ingranaggio -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.  
2. Nome OPENAI_API_KEY, incolla la tua chiave, Salva.

### 3. Cosa fare dopo?

| Voglio…             | Vai a…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Iniziare la Lezione 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lavorare offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Configurare un provider LLM | [`providers.md`](03-providers.md)                                        |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Risoluzione dei problemi

| Sintomo                                   | Soluzione                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| La build del container è bloccata > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Il terminale non si è collegato; clicca **+** ➜ *bash*          |
| `401 Unauthorized` da OpenAI              | Chiave `OPENAI_API_KEY` errata o scaduta                        |
| VS Code mostra “Dev container mounting…”  | Aggiorna la scheda del browser—Codespaces a volte perde la connessione |
| Kernel del notebook mancante              | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistemi basati su Unix:

   ```bash
   touch .env
   ```
  
   Windows:

   ```cmd
   echo . > .env
   ```
  
3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (ad esempio, VS Code, Notepad++ o qualsiasi altro editor). Aggiungi la seguente riga al file, sostituendo `your_github_token_here` con il tuo token GitHub effettivo:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```
  
4. **Salva il file**: Salva le modifiche e chiudi l'editor di testo.

5. **Installa `python-dotenv`**: Se non lo hai già fatto, dovrai installare il pacchetto `python-dotenv` per caricare le variabili d'ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```
  
6. **Carica le variabili d'ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili d'ambiente dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```
  
Ecco fatto! Hai creato con successo un file `.env`, aggiunto il tuo token GitHub e lo hai caricato nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, dovrai avere una versione di [Python installata](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per utilizzare il repository, devi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```
  
Una volta che hai tutto configurato, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alcuni pacchetti.  
Conda è un gestore di pacchetti che rende facile configurare e passare tra diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida all'installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Con Miniconda installato, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non lo hai già fatto).

Successivamente, devi creare un ambiente virtuale. Per farlo con Conda, crea un nuovo file di ambiente (_environment.yml_). Se stai seguendo il corso utilizzando Codespaces, crea questo file nella directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

Procedi a popolare il file di ambiente con il seguente snippet:

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
  
Se riscontri errori utilizzando Conda, puoi installare manualmente le librerie Microsoft AI utilizzando il seguente comando in un terminale.

```
conda install -c microsoft azure-ai-ml
```
  
Il file di ambiente specifica le dipendenze necessarie. `<environment-name>` si riferisce al nome che desideri utilizzare per il tuo ambiente Conda, e `<python-version>` è la versione di Python che desideri utilizzare, ad esempio, `3` è l'ultima versione principale di Python.

Con questo completato, puoi creare il tuo ambiente Conda eseguendo i comandi seguenti nella tua linea di comando/terminale:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```
  
Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Utilizzare Visual Studio Code con l'estensione di supporto Python

Consigliamo di utilizzare l'editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l'[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. Tuttavia, è più una raccomandazione che un requisito obbligatorio.

> **Nota**: Aprendo il repository del corso in VS Code, hai la possibilità di configurare il progetto all'interno di un container. Questo è possibile grazie alla directory [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository del corso. Maggiori dettagli in seguito.

> **Nota**: Una volta che cloni e apri la directory in VS Code, ti verrà automaticamente suggerito di installare un'estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta per utilizzare la versione di Python installata localmente.

### Utilizzare Jupyter nel browser

Puoi anche lavorare sul progetto utilizzando l'ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente nel tuo browser. Sia Jupyter classico che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piacevole con funzionalità come completamento automatico, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, vai al terminale/linea di comando, naviga nella directory del corso ed esegui:

```bash
jupyter notebook
```
  
oppure

```bash
jupyterhub
```
  
Questo avvierà un'istanza di Jupyter e l'URL per accedervi verrà mostrato nella finestra della linea di comando.

Una volta che accedi all'URL, dovresti vedere il programma del corso e poter navigare in qualsiasi file `*.ipynb`. Ad esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Eseguire in un container

Un'alternativa alla configurazione di tutto sul tuo computer o su Codespace è utilizzare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La speciale cartella `.devcontainer` all'interno del repository del corso rende possibile per VS Code configurare il progetto in un container. Al di fuori di Codespaces, questo richiederà l'installazione di Docker e, francamente, comporta un po' di lavoro, quindi lo consigliamo solo a chi ha esperienza con i container.

Uno dei modi migliori per mantenere le tue chiavi API sicure quando utilizzi GitHub Codespaces è utilizzare i segreti di Codespace. Segui la guida [Gestione dei segreti di Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.

## Lezioni e requisiti tecnici

Il corso comprende 6 lezioni teoriche e 6 lezioni pratiche.

Per le lezioni pratiche, utilizziamo il servizio Azure OpenAI. Avrai bisogno di accesso al servizio Azure OpenAI e di una chiave API per eseguire questo codice. Puoi richiedere l'accesso [completando questa domanda](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mentre aspetti che la tua domanda venga elaborata, ogni lezione pratica include anche un file `README.md` dove puoi visualizzare il codice e i risultati.

## Utilizzare il servizio Azure OpenAI per la prima volta

Se è la prima volta che lavori con il servizio Azure OpenAI, segui questa guida su come [creare e distribuire una risorsa del servizio Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utilizzare l'API OpenAI per la prima volta

Se è la prima volta che lavori con l'API OpenAI, segui la guida su come [creare e utilizzare l'interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontra altri studenti

Abbiamo creato dei canali nel nostro server ufficiale [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un ottimo modo per fare networking con altri imprenditori, sviluppatori, studenti e chiunque voglia migliorare le proprie competenze nell'Intelligenza Artificiale Generativa.

[![Unisciti al canale Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team del progetto sarà anche su questo server Discord per aiutare gli studenti.

## Contribuisci

Questo corso è un'iniziativa open-source. Se vedi aree di miglioramento o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o segnala un [problema su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team del progetto monitorerà tutti i contributi. Contribuire all'open source è un modo straordinario per costruire la tua carriera nell'Intelligenza Artificiale Generativa.

La maggior parte dei contributi richiede di accettare un Accordo di Licenza per i Contributori (CLA) dichiarando che hai il diritto e, di fatto, concedi a noi i diritti di utilizzare il tuo contributo. Per ulteriori dettagli, visita il sito web [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (ad esempio, con un'etichetta o un commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

Questo progetto ha adottato il [Codice di Condotta Open Source di Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per ulteriori informazioni, leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per eventuali domande o commenti aggiuntivi.

## Iniziamo
Ora che hai completato i passaggi necessari per terminare questo corso, iniziamo con un [introduzione all'AI generativa e ai LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.