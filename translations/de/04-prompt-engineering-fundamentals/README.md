# Grundlagen des Prompt Engineerings

[![Grundlagen des Prompt Engineerings](../../../translated_images/de/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Einführung
Dieses Modul behandelt wesentliche Konzepte und Techniken zur Erstellung effektiver Eingabeaufforderungen in generativen KI-Modellen. Die Art und Weise, wie Sie Ihre Eingabeaufforderung an ein LLM schreiben, ist ebenfalls wichtig. Eine sorgfältig gestaltete Eingabeaufforderung kann eine bessere Antwortqualität erzielen. Aber was genau bedeuten Begriffe wie _Prompt_ und _Prompt Engineering_? Und wie verbessere ich die Eingabeaufforderung (_Input_), die ich an das LLM sende? Diese Fragen versuchen wir in diesem Kapitel und dem nächsten zu beantworten.

_Generative KI_ ist in der Lage, auf Benutzeranfragen hin neue Inhalte (z.B. Text, Bilder, Audio, Code usw.) zu erstellen. Dies erreicht sie mit _Großen Sprachmodellen_ wie der GPT-Serie von OpenAI („Generative Pre-trained Transformer“), die für die Verwendung natürlicher Sprache und Code trainiert wurden.

Benutzer können jetzt mit diesen Modellen über vertraute Paradigmen wie Chat interagieren, ohne technische Kenntnisse oder Schulungen zu benötigen. Die Modelle arbeiten _promptbasiert_ – Benutzer senden eine Texteingabe (Prompt) und erhalten die KI-Antwort (Vervollständigung) zurück. Sie können dann iterativ „mit der KI chatten“ in mehrstufigen Gesprächen und ihre Eingabeaufforderung verfeinern, bis die Antwort ihren Erwartungen entspricht.

„Prompts“ werden nun zur primären _Programmierschnittstelle_ für generative KI-Anwendungen, indem sie den Modellen sagen, was sie tun sollen, und die Qualität der zurückgegebenen Antworten beeinflussen. „Prompt Engineering“ ist ein schnell wachsendes Studienfeld, das sich auf die _Gestaltung und Optimierung_ von Prompts konzentriert, um konsistente und qualitativ hochwertige Antworten im großen Maßstab zu liefern.

## Lernziele

In dieser Lektion lernen wir, was Prompt Engineering ist, warum es wichtig ist und wie wir effektivere Prompts für ein bestimmtes Modell und ein Anwendungsziel erstellen können. Wir verstehen Kernkonzepte und bewährte Methoden des Prompt Engineerings und lernen eine interaktive Jupyter Notebooks „Sandbox“-Umgebung kennen, in der wir diese Konzepte an realen Beispielen anwenden können.

Am Ende dieser Lektion werden wir in der Lage sein:

1. Zu erklären, was Prompt Engineering ist und warum es wichtig ist.
2. Die Bestandteile eines Prompts zu beschreiben und wie sie verwendet werden.
3. Best Practices und Techniken für Prompt Engineering zu erlernen.
4. Erlernte Techniken an realen Beispielen anzuwenden, unter Verwendung eines OpenAI-Endpunkts.

## Wichtige Begriffe

Prompt Engineering: Die Praxis, Eingaben zu entwerfen und zu verfeinern, um KI-Modelle zu gewünschten Ausgaben zu führen.
Tokenisierung: Der Prozess, Text in kleinere Einheiten, sogenannte Tokens, zu zerlegen, die ein Modell verstehen und verarbeiten kann.
Instruction-Tuned LLMs: Große Sprachmodelle (LLMs), die mit spezifischen Anweisungen feinabgestimmt wurden, um ihre Antwortgenauigkeit und Relevanz zu verbessern.

## Lern-Sandbox

Prompt Engineering ist aktuell mehr Kunst als Wissenschaft. Der beste Weg, unser Gespür dafür zu verbessern, ist mehr _Übung_ und die Anwendung eines Trial-and-Error-Ansatzes, der Fachwissen aus dem Anwendungsbereich mit empfohlenen Techniken und modellspezifischen Optimierungen kombiniert.

Das zu dieser Lektion gehörende Jupyter Notebook bietet eine _Sandbox_-Umgebung, in der Sie das Gelernte ausprobieren können – während Sie lernen oder als Teil der Aufgabenstellung am Ende. Um die Übungen auszuführen, benötigen Sie:

1. **Einen Azure OpenAI API-Schlüssel** – den Service-Endpunkt für ein bereitgestelltes LLM.
2. **Eine Python-Laufzeitumgebung** – um das Notebook auszuführen.
3. **Lokale Umgebungsvariablen** – _schließen Sie jetzt die [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) Schritte ab, um vorbereitet zu sein_.

Das Notebook enthält _Starter_-Übungen – Sie sind jedoch eingeladen, eigene _Markdown_ (Beschreibung) und _Code_ (Prompt-Anfragen) Abschnitte hinzuzufügen, um mehr Beispiele oder Ideen auszuprobieren – und so Ihr Gespür für das Entwerfen von Prompts zu stärken.

## Illustrierter Leitfaden

Möchten Sie einen Überblick darüber, was diese Lektion behandelt, bevor Sie eintauchen? Sehen Sie sich diesen illustrierten Leitfaden an, der Ihnen ein Gefühl für die Hauptthemen und die wichtigsten Erkenntnisse gibt, über die Sie in jedem Abschnitt nachdenken sollten. Der Lernpfad führt Sie vom Verständnis der Kernkonzepte und Herausforderungen hin zu deren Behandlung mit relevanten Techniken und Best Practices des Prompt Engineerings. Beachten Sie, dass der Abschnitt „Fortgeschrittene Techniken“ in diesem Leitfaden auf Inhalte im _nächsten_ Kapitel dieses Curriculums verweist.

![Illustrierter Leitfaden zum Prompt Engineering](../../../translated_images/de/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Unser Startup

Kommen wir nun dazu, wie _dieses Thema_ mit unserer Startup-Mission zusammenhängt, [KI-Innovation im Bildungsbereich zu fördern](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Wir wollen KI-gestützte Anwendungen für _personalisiertes Lernen_ entwickeln – denken wir also darüber nach, wie verschiedene Nutzer unserer Anwendung Prompts „gestalten“ könnten:

- **Administratoren** könnten die KI bitten, _Lehrplandaten zu analysieren, um Lücken abzudecken_. Die KI kann Ergebnisse zusammenfassen oder mit Code visualisieren.
- **Lehrkräfte** könnten die KI bitten, _einen Lehrplan für eine Zielgruppe und ein Thema zu erstellen_. Die KI kann den personalisierten Plan in einem angegebenen Format erstellen.
- **Schüler** könnten die KI bitten, _sie in einem schwierigen Fach zu unterrichten_. Die KI kann nun Schüler mit Lektionen, Hinweisen und Beispielen auf ihrem Niveau anleiten.

Das ist nur die Spitze des Eisbergs. Sehen Sie sich [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) an – eine Open-Source-Promptbibliothek, kuratiert von Bildungsexperten – um ein breiteres Bild der Möglichkeiten zu erhalten! _Probieren Sie einige dieser Prompts in der Sandbox oder im OpenAI Playground aus, um zu sehen, was passiert!_

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte Kernkonzept #1 behandeln.
Verstärken Sie das Konzept mit Beispielen und Verweisen.

KONZEPT #1:
Prompt Engineering.
Definieren Sie es und erklären Sie, warum es erforderlich ist.
-->

## Was ist Prompt Engineering?

Wir haben diese Lektion damit begonnen, **Prompt Engineering** als den Prozess _des Entwerfens und Optimierens_ von Texteingaben (Prompts) zu definieren, um konsistente und qualitativ hochwertige Antworten (Vervollständigungen) für ein gegebenes Anwendungsziel und Modell zu liefern. Wir können dies als einen zweistufigen Prozess betrachten:

- _Entwerfen_ der anfänglichen Eingabeaufforderung für ein gegebenes Modell und Ziel
- _Verfeinern_ der Eingabeaufforderung iterativ zur Verbesserung der Antwortqualität

Dies ist notwendigerweise ein Trial-and-Error-Prozess, der Benutzerintuition und -anstrengung erfordert, um optimale Ergebnisse zu erzielen. Warum ist es also wichtig? Um diese Frage zu beantworten, müssen wir zunächst drei Konzepte verstehen:

- _Tokenisierung_ = wie das Modell die Eingabeaufforderung „sieht“
- _Basis-LLMs_ = wie das Basismodell eine Eingabeaufforderung „verarbeitet“
- _Instruction-tuned LLMs_ = wie das Modell jetzt „Aufgaben“ sehen kann

### Tokenisierung

Ein LLM sieht Prompts als _Sequenz von Tokens_, wobei verschiedene Modelle (oder Modellversionen) denselben Prompt unterschiedlich tokenisieren können. Da LLMs auf Tokens (und nicht auf Rohtext) trainiert sind, hat die Art der Tokenisierung direkten Einfluss auf die Qualität der generierten Antwort.

Um ein Gespür dafür zu bekommen, wie Tokenisierung funktioniert, probieren Sie Werkzeuge wie den [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) aus, der unten gezeigt wird. Kopieren Sie Ihren Prompt hinein und sehen Sie, wie dieser in Tokens umgewandelt wird, wobei Sie darauf achten, wie Leerzeichen und Satzzeichen behandelt werden. Beachten Sie, dass dieses Beispiel ein älteres LLM (GPT-3) zeigt – mit einem neueren Modell kann das Ergebnis anders ausfallen.

![Tokenisierung](../../../translated_images/de/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konzept: Foundation Models

Sobald ein Prompt tokenisiert ist, ist die Hauptfunktion des ["Basis-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (oder Foundation-Modell) die Vorhersage des nächsten Tokens in dieser Sequenz. Da LLMs auf riesigen Textdatensätzen trainiert sind, haben sie ein gutes Verständnis der statistischen Beziehungen zwischen Tokens und können diese Vorhersage mit gewisser Sicherheit treffen. Sie verstehen jedoch nicht die _Bedeutung_ der Wörter im Prompt oder Token; sie erkennen nur ein Muster, das sie mit ihrer nächsten Vorhersage „vervollständigen“ können. Sie können die Sequenz weiter vorhersagen, bis der Vorgang durch Benutzereingriff oder eine vorab festgelegte Bedingung beendet wird.

Möchten Sie sehen, wie eine promptbasierte Vervollständigung funktioniert? Geben Sie den oben genannten Prompt im [Microsoft Foundry Playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) mit den Standardeinstellungen ein. Das System ist so konfiguriert, dass Prompts als Informationsanfragen behandelt werden – Sie sollten also eine Vervollständigung sehen, die diesen Kontext erfüllt.

Aber was ist, wenn der Nutzer etwas Spezifisches sehen möchte, das bestimmten Kriterien oder einem Aufgabenmotiv entspricht? Hier kommen _instruction-tuned_ LLMs ins Spiel.

![Basis LLM Chat-Vervollständigung](../../../translated_images/de/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konzept: Instruction Tuned LLMs

Ein [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) beginnt mit dem Foundation-Modell und verfeinert es mit Beispielen oder Ein-/Ausgabe-Paaren (z.B. mehrstufige „Nachrichten“), die klare Anweisungen enthalten können – die Antwort der KI versucht dieser Anweisung zu folgen.

Dies nutzt Techniken wie Reinforcement Learning mit menschlichem Feedback (RLHF), das das Modell trainiert, _Anweisungen zu folgen_ und _aus Feedback zu lernen_, sodass es Antworten liefert, die besser für praktische Anwendungen geeignet und relevanter für Benutzerziele sind.

Probieren wir es aus: Ändern Sie die _Systemnachricht_ im obigen Prompt, um die folgende Anweisung als Kontext zu geben:

> _Fassen Sie die bereitgestellten Inhalte für einen Zweitklässler zusammen. Halten Sie das Ergebnis in einem Absatz mit 3-5 Aufzählungspunkten._

Sehen Sie, wie das Ergebnis nun auf das gewünschte Ziel und Format abgestimmt ist? Eine Lehrkraft kann diese Antwort jetzt direkt in ihren Folien für den Unterricht verwenden.

![Instruction Tuned LLM Chat Completion](../../../translated_images/de/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Warum brauchen wir Prompt Engineering?

Nun, da wir wissen, wie Prompts von LLMs verarbeitet werden, sprechen wir darüber, _warum_ wir Prompt Engineering benötigen. Die Antwort liegt darin, dass aktuelle LLMs eine Reihe von Herausforderungen mit sich bringen, die es erschweren, _zuverlässige und konsistente Vervollständigungen_ ohne Aufwand für die Konstruktion und Optimierung der Eingabeaufforderung zu erzielen. Zum Beispiel:

1. **Modellantworten sind stochastisch.** Der _gleiche Prompt_ wird mit unterschiedlichen Modellen oder Modellversionen wahrscheinlich unterschiedliche Antworten erzeugen. Und er kann sogar mit _dem gleichen Modell_ zu verschiedenen Zeiten unterschiedliche Ergebnisse liefern. _Prompt Engineering-Techniken können helfen, diese Schwankungen durch bessere Leitplanken zu minimieren_.

1. **Modelle können Antworten erfinden.** Modelle sind mit _großen, aber endlichen_ Datensätzen vortrainiert, was bedeutet, dass ihnen Wissen über Konzepte außerhalb dieses Trainingsbereichs fehlt. Daher können sie Vervollständigungen erzeugen, die ungenau, erfunden oder direkt widersprüchlich zu bekannten Fakten sind. _Prompt Engineering-Techniken helfen Nutzern, solche Erfindungen zu erkennen und zu mindern, z.B. indem die KI nach Quellenangaben oder Begründungen gefragt wird_.

1. **Modelle weisen unterschiedliche Fähigkeiten auf.** Neuere Modelle oder Modellgenerationen verfügen über umfangreichere Fähigkeiten, bringen aber auch einzigartige Eigenheiten und Kompromisse bei Kosten und Komplexität mit sich. _Prompt Engineering kann uns helfen, Best Practices und Workflows zu entwickeln, die Unterschiede abstrahieren und sich skalierbar, nahtlos an modellspezifische Anforderungen anpassen_.

Sehen wir uns das im OpenAI- oder Azure OpenAI Playground an:

- Verwenden Sie denselben Prompt mit verschiedenen LLM-Bereitstellungen (z.B. OpenAI, Azure OpenAI, Hugging Face) – haben Sie die Unterschiede gesehen?
- Verwenden Sie denselben Prompt mehrfach mit _derselben_ LLM-Bereitstellung (z.B. Azure OpenAI Playground) – wie unterschieden sich diese Variationen?

### Beispiel zu Erfindungen

In diesem Kurs verwenden wir den Begriff **„Erfindung“** für das Phänomen, dass LLMs manchmal faktisch falsche Informationen aufgrund von Beschränkungen in ihrem Training oder anderen Einschränkungen generieren. Sie haben diesen Begriff vielleicht auch als _„Halluzinationen“_ in populären Artikeln oder Forschungsarbeiten gehört. Wir empfehlen jedoch dringend, den Begriff _„Erfindung“_ zu verwenden, um keine unbeabsichtigte Vermenschlichung des Verhaltens vorzunehmen, indem ein menschenähnliches Merkmal auf ein maschinengesteuertes Ergebnis übertragen wird. Dies unterstützt auch die [Richtlinien für verantwortliche KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aus Terminologiesicht, indem Begriffe vermieden werden, die in manchen Kontexten als anstößig oder nicht inklusiv gelten könnten.

Möchten Sie ein Gefühl dafür bekommen, wie Erfindungen funktionieren? Denken Sie an einen Prompt, der die KI anweist, Inhalte zu einem nicht existierenden Thema zu generieren (damit sichergestellt ist, dass es nicht im Trainingsdatensatz vorkommt). Zum Beispiel habe ich diesen Prompt ausprobiert:

> **Prompt:** Erstelle einen Lehrplan zum Marskrieg von 2076.

Eine Websuche zeigte mir, dass es fiktive Darstellungen (z.B. Fernsehserien oder Bücher) zu Marskriegen gibt – aber keine aus dem Jahr 2076. Der gesunde Menschenverstand sagt auch, dass 2076 _in der Zukunft_ liegt und deshalb nicht mit einem realen Ereignis verbunden sein kann.


Was passiert also, wenn wir diesen Prompt mit verschiedenen LLM-Anbietern ausführen?

> **Antwort 1**: OpenAI Playground (GPT-35)

![Antwort 1](../../../translated_images/de/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Antwort 2**: Azure OpenAI Playground (GPT-35)

![Antwort 2](../../../translated_images/de/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Antwort 3**: : Hugging Face Chat Playground (LLama-2)

![Antwort 3](../../../translated_images/de/04-fabrication-huggingchat.faf82a0a51278956.webp)

Wie erwartet erzeugt jedes Modell (oder jede Modellversion) aufgrund des stochastischen Verhaltens und der Unterschiede in den Modellfähigkeiten leicht unterschiedliche Antworten. Zum Beispiel richtet sich ein Modell an ein Publikum der 8. Klasse, während das andere einen Schüler der Highschool annimmt. Aber alle drei Modelle erzeugten Antworten, die einen uninformierten Nutzer davon überzeugen könnten, dass das Ereignis real war.

Prompt-Engineering-Techniken wie _Metaprompting_ und _Temperaturkonfiguration_ können Modell-Fälschungen bis zu einem gewissen Grad reduzieren. Neue Prompt-Engineering-_Architekturen_ integrieren auch nahtlos neue Werkzeuge und Techniken in den Prompt-Fluss, um einige dieser Effekte abzumildern oder zu reduzieren.

## Fallstudie: GitHub Copilot

Lassen Sie uns diesen Abschnitt abschließen, indem wir uns einen Eindruck davon verschaffen, wie Prompt-Engineering in realen Lösungen eingesetzt wird, anhand einer Fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ist Ihr „KI-Paarprogrammierer“ – er wandelt Texteingaben in Code-Vervollständigungen um und ist in Ihre Entwicklungsumgebung (z. B. Visual Studio Code) integriert für eine nahtlose Benutzererfahrung. Wie in der unten stehenden Blogreihe dokumentiert, basierte die früheste Version auf dem OpenAI Codex Modell – wobei die Entwickler schnell erkannten, dass es notwendig war, das Modell feinzujustieren und bessere Prompt-Engineering-Techniken zu entwickeln, um die Codequalität zu verbessern. Im Juli präsentierten sie ein [verbessertes KI-Modell, das über Codex hinausgeht](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) für noch schnellere Vorschläge.

Lesen Sie die Beiträge der Reihe in der Reihenfolge, um ihre Lernreise nachzuvollziehen.

- **Mai 2023** | [GitHub Copilot wird besser darin, Ihren Code zu verstehen](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub: Arbeiten mit den LLMs hinter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Wie man bessere Prompts für GitHub Copilot schreibt](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot geht über Codex hinaus mit verbessertem KI-Modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Ein Entwicklerleitfaden zum Prompt-Engineering und zu LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Wie man eine Enterprise-LLM-App baut: Lektionen von GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Sie können auch ihren [Engineering-Blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) für weitere Beiträge wie [diesen](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) durchsuchen, der zeigt, wie diese Modelle und Techniken für den Einsatz in realen Anwendungen _angewendet_ werden.

---

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte das Kernkonzept #2 abdecken.
Das Konzept mit Beispielen und Referenzen verstärken.

KONZEPT #2:
Prompt-Design.
Veranschaulicht mit Beispielen.
-->

## Prompt-Konstruktion

Wir haben gesehen, warum Prompt-Engineering wichtig ist – jetzt wollen wir verstehen, wie Prompts _konstruiert_ werden, um verschiedene Techniken für ein effektiveres Prompt-Design bewerten zu können.

### Basis-Prompt

Fangen wir mit dem Basis-Prompt an: eine Texteingabe, die ohne weiteren Kontext an das Modell gesendet wird. Hier ist ein Beispiel – wenn wir die ersten Wörter der US-Nationalhymne an die OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) senden, vervollständigt sie sofort die Antwort mit den nächsten Zeilen und zeigt so das grundlegende Vorhersageverhalten.

| Prompt (Eingabe)    | Vervollständigung (Ausgabe)                                                                                                                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Es klingt, als ob Sie die Liedtexte von „The Star-Spangled Banner“, der Nationalhymne der Vereinigten Staaten, beginnen. Der vollständige Text lautet ... |

### Komplexer Prompt

Jetzt fügen wir diesem Basis-Prompt Kontext und Anweisungen hinzu. Die [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) erlaubt uns, einen komplexen Prompt als Sammlung von _Nachrichten_ zu konstruieren mit:

- Eingabe/Ausgabe-Paaren, die _Benutzer_-Eingabe und _Assistent_-Antwort widerspiegeln.
- Systemnachricht zur Festlegung des Kontexts für das Verhalten oder die Persönlichkeit des Assistenten.

Die Anfrage hat nun die folgende Form, wobei die _Tokenisierung_ relevante Informationen aus dem Kontext und dem Gespräch effektiv erfasst. Das Ändern des Systemkontexts kann somit ebenso großen Einfluss auf die Qualität der Vervollständigungen haben wie die vom Benutzer gelieferten Eingaben.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruktions-Prompt

In den obigen Beispielen war der Benutzer-Prompt eine einfache Textanfrage, die als Informationsanfrage interpretiert werden kann. Bei _Instruktions_-Prompts können wir diesen Text verwenden, um eine Aufgabe detaillierter zu spezifizieren und der KI eine bessere Anleitung zu geben. Hier ein Beispiel:

| Prompt (Eingabe)                                                                                                                                                                                                                          | Vervollständigung (Ausgabe)                                                                                             | Instruktionstyp    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Schreibe eine Beschreibung des Bürgerkriegs                                                                                                                                                                                            | _gab einen einfachen Absatz zurück_                                                                                     | Einfach            |
| Schreibe eine Beschreibung des Bürgerkriegs. Gib wichtige Daten und Ereignisse an und beschreibe deren Bedeutung                                                                                                                      | _gab einen Absatz gefolgt von einer Liste mit wichtigen Ereignisdaten und Beschreibungen zurück_                         | Komplex            |
| Schreibe eine Beschreibung des Bürgerkriegs in 1 Absatz. Gib 3 Stichpunkte mit wichtigen Daten und deren Bedeutung an. Gib 3 weitere Stichpunkte mit wichtigen historischen Personen und deren Beiträgen. Gib die Ausgabe als JSON-Datei zurück | _liefert umfangreichere Details in einem Textfeld, formatiert als JSON, das du kopieren und bei Bedarf validieren kannst_ | Komplex. Formatiert. |

## Primärer Inhalt

In den obigen Beispielen war der Prompt noch relativ offen, sodass das LLM selbst entscheiden konnte, welcher Teil seines vortrainierten Datensatzes relevant ist. Mit dem Designmuster _primärer Inhalt_ wird der Eingabetext in zwei Teile geteilt:

- eine Anweisung (Aktion)
- relevanter Inhalt (der die Aktion beeinflusst)

Hier ein Beispiel, bei dem die Anweisung lautet: „Fasse dies in 2 Sätzen zusammen“.

| Prompt (Eingabe)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Vervollständigung (Ausgabe)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt, aber zweieinhalb Mal so schwer ist wie alle anderen Planeten des Sonnensystems zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und ist den antiken Zivilisationen schon seit der Vorgeschichte bekannt. Er ist nach dem römischen Gott Jupiter benannt.[19] Wenn man ihn von der Erde aus betrachtet, kann Jupiter hell genug sein, damit sein reflektiertes Licht sichtbare Schatten wirft,[20] und ist im Durchschnitt das dritthellste natürliche Objekt am Nachthimmel nach Mond und Venus. <br/> **Fasse dies in 2 kurzen Sätzen zusammen** | Jupiter, der fünfte Planet von der Sonne, ist der größte im Sonnensystem und bekannt dafür, eines der hellsten Objekte am Nachthimmel zu sein. Benannt nach dem römischen Gott Jupiter, ist er ein Gasriese mit einer Masse von zweieinhalb Mal der aller anderen Planeten im Sonnensystem zusammen. |

Das Segment für primären Inhalt kann auf verschiedene Weise verwendet werden, um effektivere Anweisungen zu erzeugen:

- **Beispiele** - Anstatt dem Modell eine explizite Anweisung zu geben, zeigen Sie Beispiele, was zu tun ist, und lassen Sie das Muster ableiten.
- **Hinweise** - Folgen Sie der Anweisung mit einem „Hinweis“, der die Vervollständigung anregt und das Modell zu relevanteren Antworten führt.
- **Vorlagen** - Dies sind wiederholbare „Rezepte“ für Prompts mit Platzhaltern (Variablen), die mit Daten für bestimmte Anwendungsfälle angepasst werden können.

Lassen Sie uns diese in der Praxis erkunden.

### Verwendung von Beispielen

Dies ist ein Ansatz, bei dem der primäre Inhalt dem Modell Beispiele für die gewünschte Ausgabe für eine bestimmte Anweisung liefert und es das Muster für die gewünschte Ausgabe ableiten lässt. Je nach Anzahl der Beispiele spricht man von Zero-shot-, One-shot- oder Few-shot-Prompting.

Der Prompt besteht nun aus drei Komponenten:

- Einer Aufgabebeschreibung
- Ein paar Beispiele für die gewünschte Ausgabe
- Dem Beginn eines neuen Beispiels (das zu einer impliziten Aufgabebeschreibung wird)

| Lerntyp   | Prompt (Eingabe)                                                                                              | Vervollständigung (Ausgabe)  |
| :-------- | :---------------------------------------------------------------------------------------------------------- | :---------------------------- |
| Zero-shot | „Die Sonne scheint“. Übersetze ins Spanische                                                               | „El Sol está brillando“.      |
| One-shot  | „Die Sonne scheint“ => „El Sol está brillando“. <br> „Es ist ein kalter und windiger Tag“ =>                  | „Es un día frío y ventoso“.   |
| Few-shot  | Der Spieler lief die Bases => Baseball <br/> Der Spieler machte ein Ass => Tennis <br/> Der Spieler erzielte eine Six => Cricket <br/> Der Spieler machte einen Slam-Dunk => | Basketball                   |
|           |                                                                                                             |                              |

Beachten Sie, wie wir beim Zero-shot-Prompting eine explizite Anweisung („Übersetze ins Spanische“) geben mussten, die beim One-shot-Prompting-Beispiel abgeleitet wird. Das Few-shot-Beispiel zeigt, wie durch Hinzufügen weiterer Beispiele Modelle genauere Schlüsse ohne weitere Anweisungen ziehen können.

### Prompt-Hinweise

Eine weitere Technik bei der Verwendung des primären Inhalts ist, dem Modell _Hinweise_ statt Beispiele zu geben. In diesem Fall geben wir dem Modell einen Stups in die richtige Richtung, indem wir mit einem Ausschnitt beginnen, der das gewünschte Antwortformat widerspiegelt. Das Modell „greift den Hinweis auf“ und setzt in dieser Weise fort.

| Anzahl der Hinweise | Prompt (Eingabe)                                                                                                                                                                                                                                                                                                                                                                                      | Vervollständigung (Ausgabe)                                                                                                                                                                                                                                                                                           |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                   | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt, aber zweieinhalb Mal so schwer wie alle anderen Planeten des Sonnensystems zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und ist den antiken Zivilisationen schon seit der Vorgeschichte bekannt. <br/>**Fasse dies zusammen**                                       | Jupiter ist der größte Planet in unserem Sonnensystem und der fünfte von der Sonne. Er ist ein Gasriese mit einer Masse von 1/1000 der Sonne, aber schwerer als alle anderen Planeten zusammen. Antike Kulturen kennen Jupiter schon lange, und er ist leicht am Nachthimmel sichtbar.          |
| 1                   | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt, aber zweieinhalb Mal so schwer wie alle anderen Planeten des Sonnensystems zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und ist den antiken Zivilisationen schon seit der Vorgeschichte bekannt. <br/>**Fasse dies zusammen** <br/> Was wir gelernt haben, ist, dass Jupiter         | der fünfte Planet von der Sonne ist und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt, aber zweieinhalb Mal so schwer wie alle anderen Planeten zusammen. Er ist mit bloßem Auge leicht sichtbar und seit der Antike bekannt.                  |

| 2              | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonnenmasse beträgt, aber zweieinhalbmal so groß ist wie die aller anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten mit bloßem Auge sichtbaren Objekte am Nachthimmel und ist seit der Zeit vor der aufgezeichneten Geschichte antiken Zivilisationen bekannt. <br/>**Fassen Sie dies zusammen** <br/> Top 3 Fakten, die wir gelernt haben:         | 1. Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. <br/> 2. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonnenmasse beträgt...<br/> 3. Jupiter ist seit der Antike mit bloßem Auge sichtbar ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-Vorlagen

Eine Prompt-Vorlage ist ein _vordefiniertes Rezept für einen Prompt_, das gespeichert und bei Bedarf wiederverwendet werden kann, um konsistentere Benutzererfahrungen im großen Maßstab zu ermöglichen. In seiner einfachsten Form ist es einfach eine Sammlung von Prompt-Beispielen wie [dieses von OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), die sowohl interaktive Prompt-Komponenten (Benutzer- und Systemnachrichten) als auch das API-gesteuerte Anforderungsformat bereitstellt – zur Unterstützung der Wiederverwendung.

In seiner komplexeren Form wie [dieses Beispiel von LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) enthält es _Platzhalter_, die durch Daten aus verschiedenen Quellen (Benutzereingaben, Systemkontext, externe Datenquellen usw.) ersetzt werden können, um dynamisch einen Prompt zu generieren. Dadurch können wir eine Bibliothek wiederverwendbarer Prompts erstellen, die zur Programmierung konsistenter Benutzererfahrungen **maßstabsgetreu** verwendet werden können.

Schließlich liegt der eigentliche Wert von Vorlagen in der Fähigkeit, _Prompt-Bibliotheken_ für vertikale Anwendungsbereiche zu erstellen und zu veröffentlichen – wobei die Prompt-Vorlage nun _optimiert_ ist, um anwendungsspezifischen Kontext oder Beispiele widerzuspiegeln, die die Antworten für die Zielnutzer relevanter und genauer machen. Das [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) Repository ist ein großartiges Beispiel für diesen Ansatz, indem es eine Bibliothek von Prompts für den Bildungsbereich mit Schwerpunkt auf Schlüsselaspekten wie Unterrichtsplanung, Curriculum-Design, Schülerbetreuung usw. kuratiert.

## Unterstützender Inhalt

Wenn wir über die Konstruktion eines Prompts nachdenken als bestehend aus einer Anweisung (Aufgabe) und einem Ziel (primärer Inhalt), dann ist _sekundärer Inhalt_ wie zusätzlicher Kontext, den wir angeben, um den Output **irgendwie zu beeinflussen**. Es könnten Einstellungsparameter, Formatierungsanweisungen, Themen-Taxonomien usw. sein, die dem Modell helfen, seine Antwort an die gewünschten Benutzerziele oder Erwartungen _maßzuschneidern_.

Zum Beispiel: Gegeben ein Kursverzeichnis mit umfangreichen Metadaten (Name, Beschreibung, Level, Metadaten-Tags, Dozent usw.) zu allen verfügbaren Kursen im Curriculum:

- können wir eine Anweisung definieren, um "das Kursverzeichnis für Herbst 2023 zusammenzufassen"
- können wir den primären Inhalt verwenden, um ein paar Beispiele für die gewünschte Ausgabe zu liefern
- können wir den sekundären Inhalt verwenden, um die Top 5 "Tags" von Interesse zu identifizieren.

Jetzt kann das Modell eine Zusammenfassung im durch die Beispiele vorgegebenen Format liefern – aber wenn ein Ergebnis mehrere Tags hat, kann es die 5 im sekundären Inhalt identifizierten Tags priorisieren.

---

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte das Kernkonzept #1 abdecken.
Verstärken Sie das Konzept mit Beispielen und Verweisen.

KONZEPT #3:
Prompt Engineering Techniken.
Was sind einige grundlegende Techniken des Prompt Engineering?
Veranschaulichen Sie es mit einigen Übungen.
-->

## Best Practices beim Prompting

Jetzt, da wir wissen, wie Prompts _konstruiert_ werden können, können wir anfangen darüber nachzudenken, wie man sie gestaltet, um Best Practices widerzuspiegeln. Wir können dies in zwei Teile gliedern – die richtige _Einstellung_ und die Anwendung der richtigen _Techniken_.

### Prompt Engineering Einstellung

Prompt Engineering ist ein Prozess von Versuch und Irrtum, daher sollten drei breite Leitfaktoren im Kopf behalten werden:

1. **Fachkenntnis im Bereich ist wichtig.** Antwortgenauigkeit und Relevanz hängen vom _Bereich_ ab, in dem die Anwendung oder der Benutzer tätig ist. Wenden Sie Ihre Intuition und Fachkenntnis an, um **Techniken weiter anzupassen**. Definieren Sie beispielsweise _Bereichsspezifische Persönlichkeiten_ in Ihren Systemprompts oder verwenden Sie _bereichsspezifische Vorlagen_ in Ihren Benutzer-Prompts. Stellen Sie sekundären Inhalt zur Verfügung, der bereichsspezifische Kontexte reflektiert, oder verwenden Sie _bereichsspezifische Hinweise und Beispiele_, um das Modell zu vertrauten Nutzungsmustern zu führen.

2. **Modellverständnis ist wichtig.** Wir wissen, dass Modelle von Natur aus stochastisch sind. Aber Modellausführungen können sich auch hinsichtlich des Trainingsdatensatzes (vorgelerntes Wissen), der Fähigkeiten, die sie bieten (z. B. über API oder SDK), und der Art von Inhalten, für die sie optimiert sind (z. B. Code vs. Bilder vs. Text), unterscheiden. Verstehen Sie die Stärken und Grenzen des Modells, das Sie verwenden, und nutzen Sie dieses Wissen, um _Aufgaben zu priorisieren_ oder _angepasste Vorlagen_ zu erstellen, die für die Fähigkeiten des Modells optimiert sind.

3. **Iteration & Validierung sind wichtig.** Modelle entwickeln sich schnell, und ebenso die Techniken des Prompt Engineerings. Als Fachexperte haben Sie möglicherweise weiteren Kontext oder Kriterien für _Ihre_ spezifische Anwendung, die nicht für die breitere Community gelten. Nutzen Sie Werkzeuge und Techniken des Prompt Engineerings, um die Prompt-Konstruktion zu „starten“, und iterieren Sie dann und validieren Sie die Ergebnisse mit eigener Intuition und Fachkenntnis. Dokumentieren Sie Ihre Erkenntnisse und erstellen Sie eine **Wissensbasis** (z.B. Prompt-Bibliotheken), die als neue Ausgangsbasis für andere genutzt werden kann, für schnellere Iterationen in Zukunft.

## Best Practices

Schauen wir uns jetzt gängige Best Practices an, die von [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) und [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) Praktikern empfohlen werden.

| Was                              | Warum                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bewerten Sie die neuesten Modelle.       | Neue Modelgenerationen haben wahrscheinlich verbesserte Funktionen und Qualität – können aber auch höhere Kosten verursachen. Bewerten Sie sie hinsichtlich der Auswirkungen und treffen Sie dann Entscheidungen zur Migration.                                                                                |
| Trennen Sie Anweisungen & Kontext   | Prüfen Sie, ob Ihr Modell/Anbieter _Begrenzer_ definiert, um Anweisungen, primären und sekundären Inhalt klarer zu unterscheiden. Dies kann Modellen helfen, Token-Gewichte genauer zuzuordnen.                                                         |
| Seien Sie spezifisch und klar             | Geben Sie mehr Details zum gewünschten Kontext, Ergebnis, Länge, Format, Stil usw. Dies verbessert sowohl die Qualität als auch die Konsistenz der Antworten. Halten Sie Rezepte in wiederverwendbaren Vorlagen fest.                                                          |
| Seien Sie beschreibend, verwenden Sie Beispiele      | Modelle reagieren möglicherweise besser auf eine „zeigen und erklären“-Vorgehensweise. Beginnen Sie mit einem `zero-shot`-Ansatz, bei dem Sie eine Anweisung geben (aber keine Beispiele), und versuchen Sie dann `few-shot` als Verfeinerung, indem Sie einige Beispiele für die gewünschte Ausgabe bereitstellen. Verwenden Sie Analogien. |
| Verwenden Sie Hinweise, um Abschlüsse zu starten | Stupsen Sie das Modell zu einem gewünschten Ergebnis an, indem Sie ihm einige führende Wörter oder Phrasen geben, die es als Ausgangspunkt für die Antwort verwenden kann.                                                                                                               |
| Verstärken Sie                     | Manchmal müssen Sie sich beim Modell wiederholen. Geben Sie Anweisungen vor und nach Ihrem primären Inhalt, verwenden Sie eine Anweisung und einen Hinweis usw. Iterieren & validieren Sie, um zu sehen, was funktioniert.                                                         |
| Reihenfolge ist wichtig                     | Die Reihenfolge, in der Sie Informationen dem Modell präsentieren, kann die Ausgabe beeinflussen, selbst bei den Lernbeispielen, aufgrund des „Recency Bias“. Probieren Sie verschiedene Optionen aus, um zu sehen, was am besten funktioniert.                                                               |
| Geben Sie dem Modell eine „Ausweichmöglichkeit“           | Geben Sie dem Modell eine _Fallback_-Antwort, die es liefern kann, falls es die Aufgabe aus irgendeinem Grund nicht erfüllen kann. Dies kann die Wahrscheinlichkeit verringern, dass Modelle falsche oder erfundene Antworten generieren.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Wie bei jeder Best Practice gilt: _Ihre Erfahrungen können variieren_ je nach Modell, Aufgabe und Bereich. Verwenden Sie diese als Ausgangspunkt und iterieren Sie, um herauszufinden, was für Sie am besten funktioniert. Evaluieren Sie Ihren Prompt Engineering Prozess kontinuierlich neu, wenn neue Modelle und Werkzeuge verfügbar werden, mit Fokus auf Prozessskalierbarkeit und Antwortqualität.

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte eine Code-Herausforderung enthalten, falls zutreffend

AUFGABE:
Verlinkung zu einem Jupyter Notebook mit nur den Codekommentaren in den Anweisungen (Codeabschnitte sind leer).

LÖSUNG:
Verlinkung zu einer Kopie dieses Notebooks mit den ausgefüllten Prompts und ausgeführt, welche ein Beispiel zeigt.
-->

## Aufgabe

Herzlichen Glückwunsch! Sie haben das Ende der Lektion erreicht! Es ist Zeit, einige dieser Konzepte und Techniken mit echten Beispielen zu testen!

Für unsere Aufgabe verwenden wir ein Jupyter Notebook mit Übungen, die Sie interaktiv ausführen können. Sie können das Notebook auch mit eigenen Markdown- und Codezellen erweitern, um Ideen und Techniken selbständig zu erkunden.

### Um zu starten, forken Sie das Repository, dann

- (Empfohlen) Starten Sie GitHub Codespaces
- (Alternativ) Klonen Sie das Repository auf Ihr lokales Gerät und verwenden Sie es mit Docker Desktop
- (Alternativ) Öffnen Sie das Notebook mit Ihrer bevorzugten Notebook-Laufzeitumgebung.

### Anschließend konfigurieren Sie Ihre Umgebungsvariablen

- Kopieren Sie die Datei `.env.copy` im Repository-Stammverzeichnis nach `.env` und füllen Sie die Werte `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` und `AZURE_OPENAI_DEPLOYMENT` aus. Kommen Sie zurück zum Abschnitt [Learning Sandbox](#lern-sandbox), um zu erfahren, wie das geht.

### Öffnen Sie anschließend das Jupyter Notebook

- Wählen Sie den Laufzeit-Kernel aus. Wenn Sie Optionen 1 oder 2 verwenden, wählen Sie einfach den Standard-Python 3.10.x Kernel, der vom Entwicklungscontainer bereitgestellt wird.

Sie sind bereit, die Übungen auszuführen. Beachten Sie, dass es hier keine _richtigen oder falschen_ Antworten gibt – sondern nur das Erforschen von Möglichkeiten durch Versuch und Irrtum und das Entwickeln von Intuition dafür, was bei einem bestimmten Modell und Anwendungsbereich funktioniert.

_Aus diesem Grund gibt es in dieser Lektion keine Code-Lösungsabschnitte. Stattdessen enthält das Notebook Markdown-Zellen mit dem Titel "Meine Lösung:", die ein Beispielergebnis zur Referenz anzeigen._

 <!--
LEKTIONSVORLAGE:
Fassen Sie den Abschnitt mit einer Zusammenfassung und Ressourcen für selbstständiges Lernen zusammen.
-->

## Wissensüberprüfung

Welcher der folgenden Prompts ist ein guter Prompt, der einige vernünftige Best Practices befolgt?

1. Zeig mir ein Bild eines roten Autos
2. Zeig mir ein Bild eines roten Autos der Marke Volvo und Modell XC90, geparkt an einer Klippe bei Sonnenuntergang
3. Zeig mir ein Bild eines roten Autos der Marke Volvo und Modell XC90

A: 2, es ist der beste Prompt, da er Details zum „Was“ liefert und in Spezifika geht (nicht nur irgendein Auto, sondern eine bestimmte Marke und ein Modell) und auch die Gesamtszenerie beschreibt. 3 ist zweitbester, da es auch viel Beschreibung enthält.

## 🚀 Herausforderung

Versuchen Sie, die „Cue“-Technik mit dem Prompt zu nutzen: Vervollständige den Satz „Zeig mir ein Bild eines roten Autos der Marke Volvo und “. Was antwortet es, und wie würden Sie es verbessern?

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Möchten Sie mehr über verschiedene Prompt Engineering Konzepte lernen? Gehen Sie zur [Fortsetzungsseite für Lernen](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), um weitere großartige Ressourcen zu diesem Thema zu finden.

Gehen Sie zu Lektion 5, wo wir [fortgeschrittene Prompt-Techniken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) anschauen werden!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->