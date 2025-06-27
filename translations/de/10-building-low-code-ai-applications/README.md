<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T17:49:42+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "de"
}
-->
# Erstellung von Low-Code-KI-Anwendungen

[![Erstellung von Low-Code-KI-Anwendungen](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.de.png)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

## Einführung

Nachdem wir gelernt haben, wie man Anwendungen zur Bildgenerierung erstellt, sprechen wir über Low Code. Generative KI kann in verschiedenen Bereichen eingesetzt werden, einschließlich Low Code. Aber was ist Low Code und wie können wir KI integrieren?

Das Erstellen von Apps und Lösungen ist durch den Einsatz von Low Code Development Platforms sowohl für traditionelle Entwickler als auch für Nicht-Entwickler einfacher geworden. Low Code Development Platforms ermöglichen es Ihnen, Apps und Lösungen mit wenig bis gar keinem Code zu erstellen. Dies wird durch eine visuelle Entwicklungsumgebung erreicht, die es Ihnen ermöglicht, Komponenten per Drag-and-Drop zu platzieren, um Apps und Lösungen zu erstellen. Dadurch können Sie Apps und Lösungen schneller und mit weniger Ressourcen entwickeln. In dieser Lektion tauchen wir tief in die Nutzung von Low Code ein und wie man die Low-Code-Entwicklung mit KI unter Verwendung der Power Platform verbessern kann.

Die Power Platform bietet Organisationen die Möglichkeit, ihre Teams zu befähigen, ihre eigenen Lösungen in einer intuitiven Low-Code- oder No-Code-Umgebung zu entwickeln. Diese Umgebung hilft, den Prozess der Erstellung von Lösungen zu vereinfachen. Mit der Power Platform können Lösungen in Tagen oder Wochen statt Monaten oder Jahren erstellt werden. Die Power Platform besteht aus fünf Hauptprodukten: Power Apps, Power Automate, Power BI, Power Pages und Copilot Studio.

Diese Lektion behandelt:

- Einführung in Generative KI in der Power Platform
- Einführung in Copilot und dessen Nutzung
- Nutzung von Generative KI zur Erstellung von Apps und Flows in der Power Platform
- Verständnis der KI-Modelle in der Power Platform mit AI Builder

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Verstehen, wie Copilot in der Power Platform funktioniert.

- Eine App zur Verfolgung von Studentenaufgaben für unser Bildungs-Startup erstellen.

- Einen Rechnungsverarbeitungs-Flow erstellen, der KI verwendet, um Informationen aus Rechnungen zu extrahieren.

- Beste Praktiken anwenden, wenn das GPT-KI-Modell zum Erstellen von Text verwendet wird.

Die Tools und Technologien, die Sie in dieser Lektion verwenden werden, sind:

- **Power Apps**, für die App zur Verfolgung von Studentenaufgaben, die eine Low-Code-Entwicklungsumgebung bietet, um Apps zu erstellen, die Daten verfolgen, verwalten und mit ihnen interagieren.

- **Dataverse**, zur Speicherung der Daten für die App zur Verfolgung von Studentenaufgaben, wo Dataverse eine Low-Code-Datenplattform zur Speicherung der App-Daten bereitstellt.

- **Power Automate**, für den Rechnungsverarbeitungs-Flow, wo Sie eine Low-Code-Entwicklungsumgebung haben, um Workflows zu erstellen, die den Rechnungsverarbeitungsprozess automatisieren.

- **AI Builder**, für das Rechnungsverarbeitungs-KI-Modell, bei dem Sie vorgefertigte KI-Modelle verwenden, um die Rechnungen für unser Startup zu verarbeiten.

## Generative KI in der Power Platform

Die Verbesserung der Low-Code-Entwicklung und -Anwendung mit generativer KI ist ein zentraler Schwerpunkt der Power Platform. Das Ziel ist es, jedem zu ermöglichen, KI-gestützte Apps, Websites, Dashboards zu erstellen und Prozesse mit KI zu automatisieren, _ohne jegliche Datenwissenschaftskenntnisse zu benötigen_. Dieses Ziel wird erreicht, indem generative KI in das Low-Code-Entwicklungserlebnis der Power Platform in Form von Copilot und AI Builder integriert wird.

### Wie funktioniert das?

Copilot ist ein KI-Assistent, der es Ihnen ermöglicht, Power Platform-Lösungen zu erstellen, indem Sie Ihre Anforderungen in einer Reihe von Konversationsschritten in natürlicher Sprache beschreiben. Sie können zum Beispiel Ihren KI-Assistenten anweisen, anzugeben, welche Felder Ihre App verwenden wird, und er erstellt sowohl die App als auch das zugrunde liegende Datenmodell oder Sie können angeben, wie ein Flow in Power Automate eingerichtet werden soll.

Sie können Copilot-gesteuerte Funktionen als Feature in Ihren App-Bildschirmen verwenden, um Benutzern zu ermöglichen, durch konversationelle Interaktionen Erkenntnisse zu gewinnen.

AI Builder ist eine Low-Code-KI-Funktionalität, die in der Power Platform verfügbar ist und es Ihnen ermöglicht, KI-Modelle zu verwenden, um Prozesse zu automatisieren und Ergebnisse vorherzusagen. Mit AI Builder können Sie KI in Ihre Apps und Flows bringen, die mit Ihren Daten in Dataverse oder in verschiedenen Cloud-Datenquellen wie SharePoint, OneDrive oder Azure verbunden sind.

Copilot ist in allen Produkten der Power Platform verfügbar: Power Apps, Power Automate, Power BI, Power Pages und Power Virtual Agents. AI Builder ist in Power Apps und Power Automate verfügbar. In dieser Lektion werden wir uns darauf konzentrieren, wie man Copilot und AI Builder in Power Apps und Power Automate verwendet, um eine Lösung für unser Bildungs-Startup zu erstellen.

### Copilot in Power Apps

Als Teil der Power Platform bietet Power Apps eine Low-Code-Entwicklungsumgebung zum Erstellen von Apps, die Daten verfolgen, verwalten und mit ihnen interagieren. Es ist eine Suite von App-Entwicklungsdiensten mit einer skalierbaren Datenplattform und der Fähigkeit, sich mit Cloud-Diensten und lokalen Daten zu verbinden. Power Apps ermöglicht es Ihnen, Apps zu erstellen, die in Browsern, auf Tablets und Telefonen laufen und mit Kollegen geteilt werden können. Power Apps erleichtert den Einstieg in die App-Entwicklung mit einer einfachen Benutzeroberfläche, sodass jeder Geschäftsanwender oder professionelle Entwickler benutzerdefinierte Apps erstellen kann. Das App-Entwicklungserlebnis wird auch durch generative KI durch Copilot verbessert.

Die Copilot-KI-Assistentenfunktion in Power Apps ermöglicht es Ihnen, zu beschreiben, welche Art von App Sie benötigen und welche Informationen Ihre App verfolgen, sammeln oder anzeigen soll. Copilot generiert dann eine responsive Canvas-App basierend auf Ihrer Beschreibung. Sie können die App dann an Ihre Bedürfnisse anpassen. Der KI-Copilot generiert und schlägt auch eine Dataverse-Tabelle mit den Feldern vor, die Sie benötigen, um die Daten zu speichern, die Sie verfolgen möchten, sowie einige Beispieldaten. Wir werden später in dieser Lektion sehen, was Dataverse ist und wie Sie es in Power Apps verwenden können. Sie können die Tabelle dann an Ihre Bedürfnisse anpassen, indem Sie die KI-Copilot-Assistentenfunktion durch konversationelle Schritte verwenden. Diese Funktion ist direkt vom Power Apps-Startbildschirm aus verfügbar.

### Copilot in Power Automate

Als Teil der Power Platform ermöglicht es Power Automate Benutzern, automatisierte Workflows zwischen Anwendungen und Diensten zu erstellen. Es hilft, sich wiederholende Geschäftsprozesse wie Kommunikation, Datenerfassung und Entscheidungsfreigaben zu automatisieren. Seine einfache Benutzeroberfläche ermöglicht es Benutzern mit jeder technischen Kompetenz (von Anfängern bis zu erfahrenen Entwicklern), Arbeitsaufgaben zu automatisieren. Das Workflow-Entwicklungserlebnis wird auch durch generative KI durch Copilot verbessert.

Die Copilot-KI-Assistentenfunktion in Power Automate ermöglicht es Ihnen, zu beschreiben, welche Art von Flow Sie benötigen und welche Aktionen Ihr Flow ausführen soll. Copilot generiert dann einen Flow basierend auf Ihrer Beschreibung. Sie können den Flow dann an Ihre Bedürfnisse anpassen. Der KI-Copilot generiert und schlägt auch die Aktionen vor, die Sie benötigen, um die Aufgabe zu automatisieren, die Sie automatisieren möchten. Wir werden später in dieser Lektion sehen, was Flows sind und wie Sie sie in Power Automate verwenden können. Sie können die Aktionen dann an Ihre Bedürfnisse anpassen, indem Sie die KI-Copilot-Assistentenfunktion durch konversationelle Schritte verwenden. Diese Funktion ist direkt vom Power Automate-Startbildschirm aus verfügbar.

## Aufgabe: Verwaltung von Studentenaufgaben und Rechnungen für unser Startup mit Copilot

Unser Startup bietet Studenten Online-Kurse an. Das Startup ist schnell gewachsen und hat nun Schwierigkeiten, mit der Nachfrage nach seinen Kursen Schritt zu halten. Das Startup hat Sie als Power Platform-Entwickler eingestellt, um ihnen zu helfen, eine Low-Code-Lösung zu entwickeln, die ihnen hilft, ihre Studentenaufgaben und Rechnungen zu verwalten. Die Lösung sollte ihnen helfen, Studentenaufgaben über eine App zu verfolgen und zu verwalten und den Rechnungsverarbeitungsprozess durch einen Workflow zu automatisieren. Sie wurden gebeten, generative KI zu verwenden, um die Lösung zu entwickeln.

Wenn Sie mit der Verwendung von Copilot beginnen, können Sie die [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) verwenden, um mit den Eingabeaufforderungen zu beginnen. Diese Bibliothek enthält eine Liste von Eingabeaufforderungen, die Sie verwenden können, um Apps und Flows mit Copilot zu erstellen. Sie können auch die Eingabeaufforderungen in der Bibliothek verwenden, um eine Vorstellung davon zu bekommen, wie Sie Ihre Anforderungen an Copilot beschreiben können.

### Erstellen Sie eine App zur Verfolgung von Studentenaufgaben für unser Startup

Die Lehrkräfte in unserem Startup haben Schwierigkeiten, den Überblick über die Studentenaufgaben zu behalten. Sie haben eine Tabelle verwendet, um die Aufgaben zu verfolgen, aber dies ist schwierig zu verwalten, da die Anzahl der Studenten gestiegen ist. Sie haben Sie gebeten, eine App zu erstellen, die ihnen hilft, die Aufgaben zu verfolgen und zu verwalten. Die App sollte es ihnen ermöglichen, neue Aufgaben hinzuzufügen, Aufgaben anzuzeigen, Aufgaben zu aktualisieren und Aufgaben zu löschen. Die App sollte auch Lehrkräften und Studenten ermöglichen, die Aufgaben anzuzeigen, die bewertet wurden, und diejenigen, die noch nicht bewertet wurden.

Sie werden die App mit Copilot in Power Apps gemäß den folgenden Schritten erstellen:

1. Navigieren Sie zum [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) Startbildschirm.

1. Verwenden Sie das Textfeld auf dem Startbildschirm, um die App zu beschreiben, die Sie erstellen möchten. Zum Beispiel: **_Ich möchte eine App zur Verfolgung und Verwaltung von Studentenaufgaben erstellen_**. Klicken Sie auf die **Senden**-Schaltfläche, um die Eingabeaufforderung an den KI-Copilot zu senden.

![Beschreiben Sie die App, die Sie erstellen möchten](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.de.png)

1. Der KI-Copilot wird eine Dataverse-Tabelle mit den Feldern vorschlagen, die Sie benötigen, um die Daten zu speichern, die Sie verfolgen möchten, sowie einige Beispieldaten. Sie können die Tabelle dann an Ihre Bedürfnisse anpassen, indem Sie die KI-Copilot-Assistentenfunktion durch konversationelle Schritte verwenden.

   > **Wichtig**: Dataverse ist die zugrunde liegende Datenplattform für die Power Platform. Es ist eine Low-Code-Datenplattform zur Speicherung der App-Daten. Es ist ein vollständig verwalteter Dienst, der Daten sicher in der Microsoft-Cloud speichert und innerhalb Ihrer Power Platform-Umgebung bereitgestellt wird. Es verfügt über integrierte Datenverwaltungskapazitäten wie Datenklassifizierung, Datenherkunft, feingranulare Zugriffskontrolle und mehr. Weitere Informationen zu Dataverse finden Sie [hier](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Vorgeschlagene Felder in Ihrer neuen Tabelle](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.de.png)

1. Lehrkräfte möchten E-Mails an die Studenten senden, die ihre Aufgaben eingereicht haben, um sie über den Fortschritt ihrer Aufgaben auf dem Laufenden zu halten. Sie können Copilot verwenden, um der Tabelle ein neues Feld hinzuzufügen, um die E-Mail-Adresse des Studenten zu speichern. Zum Beispiel können Sie die folgende Eingabeaufforderung verwenden, um der Tabelle ein neues Feld hinzuzufügen: **_Ich möchte eine Spalte hinzufügen, um die E-Mail-Adresse des Studenten zu speichern_**. Klicken Sie auf die **Senden**-Schaltfläche, um die Eingabeaufforderung an den KI-Copilot zu senden.

![Hinzufügen eines neuen Feldes](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.de.png)

1. Der KI-Copilot wird ein neues Feld generieren und Sie können das Feld dann an Ihre Bedürfnisse anpassen.

1. Sobald Sie mit der Tabelle fertig sind, klicken Sie auf die **App erstellen**-Schaltfläche, um die App zu erstellen.

1. Der KI-Copilot wird eine responsive Canvas-App basierend auf Ihrer Beschreibung generieren. Sie können die App dann an Ihre Bedürfnisse anpassen.

1. Damit Lehrkräfte E-Mails an Studenten senden können, können Sie Copilot verwenden, um der App einen neuen Bildschirm hinzuzufügen. Zum Beispiel können Sie die folgende Eingabeaufforderung verwenden, um der App einen neuen Bildschirm hinzuzufügen: **_Ich möchte einen Bildschirm hinzufügen, um E-Mails an Studenten zu senden_**. Klicken Sie auf die **Senden**-Schaltfläche, um die Eingabeaufforderung an den KI-Copilot zu senden.

![Hinzufügen eines neuen Bildschirms über eine Eingabeaufforderung](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.de.png)

1. Der KI-Copilot wird einen neuen Bildschirm generieren und Sie können den Bildschirm dann an Ihre Bedürfnisse anpassen.

1. Sobald Sie mit der App fertig sind, klicken Sie auf die **Speichern**-Schaltfläche, um die App zu speichern.

1. Um die App mit den Lehrkräften zu teilen, klicken Sie auf die **Teilen**-Schaltfläche und dann erneut auf die **Teilen**-Schaltfläche. Sie können die App dann mit den Lehrkräften teilen, indem Sie deren E-Mail-Adressen eingeben.

> **Ihre Hausaufgabe**: Die App, die Sie gerade erstellt haben, ist ein guter Anfang, kann aber verbessert werden. Mit der E-Mail-Funktion können Lehrkräfte nur manuell E-Mails an Studenten senden, indem sie deren E-Mails eingeben. Können Sie Copilot verwenden, um eine Automatisierung zu erstellen, die es Lehrkräften ermöglicht, E-Mails automatisch an Studenten zu senden, wenn sie ihre Aufgaben einreichen? Ihr Hinweis ist, dass Sie mit der richtigen Eingabeaufforderung Copilot in Power Automate verwenden können, um dies zu erstellen.

### Erstellen Sie eine Rechnungstabelle für unser Startup

Das Finanzteam unseres Startups hat Schwierigkeiten, den Überblick über Rechnungen zu behalten. Sie haben eine Tabelle verwendet, um die Rechnungen zu verfolgen, aber dies ist schwierig zu verwalten, da die Anzahl der Rechnungen gestiegen ist. Sie haben Sie gebeten, eine Tabelle zu erstellen, die ihnen hilft, die Informationen der erhaltenen Rechnungen zu speichern, zu verfolgen und zu verwalten. Die Tabelle sollte verwendet werden, um eine Automatisierung zu erstellen, die alle Rechnungsinformationen extrahiert und in der Tabelle speichert. Die Tabelle sollte auch dem Finanzteam ermöglichen, die Rechnungen anzuzeigen, die bezahlt wurden, und diejenigen, die noch nicht bezahlt wurden.

Die Power Platform verfügt über eine zugrunde liegende Datenplattform namens Dataverse, die es Ihnen ermöglicht, die Daten für Ihre Apps und Lösungen zu speichern. Dataverse bietet eine Low-Code-Datenplattform zur Speicherung der App-Daten. Es ist ein vollständig verwalteter Dienst, der Daten sicher in der Microsoft-Cloud speichert und innerhalb Ihrer Power Platform-Umgebung bereitgestellt wird. Es verfügt über integrierte Datenverwaltungskapazitäten wie Datenklassifizierung, Datenherkunft, feingranulare Zugriffskontrolle und mehr. Weitere Informationen [über Dataverse finden Sie hier](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Warum sollten wir Dataverse für unser Startup verwenden? Die Standard- und benutzerdefinierten Tabellen innerhalb von Dataverse bieten eine sichere und cloudbasierte Speicheroption für Ihre Daten. Tabellen ermöglichen es Ihnen, verschiedene Arten von Daten zu speichern, ähnlich wie Sie mehrere Arbeitsblätter in einer einzigen Excel-Arbeitsmappe verwenden könnten. Sie können Tabellen verwenden, um Daten zu speichern, die spezifisch für Ihre Organisation oder Geschäftsanforderungen sind. Einige der Vorteile, die unser Startup durch die Verwendung von Dataverse erhält, umfassen unter anderem:

- **Einfach zu verwalten**: Sowohl die Metadaten als auch die Daten werden in der Cloud gespeichert, sodass Sie sich nicht um die Details kümmern müssen, wie sie gespeichert oder verwaltet werden. Sie können sich auf den Aufbau Ihrer Apps und Lösungen konzentrieren.

- **Sicher**: Dataverse bietet eine sichere und cloudbasierte Speicheroption für Ihre Daten. Sie können steuern, wer Zugriff auf die Daten in Ihren Tabellen hat und wie sie darauf zugreifen können, indem Sie rollenbasierte Sicherheit verwenden.

- **Reiche Metadaten**: Datentypen und Beziehungen werden direkt in Power Apps verwendet.

- **Logik und Validierung**: Sie können Geschäftsregeln, berechnete Felder und Validierungsregeln verwenden, um Geschäftslogik durchzusetzen und die Datenintegrität zu gewährleisten.

Jetzt, da Sie wissen, was Dataverse ist und warum Sie es verwenden sollten, schauen wir uns an, wie Sie Copilot verwenden können, um eine Tabelle in Dataverse zu erstellen, die den Anforderungen unseres Finanzteams entspricht.

> **Hinweis**: Sie werden diese Tabelle im nächsten Abschnitt verwenden, um eine Automatisierung zu erstellen, die alle Rechnungsinformationen extrahiert und in der Tabelle speichert.
Um eine Tabelle in Dataverse mit Copilot zu erstellen, folgen Sie den folgenden Schritten: 1. Navigieren Sie zum [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) Startbildschirm. 2. Wählen Sie in der linken Navigationsleiste **Tabellen** aus und klicken Sie dann auf **Neue Tabelle beschreiben**. ![Neue Tabelle auswählen](../../../translated_images/describe-new-table.0792373eb757281e3c5f542f84cad3b5208bfe0e5c4a7786dd2bd31aa848a23c.de.png) 1. Verwenden Sie auf dem Bildschirm **Neue Tabelle beschreiben** das Textfeld, um die Tabelle zu beschreiben, die Sie erstellen möchten. Zum Beispiel: **_Ich möchte eine Tabelle erstellen, um Rechnungsinformationen zu speichern_**. Klicken Sie auf die **Senden**-Schaltfläche, um die Eingabeaufforderung an den KI-Copilot zu senden. ![Tabelle beschreiben](../../../translated_images/copilot-chat-prompt-dataverse.feb2f81e5872b9d2b05d45d11bb6830e0f2ef6a2d4742413bc9a1e50a45bbb89.de.png) 1. Der KI-Copilot wird eine Dataverse-Tabelle mit den Feldern vorschlagen, die Sie benötigen, um die Daten zu speichern, die Sie verfolgen möchten,
ein Text. - **Sentimentanalyse**: Dieses Modell erkennt positive, negative, neutrale oder gemischte Stimmung in Texten. - **Visitenkartenleser**: Dieses Modell extrahiert Informationen aus Visitenkarten. - **Texterkennung**: Dieses Modell extrahiert Text aus Bildern. - **Objekterkennung**: Dieses Modell erkennt und extrahiert Objekte aus Bildern. - **Dokumentenverarbeitung**: Dieses Modell extrahiert Informationen aus Formularen. - **Rechnungsverarbeitung**: Dieses Modell extrahiert Informationen aus Rechnungen. Mit benutzerdefinierten KI-Modellen können Sie Ihr eigenes Modell in AI Builder einbringen, sodass es wie jedes benutzerdefinierte Modell in AI Builder funktioniert und Sie das Modell mit Ihren eigenen Daten trainieren können. Sie können diese Modelle verwenden, um Prozesse zu automatisieren und Ergebnisse in sowohl Power Apps als auch Power Automate vorherzusagen. Bei der Verwendung Ihres eigenen Modells gelten bestimmte Einschränkungen. Lesen Sie mehr über diese [Einschränkungen](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst). ![AI Builder Modelle](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.de.png) ## Aufgabe #2 - Erstellen eines Rechnungsverarbeitungs-Workflows für unser Startup Das Finanzteam hat Schwierigkeiten, Rechnungen zu verarbeiten. Sie haben eine Tabelle verwendet, um die Rechnungen zu verfolgen, aber dies ist schwierig zu handhaben geworden, da die Anzahl der Rechnungen zugenommen hat. Sie haben Sie gebeten, einen Workflow zu erstellen, der ihnen hilft, Rechnungen mit KI zu verarbeiten. Der Workflow sollte ihnen ermöglichen, Informationen aus Rechnungen zu extrahieren und diese Informationen in einer Dataverse-Tabelle zu speichern. Der Workflow sollte ihnen auch ermöglichen, dem Finanzteam eine E-Mail mit den extrahierten Informationen zu senden. Jetzt, da Sie wissen, was AI Builder ist und warum Sie es verwenden sollten, schauen wir uns an, wie Sie das Rechnungsverarbeitungs-KI-Modell in AI Builder, das wir zuvor behandelt haben, verwenden können, um einen Workflow zu erstellen, der dem Finanzteam hilft, Rechnungen zu verarbeiten. Um einen Workflow zu erstellen, der dem Finanzteam hilft, Rechnungen mit dem Rechnungsverarbeitungs-KI-Modell in AI Builder zu verarbeiten, folgen Sie den untenstehenden Schritten: 1. Navigieren Sie zum [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) Startbildschirm. 2. Verwenden Sie das Textfeld auf dem Startbildschirm, um den Workflow zu beschreiben, den Sie erstellen möchten. Zum Beispiel, **_Verarbeite eine Rechnung, wenn sie in meinem Posteingang ankommt_**. Klicken Sie auf die **Senden**-Schaltfläche, um die Eingabeaufforderung an den KI-Copilot zu senden. ![Copilot Power Automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.de.png) 3. Der KI-Copilot wird die Aktionen vorschlagen, die Sie ausführen müssen, um die Aufgabe zu automatisieren, die Sie durchführen möchten. Sie können auf die **Weiter**-Schaltfläche klicken, um die nächsten Schritte durchzugehen. 4. Im nächsten Schritt wird Power Automate Sie auffordern, die für den Flow erforderlichen Verbindungen einzurichten. Wenn Sie fertig sind, klicken Sie auf die **Flow erstellen**-Schaltfläche, um den Flow zu erstellen. 5. Der KI-Copilot wird einen Flow generieren, und Sie können dann den Flow an Ihre Bedürfnisse anpassen. 6. Aktualisieren Sie den Auslöser des Flows und setzen Sie den **Ordner** auf den Ordner, in dem die Rechnungen gespeichert werden. Zum Beispiel können Sie den Ordner auf **Posteingang** setzen. Klicken Sie auf **Erweiterte Optionen anzeigen** und setzen Sie **Nur mit Anhängen** auf **Ja**. Dies stellt sicher, dass der Flow nur läuft, wenn eine E-Mail mit Anhang im Ordner empfangen wird. 7. Entfernen Sie die folgenden Aktionen aus dem Flow: **HTML zu Text**, **Zusammensetzen**, **Zusammensetzen 2**, **Zusammensetzen 3** und **Zusammensetzen 4**, da Sie diese nicht verwenden werden. 8. Entfernen Sie die **Bedingung**-Aktion aus dem Flow, da Sie diese nicht verwenden werden. Es sollte wie im folgenden Screenshot aussehen: ![Power Automate, Aktionen entfernen](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.de.png) 9. Klicken Sie auf die **Aktion hinzufügen**-Schaltfläche und suchen Sie nach **Dataverse**. Wählen Sie die **Neue Zeile hinzufügen**-Aktion. 10. Aktualisieren Sie in der **Informationen aus Rechnungen extrahieren**-Aktion die **Rechnungsdatei**, um auf den **Anhangsinhalt** aus der E-Mail zu verweisen. Dies stellt sicher, dass der Flow Informationen aus dem Rechnungsanhang extrahiert. 11. Wählen Sie die **Tabelle**, die Sie zuvor erstellt haben. Zum Beispiel können Sie die **Rechnungsinformationen**-Tabelle auswählen. Wählen Sie den dynamischen Inhalt aus der vorherigen Aktion, um die folgenden Felder auszufüllen: - ID - Betrag - Datum - Name - Status - Setzen Sie den **Status** auf **Ausstehend**. - Lieferanten-E-Mail - Verwenden Sie den **Von**-dynamischen Inhalt aus dem **Wenn eine neue E-Mail eintrifft**-Auslöser. ![Power Automate Zeile hinzufügen](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.de.png) 12. Wenn Sie mit dem Flow fertig sind, klicken Sie auf die **Speichern**-Schaltfläche, um den Flow zu speichern. Sie können den Flow dann testen, indem Sie eine E-Mail mit einer Rechnung an den im Auslöser angegebenen Ordner senden. > **Ihre Hausaufgabe**: Der Flow, den Sie gerade erstellt haben, ist ein guter Anfang. Jetzt müssen Sie darüber nachdenken, wie Sie eine Automatisierung erstellen können, die unserem Finanzteam ermöglicht, eine E-Mail an den Lieferanten zu senden, um ihn über den aktuellen Status seiner Rechnung zu informieren. Ihr Hinweis: Der Flow muss ausgeführt werden, wenn sich der Status der Rechnung ändert.

## Verwenden eines Textgenerierungs-KI-Modells in Power Automate

Das Erstellen von Text mit dem GPT-KI-Modell in AI Builder ermöglicht Ihnen, Text basierend auf einer Eingabeaufforderung zu generieren und wird vom Microsoft Azure OpenAI Service betrieben. Mit dieser Fähigkeit können Sie GPT (Generative Pre-Trained Transformer) Technologie in Ihre Apps und Flows integrieren, um eine Vielzahl von automatisierten Flows und aufschlussreichen Anwendungen zu erstellen.

GPT-Modelle durchlaufen umfangreiche Schulungen mit großen Datenmengen, die es ihnen ermöglichen, Text zu produzieren, der menschlicher Sprache nahekommt, wenn sie mit einer Eingabeaufforderung versehen werden. Bei der Integration mit Workflow-Automatisierung können KI-Modelle wie GPT genutzt werden, um eine Vielzahl von Aufgaben zu vereinfachen und zu automatisieren.

Zum Beispiel können Sie Flows erstellen, um automatisch Text für verschiedene Anwendungsfälle zu generieren, wie: Entwürfe von E-Mails, Produktbeschreibungen und mehr. Sie können das Modell auch verwenden, um Text für verschiedene Apps zu generieren, wie Chatbots und Kundendienst-Apps, die Kundendienstmitarbeitern ermöglichen, effektiv und effizient auf Kundenanfragen zu reagieren.

![Erstellen einer Eingabeaufforderung](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.de.png)

Um zu lernen, wie Sie dieses KI-Modell in Power Automate verwenden, gehen Sie durch das [Modul zur Hinzufügung von Intelligenz mit AI Builder und GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Großartige Arbeit! Setzen Sie Ihr Lernen fort

Nachdem Sie diese Lektion abgeschlossen haben, schauen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

Gehen Sie zu Lektion 11, wo wir uns anschauen, wie man [Generative KI mit Funktionsaufrufen integriert](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle angesehen werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.