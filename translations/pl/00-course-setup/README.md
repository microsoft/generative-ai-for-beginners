<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:08:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i zobaczysz, co zainspiruje Cię do stworzenia z wykorzystaniem Generative AI!

Aby zapewnić Ci sukces, ta strona przedstawia kroki konfiguracji, wymagania techniczne oraz informacje, gdzie szukać pomocy w razie potrzeby.

## Kroki konfiguracji

Aby rozpocząć kurs, musisz wykonać następujące kroki.

### 1. Forkuj to repozytorium

[Zforkuj całe to repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i realizować wyzwania. Możesz także [dodać repozytorium do ulubionych (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć wraz z powiązanymi repozytoriami.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy korzystanie z tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Możesz to zrobić, wybierając opcję `Code` w swojej zforkowanej wersji repozytorium, a następnie wybierając opcję **Codespaces**.

![Okno dialogowe pokazujące przyciski do utworzenia codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Przechowywanie kluczy API

Bezpieczne przechowywanie kluczy API jest ważne przy tworzeniu każdej aplikacji. Zalecamy, aby nie przechowywać kluczy API bezpośrednio w kodzie. Umieszczenie takich danych w publicznym repozytorium może prowadzić do problemów z bezpieczeństwem, a nawet niechcianych kosztów, jeśli ktoś niepowołany je wykorzysta.  
Oto krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz poleceń i przejdź do katalogu głównego projektu, w którym chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj swojego ulubionego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli korzystasz z linii poleceń, możesz użyć `touch` (na systemach Unix) lub `echo` (na Windows):

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

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, musisz zainstalować pakiet `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do aplikacji Python. Możesz to zrobić za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w skrypcie Python**: W swoim skrypcie Python użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś token GitHub i załadowałeś go do swojej aplikacji Python.

## Jak uruchomić lokalnie na komputerze

Aby uruchomić kod lokalnie na swoim komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Następnie, aby korzystać z repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy wszystko będzie gotowe, możesz zacząć!

## Kroki opcjonalne

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.  
Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie się między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona oraz pakietami. Przydaje się także do instalacji pakietów, które nie są dostępne przez `pip`.

Możesz skorzystać z [przewodnika instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby ją zainstalować.

Po zainstalowaniu Miniconda, musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś).

Następnie musisz utworzyć wirtualne środowisko. Aby to zrobić za pomocą Conda, stwórz nowy plik środowiska (_environment.yml_). Jeśli korzystasz z Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

Wypełnij plik środowiska poniższym fragmentem:

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

Jeśli pojawią się błędy podczas korzystania z conda, możesz ręcznie zainstalować Microsoft AI Libraries, używając poniższego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<environment-name>` to nazwa, jaką chcesz nadać swojemu środowisku Conda, a `<python-version>` to wersja Pythona, której chcesz użyć, np. `3` to najnowsza główna wersja Pythona.

Po tym możesz utworzyć środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

W razie problemów zajrzyj do [przewodnika po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem do Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) podczas tego kursu. To jednak tylko zalecenie, a nie wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Dzieje się tak dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej o tym później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, program automatycznie zasugeruje instalację rozszerzenia do Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę prośbę, jeśli chcesz korzystać z lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz także pracować nad projektem, korzystając ze środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko do pracy z funkcjami takimi jak autouzupełnianie, podświetlanie składni itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a adres URL do niej zostanie wyświetlony w oknie terminala.

Po wejściu na ten adres zobaczysz plan kursu i będziesz mógł otworzyć dowolny plik `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą dla konfiguracji wszystkiego na komputerze lub w Codespace jest użycie [kontenera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces wymaga to instalacji Dockera i, szczerze mówiąc, trochę pracy, więc polecamy to tylko osobom z doświadczeniem w pracy z kontenerami.

Jednym z najlepszych sposobów na zabezpieczenie kluczy API podczas korzystania z GitHub Codespaces jest użycie Codespace Secrets. Prosimy o zapoznanie się z przewodnikiem [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej.

## Lekcje i wymagania techniczne

Kurs składa się z 6 lekcji koncepcyjnych i 6 lekcji programistycznych.

Do lekcji programistycznych używamy Azure OpenAI Service. Aby uruchomić ten kod, potrzebujesz dostępu do usługi Azure OpenAI oraz klucza API. Możesz złożyć wniosek o dostęp, [wypełniając ten formularz](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Podczas oczekiwania na rozpatrzenie wniosku, każda lekcja programistyczna zawiera plik `README.md`, w którym możesz zobaczyć kod i wyniki.

## Korzystanie z Azure OpenAI Service po raz pierwszy

Jeśli korzystasz z Azure OpenAI Service po raz pierwszy, postępuj zgodnie z tym przewodnikiem, jak [utworzyć i wdrożyć zasób Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie z OpenAI API po raz pierwszy

Jeśli korzystasz z OpenAI API po raz pierwszy, zapoznaj się z przewodnikiem, jak [utworzyć i korzystać z interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczestników

Stworzyliśmy kanały na naszym oficjalnym serwerze [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), aby umożliwić spotkania z innymi uczestnikami. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i wszystkimi, którzy chcą rozwijać się w Generative AI.

[![Dołącz do kanału discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektu również będzie obecny na tym serwerze Discord, aby pomagać uczestnikom.

## Współtwórz

Ten kurs jest inicjatywą open-source. Jeśli zauważysz obszary do poprawy lub problemy, prosimy o utworzenie [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoszenie [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektu będzie śledził wszystkie wkłady. Współtworzenie open source to świetny sposób na rozwój kariery w Generative AI.

Większość wkładów wymaga zgody na Contributor License Agreement (CLA), w którym deklarujesz, że masz prawo i faktycznie udzielasz nam praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstów w tym repozytorium prosimy, aby nie korzystać z tłumaczeń maszynowych. Weryfikujemy tłumaczenia przez społeczność, więc prosimy o zgłaszanie się do tłumaczeń tylko w językach, w których jesteś biegły.

Po przesłaniu pull request, bot CLA automatycznie sprawdzi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Wystarczy postępować zgodnie z instrukcjami bota. Musisz to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Więcej informacji znajdziesz w FAQ dotyczących Kodeksu Postępowania lub możesz skontaktować się pod adresem [Email opencode](opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Zaczynamy

Teraz, gdy wykonałeś wszystkie niezbędne kroki, zacznijmy od [wprowadzenia do Generative AI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.