<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:30:58+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "it"
}
-->
# Framework per Reti Neurali

Come abbiamo già imparato, per poter addestrare reti neurali in modo efficiente dobbiamo fare due cose:

* Operare su tensori, ad esempio moltiplicare, sommare e calcolare alcune funzioni come sigmoid o softmax
* Calcolare i gradienti di tutte le espressioni, per poter eseguire l’ottimizzazione tramite discesa del gradiente

Mentre la libreria `numpy` può gestire la prima parte, abbiamo bisogno di un meccanismo per calcolare i gradienti. Nel nostro framework sviluppato nella sezione precedente abbiamo dovuto programmare manualmente tutte le funzioni derivate all’interno del metodo `backward`, che esegue la backpropagation. Idealmente, un framework dovrebbe darci la possibilità di calcolare i gradienti di *qualsiasi espressione* che possiamo definire.

Un altro aspetto importante è poter eseguire i calcoli su GPU, o su altre unità di calcolo specializzate, come TPU. L’addestramento di reti neurali profonde richiede *molti* calcoli, e poter parallelizzare questi calcoli su GPU è fondamentale.

> ✅ Il termine 'parallelizzare' significa distribuire i calcoli su più dispositivi.

Attualmente, i due framework neurali più popolari sono: TensorFlow e PyTorch. Entrambi offrono un’API a basso livello per operare con tensori sia su CPU che su GPU. Sopra l’API a basso livello, esiste anche un’API di livello più alto, chiamata rispettivamente Keras e PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| PyTorch

Le **API a basso livello** in entrambi i framework permettono di costruire i cosiddetti **grafi computazionali**. Questo grafo definisce come calcolare l’output (di solito la funzione di perdita) dati i parametri di input, e può essere eseguito su GPU, se disponibile. Ci sono funzioni per differenziare questo grafo computazionale e calcolare i gradienti, che possono poi essere usati per ottimizzare i parametri del modello.

Le **API di alto livello** considerano le reti neurali come una **sequenza di layer**, e rendono molto più semplice costruire la maggior parte delle reti neurali. L’addestramento del modello di solito richiede di preparare i dati e poi chiamare una funzione `fit` per eseguire il training.

L’API di alto livello permette di costruire reti neurali tipiche molto rapidamente senza preoccuparsi di molti dettagli. Allo stesso tempo, l’API a basso livello offre molto più controllo sul processo di addestramento, ed è quindi molto usata nella ricerca, quando si lavora con nuove architetture di reti neurali.

È anche importante capire che si possono usare entrambe le API insieme, ad esempio si può sviluppare la propria architettura di layer usando l’API a basso livello, e poi usarla all’interno di una rete più grande costruita e addestrata con l’API di alto livello. Oppure si può definire una rete con l’API di alto livello come sequenza di layer, e poi usare un proprio ciclo di addestramento a basso livello per eseguire l’ottimizzazione. Entrambe le API condividono gli stessi concetti di base e sono progettate per funzionare bene insieme.

## Apprendimento

In questo corso offriamo la maggior parte dei contenuti sia per PyTorch che per TensorFlow. Puoi scegliere il framework che preferisci e seguire solo i notebook corrispondenti. Se non sei sicuro su quale framework scegliere, leggi alcune discussioni online riguardo **PyTorch vs. TensorFlow**. Puoi anche dare un’occhiata a entrambi i framework per capire meglio.

Quando possibile, useremo le API di alto livello per semplicità. Tuttavia, riteniamo importante capire come funzionano le reti neurali dalle basi, quindi all’inizio lavoreremo con l’API a basso livello e i tensori. Se però vuoi partire velocemente e non vuoi perdere tempo con questi dettagli, puoi saltare direttamente ai notebook con l’API di alto livello.

## ✍️ Esercizi: Framework

Continua il tuo apprendimento nei seguenti notebook:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Dopo aver padroneggiato i framework, riepiloghiamo il concetto di overfitting.

# Overfitting

L’overfitting è un concetto estremamente importante nel machine learning, ed è fondamentale comprenderlo bene!

Considera il seguente problema di approssimare 5 punti (rappresentati da `x` nei grafici sottostanti):

!linear | overfit
-------------------------|--------------------------
**Modello lineare, 2 parametri** | **Modello non lineare, 7 parametri**
Errore di training = 5.3 | Errore di training = 0
Errore di validazione = 5.1 | Errore di validazione = 20

* A sinistra vediamo una buona approssimazione con una retta. Poiché il numero di parametri è adeguato, il modello coglie correttamente la distribuzione dei punti.
* A destra, il modello è troppo potente. Poiché abbiamo solo 5 punti e il modello ha 7 parametri, può adattarsi in modo da passare esattamente per tutti i punti, azzerando l’errore di training. Tuttavia, questo impedisce al modello di capire il pattern corretto dietro i dati, quindi l’errore di validazione è molto alto.

È molto importante trovare un giusto equilibrio tra la complessità del modello (numero di parametri) e il numero di campioni di training.

## Perché si verifica l’overfitting

  * Dati di training insufficienti
  * Modello troppo complesso
  * Troppo rumore nei dati di input

## Come rilevare l’overfitting

Come si vede dal grafico sopra, l’overfitting si può riconoscere da un errore di training molto basso e un errore di validazione alto. Normalmente durante l’addestramento vedremo sia l’errore di training che quello di validazione diminuire, poi a un certo punto l’errore di validazione potrebbe smettere di diminuire e iniziare a salire. Questo è un segnale di overfitting, e indica che probabilmente dovremmo fermare l’addestramento a questo punto (o almeno salvare uno snapshot del modello).

overfitting

## Come prevenire l’overfitting

Se noti che si verifica l’overfitting, puoi fare una delle seguenti cose:

 * Aumentare la quantità di dati di training
 * Ridurre la complessità del modello
 * Usare qualche tecnica di regolarizzazione, come Dropout, che vedremo più avanti.

## Overfitting e compromesso Bias-Varianza

L’overfitting è in realtà un caso di un problema più generale in statistica chiamato compromesso Bias-Varianza. Se consideriamo le possibili fonti di errore nel nostro modello, possiamo distinguere due tipi di errori:

* Gli **errori di bias** sono causati dal fatto che il nostro algoritmo non riesce a catturare correttamente la relazione tra i dati di training. Questo può succedere se il modello non è abbastanza potente (**underfitting**).
* Gli **errori di varianza** sono causati dal fatto che il modello approssima il rumore nei dati di input invece di una relazione significativa (**overfitting**).

Durante l’addestramento, l’errore di bias diminuisce (man mano che il modello impara ad approssimare i dati), mentre l’errore di varianza aumenta. È importante fermare l’addestramento - manualmente (quando si rileva l’overfitting) o automaticamente (introducendo regolarizzazione) - per evitare l’overfitting.

## Conclusione

In questa lezione hai imparato le differenze tra le varie API dei due framework AI più popolari, TensorFlow e PyTorch. Inoltre, hai appreso un argomento molto importante: l’overfitting.

## 🚀 Sfida

Nei notebook allegati troverai delle ‘task’ in fondo; lavora sui notebook e completa le attività.

## Revisione e Studio Autonomo

Fai qualche ricerca sui seguenti argomenti:

- TensorFlow
- PyTorch
- Overfitting

Poniti le seguenti domande:

- Qual è la differenza tra TensorFlow e PyTorch?
- Qual è la differenza tra overfitting e underfitting?

## Compito

In questo laboratorio ti viene chiesto di risolvere due problemi di classificazione usando reti completamente connesse a singolo e multi-strato, utilizzando PyTorch o TensorFlow.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.