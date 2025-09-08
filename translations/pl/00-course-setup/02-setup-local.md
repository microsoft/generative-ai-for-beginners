<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:38:13+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pl"
}
-->
# Lokalna konfiguracja 🖥️

**Skorzystaj z tego przewodnika, jeśli wolisz uruchamiać wszystko na własnym laptopie.**  
Masz dwie opcje: **(A) natywny Python + virtual-env** lub **(B) Dev Container VS Code z Dockerem**.  
Wybierz, co jest dla Ciebie łatwiejsze—obie drogi prowadzą do tych samych lekcji.

## 1.  Wymagania wstępne

| Narzędzie           | Wersja / Uwagi                                                                       |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (pobierz z <https://python.org>)                                              |
| **Git**             | Najnowsza (dostępna z Xcode / Git for Windows / menedżer pakietów Linux)             |
| **VS Code**         | Opcjonalnie, ale polecane <https://code.visualstudio.com>                            |
| **Docker Desktop**  | *Tylko* dla opcji B. Darmowa instalacja: <https://docs.docker.com/desktop/>          |

> 💡 **Wskazówka** – Sprawdź narzędzia w terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opcja A – Natywny Python (najszybsza)

### Krok 1  Sklonuj to repozytorium

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Krok 2 Utwórz i aktywuj środowisko wirtualne

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Wiersz poleceń powinien teraz zaczynać się od (.venv)—to znaczy, że jesteś w środowisku.

### Krok 3 Zainstaluj zależności

```bash
pip install -r requirements.txt
```

Przejdź do sekcji 3 o [kluczach API](../../../00-course-setup)

## 2. Opcja B – Dev Container VS Code (Docker)

To repozytorium i kurs zostały przygotowane z użyciem [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który posiada uniwersalne środowisko obsługujące Python3, .NET, Node.js i Javę. Odpowiednia konfiguracja znajduje się w pliku `devcontainer.json` w folderze `.devcontainer/` w głównym katalogu repozytorium.

>**Dlaczego warto wybrać tę opcję?**
>Identyczne środowisko jak w Codespaces; brak rozjazdu zależności.

### Krok 0 Zainstaluj dodatki

Docker Desktop – sprawdź, czy ```docker --version``` działa.
Rozszerzenie VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otwórz repozytorium w VS Code

Plik ▸ Otwórz folder…  → generative-ai-for-beginners

VS Code wykryje .devcontainer/ i wyświetli odpowiedni komunikat.

### Krok 2 Otwórz ponownie w kontenerze

Kliknij „Reopen in Container”. Docker zbuduje obraz (≈ 3 min za pierwszym razem).
Gdy pojawi się wiersz poleceń, jesteś już w kontenerze.

## 2.  Opcja C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie się między różnymi [**środowiskami wirtualnymi**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i pakietami. Przydaje się także do instalowania pakietów niedostępnych przez `pip`.

### Krok 0  Zainstaluj Minicondę

Postępuj zgodnie z [instrukcją instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby ją skonfigurować.

```bash
conda --version
```

### Krok 1 Utwórz środowisko wirtualne

Utwórz nowy plik środowiska (*environment.yml*). Jeśli korzystasz z Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

### Krok 2  Uzupełnij plik środowiska

Dodaj poniższy fragment do swojego pliku `environment.yml`

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

Wykonaj poniższe polecenia w terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jeśli napotkasz problemy, zajrzyj do [przewodnika po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Opcja D – Klasyczny Jupyter / Jupyter Lab (w przeglądarce)

> **Dla kogo to jest?**  
> Dla każdego, kto lubi klasyczny interfejs Jupyter lub chce uruchamiać notatniki bez VS Code.  

### Krok 1  Upewnij się, że Jupyter jest zainstalowany

Aby uruchomić Jupyter lokalnie, otwórz terminal, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a adres URL do niej pojawi się w oknie terminala.

Po wejściu na ten adres zobaczysz spis treści kursu i będziesz mógł przejść do dowolnego pliku `*.ipynb`. Na przykład: `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodaj swoje klucze API

Bezpieczeństwo kluczy API jest bardzo ważne podczas budowania aplikacji. Zalecamy, aby nie przechowywać kluczy API bezpośrednio w kodzie. Umieszczenie ich w publicznym repozytorium może prowadzić do problemów z bezpieczeństwem, a nawet niechcianych kosztów, jeśli ktoś je wykorzysta.
Oto instrukcja krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz poleceń i przejdź do głównego katalogu projektu, gdzie chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj ulubionego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli korzystasz z wiersza poleceń, możesz użyć `touch` (na systemach Unix) lub `echo` (w Windows):

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj poniższą linię, zamieniając `your_github_token_here` na swój prawdziwy token GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, zainstaluj pakiet `python-dotenv`, aby wczytać zmienne środowiskowe z pliku `.env` do aplikacji Pythona. Możesz to zrobić przez `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Wczytaj zmienne środowiskowe w swoim skrypcie Python**: W swoim skrypcie użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To wszystko! Udało Ci się utworzyć plik `.env`, dodać token GitHub i załadować go do aplikacji Python.

🔐 Nigdy nie commituj pliku .env—jest już w .gitignore.
Pełne instrukcje dla dostawców znajdziesz w [`providers.md`](03-providers.md).

## 4. Co dalej?

| Chcę…               | Przejdź do…                                                                |
|---------------------|----------------------------------------------------------------------------|
| Zacząć lekcję 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                   |
| Poznać innych uczestników | [Dołącz do Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Rozwiązywanie problemów

| Objaw                                      | Rozwiązanie                                                      |
|--------------------------------------------|------------------------------------------------------------------|
| `python not found`                         | Dodaj Pythona do PATH lub uruchom ponownie terminal po instalacji|
| `pip` nie może zbudować wheels (Windows)   | `pip install --upgrade pip setuptools wheel` i spróbuj ponownie. |
| `ModuleNotFoundError: dotenv`              | Uruchom `pip install -r requirements.txt` (środowisko nie było zainstalowane).|
| Błąd budowania Dockera *No space left*     | Docker Desktop ▸ *Ustawienia* ▸ *Zasoby* → zwiększ rozmiar dysku.|
| VS Code ciągle pyta o ponowne otwarcie     | Możesz mieć aktywne obie opcje; wybierz jedną (venv **lub** kontener)|
| Błędy OpenAI 401 / 429                     | Sprawdź wartość `OPENAI_API_KEY` / limity zapytań.               |
| Błędy przy użyciu Conda                    | Zainstaluj biblioteki Microsoft AI przez `conda install -c microsoft azure-ai-ml`|

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było poprawne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło nadrzędne. W przypadku informacji o kluczowym znaczeniu zalecamy skorzystanie z profesjonalnych usług tłumaczeniowych. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.