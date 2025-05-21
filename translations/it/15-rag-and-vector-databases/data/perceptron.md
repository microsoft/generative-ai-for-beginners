<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:35:35+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "it"
}
-->
# Introduzione alle Reti Neurali: Percettrone

Uno dei primi tentativi di implementare qualcosa di simile a una moderna rete neurale fu realizzato da Frank Rosenblatt del Cornell Aeronautical Laboratory nel 1957. Si trattava di un'implementazione hardware chiamata "Mark-1", progettata per riconoscere figure geometriche primitive, come triangoli, quadrati e cerchi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Il Percettrone Mark 1' />|

> Immagini da Wikipedia

Un'immagine di input era rappresentata da una matrice di fotocellule 20x20, quindi la rete neurale aveva 400 input e un output binario. Una rete semplice conteneva un neurone, chiamato anche **unità logica a soglia**. I pesi della rete neurale agivano come potenziometri che richiedevano una regolazione manuale durante la fase di addestramento.

> ✅ Un potenziometro è un dispositivo che consente all'utente di regolare la resistenza di un circuito.

> Il New York Times scrisse sul percettrone in quel periodo: *l'embrione di un computer elettronico che [la Marina] si aspetta possa camminare, parlare, vedere, scrivere, riprodursi e essere consapevole della propria esistenza.*

## Modello di Percettrone

Supponiamo di avere N caratteristiche nel nostro modello, in tal caso il vettore di input sarebbe un vettore di dimensione N. Un percettrone è un modello di **classificazione binaria**, cioè può distinguere tra due classi di dati di input. Assumeremo che per ogni vettore di input x l'output del nostro percettrone sia +1 o -1, a seconda della classe. L'output sarà calcolato usando la formula:

y(x) = f(w<sup>T</sup>x)

dove f è una funzione di attivazione a gradino

## Addestramento del Percettrone

Per addestrare un percettrone dobbiamo trovare un vettore di pesi w che classifichi correttamente la maggior parte dei valori, cioè che risulti nel minor **errore**. Questo errore è definito dal **criterio del percettrone** nel seguente modo:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

dove:

* la somma è presa su quei punti dati di addestramento i che risultano nella classificazione errata
* x<sub>i</sub> è il dato di input, e t<sub>i</sub> è -1 o +1 rispettivamente per esempi negativi e positivi.

Questo criterio è considerato come una funzione dei pesi w, e dobbiamo minimizzarlo. Spesso si utilizza un metodo chiamato **discesa del gradiente**, in cui si parte con alcuni pesi iniziali w<sup>(0)</sup>, e poi ad ogni passo si aggiornano i pesi secondo la formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Qui η è il cosiddetto **tasso di apprendimento**, e ∇E(w) denota il **gradiente** di E. Dopo aver calcolato il gradiente, otteniamo

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

L'algoritmo in Python appare così:

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

In questa lezione, hai imparato cos'è un percettrone, che è un modello di classificazione binaria, e come addestrarlo utilizzando un vettore di pesi.

## 🚀 Sfida

Se desideri provare a costruire il tuo percettrone, prova questo laboratorio su Microsoft Learn che utilizza il designer di Azure ML.

## Revisione e Studio Autonomo

Per vedere come possiamo utilizzare il percettrone per risolvere un problema semplice così come problemi reali, e per continuare ad imparare - vai al notebook sul Percettrone.

Ecco anche un articolo interessante sui percettroni.

## Compito

In questa lezione, abbiamo implementato un percettrone per un compito di classificazione binaria, e lo abbiamo utilizzato per classificare tra due cifre scritte a mano. In questo laboratorio, ti viene chiesto di risolvere completamente il problema della classificazione delle cifre, cioè determinare quale cifra è più probabile che corrisponda a una data immagine.

* Istruzioni
* Notebook

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli del fatto che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.