<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T16:45:39+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "de"
}
-->
[![Open Source Models](../../../../../translated_images/de/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Feinabstimmung Ihres LLM

Die Verwendung großer Sprachmodelle zum Erstellen generativer KI-Anwendungen bringt neue Herausforderungen mit sich. Ein zentrales Problem ist die Sicherstellung der Antwortqualität (Genauigkeit und Relevanz) bei Inhalten, die vom Modell für eine bestimmte Benutzeranfrage generiert werden. In früheren Lektionen haben wir Techniken wie Prompt Engineering und retrieval-unterstützte Generierung besprochen, die versuchen, das Problem durch _Modifikation der Eingabeaufforderung_ an das bestehende Modell zu lösen.

In der heutigen Lektion besprechen wir eine dritte Technik, **Feinabstimmung**, die versucht, die Herausforderung durch _Nachtrainieren des Modells selbst_ mit zusätzlichen Daten zu adressieren. Lassen Sie uns in die Details eintauchen.

## Lernziele

Diese Lektion führt in das Konzept der Feinabstimmung vortrainierter Sprachmodelle ein, beleuchtet die Vorteile und Herausforderungen dieses Ansatzes und gibt Hinweise, wann und wie man Feinabstimmung einsetzt, um die Leistung Ihrer generativen KI-Modelle zu verbessern.

Am Ende dieser Lektion sollten Sie in der Lage sein, die folgenden Fragen zu beantworten:

- Was ist Feinabstimmung bei Sprachmodellen?
- Wann und warum ist Feinabstimmung nützlich?
- Wie kann ich ein vortrainiertes Modell feinabstimmen?
- Was sind die Einschränkungen der Feinabstimmung?

Bereit? Lassen Sie uns anfangen.

## Illustrierter Leitfaden

Möchten Sie einen Überblick über das, was wir behandeln werden, bevor wir ins Detail gehen? Schauen Sie sich diesen illustrierten Leitfaden an, der die Lernreise für diese Lektion beschreibt – vom Erlernen der Kernkonzepte und der Motivation für Feinabstimmung bis hin zum Verständnis des Prozesses und der bewährten Methoden für die Ausführung der Feinabstimmungsaufgabe. Dies ist ein faszinierendes Thema zur Erforschung, vergessen Sie also nicht, die [Ressourcen](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite für zusätzliche Links zu Ihrer selbstgesteuerten Lernreise zu besuchen!

![Illustrierter Leitfaden für die Feinabstimmung von Sprachmodellen](../../../../../translated_images/de/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Was ist Feinabstimmung bei Sprachmodellen?

Große Sprachmodelle sind per Definition _vortrainiert_ auf großen Mengen von Text, der aus vielfältigen Quellen, einschließlich des Internets, stammt. Wie wir in früheren Lektionen gelernt haben, benötigen wir Techniken wie _Prompt Engineering_ und _retrieval-unterstützte Generierung_, um die Qualität der Modellantworten auf Benutzerfragen („Prompts“) zu verbessern.

Eine beliebte Prompt-Engineering-Technik besteht darin, dem Modell mehr Anweisungen darüber zu geben, was in der Antwort erwartet wird, entweder durch _Anweisungen_ (explizite Anleitung) oder _durch das Geben einiger Beispiele_ (implizite Anleitung). Dies wird als _few-shot learning_ bezeichnet, hat jedoch zwei Einschränkungen:

- Die Token-Grenzen des Modells können die Anzahl der Beispiele beschränken, die Sie geben können, und die Wirksamkeit begrenzen.
- Die Token-Kosten des Modells können es teuer machen, bei jeder Aufforderung Beispiele hinzuzufügen, und die Flexibilität einschränken.

Feinabstimmung ist eine gängige Praxis in maschinellen Lernsystemen, bei der wir ein vortrainiertes Modell nehmen und es mit neuen Daten nachtrainieren, um seine Leistung bei einer bestimmten Aufgabe zu verbessern. Im Kontext von Sprachmodellen können wir das vortrainierte Modell _mit einem kuratierten Satz von Beispielen für eine bestimmte Aufgabe oder Anwendungsdomäne_ feinabstimmen, um ein **benutzerdefiniertes Modell** zu erstellen, das für diese spezifische Aufgabe oder Domäne möglicherweise genauer und relevanter ist. Ein Nebeneffekt der Feinabstimmung ist, dass sie auch die Anzahl der Beispiele für Few-Shot-Lernen reduzieren kann – wodurch der Token-Verbrauch und die damit verbundenen Kosten gesenkt werden.

## Wann und warum sollten wir Modelle feinabstimmen?

In _diesem_ Kontext, wenn wir von Feinabstimmung sprechen, meinen wir **überwachte** Feinabstimmung, bei der das Nachtrainieren durch **Hinzufügen neuer Daten** erfolgt, die nicht Teil des ursprünglichen Trainingsdatensatzes waren. Dies unterscheidet sich von einem unüberwachten Feinabstimmungsansatz, bei dem das Modell mit den Originaldaten, aber mit anderen Hyperparametern nachtrainiert wird.

Das Wichtigste ist, sich daran zu erinnern, dass Feinabstimmung eine fortgeschrittene Technik ist, die ein gewisses Maß an Fachwissen erfordert, um die gewünschten Ergebnisse zu erzielen. Wenn sie falsch durchgeführt wird, kann sie die erwarteten Verbesserungen nicht liefern und sogar die Leistung des Modells für Ihre Ziel-Domäne verschlechtern.

Bevor Sie also lernen, „wie“ man Sprachmodelle feinabstimmt, müssen Sie wissen, „warum“ Sie diesen Weg einschlagen sollten, und „wann“ Sie den Prozess der Feinabstimmung starten sollten. Beginnen Sie damit, sich diese Fragen zu stellen:

- **Anwendungsfall**: Was ist Ihr _Anwendungsfall_ für die Feinabstimmung? Welchen Aspekt des aktuellen vortrainierten Modells möchten Sie verbessern?
- **Alternativen**: Haben Sie _andere Techniken_ ausprobiert, um die gewünschten Ergebnisse zu erzielen? Nutzen Sie diese, um eine Vergleichsbasis zu schaffen.
  - Prompt Engineering: Probieren Sie Techniken wie Few-Shot-Prompting mit Beispielen relevanter Prompt-Antworten. Bewerten Sie die Qualität der Antworten.
  - Retrieval Augmented Generation: Versuchen Sie, Prompts mit Suchergebnissen Ihrer Daten anzureichern. Bewerten Sie die Qualität der Antworten.
- **Kosten**: Haben Sie die Kosten der Feinabstimmung identifiziert?
  - Einstellbarkeit – ist das vortrainierte Modell für Feinabstimmung verfügbar?
  - Aufwand – für die Vorbereitung der Trainingsdaten, Bewertung & Verfeinerung des Modells.
  - Rechenleistung – für das Ausführen von Feinabstimmungsaufträgen und Bereitstellung des feinabgestimmten Modells
  - Daten – Zugriff auf genügend qualitativ hochwertige Beispiele für eine wirkungsvolle Feinabstimmung
- **Vorteile**: Haben Sie die Vorteile der Feinabstimmung bestätigt?
  - Qualität – hat das feinabgestimmte Modell die Grundlage übertroffen?
  - Kosten – reduziert es die Token-Nutzung durch Vereinfachung der Prompts?
  - Erweiterbarkeit – können Sie das Basismodell für neue Domänen wiederverwenden?

Durch das Beantworten dieser Fragen sollten Sie in der Lage sein zu entscheiden, ob Feinabstimmung der richtige Ansatz für Ihren Anwendungsfall ist. Idealerweise ist der Ansatz nur dann sinnvoll, wenn die Vorteile die Kosten überwiegen. Sobald Sie sich entscheiden weiterzumachen, ist es an der Zeit, darüber nachzudenken, _wie_ Sie das vortrainierte Modell feinabstimmen können.

Möchten Sie mehr Einblicke in den Entscheidungsprozess? Sehen Sie sich [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs) an.

## Wie können wir ein vortrainiertes Modell feinabstimmen?

Um ein vortrainiertes Modell feinabzustimmen, benötigen Sie:

- ein vortrainiertes Modell zur Feinabstimmung
- einen Datensatz zur Verwendung für die Feinabstimmung
- eine Trainingsumgebung, um den Feinabstimmungsjob auszuführen
- eine Hostingumgebung, um das feinabgestimmte Modell bereitzustellen

## Feinabstimmung in Aktion

Die folgenden Ressourcen bieten Schritt-für-Schritt-Anleitungen, die Sie durch ein echtes Beispiel mit einem ausgewählten Modell und einem kuratierten Datensatz führen. Um diese Tutorials zu bearbeiten, benötigen Sie ein Konto beim jeweiligen Anbieter sowie Zugang zu den entsprechenden Modellen und Datensätzen.

| Anbieter    | Tutorial                                                                                                                                                                       | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lernen Sie, ein `gpt-35-turbo` für eine spezifische Domäne ("Rezeptassistent") feinabzustimmen, indem Sie Trainingsdaten vorbereiten, den Feinabstimmungsjob ausführen und das feinabgestimmte Modell für Inferenz verwenden.                                                                                                                                                                                                     |
| Azure OpenAI| [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Lernen Sie, ein `gpt-35-turbo-0613` Modell **auf Azure** feinabzustimmen, indem Sie Schritte zur Erstellung & zum Hochladen von Trainingsdaten durchführen, den Feinabstimmungsjob ausführen, das neue Modell bereitstellen und verwenden.                                                                                                                                                                                          |
| Hugging Face| [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dieser Blogbeitrag führt Sie durch die Feinabstimmung eines _offenen LLM_ (z. B. `CodeLlama 7B`) unter Verwendung der [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) Bibliothek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) mit offenen [Datensätzen](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) auf Hugging Face. |
|             |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain| [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (oder AutoTrain Advanced) ist eine von Hugging Face entwickelte Python-Bibliothek, die das Feinabstimmen für viele verschiedene Aufgaben, einschließlich LLM-Feinabstimmung, erlaubt. AutoTrain ist eine No-Code-Lösung, und die Feinabstimmung kann in Ihrer eigenen Cloud, auf Hugging Face Spaces oder lokal durchgeführt werden. Es unterstützt sowohl eine webbasierte GUI, eine CLI als auch Training via YAML-Konfigurationsdateien.                     |
|             |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth  | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth)                                                                                                         | Unsloth ist ein Open-Source-Framework, das LLM-Feinabstimmung und Reinforcement Learning (RL) unterstützt. Unsloth erleichtert lokales Training, Evaluation und Bereitstellung mit gebrauchsfertigen [Notebooks](https://github.com/unslothai/notebooks). Es unterstützt auch Text-to-Speech (TTS), BERT und multimodale Modelle. Um zu starten, lesen Sie ihren schrittweisen [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                          |
|             |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Aufgabe

Wählen Sie eines der oben genannten Tutorials aus und arbeiten Sie es durch. _Wir könnten eine Version dieser Tutorials in Jupyter Notebooks in diesem Repo nur zu Referenzzwecken nachbilden. Bitte verwenden Sie die Originalquellen direkt, um die aktuellsten Versionen zu erhalten_.

## Großartige Arbeit! Setzen Sie Ihr Lernen fort.

Nach Abschluss dieser Lektion, sehen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihre Kenntnisse zu generativer KI weiter zu vertiefen!

Herzlichen Glückwunsch!! Sie haben die letzte Lektion aus der v2-Serie dieses Kurses abgeschlossen! Hören Sie nicht auf zu lernen und zu entwickeln. \*\*Schauen Sie auf der [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) Seite vorbei für eine Liste zusätzlicher Vorschläge nur zu diesem Thema.

Unsere v1-Serie von Lektionen wurde ebenfalls mit weiteren Aufgaben und Konzepten aktualisiert. Nehmen Sie sich also eine Minute Zeit, um Ihr Wissen aufzufrischen – und bitte [teilen Sie Ihre Fragen und Ihr Feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), um uns zu helfen, diese Lektionen für die Community zu verbessern.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, können automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten. Die Originalfassung des Dokuments in der Ausgangssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->