<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:53:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "de"
}
-->
# Einführung in Neuronale Netze: Perzeptron

Einer der ersten Versuche, etwas Ähnliches wie ein modernes neuronales Netzwerk zu realisieren, wurde 1957 von Frank Rosenblatt vom Cornell Aeronautical Laboratory unternommen. Es handelte sich um eine Hardware-Implementierung namens „Mark-1“, die dazu entwickelt wurde, primitive geometrische Figuren wie Dreiecke, Quadrate und Kreise zu erkennen.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Bilder von Wikipedia

Ein Eingabebild wurde durch ein 20x20 Photodioden-Array dargestellt, sodass das neuronale Netzwerk 400 Eingänge und einen binären Ausgang hatte. Ein einfaches Netzwerk bestand aus einem Neuron, auch **Threshold Logic Unit** genannt. Die Gewichte des neuronalen Netzwerks wirkten wie Potentiometer, die während der Trainingsphase manuell eingestellt werden mussten.

> ✅ Ein Potentiometer ist ein Bauteil, mit dem der Benutzer den Widerstand in einem Stromkreis einstellen kann.

> Die New York Times schrieb damals über das Perzeptron: *der Embryo eines elektronischen Computers, von dem die Marine erwartet, dass er laufen, sprechen, sehen, schreiben, sich selbst reproduzieren und sich seiner Existenz bewusst sein wird.*

## Perzeptron-Modell

Angenommen, wir haben N Merkmale in unserem Modell, dann ist der Eingabevektor ein Vektor der Größe N. Ein Perzeptron ist ein **binäres Klassifikationsmodell**, das heißt, es kann zwischen zwei Klassen von Eingabedaten unterscheiden. Wir nehmen an, dass für jeden Eingabevektor x die Ausgabe unseres Perzeptrons entweder +1 oder -1 ist, abhängig von der Klasse. Die Ausgabe wird mit folgender Formel berechnet:

y(x) = f(w<sup>T</sup>x)

wobei f eine Stufen-Aktivierungsfunktion ist.

## Training des Perzeptrons

Um ein Perzeptron zu trainieren, müssen wir einen Gewichtvektor w finden, der die meisten Werte korrekt klassifiziert, also den kleinsten **Fehler** verursacht. Dieser Fehler wird durch das **Perzeptron-Kriterium** folgendermaßen definiert:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

wobei:

* die Summe über jene Trainingsdatenpunkte i gebildet wird, die falsch klassifiziert wurden
* x<sub>i</sub> die Eingabedaten sind und t<sub>i</sub> entweder -1 oder +1 für negative bzw. positive Beispiele ist.

Dieses Kriterium wird als Funktion der Gewichte w betrachtet, die wir minimieren müssen. Häufig wird eine Methode namens **Gradientenabstieg** verwendet, bei der wir mit einem Anfangsgewicht w<sup>(0)</sup> starten und dann in jedem Schritt die Gewichte nach folgender Formel aktualisieren:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hierbei ist η die sogenannte **Lernrate** und ∇E(w) bezeichnet den **Gradienten** von E. Nach der Berechnung des Gradienten erhalten wir:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Der Algorithmus in Python sieht folgendermaßen aus:

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

## Fazit

In dieser Lektion hast du gelernt, was ein Perzeptron ist, ein binäres Klassifikationsmodell, und wie man es mithilfe eines Gewichtvektors trainiert.

## 🚀 Herausforderung

Wenn du dein eigenes Perzeptron bauen möchtest, probiere dieses Lab auf Microsoft Learn aus, das den Azure ML Designer verwendet.

## Wiederholung & Selbststudium

Um zu sehen, wie wir das Perzeptron zur Lösung eines einfachen Problems sowie realer Aufgaben einsetzen können und um weiterzulernen, gehe zum Perzeptron-Notebook.

Hier gibt es auch einen interessanten Artikel über Perzeptrons.

## Aufgabe

In dieser Lektion haben wir ein Perzeptron für eine binäre Klassifikationsaufgabe implementiert und es verwendet, um zwischen zwei handgeschriebenen Ziffern zu unterscheiden. In diesem Lab sollst du das Problem der Ziffernerkennung vollständig lösen, also bestimmen, welche Ziffer am wahrscheinlichsten zu einem gegebenen Bild gehört.

* Anweisungen
* Notebook

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.