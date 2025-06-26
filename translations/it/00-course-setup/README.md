<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:47:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "it"
}
-->
# Iniziare con questo corso

Siamo molto entusiasti che tu inizi questo corso e veda cosa ti ispira a creare con l'AI Generativa!

Per garantire il tuo successo, questa pagina delinea i passaggi di configurazione, i requisiti tecnici e dove ottenere aiuto se necessario.

## Passaggi di configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Forka questo Repository

[Forka l'intero repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare qualsiasi codice e completare le sfide. Puoi anche [aggiungere una stella (🌟) a questo repository](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo e trovare facilmente repository correlati.

### 2. Crea uno spazio di codice

Per evitare problemi di dipendenze quando esegui il codice, ti consigliamo di eseguire questo corso in [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Questo può essere creato selezionando l'opzione `Code` sulla versione forkata di questo repository e selezionando l'opzione **Codespaces**.

![Dialogo che mostra i pulsanti per creare uno spazio di codice](../../../00-course-setup/images/who-will-pay.webp)

### 3. Memorizzare le tue chiavi API

Mantenere le tue chiavi API sicure e protette è importante quando si costruisce qualsiasi tipo di applicazione. Ti consigliamo di non memorizzare direttamente le chiavi API nel tuo codice. Commettere questi dettagli in un repository pubblico potrebbe causare problemi di sicurezza e persino costi indesiderati se utilizzati da un attore malintenzionato.
Ecco una guida passo-passo su come creare un file `.env` per Python e aggiungere il `GITHUB_TOKEN`:

1. **Naviga nella directory del tuo progetto**: Apri il tuo terminale o prompt dei comandi e naviga nella directory principale del tuo progetto dove vuoi creare il file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea il file `.env`**: Usa il tuo editor di testo preferito per creare un nuovo file chiamato `.env`. Se stai usando la linea di comando, puoi usare `touch` (on Unix-based systems) or `echo` (su Windows):

   Sistemi basati su Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (ad esempio, VS Code, Notepad++ o qualsiasi altro editor). Aggiungi la seguente riga al file, sostituendo `your_github_token_here` con il tuo token GitHub reale:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l'editor di testo.

5. **Installa il pacchetto `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` per caricare le variabili d'ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

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

Ecco fatto! Hai creato con successo un file `.env`, aggiunto il tuo token GitHub e caricato nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, dovresti avere una qualche versione di [Python installata](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per utilizzare il repository, devi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta che hai tutto verificato, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, così come alcuni pacchetti.
Conda stesso è un gestore di pacchetti, che rende facile configurare e passare tra diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti che non sono disponibili tramite `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Procedi e popola il tuo file di ambiente con il frammento qui sotto:

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

Se riscontri errori usando conda, puoi installare manualmente le Librerie AI di Microsoft usando il seguente comando in un terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file di ambiente specifica le dipendenze di cui abbiamo bisogno. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` è l'ultima versione principale di Python.

Fatto ciò, puoi procedere e creare il tuo ambiente Conda eseguendo i comandi qui sotto nella tua linea di comando/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Utilizzare Visual Studio Code con l'estensione di supporto Python

Ti consigliamo di utilizzare l'editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l'[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. Tuttavia, questa è più una raccomandazione e non un requisito definitivo.

> **Nota**: Aprendo il repository del corso in VS Code, hai l'opzione di configurare il progetto all'interno di un container. Questo grazie alla [directory speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository del corso. Maggiori dettagli in seguito.

> **Nota**: Una volta clonato e aperto la directory in VS Code, ti suggerirà automaticamente di installare un'estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta per utilizzare la versione di Python installata localmente.

### Utilizzare Jupyter nel browser

Puoi anche lavorare sul progetto utilizzando l'[ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente nel tuo browser. Sia Jupyter classico che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piuttosto piacevole con caratteristiche come il completamento automatico, l'evidenziazione del codice, ecc.

Per avviare Jupyter localmente, vai al terminale/linea di comando, naviga nella directory del corso e esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un'istanza di Jupyter e l'URL per accedervi sarà mostrato nella finestra della linea di comando.

Una volta che accedi all'URL, dovresti vedere il sommario del corso e essere in grado di navigare in qualsiasi file `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` dove puoi visualizzare il codice e i risultati.

## Utilizzare il servizio Azure OpenAI per la prima volta

Se è la prima volta che lavori con il servizio Azure OpenAI, segui questa guida su come [creare e distribuire una risorsa del servizio Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utilizzare l'API OpenAI per la prima volta

Se è la prima volta che lavori con l'API OpenAI, segui la guida su come [creare e utilizzare l'interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontra altri studenti

Abbiamo creato canali nel nostro server ufficiale [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. Questo è un ottimo modo per fare networking con altri imprenditori, costruttori, studenti e chiunque desideri migliorare nell'AI Generativa.

[![Unisciti al canale Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team del progetto sarà anche su questo server Discord per aiutare gli studenti.

## Contribuire

Questo corso è un'iniziativa open-source. Se vedi aree di miglioramento o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registra un [problema su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team del progetto seguirà tutte le contribuzioni. Contribuire all'open source è un modo straordinario per costruire la tua carriera nell'AI Generativa.

La maggior parte delle contribuzioni richiede di accettare un Accordo di Licenza per Contributori (CLA) dichiarando che hai il diritto di e realmente concedi a noi i diritti di utilizzare il tuo contributo. Per i dettagli, visita il [sito web CLA, Accordo di Licenza per Contributori](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci il testo in questo repository, assicurati di non utilizzare la traduzione automatica. Verificheremo le traduzioni tramite la comunità, quindi ti preghiamo di offrirti volontario per le traduzioni solo nelle lingue in cui sei competente.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorare il PR in modo appropriato (ad esempio, etichetta, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

Questo progetto ha adottato il [Codice di Condotta Open Source di Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per ulteriori informazioni, leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Iniziamo

Ora che hai completato i passaggi necessari per completare questo corso, iniziamo con un [introduzione all'AI Generativa e ai LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di essere consapevoli che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.