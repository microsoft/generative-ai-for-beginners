<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:57:19+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "it"
}
-->
# Framework per Reti Neurali

Come abbiamo già imparato, per poter addestrare reti neurali in modo efficiente dobbiamo fare due cose:

* Operare sui tensori, ad esempio moltiplicare, sommare e calcolare alcune funzioni come sigmoide o softmax
* Calcolare i gradienti di tutte le espressioni, per eseguire l'ottimizzazione tramite discesa del gradiente

Mentre la libreria `numpy` può fare la prima parte, abbiamo bisogno di un meccanismo per calcolare i gradienti. Nel nostro framework che abbiamo sviluppato nella sezione precedente, abbiamo dovuto programmare manualmente tutte le funzioni derivate all'interno del metodo `backward`, che esegue la retropropagazione. Idealmente, un framework dovrebbe darci la possibilità di calcolare i gradienti di *qualsiasi espressione* che possiamo definire.

Un'altra cosa importante è essere in grado di eseguire calcoli su GPU, o altre unità di calcolo specializzate, come TPU. L'addestramento di reti neurali profonde richiede *molti* calcoli, e poter parallelizzare questi calcoli su GPU è molto importante.

> ✅ Il termine 'parallelizzare' significa distribuire i calcoli su più dispositivi.

Attualmente, i due framework neurali più popolari sono: TensorFlow e PyTorch. Entrambi forniscono un'API di basso livello per operare con i tensori sia su CPU che su GPU. Oltre all'API di basso livello, c'è anche un'API di alto livello, chiamata rispettivamente Keras e PyTorch Lightning.

API di Basso Livello | TensorFlow | PyTorch
---------------------|-------------------------------------|--------------------------------
API di Alto Livello | Keras | PyTorch Lightning

Le **API di basso livello** in entrambi i framework ti permettono di costruire i cosiddetti **grafici computazionali**. Questo grafico definisce come calcolare l'output (di solito la funzione di perdita) con i parametri di input dati, e può essere inviato per il calcolo su GPU, se disponibile. Ci sono funzioni per differenziare questo grafico computazionale e calcolare i gradienti, che possono poi essere utilizzati per ottimizzare i parametri del modello.

Le **API di alto livello** considerano le reti neurali come una **sequenza di livelli**, e rendono la costruzione della maggior parte delle reti neurali molto più semplice. L'addestramento del modello di solito richiede la preparazione dei dati e poi la chiamata di una funzione `fit` per svolgere il lavoro.

L'API di alto livello ti consente di costruire reti neurali tipiche molto rapidamente senza preoccuparti di molti dettagli. Allo stesso tempo, l'API di basso livello offre molto più controllo sul processo di addestramento, e quindi viene utilizzata molto nella ricerca, quando si ha a che fare con nuove architetture di reti neurali.

È anche importante capire che puoi usare entrambe le API insieme, ad esempio puoi sviluppare la tua architettura di livello di rete usando l'API di basso livello, e poi usarla all'interno della rete più grande costruita e addestrata con l'API di alto livello. Oppure puoi definire una rete usando l'API di alto livello come una sequenza di livelli, e poi usare il tuo ciclo di addestramento di basso livello per eseguire l'ottimizzazione. Entrambe le API utilizzano gli stessi concetti di base sottostanti, e sono progettate per funzionare bene insieme.

## Apprendimento

In questo corso, offriamo la maggior parte del contenuto sia per PyTorch che per TensorFlow. Puoi scegliere il tuo framework preferito e seguire solo i notebook corrispondenti. Se non sei sicuro di quale framework scegliere, leggi alcune discussioni su internet riguardo **PyTorch vs. TensorFlow**. Puoi anche dare un'occhiata a entrambi i framework per ottenere una migliore comprensione.

Dove possibile, useremo le API di Alto Livello per semplicità. Tuttavia, crediamo che sia importante capire come funzionano le reti neurali dalle basi, quindi all'inizio iniziamo lavorando con l'API di basso livello e i tensori. Tuttavia, se vuoi procedere velocemente e non vuoi spendere molto tempo ad apprendere questi dettagli, puoi saltarli e andare direttamente ai notebook delle API di alto livello.

## ✍️ Esercizi: Framework

Continua il tuo apprendimento nei seguenti notebook:

API di Basso Livello | Notebook TensorFlow+Keras | PyTorch
---------------------|-------------------------------------|--------------------------------
API di Alto Livello | Keras | *PyTorch Lightning*

Dopo aver padroneggiato i framework, riepiloghiamo il concetto di overfitting.

# Overfitting

L'overfitting è un concetto estremamente importante nell'apprendimento automatico, ed è molto importante capirlo bene!

Considera il seguente problema di approssimazione di 5 punti (rappresentati da `x` nei grafici sottostanti):

!lineare | overfit
-------------------------|--------------------------
**Modello lineare, 2 parametri** | **Modello non lineare, 7 parametri**
Errore di addestramento = 5.3 | Errore di addestramento = 0
Errore di validazione = 5.1 | Errore di validazione = 20

* A sinistra, vediamo una buona approssimazione con una linea retta. Poiché il numero di parametri è adeguato, il modello coglie bene l'idea della distribuzione dei punti.
* A destra, il modello è troppo potente. Poiché abbiamo solo 5 punti e il modello ha 7 parametri, può adattarsi in modo tale da passare attraverso tutti i punti, facendo sì che l'errore di addestramento sia 0. Tuttavia, questo impedisce al modello di comprendere il corretto schema dietro i dati, quindi l'errore di validazione è molto alto.

È molto importante trovare un giusto equilibrio tra la complessità del modello (numero di parametri) e il numero di campioni di addestramento.

## Perché si verifica l'overfitting

  * Non abbastanza dati di addestramento
  * Modello troppo potente
  * Troppo rumore nei dati di input

## Come rilevare l'overfitting

Come puoi vedere dal grafico sopra, l'overfitting può essere rilevato da un errore di addestramento molto basso e un errore di validazione alto. Normalmente durante l'addestramento vedremo sia l'errore di addestramento che di validazione iniziare a diminuire, e poi a un certo punto l'errore di validazione potrebbe smettere di diminuire e iniziare a crescere. Questo sarà un segnale di overfitting, e l'indicatore che probabilmente dovremmo fermare l'addestramento a questo punto (o almeno fare uno snapshot del modello).

overfitting

## Come prevenire l'overfitting

Se vedi che si verifica l'overfitting, puoi fare una delle seguenti cose:

 * Aumentare la quantità di dati di addestramento
 * Ridurre la complessità del modello
 * Usare qualche tecnica di regolarizzazione, come il Dropout, che considereremo più avanti.

## Overfitting e Compromesso Bias-Varianza

L'overfitting è in realtà un caso di un problema più generico in statistica chiamato Compromesso Bias-Varianza. Se consideriamo le possibili fonti di errore nel nostro modello, possiamo vedere due tipi di errori:

* **Errori di bias** sono causati dal fatto che il nostro algoritmo non è in grado di catturare correttamente la relazione tra i dati di addestramento. Può risultare dal fatto che il nostro modello non è abbastanza potente (**underfitting**).
* **Errori di varianza**, che sono causati dal modello che approssima il rumore nei dati di input invece di una relazione significativa (**overfitting**).

Durante l'addestramento, l'errore di bias diminuisce (poiché il nostro modello impara ad approssimare i dati), e l'errore di varianza aumenta. È importante fermare l'addestramento - sia manualmente (quando rileviamo l'overfitting) che automaticamente (introducendo la regolarizzazione) - per prevenire l'overfitting.

## Conclusione

In questa lezione, hai imparato le differenze tra le varie API per i due framework di AI più popolari, TensorFlow e PyTorch. Inoltre, hai imparato un argomento molto importante, l'overfitting.

## 🚀 Sfida

Nei notebook allegati, troverai 'compiti' in fondo; lavora attraverso i notebook e completa i compiti.

## Revisione & Studio Autonomo

Fai alcune ricerche sui seguenti argomenti:

- TensorFlow
- PyTorch
- Overfitting

Poniti le seguenti domande:

- Qual è la differenza tra TensorFlow e PyTorch?
- Qual è la differenza tra overfitting e underfitting?

## Compito

In questo laboratorio, ti viene chiesto di risolvere due problemi di classificazione usando reti completamente connesse a singolo e multi-strato utilizzando PyTorch o TensorFlow.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.