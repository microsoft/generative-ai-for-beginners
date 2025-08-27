<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "747668e4c53d067369f06e9ec2e6313e",
  "translation_date": "2025-08-26T13:49:56+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "de"
}
-->
# UX-Design für KI-Anwendungen

[![UX-Design für KI-Anwendungen](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.de.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Klicke auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

Die Nutzererfahrung ist ein sehr wichtiger Aspekt beim Entwickeln von Apps. Nutzer müssen deine App effizient nutzen können, um Aufgaben zu erledigen. Effizienz ist das eine, aber du solltest Apps auch so gestalten, dass sie von allen genutzt werden können – sie also _zugänglich_ machen. In diesem Kapitel liegt der Fokus darauf, damit du am Ende eine App entwirfst, die Menschen nutzen können und wollen.

## Einführung

User Experience beschreibt, wie ein Nutzer mit einem bestimmten Produkt oder Service interagiert und es verwendet – sei es ein System, ein Tool oder ein Design. Bei der Entwicklung von KI-Anwendungen achten Entwickler nicht nur darauf, dass die Nutzererfahrung effektiv ist, sondern auch ethisch. In dieser Lektion geht es darum, wie man KI-Anwendungen entwickelt, die die Bedürfnisse der Nutzer erfüllen.

Folgende Themen werden behandelt:

- Einführung in User Experience und das Verständnis von Nutzerbedürfnissen
- KI-Anwendungen für Vertrauen und Transparenz gestalten
- KI-Anwendungen für Zusammenarbeit und Feedback gestalten

## Lernziele

Nach dieser Lektion kannst du:

- Verstehen, wie man KI-Anwendungen entwickelt, die den Bedürfnissen der Nutzer entsprechen.
- KI-Anwendungen gestalten, die Vertrauen und Zusammenarbeit fördern.

### Voraussetzung

Nimm dir etwas Zeit und informiere dich über [User Experience und Design Thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Einführung in User Experience und das Verständnis von Nutzerbedürfnissen

In unserem fiktiven Bildungs-Startup gibt es zwei Hauptnutzer: Lehrkräfte und Schüler. Beide haben unterschiedliche Bedürfnisse. Ein nutzerzentriertes Design stellt den Nutzer in den Mittelpunkt und sorgt dafür, dass die Produkte relevant und nützlich für die Zielgruppe sind.

Die Anwendung sollte **nützlich, zuverlässig, zugänglich und angenehm** sein, um eine gute Nutzererfahrung zu bieten.

### Nutzbarkeit

Nützlich bedeutet, dass die Anwendung Funktionen bietet, die ihrem Zweck entsprechen, zum Beispiel die automatische Bewertung von Aufgaben oder das Erstellen von Lernkarten zur Wiederholung. Eine App, die den Bewertungsprozess automatisiert, sollte in der Lage sein, die Arbeiten der Schüler nach festgelegten Kriterien genau und effizient zu bewerten. Ebenso sollte eine App, die Lernkarten erstellt, relevante und vielfältige Fragen aus ihren Daten generieren können.

### Zuverlässigkeit

Zuverlässig bedeutet, dass die Anwendung ihre Aufgaben beständig und fehlerfrei ausführt. Aber KI ist – wie Menschen – nicht perfekt und kann Fehler machen. Anwendungen können auf Fehler oder unerwartete Situationen stoßen, die menschliches Eingreifen oder Korrekturen erfordern. Wie geht man mit Fehlern um? Im letzten Abschnitt dieser Lektion behandeln wir, wie KI-Systeme und Anwendungen für Zusammenarbeit und Feedback gestaltet werden.

### Zugänglichkeit

Zugänglich bedeutet, die Nutzererfahrung auch für Menschen mit unterschiedlichen Fähigkeiten zu ermöglichen, einschließlich Menschen mit Behinderungen, damit niemand ausgeschlossen wird. Wenn man sich an Richtlinien und Prinzipien zur Barrierefreiheit hält, werden KI-Lösungen inklusiver, nutzbarer und für alle Anwender vorteilhafter.

### Angenehm

Angenehm bedeutet, dass die Anwendung Spaß macht und gerne genutzt wird. Eine ansprechende Nutzererfahrung kann sich positiv auf die Nutzer auswirken, sie dazu motivieren, die Anwendung erneut zu nutzen und so den Geschäftserfolg steigern.

![Bild, das UX-Aspekte in KI illustriert](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.de.png)

Nicht jede Herausforderung lässt sich mit KI lösen. KI kann die Nutzererfahrung verbessern, zum Beispiel durch die Automatisierung manueller Aufgaben oder die Personalisierung von Nutzererlebnissen.

## KI-Anwendungen für Vertrauen und Transparenz gestalten

Vertrauen ist entscheidend beim Design von KI-Anwendungen. Vertrauen sorgt dafür, dass Nutzer sicher sind, dass die Anwendung die Arbeit erledigt, zuverlässig Ergebnisse liefert und die Resultate ihren Bedürfnissen entsprechen. Ein Risiko in diesem Bereich ist Misstrauen oder übermäßiges Vertrauen. Misstrauen entsteht, wenn ein Nutzer wenig oder kein Vertrauen in ein KI-System hat – das führt dazu, dass die Anwendung abgelehnt wird. Übermäßiges Vertrauen entsteht, wenn ein Nutzer die Fähigkeiten eines KI-Systems überschätzt und sich zu sehr darauf verlässt. Ein Beispiel: Ein automatisiertes Bewertungssystem könnte bei übermäßigem Vertrauen dazu führen, dass Lehrkräfte die Arbeiten nicht mehr selbst prüfen, um sicherzustellen, dass das System korrekt arbeitet. Das kann zu unfairen oder ungenauen Noten für die Schüler führen oder Chancen für Feedback und Verbesserungen verpassen.

Zwei Möglichkeiten, Vertrauen ins Zentrum des Designs zu stellen, sind Erklärbarkeit und Kontrolle.

### Erklärbarkeit

Wenn KI Entscheidungen unterstützt, zum Beispiel beim Vermitteln von Wissen an die nächste Generation, ist es wichtig, dass Lehrkräfte und Eltern verstehen, wie KI-Entscheidungen getroffen werden. Das ist Erklärbarkeit – zu verstehen, wie KI-Anwendungen Entscheidungen treffen. Beim Design für Erklärbarkeit sollte man Details hinzufügen, die zeigen, wie die KI zum Ergebnis gekommen ist. Die Nutzer müssen wissen, dass das Ergebnis von einer KI und nicht von einem Menschen stammt. Zum Beispiel: Statt "Beginne jetzt mit deinem Tutor zu chatten" könnte man sagen "Nutze den KI-Tutor, der sich an deine Bedürfnisse anpasst und dir hilft, in deinem Tempo zu lernen."

![Eine App-Landingpage mit klarer Darstellung von Erklärbarkeit in KI-Anwendungen](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.de.png)

Ein weiteres Beispiel ist, wie KI Nutzer- und persönliche Daten verwendet. Ein Nutzer mit der Persona "Schüler" hat vielleicht Einschränkungen, die sich aus seiner Rolle ergeben. Die KI darf zum Beispiel keine Antworten verraten, kann aber helfen, den Nutzer beim Nachdenken und Lösen von Aufgaben zu unterstützen.

![KI antwortet auf Fragen basierend auf der Persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.de.png)

Ein letzter wichtiger Aspekt der Erklärbarkeit ist die Vereinfachung von Erklärungen. Schüler und Lehrkräfte sind oft keine KI-Experten, daher sollten die Erklärungen zu den Möglichkeiten und Grenzen der Anwendung einfach und verständlich sein.

![Vereinfachte Erklärungen zu KI-Fähigkeiten](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.de.png)

### Kontrolle

Generative KI schafft eine Zusammenarbeit zwischen KI und Nutzer, bei der der Nutzer zum Beispiel Prompts anpassen kann, um unterschiedliche Ergebnisse zu erhalten. Außerdem sollten Nutzer die Möglichkeit haben, die generierten Ergebnisse zu verändern, um ein Gefühl von Kontrolle zu bekommen. Bei Bing kann man zum Beispiel den Prompt nach Format, Ton und Länge anpassen. Zusätzlich kann man das Ergebnis verändern, wie unten gezeigt:

![Bing-Suchergebnisse mit Optionen zur Anpassung des Prompts und Ergebnisses](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.de.png)

Eine weitere Funktion bei Bing, die dem Nutzer Kontrolle über die Anwendung gibt, ist die Möglichkeit, der Nutzung der Daten durch die KI zuzustimmen oder sie abzulehnen. In einer Schul-App könnte ein Schüler zum Beispiel seine eigenen Notizen und die Materialien der Lehrkraft als Lernmaterial verwenden wollen.

![Bing-Suchergebnisse mit Optionen zur Anpassung des Prompts und Ergebnisses](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.de.png)

> Beim Design von KI-Anwendungen ist es wichtig, bewusst darauf zu achten, dass Nutzer der KI nicht zu sehr vertrauen und unrealistische Erwartungen an ihre Fähigkeiten entwickeln. Eine Möglichkeit ist, bewusst Reibung zwischen Prompt und Ergebnis zu schaffen und den Nutzer daran zu erinnern, dass es sich um KI und nicht um einen Menschen handelt.

## KI-Anwendungen für Zusammenarbeit und Feedback gestalten

Wie bereits erwähnt, schafft generative KI eine Zusammenarbeit zwischen Nutzer und KI. Meistens gibt der Nutzer einen Prompt ein und die KI generiert ein Ergebnis. Was passiert, wenn das Ergebnis falsch ist? Wie geht die Anwendung mit Fehlern um? Gibt die KI dem Nutzer die Schuld oder erklärt sie den Fehler?

KI-Anwendungen sollten so gestaltet sein, dass sie Feedback empfangen und geben können. Das hilft nicht nur dem KI-System, sich zu verbessern, sondern stärkt auch das Vertrauen der Nutzer. Eine Feedback-Schleife sollte im Design enthalten sein, zum Beispiel ein einfaches Daumen hoch oder runter beim Ergebnis.

Eine weitere Möglichkeit ist, die Fähigkeiten und Grenzen des Systems klar zu kommunizieren. Wenn ein Nutzer einen Fehler macht und etwas verlangt, das die KI nicht leisten kann, sollte es eine Möglichkeit geben, damit umzugehen, wie unten gezeigt.

![Feedback geben und Fehler behandeln](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.de.png)

Systemfehler sind bei Anwendungen häufig, wenn der Nutzer Informationen außerhalb des KI-Bereichs benötigt oder die Anwendung eine Begrenzung hat, wie viele Fragen/Fächer ein Nutzer zusammenfassen kann. Ein Beispiel: Eine KI-Anwendung, die nur mit Daten zu bestimmten Fächern wie Geschichte und Mathematik trainiert wurde, kann keine Fragen zu Geografie beantworten. Um dem entgegenzuwirken, kann das KI-System zum Beispiel antworten: "Entschuldigung, unser Produkt wurde mit Daten zu folgenden Fächern trainiert..., ich kann die gestellte Frage leider nicht beantworten."

KI-Anwendungen sind nicht perfekt und machen Fehler. Beim Design deiner Anwendungen solltest du darauf achten, dass Nutzer einfach Feedback geben können und Fehler verständlich behandelt werden.

## Aufgabe

Nimm eine beliebige KI-App, die du bisher entwickelt hast, und überlege, wie du die folgenden Punkte umsetzen kannst:

- **Angenehm:** Überlege, wie du deine App angenehmer gestalten kannst. Erklärst du alles verständlich? Ermutigst du die Nutzer, die App zu erkunden? Wie formulierst du Fehlermeldungen?

- **Nutzbarkeit:** Baue eine Web-App. Stelle sicher, dass deine App sowohl mit Maus als auch mit Tastatur bedienbar ist.

- **Vertrauen und Transparenz:** Vertraue nicht blind der KI und ihren Ergebnissen. Überlege, wie du einen Menschen in den Prozess einbinden kannst, um die Ergebnisse zu überprüfen. Denke auch über andere Möglichkeiten nach, Vertrauen und Transparenz zu schaffen und setze sie um.

- **Kontrolle:** Gib dem Nutzer die Kontrolle über die Daten, die er der Anwendung zur Verfügung stellt. Implementiere eine Möglichkeit, wie Nutzer der Datenerfassung in der KI-Anwendung zustimmen oder widersprechen können.



## Lerne weiter!

Nach dieser Lektion kannst du mit unserer [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) dein Wissen zu generativer KI weiter vertiefen!

Gehe weiter zu Lektion 13, in der wir uns anschauen, wie man [KI-Anwendungen absichert](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.