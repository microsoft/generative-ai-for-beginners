<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T11:46:15+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "de"
}
-->
# Grundlagen des Prompt-Engineering

## Einführung
Dieses Modul behandelt wesentliche Konzepte und Techniken zur Erstellung effektiver Prompts in generativen KI-Modellen. Die Art und Weise, wie Sie Ihren Prompt an ein LLM schreiben, ist ebenfalls wichtig. Ein sorgfältig gestalteter Prompt kann eine bessere Qualität der Antwort erzielen. Aber was genau bedeuten Begriffe wie _Prompt_ und _Prompt-Engineering_? Und wie kann ich den Prompt _Input_ verbessern, den ich an das LLM sende? Diese Fragen werden wir in diesem Kapitel und im nächsten versuchen zu beantworten.

_Generative KI_ ist in der Lage, neue Inhalte (z. B. Text, Bilder, Audio, Code usw.) als Antwort auf Benutzeranfragen zu erstellen. Dies erreicht sie mithilfe von _Large Language Models_ wie der GPT-Serie ("Generative Pre-trained Transformer") von OpenAI, die auf die Verwendung von natürlicher Sprache und Code trainiert sind.

Benutzer können jetzt mit diesen Modellen über vertraute Paradigmen wie Chat interagieren, ohne technische Expertise oder Schulung zu benötigen. Die Modelle sind _Prompt-basiert_ - Benutzer senden einen Textinput (Prompt) und erhalten die KI-Antwort (Completion). Sie können dann iterativ mit der KI "chatten", in mehrstufigen Gesprächen ihren Prompt verfeinern, bis die Antwort ihren Erwartungen entspricht.

"Prompts" werden nun zur primären _Programmierschnittstelle_ für generative KI-Anwendungen, die den Modellen mitteilen, was zu tun ist und die Qualität der zurückgegebenen Antworten beeinflussen. "Prompt-Engineering" ist ein schnell wachsendes Studienfeld, das sich auf das _Design und die Optimierung_ von Prompts konzentriert, um konsistente und qualitativ hochwertige Antworten im großen Maßstab zu liefern.

## Lernziele

In dieser Lektion lernen wir, was Prompt-Engineering ist, warum es wichtig ist und wie wir effektivere Prompts für ein bestimmtes Modell und Anwendungsziel gestalten können. Wir werden die Kernkonzepte und Best Practices für das Prompt-Engineering verstehen - und erfahren von einer interaktiven Jupyter Notebooks "Sandbox"-Umgebung, in der wir sehen können, wie diese Konzepte auf reale Beispiele angewendet werden.

Am Ende dieser Lektion werden wir in der Lage sein:

1. Erklären, was Prompt-Engineering ist und warum es wichtig ist.
2. Die Komponenten eines Prompts beschreiben und wie sie verwendet werden.
3. Best Practices und Techniken für das Prompt-Engineering lernen.
4. Gelernte Techniken auf reale Beispiele anwenden, mithilfe eines OpenAI-Endpunkts.

## Schlüsselbegriffe

Prompt-Engineering: Die Praxis des Entwerfens und Verfeinerns von Eingaben, um KI-Modelle zu führen und gewünschte Ausgaben zu erzeugen.
Tokenisierung: Der Prozess der Umwandlung von Text in kleinere Einheiten, sogenannte Tokens, die ein Modell verstehen und verarbeiten kann.
Anweisungs-optimierte LLMs: Große Sprachmodelle (LLMs), die mit spezifischen Anweisungen feinabgestimmt wurden, um die Genauigkeit und Relevanz ihrer Antworten zu verbessern.

## Lern-Sandbox

Prompt-Engineering ist derzeit mehr Kunst als Wissenschaft. Der beste Weg, unser Gespür dafür zu verbessern, besteht darin, _mehr zu üben_ und einen Trial-and-Error-Ansatz zu verfolgen, der Fachwissen im Anwendungsbereich mit empfohlenen Techniken und modell-spezifischen Optimierungen kombiniert.

Das Jupyter Notebook, das diese Lektion begleitet, bietet eine _Sandbox_-Umgebung, in der Sie ausprobieren können, was Sie lernen - entweder während des Lernens oder als Teil der Code-Herausforderung am Ende. Um die Übungen auszuführen, benötigen Sie:

1. **Einen Azure OpenAI API-Schlüssel** - den Dienstendpunkt für ein bereitgestelltes LLM.
2. **Eine Python-Laufzeitumgebung** - in der das Notebook ausgeführt werden kann.
3. **Lokale Umgebungsvariablen** - _abschließen Sie jetzt die [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) Schritte, um sich vorzubereiten_.

Das Notebook enthält _Starter_-Übungen - aber Sie werden ermutigt, Ihre eigenen _Markdown_- (Beschreibung) und _Code_- (Prompt-Anfragen) Abschnitte hinzuzufügen, um mehr Beispiele oder Ideen auszuprobieren - und Ihr Gespür für das Prompt-Design zu entwickeln.

## Illustrierter Leitfaden

Möchten Sie das große Ganze dessen, was diese Lektion behandelt, bevor Sie eintauchen? Schauen Sie sich diesen illustrierten Leitfaden an, der Ihnen einen Eindruck von den Hauptthemen und den wichtigsten Erkenntnissen vermittelt, über die Sie in jedem Abschnitt nachdenken sollten. Der Lernplan führt Sie von der Erfassung der Kernkonzepte und Herausforderungen zu deren Lösung mit relevanten Prompt-Engineering-Techniken und Best Practices. Beachten Sie, dass der Abschnitt "Fortgeschrittene Techniken" in diesem Leitfaden auf Inhalte verweist, die im _nächsten_ Kapitel dieses Lehrplans behandelt werden.

## Unser Startup

Nun, lassen Sie uns darüber sprechen, wie _dieses Thema_ mit unserer Startup-Mission zusammenhängt, [KI-Innovation in die Bildung zu bringen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Wir wollen KI-gestützte Anwendungen des _personalisierten Lernens_ entwickeln - also denken wir darüber nach, wie verschiedene Benutzer unserer Anwendung "Prompts" gestalten könnten:

- **Administratoren** könnten die KI bitten, _Curriculum-Daten zu analysieren, um Lücken in der Abdeckung zu identifizieren_. Die KI kann Ergebnisse zusammenfassen oder sie mit Code visualisieren.
- **Lehrer** könnten die KI bitten, _einen Unterrichtsplan für ein Zielpublikum und ein Thema zu erstellen_. Die KI kann den personalisierten Plan in einem angegebenen Format erstellen.
- **Schüler** könnten die KI bitten, _sie in einem schwierigen Fach zu unterrichten_. Die KI kann jetzt Schüler mit Lektionen, Hinweisen und Beispielen unterstützen, die auf ihr Niveau zugeschnitten sind.

Das ist nur die Spitze des Eisbergs. Schauen Sie sich [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) an - eine von Bildungsexperten kuratierte Open-Source-Prompt-Bibliothek - um ein breiteres Gefühl für die Möglichkeiten zu bekommen! _Probieren Sie einige dieser Prompts in der Sandbox oder im OpenAI Playground aus, um zu sehen, was passiert!_

## Was ist Prompt-Engineering?

Wir haben diese Lektion begonnen, indem wir **Prompt-Engineering** als den Prozess des _Entwerfens und Optimierens_ von Texteingaben (Prompts) definiert haben, um konsistente und qualitativ hochwertige Antworten (Completions) für ein gegebenes Anwendungsziel und Modell zu liefern. Wir können dies als einen 2-Schritte-Prozess betrachten:

- _Entwerfen_ des ursprünglichen Prompts für ein gegebenes Modell und Ziel
- _Verfeinern_ des Prompts iterativ, um die Qualität der Antwort zu verbessern

Dies ist notwendigerweise ein Trial-and-Error-Prozess, der Benutzerintuition und Aufwand erfordert, um optimale Ergebnisse zu erzielen. Warum ist es also wichtig? Um diese Frage zu beantworten, müssen wir zunächst drei Konzepte verstehen:

- _Tokenisierung_ = wie das Modell den Prompt "sieht"
- _Base LLMs_ = wie das Basis-Modell einen Prompt "verarbeitet"
- _Anweisungs-optimierte LLMs_ = wie das Modell jetzt "Aufgaben" sehen kann

### Tokenisierung

Ein LLM sieht Prompts als eine _Sequenz von Tokens_, wobei verschiedene Modelle (oder Versionen eines Modells) denselben Prompt auf unterschiedliche Weise tokenisieren können. Da LLMs auf Tokens (und nicht auf Rohtext) trainiert werden, hat die Art und Weise, wie Prompts tokenisiert werden, direkten Einfluss auf die Qualität der generierten Antwort.

Um ein Gespür dafür zu bekommen, wie die Tokenisierung funktioniert, probieren Sie Tools wie den [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) aus, der unten gezeigt wird. Kopieren Sie Ihren Prompt hinein - und sehen Sie, wie dieser in Tokens umgewandelt wird, wobei Sie darauf achten, wie Leerzeichen und Satzzeichen behandelt werden. Beachten Sie, dass dieses Beispiel ein älteres LLM (GPT-3) zeigt - wenn Sie dies mit einem neueren Modell ausprobieren, kann es zu einem anderen Ergebnis kommen.

### Konzept: Foundation Models

Sobald ein Prompt tokenisiert ist, besteht die Hauptfunktion des ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (oder Foundation-Modells) darin, das nächste Token in dieser Sequenz vorherzusagen. Da LLMs auf massiven Textdatensätzen trainiert sind, haben sie ein gutes Verständnis für die statistischen Beziehungen zwischen Tokens und können diese Vorhersage mit einiger Zuversicht treffen. Beachten Sie, dass sie die _Bedeutung_ der Wörter im Prompt oder Token nicht verstehen; sie sehen nur ein Muster, das sie mit ihrer nächsten Vorhersage "vervollständigen" können. Sie können die Vorhersage der Sequenz fortsetzen, bis sie durch Benutzereingriff oder eine vorab festgelegte Bedingung beendet wird.

Möchten Sie sehen, wie die Prompt-basierte Vervollständigung funktioniert? Geben Sie den obigen Prompt in das Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) mit den Standardeinstellungen ein. Das System ist so konfiguriert, dass Prompts als Informationsanfragen behandelt werden - Sie sollten also eine Vervollständigung sehen, die diesen Kontext erfüllt.

Aber was, wenn der Benutzer etwas Spezifisches sehen wollte, das einige Kriterien oder ein Aufgabenziel erfüllt? Hier kommen _anweisungs-optimierte_ LLMs ins Spiel.

### Konzept: Anweisungs-optimierte LLMs

Ein [anweisungs-optimiertes LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) beginnt mit dem Foundation-Modell und verfeinert es mit Beispielen oder Eingabe-/Ausgabe-Paaren (z. B. mehrstufigen "Nachrichten"), die klare Anweisungen enthalten können - und die Antwort der KI versucht, diese Anweisung zu befolgen.

Dies verwendet Techniken wie Reinforcement Learning mit menschlichem Feedback (RLHF), die das Modell darauf trainieren können, _Anweisungen zu befolgen_ und _aus Feedback zu lernen_, sodass es Antworten produziert, die besser für praktische Anwendungen geeignet und relevanter für Benutzerziele sind.

Lassen Sie uns das ausprobieren - gehen Sie zurück zum obigen Prompt, aber ändern Sie jetzt die _Systemnachricht_, um die folgende Anweisung als Kontext bereitzustellen:

> _Fassen Sie den Inhalt, den Sie erhalten, für einen Zweitklässler zusammen. Halten Sie das Ergebnis in einem Absatz mit 3-5 Aufzählungspunkten._

Sehen Sie, wie das Ergebnis jetzt auf das gewünschte Ziel und Format abgestimmt ist? Ein Lehrer kann diese Antwort jetzt direkt in seinen Folien für diese Klasse verwenden.

## Warum brauchen wir Prompt-Engineering?

Jetzt, da wir wissen, wie Prompts von LLMs verarbeitet werden, sprechen wir darüber, _warum_ wir Prompt-Engineering benötigen. Die Antwort liegt darin, dass aktuelle LLMs eine Reihe von Herausforderungen darstellen, die es schwieriger machen, _zuverlässige und konsistente Vervollständigungen_ zu erreichen, ohne Aufwand in die Prompt-Konstruktion und Optimierung zu investieren. Beispielsweise:

1. **Modellantworten sind stochastisch.** Der _gleiche Prompt_ wird wahrscheinlich unterschiedliche Antworten mit verschiedenen Modellen oder Modellversionen erzeugen. Und es kann sogar unterschiedliche Ergebnisse mit dem _gleichen Modell_ zu verschiedenen Zeiten erzeugen. _Prompt-Engineering-Techniken können uns helfen, diese Variationen zu minimieren, indem sie bessere Leitplanken bereitstellen_.

2. **Modelle können Antworten erfinden.** Modelle sind mit _großen, aber endlichen_ Datensätzen vortrainiert, was bedeutet, dass ihnen Wissen über Konzepte außerhalb dieses Trainingsumfangs fehlt. Infolgedessen können sie Vervollständigungen erzeugen, die ungenau, imaginär oder direkt widersprüchlich zu bekannten Fakten sind. _Prompt-Engineering-Techniken helfen Benutzern, solche Erfindungen zu identifizieren und zu mindern, z. B. indem sie die KI um Zitate oder Argumentationen bitten_.

3. **Modelleigenschaften variieren.** Neuere Modelle oder Modellgenerationen werden reichere Fähigkeiten haben, bringen aber auch einzigartige Eigenheiten und Kompromisse in Bezug auf Kosten und Komplexität mit sich. _Prompt-Engineering kann uns helfen, Best Practices und Workflows zu entwickeln, die Unterschiede abstrahieren und sich auf modell-spezifische Anforderungen in skalierbaren, nahtlosen Wegen anpassen_.

Lassen Sie uns dies im OpenAI oder Azure OpenAI Playground in Aktion sehen:

- Verwenden Sie denselben Prompt mit verschiedenen LLM-Bereitstellungen (z. B. OpenAI, Azure OpenAI, Hugging Face) - haben Sie die Variationen gesehen?
- Verwenden Sie denselben Prompt wiederholt mit der _gleichen_ LLM-Bereitstellung (z. B. Azure OpenAI Playground) - wie unterschieden sich diese Variationen?

### Beispiel für Erfindungen

In diesem Kurs verwenden wir den Begriff **"Erfindung"** für das Phänomen, bei dem LLMs manchmal faktisch falsche Informationen aufgrund von Einschränkungen in ihrem Training oder anderen Beschränkungen generieren. Möglicherweise haben Sie dies auch als _"Halluzinationen"_ in populären Artikeln oder Forschungspapieren gehört. Wir empfehlen jedoch dringend, den Begriff _"Erfindung"_ zu verwenden, damit wir das Verhalten nicht versehentlich anthropomorphisieren, indem wir eine menschliche Eigenschaft einem maschinengesteuerten Ergebnis zuschreiben. Dies verstärkt auch [Richtlinien für verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aus einer terminologischen Perspektive, indem Begriffe entfernt werden, die in einigen Kontexten als beleidigend oder nicht inklusiv angesehen werden können.

Möchten Sie ein Gefühl dafür bekommen, wie Erfindungen funktionieren? Denken Sie an einen Prompt, der die KI anweist, Inhalte für ein nicht existierendes Thema zu erstellen (um sicherzustellen, dass es nicht im Trainingsdatensatz enthalten ist). Beispielsweise habe ich diesen Prompt ausprobiert:

> **Prompt:** Erstellen Sie einen Unterrichtsplan über den Mars-Krieg von 2076.

Eine Websuche zeigte mir, dass es fiktive Berichte (z. B. Fernsehserien oder Bücher) über Mars-Kriege gab - aber keinen im Jahr 2076. Der gesunde Menschenverstand sagt uns auch, dass 2076 _in der Zukunft_ liegt und daher nicht mit einem echten Ereignis in Verbindung gebracht werden kann.

Was passiert also, wenn wir diesen Prompt mit verschiedenen LLM-Anbietern ausführen?

> **Antwort 1**: OpenAI Playground (GPT-35)

> **Antwort 2**: Azure OpenAI Playground (GPT-35)

> **Antwort 3**: Hugging Face Chat Playground (LLama-2)

Wie erwartet erzeugt jedes Modell (oder jede Modellversion) leicht unterschiedliche Antworten dank stochastischem Verhalten und Modellfähigkeitsvariationen. Beispielsweise zielt ein Modell auf ein 8. Klasse Publikum, während das andere einen Gymnasiasten annimmt. Aber alle drei Modelle erzeugten Antworten, die einen uninformierten Benutzer davon überzeugen könnten, dass das Ereignis real war.

Prompt-Engineering-Techniken wie _Metaprompting_ und _Temperaturkonfiguration_ können Modell-Erfindungen bis zu einem gewissen Grad reduzieren. Neue Prompt-Engineering-_Architekturen_ integrieren auch nahtlos neue Werkzeuge und Techniken in den Prompt-Fluss, um einige dieser Effekte zu mindern oder zu reduzieren.

## Fallstudie: GitHub Copilot

Lassen Sie uns diesen Abschnitt abschließen, indem wir ein Gefühl dafür bekommen, wie Prompt-Engineering in realen Lösungen eingesetzt wird, indem wir eine Fallstudie betrachten: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ist Ihr "AI Pair Programmer" - es wandelt Text-Prompts in Code-Vervollständigungen um und ist in Ihre Entwicklungsumgebung (z. B. Visual Studio Code) integriert, um ein nahtloses Benutzererlebnis zu bieten. Wie in der unten stehenden Blog-Serie dokumentiert, basierte die früheste Version auf dem OpenAI Codex-Modell - mit Ingenieuren, die schnell die Notwendigkeit erkannten, das Modell zu verfeinern und bessere Prompt-Engineering-Techniken zu entwickeln, um die Codequalität zu verbessern. Im Juli [debütierten sie ein verbessertes KI-Modell, das über Codex hinausgeht](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) für noch schnellere Vorschläge.

Lesen Sie die Beiträge in der Reihenfolge, um ihrer Lernreise zu folgen.

- **Mai 2023** | [GitHub Copilot wird besser im Verständnis Ihres Codes](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub: Arbeiten mit den LLMs hinter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Wie man bessere Prompts für GitHub Copilot schreibt](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot geht über Codex hinaus mit verbessertem KI-Modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** |
Schließlich liegt der wahre Wert von Vorlagen in der Fähigkeit, _Prompt-Bibliotheken_ für vertikale Anwendungsbereiche zu erstellen und zu veröffentlichen - wobei die Prompt-Vorlage jetzt _optimiert_ ist, um anwendungsspezifischen Kontext oder Beispiele widerzuspiegeln, die die Antworten für die Zielbenutzer relevanter und genauer machen. Das [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) Repository ist ein großartiges Beispiel für diesen Ansatz, da es eine Bibliothek von Prompts für den Bildungsbereich kuratiert, mit Schwerpunkt auf Schlüsselzielen wie Unterrichtsplanung, Lehrplangestaltung, Schülerbetreuung usw.

## Unterstützende Inhalte

Wenn wir über die Konstruktion von Prompts nachdenken, die eine Anweisung (Aufgabe) und ein Ziel (Hauptinhalt) haben, dann ist _sekundärer Inhalt_ wie zusätzlicher Kontext, den wir bereitstellen, um **die Ausgabe in irgendeiner Weise zu beeinflussen**. Es könnten Parameteranpassungen, Formatierungsanweisungen, Themenklassifikationen usw. sein, die dem Modell helfen, seine Antwort _anzupassen_, um den gewünschten Benutzerzielen oder Erwartungen zu entsprechen.

Zum Beispiel: Angenommen, wir haben einen Kurskatalog mit umfangreichen Metadaten (Name, Beschreibung, Niveau, Metadaten-Tags, Dozent usw.) zu allen verfügbaren Kursen im Lehrplan:

- wir können eine Anweisung definieren, um "den Kurskatalog für Herbst 2023 zusammenzufassen"
- wir können den Hauptinhalt verwenden, um einige Beispiele für die gewünschte Ausgabe bereitzustellen
- wir können den sekundären Inhalt verwenden, um die Top 5 "Tags" von Interesse zu identifizieren.

Jetzt kann das Modell eine Zusammenfassung im Format der gezeigten Beispiele liefern - aber wenn ein Ergebnis mehrere Tags hat, kann es die 5 im sekundären Inhalt identifizierten Tags priorisieren.

---

## Best Practices für Prompts

Jetzt, da wir wissen, wie Prompts _konstruiert_ werden können, können wir darüber nachdenken, wie man sie _gestaltet_, um Best Practices widerzuspiegeln. Wir können dies in zwei Teile unterteilen - die richtige _Einstellung_ haben und die richtigen _Techniken_ anwenden.

### Einstellung für Prompt Engineering

Prompt Engineering ist ein Trial-and-Error-Prozess, daher sollten Sie drei breite Leitfaktoren im Hinterkopf behalten:

1. **Verständnis der Domäne ist wichtig.** Die Genauigkeit und Relevanz der Antwort ist eine Funktion der _Domäne_, in der die Anwendung oder der Benutzer operiert. Verwenden Sie Ihre Intuition und Fachkenntnisse, um **Techniken anzupassen**. Definieren Sie zum Beispiel _domänenspezifische Persönlichkeiten_ in Ihren System-Prompts oder verwenden Sie _domänenspezifische Vorlagen_ in Ihren Benutzer-Prompts. Stellen Sie sekundäre Inhalte bereit, die domänenspezifische Kontexte widerspiegeln, oder verwenden Sie _domänenspezifische Hinweise und Beispiele_, um das Modell in Richtung vertrauter Nutzungsmuster zu lenken.

2. **Verständnis des Modells ist wichtig.** Wir wissen, dass Modelle von Natur aus stochastisch sind. Aber Modellimplementierungen können auch in Bezug auf den Trainingsdatensatz, den sie verwenden (vorgefertigtes Wissen), die Fähigkeiten, die sie bieten (z. B. über API oder SDK) und die Art des Inhalts, für den sie optimiert sind (z. B. Code vs. Bilder vs. Text), variieren. Verstehen Sie die Stärken und Einschränkungen des Modells, das Sie verwenden, und nutzen Sie dieses Wissen, um _Aufgaben zu priorisieren_ oder _angepasste Vorlagen_ zu erstellen, die für die Fähigkeiten des Modells optimiert sind.

3. **Iteration & Validierung sind wichtig.** Modelle entwickeln sich schnell weiter, ebenso wie die Techniken für Prompt Engineering. Als Fachexperte können Sie über andere Kontexte oder Kriterien für _Ihre_ spezifische Anwendung verfügen, die möglicherweise nicht für die breitere Gemeinschaft gelten. Verwenden Sie Prompt-Engineering-Tools und -Techniken, um den Prompt-Konstruktionsprozess zu "beschleunigen", und iterieren und validieren Sie die Ergebnisse mit Ihrer eigenen Intuition und Fachkenntnis. Zeichnen Sie Ihre Erkenntnisse auf und erstellen Sie eine **Wissensdatenbank** (z. B. Prompt-Bibliotheken), die als neue Basislinie für schnellere Iterationen in der Zukunft verwendet werden kann.

## Best Practices

Schauen wir uns nun einige gängige Best Practices an, die von [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) und [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) Praktikern empfohlen werden.

| Was                               | Warum                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluieren Sie die neuesten Modelle.       | Neue Modellgenerationen haben wahrscheinlich verbesserte Funktionen und Qualität - können aber auch höhere Kosten verursachen. Bewerten Sie sie hinsichtlich ihrer Auswirkungen und treffen Sie dann Migrationsentscheidungen.                                                                                |
| Trennen Sie Anweisungen und Kontext.   | Überprüfen Sie, ob Ihr Modell/Anbieter _Trennzeichen_ definiert, um Anweisungen, primäre und sekundäre Inhalte klarer zu unterscheiden. Dies kann Modellen helfen, Gewichte genauer auf Tokens zuzuweisen.                                                         |
| Seien Sie spezifisch und klar.             | Geben Sie mehr Details zum gewünschten Kontext, Ergebnis, Länge, Format, Stil usw. Dies verbessert sowohl die Qualität als auch die Konsistenz der Antworten. Erfassen Sie Rezepte in wiederverwendbaren Vorlagen.                                                          |
| Seien Sie beschreibend, verwenden Sie Beispiele.      | Modelle reagieren möglicherweise besser auf einen "zeigen und erzählen" Ansatz. Beginnen Sie mit einem `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` Werte. Kehren Sie zum [Lern-Sandbox-Abschnitt](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) zurück, um zu lernen, wie.

### Öffnen Sie als Nächstes das Jupyter Notebook

- Wählen Sie den Runtime-Kernel aus. Wenn Sie Option 1 oder 2 verwenden, wählen Sie einfach den Standard-Python 3.10.x-Kernel aus, der vom Entwicklungscontainer bereitgestellt wird.

Sie sind bereit, die Übungen durchzuführen. Beachten Sie, dass es hier keine _richtigen oder falschen_ Antworten gibt - es geht nur darum, Optionen durch Trial-and-Error zu erkunden und ein Gefühl dafür zu entwickeln, was für ein gegebenes Modell und Anwendungsgebiet funktioniert.

_Aus diesem Grund gibt es in dieser Lektion keine Code-Lösungssegmente. Stattdessen enthält das Notebook Markdown-Zellen mit dem Titel "Meine Lösung:", die ein Beispielergebnis als Referenz zeigen._

## Wissenscheck

Welche der folgenden ist ein guter Prompt, der einigen vernünftigen Best Practices folgt?

1. Zeige mir ein Bild eines roten Autos
2. Zeige mir ein Bild eines roten Autos der Marke Volvo und Modell XC90, das an einer Klippe geparkt ist, während die Sonne untergeht
3. Zeige mir ein Bild eines roten Autos der Marke Volvo und Modell XC90

A: 2, es ist der beste Prompt, da er Details zu "was" liefert und ins Detail geht (nicht nur irgendein Auto, sondern eine bestimmte Marke und ein Modell) und auch die Gesamtsituation beschreibt. 3 ist der nächstbeste, da es ebenfalls viele Beschreibungen enthält.

## 🚀 Herausforderung

Versuchen Sie, die "Hinweis"-Technik mit dem Prompt zu nutzen: Vervollständigen Sie den Satz "Zeige mir ein Bild eines roten Autos der Marke Volvo und ". Was antwortet es, und wie würden Sie es verbessern?

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Möchten Sie mehr über verschiedene Konzepte des Prompt Engineering erfahren? Gehen Sie zur [Seite für fortgesetztes Lernen](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), um weitere großartige Ressourcen zu diesem Thema zu finden.

Gehen Sie zu Lektion 5, in der wir uns [fortgeschrittene Prompting-Techniken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) ansehen!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.