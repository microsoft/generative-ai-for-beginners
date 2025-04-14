# Rozpoczęcie Pracy z Tym Kursem

Jesteśmy bardzo podekscytowani, że rozpoczynasz ten kurs i nie możemy się doczekać, co zostaniesz zainspirowany do zbudowania z pomocą Generatywnej SI!

Aby zapewnić Twój sukces, ta strona opisuje kroki konfiguracyjne, wymagania techniczne i gdzie uzyskać pomoc, jeśli będzie potrzebna.

## Kroki Konfiguracyjne

Aby rozpocząć ten kurs, będziesz musiał wykonać następujące kroki.

### 1. Wykonaj Fork Tego Repozytorium

[Utwórz fork całego repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje własne konto GitHub, aby móc zmieniać kod i wykonywać zadania. Możesz również [oznaczyć gwiazdką (🌟) to repozytorium](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz Codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy uruchamianie tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Można go utworzyć, wybierając opcję `Code` w swojej sforkowanej wersji tego repozytorium i wybierając opcję **Codespaces**.

![Dialog pokazujący przyciski do utworzenia codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

### 3. Przechowywanie Kluczy API

Utrzymywanie twoich kluczy API w bezpieczeństwie jest ważne podczas budowania jakiejkolwiek aplikacji. Zalecamy, aby nie przechowywać kluczy API bezpośrednio w kodzie. Zatwierdzenie tych szczegółów do publicznego repozytorium może skutkować problemami z bezpieczeństwem i nawet niepożądanymi kosztami, jeśli zostaną wykorzystane przez osoby o złych zamiarach.
Oto przewodnik krok po kroku, jak utworzyć plik `.env` dla Pythona i dodać `GITHUB_TOKEN`:

1. **Przejdź do Katalogu Twojego Projektu**: Otwórz terminal lub wiersz poleceń i przejdź do głównego katalogu projektu, gdzie chcesz utworzyć plik `.env`.

   ```bash
   cd ścieżka/do/twojego/projektu
   ```

2. **Utwórz Plik `.env`**: Użyj swojego ulubionego edytora tekstu, aby utworzyć nowy plik o nazwie `.env`. Jeśli używasz wiersza poleceń, możesz użyć `touch` (w systemach Unix) lub `echo` (w Windows):

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo. > .env
   ```

3. **Edytuj Plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub dowolnym innym edytorze). Dodaj następującą linię do pliku, zastępując `twój_token_github_tutaj` swoim rzeczywistym tokenem GitHub:

   ```env
   GITHUB_TOKEN=twój_token_github_tutaj
   ```

4. **Zapisz Plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, będziesz musiał zainstalować pakiet `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do twojej aplikacji Python. Możesz go zainstalować za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj Zmienne Środowiskowe w Twoim Skrypcie Python**: W twoim skrypcie Python użyj pakietu `python-dotenv` do załadowania zmiennych środowiskowych z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Załaduj zmienne środowiskowe z pliku .env
   load_dotenv()

   # Uzyskaj dostęp do zmiennej GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś swój token GitHub i załadowałeś go do swojej aplikacji Python.

## Jak Uruchomić Lokalnie na Twoim Komputerze

Aby uruchomić kod lokalnie na swoim komputerze, będziesz potrzebować jakiejś wersji [zainstalowanego Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby następnie korzystać z repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Po sprawdzeniu wszystkiego, możesz zacząć!

## Opcjonalne Kroki

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, a także kilku pakietów.
Conda sama w sobie jest menedżerem pakietów, który ułatwia konfigurację i przełączanie się między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Jest również przydatna do instalowania pakietów, które nie są dostępne przez `pip`.

Możesz postępować zgodnie z [przewodnikiem instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby go skonfigurować.

Po zainstalowaniu Miniconda musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś)

Następnie musisz utworzyć wirtualne środowisko. Aby to zrobić z Conda, utwórz nowy plik środowiska (_environment.yml_). Jeśli używasz Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

Wypełnij swój plik środowiska poniższym fragmentem:

```yml
name: <nazwa-środowiska>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<wersja-pythona>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Jeśli napotkasz błędy podczas korzystania z conda, możesz ręcznie zainstalować Biblioteki Microsoft AI za pomocą następującego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<nazwa-środowiska>` odnosi się do nazwy, którą chcesz nadać swojemu środowisku Conda, a `<wersja-pythona>` to wersja Pythona, której chcesz użyć, na przykład `3` to najnowsza główna wersja Pythona.

Po tym, możesz utworzyć swoje środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ścieżka podkatalogu .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

Sprawdź [przewodnik po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jeśli napotkasz jakiekolwiek problemy.

### Korzystanie z Visual Studio Code z rozszerzeniem wsparcia Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dla tego kursu. Jest to jednak bardziej zalecenie niż bezwzględny wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej na ten temat później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zasugeruje ci zainstalowanie rozszerzenia wsparcia Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ci ponowne otwarcie repozytorium w kontenerze, odrzuć tę prośbę, aby używać lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w Przeglądarce

Możesz również pracować nad projektem przy użyciu [środowiska Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) zapewniają dość przyjemne środowisko programistyczne z funkcjami takimi jak automatyczne uzupełnianie, podświetlanie składni itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

Spowoduje to uruchomienie instancji Jupyter, a URL do uzyskania dostępu zostanie wyświetlony w oknie wiersza poleceń.

Po uzyskaniu dostępu do adresu URL, powinieneś zobaczyć zarys kursu i móc przejść do dowolnego pliku `*.ipynb`. Na przykład, `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą dla konfigurowania wszystkiego na swoim komputerze lub Codespace jest użycie [kontenera](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces wymaga to instalacji Dockera i, szczerze mówiąc, wymaga trochę pracy, więc zalecamy to tylko osobom mającym doświadczenie w pracy z kontenerami.

Jednym z najlepszych sposobów zabezpieczenia kluczy API podczas korzystania z GitHub Codespaces jest używanie Sekretów Codespaces. Przejdź do [przewodnika zarządzania sekretami Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej na ten temat.

## Lekcje i Wymagania Techniczne

Kurs składa się z 6 lekcji koncepcyjnych i 6 lekcji kodowania.

W przypadku lekcji kodowania korzystamy z usługi Azure OpenAI. Będziesz potrzebować dostępu do usługi Azure OpenAI i klucza API, aby uruchomić ten kod. Możesz ubiegać się o dostęp, [wypełniając ten wniosek](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Podczas oczekiwania na rozpatrzenie Twojego wniosku, każda lekcja kodowania zawiera również plik `README.md`, w którym możesz przeglądać kod i wyniki.

## Korzystanie z Usługi Azure OpenAI po raz pierwszy

Jeśli jest to Twój pierwszy raz korzystania z usługi Azure OpenAI, postępuj zgodnie z tym przewodnikiem, jak [utworzyć i wdrożyć zasób Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie z API OpenAI po raz pierwszy

Jeśli jest to Twój pierwszy raz korzystania z API OpenAI, postępuj zgodnie z przewodnikiem, jak [utworzyć konto i korzystać z Interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj Innych Uczących się

Stworzyliśmy kanały na naszym oficjalnym [serwerze Discord społeczności AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) do spotykania innych uczących się. To świetny sposób na nawiązywanie kontaktów z innymi podobnie myślącymi przedsiębiorcami, twórcami, studentami i wszystkimi, którzy chcą podnieść swój poziom w dziedzinie Generatywnej SI.

[![Dołącz do kanału discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy będzie również obecny na tym serwerze Discord, aby pomóc uczącym się.

## Przyczyń się

Ten kurs jest inicjatywą open-source. Jeśli widzisz obszary do poprawy lub problemy, utwórz [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem na GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledził wszystkie wkłady. Przyczynianie się do projektów open source to świetny sposób na budowanie swojej kariery w Generatywnej SI.

Większość wkładów wymaga zgody na Umowę Licencyjną Współtwórcy (CLA), deklarującą, że masz prawo i faktycznie udzielasz nam praw do korzystania z Twojego wkładu. Aby uzyskać szczegółowe informacje, odwiedź [stronę internetową CLA, Umowy Licencyjnej Współtwórcy](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstu w tym repozytorium upewnij się, że nie używasz tłumaczenia maszynowego. Będziemy weryfikować tłumaczenia za pośrednictwem społeczności, więc zgłaszaj się do tłumaczeń tylko w językach, w których biegle się posługujesz.

Gdy złożysz Pull Request, bot CLA automatycznie określi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Po prostu postępuj zgodnie z instrukcjami dostarczonymi przez bota. Będziesz musiał to zrobić tylko raz dla wszystkich repozytoriów używających naszego CLA.

Ten projekt przyjął [Kodeks Postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Aby uzyskać więcej informacji, przeczytaj FAQ dotyczące Kodeksu Postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com) w przypadku dodatkowych pytań lub komentarzy.

## Rozpocznijmy

Teraz, gdy wykonałeś wszystkie potrzebne kroki do ukończenia tego kursu, zacznijmy od [wprowadzenia do Generatywnej SI i modeli LLM](../../../01-introduction-to-genai/translations/pl/README.md?WT.mc_id=academic-105485-koreyst).
