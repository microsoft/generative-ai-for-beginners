<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:11:10+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "de"
}
-->
# Einführung in neuronale Netze. Mehrschichtiges Perzeptron

Im vorherigen Abschnitt haben Sie das einfachste Modell eines neuronalen Netzes kennengelernt - das einlagige Perzeptron, ein lineares Zwei-Klassen-Klassifikationsmodell.

In diesem Abschnitt werden wir dieses Modell in ein flexibleres Framework erweitern, das es uns ermöglicht:

* **Mehrklassenklassifikation** zusätzlich zur Zwei-Klassen-Klassifikation durchzuführen
* **Regressionsprobleme** zusätzlich zur Klassifikation zu lösen
* Klassen zu trennen, die nicht linear separierbar sind

Wir werden auch unser eigenes modulares Framework in Python entwickeln, das es uns ermöglicht, verschiedene Architekturen von neuronalen Netzen zu konstruieren.

## Formalisierung des maschinellen Lernens

Beginnen wir mit der Formalisierung des Problems des maschinellen Lernens. Angenommen, wir haben einen Trainingsdatensatz **X** mit Labels **Y**, und wir müssen ein Modell *f* erstellen, das die genauesten Vorhersagen trifft. Die Qualität der Vorhersagen wird durch die **Verlustfunktion** ℒ gemessen. Die folgenden Verlustfunktionen werden häufig verwendet:

* Für Regressionsprobleme, wenn wir eine Zahl vorhersagen müssen, können wir den **absoluten Fehler** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| oder den **quadratischen Fehler** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> verwenden
* Für die Klassifikation verwenden wir den **0-1-Verlust** (was im Wesentlichen dasselbe ist wie die **Genauigkeit** des Modells) oder den **logistischen Verlust**.

Für das einlagige Perzeptron wurde die Funktion *f* als lineare Funktion *f(x)=wx+b* definiert (hier ist *w* die Gewichtsmatrix, *x* ist der Vektor der Eingabefeatures und *b* ist der Bias-Vektor). Für verschiedene Architekturen von neuronalen Netzen kann diese Funktion eine komplexere Form annehmen.

> Im Fall der Klassifikation ist es oft wünschenswert, Wahrscheinlichkeiten der entsprechenden Klassen als Netzwerkausgabe zu erhalten. Um beliebige Zahlen in Wahrscheinlichkeiten umzuwandeln (z.B. um die Ausgabe zu normalisieren), verwenden wir oft die **Softmax-Funktion** σ, und die Funktion *f* wird zu *f(x)=σ(wx+b)*

In der Definition von *f* oben werden *w* und *b* als **Parameter** θ=⟨*w,b*⟩ bezeichnet. Angesichts des Datensatzes ⟨**X**,**Y**⟩ können wir einen Gesamten Fehler für den gesamten Datensatz als Funktion der Parameter θ berechnen.

> ✅ **Das Ziel des Trainings von neuronalen Netzen ist es, den Fehler durch Variation der Parameter θ zu minimieren**

## Gradient-Abstiegsoptimierung

Es gibt eine bekannte Methode der Funktionsoptimierung namens **Gradientenabstieg**. Die Idee ist, dass wir eine Ableitung (im mehrdimensionalen Fall **Gradient** genannt) der Verlustfunktion bezüglich der Parameter berechnen können und die Parameter so variieren, dass der Fehler abnimmt. Dies kann wie folgt formalisiert werden:

* Initialisieren Sie die Parameter mit einigen Zufallswerten w<sup>(0)</sup>, b<sup>(0)</sup>
* Wiederholen Sie den folgenden Schritt viele Male:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Während des Trainings sollen die Optimierungsschritte unter Berücksichtigung des gesamten Datensatzes berechnet werden (denken Sie daran, dass der Verlust als Summe über alle Trainingsproben berechnet wird). In der Realität nehmen wir jedoch kleine Teile des Datensatzes, sogenannte **Minibatches**, und berechnen die Gradienten basierend auf einem Teil der Daten. Da der Teil jedes Mal zufällig gewählt wird, wird diese Methode als **stochastischer Gradientenabstieg** (SGD) bezeichnet.

## Mehrschichtige Perzeptrons und Backpropagation

Ein einlagiges Netzwerk, wie wir oben gesehen haben, ist in der Lage, linear separierbare Klassen zu klassifizieren. Um ein reichhaltigeres Modell zu erstellen, können wir mehrere Schichten des Netzwerks kombinieren. Mathematisch würde dies bedeuten, dass die Funktion *f* eine komplexere Form hat und in mehreren Schritten berechnet wird:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hier ist α eine **nichtlineare Aktivierungsfunktion**, σ ist eine Softmax-Funktion und die Parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Der Gradientenabstiegsalgorithmus würde gleich bleiben, aber es wäre schwieriger, die Gradienten zu berechnen. Angesichts der Kettenregel der Differentiation können wir die Ableitungen wie folgt berechnen:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Die Kettenregel der Differentiation wird verwendet, um die Ableitungen der Verlustfunktion bezüglich der Parameter zu berechnen.

Beachten Sie, dass der linke Teil all dieser Ausdrücke gleich ist und wir daher die Ableitungen effektiv berechnen können, indem wir von der Verlustfunktion aus "rückwärts" durch den Berechnungsgraphen gehen. Daher wird die Methode des Trainings eines mehrschichtigen Perzeptrons als **Backpropagation** oder 'Backprop' bezeichnet.

> TODO: Bildzitat

> ✅ Wir werden Backprop in unserem Notebook-Beispiel viel detaillierter behandeln.  

## Fazit

In dieser Lektion haben wir unsere eigene Bibliothek für neuronale Netze erstellt und sie für eine einfache zweidimensionale Klassifikationsaufgabe verwendet.

## 🚀 Herausforderung

Im begleitenden Notebook werden Sie Ihr eigenes Framework für den Bau und das Training mehrschichtiger Perzeptrons implementieren. Sie werden im Detail sehen können, wie moderne neuronale Netze arbeiten.

Gehen Sie zum OwnFramework-Notebook und arbeiten Sie es durch.

## Überprüfung & Selbststudium

Backpropagation ist ein häufig verwendeter Algorithmus in KI und ML, der es wert ist, im Detail studiert zu werden.

## Aufgabe

In diesem Labor werden Sie aufgefordert, das Framework, das Sie in dieser Lektion erstellt haben, zur Lösung der MNIST-Handschriftenerkennung zu verwenden.

* Anweisungen
* Notebook

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.