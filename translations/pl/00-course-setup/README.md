<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T08:55:49+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i nie możemy się doczekać, aby zobaczyć, co zainspiruje Cię do stworzenia przy użyciu generatywnej AI!

Aby zapewnić Ci sukces, ta strona przedstawia kroki konfiguracji, wymagania techniczne i wskazuje, gdzie uzyskać pomoc, jeśli zajdzie taka potrzeba.

## Kroki konfiguracji

Aby rozpocząć kurs, musisz wykonać następujące kroki.

### 1. Forkuj to Repozytorium

[Forkuj całe repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i wykonywać wyzwania. Możesz również [dodać gwiazdkę (🌟) temu repozytorium](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć i powiązane repozytoria.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy uruchomienie tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Można to zrobić, wybierając opcję `Code` w sforkowanej wersji tego repozytorium i wybierając opcję **Codespaces**.

![Dialog pokazujący przyciski do tworzenia codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Przechowywanie kluczy API

Bezpieczeństwo kluczy API jest ważne przy tworzeniu dowolnego rodzaju aplikacji. Zalecamy nie przechowywać kluczy API bezpośrednio w kodzie. Przekazanie tych danych do publicznego repozytorium może prowadzić do problemów z bezpieczeństwem, a nawet niechcianych kosztów, jeśli zostaną użyte przez złego aktora.
Oto krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz polecenia i przejdź do katalogu głównego projektu, w którym chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj preferowanego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli korzystasz z wiersza polecenia, możesz użyć `touch` (on Unix-based systems) or `echo` (na Windowsie):

   Systemy Unixowe:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj następującą linię do pliku, zastępując `your_github_token_here` rzeczywistym tokenem GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj pakiet `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do aplikacji Python. Możesz go zainstalować za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w swoim skrypcie Python**: W swoim skrypcie Python użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

I to wszystko! Udało Ci się stworzyć plik `.env`, dodać swój token GitHub i załadować go do aplikacji Python.

## Jak uruchomić lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na swoim komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby potem użyć repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy wszystko będzie gotowe, możesz zaczynać!

## Opcjonalne kroki 

### Instalacja Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Conda sama w sobie jest menedżerem pakietów, który ułatwia konfigurację i przełączanie się między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Przydaje się również do instalacji pakietów, które nie są dostępne przez `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Przejdź do swojego pliku środowiska i dodaj poniższy fragment:

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

Jeśli napotkasz błędy podczas używania conda, możesz ręcznie zainstalować biblioteki AI Microsoftu za pomocą następującego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` to najnowsza główna wersja Pythona.

Po wykonaniu tego kroku możesz przejść do tworzenia swojego środowiska Conda, uruchamiając poniższe polecenia w wierszu polecenia/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Zapoznaj się z [przewodnikiem po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jeśli napotkasz jakiekolwiek problemy.

### Korzystanie z Visual Studio Code z rozszerzeniem wsparcia dla Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia dla Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) na potrzeby tego kursu. Jest to jednak bardziej zalecenie niż wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej na ten temat później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zasugeruje on zainstalowanie rozszerzenia wsparcia dla Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odmów tej prośby, aby korzystać z lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz również pracować nad projektem, korzystając z [środowiska Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w swojej przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko deweloperskie z funkcjami takimi jak automatyczne uzupełnianie, podświetlanie kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza polecenia, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a URL do jej dostępu zostanie wyświetlony w oknie wiersza polecenia.

Po uzyskaniu dostępu do URL, powinieneś zobaczyć zarys kursu i móc nawigować do dowolnego pliku `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, w którym możesz przeglądać kod i wyniki.

## Pierwsze użycie usługi Azure OpenAI

Jeśli to Twój pierwszy raz korzystasz z usługi Azure OpenAI, postępuj zgodnie z tym przewodnikiem, jak [utworzyć i wdrożyć zasób usługi Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Pierwsze użycie API OpenAI

Jeśli to Twój pierwszy raz korzystasz z API OpenAI, postępuj zgodnie z przewodnikiem, jak [utworzyć i używać Interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczestników kursu

Stworzyliśmy kanały na naszym oficjalnym [serwerze Discord społeczności AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) do spotkań z innymi uczestnikami kursu. To świetny sposób na nawiązywanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i każdym, kto chce się rozwijać w generatywnej AI.

[![Dołącz do kanału Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy również będzie obecny na tym serwerze Discord, aby pomóc uczestnikom kursu.

## Wnieś swój wkład

Ten kurs jest inicjatywą open-source. Jeśli dostrzegasz obszary do poprawy lub problemy, stwórz [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem na GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledzić wszystkie wkłady. Wnoszenie wkładu do open source to świetny sposób na rozwijanie kariery w generatywnej AI.

Większość wkładów wymaga zgody na Umowę Licencyjną Wkładcy (CLA), deklarującą, że masz prawo i faktycznie udzielasz nam prawa do używania swojego wkładu. Szczegóły znajdziesz na stronie [CLA, Umowa Licencyjna Wkładcy](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstu w tym repozytorium, upewnij się, że nie korzystasz z tłumaczenia maszynowego. Zweryfikujemy tłumaczenia poprzez społeczność, więc prosimy o zgłaszanie się do tłumaczeń tylko w językach, w których jesteś biegły.

Po przesłaniu pull request, CLA-bot automatycznie określi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykieta, komentarz). Po prostu postępuj zgodnie z instrukcjami dostarczonymi przez bota. Będziesz musiał to zrobić tylko raz we wszystkich repozytoriach korzystających z naszego CLA.

Ten projekt przyjął [Kodeks Postępowania Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Więcej informacji znajdziesz w FAQ Kodeksu Postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com) w przypadku dodatkowych pytań lub komentarzy.

## Zaczynajmy

Teraz, gdy ukończyłeś potrzebne kroki, aby ukończyć ten kurs, zacznijmy od [wprowadzenia do generatywnej AI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.