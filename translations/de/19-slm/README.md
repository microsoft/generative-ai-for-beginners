# Einführung in kleine Sprachmodelle für generative KI für Anfänger
Generative KI ist ein faszinierendes Gebiet der Künstlichen Intelligenz, das sich auf die Erstellung von Systemen konzentriert, die neue Inhalte generieren können. Diese Inhalte können von Text und Bildern über Musik bis hin zu ganzen virtuellen Umgebungen reichen. Eine der spannendsten Anwendungen der generativen KI ist im Bereich der Sprachmodelle.

## Was sind kleine Sprachmodelle?

Ein kleines Sprachmodell (SLM) stellt eine verkleinerte Variante eines großen Sprachmodells (LLM) dar, die viele der architektonischen Prinzipien und Techniken von LLMs nutzt, dabei jedoch einen deutlich reduzierten Rechenaufwand aufweist. 

SLMs sind eine Untergruppe von Sprachmodellen, die entwickelt wurden, um menschenähnlichen Text zu erzeugen. Im Gegensatz zu ihren größeren Gegenstücken wie GPT-4 sind SLMs kompakter und effizienter, was sie ideal für Anwendungen macht, bei denen die Rechenressourcen begrenzt sind. Trotz ihrer kleineren Größe können sie eine Vielzahl von Aufgaben ausführen. In der Regel werden SLMs durch Kompression oder Destillation von LLMs aufgebaut, mit dem Ziel, einen erheblichen Teil der ursprünglichen Funktionalität und sprachlichen Fähigkeiten des Modells zu erhalten. Diese Verringerung der Modellgröße verringert die Gesamtkonplexität, was SLMs sowohl in Bezug auf Speicherverbrauch als auch Rechenanforderungen effizienter macht. Trotz dieser Optimierungen können SLMs eine breite Palette von Aufgaben der natürlichen Sprachverarbeitung (NLP) ausführen:

- Textgenerierung: Erstellen von kohärenten und kontextuell relevanten Sätzen oder Absätzen.
- Textvervollständigung: Vorhersage und Vervollständigung von Sätzen basierend auf einer gegebenen Eingabe.
- Übersetzung: Umwandlung von Text von einer Sprache in eine andere.
- Zusammenfassung: Verdichtung langer Textstücke zu kürzeren, leichter verdaulichen Zusammenfassungen.

Wenn auch mit einigen Kompromissen in Bezug auf Leistung oder Verständnis im Vergleich zu ihren größeren Gegenstücken. 

## Wie funktionieren kleine Sprachmodelle?
SLMs werden mit großen Mengen an Textdaten trainiert. Während des Trainings lernen sie die Muster und Strukturen der Sprache, was es ihnen ermöglicht, Text zu generieren, der sowohl grammatikalisch korrekt als auch kontextuell passend ist. Der Trainingsprozess umfasst:

- Datensammlung: Sammlung großer Textdatensätze aus verschiedenen Quellen.
- Vorverarbeitung: Reinigung und Organisation der Daten, um sie für das Training geeignet zu machen.
- Training: Einsatz von maschinellen Lernalgorithmen, um dem Modell beizubringen, Text zu verstehen und zu generieren.
- Feinabstimmung: Anpassung des Modells zur Verbesserung der Leistung bei spezifischen Aufgaben.

Die Entwicklung von SLMs entspricht dem zunehmenden Bedarf an Modellen, die in ressourcenbeschränkten Umgebungen eingesetzt werden können, wie z. B. mobilen Geräten oder Edge-Computing-Plattformen, wo vollwertige LLMs aufgrund ihres hohen Ressourcenverbrauchs unpraktisch sein können. Durch die Fokussierung auf Effizienz balancieren SLMs Leistung mit Zugänglichkeit und ermöglichen einen breiteren Einsatz in verschiedenen Bereichen.

![slm](../../../translated_images/de/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Lernziele

In dieser Lektion möchten wir Wissen über SLM vermitteln und es mit Microsoft Phi-3 kombinieren, um verschiedene Szenarien in Textinhalten, Vision und MoE kennenzulernen.

Am Ende dieser Lektion sollten Sie in der Lage sein, folgende Fragen zu beantworten:

- Was ist ein SLM?
- Was ist der Unterschied zwischen SLM und LLM?
- Was ist die Microsoft Phi-3/3.5 Familie?
- Wie führt man Inferenz mit der Microsoft Phi-3/3.5 Familie durch?

Bereit? Dann legen wir los.

## Unterschiede zwischen großen Sprachmodellen (LLMs) und kleinen Sprachmodellen (SLMs)

Sowohl LLMs als auch SLMs basieren auf grundlegenden Prinzipien des probabilistischen maschinellen Lernens und verfolgen ähnliche Ansätze in ihrem architektonischen Design, Training, Datengenerierung und Modellevaluierung. Es gibt jedoch einige Schlüsselfaktoren, die diese beiden Modelltypen unterscheiden.

## Anwendungen von kleinen Sprachmodellen

SLMs haben ein breites Anwendungsspektrum, darunter:

- Chatbots: Bereitstellung von Kundensupport und Interaktion mit Nutzern in gesprächsartiger Form.
- Inhaltserstellung: Unterstützung von Autoren beim Generieren von Ideen oder sogar beim Entwurf ganzer Artikel.
- Bildung: Unterstützung von Schülern bei Schreibaufgaben oder beim Erlernen neuer Sprachen.
- Barrierefreiheit: Erstellung von Tools für Menschen mit Behinderungen, z. B. Text-zu-Sprache-Systeme.

**Größe**
  
Ein Hauptunterschied zwischen LLMs und SLMs liegt in der Modellgröße. LLMs wie ChatGPT (GPT-4) können schätzungsweise 1,76 Billionen Parameter umfassen, während Open-Source-SLMs wie Mistral 7B mit deutlich weniger Parametern – etwa 7 Milliarden – konzipiert sind. Diese Diskrepanz liegt hauptsächlich an Unterschieden in der Modellarchitektur und den Trainingsverfahren. Beispielsweise verwendet ChatGPT einen Self-Attention-Mechanismus innerhalb eines Encoder-Decoder-Rahmens, während Mistral 7B eine Sliding-Window-Attention nutzt, die effizienteres Training in einem reinen Decoder-Modell ermöglicht. Diese architektonische Variation hat tiefgreifende Auswirkungen auf die Komplexität und Leistung dieser Modelle.

**Verständnis**

SLMs sind typischerweise auf Leistung innerhalb spezifischer Domänen optimiert, wodurch sie hochspezialisiert, aber möglicherweise eingeschränkt in ihrer Fähigkeit sind, ein breites kontextuelles Verständnis über mehrere Wissensgebiete hinweg zu bieten. Im Gegensatz dazu zielen LLMs darauf ab, menschenähnliche Intelligenz auf umfassenderem Niveau zu simulieren. Sie werden auf großen, vielfältigen Datensätzen trainiert und sind darauf ausgelegt, in verschiedenen Domänen gut zu funktionieren, was ihnen größere Vielseitigkeit und Anpassungsfähigkeit verleiht. Folglich sind LLMs besser geeignet für ein breites Spektrum an nachgelagerten Aufgaben, wie natürliche Sprachverarbeitung und Programmierung.

**Rechenleistung**

Das Training und der Einsatz von LLMs sind ressourcenintensive Prozesse, die oft umfangreiche Recheninfrastruktur erfordern, einschließlich groß angelegter GPU-Cluster. Zum Beispiel kann das Training eines Modells wie ChatGPT von Grund auf Tausende von GPUs über einen langen Zeitraum benötigen. Im Gegensatz dazu sind SLMs mit ihrer geringeren Parameterzahl in Bezug auf Rechenressourcen leichter zugänglich. Modelle wie Mistral 7B können auf lokalen Maschinen mit moderaten GPU-Fähigkeiten trainiert und betrieben werden, obwohl das Training dennoch mehrere Stunden auf mehreren GPUs in Anspruch nimmt.

**Bias**

Bias ist ein bekanntes Problem bei LLMs, das vor allem durch die Natur der Trainingsdaten bedingt ist. Diese Modelle verlassen sich oft auf rohe, öffentlich verfügbare Daten aus dem Internet, die bestimmte Gruppen unterrepräsentieren oder falsch darstellen können, fehlerhafte Etikettierungen enthalten oder durch sprachliche Verzerrungen geprägt sind, die durch Dialekte, geographische Unterschiede und grammatikalische Regeln beeinflusst werden. Darüber hinaus kann die Komplexität von LLM-Architekturen unbeabsichtigt Bias verstärken, der ohne sorgfältige Feinabstimmung unbemerkt bleibt. SLMs hingegen, die auf stärker eingeschränkten, domänenspezifischen Datensätzen trainiert werden, sind von Natur aus weniger anfällig für solche Bias, jedoch nicht vollständig immun dagegen.

**Inference**

Die reduzierte Größe von SLMs verschafft ihnen einen erheblichen Vorteil hinsichtlich der Inferenzgeschwindigkeit, sodass sie Ausgaben effizient auf lokaler Hardware generieren können, ohne umfangreiche parallele Verarbeitung zu benötigen. LLMs hingegen benötigen aufgrund ihrer Größe und Komplexität oft erhebliche parallele Rechenressourcen, um akzeptable Inferenzzeiten zu erreichen. Die Anwesenheit mehrerer gleichzeitiger Nutzer verlangsamt die Antwortzeiten von LLMs insbesondere beim großflächigen Einsatz zusätzlich.

Zusammenfassend lässt sich sagen, dass LLMs und SLMs zwar eine gemeinsame Grundlage im maschinellen Lernen haben, sich jedoch deutlich in Modellgröße, Ressourcenbedarf, kontextuellem Verständnis, Anfälligkeit für Bias und Inferenzgeschwindigkeit unterscheiden. Diese Unterschiede spiegeln ihre jeweilige Eignung für unterschiedliche Anwendungsfälle wider, wobei LLMs vielseitiger, aber ressourcenintensiver sind, und SLMs spezifischere Effizienz mit reduziertem Rechenaufwand bieten.

***Hinweis: In dieser Lektion stellen wir SLM am Beispiel von Microsoft Phi-3 / 3.5 vor.***

## Vorstellung der Phi-3 / Phi-3.5 Familie

Die Phi-3 / 3.5 Familie richtet sich hauptsächlich an Text-, Vision- und Agenten-(MoE)-Anwendungsszenarien:

### Phi-3 / 3.5 Instruct

Hauptsächlich für Textgenerierung, Chatvervollständigung und Extraktion von Inhalten.

**Phi-3-mini**

Das 3,8B Sprachmodell ist auf Microsoft Foundry, Hugging Face und Ollama verfügbar. Phi-3-Modelle übertreffen Sprachmodelle gleicher und größerer Größe deutlich auf wichtigen Benchmarks (siehe unten Benchmark-Zahlen, höhere Werte sind besser). Phi-3-mini übertrifft Modelle mit doppelter Größe, während Phi-3-small und Phi-3-medium größere Modelle, einschließlich GPT-3.5, schlagen.

**Phi-3-small & medium**

Mit nur 7 Milliarden Parametern übertrifft Phi-3-small GPT-3.5T in einer Vielzahl von Sprach-, Denk-, Programmier- und Mathematik-Benchmarks.

Das Phi-3-medium mit 14 Milliarden Parametern setzt diesen Trend fort und übertrifft das Gemini 1.0 Pro.

**Phi-3.5-mini**

Man kann es als Upgrade von Phi-3-mini betrachten. Die Parameter bleiben unverändert, aber es verbessert die Fähigkeit, mehrere Sprachen zu unterstützen (unterstützt über 20 Sprachen: Arabisch, Chinesisch, Tschechisch, Dänisch, Niederländisch, Englisch, Finnisch, Französisch, Deutsch, Hebräisch, Ungarisch, Italienisch, Japanisch, Koreanisch, Norwegisch, Polnisch, Portugiesisch, Russisch, Spanisch, Schwedisch, Thailändisch, Türkisch, Ukrainisch) und bietet stärkere Unterstützung für lange Kontexte.

Phi-3.5-mini mit 3,8 Milliarden Parametern übertrifft Sprachmodelle gleicher Größe und ist vergleichbar mit Modellen, die doppelt so groß sind.

### Phi-3 / 3.5 Vision

Man kann das Instruct-Modell von Phi-3/3.5 als Phis Fähigkeit zum Verstehen ansehen, und Vision ist das, was Phi Augen gibt, um die Welt zu verstehen.


**Phi-3-Vision**

Phi-3-Vision mit nur 4,2 Milliarden Parametern setzt diesen Trend fort und übertrifft größere Modelle wie Claude-3 Haiku und Gemini 1.0 Pro V in allgemeinen visuellen Denkaufgaben, OCR sowie in Tabellen- und Diagrammverständnis.


**Phi-3.5-Vision**

Phi-3.5-Vision ist ebenfalls ein Upgrade von Phi-3-Vision und fügt Unterstützung für mehrere Bilder hinzu. Man kann es als Verbesserung der Vision ansehen: Es kann nicht nur Bilder, sondern auch Videos sehen.

Phi-3.5-Vision übertrifft größere Modelle wie Claude-3.5 Sonnet und Gemini 1.5 Flash bei OCR-, Tabellen- und Diagrammverständnis und ist vergleichbar bei allgemeinen visuellen Wissensdenkaufgaben. Es unterstützt Multi-Frame-Eingaben, d. h. es kann auf mehreren Eingabebildern gleichzeitig Schlüsse ziehen.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ermöglicht es Modellen, mit deutlich weniger Rechenleistung vortrainiert zu werden, was bedeutet, dass man die Modell- oder Datensatzgröße mit dem gleichen Rechenbudget wie bei einem dichten Modell drastisch skalieren kann. Insbesondere sollte ein MoE-Modell während des Vortrainings die gleiche Qualität wie sein dichtes Pendant viel schneller erreichen.

Phi-3.5-MoE besteht aus 16x3,8B Expertenmodulen. Phi-3.5-MoE mit nur 6,6 Milliarden aktiven Parametern erreicht ein ähnliches Niveau bei Denkaufgaben, Sprachverständnis und Mathematik wie deutlich größere Modelle.

Wir können das Phi-3/3.5-Familienmodell je nach Szenario verwenden. Im Gegensatz zu LLMs können Sie Phi-3/3.5-mini oder Phi-3/3.5-Vision auf Edge-Geräten bereitstellen.


## Nutzung der Phi-3/3.5 Familienmodelle

Wir möchten Phi-3/3.5 in verschiedenen Szenarien verwenden. Im Folgenden werden wir Phi-3/3.5 basierend auf unterschiedlichen Szenarien einsetzen.

![phi3](../../../translated_images/de/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenz über Cloud-APIs

**Microsoft Foundry Modelle**

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ist der direkte Ersatz.

Microsoft Foundry Modelle sind der direkteste Weg. Sie können schnell auf das Phi-3/3.5-Instruct-Modell über den Foundry-Modellkatalog zugreifen. Kombiniert mit dem Azure AI Inference SDK / OpenAI SDK können Sie die API über Code ansprechen, um den Phi-3/3.5-Instruct-Aufruf zu erledigen. Sie können auch verschiedene Effekte über den Playground testen.

- Demo: Vergleich der Effekte von Phi-3-mini und Phi-3.5-mini in chinesischen Szenarien

![phi3](../../../translated_images/de/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/de/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Wenn Sie hingegen die Vision- und MoE-Modelle verwenden möchten, können Sie Microsoft Foundry für den Aufruf nutzen. Wenn Sie interessiert sind, können Sie das Phi-3 Kochbuch lesen, um zu erfahren, wie man Phi-3/3.5 Instruct, Vision, MoE über Microsoft Foundry aufruft [Klicken Sie auf diesen Link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Zusätzlich zum cloudbasierten Microsoft Foundry Modellkatalog können Sie auch [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) verwenden, um entsprechende Aufrufe durchzuführen. Sie können NVIDIA NIM besuchen, um API-Aufrufe für die Phi-3/3.5 Familie durchzuführen. NVIDIA NIM (NVIDIA Inference Microservices) ist eine Sammlung beschleunigter Inferenz-Microservices, die Entwicklern helfen, KI-Modelle effizient in verschiedenen Umgebungen einzusetzen, einschließlich Clouds, Rechenzentren und Workstations.

Hier einige wichtige Funktionen von NVIDIA NIM:

- **Einfache Bereitstellung:** NIM ermöglicht die Bereitstellung von KI-Modellen mit einem einzigen Befehl, was die Integration in bestehende Arbeitsabläufe vereinfacht.
- **Optimierte Leistung:** Es nutzt voroptimierte Inferenz-Engines von NVIDIA, wie TensorRT und TensorRT-LLM, um geringe Latenz und hohe Durchsatzraten zu gewährleisten.
- **Skalierbarkeit:** NIM unterstützt Autoscaling auf Kubernetes und kann somit unterschiedlichen Arbeitslasten effektiv gerecht werden.
- **Sicherheit und Kontrolle:** Organisationen können durch das selbstverwaltete Hosting der NIM-Microservices auf ihrer eigenen Infrastruktur die Kontrolle über ihre Daten und Anwendungen behalten.
- **Standard-APIs:** NIM stellt branchenübliche APIs bereit, die den Aufbau und die Integration von KI-Anwendungen wie Chatbots, KI-Assistenten und mehr erleichtern.

NIM ist Teil von NVIDIA AI Enterprise, das darauf abzielt, die Bereitstellung und Operationalisierung von KI-Modellen zu vereinfachen und sicherzustellen, dass sie effizient auf NVIDIA-GPUs ausgeführt werden.

- Demo: Verwendung von NVIDIA NIM zur Anbindung der Phi-3.5-Vision-API  [[Klicken Sie auf diesen Link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokales Ausführen von Phi-3/3.5
Inferenz im Zusammenhang mit Phi-3 oder einem beliebigen Sprachmodell wie GPT-3 bezeichnet den Prozess der Erzeugung von Antworten oder Vorhersagen basierend auf den empfangenen Eingaben. Wenn Sie Phi-3 eine Eingabeaufforderung oder Frage geben, verwendet es sein trainiertes neuronales Netzwerk, um durch Analyse von Mustern und Zusammenhängen in den Trainingsdaten die wahrscheinlichste und relevanteste Antwort abzuleiten.

**Hugging Face Transformer**
Hugging Face Transformers ist eine leistungsstarke Bibliothek, die für Aufgaben der natürlichen Sprachverarbeitung (NLP) und andere maschinelle Lernaufgaben entwickelt wurde. Hier einige wichtige Punkte:

1. **Vortrainierte Modelle**: Sie bietet tausende vortrainierte Modelle für verschiedene Aufgaben wie Textklassifikation, Named Entity Recognition, Fragebeantwortung, Zusammenfassung, Übersetzung und Textgenerierung.

2. **Framework-Interoperabilität**: Die Bibliothek unterstützt mehrere Deep-Learning-Frameworks, darunter PyTorch, TensorFlow und JAX. So können Sie ein Modell in einem Framework trainieren und in einem anderen verwenden.

3. **Multimodale Fähigkeiten**: Neben NLP unterstützt Hugging Face Transformers auch Aufgaben in der Computer Vision (z. B. Bildklassifikation, Objekterkennung) und Audiobearbeitung (z. B. Spracherkennung, Audioklassifikation).

4. **Benutzerfreundlichkeit**: Die Bibliothek bietet APIs und Werkzeuge, um Modelle einfach herunterzuladen und feinzujustieren, was sie sowohl für Anfänger als auch Experten zugänglich macht.

5. **Community und Ressourcen**: Hugging Face verfügt über eine lebhafte Community sowie umfangreiche Dokumentationen, Tutorials und Anleitungen, um Nutzern den Einstieg zu erleichtern und die Bibliothek effektiv zu nutzen.
[offizielle Dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oder deren [GitHub-Repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dies ist die am häufigsten genutzte Methode, erfordert jedoch auch GPU-Beschleunigung. Szenarien wie Vision und MoE benötigen schließlich viele Berechnungen, die auf der CPU ohne Quantisierung sehr langsam sind.


- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Instruct [Klicken Sie auf diesen Link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-Vision [Klicken Sie auf diesen Link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufruf von Phi-3.5-MoE [Klicken Sie auf diesen Link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ist eine Plattform, die es einfacher macht, große Sprachmodelle (LLMs) lokal auf Ihrem Rechner auszuführen. Sie unterstützt verschiedene Modelle wie Llama 3.1, Phi 3, Mistral und Gemma 2 unter anderem. Die Plattform vereinfacht den Prozess, indem sie Modellgewichte, Konfiguration und Daten in einem Paket bündelt, sodass Nutzer ihre eigenen Modelle einfacher anpassen und erstellen können. Ollama ist für macOS, Linux und Windows verfügbar. Es ist ein großartiges Werkzeug, wenn Sie mit LLMs experimentieren oder diese bereitstellen möchten, ohne auf Cloud-Dienste angewiesen zu sein. Ollama ist der direkteste Weg; Sie müssen lediglich den folgenden Befehl ausführen.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ist Microsofts Offline-Laufzeitumgebung auf dem Gerät zum Ausführen von Modellen wie Phi vollständig auf Ihrer eigenen Hardware - kein Azure-Abonnement, kein API-Schlüssel oder Netzwerk erforderlich. Es wählt automatisch den besten verfügbaren Ausführungsprovider (NPU, GPU oder CPU) aus und stellt einen zu OpenAI-kompatiblen Endpunkt bereit, sodass existierender `openai`/Azure AI Inference SDK-Code mit minimalen Änderungen darauf verweisen kann. Siehe die [Foundry Local-Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ist ein plattformübergreifender Beschleuniger für Inferenz und Training im maschinellen Lernen. ONNX Runtime für Generative AI (GENAI) ist ein leistungsfähiges Tool, das Ihnen hilft, generative KI-Modelle effizient auf verschiedenen Plattformen auszuführen. 

## Was ist ONNX Runtime?
ONNX Runtime ist ein Open-Source-Projekt, das eine Hochleistungsinferenz von maschinellen Lernmodellen ermöglicht. Es unterstützt Modelle im Open Neural Network Exchange (ONNX)-Format, einem Standard für die Darstellung von maschinellen Lernmodellen. ONNX Runtime-Inferenz kann schnellere Kundenerlebnisse und geringere Kosten ermöglichen und unterstützt Modelle aus Deep-Learning-Frameworks wie PyTorch und TensorFlow/Keras sowie klassische maschinelle Lernbibliotheken wie scikit-learn, LightGBM, XGBoost usw. ONNX Runtime ist kompatibel mit unterschiedlicher Hardware, Treibern und Betriebssystemen und bietet optimale Leistung durch Nutzung von Hardwarebeschleunigern, sofern verfügbar, neben Graphoptimierungen und -transformationen.

## Was ist Generative KI?
Generative KI bezieht sich auf KI-Systeme, die neue Inhalte wie Texte, Bilder oder Musik basierend auf den Daten erzeugen können, auf denen sie trainiert wurden. Beispiele sind Sprachmodelle wie GPT-3 und Bildgenerierungsmodelle wie Stable Diffusion. Die ONNX Runtime für GenAI-Bibliothek stellt den generativen KI-Loop für ONNX-Modelle bereit, einschließlich der Inferenz mit ONNX Runtime, Logits-Verarbeitung, Suche und Sampling sowie KV-Cache-Verwaltung.

## ONNX Runtime für GENAI
ONNX Runtime für GENAI erweitert die Fähigkeiten von ONNX Runtime zur Unterstützung generativer KI-Modelle. Hier einige Hauptmerkmale:

- **Breite Plattformunterstützung:** Es funktioniert auf verschiedenen Plattformen, darunter Windows, Linux, macOS, Android und iOS.
- **Modellunterstützung:** Es unterstützt viele beliebte generative KI-Modelle wie LLaMA, GPT-Neo, BLOOM und mehr.
- **Leistungsoptimierung:** Es enthält Optimierungen für verschiedene Hardwarebeschleuniger wie NVIDIA-GPUs, AMD-GPUs und weitere2.
- **Benutzerfreundlichkeit:** Es bietet APIs für eine einfache Integration in Anwendungen, mit denen Sie Texte, Bilder und andere Inhalte mit minimalem Code erzeugen können.
- Nutzer können eine Methode generate() auf höherer Ebene aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei jeweils ein Token generiert und optional Generierungsparameter innerhalb der Schleife aktualisiert werden.
- ONNX Runtime unterstützt zudem Greedy-/Beam-Suche und TopP-, TopK-Sampling zur Erzeugung von Token-Sequenzen sowie eingebaute Logits-Verarbeitung wie Wiederholungsstrafen. Sie können auch leicht benutzerdefinierte Scoring-Methoden hinzufügen.

## Einstieg
Um mit ONNX Runtime für GENAI zu starten, können Sie folgende Schritte ausführen:

### Installieren Sie ONNX Runtime:
```Python
pip install onnxruntime
```
### Installieren Sie die Generative AI-Erweiterungen:
```Python
pip install onnxruntime-genai
```

### Führen Sie ein Modell aus: Hier ein einfaches Beispiel in Python:
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
### Demo: Verwendung von ONNX Runtime GenAI zur Anbindung von Phi-3.5-Vision


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

Neben den Referenzmethoden ONNX Runtime, Ollama und Foundry Local können wir auch Referenzen zu quantitativen Modellen auf der Basis der von verschiedenen Herstellern bereitgestellten Modellreferenzmethoden vervollständigen. Beispielsweise Apple MLX Framework mit Apple Metal, Qualcomm QNN mit NPU, Intel OpenVINO mit CPU/GPU usw. Weitere Inhalte finden Sie auch im [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Mehr

Wir haben die Grundlagen der Phi-3/3.5-Familie kennengelernt, aber um mehr über SLM zu erfahren, benötigen wir weiteres Wissen. Die Antworten finden Sie im Phi-3 Cookbook. Wenn Sie mehr erfahren möchten, besuchen Sie bitte das [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->