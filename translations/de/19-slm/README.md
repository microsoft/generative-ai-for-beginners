# Einführung in kleine Sprachmodelle für generative KI für Anfänger
Generative KI ist ein faszinierendes Gebiet der künstlichen Intelligenz, das sich auf die Erstellung von Systemen konzentriert, die in der Lage sind, neue Inhalte zu generieren. Diese Inhalte können von Text und Bildern über Musik bis hin zu ganzen virtuellen Umgebungen reichen. Eine der spannendsten Anwendungen der generativen KI liegt im Bereich der Sprachmodelle.

## Was sind kleine Sprachmodelle?

Ein kleines Sprachmodell (SLM) stellt eine verkleinerte Variante eines großen Sprachmodells (LLM) dar, das viele der architektonischen Prinzipien und Techniken von LLMs nutzt, dabei jedoch einen deutlich reduzierten Rechenaufwand aufweist.

SLMs sind eine Untergruppe von Sprachmodellen, die darauf ausgelegt sind, menschenähnlichen Text zu generieren. Im Gegensatz zu ihren größeren Pendants wie GPT-4 sind SLMs kompakter und effizienter, was sie ideal für Anwendungen macht, bei denen die Rechenressourcen begrenzt sind. Trotz ihrer kleineren Größe können sie dennoch verschiedene Aufgaben erfüllen. Typischerweise werden SLMs durch Komprimierung oder Destillation von LLMs gebaut, um einen erheblichen Teil der ursprünglichen Funktionalität und sprachlichen Fähigkeiten des Modells zu erhalten. Diese Verringerung der Modellgröße reduziert die Gesamtkonplexität, wodurch SLMs sowohl in Bezug auf Speicherverbrauch als auch auf Rechenanforderungen effizienter sind. Trotz dieser Optimierungen können SLMs weiterhin eine breite Palette von Aufgaben der Verarbeitung natürlicher Sprache (NLP) erledigen:

- Textgenerierung: Erstellung kohärenter und kontextuell relevanter Sätze oder Absätze.
- Textvervollständigung: Vorhersage und Ergänzung von Sätzen auf Basis eines vorgegebenen Prompts.
- Übersetzung: Umwandlung von Text von einer Sprache in eine andere.
- Zusammenfassung: Verdichtung langer Texte in kürzere, leichter verdauliche Zusammenfassungen.

Allerdings mit einigen Abstrichen in Bezug auf Leistung oder Tiefgang im Vergleich zu ihren größeren Pendants.

## Wie funktionieren kleine Sprachmodelle?
SLMs werden mit großen Mengen an Textdaten trainiert. Während des Trainings lernen sie die Muster und Strukturen der Sprache kennen, was es ihnen ermöglicht, Texte zu generieren, die sowohl grammatikalisch korrekt als auch kontextuell passend sind. Der Trainingsprozess umfasst:

- Datensammlung: Erfassung großer Textdatensätze aus verschiedenen Quellen.
- Vorverarbeitung: Bereinigung und Organisation der Daten, um sie für das Training geeignet zu machen.
- Training: Einsatz von maschinellen Lernalgorithmen, um dem Modell beizubringen, wie man Text versteht und generiert.
- Feinabstimmung: Anpassung des Modells, um dessen Leistung in speziellen Aufgaben zu verbessern.

Die Entwicklung von SLMs steht im Einklang mit dem steigenden Bedarf an Modellen, die in ressourcenbeschränkten Umgebungen eingesetzt werden können, wie etwa auf mobilen Geräten oder Edge-Computing-Plattformen, wo groß angelegte LLMs aufgrund ihres hohen Ressourcenbedarfs oft ungeeignet sind. Durch die Fokussierung auf Effizienz balancieren SLMs Leistung und Zugänglichkeit aus und ermöglichen breitere Anwendungen in verschiedenen Bereichen.

![slm](../../../translated_images/de/slm.4058842744d0444a.webp)

## Lernziele

In dieser Lektion möchten wir das Wissen über SLM vermitteln und es mit Microsoft Phi-3 verbinden, um verschiedene Szenarien in Textinhalten, Vision und MoE kennenzulernen.

Am Ende dieser Lektion sollten Sie folgende Fragen beantworten können:

- Was ist SLM?
- Was ist der Unterschied zwischen SLM und LLM?
- Was ist die Microsoft Phi-3/3.5 Familie?
- Wie führt man Inferenz mit der Microsoft Phi-3/3.5 Familie durch?

Bereit? Dann legen wir los.

## Die Unterschiede zwischen großen Sprachmodellen (LLMs) und kleinen Sprachmodellen (SLMs)

Sowohl LLMs als auch SLMs basieren auf grundlegenden Prinzipien des probabilistischen maschinellen Lernens und folgen ähnlichen Ansätzen in ihrer architektonischen Gestaltung, Trainingsmethoden, Datengenerierungsprozessen und Modellauswertungstechniken. Dennoch unterscheiden sich diese beiden Modelltypen in mehreren wichtigen Punkten.

## Anwendungsbereiche kleiner Sprachmodelle

SLMs finden eine breite Palette von Anwendungen, darunter:

- Chatbots: Bereitstellung von Kundensupport und Interaktion mit Nutzern in Gesprächsform.
- Inhaltserstellung: Unterstützung von Autoren durch Generierung von Ideen oder sogar kompletten Artikeln.
- Bildung: Hilfestellung für Schüler bei Schreibaufgaben oder beim Erlernen neuer Sprachen.
- Barrierefreiheit: Erstellung von Tools für Menschen mit Behinderungen, wie Text-zu-Sprache-Systeme.

**Größe**
  
Ein Hauptunterschied zwischen LLMs und SLMs liegt im Umfang der Modelle. LLMs, wie ChatGPT (GPT-4), können schätzungsweise 1,76 Billionen Parameter umfassen, während Open-Source-SLMs wie Mistral 7B mit deutlich weniger Parametern auskommen – etwa 7 Milliarden. Diese Diskrepanz beruhte hauptsächlich auf Unterschieden in Architektur und Trainingsprozessen. Beispielsweise verwendet ChatGPT einen Selbst-Attention-Mechanismus innerhalb eines Encoder-Decoder-Frameworks, wohingegen Mistral 7B Schiebefenster-Attention nutzt, was ein effizienteres Training in einem reinen Decoder-Modell ermöglicht. Diese architektonische Variation hat tiefgreifende Auswirkungen auf die Komplexität und Leistung dieser Modelle.

**Verständnis**

SLMs sind typischerweise für die Leistung in spezifischen Domänen optimiert, was sie hochspezialisiert, aber potenziell eingeschränkt in der Fähigkeit macht, ein breites kontextuelles Verständnis über verschiedene Wissensfelder hinweg anzubieten. Im Gegensatz dazu zielen LLMs darauf ab, menschliche Intelligenz umfassender zu simulieren. Trainiert an umfangreichen, vielfältigen Datensätzen, sind LLMs darauf ausgelegt, in verschiedenen Bereichen gut zu funktionieren und bieten größere Vielseitigkeit und Anpassungsfähigkeit. Folglich eignen sich LLMs besser für eine breitere Palette von nachgelagerten Aufgaben wie natürlicher Sprachverarbeitung und Programmierung.

**Rechenleistung**

Das Training und der Einsatz von LLMs sind ressourcenintensive Prozesse, die oft eine erhebliche Infrastruktur an Rechenleistung, einschließlich großflächiger GPU-Cluster, erfordern. So könnte das Training eines Modells wie ChatGPT von Grund auf Tausende von GPUs über einen längeren Zeitraum benötigen. Im Gegensatz dazu sind SLMs mit ihren geringeren Parameteranzahlen hinsichtlich Rechenressourcen zugänglicher. Modelle wie Mistral 7B können auf lokalen Rechnern mit moderaten GPU-Fähigkeiten trainiert und ausgeführt werden, wenngleich das Training noch mehrere Stunden auf mehreren GPUs in Anspruch nimmt.

**Bias**

Verzerrungen sind ein bekanntes Problem bei LLMs, hauptsächlich bedingt durch die Beschaffenheit der Trainingsdaten. Diese Modelle stützen sich oft auf rohe, öffentlich verfügbare Daten aus dem Internet, die bestimmte Gruppen unterrepräsentieren oder falsch darstellen, fehlerhafte Beschriftungen enthalten oder sprachliche Vorurteile widerspiegeln, die durch Dialekte, geografische Unterschiede und Grammatikregeln beeinflusst sind. Darüber hinaus kann die Komplexität der LLM-Architektur unbeabsichtigt Verzerrungen verstärken, die ohne sorgfältige Feinabstimmung unerkannt bleiben können. Dagegen sind SLMs, die auf enger gefassten, domänenspezifischen Datensätzen trainiert werden, von Natur aus weniger anfällig für solche Verzerrungen, wenngleich sie nicht völlig frei davon sind.

**Inference**

Die reduzierte Größe der SLMs verschafft ihnen einen erheblichen Vorteil bei der Inferenzgeschwindigkeit, wodurch sie Ausgaben effizient auf lokaler Hardware erzeugen können, ohne umfangreiche parallele Verarbeitung zu benötigen. LLMs hingegen erfordern aufgrund ihrer Größe und Komplexität oft erhebliche parallele Rechenressourcen, um akzeptable Inferenzzeiten zu erzielen. Die gleichzeitige Nutzung durch mehrere Benutzer verlangsamt die Antwortzeiten von LLMs insbesondere bei großskaliger Bereitstellung weiter.

Zusammenfassend lässt sich sagen, dass zwar sowohl LLMs als auch SLMs auf einer gemeinsamen maschinellen Lernbasis beruhen, sie sich jedoch deutlich in Modellgröße, Ressourcenbedarf, kontextuellem Verständnis, Anfälligkeit für Verzerrungen und Inferenzgeschwindigkeit unterscheiden. Diese Unterschiede spiegeln ihre jeweilige Eignung für verschiedene Anwendungsfälle wider, wobei LLMs vielseitiger, aber ressourcenintensiver sind, während SLMs spezifischere Effizienz mit geringeren Rechenanforderungen bieten.

***Hinweis: In dieser Lektion stellen wir SLM anhand von Microsoft Phi-3 / 3.5 als Beispiel vor.***

## Einführung in die Phi-3 / Phi-3.5 Familie

Die Phi-3 / 3.5 Familie richtet sich hauptsächlich an Text-, Vision- und Agenten-(MoE)-Anwendungsszenarien:

### Phi-3 / 3.5 Instruct

Hauptsächlich für Textgenerierung, Chat-Vervollständigung und Inhaltsinformations-Extraktion usw.

**Phi-3-mini**

Das 3,8-Milliarden-Parameter-Sprachmodell ist auf Microsoft Foundry, Hugging Face und Ollama verfügbar. Phi-3-Modelle übertreffen Sprachmodelle gleicher und größerer Größenordnungen bei Schlüssel-Benchmarks deutlich (siehe unten die Benchmark-Zahlen, höhere Zahlen sind besser). Phi-3-mini übertrifft Modelle der doppelten Größe, während Phi-3-small und Phi-3-medium größere Modelle schlagen, einschließlich GPT-3.5.

**Phi-3-small & medium**

Mit nur 7 Milliarden Parametern schlägt Phi-3-small GPT-3.5T bei einer Vielzahl an Sprach-, Denk-, Programmier- und Mathe-Benchmarks.

Phi-3-medium mit 14 Milliarden Parametern setzt diesen Trend fort und übertrifft Gemini 1.0 Pro.

**Phi-3.5-mini**

Wir können es als ein Upgrade von Phi-3-mini sehen. Während die Parameterzahl unverändert bleibt, verbessert es die Fähigkeit, mehrere Sprachen zu unterstützen (über 20 Sprachen: Arabisch, Chinesisch, Tschechisch, Dänisch, Niederländisch, Englisch, Finnisch, Französisch, Deutsch, Hebräisch, Ungarisch, Italienisch, Japanisch, Koreanisch, Norwegisch, Polnisch, Portugiesisch, Russisch, Spanisch, Schwedisch, Thailändisch, Türkisch, Ukrainisch) und bietet stärkere Unterstützung für langen Kontext.

Phi-3.5-mini mit 3,8 Milliarden Parametern übertrifft Sprachmodelle gleicher Größe und ist mit Modellen der doppelten Größe vergleichbar.

### Phi-3 / 3.5 Vision

Wir können das Instruct-Modell von Phi-3/3.5 als Phis Fähigkeit zum Verstehen sehen, und Vision ist das, was Phi Augen verleiht, um die Welt zu verstehen.


**Phi-3-Vision**

Phi-3-Vision mit nur 4,2 Milliarden Parametern setzt diesen Trend fort und übertrifft größere Modelle wie Claude-3 Haiku und Gemini 1.0 Pro V bei allgemeinen visuellen Denkaufgaben, OCR sowie bei Tabellen- und Diagrammverständnisaufgaben.


**Phi-3.5-Vision**

Phi-3.5-Vision ist ebenfalls ein Upgrade von Phi-3-Vision und ergänzt Mehrbildunterstützung. Man kann es als Verbesserung in der Vision betrachten: Es kann nicht nur Bilder, sondern auch Videos „sehen“.

Phi-3.5-Vision übertrifft größere Modelle wie Claude-3.5 Sonnet und Gemini 1.5 Flash bei OCR-, Tabellen- und Diagramm-Verständnisaufgaben und ist bei allgemeinen visuellen Wissens-Denkaufgaben vergleichbar. Es unterstützt Mehrfach-Frame-Eingaben, d.h. es kann Überlegungen zu mehreren Eingabebildern anstellen.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ermöglicht es, Modelle mit wesentlich geringerem Rechenaufwand vorzutrainieren, was bedeutet, dass man Modell- oder Datensatzgrößen mit demselben Rechenbudget dramatisch skalieren kann wie bei einem dichten Modell. Insbesondere sollte ein MoE-Modell während des Vortrainings schneller dieselbe Qualität wie sein dichtes Pendant erreichen.

Phi-3.5-MoE besteht aus 16x 3,8 Milliarden Expertenmodulen. Phi-3.5-MoE erreicht mit nur 6,6 Milliarden aktiven Parametern ein ähnliches Niveau in Denken, Sprachverständnis und Mathematik wie deutlich größere Modelle.

Wir können das Phi-3/3.5-Familienmodell je nach Szenario einsetzen. Im Gegensatz zu LLMs können Sie Phi-3/3.5-mini oder Phi-3/3.5-Vision auf Edge-Geräten bereitstellen.


## Wie man Phi-3/3.5 Familienmodelle verwendet

Wir beabsichtigen, Phi-3/3.5 in verschiedenen Szenarien zu nutzen. Im Folgenden verwenden wir Phi-3/3.5 basierend auf unterschiedlichen Anwendungsfällen.

![phi3](../../../translated_images/de/phi3.655208c3186ae381.webp)

### Inferenz über Cloud APIs

**Microsoft Foundry Modelle**

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ist der direkte Ersatz.

Microsoft Foundry Modelle sind der direkteste Weg. Sie können schnell auf das Phi-3/3.5-Instruct-Modell über den Foundry Modellkatalog zugreifen. Kombiniert mit dem Azure AI Inference SDK / OpenAI SDK können Sie die API über Code ansprechen, um den Phi-3/3.5-Instruct-Aufruf durchzuführen. Außerdem können Sie verschiedene Effekte über den Playground testen.

- Demo: Vergleich der Effekte von Phi-3-mini und Phi-3.5-mini bei chinesischen Szenarien

![phi3](../../../translated_images/de/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/de/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Wenn Sie hingegen Vision- und MoE-Modelle verwenden möchten, können Sie Microsoft Foundry für den entsprechenden Aufruf nutzen. Bei Interesse können Sie das Phi-3 Cookbook lesen, um zu lernen, wie man Phi-3/3.5 Instruct, Vision und MoE über Microsoft Foundry aufruft [Klicken Sie hier](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Neben dem cloudbasierten Microsoft Foundry Modelle-Katalog können Sie auch [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) nutzen, um die entsprechenden Aufrufe zu realisieren. NVIDIA NIM (NVIDIA Inference Microservices) ist eine Sammlung beschleunigter Inferenz-Microservices, die Entwicklern helfen, KI-Modelle effizient in vielen Umgebungen bereitzustellen, darunter Clouds, Rechenzentren und Workstations.

Hier sind einige zentrale Merkmale von NVIDIA NIM:

- **Einfache Bereitstellung:** NIM ermöglicht die Bereitstellung von KI-Modellen mit einem einzigen Befehl, was die Integration in bestehende Workflows erleichtert.

- **Optimierte Leistung:** Es nutzt NVIDIAs voroptimierte Inferenz-Engines wie TensorRT und TensorRT-LLM, um niedrige Latenz und hohen Durchsatz zu gewährleisten.
- **Skalierbarkeit:** NIM unterstützt Autoscaling auf Kubernetes, was eine effektive Bewältigung unterschiedlicher Arbeitslasten ermöglicht.
- **Sicherheit und Kontrolle:** Organisationen können die Kontrolle über ihre Daten und Anwendungen behalten, indem sie NIM-Mikroservices auf ihrer eigenen verwalteten Infrastruktur selbst hosten.
- **Standard-APIs:** NIM bietet branchenübliche APIs, was den Aufbau und die Integration von KI-Anwendungen wie Chatbots, KI-Assistenten und mehr erleichtert.

NIM ist Teil von NVIDIA AI Enterprise, das darauf abzielt, das Deployment und den Betrieb von KI-Modellen zu vereinfachen und sicherzustellen, dass sie effizient auf NVIDIA GPUs laufen.

- Demo: Verwendung von NVIDIA NIM zum Aufrufen der Phi-3.5-Vision-API [[Klicken Sie hier](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokal ausführen
Inferenz im Zusammenhang mit Phi-3 oder einem beliebigen Sprachmodell wie GPT-3 bezieht sich auf den Prozess der Generierung von Antworten oder Vorhersagen basierend auf der Eingabe. Wenn Sie Phi-3 eine Eingabeaufforderung oder Frage geben, verwendet es sein trainiertes neuronales Netzwerk, um durch Analyse von Mustern und Beziehungen in den Trainingsdaten die wahrscheinlichste und relevante Antwort abzuleiten.

**Hugging Face Transformer**
Hugging Face Transformers ist eine leistungsstarke Bibliothek, die für die Verarbeitung natürlicher Sprache (NLP) und andere maschinelle Lernaufgaben entwickelt wurde. Hier sind einige wichtige Punkte dazu:

1. **Vortrainierte Modelle**: Sie stellt Tausende vortrainierter Modelle bereit, die für verschiedene Aufgaben wie Textklassifikation, Named Entity Recognition, Fragebeantwortung, Zusammenfassung, Übersetzung und Textgenerierung verwendet werden können.

2. **Framework-Interoperabilität**: Die Bibliothek unterstützt mehrere Deep-Learning-Frameworks, darunter PyTorch, TensorFlow und JAX. Das ermöglicht es, ein Modell in einem Framework zu trainieren und in einem anderen zu verwenden.

3. **Multimodale Fähigkeiten**: Neben NLP unterstützt Hugging Face Transformers auch Aufgaben in Computer Vision (z. B. Bildklassifikation, Objekterkennung) und Audiobearbeitung (z. B. Spracherkennung, Audioklassifikation).

4. **Einfachheit der Nutzung**: Die Bibliothek bietet APIs und Werkzeuge, um Modelle einfach herunterzuladen und feinzujustieren, was sie sowohl für Anfänger als auch Experten zugänglich macht.

5. **Community und Ressourcen**: Hugging Face verfügt über eine lebendige Community sowie umfangreiche Dokumentation, Tutorials und Anleitungen, die Nutzern beim Einstieg helfen und die Nutzung der Bibliothek maximieren.
[offizielle Dokumentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oder ihr [GitHub-Repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Dies ist die am häufigsten verwendete Methode, erfordert jedoch GPU-Beschleunigung. Szenarien wie Vision und MoE benötigen viele Berechnungen, die auf der CPU ohne Quantisierung sehr langsam sind.


- Demo: Verwendung von Transformer zum Aufrufen von Phi-3.5-Instruct [Klicken Sie hier](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufrufen von Phi-3.5-Vision [Klicken Sie hier](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Verwendung von Transformer zum Aufrufen von Phi-3.5-MoE [Klicken Sie hier](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ist eine Plattform, die es erleichtert, große Sprachmodelle (LLMs) lokal auf Ihrem Rechner auszuführen. Sie unterstützt verschiedene Modelle wie Llama 3.1, Phi 3, Mistral und Gemma 2 unter anderem. Die Plattform vereinfacht den Prozess, indem Modellgewichte, Konfiguration und Daten in einem einzigen Paket gebündelt werden, was es Nutzern erleichtert, eigene Modelle zu erstellen und anzupassen. Ollama ist für macOS, Linux und Windows verfügbar. Es ist ein großartiges Tool, wenn Sie mit LLMs experimentieren oder sie bereitstellen möchten, ohne Cloud-Dienste nutzen zu müssen. Ollama ist der direkteste Weg, Sie müssen nur den folgenden Befehl ausführen.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ist Microsofts Offline-Laufzeitumgebung für das Ausführen von Modellen wie Phi komplett auf eigener Hardware – kein Azure-Abonnement, API-Schlüssel oder Netzwerkverbindung erforderlich. Sie wählt automatisch den besten verfügbaren Ausführungsanbieter (NPU, GPU oder CPU) aus und stellt einen OpenAI-kompatiblen Endpunkt bereit, sodass bestehender `openai`/Azure AI Inference SDK-Code mit minimalen Änderungen darauf zeigen kann. Siehe die [Foundry Local-Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg.

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
ONNX Runtime ist ein Open-Source-Projekt, das leistungsstarke Inferenz von maschinellen Lernmodellen ermöglicht. Es unterstützt Modelle im Open Neural Network Exchange (ONNX) Format, einem Standard zur Repräsentation von ML-Modellen. Die ONNX Runtime-Inferenz kann schnellere Kundenerfahrungen und niedrigere Kosten ermöglichen und unterstützt Modelle aus Deep-Learning-Frameworks wie PyTorch und TensorFlow/Keras sowie klassische ML-Bibliotheken wie scikit-learn, LightGBM, XGBoost etc. ONNX Runtime ist mit verschiedenen Hardware, Treibern und Betriebssystemen kompatibel und bietet optimale Leistung, indem es Hardwarebeschleuniger verwendet, wo möglich, zusammen mit Graph-Optimierungen und Transformationen.

## Was ist Generative AI?
Generative AI bezeichnet KI-Systeme, die neue Inhalte wie Text, Bilder oder Musik basierend auf den Daten erzeugen können, mit denen sie trainiert wurden. Beispiele sind Sprachmodelle wie GPT-3 und Bildgenerierungsmodelle wie Stable Diffusion. Die ONNX Runtime für GenAI-Bibliothek stellt den generativen KI-Zyklus für ONNX-Modelle bereit, einschließlich Inferenz mit ONNX Runtime, Logit-Verarbeitung, Suche und Sampling sowie KV-Cache-Verwaltung.

## ONNX Runtime für GENAI
ONNX Runtime für GENAI erweitert die Fähigkeiten von ONNX Runtime um Unterstützung für generative KI-Modelle. Hier sind einige wichtige Merkmale:

- **Breite Plattformunterstützung:** Sie funktioniert auf verschiedenen Plattformen einschließlich Windows, Linux, macOS, Android und iOS.
- **Modellunterstützung:** Sie unterstützt viele beliebte generative KI-Modelle wie LLaMA, GPT-Neo, BLOOM und mehr.
- **Leistungsoptimierung:** Sie enthält Optimierungen für verschiedene Hardwarebeschleuniger wie NVIDIA GPUs, AMD GPUs und weitere.
- **Benutzerfreundlichkeit:** Sie bietet APIs für eine einfache Integration in Anwendungen, mit denen Sie Text, Bilder und andere Inhalte mit minimalem Code generieren können.
- Nutzer können eine High-Level-Generate()-Methode aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei jeweils ein Token generiert und optional die Generierungsparameter innerhalb der Schleife aktualisiert werden.
- ONNX Runtime unterstützt außerdem Greedy-/Beam-Search sowie TopP- und TopK-Sampling zum Generieren von Token-Sequenzen und bietet eingebaute Logit-Verarbeitung wie Wiederholungsstrafen. Sie können auch problemlos eigene Scoring-Methoden hinzufügen.

## Loslegen
Um mit ONNX Runtime für GENAI zu starten, können Sie folgende Schritte durchführen:

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
### Demo: Verwendung von ONNX Runtime GenAI zum Aufrufen von Phi-3.5-Vision


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


**Weitere**

Neben den Referenzmethoden ONNX Runtime, Ollama und Foundry Local können wir auch die Referenz quantitativer Modelle auf Basis der vom jeweiligen Hersteller bereitgestellten Modellreferenzmethoden vervollständigen. Zum Beispiel das Apple MLX-Framework mit Apple Metal, Qualcomm QNN mit NPU, Intel OpenVINO mit CPU/GPU usw. Weitere Inhalte finden Sie auch im [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mehr

Wir haben die Grundlagen der Phi-3/3.5-Familie kennengelernt, aber um mehr über SLM zu erfahren, benötigen wir mehr Wissen. Antworten finden Sie im Phi-3 Cookbook. Wenn Sie mehr wissen möchten, besuchen Sie bitte das [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->