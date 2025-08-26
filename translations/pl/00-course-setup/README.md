<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:38:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Rozpoczęcie pracy z tym kursem

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i nie możemy się doczekać, co zainspiruje Cię do stworzenia z Generatywną Sztuczną Inteligencją!

Aby zapewnić Ci sukces, na tej stronie znajdziesz kroki konfiguracji, wymagania techniczne oraz informacje, gdzie szukać pomocy w razie potrzeby.

## Kroki konfiguracji

Aby rozpocząć kurs, wykonaj poniższe kroki.

### 1. Forkuj to repozytorium

[Forkuj całe to repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i rozwiązywać zadania. Możesz także [dodać repozytorium do ulubionych (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je odnaleźć razem z powiązanymi repozytoriami.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy korzystanie z [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) podczas pracy z tym kursem.

W swoim forku: **Code -> Codespaces -> New on main**

![Okno dialogowe z przyciskami do utworzenia codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodaj sekret

1. ⚙️ Ikona koła zębatego -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nazwij OPENAI_API_KEY, wklej swój klucz, Zapisz.

### 3.  Co dalej?

| Chcę…                | Przejdź do…                                                              |
|----------------------|--------------------------------------------------------------------------|
| Rozpocząć Lekcję 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Pracować offline     | [`setup-local.md`](02-setup-local.md)                                    |
| Skonfigurować dostawcę LLM | [`providers.md`](providers.md)                                 |
| Poznać innych uczestników | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Rozwiązywanie problemów

| Objaw                                      | Rozwiązanie                                                      |
|--------------------------------------------|------------------------------------------------------------------|
| Budowanie kontenera trwa > 10 min          | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                | Terminal nie został podłączony; kliknij **+** ➜ *bash*           |
| `401 Unauthorized` z OpenAI                | Zły / wygasły `OPENAI_API_KEY`                                   |
| VS Code pokazuje “Dev container mounting…” | Odśwież kartę przeglądarki — Codespaces czasem traci połączenie  |
| Brak kernela notebooka                     | Menu notebooka ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj poniższą linię do pliku, zamieniając `your_github_token_here` na swój prawdziwy token GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, zainstaluj pakiet `python-dotenv`, aby ładować zmienne środowiskowe z pliku `.env` do swojej aplikacji Python. Możesz to zrobić za pomocą `pip`:

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

To wszystko! Udało Ci się utworzyć plik `.env`, dodać swój token GitHub i załadować go do swojej aplikacji Python.

## Jak uruchomić lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na swoim komputerze, musisz mieć zainstalowaną jakąś wersję [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Aby korzystać z repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy już wszystko pobierzesz, możesz zaczynać!

## Kroki opcjonalne

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Sama Conda to menedżer pakietów, który ułatwia tworzenie i przełączanie się między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Przydaje się także do instalowania pakietów niedostępnych przez `pip`.

Możesz skorzystać z [przewodnika instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby ją skonfigurować.

Po zainstalowaniu Minicondy musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś).

Następnie musisz utworzyć wirtualne środowisko. Aby to zrobić za pomocą Conda, utwórz nowy plik środowiska (_environment.yml_). Jeśli korzystasz z Codespaces, utwórz go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

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

Jeśli napotkasz błędy podczas korzystania z conda, możesz ręcznie zainstalować biblioteki Microsoft AI za pomocą poniższego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa potrzebne zależności. `<environment-name>` to nazwa, jaką chcesz nadać swojemu środowisku Conda, a `<python-version>` to wersja Pythona, której chcesz użyć, np. `3` to najnowsza główna wersja Pythona.

Gdy to zrobisz, możesz utworzyć środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jeśli napotkasz problemy, zajrzyj do [przewodnika po środowiskach Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korzystanie z Visual Studio Code z rozszerzeniem do Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem do obsługi Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) podczas tego kursu. Jest to jednak tylko rekomendacja, a nie wymóg.

> **Note**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej o tym później.

> **Note**: Po sklonowaniu i otwarciu katalogu w VS Code, edytor automatycznie zasugeruje instalację rozszerzenia do obsługi Pythona.

> **Note**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę propozycję, aby korzystać z lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz także pracować nad projektem korzystając ze środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjazne środowisko programistyczne z funkcjami takimi jak autouzupełnianie, podświetlanie składni itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a adres URL do niej pojawi się w oknie terminala.

Po wejściu na ten adres zobaczysz strukturę kursu i będziesz mógł przejść do dowolnego pliku `*.ipynb`. Na przykład `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą dla konfiguracji wszystkiego na swoim komputerze lub w Codespace jest użycie [kontenera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces wymaga to instalacji Dockera i, szczerze mówiąc, wymaga trochę pracy, więc polecamy to tylko osobom z doświadczeniem w pracy z kontenerami.

Jednym z najlepszych sposobów na zabezpieczenie kluczy API podczas korzystania z GitHub Codespaces jest użycie Codespace Secrets. Zapoznaj się z przewodnikiem [Zarządzanie sekretami Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej.

## Lekcje i wymagania techniczne

Kurs składa się z 6 lekcji koncepcyjnych i 6 lekcji programistycznych.

W lekcjach programistycznych korzystamy z usługi Azure OpenAI Service. Aby uruchomić ten kod, będziesz potrzebować dostępu do usługi Azure OpenAI oraz klucza API. Możesz ubiegać się o dostęp, [wypełniając ten formularz](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Podczas oczekiwania na rozpatrzenie wniosku, każda lekcja programistyczna zawiera także plik `README.md`, w którym możesz zobaczyć kod i wyniki.

## Pierwsze użycie usługi Azure OpenAI

Jeśli po raz pierwszy korzystasz z usługi Azure OpenAI, zapoznaj się z przewodnikiem, jak [utworzyć i wdrożyć zasób Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Pierwsze użycie OpenAI API

Jeśli po raz pierwszy korzystasz z OpenAI API, zapoznaj się z przewodnikiem, jak [utworzyć i używać interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczestników

Stworzyliśmy kanały na naszym oficjalnym [serwerze Discord AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), aby umożliwić poznanie innych uczestników. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i wszystkimi, którzy chcą rozwijać się w Generatywnej AI.

[![Dołącz do kanału discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy również będzie obecny na tym serwerze Discord, aby pomagać uczestnikom.

## Współtwórz

Ten kurs to inicjatywa open-source. Jeśli zauważysz miejsca do poprawy lub błędy, utwórz [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem na GitHubie](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledził wszystkie zgłoszone wkłady. Współtworzenie open source to świetny sposób na rozwój kariery w Generatywnej AI.

Większość kontrybucji wymaga zaakceptowania Contributor License Agreement (CLA), potwierdzającego, że masz prawo i faktycznie udzielasz nam praw do wykorzystania swojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: tłumacząc teksty w tym repozytorium, nie używaj tłumaczenia maszynowego. Tłumaczenia będą weryfikowane przez społeczność, więc zgłaszaj się tylko do tłumaczeń na języki, które znasz bardzo dobrze.

Po przesłaniu pull requesta, bot CLA automatycznie sprawdzi, czy musisz zaakceptować CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Po prostu postępuj zgodnie z instrukcjami bota. Wystarczy to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Więcej informacji znajdziesz w FAQ dotyczących Code of Conduct lub kontaktując się pod [Email opencode](opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Zaczynajmy
Teraz, gdy ukończyłeś wszystkie potrzebne kroki, aby zaliczyć ten kurs, zacznijmy od [wprowadzenia do Generatywnej Sztucznej Inteligencji i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego ojczystym języku powinien być traktowany jako źródło nadrzędne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.