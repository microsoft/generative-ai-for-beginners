# Cloud-Einrichtung ☁️ – GitHub Codespaces

**Verwenden Sie diese Anleitung, wenn Sie nichts lokal installieren möchten.**  
Codespaces bietet Ihnen eine kostenlose, browserbasierte VS Code-Instanz mit allen vorinstallierten Abhängigkeiten.

---

## 1.  Warum Codespaces?

| Vorteil | Was es für Sie bedeutet |
|---------|------------------------|
| ✅ Keine Installation | Funktioniert auf Chromebook, iPad, Schul-PCs… |
| ✅ Vorgefertigter Entwicklungscontainer | Python 3, Node.js, .NET, Java bereits enthalten |
| ✅ Kostenloses Kontingent | Private Accounts erhalten **120 Kern-Stunden / 60 GB-Stunden pro Monat** |

> 💡 **Tipp**  
> Halten Sie Ihr Kontingent gesund, indem Sie **inaktive Codespaces stoppen** oder **löschen**  
> (Ansicht ▸ Befehlspalette ▸ *Codespaces: Codespace anhalten*).

---

## 2.  Erstellen Sie einen Codespace (mit einem Klick)

1. **Forken** Sie dieses Repository (oben rechts auf die Schaltfläche **Fork** klicken).  
2. Klicken Sie in Ihrem Fork auf **Code ▸ Codespaces ▸ Codespace auf main erstellen**.  
   ![Dialog zeigt Schaltflächen zum Erstellen eines Codespace](../../../translated_images/de/who-will-pay.4c0609b1c7780f44.webp)

✅ Ein VS Code-Fenster im Browser öffnet sich und der Entwicklungscontainer wird aufgebaut.
Dies dauert beim ersten Mal **ca. 2 Minuten**.

## 3. Fügen Sie Ihren API-Schlüssel hinzu (der sichere Weg)

### Option A Codespaces Secrets — Empfohlen

1. ⚙️ Zahnrad-Symbol -> Befehlspalette -> Codespaces : Benutzergeheimnis verwalten -> Neues Geheimnis hinzufügen.
2. Name: OPENAI_API_KEY
3. Wert: Fügen Sie Ihren Schlüssel ein → Geheimnis hinzufügen

Das war’s — unser Code erkennt ihn automatisch.

### Option B .env-Datei (nur wenn wirklich nötig)

```bash
cp .env.copy .env
code .env         # füllen Sie OPENAI_API_KEY=dein_schlüssel_hier aus
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->