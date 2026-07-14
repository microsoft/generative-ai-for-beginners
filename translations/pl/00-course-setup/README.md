# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i zobaczysz, co zainspiruje Cię do stworzenia przy pomocy Generatywnej SI!

Aby zapewnić Twój sukces, ta strona opisuje kroki konfiguracji, wymagania techniczne i gdzie szukać pomocy w razie potrzeby.

## Kroki konfiguracji

Aby rozpocząć ten kurs, musisz wykonać następujące kroki.

### 1. Sforkuj to repozytorium

[Sforkuj całe to repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) do swojego konta GitHub, aby móc zmieniać kod i wykonywać wyzwania. Możesz także [dodać (🌟) to repo do ulubionych](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy uruchomienie tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

W swoim fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj sekret

1. ⚙️ Ikona koła zębatego -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nazwij OPENAI_API_KEY, wklej swój klucz, Zapisz.

### 3. Co dalej?

| Chcę…             | Idź do…                                                                |
|--------------------|------------------------------------------------------------------------|
| Zacząć Lekcję 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Pracować offline   | [`setup-local.md`](02-setup-local.md)                                  |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                  |
| Spotkać innych uczących się | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rozwiązywanie problemów


| Objaw                                     | Naprawa                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Budowa kontenera zatrzymana > 10 min      | **Codespaces ➜ „Rebuild Container”**                          |
| `python: command not found`                | Terminal nie dołączył; kliknij **+** ➜ *bash*                 |
| `401 Unauthorized` od OpenAI                | Zły / wygasły `OPENAI_API_KEY`                                |
| VS Code pokazuje “Dev container mounting…”| Odśwież kartę przeglądarki—Codespaces czasami traci połączenie|
| Brak jądra w notatniku                     | Menu notatnika ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Systemy oparte na Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj poniższe linie do pliku, zastępując placeholdery rzeczywistym punktem końcowym i kluczem Microsoft Foundry Models (patrz [`providers.md`](03-providers.md), jak je zdobyć):

   > **Uwaga:** GitHub Models (i jego zmienna `GITHUB_TOKEN`) zostanie wycofany pod koniec lipca 2026. Używaj zamiast tego [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, zainstaluj pakiet `python-dotenv`, aby ładować zmienne środowiskowe z pliku `.env` do aplikacji Python. Możesz zainstalować go za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w swoim skrypcie Pythona**: W swoim skrypcie Python użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Załaduj zmienne środowiskowe z pliku .env
   load_dotenv()

   # Uzyskaj dostęp do zmiennych Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś dane uwierzytelniające Microsoft Foundry Models i załadowałeś je do swojej aplikacji Python.

## Jak uruchomić lokalnie na komputerze

Aby uruchomić kod lokalnie na komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby następnie użyć repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy masz wszystko sklonowane, możesz zacząć!

## Kroki opcjonalne

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Sam Conda to menedżer pakietów, który ułatwia konfigurację i przełączanie się między różnymi Pythonowymi [**środowiskami wirtualnymi**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i pakietami. Przydaje się też do instalacji pakietów niedostępnych przez `pip`.

Możesz postępować zgodnie z [przewodnikiem instalacji Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po zainstalowaniu Miniconda, sklonuj [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś)

Następnie stwórz środowisko wirtualne. Aby to zrobić za pomocą Conda, utwórz plik ze środowiskiem (_environment.yml_). Jeśli korzystasz z Codespaces, umieść ten plik w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

Uzupełnij swój plik środowiska poniższym fragmentem:

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

Jeśli pojawią się błędy podczas używania conda, możesz ręcznie zainstalować biblioteki Microsoft AI poleceniem w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<environment-name>` to nazwa, jaką chcesz nadać swojemu środowisku Conda, a `<python-version>` to wersja Pythona, np. `3` to najnowsza główna wersja Pythona.

Po wykonaniu tego stwórz środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podścieżka .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

Odwiedź [przewodnik po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jeśli napotkasz problemy.

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) do tego kursu. To jednak tylko zalecenie, a nie obowiązek.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. To dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium. Więcej o tym później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, program automatycznie zasugeruje instalację rozszerzenia wsparcia Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odmów tej prośby, jeśli chcesz używać lokalnej instalacji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz także pracować nad projektem korzystając ze środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko deweloperskie z funkcjami takimi jak autouzupełnianie, podświetlanie kodu itd.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wierza poleceń, wejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a URL do niej pojawi się w oknie wiersza poleceń.

Po wejściu na ten URL, zobaczysz zarys kursu i będziesz mógł przejść do dowolnego pliku `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą dla konfiguracji wszystkiego na komputerze lub w Codespace jest użycie [kontenera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny katalog `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces, wymaga to instalacji Dockera i jest nieco skomplikowane, dlatego zalecamy to osobom mającym doświadczenie z kontenerami.

Jednym z najlepszych sposobów zabezpieczenia kluczy API przy użyciu GitHub Codespaces jest korzystanie z sekretów Codespace. Prosimy o zapoznanie się z przewodnikiem [Zarządzanie sekretami w Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej.


## Lekcje i wymagania techniczne

Kurs składa się z 6 lekcji koncepcyjnych i 6 lekcji programistycznych.

Do lekcji programistycznych używamy usługi Azure OpenAI Service. Aby uruchomić ten kod, potrzebujesz dostępu do usługi Azure OpenAI i klucza API. Możesz uzyskać dostęp, [składając ten wniosek](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Podczas oczekiwania na rozpatrzenie wniosku, każda lekcja programistyczna zawiera również plik `README.md`, w którym możesz przeglądać kod i wyniki.

## Korzystanie po raz pierwszy z usługi Azure OpenAI

Jeśli korzystasz z usługi Azure OpenAI po raz pierwszy, prosimy o zapoznanie się z tym przewodnikiem jak [utworzyć i wdrożyć zasób Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie po raz pierwszy z OpenAI API

Jeśli korzystasz z OpenAI API po raz pierwszy, zapoznaj się z przewodnikiem jak [utworzyć i korzystać z interfejsu](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczących się

Utworzyliśmy kanały na naszym oficjalnym [serwerze Discord społeczności AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), aby poznać innych uczących się. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i osobami chcącymi rozwijać się w Generatywnej SI.

[![Dołącz do kanału Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektu będzie również na tym serwerze Discord, aby pomagać uczącym się.

## Współtwórz

Ten kurs jest inicjatywą open-source. Jeśli widzisz obszary do poprawy lub błędy, utwórz proszę [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem na GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektu będzie śledził wszystkie wkłady. Współtworzenie open source to świetny sposób na budowanie kariery w Generatywnej SI.

Większość wkładów wymaga zgody na Umowę Licencyjną Współtwórcy (CLA), deklarującą, że masz prawo i faktycznie udzielasz nam praw do wykorzystania Twojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstu w tym repozytorium upewnij się, że nie korzystasz z tłumaczenia maszynowego. Weryfikujemy tłumaczenia przez społeczność, więc prosimy o wolontariat do tłumaczeń tylko na języki, którymi naprawdę się posługujesz.

Po wysłaniu pull requesta bot CLA automatycznie sprawdzi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykieta, komentarz). Po prostu postępuj zgodnie z instrukcjami bota. Musisz to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.


Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Aby uzyskać więcej informacji, przeczytaj FAQ dotyczące Kodeksu Postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Zaczynajmy

Teraz, gdy ukończyłeś wymagane kroki, aby zakończyć ten kurs, zacznijmy od [wprowadzenia do Generatywnej SI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->