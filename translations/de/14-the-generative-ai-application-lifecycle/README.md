[![Integration mit Function Calling](../../../translated_images/de/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Der Lebenszyklus von Generativen KI-Anwendungen

Eine wichtige Frage für alle KI-Anwendungen ist die Relevanz der KI-Funktionen, da KI ein sich schnell entwickelndes Feld ist. Um sicherzustellen, dass Ihre Anwendung relevant, zuverlässig und robust bleibt, müssen Sie sie kontinuierlich überwachen, bewerten und verbessern. Hier kommt der Lebenszyklus der generativen KI ins Spiel.

Der Lebenszyklus der generativen KI ist ein Rahmenwerk, das Sie durch die Phasen der Entwicklung, Bereitstellung und Wartung einer generativen KI-Anwendung führt. Es hilft Ihnen, Ihre Ziele zu definieren, Ihre Leistung zu messen, Ihre Herausforderungen zu identifizieren und Ihre Lösungen umzusetzen. Es hilft Ihnen auch, Ihre Anwendung mit den ethischen und rechtlichen Standards Ihres Fachgebiets und Ihrer Interessengruppen in Einklang zu bringen. Indem Sie dem Lebenszyklus der generativen KI folgen, können Sie sicherstellen, dass Ihre Anwendung stets Mehrwert liefert und Ihre Nutzer zufriedengestellt sind.

## Einführung

In diesem Kapitel werden Sie:

- Den Paradigmenwechsel von MLOps zu LLMOps verstehen
- Den LLM-Lebenszyklus kennenlernen
- Lifecycle-Tools
- Lifecycle-Metrifizierung und Bewertung

## Den Paradigmenwechsel von MLOps zu LLMOps verstehen

LLMs sind ein neues Werkzeug im Arsenal der Künstlichen Intelligenz, sie sind unglaublich mächtig bei Analyse- und Generierungsaufgaben für Anwendungen, jedoch hat diese Macht auch Konsequenzen dafür, wie wir KI- und klassische Machine-Learning-Aufgaben straffen.

Dafür benötigen wir ein neues Paradigma, um dieses Werkzeug dynamisch mit den richtigen Anreizen anzupassen. Ältere KI-Anwendungen können wir als „ML-Apps“ und neuere KI-Anwendungen als „GenAI-Apps“ oder einfach „KI-Apps“ kategorisieren, was die damals verwendeten Technologietrends und Techniken widerspiegelt. Dies verschiebt unsere Erzählweise auf mehrere Weisen, siehe den folgenden Vergleich.

![LLMOps vs. MLOps Vergleich](../../../translated_images/de/01-llmops-shift.29bc933cb3bb0080.webp)

Beachten Sie, dass wir bei LLMOps stärker auf die Anwendungsentwickler fokussieren, Integrationen als Schlüsselpunkt nutzen, „Models-as-a-Service“ verwenden und bei den Metriken folgende Punkte betrachten.

- Qualität: Antwortqualität
- Schaden: Verantwortungsvolle KI
- Ehrlichkeit: Antwortgrundlage (Ergibt das Sinn? Ist es korrekt?)
- Kosten: Lösungsbudget
- Latenz: Durchschnittliche Antwortzeit pro Token

## Der LLM-Lebenszyklus

Zuerst, um den Lebenszyklus und die Änderungen zu verstehen, beachten wir die folgende Infografik.

![LLMOps Infografik](../../../translated_images/de/02-llmops.70a942ead05a7645.webp)

Wie Sie sehen werden, unterscheidet sich dies von den üblichen Lebenszyklen bei MLOps. LLMs haben viele neue Anforderungen, wie Prompting, verschiedene Techniken zur Qualitätsverbesserung (Fine-Tuning, RAG, Meta-Prompts), unterschiedliche Bewertungen und Verantwortlichkeiten mit Responsible AI sowie neue Bewertungsmetriken (Qualität, Schaden, Ehrlichkeit, Kosten und Latenz).

Zum Beispiel sehen Sie, wie wir Ideen entwickeln. Mithilfe von Prompt Engineering experimentieren wir mit verschiedenen LLMs, um Möglichkeiten zu erkunden und zu prüfen, ob ihre Hypothesen korrekt sein könnten.

Beachten Sie, dass dies nicht linear, sondern integrierte Schleifen sind, iterativ und mit einem übergreifenden Zyklus.

Wie könnten wir diese Schritte erkunden? Lassen Sie uns im Detail betrachten, wie wir einen Lebenszyklus aufbauen können.

![LLMOps Workflow](../../../translated_images/de/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Dies mag etwas kompliziert erscheinen, konzentrieren wir uns zuerst auf die drei großen Schritte.

1. Ideenfindung/Erkundung: Hier können wir entsprechend unserer Geschäftsbedürfnisse explorieren. Prototyping, Erstellung eines [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) und testen, ob es für unsere Hypothese effizient genug ist.
1. Aufbau/Erweiterung: Implementierung, jetzt beginnen wir, größere Datensätze zu evaluieren, Techniken wie Fine-Tuning und RAG anzuwenden, um die Robustheit unserer Lösung zu prüfen. Falls nicht, kann eine Neuimplementierung, das Hinzufügen von neuen Schritten im Ablauf oder die Umstrukturierung der Daten helfen. Nach dem Testen unseres Ablaufs und unseres Umfangs, wenn alles funktioniert und die Metriken stimmen, ist es bereit für den nächsten Schritt.
1. Operationalisierung: Integration, nun fügen wir Überwachungs- und Alarmierungssysteme zu unserem System hinzu, Deployment und Anwendungsintegration in unsere Applikation.

Dann gibt es den übergreifenden Management-Zyklus, der sich auf Sicherheit, Compliance und Governance konzentriert.

Glückwunsch, Ihre KI-Anwendung ist jetzt einsatzbereit und betriebsfähig. Für eine praktische Erfahrung schauen Sie sich die [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) an.

Welche Werkzeuge können wir nun verwenden?

## Lifecycle-Tools

Für Werkzeuge bietet Microsoft die [Azure AI Plattform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) und [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), die Ihren Zyklus erleichtern und einfach implementierbar machen.

Die [Azure AI Plattform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) ermöglicht Ihnen die Nutzung von [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (früher Azure AI Studio) ist ein Webportal, mit dem Sie Modelle, Beispiele und Werkzeuge erkunden, Ihre Ressourcen verwalten und UI-Entwicklungsabläufe sowie SDK-/CLI-Optionen für die Code-zuerst-Entwicklung nutzen können.

![Möglichkeiten von Azure AI](../../../translated_images/de/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI ermöglicht Ihnen die Nutzung zahlreicher Ressourcen, um Ihre Betriebsabläufe, Dienste, Projekte, Vektorensuchen und Datenbankanforderungen zu verwalten.

![LLMOps mit Azure AI](../../../translated_images/de/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Konstruieren Sie von Proof-of-Concept (POC) bis hin zu groß angelegten Anwendungen mit PromptFlow:

- Entwickeln und Erstellen von Apps direkt in VS Code, mit visuellen und funktionalen Werkzeugen
- Testen und Feinjustieren Ihrer Apps für qualitativ hochwertige KI, mit Leichtigkeit.
- Nutzen Sie Microsoft Foundry, um Cloud-Integration, Push und Deployment für schnelle Integration umzusetzen und iterativ zu arbeiten.

![LLMOps mit PromptFlow](../../../translated_images/de/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Großartig! Fahren Sie mit Ihrem Lernen fort!

Fantastisch, lernen Sie jetzt mehr darüber, wie wir eine Anwendung strukturieren, um die Konzepte mit der [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) anzuwenden, und sehen Sie, wie Cloud Advocacy diese Konzepte in Demonstrationen einbezieht. Für mehr Inhalte schauen Sie sich unsere [Ignite-Breakout-Session](https://www.youtube.com/watch?v=DdOylyrTOWg) an!


Schauen Sie nun in Lektion 15, um zu verstehen, wie [Retrieval Augmented Generation und Vektordatenbanken](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) die Generative KI beeinflussen und wie Sie ansprechendere Anwendungen erstellen können!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->