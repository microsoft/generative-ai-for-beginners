<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:40:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "de"
}
-->
# Einführung in Neuronale Netze. Mehrschichtiger Perzeptron

Im vorherigen Abschnitt hast du das einfachste Modell eines neuronalen Netzes kennengelernt – den einlagigen Perzeptron, ein lineares Zwei-Klassen-Klassifikationsmodell.

In diesem Abschnitt erweitern wir dieses Modell zu einem flexibleren Rahmen, der es uns ermöglicht:

* neben der Zwei-Klassen-Klassifikation auch **Mehrklassenklassifikation** durchzuführen
* neben Klassifikationsproblemen auch **Regressionsprobleme** zu lösen
* Klassen zu trennen, die nicht linear separierbar sind

Außerdem entwickeln wir unser eigenes modulares Framework in Python, mit dem wir verschiedene Architekturen neuronaler Netze aufbauen können.

## Formalisierung des Machine Learning

Beginnen wir mit der Formalisierung des Machine-Learning-Problems. Angenommen, wir haben einen Trainingsdatensatz **X** mit Labels **Y** und müssen ein Modell *f* erstellen, das möglichst genaue Vorhersagen trifft. Die Qualität der Vorhersagen wird durch die **Loss-Funktion** ℒ gemessen. Häufig verwendete Loss-Funktionen sind:

* Für Regressionsprobleme, bei denen eine Zahl vorhergesagt werden soll, können wir den **absoluten Fehler** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| oder den **quadratischen Fehler** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> verwenden
* Für Klassifikation nutzen wir die **0-1-Loss** (die im Grunde der **Genauigkeit** des Modells entspricht) oder die **logistische Loss**

Für den einlagigen Perzeptron wurde die Funktion *f* als lineare Funktion *f(x)=wx+b* definiert (wobei *w* die Gewichtsmatrix, *x* der Vektor der Eingabemerkmale und *b* der Bias-Vektor ist). Für verschiedene Architekturen neuronaler Netze kann diese Funktion komplexer sein.

> Im Fall der Klassifikation ist es oft wünschenswert, Wahrscheinlichkeiten der jeweiligen Klassen als Netzwerkausgabe zu erhalten. Um beliebige Zahlen in Wahrscheinlichkeiten umzuwandeln (z.B. zur Normalisierung der Ausgabe), verwenden wir häufig die **softmax**-Funktion σ, wodurch die Funktion *f* zu *f(x)=σ(wx+b)* wird.

In der obigen Definition von *f* werden *w* und *b* als **Parameter** θ=⟨*w,b*⟩ bezeichnet. Gegeben den Datensatz ⟨**X**,**Y**⟩, können wir den Gesamtfehler über den gesamten Datensatz als Funktion der Parameter θ berechnen.

> ✅ **Das Ziel des Trainings eines neuronalen Netzes ist es, den Fehler durch Variation der Parameter θ zu minimieren**

## Gradient Descent Optimierung

Es gibt eine bekannte Methode zur Optimierung von Funktionen, die **Gradient Descent** genannt wird. Die Idee ist, dass wir die Ableitung (im mehrdimensionalen Fall den **Gradienten**) der Loss-Funktion bezüglich der Parameter berechnen können und die Parameter so anpassen, dass der Fehler abnimmt. Formal lässt sich das so ausdrücken:

* Initialisiere die Parameter mit zufälligen Werten w<sup>(0)</sup>, b<sup>(0)</sup>
* Wiederhole den folgenden Schritt viele Male:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup> - η ∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup> - η ∂ℒ/∂b

Während des Trainings werden die Optimierungsschritte eigentlich unter Berücksichtigung des gesamten Datensatzes berechnet (denk daran, dass der Loss als Summe über alle Trainingsbeispiele berechnet wird). In der Praxis nehmen wir jedoch kleine Teilmengen des Datensatzes, sogenannte **Minibatches**, und berechnen die Gradienten nur auf Basis dieser Teilmenge. Da die Teilmenge jedes Mal zufällig gewählt wird, nennt man diese Methode **stochastischer Gradient Descent** (SGD).

## Mehrschichtige Perzeptrons und Backpropagation

Ein einlagiges Netzwerk, wie oben gezeigt, kann linear separierbare Klassen klassifizieren. Um ein komplexeres Modell zu bauen, können wir mehrere Schichten des Netzwerks kombinieren. Mathematisch bedeutet das, dass die Funktion *f* eine komplexere Form annimmt und in mehreren Schritten berechnet wird:
* z<sub>1</sub> = w<sub>1</sub>x + b<sub>1</sub>
* z<sub>2</sub> = w<sub>2</sub> α(z<sub>1</sub>) + b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hierbei ist α eine **nichtlineare Aktivierungsfunktion**, σ die softmax-Funktion, und die Parameter sind θ = ⟨*w<sub>1</sub>, b<sub>1</sub>, w<sub>2</sub>, b<sub>2</sub>*⟩.

Der Gradient-Descent-Algorithmus bleibt gleich, aber die Berechnung der Gradienten wird komplexer. Mithilfe der Kettenregel der Differentiation können wir die Ableitungen folgendermaßen berechnen:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Die Kettenregel wird verwendet, um die Ableitungen der Loss-Funktion bezüglich der Parameter zu berechnen.

Beachte, dass der linkeste Teil all dieser Ausdrücke gleich ist, sodass wir die Ableitungen effektiv ausgehend von der Loss-Funktion „rückwärts“ durch den Berechnungsgraphen berechnen können. Daher wird die Methode zum Training eines mehrschichtigen Perzeptrons **Backpropagation** oder kurz „Backprop“ genannt.

> TODO: Bildquelle

> ✅ Wir werden Backpropagation in unserem Notebook-Beispiel noch viel ausführlicher behandeln.

## Fazit

In dieser Lektion haben wir unsere eigene Bibliothek für neuronale Netze erstellt und sie für eine einfache zweidimensionale Klassifikationsaufgabe verwendet.

## 🚀 Herausforderung

Im begleitenden Notebook wirst du dein eigenes Framework zum Aufbau und Training mehrschichtiger Perzeptrons implementieren. Du wirst im Detail sehen, wie moderne neuronale Netze funktionieren.

Gehe zum OwnFramework-Notebook und arbeite es durch.

## Rückblick & Selbststudium

Backpropagation ist ein gängiger Algorithmus in KI und ML, der es wert ist, genauer studiert zu werden.

## Aufgabe

In diesem Labor sollst du das in dieser Lektion erstellte Framework verwenden, um die Klassifikation handgeschriebener Ziffern aus dem MNIST-Datensatz zu lösen.

* Anweisungen
* Notebook

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.