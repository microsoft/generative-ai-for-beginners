# Scelta e configurazione di un fornitore LLM 🔑

I compiti **possono** essere configurati per lavorare con uno o più modelli di linguaggio di grandi dimensioni (LLM) tramite un fornitore di servizi supportato come OpenAI, Azure o Hugging Face. Questi forniscono un _endpoint ospitato_ (API) a cui possiamo accedere in modo programmato con le credenziali corrette (chiave API o token). In questo corso discutiamo di questi provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelli diversi inclusa la serie principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per modelli OpenAI con focus sulla preparazione aziendale
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) per un endpoint singolo e chiave API per accedere a centinaia di modelli da OpenAI, Meta, Mistral, Cohere, Microsoft e altro (sostituisce GitHub Models, che sarà dismesso alla fine di luglio 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) o [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) se preferisci eseguire modelli completamente offline sul tuo dispositivo, senza necessità di abbonamento cloud

**Dovrai usare i tuoi account per questi esercizi**. I compiti sono opzionali quindi puoi scegliere di configurare uno, tutti, o nessuno dei provider in base ai tuoi interessi. Alcune indicazioni per la registrazione:

| Registrazione | Costo | Chiave API | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basata sul progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Modelli multipli disponibili |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Avvio rapido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Avvio rapido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Devi fare domanda per l'accesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Pagina panoramica del progetto](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Playground Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Livello gratuito disponibile; un solo endpoint + chiave per molti fornitori di modelli |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuito (gira sul tuo dispositivo) | Non richiesto | [CLI/SDK locale](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint completamente offline, compatibile OpenAI |
| | | | | |

Segui le istruzioni qui sotto per _configurare_ questo repository per l'uso con diversi provider. I compiti che richiedono un provider specifico conterranno uno di questi tag nel nome del file:

- `aoai` - richiede endpoint e chiave Azure OpenAI
- `oai` - richiede endpoint e chiave OpenAI
- `hf` - richiede token Hugging Face
- `githubmodels` - richiede endpoint e chiave Microsoft Foundry Models (GitHub Models sarà dismesso alla fine di luglio 2026)

Puoi configurare uno, nessuno o tutti i provider. I compiti correlati segnaleranno errore se mancano le credenziali.

## Creare il file `.env`

Presumiamo che tu abbia già letto le indicazioni sopra, ti sia registrato con il provider pertinente e ottenuto le credenziali di autenticazione richieste (API_KEY o token). Nel caso di Azure OpenAI, presumiamo inoltre che tu abbia un'istanza valida di Azure OpenAI Service (endpoint) con almeno un modello GPT distribuito per la chat completions.

Il passo successivo è configurare le **variabili d'ambiente locali** come segue:

1. Cerca nella cartella principale un file `.env.copy` che dovrebbe contenere il seguente:

   ```bash
   # Provider OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Il servizio Azure OpenAI fa ora parte di Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Predefinito impostato! (versione API GA stabile attuale)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelli Microsoft Foundry (catalogo modelli multi-provider, sostituisce GitHub Models, che sarà ritirato a fine luglio 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copia quel file in `.env` usando il comando sottostante. Questo file è _ignorato da git_, mantenendo i segreti al sicuro.

   ```bash
   cp .env.copy .env
   ```

3. Inserisci i valori (sostituisci i segnaposto sul lato destro di `=`) come descritto nella sezione successiva.

4. (Opzionale) Se usi GitHub Codespaces, hai la possibilità di salvare le variabili d'ambiente come _segreti di Codespaces_ associati a questo repository. In tal caso, non sarà necessario configurare un file .env locale. **Nota che questa opzione funziona solo se usi GitHub Codespaces.** Dovrai comunque configurare il file .env se usi Docker Desktop.

## Popolare il file `.env`

Diamo una rapida occhiata ai nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che configuri nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare il servizio per endpoint OpenAI non Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare quel servizio |
| AZURE_OPENAI_ENDPOINT | Questo è l'endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l'endpoint di deployment per il modello di _generazione testo_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l'endpoint di deployment per il modello di _embedding testo_ |
| AZURE_INFERENCE_ENDPOINT | Questo è l'endpoint per il tuo progetto Microsoft Foundry, usato per Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Questa è la chiave API per il tuo progetto Microsoft Foundry |
| | |

Nota: Le ultime due variabili Azure OpenAI riflettono un modello predefinito rispettivamente per chat completions (generazione testo) e ricerca vettoriale (embedding). Le istruzioni per impostarle saranno definite nei compiti correlati.

## Configurare Azure OpenAI: dal Portale

> **Nota:** Azure OpenAI Service ora fa parte di [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Le risorse e i deployment sono ancora visibili nel portale Azure, ma la gestione quotidiana dei modelli (deployment, playground, monitoraggio) avviene ora nel portale Foundry anziché nel vecchio "Azure OpenAI Studio" standalone.

I valori di endpoint e chiave Azure OpenAI si trovano nel [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), quindi iniziamo da lì.

1. Vai al [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clicca l'opzione **Chiavi e Endpoint** nella barra laterale (menu a sinistra).
1. Clicca **Mostra chiavi** - dovresti vedere: CHIAVE 1, CHIAVE 2 e Endpoint.
1. Usa il valore di CHIAVE 1 per AZURE_OPENAI_API_KEY
1. Usa il valore di Endpoint per AZURE_OPENAI_ENDPOINT

Successivamente, abbiamo bisogno degli endpoint per i modelli specifici che abbiamo distribuito.

1. Clicca l'opzione **Modelli distribuiti** nella barra laterale (menu a sinistra) per la risorsa Azure OpenAI.
1. Nella pagina di destinazione, clicca **Vai al portale Microsoft Foundry** (o **Gestisci deployment**, a seconda del tipo di risorsa)

Questo ti porterà al portale Microsoft Foundry, dove troveremo gli altri valori come descritto di seguito.

## Configurare Azure OpenAI: dal portale Microsoft Foundry

1. Naviga al [portale Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto prima.
1. Clicca la scheda **Deployments** (barra laterale sinistra) per vedere i modelli attualmente distribuiti.
1. Se il modello desiderato non è distribuito, usa **Distribuisci modello** per distribuirlo dal [catalogo modelli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Avrai bisogno di un modello di _generazione testo_ - consigliamo: **gpt-4o-mini**
1. Avrai bisogno di un modello di _embedding testo_ - consigliamo **text-embedding-3-small**

Ora aggiorna le variabili d'ambiente per riflettere il _nome del deployment_ usato. Di solito sarà uguale al nome del modello, a meno che tu non l'abbia cambiato esplicitamente. Per esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Non dimenticare di salvare il file .env quando hai finito**. Ora puoi uscire dal file e tornare alle istruzioni per eseguire il notebook.

## Configurare OpenAI: dal profilo

La tua chiave API OpenAI si trova nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai uno, puoi registrarti e creare una chiave API. Una volta ottenuta la chiave, puoi usarla per popolare la variabile `OPENAI_API_KEY` nel file `.env`.

## Configurare Hugging Face: dal profilo

Il tuo token Hugging Face si trova nel tuo profilo sotto [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non pubblicare o condividere questi pubblicamente. Invece, crea un nuovo token per l'uso in questo progetto e copialo nel file `.env` nella variabile `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente non è una chiave API ma viene usata per l'autenticazione, quindi manteniamo questa denominazione per coerenza.

## Configurare Microsoft Foundry Models: dal Portale

> **Nota:** GitHub Models sarà dismesso alla fine di luglio 2026. Microsoft Foundry Models è la sostituzione diretta, offrendo lo stesso catalogo modelli free-to-try e l'esperienza SDK Azure AI Inference / OpenAI SDK.

1. Vai a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) e crea (o apri) un progetto Foundry.
1. Sfoglia il [catalogo modelli](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) e distribuisci un modello, ad esempio `gpt-4o-mini`.
1. Nella pagina **Panoramica** del progetto, copia **endpoint** e **chiave API**.
1. Usa il valore endpoint per `AZURE_INFERENCE_ENDPOINT` e il valore chiave per `AZURE_INFERENCE_CREDENTIAL` nel tuo file `.env`.

## Provider Offline / Locali

Se preferisci non usare affatto un abbonamento cloud, puoi eseguire modelli aperti compatibili direttamente sul tuo dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime Microsoft sul dispositivo. Seleziona automaticamente il miglior provider di esecuzione (NPU, GPU o CPU) e espone un endpoint compatibile OpenAI, così puoi riutilizzare la maggior parte del codice di esempio di questo corso con modifiche minime. Consulta la [documentazione Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) per iniziare, o installa con `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - un'alternativa popolare per eseguire localmente modelli aperti come Llama, Phi, Mistral e Gemma.


Consulta [Lezione 19: Costruire con SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) per esempi pratici che utilizzano entrambe le opzioni.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->