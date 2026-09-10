# Iniziare con questo corso

Siamo molto entusiasti che tu inizi questo corso e veda cosa ti ispira a costruire con l'IA Generativa!

Per assicurarti il successo, questa pagina illustra i passaggi di configurazione, i requisiti tecnici e dove ottenere aiuto se necessario.

## Passaggi di configurazione

Per iniziare a seguire questo corso, dovrai completare i seguenti passaggi.

### 1. Fai il fork di questo repo

[Fai il fork di questo intero repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) nel tuo account GitHub per poter modificare qualsiasi codice e completare le sfide. Puoi anche [aggiungere una stella (🌟) a questo repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) per trovarlo più facilmente insieme a repo correlati.

### 2. Crea un codespace

Per evitare problemi di dipendenze durante l'esecuzione del codice, consigliamo di eseguire questo corso in un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Nel tuo fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/it/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Aggiungi un segreto

1. ⚙️ Icona ingranaggio -> Command Pallete -> Codespaces : Gestisci segreto utente -> Aggiungi un nuovo segreto.
2. Nome OPENAI_API_KEY, incolla la tua chiave, Salva.

### 3. E adesso?

| Voglio…             | Vai a…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Iniziare la Lezione 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lavorare offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Configurare un fornitore LLM | [`providers.md`](03-providers.md)                                        |
| Incontrare altri studenti | [Unisciti al nostro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Risoluzione dei problemi


| Sintomo                                   | Soluzione                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Build del container bloccato > 10 min     | **Codespaces ➜ “Ricostruisci Container”**                        |
| `python: command not found`               | Terminale non collegato; clicca su **+** ➜ *bash*                |
| `401 Unauthorized` da OpenAI              | `OPENAI_API_KEY` errata o scaduta                                |
| VS Code mostra “Dev container mounting…” | Aggiorna la scheda del browser — Codespaces a volte perde connessione |
| Kernel del notebook mancante               | Menù notebook ➜ **Kernel ▸ Seleziona Kernel ▸ Python 3**         |

   Sistemi basati su Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Modifica il file `.env`**: Apri il file `.env` in un editor di testo (es. VS Code, Notepad++ o qualsiasi altro editor). Aggiungi le seguenti righe al file, sostituendo i segnaposto con il tuo endpoint e la tua chiave Microsoft Foundry Models effettivi (consulta [`providers.md`](03-providers.md) per come ottenerli):

   > **Nota:** I Modelli GitHub (e la relativa variabile `GITHUB_TOKEN`) verranno ritirati a fine luglio 2026. Usa invece i [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salva il file**: Salva le modifiche e chiudi l'editor di testo.

5. **Installa `python-dotenv`**: Se non lo hai già fatto, devi installare il pacchetto `python-dotenv` per caricare le variabili ambiente dal file `.env` nella tua applicazione Python. Puoi installarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carica le variabili ambiente nel tuo script Python**: Nel tuo script Python, usa il pacchetto `python-dotenv` per caricare le variabili ambiente dal file `.env`:

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

Ecco fatto! Hai creato con successo un file `.env`, aggiunto le tue credenziali Microsoft Foundry Models e caricato queste ultime nella tua applicazione Python.

## Come eseguire localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, devi avere una qualche versione di [Python installata](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Per usare il repository, devi clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Una volta che hai tutto scaricato, puoi iniziare!

## Passaggi opzionali

### Installare Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) è un installer leggero per installare [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, e alcuni pacchetti.
Conda è un gestore di pacchetti che rende semplice impostare e passare tra diversi [ambienti virtuali](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacchetti. È utile anche per installare pacchetti non disponibili tramite `pip`.

Puoi seguire la [guida di installazione di MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) per configurarlo.

Dopo aver installato Miniconda, devi clonare il [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se non lo hai già fatto)

Poi devi creare un ambiente virtuale. Per farlo con Conda, crea un nuovo file ambiente (_environment.yml_). Se stai seguendo usando Codespaces, crealo all'interno della cartella `.devcontainer`, quindi `.devcontainer/environment.yml`.

Procedi a popolare il tuo file ambiente con lo snippet qui sotto:

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

Se hai errori usando conda, puoi installare manualmente le Microsoft AI Libraries usando il comando seguente in un terminale.

```
conda install -c microsoft azure-ai-ml
```

Il file ambiente specifica le dipendenze necessarie. `<environment-name>` è il nome che vuoi dare al tuo ambiente Conda, e `<python-version>` è la versione di Python che vuoi usare, ad esempio `3` per la versione principale più recente di Python.

Fatto ciò, puoi creare il tuo ambiente Conda eseguendo i comandi qui sotto nella tua linea di comando/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Il sottopercorso .devcontainer si applica solo alle configurazioni Codespace
conda activate ai4beg
```

Consulta la [guida agli ambienti Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se incontri problemi.

### Usare Visual Studio Code con l'estensione di supporto Python

Raccomandiamo di usare l'editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con l'[estensione di supporto Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installata per questo corso. È però solo una raccomandazione e non un requisito obbligatorio.

> **Nota**: Aprendo il repository del corso in VS Code, hai l'opzione di configurare il progetto all'interno di un container. Questo grazie alla [speciale cartella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente nel repository del corso. Approfondiremo più avanti.

> **Nota**: Una volta clonato e aperto il repository in VS Code, ti verrà automaticamente suggerito di installare un'estensione di supporto Python.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un container, rifiuta questa richiesta per usare la versione di Python installata localmente.

### Usare Jupyter nel Browser

Puoi anche lavorare al progetto usando l'ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direttamente nel browser. Sia Jupyter classico sia [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrono un ambiente di sviluppo molto gradevole con funzionalità come l'autocompletamento, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, apri terminale/linea di comando, spostati nella cartella del corso ed esegui:

```bash
jupyter notebook
```

oppure

```bash
jupyterhub
```

Questo avvierà un'istanza Jupyter e l'URL per accedervi sarà mostrato nella finestra della linea di comando.

Una volta aperto l'URL, vedrai il sommario del corso e potrai navigare tra i file `*.ipynb`. Ad esempio, `08-building-search-applications/python/oai-solution.ipynb`.

### Esecuzione in un container

Un'alternativa alla configurazione sul tuo computer o in Codespace è usare un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La speciale cartella `.devcontainer` nel repository del corso consente a VS Code di configurare il progetto all'interno di un container. Al di fuori di Codespaces, questo richiede l'installazione di Docker e, francamente, comporta un po' di lavoro, quindi lo consigliamo solo a chi ha esperienza con i container.

Uno dei modi migliori per mantenere sicure le tue chiavi API quando usi GitHub Codespaces è usare i Codespace Secrets. Segui la guida [Gestione segreti in Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) per saperne di più.


## Lezioni e requisiti tecnici

Il corso include lezioni "Learn" che spiegano i concetti di IA Generativa e lezioni "Build" con esempi pratici di codice in **Python** e **TypeScript** dove possibile.

Per le lezioni di coding, usiamo Azure OpenAI in Microsoft Foundry. Ti serve un abbonamento Azure e una chiave API. L'accesso è aperto - non serve domanda - quindi puoi [creare una risorsa Microsoft Foundry e distribuire un modello](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) per ottenere il tuo endpoint e la tua chiave.

Ogni lezione di coding include anche un file `README.md` dove puoi vedere codice e output senza eseguire nulla.

## Usare il servizio Azure OpenAI per la prima volta

Se è la prima volta che lavori con il servizio Azure OpenAI, segui questa guida per [creare e distribuire una risorsa Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usare la API OpenAI per la prima volta

Se è la prima volta che lavori con la API OpenAI, segui la guida su come [creare e usare l'interfaccia.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Incontrare altri studenti

Abbiamo creato canali nel nostro server ufficiale [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) per incontrare altri studenti. È un ottimo modo per fare networking con altri imprenditori, sviluppatori, studenti e chiunque voglia fare un salto di qualità nell'IA Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Il team del progetto sarà anche presente su questo server Discord per aiutare gli studenti.

## Contribuire

Questo corso è un'iniziativa open-source. Se vedi aree di miglioramento o problemi, crea una [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o segnala un [problema su GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Il team del progetto tiene traccia di tutti i contributi. Contribuire all'open source è un modo straordinario per costruire la tua carriera nell'IA Generativa.

La maggior parte dei contributi richiede l'accettazione di un accordo di licenza per il contributore (CLA) che dichiara che hai il diritto e effettivamente concedi i diritti di usare il tuo contributo. Per dettagli, visita il [sito CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: quando traduci il testo in questo repo, assicurati di non usare la traduzione automatica. Verificheremo le traduzioni tramite la comunità, quindi offriti solo per traduzioni in lingue che conosci bene.


Quando invii una pull request, un CLA-bot determinerà automaticamente se è necessario fornire un CLA e decorerà la PR di conseguenza (ad esempio, etichetta, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo una sola volta per tutti i repository che utilizzano il nostro CLA.

Questo progetto ha adottato il [Codice di Condotta Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per ulteriori informazioni, leggi le FAQ sul Codice di Condotta o contatta [Email opencode](opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Iniziamo

Ora che hai completato i passaggi necessari per completare questo corso, iniziamo con un [introduzione a Generative AI e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->