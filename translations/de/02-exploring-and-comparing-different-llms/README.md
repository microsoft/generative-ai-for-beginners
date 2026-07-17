# Erkundung und Vergleich verschiedener LLMs

[![Erkundung und Vergleich verschiedener LLMs](../../../translated_images/de/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klicken Sie auf das Bild oben, um das Video dieser Lektion anzusehen_

Mit der vorherigen Lektion haben wir gesehen, wie Generative KI die Technologieszene verändert, wie Large Language Models (LLMs) funktionieren und wie ein Unternehmen – wie unser Startup – sie für seine Anwendungsfälle einsetzen und dadurch wachsen kann! In diesem Kapitel wollen wir verschiedene Arten von großen Sprachmodellen (LLMs) vergleichen und gegenüberstellen, um deren Vor- und Nachteile zu verstehen.

Der nächste Schritt auf der Reise unseres Startups ist es, die aktuelle Landschaft der LLMs zu erkunden und zu verstehen, welche für unseren Anwendungsfall geeignet sind.

## Einführung

Diese Lektion behandelt:

- Verschiedene Typen von LLMs in der aktuellen Landschaft.
- Testen, Iterieren und Vergleichen verschiedener Modelle für Ihren Anwendungsfall in Azure.
- Wie man ein LLM bereitstellt.

## Lernziele

Nach Abschluss dieser Lektion können Sie:

- Das richtige Modell für Ihren Anwendungsfall auswählen.
- Verstehen, wie man die Leistung Ihres Modells testet, iteriert und verbessert.
- Wissen, wie Unternehmen Modelle bereitstellen.

## Verschiedene Arten von LLMs verstehen

LLMs können anhand ihrer Architektur, Trainingsdaten und ihres Anwendungsfalls unterschiedlich kategorisiert werden. Diese Unterschiede zu verstehen hilft unserem Startup, das richtige Modell für das Szenario auszuwählen und zu begreifen, wie man Leistung testet, iteriert und verbessert.

Es gibt viele verschiedene Arten von LLM-Modellen. Ihre Modellwahl hängt davon ab, wofür Sie sie einsetzen möchten, von Ihren Daten, wie viel Sie bereit sind zu zahlen und mehr.

Je nachdem, ob Sie die Modelle für Text, Audio, Video, Bildgenerierung usw. verwenden möchten, wählen Sie möglicherweise unterschiedliche Modellentypen.

- **Audio- und Spracherkennung**. Whisper-ähnliche Modelle sind nach wie vor nützliche allgemeine Spracherkennungsmodelle, aber bei Produktionsoptionen sind heute auch neuere Speech-to-Text-Modelle wie `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` und Varianten mit Diarisierung enthalten. Bewerten Sie Sprachabdeckung, Diarisierung, Echtzeitunterstützung, Latenz und Kosten für Ihr Szenario. Mehr erfahren Sie in der [OpenAI Speech-to-Text-Dokumentation](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Bildgenerierung**. DALL-E und Midjourney sind bekannte Optionen zur Bildgenerierung, jedoch konzentrieren sich aktuelle OpenAI Bild-APIs auf GPT-Bildmodelle wie `gpt-image-2`, während Stable Diffusion, Imagen, Flux und andere Modellfamilien ebenfalls häufig verwendet werden. Vergleichen Sie Einhaltung der Eingabeaufforderung, Bearbeitungsunterstützung, Stilkontrolle, Sicherheitsanforderungen und Lizenzierung. Weitere Informationen finden Sie im [OpenAI Image Generation Guide](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) und Kapitel 9 dieses Curriculums.

- **Textgenerierung**. Textmodelle umfassen heute Frontier-Modelle, Reasoning-Modelle, kleinere Modelle mit niedriger Latenz und Open-Weight-Modelle. Aktuelle Beispiele sind OpenAI GPT-5.x Modelle, Anthropic Claude 4.x Modelle, Google Gemini 3.x Modelle, Meta Llama 4 Modelle und Mistral-Modelle. Wählen Sie nicht nur nach Erscheinungsdatum oder Preis; vergleichen Sie Aufgabenqualität, Latenz, Kontextfenster, Werkzeugnutzung, Sicherheitsverhalten, regionale Verfügbarkeit und Gesamtkosten. Der [Microsoft Foundry Modellkatalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) ist ein guter Ort, um verfügbare Modelle auf Azure zu vergleichen.

- **Multimodalität**. Viele aktuelle Modelle können mehr als nur Text verarbeiten. Einige akzeptieren Bild-, Audio- oder Videoeingaben; manche können Werkzeuge aufrufen; spezialisierte Modelle können Bilder, Audio oder Video generieren. Zum Beispiel unterstützen aktuelle OpenAI Modelle Text- und Bildeingaben, Gemini-Modelle unterstützen je nach Variante Text, Code, Bild, Audio und Videoeingaben, und Llama 4 Scout sowie Maverick sind native multimodale Open-Weight-Modelle. Prüfen Sie vor dem Aufbau eines Workflows in jedem Fall die Modellbeschreibung auf die unterstützten Eingabe- und Ausgabemodalitäten.

Die Wahl eines Modells bedeutet, dass Sie einige Grundfähigkeiten erhalten, die jedoch nicht immer ausreichen. Oft gibt es unternehmensspezifische Daten, über die Sie das LLM informieren müssen. Hier gibt es verschiedene Ansätze, mehr dazu in den folgenden Abschnitten.

### Foundation Models versus LLMs

Der Begriff Foundation Model wurde von [Stanford Forschern geprägt](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) und definiert ein KI-Modell, das bestimmte Kriterien erfüllt, wie z. B.:

- **Sie werden mittels unüberwachtem Lernen oder selbstüberwachtem Lernen trainiert**, das heißt, sie werden mit unlabeled multimodalen Daten trainiert und benötigen keine menschliche Annotation oder Kennzeichnung von Daten im Trainingsprozess.
- **Sie sind sehr große Modelle**, die auf sehr tiefen neuronalen Netzwerken mit Milliarden von Parametern basieren.
- **Sie sind normalerweise dafür gedacht, als 'Basis' für andere Modelle zu dienen**, das heißt, sie können als Ausgangspunkt für den Aufbau weiterer Modelle genutzt werden, zum Beispiel durch Feinabstimmung (Fine-Tuning).

![Foundation Models versus LLMs](../../../translated_images/de/FoundationModel.e4859dbb7a825c94.webp)

Bildquelle: [Essential Guide to Foundation Models and Large Language Models | von Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Um diese Unterscheidung weiter zu verdeutlichen, betrachten wir ChatGPT als historisches Beispiel. Frühe Versionen von ChatGPT verwendeten GPT-3.5 als Foundation Model. OpenAI nutzte dann chat-spezifische Daten und Ausrichtungstechniken, um eine abgestimmte Version zu erstellen, die in Gesprächsszenarien wie Chatbots besser performt. Moderne KI-Dienste leiten oft zwischen mehreren Modellvarianten weiter, deshalb sind der Dienstname und der zugrundeliegende Modellname nicht immer identisch.

![Foundation Model](../../../translated_images/de/Multimodal.2c389c6439e0fc51.webp)

Bildquelle: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus proprietäre Modelle

Eine weitere Art, LLMs zu kategorisieren, ist die Unterscheidung zwischen open-weight, open-source und proprietär.

Open-Source- und Open-Weight-Modelle stellen Modellartefakte zur Inspektion, zum Download oder zur Anpassung bereit, unterscheiden sich jedoch in ihren Lizenzen. Einige sind vollständig Open Source, andere sind Open-Weight-Modelle mit Nutzungsbeschränkungen. Sie sind nützlich, wenn ein Unternehmen mehr Kontrolle über Bereitstellung, Datenlokalität, Kosten oder Anpassung benötigt. Dennoch müssen Teams die Lizenzbedingungen, Betriebskosten, Wartung, Sicherheits-Updates und Evaluationsqualität prüfen, bevor sie diese Modelle produktiv einsetzen. Beispiele sind [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), einige [Mistral Modelle](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) und viele Modelle, die bei [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst) gehostet werden.

Proprietäre Modelle gehören einem Anbieter und werden von diesem gehostet. Diese Modelle sind oft für den verwalteten Produktionseinsatz optimiert und bieten starken Support, Sicherheitssysteme, Tool-Integration und Skalierbarkeit. Kunden können aber üblicherweise nicht die Modellgewichte inspizieren oder modifizieren und müssen Anbieterbedingungen betreffend Datenschutz, Datenaufbewahrung, Compliance und zulässige Nutzung prüfen. Beispiele sind [OpenAI Modelle](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) und [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus Bildgenerierung versus Text- und Codegenerierung

LLMs können auch nach der Art der Ausgabe kategorisiert werden.

Embeddings sind eine Gruppe von Modellen, die Text in eine numerische Form umwandeln, ein sogenanntes Embedding, das eine numerische Darstellung des Eingabetextes darstellt. Embeddings erleichtern es Maschinen, Beziehungen zwischen Wörtern oder Sätzen zu verstehen und können als Eingaben für andere Modelle genutzt werden, wie Klassifizierungsmodelle oder Cluster-Modelle, die bessere Leistung bei numerischen Daten haben. Embedding-Modelle werden oft für Transferlernen eingesetzt, bei dem ein Modell für eine Ersatzaufgabe mit reichlich Daten erstellt wird und dann die Modellgewichte (Embeddings) für andere nachgelagerte Aufgaben wiederverwendet werden. Ein Beispiel für diese Kategorie sind [OpenAI Embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/de/Embedding.c3708fe988ccf760.webp)

Bildgenerierungsmodelle sind Modelle, die Bilder erzeugen. Diese Modelle werden oft für Bildbearbeitung, Bildsynthese und Bildübersetzung verwendet. Bildgenerierungsmodelle werden häufig auf großen Bilddatensätzen wie [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst) trainiert und können neue Bilder generieren oder bestehende Bilder mit Inpainting-, Super-Resolution- und Kolorierungstechniken bearbeiten. Beispiele sind [GPT-Bildmodelle](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion-Modelle](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) und Imagen-Modelle.

![Bildgenerierung](../../../translated_images/de/Image.349c080266a763fd.webp)

Text- und Codegenerierungsmodelle sind Modelle, die Text oder Code erzeugen. Diese Modelle werden häufig für Textzusammenfassung, Übersetzung und Beantwortung von Fragen verwendet. Textgenerierungsmodelle werden oft auf großen Textdatensätzen wie [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst) trainiert und können neuen Text generieren oder Fragen beantworten. Codegenerierungsmodelle wie [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst) werden oft auf großen Code-Datensätzen wie GitHub trainiert und können neuen Code generieren oder Fehler in bestehendem Code beheben.

![Text- und Codegenerierung](../../../translated_images/de/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus nur Decoder

Um über die verschiedenen Arten von LLM-Architekturen zu sprechen, verwenden wir eine Analogie.

Stellen Sie sich vor, Ihr Manager gibt Ihnen die Aufgabe, ein Quiz für die Schüler zu erstellen. Sie haben zwei Kollegen; einer ist für die Inhaltserstellung und der andere für die Überprüfung verantwortlich.

Der Inhaltsersteller ist wie ein nur-Decoder-Modell: Er kann sich das Thema ansehen, sehen, was Sie bereits geschrieben haben und dann den Inhalt basierend auf diesem Kontext weiter erzeugen. Sie sind sehr gut darin, ansprechenden und informativen Inhalt zu schreiben, aber nicht immer die beste Wahl, wenn die Aufgabe nur darin besteht, Informationen zu klassifizieren, abzurufen oder zu kodieren. Beispiele für nur-Decoder-Modellfamilien sind GPT- und Llama-Modelle.

Der Prüfer ist wie ein nur-Encoder-Modell; er sieht sich den geschriebenen Kurs und die Antworten an, erkennt die Beziehung zwischen ihnen und versteht den Kontext, ist aber nicht gut im Erzeugen von Inhalten. Ein Beispiel für ein nur-Encoder-Modell ist BERT.

Stellen Sie sich vor, wir hätten jemanden, der sowohl das Quiz erstellen als auch prüfen könnte – das ist ein Encoder-Decoder-Modell. Beispiele hierfür sind BART und T5.

### Dienst versus Modell

Nun sprechen wir über den Unterschied zwischen einem Dienst und einem Modell. Ein Dienst ist ein Produkt, das von einem Cloud-Service-Anbieter angeboten wird und oft eine Kombination aus Modellen, Daten und anderen Komponenten darstellt. Ein Modell ist die Kernkomponente eines Dienstes und oft ein Foundation Model wie ein LLM.

Dienste sind oft für den Produktionseinsatz optimiert und oft einfacher zu verwenden als Modelle, etwa über eine grafische Benutzeroberfläche. Dienste sind jedoch nicht immer kostenlos verfügbar und können ein Abonnement oder eine Zahlung erfordern, im Austausch für die Nutzung der Ausrüstung und Ressourcen des Dienstinhabers, Kostenoptimierung und einfache Skalierung. Ein Beispiel für einen Dienst ist [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), der ein Pay-as-you-go-Tarifmodell anbietet, bei dem Nutzer proportional zu ihrer Nutzung des Dienstes belastet werden. Azure OpenAI Service bietet zudem Sicherheit auf Unternehmensniveau und ein verantwortungsbewusstes KI-Rahmenwerk zusätzlich zu den Fähigkeiten der Modelle.

Modelle sind die Artefakte des neuronalen Netzwerks: Parameter, Gewichte, Architektur, Tokenizer und unterstützende Konfiguration. Die Ausführung eines Modells lokal oder in einer privaten Umgebung erfordert geeignete Hardware, Bereitstellungsinfrastruktur, Überwachung sowie entweder eine kompatible Open-Source/Open-Weight-Lizenz oder eine kommerzielle Lizenz. Open-Weight-Modelle wie Llama 4 oder Mistral-Modelle können selbst gehostet werden, benötigen aber weiterhin Rechenleistung und Betriebsexpertise.

## Wie man verschiedene Modelle testet und iteriert, um die Leistung auf Azure zu verstehen


Sobald unser Team die aktuelle Landschaft der LLMs erkundet und einige gute Kandidaten für ihre Szenarien identifiziert hat, besteht der nächste Schritt darin, diese mit ihren Daten und ihrer Arbeitslast zu testen. Dies ist ein iterativer Prozess, der durch Experimente und Messungen erfolgt.
Die meisten der Modelle, die wir in den vorherigen Absätzen erwähnt haben (OpenAI-Modelle, Open-Weight-Modelle wie Llama 4 und Mistral sowie Hugging Face-Modelle), sind in [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) verfügbar.

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), ehemals Azure AI Studio/Azure AI Foundry, ist eine einheitliche Azure-Plattform zum Erstellen von KI-Anwendungen und Agenten. Sie hilft Entwicklern, den Lebenszyklus vom Experimentieren und Bewerten bis hin zum Einsatz, Monitoring und der Governance zu verwalten. Der Modellkatalog in Microsoft Foundry ermöglicht es dem Nutzer:

- Im Katalog das gewünschte Foundation-Modell zu finden, einschließlich Modelle, die von Azure verkauft werden, sowie Modelle von Partnern und Community-Anbietern. Nutzer können nach Aufgabe, Anbieter, Lizenz, Bereitstellungsoption oder Name filtern.

![Model catalog](../../../translated_images/de/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Die Model Card zu prüfen, einschließlich einer detaillierten Beschreibung der beabsichtigten Nutzung und der Trainingsdaten, Codebeispielen und Evaluierungsergebnissen aus der internen Evaluierungsbibliothek.

![Model card](../../../translated_images/de/ModelCard.598051692c6e400d.webp)

- Benchmarks über Modelle und Datensätze der Branche zu vergleichen, um zu bewerten, welches Modell am besten zum Geschäftsszenario passt, über das [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst) Bedienfeld.

![Model benchmarks](../../../translated_images/de/ModelBenchmarks.254cb20fbd06c03a.webp)

- Unterstützte Modelle mit eigenen Trainingsdaten feinabzustimmen, um die Modellleistung in einem spezifischen Arbeitsaufwand zu verbessern, mit den Experimentier- und Nachverfolgungsmöglichkeiten von Microsoft Foundry.

![Model fine-tuning](../../../translated_images/de/FineTuning.aac48f07142e36fd.webp)

- Das ursprüngliche vortrainierte Modell oder die feinabgestimmte Version an einen entfernten Echtzeit-Inferenzendpunkt zu deployen, unter Verwendung von Managed Compute oder serverlosen Bereitstellungsoptionen, um Anwendungen die Nutzung zu ermöglichen.

![Model deployment](../../../translated_images/de/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nicht alle Modelle im Katalog sind derzeit für Feinabstimmung und/oder Pay-as-you-go-Bereitstellung verfügbar. Prüfen Sie die Model Card für Details zu den Fähigkeiten und Einschränkungen des Modells.

## Verbesserung der LLM-Ergebnisse

Unser Startup-Team hat verschiedene Arten von LLMs und eine Cloud-Plattform (Microsoft Foundry) erkundet, die es uns ermöglicht, verschiedene Modelle zu vergleichen, auf Testdaten zu bewerten, die Leistung zu verbessern und sie auf Inferenzendpunkten bereitzustellen.

Aber wann sollten sie in Erwägung ziehen, ein Modell fein abzustimmen, anstatt ein vortrainiertes Modell zu verwenden? Gibt es andere Ansätze, um die Modellleistung bei spezifischen Arbeitslasten zu verbessern?

Ein Unternehmen kann verschiedene Ansätze nutzen, um die Ergebnisse zu erhalten, die es von einem LLM benötigt. Sie können unterschiedliche Arten von Modellen mit verschiedenen Trainingsgraden auswählen, wenn sie ein LLM produktiv einsetzen, mit unterschiedlichen Komplexitäts-, Kosten- und Qualitätsstufen. Hier sind einige verschiedene Ansätze:

- **Prompt-Engineering mit Kontext**. Die Idee ist, beim Prompten genügend Kontext zu liefern, um sicherzustellen, dass die benötigten Antworten kommen.

- **Retrieval Augmented Generation, RAG**. Ihre Daten könnten beispielsweise in einer Datenbank oder einem Web-Endpunkt existieren, um sicherzustellen, dass diese Daten oder ein Teil davon zum Zeitpunkt des Promptings einbezogen werden, können Sie die relevanten Daten abrufen und in den Prompt des Nutzers integrieren.

- **Fein abgestimmtes Modell**. Hier wird das Modell weiter auf eigenen Daten trainiert, was zu präziseren und respondenteren Antworten führt, aber kostspielig sein kann.

![LLMs deployment](../../../translated_images/de/Deploy.18b2d27412ec8c02.webp)

Bildquelle: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt-Engineering mit Kontext

Vortrainierte LLMs funktionieren sehr gut bei allgemeinen Aufgaben in natürlicher Sprache, selbst wenn sie mit einem kurzen Prompt aufgerufen werden, wie einem Satz, der vervollständigt werden soll, oder einer Frage – dem sogenannten „Zero-Shot“-Lernen.

Je mehr der Nutzer jedoch seine Anfrage mit einer detaillierten Aufforderung und Beispielen – dem Kontext – eingrenzt, desto genauer und näher an den Erwartungen des Nutzers ist die Antwort. In diesem Fall sprechen wir von „One-Shot“-Lernen, wenn der Prompt nur ein Beispiel enthält, und „Few-Shot“-Lernen, wenn er mehrere Beispiele enthält.
Prompt-Engineering mit Kontext ist der kosteneffektivste Ansatz zum Einstieg.

### Retrieval Augmented Generation (RAG)

LLMs haben die Einschränkung, dass sie nur die während ihres Trainings verwendeten Daten zur Generierung einer Antwort nutzen können. Das bedeutet, dass sie nichts über Fakten wissen, die nach ihrem Trainingsprozess passiert sind, und keinen Zugriff auf nicht-öffentliche Informationen (wie Firmendaten) haben.
Dies kann durch RAG überwunden werden, eine Technik, die den Prompt mit externen Daten in Form von Dokumentabschnitten anreichert, wobei die Begrenzungen der Prompt-Länge berücksichtigt werden. Dies wird von Vektordatenbank-Tools (wie [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) unterstützt, die nützliche Abschnitte aus verschiedenen vordefinierten Datenquellen abrufen und dem Prompt-Kontext hinzufügen.

Diese Technik ist sehr hilfreich, wenn ein Unternehmen nicht über genügend Daten, Zeit oder Ressourcen verfügt, um ein LLM fein abzustimmen, aber dennoch die Leistung in einem spezifischen Arbeitsaufwand verbessern und Risiken von halluzinierten, veralteten oder nicht unterstützten Antworten reduzieren möchte.

### Fein abgestimmtes Modell

Feinabstimmung ist ein Prozess, der Transferlernen nutzt, um das Modell an eine nachgelagerte Aufgabe anzupassen oder ein spezifisches Problem zu lösen. Anders als Few-Shot-Lernen und RAG führt das zu einem neuen Modell mit aktualisierten Gewichten und Biases. Es benötigt einen Satz von Trainingsbeispielen, bestehend aus einem Eingabe-Prompt und der zugehörigen Ausgabe (Completion).
Dies wäre der bevorzugte Ansatz, wenn:

- **Verwendung kleinerer, aufgaben-spezifischer Modelle**. Ein Unternehmen möchte lieber ein kleineres Modell für eine enge Aufgabe fein abstimmen, anstatt wiederholt ein größeres Frontier-Modell zu prompten, was eine kostengünstigere und schnellere Lösung ergibt.

- **Latenz berücksichtigen**. Latenz ist für einen spezifischen Anwendungsfall wichtig, deshalb ist es nicht möglich, sehr lange Prompts oder eine Anzahl von Beispielen zu verwenden, die das Prompt-Längenlimit überschreiten.

- **Stabiles Verhalten anpassen**. Ein Unternehmen hat viele hochwertige Beispiele und möchte, dass das Modell konstant einem Aufgabenmuster, Ausgabeformat, Tonfall oder domänenspezifischem Stil folgt. Wenn das Hauptproblem aktuelle Fakten oder private Kenntnisse sind, die sich häufig ändern, verwenden Sie RAG anstelle einer alleinigen Feinabstimmung.

### Trainiertes Modell

Ein LLM von Grund auf zu trainieren ist zweifellos der schwierigste und komplexeste Ansatz, der enorme Datenmengen, qualifizierte Ressourcen und entsprechende Rechenleistung erfordert. Diese Option sollte nur in Betracht gezogen werden, wenn ein Unternehmen einen domänenspezifischen Anwendungsfall und eine große Menge domänenzentrierter Daten hat.

## Wissensüberprüfung

Welcher Ansatz könnte geeignet sein, um die Ergebnisse eines LLM zu verbessern?

1. Prompt-Engineering mit Kontext
1. RAG
1. Fein abgestimmtes Modell

A: Alle drei können helfen. Beginnen Sie mit Prompt-Engineering und Kontext für schnelle Verbesserungen und nutzen Sie RAG, wenn das Modell aktuelle Fakten oder private Geschäftsdaten benötigt. Wählen Sie die Feinabstimmung, wenn Sie genügend hochwertige Beispiele haben und das Modell konstant einer Aufgabe, einem Format, einem Tonfall oder einem Domänenmuster folgen soll.

## 🚀 Herausforderung

Lesen Sie mehr darüber, wie Sie [RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) für Ihr Unternehmen nutzen können.

## Gute Arbeit, setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning Kollektion](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie weiter zu Lektion 3, in der wir uns ansehen, wie man [verantwortungsvoll mit Generative AI baut](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->