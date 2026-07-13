# Erstellen von Low Code KI-Anwendungen

[![Erstellen von Low Code KI-Anwendungen](../../../translated_images/de/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

## Einführung

Nachdem wir nun gelernt haben, wie man bildgenerierende Anwendungen erstellt, sprechen wir über Low Code. Generative KI kann in verschiedenen Bereichen eingesetzt werden, einschließlich Low Code, aber was ist Low Code und wie können wir KI hinzufügen?

Das Erstellen von Apps und Lösungen ist für traditionelle Entwickler und Nicht-Entwickler durch die Verwendung von Low Code Entwicklungsplattformen einfacher geworden. Low Code Entwicklungsplattformen ermöglichen es, Apps und Lösungen mit wenig bis gar keinem Code zu erstellen. Dies wird durch eine visuelle Entwicklungsumgebung erreicht, die es ermöglicht, Komponenten per Drag & Drop zu ziehen, um Apps und Lösungen zu bauen. Dadurch können Apps und Lösungen schneller und mit weniger Ressourcen erstellt werden. In dieser Lektion tauchen wir tief in die Verwendung von Low Code ein und wie man die Low Code Entwicklung mit KI unter Verwendung der Power Platform verbessern kann.

Die Power Platform bietet Organisationen die Möglichkeit, ihre Teams zu befähigen, eigene Lösungen durch eine intuitive Low-Code- oder No-Code-Umgebung zu erstellen. Diese Umgebung vereinfacht den Prozess der Lösungserstellung. Mit der Power Platform können Lösungen in Tagen oder Wochen statt Monaten oder Jahren erstellt werden. Die Power Platform besteht aus fünf Schlüsselprodukten: Power Apps, Power Automate, Power BI, Power Pages und Copilot Studio.

Diese Lektion behandelt:

- Einführung in Generative KI in der Power Platform
- Einführung in Copilot und wie man es benutzt
- Verwendung von Generative KI zum Erstellen von Apps und Flows in der Power Platform
- Verständnis der KI-Modelle in Power Platform mit AI Builder
- Erstellen intelligenter Agenten mit Microsoft Copilot Studio

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Zu verstehen, wie Copilot in der Power Platform funktioniert.

- Eine Student Assignment Tracker App für unser Bildungs-Startup zu erstellen.

- Einen Rechnungsverarbeitungs-Flow zu erstellen, der KI verwendet, um Informationen aus Rechnungen zu extrahieren.

- Best Practices bei der Verwendung des Create Text mit GPT KI-Modells anzuwenden.

- Zu verstehen, was Microsoft Copilot Studio ist und wie man intelligente Agenten damit erstellt.

Die Werkzeuge und Technologien, die Sie in dieser Lektion verwenden werden, sind:

- **Power Apps**, für die Student Assignment Tracker App, die eine Low-Code-Entwicklungsumgebung bietet, um Apps zum Nachverfolgen, Verwalten und Interagieren mit Daten zu erstellen.

- **Dataverse**, zur Speicherung der Daten für die Student Assignment Tracker App, wobei Dataverse eine Low-Code-Datenplattform für die Speicherung der App-Daten bereitstellt.

- **Power Automate**, für den Rechnungsverarbeitungs-Flow, wobei Sie eine Low-Code-Entwicklungsumgebung zur Erstellung von Workflows haben, um den Rechnungsverarbeitungsprozess zu automatisieren.

- **AI Builder**, für das Rechnungsverarbeitungs-KI-Modell, wobei Sie vorgefertigte KI-Modelle zur Rechnungserfassung für unser Startup verwenden.

## Generative KI in der Power Platform

Die Verbesserung der Low-Code-Entwicklung und -Anwendung mit generativer KI ist ein zentrales Fokusgebiet der Power Platform. Ziel ist es, jedem zu ermöglichen, KI-gestützte Apps, Websites, Dashboards und automatisierte Prozesse mit KI zu erstellen, _ohne dass Datenwissenschafts-Kenntnisse erforderlich sind_. Dieses Ziel wird erreicht, indem generative KI in das Low-Code-Entwicklungserlebnis der Power Platform in Form von Copilot und AI Builder integriert wird.

### Wie funktioniert das?

Copilot ist ein KI-Assistent, der es Ihnen ermöglicht, Power Platform-Lösungen zu erstellen, indem Sie Ihre Anforderungen in einer Reihe von konversationellen Schritten mit natürlicher Sprache beschreiben. Sie können zum Beispiel Ihrem KI-Assistenten anweisen, welche Felder Ihre App verwenden soll, und er erstellt sowohl die App als auch das zugrunde liegende Datenmodell, oder Sie könnten angeben, wie ein Flow in Power Automate eingerichtet werden soll.

Sie können Copilot-gesteuerte Funktionen auch als Feature auf Ihre App-Bildschirme einbauen, damit Benutzer durch konversationelle Interaktionen Einblicke gewinnen können.

AI Builder ist eine Low-Code-KI-Funktion in der Power Platform, die es Ihnen ermöglicht, KI-Modelle zu verwenden, um Prozesse zu automatisieren und Ergebnisse vorherzusagen. Mit AI Builder können Sie KI in Ihre Apps und Flows integrieren, die eine Verbindung zu Ihren Daten in Dataverse oder verschiedenen Cloud-Datenquellen wie SharePoint, OneDrive oder Azure herstellen.

Copilot ist in allen Power Platform-Produkten verfügbar: Power Apps, Power Automate, Power BI, Power Pages und Copilot Studio (ehemals Power Virtual Agents). AI Builder ist in Power Apps und Power Automate verfügbar. In dieser Lektion konzentrieren wir uns darauf, wie man Copilot und AI Builder in Power Apps und Power Automate verwendet, um eine Lösung für unser Bildungs-Startup zu erstellen.

### Copilot in Power Apps

Als Teil der Power Platform bietet Power Apps eine Low-Code-Entwicklungsumgebung zum Erstellen von Apps, die Daten verfolgen, verwalten und interagieren. Es ist eine App-Entwicklungs-Suite mit einer skalierbaren Datenplattform und der Möglichkeit, sich mit Cloud-Diensten und lokalen Daten zu verbinden. Power Apps ermöglicht Ihnen das Erstellen von Apps, die in Browsern, auf Tablets und Telefonen laufen und mit Kollegen geteilt werden können. Power Apps erleichtert Nutzern den Einstieg in die App-Entwicklung durch eine einfache Benutzeroberfläche, sodass jeder Geschäftsanwender oder professionelle Entwickler benutzerdefinierte Apps erstellen kann. Die App-Entwicklungserfahrung wird außerdem durch generative KI mithilfe von Copilot verbessert.

Die Copilot-KI-Assistent-Funktion in Power Apps ermöglicht es Ihnen, zu beschreiben, welche Art von App Sie benötigen und welche Informationen Ihre App nachverfolgen, sammeln oder anzeigen soll. Copilot generiert dann basierend auf Ihrer Beschreibung eine responsive Canvas-App. Sie können die App anschließend an Ihre Bedürfnisse anpassen. Der KI-Copilot generiert und schlägt auch eine Dataverse-Tabelle mit den Feldern vor, die Sie zum Speichern der zu verfolgenden Daten benötigen, sowie einige Beispieldaten. Später in dieser Lektion werden wir uns ansehen, was Dataverse ist und wie Sie es in Power Apps nutzen können. Sie können die Tabelle anschließend mithilfe der KI-Copilot-Assistent-Funktion über konversationelle Schritte an Ihre Bedürfnisse anpassen. Diese Funktion ist direkt vom Power Apps-Startbildschirm verfügbar.

### Copilot in Power Automate

Als Teil der Power Platform ermöglicht Power Automate Benutzern, automatisierte Workflows zwischen Anwendungen und Diensten zu erstellen. Es hilft, sich wiederholende Geschäftsprozesse wie Kommunikation, Datenerfassung und Entscheidungsfreigabe zu automatisieren. Die einfache Benutzeroberfläche ermöglicht es Benutzern aller technischen Kompetenzstufen (von Anfängern bis zu erfahrenen Entwicklern), Arbeitstätigkeiten zu automatisieren. Die Workflow-Entwicklung wird ebenfalls durch generative KI mithilfe von Copilot verbessert.

Die Copilot-KI-Assistent-Funktion in Power Automate ermöglicht es Ihnen, zu beschreiben, welchen Flow Sie benötigen und welche Aktionen Ihr Flow ausführen soll. Copilot generiert dann basierend auf Ihrer Beschreibung einen Flow. Sie können den Flow anschließend an Ihre Bedürfnisse anpassen. Der KI-Copilot generiert und schlägt auch die Aktionen vor, die Sie zum Ausführen der Aufgabe benötigen, die Sie automatisieren möchten. Später in dieser Lektion werden wir uns ansehen, was Flows sind und wie Sie diese in Power Automate verwenden können. Sie können die Aktionen anschließend mithilfe der KI-Copilot-Assistent-Funktion über konversationelle Schritte an Ihre Bedürfnisse anpassen. Diese Funktion ist direkt vom Power Automate-Startbildschirm verfügbar.

## Erstellen intelligenter Agenten mit Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (ehemals Power Virtual Agents) ist das Low-Code-Mitglied der Power Platform zum Erstellen von **KI-Agenten** — konversationelle Copiloten, die Fragen beantworten, Aktionen ausführen und Aufgaben im Auftrag Ihrer Benutzer automatisieren können. Genau wie der Rest der Power Platform erstellen Sie diese Agenten in einer visuellen, auf natürliche Sprache ausgerichteten Erfahrung: Sie beschreiben, was der Agent tun soll, und Copilot Studio hilft, dessen Anweisungen, Wissen und Aktionen zu strukturieren.

Für unser Bildungs-Startup könnten Sie einen Agenten erstellen, der Studentenfragen zu Kursen beantwortet, Abgabetermine überprüft und sogar Instruktoren E-Mails sendet — alles ohne Code zu schreiben.

Hier sind einige der neuesten Funktionen, die Copilot Studio mächtig machen:

- **Generative Antworten aus Ihrem Wissen**. Anstatt jedes Gespräch manuell zu verfassen, können Sie **Wissensquellen** — öffentliche Websites, SharePoint, OneDrive, Dataverse, hochgeladene Dateien oder Unternehmensdaten über Konnektoren — verbinden, und der Agent generiert fundierte Antworten daraus.

- **Generative Orchestrierung**. Anstatt sich auf starre Auslösephrasen zu verlassen, nutzt der Agent KI, um eine Anfrage zu verstehen und dynamisch zu entscheiden, welches Wissen, welche Themen und Aktionen kombiniert werden, um sie zu erfüllen, einschließlich dem Verknüpfen mehrerer Schritte.

- **Aktionen und Konnektoren**. Agenten können *Handlungen* ausführen, nicht nur chatten. Sie können einem Agenten Aktionen bereitstellen, die durch über 1.500 vorgefertigte Power Platform-Konnektoren, Power Automate-Flows, benutzerdefinierte REST-APIs, Prompts oder **Model Context Protocol (MCP)**-Server unterstützt werden.

- **Autonome Agenten**. Agenten sind nicht auf Antworten im Chatfenster beschränkt. Sie können **autonome Agenten** erstellen, die durch Ereignisse ausgelöst werden — wie eine neue E-Mail, ein neuer Datensatz in Dataverse oder ein hochgeladenes Datei — und dann im Hintergrund eine Aufgabe ausführen.

- **Multi-Agenten-Orchestrierung**. Agenten können andere Agenten aufrufen. Ein Copilot Studio-Agent kann an andere Agenten übergeben oder durch diese erweitert werden, einschließlich Agenten, die für Microsoft 365 Copilot veröffentlicht oder in Microsoft Foundry erstellt wurden.

- **Modellauswahl**. Neben den eingebauten Modellen können Sie Modelle aus dem Microsoft Foundry Modellkatalog verwenden, um zu steuern, wie Ihr Agent denkt und antwortet.

- **Überall veröffentlichen**. Ein Agent kann nach dem Erstellen in mehreren Kanälen veröffentlicht werden — Microsoft Teams, Microsoft 365 Copilot, einer Website oder benutzerdefinierten App und mehr — mit Sicherheit, Authentifizierung und Analysen, die über die Power Platform-Administratorerfahrung verwaltet werden.

Sie können Ihren ersten Agenten unter [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) erstellen und mehr in der [Microsoft Copilot Studio-Dokumentation](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst) lernen.

## Aufgabe: Verwalten Sie Studentenaufgaben und Rechnungen für unser Startup mit Copilot

Unser Startup bietet Online-Kurse für Studenten an. Das Startup ist schnell gewachsen und hat nun Schwierigkeiten, mit der Nachfrage nach seinen Kursen Schritt zu halten. Das Startup hat Sie als Power Platform-Entwickler eingestellt, um ihnen zu helfen, eine Low-Code-Lösung zu erstellen, die ihnen bei der Verwaltung von Studentenaufgaben und Rechnungen hilft. Die Lösung soll ihnen ermöglichen, Studentenaufgaben über eine App zu verfolgen und zu verwalten und den Rechnungsverarbeitungsprozess durch einen Workflow zu automatisieren. Sie wurden gebeten, Generative KI zu verwenden, um die Lösung zu entwickeln.

Wenn Sie mit der Verwendung von Copilot beginnen, können Sie die [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) nutzen, um mit den Prompts zu starten. Diese Bibliothek enthält eine Liste von Prompts, die Sie verwenden können, um Apps und Flows mit Copilot zu erstellen. Sie können auch die Prompts in der Bibliothek verwenden, um eine Vorstellung davon zu bekommen, wie Sie Ihre Anforderungen an Copilot beschreiben.

### Erstellen Sie eine Student Assignment Tracker App für Unser Startup

Die Lehrkräfte unseres Startups haben Schwierigkeiten, den Überblick über Studentenaufgaben zu behalten. Sie haben eine Tabelle verwendet, um die Aufgaben zu verfolgen, aber das ist aufgrund der gestiegenen Anzahl von Studenten schwer zu verwalten geworden. Sie haben Sie gebeten, eine App zu erstellen, die ihnen beim Nachverfolgen und Verwalten von Studentenaufgaben hilft. Die App soll es ermöglichen, neue Aufgaben hinzuzufügen, Aufgaben anzusehen, Aufgaben zu aktualisieren und Aufgaben zu löschen. Die App soll auch Lehrkräften und Studenten ermöglichen, die bewerteten und die noch nicht bewerteten Aufgaben einzusehen.

Sie werden die App unter Verwendung von Copilot in Power Apps anhand der folgenden Schritte erstellen:

1. Navigieren Sie zum [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) Startbildschirm.

1. Verwenden Sie das Textfeld auf dem Startbildschirm, um die App zu beschreiben, die Sie erstellen möchten. Zum Beispiel **_Ich möchte eine App erstellen, um Studentenaufgaben zu verfolgen und zu verwalten_**. Klicken Sie auf die **Senden**-Schaltfläche, um den Prompt an den KI-Copilot zu senden.

![Beschreiben Sie die App, die Sie erstellen möchten](../../../translated_images/de/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. Der KI-Copilot schlägt eine Dataverse-Tabelle mit den Feldern vor, die Sie zum Speichern der zu verfolgenden Daten benötigen, sowie einige Beispieldaten. Sie können die Tabelle dann mithilfe der KI-Copilot-Assistent-Funktion über konversationelle Schritte an Ihre Bedürfnisse anpassen.

   > **Wichtig**: Dataverse ist die zugrunde liegende Datenplattform der Power Platform. Es ist eine Low-Code-Datenplattform zum Speichern der App-Daten. Es ist ein vollständig verwalteter Dienst, der Daten sicher in der Microsoft Cloud speichert und innerhalb Ihrer Power Platform-Umgebung bereitgestellt wird. Es verfügt über eingebaute Funktionen zur Datenverwaltung wie Datenklassifizierung, Datenherkunft, fein granulare Zugriffskontrolle und mehr. Mehr über Dataverse erfahren Sie [hier](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Vorgeschlagene Felder in Ihrer neuen Tabelle](../../../translated_images/de/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Die Lehrkräfte wollen E-Mails an die Studenten senden, die ihre Aufgaben eingereicht haben, um sie über den Fortschritt ihrer Aufgaben zu informieren. Sie können Copilot verwenden, um der Tabelle ein neues Feld hinzuzufügen, in dem die Studenten-E-Mail gespeichert wird. Zum Beispiel können Sie den folgenden Prompt verwenden, um ein neues Feld hinzuzufügen: **_Ich möchte eine Spalte hinzufügen, um die Studenten-E-Mail zu speichern_**. Klicken Sie auf die **Senden**-Schaltfläche, um den Prompt an den KI-Copilot zu senden.

![Hinzufügen eines neuen Feldes](../../../translated_images/de/copilot-new-column.35e15ff21acaf274.webp)

1. Der KI-Copilot generiert ein neues Feld und Sie können das Feld anschließend an Ihre Anforderungen anpassen.


1. Sobald Sie mit der Tabelle fertig sind, klicken Sie auf die Schaltfläche **App erstellen**, um die App zu erstellen.

1. Der KI-Copilot generiert eine reaktionsfähige Canvas-App basierend auf Ihrer Beschreibung. Anschließend können Sie die App an Ihre Bedürfnisse anpassen.

1. Für Lehrkräfte, die E-Mails an Studierende senden möchten, können Sie Copilot verwenden, um der App einen neuen Bildschirm hinzuzufügen. Beispielsweise können Sie die folgende Eingabeaufforderung verwenden, um der App einen neuen Bildschirm hinzuzufügen: **_Ich möchte einen Bildschirm hinzufügen, um E-Mails an Studierende zu senden_**. Klicken Sie auf die Schaltfläche **Senden**, um die Aufforderung an den KI-Copilot zu senden.

![Hinzufügen eines neuen Bildschirms über eine Eingabeaufforderung](../../../translated_images/de/copilot-new-screen.2e0bef7132a17392.webp)

1. Der KI-Copilot erstellt einen neuen Bildschirm, den Sie dann an Ihre Bedürfnisse anpassen können.

1. Sobald Sie mit der App fertig sind, klicken Sie auf die Schaltfläche **Speichern**, um die App zu speichern.

1. Um die App mit den Lehrkräften zu teilen, klicken Sie auf die Schaltfläche **Freigeben** und klicken Sie dann erneut auf die Schaltfläche **Freigeben**. Sie können die App dann mit den Lehrkräften teilen, indem Sie ihre E-Mail-Adressen eingeben.

> **Deine Hausaufgabe**: Die App, die Sie gerade erstellt haben, ist ein guter Anfang, kann aber verbessert werden. Mit der E-Mail-Funktion können Lehrkräfte E-Mails nur manuell an Studierende senden, indem sie deren E-Mails eingeben müssen. Können Sie Copilot verwenden, um eine Automatisierung zu erstellen, die es den Lehrkräften ermöglicht, automatisch E-Mails an Studierende zu senden, wenn diese ihre Aufgaben einreichen? Dein Hinweis: Mit der richtigen Eingabeaufforderung kannst du Copilot in Power Automate verwenden, um dies zu erstellen.

### Erstellen einer Rechnungstabelle für unser Startup

Das Finanzteam unseres Startups hat Schwierigkeiten, den Überblick über Rechnungen zu behalten. Sie haben eine Tabelle verwendet, um die Rechnungen zu verfolgen, aber dies ist schwierig geworden, da die Anzahl der Rechnungen zugenommen hat. Sie haben Sie gebeten, eine Tabelle zu erstellen, die ihnen hilft, die Daten der erhaltenen Rechnungen zu speichern, zu verfolgen und zu verwalten. Die Tabelle soll verwendet werden, um eine Automatisierung zu erstellen, die alle Rechnungsinformationen extrahiert und in der Tabelle speichert. Außerdem soll die Tabelle dem Finanzteam ermöglichen, bezahlte und unbezahlte Rechnungen anzuzeigen.

Die Power Platform verfügt über eine zugrundeliegende Datenplattform namens Dataverse, die es Ihnen ermöglicht, die Daten für Ihre Apps und Lösungen zu speichern. Dataverse bietet eine Low-Code-Datenplattform zur Speicherung der App-Daten. Es ist ein vollständig verwalteter Service, der Daten sicher in der Microsoft Cloud speichert und innerhalb Ihrer Power Platform-Umgebung bereitgestellt wird. Es bietet integrierte Datenverwaltungsmöglichkeiten, wie Datenklassifizierung, Datenherkunft, fein abgestufte Zugriffskontrolle und mehr. Weitere Informationen zu Dataverse finden Sie [hier](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Warum sollten wir Dataverse für unser Startup verwenden? Die Standard- und benutzerdefinierten Tabellen in Dataverse bieten eine sichere und cloudbasierte Speicheroption für Ihre Daten. Tabellen ermöglichen es Ihnen, verschiedene Datentypen zu speichern, ähnlich wie Sie mehrere Arbeitsblätter in einer Excel-Arbeitsmappe verwenden. Sie können Tabellen verwenden, um Daten zu speichern, die spezifisch für Ihre Organisation oder Geschäftsbedürfnisse sind. Zu den Vorteilen, die unser Startup durch die Verwendung von Dataverse erhält, gehören unter anderem:

- **Einfach zu verwalten**: Sowohl Metadaten als auch Daten werden in der Cloud gespeichert, sodass Sie sich keine Sorgen darüber machen müssen, wie sie gespeichert oder verwaltet werden. Sie können sich auf den Aufbau Ihrer Apps und Lösungen konzentrieren.

- **Sicher**: Dataverse bietet eine sichere und cloudbasierte Speicheroption für Ihre Daten. Sie können steuern, wer Zugriff auf die Daten in Ihren Tabellen hat und wie dieser Zugriff erfolgt, mittels rollenbasierter Sicherheit.

- **Umfangreiche Metadaten**: Datentypen und Beziehungen werden direkt innerhalb von Power Apps verwendet.

- **Logik und Validierung**: Sie können Geschäftsregeln, berechnete Felder und Validierungsregeln verwenden, um Geschäftslogik durchzusetzen und die Datenintegrität zu wahren.

Jetzt, wo Sie wissen, was Dataverse ist und warum Sie es verwenden sollten, sehen wir uns an, wie Sie Copilot verwenden können, um eine Tabelle in Dataverse zu erstellen, die den Anforderungen unseres Finanzteams entspricht.

> **Hinweis** : Sie werden diese Tabelle im nächsten Abschnitt verwenden, um eine Automatisierung zu erstellen, die alle Rechnungsinformationen extrahiert und in der Tabelle speichert.

Um mit Copilot eine Tabelle in Dataverse zu erstellen, befolgen Sie die folgenden Schritte:

1. Navigieren Sie zum Startbildschirm von [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Wählen Sie in der linken Navigationsleiste **Tabellen** und klicken Sie dann auf **Neue Tabelle beschreiben**.

![Neue Tabelle auswählen](../../../translated_images/de/describe-new-table.0792373eb757281e.webp)

1. Verwenden Sie auf dem Bildschirm **Neue Tabelle beschreiben** das Textfeld, um die Tabelle zu beschreiben, die Sie erstellen möchten. Zum Beispiel: **_Ich möchte eine Tabelle erstellen, um Rechnungsinformationen zu speichern_**. Klicken Sie auf die Schaltfläche **Senden**, um die Aufforderung an den KI-Copilot zu senden.

![Beschreibung der Tabelle](../../../translated_images/de/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. Der KI-Copilot schlägt Ihnen eine Dataverse-Tabelle mit den Feldern vor, die Sie benötigen, um die zu verfolgenden Daten zu speichern, sowie einige Beispieldaten. Anschließend können Sie die Tabelle mit der Copilot-Assistenzfunktion über Konversationsschritte anpassen.

![Vorgeschlagene Dataverse-Tabelle](../../../translated_images/de/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Das Finanzteam möchte dem Lieferanten eine E-Mail senden, um diesen über den aktuellen Status seiner Rechnung zu informieren. Sie können Copilot verwenden, um der Tabelle ein neues Feld hinzuzufügen, in dem die E-Mail-Adresse des Lieferanten gespeichert wird. Zum Beispiel können Sie die folgende Aufforderung verwenden, um der Tabelle eine neue Spalte hinzuzufügen: **_Ich möchte eine Spalte hinzufügen, um die E-Mail des Lieferanten zu speichern_**. Klicken Sie auf die Schaltfläche **Senden**, um die Aufforderung an den KI-Copilot zu senden.

1. Der KI-Copilot erstellt ein neues Feld, das Sie anschließend an Ihre Bedürfnisse anpassen können.

1. Sobald Sie mit der Tabelle fertig sind, klicken Sie auf die Schaltfläche **Erstellen**, um die Tabelle zu erstellen.

## KI-Modelle in der Power Platform mit AI Builder

AI Builder ist eine Low-Code-KI-Funktion in der Power Platform, die es Ihnen ermöglicht, KI-Modelle zu verwenden, um Prozesse zu automatisieren und Ergebnisse vorherzusagen. Mit AI Builder können Sie KI in Ihre Apps und Abläufe integrieren, die mit Ihren Daten in Dataverse oder verschiedenen Cloud-Datenquellen wie SharePoint, OneDrive oder Azure verbunden sind.

## Vorgefertigte KI-Modelle vs. Benutzerdefinierte KI-Modelle

AI Builder bietet zwei Arten von KI-Modellen: Vorgefertigte KI-Modelle und Benutzerdefinierte KI-Modelle. Vorgefertigte KI-Modelle sind einsatzbereite Modelle, die von Microsoft trainiert und in der Power Platform zur Verfügung gestellt werden. Diese helfen Ihnen, Intelligenz zu Ihren Apps und Abläufen hinzuzufügen, ohne dass Sie Daten sammeln oder eigene Modelle erstellen, trainieren und veröffentlichen müssen. Sie können diese Modelle verwenden, um Prozesse zu automatisieren und Ergebnisse vorherzusagen.

Einige der in der Power Platform verfügbaren vorgefertigten KI-Modelle sind:

- **Schlüsselwortextraktion**: Dieses Modell extrahiert Schlüsselwörter aus Texten.
- **Spracherkennung**: Dieses Modell erkennt die Sprache eines Textes.
- **Stimmungsanalyse**: Dieses Modell erkennt positive, negative, neutrale oder gemischte Stimmungen in Texten.
- **Visitenkartenerkennung**: Dieses Modell extrahiert Informationen von Visitenkarten.
- **Texterkennung**: Dieses Modell extrahiert Text aus Bildern.
- **Objekterkennung**: Dieses Modell erkennt und extrahiert Objekte aus Bildern.
- **Dokumentenverarbeitung**: Dieses Modell extrahiert Informationen aus Formularen.
- **Rechnungsverarbeitung**: Dieses Modell extrahiert Informationen aus Rechnungen.

Mit Benutzerdefinierten KI-Modellen können Sie Ihr eigenes Modell in AI Builder integrieren, sodass es wie jedes andere benutzerdefinierte Modell in AI Builder funktioniert und mit Ihren eigenen Daten trainiert werden kann. Sie können diese Modelle verwenden, um Prozesse in Power Apps und Power Automate zu automatisieren und Ergebnisse vorherzusagen. Bei Verwendung eigener Modelle gelten bestimmte Einschränkungen. Lesen Sie mehr zu diesen [Einschränkungen](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![KI-Builder-Modelle](../../../translated_images/de/ai-builder-models.8069423b84cfc47f.webp)

## Aufgabe #2 - Erstellen eines Workflows zur Rechnungsverarbeitung für unser Startup

Das Finanzteam hat Schwierigkeiten bei der Verarbeitung von Rechnungen. Sie haben eine Tabelle verwendet, um die Rechnungen zu verfolgen, aber dies ist schwierig geworden, da die Anzahl der Rechnungen zugenommen hat. Sie haben Sie gebeten, einen Workflow zu erstellen, der ihnen bei der Verarbeitung von Rechnungen mit KI hilft. Der Workflow sollte es ihnen ermöglichen, Informationen aus Rechnungen zu extrahieren und diese Informationen in einer Dataverse-Tabelle zu speichern. Außerdem sollte der Workflow es ermöglichen, dem Finanzteam eine E-Mail mit den extrahierten Informationen zu senden.

Nun, da Sie wissen, was AI Builder ist und warum Sie es verwenden sollten, sehen wir uns an, wie Sie das Rechnungsverarbeitungs-KI-Modell in AI Builder, das wir zuvor behandelt haben, verwenden können, um einen Workflow zu erstellen, der dem Finanzteam bei der Rechnungsverarbeitung hilft.

Um einen Workflow zu erstellen, der dem Finanzteam bei der Rechnungsverarbeitung mit dem Rechnungsverarbeitungs-KI-Modell in AI Builder hilft, befolgen Sie die folgenden Schritte:

1. Navigieren Sie zum Startbildschirm von [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Verwenden Sie den Textbereich auf dem Startbildschirm, um den Workflow zu beschreiben, den Sie erstellen möchten. Zum Beispiel: **_Verarbeite eine Rechnung, wenn sie in meinem Postfach ankommt_**. Klicken Sie auf die Schaltfläche **Senden**, um die Aufforderung an den KI-Copilot zu senden.

   ![Copilot Power Automate](../../../translated_images/de/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. Der KI-Copilot schlägt die Aktionen vor, die Sie benötigen, um die Aufgabe, die Sie automatisieren möchten, auszuführen. Sie können auf die Schaltfläche **Weiter** klicken, um die nächsten Schritte durchzugehen.

4. Im nächsten Schritt fordert Sie Power Automate auf, die für den Ablauf erforderlichen Verbindungen einzurichten. Nachdem Sie fertig sind, klicken Sie auf die Schaltfläche **Workflow erstellen**, um den Ablauf zu erstellen.

5. Der KI-Copilot erstellt einen Ablauf, den Sie anschließend an Ihre Bedürfnisse anpassen können.

6. Aktualisieren Sie den Trigger des Ablaufs und legen Sie den **Ordner** auf den Ordner fest, in dem die Rechnungen gespeichert werden. Zum Beispiel können Sie den Ordner auf **Posteingang** setzen. Klicken Sie auf **Erweiterte Optionen anzeigen** und setzen Sie **Nur mit Anhängen** auf **Ja**. Dadurch wird sichergestellt, dass der Ablauf nur ausgeführt wird, wenn eine E-Mail mit Anhang im Ordner eingeht.

7. Entfernen Sie die folgenden Aktionen aus dem Ablauf: **HTML zu Text**, **Compose**, **Compose 2**, **Compose 3** und **Compose 4**, da Sie diese nicht verwenden werden.

8. Entfernen Sie die Aktion **Bedingung** aus dem Ablauf, da Sie diese nicht verwenden werden. Es sollte wie im folgenden Screenshot aussehen:

   ![Power Automate, Aktionen entfernen](../../../translated_images/de/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klicken Sie auf die Schaltfläche **Aktion hinzufügen** und suchen Sie nach **Dataverse**. Wählen Sie die Aktion **Neue Zeile hinzufügen** aus.

10. Aktualisieren Sie bei der Aktion **Informationen aus Rechnungen extrahieren** die **Rechnungsdatei**, sodass sie auf den **Anlageinhalt** aus der E-Mail verweist. Dadurch wird sichergestellt, dass der Ablauf Informationen aus dem Anhang der Rechnung extrahiert.

11. Wählen Sie die Tabelle aus, die Sie zuvor erstellt haben. Zum Beispiel können Sie die Tabelle **Rechnungsinformationen** auswählen. Wählen Sie die dynamischen Inhalte aus der vorherigen Aktion aus, um die folgenden Felder zu füllen:

    - ID
    - Betrag
    - Datum
    - Name
    - Status - Setzen Sie den **Status** auf **Ausstehend**.
    - E-Mail Lieferant - Verwenden Sie den dynamischen Inhalt **Von** aus dem Trigger **Wenn eine neue E-Mail eintrifft**.

    ![Power Automate Zeile hinzufügen](../../../translated_images/de/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Sobald Sie mit dem Ablauf fertig sind, klicken Sie auf die Schaltfläche **Speichern**, um den Ablauf zu sichern. Sie können den Ablauf dann testen, indem Sie eine E-Mail mit einer Rechnung an den Ordner senden, den Sie im Trigger angegeben haben.

> **Deine Hausaufgabe**: Der Ablauf, den du gerade erstellt hast, ist ein guter Anfang. Nun musst du überlegen, wie du eine Automatisierung erstellen kannst, die es unserem Finanzteam ermöglicht, dem Lieferanten eine E-Mail zu senden, um ihn über den aktuellen Status seiner Rechnung zu informieren. Dein Hinweis: Der Ablauf muss ausgeführt werden, wenn sich der Status der Rechnung ändert.

## Verwendung eines Textgenerierungs-KI-Modells in Power Automate

Das KI-Modell "Text mit GPT erstellen" in AI Builder ermöglicht es Ihnen, basierend auf einer Eingabeaufforderung Text zu generieren und wird vom Microsoft Azure OpenAI Service unterstützt. Mit dieser Funktion können Sie GPT-Technologie (Generative Pre-Trained Transformer) in Ihre Apps und Abläufe integrieren, um eine Vielzahl automatisierter Abläufe und intelligenter Anwendungen zu erstellen.

GPT-Modelle durchlaufen ein umfangreiches Training mit riesigen Datenmengen, was ihnen ermöglicht, Text zu erzeugen, der menschlicher Sprache sehr nahekommt, wenn sie eine Eingabeaufforderung erhalten. In Verbindung mit Workflow-Automatisierung können KI-Modelle wie GPT genutzt werden, um zahlreiche Aufgaben effizient zu automatisieren und zu optimieren.

Zum Beispiel können Sie Abläufe erstellen, die automatisch Text für verschiedene Anwendungsfälle generieren, wie Entwürfe von E-Mails, Produktbeschreibungen und mehr. Sie können das Modell auch verwenden, um Texte für verschiedene Apps zu generieren, wie Chatbots und Kundenservice-Apps, die Kundenservice-Mitarbeitern ermöglichen, effektiv und effizient auf Kundenanfragen zu reagieren.

![Erstelle eine Eingabeaufforderung](../../../translated_images/de/create-prompt-gpt.69d429300c2e870a.webp)


Um zu lernen, wie Sie dieses KI-Modell in Power Automate verwenden, durchlaufen Sie das Modul [Intelligenz mit AI Builder und GPT hinzufügen](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Tolle Arbeit! Setzen Sie Ihr Lernen fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter auszubauen!

Möchten Sie Copilot anpassen und mehr daraus herausholen? Erkunden Sie [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — eine von der Community beigetragene Sammlung von Anweisungen, Agenten, Skills und Konfigurationen, die Ihnen helfen, GitHub Copilot optimal zu nutzen.

Gehen Sie zu Lektion 11, wo wir uns ansehen, wie man [Generative AI mit Function Calling integriert](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->