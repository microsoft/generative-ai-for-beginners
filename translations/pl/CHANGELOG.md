# Dziennik zmian

Wszystkie istotne zmiany w programie nauczania Generative AI dla początkujących są udokumentowane w tym pliku.

Format opiera się na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Ponieważ jest to
program nauczania, a nie wersjonowany pakiet oprogramowania, wpisy są pogrupowane według daty.

## [2026-07-06] — Odświeżenie modernizacji treści

Szerokie odświeżenie, aby program nauczania był dokładny dla 2026 roku: nowoczesne API, obecne nazwy produktów i
modeli, zaktualizowane wskazówki dotyczące dostawców oraz nowe narzędzia poprawiające doświadczenie programistów.

### Dodano

- Sekcja **Microsoft Agent Framework** w lekcji `17-ai-agents` obejmująca pojedynczych agentów czatu,
  wywoływanie narzędzi/funkcji, konfigurację Azure OpenAI (Microsoft Foundry) oraz orkiestrację przepływów pracy z wieloma agentami
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** udokumentowane jako dostawca offline / lokalny (obok Ollama) w
  `00-course-setup/03-providers.md` oraz lekcji `19-slm`.
- **Przepływy pracy ciągłej integracji (CI)**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (egzekwowane w utrzymywanym module `shared/`,
    zalecenia w pozostałej części programu nauczania), dodatkowo ESLint i zadanie pytest.
  - `.github/workflows/security.yml` — analiza CodeQL (Python + JavaScript/TypeScript) oraz
    przegląd zależności dla pull requestów.
- **Zestaw testów** w `tests/` — 41 testów pytest obejmujących wspólny moduł narzędziowy.
- **Umiejętność migracji Azure OpenAI → Responses API** w
  `.github/skills/azure-openai-to-responses/` służąca do prowadzenia migracji API.

### Zmieniono

- **Chat Completions API → Responses API** we wszystkich przykładach czatu w Pythonie i TypeScript
  (`client.responses.create(...)` → `response.output_text`), w tym lekcje 04, 06, 07, 11,
  15 i 18, oraz ich pliki README.
- **GitHub Models → Microsoft Foundry Models** w całym tekście, linkach i przykładach. GitHub Models
  zostają wycofane pod koniec lipca 2026; przykłady teraz wskazują na katalog modeli Microsoft Foundry i
  korzystają ze zmiennych środowiskowych `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` i dokumentacja dostawców** zaktualizowane, aby odzwierciedlić, że Azure OpenAI jest teraz częścią
  Microsoft Foundry, a domyślna wersja API podniesiona do `2024-10-21`.
- **Przykłady w TypeScript** (lekcje 06, 07, 08, 11) przeniesione z przestarzałego beta SDK `@azure/openai`
  do pakietu `openai` (aplikacje czatu używają Responses API; aplikacja wyszukująca używa klienta
  embeddings).
- **Notatniki .NET** (`dotnet/*.dib`) ustandaryzowane na `Azure.AI.OpenAI` **2.1.0**: lekcje 06 i 07
  korzystają z API `ChatClient`, lekcja 08 używa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), a
  lekcja 09 korzysta z `ImageClient` (`GenerateImage`) z `gpt-image-1`, zastępując starsze
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` z wersji `1.0.0-beta.9`.
- **Modernizacja nazw produktów**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcje 14, 16, 17) oraz "Bing" → **Microsoft Copilot** (lekcja 12), tam gdzie odnosiły się do
  aktualnych produktów.
- **DevContainer** (`.devcontainer/`) teraz zawiera rozszerzenia Pylance, Black, Ruff, ESLint, Prettier i Copilot,
  włącza formatowanie przy zapisie i instaluje `ruff`, `black`, `mypy` i `pytest`, aby kontrole CI
  mogły być odtworzone lokalnie.
- **Generowanie obrazów** (lekcja 09) rekomenduje `gpt-image-1` dla Azure (katalog Azure usunął
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** zaktualizowano, aby odzwierciedlić ukończone prace (migracja API, CI,
  DevContainer, testy) oraz aktualne fakty (tłumaczenia są generowane automatycznie przez
  Azure Co-op Translator; API Asystentów zostało zastąpione przez Responses API).

### Poprawiono

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` teraz zwraca
  pusty łańcuch dla wejścia zawierającego tylko spacje, zamiast zgłaszać błąd „za krótki” (zgodnie z
  przypadkiem `None`). Znalezione i objęte nowym zestawem testów.
- **Przykłady obrazów w lekcji 09** — poprawione prawdziwe błędy: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  oraz zmienna, która zasłaniała moduł `openai`.
- **Notatnik RAG z lekcji 15** — naprawiono konfigurację klienta, zastąpiono usuniętą metodę `DataFrame.append`
  funkcją `pd.concat` oraz unowocześniono przestarzałe użycie SDK.
- Nazwy modeli przestarzałych / wycofanych (`gpt-3.5-turbo`, `gpt-35-turbo`) zastąpione `gpt-4o-mini`
  w aktywnych przykładach; historyczne wyniki fine-tuningu w lekcji 18 zachowano i oznaczono
  zamiast przepisywać.

### Przestarzałe / Uwagi

- Przykłady modeli Microsoft Foundry, które używają SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — przykłady `githubmodels-*` i `js-githubmodels` oraz lekcje 19, 20,
  i 21 — pozostają przy Model Inference API, które **nie** obsługuje Responses API. Te przykłady
  celowo pozostają na tym SDK.
- `AzureOpenAI()` jest celowo zachowane tam, gdzie nadal jest odpowiednie (embeddingi i generowanie obrazów),
  ponieważ te przepływy pracy nie są częścią migracji Responses API.
- Odniesienia do `text-embedding-ada-002` są utrzymane tam, gdzie zależy od nich preobliczony indeks embeddingów.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->