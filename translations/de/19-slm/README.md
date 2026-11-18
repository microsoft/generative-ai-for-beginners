# Einführung in kleine Sprachmodelle für generative KI für Anfänger
Generative KI ist ein faszinierendes Gebiet der künstlichen Intelligenz, das sich darauf konzentriert, Systeme zu erschaffen, die in der Lage sind, neue Inhalte zu erzeugen. Diese Inhalte können von Text und Bildern bis hin zu Musik und sogar ganzen virtuellen Umgebungen reichen. Eine der spannendsten Anwendungen generativer KI liegt im Bereich der Sprachmodelle.

## Was sind kleine Sprachmodelle?

Ein kleines Sprachmodell (SLM) stellt eine verkleinerte Variante eines großen Sprachmodells (LLM) dar, das viele der architektonischen Prinzipien und Techniken von LLMs nutzt, dabei jedoch einen deutlich geringeren Rechenaufwand aufweist.

SLMs sind eine Untergruppe von Sprachmodellen, die darauf ausgelegt sind, menschenähnlichen Text zu generieren. Im Gegensatz zu ihren größeren Pendants wie GPT-4 sind SLMs kompakter und effizienter, wodurch sie ideal für Anwendungen sind, bei denen die Rechenressourcen begrenzt sind. Trotz ihrer kleineren Größe können sie eine Vielzahl von Aufgaben ausführen. Typischerweise werden SLMs durch Kompression oder Destillation von LLMs erstellt, mit dem Ziel, einen wesentlichen Teil der ursprünglichen Funktionalität und sprachlichen Fähigkeiten zu erhalten. Diese Verkleinerung des Modells verringert die Gesamtkomplexität und macht SLMs sowohl in Bezug auf den Speicherverbrauch als auch den Rechenaufwand effizienter. Trotz dieser Optimierungen können SLMs eine breite Palette von Aufgaben der natürlichen Sprachverarbeitung (NLP) bewältigen:

- Textgenerierung: Erstellen kohärenter und kontextuell relevanter Sätze oder Absätze.
- Textvervollständigung: Vorhersagen und Vervollständigen von Sätzen basierend auf einem gegebenen Prompt.
- Übersetzung: Umwandlung von Text von einer Sprache in eine andere.
- Zusammenfassung: Verdichtung langer Texte in kürzere, leichter verdauliche Zusammenfassungen.

Zwar mit einigen Kompromissen bei der Leistung oder dem Tiefgang des Verständnisses im Vergleich zu größeren Modellen.

## Wie funktionieren kleine Sprachmodelle?
SLMs werden mit großen Mengen an Textdaten trainiert. Während des Trainings lernen sie die Muster und Strukturen der Sprache, was es ihnen ermöglicht, Texte zu erzeugen, die sowohl grammatikalisch korrekt als auch kontextuell passend sind. Der Trainingsprozess beinhaltet:

- Datensammlung: Erfassung großer Datensätze aus verschiedenen Quellen.
- Vorverarbeitung: Bereinigung und Organisation der Daten, um sie für das Training geeignet zu machen.
- Training: Einsatz von maschinellen Lernalgorithmen, um dem Modell zu vermitteln, wie es Texte versteht und generiert.
- Feinabstimmung: Anpassung des Modells, um die Leistung bei spezifischen Aufgaben zu verbessern.

Die Entwicklung von SLMs entspricht dem zunehmenden Bedarf an Modellen, die in ressourcenbeschränkten Umgebungen, wie mobilen Geräten oder Edge-Computing-Plattformen, eingesetzt werden können, wo vollskalige LLMs aufgrund ihres hohen Ressourcenbedarfs unpraktisch sind. Durch den Fokus auf Effizienz balancieren SLMs Leistung und Zugänglichkeit, was eine breitere Anwendung in verschiedenen Bereichen ermöglicht.

![slm](../../../translated_images/de/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Lernziele

In dieser Lektion möchten wir Wissen über SLM vermitteln und es mit Microsoft Phi-3 kombinieren, um verschiedene Szenarien im Textbereich, der Bildverarbeitung und MoE kennenzulernen.

Am Ende dieser Lektion sollten Sie in der Lage sein, folgende Fragen zu beantworten:

- Was ist ein SLM?
- Was ist der Unterschied zwischen SLM und LLM?
- Was ist die Microsoft Phi-3/3.5 Familie?
- Wie führt man Inferenz mit der Microsoft Phi-3/3.5 Familie aus?

Bereit? Dann beginnen wir.

## Die Unterschiede zwischen großen Sprachmodellen (LLMs) und kleinen Sprachmodellen (SLMs)

Sowohl LLMs als auch SLMs basieren auf grundlegenden Prinzipien des probabilistischen maschinellen Lernens und verfolgen ähnliche Ansätze in ihrer architektonischen Gestaltung, Trainingsmethoden, Datengenerierungsprozessen und Modelbewertungsverfahren. Es gibt jedoch mehrere entscheidende Faktoren, die diese beiden Modelltypen unterscheiden.

## Anwendungen kleiner Sprachmodelle

SLMs haben ein breites Anwendungsspektrum, darunter:

- Chatbots: Bereitstellung von Kundensupport und Interaktion mit Nutzern in Gesprächsform.
- Inhaltserstellung: Unterstützung von Autoren durch Generierung von Ideen oder sogar vollständigen Artikeln.
- Bildung: Hilfe für Schüler bei Schreibaufgaben oder beim Erlernen neuer Sprachen.
- Barrierefreiheit: Erstellung von Tools für Menschen mit Behinderungen, wie Text-zu-Sprache-Systeme.

**Größe**
  
Ein wesentlicher Unterschied zwischen LLMs und SLMs liegt im Umfang der Modelle. LLMs, wie ChatGPT (GPT-4), können geschätzte 1,76 Billionen Parameter umfassen, während Open-Source-SLMs wie Mistral 7B mit deutlich weniger Parametern – etwa 7 Milliarden – konzipiert sind. Diese Diskrepanz beruht hauptsächlich auf Unterschieden in der Modellarchitektur und den Trainingsprozessen. Beispielsweise verwendet ChatGPT einen Selbstaufmerksamkeitsmechanismus innerhalb eines Encoder-Decoder-Rahmens, während Mistral 7B Sliding-Window-Attention nutzt, was ein effizienteres Training innerhalb eines Decoder-Modells ermöglicht. Diese architektonische Variation hat tiefgreifende Auswirkungen auf die Komplexität und Leistung dieser Modelle.

**Verständnis**

SLMs sind typischerweise für die Leistung in spezifischen Domänen optimiert, wodurch sie hoch spezialisiert, jedoch potenziell begrenzt in der Fähigkeit sind, ein breites kontextuelles Verständnis über mehrere Wissensgebiete hinweg bereitzustellen. Im Gegensatz dazu zielen LLMs darauf ab, eine menschenähnliche Intelligenz auf umfassenderem Niveau zu simulieren. Trainiert auf umfangreichen, vielfältigen Datensätzen, sind LLMs darauf ausgelegt, in verschiedenen Domänen gut zu funktionieren und bieten größere Vielseitigkeit und Anpassungsfähigkeit. Folglich sind LLMs besser geeignet für eine breitere Palette von nachgelagerten Aufgaben wie der Verarbeitung natürlicher Sprache und Programmierung.

**Rechenleistung**

Das Training und der Einsatz von LLMs sind ressourcenintensive Prozesse, die oft eine erhebliche Infrastruktur erfordern, einschließlich groß angelegter GPU-Cluster. Zum Beispiel kann das Training eines Modells wie ChatGPT von Grund auf tausende GPUs über längere Zeiträume benötigen. Im Gegensatz dazu sind SLMs mit ihrer geringeren Parameteranzahl zugänglicher hinsichtlich der Rechenressourcen. Modelle wie Mistral 7B können auf lokalen Rechnern mit moderaten GPU-Fähigkeiten trainiert und ausgeführt werden, wobei das Training dennoch mehrere Stunden über mehrere GPUs dauern kann.

**Bias**

Bias ist ein bekanntes Problem bei LLMs, hauptsächlich bedingt durch die Art der Trainingsdaten. Diese Modelle basieren häufig auf rohen, offen verfügbaren Internetdaten, die bestimmte Gruppen unterrepräsentieren oder falsch darstellen können, fehlerhafte Kennzeichnungen enthalten oder durch dialektale, geografische und grammatikalische Sprachvariationen beeinflusste Verzerrungen aufweisen. Zudem kann die Komplexität der LLM-Architekturen unbeabsichtigt Bias verstärken, der ohne sorgfältiges Feintuning unbemerkt bleiben kann. Andererseits sind SLMs, da sie auf eingeschränktere, domänenspezifische Datensätze trainiert werden, prinzipiell weniger anfällig für solche Verzerrungen, aber nicht völlig immun.

**Inference**

Die geringere Größe von SLMs verschafft ihnen einen erheblichen Vorteil hinsichtlich der Inferenzgeschwindigkeit, wodurch sie Ausgaben effizient auf lokaler Hardware generieren können, ohne umfangreiche parallele Verarbeitung zu benötigen. LLMs benötigen aufgrund ihrer Größe und Komplexität oft erhebliche parallele Rechenressourcen, um akzeptable Inferenzzeiten zu erreichen. Die gleichzeitige Nutzung durch mehrere Anwender verlangsamt die Antwortzeiten von LLMs besonders bei großflächiger Bereitstellung zusätzlich.

Zusammenfassend lässt sich sagen, dass LLMs und SLMs zwar auf einem gemeinsamen maschinellen Lernfundament basieren, sich jedoch signifikant in Modellgröße, Ressourcenbedarf, kontextuellem Verständnis, Anfälligkeit für Bias und Inferenzgeschwindigkeit unterscheiden. Diese Unterschiede spiegeln ihre jeweilige Eignung für unterschiedliche Anwendungsfälle wider, wobei LLMs vielseitiger, aber ressourcenintensiver sind und SLMs domänenspezifische Effizienz bei reduziertem Ressourcenaufwand bieten.

***Hinweis: In dieser Lektion führen wir SLM anhand von Microsoft Phi-3 / 3.5 als Beispiel ein.***

## Vorstellung der Phi-3 / Phi-3.5 Familie

Die Phi-3 / 3.5 Familie zielt hauptsächlich auf Anwendungsfälle in Text, Bildverarbeitung und Agent (MoE) ab:

### Phi-3 / 3.5 Instruct

Hauptsächlich für Textgenerierung, Chat-Vervollständigung und die Extraktion von Inhaltsinformationen usw.

**Phi-3-mini**

Das 3,8 Milliarden Parameter umfassende Sprachmodell ist auf Microsoft Foundry, Hugging Face und Ollama verfügbar. Phi-3-Modelle übertreffen Sprachmodelle gleicher oder größerer Größe bei wichtigen Benchmarks deutlich (siehe unten Benchmark-Zahlen, höhere Zahlen sind besser). Phi-3-mini übertrifft Modelle mit der doppelten Größe, während Phi-3-small und Phi-3-medium größere Modelle, einschließlich GPT-3.5, übertreffen.

**Phi-3-small & medium**

Mit nur 7 Milliarden Parametern schlägt Phi-3-small GPT-3.5T bei einer Vielzahl von Sprach-, Denk-, Programmier- und Mathematik-Benchmarks.

Phi-3-medium mit 14 Milliarden Parametern setzt diesen Trend fort und übertrifft den Gemini 1.0 Pro.

**Phi-3.5-mini**

Man kann es als Upgrade von Phi-3-mini betrachten. Während die Parameteranzahl unverändert bleibt, verbessert es die Unterstützung für mehrere Sprachen (unterstützt 20+ Sprachen: Arabisch, Chinesisch, Tschechisch, Dänisch, Niederländisch, Englisch, Finnisch, Französisch, Deutsch, Hebräisch, Ungarisch, Italienisch, Japanisch, Koreanisch, Norwegisch, Polnisch, Portugiesisch, Russisch, Spanisch, Schwedisch, Thailändisch, Türkisch, Ukrainisch) und bietet eine stärkere Unterstützung für längere Kontexte.

Phi-3.5-mini mit 3,8 Milliarden Parametern übertrifft Sprachmodelle der gleichen Größe und ist vergleichbar mit Modellen der doppelten Größe.

### Phi-3 / 3.5 Vision

Man kann das Instruct-Modell von Phi-3/3.5 als Phis Fähigkeit zu verstehen betrachten, und Vision verleiht Phi die Augen, um die Welt zu verstehen.


**Phi-3-Vision**

Phi-3-vision mit nur 4,2 Milliarden Parametern setzt diesen Trend fort und übertrifft größere Modelle wie Claude-3 Haiku und Gemini 1.0 Pro V bei allgemeinen visuell-logischen Aufgaben, OCR sowie Aufgaben zum Verständnis von Tabellen und Diagrammen.


**Phi-3.5-Vision**

Phi-3.5-Vision ist ebenfalls ein Upgrade von Phi-3-Vision und erweitert die Unterstützung auf mehrere Bilder. Man kann es als Verbesserung im Bereich Vision sehen, nicht nur können Bilder erkannt werden, sondern auch Videos.

Phi-3.5-vision übertrifft größere Modelle wie Claude-3.5 Sonnet und Gemini 1.5 Flash bei OCR-, Tabellen- und Diagrammverständnisaufgaben und ist vergleichbar bei allgemeinen visuell-logischen Aufgaben. Unterstützt Mehrbild-Eingaben, d.h., es kann auf mehreren Eingabebildern schlussfolgern.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ermöglicht es, Modelle mit deutlich weniger Rechenleistung vorzutrainieren, was bedeutet, dass man die Modell- oder Datensatzgröße dramatisch mit dem gleichen Rechenbudget wie ein dichtes Modell skalieren kann. Insbesondere sollte ein MoE-Modell während des Vortrainings die gleiche Qualität wie sein dichtes Pendant deutlich schneller erreichen.

Phi-3.5-MoE besteht aus 16x3,8 Milliarden Expertenmodulen. Phi-3.5-MoE mit nur 6,6 Milliarden aktiven Parametern erreicht ein ähnliches Niveau bei Denk-, Sprachverständnis- und Mathematikaufgaben wie deutlich größere Modelle.

Wir können das Phi-3/3.5 Familenmodell je nach Szenario verwenden. Im Gegensatz zu LLMs kann man Phi-3/3.5-mini oder Phi-3/3.5-Vision auf Edge-Geräten einsetzen.


## Wie man Phi-3/3.5 Familienmodelle nutzt

Wir möchten Phi-3/3.5 in verschiedenen Szenarien einsetzen. Im Folgenden werden wir Phi-3/3.5 je nach Szenario einsetzen.

![phi3](../../../translated_images/de/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenz über Cloud-APIs

**Microsoft Foundry Modelle**

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ist der direkte Ersatz.

> **Hinweis:** Die gesamte Phi-3/3.5 Familie (Instruct-, Vision- und MoE-Varianten) wurde am 30.08.2025 aus dem Microsoft Foundry Models Katalog entfernt. Verwenden Sie stattdessen `Phi-4` (Instruct) oder `Phi-4-mini-instruct` – die Phi-3/3.5 Beispiele unten funktionieren weiterhin über Hugging Face, Ollama, ONNX Runtime und NVIDIA NIM.

Microsoft Foundry Models bietet jetzt die Nachfolger Phi-4 an. Verwenden Sie `Phi-4` oder `Phi-4-mini-instruct` anstelle der eingestellten Phi-3/3.5 Modelle, wenn Sie den Cloud-API-Beispielen folgen.

- Demo: Vergleich der Effekte von Phi-3-mini und Phi-3.5-mini in chinesischen Szenarien

![phi3](../../../translated_images/de/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/de/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Wenn Sie Vision- (multimodale) Modelle in der Cloud nutzen möchten, verwenden Sie die derzeit verfügbaren `Phi-4-multimodal-instruct` über Microsoft Foundry anstelle der eingestellten Phi-3/3.5 Vision Modelle; für Textaufgaben nutzen Sie `Phi-4` oder `Phi-4-mini-instruct`. Das Phi-3.5 MoE Modell wurde aus Microsoft Foundry entfernt, verwenden Sie die anderen in dieser Lektion beschriebenen Optionen (z.B. Hugging Face), wenn Sie damit experimentieren möchten. Bei Interesse können Sie das Phi Cookbook lesen, um zu erfahren, wie man Phi-Modelle über Microsoft Foundry aufruft [Klicken Sie diesen Link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Zusätzlich zum cloudbasierten Microsoft Foundry Models Katalog können Sie auch [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) zur Ausführung der entsprechenden Aufrufe nutzen. Besuchen Sie NVIDIA NIM, um die API-Aufrufe der Phi-3/3.5 Familie zu tätigen. NVIDIA NIM (NVIDIA Inference Microservices) ist eine Reihe beschleunigter Inferenz-Mikroservices, die Entwicklern helfen sollen, KI-Modelle effizient über verschiedene Umgebungen hinweg zu betreiben, einschließlich Clouds, Rechenzentren und Workstations.

Hier sind einige Hauptmerkmale von NVIDIA NIM:

- **Einfache Bereitstellung:** NIM ermöglicht die Bereitstellung von KI-Modellen mit einem einzigen Befehl, wodurch die Integration in bestehende Arbeitsabläufe einfach ist.
- **Optimierte Leistung:** Es nutzt die voroptimierten Inferenz-Engines von NVIDIA, wie TensorRT und TensorRT-LLM, um geringe Latenz und hohe Durchsatzraten sicherzustellen.
- **Skalierbarkeit:** NIM unterstützt Auto-Scaling auf Kubernetes, wodurch es variable Arbeitslasten effektiv bewältigen kann.
- **Sicherheit und Kontrolle:** Organisationen können die Kontrolle über ihre Daten und Anwendungen behalten, indem sie NIM-Mikrodienste auf ihrer eigenen verwalteten Infrastruktur selbst hosten.
- **Standardisierte APIs:** NIM stellt branchenübliche APIs bereit, die den Aufbau und die Integration von KI-Anwendungen wie Chatbots, KI-Assistenten und mehr erleichtern.

NIM ist Teil von NVIDIA AI Enterprise, das darauf abzielt, die Bereitstellung und Operationalisierung von KI-Modellen zu vereinfachen und sicherzustellen, dass sie effizient auf NVIDIA GPUs laufen.

- Demo: Verwendung von NVIDIA NIM zum Aufrufen der Phi-3.5-Vision-API [[Klicken Sie auf diesen Link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokal ausführen
Inferenz im Zusammenhang mit Phi-3 oder einem Sprachmodell wie GPT-3 bezieht sich auf den Prozess der Generierung von Antworten oder Vorhersagen basierend auf den erhaltenen Eingaben. Wenn Sie Phi-3 eine Eingabe oder Frage geben, verwendet es sein trainiertes neuronales Netzwerk, um durch Analyse von Mustern und Zusammenhängen in den Trainingsdaten die wahrscheinlichste und relevanteste Antwort abzuleiten.

**Hugging Face Transformer**
Hugging Face Transformers ist eine leistungsstarke Bibliothek für die Verarbeitung natürlicher Sprache (NLP) und weitere maschinelle Lernaufgaben. Hier sind einige wichtige Punkte dazu:

1. **Vortrainierte Modelle**: Sie bietet Tausende vortrainierte Modelle, die für verschiedene Aufgaben wie Textklassifikation, Named Entity Recognition, Fragebeantwortung, Zusammenfassung, Übersetzung und Textgenerierung verwendet werden können.

2. **Framework-Interoperabilität**: Die Bibliothek unterstützt mehrere Deep-Learning-Frameworks wie PyTorch, TensorFlow und JAX. Dadurch können Sie ein Modell in einem Framework trainieren und in einem anderen verwenden.

3. **Multimodale Fähigkeiten**: Neben NLP unterstützt Hugging Face Transformers auch Aufgaben im Bereich Computer Vision (z. B. Bildklassifikation, Objekterkennung) und Audiobearbeitung (z. B. Spracherkennung, Audioklassifikation).

4. **Benutzerfreundlichkeit**: Die Bibliothek bietet APIs und Tools, um Modelle einfach herunterzuladen und feinzujustieren, was sie sowohl für Anfänger als auch Experten zugänglich macht.

5. **Community und Ressourcen**: Hugging Face verfügt über eine lebendige Community sowie umfangreiche Dokumentationen, Tutorials und Anleitungen, die Nutzern den Einstieg erleichtern und die Nutzung der Bibliothek optimieren.
[offizielle Dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oder deren [GitHub-Repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dies ist die am häufigsten genutzte Methode, aber sie erfordert auch GPU-Beschleunigung. Szenarien wie Vision und MoE benötigen viele Berechnungen, die auf einer CPU ohne Quantisierung sehr langsam wären.


- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Instruct [Klicken Sie auf diesen Link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Vision [Klicken Sie auf diesen Link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-MoE [Klicken Sie auf diesen Link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ist eine Plattform, die es leichter macht, große Sprachmodelle (LLMs) lokal auf Ihrem Gerät auszuführen. Sie unterstützt verschiedene Modelle wie Llama 3.1, Phi 3, Mistral und Gemma 2 unter anderem. Die Plattform vereinfacht den Prozess, indem sie Modellgewichte, Konfiguration und Daten in einem Paket bündelt, was es Nutzern zugänglicher macht, eigene Modelle anzupassen und zu erstellen. Ollama ist für macOS, Linux und Windows verfügbar. Es ist ein großartiges Tool, wenn Sie mit LLMs experimentieren oder sie ohne Cloud-Dienste bereitstellen möchten. Ollama ist der direkteste Weg, Sie müssen nur den folgenden Befehl ausführen.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ist Microsofts Offline-On-Device-Laufzeitumgebung zum Ausführen von Modellen wie Phi vollständig auf Ihrer eigenen Hardware – kein Azure-Abonnement, API-Schlüssel oder Netzwerkverbindung erforderlich. Es wählt automatisch den besten verfügbaren Ausführungsanbieter (NPU, GPU oder CPU) und stellt einen OpenAI-kompatiblen Endpunkt bereit, sodass bestehender `openai`/Azure AI Inference SDK-Code mit minimalen Änderungen darauf zeigen kann. Siehe die [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ist ein plattformübergreifender Beschleuniger für Inferenz und Training im Maschinenlernen. ONNX Runtime für Generative AI (GENAI) ist ein leistungsstarkes Werkzeug, das Ihnen hilft, generative KI-Modelle effizient auf verschiedenen Plattformen auszuführen.

## Was ist ONNX Runtime?
ONNX Runtime ist ein Open-Source-Projekt, das hochleistungsfähige Inferenz für Maschinenlernmodelle ermöglicht. Es unterstützt Modelle im Open Neural Network Exchange (ONNX)-Format, einem Standard zur Repräsentation von Maschinenlernmodellen. ONNX Runtime-Inferenz kann schnellere Kundenerlebnisse und geringere Kosten ermöglichen und unterstützt Modelle von Deep-Learning-Frameworks wie PyTorch und TensorFlow/Keras sowie klassische Maschinenlern-Bibliotheken wie scikit-learn, LightGBM, XGBoost usw. ONNX Runtime ist kompatibel mit verschiedenster Hardware, Treibern und Betriebssystemen und erzielt optimale Leistung durch Nutzung von Hardwarebeschleunigern wo möglich, kombiniert mit Graph-Optimierungen und Transformationen.

## Was ist Generative KI?
Generative KI bezeichnet KI-Systeme, die neue Inhalte wie Texte, Bilder oder Musik anhand der Daten erzeugen können, auf denen sie trainiert wurden. Beispiele sind Sprachmodelle wie GPT-3 und Bildgenerierungsmodelle wie Stable Diffusion. Die ONNX Runtime für GenAI-Bibliothek stellt den generativen KI-Workflow für ONNX-Modelle bereit, einschließlich Inferenz mit ONNX Runtime, Verarbeitung von Logits, Suche und Sampling sowie Verwaltung des KV-Caches.

## ONNX Runtime für GENAI
ONNX Runtime für GENAI erweitert die Fähigkeiten von ONNX Runtime, um generative KI-Modelle zu unterstützen. Hier einige Hauptmerkmale:

- **Breite Plattformunterstützung:** Es läuft auf verschiedenen Plattformen, darunter Windows, Linux, macOS, Android und iOS.
- **Modellunterstützung:** Es unterstützt viele beliebte generative KI-Modelle wie LLaMA, GPT-Neo, BLOOM und mehr.
- **Leistungsoptimierung:** Es enthält Optimierungen für verschiedene Hardwarebeschleuniger wie NVIDIA-GPUs, AMD-GPUs und weitere2.
- **Benutzerfreundlichkeit:** Es bietet APIs zur einfachen Integration in Anwendungen, mit denen Sie Texte, Bilder und andere Inhalte mit minimalem Code generieren können
- Nutzer können eine hochstufige generate()-Methode aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei Token für Token generiert werden und optional die Generierungsparameter innerhalb der Schleife aktualisiert werden.
- ONNX Runtime unterstützt außerdem Greedy/Beam Search und TopP-, TopK-Sampling zur Generierung von Token-Sequenzen sowie integrierte Logits-Verarbeitung wie Wiederholungsstrafen. Sie können auch leicht benutzerdefinierte Bewertungen hinzufügen.

## Erste Schritte
Um mit ONNX Runtime für GENAI zu starten, können Sie folgende Schritte befolgen:

### ONNX Runtime installieren:
```Python
pip install onnxruntime
```
### Erweiterungen für Generative KI installieren:
```Python
pip install onnxruntime-genai
```

### Ein Modell ausführen: Hier ein einfaches Beispiel in Python:
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


**Weiteres**

Zusätzlich zu ONNX Runtime, Ollama und Foundry Local Referenzmethoden können wir auch den Bezug von quantitativen Modellen anhand der von verschiedenen Herstellern bereitgestellten Modellreferenzmethoden vervollständigen. Beispielsweise Apple MLX Framework mit Apple Metal, Qualcomm QNN mit NPU, Intel OpenVINO mit CPU/GPU, etc. Weitere Inhalte finden Sie auch im [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mehr

Wir haben die Grundlagen der Phi-3/3.5 Familie gelernt, aber um mehr über SLM zu erfahren, benötigen wir mehr Wissen. Die Antworten finden Sie im Phi-3 Cookbook. Wenn Sie mehr lernen möchten, besuchen Sie bitte das [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->