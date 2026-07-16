# Změny

Veškeré významné změny v kurzu Generativní AI pro začátečníky jsou zdokumentovány v tomto souboru.

Formát je založen na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Protože se jedná o
výukový kurz místo verzovaného softwarového balíčku, jsou záznamy seskupeny podle data.

## [2026-07-06] — Obnova modernizace obsahu

Široká obnova pro udržení přesnosti kurikula pro rok 2026: moderní API, aktuální názvy produktů a
modelů, aktualizované pokyny poskytovatelů a nové nástroje pro vývojářskou zkušenost.

### Přidáno

- Sekce **Microsoft Agent Framework** v lekci `17-ai-agents` pokrývající jednotlivé chatové agenty,
  nástroje/volání funkcí, konfiguraci Azure OpenAI (Microsoft Foundry) a orchestraci víceagentních
  pracovních postupů (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** zdokumentováno jako offline / na zařízení poskytovatel (vedle Ollama) v
  `00-course-setup/03-providers.md` a lekci `19-slm`.
- **Pracovní toky kontinuální integrace**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (vynucováno na udržovaném modulu `shared/`
    , poradní kontrola v celém kurikulu), poradní průchod ESLint a práce pytest.
  - `.github/workflows/security.yml` — analýza CodeQL (Python + JavaScript/TypeScript) a
    kontrola závislostí při pull requestech.
- **Testovací sada** v `tests/` — 41 testů pytest pokrývajících sdílený užitkový modul.
- **Dovednost migrace Azure OpenAI → Responses API** v
  `.github/skills/azure-openai-to-responses/` používaná k vedení migrace API.

### Změněno

- **Chat Completions API → Responses API** ve všech ukázkách chatu v Pythonu a TypeScriptu
  (`client.responses.create(...)` → `response.output_text`), včetně lekcí 04, 06, 07, 11,
  15 a 18, plus jejich README.
- **GitHub Models → Microsoft Foundry Models** v celém textu, odkazech a ukázkách. GitHub Models
  končí na konci července 2026; ukázky nyní odkazují na katalog modelů Microsoft Foundry a používají
  proměnné prostředí `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Aktualizace **`.env.copy`, `AGENTS.md` a dokumentace poskytovatelů** odpovídající tomu, že Azure OpenAI je nyní součástí
  Microsoft Foundry a výchozí verze API byla zvýšena na `2024-10-21`.
- **TypeScript ukázky** (lekce 06, 07, 08, 11) převedeny z zastaralého beta SDK `@azure/openai`
  na balíček `openai` (chat aplikace používají Responses API; vyhledávací aplikace používá
  klient embeddings).
- **.NET notebooky** (`dotnet/*.dib`) standardizovány na `Azure.AI.OpenAI` **2.1.0**: lekce 06 a 07
  používají API `ChatClient`, lekce 08 používá `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) a
  lekce 09 používá `ImageClient` (`GenerateImage`) s `gpt-image-1`, nahrazující zastaralé
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` ze `1.0.0-beta.9`.
- Modernizace názvů produktů: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekce 14, 16, 17) a "Bing" → **Microsoft Copilot** (lekce 12), pokud se odkazují na
  aktuální produkty.
- **DevContainer** (`.devcontainer/`) nyní obsahuje Pylance, Black, Ruff, ESLint, Prettier a Copilot
  rozšíření, povoluje formátování při uložení a instaluje `ruff`, `black`, `mypy` a `pytest`, aby bylo možné
  kontrolu CI replikovat lokálně.
- **Generování obrázků** (lekce 09) doporučuje `gpt-image-1` pro Azure (Azure katalog již
  nepodporuje `dall-e-3`).
- Aktualizace **`docs/ENHANCED_FEATURES_ROADMAP.md`** odpovídající dokončené práci (migrace API, CI,
  DevContainer, testy) a aktuálním skutečnostem (překlady jsou generovány automaticky pomocí
  Azure Co-op Translator; Assistants API je nahrazeno Responses API).

### Opraveno

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` nyní vrací
  prázdný řetězec pro vstupy pouze s bílými znaky namísto vyvolání chyby "příliš krátký" (v souladu s
  případem `None`). Bylo nalezeno a pokryto novou testovací sadou.
- Ukázky obrázků v lekci 09 — opraveny skutečné chyby: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  a proměnná, která stínila modul `openai`.
- Notebook RAG v lekci 15 — opraveno nastavení klienta, nahrazeno odstraněné `DataFrame.append`
  za `pd.concat` a modernizováno používání staršího SDK.
- Zastaralé / ukončené názvy modelů (`gpt-3.5-turbo`, `gpt-35-turbo`) nahrazeny `gpt-4o-mini`
  v aktivních ukázkách; historické výsledky ladění v lekci 18 byly zachovány a okomentovány
  místo přepisování.

### Zastaralé / Poznámky

- Ukázky Microsoft Foundry Models používající `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — ukázky `githubmodels-*` a `js-githubmodels` a lekce 19, 20
  a 21 — zůstávají na Model Inference API, které **nepodporuje** Responses API. Tyto zůstávají
  záměrně na tomto SDK.
- `AzureOpenAI()` je záměrně ponecháno tam, kde je stále vhodné (embeddings a generování obrázků),
  protože tyto pracovní postupy nejsou součástí migrace na Responses API.
- Odkazy na `text-embedding-ada-002` jsou ponechány tam, kde na ně závisí předpočítaný embedding index.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->