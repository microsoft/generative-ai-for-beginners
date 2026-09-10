# AGENTS.md

## Przegląd Projektu

To repozytorium zawiera kompleksowy program nauczania składający się z 21 lekcji, uczących podstaw Generatywnej Sztucznej Inteligencji oraz tworzenia aplikacji. Kurs jest przeznaczony dla początkujących i obejmuje wszystko, od podstawowych pojęć po budowanie aplikacji gotowych do produkcji.

**Kluczowe Technologie:**
- Python 3.9+ z bibliotekami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js i bibliotekami: `openai` (Azure OpenAI przez endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, oraz Microsoft Foundry Models (GitHub Models będą wycofywane do końca lipca 2026)
- Jupyter Notebooks do interaktywnej nauki
- Dev Containers dla spójnego środowiska deweloperskiego

**Struktura Repozytorium:**
- 21 numerowanych katalogów lekcji (00-21) zawierających README, przykłady kodu i zadania
- Wielokrotne implementacje: przykłady w Python, TypeScript, a czasem .NET
- Katalog tłumaczeń z ponad 40 wersjami językowymi
- Centralna konfiguracja za pomocą pliku `.env` (użyj `.env.copy` jako szablon)

## Komendy Konfiguracyjne

### Początkowa konfiguracja repozytorium

```bash
# Sklonuj repozytorium
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Skopiuj szablon środowiska
cp .env.copy .env
# Edytuj plik .env, wpisując klucze API i punkty końcowe
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
# Zainstaluj zależności na poziomie root (do narzędzi dokumentacyjnych)
npm install

# Aby przejść do przykładów TypeScript z pojedynczych lekcji, przejdź do konkretnej lekcji:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Konfiguracja Dev Container (zalecane)

Repozytorium zawiera konfigurację `.devcontainer` dla GitHub Codespaces lub VS Code Dev Containers:

1. Otwórz repozytorium w GitHub Codespaces lub VS Code z rozszerzeniem Dev Containers
2. Dev Container automatycznie:
   - Instaluje zależności Pythona z `requirements.txt`
   - Uruchamia skrypt post-create (`.devcontainer/post-create.sh`)
   - Konfiguruje kernel Jupyter

## Przebieg Rozwoju

### Zmienne środowiskowe

Wszystkie lekcje wymagające dostępu do API używają zmiennych środowiskowych zdefiniowanych w `.env`:

- `OPENAI_API_KEY` - Dla OpenAI API
- `AZURE_OPENAI_API_KEY` - Dla Azure OpenAI w Microsoft Foundry (Azure OpenAI Service jest teraz częścią Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI (endpoint zasobu Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nazwa deploymentu modelu do chat completions (domyślnie kursu: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nazwa deploymentu modelu embeddings (domyślnie kursu: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Wersja API (domyślnie: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Dla modeli Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint modeli Microsoft Foundry (katalog modeli wielodostawcy)
- `AZURE_INFERENCE_CREDENTIAL` - Klucz API modeli Microsoft Foundry (zastępuje wycofywany `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Model bez zdolności rozumowania (np. `Llama-3.3-70B-Instruct`) używany w przykładach z `temperature`, ponieważ modele rozumujące nie obsługują sterowania samplingiem

### Konwencje dotyczące modeli (ważne)

- **Domyślny model chat to `gpt-5-mini`** - aktualny, nieprzestarzały model **rozumujący**. Od 2026 starsze modele "mini" z obsługą temperatury (`gpt-4o-mini`, `gpt-4.1-mini`) są *wycofywane*, więc program standaryzuje rodzinę GPT-5.
- **Modele rozumujące odrzucają `temperature` i `top_p`**, i używają `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) zamiast `max_tokens`. **Nie dodawaj** `temperature`/`top_p`/`max_tokens` do przykładów wywołujących `gpt-5-mini`.
- **Aby pokazać `temperature`**, przykłady używają modelu **Llama** (`Llama-3.3-70B-Instruct`) poprzez endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Steruj modelami rozumującymi inżynierią promptów i kontrolą rozumowania zamiast pokręteł do samplicingu.
- **Dostrajanie (lekcja 18)** zachowuje `gpt-4.1-mini`: GPT-5 wspiera tylko fine-tuning z wzmocnieniem (RFT), a nie nadzorowany fine-tuning (SFT) pokazany tam.
- Lekcje 20 (Mistral) i 21 (Meta) zachowują `temperature`/`max_tokens`, ponieważ są skierowane do modeli Mistral/Llama, które je obsługują.

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

### Uruchamianie notebooków Jupyter

```bash
# Uruchom Jupyter w głównym katalogu repozytorium
jupyter notebook

# Lub użyj VS Code z rozszerzeniem Jupyter
```

### Praca z różnymi typami lekcji

- **Lekcje "Learn"**: Skupiają się na dokumentacji README.md i koncepcjach
- **Lekcje "Build"**: Zawierają działające przykłady kodu w Pythonie i TypeScript
- Każda lekcja ma README.md z teorią, omówieniem kodu i linkami do materiałów wideo

## Wytyczne Stylu Kodowania

### Python

- Używaj `python-dotenv` do zarządzania zmiennymi środowiskowymi
- Importuj bibliotekę `openai` do interakcji z API
- Używaj `pylint` do lintingu (w niektórych przykładach jest `# pylint: disable=all` dla prostoty)
- Stosuj konwencje nazewnictwa PEP 8
- Przechowuj dane uwierzytelniające API w pliku `.env`, nigdy w kodzie

### TypeScript

- Używaj pakietu `dotenv` do zmiennych środowiskowych
- Konfiguracja TypeScript w `tsconfig.json` dla każdej aplikacji
- Używaj pakietu `openai` dla Azure OpenAI (skieruj klienta na endpoint `/openai/v1/` i wywołuj `client.responses.create`); używaj `@azure-rest/ai-inference` dla Microsoft Foundry Models
- Używaj `nodemon` do dewelopmentu z automatycznym przeładowaniem
- Kompiluj przed uruchomieniem: `npm run build` a potem `npm start`

### Ogólne Konwencje

- Utrzymuj przykłady kodu proste i edukacyjne
- Dodawaj komentarze wyjaśniające kluczowe koncepcje
- Kod każdej lekcji powinien być samodzielny i możliwy do uruchomienia
- Stosuj spójne nazewnictwo: prefix `aoai-` dla Azure OpenAI, `oai-` dla OpenAI API, `githubmodels-` dla Microsoft Foundry Models (dziedziczny prefix z epoki GitHub Models)

## Wytyczne Dokumentacyjne

### Styl Markdown

- Wszystkie URL-e muszą być w formacie `[tekst](../../url)` bez dodatkowych spacji
- Linki względne muszą zaczynać się od `./` lub `../`
- Wszystkie linki do domen Microsoft muszą zawierać identyfikator śledzenia: `?WT.mc_id=academic-105485-koreyst`
- Nie używaj lokalizacji specyficznych dla kraju w URL-ach (unikaj `/en-us/`)
- Obrazy przechowuj w folderze `./images` z opisowymi nazwami
- Używaj znaków angielskich, cyfr i myślników w nazwach plików

### Wsparcie tłumaczeń

- Repozytorium wspiera 40+ języków przez automatyczne GitHub Actions
- Tłumaczenia przechowywane w katalogu `translations/`
- Nie wysyłaj tłumaczeń częściowych
- Tłumaczenia maszynowe nie są akceptowane
- Przetłumaczone obrazy przechowywane w katalogu `translated_images/`

## Testowanie i Walidacja

### Sprawdzenia przed wysłaniem

To repozytorium używa GitHub Actions do walidacji. Przed wysłaniem PR:

1. **Sprawdź linki Markdown**:
   ```bash
   # Praca validate-markdown.yml sprawdza:
   # - Uszkodzone ścieżki względne
   # - Brakujące identyfikatory śledzenia na ścieżkach
   # - Brakujące identyfikatory śledzenia na adresach URL
   # - Adresy URL z lokalizacją kraju
   # - Uszkodzone zewnętrzne adresy URL
   ```

2. **Testy manualne**:
   - Testuj przykłady Python: Aktywuj venv i uruchom skrypty
   - Testuj przykłady TypeScript: `npm install`, `npm run build`, `npm start`
   - Sprawdź, czy zmienne środowiskowe są poprawnie skonfigurowane
   - Sprawdź, czy klucze API działają z przykładami kodu

3. **Przykłady kodu**:
   - Upewnij się, że cały kod działa bez błędów
   - Testuj zarówno z Azure OpenAI jak i OpenAI API, w razie potrzeby
   - Sprawdź, czy przykłady działają z Microsoft Foundry Models tam gdzie są wspierane

### Brak automatycznych testów

To repozytorium edukacyjne koncentruje się na tutorialach i przykładach. Nie ma testów jednostkowych ani integracyjnych do uruchomienia. Walidacja to głównie:
- Manualne testowanie przykładów kodu
- GitHub Actions do walidacji Markdown
- Recenzje społeczności wartości edukacyjnej

## Wytyczne dla Pull Requestów

### Przed wysłaniem

1. Testuj zmiany w kodzie zarówno w Python jak i TypeScript tam gdzie to możliwe
2. Uruchom walidację Markdown (uruchamiana automatycznie przy PR)
3. Upewnij się, że wszystkie linki Microsoft zawierają ID śledzenia
4. Sprawdź, czy linki względne są poprawne
5. Zweryfikuj prawidłowe odniesienia do obrazów

### Format nagłówka PR

- Używaj opisowych tytułów: `[Lekcja 06] Poprawka literówki w przykładzie Python` albo `Aktualizacja README dla lekcji 08`
- Podawaj numery zgłoszeń jeśli dotyczy: `Naprawia #123`

### Opis PR

- Wyjaśnij co zostało zmienione i dlaczego
- Podaj linki do powiązanych zgłoszeń
- Dla zmian kodu podaj, które przykłady zostały przetestowane
- Dla PR tłumaczeniowych załącz wszystkie pliki dla kompletnego tłumaczenia

### Wymagania dotyczące wkładu

- Podpisz Microsoft CLA (automatycznie przy pierwszym PR)
- Rozgałęź repozytorium na swoje konto przed wprowadzaniem zmian
- Jeden PR na logiczną zmianę (nie łącz niepowiązanych poprawek)
- Staraj się, aby PR-y były skupione i małe

## Typowe Przepływy Pracy

### Dodawanie nowego przykładu kodu

1. Przejdź do odpowiedniego katalogu lekcji
2. Utwórz przykład w podkatalogu `python/` lub `typescript/`
3. Stosuj konwencję nazewnictwa: `{provider}-{example-name}.{py|ts|js}`
4. Testuj z użyciem faktycznych danych API
5. Udokumentuj nowe zmienne środowiskowe w README lekcji

### Aktualizacja dokumentacji

1. Edytuj README.md w katalogu lekcji
2. Stosuj wytyczne Markdown (ID śledzenia, linki względne)
3. Aktualizacje tłumaczeń są obsługiwane przez GitHub Actions (nie edytuj ręcznie)
4. Sprawdź, czy wszystkie linki działają

### Praca z Dev Containers

1. Repozytorium zawiera `.devcontainer/devcontainer.json`
2. Skrypt post-create automatycznie instaluje zależności Pythona
3. Rozszerzenia dla Pythona i Jupyter są wstępnie skonfigurowane
4. Środowisko opiera się na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Wdrażanie i Publikacja

To repozytorium edukacyjne - nie ma procesu wdrożeniowego. Materiał jest konsumpowany przez:

1. **Repozytorium GitHub**: Bezpośredni dostęp do kodu i dokumentacji
2. **GitHub Codespaces**: Natychmiastowe środowisko deweloperskie z pre-konfiguracją
3. **Microsoft Learn**: Treści mogą być dystrybuowane na oficjalnej platformie edukacyjnej
4. **docsify**: Strona dokumentacji budowana z Markdown (zobacz `docsifytopdf.js` i `package.json`)

### Budowanie strony dokumentacji

```bash
# Wygeneruj PDF z dokumentacji (jeśli potrzebne)
npm run convert
```

## Rozwiązywanie problemów

### Typowe problemy

**Błędy importu w Pythonie**:
- Upewnij się, że środowisko wirtualne jest aktywowane
- Uruchom `pip install -r requirements.txt`
- Sprawdź wersję Pythona, musi być 3.9 lub wyżej

**Błędy kompilacji TypeScript**:
- Uruchom `npm install` w katalogu danej aplikacji
- Sprawdź, czy wersja Node.js jest kompatybilna
- Wyczyść katalog `node_modules` i zainstaluj ponownie, jeśli trzeba

**Błędy uwierzytelniania API**:
- Zweryfikuj, czy plik `.env` istnieje i zawiera poprawne wartości
- Sprawdź, czy klucze API są ważne i nie wygasły
- Upewnij się, że URL endpointów są poprawne dla Twojego regionu

**Brakujące zmienne środowiskowe**:
- Skopiuj `.env.copy` do `.env`
- Wypełnij wszystkie wymagane wartości dla lekcji, nad którą pracujesz
- Zrestartuj aplikację po aktualizacji `.env`

## Dodatkowe Zasoby

- [Przewodnik konfiguracji kursu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Wytyczne dotyczące wkładu](./CONTRIBUTING.md)
- [Kodeks postępowania](./CODE_OF_CONDUCT.md)
- [Polityka bezpieczeństwa](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbiór Zaawansowanych Przykładów Kodów](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notatki Specyficzne dla Projektu

- To jest **repozytorium edukacyjne** skupiające się na nauce, nie na kodzie produkcyjnym
- Przykłady są celowo proste i skupione na nauczaniu koncepcji
- Jakość kodu jest zbalansowana z klarownością edukacyjną
- Każda lekcja jest samodzielna i może być ukończona niezależnie
- Repozytorium wspiera wielu dostawców API: Azure OpenAI, OpenAI, Microsoft Foundry Models oraz dostawców offline jak Foundry Local i Ollama
- Treści są wielojęzyczne z automatycznymi workflow tłumaczeń
- Aktywna społeczność na Discordzie do pytań i wsparcia

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->