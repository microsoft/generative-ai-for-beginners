# Iniziare con questo corso

Siamo molto entusiasti che tu inizi questo corso e veda cosa ti ispira a costruire con l'IA Generativa!

Per assicurarti il successo, questa pagina illustra i passaggi di configurazione, i requisiti tecnici e dove ottenere aiuto se necessario.

## Passaggi di configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Fork di questo Repo

[Fork dell’intero repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare qualsiasi codice e completare le sfide. Puoi anche [aggiungere una stella (🌟) a questo repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo più facilmente insieme ai repos correlati.

### 2. Crea un codespace

Per evitare problemi di dipendenze durante l’esecuzione del codice, raccomandiamo di eseguire questo corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Nel tuo fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/it/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Aggiungi un secret

1. ⚙️ Icona ingranaggio -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.  
2. Nome OPENAI_API_KEY, incolla la tua chiave, Salva.

### 3.  Cosa fare dopo?

| Voglio…             | Vai a…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| Iniziare la Lezione 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lavorare offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Configurare un fornitore LLM | [`providers.md`](03-providers.md)                                   |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Risoluzione dei problemi

| Sintomo                                   | Soluzione                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| Costruzione del container bloccata > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Il terminale non si è collegato; clicca **+** ➜ *bash*          |
| `401 Unauthorized` da OpenAI              | `OPENAI_API_KEY` errata / scaduta                               |
| VS Code mostra “Dev container mounting…”  | Ricarica la scheda del browser—Codespaces a volte perde connessione |
| Kernel del notebook mancante              | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sistemi basati su Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (es. VS Code, Notepad++ o altro editor). Aggiungi la seguente riga nel file, sostituendo `your_github_token_here` con il tuo token GitHub effettivo:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor di testo.

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

Ecco fatto! Hai creato con successo un file `.env`, aggiunto il token GitHub e caricato il tutto nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, devi avere una versione di [Python installata](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per utilizzare il repository, devi quindi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta scaricato tutto, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installatore leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, e alcuni pacchetti.  
Conda è un gestore di pacchetti che rende facile configurare e passare tra diversi [**ambienti virtuali**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida all’installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Con Miniconda installato, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non lo hai già fatto).

Poi crea un ambiente virtuale. Per farlo con Conda, crea un nuovo file ambiente (_environment.yml_). Se usi Codespaces, crea questo file nella cartella `.devcontainer`, quindi `.devcontainer/environment.yml`.

Prosegui popolando il file ambiente con il seguente snippet:

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

Se riscontri errori usando conda, puoi installare manualmente le Microsoft AI Libraries con il comando seguente nel terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file ambiente specifica le dipendenze necessarie. `<environment-name>` si riferisce al nome che vuoi dare all’ambiente Conda, mentre `<python-version>` è la versione di Python che vuoi usare, per esempio `3` per la versione maggiore più recente di Python.

Fatto ciò, puoi creare l’ambiente Conda eseguendo i comandi seguenti nella linea di comando/terminale:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Il percorso secondario .devcontainer si applica solo alle configurazioni di Codespace
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se hai problemi.

### Usare Visual Studio Code con l’estensione di supporto Python

Consigliamo di usare l’editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l’[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. È però solo un consiglio, non un requisito obbligatorio.

> **Nota**: Aprendo il repository del corso in VS Code, puoi configurare il progetto dentro un container. Questo grazie alla [cartella speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository del corso. Ne parleremo più avanti.

> **Nota**: Una volta clonato e aperto il progetto in VS Code, ti verrà automaticamente suggerito di installare l’estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta se vuoi usare la versione locale di Python installata sul tuo computer.

### Usare Jupyter nel browser

Puoi anche lavorare al progetto usando l’ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente dal browser. Sia Jupyter classico che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piacevole con completamento automatico, evidenziazione del codice ecc.

Per avviare Jupyter localmente, vai al terminale e naviga alla cartella del corso, quindi esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un’istanza di Jupyter e mostrerà l’URL per accedervi nella finestra del terminale.

Accedendo a questo URL, vedrai la panoramica del corso e potrai navigare in qualsiasi file `*.ipynb`. Per esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Eseguire in un container

Come alternativa all’impostazione sul tuo computer o in Codespace, puoi usare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La cartella speciale `.devcontainer` nel repository del corso permette a VS Code di impostare il progetto dentro un container.  
Fuori da Codespaces, questo richiede l’installazione di Docker e comporta un po’ di lavoro, quindi lo consigliamo solo a chi ha esperienza con i container.

Uno dei modi migliori per mantenere sicure le tue chiavi API quando usi GitHub Codespaces è tramite i Codespace Secrets. Segui la guida su [gestione segreti in Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.

## Lezioni e requisiti tecnici

Il corso comprende 6 lezioni concettuali e 6 lezioni pratiche di programmazione.

Per le lezioni di programmazione, usiamo Azure OpenAI Service. Hai bisogno di accesso al servizio Azure OpenAI e di una chiave API per eseguire il codice. Puoi richiedere l’accesso [completando questa domanda](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mentre aspetti che la tua domanda venga processata, ogni lezione di programmazione include anche un file `README.md` dove puoi vedere il codice e gli output.

## Usare l’Azure OpenAI Service per la prima volta

Se è la prima volta che usi Azure OpenAI Service, segui questa guida su come [creare e distribuire una risorsa Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usare l’API OpenAI per la prima volta

Se è la prima volta che utilizzi l’API OpenAI, segui la guida su come [creare e usare l’interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontrare altri studenti

Abbiamo creato canali nel nostro server ufficiale [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un modo eccellente per fare rete con imprenditori, sviluppatori, studenti e chiunque voglia migliorare in Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team di progetto sarà presente anche su questo server Discord per assistere gli studenti.

## Contribuire

Questo corso è un’iniziativa open-source. Se vedi aree di miglioramento o problemi, per favore crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o apri un [issue GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team di progetto traccerà tutti i contributi. Contribuire all’open source è un modo fantastico per costruire la tua carriera nell’IA Generativa.

La maggior parte dei contributi richiede di accettare un Contributor License Agreement (CLA) che dichiara che hai il diritto di concedere i diritti legali per usare il tuo contributo. Per dettagli, visita il sito [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci il testo in questo repo, assicurati di non usare traduzioni automatiche. Verificheremo le traduzioni tramite la community, quindi offri il tuo contributo solo per le lingue in cui sei competente.

Quando invii una pull request, un bot CLA determinerà automaticamente se devi fornire un CLA e decorerà la PR di conseguenza (es. etichetta, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo una sola volta per tutti i repository che usano il nostro CLA.

Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per maggiori informazioni leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per domande o commenti aggiuntivi.

## Iniziamo!
Ora che hai completato i passaggi necessari per completare questo corso, iniziamo con un [introduzione a Generative AI e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale da parte di un esperto umano. Non ci assumiamo alcuna responsabilità per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->