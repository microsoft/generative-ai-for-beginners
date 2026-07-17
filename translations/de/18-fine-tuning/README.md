[![Open Source Modelle](../../../translated_images/de/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Feinabstimmung Ihres LLM

Die Nutzung großer Sprachmodelle zum Aufbau generativer KI-Anwendungen bringt neue Herausforderungen mit sich. Ein zentrales Problem ist die Sicherstellung der Antwortqualität (Genauigkeit und Relevanz) in den vom Modell erzeugten Inhalten für eine gegebene Benutzeranfrage. In früheren Lektionen haben wir Techniken wie Prompt-Engineering und retrieval-unterstützte Generierung besprochen, die versuchen, das Problem durch _Ändern der Eingabeaufforderung_ für das vorhandene Modell zu lösen.

In der heutigen Lektion sprechen wir über eine dritte Technik, das **Feinabstimmen**, die das Problem durch _das erneute Training des Modells selbst_ mit zusätzlichen Daten angeht. Tauchen wir in die Details ein.

## Lernziele

Diese Lektion stellt das Konzept der Feinabstimmung für vortrainierte Sprachmodelle vor, untersucht die Vorteile und Herausforderungen dieses Ansatzes und bietet Anleitungen dazu, wann und wie Feinabstimmung eingesetzt werden kann, um die Leistung Ihrer generativen KI-Modelle zu verbessern.

Am Ende dieser Lektion sollten Sie folgende Fragen beantworten können:

- Was ist Feinabstimmung für Sprachmodelle?
- Wann und warum ist Feinabstimmung nützlich?
- Wie kann ich ein vortrainiertes Modell feinabstimmen?
- Was sind die Einschränkungen der Feinabstimmung?

Bereit? Dann legen wir los.

## Illustrierter Leitfaden

Möchten Sie einen Überblick darüber erhalten, was wir behandeln, bevor wir tiefer einsteigen? Schauen Sie sich diesen illustrierten Leitfaden an, der die Lernreise für diese Lektion beschreibt – von den Kernkonzepten und der Motivation für Feinabstimmung bis hin zum Verständnis des Prozesses und der besten Praktiken für die Durchführung der Feinabstimmungsaufgabe. Dies ist ein faszinierendes Thema, also vergessen Sie nicht, die [Ressourcen](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite für zusätzliche Links zu Ihrer selbstgesteuerten Lernreise zu besuchen!

![Illustrierter Leitfaden zur Feinabstimmung von Sprachmodellen](../../../translated_images/de/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Was ist Feinabstimmung für Sprachmodelle?

Laut Definition sind große Sprachmodelle _vortrainiert_ auf großen Textmengen aus vielfältigen Quellen, darunter das Internet. Wie wir in früheren Lektionen gelernt haben, benötigen wir Techniken wie _Prompt-Engineering_ und _retrieval-unterstützte Generierung_, um die Qualität der Antworten des Modells auf Benutzerfragen („Prompts“) zu verbessern.

Eine beliebte Prompt-Engineering-Technik besteht darin, dem Modell mehr Anleitung zu geben, was in der Antwort erwartet wird, entweder durch _Anweisungen_ (explizite Anleitung) oder _indem man ihm einige Beispiele gibt_ (implizite Anleitung). Dies wird als _Few-Shot-Lernen_ bezeichnet, hat jedoch zwei Einschränkungen:

- Modell-Token-Limits können die Anzahl der Beispiele begrenzen, die Sie geben können, und somit die Effektivität einschränken.
- Die Kosten pro Token können es teuer machen, bei jeder Aufforderung Beispiele hinzuzufügen, und schränken die Flexibilität ein.

Feinabstimmung ist eine gängige Praxis in maschinellen Lernsystemen, bei der wir ein vortrainiertes Modell nehmen und es mit neuen Daten erneut trainieren, um seine Leistung bei einer bestimmten Aufgabe zu verbessern. Im Kontext von Sprachmodellen können wir das vortrainierte Modell _mit einer kuratierten Beispielsammlung für eine bestimmte Aufgabe oder Domäne_ feinabstimmen, um ein **kundenspezifisches Modell** zu erstellen, das für diese spezifische Aufgabe oder Domäne genauer und relevanter sein kann. Ein Nebeneffekt der Feinabstimmung ist, dass die Anzahl der für Few-Shot-Lernen benötigten Beispiele reduziert werden kann – was Token-Verbrauch und damit verbundene Kosten senkt.

## Wann und warum sollten wir Modelle feinabstimmen?

In _diesem_ Zusammenhang bezieht sich Feinabstimmung auf **überwachtes** Feinabstimmen, bei dem das erneute Training durch **Hinzufügen neuer Daten** erfolgt, die nicht im ursprünglichen Trainingsdatensatz enthalten waren. Dies unterscheidet sich von einem unüberwachten Feinabstimmungsansatz, bei dem das Modell mit den Originaldaten, jedoch mit geänderten Hyperparametern erneut trainiert wird.

Wichtig ist, sich daran zu erinnern, dass Feinabstimmung eine fortgeschrittene Technik ist, die ein gewisses Maß an Fachkenntnis erfordert, um die gewünschten Ergebnisse zu erzielen. Wird sie falsch durchgeführt, kann sie die erwarteten Verbesserungen ausbleiben lassen oder sogar die Leistung des Modells für Ihre Ziel-Domäne verschlechtern.

Bevor Sie also lernen, _wie_ man Sprachmodelle feinabstimmt, müssen Sie wissen, _warum_ Sie diesen Weg gehen sollten und _wann_ Sie den Prozess der Feinabstimmung starten sollten. Fragen Sie sich dazu:

- **Anwendungsfall**: Was ist Ihr _Anwendungsfall_ für die Feinabstimmung? Welchen Aspekt des aktuellen vortrainierten Modells möchten Sie verbessern?
- **Alternativen**: Haben Sie _andere Techniken_ ausprobiert, um die gewünschten Ergebnisse zu erzielen? Nutzen Sie diese als Vergleichsgrundlage.
  - Prompt-Engineering: Versuchen Sie Techniken wie Few-Shot-Prompting mit Beispielen relevanter Antwortaufforderungen. Bewerten Sie die Qualität der Antworten.
  - Retrieval-unterstützte Generierung: Versuchen Sie, Prompts mit Suchergebnissen aus Ihren Daten zu ergänzen. Bewerten Sie die Qualität der Antworten.
- **Kosten**: Haben Sie die Kosten für die Feinabstimmung identifiziert?
  - Anpassbarkeit – Ist das vortrainierte Modell für Feinabstimmung verfügbar?
  - Aufwand – für die Vorbereitung von Trainingsdaten, Evaluierung und Verfeinerung des Modells.
  - Rechenleistung – für das Ausführen der Feinabstimmungsaufgaben und Bereitstellung des feinabgestimmten Modells.
  - Daten – Zugang zu qualitativ ausreichenden Beispielen für den Effekt der Feinabstimmung.
- **Vorteile**: Haben Sie die Vorteile der Feinabstimmung bestätigt?
  - Qualität – Hat das feinabgestimmte Modell die Ausgangsbasis übertroffen?
  - Kosten – Reduziert es durch Vereinfachung der Prompts den Token-Verbrauch?
  - Erweiterbarkeit – Können Sie das Basismodell für neue Domänen wiederverwenden?

Durch die Beantwortung dieser Fragen sollten Sie entscheiden können, ob Feinabstimmung der richtige Ansatz für Ihren Anwendungsfall ist. Idealerweise ist der Ansatz nur dann gültig, wenn der Nutzen die Kosten überwiegt. Wenn Sie sich zum Fortfahren entscheiden, ist es Zeit, darüber nachzudenken, _wie_ Sie das vortrainierte Modell feinabstimmen können.

Möchten Sie mehr Einblicke in den Entscheidungsprozess erhalten? Sehen Sie sich [Feinabstimmen oder nicht feinabstimmen](https://www.youtube.com/watch?v=0Jo-z-MFxJs) an.

## Wie können wir ein vortrainiertes Modell feinabstimmen?

Um ein vortrainiertes Modell feinabstimmen zu können, benötigen Sie:

- Ein vortrainiertes Modell zum Feinabstimmen
- Einen Datensatz zum Feinabstimmen
- Eine Trainingsumgebung, um den Feinabstimmungsjob auszuführen
- Eine Hosting-Umgebung, um das feinabgestimmte Modell bereitzustellen

## Feinabstimmung mit Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ist der Ort, an dem Sie heute benutzerdefinierte Modelle auf Azure feinabstimmen, bereitstellen und verwalten (es vereint, was früher Azure OpenAI Studio und Azure AI Studio waren). Bevor Sie einen Job starten, ist es hilfreich, die Auswahlmöglichkeiten von Foundry und die empfohlenen Best Practices der Plattform zu verstehen. Im Kern verwendet Foundry **LoRA (Low-Rank Adaptation)**, um Modelle effizient feinabzustimmen, was das Training gegenüber dem kompletten Neuerlernen aller Gewichte schneller und kostengünstiger hält.

### Schritt 1: Wählen Sie eine Trainingstechnik

Foundry unterstützt drei Feinabstimmungstechniken. **Beginnen Sie mit SFT** – es deckt den breitesten Bereich von Szenarien ab.

| Technik | Was sie macht | Wann man sie verwendet |
| --- | --- | --- |
| **Überwachte Feinabstimmung (SFT)** | Trainiert mit Eingabe/Ausgabe-Beispielpaaren, sodass das Modell lernt, die gewünschten Antworten zu erzeugen. | Die Standardmethode für die meisten Aufgaben: Domänenspezialisierung, Aufgabenleistung, Stil und Ton, Befolgen von Anweisungen und Sprachadaption. |
| **Direkte Präferenzoptimierung (DPO)** | Lernt aus _bevorzugten vs. nicht-bevorzugten_ Antwortpaaren, um Ausgaben mit menschlichen Präferenzen abzugleichen. | Verbesserung der Antwortqualität, Sicherheit und Ausrichtung bei vergleichendem Feedback. |
| **Verstärkungs-Feinabstimmung (RFT)** | Nutzt Belohnungssignale von _Bewertenden_, um komplexe Verhaltensweisen mit Verstärkungslernen zu optimieren. | Objektive, stark argumentationslastige Domänen (Mathematik, Chemie, Physik) mit klaren richtigen/falschen Antworten. Erfordert mehr ML-Expertise. |

### Schritt 2: Wählen Sie einen Trainingsrang

Foundry lässt Sie wählen, wie und wo das Training ausgeführt wird:

- **Standard** – trainiert in der Region Ihrer Ressource und garantiert Datenresidenz. Verwenden Sie dies, wenn Daten in einer bestimmten Region verbleiben müssen.
- **Global** – günstiger und schneller in der Warteschlange, indem Kapazität außerhalb Ihrer Region genutzt wird (Daten und Gewichte werden in die Trainingsregion kopiert). Eine gute Standardeinstellung, wenn keine Datenresidenzpflicht besteht.
- **Entwickler** – die günstigste Option, verwendet Leerlaufkapazität ohne Latenz-/SLA-Garantien (Jobs können unterbrochen und fortgesetzt werden). Ideal für Experimente.

### Schritt 3: Wählen Sie ein Basismodell

Feinabstimmbare Modelle umfassen OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` und `gpt-4.1-nano` (SFT; die 4o/4.1-Familie unterstützt auch DPO), die Reasoning-Modelle `o4-mini` und `gpt-5` (RFT), sowie Open-Source-Modelle wie `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` und `gpt-oss-20b` (SFT auf Foundry-Ressourcen). Prüfen Sie stets die aktuelle [Liste der Feinabstimmungsmodelle](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst) hinsichtlich unterstützter Methoden, Regionen und Verfügbarkeit.

> Foundry bietet zwei Modalitäten: **Serverless** (verbrauchsabhängige Abrechnung, keine Verwaltung von GPU-Kontingenten, OpenAI- und ausgewählte Modelle) und **Managed Compute** (Bring-Your-Own-VMs über Azure Machine Learning für die breiteste Modellpalette). Die meisten sollten mit serverlos beginnen.

### Foundry Best Practices

- **Erst Basislinie.** Messen Sie das Basismodell mit Prompt-Engineering und RAG _bevor_ Sie feinabstimmen, um den Gewinn zu belegen.
- **Klein anfangen, dann skalieren.** Starten Sie mit 50-100 hochwertigen Beispielen zur Validierung des Ansatzes, wachsen Sie dann auf 500+ für die Produktion. Qualität vor Quantität – entfernen Sie Beispiele von schlechter Qualität.
- **Daten korrekt formatieren.** Trainings- und Validierungsdateien müssen JSONL, UTF-8 **mit BOM**, unter 512 MB, im Nachrichtenformat für Chat-Vervollständigungen sein. Einschließlich Validierungsdatei zur Überwachung von Overfitting ist immer erforderlich.
- **System-Prompt während der Inferenz beibehalten.** Verwenden Sie dieselbe Systemnachricht beim Modellaufruf wie beim Training.
- **Evaluieren Sie Checkpoints – setzen Sie nicht blind den letzten ein.** Foundry behält die letzten drei Epochen als bereitstellbare Checkpoints; wählen Sie denjenigen, der am besten generalisiert, indem Sie `train_loss` / `valid_loss` und Token-Genauigkeit beobachten.
- **Messen Sie Token-Kosten neben der Qualität** beim Vergleich des feinabgestimmten Modells mit der Basislinie.
- **Iterieren Sie mit kontinuierlicher Feinabstimmung.** Sie können ein bereits feinabgestimmtes Modell auf neuen Daten weiter feinabstimmen (unterstützt für OpenAI-Modelle).
- **DenkEN Sie an Hosting-Kosten.** Ein bereitgestelltes kundenspezifisches Modell wird stündlich abgerechnet; eine inaktive Bereitstellung wird nach 15 Tagen entfernt – bereinigen Sie, was Sie nicht benötigen.

Durcharbeiten Sie die durchgehende Anleitung in [Modell mit Feinabstimmung anpassen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) und sehen Sie sich die Anleitungen für [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) und [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) an, wenn Sie für die anderen Techniken bereit sind.

## Feinabstimmung in der Praxis

Die folgenden Ressourcen bieten Schritt-für-Schritt-Tutorials, die Sie durch ein echtes Beispiel mit einem aktuell unterstützten Modell und einem kuratierten Datensatz führen. Für die Arbeit damit benötigen Sie einen Account beim jeweiligen Anbieter sowie Zugriff auf das relevante Modell und die Datensätze.

| Anbieter     | Tutorial                                                                                                                                                                       | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Wie man Chat-Modelle feinabstimmt](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lernen Sie, wie Sie ein aktuelles OpenAI-Chatmodell für eine spezifische Domäne („Rezept-Assistent“) feinabstimmen, indem Sie Trainingsdaten vorbereiten, den Feinabstimmungsjob ausführen und das feinabgestimmte Modell für Inferenz nutzen.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Modell mit Feinabstimmung anpassen](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Lernen Sie, wie Sie ein aktuell unterstütztes Modell wie `gpt-4.1-mini` **auf Azure** mit Microsoft Foundry feinabstimmen: Vorbereiten & Hochladen von Trainings- und Validierungsdaten, Ausführen des Feinabstimmungsjobs, dann Bereitstellen & Nutzen des neuen Modells.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Fine-Tuning von LLMs mit Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dieser Blogbeitrag führt dich durch das Fine-Tuning eines _offenen LLM_ (z.B.: `CodeLlama 7B`) mit der [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) Bibliothek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) unter Verwendung offener [Datensätze](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) auf Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-Tuning von LLMs mit AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (oder AutoTrain Advanced) ist eine von Hugging Face entwickelte Python-Bibliothek, die Fine-Tuning für viele verschiedene Aufgaben ermöglicht, einschließlich LLM-Fine-Tuning. AutoTrain ist eine No-Code-Lösung und das Fine-Tuning kann in der eigenen Cloud, auf Hugging Face Spaces oder lokal durchgeführt werden. Es unterstützt sowohl eine webbasiertes GUI, CLI und Training über YAML-Konfigurationsdateien.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-Tuning von LLMs mit Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth ist ein Open-Source-Framework, das LLM Fine-Tuning und Reinforcement Learning (RL) unterstützt. Unsloth erleichtert lokales Training, Evaluation und Deployment mit gebrauchsfertigen [Notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Es unterstützt zudem Text-to-Speech (TTS), BERT und multimodale Modelle. Um zu starten, lese ihren Schritt-für-Schritt [Fine-Tuning LLMs Leitfaden](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Aufgabe

Wähle eine der obigen Anleitungen aus und arbeite sie durch. _Wir könnten eine Version dieser Tutorials in Jupyter Notebooks in diesem Repo nur zu Referenzzwecken replizieren. Bitte nutze die Originalquellen direkt, um die neuesten Versionen zu erhalten_.

## Großartige Arbeit! Setze dein Lernen fort.

Nach Abschluss dieser Lektion sieh dir unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen zu Generativer KI weiter zu vertiefen!

Herzlichen Glückwunsch!! Du hast die letzte Lektion der v2-Serie für diesen Kurs abgeschlossen! Höre nicht auf zu lernen und zu entwickeln. \*\*Sieh dir die [RESSOURCEN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite für eine Liste weiterer Vorschläge speziell zu diesem Thema an.

Unsere v1-Serie von Lektionen wurde ebenfalls mit weiteren Aufgaben und Konzepten aktualisiert. Nimm dir also eine Minute, um dein Wissen aufzufrischen – und bitte [teile deine Fragen und dein Feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), um uns zu helfen, diese Lektionen für die Community zu verbessern.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->