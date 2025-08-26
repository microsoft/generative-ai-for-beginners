<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T13:42:51+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "de"
}
-->
# Cloud-Setup ☁️ – GitHub Codespaces

**Nutze diese Anleitung, wenn du nichts lokal installieren möchtest.**  
Codespaces bietet dir eine kostenlose, browserbasierte VS Code-Instanz mit allen vorinstallierten Abhängigkeiten.

---

## 1.  Warum Codespaces?

| Vorteil | Was das für dich bedeutet |
|---------|--------------------------|
| ✅ Keine Installation nötig | Funktioniert auf Chromebook, iPad, Schul-PCs… |
| ✅ Vorgefertigter Dev-Container | Python 3, Node.js, .NET, Java sind schon drin |
| ✅ Kostenloses Kontingent | Private Accounts erhalten **120 Core-Stunden / 60 GB-Stunden pro Monat** |

> 💡 **Tipp**  
> Halte dein Kontingent gesund, indem du ungenutzte Codespaces **stoppst** oder **löschst**  
> (Ansicht ▸ Befehlspalette ▸ *Codespaces: Codespace stoppen*).

---

## 2.  Codespace erstellen (mit einem Klick)

1. **Forke** dieses Repository (oben rechts auf **Fork** klicken).  
2. In deinem Fork auf **Code ▸ Codespaces ▸ Create codespace on main** klicken.  
   ![Dialog mit Buttons zum Erstellen eines Codespaces](../../../00-course-setup/images/who-will-pay.webp)

✅ Ein VS Code-Fenster im Browser öffnet sich und der Dev-Container wird gestartet.
Beim ersten Mal dauert das **ca. 2 Minuten**.

## 3. Füge deinen API-Schlüssel hinzu (die sichere Methode)

### Option A Codespaces Secrets — Empfohlen

1. ⚙️ Zahnrad-Symbol -> Befehlspalette -> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Wert: Schlüssel einfügen → Add secret

Das war’s – unser Code erkennt den Schlüssel automatisch.

### Option B .env-Datei (nur wenn unbedingt nötig)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.