# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i zobaczysz, co zainspiruje Cię do stworzenia z wykorzystaniem Generatywnej AI!

Aby zapewnić Twój sukces, ta strona przedstawia kroki konfiguracyjne, wymagania techniczne oraz gdzie szukać pomocy, jeśli zajdzie taka potrzeba.

## Kroki konfiguracyjne

Aby rozpocząć kurs, musisz wykonać następujące kroki.

### 1. Utwórz fork tego repozytorium

[Utwórz fork całego repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i wykonywać zadania. Możesz także [oznaczyć to repozytorium gwiazdką (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy wykonywanie tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

W swoim forku: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj sekret

1. ⚙️ Ikona ustawień -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nazwij OPENAI_API_KEY, wklej swój klucz, Zapisz.

### 3. Co dalej?

| Chcę…              | Idź do…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Zacząć lekcję 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracować offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                     |
| Spotkać innych uczestników | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rozwiązywanie problemów


| Objaw                                     | Rozwiązanie                                                      |
|-------------------------------------------|-----------------------------------------------------------------|
| Budowanie kontenera zawiesza się > 10 min | **Codespaces ➜ „Rebuild Container”**                            |
| `python: command not found`               | Terminal nie został podłączony; kliknij **+** ➜ *bash*          |
| `401 Unauthorized` od OpenAI              | Błędny / wygasły `OPENAI_API_KEY`                               |
| VS Code pokazuje „Dev container mounting…” | Odśwież kartę przeglądarki — Codespaces czasami traci połączenie |
| Brak jądra w notatniku                    | Menu notatnika ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Systemy oparte na Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstowym (np. VS Code, Notepad++ lub innym). Dodaj do pliku poniższe linie, zamieniając miejsca zastępcze na rzeczywiste endpoint i klucz Microsoft Foundry Models (zobacz [`providers.md`](03-providers.md), jak je uzyskać):

   > **Uwaga:** GitHub Models (i zmienna `GITHUB_TOKEN`) będą wycofane z końcem lipca 2026 r. Zamiast nich używaj [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, zainstaluj pakiet `python-dotenv`, aby ładować zmienne środowiskowe z pliku `.env` do aplikacji Python. Możesz zainstalować go za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w skrypcie Pythona**: W Twoim skrypcie Python użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

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

To wszystko! Udało Ci się utworzyć plik `.env`, dodać dane uwierzytelniające Microsoft Foundry Models i załadować je do aplikacji Python.

## Jak uruchomić lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Następnie, aby korzystać z repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy masz już wszystko pobrane, możesz zacząć!

## Opcjonalne kroki

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie się między różnymi [wirtualnymi środowiskami](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Jest też pomocny przy instalacji pakietów, które nie są dostępne przez `pip`.

Możesz skorzystać z [przewodnika instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) aby ją zainstalować.

Po zainstalowaniu Miniconda musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś)

Następnie musisz utworzyć środowisko wirtualne. Aby to zrobić za pomocą Conda, utwórz nowy plik środowiska (_environment.yml_). Jeśli korzystasz z Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

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

Jeśli pojawiają się błędy przy korzystaniu z conda, możesz ręcznie zainstalować Microsoft AI Libraries wykonując poniższe polecenie w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<environment-name>` to nazwa, którą chcesz nadać środowisku Conda, a `<python-version>` to wersja Pythona, którą chcesz używać, na przykład `3` jest najnowszą główną wersją Pythona.

Po tym możesz utworzyć środowisko Conda, wykonując poniższe polecenia w wierszu poleceń/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podścieżka .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

Jeśli napotkasz problemy, zobacz [przewodnik po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korzystanie z Visual Studio Code z rozszerzeniem wsparcia Pythona

Zalecamy używanie edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) do tego kursu. To jednak bardziej rekomendacja niż bezwzględny wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, możesz ustawić projekt w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) w repozytorium kursu. Więcej o tym później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zostanie zasugerowane zainstalowanie rozszerzenia wsparcia Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę prośbę, aby używać lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz też pracować nad projektem korzystając ze środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko pracy z funkcjami takimi jak autouzupełnianie, podświetlanie kodu i inne.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a URL do niej zostanie wyświetlony w oknie wiersza poleceń.

Po wejściu pod URL zobaczysz konspekt kursu i będziesz mógł nawigować do dowolnego pliku `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą do instalacji wszystkiego na komputerze lub Codespace jest użycie [kontenera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu pozwala VS Code na skonfigurowanie projektu w kontenerze. Poza Codespaces wymaga to instalacji Dockera i, szczerze mówiąc, wiąże się z trochę większą pracą, więc zalecamy to tylko osobom doświadczonym w pracy z kontenerami.

Jednym z najlepszych sposobów na ochronę kluczy API podczas używania GitHub Codespaces jest korzystanie z Secrets Codespace. Proszę zapoznaj się z przewodnikiem [Zarządzanie sekretami w Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej.


## Lekcje i wymagania techniczne

Kurs zawiera lekcje "Learn", które wyjaśniają koncepcje Generatywnej AI, oraz lekcje "Build" z przykładami kodu praktycznego w **Pythonie** i **TypeScript**, gdzie to możliwe.

W lekcjach kodowania korzystamy z Azure OpenAI w Microsoft Foundry. Potrzebujesz subskrypcji Azure oraz klucza API. Dostęp jest otwarty - nie wymaga zgłoszenia - więc możesz [utworzyć zasób Microsoft Foundry i wdrożyć model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), aby uzyskać endpoint i klucz.

Każda lekcja kodowania zawiera również plik `README.md`, w którym możesz zobaczyć kod i wyniki bez uruchamiania czegokolwiek.

## Korzystanie z usługi Azure OpenAI po raz pierwszy

Jeśli to twój pierwszy raz z usługą Azure OpenAI, proszę zapoznaj się z przewodnikiem jak [utworzyć i wdrożyć zasób usługi Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Korzystanie z API OpenAI po raz pierwszy

Jeśli to twój pierwszy raz z API OpenAI, proszę zapoznaj się z przewodnikiem jak [utworzyć i korzystać z interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczestników

Utworzyliśmy kanały na naszym oficjalnym serwerze [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) do spotkań z innymi uczestnikami. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i każdym, kto chce rozwijać się w Generatywnej AI.

[![Dołącz do kanału na Discordzie](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy również będzie dostępny na tym serwerze Discord, aby pomagać uczestnikom.

## Wkład

Ten kurs jest inicjatywą open-source. Jeśli widzisz miejsca do poprawy lub błędy, prosimy utwórz [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem w GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledzić wszystkie wkłady. Udział w open source to świetny sposób na rozwój kariery w Generatywnej AI.

Większość wkładów wymaga zaakceptowania Contributor License Agreement (CLA), w którym oświadczasz, że masz prawo i faktycznie udzielasz nam praw do używania Twojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: podczas tłumaczenia tekstu w tym repozytorium, prosimy nie korzystaj z tłumaczeń maszynowych. Będziemy weryfikować tłumaczenia przez społeczność, więc zgłaszaj się tylko do tłumaczeń na języki, którymi naprawdę się posługujesz.


Gdy zgłaszasz pull request, bot CLA automatycznie określi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Wystarczy postępować zgodnie z instrukcjami przekazanymi przez bota. Będziesz musiał to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Aby uzyskać więcej informacji, przeczytaj FAQ dotyczące kodeksu postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Zaczynajmy

Teraz, gdy wykonałeś niezbędne kroki, aby ukończyć ten kurs, zacznijmy od [wprowadzenia do Generative AI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->