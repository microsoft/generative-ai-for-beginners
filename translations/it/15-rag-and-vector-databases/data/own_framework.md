<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:18:44+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali. Percettrone Multi-Strato

Nella sezione precedente, hai appreso il modello di rete neurale più semplice - il percettrone a uno strato, un modello di classificazione lineare a due classi.

In questa sezione estenderemo questo modello in un framework più flessibile, che ci permetterà di:

* eseguire la **classificazione multi-classe** oltre a quella a due classi
* risolvere problemi di **regressione** oltre alla classificazione
* separare classi che non sono linearmente separabili

Svilupperemo anche il nostro framework modulare in Python che ci permetterà di costruire diverse architetture di reti neurali.

## Formalizzazione del Machine Learning

Iniziamo con la formalizzazione del problema di Machine Learning. Supponiamo di avere un dataset di addestramento **X** con etichette **Y**, e dobbiamo costruire un modello *f* che fornirà previsioni più accurate. La qualità delle previsioni è misurata dalla **funzione di perdita** ℒ. Le seguenti funzioni di perdita sono spesso utilizzate:

* Per un problema di regressione, quando dobbiamo prevedere un numero, possiamo usare l'**errore assoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o l'**errore quadrato** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Per la classificazione, utilizziamo la **perdita 0-1** (che è essenzialmente la stessa dell'**accuratezza** del modello), o la **perdita logistica**.

Per il percettrone a un livello, la funzione *f* era definita come una funzione lineare *f(x)=wx+b* (qui *w* è la matrice dei pesi, *x* è il vettore delle caratteristiche di input, e *b* è il vettore di bias). Per diverse architetture di reti neurali, questa funzione può assumere una forma più complessa.

> Nel caso della classificazione, è spesso desiderabile ottenere probabilità delle classi corrispondenti come output della rete. Per convertire numeri arbitrari in probabilità (ad esempio per normalizzare l'output), spesso utilizziamo la funzione **softmax** σ, e la funzione *f* diventa *f(x)=σ(wx+b)*

Nella definizione di *f* sopra, *w* e *b* sono chiamati **parametri** θ=⟨*w,b*⟩. Dato il dataset ⟨**X**,**Y**⟩, possiamo calcolare un errore complessivo su tutto il dataset come funzione dei parametri θ.

> ✅ **L'obiettivo dell'addestramento della rete neurale è minimizzare l'errore variando i parametri θ**

## Ottimizzazione con Discesa del Gradiente

Esiste un metodo ben noto di ottimizzazione delle funzioni chiamato **discesa del gradiente**. L'idea è che possiamo calcolare una derivata (nel caso multidimensionale chiamata **gradiente**) della funzione di perdita rispetto ai parametri, e variare i parametri in modo tale che l'errore diminuisca. Questo può essere formalizzato come segue:

* Inizializzare i parametri con alcuni valori casuali w<sup>(0)</sup>, b<sup>(0)</sup>
* Ripetere il seguente passo molte volte:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante l'addestramento, i passi di ottimizzazione devono essere calcolati considerando l'intero dataset (ricorda che la perdita è calcolata come una somma attraverso tutti i campioni di addestramento). Tuttavia, nella vita reale prendiamo piccole porzioni del dataset chiamate **minibatch**, e calcoliamo i gradienti basandoci su un sottoinsieme di dati. Poiché il sottoinsieme è preso casualmente ogni volta, tale metodo è chiamato **discesa del gradiente stocastica** (SGD).

## Percettroni Multi-Strato e Backpropagation

La rete a uno strato, come abbiamo visto sopra, è in grado di classificare classi linearmente separabili. Per costruire un modello più ricco, possiamo combinare diversi strati della rete. Matematicamente significherebbe che la funzione *f* avrebbe una forma più complessa, e sarà calcolata in diversi passaggi:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Qui, α è una **funzione di attivazione non lineare**, σ è una funzione softmax, e i parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L'algoritmo di discesa del gradiente rimarrebbe lo stesso, ma sarebbe più difficile calcolare i gradienti. Dato il principio della derivazione a catena, possiamo calcolare le derivate come:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regola della derivazione a catena è utilizzata per calcolare le derivate della funzione di perdita rispetto ai parametri.

Nota che la parte più a sinistra di tutte quelle espressioni è la stessa, e quindi possiamo calcolare efficacemente le derivate partendo dalla funzione di perdita e andando "all'indietro" attraverso il grafo computazionale. Pertanto, il metodo di addestramento di un percettrone multi-strato è chiamato **backpropagation**, o 'backprop'.

> TODO: citazione immagine

> ✅ Approfondiremo il backprop in modo molto più dettagliato nel nostro esempio di notebook.

## Conclusione

In questa lezione, abbiamo costruito la nostra libreria di reti neurali e l'abbiamo utilizzata per un semplice compito di classificazione bidimensionale.

## 🚀 Sfida

Nel notebook allegato, implementerai il tuo framework per costruire e addestrare percettroni multi-strato. Sarai in grado di vedere in dettaglio come operano le reti neurali moderne.

Procedi al notebook OwnFramework e lavoraci su.

## Revisione & Studio Autonomo

La backpropagation è un algoritmo comune utilizzato in AI e ML, vale la pena studiarlo in modo più dettagliato.

## Compito

In questo laboratorio, ti viene chiesto di utilizzare il framework che hai costruito in questa lezione per risolvere la classificazione delle cifre scritte a mano MNIST.

* Istruzioni
* Notebook

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di essere consapevoli che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.