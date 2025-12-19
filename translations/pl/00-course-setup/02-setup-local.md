<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T14:51:32+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pl"
}
-->
# Lokalna konfiguracja 🖥️

**Skorzystaj z tego przewodnika, jeśli wolisz uruchamiać wszystko na własnym laptopie.**  
Masz dwie ścieżki: **(A) natywny Python + virtual-env** lub **(B) VS Code Dev Container z Dockerem**.  
Wybierz tę, która wydaje się łatwiejsza — obie prowadzą do tych samych lekcji.

## 1. Wymagania wstępne

| Narzędzie          | Wersja / Uwagi                                                                     |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (pobierz z <https://python.org>)                                           |
| **Git**            | Najnowsza (dostępna z Xcode / Git dla Windows / menedżer pakietów Linux)           |
| **VS Code**        | Opcjonalny, ale zalecany <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Tylko* dla opcji B. Darmowa instalacja: <https://docs.docker.com/desktop/>       |

> 💡 **Wskazówka** – Sprawdź narzędzia w terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Opcja A – Natywny Python (najszybszy)

### Krok 1  Sklonuj to repozytorium

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Utwórz i aktywuj środowisko wirtualne

```bash
python -m venv .venv          # utwórz jeden
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Wiersz poleceń powinien teraz zaczynać się od (.venv) — to oznacza, że jesteś w środowisku.

### Krok 3 Zainstaluj zależności

```bash
pip install -r requirements.txt
```

Przejdź do Sekcji 3 o [kluczach API](../../../00-course-setup)

## 2. Opcja B – VS Code Dev Container (Docker)

To repozytorium i kurs zostały przygotowane z użyciem [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który ma uniwersalne środowisko uruchomieniowe obsługujące Python3, .NET, Node.js i Java. Powiązana konfiguracja jest zdefiniowana w pliku `devcontainer.json` znajdującym się w folderze `.devcontainer/` w katalogu głównym tego repozytorium.

>**Dlaczego warto wybrać tę opcję?**  
>Identyczne środowisko jak w Codespaces; brak dryfu zależności.

### Krok 0 Zainstaluj dodatki

Docker Desktop – potwierdź, że działa polecenie ```docker --version```.  
Rozszerzenie VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otwórz repozytorium w VS Code

Plik ▸ Otwórz folder… → generative-ai-for-beginners

VS Code wykryje folder .devcontainer/ i wyświetli monit.

### Krok 2 Otwórz ponownie w kontenerze

Kliknij „Reopen in Container”. Docker zbuduje obraz (≈ 3 min przy pierwszym uruchomieniu).  
Gdy pojawi się wiersz poleceń, jesteś wewnątrz kontenera.

## 2. Opcja C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.  
Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie się między różnymi [**środowiskami wirtualnymi**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Przydaje się także do instalacji pakietów niedostępnych przez `pip`.

### Krok 0  Zainstaluj Minicondę

Postępuj zgodnie z [przewodnikiem instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Utwórz środowisko wirtualne

Utwórz nowy plik środowiska (*environment.yml*). Jeśli korzystasz z Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

### Krok 2  Wypełnij plik środowiska

Dodaj poniższy fragment do pliku `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### Krok 3 Utwórz środowisko Conda

Uruchom poniższe polecenia w terminalu/wierszu poleceń

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podścieżka .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

Jeśli napotkasz problemy, zajrzyj do [przewodnika po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. Opcja D – Klasyczny Jupyter / Jupyter Lab (w przeglądarce)

> **Dla kogo?**  
> Dla tych, którzy kochają klasyczny interfejs Jupyter lub chcą uruchamiać notatniki bez VS Code.

### Krok 1  Upewnij się, że Jupyter jest zainstalowany

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a adres URL do niej zostanie wyświetlony w oknie terminala.

Po wejściu na ten adres URL zobaczysz plan kursu i będziesz mógł nawigować do dowolnego pliku `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodaj swoje klucze API

Bezpieczne przechowywanie kluczy API jest ważne przy tworzeniu dowolnej aplikacji. Zalecamy, aby nie przechowywać kluczy API bezpośrednio w kodzie. Umieszczenie ich w publicznym repozytorium może prowadzić do problemów z bezpieczeństwem, a nawet niechcianych kosztów, jeśli ktoś je wykorzysta.  
Oto krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz poleceń i przejdź do katalogu głównego projektu, gdzie chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj swojego ulubionego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli korzystasz z wiersza poleceń, możesz użyć `touch` (na systemach Unix) lub `echo` (na Windows):

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj następującą linię, zastępując `your_github_token_here` swoim rzeczywistym tokenem GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, zainstaluj pakiet `python-dotenv`, który pozwala ładować zmienne środowiskowe z pliku `.env` do aplikacji Python. Możesz to zrobić za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w skrypcie Python**: W swoim skrypcie Python użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Załaduj zmienne środowiskowe z pliku .env
   load_dotenv()

   # Uzyskaj dostęp do zmiennej GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś token GitHub i załadowałeś go do aplikacji Python.

🔐 Nigdy nie commituj pliku .env — jest już w .gitignore.  
Pełne instrukcje dostawców znajdziesz w [`providers.md`](03-providers.md).

## 4. Co dalej?

| Chcę…               | Przejdź do…                                                             |
|---------------------|------------------------------------------------------------------------|
| Zacząć Lekcję 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                  |
| Poznać innych uczących się | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Rozwiązywanie problemów

| Objaw                                    | Rozwiązanie                                                      |
|------------------------------------------|-----------------------------------------------------------------|
| `python not found`                       | Dodaj Pythona do PATH lub otwórz terminal ponownie po instalacji |
| `pip` nie może zbudować kółek (Windows) | `pip install --upgrade pip setuptools wheel`, potem spróbuj ponownie |
| `ModuleNotFoundError: dotenv`            | Uruchom `pip install -r requirements.txt` (środowisko nie zostało zainstalowane) |
| Błąd budowania Dockera *No space left*   | Docker Desktop ▸ *Settings* ▸ *Resources* → zwiększ rozmiar dysku |
| VS Code ciągle prosi o ponowne otwarcie | Możesz mieć aktywne obie opcje; wybierz jedną (venv **lub** kontener) |
| Błędy OpenAI 401 / 429                   | Sprawdź wartość `OPENAI_API_KEY` / limity zapytań               |
| Błędy przy użyciu Conda                  | Zainstaluj biblioteki Microsoft AI za pomocą `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->