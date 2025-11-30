<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T22:58:18+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "de"
}
-->
[![Open Source Modelle](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.de.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Feinabstimmung Ihres LLM

Die Nutzung großer Sprachmodelle zur Entwicklung generativer KI-Anwendungen bringt neue Herausforderungen mit sich. Ein zentrales Problem ist die Sicherstellung der Qualität der Antworten (Genauigkeit und Relevanz) in den vom Modell generierten Inhalten für eine bestimmte Benutzeranfrage. In den vorherigen Lektionen haben wir Techniken wie Prompt Engineering und Retrieval-augmented Generation besprochen, die versuchen, das Problem durch _Modifikation der Eingabeaufforderung_ des bestehenden Modells zu lösen.

In der heutigen Lektion besprechen wir eine dritte Technik, **Feinabstimmung**, die versucht, die Herausforderung durch _Neutrainieren des Modells selbst_ mit zusätzlichen Daten zu bewältigen. Tauchen wir in die Details ein.

## Lernziele

Diese Lektion führt in das Konzept der Feinabstimmung vortrainierter Sprachmodelle ein, untersucht die Vorteile und Herausforderungen dieses Ansatzes und gibt Hinweise, wann und wie Feinabstimmung eingesetzt werden kann, um die Leistung Ihrer generativen KI-Modelle zu verbessern.

Am Ende dieser Lektion sollten Sie folgende Fragen beantworten können:

- Was ist Feinabstimmung für Sprachmodelle?
- Wann und warum ist Feinabstimmung nützlich?
- Wie kann ich ein vortrainiertes Modell feinabstimmen?
- Welche Einschränkungen hat die Feinabstimmung?

Bereit? Los geht's.

## Illustrierte Anleitung

Möchten Sie sich einen Überblick über die Inhalte verschaffen, bevor wir ins Detail gehen? Sehen Sie sich diese illustrierte Anleitung an, die die Lernreise für diese Lektion beschreibt – von den Kernkonzepten und der Motivation für die Feinabstimmung bis hin zum Verständnis des Prozesses und der besten Praktiken für die Durchführung der Feinabstimmung. Dies ist ein faszinierendes Thema, das es zu erkunden gilt. Vergessen Sie nicht, die Seite [Ressourcen](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) für zusätzliche Links zu besuchen, die Ihre selbstgesteuerte Lernreise unterstützen!

![Illustrierte Anleitung zur Feinabstimmung von Sprachmodellen](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.de.png)

## Was ist Feinabstimmung für Sprachmodelle?

Per Definition sind große Sprachmodelle _vortrainiert_ auf großen Mengen von Texten, die aus verschiedenen Quellen, einschließlich des Internets, stammen. Wie wir in den vorherigen Lektionen gelernt haben, benötigen wir Techniken wie _Prompt Engineering_ und _Retrieval-augmented Generation_, um die Qualität der Antworten des Modells auf die Fragen des Benutzers („Prompts“) zu verbessern.

Eine beliebte Technik des Prompt Engineering besteht darin, dem Modell mehr Anleitung zu geben, was in der Antwort erwartet wird, entweder durch _Anweisungen_ (explizite Anleitung) oder _einige Beispiele_ (implizite Anleitung). Dies wird als _Few-Shot-Lernen_ bezeichnet, hat jedoch zwei Einschränkungen:

- Die Token-Limits des Modells können die Anzahl der Beispiele, die Sie geben können, einschränken und die Effektivität begrenzen.
- Die Token-Kosten des Modells können es teuer machen, Beispiele zu jeder Eingabeaufforderung hinzuzufügen, und die Flexibilität einschränken.

Feinabstimmung ist eine gängige Praxis in maschinellen Lernsystemen, bei der wir ein vortrainiertes Modell nehmen und es mit neuen Daten neu trainieren, um seine Leistung für eine bestimmte Aufgabe zu verbessern. Im Kontext von Sprachmodellen können wir das vortrainierte Modell _mit einer kuratierten Sammlung von Beispielen für eine bestimmte Aufgabe oder einen bestimmten Anwendungsbereich_ feinabstimmen, um ein **benutzerdefiniertes Modell** zu erstellen, das für diese spezifische Aufgabe oder diesen Bereich möglicherweise genauer und relevanter ist. Ein Nebeneffekt der Feinabstimmung ist, dass sie auch die Anzahl der für das Few-Shot-Lernen benötigten Beispiele reduzieren kann – was den Tokenverbrauch und die damit verbundenen Kosten senkt.

## Wann und warum sollten wir Modelle feinabstimmen?

In _diesem_ Kontext sprechen wir von **überwachter** Feinabstimmung, bei der das Neutrainieren durch **Hinzufügen neuer Daten** erfolgt, die nicht Teil des ursprünglichen Trainingsdatensatzes waren. Dies unterscheidet sich von einem unüberwachten Feinabstimmungsansatz, bei dem das Modell mit den ursprünglichen Daten, aber mit anderen Hyperparametern neu trainiert wird.

Das Wichtigste, das Sie sich merken sollten, ist, dass Feinabstimmung eine fortgeschrittene Technik ist, die ein gewisses Maß an Fachwissen erfordert, um die gewünschten Ergebnisse zu erzielen. Wenn sie falsch durchgeführt wird, kann sie die erwarteten Verbesserungen nicht liefern und sogar die Leistung des Modells für Ihren Zielbereich verschlechtern.

Bevor Sie also lernen, „wie“ Sie Sprachmodelle feinabstimmen, müssen Sie wissen, „warum“ Sie diesen Weg einschlagen sollten und „wann“ Sie mit dem Prozess der Feinabstimmung beginnen sollten. Stellen Sie sich zunächst folgende Fragen:

- **Anwendungsfall**: Was ist Ihr _Anwendungsfall_ für die Feinabstimmung? Welchen Aspekt des aktuellen vortrainierten Modells möchten Sie verbessern?
- **Alternativen**: Haben Sie _andere Techniken_ ausprobiert, um die gewünschten Ergebnisse zu erzielen? Verwenden Sie diese, um eine Vergleichsgrundlage zu schaffen.
  - Prompt Engineering: Probieren Sie Techniken wie Few-Shot-Prompting mit Beispielen relevanter Eingabeaufforderungsantworten aus. Bewerten Sie die Qualität der Antworten.
  - Retrieval-augmented Generation: Versuchen Sie, Eingabeaufforderungen mit Abfrageergebnissen zu ergänzen, die durch die Suche in Ihren Daten abgerufen wurden. Bewerten Sie die Qualität der Antworten.
- **Kosten**: Haben Sie die Kosten für die Feinabstimmung identifiziert?
  - Abstimmungsfähigkeit – Ist das vortrainierte Modell für die Feinabstimmung verfügbar?
  - Aufwand – für die Vorbereitung von Trainingsdaten, die Bewertung und Verfeinerung des Modells.
  - Rechenleistung – für die Durchführung von Feinabstimmungsjobs und die Bereitstellung des feinabgestimmten Modells.
  - Daten – Zugang zu ausreichend qualitativ hochwertigen Beispielen für den Einfluss der Feinabstimmung.
- **Vorteile**: Haben Sie die Vorteile der Feinabstimmung bestätigt?
  - Qualität – hat das feinabgestimmte Modell die Vergleichsgrundlage übertroffen?
  - Kosten – reduziert es den Tokenverbrauch durch vereinfachte Eingabeaufforderungen?
  - Erweiterbarkeit – können Sie das Basismodell für neue Bereiche wiederverwenden?

Indem Sie diese Fragen beantworten, sollten Sie entscheiden können, ob die Feinabstimmung der richtige Ansatz für Ihren Anwendungsfall ist. Idealerweise ist der Ansatz nur dann gültig, wenn die Vorteile die Kosten überwiegen. Sobald Sie sich entschieden haben, weiterzumachen, ist es an der Zeit, darüber nachzudenken, _wie_ Sie das vortrainierte Modell feinabstimmen können.

Möchten Sie weitere Einblicke in den Entscheidungsprozess erhalten? Sehen Sie sich [Feinabstimmen oder nicht feinabstimmen](https://www.youtube.com/watch?v=0Jo-z-MFxJs) an.

## Wie können wir ein vortrainiertes Modell feinabstimmen?

Um ein vortrainiertes Modell feinabzustimmen, benötigen Sie:

- ein vortrainiertes Modell zur Feinabstimmung
- einen Datensatz zur Feinabstimmung
- eine Trainingsumgebung, um den Feinabstimmungsjob auszuführen
- eine Hosting-Umgebung, um das feinabgestimmte Modell bereitzustellen

## Feinabstimmung in der Praxis

Die folgenden Ressourcen bieten Schritt-für-Schritt-Tutorials, die Sie durch ein echtes Beispiel mit einem ausgewählten Modell und einem kuratierten Datensatz führen. Um diese Tutorials durchzuarbeiten, benötigen Sie ein Konto beim jeweiligen Anbieter sowie Zugriff auf das entsprechende Modell und die Datensätze.

| Anbieter      | Tutorial                                                                                                                                                                       | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI        | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Lernen Sie, wie Sie ein `gpt-35-turbo` für einen bestimmten Bereich („Rezeptassistent“) feinabstimmen, indem Sie Trainingsdaten vorbereiten, den Feinabstimmungsjob ausführen und das feinabgestimmte Modell für Inferenz verwenden.                                                                                                                                                                                                 |
| Azure OpenAI  | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Lernen Sie, wie Sie ein `gpt-35-turbo-0613` Modell **auf Azure** feinabstimmen, indem Sie Schritte unternehmen, um Trainingsdaten zu erstellen und hochzuladen, den Feinabstimmungsjob auszuführen. Stellen Sie das neue Modell bereit und verwenden Sie es.                                                                                                                                                                                                                 |
| Hugging Face  | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dieser Blogbeitrag führt Sie durch die Feinabstimmung eines _offenen LLM_ (z. B. `CodeLlama 7B`) mit der [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) Bibliothek & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) mit offenen [Datensätzen](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) auf Hugging Face. |
|               |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain  | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (oder AutoTrain Advanced) ist eine von Hugging Face entwickelte Python-Bibliothek, die Feinabstimmung für viele verschiedene Aufgaben einschließlich LLM-Feinabstimmung ermöglicht. AutoTrain ist eine No-Code-Lösung, und die Feinabstimmung kann in Ihrer eigenen Cloud, auf Hugging Face Spaces oder lokal durchgeführt werden. Es unterstützt sowohl eine webbasierte GUI, CLI als auch Training über YAML-Konfigurationsdateien.                     |
|               |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Aufgabe

Wählen Sie eines der oben genannten Tutorials aus und arbeiten Sie es durch. _Wir können eine Version dieser Tutorials in Jupyter Notebooks in diesem Repository nur zu Referenzzwecken replizieren. Bitte verwenden Sie die Originalquellen direkt, um die neuesten Versionen zu erhalten_.

## Gute Arbeit! Setzen Sie Ihr Lernen fort.

Nachdem Sie diese Lektion abgeschlossen haben, sehen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter zu vertiefen!

Herzlichen Glückwunsch!! Sie haben die letzte Lektion der v2-Serie dieses Kurses abgeschlossen! Hören Sie nicht auf zu lernen und zu bauen. \*\*Sehen Sie sich die Seite [RESSOURCEN](RESOURCES.md?WT.mc_id=academic-105485-koreyst) für eine Liste zusätzlicher Vorschläge zu diesem Thema an.

Unsere v1-Serie von Lektionen wurde ebenfalls mit weiteren Aufgaben und Konzepten aktualisiert. Nehmen Sie sich also einen Moment Zeit, um Ihr Wissen aufzufrischen – und bitte [teilen Sie uns Ihre Fragen und Ihr Feedback mit](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), um uns zu helfen, diese Lektionen für die Community zu verbessern.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.