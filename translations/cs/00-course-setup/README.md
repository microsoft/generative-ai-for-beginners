<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:35:22+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Začínáme s tímto kurzem

Jsme velmi nadšeni, že začínáte tento kurz a těšíme se, co vás inspiruje k vytvoření pomocí Generativní AI!

Abychom zajistili váš úspěch, tato stránka obsahuje kroky k nastavení, technické požadavky a informace o tom, kde získat pomoc, pokud je potřeba.

## Kroky nastavení

Abyste mohli začít tento kurz, budete muset dokončit následující kroky.

### 1. Forkujte tento repo

[Forkujte celý tento repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svůj vlastní GitHub účet, abyste mohli měnit jakýkoliv kód a plnit výzvy. Můžete také [označit (🌟) tento repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pro snadnější nalezení tohoto a souvisejících repozitářů.

### 2. Vytvořte codespace

Aby se předešlo problémům se závislostmi při spuštění kódu, doporučujeme tento kurz spustit v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To lze vytvořit výběrem možnosti `Code` na vaší forkované verzi tohoto repo a výběrem možnosti **Codespaces**.

![Dialog ukazující tlačítka pro vytvoření codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Uložení vašich API klíčů

Udržení vašich API klíčů v bezpečí je důležité při vytváření jakékoliv aplikace. Doporučujeme neukládat žádné API klíče přímo do vašeho kódu. Závazek těchto detailů do veřejného repozitáře by mohl vést k bezpečnostním problémům a dokonce k nežádoucím nákladům, pokud by byly použity špatným aktérem. Zde je krok za krokem návod, jak vytvořit soubor `.env` pro Python a přidat `GITHUB_TOKEN`:

1. **Navigujte do adresáře vašeho projektu**: Otevřete svůj terminál nebo příkazový řádek a přejděte do kořenového adresáře vašeho projektu, kde chcete vytvořit soubor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte soubor `.env`**: Použijte svůj preferovaný textový editor k vytvoření nového souboru s názvem `.env`. Pokud používáte příkazový řádek, můžete použít `touch` (on Unix-based systems) or `echo` (na Windows):

   Systémy založené na Unixu:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete soubor `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiném editoru). Přidejte následující řádek do souboru, nahraďte `your_github_token_here` vaším skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete textový editor.

5. **Nainstalujte balíček `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` pro načtení proměnných prostředí ze souboru `.env` do vaší Python aplikace. Můžete ho nainstalovat pomocí `pip`:

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

To je vše! Úspěšně jste vytvořili soubor `.env`, přidali svůj GitHub token a načetli ho do vaší Python aplikace.

## Jak spustit lokálně na vašem počítači

Aby bylo možné spustit kód lokálně na vašem počítači, budete potřebovat mít nějakou verzi [Pythonu nainstalovanou](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Abyste pak mohli použít repozitář, musíte ho naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše zkontrolováno, můžete začít!

## Volitelné kroky

### Instalace Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu, stejně jako několika balíčků.
Conda sama o sobě je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Také se hodí pro instalaci balíčků, které nejsou dostupné přes `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Pokračujte a naplňte svůj soubor prostředí níže uvedeným úryvkem:

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

Pokud zjistíte, že se vám objevují chyby při používání conda, můžete ručně nainstalovat Microsoft AI knihovny pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` je poslední hlavní verze Pythonu.

Jakmile je to hotové, můžete pokračovat a vytvořit své Conda prostředí spuštěním následujících příkazů ve vašem příkazovém řádku/terminálu

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Odkazujte na [Conda průvodce prostředími](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) pokud narazíte na nějaké problémy.

### Použití Visual Studio Code s rozšířením pro podporu Pythonu

Doporučujeme použít editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro podporu Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pro tento kurz. To je však spíše doporučení než nezbytný požadavek.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt uvnitř kontejneru. To je kvůli [speciální `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) adresáři nalezeném v repozitáři kurzu. Více o tom později.

> **Poznámka**: Jakmile naklonujete a otevřete adresář ve VS Code, automaticky vám doporučí nainstalovat rozšíření pro podporu Pythonu.

> **Poznámka**: Pokud vám VS Code doporučí znovu otevřít repozitář v kontejneru, odmítněte tuto žádost, abyste mohli použít lokálně nainstalovanou verzi Pythonu.

### Použití Jupyter v prohlížeči

Můžete také pracovat na projektu pomocí [Jupyter prostředí](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve vašem prohlížeči. Jak klasický Jupyter, tak [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují velmi příjemné vývojové prostředí s funkcemi jako automatické doplňování, zvýraznění kódu, atd.

Abyste mohli spustit Jupyter lokálně, přejděte do terminálu/příkazového řádku, navigujte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

To spustí instanci Jupyter a URL pro přístup k ní bude zobrazeno v okně příkazového řádku.

Jakmile přistoupíte k URL, měli byste vidět osnovu kurzu a být schopni navigovat k jakémukoliv souboru `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`, kde můžete zobrazit kód a výstupy.

## Použití Azure OpenAI služby poprvé

Pokud je to vaše první zkušenost s Azure OpenAI službou, prosím, postupujte podle tohoto průvodce, jak [vytvořit a nasadit zdroj Azure OpenAI služby.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použití OpenAI API poprvé

Pokud je to vaše první zkušenost s OpenAI API, prosím, postupujte podle průvodce, jak [vytvořit a použít rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními účastníky

Vytvořili jsme kanály na našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro setkání s ostatními účastníky. To je skvělý způsob, jak se propojit s ostatními podobně smýšlejícími podnikateli, tvůrci, studenty a kýmkoliv, kdo se chce zlepšit v Generativní AI.

[![Připojte se k discord kanálu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektový tým bude také na tomto Discord serveru, aby pomohl všem účastníkům.

## Přispějte

Tento kurz je iniciativa s otevřeným zdrojovým kódem. Pokud vidíte oblasti ke zlepšení nebo problémy, prosím, vytvořte [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo zaznamenejte [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektový tým bude sledovat všechny příspěvky. Přispívání do open source je úžasný způsob, jak budovat svou kariéru v Generativní AI.

Většina příspěvků vyžaduje, abyste souhlasili s Licenční smlouvou přispěvatele (CLA), která prohlašuje, že máte právo a skutečně nám udělujete práva na použití vašeho příspěvku. Podrobnosti naleznete na [CLA, webové stránce Licenční smlouvy přispěvatele](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překládání textu v tomto repo, prosím, zajistěte, že nepoužíváte strojový překlad. Překlady ověříme prostřednictvím komunity, takže prosím dobrovolně přispívejte překlady pouze v jazycích, kde jste zdatní.

Když odešlete pull request, CLA-bot automaticky určí, zda potřebujete poskytnout CLA a přiměřeně označí PR (např. štítek, komentář). Jednoduše postupujte podle pokynů poskytnutých botem. Toto budete muset udělat pouze jednou ve všech repozitářích používajících naši CLA.

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte FAQ Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s jakýmikoliv dalšími otázkami nebo komentáři.

## Začněme

Nyní, když jste dokončili potřebné kroky k dokončení tohoto kurzu, začněme s [úvodem do Generativní AI a LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Upozornění**:
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, prosíme, vezměte na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.