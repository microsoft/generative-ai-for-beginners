<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:30:31+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "it"
}
-->
# Scelta e Configurazione di un Provider LLM 🔑

Gli esercizi **possono** essere configurati per funzionare con uno o più deployment di Large Language Model (LLM) tramite un provider supportato come OpenAI, Azure o Hugging Face. Questi offrono un _endpoint ospitato_ (API) a cui possiamo accedere in modo programmatico con le credenziali corrette (API key o token). In questo corso, parliamo di questi provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con una vasta gamma di modelli, inclusa la serie principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per i modelli OpenAI con attenzione alle esigenze aziendali
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza

**Dovrai utilizzare i tuoi account per questi esercizi**. Gli esercizi sono facoltativi, quindi puoi scegliere di configurare uno, tutti - o nessuno - dei provider in base ai tuoi interessi. Ecco alcune indicazioni per la registrazione:

| Registrazione | Costo | API Key | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basata su progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Disponibili più modelli |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Richiesta preventiva di accesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segui le istruzioni qui sotto per _configurare_ questo repository per l’uso con diversi provider. Gli esercizi che richiedono un provider specifico avranno uno di questi tag nel nome del file:

- `aoai` - richiede endpoint e chiave Azure OpenAI
- `oai` - richiede endpoint e chiave OpenAI
- `hf` - richiede token Hugging Face

Puoi configurare uno, nessuno o tutti i provider. Gli esercizi collegati daranno semplicemente errore se mancano le credenziali.

## Creare il file `.env`

Si presume che tu abbia già letto le indicazioni sopra, ti sia registrato al provider scelto e abbia ottenuto le credenziali di autenticazione necessarie (API_KEY o token). Nel caso di Azure OpenAI, si presume anche che tu abbia un deployment valido di Azure OpenAI Service (endpoint) con almeno un modello GPT distribuito per chat completion.

Il prossimo passo è configurare le **variabili d’ambiente locali** come segue:

1. Cerca nella cartella principale il file `.env.copy` che dovrebbe avere contenuti simili a questi:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copia quel file in `.env` usando il comando qui sotto. Questo file è _gitignore-d_, quindi mantiene le credenziali al sicuro.

   ```bash
   cp .env.copy .env
   ```

3. Inserisci i valori (sostituisci i segnaposto a destra di `=`) come descritto nella sezione successiva.

4. (Opzione) Se usi GitHub Codespaces, puoi salvare le variabili d’ambiente come _segreti di Codespaces_ associati a questo repository. In questo caso, non sarà necessario configurare un file .env locale. **Tieni presente però che questa opzione funziona solo se usi GitHub Codespaces.** Dovrai comunque configurare il file .env se usi Docker Desktop.

## Compilare il file `.env`

Vediamo rapidamente i nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che hai impostato nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare il servizio su endpoint OpenAI non Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare quel servizio |
| AZURE_OPENAI_ENDPOINT | Questo è l’endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l’endpoint di deployment del modello _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l’endpoint di deployment del modello _text embeddings_ |
| | |

Nota: Le ultime due variabili di Azure OpenAI si riferiscono rispettivamente al modello predefinito per chat completion (text generation) e per la ricerca vettoriale (embeddings). Le istruzioni per impostarle saranno fornite negli esercizi pertinenti.

## Configurare Azure: Dal Portal

I valori di endpoint e chiave di Azure OpenAI si trovano nel [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), quindi partiamo da lì.

1. Vai al [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clicca sull’opzione **Keys and Endpoint** nella barra laterale (menu a sinistra).
1. Clicca su **Show Keys** - dovresti vedere: KEY 1, KEY 2 e Endpoint.
1. Usa il valore di KEY 1 per AZURE_OPENAI_API_KEY
1. Usa il valore di Endpoint per AZURE_OPENAI_ENDPOINT

Ora servono gli endpoint per i modelli specifici che hai distribuito.

1. Clicca sull’opzione **Model deployments** nella barra laterale (menu a sinistra) della risorsa Azure OpenAI.
1. Nella pagina di destinazione, clicca su **Manage Deployments**

Questo ti porterà al sito Azure OpenAI Studio, dove troverai gli altri valori come descritto sotto.

## Configurare Azure: Dallo Studio

1. Vai su [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto sopra.
1. Clicca sulla scheda **Deployments** (barra laterale, sinistra) per vedere i modelli attualmente distribuiti.
1. Se il modello desiderato non è distribuito, usa **Create new deployment** per distribuirlo.
1. Ti servirà un modello _text-generation_ - consigliamo: **gpt-35-turbo**
1. Ti servirà un modello _text-embedding_ - consigliamo **text-embedding-ada-002**

Ora aggiorna le variabili d’ambiente con il _nome del deployment_ usato. Di solito coincide con il nome del modello, a meno che tu non l’abbia cambiato esplicitamente. Ad esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ricordati di salvare il file .env quando hai finito**. Ora puoi chiudere il file e tornare alle istruzioni per eseguire il notebook.

## Configurare OpenAI: Dal Profilo

La tua API key di OpenAI si trova nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai una, puoi registrarti e crearne una. Una volta ottenuta la chiave, puoi usarla per compilare la variabile `OPENAI_API_KEY` nel file `.env`.

## Configurare Hugging Face: Dal Profilo

Il tuo token Hugging Face si trova nel profilo sotto [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non pubblicare o condividere questi token. Crea invece un nuovo token per questo progetto e copialo nel file `.env` sotto la variabile `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente non è una API key, ma viene usato per l’autenticazione, quindi manteniamo questa convenzione per coerenza.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.