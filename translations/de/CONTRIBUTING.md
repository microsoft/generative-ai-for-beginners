# Mitwirken

Dieses Projekt heißt Beiträge und Vorschläge willkommen. Die meisten Beiträge setzen voraus, dass Sie
einem Contributor License Agreement (CLA) zustimmen, das erklärt, dass Sie das Recht haben,
und tatsächlich die Rechte eingeräumt haben, uns die Nutzung Ihres Beitrags zu gestatten. Für Details besuchen Sie
<https://cla.microsoft.com>.

> Wichtig: Wenn Sie Texte in diesem Repository übersetzen, verwenden Sie bitte keine maschinelle Übersetzung. Wir werden Übersetzungen durch die Community überprüfen, daher sollten Sie sich nur für Übersetzungen in Sprachen melden, in denen Sie geübt sind.

Wenn Sie einen Pull-Request einreichen, bestimmt ein CLA-Bot automatisch, ob Sie
ein CLA bereitstellen müssen und versieht den PR entsprechend (z. B. mit Label, Kommentar). Folgen Sie einfach den
Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unser CLA verwenden.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen.
Für weitere Informationen lesen Sie die [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Frage oder Problem?

Bitte eröffnen Sie keine GitHub-Issues für allgemeine Supportanfragen, da die GitHub-Liste für Feature-Anfragen und Fehlerberichte vorgesehen ist. So können wir tatsächliche Probleme oder Bugs im Code besser verfolgen und die allgemeine Diskussion vom eigentlichen Code getrennt halten.

## Tippfehler, Probleme, Bugs und Beiträge

Wenn Sie Änderungen im Generative AI for Beginners Repository einreichen, befolgen Sie bitte diese Empfehlungen.

* Forken Sie das Repository immer zunächst auf Ihr eigenes Konto, bevor Sie Änderungen vornehmen
* Fassen Sie nicht mehrere Änderungen in einem Pull Request zusammen. Reichen Sie z.B. Bugfixes und Dokumentationsupdates jeweils in separaten PRs ein
* Wenn Ihr Pull Request Merge-Konflikte anzeigt, aktualisieren Sie zunächst Ihr lokales main, damit es ein Spiegel des Hauptrepositories ist, bevor Sie Ihre Änderungen vornehmen
* Wenn Sie eine Übersetzung einreichen, erstellen Sie bitte einen PR für alle übersetzten Dateien, da wir keine Teilübersetzungen akzeptieren
* Wenn Sie einen Tippfehler oder Dokumentationsfehler korrigieren, können Sie Änderungen bei Bedarf in einem einzigen PR zusammenfassen

## Redaktioneller Umfang und Drittanbieterprodukte

Dieser Lehrplan konzentriert sich auf Microsoft-Technologien und herstellerneutrale offene Standards. Beiträge sollten einem klaren Bildungszweck dienen und dürfen nicht in erster Linie dazu dienen, ein kommerzielles Produkt, einen gehosteten Dienst, Modellrouter, SDK, MCP-Server oder ein anderes herstellerspezifisches Angebot vorzustellen oder zu bewerben.

Open-Source-Software und Drittanbieterabhängigkeiten dürfen referenziert werden, wenn sie notwendig sind, um einen offenen Standard oder ein Interoperabilitätsszenario zu erklären, neutral dargestellt werden und nicht im Mittelpunkt eines Herstellerprodukts oder gehosteten Endpunkts stehen. Wenn Ihr Vorschlag ein herstellerspezifisches Produkt oder einen Dienst umfasst, eröffnen Sie bitte ein Issue und holen Sie die Zustimmung des Maintainers ein, bevor Sie einen Pull Request einreichen.

Mitwirkende müssen alle relevanten Beschäftigungen, Eigentumsverhältnisse, Sponsorings oder andere Verbindungen mit einem Produkt oder Dienst, die in ihrem Beitrag erwähnt werden, offenlegen. Bitte fügen Sie keine unbelegten Preis-, Leistungs-, Sicherheits-, Datenschutz- oder Vergleichsaussagen hinzu. Ausführbare Beispiele dürfen standardmäßig keine Lernerdaten übertragen oder öffentliche Aktionen über externe Drittanbieterdienste ausführen.

## Allgemeine Richtlinien zum Schreiben

- Stellen Sie sicher, dass alle Ihre URLs in eckige Klammern eingeschlossen sind, gefolgt von runden Klammern ohne zusätzliche Leerzeichen darum oder darin `[]()`.
- Stellen Sie sicher, dass jeder relative Link (d. h. Links zu anderen Dateien und Ordnern im Repository) mit einem `./` beginnt, das auf eine Datei oder einen Ordner im aktuellen Arbeitsverzeichnis verweist, oder einem `../`, das auf eine Datei oder einen Ordner in einem übergeordneten Arbeitsverzeichnis verweist.
- Stellen Sie sicher, dass jeder relative Link (d. h. Links zu anderen Dateien und Ordnern im Repository) eine Tracking-ID (d. h. `?` oder `&` gefolgt von `wt.mc_id=` oder `WT.mc_id=`) am Ende hat.
- Stellen Sie sicher, dass jede URL von den folgenden Domains _github.com, microsoft.com, visualstudio.com, aka.ms und azure.com_ eine Tracking-ID (d. h. `?` oder `&` gefolgt von `wt.mc_id=` oder `WT.mc_id=`) am Ende hat.
- Stellen Sie sicher, dass Ihre Links keine länderspezifische Locale enthalten (d. h. `/en-us/` oder `/en/`).
- Stellen Sie sicher, dass alle Bilder im Ordner `./images` gespeichert sind.
- Stellen Sie sicher, dass die Bilder beschreibende Namen mit englischen Buchstaben, Zahlen und Bindestrichen enthalten.

## GitHub Workflows

Wenn Sie einen Pull Request einreichen, werden vier verschiedene Workflows ausgelöst, die die vorherigen Regeln überprüfen.
Befolgen Sie einfach die hier aufgeführten Anweisungen, um die Workflow-Prüfungen zu bestehen.

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check Paths Have Tracking](#check-paths-have-tracking)
- [Check URLs Have Tracking](#check-urls-have-tracking)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

### Check Broken Relative Paths

Dieser Workflow stellt sicher, dass jeder relative Pfad in Ihren Dateien funktioniert.
Dieses Repository wird auf GitHub Pages bereitgestellt, daher müssen Sie beim Eingeben der Links, die alles verbinden, sehr vorsichtig sein, um niemanden an die falsche Stelle zu leiten.

Um sicherzustellen, dass Ihre Links richtig funktionieren, verwenden Sie einfach VS Code dafür.

Zum Beispiel werden Sie beim Überfahren eines Links in Ihren Dateien dazu aufgefordert, dem Link über **Strg + Klick** zu folgen.

![VS code follow links screenshot](../../translated_images/de/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot von VS Code Eingabeaufforderung um einem Link zu folgen, wenn Sie darüber hovern.")

Wenn Sie auf einen Link klicken und dieser lokal nicht funktioniert, wird sicher der Workflow ausgelöst und er funktioniert auch nicht auf GitHub.

Um dieses Problem zu beheben, versuchen Sie, den Link mit Hilfe von VS Code einzugeben.

Wenn Sie `./` oder `../` eingeben, fordert VS Code Sie auf, aus verfügbaren Optionen entsprechend Ihrer Eingabe auszuwählen.

![VS code select relative path screenshot](../../translated_images/de/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot von VS Code Eingabeaufforderung zur Auswahl relativer Pfade aus einer Pop-up-Liste.")

Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den gewünschten Ordner klicken, und Sie können sicher sein, dass Ihr Pfad nicht defekt ist.

Sobald Sie den korrekten relativen Pfad hinzugefügt, gespeichert und Ihre Änderungen gepusht haben, wird der Workflow erneut ausgelöst, um Ihre Änderungen zu überprüfen.
Wenn Sie den Check bestehen, sind Sie startklar.

### Check Paths Have Tracking

Dieser Workflow stellt sicher, dass jeder relative Pfad eine Tracking-ID enthält.
Dieses Repository wird auf GitHub Pages bereitgestellt, daher müssen wir die Bewegung zwischen den verschiedenen Dateien und Ordnern nachverfolgen.

Um sicherzustellen, dass Ihre relativen Pfade Tracking enthalten, prüfen Sie einfach, ob am Ende des Pfads der Text `?wt.mc_id=` steht.
Wenn er an Ihre relativen Pfade angehängt ist, besteht Ihr Pfad diese Prüfung.

Falls nicht, erhalten Sie möglicherweise folgenden Fehler.

![GitHub check paths missing tracking comment screenshot](../../translated_images/de/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot von GitHub-Kommentar, der fehlendes Tracking bei relativen Pfaden anzeigt")

Um dieses Problem zu beheben, öffnen Sie den vom Workflow hervorgehobenen Datei-Pfad und fügen die Tracking-ID an das Ende der relativen Pfade ein.

Sobald Sie die Tracking-ID hinzugefügt, gespeichert und Ihre Änderungen gepusht haben, wird der Workflow erneut ausgelöst, um Ihre Änderungen zu überprüfen.
Wenn Sie den Check bestehen, sind Sie startklar.

### Check URLs Have Tracking

Dieser Workflow stellt sicher, dass jede Web-URL eine Tracking-ID enthält.
Dieses Repository ist für jeden verfügbar, daher müssen Sie den Zugriff verfolgen, um zu wissen, woher der Traffic kommt.

Um sicherzustellen, dass Ihre URLs Tracking enthalten, prüfen Sie einfach, ob am Ende der URL der Text `?wt.mc_id=` steht.
Wenn er an Ihre URLs angehängt ist, besteht Ihre URL diese Prüfung.

Falls nicht, erhalten Sie möglicherweise folgenden Fehler.

![GitHub check urls missing tracking comment screenshot](../../translated_images/de/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot von GitHub-Kommentar, der fehlendes Tracking bei URLs anzeigt")

Um dieses Problem zu beheben, öffnen Sie den vom Workflow hervorgehobenen Datei-Pfad und fügen die Tracking-ID an das Ende der URLs ein.

Sobald Sie die Tracking-ID hinzugefügt, gespeichert und Ihre Änderungen gepusht haben, wird der Workflow erneut ausgelöst, um Ihre Änderungen zu überprüfen.
Wenn Sie den Check bestehen, sind Sie startklar.

### Check URLs Don't Have Locale

Dieser Workflow stellt sicher, dass keine Web-URL eine länderspezifische Locale enthält.
Dieses Repository ist weltweit verfügbar, daher müssen Sie sicherstellen, die Locale Ihres Landes nicht in URLs einzubinden.

Um sicherzustellen, dass Ihre URLs keine Ländercode-Locale enthalten, prüfen Sie einfach, ob Text wie `/en-us/` oder `/en/` oder eine andere Sprachlocale irgendwo in der URL enthalten ist.
Wenn keine enthalten ist, bestehen Ihre URLs diese Prüfung.

Falls nicht, erhalten Sie möglicherweise folgenden Fehler.

![GitHub check country locale comment screenshot](../../translated_images/de/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot von GitHub-Kommentar, der eine hinzugefügte Ländercode-Locale in URLs anzeigt")

Um dieses Problem zu beheben, öffnen Sie den vom Workflow hervorgehobenen Datei-Pfad und entfernen die Ländercode-Locale aus den URLs.

Sobald Sie die Ländercode-Locale entfernt, gespeichert und Ihre Änderungen gepusht haben, wird der Workflow erneut ausgelöst, um Ihre Änderungen zu überprüfen.
Wenn Sie den Check bestehen, sind Sie startklar.

Herzlichen Glückwunsch! Wir werden uns so schnell wie möglich mit Feedback zu Ihrem Beitrag bei Ihnen melden.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->