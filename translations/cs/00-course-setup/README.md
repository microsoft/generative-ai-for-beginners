<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:15:57+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Začínáme s tímto kurzem

Jsme nadšeni, že začínáte tento kurz a uvidíte, co vás inspiruje vytvořit s Generativní AI!

Abychom vám zajistili úspěch, tato stránka shrnuje kroky nastavení, technické požadavky a kde získat pomoc, pokud ji budete potřebovat.

## Kroky nastavení

Pro zahájení kurzu je potřeba dokončit následující kroky.

### 1. Vytvořte fork tohoto repozitáře

[Vytvořte fork celého tohoto repozitáře](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svůj vlastní GitHub účet, abyste mohli měnit kód a plnit úkoly. Můžete také [označit (🌟) tento repozitář hvězdičkou](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), abyste jej a související repozitáře snáze našli.

### 2. Vytvořte codespace

Aby se předešlo problémům s závislostmi při spouštění kódu, doporučujeme spouštět tento kurz v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Codespace vytvoříte výběrem možnosti `Code` ve vašem forku tohoto repozitáře a následným výběrem možnosti **Codespaces**.

![Dialog zobrazující tlačítka pro vytvoření codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Ukládání vašich API klíčů

Je důležité uchovávat vaše API klíče v bezpečí při tvorbě jakékoliv aplikace. Doporučujeme neukládat API klíče přímo v kódu. Pokud byste tyto údaje nahráli do veřejného repozitáře, mohlo by to vést k bezpečnostním problémům a dokonce i nežádoucím nákladům, pokud by je zneužil někdo nepovolaný.  
Zde je krok za krokem návod, jak vytvořit soubor `.env` pro Python a přidat `GITHUB_TOKEN`:

1. **Přejděte do adresáře vašeho projektu**: Otevřete terminál nebo příkazový řádek a přejděte do kořenového adresáře projektu, kde chcete vytvořit soubor `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Vytvořte soubor `.env`**: Použijte svůj oblíbený textový editor k vytvoření nového souboru s názvem `.env`. Pokud používáte příkazový řádek, můžete použít `touch` (na systémech Unix) nebo `echo` (na Windows):

   Unixové systémy:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Upravte soubor `.env`**: Otevřete `.env` v textovém editoru (např. VS Code, Notepad++ nebo jiný editor). Přidejte následující řádek, kde `your_github_token_here` nahraďte svým skutečným GitHub tokenem:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Uložte soubor**: Uložte změny a zavřete editor.

5. **Nainstalujte `python-dotenv`**: Pokud jste tak ještě neučinili, nainstalujte balíček `python-dotenv`, který umožní načítat proměnné prostředí ze souboru `.env` do vaší Python aplikace. Instalaci provedete pomocí `pip`:

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

A je to! Úspěšně jste vytvořili soubor `.env`, přidali GitHub token a načetli ho do Python aplikace.

## Jak spustit lokálně na vašem počítači

Pro spuštění kódu lokálně na vašem počítači je potřeba mít nainstalovanou nějakou verzi [Pythonu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Repozitář pak musíte naklonovat:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Jakmile máte vše připraveno, můžete začít!

## Volitelné kroky

### Instalace Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lehký instalátor pro instalaci [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonu a několika balíčků.  
Conda je správce balíčků, který usnadňuje nastavení a přepínání mezi různými Python [**virtuálními prostředími**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) a balíčky. Hodí se také pro instalaci balíčků, které nejsou dostupné přes `pip`.

Postupujte podle [návodu na instalaci MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Po instalaci Miniconda je potřeba naklonovat [repozitář](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (pokud jste tak ještě neučinili).

Dále je potřeba vytvořit virtuální prostředí. Pro Conda vytvořte nový soubor prostředí (_environment.yml_). Pokud pracujete v Codespaces, vytvořte ho v adresáři `.devcontainer`, tedy `.devcontainer/environment.yml`.

Vyplňte soubor prostředí následujícím úryvkem:

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

Pokud při používání conda narazíte na chyby, můžete ručně nainstalovat Microsoft AI knihovny pomocí následujícího příkazu v terminálu.

```
conda install -c microsoft azure-ai-ml
```

Soubor prostředí specifikuje závislosti, které potřebujeme. `<environment-name>` je název, který chcete použít pro své Conda prostředí, a `<python-version>` je verze Pythonu, kterou chcete použít, například `3` je nejnovější hlavní verze Pythonu.

Po dokončení můžete vytvořit Conda prostředí spuštěním příkazů níže v příkazovém řádku/terminálu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pokud narazíte na problémy, podívejte se na [návod k Conda prostředím](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Použití Visual Studio Code s rozšířením pro Python

Pro tento kurz doporučujeme používat editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) s nainstalovaným [rozšířením pro Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Jedná se však spíše o doporučení než o povinnou podmínku.

> **Poznámka**: Otevřením repozitáře kurzu ve VS Code máte možnost nastavit projekt v kontejneru. Je to díky [speciálnímu adresáři `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitáři kurzu. O tom více později.

> **Poznámka**: Po naklonování a otevření adresáře ve VS Code vám editor automaticky nabídne instalaci rozšíření pro Python.

> **Poznámka**: Pokud vám VS Code nabídne znovu otevřít repozitář v kontejneru, odmítněte tuto nabídku, pokud chcete používat lokálně nainstalovanou verzi Pythonu.

### Použití Jupyter v prohlížeči

Na projektu můžete pracovat také pomocí prostředí [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) přímo ve vašem prohlížeči. Klasický Jupyter i [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) poskytují příjemné vývojové prostředí s funkcemi jako automatické doplňování, zvýraznění kódu a další.

Pro spuštění Jupyter lokálně otevřete terminál/příkazový řádek, přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```

nebo

```bash
jupyterhub
```

Tím se spustí instance Jupyter a URL pro přístup k ní se zobrazí v okně příkazového řádku.

Po přístupu na URL byste měli vidět osnovu kurzu a můžete procházet jakýkoliv soubor `*.ipynb`. Například `08-building-search-applications/python/oai-solution.ipynb`.

### Spuštění v kontejneru

Alternativou k nastavení všeho na vašem počítači nebo v Codespace je použití [kontejneru](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Speciální složka `.devcontainer` v repozitáři kurzu umožňuje VS Code nastavit projekt v kontejneru. Mimo Codespaces to vyžaduje instalaci Dockeru a upřímně řečeno, je to trochu složitější, proto to doporučujeme jen zkušenějším uživatelům pracujícím s kontejnery.

Jedním z nejlepších způsobů, jak zabezpečit vaše API klíče při používání GitHub Codespaces, je využití Codespace Secrets. Podívejte se na průvodce [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pro více informací.

## Lekce a technické požadavky

Kurz obsahuje 6 konceptuálních lekcí a 6 lekcí s kódováním.

Pro lekce s kódováním používáme Azure OpenAI Service. Budete potřebovat přístup k Azure OpenAI službě a API klíč pro spuštění kódu. Přístup můžete získat [vyplněním této žádosti](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Zatímco čekáte na zpracování žádosti, každá lekce s kódováním obsahuje také soubor `README.md`, kde můžete prohlížet kód a výstupy.

## Použití Azure OpenAI Service poprvé

Pokud s Azure OpenAI službou pracujete poprvé, postupujte podle tohoto návodu, jak [vytvořit a nasadit Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Použití OpenAI API poprvé

Pokud s OpenAI API pracujete poprvé, postupujte podle návodu, jak [vytvořit a používat rozhraní.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Seznamte se s ostatními studenty

Vytvořili jsme kanály v našem oficiálním [AI Community Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pro setkávání s ostatními studenty. Je to skvělý způsob, jak navázat kontakty s dalšími podnikateli, tvůrci, studenty a všemi, kdo chtějí posunout své znalosti v Generativní AI na vyšší úroveň.

[![Připojit se na discord kanál](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Tým projektu bude také na tomto Discord serveru, aby pomáhal studentům.

## Přispívejte

Tento kurz je open-source iniciativa. Pokud vidíte možnosti zlepšení nebo chyby, vytvořte prosím [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) nebo nahlaste [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Tým projektu sleduje všechny příspěvky. Přispívání do open source je skvělý způsob, jak rozvíjet svou kariéru v Generativní AI.

Většina příspěvků vyžaduje souhlas s Contributor License Agreement (CLA), který potvrzuje, že máte právo a skutečně udělujete práva k použití vašeho příspěvku. Podrobnosti najdete na [webu CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Důležité: při překladu textu v tomto repozitáři prosím nepoužívejte strojový překlad. Překlady budou ověřovány komunitou, proto se přihlašujte pouze na překlady do jazyků, ve kterých jste zdatní.

Po odeslání pull requestu CLA-bot automaticky zjistí, zda je potřeba poskytnout CLA, a označí PR odpovídajícím způsobem (např. štítek, komentář). Stačí postupovat podle pokynů bota. Toto je potřeba udělat pouze jednou pro všechny repozitáře využívající náš CLA.

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pro více informací si přečtěte FAQ ke Kodexu chování nebo kontaktujte [Email opencode](opencode@microsoft.com) s případnými dotazy či připomínkami.

## Pojďme začít

Nyní, když jste dokončili potřebné kroky pro absolvování kurzu, pojďme začít s [úvodem do Generativní AI a LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.