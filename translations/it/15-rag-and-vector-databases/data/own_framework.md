<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:45:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali. Perceptrone Multistrato

Nella sezione precedente, hai imparato il modello di rete neurale più semplice: il perceptrone a singolo strato, un modello lineare per la classificazione binaria.

In questa sezione estenderemo questo modello in un framework più flessibile, che ci permetterà di:

* eseguire la **classificazione multiclasse** oltre alla classificazione binaria
* risolvere problemi di **regressione** oltre alla classificazione
* separare classi che non sono linearmente separabili

Svilupperemo inoltre un nostro framework modulare in Python che ci consentirà di costruire diverse architetture di reti neurali.

## Formalizzazione del Machine Learning

Iniziamo formalizzando il problema del Machine Learning. Supponiamo di avere un dataset di addestramento **X** con etichette **Y**, e di dover costruire un modello *f* che faccia previsioni il più accurate possibile. La qualità delle previsioni è misurata dalla **funzione di perdita** ℒ. Le seguenti funzioni di perdita sono spesso utilizzate:

* Per problemi di regressione, quando dobbiamo prevedere un numero, possiamo usare l’**errore assoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, oppure l’**errore quadratico** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Per la classificazione, usiamo la **perdita 0-1** (che è sostanzialmente la stessa cosa della **accuratezza** del modello), oppure la **perdita logistica**.

Per il perceptrone a un livello, la funzione *f* era definita come una funzione lineare *f(x)=wx+b* (qui *w* è la matrice dei pesi, *x* è il vettore delle caratteristiche di input, e *b* è il vettore di bias). Per diverse architetture di reti neurali, questa funzione può assumere forme più complesse.

> Nel caso della classificazione, spesso è desiderabile ottenere come output della rete le probabilità delle classi corrispondenti. Per convertire numeri arbitrari in probabilità (ad esempio per normalizzare l’output), usiamo spesso la funzione **softmax** σ, e la funzione *f* diventa *f(x)=σ(wx+b)*

Nella definizione di *f* sopra, *w* e *b* sono chiamati **parametri** θ=⟨*w,b*⟩. Dato il dataset ⟨**X**,**Y**⟩, possiamo calcolare l’errore complessivo su tutto il dataset come funzione dei parametri θ.

> ✅ **L’obiettivo dell’addestramento della rete neurale è minimizzare l’errore variando i parametri θ**

## Ottimizzazione con Discesa del Gradiente

Esiste un metodo ben noto per l’ottimizzazione di funzioni chiamato **discesa del gradiente**. L’idea è che possiamo calcolare la derivata (nel caso multidimensionale chiamata **gradiente**) della funzione di perdita rispetto ai parametri, e modificare i parametri in modo che l’errore diminuisca. Questo può essere formalizzato come segue:

* Inizializza i parametri con valori casuali w<sup>(0)</sup>, b<sup>(0)</sup>
* Ripeti più volte il seguente passo:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante l’addestramento, i passi di ottimizzazione dovrebbero essere calcolati considerando l’intero dataset (ricorda che la perdita è calcolata come somma su tutti i campioni di addestramento). Tuttavia, nella pratica si prendono piccole porzioni del dataset chiamate **minibatch**, e si calcolano i gradienti su un sottoinsieme di dati. Poiché il sottoinsieme viene scelto casualmente ogni volta, questo metodo è chiamato **discesa del gradiente stocastica** (SGD).

## Perceptroni Multistrato e Backpropagation

La rete a un solo strato, come abbiamo visto sopra, è in grado di classificare classi linearmente separabili. Per costruire un modello più ricco, possiamo combinare più strati della rete. Matematicamente questo significa che la funzione *f* avrà una forma più complessa, e sarà calcolata in più passaggi:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Qui, α è una **funzione di attivazione non lineare**, σ è la funzione softmax, e i parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L’algoritmo di discesa del gradiente rimane lo stesso, ma il calcolo dei gradienti diventa più complesso. Applicando la regola della derivazione a catena, possiamo calcolare le derivate come:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regola della derivazione a catena viene usata per calcolare le derivate della funzione di perdita rispetto ai parametri.

Nota che la parte più a sinistra di tutte queste espressioni è la stessa, quindi possiamo calcolare efficacemente le derivate partendo dalla funzione di perdita e procedendo "a ritroso" attraverso il grafo computazionale. Per questo motivo il metodo di addestramento di un perceptrone multistrato si chiama **backpropagation**, o semplicemente 'backprop'.



> TODO: citazione immagine

> ✅ Approfondiremo il backprop in modo molto più dettagliato nel nostro esempio nel notebook.

## Conclusione

In questa lezione abbiamo costruito la nostra libreria per reti neurali e l’abbiamo utilizzata per un semplice compito di classificazione bidimensionale.

## 🚀 Sfida

Nel notebook allegato, implementerai il tuo framework per costruire e addestrare perceptroni multistrato. Potrai vedere nel dettaglio come funzionano le reti neurali moderne.

Procedi al notebook OwnFramework e segui le istruzioni.



## Revisione e Autoapprendimento

La backpropagation è un algoritmo comune usato in AI e ML, vale la pena studiarlo più a fondo.

## Compito

In questo laboratorio ti viene chiesto di usare il framework costruito in questa lezione per risolvere la classificazione delle cifre scritte a mano del dataset MNIST.

* Istruzioni
* Notebook

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.