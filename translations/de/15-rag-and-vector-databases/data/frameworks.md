<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:25:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "de"
}
-->
# Neural Network Frameworks

Wie wir bereits gelernt haben, müssen wir zwei Dinge tun, um neuronale Netzwerke effizient trainieren zu können:

* Mit Tensoren arbeiten, z. B. multiplizieren, addieren und Funktionen wie Sigmoid oder Softmax berechnen
* Die Gradienten aller Ausdrücke berechnen, um eine Gradientenabstiegsoptimierung durchzuführen

Während die `numpy`-Bibliothek den ersten Teil erledigen kann, benötigen wir einen Mechanismus zur Berechnung der Gradienten. In unserem Framework, das wir im vorherigen Abschnitt entwickelt haben, mussten wir alle Ableitungsfunktionen manuell in der `backward`-Methode programmieren, die das Backpropagation durchführt. Idealerweise sollte ein Framework uns die Möglichkeit geben, die Gradienten *beliebiger Ausdrücke* zu berechnen, die wir definieren können.

Ein weiterer wichtiger Punkt ist die Möglichkeit, Berechnungen auf der GPU oder anderen spezialisierten Recheneinheiten wie TPU durchzuführen. Das Training tiefer neuronaler Netzwerke erfordert *sehr viele* Berechnungen, und die Parallelisierung dieser Berechnungen auf GPUs ist daher sehr wichtig.

> ✅ Der Begriff 'parallelisieren' bedeutet, die Berechnungen auf mehrere Geräte zu verteilen.

Derzeit sind die beiden beliebtesten neuronalen Frameworks TensorFlow und PyTorch. Beide bieten eine Low-Level-API, um mit Tensoren sowohl auf CPU als auch GPU zu arbeiten. Auf der Low-Level-API aufbauend gibt es auch eine High-Level-API, die entsprechend Keras und PyTorch Lightning heißt.

Low-Level API | TensorFlow | PyTorch  
--------------|-------------------------------|------------------------------  
High-Level API| Keras                         | PyTorch

**Low-Level-APIs** in beiden Frameworks ermöglichen es, sogenannte **Rechen-Graphen** zu erstellen. Dieser Graph definiert, wie die Ausgabe (meist die Verlustfunktion) mit gegebenen Eingabeparametern berechnet wird und kann zur Berechnung auf die GPU ausgelagert werden, falls verfügbar. Es gibt Funktionen, um diesen Rechen-Graphen zu differenzieren und Gradienten zu berechnen, die dann zur Optimierung der Modellparameter verwendet werden können.

**High-Level-APIs** betrachten neuronale Netzwerke im Wesentlichen als **Sequenz von Schichten** und erleichtern den Aufbau der meisten neuronalen Netzwerke erheblich. Das Training des Modells erfordert normalerweise die Vorbereitung der Daten und dann den Aufruf einer `fit`-Funktion, die den Trainingsprozess übernimmt.

Die High-Level-API ermöglicht es, typische neuronale Netzwerke sehr schnell zu erstellen, ohne sich um viele Details kümmern zu müssen. Gleichzeitig bieten Low-Level-APIs viel mehr Kontrolle über den Trainingsprozess und werden daher häufig in der Forschung eingesetzt, wenn man mit neuen neuronalen Netzwerkarchitekturen arbeitet.

Es ist auch wichtig zu verstehen, dass man beide APIs zusammen verwenden kann, z. B. kann man seine eigene Netzwerkschicht-Architektur mit der Low-Level-API entwickeln und diese dann in einem größeren Netzwerk verwenden, das mit der High-Level-API erstellt und trainiert wird. Oder man definiert ein Netzwerk mit der High-Level-API als Sequenz von Schichten und verwendet dann eine eigene Low-Level-Trainingsschleife zur Optimierung. Beide APIs basieren auf denselben grundlegenden Konzepten und sind so konzipiert, dass sie gut zusammenarbeiten.

## Lernen

In diesem Kurs bieten wir den Großteil des Inhalts sowohl für PyTorch als auch für TensorFlow an. Du kannst dein bevorzugtes Framework wählen und nur die entsprechenden Notebooks durcharbeiten. Wenn du unsicher bist, welches Framework du wählen sollst, lies einige Diskussionen im Internet zum Thema **PyTorch vs. TensorFlow**. Du kannst auch beide Frameworks ausprobieren, um ein besseres Verständnis zu bekommen.

Wo immer möglich, verwenden wir aus Gründen der Einfachheit High-Level-APIs. Wir halten es jedoch für wichtig, zu verstehen, wie neuronale Netzwerke von Grund auf funktionieren, weshalb wir am Anfang mit der Low-Level-API und Tensoren arbeiten. Wenn du jedoch schnell starten möchtest und nicht viel Zeit mit diesen Details verbringen willst, kannst du diesen Teil überspringen und direkt mit den High-Level-API-Notebooks beginnen.

## ✍️ Übungen: Frameworks

Setze dein Lernen in den folgenden Notebooks fort:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|----------------------------|------------------------------  
High-Level API| Keras                      | *PyTorch Lightning*

Nachdem du die Frameworks gemeistert hast, fassen wir den Begriff Overfitting zusammen.

# Overfitting

Overfitting ist ein äußerst wichtiges Konzept im maschinellen Lernen, und es ist sehr wichtig, es richtig zu verstehen!

Betrachte folgendes Problem, bei dem 5 Punkte (im Diagramm unten durch `x` dargestellt) approximiert werden sollen:

!linear | overfit  
-------------------------|--------------------------  
**Lineares Modell, 2 Parameter** | **Nicht-lineares Modell, 7 Parameter**  
Trainingsfehler = 5,3 | Trainingsfehler = 0  
Validierungsfehler = 5,1 | Validierungsfehler = 20

* Links sehen wir eine gute Gerade als Approximation. Da die Anzahl der Parameter angemessen ist, erfasst das Modell die Verteilung der Punkte richtig.
* Rechts ist das Modell zu mächtig. Da wir nur 5 Punkte haben und das Modell 7 Parameter besitzt, kann es so angepasst werden, dass es durch alle Punkte verläuft, wodurch der Trainingsfehler 0 wird. Dies verhindert jedoch, dass das Modell das zugrundeliegende Muster der Daten versteht, weshalb der Validierungsfehler sehr hoch ist.

Es ist sehr wichtig, ein ausgewogenes Verhältnis zwischen der Komplexität des Modells (Anzahl der Parameter) und der Anzahl der Trainingsbeispiele zu finden.

## Warum Overfitting auftritt

  * Zu wenig Trainingsdaten
  * Zu mächtiges Modell
  * Zu viel Rauschen in den Eingabedaten

## Wie man Overfitting erkennt

Wie im obigen Diagramm zu sehen ist, erkennt man Overfitting an einem sehr niedrigen Trainingsfehler und einem hohen Validierungsfehler. Normalerweise sinken während des Trainings sowohl Trainings- als auch Validierungsfehler, aber irgendwann kann der Validierungsfehler aufhören zu sinken und stattdessen steigen. Dies ist ein Zeichen für Overfitting und ein Hinweis darauf, dass man das Training an dieser Stelle stoppen sollte (oder zumindest einen Snapshot des Modells machen sollte).

overfitting

## Wie man Overfitting verhindert

Wenn du erkennst, dass Overfitting auftritt, kannst du Folgendes tun:

 * Die Menge der Trainingsdaten erhöhen
 * Die Komplexität des Modells verringern
 * Eine Regularisierungstechnik verwenden, wie z. B. Dropout, die wir später behandeln werden.

## Overfitting und Bias-Variance Tradeoff

Overfitting ist eigentlich ein Fall eines allgemeineren Problems in der Statistik, das als Bias-Variance Tradeoff bezeichnet wird. Betrachtet man die möglichen Fehlerquellen in unserem Modell, so gibt es zwei Arten von Fehlern:

* **Bias-Fehler** entstehen, wenn unser Algorithmus die Beziehung in den Trainingsdaten nicht korrekt erfassen kann. Dies kann daran liegen, dass unser Modell nicht mächtig genug ist (**Underfitting**).
* **Varianz-Fehler** entstehen, wenn das Modell Rauschen in den Eingabedaten anstelle von sinnvollen Zusammenhängen approximiert (**Overfitting**).

Während des Trainings nimmt der Bias-Fehler ab (da unser Modell lernt, die Daten zu approximieren), während der Varianz-Fehler zunimmt. Es ist wichtig, das Training zu stoppen – entweder manuell (wenn Overfitting erkannt wird) oder automatisch (durch Einführung von Regularisierung) – um Overfitting zu verhindern.

## Fazit

In dieser Lektion hast du die Unterschiede zwischen den verschiedenen APIs der beiden beliebtesten KI-Frameworks TensorFlow und PyTorch kennengelernt. Außerdem hast du ein sehr wichtiges Thema behandelt: Overfitting.

## 🚀 Herausforderung

In den begleitenden Notebooks findest du unten 'Aufgaben'; arbeite die Notebooks durch und erledige die Aufgaben.

## Wiederholung & Selbststudium

Recherchiere zu folgenden Themen:

- TensorFlow  
- PyTorch  
- Overfitting

Stelle dir selbst folgende Fragen:

- Was ist der Unterschied zwischen TensorFlow und PyTorch?  
- Was ist der Unterschied zwischen Overfitting und Underfitting?

## Aufgabe

In diesem Labor sollst du zwei Klassifikationsprobleme mit ein- und mehrschichtigen vollständig verbundenen Netzwerken mit PyTorch oder TensorFlow lösen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.