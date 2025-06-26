<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:23:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali. Perceptron Multistrato

Nella sezione precedente, hai appreso il modello di rete neurale più semplice: il perceptron a un solo strato, un modello di classificazione lineare a due classi.

In questa sezione estenderemo questo modello in un framework più flessibile, permettendoci di:

* eseguire **classificazioni multi-classe** oltre a quelle a due classi
* risolvere **problemi di regressione** oltre alla classificazione
* separare classi che non sono linearmente separabili

Svilupperemo anche il nostro framework modulare in Python che ci permetterà di costruire diverse architetture di reti neurali.

## Formalizzazione del Machine Learning

Iniziamo formalizzando il problema del Machine Learning. Supponiamo di avere un dataset di addestramento **X** con etichette **Y**, e dobbiamo costruire un modello *f* che faccia previsioni il più accurate possibile. La qualità delle previsioni è misurata dalla **Funzione di perdita** ℒ. Le seguenti funzioni di perdita sono spesso utilizzate:

* Per i problemi di regressione, quando dobbiamo prevedere un numero, possiamo usare **errore assoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o **errore quadratico** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Per la classificazione, usiamo la **perdita 0-1** (che è essenzialmente la stessa dell'**accuratezza** del modello), o la **perdita logistica**.

Per il perceptron a un livello, la funzione *f* era definita come una funzione lineare *f(x)=wx+b* (qui *w* è la matrice dei pesi, *x* è il vettore delle caratteristiche di input, e *b* è il vettore di bias). Per diverse architetture di reti neurali, questa funzione può assumere una forma più complessa.

> Nel caso della classificazione, è spesso desiderabile ottenere le probabilità delle classi corrispondenti come output della rete. Per convertire numeri arbitrari in probabilità (ad esempio per normalizzare l'output), usiamo spesso la funzione **softmax** σ, e la funzione *f* diventa *f(x)=σ(wx+b)*

Nella definizione di *f* sopra, *w* e *b* sono chiamati **parametri** θ=⟨*w,b*⟩. Dato il dataset ⟨**X**,**Y**⟩, possiamo calcolare un errore complessivo su tutto il dataset come funzione dei parametri θ.

> ✅ **L'obiettivo dell'addestramento della rete neurale è minimizzare l'errore variando i parametri θ**

## Ottimizzazione con Discesa del Gradiente

Esiste un metodo noto di ottimizzazione delle funzioni chiamato **discesa del gradiente**. L'idea è che possiamo calcolare una derivata (nel caso multidimensionale chiamata **gradiente**) della funzione di perdita rispetto ai parametri, e variare i parametri in modo tale che l'errore diminuisca. Questo può essere formalizzato come segue:

* Inizializzare i parametri con alcuni valori casuali w<sup>(0)</sup>, b<sup>(0)</sup>
* Ripetere il seguente passo molte volte:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante l'addestramento, i passi di ottimizzazione dovrebbero essere calcolati considerando l'intero dataset (ricorda che la perdita è calcolata come somma su tutti i campioni di addestramento). Tuttavia, nella vita reale prendiamo piccole porzioni del dataset chiamate **minibatch**, e calcoliamo i gradienti basandoci su un sottoinsieme di dati. Poiché il sottoinsieme è preso casualmente ogni volta, tale metodo è chiamato **discesa del gradiente stocastica** (SGD).

## Perceptron Multistrato e Backpropagation

Una rete a un solo strato, come abbiamo visto sopra, è in grado di classificare classi linearmente separabili. Per costruire un modello più ricco, possiamo combinare diversi strati della rete. Matematicamente significherebbe che la funzione *f* avrebbe una forma più complessa e verrebbe calcolata in diversi passaggi:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Qui, α è una **funzione di attivazione non lineare**, σ è una funzione softmax, e i parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L'algoritmo di discesa del gradiente rimarrebbe lo stesso, ma sarebbe più difficile calcolare i gradienti. Dato il principio della derivazione a catena, possiamo calcolare le derivate come:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regola della derivazione a catena è usata per calcolare le derivate della funzione di perdita rispetto ai parametri.

Nota che la parte più a sinistra di tutte queste espressioni è la stessa, e quindi possiamo calcolare efficacemente le derivate partendo dalla funzione di perdita e andando "indietro" attraverso il grafo computazionale. Pertanto, il metodo di addestramento di un perceptron multistrato è chiamato **backpropagation**, o 'backprop'.

> TODO: citazione immagine

> ✅ Approfondiremo la backpropagation in modo molto più dettagliato nel nostro esempio in notebook.

## Conclusione

In questa lezione, abbiamo costruito la nostra libreria di reti neurali e l'abbiamo utilizzata per un semplice compito di classificazione bidimensionale.

## 🚀 Sfida

Nel notebook allegato, implementerai il tuo framework per costruire e addestrare perceptron multistrato. Potrai vedere in dettaglio come funzionano le moderne reti neurali.

Procedi al notebook OwnFramework e lavoraci sopra.

## Revisione e Studio Autonomo

La backpropagation è un algoritmo comune utilizzato nell'IA e nel ML, vale la pena studiarlo in dettaglio.

## Compito

In questo laboratorio, ti viene chiesto di utilizzare il framework che hai costruito in questa lezione per risolvere la classificazione delle cifre scritte a mano del dataset MNIST.

* Istruzioni
* Notebook

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.