<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:01:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "it"
}
-->
# Frameworks di Reti Neurali

Come abbiamo già appreso, per poter addestrare le reti neurali in modo efficiente dobbiamo fare due cose:

* Operare su tensori, ad esempio moltiplicare, sommare e calcolare alcune funzioni come sigmoid o softmax
* Calcolare i gradienti di tutte le espressioni, per eseguire l'ottimizzazione della discesa del gradiente

Mentre la libreria `numpy` può fare la prima parte, abbiamo bisogno di un meccanismo per calcolare i gradienti. Nel nostro framework che abbiamo sviluppato nella sezione precedente, abbiamo dovuto programmare manualmente tutte le funzioni derivate all'interno del metodo `backward`, che esegue la retropropagazione. Idealmente, un framework dovrebbe darci la possibilità di calcolare i gradienti di *qualsiasi espressione* che possiamo definire.

Un'altra cosa importante è essere in grado di eseguire calcoli su GPU, o su qualsiasi altra unità di calcolo specializzata, come TPU. L'addestramento delle reti neurali profonde richiede *molti* calcoli, e poter parallelizzare questi calcoli su GPU è molto importante.

> ✅ Il termine 'parallelizzare' significa distribuire i calcoli su più dispositivi.

Attualmente, i due framework neurali più popolari sono: TensorFlow e PyTorch. Entrambi forniscono un'API di basso livello per operare con tensori sia su CPU che su GPU. Sopra l'API di basso livello, c'è anche un'API di livello superiore, chiamata rispettivamente Keras e PyTorch Lightning.

API di basso livello | TensorFlow| PyTorch
----------------------|-------------------------------------|--------------------------------
API di alto livello   | Keras| Pytorch

**Le API di basso livello** in entrambi i framework ti permettono di costruire i cosiddetti **grafi computazionali**. Questo grafo definisce come calcolare l'output (solitamente la funzione di perdita) con i parametri di input forniti, e può essere inviato per il calcolo su GPU, se disponibile. Ci sono funzioni per differenziare questo grafo computazionale e calcolare i gradienti, che possono poi essere utilizzati per ottimizzare i parametri del modello.

**Le API di alto livello** considerano le reti neurali come una **sequenza di strati**, e rendono la costruzione della maggior parte delle reti neurali molto più semplice. L'addestramento del modello solitamente richiede la preparazione dei dati e poi la chiamata di una funzione `fit` per svolgere il lavoro.

L'API di alto livello ti permette di costruire reti neurali tipiche molto rapidamente senza preoccuparti di molti dettagli. Allo stesso tempo, l'API di basso livello offre molto più controllo sul processo di addestramento, e quindi è molto utilizzata nella ricerca, quando si trattano nuove architetture di reti neurali.

È anche importante capire che puoi usare entrambe le API insieme, ad esempio puoi sviluppare la tua architettura di strato di rete usando l'API di basso livello, e poi usarla all'interno della rete più grande costruita e addestrata con l'API di alto livello. Oppure puoi definire una rete usando l'API di alto livello come una sequenza di strati, e poi usare il tuo ciclo di addestramento di basso livello per eseguire l'ottimizzazione. Entrambe le API utilizzano gli stessi concetti di base e sono progettate per funzionare bene insieme.

## Apprendimento

In questo corso, offriamo la maggior parte dei contenuti sia per PyTorch che per TensorFlow. Puoi scegliere il tuo framework preferito e seguire solo i notebook corrispondenti. Se non sei sicuro di quale framework scegliere, leggi alcune discussioni su internet riguardo a **PyTorch vs. TensorFlow**. Puoi anche dare un'occhiata a entrambi i framework per ottenere una migliore comprensione.

Dove possibile, utilizzeremo le API di alto livello per semplicità. Tuttavia, crediamo che sia importante capire come funzionano le reti neurali dalle basi, quindi all'inizio iniziamo lavorando con l'API di basso livello e i tensori. Tuttavia, se vuoi procedere rapidamente e non vuoi dedicare molto tempo a imparare questi dettagli, puoi saltarli e passare direttamente ai notebook dell'API di alto livello.

## ✍️ Esercizi: Framework

Continua il tuo apprendimento nei seguenti notebook:

API di basso livello | Notebook TensorFlow+Keras | PyTorch
----------------------|-------------------------------------|--------------------------------
API di alto livello   | Keras | *PyTorch Lightning*

Dopo aver padroneggiato i framework, riepiloghiamo il concetto di overfitting.

# Overfitting

L'overfitting è un concetto estremamente importante nell'apprendimento automatico, ed è molto importante capirlo bene!

Considera il seguente problema di approssimazione di 5 punti (rappresentati da `x` sui grafici sottostanti):

!lineare | sovradattamento
-------------------------|--------------------------
**Modello lineare, 2 parametri** | **Modello non lineare, 7 parametri**
Errore di addestramento = 5.3 | Errore di addestramento = 0
Errore di validazione = 5.1 | Errore di validazione = 20

* A sinistra, vediamo una buona approssimazione con una linea retta. Poiché il numero di parametri è adeguato, il modello coglie correttamente l'idea dietro la distribuzione dei punti.
* A destra, il modello è troppo potente. Poiché abbiamo solo 5 punti e il modello ha 7 parametri, può adattarsi in modo tale da passare attraverso tutti i punti, portando l'errore di addestramento a essere 0. Tuttavia, questo impedisce al modello di comprendere il corretto schema dietro i dati, quindi l'errore di validazione è molto alto.

È molto importante trovare un corretto equilibrio tra la ricchezza del modello (numero di parametri) e il numero di campioni di addestramento.

## Perché si verifica l'overfitting

  * Non abbastanza dati di addestramento
  * Modello troppo potente
  * Troppo rumore nei dati di input

## Come rilevare l'overfitting

Come puoi vedere dal grafico sopra, l'overfitting può essere rilevato da un errore di addestramento molto basso e un errore di validazione alto. Normalmente durante l'addestramento vedremo sia gli errori di addestramento che di validazione iniziare a diminuire, e poi a un certo punto l'errore di validazione potrebbe smettere di diminuire e iniziare a salire. Questo sarà un segno di overfitting e l'indicatore che probabilmente dovremmo fermare l'addestramento a questo punto (o almeno fare uno snapshot del modello).

overfitting

## Come prevenire l'overfitting

Se vedi che si verifica l'overfitting, puoi fare una delle seguenti cose:

 * Aumentare la quantità di dati di addestramento
 * Ridurre la complessità del modello
 * Utilizzare qualche tecnica di regolarizzazione, come Dropout, che considereremo più avanti.

## Overfitting e Compromesso Bias-Varianza

L'overfitting è in realtà un caso di un problema più generico in statistica chiamato Compromesso Bias-Varianza. Se consideriamo le possibili fonti di errore nel nostro modello, possiamo vedere due tipi di errori:

* **Errori di bias** sono causati dal nostro algoritmo che non riesce a catturare correttamente la relazione tra i dati di addestramento. Può derivare dal fatto che il nostro modello non è abbastanza potente (**underfitting**).
* **Errori di varianza**, che sono causati dal modello che approssima il rumore nei dati di input invece di una relazione significativa (**overfitting**).

Durante l'addestramento, l'errore di bias diminuisce (mentre il nostro modello impara ad approssimare i dati), e l'errore di varianza aumenta. È importante fermare l'addestramento - sia manualmente (quando rileviamo l'overfitting) sia automaticamente (introducendo la regolarizzazione) - per prevenire l'overfitting.

## Conclusione

In questa lezione, hai imparato le differenze tra le varie API per i due framework di AI più popolari, TensorFlow e PyTorch. Inoltre, hai appreso di un argomento molto importante, l'overfitting.

## 🚀 Sfida

Nei notebook allegati, troverai 'compiti' alla fine; lavora attraverso i notebook e completa i compiti.

## Revisione & Studio Autonomo

Fai qualche ricerca sui seguenti argomenti:

- TensorFlow
- PyTorch
- Overfitting

Poniti le seguenti domande:

- Qual è la differenza tra TensorFlow e PyTorch?
- Qual è la differenza tra overfitting e underfitting?

## Compito

In questo laboratorio, ti viene chiesto di risolvere due problemi di classificazione utilizzando reti completamente connesse a singolo e multi-strato usando PyTorch o TensorFlow.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.