<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T00:53:04+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pl"
}
-->
# Rozpoczęcie kursu

Jesteśmy bardzo podekscytowani, że zaczynasz ten kurs i nie możemy się doczekać, aby zobaczyć, co zainspiruje Cię do stworzenia z Generative AI!

Aby zapewnić Ci sukces, na tej stronie znajdziesz kroki konfiguracji, wymagania techniczne oraz informacje, gdzie szukać pomocy w razie potrzeby.

## Kroki konfiguracji

Aby rozpocząć kurs, musisz wykonać następujące kroki.

### 1. Zforkuj to repozytorium

[Zforkuj całe repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na swoje konto GitHub, aby móc zmieniać kod i realizować wyzwania. Możesz również [dodać gwiazdkę (🌟) do tego repozytorium](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), aby łatwiej je znaleźć oraz powiązane repozytoria.

### 2. Utwórz Codespace

Aby uniknąć problemów z zależnościami podczas uruchamiania kodu, zalecamy korzystanie z [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

W swoim forku: **Code -> Codespaces -> New on main**

![Okno dialogowe pokazujące przyciski do utworzenia Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Dodaj sekret

1. ⚙️ Ikona koła zębatego -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nazwij OPENAI_API_KEY, wklej swój klucz, Zapisz.

### 3. Co dalej?

| Chcę…               | Przejdź do…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Rozpocząć Lekcję 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Pracować offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Skonfigurować dostawcę LLM | [`providers.md`](03-providers.md)                                        |
| Poznać innych uczestników | [Dołącz do naszego Discorda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Rozwiązywanie problemów

| Objaw                                    | Rozwiązanie                                                    |
|------------------------------------------|----------------------------------------------------------------|
| Budowa kontenera trwa > 10 minut         | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`              | Terminal nie został podłączony; kliknij **+** ➜ *bash*         |
| `401 Unauthorized` od OpenAI             | Nieprawidłowy / wygasły `OPENAI_API_KEY`                       |
| VS Code pokazuje “Dev container mounting…” | Odśwież kartę przeglądarki—Codespaces czasami traci połączenie |
| Brak kernela w notebooku                 | Menu notebooka ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

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

5. **Zainstaluj `python-dotenv`**: Jeśli jeszcze tego nie zrobiłeś, musisz zainstalować pakiet `python-dotenv`, aby załadować zmienne środowiskowe z pliku `.env` do swojej aplikacji Python. Możesz go zainstalować za pomocą `pip`:

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

Gdy wszystko będzie gotowe, możesz zacząć!

## Opcjonalne kroki

### Instalacja Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) to lekki instalator do instalacji [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona oraz kilku pakietów.
Conda to menedżer pakietów, który ułatwia konfigurację i przełączanie między różnymi [**wirtualnymi środowiskami**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Pythona i pakietami. Jest również przydatny do instalacji pakietów, które nie są dostępne przez `pip`.

Możesz skorzystać z [przewodnika instalacji MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), aby go skonfigurować.

Po zainstalowaniu Miniconda musisz sklonować [repozytorium](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jeśli jeszcze tego nie zrobiłeś).

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

Jeśli napotkasz błędy podczas korzystania z Conda, możesz ręcznie zainstalować biblioteki Microsoft AI za pomocą następującego polecenia w terminalu.

```
conda install -c microsoft azure-ai-ml
```

Plik środowiska określa wymagane zależności. `<environment-name>` odnosi się do nazwy, której chcesz użyć dla swojego środowiska Conda, a `<python-version>` to wersja Pythona, której chcesz użyć, na przykład `3` to najnowsza główna wersja Pythona.

Po wykonaniu tych kroków możesz utworzyć swoje środowisko Conda, uruchamiając poniższe polecenia w wierszu poleceń/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Zapoznaj się z [przewodnikiem dotyczącym środowisk Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), jeśli napotkasz jakiekolwiek problemy.

### Korzystanie z Visual Studio Code z rozszerzeniem wsparcia dla Pythona

Zalecamy korzystanie z edytora [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z zainstalowanym [rozszerzeniem wsparcia dla Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) podczas tego kursu. Jest to jednak bardziej zalecenie niż wymóg.

> **Uwaga**: Otwierając repozytorium kursu w VS Code, masz możliwość skonfigurowania projektu w kontenerze. Jest to możliwe dzięki [specjalnemu katalogowi `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) znajdującemu się w repozytorium kursu. Więcej na ten temat później.

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zasugeruje on instalację rozszerzenia wsparcia dla Pythona.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, odrzuć tę propozycję, aby używać lokalnie zainstalowanej wersji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz również pracować nad projektem, korzystając ze środowiska [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) bezpośrednio w przeglądarce. Zarówno klasyczny Jupyter, jak i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferują przyjemne środowisko programistyczne z funkcjami takimi jak autouzupełnianie, podświetlanie kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do terminala/wiersza poleceń, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```

lub

```bash
jupyterhub
```

To uruchomi instancję Jupyter, a URL do jej dostępu zostanie pokazany w oknie wiersza poleceń.

Po uzyskaniu dostępu do URL, powinieneś zobaczyć plan kursu i móc przejść do dowolnego pliku `*.ipynb`. Na przykład, `08-building-search-applications/python/oai-solution.ipynb`.

### Uruchamianie w kontenerze

Alternatywą dla konfiguracji wszystkiego na komputerze lub w Codespace jest użycie [kontenera](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specjalny folder `.devcontainer` w repozytorium kursu umożliwia VS Code skonfigurowanie projektu w kontenerze. Poza Codespaces, wymaga to instalacji Dockera i, szczerze mówiąc, wiąże się z pewnym nakładem pracy, więc zalecamy to tylko osobom z doświadczeniem w pracy z kontenerami.

Jednym z najlepszych sposobów na zabezpieczenie kluczy API podczas korzystania z GitHub Codespaces jest użycie Codespace Secrets. Proszę zapoznać się z przewodnikiem [Zarządzanie sekretami Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), aby dowiedzieć się więcej na ten temat.

## Lekcje i wymagania techniczne

Kurs składa się z 6 lekcji koncepcyjnych i 6 lekcji programistycznych.

W przypadku lekcji programistycznych korzystamy z usługi Azure OpenAI Service. Aby uruchomić ten kod, będziesz potrzebować dostępu do usługi Azure OpenAI oraz klucza API. Możesz ubiegać się o dostęp, [wypełniając ten formularz](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Podczas oczekiwania na przetworzenie wniosku, każda lekcja programistyczna zawiera również plik `README.md`, w którym możesz zobaczyć kod i wyniki.

## Korzystanie z usługi Azure OpenAI Service po raz pierwszy

Jeśli po raz pierwszy korzystasz z usługi Azure OpenAI, zapoznaj się z tym przewodnikiem, jak [utworzyć i wdrożyć zasób usługi Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Korzystanie z OpenAI API po raz pierwszy

Jeśli po raz pierwszy korzystasz z OpenAI API, zapoznaj się z przewodnikiem, jak [utworzyć i używać interfejsu.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Poznaj innych uczestników

Stworzyliśmy kanały na naszym oficjalnym [serwerze Discord społeczności AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), aby umożliwić spotkania z innymi uczestnikami. To świetny sposób na nawiązanie kontaktów z innymi przedsiębiorcami, twórcami, studentami i wszystkimi, którzy chcą rozwijać się w Generative AI.

[![Dołącz do kanału Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Zespół projektowy również będzie obecny na tym serwerze Discord, aby pomóc uczestnikom.

## Współtworzenie

Ten kurs jest inicjatywą open-source. Jeśli zauważysz obszary do poprawy lub problemy, utwórz [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) lub zgłoś [problem na GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Zespół projektowy będzie śledził wszystkie wkłady. Współtworzenie open source to niesamowity sposób na rozwój kariery w Generative AI.

Większość wkładów wymaga od Ciebie zgody na Umowę Licencyjną Współtwórcy (CLA), która potwierdza, że masz prawo i faktycznie udzielasz nam prawa do korzystania z Twojego wkładu. Szczegóły znajdziesz na stronie [Umowa Licencyjna Współtwórcy CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Ważne: tłumacząc tekst w tym repozytorium, upewnij się, że nie korzystasz z tłumaczenia maszynowego. Zweryfikujemy tłumaczenia za pośrednictwem społeczności, więc prosimy o zgłaszanie się do tłumaczeń tylko w językach, w których jesteś biegły.

Gdy prześlesz pull request, bot CLA automatycznie określi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. etykietą, komentarzem). Wystarczy postępować zgodnie z instrukcjami podanymi przez bota. Będziesz musiał to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

Ten projekt przyjął [Kodeks postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Aby uzyskać więcej informacji, przeczytaj FAQ dotyczące Kodeksu Postępowania lub skontaktuj się z [Email opencode](opencode@microsoft.com), jeśli masz dodatkowe pytania lub uwagi.

## Zaczynajmy!
Teraz, gdy ukończyłeś wymagane kroki, aby zakończyć ten kurs, zacznijmy od [wprowadzenia do Generatywnej AI i LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.