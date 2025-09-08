<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:30:49+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "it"
}
-->
# Iniziare con questo corso

Siamo molto entusiasti che tu stia per iniziare questo corso e non vediamo l’ora di scoprire cosa ti ispirerà a creare con l’Intelligenza Artificiale Generativa!

Per aiutarti a partire con il piede giusto, in questa pagina trovi i passaggi per la configurazione, i requisiti tecnici e dove trovare supporto se ne avrai bisogno.

## Passaggi per la configurazione

Per iniziare il corso, dovrai completare i seguenti passaggi.

### 1. Fai il fork di questo repository

[Fai il fork di tutto il repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare il codice e completare le sfide. Puoi anche [aggiungere una stella (🌟) a questo repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per ritrovarlo facilmente insieme ai repository correlati.

### 2. Crea un codespace

Per evitare problemi di dipendenze durante l’esecuzione del codice, ti consigliamo di seguire il corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Nel tuo fork: **Code -> Codespaces -> New on main**

![Finestra di dialogo che mostra i pulsanti per creare un codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Aggiungi un secret

1. ⚙️ Icona ingranaggio -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nome OPENAI_API_KEY, incolla la tua chiave, Salva.

### 3.  E ora?

| Voglio…              | Vai a…                                                                  |
|----------------------|-------------------------------------------------------------------------|
| Iniziare la Lezione 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lavorare offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Configurare un provider LLM | [`providers.md`](providers.md)                                   |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Risoluzione dei problemi

| Sintomo                                   | Soluzione                                                      |
|-------------------------------------------|----------------------------------------------------------------|
| Build del container bloccato > 10 min     | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Il terminale non si è collegato; clicca **+** ➜ *bash*         |
| `401 Unauthorized` da OpenAI              | `OPENAI_API_KEY` errata o scaduta                              |
| VS Code mostra “Dev container mounting…”  | Aggiorna la scheda del browser—Codespaces a volte perde la connessione |
| Kernel notebook mancante                  | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Sistemi Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (ad esempio VS Code, Notepad++ o un altro editor). Aggiungi la seguente riga al file, sostituendo `your_github_token_here` con il tuo vero token GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor di testo.

5. **Installa `python-dotenv`**: Se non l’hai già fatto, dovrai installare il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo con `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili d’ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Fatto! Hai creato con successo un file `.env`, aggiunto il tuo token GitHub e lo hai caricato nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, devi avere una versione di [Python installata](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per utilizzare il repository, devi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta che hai tutto pronto, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alcuni pacchetti.
Conda è un gestore di pacchetti che semplifica la creazione e il passaggio tra diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È anche utile per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida all’installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Dopo aver installato Miniconda, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non l’hai già fatto)

Successivamente, devi creare un ambiente virtuale. Per farlo con Conda, crea un nuovo file di ambiente (_environment.yml_). Se stai seguendo con Codespaces, crealo all’interno della directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

Popola il tuo file di ambiente con il seguente snippet:

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

Se riscontri errori usando conda puoi installare manualmente le librerie Microsoft AI con il seguente comando nel terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file di ambiente specifica le dipendenze necessarie. `<environment-name>` è il nome che vuoi dare al tuo ambiente Conda, e `<python-version>` è la versione di Python che vuoi usare, ad esempio, `3` è l’ultima versione principale di Python.

Fatto questo, puoi creare il tuo ambiente Conda eseguendo i seguenti comandi nel terminale/command line

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Usare Visual Studio Code con l’estensione di supporto Python

Ti consigliamo di usare l’editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l’[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. Tuttavia, si tratta solo di un suggerimento e non di un requisito obbligatorio.

> **Nota**: Aprendo il repository del corso in VS Code, hai la possibilità di configurare il progetto all’interno di un container. Questo grazie alla [cartella speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository del corso. Ne parleremo più avanti.

> **Nota**: Una volta clonato e aperto il repository in VS Code, ti verrà suggerito automaticamente di installare l’estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta per usare la versione di Python installata localmente.

### Usare Jupyter nel browser

Puoi anche lavorare al progetto usando l’[ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente dal browser. Sia Jupyter classico che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piacevole con funzionalità come auto-completamento, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, apri il terminale/command line, vai nella directory del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un’istanza Jupyter e l’URL per accedervi verrà mostrato nella finestra del terminale.

Una volta aperto l’URL, dovresti vedere la struttura del corso e poter navigare in qualsiasi file `*.ipynb`. Ad esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Eseguire in un container

Un’alternativa alla configurazione sul tuo computer o su Codespace è usare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La cartella speciale `.devcontainer` all’interno del repository del corso permette a VS Code di configurare il progetto in un container. Al di fuori di Codespaces, sarà necessario installare Docker e, onestamente, richiede un po’ di lavoro, quindi lo consigliamo solo a chi ha già esperienza con i container.

Uno dei modi migliori per mantenere sicure le tue chiavi API quando usi GitHub Codespaces è tramite i Codespace Secrets. Segui la guida sulla [gestione dei secrets in Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.


## Lezioni e requisiti tecnici

Il corso è composto da 6 lezioni teoriche e 6 lezioni di programmazione.

Per le lezioni di programmazione, utilizziamo Azure OpenAI Service. Avrai bisogno dell’accesso al servizio Azure OpenAI e di una chiave API per eseguire il codice. Puoi richiedere l’accesso [compilando questa domanda](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mentre aspetti che la tua richiesta venga elaborata, ogni lezione di programmazione include anche un file `README.md` dove puoi vedere il codice e i risultati.

## Usare Azure OpenAI Service per la prima volta

Se è la prima volta che lavori con Azure OpenAI Service, segui questa guida su come [creare e distribuire una risorsa Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usare l’API OpenAI per la prima volta

Se è la prima volta che lavori con l’API OpenAI, segui la guida su come [creare e usare l’interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontra altri studenti

Abbiamo creato dei canali nel nostro [server Discord ufficiale della Community AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un ottimo modo per fare networking con altri imprenditori, sviluppatori, studenti e chiunque voglia migliorare le proprie competenze nell’AI Generativa.

[![Unisciti al canale discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Anche il team di progetto sarà presente su questo server Discord per aiutare gli studenti.

## Contribuisci

Questo corso è un’iniziativa open-source. Se noti aree da migliorare o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o segnala una [issue su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team di progetto terrà traccia di tutti i contributi. Contribuire all’open source è un modo fantastico per costruire la tua carriera nell’AI Generativa.

La maggior parte dei contributi richiede di accettare un Contributor License Agreement (CLA) che dichiara che hai il diritto di concedere e concedi effettivamente i diritti di utilizzo del tuo contributo. Per maggiori dettagli, visita il sito [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci i testi in questo repository, assicurati di non utilizzare traduzioni automatiche. Le traduzioni saranno verificate dalla community, quindi offriti solo per le lingue in cui sei davvero competente.

Quando invii una pull request, un CLA-bot determinerà automaticamente se devi fornire un CLA e aggiungerà le etichette appropriate (ad esempio, label, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che usano il nostro CLA.

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per maggiori informazioni leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per domande o commenti.

## Iniziamo!
Ora che hai completato i passaggi necessari per terminare questo corso, iniziamo con una [introduzione all’Intelligenza Artificiale Generativa e ai LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.