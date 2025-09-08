<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:10:12+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "de"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.de.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Einführung

Die Welt der Open-Source-LLMs ist spannend und entwickelt sich ständig weiter. Diese Lektion soll einen tiefen Einblick in Open-Source-Modelle geben. Wenn Sie Informationen darüber suchen, wie proprietäre Modelle im Vergleich zu Open-Source-Modellen abschneiden, besuchen Sie die Lektion ["Untersuchung und Vergleich verschiedener LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Diese Lektion behandelt auch das Thema Fine-Tuning, aber eine detailliertere Erklärung finden Sie in der Lektion ["Fine-Tuning von LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Lernziele

- Ein Verständnis für Open-Source-Modelle gewinnen
- Die Vorteile der Arbeit mit Open-Source-Modellen verstehen
- Die verfügbaren Open-Source-Modelle auf Hugging Face und im Azure AI Studio erkunden

## Was sind Open-Source-Modelle?

Open-Source-Software hat eine entscheidende Rolle im Wachstum der Technologie in verschiedenen Bereichen gespielt. Die Open Source Initiative (OSI) hat [10 Kriterien für Software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) definiert, um als Open Source klassifiziert zu werden. Der Quellcode muss unter einer von der OSI genehmigten Lizenz offen geteilt werden.

Obwohl die Entwicklung von LLMs ähnliche Elemente wie die Softwareentwicklung aufweist, ist der Prozess nicht genau derselbe. Dies hat in der Community zu vielen Diskussionen über die Definition von Open Source im Kontext von LLMs geführt. Damit ein Modell der traditionellen Definition von Open Source entspricht, sollten folgende Informationen öffentlich zugänglich sein:

- Datensätze, die zur Modellschulung verwendet wurden.
- Vollständige Modellgewichte als Teil des Trainings.
- Der Evaluierungscode.
- Der Fine-Tuning-Code.
- Vollständige Modellgewichte und Trainingsmetriken.

Derzeit gibt es nur wenige Modelle, die diese Kriterien erfüllen. Das [OLMo-Modell, erstellt vom Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), gehört zu dieser Kategorie.

Für diese Lektion werden wir die Modelle im Folgenden als "Open Models" bezeichnen, da sie möglicherweise zum Zeitpunkt des Schreibens nicht den oben genannten Kriterien entsprechen.

## Vorteile von Open Models

**Hochgradig anpassbar** – Da Open Models mit detaillierten Trainingsinformationen veröffentlicht werden, können Forscher und Entwickler die internen Strukturen des Modells modifizieren. Dies ermöglicht die Erstellung hochspezialisierter Modelle, die für eine bestimmte Aufgabe oder ein bestimmtes Studiengebiet optimiert sind. Beispiele hierfür sind Codegenerierung, mathematische Operationen und Biologie.

**Kosten** – Die Kosten pro Token für die Nutzung und Bereitstellung dieser Modelle sind niedriger als bei proprietären Modellen. Beim Aufbau von Generative-AI-Anwendungen sollte die Leistung im Vergleich zu den Kosten für den jeweiligen Anwendungsfall berücksichtigt werden.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.de.png)  
Quelle: Artificial Analysis

**Flexibilität** – Die Arbeit mit Open Models ermöglicht Flexibilität bei der Nutzung verschiedener Modelle oder deren Kombination. Ein Beispiel hierfür sind die [HuggingChat-Assistenten](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), bei denen der Benutzer direkt in der Benutzeroberfläche das verwendete Modell auswählen kann:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.de.png)

## Erkundung verschiedener Open Models

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), entwickelt von Meta, ist ein Open Model, das für chatbasierte Anwendungen optimiert ist. Dies liegt an seiner Fine-Tuning-Methode, die eine große Menge an Dialogen und menschlichem Feedback umfasst. Mit dieser Methode liefert das Modell Ergebnisse, die besser den menschlichen Erwartungen entsprechen und somit eine bessere Benutzererfahrung bieten.

Einige Beispiele für Fine-Tuning-Versionen von Llama sind [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), das sich auf Japanisch spezialisiert hat, und [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), eine erweiterte Version des Basismodells.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ist ein Open Model mit starkem Fokus auf hohe Leistung und Effizienz. Es verwendet den Mixture-of-Experts-Ansatz, bei dem eine Gruppe spezialisierter Expertenmodelle zu einem System kombiniert wird, in dem je nach Eingabe bestimmte Modelle ausgewählt werden. Dies macht die Berechnung effektiver, da Modelle nur die Eingaben bearbeiten, auf die sie spezialisiert sind.

Einige Beispiele für Fine-Tuning-Versionen von Mistral sind [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), das sich auf den medizinischen Bereich konzentriert, und [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), das mathematische Berechnungen durchführt.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ist ein LLM, das vom Technology Innovation Institute (**TII**) entwickelt wurde. Der Falcon-40B wurde mit 40 Milliarden Parametern trainiert, was gezeigt hat, dass er mit weniger Rechenaufwand besser als GPT-3 abschneidet. Dies liegt an der Verwendung des FlashAttention-Algorithmus und der Multiquery-Attention, die die Speicheranforderungen zur Inferenzzeit reduziert. Mit dieser verkürzten Inferenzzeit eignet sich der Falcon-40B für Chat-Anwendungen.

Einige Beispiele für Fine-Tuning-Versionen von Falcon sind [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), ein Assistent, der auf Open Models basiert, und [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), das eine höhere Leistung als das Basismodell bietet.

## Wie man auswählt

Es gibt keine allgemeingültige Antwort darauf, wie man ein Open Model auswählt. Ein guter Ausgangspunkt ist die Verwendung der Filterfunktion nach Aufgaben im Azure AI Studio. Dies hilft Ihnen zu verstehen, für welche Arten von Aufgaben das Modell trainiert wurde. Hugging Face führt auch ein LLM-Leaderboard, das die leistungsstärksten Modelle basierend auf bestimmten Metriken zeigt.

Wenn Sie LLMs über verschiedene Typen hinweg vergleichen möchten, ist [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) eine weitere großartige Ressource:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.de.png)  
Quelle: Artificial Analysis

Wenn Sie an einem spezifischen Anwendungsfall arbeiten, kann die Suche nach Fine-Tuning-Versionen, die sich auf denselben Bereich konzentrieren, effektiv sein. Das Experimentieren mit mehreren Open Models, um zu sehen, wie sie sich gemäß Ihren und den Erwartungen Ihrer Benutzer verhalten, ist ebenfalls eine gute Praxis.

## Nächste Schritte

Das Beste an Open Models ist, dass Sie schnell mit ihnen arbeiten können. Schauen Sie sich den [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) an, der eine spezielle Hugging Face-Sammlung mit den hier besprochenen Modellen enthält.

## Lernen hört hier nicht auf, setzen Sie Ihre Reise fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative AI weiter zu vertiefen!

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.