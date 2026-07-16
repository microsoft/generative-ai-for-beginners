# Plan funkcji rozszerzonych i usprawnień

Dokument ten przedstawia zalecane ulepszenia i usprawnienia programu Generative AI dla początkujących, oparte na kompleksowym przeglądzie kodu i analizie najlepszych praktyk branżowych.

## Streszczenie wykonawcze

Kod źródłowy został przeanalizowany pod kątem bezpieczeństwa, jakości kodu i skuteczności edukacyjnej. Dokument zawiera rekomendacje dotyczące natychmiastowych poprawek, usprawnień w krótkim terminie oraz dalszych ulepszeń.

---

## 1. Ulepszenia bezpieczeństwa (Priorytet: Krytyczny)

### 1.1 Natychmiastowe poprawki (Zrealizowane)

| Problem | Dotknięte pliki | Status |
|-------|----------------|--------|
| Twardo zakodowany SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Naprawione |
| Brak walidacji zmiennych środowiskowych | Wiele plików JS/TS | Naprawione |
| Niebezpieczne wywołania funkcji | `11-integrating-with-function-calling/js-githubmodels/app.js` | Naprawione |
| Wycieki uchwytów plików | `08-building-search-applications/scripts/` | Naprawione |
| Brak limitów czasu żądań | `09-building-image-applications/python/` | Naprawione |

### 1.2 Zalecane dodatkowe funkcje bezpieczeństwa

1. **Przykłady ograniczania częstotliwości (Rate Limiting)**
   - Dodaj przykładowy kod pokazujący, jak wdrożyć rate limiting dla wywołań API
   - Pokaż wzorce wykładniczego cofania (exponential backoff)

2. **Rotacja kluczy API**
   - Dodaj dokumentację najlepszych praktyk rotacji kluczy API
   - Zamieść przykłady użycia Azure Key Vault lub podobnych usług

3. **Integracja bezpieczeństwa treści**
   - Dodaj przykłady użycia Azure Content Safety API
   - Zaprezentuj wzorce moderacji danych wejściowych/wyjściowych

---

## 2. Ulepszenia jakości kodu

### 2.1 Dodane pliki konfiguracyjne

| Plik | Przeznaczenie |
|------|---------|
| `.eslintrc.json` | Reguły lintingu JavaScript/TypeScript |
| `.prettierrc` | Standardy formatowania kodu |
| `pyproject.toml` | Konfiguracja narzędzi Python (Black, Ruff, mypy) |

### 2.2 Utworzone wspólne narzędzia

Nowy moduł `shared/python/` zawierający:
- `env_utils.py` - Obsługa zmiennych środowiskowych
- `input_validation.py` - Walidacja i oczyszczanie danych wejściowych
- `api_utils.py` - Bezpieczne opakowania żądań API

### 2.3 Zalecane ulepszenia kodu

1. **Pokrycie adnotacjami typów**
   - Dodaj adnotacje typów do wszystkich plików Python
   - Włącz ścisły tryb TypeScript we wszystkich projektach TS

2. **Standardy dokumentacji**
   - Dodaj docstringi do wszystkich funkcji Python
   - Dodaj komentarze JSDoc do wszystkich funkcji JavaScript/TypeScript

3. **Framework testowy**
   - Dodaj konfigurację pytest i przykładowe testy _(zrealizowano: konfiguracja pytest w `pyproject.toml`; przykładowe testy narzędzi współdzielonych w [`tests/`](../../../tests) uruchamiane w CI)_
   - Dodaj konfigurację Jest dla JavaScript/TypeScript

---

## 3. Usprawnienia edukacyjne

### 3.1 Nowe tematy lekcji

1. **Bezpieczeństwo w aplikacjach AI** (Proponowana lekcja 22)
   - Ataki i obrona przed wstrzyknięciem promptów
   - Zarządzanie kluczami API
   - Moderacja treści
   - Ograniczanie częstotliwości i zapobieganie nadużyciom

2. **Wdrożenie produkcyjne** (Proponowana lekcja 23)
   - Konteneryzacja z Dockerem
   - Pipeline'y CI/CD
   - Monitorowanie i logowanie
   - Zarządzanie kosztami

3. **Zaawansowane techniki RAG** (Proponowana lekcja 24)
   - Wyszukiwanie hybrydowe (słowa kluczowe + semantyczne)
   - Strategie ponownego rankingu
   - RAG multimodalny
   - Metryki ewaluacyjne

### 3.2 Usprawnienia istniejących lekcji

| Lekcja | Zalecane ulepszenie |
|--------|------------------------|
| 06 - Generowanie tekstu | Dodaj przykłady strumieniowej odpowiedzi |
| 07 - Aplikacje czatu | Dodaj wzorce pamięci konwersacji |
| 08 - Aplikacje wyszukiwania | Dodaj porównanie baz wektorowych |
| 09 - Generowanie obrazów | Dodaj przykłady edycji/wariacji obrazów |
| 11 - Wywoływanie funkcji | Dodaj wywoływanie funkcji równoległych |
| 15 - RAG | Dodaj porównanie strategii dzielenia na porcje (chunking) |
| 17 - Agenci AI | Dodaj orkiestrację wieloagentową |

---

## 4. Modernizacja API

### 4.1 Przestarzałe wzorce API (Migracja zakończona)

Wszystkie próbki chat w Pythonie i TypeScript zostały przeniesione z API Chat Completions do **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Stary wzorzec | Nowy wzorzec | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Zakończone |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Zakończone |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | Pakiet `openai` `client.responses.create()` → `response.output_text` | Zakończone |
| `df.append()` (pandas) | `pd.concat()` | Zakończone |

> **Uwaga:** Próbki Microsoft Foundry Models używające SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) pozostają przy Model Inference API, które nie obsługuje Responses API. `AzureOpenAI()` jest celowo utrzymane tam, gdzie jest nadal ważne (embeddingi i generowanie obrazów).

### 4.2 Nowe funkcje API do demonstracji

1. **Strukturalne wyjścia** (OpenAI)
   - Tryb JSON
   - Wywoływanie funkcji ze ścisłymi schematami

2. **Możliwości wizji**
   - Analiza obrazów za pomocą GPT-4o (vision)
   - Prompt multimodalny

3. **Wbudowane narzędzia w Responses API** (zastępujące przestarzałe API Assistantów)
   - Interpretator kodu
   - Wyszukiwanie plików
   - Wyszukiwanie w sieci i narzędzia niestandardowe

---

## 5. Ulepszenia infrastruktury

### 5.1 Ulepszenia CI/CD

Wdrożone w [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/formatowanie Pythona (Ruff + Black) **egzekwowane** na utrzymywanym module narzędzi wspólnych `shared/` oraz uruchamiane **doradczo** na pozostałej części programu, plus doradczy przebieg ESLint dla JS/TS. Przykładowa baza:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Skanowanie bezpieczeństwa

Wdrożone w [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): analiza CodeQL dla Pythona oraz JS/TS (przy push, pull request i w harmonogramie tygodniowym) oraz przegląd zależności w pull requestach. Przykładowa baza:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Usprawnienia doświadczenia dewelopera

### 6.1 Ulepszenia DevContainer

Wdrożone w [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) i [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontener teraz zawiera rozszerzenia Pylance, formatera Black, Ruff, ESLint, Prettier i Copilot, włącza formatowanie przy zapisie powiązane z konfiguracją Black/Prettier repozytorium oraz instaluje narzędzia deweloperskie (`ruff`, `black`, `mypy`, `pytest`), dzięki czemu [workflow code-quality](../../../.github/workflows/code-quality.yml) może być uruchamiany lokalnie. Obraz bazowy `mcr.microsoft.com/devcontainers/universal` zawiera już Pythona i Node, więc nie są potrzebne dodatkowe funkcje. Przykładowa baza:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Interaktywny plac zabaw (playground)

Rozważ dodanie:
- Notatników Jupyter z wstępnie wypełnionymi kluczami API (poprzez zmienne środowiskowe)
- Demonstracji Gradio/Streamlit dla osób uczących się wizualnie
- Interaktywnych quizów do oceny wiedzy

---

## 7. Wsparcie wielojęzyczne

### 7.1 Obecne pokrycie językowe

| Technologia | Obsługiwane lekcje | Status |
|------------|-----------------|--------|
| Python | Wszystkie | Kompletny |
| TypeScript | 06-09, 11 | Częściowy |
| JavaScript | 06-08, 11 | Częściowy |
| .NET/C# | Niektóre | Częściowy |

### 7.2 Zalecane dodatki

1. **Go** - rosnące narzędzia AI/ML
2. **Rust** - aplikacje o wysokiej wydajności
3. **Java/Kotlin** - aplikacje korporacyjne

---

## 8. Optymalizacje wydajności

### 8.1 Optymalizacje na poziomie kodu

1. **Wzorce Async/Await**
   - Dodaj przykłady asynchronicznego przetwarzania wsadowego
   - Zademonstruj równoczesne wywołania API

2. **Strategie cache’owania**
   - Dodaj przykłady cache’owania embeddingów
   - Zademonstruj wzorce cache’owania odpowiedzi

3. **Optymalizacja tokenów**
   - Dodaj przykłady użycia tiktoken
   - Zademonstruj techniki kompresji promptów

### 8.2 Przykłady optymalizacji kosztów

Dodaj przykłady demonstrujące:
- Dobór modelu w zależności od złożoności zadania
- Projektowanie promptów pod kątem efektywności tokenów
- Przetwarzanie wsadowe dla operacji masowych

---

## 9. Dostępność i internacjonalizacja

### 9.1 Obecny status tłumaczeń

Wszystkie tłumaczenia są **kompletne** i generowane automatycznie przez [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), który produkuje i utrzymuje w synchronizacji ponad 50 wersji językowych programu względem źródła w języku angielskim. Przetłumaczone treści znajdują się pod `translations/`, a lokalizowane obrazy pod `translated_images/`; pełna lista dostępnych języków jest opublikowana na górze pliku README repozytorium.

| Aspekt | Status |
|--------|--------|
| Pokrycie tłumaczeń | Kompletne — 50+ języków, wszystkie lekcje |
| Metoda tłumaczenia | Automatyczne przez [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Synchronizacja ze źródłem angielskim | Tak — generowane automatycznie |

### 9.2 Usprawnienia dostępności

1. Dodaj teksty alternatywne do wszystkich obrazów
2. Zapewnij odpowiednie podświetlenie składni w przykładach kodu
3. Dodaj transkrypcje wideo do całych materiałów wideo
4. Zapewnij kontrast kolorów spełniający wytyczne WCAG

---

## 10. Priorytet wdrożenia

### Faza 1: Natychmiastowa (tydzień 1-2)
- [x] Napraw krytyczne problemy bezpieczeństwa
- [x] Dodaj konfigurację jakości kodu
- [x] Utwórz narzędzia wspólne
- [x] Udokumentuj wytyczne bezpieczeństwa

### Faza 2: Krótkoterminowa (tydzień 3-4)
- [x] Zaktualizuj przestarzałe wzorce API (Chat Completions → Responses API, Python + TypeScript)
- [ ] Dodaj adnotacje typów do wszystkich plików Python (zrobione dla utrzymywanego modułu `shared/`; próbki z lekcji pozostawiono proste)
- [x] Dodaj workflowy CI/CD do jakości kodu
- [x] Utwórz workflow skanowania bezpieczeństwa

### Faza 3: Średnioterminowa (miesiąc 2-3)
- [ ] Dodaj nową lekcję o bezpieczeństwie
- [ ] Dodaj lekcję o wdrożeniu produkcyjnym
- [x] Ulepsz konfigurację DevContainer
- [ ] Dodaj interaktywne demonstracje

### Faza 4: Długoterminowa (miesiąc 4+)
- [ ] Dodaj zaawansowaną lekcję RAG
- [ ] Rozszerz wsparcie językowe
- [ ] Dodaj kompletny zestaw testów
- [ ] Utwórz program certyfikacji

---

## Podsumowanie

Ten plan zapewnia ustrukturyzowane podejście do ulepszania programu Generative AI dla początkujących. Poprzez rozwiązanie kwestii bezpieczeństwa, modernizację API oraz dodanie treści edukacyjnych, kurs lepiej przygotuje studentów do tworzenia aplikacji AI w praktyce.

W przypadku pytań lub chęci wniesienia wkładu, prosimy o otwarcie zgłoszenia w repozytorium GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->