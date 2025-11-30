<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:01:11+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pl"
}
-->
# AGENTS.md

## Przegląd projektu

To repozytorium zawiera kompleksowy program nauczania składający się z 21 lekcji, uczący podstaw Generatywnej AI oraz tworzenia aplikacji. Kurs jest przeznaczony dla początkujących i obejmuje wszystko, od podstawowych pojęć po budowanie aplikacji gotowych do produkcji.

**Kluczowe technologie:**
- Python 3.9+ z bibliotekami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js i bibliotekami: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API oraz modele GitHub
- Jupyter Notebooks do interaktywnej nauki
- Dev Containers dla spójnego środowiska programistycznego

**Struktura repozytorium:**
- 21 ponumerowanych katalogów lekcji (00-21) zawierających pliki README, przykłady kodu i zadania
- Wiele implementacji: Python, TypeScript, a czasami przykłady .NET
- Katalog tłumaczeń z wersjami w ponad 40 językach
- Centralna konfiguracja za pomocą pliku `.env` (użyj `.env.copy` jako szablonu)

## Polecenia konfiguracji

### Wstępna konfiguracja repozytorium

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Konfiguracja środowiska Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Konfiguracja Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Konfiguracja Dev Container (zalecane)

Repozytorium zawiera konfigurację `.devcontainer` dla GitHub Codespaces lub Dev Containers w VS Code:

1. Otwórz repozytorium w GitHub Codespaces lub VS Code z rozszerzeniem Dev Containers
2. Dev Container automatycznie:
   - Zainstaluje zależności Pythona z `requirements.txt`
   - Uruchomi skrypt post-create (`.devcontainer/post-create.sh`)
   - Skonfiguruje kernel Jupyter

## Przebieg pracy programistycznej

### Zmienne środowiskowe

Wszystkie lekcje wymagające dostępu do API używają zmiennych środowiskowych zdefiniowanych w `.env`:

- `OPENAI_API_KEY` - Klucz API OpenAI
- `AZURE_OPENAI_API_KEY` - Klucz API Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL punktu końcowego Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nazwa wdrożenia modelu do uzupełniania czatu
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nazwa wdrożenia modelu do osadzania
- `AZURE_OPENAI_API_VERSION` - Wersja API (domyślnie: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Klucz API Hugging Face
- `GITHUB_TOKEN` - Token dla modeli GitHub

### Uruchamianie przykładów w Pythonie

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Uruchamianie przykładów w TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Uruchamianie Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Praca z różnymi typami lekcji

- **Lekcje "Learn"**: Skupiają się na dokumentacji README.md i koncepcjach
- **Lekcje "Build"**: Zawierają działające przykłady kodu w Pythonie i TypeScript
- Każda lekcja ma README.md z teorią, omówieniem kodu i linkami do materiałów wideo

## Wytyczne dotyczące stylu kodu

### Python

- Używaj `python-dotenv` do zarządzania zmiennymi środowiskowymi
- Importuj bibliotekę `openai` do interakcji z API
- Używaj `pylint` do lintowania (niektóre przykłady zawierają `# pylint: disable=all` dla uproszczenia)
- Przestrzegaj konwencji nazewnictwa PEP 8
- Przechowuj dane uwierzytelniające API w pliku `.env`, nigdy w kodzie

### TypeScript

- Używaj pakietu `dotenv` do zmiennych środowiskowych
- Konfiguracja TypeScript w `tsconfig.json` dla każdej aplikacji
- Używaj `@azure/openai` lub `@azure-rest/ai-inference` dla usług Azure
- Używaj `nodemon` do rozwoju z automatycznym przeładowaniem
- Buduj przed uruchomieniem: `npm run build`, a następnie `npm start`

### Ogólne konwencje

- Utrzymuj przykłady kodu proste i edukacyjne
- Dodawaj komentarze wyjaśniające kluczowe koncepcje
- Kod każdej lekcji powinien być samodzielny i możliwy do uruchomienia
- Używaj spójnego nazewnictwa: prefiks `aoai-` dla Azure OpenAI, `oai-` dla OpenAI API, `githubmodels-` dla modeli GitHub

## Wytyczne dotyczące dokumentacji

### Styl Markdown

- Wszystkie URL-e muszą być opakowane w format `[tekst](../../url)` bez dodatkowych spacji
- Linki względne muszą zaczynać się od `./` lub `../`
- Wszystkie linki do domen Microsoft muszą zawierać identyfikator śledzenia: `?WT.mc_id=academic-105485-koreyst`
- Unikaj lokalizacji specyficznych dla kraju w URL-ach (np. `/en-us/`)
- Obrazy przechowywane w folderze `./images` z opisowymi nazwami
- Używaj angielskich znaków, cyfr i myślników w nazwach plików

### Obsługa tłumaczeń

- Repozytorium obsługuje ponad 40 języków dzięki automatycznym akcjom GitHub
- Tłumaczenia przechowywane w katalogu `translations/`
- Nie przesyłaj częściowych tłumaczeń
- Tłumaczenia maszynowe nie są akceptowane
- Przetłumaczone obrazy przechowywane w katalogu `translated_images/`

## Testowanie i walidacja

### Kontrole przed przesłaniem

To repozytorium używa GitHub Actions do walidacji. Przed przesłaniem PR:

1. **Sprawdź linki Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Testowanie ręczne**:
   - Testuj przykłady Pythona: Aktywuj venv i uruchom skrypty
   - Testuj przykłady TypeScript: `npm install`, `npm run build`, `npm start`
   - Zweryfikuj, że zmienne środowiskowe są poprawnie skonfigurowane
   - Sprawdź, czy klucze API działają z przykładami kodu

3. **Przykłady kodu**:
   - Upewnij się, że kod działa bez błędów
   - Testuj zarówno z Azure OpenAI, jak i OpenAI API, jeśli to możliwe
   - Zweryfikuj, że przykłady działają z modelami GitHub, jeśli są obsługiwane

### Brak testów automatycznych

To jest repozytorium edukacyjne skupione na tutorialach i przykładach. Nie ma testów jednostkowych ani integracyjnych do uruchomienia. Walidacja opiera się głównie na:
- Ręcznym testowaniu przykładów kodu
- GitHub Actions do walidacji Markdown
- Przeglądzie treści edukacyjnych przez społeczność

## Wytyczne dotyczące Pull Requestów

### Przed przesłaniem

1. Testuj zmiany w kodzie zarówno w Pythonie, jak i TypeScript, jeśli to możliwe
2. Uruchom walidację Markdown (automatycznie uruchamiana przy PR)
3. Upewnij się, że identyfikatory śledzenia są obecne we wszystkich URL-ach Microsoft
4. Sprawdź, czy linki względne są poprawne
5. Zweryfikuj, czy obrazy są poprawnie odwołane

### Format tytułu PR

- Używaj opisowych tytułów: `[Lekcja 06] Poprawka literówki w przykładzie Pythona` lub `Aktualizacja README dla lekcji 08`
- Odnoś się do numerów problemów, jeśli to możliwe: `Fixes #123`

### Opis PR

- Wyjaśnij, co zostało zmienione i dlaczego
- Podaj linki do powiązanych problemów
- W przypadku zmian w kodzie określ, które przykłady zostały przetestowane
- W przypadku PR dotyczących tłumaczeń, dołącz wszystkie pliki dla kompletnego tłumaczenia

### Wymagania dotyczące wkładu

- Podpisz Microsoft CLA (automatycznie przy pierwszym PR)
- Sforkuj repozytorium na swoje konto przed wprowadzeniem zmian
- Jeden PR na jedną logiczną zmianę (nie łącz niepowiązanych poprawek)
- Utrzymuj PR-y skoncentrowane i małe, jeśli to możliwe

## Typowe przepływy pracy

### Dodawanie nowego przykładu kodu

1. Przejdź do odpowiedniego katalogu lekcji
2. Utwórz przykład w podkatalogu `python/` lub `typescript/`
3. Przestrzegaj konwencji nazewnictwa: `{provider}-{example-name}.{py|ts|js}`
4. Testuj z rzeczywistymi danymi uwierzytelniającymi API
5. Udokumentuj nowe zmienne środowiskowe w README lekcji

### Aktualizacja dokumentacji

1. Edytuj README.md w katalogu lekcji
2. Przestrzegaj wytycznych Markdown (identyfikatory śledzenia, linki względne)
3. Aktualizacje tłumaczeń są obsługiwane przez GitHub Actions (nie edytuj ręcznie)
4. Testuj, czy wszystkie linki są poprawne

### Praca z Dev Containers

1. Repozytorium zawiera `.devcontainer/devcontainer.json`
2. Skrypt post-create automatycznie instaluje zależności Pythona
3. Rozszerzenia dla Pythona i Jupyter są wstępnie skonfigurowane
4. Środowisko bazuje na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Wdrażanie i publikowanie

To jest repozytorium edukacyjne - nie ma procesu wdrażania. Program nauczania jest wykorzystywany przez:

1. **Repozytorium GitHub**: Bezpośredni dostęp do kodu i dokumentacji
2. **GitHub Codespaces**: Natychmiastowe środowisko programistyczne z wstępnie skonfigurowanym setupem
3. **Microsoft Learn**: Treści mogą być syndykowane na oficjalnej platformie edukacyjnej
4. **docsify**: Strona dokumentacji zbudowana z Markdown (zobacz `docsifytopdf.js` i `package.json`)

### Budowanie strony dokumentacji

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Rozwiązywanie problemów

### Typowe problemy

**Błędy importu w Pythonie**:
- Upewnij się, że wirtualne środowisko jest aktywowane
- Uruchom `pip install -r requirements.txt`
- Sprawdź, czy wersja Pythona to 3.9+

**Błędy budowania TypeScript**:
- Uruchom `npm install` w odpowiednim katalogu aplikacji
- Sprawdź, czy wersja Node.js jest kompatybilna
- Wyczyść `node_modules` i zainstaluj ponownie, jeśli to konieczne

**Błędy uwierzytelniania API**:
- Zweryfikuj, czy plik `.env` istnieje i zawiera poprawne wartości
- Sprawdź, czy klucze API są ważne i nie wygasły
- Upewnij się, że URL-e punktów końcowych są poprawne dla Twojego regionu

**Brak zmiennych środowiskowych**:
- Skopiuj `.env.copy` do `.env`
- Wypełnij wszystkie wymagane wartości dla lekcji, nad którą pracujesz
- Uruchom aplikację ponownie po zaktualizowaniu `.env`

## Dodatkowe zasoby

- [Przewodnik konfiguracji kursu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Wytyczne dotyczące wkładu](./CONTRIBUTING.md)
- [Kodeks postępowania](./CODE_OF_CONDUCT.md)
- [Polityka bezpieczeństwa](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbiór zaawansowanych przykładów kodu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Uwagi dotyczące projektu

- To jest **repozytorium edukacyjne** skupione na nauce, a nie kodzie produkcyjnym
- Przykłady są celowo proste i skoncentrowane na nauczaniu koncepcji
- Jakość kodu jest zrównoważona z przejrzystością edukacyjną
- Każda lekcja jest samodzielna i może być ukończona niezależnie
- Repozytorium obsługuje wielu dostawców API: Azure OpenAI, OpenAI i modele GitHub
- Treści są wielojęzyczne z automatycznymi przepływami tłumaczeń
- Aktywna społeczność na Discordzie do pytań i wsparcia

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.