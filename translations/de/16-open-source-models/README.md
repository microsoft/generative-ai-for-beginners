<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T12:44:28+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "de"
}
-->
[![Open Source Models](../../../translated_images/de/16-lesson-banner.6b56555e8404fda1.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Einführung

Die Welt der Open-Source-LLMs ist spannend und entwickelt sich ständig weiter. Diese Lektion zielt darauf ab, einen tiefgehenden Einblick in Open-Source-Modelle zu geben. Wenn Sie Informationen darüber suchen, wie proprietäre Modelle im Vergleich zu Open-Source-Modellen abschneiden, gehen Sie zur ["Exploring and Comparing Different LLMs"-Lektion](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Diese Lektion behandelt auch das Thema Fine-Tuning, eine ausführlichere Erklärung finden Sie jedoch in der ["Fine-Tuning LLMs"-Lektion](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Lernziele

- Verständnis für Open-Source-Modelle gewinnen  
- Die Vorteile der Arbeit mit Open-Source-Modellen verstehen  
- Die auf Hugging Face und im Azure AI Studio verfügbaren Open-Modelle erkunden  

## Was sind Open-Source-Modelle?

Open-Source-Software hat eine entscheidende Rolle beim Wachstum der Technologie in verschiedenen Bereichen gespielt. Die Open Source Initiative (OSI) hat [10 Kriterien für Software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) definiert, um als Open Source klassifiziert zu werden. Der Quellcode muss unter einer von der OSI genehmigten Lizenz offen geteilt werden.

Obwohl die Entwicklung von LLMs ähnliche Elemente wie die Softwareentwicklung aufweist, ist der Prozess nicht genau derselbe. Dies hat in der Community zu vielen Diskussionen über die Definition von Open Source im Kontext von LLMs geführt. Damit ein Modell mit der traditionellen Definition von Open Source übereinstimmt, sollten folgende Informationen öffentlich verfügbar sein:

- Datensätze, die zum Trainieren des Modells verwendet wurden.  
- Vollständige Modellgewichte als Teil des Trainings.  
- Der Evaluierungscode.  
- Der Fine-Tuning-Code.  
- Vollständige Modellgewichte und Trainingsmetriken.  

Derzeit gibt es nur wenige Modelle, die diese Kriterien erfüllen. Das [OLMo-Modell, erstellt vom Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), ist eines, das in diese Kategorie passt.

Für diese Lektion werden wir die Modelle im Folgenden als "Open Models" bezeichnen, da sie zum Zeitpunkt des Schreibens möglicherweise nicht alle oben genannten Kriterien erfüllen.

## Vorteile von Open Models

**Hochgradig anpassbar** – Da Open Models mit detaillierten Trainingsinformationen veröffentlicht werden, können Forscher und Entwickler die internen Strukturen des Modells modifizieren. Dies ermöglicht die Erstellung hochspezialisierter Modelle, die für eine bestimmte Aufgabe oder ein bestimmtes Fachgebiet feinabgestimmt sind. Beispiele hierfür sind Codegenerierung, mathematische Operationen und Biologie.

**Kosten** – Die Kosten pro Token für die Nutzung und Bereitstellung dieser Modelle sind niedriger als bei proprietären Modellen. Beim Aufbau von Generative-AI-Anwendungen sollte man die Leistung im Verhältnis zum Preis bei der Arbeit mit diesen Modellen für den eigenen Anwendungsfall berücksichtigen.

![Model Cost](../../../translated_images/de/model-price.3f5a3e4d32ae00b4.png)  
Quelle: Artificial Analysis

**Flexibilität** – Die Arbeit mit Open Models ermöglicht Flexibilität bei der Verwendung verschiedener Modelle oder deren Kombination. Ein Beispiel hierfür sind die [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), bei denen ein Nutzer das verwendete Modell direkt in der Benutzeroberfläche auswählen kann:

![Choose Model](../../../translated_images/de/choose-model.f095d15bbac92214.png)

## Verschiedene Open Models erkunden

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), entwickelt von Meta, ist ein Open Model, das für chatbasierte Anwendungen optimiert ist. Dies liegt an seiner Fine-Tuning-Methode, die eine große Menge an Dialogen und menschlichem Feedback einbezog. Mit dieser Methode liefert das Modell Ergebnisse, die stärker an menschlichen Erwartungen ausgerichtet sind, was eine bessere Benutzererfahrung bietet.

Einige Beispiele für feinabgestimmte Versionen von Llama sind [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), das sich auf Japanisch spezialisiert hat, und [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), eine verbesserte Version des Basismodells.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ist ein Open Model mit starkem Fokus auf hohe Leistung und Effizienz. Es verwendet den Mixture-of-Experts-Ansatz, der eine Gruppe spezialisierter Expertenmodelle zu einem System kombiniert, bei dem je nach Eingabe bestimmte Modelle ausgewählt werden. Dies macht die Berechnung effektiver, da Modelle nur die Eingaben bearbeiten, auf die sie spezialisiert sind.

Einige Beispiele für feinabgestimmte Versionen von Mistral sind [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), das sich auf den medizinischen Bereich konzentriert, und [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), das mathematische Berechnungen durchführt.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ist ein LLM, das vom Technology Innovation Institute (**TII**) erstellt wurde. Der Falcon-40B wurde mit 40 Milliarden Parametern trainiert und hat gezeigt, dass er bei geringerem Rechenaufwand besser als GPT-3 abschneidet. Dies ist auf die Verwendung des FlashAttention-Algorithmus und der Multiquery-Attention zurückzuführen, die den Speicherbedarf zur Inferenzzeit reduzieren. Mit dieser verkürzten Inferenzzeit eignet sich der Falcon-40B für Chat-Anwendungen.

Einige Beispiele für feinabgestimmte Versionen von Falcon sind der [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), ein auf Open Models basierender Assistent, und [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), der eine höhere Leistung als das Basismodell bietet.

## Wie wählt man aus?

Es gibt keine eindeutige Antwort darauf, wie man ein Open Model auswählt. Ein guter Ausgangspunkt ist die Filterfunktion nach Aufgaben im Azure AI Studio. Dies hilft Ihnen zu verstehen, für welche Arten von Aufgaben das Modell trainiert wurde. Hugging Face pflegt außerdem ein LLM-Leaderboard, das die besten Modelle basierend auf bestimmten Metriken zeigt.

Wenn Sie LLMs verschiedener Typen vergleichen möchten, ist [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) eine weitere großartige Ressource:

![Model Quality](../../../translated_images/de/model-quality.aaae1c22e00f7ee1.png)  
Quelle: Artificial Analysis

Wenn Sie an einem spezifischen Anwendungsfall arbeiten, kann die Suche nach feinabgestimmten Versionen, die sich auf denselben Bereich konzentrieren, effektiv sein. Das Experimentieren mit mehreren Open Models, um zu sehen, wie sie Ihren und den Erwartungen Ihrer Nutzer entsprechen, ist ebenfalls eine gute Praxis.

## Nächste Schritte

Das Beste an Open Models ist, dass Sie ziemlich schnell mit der Arbeit beginnen können. Schauen Sie sich den [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) an, der eine spezielle Hugging Face-Sammlung mit den hier besprochenen Modellen enthält.

## Lernen hört hier nicht auf, setzen Sie die Reise fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative AI weiter zu vertiefen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->