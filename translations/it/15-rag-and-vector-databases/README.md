<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:15:40+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "it"
}
-->
# Recupero Generativo Aumentato (RAG) e Database di Vettori

Nella lezione sulle applicazioni di ricerca, abbiamo appreso brevemente come integrare i tuoi dati nei Modelli di Linguaggio di Grandi Dimensioni (LLM). In questa lezione, approfondiremo i concetti di radicare i tuoi dati nella tua applicazione LLM, la meccanica del processo e i metodi per archiviare i dati, inclusi sia gli embeddings che il testo.

> **Video in arrivo**

## Introduzione

In questa lezione copriremo i seguenti argomenti:

- Un'introduzione al RAG, cos'è e perché viene utilizzato nell'intelligenza artificiale.

- Comprendere cosa sono i database di vettori e crearne uno per la nostra applicazione.

- Un esempio pratico su come integrare il RAG in un'applicazione.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Spiegare l'importanza del RAG nel recupero e nel trattamento dei dati.

- Configurare un'applicazione RAG e radicare i tuoi dati in un LLM

- Integrazione efficace di RAG e Database di Vettori nelle Applicazioni LLM.

## Il nostro scenario: migliorare i nostri LLM con i nostri dati

Per questa lezione, vogliamo aggiungere le nostre note nella startup educativa, che permette al chatbot di ottenere maggiori informazioni sui diversi argomenti. Utilizzando le note che abbiamo, gli studenti saranno in grado di studiare meglio e comprendere i diversi argomenti, rendendo più facile la revisione per gli esami. Per creare il nostro scenario, utilizzeremo:

- `Azure OpenAI:` l'LLM che utilizzeremo per creare il nostro chatbot

- `AI for beginners' lesson on Neural Networks`: questi saranno i dati su cui radicheremo il nostro LLM

- `Azure AI Search` e `Azure Cosmos DB:` database di vettori per archiviare i nostri dati e creare un indice di ricerca

Gli utenti saranno in grado di creare quiz di pratica dalle loro note, schede di revisione e riassumerle in panoramiche concise. Per iniziare, diamo un'occhiata a cosa è il RAG e come funziona:

## Recupero Generativo Aumentato (RAG)

Un chatbot alimentato da un LLM elabora i prompt degli utenti per generare risposte. È progettato per essere interattivo e coinvolge gli utenti su una vasta gamma di argomenti. Tuttavia, le sue risposte sono limitate al contesto fornito e ai suoi dati di addestramento fondamentali. Ad esempio, la conoscenza di GPT-4 si ferma a settembre 2021, il che significa che manca di conoscenze sugli eventi che sono avvenuti dopo questo periodo. Inoltre, i dati utilizzati per addestrare gli LLM escludono informazioni riservate come note personali o il manuale di un prodotto aziendale.

### Come funzionano i RAG (Recupero Generativo Aumentato)

Supponiamo di voler distribuire un chatbot che crea quiz dalle tue note, avrai bisogno di una connessione alla base di conoscenza. È qui che il RAG viene in soccorso. I RAG operano come segue:

- **Base di conoscenza:** Prima del recupero, questi documenti devono essere ingeriti e preprocessati, tipicamente suddividendo documenti grandi in pezzi più piccoli, trasformandoli in embeddings di testo e archiviandoli in un database.

- **Query dell'utente:** l'utente pone una domanda

- **Recupero:** Quando un utente pone una domanda, il modello di embedding recupera informazioni rilevanti dalla nostra base di conoscenza per fornire più contesto che sarà incorporato nel prompt.

- **Generazione Aumentata:** l'LLM migliora la sua risposta basandosi sui dati recuperati. Permette alla risposta generata di essere non solo basata sui dati pre-addestrati ma anche su informazioni rilevanti dal contesto aggiunto. I dati recuperati vengono utilizzati per aumentare le risposte dell'LLM. L'LLM quindi restituisce una risposta alla domanda dell'utente.

L'architettura per i RAG è implementata utilizzando trasformatori costituiti da due parti: un encoder e un decoder. Ad esempio, quando un utente pone una domanda, il testo di input viene 'codificato' in vettori che catturano il significato delle parole e i vettori vengono 'decodificati' nel nostro indice di documenti e generano nuovo testo basato sulla query dell'utente. L'LLM utilizza un modello encoder-decoder per generare l'output.

Due approcci quando si implementa il RAG secondo il documento proposto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sono:

- **_RAG-Sequence_** utilizzando documenti recuperati per prevedere la migliore risposta possibile a una query dell'utente

- **RAG-Token** utilizzando documenti per generare il prossimo token, quindi recuperarli per rispondere alla query dell'utente

### Perché usare i RAG?

- **Ricchezza di informazioni:** assicura che le risposte di testo siano aggiornate e attuali. Pertanto, migliora le prestazioni su compiti specifici del dominio accedendo alla base di conoscenza interna.

- Riduce la fabbricazione utilizzando **dati verificabili** nella base di conoscenza per fornire contesto alle query degli utenti.

- È **economicamente vantaggioso** poiché sono più economici rispetto al fine-tuning di un LLM

## Creare una base di conoscenza

La nostra applicazione si basa sui nostri dati personali, ovvero la lezione sulla Rete Neurale nel curriculum AI For Beginners.

### Database di Vettori

Un database di vettori, a differenza dei database tradizionali, è un database specializzato progettato per archiviare, gestire e cercare vettori incorporati. Archivia rappresentazioni numeriche di documenti. Scomporre i dati in embeddings numerici facilita la comprensione e l'elaborazione dei dati da parte del nostro sistema AI.

Archiviamo i nostri embeddings nei database di vettori poiché gli LLM hanno un limite al numero di token che accettano come input. Poiché non puoi passare l'intero embedding a un LLM, dovremo suddividerli in pezzi e quando un utente pone una domanda, gli embeddings più simili alla domanda saranno restituiti insieme al prompt. La suddivisione in pezzi riduce anche i costi sul numero di token passati attraverso un LLM.

Alcuni popolari database di vettori includono Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Puoi creare un modello Azure Cosmos DB utilizzando Azure CLI con il seguente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dal testo agli embeddings

Prima di archiviare i nostri dati, dovremo convertirli in embeddings vettoriali prima che vengano archiviati nel database. Se stai lavorando con documenti di grandi dimensioni o testi lunghi, puoi suddividerli in base alle query che ti aspetti. La suddivisione in pezzi può essere effettuata a livello di frase o a livello di paragrafo. Poiché la suddivisione in pezzi deriva significati dalle parole circostanti, puoi aggiungere un altro contesto a un pezzo, ad esempio, aggiungendo il titolo del documento o includendo del testo prima o dopo il pezzo. Puoi suddividere i dati come segue:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Una volta suddivisi in pezzi, possiamo quindi incorporare il nostro testo utilizzando diversi modelli di embedding. Alcuni modelli che puoi utilizzare includono: word2vec, ada-002 di OpenAI, Azure Computer Vision e molti altri. La selezione di un modello da utilizzare dipenderà dalle lingue che stai utilizzando, dal tipo di contenuto codificato (testo/immagini/audio), dalla dimensione dell'input che può codificare e dalla lunghezza dell'output dell'embedding.

Un esempio di testo incorporato utilizzando il modello `text-embedding-ada-002` di OpenAI è:

## Recupero e Ricerca Vettoriale

Quando un utente pone una domanda, il retriever la trasforma in un vettore utilizzando il codificatore di query, quindi cerca nel nostro indice di ricerca dei documenti vettori rilevanti nel documento che sono correlati all'input. Una volta fatto, converte sia il vettore di input che i vettori del documento in testo e li passa attraverso l'LLM.

### Recupero

Il recupero avviene quando il sistema cerca rapidamente di trovare i documenti dall'indice che soddisfano i criteri di ricerca. L'obiettivo del retriever è ottenere documenti che verranno utilizzati per fornire contesto e radicare l'LLM sui tuoi dati.

Ci sono diversi modi per eseguire la ricerca all'interno del nostro database, come:

- **Ricerca per parole chiave** - utilizzata per ricerche di testo

- **Ricerca semantica** - utilizza il significato semantico delle parole

- **Ricerca vettoriale** - converte i documenti da testo a rappresentazioni vettoriali utilizzando modelli di embedding. Il recupero verrà effettuato interrogando i documenti le cui rappresentazioni vettoriali sono più vicine alla domanda dell'utente.

- **Ibrido** - una combinazione di ricerca per parole chiave e ricerca vettoriale.

Una sfida con il recupero si presenta quando non c'è una risposta simile alla query nel database, il sistema restituirà quindi le migliori informazioni che possono ottenere, tuttavia, puoi utilizzare tattiche come impostare la distanza massima per la rilevanza o utilizzare una ricerca ibrida che combina sia parole chiave che ricerca vettoriale. In questa lezione utilizzeremo la ricerca ibrida, una combinazione di ricerca vettoriale e per parole chiave. Archivieremo i nostri dati in un dataframe con colonne contenenti i pezzi così come gli embeddings.

### Similarità Vettoriale

Il retriever cercherà nel database di conoscenza embeddings che sono vicini, il vicino più prossimo, poiché sono testi che sono simili. Nello scenario in cui un utente pone una query, viene prima incorporata e poi abbinata a embeddings simili. La misura comune che viene utilizzata per trovare quanto siano simili diversi vettori è la similarità coseno che si basa sull'angolo tra due vettori.

Possiamo misurare la similarità utilizzando altre alternative come la distanza euclidea che è la linea retta tra i punti finali dei vettori e il prodotto scalare che misura la somma dei prodotti degli elementi corrispondenti di due vettori.

### Indice di ricerca

Quando si effettua il recupero, dovremo costruire un indice di ricerca per la nostra base di conoscenza prima di eseguire la ricerca. Un indice archivierà i nostri embeddings e potrà recuperare rapidamente i pezzi più simili anche in un grande database. Possiamo creare il nostro indice localmente utilizzando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Riordinamento

Una volta interrogato il database, potresti aver bisogno di ordinare i risultati dal più rilevante. Un LLM di riordinamento utilizza il Machine Learning per migliorare la rilevanza dei risultati di ricerca ordinandoli dal più rilevante. Utilizzando Azure AI Search, il riordinamento viene fatto automaticamente per te utilizzando un riordinatore semantico. Un esempio di come funziona il riordinamento utilizzando i vicini più prossimi:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Mettere tutto insieme

L'ultimo passaggio è aggiungere il nostro LLM al mix per essere in grado di ottenere risposte che sono radicate sui nostri dati. Possiamo implementarlo come segue:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Valutare la nostra applicazione

### Metriche di valutazione

- Qualità delle risposte fornite assicurando che suonino naturali, fluide e simili a quelle umane

- Radicamento dei dati: valutare se la risposta proviene dai documenti forniti

- Rilevanza: valutare se la risposta corrisponde ed è correlata alla domanda posta

- Fluidità - se la risposta ha senso grammaticalmente

## Casi d'uso per l'utilizzo di RAG (Recupero Generativo Aumentato) e database di vettori

Ci sono molti casi d'uso diversi in cui le chiamate di funzione possono migliorare la tua app come:

- Domanda e risposta: radicare i dati della tua azienda a una chat che può essere utilizzata dai dipendenti per fare domande.

- Sistemi di raccomandazione: dove puoi creare un sistema che corrisponde ai valori più simili, ad esempio film, ristoranti e molti altri.

- Servizi chatbot: puoi archiviare la cronologia delle chat e personalizzare la conversazione in base ai dati dell'utente.

- Ricerca di immagini basata su embeddings vettoriali, utile quando si fa riconoscimento di immagini e rilevamento di anomalie.

## Riepilogo

Abbiamo coperto le aree fondamentali del RAG dall'aggiunta dei nostri dati all'applicazione, alla query dell'utente e all'output. Per semplificare la creazione di RAG, puoi utilizzare framework come Semanti Kernel, Langchain o Autogen.

## Compito

Per continuare il tuo apprendimento del Recupero Generativo Aumentato (RAG) puoi costruire:

- Costruire un front-end per l'applicazione utilizzando il framework di tua scelta

- Utilizzare un framework, sia LangChain che Semantic Kernel, e ricreare la tua applicazione.

Congratulazioni per aver completato la lezione 👏.

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI Generativa!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.