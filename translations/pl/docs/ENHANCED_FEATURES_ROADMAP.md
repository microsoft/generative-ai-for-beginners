# Plan rozwoju rozszerzonych funkcji i usprawnień

Dokument ten przedstawia zalecane ulepszenia i usprawnienia dla programu nauczania Generative AI dla początkujących, oparte na kompleksowym przeglądzie kodu i analizie najlepszych praktyk branżowych.

## Streszczenie wykonawcze

Baza kodu została przeanalizowana pod kątem bezpieczeństwa, jakości kodu i skuteczności edukacyjnej. Dokument ten zawiera rekomendacje dotyczące natychmiastowych poprawek, ulepszeń krótkoterminowych i przyszłych usprawnień.

---

## 1. Ulepszenia bezpieczeństwa (Priorytet: Krytyczny)

### 1.1 Natychmiastowe poprawki (Zakończone)

| Problem | Pliki dotknięte | Status |
|---------|-----------------|--------|
| Twardo zakodowany SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Naprawiono |
| Brak walidacji środowiska | Wiele plików JS/TS | Naprawiono |
| Niebezpieczne wywołania funkcji | `11-integrating-with-function-calling/js-githubmodels/app.js` | Naprawiono |
| Wycieki uchwytów plików | `08-building-search-applications/scripts/` | Naprawiono |
| Brak timeoutów zapytań | `09-building-image-applications/python/` | Naprawiono |

### 1.2 Zalecane dodatkowe funkcje bezpieczeństwa

1. **Przykłady limitowania liczby zapytań (Rate Limiting)**
   - Dodanie przykładowego kodu pokazującego, jak wdrożyć limitowanie zapytań do API
   - Demonstracja wzorców wykładniczego cofania (exponential backoff)

2. **Rotacja kluczy API**
   - Dodanie dokumentacji najlepszych praktyk dotyczących rotacji kluczy API
   - Uwzględnienie przykładów użycia Azure Key Vault lub podobnych usług

3. **Integracja bezpieczeństwa treści**
   - Dodanie przykładów wykorzystania Azure Content Safety API
   - Demonstracja wzorców moderacji wejścia/wyjścia

---

## 2. Ulepszenia jakości kodu

### 2.1 Dodane pliki konfiguracyjne

| Plik | Cel |
|-------|-----|
| `.eslintrc.json` | Zasady lintowania JavaScript/TypeScript |
| `.prettierrc` | Standardy formatowania kodu |
| `pyproject.toml` | Konfiguracja narzędzi Pythona (Black, Ruff, mypy) |

### 2.2 Utworzone udostępnione narzędzia

Nowy moduł `shared/python/` zawiera:
- `env_utils.py` - Obsługa zmiennych środowiskowych
- `input_validation.py` - Walidacja i oczyszczanie danych wejściowych
- `api_utils.py` - Bezpieczne wrappery zapytań API

### 2.3 Zalecane ulepszenia kodu

1. **Pokrycie typami (Type Hints)**
   - Dodanie adnotacji typów do wszystkich plików Pythona
   - Włączenie ścisłego trybu TypeScript we wszystkich projektach TS

2. **Standardy dokumentacji**
   - Dodanie docstringów do wszystkich funkcji Pythona
   - Dodanie komentarzy JSDoc do wszystkich funkcji JavaScript/TypeScript

3. **Framework testowy**
   - Dodanie konfiguracji pytest i przykładowych testów
   - Dodanie konfiguracji Jest dla JavaScript/TypeScript

---

## 3. Ulepszenia edukacyjne

### 3.1 Nowe tematy lekcji

1. **Bezpieczeństwo w aplikacjach AI** (Proponowana Lekcja 22)
   - Ataki i obrona przed wstrzyknięciem podpowiedzi (prompt injection)
   - Zarządzanie kluczami API
   - Moderacja treści
   - Limitowanie zapytań i zapobieganie nadużyciom

2. **Wdrożenie produkcyjne** (Proponowana Lekcja 23)
   - Konteneryzacja za pomocą Dockera
   - Pipeline'y CI/CD
   - Monitorowanie i logowanie
   - Zarządzanie kosztami

3. **Zaawansowane techniki RAG** (Proponowana Lekcja 24)
   - Wyszukiwanie hybrydowe (słowo-klucz + semantyczne)
   - Strategie ponownego rankingowania
   - RAG wielomodalny
   - Metryki oceny

### 3.2 Ulepszenia istniejących lekcji

| Lekcja | Zalecane ulepszenie |
|--------|---------------------|
| 06 - Generowanie tekstu | Dodanie przykładów odpowiedzi strumieniowych |
| 07 - Aplikacje czatu | Dodanie wzorców pamięci konwersacji |
| 08 - Aplikacje wyszukiwania | Dodanie porównania baz wektorowych |
| 09 - Generowanie obrazów | Dodanie przykładów edycji/wariacji obrazów |
| 11 - Wywoływanie funkcji | Dodanie wywołań funkcji równoległych |
| 15 - RAG | Dodanie porównania strategii dzielenia na fragmenty |
| 17 - Agenci AI | Dodanie orkiestracji wieloagentowej |

---

## 4. Modernizacja API

### 4.1 Wzorce API do aktualizacji (przestarzałe)

| Stary wzorzec | Nowy wzorzec | Pliki dotknięte |
|---------------|--------------|----------------|
| `openai.api_type = "azure"` | klient `AzureOpenAI()` | Wiele skryptów w `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Wiele notebooków |
| `df.append()` (pandas) | `pd.concat()` | Notebook RAG |

### 4.2 Nowe funkcje API do pokazania

1. **Strukturalne wyniki** (OpenAI)
   - Tryb JSON
   - Wywoływanie funkcji ze ścisłymi schematami

2. **Zdolności wizji**
   - Analiza obrazów z GPT-4V
   - Wielomodalne podpowiedzi

3. **API Asystentów**
   - Interpreter kodu
   - Wyszukiwanie plików
   - Niestandardowe narzędzia

---

## 5. Ulepszenia infrastruktury

### 5.1 Ulepszenia CI/CD

Obecne workflow obsługują walidację markdown. Zalecane dodatki:

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

## 6. Ulepszenia doświadczenia programisty

### 6.1 Ulepszenia DevContainer

Aktualizacja `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktywne środowisko do nauki

Rozważ dodanie:
- Notatników Jupyter z wstępnie ustawionymi kluczami API (poprzez środowisko)
- Demo Gradio/Streamlit dla wizualnych uczniów
- Interaktywnych quizów do oceny wiedzy

---

## 7. Wsparcie wielojęzyczne

### 7.1 Aktualne pokrycie językowe

| Technologia | Ujęte lekcje | Status |
|-------------|--------------|--------|
| Python | Wszystkie | Pełne |
| TypeScript | 06-09, 11 | Częściowe |
| JavaScript | 06-08, 11 | Częściowe |
| .NET/C# | Niektóre | Częściowe |

### 7.2 Zalecane dodatki

1. **Go** - rosnące zastosowanie w narzędziach AI/ML
2. **Rust** - aplikacje wymagające wysokiej wydajności
3. **Java/Kotlin** - aplikacje korporacyjne

---

## 8. Optymalizacje wydajności

### 8.1 Optymalizacje na poziomie kodu

1. **Wzorce Async/Await**
   - Dodanie przykładów asynchronicznych do przetwarzania partiami
   - Demonstracja współbieżnych wywołań API

2. **Strategie cache'owania**
   - Dodanie przykładów cache'owania embeddingów
   - Demonstracja wzorców cache'owania odpowiedzi

3. **Optymalizacja tokenów**
   - Dodanie przykładów użycia tiktoken
   - Demonstracja technik kompresji promptów

### 8.2 Przykłady optymalizacji kosztów

Dodanie przykładów pokazujących:
- Dobór modelu w zależności od złożoności zadania
- Inżynierię promptów pod kątem efektywności tokenów
- Przetwarzanie partiami dla operacji hurtowych

---

## 9. Dostępność i internacjonalizacja

### 9.1 Aktualny status tłumaczeń

| Język | Status |
|--------|--------|
| Angielski | Pełne |
| Chiński (uproszczony) | Pełne |
| Japoński | Pełne |
| Koreański | Pełne |
| Hiszpański | Częściowe |
| Portugalski | Częściowe |
| Turecki | Częściowe |
| Polski | Częściowe |

### 9.2 Ulepszenia dostępności

1. Dodanie tekstu alternatywnego do wszystkich obrazów
2. Zapewnienie właściwego podświetlania składni w przykładach kodu
3. Dodanie transkryptów wideo do wszystkich materiałów wideo
4. Zapewnienie kontrastu kolorów zgodnego z wytycznymi WCAG

---

## 10. Priorytet wdrożenia

### Faza 1: Natychmiastowa (tydzień 1-2)
- [x] Naprawa krytycznych problemów bezpieczeństwa
- [x] Dodanie konfiguracji jakości kodu
- [x] Utworzenie udostępnionych narzędzi
- [x] Udokumentowanie wytycznych bezpieczeństwa

### Faza 2: Krótkoterminowa (tydzień 3-4)
- [ ] Aktualizacja przestarzałych wzorców API
- [ ] Dodanie adnotacji typów do wszystkich plików Pythona
- [ ] Dodanie workflow CI/CD dla jakości kodu
- [ ] Utworzenie workflow skanowania bezpieczeństwa

### Faza 3: Średnioterminowa (miesiące 2-3)
- [ ] Dodanie nowej lekcji bezpieczeństwa
- [ ] Dodanie lekcji wdrożenia produkcyjnego
- [ ] Ulepszenie konfiguracji DevContainer
- [ ] Dodanie interaktywnych demo

### Faza 4: Długoterminowa (miesiąc 4+)
- [ ] Dodanie zaawansowanej lekcji RAG
- [ ] Rozszerzenie pokrycia językowego
- [ ] Dodanie kompleksowego zestawu testów
- [ ] Utworzenie programu certyfikacji

---

## Podsumowanie

Ten plan rozwoju zapewnia strukturalne podejście do ulepszania programu Generative AI dla początkujących. Poprzez adresowanie kwestii bezpieczeństwa, modernizację API i dodawanie treści edukacyjnych, kurs lepiej przygotuje studentów do rzeczywistego tworzenia aplikacji AI.

W przypadku pytań lub wkładu, prosimy o otwarcie issue w repozytorium GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->