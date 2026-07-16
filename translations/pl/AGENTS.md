# AGENTS.md

## Przegląd projektu

To repozytorium zawiera kompleksowy program nauczania składający się z 21 lekcji uczących podstaw Generative AI oraz tworzenia aplikacji. Kurs jest przeznaczony dla początkujących i obejmuje wszystko, od podstawowych koncepcji po budowę gotowych do produkcji aplikacji.

**Kluczowe technologie:**
- Python 3.9+ z bibliotekami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js i bibliotekami: `openai` (Azure OpenAI przez endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Usługa Azure OpenAI, API OpenAI i Microsoft Foundry Models (GitHub Models zostaną wycofane pod koniec lipca 2026)
- Notatniki Jupyter do nauki interaktywnej
- Dev Containery dla spójnego środowiska developerskiego

**Struktura repozytorium:**
- 21 katalogów z lekcjami numerowanymi (00-21) zawierających README, przykłady kodu i zadania
- Wiele implementacji: Python, TypeScript i czasem przykłady .NET
- Katalog tłumaczeń z wersjami w ponad 40 językach
- Centralna konfiguracja przez plik `.env` (użyj `.env.copy` jako szablonu)

## Komendy instalacyjne

### Początkowa konfiguracja repozytorium

```bash
# Sklonuj repozytorium
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Skopiuj szablon środowiska
cp .env.copy .env
# Edytuj plik .env z twoimi kluczami API i punktami końcowymi
```

### Konfiguracja środowiska Python

```bash
# Utwórz środowisko wirtualne
python3 -m venv venv

# Aktywuj środowisko wirtualne
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Zainstaluj zależności
pip install -r requirements.txt
```

### Konfiguracja Node.js/TypeScript

```bash
# Zainstaluj zależności na poziomie root (dla narzędzi dokumentacyjnych)
npm install

# Aby uzyskać przykłady TypeScript dla poszczególnych lekcji, przejdź do konkretnej lekcji:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Konfiguracja Dev Container (zalecane)

Repozytorium zawiera konfigurację `.devcontainer` dla GitHub Codespaces lub VS Code Dev Containers:

1. Otwórz repozytorium w GitHub Codespaces lub VS Code z rozszerzeniem Dev Containers
2. Dev Container automatycznie:
   - zainstaluje zależności Pythona z `requirements.txt`
   - uruchomi skrypt post-create (`.devcontainer/post-create.sh`)
   - skonfiguruje kernel Jupyter

## Przebieg pracy developerskiej

### Zmienne środowiskowe

Wszystkie lekcje wymagające dostępu do API używają zmiennych środowiskowych zdefiniowanych w `.env`:

- `OPENAI_API_KEY` - dla API OpenAI
- `AZURE_OPENAI_API_KEY` - dla Azure OpenAI w Microsoft Foundry (Azure OpenAI Service jest teraz częścią Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - adres endpointa Azure OpenAI (endpoint zasobu Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - nazwa wdrożenia modelu do kompletów czatowych
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - nazwa wdrożenia modelu osadzającego (embeddings)
- `AZURE_OPENAI_API_VERSION` - wersja API (domyślnie: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - dla modeli Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - endpoint dla Microsoft Foundry Models (katalog modeli z wieloma dostawcami)
- `AZURE_INFERENCE_CREDENTIAL` - klucz API dla Microsoft Foundry Models (zastępuje wycofywany `GITHUB_TOKEN`)

### Uruchamianie przykładów w Pythonie

```bash
# Przejdź do katalogu lekcji
cd 06-text-generation-apps/python

# Uruchom skrypt Pythona
python aoai-app.py
```

### Uruchamianie przykładów w TypeScript

```bash
# Przejdź do katalogu aplikacji TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Zbuduj kod TypeScript
npm run build

# Uruchom aplikację
npm start
```

### Uruchamianie notatników Jupyter

```bash
# Uruchom Jupyter w katalogu głównym repozytorium
jupyter notebook

# Lub użyj VS Code z rozszerzeniem Jupyter
```

### Praca z różnymi typami lekcji

- **Lekcje „Learn”**: Skupiają się na dokumentacji README.md i koncepcjach
- **Lekcje „Build”**: Zawierają działające przykłady kodu w Pythonie i TypeScript
- Każda lekcja posiada README.md z teorią, omówieniami kodu i linkami do materiałów wideo

## Wytyczne dotyczące stylu kodu

### Python

- Używaj `python-dotenv` do zarządzania zmiennymi środowiskowymi
- Importuj bibliotekę `openai` do interakcji z API
- Używaj `pylint` do lintowania (niektóre przykłady zawierają `# pylint: disable=all` dla uproszczenia)
- Stosuj konwencje nazewnicze PEP 8
- Przechowuj dane uwierzytelniające API w pliku `.env`, nigdy bezpośrednio w kodzie

### TypeScript

- Używaj pakietu `dotenv` dla zmiennych środowiskowych
- Konfiguracja TypeScript w `tsconfig.json` dla każdej aplikacji
- Używaj pakietu `openai` dla Azure OpenAI (kieruj klienta na endpoint `/openai/v1/` i wywołuj `client.responses.create`); korzystaj z `@azure-rest/ai-inference` dla Microsoft Foundry Models
- Używaj `nodemon` podczas developingu z automatycznym przeładowaniem
- Buduj przed uruchomieniem: `npm run build` a następnie `npm start`

### Ogólne zasady

- Zachowuj proste i edukacyjne przykłady kodu
- Dodawaj komentarze wyjaśniające kluczowe koncepcje
- Kod każdej lekcji powinien być samowystarczalny i możliwy do uruchomienia
- Stosuj spójne nazewnictwo: prefiks `aoai-` dla Azure OpenAI, `oai-` dla API OpenAI, `githubmodels-` dla Microsoft Foundry Models (starszy prefiks z czasów GitHub Models)

## Wytyczne dotyczące dokumentacji

### Styl Markdown

- Wszystkie adresy URL muszą być ujęte w format `[tekst](../../url)` bez dodatkowych spacji
- Linki względne powinny zaczynać się od `./` lub `../`
- Wszystkie linki do domen Microsoft muszą zawierać ID śledzenia: `?WT.mc_id=academic-105485-koreyst`
- Nie używaj lokalizacji specyficznych dla kraju w URL (unikaj `/en-us/`)
- Obrazy przechowywane w folderze `./images` z opisowymi nazwami
- Używaj znaków angielskich, cyfr i myślników w nazwach plików

### Wsparcie tłumaczeń

- Repozytorium obsługuje ponad 40 języków za pomocą automatycznych działań GitHub Actions
- Tłumaczenia przechowywane w katalogu `translations/`
- Nie dostarczaj tłumaczeń niepełnych
- Nie są akceptowane tłumaczenia maszynowe
- Przetłumaczone obrazy przechowywane w katalogu `translated_images/`

## Testowanie i walidacja

### Kontrole przed zgłoszeniem

To repozytorium używa GitHub Actions do walidacji. Przed zgłoszeniem PR:

1. **Sprawdź linki Markdown**:
   ```bash
   # Workflow validate-markdown.yml sprawdza:
   # - Uszkodzone ścieżki względne
   # - Brakujące identyfikatory śledzenia na ścieżkach
   # - Brakujące identyfikatory śledzenia na adresach URL
   # - Adresy URL z lokalizacją kraju
   # - Uszkodzone zewnętrzne adresy URL
   ```

2. **Testy manualne**:
   - Testuj przykłady Python: aktywuj venv i uruchom skrypty
   - Testuj przykłady TypeScript: `npm install`, `npm run build`, `npm start`
   - Sprawdź poprawność konfiguracji zmiennych środowiskowych
   - Zweryfikuj działanie kluczy API z przykładami kodu

3. **Przykłady kodu**:
   - Zapewnij, że cały kod działa bez błędów
   - Testuj jednocześnie z Azure OpenAI i OpenAI API, jeśli to możliwe
   - Zweryfikuj działanie z Microsoft Foundry Models tam, gdzie obsługiwane

### Brak testów automatycznych

Jest to repozytorium edukacyjne koncentrujące się na samouczkach i przykładach. Nie ma testów jednostkowych ani integracyjnych do uruchomienia. Walidacja opiera się głównie na:
- Testach manualnych przykładów kodu
- GitHub Actions do walidacji Markdown
- Przeglądzie społeczności treści edukacyjnych

## Wytyczne dotyczące Pull Requestów

### Przed zgłoszeniem

1. Testuj zmiany kodu w Pythonie i TypeScript, jeśli dotyczy
2. Uruchom walidację Markdown (wyzwalana automatycznie na PR)
3. Upewnij się, że wszystkie linki Microsoft zawierają ID śledzenia
4. Sprawdź ważność linków względnych
5. Zweryfikuj poprawność odwołań do obrazów

### Format tytułu PR

- Używaj opisowych tytułów: `[Lesson 06] Poprawka literówki w przykładzie Python` lub `Aktualizacja README dla lekcji 08`
- Odwołuj się do numerów zgłoszeń, jeśli to możliwe: `Fixes #123`

### Opis PR

- Wyjaśnij, co zostało zmienione i dlaczego
- Dołącz linki do powiązanych zgłoszeń
- Dla zmian w kodzie podaj, które przykłady były testowane
- Dla PR z tłumaczeniami dołącz wszystkie pliki gwarantujące kompletność tłumaczenia

### Wymagania dotyczące wkładu

- Podpisz Microsoft CLA (automatycznie przy pierwszym PR)
- Zrób fork repozytorium na swoje konto przed zmianami
- Jeden PR na logiczną zmianę (nie łącz niepowiązanych poprawek)
- Staraj się, aby PR były skoncentrowane i niewielkie

## Częste procesy pracy

### Dodawanie nowego przykładu kodu

1. Przejdź do odpowiedniego katalogu lekcji
2. Utwórz przykład w podkatalogu `python/` lub `typescript/`
3. Stosuj konwencję nazewnictwa: `{provider}-{example-name}.{py|ts|js}`
4. Testuj z faktycznymi poświadczeniami API
5. Udokumentuj nowe zmienne środowiskowe w README lekcji

### Aktualizacja dokumentacji

1. Edytuj README.md w katalogu lekcji
2. Stosuj wytyczne Markdown (ID śledzenia, linki względne)
3. Aktualizacje tłumaczeń obsługiwane są przez GitHub Actions (nie edytuj ręcznie)
4. Sprawdź, czy wszystkie linki działają poprawnie

### Praca z Dev Containers

1. Repozytorium zawiera `.devcontainer/devcontainer.json`
2. Skrypt post-create automatycznie instaluje zależności Pythona
3. Rozszerzenia dla Pythona i Jupyter są wstępnie skonfigurowane
4. Środowisko bazuje na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Wdrażanie i publikacja

To repozytorium naukowe - nie ma procesu wdrażania. Program jest używany przez:

1. **GitHub Repository**: bezpośredni dostęp do kodu i dokumentacji
2. **GitHub Codespaces**: natychmiastowe środowisko dev z wstępną konfiguracją
3. **Microsoft Learn**: treści mogą być syndykowane do oficjalnej platformy edukacyjnej
4. **docsify**: witryna dokumentacji zbudowana z Markdown (patrz `docsifytopdf.js` i `package.json`)

### Budowanie witryny dokumentacji

```bash
# Wygeneruj PDF z dokumentacji (jeśli potrzebne)
npm run convert
```

## Rozwiązywanie problemów

### Częste problemy

**Błędy importu w Pythonie**:
- Upewnij się, że środowisko wirtualne jest aktywne
- Uruchom `pip install -r requirements.txt`
- Sprawdź, czy wersja Pythona to 3.9+

**Błędy budowania TypeScript**:
- Uruchom `npm install` w katalogu konkretnej aplikacji
- Sprawdź kompatybilność wersji Node.js
- Wyczyść `node_modules` i zainstaluj ponownie jeśli potrzeba

**Błędy uwierzytelnienia API**:
- Zweryfikuj istnienie pliku `.env` i poprawność wartości
- Sprawdź, czy klucze API są ważne i nie wygasły
- Upewnij się, że adresy endpointów są poprawne dla twojego regionu

**Brakujące zmienne środowiskowe**:
- Skopiuj `.env.copy` do `.env`
- Uzupełnij wszystkie wymagane wartości dla lekcji, nad którą pracujesz
- Uruchom ponownie aplikację po aktualizacji `.env`

## Dodatkowe zasoby

- [Przewodnik po konfiguracji kursu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Wytyczne dotyczące wkładu](./CONTRIBUTING.md)
- [Kodeks postępowania](./CODE_OF_CONDUCT.md)
- [Polityka bezpieczeństwa](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbiór zaawansowanych przykładów kodu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notatki specyficzne dla projektu

- To jest **repozytorium edukacyjne** skoncentrowane na nauce, a nie na kodzie produkcyjnym
- Przykłady są celowo proste i skupione na nauce koncepcji
- Jakość kodu jest wyważona względem czytelności edukacyjnej
- Każda lekcja jest samodzielna i można ją ukończyć niezależnie
- Repozytorium obsługuje wielu dostawców API: Azure OpenAI, OpenAI, Microsoft Foundry Models oraz dostawców offline takich jak Foundry Local i Ollama
- Treści są wielojęzyczne z automatycznymi procesami tłumaczeń
- Aktywna społeczność na Discordzie do pytań i wsparcia

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->