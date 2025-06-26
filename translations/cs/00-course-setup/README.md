<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:58:15+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Začínáme s tímto kurzem

Jsme velmi nadšení, že začínáte tento kurz, a těšíme se, co vás inspiruje k vytvoření s Generativní AI!

Abychom zajistili váš úspěch, tato stránka uvádí kroky k nastavení, technické požadavky a kde získat pomoc, pokud je potřeba.

## Kroky nastavení

Abyste mohli začít s tímto kurzem, je třeba dokončit následující kroky.

### 1. Forkněte tento Repo

[Forkněte celý tento repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svůj vlastní GitHub účet, abyste mohli měnit jakýkoliv kód a splnit výzvy. Můžete také [označit hvězdičkou (🌟) tento repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste ho a související repozitáře snadněji našli.

### 2. Vytvořte codespace

Abychom se vyhnuli problémům se závislostmi při spouštění kódu, doporučujeme spustit tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To lze vytvořit výběrem možnosti `Code` na vaší forkované verzi tohoto repo a výběrem možnosti **Codespaces**.

![Dialog ukazující tlačítka pro vytvoření codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Uložení vašich API klíčů

Je důležité udržet vaše API klíče bezpečné a zabezpečené při budování jakéhokoliv typu aplikace. Doporučujeme neukládat žádné API klíče přímo do vašeho kódu. Zveřejnění těchto údajů v veřejném repozitáři by mohlo vést k bezpečnostním problémům a dokonce k nežádoucím nákladům, pokud je použije škodlivý aktér.
Zde je průvodce krok za krokem, jak vytvořit soubor `.env` pro Python a přidat `GITHUB_TOKEN`:

1. **Přejděte do adresáře vašeho projektu**: Otevřete svůj terminál nebo příkazový řádek a přejděte do kořenového adresáře vašeho projektu, kde chcete vytvořit soubor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte soubor `.env`**: Použijte svůj oblíbený textový editor k vytvoření nového souboru nazvaného `.env`. Pokud používáte příkazový řádek, můžete použít `touch` (on Unix-based systems) or `echo` (na Windows):

   Systémy založené na Unixu:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiný editor). Přidejte následující řádek do souboru, nahraďte `your_github_token_here` vaším skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte balíček `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`, abyste mohli načítat proměnné prostředí ze souboru `.env` do vaší Python aplikace. Můžete jej nainstalovat pomocí `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Načtěte proměnné prostředí ve vašem Python skriptu**: Ve vašem Python skriptu použijte balíček `python-dotenv` k načtení proměnných prostředí ze souboru `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je vše! Úspěšně jste vytvořili soubor `.env`, přidali svůj GitHub token a načetli jej do své Python aplikace.

## Jak spustit lokálně na vašem počítači

Abyste mohli kód spustit lokálně na vašem počítači, potřebujete mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Poté je třeba repozitář klonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše staženo, můžete začít!

## Volitelné kroky

### Instalace Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, stejně jako několika balíčků.
Conda sama je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Také se hodí pro instalaci balíčků, které nejsou dostupné přes `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Pokračujte a naplňte svůj soubor prostředí úryvkem níže:

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

Pokud narazíte na chyby při používání conda, můžete ručně nainstalovat Microsoft AI Libraries pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je nejnovější hlavní verze Pythonu.

Jakmile je to hotovo, můžete pokračovat a vytvořit své Conda prostředí spuštěním příkazů níže ve vašem příkazovém řádku/terminálu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pokud narazíte na problémy, odkazujte na [průvodce prostředími Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením pro podporu Pythonu

Doporučujeme používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pro tento kurz. Toto je však spíše doporučení a ne definitivní požadavek.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt uvnitř kontejneru. To je kvůli [speciálnímu adresáři `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) nalezeném v repozitáři kurzu. Více o tom později.

> **Poznámka**: Jakmile klonujete a otevřete adresář ve VS Code, automaticky vám doporučí nainstalovat rozšíření pro podporu Pythonu.

> **Poznámka**: Pokud vám VS Code doporučí znovu otevřít repozitář v kontejneru, odmítněte tuto žádost, abyste použili lokálně nainstalovanou verzi Pythonu.

### Použití Jupyter v prohlížeči

Můžete také pracovat na projektu pomocí [Jupyter prostředí](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve vašem prohlížeči. Jak klasický Jupyter, tak [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují velmi příjemné vývojové prostředí s funkcemi jako automatické dokončování, zvýraznění kódu, atd.

Chcete-li spustit Jupyter lokálně, přejděte do terminálu/příkazového řádku, přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

To spustí instanci Jupyteru a URL pro přístup k ní bude zobrazena v okně příkazového řádku.

Jakmile přistoupíte na URL, měli byste vidět osnovu kurzu a být schopni navigovat na jakýkoliv soubor `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kde můžete vidět kód a výstupy.

## Použití Azure OpenAI služby poprvé

Pokud je to poprvé, co pracujete s Azure OpenAI službou, prosím, následujte tento průvodce, jak [vytvořit a nasadit Azure OpenAI Service zdroj.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použití OpenAI API poprvé

Pokud je to poprvé, co pracujete s OpenAI API, prosím, následujte průvodce, jak [vytvořit a používat rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními studenty

Vytvořili jsme kanály na našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro setkání s ostatními studenty. Je to skvělý způsob, jak se spojit s dalšími podobně smýšlejícími podnikateli, tvůrci, studenty a každým, kdo chce zlepšit své dovednosti v Generativní AI.

[![Připojte se k discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tým bude také na tomto Discord serveru, aby pomohl všem studentům.

## Přispějte

Tento kurz je iniciativa s otevřeným zdrojovým kódem. Pokud vidíte oblasti pro zlepšení nebo problémy, prosím, vytvořte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo zaregistrujte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tým bude sledovat všechny příspěvky. Přispívání do open source je úžasný způsob, jak budovat svou kariéru v Generativní AI.

Většina příspěvků vyžaduje, abyste souhlasili s Licenční smlouvou pro přispěvatele (CLA), která deklaruje, že máte právo a skutečně nám udělujete práva používat váš příspěvek. Pro podrobnosti navštivte [CLA, webovou stránku Licenční smlouvy pro přispěvatele](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překladu textu v tomto repo prosím zajistěte, že nepoužíváte strojový překlad. Ověříme překlady prostřednictvím komunity, takže se prosím dobrovolně přihlaste k překladům pouze v jazycích, ve kterých jste zdatní.

Když podáte pull request, CLA-bot automaticky určí, zda potřebujete poskytnout CLA, a příslušně označí PR (např. štítek, komentář). Jednoduše následujte pokyny poskytované botem. Budete to muset udělat pouze jednou ve všech repozitářích používajících naše CLA.

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte FAQ Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s jakýmikoliv dalšími otázkami nebo komentáři.

## Začněme

Nyní, když jste dokončili potřebné kroky k dokončení tohoto kurzu, pojďme začít tím, že získáme [úvod do Generativní AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.