<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2f686f2eb794941761252ac5e8e090b",
  "translation_date": "2025-06-25T10:14:48+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "de"
}
-->
# Erkundung und Vergleich verschiedener LLMs

[![Erkundung und Vergleich verschiedener LLMs](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.de.png)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Klicken Sie auf das obige Bild, um das Video dieser Lektion anzusehen_

In der vorherigen Lektion haben wir gesehen, wie Generative KI die Technologielandschaft verändert, wie große Sprachmodelle (LLMs) funktionieren und wie ein Unternehmen - wie unser Startup - sie auf seine Anwendungsfälle anwenden und wachsen kann! In diesem Kapitel wollen wir verschiedene Arten von großen Sprachmodellen (LLMs) vergleichen und gegenüberstellen, um ihre Vor- und Nachteile zu verstehen.

Der nächste Schritt in der Reise unseres Startups besteht darin, die aktuelle Landschaft der LLMs zu erkunden und zu verstehen, welche für unseren Anwendungsfall geeignet sind.

## Einführung

Diese Lektion behandelt:

- Verschiedene Arten von LLMs in der aktuellen Landschaft.
- Testen, Iterieren und Vergleichen verschiedener Modelle für Ihren Anwendungsfall in Azure.
- Wie man ein LLM bereitstellt.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- Das richtige Modell für Ihren Anwendungsfall auszuwählen.
- Zu verstehen, wie Sie die Leistung Ihres Modells testen, iterieren und verbessern können.
- Zu wissen, wie Unternehmen Modelle bereitstellen.

## Verschiedene Arten von LLMs verstehen

LLMs können basierend auf ihrer Architektur, ihren Trainingsdaten und ihrem Anwendungsfall mehrere Kategorisierungen haben. Das Verständnis dieser Unterschiede wird unserem Startup helfen, das richtige Modell für das Szenario auszuwählen und zu verstehen, wie man Leistung testet, iteriert und verbessert.

Es gibt viele verschiedene Arten von LLM-Modellen, Ihre Wahl des Modells hängt davon ab, wofür Sie sie verwenden möchten, Ihre Daten, wie viel Sie bereit sind zu zahlen und mehr.

Je nachdem, ob Sie die Modelle für Text-, Audio-, Video-, Bilderzeugung und so weiter verwenden möchten, könnten Sie sich für einen anderen Modelltyp entscheiden.

- **Audio- und Spracherkennung**. Für diesen Zweck sind Whisper-Modelle eine ausgezeichnete Wahl, da sie allgemeine Zwecke erfüllen und auf Spracherkennung ausgerichtet sind. Sie sind auf vielfältige Audiodaten trainiert und können mehrsprachige Spracherkennung durchführen. Erfahren Sie mehr über [Whisper-Modelle hier](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Bilderzeugung**. Für die Bilderzeugung sind DALL-E und Midjourney zwei sehr bekannte Optionen. DALL-E wird von Azure OpenAI angeboten. [Lesen Sie mehr über DALL-E hier](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) und auch in Kapitel 9 dieses Lehrplans.

- **Texterzeugung**. Die meisten Modelle sind auf Texterzeugung trainiert und Sie haben eine große Auswahl von GPT-3.5 bis GPT-4. Sie kommen zu unterschiedlichen Kosten, wobei GPT-4 das teuerste ist. Es lohnt sich, einen Blick in den [Azure OpenAI Playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) zu werfen, um zu beurteilen, welche Modelle am besten zu Ihren Bedürfnissen in Bezug auf Fähigkeiten und Kosten passen.

- **Multi-Modality**. Wenn Sie mehrere Arten von Daten in Eingabe und Ausgabe verarbeiten möchten, könnten Sie Modelle wie [gpt-4 turbo mit Vision oder gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - die neuesten Veröffentlichungen von OpenAI-Modellen - in Betracht ziehen, die in der Lage sind, natürliche Sprachverarbeitung mit visueller Verständigung zu kombinieren und Interaktionen durch multimodale Schnittstellen zu ermöglichen.

Die Auswahl eines Modells bedeutet, dass Sie einige grundlegende Fähigkeiten erhalten, die jedoch möglicherweise nicht ausreichen. Oft haben Sie unternehmensspezifische Daten, die Sie dem LLM irgendwie mitteilen müssen. Es gibt einige verschiedene Möglichkeiten, wie man dies angehen kann, mehr dazu in den kommenden Abschnitten.

### Foundation Models versus LLMs

Der Begriff Foundation Model wurde von [Stanford-Forschern geprägt](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) und definiert als ein KI-Modell, das einige Kriterien erfüllt, wie zum Beispiel:

- **Sie werden mit unüberwachtem Lernen oder selbstüberwachtem Lernen trainiert**, was bedeutet, dass sie auf unbeschrifteten multimodalen Daten trainiert werden und keine menschliche Annotation oder Beschriftung der Daten für ihren Trainingsprozess benötigen.
- **Es sind sehr große Modelle**, basierend auf sehr tiefen neuronalen Netzwerken, die auf Milliarden von Parametern trainiert werden.
- **Sie sollen normalerweise als „Foundation“ für andere Modelle dienen**, was bedeutet, dass sie als Ausgangspunkt für andere Modelle verwendet werden können, die darauf aufgebaut werden, was durch Feinabstimmung erfolgen kann.

![Foundation Models versus LLMs](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.de.png)

Bildquelle: [Essential Guide to Foundation Models and Large Language Models | von Babar M Bhatti | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Um diese Unterscheidung weiter zu klären, nehmen wir ChatGPT als Beispiel. Um die erste Version von ChatGPT zu erstellen, diente ein Modell namens GPT-3.5 als Foundation Model. Das bedeutet, dass OpenAI einige chat-spezifische Daten verwendet hat, um eine abgestimmte Version von GPT-3.5 zu erstellen, die darauf spezialisiert ist, in Konversationsszenarien wie Chatbots gut zu funktionieren.

![Foundation Model](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.de.png)

Bildquelle: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open Source versus Proprietäre Modelle

Eine weitere Möglichkeit, LLMs zu kategorisieren, besteht darin, ob sie Open Source oder proprietär sind.

Open-Source-Modelle sind Modelle, die der Öffentlichkeit zugänglich gemacht werden und von jedem genutzt werden können. Sie werden oft von dem Unternehmen, das sie erstellt hat, oder von der Forschungsgemeinschaft zur Verfügung gestellt. Diese Modelle dürfen inspiziert, modifiziert und für die verschiedenen Anwendungsfälle in LLMs angepasst werden. Sie sind jedoch nicht immer für den Produktionseinsatz optimiert und möglicherweise nicht so leistungsfähig wie proprietäre Modelle. Außerdem kann die Finanzierung von Open-Source-Modellen begrenzt sein, und sie werden möglicherweise nicht langfristig gewartet oder mit den neuesten Forschungsergebnissen aktualisiert. Beispiele für beliebte Open-Source-Modelle sind [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) und [LLaMA](https://llama.meta.com).

Proprietäre Modelle sind Modelle, die einem Unternehmen gehören und nicht der Öffentlichkeit zugänglich gemacht werden. Diese Modelle sind oft für den Produktionseinsatz optimiert. Sie dürfen jedoch nicht inspiziert, modifiziert oder für verschiedene Anwendungsfälle angepasst werden. Außerdem sind sie nicht immer kostenlos verfügbar und erfordern möglicherweise ein Abonnement oder eine Zahlung, um verwendet zu werden. Auch haben die Benutzer keine Kontrolle über die Daten, die zum Trainieren des Modells verwendet werden, was bedeutet, dass sie dem Modelleigentümer vertrauen sollten, dass er sich für den Datenschutz und die verantwortungsvolle Nutzung von KI einsetzt. Beispiele für beliebte proprietäre Modelle sind [OpenAI-Modelle](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) oder [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus Bilderzeugung versus Text- und Codeerzeugung

LLMs können auch nach dem von ihnen erzeugten Output kategorisiert werden.

Embeddings sind eine Reihe von Modellen, die Text in eine numerische Form, das sogenannte Embedding, umwandeln können, das eine numerische Darstellung des Eingangstextes ist. Embeddings erleichtern es Maschinen, die Beziehungen zwischen Wörtern oder Sätzen zu verstehen und können als Eingaben von anderen Modellen verwendet werden, wie Klassifikationsmodellen oder Clustermodellen, die eine bessere Leistung bei numerischen Daten haben. Embedding-Modelle werden oft für Transfer-Learning verwendet, bei dem ein Modell für eine Ersatzaufgabe gebaut wird, für die es eine Fülle von Daten gibt, und dann die Modellgewichte (Embeddings) für andere nachgelagerte Aufgaben wiederverwendet werden. Ein Beispiel für diese Kategorie ist [OpenAI Embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.de.png)

Bilderzeugungsmodelle sind Modelle, die Bilder erzeugen. Diese Modelle werden oft für die Bildbearbeitung, Bildsynthese und Bildübersetzung verwendet. Bilderzeugungsmodelle werden oft auf großen Datensätzen von Bildern trainiert, wie [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), und können verwendet werden, um neue Bilder zu erzeugen oder bestehende Bilder mit Inpainting-, Super-Resolution- und Colorization-Techniken zu bearbeiten. Beispiele sind [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) und [Stable Diffusion Modelle](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Bilderzeugung](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.de.png)

Text- und Codeerzeugungsmodelle sind Modelle, die Text oder Code erzeugen. Diese Modelle werden oft für Textzusammenfassung, Übersetzung und Fragebeantwortung verwendet. Texterzeugungsmodelle werden oft auf großen Datensätzen von Text trainiert, wie [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), und können verwendet werden, um neuen Text zu erzeugen oder Fragen zu beantworten. Codeerzeugungsmodelle, wie [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), werden oft auf großen Datensätzen von Code, wie GitHub, trainiert und können verwendet werden, um neuen Code zu erzeugen oder Fehler im bestehenden Code zu beheben.

![Text- und Codeerzeugung](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.de.png)

### Encoder-Decoder versus Decoder-only

Um über die verschiedenen Arten von Architekturen von LLMs zu sprechen, verwenden wir eine Analogie.

Stellen Sie sich vor, Ihr Manager hat Ihnen die Aufgabe gegeben, ein Quiz für die Studenten zu schreiben. Sie haben zwei Kollegen; einer ist für die Erstellung des Inhalts verantwortlich und der andere für die Überprüfung.

Der Inhaltsersteller ist wie ein Decoder-only-Modell, er kann sich das Thema ansehen und sehen, was Sie bereits geschrieben haben, und dann kann er einen Kurs darauf basierend schreiben. Sie sind sehr gut darin, ansprechende und informative Inhalte zu schreiben, aber sie sind nicht sehr gut darin, das Thema und die Lernziele zu verstehen. Einige Beispiele für Decoder-Modelle sind die GPT-Familienmodelle, wie GPT-3.

Der Prüfer ist wie ein Encoder-only-Modell, sie schauen sich den geschriebenen Kurs und die Antworten an, bemerken die Beziehung zwischen ihnen und verstehen den Kontext, aber sie sind nicht gut darin, Inhalte zu generieren. Ein Beispiel für ein Encoder-only-Modell wäre BERT.

Stellen Sie sich vor, wir könnten auch jemanden haben, der das Quiz erstellen und überprüfen könnte, das ist ein Encoder-Decoder-Modell. Einige Beispiele wären BART und T5.

### Service versus Modell

Nun sprechen wir über den Unterschied zwischen einem Service und einem Modell. Ein Service ist ein Produkt, das von einem Cloud-Dienstanbieter angeboten wird und oft eine Kombination aus Modellen, Daten und anderen Komponenten ist. Ein Modell ist die Kernkomponente eines Service und ist oft ein Foundation Model, wie ein LLM.

Services sind oft für den Produktionseinsatz optimiert und sind oft einfacher zu verwenden als Modelle, über eine grafische Benutzeroberfläche. Services sind jedoch nicht immer kostenlos verfügbar und erfordern möglicherweise ein Abonnement oder eine Zahlung, um verwendet zu werden, im Austausch für die Nutzung der Ausrüstung und Ressourcen des Serviceanbieters, Optimierung der Ausgaben und einfache Skalierung. Ein Beispiel für einen Service ist [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), das einen Pay-as-you-go-Tarifplan bietet, was bedeutet, dass Benutzer proportional zu ihrer Nutzung des Service belastet werden. Außerdem bietet Azure OpenAI Service Sicherheit auf Unternehmensniveau und einen verantwortungsvollen KI-Rahmen auf den Fähigkeiten der Modelle.

Modelle sind nur das neuronale Netzwerk, mit den Parametern, Gewichten und anderen. Dies ermöglicht es Unternehmen, lokal zu arbeiten, erfordert jedoch den Kauf von Ausrüstung, den Aufbau einer Struktur zur Skalierung und den Kauf einer Lizenz oder die Nutzung eines Open-Source-Modells. Ein Modell wie LLaMA ist verfügbar zur Nutzung, erfordert jedoch Rechenleistung, um das Modell auszuführen.

## Wie man mit verschiedenen Modellen testet und iteriert, um die Leistung auf Azure zu verstehen

Sobald unser Team die aktuelle LLMs-Landschaft erkundet und einige gute Kandidaten für ihre Szenarien identifiziert hat, besteht der nächste Schritt darin, sie auf ihren Daten und ihrer Arbeitslast zu testen. Dies ist ein iterativer Prozess, der durch Experimente und Messungen durchgeführt wird. Die meisten der Modelle, die wir in den vorherigen Absätzen erwähnt haben (OpenAI-Modelle, Open-Source-Modelle wie Llama2 und Hugging Face-Transformers) sind im [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) in [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) verfügbar.

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) ist eine Cloud-Plattform, die für Entwickler entwickelt wurde, um generative KI-Anwendungen zu erstellen und den gesamten Entwicklungslebenszyklus zu verwalten - von Experimenten bis zur Bewertung - indem alle Azure AI-Dienste in einem einzigen Hub mit einer praktischen GUI kombiniert werden. Der Model Catalog in Azure AI Studio ermöglicht es dem Benutzer:

- Das Foundation Model von Interesse im Katalog zu finden - entweder proprietär oder Open Source, gefiltert nach Aufgabe, Lizenz oder Name. Um die Suchbarkeit zu verbessern, sind die Modelle in Sammlungen organisiert, wie Azure OpenAI-Sammlung, Hugging Face-Sammlung und mehr.

![Model catalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.de.png)

- Die Modellkarte zu überprüfen, einschließlich einer detaillierten Beschreibung der beabsichtigten Nutzung und Trainingsdaten, Codebeispiele und Bewertungsergebnisse in der internen Bewertungslibrary.

![Model card](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.de.png)
- Vergleichen Sie Benchmarks über Modelle und Datensätze, die in der Branche verfügbar sind, um zu beurteilen, welches Szenario den geschäftlichen Anforderungen entspricht, über das [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) Fenster.

![Model Benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.de.png)

- Feinabstimmung des Modells auf benutzerdefinierte Trainingsdaten, um die Modellleistung in einer bestimmten Arbeitslast zu verbessern, unter Nutzung der Experimentier- und Tracking-Fähigkeiten von Azure AI Studio.

![Model Fine-Tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.de.png)

- Bereitstellung des ursprünglichen vortrainierten Modells oder der feinabgestimmten Version für eine Remote-Echtzeit-Inferenz – verwaltetes Rechnen – oder serverlosen API-Endpunkt – [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) – um Anwendungen zu ermöglichen, es zu nutzen.

![Model Deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.de.png)

> [!NOTE]
> Nicht alle Modelle im Katalog sind derzeit für Feinabstimmung und/oder Pay-as-you-go-Bereitstellung verfügbar. Überprüfen Sie die Modellkarte für Details zu den Fähigkeiten und Einschränkungen des Modells.

## Verbesserung der LLM-Ergebnisse

Wir haben mit unserem Startup-Team verschiedene Arten von LLMs und eine Cloud-Plattform (Azure Machine Learning) untersucht, die es uns ermöglicht, verschiedene Modelle zu vergleichen, sie auf Testdaten zu bewerten, die Leistung zu verbessern und sie auf Inferenzendpunkten bereitzustellen.

Aber wann sollten sie eine Feinabstimmung eines Modells in Betracht ziehen, anstatt ein vortrainiertes zu verwenden? Gibt es andere Ansätze, um die Modellleistung in spezifischen Arbeitslasten zu verbessern?

Es gibt mehrere Ansätze, die ein Unternehmen nutzen kann, um die gewünschten Ergebnisse von einem LLM zu erzielen. Sie können verschiedene Arten von Modellen mit unterschiedlichen Trainingsgraden auswählen, wenn Sie ein LLM in der Produktion bereitstellen, mit unterschiedlichen Komplexitäts-, Kosten- und Qualitätsstufen. Hier sind einige verschiedene Ansätze:

- **Prompt-Engineering mit Kontext**. Die Idee ist, beim Prompten genügend Kontext bereitzustellen, um sicherzustellen, dass Sie die gewünschten Antworten erhalten.

- **Retrieval Augmented Generation, RAG**. Ihre Daten könnten beispielsweise in einer Datenbank oder einem Web-Endpunkt existieren. Um sicherzustellen, dass diese Daten oder ein Teil davon zum Zeitpunkt des Promptings einbezogen werden, können Sie die relevanten Daten abrufen und in den Benutzer-Prompt integrieren.

- **Feinabgestimmtes Modell**. Hier haben Sie das Modell weiter auf Ihren eigenen Daten trainiert, was dazu führt, dass das Modell genauer und an Ihre Bedürfnisse angepasst ist, aber möglicherweise kostspielig ist.

![LLMs Deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.de.png)

Bildquelle: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt-Engineering mit Kontext

Vortrainierte LLMs funktionieren sehr gut bei allgemeinen Aufgaben der natürlichen Sprachverarbeitung, sogar wenn sie mit einem kurzen Prompt aufgerufen werden, wie einem Satz zum Vervollständigen oder einer Frage – das sogenannte „Zero-Shot“-Lernen.

Je mehr der Benutzer seine Anfrage mit einer detaillierten Anfrage und Beispielen – dem Kontext – formulieren kann, desto genauer und näher an den Erwartungen des Benutzers wird die Antwort sein. In diesem Fall sprechen wir von „One-Shot“-Lernen, wenn der Prompt nur ein Beispiel enthält, und „Few-Shot-Lernen“, wenn er mehrere Beispiele enthält. Prompt-Engineering mit Kontext ist der kosteneffektivste Ansatz für den Einstieg.

### Retrieval Augmented Generation (RAG)

LLMs haben die Einschränkung, dass sie nur die Daten verwenden können, die während ihres Trainings verwendet wurden, um eine Antwort zu generieren. Das bedeutet, dass sie nichts über die Fakten wissen, die nach ihrem Trainingsprozess passiert sind, und sie können nicht auf nicht-öffentliche Informationen zugreifen (wie Unternehmensdaten).
Dies kann durch RAG überwunden werden, eine Technik, die den Prompt mit externen Daten in Form von Dokumentenfragmenten ergänzt, unter Berücksichtigung der Prompt-Längenbeschränkungen. Dies wird von Vektordatenbank-Tools (wie [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) unterstützt, die die nützlichen Fragmente aus verschiedenen vordefinierten Datenquellen abrufen und dem Prompt-Kontext hinzufügen.

Diese Technik ist sehr hilfreich, wenn ein Unternehmen nicht genügend Daten, Zeit oder Ressourcen hat, um ein LLM fein abzustimmen, aber dennoch die Leistung bei einer spezifischen Arbeitslast verbessern und das Risiko von Erfindungen, d.h. Verfälschungen der Realität oder schädlichen Inhalten, reduzieren möchte.

### Feinabgestimmtes Modell

Feinabstimmung ist ein Prozess, der Transferlernen nutzt, um das Modell an eine nachgelagerte Aufgabe anzupassen oder ein spezifisches Problem zu lösen. Anders als Few-Shot-Lernen und RAG führt es zur Erzeugung eines neuen Modells mit aktualisierten Gewichten und Biases. Es erfordert eine Reihe von Trainingsbeispielen, die aus einem einzelnen Eingabeprompt und dessen zugehörigem Output (der Vervollständigung) bestehen.
Dies wäre der bevorzugte Ansatz, wenn:

- **Verwendung feinabgestimmter Modelle**. Ein Unternehmen möchte weniger leistungsfähige feinabgestimmte Modelle (wie Einbettungsmodelle) anstelle von Hochleistungsmodellen verwenden, was zu einer kostengünstigeren und schnelleren Lösung führt.

- **Berücksichtigung von Latenz**. Latenz ist wichtig für einen spezifischen Anwendungsfall, sodass es nicht möglich ist, sehr lange Prompts zu verwenden oder die Anzahl der Beispiele, aus denen das Modell lernen soll, passt nicht zu den Prompt-Längenbeschränkungen.

- **Aktualität wahren**. Ein Unternehmen hat viele qualitativ hochwertige Daten und Ground-Truth-Labels und die Ressourcen, um diese Daten im Laufe der Zeit aktuell zu halten.

### Trainiertes Modell

Das Training eines LLM von Grund auf ist zweifellos der schwierigste und komplexeste Ansatz, der massive Datenmengen, qualifizierte Ressourcen und angemessene Rechenleistung erfordert. Diese Option sollte nur in einem Szenario in Betracht gezogen werden, in dem ein Unternehmen einen domänenspezifischen Anwendungsfall und eine große Menge domänenzentrierter Daten hat.

## Wissensüberprüfung

Was könnte ein guter Ansatz sein, um die Ergebnisse der LLM-Vervollständigung zu verbessern?

1. Prompt-Engineering mit Kontext
1. RAG
1. Feinabgestimmtes Modell

A:3, wenn Sie die Zeit und Ressourcen sowie qualitativ hochwertige Daten haben, ist die Feinabstimmung die bessere Option, um aktuell zu bleiben. Wenn Sie jedoch Verbesserungen anstreben und Ihnen die Zeit fehlt, lohnt es sich, zuerst RAG in Betracht zu ziehen.

## 🚀 Herausforderung

Lesen Sie mehr darüber, wie Sie [RAG verwenden](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) für Ihr Unternehmen.

## Großartige Arbeit, setzen Sie Ihr Lernen fort

Nachdem Sie diese Lektion abgeschlossen haben, sehen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 3, in der wir uns damit befassen, wie man [verantwortungsvoll mit generativer KI arbeitet](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle angesehen werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.