<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T22:52:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "de"
}
-->
# Neuronale Netzwerk-Frameworks

Wie wir bereits gelernt haben, müssen wir zwei Dinge tun, um neuronale Netzwerke effizient trainieren zu können:

* Mit Tensoren arbeiten, z.B. multiplizieren, addieren und einige Funktionen wie Sigmoid oder Softmax berechnen
* Gradienten aller Ausdrücke berechnen, um eine Gradientenabstiegsoptimierung durchzuführen

Während die `numpy`-Bibliothek den ersten Teil übernehmen kann, benötigen wir einen Mechanismus zur Berechnung der Gradienten. In unserem Framework, das wir im vorherigen Abschnitt entwickelt haben, mussten wir alle Ableitungsfunktionen manuell innerhalb der `backward`-Methode programmieren, die die Rückwärtspropagation durchführt. Idealerweise sollte uns ein Framework die Möglichkeit bieten, Gradienten *jedes Ausdrucks* zu berechnen, den wir definieren können.

Ein weiterer wichtiger Punkt ist, Berechnungen auf der GPU oder anderen spezialisierten Recheneinheiten wie der TPU durchführen zu können. Das Training tiefer neuronaler Netzwerke erfordert *sehr viele* Berechnungen, und die Möglichkeit, diese Berechnungen auf GPUs zu parallelisieren, ist sehr wichtig.

> ✅ Der Begriff 'parallelisieren' bedeutet, die Berechnungen auf mehrere Geräte zu verteilen.

Derzeit sind die beiden beliebtesten neuronalen Frameworks: TensorFlow und PyTorch. Beide bieten eine Low-Level-API, um mit Tensoren sowohl auf der CPU als auch auf der GPU zu arbeiten. Über der Low-Level-API gibt es auch eine High-Level-API, die entsprechend Keras und PyTorch Lightning genannt wird.

Low-Level-API | TensorFlow | PyTorch
--------------|-------------------------------------|--------------------------------
High-Level-API | Keras | Pytorch

**Low-Level-APIs** in beiden Frameworks ermöglichen es Ihnen, sogenannte **Rechengraphen** zu erstellen. Dieser Graph definiert, wie das Ergebnis (normalerweise die Verlustfunktion) mit gegebenen Eingabeparametern berechnet wird und kann zur Berechnung auf die GPU geschoben werden, wenn sie verfügbar ist. Es gibt Funktionen, um diesen Rechengraphen zu differenzieren und Gradienten zu berechnen, die dann zur Optimierung der Modellparameter verwendet werden können.

**High-Level-APIs** betrachten neuronale Netzwerke im Wesentlichen als eine **Abfolge von Schichten** und erleichtern den Aufbau der meisten neuronalen Netzwerke erheblich. Das Training des Modells erfordert normalerweise die Vorbereitung der Daten und dann das Aufrufen einer `fit`-Funktion, um die Arbeit zu erledigen.

Die High-Level-API ermöglicht es, typische neuronale Netzwerke sehr schnell zu konstruieren, ohne sich um viele Details kümmern zu müssen. Gleichzeitig bieten Low-Level-APIs viel mehr Kontrolle über den Trainingsprozess und werden daher häufig in der Forschung eingesetzt, wenn Sie mit neuen neuronalen Netzwerkarchitekturen arbeiten.

Es ist auch wichtig zu verstehen, dass Sie beide APIs zusammen verwenden können, z.B. können Sie Ihre eigene Netzwerkschichtarchitektur mit der Low-Level-API entwickeln und dann innerhalb des größeren Netzwerks verwenden, das mit der High-Level-API konstruiert und trainiert wurde. Oder Sie können ein Netzwerk mit der High-Level-API als Abfolge von Schichten definieren und dann Ihre eigene Low-Level-Trainingsschleife zur Optimierung verwenden. Beide APIs verwenden die gleichen grundlegenden Konzepte und sind so konzipiert, dass sie gut zusammenarbeiten.

## Lernen

In diesem Kurs bieten wir die meisten Inhalte sowohl für PyTorch als auch für TensorFlow an. Sie können Ihr bevorzugtes Framework wählen und nur die entsprechenden Notebooks durchgehen. Wenn Sie sich nicht sicher sind, welches Framework Sie wählen sollen, lesen Sie einige Diskussionen im Internet über **PyTorch vs. TensorFlow**. Sie können sich auch beide Frameworks ansehen, um ein besseres Verständnis zu bekommen.

Wo möglich, werden wir der Einfachheit halber High-Level-APIs verwenden. Wir glauben jedoch, dass es wichtig ist, zu verstehen, wie neuronale Netzwerke von Grund auf funktionieren, daher beginnen wir damit, mit der Low-Level-API und Tensoren zu arbeiten. Wenn Sie jedoch schnell vorankommen möchten und nicht viel Zeit damit verbringen wollen, diese Details zu lernen, können Sie diese überspringen und direkt in die High-Level-API-Notebooks einsteigen.

## ✍️ Übungen: Frameworks

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Low-Level-API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-Level-API | Keras | *PyTorch Lightning*

Nachdem Sie die Frameworks gemeistert haben, lassen Sie uns das Konzept des Overfittings rekapitulieren.

# Overfitting

Overfitting ist ein äußerst wichtiges Konzept im maschinellen Lernen, und es ist sehr wichtig, es richtig zu verstehen!

Betrachten Sie das folgende Problem der Annäherung von 5 Punkten (dargestellt durch `x` in den untenstehenden Grafiken):

!linear | overfit
-------------------------|--------------------------
**Lineares Modell, 2 Parameter** | **Nicht-lineares Modell, 7 Parameter**
Trainingsfehler = 5.3 | Trainingsfehler = 0
Validierungsfehler = 5.1 | Validierungsfehler = 20

* Links sehen wir eine gute lineare Annäherung. Da die Anzahl der Parameter angemessen ist, erfasst das Modell die Idee hinter der Punktverteilung richtig.
* Rechts ist das Modell zu mächtig. Da wir nur 5 Punkte haben und das Modell 7 Parameter hat, kann es sich so anpassen, dass es durch alle Punkte geht, wodurch der Trainingsfehler 0 wird. Dies hindert das Modell jedoch daran, das richtige Muster hinter den Daten zu verstehen, wodurch der Validierungsfehler sehr hoch ist.

Es ist sehr wichtig, ein korrektes Gleichgewicht zwischen der Komplexität des Modells (Anzahl der Parameter) und der Anzahl der Trainingsbeispiele zu finden.

## Warum Overfitting auftritt

  * Nicht genug Trainingsdaten
  * Zu mächtiges Modell
  * Zu viel Rauschen in den Eingabedaten

## Wie man Overfitting erkennt

Wie Sie aus der obigen Grafik sehen können, kann Overfitting durch einen sehr niedrigen Trainingsfehler und einen hohen Validierungsfehler erkannt werden. Normalerweise sehen wir während des Trainings, dass sowohl der Trainings- als auch der Validierungsfehler beginnen zu sinken, und dann könnte der Validierungsfehler an einem Punkt aufhören zu sinken und anfangen zu steigen. Dies wird ein Zeichen für Overfitting sein und ein Hinweis darauf, dass wir das Training an diesem Punkt wahrscheinlich stoppen sollten (oder zumindest einen Schnappschuss des Modells machen).

## Wie man Overfitting verhindert

Wenn Sie sehen, dass Overfitting auftritt, können Sie eines der folgenden Dinge tun:

 * Erhöhen Sie die Menge der Trainingsdaten
 * Verringern Sie die Komplexität des Modells
 * Verwenden Sie eine Regularisierungstechnik wie Dropout, die wir später betrachten werden.

## Overfitting und Bias-Varianz-Kompromiss

Overfitting ist tatsächlich ein Fall eines allgemeineren Problems in der Statistik, das als Bias-Varianz-Kompromiss bezeichnet wird. Wenn wir die möglichen Fehlerquellen in unserem Modell betrachten, können wir zwei Arten von Fehlern sehen:

* **Bias-Fehler** entstehen dadurch, dass unser Algorithmus die Beziehung zwischen den Trainingsdaten nicht korrekt erfassen kann. Dies kann daraus resultieren, dass unser Modell nicht mächtig genug ist (**Underfitting**).
* **Varianz-Fehler**, die dadurch entstehen, dass das Modell Rauschen in den Eingabedaten statt einer sinnvollen Beziehung approximiert (**Overfitting**).

Während des Trainings nimmt der Bias-Fehler ab (da unser Modell lernt, die Daten zu approximieren), und der Varianz-Fehler nimmt zu. Es ist wichtig, das Training zu stoppen - entweder manuell (wenn wir Overfitting feststellen) oder automatisch (durch Einführung von Regularisierung) - um Overfitting zu verhindern.

## Fazit

In dieser Lektion haben Sie die Unterschiede zwischen den verschiedenen APIs für die beiden beliebtesten KI-Frameworks, TensorFlow und PyTorch, kennengelernt. Darüber hinaus haben Sie ein sehr wichtiges Thema, das Overfitting, kennengelernt.

## 🚀 Herausforderung

In den begleitenden Notebooks finden Sie 'Aufgaben' am Ende; arbeiten Sie die Notebooks durch und erledigen Sie die Aufgaben.

## Überprüfung & Selbststudium

Recherchieren Sie zu folgenden Themen:

- TensorFlow
- PyTorch
- Overfitting

Stellen Sie sich folgende Fragen:

- Was ist der Unterschied zwischen TensorFlow und PyTorch?
- Was ist der Unterschied zwischen Overfitting und Underfitting?

## Aufgabe

In diesem Labor werden Sie gebeten, zwei Klassifikationsprobleme mit ein- und mehrschichtigen vollständig verbundenen Netzwerken unter Verwendung von PyTorch oder TensorFlow zu lösen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.