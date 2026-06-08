# Grundlagen des Prompt Engineering

[![Grundlagen des Prompt Engineering](../../../translated_images/de/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Einführung
Dieses Modul behandelt wesentliche Konzepte und Techniken zur Erstellung effektiver Prompts für generative KI-Modelle. Die Art und Weise, wie Sie Ihr Prompt an ein LLM schreiben, ist ebenfalls wichtig. Ein sorgfältig gestaltetes Prompt kann eine bessere Antwortqualität erzielen. Aber was genau bedeuten Begriffe wie _Prompt_ und _Prompt Engineering_? Und wie verbessere ich das Prompt-_Input_, das ich an das LLM sende? Diese Fragen versuchen wir im Rahmen dieses Kapitels und des nächsten zu beantworten.

_Generative KI_ ist in der Lage, neue Inhalte (z. B. Text, Bilder, Audio, Code usw.) als Antwort auf Benutzeranfragen zu erstellen. Dies geschieht mithilfe von _Large Language Models_ wie der GPT-Serie von OpenAI („Generative Pre-trained Transformer“), die für die Verwendung natürlicher Sprache und Code trainiert wurden.

Benutzer können jetzt mit diesen Modellen über vertraute Paradigmen wie Chat interagieren, ohne technische Fachkenntnisse oder Schulungen zu benötigen. Die Modelle sind _prompt-basiert_ – die Benutzer senden eine Texteingabe (Prompt) und erhalten die KI-Antwort (Vervollständigung) zurück. Sie können dann iterativ „mit der KI chatten“ in mehrstufigen Gesprächen und ihr Prompt so verfeinern, bis die Antwort ihren Erwartungen entspricht.

„Prompts“ sind nun die primäre _Programmierschnittstelle_ für generative KI-Anwendungen, die den Modellen sagen, was sie tun sollen, und die Qualität der zurückgegebenen Antworten beeinflussen. „Prompt Engineering“ ist ein schnell wachsendes Studienfeld, das sich auf die _Gestaltung und Optimierung_ von Prompts konzentriert, um konsistente und qualitativ hochwertige Antworten in großem Maßstab zu liefern.

## Lernziele

In dieser Lektion lernen wir, was Prompt Engineering ist, warum es wichtig ist und wie wir für ein gegebenes Modell und Anwendungsziel effektivere Prompts erstellen können. Wir verstehen Kernkonzepte und bewährte Methoden des Prompt Engineering – und lernen eine interaktive Jupyter-Notebook-„Sandbox“-Umgebung kennen, in der wir diese Konzepte an praktischen Beispielen sehen können.

Am Ende dieser Lektion werden wir in der Lage sein:

1. Zu erklären, was Prompt Engineering ist und warum es wichtig ist.
2. Die Komponenten eines Prompts zu beschreiben und deren Verwendung zu erklären.
3. Best Practices und Techniken für Prompt Engineering zu erlernen.
4. Gelernte Techniken an realen Beispielen unter Verwendung eines OpenAI-Endpunkts anzuwenden.

## Schlüsselbegriffe

Prompt Engineering: Die Praxis, Eingaben zu entwerfen und zu verfeinern, um KI-Modelle dazu zu bringen, gewünschte Ausgaben zu erzeugen.  
Tokenisierung: Der Prozess, Text in kleinere Einheiten, sogenannte Token, umzuwandeln, die ein Modell verstehen und verarbeiten kann.  
Instruction-Tuned LLMs: Große Sprachmodelle (LLMs), die mit spezifischen Anweisungen feinabgestimmt wurden, um ihre Antwortgenauigkeit und Relevanz zu verbessern.

## Lern-Sandbox

Prompt Engineering ist derzeit eher Kunst als Wissenschaft. Die beste Möglichkeit, unsere Intuition dafür zu verbessern, ist, _mehr zu üben_ und einen Trial-and-Error-Ansatz zu verfolgen, der Fachwissen im Anwendungsbereich mit empfohlenen Techniken und modell-spezifischen Optimierungen kombiniert.

Das zugehörige Jupyter Notebook zu dieser Lektion bietet eine _Sandbox_-Umgebung, in der Sie ausprobieren können, was Sie lernen – während des Lernens oder im Rahmen der Code-Herausforderung am Ende. Um die Übungen auszuführen, benötigen Sie:

1. **Einen Azure OpenAI API-Schlüssel** – den Serviceendpunkt für ein bereitgestelltes LLM.  
2. **Eine Python-Laufzeitumgebung** – in der das Notebook ausgeführt werden kann.  
3. **Lokale Umgebungsvariablen** – _schließen Sie jetzt die [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-Schritte ab, um bereit zu sein_.

Das Notebook enthält _Starter_-Übungen – Sie werden jedoch ermutigt, Ihre eigenen _Markdown_ (Beschreibung) und _Code_ (Prompt-Anfragen)-Abschnitte hinzuzufügen, um weitere Beispiele oder Ideen auszuprobieren – und so Ihre Intuition für das Prompt-Design zu stärken.

## Illustrierter Leitfaden

Möchten Sie einen Überblick über die Themen dieser Lektion erhalten, bevor Sie eintauchen? Schauen Sie sich diesen illustrierten Leitfaden an, der Ihnen ein Gefühl für die Hauptthemen und die wichtigsten Erkenntnisse gibt, über die Sie in jedem Abschnitt nachdenken können. Die Lektion führt Sie von den Kernkonzepten und Herausforderungen hin zu deren Behandlung mit relevanten Techniken und bewährten Vorgehensweisen des Prompt Engineerings. Beachten Sie, dass sich der Abschnitt „Fortgeschrittene Techniken“ in diesem Leitfaden auf Inhalte im _nächsten_ Kapitel dieses Lehrplans bezieht.

![Illustrated Guide to Prompt Engineering](../../../translated_images/de/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Unser Startup

Kommen wir nun dazu, wie _dieses Thema_ mit unserer Startup-Mission zusammenhängt, [KI-Innovationen in die Bildung zu bringen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Wir wollen KI-gestützte Anwendungen des _personalisierten Lernens_ aufbauen – denken wir also darüber nach, wie unterschiedliche Nutzer unserer Anwendung Prompts „gestalten“ könnten:

- **Administratoren** könnten die KI bitten, _Lehrplandaten zu analysieren, um Lücken in der Abdeckung zu identifizieren_. Die KI kann Ergebnisse zusammenfassen oder mit Code visualisieren.
- **Lehrkräfte** könnten die KI bitten, _einen Unterrichtsplan für eine Zielgruppe und ein Thema zu erstellen_. Die KI kann den personalisierten Plan in einem vorgegebenen Format erstellen.
- **Schülerinnen und Schüler** könnten die KI bitten, _sie in einem schwierigen Fach zu unterrichten_. Die KI kann nun mit Lektionen, Hinweisen und Beispielen, die dem Niveau der Lernenden angepasst sind, begleiten.

Das ist erst die Spitze des Eisbergs. Schauen Sie sich [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) an – eine Open-Source-Prompt-Bibliothek, kuratiert von Bildungsexpertinnen und -experten – um ein breiteres Spektrum der Möglichkeiten zu entdecken! _Probieren Sie einige dieser Prompts in der Sandbox oder im OpenAI Playground aus, um zu sehen, was passiert!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Was ist Prompt Engineering?

Wir haben diese Lektion begonnen, indem wir **Prompt Engineering** definiert haben als den Prozess des _Entwerfens und Optimierens_ von Texteingaben (Prompts), um konsistente und qualitativ hochwertige Antworten (Vervollständigungen) für ein gegebenes Anwendungsziel und Modell zu liefern. Man kann dies als einen 2-Schritte-Prozess verstehen:

- Das initiale Prompt für ein gegebenes Modell und Ziel _entwerfen_.  
- Das Prompt iterativ _verfeinern_, um die Qualität der Antwort zu verbessern.

Dies ist zwangsläufig ein Trial-and-Error-Prozess, der Nutzerintuition und -aufwand erfordert, um optimale Ergebnisse zu erzielen. Warum ist das wichtig? Um diese Frage zu beantworten, müssen wir zuerst drei Konzepte verstehen:

- _Tokenisierung_ = wie das Modell das Prompt „sieht“  
- _Basis-LLMs_ = wie das Grundmodell ein Prompt „verarbeitet“  
- _Instruction-Tuned LLMs_ = wie das Modell jetzt „Aufgaben“ versteht

### Tokenisierung

Ein LLM sieht Prompts als eine _Abfolge von Token_, wobei verschiedene Modelle (oder Modellversionen) denselben Prompt unterschiedlich tokenisieren können. Da LLMs auf Token (und nicht auf Rohtext) trainiert sind, hat die Art und Weise, wie Prompts tokenisiert werden, einen direkten Einfluss auf die Qualität der erzeugten Antwort.

Um eine Intuition für die Funktionsweise der Tokenisierung zu bekommen, probieren Sie Tools wie den [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), der unten gezeigt wird. Kopieren Sie Ihr Prompt hinein – und sehen Sie, wie es in Token umgewandelt wird, achten Sie darauf, wie Leerzeichen und Satzzeichen behandelt werden. Beachten Sie, dass dieses Beispiel ein älteres LLM (GPT-3) zeigt – das Ergebnis mit einem neueren Modell kann anders ausfallen.

![Tokenisierung](../../../translated_images/de/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konzept: Basis-Modelle

Sobald ein Prompt tokenisiert ist, besteht die Hauptfunktion des ["Basis-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (oder Grundmodells) darin, das nächste Token in dieser Sequenz vorherzusagen. Da LLMs auf massiven Textdatensätzen trainiert sind, haben sie ein gutes Verständnis der statistischen Zusammenhänge zwischen Token und können diese Vorhersage mit gewisser Zuversicht treffen. Beachten Sie, dass sie die _Bedeutung_ der Wörter im Prompt oder Token nicht verstehen; sie sehen nur ein Muster, das sie mit ihrer nächsten Vorhersage „vervollständigen“ können. Sie können die Vorhersage der Sequenz so lange fortsetzen, bis der Nutzer eingreift oder eine vorher festgelegte Bedingung erfüllt ist.

Möchten Sie sehen, wie prompt-basierte Vervollständigungen funktionieren? Geben Sie das obige Prompt im Azure OpenAI Studio im [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) mit den Standard-Einstellungen ein. Das System ist so konfiguriert, dass Prompts als Informationsanfragen behandelt werden – Sie sollten also eine Antwort erhalten, die diesem Kontext entspricht.

Aber was, wenn der Nutzer etwas Spezifisches sehen möchte, das bestimmte Kriterien oder ein Aufgaben-Ziel erfüllt? Hier kommen _instruction-tuned_ LLMs ins Spiel.

![Basis-LLM Chat-Vervollständigung](../../../translated_images/de/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konzept: Instruction-Tuned LLMs

Ein [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) startet mit dem Grundmodell und feinjustiert es mit Beispielen oder Eingabe-/Ausgabe-Paaren (z. B. mehrstufige „Nachrichten“), die klare Anweisungen enthalten können – und die Antwort der KI versucht, diesen Anweisungen zu folgen.

Dies nutzt Techniken wie Verstärkendes Lernen mit menschlichem Feedback (Reinforcement Learning with Human Feedback, RLHF), die das Modell trainieren können, _Anweisungen zu befolgen_ und _aus Feedback zu lernen_, sodass es Antworten erzeugt, die besser für praktische Anwendungen geeignet und relevanter für Nutzerziele sind.

Lassen Sie es uns ausprobieren – nehmen Sie das obige Prompt und ändern Sie nun die _Systemnachricht_, um folgende Anweisung als Kontext bereitzustellen:

> _Fasse den bereitgestellten Inhalt so zusammen, dass ein Zweitklässler ihn versteht. Halte das Ergebnis in einem Absatz mit 3-5 Stichpunkten._

Sehen Sie, wie das Ergebnis nun auf das gewünschte Ziel und Format abgestimmt ist? Ein Lehrender kann diese Antwort direkt in seinen Folien für die Klasse verwenden.

![Instruction-Tuned LLM Chat-Vervollständigung](../../../translated_images/de/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Warum brauchen wir Prompt Engineering?

Da wir jetzt wissen, wie Prompts von LLMs verarbeitet werden, wollen wir darüber sprechen, _warum_ wir Prompt Engineering brauchen. Die Antwort liegt darin, dass aktuelle LLMs einige Herausforderungen mit sich bringen, die es erschweren, _zuverlässige und konsistente Vervollständigungen_ zu erreichen, ohne Aufwand für die Erstellung und Optimierung von Prompts zu betreiben. Zum Beispiel:

1. **Modellantworten sind stochastisch.** Dasselbe Prompt wird wahrscheinlich mit unterschiedlichen Modellen oder Modellversionen unterschiedliche Antworten erzeugen. Und es kann sogar bei _dem gleichen Modell_ zu verschiedenen Zeiten unterschiedliche Ergebnisse liefern. _Techniken des Prompt Engineering können uns helfen, diese Variationen zu minimieren, indem sie bessere Leitplanken bieten_.

1. **Modelle können Antworten erfinden.** Modelle werden mit _großen, aber endlichen_ Datensätzen vortrainiert, was bedeutet, dass sie kein Wissen über Konzepte außerhalb dieses Trainingsumfangs besitzen. Deshalb können sie Vervollständigungen erzeugen, die ungenau, erfunden oder direkt widersprüchlich zu bekannten Fakten sind. _Techniken des Prompt Engineering helfen Nutzern, solche Erfindungen zu erkennen und zu mildern, z. B. indem die KI nach Quellenangaben oder Begründungen gefragt wird_.

1. **Modelleigenschaften variieren.** Neuere Modelle oder Modellgenerationen verfügen über umfangreichere Fähigkeiten, bringen jedoch auch einzigartige Eigenheiten und Kompromisse in Bezug auf Kosten und Komplexität mit sich. _Prompt Engineering kann uns helfen, Best Practices und Workflows zu entwickeln, die Unterschiede abstrahieren und sich skalierbar und nahtlos an modellspezifische Anforderungen anpassen_.

Sehen wir das im OpenAI oder Azure OpenAI Playground in Aktion:

- Verwenden Sie dasselbe Prompt mit unterschiedlichen LLM-Bereitstellungen (z. B. OpenAI, Azure OpenAI, Hugging Face) – haben Sie die Variationen bemerkt?  
- Verwenden Sie dasselbe Prompt wiederholt mit _dem gleichen_ LLM (z. B. im Azure OpenAI Playground) – wie unterschieden sich die Variationen?

### Beispiel für Erfindungen

In diesem Kurs verwenden wir den Begriff **„Erfindung“** (fabrication), um das Phänomen zu beschreiben, dass LLMs manchmal faktisch falsche Informationen erzeugen, bedingt durch Einschränkungen im Training oder andere Beschränkungen. Sie haben vielleicht auch schon von _„Halluzinationen“_ in populären Artikeln oder Forschungsarbeiten gehört. Wir empfehlen jedoch ausdrücklich, den Begriff _„Erfindung“_ zu verwenden, um zu vermeiden, dass wir dieses Verhalten vermenschlichen, indem wir einem maschinengetriebenen Ergebnis eine menschliche Eigenschaft zuschreiben. Dies entspricht auch den [Richtlinien für verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aus terminologischer Sicht und vermeidet Begriffe, die in manchen Kontexten als anstößig oder nicht inklusiv gelten könnten.

Möchten Sie ein Gefühl dafür bekommen, wie Erfindungen entstehen? Stellen Sie sich ein Prompt vor, das die KI anweist, Inhalte für ein nicht existierendes Thema zu generieren (um sicherzugehen, dass dieses im Trainingsdatensatz nicht enthalten ist). Zum Beispiel habe ich dieses Prompt ausprobiert:

> **Prompt:** Erstelle einen Unterrichtsplan zum Mars-Krieg von 2076.
Eine Websuche zeigte mir, dass es fiktive Berichte (z. B. Fernsehserien oder Bücher) über Marskriege gibt – aber keine im Jahr 2076. Der gesunde Menschenverstand sagt uns auch, dass 2076 _in der Zukunft_ liegt und daher nicht mit einem realen Ereignis in Verbindung gebracht werden kann.

Was passiert also, wenn wir diese Eingabeaufforderung bei verschiedenen LLM-Anbietern ausführen?

> **Antwort 1**: OpenAI Playground (GPT-35)

![Antwort 1](../../../translated_images/de/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Antwort 2**: Azure OpenAI Playground (GPT-35)

![Antwort 2](../../../translated_images/de/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Antwort 3**: : Hugging Face Chat Playground (LLama-2)

![Antwort 3](../../../translated_images/de/04-fabrication-huggingchat.faf82a0a51278956.webp)

Wie erwartet erzeugt jedes Modell (bzw. jede Modellversion) aufgrund des stochastischen Verhaltens und der unterschiedlichen Modellfähigkeiten leicht unterschiedliche Antworten. Zum Beispiel richtet sich ein Modell an eine Zielgruppe der 8. Klasse, während das andere einen Schüler der Oberstufe annimmt. Aber alle drei Modelle generierten Antworten, die einen uninformierten Nutzer davon überzeugen könnten, dass das Ereignis real war.

Techniken des Prompt Engineerings wie _Metaprompting_ und _Temperaturkonfiguration_ können Modellfälschungen bis zu einem gewissen Grad reduzieren. Neue _Architekturen_ im Prompt Engineering binden außerdem nahtlos neue Werkzeuge und Techniken in den Prompt-Ablauf ein, um einige dieser Effekte abzuschwächen oder zu reduzieren.

## Fallstudie: GitHub Copilot

Schließen wir diesen Abschnitt ab, indem wir einen Eindruck davon gewinnen, wie Prompt Engineering in realen Lösungen eingesetzt wird, und betrachten dazu eine Fallstudie: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ist Ihr „KI-Pair-Programmierer“ – es wandelt Texteingaben in Codevervollständigungen um und ist in Ihre Entwicklungsumgebung (z. B. Visual Studio Code) integriert, um eine nahtlose Nutzererfahrung zu bieten. Wie in den untenstehenden Blogserien dokumentiert, basierte die erste Version auf dem OpenAI Codex-Modell – Ingenieure erkannten schnell die Notwendigkeit, das Modell feinzujustieren und bessere Prompt-Engineering-Techniken zu entwickeln, um die Codequalität zu verbessern. Im Juli stellten sie ein [verbessertes KI-Modell vor, das über Codex hinausgeht](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) und noch schnellere Vorschläge ermöglicht.

Lesen Sie die Beiträge der Reihe nach, um ihre Lernreise nachzuvollziehen.

- **Mai 2023** | [GitHub Copilot wird besser im Verstehen Ihres Codes](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub: Arbeit mit den LLMs hinter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jun 2023** | [Wie man bessere Prompts für GitHub Copilot schreibt](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [GitHub Copilot geht mit verbessertem KI-Modell über Codex hinaus](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Ein Entwicklerleitfaden zum Prompt Engineering und zu LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Wie man eine Unternehmens-LLM-App baut: Lektionen von GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Sie können auch in ihrem [Engineering-Blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) weitere Beiträge wie [diesen](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) lesen, der zeigt, wie diese Modelle und Techniken _angewandt_ werden, um reale Anwendungen zu steuern.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt-Konstruktion

Wir haben gesehen, warum Prompt Engineering wichtig ist – jetzt wollen wir verstehen, wie Prompts _konstruiert_ werden, damit wir verschiedene Techniken für ein effektiveres Prompt-Design bewerten können.

### Einfacher Prompt

Fangen wir mit dem einfachen Prompt an: eine Texteingabe, die an das Modell ohne weiteren Kontext gesendet wird. Hier ein Beispiel – wenn wir die ersten Worte der US-Nationalhymne an die OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) senden, _vervollständigt_ sie sofort die Antwort mit den nächsten Zeilen und illustriert so das grundlegende Vorhersageverhalten.

| Prompt (Eingabe)   | Vervollständigung (Ausgabe)                                                                                                                   |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Es klingt, als würden Sie gerade den Text von „The Star-Spangled Banner“ beginnen, der Nationalhymne der Vereinigten Staaten. Der vollständige Text lautet ... |

### Komplexer Prompt

Nun fügen wir Kontext und Anweisungen zu diesem einfachen Prompt hinzu. Die [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) erlaubt es uns, einen komplexen Prompt als Sammlung von _Nachrichten_ zu konstruieren mit:

- Eingabe-/Ausgabepaaren, die den _Nutzerinput_ und die _Antwort des Assistenten_ widerspiegeln.
- Systemnachricht, die den Kontext für das Verhalten oder die Persönlichkeit des Assistenten setzt.

Die Anfrage hat nun die folgende Form, wobei die _Tokenisierung_ relevante Informationen aus Kontext und Gespräch effektiv erfasst. Das Ändern des Systemkontexts kann nun ebenso wirkungsvoll die Qualität der Vervollständigungen beeinflussen wie die vom Nutzer gelieferten Eingaben.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Anweisungs-Prompt

In den obigen Beispielen war der Nutzerprompt eine einfache Textanfrage, die als Informationsanfrage interpretiert werden kann. Mit _Anweisungs-Prompts_ können wir diesen Text verwenden, um eine Aufgabe detaillierter zu spezifizieren und der KI damit bessere Vorgaben zu geben. Hier ein Beispiel:

| Prompt (Eingabe)                                                                                                                                                                                                                         | Vervollständigung (Ausgabe)                                                                                                | Anweisungstyp        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
| Schreibe eine Beschreibung des Bürgerkriegs                                                                                                                                                                                           | _gab einen einfachen Absatz zurück_                                                                                        | Einfach               |
| Schreibe eine Beschreibung des Bürgerkriegs. Gib wichtige Termine und Ereignisse an und beschreibe deren Bedeutung                                                                                                                  | _gab einen Absatz zurück, gefolgt von einer Liste mit Schlüsselterminen und den Beschreibungen_                            | Komplex               |
| Schreibe eine Beschreibung des Bürgerkriegs in 1 Absatz. Gib 3 Stichpunkte mit wichtigen Terminen und deren Bedeutung an. Gib 3 weitere Stichpunkte mit wichtigen historischen Persönlichkeiten und deren Beiträgen. Gib die Ausgabe als JSON-Datei zurück | _gibt ausführlichere Details in einem Textfeld zurück, formatiert als JSON, das Sie bei Bedarf kopieren, einfügen und validieren können_ | Komplex. Formatiert. |

## Primärer Inhalt

In den obigen Beispielen war der Prompt noch ziemlich offen, so dass das LLM selbst entscheiden konnte, welche Teile seines vortrainierten Datensatzes relevant sind. Beim Designmuster _primärer Inhalt_ wird der Eingabetext in zwei Teile gegliedert:

- eine Anweisung (Aktion)
- relevanter Inhalt (der die Aktion beeinflusst)

Hier ein Beispiel, bei dem die Anweisung lautet: „Fasse dies in 2 Sätzen zusammen“.

| Prompt (Eingabe)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Vervollständigung (Ausgabe)                                                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalb Mal so schwer wie alle anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und ist den antiken Zivilisationen seit vor der schriftlichen Aufzeichnung bekannt. Er ist nach dem römischen Gott Jupiter benannt.[19] Von der Erde aus gesehen kann Jupiter hell genug sein, um sichtbare Schatten durch reflektiertes Licht zu werfen,[20] und ist im Durchschnitt nach Mond und Venus das dritthellste natürliche Objekt am Nachthimmel. <br/> **Fasse dies in 2 kurzen Sätzen zusammen** | Jupiter, der fünfte Planet von der Sonne, ist der größte im Sonnensystem und bekannt als eines der hellsten Objekte am Nachthimmel. Er ist nach dem römischen Gott Jupiter benannt, ein Gasriese, dessen Masse zweieinhalb Mal so groß ist wie die aller anderen Planeten im Sonnensystem zusammen. |

Das primäre Inhaltssegment kann auf verschiedene Weise eingesetzt werden, um effektivere Anweisungen zu geben:

- **Beispiele** – Anstatt dem Modell mit einer expliziten Anweisung zu sagen, was zu tun ist, geben Sie ihm Beispiele für das Vorgehen und lassen es dann das Muster erkennen.
- **Hinweise** – Folgen Sie der Anweisung mit einem „Hinweis“, der die Vervollständigung anstößt und das Modell zu relevanteren Antworten führt.
- **Vorlagen** – Das sind wiederholbare „Rezepte“ für Prompts mit Platzhaltern (Variablen), die mit Daten für bestimmte Anwendungsfälle angepasst werden können.

Lassen Sie uns diese Ansätze in der Praxis erkunden.

### Verwendung von Beispielen

Dies ist ein Ansatz, bei dem der primäre Inhalt genutzt wird, um dem Modell Beispiele für die gewünschte Ausgabe einer bestimmten Anweisung zu „zufüttern“ und es das Muster der gewünschten Ausgabe erkennen zu lassen. Je nach Anzahl der bereitgestellten Beispiele spricht man von Zero-Shot-, One-Shot- oder Few-Shot-Prompting usw.

Der Prompt besteht nun aus drei Komponenten:

- Einer Aufgabenbeschreibung
- Ein paar Beispielen der gewünschten Ausgabe
- Dem Beginn eines neuen Beispiels (das zur impliziten Aufgabenbeschreibung wird)

| Lernart      | Prompt (Eingabe)                                                                                                       | Vervollständigung (Ausgabe)     |
| :----------- | :--------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
| Zero-Shot    | „Die Sonne scheint“. Übersetze ins Spanische                                                                          | „El Sol está brillando“.        |
| One-Shot     | „Die Sonne scheint“ => „El Sol está brillando“. <br> „Es ist ein kalter und windiger Tag“ =>                          | „Es un día frío y ventoso“.     |
| Few-Shot     | Der Spieler lief die Bases entlang => Baseball <br/> Der Spieler spielte einen As => Tennis <br/> Der Spieler schlug eine Sechs => Cricket <br/> Der Spieler machte einen Slam-Dunk => | Basketball                      |
|              |                                                                                                                        |                                 |

Beachten Sie, dass wir bei Zero-Shot-Prompting eine explizite Anweisung („Übersetze ins Spanische“) geben mussten, diese aber im One-Shot-Beispiel implizit erkannt wird. Das Few-Shot-Beispiel zeigt, wie durch mehr Beispiele genauere Schlussfolgerungen möglich sind, ohne weitere Anweisungen.

### Prompt-Hinweise

Eine weitere Technik für den primären Inhalt ist es, _Hinweise_ statt Beispiele zu geben. In diesem Fall geben wir dem Modell einen Anstoß in die richtige Richtung, indem wir mit einem Ausschnitt beginnen, der das gewünschte Antwortformat widerspiegelt. Das Modell „nimmt den Hinweis auf“ und setzt in diesem Stil fort.

| Anzahl der Hinweise | Prompt (Eingabe)                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Vervollständigung (Ausgabe)                                                                                                                                                                                                                                                                     |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0                   | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalb Mal so schwer wie alle anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und ist den antiken Zivilisationen seit vor der schriftlichen Aufzeichnung bekannt. <br/>**Fasse dies zusammen**                                     | Jupiter ist der größte Planet in unserem Sonnensystem und der fünfte von der Sonne entfernt. Er ist ein Gasriese mit einer Masse von 1/1000 der Sonne, aber schwerer als alle anderen Planeten zusammen. Antike Zivilisationen kennen Jupiter seit langer Zeit, und er ist am Nachthimmel leicht sichtbar.. |
| 1              | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Masse der Sonne beträgt, aber zweieinhalbmal so groß ist wie die aller anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und war den alten Zivilisationen schon vor der aufgezeichneten Geschichte bekannt. <br/>**Fasse dies zusammen** <br/> Was wir gelernt haben, ist, dass Jupiter | der fünfte Planet von der Sonne und der größte im Sonnensystem ist. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Masse der Sonne beträgt, aber zweieinhalbmal so groß wie die aller anderen Planeten zusammen. Er ist mit bloßem Auge leicht sichtbar und seit der Antike bekannt.                        |
| 2              | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Masse der Sonne beträgt, aber zweieinhalbmal so groß ist wie die aller anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und war den alten Zivilisationen schon vor der aufgezeichneten Geschichte bekannt. <br/>**Fasse dies zusammen** <br/> Top 3 Fakten, die wir gelernt haben:         | 1. Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. <br/> 2. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Masse der Sonne beträgt...<br/> 3. Jupiter ist seit der Antike mit bloßem Auge sichtbar ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Aufforderungsvorlagen

Eine Aufforderungsvorlage ist ein _vordefiniertes Rezept für eine Aufforderung_, das gespeichert und bei Bedarf wiederverwendet werden kann, um konsistentere Benutzererfahrungen im großen Maßstab zu ermöglichen. Im einfachsten Fall ist es einfach eine Sammlung von Aufforderungsbeispielen wie [dieses von OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), das sowohl die interaktiven Aufforderungskomponenten (Benutzer- und Systemnachrichten) als auch das API-gesteuerte Anfrageformat bereitstellt – um Wiederverwendung zu unterstützen.

In seiner komplexeren Form wie [dieses Beispiel von LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) enthält es _Platzhalter_, die mit Daten aus verschiedenen Quellen (Benutzereingaben, Systemkontext, externe Datenquellen etc.) ersetzt werden können, um eine Aufforderung dynamisch zu generieren. So können wir eine Bibliothek wiederverwendbarer Aufforderungen erstellen, die **programmgesteuert** im großen Maßstab konsistente Benutzererlebnisse ermöglichen.

Schließlich liegt der wahre Wert von Vorlagen in der Möglichkeit, _Bibliotheken von Aufforderungen_ für vertikale Anwendungsdomänen zu erstellen und zu veröffentlichen – wo die Aufforderungsvorlage nun _optimiert_ ist, um anwendungsspezifischen Kontext oder Beispiele widerzuspiegeln, die die Antworten für die anvisierte Benutzergruppe relevanter und genauer machen. Das [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) Repository ist ein großartiges Beispiel für diesen Ansatz und kuratiert eine Bibliothek von Aufforderungen für den Bildungsbereich mit Schwerpunkt auf Schlüsselzielen wie Unterrichtsplanung, Curriculum-Design, Schülertutoring etc.

## Unterstützende Inhalte

Wenn wir an die Konstruktion von Aufforderungen denken als bestehend aus einer Anweisung (Aufgabe) und einem Ziel (Primärinhalt), dann ist _sekundärer Inhalt_ wie zusätzlicher Kontext, den wir bereitstellen, um die Ausgabe **in gewisser Weise zu beeinflussen**. Das können Feinabstimmungsparameter, Formatierungshinweise, thematische Taxonomien etc. sein, die dem Modell helfen, seine Antwort besser auf die gewünschten Benutzerziele oder Erwartungen zuzuschneiden.

Zum Beispiel: Gegeben ein Kurskatalog mit umfangreichen Metadaten (Name, Beschreibung, Niveau, Metadaten-Tags, Dozent etc.) zu allen verfügbaren Kursen im Curriculum:

- können wir eine Anweisung definieren „Fasse den Kurskatalog für Herbst 2023 zusammen“
- können wir den Primärinhalt verwenden, um einige Beispiele der gewünschten Ausgabe bereitzustellen
- können wir den Sekundärinhalt verwenden, um die Top 5 „Tags“ von Interesse zu identifizieren.

Nun kann das Modell eine Zusammenfassung im Format der Beispiele liefern – aber wenn ein Ergebnis mehrere Tags enthält, priorisiert es die 5 im sekundären Inhalt identifizierten Tags.

---

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte das Kernkonzept Nr. 1 abdecken.
Untermauere das Konzept mit Beispielen und Referenzen.

KONZEPT #3:
Techniken zur Aufforderungsoptimierung.
Was sind einige grundlegende Techniken für die Aufforderungsoptimierung?
Veranschauliche es mit einigen Übungen.
-->

## Beste Praktiken bei Aufforderungen

Jetzt, wo wir wissen, wie Aufforderungen _konstruiert_ werden können, können wir darüber nachdenken, wie man sie _gestaltet_, um bewährte Methoden widerzuspiegeln. Wir können das in zwei Teile gliedern – die richtige _Einstellung_ und die richtigen _Techniken_ anwenden.

### Einstellung zur Aufforderungsoptimierung

Aufforderungsoptimierung ist ein Versuch-und-Irrtum-Prozess, daher sollten drei wichtige Leitgedanken im Hinterkopf behalten werden:

1. **Domänenverständnis ist wichtig.** Genauigkeit und Relevanz der Antwort hängen von der _Domäne_ ab, in der die Anwendung oder der Benutzer tätig ist. Wenden Sie Ihre Intuition und Fachexpertise an, um **Techniken weiter anzupassen**. Definieren Sie zum Beispiel _domänenspezifische Persönlichkeiten_ in Ihren Systemaufforderungen oder verwenden Sie _domänenspezifische Vorlagen_ in Ihren Benutzeraufforderungen. Stellen Sie sekundären Inhalt bereit, der domänenspezifische Kontexte widerspiegelt, oder verwenden Sie _domänenspezifische Hinweise und Beispiele_, um das Modell zu bekannten Nutzungsmustern zu führen.

2. **Modellverständnis ist wichtig.** Wir wissen, dass Modelle von Natur aus stochastisch sind. Aber Implementierungen können auch variieren hinsichtlich des Trainingsdatensatzes (vortrainiertes Wissen), der bereitgestellten Fähigkeiten (z.B. via API oder SDK) und der Art des Inhalts, für den sie optimiert sind (z.B. Code vs. Bilder vs. Text). Verstehen Sie die Stärken und Grenzen des verwendeten Modells und nutzen Sie dieses Wissen, um _Aufgaben zu priorisieren_ oder _angepasste Vorlagen_ zu erstellen, die auf die Fähigkeiten des Modells abgestimmt sind.

3. **Iteration und Validierung sind wichtig.** Modelle entwickeln sich schnell weiter, ebenso wie Techniken der Aufforderungsoptimierung. Als Fachexperte haben Sie möglicherweise weitere Kontexte oder Kriterien, die _Ihre_ spezifische Anwendung betreffen, und die nicht auf die größere Gemeinschaft zutreffen. Nutzen Sie Werkzeuge und Techniken zur Aufforderungsoptimierung, um den Bau von Aufforderungen „anzustoßen“, dann iterieren und validieren Sie die Ergebnisse anhand Ihrer eigenen Intuition und Fachkenntnis. Dokumentieren Sie Ihre Erkenntnisse und erstellen Sie eine **Wissensbasis** (z.B. Aufforderungsbibliotheken), die von anderen als neue Basis für schnellere Iterationen genutzt werden kann.

## Beste Praktiken

Sehen wir uns nun gängige bewährte Praktiken an, die von [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) und [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) empfohlen werden.

| Was                              | Warum                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bewerten Sie die neuesten Modelle.       | Neue Modelgenerationen haben wahrscheinlich verbesserte Funktionen und Qualität – verursachen aber möglicherweise auch höhere Kosten. Bewerten Sie sie hinsichtlich ihrer Auswirkungen und treffen Sie dann Migrationsentscheidungen.                                                                                |
| Trennen Sie Anweisungen und Kontext   | Prüfen Sie, ob Ihr Modell/Anbieter _Begrenzer_ definiert, um Anweisungen, Primär- und Sekundärinhalt klarer zu unterscheiden. Dies kann helfen, dass Modelle Token genauer gewichten.                                                         |
| Seien Sie spezifisch und klar             | Geben Sie mehr Details zum gewünschten Kontext, Ergebnis, Länge, Format, Stil etc. Dies verbessert sowohl die Qualität als auch die Konsistenz der Antworten. Erfassen Sie Rezepte in wiederverwendbaren Vorlagen.                                                          |
| Seien Sie beschreibend, verwenden Sie Beispiele      | Modelle reagieren oft besser auf einen „Show and Tell“-Ansatz. Beginnen Sie mit einer `zero-shot` Methode, bei der Sie nur eine Anweisung geben (ohne Beispiele), und versuchen Sie dann `few-shot` als Verfeinerung, indem Sie einige Beispiele der gewünschten Ausgabe bereitstellen. Verwenden Sie Analogien. |
| Verwenden Sie Hinweise zur Anstoßung | Stoßen Sie das Modell zu einem gewünschten Ergebnis an, indem Sie ihm einige einleitende Wörter oder Phrasen geben, die es als Ausgangspunkt für die Antwort verwenden kann.                                                                                                               |
| Verdoppeln Sie die Anweisungen                       | Manchmal müssen Sie das Modell wiederholen. Geben Sie Anweisungen vor und nach Ihrem Primärinhalt, verwenden Sie eine Anweisung und einen Hinweis usw. Iterieren und validieren Sie, um zu sehen, was funktioniert.                                                         |
| Reihenfolge ist wichtig                     | Die Reihenfolge, in der Sie Informationen dem Modell präsentieren, kann das Ergebnis beeinflussen, auch in Lernbeispielen, aufgrund von Rezenzbias. Probieren Sie verschiedene Optionen aus, um herauszufinden, was am besten funktioniert.                                                               |
| Geben Sie dem Modell eine „Ausweichmöglichkeit“           | Geben Sie dem Modell eine _Fallback_-Antwortmöglichkeit, die es geben kann, falls es aus irgendeinem Grund die Aufgabe nicht abschließen kann. Dies kann die Wahrscheinlichkeit verringern, dass Modelle falsche oder erfundene Antworten generieren.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Wie bei jeder bewährten Methode gilt: _Ihre Erfahrungen können variieren_ je nach Modell, Aufgabe und Domäne. Nutzen Sie diese als Ausgangspunkt und iterieren Sie, um herauszufinden, was für Sie am besten funktioniert. Bewerten Sie Ihren Aufforderungsoptimierungsprozess ständig neu, wenn neue Modelle und Werkzeuge verfügbar werden, mit Fokus auf Skalierbarkeit des Prozesses und Antwortqualität.

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte eine Code-Herausforderung enthalten, falls anwendbar.

HERAUSFORDERUNG:
Link zu einem Jupyter Notebook, in dem nur die Kommentare zu sehen sind (Codeabschnitte sind leer).

LÖSUNG:
Link zu einer Kopie dieses Notebooks mit ausgefüllten Aufforderungen und Ausführung, die ein Beispiel zeigt.
-->

## Aufgabe

Herzlichen Glückwunsch! Sie haben das Ende der Lektion erreicht! Es ist Zeit, einige dieser Konzepte und Techniken mit echten Beispielen zu testen!

Für unsere Aufgabe verwenden wir ein Jupyter Notebook mit Übungen, die Sie interaktiv ausführen können. Sie können das Notebook auch mit eigenen Markdown- und Codezellen erweitern, um Ideen und Techniken eigenständig zu erkunden.

### Zum Starten, forken Sie das Repository, dann

- (Empfohlen) Starten Sie GitHub Codespaces
- (Alternativ) Klonen Sie das Repository auf Ihr lokales Gerät und verwenden Sie es mit Docker Desktop
- (Alternativ) Öffnen Sie das Notebook mit Ihrer bevorzugten Notebook-Laufzeitumgebung.

### Als nächstes konfigurieren Sie Ihre Umgebungsvariablen

- Kopieren Sie die Datei `.env.copy` im Repository-Stammverzeichnis nach `.env` und füllen Sie die Werte für `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` und `AZURE_OPENAI_DEPLOYMENT` aus. Kehren Sie zur [Learning Sandbox Sektion](#lern-sandbox) zurück, um zu erfahren wie.

### Dann öffnen Sie das Jupyter Notebook

- Wählen Sie den Kernel der Laufzeitumgebung. Wenn Sie Option 1 oder 2 nutzen, wählen Sie einfach den Standard-Python-3.10.x-Kernel, der vom Dev-Container bereitgestellt wird.

Sie sind bereit, die Übungen auszuführen. Beachten Sie, dass es hier keine _richtigen oder falschen_ Antworten gibt – es geht darum, durch Ausprobieren Optionen zu erkunden und ein Gespür dafür zu entwickeln, was für ein bestimmtes Modell und eine Anwendung funktioniert.

_Aus diesem Grund gibt es in dieser Lektion keine Code-Lösungsteile. Stattdessen enthält das Notebook Markdown-Zellen mit dem Titel „Meine Lösung:“, die ein beispielhaftes Ausgabeergebnis zum Nachschlagen zeigen._

 <!--
LEKTIONSVORLAGE:
Fassen Sie den Abschnitt mit einer Zusammenfassung und Ressourcen für eigenständiges Lernen ab.
-->

## Wissenscheck

Welche der folgenden drei Aufforderungen folgt guten Praktiken?

1. Zeig mir ein Bild von einem roten Auto
2. Zeig mir ein Bild von einem roten Auto der Marke Volvo und Modell XC90, das an einer Klippe mit Sonnenuntergang parkt
3. Zeig mir ein Bild von einem roten Auto der Marke Volvo und Modell XC90

A: 2 ist die beste Aufforderung, da sie Details darüber liefert, „was“ gewünscht ist, und ins Spezifische geht (nicht irgendein Auto, sondern eine bestimmte Marke und Modell) und auch die Umgebung beschreibt. 3 ist die nächstbeste, da sie ebenfalls viele Beschreibungen enthält.

## 🚀 Herausforderung

Versuchen Sie, die „Hinweis“-Technik mit der Aufforderung zu verwenden: Vervollständige den Satz „Zeig mir ein Bild von einem roten Auto der Marke Volvo und “. Was antwortet das Modell und wie würden Sie es verbessern?

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Möchten Sie mehr über verschiedene Konzepte der Aufforderungsoptimierung erfahren? Besuchen Sie die [Seite für weiterführendes Lernen](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), um weitere großartige Ressourcen zu diesem Thema zu finden.

Besuchen Sie Lektion 5, wo wir uns [fortgeschrittene Aufforderungstechniken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) ansehen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->