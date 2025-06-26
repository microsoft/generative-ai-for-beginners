<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:34:10+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "de"
}
-->
# Einführung in Neuronale Netze: Perzeptron

Einer der ersten Versuche, etwas Ähnliches wie ein modernes neuronales Netzwerk zu implementieren, wurde 1957 von Frank Rosenblatt vom Cornell Aeronautical Laboratory unternommen. Es handelte sich um eine Hardware-Implementierung namens "Mark-1", die darauf ausgelegt war, primitive geometrische Figuren wie Dreiecke, Quadrate und Kreise zu erkennen.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Das Mark 1 Perzeptron' />|

> Bilder von Wikipedia

Ein Eingabebild wurde durch ein 20x20 Fotodiodenarray dargestellt, sodass das neuronale Netzwerk 400 Eingaben und eine binäre Ausgabe hatte. Ein einfaches Netzwerk enthielt ein Neuron, das auch als **Schwellenwertlogikeinheit** bezeichnet wird. Die Gewichte des neuronalen Netzwerks wirkten wie Potentiometer, die während der Trainingsphase manuell angepasst werden mussten.

> ✅ Ein Potentiometer ist ein Gerät, das es dem Benutzer ermöglicht, den Widerstand eines Stromkreises anzupassen.

> Die New York Times schrieb damals über das Perzeptron: *der Embryo eines elektronischen Computers, von dem [die Marine] erwartet, dass er laufen, sprechen, sehen, schreiben, sich selbst reproduzieren und sich seiner Existenz bewusst sein wird.*

## Perzeptron-Modell

Angenommen, wir haben N Merkmale in unserem Modell, in diesem Fall wäre der Eingabevektor ein Vektor der Größe N. Ein Perzeptron ist ein **binäres Klassifikationsmodell**, d.h. es kann zwischen zwei Klassen von Eingabedaten unterscheiden. Wir gehen davon aus, dass für jeden Eingabevektor x die Ausgabe unseres Perzeptrons entweder +1 oder -1 ist, je nach Klasse. Die Ausgabe wird mit der Formel berechnet:

y(x) = f(w<sup>T</sup>x)

wobei f eine Stufenaktivierungsfunktion ist

## Training des Perzeptrons

Um ein Perzeptron zu trainieren, müssen wir einen Gewichtungsvektor w finden, der die meisten Werte korrekt klassifiziert, d.h. zu dem kleinsten **Fehler** führt. Dieser Fehler wird durch das **Perzeptron-Kriterium** wie folgt definiert:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

wobei:

* die Summe über diejenigen Trainingsdatenpunkte i gebildet wird, die zu einer falschen Klassifikation führen
* x<sub>i</sub> die Eingabedaten sind und t<sub>i</sub> entsprechend -1 oder +1 für negative und positive Beispiele ist.

Dieses Kriterium wird als Funktion der Gewichte w betrachtet, und wir müssen es minimieren. Oft wird eine Methode namens **Gradientenabstieg** verwendet, bei der wir mit einigen anfänglichen Gewichten w<sup>(0)</sup> beginnen und dann in jedem Schritt die Gewichte gemäß der Formel aktualisieren:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hier ist η die sogenannte **Lernrate**, und ∇E(w) bezeichnet den **Gradienten** von E. Nachdem wir den Gradienten berechnet haben, erhalten wir

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

In dieser Lektion haben Sie ein Perzeptron kennengelernt, ein binäres Klassifikationsmodell, und wie man es mit einem Gewichtungsvektor trainiert.

## 🚀 Herausforderung

Wenn Sie versuchen möchten, Ihr eigenes Perzeptron zu erstellen, probieren Sie dieses Lab auf Microsoft Learn aus, das den Azure ML Designer verwendet.

## Überprüfung & Selbststudium

Um zu sehen, wie wir das Perzeptron verwenden können, um ein einfaches Problem sowie reale Probleme zu lösen, und um weiterzulernen - gehen Sie zum Perzeptron-Notebook.

Hier ist auch ein interessanter Artikel über Perzeptrons.

## Aufgabe

In dieser Lektion haben wir ein Perzeptron für eine binäre Klassifikationsaufgabe implementiert und es verwendet, um zwischen zwei handgeschriebenen Ziffern zu klassifizieren. In diesem Lab sollen Sie das Problem der Ziffernklassifikation vollständig lösen, d.h. bestimmen, welche Ziffer am wahrscheinlichsten einem gegebenen Bild entspricht.

* Anweisungen
* Notebook

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.