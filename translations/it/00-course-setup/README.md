# Iniziare con questo corso

Siamo molto entusiasti che tu inizi questo corso e veda cosa ti ispira a costruire con l'AI Generativa!

Per garantirti il successo, questa pagina descrive i passaggi di configurazione, i requisiti tecnici e dove ottenere aiuto in caso di necessità.

## Passaggi di Configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Fai il fork di questo Repository

[Fai il fork di tutto questo repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sul tuo account GitHub per poter modificare qualsiasi codice e completare le sfide. Puoi anche [aggiungere una ⭐ a questo repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo più facilmente insieme a repo correlati.

### 2. Crea un codespace

Per evitare problemi di dipendenze durante l’esecuzione del codice, ti consigliamo di eseguire questo corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Nel tuo fork: **Code -> Codespaces -> New on main**

![Dialogo che mostra i pulsanti per creare un codespace](../../../translated_images/it/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Aggiungi un segreto

1. ⚙️ Icona ingranaggio -> Command Palette -> Codespaces : Gestisci segreti utente -> Aggiungi un nuovo segreto.
2. Nome OPENAI_API_KEY, incolla la tua chiave, Salva.

### 3. Cosa fare dopo?

| Voglio…               | Vai a…                                                                 |
|-----------------------|------------------------------------------------------------------------|
| Iniziare la Lezione 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Lavorare offline       | [`setup-local.md`](02-setup-local.md)                                  |
| Configurare un Fornitore LLM | [`providers.md`](03-providers.md)                                  |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Risoluzione dei problemi


| Sintomo                                    | Soluzione                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| Costruzione container bloccata > 10 min     | **Codespaces ➜ “Ricostruisci Container”**                       |
| `python: command not found`                  | Il terminale non si è attaccato; clicca **+** ➜ *bash*          |
| `401 Unauthorized` da OpenAI                 | Chiave `OPENAI_API_KEY` errata/scaduta                          |
| VS Code mostra “Dev container mounting…”    | Aggiorna la scheda del browser—Codespaces a volte perde la connessione |
| Kernel del notebook mancante                  | Menu notebook ➜ **Kernel ▸ Seleziona Kernel ▸ Python 3**        |

   Sistemi basati su Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (ad esempio VS Code, Notepad++ o qualsiasi altro editor). Aggiungi le seguenti righe al file, sostituendo i segnaposto con il tuo endpoint e la tua chiave effettiva dei Microsoft Foundry Models (vedi [`providers.md`](03-providers.md) per sapere come ottenerli):

   > **Nota:** GitHub Models (e la sua variabile `GITHUB_TOKEN`) saranno dismessi alla fine di luglio 2026. Usa invece i [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l’editor di testo.

5. **Installa `python-dotenv`**: Se non lo hai già, dovrai installare il pacchetto `python-dotenv` per caricare le variabili di ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili di ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili di ambiente dal file `.env`:

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

Fatto! Hai creato con successo un file `.env`, aggiunto le credenziali Microsoft Foundry Models e caricate nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, è necessario installare una versione di [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per poi usare il repository, devi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta che hai tutto scaricato, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, e alcuni pacchetti.
Conda è un gestore di pacchetti che facilita la configurazione e il passaggio tra diversi [ambienti virtuali](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È comodo anche per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida all’installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Con Miniconda installato, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non l’hai già fatto)

Poi, devi creare un ambiente virtuale. Per farlo con Conda, crea un nuovo file ambiente (_environment.yml_). Se stai seguendo usando Codespaces, crealo nella directory `.devcontainer`, ossia `.devcontainer/environment.yml`.

Procedi a compilare il file ambiente con lo snippet qui sotto:

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

Se ricevi errori usando conda, puoi installare manualmente le Microsoft AI Libraries con questo comando da terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file ambiente specifica le dipendenze necessarie. `<environment-name>` è il nome che vuoi dare al tuo ambiente Conda, e `<python-version>` è la versione di Python, ad esempio `3` per l’ultima versione principale.

Fatto questo, puoi creare il tuo ambiente Conda eseguendo i seguenti comandi nella linea di comando/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Il percorso secondario .devcontainer si applica solo alle configurazioni di Codespace
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Usare Visual Studio Code con l’estensione Python

Per questo corso raccomandiamo di usare l’editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l’[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata. Si tratta però solo di una raccomandazione, non un requisito inderogabile.

> **Nota**: Aprendo il repository del corso in VS Code, puoi decidere di configurare il progetto all’interno di un container. Questo è possibile grazie alla [cartella speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository. Ne parleremo più avanti.

> **Nota**: Una volta che cloni e apri la directory in VS Code, ti verrà automaticamente suggerito di installare l’estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta per utilizzare la versione di Python installata localmente.

### Usare Jupyter nel browser

Puoi anche lavorare sul progetto usando l’ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente nel browser. Sia il classico Jupyter che [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo piacevole con funzionalità come l’autocompletamento, l’evidenziazione del codice, ecc.

Per avviare Jupyter localmente, apri il terminale/linea di comando, naviga nella directory del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Verrà avviata un’istanza Jupyter e l’URL per accedervi sarà mostrato nella finestra della linea di comando.

Una volta aperto l’URL, dovresti vedere l’indice del corso e potrai navigare qualsiasi file `*.ipynb`. Per esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Eseguire in un container

Un’alternativa per evitare di configurare tutto sul computer o su Codespace è usare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La cartella speciale `.devcontainer` nel repository permette a VS Code di configurare il progetto in un container. Fuori da Codespaces, è necessario installare Docker, e francamente, è un po’ complesso, quindi consigliamo questa opzione solo a chi ha esperienza con i container.

Uno dei modi migliori per mantenere sicure le chiavi API usando GitHub Codespaces è utilizzare i Segreti di Codespaces. Segui la guida sulla [gestione segreti in Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.


## Lezioni e Requisiti Tecnici

Il corso include 6 lezioni teoriche e 6 lezioni pratiche di programmazione.

Per le lezioni di programmazione, utilizziamo il servizio Azure OpenAI. Avrai bisogno di accesso al servizio Azure OpenAI e di una chiave API per eseguire il codice. Puoi richiedere l’accesso [completando questa candidatura](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mentre aspetti la risposta alla candidatura, ogni lezione di programmazione include anche un file `README.md` in cui puoi vedere il codice e i risultati.

## Usare il servizio Azure OpenAI per la prima volta

Se è la prima volta che usi il servizio Azure OpenAI, segui questa guida su come [creare e distribuire una risorsa Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usare l’API OpenAI per la prima volta

Se è la prima volta che usi l’API OpenAI, segui la guida su come [creare e usare l’interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontra altri studenti

Abbiamo creato canali nel nostro server ufficiale [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un ottimo modo per fare networking con altri imprenditori, sviluppatori, studenti e chiunque voglia migliorare nelle AI Generativa.

[![Unisciti al canale discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team del progetto sarà anche su questo server Discord per assistere gli studenti.

## Contribuisci

Questo corso è un’iniziativa open source. Se noti aree di miglioramento o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oppure segnala un [issue su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team del progetto monitorerà tutti i contributi. Contribuire all’open source è un modo eccellente per costruire la tua carriera nell’AI Generativa.

La maggior parte dei contributi richiede l’accettazione di un Accordo di Licenza per i Contributori (CLA) che dichiara che hai il diritto e concedi ai diritti di usare il tuo contributo. Per dettagli, visita il sito [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci il testo in questo repo, assicurati di NON utilizzare la traduzione automatica. Verificheremo le traduzioni tramite la community, quindi volonta’ solo in lingue in cui sei competente.

Quando invii una pull request, un CLA-bot deciderà automaticamente se devi firmare un CLA e decorerà la PR di conseguenza (ad esempio con etichetta, commento). Segui semplicemente le istruzioni del bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.


Questo progetto ha adottato il [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per maggiori informazioni leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Iniziamo

Ora che hai completato i passaggi necessari per completare questo corso, iniziamo con un [introduzione all'Intelligenza Artificiale Generativa e LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->