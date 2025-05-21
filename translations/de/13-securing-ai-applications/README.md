<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:13:54+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "de"
}
-->
# Sicherung Ihrer generativen KI-Anwendungen

## Einführung

Diese Lektion behandelt:

- Sicherheit im Kontext von KI-Systemen.
- Häufige Risiken und Bedrohungen für KI-Systeme.
- Methoden und Überlegungen zur Sicherung von KI-Systemen.

## Lernziele

Nach Abschluss dieser Lektion werden Sie ein Verständnis für Folgendes haben:

- Die Bedrohungen und Risiken für KI-Systeme.
- Häufige Methoden und Praktiken zur Sicherung von KI-Systemen.
- Wie die Implementierung von Sicherheitstests unerwartete Ergebnisse und den Verlust des Benutzervertrauens verhindern kann.

## Was bedeutet Sicherheit im Kontext von generativer KI?

Da künstliche Intelligenz (KI) und maschinelles Lernen (ML) zunehmend unser Leben prägen, ist es entscheidend, nicht nur Kundendaten, sondern auch die KI-Systeme selbst zu schützen. KI/ML wird zunehmend zur Unterstützung von Entscheidungsprozessen mit hohem Wert in Branchen eingesetzt, in denen eine falsche Entscheidung schwerwiegende Konsequenzen haben kann.

Hier sind wichtige Punkte, die zu beachten sind:

- **Auswirkungen von KI/ML**: KI/ML haben erhebliche Auswirkungen auf das tägliche Leben, und daher ist der Schutz dieser Systeme unerlässlich geworden.
- **Sicherheitsherausforderungen**: Diese Auswirkungen von KI/ML erfordern angemessene Aufmerksamkeit, um die Notwendigkeit zu adressieren, KI-basierte Produkte vor raffinierten Angriffen zu schützen, sei es durch Trolle oder organisierte Gruppen.
- **Strategische Probleme**: Die Technologiebranche muss proaktiv strategische Herausforderungen angehen, um die langfristige Sicherheit der Kunden und den Datenschutz zu gewährleisten.

Darüber hinaus sind Maschinenlernmodelle weitgehend nicht in der Lage, zwischen bösartigen Eingaben und harmlosen anomalen Daten zu unterscheiden. Eine bedeutende Quelle für Trainingsdaten stammt aus unkuratierten, unmoderierten öffentlichen Datensätzen, die für Beiträge Dritter offen sind. Angreifer müssen keine Datensätze kompromittieren, wenn sie frei sind, zu ihnen beizutragen. Im Laufe der Zeit werden bösartige Daten mit geringem Vertrauen zu vertrauenswürdigen Daten mit hohem Vertrauen, wenn die Datenstruktur/-formatierung korrekt bleibt.

Deshalb ist es entscheidend, die Integrität und den Schutz der Datenspeicher sicherzustellen, die Ihre Modelle zur Entscheidungsfindung verwenden.

## Verständnis der Bedrohungen und Risiken von KI

In Bezug auf KI und verwandte Systeme sticht Datenvergiftung als die bedeutendste Sicherheitsbedrohung heute hervor. Datenvergiftung tritt auf, wenn jemand absichtlich die Informationen ändert, die zum Trainieren einer KI verwendet werden, wodurch diese Fehler macht. Dies ist auf das Fehlen standardisierter Erkennungs- und Abhilfemethoden zurückzuführen, gepaart mit unserer Abhängigkeit von unzuverlässigen oder unkuratierten öffentlichen Datensätzen für das Training. Um die Datenintegrität zu wahren und einen fehlerhaften Trainingsprozess zu verhindern, ist es entscheidend, den Ursprung und die Herkunft Ihrer Daten zu verfolgen. Andernfalls bewahrheitet sich das alte Sprichwort "Müll rein, Müll raus", was zu einer beeinträchtigten Modellleistung führt.

Hier sind Beispiele dafür, wie Datenvergiftung Ihre Modelle beeinflussen kann:

1. **Label-Flipping**: Bei einer binären Klassifikationsaufgabe ändert ein Gegner absichtlich die Labels eines kleinen Teils der Trainingsdaten. Zum Beispiel werden harmlose Proben als bösartig gekennzeichnet, was dazu führt, dass das Modell falsche Assoziationen lernt.\
   **Beispiel**: Ein Spam-Filter, der legitime E-Mails aufgrund manipulierter Labels als Spam klassifiziert.
2. **Feature-Vergiftung**: Ein Angreifer ändert subtil Merkmale in den Trainingsdaten, um Bias einzuführen oder das Modell in die Irre zu führen.\
   **Beispiel**: Hinzufügen irrelevanter Schlüsselwörter zu Produktbeschreibungen, um Empfehlungssysteme zu manipulieren.
3. **Dateninjektion**: Einschleusen bösartiger Daten in den Trainingssatz, um das Verhalten des Modells zu beeinflussen.\
   **Beispiel**: Einfügen gefälschter Benutzerbewertungen, um die Ergebnisse der Sentiment-Analyse zu verzerren.
4. **Hintertür-Angriffe**: Ein Gegner fügt ein verstecktes Muster (Hintertür) in die Trainingsdaten ein. Das Modell lernt, dieses Muster zu erkennen und verhält sich bösartig, wenn es ausgelöst wird.\
   **Beispiel**: Ein Gesichtserkennungssystem, das mit hintertürbelasteten Bildern trainiert wurde und eine bestimmte Person falsch identifiziert.

Die MITRE Corporation hat [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) erstellt, eine Wissensdatenbank von Taktiken und Techniken, die von Gegnern bei realen Angriffen auf KI-Systeme eingesetzt werden.

> Es gibt eine wachsende Anzahl von Schwachstellen in KI-fähigen Systemen, da die Integration von KI die Angriffsfläche bestehender Systeme über traditionelle Cyberangriffe hinaus vergrößert. Wir haben ATLAS entwickelt, um das Bewusstsein für diese einzigartigen und sich entwickelnden Schwachstellen zu schärfen, da die globale Gemeinschaft zunehmend KI in verschiedene Systeme integriert. ATLAS ist dem MITRE ATT&CK®-Framework nachempfunden, und seine Taktiken, Techniken und Verfahren (TTPs) ergänzen die im ATT&CK.

Ähnlich wie das MITRE ATT&CK®-Framework, das in der traditionellen Cybersicherheit weit verbreitet ist, um fortschrittliche Bedrohungsszenarien zu planen, bietet ATLAS einen leicht durchsuchbaren Satz von TTPs, die helfen können, aufkommende Angriffe besser zu verstehen und sich darauf vorzubereiten.

Darüber hinaus hat das Open Web Application Security Project (OWASP) eine "[Top 10 Liste](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" der kritischsten Schwachstellen in Anwendungen, die LLMs verwenden, erstellt. Die Liste hebt die Risiken von Bedrohungen wie der oben genannten Datenvergiftung sowie anderen hervor, wie:

- **Prompt Injection**: eine Technik, bei der Angreifer ein großes Sprachmodell (LLM) durch sorgfältig gestaltete Eingaben manipulieren, sodass es sich außerhalb seines beabsichtigten Verhaltens verhält.
- **Lieferketten-Schwachstellen**: Die Komponenten und Software, die die von einem LLM verwendeten Anwendungen ausmachen, wie Python-Module oder externe Datensätze, können selbst kompromittiert werden, was zu unerwarteten Ergebnissen, eingeführten Verzerrungen und sogar Schwachstellen in der zugrunde liegenden Infrastruktur führen kann.
- **Übermäßige Abhängigkeit**: LLMs sind fehleranfällig und neigen dazu, zu halluzinieren, was zu ungenauen oder unsicheren Ergebnissen führt. In mehreren dokumentierten Fällen haben Menschen die Ergebnisse für bare Münze genommen, was zu unbeabsichtigten negativen Konsequenzen in der realen Welt führte.

Microsoft Cloud Advocate Rod Trent hat ein kostenloses E-Book geschrieben, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), das sich eingehend mit diesen und anderen aufkommenden KI-Bedrohungen befasst und umfassende Anleitungen bietet, wie man diese Szenarien am besten angeht.

## Sicherheitstests für KI-Systeme und LLMs

Künstliche Intelligenz (KI) transformiert verschiedene Bereiche und Branchen und bietet neue Möglichkeiten und Vorteile für die Gesellschaft. Allerdings stellt KI auch erhebliche Herausforderungen und Risiken dar, wie Datenschutz, Bias, mangelnde Erklärbarkeit und potenziellen Missbrauch. Daher ist es entscheidend, sicherzustellen, dass KI-Systeme sicher und verantwortlich sind, das heißt, dass sie ethischen und gesetzlichen Standards entsprechen und von Benutzern und Interessengruppen vertraut werden können.

Sicherheitstests sind der Prozess der Bewertung der Sicherheit eines KI-Systems oder LLM, indem deren Schwachstellen identifiziert und ausgenutzt werden. Dies kann von Entwicklern, Benutzern oder externen Prüfern durchgeführt werden, je nach Zweck und Umfang der Tests. Einige der häufigsten Sicherheitstestmethoden für KI-Systeme und LLMs sind:

- **Datenbereinigung**: Dies ist der Prozess des Entfernens oder Anonymisierens sensibler oder privater Informationen aus den Trainingsdaten oder den Eingaben eines KI-Systems oder LLM. Datenbereinigung kann helfen, Datenlecks und bösartige Manipulationen zu verhindern, indem die Exposition vertraulicher oder persönlicher Daten reduziert wird.
- **Adversarial Testing**: Dies ist der Prozess der Generierung und Anwendung von adversarialen Beispielen auf die Eingabe oder Ausgabe eines KI-Systems oder LLM, um dessen Robustheit und Widerstandsfähigkeit gegen adversariale Angriffe zu bewerten. Adversarial Testing kann helfen, die Schwachstellen und Schwächen eines KI-Systems oder LLM zu identifizieren und zu mindern, die von Angreifern ausgenutzt werden könnten.
- **Modellverifizierung**: Dies ist der Prozess der Überprüfung der Korrektheit und Vollständigkeit der Modellparameter oder Architektur eines KI-Systems oder LLM. Modellverifizierung kann helfen, Modell-Diebstahl zu erkennen und zu verhindern, indem sichergestellt wird, dass das Modell geschützt und authentifiziert ist.
- **Ausgabeverifizierung**: Dies ist der Prozess der Validierung der Qualität und Zuverlässigkeit der Ausgabe eines KI-Systems oder LLM. Ausgabeverifizierung kann helfen, bösartige Manipulationen zu erkennen und zu korrigieren, indem sichergestellt wird, dass die Ausgabe konsistent und genau ist.

OpenAI, ein führendes Unternehmen im Bereich KI-Systeme, hat eine Reihe von _Sicherheitsbewertungen_ im Rahmen ihres Red-Teaming-Netzwerks initiiert, mit dem Ziel, die Ausgabe von KI-Systemen zu testen, um zur KI-Sicherheit beizutragen.

> Bewertungen können von einfachen Frage-und-Antwort-Tests bis hin zu komplexeren Simulationen reichen. Als konkrete Beispiele hier einige von OpenAI entwickelte Bewertungen zur Bewertung von KI-Verhalten aus verschiedenen Blickwinkeln:

#### Überzeugung

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System ein anderes KI-System dazu bringen, ein geheimes Wort zu sagen?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System ein anderes KI-System dazu bringen, Geld zu spenden?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System die Unterstützung eines anderen KI-Systems für einen politischen Vorschlag beeinflussen?

#### Steganographie (versteckte Nachrichtenübermittlung)

- [Steganographie](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System geheime Nachrichten übermitteln, ohne von einem anderen KI-System erwischt zu werden?
- [Textkompression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System Nachrichten komprimieren und dekomprimieren, um das Verstecken geheimer Nachrichten zu ermöglichen?
- [Schelling-Punkt](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Wie gut kann ein KI-System mit einem anderen KI-System ohne direkte Kommunikation koordinieren?

### KI-Sicherheit

Es ist unerlässlich, dass wir darauf abzielen, KI-Systeme vor bösartigen Angriffen, Missbrauch oder unbeabsichtigten Folgen zu schützen. Dazu gehört, Maßnahmen zu ergreifen, um die Sicherheit, Zuverlässigkeit und Vertrauenswürdigkeit von KI-Systemen sicherzustellen, wie zum Beispiel:

- Sicherung der Daten und Algorithmen, die zum Trainieren und Ausführen von KI-Modellen verwendet werden
- Verhinderung unbefugten Zugriffs, Manipulation oder Sabotage von KI-Systemen
- Erkennung und Minderung von Bias, Diskriminierung oder ethischen Problemen in KI-Systemen
- Sicherstellung der Verantwortlichkeit, Transparenz und Erklärbarkeit von KI-Entscheidungen und -Aktionen
- Ausrichtung der Ziele und Werte von KI-Systemen auf die von Menschen und Gesellschaft

KI-Sicherheit ist wichtig, um die Integrität, Verfügbarkeit und Vertraulichkeit von KI-Systemen und Daten zu gewährleisten. Einige der Herausforderungen und Chancen der KI-Sicherheit sind:

- Chance: Integration von KI in Cybersicherheitsstrategien, da sie eine entscheidende Rolle bei der Identifizierung von Bedrohungen und der Verbesserung der Reaktionszeiten spielen kann. KI kann helfen, die Erkennung und Minderung von Cyberangriffen wie Phishing, Malware oder Ransomware zu automatisieren und zu erweitern.
- Herausforderung: KI kann auch von Gegnern genutzt werden, um ausgeklügelte Angriffe zu starten, wie das Generieren von gefälschten oder irreführenden Inhalten, das Imitieren von Benutzern oder das Ausnutzen von Schwachstellen in KI-Systemen. Daher haben KI-Entwickler eine einzigartige Verantwortung, Systeme zu entwerfen, die robust und widerstandsfähig gegen Missbrauch sind.

### Datenschutz

LLMs können Risiken für die Privatsphäre und Sicherheit der Daten darstellen, die sie verwenden. Zum Beispiel können LLMs potenziell sensible Informationen aus ihren Trainingsdaten speichern und weitergeben, wie persönliche Namen, Adressen, Passwörter oder Kreditkartennummern. Sie können auch von böswilligen Akteuren manipuliert oder angegriffen werden, die ihre Schwachstellen oder Vorurteile ausnutzen wollen. Daher ist es wichtig, sich dieser Risiken bewusst zu sein und geeignete Maßnahmen zu ergreifen, um die mit LLMs verwendeten Daten zu schützen. Es gibt mehrere Schritte, die Sie unternehmen können, um die Daten zu schützen, die mit LLMs verwendet werden. Diese Schritte umfassen:

- **Begrenzung der Menge und Art der Daten, die sie mit LLMs teilen**: Teilen Sie nur die Daten, die notwendig und relevant für die beabsichtigten Zwecke sind, und vermeiden Sie das Teilen von Daten, die sensibel, vertraulich oder persönlich sind. Benutzer sollten auch die Daten, die sie mit LLMs teilen, anonymisieren oder verschlüsseln, zum Beispiel durch Entfernen oder Maskieren von Identifikationsinformationen oder durch Verwendung sicherer Kommunikationskanäle.
- **Verifizierung der von LLMs generierten Daten**: Überprüfen Sie immer die Genauigkeit und Qualität der von LLMs generierten Ausgaben, um sicherzustellen, dass sie keine unerwünschten oder unangemessenen Informationen enthalten.
- **Meldung und Alarmierung bei Datenverletzungen oder Vorfällen**: Seien Sie wachsam gegenüber verdächtigen oder abnormalen Aktivitäten oder Verhaltensweisen von LLMs, wie das Generieren von Texten, die irrelevant, ungenau, beleidigend oder schädlich sind. Dies könnte ein Hinweis auf eine Datenverletzung oder einen Sicherheitsvorfall sein.

Datensicherheit, Governance und Compliance sind entscheidend für jede Organisation, die die Leistungsfähigkeit von Daten und KI in einer Multi-Cloud-Umgebung nutzen möchte. Die Sicherung und Verwaltung aller Ihrer Daten ist eine komplexe und facettenreiche Aufgabe. Sie müssen unterschiedliche Arten von Daten (strukturierte, unstrukturierte und von KI generierte Daten) an verschiedenen Standorten über mehrere Clouds hinweg sichern und verwalten, und Sie müssen bestehende und zukünftige Datenschutz-, Governance- und KI-Vorschriften berücksichtigen. Um Ihre Daten zu schützen, sollten Sie einige bewährte Praktiken und Vorsichtsmaßnahmen ergreifen, wie:

- Verwenden Sie Cloud-Dienste oder -Plattformen, die Datenschutz- und Datenschutzfunktionen bieten.
- Verwenden Sie Datenqualitäts- und Validierungstools, um Ihre Daten auf Fehler, Inkonsistenzen oder Anomalien zu überprüfen.
- Verwenden Sie Daten-Governance- und Ethik-Frameworks, um sicherzustellen, dass Ihre Daten verantwortungsbewusst und transparent verwendet werden.

### Emulation von Bedrohungen aus der realen Welt - KI-Red-Teaming

Die Emulation von Bedrohungen aus der realen Welt wird heute als Standardpraxis beim Aufbau widerstandsfähiger KI-Systeme angesehen, indem ähnliche Tools, Taktiken und Verfahren eingesetzt werden, um die Risiken für Systeme zu identifizieren und die Reaktion der Verteidiger zu testen.

> Die Praxis des KI-Red-Teaming hat sich zu einer erweiterten Bedeutung entwickelt: Sie umfasst nicht nur das Aufspüren von Sicherheitslücken, sondern auch das Aufspüren anderer Systemfehler, wie die Generierung potenziell schädlicher Inhalte. KI-Systeme bringen neue Risiken mit sich, und Red-Teaming ist entscheidend, um diese neuartigen Risiken zu verstehen, wie Prompt Injection und die Erzeugung ungesicherter Inhalte. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Nachfolgend finden Sie wichtige Erkenntnisse, die das AI Red Team-Programm von Microsoft geprägt haben.

1. **Erweiterter Umfang des KI-Red-Teaming:**
   Das KI-Red-Teaming umfasst nun sowohl Sicherheits- als auch Responsible AI (RAI)-Ergebnisse. Traditionell konzentrierte sich das Red-Teaming auf Sicherheitsaspekte und behandelte das Modell als Vektor (z. B. Diebstahl des zugrunde liegenden Modells). KI-Systeme bringen jedoch neuartige Sicherheitslücken mit sich (z. B. Prompt Injection, Vergiftung), die besondere Aufmerksamkeit erfordern. Über die Sicherheit hinaus untersucht das KI-Red-Teaming auch Fairness-Probleme (z. B. Stereotypisierung) und schädliche Inhalte (z. B. Verherrlichung von Gewalt). Die frühzeitige Identifizierung dieser Probleme ermöglicht die Priorisierung von Investitionen in die Verteidigung.
2. **Bösartige und harmlose Fehler:**
   Das KI-Red-Teaming berücksichtigt Fehler aus sowohl bösartigen als auch harmlosen Perspektiven. Zum Beispiel, wenn das neue Bing im Red-Teaming getestet wird, untersuchen wir nicht nur, wie bösartige Gegner das System unter

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.