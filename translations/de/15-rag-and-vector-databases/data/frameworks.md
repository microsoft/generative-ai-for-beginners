<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:48:42+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "de"
}
-->
# Frameworks für Neuronale Netzwerke

Wie wir bereits gelernt haben, müssen wir zwei Dinge tun, um neuronale Netzwerke effizient trainieren zu können:

* Mit Tensoren arbeiten, z. B. multiplizieren, addieren und einige Funktionen wie Sigmoid oder Softmax berechnen
* Gradienten aller Ausdrücke berechnen, um die Gradientenabstiegsoptimierung durchzuführen

Während die `numpy`-Bibliothek den ersten Teil erledigen kann, benötigen wir einen Mechanismus, um Gradienten zu berechnen. In unserem Framework, das wir im vorherigen Abschnitt entwickelt haben, mussten wir alle Ableitungsfunktionen manuell im `backward`-Methoden programmieren, die die Rückpropagation durchführt. Idealerweise sollte ein Framework uns die Möglichkeit bieten, Gradienten von *beliebigen Ausdrücken* zu berechnen, die wir definieren können.

Ein weiterer wichtiger Punkt ist, Berechnungen auf der GPU oder anderen spezialisierten Recheneinheiten wie TPU durchführen zu können. Das Training von tiefen neuronalen Netzwerken erfordert *eine Menge* Berechnungen, und die Möglichkeit, diese Berechnungen auf GPUs zu parallelisieren, ist sehr wichtig.

> ✅ Der Begriff 'parallelisieren' bedeutet, die Berechnungen über mehrere Geräte zu verteilen.

Derzeit sind die beiden beliebtesten neuronalen Frameworks: TensorFlow und PyTorch. Beide bieten eine Low-Level-API, um mit Tensoren sowohl auf der CPU als auch auf der GPU zu arbeiten. Auf der Low-Level-API gibt es auch eine High-Level-API, die entsprechend Keras und PyTorch Lightning genannt wird.

Low-Level-API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-Level-API| Keras| Pytorch

**Low-Level-APIs** in beiden Frameworks ermöglichen es Ihnen, sogenannte **Berechnungsgraphen** zu erstellen. Dieser Graph definiert, wie der Output (normalerweise die Verlustfunktion) mit gegebenen Eingabeparametern berechnet wird und kann zur Berechnung auf die GPU geschoben werden, wenn sie verfügbar ist. Es gibt Funktionen, um diesen Berechnungsgraphen zu differenzieren und Gradienten zu berechnen, die dann zur Optimierung der Modellparameter verwendet werden können.

**High-Level-APIs** betrachten neuronale Netzwerke weitgehend als eine **Sequenz von Schichten** und erleichtern das Erstellen der meisten neuronalen Netzwerke erheblich. Das Training des Modells erfordert normalerweise die Vorbereitung der Daten und dann das Aufrufen einer `fit`-Funktion, um die Aufgabe zu erledigen.

Die High-Level-API ermöglicht es Ihnen, typische neuronale Netzwerke sehr schnell zu konstruieren, ohne sich um viele Details kümmern zu müssen. Gleichzeitig bieten Low-Level-APIs viel mehr Kontrolle über den Trainingsprozess, und deshalb werden sie in der Forschung häufig verwendet, wenn Sie mit neuen neuronalen Netzwerkarchitekturen arbeiten.

Es ist auch wichtig zu verstehen, dass Sie beide APIs zusammen verwenden können, z. B. können Sie Ihre eigene Netzwerkarchitektur mit der Low-Level-API entwickeln und dann innerhalb des größeren Netzwerks verwenden, das mit der High-Level-API konstruiert und trainiert wird. Oder Sie können ein Netzwerk mit der High-Level-API als Sequenz von Schichten definieren und dann Ihre eigene Low-Level-Trainingsschleife zur Optimierung verwenden. Beide APIs verwenden die gleichen grundlegenden Konzepte und sind darauf ausgelegt, gut zusammenzuarbeiten.

## Lernen

In diesem Kurs bieten wir die meisten Inhalte sowohl für PyTorch als auch für TensorFlow an. Sie können Ihr bevorzugtes Framework auswählen und nur die entsprechenden Notebooks durchgehen. Wenn Sie nicht sicher sind, welches Framework Sie wählen sollen, lesen Sie einige Diskussionen im Internet über **PyTorch vs. TensorFlow**. Sie können auch einen Blick auf beide Frameworks werfen, um ein besseres Verständnis zu bekommen.

Wo möglich, werden wir High-Level-APIs der Einfachheit halber verwenden. Wir glauben jedoch, dass es wichtig ist, zu verstehen, wie neuronale Netzwerke von Grund auf funktionieren, daher beginnen wir zunächst mit der Arbeit mit der Low-Level-API und Tensoren. Wenn Sie jedoch schnell starten möchten und nicht viel Zeit mit dem Lernen dieser Details verbringen möchten, können Sie diese überspringen und direkt in die High-Level-API-Notebooks gehen.

## ✍️ Übungen: Frameworks

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Low-Level-API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-Level-API| Keras | *PyTorch Lightning*

Nachdem Sie die Frameworks gemeistert haben, lassen Sie uns das Konzept des Overfitting rekapitulieren.

# Overfitting

Overfitting ist ein äußerst wichtiges Konzept im maschinellen Lernen, und es ist sehr wichtig, es richtig zu verstehen!

Betrachten Sie das folgende Problem der Annäherung von 5 Punkten (dargestellt durch `x` in den unten stehenden Grafiken):

!linear | überanpasst
-------------------------|--------------------------
**Lineares Modell, 2 Parameter** | **Nicht-lineares Modell, 7 Parameter**
Trainingsfehler = 5.3 | Trainingsfehler = 0
Validierungsfehler = 5.1 | Validierungsfehler = 20

* Links sehen wir eine gute Gerade, die die Punkte annähert. Da die Anzahl der Parameter angemessen ist, erfasst das Modell die Idee hinter der Punktverteilung richtig.
* Rechts ist das Modell zu mächtig. Da wir nur 5 Punkte haben und das Modell 7 Parameter hat, kann es sich so anpassen, dass es durch alle Punkte geht, was den Trainingsfehler auf 0 bringt. Dies verhindert jedoch, dass das Modell das richtige Muster hinter den Daten versteht, sodass der Validierungsfehler sehr hoch ist.

Es ist sehr wichtig, ein korrektes Gleichgewicht zwischen der Komplexität des Modells (Anzahl der Parameter) und der Anzahl der Trainingsbeispiele zu finden.

## Warum Overfitting auftritt

  * Nicht genug Trainingsdaten
  * Zu mächtiges Modell
  * Zu viel Rauschen in den Eingabedaten

## Wie man Overfitting erkennt

Wie Sie in der obigen Grafik sehen können, kann Overfitting durch einen sehr niedrigen Trainingsfehler und einen hohen Validierungsfehler erkannt werden. Normalerweise werden wir während des Trainings sowohl den Trainings- als auch den Validierungsfehler sehen, die beginnen zu sinken, und dann könnte der Validierungsfehler zu einem bestimmten Punkt aufhören zu sinken und anfangen zu steigen. Dies wird ein Zeichen für Overfitting sein und der Indikator, dass wir das Training wahrscheinlich an diesem Punkt stoppen sollten (oder zumindest einen Schnappschuss des Modells machen).

## Wie man Overfitting verhindert

Wenn Sie sehen, dass Overfitting auftritt, können Sie eines der folgenden tun:

 * Die Menge der Trainingsdaten erhöhen
 * Die Komplexität des Modells verringern
 * Eine Regularisierungstechnik wie Dropout verwenden, die wir später betrachten werden.

## Overfitting und Bias-Variance Tradeoff

Overfitting ist tatsächlich ein Fall eines allgemeineren Problems in der Statistik, das als Bias-Variance Tradeoff bezeichnet wird. Wenn wir die möglichen Fehlerquellen in unserem Modell betrachten, können wir zwei Arten von Fehlern sehen:

* **Bias-Fehler** entstehen dadurch, dass unser Algorithmus nicht in der Lage ist, die Beziehung zwischen den Trainingsdaten korrekt zu erfassen. Dies kann darauf zurückzuführen sein, dass unser Modell nicht mächtig genug ist (**unteranpasst**).
* **Varianzfehler**, die dadurch entstehen, dass das Modell Rauschen in den Eingabedaten anstatt einer sinnvollen Beziehung approximiert (**überanpasst**).

Während des Trainings verringert sich der Bias-Fehler (da unser Modell lernt, die Daten zu approximieren) und der Varianzfehler nimmt zu. Es ist wichtig, das Training zu stoppen - entweder manuell (wenn wir Overfitting erkennen) oder automatisch (durch Einführung von Regularisierung) - um Overfitting zu verhindern.

## Fazit

In dieser Lektion haben Sie die Unterschiede zwischen den verschiedenen APIs für die beiden beliebtesten KI-Frameworks, TensorFlow und PyTorch, kennengelernt. Außerdem haben Sie ein sehr wichtiges Thema, das Overfitting, kennengelernt.

## 🚀 Herausforderung

In den begleitenden Notebooks finden Sie 'Aufgaben' am Ende; arbeiten Sie sich durch die Notebooks und erledigen Sie die Aufgaben.

## Überprüfung & Selbststudium

Recherchieren Sie zu den folgenden Themen:

- TensorFlow
- PyTorch
- Overfitting

Stellen Sie sich die folgenden Fragen:

- Was ist der Unterschied zwischen TensorFlow und PyTorch?
- Was ist der Unterschied zwischen Overfitting und Underfitting?

## Aufgabe

In diesem Labor werden Sie aufgefordert, zwei Klassifikationsprobleme mit ein- und mehrschichtigen voll verbundenen Netzwerken unter Verwendung von PyTorch oder TensorFlow zu lösen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.