# Grundlagen des Prompt Engineerings

[![Grundlagen des Prompt Engineerings](../../../translated_images/de/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Einführung
Dieses Modul behandelt grundlegende Konzepte und Techniken für die Erstellung effektiver Prompts in generativen KI-Modellen. Die Art und Weise, wie Sie Ihren Prompt an ein LLM schreiben, ist ebenfalls entscheidend. Ein sorgfältig gestalteter Prompt kann eine bessere Antwortqualität erzielen. Aber was genau bedeuten Begriffe wie _Prompt_ und _Prompt Engineering_? Und wie verbessere ich das Prompt-_Eingabe_, das ich an das LLM sende? Diese Fragen werden wir in diesem und dem nächsten Kapitel zu beantworten versuchen.

_Generative KI_ ist in der Lage, neue Inhalte (z. B. Text, Bilder, Audio, Code usw.) als Antwort auf Benutzeranfragen zu erstellen. Dies wird mit Hilfe von _Großen Sprachmodellen_ wie der GPT-Serie von OpenAI ("Generative Pre-trained Transformer") erreicht, die für die Nutzung natürlicher Sprache und Code trainiert wurden.

Benutzer können nun mit diesen Modellen über vertraute Paradigmen wie Chat interagieren, ohne technische Expertise oder Schulung zu benötigen. Die Modelle sind _promptbasiert_ – Benutzer senden eine Texteingabe (Prompt) und erhalten die KI-Antwort (Vervollständigung) zurück. Sie können dann iterativ „mit der KI chatten“ in mehrstufigen Gesprächen und ihren Prompt verfeinern, bis die Antwort ihren Erwartungen entspricht.

„Prompts“ werden nun zur primären _Programmierschnittstelle_ für generative KI-Anwendungen, indem sie den Modellen sagen, was zu tun ist, und die Qualität der zurückgegebenen Antworten beeinflussen. „Prompt Engineering“ ist ein schnell wachsendes Fachgebiet, das sich auf das _Design und die Optimierung_ von Prompts konzentriert, um konsistente und hochwertige Antworten in großem Maßstab zu liefern.

## Lernziele

In diesem Abschnitt lernen wir, was Prompt Engineering ist, warum es wichtig ist und wie wir effektivere Prompts für ein gegebenes Modell und ein bestimmtes Anwendungsziel erstellen können. Wir verstehen die Kernkonzepte und bewährte Vorgehensweisen im Prompt Engineering – und lernen eine interaktive Jupyter Notebook „Sandbox“-Umgebung kennen, in der wir diese Konzepte an realen Beispielen sehen können.

Am Ende dieses Abschnitts werden wir in der Lage sein:

1. Erklären, was Prompt Engineering ist und warum es wichtig ist.
2. Die Bestandteile eines Prompts beschreiben und wie sie verwendet werden.
3. Best Practices und Techniken im Prompt Engineering lernen.
4. Gelernte Techniken anhand realer Beispiele unter Verwendung eines OpenAI-Endpunkts anwenden.

## Schlüsselbegriffe

Prompt Engineering: Die Praxis des Entwurfs und der Verfeinerung von Eingaben, um KI-Modelle zur Erzeugung gewünschter Ausgaben zu führen.
Tokenisierung: Der Prozess der Umwandlung von Text in kleinere Einheiten, sogenannte Tokens, die ein Modell verstehen und verarbeiten kann.
Instruction-Tuned LLMs: Große Sprachmodelle (LLMs), die mit spezifischen Anweisungen feinabgestimmt wurden, um ihre Antwortgenauigkeit und Relevanz zu verbessern.

## Lern-Sandbox

Prompt Engineering ist derzeit mehr Kunst als Wissenschaft. Der beste Weg, unsere Intuition dafür zu verbessern, ist, _mehr zu üben_ und einen Trial-and-Error-Ansatz zu verfolgen, der Fachwissen im Anwendungsbereich mit empfohlenen Techniken und modellbezogenen Optimierungen kombiniert.

Das Jupyter Notebook zu diesem Abschnitt bietet eine _Sandbox_-Umgebung, in der Sie das Gelernte ausprobieren können – während des Lernens oder als Teil der Code-Challenge am Ende. Zum Ausführen der Übungen benötigen Sie:

1. **Einen Azure OpenAI API-Schlüssel** – den Dienstendpunkt für ein bereitgestelltes LLM.
2. **Eine Python-Laufzeitumgebung** – in der das Notebook ausgeführt werden kann.
3. **Lokale Umgebungsvariablen** – _schließen Sie jetzt die [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) Schritte ab, um startklar zu sein_.

Das Notebook enthält _Starter_-Übungen – Sie sind jedoch eingeladen, eigene _Markdown_- (Beschreibungen) und _Code_- (Prompt-Anfragen) Abschnitte hinzuzufügen, um weitere Beispiele oder Ideen auszuprobieren – und Ihre Intuition für das Design von Prompts zu erweitern.

## Illustrierter Leitfaden

Möchten Sie einen Überblick darüber bekommen, was dieser Abschnitt abdeckt, bevor Sie tiefer einsteigen? Sehen Sie sich diesen illustrierten Leitfaden an, der Ihnen einen Eindruck von den Hauptthemen und den wichtigsten Erkenntnissen gibt, über die Sie in jedem Thema nachdenken können. Die Roadmap des Abschnitts führt Sie vom Verständnis der Kernkonzepte und Herausforderungen bis hin zur Lösung mit relevanten Prompt-Engineering-Techniken und Best Practices. Beachten Sie, dass sich der Abschnitt „Fortgeschrittene Techniken“ in diesem Leitfaden auf Inhalte im _nächsten_ Kapitel dieses Lehrplans bezieht.

![Illustrierter Leitfaden zum Prompt Engineering](../../../translated_images/de/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Unser Startup

Sprechen wir nun darüber, wie _dieses Thema_ mit unserer Startup-Mission verbunden ist, [KI-Innovation in die Bildung zu bringen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Wir wollen KI-gestützte Anwendungen für _personalisiertes Lernen_ entwickeln – also denken wir darüber nach, wie verschiedene Nutzer unserer Anwendung Prompts "gestalten" könnten:

- **Administratoren** könnten die KI bitten, _Lehrplandaten zu analysieren, um Lücken in der Abdeckung zu identifizieren_. Die KI kann die Ergebnisse zusammenfassen oder sie mit Code visualisieren.
- **Lehrkräfte** könnten die KI bitten, _einen Unterrichtsplan für ein Zielpublikum und Thema zu erstellen_. Die KI kann den personalisierten Plan in einem vorgegebenen Format erstellen.
- **Schülerinnen und Schüler** könnten die KI bitten, _sie in einem schwierigen Fach zu unterrichten_. Die KI kann nun die Lernenden mit Lektionen, Hinweisen und Beispielen auf ihrem Niveau begleiten.

Das ist nur die Spitze des Eisbergs. Schauen Sie sich [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) an – eine Open-Source-Prompt-Bibliothek, die von Bildungsexperten kuratiert wird – um einen umfassenderen Eindruck von den Möglichkeiten zu bekommen! _Probieren Sie einige dieser Prompts in der Sandbox oder im OpenAI Playground aus und sehen Sie, was passiert!_

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte Kernkonzept #1 abdecken.
Verstärken Sie das Konzept mit Beispielen und Verweisen.

KONZEPT #1:
Prompt Engineering.
Definieren Sie es und erklären Sie, warum es benötigt wird.
-->

## Was ist Prompt Engineering?

Wir haben diese Lektion begonnen, indem wir **Prompt Engineering** als den Prozess definiert haben, Texteingaben (Prompts) zu _entwerfen und zu optimieren_, um konsistente und qualitativ hochwertige Antworten (Vervollständigungen) für ein bestimmtes Anwendungsziel und Modell zu liefern. Wir können dies als einen 2-Schritte-Prozess betrachten:

- den initialen Prompt für ein gegebenes Modell und Ziel _entwerfen_
- den Prompt iterativ _verfeinern_, um die Qualität der Antwort zu verbessern

Dies ist notwendigerweise ein Trial-and-Error-Prozess, der Benutzerintuition und -aufwand erfordert, um optimale Ergebnisse zu erzielen. Warum ist das also wichtig? Um diese Frage zu beantworten, müssen wir zuerst drei Konzepte verstehen:

- _Tokenisierung_ = wie das Modell den Prompt „sieht“
- _Basis-LLMs_ = wie das Basismodell einen Prompt „verarbeitet“
- _instruction-tuned LLMs_ = wie das Modell nun „Aufgaben“ sehen kann

### Tokenisierung

Ein LLM sieht Prompts als _Sequenz von Tokens_, wobei verschiedene Modelle (oder Modellversionen) denselben Prompt unterschiedlich tokenisieren können. Da LLMs auf Tokens (und nicht auf rohem Text) trainiert werden, hat die Art der Tokenisierung von Prompts direkten Einfluss auf die Qualität der generierten Antwort.

Um ein Gefühl dafür zu bekommen, wie die Tokenisierung funktioniert, probieren Sie Tools wie den [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) aus, der unten gezeigt wird. Kopieren Sie Ihren Prompt hinein und sehen Sie, wie er in Tokens umgewandelt wird, und achten Sie darauf, wie Leerzeichen und Satzzeichen behandelt werden. Beachten Sie, dass dieses Beispiel ein älteres LLM (GPT-3) zeigt – ein Versuch mit einem neueren Modell könnte zu einem anderen Ergebnis führen.

![Tokenisierung](../../../translated_images/de/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konzept: Foundation Models

Sobald ein Prompt tokenisiert ist, besteht die Hauptfunktion des ["Basis-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (oder Foundation Modells) darin, das nächste Token in der Sequenz vorherzusagen. Da LLMs auf riesigen Textdatensätzen trainiert werden, haben sie ein gutes Verständnis für statistische Zusammenhänge zwischen Tokens und können diese Vorhersage mit einiger Sicherheit treffen. Beachten Sie, dass sie die _Bedeutung_ der Wörter im Prompt oder Token nicht verstehen; sie erkennen nur ein Muster, das sie mit ihrer nächsten Vorhersage „vervollständigen“ können. Sie können die Sequenz weiterhin vorhersagen, bis diese durch eine Benutzereingabe oder eine vorher festgelegte Bedingung beendet wird.

Möchten Sie sehen, wie promptbasierte Vervollständigung funktioniert? Geben Sie den obigen Prompt im [Microsoft Foundry Playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) mit den Standardeinstellungen ein. Das System ist so konfiguriert, dass Prompts als Informationsanfragen behandelt werden – Sie sollten also eine Antwort sehen, die diesen Kontext erfüllt.

Aber was, wenn der Benutzer etwas Spezifisches sehen möchte, das bestimmte Kriterien oder ein Aufgabenziel erfüllt? Hier kommen _instruction-tuned_ LLMs ins Spiel.

![Base LLM Chat Completion](../../../translated_images/de/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konzept: Instruction Tuned LLMs

Ein [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) baut auf dem Foundation Model auf und verfeinert es mit Beispielen oder Eingabe-/Ausgabepaaren (z. B. mehrstufige „Nachrichten“), die klare Anweisungen enthalten können – und die Antwort der KI versucht, dieser Anweisung zu folgen.

Dabei werden Techniken wie Reinforcement Learning mit menschlichem Feedback (RLHF) verwendet, die das Modell darin trainieren, _Anweisungen zu befolgen_ und _aus Feedback zu lernen_, sodass es Antworten erzeugt, die besser für praktische Anwendungen geeignet und relevanter für die Ziele der Benutzer sind.

Probieren wir es aus – nehmen Sie den obigen Prompt und ändern Sie nun die _Systemnachricht_, um die folgende Anweisung als Kontext bereitzustellen:

> _Fassen Sie Inhalte, die Sie erhalten, für eine/n Zweitklässler/in zusammen. Halten Sie das Ergebnis in einem Absatz mit 3–5 Aufzählungspunkten._

Sehen Sie, wie das Ergebnis nun darauf abgestimmt ist, das gewünschte Ziel und Format widerzuspiegeln? Eine Lehrkraft kann diese Antwort nun direkt in ihre Folien für diesen Unterricht verwenden.

![Instruction Tuned LLM Chat Completion](../../../translated_images/de/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Warum brauchen wir Prompt Engineering?

Nun, da wir wissen, wie Prompts von LLMs verarbeitet werden, sprechen wir darüber, _warum_ Prompt Engineering notwendig ist. Die Antwort liegt darin, dass aktuelle LLMs eine Reihe von Herausforderungen mit sich bringen, die es erschweren, _zuverlässige und konsistente Vervollständigungen_ ohne Aufwand bei der Prompt-Konstruktion und -Optimierung zu erreichen. Zum Beispiel:

1. **Modellantworten sind stochastisch.** Derselbe Prompt wird wahrscheinlich unterschiedliche Antworten mit verschiedenen Modellen oder Modellversionen erzeugen. Und er kann sogar bei _dem gleichen Modell_ zu unterschiedlichen Zeiten verschiedene Ergebnisse liefern. _Prompt Engineering-Techniken können helfen, diese Variationen durch bessere Leitplanken zu minimieren_.

1. **Modelle können Antworten erfinden.** Modelle sind mit _großen, aber endlichen_ Datensätzen vortrainiert, was bedeutet, dass ihnen Wissen über Konzepte außerhalb dieses Trainings fehlt. Daher können sie Vervollständigungen erzeugen, die ungenau, erfunden oder direkt widersprüchlich zu bekannten Fakten sind. _Prompt Engineering-Techniken helfen Nutzern, solche Erfindungen zu erkennen und zu mildern, z. B. indem sie die KI um Nachweise oder Begründungen bitten_.

1. **Die Fähigkeiten der Modelle variieren.** Neuere Modelle oder Modellgenerationen haben umfangreichere Fähigkeiten, bringen aber auch eigene Besonderheiten und Kompromisse bei Kosten und Komplexität mit sich. _Prompt Engineering kann helfen, Best Practices und Arbeitsabläufe zu entwickeln, die Unterschiede abstrahieren und sich modell-spezifisch skalierbar und nahtlos anpassen_.

Sehen wir uns das im OpenAI- oder Azure OpenAI Playground in Aktion an:

- Verwenden Sie denselben Prompt mit verschiedenen LLM-Bereitstellungen (z. B. OpenAI, Azure OpenAI, Hugging Face) – haben Sie die Unterschiede bemerkt?
- Verwenden Sie denselben Prompt mehrfach mit _dem gleichen_ LLM (z. B. Azure OpenAI Playground) – wie unterschieden sich diese Variationen?

### Beispiel für Erfindungen

In diesem Kurs verwenden wir den Begriff **„Erfindung“**, um das Phänomen zu beschreiben, bei dem LLMs manchmal aufgrund von Beschränkungen ihres Trainings oder anderer Faktoren faktisch falsche Informationen generieren. Sie haben das vielleicht auch schon als _„Halluzinationen“_ in populären Artikeln oder Forschungsarbeiten gehört. Wir empfehlen jedoch dringend, den Begriff _„Erfindung“_ zu verwenden, um nicht versehentlich das Verhalten zu vermenschlichen, indem wir einer maschinengesteuerten Ausgabe eine menschliche Eigenschaft zuschreiben. Dies unterstützt auch die [Richtlinien für verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aus Sicht der Terminologie, indem Begriffe vermieden werden, die in manchen Kontexten als beleidigend oder nicht inklusiv angesehen werden könnten.

Möchten Sie ein Gefühl dafür bekommen, wie Erfindungen entstehen? Denken Sie an einen Prompt, der die KI anweist, Inhalte zu einem nicht existierenden Thema zu generieren (um sicherzustellen, dass es nicht im Trainingsdatensatz enthalten ist). Zum Beispiel habe ich diesen Prompt ausprobiert:

> **Prompt:** Erstelle einen Unterrichtsplan zum Marskrieg von 2076.

Eine Websuche zeigte mir, dass es fiktive Darstellungen (z. B. Fernsehserien oder Bücher) über Marskriege gab – aber keine im Jahr 2076. Der gesunde Menschenverstand sagt uns auch, dass 2076 _in der Zukunft_ liegt und daher keinem realen Ereignis zugeordnet werden kann.


Was passiert also, wenn wir diese Eingabeaufforderung mit verschiedenen LLM-Anbietern ausführen?

> **Antwort 1**: OpenAI Playground (GPT-35)

![Antwort 1](../../../translated_images/de/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Antwort 2**: Azure OpenAI Playground (GPT-35)

![Antwort 2](../../../translated_images/de/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Antwort 3**: : Hugging Face Chat Playground (LLama-2)

![Antwort 3](../../../translated_images/de/04-fabrication-huggingchat.faf82a0a51278956.webp)

Wie erwartet erzeugt jedes Modell (oder jede Modellversion) aufgrund stochastischen Verhaltens und unterschiedlicher Modellfähigkeiten leicht unterschiedliche Antworten. Zum Beispiel richtet sich ein Modell an eine 8. Klasse, während das andere einen Gymnasiasten voraussetzt. Aber alle drei Modelle generierten Antworten, die einen uninformierten Benutzer davon überzeugen könnten, dass das Ereignis real war.

Eingabekonstruktionstechniken wie _Metaprompting_ und _Temperaturkonfiguration_ können Modell-Fälschungen bis zu einem gewissen Grad reduzieren. Neue Eingabekonstruktions-_Architekturen_ integrieren zudem nahtlos neue Werkzeuge und Techniken in den Eingabefluss, um einige dieser Effekte zu mildern oder zu verringern.

## Fallstudie: GitHub Copilot

Lassen Sie uns diesen Abschnitt abschließen, indem wir einen Eindruck davon bekommen, wie Eingabekonstruktion in realen Lösungen verwendet wird, indem wir eine Fallstudie betrachten: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ist dein „KI-Paarprogrammierer“ – es wandelt Texteingaben in Codevervollständigungen um und ist in deine Entwicklungsumgebung (z. B. Visual Studio Code) für ein nahtloses Benutzererlebnis integriert. Wie in der untenstehenden Blogserie dokumentiert, basierte die früheste Version auf dem OpenAI Codex-Modell – wobei die Entwickler schnell erkannten, dass das Modell feinjustiert und bessere Eingabekonstruktionstechniken entwickelt werden müssen, um die Codequalität zu verbessern. Im Juli haben sie [ein verbessertes KI-Modell vorgestellt, das über Codex hinausgeht](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) für noch schnellere Vorschläge.

Lesen Sie die Beiträge in der Reihenfolge, um ihrer Lernreise zu folgen.

- **Mai 2023** | [GitHub Copilot wird immer besser im Verstehen deines Codes](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub: Arbeiten mit den LLMs hinter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Wie man bessere Eingabeaufforderungen für GitHub Copilot schreibt](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot geht mit verbessertem KI-Modell über Codex hinaus](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Ein Entwicklerleitfaden für Eingabekonstruktion und LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Wie man eine Unternehmens-LLM-App baut: Lektionen von GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kannst auch ihren [Engineering-Blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) für weitere Beiträge wie [diesen](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) durchstöbern, der zeigt, wie diese Modelle und Techniken _angewandt_ werden, um reale Anwendungen zu steuern.

---

<!--
LEKTIONSVORLAGE:
Diese Einheit sollte das Kernkonzept #2 behandeln.
Verstärken Sie das Konzept mit Beispielen und Verweisen.

KONZEPT #2:
Eingabekonstruktion.
Veranschaulicht mit Beispielen.
-->

## Eingabekonstruktion

Wir haben gesehen, warum Eingabekonstruktion wichtig ist – nun wollen wir verstehen, wie Eingaben _konstruiert_ werden, damit wir verschiedene Techniken für ein effektiveres Eingabedesign bewerten können.

### Grundlegende Eingabe

Beginnen wir mit der grundlegenden Eingabe: eine Texteingabe, die ohne weiteren Kontext an das Modell gesendet wird. Hier ein Beispiel – wenn wir die ersten paar Worte der US-Nationalhymne an die OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) senden, vervollständigt sie sofort die Antwort mit den nächsten Zeilen, was das grundlegende Vorhersageverhalten illustriert.

| Eingabe (Input)      | Vervollständigung (Output)                                                                                                                |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see  | Es klingt so, als würdest du die Liedtexte zu „The Star-Spangled Banner“, der Nationalhymne der Vereinigten Staaten, beginnen. Der vollständige Text lautet ... |

### Komplexe Eingabe

Nun fügen wir diesem grundlegenden Prompt Kontext und Anweisungen hinzu. Die [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ermöglicht es uns, eine komplexe Eingabe als Sammlung von _Nachrichten_ zu konstruieren mit:

- Eingabe/Ausgabe-Paaren, die den _Benutzer_-Eingaben und der _Assistent_-Antwort entsprechen.
- Systemnachricht, die den Kontext für das Verhalten oder die Persönlichkeit des Assistenten festlegt.

Die Anfrage hat nun die folgende Form, wobei die _Tokenisierung_ relevante Informationen aus Kontext und Konversation effektiv erfasst. Das Ändern des Systemkontexts kann nun ebenso großen Einfluss auf die Qualität der Vervollständigungen haben wie die bereitgestellten Benutzereingaben.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Anweisungs-Prompt

In den obigen Beispielen war die Benutzereingabe eine einfache Textanfrage, die als Informationsanfrage interpretiert werden kann. Mit _Anweisungs_-Prompts können wir diesen Text verwenden, um eine Aufgabe detaillierter zu spezifizieren und der KI damit bessere Anleitungen zu geben. Hier ein Beispiel:

| Eingabe (Input)                                                                                                                                                                                                                          | Vervollständigung (Output)                                                                                  | Anweisungstyp     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----------------- |
| Schreibe eine Beschreibung des Bürgerkriegs                                                                                                                                                                                            | _gab einen einfachen Absatz zurück_                                                                             | Einfach            |
| Schreibe eine Beschreibung des Bürgerkriegs. Nenne wichtige Daten und Ereignisse und beschreibe ihre Bedeutung                                                                                                                        | _gab einen Absatz gefolgt von einer Liste wichtiger Ereignisdaten mit Beschreibungen zurück_                      | Komplex            |
| Schreibe eine Beschreibung des Bürgerkriegs in 1 Absatz. Gib 3 Stichpunkte mit wichtigen Daten und deren Bedeutung. Gib 3 weitere Stichpunkte mit wichtigen historischen Persönlichkeiten und deren Beiträgen. Gib die Ausgabe als JSON-Datei zurück | _liefert ausführlichere Details in einem Textfeld zurück, formatiert als JSON, das kopiert, eingefügt und bei Bedarf validiert werden kann_ | Komplex. Formatiert. |

## Primäre Inhalte

In den obigen Beispielen war die Eingabe noch ziemlich offen gestaltet, wodurch das LLM selbst entscheiden konnte, welcher Teil seines vortrainierten Datensatzes relevant ist. Mit dem Designmuster _primäre Inhalte_ wird der Eingabetext in zwei Teile gegliedert:

- eine Anweisung (Aktion)
- relevante Inhalte (die die Aktion beeinflussen)

Hier ein Beispiel, bei dem die Anweisung lautet: „Fasse dies in 2 Sätzen zusammen“.

| Eingabe (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Vervollständigung (Output)                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalbmal so groß wie alle anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und war den alten Zivilisationen schon vor der aufgezeichneten Geschichte bekannt. Er ist nach dem römischen Gott Jupiter benannt.[19] Von der Erde aus gesehen kann Jupiter hell genug sein, um sichtbare Schatten zu werfen,[20] und ist durchschnittlich das dritthellste natürliche Objekt am Nachthimmel nach Mond und Venus. <br/> **Fasse dies in 2 kurzen Sätzen zusammen** | Jupiter, der fünfte Planet von der Sonne, ist der größte im Sonnensystem und bekannt als eines der hellsten Objekte am Nachthimmel. Benannt nach dem römischen Gott Jupiter, ist er ein Gasriese, dessen Masse zweieinhalbmal so groß ist wie die aller anderen Planeten im Sonnensystem zusammen. |

Das Segment für primäre Inhalte kann auf verschiedene Weise verwendet werden, um effektivere Anweisungen zu geben:

- **Beispiele** – statt dem Modell eine explizite Anweisung zu geben, gib ihm Beispiele, was es tun soll, und lass es das Muster ableiten.
- **Hinweise** – Folge der Anweisung mit einem „Hinweis“, der die Vervollständigung stimuliert und das Modell zu relevanteren Antworten führt.
- **Vorlagen** – das sind wiederholbare „Rezepte“ für Prompts mit Platzhaltern (Variablen), die mit Daten für spezifische Anwendungsfälle angepasst werden können.

Schauen wir uns diese in der Praxis an.

### Verwendung von Beispielen

Dies ist ein Ansatz, bei dem du die primären Inhalte nutzt, um dem Modell einige Beispiele für die gewünschte Ausgabe einer bestimmten Anweisung zu „füttern“ und es das Muster für die gewünschte Ausgabe ableiten lässt. Je nach Anzahl der bereitgestellten Beispiele spricht man von Zero-Shot-Prompting, One-Shot-Prompting, Few-Shot-Prompting etc.

Die Eingabe besteht nun aus drei Komponenten:

- Einer Aufgabenbeschreibung
- Einer Reihe von Beispielen für die gewünschte Ausgabe
- Dem Beginn eines neuen Beispiels (das zur impliziten Aufgabenbeschreibung wird)

| Lernmodus     | Eingabe (Input)                                                                                                                                | Vervollständigung (Output)     |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
| Zero-Shot    | „Die Sonne scheint“. Übersetze ins Spanische                                                                                                   | „El Sol está brillando“.        |
| One-Shot     | „Die Sonne scheint“ => „El Sol está brillando“. <br> „Es ist ein kalter und windiger Tag“ =>                                                  | „Es un día frío y ventoso“.     |
| Few-Shot     | Der Spieler umrannte die Bases => Baseball <br/> Der Spieler erzielte ein Ass => Tennis <br/> Der Spieler erzielte eine Sechs => Cricket <br/> Der Spieler machte einen Slam-Dunk => | Basketball                      |
|              |                                                                                                                                                |                               |

Beachte, wie wir bei Zero-Shot-Prompting eine explizite Anweisung („Übersetze ins Spanische“) geben mussten, die im One-Shot-Beispiel implizit abgeleitet wird. Das Few-Shot-Beispiel zeigt, wie mehr Beispiele den Modellen helfen, genauere Schlüsse ohne weitere Anweisungen zu ziehen.

### Eingabehinweise

Eine weitere Technik bei der Verwendung von primären Inhalten ist, _Hinweise_ anstelle von Beispielen zu geben. In diesem Fall geben wir dem Modell einen Anstoß in die richtige Richtung, indem wir es mit einem Ausschnitt starten lassen, der das gewünschte Antwortformat widerspiegelt. Das Modell „nimmt den Hinweis“ auf und setzt in diesem Stil fort.

| Anzahl der Hinweise | Eingabe (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Vervollständigung (Output)                                                                                                                                                                                                                                                                      |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0                  | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalbmal so groß wie alle anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und war den alten Zivilisationen schon vor der aufgezeichneten Geschichte bekannt. <br/>**Fasse das zusammen**                              | Jupiter ist der größte Planet in unserem Sonnensystem und der fünfte von der Sonne entfernt. Er ist ein Gasriese mit einer Masse von 1/1000 der Sonnenmasse, aber schwerer als alle anderen Planeten zusammen. Alte Zivilisationen kennen Jupiter seit langer Zeit, und er ist am Nachthimmel leicht sichtbar. |
| 1                  | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalbmal so groß wie alle anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten Objekte, die mit bloßem Auge am Nachthimmel sichtbar sind, und war den alten Zivilisationen schon vor der aufgezeichneten Geschichte bekannt. <br/>**Fasse das zusammen** <br/> Was wir gelernt haben, ist, dass Jupiter | der fünfte Planet von der Sonne und der größte im Sonnensystem ist. Er ist ein Gasriese mit einer Masse von einem Tausendstel der Sonne, aber zweieinhalbmal so groß wie alle anderen Planeten zusammen. Er ist mit bloßem Auge gut sichtbar und seit der Antike bekannt.                       |

| 2              | Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt, aber zweieinhalbmal so groß wie die aller anderen Planeten im Sonnensystem zusammen. Jupiter ist eines der hellsten mit bloßem Auge sichtbaren Objekte am Nachthimmel und ist seit der Antike bekannt. <br/>**Fassen Sie dies zusammen** <br/> Top 3 Fakten, die wir gelernt haben:         | 1. Jupiter ist der fünfte Planet von der Sonne und der größte im Sonnensystem. <br/> 2. Er ist ein Gasriese mit einer Masse, die ein Tausendstel der Sonne beträgt...<br/> 3. Jupiter ist seit der Antike mit bloßem Auge sichtbar ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-Vorlagen

Eine Prompt-Vorlage ist ein _vordefiniertes Rezept für einen Prompt_, das gespeichert und bei Bedarf wiederverwendet werden kann, um konsistentere Nutzererfahrungen in großem Maßstab zu gewährleisten. In seiner einfachsten Form ist es einfach eine Sammlung von Prompt-Beispielen wie [diesem von OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), die sowohl die interaktiven Prompt-Komponenten (Benutzer- und Systemnachrichten) als auch das API-gesteuerte Anfrageformat bereitstellt – zur Unterstützung der Wiederverwendung.

In seiner komplexeren Form, wie [diesem Beispiel von LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), enthält es _Platzhalter_, die mit Daten aus verschiedenen Quellen (Benutzereingaben, Systemkontext, externe Datenquellen usw.) ersetzt werden können, um einen Prompt dynamisch zu erzeugen. Das ermöglicht es uns, eine Bibliothek wiederverwendbarer Prompts zu erstellen, die **programmatisch** in großem Maßstab konsistente Nutzererfahrungen ermöglichen.

Schließlich liegt der eigentliche Wert von Vorlagen in der Fähigkeit, _Prompt-Bibliotheken_ für vertikale Anwendungsbereiche zu erstellen und zu veröffentlichen – bei denen die Prompt-Vorlage nun _optimiert_ ist, um anwendungsspezifischen Kontext oder Beispiele zu reflektieren, die die Antworten für die Zielgruppe relevanter und genauer machen. Das [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) Repository ist ein großartiges Beispiel für diesen Ansatz. Es stellt eine Bibliothek von Prompts für den Bildungsbereich zusammen mit Schwerpunkt auf wichtigen Zielen wie Unterrichtsplanung, Curriculum-Design, Schülernachhilfe usw.

## Unterstützender Inhalt

Wenn wir Prompt-Konstruktion so betrachten, dass eine Anweisung (Aufgabe) und ein Ziel (primärer Inhalt) vorliegen, dann ist _sekundärer Inhalt_ wie zusätzlicher Kontext, den wir bereitstellen, um die Ausgabe in irgendeiner Weise zu **beeinflussen**. Das könnten Feinabstimmungsparameter, Formatierungsanweisungen, Themen-Taxonomien usw. sein, die dem Modell helfen, seine Antwort an die gewünschten Nutzerziele oder Erwartungen _anzupassen_.

Zum Beispiel: Angenommen, wir haben einen Kurskatalog mit umfangreichen Metadaten (Name, Beschreibung, Niveau, Metadaten-Tags, Dozent usw.) zu allen vorhandenen Kursen im Curriculum:

- wir können eine Anweisung definieren, um den Kurskatalog für Herbst 2023 zusammenzufassen
- wir können den primären Inhalt verwenden, um einige Beispiele des gewünschten Outputs bereitzustellen
- wir können den sekundären Inhalt verwenden, um die Top 5 „Tags“ von Interesse zu identifizieren.

Nun kann das Modell eine Zusammenfassung im Format der wenigen Beispiele liefern – aber falls ein Ergebnis mehrere Tags enthält, kann es die 5 im sekundären Inhalt identifizierten Tags priorisieren.

---

<!--
UNTERRICHTSVORLAGE:
Diese Einheit sollte Konzept #1 abdecken.
Verstärken Sie das Konzept mit Beispielen und Referenzen.

KONZEPT #3:
Prompt-Engineering-Techniken.
Was sind einige grundlegende Techniken des Prompt-Engineerings?
Veranschaulichen Sie dies mit einigen Übungen.
-->

## Beste Praktiken für Prompting

Jetzt, da wir wissen, wie Prompts _konstruiert_ werden können, können wir anfangen, darüber nachzudenken, wie man sie _gestaltet_, um bewährte Verfahren widerzuspiegeln. Wir können dies in zwei Teile gliedern – die richtige _Einstellung_ und die Anwendung der richtigen _Techniken_.

### Denkweise beim Prompt-Engineering

Prompt Engineering ist ein Prozess von Versuch und Irrtum, daher sollten Sie drei breit gefasste Leitfaktoren im Auge behalten:

1. **Domänenverständnis ist wichtig.** Die Genauigkeit und Relevanz der Antwort hängt von der _Domäne_ ab, in der die Anwendung oder der Nutzer operiert. Wenden Sie Ihre Intuition und Domänenexpertise an, um **Techniken weiter anzupassen**. Definieren Sie z.B. _domänenspezifische Persönlichkeiten_ in Ihren Systemprompts oder verwenden Sie _domänenspezifische Vorlagen_ in Ihren Benutzerprompts. Stellen Sie sekundären Inhalt bereit, der domänenspezifische Kontexte widerspiegelt, oder verwenden Sie _domänenspezifische Hinweise und Beispiele_, um das Modell zu vertrauten Nutzungsmustern zu führen.

2. **Modellverständnis ist wichtig.** Wir wissen, dass Modelle von Natur aus stochastisch sind. Aber Modellimplementierungen können sich auch in Bezug auf den verwendeten Trainingsdatensatz (vorgefertigtes Wissen), die bereitgestellten Fähigkeiten (z.B. über API oder SDK) und die Art des Contents, für den sie optimiert sind (z.B. Code vs. Bilder vs. Text) unterscheiden. Verstehen Sie die Stärken und Grenzen des von Ihnen verwendeten Modells und nutzen Sie dieses Wissen, um _Aufgaben zu priorisieren_ oder _angepasste Vorlagen_ zu erstellen, die auf die Fähigkeiten des Modells optimiert sind.

3. **Iteration und Validierung sind wichtig.** Modelle entwickeln sich schnell weiter, und das gilt auch für die Techniken des Prompt-Engineerings. Als Domänenexperte haben Sie möglicherweise anderen Kontext oder Kriterien für _Ihre_ spezifische Anwendung, die nicht für die breitere Gemeinschaft gelten. Nutzen Sie Tools und Techniken des Prompt-Engineerings, um den Promptbau zu "starten", iterieren und überprüfen Sie die Ergebnisse dann mit Ihrer eigenen Intuition und Domänenexpertise. Dokumentieren Sie Ihre Erkenntnisse und erstellen Sie eine **Wissensbasis** (z.B. Prompt-Bibliotheken), die von anderen als neue Basis für schnellere Iterationen genutzt werden kann.

## Beste Praktiken

Sehen wir uns nun gängige Best Practices an, die von [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) und [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) Praktikern empfohlen werden.

| Was                              | Warum                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bewerten Sie die neuesten Modelle.       | Neue Modelleditionen verfügen wahrscheinlich über verbesserte Funktionen und Qualität – können aber auch höhere Kosten verursachen. Bewerten Sie sie hinsichtlich ihrer Wirkung und treffen Sie dann Migrationsentscheidungen.                                                                                |
| Trennen Sie Anweisungen & Kontext   | Prüfen Sie, ob Ihr Modell/Anbieter _Begrenzer_ definiert, um Anweisungen, primären und sekundären Inhalt klarer zu unterscheiden. Dies kann helfen, dass Modelle Tokens genauer gewichten.                                                         |
| Seien Sie spezifisch und klar             | Geben Sie mehr Details über den gewünschten Kontext, das Ergebnis, die Länge, das Format, den Stil usw. an. Das verbessert sowohl Qualität als auch Konsistenz der Antworten. Halten Sie Rezepte in wiederverwendbaren Vorlagen fest.                                                          |
| Verwenden Sie Beispiele und Hinweise      | Modelle reagieren oft besser auf einen "zeigen und erzählen"-Ansatz. Beginnen Sie mit einem `Zero-Shot`-Ansatz, bei dem Sie eine Anweisung geben (aber keine Beispiele), und versuchen Sie dann `Few-Shot` als Verfeinerung, indem Sie einige Beispiele für den gewünschten Output liefern. Verwenden Sie Analogien. |
| Nutzen Sie Hinweise, um Antworten zu starten | Schubsen Sie das Modell zu einem gewünschten Ergebnis, indem Sie ihm einige führende Wörter oder Phrasen geben, die es als Startpunkt für die Antwort verwenden kann.                                                                                                               |
| Doppelte Anweisungen                       | Manchmal müssen Sie sich gegenüber dem Modell wiederholen. Geben Sie Anweisungen vor und nach Ihrem primären Inhalt, verwenden Sie Anweisung und Hinweis usw. Iterieren und validieren Sie, um herauszufinden, was funktioniert.                                                         |
| Reihenfolge ist wichtig                   | Die Reihenfolge, in der Sie Informationen dem Modell präsentieren, kann die Ausgabe beeinflussen, auch bei den Lernbeispielen, aufgrund des Rückgriffeffekts. Probieren Sie verschiedene Optionen aus, um zu sehen, was am besten funktioniert.                                                               |
| Geben Sie dem Modell eine „Ausweichmöglichkeit“ | Bieten Sie dem Modell eine _Fallback_-Antwort, die es geben kann, wenn es die Aufgabe aus irgendeinem Grund nicht erfüllen kann. Dies kann helfen, die Wahrscheinlichkeit von falschen oder erfundenen Antworten zu reduzieren.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Wie bei jeder Best Practice gilt: _Ihre Erfahrungen können variieren_ je nach Modell, Aufgabe und Domäne. Nutzen Sie diese als Ausgangspunkt und iterieren Sie, um das für Sie Beste zu finden. Bewerten Sie Ihren Prompt-Engineering-Prozess ständig neu, wenn neue Modelle und Tools verfügbar werden, mit Fokus auf Skalierbarkeit des Prozesses und Qualität der Antworten.

<!--
UNTERRICHTSVORLAGE:
Diese Einheit sollte, falls anwendbar, eine Code-Herausforderung bereitstellen.

HERAUSFORDERUNG:
Verlinken Sie zu einem Jupyter Notebook, das nur codebezogene Kommentare in den Anweisungen enthält (Code-Sektionen sind leer).

LÖSUNG:
Verlinken Sie zu einer Kopie dieses Notebooks mit ausgefüllten und ausgeführten Prompts, die zeigen, wie ein Beispiel aussehen könnte.
-->

## Aufgabe

Glückwunsch! Sie haben das Ende der Lektion erreicht! Jetzt ist es an der Zeit, einige dieser Konzepte und Techniken mit echten Beispielen zu testen!

Für unsere Aufgabe verwenden wir ein Jupyter Notebook mit Übungen, die Sie interaktiv bearbeiten können. Sie können das Notebook auch mit eigenen Markdown- und Code-Zellen erweitern, um Ideen und Techniken eigenständig zu erkunden.

### Zum Start forken Sie das Repository und dann

- (Empfohlen) Starten Sie GitHub Codespaces
- (Alternativ) Klonen Sie das Repository auf Ihr lokales Gerät und verwenden Sie es mit Docker Desktop
- (Alternativ) Öffnen Sie das Notebook mit Ihrer bevorzugten Notebook-Laufzeitumgebung.

### Konfigurieren Sie als Nächstes Ihre Umgebungsvariablen

- Kopieren Sie die Datei `.env.copy` im Repository-Stammverzeichnis nach `.env` und füllen Sie die Werte für `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` und `AZURE_OPENAI_DEPLOYMENT` aus. Kehren Sie danach zur [Learning Sandbox Sektion](#lern-sandbox) zurück, um zu erfahren, wie das geht.

### Öffnen Sie anschließend das Jupyter Notebook

- Wählen Sie den Laufzeit-Kernel aus. Bei Verwendung von Option 1 oder 2 wählen Sie einfach den Standard-Python-3.10.x-Kernel, der vom Entwicklungscontainer bereitgestellt wird.

Sie sind bereit, die Übungen auszuführen. Beachten Sie, dass es hier keine _richtigen oder falschen_ Antworten gibt – es geht darum, Optionen durch Versuch und Irrtum zu erkunden und ein Gefühl dafür zu entwickeln, was für ein bestimmtes Modell und eine Domäne funktioniert.

_Aus diesem Grund gibt es in dieser Lektion keine Code-Lösungsabschnitte. Stattdessen enthält das Notebook Markdown-Zellen mit dem Titel "Meine Lösung:", die als Referenz ein Beispiel für eine Ausgabe zeigen._

 <!--
UNTERRICHTSVORLAGE:
Schließen Sie den Abschnitt mit einer Zusammenfassung und Ressourcen für selbstständiges Lernen ab.
-->

## Wissensüberprüfung

Welches der folgenden Prompts entspricht einigen vernünftigen Best Practices?

1. Zeige mir ein Bild eines roten Autos
2. Zeige mir ein Bild eines roten Autos der Marke Volvo und des Modells XC90, geparkt an einer Klippe mit untergehender Sonne
3. Zeige mir ein Bild eines roten Autos der Marke Volvo und des Modells XC90

Antwort: 2, es ist der beste Prompt, da er Details darüber liefert, „was“ gewünscht wird, und ins Detail geht (nicht irgendein Auto, sondern eine bestimmte Marke und Modell) und außerdem die Gesamtszene beschreibt. 3 ist der nächstbeste, weil es ebenfalls viele Details enthält.

## 🚀 Herausforderung

Versuchen Sie, die "Cue"-Technik mit dem Prompt zu verwenden: Vervollständige den Satz „Zeige mir ein Bild eines roten Autos der Marke Volvo und“. Womit antwortet es und wie würden Sie den Prompt verbessern?

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Möchten Sie mehr über verschiedene Konzepte des Prompt-Engineerings erfahren? Gehen Sie auf die [weiterführende Lernseite](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), um weitere großartige Ressourcen zu diesem Thema zu finden.

Gehen Sie zu Lektion 5, wo wir uns [fortgeschrittene Prompting-Techniken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) ansehen werden!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->