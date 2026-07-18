# Einführung in kleine Sprachmodelle für generative KI für Anfänger
Generative KI ist ein faszinierendes Gebiet der künstlichen Intelligenz, das sich darauf konzentriert, Systeme zu schaffen, die in der Lage sind, neue Inhalte zu generieren. Diese Inhalte können von Text und Bildern bis hin zu Musik und sogar ganzen virtuellen Umgebungen reichen. Eine der spannendsten Anwendungen generativer KI liegt im Bereich der Sprachmodelle.

## Was sind kleine Sprachmodelle?

Ein kleines Sprachmodell (SLM) stellt eine verkleinerte Variante eines großen Sprachmodells (LLM) dar, das viele der architektonischen Prinzipien und Techniken von LLMs nutzt, während es einen deutlich reduzierten Rechenaufwand aufweist. 

SLMs sind eine Untergruppe von Sprachmodellen, die darauf ausgelegt sind, menschenähnlichen Text zu generieren. Im Gegensatz zu ihren größeren Pendants wie GPT-4 sind SLMs kompakter und effizienter, was sie ideal für Anwendungen macht, bei denen die Rechenressourcen begrenzt sind. Trotz ihrer kleineren Größe können sie dennoch eine Vielzahl von Aufgaben ausführen. Üblicherweise werden SLMs durch Komprimierung oder Destillierung von LLMs erstellt, wobei angestrebt wird, einen beträchtlichen Teil der ursprünglichen Funktionalität und sprachlichen Fähigkeiten des Modells zu bewahren. Diese Verringerung der Modellgröße verringert die Gesamtkonplexität und macht SLMs sowohl hinsichtlich Speicherverbrauch als auch rechnerischer Anforderungen effizienter. Trotz dieser Optimierungen können SLMs immer noch eine breite Palette von Aufgaben der natürlichen Sprachverarbeitung (NLP) ausführen:

- Textgenerierung: Erstellung kohärenter und kontextuell relevanter Sätze oder Absätze.
- Textvervollständigung: Vorhersage und Ergänzung von Sätzen basierend auf einem gegebenen Eingabestichwort.
- Übersetzung: Umwandlung von Text von einer Sprache in eine andere.
- Zusammenfassung: Verdichtung langer Textabschnitte in kürzere, besser verdauliche Zusammenfassungen.

Wenn auch mit einigen Kompromissen bei der Leistung oder Tiefe des Verständnisses im Vergleich zu ihren größeren Pendants. 

## Wie funktionieren kleine Sprachmodelle?
SLMs werden auf großen Mengen von Textdaten trainiert. Während des Trainings lernen sie die Muster und Strukturen der Sprache, sodass sie Text generieren können, der sowohl grammatikalisch korrekt als auch kontextuell passend ist. Der Trainingsprozess umfasst:

- Datensammlung: Zusammenstellung großer Textdatensätze aus verschiedenen Quellen.
- Vorverarbeitung: Säuberung und Organisation der Daten, um sie für das Training geeignet zu machen.
- Training: Einsatz von maschinellen Lernalgorithmen, um das Modell darin zu schulen, Text zu verstehen und zu generieren.
- Feinabstimmung: Anpassung des Modells zur Verbesserung seiner Leistung bei spezifischen Aufgaben.

Die Entwicklung von SLMs steht im Einklang mit dem zunehmenden Bedarf an Modellen, die in ressourcenbeschränkten Umgebungen wie mobilen Geräten oder Edge-Computing-Plattformen eingesetzt werden können, wo vollwertige LLMs aufgrund ihres hohen Ressourceneinsatzes unpraktisch sind. Durch den Fokus auf Effizienz balancieren SLMs Leistung und Zugänglichkeit aus und ermöglichen so einen breiteren Einsatz in verschiedenen Anwendungsbereichen.

![slm](../../../translated_images/de/slm.4058842744d0444a.webp)

## Lernziele

In dieser Lektion möchten wir das Wissen über SLM vorstellen und es mit Microsoft Phi-3 kombinieren, um verschiedene Szenarien im Textinhalt, in der Vision und im MoE zu erlernen.

Am Ende dieser Lektion sollten Sie in der Lage sein, die folgenden Fragen zu beantworten:

- Was ist SLM?
- Was ist der Unterschied zwischen SLM und LLM?
- Was ist die Microsoft Phi-3/3.5-Familie?
- Wie führt man Inferenz mit der Microsoft Phi-3/3.5-Familie durch?

Bereit? Dann legen wir los.

## Die Unterschiede zwischen großen Sprachmodellen (LLMs) und kleinen Sprachmodellen (SLMs)

Sowohl LLMs als auch SLMs basieren auf grundlegenden Prinzipien des probabilistischen maschinellen Lernens und folgen ähnlichen Ansätzen in ihrem architektonischen Design, in Trainingsmethoden, Datenproduktionsprozessen und Modellbewertungsansätzen. Dennoch gibt es mehrere Schlüsselfaktoren, die diese beiden Modelltypen unterscheiden.

## Anwendungen kleiner Sprachmodelle

SLMs finden in vielen Bereichen Anwendung, darunter:

- Chatbots: Bereitstellung von Kundensupport und Interaktion mit Nutzern in gesprächsähnlicher Weise.
- Inhaltserstellung: Unterstützung von Autoren durch Generierung von Ideen oder sogar Entwurf ganzer Artikel.
- Bildung: Hilfe für Schüler bei Schreibaufgaben oder beim Erlernen neuer Sprachen.
- Barrierefreiheit: Erstellung von Werkzeugen für Menschen mit Behinderungen, wie z. B. Text-zu-Sprache-Systeme.

**Größe**
  
Ein wesentlicher Unterschied zwischen LLMs und SLMs liegt in der Modellgröße. LLMs, wie ChatGPT (GPT-4), können schätzungsweise 1,76 Billionen Parameter umfassen, während Open-Source-SLMs wie Mistral 7B deutlich weniger Parameter besitzen – etwa 7 Milliarden. Diese Diskrepanz resultiert hauptsächlich aus Unterschieden in der Modellarchitektur und den Trainingsprozessen. Zum Beispiel verwendet ChatGPT einen Selbstaufmerksamkeitsmechanismus innerhalb eines Encoder-Decoder-Frameworks, während Mistral 7B Sliding Window Attention verwendet, was ein effizienteres Training in einem nur aus Decoder bestehenden Modell ermöglicht. Diese architektonische Variation hat weitreichende Auswirkungen auf die Komplexität und Leistung dieser Modelle.

**Verständnis**

SLMs sind typischerweise für die Leistung in spezifischen Domänen optimiert, was sie sehr spezialisiert, aber möglicherweise eingeschränkt in ihrer Fähigkeit macht, ein breites kontextuelles Verständnis über verschiedene Wissensgebiete hinweg bereitzustellen. Im Gegensatz dazu zielen LLMs darauf ab, menschliche Intelligenz auf umfassenderer Ebene zu simulieren. Sie werden mit großen, vielfältigen Datensätzen trainiert und sind darauf ausgelegt, in verschiedenen Domänen gut zu funktionieren, was sie vielseitiger und anpassungsfähiger macht. Folglich eignen sich LLMs besser für eine größere Bandbreite von nachgelagerten Aufgaben wie der Verarbeitung natürlicher Sprache und Programmierung.

**Rechenleistung**

Das Training und der Einsatz von LLMs sind ressourcenintensive Prozesse, die oft erhebliche Recheninfrastrukturen erfordern, einschließlich groß angelegter GPU-Cluster. Beispielsweise kann das Training eines Modells wie ChatGPT von Grund auf Tausende von GPUs über längere Zeiträume benötigen. Im Gegensatz dazu sind SLMs mit ihrer geringeren Parameteranzahl hinsichtlich der benötigten Rechenressourcen zugänglicher. Modelle wie Mistral 7B können auf lokalen Maschinen mit moderaten GPU-Kapazitäten trainiert und ausgeführt werden, obwohl das Training dennoch mehrere Stunden auf mehreren GPUs in Anspruch nimmt.

**Bias**

Bias ist ein bekanntes Problem bei LLMs, hauptsächlich aufgrund der Natur der Trainingsdaten. Diese Modelle stützen sich oft auf rohe, öffentlich verfügbare Daten aus dem Internet, die bestimmte Gruppen unterrepräsentieren oder falsch darstellen können, fehlerhafte Etikettierungen enthalten oder sprachliche Vorurteile widerspiegeln, die durch Dialekte, geographische Unterschiede und grammatikalische Regeln beeinflusst werden. Darüber hinaus kann die Komplexität der LLM-Architekturen unabsichtlich Verzerrungen verstärken, die ohne sorgfältige Feinabstimmung unbemerkt bleiben können. SLMs hingegen, die auf stärker eingeschränkten, domänenspezifischen Datensätzen trainiert werden, sind von Natur aus weniger anfällig für solche Verzerrungen, sind jedoch nicht völlig frei von ihnen.

**Inference**

Die reduzierte Größe von SLMs verschafft ihnen einen erheblichen Vorteil hinsichtlich der Inferenzgeschwindigkeit, da sie Ausgaben effizient auf lokaler Hardware generieren können, ohne umfangreiche parallele Verarbeitung zu benötigen. LLMs hingegen benötigen aufgrund ihrer Größe und Komplexität oft erhebliche parallele Rechenressourcen, um akzeptable Inferenzzeiten zu erreichen. Die Anwesenheit mehrerer gleichzeitiger Nutzer verlangsamt zudem die Antwortzeiten von LLMs, insbesondere bei größerem Einsatzmaßstab.

Zusammenfassend lässt sich sagen, dass sowohl LLMs als auch SLMs auf maschinellem Lernen basieren, sie sich jedoch deutlich durch Modellgröße, Ressourcenbedarf, kontextuelles Verständnis, Anfälligkeit für Bias und Inferenzgeschwindigkeit unterscheiden. Diese Unterschiede spiegeln ihre jeweilige Eignung für verschiedene Anwendungsfälle wider, wobei LLMs vielseitiger, aber ressourcenintensiver sind und SLMs eine domänenspezifischere Effizienz mit reduziertem Rechenaufwand bieten.

***Hinweis: In dieser Lektion führen wir SLM anhand von Microsoft Phi-3 / 3.5 als Beispiel ein.***

## Vorstellung der Phi-3 / Phi-3.5-Familie

Die Phi-3 / 3.5-Familie richtet sich hauptsächlich an Anwendungsszenarien in den Bereichen Text, Vision und Agent (MoE):

### Phi-3 / 3.5 Instruct

Hauptsächlich für Textgenerierung, Chatvervollständigung und die Extraktion von Inhaltsinformationen usw.

**Phi-3-mini**

Das 3,8 Milliarden Parameter umfassende Sprachmodell ist auf Microsoft Foundry, Hugging Face und Ollama verfügbar. Phi-3-Modelle übertreffen Sprachmodelle gleicher oder größerer Größe in wichtigen Benchmarks deutlich (siehe unten Benchmark-Zahlen, höhere Werte sind besser). Phi-3-mini übertrifft Modelle, die doppelt so groß sind, während Phi-3-small und Phi-3-medium größere Modelle, einschließlich GPT-3.5, übertreffen.

**Phi-3-small & medium**

Mit nur 7 Milliarden Parametern schlägt Phi-3-small GPT-3.5T in verschiedenen Sprach-, Denk-, Programmier- und Mathematik-Benchmarks.

Phi-3-medium mit 14 Milliarden Parametern setzt diesen Trend fort und übertrifft Gemini 1.0 Pro.

**Phi-3.5-mini**

Man kann es als Upgrade von Phi-3-mini betrachten. Während die Parameter unverändert bleiben, verbessert es die Unterstützung mehrerer Sprachen (unterstützt über 20 Sprachen: Arabisch, Chinesisch, Tschechisch, Dänisch, Niederländisch, Englisch, Finnisch, Französisch, Deutsch, Hebräisch, Ungarisch, Italienisch, Japanisch, Koreanisch, Norwegisch, Polnisch, Portugiesisch, Russisch, Spanisch, Schwedisch, Thailändisch, Türkisch, Ukrainisch) und bietet stärkere Unterstützung für lange Kontexte.

Phi-3.5-mini mit 3,8 Milliarden Parametern übertrifft Sprachmodelle gleicher Größe und steht Modellen mit der doppelten Größe gleich.

### Phi-3 / 3.5 Vision

Man kann sich das Instruct-Modell von Phi-3/3.5 als Phis Fähigkeit zum Verstehen vorstellen, und Vision verleiht Phi die Augen, um die Welt zu verstehen.


**Phi-3-Vision**

Phi-3-Vision mit nur 4,2 Milliarden Parametern setzt diesen Trend fort und übertrifft größere Modelle wie Claude-3 Haiku und Gemini 1.0 Pro V bei allgemeinen Aufgaben des visuellen Denkens, OCR sowie Tabellen- und Diagrammverständnis.


**Phi-3.5-Vision**

Phi-3.5-Vision ist ebenfalls ein Upgrade von Phi-3-Vision und fügt Unterstützung für mehrere Bilder hinzu. Man kann es als Verbesserung der Vision betrachten: Es kann nicht nur Bilder, sondern auch Videos sehen.

Phi-3.5-Vision übertrifft größere Modelle wie Claude-3.5 Sonnet und Gemini 1.5 Flash bei OCR- sowie Tabellen- und Diagrammverständnisaufgaben und erreicht bei allgemeinen Aufgaben des visuellen Wissensdenkens ein gleichwertiges Niveau. Unterstützt Multi-Frame-Eingaben, d.h. ermöglicht das Denken über mehrere Eingabebilder hinweg.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ermöglicht es Modellen, mit deutlich weniger Rechenaufwand vortrainiert zu werden, was bedeutet, dass man das Modell oder die Datensatzgröße mit dem gleichen Rechenbudget wie bei einem dichten Modell dramatisch skalieren kann. Insbesondere sollte ein MoE-Modell während des Vortrainings die gleiche Qualität wie sein dichtes Pendant viel schneller erreichen.

Phi-3.5-MoE besteht aus 16x3,8 Milliarden Expertenmodulen. Phi-3.5-MoE mit nur 6,6 Milliarden aktiven Parametern erreicht ein vergleichbares Niveau in den Bereichen Denkvermögen, Sprachverständnis und Mathematik wie deutlich größere Modelle.

Wir können das Phi-3/3.5-Familienmodell je nach Szenario verwenden. Anders als bei LLMs kann man Phi-3/3.5-mini oder Phi-3/3.5-Vision auf Edge-Geräten einsetzen.


## Wie verwendet man Phi-3/3.5-Familienmodelle?

Wir möchten Phi-3/3.5 in verschiedenen Szenarien nutzen. Im Folgenden werden wir Phi-3/3.5 je nach Szenario verwenden.

![phi3](../../../translated_images/de/phi3.655208c3186ae381.webp)

### Inferenz via Cloud-APIs

**Microsoft Foundry Modelle**

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ist der direkte Nachfolger.

Microsoft Foundry Modelle sind der direkteste Weg. Sie können schnell auf das Phi-3/3.5-Instruct-Modell über den Foundry-Modellkatalog zugreifen. Kombiniert mit dem Azure AI Inference SDK / OpenAI SDK können Sie die API über Code aufrufen, um Phi-3/3.5-Instruct-Anfragen zu erledigen. Außerdem können Sie über den Playground verschiedene Effekte testen.

- Demo: Vergleich der Effekte von Phi-3-mini und Phi-3.5-mini in chinesischen Szenarien

![phi3](../../../translated_images/de/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/de/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Wenn Sie hingegen Vision- und MoE-Modelle verwenden möchten, können Sie Microsoft Foundry für den Aufruf nutzen. Wenn Sie interessiert sind, können Sie im Phi-3 Cookbook nachlesen, wie man Phi-3/3.5-Instruct, Vision, MoE über Microsoft Foundry aufruft [Klicken Sie diesen Link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Neben dem cloudbasierten Microsoft Foundry Modelle-Katalog können Sie auch [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) für verwandte Aufrufe nutzen. Sie können NVIDIA NIM besuchen, um die API-Aufrufe der Phi-3/3.5-Familie durchzuführen. NVIDIA NIM (NVIDIA Inference Microservices) ist eine Reihe beschleunigter Inferenz-Microservices, die Entwicklern helfen sollen, KI-Modelle effizient in verschiedenen Umgebungen, einschließlich Clouds, Rechenzentren und Workstations, bereitzustellen.

Hier einige Hauptmerkmale von NVIDIA NIM:

- **Einfache Bereitstellung:** NIM ermöglicht die Bereitstellung von KI-Modellen mit nur einem Befehl, was die Integration in bestehende Workflows unkompliziert macht.

- **Optimierte Leistung:** Es nutzt die von NVIDIA voroptimierten Inferenz-Engines wie TensorRT und TensorRT-LLM, um niedrige Latenz und hohe Durchsatzrate zu gewährleisten.
- **Skalierbarkeit:** NIM unterstützt die automatische Skalierung auf Kubernetes, wodurch es effektiv mit unterschiedlichen Arbeitslasten umgehen kann.
- **Sicherheit und Kontrolle:** Organisationen können die Kontrolle über ihre Daten und Anwendungen behalten, indem sie NIM-Mikroservices auf ihrer eigenen verwalteten Infrastruktur selbst hosten.
- **Standardisierte APIs:** NIM stellt branchentypische APIs bereit, die den Aufbau und die Integration von KI-Anwendungen wie Chatbots, KI-Assistenten und mehr erleichtern.

NIM ist Teil von NVIDIA AI Enterprise, das darauf abzielt, die Bereitstellung und Operationalisierung von KI-Modellen zu vereinfachen und deren effizienten Betrieb auf NVIDIA-GPUs sicherzustellen.

- Demo: Verwendung von NVIDIA NIM, um die Phi-3.5-Vision-API aufzurufen [[Klicken Sie hier](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokales Ausführen von Phi-3/3.5
Inferenz in Bezug auf Phi-3 oder jedes andere Sprachmodell wie GPT-3 bezeichnet den Prozess der Generierung von Antworten oder Vorhersagen basierend auf den erhaltenen Eingaben. Wenn Sie Phi-3 eine Eingabe oder Frage geben, verwendet es sein trainiertes neuronales Netzwerk, um die wahrscheinlichste und relevanteste Antwort zu ermitteln, indem es Muster und Zusammenhänge in den Trainingsdaten analysiert.

**Hugging Face Transformer**
Hugging Face Transformers ist eine leistungsstarke Bibliothek für natürliche Sprachverarbeitung (NLP) und andere Aufgaben des maschinellen Lernens. Hier einige wichtige Punkte:

1. **Vortrainierte Modelle**: Sie bietet Tausende vortrainierte Modelle für verschiedene Aufgaben wie Textklassifizierung, Named Entity Recognition, Fragebeantwortung, Zusammenfassung, Übersetzung und Textgenerierung.

2. **Framework-Interoperabilität:** Die Bibliothek unterstützt mehrere Deep-Learning-Frameworks, darunter PyTorch, TensorFlow und JAX. So können Sie ein Modell in einem Framework trainieren und in einem anderen verwenden.

3. **Multimodale Fähigkeiten:** Neben NLP unterstützt Hugging Face Transformers auch Aufgaben in der Computer Vision (z. B. Bildklassifikation, Objekterkennung) und Audioverarbeitung (z. B. Spracherkennung, Audioklassifikation).

4. **Einfache Nutzung:** Die Bibliothek bietet APIs und Werkzeuge zum einfachen Herunterladen und Feinabstimmen von Modellen, wodurch sie sowohl für Anfänger als auch Experten zugänglich ist.

5. **Community und Ressourcen:** Hugging Face verfügt über eine lebendige Community sowie umfangreiche Dokumentationen, Tutorials und Anleitungen, die den Einstieg erleichtern und die Nutzung der Bibliothek optimieren.
[offizielle Dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oder ihres [GitHub-Repositories](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dies ist die meistgenutzte Methode, erfordert jedoch GPU-Beschleunigung. Anwendungsfälle wie Vision und MoE erfordern viel Rechenleistung, was auf der CPU sehr langsam wäre, wenn diese nicht quantisiert sind.


- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Instruct [Klicken Sie hier](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Vision [Klicken Sie hier](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-MoE [Klicken Sie hier](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ist eine Plattform, die es einfacher macht, große Sprachmodelle (LLMs) lokal auf Ihrem Rechner auszuführen. Sie unterstützt verschiedene Modelle wie Llama 3.1, Phi 3, Mistral und Gemma 2 und weitere. Die Plattform vereinfacht den Prozess, indem sie Modellgewichte, Konfiguration und Daten in einem Paket bündelt, was es Nutzern erleichtert, eigene Modelle zu erstellen und anzupassen. Ollama ist für macOS, Linux und Windows verfügbar. Es ist ein großartiges Werkzeug, wenn Sie mit LLMs experimentieren oder sie bereitstellen möchten, ohne Cloud-Dienste zu nutzen. Ollama ist der direkteste Weg, Sie müssen nur folgenden Befehl ausführen.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ist Microsofts Offline-Laufzeitumgebung für Modelle wie Phi, die vollständig auf Ihrer eigenen Hardware läuft - kein Azure-Abonnement, API-Schlüssel oder Netzwerkverbindung erforderlich. Es wählt automatisch den besten verfügbaren Ausführungstreiber (NPU, GPU oder CPU) aus und bietet einen OpenAI-kompatiblen Endpunkt, sodass bestehender `openai`-/Azure AI Inference SDK-Code mit minimalen Änderungen darauf zugreifen kann. Siehe die [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Oder verwenden Sie das SDK direkt in Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime für GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ist ein plattformübergreifender Beschleuniger für Inferenz und Training von maschinellen Lernmodellen. ONNX Runtime für Generative AI (GENAI) ist ein leistungsstarkes Werkzeug, das Ihnen hilft, generative KI-Modelle effizient auf verschiedenen Plattformen auszuführen.

## Was ist ONNX Runtime?
ONNX Runtime ist ein Open-Source-Projekt, das eine leistungsstarke Inferenz von maschinellen Lernmodellen ermöglicht. Es unterstützt Modelle im Open Neural Network Exchange (ONNX)-Format, einem Standard zur Repräsentation von Modellen des maschinellen Lernens. Die ONNX Runtime-Inferenz kann schnellere Kundenerfahrungen und niedrigere Kosten ermöglichen und unterstützt Modelle aus Deep-Learning-Frameworks wie PyTorch und TensorFlow/Keras sowie klassische maschinelle Lernbibliotheken wie scikit-learn, LightGBM, XGBoost usw. ONNX Runtime ist kompatibel mit verschiedener Hardware, Treibern und Betriebssystemen und bietet optimale Leistung durch Nutzung von Hardwarebeschleunigern sowie Graph-Optimierungen und Transformationen.

## Was ist Generative AI?
Generative AI bezeichnet KI-Systeme, die neue Inhalte erzeugen können, beispielsweise Text, Bilder oder Musik, basierend auf den Daten, mit denen sie trainiert wurden. Beispiele sind Sprachmodelle wie GPT-3 und Bildgenerierungsmodelle wie Stable Diffusion. Die ONNX Runtime für GenAI-Bibliothek stellt eine generative KI-Schleife für ONNX-Modelle bereit, einschließlich Inferenz mit ONNX Runtime, Logits-Verarbeitung, Such- und Sampling-Methoden sowie Verwaltung des KV-Caches.

## ONNX Runtime für GENAI
ONNX Runtime für GENAI erweitert die Fähigkeiten von ONNX Runtime um die Unterstützung generativer KI-Modelle. Hier einige Hauptmerkmale:

- **Breite plattformübergreifende Unterstützung:** Funktioniert auf verschiedenen Plattformen, darunter Windows, Linux, macOS, Android und iOS.
- **Modell-Unterstützung:** Unterstützt viele populäre generative KI-Modelle wie LLaMA, GPT-Neo, BLOOM und mehr.
- **Leistungsoptimierung:** Enthält Optimierungen für verschiedene Hardwarebeschleuniger wie NVIDIA GPUs, AMD GPUs und mehr2.
- **Einfache Nutzung:** Bietet APIs zur einfachen Integration in Anwendungen, damit Sie Texte, Bilder und andere Inhalte mit minimalem Code generieren können.
- Nutzer können eine hochrangige generate()-Methode aufrufen oder jede Iteration des Modells in einer Schleife ausführen, dabei je Token generieren und optional die Generierungsparameter in der Schleife anpassen.
- ONNX Runtime unterstützt außerdem Greedy-/Beam-Search und TopP- sowie TopK-Sampling zur Generierung von Token-Sequenzen und eingebaute Logits-Verarbeitung wie Wiederholungsstrafen. Sie können auch leicht eigene Bewertungsfunktionen hinzufügen.

## Erste Schritte
Um mit ONNX Runtime für GENAI zu starten, können Sie folgende Schritte befolgen:

### ONNX Runtime installieren:
```Python
pip install onnxruntime
```
### Die Generative AI Extensions installieren:
```Python
pip install onnxruntime-genai
```

### Modell ausführen: Hier ein einfaches Beispiel in Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Verwendung von ONNX Runtime GenAI zum Aufruf von Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Andere**

Zusätzlich zu ONNX Runtime, Ollama und Foundry Local Referenzmethoden können wir auch die Referenz Quantifizierter Modelle basierend auf den Referenzmethoden verschiedener Hersteller vervollständigen. Zum Beispiel Apple MLX-Framework mit Apple Metal, Qualcomm QNN mit NPU, Intel OpenVINO mit CPU/GPU usw. Weitere Inhalte finden Sie auch im [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mehr

Wir haben die Grundlagen der Phi-3/3.5-Familie gelernt, aber um mehr über SLM zu erfahren, benötigen wir weiterführendes Wissen. Die Antworten finden Sie im Phi-3 Cookbook. Wenn Sie mehr erfahren möchten, besuchen Sie bitte das [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->