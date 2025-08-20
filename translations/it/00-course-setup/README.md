<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:08:00+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "it"
}
-->
# Iniziare con questo corso

Siamo molto entusiasti che tu inizi questo corso e scopra cosa ti ispira a creare con l’Intelligenza Artificiale Generativa!

Per garantirti il successo, questa pagina illustra i passaggi per la configurazione, i requisiti tecnici e dove trovare aiuto se necessario.

## Passaggi per la configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Fai il fork di questo repository

[Fai il fork di tutto questo repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare il codice e completare le sfide. Puoi anche [mettere una stella (🌟) a questo repository](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo più facilmente insieme ai repository correlati.

### 2. Crea un codespace

Per evitare problemi di dipendenze durante l’esecuzione del codice, consigliamo di eseguire questo corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Puoi crearlo selezionando l’opzione `Code` sulla tua versione forkata di questo repository e scegliendo l’opzione **Codespaces**.

![Dialogo che mostra i pulsanti per creare un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Conservare le tue API Keys

Mantenere le tue API keys al sicuro è importante quando si sviluppa qualsiasi tipo di applicazione. Ti consigliamo di non memorizzare le API keys direttamente nel codice. Inserirle in un repository pubblico potrebbe causare problemi di sicurezza e anche costi indesiderati se usate da malintenzionati.  
Ecco una guida passo-passo su come creare un file `.env` per Python e aggiungere il `GITHUB_TOKEN`:

1. **Vai alla directory del tuo progetto**: apri il terminale o il prompt dei comandi e spostati nella directory principale del progetto dove vuoi creare il file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea il file `.env`**: usa il tuo editor di testo preferito per creare un nuovo file chiamato `.env`. Se usi la riga di comando, puoi usare `touch` (su sistemi Unix) o `echo` (su Windows):

   Sistemi Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: apri il file `.env` in un editor di testo (ad esempio VS Code, Notepad++ o altro). Aggiungi la seguente riga, sostituendo `your_github_token_here` con il tuo token GitHub reale:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: salva le modifiche e chiudi l’editor.

5. **Installa `python-dotenv`**: se non l’hai già fatto, devi installare il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili d’ambiente nel tuo script Python**: nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili d’ambiente dal file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ecco fatto! Hai creato con successo un file `.env`, aggiunto il tuo token GitHub e caricato tutto nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, devi avere installata una versione di [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per usare il repository, devi quindi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta che hai tutto pronto, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alcuni pacchetti.  
Conda è un gestore di pacchetti che facilita la configurazione e il passaggio tra diversi [ambienti virtuali](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida all’installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Dopo aver installato Miniconda, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non l’hai già fatto).

Successivamente, devi creare un ambiente virtuale. Per farlo con Conda, crea un nuovo file ambiente (_environment.yml_). Se stai seguendo il corso usando Codespaces, crea questo file nella directory `.devcontainer`, quindi `.devcontainer/environment.yml`.

Popola il file ambiente con lo snippet qui sotto:

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

Se riscontri errori usando conda, puoi installare manualmente le Microsoft AI Libraries con il seguente comando nel terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file ambiente specifica le dipendenze necessarie. `<environment-name>` è il nome che vuoi dare al tuo ambiente Conda, mentre `<python-version>` è la versione di Python che vuoi usare, ad esempio `3` per l’ultima versione principale di Python.

Fatto ciò, puoi creare il tuo ambiente Conda eseguendo i comandi seguenti nella riga di comando/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Usare Visual Studio Code con l’estensione di supporto Python

Consigliamo di usare l’editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l’[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. Tuttavia, è solo una raccomandazione e non un requisito obbligatorio.

> **Nota**: Aprendo il repository del corso in VS Code, puoi configurare il progetto all’interno di un container. Questo grazie alla [cartella speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository. Ne parleremo più avanti.

> **Nota**: Una volta clonato e aperto il repository in VS Code, ti verrà automaticamente suggerito di installare un’estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta per usare la versione di Python installata localmente.

### Usare Jupyter nel browser

Puoi anche lavorare al progetto usando l’ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente nel browser. Sia Jupyter classico che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piacevole con funzionalità come completamento automatico, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, apri il terminale/prompt dei comandi, spostati nella directory del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un’istanza di Jupyter e l’URL per accedervi verrà mostrato nella finestra del terminale.

Una volta aperto l’URL, vedrai la struttura del corso e potrai navigare in qualsiasi file `*.ipynb`. Ad esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Eseguire in un container

Un’alternativa a configurare tutto sul tuo computer o in Codespace è usare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La cartella speciale `.devcontainer` nel repository del corso permette a VS Code di configurare il progetto all’interno di un container.  
Al di fuori di Codespaces, questo richiede l’installazione di Docker e, a dire il vero, un po’ di lavoro, quindi consigliamo questa opzione solo a chi ha esperienza con i container.

Uno dei modi migliori per mantenere le tue API keys sicure usando GitHub Codespaces è tramite i Codespace Secrets. Segui la guida su [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.

## Lezioni e requisiti tecnici

Il corso comprende 6 lezioni teoriche e 6 lezioni di coding.

Per le lezioni di coding, utilizziamo il servizio Azure OpenAI. Avrai bisogno di accesso al servizio Azure OpenAI e di una API key per eseguire il codice. Puoi richiedere l’accesso [compilando questa domanda](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mentre aspetti che la tua richiesta venga elaborata, ogni lezione di coding include anche un file `README.md` dove puoi vedere il codice e i risultati.

## Usare il servizio Azure OpenAI per la prima volta

Se è la prima volta che usi il servizio Azure OpenAI, segui questa guida su come [creare e distribuire una risorsa Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usare l’API OpenAI per la prima volta

Se è la prima volta che usi l’API OpenAI, segui la guida su come [creare e usare l’interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontra altri studenti

Abbiamo creato canali nel nostro server ufficiale Discord della [AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un ottimo modo per fare networking con altri imprenditori, sviluppatori, studenti e chiunque voglia migliorare le proprie competenze in Intelligenza Artificiale Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team del progetto sarà presente su questo server Discord per aiutare gli studenti.

## Contribuire

Questo corso è un’iniziativa open source. Se noti aree di miglioramento o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o segnala un [issue su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team del progetto monitorerà tutti i contributi. Contribuire all’open source è un modo fantastico per costruire la tua carriera nell’Intelligenza Artificiale Generativa.

La maggior parte dei contributi richiede di accettare un Contributor License Agreement (CLA) che dichiara che hai il diritto e concedi effettivamente i diritti per usare il tuo contributo. Per dettagli, visita il sito [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci testi in questo repository, assicurati di non usare traduzioni automatiche. Verificheremo le traduzioni tramite la community, quindi offriti solo per traduzioni in lingue in cui sei competente.

Quando invii una pull request, un CLA-bot determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (ad esempio, con etichetta o commento). Segui semplicemente le istruzioni del bot. Dovrai farlo solo una volta per tutti i repository che usano il nostro CLA.

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per maggiori informazioni leggi le FAQ sul Code of Conduct o contatta [Email opencode](opencode@microsoft.com) per domande o commenti.

## Iniziamo

Ora che hai completato i passaggi necessari per seguire questo corso, iniziamo con un’[introduzione all’Intelligenza Artificiale Generativa e ai LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.