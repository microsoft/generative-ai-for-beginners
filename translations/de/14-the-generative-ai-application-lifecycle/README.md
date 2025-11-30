<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T22:58:04+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "de"
}
-->
[![Integration mit Funktionsaufrufen](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.de.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Der Lebenszyklus von generativen KI-Anwendungen

Eine wichtige Frage für alle KI-Anwendungen ist die Relevanz der KI-Funktionen, da sich das Feld der KI schnell weiterentwickelt. Um sicherzustellen, dass Ihre Anwendung relevant, zuverlässig und robust bleibt, müssen Sie sie kontinuierlich überwachen, bewerten und verbessern. Hier kommt der Lebenszyklus von generativer KI ins Spiel.

Der Lebenszyklus von generativer KI ist ein Rahmenwerk, das Sie durch die Phasen der Entwicklung, Bereitstellung und Wartung einer generativen KI-Anwendung führt. Es hilft Ihnen, Ihre Ziele zu definieren, Ihre Leistung zu messen, Herausforderungen zu identifizieren und Lösungen umzusetzen. Außerdem unterstützt es Sie dabei, Ihre Anwendung mit den ethischen und rechtlichen Standards Ihres Fachgebiets und Ihrer Interessengruppen in Einklang zu bringen. Indem Sie dem Lebenszyklus von generativer KI folgen, können Sie sicherstellen, dass Ihre Anwendung stets Mehrwert bietet und Ihre Nutzer zufriedenstellt.

## Einführung

In diesem Kapitel werden Sie:

- Den Paradigmenwechsel von MLOps zu LLMOps verstehen
- Den Lebenszyklus von LLMs kennenlernen
- Tools für den Lebenszyklus entdecken
- Metrifizierung und Bewertung des Lebenszyklus verstehen

## Den Paradigmenwechsel von MLOps zu LLMOps verstehen

LLMs sind ein neues Werkzeug im Arsenal der Künstlichen Intelligenz. Sie sind unglaublich leistungsfähig bei Analyse- und Generierungsaufgaben für Anwendungen. Diese Stärke hat jedoch Konsequenzen für die Art und Weise, wie wir KI- und klassische maschinelle Lernaufgaben optimieren.

Daher benötigen wir ein neues Paradigma, um dieses Werkzeug dynamisch und mit den richtigen Anreizen anzupassen. Wir können ältere KI-Anwendungen als "ML-Apps" und neuere KI-Anwendungen als "GenAI-Apps" oder einfach "KI-Apps" kategorisieren, was die zu der Zeit vorherrschende Technologie und Techniken widerspiegelt. Dies verändert unsere Herangehensweise in vielerlei Hinsicht. Sehen Sie sich den folgenden Vergleich an.

![Vergleich LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.de.png)

Beachten Sie, dass wir uns bei LLMOps stärker auf die App-Entwickler konzentrieren, Integrationen als Schlüsselpunkt nutzen, "Models-as-a-Service" verwenden und die folgenden Punkte für Metriken berücksichtigen:

- Qualität: Antwortqualität
- Schaden: Verantwortungsvolle KI
- Ehrlichkeit: Fundiertheit der Antwort (Ergibt sie Sinn? Ist sie korrekt?)
- Kosten: Budget der Lösung
- Latenz: Durchschnittliche Zeit für Token-Antworten

## Der Lebenszyklus von LLMs

Um den Lebenszyklus und die Änderungen zu verstehen, werfen wir einen Blick auf die folgende Infografik.

![LLMOps Infografik](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.de.png)

Wie Sie sehen können, unterscheidet sich dies von den üblichen Lebenszyklen in MLOps. LLMs haben viele neue Anforderungen, wie Prompting, verschiedene Techniken zur Qualitätsverbesserung (Fine-Tuning, RAG, Meta-Prompts), unterschiedliche Bewertungen und Verantwortlichkeiten im Rahmen von verantwortungsvoller KI sowie neue Bewertungsmetriken (Qualität, Schaden, Ehrlichkeit, Kosten und Latenz).

Betrachten Sie beispielsweise, wie wir Ideen entwickeln. Mithilfe von Prompt Engineering können wir mit verschiedenen LLMs experimentieren, um Möglichkeiten zu erkunden und zu testen, ob ihre Hypothesen korrekt sein könnten.

Beachten Sie, dass dies kein linearer Prozess ist, sondern integrierte Schleifen, iterativ und mit einem übergeordneten Zyklus.

Wie können wir diese Schritte erkunden? Lassen Sie uns im Detail darauf eingehen, wie wir einen Lebenszyklus aufbauen können.

![LLMOps Arbeitsablauf](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.de.png)

Das mag zunächst etwas kompliziert erscheinen, konzentrieren wir uns daher auf die drei großen Schritte:

1. Ideenfindung/Erkundung: Exploration. Hier können wir basierend auf unseren geschäftlichen Anforderungen experimentieren. Prototyping, Erstellen eines [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) und Testen, ob es effizient genug für unsere Hypothese ist.
2. Aufbau/Erweiterung: Implementierung. Jetzt beginnen wir mit der Bewertung größerer Datensätze, implementieren Techniken wie Fine-Tuning und RAG, um die Robustheit unserer Lösung zu überprüfen. Falls dies nicht ausreicht, kann eine erneute Implementierung, das Hinzufügen neuer Schritte in unserem Ablauf oder die Umstrukturierung der Daten helfen. Nach dem Testen unseres Ablaufs und unserer Skalierung, wenn alles funktioniert und unsere Metriken erfüllt sind, ist es bereit für den nächsten Schritt.
3. Operationalisierung: Integration. Jetzt fügen wir Überwachungs- und Alarmsysteme zu unserem System hinzu, führen die Bereitstellung durch und integrieren die Anwendung in unser System.

Dann gibt es den übergeordneten Zyklus des Managements, der sich auf Sicherheit, Compliance und Governance konzentriert.

Herzlichen Glückwunsch, jetzt ist Ihre KI-Anwendung einsatzbereit und betriebsfähig. Für praktische Erfahrungen werfen Sie einen Blick auf die [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Welche Tools können wir verwenden?

## Tools für den Lebenszyklus

Für die Tools stellt Microsoft die [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) und [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) bereit, um Ihren Lebenszyklus einfach umzusetzen und einsatzbereit zu machen.

Die [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) ermöglicht Ihnen die Nutzung von [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio ist ein Webportal, das Ihnen erlaubt, Modelle, Beispiele und Tools zu erkunden, Ihre Ressourcen zu verwalten, UI-Entwicklungsabläufe zu erstellen und SDK/CLI-Optionen für Code-First-Entwicklung zu nutzen.

![Azure AI Möglichkeiten](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.de.png)

Azure AI ermöglicht Ihnen die Nutzung verschiedener Ressourcen, um Ihre Operationen, Dienste, Projekte, Vektorsuche und Datenbankanforderungen zu verwalten.

![LLMOps mit Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.de.png)

Erstellen Sie Anwendungen vom Proof-of-Concept (POC) bis hin zu groß angelegten Anwendungen mit PromptFlow:

- Entwerfen und Erstellen von Apps in VS Code mit visuellen und funktionalen Tools
- Testen und Feinabstimmen Ihrer Apps für qualitativ hochwertige KI, ganz einfach.
- Verwenden Sie Azure AI Studio, um mit der Cloud zu integrieren und zu iterieren, Push und Deployment für eine schnelle Integration.

![LLMOps mit PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.de.png)

## Großartig! Lernen Sie weiter!

Fantastisch! Lernen Sie jetzt mehr darüber, wie wir eine Anwendung strukturieren, um die Konzepte mit der [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) zu nutzen und zu sehen, wie Cloud Advocacy diese Konzepte in Demonstrationen einsetzt. Für weitere Inhalte schauen Sie sich unsere [Ignite Breakout Session](https://www.youtube.com/watch?v=DdOylyrTOWg) an!

Sehen Sie sich nun Lektion 15 an, um zu verstehen, wie [Retrieval Augmented Generation und Vektordatenbanken](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) die generative KI beeinflussen und ansprechende Anwendungen ermöglichen!

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.