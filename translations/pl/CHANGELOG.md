# Dziennik zmian

Wszystkie znaczące zmiany w programie nauczania Generative AI for Beginners są dokumentowane w tym pliku.

Format opiera się na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Ponieważ jest to
program nauczania, a nie opakowanie oprogramowania z wersjami, wpisy są grupowane według daty.

## [2026-07-16] — Walidacja treści + zasoby graficzne lekcji 09

### Zmiany

- **Lekcja 10 (aplikacje AI low-code):** zaktualizowano dwa wycofane odnośniki `docs.microsoft.com/powerapps/...` Dataverse
  na aktualne `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (sprawdzone na żywo).
- **Lekcja 17 (agenci AI):** zmodernizowano przestarzały przykład modelu (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o oraz Llama 3.3`) oraz nazwę zastępczą wdrożenia w przykładzie Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Główny plik `README.md`:** dodano brakujący identyfikator śledzenia `?WT.mc_id=academic-105485-koreyst` do
  linku *Microsoft for Startups*.
- **Zasoby graficzne lekcji 09** zostały wygenerowane na nowo z wykorzystaniem modelu `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` oraz
  `images/startup.png` (para przed/po przykładu edycji została wygenerowana za pomocą rzeczywistego
  wywołania `client.images.edit` z generowaną maską).

### Zweryfikowano

- Przeprowadzono audyt plików README dla lekcji 01, 03, 05, 12, 14 i 16 — wszystkie aktualne (poprawne nazewnictwo i linki Microsoft Foundry);
  brak konieczności zmian.
- Przeprowadzono pełną walidację markdown we wszystkich 41 plikach markdown w repozytorium (z wyłączeniem tłumaczeń)
  względem przestarzałych ścieżek dokumentacji, lokalizacji Microsoft z `/en-us/`, przestarzałych nazw produktów/modeli,
  brakujących identyfikatorów śledzenia oraz uszkodzonych względnych linków/obrazów. Jedynym adresowalnym problemem
  była luka w identyfikatorze śledzenia *Microsoft for Startups*; wszystkie inne zgłoszenia okazały się fałszywymi alarmami (automatycznie generowane linki do tłumaczeń,
  zakomentowane miejsca zastępcze oraz zewnętrzne strukturalne adresy URL `/en/`).

## [2026-07-15] — Przepisanie lekcji 09 (Aplikacje graficzne) dla modeli GPT Image

### Zmiany

- **Przepisano lekcję 09 "Tworzenie aplikacji generujących obrazy"** wokół obecnej rodziny modeli **`gpt-image`**
  (domyślny **`gpt-image-2`**; dostępne również `gpt-image-1.5` / `gpt-image-1-mini` GA), zastępując
  poprzednią zawartość DALL·E 2/3. Kluczowe poprawki:
  - modele `gpt-image` zwracają obraz jako **base64 (`b64_json`)**, a nie URL. Zaktualizowano wszystkie przykłady do
    `base64.b64decode(...)` zamiast pobierania `url` przy pomocy `requests`.
  - Zwiększono wersję API obrazów do `2025-04-01-preview`.

  - Zastąpiono zmyśloną sekcję "temperature" (modele obrazów nie używają `temperature`) oraz
    zawartość dotyczącą wariacji obrazów tylko dla DALL·E-2 sekcją **edycji obrazu** (maska/redagowanie).
  - Zaktualizowano `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, oba
    notatniki z zadaniami (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), oraz notatnik .NET `.dib`.

### Usunięto

- Usunięto przestarzałe przykłady `python/aoai-app-variation.py` i `python/oai-app-variation.py`
  (`images.create_variation` jest tylko dla DALL·E-2 i nieobsługiwane przez `gpt-image`).
- Usunięto 4 osierocone zasoby obrazów powiązane z usuniętą sekcją porównania temperatur
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Usunięto niepotrzebną zależność `requests` z próbek Pythona i wymagań lekcji.

### Zweryfikowano

- Uruchomiono `aoai-app.py` end-to-end na wdrożonym modelu `gpt-image-1.5` i potwierdzono, że przepływ
  dekodowania/zapisywania base64 generuje plik PNG. Notatniki potwierdzono jako prawidłowy JSON.

## [2026-07-14] — Aktualizacja domyślnego modelu + wskazówki dotyczące modelu rozumowania

### Zmiany

- **Domyślny model czatu `gpt-4o-mini` → `gpt-5-mini`** w całym kursie, w działających przykładach,
  dokumentacji i konfiguracji. Zmiana ta została wymuszona statusem cyklu życia modelu: na Microsoft Foundry,
  `gpt-4o-mini` (wycofywany 2026-10-01) oraz cała rodzina `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, wycofywane 2026-10-14) są **wycofywane**, podczas gdy **rodzina GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) jest ogólnie dostępna** (wycofywana 2027-02-06). Zaktualizowano:
  - `.env.copy`, `00-course-setup/03-providers.md` (zalecane wdrożenia oraz polecenia `az cognitiveservices`
    deploy), oraz pliki README do lekcji 04, 06, 07 i 15.
  - Przykłady Pythona w lekcji 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) i skrypty lekcji 08.
  - Przykłady TypeScript / JavaScript w lekcjach 06, 07 i 11 oraz notatniki `.dib` .NET dla
    lekcji 06 i 07.
  - Notatniki z zadaniami w lekcjach 04, 06, 07 i 11 (komórki z kodem), plus przykłady docstringów `shared/python/api_utils.py`.
    

- **Wskazówki dotyczące parametrów modelu rozumowania (nowe).** `gpt-5-mini` to model *rozumowania*: nie obsługuje **  
  `temperature`/`top_p` i używa `max_completion_tokens` (uzupełnienia czatu) /  
  `max_output_tokens` (Responses API) zamiast `max_tokens`. W związku z tym:  

  - Usunięto `temperature`/`top_p`/`max_tokens` z przykładów, które teraz domyślnie używają `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lekcja 15 RAG README).
  - Dodano notatkę **"Modele rozumowania nie używają `temperature`"** do lekcji 06, wyjaśniając, że
    modele rozumowania są kierowane za pomocą **prompt engineering + kontroli rozumowania** zamiast
    pokręteł próbkowania, podczas gdy `temperature`/`top_p` pozostają ważne w modelach nierozumujących
    (GPT-4.x, Mistral, Llama, Phi, modele otwarte).
- **`gpt-5-mini` nie jest używany do tutorialu fine-tuningu (lekcja 18).** GPT-5 obsługuje tylko
  fine-tuning przez wzmocnienie (RFT); w tutorialu lekcji 18 dotyczącym fine-tuningu nadzorowanego (SFT)
  pozostawiono `gpt-4.1-mini`, które obsługuje SFT/DPO.
- **Demonstracje temperatury używają modelu Llama.** Aby kontynuować naukę `temperature` (której modele rozumujące
  odmawiają), używany jest model `Llama-3.3-70B-Instruct` za pośrednictwem end-pointu Foundry Models. Dodano nową
  zmienną `AZURE_INFERENCE_CHAT_MODEL` do `.env.copy`; notatniki `githubmodels` z lekcji 04/06 oraz
  przykładowy kod `06` `js-githubmodels` ją odczytują (z powrotem do `Llama-3.3-70B-Instruct`) i zachowują
  demonstracje `temperature`/`top_p`/`max_tokens`.
- **Przykłady JS/.NET zaktualizowane dla GPT-5.** Usunięto `temperature`/`top_p`/`max_tokens` z przykładów GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - gdzie podniesiono też `MaxOutputTokenCount`,
  aby wyjście rozumowania nie było obcinane). Przykład `06` `js-githubmodels` teraz korzysta z Llama dla
  demonstracji temperatury. W `.dib` wskazano, że `Azure.AI.Inference` + model Llama to sposób na
  pokazanie `Temperature` w .NET.
- Pozostawiono `gpt-4o-mini` / `gpt-5-mini` tam, gdzie pozostają poprawne: odniesienia do kodowania tokenów `tiktoken`,
  listy dostępności katalogu modeli oraz modele mowy lekcji 02 (`gpt-4o-transcribe`).
- Przykłady z lekcji 20 (Mistral) i 21 (Meta) zachowują `temperature`/`max_tokens`, ponieważ dotyczą
  modeli Mistral/Llama, które obsługują te parametry.

## [2026-07-06] — Odświeżenie treści i modernizacja

Szerokie odświeżenie, aby utrzymać aktualność programu nauczania na 2026 rok: nowoczesne API, aktualne nazwy produktów i
modeli, zaktualizowane wskazówki dotyczące dostawców oraz nowe narzędzia poprawiające doświadczenie programisty.

### Dodano

- Sekcja **Microsoft Agent Framework** w lekcji `17-ai-agents` obejmująca pojedynczych agentów czatu,
  narzędzia/wywoływanie funkcji, konfigurację Azure OpenAI (Microsoft Foundry) oraz orkiestrację
  wieloagentową (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** udokumentowane jako dostawca offline / na urządzeniu (obok Ollama) w
  `00-course-setup/03-providers.md` oraz lekcji `19-slm`.
- **Przepływy pracy ciągłej integracji**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (egzekwowane na utrzymywanym module `shared/`,
    narzędzia doradcze dla całego programu nauczania), kontrola ESLint oraz zadanie pytest.
  - `.github/workflows/security.yml` — analiza CodeQL (Python + JavaScript/TypeScript) oraz
    przegląd zależności przy pull requestach.
- **Zestaw testów** w `tests/` — 41 testów pytest obejmujących współdzielony moduł narzędziowy.
- **Zdolność migracji Azure OpenAI → Responses API** w
  `.github/skills/azure-openai-to-responses/` używana do prowadzenia migracji API.

### Zmieniono

- **Chat Completions API → Responses API** we wszystkich przykładach czatu w Python i TypeScript
  (`client.responses.create(...)` → `response.output_text`), w tym lekcje 04, 06, 07, 11,
  15 i 18 oraz ich pliki README.
- **GitHub Models → Microsoft Foundry Models** w całym tekście, linkach i przykładach. GitHub Models
  zostaną wycofane pod koniec lipca 2026; przykłady wskazują teraz na katalog modeli Microsoft Foundry
  i używają zmiennych środowiskowych `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Aktualizacja **`.env.copy`, `AGENTS.md` i dokumentacji dostawców**, aby odzwierciedlić, że Azure OpenAI jest teraz
  częścią Microsoft Foundry, a domyślna wersja API to `2024-10-21`.
- Przykłady w **TypeScript** (lekcje 06, 07, 08, 11) zmigrowano z przestarzałego `@azure/openai`
  beta SDK do pakietu `openai` (aplikacje czatu używają Responses API; aplikacja wyszukiwania korzysta z
  klienta embeddings).
- **Notatniki .NET** (`dotnet/*.dib`) ujednolicone na `Azure.AI.OpenAI` **2.1.0**: lekcje 06 i 07
  korzystają z API `ChatClient`, lekcja 08 używa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), oraz
  lekcja 09 korzysta z `ImageClient` (`GenerateImage`) z `gpt-image-1`, zastępując starsze
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` z `1.0.0-beta.9`.
- **Modernizacja nazw produktów**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lekcje 14, 16, 17) oraz "Bing" → **Microsoft Copilot** (lekcja 12), tam gdzie odnosiły się do
  aktualnych produktów.
- **DevContainer** (`.devcontainer/`) teraz zawiera rozszerzenia Pylance, Black, Ruff, ESLint, Prettier i Copilot,
  włącza formatowanie przy zapisie oraz instaluje `ruff`, `black`, `mypy` i `pytest`, aby umożliwić
  lokalne odtwarzanie kontroli CI.
- **Generowanie obrazów** (lekcja 09) rekomenduje `gpt-image-1` dla Azure (katalog Azure usunął
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** zaktualizowany, aby odzwierciedlić zakończone prace (migracja API, CI,
  DevContainer, testy) oraz aktualne fakty (tłumaczenia są tworzone automatycznie przez
  Azure Co-op Translator; API Asystentów zostało zastąpione przez API Responses).

### Naprawione

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` zwraca teraz
  pusty ciąg dla wejścia zawierającego same białe znaki zamiast zgłaszania błędu "za krótki"
  (zgodnie z przypadkiem `None`). Znalezione i pokryte nowym zestawem testów.
- **Przykłady obrazów z lekcji 09** — poprawiono rzeczywiste błędy: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  oraz zmienną, która zacieniała moduł `openai`.
- **Notatnik RAG z lekcji 15** — naprawiono konfigurację klienta, zastąpiono usuniętą metodę `DataFrame.append`
  funkcją `pd.concat`, a także unowocześniono użycie przestarzałego SDK.
- Przestarzałe / wycofane nazwy modeli (`gpt-3.5-turbo`, `gpt-35-turbo`) zostały zastąpione przez `gpt-4o-mini`
  w aktywnych przykładach; historyczne wyniki dostrajania z lekcji 18 zostały zachowane i opisane,
  zamiast przepisywane.

### Przestarzałe / Uwagi

- **Przykłady modeli Microsoft Foundry** używające SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — przykłady `githubmodels-*` i `js-githubmodels` oraz lekcje 19, 20,
  oraz 21 — pozostają przy Model Inference API, które **nie** obsługuje API Responses. Te przykłady
  celowo pozostawiono przy tym SDK.
- `AzureOpenAI()` jest celowo zachowane tam, gdzie jest jeszcze stosowne (tworzenie embeddingów i generowanie obrazów),
  ponieważ te przepływy pracy nie są częścią migracji do Responses API.
- Odniesienia do `text-embedding-ada-002` są zachowane tam, gdzie polega na nich wstępnie obliczony indeks embeddingów.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->