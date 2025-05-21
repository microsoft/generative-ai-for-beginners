<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T21:41:56+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "de"
}
-->
# Gestaltung von UX für KI-Anwendungen

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_

Benutzererfahrung ist ein sehr wichtiger Aspekt beim Erstellen von Apps. Benutzer müssen Ihre App effizient nutzen können, um Aufgaben zu erledigen. Effizienz ist eine Sache, aber Sie müssen Apps auch so gestalten, dass sie von allen genutzt werden können, um sie _zugänglich_ zu machen. Dieses Kapitel konzentriert sich auf diesen Bereich, damit Sie hoffentlich eine App entwerfen, die Menschen nutzen können und wollen.

## Einführung

Benutzererfahrung beschreibt, wie ein Benutzer mit einem bestimmten Produkt oder Dienst interagiert und es nutzt, sei es ein System, Werkzeug oder Design. Bei der Entwicklung von KI-Anwendungen konzentrieren sich Entwickler nicht nur darauf, die Benutzererfahrung effektiv zu gestalten, sondern auch ethisch. In dieser Lektion behandeln wir, wie man Künstliche Intelligenz (KI) Anwendungen entwickelt, die den Bedürfnissen der Benutzer gerecht werden.

Die Lektion umfasst folgende Bereiche:

- Einführung in die Benutzererfahrung und Verständnis der Benutzerbedürfnisse
- Gestaltung von KI-Anwendungen für Vertrauen und Transparenz
- Gestaltung von KI-Anwendungen für Zusammenarbeit und Feedback

## Lernziele

Nach dieser Lektion können Sie:

- Verstehen, wie man KI-Anwendungen entwickelt, die den Benutzerbedürfnissen entsprechen.
- KI-Anwendungen entwerfen, die Vertrauen und Zusammenarbeit fördern.

### Voraussetzung

Nehmen Sie sich etwas Zeit und lesen Sie mehr über [Benutzererfahrung und Design Thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Einführung in die Benutzererfahrung und Verständnis der Benutzerbedürfnisse

In unserem fiktiven Bildungs-Startup haben wir zwei Hauptnutzer: Lehrer und Schüler. Jeder der beiden Nutzer hat einzigartige Bedürfnisse. Ein benutzerzentriertes Design priorisiert den Benutzer und stellt sicher, dass die Produkte für die beabsichtigten Nutzer relevant und nützlich sind.

Die Anwendung sollte **nützlich, zuverlässig, zugänglich und angenehm** sein, um eine gute Benutzererfahrung zu bieten.

### Benutzerfreundlichkeit

Nützlich zu sein bedeutet, dass die Anwendung Funktionen hat, die ihrem beabsichtigten Zweck entsprechen, wie z.B. die Automatisierung des Bewertungsprozesses oder das Erstellen von Karteikarten zur Wiederholung. Eine Anwendung, die den Bewertungsprozess automatisiert, sollte in der Lage sein, Schülerarbeiten anhand vordefinierter Kriterien genau und effizient zu bewerten. Ebenso sollte eine Anwendung, die Wiederholungskarteikarten erstellt, relevante und vielfältige Fragen basierend auf ihren Daten generieren können.

### Zuverlässigkeit

Zuverlässig zu sein bedeutet, dass die Anwendung ihre Aufgabe konsistent und fehlerfrei ausführen kann. Allerdings ist KI, genau wie Menschen, nicht perfekt und kann anfällig für Fehler sein. Die Anwendungen können auf Fehler oder unerwartete Situationen stoßen, die menschliches Eingreifen oder Korrekturen erfordern. Wie gehen Sie mit Fehlern um? Im letzten Abschnitt dieser Lektion werden wir behandeln, wie KI-Systeme und -Anwendungen für Zusammenarbeit und Feedback gestaltet werden.

### Zugänglichkeit

Zugänglich zu sein bedeutet, die Benutzererfahrung auf Nutzer mit unterschiedlichen Fähigkeiten, einschließlich Behinderungen, auszudehnen, um sicherzustellen, dass niemand ausgeschlossen wird. Durch die Einhaltung von Richtlinien und Prinzipien zur Barrierefreiheit werden KI-Lösungen inklusiver, nutzbarer und nützlicher für alle Nutzer.

### Angenehm

Angenehm zu sein bedeutet, dass die Anwendung Freude bereitet. Eine ansprechende Benutzererfahrung kann einen positiven Einfluss auf den Benutzer haben, ihn ermutigen, zur Anwendung zurückzukehren, und den Geschäftserfolg steigern.

Nicht jede Herausforderung kann mit KI gelöst werden. KI ergänzt Ihre Benutzererfahrung, sei es durch die Automatisierung manueller Aufgaben oder die Personalisierung von Benutzererlebnissen.

## Gestaltung von KI-Anwendungen für Vertrauen und Transparenz

Vertrauen aufzubauen ist entscheidend bei der Gestaltung von KI-Anwendungen. Vertrauen stellt sicher, dass ein Benutzer darauf vertraut, dass die Anwendung die Arbeit erledigt, konsistent Ergebnisse liefert und die Ergebnisse das sind, was der Benutzer benötigt. Ein Risiko in diesem Bereich ist Misstrauen und Übervertrauen. Misstrauen tritt auf, wenn ein Benutzer wenig oder kein Vertrauen in ein KI-System hat, was dazu führt, dass der Benutzer Ihre Anwendung ablehnt. Übervertrauen tritt auf, wenn ein Benutzer die Fähigkeit eines KI-Systems überschätzt, was dazu führt, dass die Benutzer dem KI-System zu sehr vertrauen. Ein Beispiel dafür ist ein automatisiertes Bewertungssystem, das bei Übervertrauen dazu führen könnte, dass der Lehrer einige der Arbeiten nicht überprüft, um sicherzustellen, dass das Bewertungssystem gut funktioniert. Dies könnte zu unfairen oder ungenauen Noten für die Schüler oder verpassten Gelegenheiten für Feedback und Verbesserung führen.

Zwei Möglichkeiten, um sicherzustellen, dass Vertrauen im Mittelpunkt des Designs steht, sind Erklärbarkeit und Kontrolle.

### Erklärbarkeit

Wenn KI bei Entscheidungen hilft, wie z.B. Wissen an zukünftige Generationen zu vermitteln, ist es entscheidend, dass Lehrer und Eltern verstehen, wie KI-Entscheidungen getroffen werden. Dies ist Erklärbarkeit - das Verständnis, wie KI-Anwendungen Entscheidungen treffen. Die Gestaltung für Erklärbarkeit beinhaltet das Hinzufügen von Details zu Beispielen, was eine KI-Anwendung tun kann. Zum Beispiel, anstatt "Starten Sie mit dem KI-Lehrer", könnte das System verwenden: "Fassen Sie Ihre Notizen für eine einfachere Wiederholung mit KI zusammen."

Ein weiteres Beispiel ist, wie KI Benutzer- und persönliche Daten verwendet. Zum Beispiel kann ein Benutzer mit der Persona "Schüler" Einschränkungen basierend auf seiner Persona haben. Die KI kann möglicherweise keine Antworten auf Fragen geben, aber sie kann den Benutzer dazu anleiten, darüber nachzudenken, wie er ein Problem lösen kann.

Ein letzter wichtiger Teil der Erklärbarkeit ist die Vereinfachung der Erklärungen. Schüler und Lehrer sind möglicherweise keine KI-Experten, daher sollten die Erklärungen darüber, was die Anwendung kann oder nicht kann, vereinfacht und leicht verständlich sein.

### Kontrolle

Generative KI schafft eine Zusammenarbeit zwischen KI und dem Benutzer, bei der ein Benutzer beispielsweise Eingabeaufforderungen für unterschiedliche Ergebnisse ändern kann. Darüber hinaus sollten Benutzer, sobald ein Ergebnis generiert wurde, die Möglichkeit haben, die Ergebnisse zu ändern und ihnen ein Gefühl der Kontrolle zu geben. Zum Beispiel können Sie bei der Verwendung von Bing Ihre Eingabeaufforderung basierend auf Format, Ton und Länge anpassen. Darüber hinaus können Sie Änderungen an Ihrem Ergebnis vornehmen und das Ergebnis wie unten gezeigt ändern:

Ein weiteres Merkmal von Bing, das einem Benutzer die Kontrolle über die Anwendung ermöglicht, ist die Möglichkeit, sich in die von der KI verwendeten Daten ein- und auszutragen. Für eine Schul-Anwendung möchte ein Schüler möglicherweise seine Notizen sowie die Ressourcen der Lehrer als Wiederholungsmaterial verwenden.

> Bei der Gestaltung von KI-Anwendungen ist Absicht entscheidend, um sicherzustellen, dass Benutzer nicht übertrieben vertrauen und unrealistische Erwartungen an die Fähigkeiten haben. Eine Möglichkeit, dies zu tun, besteht darin, Reibung zwischen den Eingabeaufforderungen und den Ergebnissen zu erzeugen. Erinnern Sie den Benutzer daran, dass dies KI ist und kein Mitmensch

## Gestaltung von KI-Anwendungen für Zusammenarbeit und Feedback

Wie bereits erwähnt, schafft generative KI eine Zusammenarbeit zwischen dem Benutzer und der KI. Die meisten Interaktionen bestehen darin, dass ein Benutzer eine Eingabeaufforderung eingibt und die KI ein Ergebnis generiert. Was, wenn das Ergebnis falsch ist? Wie geht die Anwendung mit Fehlern um, wenn sie auftreten? Gibt die KI dem Benutzer die Schuld oder nimmt sie sich die Zeit, den Fehler zu erklären?

KI-Anwendungen sollten so gebaut werden, dass sie Feedback erhalten und geben. Dies hilft nicht nur dem KI-System, sich zu verbessern, sondern baut auch Vertrauen bei den Benutzern auf. Eine Feedback-Schleife sollte im Design enthalten sein, ein Beispiel könnte ein einfaches Daumen hoch oder runter auf dem Ergebnis sein.

Eine weitere Möglichkeit, damit umzugehen, besteht darin, die Fähigkeiten und Grenzen des Systems klar zu kommunizieren. Wenn ein Benutzer einen Fehler macht und etwas anfordert, das über die Fähigkeiten der KI hinausgeht, sollte es auch eine Möglichkeit geben, damit umzugehen, wie unten gezeigt.

Systemfehler sind häufig bei Anwendungen, bei denen der Benutzer möglicherweise Hilfe bei Informationen benötigt, die außerhalb des Rahmens der KI liegen, oder die Anwendung hat möglicherweise ein Limit, wie viele Fragen/Fächer ein Benutzer Zusammenfassungen generieren kann. Zum Beispiel kann eine KI-Anwendung, die mit Daten zu begrenzten Fächern wie Geschichte und Mathematik trainiert wurde, möglicherweise keine Fragen zur Geografie bearbeiten. Um dies abzumildern, kann das KI-System eine Antwort wie: "Entschuldigung, unser Produkt wurde mit Daten in den folgenden Fächern trainiert....., ich kann auf die von Ihnen gestellte Frage nicht antworten."

KI-Anwendungen sind nicht perfekt, daher machen sie zwangsläufig Fehler. Beim Entwerfen Ihrer Anwendungen sollten Sie sicherstellen, dass Sie Raum für Feedback von Benutzern und Fehlerbehebung auf eine einfache und leicht verständliche Weise schaffen.

## Aufgabe

Nehmen Sie sich eine beliebige KI-App, die Sie bisher erstellt haben, und überlegen Sie, wie Sie die folgenden Schritte in Ihrer App implementieren können:

- **Angenehm:** Überlegen Sie, wie Sie Ihre App angenehmer gestalten können. Fügen Sie überall Erklärungen hinzu? Ermutigen Sie den Benutzer zur Erkundung? Wie formulieren Sie Ihre Fehlermeldungen?

- **Benutzerfreundlichkeit:** Erstellen Sie eine Web-App. Stellen Sie sicher, dass Ihre App sowohl mit Maus als auch mit Tastatur navigierbar ist.

- **Vertrauen und Transparenz:** Vertrauen Sie der KI und ihren Ergebnissen nicht vollständig, überlegen Sie, wie Sie einen Menschen in den Prozess einbinden könnten, um die Ergebnisse zu überprüfen. Erwägen und implementieren Sie auch andere Möglichkeiten, um Vertrauen und Transparenz zu erreichen.

- **Kontrolle:** Geben Sie dem Benutzer die Kontrolle über die Daten, die er der Anwendung zur Verfügung stellt. Implementieren Sie eine Möglichkeit, wie ein Benutzer sich in die Datenerfassung in der KI-Anwendung ein- und austragen kann.

## Setzen Sie Ihr Lernen fort!

Nachdem Sie diese Lektion abgeschlossen haben, schauen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter auszubauen!

Schauen Sie sich Lektion 13 an, in der wir uns mit der [Sicherung von KI-Anwendungen](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) befassen werden!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.