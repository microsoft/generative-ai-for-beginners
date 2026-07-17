# Erstellung von generativen KI-gestützten Chat-Anwendungen

[![Erstellung von generativen KI-gestützten Chat-Anwendungen](../../../translated_images/de/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Nun, da wir gesehen haben, wie wir Textgenerierungs-Apps bauen können, schauen wir uns Chat-Anwendungen an.

Chat-Anwendungen sind in unser tägliches Leben integriert und bieten mehr als nur eine Möglichkeit für zwanglose Unterhaltungen. Sie sind wesentliche Bestandteile des Kundendienstes, technischen Supports und sogar hochentwickelter Beratungssysteme. Wahrscheinlich haben Sie vor nicht allzu langer Zeit Hilfe von einer Chat-Anwendung erhalten. Mit der Integration fortschrittlicher Technologien wie generativer KI in diese Plattformen steigt die Komplexität, ebenso wie die Herausforderungen.

Einige Fragen, die beantwortet werden müssen, lauten:

- **Erstellung der Anwendung**. Wie bauen wir diese KI-gestützten Anwendungen effizient und integrieren sie nahtlos für spezifische Anwendungsfälle?
- **Überwachung**. Nach der Bereitstellung, wie können wir überwachen und sicherstellen, dass die Anwendungen sowohl funktional als auch im Einklang mit den [sechs Grundsätzen für verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) auf höchstem Qualitätsniveau arbeiten?

Während wir weiter in ein Zeitalter vordringen, das von Automatisierung und nahtlosen Mensch-Maschine-Interaktionen geprägt ist, wird es entscheidend zu verstehen, wie generative KI den Umfang, die Tiefe und die Anpassungsfähigkeit von Chat-Anwendungen verändert. Diese Lektion untersucht die architektonischen Aspekte, die diese komplexen Systeme unterstützen, beleuchtet die Methoden zur Feinabstimmung für domänenspezifische Aufgaben und bewertet die Metriken sowie Überlegungen, die für eine verantwortungsbewusste KI-Bereitstellung relevant sind.

## Einführung

Diese Lektion umfasst:

- Techniken zum effizienten Aufbau und zur Integration von Chat-Anwendungen.
- Wie man Anpassungen und Feinabstimmungen bei Anwendungen anwendet.
- Strategien und Überlegungen zur effektiven Überwachung von Chat-Anwendungen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Überlegungen zum Bau und zur Integration von Chat-Anwendungen in bestehende Systeme zu beschreiben.
- Chat-Anwendungen für spezifische Anwendungsfälle anzupassen.
- Wichtige Metriken und Überlegungen zu identifizieren, um die Qualität von KI-gestützten Chat-Anwendungen effektiv zu überwachen und aufrechtzuerhalten.
- Sicherzustellen, dass Chat-Anwendungen KI verantwortungsvoll nutzen.

## Integration von generativer KI in Chat-Anwendungen

Die Verbesserung von Chat-Anwendungen durch generative KI konzentriert sich nicht nur darauf, sie intelligenter zu machen; es geht vielmehr darum, ihre Architektur, Leistung und Benutzeroberfläche zu optimieren, um eine qualitativ hochwertige Benutzererfahrung zu bieten. Dies beinhaltet die Untersuchung der architektonischen Grundlagen, API-Integrationen und Überlegungen zur Benutzeroberfläche. Dieser Abschnitt bietet Ihnen eine umfassende Roadmap, um diese komplexen Bereiche zu navigieren – egal, ob Sie sie in bestehende Systeme einbinden oder als eigenständige Plattformen erstellen.

Am Ende dieses Abschnitts verfügen Sie über das nötige Fachwissen, um Chat-Anwendungen effizient zu erstellen und zu integrieren.

### Chatbot oder Chat-Anwendung?

Bevor wir in den Bau von Chat-Anwendungen eintauchen, vergleichen wir „Chatbots“ mit „KI-gestützten Chat-Anwendungen“, die unterschiedliche Rollen und Funktionalitäten bedienen. Ein Chatbot hat hauptsächlich die Aufgabe, spezifische Konversationsaufgaben zu automatisieren, wie zum Beispiel das Beantworten häufig gestellter Fragen oder das Verfolgen eines Pakets. Er wird typischerweise durch regelbasierte Logik oder komplexe KI-Algorithmen gesteuert. Im Gegensatz dazu ist eine KI-gestützte Chat-Anwendung ein weitaus umfassenderes Umfeld, das verschiedene Formen der digitalen Kommunikation ermöglicht, z.B. Text-, Sprach- und Video-Chats zwischen menschlichen Nutzern. Ihr prägendes Merkmal ist die Integration eines generativen KI-Modells, das nuancierte, menschenähnliche Gespräche simuliert und auf einer Vielzahl von Eingangs- und Kontexthinweisen basierende Antworten generiert. Eine generativ KI-gestützte Chat-Anwendung kann offene Gespräche führen, sich an sich ändernde Gesprächskontexte anpassen und sogar kreative oder komplexe Dialoge erzeugen.

Die folgende Tabelle zeigt die wichtigsten Unterschiede und Gemeinsamkeiten, um ihre einzigartigen Rollen in der digitalen Kommunikation verständlich zu machen.

| Chatbot                               | Generative KI-gestützte Chat-Anwendung                      |
| ------------------------------------- | ----------------------------------------------------------- |
| Aufgabenorientiert und regelbasiert   | Kontextbewusst                                             |
| Oft in größere Systeme integriert     | Kann einen oder mehrere Chatbots hosten                     |
| Auf programmierte Funktionen beschränkt | Integriert generative KI-Modelle                           |
| Spezialisierte & strukturierte Interaktionen | Fähig zu offenen Diskussionen                            |

### Nutzung vorgefertigter Funktionalitäten mit SDKs und APIs

Beim Erstellen einer Chat-Anwendung ist ein guter erster Schritt, zu bewerten, was bereits vorhanden ist. Die Verwendung von SDKs und APIs beim Bau von Chat-Anwendungen ist aus verschiedenen Gründen eine vorteilhafte Strategie. Durch die Integration gut dokumentierter SDKs und APIs positionieren Sie Ihre Anwendung strategisch für langfristigen Erfolg und adressieren Skalierbarkeits- und Wartungsaspekte.

- **Beschleunigt den Entwicklungsprozess und reduziert den Aufwand**: Die Nutzung vorgefertigter Funktionalitäten anstelle des kostspieligen Prozesses, diese selbst zu erstellen, erlaubt Ihnen, sich auf andere Aspekte Ihrer Anwendung zu konzentrieren, die Sie möglicherweise wichtiger finden, wie z.B. die Geschäftslogik.
- **Bessere Leistung**: Beim Aufbau von Funktionalität von Grund auf fragen Sie sich irgendwann: „Wie skaliert das? Kann diese Anwendung plötzlich steigende Nutzerzahlen bewältigen?“ Gut gepflegte SDKs und APIs haben oft eingebaute Lösungen für diese Anliegen.
- **Leichtere Wartung**: Updates und Verbesserungen sind einfacher zu handhaben, da die meisten APIs und SDKs einfach ein Update einer Bibliothek erfordern, wenn eine neuere Version veröffentlicht wird.
- **Zugang zu Spitzentechnologie**: Die Nutzung von Modellen, die feinabgestimmt und auf umfangreichen Datensätzen trainiert wurden, bietet Ihrer Anwendung Fähigkeiten in natürlicher Sprachverarbeitung.

Der Zugriff auf Funktionalitäten eines SDKs oder einer API erfolgt typischerweise durch die Erteilung der Berechtigung zur Nutzung der angebotenen Dienste, oft mittels eines einzigartigen Schlüssels oder Authentifizierungs-Tokens. Wir werden die OpenAI Python Bibliothek nutzen, um zu zeigen, wie das aussieht. Sie können dies auch selbst im folgenden [OpenAI-Notebook](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) oder [Azure OpenAI-Notebook](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) für diese Lektion ausprobieren.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Das obige Beispiel verwendet das GPT-5 mini Modell mit der Responses API, um die Eingabe zu vervollständigen, aber beachten Sie, dass der API-Schlüssel vorher gesetzt werden muss. Sie würden einen Fehler erhalten, wenn Sie den Schlüssel nicht setzen.

## Benutzererfahrung (UX)

Allgemeine UX-Prinzipien gelten für Chat-Anwendungen, aber hier sind einige zusätzliche Überlegungen, die durch die maschinellen Lernkomponenten besonders wichtig werden.

- **Mechanismus zur Klärung von Mehrdeutigkeiten**: Generative KI-Modelle erzeugen gelegentlich mehrdeutige Antworten. Eine Funktion, die den Nutzern ermöglicht, um Erläuterung zu bitten, kann hilfreich sein, wenn sie auf dieses Problem stoßen.
- **Kontextbeibehaltung**: Fortschrittliche generative KI-Modelle können den Kontext innerhalb eines Gesprächs behalten, was ein notwendiger Vorteil für die Benutzererfahrung sein kann. Nutzern die Möglichkeit zu geben, den Kontext zu kontrollieren und zu verwalten, verbessert die Nutzererfahrung, birgt aber das Risiko, sensible Benutzerdaten zu speichern. Überlegungen, wie lange diese Daten gespeichert werden, z.B. die Einführung einer Aufbewahrungsrichtlinie, können den Bedarf an Kontext mit Datenschutz abwägen.
- **Personalisierung**: Mit der Fähigkeit zu lernen und sich anzupassen, bieten KI-Modelle eine individualisierte Erfahrung für Nutzer. Die Anpassung der Nutzererfahrung durch Funktionen wie Nutzerprofile vermittelt nicht nur das Gefühl, verstanden zu werden, sondern unterstützt auch das Finden spezifischer Antworten und schafft eine effizientere und zufriedenstellendere Interaktion.

Ein Beispiel für Personalisierung sind die „Custom instructions“-Einstellungen in OpenAIs ChatGPT. Sie ermöglichen es Ihnen, Informationen über sich selbst bereitzustellen, die für Ihre Eingaben wichtig sein könnten. Hier ein Beispiel für eine individuelle Anweisung.

![Einstellungen für benutzerdefinierte Anweisungen in ChatGPT](../../../translated_images/de/custom-instructions.b96f59aa69356fcf.webp)

Dieses „Profil“ veranlasst ChatGPT, einen Lehrplan über verkettete Listen zu erstellen. Beachten Sie, dass ChatGPT berücksichtigt, dass die Nutzerin möglicherweise einen detaillierteren Lehrplan basierend auf ihrer Erfahrung möchte.

![Eine Eingabeaufforderung in ChatGPT für einen Lehrplan über verkettete Listen](../../../translated_images/de/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofts System Message Framework für große Sprachmodelle

[Microsoft hat Richtlinien bereitgestellt](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) für das Schreiben effektiver Systemnachrichten bei der Generierung von Antworten aus LLMs, unterteilt in 4 Bereiche:

1. Festlegung, für wen das Modell gedacht ist, sowie seiner Fähigkeiten und Grenzen.
2. Definition des Ausgabeformats des Modells.
3. Bereitstellung spezifischer Beispiele, die das beabsichtigte Verhalten des Modells demonstrieren.
4. Bereitstellung zusätzlicher Verhaltensleitplanken.

### Barrierefreiheit

Unabhängig davon, ob ein Nutzer visuelle, auditive, motorische oder kognitive Beeinträchtigungen hat, sollte eine gut gestaltete Chat-Anwendung für alle nutzbar sein. Die folgende Liste zeigt spezifische Funktionen zur Verbesserung der Barrierefreiheit für verschiedene Nutzerbeeinträchtigungen.

- **Funktionen für Sehbeeinträchtigungen**: Hochkontrast-Themen und vergrößerbarer Text, Bildschirmleser-Kompatibilität.
- **Funktionen für Hörbeeinträchtigungen**: Text-zu-Sprache- und Sprache-zu-Text-Funktionen, visuelle Hinweise für Audio-Benachrichtigungen.
- **Funktionen für motorische Beeinträchtigungen**: Unterstützung der Tastaturnavigation, Sprachbefehle.
- **Funktionen für kognitive Beeinträchtigungen**: Vereinfachte Sprachoptionen.

## Anpassung und Feinabstimmung für domänenspezifische Sprachmodelle

Stellen Sie sich eine Chat-Anwendung vor, die die Fachsprache Ihres Unternehmens versteht und die spezifischen Anfragen ihrer Nutzerbasis vorhersieht. Es gibt einige Ansätze, die erwähnenswert sind:

- **Nutzung von DSL-Modellen**. DSL steht für Domain Specific Language (domänenspezifische Sprache). Sie können ein sogenanntes DSL-Modell nutzen, das auf eine bestimmte Domäne trainiert ist, um deren Konzepte und Szenarien zu verstehen.
- **Feinabstimmung anwenden**. Feinabstimmung ist der Prozess, Ihr Modell mit spezifischen Daten weiter zu trainieren.

## Anpassung: Verwendung eines DSL

Die Nutzung von domänenspezifischen Sprachmodellen (DSL-Modelle) kann das Nutzerengagement steigern, indem sie spezialisierte, kontextuell relevante Interaktionen bietet. Es handelt sich um ein Modell, das darauf trainiert oder feinabgestimmt wurde, Texte aus einem bestimmten Fachgebiet, einer Branche oder einem Thema zu verstehen und zu generieren. Optionen zur Verwendung eines DSL-Modells reichen vom Eigenbau über die Nutzung vorliegender Modelle über SDKs und APIs bis hin zur Feinabstimmung, bei der ein bereits vortrainiertes Modell für eine bestimmte Domäne angepasst wird.

## Anpassung: Feinabstimmung anwenden

Feinabstimmung wird häufig in Betracht gezogen, wenn ein vortrainiertes Modell in einem spezialisierten Bereich oder für eine konkrete Aufgabe an seine Grenzen stößt.

Zum Beispiel sind medizinische Anfragen komplex und erfordern viel Kontext. Wenn ein Mediziner einen Patienten diagnostiziert, beruhen die Entscheidungen auf verschiedenen Faktoren wie Lebensstil oder Vorerkrankungen und stützen sich eventuell auf aktuelle medizinische Fachliteratur zur Validierung der Diagnose. In solch nuancierten Fällen kann eine allgemein einsetzbare KI-Chat-Anwendung keine verlässliche Quelle darstellen.

### Szenario: eine medizinische Anwendung

Betrachten Sie eine Chat-Anwendung, die medizinisches Fachpersonal unterstützt, indem sie schnelle Informationen zu Behandlungsleitlinien, Wechselwirkungen von Medikamenten oder aktuellen Forschungsergebnissen bietet.

Ein Allgemeinmodell mag ausreichend sein, um grundlegende medizinische Fragen zu beantworten oder allgemeine Ratschläge zu geben, könnte jedoch Schwierigkeiten haben bei:

- **Sehr spezifischen oder komplexen Fällen**. Zum Beispiel könnte ein Neurologe die Anwendung fragen: „Was sind aktuell die besten Vorgehensweisen zur Behandlung medikamentenresistenter Epilepsie bei pädiatrischen Patienten?“
- **Fehlenden aktuellen Fortschritten**. Ein Allgemeinmodell könnte schwer tun, eine aktuell fundierte Antwort zu liefern, die neueste Fortschritte in Neurologie und Pharmakologie berücksichtigt.

In solchen Fällen kann die Feinabstimmung des Modells mit einem spezialisierten medizinischen Datensatz seine Fähigkeit deutlich verbessern, diese komplexen medizinischen Anfragen präziser und zuverlässiger zu beantworten. Dafür ist der Zugriff auf einen großen und relevanten Datensatz erforderlich, der die domänenspezifischen Herausforderungen und Fragestellungen repräsentiert, die adressiert werden müssen.

## Überlegungen für eine qualitativ hochwertige KI-getriebene Chat-Erfahrung

Dieser Abschnitt beschreibt die Kriterien für „hochwertige“ Chat-Anwendungen, die sowohl die Erfassung aussagekräftiger Metriken als auch die Einhaltung eines Rahmens beinhalten, der KI-Technologie verantwortungsbewusst nutzt.

### Wichtige Metriken

Um die hochwertige Leistung einer Anwendung aufrechtzuerhalten, ist es entscheidend, wichtige Metriken und Überlegungen fortlaufend zu beobachten. Diese Messwerte sichern nicht nur die Funktionalität der Anwendung, sondern bewerten auch die Qualität des KI-Modells und der Nutzererfahrung. Nachfolgend eine Liste mit grundlegenden, KI- und UX-relevanten Metriken zum Berücksichtigen.

| Metrik                       | Definition                                                                                                             | Überlegungen für den Chat-Entwickler                                 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Verfügbarkeit (Uptime)**   | Misst die Zeit, in der die Anwendung für Nutzer erreichbar und betriebsbereit ist.                                     | Wie minimieren Sie Ausfallzeiten?                                    |
| **Antwortzeit**              | Die Zeit, die die Anwendung benötigt, um auf eine Nutzeranfrage zu reagieren.                                          | Wie optimieren Sie die Anfragenverarbeitung, um Antwortzeiten zu verbessern? |
| **Genauigkeit (Precision)**  | Das Verhältnis der korrekt positiven Vorhersagen zur Gesamtzahl der positiven Vorhersagen                              | Wie validieren Sie die Genauigkeit Ihres Modells?                    |
| **Erfassung (Recall / Sensitivität)** | Das Verhältnis der korrekt positiven Vorhersagen zur tatsächlichen Anzahl positiver Fälle                           | Wie messen und verbessern Sie die Erfassung?                        |
| **F1-Score**                | Das harmonische Mittel von Precision und Recall, das den Kompromiss zwischen beiden ausgleicht.                         | Was ist Ihr Ziel-F1-Score? Wie balancieren Sie zwischen Precision und Recall? |
| **Perplexität**             | Misst, wie gut die Wahrscheinlichkeitsverteilung des Modells mit der tatsächlichen Verteilung der Daten übereinstimmt. | Wie minimieren Sie die Perplexität?                                 |
| **Benutzerzufriedenheitsmetriken** | Misst die Wahrnehmung der Anwendung durch den Nutzer. Wird oft durch Umfragen erfasst.                              | Wie oft sammeln Sie Nutzerfeedback? Wie passen Sie sich daran an?   |
| **Fehlerrate**              | Die Rate, mit der das Modell Fehler im Verständnis oder der Ausgabe macht.                                              | Welche Strategien haben Sie zur Reduzierung der Fehlerraten?        |
| **Retrainingszyklen**       | Die Häufigkeit, mit der das Modell aktualisiert wird, um neue Daten und Erkenntnisse einzubeziehen.                     | Wie oft trainieren Sie das Modell neu? Was löst einen Retrainingszyklus aus? |

| **Anomalieerkennung**         | Werkzeuge und Techniken zur Identifizierung ungewöhnlicher Muster, die nicht dem erwarteten Verhalten entsprechen.        | Wie werden Sie auf Anomalien reagieren?                                  |

### Implementierung verantwortungsvoller KI-Praktiken in Chat-Anwendungen

Microsofts Ansatz für verantwortungsvolle KI hat sechs Prinzipien identifiziert, die die KI-Entwicklung und -Nutzung leiten sollten. Nachfolgend sind die Prinzipien, deren Definition und Überlegungen für Chat-Entwickler sowie warum sie diese ernst nehmen sollten.

| Prinzipien             | Microsofts Definition                                | Überlegungen für Chat-Entwickler                                        | Warum es wichtig ist                                                                 |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Fairness               | KI-Systeme sollten alle Menschen fair behandeln.     | Stellen Sie sicher, dass die Chat-Anwendung nicht aufgrund von Nutzerdaten diskriminiert.  | Zum Aufbau von Vertrauen und Inklusivität unter den Nutzern; vermeidet rechtliche Folgen. |
| Zuverlässigkeit und Sicherheit | KI-Systeme sollten zuverlässig und sicher funktionieren.    | Implementieren Sie Tests und Sicherheitsmechanismen zur Minimierung von Fehlern und Risiken.        | Gewährleistet Nutzerzufriedenheit und verhindert potenziellen Schaden. |
| Datenschutz und Sicherheit   | KI-Systeme sollten sicher sein und Datenschutz respektieren.      | Implementieren Sie starke Verschlüsselung und Maßnahmen zum Datenschutz.              | Zum Schutz sensibler Nutzerdaten und zur Einhaltung von Datenschutzgesetzen. |
| Inklusivität          | KI-Systeme sollen alle befähigen und Menschen einbeziehen. | Gestalten Sie UI/UX zugänglich und benutzerfreundlich für diverse Zielgruppen. | Stellt sicher, dass eine breitere Nutzergruppe die Anwendung effektiv nutzen kann. |
| Transparenz           | KI-Systeme sollten verständlich sein.                  | Bieten Sie klare Dokumentation und Begründungen für KI-Antworten.            | Nutzer vertrauen einem System eher, wenn sie nachvollziehen können, wie Entscheidungen getroffen werden. |
| Verantwortlichkeit         | Menschen sollten für KI-Systeme verantwortlich sein.          | Etablieren Sie einen klaren Prozess zur Prüfung und Verbesserung von KI-Entscheidungen.     | Ermöglicht kontinuierliche Verbesserungen und Korrekturmaßnahmen bei Fehlern.              |

## Aufgabe

Siehe [assignment](../../../07-building-chat-applications/python). Es führt Sie durch eine Reihe von Übungen, von den ersten Chat-Aufforderungen über die Klassifizierung und Zusammenfassung von Texten bis hin zu mehr. Beachten Sie, dass die Aufgaben in verschiedenen Programmiersprachen verfügbar sind!

## Großartige Arbeit! Setzen Sie die Reise fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen rund um Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 8, um zu sehen, wie Sie mit dem [Erstellen von Suchanwendungen](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst) starten können!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->