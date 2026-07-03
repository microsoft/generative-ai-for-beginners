# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i zobaczysz, co zainspiruje Cię do stworzenia z wykorzystaniem Generative AI!

Aby zapewnić Ci sukces, ta strona przedstawia kroki konfiguracji, wymagania techniczne oraz informacje, gdzie szukać pomocy, jeśli zajdzie taka potrzeba.

## Kroki konfiguracji

Aby rozpocząć ten kurs, musisz wykonać następujące kroki.

### 1. Utwórz fork tego repozytorium

[Utwórz fork całego repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoim koncie GitHub, aby móc zmieniać dowolny kod i realizować wyzwania. Możesz też [dodać to repo do ulubionych (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy korzystanie z tego kursu w [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

W Twoim forku: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Dodaj sekret

1. ⚙️ Ikona koła zębatego -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.  
2. Nazwij OPENAI_API_KEY, wklej swój klucz, Zapisz.

### 3. Co dalej?

| Chcę…                | Przejdź do…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Zacząć Lekcję 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracować offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                        |
| Spotkać innych uczniów | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Rozwiązywanie problemów


| Objaw                                     | Rozwiązanie                                                    |
|-------------------------------------------|-----------------------------------------------------------------|
| Budowanie kontenera zawiesza się > 10 min| **Codespaces ➜ „Rebuild Container”**                           |
| `python: command not found`                | Terminal się nie podłączył; kliknij **+** ➜ *bash*             |
| `401 Unauthorized` z OpenAI                 | Nieprawidłowy / wygasły `OPENAI_API_KEY`                      |
| VS Code pokazuje „Dev container mounting…”| Odśwież kartę przeglądarki—Codespaces czasem traci połączenie |
| Brak jądra w notebooku                      | Menu notebooka ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Systemy Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edytuj plik `.env`**: Otwórz plik `.env` w edytorze tekstu (np. VS Code, Notepad++ lub innym). Dodaj następującą linię do pliku, zastępując `your_github_token_here` swoim rzeczywistym tokenem GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Zapisz plik**: Zapisz zmiany i zamknij edytor tekstu.

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, musisz zainstalować pakiet `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do swojej aplikacji w Pythonie. Możesz to zrobić za pomocą `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Załaduj zmienne środowiskowe w swoim skrypcie Python**: W swoim skrypcie Pythona użyj pakietu `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Załaduj zmienne środowiskowe z pliku .env
   load_dotenv()

   # Uzyskaj dostęp do zmiennej GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To wszystko! Pomyślnie utworzyłeś plik `.env`, dodałeś swój token GitHub i załadowałeś go do aplikacji Python.

## Jak uruchomić lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na swoim komputerze, musisz mieć zainstalowaną jakąś wersję [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Następnie, aby używać repozytorium, musisz je sklonować:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Gdy już wszystko masz, możesz zacząć!

## Kroki opcjonalne

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.  
Sama Conda jest menedżerem pakietów, który ułatwia tworzenie i przełączanie między różnymi środowiskami wirtualnymi Pythona ([**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)) i pakietami. Przydaje się też do instalacji pakietów niedostępnych przez `pip`.

Możesz skorzystać z [instrukcji instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po zainstalowaniu Miniconda, musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś).

Następnie musisz utworzyć środowisko wirtualne. Aby to zrobić za pomocą Conda, utwórz plik środowiska (_environment.yml_). Jeśli korzystasz z Codespaces, umieść go w katalogu `.devcontainer`, czyli `.devcontainer/environment.yml`.

Uzupełnij plik środowiska podanym poniżej fragmentem:

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

Jeśli pojawiają się błędy używając conda, możesz ręcznie zainstalować Microsoft AI Libraries za pomocą następującego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska definiuje wymagane zależności. `<environment-name>` to nazwa środowiska Conda, którą chcesz użyć, a `<python-version>` to wersja Pythona, na przykład `3` oznacza najnowszą główną wersję.

Po tym możesz utworzyć środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Podścieżka .devcontainer dotyczy tylko konfiguracji Codespace
conda activate ai4beg
```

Jeśli napotkasz problemy, zapoznaj się z [instrukcją obsługi środowisk Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Korzystanie z Visual Studio Code z rozszerzeniem do Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia dla Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) do tego kursu. Jest to jednak rekomendacja, a nie wymóg obligatoryjny.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, możesz skonfigurować projekt wewnątrz kontenera. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Później omówimy to dokładniej.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, edytor automatycznie zasugeruje instalację rozszerzenia wsparcia dla Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę propozycję, aby korzystać z lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz też pracować nad projektem za pomocą środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko do rozwoju z funkcjami takimi jak automatyczne uzupełnianie, podświetlanie składni itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza polecenia, nawiguj do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a adres URL dostępu pojawi się w oknie wiersza poleceń.

Po wejściu pod ten adres URL zobaczysz konspekt kursu i będziesz mógł nawigować do dowolnego pliku `*.ipynb`, np. `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą do konfiguracji wszystkiego na komputerze lub w Codespace jest użycie [kontenera](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces wymaga to instalacji Dockera i trochę pracy, więc polecamy to tylko osobom z doświadczeniem w pracy z kontenerami.

Jednym z najlepszych sposobów na bezpieczne przechowywanie kluczy API podczas korzystania z GitHub Codespaces jest używanie sekretów Codespace. Prosimy zapoznać się z przewodnikiem [zarządzania sekretami w Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekcje i wymagania techniczne

Kurs zawiera 6 lekcji koncepcyjnych i 6 lekcji programowania.

Do lekcji programowania korzystamy z Azure OpenAI Service. Będziesz potrzebować dostępu do usługi Azure OpenAI oraz klucza API, aby uruchomić ten kod. Możesz złożyć wniosek o dostęp, [wypełniając ten formularz](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

W czasie oczekiwania na przetworzenie wniosku każda lekcja programowania zawiera także plik `README.md`, gdzie możesz zobaczyć kod i wyniki.

## Korzystanie z Azure OpenAI Service po raz pierwszy

Jeśli korzystasz z Azure OpenAI service po raz pierwszy, postępuj zgodnie z tym przewodnikiem, jak [utworzyć i wdrożyć zasób Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie z OpenAI API po raz pierwszy

Jeśli korzystasz z OpenAI API po raz pierwszy, zapoznaj się z przewodnikiem jak [utworzyć i korzystać z interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spotkaj innych uczniów

Stworzyliśmy kanały na naszym oficjalnym serwerze Discord [AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), gdzie możesz poznać innych uczestników kursu. To świetny sposób na nawiązywanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i osobami, które chcą rozwijać się w zakresie Generative AI.

[![Dołącz do kanału discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektu także będzie dostępny na tym serwerze Discord, aby pomagać uczestnikom.

## Współtworzenie

Ten kurs to inicjatywa open-source. Jeśli zauważysz miejsca do poprawy lub błędy, prosimy o utworzenie [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoszenie [issues na GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektu śledzi wszystkie wkłady. Współtworzenie open-source to świetny sposób na rozwijanie kariery w Generative AI.

Większość wkładów wymaga zaakceptowania Contributor License Agreement (CLA), który oświadcza, że masz prawo i faktycznie udzielasz nam praw do wykorzystania swojego wkładu. Szczegóły znajdziesz na stronie [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: przy tłumaczeniu tekstów w tym repozytorium prosimy o niekorzystanie z tłumaczeń maszynowych. Weryfikujemy tłumaczenia społecznościowo, więc prosimy zgłaszać się tylko do tłumaczeń na języki, w których jesteś biegły.

Po złożeniu pull requesta, bot CLA automatycznie zweryfikuje, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Po prostu postępuj zgodnie z instrukcjami bota. Robisz to tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

Ten projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Więcej informacji znajdziesz w FAQ Kodeksu Postępowania lub możesz kontaktować się przez [Email opencode](opencode@microsoft.com) w razie pytań lub uwag.

## Zaczynajmy!
Teraz, gdy ukończyłeś niezbędne kroki, aby ukończyć ten kurs, zacznijmy od [wprowadzenia do Generatywnej SI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->