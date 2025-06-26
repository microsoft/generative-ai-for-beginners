<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:15:32+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "de"
}
-->
# Einführung in Neuronale Netzwerke. Mehrschichtiger Perzeptron

Im vorherigen Abschnitt haben Sie das einfachste Modell eines neuronalen Netzwerks kennengelernt – den einlagigen Perzeptron, ein lineares Zwei-Klassen-Klassifikationsmodell.

In diesem Abschnitt erweitern wir dieses Modell zu einem flexibleren Rahmen, der es uns ermöglicht:

* **Mehrklassen-Klassifikation** zusätzlich zur Zwei-Klassen-Klassifikation durchzuführen
* **Regressionsprobleme** zusätzlich zur Klassifikation zu lösen
* Klassen zu trennen, die nicht linear trennbar sind

Wir werden auch unser eigenes modulares Framework in Python entwickeln, das es uns ermöglicht, verschiedene Architekturen von neuronalen Netzwerken zu konstruieren.

## Formalisierung des maschinellen Lernens

Beginnen wir mit der Formalisierung des maschinellen Lernproblems. Angenommen, wir haben einen Trainingsdatensatz **X** mit Labels **Y**, und wir müssen ein Modell *f* erstellen, das die genauesten Vorhersagen trifft. Die Qualität der Vorhersagen wird durch die **Verlustfunktion** ℒ gemessen. Die folgenden Verlustfunktionen werden häufig verwendet:

* Für ein Regressionsproblem, bei dem wir eine Zahl vorhersagen müssen, können wir den **absoluten Fehler** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| oder den **quadratischen Fehler** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> verwenden
* Für die Klassifikation verwenden wir den **0-1-Verlust** (der im Wesentlichen dasselbe wie die **Genauigkeit** des Modells ist) oder den **logistischen Verlust**.

Für den einlagigen Perzeptron wurde die Funktion *f* als lineare Funktion *f(x)=wx+b* definiert (hierbei ist *w* die Gewichtsmatrix, *x* der Vektor der Eingabefunktionen und *b* der Bias-Vektor). Für verschiedene Architekturen neuronaler Netzwerke kann diese Funktion eine komplexere Form annehmen.

> Im Fall der Klassifikation ist es oft wünschenswert, Wahrscheinlichkeiten der entsprechenden Klassen als Netzausgabe zu erhalten. Um beliebige Zahlen in Wahrscheinlichkeiten umzuwandeln (z.B. um die Ausgabe zu normalisieren), verwenden wir häufig die **Softmax**-Funktion σ, und die Funktion *f* wird zu *f(x)=σ(wx+b)*

In der obigen Definition von *f* werden *w* und *b* als **Parameter** θ=⟨*w,b*⟩ bezeichnet. Angesichts des Datensatzes ⟨**X**,**Y**⟩ können wir einen Gesamterror auf dem gesamten Datensatz als Funktion der Parameter θ berechnen.

> ✅ **Das Ziel des Trainings eines neuronalen Netzwerks ist es, den Fehler durch Variation der Parameter θ zu minimieren**

## Gradientabstiegsoptimierung

Es gibt eine bekannte Methode der Funktionsoptimierung, die als **Gradientenabstieg** bezeichnet wird. Die Idee ist, dass wir eine Ableitung (im mehrdimensionalen Fall als **Gradient** bezeichnet) der Verlustfunktion bezüglich der Parameter berechnen und die Parameter so variieren können, dass der Fehler abnimmt. Dies kann wie folgt formalisiert werden:

* Initialisieren Sie die Parameter mit einigen Zufallswerten w<sup>(0)</sup>, b<sup>(0)</sup>
* Wiederholen Sie den folgenden Schritt viele Male:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Während des Trainings sollten die Optimierungsschritte unter Berücksichtigung des gesamten Datensatzes berechnet werden (denken Sie daran, dass der Verlust als Summe über alle Trainingsproben berechnet wird). In der Praxis nehmen wir jedoch kleine Teile des Datensatzes, sogenannte **Minibatches**, und berechnen die Gradienten basierend auf einem Teil der Daten. Da der Teil jedes Mal zufällig genommen wird, wird diese Methode als **stochastischer Gradientenabstieg** (SGD) bezeichnet.

## Mehrschichtige Perzeptrons und Rückwärtsausbreitung

Ein einlagiges Netzwerk, wie wir oben gesehen haben, kann linear trennbare Klassen klassifizieren. Um ein reichhaltigeres Modell zu erstellen, können wir mehrere Schichten des Netzwerks kombinieren. Mathematisch bedeutet dies, dass die Funktion *f* eine komplexere Form hat und in mehreren Schritten berechnet wird:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hierbei ist α eine **nicht-lineare Aktivierungsfunktion**, σ ist eine Softmax-Funktion, und die Parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Der Gradientabstiegsalgorithmus würde gleich bleiben, aber es wäre schwieriger, die Gradienten zu berechnen. Gemäß der Kettenregel der Differenzierung können wir die Ableitungen berechnen als:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Die Kettenregel der Differenzierung wird verwendet, um die Ableitungen der Verlustfunktion bezüglich der Parameter zu berechnen.

Beachten Sie, dass der linkeste Teil all dieser Ausdrücke derselbe ist, und wir daher effektiv die Ableitungen berechnen können, indem wir von der Verlustfunktion aus "rückwärts" durch den Berechnungsgraphen gehen. Daher wird die Methode des Trainings eines mehrschichtigen Perzeptrons als **Rückwärtsausbreitung** oder 'Backprop' bezeichnet.

> TODO: Bildzitat

> ✅ Wir werden die Rückwärtsausbreitung in unserem Notizbuch-Beispiel viel detaillierter behandeln.

## Fazit

In dieser Lektion haben wir unsere eigene Bibliothek für neuronale Netzwerke erstellt und sie für eine einfache zweidimensionale Klassifikationsaufgabe verwendet.

## 🚀 Herausforderung

Im begleitenden Notizbuch implementieren Sie Ihr eigenes Framework zum Erstellen und Trainieren mehrschichtiger Perzeptrons. Sie werden im Detail sehen können, wie moderne neuronale Netzwerke arbeiten.

Gehen Sie zum OwnFramework-Notizbuch und arbeiten Sie es durch.

## Überprüfung & Selbststudium

Die Rückwärtsausbreitung ist ein gängiger Algorithmus in KI und ML, der es wert ist, im Detail studiert zu werden.

## Aufgabe

In diesem Labor werden Sie aufgefordert, das Framework, das Sie in dieser Lektion erstellt haben, zu verwenden, um die MNIST-Handschriftenerkennung zu lösen.

* Anleitungen
* Notizbuch

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.