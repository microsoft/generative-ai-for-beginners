<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:48:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Rozpoczęcie kursu

Cieszymy się, że zaczynasz ten kurs i zobaczysz, do czego zainspiruje Cię budowanie z Generative AI!

Aby zapewnić Twój sukces, ta strona przedstawia kroki konfiguracyjne, wymagania techniczne oraz miejsca, gdzie możesz uzyskać pomoc, jeśli zajdzie taka potrzeba.

## Kroki konfiguracyjne

Aby rozpocząć ten kurs, musisz wykonać następujące kroki.

### 1. Zrób fork tego repozytorium

[Zrób fork całego tego repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i realizować wyzwania. Możesz również [dodać gwiazdkę (🌟) temu repozytorium](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz przestrzeń kodu

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy uruchomienie tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Można to zrobić, wybierając opcję `Code` w swojej wersji forkowanej tego repozytorium i wybierając opcję **Codespaces**.

![Dialog pokazujący przyciski do tworzenia przestrzeni kodu](../../../00-course-setup/images/who-will-pay.webp)

### 3. Przechowywanie kluczy API

Zabezpieczenie i ochrona kluczy API jest ważne przy tworzeniu jakiegokolwiek rodzaju aplikacji. Zalecamy nie przechowywać kluczy API bezpośrednio w kodzie. Umieszczanie tych danych w publicznym repozytorium może prowadzić do problemów z bezpieczeństwem, a nawet niechcianych kosztów, jeśli zostaną użyte przez złośliwe osoby. Oto przewodnik krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do katalogu projektu**: Otwórz terminal lub wiersz poleceń i przejdź do katalogu głównego projektu, w którym chcesz utworzyć plik `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Utwórz plik `.env`**: Użyj preferowanego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli korzystasz z wiersza poleceń, możesz użyć `touch` (on Unix-based systems) or `echo` (w systemie Windows):

   Systemy Unixowe:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym edytorze). Dodaj poniższą linię do pliku, zastępując `your_github_token_here` swoim rzeczywistym tokenem GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj pakiet `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do swojej aplikacji Python. Możesz go zainstalować za pomocą `pip`:

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

I to wszystko! Udało Ci się utworzyć plik `.env`, dodać swój token GitHub i załadować go do swojej aplikacji Python.

## Jak uruchomić lokalnie na komputerze

Aby uruchomić kod lokalnie na komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby następnie używać repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy wszystko będzie gotowe, możesz zaczynać!

## Kroki opcjonalne

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów. Sama Conda to menedżer pakietów, który ułatwia konfigurację i przełączanie się między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Jest także przydatna do instalowania pakietów, które nie są dostępne przez `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Przejdź dalej i uzupełnij swój plik środowiskowy poniższym fragmentem:

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

Jeśli napotkasz błędy podczas korzystania z conda, możesz ręcznie zainstalować Microsoft AI Libraries za pomocą poniższego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiskowy określa potrzebne zależności. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` to najnowsza główna wersja Pythona.

Po wykonaniu tego kroku możesz przejść do utworzenia środowiska Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Zapoznaj się z [przewodnikiem po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jeśli napotkasz jakiekolwiek problemy.

### Korzystanie z Visual Studio Code z rozszerzeniem wspierającym Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wspierającym Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dla tego kursu. Jest to jednak bardziej rekomendacja niż wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej na ten temat później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zasugeruje on zainstalowanie rozszerzenia wspierającego Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę prośbę, aby korzystać z lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz również pracować nad projektem, korzystając z [środowiska Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczne Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko deweloperskie z funkcjami takimi jak autouzupełnianie, podświetlanie kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a URL do jej dostępu zostanie pokazany w oknie wiersza poleceń.

Po uzyskaniu dostępu do URL, powinieneś zobaczyć zarys kursu i móc przejść do dowolnego pliku `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, gdzie możesz przeglądać kod i wyniki.

## Korzystanie z usługi Azure OpenAI po raz pierwszy

Jeśli po raz pierwszy korzystasz z usługi Azure OpenAI, postępuj zgodnie z tym przewodnikiem, jak [utworzyć i wdrożyć zasób usługi Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie z OpenAI API po raz pierwszy

Jeśli po raz pierwszy korzystasz z OpenAI API, postępuj zgodnie z przewodnikiem, jak [utworzyć i używać interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczących się

Stworzyliśmy kanały na naszym oficjalnym [serwerze Discord społeczności AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) do spotkań z innymi uczącymi się. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, budowniczymi, studentami i wszystkimi, którzy chcą rozwijać się w Generative AI.

[![Dołącz do kanału discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy również będzie na tym serwerze Discord, aby pomóc uczącym się.

## Współtwórz

Ten kurs jest inicjatywą open-source. Jeśli zauważysz obszary do poprawy lub problemy, prosimy o stworzenie [Pull Requesta](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoszenie [problemu na GitHubie](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledził wszystkie wkłady. Współpraca z open source to niesamowity sposób na rozwijanie kariery w Generative AI.

Większość wkładów wymaga zgody na Umowę Licencyjną Współtwórcy (CLA), deklarującą, że masz prawo do i faktycznie udzielasz nam praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstu w tym repozytorium, upewnij się, że nie używasz tłumaczenia maszynowego. Zweryfikujemy tłumaczenia przez społeczność, więc prosimy o zgłaszanie się do tłumaczeń tylko w językach, w których jesteś biegły.

Gdy zgłosisz pull request, bot CLA automatycznie określi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykieta, komentarz). Po prostu postępuj zgodnie z instrukcjami podanymi przez bota. Musisz to zrobić tylko raz we wszystkich repozytoriach korzystających z naszego CLA.

Ten projekt przyjął [Kodeks postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Aby uzyskać więcej informacji, przeczytaj FAQ dotyczące Kodeksu postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com) z dodatkowymi pytaniami lub komentarzami.

## Zaczynamy

Teraz, gdy ukończyłeś potrzebne kroki, aby ukończyć ten kurs, zacznijmy od [wprowadzenia do Generative AI i LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku istotnych informacji zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.