<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:52:03+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "de"
}
-->
# Grundlagen der Prompt-Entwicklung

## Einführung
Dieses Modul behandelt wesentliche Konzepte und Techniken zur Erstellung effektiver Prompts in generativen KI-Modellen. Auch die Art und Weise, wie Sie Ihren Prompt an ein LLM schreiben, ist wichtig. Ein sorgfältig gestalteter Prompt kann eine bessere Qualität der Antwort erzielen. Aber was genau bedeuten Begriffe wie _Prompt_ und _Prompt Engineering_? Und wie verbessere ich den Prompt _Input_, den ich an das LLM sende? Dies sind die Fragen, die wir in diesem Kapitel und dem nächsten zu beantworten versuchen.

_Generative KI_ ist in der Lage, neue Inhalte (z.B. Text, Bilder, Audio, Code etc.) als Antwort auf Benutzeranfragen zu erstellen. Dies erreicht sie durch _Large Language Models_ wie die GPT-Serie ("Generative Pre-trained Transformer") von OpenAI, die für die Nutzung von natürlicher Sprache und Code trainiert sind.

Benutzer können jetzt mit diesen Modellen über vertraute Paradigmen wie Chat interagieren, ohne technische Kenntnisse oder Schulungen zu benötigen. Die Modelle sind _prompt-basiert_ - Benutzer senden einen Texteingabe (Prompt) und erhalten die KI-Antwort (Vervollständigung) zurück. Sie können dann iterativ "mit der KI chatten" und ihre Prompts verfeinern, bis die Antwort ihren Erwartungen entspricht.

"Prompts" werden nun zur primären _Programmierschnittstelle_ für generative KI-Anwendungen, die den Modellen sagen, was zu tun ist, und die Qualität der zurückgegebenen Antworten beeinflussen. "Prompt Engineering" ist ein schnell wachsendes Forschungsfeld, das sich auf das _Design und die Optimierung_ von Prompts konzentriert, um konsistente und qualitativ hochwertige Antworten in großem Maßstab zu liefern.

## Lernziele

In dieser Lektion lernen wir, was Prompt Engineering ist, warum es wichtig ist und wie wir effektivere Prompts für ein gegebenes Modell und Anwendungsziel erstellen können. Wir verstehen grundlegende Konzepte und Best Practices für Prompt Engineering - und lernen eine interaktive Jupyter Notebooks "Sandbox"-Umgebung kennen, in der wir diese Konzepte an realen Beispielen anwenden können.

Am Ende dieser Lektion werden wir in der Lage sein:

1. Zu erklären, was Prompt Engineering ist und warum es wichtig ist.
2. Die Komponenten eines Prompts zu beschreiben und wie sie verwendet werden.
3. Best Practices und Techniken für Prompt Engineering zu erlernen.
4. Gelernte Techniken an realen Beispielen anzuwenden, unter Verwendung eines OpenAI-Endpunkts.

## Schlüsselbegriffe

Prompt Engineering: Die Praxis des Entwerfens und Verfeinerns von Eingaben, um KI-Modelle dazu zu führen, gewünschte Ausgaben zu erzeugen.
Tokenisierung: Der Prozess der Umwandlung von Text in kleinere Einheiten, sogenannte Tokens, die ein Modell verstehen und verarbeiten kann.
Instruction-Tuned LLMs: Große Sprachmodelle (LLMs), die mit spezifischen Anweisungen feinabgestimmt wurden, um ihre Antwortgenauigkeit und Relevanz zu verbessern.

## Lern-Sandbox

Prompt Engineering ist derzeit mehr Kunst als Wissenschaft. Der beste Weg, unser Gespür dafür zu verbessern, ist _mehr zu üben_ und einen Trial-and-Error-Ansatz zu verfolgen, der Fachwissen aus dem Anwendungsbereich mit empfohlenen Techniken und modellspezifischen Optimierungen kombiniert.

Das Jupyter Notebook, das diese Lektion begleitet, bietet eine _Sandbox_-Umgebung, in der Sie ausprobieren können, was Sie lernen - entweder während der Lektion oder als Teil der Code-Herausforderung am Ende. Um die Übungen auszuführen, benötigen Sie:

1. **Einen Azure OpenAI API-Schlüssel** - den Dienstendpunkt für ein bereitgestelltes LLM.
2. **Eine Python-Laufzeitumgebung** - in der das Notebook ausgeführt werden kann.
3. **Lokale Umgebungsvariablen** - _schließen Sie jetzt die [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) Schritte ab, um bereit zu sein_.

Das Notebook enthält _Starter_-Übungen - aber Sie werden ermutigt, Ihre eigenen _Markdown_- (Beschreibung) und _Code_- (Prompt-Anfragen) Abschnitte hinzuzufügen, um mehr Beispiele oder Ideen auszuprobieren - und Ihr Gespür für das Prompt-Design zu entwickeln.

## Illustrierte Anleitung

Möchten Sie das große Ganze dessen, was diese Lektion abdeckt, sehen, bevor Sie eintauchen? Schauen Sie sich diese illustrierte Anleitung an, die Ihnen einen Eindruck von den Hauptthemen vermittelt und die wichtigsten Erkenntnisse, über die Sie nachdenken sollten. Der Lektionfahrplan führt Sie von der Verständnis der grundlegenden Konzepte und Herausforderungen zur Bewältigung dieser mit relevanten Prompt-Engineering-Techniken und Best Practices. Beachten Sie, dass sich der Abschnitt "Erweiterte Techniken" in dieser Anleitung auf Inhalte bezieht, die im _nächsten_ Kapitel dieses Lehrplans behandelt werden.

## Unser Startup

Nun, lassen Sie uns darüber sprechen, wie _dieses Thema_ mit unserer Startup-Mission zusammenhängt, [KI-Innovationen in die Bildung zu bringen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Wir wollen KI-gestützte Anwendungen für _personalisiertes Lernen_ entwickeln - also denken wir darüber nach, wie verschiedene Benutzer unserer Anwendung "Prompts entwerfen" könnten:

- **Administratoren** könnten die KI bitten, _Lehrplandaten zu analysieren, um Lücken in der Abdeckung zu identifizieren_. Die KI kann Ergebnisse zusammenfassen oder sie mit Code visualisieren.
- **Lehrer** könnten die KI bitten, _einen Unterrichtsplan für eine Zielgruppe und ein Thema zu erstellen_. Die KI kann den personalisierten Plan in einem bestimmten Format erstellen.
- **Schüler** könnten die KI bitten, _sie in einem schwierigen Fach zu unterrichten_. Die KI kann jetzt Schüler mit Lektionen, Hinweisen & Beispielen unterstützen, die auf ihrem Niveau zugeschnitten sind.

Das ist nur die Spitze des Eisbergs. Schauen Sie sich [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) an - eine Open-Source-Prompt-Bibliothek, die von Bildungsexperten kuratiert wurde - um ein breiteres Gefühl für die Möglichkeiten zu bekommen! _Versuchen Sie, einige dieser Prompts in der Sandbox auszuführen oder den OpenAI Playground zu verwenden, um zu sehen, was passiert!_

## Was ist Prompt Engineering?

Wir haben diese Lektion begonnen, indem wir **Prompt Engineering** als den Prozess des _Entwerfens und Optimierens_ von Texteingaben (Prompts) definiert haben, um konsistente und qualitativ hochwertige Antworten (Vervollständigungen) für ein gegebenes Anwendungsziel und Modell zu liefern. Wir können dies als einen zweistufigen Prozess betrachten:

- _Entwerfen_ des ursprünglichen Prompts für ein gegebenes Modell und Ziel
- _Verfeinern_ des Prompts iterativ, um die Qualität der Antwort zu verbessern

Dies ist notwendigerweise ein Trial-and-Error-Prozess, der Benutzerintelligenz und Aufwand erfordert, um optimale Ergebnisse zu erzielen. Warum ist das wichtig? Um diese Frage zu beantworten, müssen wir zunächst drei Konzepte verstehen:

- _Tokenisierung_ = wie das Modell den Prompt "sieht"
- _Basis-LLMs_ = wie das Grundmodell einen Prompt "verarbeitet"
- _Instruction-Tuned LLMs_ = wie das Modell jetzt "Aufgaben" sehen kann

### Tokenisierung

Ein LLM sieht Prompts als eine _Sequenz von Tokens_, bei der verschiedene Modelle (oder Versionen eines Modells) denselben Prompt auf unterschiedliche Weise tokenisieren können. Da LLMs auf Tokens trainiert werden (und nicht auf Rohtext), hat die Art und Weise, wie Prompts tokenisiert werden, einen direkten Einfluss auf die Qualität der generierten Antwort.

Um ein Gespür dafür zu bekommen, wie Tokenisierung funktioniert, probieren Sie Tools wie den [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) aus, der unten gezeigt wird. Kopieren Sie Ihren Prompt hinein - und sehen Sie, wie dieser in Tokens umgewandelt wird, wobei Sie darauf achten, wie Leerzeichen und Satzzeichen behandelt werden. Beachten Sie, dass dieses Beispiel ein älteres LLM (GPT-3) zeigt - das Ausprobieren mit einem neueren Modell kann ein anderes Ergebnis liefern.

### Konzept: Basis-Modelle

Sobald ein Prompt tokenisiert ist, besteht die Hauptfunktion des ["Basis-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (oder Grundmodell) darin, das Token in dieser Sequenz vorherzusagen. Da LLMs auf riesigen Textdatensätzen trainiert sind, haben sie ein gutes Gespür für die statistischen Beziehungen zwischen Tokens und können diese Vorhersage mit einiger Zuversicht treffen. Beachten Sie, dass sie nicht die _Bedeutung_ der Wörter im Prompt oder Token verstehen; sie sehen nur ein Muster, das sie mit ihrer nächsten Vorhersage "vervollständigen" können. Sie können die Sequenz weiter vorhersagen, bis sie durch Benutzereingriff oder eine vorab festgelegte Bedingung beendet wird.

Möchten Sie sehen, wie promptbasierte Vervollständigung funktioniert? Geben Sie den obigen Prompt in das Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) mit den Standardeinstellungen ein. Das System ist so konfiguriert, dass es Prompts als Informationsanfragen behandelt - Sie sollten also eine Vervollständigung sehen, die diesen Kontext erfüllt.

Aber was ist, wenn der Benutzer etwas Spezifisches sehen möchte, das einige Kriterien oder Aufgaben erfüllt? Hier kommen _instruction-tuned_ LLMs ins Spiel.

### Konzept: Instruction Tuned LLMs

Ein [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) beginnt mit dem Grundmodell und wird mit Beispielen oder Eingabe-/Ausgabepaaren (z.B. mehrstufige "Nachrichten") feinabgestimmt, die klare Anweisungen enthalten können - und die Antwort der KI versucht, dieser Anweisung zu folgen.

Dies verwendet Techniken wie Reinforcement Learning mit menschlichem Feedback (RLHF), die das Modell trainieren können, _Anweisungen zu folgen_ und _aus Feedback zu lernen_, sodass es Antworten liefert, die besser für praktische Anwendungen geeignet und relevanter für Benutzerziele sind.

Probieren wir es aus - rufen Sie den obigen Prompt erneut auf, aber ändern Sie jetzt die _Systemnachricht_, um die folgende Anweisung als Kontext bereitzustellen:

> _Fassen Sie den Inhalt, den Sie erhalten, für einen Zweitklässler zusammen. Halten Sie das Ergebnis in einem Absatz mit 3-5 Aufzählungspunkten._

Sehen Sie, wie das Ergebnis jetzt auf das gewünschte Ziel und Format abgestimmt ist? Ein Lehrer kann diese Antwort jetzt direkt in seinen Folien für diese Klasse verwenden.

## Warum brauchen wir Prompt Engineering?

Da wir nun wissen, wie Prompts von LLMs verarbeitet werden, sprechen wir darüber, _warum_ wir Prompt Engineering benötigen. Die Antwort liegt darin, dass aktuelle LLMs eine Reihe von Herausforderungen darstellen, die es schwieriger machen, _zuverlässige und konsistente Vervollständigungen_ zu erreichen, ohne Aufwand in die Erstellung und Optimierung von Prompts zu stecken. Zum Beispiel:

1. **Modellantworten sind stochastisch.** Der _gleiche Prompt_ wird wahrscheinlich unterschiedliche Antworten mit verschiedenen Modellen oder Modellversionen erzeugen. Und er kann sogar unterschiedliche Ergebnisse mit demselben Modell zu unterschiedlichen Zeiten erzeugen. _Prompt Engineering-Techniken können uns helfen, diese Variationen zu minimieren, indem sie bessere Leitplanken bieten_.

1. **Modelle können Antworten erfinden.** Modelle sind mit _großen, aber endlichen_ Datensätzen vortrainiert, was bedeutet, dass sie kein Wissen über Konzepte außerhalb dieses Trainingsumfangs haben. Infolgedessen können sie Vervollständigungen erzeugen, die ungenau, erfunden oder direkt im Widerspruch zu bekannten Fakten stehen. _Prompt Engineering-Techniken helfen Benutzern, solche Erfindungen zu identifizieren und zu mindern, z.B. indem sie die KI um Zitate oder Begründungen bitten_.

1. **Modellfähigkeiten variieren.** Neuere Modelle oder Modellgenerationen haben reichere Fähigkeiten, bringen aber auch einzigartige Eigenheiten und Kompromisse in Bezug auf Kosten und Komplexität mit sich. _Prompt Engineering kann uns helfen, Best Practices und Workflows zu entwickeln, die Unterschiede abstrahieren und sich nahtlos an modellspezifische Anforderungen anpassen_.

Lassen Sie uns dies in Aktion im OpenAI oder Azure OpenAI Playground sehen:

- Verwenden Sie denselben Prompt mit verschiedenen LLM-Bereitstellungen (z.B. OpenAI, Azure OpenAI, Hugging Face) - haben Sie die Variationen gesehen?
- Verwenden Sie denselben Prompt wiederholt mit derselben LLM-Bereitstellung (z.B. Azure OpenAI Playground) - wie unterschieden sich diese Variationen?

### Beispiel für Erfindungen

In diesem Kurs verwenden wir den Begriff **"Erfindung"**, um das Phänomen zu beschreiben, bei dem LLMs manchmal faktisch falsche Informationen aufgrund von Einschränkungen in ihrem Training oder anderen Beschränkungen generieren. Möglicherweise haben Sie dies auch als _"Halluzinationen"_ in populären Artikeln oder Forschungspapieren gehört. Wir empfehlen jedoch dringend, den Begriff _"Erfindung"_ zu verwenden, um das Verhalten nicht versehentlich zu vermenschlichen, indem wir eine menschliche Eigenschaft einem maschinengesteuerten Ergebnis zuschreiben. Dies verstärkt auch die [Richtlinien für verantwortungsvolle KI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) aus einer terminologischen Perspektive, indem Begriffe entfernt werden, die in einigen Kontexten als anstößig oder nicht inklusiv angesehen werden könnten.

Möchten Sie ein Gefühl dafür bekommen, wie Erfindungen funktionieren? Denken Sie an einen Prompt, der die KI anweist, Inhalte für ein nicht existierendes Thema zu generieren (um sicherzustellen, dass es nicht im Trainingsdatensatz zu finden ist). Zum Beispiel habe ich diesen Prompt ausprobiert:

> **Prompt:** Erstellen Sie einen Unterrichtsplan über den Marskrieg von 2076.

Eine Websuche zeigte mir, dass es fiktionale Berichte (z.B. Fernsehserien oder Bücher) über Marskriege gab - aber keinen im Jahr 2076. Der gesunde Menschenverstand sagt uns auch, dass 2076 _in der Zukunft_ liegt und daher nicht mit einem realen Ereignis in Verbindung gebracht werden kann.

Was passiert also, wenn wir diesen Prompt mit verschiedenen LLM-Anbietern ausführen?

> **Antwort 1**: OpenAI Playground (GPT-35)

> **Antwort 2**: Azure OpenAI Playground (GPT-35)

> **Antwort 3**: : Hugging Face Chat Playground (LLama-2)

Wie erwartet, erzeugt jedes Modell (oder Modellversion) aufgrund des stochastischen Verhaltens und der Variationen der Modellfähigkeiten leicht unterschiedliche Antworten. Zum Beispiel richtet sich ein Modell an ein Publikum der 8. Klasse, während das andere von einem Schüler der High School ausgeht. Aber alle drei Modelle erzeugten Antworten, die einen uninformierten Benutzer davon überzeugen könnten, dass das Ereignis real war.

Prompt Engineering-Techniken wie _Metaprompting_ und _Temperaturkonfiguration_ können Modell-Erfindungen bis zu einem gewissen Grad reduzieren. Neue Prompt Engineering-_Architekturen_ integrieren auch nahtlos neue Tools und Techniken in den Prompt-Flow, um einige dieser Effekte zu mindern oder zu reduzieren.

## Fallstudie: GitHub Copilot

Lassen Sie uns diesen Abschnitt abschließen, indem wir ein Gefühl dafür bekommen, wie Prompt Engineering in realen Lösungen verwendet wird, indem wir eine Fallstudie betrachten: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot ist Ihr "KI-Paar-Programmierer" - es wandelt Text-Prompts in Code-Vervollständigungen um und ist in Ihre Entwicklungsumgebung (z.B. Visual Studio Code) für ein nahtloses Benutzererlebnis integriert. Wie in der unten stehenden Blog-Serie dokumentiert, basierte die früheste Version auf dem OpenAI Codex-Modell - wobei Ingenieure schnell die Notwendigkeit erkannten, das Modell zu verfeinern und bessere Prompt Engineering-Techniken zu entwickeln, um die Codequalität zu verbessern. Im Juli [debütierten sie ein verbessertes KI-Modell, das über Codex hinausgeht](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) für noch schnellere Vorschläge.

Lesen Sie die Beiträge der Reihe nach, um ihre Lernreise zu verfolgen.

- **Mai 2023** | [GitHub Copilot wird besser darin, Ihren Code zu verstehen](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inside GitHub: Arbeiten mit den LLMs hinter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Wie man bessere Prompts für GitHub Copilot schreibt](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot geht über Codex hinaus mit verbessertem KI-Modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [Ein Entwicklerleitfaden für Prompt Engineering und LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms
Schließlich liegt der wahre Wert von Vorlagen in der Fähigkeit, _Prompt-Bibliotheken_ für vertikale Anwendungsdomänen zu erstellen und zu veröffentlichen - wo die Prompt-Vorlage nun _optimiert_ wird, um anwendungsspezifischen Kontext oder Beispiele widerzuspiegeln, die die Antworten für die Zielnutzergruppe relevanter und genauer machen. Das [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) Repository ist ein großartiges Beispiel für diesen Ansatz und kuratiert eine Bibliothek von Prompts für den Bildungsbereich mit Schwerpunkt auf Schlüsselzielen wie Unterrichtsplanung, Lehrplangestaltung, Schülerbetreuung usw.

## Unterstützende Inhalte

Wenn wir die Erstellung von Prompts als Anweisung (Aufgabe) und Ziel (Hauptinhalt) betrachten, dann ist _sekundärer Inhalt_ wie zusätzlicher Kontext, den wir bereitstellen, um **die Ausgabe in gewisser Weise zu beeinflussen**. Es könnten Parameteranpassungen, Formatierungsanweisungen, Themen-Taxonomien usw. sein, die dem Modell helfen können, seine Antwort an die gewünschten Nutzerziele oder Erwartungen anzupassen.

Beispiel: Gegeben sei ein Kurskatalog mit umfangreichen Metadaten (Name, Beschreibung, Niveau, Metadaten-Tags, Dozent usw.) zu allen verfügbaren Kursen im Lehrplan:

- Wir können eine Anweisung definieren, um "den Kurskatalog für Herbst 2023 zusammenzufassen".
- Wir können den Hauptinhalt nutzen, um einige Beispiele des gewünschten Outputs bereitzustellen.
- Wir können den sekundären Inhalt verwenden, um die Top 5 "Tags" von Interesse zu identifizieren.

Nun kann das Modell eine Zusammenfassung im Format der gezeigten Beispiele liefern - aber wenn ein Ergebnis mehrere Tags hat, kann es die 5 im sekundären Inhalt identifizierten Tags priorisieren.

---

<!--
UNTERRICHTSVORLAGE:
Diese Einheit sollte das Kernkonzept #1 abdecken.
Verstärken Sie das Konzept mit Beispielen und Referenzen.

KONZEPT #3:
Techniken des Prompt-Engineerings.
Was sind einige grundlegende Techniken für das Prompt-Engineering?
Veranschaulichen Sie es mit einigen Übungen.
-->

## Best Practices für Prompts

Jetzt, da wir wissen, wie Prompts _konstruiert_ werden können, können wir darüber nachdenken, wie wir sie _gestalten_ können, um Best Practices widerzuspiegeln. Wir können dies in zwei Teile unterteilen - die richtige _Einstellung_ und die Anwendung der richtigen _Techniken_.

### Einstellung zum Prompt-Engineering

Prompt-Engineering ist ein Prozess des Ausprobierens, daher sollten Sie drei breite Leitfaktoren im Auge behalten:

1. **Domänenverständnis zählt.** Die Genauigkeit und Relevanz der Antworten hängt von der _Domäne_ ab, in der die Anwendung oder der Benutzer arbeitet. Nutzen Sie Ihre Intuition und Fachkenntnisse, um **Techniken weiter anzupassen**. Definieren Sie beispielsweise _domänenspezifische Persönlichkeiten_ in Ihren System-Prompts oder verwenden Sie _domänenspezifische Vorlagen_ in Ihren Nutzer-Prompts. Stellen Sie sekundären Inhalt bereit, der domänenspezifische Kontexte widerspiegelt, oder verwenden Sie _domänenspezifische Hinweise und Beispiele_, um das Modell zu vertrauten Nutzungsmustern zu führen.

2. **Modellverständnis zählt.** Wir wissen, dass Modelle von Natur aus stochastisch sind. Aber Modellimplementierungen können auch hinsichtlich des verwendeten Trainingsdatensatzes (vortrainiertes Wissen), der bereitgestellten Fähigkeiten (z.B. über API oder SDK) und der Art der Inhalte, für die sie optimiert sind (z.B. Code vs. Bilder vs. Text), variieren. Verstehen Sie die Stärken und Einschränkungen des von Ihnen verwendeten Modells und nutzen Sie dieses Wissen, um _Aufgaben zu priorisieren_ oder _angepasste Vorlagen zu erstellen_, die für die Fähigkeiten des Modells optimiert sind.

3. **Iteration & Validierung zählen.** Modelle entwickeln sich schnell weiter, ebenso wie die Techniken des Prompt-Engineerings. Als Fachexperte können Sie andere Kontexte oder Kriterien für _Ihre_ spezifische Anwendung haben, die möglicherweise nicht auf die breitere Gemeinschaft zutreffen. Verwenden Sie Tools und Techniken des Prompt-Engineerings, um den Prompt-Aufbau zu "beschleunigen", und iterieren und validieren Sie die Ergebnisse dann mit Ihrer eigenen Intuition und Fachkenntnis. Zeichnen Sie Ihre Erkenntnisse auf und erstellen Sie eine **Wissensbasis** (z.B. Prompt-Bibliotheken), die als neue Grundlage für andere verwendet werden kann, um in Zukunft schnellere Iterationen zu ermöglichen.

## Best Practices

Schauen wir uns nun allgemeine Best Practices an, die von [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) und [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) Praktikern empfohlen werden.

| Was                               | Warum                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bewerten Sie die neuesten Modelle. | Neue Modellgenerationen haben wahrscheinlich verbesserte Funktionen und Qualität - können aber auch höhere Kosten verursachen. Bewerten Sie sie auf ihre Auswirkungen hin und treffen Sie dann Migrationsentscheidungen.                             |
| Trennen Sie Anweisungen & Kontext | Überprüfen Sie, ob Ihr Modell/Anbieter _Trennzeichen_ definiert, um Anweisungen, Haupt- und Sekundärinhalte klarer zu unterscheiden. Dies kann den Modellen helfen, Tokens genauer zu gewichten.                                                     |
| Seien Sie spezifisch und klar     | Geben Sie mehr Details über den gewünschten Kontext, das Ergebnis, die Länge, das Format, den Stil usw. an. Dies wird sowohl die Qualität als auch die Konsistenz der Antworten verbessern. Erfassen Sie Rezepte in wiederverwendbaren Vorlagen.      |
| Seien Sie beschreibend, verwenden Sie Beispiele | Modelle reagieren möglicherweise besser auf einen "zeigen und erzählen" Ansatz. Beginnen Sie mit einem `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` Werte. Kehren Sie zum Abschnitt [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) zurück, um zu erfahren, wie.

### Öffnen Sie als nächstes das Jupyter Notebook

- Wählen Sie den Laufzeitkernel aus. Wenn Sie die Optionen 1 oder 2 verwenden, wählen Sie einfach den Standard-Python 3.10.x-Kernel aus, der vom Dev-Container bereitgestellt wird.

Sie sind bereit, die Übungen durchzuführen. Beachten Sie, dass es hier keine _richtigen und falschen_ Antworten gibt - es geht nur darum, Optionen durch Ausprobieren zu erkunden und ein Gefühl dafür zu entwickeln, was für ein bestimmtes Modell und eine bestimmte Anwendungsdomäne funktioniert.

_Aus diesem Grund gibt es in dieser Lektion keine Code-Lösungssegmente. Stattdessen enthält das Notebook Markdown-Zellen mit dem Titel "Meine Lösung:", die ein Beispielergebnis als Referenz zeigen._

<!--
UNTERRICHTSVORLAGE:
Schließen Sie den Abschnitt mit einer Zusammenfassung und Ressourcen für selbstgesteuertes Lernen ab.
-->

## Wissensüberprüfung

Welche der folgenden Optionen ist ein gutes Prompt, das einigen vernünftigen Best Practices folgt?

1. Zeige mir ein Bild eines roten Autos
2. Zeige mir ein Bild eines roten Autos der Marke Volvo und Modell XC90, das an einer Klippe mit untergehender Sonne geparkt ist
3. Zeige mir ein Bild eines roten Autos der Marke Volvo und Modell XC90

A: 2, es ist das beste Prompt, da es Details zu "was" liefert und spezifisch wird (nicht nur ein beliebiges Auto, sondern eine bestimmte Marke und ein bestimmtes Modell) und es beschreibt auch die Gesamtszenerie. 3 ist das nächstbeste, da es ebenfalls viele Beschreibungen enthält.

## 🚀 Herausforderung

Sehen Sie, ob Sie die "Hinweis"-Technik mit dem Prompt nutzen können: Vervollständigen Sie den Satz "Zeige mir ein Bild eines roten Autos der Marke Volvo und ". Was antwortet es, und wie würden Sie es verbessern?

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Möchten Sie mehr über verschiedene Konzepte des Prompt-Engineerings erfahren? Besuchen Sie die [Seite für kontinuierliches Lernen](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), um weitere großartige Ressourcen zu diesem Thema zu finden.

Gehen Sie zu Lektion 5, in der wir uns [fortgeschrittene Prompting-Techniken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) ansehen werden!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.