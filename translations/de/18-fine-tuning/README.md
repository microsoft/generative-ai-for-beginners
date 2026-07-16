[![Open Source Modelle](../../../translated_images/de/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Feinabstimmung Ihres LLM

Die Verwendung großer Sprachmodelle zum Erstellen generativer KI-Anwendungen bringt neue Herausforderungen mit sich. Ein zentrales Problem ist die Sicherstellung der Antwortqualität (Genauigkeit und Relevanz) im vom Modell für eine Benutzeranfrage generierten Inhalt. In vorherigen Lektionen haben wir Techniken wie Prompt Engineering und Retrieval-Augmented Generation besprochen, die versuchen, das Problem durch _Modifikation der Eingabeaufforderung_ im bestehenden Modell zu lösen.

In der heutigen Lektion besprechen wir eine dritte Technik, die **Feinabstimmung**, die versucht, die Herausforderung durch _Weitertrainieren des Modells selbst_ mit zusätzlichen Daten zu lösen. Lassen Sie uns ins Detail gehen.

## Lernziele

Diese Lektion führt in das Konzept der Feinabstimmung für vortrainierte Sprachmodelle ein, erkundet die Vorteile und Herausforderungen dieses Ansatzes und gibt Hinweise, wann und wie Sie die Feinabstimmung nutzen können, um die Leistung Ihrer generativen KI-Modelle zu verbessern.

Am Ende dieser Lektion sollten Sie folgende Fragen beantworten können:

- Was ist Feinabstimmung bei Sprachmodellen?
- Wann und warum ist Feinabstimmung nützlich?
- Wie kann ich ein vortrainiertes Modell feinabstimmen?
- Was sind die Einschränkungen der Feinabstimmung?

Bereit? Legen wir los.

## Illustrierter Leitfaden

Möchten Sie einen Überblick über die Themen erhalten, bevor wir ins Detail gehen? Sehen Sie sich diesen illustrierten Leitfaden an, der die Lernreise für diese Lektion beschreibt – von den Kernkonzepten und der Motivation für die Feinabstimmung bis hin zum Verständnis des Prozesses und der besten Praktiken für die Durchführung der Feinabstimmung. Dies ist ein faszinierendes Thema zur Erkundung, also vergessen Sie nicht, die [Ressourcen](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite für zusätzliche Links zur Unterstützung Ihrer selbstgesteuerten Lernreise zu besuchen!

![Illustrierter Leitfaden zur Feinabstimmung von Sprachmodellen](../../../translated_images/de/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Was ist Feinabstimmung bei Sprachmodellen?

Per Definition sind große Sprachmodelle _vortrainiert_ auf großen Textmengen, die aus verschiedenen Quellen, einschließlich des Internets, stammen. Wie wir in früheren Lektionen gelernt haben, benötigen wir Techniken wie _Prompt Engineering_ und _Retrieval-Augmented Generation_, um die Qualität der Antworten des Modells auf die Benutzerfragen („Prompts“) zu verbessern.

Eine beliebte Prompt-Engineering-Methode besteht darin, dem Modell mehr Anleitung zu geben, was in der Antwort erwartet wird, entweder durch die Bereitstellung von _Anweisungen_ (explizite Anleitung) oder durch _Einige Beispiele_ (implizite Anleitung). Dies wird als _Few-Shot-Lernen_ bezeichnet, hat aber zwei Einschränkungen:

- Modell-Token-Limits können die Anzahl der Beispiele einschränken, die Sie geben können, und die Effektivität begrenzen.
- Modell-Token-Kosten können es teuer machen, Beispiele zu jeder Eingabeaufforderung hinzuzufügen, und die Flexibilität einschränken.

Feinabstimmung ist eine gängige Praxis in maschinellen Lernsystemen, bei der wir ein vortrainiertes Modell nehmen und es mit neuen Daten weitertrainieren, um die Leistung bei einer bestimmten Aufgabe zu verbessern. Im Kontext von Sprachmodellen können wir das vortrainierte Modell _mit einem kuratierten Satz von Beispielen für eine bestimmte Aufgabe oder Anwendungsdomäne_ feinabstimmen, um ein **kundenspezifisches Modell** zu erstellen, das für diese spezifische Aufgabe oder Domäne möglicherweise genauer und relevanter ist. Ein Neben-Nutzen der Feinabstimmung ist, dass sie auch die Anzahl der benötigten Beispiele für das Few-Shot-Lernen reduzieren kann – was den Tokenverbrauch und die damit verbundenen Kosten senkt.

## Wann und warum sollten wir Modelle feinabstimmen?

In _diesem_ Kontext, wenn wir von Feinabstimmung sprechen, beziehen wir uns auf die **überwachte** Feinabstimmung, bei der das Weitertrainieren durch **Hinzufügen neuer Daten** erfolgt, die nicht Teil des ursprünglichen Trainingsdatensatzes waren. Dies unterscheidet sich von einem unüberwachten Feinabstimmungsansatz, bei dem das Modell auf den Originaldaten mit anderen Hyperparametern weitertrainiert wird.

Wichtig ist zu bedenken, dass Feinabstimmung eine fortgeschrittene Technik ist, die ein gewisses Maß an Fachwissen erfordert, um die gewünschten Ergebnisse zu erzielen. Wenn sie falsch durchgeführt wird, kann sie die erwarteten Verbesserungen nicht bringen und sogar die Leistung des Modells für Ihren Zielbereich verschlechtern.

Bevor Sie also lernen, "wie" man Sprachmodelle feinabstimmt, müssen Sie wissen, "warum" Sie diesen Weg gehen sollten und "wann" Sie mit dem Feinabstimmungsprozess beginnen sollten. Beginnen Sie mit diesen Fragen:

- **Anwendungsfall**: Was ist Ihr _Anwendungsfall_ für die Feinabstimmung? Welchen Aspekt des aktuellen vortrainierten Modells möchten Sie verbessern?
- **Alternativen**: Haben Sie _andere Techniken_ ausprobiert, um die gewünschten Ergebnisse zu erzielen? Nutzen Sie sie, um eine Vergleichsbasis zu schaffen.
  - Prompt Engineering: Probieren Sie Techniken wie Few-Shot-Prompting mit Beispielen für relevante Eingabeaufforderungen. Bewerten Sie die Qualität der Antworten.
  - Retrieval-Augmented Generation: Versuchen Sie, die Eingabeaufforderungen mit Suchergebnissen aus Ihren Daten anzureichern. Bewerten Sie die Qualität der Antworten.
- **Kosten**: Haben Sie die Kosten für die Feinabstimmung identifiziert?
  - Einstellbarkeit – ist das vortrainierte Modell für die Feinabstimmung verfügbar?
  - Aufwand – für die Vorbereitung der Trainingsdaten, Bewertung und Verfeinerung des Modells.
  - Rechenleistung – für das Ausführen der Feinabstimmjobs und das Bereitstellen des feinabgestimmten Modells.
  - Daten – Zugang zu ausreichender Anzahl qualitativ hochwertiger Beispiele für den Feinabstimmungseffekt.
- **Vorteile**: Haben Sie die Vorteile der Feinabstimmung bestätigt?
  - Qualität – hat das feinabgestimmte Modell die Ausgangsbasis übertroffen?
  - Kosten – reduziert es den Tokenverbrauch durch Vereinfachung der Eingabeaufforderungen?
  - Erweiterbarkeit – können Sie das Basismodell für neue Domänen wiederverwenden?

Durch das Beantworten dieser Fragen sollten Sie entscheiden können, ob Feinabstimmung der richtige Ansatz für Ihren Anwendungsfall ist. Idealerweise ist der Ansatz nur gültig, wenn die Vorteile die Kosten überwiegen. Sobald Sie sich zum Weitergehen entschieden haben, ist es Zeit, darüber nachzudenken, _wie_ Sie das vortrainierte Modell feinabstimmen können.

Möchten Sie weitere Einblicke in den Entscheidungsprozess erhalten? Sehen Sie sich [Feinabstimmen oder nicht feinabstimmen](https://www.youtube.com/watch?v=0Jo-z-MFxJs) an.

## Wie können wir ein vortrainiertes Modell feinabstimmen?

Um ein vortrainiertes Modell feinabzustimmen, benötigen Sie:

- ein vortrainiertes Modell zum Feinabstimmen
- einen Datensatz für die Feinabstimmung
- eine Trainingsumgebung für den Feinabstimm-Job
- eine Hosting-Umgebung, um das feinabgestimmte Modell bereitzustellen

## Feinabstimmung in Aktion

> **Hinweis:** `gpt-35-turbo` / `gpt-3.5-turbo`, das in einigen der folgenden Tutorials erwähnt wird, ist sowohl für Inferenz als auch Feinabstimmung eingestellt. Wenn Sie heute einen neuen Feinabstimm-Job starten, zielen Sie stattdessen auf ein derzeit unterstütztes Modell ab – zum Beispiel `gpt-4o-mini` oder `gpt-4.1-mini`. Siehe die [Liste der feinabstimmbaren Modelle](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) für die aktuelle Auswahl an feinabstimmbaren Modellen. Die Konzepte und Schritte in diesen Tutorials gelten weiterhin.

Die folgenden Ressourcen bieten Schritt-für-Schritt-Tutorials, die Sie durch ein konkretes Beispiel mit einem ausgewählten Modell und einem kuratierten Datensatz führen. Um diese Tutorials durchzuarbeiten, benötigen Sie ein Konto beim jeweiligen Anbieter sowie Zugriff auf das relevante Modell und die Datensätze.

| Anbieter     | Tutorial                                                                                                                                                                       | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Wie man Chat-Modelle feinabstimmt](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lernen Sie, ein `gpt-35-turbo` für eine spezifische Domäne („Rezeptassistent“) feinabzustimmen, indem Sie Trainingsdaten vorbereiten, den Feinabstimm-Job ausführen und das feinabgestimmte Modell für die Inferenz verwenden.                                                                                                                                                                                                      |
| Azure OpenAI | [GPT 3.5 Turbo Feinabstimmungs-Tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Lernen Sie, ein `gpt-35-turbo-0613` Modell **auf Azure** feinabzustimmen, indem Sie Schritte zur Erstellung und zum Hochladen von Trainingsdaten durchführen, den Feinabstimm-Job ausführen, das neue Modell bereitstellen und verwenden.                                                                                                                                                                                               |
| Hugging Face | [Feinabstimmung von LLMs mit Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dieser Blogbeitrag führt Sie durch die Feinabstimmung eines _offenen LLM_ (z.B. `CodeLlama 7B`) mit der [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) Bibliothek und [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) mit offenen [Datensätzen](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) auf Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Feinabstimmung von LLMs mit AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (oder AutoTrain Advanced) ist eine von Hugging Face entwickelte Python-Bibliothek, die Feinabstimmung für viele verschiedene Aufgaben, einschließlich LLM-Feinabstimmung, ermöglicht. AutoTrain ist eine No-Code-Lösung und Feinabstimmungen können in Ihrer eigenen Cloud, auf Hugging Face Spaces oder lokal durchgeführt werden. Es unterstützt sowohl eine webbasierte GUI, CLI als auch Training über YAML-Konfigurationsdateien.                        |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Feinabstimmung von LLMs mit Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth ist ein Open-Source-Framework, das LLM-Feinabstimmung und Reinforcement Learning (RL) unterstützt. Unsloth erleichtert lokales Training, Evaluation und Bereitstellung mit einsatzfertigen [Notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Es unterstützt auch Text-zu-Sprache (TTS), BERT und multimodale Modelle. Um loszulegen, lesen Sie deren Schritt-für-Schritt [Feinabstimmungs-Leitfaden für LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Aufgabe

Wählen Sie eines der oben genannten Tutorials aus und arbeiten Sie es durch. _Wir könnten eine Version dieser Tutorials in Jupyter Notebooks in diesem Repo zu Referenzzwecken nachbilden. Bitte verwenden Sie direkt die Originalquellen, um die aktuellsten Versionen zu erhalten_.

## Großartige Arbeit! Setzen Sie Ihr Lernen fort.

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Lernsammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter auszubauen!

Herzlichen Glückwunsch!! Sie haben die letzte Lektion der v2-Serie dieses Kurses abgeschlossen! Hören Sie nicht auf zu lernen und zu bauen. \*\*Schauen Sie auf der [RESSOURCEN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite für eine Liste weiterer Vorschläge speziell zu diesem Thema vorbei.

Unsere v1-Serie von Lektionen wurde auch mit weiteren Aufgaben und Konzepten aktualisiert. Nehmen Sie sich also eine Minute Zeit, um Ihr Wissen aufzufrischen – und bitte [teilen Sie Ihre Fragen und Feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), um uns zu helfen, diese Lektionen für die Community zu verbessern.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->