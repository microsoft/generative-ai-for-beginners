# Änderungsprotokoll

Alle bemerkenswerten Änderungen am Generative AI for Beginners Curriculum sind in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Da es sich um ein
Lerncurriculum und nicht um ein versioniertes Softwarepaket handelt, sind die Einträge nach Datum gruppiert.

## [2026-07-16] — Inhaltsvalidierung + Bildmaterial für Lektion 09

### Geändert

- **Lektion 10 (Low-Code AI-Apps):** zwei veraltete `docs.microsoft.com/powerapps/...` Dataverse-Links
  wurden zu den aktuellen `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (live überprüft) aktualisiert.
- **Lektion 17 (KI-Agenten):** veraltetes Modellbeispiel modernisiert (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o und Llama 3.3`) sowie ein Platzhalter-Bereitstellungsname im Agent Framework Beispiel
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`) aktualisiert.
- **Root `README.md`:** die fehlende `?WT.mc_id=academic-105485-koreyst` Verfolgungs-ID zum
  *Microsoft for Startups*-Link hinzugefügt.
- **Bildmaterial der Lektion 09** mit dem Modell `gpt-image` neu generiert: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` und
  `images/startup.png` (das Beispiel zum Editieren vor/nach wurde über einen echten
  `client.images.edit` Aufruf mit einer generierten Maske erstellt).

### Validiert

- README-Dateien der Lektionen 01, 03, 05, 12, 14 und 16 geprüft — alle aktuell (korrekte Microsoft Foundry
  Benennung und Links); keine Änderungen notwendig.
- Eine umfassende Markdown-Validierung aller 41 Markdown-Dateien im Repo (ohne Übersetzungen) auf
  veraltete Dokumentpfade, `/en-us/` Microsoft-Lokalisierungen, veraltete Produkt-/Modellnamen, fehlende Tracking-
  IDs und defekte relative Links/Bilder durchgeführt. Nur die einzelne *Microsoft for Startups* Tracking-ID-Lücke
  war relevant; alle anderen Warnungen erwiesen sich als Fehlalarme (auto-generierte Übersetzungslinks,
  auskommentierte Platzhalter und Drittanbieter-`/en/` Struktur-URLs).

## [2026-07-15] — Neuverfassung von Lektion 09 (Bildanwendungen) für GPT-Bildmodelle

### Geändert

- **Lektion 09 „Bauen von Bildgenerierungsanwendungen“ neu geschrieben** rund um die aktuelle **`gpt-image`**
  Modellfamilie (Standard **`gpt-image-2`**; auch `gpt-image-1.5` / `gpt-image-1-mini` GA), ersetzt Legacy-
  DALL·E 2/3 Inhalte. Wichtige Korrekturen:
  - `gpt-image` Modelle liefern das Bild als **Base64 (`b64_json`)**, nicht als URL. Alle Beispiele wurden
    auf `base64.b64decode(...)` anstelle Herunterladen der `url` mit `requests` angeglichen.
  - Die Bild-API-Version wurde auf `2025-04-01-preview` erhöht.
  - Den erfundenen „temperature“-Abschnitt (Bildmodelle akzeptieren kein `temperature`) und die
    DALL·E-2-exklusive Bildvariationen durch einen Abschnitt **Bildbearbeitung** (Maske/Inpainting) ersetzt.
  - `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, beide
    Zuordnungs-Notebooks (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) und das .NET `.dib` Notebook aktualisiert.

### Entfernt

- Die veralteten Samples `python/aoai-app-variation.py` und `python/oai-app-variation.py` gelöscht
  (`images.create_variation` ist DALL·E-2-exklusiv und von `gpt-image` nicht unterstützt).
- Vier verwaiste Bilddateien entfernt, die an den entfernten Temperaturvergleichsabschnitt gebunden waren
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Die unnötige `requests`-Abhängigkeit aus den Python-Beispielen und Anforderungen der Lektion entfernt.

### Validiert

- `aoai-app.py` End-to-End mit einem bereitgestellten `gpt-image-1.5` Modell getestet und bestätigt, dass
  der Base64-decode/save-Flow ein PNG erzeugt. Notebooks auf gültiges JSON überprüft.

## [2026-07-14] — Standardmodell-Update + Anleitung für Reasoning-Modelle

### Geändert

- **Standard-Chatmodell von `gpt-4o-mini` → `gpt-5-mini`** in allen ausführbaren Proben,
  Dokumentationen und Konfigurationen der Curriculum. Ursache war der Modelllebenszyklus: bei Microsoft Foundry
  wird `gpt-4o-mini` (Ausmusterung 2026-10-01) und gesamte `gpt-4.1` Familie (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, Ausmusterung 2026-10-14) eingestellt, während die **GPT-5 Familie
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) allgemein verfügbar** ist (Ruhestand 2027-02-06). Aktualisiert:
  - `.env.copy`, `00-course-setup/03-providers.md` (empfohlene Bereitstellung und `az cognitiveservices`
    Deploy-Befehle) sowie die README-Dateien für Lektionen 04, 06, 07 und 15.
  - Python-Beispiele in Lektion 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) und Skripte in Lektion 08.
  - TypeScript / JavaScript-Beispiele in Lektionen 06, 07 und 11 sowie die `.dib` .NET Notebooks für
    Lektionen 06 und 07.
  - Zuordnungs-Notebooks in Lektionen 04, 06, 07 und 11 (Code-Zellen) sowie `shared/python/api_utils.py`
    Docstring-Beispiele.
- **Anleitung zu Reasoning-Modelparametern (neu).** `gpt-5-mini` ist ein *Reasoning*-Modell: es unterstützt **kein**
  `temperature`/`top_p` und verwendet stattdessen `max_completion_tokens` (Chat Completions) /
  `max_output_tokens` (Responses API) anstelle von `max_tokens`. Dementsprechend:
  - `temperature`/`top_p`/`max_tokens` aus allen Proben entfernt, die jetzt standardmäßig `gpt-5-mini`
    verwenden (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, Lektion 15 RAG README).
  - Einen **„Reasoning-Modelle verwenden kein `temperature`“** Hinweis zu Lektion 06 hinzugefügt, der
    erklärt, dass Reasoning-Modelle eher mit **Prompt-Engineering + Reasoning-Steuerungen** gesteuert werden
    als mit Sampling-Parametern, während `temperature`/`top_p` für nicht-Reasoning-Modelle
    (GPT-4.x, Mistral, Llama, Phi, offene Modelle) gültig bleiben.
- **`gpt-5-mini` wird im Feintuning-Tutorial (Lektion 18) nicht verwendet.** GPT-5 unterstützt nur
  verstärktes Feintuning (RFT); die Lektion 18 zum überwachtem Feintuning (SFT) behält
  `gpt-4.1-mini`, welches SFT/DPO unterstützt.
- **Temperatur-Demos verwenden ein Llama-Modell.** Um `temperature` zu lehren (was Reasoning-Modelle
  ablehnen), wird über den Foundry Models Endpunkt ein `Llama-3.3-70B-Instruct` Modell eingesetzt. Eine neue
  Umgebungsvariable `AZURE_INFERENCE_CHAT_MODEL` wurde zu `.env.copy` hinzugefügt; die Lektion 04/06 `githubmodels` Notebooks und
  das `06` `js-githubmodels` Beispiel lesen diese ein (mit Fallback auf `Llama-3.3-70B-Instruct`) und behalten ihre
  `temperature`/`top_p`/`max_tokens` Demos bei.
- **JS / .NET Beispiele auf GPT-5 aktualisiert.** `temperature`/`top_p`/`max_tokens` aus GPT-5
  Beispielen entfernt (`06` `recipe-app` TypeScript, `06` `.dib` .NET - inklusive Anhebung von `MaxOutputTokenCount`
  damit Reasoning-Ausgaben nicht abgeschnitten werden). Das `06` `js-githubmodels` Beispiel verwendet nun Llama,
  um seine Temperaturdemo zu erhalten. Die `.dib` Dateianmerkung schreibt, dass `Azure.AI.Inference` + ein Llama-Modell der Weg ist,
  `Temperature` in .NET zu demonstrieren.
- `gpt-4o-mini` / `gpt-5-mini` wurde an Stellen belassen, wo sie noch korrekt sind: `tiktoken` Token-Encoding
  Verweise, Modellkatalog-Verfügbarkeitslisten und Sprachmodelle in Lektion 02 (`gpt-4o-transcribe`).
- Lektion 20 (Mistral) und 21 (Meta) Beispiele behalten `temperature`/`max_tokens`, da sie sich auf
  Mistral/Llama-Modelle beziehen, die diese Parameter unterstützen.

## [2026-07-06] — Inhaltsmodernisierung Auffrischung

Eine umfassende Auffrischung, um das Curriculum für 2026 aktuell zu halten: moderne APIs, aktuelle Produkt- und
Modellnamen, aktualisierte Anbieterrichtlinien und neue Entwickler-Tooling-Erfahrungen.

### Hinzugefügt

- **Microsoft Agent Framework** Abschnitt in Lektion `17-ai-agents`, der einzelne Chat-Agenten,
  Tools/Funktionsaufrufe, Azure OpenAI (Microsoft Foundry) Konfiguration und Multi-Agenten-
  Workflow-Orchestrierung (`SequentialBuilder` / `ConcurrentBuilder`) abdeckt.
- **Foundry Local** als Offline- / Gerätanbieter (neben Ollama) in
  `00-course-setup/03-providers.md` und Lektion `19-slm` dokumentiert.
- **Continuous Integration Workflows**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (durchgesetzt für das gepflegte `shared/`
    Modul, Hinweis für den Rest des Curriculums), ein prüfender ESLint-Durchlauf, und ein pytest-Job.
  - `.github/workflows/security.yml` — CodeQL-Analyse (Python + JavaScript/TypeScript) und
    Abhängigkeitsprüfung bei Pull Requests.
- **Test-Suite** unter `tests/` — 41 pytest-Tests zur Abdeckung des gemeinsamen Utility-Moduls.
- **Azure OpenAI → Responses API Migrations-Leitfaden** unter
  `.github/skills/azure-openai-to-responses/` zur Unterstützung der API-Migration.

### Geändert

- **Chat Completions API → Responses API** in allen Python- und TypeScript-Chat-Beispielen
  (`client.responses.create(...)` → `response.output_text`), inklusive Lektionen 04, 06, 07, 11,
  15 und 18 sowie deren README-Dateien.
- **GitHub-Modelle → Microsoft Foundry Modelle** in allen Texten, Links und Beispielen. GitHub Modelle
  werden Ende Juli 2026 eingestellt; Beispiele zeigen jetzt auf den Modellkatalog von Microsoft Foundry und verwenden
  die Umgebungsvariablen `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` und Anbieterdokumentation** aktualisiert, um widerzuspiegeln, dass Azure OpenAI nun Teil
  von Microsoft Foundry ist, und die Standard-API-Version auf `2024-10-21` erhöht wurde.
- **TypeScript-Beispiele** (Lektionen 06, 07, 08, 11) sind vom veralteten `@azure/openai`
  Beta-SDK auf das `openai` Package migriert (Chat-Apps nutzen die Responses API; die Such-App verwendet den
  Embeddings-Client).
- **.NET-Notebooks** (`dotnet/*.dib`) standardisiert auf `Azure.AI.OpenAI` **2.1.0**: Lektionen 06 und 07
  nutzen die `ChatClient` API, Lektion 08 den `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) und
  Lektion 09 den `ImageClient` (`GenerateImage`) mit `gpt-image-1`, als Ersatz für die Legacy-
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` aus `1.0.0-beta.9`.
- **Produktname-Modernisierung**: „Azure AI Studio“ / „Azure AI Foundry“ → **Microsoft Foundry**
  (Lektionen 14, 16, 17) und „Bing“ → **Microsoft Copilot** (Lektion 12), sofern sie auf die
  aktuellen Produkte bezogen waren.
- **DevContainer** (`.devcontainer/`) enthält nun Pylance, Black, Ruff, ESLint, Prettier und Copilot
  Extensions, aktiviert Format-on-Save und installiert `ruff`, `black`, `mypy` und `pytest`, damit CI-
  Checks lokal reproduziert werden können.
- **Bildgenerierung** (Lektion 09) empfiehlt `gpt-image-1` für Azure (der Azure-Katalog hat
  `dall-e-3` fallen gelassen).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** wurde aktualisiert, um abgeschlossene Arbeiten (API-Migration, CI,
  DevContainer, Tests) und aktuelle Fakten widerzuspiegeln (Übersetzungen werden automatisch vom
  Azure Co-op Translator erzeugt; die Assistants API wurde durch die Responses API ersetzt).

### Behoben

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` gibt jetzt für rein aus Leerzeichen bestehende Eingaben einen
  leeren String zurück, anstatt einen "zu kurz"-Fehler zu werfen (konsistent mit dem
  `None`-Fall). Gefunden und durch die neue Testsuite abgedeckt.
- **Lesson 09 Bildbeispiele** — echte Fehler korrigiert: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  und eine Variable, die das `openai`-Modul überschattet hat.
- **Lesson 15 RAG-Notebook** — die Client-Einrichtung repariert, das entfallene `DataFrame.append`
  durch `pd.concat` ersetzt und die veraltete SDK-Nutzung modernisiert.
- Veraltete / eingestellte Modellnamen (`gpt-3.5-turbo`, `gpt-35-turbo`) in aktiven Beispielen durch `gpt-4o-mini`
  ersetzt; historische Fine-Tuning-Ergebnisse in Lektion 18 wurden beibehalten und kommentiert,
  statt neu geschrieben.

### Veraltet / Hinweise

- **Microsoft Foundry Models Beispiele**, die das `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) verwenden — die `githubmodels-*` und `js-githubmodels` Beispiele und die Lektionen 19, 20,
  und 21 — bleiben bei der Model Inference API, welche die Responses API **nicht** unterstützt. Diese bleiben
  bewusst bei diesem SDK.
- `AzureOpenAI()` wird dort, wo noch passend (Embeddings und Bildgenerierung), bewusst beibehalten,
  da diese Workflows nicht Teil der Responses API Migration sind.
- Referenzen auf `text-embedding-ada-002` bleiben erhalten, wenn ein vorcomputierter Embedding-Index davon abhängt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->