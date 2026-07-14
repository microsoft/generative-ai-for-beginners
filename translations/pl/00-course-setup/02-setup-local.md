# Lokalne środowisko 🖥️

**Użyj tego przewodnika, jeśli wolisz uruchomić wszystko na własnym laptopie.**   
Masz dwie opcje: **(A) natywne Python + virtual-env** lub **(B) VS Code Dev Container z Dockerem**.  
Wybierz tę, która wydaje się łatwiejsza — obie prowadzą do tych samych lekcji.

## 1. Wymagania wstępne

| Narzędzie           | Wersja / Uwagi                                                                     |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (pobierz z <https://python.org>)                                          |
| **Git**            | Najnowsza (dostępna z Xcode / Git na Windows / menedżer pakietów Linux)           |
| **VS Code**        | Opcjonalny, ale zalecany <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Tylko* dla opcji B. Bezpłatna instalacja: <https://docs.docker.com/desktop/>     |

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

✅ Wiersz poleceń powinien teraz zaczynać się od (.venv)—oznacza to, że jesteś w środowisku.

### Krok 3 Zainstaluj zależności

```bash
pip install -r requirements.txt
```

Przejdź do Sekcji 3 o [kluczach API](#3-dodaj-swoje-klucze-api)

## 2. Opcja B – VS Code Dev Container (Docker)

Przygotowaliśmy to repozytorium i kurs z użyciem [kontenera deweloperskiego](https://containers.dev?WT.mc_id=academic-105485-koreyst), który ma uniwersalne środowisko uruchomieniowe obsługujące Python3, .NET, Node.js oraz Java. Powiązana konfiguracja znajduje się w pliku `devcontainer.json` w folderze `.devcontainer/` u podstawy tego repozytorium.

>**Dlaczego warto to wybrać?**
>Identyczne środowisko jak w Codespaces; brak dryfu zależności.

### Krok 0 Zainstaluj dodatki

Docker Desktop – potwierdź działanie polecenia ```docker --version```.
Rozszerzenie VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Krok 1 Otwórz repozytorium w VS Code

Plik ▸ Otwórz folder… → generative-ai-for-beginners

VS Code wykryje .devcontainer/ i wyświetli monit.

### Krok 2 Otwórz ponownie w kontenerze

Kliknij „Otwórz ponownie w kontenerze”. Docker buduje obraz (≈ 3 min pierwsze uruchomienie).
Gdy pojawi się wiersz poleceń, jesteś w środku kontenera.

## 2. Opcja C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie między różnymi wirtualnymi środowiskami Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) oraz pakietami. Jest też przydatny do instalowania pakietów niedostępnych przez `pip`.

### Krok 0  Zainstaluj Miniconda

Postępuj zgodnie z [instrukcją instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### Krok 1 Utwórz środowisko wirtualne

Utwórz nowy plik środowiskowy (*environment.yml*). Jeśli pracujesz w Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

### Krok 2 Wypełnij plik środowiska

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

Wykonaj poniższe polecenia w terminalu/wierszu poleceń

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podścieżka .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

W razie problemów zobacz [przewodnik po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2 Opcja D – Klasyczny Jupyter / Jupyter Lab (w przeglądarce)

> **Dla kogo?**  
> Dla tych, którzy lubią klasyczny interfejs Jupyter lub chcą uruchamiać notebooki bez VS Code.  

### Krok 1  Upewnij się, że Jupyter jest zainstalowany

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, nawiguj do folderu kursu i wykonaj polecenie:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupytera, a adres URL do jej otwarcia pojawi się w oknie wiersza poleceń.

Po wejściu na adres URL zobaczysz plan kursu i będziesz mógł nawigować do dowolnego pliku `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodaj swoje klucze API

Bezpieczeństwo kluczy API jest ważne przy budowaniu dowolnej aplikacji. Zalecamy nie przechowywać kluczy API bezpośrednio w kodzie. Umieszczenie ich w publicznym repozytorium może prowadzić do problemów bezpieczeństwa i niechcianych kosztów, jeśli zostaną wykorzystane przez osoby niepowołane.
Oto krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać swoje poświadczenia Microsoft Foundry Models:

> **Uwaga:** GitHub Models (i jego zmienna `GITHUB_TOKEN`) wycofywane pod koniec lipca 2026. Ten przewodnik używa zamiast tego [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Wolisz pracować całkowicie offline? Zobacz [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz poleceń i przejdź do katalogu głównego projektu, gdzie chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj ulubionego edytora tekstu, by stworzyć nowy plik o nazwie `.env`. Z poziomu terminala możesz użyć `touch` (na systemach Unix) lub `echo` (na Windows):

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj następujące linie, zastępując symbole zastępcze swoimi rzeczywistymi danymi Microsoft Foundry projektu i klucza API:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze nie masz, zainstaluj pakiet `python-dotenv` do ładowania zmiennych środowiskowych z pliku `.env` do aplikacji Python. Możesz to zrobić za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w skrypcie Python**: W skrypcie użyj pakietu `python-dotenv`, aby załadować zmienne z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Załaduj zmienne środowiskowe z pliku .env
   load_dotenv()

   # Uzyskaj dostęp do zmiennych modeli Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś poświadczenia Microsoft Foundry Models i załadowałeś je do aplikacji Python.

🔐 Nigdy nie commituj pliku .env — jest już w .gitignore.
Pełne instrukcje od dostawców znajdziesz w [`providers.md`](03-providers.md).

## 4. Co dalej?

| Chcę…              | Przejdź do…                                                            |
|---------------------|------------------------------------------------------------------------|
| Zacząć lekcję 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                       |
| Poznać innych uczniów | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Rozwiązywanie problemów

| Objaw                                     | Naprawa                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python nie znaleziony`                    | Dodaj Pythona do PATH lub ponownie otwórz terminal po instalacji|
| `pip` nie może zbudować kółek (Windows)    | `pip install --upgrade pip setuptools wheel`, potem ponów próbę.|
| `ModuleNotFoundError: dotenv`               | Uruchom `pip install -r requirements.txt` (środowisko nie było zainstalowane). |
| Błąd budowy Dockera *No space left*          | Docker Desktop ▸ *Ustawienia* ▸ *Zasoby* → zwiększ rozmiar dysku.|
| VS Code ciągle pyta o ponowne otwarcie       | Możesz mieć aktywne obie opcje; wybierz jedną (venv **lub** kontener)|
| Błędy OpenAI 401 / 429                      | Sprawdź wartość `OPENAI_API_KEY` / limity zapytań.              |
| Błędy korzystania z Conda                   | Zainstaluj biblioteki Microsoft AI używając `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->