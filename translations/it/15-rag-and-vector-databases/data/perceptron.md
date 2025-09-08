<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:57:14+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali: Perceptron

Uno dei primi tentativi di implementare qualcosa di simile a una rete neurale moderna fu fatto da Frank Rosenblatt del Cornell Aeronautical Laboratory nel 1957. Si trattava di un'implementazione hardware chiamata "Mark-1", progettata per riconoscere figure geometriche primitive, come triangoli, quadrati e cerchi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Immagini da Wikipedia

Un'immagine di input era rappresentata da una matrice di fotocellule 20x20, quindi la rete neurale aveva 400 ingressi e un'uscita binaria. Una rete semplice conteneva un solo neurone, chiamato anche **unità logica a soglia**. I pesi della rete neurale agivano come potenziometri che richiedevano una regolazione manuale durante la fase di addestramento.

> ✅ Un potenziometro è un dispositivo che permette all'utente di regolare la resistenza di un circuito.

> Il New York Times scrisse del perceptron in quel periodo: *l'embrione di un computer elettronico che [la Marina] si aspetta sarà in grado di camminare, parlare, vedere, scrivere, riprodursi e essere consapevole della propria esistenza.*

## Modello di Perceptron

Supponiamo di avere N caratteristiche nel nostro modello, in tal caso il vettore di input sarà un vettore di dimensione N. Un perceptron è un modello di **classificazione binaria**, cioè può distinguere tra due classi di dati di input. Assumeremo che per ogni vettore di input x l'output del nostro perceptron sia +1 o -1, a seconda della classe. L'output sarà calcolato usando la formula:

y(x) = f(w<sup>T</sup>x)

dove f è una funzione di attivazione a gradino

## Addestramento del Perceptron

Per addestrare un perceptron dobbiamo trovare un vettore di pesi w che classifichi correttamente la maggior parte dei valori, cioè che produca il più piccolo **errore** possibile. Questo errore è definito dal **criterio del perceptron** nel modo seguente:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

dove:

* la somma è calcolata sui punti dati di addestramento i che risultano in una classificazione errata
* x<sub>i</sub> è il dato di input, e t<sub>i</sub> è -1 o +1 per esempi negativi e positivi rispettivamente.

Questo criterio è considerato come una funzione dei pesi w, e dobbiamo minimizzarlo. Spesso si usa un metodo chiamato **discesa del gradiente**, in cui si parte da un vettore di pesi iniziale w<sup>(0)</sup>, e poi ad ogni passo si aggiornano i pesi secondo la formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Qui η è il cosiddetto **tasso di apprendimento**, e ∇E(w) indica il **gradiente** di E. Dopo aver calcolato il gradiente, otteniamo

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

L'algoritmo in Python è il seguente:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Conclusione

In questa lezione hai imparato cos'è un perceptron, un modello di classificazione binaria, e come addestrarlo usando un vettore di pesi.

## 🚀 Sfida

Se vuoi provare a costruire il tuo perceptron, prova questo laboratorio su Microsoft Learn che utilizza Azure ML designer


## Revisione e Autoapprendimento

Per vedere come possiamo usare il perceptron per risolvere un problema semplice così come problemi reali, e per continuare a imparare - vai al notebook Perceptron.

Ecco anche un articolo interessante sui perceptron.

## Compito

In questa lezione abbiamo implementato un perceptron per un compito di classificazione binaria, e lo abbiamo usato per classificare due cifre scritte a mano. In questo laboratorio, ti viene chiesto di risolvere completamente il problema della classificazione delle cifre, cioè determinare quale cifra corrisponde più probabilmente a una data immagine.

* Istruzioni
* Notebook

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.